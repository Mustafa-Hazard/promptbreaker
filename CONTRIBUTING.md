# Contributing to PromptBreaker

## Branching Strategy — GitHub Flow + Protected Main

```
main          ← protected, production-ready, never commit directly
└── dev       ← integration branch, all feature branches merge here
    ├── phase/0-setup
    ├── phase/1-vulnerable-chatbot
    ├── phase/2-attack-docs
    ├── phase/3-defense-layer
    ├── phase/4-ui-polish
    └── phase/5-docs-and-report
```

- `main` and `dev` are protected: PRs required, CI must pass, no force pushes.
- Work happens on `phase/*` branches, merged into `dev` via PR.
- `dev` merges into `main` once a phase (or milestone) is stable.

## Daily Workflow

```bash
git checkout dev
git pull origin dev

git checkout -b phase/1-vulnerable-chatbot
# ...work...

git add .
git commit -m "feat(backend): add /api/chat endpoint with groq integration"

git push origin phase/1-vulnerable-chatbot
# open a PR into dev
```

## Conventional Commits

Always use this format:

```
feat(scope): add new feature
fix(scope): fix a bug
docs(scope): update documentation
chore(scope): config, tooling, setup
test(scope): add or update tests
refactor(scope): restructure without behavior change
security(scope): security-related change
```

Examples:

```
feat(backend): add input sanitizer middleware
fix(frontend): resolve mode toggle state bug
security(backend): harden system prompt against role hijacking
docs(attacks): add direct injection writeup with payload examples
```

## Pull Requests

- One logical change per PR where possible.
- Fill out the PR template completely.
- CI (lint + docker build) must pass before merge.
- No secrets, no `.env` files, ever.
