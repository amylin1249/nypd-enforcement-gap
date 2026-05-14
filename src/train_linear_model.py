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


def logreg_variations(X, y, penalty, C=1.0, cv=5, scoring=None):
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


def find_best_hyperparameters(X, y, penalty_list, C_list, metric):
    """
    Returns the best penalty (l2, l1) C (i.e., inverse of lambda) from the specified list of C's
    based on the given metric (e.g., accuracy, precision, recall)
    """
    mean_test_scores_penalty = {}

    for penalty in penalty_list:
        # Initialize dictionary for the given penalty to store the mean score for each C
        mean_test_scores_C = {}

        for C in C_list:
            scores = logreg_variations(X, y, penalty=penalty, C=C, scoring=metric)
            mean_test_score = np.mean(scores["test_score"])
            mean_test_scores_C[C] = mean_test_score
        
        # Determine the best C for the given penalty based on the highest mean score
        best_C = max(mean_test_scores_C, key=mean_test_scores_C.get)
        mean_test_scores_penalty[penalty] = {"best_C": best_C, "score": mean_test_scores_C[best_C]} 

    # Determine the best penalty to be used based on the highest mean score among penalties
    best_penalty = max(mean_test_scores_penalty, key=lambda k: mean_test_scores_penalty[k]["score"])

    return best_penalty, mean_test_scores_penalty[best_penalty]["best_C"], mean_test_scores_penalty[best_penalty]["score"]


def get_coefficients(X, y, penalty, C):
    """
    Determines the coefficients of the logistic regression model for the given
    samples and C value
    """
    logreg = LogisticRegression(
        penalty=penalty, C=C, solver="liblinear", class_weight="balanced"
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

    metric = "recall"
    penalty_list = ["l2", "l1"]
    C_list = [1.0, 0.1, 0.01, 0.001, 0.0001]

    # Obtain coefficients based on the selected metric and tuned hyperparameters
    best_penalty, best_C, train_score = find_best_hyperparameters(X_train, y_train, penalty_list, C_list, metric)
    coef_table_train = get_coefficients(X_train, y_train, best_penalty, best_C)
    print(f"Training set: Best penalty selected is {best_penalty}, best C selected is {best_C}, based on {metric} with score {train_score}")
    print("Training set: Estimated coefficients")
    print(coef_table_train.sort_values(by="coef", ascending=False))

    ### CALCULATE RECALL ON TEST SET (PREDICTIONS)


