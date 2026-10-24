# Second review of a Capital course: the brief

Every course of the Capital Subject gets two reviews: a pedagogy assessment
(`docs/pedagogy/capital-<course-slug>.md`) and this second, independent read
(`docs/reviews/capital-<course-slug>-second-review.md`). The Course 1 second
review found no arithmetic errors but seven places where the course misstated
what Marx argues, all in passages the pedagogy assessment had praised. That is
what this review is for.

## Do not anchor

Do not read the course's pedagogy assessment until you have written your own
findings. Then read it and record where you disagree.

## Read first

`AGENTS.md` §0, §7, §8 (never read `site/`), `content/AGENTS.md`,
`docs/capital/PLAN.md` (§0, §B, the course's §C entries, §E, §F, §G),
`docs/capital/AUTHORING.md`, and the kit report for the course's modes
(`docs/capital/kit-a-report.md` for Volume I, `kit-b-report.md` for II and III).

## What to look for

1. **Misrepresentation of Marx.** Every sentence that says what Marx argues,
   replies, concludes or means must have a line in the chapter that supports
   it. A footnote aimed at one writer is not a verdict on another. A reply to a
   critic must be Marx's reply, not a computation the critic would accept. A
   step skipped that makes the argument look weaker or stronger than it is.
   Use the Kerr text at `/mnt/project-files/capital-texts/volume-{1,2,3}-kerr.txt`
   (read-only).
2. **Critics and historians.** Named people, dates and positions accurate, and
   stated at strength. Marx presented, not endorsed: flag the lesson's own
   verdicts ("one of the best passages", "a sign worth remembering").
3. **Quotations.** Run
   `python3 /tmp/claude-0/-home-claude/52c4c1c4-2505-5c40-a28f-55e7509d8718/scratchpad/tools/strict_quotes.py <course-package> <volume>`
   from the repo (do not edit it). Fix real misses; list convention-only ones
   (drop capitals, nested quote marks, page-break splits).
4. **Arithmetic.** Recompute every figure in prose, worked lines, quiz answers
   and `why`s exactly. Render with
   `python3 scripts/preview_subject.py capital --course <course-slug> --out <dir>`
   into a folder of your own under
   `/tmp/claude-0/-home-claude/52c4c1c4-2505-5c40-a28f-55e7509d8718/scratchpad/`,
   and read every preset's tiles with `node scripts/labcheck.js --observe <page>`.
5. **Quiz.** Exactly one defensible answer per question; argue for every
   distractor.
6. **Voice** against §F: natural, warm, line by line; flag anything performed
   or preachy.

## Rules

Fix what you are confident of in the course's own files (and its §C entries
where they must agree), keeping the preview at OK. Leave taste as
recommendations. Do not touch other courses, `scripts/`, `tests/` or the kit.
Never run git commands that change the index or working tree; other agents
share this checkout. Do not commit. If the package fails to import because
another course is mid-edit, wait and retry.

Write the findings file (each finding with lesson, what was wrong, what you
changed or recommend; then where you disagree with the pedagogy assessment)
and report a short summary with the final preview output line.
