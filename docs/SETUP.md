# Setup (after implementation)

This repository is currently a **scaffold** — the API, database, and workers are placeholders.

## Intended local processes (future)

1. **FastAPI** — `uvicorn` from `backend/` (see README when wired).
2. **Watcher worker** — `python -m app.workers.watcher_main` (from `backend/` with `PYTHONPATH` or installed package).
3. **Builder worker** — `python -m app.workers.builder_main`.
4. **Electron** — `npm run dev` in `desktop/`.

## Environment

- Copy [`.env.example`](../.env.example) to `backend/.env` (or repo root — team picks one convention).
- Install Playwright browsers after Python deps: `playwright install chromium`.

## SQLite

- Database file: `backend/data/app.db` (gitignored).
- Use **WAL** and **busy_timeout** when multiple processes access the same file.

## Troubleshooting

- **database is locked** — ensure WAL mode, single-writer discipline, and adequate SQLite timeout.
