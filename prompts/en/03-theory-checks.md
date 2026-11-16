<!-- Translated from the Chinese canonical version (prompts/03-理论推导与检查.md). -->
# 03 · Theory derivation & checks (P08–P12)

> Companions: `checklists/en/C2-theory-check.md` · `skills-en/stat-theory-check/SKILL.md`.
> This project's stance on AI and theory:
> 1. AI is a **proof auditor** and a **technique locator**, not a **theorem inventor**. The core ideas — the decomposition strategy, the key inequality, the choice of assumptions — come from the author, who owns them.
> 2. AI-generated proofs **default to containing skipped steps and phantom citations**. Line-by-line review (P10) is mandatory, not optional.
> 3. The reliable loop: author hand-drafts the skeleton → AI fills technical details → AI attacks line by line → human adjudicates.

---

## P08 · Design the theorem landscape

**When**: after the method is fixed, before attempting any proof. Turns "I think I can show something" into a full theorem–lemma dependency map.
**Input**: the objective function, candidate assumptions, the desired conclusion shape.
**Verify**: C2-B4 the dependency DAG has no cycles; C2-D1 the theorem's object is exactly the objective function.

```text
You are an expert in statistical asymptotic theory. From my method draft, design
the paper's theorem landscape. Plan WHAT to prove, in what order, and where the
technical bottleneck is. Do not prove anything for me.

[Method draft] {{objective function + algorithm in one sentence}}
[Candidate assumptions] {{e.g., sub-Gaussian design, sparsity s, smoothness of loss}}
[Desired conclusions] {{e.g., probability bound on the estimation error;
sqrt(n)-asymptotic normality supporting inference}}

Output:
1. Main theorem draft (Theorem 1), stated per convention:
   "Assume [each]. If [order of λ], then [with probability ≥ 1-δ / in distribution],
   [conclusion with rate]." Every quantity defined; Big-O with all parameters.
2. Required intermediate results (lemmas/propositions), each annotated with:
   - content in one sentence
   - dependencies (which lemmas/assumptions it needs)
   - status: [textbook (where to look) | borrowable from literature (adjust
     conditions) | must prove (difficulty)]
   - risk: where it is most likely to get stuck
3. The dependency DAG (textual): Lemma A → Lemma B → Theorem 1 → Corollary 1…
4. Rate positioning: if my rate is X, what is known about lower bounds
   (state that this is your field knowledge and I must verify it [TO VERIFY]).
5. Assumption–conclusion matching check: for each assumption, "which proof step
   uses it?" Any assumption without a use site is flagged as suspect or removed.

Constraint: if my desired conclusion is out of reach with current techniques,
say so explicitly and propose an attainable alternative conclusion shape.
```

---

## P09 · Draft the proof skeleton (author-led)

**When**: after P08, per theorem.
**Input**: the theorem statement + lemma list from P08 + your proof-route intuition (even if rough).
**Verify**: AI introduces undeclared assumptions and phantom lemmas — every "by Lemma/by [Ref]" goes to C2-B1/C14.

```text
You are a proof-drafting assistant. I give you the theorem statement, the lemma
list, and my route intuition. Draft the proof along MY route; do not invent a
different route. If you believe the route fails, stop and say why, and wait for
my confirmation.

[Theorem statement] {{paste from P08}}
[Available lemmas] {{each: Lemma A.1 content ... (ONLY these IDs may be cited)}}
[My route intuition] {{e.g., basic inequality decomposition; split L1 error into
estimation + approximation; control the penalty term via KKT conditions}}

Drafting rules:
1. Stepwise: Step 1/2/3... each step one assertion; assertions must be complete
   and readable.
2. Every citation of a lemma/reference/previous step writes its ID explicitly.
   Anything outside the lemma list is forbidden — if a new lemma is needed,
   output "⚠ NEW LEMMA NEEDED: content draft" instead.
3. Every inequality states its direction and its justification (triangle /
   Minkowski / Hölder / ...). "Obviously" is banned.
4. For probability bounds: keep the two parts separate — the bound ON event E,
   and the control of P(E^c). Both, every time.
5. Number constants C1, C2, ... increasing throughout; no reuse.
6. End with □ and a "skipped-steps list": places you have not fully expanded
   (I will decide to expand or promote to a lemma).
7. Output in LaTeX (inside an amsthm proof environment).
```

---

## P10 · Line-by-line proof attack (AI as hostile referee)

**When**: mandatory after every proof draft; the automated layer of checklist C2.
**Input**: the full proof + the list of lemmas it is allowed to cite (in full).
**Verify**: AI review findings also need adjudication — AI produces both false negatives and false positives.
**Working mode**: run the same proof through two different models independently; union the findings; adjudicate by hand.

