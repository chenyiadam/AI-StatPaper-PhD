<!-- Translated from the Chinese canonical version (prompts/04-实验设计与审计.md). -->
# 04 · Experiment design & audit (P13–P16)

> Companions: `checklists/en/C3-experiments.md` · `templates/simulation/` (R/Python skeletons) · `skills-en/stat-simulation-audit`.
> Borrowed principle (Polaris experiment engine): **deterministic code does the grunt work; LLM only judges** — scripts run experiments; AI designs grids, audits code, interprets results. Every number in the paper traces to an experiment output cell.

---

## P13 · Design the simulation study (scenario grid + metrics)

**When**: after theory, before writing simulation code.
**Input**: the theorem (assumptions + conclusion — the simulation "acts out the theorem") + candidate baselines.
**Verify**: all of C3-A; especially A4 (fair baselines) and A7 (λ consistent with theory).

```text
You are an expert in statistical simulation design. From my theorem and
candidate baselines, design a simulation study a referee cannot fault.

[Theorem statement] {{paste: assumptions, rate, order of λ}}
[Method] {{one sentence: which estimator/test}}
[Candidate baselines] {{e.g., OLS, Lasso, debiased Lasso, a Bayesian method}}
[Compute budget] {{cores, wall-clock ceiling}}

Output five parts:

1. Scenario grid table:
   Dimensions: n | p | s | signal strength | error distribution | correlation
   For each value explain WHY it is in the grid (which assumption of the theorem
   it satisfies / stress-tests / violates); include the theorem's boundary
   scenario (e.g., n just crossing the s log p condition); total combos ×
   replications × methods = total runs; trim to my budget and report the
   expected wall-clock.
2. DGP specification: pseudocode transcribable to R/Python, including:
   - construction of β0 and the signal-strength definition
   - standardization of heavy-tailed errors (same scale as the Gaussian case)
   - the seed rule per scenario (seed = base + 1000*scenario + replication)
3. Metrics table: metric | formula | why chosen | which theorem conclusion it
   exercises. Must include: estimation error (two norms), selection (TPR/FDR),
   inference (coverage of the TRUE parameter, interval length, size, power),
   compute time.
4. Baseline fairness protocol:
   - how each baseline's hyperparameters are tuned (same grid CV / same λ
     sequence) — tuning only my method is forbidden
   - the canonical implementation of each baseline (R package / Python library)
   - the straw-man self-check: for every baseline, the answer to "did you tune
     it?" must be yes.
5. Failure protocol: non-convergence/divergence is RECORDED as a failure rate
   in the table; silently dropping scenarios is forbidden.
```

---

## P14 · Audit the experiment code (before the big run)

**When**: after coding, before the production run. **Auditing code is far cheaper than auditing papers.**
**Input**: the full code + the P13 design doc + the DGP formulas.
**Verify**: the audit is triage; the deterministic smoke test (tiny n, hand-checked) is still mandatory.

```text
You are a statistical-computing auditor. Audit the following experiment code
before the production run. Find problems; do not praise the code.

[Design doc] {{P13 output}}
[Code] {{paste all}}

Audit and output a numbered list (location / problem / why it matters / fix):

1. DGP consistency: the code's data generation vs. the design doc, formula by
   formula (standardization, signal definition, correlation) — the #1 source
   of simulation bugs.
2. Seed discipline: does the seed rule match the doc; any hidden global RNG
   calls (samplers using defaults); are parallel seeds safe.
3. Statistical correctness:
   - is coverage computed against the TRUE parameter (not the estimate)
   - TPR/FDR denominators and directions; empty-selection handling
   - degrees of freedom, standardization, test-statistic formulas
   - is λ/hyperparameter consistent with the theoretical order; does CV leak.
4. Boundaries & failures: convergence failures captured and recorded (no silent
   NaN); empty active sets; degenerate behavior when n < p.
5. Reproducibility: outputs carry seed and date; environment lockable; all
   randomness via controlled RNG.
6. Performance traps: obvious vectorization, memory peaks, parallel grain
   (parallelize over scenarios, not replications sharing an RNG).

Finally: give me a "10-minute smoke test" checklist — minimal parameters
(n=50, p=10, rep=20) and the concrete steps to validate each component's output
shape and magnitude.
```

---

## P15 · Interpret the results (faithful table-to-prose)

**When**: after the run, before writing Section 5.2.
**Verify**: every number in the interpretation matches the table (run `scripts/fig_table_check.py`); interpretation must not exceed what the data support (no "causal" claims).

```text
You are a writing coach for statistics papers. Convert the results table into
the paper's "Results" prose. You may only use numbers that appear in the table —
not one number more.

[Results table] {{paste: rows = scenario × method, columns = metrics, mean (SD)}}
[Scenario design] {{the P13 grid description}}
[Theoretical expectation] {{what the theorem predicts: error decreases at
O(sqrt(s log p/n)); method X should be more stable under heavy tails...}}

Rules:
1. Structure: overall-first — paragraph 1 states the cross-scenario pattern
   (which class of methods wins where); paragraphs 2–3 discuss patterns one by
   one; final paragraph ties back to the theoretical expectation.
2. Every pattern carries exact numbers ("in the n=200, p=1000 scenario, method A
   attains RMSE 0.123, 18% lower than Lasso") copied from the table.
3. Theory check-in: does the direction agree with the theorem? Scenarios that
   DISAGREE must be reported honestly with candidate explanations (this is
   honesty, not weakness).
4. Language discipline: no "clearly/significant improvement"; relative claims
   give percentage AND absolute values; size readings give a range
   ("0.052–0.061 across scenarios").
5. Forbidden: numbers not in the table; cross-scenario averaging that hides
   heterogeneity; trend claims without numbers.
6. End with a "number–cell" reconciliation table: every number you used and its
   source cell, for my row-by-row check.
```

---

## P16 · Real-data analysis plan & writing

**When**: after simulations; before selecting and preprocessing real data.
**Input**: dataset metadata (source, n, variables) + prior analyses of this dataset in the literature.
**Verify**: all of C3-D; especially D4 (interpretation within bounds) and D1 (data availability).

```text
You are a consultant with applied-statistics and data-ethics backgrounds. Plan
my real-data analysis section.

[Dataset] {{source / sample size / variables / license}}
[My method] {{one sentence}}
[Existing analyses] {{what the field already found on this data (as I know it)}}

Output:
1. Fit assessment:
   - what this data can and cannot answer (do my method's assumptions make
     sense here?)
   - does n, p fall inside my theorem's scope; if not, how to handle it
     (honestly: "theoretical conditions cannot be verified on this data;
     results are interpreted exploratorily").
2. Preprocessing protocol (fully reproducible):
   - missing values: method choice + a sensitivity plan (at least two treatments)
   - outliers: rules fixed BEFORE looking at the data (no rule-after-plot)
   - encoding/standardization: hard-coded in the script.
3. Analysis plan: main analysis + at least one sensitivity/perturbation analysis.
4. Interpretation-bounds draft:
   - observational or experimental? what identification assumptions? the
     wording ceiling ("consistent with" < "suggests" < "shows" < "proves").
5. Writing template: data-source paragraph (with availability statement),
   Table 1 (summary statistics) spec, results-paragraph structure (descriptive
   first, inferential second), limitations (data-specific).

Ethics: does the license cover this use; identifiable information; citation
format for the dataset and its license.
```
