# Skill Pack (English)

> English versions of the 9 skills. The Chinese versions in `skills/` are canonical
> and identical in substance. Skills follow the [Agent Skills specification](https://agentskills.io/specification):
> YAML frontmatter with `name` (matches the directory name) + `description`
> (trigger-style) + `metadata`; progressive disclosure — name/description live in
> the system prompt, the body loads on activation, and checklists/scripts are read
> on demand.

## Installation

```bash
# Project-level install (recommended; travels with the repo)
cp -r skills-en/*  your-paper-project/.claude/skills/

# User-level install
cp -r skills-en/*  ~/.claude/skills/
```

Restart the session; skills trigger by description, or invoke explicitly:
> Use the stat-theory-check skill to review the proof of Theorem 1

No skill mechanism (plain chat UIs)? Open the `SKILL.md`, paste the body (without
frontmatter) as the first message, then continue the workflow.

## Skill list & pipeline position

| Skill | Stage | Triggers when |
|---|---|---|
| [stat-pipeline](stat-pipeline/SKILL.md) | throughout | the user describes a whole-paper task or is lost between stages |
| [stat-research](stat-research/SKILL.md) | S1–S2 | topic refinement, search, notes, related work |
| [stat-theory-check](stat-theory-check/SKILL.md) | S3 | reviewing theorems, proofs, assumptions |
| [stat-simulation-audit](stat-simulation-audit/SKILL.md) | S4 | designing/auditing simulations, real-data plans |
| [stat-writing](stat-writing/SKILL.md) | S5 | drafting and polishing sections, de-AI-flavor, translation |
| [stat-citation-verify](stat-citation-verify/SKILL.md) | throughout | any citation entering the paper (three-layer check) |
| [stat-reviewer](stat-reviewer/SKILL.md) | S6 | three-reviewer simulation, meta-review, rebuttals |
| [stat-journal-fit](stat-journal-fit/SKILL.md) | S7 (first half) | venue selection, style adaptation, format migration, cover letters |
| [stat-format-lint](stat-format-lint/SKILL.md) | S7 (second half) | LaTeX format, figures, citation consistency, AI-flavor symbol scan |
| [stat-postsub](stat-postsub/SKILL.md) | S0 & S8 | submission-system execution, preprints, status inquiries, decision routes, proofs & post-publication |

## Design conventions

- Each skill references repo assets (`checklists/`, `scripts/`, `prompts/`) by
  path — clone the whole repository so relative paths resolve. The English skills
  reference the English checklists under `checklists/en/` and English prompts
  under `prompts/en/`; deterministic scripts are language-agnostic.
- Hard disciplines sit at the top of each body (non-negotiable): verify citations,
  attack proofs line by line, trace numbers.
- Every skill's output includes "human verification points" — **AI pass ≠ pass**.
