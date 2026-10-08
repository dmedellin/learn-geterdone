# Pedagogy assessment — Science, Induction and Causation (philosophy, course 3)

First assessment, formed from the ten lesson dicts in
`content/philosophy/c3_science/` (`part_a.py`, lessons 1–5, one author;
`part_b.py`, lessons 6–10, another; `__init__.py`, the course home) on the
branch `feat/philosophy`, against the design in `docs/philosophy/PLAN.md` §C
(course 3) and §F, and against what the two courses it may assume actually
teach. Every lesson was read in full before anything was changed. Every page
was rendered with `scripts/preview_subject.py` and every tile string quoted
in prose was read off the rendered page with `node scripts/labcheck.js
--observe`; every figure quoted in prose was recomputed in exact arithmetic
(`fractions.Fraction`). The ten slugs, in course order:
`enumerative-induction-and-humes-problem`, `grue-and-the-new-riddle`,
`confirmation-and-the-weight-of-evidence`,
`falsification-and-what-a-theory-forbids`, `the-raven-paradox`,
`the-duhem-quine-problem`, `mills-methods-and-the-common-factor`,
`correlation-confounding-and-simpsons-paradox`,
`counterfactual-causation-and-the-but-for-test`,
`preemption-and-overdetermination`.

The verdict first: the course teaches its subject. Its one organising act —
put the claim in a form the lab can compute, read the verdict, then say which
premise the verdict rests on — is carried through all ten lessons, every
`standard` names an act the closing quiz measures, the labs compute exactly
what the prose says they compute, and the positions that matter (Hume, the
holist, the counterfactual theorist) are set out as arguments rather than as
opinions. The defects found were local: one false rule stated as a key line,
one of Mill's methods described as a different one, two authorities never
named or distinguished, one lab preset that did not match the sentence
describing it, and a handful of places where a position was stated short of
its strongest form. All are fixed below. Nothing needs splitting or
restructuring, and the URL space is untouched.

## What the course teaches well

- **The objective is observable in every lesson and it is the right one.**
  Construct the counterexample row and compute the prediction under two
  priors (`enumerative-induction-and-humes-problem`); show a Bayes factor of
  exactly 1 and say what follows (`grue-and-the-new-riddle`); classify
  evidence and give its weight (`confirmation-and-the-weight-of-evidence`);
  list what a row forbids and compute the effect
  (`falsification-and-what-a-theory-forbids`); compute the factor for each
  way of sampling (`the-raven-paradox`); write a failed prediction as a set
  and locate what it refutes (`the-duhem-quine-problem`); apply both methods
  and state what the table leaves open (`mills-methods-and-the-common-factor`);
  compute both comparisons, test for a reversal, name the confounder
  (`correlation-confounding-and-simpsons-paradox`); flip and recompute
  (`counterfactual-causation-and-the-but-for-test`); build the preemption
  model, show but-for fail, recover the cause
  (`preemption-and-overdetermination`). No "understand" anywhere, and the six
  course outcomes in `__init__.py` are the same acts at course grain.
