"""Tests d'INTÉGRATION : on teste l'API HTTP via le TestClient FastAPI
(routing + validation + sérialisation), sans serveur réel."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_convert_endpoint_ok():
    response = client.get("/convert", params={"amount": 10, "source": "EUR", "target": "USD"})
    assert response.status_code == 200
    assert response.json()["result"] == 10.8


def test_convert_unknown_currency_returns_404():
    response = client.get("/convert", params={"amount": 10, "source": "EUR", "target": "XXX"})
    assert response.status_code == 404


def test_convert_negative_amount_returns_400():
    response = client.get("/convert", params={"amount": -1, "source": "EUR", "target": "USD"})
    assert response.status_code == 400
