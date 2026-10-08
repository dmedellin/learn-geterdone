# Pedagogy assessment — Identity, Modality and Freedom (philosophy, course 8)

First assessment, formed from the twelve lesson dicts in
`content/philosophy/c8_metaphysics/` (`part_a.py`, lessons 1–6, one author;
`part_b.py`, lessons 7–12, another; `__init__.py`, the course home) and the
spoken forms in `content/spoken/philosophy_c8_metaphysics.py`, on the branch
`feat/philosophy`, against the design in `docs/philosophy/PLAN.md` §C
(course 8), §D (`kripke`, `sorites`, `consistency`, `structural`, the reused
`relation` kit) and §F, and against what the two courses it may assume
actually teach. Every lesson was read in full before anything was changed.
Every page was rendered with `scripts/preview_subject.py`, every pinned tile
was checked by `labcheck.js`, and every figure the prose quotes that is NOT
pinned (the relation grid's counts and failing pair, the sorites tiles under
the cutoff and degree treatments, the frame tiles of the consequence-argument
presets) was read off the rendered page with `node scripts/labcheck.js
--observe`. The twelve slugs, in course order:
`necessity-possibility-and-possible-worlds`,
`frames-axioms-and-what-necessity-obeys`,
`modal-fallacies-and-the-sea-battle`, `the-ontological-argument-in-s5`,
`leibnizs-law-and-the-masked-man`, `the-ship-of-theseus`,
`personal-identity-and-psychological-continuity`,
`fission-and-what-matters`, `free-will-determinism-and-compatibility`,
`the-consequence-argument`,
`frankfurt-cases-and-the-ability-to-do-otherwise`,
`the-problem-of-evil-as-an-inconsistent-set`.

