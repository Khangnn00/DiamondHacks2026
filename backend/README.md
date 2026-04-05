# Backend

Scaffold only. See [../PROJECT_PLAN.md](../PROJECT_PLAN.md).

**Database:** SQLite file at `data/app.db` (via `DATABASE_URL`). Hackathon scope — **no Supabase/Postgres**.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
playwright install chromium
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Run from the `backend/` directory so `app` resolves.
