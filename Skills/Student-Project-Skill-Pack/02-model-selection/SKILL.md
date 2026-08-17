---
name: mat422-model-selection
description: Select and justify candidate mathematical, statistical, ML, econometric, physical, engineering, optimization, or computational models under student-specified conditions.
---
# Model / Method Selection Skill

Use this skill after the problem has been formulated. Codex must characterize the problem before selecting a model and should require at least two reasonable candidate models or methods when the problem permits.

## Inputs to review

- Problem statement, objective, task type, and success criteria.
- Dataset/input description, variable types, units, size, quality, and constraints.
- Assumptions, restrictions, interpretability needs, and computational limits.
- Chosen or possible software platform.
- Validation evidence that will be available after execution.

## Agent responsibilities

1. Characterize the modeling task: prediction, inference, classification, clustering, optimization, simulation, numerical computation, forecasting, or mixed task.
2. Identify at least two reasonable candidate models/methods when possible.
3. For each candidate, explain fit to the data type, objective, assumptions, constraints, interpretability needs, and computational requirements.
4. Identify relevant limitations, failure modes, and risks such as data leakage, overfitting, weak assumptions, multicollinearity, class imbalance, nonlinearity, numerical instability, causal overclaiming, or infeasible constraints.
5. Define quantitative comparison criteria before implementation.
6. Recommend a primary method and at least one alternative or baseline where appropriate.
7. Do not choose a method only because it is easy to execute.
8. Identify what outside references, course topics, or software documentation the student should consult when appropriate.

## Candidate examples

- Python: linear/logistic regression, random forest, gradient boosting, SVM, k-means, PCA/SVD, neural networks, graph/network methods, optimization with SciPy.
- MATLAB: regression, PCA/SVD, optimization, numerical algorithms, SVM, neural networks, simulation, parameter estimation.
- R: regression, classification, inference, PCA, statistical learning, diagnostics, uncertainty modeling.
- SAS: regression, classification, ANOVA, model selection, diagnostics, predictive analytics procedures.
- Stata: regression, panel/longitudinal models, forecasting, robustness checks, econometric specifications.
- Optional approved software: CAD/CAE/design optimization, symbolic/numerical modeling, dashboards, GIS, or structured file-based workflows.

## Output format

Produce a model-selection record with these headings:

- Problem characterization
- Candidate model/method table
- Assumptions and limitations
- Quantitative comparison criteria
- Recommended primary method
- Baseline or alternative method
- Validation plan preview
- Software/toolbox/package requirements
- Student judgment checkpoints

## Quality bar

The output should make it possible to justify the final method using quantitative evidence after execution. If only one model is reasonable, explain why and propose a baseline, diagnostic, sensitivity check, or simplified comparison instead.
