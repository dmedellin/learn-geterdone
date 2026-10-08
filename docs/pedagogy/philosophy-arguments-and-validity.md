# Pedagogy assessment — Arguments and Validity (philosophy, course 1)

Formed from the twelve lesson dicts in `content/philosophy/c1_arguments/`
(`part_a.py`, lessons 1–6; `part_b.py`, lessons 7–12; `__init__.py`, the
course dict), the spoken forms in `content/spoken/philosophy_c1_arguments.py`,
and the kits they render through (`scripts/mathpath/labs/argkit.py` modes
`validity`, `consistency`, `syllogism`; `scripts/mathpath/labs/logic.py`
`truth_table` and `quantifier`), on branch `feat/philosophy` before the
course was wired into the site. The design authority is
`docs/philosophy/PLAN.md` §C (course 1) and §F; the course was written by two
authors, one per part, so the seam at lesson 7 is assessed as well.

Every lesson was read in full before anything was changed. Every pinned figure
and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through `scripts/preview_subject.py`,
with a sibling course that does not currently import stubbed out), not out of
the kit source. Lessons, in course order: `premises-conclusions-and-standard-form`,
`validity-and-soundness`, `truth-values-and-the-connectives`, `the-conditional`,
`validity-by-truth-table`, `equivalence-de-morgan-and-contraposition`,
`consistency-and-belief-sets`, `categorical-statements-and-immediate-inference`,
`the-square-of-opposition-and-existential-import`,
`syllogisms-tested-by-venn-regions`, `quantifiers-and-their-order`,
`fallacies-and-the-counterexample-method`. This is the entry course of the
Subject and may assume nothing; it is judged as such.

## Verdict

The course teaches its subject. A reader who finishes it can set a passage out
in standard form, decide validity by looking for a row, keep validity apart
from soundness, negate and contrapose without producing the converse, test a
set of beliefs for a model and name the smallest subset that fails, read the
four categorical forms as region claims and test syllogisms on them with
existential import as a switch, read nested quantifiers off a grid, and refute
a bad form with a case. Those are the acts the `standard` fields measure and
the labs compute, and none of the twelve objectives is "understand X". The
defects found were local: one factual slip in a table paragraph, one concept
title that says the opposite of its body, one mistake paragraph that
contradicts the lesson's own thesis, a vocabulary quiz, and a handful of
places where the prose was looser than the lab it describes. All are repaired
below. Nothing needs splitting, merging or reordering.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names what is produced: the
  layout with reasons (`premises-conclusions-and-standard-form`), the two
  classifications with a reason each (`validity-and-soundness`), the row where
  inclusive and exclusive or part (`truth-values-and-the-connectives`), the
  counterexample row and the form's name (`validity-by-truth-table`), the
  model or the failing subset (`consistency-and-belief-sets`), the region that
  decides each inference (`categorical-statements-and-immediate-inference`),
  which side of the import switch an inference sits on
  (`the-square-of-opposition-and-existential-import`), the pattern that
  decides a syllogism (`syllogisms-tested-by-venn-regions`), the six values and
  the cell, row or column deciding each (`quantifiers-and-their-order`), and a
  substitution instance with true premises and a false conclusion
  (`fallacies-and-the-counterexample-method`).
- **Validity is taught as the absence of a row, and the lab is always the
  row.** The course never announces a verdict it has not shown. `validity-by-truth-table`
  prints the table for modus ponens and for affirming the consequent with the
  irrelevant rows marked "a premise is F" and the one that matters marked
  COUNTEREXAMPLE, which is the whole method in two blocks. The lab's `vaShow`
  control then strips the table to the counterexample rows, which is the same
  idea as a control.
- **The hard philosophical move is made early and repeated honestly.**
  `validity-and-soundness` puts the lesson's third concept where it belongs:
  "If a valid argument leads to a conclusion you reject, you are not entitled
  to say the argument is invalid. You are committed to rejecting at least one
  premise." `consistency-and-belief-sets` then shows, with the lab's give-up
  menu and a four-row table of the models that appear, that an inconsistent
  set says one member must go and never which; the quiz asks "which sentence
  is the false one?" and the right answer is that the table does not say. That
  neutrality is the Subject's thesis and the course earns it rather than
  asserting it.
