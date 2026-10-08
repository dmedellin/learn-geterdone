# Pedagogy assessment — Ethics and the Arithmetic of Welfare (philosophy, course 6)

First assessment, formed from the twelve lesson dicts in
`content/philosophy/c6_ethics/` (`part_a.py`, lessons 1–6, and `part_b.py`,
lessons 7–12, by two authors; `__init__.py`), the spoken forms in
`content/spoken/philosophy_c6_ethics.py`, the design they were written from
(`docs/philosophy/PLAN.md` §C Course 6; §D.1 `validity`, `analysis`,
`structural`, `consistency`, `sorites`; §D.2 `aggregate`, `decide`, `commons`),
and the kits they render through (`scripts/mathpath/labs/argkit.py` and
`scripts/mathpath/labs/choicekit.py`), on branch `feat/philosophy` before the
Subject is wired into the site. No prior assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in course
order: `is-and-ought`, `defining-good-and-the-open-question`,
`utilitarianism-and-the-sum-of-welfare`,
`total-average-and-the-repugnant-conclusion`,
`priority-equality-and-levelling-down`,
`the-trolley-problem-as-a-decision-matrix`,
`kant-and-the-universalisability-test`, `double-effect-means-and-side-effects`,
`doing-allowing-and-omissions-as-causes`,
`moral-dilemmas-and-deontic-consistency`,
`virtue-ethics-and-the-function-argument`,
`slippery-slopes-and-small-differences`. The course declares Decision and
Rationality, Games and the Social Contract and Science, Induction and Causation
as what it assumes, and the path promises that each course assumes the ones
before it and nothing else, so it is judged against the five earlier courses
only.

Every figure quoted below was read off the rendered page with
`node scripts/labcheck.js --observe` (`scripts/preview_subject.py` rendering
to a scratch directory), not predicted, and then recomputed by hand. The
preview reported OK before any change was made: twelve labs execute and
survive the control sweep, twelve pages carry pinned figures and all of them
match, and no math run lacks a spoken form. It reports OK after the changes
below as well.

## What the course teaches well

- **Every lesson closes on an act the lab measures.** Produce the
  counterexample row and write the bridge (`is-and-ought`); evaluate a
  definition on every row and name each failure's direction
  (`defining-good-and-the-open-question`); rank by total and write each
  person's change (`utilitarianism-and-the-sum-of-welfare`); compute n* and
  name the rule that blocks it (`total-average-and-the-repugnant-conclusion`);
  apply a weighting and a Gini and say where they part
  (`priority-equality-and-levelling-down`); strike an act and name the case
  where the answer moves (`the-trolley-problem-as-a-decision-matrix`); compute
  the defector's two figures (`kant-and-the-universalisability-test`); write
  the equations and flip the harm (`double-effect-means-and-side-effects`);
  model the omission and flip it (`doing-allowing-and-omissions-as-causes`);
  write the five sentences and name what each exit rejects
  (`moral-dilemmas-and-deontic-consistency`); state the premise an enthymeme
  leaves out (`virtue-ethics-and-the-function-argument`); run one chain under
  four treatments (`slippery-slopes-and-small-differences`). No `standard`
  says "understand".
- **The prose figures and the lab agree, everywhere.** Observed tiles:
  `equal-vs-skewed` prints B ≻ A, 30 vs 33, Gini 0 vs 58/99; `transfer` a tie
  at 20; `sacrifice` 30 vs 31; `repugnant` n* = 301 with A ≻ B at 30 vs 6/5;
  `mere-addition` 30 vs 34; `average-trap` 11 vs 120 under total;
  `levelling-down` 27 vs 15 with Gini 0 vs 0; `levelled` 11 vs 4 with Gini
  1/3 vs 0; `priority` a tie at 17 with Gini 1/5 vs 0; `switch` divert at −1
  and `footbridge` / `loop` do nothing at −5 under the constrained rule;
  `false-promise` "alone +3, everyone −2" with the social optimum "7
  cooperate: total 77/3"; `tax` "alone +3/2, everyone −3"; `queue-jumping`
  "alone +2, everyone −3"; the four structural presets of double effect and
  the five of omissions print exactly the but-for and Halpern–Pearl verdicts
  the bodies state, including "joint cause with W2" for the boat; the dilemma
  set prints "{1, 2, 3, 4, 5}" and each single deletion a model; the
  function argument prints one counterexample row as told and none bridged;
  `weeks` prints 40 steps, "all 40 true", True classically, "one false, at
  k = 24", "16 indeterminate (17–32)" and "each 39/40" with conclusion 0 under
  the other three treatments. Every one of these numbers is the number the
  body, the worked example or the quiz states; the kit's prioritarian `g`
  was read in `choicekit.py` to confirm the one figure a quiz now asks the
  reader to compute without a preset (knee 9: 35/2 against 18).
