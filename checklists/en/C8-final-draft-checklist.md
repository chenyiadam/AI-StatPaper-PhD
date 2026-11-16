<!-- Translated from the Chinese canonical version (checklists/C8-定稿逐项检查清单.md). -->
# C8 · Final-draft item-by-item checklist (mandatory checks between first draft and submission)

> Position: this sits between C5 (format quick reference) and C7 (countdown
> process) as the **item-level adjudication layer** — every item is decidable
> (pass / fail / not-applicable with a written reason), executed against the
> target venue until everything is cleared.
> Automation entry point:
> `python scripts/presubmit_check.py main.tex appendix.tex supplement.tex --bib refs.bib`
> (orchestrates the four existing scripts plus the new deterministic checks for
> this checklist; output maps onto groups A–E below; items that cannot be
> decided automatically carry [manual] actions).
> Fixing principle: **automated checks locate problems; fixes happen in the
> corresponding prompts** (format → P31; language → P20/P21; citations → P07;
> theory → P10) — deterministic code never edits the manuscript.

## How to use (three passes)

1. **Pass 1 · mechanical**: run `presubmit_check.py`; clear every [automatic] item;
2. **Pass 2 · item-by-item**: walk the [manual] items A→E in order; mark each
   pass / N-A + reason;
3. **Pass 3 · regression**: after edits, rerun the script and spot-check the
   touched items (fixing A must not break B).

---

## A. Venue-format hard requirements (the venue's official guidelines are the sole authority; `journals/` profiles are the index)

- [ ] A1 **Item-by-item cross-check action**: open the target venue's Author
      Guidelines and transcribe every formatting requirement into your own
      checklist (A2–A12 below is the generic skeleton; append venue-specific
      items at the end)
- [ ] A2 Title page: title capitalization style (Title Case vs Sentence case
      per venue); author full-name spellings and **order** (= the CRediT-agreed
      order); affiliations formatted; corresponding-author mark; ORCID [manual]
- [ ] A3 Funding & acknowledgments: grant numbers in full and format (per
      template); acknowledgments placement (footnote / own section / title
      page); conflict-of-interest statement per venue; anonymized version
      strips acknowledgments and funding [manual]
- [ ] A4 Abstract & keywords: abstract word count (statistics venues commonly
      150–250; **presubmit_check counts automatically**); structured or not;
      keyword count (commonly 3–6, **counted automatically**) and **ordering
      rule** (alphabetical / importance order, per venue); whether citations
      and abbreviations are allowed in the abstract [auto + manual]
- [ ] A5 Heading levels: level-1/2 heading style (numbered vs unnumbered,
      capitalization, statement-style headings per venue); **whether level-3
      headings are allowed** (some venues allow two levels only —
      `presubmit_check` detects `\subsubsection` and prompts the check);
      whether Discussion/Conclusion sections are required [auto-prompt + manual]
- [ ] A6 Body format: punctuation uniform (Oxford-comma consistency; full-width
      punctuation in Chinese manuscripts); numbering systems (equations /
      theorems / figures / tables each independent; `cleveref` references with
      no hand-typed numbers — **notation_check automatic**); figure/table name
      style (Figure/Fig./图, uniform throughout) [auto + manual]
- [ ] A7 Abbreviation style: every abbreviation expanded once at first use;
      abbreviation-only afterwards; one abbreviation per concept (LASSO/lasso
      casing uniform); no abbreviations in titles (unless near-universal like
      MSE) [manual, glossary-assisted]
- [ ] A8 Figures: vector preferred (PDF/EPS); raster ≥ 300 dpi; widths per
      venue (single/double column); ≥ 8 pt effective after scaling;
      colorblind-safe + black-white-readable (C5-D) [manual]
- [ ] A9 Figure/table layout: **centered or left-aligned** per venue (figure
      environments center by default; set explicitly if the venue differs);
      **decimal places in tables**: uniform per column, three-digits rule
      (**presubmit_check detects mixed decimal precision per column**);
      complete table notes (replications / criterion / abbreviations)
      [auto + manual]
- [ ] A10 Forbidden things (AI/format pathologies): **prose em-dashes** (numeric
      ranges keep en-dashes — style_check automatic); **\item abuse**
      (consecutive list environments, single-item lists, more than 3 list
      environments in one section — **presubmit_check automatic**);
      **metaphorical quotation marks** (scare-quote "so-called X" style, prose
      straight quotes — **presubmit_check detects straight quotes and suggests
      rewrites**) [automatic]
- [ ] A11 In-text citation style: author-year / numeric per venue; \citep/\citet
      used correctly; superscript or not; citation sentence patterns varied
      (avoid every paragraph ending "(Author, 2020)") [auto-triage + manual]
- [ ] A12 End-of-paper references: **sorting rule** (order of citation /
      alphabetical, per venue); journal-name abbreviation policy uniform;
      published arXiv items upgraded; no orphan entries, no missing fields
      (**citation_check automatic**) [automatic]

## B. Citation-authenticity closeout (maps to C6; the final round before submission)

