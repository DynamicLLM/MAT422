# MAT 422 Student Project Requirements

## Project objective

Use Codex or another approved LLM-based coding agent as an AI modeling agent. The student defines a discipline-specific problem, objectives, available information, conditions, assumptions, constraints, and measurable success criteria. Codex proposes appropriate models or methods, generates the implementation, evaluates actual results, and iterates toward a better solution.

Codex should do more than generate prose or isolated code. It should help analyze problem conditions, propose candidate mathematical/statistical/machine-learning/econometric/optimization/computational models, implement them in the selected software, interpret execution results, and revise the workflow when needed.

## Approved software choices

Recommended software choices are Python, MATLAB, R, SAS, and Stata. Software choice is not determined by major. Students should choose the platform that best supports the selected problem and explain the choice.

Other computational software may be used with instructor approval when it supports a reproducible scripting, programming, notebook, command, or structured file/data workflow. Specialized software access or paid API access is not provided or required by the course.

Approval rule for optional software: choose the problem first and the software second. The student must explain how Codex will pass instructions/data to the software, how results will be returned, and how the workflow will be reproduced. API access is not assumed.

## Required workflow

1. **Problem formulation**: state the problem, objective, inputs/data, assumptions, conditions, constraints, and success criteria.
2. **Model selection**: ask Codex to characterize the problem before choosing a model. Require at least two reasonable candidate models or methods when the problem permits.
3. **Interface selection**: document how the selected software will be used, such as scripts, notebooks, commands, APIs, packages, or structured file/data exchange.
4. **Software implementation**: implement the selected method in Python, MATLAB, R, SAS, Stata, or approved software.
5. **Execution and verification**: run the software yourself when necessary; do not claim success without evidence.
6. **Validation**: evaluate the result against quantitative criteria, assumptions, diagnostics, and model requirements.
7. **Comparison or optimization**: compare candidate models or a final model against a meaningful baseline when possible, and/or improve parameters, features, preprocessing, or model choices.
8. **AI critique**: document important Codex errors, corrections, limitations, and cases where human judgment was required.
9. **Final communication**: explain the method, results, validation, limitations, conclusions, and possible future improvements.

## Interface requirement

A formal external API is not required. The essential requirement is a reproducible computational loop:

```text
student requirements/data -> Codex model/method selection -> generated code/script -> software execution -> quantitative results -> Codex evaluation/revision -> final validated result
```

Depending on the platform, acceptable interfaces include native programming/scripting, notebooks or interactive execution, structured file/data exchange, APIs or engine interfaces, command-line or batch execution, plugins/add-ins, macros, or GUI automation when appropriate.

## Common project requirements

### Problem and data definition

- State the problem or research question clearly.
- Describe the dataset or computational inputs, including variables, units, response/target, and relevant metadata.
- State assumptions, conditions, restrictions, and success criteria.
- Identify whether the goal is prediction, explanation/inference, classification, clustering, optimization, simulation, or another quantitative task.

### Codex-based model or method selection

- Ask Codex to characterize the problem before choosing a model.
- Require at least two candidate models/methods when reasonable.
- Require a rationale for each candidate based on data type, assumptions, objective, constraints, interpretability, and computational requirements.
- Evaluate whether Codex's choices are defensible using course knowledge and outside references when appropriate.

### Computational implementation

- Generate reproducible code, scripts, notebooks, or commands in the chosen software.
- Document required packages, toolboxes, procedures, and execution commands.
- Run all code and preserve actual outputs used in the report.
- When errors occur, document at least one meaningful diagnose-correct-rerun cycle when applicable.

### Validation, comparison, and iteration

- Use appropriate train/validation/test separation, cross-validation, residual/diagnostic analysis, sensitivity analysis, numerical checks, or other validation methods.
- Compare candidate models or the final model against a meaningful baseline when possible.
- Use quantitative criteria such as error, accuracy, F1/AUC, likelihood/information criteria, residual diagnostics, computational cost, or problem-specific metrics.
- Use Codex to revise preprocessing, model choice, features, parameters, or hyperparameters based on observed results.
- Do not claim improvement unless supported by actual executed results.

### Mathematical and data-science connection

The project should demonstrate understanding of at least one substantive quantitative method. Relevant MAT 422 topics include least squares/QR, SVD/PCA, probability and MLE, optimization and gradient descent, logistic regression, k-means, SVM, neural networks, and network methods. Other appropriate methods are allowed when they fit the student's problem.

## Minimum deliverables

- Problem statement, objective, assumptions/conditions, constraints, and success criteria.
- Dataset/input description and preprocessing record.
- Explanation of software choice and computational workflow.
- Representative Codex prompts showing problem formulation, model/method selection, implementation, and revision.
- Complete reproducible code, script, notebook, or software files.
- At least one quantitative model/method comparison or justified baseline comparison when the problem permits.
- Validation metrics, diagnostics, figures/tables, and actual software outputs.
- Evidence of at least one meaningful iteration or improvement cycle when applicable.
- GitHub repository URL with required README, code/scripts, inputs or data-access instructions, prompts/iteration log, results, and final report.
- Final model/solution, interpretation, limitations, and discussion of AI errors or human corrections.

## Evaluation criteria

| Criterion | Weight | Expectation |
| --- | ---: | --- |
| Problem formulation and constraints | 20% | Problem is meaningful, measurable, and sufficiently specified; data/inputs and success criteria are clear. |
| Codex/AI modeling-agent use | 20% | Codex contributes to model/method selection, implementation, diagnosis, comparison, and revision; important prompts/decisions are documented. |
| Computational implementation | 15% | Chosen software is used reproducibly through code, scripts, notebooks, and structured data/results. |
| Mathematical/data-science methodology | 20% | Appropriate quantitative methods are correctly applied and explained. |
| Validation, comparison, and iteration | 15% | Results are quantitatively validated; alternatives/baselines are compared; errors and limitations are addressed. |
| Communication and reproducibility | 10% | Report/presentation is clear and includes sufficient code, files, figures/tables, and execution detail to reproduce the work. |

## Required final report structure

1. Problem and context
2. Objectives, data/inputs, assumptions, conditions, and constraints
3. Selected software, computational/file interface, and GitHub repository structure
4. Codex/AI-agent workflow and representative prompts
5. Candidate models/methods and selection rationale
6. Mathematical/statistical/optimization/data-science methods
7. Implementation and execution
8. Model comparison, validation, and iteration
9. Final results and interpretation
10. Limitations, AI errors, and human corrections
11. Conclusions and possible future improvements

## GitHub rules

- Do not commit passwords, API keys, private datasets, proprietary data, or other secrets.
- Use relative paths so the project is reproducible on another machine when practical.
- Include a README with setup and run instructions.
- Use meaningful commit messages and maintain a clear history beyond a single final upload.
- Keep generated outputs that are needed to understand the final result; avoid committing unnecessary temporary files.

Academic integrity note: AI tools may augment the student's work but do not replace student understanding, verification, or authorship. Students must document AI use and follow the course and ASU academic-integrity requirements.