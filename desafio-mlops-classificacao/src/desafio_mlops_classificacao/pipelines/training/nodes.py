"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.4
"""

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification

def grid_search_models(transformed_train_df):

    X = transformed_train_df.iloc[:,1:]
    y = transformed_train_df.iloc[:,0]

    # Create a OneHotEncoder
    column_transformer = ColumnTransformer(
        transformers=[
            ('one_hot', OneHotEncoder(handle_unknown='ignore'), ['Pclass', 'Sex', 'Embarked'])  
        ],
        remainder='passthrough'
    )

### MODELS
    # Define the models you want to evaluate
    models = [
        ('rf', RandomForestClassifier()),
        ('dt', DecisionTreeClassifier()),
        ('hgb', GradientBoostingClassifier())
    ]

    # Define the parameters you want to search over for each model
    param_grids = {
        'rf': {
            'model__n_estimators': [50, 100, 200],
            'model__max_depth': [5, 10, 15],
        },
        'dt': {
            'model__max_depth': [5, 10, 15],
        },
        'hgb': {
            'model__max_depth': [5, 10, 15],
            'model__learning_rate': [0.1, 0.01],
        }
    }

# Use GridSearchCV to search over the parameter grid for each model
    cv_results = {}
    for name, model in models:
        pipeline = Pipeline([
            ('transformer', column_transformer),
            ('model', model)
        ])
        search = GridSearchCV(pipeline, param_grids[name], cv=5, n_jobs=-1)
        search.fit(X, y)
        cv_results[name] = search

    return cv_results
