from flask import Blueprint, current_app, request, jsonify

from ..prompts import VULNERABLE_SYSTEM_PROMPT, HARDENED_SYSTEM_PROMPT
from ..services.llm_client import LLMClient
from ..services.sanitizer import sanitize_input
from ..services.validator import validate_output, SAFE_FALLBACK_RESPONSE

chat_bp = Blueprint("chat", __name__)

MAX_MESSAGE_LENGTH = 1000

SYSTEM_PROMPTS = {
    "vulnerable": VULNERABLE_SYSTEM_PROMPT,
    "hardened": HARDENED_SYSTEM_PROMPT,
}


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "message field required", "code": "MISSING_MESSAGE"}), 400

    message = data["message"]

    if not isinstance(message, str) or not message.strip():
        return jsonify(
            {"error": "message must be a non-empty string", "code": "INVALID_MESSAGE"}
        ), 400

    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": "message too long", "code": "MESSAGE_TOO_LONG"}), 400

    mode = data.get("mode", "vulnerable")
    if mode not in SYSTEM_PROMPTS:
        return jsonify({"error": f"unsupported mode: {mode}", "code": "UNSUPPORTED_MODE"}), 400

    # defense_layer reports which layer (if any) intervened, so callers
    # can tell "the model refused on its own" apart from "sanitizer/
    # validator caught it" instead of guessing from response text alone.
    defense_layer = "none"

    # Defense layer 1 — input sanitization. Only active in hardened mode:
    # vulnerable mode is intentionally undefended for the attack demos.
    if mode == "hardened":
        is_suspicious, _pattern = sanitize_input(message)
        if is_suspicious:
            return jsonify(
                {"response": SAFE_FALLBACK_RESPONSE, "mode": mode, "defense_layer": "sanitizer"}
            ), 200

    api_key = current_app.config.get("GROQ_API_KEY")
    if not api_key:
        return jsonify(
            {"error": "server misconfigured: missing GROQ_API_KEY", "code": "SERVER_CONFIG_ERROR"}
        ), 500

    try:
        client = LLMClient(api_key=api_key)
        # Defense layer 2 — prompt hardening (the hardened system prompt
        # itself contains the instruction-integrity rules). There's no
        # separate signal to report here: if this layer worked, the model
        # simply refused on its own, indistinguishable in code from any
        # other "none" response — the response text is the evidence.
        reply = client.get_completion(SYSTEM_PROMPTS[mode], message)
    except Exception:
        current_app.logger.exception("LLM completion failed")
        return jsonify(
            {"error": "something went wrong talking to the model", "code": "LLM_ERROR"}
        ), 502

    # Defense layer 3 — output validation. Backstop that catches leaked
    # secrets regardless of how layers 1 and 2 were bypassed.
    if mode == "hardened":
        was_leaked, reply = validate_output(reply)
        if was_leaked:
            defense_layer = "validator"

    return jsonify({"response": reply, "mode": mode, "defense_layer": defense_layer}), 200
