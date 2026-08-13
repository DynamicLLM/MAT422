# Problem Statement

## Background
A university wants an early-warning model to identify students who may be at risk of not meeting a target final-course performance threshold.

## Inputs
- Weekly study hours
- Attendance rate
- Prior GPA
- Assignment average

## Target
Binary indicator: final performance meets the selected threshold.

## Objective
Develop a predictive model that identifies at-risk students with strong validation performance while avoiding data leakage.

## Constraints
- Binary classification
- Five-fold cross-validation
- Use only variables available before the prediction point
- Compare at least two models
- Report accuracy, F1, precision, recall, and ROC-AUC

## Success criteria
The final model should outperform a simple baseline on the primary validation metric while maintaining acceptable recall for the at-risk class.

The threshold and final metric should be justified by the student rather than copied from this example.
