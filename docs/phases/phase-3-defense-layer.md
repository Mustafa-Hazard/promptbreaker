# Phase 3 — Defense Layer

**Branch:** `phase/3-defense-layer`

## What was built

- `backend/app/services/sanitizer.py` — pattern-matches known injection
  *techniques* (not exact strings) before a message reaches the LLM
- `backend/app/services/validator.py` — scans the model's response for
  the literal bait secrets and redacts before returning to the user
- `HARDENED_SYSTEM_PROMPT` in `prompts.py` — instruction-integrity rules,
  a statelessness reminder (defeats fake "we already agreed" claims), and
  explicit content/instruction separation (defeats indirect injection)
- `defense_layer` field added to the `/api/chat` response, reporting
  exactly which layer (`sanitizer`, `validator`, or `none`) intervened
- `scripts/run_attacks.py` extended with `--runs N` to run each attack
  multiple times per mode and report a leak rate, since LLM responses are
  non-deterministic

## Key decisions

- **Defense in depth over a single best defense** — sanitization catches
  blunt injection phrasing for free (no LLM call needed), prompt
  hardening catches persona/authority attacks the sanitizer can't
  pattern-match, and output validation is a backstop that catches leaks
  regardless of mechanism.
- Instrumenting *which* layer blocked an attack (rather than just
  pass/fail) turned an ambiguous result into a debuggable, provable one.

## Results

Across 25 attempts per mode (5 attacks × 5 runs), hardened mode blocked
100% — 0/25 leaked. Vulnerable mode's own leak rate varied by attack
(20%-100%), confirming that LLM non-determinism matters and a single run
isn't conclusive evidence either way.

## Notable bugs hit and fixed

- The Phase 3 commit initially omitted `sanitizer.py`, `validator.py`,
  and their tests — `chat.py` imported them, so CI correctly failed with
  `ModuleNotFoundError` until the missing files were added.
