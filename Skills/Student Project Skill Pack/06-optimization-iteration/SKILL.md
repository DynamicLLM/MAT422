---
name: mat422-optimization-iteration
description: Improve a solution through comparison, tuning, optimization, diagnostics, or revised modeling while respecting constraints and validation evidence.
---
# Optimization and Iteration Skill

Use this skill after initial validation. The goal is to perform at least one meaningful comparison, correction, tuning, or improvement cycle when applicable. Improvements must be supported by actual executed results.

## Agent responsibilities

1. Define the objective or comparison criterion before making changes.
2. Identify adjustable parameters, features, preprocessing steps, model specifications, design variables, constraints, or assumptions.
3. Select a defensible iteration strategy: baseline comparison, model comparison, hyperparameter tuning, feature engineering, sensitivity analysis, robustness check, numerical optimization, diagnostic correction, or design search.
4. Generate revised code, scripts, commands, notebooks, or structured files.
5. Require the student to execute the revised workflow when direct execution is unavailable.
6. Compare initial and revised results quantitatively.
7. Keep only conclusions supported by actual outputs.
8. Document what changed, why it changed, what improved, what did not improve, and what tradeoffs appeared.

## Example iteration types

- Python/ML: tune hyperparameters, compare algorithms, adjust features, check leakage, rebalance classes, or improve validation design.
- MATLAB: improve numerical method, tune optimization parameters, compare regression/PCA/SVD/ML alternatives, or test sensitivity.
- R/SAS/Stata: compare specifications/procedures, add diagnostics, transform variables, address missingness, or run robustness checks.
- Optimization/design: compare baseline and revised designs under constraints such as cost, mass, error, runtime, displacement, or feasibility.
- Dashboard/business analytics: revise measures, forecasting model, transformation logic, or evaluation metric.

## Output format

Produce an iteration record with:

- Initial result and evidence
- Objective or criterion for improvement
- Change proposed by Codex
- Revised implementation steps
- Executed revised result
- Quantitative comparison
- Tradeoffs and limitations
- Decision: keep, reject, or further revise
- Files/results to preserve in GitHub

## Quality bar

The iteration must be meaningful. Cosmetic changes, prose-only edits, or unexecuted claims do not satisfy the improvement cycle. If improvement is not possible or not appropriate, document a justified baseline comparison, sensitivity analysis, or robustness check instead.
