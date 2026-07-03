# PromptBreaker 🔴🟢

> A live demo web app showing how prompt injection attacks compromise
> AI-powered customer support chatbots — and how to stop them.
> Mapped to the [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

![CI](https://github.com/Mustafa-Hazard/promptbreaker/actions/workflows/lint.yml/badge.svg)
![Docker Build](https://github.com/Mustafa-Hazard/promptbreaker/actions/workflows/docker-build.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## What Is Prompt Injection?

*(coming in Phase 2 — attack docs)*

## Architecture

*(coming in Phase 0/5 — architecture diagram)*

## Attack Classes (5)

*(coming in Phase 2)*

- Direct Injection
- Role Hijacking
- Data Exfiltration
- Indirect Injection
- Context Manipulation

## Defense Layer

*(coming in Phase 3)*

## OWASP LLM Top 10 Mapping

*(coming in Phase 5 — `/docs/owasp-llm-mapping.md`)*

## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Flask
- **LLM:** Groq API
- **Infra:** Docker Compose, GitHub Actions CI/CD

## Getting Started

```bash
git clone https://github.com/Mustafa-Hazard/promptbreaker.git
cd promptbreaker
cp .env.example .env
# fill in your GROQ_API_KEY in .env
```

## Running with Docker Compose

```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend health check: http://localhost:5000/api/health

## Running Tests

```bash
cd backend
pytest tests/ -v
```

## Project Structure

*(see `/docs` for full build log and phase-by-phase breakdown)*

## Build Log

See [`/docs/phases`](./docs/phases) for a phase-by-phase development log.

## Known Limitations

*(to be filled in as the project develops)*

## Author

**Mustafa Hazard**
[GitHub](https://github.com/Mustafa-Hazard)

## License

[MIT](./LICENSE)