The verdict first: the course teaches its subject. Its organising act is the
one §0 asks for — put the position in a form the lab can compute, read the
verdict, then say which premise or which frame the verdict rests on — and it
is carried through all twelve lessons by both authors. Every `standard` names
an act the closing quiz measures; every lab computes what the prose says it
computes, to the string; the modal logic is right (the correspondence table,
the euclidean condition for `◇□G → □G`, the reflexive-plus-euclidean equals
equivalence step, K on every frame); the positions that matter (the fatalist,
the modal theist, Reid, Parfit, the compatibilist, Lewis, Frankfurt, Mackie
and Plantinga) are argued rather than announced; and the seam between the two
authors is nearly invisible — the second author picks up the first's
vocabulary (arcs, sees, valuation, the drop menu, the witness) without a
restatement. The defects found were local: one quiz distractor that is a
logical equivalent of a sentence in the set, one quiz question that asks about
memory in the wrong direction, one misattribution (omniscience put into
Mackie's set), one wrong description of the privation view, one modelling
inconsistency in the consequence-argument presets (an operator defined as
truth-entailing modelled on a frame where it is not), one forward reference
to lessons not yet read, one positional cross-reference, one muddled sentence
about what the three sorites treatments give up, one strongest-form gap (the
agglomeration objection to the transfer rule named but not shown), and some
loose wording. All are fixed below. Nothing needs splitting or merging, and
the URL space is untouched.

## What the course teaches well

- **The objective is observable in every lesson and it is the right one.**
  Compute a box and a diamond from a diagram and name the arc that changed the
  verdict (`necessity-possibility-and-possible-worlds`); read the axiom list
  off a set of arcs and add one arc to make a chosen axiom appear
  (`frames-axioms-and-what-necessity-obeys`); show with a model that the box
  does not distribute over a disjunction (`modal-fallacies-and-the-sea-battle`);
  say which frame property the argument needs and which premise is left
  (`the-ontological-argument-in-s5`); show two true sentences differing under
  a box and say why the law is untouched (`leibnizs-law-and-the-masked-man`);
  write the puzzle as a chain and say what each treatment commits you to
  (`the-ship-of-theseus`); give a non-transitive tie, build its closure, name
  the stages continuous but not connected
  (`personal-identity-and-psychological-continuity`); write the set, name the
  minimal inconsistent subset, state what each deletion yields
  (`fission-and-what-matters`, `free-will-determinism-and-compatibility`,
  `the-problem-of-evil-as-an-inconsistent-set`); show the transfer step valid
  on every frame and name what each reply rejects (`the-consequence-argument`);
  build the model and report both tests of cause
  (`frankfurt-cases-and-the-ability-to-do-otherwise`). No "understand"
  anywhere, and the five course outcomes in `__init__.py` are the same acts at
  course grain.
- **The one hard idea per lesson is respected, and the first author sequences
  the modal half as PLAN §C asks.** Evaluation at a world; then validity on a
  frame and the correspondence; then one scope fallacy; then one argument whose
  validity turns on a frame property; then one opaque context. Each lesson's
  `concepts_intro` says what the previous one supplied and what this one adds.
  The second author does the same for the identity and freedom halves: a tie
  and its closure, then the fork, then the triad, then the triad's best
  support, then the premise that support needed, then the method once more.
- **The labs compute what the prose says, to the string.** All 39 pinned
  tiles match. The figures that cannot be pinned (rule 6 of
  `scripts/mathpath/AGENTS.md`) were read off the page: the `relation` grid
  under `succ` holds 4 pairs, its transitive row reports `(1, 2) and (2, 3) ∈
  R but (1, 3) ∉ R`, the transitive closure marks 6 cells amber and leaves the
  count at 4, and the status line reports equivalence classes only for an
  equivalence relation — all exactly as
  `personal-identity-and-psychological-continuity` says. The sorites page under
  the moved treatment menu prints `one false, at k = 500` / `False` and `each
  999/1000` / `0`, as `the-ship-of-theseus` says. The author of that lesson
  correctly declined PLAN's `cutoff-half` and `degrees` presets, because the
  treatment is a redraw-only select and a preset cannot move it (§D.0); the
  `note` says so.
- **The logic is right, and it is reasoned, not announced.**
  `frames-axioms-and-what-necessity-obeys` derives T and 4 from the arcs in
  prose before the table; `the-ontological-argument-in-s5` gives the short
  proof that the conditional holds on euclidean frames and the countermodel on
  the S4 frame; `the-consequence-argument` gives the three-line reason K holds
  on every frame. I checked each: `◇□p → □p` is valid on exactly the euclidean
  frames (it is the dual form of 5), reflexive plus euclidean is an
  equivalence relation, and the cycle frame validates D alone.
- **Positions are stated at their strongest and the lab's limit is stated
  where it is leaned on.** The fatalist is given the repair `p → □p` and told
  what accepting it costs; the modal theist is told that granting `◇□G` in S5
  is not a modest concession, and the critic is given two exits that are each
  arguments; Lewis's weak ability is stated correctly (I can act such that a
  law would have been broken, though I cannot break a law); Frankfurt's case
  carries both the flicker objection and the dilemma defence; the free-will
  defence is held to what it claims (possibility, not truth) and the
  evidential problem is given its support and its skeptical-theist reply.
  Every lesson's `note` says what the lab cannot decide.
