#!/usr/bin/env python3
"""Generate a MAT 422 - Section 3.3: Optimization and Gradient Descent starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CELLS_JSON = r'''[
    {
        "source":  [
                       "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/Student-Home-Work-Skills-Pack/mat422-section-3-3-optimization-gradient-descent/assets/MAT422_Section_3_3_Optimization_Gradient_Descent.ipynb)\\\\n",
                       "\\\\n",
                       "# MAT 422 - Section 3.3: Optimization and Gradient Descent\\\\n",
                       "\\\\n",
                       "**Topics:** Necessary and sufficient conditions of local minimizers, Convexity and global minimizers, Gradient descent\\\\n",
                       "\\\\n",
                       "\\\\u003e Student note: This Colab badge is required for submission. Create or edit the notebook in Google Colab, then save it directly to GitHub so the badge/icon remains available for grading and reruns.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "import numpy as np\\\\n",
                       "import matplotlib.pyplot as plt\\\\n",
                       "\\\\n",
                       "np.set_printoptions(precision=5, suppress=True)\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Necessary and sufficient conditions of local minimizers\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Necessary and sufficient conditions of local minimizers**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "def f(x):\\\\n",
                       "    return (x**2 - 1)**2\\\\n",
                       "\\\\n",
                       "def fp(x):\\\\n",
                       "    return 4*x*(x**2 - 1)\\\\n",
                       "\\\\n",
                       "def fpp(x):\\\\n",
                       "    return 12*x**2 - 4\\\\n",
                       "\\\\n",
                       "critical_points = np.array([-1, 0, 1])\\\\n",
                       "for c in critical_points:\\\\n",
                       "    print(f\\\\"x={c}: f\\\\u0027(x)={fp(c)}, f\\\\u0027\\\\u0027(x)={fpp(c)}, f(x)={f(c)}\\\\")\\\\n",
                       "\\\\n",
                       "x = np.linspace(-2, 2, 400)\\\\n",
                       "plt.plot(x, f(x))\\\\n",
                       "plt.scatter(critical_points, f(critical_points), color=\\\\"tab:red\\\\")\\\\n",
                       "plt.title(\\\\"Local minimizers and a local maximizer\\\\")\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Convexity and global minimizers\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Convexity and global minimizers**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "def g(x):\\\\n",
                       "    return (x - 2)**2 + 1\\\\n",
                       "\\\\n",
                       "x = np.linspace(-1, 5, 300)\\\\n",
                       "plt.plot(x, g(x))\\\\n",
                       "plt.axvline(2, color=\\\\"tab:red\\\\", linestyle=\\\\"--\\\\", label=\\\\"global minimizer\\\\")\\\\n",
                       "plt.title(\\\\"A convex function has one global minimizer here\\\\")\\\\n",
                       "plt.legend()\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Gradient descent\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Gradient descent**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "def grad_g(x):\\\\n",
                       "    return 2 * (x - 2)\\\\n",
                       "\\\\n",
                       "learning_rate = 0.2\\\\n",
                       "current = -1.0\\\\n",
                       "path = [current]\\\\n",
                       "for _ in range(20):\\\\n",
                       "    current = current - learning_rate * grad_g(current)\\\\n",
                       "    path.append(current)\\\\n",
                       "\\\\n",
                       "path = np.array(path)\\\\n",
                       "print(\\\\"Final x =\\\\", path[-1])\\\\n",
                       "print(\\\\"Final objective =\\\\", g(path[-1]))\\\\n",
                       "\\\\n",
                       "plt.plot(path, marker=\\\\"o\\\\")\\\\n",
                       "plt.axhline(2, color=\\\\"tab:red\\\\", linestyle=\\\\"--\\\\", label=\\\\"minimizer\\\\")\\\\n",
                       "plt.xlabel(\\\\"iteration\\\\")\\\\n",
                       "plt.ylabel(\\\\"x value\\\\")\\\\n",
                       "plt.title(\\\\"Gradient descent iterates\\\\")\\\\n",
                       "plt.legend()\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Reflection and Submission Checklist\\\\n",
                       "\\\\n",
                       "- I explained each concept in words before or after the code.\\\\n",
                       "- I verified important claims numerically or visually.\\\\n",
                       "- I changed or extended at least one example so the notebook reflects my own work.\\\\n",
                       "- I ran the notebook from top to bottom without errors.\\\\n",
                       "- I saved the notebook from Google Colab directly to GitHub, following the course instructions.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    }
]'''


def build_notebook() -> dict:
    return {
        "cells": json.loads(CELLS_JSON),
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "colab": {"name": "MAT422_Section_3_3_Optimization_Gradient_Descent.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_3_3_Optimization_Gradient_Descent.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()