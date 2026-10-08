# Pedagogy assessment — Mind, Language and Meaning (philosophy, course 9)

Formed from the ten lesson dicts in `content/philosophy/c9_mind_language/`
(`part_a.py`, lessons 1–5, the philosophy of mind; `part_b.py`, lessons
6–10, the philosophy of language; `__init__.py`, the course dict), the spoken
forms in `content/spoken/philosophy_c9_mind_language.py`, and the kits they
render through (`scripts/mathpath/labs/argkit.py` modes `kripke`,
`validity`, `semantics`, `sorites`; `scripts/mathpath/labs/choicekit.py`
mode `update`; `scripts/mathpath/labs/logic.py` `truth_table` in `two`
mode; `scripts/mathpath/labs/counting.py` rule `pr`), on branch
`feat/philosophy` before the course was wired into the site. The design
authority is `docs/philosophy/PLAN.md` §C (course 9) and §F. The course was
written by two authors, one per part, so the seam at lesson 6 is assessed
as well.

Every lesson was read in full before anything was changed. Every pinned
figure and every figure quoted in prose was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py`), not out of the kit source; where the prose
makes a claim about a control the sweep does not exercise (the second
sorites preset under the cutoff treatment, formula B of the truth table) the
kit's own function was read and the claim recomputed by hand. Lessons, in
course order: `dualism-and-the-conceivability-argument`,
`behaviourism-and-the-turing-test`, `functionalism-and-multiple-realisability`,
`the-chinese-room-and-the-lookup-table`, `the-knowledge-argument`,
`compositional-truth-conditions`, `names-reference-and-identity-statements`,
`definite-descriptions-and-the-king-of-france`,
`scope-ambiguity-and-negation`, `vagueness-and-the-sorites`. The course may
assume Identity, Modality and Freedom and, through it, the courses before;
it was judged against what those courses actually contain, not against
what their titles suggest.

## Verdict

The course teaches its subject. A reader who finishes it can build the
possible-worlds model a conceivability argument needs and point at the one
world that carries it, compute the Bayes factor of a Turing judge's answer
and say why a factor of 1 is a fact about imitation and not about thought,
write two circuits for one truth table, count a lookup table and separate
Block's device from Searle's, formalise the knowledge argument as modus
tollens and place each reply in a premise, evaluate a quantified sentence in
a finite model with its witness or failing individual, keep a name's
reference apart from its sense, expand a description in Russell's three
clauses and say what Strawson calls the empty case, give both scopes of a
negation and of a quantifier pair, and run the heap under four treatments
with the price of each. Those are the acts the `standard` fields measure and
the labs compute; none of the ten objectives is "understand X". Every
position is given its strongest form and the lab never announces a winner.
The defects found were real but local: one cross-reference to the previous
course for a doctrine that course never teaches, one lab instruction whose
"find none" would have found one row, one forward reference to a point the
cited lesson does not make, one lesson that presents as new a chain the
reader has already run twice, one pinned preset and one tile that the
lesson's prose never mentions, and three places where a position was stated
below its strength. All are repaired below. Nothing needs splitting, merging
or reordering.

## What the course teaches well

- **The thesis of the Subject is honoured in every lesson.** The lab computes
  what follows from the model, and the lesson says where the model is the
  philosophy: the second premise is the licence to add `w2`
  (`dualism-and-the-conceivability-argument`); the bridge from "who" to
  "whether" is behaviourism, named as the premise the test does not supply
  (`behaviourism-and-the-turing-test`); the ability reply denies `n` rather
  than validity, and the equivocation charge is a choice of one atom or two
  (`the-knowledge-argument`); the value tile is Russell's and the
  description tile is the fact Strawson relies on, and "which tile to treat
  as the sentence's status is the philosophical choice"
  (`definite-descriptions-and-the-king-of-france`); the reader chooses a
  treatment of vagueness "by the one they would least mind paying"
  (`vagueness-and-the-sorites`).
- **The objectives are acts.** "Say which world carries the argument",
  "count the table and say what each argument uses it for", "place a reply
  to the argument", "expand a description and name the clause that fails",
  "give both readings and a model that separates them", "run the chain four
  ways and state each price". The quizzes drill those acts: lesson 5's
  fourth item asks the reader to read the counterexample row back as a
  philosophical position, and the answer is the physicalist's picture, not a
  truth value.
- **Figures agree with the lab.** Every count and tile string in prose was
  checked against the observed page: `False at w1` and `w2` against `True at
  w1` and `all`; posteriors `1/2`, `1/10`, `1/2` and factors `1`, `1/9`;
  `4`/`0`/`Valid`/`modus tollens`, `8`/`1`/`Invalid`, `16`/`1`/`Invalid`
  and the counterexample rows `a, k` true with `n` false and `a, f, m` true
  with `l` false, recomputed by hand; `fails at x = b`, `3 of 3 satisfy`,
  `2 of 3 satisfy`, `0 of 3 satisfy`, `fails at x = a` on Twin Earth;
  `denotes nothing`, `denotes b`, `not unique: a, b`, `denotes a`; `all 10000
  true`/`True`, `one false, at k = 5000`/`False`, `150 indeterminate
  (51–200)`/`Super-false`, `each 9999/10000`/`0` and `each 999/1000`/`0`.
  The counting lab groups digits with spaces, so `36 520 347 436 056 576`
  and `13 824` in the lesson are what the page prints, and `12 144` in the
  quiz is `24 · 23 · 22` as the `why` says.
- **The misconception is `mistakes[0]` in all ten lessons, named as a model
  someone holds and refuted with the number.** The epistemic view of
  vagueness is treated as "one of the four treatments ... and it is
  defensible", and the mistake is located not in holding it but in taking it
  as the default without paying its cost. That is the PLAN §F rule done
  properly: the misconception corrected without flattening the position.
- **Positions are stated fairly.** Block's rejoinder to "the table cannot be
  built" is given (behaviourism was a conceptual claim, so an in-principle
  case refutes it). Russell's reply to Strawson is given. The dualist's reply
  to the heat precedent is given. Łukasiewicz's rule is stated correctly
  (`1 − 1/10000` per step, lower bound `max(0, 1 − steps·δ)`), the
  supervaluationist's super-falsity is described correctly (false on every
  sharpening though no single conditional is), and the cost named for each is
  the standard one (an unknowable line; a true disjunction with no true
  disjunct; artificial precision; validity that does not carry near-truth).
- **The lab's limit is stated where it matters.** "A model has the worlds you
  gave it" (lesson 1); "the probabilities in the lab are numbers someone
  chose" (lesson 2); "the circuits here have no memory" (lesson 3, note);
  "the lab has no senses to hold and no beliefs to report" (lesson 7); "the
  lab evaluates the formulas, and it does not choose between them" (lesson
  9); higher-order vagueness "is not a number the lab can print" (lesson 10).
- **Retrieval practice reaches the idea, not the vocabulary.** No quiz item
  asks for a name or a date. Lesson 6's fourth item ("I know what the sentence
  means, so I know whether it is true") tests the lesson's thesis directly;
  lesson 8's third item tests the one confusion the lesson exists to prevent
  (Russell and Strawson swapped); lesson 2's fourth item asks for the
  prior-heavy posterior, which a reader who memorised `1/10` gets wrong.
- **Cross-references are by title throughout**, and the only numbers in the
  modules are in Python docstrings that never render.

## What it taught badly, or said wrongly

### A prerequisite claimed that the earlier course does not teach

- **`dualism-and-the-conceivability-argument`, `concepts[0]`:** "This is the
  necessity of identity met in Identity, Modality and Freedom." That course
  teaches the box semantics, frames and axioms, and in “Leibniz's Law and the
  Masked Man” the indiscernibility of identicals; it never states that a true
  identity holds at every world. A reader sent back to look for it would not
  find it. Repaired: the concept now says the necessity of identity is what
  the argument's own fourth step asserts, that it extends Leibniz's law from
  properties to worlds, and that the earlier course supplies the instrument,
  not the doctrine.
- **Same lesson, body:** the physicalist was given one reply (the heat
  precedent, at the second step) when the position's older and still-live
  reply is at the fourth: the first identity theorists held the identity
  contingent, as lightning and electrical discharge were taken to be. PLAN §F
  asks for positions at their strongest. A new paragraph states the
  contingent-identity reply, gives Kripke's answer to it (an identity between
  two things each named for what it is cannot hold here and fail elsewhere),
  and says why the lab therefore writes the identity as a necessity. Quiz 2's
  first distractor, "Identical things are necessarily identical", is now a
  premise the reader has met rather than a stray slogan.
- **Same lesson, `mistakes[0]`:** "The argument is valid if the world may be
  added" conflated validity with the truth of the second premise, in the one
  Subject where that distinction is the whole first course. Repaired to "goes
  through if the world may be added, and nothing else in it does any work".

### A lab instruction that would have failed

- **`functionalism-and-multiple-realisability`, `panel_intro`:** "set A to
  the formula with a negation at each input and find none." Formula B is
  `p ∧ (q ∨ r)` and stays so unless the reader changes it; `¬(¬p ∨ ¬q)` is
  `p ∧ q`, which differs from B in the row `p = T, q = F, r = T`. The lab
  would have printed "Not equivalent" and named that row, directly under an
  instruction promising none. Repaired: the instruction now has the reader
  set B to `p ∧ q` first.

### Prose that pointed at the wrong lesson, or at none

- **`functionalism-and-multiple-realisability`, `mistakes[1]`:** said the
  weakness of a test that skips an input is what “The Chinese Room and the
  Lookup Table” presses. It is not: Block's table covers every conversation
  of its length and passes on all of them; its argument is about what passing
  shows, not about untried inputs. The lesson that is in that position is
  “Behaviourism and the Turing Test”, whose judge hears ten answers. The
  reference now points there and says why.
- **`compositional-truth-conditions`:** the `everyone-loves` preset is
  pinned (`True`, `3 of 3 satisfy`) and the body never mentioned it, and the
  fourth tile, "The outermost quantifier", was never explained anywhere in
  the five `semantics` lessons. A new paragraph introduces nested quantifiers
  through the ring, reads the tile as a count of passes (3 of 3 in the ring,
  3 of 3 for the planets, 2 of 3 once `bc` is removed) and says that the
  order question is left to “Scope Ambiguity and Negation”, which then opens
  on the same ring.
- **`scope-ambiguity-and-negation`:** the `∀x ∃y` against `∃y ∀x` contrast
  was taught in Arguments and Validity (“Quantifiers and Their Order”, on a
  grid) and the lesson did not say so. One clause now names it, so the reader
  knows this is the earlier result in a model they can type rather than a new
  one.

### A lesson that misplaced itself in the path

- **`vagueness-and-the-sorites`, `concepts_intro`:** "Here it is run once, in
  a lab that treats vagueness four ways." The reader has already run the
  `sorites` lab under all four treatments in “Slippery Slopes and Small
  Differences” (Ethics and the Arithmetic of Welfare) and under three in “The
  Ship of Theseus” (Identity, Modality and Freedom). Presenting the
  treatments as new misjudges the load (it is lower than the lesson implies)
  and hides what the lesson actually adds: the heap as the original case,
  the treatments as rival accounts of what vagueness is, and higher-order
  vagueness. The intro now says all three and names the two earlier lessons
  by title. The body, which already does the new work well, needed no change
  beyond the next item.
- **Same lesson, the cutoff paragraph:** "the verdict is the same for all of
  them" was true but gave the reader nothing to check, and the second preset
  (`heap-cutoff`) existed without the prose saying what it is for. The
  sentence now reads the tiles: the first preset reports `one false, at
  k = 5000`, the second moves the cutoff to 1000 and the false conditional
  moves with it, and the conclusion is False under both. (The second preset's
  pinned tiles are the degrees tiles, because the treatment menu is
  redraw-only and the page opens on degrees; that is PLAN §D.0's rule and
  the `panel_intro` already explains it.)

### Positions stated below their strength

- **`behaviourism-and-the-turing-test`, body:** "Turing's proposal is that
  behaviourism be put to work" attributed the doctrine to Turing, who set the
  question "can machines think?" aside as too ill-defined to discuss rather
  than answering it behaviourally. The paragraph now says the game replaces
  the question, that Turing declined the original, and that reading the game
  as a test of thought is behaviourism put to work, which is the reading the
  lesson examines.
- **`the-chinese-room-and-the-lookup-table`, body:** Searle was given the
  systems reply and no rejoinder, and "the room has rules, so it need not be
  large" was a claim about size the lesson could not support. The paragraph
  now says the room's size is the size of its rulebook rather than the number
  of conversations (which is the point the count makes), and gives Searle's
  rejoinder to the systems reply: let the person memorise the rulebook, so
  the system is the person, who still understands nothing. The lesson still
  does not choose.

### Quiz items

Every distractor in the course was argued for and none could be defended.
The ones that looked closest were checked by hand: in lesson 3 quiz 1, the
row `p = T, q = F, r = F` has both formulas false and the row `p = F` has both
false, so neither distractor names a differing row; in lesson 4 quiz 1,
`12 144` is `24 · 23 · 22` and `576` is two turns; in lesson 5 quiz 1, "the
conclusion mentions physicalism and the premise does not" is false of
`a → ¬n`; in lesson 8 quiz 1, "nobody who is a king is not bald" is the
vacuous universal and not the expansion; in lesson 10 quiz 3, keeping
classical logic is the cutoff view's benefit and the `why` says so. No item
tests vocabulary.

### The seam between part A and part B

Both parts use British spelling (behaviourism, realisability, formalise,
recognise), both cite lessons in curly quotes and courses by name, and both
end each body with the lab's limit. Part A writes curly quotes as `&ldquo;`
entities in prose fields and part B sometimes writes them as characters; the
renderer treats both identically. The one real seam was that lesson 6 opened
as "the first lesson of the language half" with no word about the half just
finished, so a reader stepped from Mary's room into a model of planets with
no reason given. The `concepts_intro` now says what the two halves share: in
both, a claim is evaluated in a model, and the philosophy is in the choice of
model. Lesson 3's `mistakes[1]` and lesson 6's new paragraph also give part A
a forward link into part B and part B a backward link into part A, so the
course reads as one.

### Philosophical accuracy, checked and found sound

Kripke's heat precedent and the dualist's reply to it; Block's Blockhead
argument and his answer to the nomological-impossibility objection; Jackson's
Mary as modus tollens, the Lewis–Nemirow ability hypothesis as a denial of
the second premise, and the two-senses reply as the charge of equivocation;
Frege on sense and reference with the Hesperus/Phosphorus case; Putnam's Twin
Earth as a claim about speakers that the lab only illustrates; Russell's
three clauses and his use of scope to defend excluded middle; Strawson's
presupposition failure; `∃y ∀x` implying `∀x ∃y` and not conversely;
Łukasiewicz degrees with the chained-modus-ponens lower bound; the
supervaluationist's super-falsity; the epistemicist's margin-for-error
defence; higher-order vagueness as the shared residue. The course home's
`not_covered` correctly names what is left out (the hard problem as a whole,
the causal theory of reference, quantified modal logic, supervaluation
proper).

## Where a learner gets stuck

- **`names-reference-and-identity-statements` carries the most.** Frege's
  puzzle is the hard idea; Twin Earth is a second one, prescribed by PLAN §C
  as a preset pair with one sentence and two extensions. The lesson confines
  Putnam to one paragraph, one preset pair and one `mistakes` entry, and
  frames him as "the same gap from the other side", which is the right
  handling; a reader who finds the lesson long should read the Twin Earth
  paragraph as an illustration of the one point (extension is fixed by the
  model, not by the sentence) and not as a new theory. Left as designed.
- **The sorites page opens on degrees.** A reader who arrives from the two
  earlier `sorites` lessons, both of which open classically, meets `each
  9999/10000` and `0` first. The `panel_intro` says so and the body treats
  classical first, so this is a one-line surprise rather than a stall, and
  the choice is PLAN's: the degrees verdict is the one this lesson is built
  to show.
- **The equivocation preset's three atoms** (`f`, `l`, `m` with `a → ¬(f ∧
  l)`) are the densest formalisation in the course. The body spells out what
  each letter says, the panel has the reader type `l` for `m` and watch
  validity return, and quiz 4 asks for the counterexample row as a
  philosophical picture. It is as good as prose makes this; nothing to move.

## Repairs made in this pass

In `content/philosophy/c9_mind_language/part_a.py`:
`dualism-and-the-conceivability-argument` `concepts[0]`, a new body
paragraph on the contingent-identity reply, `mistakes[0]`;
`behaviourism-and-the-turing-test` the Turing paragraph;
`functionalism-and-multiple-realisability` `panel_intro` and `mistakes[1]`;
`the-chinese-room-and-the-lookup-table` the Searle paragraph. In
`part_b.py`: `compositional-truth-conditions` `concepts_intro` and a new
body paragraph on nested quantifiers and the outermost-quantifier tile;
`scope-ambiguity-and-negation` the two-quantifier paragraph;
`vagueness-and-the-sorites` `concepts_intro` and the cutoff paragraph. No
change to `__init__.py` was needed: the course home's objectives, key lines,
`assumes_long`, `not_covered` and `how_to` were checked against the lessons
and hold. The two math runs added (`∀x ∃y Loves(x, y)`, `k = 5000`) read
correctly under the speech rules, so `content/spoken/philosophy_c9_mind_language.py`
needed no change; every key in it is still a live run.

Slugs, lesson count, modules, lab keys and modes are as
`docs/philosophy/COURSES.json` lists them. `scripts/preview_subject.py
philosophy --course mind-language-and-meaning` reports OK: 11 pages, every
lab executes and survives the sweep, every pinned figure on the eight
argkit/choicekit pages matches, no math run without a spoken form.

## Remaining issues

- None requires a structural change. No lesson should be split, merged or
  cut.
- `names-reference-and-identity-statements` is the heaviest lesson, for the
  reason given above. If readers stall there, the Twin Earth material is the
  part to move, and its natural home would be a lesson on externalism that
  the URL space does not have and PLAN §G does not plan.
- `functionalism-and-multiple-realisability` and
  `the-chinese-room-and-the-lookup-table` use kits outside
  `KITS_WITH_EXPECTATIONS` (`truth_table`, `counting`), so their pages carry
  no pinned figures and labcheck only sweeps them. The figures the prose
  quotes (`13 824`, `36 520 347 436 056 576`, the three true rows `TTT TTF
  TFT`) were verified by hand and against the kit's grouping function; they
  are not gated.
- The `heap-cutoff` preset's pinned tiles are necessarily the degrees tiles
  (redraw-only treatment menu). The cutoff verdict it exists to show is
  therefore stated in prose and checked by hand, not pinned. This is a
  property of the §D.0 convention, not of the lesson.
