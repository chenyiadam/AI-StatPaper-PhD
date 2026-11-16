---
name: stat-writing
description: Drafting and polishing statistics papers. use when the user wants to draft a section (Introduction / methods / abstract), polish academic English, remove AI flavor, translate between Chinese and English, or design figures and captions — i.e., stage S5.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-format-lint]
---

# stat-writing · Writing & language

## Hard disciplines

1. **Expression only, never content**: any polish that changes mathematical
   meaning, condition range, or claim strength is a violation; when unsure, ask
   the author instead of editing.
2. **One paragraph at a time** (Manubot ai-revision practice): whole-chapter
   rewrites lose control; deliver original → edited → reason triads, accepted
   or rejected per paragraph.
3. **Mark AI output first**: wrap AI-written sentences in `\AICHECK{}` and clear
   them after verification (`scripts/notation_check.py` finds stragglers).
4. **Fixed drafting order** (Polaris): Introduction → Method → Theoretical
   results → Experimental setup → Results → Discussion → Abstract (LAST);
   Related Work may come last too.
5. Every number has provenance; every citation comes from the verified
   refs.bib pool.

## Workflow

### A. Section drafting (all prompts in `prompts/en/05`)

| Section | Prompt | Key points |
|---|---|---|
| Introduction | P17 | five paragraphs: problem → gap → method → contributions → organization; never open with "In recent years" |
| Methodology | P18 | 2.1 setup/notation → 2.2 estimator (formula + three-part reading + difference) → 2.3 algorithm; equations are part of the sentence |
| Theoretical results | P18 + stat-theory-check | assumptions → main theorem → remark → proof sketch; full proofs in the appendix |
| Figures/tables | P19 | selection table → self-contained caption template → two in-text callouts |
| Abstract & title | P23 | six-sentence structure S1–S6; title = method + problem + type; abstract numbers match the body |

### B. Language polish (rolling, per section)
1. **P20** polish: triad output + sweep list (delve/crucial/pivotal/
   comprehensive/utilize/leverage/...) + tense discipline + glossary alignment
   + the "risk list" of meaning-touching edits.
2. **P21** de-AI-flavor: template structures, flagged words, stacked parallelism,
   empty intensifiers, anthropomorphism, isomorphic openings, clause nesting;
   moves DELETE > SPLIT > REPLACE > REORDER; yardstick = Casella/Hastie plain
   directness. Symbols: prose em-dashes go; numeric-range en-dashes stay;
   `scripts/style_check.py` does the mechanical pass.
3. Chinese papers: C4 group C (translationese, 的-chains, full-width
   punctuation) + the glossary's Chinese column.

### C. Translation
Run **P22**: glossary absolute priority + math untouched + restructure-not-
transliterate + quantifier fidelity + provisional-terms table + back-translation
for drift checking.

## Quality floor (self-check per deliverable)

- [ ] C4 groups A/B walked (AI flavor, tense, terminology, difference markers)
- [ ] every claim has provenance (citation / theorem / table / flagged as claim)
- [ ] contributions map to the body (C4-D2)
- [ ] new symbols logged; `scripts/notation_check.py` passes
- [ ] glossary updates committed back (repo convention)

## Related files

`prompts/en/05` (P17–P23) · `checklists/en/C4-writing-language.md` ·
`checklists/en/C5-format-figures.md` · `docs/glossary-中英术语表.md` (bilingual) ·
`docs/06` (Chinese) · `templates/latex/main.tex`
