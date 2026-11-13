<!-- Translated from the Chinese canonical version (prompts/05-论文撰写.md). -->
# 05 · Writing the paper (P17–P23)

> Companions: `templates/latex/main.tex` (the structural anchor) · `checklists/en/C4-writing-language.md` · `docs/glossary-中英术语表.md` (bilingual glossary).
> Borrowed discipline (Manubot ai-revision / Polaris drafting rules): **process one paragraph at a time**; fixed drafting order (Introduction → Method → ... → Abstract LAST); every number traces to experiment output; every citation comes from the verified pool.

---

## P17 · Write the Introduction (five-paragraph template)

**When**: after the contribution list (P03) and related work (P06) are ready.
**Verify**: C4-D2 contributions map to sections; D1 claims have provenance; the A-group de-AI-flavor items.

```text
You are a writing coach for top statistics journals. Write the Introduction
draft in the classic five-paragraph shape. First restate my materials' logic
chain; then write only after I confirm.

[Five-paragraph skeleton] (strict)
P1 The scientific problem: concrete data/background → WHY it is statistically
   hard (name the property) → what happens if unsolved. Never open with
   "In recent years".
P2 The methodological gap: existing lineages (2–3, with citations) → each one's
   specific statistical defect (consistency/rate/coverage/computation) → one
   sentence stating the gap.
P3 Our method: what we propose + the mechanism intuition (1–2 sentences a
   non-specialist can follow).
P4 Contributions: adopt my contribution list verbatim — do not rewrite numbers.
P5 Remaining literature + organization: one sentence on adjacent directions not
   covered + Section map + appendix/replication pointer.

[Materials] question: {{P01}} contributions: {{P03}} related work: {{P06}}
[Style anchor] {{1–2 opening paragraphs from the target venue}}

Hard constraints:
- Every claim has provenance: a citation (placeholder key) / a theorem number /
  a table number / explicitly flagged "our claim, proven later".
- Numbers, rates, assumption IDs copied verbatim from my materials.
- Each paragraph ≤ 12 lines; whole section ≤ 2.5 pages (LaTeX, single spacing).
- Output LaTeX; wrap AI-written sentences in \AICHECK{} for my clearance.
```

---

## P18 · Write the methods section (from formulas to prose)

**When**: after the method is fixed.
**Input**: the objective function/algorithm draft + notation table + the nearest-neighbor objective function (for differencing).
**Verify**: C2-D1 the theorem targets this estimator; C5-B3 punctuation after display equations and where-clauses.

```text
You are an expert writer of methods sections. Convert my method draft into
Section 2 (Methodology).

[Method draft] {{objective in LaTeX + pseudocode + plain-language intuition}}
[Notation table] {{all symbols and definitions}}
[Nearest-neighbor method] {{its objective function and citation}}

Structure (statistical-paper convention):
2.1 Problem setup and notations: the DGP in one paragraph (every symbol defined
    at first use, in observation–model–target order);
2.2 The proposed estimator: Eq. (1) the objective → a three-part reading right
    after (the statistical meaning of each term) → the form difference vs. the
    nearest neighbor (term-by-term, whereas style) → one sentence on λ's role;
2.3 Algorithm: pseudocode (algorithm environment, every step executable) +
    complexity O(·) + one sentence on convergence (details to the appendix).

Rules:
- Display equations are part of the sentence: they take punctuation; new
  symbols are defined in a where-clause immediately.
- Intuition first, formula second: one sentence of "what it is for" before each
  display equation.
- Symbols come only from the notation table; log any new symbol in the
  "new symbols" section at the end.
- Output LaTeX + the new-symbol list.
```

---

## P19 · Design figures/tables + captions and in-text callouts

**When**: before making figures (design) and after (captions & callouts).
**Verify**: all of C5-C/D; captions self-contained; every figure/table cited.

```text
You are a statistical graphics expert (Tufte school + journal pragmatics).
Two-part task:

[Part 1 · chart selection]
Give a result-type → chart-form recommendation table:
- scenario × method × single metric → faceted lines / heatmap (say which, when)
- paired error distributions (ours vs. baseline) → box/violin + paired lines
- coverage across scenarios → dot plot with the nominal reference line
- compute time → log-scale bars
Include: an Okabe-Ito or viridis palette, redundant linetype/marker encoding
(black-white-safe), minimum font sizes, vector PDF export.

[Part 2 · captions and in-text sentences]
For my results {{describe data and figure}}, write for each figure/table:
1. A self-contained caption template: what the result is + conditions (scenario,
   seed, replications) + how to read it + abbreviation definitions. ≤ 5 lines.
2. Two in-text sentences: one "Figure X shows that ..." reading with exact
   numbers; one theory-bridge sentence pointing at the theorem ID.

Constraints: no "as shown in the figure / clearly" in captions; numbers must
come from my data; output LaTeX (figure/table skeletons + booktabs skeleton).
```

