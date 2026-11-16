<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C3 · Experiments Checklist (simulations + real data)

> Usage: run through it once at the experiment-design stage; run through it once again before submission.
> With [`skills/stat-simulation-audit/SKILL.md`](../../skills/stat-simulation-audit/SKILL.md) and
> prompts [P13–P16](../../prompts/04-实验设计与审计.md).

## A. Simulation design

- [ ] A1. **The scenario grid is listed explicitly**: n × p × signal strength × error distribution × method,
      mapped onto the rows and columns of the paper's tables — no more, no fewer
- [ ] A2. **Each DGP corresponds item by item to the formulas of Section 5.1** (write DGP-1, DGP-2… in the
      script comments; when one changes, both change in step)
- [ ] A3. The error distributions include at least one **non-Gaussian/heavy-tailed** option (to demonstrate
      robustness); if inference is done, include alternative scenarios the test was constructed against
- [ ] A4. Baseline selection is justified: at least one representative method per related paper + one naive
      baseline; the baselines' hyperparameters are tuned too (avoid "straw-man baselines" — an
      instant-reject point with referees)
- [ ] A5. Repetitions ≥ 500 (≥ 1000 recommended for inference experiments); Monte Carlo standard errors
      reported or computable
- [ ] A6. **Random seeds are fixed** and written into the output files; the seed scheme is regular
      (e.g., seed = base + 1000*scenario + replication index)
- [ ] A7. The order of λ in the theory matches the λ used in the experiments; with a data-driven choice (CV)
      as a comparison
- [ ] A8. The compute time is affordable: estimate the total runtime and write it down (rerunning everything
      after a crash is a classic cause of PhD delays)
- [ ] A9. Failure handling: when the method fails to converge in some scenarios, record the failure rate rather
      than dropping them silently (NaNs are a referee follow-up point)

## B. Evaluation metrics

- [ ] B1. Estimation: RMSE / L2 error / L1 error / relative error, at least two of them (they respond
      differently to $s$)
- [ ] B2. Model selection: TPR, FDR (or Hamming distance) — mandatory in high-dimensional settings
- [ ] B3. Inference: **coverage probability** (for the true parameter), interval length, and the empirical
      size and power of tests — size calibration (is nominal 5% actually near 5%?) is a must-check at top journals
- [ ] B4. Prediction: out-of-sample MSE computed on an **independent test set**, not training residuals
- [ ] B5. All metrics computed "in a single run" (avoids scenario drift caused by changing a metric and rerunning)

## C. Presentation

- [ ] C1. Tables follow the **three-digits rule**: only the digits needed for relative comparison; no piling up
      six decimal places
- [ ] C2. Best values in bold; the criterion for "best" stated in a table footnote (per column or across the table)
- [ ] C3. Every table/figure **has a textual reading in the main text**, and the numbers in the reading match the
      table (run [`scripts/fig_table_check.py`](../../scripts/fig_table_check.py))
- [ ] C4. Figures: axes labeled with units, complete legends, distinguishable line styles/grayscale
      (color-blind and black-and-white printing considered), captions self-contained and noting the seed
- [ ] C5. A uniform way of presenting variability (mean±SD or MC error), consistent throughout
- [ ] C6. The main text shows representative scenarios; the full results go to the appendix/supplementary
      material, with no contradiction between the two

## D. Real-data analysis

- [ ] D1. **Data availability statement**: for public data, how to obtain it plus version/hash; for restricted
      data, the access procedure
- [ ] D2. Every preprocessing step is reproducible (no hand-edited tables); missing-value handling has a
      sensitivity analysis or an explicit justification
- [ ] D3. Sample size, number of covariates, and number of events (if applicable) reported in Table 1
- [ ] D4. Interpretation **does not exceed what the data support**: no "proves causality" unless the
      identification assumptions hold and carry assumption numbers
- [ ] D5. Results compared against existing findings in the domain literature, with the differences explained
- [ ] D6. At least one real dataset; top journals often expect two (or one dataset + external corroboration)
- [ ] D7. Sensitivity analysis: at least one round of perturbation of hyperparameters/model specification
- [ ] D8. **Pre-analysis plan** (for confirmatory analyses): primary analysis /
      sensitivity analyses / exclusion rules fixed in writing BEFORE outcome
      data are seen (OSF preregistration or archived in the project charter);
      if not preregistered, state the reason per the P33 decision tree — a
      referee will ask

## E. Replication package

- [ ] E1. Directory per TIER 4.0: `data/ code/ output/ docs/`, with a README containing a one-command run line
- [ ] E2. Environment pinned: `requirements.txt` / `renv.lock` / `environment.yml`, with the R/Python versions
- [ ] E3. All figures and tables regenerated by scripts, with numbers matching the paper (the verification
      procedure is written into the README)
- [ ] E4. Code deposited on Zenodo/OSF for a DOI and cited in the paper
- [ ] E5. Sensitive-information sweep: API keys, local paths, and personal identifiers removed from code and logs
