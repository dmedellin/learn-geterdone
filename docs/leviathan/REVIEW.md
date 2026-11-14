# Reviewing a Leviathan course: the brief

You review one finished course of the read-along of Thomas Hobbes,
*Leviathan* (1651), for accuracy against the text and for teaching. The model
is `docs/reviews/enterprise-patterns-domain-logic-review.md` (read its first 80
lines for the shape). Read `docs/leviathan/PLAN.md`,
`docs/leviathan/AUTHORING.md` (it names the text and the tools) and the parts
of `docs/leviathan/kit-report.md` (or, for `argkit`/`choicekit`, the
Philosophy PLAN §D entries) your course's labs use. Never read `site/`; never
read the text file whole.

Write ONLY `docs/reviews/leviathan-<course-slug-without-leviathan->-review.md`.
Change nothing else; the course's author applies the fixes. Run no git command
that changes the index or working tree.

## What to check

1. **Gates.** `python3 scripts/preview_subject.py leviathan --course <slug> --out /tmp/claude-0/-home-claude/38cc3589-e9c2-59a8-8621-efe796c7d5fc/scratchpad/rev/<slug>` prints OK. `quotes.py` on every quotation, opening and inline (every `&ldquo;…&rdquo;` span): exact as printed (check LOOSE/NEAR results on the page image with `page.py N --png`), the PDF page in the source comment right, at most 120 words.
2. **Accuracy.** For every sentence that says what Hobbes argues, defines, concludes, lists or counts — every "Hobbes says", every list ("seven causes", "twelve rights", "three causes of quarrel"), every definition and every historical claim (dates, people, controversies) — read the pages behind it and say whether the text supports it. A claim the chapter does not make, a definition misstated, a list miscounted, an argument given to the wrong chapter, a critic's position misstated: each is a MUST-FIX with the location (file:line) and replacement text. Nothing may be taken from Tuck's introduction or notes.
3. **Labs.** Load each lesson in Playwright (`require('playwright')`, `chromium.launch()`, `file://` on the preview's pages), each preset; check the tiles against the prose and worked lines by your own computation; type the exercise in and check it against the quiz `why`. A figure in the prose the lab does not print, or prints differently, is a MUST-FIX. Check at 375 px for sideways scroll.
4. **Teaching.** Every wrong quiz answer: try to argue for it; if you can, it is a MUST-FIX with a replacement. Is the lab's computation actually connected to the chapter's argument, or is it decoration? Does each lesson close on the gap the material clause names (what follows on Hobbes's definitions, not whether they are true)? Is Hobbes presented at strength and his critics at strength (PLAN §F)? For Parts III and IV: fair, neither mocking nor preaching.
5. **Voice.** PLAN §F and Capital §F: reads the passage, then goes through it; history with people in it; "you"; no slang, no "let's dive in", no performed friendliness.

## Report shape

Sections: Gates; MUST-FIX (numbered, file:line, what is wrong, the text's
position with PDF page, replacement text); SHOULD-FIX; NOTE; and a one-line
verdict. Under 1,500 words. Your final message: the path of the review,
counts of MUST/SHOULD/NOTE, and the three most important findings in a
sentence each.
