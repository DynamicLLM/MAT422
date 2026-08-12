# Section 1.3 Guidance

## Assignment philosophy

The homework should demonstrate understanding through selected examples rather than a fixed problem set. Students may use these examples as a starting point, but they should personalize values, comments, visuals, and reflection before submission.

## Required concepts

### 1.3.1 QR decomposition

Show that a matrix A can be decomposed as A = Q R, where Q has orthonormal columns and R is upper triangular. Use a small full-rank rectangular matrix so the connection to least squares is natural.

Recommended checks:
- Compute `Q, R = np.linalg.qr(A)`.
- Verify `Q.T @ Q` is close to the identity matrix.
- Verify `Q @ R` reconstructs A.
- Explain why orthonormal columns make computations stable and interpretable.

### 1.3.2 Least-squares problems

Use an overdetermined linear system A x approximately equals b. Show that the least-squares solution minimizes the residual norm when an exact solution usually does not exist.

Recommended checks:
- Compute the solution with `np.linalg.lstsq`.
- Compute residual vector `b - A @ x_hat` and its norm.
- Compare with solving through QR: `R x = Q.T b` for full-rank A.
- Optionally check the normal-equation condition `A.T @ residual` is close to zero.

### 1.3.3 Linear regression

Frame simple linear regression as a least-squares problem with a design matrix containing a column of ones and the predictor values. Fit a line y = beta_0 + beta_1 x, compute predictions and residuals, and visualize the fitted line with the data.

Recommended checks:
- Build `X = np.column_stack([np.ones_like(x), x])`.
- Fit coefficients with `np.linalg.lstsq`.
- Plot data points and fitted line.
- Report residual sum of squares or root mean squared error.
- Interpret slope and intercept in words.

## Suggested notebook structure

1. Required Colab badge, title, and course/section information.
2. Imports and formatting helpers.
3. QR decomposition demonstration.
4. Least-squares demonstration with QR comparison.
5. Linear regression demonstration and plot.
6. Reflection and rubric-aligned submission checklist.

## Quality bar

A good notebook should be runnable top to bottom, visually readable on GitHub, and understandable to a peer who is new to numerical linear algebra. Use markdown to state the math idea, code to test it, and a sentence after the output to interpret the result.
