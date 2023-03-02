"""
This is a boilerplate pipeline 'df_preprocessing'
generated using Kedro 0.18.4
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_data(train_df, test_df):
    """
    Node that transform train and test dataset, eliminating useless features and replacing null values
    """
    # Train Dataset Transformation
    train_df = train_df.drop(columns=['Name', 'Ticket', 'Cabin'])
    new_column_order = ['Survived', 'PassengerId','Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    train_df = train_df[new_column_order]
    train_df = train_df.dropna(subset=['Embarked'])
    train_df['Age'] = train_df.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.mean())).round(0).astype('Int64')

    train, test = train_test_split(train_df, test_size=0.25)

    return train, test
