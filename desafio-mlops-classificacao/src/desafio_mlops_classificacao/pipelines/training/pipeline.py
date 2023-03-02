"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import grid_search_models

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=grid_search_models,
            inputs="transformed_train_df",
            outputs="cv_results",
            name="grid_search_models"
        )
    ])