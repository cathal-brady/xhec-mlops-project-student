import os

import kagglehub
import pandas as pd
from modules.model_utils import save_model, save_object
from modules.preprocessing import preprocess_data
from prefect import Flow, task
from sklearn.linear_model import Ridge


@task
def load_data():
    path = kagglehub.dataset_download("rodolfomendes/abalone-dataset")
    csv_path = os.path.join(path, "abalone.csv")
    df = pd.read_csv(csv_path)
    return df


@task
def preprocess(df):
    X, y, scaler = preprocess_data(df)
    return X, y, scaler


@task
def train_model(X, y):
    model = Ridge(alpha=1.0)
    model.fit(X, y)
    save_model(model, "Ridge_Model")
    return model


@task
def save_scaler(scaler):
    save_object(scaler, "scaler.pkl")


with Flow("Train Model Flow") as flow:
    df = load_data()
    X, y, scaler = preprocess(df)
    model = train_model(X, y)
    save_scaler(scaler)

if __name__ == "__main__":
    flow.run()
