# Convertisseur de devises — démo CI / CD

Monorepo fullstack servant de support à un TP **CI/CD** (GitHub Actions).

- **`apps/api`** — back Python (FastAPI), géré par **uv**, tâches via **poe**.
- **`apps/web`** — front React + Vite + TypeScript, tâches via **scripts npm**.

## Idée clé : l'app expose une interface de tâches, la CI ne fait que l'appeler

Chaque service définit **les mêmes noms de tâches** (peu importe l'outil derrière).
La CI n'appelle jamais `ruff`/`oxlint`/`pytest`… directement, seulement la tâche.

| Famille      | Tâches                                             | Back (poe)    | Front (npm)   |
| ------------ | -------------------------------------------------- | ------------- | ------------- |
| **quality**  | `lint` · `format` · `typecheck` (+`:fix`) · `deadcode` | ruff/ty/vulture | oxlint/oxfmt/tsc/knip |
| **tests**    | `tests:unit` · `tests:integ` · `tests:e2e` · `tests:coverage` | pytest | vitest/playwright |
| **build**    | `start` · `build`                                  | uvicorn/compileall | vite     |
| **security** | `audit:deps` · `audit:code`                        | pip-audit/bandit | npm audit/oxlint |

```bash
# back                         # front
cd apps/api                    cd apps/web
uv sync --dev                  npm install
uv run poe <tache>             npm run <tache>
```

Les **composites** (`quality`, `tests`, `security`, `ci`) servent surtout **en local**
(et dans les hooks git). La **CI appelle les tâches granulaires** une par step.

## CI — garder `main` déployable (`.github/workflows/ci-*.yml`)

Un fichier **par service** (`ci-api.yml`, `ci-web.yml`), déclenché au push/PR sur `main`
(filtré par chemin). Un **job par famille de risque**, chaque **step = une tâche** :

```
quality  → lint → format → typecheck → deadcode
security → audit:deps → audit:code
tests    → tests:unit → tests:integ
build    → build → docker build         (dépend de quality+security+tests)
```

CI verte ⇒ `main` propre ⇒ déployable.

## CD — déployer au tag SemVer (`.github/workflows/cd-*.yml`)

Un fichier **par service** (`cd-api.yml`, `cd-web.yml`), déclenché au **push d'un tag `vX.Y.Z`** :

```
ci (réutilise la CI) → publish (image Docker taguée SemVer sur GHCR)
                     → e2e (sur l'image publiée / la stack)
                     → deploy (simulé : run image + smoke test)
```

Versionnage **SemVer** : `vMAJEUR.MINEUR.CORRECTIF`.

```bash
git tag v1.0.0
git push origin v1.0.0     # déclenche la CD
```

Sur un vrai serveur, la version déployée est pilotée par un `.env` (voir `.env.example`
et `docker-compose.deploy.yml`) : `OWNER` + `VERSION=v1.0.0`.

## Hooks git (Husky) — sécurité en local

| Hook         | Rôle                                                        |
| ------------ | ----------------------------------------------------------- |
| `pre-commit` | checks **rapides** : `lint` + `format` (back & front)       |
| `pre-push`   | **CI complète** en local : `ci` (quality + tests + security)|
| `commit-msg` | impose les **Conventional Commits** (`feat:`, `fix:`…)      |

## Lancer l'appli en local

```bash
docker compose up --build     # front sur http://localhost:8080, back sur :8000
```
