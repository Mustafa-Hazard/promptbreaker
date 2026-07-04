import { useEffect, useState } from "react";
import "./ChatWindow.css";

export default function ChatWindow({
  mode,
  messages,
  loading,
  error,
  onSend,
  prefillText,
  onPrefillConsumed,
}) {
  const [draft, setDraft] = useState("");

  // When an attack button in the side panel sets a prefill payload,
  // drop it into the input for the user to review before sending.
  useEffect(() => {
    if (prefillText) {
      setDraft(prefillText);
      onPrefillConsumed();
    }
  }, [prefillText, onPrefillConsumed]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!draft.trim() || loading) return;
    onSend(draft);
    setDraft("");
  };

  return (
    <div className={`chat-window ${mode}`}>
      <div className="chat-header">
        <div className="chat-header-identity">
          <span className="chat-bank-name">SecureBank Digital</span>
          <span className="chat-agent-name">Ava · Support Assistant</span>
        </div>
        <span className={`mode-badge ${mode}`}>{mode} Mode</span>
      </div>

      <div className="chat-log">
        {messages.length === 0 && (
          <p className="chat-empty-state">
            Ask Ava about accounts, fees, or disputes — or try an attack from the panel.
          </p>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`chat-bubble ${msg.role}`}>
            {msg.role === "assistant" && (
              <div className="chat-bubble-meta">
                <span className={`mode-tag ${msg.mode}`}>{msg.mode}</span>
                {msg.defenseLayer && msg.defenseLayer !== "none" && (
                  <span className={`defense-tag ${msg.defenseLayer}`}>{msg.defenseLayer}</span>
                )}
              </div>
            )}
            {msg.content}
          </div>
        ))}

        {loading && <div className="chat-bubble assistant pending">Ava is typing…</div>}
        {error && <div className="chat-error">{error}</div>}
      </div>

      <form className="chat-input-row" onSubmit={handleSubmit}>
        <span className="chat-prompt-glyph">&gt;</span>
        <input
          className="chat-input"
          type="text"
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          placeholder="Type a message…"
          disabled={loading}
        />
        <button className="chat-send-btn" type="submit" disabled={loading || !draft.trim()}>
          Send
        </button>
      </form>
    </div>
  );
}
