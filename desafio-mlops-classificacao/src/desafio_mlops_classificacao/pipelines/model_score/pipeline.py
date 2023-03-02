"""
This is a boilerplate pipeline 'model_score'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import score


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=score,
            inputs=["cv_results", "transformed_test_df"],
            outputs="best_model",
            name="score"
        )
    ])
