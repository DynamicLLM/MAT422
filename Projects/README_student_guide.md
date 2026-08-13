# MAT 422 Student Projects - Student Guide

This file provides a student-facing guide for the MAT 422 AI-Assisted Modeling Project.

Use `Projects/README.md` and `Projects/student-project-requirements.md` as the main assignment references. Use `Projects/example-project/` as the repository template/reference.

## Start Here

1. Read the project requirements.
2. Choose the problem first, then choose the software.
3. Standard software choices: Python, MATLAB, R, SAS, or Stata.
4. Define objectives, inputs/data, assumptions, constraints, and success criteria.
5. Use Codex as a modeling agent: propose candidate methods, implement them, evaluate results, diagnose problems, and iterate.
6. Create your own GitHub repository following the example structure.
7. Submit your GitHub repository URL through Canvas.

## Suggested repository structure

```text
student-project/
├── README.md
├── problem/
│   └── problem-statement.md
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── notebooks/
├── prompts/
│   ├── problem-formulation.md
│   ├── model-selection.md
│   └── iteration-log.md
├── results/
│   ├── figures/
│   └── tables/
├── report/
│   └── final-report.pdf
├── software-info.md
├── requirements.txt or environment.yml
└── .gitignore
```

## Folder purposes

- `README.md`: project overview, objective, software, model, main results, and reproducibility instructions.
- `problem/`: problem definition, assumptions, inputs, constraints, and success criteria.
- `data/`: appropriate raw and processed data; do not upload restricted/private data.
- `src/`: reusable code, scripts, and functions.
- `notebooks/`: Jupyter or other notebooks, when appropriate.
- `prompts/`: representative Codex prompts and an iteration log showing important AI decisions and corrections.
- `results/`: figures, tables, metrics, and other evidence.
- `report/`: final report.
- `software-info.md`: software/version/environment and the mechanism used to interact with it.
- `requirements.txt` or `environment.yml`: dependencies when applicable.
- `.gitignore`: exclude temporary files, credentials, and local environment artifacts.

## Codex documentation

Document the important AI interactions that materially affected the project: problem formulation, model selection, implementation, debugging, validation, and iteration. Do not claim successful execution unless the software was actually run and the result observed.

## Interface options

A formal API is not required. Use an appropriate machine-actionable mechanism such as an API/engine interface, plugin/add-in, scripting or command interface, structured file/data exchange, or GUI automation when appropriate.

## GitHub practices

Use meaningful commits such as `Add baseline model`, `Compare candidate models`, `Fix validation issue`, and `Add final results`. Do not commit passwords, API keys, tokens, or other secrets.

## Important

`example-project/` is a template/reference. Do not submit the example as your project. Your problem, data, model selection, Codex interactions, code, validation, results, and conclusions must be your own work.
