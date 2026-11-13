<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Biometrics

> The flagship of the International Biometric Society (IBS). This profile is a convention-based summary; before submitting, the website prevails.

## Positioning and preferences

**What it publishes**: statistical methods and applications driven by a biomedical context —
biostatistical methodology (must start from real biomedical problems), statistics for clinical
trials of drugs and devices, epidemiological data analysis, omics data analysis. Article types
usually include Methodology (method + application), Case Studies, Practice, and the like
(article-type names per the website).

**What it does not publish**: methodology unrelated to biomedicine, pure-method papers without real
health/biological data, minor tweaks to existing biostatistical methods.

## Structural conventions

- **Clinical/biological motivation comes first**: the Introduction speaks the language of medicine
  (disease, endpoints, decisions), and the statistical difficulty is derived from the medical need;
  both statistical and medical readers must be able to follow.
- The methods section includes **implementation details**: model specification, estimation, software
  implementation (which R packages were used, code availability) — Biometrics readers are
  practitioners, and hands-on details carry heavy weight.
- Reporting standards: for clinical trials / observational studies / prediction models, adherence to
  the corresponding reporting checklist (the CONSORT/STROBE/TRIPOD families) is a hard refereeing item.
- Section conventions: Methods → Simulation → Application → Discussion, plus Ethics and a data
  availability statement.

## Language and tone

- Mostly author-year citations (per the website); medical terminology follows field standards
  (disease names and endpoint measures use the field's standard names/original terms).
- Respect the medical register: effect sizes with CIs; standardized p-value reporting; never write
  "proves effective" — write "results support / consistent with…"; safety and ethics statements in place.

## Presentation of theory

- Methodology papers need core theorems (consistency / asymptotic normality / testing properties),
  but presented compactly: main theorem + plausibility of the conditions + proofs in the supplement.
- Refereeing often focuses on whether the **realities of medical data** — missing covariates,
  measurement error, time-varying covariates — are handled: the theoretical conditions must survive
  the question "does real data actually look like this?"

## Expected experiments (simulations + data)

- Simulations: scenarios mapped onto medical reality (dropout, covariate measurement error, number
  of events); every item of the [C3 checklist](../../checklists/C3-实验检查清单.md) plus size calibration.
- Real data: at least one genuine medical dataset; report sample size / number of events / follow-up
  time honestly; reconcile the conclusions against the existing clinical literature; ethics approval
  and informed-consent statements are mandatory.

## Hard formatting requirements (verification items)

- [ ] Template: the journal's template; whether the abstract is structured per the website
- [ ] Reporting checklist: tick per study type (CONSORT/STROBE/TRIPOD…)
- [ ] Ethics statement, clinical-trial registration number (if applicable)
- [ ] Data availability + code availability statements
- [ ] Anonymity requirements per the website

## Journal-specific adaptation checklist (first draft → Biometrics-ready)

- [ ] Re-cast the Introduction as a medical narrative: disease burden → clinical decision → statistical gap
- [ ] Check against the reporting checklist and submit it with the manuscript
- [ ] Land the implementation details: software, package versions, code repository
- [ ] Medicalize the simulation scenarios: add dropout / measurement error / sparse-event settings
- [ ] Put the ethics and data statements in place (approval number, registration number)
- [ ] A medical-terminology check sheet (endpoints, population, and effect-measure names consistent with field standards)
- [ ] Add a clinical-significance paragraph to the Discussion: whose decisions, about what, are affected
