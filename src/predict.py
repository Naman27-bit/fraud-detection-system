import joblib
import pandas as pd

model = joblib.load("models/fraud_model.pkl")

# Expected training-time feature names.
# The dataset/model was trained with lowercase/other columns,
# so we map incoming API keys to the expected schema.
FEATURE_MAP = {
    "Time": "time",
    "V1": "v1",
    "V2": "v2",
    "V3": "v3",
    "Amount": "amount",
}


def predict_transaction(data: dict):
    # Convert input keys to model-expected keys
    mapped = {}
    for k, v in data.items():
        if k in FEATURE_MAP:
            mapped[FEATURE_MAP[k]] = v
        else:
            mapped[k] = v

    df = pd.DataFrame([mapped])

    # Ensure all expected columns exist (fill missing with 0)
    expected_cols = getattr(model, "feature_names_in_", None)
    if expected_cols is not None:
        for col in expected_cols:
            if col not in df.columns:
                df[col] = 0.0
        df = df[list(expected_cols)]

    prediction = model.predict(df)[0]
    return int(prediction)

