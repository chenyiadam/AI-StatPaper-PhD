<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# JRSS-B · Journal of the Royal Statistical Society Series B

> The methodology journal of the Royal Statistical Society (published by Oxford University Press). This profile is a convention-based summary; before submitting, the website prevails.

## Positioning and preferences

**What it publishes**: major advances in statistical methodology that **must be supported by
substantive applications** — this is Series B's signature requirement: a methodology paper must
show the method changing the answer to a real problem. Theoretical depth ranks below AoS and above
AOAS; novelty and generalizability carry heavy weight.

**What it does not publish**: pure theory (send it to AoS/Bernoulli), pure application cases
(send them to Series C/AOAS), methodology papers without real data.

## Structural conventions

- The Introduction emphasizes the **narrative of the applied story**: start from a real problem,
  with a vivid picture of it (Series B likes "data with their own story").
- Presentation of the contributions sits between JASA and Biometrika: a contributions list may be
  used but is not required.
- Method → theory (main theorem in the text, proof in the appendix) → application; the simulation
  section can be comparatively light.
- There is a historical read-paper (presentation plus discussion) tradition; ordinary submissions
  follow standard refereeing. Being selected as a discussion paper is an honor track — write so as
  to leave hooks for discussion (state open questions and extendable directions concretely).

## Language and tone

- author-year citations; British spelling (as at Biometrika, unified throughout).
- More narrative than JASA: a moderate story-telling register is allowed, but AI-flavored rhetoric
  remains banned.
- "Contribution to practice" must be concrete: state whose decisions, about what, will change as a
  result.

## Presentation of theory

- 1–3 main theorems suffice; the point is the **connection between the guarantees and the
  application**: discuss whether the theorem's conditions are plausible in the real-data setting
  (this draws more attention than rate optimality).
- Assumptions get Remarks but need not be compared against the literature item by item; Series B
  favors valid inference (intervals/tests) over point-estimation rates.

## Expected experiments (simulations + data)

- Simulations: moderate scale is enough (design discipline > scale); Group A of the
  [C3 checklist](../../checklists/C3-实验检查清单.md) is the floor.
- Real data: **at least one, and it must carry a story**; more background on the data than JASA
  expects (what the variables mean, the scientific question, existing findings); the conclusions
  must loop back to the Introduction's question.
- Replication packages strongly encouraged.

## Hard formatting requirements (verification items)

- [ ] Template: the official OUP/Society template
- [ ] Citation style: author-year; British spelling unified
- [ ] Anonymity: per the website
- [ ] Supplementary material: proofs and secondary results pushed down

## Journal-specific adaptation checklist (first draft → JRSS-B-ready)

- [ ] Rewrite the Introduction as an applied narrative: a vivid real problem + the statistical difficulty (a [P17](../../prompts/05-论文撰写.md) variant)
- [ ] Expand the real-data section: background, a variable dictionary, reconciliation against existing domain findings
- [ ] A discussion paragraph on theorem conditions vs. plausibility in the real setting (referees always ask)
- [ ] Elevate inference-type results (size/coverage of intervals and tests) to equal standing with point-estimation rates
- [ ] Unify British spelling; calibrate the narrative sentence patterns (story-telling without an AI cadence)
- [ ] Leave hooks for a possible discussion: make the open questions concrete
- [ ] Put the replication-package DOI in place
