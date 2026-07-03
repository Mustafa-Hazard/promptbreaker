# Output Validation

**Layer 3 of 3** — the backstop, applied after the LLM responds and before
the response reaches the user.

## What it does

`backend/app/services/validator.py` scans the model's raw response for
the literal bait secrets seeded in the system prompt (the escalation
code, the test account number, the admin override phrase). If any of them
appear in the output — regardless of how the model was talked into
producing them — the response is replaced with a generic, safe fallback
before it's returned to the user.

This layer is deliberately independent of *mechanism*. It doesn't matter
whether sanitization missed the attack because it used no injection
phrasing, or whether prompt hardening's rules were somehow argued around —
if the exact secret value shows up in the text the model generated, it
gets caught here. This makes it the most reliable of the three layers
against novel attack phrasings, at the cost of only catching leaks whose
exact shape is already known.

## What it does NOT do

Output validation only catches *verbatim or near-verbatim* matches against
known patterns. A model that paraphrases a secret instead of quoting it
directly — for example, describing the escalation code's structure or
spelling it with spaces/hyphens removed — could still slip through. In a
production system, this would need to be paired with more sophisticated
detection (e.g. entropy-based secret scanning, or classifying whether a
response discusses "internal reference info" as a category rather than
matching specific strings) rather than a fixed list of known values.

## Why all three layers together

No single layer here is sufficient on its own:

| Layer | Catches | Misses |
|---|---|---|
| Input sanitization | Blunt injection phrasing | Social-engineering framed as legitimate requests |
| Prompt hardening | Persona/authority/context attacks the model reasons about | Attacks a sufficiently persuasive prompt still argues past |
| Output validation | Any leak of a known secret value, regardless of technique | Paraphrased or reformatted leaks of the same secret |

Layering them means an attack has to defeat all three simultaneously to
succeed — see `/docs/attacks/*.md` for the live before/after comparison
showing how the same 5 attacks fare against vulnerable mode vs. hardened
mode (all three layers combined).
