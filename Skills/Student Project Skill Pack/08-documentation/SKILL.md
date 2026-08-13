---
name: mat422-project-documentation
description: Produce reproducible GitHub documentation of the problem, Codex interactions, software/interface, modeling decisions, validation, iteration, results, and final report.
---
# Project Documentation Skill

Use this skill at the end of the project and whenever repository documentation needs cleanup. The project record should let a classmate or instructor understand what problem was solved, what Codex contributed, what software ran, what evidence was produced, and what conclusions are justified.

## Required repository evidence

- `README.md`: project title, problem, objectives, constraints, software, how to run the project, main results, and repository contents.
- `data/`: raw/processed data when redistribution is permitted, or data-access instructions and a small example file when data are private, proprietary, or too large.
- `src/`: executable code/scripts/functions.
- `notebooks/`: notebooks when used. Project notebooks do not require a Colab badge unless the instructor specifically requires one.
- `prompts/`: representative prompts and concise records of problem formulation, model selection, implementation, diagnosis, comparison, and iteration.
- `results/`: figures, tables, metrics, model outputs, logs, diagnostics, and validation evidence.
- `report/`: final report and optional supporting documents.
- `software-info.md`: software/version, packages/toolboxes, execution environment, interface mechanism, and setup instructions.
- `requirements.txt` or `environment.yml`: environment dependencies when applicable.
- `.gitignore`: excludes temporary files, credentials, local environment files, and unnecessary generated files.

## Final report structure

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

## Agent responsibilities

1. Check that each required deliverable is present or clearly marked as not applicable.
2. Ensure representative Codex prompts are documented without requiring full chat transcripts.
3. Confirm that model comparison, validation evidence, and iteration records cite actual outputs.
4. Ensure claims in the report match the evidence preserved in the repository.
5. Remove or flag secrets, API keys, passwords, private data, proprietary data, and unnecessary temporary files.
6. Keep paths relative where practical.
7. Make setup and run instructions clear enough for reproduction.
8. Include academic-integrity language that identifies AI-assisted work and preserves student authorship.

## Output format

Produce a documentation checklist and final report outline with:

- Repository files present
- Missing or weak evidence
- README updates needed
- Prompt/iteration log updates needed
- Results and validation files to preserve
- Final report section-by-section notes
- Reproducibility instructions
- Academic integrity / AI-use statement

## Quality bar

Documentation should be clear, reproducible, and evidence-based. Do not let the final report claim software execution, model improvement, or validation success unless the repository contains supporting outputs.
