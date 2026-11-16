<!-- Translated from the Chinese canonical version (prompts/01-科学问题与选题.md). -->
# 01 · Research question & topic (P01–P03)

> Companion docs: `docs/02-阶段一-科学问题凝练.md` (Chinese) · checklist `checklists/en/C1-topic-selection.md`.
> This stage is the watershed between a PhD paper and a master's exercise: **the statistical depth of the question itself**.

---

## P01 · Refine the research question

**When**: before the proposal; or when you have phenomena/data but no statistical question.
**Input**: a ~200-word plain-language description (what the data look like, what you want to answer, where you are stuck).
**Verify**: test every candidate question against C1-A1~A5. AI tends to propose "applied exercises" rather than "theory-tension questions" — keep pushing.

```text
You are a PhD advisor in statistics, specializing in [your area: e.g., high-dimensional
inference / causal inference / functional data]. I will give you a plain-language
description of a research phenomenon. Your job is NOT to praise it, but to force it
into a "PhD-level statistical research question."

[My phenomenon description]
{{paste: in ~200 plain words — data shape, the question I want to answer, the
intuitive difficulty}}

Work in four steps:

Step 1 · Restate: in 3 sentences, restate the phenomenon and goal. If your
understanding disagrees with mine, ask first.

Step 2 · Deconstruct the status quo (list explicitly):
  a. What statistical model/assumptions underlie this phenomenon?
  b. What is the routine approach (name specific methods and the literature)?
  c. What is the specific statistical mechanism by which the routine approach
     fails here? Be precise about WHICH statistical property breaks:
     consistency? convergence rate? coverage? identifiability? sensitivity to
     distributional assumptions? where exactly does the curse of dimensionality
     bite?

Step 3 · Candidate research questions (give 3, each in this template):
  Question: one sentence; subject is a statistical object, predicate is a
  statistical property.
  Tension: which two statistical demands are fighting each other?
  Why now: data-shape changes / new technical tools, one sentence each.
  Failure risk: where is this most likely to die.
  Difficulty: is the theoretical toolbox ready (off-the-shelf / needs
  adaptation / needs invention)?

Step 4 · Demotion test: for each candidate, answer — if we strip it down to a
master's-level task (e.g., "apply method A to data B"), what exactly is removed?
That removed part is what makes it a PhD question.

Constraints:
- Forbid content-free phrases like "improve accuracy / enhance robustness /
  combine with deep learning".
- Every question must map to "something a theorem can state".
- If you believe my description contains no PhD question at all, say so
  directly and identify the gap.
```

---

## P02 · Map the research gap (lineage-based differencing)

**When**: after P01 selects a candidate — once before the literature search (to form hypotheses), once after (to validate).
**Input**: the P01 question statement + your collected literature (titles + years suffice).
**Verify**: without having read your papers, AI will invent "known results"; mark every literature-specific claim for C6 verification.

```text
You are a senior editor of statistical methods papers. Based on my question
statement and literature list, help me locate the research gap. Your value is
structured differencing, not reading papers for me.

[Question statement] {{paste}}
[Collected literature] {{list: author year title venue}}

Tasks:
1. Organize the literature into 2–4 methodological lineages. For each lineage:
   - one sentence of its evolution logic (from what to what; what it solved,
     what it exposed);
   - each paper's role in the lineage (seminal / improvement / survey / application).
2. For each lineage answer: what is its **implicit assumption**? Which part of
   my question statement touches that assumption?
3. Output a "gap map" table: rows = the dimensions below, columns = lineages:
   - theoretical guarantees (existence, conditions, rate)
   - computational scalability
   - dependence on distributional/design assumptions
   - inferential validity (are CIs/tests usable?)
   In each cell, state how that lineage handles it — using only information you
   are certain of; write "TO VERIFY" otherwise. Fabricating is forbidden.
4. Say which cell's gap my question statement best matches, and write the
   one-sentence difference statement vs. the nearest-neighbor paper:
   "whereas X assumes/achieves ..., our approach ...".

Note: use only my literature list and uncontroversial field knowledge. Any claim
of the form "so-and-so (2021) proved..." that is not in my list must be tagged
[TO VERIFY].
```

---

## P03 · Generate the contribution statement (raw material for Introduction (ii))

**When**: after the method and theory take shape, before writing the Introduction.
**Input**: draft objective function, main theorem statement, key simulation numbers.
**Verify**: C1-C2 — every contribution must point to an equation/theorem/table ID; run the C1-C4 reverse-deletion test.

```text
You are a scientific writing coach for statistics papers. From my materials,
draft the Introduction's contribution list.

[My method] {{one sentence + the objective function (paste LaTeX)}}
[Main theorem] {{paste the statement (with assumption numbers and conclusion)}}
[Simulation highlights] {{3–5 key numbers: e.g., X% RMSE reduction vs. baseline;
size controlled within 5%±1%; coverage Y%}}

Produce three contributions, each strictly in this structure:

(i) Method: we propose [method name] for [statistical problem]; its mechanism is
    [one sentence]; unlike [nearest-neighbor method], it [specific difference].
(ii) Theory: under Assumptions [IDs], we establish [specific result:
    probability bound / asymptotic distribution / rate], which is [matched to
    the minimax lower bound / positioned against the literature's rate]. The
    theorem enables [downstream use: confidence intervals / model selection / …].
(iii) Computation/empirics: [complexity or software package] + simulations and
    real data show [quantified conclusion with exact numbers].

Hard constraints:
- End each contribution with the corresponding artifact in parentheses:
  (Eq. (1); Thm 1; Table 2). If my materials contain no artifact for a claim,
  delete the claim — do not invent.
- Each ≤ 3 lines; concrete words (write the convergence order, the numbers);
  forbid "significantly improves / superior performance".
- Self-check at the end: for each contribution, answer "if deleted, does the
  paper still stand independently?" If yes, downgrade or merge it.
```
