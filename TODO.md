# TODO

## Plan (fraud always predicted)
1. Identify why backend always returns `prediction: "Fraud"` regardless of input.
2. Update backend `POST /predict` to call `src/predict.py` (or load the model in backend) and return real model output.
3. Fix any response keys / naming and ensure Streamlit reads the correct field.
4. Add basic validation for required features.
5. Run backend locally and test via a curl/json payload.
6. Run Streamlit and verify predictions change.

