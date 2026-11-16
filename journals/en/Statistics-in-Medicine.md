<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Statistics in Medicine

> A leading Wiley journal for medical-statistics applications and methodology. This profile is a convention-based summary; before submitting, the website prevails.

## Positioning and preferences

**What it publishes**: medical-statistics methodology (design, analysis, missing data, diagnostic
markers, real-world data) and **medical application research with methodological substance**;
methodology papers must include a demonstration on real medical data. The readership is medical
statisticians and clinical researchers.

**What it does not publish**: methodology unrelated to medicine, simulation papers without real
data, pure software articles (other journals exist for those).

## Structural conventions

- Many structured elements (per the website): some article types require a structured abstract, a
  **plain language summary**, patient contribution statements, and the like —
  the biggest difference from statistical-theory journals; reserve slots for these components in
  the submission package.
- The customary skeleton: Introduction (clinical problem + statistical gap) → Methods →
  Simulation → Application (a real study) → Discussion (clinical significance and limitations).
- Reporting standards are a hard item: RCT → CONSORT, observational → STROBE, diagnostic accuracy →
  STARD, prediction models → TRIPOD, systematic reviews → PRISMA; the completed checklist is
  submitted with the manuscript.

## Language and tone

- Citation style and abstract format per the website (Wiley journals differ from one another;
  verify before submitting).
- A two-audience register: method paragraphs rigorous, clinical-interpretation paragraphs plain;
  statistical terms explained in plain words at first use.
- The generic discipline of medical papers: effect sizes + confidence intervals lead (not p-values
  alone); the handling of multiplicity must be stated; subgroup analyses need a pre-specification note.

## Presentation of theory

- Theory is kept lean: core properties (unbiasedness / consistency / asymptotic normality / test
  level) suffice, with all proofs in the supplement; the main text states the theoretical points in
  under a page.
- Refereeing centers on the **medical applicability of the method**: whether the assumptions hold on
  clinical data (time-varying confounding, informative censoring, measurement error), and whether
  the missing-data mechanism is adequately discussed.

## Expected experiments (simulations + data)

- Simulations: aligned with the target study design (sample size, event rates, dropout rates at
  realistic magnitudes); sensitivity analyses are standard equipment.
- Real data: genuine clinical/epidemiological data is mandatory; name the source
  (registry / trial / cohort) and the access conditions; ethics approval number; reconcile the
  results against the clinical conclusions of the existing literature.

## Hard formatting requirements (verification items)

- [ ] Abstract type: structured / plain-language / word limit — check each against the website
- [ ] Reporting checklist + flow diagram (e.g., a CONSORT flow diagram)
- [ ] Ethics statement, registration number, data availability
- [ ] Reference style (Wiley medical journals are mostly numeric — different from statistics journals!)
- [ ] Tables/figures per medical-journal conventions (baseline Table 1 as a three-line (booktabs) table, etc.)

## Journal-specific adaptation checklist (first draft → SIM-ready)

- [ ] Verify the citation-style switch: statistics-journal author-year ↔ medical-journal numeric
      (a large migration; use the [P31](../../prompts/07-期刊风格适配.md) workflow)
- [ ] Write the plain language summary (aimed at patients/the public; jargon banned)
- [ ] Tick the reporting checklist + complete the flow diagram
- [ ] Rebuild the baseline table (Table 1) per medical convention (by group, standardized differences)
- [ ] Sieve the whole paper for p-value discipline: effect size + CI first
- [ ] Add pre-specification and adjustment notes to the multiplicity/subgroup paragraphs
- [ ] A clinical-significance Discussion paragraph (impact on guidelines/practice, stated with restraint)
