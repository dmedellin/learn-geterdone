# Pedagogy assessment — Games and the Social Contract (philosophy, course 5)

First assessment, formed from the eleven lesson dicts in
`content/philosophy/c5_games/` (`part_a.py`, lessons 1–6, and `part_b.py`,
lessons 7–11, written by two authors from `docs/philosophy/PLAN.md` §C
course 5), the course dict in `__init__.py`, the spoken forms in
`content/spoken/philosophy_c5_games.py`, and the three `choicekit` modes the
course renders through (`game`, `iterated`, `commons` in
`scripts/mathpath/labs/choicekit.py`). The pages were rendered with
`scripts/preview_subject.py` and every tile read with
`node scripts/labcheck.js --observe`; every figure the prose states was
recomputed by hand, and the seven-strategy round robin was re-simulated in
Python from the kit's own strategy rules at 1, 5, 8, 10, 12, 20 and 50
rounds. The course assumes Decision and Rationality and the courses before
it, and is judged against what those teach: expected value and the decision
matrix, dominance as "at least as good in every state and better in one",
exact fractions, and the partial sums and limits of “The St Petersburg Game”.

Lessons, in course order: `strategic-form-and-best-responses`,
`the-prisoners-dilemma`, `nash-equilibrium-in-pure-and-mixed-strategies`,
`coordination-conventions-and-the-stag-hunt`,
`repeated-games-and-reciprocity`, `the-shadow-of-the-future`,
`humes-farmers-and-convention`, `hobbes-and-the-state-of-nature`,
`the-tragedy-of-the-commons`, `public-goods-and-free-riding`,
`the-evolution-of-cooperation`.

## Verdict

The course teaches its subject. Every lesson closes on an act the lab can
check, every §C misconception is `mistakes[0]` and is refuted with a number,
every figure in the prose is one the lab prints (including the tournament
totals at ten rounds, `TF2T 185, TFT 184, ALLD 146`, and the claims about
the winner at one, five, eight and fifty rounds, all of which the simulation
confirms), and the philosophers are treated as arguments rather than as
history, at their strongest. The defects found are local: one quiz
distractor that is true, one invitation in a lab panel that the lab answers
differently from the prose because the many-player kit counts a tie as
dominance where the two-player kit does not, one sentence that reads a
claim into Hobbes he did not make, one appeal to an infinite sum the
earlier courses never stated in general, a convention defined twice in two
senses without the seam being named, and three lessons whose labs print
tiles the lesson has not yet taught. All are fixed below.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Mark a
  table and say for one unmarked cell who would switch
  (`strategic-form-and-best-responses`); prove a game is a dilemma or show
  it is not, then flip the verdict by changing one payoff
  (`the-prisoners-dilemma`); compute a mix and check it against pure
  deviations (`nash-equilibrium-in-pure-and-mixed-strategies`); compute the
  belief threshold (`coordination-conventions-and-the-stag-hunt`); read a
  match round by round (`repeated-games-and-reciprocity`); derive a
  threshold and use it (`the-shadow-of-the-future`); say what turns refusal
  into help (`humes-farmers-and-convention`); show how a penalty moves an
  equilibrium (`hobbes-and-the-state-of-nature`); find the gap and choose
  the fee that closes it (`the-tragedy-of-the-commons`); say whether a
  public-goods game is a dilemma and by how much
  (`public-goods-and-free-riding`); say where a population goes from a
  stated start (`the-evolution-of-cooperation`). None is "understand".
- **One diagnosis runs through the whole course and is repeated from a
  new angle each time: the verdict is in the payoffs, not in the people.**
  Trust makes defecting more tempting, not less (`the-prisoners-dilemma`,
  mistake 1, with `5` against `3`); the farmers of the twelve-season preset
  are "exactly as selfish" as those of the one-harvest preset
  (`humes-farmers-and-convention`); the sovereign "changes payoffs, not
  people" and the fine is never collected (`hobbes-and-the-state-of-nature`);
  greed is "a change in wishes; the tragedy needs only a change in who pays"
  (`the-tragedy-of-the-commons`); assortment changes "who meets whom" and no
  payoff (`the-evolution-of-cooperation`). This is the right spine for a
  course whose stated purpose is to write social-contract arguments as games.
- **Stability is separated from merit, three times and with the number
  that shows it.** Chicken's mixed equilibrium expects `−1/10` against the
  `0` of the cell nobody plays
  (`nash-equilibrium-in-pure-and-mixed-strategies`); the equilibrium of the
  commons totals `40` against an optimum of `121`
  (`the-tragedy-of-the-commons`); a population of cooperators averages `3`
  and one of defectors `1`, and selection moves to the defectors anyway
  (`the-evolution-of-cooperation`).