- **The lab's limit is stated in the lesson that leans on it.** Soundness is
  not checked (`validity-and-soundness`, footer, `how_to`); "whether it rained
  is the right way to put the author's claim" is not checked
  (`premises-conclusions-and-standard-form`); a finite grid refutes a form and
  cannot prove one valid (`quantifiers-and-their-order`, note and last body
  paragraph); the lab takes at most six letters, eight sentences, three terms,
  and defaults to the Boolean reading (`validity-by-truth-table`,
  `consistency-and-belief-sets`, `syllogisms-tested-by-venn-regions`). Each is
  said once, plainly, where it matters.
- **Positions are stated at their strongest.** The Aristotelian reading is
  "not an error; it is a theory of what ordinary general statements
  presuppose", and the lesson prices both readings (`the-square-of-opposition-and-existential-import`):
  the Boolean one lets a law survive a quiet year, the Aristotelian one keeps
  the square. The material conditional is defended by a promise and by an
  arithmetic generalisation that would fail at 3 and 6 if the false-antecedent
  rows were not T (`the-conditional`), and the note concedes that ordinary
  if-then sometimes means more. The cosmological argument is "accused of" the
  shift, not convicted (`quantifiers-and-their-order`).
- **Every misconception is named as a model someone holds and refuted with
  the row, region or number.** The §C misconception is `mistakes[0]` in all
  twelve lessons, and each refutation is specific: the row `p` false, `q`
  false has a false second premise, so it refutes nothing
  (`validity-by-truth-table`); the pattern with every region empty satisfies
  All `S` are `P` and fails Some `S` are `P`
  (`the-square-of-opposition-and-existential-import`); no cats are fish, no
  dogs are fish, so no dogs are cats has three true statements and a pattern
  with cats and dogs overlapping outside fish (`syllogisms-tested-by-venn-regions`).
- **The worked examples are the famous ones, and they are worked to the
  row.** Wet streets, whales and fish, soup or salad, the match being off, God
  and the meaning of life, rich and famous, the alarm that did not wake her,
  squares and rectangles, unicorns and trespassers, cats and dogs and mammals,
  the successor loop, the butler and the maid. Each ends on the case that
  decides it, and the `after` paragraphs say what the verdict does not show.
- **Figures agree with the lab.** Every count in prose was checked against the
  observed tiles: 4 and 8 rows and 0 or 1 counterexample rows in the three
  `validity` lessons; 2, 4 and 4 rows in `validity-and-soundness`; `0 of 4`,
  `0 of 8`, `1 of 8`, the subsets `{1, 2, 3}` and `{1, 2, 3, 4}` and the
  witness `p=F q=T r=T` in `consistency-and-belief-sets`, and the four
  give-up models in its table (`p=T q=F r=F`, `p=T q=T r=F`, `p=F q=F r=F`,
  `p=T q=T r=T`) recomputed by hand; counterexample regions `P`, `S`, `every
  region empty`, `S+M`, `S+P` and forms `AAA-1 Barbara`, `AAA-2 (no name)`,
  `AEE-1 (no name)` in the three `syllogism` lessons; 8, 4 and 16 rows for the
  three valid forms in `fallacies-and-the-counterexample-method`. The claims
  that the syllogism status line "always reports the other verdict as well"
  and that the quantifier status line says "this is the case that settles the
  order question" when the loop is closed were verified in the kit source
  and hold.
