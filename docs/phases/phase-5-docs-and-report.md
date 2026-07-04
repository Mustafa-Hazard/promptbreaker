# Phase 5 — Docs and Report

**Branch:** `phase/5-docs-and-report`

## What was built

- Full `README.md`, replacing the Phase 0 placeholders with real content
  covering what prompt injection is, the architecture, attack classes,
  defense layers, and results
- `docs/owasp-llm-mapping.md` — maps each of the 5 attack classes and 3
  defense layers to the OWASP Top 10 for LLM Applications
- `docs/architecture-diagram.svg` — client/backend/external service
  diagram showing the vulnerable vs. hardened request paths
- This set of `/docs/phases/*.md` build logs

## Key decisions

- Kept the build log honest about the bugs hit along the way (dependency
  pinning issues, a missing branch-protection setting, a stray direct
  commit to `main`) rather than presenting a sanitized version — the
  debugging process is itself a demonstration of the workflow discipline
  the project's `CONTRIBUTING.md` describes.
- Docs were written after each phase's real, live-captured results were
  available, not drafted speculatively in advance.
