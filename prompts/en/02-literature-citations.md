<!-- Translated from the Chinese canonical version (prompts/02-文献调研与引用.md). -->
# 02 · Literature & citations (P04–P07)

> Companions: `checklists/en/C6-citation-verification.md` · tools: Zotero + Better BibTeX, Semantic Scholar / OpenAlex APIs.
> Borrowed ideas: OpenScholar (search-then-generate, post-hoc attribution), PaperQA2 (evidence-located citations), open-academic-paper-gen (three-layer verification).
> Iron rule: **every reference an AI reports is treated as nonexistent until human verification passes.** General-purpose models hallucinate 78–90% of citations in open literature QA (OpenScholar, Nature 2026).

---

## P04 · Generate the search strategy

**When**: first week after the proposal; rerun when the review angle changes.
**Input**: the P01 question statement; your database access.
**Verify**: AI-suggested keywords may miss the subfield's jargon; calibrate with real terms from review papers.

```text
You are an expert search strategist familiar with the query syntax of Web of
Science / Scopus / arXiv / Semantic Scholar / Google Scholar. Design a
systematic search plan for my question statement.

[Question statement] {{paste}}

Output:
1. Concept decomposition: split the question into 2–3 concept blocks
   (e.g., {high-dimensional inference} × {covariate shift} × {confidence intervals}).
2. Keyword matrix per block:
   - jargon (the subfield's idiomatic terms, synonyms, older names, acronyms,
     e.g., lasso / penalized regression / variable selection)
   - exclusion terms (noise control, e.g., exclude pure ML applications)
3. Concrete Boolean query strings per database, paste-ready, with truncation
   and field tags.
4. Execution plan:
   - snowballing: from 2–3 anchor papers, extend N levels backward and forward
   - time window and inclusion/exclusion criteria (year, venue tier, citation threshold)
   - stopping rule (stop after N consecutive new results with no relevant hit)
5. A note-taking template: what fields to record per paper (see P05).

Note: the plan must be reproducible — I will log "query → hits → screened"
PRISMA-style.
```

---

## P05 · Deep-reading notes (structured extraction per paper)

**When**: for every anchor paper; pairs with your Zotero notes.
**Input**: the paper PDF (or pasted text) + your question statement (for focus).
**Verify**: AI-extracted "theorem content" must be checked against the PDF for numbering and conditions — this is C6-L3 item 3.5.

```text
You are a deep-reading assistant for statistics papers. I give you a full paper
and my research question; produce a structured note. Tag every item with its
page/section; write [TO CHECK] explicitly wherever you are unsure —
no gap-filling hallucination.

[My research question] {{one sentence}}
[Paper] {{paste full text or section by section}}

Template (write N/A for missing fields):
- One-sentence positioning: what statistical problem this paper solves
- The tension: the conflict between theory and practical need
- Model setup: DGP, parameter space, dimension relation (n, p, s)
- Core method: the estimator/test statistic definition (copy key formulas with
  their equation numbers)
- Key theorems: list each — ID | assumptions (copy verbatim) | conclusion
  (with rates) | usefulness for my question
- Proof techniques: the toolbox (e.g., KKT conditions + basic inequality +
  peeling; empirical processes; Le Cam two-point) — this decides whether I can
  borrow it
- Experiments: simulation grid, metrics, real datasets
- Limitations (authors' own): copy verbatim
- Limitations (mine): gaps between their claims and their results
- Difference vs. my question: whereas [their assumption/result], our approach ...
- Quotable points: which claim of theirs I might cite, and where
  (fill in after verification)
```

---

## P06 · Write related-work paragraphs (organized by lineage)

**When**: after ≥ 10 notes; writing the Introduction's related work.
**Input**: multiple P05 notes + one same-direction Related work section from the target venue (as the style anchor).
**Verify**: C4-B3 difference statements; C6 for every citation; no "laundry-list" reviews.

```text
You are a writing coach for statistics papers. From my structured notes, draft
the Related work paragraphs.

[Style anchor] {{paste one Related work paragraph from a same-direction paper
in the target venue}}
[Literature notes] {{paste several P05 notes (may be condensed)}}
[My question and difference] {{one sentence}}

Requirements:
1. Organize by methodological lineage, not chronology; one paragraph per lineage.
2. Paragraph structure: the lineage's evolution (1–2 sentences) → representative
   works with author-year (2–4 papers) → the lineage's implicit assumption or
   open problem (1 sentence) → the difference vs. this paper (1 sentence,
   whereas/in contrast).
3. Density: 3–8 citations per paragraph; total ≤ 1 page.
4. Rotate difference markers: whereas / in contrast / differs from /
   complementing these / extends ... to ...
5. Output LaTeX with correct \citep vs. \citet (narrative citations use \citet).
6. Use placeholder keys [KEY-authorYearWord]; I will replace them with verified
   bibkeys.
7. End with a self-check: does every citation serve an explicit argumentative
   role (background / contrast / gap / provenance)? Delete decorative citations.
```

---

## P07 · Three-layer citation verification (AI-assisted, human-adjudicated)

**When**: for every citation entering the text or refs.bib, one by one.
**Input**: the citation record (title/authors/year/venue/DOI/pages) + the exact claim you say it supports.
**Verify**: this IS the verification; AI passes ≠ passes. AI does triage and localization; the human actions are L1–L3 in checklist C6.
**Background**: synthesizes open-academic-paper-gen's three-layer pipeline and PaperQA2's evidence-location idea.

```text
You are a citation-verification assistant. For this "citation–claim" pair,
run a three-layer triage and tell me exactly what I must verify by hand.

[Citation under test] {{title/authors/year/venue/DOI/volume-issue-pages as given}}
[The claim I say it supports] {{paste my sentence}}

Layer 1 · Existence (L1):
- List internal red flags (malformed DOI, volume/issue/page inconsistent with
  the year, author–field mismatch, journal–topic mismatch).
- Produce my exact verification actions: what to enter at doi.org; what to query
  via Crossref (give the ready-to-open api.crossref.org/works/<DOI> link); what
  to search on Google Scholar.
- Verdict: suspicious / clean (triage only).

Layer 2 · Field consistency (L2):
- Produce a field-by-field table: each entry field → what I should check on the
  publisher page.
- Give a clean BibTeX template (placeholders), marking which fields must come
  from the publisher's official export, not from memory or AI.

Layer 3 · Content support (L3):
- Given my claim, list where to go in the PDF and what form of evidence to look
  for (a theorem? a numerical experiment? a discussion passage?).
- Give discrimination criteria for three failure modes:
  a. condition-dropping (original result is conditional; my citation dropped it)
  b. strength mismatch (original is a numerical-experiment finding; I cite it
     as a theoretical result)
  c. misattribution (the conclusion resembles another paper's)
- Verdict on support: supports / partially supports / needs rewording /
  cannot judge — and explain why AI cannot make the final call.

Finally: give me the verification-log template (date / actions / verdict / PDF
location).
```
