# Phase 1 — Vulnerable Chatbot

**Branch:** `phase/1-vulnerable-chatbot`

## What was built

- `backend/app/prompts.py` — the vulnerable system prompt for "Ava," a
  support assistant for the fictional SecureBank Digital, seeded with
  bait secrets (an escalation code, a test account number, an admin
  override phrase) for later attacks to target
- `backend/app/services/llm_client.py` — thin wrapper around the Groq
  chat completions API (`llama-3.1-8b-instant`)
- `backend/app/routes/chat.py` — `/api/chat` endpoint: input validation,
  length limits, calls the LLM, structured error responses
- Frontend: `services/api.js`, `hooks/useChat.js`, and
  `components/ChatWindow.jsx` — the chat UI, styled as a terminal-flavored
  banking console

## Key decisions

- All account numbers, codes, and "internal" details in the vulnerable
  prompt are fictional, invented specifically for this lab — they don't
  correspond to any real institution or system.
- Chose `llama-3.1-8b-instant` for Groq's free tier's most generous rate
  limits, sufficient for a demo project.

## Notable bugs hit and fixed

- `Config` read environment variables once at import time (frozen as
  class attributes), so `.env` changes or test-time env overrides never
  actually took effect — fixed by making them properties read fresh on
  each `create_app()` call.
- Flask's `app.config.from_object()` only resolves properties correctly
  on an *instance*, not a class — `create_app(config=Config)` needed to
  become `create_app(config=Config())`.
- A `groq`/`httpx` version mismatch (`groq==0.9.0` calling `httpx` with a
  `proxies=` kwarg that newer `httpx` removed) broke every LLM call with
  a `TypeError` — fixed by pinning `httpx==0.27.2`.
- flake8's config file wasn't being found in CI because CI runs
  `flake8 backend/` from the repo root, and flake8 only searches for
  config starting at the current working directory — moved `.flake8` to
  the repo root.
