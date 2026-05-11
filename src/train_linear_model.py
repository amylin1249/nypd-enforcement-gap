import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import UndefinedMetricWarning
from datatypes import CLEAN_SQF
import warnings

# Silence warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)


def split_dataset():
    """
    Splits the cleaned SQF dataset into training and testing sets.
    """
    clean_df = pd.read_csv(CLEAN_SQF)

    features = clean_df.columns.difference(["USE_OF_FORCE_FLAG"]).values
    X = clean_df[features]
    y = clean_df["USE_OF_FORCE_FLAG"]

    return train_test_split(X, y, test_size=0.2, random_state=123)


def logreg_variations(X, y, penalty="l2", C=1.0, cv=5, scoring=None):
    """
    Performs cross-validation for a logistic regression model with specified C.
    """
    logreg = LogisticRegression(
        penalty=penalty, C=C, solver="liblinear", class_weight="balanced"
    )
    scores = cross_validate(
        logreg, X, y, cv=cv, return_train_score=True, scoring=scoring
    )
    return scores


##included "metric", so we can just put different metrics to compare
def find_best_C(X, y, C_list, metric):
    """
    Returns the best C (i.e., inverse of lambda) from the specified list of C's
    based on the given metric (e.g., accuracy, precision, recall)
    """
    mean_test_scores = {}

    for C in C_list:
        scores = logreg_variations(X, y, C=C, scoring=metric)
        mean_test_score = np.mean(scores["test_score"])
        mean_test_scores[C] = mean_test_score

    return max(mean_test_scores, key=mean_test_scores.get)


def get_coefficients(X, y, C):
    """
    Determines the coefficients of the logistic regression model for the given
    samples and C value
    """
    logreg = LogisticRegression(
        penalty="l2", C=C, solver="liblinear", class_weight="balanced"
    )
    logreg.fit(X, y)

    # Organize features and corresponding coefficients into a table
    coef_table = pd.DataFrame(
        zip(X.columns, np.transpose(logreg.coef_)), columns=["features", "coef"]
    )

    return coef_table


if __name__ == "__main__":
    # Show results in full
    pd.set_option("display.max_rows", None)
    pd.set_option("display.show_dimensions", False)
    pd.set_option("display.width", None)

    X_train, X_test, y_train, y_test = split_dataset()

    C_list = [1.0, 0.1, 0.01, 0.001, 0.0001]
    metrics = ["accuracy", "precision", "recall", "f1"]
    for metric in metrics:
        best_C = find_best_C(X_train, y_train, C_list, metric)
        coef_table = get_coefficients(X_train, y_train, best_C)
        print(f"Estimated coefficients (using the best C based on {metric}):")
        print(coef_table.sort_values(by="coef", ascending=False))
        print()
