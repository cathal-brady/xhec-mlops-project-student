import pandas as pd
from utils import load_model, load_object
from prefect import Flow, task

# Define tasks to load the model and scaler
@task
def load_trained_model():
    """Load the trained Ridge Regression model."""
    return load_model("Ridge_Model")


@task
def load_scaler():
    """Load the pre-fitted scaler object."""
    return load_object("scaler.pkl")


@task
def predict_age(model, scaler, new_data):
    """Scale the input data and predict the age using the trained model."""
    new_data_scaled = scaler.transform(new_data)
    return model.predict(new_data_scaled)


def get_prediction(input_data):
    """Run the prediction flow for new input data."""
    # Convert input data to a DataFrame with the required structure
    new_data = pd.DataFrame(
        [input_data],
        columns=[
            "Length",
            "Diameter",
            "Height",
            "Whole_weight",
            "Shucked_weight",
            "Viscera_weight",
            "Shell_weight",
            "Male",
            "Female",
            "Infant"
        ],
    )

    # Define the flow for loading the model and making predictions
    with Flow("Inference Flow") as flow:
        model = load_trained_model()
        scaler = load_scaler()
        predictions = predict_age(model, scaler, new_data)

    # Run the flow and return the prediction result
    state = flow.run()
    return state.result[predictions].result[0]  # Return the first prediction
