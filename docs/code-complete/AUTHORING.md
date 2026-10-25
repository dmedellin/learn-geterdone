# Authoring a Code Complete course: the brief every author works from

This is the hand-off for writing one course of the Code Complete read-along.
The design authority is `docs/code-complete/PLAN.md`; where this file and the
plan differ, the plan wins, and you say so in your report. The Subject is
built the way Capital and Phenomenology of Perception were
(`docs/phenomenology/AUTHORING.md` is the model, and its "Lessons from"
sections apply here in full), with one difference that runs through
everything: every lesson is applied, and the code in it is the lesson's own.

**Do not start until the renderer's `code` block and code read-out (PLAN
§H.1, R1 and R2, including the review's R2 additions) have landed**, unless
the orchestrator says you are working around them. Without R1 there is
nowhere to put a snippet; without R2 a lesson on `!done` is read aloud as
"done" and a listing is read without the line numbers the prose refers to.
The book's text is in hand (PLAN §E.2), and PLAN has been reviewed and
reconciled (§R): read §R's entries for your course before you start.

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; never read `site/`), and
   `content/AGENTS.md` (how prose, inline runs and spoken forms are written).
2. `docs/code-complete/PLAN.md` §0, §B, your course's entries in §C, §D.0,
   §D.4, §E, §F, §G and §S (all of §S.2). §F is the voice; read the exemplary
   paragraph twice. §D.4 holds the snippets and the reference model's figures.
3. `docs/code-complete/kit-report.md` once the kit engineer has written it:
   every cfg field per mode and view, every input and tile id with an example
   string, how the code textarea is filled, and the deviations from §D you
   must follow. The code is `scripts/mathpath/labs/cckit*.py`; the lab key is
   always `"cckit"`. Where the kit report and §D differ, the kit report wins.
4. One finished course as a shape reference:
   `content/phenomenology/c1_preface/__init__.py` and its `part_a.py`. The
   field table is `docs/philosophy/PLAN.md` §E ("Course fields" and the
   lesson field table); same ranges, same enforcement. A `code` block counts
   as one body block.
5. If Course 1 (`content/code_complete/c1_foundation/`) is already written,
   read two of its lessons as the voice reference for this Subject.

## The text

The source is McConnell, *Code Complete*, 2nd edition (Microsoft Press,
2004), PLAN §E.2. It is in copyright.

**Where it is.** A private extraction of the operator's copy, outside the
repository:
`/tmp/claude-0/-home-claude/3b1d3502-1b81-5554-ace3-d7f9f019031f/scratchpad/book/cc2.txt`
(`pdftotext -layout`, one form feed per PDF page). **Printed page = PDF page
− 37.** If the orchestrator has moved it, the new route is in your brief.
Two helpers sit in `…/scratchpad/tools/`:

- `python3 ccbook.py '<regex>'` prints each matching line as
  `printed page | line`. Use it to find a passage; then read the section you
  need with a narrow `sed -n` on the page, never the file whole.
- `python3 cc_quotes.py <file>` checks lines `tag|page|quote` against the
  page (and the next) and prints OK, LOOSE or MISS with the word count. Run
  it on every quotation you use.

**What is settled.** Every page, section number and title in PLAN §C is the
book's, checked against the text. Every figure in §S.2 (F1–F30) is settled,
with its page and the sources the book names. Each lesson's opening
quotation is chosen in §C's **Quote** line, with its page and word count.

- Put the page in a comment beside the dict (`# McConnell §10.4,
  pp. 244–258`); in prose, name the chapter and sections and invite the
  reader to read them in their own copy first.
- Every figure you attribute to the book carries a comment with its §S.2 id
  and page (`# F17, p. 470`) and is written as the book's report of
  someone's figure ("the book's table, after Jones, gives …"), at the
  strength §S.2 gives. A figure not in §S.2 is not attributed to the book; if
  you need one, find it with `ccbook.py`, add the row to §S.2 in the same
  change, and say so in your report.
- Read the section, not only the line: before you write "McConnell argues",
  grep the passage and read the paragraph around it. If the book differs
  from §C, the book wins; correct §C in the same change and report it.
- **Quotations.** Open with §C's **Quote** or none. One quotation of at most
  **40 words**; a lesson's quotations total at most **60 words** (PLAN
  §E.3). Copy character for character from the text (curly quotes and
  apostrophes as the book prints them; inner quotation marks as
  `&lsquo;…&rsquo;`), the page in a comment beside the dict, and check it
  with `cc_quotes.py`. Never from memory, a blog, a secondary source or the
  PLAN's line wrapping. A line McConnell quotes from someone else (Knuth,
  Brooks, Dijkstra) is attributed to its author and counted against the same
  limits.