- **The misconceptions are the PLAN's, named as models and refuted with a
  row or a number.** Hume as "moral claims are false" against the row
  `p = T, q = T, o = F` and the valid bridged form; taste against the two-of-five
  that changing the machine's verdict buys; the two-aims slogan against two of
  three people losing while the sum prefers B; averaging as a free exit against
  one at 11 beating twelve at 10; priority as equality against the two levelled
  cases; the trolley numbers against two identical tables; the Kantian test as
  a forecast against a social optimum that contains liars; intentions the lab
  can read against identical tiles for opposite intentions; omissions as
  non-causes against the lifeguard flip; a dilemma as ignorance against a
  settled set with no model; prestige as validity against the row
  `f = F, g = F, r = T`; the slope as a fallacy against a valid chain whose
  conclusion is true when the premises are.
- **Positions are stated at their strongest and the reader is left to
  choose.** The utilitarian's diminishing-returns reply and the revise-the-
  intuition reply (`utilitarianism-and-the-sum-of-welfare`); the hedonist who
  rejects a verdict and pays for it (`defining-good-and-the-open-question`);
  the egalitarian's pluralism against levelling down
  (`priority-equality-and-levelling-down`); Kant's own refusal to compute and
  the generality objection (`kant-and-the-universalisability-test`); the many
  who judge the loop permissible against the doctrine
  (`double-effect-means-and-side-effects`); the three candidate grounds for
  killing being worse than letting die, none computed
  (`doing-allowing-and-omissions-as-causes`); the sound slope about a million
  (`slippery-slopes-and-small-differences`).
- **Earlier courses are used without re-derivation and named by title.**
  The decision matrix and the expected-utility rule, the n-player game and
  its universalisation tile, the but-for test and the Halpern–Pearl witness,
  the consistency check and the smallest inconsistent subset each arrive as
  known instruments. Cross-references are by title throughout; a grep of the
  rendered fields finds no numbered reference.
- **Three deviations from the PLAN are right and should be kept.** The PLAN's
  `levelling-down` instance (10, 10, 10 against 5, 5, 5) is not a levelling-down
  case, since everyone is worse off and inequality is unchanged; the author
  kept it and added `levelled` (10, 2 against 2, 2), which is. The PLAN's
  `two-rescuers` instance R = W₁ ∨ W₂ makes each unwilling rescuer a but-for
  cause, contrary to the PLAN's own claim that "neither alone is but-for"; the
  author kept the ∨ case under its correct verdict and added `two-needed`
  (R = W₁ ∧ W₂) for the joint cause. The PLAN's `bomber` preset gained a
  `strategic-bomber` partner so the contrast the body draws is on the page.

## What the course taught badly, or wrongly

1. **A swapped attribution** (`moral-dilemmas-and-deontic-consistency`,
   `body`, `lab` labels, `quiz` items 2 and 3). The body had Marcus rejecting
   agglomeration and Williams rejecting ought-implies-can on the strength of
   remorse. Williams's "Ethical Consistency" is where the word "agglomeration"
   comes from, and his claim is that 'ought' does not agglomerate; the remorse
   argument is his reason for holding that the obligation not acted on did
   not lapse, which is why he keeps both oughts and gives up the combined
   one. Marcus's "Moral Dilemmas and Consistency" makes a different point:
   a set of rules is consistent if some world lets all of them be obeyed, so
   a dilemma is a consistent code meeting a contingent situation, and there is
   a second-order obligation to arrange one's life so that such situations are
   rare. The lab displays her point exactly: delete sentence 5 and the four
   principles have a model. The preset labelled "Marcus" and the quiz item
   that had Williams rejecting ought-implies-can would have taught two
   philosophers' positions backwards.
