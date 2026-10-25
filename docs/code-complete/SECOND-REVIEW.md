# Second review of a Code Complete course: the brief

Every course of the Code Complete read-along gets two reviews: a pedagogy
assessment (`docs/pedagogy/code-complete-<course-slug-without-prefix>.md`) and
this second, independent read
(`docs/reviews/code-complete-<course-slug-without-prefix>-second-review.md`).
In Capital and Phenomenology the second reviews found few arithmetic errors
but many places where a course misstated what the author argues, usually in
passages the pedagogy assessment praised; in Reading Faster they found
findings stated more strongly or broadly than the study showed. This book
carries both risks — it is an argument and a synthesis of other people's
research — and a third of its own: the code. A snippet that does not do what
the lesson says teaches the opposite of the chapter. Those three are what this
review is for.

## Do not anchor

Do not read the course's pedagogy assessment until you have written your own
findings. Then read it and record where you disagree.

## Read first

`AGENTS.md` §0, §7, §8 (never read `site/`), `content/AGENTS.md`,
`docs/code-complete/PLAN.md` (the status note, §0, §B, the course's §C
entries, §D.0, §D.4, §E, §F, §G, §S and §R — §R records what the two
pre-authoring reviews found and what was done, so do not re-raise a settled
point without new evidence), `docs/code-complete/AUTHORING.md`, and
`docs/code-complete/kit-report.md`.

The book's text is in hand: a private extraction outside the repository,
with `ccbook.py` to grep it and `cc_quotes.py` to check quotations
(AUTHORING.md, "The text"; printed page = PDF page − 37). Every check below
against "the book" is against the page. Grep it; never read it whole, and
never copy its text into your findings beyond a phrase that identifies a
claim.

## What to look for

1. **Misrepresentation of McConnell.** Every sentence that says what he
   argues, recommends, reports or concludes must match the book (or §C, at
   §C's strength). A position he states in order to qualify it (the case for
   long routines, the voice in the comment dialogue) presented as his
   conclusion. A recommendation made absolute that the book hedges ("never
   use `goto`", "routines must be short"). A structure imposed that the
   chapter lacks. A verdict in the lesson's own voice, for or against him.
2. **Misstated research.** Every figure attributed to the book or to the
   people it cites (Jones, Boehm, Fagan, McCabe, Gorla, Sackman, Miara,
   Basili, Knuth…) must match §S.2 at the same strength: whose figure, from
   which projects or population, which year, an average or a range. A modal
   rate stated as a guarantee; one study generalised to all programmers; a
   correlation stated as a cause. Run `grep -n "# F[0-9]" <course-package>`:
   every book figure in the course has a comment with its §S.2 id and page,
   and no figure lacks one; check each against the page with `ccbook.py`.
   Where a claim goes beyond the book (an original study), use
   WebSearch/WebFetch (load with ToolSearch) and say what you checked; a
   figure you cannot confirm is listed, not corrected from memory.
3. **Copyright.** No code listing, checklist, table or figure of the book's
   reproduced or adapted line by line; at most two or three points of a
   checklist, paraphrased; quotations at most 40 words for the opening and
   60 a lesson, each with its page (PLAN §E.3). Run every quotation in the
   course through `cc_quotes.py` (a line `tag|page|quote` per quotation): a
   MISS, a word count over the limit, a page that differs, or a quotation
   other than §C's **Quote** that §C does not record is a finding. A phrase in
   quotation marks attributed to McConnell that is not on the page is a
   finding of the first rank.
4. **The code.** For every snippet: does the Java compile as the fragment the
   lesson presents (types declared, braces balanced, no feature PLAN §D.0
   excludes)? Does it do what the prose says it does? Trace it by hand for
   every value the prose, worked line or quiz names. A deliberately faulty
   snippet must be faulty in exactly the way the lesson says and no other: an
   off-by-one with a second, unmentioned off-by-one is a finding. Where Java
   behaves differently from what a C or Python reader expects (integer
   overflow, `==` on strings, `switch` fall-through), the lesson says so.
   Compare each snippet against §D.4: a changed one must have its new
   figures recorded in §C.
5. **Arithmetic and counts.** Recompute every figure in prose, worked lines,
   quiz answers and `why`s exactly, by hand on the snippet, by the rule the
   lesson states (decision points, span and live time, boundary values, call
   counts, removal rates). Render with
   `python3 scripts/preview_subject.py code-complete --course <course-slug> --out <dir>`
   into a folder of your own under your session's scratchpad directory, and
   read every preset's tiles with `node scripts/labcheck.js --observe <page>`.
   Where your count, the lab's and the lesson's disagree, say which is right
   and why. Check that each figure is attributed to what produced it: a count
   is the lab's rule applied to this code, never a verdict on the code; a
   figure computed from a quoted rate is arithmetic on someone's average.
6. **The labs.** Open each lesson in a real browser once (Playwright is
   pre-installed: `require('playwright')`, `chromium.launch()`; serve the
   output with `python3 -m http.server`). Load each preset; edit the code as
   the exercise asks; read the tiles and the listing's line numbers against
   the prose. Does the lesson's text match what the lab does? Check that the
   preset's code and the body's `code` block are the same constant (PLAN
   §E.4 item 2), and that the exercise's answer appears only in a quiz
   `why`.
7. **The read-out.** Run `/usr/bin/python3 scripts/speechcheck.py`, and listen
   to (or read the spoken text of) each lesson's code lines and backtick
   runs: `&&`, `||` and a prefix `!` must be said "and", "or", "not"; a
   `code` block's lines are announced by number; `%` is "mod". A negation
   dropped is a finding of the first rank.
8. **Quiz.** Exactly one defensible answer per question; argue for every
   distractor. A wrong answer that the book partly supports (it does tolerate
   long routines in some cases) is defensible: sharpen it into the reading the
   lesson argues against. Distractors that are the same condition or the same
   integer check as the answer, a quizzed verdict, and a decision-point
   question without the rule in its stem are findings (PLAN §E.4 item 5).
9. **Voice** against §F: the chapter first, then the code; warm, practical,
   about the reader's own code; McConnell presented, not endorsed; the
   numbers named as other people's; at most one modern aside in the course,
   in the lesson §F names, stated fairly in both directions; no language
   wars; flag anything performed, preachy or dismissive ("outdated",
   "modern developers know better").

## Rules

Fix what you are confident of in the course's own files (and its §C entries
where they must agree), keeping the preview at OK. Leave taste as
recommendations. Do not touch other courses, `scripts/`, `tests/` or the kit;
a kit fault goes in the findings with the page and the preset that shows it.
Never run git commands that change the index or working tree; other agents
share this checkout. Do not commit. If the package fails to import because
another course is mid-edit, wait and retry.

Write the findings file (each finding with lesson, what was wrong, what you
changed or recommend; then any claim you could not settle against the page,
with what you searched; then where you disagree with the pedagogy
assessment) and report a short summary with the final preview output line,
the count of `# F` figure comments in the course, and the `cc_quotes.py`
results.
