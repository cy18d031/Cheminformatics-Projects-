# QSAR Modeling Pipeline

**Colab-ready — RDKit + scikit-learn**

---

## Overview

This repository hosts a complete **QSAR (Quantitative Structure–Activity Relationship)** modeling pipeline implemented in Python for **Google Colab**. It is designed to showcase high-level computational chemistry and cheminformatics skills, including dataset curation, descriptor generation, machine learning model training, evaluation, and prediction.

The pipeline is optimized for reproducibility, modularity, and professional presentation — ideal for portfolio demonstrations to recruiters or collaborators.

---

## Key Features

* Automated fetching of example bioactivity datasets (e.g., EGFR inhibitors) from public sources.
* RDKit-based molecular descriptor and fingerprint generation.
* Data cleaning, feature selection, and train/test splitting.
* Machine learning with Random Forest and XGBoost, using reproducible seeds.
* Model evaluation with R², RMSE, and visual diagnostics.
* Fully executable in Google Colab with one-click dependency installation.

---

## Files

* `QSAR_pipeline_colab.ipynb` — Main Colab notebook.
* `README.md` — Project documentation.
* `requirements.txt` — Optional pinned dependencies for local execution.
* `examples/` — Optional example datasets and outputs.

---

## How to Run (Google Colab)

1. Open `QSAR_pipeline_colab.ipynb` in Google Colab.
2. Run the first cell to install dependencies (`rdkit`, `scikit-learn`, `xgboost`, `pandas`, `matplotlib`).
3. Execute cells sequentially from top to bottom.

**Notes:**

* Replace the default dataset with any CSV containing `smiles` and a numeric activity column (e.g., `pIC50`).
* For large datasets, enable GPU acceleration in Colab for faster training.

---

## Example Results

* **R²:** 0.6–0.8 for clean, well-curated datasets.
* **RMSE:** Varies by dataset; visualizations include scatter plots and residual diagnostics.

---

## Extensibility

* Swap in Graph Neural Networks (PyTorch Geometric) for deep learning.
* Use advanced feature selection (LASSO, RFE).
* Implement cross-validation and Bayesian hyperparameter optimization.
* Integrate into docking or ADMET workflows.

---
