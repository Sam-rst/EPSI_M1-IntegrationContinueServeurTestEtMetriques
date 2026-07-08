# api — Converter API (back)

API FastAPI de conversion de devises, gérée avec [uv](https://docs.astral.sh/uv/).
La CI n'appelle jamais les outils directement : elle passe par les **tâches poe**.

```bash
uv sync --dev                # installe deps + outils de dev
uv run poe <tache>           # lance une tâche
```

## Interface de tâches (`uv run poe …`)

| Famille      | Tâche             | Outil              |
| ------------ | ----------------- | ------------------ |
| **quality**  | `lint` / `lint:fix`         | ruff       |
|              | `format` / `format:fix`     | ruff       |
|              | `typecheck` / `typecheck:fix` | ty       |
|              | `deadcode`        | vulture            |
| **tests**    | `tests:unit`      | pytest             |
|              | `tests:integ`     | pytest             |
|              | `tests:e2e`       | pytest (+ serveur) |
|              | `tests:coverage`  | pytest-cov         |
| **build**    | `start`           | uvicorn            |
|              | `build`           | compileall         |
| **security** | `audit:deps`      | pip-audit          |
|              | `audit:code`      | bandit             |

Composites : `quality`, `tests`, `security`, `ci` (= quality + tests + security).
