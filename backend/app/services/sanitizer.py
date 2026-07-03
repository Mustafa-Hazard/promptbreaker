"""
Input sanitization — first defense layer.

Pattern-matches known prompt-injection phrasing before the message ever
reaches the LLM. This catches blunt, direct attacks cheaply (no API call
needed) but is NOT sufficient on its own — see prompts.py (hardening) and
validator.py (output-side backstop) for the other two layers. Attackers
can phrase things in ways that dodge keyword matching, which is exactly
why this is one layer of three, not the whole defense.
"""

import re

# Each pattern targets a known injection *technique*, not a specific
# wording, so paraphrases of the same technique still get caught.
SUSPICIOUS_PATTERNS = [
    # Direct injection: telling the model to disregard its instructions
    re.compile(r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions?\b", re.I),
    re.compile(r"\bdisregard\s+(all\s+)?(previous|prior|above)\b", re.I),
    re.compile(r"\bforget\s+(everything|all)\s+(above|before)\b", re.I),
    re.compile(r"\byou\s+are\s+no\s+longer\s+bound\b", re.I),
    # Asking the model to reveal its own instructions
    re.compile(r"\brepeat\s+(everything\s+in\s+)?your\s+(system\s+)?instructions?\b", re.I),
    re.compile(r"\bprint\s+your\s+(full\s+)?(configuration|instructions|system\s+prompt)\b", re.I),
    re.compile(r"\bwhat\s+(are|is)\s+your\s+(system\s+)?instructions?\b", re.I),
    # Role hijacking: assigning the model a new identity
    re.compile(r"\byou\s+are\s+(now|no\s+longer)\s+['\"]?\w+['\"]?", re.I),
    re.compile(r"\bact\s+as\s+(if\s+you\s+(are|were)\s+)?['\"]?\w+['\"]?", re.I),
    re.compile(r"\bpretend\s+(to\s+be|you\s+are)\b", re.I),
    # Embedded fake "system"/"admin" directives inside user content
    re.compile(r"\[?\s*system\s+note\s+to\s+assistant\s*[:\]]", re.I),
    re.compile(r"\[?\s*admin\s+override\s*[:\]]", re.I),
]


def sanitize_input(message: str) -> tuple[bool, str | None]:
    """
    Returns (is_suspicious, matched_pattern_description).
    Does not modify the message — callers decide what to do with a hit
    (in this project: block with a canned refusal before calling the LLM).
    """
    for pattern in SUSPICIOUS_PATTERNS:
        if pattern.search(message):
            return True, pattern.pattern
    return False, None
