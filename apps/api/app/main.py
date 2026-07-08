"""Point d'entrée FastAPI : expose la logique de `converter.py` en HTTP."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.converter import RATES, UnknownCurrencyError, convert

app = FastAPI(title="Converter API", version="0.1.0")

# CORS ouvert : pratique pour le dev local front <-> back.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Endpoint de liveness, utilisé par les smoke tests / le déploiement."""
    return {"status": "ok"}


@app.get("/currencies")
def currencies() -> dict[str, list[str]]:
    return {"currencies": sorted(RATES)}


@app.get("/convert")
def convert_endpoint(amount: float, source: str, target: str) -> dict:
    try:
        result = convert(amount, source, target)
    except UnknownCurrencyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "amount": amount,
        "source": source.upper(),
        "target": target.upper(),
        "result": result,
    }
