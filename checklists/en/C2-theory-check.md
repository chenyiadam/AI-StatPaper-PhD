<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C2 · Theory Checklist (item-by-item review of proofs)

> Usage: when feeding theorems and proofs to AI, supply them **together with this checklist** as the review
> framework (with [`skills/stat-theory-check/SKILL.md`](../../skills/stat-theory-check/SKILL.md) and
> [prompt P10, line-by-line proof review](../../prompts/03-理论推导与检查.md)).
> Every item must be confirmed by a human as "pass / not applicable / needs fixing". An AI report of
> "pass" ≠ passed; the AI only locates the suspicious spots — correctness is adjudicated by the author.

## A. Assumptions and conditions

- [ ] A1. Every assumption is **numbered, named, and cited explicitly in the theorem** ("under
      Assumptions 1–3"); no hidden conditions
- [ ] A2. Every assumption is followed by a Remark discussing its strength: comparison with assumptions in the
      literature (weaker/stronger/equivalent) and whether it can be relaxed
- [ ] A3. The assumptions are **mutually consistent**: e.g., if both distributional and moment conditions are
      assumed, check compatibility
- [ ] A4. The assumptions are **verifiable or plausible in the setting studied** (e.g., conditions on the design
      matrix — could real data actually satisfy them?)
- [ ] A5. Dimension conditions are self-consistent: $s\log p = o(n)$ / $\log p = o(n^c)$ and the like agree
      throughout (main text + appendix + simulation parameters)
- [ ] A6. The constants $C, c, \delta$ are defined without conflicts or circular dependencies

## B. The lemma–theorem system

- [ ] B1. Every cited lemma **has actually been proved** and is numbered correctly (a high-frequency AI error:
      citing a nonexistent Lemma 3.2)
- [ ] B2. Every quantity in a theorem statement **is defined** (including $\beta_0$, $\lambda$, $s$, $C$)
- [ ] B3. Statements are self-contained: the theorem can be read on its own, without the main text
      (dropping the parameter $\delta$ inside a Big-O is a high-frequency error)
- [ ] B4. The logical dependencies among theorems form a DAG, with no circular references
- [ ] B5. A Corollary is genuinely a direct combination of the theorems, with conditions never quietly strengthened

## C. Inside the proof (high-frequency holes; the worst-hit zone of AI-generated proofs)

- [ ] C1. **Interchanging limits**: $\lim \sum \ne \sum \lim$, exchanging integrals and limits
      (the hypotheses of the dominated/monotone convergence theorem must be verified)
- [ ] C2. **Expectation and probability**: the $O_p$/$o_p$ arithmetic is correct
      ($O_p(a)\cdot O_p(b)=O_p(ab)$; $o_p+o_p=o_p$; limits in probability and expectations must not be
      swapped casually)
- [ ] C3. **Modes of convergence not conflated**: in probability / a.s. / $L^q$ aligned item by item; a
      conclusion under one mode is never applied under another
- [ ] C4. **Every "obviously / easily / it is easy to see" eliminated**: either expanded, or replaced by an
      explicit lemma reference
- [ ] C5. **Control of maxima and sums**: inequalities such as $\max_j |X_j| \le (\sum_j X_j^q)^{1/q}$ have
      the correct direction and constants
- [ ] C6. **Event decomposition**: the bound on the good event $\mathcal{E}$ and the probability control of
      $\mathcal{E}^c$ — **both parts present** (proving only one half is a high-frequency hole)
- [ ] C7. **Use of the KKT conditions**: subgradient signs correct, and the scaling of $\lambda$ matches the
      normalization of the penalty (the $1/n$ factor)
- [ ] C8. **Condition numbers and dimensions**: matrix rank and eigenvalue bounds depend on the dimensions
      correctly (e.g., when $p$ grows with $n$, $p$ is not treated as a constant)
- [ ] C9. **Measure-theoretic details**: measurability, almost surely vs. pointwise, existence of conditional
      expectations (a standing referee checkpoint for PhD theses)
- [ ] C10. **Deriving asymptotic distributions**: Delta-method conditions (differentiability, the $\sqrt{n}$
      scaling) and Slutsky's theorem used correctly
- [ ] C11. **Coverage/inference theorems**: the constructed interval is oriented correctly
      (lower bound ≤ estimate ≤ upper bound), and the coverage probability is for the true parameter,
      not the estimate
- [ ] C12. **Constant tracking**: $C_1, C_2, \ldots$ in the proof are never re-assigned; the final constants are
      finite and free of $n,p$ (or the dependence is declared)
- [ ] C13. **Direction of the bounds**: for minimax lower bounds via Fano/Le Cam, the KL-divergence computation
      and the reduction assumptions are checked
- [ ] C14. **Citation-by-citation verification**: for every "by [Ref, Theorem 2]" in the proof, pull the original
      source and check **whether its conditions are met** (AI often cites wrong numbers, or cites a theorem
      with stronger conditions)

## D. Theory ↔ method correspondence

- [ ] D1. The estimator the theorems address **is the same one** as the objective function defined in equation (1)
      (AI often writes a hybrid of different penalties)
- [ ] D2. The order of $\lambda$ in the theory (e.g., $\sqrt{\log p/n}$) **matches** the value used in the
      implementation/simulations
- [ ] D3. The sparsity assumption of the theorems matches the $s$ setting of the simulation DGP
- [ ] D4. Properties claimed in the text (e.g., the "oracle property") **really do have a corresponding theorem
      statement**
- [ ] D5. The notation table (or the first-definition spots) matches the proofs item by item
      (run [`scripts/notation_check.py`](../../scripts/notation_check.py))

## E. Presentation standards

- [ ] E1. Proof environments end with $\square$; interruptions in a proof ("leaving open") are marked explicitly
- [ ] E2. "Proof Sketch" contains only the route; full proofs sit in the appendix with a one-to-one correspondence
- [ ] E3. Math typesetting: upright operators ($\mathrm{P}, \mathrm{E}$), sets in $\mathbb{}$, vectors/matrices
      bold and consistent throughout
- [ ] E4. No "we" inside theorem statements (We assume → Assume); assumption phrasing uniform
- [ ] E5. All cross-references use \cref/\eqref, no hand-typed numbers (avoids misalignment under revision)

## F. Final sweep from the referee's seat (corresponds to prompts [P24–P25](../../prompts/06-审稿与投稿.md))

- [ ] F1. Is the rate minimax optimal? If not, is there a remark in the main text explaining the gap and its cause?
- [ ] F2. Are there **known counterexamples** violating the assumptions? (Have AI construct them on purpose:
      [P12](../../prompts/03-理论推导与检查.md))
- [ ] F3. Is the theory "spinning idle": are the theorem conditions so strong that the paper's own method fails them?
- [ ] F4. Is every assumption reflected in the simulation DGP? (Referees often ask: does Assumption 2 hold in
      the experiments?)