---

## P20 · Academic language polishing (for English journals)

**When**: rolling use after each section's first draft.
**Input**: the paragraph + 2 style samples from the target venue + the glossary.
**Verify**: all of C4-A/B; zero math-content change (check the diff line by line).
**Engineering borrowed from GPT Academic**: protect structure — declare formulas and `\cite`/`\ref`/`\label` commands as a protected zone the model must not touch.

```text
You are a native-level copy editor for statistics journals. Polish the passage
below. Rules:

[Text] {{paste the LaTeX fragment}}
[Style samples] {{2 paragraphs from same-direction venue papers}}
[Glossary] {{the relevant sub-table of docs/glossary}}

0. Protected zone (hard): LaTeX commands (\section/\cite/\ref/\begin/\item,
   etc.) and math ($...$) stay byte-identical — no modification, translation,
   or reordering. Keep escaping (% → \%, _ → \_, & → \&).
1. Expression only, never content: any edit that changes mathematical meaning,
   the range of conditions, or claim strength is a violation. If unsure whether
   an edit touches meaning, list it for me instead of making it.
2. Modification threshold (no presence-seeking edits): keep sentences that are
   already accurate; your value is fixing real defects, not swapping synonyms.
3. Output three parts:
   Part 1 [LaTeX]: the polished text;
   Part 2 [Comparison]: original → edited → reason (type: collocation /
   redundancy / tense / register / terminology);
   Part 3 [Risk list]: all edits that might have touched meaning, for my
   line-by-line adjudication.
4. Sweep on sight: delve/crucial/pivotal/comprehensive/utilize/leverage/
   stacked Moreover/"It is worth noting"/"plays a vital role"; nominalization
   piles; consecutive isomorphic sentences.
5. Tense: methods and conclusions in present; experiments in past; reading
   figures in present.
6. Terminology: follow the glossary; keep the estimator/estimate distinction.
   For a forced replacement, add one line: If the term "X" is used, replace
   with "Y".
7. Statistical conventions: keep whereas/in contrast precise in difference
   statements; impersonal theorem statements; moderate "we" (proposals/findings
   yes, assumption statements no).
8. Register: no contractions (it is, not it's); no possessives on method names
   (the performance of METHOD, not METHOD's performance); never convert
   paragraphs into \item lists.
```

---

## P21 · De-AI-flavor rewrite (mandatory before submission)

**When**: after polishing, before format freeze.
**Input**: the full text (or section by section).
**Verify**: all of C4-A; run the AI self-check after rewriting.
**Word list source**: the AI-flavor replacement list from awesome-ai-research-writing (a collection of working tips from MSRA/ByteDance/Shanghai AI Lab researchers; now maintained at github.com/Leey21/awesome-ai-research-writing). Mechanical scan: `scripts/style_check.py`.