2. **A false explanation of a correct figure**
   (`kant-and-the-universalisability-test`, `body`). The social optimum tile
   prints "7 cooperate: total 77/3", and the body said this was "because a few
   liars profit more than the rest lose". In the PLAN's instance the honest
   payoff is the constant 2, so the honest lose nothing to anyone; the optimum
   holds liars because each gains 3 and nobody pays. That stipulation is
   generous to the liar and was not stated. Its scope matters and was also
   unstated: a table in which the deceived lose moves the optimum and leaves
   the two figures the test reads untouched, since both are read where all
   nine others are honest and where none is.
3. **The argument as told was not the argument formalised**
   (`virtue-ethics-and-the-function-argument`, `body` paragraph 1 against
   paragraph 2). Paragraph 1 told the function argument with "Reasoning is
   the human function" as its second premise; with `f → g` that is modus
   ponens and valid. Paragraph 2 then formalised "the argument as told" with
   `r`, distinctiveness, as the second premise, and found it invalid. A reader
   who had just been shown a valid version would be told the argument is
   invalid. Aristotle's actual premise is the distinctiveness one (what is
   peculiar to man, shared with neither plants nor animals), which is why the
   step from distinctive to function is the one the critics press; the telling
   now says so.
4. **The levelling-down case was misnamed**
   (`priority-equality-and-levelling-down`, `body`, `key`, `mistakes[0]`,
   `quiz` item 3, preset labels). The body introduced 10, 10, 10 against
   5, 5, 5 as "the levelling-down case" and then the real one as "the levelled
   preset"; `mistakes[0]` and quiz item 3 repeated the misnaming; the key line
   said "levelling down: equal, and worse for all", which is false of the case
   that matters, where the person at 2 is no worse off. The 5, 5, 5 case is
   useful for a different reason, that the Gini is blind to level, and is now
   introduced as that.
5. **A lab output the prose did not explain**
   (`slippery-slopes-and-small-differences`, `body`, `worked`). The range
   treatment was given one clause, "steps whose conditionals are neither true
   nor false", and the lab prints "16 indeterminate (17–32)" for a typed range
   of 16–32. The kit (read in `argkit.py`) lets an admissible sharpening put
   its cutoff at any c with lo < c ≤ hi, so the indeterminate conditionals run
   from `F(17) → F(16)` to `F(32) → F(31)`. A reader who typed 16–32 and read
   17–32 had nothing on the page to explain the shift. The body now says what
   a sharpening is and which sixteen conditionals are indeterminate, and the
   worked line matches the tile.
6. **Two tiles the lesson never mentions**
   (`utilitarianism-and-the-sum-of-welfare`, `body`). The aggregate page
   prints a Gini and a "Population at ε to beat A" on the first lesson that
   uses it; both are later lessons' instruments and the body said nothing. One
   paragraph now sends the reader forward by title. The same kind of gap in
   `kant-and-the-universalisability-test`, where "Equilibria: k* = 4" and the
   replicator share sit beside the two figures the test reads, is now closed
   by one sentence naming them as the earlier course's tiles.
7. **Quiz items with a defensible distractor or a baseless one.**
   `utilitarianism-and-the-sum-of-welfare` item 4 asked what the total "leaves
   out" and offered "the welfare of the person with least", which in the loose
   sense the lesson itself uses ("cannot see who gets what") is true; the item
   now asks which change always leaves the total unchanged, where only the
   swap does. `total-average-and-the-repugnant-conclusion` item 4 offered 61 as
   "dividing the wrong way", and no reading of the problem produces 61; it
   now offers 31 with the specific error (counting each person as a whole
   unit). `moral-dilemmas-and-deontic-consistency` item 1's first distractor
   began with a true clause ("four of the five can be true together") before
   its false conclusion; left, since the item's `why` addresses it directly.
