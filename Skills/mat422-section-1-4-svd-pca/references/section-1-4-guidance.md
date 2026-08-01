# Section 1.4 Guidance

## Assignment philosophy

The homework should demonstrate understanding through selected examples rather than a fixed problem set. Students may use these examples as a starting point, but they should personalize values, comments, visuals, and reflection before submission.

## Required concepts

### 1.4.1 Singular value decomposition

Show that a matrix A can be decomposed as A = U Sigma V^T. Use a small matrix first so students can inspect dimensions, singular values, orthonormal singular vectors, and reconstruction.

Recommended checks:
- Compute `U, s, Vt = np.linalg.svd(A, full_matrices=False)`.
- Convert singular values to `Sigma = np.diag(s)`.
- Verify `U @ Sigma @ Vt` reconstructs A.
- Verify `U.T @ U` and `Vt @ Vt.T` are close to identity matrices.
- Plot singular values to show their relative importance.

### 1.4.2 Low-rank matrix approximations

Use truncated SVD to approximate A with rank k. Show that keeping the largest singular values captures the most important structure while reducing rank. Use either a small numeric matrix or a simple synthetic image-like matrix.

Recommended checks:
- Build `A_k = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]`.
- Compare rank-1, rank-2, and full reconstructions.
- Compute Frobenius norm errors `||A - A_k||_F`.
- Plot approximation error as k increases.

### 1.4.3 Principal component analysis

Frame PCA as SVD applied to centered data. Use a two-dimensional dataset with correlated features so the first principal component is visible.

Recommended checks:
- Center the data by subtracting feature means.
- Compute SVD of centered data.
- Interpret rows of `Vt` as principal directions.
- Compute scores/projections with `X_centered @ Vt.T`.
- Compute explained variance ratios from singular values.
- Plot centered data with principal component directions and plot the projection onto PC1/PC2.

## Suggested notebook structure

1. Required Colab badge, title, and course/section information.
2. Imports and formatting helpers.
3. SVD decomposition and reconstruction demonstration.
4. Low-rank approximation demonstration and error plot.
5. PCA demonstration with centered data, explained variance, and projection plot.
6. Reflection and rubric-aligned submission checklist.

## Quality bar

A good notebook should be runnable top to bottom, visually readable on GitHub, and understandable to a peer who is new to SVD and PCA. Use markdown to state the math idea, code to test it, and a sentence after the output to interpret the result.
