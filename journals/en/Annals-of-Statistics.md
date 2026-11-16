<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Annals of Statistics (AoS)

> The IMS flagship and the discipline's highest temple of statistical theory. This profile is a convention-based summary; before submitting, the latest IMS/Euclid instructions prevail.

## Positioning and preferences

**What it publishes**: core advances in statistical theory — asymptotics, minimax optimality,
empirical processes, high-dimensional theory, random matrices, Bayesian asymptotics,
semiparametric/nonparametric theory — and methodology with **sufficient theoretical depth**
(the method must raise new theoretical questions or require new techniques).

**What it does not publish**: application-driven work, methodology papers with simulations but no
theory, and results that combine known techniques without a genuinely new inequality or a new proof
technique. The first question an AoS referee asks is always: "**What is the new theoretical
contribution? Which lemma is new? Which proof technique?**"

## Structural conventions

- The structure is relatively free but dense: the Introduction is often tighter (no JASA-style
  five-paragraph build-up needed); the point is to get to the mathematics quickly.
- The theorem system is the protagonist: the main text runs Assumptions → Theorem → Discussion;
  **proofs may stay in the main text** (AoS has traditionally been happy to print proofs in the
  paper), with overlong proofs moved to the appendix.
- A notation section is indispensable and must be strictly self-consistent; a global notation
  table is good practice.
- The abstract is short (on the order of 100–150 words) and states results directly (rates included).

## Language and tone

- author-year citations; a leaning toward British spelling (behaviour/analyse) — uniform throughout
  is what matters.
- A declarative register: "The estimator is shown to attain…"; less of the "we" narrative voice.
- Overclaiming is the cardinal sin: AoS referees are extremely sensitive to "first/novel/optimal" —
  claiming optimality requires a lower-bound proof or a precise positioning against the literature.

## Presentation of theory

- Theorem density: 2–5 main theorems, with the auxiliary lemma chain fully exposed in public
  (auxiliary lemmas are half the value of the paper).
- The optimality vocabulary: if the rate matches a known lower bound, say minimax optimal explicitly
  and cite the lower-bound literature; if it does not, quantify the gap and explain which step it
  comes from.
- The "irremovability" of assumptions is argued by counterexample (the output of
  [P12](../../prompts/03-理论推导与检查.md) in this project is hard currency here).
- Self-audit of proof techniques: if a core inequality is borrowed from the literature, verify its
  conditions item by item ([C2–C14](../../checklists/C2-理论检查清单.md)); AoS referees really do
  re-derive line by line.

## Expected experiments (simulations + data)

- Simulations are usually lightweight: 1–2 tables verifying that finite-sample performance is
  consistent with the order of the theoretical rate suffice; the emphasis is on a log-log plot whose
  slope shows the rate (rate verification) rather than an exhaustive scenario grid.
- Real data is not required (a plus if present); replication packages are encouraged.

## Hard formatting requirements (verification items)

- [ ] Template: the official IMS `imsart` family (imsart-aos); LaTeX strictly per the template
- [ ] Citation style: author-year; theorem environments as defined by the template
- [ ] Length: per the website (AoS has no strict page limit, but the editorial office will ask for concision)
- [ ] Supplementary material: uploaded to the Euclid platform; make the relationship between the appendix and the main line explicit

## Journal-specific adaptation checklist (first draft → AoS-ready)

- [ ] Compress the Introduction: one paragraph for the scientific question; the weight goes on "theoretical contribution and new proof techniques"
- [ ] Promote proofs into the main text, or partially so (the opposite of JASA!), keeping only the overlong parts in the appendix
- [ ] Add minimax positioning: alignment with known lower bounds or a quantified gap, written as a standalone Remark
- [ ] Make the lemma chain self-contained: verify conditions for every cited external theorem and rewrite it in the paper's notation (C2–C14)
- [ ] Convert the rate-verification simulation into a log-log slope plot
- [ ] Delete every "optimal/novel" without lower-bound support
- [ ] Give the notation table its own section; [`scripts/notation_check.py`](../../scripts/notation_check.py) runs with zero warnings
- [ ] Unify British spelling (behaviour and the like) consistently throughout
