import joblib
import pandas as pd

model = joblib.load("models/fraud_model.pkl")

def predict_transaction(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return int(prediction)