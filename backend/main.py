from fastapi import FastAPI

# Use the real model scorer from src/predict.py
from src.predict import predict_transaction

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.post("/predict")
def predict(data: dict):
    # Expect numeric fields: Time, V1, V2, V3, Amount
    # Model returns int label; map it to human-readable classes.
    label = predict_transaction(data)
    prediction = "Fraud" if int(label) == 1 else "Not Fraud"

    return {
        "prediction": prediction,
        "prediction_label": int(label),
        "received_data": data,
    }
