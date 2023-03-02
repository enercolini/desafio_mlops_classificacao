"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from desafio_mlops_classificacao.pipelines import (
    df_preprocessing,
    training,
    model_score,
)

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    
    df_preprocessing_pipeline = df_preprocessing.create_pipeline()
    training_pipeline = training.create_pipeline()
    model_score_pipeline = model_score.create_pipeline()

    return {
        "preprocessing": df_preprocessing_pipeline,
        "train": training_pipeline,
        "score": model_score_pipeline,
        "__default__": 
            df_preprocessing_pipeline
            + training_pipeline
            + model_score_pipeline
    }
