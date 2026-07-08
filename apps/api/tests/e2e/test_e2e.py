"""Tests E2E : on tape sur une VRAIE instance qui tourne (conteneur Docker).

Contrairement aux tests d'intégration (TestClient en mémoire), ici on fait
de vraies requêtes réseau vers `BASE_URL`. Utilisé dans la CD, après le
déploiement des images.
"""

import os

import httpx

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")


def test_health_live():
    response = httpx.get(f"{BASE_URL}/health", timeout=10)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_convert_live():
    response = httpx.get(
        f"{BASE_URL}/convert",
        params={"amount": 10, "source": "EUR", "target": "USD"},
        timeout=10,
    )
    assert response.status_code == 200
    assert response.json()["result"] == 10.8
