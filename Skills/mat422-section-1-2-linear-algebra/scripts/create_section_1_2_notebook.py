#!/usr/bin/env python3
"""Generate a MAT 422 Section 1.2 starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def md(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.strip().splitlines(True)}


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.strip().splitlines(True),
    }


def build_notebook() -> dict:
    cells = [
        md(
            """
# MAT 422 - Section 1.2: Linear Algebra Concepts in Python

**Topics:** linear spaces, orthogonality, Gram-Schmidt process, eigenvalues and eigenvectors

> Student note: Replace or extend at least one example with your own numbers, then explain what your output means in your own words before submitting.
"""
        ),
        code(
            """
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)
"""
        ),
        md(
            """
## 1.2.1 Linear Spaces

A linear space is closed under vector addition and scalar multiplication. In this example, vectors in R3 stay in R3 after we add them or multiply them by scalars. We also show a span calculation: a linear combination of two vectors is still in the same space.
"""
        ),
        code(
            """
u = np.array([2, -1, 3], dtype=float)
v = np.array([-4, 5, 1], dtype=float)
c = 2.5

print("u =", u)
print("v =", v)
print("u + v =", u + v)
print("c * u =", c * u)
print("linear combination 3u - 2v =", 3*u - 2*v)
print("zero vector =", np.zeros_like(u))
print("additive inverse check u + (-u) =", u + (-u))
"""
        ),
        md(
            """
A useful non-example is the set of vectors in R2 whose first coordinate is exactly 1. It is not a vector space because multiplying by most scalars leaves the set.
"""
        ),
        code(
            """
w = np.array([1, 3], dtype=float)
scaled_w = 2 * w
print("w =", w)
print("2w =", scaled_w)
print("Is 2w still in the set first coordinate = 1?", np.isclose(scaled_w[0], 1))
"""
        ),
        md(
            """
## 1.2.2 Orthogonality

Two vectors are orthogonal when their dot product is zero. Geometrically, this means the angle between them is 90 degrees. The projection of one vector onto an orthogonal vector has zero length.
"""
        ),
        code(
            """
a = np.array([3, 4], dtype=float)
b = np.array([4, -3], dtype=float)

dot_ab = np.dot(a, b)
angle = np.degrees(np.arccos(dot_ab / (np.linalg.norm(a) * np.linalg.norm(b))))
projection_of_a_on_b = (np.dot(a, b) / np.dot(b, b)) * b

print("a dot b =", dot_ab)
print("angle in degrees =", angle)
print("projection of a onto b =", projection_of_a_on_b)

plt.figure(figsize=(5, 5))
plt.quiver(0, 0, a[0], a[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="a")
plt.quiver(0, 0, b[0], b[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="b")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.legend()
plt.title("Orthogonal vectors in R2")
plt.show()
"""
        ),
        md(
            """
## 1.2.3 Gram-Schmidt Process

The Gram-Schmidt process converts a linearly independent set of vectors into an orthonormal basis for the same span. The loop below subtracts projections onto earlier basis vectors, then normalizes the remaining component.
"""
        ),
        code(
            """
def gram_schmidt(columns):
    basis = []
    for x in columns.T:
        y = x.astype(float).copy()
        for q in basis:
            y -= np.dot(q, y) * q
        norm_y = np.linalg.norm(y)
        if norm_y < 1e-12:
            raise ValueError("Input vectors are linearly dependent or nearly dependent.")
        basis.append(y / norm_y)
    return np.column_stack(basis)

A = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
], dtype=float)

Q = gram_schmidt(A)
print("Original column vectors A:")
print(A)
print("\nOrthonormal basis Q:")
print(Q)
print("\nQ.T @ Q should be the identity matrix:")
print(Q.T @ Q)
print("All close to identity?", np.allclose(Q.T @ Q, np.eye(3)))
"""
        ),
        md(
            """
## 1.2.4 Eigenvalues and Eigenvectors

For a square matrix A, an eigenvector v keeps its direction when multiplied by A. Only its scale changes: `A v = lambda v`, where lambda is the eigenvalue.
"""
        ),
        code(
            """
M = np.array([
    [2, 1],
    [1, 2],
], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(M)
print("Matrix M:")
print(M)
print("eigenvalues =", eigenvalues)
print("eigenvectors as columns:")
print(eigenvectors)

for i, lam in enumerate(eigenvalues):
    vec = eigenvectors[:, i]
    residual = M @ vec - lam * vec
    print(f"\nEigenpair {i+1}")
    print("lambda =", lam)
    print("v =", vec)
    print("M @ v =", M @ vec)
    print("lambda * v =", lam * vec)
    print("residual norm =", np.linalg.norm(residual))
"""
        ),
        md(
            """
## Reflection and Submission Checklist

- I explained each concept in words before or after the code.
- I verified important claims numerically, such as dot products, norms, identities, or residuals.
- I changed or extended at least one example so the notebook reflects my own work.
- I ran the notebook from top to bottom without errors.
- I saved the notebook from Google Colab directly to GitHub, following the course instructions.
"""
        ),
    ]
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "colab": {"name": "MAT422_Section_1_2_Linear_Algebra.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_1_2_Linear_Algebra.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
