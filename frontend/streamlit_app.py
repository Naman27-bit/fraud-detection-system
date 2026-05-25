import requests
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://localhost:8000/predict")

st.set_page_config(page_title="Fraud Detection", layout="centered")
st.title("💳 Fintech Fraud Detection")
st.caption("Enter transaction features to get a fraud prediction.")

with st.form("fraud_form"):
    st.subheader("Transaction Inputs")

    Time = st.number_input("Time", value=0.0, format="%f")
    V1 = st.number_input("V1", value=0.0, format="%f")
    V2 = st.number_input("V2", value=0.0, format="%f")
    V3 = st.number_input("V3", value=0.0, format="%f")
    Amount = st.number_input("Amount", value=0.0, format="%f")

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "Time": float(Time),
        "V1": float(V1),
        "V2": float(V2),
        "V3": float(V3),
        "Amount": float(Amount),
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=30)
        res.raise_for_status()
        data = res.json()
        prediction = data.get("prediction", "Unknown")

        st.success(f"Prediction: **{prediction}**")
        st.write("Model response:")
        st.json(data)

    except requests.exceptions.RequestException as e:
        st.error("Request to backend failed.")
        st.write(f"API_URL: {API_URL}")
        st.exception(e)

