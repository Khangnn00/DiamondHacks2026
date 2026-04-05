#!/usr/bin/env python3
"""
Export OpenAPI JSON once FastAPI `app` is implemented.

Usage (from repo root, after backend is wired):
  cd backend && python ../scripts/export_openapi.py
"""
from __future__ import annotations

import sys


def main() -> int:
    print(
        "export_openapi: not implemented yet. "
        "Point this script at your FastAPI app and write openapi/openapi.json.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
