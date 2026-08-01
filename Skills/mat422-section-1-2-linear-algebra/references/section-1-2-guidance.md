# Section 1.2 Guidance

## Assignment philosophy

The homework should demonstrate understanding through selected examples rather than a fixed problem set. Students may use these examples as a starting point, but they should personalize values, comments, visuals, and reflection before submission.

## Required concepts

### 1.2.1 Linear spaces

Show vectors as elements of a vector space and demonstrate closure under addition and scalar multiplication. Good examples include vectors in R2/R3, polynomial coefficient vectors, or small matrices. Include a non-example if helpful, such as a set that is not closed under scalar multiplication.

Recommended checks:
- Compute `u + v` and `c * u`.
- Explain zero vector and additive inverse.
- Demonstrate span with a small linear combination.

### 1.2.2 Orthogonality

Show the dot product criterion `u dot v = 0`. Include geometric interpretation in R2 or R3. Demonstrate that orthogonal vectors have zero projection on each other and that numerical roundoff can make results very close to zero instead of exactly zero.

Recommended checks:
- Dot product.
- Norms and angle from cosine formula.
- Projection of one vector onto another.

### 1.2.3 Gram-Schmidt process

Start with two or three linearly independent vectors and construct an orthonormal basis. Show each projection removal step or compute it in a transparent loop. Verify the result with `Q.T @ Q`, which should be close to the identity matrix.

Recommended checks:
- Each output vector has norm 1.
- Pairwise dot products are near 0.
- The span is preserved by comparing projection/reconstruction or using QR decomposition intuition.

### 1.2.4 Eigenvalues and eigenvectors

Use a small square matrix with interpretable behavior. Good examples include diagonal scaling, a shear-like matrix, a Markov transition matrix, or a symmetric matrix. Compute eigenvalues/eigenvectors and verify `A @ v = lambda * v`.

Recommended checks:
- Residual norm `||A v - lambda v||`.
- Interpret eigenvectors as directions changed only by scaling.
- For symmetric matrices, mention orthogonal eigenvectors when visible in the example.

## Suggested notebook structure

1. Title and student/course information.
2. Imports and formatting helpers.
3. Linear spaces demonstration.
4. Orthogonality demonstration.
5. Gram-Schmidt demonstration.
6. Eigenvalues/eigenvectors demonstration.
7. Reflection and submission checklist.

## Quality bar

A good notebook should be runnable top to bottom, visually readable on GitHub, and understandable to a peer who is new to linear algebra. Use markdown to state the math idea, code to test it, and a sentence after the output to interpret the result.
