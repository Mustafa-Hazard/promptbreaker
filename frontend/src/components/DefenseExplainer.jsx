import "./DefenseExplainer.css";

const MODE_COPY = {
  vulnerable:
    "No defenses active. Ava will follow whatever instructions she's given, including ones hidden inside pasted content or claimed prior context.",
  hardened:
    "All three defense layers active: input sanitization, a hardened system prompt, and output validation.",
};

const LAYER_COPY = {
  sanitizer: "Blocked before reaching the model — the message matched a known injection pattern.",
  validator: "The model's response contained a secret, so it was redacted before being shown.",
  none: "The model answered on its own — either normally, or refusing based on its hardened instructions.",
};

export default function DefenseExplainer({ mode, lastDefenseLayer }) {
  return (
    <div className="defense-explainer">
      <p className="defense-explainer-title">Defense status</p>
      <p className="defense-explainer-body">{MODE_COPY[mode]}</p>

      {mode === "hardened" && lastDefenseLayer && (
        <div>
          <span className={`defense-layer-tag ${lastDefenseLayer}`}>layer: {lastDefenseLayer}</span>
          <p className="defense-explainer-body" style={{ marginTop: "0.4rem" }}>
            {LAYER_COPY[lastDefenseLayer]}
          </p>
        </div>
      )}
    </div>
  );
}
