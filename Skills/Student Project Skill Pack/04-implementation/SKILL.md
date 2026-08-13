---
name: mat422-software-implementation
description: Implement the selected model or computational workflow in the chosen software with Codex assistance while preserving reproducibility and actual execution evidence.
---
# Software Implementation Skill

Use this skill to generate or revise the executable project work: code, scripts, notebooks, commands, structured input files, or software-specific files. The implementation must connect directly to the formulated problem, selected model/method, interface plan, and validation criteria.

## Agent responsibilities

1. Generate reproducible code, scripts, notebooks, commands, API calls, plugin code, macros, or structured files appropriate for the selected software.
2. Keep the implementation modular enough to inspect, rerun, and debug.
3. Include data loading, preprocessing, model fitting or computation, validation, metrics, figures/tables, and output saving when applicable.
4. Prevent common modeling errors such as data leakage, using test data during training/tuning, silently dropping important variables, overwriting raw data, hard-coding local absolute paths, or reporting unexecuted results.
5. Add concise comments explaining important operations, not every line.
6. Document required packages, toolboxes, procedures, commands, seeds, and software versions.
7. Provide repeatable execution steps for the student.
8. Never claim successful execution unless actual execution was observed or the student provides outputs.
9. When errors occur, help diagnose, correct, and rerun; preserve at least one meaningful diagnose-correct-rerun cycle when applicable.

## Platform guidance

- Python: prefer reproducible scripts or notebooks with clear package imports, train/validation/test separation when needed, metrics, plots, and saved outputs.
- MATLAB: use scripts/functions or Live Scripts, state mathematical assumptions, include numerical diagnostics, and save figures/tables/results.
- R: use `.R`, R Markdown, Quarto, or notebooks; include diagnostics, uncertainty, validation, and reproducible package notes.
- SAS: preserve `.sas` programs, procedure choices, logs/outputs, diagnostics, and result tables.
- Stata: preserve `.do` files, logs, model specifications, diagnostics/robustness checks, and output interpretation.

## Output format

Produce an implementation package plan or files with:

- Files created or modified
- How to run the workflow
- Required dependencies or software/toolboxes
- Inputs used
- Outputs produced
- Metrics/diagnostics generated
- Checks against assumptions and constraints
- Known limitations or remaining execution steps

## Quality bar

The implementation should allow the student to run the software, collect actual outputs, and proceed to `mat422-validation`. If the agent cannot execute the software directly, it must clearly tell the student what to run and what outputs/errors to bring back.
