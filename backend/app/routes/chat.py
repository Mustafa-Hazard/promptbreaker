from flask import Blueprint, current_app, request, jsonify

from ..prompts import VULNERABLE_SYSTEM_PROMPT
from ..services.llm_client import LLMClient

chat_bp = Blueprint("chat", __name__)

MAX_MESSAGE_LENGTH = 1000


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

    # Phase 1: only "vulnerable" mode exists. Phase 3 adds "hardened".
    mode = data.get("mode", "vulnerable")
    if mode != "vulnerable":
        return jsonify({"error": f"unsupported mode: {mode}", "code": "UNSUPPORTED_MODE"}), 400

    api_key = current_app.config.get("GROQ_API_KEY")
    if not api_key:
        return jsonify(
            {"error": "server misconfigured: missing GROQ_API_KEY", "code": "SERVER_CONFIG_ERROR"}
        ), 500

    try:
        client = LLMClient(api_key=api_key)
        reply = client.get_completion(VULNERABLE_SYSTEM_PROMPT, message)
    except Exception:
        current_app.logger.exception("LLM completion failed")
        return jsonify(
            {"error": "something went wrong talking to the model", "code": "LLM_ERROR"}
        ), 502

    return jsonify({"response": reply, "mode": mode}), 200
