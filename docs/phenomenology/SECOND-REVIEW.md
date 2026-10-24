# Second review of a Phenomenology course: the brief

Every course of the Phenomenology Subject gets two reviews: a pedagogy
assessment (`docs/pedagogy/phenomenology-<course-slug>.md`) and this second,
independent read (`docs/reviews/phenomenology-<course-slug>-second-review.md`).
In the Capital Subject the second reviews found few arithmetic errors but many
places where a course misstated what the author argues, usually in passages
the pedagogy assessment praised. That is what this review is for.

## Do not anchor

Do not read the course's pedagogy assessment until you have written your own
findings. Then read it and record where you disagree.

## Read first

`AGENTS.md` §0, §7, §8 (never read `site/`), `content/AGENTS.md`,
`docs/phenomenology/PLAN.md` (§0, §B, the course's §C entries, §E, §F, §G),
`docs/phenomenology/AUTHORING.md`, and `docs/phenomenology/kit-report.md`.

## What to look for

1. **Misrepresentation of Merleau-Ponty.** Every sentence that says what he
   argues, replies, concludes or means must have a page in Smith that supports
   it (`/tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/pop/smith.txt`, read-only, private: never copy long stretches of
   it into your findings). A view he states in order to reject it, presented
   as his. A step skipped that makes the argument look weaker or stronger.
2. **Opponents, sources and historians.** Named people (Descartes, Kant,
   Husserl, Heidegger, Sartre, Bergson, Köhler, Koffka, Wertheimer, Gelb,
   Goldstein, Stratton, Binswanger, Minkowski…), dates, cases and positions
   accurate, and stated at strength. Merleau-Ponty presented, not endorsed:
   flag the lesson's own verdicts. Clinical cases treated with respect.
3. **Quotations.** Run `python3 -I /tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/tools/phen_quotes.py <course-package>`
   from the repo (do not edit it). Fix real misses and cap overruns; list
   convention-only ones. Check by eye that each quoted sentence is in the voice
   the lesson says it is in.
4. **Arithmetic and models.** Recompute every figure in prose, worked lines,
   quiz answers and `why`s exactly, and check that each figure is attributed
   to the model that predicts it (never to perception itself). Render with
   `python3 scripts/preview_subject.py phenomenology --course <course-slug> --out <dir>`
   into a folder of your own under `/tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/`, and read every preset's tiles with
   `node scripts/labcheck.js --observe <page>`.
5. **Quiz.** Exactly one defensible answer per question; argue for every
   distractor.
6. **Voice** against §F: natural, warm, line by line; flag anything performed
   or preachy; modern asides only where §F allows.

## Rules

Fix what you are confident of in the course's own files (and its §C entries
where they must agree), keeping the preview at OK and the quotation checker at
OK. Leave taste as recommendations. Do not touch other courses, `scripts/`,
`tests/` or the kit. Never run git commands that change the index or working
tree; other agents share this checkout. Do not commit. If the package fails to
import because another course is mid-edit, wait and retry.

Write the findings file (each finding with lesson, what was wrong, what you
changed or recommend; then where you disagree with the pedagogy assessment)
and report a short summary with the final preview and checker output lines.
