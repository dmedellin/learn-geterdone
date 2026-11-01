# Reviewing a Design Patterns course: the brief

You review one finished course of the read-along of Gamma, Helm, Johnson and
Vlissides, *Design Patterns* (1995), for accuracy against the book and for
teaching. The model is `docs/reviews/enterprise-patterns-domain-logic-review.md`
(read its first 80 lines for the shape). Read `docs/design-patterns/PLAN.md`,
`docs/design-patterns/AUTHORING.md` (it names the text and the tools) and the
parts of `docs/design-patterns/kit-report.md` (and of dddkit's or cckit's
reports) your course's labs use. Never read `site/`; never read the book file
whole; never copy the book's text into the review beyond the few words needed
to locate a passage.

Write ONLY `docs/reviews/gof-<course-slug-without-gof->-review.md`. Change
nothing else; the course's author applies the fixes. Run no git command that
changes the index or working tree.

## What to check

1. **Gates.** `python3 scripts/preview_subject.py design_patterns --course <slug> --out <new dir under the scratchpad>/rev/<slug>` prints OK. `quotes.py` on every quotation (exact, PDF page right, ≤ 40 words opening, ≤ 60 a lesson). `overlap.py <course dir> 8`: every run is a title, a pattern or section name, or a counted quotation — list any other.
2. **Accuracy.** For every sentence that says what the authors argue, recommend, warn against or describe — a pattern's intent, applicability, participants, consequences, implementation issues, known uses, related patterns — read the pages behind it with `book.py`/`page.py` and say whether the book supports it. Misattributions, overstatements, a pattern's intent garbled, a consequence invented or inverted, the book's example misdescribed, a section credited to the wrong pattern: each is a MUST-FIX with the location (file:line) and replacement text. Java sketches: does the sketch actually show the pattern's structure (the right participants, the right direction of reference), and does it compile as Java 8 in your reading?
3. **Labs.** Load each lesson in Playwright (`require('playwright')`, `chromium.launch()`, `file://` on the preview's pages), each preset; check the tiles against the prose and worked lines by your own count; type the exercise in and check it against the quiz `why`. A figure in the prose the lab does not print, or prints differently, is a MUST-FIX. Check at 375 px for sideways scroll.
4. **Teaching.** Every wrong quiz answer: try to argue for it; if you can, it is a MUST-FIX with a replacement. Is the lab's count actually connected to the pattern's consequences, or is it decoration? Does each lesson close on the gap the material clause names (the count is one consequence of applying a pattern, not a verdict on it)? Does each lesson state the pattern's liabilities beside its benefits, as the book does? Any lesson using a book example domain as lab data (PLAN §C) is a MUST-FIX.
5. **Copyright.** No book code, diagram or table reproduced; no close paraphrase of a pattern's Intent or of the Applicability bullets (8-word runs are caught by the scanner; look for 5–7-word near-runs in those too).

## Report shape

Sections: Gates; MUST-FIX (numbered, file:line, what is wrong, the book's
position with PDF page, replacement text); SHOULD-FIX; NOTE; and a one-line
verdict. Under 1,500 words. Your final message to the orchestrator: the path
of the review, counts of MUST/SHOULD/NOTE, and the three most important
findings in a sentence each.
