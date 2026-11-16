<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# AOAS · Annals of Applied Statistics

> The IMS flagship for applications. This profile is a convention-based summary; before submitting, the latest IMS/Euclid instructions prevail.

## Positioning and preferences

**What it publishes**: **application-centered** statistics — statistical analyses of new data,
applied demonstrations of new methods, statistical problems arising in interdisciplinary
collaborations. The methodological innovation may be "a clever combination of existing tools",
but it must genuinely solve the applied problem. The theoretical bar is lower than at
Annals of Statistics, but the **bar for persuasive application outweighs everything**.

**What it does not publish**: methodology papers without real data, simulation studies, and
analyses whose domain content is mediocre and merely "applies standard methods" (the data, the
problem, or the insight must be new).

## Structural conventions

- **The Introduction must be readable by non-statisticians**: the scientific background takes up
  more than a third; the statistical question grows naturally out of the scientific one.
- A "statistical challenges" paragraph: explicitly list what this dataset/problem challenges
  statistics to do (this is a signature structural element of AoAS).
- A compact methods section; theoretical results (if any) presented lightly, with proofs entirely
  in the appendix; the weight sits on the data-analysis section — **the data analysis must be as
  detailed as a domain paper's**: exploratory analysis, model diagnostics, sensitivity analysis.
- The conclusions loop back to the scientific question (closing the narrative loop of statistics
  serving science).

## Language and tone

- author-year citations; written for an interdisciplinary readership: every term must be explained
  at first use.
- Strict discipline in the wording of domain conclusions (the wording-grading scheme of
  [P16](../../prompts/04-实验设计与审计.md) in this project is exactly what referees scrutinize here):
  no causal claims from observational data; "consistent with …" is the default phrasing.

## Presentation of theory

- Theory is a supporting player: 1–2 results (consistency / asymptotic normality) are enough; a
  discussion of why the conditions are plausible beats refinement of rates.
- If the method is borrowed from the literature, say so explicitly and describe the adaptations
  (AoAS sets a high bar for honesty about method genealogy).

## Expected experiments (simulations + data)

- Simulations: demonstrate the method on data shaped like yours (no need for a large grid).
- Real data: the protagonist. One deep analysis usually beats two shallow ones;
  exploratory analysis + diagnostics + sensitivity analysis is the standard trio; reconciling the
  domain conclusions against the existing literature is indispensable.

## Hard formatting requirements (verification items)

- [ ] Template: the imsart family (imsart-aoas)
- [ ] Citation style: author-year
- [ ] Figures/tables: aimed at interdisciplinary readers (figures beat tables; each figure tells one scientific story)
- [ ] Supplementary material: diagnostics and extra analyses pushed down

## Journal-specific adaptation checklist (first draft → AOAS-ready)

- [ ] Invert the Introduction's center of gravity: 1/3+ scientific background, with statistical challenges in their own paragraph
- [ ] Promote the data-analysis section to protagonist: the exploratory-analysis/model-diagnostic/sensitivity trio
- [ ] Explain all terminology (the interdisciplinary-reader test: have a student outside the area read the Intro and ask questions)
- [ ] Wording-demotion audit: sieve the whole paper for causal claims ([P16](../../prompts/04-实验设计与审计.md) wording grades)
- [ ] Slim the theory section: main results + discussion of condition plausibility; the rest pushed down
- [ ] Make each figure tell a scientific (not methodological) story, self-contained
- [ ] A closing paragraph that loops the conclusions back to the scientific question
