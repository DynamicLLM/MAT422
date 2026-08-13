# MAT 422 Student Project Skill Pack

Common Codex workflow for discipline-specific AI-assisted modeling projects.

These skills are intended to make Codex behave as a modeling and coding agent, not merely as a prose generator. The student defines the problem, objectives, data/inputs, assumptions, constraints, and success criteria. Codex helps characterize the problem, compare candidate models or methods, implement the workflow in the chosen software, evaluate actual outputs, diagnose problems, and iterate. The student remains responsible for running the software, verifying results, documenting evidence, and making final judgments.

## Required workflow

1. `01-problem-formulation`: convert a real problem into a precise computational/modeling specification.
2. `02-model-selection`: compare candidate mathematical, statistical, ML, econometric, optimization, or computational methods.
3. `03-interface-selection`: choose a reproducible way for Codex-generated work to reach the selected software.
4. `04-implementation`: generate reproducible code, scripts, notebooks, commands, or structured files.
5. `05-validation`: verify outputs against assumptions, success criteria, diagnostics, and quantitative evidence.
6. `06-optimization-iteration`: compare alternatives, tune parameters, improve preprocessing/features, or revise the method.
7. `07-ai-critic`: inspect AI-generated reasoning, code, results, and claims before final acceptance.
8. `08-documentation`: assemble the GitHub record, report, prompts, validation evidence, and conclusions.

## Software choices

Recommended software choices are Python, MATLAB, R, SAS, and Stata. Software choice is not determined by major; students should choose the platform that fits the problem and explain why.

Optional advanced software may be used with instructor approval when the student can demonstrate a practical, reproducible mechanism for Codex-assisted interaction. Examples include Mathematica/Wolfram Language, Power BI, Excel, SOLIDWORKS, Siemens NX, AutoCAD, ANSYS, COMSOL, Simulink, SPSS, JMP, ArcGIS, or other computational tools. Specialized software access or paid API access is not provided or required by the course.

## Interface options

A formal external API is not mandatory. Prefer the simplest reliable machine-actionable mechanism that can be reproduced:

- Native programming or scripting: Python `.py`/`.ipynb`, MATLAB `.m`, R `.R`/`.Rmd`, SAS `.sas`, Stata `.do`.
- Notebook or interactive execution: Jupyter/Colab, MATLAB Live Scripts, R notebooks, Quarto, or similar.
- Structured file/data exchange: CSV, Excel, JSON, MAT, RDS, DTA, SAS datasets, model/input files, and saved result files.
- API or engine interface: MATLAB Engine API, Python package APIs, software APIs, or other available interfaces.
- Command-line or batch execution: Python, Rscript, SAS batch, Stata batch, or other repeatable command workflows.
- GUI automation: fallback only when a stronger interface is unavailable; document limitations.

## Minimum evidence expected from a completed project

- Clear problem statement, objective, assumptions, constraints, and success criteria.
- Dataset/input description and preprocessing record.
- Software choice and reproducible computational workflow.
- At least two candidate models or methods when the problem permits, with rationale and comparison criteria.
- Reproducible code, scripts, notebooks, commands, or software files.
- Actual execution outputs, metrics, figures, tables, diagnostics, or result files.
- At least one meaningful diagnose-correct-rerun, comparison, optimization, or improvement cycle when applicable.
- AI critique: errors, limitations, questionable assumptions, and human corrections.
- Final report following the required MAT 422 report structure.
- Organized GitHub repository with no secrets or restricted data.

## Evaluation priorities

- Problem formulation and constraints: 20%.
- Codex/AI modeling-agent use: 20%.
- Computational implementation: 15%.
- Mathematical/data-science methodology: 20%.
- Validation, comparison, and iteration: 15%.
- Communication and reproducibility: 10%.

## Important distinction from homework notebooks

Homework assignments require notebook format and a visible `Open in Colab` badge. Projects may use notebooks when appropriate, but projects are not required to use notebook format or a Colab badge unless the instructor gives that requirement for a specific project.