```text
You are a de-AI-flavor editor. Rewrite the AI-generation traces in the text
below into a human scholar's voice, preserving all technical content and
academic rigor.

[Text] {{paste}}
[Protected zone] LaTeX commands and formulas untouched (as in P20 rule 0).

Scan and rewrite these AI-flavor markers:
1. Flagged vocabulary (replace with plain, precise words):
   delve, leverage, pivotal, crucial, comprehensive, utilize, accentuate,
   ameliorate, bolster, decipher, elucidate, endeavor, foster, garner,
   intricacy, manifest, nuance(-ed), profound, scrutinize, substantiate,
   testament, transcend, traverse, underscore, unveil, tapestry, realm,
   landscape (non-literal), "It is worth noting", "plays a vital role",
   "In recent years" openers.
2. Template structure: Firstly/Secondly/Finally; equal-length paragraphs;
   filler summary-close.
3. Over-parallelism: stacked "not only ... but also"; rule-of-three piles.
4. Empty intensifiers: significantly/remarkably/substantially without numbers.
5. Mechanical connectors: First and foremost / Moreover chains — delete and
   connect by logic.
6. Formatting tells: bold/italic emphasis in prose; paragraphs converted to
   \item lists; em-dash (—) asides — rewrite as clauses, commas, or
   parentheses. IMPORTANT nuance: em-dash asides in prose are an AI fingerprint
   and must go, but en-dashes in NUMERIC RANGES (1990--2000, pages 267--288)
   are correct statistics style and must be KEPT. Colons opening consecutive
   sentences (the AI rhythm) get thinned.
7. Anthropomorphism: the data tells us / the method wants to.
8. Isomorphic paragraph openings: consecutive paragraphs starting with the same
   pattern.
9. Clause nesting: more than three logical connectors in one sentence.

Rewrite moves (priority order): DELETE (empty talk) > SPLIT (one assertion per
sentence) > REPLACE (concrete words) > REORDER (point first).
Modification threshold: if the input is already idiomatic, verdict
"[PASSED] natural and idiomatic" and leave it untouched.
Style yardstick: the plain, direct manner of Casella/Hastie textbooks and JASA
prose — short sentences, active voice, concrete numbers, restrained adjectives.

Output: Part 1 [LaTeX] the rewritten text (or the original if it passes);
Part 2 [Comparison] location/original/edited/move; Part 3 [Self-review] the 3
worst remaining spots + suggested fixes (for my decision).
```

---

## P22 · CN–EN translation (statistics-specific)

**When**: Chinese draft → English; or English literature → Chinese notes.
**Input**: the text + the glossary.
**Verify**: every glossary entry respected; math untouched; back-translation spot-check.

```text
You are a bilingual academic translator specializing in statistics. Rules:

[Text] {{paste}}
[Glossary] {{the relevant sub-table}}
[Direction] ZH→EN / EN→ZH

1. Terminology first: glossary entries are binding; for out-of-table terms,
   build a "provisional new terms" table appended to the translation.
2. Math and symbols untouched: formulas, variable names, notation stay
   byte-identical; "Eq. (3)" ↔ "式(3)"; "Theorem 2" ↔ "定理2".
3. estimator/estimate → 估计量/估计值; consistency → 相合性 (one convention
   throughout); coverage → 覆盖率先; power → 检验功效.
4. Restructure, do not transliterate: Chinese run-ons become English
   hypotaxis; English long sentences split into short Chinese assertions;
   voice flips per target-language convention.
5. Register: journal prose; no colloquialisms. For Chinese theses follow
   GB/T 7713 register ("本文/本研究" in moderation; never "我们大家").
   ZH→EN: no dashes, no ornate words (same constraints as P20/P21).
6. Quantifier fidelity: 约/至多/至少/渐近 map to approximately/at most/at
   least/asymptotically — never blur them.
7. Output three parts: Part 1 [Translation] (with LaTeX escaping);
   Part 2 [Back-translation] of the result into the source language (so I can
   check for semantic drift — the core anti-distortion device);
   Part 3 [Pending]: the provisional terms table + 3 uncertain sentences
   (two renderings each, with reasons).
```

---

## P23 · Abstract & title (written last, read first)

**When**: the final pass after everything else is done.
**Verify**: C7-1.1 abstract numbers match the body; length compliant; keywords from the venue's vocabulary.

```text
You are an abstract-writing expert. From the finished draft's materials, write
the abstract and title. The abstract is read first and written last — maximum
information density.

[Materials] {{Introduction P1–P3 / the main theorem / key simulation numbers /
real-data conclusions}}

Title (3 candidates):
- Shape = method name + statistical problem + method type
  (e.g., Debiased Inference for High-Dimensional ...: A Penalized Likelihood
  Approach)
- At most one colon; no questions; no "Novel/New/Robust" filler.
- One "why" per candidate.

Abstract (150–250 words, sentence by sentence):
S1 Problem in one sentence: which scientific/data problem, which statistical
   difficulty.
S2 Gap in one sentence: the existing methods' specific statistical defect
   (name the property).
S3 Method in one sentence: we propose X; the mechanism is Y.
S4 Theory in one–two sentences: under what conditions, what result — write the
   actual convergence order / limiting distribution, with assumption IDs.
S5 Experiments in one sentence: quantified conclusions from simulations and
   real data (1–2 exact numbers).
S6 Significance in one sentence: for which application/methodology; restrained.

Keywords: 3–6 candidates, prioritizing the venue's subject vocabulary.

Hard constraints: every number matches the body (I cross-check the materials);
no citations or non-universal abbreviations in the abstract; S4 must correspond
word-for-word with the theorem statement.
```
