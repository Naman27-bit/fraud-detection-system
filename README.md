# Fintech Fraud Detection (FastAPI + Streamlit)

This project provides a simple end-to-end fintech fraud detection application:

- **Backend API** (FastAPI) exposes an endpoint to score transactions.
- **Frontend UI** (Streamlit) collects transaction features and displays predictions.
- A pre-trained model is loaded from `models/fraud_model.pkl`.
- Services can be run together using **Docker Compose**.

---

## Project Structure

- `backend/`
  - `app.py` - FastAPI server with `/predict` endpoint
  - `requirements.txt`
  - `Dockerfile`
- `frontend/`
  - `app.py` - (may be an alternative UI entrypoint)
  - `streamlit_app.py` - Streamlit UI
  - `requirements.txt`
  - `Dockerfile`
- `models/`
  - `fraud_model.pkl` - trained ML model (loaded by backend)
- `src/`
  - `main.py`, `predict.py` - helper scripts (if used during experimentation)
- `docker-compose.yml` - orchestrates `backend` and `frontend`

---

## Backend (FastAPI)

### Endpoints

- `GET /`
  - Health check: returns a message
- `POST /predict`
  - **Body**: JSON with the following fields:
    - `Time` (float)
    - `V1` (float)
    - `V2` (float)
    - `V3` (float)
    - `Amount` (float)
  - **Response**:
    - `prediction`: `"Fraud"` or `"Not Fraud"`

### Run backend locally (without Docker)

```bash
pip install -r backend/requirements.txt
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

> Note: the backend currently loads the model from `models/fraud_model.pkl`. Ensure that file exists.

---

## Frontend (Streamlit)

The Streamlit app renders a form with transaction inputs and sends them to the backend API.

- Default backend URL:
  - `http://backend:8000/predict` (when running with Docker)
- Configurable via Streamlit secrets:
  - `API_URL`

### Run frontend locally (without Docker)

```bash
pip install -r frontend/requirements.txt
streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

---

## Run with Docker Compose

This starts both services:

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:8501`

```bash
docker compose up --build
```

---

## API Request Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Time": 0.0,
    "V1": 0.1,
    "V2": -0.2,
    "V3": 0.3,
    "Amount": 100.0
  }'
```

---

## Notes / Troubleshooting

1. **Model file**
   - Ensure `models/fraud_model.pkl` exists.
2. **Backend model path**
   - The backend uses `joblib.load(...)` to load the model. If you move the project, update the path accordingly.
3. **Docker networking**
   - Streamlit uses `API_URL` pointing to the Docker service name `backend`.

---

## Requirements

See `requirements.txt` inside:
- `backend/`
- `frontend/`

---

## License

Add a license file (e.g., `MIT`, `Apache-2.0`) if you plan to share this project.
