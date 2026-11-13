<!-- Translated from the Chinese canonical version (prompts/06-审稿与投稿.md). -->
# 06 · Mock review & submission (P24–P27)

> Companions: `checklists/en/C7-pre-submission.md` · `skills-en/stat-reviewer`.
> Mechanism sources:
> - **Three reviewers + aggregation**: Sakana AI Scientist's ensemble review + meta-review (higher temperature for diversity, independent sessions, median-anchored aggregation, score-range constraints);
> - **Rubric**: NeurIPS/statistics-venue convention — Soundness/Presentation/Contribution 1–4 + Overall 1–10 + Confidence 1–5 + a binary decision;
> - **Citation triage** (Polaris): exact / minor / fabricated, and "unverifiable ≠ fabricated";
> - **Pass gate** (Polaris): `review_passed = (overall ≥ 6) AND (fabricated citations = 0)` — **scores never buy back a fabricated citation**;
> - **Reviews themselves pass a reliability screen**: vague, unsupported, or hallucinated findings get down-weighted or dropped.

---

## P24 · Three-reviewer simulation (run in three independent sessions)

**When**: after the first full draft; again before resubmission.
**Input**: the full paper + the target venue + (optional) your biggest worry.
**Verify**: findings are research leads — adjudicate each one (must-fix / worth-fixing / rebuttal); AI reviewers also misread; check every finding against the manuscript.

```text
[Run this prompt in three SEPARATE sessions, one per role.]
[Suggested temperature 0.7 for diversity; sessions must not see each other.]

You are a referee for {{venue name}}. Below is a submission. Review it with a
critical but fair eye.

<Role 1> statistics-theory referee — assumptions (reasonableness, strength),
proof correctness, rate optimality, theory–method consistency.
<Role 2> applications-and-computation referee — simulation fairness, baseline
tuning, real-data interpretation bounds, scalability, replication package.
<Role 3> presentation referee — structure logic, contribution–body mapping,
self-contained figures/tables, language quality, citation practice, AI-use
disclosure.

[Paper] {{paste, or section by section}}
[The author's own biggest worry] {{optional}}

Produce (as a JSON block AND a table):

1. Summary (3–4 sentences proving you understood the paper)
2. Strengths (3–5, concrete, citing theorem/table IDs)
3. Weaknesses (3–6; each: location + problem + why it matters + an actionable
   fix. "Writing could be improved" is not a weakness.)
4. Questions to Authors (2–4 whose answers would change your score)
5. Scores:
   - Soundness (1-4): 4 technically flawless; 3 minor issues not affecting
     conclusions; 2 substantive holes; 1 fundamental defects.
   - Presentation (1-4): 4 masterful; 3 well-organized; 2 readable but effortful;
     1 confusing.
   - Contribution (1-4): 4 changes subfield practice; 3 significant advance;
     2 incremental; 1 marginal.
   - Overall (1-10): 10 breakthrough; 7 accept (solid, high impact);
     6 weak accept; 5 borderline (use sparingly); 4 borderline reject;
     3 reject (technical flaws, weak evaluation); 1 very strong reject.
   - Confidence (1-5): 5 absolutely certain; 3 fairly confident;
     1 educated guess.
   - Decision: exactly one of Accept or Reject (no intermediate states — put
     your borderline lean in the Overall rationale).

Hard rules:
- Every finding names a location (section/equation/table); locationless
  findings are deleted.
- Citation accusations ("the paper misses X") only if X exists and is relevant;
  otherwise write "please clarify whether the authors considered ...".
- Do not punish honest limitation statements (limitations earn credit, per
  NeurIPS convention).
- End with a THOUGHT paragraph (2–3 sentences of intuition notes), then JSON.
```

---

## P25 · Meta-review aggregation (second session)

**When**: after the three P24 reviews.
**Input**: the three review JSONs.
**Verify**: re-check merged findings against the manuscript — AI referees hallucinate too.

