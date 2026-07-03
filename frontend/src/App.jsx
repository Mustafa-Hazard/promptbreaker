import ChatWindow from "./components/ChatWindow";
import "./App.css";

function App() {
  return (
    <div className="app-shell">
      <div>
        <div className="app-header">
          <p className="app-title">
            <strong>PromptBreaker</strong> — Prompt Injection Attack &amp; Defense Lab
          </p>
        </div>
        <ChatWindow />
      </div>
    </div>
  );
}

export default App;
