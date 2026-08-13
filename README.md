# MAT 422

This repository supports MAT 422 coursework with three kinds of materials:

- Course topic materials, organized by subject area.
- Student homework skills in `Skills/Student Home Work Skills Pack/`, which help students and AI agents create section-specific Jupyter Notebook assignments.
- Student project materials in `Projects/` and project workflow skills in `Skills/Student Project Skill Pack/`, which support AI-assisted modeling projects that may use notebooks, scripts, reports, or discipline-specific software.

## Repository Structure

- `Introduction/`: Introductory course resources, including additional readings and Colab upload guidance.
- `LinearAlgebra/`: Linear algebra readings and examples, including least squares, SVD, PCA, covariance, and Python-based linear algebra materials.
- `Calculus/`: Calculus and optimization-related readings, including Taylor series, Hessian matrices, SVMs, neural networks, and clustering materials.
- `Probability/`: Probability and statistics readings, including expected value, variance, binomial distributions, Pearson correlation, and the central limit theorem.
- `LLM Fine-Tuning/`: Materials related to fine-tuning and large language models.
- `Projects/`: Student project requirements, a student guide, and an example project repository structure for the MAT 422 AI-Assisted Modeling Project.
- `tools/`: Utility notes and supporting course tools.
- `Skills/`: Reusable Codex skills for homework notebooks and student projects.

## Using AI Responsibly

AI tools are permitted for MAT 422 assignments. You may use AI systems, including Codex through ChatGPT/ASU, as a reference, coding assistant, debugging partner, and study aid. AI can help you understand concepts, generate starter examples, explain Python code, organize your notebook or project repository, compare modeling approaches, and improve documentation.

However, you are still responsible for doing the work independently. Do not submit AI output without reading, running, checking, and personalizing it. Your homework notebooks and project materials should show your own understanding through explanations, examples, comments, validation, interpretation of results, and final conclusions.

For each homework assignment or project phase, skills may be provided in `Skills/` as examples and references. You can ask Codex to use the relevant skill while working, but you should still verify the math, run the code or software yourself when required, and make the final submission your own work.

Codex tutorial: https://www.youtube.com/watch?v=0TitiOk7hbI

## Homework Skills

The homework skills are located under `Skills/Student Home Work Skills Pack/`. Each section skill is designed to guide an AI agent or student through creating a complete, rubric-aligned Jupyter Notebook homework submission.

Current homework skills include:

- `Skills/Student Home Work Skills Pack/mat422-section-1-2-linear-algebra`: Linear spaces, orthogonality, Gram-Schmidt process, eigenvalues and eigenvectors.
- `Skills/Student Home Work Skills Pack/mat422-section-1-3-qr-least-squares`: QR decomposition, least-squares problems, and linear regression.
- `Skills/Student Home Work Skills Pack/mat422-section-1-4-svd-pca`: Singular value decomposition, low-rank matrix approximations, and principal component analysis.

Each homework skill folder may include:

- `SKILL.md`: Main instructions for the homework workflow.
- `references/`: Section guidance and rubric expectations.
- `scripts/`: Helper scripts for generating starter notebooks.
- `assets/`: Starter `.ipynb` notebook assets.

The generator scripts are helper tools only. The homework submission should be the completed, personalized Jupyter Notebook, not the `.py` generator script.

## Project Materials and Skills

The project materials are located in `Projects/`. Students should start with `Projects/student-project-requirements.md`, review `Projects/README_student_guide.md`, and use `Projects/example-project/` as a reference for organizing a reproducible project repository.

The project skills are located under `Skills/Student Project Skill Pack/`. They support a richer workflow than a single prompt by breaking the project into repeatable phases:

1. Problem formulation: define the domain problem, objectives, inputs, assumptions, constraints, and success criteria.
2. Model or method selection: compare candidate approaches and justify the final choice.
3. Interface selection: choose a practical way to work with the selected software, such as scripts, notebooks, APIs, command-line tools, packages, structured data exchange, or GUI automation when needed.
4. Implementation: build the model, analysis, or computational workflow in the selected software.
5. Validation and verification: run the work, check results against requirements, and document evidence.
6. Optimization and iteration: compare alternatives or improve parameters, features, assumptions, or implementation details.
7. AI critique: record important Codex errors, corrections, limitations, and places where human judgment was required.
8. Documentation: prepare clear project files, reproducibility notes, results, limitations, and final conclusions.

Discipline-specific project skill files are also provided for Python/ML, MATLAB/Mathematica, SAS/R, Stata, Power BI, SOLIDWORKS, and related computational workflows. The project skill pack is intended to guide planning, implementation, validation, and documentation, not merely to generate a short answer.

## Homework Colab and GitHub Submission Requirement

Homework notebooks should be created or edited in Google Colab and saved directly from Colab to GitHub. The notebook should show a visible `Open in Colab` badge on GitHub so the instructor and other readers can open, run, and modify the notebook in Colab.

Do not rely only on uploading an `.ipynb` file from a local computer if the assignment requires saving from Colab. The Colab badge/icon is part of the homework submission expectation.

This Colab badge requirement applies to homework notebooks. Student projects may use notebooks when appropriate, but projects are not required to use notebook format or include a Colab badge unless the instructor gives that requirement for a specific project.

## Homework Rubric Expectations

A strong MAT 422 homework notebook should include:

- Python code that runs from top to bottom without errors.
- Coverage of every required math concept for the assigned section.
- Examples that clearly demonstrate the math concepts.
- Markdown explanations that interpret both the mathematics and the code output.
- A visible and working `Open in Colab` badge.
- Clear formatting, readable code, and a logical notebook flow.
- Student personalization, such as changed examples, added comments, or additional interpretation.

## Project Expectations

A strong MAT 422 project repository should include:

- A clear problem statement with objectives, assumptions, constraints, and success criteria.
- A description of the data, inputs, software platform, and reproducible execution method.
- Evidence that Codex or another approved AI coding agent contributed to problem formulation, model selection, implementation, debugging, validation, or iteration.
- Reproducible code, notebooks, scripts, or software files appropriate for the selected platform.
- Validation results, comparisons, improvements, and a discussion of limitations.
- A final report or clearly documented final conclusions.
- Organized GitHub files with no passwords, API keys, tokens, private data, or unnecessary temporary files.

## Suggested Homework Workflow

1. Review the relevant course topic materials.
2. Use the matching skill under `Skills/Student Home Work Skills Pack/` as homework guidance.
3. Open or create the notebook in Google Colab.
4. Run all code cells and verify the outputs.
5. Add your own explanations and personalize at least one example.
6. Save the notebook directly from Colab to GitHub.
7. Submit the GitHub permalink for the notebook to Canvas.

## Suggested Project Workflow

1. Read `Projects/student-project-requirements.md` and `Projects/README_student_guide.md`.
2. Review `Projects/example-project/` for the recommended repository structure.
3. Use the relevant workflow and discipline skills under `Skills/Student Project Skill Pack/`.
4. Define your project problem, data or inputs, assumptions, constraints, and success criteria.
5. Use Codex to compare methods, implement the workflow, debug, validate, and iterate.
6. Document important prompts, AI contributions, corrections, and human decisions.
7. Organize the final project repository and submit the GitHub repository URL to Canvas.