- **The seam at lesson 7 is nearly invisible.** `consistency-and-belief-sets`
  opens by contrasting itself with the preceding six ("An argument has a
  conclusion to test. A set of beliefs has none"), names its test as the table
  of “Validity by Truth Table”, and uses the vocabulary part A established
  (row, case, letter). Part B's `categorical-statements-and-immediate-inference`
  opens with why propositional logic is not enough ("The propositional
  connectives cannot see inside a sentence"), and `quantifiers-and-their-order`
  opens with why categorical logic is not enough ("The categorical forms had
  one variable"). Spelling is British throughout both parts; neither part
  uses a numbered cross-reference; both cite lessons by title and courses by
  name. The only visible difference is that part A writes curly quotes as
  `&ldquo;` entities and part B sometimes writes them as characters, which
  renders identically.

## What it taught badly, or said wrongly

### Facts a reader would trust that were wrong

- **`the-conditional`, body, paragraph after the table:** "The last column is
  the proof that the second and fourth rows are forced." The second row is
  `p` true, `q` false, the one row where the conditional is F. The rows the
  paragraph is defending are the third and fourth, where `p` is false. A
  reader who trusts the sentence and looks at the table is told the F row is
  "forced" T. Repaired: the paragraph now names the third and fourth rows and
  says why a sentence that rules out one case is true in the others.
- **`consistency-and-belief-sets`, `concepts[1]` title:** "An inconsistent
  set is a failed argument in disguise." The body says the opposite and is
  right: premises plus the conclusion's denial have no model exactly when the
  argument is valid. The title taught the inverse of the lesson's own point in
  the position most likely to be read alone. Repaired: "a valid argument in
  disguise".
- **`validity-and-soundness`, `mistakes[0]`:** "its conclusion is false
  because its premises are." The lesson's own body says a valid argument can
  have false premises and a true conclusion, so false premises do not make a
  conclusion false. The misconception paragraph contradicted the thesis it
  was correcting. Repaired: the conclusion is false, and validity allows that
  only because a premise is false too.

### Prose looser than the lab

- **`categorical-statements-and-immediate-inference`, conversion paragraph:**
  "All `S` are `P` empties the region outside `P`" is wrong as written (it
  empties `S` outside `P`), and "Some-not fails in the same way" gave the
  reader nothing to check. Repaired: each statement now names its region, and
  the O conversion is spelt out as the same failure with occupied in place of
  empty. The same paragraph's "sixteen patterns" sat beside a tile reading
  `8` with nothing connecting them; the body now says a premise fixing one
  region leaves three open, so eight patterns survive it, and that this is
  the count the lab reports.
- **`validity-and-soundness`, body:** the `both` preset was pinned (4 rows,
  valid) and never mentioned. One sentence now says why it is valid.
- **`the-conditional`, lab paragraph:** the menu carries the contrapositive
  and the inverse, which the lesson never names, and the panel asks the
  reader to compare against "the other two". The body now says these are
  taken up in “Equivalence, De Morgan and Contraposition” and asks only for
  the row count.
- **`syllogisms-tested-by-venn-regions`, `concepts[1]`:** "four of the forms
  in the first figure have names" reads as though only four forms are named;
  the lab's catalogue names twenty-four. Repaired to say the valid forms carry
  traditional names, the four from the first figure are the ones taught here,
  and the lab knows the rest.

### Quiz items

- **`premises-conclusions-and-standard-form`, quiz 3** tested the vocabulary
  ("which word most often marks a conclusion?") where PLAN §F asks that a
  quiz test the idea. The lesson's misconception, that the conclusion is
  whatever comes last, was tested only glancingly by quiz 1. Replaced with a
  conclusion-first passage with no indicator word ("We should leave now. The
  last train is at eleven, and it is already half past ten"), whose
  distractors include "there is no conclusion".
- Every other distractor in the course was argued for and none could be
  defended. The ones that looked closest were checked by hand: in
  `syllogisms-tested-by-venn-regions` quiz 2, the pattern "`M` outside `P`
  and `S`" and the pattern "`P` inside `M` and inside `S`" both satisfy the
  premises and leave the conclusion true, so neither refutes; in
  `consistency-and-belief-sets` quiz 3 the three distractor sets each have a
  model (all true; `p` false with `r` true; everything false); in
  `fallacies-and-the-counterexample-method` quiz 3 only the last choice makes
  both letters true.

### Philosophical accuracy and fairness

- **`quantifiers-and-their-order`, example "A quantifier shift":** the
  cosmological argument was presented as committing the shift, with the hedge
  "accused of" only in `mistakes[0]`. Its defenders hold that no serious
  version takes this step and argue instead that a beginningless causal chain
  is impossible. PLAN §F requires the position in its strongest form, so the
  example now states that reply and says why it is the right kind of reply:
  it grants the verdict on the form and disputes the formalisation.
- **`truth-values-and-the-connectives`, note:** "'Because' is not
  [truth-functional], and that is why it is an argument indicator and not a
  connective" inferred too much from too little. Repaired to say what is
  true: no table can be drawn for "`p` because `q`", so the course treats the
  word as a signpost rather than a connective.
- Attributions are correct throughout: De Morgan's laws, the Boolean and
  Aristotelian readings, Barbara–Celarent–Darii–Ferio as first-figure names,
  conversion per accidens, the illicit major as AEE-1 with `P` undistributed
  in the major premise. The `not_covered` paragraph says the syllogism is
  taught as a test and not as Aristotle's system, which is the honest frame
  for a Boolean-default lab.

### Course home

- `outcomes_intro` promised the reader would "say which premise to doubt",
  which `consistency-and-belief-sets` spends a lesson explaining the logic
  cannot do. Repaired to "say what rejecting that conclusion commits you to
  giving up". The sixth outcome's title, "Refute a fallacy", did not cover the
  quantifier-order half of its body; retitled.

## Where a learner gets stuck

- **The lab says Valid before the word is defined** (`premises-conclusions-and-standard-form`).
  The `validity` kit prints a verdict tile and a form tile on every page; the
  first lesson wants only the rows. The lesson's note handles it ("The lab is
  here for its rows, not its verdicts. The word valid is defined in the next
  lesson") and that is the right handling, but a reader who skips notes meets
  "Invalid" and "no catalogued form" a lesson early. Not a defect in the
  content; recorded so nobody rewrites the kit to hide tiles per lesson.
- **"Only if" and "unless"** (`the-conditional`) remain the place a beginner
  stalls. The lesson has the right machinery: two steps that ask which part is
  required before choosing the word, a quiz item on each, and a misconception
  on reversing "only if". It is as good as prose makes this; the lab has no
  translation mode, and the next-best check is the reader's own row.
- **The Aristotelian switch on the syllogism pages** (`syllogisms-tested-by-venn-regions`)
  changes the pattern count (16 to 8 for Barbara) without the lesson saying
  so. It is not pinned and the lesson pins only the Boolean verdicts, which is
  what PLAN prescribes; a reader who flips the switch is told by the status
  line what changed. Acceptable.

## Repairs made in this pass

In `content/philosophy/c1_arguments/__init__.py`: `outcomes_intro` and the
sixth outcome's title. In `part_a.py`: `premises-conclusions-and-standard-form`
quiz 3; `validity-and-soundness` `one_line`, the `other`/`both` paragraph,
`mistakes[0]`; `truth-values-and-the-connectives` note; `the-conditional` the
rows paragraph and the lab paragraph. In `part_b.py`: `consistency-and-belief-sets`
`concepts[1]` title; `categorical-statements-and-immediate-inference` the
patterns paragraph and the conversion paragraph; `syllogisms-tested-by-venn-regions`
`concepts[1]`; `quantifiers-and-their-order` the quantifier-shift example. No
math run was added or removed, so `content/spoken/philosophy_c1_arguments.py`
needed no change; every key in it is still a live run.

Slugs, lesson count, modules, lab keys and modes are as `docs/philosophy/COURSES.json`
lists them. `scripts/preview_subject.py philosophy --course arguments-and-validity`
reports OK: 13 pages, every lab executes and survives the sweep, every pinned
figure on the eight argkit pages matches, no math run without a spoken form.

## Remaining issues

- None requires a structural change. No lesson should be split, merged or cut.
- `the-conditional` carries the most new material in the course (the table,
  four translation idioms, the converse); PLAN §C assigns all of it to this
  lesson and the quiz covers each piece, so it is left as designed. If readers
  stall here, the translation idioms are the part to move, and the natural
  home would be a lesson the URL space does not have.
- Part A writes curly quotes as entities and part B sometimes as characters.
  Both are permitted in prose fields and render identically; harmonising is
  cosmetic and was not done.