- **One diagnosis is repeated until it sticks: the number you read off the
  lab was put there by a premise, and the lab cannot check the premise.**
  The prior in `enumerative-induction-and-humes-problem` ("the data did not
  change; the prior did"), the projectibility judgement in
  `grue-and-the-new-riddle`, the alternative's likelihood in
  `confirmation-and-the-weight-of-evidence` ("a number you chose"), the
  sampling description in `the-raven-paradox`, the choice of what to blame in
  `the-duhem-quine-problem`, the columns the table lacks in
  `mills-methods-and-the-common-factor`, the causal story that decides which
  table to trust in `correlation-confounding-and-simpsons-paradox`, the
  equations themselves in the two causal lessons ("the model is a premise").
  The course home's `footer_lead` says it once more, plainly. This is the §F
  rule "the lab's limit is stated in the lesson that leans on it", kept in
  every lesson.
- **The labs compute what the prose says, to the digit.** Every pinned tile
  matches; every figure in prose that is not pinned was recomputed:
  `524288/554325` and `43735/44346` (uniform prior, ten sunrises);
  `131072/881997` and `1382119/1763994`, about `0.78` (the skeptic's prior);
  `5845851/5846875`, about `0.9998` (ten allowed outcomes); `901/900`,
  `901/1801`, `10/9`, `10/19` (ravens); `27/29`, `13/15`, `11/16`, `39/50`,
  and the standardised `634983/762700` against `6231/8000`, about `0.83`
  against `0.78` (kidney stones, with the kit's weighting read from
  `choicekit.py`: each group by its share of all trials); `113/449` against
  `534/1198` (Berkeley). The two Mill tables were checked by hand against
  the kit's candidate search (positive and negated literals, every
  conjunction and disjunction of two): `O` and `O ∧ B` fit the first, and
  only `P ∨ E` fits the second.
- **Positions are argued, not announced.** Hume's argument is set out as a
  numbered valid argument and the reader is told what rejecting each premise
  costs; the falsificationist and the holist each get a paragraph in
  `the-duhem-quine-problem` and "the lab agrees with both"; the reader who
  rejects the held-fixed account of causation "owes a different account of
  why Suzy broke the bottle". The misconception in each lesson is a model
  someone holds and is refuted with the specific number or row, as §F
  requires: the neutral row for "consistent evidence confirms", Cy's bread
  for "the common factor is the cause", `289/350` against two group wins
  for "a higher overall rate means a better treatment".
- **The worked-example progression is complete in every lesson**: a worked
  example in exact fractions, four or five method steps that generalise it,
  a lab with two to four presets that vary one thing at a time (the prior;
  one likelihood; which variable is held), and a quiz whose `why` addresses
  each distractor rather than restating the rule. Retrieval is cumulative:
  the quiz in `falsification-and-what-a-theory-forbids` asks for the
  posterior after a hundred confirmations, and the one in
  `counterfactual-causation-and-the-but-for-test` asks what a missing pilot
  light does to a verdict.
- **The historical anchors are right.** Neptune 1846 from the Uranus
  residuals; Vulcan proposed and not found; Mercury's perihelion and 1915;
  the Charig kidney-stone counts (open surgery against the keyhole
  procedure); the 1973 Berkeley admissions for departments A and F; Hume's
  second definition of cause from the Enquiry quoted correctly.

## What it taught badly, and the fix applied

1. **A false rule in the key box and the one-line summary
   (`falsification-and-what-a-theory-forbids`).** The key line read "forbids
   nothing ⟹ no data moves it" and the `one_line` said "a hypothesis that
   forbids nothing is never moved". Both are false: a hypothesis with no
   zero in its row is moved whenever its row differs from its rival's (edit
   the unfalsifiable preset's row to `1/2, 1/4, 1/4` and the same four
   observations confirm it by `81/64`). The `summary`, the quiz and the
   mistakes hedged correctly ("and shares its rows with its rivals"), so the
   lesson contradicted its own hero. The preset conflates two properties —
   unrefutable (no zero) and unmovable (same row) — and the body never
   separated them. Fixed: the key box now carries both rules as two lines
   ("no zero in the row ⟹ never refuted", "same row as the rival ⟹ never
   moved"), the `one_line` and `summary` say the same, concept 3 states the
   middle case, and the body paragraph walks the reader through editing the
   row and reading `81/64`.
2. **Popper stated short of his strongest form (same lesson).** The lesson
   put his asymmetry into a Bayesian frame without saying that he rejected
   that frame: on his account survival corroborates and never raises
   probability, and a universal law has probability 0. A reader who knows
   this would think the lesson had misread him. Fixed: one paragraph states
   his position at full strength, says the lesson borrows the asymmetry into
   a frame he refused, and names what a reader who follows him then owes.
3. **Mill's method of difference described as something else
   (`mills-methods-and-the-common-factor`).** Concept 2, the def, the body,
   step 2, the key line, the worked line and quiz 1 all called "look at the
   negative cases and eliminate any factor present there" the method of
   difference. Mill's method of difference compares one positive instance
   with one negative instance alike in every circumstance but one; the
   elimination the lesson performs is the negative half of his joint
   (indirect) method. The table in fact holds no pair alike in all but one
   dish — Ann and Cy, the closest, differ in the oysters and in the wine —
   which is itself worth teaching. Fixed: concept 2 states the method of
   difference as Mill gave it and says what a table offers instead; the def
   describes the joint method as agreement applied twice; the body shows the
   table has no clean pair; step 2, the key line, the worked line, the
   summary and the quiz now say "the negative cases eliminate".
4. **Duhem and Quine never named or told apart (`the-duhem-quine-problem`).**
   The lesson title carries both names and the body mentioned neither, so
   the reader could not learn that Duhem's thesis was about physics and a
   theoretical group, and Quine's about the whole of what we believe. Fixed:
   one paragraph states each, says the lab's five-line set is Duhem's group
   written out, and locates the difference between them (whether the group's
   boundary can be drawn short of everything) as a question the lab cannot
   answer.
5. **Two presets did not match the sentence describing them (same
   lesson).** The prose and the worked example said the second repair
   "replaces `a` by its denial" and the third "replaces `h` by its denial";
   the `neptune` and `rival` presets also silently dropped the bridge `b`
   and shortened the conditional, so the reader who compared the set on the
   page with the description read a different set. Fixed: both presets keep
   `b` and the full conditional; the tiles were re-read from the page
   (`1 of 16`, witnesses `a=F b=T e=F h=T` and `a=T b=T e=F h=F`) and pinned;
   the worked lines now show `b = T`.
6. **Hume's argument not quite valid as written
   (`enumerative-induction-and-humes-problem`).** The third premise ran "not
   a necessary truth, and cannot be established by past experience without
   using it" and the conclusion "nothing non-circular supports it"; the step
   needs Hume's fork (no third source of support), which was missing, and
   the circularity premise was doing two jobs. Fixed: the argument is now
   five premises with the fork explicit and the circularity separate, and
   the paragraph after it says what rejecting each costs.
7. **Two smaller accuracy points.** "The sun rose this morning … confirms
   none of them" (`confirmation-and-the-weight-of-evidence`) now reads
   "confirms none of them against the others", which is what the factor
   says. `the-raven-paradox` now carries Good's point that the background
   can change the sign of the factor, with a description of how to see it in
   the lab (both rows rewritten for a draw from all the birds; with the
   hypothesis row fixed at black = 1 the rival's row alone cannot do it).
   `preemption-and-overdetermination` now attributes the trumping case to
   Schaffer.
8. **A dropped thread from the previous course
   (`correlation-confounding-and-simpsons-paradox`).** Knowledge and
   Evidence's “Reference Classes and Statistical Evidence” shows the same
   kidney-stone counts and says in so many words that the reason for the
   reversal "belongs to Science, Induction and Causation". This lesson
   opened as if the counts were new and called the arms `A` and `B` where
   the earlier lesson called them the open operation and the keyhole
   procedure. Fixed: the first paragraph picks up the thread by title and
   names the arms both ways.
9. **The course home's `assumes_long` named only Knowledge and Evidence**,
   while lessons 1, 5 and 6 reach back to Arguments and Validity by title
   (“Validity by Truth Table”, “Equivalence, De Morgan and Contraposition”,
   and now “Consistency and Belief Sets”). The transitive assumption is
   legitimate; the sentence now says so.

## What it claims to teach and does not

Nothing of substance. The course home's `not_covered` is honest and matches
§G: no statistical inference, no continuous priors, no causal inference from
data, no history of science as history. Two claims are slightly larger than
what is delivered and are left as they are: `the-raven-paradox`'s `standard`
asks the reader to "say why the two [factors] differ", and the lesson's answer
("the size of the sampled class") is the right one for the stipulated world
but the reader is not shown a second world; and
`preemption-and-overdetermination`'s `one_line` promises that holding the
backup fixed "repairs" the test, while the lesson is careful to say the
repair is contested and simplified — the `note` carries the hedge, the hero
does not.

## Where a learner gets stuck

- `enumerative-induction-and-humes-problem` asks the reader to accept a
  five-point "rule of succession" without ever having met the rule; the
  phrase is used once and explained as a discretisation, which is enough
  for the lesson but will send a curious reader elsewhere. Not changed.
- `correlation-confounding-and-simpsons-paradox` carries two hard ideas: the
  reversal, and the question of which table to trust (confounder against
  mediator). The second is required by the §C objective ("name the
  confounder") and by the forward link to the causal lessons, and it is
  confined to one paragraph, one step and one quiz item. It is the heaviest
  single page in the course; it is within the §E range and is not split.
- `preemption-and-overdetermination` carries preemption, overdetermination,
  the actual-value restriction, joint causes, Billy's hit as a non-cause and
  the trumping limit. All are in the §C entry, the lesson takes them in
  that order, and each is one recomputation; but a reader who has not done
  the previous lesson's chain preset by hand will not follow the third
  column. The lesson says so ("a third column that the next lesson puts to
  use") at the end of the previous one, which is the right place.
- Nothing in `grue-and-the-new-riddle` tells the reader that the two
  presets differ only in one likelihood row; the reader finds it by looking.
  The steps ("Compare the rows", "Find the outcome where they differ") make
  the looking the exercise, which is defensible.

## Misconceptions

Every `mistakes[0]` is the §C misconception for its lesson, stated as a model
someone holds and refuted with the lesson's own number or row. Beyond those
ten, the course also names and corrects: reading the posterior as if the data
alone produced it; "grue is a trick of language"; measuring confirmation
without an alternative; the Bayes factor as a probability; a likelihood of
zero as a prior of zero; "indoor ornithology works"; rejecting the
equivalence condition; "any theory can be saved, so tests prove nothing";
an inconsistent set as "every member is false"; every effect has one factor;
always trusting the within-group comparison; the reversal as a trick;
applying the but-for test only to the nearest variable; a verdict as a fact
about the world; holding the backup at a convenient value; expecting each of
two simultaneous causes to pass alone.

Two that were unaddressed before this pass and are now in the body text:
"unfalsifiable means unconfirmable" (now separated in
`falsification-and-what-a-theory-forbids`), and "the method of difference is
elimination by the negative cases" (now corrected in
`mills-methods-and-the-common-factor`). One remains unaddressed and is noted
below: that "confounder" and "mediator" are the same kind of third variable.

## The seam between part A and part B

The two halves read as one author. Both keep British spelling
(discretisation, standardised, colour, favour), both report the lab in the
same construction ("the lab prints", "the lab calls that"), both end every
body with the lab's limit, and the module boundary is in the right place:
part B's first lesson opens by referring back to what part A's falsification
lesson let a theory forbid, and part B's Mill lesson opens by turning from
"what evidence does to a hypothesis" to "how to find a hypothesis about a
cause". Two seams needed stitching and were stitched: the Duhem–Quine lesson
now names the consistency test it reuses by title, and the Simpson lesson now
picks up the thread the previous course handed it. One cosmetic seam is left:
part A's labs name the rival hypothesis `not-H` and part B's Duhem presets
use lowercase `h, a, b, e`; both are lab syntax, both are explained in the
kit's own hint, and nothing in prose depends on the difference.

## Prerequisites, checked backwards

The course may assume Knowledge and Evidence and, through it, Arguments and
Validity. Every backward reference resolves to a lesson that teaches what is
relied on: “Validity by Truth Table” (the counterexample row), “Equivalence,
De Morgan and Contraposition” (the contrapositive table in
`the-raven-paradox`), “Consistency and Belief Sets” (models and the minimal
inconsistent subset), “Updating on Evidence” (the procedure, and the Bayes
factor defined there as `P(E | H) / P(E | ¬H)` "with the likelihood on the
alternatives averaged by their priors when there are several", which is
exactly the kit's mixture and exactly what
`confirmation-and-the-weight-of-evidence` says), and “Reference Classes and
Statistical Evidence” (the kidney counts). Nothing from a later course is
used. No numbered course or lesson reference appears anywhere in the course
(the only numerals near the word "lesson" are the module docstrings).

## Changes made

In `content/philosophy/c3_science/part_a.py`:
`enumerative-induction-and-humes-problem` (Hume's argument, five premises
with the fork; the costs paragraph); `confirmation-and-the-weight-of-evidence`
(one clause; two worked lines trimmed from 61 characters to within the §E
limit of 60, which `preview_subject.py` does not gate);
`falsification-and-what-a-theory-forbids` (`one_line`,
`summary`, `key` now five lines, concept 3, the unfalsifiable-preset
paragraph, a new Popper paragraph); `the-raven-paradox` (Good's point in the
last body paragraph).

In `content/philosophy/c3_science/part_b.py`: `the-duhem-quine-problem`
(cross-reference by title; a new Duhem/Quine paragraph; `neptune` and
`rival` presets keep `b`, tiles re-read and pinned; two worked lines);
`mills-methods-and-the-common-factor` (`summary`, `key[1]`, concept 2, body
paragraph, def, step 2, worked line, quiz 1);
`correlation-confounding-and-simpsons-paradox` (first body paragraph);
`preemption-and-overdetermination` (attribution).

In `content/philosophy/c3_science/__init__.py`: `assumes_long`.

`content/spoken/philosophy_c3_science.py` needed no new entry: the preview's
read-out check reports every math run spoken after the edits.

`scripts/preview_subject.py philosophy --course
science-induction-and-causation` reports OK: ten labs execute and are swept,
ten pages with pinned figures, none failing.

## Remaining issues

- `correlation-confounding-and-simpsons-paradox` uses "the grouping variable
  is itself an effect of the treatment" without the word *mediator*, and the
  reader who later meets the word elsewhere will not connect it. One
  sentence would do; it was not added because the course has no lab that
  computes the distinction, and naming a concept the lab cannot test is
  against §0. Worth revisiting when the course after it (Decision and
  Rationality) is assessed, in case a later lesson supplies the word.
- The `kidney` preset pins `siAdjusted` to the pooled string, because the
  shipped `weight` is `pooled` and under that setting the Adjusted tile
  mirrors the Pooled one. The pin is true and redundant; the standardised
  figures the prose quotes are checked only by hand and by the status
  banner. §C requires `siWeight = pooled` shipped, so this is a limit of the
  pin mechanism (expectations key on the preset menu only), not of the
  lesson. Recorded for `@lab-arithmetic`.
- `preemption-and-overdetermination` is the heaviest lesson in the course
  (six distinct moves). It is within every §E range and every move is one
  recomputation; it is not split because the URL space is fixed and because
  §C specifies all six. If a future revision adds a lesson, the trumping
  preset and the "Billy's hit is not a cause" paragraph are the material to
  move.
- `scripts/preview_subject.py` imports the whole `philosophy` package, so a
  syntax error in any sibling course (today `c8_metaphysics/part_b.py`, mid
  edit by another author) stops every course's preview. This assessment ran
  it through a scratchpad wrapper that stubs a sibling that fails to import
  with `COURSE = None`. The script could do the same itself when `--course`
  is given; recorded for whoever owns it.
