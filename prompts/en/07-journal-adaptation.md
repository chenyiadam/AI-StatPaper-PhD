<!-- Translated from the Chinese canonical version (prompts/07-期刊风格适配.md). -->
# 07 · Journal style adaptation (P28–P32)

> Companions: `journals/` (9 venue profiles; the ammunition source) · `skills-en/stat-journal-fit` · `checklists/en/C5` · `templates/cover-letter.md`.
> Goal: reshape a draft that already passed S1–S6 into the target venue's submission-ready state.
> Iron rule: adapt style, never content — no rewrite may change mathematical meaning, claim strength, or numbers (same three-part output and risk-list mechanism as P20/P21).

---

## P28 · Profile the venue's style (produce the style rule card)

**When**: first step after choosing the venue; rerun when switching venues.
**Input**: 2–3 same-direction papers from the venue (full text, or Introduction + methods opening + one theorem statement + one table) + `journals/en/<venue>.md`.
**Verify**: every rule must be actionable — each answers "what does this sentence become?"

```text
You are a journal style analyst. From the venue profile and same-direction
samples I provide, produce a "style rule card" for later paragraph-level
rewriting.

[Venue profile] {{paste journals/en/<venue>.md}}
[Sample papers] {{key parts of 2–3 same-direction papers}}

Output the rule card (each rule: name / convention / one quoted instance from
the samples / the action for my paper):

1. Structure rules: section organization; how contributions are presented
   (list vs. woven prose); Discussion presence and shape; where proofs live
   (body/appendix); length feel.
2. Paragraph & sentence rules: average paragraph length; paragraph-opening
   style (claim sentence vs. background); preferred difference markers; "we"
   density; tense conventions.
3. Theory-presentation rules: theorem density; assumption–remark pairing; how
   rates are discussed against the literature; proof detail level.
4. Experiment-presentation rules: table density and format; scenario
   presentation; how much data storytelling; replication-material conventions.
5. Vocabulary rules: the venue's high-frequency scholarly words (counted from
   samples); words it shuns (plus the AI-flavor list); spelling system
   (British/American).
6. Format signals: citation style, figure/table specs, theorem-environment
   numbering.

End with a "gap table": my draft's opening paragraph side-by-side with a sample
opening paragraph, and the 5 most glaring style gaps (show me the gaps before
touching anything).
```

---

## P29 · Restructure (draft → venue skeleton)

**When**: after the rule card.
**Input**: the draft's structure + the venue profile's structure conventions.
**Verify**: C4-D2 contribution–body mapping survives; theorem–proof references stay closed.

```text
You are a paper structure architect. Reshuffle my draft into the target venue's
structural conventions. Deliverable: a migration plan + a skeleton — not
paragraph-level rewriting.

[Draft structure] {{section titles + 2-sentence summaries + list of existing
theorem/table IDs}}
[Venue conventions] {{the profile's structure section + the P28 structure rules}}

Output:
1. Difference list: draft vs. venue conventions, section by section (add /
   delete / move / merge / split), each with a reason and blast radius (which
   cross-references change).
2. Migration plan table: content block → destination (body / appendix /
   supplement / pending-deletion), with an ID remapping table
   (old → new: Thm 3 → Thm 2, Lemma A.4 → B.2).
3. The restructured LaTeX skeleton (section tree + first-sentence placeholder +
   a list of cross-references to rewrite).
4. Breakage check: after restructuring, is every theorem/table/equation still
   cited and every citation resolvable (a pre-run checklist for
   notation_check.py).

Constraint: blocks may move or sink; nothing is deleted at this stage —
deletions are adjudicated at the P32 compliance check.
```

---

## P30 · Style rewriting (paragraph-by-paragraph venue voice)

**When**: after restructuring, section by section.
**Input**: one restructured section + the P28 rule card + a sample same-function passage from the venue.
**Verify**: zero content change (three-part output + risk list); numbers and citations untouched.

