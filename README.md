# Flask Docker App

A minimal Flask API (app factory + blueprint) served by gunicorn and ready for Docker.

## Structure

```
app/            application package (factory, config, routes)
tests/          pytest tests
wsgi.py         entry point (gunicorn: wsgi:app)
Dockerfile      production image (non-root, healthcheck)
docker-compose.yml
```

## Run with Docker

```bash
docker build -t flask-docker-app .
docker run -p 5000:5000 --env-file .env flask-docker-app
# or
docker compose up --build
```

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python wsgi.py
```

## Test

```bash
pytest
```

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET/POST | `/api/items` | List / create items |
| GET/DELETE | `/api/items/<id>` | Fetch / delete an item |

```bash
curl -X POST localhost:5000/api/items -H 'Content-Type: application/json' -d '{"name":"widget"}'
curl localhost:5000/api/items
```
