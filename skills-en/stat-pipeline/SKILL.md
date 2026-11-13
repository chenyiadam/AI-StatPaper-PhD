---
name: stat-pipeline
description: Full-pipeline orchestration for statistics papers. use when the user asks to "write a statistics paper / go from idea to submission / advance my paper to the next stage", or when it is unclear which stat-* skill applies — this skill locates the current stage and dispatches the right skills, prompts, checklists and scripts.
metadata:
  version: "1.0"
  related_skills: [stat-research, stat-theory-check, stat-simulation-audit, stat-writing, stat-citation-verify, stat-reviewer, stat-journal-fit, stat-format-lint]
---

# stat-pipeline · Statistics paper pipeline orchestration

## Hard disciplines (non-negotiable)

1. **AI produces starting points, not papers.** Every stage's deliverable must
   pass its checklist and be adjudicated by the author before the next stage.
2. **Citations verified first**: any citation entering the text goes through
   stat-citation-verify's three layers.
3. **Number provenance**: every number in the paper traces to a cell of an
   experiment output file (±0.01 tolerance); small integers, years, and table
   IDs are exempt.
4. **Degrade loudly**: unverifiable content is marked `[AI-UNVERIFIED]` for the
   author — it is never silently mixed into the text.

## The seven-stage pipeline and its gates

```
S0 charter (stat-postsub + P33) ──▶ S1 question ──gate1──▶ S2 literature
──gate2──▶ S3 theory ──gate3──▶ S4 experiments ──gate4──▶ S5 writing
──gate5──▶ S6 mock review ──gate6──▶ S7 journal fit (stat-journal-fit +
journals/) ──gate7──▶ S8 submission execution & post-publication
(stat-postsub + P34–P38)
```

| Stage | Skills / prompts | Gate (all must pass) |
|---|---|---|
| S1 question | stat-research + `prompts/en/01` | every C1 item has a concrete answer; the question lives on a statistical property |
| S2 literature | stat-research + stat-citation-verify + `prompts/en/02` | reproducible search log; all citations L1/L2; gap map written |
| S3 theory | stat-theory-check + `prompts/en/03` | C2 adjudicated item by item; every "obviously" expanded; assumption–use table done |
| S4 experiments | stat-simulation-audit + `prompts/en/04` | smoke test passed; C3 passed; baseline-fairness protocol in place |
| S5 writing | stat-writing + `prompts/en/05` | section drafts + P21 de-AI-flavor + style_check symbol scan + notation table synced |
| S6 mock review | stat-reviewer + `prompts/en/06` | three reviews aggregated and adjudicated; must-fix items cleared |
| S7 journal fit · formatting · submission | **stat-journal-fit + `journals/` + `prompts/en/07`** → stat-format-lint + 4 scripts + `checklists/en/C7` | venue checklist complete; four scripts zero blockers; C7 done |
| S8 submission execution · post-publication | stat-postsub + `prompts/en/08` (P34–P38) + `docs/11` | P34 pre-check passed; correspondence archived; decision routes per P37 |

## Operating protocol

1. **Locate the stage**: ask the author, or infer from workspace state — no
   `refs.bib` yet (before S2), no theorem draft (before S3), no results CSV
   (before S4), no full draft (before S5).
2. **One stage at a time**: end each session with (a) gate items passed/failed
   and (b) the next stage's first concrete action (which file, which prompt).
3. **The author owns gate adjudication**: AI reports "gate passed" as triage
   only; the stage switch happens on the author's explicit confirmation.
4. **Rollback is normal**: a theory hole found in S6 sends you back to S3; only
   affected downstream stages re-run.

## Session opener (authors can paste this)

```text
I am writing a statistics paper:
- area: {{high-dimensional inference / causal inference / longitudinal data / ...}}
- current stage: {{S1–S7 or "not sure"}}
- existing materials: {{e.g., a one-page problem statement + 30 literature notes}}
- this session's goal: {{e.g., finish reviewing the proof of Theorem 1}}
Follow the stat-pipeline protocol: locate my stage, check gate gaps, and give me
this session's concrete steps (which prompt / which checklist / which script).
```

## Related files

- Pipeline overview: `docs/01-全流程总览.md` (Chinese); stage docs `docs/02`–`docs/08`
- Checklists: `checklists/en/` · scripts: `scripts/`
- Venue profiles: `journals/en/`
