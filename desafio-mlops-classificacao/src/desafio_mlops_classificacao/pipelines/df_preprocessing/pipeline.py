"""
This is a boilerplate pipeline 'df_preprocessing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_data,
            inputs=["train_df", "test_df"],
            outputs=["transformed_train_df", "transformed_test_df"],
            name="preprocess_data"
        )
    ])
