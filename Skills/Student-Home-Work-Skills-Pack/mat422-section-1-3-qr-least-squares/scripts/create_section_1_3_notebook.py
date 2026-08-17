#!/usr/bin/env python3
"""Generate a MAT 422 Section 1.3 starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def md(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.strip().splitlines(True)}


def code(source: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source.strip().splitlines(True)}


def build_notebook() -> dict:
    cells = [
        md("""
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/mat422-section-1-3-qr-least-squares/assets/MAT422_Section_1_3_QR_Least_Squares_Regression.ipynb)

# MAT 422 - Section 1.3: QR Decomposition, Least Squares, and Linear Regression

**Topics:** QR decomposition, least-squares problems, linear regression

> Student note: This Colab badge is required for submission. Create or edit the notebook in Google Colab, then save it directly to GitHub so the badge/icon remains available for grading and reruns.
"""),
        code("""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)
"""),
        md("""
## 1.3.1 QR Decomposition

QR decomposition factors a matrix A into A = Q R. The columns of Q are orthonormal, meaning their dot products form the identity matrix, and R is upper triangular. This is useful because orthonormal columns make projections and least-squares calculations cleaner.
"""),
        code("""
A = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
], dtype=float)

Q, R = np.linalg.qr(A)

print("A =")
print(A)
print("\\nQ =")
print(Q)
print("\\nR =")
print(R)
print("\\nQ.T @ Q =")
print(Q.T @ Q)
print("\\nQ @ R =")
print(Q @ R)
print("Q has orthonormal columns?", np.allclose(Q.T @ Q, np.eye(Q.shape[1])))
print("Q @ R reconstructs A?", np.allclose(Q @ R, A))
"""),
        md("""
The checks above show the two main facts: Q has orthonormal columns, and multiplying Q by R reconstructs the original matrix A.
"""),
        md("""
## 1.3.2 Least-Squares Problems

A least-squares problem solves an overdetermined system A x approximately equals b. There may be no exact solution, so we choose x that minimizes the residual norm ||b - A x||. QR decomposition gives a stable way to solve this problem.
"""),
        code("""
b = np.array([1.2, 1.9, 3.2, 3.9], dtype=float)

x_lstsq, residual_sum, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
residual = b - A @ x_lstsq

print("Least-squares solution from np.linalg.lstsq:", x_lstsq)
print("residual vector b - A @ x =", residual)
print("residual norm =", np.linalg.norm(residual))
print("rank of A =", rank)
print("singular values =", singular_values)
print("normal-equation check A.T @ residual =", A.T @ residual)
"""),
        code("""
# Solve the same least-squares problem using QR.
y = Q.T @ b
x_qr = np.linalg.solve(R, y)
qr_residual = b - A @ x_qr

print("Q.T @ b =", y)
print("Least-squares solution from QR:", x_qr)
print("QR residual norm =", np.linalg.norm(qr_residual))
print("QR solution matches np.linalg.lstsq?", np.allclose(x_qr, x_lstsq))
"""),
        md("""
The normal-equation check is close to zero, which means the residual is orthogonal to the column space of A. That is the geometric meaning of the least-squares solution.
"""),
        md("""
## 1.3.3 Linear Regression

Simple linear regression is a least-squares problem. For a line y = beta_0 + beta_1 x, the design matrix has one column of ones for the intercept and one column for x values. The least-squares solution gives the fitted intercept and slope.
"""),
        code("""
x = np.array([0, 1, 2, 3, 4, 5], dtype=float)
y_data = np.array([1.1, 2.0, 2.9, 4.2, 5.1, 5.9], dtype=float)

X = np.column_stack([np.ones_like(x), x])
beta, *_ = np.linalg.lstsq(X, y_data, rcond=None)
y_pred = X @ beta
regression_residuals = y_data - y_pred
rmse = np.sqrt(np.mean(regression_residuals**2))

print("Design matrix X =")
print(X)
print("beta_0 intercept =", beta[0])
print("beta_1 slope =", beta[1])
print("predicted y =", y_pred)
print("residuals =", regression_residuals)
print("RMSE =", rmse)
"""),
        code("""
plt.figure(figsize=(6, 4))
plt.scatter(x, y_data, color="tab:blue", label="data")
plt.plot(x, y_pred, color="tab:red", label="least-squares regression line")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear regression as a least-squares problem")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
"""),
        md("""
The slope tells us the fitted change in y for each one-unit increase in x. The intercept is the fitted value when x = 0. The RMSE summarizes the typical prediction error for this small dataset.
"""),
        md("""
## Reflection and Rubric Checklist

- Code Accuracy and Completeness: I ran the notebook from top to bottom without errors.
- Math Concept Coverage: I demonstrated QR decomposition, least-squares problems, and linear regression.
- Examples Appropriateness: My examples show the concepts clearly and are connected to the math.
- Explanation and Documentation: I explained the purpose and meaning of each code section.
- GitHub and Colab: I saved the notebook directly from Colab to GitHub, and the `Open in Colab` badge is visible and working.
- Format and Clarity: The notebook has a logical flow, readable code, and clear section headings.
- Personalization: I changed or extended at least one example so the notebook reflects my own work.
"""),
    ]
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "colab": {"name": "MAT422_Section_1_3_QR_Least_Squares_Regression.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_1_3_QR_Least_Squares_Regression.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
