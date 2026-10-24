# Pedagogy assessment — Classical Prejudices (Phenomenology of Perception, course 2)

Formed from the five lesson dicts in `content/phenomenology/c2_prejudices/`
(`part_a.py`, Chapter 1 of the Introduction in two lessons and Chapters 2, 3
and 4 in one each; `__init__.py`, the course dict) and the kit they render
through (`scripts/mathpath/labs/phenkit.py`, modes `grouping/proximity`,
`stimulus/illusion`, `cues/pattern`, `cues/sequence`, `cases/table`), on
branch `feat/phenomenology-subject` before the Subject was wired into the
site. The design authority is `docs/phenomenology/PLAN.md` §0, §B, the
Course 2 entries in §C, §D as summarised in `docs/phenomenology/kit-report.md`,
§E and §F, and `docs/phenomenology/AUTHORING.md` with its three "Lessons from"
sections, which this course is the first to have been written under. The
Course 1 assessment (`phenomenology-perception-what-phenomenology-is.md`) is
the model for shape and depth, and its eleven lessons for the remaining
authors are used here as a checklist.

Every lesson was read in full before anything was changed. The whole
Introduction (Smith pp. 3–74, all four chapters with their footnotes) was
read first, then each lesson's passage and the pages it reads line by line.
Every pinned tile was read off the rendered page with `node scripts/labcheck.js
--observe` (rendered through `scripts/preview_subject.py phenomenology
--course perception-classical-prejudices`), every figure in prose, worked
lines and quiz `why`s was recomputed by hand, every `data-say` on the five
pages was read, and all 32 spans in `&ldquo;…&rdquo;` were run through the
Subject's quotation checker (`phen_quotes.py`) and the opening passages
checked by eye against the page. Lessons, in course order:
`the-idea-of-pure-sensation`, `the-constancy-hypothesis`,
`association-and-the-projection-of-memories`, `attention-and-judgment`,
`the-phenomenal-field`. The course assumes Course 1 and school arithmetic,
and is judged against that.

A second reviewer was reading the same course at the same time and changed
the same file while this pass was under way. Those changes are noted where
they bear on a finding and are not claimed here.

## Verdict

The course teaches its subject, and it meets the brief that Course 1's
review wrote for it. A reader who finishes it can cut a row of measured dots
into groups by a stated proximity rule and say that the grouping is in no
dot; compute what the constancy hypothesis predicts for two measured lines,
the signed gap to a report, and say what calling that gap an illusion
assumes; count the remembered words a pattern of seen letters and a context
leave, and say that the pattern and the context, both present, did the
selecting; run a judgement-from-signs model through ordered cues to the step
at which it decides, and set that step beside the walk along the shore; and
read a coded table of the Introduction's cases for each account's record,
the survivors (none) and the rows on which the two accounts part. Those are
the acts the five `standard` fields name and the quizzes measure. The
`mistakes[0]` of every lesson is the §C misconception, each refuted with the
lesson's own figure: the dot at 4 that did not move and lost its partner
(`{4, 5}` to `{4}`); predicted `0 cm`, reported `2 cm`, gap `2 cm`, "every
figure a measurement or a report and none of them the figure as seen";
`ho_se` leaving two words and `_a_e` eighteen until the context door leaves
`gate`; the `ship` preset that keeps `2` at every step and never concludes;
the `intro` table on which neither account survives "without any row being
an inner state". All 43 pinned tile strings on the five pages match the lab,
and every figure in prose agrees with the lab or with a recomputation.

