import "./ModeToggle.css";

export default function ModeToggle({ mode, onChange }) {
  return (
    <div className="mode-toggle" role="group" aria-label="Chat mode">
      <button
        type="button"
        className={`mode-toggle-btn vulnerable ${mode === "vulnerable" ? "active" : ""}`}
        onClick={() => onChange("vulnerable")}
      >
        Vulnerable
      </button>
      <button
        type="button"
        className={`mode-toggle-btn hardened ${mode === "hardened" ? "active" : ""}`}
        onClick={() => onChange("hardened")}
      >
        Hardened
      </button>
    </div>
  );
}