8. **A vocabulary item where a computation belonged**
   (`priority-equality-and-levelling-down`, `quiz` item 4). "Gini is 0 exactly
   when" tested a definition. The lesson's own `mistakes[2]` says that moving
   the knee moves the tie, and nothing asked the reader to do it. The item now
   moves the knee to 9 and asks what the lab reports: B ≻ A, 18 against 35/2,
   with the `why` showing both scores.
9. **The process view of causation dismissed rather than stated**
   (`doing-allowing-and-omissions-as-causes`, `mistakes[0]`). "What an omission
   lacks is energy, and the test does not ask for any" treats a live position
   (that causes must be processes, so absences do not cause) as an oversight.
   It is now stated as a position with its price: it must say what the match
   has that the lifeguard lacks, since the drowning depends on each in the
   same way.
10. **A category confusion in a misconception's refutation**
    (`moral-dilemmas-and-deontic-consistency`, `mistakes[0]`). Deleting the
    inability sentence was described as "the case where you simply do not know
    yet whether you can manage both". A deleted sentence is not an unsettled
    one. The refutation now says what a settled set with no model is, and
    that the lab needs no truth values to report it.
11. **A verbal tic across both authors.** "The limit is stated once", "The
    lab's limit should be stated plainly", "The limit belongs here", "Three
    limits should be stated", "The lab's limit is stated plainly", "that should
    be said plainly" — six lessons announced the limit before stating it. The
    PLAN asks for the limit to be stated, not for the statement to be
    announced. Four of the six now state it directly; two distinct ones stay.
12. **One chatty opener** (`doing-allowing-and-omissions-as-causes`, `body`):
    "Actually the lifeguard is in reach and unwilling" now reads "In the case
    as it happened".

## What it claims to teach but does not, and where a learner gets stuck

- **`slippery-slopes-and-small-differences` is the Subject's first contact
  with vagueness and carries four treatments.** The `sorites` mode is first
  used here (the PLAN reuses it in Identity, Modality and Freedom and in Mind,
  Language and Meaning), so the lesson must introduce classical logic,
  epistemicist cutoffs, supervaluation and degrees from nothing, each in a
  sentence or two. The one hard idea, that the chain is valid so a premise
  must fail and the treatments disagree about which, is carried; the range
  treatment was the one a reader could not reconstruct from the page and is
  now explained. The reader is asked to read 39/40 and 0 under degrees, not to
  compute them, which is the right depth for a first contact. A lesson of its
  own on vagueness would be the structural fix; see remaining issues.
- **`priority-equality-and-levelling-down` introduces two instruments.** The
  prioritarian weighting and the Gini coefficient are both new and both
  defined here, as the PLAN requires. The load is held by one worked example
  that applies both to one pair, and by the levelled case being the only
  place the two verdicts part. With the naming fixed, the reader now meets
  "what the Gini does not measure" before "the case that separates the
  views", in that order.
- **`the-trolley-problem-as-a-decision-matrix` ships two dead tiles.** With
  one certain state, the value of perfect information prints 0 and the
  tipping probability prints a dash on every preset. The body does not
  mention them and nothing on the page explains why they are empty. Harmless,
  and a kit matter (below).
- **`kant-and-the-universalisability-test` reads two numbers off a model
  whose honest players never lose.** The lesson now says so, and says what
  that stipulation does and does not move. A second promising preset with a
  k-dependent honest payoff would make the social-optimum contrast sharper;
  not added, to keep one hard idea per lesson.

## Prerequisite order

Checked backwards across the path. `the-trolley-problem-as-a-decision-matrix`
uses the matrix of “The Decision Matrix and Dominance” and the expected-utility
rule of “Expected Value and Expected Utility”; the constrained rule is new and
defined in the lesson. `kant-and-the-universalisability-test` uses the n-player
game of “The Tragedy of the Commons” and the universalisation tile pinned in
“Public Goods and Free-Riding”. `double-effect-means-and-side-effects` and
`doing-allowing-and-omissions-as-causes` use the but-for test of “Counterfactual
Causation and the But-For Test” and the held-fixed and joint verdicts of
“Preemption, Overdetermination and Redundant Causes”.
`moral-dilemmas-and-deontic-consistency` uses the smallest inconsistent subset
of “Consistency and Belief Sets”. `is-and-ought` and
`virtue-ethics-and-the-function-argument` use nothing past “Validity by Truth
Table”. `defining-good-and-the-open-question` uses the case table of “Belief,
Truth and Justification”. The three aggregate lessons define their rules in
place. No lesson leans on a later course; the two forward references
(sufficientarianism to Justice and Collective Choice, first-order machinery
"later in the Subject") are by title and promise nothing the lesson needs.

