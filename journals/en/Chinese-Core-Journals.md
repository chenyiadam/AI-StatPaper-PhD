<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Chinese Core Statistics Journals (《应用概率统计》《数理统计与管理》《统计研究》, among others)

> Covers the conventions common to the Chinese core journals in statistics. Details differ
> considerably from journal to journal; check each journal's latest instructions before submitting.
> Also serves as the stylistic base for Chinese academic theses (the GB/T 7713 series).

## Positioning and preferences (by journal)

- **《应用概率统计》 (Applied Probability and Statistics)**: probability and statistics theory and
  methods (the highest bar for theoretical content; close to an English-language methodology paper
  rendered in Chinese).
- **《数理统计与管理》 (Application of Statistics and Management)**: applications of statistical
  methods in economics/management and the social sphere; interpretability of the methods comes first.
- **《统计研究》 (Statistical Research)**: an official-statistics-system background; economic
  statistics and statistical institutional methodology in equal measure; strongly policy-connected.
- **《中国科学：数学》 (Science China Mathematics) / 《数学学报》 (Acta Mathematica Sinica)**:
  probability and statistics theory may be submitted (the mathematics category; an extremely high
  theoretical bar).

## Structural conventions (common to Chinese journals)

- A Chinese abstract (200–300 characters) + 3–5 keywords + parallel English title/abstract/keywords;
  a CLC (Chinese Library Classification) number + a document code + a first-page funding footnote.
- The Introduction contains: research background → literature review (Chinese-language literature
  must not be absent! AI searches routinely miss Chinese literature — run a supplementary search on
  CNKI) → this paper's work → the organization of the paper.
- Theorem presentation follows the Chinese conventions: "定理 1 (Theorem 1) / 引理 1 (Lemma 1) /
  假设 A (Assumption A), proofs closed with □"; proofs may go into an end-of-paper appendix.
- Conclusions and discussion form a separate section; acknowledgments and funding are kept separate.

## Language and tone (norms for Chinese statistical writing)

- Discipline shared by theses and journal submissions:
  - Narrate with "本文/本研究" (this paper/this study); "我们大家" is banned; "笔者" belongs to
    social-commentary prose.
  - Terminology follows the *Statistics Terminology* (《统计学名词》) of the China National Committee
    for Scientific and Technical Terminology; the Chinese column of this project's
    [`docs/glossary-中英术语表.md`](../../docs/glossary-中英术语表.md) is aligned with mainstream translations.
  - The distinction between estimator (估计量) and estimate (估计值) is the number-one chronic
    stumbling block in Chinese statistical writing.
  - Numerals follow GB/T 15835; punctuation is full-width; references follow GB/T 7714—2015
    (the numeric citation-order style dominates; author-year is rarely used).
- Banned AI cadence (Chinese-specific): stacked "——" parentheticals; "不仅…更是…" ("not only…but
  even…") parallelism; business jargon such as "赋能/抓手/闭环"; vacuous "综上所述" summaries; chained
  被字句 (passive constructions) — see the Chinese rules in
  [`scripts/style_check.py`](../../scripts/style_check.py).

## Expected theory and experiments

- Theory: theorem conditions and conclusions stated completely in Chinese; asymptotic results keep
  their English notation ($O_p(\cdot)$ and the like) — do not translate mathematical symbols into Chinese.
- Simulations and data: the same standards as English-language journals (the
  [C3 checklist](../../checklists/C3-实验检查清单.md) applies); figure and table captions in Chinese,
  legends may be Chinese; three-line (booktabs) tables under the same rules.

## Hard formatting requirements (verification items)

- [ ] Reference style: GB/T 7714—2015 (numeric citation-order style); in-text citations as superscript [1]
- [ ] Parallel Chinese–English abstracts, keywords, CLC number, funding footnote
- [ ] Figures/tables: Chinese captions (centered) + English parallels (per the journal's requirements)
- [ ] Fonts, type sizes, and layout per each journal's template (most provide Word templates)

## Journal-specific adaptation checklist (first draft → Chinese-core-ready)

- [ ] English manuscript → Chinese manuscript: follow the [P22](../../prompts/05-论文撰写.md)
      translation discipline (glossary mandatory + back-translation check)
- [ ] Convert the references to GB/T 7714 numeric style (re-arrange all author-year entries)
- [ ] Supplementary search for, and citation of, Chinese literature (search CNKI; AI-built reference
      pools usually lack Chinese sources — Chinese referees invariably raise this)
- [ ] Rewrite the abstract to the Chinese norm (four elements: objective–method–results–conclusion,
      200–300 characters)
- [ ] Unify terminology per *Statistics Terminology* + the project glossary
- [ ] Clean up "的"-chains / translationese / 被字句 ([C4](../../checklists/C4-写作语言检查清单.md)
      Group C + the Chinese rules in style_check)
- [ ] Funding footnote, CLC number, and author-bio formats per the target journal's template
