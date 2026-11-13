<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C6 · Citation Verification Checklist (three-layer verification)

> Usage: every reference **generated with AI involvement** must pass the three-layer verification.
> This is a hard gate of research integrity.
> With [`skills/stat-citation-verify/SKILL.md`](../../skills/stat-citation-verify/SKILL.md),
> [prompt P07, citation verification](../../prompts/02-文献调研与引用.md), and
> [`scripts/citation_check.py`](../../scripts/citation_check.py).
> Background data: GPT-4o exhibits citation hallucination in 78%–90% of open-literature Q&A cases
> (OpenScholar, Nature 2026).
> **Default stance: every reference an AI supplies is treated as nonexistent until human verification passes.**

## L1 · Existence verification (does this paper actually exist)

- [ ] 1.1 Verify at a DOI resolver (doi.org) that the DOI resolves and points to that title
- [ ] 1.2 A search for the title on Google Scholar / Semantic Scholar / Crossref finds it
- [ ] 1.3 The authors really exist: the author does have other work in this direction (AI often stitches two
      real authors into one reference)
- [ ] 1.4 Volume(issue) and pages match the publisher's page verbatim; arXiv IDs well-formed (arXiv:XXXX.XXXXX)
- [ ] 1.5 Beware literature that "looks too convenient": a title that fits your argument perfectly is the
      signature of a hallucinated reference
- [ ] 1.6 Chinese-language literature double-checked on CNKI/Wanfang (AI hallucination rates for Chinese
      references are high, and nonexistent journal volume/issue numbers are common)

## L2 · Field-consistency verification (does the bib entry match the original)

- [ ] 2.1 BibTeX entries compared field by field against the publisher's official BibTeX export
      (never import AI-generated entries directly into the bibliography)
- [ ] 2.2 The author list is complete and in the correct order (whether there really are more authors behind
      "et al.")
- [ ] 2.3 Journal names (full/abbreviated) match the target journal's requirements; conference papers carry
      location and pages
- [ ] 2.4 The year is correct (online-first vs. formal publication year is a frequent AI confusion)
- [ ] 2.5 Preprints upgraded to a published version are replaced; preprints genuinely unpublished are annotated
      per the journal's rules

## L3 · Content-support verification (does the source actually support your claim)

- [ ] 3.1 Open the PDF and locate the section where your claimed conclusion lives; **secondhand citation is
      unacceptable** (citing without reading the original)
- [ ] 3.2 Your statement agrees with the direction of the original conclusion (a high-frequency AI failure:
      quoting a result that holds "under certain conditions" as if unconditional)
- [ ] 3.3 Strength matched: the original says "numerical experiments suggest" and you wrote "theoretically
      proved" — not acceptable
- [ ] 3.4 The best source is cited: if a more authoritative/earlier original source exists for the same
      conclusion, cite the original instead
- [ ] 3.5 The citation is placed correctly: method origins, theorem provenance, and data sources each cited
      where they belong (wrong theorem provenance is something referees particularly resent)
- [ ] 3.6 Self-citations reasonable: topical self-citations are fine; stacked self-citations are removed

## Wrap-up

- [ ] S1. Run [`scripts/citation_check.py`](../../scripts/citation_check.py): in-text \cite and refs.bib agree
      in both directions, no orphan entries
- [ ] S2. The "citation density" of review paragraphs is reasonable: 3–8 papers per paragraph, organized along
      the methodological thread, not a laundry list
- [ ] S3. The citation distribution across the paper is healthy: ≥ 1/3 of references from the last 3 years;
      2–4 self-relevant citations of the target journal (if genuinely relevant)
- [ ] S4. Verification records kept: verification date, verifier, and storage path of the source PDF
      (Zotero attachments + notes recommended)
