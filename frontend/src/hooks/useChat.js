import { useState } from "react";
import { sendMessage } from "../services/api";

export function useChat(mode = "vulnerable") {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const send = async (text) => {
    if (!text.trim()) return;

    setLoading(true);
    setError(null);

    setMessages((prev) => [...prev, { role: "user", content: text }]);

    try {
      const reply = await sendMessage(text, mode);
      setMessages((prev) => [...prev, { role: "assistant", content: reply.response }]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { messages, loading, error, send };
}
