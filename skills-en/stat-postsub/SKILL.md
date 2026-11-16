---
name: stat-postsub
description: Submission execution and post-submission management. use when the user wants to execute a journal submission, decide preprint strategy (arXiv endorsement), inquire about manuscript status or nudge the editor, handle revise/reject/accept decisions, manage proofs and copyright/OA, or handle post-publication tasks (promotion/errata) — i.e., stage S0 initiation (P33) and all of S8 (P34–P38).
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-journal-fit, stat-reviewer]
---

# stat-postsub · Submission execution & post-submission

## Hard disciplines

1. **Facts only, low frequency, polite**: every editorial communication ≤ 120
   words, contains only IDs/dates/statuses; ≥ 6 weeks between two inquiries on
   the same manuscript; addressed to the editorial office, never to referees.
2. **Proofs change nothing substantive**: fix typographical errors only;
   content changes go through the errata process.
3. **Promises match real files**: the data statement / AI disclosure / CRediT
   entered in the system must match the actual files (per the P33 charter and
   C7 records).
4. **Rejection cooldown**: no submission action within 24 hours of a rejection.

## Workflow (P33–P38 in `prompts/en/08`)

### A. S0 initiation (P33, before writing)
The seven charter questions: backward-planned milestones (≥ 25% buffer) →
data-availability pre-check (with a backup dataset) → compute budget →
authorship (CRediT per person + written order agreement) → preregistration
decision tree (Registered Reports / pre-analysis plan / a written
"why-not-preregistered" rationale) → literature monitoring plan → risk
register.

### B. Submission execution (P34–P35, submission day)
1. P34 field-by-field plan: file pre-check (anonymization leaks / formats /
   sizes) → mandatory-field mapping (data / funding / COI / AI disclosure /
   CRediT) → technical veto points → upload order → receipt inspection →
   **record the manuscript ID and submission date**.
2. P35 preprint: policy check → endorsement path → version-sync discipline →
   license interplay.
3. Within 48 hours: confirm status transition; if stalled, one status-
   confirmation email (P36 template 1).

### C. Waiting & status inquiries (P36)
The status decoder and inquiry timing live in `docs/11-阶段八-投稿执行与出版跟进.md`
§8.3 (Chinese); the three English templates are in P36. Archive every
communication under `project/correspondence/`.

### D. Decision response (P37)
- Revise: P25 aggregation → P26 response letter → revision with full
  stat-writing / stat-format-lint discipline; extension requests one-shot;
  **literature-freshness search before every revision round**.
- Reject: cooldown → comment triage → appeal assessment (default: don't) →
  re-select via journals/ → **recalibrate the theory-check intensity for the
  new venue** (the calibration table in docs/11 §8.6).
- Accept: go to E.

### E. Proofs & post-publication (P38)
Proofs checklist (typo-only, AQ by AQ, 48–72h) → copyright/OA/license
decisions → first 30 days (restrained promotion / citation alerts / errata
template) → feed refereeing lessons back into `checklists/` (CONTRIBUTING).

## Status quick decoder (details in docs/11 §8.3)

`Submitted → With Editor` (triage 2–6 weeks) → `Under Review` (3–6 months,
the venue's stated numbers rule) → `Required Reviews Completed` (2–8 weeks) →
`Decision in Process` (1–4 weeks). Inquire at: stated timeline + 4 weeks.

## Related files

`prompts/en/08` (P33–P38) · `docs/11` (calibration table / status decoder /
etiquette, Chinese) · `templates/cover-letter.md` ·
`templates/response-letter.tex` · `checklists/en/C7-pre-submission.md` ·
`journals/en/` (resubmission venue selection)