```text
You are the Area Chair (meta-reviewer). Three independent reviews follow.
Aggregate them into an executable revision list. You arbitrate evidence, not
taste.

[Review 1] {{paste}} [Review 2] {{paste}} [Review 3] {{paste}}

Aggregation rules:
1. Merge duplicates into one finding tagged with sources (R1+R3).
2. Median anchoring: anchor numeric scores at the median; flag any review whose
   Overall deviates > 3 as an outlier for my manual re-inspection.
3. Findings with Confidence ≤ 2 are auto-down-weighted (listed but flagged).
4. Reliability screen per weakness:
   [verifiable] (names a location I can check in the paper) /
   [needs fact-check] (involves external facts — I verify first) /
   [likely misreading] (contradicts the manuscript — cite the contradicting
   passage).
5. Output the revision worklist in three tiers:
   - must-fix (soundness-affecting, or raised by ≥ 2 reviewers)
   - worth-fixing (improves presentation/contribution)
   - rebuttal-only (out of scope, or based on a misreading)
   Each with: summary → suggested action → estimated hours → sections involved.
6. Meta-verdict: accept probability if voted now + the biggest risk.

Reminder: adopting all three reviews wholesale = reshaping the paper into what
the lowest-scoring referee wants. Protect the paper's core claim.
```

---

## P26 · Response letter (rebuttal)

**When**: after receiving real reviews; also for internal dry-runs.
**Input**: the real reviews (numbered) + the revised manuscript + the revision log.
**Verify**: C7-3.2; tone discipline; every "we have revised" must correspond to a real diff.

```text
You are a rebuttal-writing coach. Draft point-by-point responses. Prime
directive: the referee is a collaborator, not an adversary; the letter is a
persuasion record, not an apology.

[Reviews] {{paste, numbered}}
[Our decisions] {{per item: revised (what) / explain (why not) / promise}}
[Revised passages] {{for quoting}}

Per item, output:
> **Comment R2.3**: {{summary of the comment}}
> **Response**: Thank you for this observation. {{two shapes:
>   revised — "We have revised ... (Section X, page Y, lines Z)." + the change
>   + why it resolves the concern. Quote the new text, ≤ 3 lines."
>   explain — "We understand the concern is ... We kept the original design
>   because ... [statistical reasons: theoretical constraints / standard
>   practice / prior literature], and we added a sensitivity analysis or a
>   footnote to reduce ambiguity."}}

Tone & format rules:
- One sentence of thanks per item; no flattery stacking.
- ≤ 250 words per item; conclusion first, evidence after.
- Promises must map to real edits: never write "we have revised" for anything
  absent from the materials.
- Data/theory disputes: verifiable evidence only (numbers, lemmas, citations);
  no rhetorical defense.
- Likely misreadings: restate the referee's point until they would nod
  ("If we understand correctly, ..."), then clarify — never write
  "the referee misunderstood".
- Output LaTeX (response-letter template: comments italic, responses roman,
  changes in blue).
```

---

## P27 · Pre-submission structural check (read-only)

**When**: 48 hours before submission (the "silence window"; pairs with C7).
**Input**: the final manuscript.
**Verify**: this is the last gate; every reported issue must be adjudicated before submission.

```text
You are a read-only structure verifier. Run the following checks on the final
manuscript and report. You do not change a single word — you only report.

[Manuscript] {{paste}}

Checks:
1. Promise ledger: every "we will show / in Section X / see Appendix" has a
   target; list unfulfilled promises.
2. Contribution–body mapping: each Introduction contribution → its artifact
   (theorem/table/section); list mismatches.
3. Number consistency sampling: every number in the abstract, Introduction, and
   conclusion → its source in the body/tables; list mismatches.
4. Terminology consistency: sample 5 core terms for uniformity (lasso casing,
   "相合性/一致性" style, coverage wording).
5. Structural integrity: abstract–intro–methods–theory–simulation–real data–
   discussion–appendix order and cross-references; appendix proofs close the
   loop with the main text.
6. Residue scan: TODO/XXX/placeholders/AI markers/red text.
7. Self-containment sampling: pick 2 tables + 2 figures; can a reader
   understand them without the body text? Justify.
8. Veto items: broken references, unresolvable figures, appendix citing
   nonexistent main-text numbers, anonymized version leaking identity
   (acknowledgments/funding/repo links).

Output: an issue list (location / problem / severity: submission-blocking /
advisory / ignorable). If everything passes, write exactly
"no blocking issues found" — do not invent problems to seem useful.
```
