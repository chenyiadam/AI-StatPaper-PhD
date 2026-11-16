---
name: stat-reviewer
description: Mock peer review and submission strategy. use when the user wants simulated referee reports, aggregation of multiple reviews, rebuttal/response-letter drafting, or an acceptance-probability read — i.e., stage S6 and real post-submission revisions.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-theory-check]
---

# stat-reviewer · Mock review & rebuttal

## Hard disciplines

1. **Findings are research leads**: adjudicate each (must-fix / worth-fixing /
   rebuttal); AI referees also misread — check [likely-misreading] findings
   against the manuscript before acting.
2. **Down-weight outliers** (AI Scientist / Polaris aggregation): anchor at the
   median; Overall deviations > 3 are flagged; Confidence ≤ 2 is down-weighted.
3. **Scores never buy back a citation** (Polaris pass rule):
   `pass = (overall ≥ 6) AND (fabricated citations = 0)` — one fabricated
   reference fails the whole mock review.
4. **Honest limitations earn credit**: do not punish candor (NeurIPS
   convention).

## Workflow

### A. Three-reviewer simulation (P24, `prompts/en/06`)

Three **independent sessions** (invisible to each other; temperature ~0.7):

| Role | Focus |
|---|---|
| theory referee | assumption strength, proof correctness, rate optimality, theory–method consistency |
| applications & computation referee | simulation fairness, baseline tuning, real-data interpretation bounds, replication package |
| presentation referee | structure, contribution–body mapping, self-contained figures, citation practice, AI disclosure |

Rubric (identical across roles, for aggregation): Soundness / Presentation /
Contribution 1–4 (anchored) + Overall 1–10 + Confidence 1–5 + **binary
Decision** (Accept/Reject only; borderline lean goes in the rationale).
Findings must name a location; locationless findings are dropped. THOUGHT +
REVIEW JSON dual output (JSON feeds programmatic aggregation).

### B. Meta-review (P25)
1. Merge duplicates (tag sources R1+R3); anchor numerics at the median.
2. Tag each weakness: `[verifiable] / [needs fact-check] / [likely misreading]`.
3. Three-tier worklist: must-fix → worth-fixing → rebuttal-only; each with
   action, hours, sections.
4. Meta-verdict: accept probability + biggest risk.
5. **Protect the core claim**: wholesale adoption = reshaping the paper into
   the lowest scorer's taste.

### C. Two-round loop (recommended)
Round 1 findings → fixes → Round 2 verification (new session/model) → residual
adjudication. A substantive theory hole rolls back to S3 (stat-theory-check) —
normal pipeline behavior.

### D. Real rebuttals (after real reviews)
Run **P26**: conclusion first, ≤ 250 words per item, promises map to real
diffs, verifiable evidence in disputes, misreadings restated before clarifying.
Output via `templates/response-letter.tex`.

### E. Submission strategy
1. Venue fit: contribution type vs. the venue's recent output mix.
2. Suggested reviewers: 3–5 conflict-free names from the literature pool
   (nearest-neighbor lineage authors; exclude collaborators).
3. Cover letter via `templates/cover-letter.md`.

## Output format

Aggregated table:
```
| Finding | Source | Location | Class (theory/exp/presentation) | Adjudication (must-fix/worth-fix/rebuttal) | Status |
```
Ends with: the three-tier list + Overall median + an AI-estimated accept
probability (informational only).

## Related files

`prompts/en/06` (P24–P27) · `checklists/en/C7-pre-submission.md` ·
`docs/07` (Chinese) · `templates/response-letter.tex`
