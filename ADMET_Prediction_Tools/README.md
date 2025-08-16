# ADMET Prediction Tools

This project implements a simple pipeline for predicting **ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity)** properties of small molecules.

---

## Workflow
1. **Data Input**: Load molecules using SMILES strings.  
2. **Descriptor Calculation**: Generate molecular descriptors with RDKit.  
3. **Model Training**: Train machine learning models to predict ADMET properties.  
4. **Evaluation**: Assess model performance (R², RMSE, accuracy depending on property).  

---

## Run on Binder
Click below to launch the notebook interactively:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cy18d031/Cheminformatics-Projects-/main?filepath=ADMET_Prediction_Tools%2FADMET_Prediction_Tools.py)