- **The arithmetic is right everywhere it was checked.** Chicken's `9/10`
  and the crash one time in a hundred; the stag hunt's `3/4` read first as
  a mix and then as a belief threshold and then as a replicator rest point,
  which is the course's best piece of sequencing; GRIM's `1/2` and TFT's
  `2/3`, with `30` against `14` at `δ = 9/10` and `4` against about `5.33`
  at `1/4`; the farmers' `36` and `30`; the herders' `C(k) = 3 + k`,
  `D(k) = 4 + 2·k`, the `121` at nine restrainers, and the claim that the
  gap opens between five and six herders; the public good's `3k − 7`
  against `3k`; the replicator's `1/3`, `64/79`, `2/5` and `9/17`. The
  tournament prose in `repeated-games-and-reciprocity` (`50` from ALLC,
  `30` from PAVLOV, `14`, `18`, `10`) is exact.
- **The positions are stated fairly and at their strongest.** Hume's
  farmers are quoted, the turn-taking of his version is admitted and the
  flattening named (`humes-farmers-and-convention`); Hobbes gets both the
  competition reading (a dilemma) and the diffidence reading (a stag hunt),
  which is the honest state of the scholarship, and the lesson says glory
  cannot be tabulated and leaves it out (`hobbes-and-the-state-of-nature`);
  Ostrom is named as the reason the commons lesson claims only a
  conditional; experiments in which people give are not claimed to be
  refuted by the public-goods table. The three causes of quarrel and the
  three quotations are accurate.
- **Every lab is honest about what it did not compute.** The limits of the
  seven-strategy field, the chosen payoffs, the absence of turns, the
  replicator's infinite population and lack of mutation are each stated in
  the lesson that leans on them.

## What the course teaches badly, or claims and does not deliver

1. **A distractor that is true** (`the-tragedy-of-the-commons`, quiz 3,
   "Why 11 and not 5?"). The distractor "Eleven is the number of herders
   plus one" is correct for this payoff family: the largest gain from adding
   is `1 + (n − 1) = n`, so the smallest whole fee that makes restraint
   strictly better everywhere is `n + 1`. A reader who worked that out
   would be marked wrong and the `why` says nothing to them. Replaced with
   a distractor that is false for a reason the lesson teaches (a fee need
   only beat the gain at `k = 0`), and the `why` now names it.
2. **The lab panel asks a question the lab answers differently from the
   prose** (`the-tragedy-of-the-commons`). The panel says "find the
   smallest whole fee that makes restraining dominate"; the prose says
   `11`. But `commons` reports dominance in the weak sense of “The Decision
   Matrix and Dominance” (at least as good at every `k`, better at some),
   while `game`, which “The Prisoner's Dilemma” defined strict dominance
   against, reports only strict dominance. At a fee of `10` the herder
   facing nine restrainers is indifferent and the tile already says
   "Cooperate dominates", with equilibria at nine and ten restrainers. A
   reader who follows the panel's instruction finds `10` and the prose
   never explains why. Fixed by saying so in the body, adding a `fee-ten`
   preset at the border pinned to the two tiles that show it, and making
   the panel ask for both numbers.
3. **A claim read into Hobbes** (`hobbes-and-the-state-of-nature`). "Covenants
   without the sword are but words" was glossed as "the claim that no cheaper
   change to the table will do", which is not what the remark says; it says
   that a promise changes no payoff. Rewritten to that, with the penalty
   arithmetic (ties at `2`, strict at `3`, the lab's dominance tile being
   strict) kept beside it.
4. **An infinite sum used as if taught** (`the-shadow-of-the-future`). The
   value of `x` every round is given as `x / (1 − δ)` with no derivation.
   “The St Petersburg Game” summed one tail, `1/2 + 1/4 + …`, and never
   stated the general series. One sentence now derives it (multiply by `δ`
   and subtract), which is all the course needs.
5. **Convention is defined twice, in two senses, and the seam between the
   two authors' halves is where it happens.** The Lewis sense in
   `coordination-conventions-and-the-stag-hunt` (an equilibrium of a
   recurring coordination game with an alternative that would have served)
   and Hume's wider sense in `humes-farmers-and-convention` (any regularity
   each keeps because the others keep it). The second lesson's rowers are a
   case of the first kind and its farmers are not, since helping is not an
   equilibrium of the one-harvest game at all. A reader who learned the
   first definition and meets the second without comment will think one is
   wrong. One paragraph now names the difference and what the two share.
6. **A preset presented as computing what it only replays**
   (`humes-farmers-and-convention`). "Both refuse, each collects 1, and the
   lab's first preset prints exactly that" — the preset sets both farmers
   to ALLD, so it prints `1` each by construction; the dominance that
   produces the refusal was computed in “The Prisoner's Dilemma”'s lab, and
   the `iterated` mode has no dominance tile. Reworded to say what was
   computed and where.
7. **Tiles the lesson has not taught.** `strategic-form-and-best-responses`
   prints a mixed equilibrium (`row L: 1/3, col L: 1/3`) and a Pareto
   verdict before either idea exists; `repeated-games-and-reciprocity`
   prints the continuation threshold a lesson early; `the-tragedy-of-the-
   commons` and `public-goods-and-free-riding` print "Cooperators after the
   generations: 1/2" with the generations at zero. A kit is shared and the
   tiles cannot be hidden, so each lesson's `note` now says which tile
   belongs to which later lesson. Small, but it is where a careful reader
   stalls.
