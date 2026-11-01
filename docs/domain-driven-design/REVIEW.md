# Reviewing a Domain-Driven Design course: the brief

You review one finished course of the read-along of Evans, *Domain-Driven
Design* (2004), for accuracy against the book and for teaching. The model is
`docs/reviews/enterprise-patterns-domain-logic-review.md` (read its first 80
lines for the shape). Read `docs/domain-driven-design/PLAN.md`,
`docs/domain-driven-design/AUTHORING.md` (it names the text and the tools) and
the parts of `docs/domain-driven-design/kit-report.md` your course's labs use.
Never read `site/`; never read the book file whole; never copy the book's text
into the review beyond the few words needed to locate a passage.

Write ONLY `docs/reviews/ddd-<course-slug-without-ddd->-review.md`. Change
nothing else; the course's author applies the fixes. Run no git command that
changes the index or working tree.

## What to check

1. **Gates.** `python3 scripts/preview_subject.py domain_driven_design --course <slug> --out <new dir under the scratchpad>/rev/<slug>` prints OK. `quotes.py` on every quotation (exact, PDF page right, ≤ 40 words opening, ≤ 60 a lesson). `overlap.py <course dir> 8`: every run is a title, a pattern or section name, or a counted quotation — list any other.
2. **Accuracy.** For every sentence that says what Evans (or Fowler, in Chapter 11) argues, recommends, warns against or describes, read the pages behind it with `book.py`/`page.py` and say whether the book supports it. Misattributions, overstatements, a pattern's intent garbled, the book's example misdescribed, a section credited to the wrong chapter: each is a MUST-FIX with the location (file:line) and replacement text.
3. **Labs.** Load each lesson in Playwright (`require('playwright')`, `chromium.launch()`, `file://` on the preview's pages), each preset; check the tiles against the prose and worked lines by your own count; type the exercise in and check it against the quiz `why`. A figure in the prose the lab does not print, or prints differently, is a MUST-FIX. Check at 375 px for sideways scroll.
4. **Teaching.** Every wrong quiz answer: try to argue for it; if you can, it is a MUST-FIX with a replacement. Is the lab's count actually connected to the pattern's argument, or is it decoration? Does each lesson close on the gap the material clause names (the count is one consequence of one choice, not a verdict)? Is the book fair-minded where Evans is (Smart UI's legitimate uses, a pattern's costs)? Any lesson using a book example domain as lab data is a MUST-FIX.
5. **Copyright.** No book code, diagram, dialogue or table reproduced; no close paraphrase of a pattern's boxed statement (8-word runs are caught by the scanner; look for 5–7-word near-runs in pattern statements too).

## Report shape

Sections: Gates; MUST-FIX (numbered, file:line, what is wrong, the book's
position with PDF page, replacement text); SHOULD-FIX; NOTE; and a one-line
verdict. Under 1,500 words. Your final message to the orchestrator: the path
of the review, counts of MUST/SHOULD/NOTE, and the three most important
findings in a sentence each.
