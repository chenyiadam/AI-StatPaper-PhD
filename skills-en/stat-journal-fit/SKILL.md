---
name: stat-journal-fit
description: Journal style adaptation. use when the user wants to choose a submission venue, reshape a draft into a specific journal's submission-ready form, rewrite in a venue's style, migrate LaTeX formats and citation styles, or draft a venue-specific cover letter — paired with the journals/ directory of 9 venue profiles.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-writing, stat-format-lint]
---

# stat-journal-fit · Journal style adaptation

## Hard disciplines

1. **Adapt style, never content**: adaptation touches expression, structure
   placement, and format only; mathematical meaning, claim strength, and
   numbers are immutable. Three-part output + risk list (as in P20).
2. **The official site wins**: `journals/` profiles summarize conventions;
   page limits, anonymization, and citation styles must be re-checked against
   the venue's current Author Guidelines before submission.
3. **Profile before rewriting**: rewriting without P28's style rule card just
   produces a different AI flavor.
4. **Deletion is a compliance-stage decision**: P29 only moves content;
   deletions are adjudicated at P32.

## The seven-step workflow

### 1. Venue decision
Contribution type (theory / methods / applications) × the profiles' "scope"
sections, item by item; output a target venue + 2 backups + one-line reasons.
Undecided? Run P28 on 2–3 candidates and compare rule cards.

### 2. Style profiling (P28)
Feed 2–3 same-direction venue papers → the style rule card (structure /
sentence habits / theory presentation / experiment presentation / vocabulary /
format signals, each with a quoted sample and an action) → the closing
"gap table".

### 3. Restructuring (P29)
Draft structure → venue conventions: difference list → migration plan
(body / appendix / supplement / pending-deletion) → ID remapping → skeleton →
breakage pre-check.
Typical divergences: JASA sinks all proofs to the appendix ↔ AoS keeps proofs
in the body ↔ Biometrika compresses 30–50%.

### 4. Style rewriting (P30)
Per paragraph, five passes: de-symbol AI flavor (em-dash asides → clauses,
parentheses; keep numeric-range en-dashes) → de-vocabulary (blacklist) →
align sentence habits → align the venue's discourse → spelling system switch
(Biometrika/JRSS-B British).
Triad output per paragraph; the author adjudicates each.

### 5. Format & citation migration (P31)
Template/class swaps → citation-style migration (author-year ↔ numeric mapping
is the heavy item) → figure/table specs → front matter (title page /
acknowledgments / data statement) → anonymization scan → validation commands
(compile + 4 scripts + standalone supplement).

### 6. Venue compliance check (P32)
The venue's dedicated checklist item by item + C7 spot-checks + style
regression (style_check zero warnings; numbers consistent; contribution–
theorem–table mapping intact) → submittable / blocking list.

### 7. Cover letter
Via `templates/cover-letter.md`, the venue version: one-sentence contribution +
why THIS venue (its scope language) + no-simultaneous-submission statement +
one-line AI-use disclosure + 3–5 conflict-free suggested reviewers.

## Migration traps

| Trap | Note |
|---|---|
| author-year → numeric | SIM / Chinese venues / JMLR are numeric; map every \citep — one miss renders as [?] |
| British vs. American spelling | Biometrika, JRSS-B traditionally British; uniform throughout |
| Proofs in opposite places | JASA all-appendix vs. AoS partly in-body — opposite directions for the same paper |
| Terminology systems | JMLR wants excess-risk/sample-complexity bridges; Biometrics wants clinical narrative |
| Anonymization policy | varies by venue and changes — re-verify yearly |
| Chinese references | Chinese-core venues require Chinese-language references (CNKI); AI pools usually miss them |

## Related files

`journals/` (9 profiles; `journals/en/` for English) ·
`prompts/en/07` (P28–P32) · `checklists/en/C5`, `checklists/en/C7` ·
`templates/cover-letter.md` · `templates/response-letter.tex` ·
`scripts/style_check.py`