```text
You are a notoriously harsh statistics theory referee (Referee #2 persona).
Your only task: attack the proof below. You do not admire it, you do not polish
it; you find holes.

[Allowed materials] {{full lemma list / references; anything else is uncitable}}
[Proof under attack] {{paste}}

Scan line by line across six classes; output a numbered issue list
(each: location / class / concrete reason / suggested fix / severity H-M-L):

[Q1 Phantom citations] For every "by Lemma X / by [Ref]" — is it in the allowed
  list? Are its conditions actually satisfied here? (Check every single one.)
[Q2 Skipped steps] Any "obviously / clearly / it follows", or implicit unproven
  assertions; inequality directions, constant absorption, order-of-summation
  swaps without justification.
[Q3 Convergence modes] Is O_p/o_p algebra legal (O_p(a)O_p(b)=O_p(ab);
  o_p+o_p=o_p; probability limits vs. expectations not swapped); are
  in-probability / a.s. / L^q kept separate and used correctly.
[Q4 Dimensions & constants] When p depends on n, is p treated as constant
  anywhere; is C consistent; how does δ enter.
[Q5 Event completeness] Do BOTH parts exist — the bound on the good event AND
  the control of P(E^c)? (Half a proof is the classic defect.)
[Q6 Condition–conclusion match] Is every assumption in the statement actually
  used; is any condition used that the statement does not declare (the most
  serious offense).

End with an overall verdict: holds (minor fixes) / substantive holes (list) /
route infeasible. When unsure, say unsure. Never pass a step to look good.
```

---

## P11 · Assumption review (strength & verifiability)

**When**: before freezing the assumptions section; before answering "assumptions too strong".
**Input**: all assumptions in LaTeX + the theorem conclusions.
**Verify**: C2-A items; especially A5 dimension conditions consistent everywhere and A2 having strength-comparison remarks.

```text
You are an asymptotic-theory expert. Review my paper's assumptions row by row
with a five-dimension table (one row per assumption):

[Assumptions] {{paste each}}
[Theorem conclusions] {{paste}}

Five dimensions:
1. Semantic precision: is the statement mathematically unambiguous (quantifiers,
   uniformity, constant dependencies)? If ambiguous, propose a LaTeX rewrite.
2. Standardness: is this a standard assumption in the area? If standard, give
   the common form and where it appears [I will verify]; if non-standard, why
   it is needed.
3. Strength: weaker/stronger/incomparable vs. nearest-neighbor papers? List
   relaxation directions (e.g., elementwise condition → row-norm condition).
4. Verifiability: can a practitioner check it on real data? Give a test idea,
   or state "unverifiable; a belief-type assumption".
5. Use site: which proof step uses it (flag "possibly redundant" if neither of
   us can name one).

Then output:
- assumptions to DELETE (redundant)
- assumptions to RELAX (concrete weaker rewrite)
- assumptions needing a Remark (draft the remark)
- dimension-condition consistency: s log p = o(n)-type conditions consistent
  across text/appendix/simulation parameters (when I provide the sim settings).
```

---

## P12 · Counterexample construction (attack your own theorem)

**When**: after freezing assumptions (to show they cannot be weakened); during referee responses.
**Input**: the candidate weakened condition; the theorem statement.
**Verify**: verify the counterexample by hand — AI counterexamples often fail the very conditions they claim to satisfy (double hallucination).

```text
You are an expert at building counterexamples. Task: decide whether the proposed
"assumption weakening" is feasible — i.e., construct an explicit example
satisfying the weakened conditions where the theorem's conclusion fails.

[Theorem statement] {{paste}}
[Candidate weakening] {{e.g., elementwise sub-Gaussian → only second moments}}

Tasks:
1. If constructible, give the full construction:
   - explicit definition of the distribution/sequence (all parameters)
   - verify item by item that the example satisfies ALL weakened assumptions
     (this part must be complete; no skipping)
   - prove the theorem's conclusion fails on it (compute the contradicting
     quantity)
   - the intuition: which key inequality in the original proof it breaks
2. If not constructible: give your reasons (which structural properties the
   weak conditions still guarantee), and state whether this is your judgment or
   a citable general theorem [TO VERIFY].
3. Either way, state the writing consequence:
   - counterexample holds → add "the condition cannot be dropped" to the
     assumption's Remark and include the example in the appendix (a plus, not
     an embarrassment)
   - counterexample fails → the assumption can be relaxed; return to P11.

Warning: your counterexample error rate is nontrivial. I will recompute every
"verification" step; any hand-waving voids the whole example.
```
