import os
import kagglehub
import pandas as pd
from utils import save_model, save_object
from preprocessing import preprocess_data
from prefect import Flow, task
from sklearn.linear_model import Ridge


@task
def load_data() -> pd.DataFrame:
    """Download the Abalone dataset from Kaggle and return it as a DataFrame."""
    path = kagglehub.dataset_download("rodolfomendes/abalone-dataset")
    csv_path = os.path.join(path, "abalone.csv")
    df = pd.read_csv(csv_path)
    return df


@task
def preprocess(df: pd.DataFrame):
    """Preprocess the dataset."""
    X, y, scaler = preprocess_data(df)
    return X, y, scaler


@task
def train_model(X, y):
    """Train a Ridge regression model."""
    model = Ridge(alpha=1.0)
    model.fit(X, y)
    return model


@task
def save_scaler(scaler):
    """Save the scaler to a pickle file."""
    save_object(scaler, "scaler.pkl")


@task
def save_model_task(model):
    """Save the trained model."""
    save_model(model, "Ridge_Model")


with Flow("Train Model Flow") as flow:
    df = load_data()
    X, y, scaler = preprocess(df)
    model = train_model(X, y)
    save_model_task(model)
    save_scaler(scaler)

if __name__ == "__main__":
    flow.run()
