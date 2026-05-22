from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load(r"C:\Users\DELL\OneDrive\Desktop\fintech fraud detection\models\fraud_model.pkl")

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    Amount: float

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(data: Transaction):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    result = "Fraud" if prediction == 1 else "Not Fraud"

    return {
        "prediction": result
    }
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load(r"C:\Users\DELL\OneDrive\Desktop\fintech fraud detection\models\fraud_model.pkl")

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    Amount: float

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(data: Transaction):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    result = "Fraud" if prediction == 1 else "Not Fraud"

    return {
        "prediction": result
    }

