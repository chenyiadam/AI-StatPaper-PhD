<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# JASA · Journal of the American Statistical Association

> ASA's flagship journal. This profile is a convention-based summary; before submitting, the latest Author Guidelines on the ASA website prevail.

## Positioning and preferences

**What it publishes**: two tracks —
- **Theory & Methods**: new statistical methods with substantive theoretical guarantees
  (consistency / asymptotic distributions / rates / validity of inference). Purely numerical
  tricks or methodology without theorems rarely gets in.
- **Applications & Case Studies**: contributions centered on a **new application or new data**;
  the method may be a clever combination of existing tools, but it must solve a key statistical
  problem of that application domain.

**What it does not publish**: pure simulation comparisons, incremental variants of existing
methods (a different penalty, a different kernel), methodology papers without real data
(even the T&M track expects at least one dataset demonstrating practical relevance).

## Structural conventions

- The five-paragraph Introduction (prompt [P17](../../prompts/05-论文撰写.md) in this project is
  designed around exactly this): scientific question → methodological gap → this paper's method →
  **a list of contributions (i)(ii)(iii)** → literature and structure. The contributions list is a
  JASA signature; each item must be traceable to a theorem or table number.
- Methods section: setup/notation first, then the estimator, then the algorithm; theory section =
  Assumptions → Main theorem → Remark (comparison with rates in the literature) → Proof sketch;
  **full proofs go into the appendix or a supplement** (main-text page budgets are tight).
- Discussion section: limitations + extensions + practical recommendations; referees look hard at
  whether this section is honest and concrete.
- Abstract: roughly 200 words or fewer, and it must contain at least one sentence of theoretical
  conclusion and one of quantitative experimental conclusion.

## Language and tone

- author-year citations (a Chicago-family style), with \citep and \citet used in their proper roles.
- Confident but restrained: "We propose / We establish" is fine; novel / seamlessly /
  unsupported "significantly" are banned.
- An applied register: non-statisticians must be able to read the Introduction and the Discussion
  (the readership spans disciplines).

## Presentation of theory

- Theorem density: the T&M track typically carries 2–4 main results (an estimation-error bound plus
  an asymptotic-distribution or inference theorem are standard equipment).
- Every assumption gets a Remark (how strong it is relative to the literature, whether it can be
  relaxed); rates should align with minimax lower bounds, or the gap must be explained.
- Lower-bound arguments (Le Cam / Fano) are a plus; if present, put them in an appendix and
  double-check the divergence computations.

## Expected experiments (simulations + data)

- Simulations: a scenario grid plus at least one heavy-tailed or boundary scenario; size calibration
  and coverage probability must be checked; baselines must be tuned (ASA referees have zero tolerance
  for straw-man baselines).
- Real data: at least one dataset for the T&M track; usually two or more for the Applications track,
  with a data availability statement and a replication package (ASA stresses reproducibility; a
  Zenodo / Code Ocean DOI is recommended).

## Hard formatting requirements (verification items)

- [ ] Template/style: per the official guidelines (main text usually double-spaced; page limits per the website)
- [ ] Citation style: author-year (Chicago family)
- [ ] Supplementary material: long-form proofs / extra simulations / replication package, separately compilable and parseable
- [ ] Data and code availability statement is mandatory
- [ ] Anonymity requirements: per the website (historically the JASA tracks have differed)

## Journal-specific adaptation checklist (first draft → JASA-ready)

- [ ] Recast the contributions as an (i)(ii)(iii) list, each item tied to a theorem/table number ([P03](../../prompts/01-科学问题与选题.md))
- [ ] Move all proofs out of the main text (keep only a Proof sketch), and complete the lemma chain in the appendix
- [ ] Add a Remark to every assumption (strength comparison + discussion of relaxations)
- [ ] Add tuning details for the baselines (same CV grid), with a "tuning protocol" note in the table captions
- [ ] Put the replication-package DOI and the data availability statement in place
- [ ] Expand the Discussion into "limitations → extensions → practical recommendations", with limitations mapped to doable research questions
- [ ] Run [`scripts/style_check.py`](../../scripts/style_check.py) to scrub AI-flavored symbols and wording
- [ ] Rewrite the abstract: six-sentence structure ([P23](../../prompts/05-论文撰写.md)) + under 200 words + rate and coverage numbers