Fidelity to the Introduction is high, and it is high in exactly the place
Course 1's review said the Introduction would be dangerous: whose voice a
sentence is in. The Introduction states empiricism, intellectualism, Alain,
Lagneau, Descartes, Bergson, Hering and the Gestalt psychologists for a page
at a time before answering, and the lessons name the speaker every time:
"in the empiricist's voice", "as the theory itself describes it", "the
intellectualist has a test, and the chapter reports it from Alain", "That is
physiology's premise, as the chapter states it", "Lagneau adds", "the
chapter's example of how that goes wrong". No paraphrase presents an
opponent's observation as the book's, which was the pilot's one fidelity
error. Every one of the 32 quoted spans is in Smith's text character for
character (the checker reports OK; quotation budgets 86, 110, 85, 129 and
109 of 150; openings 48, 40, 47, 56 and 68 of 70). The defects found were
small and are repaired: two quotations whose first letter did not match the
text's case; the `_` in the reading lab's patterns read aloud as "sub", so
that a listener heard "ho sub se" where the page shows a blank; the umlaut
in one key line split into "M ü ller" and "set-up" read as "set-u p"; and
one term of art (*physiognomy*) left unglossed in a course that promises to
assume no philosophy. Three further corrections (a page count, a concession
the text makes that the lesson had folded into the conflicts, and a line on
Husserl's programme) were made by the second reviewer during this pass and
are consistent with the text. Nothing needs splitting, merging or
reordering.

## The voice, judged against §F

The course keeps the register Course 1 set, and in two places improves on
it.

**What works:**

- **The passage first, then the phrases in order, and the pages named.**
  Every body opens with `<strong>Introduction, Chapter n, p. m.</strong>`,
  the passage, the page, and an instruction to read an exact range in the
  reader's own copy: pp. 3 to the paragraph on p. 7 that turns to physiology;
  the Müller-Lyer figure on p. 6 to the end of the chapter on p. 14; pp.
  15–29; pp. 30–59 ("the longest in the Introduction"); pp. 60–74. Each is
  the range the lesson then reads, which was lesson 2 of the brief. Then the
  phrases: "Now the passage's first sentence…"; "Then an objection, in the
  empiricist's voice…"; "Now the chapter's reading of the figure, which it
  gives twice."
- **Scenes rationed to two of five.** The Müller-Lyer lines ("You have almost
  certainly seen the two lines with arrowheads", PLAN §F's own exemplary
  paragraph, used where PLAN wrote it) and the proofreader ("Anyone who has
  proofread their own writing knows the trouble"). The other three open with
  the text, as §F.2 asks. Both scenes reach the chapter's category within
  the paragraph.
- **History with people in it, one sentence each.** Wertheimer, Köhler and
  Koffka "working in Germany from the 1910s"; Köhler's 1913 paper and Carl
  Stumpf "the experimental psychologist under whom Köhler had trained";
  Locke's phrase and Hume's principle; Lewin's syllables and Gottschaldt's
  figures; Brunschvicg and Bergson as holders of the projection of memories
  "outside empiricism too"; Hering as the physiologist of memory colour;
  Lagneau "and his pupil Émile Chartier, who wrote as Alain"; Henry Head's
  "local weakening of attention" and J. Stein's clinical reports; Herder and
  Romantic usage; Bergson "who had asked his readers to go back to the
  immediate data of consciousness". Each is given his position at strength
  before the chapter replies, and none is praised or mocked in the lesson's
  own voice. The intellectualist's two-eyes argument, the men in hats and
  coats and the cardboard tube are each given as "the intellectualist's
  strongest argument", "the intellectualist's showcase", "the opponent's".
- **Whose voice, every time.** The course `how_to` warns "Watch whose voice a
  sentence is in" and names the tube as "Alain's test, not his"; the lessons
  keep the promise, as above. Lesson 4 is the best example on the Subject so
  far of the rule in action: the moon through the tube is "the opponent's",
  the reply is placed on p. 36 with its content, and the ship on the shore is
  announced three times (body, `panel_intro`, `note`) as the book's case
  from Chapter 2, aimed at association, borrowed by the lesson to test a
  model the chapter criticises in Chapter 3, "and testing the judgement
  model on it is the lesson's use of the case".
- **Second person, warm, in `p` and `worked.intro` only.** "Look at what the
  rule had to use. No dot carries the word pair"; "The chapter ends with a
  reversal you might not expect"; "Look at what did the selecting. The
  memories sat in their list throughout". No "let's", no "dive in", no
  first-person anecdote, no exclamation mark; `steps`, `standard`, quiz
  items and tile text stay impersonal.
- **One light remark, and the author's own.** Lesson 3 lets through the
  Introduction's one joke, that reflection "is a system as closed as
  insanity, with the difference that it understands itself and the madman
  too", and calls it "a dry comparison" Merleau-Ponty "allows himself".
  Nothing else in the course tries to be funny.
- **The limit admitted, and the lab turned against itself.** Every `note`
  names what the lab cannot do: it "cannot show the figure arriving before
  the dots"; it "has no tile for different"; it "cannot show a word with its
  structure before any matching"; it "cannot show the recasting the book
  describes"; it "cannot show the shared prejudice that the chapter says
  lies behind every failure". Lesson 2's closing paragraph makes the limit
  the lesson: "Its reported tile has to print a number of centimetres, and a
  number of centimetres already treats the two lines as comparable in one
  measured space." That is the Subject's material clause done in a lesson's
  own words.
- **Model and family named, and the coding owned.** Each `panel_intro` says
  what is computed and whose: "the Gestalt proximity rule, Wertheimer's law
  of 1923, as the lesson states it", "the constancy hypothesis, Köhler's
  term", "the associationist account of reading", "perception as a judgement
  from signs, the psychologists' intellectualism the chapter criticises",
  "the lesson's coding … Merleau-Ponty's own account is not a column". The
  `cases` lab does what §0 requires of it: two opponents' columns, no column
  for the book, and the lesson says three times that the record "is not a
  ranking".
- **The one modern aside, in its one permitted home, fair to both sides.**
  Lesson 2's `note` sets predictive processing beside the chapter in four
  sentences: both reject the constancy hypothesis; they differ "and among
  themselves" on what replaces it, "on one reading … an unconscious
  inference, close to the judgement Introduction III argues against; on
  enactive and active-inference readings … nearer the body's own hold on the
  world"; "The chapter, written in 1945, answers neither"; and what in it
  bears on the dispute is its own choice on p. 9. No names are dropped, no
  side is given the verdict, and no other lesson on the course carries an
  aside.
- **Pointing forward by title.** Every body ends by naming the next lesson's
  question and title, and lesson 5 ends with the next course by its §B title
  and its first module, "Experience and Objective Thought".

**What was changed here, and what the courses that follow should copy:**

- **First-word case inside a quotation must match the text.** Lesson 1 had
  `&ldquo;each part arouses…&rdquo;` where Smith prints "Each", and lesson 4
  `&ldquo;There will be a moment…&rdquo;` where Smith prints "there" (the
  clause is mid-sentence on p. 20). The checker normalises case, so it did
  not catch either; AUTHORING's rule is the only guard. Both reworded around
  the first word.
- **A blank in a lab pattern is not a subscript.** The read-out turned
  `ho_se` into "ho sub se" and `_a_e` into "sub a sub e", in the body, the
  mistakes and all three worked lines, and `speechcheck` reported nothing
  because the rule for `_` is settled. Seven spoken forms added under a
  `# Classical Prejudices` block in `content/spoken/phenomenology.py`, so a
  listener now hears "h o blank s e". Two more for the key lines "Müller-Lyer:
  neither equal nor unequal" (read "M ü ller") and "analysis may substitute a
  set-up" (read "set-u p"). The rule for the brief: read the `data-say` of
  every key line and worked line, not only the preview's list of unspoken
  runs, because a wrong reading that the rules consider settled is not
  listed.
- **Gloss every term of art.** *Physiognomy*, in the chapter's own summary
  line on the Gestalt of a circle, now carries "the look it has, as a face
  has one". Everything else the course uses is glossed on first use:
  *posit*, *Gestalten*, *constitutes*, *synopsis*, *nominalism*, *le
  sentir*, *horizon*, *analytic perception*, *motive*, *transcendental
  field*.

## What the course teaches well

- **One hard idea per lesson, in the Introduction's order.** Lesson 1 carries
  figure-on-ground as the definition of perception and stops where the
  chapter turns to physiology; lesson 2 carries the constancy hypothesis and
  "different, not unequal"; lesson 3 the projection of memories presupposing
  the shape it was to supply; lesson 4 the symmetry of the two accounts,
  through attention and then judgement; lesson 5 the phenomenal field as not
  an inner world. The course `how_to` says the argument is cumulative and
  that the last lesson reads best after the other four, which is true.
- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names a product with a second clause
  from the reading: "compute proximity groups and say what is in no single
  dot"; "compute the hypothesis's prediction and say why the gap is not a
  mistake"; "count the memories that fit and say what selected them"; "run
  the judgement model through its cues and say what it needs that the
  description does not"; "compute the accounts' record and say what no cell
  shows". The five course `outcomes` are the same acts.
- **The arithmetic is right and every figure is attributed.** Gaps 1, 3, 1,
  3, 1 with threshold `2 × 1 = 2` give three pairs; 0, 1, 4, 6, 8, 9 give
  gaps 1, 3, 2, 2, 1 and four groups; the quiz row 0, 2, 3, 7, 8 gives gaps
  2, 1, 4, 1 and `{0} {2, 3} {7, 8}`. `10 − 10 = 0`, gap `2 − 0 = 2`;
  `9 − 10 = −1`, gap `1 − (−1) = 2`. Eighteen of twenty words fit `_a_e`
  (only house and horse do not); gate alone is tagged door, lake alone
  water. The judgement model keeps 2, 2, then 1; the quiz's third candidate,
  a shadow fitting c1 only, is removed by c2. The eight-row table gives
  empiricism 1 y and 7 n, intellectualism 2 y, 5 n and 1 silent, split on
  rows 2, 4 and 5; the three sub-tables were recomputed and match. Every
  magnitude that is not a measurement is labelled illustrative in the
  preset label, the body and the `note`.
- **The misconceptions are refuted with the specific figure**, as the
  Verdict lists, and the second and third `mistakes` of each lesson are the
  two further errors a reader actually makes: reading the lab's groups as
  what is seen; taking the reported tile for what is seen; concluding the
  past plays no part; reading the deciding step as the moment of seeing;
  reading the record as a ranking; expecting Merleau-Ponty's own column.
- **The labs earn their place, each for a stated reason.** The grouping lab
  (family 1, Wertheimer's rule with a threshold the lesson owns) computes a
  relation "in no single dot", and the lesson says at once that the next
  chapter warns against reading the rule over measured stimuli as a cause of
  the grouping (p. 19), so the lab is used and disowned in the same breath,
  correctly. The constancy lab is the opponent's prediction exactly as §0
  describes the method, and the `context` preset (the same shaft alone and
  in a figure, p. 13) is the chapter's sharper case, not the textbook's.
  The reading lab is honest that the book's example, "deduction" for
  "destruction", cannot be modelled by blanks, and makes a point the chapter
  needs: on the model "its pattern is a present datum doing the choosing",
  which is the second horn of p. 24's dilemma. The judgement lab sets the
  model's deciding step beside the sentence on p. 20 that the reasons "were
  not given as reasons beforehand", which is the right use of a lab that
  computes a model the book rejects. The cases lab is coded as §0 and §C
  prescribe, with the two arguable cells (the misprint for intellectualism,
  the ship) argued for in the body and flagged in the `note`.
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first preset by hand and then the preset that changes the
  result; every quiz's first item is the same act on a fresh instance (five
  new dots; 12 cm shafts; the tag water; a third candidate; a three-row
  table). The distractors are the named errors: taking the report for the
  prediction, subtracting the wrong way round, confusing a length with a
  difference, ignoring the context, ignoring c2, choosing a survivor that
  has an n.
- **The Introduction's own images are the Introduction's**: the grey behind
  closed eyes, the ape and the hen, the woolly red of the carpet (with
  Sartre named), the segment surrounded by blackness, the receiver and the
  recording station, the net with its knots (Scheler), evening and night,
  the rabbit and the hunter, tak-dak and ged-deg, the spectacles of memory,
  bricks and a house, the searchlight, the wax and the plate, hats and
  coats, the cardboard box, the drawn cube, Zöllner's lines, the screen and
  the steeple, the wheel and the candle, the rabbit in the foliage, the sun
  two hundred yards away. All checked against the page; each is in Smith's
  words where quoted and in fair paraphrase where not.
- **Cross-references are right.** Chapters by Part, chapter and page;
  lessons by title; the next course by §B title; the moon cited to pp. 32
  and 36; the ship to Chapter 2, p. 20; Zöllner to p. 41; the Sixth
  Meditation's natural judgement to the pages the chapter reads it on.

## What it taught badly, or said wrongly

### Fidelity

- **`the-idea-of-pure-sensation`, body:** `&ldquo;each part arouses…&rdquo;`
  against Smith's "Each". Repaired by rewording around the first word.
- **`attention-and-judgment`, body:** `&ldquo;There will be a moment…&rdquo;`
  against Smith's "there" (p. 20, mid-sentence). Repaired.
- **`attention-and-judgment`, body:** "the reply comes three pages later" for
  a test on p. 32 answered on p. 36. Repaired by the second reviewer during
  this pass ("on page 36"); read after it landed.
- **`the-constancy-hypothesis`, body:** the five phenomena on pp. 8–9 were
  listed as "the conflicts" when the text divides them: three the chapter
  sets against the hypothesis, and two (red and green giving grey; apparent
  size with apparent distance) that "it is conceded" show central influence,
  after which the chapter asks whether the same conclusion follows for the
  first three. Repaired by the second reviewer during this pass, with a
  clause that names the concession; faithful.
- **`the-phenomenal-field`, body:** the second reviewer added that the
  classical transcendental philosopher's completion of the analysis "is to
  all appearances the programme of Husserl's transcendental phenomenology
  too" (p. 70 and n. 12). Checked: faithful, and it marks the one place on
  the course where the book distances itself from Husserl, which §F.4 asks
  for.
- Nothing else was found. Every "the chapter says / argues / concludes" was
  tied to a sentence on the page it names, and every paraphrase of an
  opponent names the opponent.

### Prose that left the reader unexplained

- **`the-phenomenal-field`, body:** *physiognomy* unglossed. Repaired.
- **`association-and-the-projection-of-memories`:** the `wide` preset's
  candidates tile prints an eighteen-word list the body does not quote. The
  body gives the count and the worked line says which two words are
  missing, which is enough; recorded so the "every tile" rule is not read as
  broken.

### Quiz

Every distractor on the twenty questions was argued for and could not be
defended. The two that came closest: lesson 2's "That they look unequal, so
perception is mistaken about them" is half-supported by p. 8, where the
chapter lists the auxiliary lines making "two figures unequal which are
objectively equal" among the phenomena against the hypothesis, but the
question asks what the chapter says of the lines "as they are perceived" and
the second clause is the reading the chapter denies on pp. 6 and 13; and
lesson 3's "As an intellectualist theory opposed to association", which a
reader might argue from Bergson's and Brunschvicg's being named as holders
of the view, but p. 24 says in so many words that it is "a mistake to think
that with the 'projection of memories' we are bringing into perception some
mental activity". Lesson 5's survivors-and-split item is a clean instance of
the act, and lesson 4's item on what the two theories of attention share is
the best conceptual item on the course: its answer is a sentence on p. 33
and its three distractors are the three things the chapter says attention
is not.

### Speech

Every `data-say` on the five pages was read. Three readings were wrong, all
in lessons 2 and 3: "ho sub se" and "sub a sub e" for the patterns with a
blank (in the body, the mistakes and all three worked lines), "M ü
ller-Lyer" for the key line, and "set-u p" for the key line ending in
"set-up". All now carry spoken forms and read as "h o blank s e", "blank a
blank e", "Muller-Lyer" and "set-up". Nothing else misfires: "gap, 2 minus 0
equals 2 cm" keeps the three-letter head whole, "predicted equals A minus
b" is clear, and the table rows of lesson 5's worked example read as
sentences. `speechcheck` reports 0 unresolved for the Subject and
`tests.test_speech` passes (25 tests).

### Cross-references

Lessons are cited by title (“The Constancy Hypothesis”, “Association and the
Projection of Memories”, “Attention and Judgment”, “The Phenomenal Field”,
each as the lesson carries it); the book by Part, chapter and page; the
next course by its §B title, with its first module named. No lesson is cited
by number.

## Can a first-time reader of the Introduction follow the five lessons?

Yes, and the lessons slow where the Introduction's readers slow.

- **Lesson 1** gives the reader the two opponents in one paragraph before
  the sensation is examined, then follows the chapter's two definitions in
  order, with the `def` block on figure and ground arriving before the
  Gestalt paragraph. The one paragraph a newcomer will reread is the one on
  the retinal construction (p. 6), and the lesson helps by calling it "a
  test the reader can try" and giving the result in two plain sentences.
- **Lesson 2** opens with PLAN §F's exemplary paragraph, and the rest of the
  lesson lives up to it. The hypothesis is given "at its strength" with the
  transmitter image before any objection; the footnote's fairness (no
  crucial experiment, no refutation by induction) is quoted rather than
  skipped; and the `def` block "Different, not unequal" restates the
  chapter's hardest thought in two lines. The children's constancy reversal
  at the end is the place a reader will need the lesson most, and the
  lesson says why it is surprising.
- **Lesson 3** is the clearest of the five and the one where a reader with no
  philosophy is least at risk, because the proofreader is in their life and
  the dilemma on p. 24 is given as a dilemma ("If memories projected
  themselves … If instead consciousness compares…"). The Lewin paragraph is
  the one piece of experimental detail on the course and is kept to six
  sentences.
- **Lesson 4** is the course's hardest, as Chapter 3 is the Introduction's
  hardest, and the lesson is honest about that ("the longest in the
  Introduction, and the lesson follows its two halves"). A newcomer will
  manage the attention half, which is a story with Head, Stein and the
  infants in it. The judgement half moves faster: Descartes, Lagneau, the
  box, the cube, true and false perception, the natural judgement of the
  Sixth Meditation and the Gestalt pages on motive are each a paragraph.
  What the lesson leaves out is pp. 43–47 (analytical reflection, the
  Spinozist true idea, the "original doxa" of p. 47), which it summarises in
  the one quoted sentence from p. 45. That is a defensible cut for a
  Beginner course and the `not_covered` says the footnotes are not read;
  recorded below.
- **Lesson 5** gives the reader the two things they need before the lab: what
  the prejudice is (the `concepts` block) and what the field is not (the
  passage's second sentence, read second). The paragraph on the
  transcendental field is the densest on the course, and the lesson keeps it
  to five sentences with the circle's physiognomy, now glossed, as its
  anchor. The lab then lets the reader see the whole Introduction in one
  table, which is the right way to end a course whose claim is a symmetry.

## Repairs made in this pass

In `content/phenomenology/c2_prejudices/part_a.py`:
`the-idea-of-pure-sensation` the white-patch paragraph (first-word case);
`attention-and-judgment` the `close` preset paragraph (first-word case);
`the-phenomenal-field` the transcendental-field paragraph (*physiognomy*
glossed). In `content/spoken/phenomenology.py`: a `# Classical Prejudices`
block of seven spoken forms, for the two key lines and the five runs with a
blank. Nothing in `__init__.py`. No preset, `expect`, slug, module, lab key,
mode or view changed, and no §C entry needed correcting: every instance the
lessons carry is the one §C records, and §C's Course 2 entries already carry
"(checked)" or "corrected against the text" on every point AUTHORING left to
the author.

The second reviewer's concurrent changes to the same file (the p. 36 page
reference, the pp. 8–9 concession clause, the Husserl line on p. 70) were
read after they landed and are consistent with the text and with this
assessment; none is claimed here.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and
§C list them. The preview reports OK: 6 pages, every lab executes and
survives the sweep, every pinned figure on the five pages matches, no math
run without a spoken form. `phen_quotes.py c2_prejudices` reports OK: no
span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **`the-constancy-hypothesis`, the `context` preset:** "the same local
  stimulus twice" is the chapter's point (p. 13: an isolated line and the
  same line in a figure), but the fins are added stimulus, so a careful
  reader may object that the two stimuli differ. "the same shaft, point for
  point, twice" would say exactly what the hypothesis forbids and no more.
- **`attention-and-judgment`, body:** "That is the intellectualist's
  strongest argument" is the lesson's word; p. 38 says only that once vision
  is defined as a quality impressed by the stimulus, "the least illusion …
  is sufficient to establish that perception is a judgement". "That is the
  shape of the intellectualist's argument, as the chapter lays it bare"
  would mark whose assessment it is.
- **`attention-and-judgment`, the judgement half:** pp. 43–47 are
  represented by the p. 45 sentence alone. The chapter's claim there, that
  intellectualism uses perception's "de facto power" of bringing experiences
  together "tacitly" (p. 47), is the premise of the passage's thesis and a
  reader following in the book will meet four pages the lesson passes over
  in one sentence. One paragraph would carry it; the lesson has 21 words of
  quotation budget left.
- **`the-idea-of-pure-sensation`, body:** "to posit impressions beneath it,
  to set them down as there" glosses *posit* in an apposition that reads
  clumsily. "to posit impressions beneath it, that is, to assume they are
  there" would gloss as plainly.
- **`the-idea-of-pure-sensation`, body:** "the grey that surrounds me when I
  close my eyes, the sounds that hum in my head" paraphrases the chapter's
  own first person without saying so. Harmless, and the sentence before
  names the chapter; "in the chapter's first person" would close the gap.
- **`the-idea-of-pure-sensation`, `concepts`:** "The chapter takes it as
  empiricism's starting point" of the first definition (sensation as the way
  I am affected). The chapter attaches empiricism by name to the second
  definition (p. 7, "the determinate quality by which empiricism tried to
  define sensation"); the first is examined without a holder. Not wrong in
  substance, since the Introduction treats sensation as empiricism's unit
  throughout, but the words are the lesson's.
- **`the-phenomenal-field`:** p. 68's summary line, that the experience of
  phenomena "is not an irrational conversion, but an intentional analysis",
  is in the lesson's comment and not in its body, which covers the point in
  paraphrase. It is the chapter's best one-line answer to the Bergson
  objection and would cost nine words of a budget with 41 to spare.

## Lessons for the remaining authors

The brief's eleven lessons from Course 1 all held here; two more from this
course:

1. **Read the `data-say` of every key line and worked line, not only the
   preview's unspoken list.** A `_` is read as a subscript, an umlaut can
   split a name, and a hyphenated "up" can come apart, and none is reported,
   because each has a rule. A blank, a name with a diacritic, or a word that
   is also a notation needs a spoken form keyed by the exact line.
2. **The checker does not see case.** AUTHORING's rule that a quotation's
   first letter match the text is enforced by eye only. When a quotation
   begins mid-sentence, write it mid-sentence.

Final lines. Preview: `OK` (6 pages rendered; labcheck, every lab executes:
5 page(s) executed and swept, 0 failing; labcheck, pinned figures match: 5
page(s) executed and swept, 5 with pinned figures, 0 failing). Quotation
checker: `OK` (86, 110, 85, 129, 109 quoted words; openings 48, 40, 47, 56,
68).
