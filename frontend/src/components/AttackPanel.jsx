import { ATTACKS } from "../data/attacks";
import "./AttackPanel.css";

export default function AttackPanel({ onSelectAttack }) {
  return (
    <div className="attack-panel">
      <p className="attack-panel-title">Try an attack</p>
      {ATTACKS.map((attack) => (
        <button
          key={attack.id}
          type="button"
          className="attack-btn"
          onClick={() => onSelectAttack(attack.payload)}
        >
          {attack.label}
        </button>
      ))}
    </div>
  );
}
