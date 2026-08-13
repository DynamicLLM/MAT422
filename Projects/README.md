# MAT 422 Student Projects

This folder provides the common template and requirements for the MAT 422 AI-Assisted Modeling Project.

The project asks students to use Codex or another approved LLM-based coding agent as an AI modeling agent. Codex should help formulate the problem, compare candidate models or methods, generate reproducible implementation code, evaluate actual execution results, diagnose errors, and iterate toward a better solution.

## Start here

1. Read `student-project-requirements.md`.
2. Review `README_student_guide.md` and `example-project/` to see how a complete project repository can be organized.
3. Choose the problem first, then choose the software.
4. Recommended software choices are Python, MATLAB, R, SAS, and Stata. Other computational software requires instructor approval and must support a reproducible scripting, programming, notebook, command, or structured file/data workflow.
5. Define your own discipline-specific problem, objectives, data/inputs, assumptions, constraints, and measurable success criteria.
6. Use Codex to compare at least two reasonable candidate models or methods when the problem permits.
7. Run the code or software, preserve actual outputs, and use Codex to diagnose, compare, validate, and improve the work.
8. Submit the completed GitHub repository URL through Canvas.

## Common modeling workflow

1. Student defines a meaningful problem or quantitative question and identifies the dataset or computational inputs.
2. Student specifies the prediction, analysis, inference, classification, clustering, optimization, simulation, or other quantitative objective.
3. Codex characterizes the problem and proposes candidate mathematical, statistical, machine-learning, econometric, optimization, or computational methods.
4. Codex explains assumptions, limitations, and why each method may fit the problem.
5. Codex generates reproducible code, scripts, notebooks, commands, or structured input/output files.
6. Student executes the software and provides actual outputs, errors, metrics, figures, or result files back to Codex when the agent cannot directly run the environment.
7. Codex evaluates results, compares candidate approaches, diagnoses issues, and revises preprocessing, model choice, features, parameters, or code.
8. Student validates the final result and explains the quantitative method, AI decisions, software workflow, limitations, and conclusions.

## Recommended repository structure

```text
student-project/
├── README.md
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
│   ├── tables/
│   └── metrics/
├── report/
│   └── final-report.pdf
├── software-info.md
├── requirements.txt or environment.yml
└── .gitignore
```

Students may simplify the structure when a project does not need every folder, but the README, source/notebook code, prompts/AI record, results, software information, and final report should remain clearly documented.

## Folder purposes

- `README.md`: Project title, problem, objectives, constraints, software, how to run the project, main results, and repository contents.
- `data/`: Input and processed datasets when redistribution is permitted. If data are private, proprietary, or too large, provide access instructions and a small example file when appropriate.
- `src/`: Executable Python, MATLAB, R, SAS, Stata, or other project code/scripts.
- `notebooks/`: Jupyter, Colab, MATLAB Live, R Markdown, Quarto, or other notebooks when used. Projects may use notebooks, but notebook format and a Colab badge are not required unless assigned by the instructor.
- `prompts/`: Important Codex prompts and concise records of model-selection and diagnose-correct-rerun iterations.
- `results/`: Figures, tables, metrics, model outputs, and other evidence used in the final report.
- `report/`: Final report and, when useful, presentation or supplementary documentation.
- `software-info.md`: Software/version, packages/toolboxes, execution environment, and special setup instructions.
- `requirements.txt` or `environment.yml`: Reproducible environment files when applicable.
- `.gitignore`: Excludes temporary files, credentials, large generated files, and local environment files.

## GitHub submission

Submit the URL of the completed GitHub repository in Canvas. The repository should contain enough information for another student or instructor to understand and reproduce the main workflow.

Use meaningful commit messages and maintain a clear project history. A small project should still show development beyond a single final upload.

Do not commit passwords, API keys, private student data, proprietary datasets, or other restricted information.