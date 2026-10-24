# Pedagogy assessment — Things, the World and Others (Phenomenology of Perception, course 6)

Formed from the seven lesson dicts in `content/phenomenology/c6_things_others/`
(`part_a.py`, the four lessons on Part Two Chapter 3 up to the natural world;
`part_b.py`, hallucination and the two lessons on Chapter 4; `__init__.py`,
the course dict) and the kit they render through (`scripts/mathpath/labs/
phenkit.py`, modes `size/constancy`, `light/ratio`, `cases/table` twice,
`cues/sequence`, `variation/core`, and the Philosophy Subject's
`argkit/validity`), on branch `feat/phenomenology-subject` before the Subject
was wired into the site. The design authority is `docs/phenomenology/PLAN.md`
§0 (the one question and the three families of lab), §B, the Course 6 entries
in §C, §D as summarised in `docs/phenomenology/kit-report.md`, §E (how a book
in copyright is quoted) and §F (the voice), with the "Lessons from" sections
of `docs/phenomenology/AUTHORING.md`, which the pilot's two reviews wrote for
every later course. The model for this document is the Course 1 assessment.

Every lesson was read in full before anything was changed. The whole of
Chapter 3, The Thing and the Natural World (Smith pp. 348–402), and the whole
of Chapter 4, Other Selves and the Human World (pp. 403–425), were read first,
then each lesson's passage and the pages it reads line by line, with the three
pages outside the two chapters the lessons cite (p. 346 for the stone on the
sunken road, which the natural-world lesson places there and not here; the
Course 2 and Course 5 lessons named by title for the constancy hypothesis, the
glass, the spatial level and the stone). Every pinned tile on the seven pages
was read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py phenomenology --course
perception-things-world-and-others`), every figure in prose, key lines, worked
lines and quiz `why`s was recomputed by hand, every `data-say` on the pages
with arithmetic was read, and every span in `&ldquo;…&rdquo;` was run through
the Subject's quotation checker (`phen_quotes.py`), the opening passages
checked by eye against the page. Lessons, in course order:
`size-and-shape-constancy`, `colour-and-lighting`, `the-thing-and-the-real`,
`the-natural-world`, `hallucination`, `the-cultural-world-and-others`,
`the-truth-of-solipsism`. The course is marked Advanced and assumes the
courses before it; it is judged against a reader who has those and no
philosophy beyond them.

A second reviewer was reading the same course at the same time and changed
`part_a.py` while this pass was under way. Those changes were read after they
landed, are noted where they bear on a finding, and are not claimed here.

## Verdict

The course teaches its subject. A reader who finishes it can compute what a
retinal-image account and an unconscious inference each predict for the size
of a distant person and place a reported size between them on Brunswik's
ratio; compute luminances and ratios to a surround for Gelb's disc and say,
exactly, what putting a paper in the beam changed and what it did not; code
two opponent accounts against a chapter's observations, read each account's
record, the survivors and the split, and say which observation a record
depends on; follow a sequence of cues through a shrinking list of
interpretations and say what the list never contained; intersect a coded set
of perceived things to find a core and name what a reported hallucination
lacks of it; and write the argument from analogy in sentence letters, find its
one counterexample row, repair it, and see that the repair, and the circle,
are valid. Those are the acts the seven `standard` fields name and the quizzes
measure; no objective is "understand X". The `mistakes[0]` of every lesson is
the §C misconception, and each is refuted with the lesson's own figure: the
inference "done right" predicts `170 cm`, perfect constancy, "with no room
for a report in between"; the disc's luminance "stays `4/5`" when the paper
goes into the beam and only the surround changes; the sum of qualities "fails
the hot object and the carpet" and the mind's binding "fails the carpet and
the aloof thing"; the candidates "are all interpretations of something there;
dropping one never produced nothing"; the hallucination "keeps only
*real-for-me*"; the repaired analogy "is valid" and "the chapter's objection
survives the repair"; and the table "shows only the first half" of the
solipsism lesson's two claims. All 54 pinned tile strings on the seven pages
match the lab, and every figure in prose agrees with the lab or with a
recomputation.

Fidelity to the two chapters is high, and the hard part of these chapters,
whose voice a sentence is in, is handled well. Every quoted span is in Smith's
text character for character (the checker reports OK with no misses; the
quotation budget is 106, 141, 100, 112, 146, 105 and 149 words of the 150
allowed, and the opening passages 61, 65, 50, 36, 49, 45 and 55 of 70). The
law view of size is given "two pages in its own words before questioning it";
the analogical reply is "given on page 406 in the voice of the theory the
chapter is about to question"; the objectifying look is "introduced as
something asserted"; the memory colour is "in the empiricist's voice"; Alain
and Montaigne carry the intellectualist account of hallucination. Each `note`
names what its lab cannot settle, and the patients of the hallucination pages
are treated as the book treats them, with a sentence in the body and in the
course `how_to` saying that the lab codes the reports and not the people. The
defects found were local and are repaired: a quiz distractor whose
explanation did its arithmetic wrong (`1/10 m` said to be "6/30"); a sentence
that put Gelb's result on the wrong object (the paper "appears black" where
Smith's "the former" is the box); a footnote's first sentence reported as its
conclusion; *a priori* and *transcendence* unglossed in a course that assumes
no philosophy; the hallucinated man coded as lacking *seen* with no page given
for it; a living author told what he "would see"; Sartre named as the
chapter's target in the lesson's own voice where the concept and §C say
"widely read as"; the family-1 cues lab called "the lesson's model"; the
retinal-image account and Mill left without the holder or the disclaimer the
lesson gives Helmholtz; and *modus ponens* used in a key line and a quiz
without being said in the body. Nothing needs splitting, merging or
reordering.

## The voice, judged against §F

**What works, and should be kept:**

- **The passage first, then the pages in the chapter's own order.** Every
  body opens with `<strong>Part Two, Chapter n, p. m.</strong>`, the passage,
  the page, and an exact reading range that is the range the lesson then
  reads ("from its first page, 348, to the paragraph on page 354 that turns to
  colour"; "from the paragraph on page 414 that asks whether it is indeed
  other people we arrive at to the end of the chapter and of Part Two on page
  425"). This is the rule the Course 1 assessment asked for and all seven
  lessons keep it. Then each lesson returns to the passage a phrase at a time:
  "A *substratum*, a *vacant X*, a *subject in which properties inhere*:
  three names for the traditional picture of a thing as an unknown bearer
  under its qualities, and the chapter rejects all three"; "It is *not
  accessible*: no path leads from it to the rest of the patient's experience,
  or to anyone else's"; "*The truth of solipsism is there.* But I can fly
  from being only into being, the chapter goes on".
- **Scenes rationed to one.** Only the first lesson opens with the reader's
  world (someone walking away down a corridor and waving), and it reaches
  the chapter's category in the second sentence. The other six open with the
  text: the brown table, the moon's disc and the skull, the crystal cube, the
  patients' reports, nature at the centre of subjectivity, the chapter
  doubting its own result. §F.2's ceiling is half; the course uses a seventh,
  and since the chapters' own cases are vivid (the pen held to the eye, the
  arc lamp on the disc, Chartres from the road, the powder in the bed, the
  baby's finger between my teeth, Paul's stolen watch) nothing is lost.
- **The history of ideas with people in it.** Kant is "the Königsberg
  philosopher whose *Critique of Pure Reason* (1781) made the mind's own
  forms the conditions of any possible experience"; Helmholtz "the German
  physicist and physiologist whose *Treatise on Physiological Optics*
  (1856–67) called it unconscious inference"; Hering "the physiologist" who
  "called it memory colour"; Katz "a German psychologist whose book on the
  world of colour the chapter draws on throughout"; Gelb "the Frankfurt
  psychologist who also studied the patient Schneider with Kurt Goldstein";
  Wallach's principle "published in 1948, three years after the book";
  Novotny "the art historian"; Scheler "the German phenomenologist whose
  book on sympathy (1913, revised 1923) argued that we perceive other minds
  directly"; Mill, who "gave it its best-known form in 1865, as an inference
  from like effects to like causes"; Piaget "the Swiss psychologist";
  Sartre's *Being and Nothingness* (1943) with its "shame". Each opponent
  gets his fact before the chapter's reply.
- **Whose voice, every time.** The `how_to` warns that "these chapters state
  the psychologist's, Kant's and the objectifying look's views at length in
  their own words before answering them", and the lessons do it: "The first
  answer is given in the voice of 'the psychologist'"; "the easy answer,
  given on page 406 in the voice of the theory the chapter is about to
  question"; "Being in itself and being for itself, and the impossible
  demand that another person be both, are objective thought's terms, set out
  on page 407 to show why it has no room for others"; "the chapter introduces
  it as something asserted". Where the chapter does not name a holder the
  lesson says so and names one as its own: Helmholtz, Brunswik, Wallach,
  Mill, Sartre.
- **Presented, not endorsed, and the limit admitted.** "Whether that reading
  of Kant is fair is a question the chapter does not stop to argue." "That is
  as far as a lab can go, and the chapter goes further." "Neither the chapter
  nor the lab settles the dispute." "The chapter does not refute the first;
  it says what it cannot reach." The one modern aside is in Hallucination, in
  the second-last `p` as §F.1 and §C require, and it gives both sides: the
  chapter's one primordial function and "the initiative comes from us" on
  Seth's side, the shared world on the chapter's, and "neither … settles the
  dispute". It names *Being You* (2021) and says only that Seth did not coin
  the phrase, which is what §C allowed after the attribution could not be
  confirmed.
- **The patients as patients.** The hallucination lesson says in its second
  paragraph that "they were people in hospital care, reported as the clinical
  literature of the time reported them", names the psychiatrists, and says
  "the lab codes those reports, not the people they describe"; the `note`,
  the `panel_intro` and the course `how_to` say it again. The man in the
  garden, the old woman and the powder, the doctor in the boat, the woman at
  the market are given as the book gives them and never for an effect.
- **The chapter's own summary lines carry the summary.** "I am not the
  spectator, I am involved"; "colour in living perception is a way into the
  thing"; "It is not seen itself, but causes us to see the rest"; "In order
  to perceive things, we need to live them"; "I experience the unity of the
  world as I recognize a style"; "The hallucination is not a perception, but
  it has the value of reality"; "reasoning by analogy presupposes what it is
  called on to explain"; "Solitude and communication cannot be the two horns
  of a dilemma, but two 'moments' of one phenomenon". The budget is spent
  where the Course 1 assessment said to spend it.
- **Second person, warm, no performance.** "Hold a fountain-pen up to your
  eye so that it hides the whole scene, and it stays small"; "Now look at
  what was never in the list"; "that is a description to test against your
  own experience of a conversation". No "let's", no exclamation mark, no
  first-person anecdote, no slang anywhere in the course. The one light touch
  is the chapter's own ("a dog's gaze embarrasses no one").
- **Pointing forward by title.** Every body ends by naming the next lesson's
  title and its first object, and the last lesson names the next course by
  its §B title and its first lesson, "The Cogito and the Certainty of
  Seeing", which is the title §C gives it.

**What was changed here, and what the authors of later courses should take
from it:**

- **The holder of a model the lab computes is named even when the lesson,
  not the book, supplies him.** The size lab named Helmholtz for the inference
  and said the chapter does not name him, but left "the retinal-image
  account" with no holder; the body now says it is the constancy hypothesis
  of Classical Prejudices applied to size. The analogy lesson credited Mill
  in a concept and in the body without saying, as it did for Helmholtz, that
  the chapter does not name him; it now does.
- **A living author is stated, not ventriloquised.** "Seth would see his view
  in that" told a living writer what he would think. It now reads "a reader
  of Seth can point to that". The chapter's opponents are dead and the book
  answers them; the modern aside answers nobody and should not speak for
  anybody.
- **When a cell is coded from a page, give the page.** The vision preset codes
  the hallucinated man as lacking *seen*, which is right (p. 397: the thing
  in hallucination "is never seen and is never visible"), but the body gave
  the four world-properties their pages and this one none. One clause added.
- **"Widely read as" in the concept must be "widely read as" in the body.**
  The solipsism lesson's concept and `note` say the objectifying look is
  "widely read as Sartre's", as §C requires because the chapter does not name
  him; the body said "That is the analysis Jean-Paul Sartre gave". Aligned.
- **A family-1 lab is "the model the lab computes", not "the lesson's
  model".** The cues lab is family 1 (the sceptic's picture); "the lesson's
  model" is §0's phrase for family 3 and would have told a reader the lesson
  built the judgement-from-signs account. Reworded.
- **Gloss the chapter's Latin and its terms of art in the sentence.** *A
  priori* carried the weight of a whole table cell and was not glossed;
  *transcendence* (p. 380) was not glossed; *modus ponens* appeared in a key
  line and a quiz `why` and nowhere in the body. All three now have an
  English phrase beside them on first use. *Apodeictic* ("the certainty of a
  proof"), *natural attitude*, *Urdoxa*, *in itself* and *for itself*,
  *phenomenal body* were already glossed and are the pattern.
- **A footnote's first sentence is not its conclusion.** The Koffka note on
  p. 353 opens with "constancy … is not an intellectual function, but an
  existential one"; the lesson said "the note concludes". Now "begins by
  saying". Small, but a reader following in the book looks for it at the end.
- **The object of a reported result must be the text's.** "Put a white paper
  in the black box and at once it appears black and strongly lit" let the
  paper appear black; in Smith "the former", the black box, does. Now "the
  box appears".
- **Argue each wrong answer's explanation as well as the answer.** The
  lamp-post question's `1/10 m` was said to "forget the standard distance",
  but forgetting it gives `6/30 = 1/5`. The distractor is now `1/5 m` and the
  `why` shows the division.

## What the course teaches well

- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names the product and whose it is:
  "compute both predictions and the ratio, and say whose each is"; "compute
  Gelb's luminances and ratios and say what the paper changed"; "count the two
  accounts and state the chapter's alternative"; "test the argument, repair
  it, and say why the repair does not answer the chapter". The six course
  `outcomes` are the same acts, with a sixth that is the reading's: state
  five accounts at strength and the chapters' reply to each.
- **One hard idea per lesson, in the chapters' own order, at the splits §B
  and §C fix.** Chapter 3's four parts, which Smith marks only by a blank
  line, are located by page in the `part_a.py` docstring and in each
  lesson's reading range, with the constancies split at p. 354 where the
  chapter turns to colour; Chapter 4 is split at p. 414, where it asks
  "whether it is indeed other people that we arrive at", and the solipsism
  lesson says it is reading the baby and the dialogue back from the previous
  lesson's pages. The pages on touch and weight, and Chapter 4's pages on
  class and nation, are summarised in a paragraph each and the course
  `not_covered` says so.
- **The arithmetic is right and each figure is attributed.** `170 × 2/8 =
  85/2`; `(85/2) × 8/2 = 170`; `(85/2) × 4/2 = 85`; `(160 − 85/2)/(170 −
  85/2) = (235/2)/(255/2) = 47/51 ≈ 92.2%`; the disc `1/20 × 16 = 4/5`, "exactly
  the white paper's luminance in the room"; `(4/5)/(1/2) = 8/5` with the wall
  as surround and `(4/5)/(64/5) = 1/16` with the paper; one counterexample row
  in eight, none in eight with `q → r`, none in four with `r` among the
  premises. The lesson says each time that the person, the distances, the
  reported 160 cm, the reflectances and the beam's 16 are illustrative, that
  the chapter "gives no figures for Gelb's experiment", that the candidates
  and cues are the lesson's "since the chapter gives none", and that the
  coding of every table is the lesson's.
- **The labs earn their place, each for a stated reason.**
  - *Size* (family 1, two named models and the lesson's measure) computes
    the two classical predictions and shows that the inference, done right,
    predicts full constancy "with no room for a report in between", which is
    the lesson's way of making the chapter's objection to the law view
    concrete: it treats sizes as "already determinate". The `misjudged`
    preset shows that the inference "predicts a figure" either way, which is
    "the point the chapter presses next".
  - *Light* (family 1, the empiricist's luminance and Wallach's later ratio)
    is the best lab on the course. The `gelb` and `paper` presets hold the
    disc's luminance at `4/5` and change only the surround, so the reader sees
    on the page that the empiricist's sensation "cannot tell the two
    situations apart" and the later ratio can; then the lesson refuses to let
    the ratio stand in for the chapter ("A ratio is a relation between two
    figures; the chapter's claim is about the organisation of a field").
  - *Cases* twice (family 2) does what §0 asks: the opponents only, the
    chapter's own account "stated here and not scored", the coding admitted
    to be an interpretation cell by cell, and a preset (`alien`, `infant`)
    that lets one account survive so the reader sees that "a record depends
    on which observations are on the table".
  - *Cues* (family 1) is used against itself, as the Course 1 faces lab was:
    the count falls 3, 2, 1 and the lesson's point is the fourth step, "Ask
    what was never a candidate". The step slider and its clamp in the `first`
    preset are explained.
  - *Variation* (family 2) makes the chapter's list of what a hallucination
    lacks into something a reader can see fail: the `all` preset's core is
    the four world-properties and *real-for-me*, the senses vary, and "what
    every perceived thing has, on this coding, is not a sense but a place in
    one world".
  - *Validity* (family 1, the logic "undisputed") sets out the argument from
    analogy and then shows, with the `circle` preset, exactly what the chapter's
    objection is not: the lab "calls it valid, and it is", and "no truth
    table can catch it". The `note` says the lab "cannot see circularity",
    which is the right use of a truth table in a lesson whose point is that
    the fault lies in how a premise is known.
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first preset by hand; every `panel_intro` asks for a
  comparison before the press ("Compare the gelb and paper presets"; "Move the
  step slider in the all preset and watch the count fall"); every quiz asks
  the same act on a fresh instance (a lamp-post at 30 m; a grey card under a
  lamp; a hedge, a wall and a barn; variants A, B, C and D; `p`, `p → q`; two
  accounts and three cases).
- **The cross-references are right.** The stone is on p. 346 and belongs to
  Lived Space; the glass to The Unity of the Senses; the level to Up and
  Down; the ship to Attention and Judgment; the angular size to Description,
  Not Explanation; the reply to the sceptic to p. 401 in the hallucination
  pages, which the natural-world lesson says. Each title exists in §C
  exactly as cited. The Part's title in the course `summary`, "The World as
  Perceived", is Smith's.

## What it taught badly, or said wrongly

### Fidelity

- **`colour-and-lighting`, body (the two boxes):** the paper "appears black".
  Repaired.
- **`size-and-shape-constancy`, body (Koffka):** "the note concludes".
  Repaired.
- **`the-truth-of-solipsism`, body:** "That is the analysis Jean-Paul Sartre
  gave". Repaired to "widely read as".
- **`hallucination`, body:** "Seth would see his view in that". Repaired.
- **`hallucination`, body (vision preset):** *seen* coded as lacking, with
  no page. Repaired with p. 397.
- **`the-natural-world`, body:** "The lesson's model is the sceptic's
  picture". Repaired.
- **`size-and-shape-constancy`, body:** before the second reviewer's pass the
  Kant paragraph called Kant "the view's best advocate" and the "constant
  product" sentence "the passage's statement of its consequence"; Smith has
  "with Kant, see that it refers to the positing of a world", and the product
  is what the object is "for science and objective thought". The second
  reviewer reworded both during this pass; read after they landed, the new
  wording is faithful.

### Prose that left the reader unexplained

- *A priori*, *transcendence*, *modus ponens*: unglossed. Repaired.
- The retinal-image account's holder and Mill's absence from the chapter.
  Repaired.

### Quiz

Every distractor on the twenty-eight questions was argued for. Twenty-seven
could not be defended. The one that could be argued against was the
lamp-post item, whose `1/10 m` was not a named error at all; it is now `1/5
m`, the answer that forgets the standard distance. Two items are worth
recording without change: the colour lesson's `12/10 and 12/5` pairs the right
luminance unreduced with a wrong ratio, which is a legitimate distractor but an
odd one to read; and the hallucination lesson's fourth item asks about "the
lesson's aside", which tests the lesson rather than the chapter (see
recommendations). The best conceptual items are the solipsism lesson's third
("When, according to page 420, does the other's gaze transform me into an
object?"), whose three distractors are "whenever he looks", "only when he
speaks" and "never, since the look is Sartre's error", each of which the page
rules out in a clause; and the analogy lesson's third, which asks why the
circle preset is valid and makes the reader say what circularity is not.

### Speech

Every math run on the seven pages was read from `data-say`. The figures read
well: "170 times 2 over 8 equals 85 over 2", "the quantity 85 over 2, times 8
over 2 equals 170", "q implies r", "p, q, so r, 8 rows, 1 counterexample". The
key lines that begin with "the" ("the real size, the thing at its best
distance") are read as words, not spelt, so the three-letter rule from the
Capital brief is not tripped; the cell codes "n" and "y" in the worked lines
are read as letters, which is what they are. The preview lists no unspoken
run.

### Cross-references

Lessons by title, the book by Part, chapter and page, the next course by its
§B title: all as §0's first deviation requires. No lesson is cited by number.

## Can a reader of the earlier courses follow the seven lessons?

Yes, and the places they will slow down are the chapters' own.

- **Lesson 1** is the course's clearest, because the lab gives the reader
  something to hold while the chapter does its hardest move. The psychologist,
  the law view and Kant arrive in order, the two predictions are computed
  before the chapter's reply, and the reply ("not a size which increases or
  decreases, but a tension which fluctuates round a norm") is given its
  everyday case, the picture in the gallery and the skin under a magnifying
  glass. The Koffka footnote ties the course back to the moon of Course 1.
- **Lesson 2** carries the most material (Hering, Katz's modes, the screen, the
  two boxes, the disc, the painters, the flat, the level, weight and touch) and
  keeps it in the chapter's order; a reader will manage because each
  experiment is stated in one sentence and the lab holds the one that matters.
  The paragraph that refuses to let Wallach's ratio be "the chapter's
  explanation" is the one to copy: it is the Subject's material clause done
  with a specific figure.
- **Lesson 3** is where a reader with no philosophy meets a table for the first
  time in this course, and the lesson protects them: the two accounts are
  stated "at their strength" in a paragraph each before any cell is coded, and
  the coding paragraph gives a reason for every cell. The die and its four
  reductions are the hardest page and are read as the text reads them, as a
  series "reflection performs", not as the order of perception.
- **Lesson 4** moves from the style of a person to the horizon of all horizons
  by way of Chartres, and the cues lab is small enough not to distract. The
  temporal resolution of the contradiction (pp. 385–7) is the chapter's
  densest page and the lesson keeps it to one paragraph with the sentence that
  carries it ("If I am at all times and everywhere, then I am at no time and
  nowhere").
- **Lesson 5** is the one a reader will remember. It opens with the patients
  and lets them speak in the book's words, states both classical accounts
  before rejecting them, reads the passage phrase by phrase, and only then
  shows the table. The aside on Seth is late, fair and short. What a reader
  will miss is the chapter's own sentence that the normal person "is equally
  afflicted with this gaping wound" (p. 399), which the lesson paraphrases;
  with four words of budget left after the second reviewer's pass, it would
  need a shorter quotation dropped to make room.
- **Lesson 6** asks the most of a reader (the cultural object, the two modes of
  being, the third genus, the baby, the truth table, the circle, the vortex,
  Piaget and Hegel) and is the lesson a philosophy teacher would be most glad
  to have: the circle preset is a real pedagogical find, because it lets the
  reader see with their own count that "a circular argument is perfectly
  valid" and so that the chapter's objection is of another kind.
- **Lesson 7** holds two claims that seem to exclude each other and says so in
  its first line. The table does the first half and the prose the second,
  which is exactly §0's division; the `steps` say it in one line ("The case
  both absorb is the truth the chapter grants solipsism; the case both fail
  is the coexistence it says is lived beneath it"). The Waterloo paragraph
  earns its place as the chapter's last example and is not over-read.

## Repairs made in this pass

In `content/phenomenology/c6_things_others/part_a.py`:
`size-and-shape-constancy` the `far` paragraph (the retinal-image account's
holder), the Koffka paragraph ("begins by saying"), and quiz 1 (`1/5 m` and its
`why`); `colour-and-lighting` the two-boxes paragraph ("the box appears");
`the-thing-and-the-real` the coding paragraph (*a priori* and *transcendence*
glossed); `the-natural-world` the lab paragraph ("the model the lab
computes"). In `part_b.py`: `hallucination` the vision-preset paragraph (p. 397
for *seen*) and the Seth paragraph ("a reader of Seth can point to that");
`the-cultural-world-and-others` the `valid` paragraph (*modus ponens* said) and
the `analogy` paragraph ("Mill, whom the chapter does not name");
`the-truth-of-solipsism` the look paragraph ("widely read as"). Nothing in
`__init__.py`. No preset, `expect`, slug, module, lab key, mode, view, cfg key
or observation string changed.

The second reviewer's concurrent changes to `part_a.py` (the law view as what
"looks at first, the chapter says, like a way round the question"; Kant as
"where the view leads"; the product as what the object is "for science and
objective thought"; Helmholtz as unnamed with "the same computation"; Brunswik
"who proposed it around 1930"; and the first mistake's wording) were read
after they landed and are consistent with the text and with this assessment;
none is claimed here.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and §C
list them, and every instance the lessons carry is the one §C's "Checked"
paragraphs record. `python3 scripts/preview_subject.py phenomenology --course
perception-things-world-and-others` reports OK: 8 pages, every lab executes
and survives the sweep, every pinned figure on the seven pages matches, no
math run without a spoken form. `phen_quotes.py c6_things_others` reports OK:
no span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **§C's lesson 4 entry is self-contradicting.** Its "Checked" paragraph
  replaces the stone, the puddle and the patch of sunlight with the poplars,
  the village church and Chartres, which is what the lesson carries; but the
  entry's **Lab** and **Worked** lines still list the stone candidates and
  "*nothing there* is never a candidate". The author should rewrite those two
  lines to the instance as built (PLAN.md is outside this assessment's
  files).
- **§G still says Brunswik's ratio is "later than the book".** It is from
  about 1930, as §C's lesson 1 entry and now the lesson's `def` say; §G's
  sentence should say "Wallach's ratio principle later than the book,
  Brunswik's ratio not used by it".
- **The hallucination quiz's fourth item tests the lesson's aside, not the
  chapter.** A chapter item would serve the reader better and the page has
  two ready: where the hallucination is ("not in the world but 'before' it",
  p. 396, because the body has lost its insertion in the system of
  appearances), or what the sun's rising shows (p. 401, that the percept is
  "on the hither side of doubt and demonstration"). The aside could stay in
  the `why` of another item or be left to the prose.
- **The look's `y` for the baby is the weakest cell on the course**, and the
  lesson says so twice ("coded y for the look only because the look's account
  gives the other without inference"; the `note`). An alternative the author
  may prefer is `-`: the objectifying look is an account of being seen, and
  the baby is not looking at anyone as an object. That coding would make
  `caSplit` read `none` in the `all` preset and the `infant` preset would show
  no survivor, so the prose and three `expect`s would change with it; the
  present coding is defensible and is admitted, so it is left.
- **The hot object's `n` for empiricism** could likewise be `-` (the `note`
  says so). Left, for the same reason.
- **Two sentences of the chapters' own that are not quoted and would fit the
  budget:** "the normal person is equally afflicted with this gaping wound
  through which illusion can make its way in" (p. 399; lesson 5 now has
  four words left, so one of its shorter quotations would have to go) and
  "The real lends itself to unending exploration; it is inexhaustible"
  (p. 378; lesson 3 has fifty).
- **The `caPair` select** renders on both `cases` pages with one option and
  is not mentioned in prose. Harmless; recorded so the "every tile" rule is
  not read as broken.
- **Lesson 2's reading range runs to p. 370 and the body summarises pp.
  365–70 in two sentences.** A reader who follows the instruction reads five
  pages on weight and touch that the lesson then passes over; the `not_covered`
  says so, and the summary gives the one sentence that matters (p. 367). A
  clause in the opening `p` ("the pages on weight and touch, from page 365,
  are summarised at the end") would spare the surprise.

## Lessons for the remaining authors

1. **Name the holder of every model a lab computes, and say when the chapter
   does not name him.** This course does it for Helmholtz, Wallach and Sartre
   and now for the retinal-image account and Mill. It is the rule from Course
   1 ("name the voice of every paraphrase") applied to the labs.
2. **Where the lesson codes a cell, give the page for the cell**, not only for
   the observation. The vision preset's *seen* was right and unsupported on the
   page.
3. **Do not speak for a living author.** State the modern view and what in the
   chapter bears on it, as §F.1 says; "X would see" is a verdict the lesson
   has no page for.
4. **Keep "widely read as" consistent across concept, body, `note` and
   `mistakes`** when a view the chapter answers is unnamed in the text.
5. **Family words are not interchangeable**: "the lesson's model" is family
   3, "the model the lab computes" or the model's own name is family 1, "the
   lesson's coding" is family 2.
6. **Gloss Latin and the logician's names in the sentence** (*a priori*,
   *modus ponens*, *apodeictic*), as this course glosses the German and the
   French.
7. **Check the arithmetic in the `why` of every distractor, not only in the
   right answer**; a wrong error named for a wrong answer teaches the error.
8. **Split a chapter where the book turns, and tell the reader the page.**
   Both docstrings and every reading range here do that for a chapter Smith
   does not subdivide; the pattern is worth copying for Part Three.

Final lines. Preview: `OK` (8 pages rendered; labcheck, every lab executes:
7 page(s) executed and swept, 0 failing; labcheck, pinned figures match: 7
page(s) executed and swept, 7 with pinned figures, 0 failing). Quotation
checker: `OK` (106, 141, 100, 112, 146, 105, 149 quoted words; openings 61, 65,
50, 36, 49, 45, 55).
