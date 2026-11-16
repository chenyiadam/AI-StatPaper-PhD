---
name: stat-format-lint
description: LaTeX format and consistency checking. use when the user wants format checks, cross-reference fixes, numbering cleanup, figure/table discipline, or submission-pack preparation (anonymization / page limits / template switches) — i.e., stage S7 formatting and the submission package.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-writing]
---

# stat-format-lint · Format checks & submission prep

## Hard disciplines

1. **Scripts do the mechanical layer; humans adjudicate the semantic layer**:
   this skill dispatches the five scripts in `scripts/`, and every finding is
   adjudicated by a human before any fix.
2. **Two passes before verdicts**: all "broken reference" judgments happen
   after latexmk / two xelatex runs + bibtex.
3. **Red markers cleared**: `\TODO{}`, `\AICHECK{}`, `\REFCHECK{}` must be
   zero before the submission build (the script scans for them).

## Workflow

### A. Automated checks (every freeze)

```bash
# One-shot orchestrator (recommended): aggregates all four scripts below plus
# the C8 checks (abstract/keyword counts, level-3 headings, list abuse,
# straight quotes, meta-statements, theorem-env distribution, body–appendix
# proof correspondence, per-column decimals)
python scripts/presubmit_check.py main.tex appendix.tex supplement.tex --bib refs.bib

# — or run each script individually —

# 1. Citation consistency: text–bib bidirectional, field completeness, orphans
python scripts/citation_check.py main.tex appendix.tex --bib refs.bib

# 2. Notation & environments: duplicate labels/macros, dangling refs,
#    uncited theorems, "obviously" scan
python scripts/notation_check.py main.tex appendix.tex supplement.tex

# 3. Figures/tables: reference closure, self-contained captions, booktabs rules
python scripts/fig_table_check.py main.tex appendix.tex

# 4. AI-flavor symbols & words: em-dash asides, flagged words, connector density
python scripts/style_check.py main.tex appendix.tex
```

Non-zero exit = findings; process each until the run is clean or every
remaining item has a recorded "won't fix" reason. Walk the manual items via
`checklists/en/C8-final-draft-checklist.md` (three passes: mechanical /
item-by-item A–E / regression). Fixes happen in the prompts: format → P31 ·
language → P20/P21 · citations → P07 · theory → P10.

### B. Statistics-venue format discipline (manual; checklist C5)

1. Theorem systems: `\newtheorem` centralized in the preamble; assumptions
   numbered separately; all references via `\cref`/`\eqref`.
2. Three-line tables: booktabs; no vertical rules; decimal alignment; table
   notes carry replications, criteria, abbreviations.
3. Math typesetting: upright operators (\mathrm{Var}), \mathbb{E},\mathbb{P},
   ^\top; punctuation after display equations; where-clauses for new symbols.
4. Figures: vector PDF; colorblind-safe palettes (Okabe-Ito / viridis);
   black-white-safe redundant encoding; ≥ 300 dpi for raster.
5. Terms & abbreviations: full form at first use; estimator/estimate kept
   distinct throughout.

### C. Template & venue adaptation

1. Write from `templates/latex/main.tex` (JASA-style); switching venues swaps
   class + bst only, the content layer stays.
2. Over-length migration path: proofs → appendix; secondary tables →
   supplement; `supplement.tex` compiles standalone.
3. Double-blind branch: acknowledgments/funding/third-person self-citations/
   anonymous replication repo; build a separate anonymous version.
4. Line numbers per the submission system's requirements.

### D. Submission-pack checks (C7 Day −3/−1 items)

- [ ] zero compile errors; warnings reviewed (overfull boxes one by one)
- [ ] global search: TODO / AICHECK / REFCHECK cleared
- [ ] PDF page-by-page inspection: embedded fonts, crisp figures, live links
- [ ] replication package: README one-command run tested; lock files present;
        DOI minted
- [ ] system metadata + suggested reviewers + cover letter ready
- [ ] download the receipt PDF and inspect it again

## Quick-fix table

| Symptom | Root cause | Fix |
|---|---|---|
| "?? " cross-references | single pass / typo'd label | latexmk full cycle; notation_check finds typos |
| Uncited figure/table | missing \cref | fig_table_check lists them |
| Incomplete bib fields | hand-typed entries | re-export from the publisher |
| Theorem numbering drift | hand-written numbers | switch to \cref + environments |
| Supplement refs broken | standalone build | make supplement labels self-contained |
| Anonymized version leaks | acknowledgments/links | grep acknowledgments, thanks, github |

## Related files

`scripts/citation_check.py` · `scripts/notation_check.py` ·
`scripts/fig_table_check.py` · `scripts/style_check.py` ·
`checklists/en/C5-format-figures.md` · `checklists/en/C7-pre-submission.md` ·
`docs/08` (Chinese) · `journals/` (style rewriting belongs to stat-journal-fit;
this skill handles the format layer) · `templates/latex/` ·
`scripts/presubmit_check.py` (one-shot orchestrator aggregating the four) ·
`checklists/en/C8-final-draft-checklist.md` (the three-pass master checklist)
