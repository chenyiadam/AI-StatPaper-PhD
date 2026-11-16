<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C5 · Format, Figures and Tables Checklist

> Usage: the finalization stage. With [`skills/stat-format-lint/SKILL.md`](../../skills/stat-format-lint/SKILL.md)
> and the checking scripts under [`scripts/`](../../scripts).

## A. Journal/thesis format

- [ ] A1. The template matches the target outlet (JASA/ARXIV/Biometrika/thesis norms); margins, line spacing,
      and font sizes per the guidelines
- [ ] A2. Title page: authors' full names, affiliations, corresponding-author marking, acknowledgments,
      grant numbers (grant-number format verified)
- [ ] A3. Abstract length compliant (about 200 words for most statistics journals); 3–6 keywords drawn from
      the journal's subject term list
- [ ] A4. Section numbering continuous; after \appendix the numbering switches to A/B/C correctly
- [ ] A5. The supplement compiles independently with no broken references (every \ref inside the supplement
      resolves locally)
- [ ] A6. Fonts embedded; image resolution ≥ 300 dpi (vector PDF/EPS preferred)
- [ ] A7. Line numbers (when submission requires them); anonymization (double-blind: acknowledgments, funding,
      repository links, and self-citations recast in the third person)

## B. Mathematical typesetting

- [ ] B1. Numbering schemes: equations (1)…, Theorem 1…, Assumption 1…, Figure 1…, Table 1… independent of one
      another and free of duplicates
- [ ] B2. All references via \cref/\eqref, no "??" after compilation (two passes of latex + bibtex)
- [ ] B3. Display equations carry trailing punctuation (equations are part of the sentence); "where" clauses
      define new symbols
- [ ] B4. Upright operators: \mathrm{Var}, \mathrm{Cov}, \mathbb{E}, \mathbb{P}; transposes as ^\top
- [ ] B5. A matrix/vector bolding policy consistent throughout (lowercase bold vectors, uppercase bold
      matrices), or italic — but uniform either way
- [ ] B6. Alignment points in multi-line derivations are meaningful (aligned at =); overlong lines split

## C. Tables (the three-line (booktabs) discipline of statistics papers)

- [ ] C1. All tables in booktabs three-line style, no vertical rules; numbers decimal-aligned (siunitx or manual)
- [ ] C2. Self-contained headers: meaning and units of each column's metric, and the best-value criterion;
      rows are scenarios and columns are methods (or vice versa), consistent throughout
- [ ] C3. Table notes include: number of repetitions, metric-definition abbreviations, what bolding means,
      and the seed or "see the replication package"
- [ ] C4. Digits follow the three-digits rule; decimal places consistent within a column
- [ ] C5. No "cropping traces": columns do not overflow the text block; multipage tables use longtable with a
      repeated header

## D. Figures

- [ ] D1. Every figure has a self-contained caption: figure + caption alone convey the conclusion, without the text
- [ ] D2. Axis labels complete (quantity, unit); font sizes still readable after scaling (≥ 8pt equivalent)
- [ ] D3. Color-blind-friendly palettes (the viridis family or Okabe-Ito); distinguishable in black-and-white
      printing (redundant coding via line styles/markers)
- [ ] D4. No bitmap jaggies in in-figure text; the meaning of error bars/confidence bands stated in the caption
- [ ] D5. No redundant figure–table duplication: the same result is either a figure or a table, or the text
      explicitly says "the figure visualizes the table"
- [ ] D6. No missing citations: every \begin{figure} is \cref'd from the text
      (run [`scripts/fig_table_check.py`](../../scripts/fig_table_check.py))

## E. References

- [ ] E1. Style matches the journal (author-year vs. numeric); natbib commands uniform
      (\citep/\citet used correctly)
- [ ] E2. All entries field-complete: authors, year, journal name (abbreviations consistent or full names
      consistent), volume(issue), pages, DOI
- [ ] E3. arXiv preprints: replaced by the published version if one exists (AI leaving stale preprints in place
      is a common error)
- [ ] E4. No duplicate entries (two keys for the same paper); case protection ({Bayesian}, {LASSO})
- [ ] E5. In-text citations and the .bib agree in both directions: no \cite{nonexistent} and no orphan entries
      that are never cited (run [`scripts/citation_check.py`](../../scripts/citation_check.py))
