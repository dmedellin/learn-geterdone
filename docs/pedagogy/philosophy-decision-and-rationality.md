# Pedagogy assessment — Decision and Rationality (philosophy, course 4)

First assessment, formed from the ten lesson dicts in
`content/philosophy/c4_decision/` (`part_a.py`, lessons 1–5, and `part_b.py`,
lessons 6–10, by two authors; `__init__.py`), the spoken forms in
`content/spoken/philosophy_c4_decision.py`, the design they were written from
(`docs/philosophy/PLAN.md` §C Course 4, §D.2 `decide` and `series`, §D.3
`relation`), and the kits they render through (`scripts/mathpath/labs/choicekit.py`
and the relation grid in `scripts/mathpath/labs/sets.py`), on branch
`feat/philosophy` before the Subject is wired into the site. No prior
assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in course
order: `preference-transitivity-and-the-money-pump`,
`the-decision-matrix-and-dominance`, `maximin-maximax-and-minimax-regret`,
`expected-value-and-expected-utility`,
`risk-aversion-and-the-value-of-information`,
`the-allais-paradox-and-the-sure-thing-principle`,
`ambiguity-and-the-ellsberg-urn`, `pascals-wager`, `newcombs-problem`,
`the-st-petersburg-game`. The course declares Knowledge and Evidence as its
prerequisite ("credence as a degree of belief and the rule that probabilities
add to 1"), and the path promises that each course assumes the ones before it
and nothing else, so the course is judged against Arguments and Validity,
Knowledge and Evidence and Science, Induction and Causation only.

Every figure quoted below was read off the rendered page with
`node scripts/labcheck.js --observe` (`scripts/preview_subject.py` rendering
to a scratch directory), not predicted, and then recomputed by hand. The
preview reported OK before any change was made: ten labs execute and survive
the control sweep, nine pages carry pinned figures and all of them match, and
no math run lacks a spoken form.

## What the course teaches well

- **Every lesson closes on an act, and the act is the one the lab measures.**
  Build a cycle and price a lap (`preference-transitivity-and-the-money-pump`);
  lay out a table and name the dominated act with the column that shows it
  (`the-decision-matrix-and-dominance`); score one table three ways and name
  the state that drives the disagreement (`maximin-maximax-and-minimax-regret`);
  score two acts and solve for the flip (`expected-value-and-expected-utility`);
  show a sure thing beating a fair gamble and price a forecast
  (`risk-aversion-and-the-value-of-information`); show a pair of choices breaks
  expected utility (`the-allais-paradox-and-the-sure-thing-principle`); show two
  choices fit no single credence (`ambiguity-and-the-ellsberg-urn`); compute a
  threshold and say what removes it (`pascals-wager`); compute both verdicts
  and the accuracy at which they part (`newcombs-problem`); sum the game and
  price it against a bank (`the-st-petersburg-game`). No `standard` says
  "understand".
- **One table carries the whole course.** The umbrella (take 2, 1; leave −3, 3)
  is laid out in `the-decision-matrix-and-dominance`, scored three ways in
  `maximin-maximax-and-minimax-regret`, given a probability and a tipping point
  of 2/7 in `expected-value-and-expected-utility`, and priced for a perfect
  forecast at 4/3 in `risk-aversion-and-the-value-of-information`. A reader
  meets each new rule on numbers already known, which is what keeps the load to
  one idea a lesson.
- **The prose figures and the lab agree, everywhere.** Observed tiles:
  `umbrella-p` prints take, 4/3, flip at p(rain) = 2/7; `insurance` prints
  insure, VPI 3/4, flip at p(fire) = 1/5; `fair-gamble` prints keep, flip at
  p(heads) = 2/3; `allais-a` prints B at 103/10 and `allais-b` D at 7/5, both
  gaps 3/10; `ellsberg-1` red at 1/3 and `ellsberg-2` black or yellow at 2/3;
  `pascal` a tie at 0 with the flip at 1/1000 and `pascal-wins` 1/1000;
  `newcomb-90` one-box at 900000, `newcomb-coin` two-box at 501000, the
  threshold preset a tie at 500500; `cap-1024` a partial sum of 43/4 against a
  limit of 11 and `cap-million` 20 against 21. Every one of those numbers is
  the number the body, the worked example or the quiz states. The panel
  instructions ("change 1/3 to 1/5 and the choice turns to leave", "change the
  14 to 21/2 in both presets", "change the probabilities to 2/1000, 1/1000,
  997/1000 and the tie breaks for A", "change the bankroll to 2048 and the
  limit moves to 12") were each recomputed and each does what it says.
- **The misconceptions are the PLAN's, named as models and refuted with a
  number.** Transitivity as taste is refuted by 3ε a lap whatever the options
  (`preference-transitivity-and-the-money-pump`); best cell as best act by the 3
  and the −3 in the same row (`the-decision-matrix-and-dominance`); regret as
  "maximin on another table, stop there" by the shifted column that moves
  maximin and not regret (`maximin-maximax-and-minimax-regret`); expected value
  as the value you expect by an act that pays 2 or 1 and scores 4/3
  (`expected-value-and-expected-utility`); refusing a fair bet as irrational by
  8 against 10 under the square root (`risk-aversion-and-the-value-of-information`);
  the certainty premium by B at 103/10 over A at 10
  (`the-allais-paradox-and-the-sure-thing-principle`); ambiguity aversion as
  risk aversion by the common factor that cannot reorder red and black
  (`ambiguity-and-the-ellsberg-urn`); ignoring a tiny probability by the 1/1000
  that wagering wins by (`pascals-wager`); the record as irrelevant or decisive
  by 101,000 against 900,000 and the 1001/2000 threshold (`newcombs-problem`);
  infinite expectation as "pay any price" by 11 and 21 (`the-st-petersburg-game`).
- **Positions are stated at their strongest, and the lesson does not announce
  a winner.** The multi-criteria objection to the money pump gets its hearing
  and its cost (`preference-transitivity-and-the-money-pump`); the regret
  defence of the Allais pattern is given and then asked to say what the outcome
  is (`the-allais-paradox-and-the-sure-thing-principle`); the Ellsberg lesson
  builds the worst-case rule that reproduces the pattern, shows it in the lab
  under maximin, and states what it pays for that; the one-boxer and the
  two-boxer each get a valid argument and the disagreement is located in a
  premise (`newcombs-problem`); the St Petersburg lesson names the harder
  position, that the uncapped game is coherent and the rule is wrong on it.
- **Each lesson states the lab's limit where it leans on it.** The lab cannot
  say a soaking is worth −3 (`the-decision-matrix-and-dominance`, `note` of
  `expected-value-and-expected-utility`); the square root is one curve among
  many (`risk-aversion-and-the-value-of-information`); the lab cannot take an
  infinity (`pascals-wager`); the causal alternative is not built
  (`newcombs-problem`); the bounded utility is described and not computed
  (`the-st-petersburg-game`).
- **Cross-references are by title, never by number**, in both parts; spelling
  is British in both; the `x` shorthand reads as sentences and every run has a
  spoken form.

## What the course teaches badly, or claims and does not teach

- **A distractor that is true** (`risk-aversion-and-the-value-of-information`,
  quiz 4). "It can exceed the largest payoff in the table" is offered as false
  and explained as "bounded by the largest payoffs". It is not: with payoffs
  (−100, 0) and (0, −100) at even odds the expected best is 0, the best expected
  is −50, and the VPI is 50, above every cell. A reader who thinks of a loss
  table is marked wrong for being right. Replaced by a distractor that is false
  everywhere (the VPI as "the probability the forecast turns out right"), with
  the `why` rewritten to say what kind of quantity it is.
- **A prerequisite the path does not have**
  (`preference-transitivity-and-the-money-pump`, `note`). "Transitivity is the
  property you already met there", of the Discrete Mathematics path. The
  Philosophy path promises that each course assumes the ones before it and
  nothing else; the lesson defines transitivity itself and should say that
  nothing from the other path is assumed. Reworded.
- **A sentence that misplaces the disagreement** (`newcombs-problem`, body).
  "The two rules disagree only in the middle. A predictor right less than about
  half the time gives both rules the same answer." The rules agree for every
  accuracy up to 1001/2000 and part for every accuracy above it, which is not
  "the middle" and not "about half" in the direction the words suggest. The
  surrounding paragraphs and the threshold tile are right; this one sentence
  undoes them. Rewritten to say below and above the threshold.
- **A preset with no story** (`expected-value-and-expected-utility`,
  `lottery-ticket`). The umbrella and the fair bet are each worked in the body;
  the third preset, a ticket costing 1 that pays 500 at one in a thousand, is
  never mentioned, so a reader who selects it sees skip, 0 and a tie at 1/500
  with nothing to check them against. One paragraph added: buying scores −1/2,
  the tie is where the prize equals the odds against.
- **A preset whose pinned tile does not say why it exists**
  (`the-decision-matrix-and-dominance`, `dominated`). The preset adds a coat
  the umbrella dominates; the choice tile still prints `none`, because the
  survivors do not dominate each other, and the kit has no tile for the
  undominated set. The fact the preset exists to show lives only in the status
  line. The body now tells the reader to read it there. The kit-side fix, a
  tile for the acts that survive, is recorded below.
- **Pascal's own reply is missing** (`pascals-wager`). The table scores an act
  called abstain at 0, and the lesson's objections are all against the wager;
  Pascal's best-known move, that abstaining is not on offer because not to
  wager for is to wager against, is the one a defender would make first and it
  was not stated. Added, with the observation that it leaves the arithmetic
  unchanged and changes only what the chooser can claim.
- **A compressed claim about bounded utility that reads as false**
  (`the-st-petersburg-game`, body). "It removes the puzzle only if it is
  bounded, not merely concave." For the game as stated a concave unbounded
  utility such as the logarithm does give a finite expectation, which is Daniel
  Bernoulli's 1738 reply; what concavity cannot do is close the puzzle for
  every game, since prizes can be made to grow faster than any unbounded curve.
  Rewritten to say exactly that, and Bernoulli's reply is now named where the
  lesson leans on it.
- **An unattributed principle** (`the-allais-paradox-and-the-sure-thing-principle`).
  The sure-thing principle is Savage's name and the lesson never says so. One
  clause added to the definition.
- **A quiz `why` that explains half its own answer**
  (`maximin-maximax-and-minimax-regret`, quiz 3). The correct choice is
  "maximin and maximax, but not minimax regret" and the explanation mentions
  only maximin. Extended with the maximax case on the shifted umbrella (leave
  to take).
- **A `note` that miscounts the menu** (`maximin-maximax-and-minimax-regret`).
  "A fourth rule appears in the menu": the menu has eight. Reworded to name
  Laplace as the one rule on the menu the course does not teach and to say the
  rest need probabilities, which is the next lesson's business.

## The seam between part A and part B

The two parts are in one voice: British spelling throughout, the same "the lab
prints" idiom, the same habit of stating the position's strongest form before
its cost. The module labels are the PLAN's (Risk runs from
`expected-value-and-expected-utility` to `ambiguity-and-the-ellsberg-urn`, so
the first two lessons of part B are still Risk, which the package docstring
had wrong and now has right). Part A's last lesson points forward to the
Allais lesson by title, at the point where it says one set of utilities must
explain every choice; part B's first lesson did not point back, so a reader who
had just learned that concave utility justifies preferring a sure thing arrived
at "A gives up a little expected money for certainty" without being told that
this is exactly what the previous lesson licensed, and that the Allais result
is that the same utilities must then also license C over D. One clause added.
The one stylistic drift found is currency: part A's single "pounds" against
part B's dollars, which are the problems' own. The pounds are gone.

## Where a learner gets stuck

- `risk-aversion-and-the-value-of-information` carries two ideas, concave
  utility and the value of perfect information, and the PLAN puts them together
  on purpose ("two ideas share one mechanism"). They do share the arithmetic
  but not the difficulty: the first needs the reader to stop averaging money,
  the second needs a new quantity (expected best) with a name that is easy to
  confuse with the old one (best expected). The worked example covers only the
  second. The lesson count is fixed by `COURSES.json`, so this is recorded
  rather than split; if the course is ever extended, this is the lesson to cut
  in two.
- `the-st-petersburg-game` asserts that 1/2 + 1/4 + 1/8 + … is exactly 1. The
  path promises school arithmetic only, and this is the one infinite sum a
  reader is asked to take on trust; the lab's remainder tile shows the gap
  closing (1/4 at twelve terms) and the panel asks the reader to push n to 60.
  That is adequate evidence for a reader who moves the slider and none for one
  who does not.

## Verified correct and left alone

The money-pump witness in `preference-transitivity-and-the-money-pump` is
right: the relation kit's transitivity scan visits (1, 5) then (5, 1) first and
reports "(1, 5) and (5, 1) ∈ R but (1, 1) ∉ R", which is the pair the body
names; the relation kit carries no pinned tiles, so this was checked by reading
the kit, not by labcheck. The Ellsberg algebra (red needs p < 1/3, black or
yellow needs p > 1/3), the Allais identity (both gaps 11/100·u(1M) −
10/100·u(5M) − 1/100·u(0)), the Newcomb threshold (1001/2000), the capped
St Petersburg limit (K + cap/2^K: 11 for 1024, 21 for 2^20, a little over
forty for a trillion) and the insurance figures (cover 19 against an expected
loss of 18.75, 9 against 35/4) were each recomputed and are correct. Dates and
attributions are right: Allais 1953, Ellsberg 1961, Nozick's statement of
Newcomb's problem, Nicolaus Bernoulli's letter of 1713.

## Remaining issues, for whoever next owns this course or the kit

- The `decide` mode has no tile for the undominated set, so a preset built to
  show a dominated act can pin only `none`. A `deSurvive` tile (the acts no act
  dominates, in act order) would let `dominated` pin what it is for.
- `risk-aversion-and-the-value-of-information` should be two lessons; see
  above.
- The relation kit is not in `KITS_WITH_EXPECTATIONS`, so the first lesson's
  one computed claim is checked by no gate.
