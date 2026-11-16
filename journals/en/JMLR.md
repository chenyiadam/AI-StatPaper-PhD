<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# JMLR · Journal of Machine Learning Research

> A flagship for machine learning theory/methods (a common destination for papers at the statistics–ML interface). This profile is a convention-based summary; before submitting, the website prevails.

## Positioning and preferences

**What it publishes**: the theory and methods of machine learning — learning theory, optimization,
the high-dimensional statistics × ML interface (high-dimensional inference, nonparametric methods,
causality + ML), and new algorithms with theoretical guarantees. For a statistical methodology paper
whose algorithmic and learning perspective is prominent, JMLR is a legitimate destination.

**What it does not publish**: pure applications / benchmark-chasing without theoretical support,
narrow-domain papers with no general methodological contribution.

## Structural conventions

- Generous length (JMLR has no strict page limit, but referees dislike redundancy); appendices may be long.
- The customary skeleton: Introduction (with a contributions list) → Related Work (usually a
  separate section and expected to be **comprehensive** — JMLR weighs related-work coverage very
  heavily) → Problem Setup → Method → Theory → Experiments → Conclusion.
- Experiments typically include standard benchmark datasets (UCI / synthetic + public data);
  computational efficiency and scalability are routine assessment items.
- Open-source code is close to an implicit requirement (the journal officially stresses reproducibility).

## Language and tone

- Citations use JMLR's own .bst (numeric! different from the statistics journals).
- The ML vocabulary: algorithmic complexity, scalability, benchmark comparisons, and ablation studies
  are standard currency; when migrating a statistics paper, align the terminology
  (e.g., run "covariates" and "features" in parallel as a bridging strategy).
- The (i)(ii)(iii) contributions list has the same structure as in statistics journals.

## Presentation of theory

- Theorem presentation resembles statistics (assumptions → theorem → proof in the appendix);
  the referee pool differs, however: ML theory referees are more at home with the vocabulary of
  concentration inequalities and generalization bounds, and classical statistical asymptotics
  (Donsker and the like) must be written more self-containedly.
- Bridge convergence rates to ML notation (excess risk, sample complexity).

## Expected experiments (simulations + data)

- Simulations + real data + **computational scalability experiments** (runtime vs. n/p curves);
  ablation studies (drop the regularizer / swap the loss) are a fixed ML-referee question.
- Baselines must include strong methods recognized by the ML community (not just the usual
  statistics-journal few).

## Hard formatting requirements (verification items)

- [ ] Template: the official JMLR LaTeX style
- [ ] Citation style: the jmlr .bst (numeric)
- [ ] Anonymity: per the website (historically JMLR has been non-blind, with author information kept — verify!)
- [ ] Supplementary material / code repository links

## Journal-specific adaptation checklist (first draft → JMLR-ready)

- [ ] Make Related Work a separate section and expand it (full coverage of the ML literature, including recent conference papers)
- [ ] A terminology bridge table: statistical notation ↔ ML notation (excess risk / sample complexity)
- [ ] Add computational scalability experiments (runtime-vs-scale curves)
- [ ] Add ablation studies (decomposing component contributions)
- [ ] Code repository + reproduction scripts (JMLR readers will run them)
- [ ] Switch citations to the jmlr .bst; align theorem environments with the template
- [ ] Add ML-baseline comparisons in Experiments