## Philosophical accuracy, verified and left alone

- Hume's remark is paraphrased, not quoted, and correctly: the point is about
  what a deduction can deliver. Searle's derivation is compressed to three
  steps with its institutional reply and the reply to that (the "why act
  inside the institution" line) at full strength.
- Moore's open question is stated against the bachelor contrast, and the
  lesson says plainly that the lab runs the method of cases the argument
  motivates, not the argument. The experience machine is stipulated as
  desired by the one inside it, which is a legitimate reading of Nozick's
  case and the one the table needs.
- Bentham's slogan: the lesson's point that "greatest good for the greatest
  number" names two aims is right; one clause now adds that Bentham himself
  came to drop the second.
- Parfit's repugnant conclusion and mere addition are stated as he states
  them; critical-level views are named in the note as the escape not built.
- Prioritarianism against egalitarianism and the levelling-down objection are
  Parfit's distinctions; the egalitarian's pluralist reply is given.
- Foot's switch, Thomson's footbridge and loop; the lesson says people
  disagree on the loop and the double-effect lesson says many judge it
  permissible, which is what the loop was devised to show.
- Kant: the Formula of Universal Law, the two failures (contradiction in
  conception, contradiction in the will), the generality objection. The lab
  computes the practical-contradiction reading (the lie buys nothing) and the
  body says the reading is the reader's, not the output's.
- Double effect traced to Aquinas; one clause tested, proportionality and the
  act's own permissibility named as untested; the bombers are distinguished
  by dependence, not by what the pilot wants.
- Singer's pond; the three candidate grounds for the doing/allowing asymmetry
  named and none computed.
- Dilemmas: attributions corrected as above; standard deontic logic's
  building-in of both principles named as a position.
- Aristotle's function argument from Nicomachean Ethics I.7; the laughing
  objection; the doctrine of the mean declined honestly.
- Sorites: the lab's four treatments are classical logic, epistemicism (a
  sharp cutoff), supervaluationism (super-truth over admissible sharpenings)
  and Łukasiewicz degrees; "super-false" is used correctly of the universal
  tolerance premise and of the conclusion.

## The seam between part A and part B

Part A ends on the trolley with a forward reference by title to “Double
Effect, Means and Side Effects”, and that lesson refers back to the loop
"put on the forbidden list by hand". The `concepts_intro` pattern, "X supplied
Y", holds across both authors. What was missing was the bridge at the start of
part B: `kant-and-the-universalisability-test` opened on Kant with nothing to
say why deontology follows a lesson about striking an act from a table. Its
body now opens with one paragraph: the forbidden list was typed by hand; the
deontological theories are attempts to say why an act belongs on it; the next
three lessons each give one such account a checkable structure. Spelling is
consistent (British; "judgment" in both parts; "skeptic" appears in part A
only and part B does not use the word). Both authors share the "limit" tic,
now reduced. The module boundary places the trolley lesson under
Consequentialism, as the PLAN does; its body already frames the side
constraint as "the distinction deontologists draw", so the reader is handed
across rather than dropped.

## Changes made

`content/philosophy/c6_ethics/part_a.py`

- `utilitarianism-and-the-sum-of-welfare`: added that Bentham dropped the
  second clause of the slogan; added a paragraph naming the Gini and ε tiles
  as later lessons' and sending the reader forward by title; replaced quiz
  item 4 with "which change always leaves the total unchanged".
- `total-average-and-the-repugnant-conclusion`: quiz item 4's distractor 61
  replaced by 31, with the error it represents.
- `priority-equality-and-levelling-down`: key line "levelling down: more
  equal, better for no one"; the 5, 5, 5 case re-introduced as what the Gini
  does not measure and the 10, 2 against 2, 2 case as the levelling-down
  case; preset labels "Everyone brought down by half" and "Levelling down:
  the better off brought to the worse off" (ids unchanged); `mistakes[0]`
  reworded to match; quiz item 3 now names the preset by its numbers; quiz
  item 4 replaced by the knee-at-9 computation.
