# Pedagogy assessment — Paradoxes and Their Exits (philosophy, course 10)

Formed from the nine lesson dicts in `content/philosophy/c10_paradoxes/`
(`part_a.py`, lessons 1–5, and `part_b.py`, lessons 6–9, written by two
authors from `docs/philosophy/PLAN.md` §C), the course dict in `__init__.py`,
the spoken forms in `content/spoken/philosophy_c10_paradoxes.py`, and the
pages as `scripts/preview_subject.py` renders them, with every preset's tiles
read off the built page by `labcheck.js --observe`. The course may assume the
nine courses before it and nothing else. All nine lessons were read before any
was changed; the last two sections record what was changed and what was not.

Lessons, in course order: `the-barber-and-the-anatomy-of-a-paradox`,
`the-liar`, `zenos-dichotomy`, `achilles-and-the-tortoise`,
`thomsons-lamp-and-supertasks` | `the-two-envelopes`, `sleeping-beauty`,
`monty-hall`, `moores-paradox-and-what-cannot-be-believed`. The bar marks the
seam between the two authors.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.**
  Classify an argument by its exit and refute the barber in a model
  (`the-barber-and-the-anatomy-of-a-paradox`); derive the biconditional, test
  it, name an exit with its price (`the-liar`); sum the halves exactly and
  bound the remainder (`zenos-dichotomy`); set a race up as a series and
  compute where it ends (`achilles-and-the-tortoise`); separate what a
  supertask settles from what it leaves open (`thomsons-lamp-and-supertasks`);
  compute the worth of switching from a prior and locate the failing step
  (`the-two-envelopes`); compute both answers by one rule and say what the
  disagreement is about (`sleeping-beauty`); compute the posterior from the
  host's rule and show it changes with the rule (`monty-hall`); show a
  sentence true at a world and its known form true at none
  (`moores-paradox-and-what-cannot-be-believed`). None is "understand".
- **The method is taught once, in the shape the later lessons reuse.**
  `the-barber-and-the-anatomy-of-a-paradox` fixes the definition (valid,
  plausible, unacceptable), the three exits, and a four-move procedure whose
  first move is standard form. Its three concepts are the right three, and the
  third ("a contradiction is the usual bad conclusion, not the only one")
  heads off the misconception the quiz then tests. The barber is the right
  opening case because its exit costs nothing, and the lesson says so before
  the liar arrives to show an exit that costs a great deal.
- **The figures are right and the prose agrees with every tile.** All
  fifty-five pinned strings across eight pages match the page
  (`labcheck`), and every figure quoted in prose was recomputed: 1023/1024 and
  1/1024 after ten halves, 1/512 after nine, 1/1048576 after twenty
  (`zenos-dichotomy`); 111111/1000 with 1/9000 to go, 1000/9, 271 and 1000 for
  the close race, no limit at ratio 1 (`achilles-and-the-tortoise`); off at
  ten, on at eleven, within a billionth at thirty
  (`thomsons-lamp-and-supertasks`); 10 against 8, 4 against 8, 16, and the tie
  at a prior of 2/3 that the panel sends the reader to find
  (`the-two-envelopes`); Bayes factors 1, 1/2, 2, 2 and posteriors 1/2, 1/3,
  1/2, 2/3 (`sleeping-beauty`); 1/3, 2/3, 0; 1/2 each with a random host; 1/4
  and 3/8 with four doors (`monty-hall`); `w1`, `none`, `w1, w3`, `none`
  (`moores-paradox-and-what-cannot-be-believed`).
- **Positions are stated at their strongest and the lab stops where it
  should.** The liar's three premises are each given a defender and the
  strengthened liar is used against the gap theorist; Tarski's hierarchy is
  given its price in the same paragraph as its merit; the dialetheist is named
  as needing a consequence relation the lab does not implement (`the-liar`).
  The lamp lesson gives the standard reply and then "the case against this
  reply has force too" (`thomsons-lamp-and-supertasks`). Lewis's halfer is
  made to pay for the Monday case and Elga's thirder for a credence of one
  third in a fair coin, and the lesson announces no winner
  (`sleeping-beauty`). Every lesson says what the lab does not do: it does not
  search all models (`the-barber-and-the-anatomy-of-a-paradox`), it does not
  settle whether space is divisible (`zenos-dichotomy`), it cannot add a rule
  for the end of the minute (`thomsons-lamp-and-supertasks`), it does not know
  the organiser's prior (`the-two-envelopes`), the likelihood
  (`sleeping-beauty`) or the host's rule (`monty-hall`).
