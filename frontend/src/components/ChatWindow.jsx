import { useState } from "react";
import { useChat } from "../hooks/useChat";
import "./ChatWindow.css";

export default function ChatWindow() {
  const { messages, loading, error, send } = useChat("vulnerable");
  const [draft, setDraft] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!draft.trim() || loading) return;
    send(draft);
    setDraft("");
  };

  return (
    <div className="chat-window">
      <div className="chat-header">
        <div className="chat-header-identity">
          <span className="chat-bank-name">SecureBank Digital</span>
          <span className="chat-agent-name">Ava · Support Assistant</span>
        </div>
        <span className="mode-badge">Vulnerable Mode</span>
      </div>

      <div className="chat-log">
        {messages.length === 0 && (
          <p className="chat-empty-state">
            Ask Ava about accounts, fees, or disputes — or see what happens when you don&apos;t.
          </p>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`chat-bubble ${msg.role}`}>
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
