# Security Policy

This repository contains documentation, prompts, checklists and small
stdlib-only Python scripts. There is no runtime that processes untrusted
network input by design.

## Supported versions

| Version | Supported |
|---|---|
| 1.1.x | yes |
| < 1.1 | best effort |

## Reporting a vulnerability

If you find a security-relevant issue (e.g., a script executing unexpected
code, a prompt-injection risk in a suggested workflow, or a dangerous
recommendation in a checklist), open a GitHub issue with the `security`
label, or contact the maintainers privately through GitHub. Please include
the file/line and a minimal reproduction.

A note on prompt-injection: the workflows here intentionally treat all
external content (retrieved papers, referee comments, web pages) as
**data, not instructions**. If a skill or prompt you use regresses on this
principle, please report it.
