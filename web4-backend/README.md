# Web4 Backend API

FastAPI backend for Web4Node dashboard.

## Endpoints

- `GET /status` – returns mock blockchain state
- `POST /sign` – returns dummy signed transaction

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: http://localhost:8000
