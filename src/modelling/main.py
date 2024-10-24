import os

import kagglehub  # Ensure this is correctly imported
import pandas as pd
from prefect import flow, task  # Use `flow` decorator for flow definition
from preprocessing import preprocess_data
from sklearn.linear_model import Ridge
from utils import save_model, save_object


@task
def read_data() -> pd.DataFrame:
    """Download the dataset from Kaggle and read it into a DataFrame."""
    path = kagglehub.dataset_download("rodolfomendes/abalone-dataset")
    csv_path = os.path.join(path, "abalone.csv")
    df = pd.read_csv(csv_path)
    return df


@task
def preprocess_data_task(df: pd.DataFrame) -> tuple:
    """Preprocess the data."""
    X_scaled, y, scaler = preprocess_data(df)
    return X_scaled, y, scaler


@task
def train_model_task(X_scaled: pd.DataFrame, y: pd.Series) -> Ridge:
    """Train a Ridge regression model."""
    model = Ridge(alpha=1.0)
    model.fit(X_scaled, y)
    return model


@task
def save_model_task(model: Ridge, scaler):
    """Save the model and scaler."""
    save_model(model, "Ridge_Model")
    save_object(scaler, "scaler.pkl")


@flow  # Use the `flow` decorator for defining the flow
def main() -> None:
    """Train a model using the data downloaded from Kaggle
    and save the model."""
    # Load data and train the model
    df = read_data()
    X_scaled, y, scaler = preprocess_data_task(df)
    model = train_model_task(X_scaled, y)
    save_model_task(model, scaler)


if __name__ == "__main__":
    main()