- [ ] B1 Every citation truly exists: L1 fully passed (DOI resolves, Scholar
      hits) [manual sampling + citation_check formal layer]
- [ ] B2 **Uncertain references: replace or delete** — the iron rule is "better
      fewer citations than a doubtful one": any reference shaky at L1/L3 is
      either replaced by a verified equivalent or deleted with the sentence
      lightly reworked; **never submit carrying a "it probably exists" citation**
      [manual]
- [ ] B3 In-text descriptions of citations are accurate: paraphrase agrees with
      the original in direction, strength, and conditions (the three L3
      mismatch types, one by one) [manual]
- [ ] B4 Text–bib bidirectional consistency (**citation_check automatic**)
      [automatic]

## C. Content completeness (theory verification)

- [ ] C1 Theory derivation: walk all of C2 + calibrate check intensity to the
      target venue's tier in `docs/11` §8.6 (tier L3 line-by-line requires
      recomputing the key inequalities by hand) [manual]
- [ ] C2 **Body–appendix one-to-one correspondence**: every numbered
      theorem/lemma/proposition/corollary in the body has a proof location
      (in-text or "Proof of Theorem X" in the appendix) — **presubmit_check
      automatically cross-references theorem labels against the appendix** and
      emits a "no appendix counterpart" list for human adjudication (some
      results are proven in-text, which is legitimate — but each must be
      confirmed) [auto-triage + manual adjudication]
- [ ] C3 Appendix complete, detailed, accurate: the lemma chain is whole (every
      cited intermediate result proved first); no residual "obviously"
      (**notation_check automatic scan**); constant numbering not reused;
      notation consistent with the body (**notation_check automatic**)
      [auto + manual]
- [ ] C4 Theorems/propositions/lemmas **not abused**: the right environment
      (main result → theorem, auxiliary → lemma, direct consequence →
      corollary, commentary → remark); counts sensible
      (**presubmit_check reports the environment distribution**; e.g., more
      corollaries than theorems is an anomaly signal); every numbered result
      cited in the text (**notation_check automatic**) [auto-statistics + manual]

## D. Language & logic

- [ ] D1 **Natural sentence-to-sentence flow**: every sentence has an
      identifiable relation to the previous one (continuation / contrast /
      cause / example); connector density normal (stacked Moreover ≤ 3 —
      style_check automatic); read-through for "jump sentences" (where the
      reader must invent the bridge) [auto + manual read-through]
- [ ] D2 **Every paragraph has a point**: the opening sentence states the
      claim; one idea per paragraph; delete sentences serving no claim
      [manual]
- [ ] D3 **No meta-statements**: per-paragraph previews ("In this section we
      will discuss..." — one roadmap sentence per section is convention;
      per-paragraph/per-sentence previews are meta-talk); "As mentioned above /
      as discussed earlier" abuse; "It should be noted"; unfulfilled promises
      (search "we will show" — **presubmit_check detects meta patterns and
      promise sentences**) [auto + manual]
- [ ] D4 Transitions and explanations exist: every theorem followed by
      interpretation (meaning / rate implications); every equation followed by
      symbol explanations; every figure/table interpreted in prose
      (**fig_table_check automatic** for reference closure; the interpretation
      prose [manual]) [auto + manual]
- [ ] D5 Language accuracy: tense, terminology, tone per C4; glossary hard
      conventions such as estimator/estimate [manual + glossary]

## E. Experiment alignment (do the experiments embody the paper's and algorithm's ideas?)

- [ ] E1 **Experiment-purpose mapping table** (this checklist's core artifact):
      list `experiment item (scenario/metric/dataset) → the paper claim it
      supports → the corresponding theorem or argument ID`; any row with no
      "claim" entry is a useless experiment (delete it or add the claim); any
      Introduction contribution with no experiment row is an empty claim (add
      experiments or soften the claim) [manual]
- [ ] E2 **Implementation matches the paper**: the code's objective/loss/
      penalty matches Eq. (1) term by term; λ and hyperparameters consistent
      with the theoretical order; pseudocode consistent with the implementation
      (stat-simulation-audit P14 already checked; re-verify that final-stage
      edits did not break consistency) [manual]
- [ ] E3 **Experiments "act out the theorem"**: boundary scenarios present
      (conditions just satisfied / just violated); inference experiments
      include size calibration and coverage (of the true parameter);
      heavy-tailed/non-Gaussian scenarios present [manual, against the P13 grid]
- [ ] E4 Interpretation and number reconciliation: all numbers in the prose ↔
      experiment output ± 0.01; simulation conclusions disagreeing with theory
      reported honestly and explained [manual + number–cell table]
- [ ] E5 Component evidence (the algorithm's ideas at work): ablation/
      sensitivity analyses decompose each component's contribution (proving
      "mechanism X is doing the work," not a black-box win) [manual]

---

## Completion standard

- `presubmit_check.py` exit code 0 (or a written "won't fix" reason per
  [automatic] item)
- Every A–E item: pass / N-A + one-line reason; zero pending items
- Archive this completed checklist under `project/` (alongside the C7 records);
  reusable as the revision baseline during refereeing
