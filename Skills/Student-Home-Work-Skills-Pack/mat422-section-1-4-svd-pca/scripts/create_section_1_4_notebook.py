#!/usr/bin/env python3
"""Generate a MAT 422 Section 1.4 starter Jupyter Notebook."""

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
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/mat422-section-1-4-svd-pca/assets/MAT422_Section_1_4_SVD_Low_Rank_PCA.ipynb)

# MAT 422 - Section 1.4: SVD, Low-Rank Approximation, and PCA

**Topics:** singular value decomposition, low-rank matrix approximations, principal component analysis

> Student note: This Colab badge is required for submission. Create or edit the notebook in Google Colab, then save it directly to GitHub so the badge/icon remains available for grading and reruns.
"""),
        code("""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)
"""),
        md("""
## 1.4.1 Singular Value Decomposition

Singular value decomposition factors a matrix A into A = U Sigma V^T. The columns of U and V are orthonormal directions, and the singular values in Sigma measure how much each direction contributes to the matrix.
"""),
        code("""
A = np.array([
    [3, 2, 2],
    [2, 3, -2],
    [1, 1, 0],
    [0, 2, 1],
], dtype=float)

U, s, Vt = np.linalg.svd(A, full_matrices=False)
Sigma = np.diag(s)
A_reconstructed = U @ Sigma @ Vt

print("A =")
print(A)
print("\\nSingular values =", s)
print("\\nU shape, Sigma shape, Vt shape =", U.shape, Sigma.shape, Vt.shape)
print("\\nU.T @ U =")
print(U.T @ U)
print("\\nVt @ Vt.T =")
print(Vt @ Vt.T)
print("\\nReconstruction error ||A - U Sigma Vt||_F =", np.linalg.norm(A - A_reconstructed, ord="fro"))
print("Reconstruction is accurate?", np.allclose(A, A_reconstructed))
"""),
        code("""
plt.figure(figsize=(5, 3.5))
plt.plot(np.arange(1, len(s) + 1), s, marker="o")
plt.xlabel("index")
plt.ylabel("singular value")
plt.title("Singular values of A")
plt.grid(True, alpha=0.3)
plt.show()
"""),
        md("""
Large singular values indicate directions that carry more structure. Smaller singular values contribute less, which is why SVD is useful for approximation and compression.
"""),
        md("""
## 1.4.2 Low-Rank Matrix Approximations

A rank-k approximation keeps only the first k singular values and singular vectors. This gives a simpler matrix A_k that captures the strongest patterns in A.
"""),
        code("""
def rank_k_approximation(U, s, Vt, k):
    return U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

errors = []
for k in range(1, len(s) + 1):
    A_k = rank_k_approximation(U, s, Vt, k)
    error = np.linalg.norm(A - A_k, ord="fro")
    errors.append(error)
    print(f"Rank-{k} approximation:")
    print(A_k)
    print("Frobenius error =", error)
    print("matrix rank =", np.linalg.matrix_rank(A_k))
    print()
"""),
        code("""
plt.figure(figsize=(5, 3.5))
plt.plot(np.arange(1, len(errors) + 1), errors, marker="o", color="tab:red")
plt.xlabel("rank k")
plt.ylabel("||A - A_k||_F")
plt.title("Low-rank approximation error")
plt.grid(True, alpha=0.3)
plt.show()
"""),
        md("""
The approximation error decreases as k increases. When k reaches the full rank, the approximation becomes the original matrix up to numerical roundoff.
"""),
        md("""
## 1.4.3 Principal Component Analysis

Principal component analysis finds directions of maximum variation in centered data. PCA can be computed using SVD: after centering the data matrix X, the rows of V^T give principal component directions.
"""),
        code("""
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9],
], dtype=float)

mean = X.mean(axis=0)
X_centered = X - mean
U_pca, s_pca, Vt_pca = np.linalg.svd(X_centered, full_matrices=False)
scores = X_centered @ Vt_pca.T
explained_variance = (s_pca**2) / (len(X) - 1)
explained_ratio = explained_variance / explained_variance.sum()

print("feature means =", mean)
print("principal directions as rows of Vt =")
print(Vt_pca)
print("singular values =", s_pca)
print("explained variance =", explained_variance)
print("explained variance ratio =", explained_ratio)
print("first three PCA scores =")
print(scores[:3])
"""),
        code("""
origin = np.zeros(2)
pc1 = Vt_pca[0] * s_pca[0] / np.sqrt(len(X) - 1)
pc2 = Vt_pca[1] * s_pca[1] / np.sqrt(len(X) - 1)

plt.figure(figsize=(6, 5))
plt.scatter(X_centered[:, 0], X_centered[:, 1], color="tab:blue", label="centered data")
plt.quiver(*origin, *pc1, angles="xy", scale_units="xy", scale=1, color="tab:red", label="PC1")
plt.quiver(*origin, *pc2, angles="xy", scale_units="xy", scale=1, color="tab:green", label="PC2")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.xlabel("feature 1 centered")
plt.ylabel("feature 2 centered")
plt.title("PCA directions on centered data")
plt.grid(True, alpha=0.3)
plt.axis("equal")
plt.legend()
plt.show()
"""),
        code("""
plt.figure(figsize=(6, 4))
plt.scatter(scores[:, 0], scores[:, 1], color="tab:purple")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.xlabel("PC1 score")
plt.ylabel("PC2 score")
plt.title("Data represented in principal component coordinates")
plt.grid(True, alpha=0.3)
plt.show()
"""),
        md("""
The first principal component explains the largest share of variance. Projecting data onto PC1 and PC2 rotates the coordinate system so the strongest variation appears along the first axis.
"""),
        md("""
## Reflection and Rubric Checklist

- Code Accuracy and Completeness: I ran the notebook from top to bottom without errors.
- Math Concept Coverage: I demonstrated SVD, low-rank approximation, and PCA.
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
            "colab": {"name": "MAT422_Section_1_4_SVD_Low_Rank_PCA.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_1_4_SVD_Low_Rank_PCA.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
