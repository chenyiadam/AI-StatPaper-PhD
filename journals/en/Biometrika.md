<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Biometrika

> A renowned journal of statistical methodology (published by Oxford University Press), known for concision and correctness. This profile is a convention-based summary; before submitting, the website prevails.

## Positioning and preferences

**What it publishes**: original statistical methodology that is theoretically sound and **written
with extreme concision**; also theory papers (at the probability–statistics interface) and a small
number of applications. Biometrika's brand is "every sentence carries information".

**What it does not publish**: long-winded method variants, papers dominated by simulations, applied
case studies. The referee preference can be stated as a maxim: **the same result, written on fewer
pages**.

## Structural conventions

- Short length is a hard feature: the main text is compact (over the long run, typical papers are
  far shorter than JASA), with a great deal of content pushed down: proofs → Appendix; secondary
  results → supplementary material.
- The Introduction is usually 1–1.5 pages: problem → gap → the method in one sentence → the result
  in one sentence. There is no (i)(ii)(iii) contributions-list tradition; contributions are woven
  into the prose.
- Theorems enter the main text directly, while proofs go almost entirely into the appendix; the
  theorems in the text are connected by a one-or-two-sentence "Sketch of proof".
- Section numbering is spare; no Discussion section is expected (a short closing commentary is common).

## Language and tone

- author-year citations; British spelling is the **tradition** (colour/favourable/normalise) —
  for Biometrika, unify British spelling throughout (referees notice this detail).
- Short sentences; every formula is followed by an interpretation; list environments almost never appear.
- Restraint bordering on austerity: "Sections 2 and 3 introduce the estimator and its
  asymptotics. Section 4 examines finite-sample performance."

## Presentation of theory

- Theoretical correctness is the lifeline: Biometrika refereeing is famous for line-by-line
  verification (the rigor of this project's [C2 checklist](../../checklists/C2-理论检查清单.md) is
  calibrated to this journal).
- A restrained number of assumptions: if one condition can say it, do not use three; the necessity
  of assumptions is argued by counterexample or remark.
- No minimax rhetoric, but rates must be correct and the dependence of the constants spelled out.

## Expected experiments (simulations + data)

- Simulations: 1–2 precise tables (each earning its place), with a heavy-tailed or boundary scenario
  mandatory; figures and tables must be minimal (Biometrika figures prize plain readability).
- One real dataset usually suffices; the point is to illustrate the mechanism of the method, not
  domain conclusions.

## Hard formatting requirements (verification items)

- [ ] Template: the journal's official LaTeX template (Biometrika's own style)
- [ ] Citation style: author-year; British spelling unified throughout
- [ ] Length: per the website (overlength requires an application or splitting)
- [ ] Figures/tables: legible in black and white first; self-contained captions

## Journal-specific adaptation checklist (first draft → Biometrika-ready)

- [ ] Compress the whole paper by 30–50%: fold the contributions list into the prose; dismantle all JASA-style scaffolding
- [ ] Replace spellings (the collect/colour type; a script or a global manual pass)
- [ ] Push all proofs down to the appendix, leaving only sketch sentences in the text
- [ ] Merge assumptions: review whether each can be merged or stated more weakly
- [ ] Slim the tables: keep only each table's core comparison columns; the rest goes to the supplementary material
- [ ] Make figures black-and-white and minimal (separation by line style, no gridlines, few colours)
- [ ] End with a short commentary (no large Discussion section)
- [ ] Run [`scripts/style_check.py`](../../scripts/style_check.py), and check list environments in particular (Biometrika frowns on \item)