- **The misconceptions are the real ones and each is refuted with a row, a
  number or a world.** A paradox is a contradiction, refuted by the argument
  from "there is such a barber" to `s ↔ ¬s`; the liar is simply false, refuted
  by the row `p = F` crossing to the other row; infinitely many steps take
  infinitely long, refuted by `1/2^n`; Achilles never catches up because the
  gaps never reach zero, refuted by 1000/9; a convergent series of actions has
  a last action; symmetry shows switching is always better, refuted at the top
  of the list; the coin is fair so the answer must be one half, refuted by two
  likelihoods under one prior; two doors remain so each is one half, refuted
  by the likelihoods 1/2, 1, 0; Moore's sentence is a contradiction, refuted
  at `w1`. Every `mistakes[0]` is the §C misconception.
- **Retrieval practice is real.** Every quiz item has a `why` that addresses
  each wrong choice, and the questions test the idea rather than the words:
  "in which row is `p → ¬p` true" (`the-liar`), "how far after five steps"
  (`zenos-dichotomy`), "what is the common ratio when the speeds are 10 and 5"
  (`achilles-and-the-tortoise`), "the thirder is told it is Monday"
  (`sleeping-beauty`), "four doors, the host opens 4" (`monty-hall`).
- **The Moore lesson is better than its brief.** PLAN §C asks for three
  presets; the author added a fourth, a KD45 frame (serial, transitive,
  euclidean, which the frame tile prints), so that the result is shown for
  belief with introspection and not only for factive knowledge. That is the
  right strengthening, because the title says "believed" and reflexivity is a
  condition on knowledge, and the lesson says why the two differ.

## What the course teaches badly, or wrongly

1. **`achilles-and-the-tortoise` contradicted its own method at the one
   place the course exists to teach.** The argument is set out with three true
   premises and a conclusion that does not follow from them; the exit
   paragraph said "the step that fails is the move from them to the
   conclusion", which is exit two by `the-barber-and-the-anatomy-of-a-paradox`'s
   definition, and in the next sentence "it is the previous lesson's exit
   again", which was exit one. The `standard` then asked the reader to "name
   which premise of Zeno's argument the result refutes", when by the lesson's
   own account none of the stated premises is refuted. A reader doing what the
   first lesson taught (write it in standard form, check the steps) reaches
   exit two and is told it was exit one. The fix is not to choose, but to
   teach the fact the muddle hides: a step that fails only because it borrows
   an unstated premise is faulted by stating the premise and denying it, so
   exits one and two are two descriptions of one repair, and which name it
   gets depends on how much of the argument was written down — which is why
   standard form is the first move. The paragraph, a fifth step and the
   standard now say so.
2. **Three lessons never named an exit, against the course's own promise.**
   The course home (`summary`, `how_to`) and the first lesson both say every
   lesson ends by asking which exit the best reply takes and what it costs.
   `zenos-dichotomy`, `achilles-and-the-tortoise` and
   `thomsons-lamp-and-supertasks` had no such step, and `monty-hall`'s last
   step was "try a different rule". The lamp lesson was the costly one: it
   presents two replies (the story is silent at the minute; the story is
   impossible) without saying that both are exit one against different
   premises with different prices, which is exactly the classification the
   closing standard of the course asks for. Each of the four now has the step,
   and the lamp lesson's argument has its conclusion as a fifth line so that
   "the fourth premise" means something.
