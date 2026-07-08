# web — Convertisseur (front)

Front React + Vite + TypeScript. La CI passe par les **scripts npm** (mêmes noms que le back).

```bash
npm install            # installe deps + outils
npm run <tache>        # lance une tâche
```

## Interface de tâches (`npm run …`)

| Famille      | Tâche             | Outil               |
| ------------ | ----------------- | ------------------- |
| **quality**  | `lint` / `lint:fix`         | oxlint    |
|              | `format` / `format:fix`     | oxfmt     |
|              | `typecheck` / `typecheck:fix` | tsc     |
|              | `deadcode`        | knip                |
| **tests**    | `tests:unit`      | vitest              |
|              | `tests:integ`     | vitest              |
|              | `tests:e2e`       | playwright          |
|              | `tests:coverage`  | vitest --coverage   |
| **build**    | `start`           | vite (dev)          |
|              | `build`           | vite build          |
| **security** | `audit:deps`      | npm audit           |
|              | `audit:code`      | oxlint (analyse statique) |

Composites : `quality`, `tests`, `security`, `ci` (= quality + tests + security).

> Note : `oxfmt` (formateur oxc) et `ty` côté back sont des outils récents ;
> `typecheck:fix` n'a pas de correction auto pour les erreurs de types (tsc/ty),
> il relance simplement la vérification.
