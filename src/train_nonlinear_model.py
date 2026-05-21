import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from train_linear_model import split_dataset
from datatypes import CLEAN_SQF
import warnings

# Silence warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)


# decision tree
def dt_variations(X, y, max_depth=None, cv=5, scoring="f1"):
    """
    Decision Tree model doing cross validation
    """
    dt = DecisionTreeClassifier(max_depth=max_depth, random_state=123)
    scores = cross_validate(dt, X, y, cv=cv, return_train_score=True, scoring=scoring)
    return scores


def find_best_dt_depth(X, y, depth_list, metric="f1"):
    """
    Find best depth of Decision Tree
    """
    results = {}
    for depth in depth_list:
        scores = dt_variations(X, y, max_depth=depth, scoring=metric)
        results[depth] = np.mean(scores["test_score"])
    return max(results, key=results.get)


def get_dt_importance(X, y, best_depth):
    """
    train decision tree and get importance.
    """
    dt = DecisionTreeClassifier(max_depth=best_depth, random_state=123)
    dt.fit(X, y)

    importance_table = pd.DataFrame(
        {"features": X.columns, "importance": dt.feature_importances_}
    )
    return importance_table.sort_values(by="importance", ascending=False)


## random forest
def rf_variations(X, y, max_depth=None, n_estimators=100, cv=5, scoring="f1"):
    """
    Random Forest model doing cross validation
    """
    rf = RandomForestClassifier(
        n_estimators=n_estimators, max_depth=max_depth, random_state=123
    )
    scores = cross_validate(rf, X, y, cv=cv, return_train_score=True, scoring=scoring)
    return scores


def find_best_rf_depth(X, y, depth_list, metric="f1"):
    """
    Find best depth of Random Forest
    """
    results = {}
    for depth in depth_list:
        scores = rf_variations(X, y, max_depth=depth, scoring=metric)
        results[depth] = np.mean(scores["test_score"])
    return max(results, key=results.get)


def get_rf_importance(X, y, best_depth):
    """
    train decision tree and get importance.
    """
    rf = RandomForestClassifier(
        n_estimators=100, max_depth=best_depth, random_state=123
    )
    rf.fit(X, y)

    importance_table = pd.DataFrame(
        {"features": X.columns, "importance": rf.feature_importances_}
    )
    return importance_table.sort_values(by="importance", ascending=False)


if __name__ == "__main__":
    # Show results in full
    pd.set_option("display.max_rows", None)
    pd.set_option("display.show_dimensions", False)
    pd.set_option("display.width", None)

    X_train, X_test, y_train, y_test = split_dataset()

    depths = [3, 5, 10, 20, None]
    metrics = ["recall", "f1"]

    for metric in metrics:
        # Decision Tree
        best_dt_d = find_best_dt_depth(X_train, y_train, depths, metric=metric)
        dt_importance = get_dt_importance(X_train, y_train, best_dt_d)
        dt_scores = dt_variations(X_train, y_train, max_depth=best_dt_d, scoring=metric)
        print(f"\n[Decision Tree]")
        print(f"Mean Train {metric.upper()}: {np.mean(dt_scores['train_score']):.4f}")
        print(f"Mean Test {metric.upper()}: {np.mean(dt_scores['test_score']):.4f}")
        print(f"Best Decision Tree Depth: {best_dt_d}")
        print(f"Decision Tree Feature Importance: {dt_importance}")

        # Random Forest
        best_rf_d = find_best_rf_depth(X_train, y_train, depths, metric=metric)
        rf_importance = get_rf_importance(X_train, y_train, best_rf_d)
        rf_scores = rf_variations(X_train, y_train, max_depth=best_rf_d, scoring=metric)
        print(f"\n[Random Forest]")
        print(f"Best Random Forest Depth: {best_rf_d}")
        print(f"Mean Train {metric.upper()}: {np.mean(rf_scores['train_score']):.4f}")
        print(f"Mean Test {metric.upper()}: {np.mean(rf_scores['test_score']):.4f}")
        print(f"Random Forest Feature Importance: {rf_importance}")
