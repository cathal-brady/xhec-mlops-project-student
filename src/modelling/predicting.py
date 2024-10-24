import pandas as pd
from modules.model_utils import load_model, load_object
from prefect import Flow, task


@task
def load_trained_model():
    return load_model("Ridge_Model")


@task
def load_scaler():
    return load_object("scaler.pkl")


@task
def predict_age(model, scaler, new_data):
    new_data_scaled = scaler.transform(new_data)
    return model.predict(new_data_scaled)


with Flow("Inference Flow") as flow:
    model = load_trained_model()
    scaler = load_scaler()
    new_data = pd.DataFrame(
        [[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0]],
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
        ],
    )
    predictions = predict_age(model, scaler, new_data)

if __name__ == "__main__":
    flow.run()
