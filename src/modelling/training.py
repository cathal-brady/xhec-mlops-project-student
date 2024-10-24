import os
import kagglehub
import pandas as pd
from utils import save_model, save_object
from preprocessing import preprocess_data
from prefect import task, Flow
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
    save_model(model, "Ridge_Model")  # Save the model in MLflow
    return model

@task
def save_scaler(scaler):
    save_object(scaler, "scaler.pkl")

@task
def save_model_locally(model):
    # Save the model locally in src/web_service/local_objects
    import pickle
    model_path = "src/web_service/local_objects/Ridge_Model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

def create_flow():
    # Instead of 'with Flow', just define the flow here
    flow = Flow("Train Model Flow")
    df = load_data()
    X, y, scaler = preprocess(df)
    model = train_model(X, y)
    save_scaler(scaler)
    save_model_locally(model)
    # Set task dependencies
    flow.set_dependencies(task=model, upstream_tasks=[df, X])
    return flow

if __name__ == "__main__":
    # Create and run the flow
    flow = create_flow()
    flow.run()
