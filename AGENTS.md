# Agent / contributor notes

## Scope of this repo (current)

This tree is a **scaffold**: folders, placeholders, and documentation. **No watcher, builder, or real API behavior** is implemented until you add it.

## Product rules (when implementing)

- **Human approval** before any application submit.
- **Browser-use** is the primary automation path; raw Playwright is fallback only.
- **Electron** calls **FastAPI only** — workers run browser agents.
- **Secrets** live in `.env` (never committed). Use `.env.example` as the checklist.
- **Persistence:** **SQLite only** for all structured data (hackathon scope). Do not introduce Supabase/Postgres unless the team explicitly replans after the event.

## Where to work

| Area | Path |
|------|------|
| Agent task prompts | `backend/app/agent_tasks/` |
| Browser-use wrapper | `backend/app/services/browser_agent.py` |
| Watcher entry | `backend/app/workers/watcher_main.py` |
| Builder entry | `backend/app/workers/builder_main.py` |
| API routes | `backend/app/api/` |
| Desktop UI | `desktop/renderer/` |

## Cursor

Use Cursor agents to iterate **task prompts** and guardrails under `agent_tasks/`, not to replace the FastAPI + SQLite architecture without team agreement.
