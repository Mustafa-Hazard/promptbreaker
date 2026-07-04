# Phase 0 — Setup

**Branch:** `phase/0-setup`

## What was built

- Repo scaffolding: `backend/`, `frontend/`, `docs/`, `.github/` folder tree
- Docker Compose setup — `docker-compose.yml` (production targets) and
  `docker-compose.override.yml` (dev targets with hot reload, auto-applied
  locally)
- Multi-stage Dockerfiles for both services, running as non-root users
- GitHub Actions CI: `lint.yml` (Flake8 + Bandit + Pytest, ESLint +
  Prettier) and `docker-build.yml` (validates the production build)
- `.env.example`, `.gitignore`, `.editorconfig`, `.gitattributes`
- `SECURITY.md`, `CONTRIBUTING.md`, PR/issue templates
- Minimal Flask app factory with a `/api/health` endpoint
- Minimal React app (placeholder page) via Vite

## Key decisions

- **GitHub Flow with a protected `main`**, all work merging through `dev`
  via `phase/*` branches — chosen for a solo project specifically to make
  branch protection meaningful (see the recovery notes below) rather than
  just following convention for its own sake.
- Flask **app factory pattern** from the start, to keep routes,
  services, and config cleanly separated as the app grows.

## Notable bugs hit and fixed

- Missing `package-lock.json` broke both CI's `npm ci` and the Docker
  build.
- Frontend Dockerfile installed only production deps (`npm ci
  --only=production`), but the build/preview stages needed `vite`, a
  devDependency.
- `docker-compose.override.yml` auto-loads on bare `docker compose`
  commands, which would have silently made CI validate the dev target
  instead of production — fixed by pinning CI to `-f docker-compose.yml`.
- A direct push to `main` slipped through once because branch protection
  didn't have "include administrators" enabled — fixed, and the empty
  commit it created was reverted rather than force-erased from history.
