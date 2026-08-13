---
name: mat422-validation
description: Validate a model, design, or computational result against requirements, assumptions, diagnostics, and quantitative criteria.
---
# Validation and Verification Skill

Use this skill after code or software has been executed. Validation must be based on actual outputs, metrics, figures, tables, logs, or result files. Do not accept generated claims without evidence.

## Evidence to request

- Actual output files, metrics, logs, figures, tables, screenshots, or copied console output.
- Train/validation/test split details, cross-validation results, diagnostics, residual plots, sensitivity analysis, numerical checks, or constraint checks when applicable.
- Baseline or alternative model results when available.
- Error messages and corrections from diagnose-correct-rerun cycles.
- Software version, packages/toolboxes, and execution notes.

## Agent responsibilities

1. Compare results against the original success criteria and constraints.
2. Check assumptions and identify where assumptions remain unverified.
3. Evaluate quantitative performance using appropriate criteria: error, accuracy, F1/AUC, likelihood/information criteria, residual diagnostics, computational cost, feasibility, stability, or problem-specific metrics.
4. Check for data leakage, overfitting, incorrect splits, inappropriate preprocessing, invalid causal claims, numerical instability, or software execution issues.
5. Distinguish verified results from assumptions, estimates, or unverified claims.
6. Recommend additional checks when the evidence is insufficient.
7. Identify whether the project is ready for optimization/iteration or final reporting.

## Validation methods by task type

- Prediction/classification: train/validation/test separation, cross-validation, confusion matrix, ROC/AUC, F1, calibration, error analysis, leakage checks.
- Regression/inference: residual diagnostics, uncertainty, coefficient interpretation, model assumptions, robustness checks.
- Clustering/PCA/SVD: explained variance, reconstruction error, cluster diagnostics, interpretability, sensitivity to preprocessing.
- Optimization/design: objective value, feasibility, constraint satisfaction, sensitivity analysis, comparison to baseline design.
- Simulation/numerical work: convergence, stability, known-case checks, parameter sensitivity, units and physical plausibility.

## Output format

Produce a validation record with:

- Evidence reviewed
- Requirement/criterion table
- Metrics and diagnostics
- Baseline or candidate comparison
- Pass/fail or quantitative assessment
- Risks, limitations, and unresolved assumptions
- Recommended next iteration
- Files/results to preserve in GitHub

## Quality bar

The validation record should make it clear what was actually run, what evidence supports the result, and what cannot yet be claimed. Do not claim improvement unless the executed results support it.