8. **One number the battle of the sexes preset prints and the prose does
   not use** (`coordination-conventions-and-the-stag-hunt`). The paragraph
   says "two pure equilibria and a mixed one" with no figures. The lab's
   `3/5` and `2/5`, and the `6/5` each then expects, are now in the prose,
   and the preset pins its Pareto tile.
9. **"Stable" used before it means anything**
   (`nash-equilibrium-in-pure-and-mixed-strategies`): "the mixed
   equilibrium is stable" is true of chicken under the replicator step but
   the course only defines stability in `the-evolution-of-cooperation`, and
   there the stag hunt's interior rest point is unstable. Reworded to the
   equilibrium property that was actually shown.

## Where a learner gets stuck

- `coordination-conventions-and-the-stag-hunt` carries four ideas
  (coordination, convention, payoff against risk dominance, the belief
  threshold) and a third game. §C mandates all of them. The lesson survives
  because the threshold and the risk-dominance product pick out the same
  equilibrium and the `note` says so; a reader who skips the note will see
  two unrelated tests. Not restructured, since the slug and the §C
  objective fix the content; recorded as the heaviest page in the course.
- `repeated-games-and-reciprocity` introduces seven strategies at once.
  The lesson mitigates this well (the worked example plays one match by
  hand; the quiz asks for the record of TFT against ALLD), and the
  tournament prose names where every ALLD point comes from. Acceptable.
- The step from two players to `C(k)` and `D(k)` in
  `the-tragedy-of-the-commons` is the course's second genuinely new skill.
  The lesson names it as such in `concepts_intro`, and the worked example
  counts the animals explicitly. Good.

## Misconceptions

Every §C misconception is `mistakes[0]` and each is refuted by a specific
number rather than restated. Two further wrong models the course names
without being told to, and should keep: that a mixing player randomises to
be unpredictable (`nash-equilibrium-in-pure-and-mixed-strategies`, mistake
2: the weights are fixed by the opponent's payoffs), and that a rising
share is a verdict that the type is good (`the-evolution-of-cooperation`,
mistake 2). One the course could name and does not: that a mixed
equilibrium is "half the time" (matching pennies happens to be `1/2`;
chicken's `9/10` is the counterexample and is used as one in the quiz, so
this is covered in practice).

## Prerequisite order

Checked backwards. Dominance (weak) is from “The Decision Matrix and
Dominance”; strict dominance is defined fresh in `the-prisoners-dilemma` and
the difference now matters once, in the commons, where it is named. Expected
value, exact fractions and probability as weight are from Decision and
Rationality and Knowledge and Evidence. Pareto domination is defined in
`the-prisoners-dilemma` before use. Nothing in the course reaches forward
except by title to a later lesson of the same course. No violation found in
an earlier course.

## Voice, references, structure

Careful prose throughout; no "in this lesson", no exclamation marks, no
rhetorical questions outside quiz stems; British spelling consistent across
both halves. Cross-references are by title in curly quotes and all six
titles cited exist. No numbered course or lesson reference in any prose
field. Concepts, steps, mistakes and quiz counts are within the renderer's
ranges on every lesson; all key lines are within 46 characters; every lab
builds and every pinned figure matches.

## Changes made in this pass

- `the-tragedy-of-the-commons`: body paragraph on the fee rewritten to
  state the weak/strict border at `10`; new preset `fee-ten` pinned to
  `cmDom` and `cmEq`; panel intro asks for both the dominance border and
  the single-equilibrium border; quiz 3 distractor and `why` replaced;
  `note` names the replicator tile.
- `hobbes-and-the-state-of-nature`: the "covenants without the sword"
  sentence rewritten.
- `the-shadow-of-the-future`: the geometric sum derived in one sentence.
- `humes-farmers-and-convention`: the one-harvest preset described as a
  replay of a verdict computed elsewhere; a paragraph naming the two senses
  of "convention" and what they share.
- `coordination-conventions-and-the-stag-hunt`: the battle of the sexes
  given its figures (`3/5`, `2/5`, `6/5` each); `sexes` pins `gaPareto`.
- `nash-equilibrium-in-pure-and-mixed-strategies`: "stable" replaced by the
  property shown.
- `strategic-form-and-best-responses`, `repeated-games-and-reciprocity`,
  `public-goods-and-free-riding`: `note` says which tiles belong to later
  lessons.

## Remaining

- `coordination-conventions-and-the-stag-hunt` would be lighter as two
  lessons (conventions; the stag hunt and risk dominance). The URL space is
  fixed, so it stays one; recorded here.
- The `commons` kit reports weak dominance and the `game` kit strict. That
  is a kit decision outside this course; the course now says so where it
  matters, and a future kit revision could print "weakly" in the tile.