- **Retrieval practice addresses the specific error.** Each quiz `why`
  explains every wrong choice; the `standard` bodies end with the shape of an
  answer that has not been computed ("a verdict stated without the list of
  worlds it consulted", "a deletion named without the model it yields").
- **The voice holds.** Careful prose throughout; no "in this lesson you
  will"; cross-references by title. The second author's "a spare tyre in the
  boot does not take over from the tyre that carried the car" is the
  library's register.

## What the course teaches badly, or got wrong

- **A quiz distractor that is true** (`fission-and-what-matters`, quiz 2).
  Choice four, "A is me only if B is not", is `ia → ¬ib`, which is the
  one-one sentence `¬(ia ∧ ib)` itself; the `why` then asserts that the
  one-one sentence "is not a conditional on A", which is false. A reader who
  chose it was right and was told they were wrong. Rewritten to a choice the
  set does refute, with a `why` that cites the model the lab prints.
- **A quiz question that reads memory backwards**
  (`personal-identity-and-psychological-continuity`, quiz 1). "Does stage 1
  remember stage 3?" — under the lesson's own convention a later stage
  remembers an earlier one, so the answer "no" is right for a reason the
  lesson never taught. Rewritten to ask whether `(1, 3)`, stage 3 directly
  remembering stage 1, is in the grid.
- **A misattribution** (`the-problem-of-evil-as-an-inconsistent-set`).
  Mackie's set is omnipotent, wholly good, evil exists, plus two
  "quasi-logical" rules; omniscience is a later addition. The lesson called
  the five-sentence set "Mackie's version". Rewritten to state his set and say
  what the lesson's set adds and why.
- **The privation view misdescribed** (same lesson). Dropping "evil exists"
  was glossed as "evil is an illusion or a privation". The privation view does
  not deny that evil exists; it says what evil is. The clause is removed.
- **A modelling inconsistency** (`the-consequence-argument`). `N p` is
  defined as "`p`, and no one has power over `p`", so a frame modelling `N`
  has every world seeing itself; but the presets that evaluate a premise left
  w1 without an arc to itself, and in `premise-two` the act `a` was false at
  w1 — the libertarian's picture had the agent not acting. Fixed: the three
  premise presets give w1 the arc to itself and make the act actual; the
  worked example is redone on the reflexive frame; the body says why. The
  transfer preset is untouched, because K needs no arc. Pinned tiles were
  re-read after the change.
- **A strongest-form gap** (same lesson). The "third place to push" said
  that powerlessness "need not combine across independent facts" without
  showing a case. The objection's strength is the untossed coin: no power
  over its not landing heads, none over its not landing tails, power over its
  not doing both — so `N` fails agglomeration, which every box satisfies.
  Added, with the defender's reply (redefine `N` as a box over the regions of
  possibility anyone can reach, then argue the premises under that reading).
- **A forward reference** (`fission-and-what-matters`, `concepts_intro`).
  "The same method as the free-will triad, the regress and the problem of
  evil" names two lessons the reader has not reached. Rewritten to name
  “Consistency and Belief Sets” and “The Regress of Justification”, which the
  reader has done, and to say two later lessons use it again.
- **A positional cross-reference** (`frames-axioms-and-what-necessity-obeys`,
  `concepts_intro`): "The first lesson fixed the meaning of the box" — a
  number in disguise. Now "the previous lesson".
- **A muddled sentence** (`the-ship-of-theseus`, mistake 2). "The three
  treatments are three things to give up: the bivalence of `F`, one
  conditional, or the full truth of each" lists the degree treatment twice
  and the classical treatment not at all. Rewritten: classical gives up
  nothing and accepts `F(0)`; cutoff gives up one conditional; degrees give
  up the full truth of every conditional.
- **The seam between the authors was a hard cut at lesson 6.** Lesson 5 ends
  the modal module and lesson 6 begins with "The ship of Theseus is a sorites
  in disguise" with no turn from worlds to time. One sentence added to the
  `concepts_intro` of `the-ship-of-theseus` makes the turn. Lesson 7's
  intro already looks back at the ship; from there on each lesson picks up
  the last.
- **Loose wording.** `modal-fallacies-and-the-sea-battle` quiz 3, choice
  four, read "p is true at w2, w3 and w4 except w4"; now "true at w2 and w3
  and false at w4". `the-ontological-argument-in-s5` quiz 3 had "a theist"
  deny the possibility premise, which puzzles the reader for no reason; now
  "a critic". `the-consequence-argument` defined `h` to include the laws and
  then introduced `l` for the laws; now `h`, `l` and `a` are introduced
  together. `fission-and-what-matters` said "three things are hard to deny
  together" and in the next sentence "these are the five sentences" without
  saying that the sufficiency claim is split over the two survivors; now it
  does, and "sentence 5 denies both" is now "denies their conjunction".
  `the-problem-of-evil-as-an-inconsistent-set` step 2 said "the subset names
  what must be given up from"; rewritten.

## What it claims to teach but does not

