import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("FinTech Fraud Detection System")

st.subheader("Enter Transaction Details")

time = st.number_input("Time")
amount = st.number_input("Amount")
v1 = st.number_input("V1")
v2 = st.number_input("V2")
v3 = st.number_input("V3")
v4 = st.number_input("V4")

if st.button("Predict Fraud"):

    payload = {
        "Time": time,
        "Amount": amount,
        "V1": v1,
        "V2": v2,
        "V3": v3,
        "V4": v4
    }

    response = requests.post(API_URL, json=payload)

    result = response.json()

    if "prediction" in result:
        st.success(result["prediction"])

    else:
        st.error(result["error"])