**Never:** reproduce the book's code listings, checklists, tables or
figures, retyped or "adapted" line by line (the review found four
adaptations in the first draft of this plan, all since replaced: PLAN §R,
MF-1). A table's figures may be used a few at a time as facts with their
source; a checklist may be named and two or three of its points paraphrased;
no more. Never copy the text, or any stretch of it beyond the quotations
above, into the repository, the project files or a report.

## The code

Every snippet in a lesson is written for it (PLAN §D.4); never the book's,
never one found online.

- **Java**, plain Java 8 or later as PLAN §D.0 says: no records, no `var`,
  no lambdas, no streams, no annotations. It must compile as a fragment a
  reader would accept: declared types, balanced braces, no undeclared names
  except calls the prose names as "some routine that …".
- As short as the point allows: at most 20 lines (the renderer allows 30;
  `nested-shipping`, 22, is the one exception, because the nesting is the
  lesson), at most 72 characters a line where possible and never more than
  80 (R1's limit), four-space indentation, no tabs.
- **One constant per snippet.** Each snippet is one Python string constant
  in your course module, used by the lesson's `code` block (split into
  lines) and by the preset's cfg, so the line numbers the prose names are
  the lab's. Never paste the same code twice. The test
  `test_code_complete_presets_use_the_lessons_snippets` checks it.
- A snippet that is in §D.4 (or `presets.py`) is copied from there exactly,
  because its figures are computed from that text. A changed or new snippet
  is run through the reference model or the built lab (`labcheck.js
  --observe`, below) and its figures are recorded in your course's §C entry
  in the same change.
- The snippet must do what the lesson says it does. Trace it by hand for the
  values the prose names; a deliberately buggy snippet (the off-by-one, the
  dangling `else`, the `clamp` whose `return high;` is unconditional) is
  wrong in exactly the one way the lesson says and no other.
- Inline code in prose is a backtick run and stays short: an identifier, a
  condition, a call. Anything longer than about 40 characters goes in a
  `code` block.

## Where you write

- `content/code_complete/cN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` where PLAN §E.1 splits the
  course (Courses 2, 4 and 5, at the chapters it names). The course `how_to`
  carries the attribution: a read-along of McConnell's *Code Complete*, 2nd
  edition (Microsoft Press, 2004), with code written for these lessons and
  section numbers that edition's.
- `content/spoken/code_complete.py`: spoken forms for runs the read-out
  cannot settle even with the code dialect. Other authors write to this file
  at the same time: re-read it just before each edit, add only a block headed
  `# <Your course title>`, and never touch another course's block.
- `docs/code-complete/PLAN.md`: only §C corrections your course forces, in
  your course's entries (a snippet you had to change, with its figures; a
  section the book numbers differently), and §S.2 rows the book settles.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kit. If the kit cannot show something a lesson needs, write the lesson
  with what it can show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout. The orchestrator reviews
  and commits.

## The loop for each lesson

1. Write the dict from the §C entry; §C's misconception is `mistakes[0]`;
   the `standard` measures §C's **Standard**; the exercise is §C's
   **Exercise**, laid out as PLAN §E.4 item 4 says (an `h3` "Exercise", the
   `code` block, a `p` saying what to find). §C's **Answer** is the `why` of
   one quiz item that asks for it, and appears nowhere else on the page;
   `worked` works the preset §C's **Worked** names. The last of the `steps`
   is §C's **Own:** line, as an instruction with an observable result.
   §C's **Also** misconception, where given, is `mistakes[1]`.
2. Write the lab cfg and presets with `expect: {}`.
3. Render your course only:
   `python3 scripts/preview_subject.py code-complete --course <course-slug> --out <dir>`
   with `<dir>` a folder of your own under your session's scratchpad
   directory.
4. `node scripts/labcheck.js --observe <dir>/site/<path>/index.html` and copy
   the tile strings each preset exists to show into `expect`. Check each
   against §C and against your own count on the snippet before you pin it. A
   pinned string you did not verify is worse than none. Where the lab and §C
   disagree, find out which is wrong: a §C figure is a reference model's, and
   the model can be wrong; the lab can be too (report it as a kit gap).
5. Open the lesson in a real browser once (serve `<dir>/site` with
   `python3 -m http.server`; Playwright is pre-installed:
   `require('playwright')`, `chromium.launch()`). Load each preset, then
   edit the code in the textarea the way the exercise asks and read the
   tiles. A lab that confuses you is a lesson defect: fix the instructions,
   or report the kit gap.
6. Re-run `preview_subject.py` without `--no-labcheck` until it prints OK,
   fix every unspoken run it lists, and run
   `/usr/bin/python3 scripts/speechcheck.py` with the code dialect on. Listen
   to one lesson per course with the read-out: every `&&`, `||` and prefix
   `!` must be said as "and", "or" and "not".
