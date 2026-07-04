# Phase 2 — Attack Documentation

**Branch:** `phase/2-attack-docs`

## What was built

- `scripts/run_attacks.py` — sends 5 prompt-injection attack payloads to
  the live `/api/chat` endpoint and writes the real responses into
  `/docs/attacks/*.md`, so the documentation reflects actual model
  behavior rather than hypothetical examples
- Five attack classes covered: Direct Injection, Role Hijacking, Data
  Exfiltration, Indirect Injection, Context Manipulation

## Key decisions

- Results are captured live from the running model, never fabricated —
  the point of the lab is to demonstrate real behavior, and a scripted
  capture keeps that honest and reproducible.
- Each attack targets the same three bait secrets seeded in Phase 1, so
  "did it leak" is unambiguous and checkable by pattern match.

## Results

All 5 attacks succeeded against vulnerable mode on first capture — every
secret leaked, including one attack (Role Hijacking) that also
hallucinated additional fake infrastructure details around the real
leaked secrets.

## Notable bugs hit and fixed

- Same `httpx`/`groq` incompatibility from Phase 1 resurfaced here since
  the fix hadn't been merged yet when this phase's script was first run —
  all 5 attacks initially came back as `502` errors instead of real
  responses.
