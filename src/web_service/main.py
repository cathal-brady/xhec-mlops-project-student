import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modelling.predicting import get_prediction

app = FastAPI(
    title="Abalone Age Prediction API",
    description="Predict the age of abalone using a Ridge Regression model."
)

# Pydantic schema for input validation
class AbaloneFeatures(BaseModel):
    length: float
    diameter: float
    height: float
    whole_weight: float
    shucked_weight: float
    viscera_weight: float
    shell_weight: float
    sex: str

# Define Pydantic model for the response
class PredictionResponse(BaseModel):
    predicted_age: float

# Health check route
@app.get("/")
def home() -> dict:
    return {"health_check": "App is running"}

# Prediction route
@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(payload: AbaloneFeatures) -> PredictionResponse:
    # Convert the input into the required format for prediction
    input_data = [
        payload.length, payload.diameter, payload.height, payload.whole_weight,
        payload.shucked_weight, payload.viscera_weight, payload.shell_weight,
        1 if payload.sex == 'M' else 0,  # Male
        1 if payload.sex == 'F' else 0,  # Female
        1 if payload.sex == 'I' else 0   # Infant
    ]

    try:
        predicted_age = get_prediction(input_data)  # Call the prediction function
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

    return PredictionResponse(predicted_age=predicted_age)  