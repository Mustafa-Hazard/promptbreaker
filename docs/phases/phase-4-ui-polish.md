# Phase 4 — UI Polish

**Branch:** `phase/4-ui-polish`

## What was built

- `ModeToggle` — switches between vulnerable and hardened mode, recolors
  the whole chat window (red/green) so the active mode is unmistakable
- `AttackPanel` — buttons for all 5 attack payloads; clicking one fills
  the input for review rather than sending immediately
- `DefenseExplainer` — explains the current mode's posture and, after a
  hardened-mode response, which `defense_layer` intervened and why
- Per-message mode/defense tags on chat bubbles, so a conversation that
  mixes modes stays legible
- Desktop side-panel layout with a responsive stacked fallback

## Key decisions

- Attack buttons prefill rather than auto-send, so a demo presenter (or
  a curious visitor) can read the payload before firing it — better for
  teaching than a surprise auto-fire.
- Chat state was lifted to `App.jsx` so the mode toggle, attack panel,
  and defense explainer could all react to the same live state without
  awkward prop drilling.

## Notable bugs hit and fixed

- `docker-compose.override.yml`'s dev volume mounted only
  `frontend/src`, never `vite.config.js` or `index.html` — so the dev
  container's Vite server fell back to its own default port (5173)
  instead of the 3000 the compose file actually exposed, and couldn't
  find an HTML entry point. Fixed by mounting both files and making the
  dev command explicit about host/port.
- ESLint's `react/recommended` preset requires PropTypes on every
  component by default; since this project intentionally doesn't use the
  `prop-types` package, that rule was turned off rather than adding an
  unnecessary dependency.
