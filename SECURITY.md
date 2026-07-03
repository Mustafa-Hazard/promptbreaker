# Security Policy

PromptBreaker is an **educational lab** intentionally containing a
vulnerable-by-design chatbot mode used to demonstrate prompt injection
attacks. That mode is meant to be insecure — please don't file issues about
the vulnerable mode behaving as designed.

That said, we take the security of the project's infrastructure (CI/CD,
dependencies, the hardened/defense mode, and the codebase itself) seriously.

## Reporting a Vulnerability

If you find a security issue that is **not** part of the intentional
vulnerable-mode teaching content — for example, a flaw in the hardened
defense mode, a dependency vulnerability, exposed secrets, or a CI/CD
misconfiguration — please report it responsibly:

1. **Do not** open a public GitHub issue.
2. Email the maintainer directly (see the GitHub profile for contact info)
   or use GitHub's private [Security Advisories](../../security/advisories)
   feature for this repo.
3. Include steps to reproduce, impact, and any suggested fix if known.

We'll acknowledge reports within a few days and aim to patch confirmed
issues promptly.

## Supported Versions

This is a portfolio/demo project without formal version support. Security
fixes are applied to the `main` branch only.

## Scope

| Component | In scope |
|---|---|
| Hardened/defense mode | ✅ |
| CI/CD pipelines | ✅ |
| Dependency vulnerabilities | ✅ |
| Vulnerable mode's intentional weaknesses | ❌ (that's the point) |