- `the-trolley-problem-as-a-decision-matrix`: the limit stated without
  announcing it.

`content/philosophy/c6_ethics/part_b.py`

- `kant-and-the-universalisability-test`: new opening paragraph bridging from
  the hand-typed forbidden list; the social-optimum explanation corrected and
  the constant honest payoff named as a stipulation with its scope; the
  equilibrium and replicator tiles named as the earlier course's.
- `double-effect-means-and-side-effects`: "Three limits apply."
- `doing-allowing-and-omissions-as-causes`: opener reworded; `mistakes[0]`
  states the process view as a position with its price.
- `moral-dilemmas-and-deontic-consistency`: Williams now rejects
  agglomeration on the strength of remorse; the ought-implies-can exit is
  unnamed; Marcus's consistency point added as its own paragraph tied to the
  drop-5 model; preset labels "Williams: oughts do not combine" and "Ought
  does not imply can"; quiz items 2 and 3 rewritten; `mistakes[0]` rewritten;
  the limit stated without announcing it.
- `virtue-ethics-and-the-function-argument`: the argument as told now gives
  the distinctiveness premise, so telling and formalisation agree; the limit
  stated without announcing it.
- `slippery-slopes-and-small-differences`: the range treatment explained
  with the lab's sharpening semantics and the sixteen conditionals named;
  worked line "range 16 to 32: 16 indeterminate (17 to 32), super-false".

`content/spoken/philosophy_c6_ethics.py`

- Spoken forms for the two new runs `F(17) → F(16)` and `F(32) → F(31)`,
  which the rules would otherwise read as "goes to".

No preset instance, slug, title, lesson count or `expect` changed. The
preview reports OK: thirteen pages rendered, twelve labs execute and survive
the sweep, twelve pages with pinned figures all match, no unspoken run.

## Remaining issues

- **`slippery-slopes-and-small-differences` should be two lessons.** One on
  the slope as a valid chain whose premise must fail, with the classical and
  cutoff treatments; one on vagueness proper, with supervaluation and
  degrees. The lesson count and slugs are fixed by the URL space, so this is
  recorded rather than done. Whoever writes the sorites lessons of Identity,
  Modality and Freedom and Mind, Language and Meaning should not re-introduce
  all four treatments; this lesson now carries the introduction.
- **`priority-equality-and-levelling-down` carries two instruments** by the
  PLAN's design. If the course is ever re-cut, the Gini belongs with the
  Justice and Collective Choice lesson that measures patterns, and this
  lesson would keep priority against equality with maximin as the comparison.
- **Three PLAN §C entries disagree with their own instances** and should be
  corrected by the PLAN's owner so the next author does not "fix" the course
  back: 6.5 `levelling-down` (10, 10, 10 against 5, 5, 5) is not a
  levelling-down case; 6.9 `two-rescuers` with R = W₁ ∨ W₂ makes each a
  but-for cause, not "neither"; 6.7's constant honest payoff gives the
  deceived no loss, which the lesson now has to explain.
- **Kit: tiles a mode's instance cannot populate.** The decide page prints a
  0 value of information and a dash tipping point on every certain-outcome
  preset, and the aggregate page prints a dash prioritarian verdict when a
  preset carries no knee and the reader switches rule. The banner explains
  the second; nothing explains the first. A per-cfg way to hide a tile the
  instance cannot fill would remove the noise. `@lab-arithmetic` or the kit
  owner.
- **`utilitarianism-and-the-sum-of-welfare` pins a Gini** (`equal-vs-skewed`,
  0 vs 58/99) that the lesson does not teach. Left, because it is correct,
  the lesson now says where it is read, and the same distribution's Gini is
  the one quoted in `priority-equality-and-levelling-down`.
- **`kant-and-the-universalisability-test` would be sharper with a second
  promising preset** in which the honest payoff falls with the number of
  liars, so the social optimum and the test can be seen to part for a reason
  the reader controls. Not added, to hold the lesson to one hard idea.
