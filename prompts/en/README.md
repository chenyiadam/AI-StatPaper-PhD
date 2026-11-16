# Prompt Library (English) — Overview & Rules

> English versions of the 38 numbered prompts (P01–P38). The Chinese originals in
> `prompts/` remain canonical; both are equivalent in content. Each prompt is
> copy-paste ready. Companion pieces: stage methodology in `docs/` (Chinese),
> journal profiles in `journals/`, automated checks in `checklists/en/` and
> `scripts/`, one-click skills in `skills-en/`.

## Index

| File | IDs | Content |
|---|---|---|
| [01-research-question.md](01-research-question.md) | P01–P03 | Refining the research question, gap mapping, contribution statements |
| [02-literature-citations.md](02-literature-citations.md) | P04–P07 | Search strategy, deep-reading notes, related-work paragraphs, three-layer citation verification |
| [03-theory-checks.md](03-theory-checks.md) | P08–P12 | Theorem landscape, proof drafting, line-by-line attack, assumption review, counterexample construction |
| [04-experiments-audit.md](04-experiments-audit.md) | P13–P16 | Simulation design, code audit, results interpretation, real-data analysis |
| [05-writing.md](05-writing.md) | P17–P23 | Introduction, methods section, figures/tables, polishing, de-AI-flavor, CN–EN translation, abstract & title |
| [06-review-submission.md](06-review-submission.md) | P24–P27 | Three-reviewer simulation, meta-review aggregation, response letters, pre-submission structure check |
| [07-journal-adaptation.md](07-journal-adaptation.md) | P28–P32 | Style profiling, restructuring, style rewriting, format migration, venue compliance check |
| [08-project-initiation-submission.md](08-project-initiation-submission.md) | P33–P38 | Project charter (S0), submission-system execution, preprint strategy, status inquiries & nudges, decision routes, proofs & post-publication |

## Twelve rules of engagement

0. **Five-segment skeleton** (the shared pattern of lab-grade prompts, from
   awesome-ai-research-writing): Role / Task / Constraints / Execution Protocol /
   Input. All 38 prompts follow this skeleton — keep it for your own new prompts.
1. **One prompt does one thing.** Never ask AI to "write the whole paper in one
   go" — that manufactures template prose.
2. **Feed context, not vibes.** Attach (a) your notation table, (b) related
   existing paragraphs, (c) a style sample from the target venue — not just
   "please polish".
3. **AI output is a draft, not a verdict.** Proofs go through checklist C2 with
   human adjudication; citations go through the three-layer verification (C6);
   numbers reconcile against experiment output.
4. **Keep markers.** Wrap AI-generated content in `\AICHECK{}` or comments and
   clear them after verification (`scripts/notation_check.py` finds stragglers).
5. **Cross-examine with multiple models.** For theory checks and mock reviews,
   run at least two independent models/sessions and take the union of findings.
6. **Temperature is quality.** Low temperature for theory checks and citation
   verification; higher for brainstorming and counterexample construction.
7. **Restate before acting.** For long tasks the AI first restates its
   understanding and plan; you confirm, then it executes (built into the prompts).
8. **Push back on "obviously".** When AI says a step is obvious, ask it to list
   the justification and any lemmas used, and to flag every skipped step.
9. **Keep logs.** Archive each stage's AI conversations under `project/ai_logs/`;
   the disclosure statement (checklist C7-4.1) is generated from these logs.
10. **Modification thresholds.** Polishing prompts carry the "respect the
    original, intervene sparingly, prefer no change" threshold (a consensus
    design from awesome-ai-research-writing). If AI rewrites fluent sentences
    for the sake of it, ask it to revert.
11. **Dual output for semantic drift.** Translation/rewriting prompts must emit
    Part 1 [result] + Part 2 [back-translation or comparison] so you can check
    for drift.
12. **Silence before submission.** 48 hours before submission, no major AI
    rewrites — only the read-only structural check in P27.
