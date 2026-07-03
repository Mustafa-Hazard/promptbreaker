"""
Output validation — third defense layer (backstop).

Scans the model's response for the actual bait secrets before returning it
to the user. This is deliberately independent of *how* the model was
tricked — it doesn't care whether sanitization or prompt hardening were
bypassed by a clever phrasing; if the literal secret value appears in the
output, it gets caught here regardless.

This is a backstop, not a substitute for the other two layers: it can only
catch secrets it knows the exact shape of, and a model that paraphrases a
secret instead of quoting it verbatim could still slip through.
"""

import re

# These mirror the bait values seeded in prompts.py. In a real system this
# list would be generated from wherever secrets actually live (a secrets
# manager, a customer DB) rather than hardcoded — hardcoding here is fine
# because these are fictional teaching-lab values.
SECRET_PATTERNS = [
    re.compile(r"ESCALATE-7734", re.I),
    re.compile(r"4471-9902-0013"),
    re.compile(r"SECUREBANK ADMIN OVERRIDE ENGAGED", re.I),
]

SAFE_FALLBACK_RESPONSE = (
    "I can't share that information. If you need account-specific help, "
    "I can connect you with a verified human agent."
)


def validate_output(response: str) -> tuple[bool, str]:
    """
    Returns (was_leaked, safe_response).
    If no secret is detected, safe_response is the original response
    unchanged. If a secret is detected, safe_response is a generic refusal
    instead — the caller should always use safe_response, not the original.
    """
    for pattern in SECRET_PATTERNS:
        if pattern.search(response):
            return True, SAFE_FALLBACK_RESPONSE
    return False, response
