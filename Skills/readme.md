# MAT 422 Skills

This folder contains reusable Codex skills for MAT 422 homework sections and student project workflows. Homework section skills are organized under `Student-Home-Work-Skills-Pack/`, while interdisciplinary modeling and project workflow skills are organized under `Student-Project-Skill-Pack/`.

## AI Use Guidance

AI tools are permitted for MAT 422 assignments. Students may use AI systems, including Codex through ChatGPT/ASU, as a reference, coding assistant, debugging partner, and study aid.

Use AI to help understand math concepts, generate starter examples, explain Python code, organize notebooks, and check errors. Do not submit AI output without reviewing it carefully. Students are responsible for running the code, verifying the math, personalizing examples, and writing explanations in their own words.

For each homework assignment or project phase, a skill may be provided as an example/reference. Ask Codex to use the relevant skill when helpful, but treat it as support for your own independent work. The use of AI is optional.

Codex tutorial: https://www.youtube.com/watch?v=0TitiOk7hbI

## Student Home Work Skills

The homework skills are located under `Student-Home-Work-Skills-Pack/`. Each section skill helps students and AI agents create a complete, rubric-aligned Jupyter Notebook homework submission.

Current homework skills include:

- `Student-Home-Work-Skills-Pack/mat422-section-1-2-linear-algebra`: Linear spaces, orthogonality, Gram-Schmidt process, eigenvalues and eigenvectors.
- `Student-Home-Work-Skills-Pack/mat422-section-1-3-qr-least-squares`: QR decomposition, least-squares problems, and linear regression.
- `Student-Home-Work-Skills-Pack/mat422-section-1-4-svd-pca`: Singular value decomposition, low-rank matrix approximations, and principal component analysis.
- `Student-Home-Work-Skills-Pack/mat422-section-2-2-probability-random-variables`: Probability axioms, conditional probability, discrete random variables, and continuous random variables.
- `Student-Home-Work-Skills-Pack/mat422-section-2-3-joint-distributions-sampling`: Joint probability distributions, correlation and dependence, and random samples.
- `Student-Home-Work-Skills-Pack/mat422-section-2-4-mle-linear-regression`: Maximum likelihood estimation for random samples and linear regression.
- `Student-Home-Work-Skills-Pack/mat422-section-3-2-limits-derivatives-taylor`: Limits and continuity, derivatives, and Taylor's theorem.
- `Student-Home-Work-Skills-Pack/mat422-section-3-3-optimization-gradient-descent`: Local minimizers, convexity and global minimizers, and gradient descent.
- `Student-Home-Work-Skills-Pack/mat422-section-3-4-logistic-regression`: Logistic regression, sigmoid probabilities, fitting, and decision boundaries.
- `Student-Home-Work-Skills-Pack/mat422-section-3-5-3-6-kmeans-svm`: K-means clustering and support vector machines.
- `Student-Home-Work-Skills-Pack/mat422-section-3-7-neural-networks`: Neural-network formulation, activation functions, cost functions, and backpropagation.
- `Student-Home-Work-Skills-Pack/mat422-section-4-1-4-2-graph-modeling`: Graph basics, adjacency representations, graph traversal, and graph modeling.

## Student Project Skills

The `Student-Project-Skill-Pack/` contains the common Codex workflow and discipline-specific modeling skills for projects using professional or computational software.

Students should use the project skills for planning, implementation, validation, iteration, critique, and documentation. The project skill pack is intended to guide a reproducible project workflow, not merely to generate a short answer.

## How students should use the homework skills

1. Use the section skill as a reference for what concepts the homework notebook should demonstrate.
2. Open or create the notebook in Google Colab.
3. Run all code cells and make sure the notebook runs from top to bottom without errors.
4. Personalize at least one example, add your own explanations, and interpret your output in your own words.
5. Save the final `.ipynb` directly from Google Colab to GitHub.
6. Submit the GitHub permalink to the notebook in Canvas.

## Important Colab requirement

The `Open in Colab` badge is required. It should be the first visible element in the notebook. The badge confirms that the notebook can be opened and rerun from GitHub through Google Colab.

Do not upload a notebook file only from your local computer if the course requires saving directly from Colab. The GitHub page should show the Colab badge/icon and the notebook should open correctly in Colab.

## What the files mean

- `SKILL.md`: Main instructions for an AI agent creating or revising the homework notebook.
- `references/section-*-guidance.md`: Math concept guidance and suggested notebook structure for that section.
- `references/homework-rubric.md`: Rubric expectations used across homework sections.
- `scripts/create_section_*_notebook.py`: Helper script used to generate a starter notebook. This script is not the homework submission.
- `assets/*.ipynb`: Starter notebook asset. The submitted homework should be the student's completed, personalized notebook saved from Colab to GitHub.

## Rubric reminders

A strong MAT 422 notebook should include:

- Accurate Python code that runs without errors.
- Coverage of all required section concepts.
- Relevant examples that clearly illustrate the math.
- Markdown explanations before or after code cells.
- A visible and working `Open in Colab` badge on GitHub.
- Clear formatting, logical flow, and readable code.
