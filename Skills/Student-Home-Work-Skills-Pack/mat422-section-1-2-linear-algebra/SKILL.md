---
name: mat422-section-1-2-linear-algebra
description: Create MAT 422 Section 1.2 Python/Jupyter Notebook homework demonstrations for linear spaces, orthogonality, the Gram-Schmidt process, and eigenvalues/eigenvectors. Use when a student or instructor asks for a Colab-ready notebook, sample homework, explanatory Python examples, rubric-aligned guidance, or a reusable assignment template for Section 1.2 linear algebra concepts.
---

# MAT 422 Section 1.2 Linear Algebra Homework

## Purpose

Use this skill to create a student-facing Jupyter Notebook for MAT 422 Section 1.2. The notebook should demonstrate the requested math concepts with Python code, short explanations, appropriate examples, rubric-aligned formatting, and a visible working Colab badge suitable for a public GitHub homework record.

## Core Workflow

1. Read `references/section-1-2-guidance.md` and `references/homework-rubric.md` before drafting content.
2. Create or revise a Colab-friendly `.ipynb` notebook. Prefer running `scripts/create_section_1_2_notebook.py` as a starting point, then customize examples if the user gives preferences.
3. Cover all four topics unless the user narrows the request:
   - Linear spaces
   - Orthogonality
   - Gram-Schmidt process
   - Eigenvalues and eigenvectors
4. Put a real `Open in Colab` badge as the first visible notebook element. The badge is required, not optional.
5. Include markdown explanations before each code block. Explain what the example proves or illustrates, not just what the code does.
6. Use NumPy for calculations and Matplotlib for at least one visual explanation when useful.
7. Keep examples small enough that beginners can inspect the numbers by hand.
8. End with a rubric-aligned reflection/checklist reminding students to run the notebook top-to-bottom, personalize at least one example, and save directly from Colab to GitHub.

## Notebook Standards

- Include a title, course/section label, topic list, and a required Colab badge as the first visible notebook element.
- Show code outputs for important cells when possible.
- Use deterministic examples; set random seeds if randomness is used.
- Prefer exact or near-exact validation checks such as dot products, residual norms, reconstruction checks, eigenpair residuals, and `np.allclose`.
- Cover every requested math concept with a relevant example and a short interpretation of the output.
- Avoid presenting the notebook as the only correct homework. Encourage students to change examples, add comments, and explain their reasoning in their own words.
- Require the notebook to be created in or saved from Google Colab to GitHub so the Colab badge/icon appears and opens the notebook in Colab.

## Script

Run this command from the skill folder to generate a complete starter notebook:

```powershell
python scripts/create_section_1_2_notebook.py --output MAT422_Section_1_2_Linear_Algebra.ipynb
```

If system `python` is unavailable, use the bundled Python runtime in Codex or another local Python executable.
