# Image du back : on réutilise uv pour installer les deps de façon reproductible.
FROM python:3.13-slim

# On copie le binaire uv depuis l'image officielle (pas besoin de l'installer via pip).
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1) On installe d'abord SEULEMENT les dépendances (cache Docker efficace).
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# 2) Puis le code applicatif.
COPY app ./app

EXPOSE 8000
# uv run utilise le venv créé par uv sync.
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