```text
You are a senior editor at this venue. Rewrite the passage below into the
venue's voice per the style rule card. All P20/P21 disciplines apply
(expression only, never content; modification thresholds; protected zone =
formulas and LaTeX commands).

[Style rule card] {{the relevant P28 rules}}
[Sample reference] {{1–2 same-function passages from venue papers}}
[Text to rewrite] {{paste}}

Per-paragraph sequence:
1. De-symbol the AI flavor: remove em-dash asides (— / ---) in prose — replace
   with clauses, commas, or parentheses; KEEP en-dashes in numeric ranges
   (1990--2000); thin colon-led sentence chains; split semicolon chains.
2. De-vocabulary the AI flavor: run the blacklist (delve/leverage/pivotal/...).
3. Align sentence habits: paragraph-opening style, paragraph length, difference
   markers per the rule card.
4. Align the venue's discourse: how theorems–rates–optimality are discussed per
   venue convention (AoS minimax talk / JASA contribution talk / Biometrika
   restraint).
5. Switch the spelling system (British/American) if the venue expects it.

Output: Part 1 [Rewritten] (LaTeX, protected zone untouched);
Part 2 [Comparison]: original → rewritten → which rule fired;
Part 3 [Risk list]: edits that might have touched meaning, for my adjudication.
```

---

## P31 · Format & citation migration (compile-ready submission)

**When**: after style rewriting.
**Input**: the venue profile's format section + current LaTeX sources + bib.
**Verify**: zero compile errors; all five scripts pass; the supplement compiles standalone.

```text
You are a LaTeX submission engineer. Produce a "migration work order" to move
my sources onto the target venue's template.

[Venue format requirements] {{the profile's format section}}
[Current sources] {{main/appendix/supplement/refs.bib + current document class}}

Work order, in order:
1. Template migration: document class / style swaps; macro conflict scan
   (\newtheorem numbering, \cref config); margins, font size, spacing.
2. Citation-style migration: bst switch (author-year ↔ numeric is heavy — give
   the \citep/\citet → \cite mapping rules); bib field completion list (fields
   the new style requires); in-text format checks.
3. Figure/table migration: sizes (width/font/dpi), caption position, booktabs
   check, numbering style (Figure 1 vs Fig. 1 vs 图 1).
4. Front matter: title page, author footnotes, acknowledgments, funding, data
   availability statement in the venue's shape.
5. Anonymization (if required): leak scan list (acknowledgments / repo links /
   self-citations / paths).
6. Validation: the post-migration command list
   (2× compile + bibtex + the five check scripts + standalone supplement build).

Output as a checkable list, each item tagged "manual / scriptable".
```

---

## P32 · Venue compliance check + cover letter

**When**: after migration, 48 hours before submission (merged with the C7 countdown).
**Input**: the submission version + the venue profile + the venue's current official guidelines (human-checked).
**Verify**: this is the final gate; the official guidelines override the profile.

```text
You are a compliance officer. Check the submission against the venue profile
and checklist C7. Report only — do not modify.

[Submission] {{full text / file list}}
[Venue profile] {{all of journals/en/<venue>.md}}
[Guideline deltas] {{what the author verified on the official site that differs
from the profile}}

Output:
1. Item-by-item check of the venue's dedicated transformation checklist
   (pass / pending / n-a).
2. Spot-check of the C7 countdown (Day −7 / −3 / −1 key items).
3. Style regression check — did anything creep back:
   a. style_check.py zero warnings (symbols & vocabulary)
   b. abstract/intro/conclusion numbers still consistent with the body
   c. contribution–theorem–table mapping intact after restructuring.
4. Cover letter: per templates/cover-letter.md, produce the venue version —
   one-sentence contribution + why THIS venue (quote its scope language and
   recent related papers) + originality/no-simultaneous-submission statement +
   one-line AI-use disclosure + 3–5 suggested reviewers (no conflicts; the
   nearest-neighbor authors from your verified literature pool).
5. Final verdict: submittable / blocking-issue list (each with a fix action).
```
