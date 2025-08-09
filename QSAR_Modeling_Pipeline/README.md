# QSAR Modeling Pipeline

**Colab-ready — RDKit + scikit-learn**

---

## Overview

This repository contains a polished, end-to-end **QSAR (Quantitative Structure–Activity Relationship)** modeling pipeline implemented in Python and designed to run in **Google Colab**. It demonstrates PhD-level computational work suitable for senior cheminformatics / computational chemistry roles: dataset curation, descriptor generation, model training (ensemble methods), evaluation, and prediction.

The notebook is structured for reproducibility, reusability, and quick inspection by recruiters or hiring managers.

---

## Key features

* Fetches open bioactivity data (example: EGFR inhibitors) and prepares it for modeling.
* Generates a broad set of RDKit molecular descriptors.
* Performs data cleaning, feature selection/aggregation, and train/test splitting.
* Trains robust ML models (Random Forest / XGBoost) with sensible defaults and reproducible seeds.
* Evaluates model performance (R², RMSE) and visualizes predicted vs actual values.
* Colab-ready: single notebook that installs dependencies and can be run end-to-end in one click.

---

## Files

* `QSAR_pipeline_colab.ipynb` — Main Colab notebook (recommended entry point).
* `README.md` — This file.
* `requirements.txt` — Optional pinned dependencies for local runs.
* `examples/` — Example input SMILES and sample predictions (optional).

---

## How to run (Google Colab)

1. Open the notebook `QSAR_pipeline_colab.ipynb` in Google Colab.
2. Run the first cell to install dependencies (RDKit, scikit-learn, xgboost, pandas, matplotlib).
3. Execute cells from top to bottom. The notebook is modular — you can skip to descriptor generation or modeling sections if desired.

**Notes:**

* The notebook downloads a curated public dataset (ChEMBL-derived CSV) for the example task. Replace with any other labeled bioactivity CSV that has `smiles` and a numeric activity column (e.g., `pIC50`).
* For larger datasets, enable GPU in Colab (Runtime > Change runtime type > GPU) to accelerate model training (especially for deep learning models).

---

## Recommended workflow for recruiters/interviewers

1. Inspect the dataset and descriptor summary (first analysis cells).
2. Run the model training and evaluation cells to reproduce performance metrics.
3. Review the `Modeling` section (hyperparameters and feature importances) to assess methodology rigor.
4. Optional: Replace the sample dataset with your own and run the inference cell.

---

## Example results (expected)

* **R²:** Typically in the range depending on dataset quality; example run gives R² ≈ 0.6–0.8 for well-curated targets.
* **RMSE:** Dataset-dependent; plots include predicted vs actual scatter and residual diagnostics.

Include exact numbers / plots from your current run in the notebook outputs — these will serve as immediate evidence of model quality in your GitHub repo.

---

## Extensibility

This pipeline is intentionally modular so you can extend it to:

* Graph Neural Networks (PyTorch Geometric) for structure-aware modeling.
* Feature selection (LASSO, recursive feature elimination).
* Cross-validation and nested hyperparameter tuning (Optuna / scikit-optimize).
* Integration into a larger virtual screening workflow (docking + ADMET filtering).

---

## Reproducibility & Licensing

* The notebook sets random seeds for reproducibility where applicable.
* **License:** MIT — modify as needed.

---

## Contact & Attribution

If you use or adapt this work, include a reference to the GitHub repo and optionally contact me via GitHub profile for questions or collaborations.

---

*Prepared as a flagship, recruiter-ready project showcasing senior-level cheminformatics and ML skills.*
