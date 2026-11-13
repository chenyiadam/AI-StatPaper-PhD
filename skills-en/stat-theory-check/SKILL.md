---
name: stat-theory-check
description: Theory checking for statistics papers. use when the user wants to review theorems and proofs, check assumptions (regularity conditions), design the theorem landscape, draft proof skeletons, construct counterexamples, or verify rate/assumption consistency — i.e., stage S3, plus re-checks when mock referees find theory issues.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-citation-verify, stat-simulation-audit]
---

# stat-theory-check · Theory & proof review

## Hard disciplines

1. **The ideas are the author's**: decomposition strategy, key inequalities,
   assumption choices. AI drafts technical details, checks consistency, and
   attacks proofs.
2. **AI-generated proofs default to skipped steps and phantom citations**:
   the line-by-line attack (Mode B) is mandatory.
3. **"Obviously" is banned**: expand it or replace it with a lemma reference.
4. **AI saying "the proof holds" ≠ holds**: the deliverable is a suspect list
   + fixes; the author adjudicates correctness.

## Three working modes

### Mode A · Theorem landscape design (new theory)
1. Run **P08** (`prompts/en/03`): main-theorem draft → lemma list (dependency
   DAG, status, risk) → rate positioning → assumption–use-site self-check.
2. Run **P11** on every assumption (precision / standardness / strength /
   verifiability / use site).
3. Output the DAG (acyclic) + a remark draft per assumption.

### Mode B · Line-by-line proof attack (the default)
1. The author supplies the proof + **the allowed lemma list** (anything else is
   uncitable).
2. Run **P10**: six scan classes — Q1 phantom citations / Q2 skipped steps /
   Q3 convergence-mode mixing / Q4 dimensions & constants / Q5 event
   completeness (good event + P(E^c) both present) / Q6 undeclared conditions.
3. **Dual-model cross-examination**: two different models attack the same
   proof independently; union the findings; adjudicate each by hand (AI also
   false-positives on correct steps).
4. Walk `checklists/en/C2-theory-check.md` group C (C1–C14) by hand.

### Mode C · Counterexample construction (can assumptions weaken?)
1. Run **P12**: explicit construction (DGP definition → item-by-item
   verification of the weakened assumptions → proof the conclusion fails →
   which proof step it breaks).
2. Recompute every "satisfies the assumption" step yourself — AI counterexamples
   often fail their own conditions.
3. Holds → add "the condition cannot be dropped" to the Remark with the example
   in the appendix (a plus, not an embarrassment). Fails → relax via Mode A.

## High-frequency defect quick table (where AI-generated proofs fail)

| Defect | Check |
|---|---|
| Citing a lemma that never existed (e.g., Lemma 3.2) | reconcile every ID against the allowed list |
| Illegal $O_p/o_p$ algebra | re-derive each stochastic-order step |
| in-probability vs. a.s. mixing | tag each limit's mode and verify |
| Only the good event bounded; P(E^c) missing | grep "on the event"; confirm the complement |
| Swapping limits with sums/integrals/expectations | demand a domination condition (DCT/MCT/uniform) |
| Treating p as constant when p = p(n) | check dimension conditions and rank arguments |
| Citing a reference theorem whose conditions are stronger | pull the original and compare (links to citation verification) |
| λ order mismatched with the objective's penalty normalization | compare against Eq. (1)'s 1/n factor |

## Cross-checks

- Notation: run `scripts/notation_check.py` (duplicate macros, dangling refs,
  uncited theorems, "obviously" scan, TODO residue).
- Theory–simulation consistency (λ order, sparsity, DGP): stat-simulation-audit.
- Every literature theorem cited in a proof goes through stat-citation-verify L3
  (does the original actually contain it, under these conditions?).

## Output format

```
Verdict: holds (minor fixes) / substantive holes / route infeasible
Issue list: Q# | location | class | reason | suggested fix | severity
Assumption–use table: Assumption k → used in Step j ✓/redundant/unused
Items for author adjudication: every point AI was unsure about
```

## Related files

`prompts/en/03` (P08–P12) · `checklists/en/C2-theory-check.md` ·
`docs/04` (Chinese) · `docs/11-阶段八-投稿执行与出版跟进.md` §8.6
**venue-calibrated theory-check intensity table** (set the P10 intensity per
target venue: L3 line-by-line for AoS/Biometrika, L2 guarantee-level for
JASA/JRSS-B, L1 reasonable-level for the rest) · `scripts/notation_check.py`
