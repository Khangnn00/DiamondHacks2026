# Job application co-pilot (scaffold)

**Status:** Repository scaffold only — no product features implemented yet.

## North star

**Browser-use agents** (LLM + Playwright) power job discovery, company intel, and ATS flows. **FastAPI** + **SQLite** persist state; **Electron** is the desktop shell that talks to the API only (no agents in the UI).

## Layout

| Path | Purpose |
|------|---------|
| `backend/` | FastAPI app, workers, agent tasks, SQLModel/Alembic (to be wired) |
| `desktop/` | Electron main / preload / renderer (HTML/CSS/JS) |
| `docs/SETUP.md` | How to run processes once the app is implemented |
| `PROJECT_PLAN.md` | Full architecture and env checklist |

## Next steps

1. Implement API, DB models, and workers per `PROJECT_PLAN.md`.
2. `cd backend && python -m venv .venv && pip install -r requirements.txt && playwright install chromium`
3. `cd desktop && npm install`

## License

See [LICENSE](LICENSE).
