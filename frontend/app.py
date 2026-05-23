import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression
import requests

API_URL = "http://localhost:8000/predict"

# Dummy training
X = np.array([
    [100, 1],
    [5000, 0],
    [200, 1],
    [9000, 0]
])

y = np.array([0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

st.title("Fraud Detection System")

amount = st.number_input("Transaction Amount")
location = st.selectbox("International Transaction?", [0, 1])

if st.button("Predict"):

    prediction = model.predict([[amount, location]])

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
 
 
        st.success("Authentic Transaction")



st.title("Fintech Fraud Detection System")

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

    response = requests.post(API_URL, data=payload)
    print("status:", response.status_code)
    print("content;",response.text)

    if response.status_code== 200:
        try:
            prediction=response.json()

            if prediction[0] == 1:
                st.error("Fraud Transaction")
            else:
                st.success("Authentic Transaction")
        except Exception as e:
            st.error(f"Error parsing response: {e}")
            prediction = None

    result = None
    try:
        result = response.json()
    except Exception:
        result = {}

    if "prediction" in result:
        st.success(result["prediction"])

    else:
        st.error(result["error"])
