<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C4 · Academic Language and Style Checklist

> Usage: after the first draft is done, go through it section by section. With
> [`skills/stat-writing/SKILL.md`](../../skills/stat-writing/SKILL.md) and
> prompts [P20–P22](../../prompts/05-论文撰写.md).
> Principle: AI polishing touches expression only, never mathematical content; every polishing diff is
> confirmed by a human.

## A. De-AI-flavor (the high-frequency tells of AI-generated drafts; remove them item by item)

- [ ] A1. Banned words replaced: delve, crucial, pivotal, comprehensive, utilize, leverage,
      stacked moreover, "It is worth noting that", "plays a vital role", opening with "In recent years"
- [ ] A2. Break the three-beat template cadence: no "Firstly/Secondly/Finally" filler feel;
      paragraphs are joined by logic, not by formula words
- [ ] A3. Delete vacuous summary sentences ("In conclusion, our method is effective and promising")
- [ ] A4. Each paragraph has one and only one point; the opening sentence states the point rather than
      recapping background
- [ ] A5. Unstack piled-up nominalizations ("the implementation of the utilization of…" → direct verbs)
- [ ] A6. Rewrite AI's repetitive sentence patterns (consecutive paragraphs of the same shape:
      "This method… This approach… This framework…")
- [ ] A7. Calibrate the register: no inflation (novel/first used sparingly, and only when provable),
      no self-diminishment (we merely/only)
- [ ] A8. **Symbol-level AI flavor** (run [`scripts/style_check.py`](../../scripts/style_check.py),
      rules R1–R10): remove em-dash asides in the body text (— / ---) (recast as clauses/commas/parentheses);
      remove spaced " -- "; **keep en-dashes in numeric ranges (1990--2000, page ranges)** —
      that is standard usage, not AI flavor; at most one Chinese "——" per paragraph; thin out colon-led
      sentences; cut Moreover/Furthermore when they reach ≥3 occurrences per file; dismantle
      "not only…but also"

## B. Language norms for statistics papers

- [ ] B1. Tense: methods and conclusions in the present tense; the execution of experiments in the past
      tense; the reading of figures and tables in the present tense
- [ ] B2. The use of "we": active voice allowed (We propose), but assumption statements use the
      imperative/passive (Assume that… / Suppose that…), keeping "We assume" out of theorems
- [ ] B3. The delta sentence: after each piece of related work, immediately "whereas/in contrast our
      method…" — parallel piling of citations is not allowed
- [ ] B4. Terminology uniform throughout: one concept, one word (do not mix estimator/estimate;
      high-dimensional / high dimension consistent throughout)
- [ ] B5. Abbreviations expanded at first occurrence, abbreviated ever after; counted independently
      in the abstract
- [ ] B6. Numbers and units per convention; p-value format uniform (p = 0.032; p < 0.001, never p = 0.000)
- [ ] B7. A uniform citation phrasing for figures and tables (Figure 1 shows… / As shown in Table 2…),
      no mixing in the abbreviation "Fig."

## C. Chinese academic writing (for Chinese papers/theses)

- [ ] C1. Remove translationese: "被进行", "进行…的研究", "基于…的基础上"
- [ ] C2. Standard statistical translations (see
      [`docs/glossary-中英术语表.md`](../../docs/glossary-中英术语表.md)): consistently distinguish
      估计量/估计值 for estimator/estimate; "显著" (significant) only for statistical significance; etc.
- [ ] C3. Split long sentences: one assertion per sentence; "的"-chains no deeper than 3 levels
- [ ] C4. Full-width punctuation in Chinese papers; a uniform rule for spacing around English terms,
      applied throughout

## D. Logic and argument

- [ ] D1. Every claim either carries a citation, or a proof/experiment, or is explicitly flagged as a conjecture
- [ ] D2. Every contribution in the Introduction has a corresponding section in the body, in the same order
- [ ] D3. The paragraph chain is complete: Motivation → Gap → Method → Theory → Evidence → Implication
      closes the loop at the level of the whole paper
- [ ] D4. Every limitation in the Discussion is honest and concrete, without overturning the paper's core claim
- [ ] D5. Have AI do a "structure-only" retelling ([P27](../../prompts/06-审稿与投稿.md)); if the logic chain
      AI retells does not match your intent, the prose is ambiguous