3. **`the-two-envelopes` stated the strongest version of the reply but not
   the strongest version of the puzzle.** It said "faulting a step would mean
   faulting the expected value, and the arithmetic above is right", and
   presented exit one (the chance of "double" cannot be one half at every
   amount) as the only live exit. That is right for the open version, where
   the 8 is in hand. But the lesson also runs the closed version ("you may as
   well switch without opening"), and there the standard diagnosis is exit
   two: `x` names the smaller amount in one case and the larger in the other,
   so `x/2` and `2x` are not halves and doubles of one number, and averaging
   them is the step that only looks valid. A lesson that tells the reader
   exit two is unavailable, in a course whose subject is choosing exits,
   misstates the field. The paragraph now runs both versions and names the
   exit of each; the first concept is retitled "Once the amount is fixed, the
   argument is valid"; the quiz question about the standard reply now says
   the envelope has been opened.
4. **`monty-hall` classified an exit without saying which argument it was
   classifying.** Two arguments are on the page — the familiar one to one
   half and the correct one to two thirds — and the body first says "that is
   the premise to look at" (exit one, of the first argument) and later "the
   best exit is the third: accept it" (of the second), with neither argument
   ever put in standard form. The lesson now sets the two-thirds argument out
   as four premises from the rules of the game, says it is the paradox and
   exit three is its exit, and says the one-half argument is not the paradox
   but a mistake with a false premise the lab exposes.
5. **`moores-paradox-and-what-cannot-be-believed` had no argument.** The
   first lesson's method begins with standard form; the Moore lesson gave the
   sentence, the model and the exit ("the premise denied is that whatever can
   be true can be known") without ever listing the premises that the denied
   one belongs to. It now has them: the sentence can be true; whatever can be
   true can be known and so sincerely asserted by the one it is about; no one
   can sincerely assert it; so someone can and no one can. The body also said
   that to assert the sentence sincerely the speaker "would have to claim" the
   boxed sentence, which is wrong (sincerity requires knowing or believing, not
   claiming to), and now says what would have to hold of the speaker.
6. **Two quiz distractors were true.** In
   `moores-paradox-and-what-cannot-be-believed`, "only the worlds that see no
   other world" was offered against "none of them" for a reflexive frame; a
   reflexive frame has no such worlds, so the two choices named the same empty
   set, and the `why` admitted it. In `monty-hall`, "switching never matters
   when the host acts at random" is true whenever the random host shows a
   goat, which is the case the question stipulates, and the `why` could only
   say it was "too general". Both are replaced by choices that are false, and
   the `why` of a third (`monty-hall`, "door 3 is empty, so its probability
   moves to door 2 alone") now says why a right number reached for a wrong
   reason is wrong: with a random host door 3 is just as empty and its third
   is shared.
7. **A cross-reference to a lesson that does not exist.** Both
   `the-two-envelopes` and `sleeping-beauty` sent the reader to “Bayes'
   Theorem and Updating on Evidence”; the lesson in Knowledge and Evidence is
   “Updating on Evidence”. `the-two-envelopes` also referred to "the course on
   decisions" where the rule is a title. `the-barber-and-the-anatomy-of-a-paradox`
   credited “Quantifiers and Their Order” with teaching evaluation in a finite
   model of the kind the `semantics` lab does; that lesson's lab is the grid
   `quantifier` mode, and the first-order model with names and extensions is
   “Compositional Truth Conditions”. `moores-paradox-and-what-cannot-be-believed`
   cited no earlier lesson at all for the frame condition it leans on; it now
   names the axiom `□p → p` from “Frames, Axioms and What Necessity Obeys”
   and points at the axioms tile, which prints T for the reflexive presets.
8. **The course home claimed a thing the earlier courses do not do.**
   `how_to` said the nine paradoxes met earlier were "each classified by its
   exit where it was met". The ravens, grue, Simpson, Newcomb and Condorcet
   lessons contain no exit classification (the word does not occur in those
   modules); the sorites, lottery, Gettier and Theseus lessons discuss replies
   without the three-exit vocabulary, which this course introduces. The
   sentence now says what is true: each was worked where its tools were
   introduced, and the question asked there is given its general form here.
9. **Small prose faults.** "Three ideas show where it is about"
   (`sleeping-beauty`); "After every gap of the list, he is" where "every" had
   to mean "all together" to be true (`achilles-and-the-tortoise`); "a list in
   which each term is a fixed multiple of the last is a geometric series"
   (that is a sequence; the series is its sum) (`zenos-dichotomy`); straight
   single quotes in the escaped fields of part B where part A uses typographic
   quotes throughout.

## What it claims to teach but does not, and where a learner gets stuck

- **`sleeping-beauty` is not a paradox in the course's sense and the lesson
  knew it** ("so the exit is not the usual one") but did not say what it is
  instead. It is two valid arguments from one prior and two likelihoods to
  credences that cannot both be held, and the exit is to deny the one premise
  on which they differ. One sentence now says so, which keeps the lesson
  inside the course's method without pretending the arithmetic decides.
- **The relation between exit one and exit two was left for the reader to
  discover**, and the reader discovered it at `achilles-and-the-tortoise` as a
  contradiction. It is now taught there (item 1 above). It would sit as well
  in `the-barber-and-the-anatomy-of-a-paradox`, but that lesson already
  carries the definition, the three exits, the barber and the lab's limit, and
  a fifth idea would be one too many for the opening lesson.
- **`the-liar`'s lab does not show the reader what the panel promises in the
  author's instrument, though it does in a browser.** The panel says "pick the
  first formula, p if and only if not p". The option is there (the page's
  `<select>` carries all four formulas, and shipped Discrete Mathematics pages
  carry `<->` in option values and pass CI), but `labcheck.js --observe`
  lists only two of the four options for `ttA`, because its source-level
  option scan (`<option\b([^>]*)>`) ends at the first `>` inside a value, so
  `p <-> ~p`, `p -> ~p` and `~p -> p` are all read as the empty string. A
  reviewer reading the instrument would think the biconditional is missing.
  The page is right; the instrument under-reports. Recorded under remaining
  issues.

## Prerequisite order

Checked backwards across the path. `the-barber-and-the-anatomy-of-a-paradox`
needs validity (“Validity and Soundness”), standard form (“Premises,
Conclusions and Standard Form”), quantifiers (“Quantifiers and Their Order”)
and a first-order model with names (“Compositional Truth Conditions”); all
earlier, and after the fix all cited. `the-liar` needs the truth table of
“Truth Values and the Connectives” and the biconditional of “The
Conditional”. `zenos-dichotomy` introduces the geometric series from scratch,
which is right: no earlier lesson teaches it (“The St Petersburg Game” uses
the `series` mode's `petersburg` kind, whose terms are equal, and the lesson's
note points there as the other side of the same premise). The three
probability lessons need prior, likelihood, Bayes factor and the best act
after updating, all of “Updating on Evidence” and the `update` mode it
introduces, and expected value from “Expected Value and Expected Utility”.
`moores-paradox-and-what-cannot-be-believed` needs Kripke models, frame
conditions and the axioms T, D, 4, 5 (“Necessity, Possibility and Possible
Worlds”, “Frames, Axioms and What Necessity Obeys”) and the epistemic reading
of the box, used once before in “Leibniz's Law and the Masked Man”; now cited.
No violation sits in an earlier course. Inside the course the order is right:
method, then the series three times with the question changing (does it
converge; where; what does convergence not fix), then three posteriors with
the disputed element moving (the prior; the likelihood; the host's rule), then
a paradox with no number in it.

## Philosophical accuracy

- The barber as "a popular form of Russell's paradox" with the same instance
  `s ↔ ¬s` at its heart: right, and the note is careful not to say the two are
  the same. The honest-barber preset is the standard observation that the
  rule can be satisfied if it does not range over the barber.
- The liar: the three premises (self-reference, the T-schema, bivalence
  stated as "true or not true"), the strengthened liar against gap theories,
  Tarski's hierarchy with its price (English has one "true"), dialetheism as
  needing paraconsistent consequence. All stated fairly and in their strongest
  form; the lesson chooses none.
- Zeno and Achilles: the standard modern reply (a convergent series of
  times), with the humility paragraph that the arithmetic does not settle
  whether space is infinitely divisible or whether a body can complete an
  infinite list. The equal-speed preset, where Zeno is right, is a good
  addition to the brief.
- Thomson's lamp: Thomson's reductio and Benacerraf's reply (the description
  determines the state at every time before the minute and says nothing of the
  minute), both at their strongest, now both classified. Benacerraf is not
  named; the lesson is about the argument, as §G asks.
- The two envelopes: the bounded-prior reply is the standard one for the
  open version and is correctly limited to finite priors, with the
  infinite-expectation priors named in the course home as not built. The
  closed version's equivocation diagnosis was missing and is now there.
- Sleeping Beauty: the halfer and thirder positions are Lewis's and Elga's
  as usually reconstructed, including Lewis's two-thirds on learning it is
  Monday and the Monday-night toss in Elga's version. The "P(this waking | H)
  = 1/2" likelihood is one standard formalisation of the thirder and is
  presented as a model, not as the only one.
- Monty Hall: a veridical paradox, which is exit three; the random-host
  variant with 1/2 is correct; the four-door figures are correct.
- Moore's paradox: the omissive form only, which is the form the lab can
  handle; the knowledge version via T, the belief version via KD45 in the
  fourth preset; the definition's tail is now limited to what the lesson
  derives ("nor believed by a believer who knows their own mind"). Hintikka's
  observation that `□(p ∧ ¬□p)` is unsatisfiable in such frames is what the
  lab computes.

## The seam between part A and part B

The two authors agree on voice (careful prose, British spelling, no filler),
on the entity conventions in prose fields, and on the exit vocabulary. They
differed in three ways, all now closed: part A put every argument in standard
form as an `ol` and part B never did (`monty-hall` and
`moores-paradox-and-what-cannot-be-believed` now do; `the-two-envelopes`
has its argument in a `math` block, which is the right form for it); part A
closed each lesson on an exit and part B was inconsistent ("exit one", "the
third", "an exit of the first kind"; now "exit one", "exit three", "exit one");
part A used typographic quotes in escaped fields and part B used straight
single quotes (now typographic). Part A's closing note hands over correctly
("the next three lessons leave the infinite and take up paradoxes in which
every number is finite"), and part B's first concepts_intro picks up at the
right altitude.

## Changes made

- `__init__.py`: `how_to` no longer claims the earlier paradoxes were
  classified by exit.
- `the-barber-and-the-anatomy-of-a-paradox`: the model-evaluation
  cross-reference now names “Compositional Truth Conditions” beside
  “Quantifiers and Their Order”.
- `zenos-dichotomy`: a fifth step naming the exit and its price; "added up"
  in the first concept.
- `achilles-and-the-tortoise`: the exit paragraph rewritten to teach that
  faulting a step which borrows an unstated premise and denying that premise
  are one repair; a fifth step; the standard asks for the exit and the
  unstated premise; "after all of the gaps together, which is the limit, he
  is level".
- `thomsons-lamp-and-supertasks`: the argument's conclusion added as a fifth
  line and the premise under attack renumbered; both replies classified as
  exit one against different premises with their prices; a fifth step; the
  standard asks for the premise each reply denies.
- `the-two-envelopes`: the closed version's equivocation named as exit two
  and the open version's premise as exit one, in one paragraph; the first
  concept retitled; “Updating on Evidence” and Decision and Rationality by
  title; the standard-reply quiz question says the envelope is open;
  typographic quotes.
- `sleeping-beauty`: “Updating on Evidence”; "what it is about"; one sentence
  setting the puzzle out as two arguments that differ in one premise;
  typographic quotes.
- `monty-hall`: the two-thirds argument in standard form; the exit paragraph
  rewritten around it; the fifth step names the exit; the standard asks for
  it; the true distractor replaced and the right-number-wrong-reason
  distractor's `why` rewritten; typographic quotes.
- `moores-paradox-and-what-cannot-be-believed`: the paradox in standard form;
  “Leibniz's Law and the Masked Man” for the epistemic reading and “Frames,
  Axioms and What Necessity Obeys” for `□p → p`, with the axioms tile named;
  the sincerity sentence corrected; the definition's tail limited to what is
  derived; "exit one"; the vacuously true distractor replaced and the
  ambiguous one ("the paradox arises for any frame") made definite, with both
  `why`s rewritten; typographic quotes.
- `content/spoken/philosophy_c10_paradoxes.py`: a spoken form for `□p → p`
  under this course's epistemic reading of the box.

Lesson slugs, count and order are as `COURSES.json` lists them. The preview
(`scripts/preview_subject.py philosophy --course paradoxes-and-their-exits`)
reports OK: ten pages, nine labs executed and swept, eight pages with
fifty-five pinned figures all matching, no math run guessed at.

## Remaining issues

- `labcheck.js --observe` lists two of the four options of the liar's
  formula menu: `selectsOf` matches `<option\b([^>]*)>`, so the attribute
  scan ends at the first `>` inside a value, and every option whose value
  contains `->` or `<->` is read as the empty string. The sweep in `runPage`
  uses the same scan (`controlValues`), so those options are never swept on
  `the-liar`, nor on any `truth_table` page whose menu carries a
  conditional (“The Conditional” in Arguments and Validity, and the Discrete
  Mathematics logic pages). The pages are correct and CI's well-formedness
  check accepts them. The fix is to the instrument (escape `>` in the scan, or
  escape the option markup in `logic.truth_table`), which is
  `@lab-arithmetic`'s, not the course's.
- `moores-paradox-and-what-cannot-be-believed` is the heaviest lesson in the
  course: knowledge against belief, reflexivity, dead ends and introspection,
  four presets and now a standard-form argument. It is one lesson by PLAN §C
  and the URL space is fixed; if the Subject is ever re-cut, the KD45 preset
  and the knowledge/belief distinction are the natural second half.
- `the-two-envelopes` now carries two versions of the puzzle (closed, exit
  two; open, exit one) in one paragraph. That is the price of stating the
  puzzle at its strongest, and it is the second-hardest lesson for the same
  reason; the lab serves only the open version, which the paragraph says.
- `sleeping-beauty` presents one formalisation of the thirder's likelihood
  (`P(this waking | H) = 1/2`). Other reconstructions (Elga's indifference
  over centred worlds, Lewis's own) reach the same figures by a different
  route; the lesson's note says real work weighs both costs and some reject
  both models, which is honest, but a reader who meets the literature will
  find the likelihood route is one of several. Not changed: the lab computes
  from a likelihood and the course has no mode for centred worlds.
- The earlier courses do not use the three-exit vocabulary for the paradoxes
  they teach (ravens, grue, Simpson, Newcomb, Condorcet, lottery, Gettier,
  Theseus, sorites). The course home no longer claims they do. Whether each
  of those lessons should close with "name the exit" is a question for the
  assessments of those courses, not this one.
