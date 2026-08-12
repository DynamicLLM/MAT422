---
name: mat422-section-1-3-qr-least-squares
description: Create MAT 422 Section 1.3 Python/Jupyter Notebook homework demonstrations for QR decomposition, least-squares problems, and linear regression. Use when a student or instructor asks for a Colab-ready notebook, sample homework, explanatory Python examples, or a reusable assignment template for Section 1.3 numerical linear algebra and regression concepts.
---

# MAT 422 Section 1.3 QR, Least Squares, and Regression Homework

## Purpose

Use this skill to create a student-facing Jupyter Notebook for MAT 422 Section 1.3. The notebook must demonstrate QR decomposition, least-squares problems, and linear regression with Python code, markdown explanations, appropriate examples, and a visible working Colab badge.

## Core Workflow

1. Read `references/section-1-3-guidance.md` and `references/homework-rubric.md` before drafting content.
2. Create or revise a Colab-friendly `.ipynb` notebook. Prefer running `scripts/create_section_1_3_notebook.py` as a starting point, then customize examples if the user gives preferences.
3. Cover all three topics unless the user narrows the request:
   - QR decomposition
   - Least-squares problems
   - Linear regression
4. Put a real `Open in Colab` badge as the first visible notebook element. The badge is required, not optional.
5. Include markdown explanations before each code block. Explain what the example proves or illustrates, not just what the code does.
6. Use NumPy for calculations and Matplotlib for visualizing regression or residuals.
7. Keep examples small enough that beginners can inspect the numbers by hand, while still showing realistic overdetermined data for least squares/regression.
8. End with a rubric-aligned checklist reminding students to run the notebook top-to-bottom, personalize at least one example, and save directly from Colab to GitHub.

## Notebook Standards

- Include a title, course/section label, topic list, and a required Colab badge as the first visible notebook element.
- Show code outputs for important cells when possible.
- Use deterministic examples; set random seeds if randomness is used.
- Verify important claims numerically with checks such as `Q.T @ Q`, `Q @ R`, residual norms, normal equation residuals, and `np.allclose`.
- For linear regression, include a clear design matrix, fitted coefficients, predictions, residuals, and a plot of data plus fitted line or curve.
- Avoid presenting the notebook as the only correct homework. Encourage students to change examples, add comments, and explain their reasoning in their own words.
- Require the notebook to be created in or saved from Google Colab to GitHub so the Colab badge/icon appears and opens the notebook in Colab.

## Script

Run this command from the skill folder to generate a complete starter notebook:

```powershell
python scripts/create_section_1_3_notebook.py --output MAT422_Section_1_3_QR_Least_Squares_Regression.ipynb
```

If system `python` is unavailable, use the bundled Python runtime in Codex or another local Python executable.
