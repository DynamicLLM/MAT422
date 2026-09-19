#!/usr/bin/env python3
"""Generate a MAT 422 - Sections 3.5 and 3.6: K-means and Support Vector Machines starter Jupyter Notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CELLS_JSON = r'''[
    {
        "source":  [
                       "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DynamicLLM/MAT422/blob/main/Skills/Student-Home-Work-Skills-Pack/mat422-section-3-5-3-6-kmeans-svm/assets/MAT422_Section_3_5_3_6_KMeans_SVM.ipynb)\\\\n",
                       "\\\\n",
                       "# MAT 422 - Sections 3.5 and 3.6: K-means and Support Vector Machines\\\\n",
                       "\\\\n",
                       "**Topics:** K-means, Support vector machine\\\\n",
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
                       "from sklearn.datasets import make_blobs, make_classification\\\\n",
                       "from sklearn.cluster import KMeans\\\\n",
                       "from sklearn.svm import SVC\\\\n",
                       "from sklearn.metrics import accuracy_score\\\\n",
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
                       "## K-means\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **K-means**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "X, true_labels = make_blobs(n_samples=180, centers=3, cluster_std=0.7, random_state=422)\\\\n",
                       "kmeans = KMeans(n_clusters=3, n_init=10, random_state=422)\\\\n",
                       "cluster_labels = kmeans.fit_predict(X)\\\\n",
                       "\\\\n",
                       "print(\\\\"Cluster centers:\\\\")\\\\n",
                       "print(kmeans.cluster_centers_)\\\\n",
                       "print(\\\\"Inertia:\\\\", kmeans.inertia_)\\\\n",
                       "\\\\n",
                       "plt.scatter(X[:,0], X[:,1], c=cluster_labels, cmap=\\\\"viridis\\\\", alpha=0.8)\\\\n",
                       "plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker=\\\\"X\\\\", s=200, color=\\\\"red\\\\")\\\\n",
                       "plt.title(\\\\"K-means clustering\\\\")\\\\n",
                       "plt.show()\\\\n"
                   ],
        "cell_type":  "code",
        "execution_count":  null,
        "metadata":  {

                     }
    },
    {
        "source":  [
                       "## Support vector machine\\\\n",
                       "\\\\n",
                       "This section gives one compact Python demonstration of **Support vector machine**. After running the code, add your own interpretation and change at least one input, parameter, or example so the notebook reflects your own work.\\\\n"
                   ],
        "cell_type":  "markdown",
        "metadata":  {

                     }
    },
    {
        "outputs":  [

                    ],
        "source":  [
                       "Xc, yc = make_classification(n_samples=140, n_features=2, n_redundant=0, n_informative=2,\\\\n",
                       "                             n_clusters_per_class=1, class_sep=1.3, random_state=422)\\\\n",
                       "svm = SVC(kernel=\\\\"linear\\\\", C=1.0)\\\\n",
                       "svm.fit(Xc, yc)\\\\n",
                       "pred = svm.predict(Xc)\\\\n",
                       "\\\\n",
                       "print(\\\\"Training accuracy:\\\\", accuracy_score(yc, pred))\\\\n",
                       "print(\\\\"Number of support vectors:\\\\", svm.n_support_)\\\\n",
                       "\\\\n",
                       "xx, yy = np.meshgrid(np.linspace(Xc[:,0].min()-1, Xc[:,0].max()+1, 150),\\\\n",
                       "                     np.linspace(Xc[:,1].min()-1, Xc[:,1].max()+1, 150))\\\\n",
                       "Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)\\\\n",
                       "\\\\n",
                       "plt.contour(xx, yy, Z, levels=[-1, 0, 1], colors=[\\\\"gray\\\\", \\\\"black\\\\", \\\\"gray\\\\"], linestyles=[\\\\"--\\\\", \\\\"-\\\\", \\\\"--\\\\"])\\\\n",
                       "plt.scatter(Xc[:,0], Xc[:,1], c=yc, cmap=\\\\"bwr\\\\", edgecolor=\\\\"white\\\\")\\\\n",
                       "plt.scatter(svm.support_vectors_[:,0], svm.support_vectors_[:,1], s=120, facecolors=\\\\"none\\\\", edgecolors=\\\\"black\\\\", label=\\\\"support vectors\\\\")\\\\n",
                       "plt.title(\\\\"Linear SVM margin and support vectors\\\\")\\\\n",
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
            "colab": {"name": "MAT422_Section_3_5_3_6_KMeans_SVM.ipynb"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="MAT422_Section_3_5_3_6_KMeans_SVM.ipynb", help="Output notebook path")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_notebook(), indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()