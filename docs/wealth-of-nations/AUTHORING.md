# Authoring a Wealth of Nations course: the brief every author works from

This is the hand-off for writing one or two courses of The Wealth of Nations,
Read Along. The design authority is `docs/wealth-of-nations/PLAN.md`; where
this file and the plan differ, the plan wins, and you say so in your report.

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; **never read `site/`**), and
   `content/AGENTS.md` (how prose, math runs and spoken forms are written).
2. `docs/wealth-of-nations/PLAN.md` §0, §A, §B, your courses' entries in §C,
   §E, §F, §G. §F is the voice.
3. `docs/capital/AUTHORING.md`, the sections "Voice, in short" and both
   "Lessons from the Course 1 review" lists. They apply here word for word,
   with Smith for Marx (Smith died in 1790: never "Smith's answer to Ricardo").
4. The kit you will configure. Read the kit reports, which list every cfg
   field per mode and view and every tile id with an example string:
   - Book I modes (division, money, price, wages, advantage, rent, interest):
     `docs/wealth-of-nations/kit-report-a.md`
   - Books II to V modes (stock, bank, trade, tax, debt, public, system):
     `docs/wealth-of-nations/kit-report-b.md`
   The lab key is always `"wonkit"`: `"lab": ("wonkit", {"mode": ..., "view":
   ..., "presets": [...]})`.
5. One finished course as a shape reference, field for field:
   `content/capital/c01_commodities/__init__.py` and its `part_a.py` (read two
   lessons whole: they are the voice reference too). Ranges are enforced by
   `scripts/preview_subject.py`: 3 concepts, 3 mistakes, 4–5 steps, 3–4 quiz
   questions with 4 distinct choices, 3–8 key lines of at most 46 columns,
   7–18 body blocks.

## The text

`/mnt/project-files/wealth-texts/wealth-of-nations-psu.txt` (read-only;
never write to that folder; about 31,000 lines: never read it whole). Tools,
run from their directory
`/tmp/claude-0/-home-claude/799ff4e6-d40c-554f-8670-3d4578ce9497/scratchpad/tools/`:

- `python3 grep_text.py N M` prints lines N to M with line numbers. Use
  `grep -n` on the text file to find passages.
- `python3 quotes.py <your course dir>` checks every `&ldquo;…&rdquo;` span in
  your files against the text (case-sensitive, ignoring line breaks,
  hyphenation and punctuation spacing) and prints OK with the line or MISS.
  Every MISS is a defect: fix the quotation from the text, or reword so it is
  not a quotation.

Before writing a lesson, read its whole chapter or Part (PLAN §C gives
approximate line ranges; find the true boundaries). Quote by copying from the
file, at most 120 words in any one quotation, and put the line in a comment
beside the lesson dict (`# PSU text l. 1234`). The extraction repeats headings
and running heads and sometimes jams a word ("fortyfour"): quote clean
running text and spell a jammed word as printed books do. Smith's figures
that you state or use as preset data are checked against the line you cite.

## Where you write

- `content/wealth_of_nations/cNN_<name>/__init__.py` (the COURSE dict,
  replacing `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons.
  The course `how_to` carries the attribution: a read-along of Adam Smith,
  *An Inquiry into the Nature and Causes of the Wealth of Nations* (1776),
  quoted from the public-domain Electronic Classics Series edition.
- `content/spoken/wealth_of_nations.py`: spoken forms for math runs the
  read-out cannot settle. Other authors write to this file at the same time:
  re-read it just before each edit, add only a block headed
  `# <Your course title>` inside the SPOKEN dict, never touch another block.
- `docs/wealth-of-nations/PLAN.md`: only §C corrections the text forces, in
  your courses' entries (line ranges, a misremembered figure).
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses,
  `content/wealth_of_nations/__init__.py`, or the kit. If the kit cannot show
  something a lesson needs, write the lesson with what it can show and list
  the gap in your report.
- Do not commit or push, and run no git command that changes the index or
  the working tree; other authors and engineers share this checkout.

## Two phases

**Phase A (while the kit is being built):** read your chapters, then write
every lesson in full (prose, concepts, steps, mistakes, quiz, key lines,
worked example, note) with a `lab` drafted from PLAN §D (mode, view, presets
with `expect: {}`). The kit is ready when
`grep -c '"wonkit"' scripts/mathpath/labs/__init__.py` is non-zero and both
kit reports exist. Run `quotes.py` in phase A. If the kit is not ready when
your prose is done, poll every few minutes (`sleep 120` between checks is
fine) for up to an hour; then continue with phase B.

**Phase B (when the kit reports exist and wonkit is registered):** correct
every lab cfg against the kit reports, then run the loop.

## The loop

Render your course only:
`python3 scripts/preview_subject.py wealth_of_nations --course <course-slug> --out <dir>`
with `<dir>` a new folder under
`/tmp/claude-0/-home-claude/799ff4e6-d40c-554f-8670-3d4578ce9497/scratchpad/preview/`.
`wonkit` is a gated kit: every preset needs an `expect`. Write `expect: {}`
first, run
`node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own arithmetic
by hand (and against Smith's figure in the text, where the preset is his). A
pinned string you did not verify is worse than none. Every preset id must
appear in a body paragraph with the figure it shows. Re-run
`preview_subject.py` until it prints OK; fix every unspoken run it lists
(add spoken forms where needed). Try to argue for every wrong quiz answer; if
you can, rewrite it. Spread the correct answers' positions (not all `c: 1`).

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Points specific to this book

- **Money.** Smith writes £, s and d; say once per course what the units are
  (12 pence a shilling, 20 shillings a pound) where the figures need it. A
  quarter of corn is eight bushels. In key lines and math runs, beware
  three-letter words at the head of a line (`tax`, `net`, `due`): the read-out
  spells them; reword.
- **Smith's figures and the lesson's.** A preset with Smith's figures says so
  in its label ("Smith's pin factory"); a preset written for the lesson says
  that ("a village, written for this lesson"). Never present an invented
  figure as Smith's, or a figure as history that Smith reports second-hand
  without saying whose it is.
- **Capital.** Where a lesson meets a point Capital argues with, name the
  Capital lesson by its title in one sentence (find titles with
  `grep -n '"title"' content/capital/c*/part_*.py`) and do not repeat its
  argument. Capital is the next Subject on the shelf, not a rebuttal.
- **Fairness.** Present Smith at strength and his critics at strength:
  Ricardo on rent and comparative cost, Malthus on population, Say, List on
  infant industries, Marx on productive labour and the resolution of price,
  later historians on the invisible hand's single appearance in the book. Do
  not praise either side in the lesson's own voice.

## Report

End with a short report (under 400 words): lessons written; every §C
deviation and why; any kit gap; renderer or read-out problems; the
`quotes.py` final state (any MISS left is a defect); the preview command's
final output line; spoken forms added.
