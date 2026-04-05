# Team GitHub setup

**Current working repo:** [github.com/Khangnn00/DiamondHacks2026](https://github.com/Khangnn00/DiamondHacks2026) (this is what `git remote` should match until you transfer).

You can later move the project to a **GitHub Organization** so the URL becomes `https://github.com/<ORG_NAME>/DiamondHacks2026` instead of living under one person’s username.

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