7. Try to argue for every wrong quiz answer. If you can, rewrite it. The
   rules (PLAN §E.4 item 5): every distractor differs from the answer on a
   row of a truth table or an integer, and the `why` names it (`!isAdmin &&
   isOwner` and `isOwner && !isAdmin` are the same condition; `qty >= 1 &&
   qty <= 99` and `qty > 0 && qty < 100` are the same check); never quiz a
   verdict ("is this routine too complex?"); a question on decision points
   states the rule in the stem; a figure from the book is asked only as §S.2
   gives it, with its source in the `why`.
8. `grep -n "# F[0-9]" <your course package>` and check that every figure
   attributed to the book has its §S.2 id and page, and nothing else does;
   run `cc_quotes.py` on your quotations.

## What every lesson must do (from §B, §C, §E and §F)

- **The chapter's argument, then the code.** The first half sets out what
  the chapter argues, section by section, in paraphrase that names whose
  claim it is; the second half turns to the snippet, does the chapter's count
  on it with the lab, and ends with the exercise. The count is never the
  point; what it shows about the code is.
- **Every preset id appears in a body `p`** with the figures it shows, and
  every tile a view prints is explained in prose at least once in the course.
- **A count is a reason to look, not a verdict** (the material clause). Never
  write that code "is" bad because a number is high; write what the number
  measured and what to look at.
- **The numbers are other people's.** Where a lesson leans on a rate, cost or
  ratio from the book, it says once whose figure it is, that it is an average
  over other people's projects, and that the reader's own records can test it.
  Never "studies show" without the study. A lab figure computed from a
  figure the lesson supplies (a removal rate, a cost multiplier) is the
  model's arithmetic on that figure, and the prose says so.
- **No language wars.** Where Java differs from C or Python on the point,
  say so in a sentence; never say one language is better.
- **At most one modern aside per course**, in the lesson §F item 4 names as
  its home, stating the book's position at strength and the later view
  fairly. Never "outdated" or "modern developers know better" in the
  lesson's voice.
- **Key lines** are at most 46 characters; a three-letter word at the head of
  a key line or after `=` is spelt out letter by letter by the read-out
  (`int`, `for`, `LOC`): reword, and check `speechcheck` output.
- The last `p` of the body points to the next lesson by title (at a course's
  end, to the next course).

## Voice, in short (PLAN §F is the authority)

The read-along voice of Capital and Phenomenology, for a working programmer:
the chapter first, then section by section; "you", warmly; the history of an
idea as a story with people in it (Dijkstra's letter, Knuth's reply, Fagan's
inspections), at most once a lesson; at most one light remark, preferably
pointing at McConnell's own. Open with the reader's own code (a routine that
has grown, a bug found by bisecting) in at most half of a course's lessons,
and with the chapter's own question in the rest. McConnell is presented, not
endorsed. No slang, no first-person anecdotes, no "let's dive in", no
performed enthusiasm about clean code. The `note` names what the lesson's lab
cannot settle.

## Lessons from Capital and Phenomenology that apply here

- Do not give McConnell a verdict the book does not contain. Re-read every
  sentence that begins "McConnell says", "argues", "recommends" or
  paraphrases him, against the page (`ccbook.py`), at the strength the page
  states.
- A misconception is refuted by the chapter's argument; a lab run on the
  lesson's illustrative instance illustrates the refutation and is said to
  ("on the lesson's illustration, …"). The later view named as a course's
  modern aside is never `mistakes[0]` (PLAN §C preamble, §F.4).
- A view McConnell states in order to qualify it (the case for long routines
  in §7.4, the case against comments in §32.3's dialogue) is not his
  conclusion. Say whose voice it is.
- A figure the book reports from someone else is that person's figure, from
  that person's projects, in that year. Say so the first time.
- A lab figure is what the model computes from the code or the quantities
  given, never a property of good software. "The lab counts 9 decision
  points", not "this routine is too complex".
- Do not impose a structure the chapter lacks, and do not praise one side in
  the lesson's own voice.
- Gloss every term of art in plain English on first use (*cohesion*,
  *coupling*, *span*, *structured basis*, *refactoring*).
- Several authors share this checkout. If the package fails to import
  because another course is mid-edit, wait a minute and retry; re-read a file
  before each edit.

## Report

End with a short report: lessons written, every §C deviation and why (each
changed or new snippet with its figures), any kit gap, any renderer or
read-out problem, every page or figure you corrected against the text, each
quotation used with its `cc_quotes.py` result, the preview command's final
output line, and any spoken forms added.
