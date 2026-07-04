import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import ModeToggle from "./components/ModeToggle";
import AttackPanel from "./components/AttackPanel";
import DefenseExplainer from "./components/DefenseExplainer";
import { useChat } from "./hooks/useChat";
import "./App.css";

function App() {
  const [mode, setMode] = useState("vulnerable");
  const [prefillText, setPrefillText] = useState(null);
  const { messages, loading, error, send } = useChat();

  const lastAssistantMessage = [...messages].reverse().find((m) => m.role === "assistant");
  const lastDefenseLayer = lastAssistantMessage?.defenseLayer ?? null;

  const handleSend = (text) => send(text, mode);

  return (
    <div className="app-shell">
      <div className="app-layout">
        <div className="app-header">
          <p className="app-title">
            <strong>PromptBreaker</strong> — Prompt Injection Attack &amp; Defense Lab
          </p>
        </div>

        <div className="app-columns">
          <ChatWindow
            mode={mode}
            messages={messages}
            loading={loading}
            error={error}
            onSend={handleSend}
            prefillText={prefillText}
            onPrefillConsumed={() => setPrefillText(null)}
          />

          <aside className="side-panel">
            <ModeToggle mode={mode} onChange={setMode} />
            <AttackPanel onSelectAttack={setPrefillText} />
            <DefenseExplainer mode={mode} lastDefenseLayer={lastDefenseLayer} />
          </aside>
        </div>
      </div>
    </div>
  );
}

export default App;
