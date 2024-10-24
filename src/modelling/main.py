# This module is the training flow: it reads the data, preprocesses it, trains a model, and saves it.

import argparse
from pathlib import Path
from prefect import Flow, task
import pandas as pd
from utils import save_model, save_object
from preprocessing import preprocess_data
from sklearn.linear_model import Ridge

@task
def read_data(trainset_path: Path) -> pd.DataFrame:
    """Read the dataset from the given path."""
    return pd.read_csv(trainset_path)


@task
def preprocess_data_task(df: pd.DataFrame):
    """Preprocess the data."""
    X_scaled, y, scaler = preprocess_data(df)
    return X_scaled, y, scaler


@task
def train_model_task(X_scaled, y):
    """Train a Ridge regression model."""
    model = Ridge(alpha=1.0)
    model.fit(X_scaled, y)
    return model


@task
def save_model_task(model, scaler):
    """Save the model and scaler."""
    save_model(model, "Ridge_Model")
    save_object(scaler, "scaler.pkl")


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model."""
    with Flow("Training Flow") as flow:
        # Load data and train the model
        df = read_data(trainset_path)
        X_scaled, y, scaler = preprocess_data_task(df)
        model = train_model_task(X_scaled, y)
        save_model_task(model, scaler)

    # Run the flow
    flow.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(Path(args.trainset_path))
