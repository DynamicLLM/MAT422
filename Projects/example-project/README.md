# Example MAT 422 Project

## Title
AI-Assisted Model Selection for Student Performance Prediction

## Software
Python 3.12, pandas, scikit-learn, matplotlib

## Problem
Given a dataset containing study hours, attendance, prior GPA, and assignment scores, predict whether a student will achieve a target final grade.

## Objective
Maximize predictive performance while maintaining a reproducible and interpretable workflow.

## Constraints
- Binary target
- No data leakage
- Five-fold cross-validation
- Compare at least two reasonable models
- Report accuracy, F1, and ROC-AUC

## Project workflow

```text
Problem + constraints
        ↓
Codex proposes candidate models
        ↓
Logistic regression + SVM
        ↓
Train / cross-validate
        ↓
Compare metrics
        ↓
Tune selected model
        ↓
Final validation
```

## Repository map

- `problem/`: problem statement and requirements
- `data/raw/`: original input data (use a public/sample dataset for the example)
- `data/processed/`: cleaned data used by the analysis
- `src/`: reusable Python source code
- `notebooks/`: exploratory analysis and model comparison
- `prompts/`: representative Codex prompts and iteration log
- `results/`: figures and tables used in the report
- `report/`: final report
- `software-info.md`: software and environment details

## How to run

1. Create the Python environment described in `requirements.txt`.
2. Run `notebooks/model-comparison.ipynb`.
3. Review outputs in `results/`.

This repository is a structural example. Students must use their own problem, data, analysis, and conclusions.
