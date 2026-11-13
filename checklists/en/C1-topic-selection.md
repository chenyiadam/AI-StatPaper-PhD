<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C1 · Topic and Research-Question Checklist

> Usage: at the topic-selection/proposal stage, together with prompts [P01–P03](../../prompts/01-科学问题与选题.md)
> and [`docs/02-阶段一-科学问题凝练.md`](../../docs/02-阶段一-科学问题凝练.md).
> Passing standard: for every item you can write down a **specific** answer; if you cannot write a specific
> answer, the item is not yet passed.

## A. Depth of the research question (the PhD-level watershed)

- [ ] A1. State the core scientific question in one sentence, and the question is **not** "apply method A to data B"
- [ ] A2. There is a **statistical tension** behind the question: e.g., a gap between theoretical guarantees and
      empirical performance, high dimension vs. interpretability, the robustness–efficiency trade-off —
      you can say what the tension is
- [ ] A3. Why existing methods **cannot directly solve it**: name the specific statistical deficiency
      (consistency failing? interval coverage too low? suboptimal rate? sensitivity to distributional assumptions?)
- [ ] A4. "Why now": changing data shapes (larger p, complex dependence, heterogeneity) or newly available
      theoretical tools make the problem solvable/important
- [ ] A5. The elevator test: in 90 seconds, explain the problem, the difficulty, and your approach to a
      statistician outside your subfield; the listener can ask at least one serious question

## B. Positioning of the problem

- [ ] B1. Mark the literature map: what are the 3–5 nearest-neighbor papers, and the **delta** from each in one sentence
- [ ] B2. The gap genuinely exists: in the last 3 years no top journal/conference has published essentially the
      same result (the search has been done)
- [ ] B3. Feasibility pre-check: the theoretical toolkit exists (not inventing mathematics from scratch),
      the algorithm is writable, simulations are runnable, real data is obtainable — preliminary evidence for each
- [ ] B4. The deliverable decomposes: paper = method + theorems (≥2 meaningful results) + simulations + real data
      + an open-source package, each block with an explicit "success criterion"
- [ ] B5. Risk plan: if the main theorem only achieves a suboptimal rate / the conditions turn out somewhat
      strong, does the paper still stand (Plan B)?

## C. The contribution statement (raw material for paragraph (ii) of the Introduction)

- [ ] C1. One sentence per class of contribution: method (mechanism), theory (conditions → conclusions,
      with rates), computation/empirics
- [ ] C2. Every contribution is **pointable**: you can name the objective-function equation, theorem number,
      and table number it maps to
- [ ] C3. The contributions are ranked: the paper's strongest card goes first
- [ ] C4. The reverse test: delete one of the paper's contributions — does the paper still stand independently?
      If it fully stands, that contribution was never "this paper's"
