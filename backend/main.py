from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/predict")
def predict(data: dict):
    return {
        "prediction": "Fraud",
        "recieved_data": data
    }