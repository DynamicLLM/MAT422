---
name: mat422-section-1-4-svd-pca
description: Create MAT 422 Section 1.4 Python/Jupyter Notebook homework demonstrations for singular value decomposition, low-rank matrix approximations, and principal component analysis. Use when a student or instructor asks for a Colab-ready notebook, sample homework, explanatory Python examples, rubric-aligned guidance, or a reusable assignment template for Section 1.4 SVD/PCA concepts.
---

# MAT 422 Section 1.4 SVD, Low-Rank Approximation, and PCA Homework

## Purpose

Use this skill to create a student-facing Jupyter Notebook for MAT 422 Section 1.4. The notebook must demonstrate singular value decomposition, low-rank matrix approximations, and principal component analysis with Python code, markdown explanations, appropriate examples, rubric-aligned formatting, and a visible working Colab badge.

## Core Workflow

1. Read `references/section-1-4-guidance.md` and `references/homework-rubric.md` before drafting content.
2. Create or revise a Colab-friendly `.ipynb` notebook. Prefer running `scripts/create_section_1_4_notebook.py` as a starting point, then customize examples if the user gives preferences.
3. Cover all three topics unless the user narrows the request:
   - Singular value decomposition
   - Low-rank matrix approximations
   - Principal component analysis
4. Put a real `Open in Colab` badge as the first visible notebook element. The badge is required, not optional.
5. Include markdown explanations before each code block. Explain what the example proves or illustrates, not just what the code does.
6. Use NumPy for calculations and Matplotlib for visualizing singular values, approximation quality, and PCA projections.
7. Keep examples small enough that beginners can inspect the numbers, while still showing meaningful dimension reduction.
8. End with a rubric-aligned reflection/checklist reminding students to run the notebook top-to-bottom, personalize at least one example, and save directly from Colab to GitHub.

## Notebook Standards

- Include a title, course/section label, topic list, and a required Colab badge as the first visible notebook element.
- Show code outputs for important cells when possible.
- Use deterministic examples; set random seeds if randomness is used.
- Verify important claims numerically with checks such as SVD reconstruction error, orthogonality of singular vectors, rank-k approximation error, explained variance ratios, and `np.allclose`.
- For PCA, center the data, compute principal directions, project data to principal component coordinates, and visualize the projection.
- Cover every requested math concept with a relevant example and a short interpretation of the output.
- Avoid presenting the notebook as the only correct homework. Encourage students to change examples, add comments, and explain their reasoning in their own words.
- Require the notebook to be created in or saved from Google Colab to GitHub so the Colab badge/icon appears and opens the notebook in Colab.

## Script

Run this command from the skill folder to generate a complete starter notebook:

```powershell
python scripts/create_section_1_4_notebook.py --output MAT422_Section_1_4_SVD_Low_Rank_PCA.ipynb
```

If system `python` is unavailable, use the bundled Python runtime in Codex or another local Python executable.
