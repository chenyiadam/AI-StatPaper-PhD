---
name: stat-research
description: Topic refinement and literature research for statistics papers. use when the user wants to refine a research question, map research gaps, generate search queries, deep-read and organize literature, or write related-work paragraphs — i.e., stages S1 (question) and S2 (literature).
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-citation-verify]
---

# stat-research · Research question & literature

## Hard disciplines

1. **AI never fabricates literature**: statements about specific papers come
   only from (a) the author's list or (b) real search-tool output; everything
   else is tagged `[TO VERIFY]`.
2. **Structure before content**: build the lineage map first, fill content
   second; chronological laundry lists are forbidden.
3. Questions must land on a **statistical property** — consistency, rate,
   coverage, identifiability, robustness — never on "improve accuracy /
   enhance robustness".

## Workflow

### A. Refine the question (S1)
1. Run **P01** in `prompts/en/01`: four steps — restate → deconstruct (name the
   exact failing property) → 3 candidate questions (tension / attainability /
   risk / difficulty) → demotion test.
2. Test candidates against `checklists/en/C1-topic-selection.md` group A
   (concrete answers required).
3. Run **P02** for gap mapping (before and after the actual search).

### B. Search (first half of S2)
1. Run **P04**: concept decomposition → keyword matrix → Boolean queries per
   database → snowball plan → stopping rule.
2. Log PRISMA-style: query → hits → deduplicated → screened → deep-read.
3. Sources: Semantic Scholar API / OpenAlex / Google Scholar / arXiv
   (stat.TH etc.); Web of Science/Scopus when available.
4. Import to Zotero + Better BibTeX; citekeys `{firstAuthor}{year}{firstWord}`.

### C. Deep reading (mid S2)
1. Per anchor paper run **P05**: setup / key theorems (assumptions & rates
   verbatim) / proof toolbox / experiments / limitations / difference vs. ours.
2. AI-extracted theorem content **must be checked against the PDF** (wrong
   lemma numbers are a classic AI error).
3. Store notes in `project/notes/`, named `authorYear-word.md`, linked to the
   Zotero attachment.

### D. Related work (late S2)
1. With ≥ 10 notes run **P06**: lineage paragraphs, difference statements,
   placeholder citekeys pending verification.
2. Every citation passes stat-citation-verify's three layers before a real
   bibkey replaces the placeholder.

## Exit artifacts (to enter S3)

- [ ] one-page problem statement (question + tension + gap map)
- [ ] reproducible search log
- [ ] literature notes (each with the "difference vs. ours" field)
- [ ] refs.bib skeleton (every entry through C6 L1/L2)

## Related files

`prompts/en/01`, `prompts/en/02` · `checklists/en/C1`, `checklists/en/C6` ·
`docs/02`, `docs/03` (Chinese) · `scripts/citation_check.py`
