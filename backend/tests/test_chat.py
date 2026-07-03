from unittest.mock import patch

from app import create_app


def make_client(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-key-not-real")
    app = create_app()
    return app.test_client()


def test_chat_missing_message(monkeypatch):
    client = make_client(monkeypatch)
    response = client.post("/api/chat", json={})
    assert response.status_code == 400
    assert response.get_json()["code"] == "MISSING_MESSAGE"


def test_chat_empty_message(monkeypatch):
    client = make_client(monkeypatch)
    response = client.post("/api/chat", json={"message": "   "})
    assert response.status_code == 400
    assert response.get_json()["code"] == "INVALID_MESSAGE"


def test_chat_message_too_long(monkeypatch):
    client = make_client(monkeypatch)
    response = client.post("/api/chat", json={"message": "a" * 1001})
    assert response.status_code == 400
    assert response.get_json()["code"] == "MESSAGE_TOO_LONG"


def test_chat_unsupported_mode(monkeypatch):
    client = make_client(monkeypatch)
    response = client.post("/api/chat", json={"message": "hello", "mode": "hardened"})
    assert response.status_code == 400
    assert response.get_json()["code"] == "UNSUPPORTED_MODE"


@patch("app.routes.chat.LLMClient")
def test_chat_success(mock_llm_client, monkeypatch):
    mock_instance = mock_llm_client.return_value
    mock_instance.get_completion.return_value = "Hello! How can I help you today?"

    client = make_client(monkeypatch)
    response = client.post("/api/chat", json={"message": "What are your account types?"})

    assert response.status_code == 200
    body = response.get_json()
    assert body["response"] == "Hello! How can I help you today?"
    assert body["mode"] == "vulnerable"
