import os
import kagglehub
import pandas as pd
from utils import save_model, save_object
from preprocessing import preprocess_data
from prefect import Flow, task
from sklearn.linear_model import Ridge


# Define the Prefect tasks
@task
def load_data():
    """Download and load the Abalone dataset."""
    path = kagglehub.dataset_download("rodolfomendes/abalone-dataset")
    csv_path = os.path.join(path, "abalone.csv")
    df = pd.read_csv(csv_path)
    return df

@task
def preprocess(df):
    """Preprocess the data (scaling and feature engineering)."""
    X, y, scaler = preprocess_data(df)
    return X, y, scaler

@task
def train_model(X, y):
    """Train a Ridge regression model."""
    model = Ridge(alpha=1.0)
    model.fit(X, y)
    save_model(model, "Ridge_Model")
    return model

@task
def save_scaler(scaler):
    """Save the fitted scaler object."""
    save_object(scaler, "scaler.pkl")


# Now we define the flow explicitly
def create_flow():
    # Create a flow object
    flow = Flow("Train Model Flow")
    
    # Add tasks to the flow
    df = load_data()
    X, y, scaler = preprocess(df)
    model = train_model(X, y)
    save_scaler(scaler)
    
    # Return the flow object
    return flow

if __name__ == "__main__":
    # Create and run the flow
    flow = create_flow()
    flow.run()
