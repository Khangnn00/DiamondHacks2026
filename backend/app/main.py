"""
FastAPI entrypoint — scaffold only.

Wire routers, DB lifespan, and OpenAPI in a later milestone.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Job Agent API",
    version="0.0.0",
    description="Scaffold — no product routes yet.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
