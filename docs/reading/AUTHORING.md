# Authoring a Reading Faster course: the brief every author works from

This is the hand-off for writing one course of the Reading Faster Subject. The
design authority is `docs/reading/PLAN.md`; where this file and the plan
differ, the plan wins, and you say so in your report.

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; never read `site/`), and
   `content/AGENTS.md` (how prose, math runs and spoken forms are written).
2. `docs/reading/PLAN.md` §0, §B, your course's entries in §C, §D.3, §P, §E,
   §F, §G and §S. §F is the voice; read the exemplary paragraph twice. §D.3
   wins over the rest of §D.
3. `docs/reading/kit-report.md`, which lists every cfg field per mode and view,
   every input and tile id with an example string, the drill flow, and the
   deviations from §D you must follow. The code is
   `scripts/mathpath/labs/readkit*.py`; the lab key is always `"readkit"`.
4. One finished course as a shape reference:
   `content/philosophy/c1_arguments/__init__.py` and its `part_a.py`. The
   field table is `docs/philosophy/PLAN.md` §E ("Course fields" and the lesson
   field table); same ranges, same enforcement.
5. If Measure Your Reading (`content/reading/c1_measure/`) is already
   written, read two of its lessons as the voice reference.

## The passages

The drills' texts are in `content/reading/passages/` (`bank_a.py`,
`bank_b.py`, `pool.py`; `PASSAGES` in `__init__.py` merges them). Import them
(`from reading.passages import PASSAGES`) and put the dicts themselves into
the cfg as the kit report says. Read every passage your lessons use, and do
the drill yourself on the rendered page (below). Never edit a passage; if one
does not serve its lesson (a question with two defensible answers, a matched
pair that is not matched), say so in your report with the fix you propose.

## Where you write

- `content/reading/cNN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` for Skimming, Scanning and
  Previewing (lessons 5–7).
- `content/spoken/reading.py`: spoken forms for math runs the read-out cannot
  settle. Other authors write to this file at the same time: re-read it just
  before each edit, add only a block headed `# <Your course title>`, and never
  touch another course's block.
- `docs/reading/PLAN.md`: only §C corrections your course forces, in your
  course's entries (a preset instance you had to change, with its figures).
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, the passages,
  other courses or the kit. If the kit cannot show something a lesson needs,
  write the lesson with what it can show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree. The orchestrator reviews and commits.

## The loop for each lesson

1. Write the dict from the §C entry; §C's misconception is `mistakes[0]`;
   the `standard` measures §C's **Standard**.
2. Write the lab cfg and presets with `expect: {}`.
3. Render your course only:
   `python3 scripts/preview_subject.py reading --course <course-slug> --out <dir>`
   with a directory under
   `/tmp/claude-0/-home-claude/291ed4a3-3972-5b4f-bb6a-9013cbbfacc9/scratchpad/`.
4. `node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`
   and copy the tile strings each preset exists to show into `expect`. Check
   each against your own arithmetic and against §C before you pin it. A
   pinned string you did not verify is worse than none.
5. Do the drill in a real browser: serve `<dir>/site` with
   `python3 -m http.server`, open the lesson with Playwright (pre-installed;
   `require('playwright')`, `chromium.launch()`), run Start → Done → answer →
   Score, and read what the reader sees. A drill that confuses you is a lesson
   defect; fix the lesson's instructions or report the kit gap.
6. Re-run `preview_subject.py` without `--no-labcheck` until it prints OK, and
   fix every unspoken run it lists.
7. Try to argue for every wrong quiz answer. If you can, rewrite it.

## What every lesson must do (from §B, §C and §F)

- **The drill is the lesson.** The body explains what the drill measured and
  why; the `steps` are the protocol for doing the drill again on another day
  (in Course 2 lesson 3 and after, the last step is "then today's Daily Drill"
  with its title).
- **Drill-first lessons** (§C marks them): the first `p` sends the reader to
  the drill; `summary`, `one_line` and `concepts` state the question and the
  method, never the expected result.
- **Every preset id appears in a body `p`** with the figures it shows.
- **Every compare lesson**: the body says once that a reader whose result goes
  the other way has not refuted the study, and the study has not refuted
  them; the `note` names the two confounds (different passages; which came
  first).
- **Claims about research** are taken from §C and §S as corrected by the
  accuracy review, at the strength stated there, with the author and year.
  Do not add a study, figure or quotation that is not in §S; if a lesson
  needs one, propose it in your report.
- **No promises** of a speed gain; never call a measurement "your reading
  speed" or "your level".
- A three-letter word at the head of a key line or after `=` is spelt out
  letter by letter by the read-out (`wpm` included): write "words a minute",
  or put the abbreviation mid-phrase, and check `speechcheck` output.
- The last `p` of the body points to the next lesson by title (at a course's
  end, to the next course).

## Report

End with a short report: lessons written, every §C deviation and why, any kit
gap, any passage problem, the preview command's final output line, and any
spoken forms added.
