import { useState } from "react";
import { sendMessage } from "../services/api";

export function useChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const send = async (text, mode) => {
    if (!text.trim()) return;

    setLoading(true);
    setError(null);

    setMessages((prev) => [...prev, { role: "user", content: text, mode }]);

    try {
      const reply = await sendMessage(text, mode);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: reply.response,
          mode: reply.mode,
          defenseLayer: reply.defense_layer ?? null,
        },
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { messages, loading, error, send };
}
