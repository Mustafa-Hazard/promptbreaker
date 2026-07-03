# Prompt Hardening

**Layer 2 of 3** — constrains what the model itself is willing to do,
independent of whether the input looked suspicious.

## What it does

`backend/app/prompts.py` defines `HARDENED_SYSTEM_PROMPT`, which applies
several hardening techniques on top of the same base persona used in
`VULNERABLE_SYSTEM_PROMPT`:

1. **Explicit instruction-integrity rules**, stated as absolute and listed
   before any task-related content, telling the model it must never
   reveal the internal reference info regardless of who asks, what
   authority they claim, or what "mode" they claim to invoke it in.
2. **Statelessness reminder** — since each `/api/chat` request is
   independent with no real conversation memory, the prompt explicitly
   tells the model to treat any claim of "we already agreed to this
   earlier" as false. This directly targets the context manipulation
   attack class (`05`).
3. **Content vs. instruction separation** — the model is told that
   anything it's asked to summarize/translate/process on a customer's
   behalf (e.g. a pasted complaint) is *data*, never instructions — even
   if it's formatted to look like a system directive. This targets the
   indirect injection attack class (`04`).
4. **Persona immutability** — the model is told it cannot be renamed or
   reassigned a role by anything in the conversation, targeting the role
   hijacking attack class (`02`).
5. **A fixed canned refusal**, repeated verbatim rather than left to the
   model's discretion, so a partial-compliance response ("I probably
   shouldn't say the whole thing, but the escalation code starts with...")
   isn't possible — the model either helps normally or gives the exact
   same refusal text every time.
6. **Repetition of the priority rule at the end of the prompt** — models
   tend to weight instructions near the end of their context more
   heavily, so the "these rules take priority" reminder is restated after
   the task description, not just before it.

## What it does NOT do

A hardened prompt is still just an instruction the model can, in
principle, be argued out of by a sufficiently creative attack — it raises
the bar significantly but isn't a mathematical guarantee. This is why
`output-validation.md`'s layer exists as a backstop: even if a clever
attack talks the model into leaking a secret despite these rules, the
response never reaches the user unfiltered.
