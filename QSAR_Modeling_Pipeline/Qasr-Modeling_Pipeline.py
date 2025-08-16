

# QSAR Modeling Pipeline using ChEMBL + RDKit

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from chembl_webresource_client.new_client import new_client

# -----------------------
# Fetching ChEMBL Data
# -----------------------

target_name = "EGFR"  # Example: Epidermal Growth Factor Receptor
target = new_client.target
target_id = target.search(target_name)[0]['target_chembl_id']
print("Target ChEMBL ID:", target_id)

# Get IC50 bioactivity data
activity = new_client.activity
data = activity.filter(target_chembl_id=target_id, standard_type="IC50")

# Convert to DataFrame
df = pd.DataFrame(data)
print(f"Fetched {len(df)} records for {target_name}")
df.head()

# -----------------------
# Computing Descriptors
# -----------------------

def calc_rdkit_desc(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return [func(mol) for _, func in Descriptors.descList]
    else:
        return None

desc_names = [name for name, _ in Descriptors.descList]
desc_data = []

for smi in df['smiles']:
    d = calc_rdkit_desc(smi)
    if d:
        desc_data.append(d)
    else:
        desc_data.append([np.nan]*len(desc_names))

desc_df = pd.DataFrame(desc_data, columns=desc_names)

# Merge descriptors with activity data
if "pIC50" in df.columns:
    full_df = pd.concat([df['pIC50'], desc_df], axis=1)
    full_df = full_df.dropna()
else:
    # Sometimes ChEMBL does not directly give pIC50, only IC50
    # Try converting IC50 to pIC50 if available
    if "standard_value" in df.columns:
        df["pIC50"] = -np.log10(df["standard_value"].astype(float) * 1e-9)
        full_df = pd.concat([df['pIC50'], desc_df], axis=1).dropna()
    else:
        raise ValueError("No IC50 or pIC50 values found in dataset.")

print(full_df.shape)
full_df.head()

# -----------------------
# QSAR Model Training
# -----------------------

X = full_df.drop(columns=['pIC50'])
y = full_df['pIC50']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² score: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")

# -----------------------
# Visualization
# -----------------------

plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)
plt.xlabel("Actual pIC50")
plt.ylabel("Predicted pIC50")
plt.title(f"QSAR Model (R²={r2:.2f}, RMSE={rmse:.2f})")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()