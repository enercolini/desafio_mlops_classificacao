"""
This is a boilerplate pipeline 'model_score'
generated using Kedro 0.18.4
"""
from typing import Any, Dict, Tuple

import pandas as pd
from sklearn.metrics import accuracy_score


def score(cv_results, transformed_test_df):
    # Print the results for each model
    X = transformed_test_df.iloc[:,1:]
    y = transformed_test_df.iloc[:,0]
    for name, result in cv_results.items():
        print(name)
        print("Best parameters:", result.best_params_)
        print("Train score:", result.best_score_)
        print ("Test score:", accuracy_score(result.best_estimator_.predict(X), y))

    best_model = cv_results['rf'].best_estimator_

    return best_model