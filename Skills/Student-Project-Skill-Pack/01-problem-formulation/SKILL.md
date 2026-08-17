---
name: mat422-problem-formulation
description: Define a discipline-specific AI-assisted modeling project with objectives, inputs, assumptions, constraints, outputs, and measurable success criteria.
---
# Problem Formulation Skill

Use this skill at the beginning of a MAT 422 AI-Assisted Modeling Project. The goal is to turn a real-world problem, dataset, or quantitative question into a precise computational/modeling specification before any final model or code is chosen.

## Student provides

- Discipline or application area.
- Problem context and why the question matters.
- Available data, geometry, materials, observations, equations, business records, simulations, or other inputs.
- Variables, units, response/target, predictors/features, metadata, or design parameters when known.
- Objective: prediction, explanation/inference, classification, clustering, optimization, simulation, forecasting, numerical computation, or another quantitative task.
- Conditions, assumptions, restrictions, constraints, and success criteria.
- Preferred or required software, if any.

## Agent responsibilities

1. Restate the problem as a precise computational/modeling task.
2. Separate the objective from constraints, assumptions, and evaluation criteria.
3. Identify inputs, outputs, decision variables, response/target variables, features, parameters, and units when applicable.
4. Identify missing information that would materially affect model selection or validation.
5. Do not invent critical requirements, data, outputs, or success criteria.
6. Translate vague goals into measurable criteria, such as error, accuracy, F1/AUC, residual diagnostics, cost, runtime, design feasibility, parameter error, or a problem-specific metric.
7. Identify at least one relevant MAT 422 or quantitative-method connection, such as least squares/QR, SVD/PCA, probability/MLE, optimization, logistic regression, k-means, SVM, neural networks, networks, or another suitable method.
8. Recommend what evidence should be preserved in GitHub for this phase.

## Output format

Produce a concise project specification with these headings:

- Project title
- Problem and context
- Objective and task type
- Data or computational inputs
- Variables, parameters, units, and outputs
- Assumptions and conditions
- Constraints and restrictions
- Success criteria and validation evidence
- Candidate software platforms
- MAT 422 / quantitative-method connection
- Missing information or student decisions needed
- Files to create in the project repository

## Quality bar

The specification should be detailed enough for the next skill, `mat422-model-selection`, to compare candidate methods without guessing the project goal. If the problem is still too vague, ask targeted questions or state the assumptions that must be confirmed before moving forward.
