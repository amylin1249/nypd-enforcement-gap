import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from datatypes import FINAL_SQF


def normalize_continuous_features():
    """
    ADD DOCSTRING
    """
    final_df = pd.read_csv(FINAL_SQF)
    continuous_features = ["SUSPECT_REPORTED_AGE", "STOP_LOCATION_PRECINCT"]
    
    for feature in continuous_features:
        x_array = np.array(final_df[feature])
        normalized = preprocessing.normalize([x_array])
        final_df[feature] = normalized[0]

    return final_df


def split_dataset():
    """
    ADD DOCSTRING
    """
    normalized_df = normalize_continuous_features()

    features = normalized_df.columns.difference(["use_of_force"]).values
    X = normalized_df[features]
    y = normalized_df["use_of_force"]
    return train_test_split(X, y, test_size=0.2, random_state=123)


def logreg_variations(X, y, penalty = "l2", C = 1.0, cv = 5, scoring = None):
    """
    ADD DOCSTRING
    """
    logreg = LogisticRegression(penalty = penalty, C = C, solver = "liblinear")
    scores = cross_validate(logreg, X, y, cv=cv, return_train_score=True, scoring = scoring)
    return scores


def find_best_C(X, y, C_list):
    """
    ADD DOCSTRING
    Based on accuracy (have not calculated precision or recall yet)
    """
    mean_test_scores = {}
    
    for C in C_list:
        scores = logreg_variations(X, y, C = C)
        mean_test_score =  np.mean(scores["test_score"])
        mean_test_scores[C] = mean_test_score
    
    return max(mean_test_scores, key=mean_test_scores.get)


def get_coefficients(X, y, C):
    """
    ADD DOCSTRING
    """
    logreg = LogisticRegression(penalty = "l2", C = C, solver = "liblinear")
    logreg.fit(X, y)

    # Organize features and corresponding coefficients into a table
    coef_table = pd.DataFrame(zip(X.columns, np.transpose(logreg.coef_)), columns=["features", "coef"])
    
    return coef_table


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = split_dataset()
    best_C = find_best_C(X_train, y_train, [1.0, 0.1, 0.01, 0.001, 0.0001])
    coef_table = get_coefficients(X_train, y_train, best_C)
    print(coef_table.sort_values(by="coef", ascending=False))

    # scores = logreg_variations(X_train, y_train, best_C)
    # mean_train_score = np.mean(scores["train_score"])
    # mean_test_score =  np.mean(scores["test_score"])
    # print(f"Mean cross validation train score is {mean_train_score} and mean cross validation test score is {mean_test_score}")