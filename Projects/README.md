# MAT 422 Student Projects

This folder provides the common template and requirements for the MAT 422 AI-Assisted Modeling Project.

## Start here

1. Read `student-project-requirements.md`.
2. Review `example-project/` to see how a complete project repository can be organized.
3. Choose one approved software platform: Python, MATLAB, R, SAS, or Stata.
4. Define your own discipline-specific problem, objectives, data/inputs, and constraints.
5. Use Codex or another approved LLM-based coding agent to select, implement, evaluate, and improve the model.
6. Copy the example repository structure into your own project repository and replace the example content with your work.

## Recommended repository structure

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

Students may simplify the structure when a project does not need every folder, but the README, problem definition, source/notebook code, prompts/AI record, results, software information, and final report should remain clearly documented.

## GitHub submission

Submit the URL of the completed GitHub repository in Canvas. The repository should contain enough information for another student or instructor to understand and reproduce the main workflow.
