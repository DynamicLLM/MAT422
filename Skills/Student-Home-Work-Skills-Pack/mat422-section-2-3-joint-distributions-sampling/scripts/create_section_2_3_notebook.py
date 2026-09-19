#!/usr/bin/env python3
"""Generate a MAT 422 - Section 2.3: Joint Distributions, Dependence, and Sampling starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CELLS_JSON = r'''[
    {
        "source":  [
                       "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/Student-Home-Work-Skills-Pack/mat422-section-2-3-joint-distributions-sampling/assets/MAT422_Section_2_3_Joint_Distributions_Sampling.ipynb)\\\\n",
                       "\\\\n",
                       "# MAT 422 - Section 2.3: Joint Distributions, Dependence, and Sampling\\\\n",
                       "\\\\n",
                       "**Topics:** Joint probability distributions, Correlation and dependence, Random samples\\\\n",
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
                       "np.set_printoptions(precision=4, suppress=True)\\\\n",
                       "rng = np.random.default_rng(422)\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Joint probability distributions\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Joint probability distributions**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "joint = np.array([[0.10, 0.20, 0.10],\\\\n",
                       "                  [0.05, 0.25, 0.30]])\\\\n",
                       "x_values = np.array([0, 1])\\\\n",
                       "y_values = np.array([0, 1, 2])\\\\n",
                       "\\\\n",
                       "px = joint.sum(axis=1)\\\\n",
                       "py = joint.sum(axis=0)\\\\n",
                       "print(\\\\"Joint total =\\\\", joint.sum())\\\\n",
                       "print(\\\\"P(X) =\\\\", px)\\\\n",
                       "print(\\\\"P(Y) =\\\\", py)\\\\n",
                       "print(\\\\"P(Y=2 | X=1) =\\\\", joint[1, 2] / px[1])\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Correlation and dependence\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Correlation and dependence**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "x = rng.normal(0, 1, 200)\\\\n",
                       "y_dependent = 2 * x + rng.normal(0, 0.5, 200)\\\\n",
                       "y_independent = rng.normal(0, 1, 200)\\\\n",
                       "\\\\n",
                       "print(\\\\"corr(x, dependent y) =\\\\", np.corrcoef(x, y_dependent)[0, 1])\\\\n",
                       "print(\\\\"corr(x, independent y) =\\\\", np.corrcoef(x, y_independent)[0, 1])\\\\n",
                       "\\\\n",
                       "plt.scatter(x, y_dependent, alpha=0.7, label=\\\\"dependent\\\\")\\\\n",
                       "plt.scatter(x, y_independent, alpha=0.5, label=\\\\"mostly independent\\\\")\\\\n",
                       "plt.legend()\\\\n",
                       "plt.title(\\\\"Correlation as a dependence summary\\\\")\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Random samples\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Random samples**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "sample_means = []\\\\n",
                       "for _ in range(1000):\\\\n",
                       "    sample = rng.exponential(scale=2.0, size=30)\\\\n",
                       "    sample_means.append(sample.mean())\\\\n",
                       "\\\\n",
                       "sample_means = np.array(sample_means)\\\\n",
                       "print(\\\\"Mean of sample means =\\\\", sample_means.mean())\\\\n",
                       "print(\\\\"Std of sample means =\\\\", sample_means.std())\\\\n",
                       "\\\\n",
                       "plt.hist(sample_means, bins=30, color=\\\\"tab:green\\\\", edgecolor=\\\\"white\\\\")\\\\n",
                       "plt.title(\\\\"Sampling distribution of the sample mean\\\\")\\\\n",
                       "plt.xlabel(\\\\"sample mean\\\\")\\\\n",
                       "plt.ylabel(\\\\"count\\\\")\\\\n",
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
            "colab": {"name": "MAT422_Section_2_3_Joint_Distributions_Sampling.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_2_3_Joint_Distributions_Sampling.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()