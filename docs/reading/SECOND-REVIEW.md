# Second review of a Reading Faster course: the brief

Every course of the Reading Faster Subject gets two reviews: a pedagogy
assessment (`docs/pedagogy/reading-<course-slug-without-prefix>.md`) and this
second, independent read
(`docs/reviews/reading-<course-slug-without-prefix>-second-review.md`). In the
earlier Subjects the second review found errors in what lessons said a source
argues, in passages the pedagogy assessment had praised. That is what this
review is for. Here the sources are research findings, so the risk is a
finding stated more strongly, more broadly or differently than the study
showed.

## Do not anchor

Do not read the course's pedagogy assessment until you have written your own
findings. Then read it and record where you disagree.

## Read first

`AGENTS.md` §0, §7, §8 (never read `site/`), `content/AGENTS.md`,
`docs/reading/PLAN.md` (§0, §B, the course's §C entries, §D.3, §F, §G, §S and
§R), `docs/reviews/reading-spec-accuracy-review.md` (what was already
corrected, and how), `docs/reading/AUTHORING.md`, and
`docs/reading/kit-report.md`.

## What to look for

1. **Misstated research.** Every sentence that says what a study found, who
   found it and when, must match §S and the accuracy review, at the same
   strength: population (college students, school-age readers, learners of
   English), method (EMG feedback against articulatory suppression; a
   trailing mask, not blocked regressions), and size. A correlation stated as
   a cause; a contested threshold stated as settled; one study generalised to
   all readers. Use WebSearch/WebFetch (load with ToolSearch) where a claim
   goes beyond §S, and say what you checked.
2. **Honesty of the Subject's own claims.** No promised gains; no
   measurement called "your reading speed"; the speed-reading tradition
   stated fairly before the evidence; no verdict in the lesson's own voice
   that the evidence does not support (in either direction).
3. **Arithmetic.** Recompute every figure in prose, worked lines, quiz
   answers and `why`s exactly. Render with
   `python3 scripts/preview_subject.py reading --course <course-slug> --out <dir>`
   into a folder of your own under
   `/tmp/claude-0/-home-claude/291ed4a3-3972-5b4f-bb6a-9013cbbfacc9/scratchpad/`,
   and read every preset's tiles with `node scripts/labcheck.js --observe <page>`.
4. **The drills.** Do each drill in a real browser (Playwright is
   pre-installed: `require('playwright')`, `chromium.launch()`; serve the
   output with `python3 -m http.server`). Does the lesson's text match what the
   drill does? Is the passage hidden during questions, the log written with
   the right `kind`, the comparison explained with its confounds?
5. **Quiz and passages.** Exactly one defensible answer per quiz question;
   argue for every distractor. For the passages the lesson uses: any
   comprehension question answerable without reading, or with two defensible
   answers (report; do not edit passages).
6. **Voice** against §F: warm, practical, about the reader's own numbers;
   flag anything performed, preachy or promising.

## Rules

Fix what you are confident of in the course's own files (and its §C entries
where they must agree), keeping the preview at OK. Leave taste as
recommendations. Do not touch other courses, the passages, `scripts/`,
`tests/` or the kit. Never run git commands that change the index or working
tree; other agents share this checkout. Do not commit. If the package fails to
import because another course is mid-edit, wait and retry.

Write the findings file (each finding with lesson, what was wrong, what you
changed or recommend; then where you disagree with the pedagogy assessment)
and report a short summary with the final preview output line.
