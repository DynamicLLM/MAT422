# MAT 422

This repository supports MAT 422 coursework with two kinds of materials:

- Course topic materials, organized by subject area.
- Reusable homework skills in `Skills/`, which help students and AI agents create section-specific Jupyter Notebook assignments.

## Repository Structure

- `Introduction/`: Introductory course resources, including additional readings and Colab upload guidance.
- `LinearAlgebra/`: Linear algebra readings and examples, including least squares, SVD, PCA, covariance, and Python-based linear algebra materials.
- `Calculus/`: Calculus and optimization-related readings, including Taylor series, Hessian matrices, SVMs, neural networks, and clustering materials.
- `Probability/`: Probability and statistics readings, including expected value, variance, binomial distributions, Pearson correlation, and the central limit theorem.
- `LLM Fine-Tuning/`: Materials related to fine-tuning and large language models.
- `tools/`: Utility notes and supporting course tools.
- `Skills/`: Reusable Codex skills for creating MAT 422 homework notebooks by section.

## Homework Skills

The `Skills/` folder contains section-specific skill subfolders. Each skill is designed to guide an AI agent or student through creating a complete, rubric-aligned Jupyter Notebook homework submission.

Current skills include:

- `Skills/mat422-section-1-2-linear-algebra`: Linear spaces, orthogonality, Gram-Schmidt process, eigenvalues and eigenvectors.
- `Skills/mat422-section-1-3-qr-least-squares`: QR decomposition, least-squares problems, and linear regression.
- `Skills/mat422-section-1-4-svd-pca`: Singular value decomposition, low-rank matrix approximations, and principal component analysis.

Each skill folder may include:

- `SKILL.md`: Main instructions for the homework workflow.
- `references/`: Section guidance and rubric expectations.
- `scripts/`: Helper scripts for generating starter notebooks.
- `assets/`: Starter `.ipynb` notebook assets.

The generator scripts are helper tools only. The homework submission should be the completed, personalized Jupyter Notebook, not the `.py` generator script.

## Colab and GitHub Submission Requirement

Homework notebooks should be created or edited in Google Colab and saved directly from Colab to GitHub. The notebook should show a visible `Open in Colab` badge on GitHub so the instructor and other readers can open, run, and modify the notebook in Colab.

Do not rely only on uploading an `.ipynb` file from a local computer if the assignment requires saving from Colab. The Colab badge/icon is part of the submission expectation.

## Rubric Expectations

A strong MAT 422 homework notebook should include:

- Python code that runs from top to bottom without errors.
- Coverage of every required math concept for the assigned section.
- Examples that clearly demonstrate the math concepts.
- Markdown explanations that interpret both the mathematics and the code output.
- A visible and working `Open in Colab` badge.
- Clear formatting, readable code, and a logical notebook flow.
- Student personalization, such as changed examples, added comments, or additional interpretation.

## Suggested Student Workflow

1. Review the relevant course topic materials.
2. Use the matching skill under `Skills/` as homework guidance.
3. Open or create the notebook in Google Colab.
4. Run all code cells and verify the outputs.
5. Add your own explanations and personalize at least one example.
6. Save the notebook directly from Colab to GitHub.
7. Submit the GitHub permalink for the notebook to Canvas.
