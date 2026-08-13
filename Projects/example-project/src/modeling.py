"""Minimal example source file for the MAT 422 project structure.

Students should replace this with their own validated implementation.
"""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "example.csv"


def main() -> None:
    df = pd.read_csv(DATA)
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    models = {
        "logistic_regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=2000)),
        ]),
        "svm": Pipeline([
            ("scale", StandardScaler()),
            ("model", SVC(probability=True)),
        ]),
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    for name, model in models.items():
        scores = cross_validate(
            model,
            X_train,
            y_train,
            cv=cv,
            scoring=["accuracy", "f1", "roc_auc"],
        )
        print(name)
        print("CV accuracy:", scores["test_accuracy"].mean())
        print("CV F1:", scores["test_f1"].mean())
        print("CV ROC-AUC:", scores["test_roc_auc"].mean())
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        prob = model.predict_proba(X_test)[:, 1]
        print("Test accuracy:", accuracy_score(y_test, pred))
        print("Test F1:", f1_score(y_test, pred))
        print("Test ROC-AUC:", roc_auc_score(y_test, prob))


if __name__ == "__main__":
    main()
