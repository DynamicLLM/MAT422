---
name: mat422-section-3-7-neural-networks
description: Create MAT 422 Section 3.7 Python/Jupyter Notebook homework demonstrations for neural-network formulation, activation functions, cost functions, backpropagation, and the backpropagation algorithm. Use when a student or instructor asks for a Colab-ready notebook, sample homework, explanatory Python examples, rubric-aligned guidance, or a reusable assignment template for Section 3.7: Artificial Neural Networks.
---

# MAT 422 - Section 3.7: Artificial Neural Networks Homework

## Purpose

Use this skill to create a student-facing Jupyter Notebook for Section 3.7: Artificial Neural Networks. The notebook should demonstrate the requested math concepts with Python code, short explanations, appropriate examples, rubric-aligned formatting, and a visible working Colab badge suitable for a public GitHub homework record.

## Core Workflow

1. Read eferences/section-3-7-guidance.md and eferences/homework-rubric.md before drafting content.
2. Create or revise a Colab-friendly .ipynb notebook. Prefer running scripts/create_section_3_7_notebook.py as a starting point, then customize examples if the user gives preferences.
3. Cover all assigned topics unless the user narrows the request:
   - Mathematical formulation
   - Activation functions
   - Cost function
   - Backpropagation
   - Backpropagation algorithm
4. Put a real Open in Colab badge as the first visible notebook element. The badge is required, not optional.
5. Include markdown explanations before each code block. Explain what the example proves or illustrates, not just what the code does.
6. Use NumPy, Matplotlib, and standard scientific Python libraries when appropriate.
7. Keep examples small enough that beginners can inspect the numbers and outputs by hand.
8. End with a rubric-aligned reflection/checklist reminding students to run the notebook top-to-bottom, personalize at least one example, and save directly from Colab to GitHub.

## Notebook Standards

- Include a title, course/section label, topic list, and a required Colab badge as the first visible notebook element.
- Show code outputs for important cells when possible.
- Use deterministic examples; set random seeds if randomness is used.
- Include numeric checks, plots, or validation output so the mathematical claims are visible.
- Cover every requested math concept with a relevant example and a short interpretation of the output.
- Avoid presenting the notebook as the only correct homework. Encourage students to change examples, add comments, and explain their reasoning in their own words.
- Require the notebook to be created in or saved from Google Colab to GitHub so the Colab badge/icon appears and opens the notebook in Colab.

## Script

Run this command from the skill folder to generate a complete starter notebook:

`powershell
python scripts/create_section_3_7_notebook.py --output assets/MAT422_Section_3_7_Neural_Networks.ipynb
`

If system python is unavailable, use the bundled Python runtime in Codex, GitHub Codespaces, Google Colab, or another local Python executable.