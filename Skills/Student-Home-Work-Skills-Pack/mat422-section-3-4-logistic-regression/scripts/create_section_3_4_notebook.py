#!/usr/bin/env python3
"""Generate a MAT 422 - Section 3.4: Logistic Regression starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CELLS_JSON = r'''[
    {
        "source":  [
                       "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/Student-Home-Work-Skills-Pack/mat422-section-3-4-logistic-regression/assets/MAT422_Section_3_4_Logistic_Regression.ipynb)\\\\n",
                       "\\\\n",
                       "# MAT 422 - Section 3.4: Logistic Regression\\\\n",
                       "\\\\n",
                       "**Topics:** Sigmoid/logistic function, Binary classification probabilities, Logistic regression fitting and interpretation\\\\n",
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
                       "from sklearn.datasets import make_classification\\\\n",
                       "from sklearn.linear_model import LogisticRegression\\\\n",
                       "from sklearn.metrics import accuracy_score, confusion_matrix\\\\n",
                       "\\\\n",
                       "np.set_printoptions(precision=4, suppress=True)\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Sigmoid/logistic function\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Sigmoid/logistic function**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "def sigmoid(z):\\\\n",
                       "    return 1 / (1 + np.exp(-z))\\\\n",
                       "\\\\n",
                       "z = np.linspace(-8, 8, 300)\\\\n",
                       "plt.plot(z, sigmoid(z))\\\\n",
                       "plt.axhline(0.5, color=\\\\"black\\\\", linewidth=0.8)\\\\n",
                       "plt.xlabel(\\\\"z\\\\")\\\\n",
                       "plt.ylabel(\\\\"sigmoid(z)\\\\")\\\\n",
                       "plt.title(\\\\"Logistic function maps real numbers to probabilities\\\\")\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Binary classification probabilities\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Binary classification probabilities**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "X, y = make_classification(n_samples=120, n_features=2, n_redundant=0, n_informative=2,\\\\n",
                       "                           n_clusters_per_class=1, class_sep=1.2, random_state=422)\\\\n",
                       "model = LogisticRegression()\\\\n",
                       "model.fit(X, y)\\\\n",
                       "pred = model.predict(X)\\\\n",
                       "proba = model.predict_proba(X)[:, 1]\\\\n",
                       "\\\\n",
                       "print(\\\\"Coefficients:\\\\", model.coef_)\\\\n",
                       "print(\\\\"Intercept:\\\\", model.intercept_)\\\\n",
                       "print(\\\\"Training accuracy:\\\\", accuracy_score(y, pred))\\\\n",
                       "print(\\\\"Confusion matrix:\\\\")\\\\n",
                       "print(confusion_matrix(y, pred))\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Logistic regression fitting and interpretation\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Logistic regression fitting and interpretation**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 150),\\\\n",
                       "                     np.linspace(X[:,1].min()-1, X[:,1].max()+1, 150))\\\\n",
                       "grid = np.c_[xx.ravel(), yy.ravel()]\\\\n",
                       "zz = model.predict_proba(grid)[:, 1].reshape(xx.shape)\\\\n",
                       "\\\\n",
                       "plt.contourf(xx, yy, zz, levels=20, cmap=\\\\"RdBu\\\\", alpha=0.6)\\\\n",
                       "plt.colorbar(label=\\\\"P(class 1)\\\\")\\\\n",
                       "plt.scatter(X[:,0], X[:,1], c=y, edgecolor=\\\\"white\\\\", cmap=\\\\"bwr\\\\")\\\\n",
                       "plt.title(\\\\"Logistic regression probability surface\\\\")\\\\n",
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
            "colab": {"name": "MAT422_Section_3_4_Logistic_Regression.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_3_4_Logistic_Regression.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()