Nothing of substance. The course home's five outcomes are each delivered by
the lesson that names them. One small gap: the home's `assumes_long` names
Arguments and Validity and Science, Induction and Causation, but
`the-ship-of-theseus` points the reader to “Slippery Slopes and Small
Differences” in Ethics and the Arithmetic of Welfare as "the same chain". The
lesson builds the chain from nothing, so the pointer is not a dependency, and
Ethics precedes this course in the path; left as is and recorded here.

## Where a learner gets stuck

- **Vacuous boxes.** Every kripke lesson has worlds that see nothing, and
  the `krWorlds` tile lists them as worlds where the formula holds. The first
  lesson teaches this on purpose (`blind`), and lessons 3, 5 and 10 each carry
  a `note` saying "read the value at w1". That is the right handling; the
  reader who skips the note will be puzzled once and then not again.
- **`the-consequence-argument` is the densest lesson.** K, three replies
  (Lewis, the libertarian, the operator objection) and the agglomeration case
  in one page. It is the lesson PLAN §C specifies and each piece is needed to
  state the argument at its strongest, so it stays; a reader should expect to
  take it in two sittings. Recorded below as the one candidate for a split if
  the lesson count were ever reopened.
- **Minimal inconsistent subsets.** `fission-and-what-matters` defines the
  term in a `def` block; `free-will-determinism-and-compatibility` and
  `the-problem-of-evil-as-an-inconsistent-set` use it without repeating the
  definition. The order is right for a reader going forward.

## Misconceptions

All twelve `mistakes[0]` entries are the §C misconception for that lesson,
named as a model someone holds and refuted with the specific preset, world or
row. The second and third entries are good and specific throughout; two were
improved: the consequence argument's third mistake, which repeated a point
about reflexivity that now lives in the body, is replaced by the error of
drawing the arcs of `N` to every logically possible world (which falsifies
the first premise before anyone has argued against it), and the ship's second
mistake is corrected as above.

## Changes made

In `content/philosophy/c8_metaphysics/part_a.py`:
`frames-axioms-and-what-necessity-obeys` concepts_intro;
`modal-fallacies-and-the-sea-battle` quiz 3 choice;
`the-ontological-argument-in-s5` quiz 3 stem; `the-ship-of-theseus`
concepts_intro (the seam) and mistake 2.

In `content/philosophy/c8_metaphysics/part_b.py`:
`personal-identity-and-psychological-continuity` quiz 1;
`fission-and-what-matters` concepts_intro, two body sentences, quiz 2;
`the-consequence-argument` first two body paragraphs, the third-place
paragraph (agglomeration), presets `premise-one`, `premise-two`, `both-hold`
(w1 sees itself; the act is actual), panel_intro, worked example, mistake 3;
`the-problem-of-evil-as-an-inconsistent-set` the Mackie paragraph, the
deletions paragraph, step 2.

`content/spoken/philosophy_c8_metaphysics.py`: unchanged. The preview's
read-out check reported no unspoken or guessed-at run after the edits, so no
entry was needed.

Verification: `scripts/preview_subject.py philosophy --course
identity-modality-and-freedom` reports OK after the changes; the three
altered presets were re-observed and their pinned strings confirmed.

## Remaining issues

- `the-consequence-argument` carries more than one hard idea (K; the two
  premise denials; the operator objection). It is what PLAN specifies and the
  pieces are inseparable for a fair statement, but if the lesson count is
  ever reopened it is the one lesson in this course that would benefit from a
  split into "the transfer step is K" and "where to push".
- The `relation` kit is not in `KITS_WITH_EXPECTATIONS`, so the four figures
  `personal-identity-and-psychological-continuity` quotes from it are checked
  by this assessment and by nothing automated. A future conversion of that
  kit should pin `relCount` under `succ` (`4`).
- The sorites figures under the cutoff and degree treatments are unpinnable
  by rule 6 and are quoted in `the-ship-of-theseus`; the `note` says so. If
  `soTreat` ever becomes preset-driven, pin `soCond` and `soConc` for both.
