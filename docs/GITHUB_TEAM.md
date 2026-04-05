# Team GitHub setup

This project is intended to live under a **GitHub Organization** (hackathon / team account) so the URL is `https://github.com/<ORG_NAME>/DiamondHacks2026`, not tied to one person’s username.

## Option A — Transfer an existing repo

1. Create or use a [GitHub Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).
2. In the repo: **Settings → General → Danger Zone → Transfer ownership** → choose the org.
3. Everyone updates the remote:
   ```bash
   git remote set-url origin https://github.com/<ORG_NAME>/DiamondHacks2026.git
   git remote -v
   ```

## Option B — New org repo, push this code

1. Create an empty repo under the org: `DiamondHacks2026`.
2. Point `origin` at it and push:
   ```bash
   git remote set-url origin https://github.com/<ORG_NAME>/DiamondHacks2026.git
   git push -u origin main
   ```

## Docs and links

After the org slug is final, replace `<ORG_NAME>` in README / PROJECT_PLAN with the real org (or keep this doc as the single source of truth).
