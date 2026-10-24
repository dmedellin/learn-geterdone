# Pedagogy assessment — Sensing and Space (Phenomenology of Perception, course 5)

Formed from the eight lesson dicts in `content/phenomenology/c5_sensing_space/`
(`part_a.py`, Part Two's introduction and the three lessons on Sense
Experience; `part_b.py`, the four sections of Space; `__init__.py`, the course
dict) and the kit they render through (`scripts/mathpath/labs/phenkit.py`,
modes `perspective/faces`, `stimulus/illusion`, `cases/table`,
`variation/core`, `level/tilt`, `depth/binocular`, `motion/phi`), on branch
`feat/phenomenology-subject` before the Subject was wired into the site. The
design authority is `docs/phenomenology/PLAN.md` §0 (the one question and the
three families of lab), §B, the Course 5 entries in §C, §D as summarised in
`docs/phenomenology/kit-report.md`, §E (how a book in copyright is quoted) and
§F (the voice), with `docs/phenomenology/AUTHORING.md` and its three "Lessons
from" sections as the brief every course must meet. The Course 1 assessment
(`phenomenology-perception-what-phenomenology-is.md`) is the model.

Every lesson was read in full before anything was changed. The whole of Smith
pp. 235–347 was read first, chapter by chapter (the introduction to Part Two,
Sense Experience, and all four sections of Space), then each lesson's passage
and the pages it reads line by line, then the one page outside the range a
lesson cites (Part Two Chapter 3, p. 372, for the glass's single manner of
being). Every pinned tile was read off the rendered page with
`node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py phenomenology --course
perception-sensing-and-space`), every figure in prose, worked lines and quiz
`why`s was recomputed by hand, the `data-say` of every worked block and key
list was read, and all the spans in `&ldquo;…&rdquo;` were run through the
Subject's quotation checker (`phen_quotes.py c5_sensing_space`) with the
opening passages checked by eye against the page. Lessons, in course order:
`the-body-and-perception`, `the-motor-physiognomy-of-colours`,
`the-anonymous-subject-of-sensing`, `the-unity-of-the-senses`, `up-and-down`,
`depth`, `movement`, `lived-space`. The course assumes Classical Prejudices and
The Lived Body and school geometry, and is judged against that.

A second reviewer was reading the same course at the same time and landed
small exact-string edits in both lesson files after this pass's own edits.
They were read in the diff after they landed (Stratton's dates, the
abduction misprint noted twice, Werner's spasm as a report, "circle from a
rectangle", the mescalin attribution, "predicted-tilt", the chapter's own
remark on *sens*, "Berkeley would probably reply, the chapter supposes", the
Gestalt source of the first objection in Depth, Linke's description, the phi
definition with Smith's "phenomenon ø", and the mescalin subject's food) and
are consistent with the text and with this assessment; the preview and the
checker were re-run after them and both report OK. None is claimed here.

## Verdict

The course teaches its subject. A reader who finishes it can compute which
faces of a cube a whole-number direction presents and at what fraction of
their area, and say why the introduction calls the cube with six equal faces a
limiting idea; compute what a pure-quality account of sensation predicts for
the arm under two colours and read the gap as the chapter reads it; count two
classical accounts against a coded table of observations and name the one
both fail; intersect two codings of a glass as given to four senses and say
which coding the chapter describes; run the lesson's own model of a spatial
level under a sudden and a gradual re-anchoring; compute convergence and
disparity as the classical theory of depth does and say why the chapter calls
them motives; compute the speed two alternating lights imply and place an
interval in Wertheimer's bands. Those are the acts the eight `standard` fields
name and the quizzes measure; no objective is "understand X". The
`mistakes[0]` of every lesson is the §C misconception, refuted with the
lesson's own figure: the six equal faces "nowhere" in `1`, `4/5`, `3/5`, `2/3`,
`1/3`, `2/3`; a pure quality's `0` cm against an illustrative `6`; the
`passivity` preset's survivor `empiricism`, which the lesson turns into the
point that one observation is not the chapter's case; the `sense-bound` core
`none` as "what the view put in"; the series `45°, 45°, 0°` with the image
unchanged; `13/100`, `13/120` and `13/600` as "the calculation the chapter says
nobody performs"; `1/12` cm per ms as "the speed of a body nobody sees". All
31 pinned tile strings on the eight pages match the lab, and every figure in
prose agrees with the lab or with a recomputation (6.5/50 = 13/100,
6.5/60 = 13/120, 13·(1/50 − 1/60) = 13/600 ≈ 0.02167, 13/6000 a tenth of it,
13/51000 one eighty-fifth; 5/20 = 1/4, 5/60 = 1/12, 5/250 = 1/50; 180, 90, 45,
45/2, 45/4; 6/120 = 1/20; 6.5/65 = 1/10; 13/100 − 13/200 = 13/200).

Fidelity to the text is high. Every quoted span is in Smith character for
character (the checker reports OK, with 91, 85, 90, 71, 113, 102, 116 and 91
quoted words of the 150 allowed; opening passages 36, 30, 45, 35, 65, 34, 62
and 44 of 70). The voice of every paraphrase is named, and this course has to
name a great many: the objector's cube (p. 235–236), the associationist
reading of Stratton that a footnote makes "at least implicitly" his own
(p. 285), the classical theory of depth "stated in its own voice" (p. 299),
the objective idea of movement "at its strongest" (p. 312), the logician
(Linke) and the psychologist (Wertheimer) in turn, and objective thought's
objection to lived space (pp. 335–336). Merleau-Ponty is presented, not
endorsed; the opponents (Kant, Berkeley, the Cartesians and Malebranche, the
Gestalt psychologists, Bergson, Linke) each get their view before the reply,
and each `note` names what the lab cannot settle. The defects found were
local and are repaired: two sentences that misplaced where in the text a view
begins (the objector's cube "in the next paragraph", when it is the rest of
the first paragraph; the chapter's reply to objective thought "begins with"
Binswanger's patient, who comes two pages into it); one preset label and
sentence that said Werner's faint colours were "too faint to be named" when
the subjects name them and do not see them (p. 244–245); one confusing
sentence about what Stratton's reports do and do not contain; one piece of
Berkeley's own book presented without saying it is not in the chapter; and
one unglossed instrument. Nothing needs splitting, merging or reordering.

## The voice, judged against §F

**What works, and should be kept:**

- **The passage first, the exact pages, then line by line.** Every body opens
  with `<strong>Section, p. n.</strong>` and the passage, names the page,
  tells the reader the exact pages to read in their own copy, and that range
  is the one the lesson then reads (235–239, 240 to the communion paragraph
  on 246, 246 to the paragraph defining a sense on 252, 252–282, 283–296,
  297–311, 311–327, 327–347). Because Smith prints no headings inside Space,
  the course `how_to` and each of those four lessons give the page and the
  sentence where the section begins and ends; that is a kindness the pilot
  did not need and these lessons do. Then the phrase-by-phrase move: "its
  first clause is the opponents' idea, rejected… Its second clause is the
  finding" (lesson 2); "Now the passage, and its two halves" (lesson 3); "Now
  the passage. Each colour, the paragraph before it says…" (lesson 4).
- **The book read whole before the passage, in the lectures' order.** Lesson 2
  reads the chapter's first page (objective thought "unaware of the subject
  of perception") before its p. 243 verdict; lesson 3 reads the
  intellectualist account on pp. 246–247 before the p. 250 answer that
  replaces it; lesson 5 reads Kant, Stratton and the two rejected
  interpretations before returning to the mirror; lesson 7 reads the stone
  and Zeno before Wertheimer. The reader meets the view being refused before
  the refusal every time.
- **Scenes rationed.** Three of eight open with a scene (a die in the fingers,
  lying on your back under a clear sky, a glass sliding off a table), one with
  the chapter's own stone across the garden, and four with the text's own
  case (Goldstein's patients, Wertheimer's mirror, Berkeley, the section's
  first sentence). That is under the half §F.2 allows, and each scene reaches
  the chapter's question within the paragraph ("The chapter's question is who
  did the seeing").
- **The history of ideas as a story with people in it.** Goldstein is "the
  same Goldstein who with Adhémar Gelb studied Schneider in Part One"; Werner
  "a developmental psychologist then working in Hamburg"; von Senden's 1932
  collection; Wertheimer's 1912 study "usually taken as the start of Gestalt
  psychology"; Stratton "an American psychologist"; Berkeley "the Irish
  philosopher and later bishop" and his 1709 book; Malebranche "Descartes's
  follower"; Koffka and Guillaume named from the footnote; Linke "of
  Husserl's school"; Zeno of Elea; Minkowski's *Le Temps vécu* of 1933;
  Binswanger "who read his patients through Heidegger"; Fischer and Straus.
  One sentence each, before the reply.
- **The cases are people, named with the book's respect.** Lessons 2, 4 and 8
  each say in a sentence that "these are patients, and what the chapter has
  is their physicians' reports; the lab below codes the reports, not the
  patients", which §F.3 asks for and the pilot had no occasion to show.
- **Second person, warm, in `p` and `worked.intro` only.** "Pick up a die and
  turn it slowly in your fingers"; "You did not decide to see blue, the way
  you might decide to take a job"; "Before it lands you know how it will
  sound". `steps`, `standard`, quiz items and tile text stay impersonal; no
  "let's", no first-person anecdote, no exclamation mark anywhere in the
  course.
- **The light touch, where there is one, points at the text.** "The arithmetic
  is trivial, and that is its point" (lesson 2); "The arithmetic is an
  intersection and cannot go wrong. Everything depends on the coding"
  (lesson 4). Nothing performs friendliness.
- **Family and model named, and the lab turned against itself where that is
  the point.** Every `panel_intro` names what it computes and whose: "parallel
  projection, which is undisputed geometry… the figures are the projection's,
  not a report of what is seen"; "the prediction of sensation as a pure
  quality"; "the lesson's coding… Merleau-Ponty's own account is not a
  column"; "the lesson's model, which no theory states"; "the classical
  theory of depth from signs"; "Wertheimer's bands as later textbooks report
  them… not in Merleau-Ponty". Lesson 1 makes the lab's procedure the lesson
  ("Notice how the lab gets these figures. It holds a cube with six equal
  faces in advance, from no point of view… That is exactly the objector's
  procedure"), and lesson 7 does the same with the speed tile ("the objective
  idea of movement turned into arithmetic: one thing, every position, a
  time"). That is the Subject's material clause done as teaching.
- **Whose voice, every time.** The course `how_to` warns that "these chapters
  let an objector, a logician or a psychologist speak for a page before
  answering", and the lessons keep the promise. The Smith misprint on p. 243
  (abduction for adduction) is pointed out to the reader checking their copy
  and not quoted; the remark on the two senses of *sens* is the chapter's
  own (p. 294), with a translator's note beside it, and the lesson now says
  so; "Smith writes body schema here and body image a page earlier"
  is said once, where the term is introduced.
- **No modern aside.** §F.1 gives this course none, `not_covered` says so, and
  there is none. Korte's laws (1915) and the textbook thresholds are a later
  psychologist's figures labelled as the lesson's addition, which §0 permits.
- **Pointing forward by title.** Every body ends by naming the next lesson's
  question by its title, and lesson 8 ends with the next course by its §B
  title and its first object, the thing that keeps its size and colour.

**What was changed, and what the brief should add:**

- **Say where in the text a voice begins, exactly.** Lesson 1 said "the next
  paragraph is in the objector's voice"; the objection begins mid-way through
  the first paragraph of Part Two ("It will perhaps be objected", p. 235) and
  runs to the end of that paragraph on p. 236, and the reply opens the next.
  Its quiz `why` said "The paragraph begins" with those words. Both reworded.
  Lesson 8 said "The chapter's reply begins with a patient of Binswanger's";
  the reply begins on p. 337 ("It is true, we shall reply") and the brush
  comes on p. 339, after the myth. Reworded to "runs from page 337 to page
  339, and its sharpest case, near its end". A reader following in the book
  looks for the paragraph break, as Capital's reader looked for a fourth
  case.
- **A report's own words decide a label.** The `faint` preset and its
  sentence said red against green "too faint to be named". Werner's subjects
  (pp. 244–245) name the colour and do not see it ("it cannot be green, and
  can be only blue but in fact I see no blue"), and the chapter's phrase is
  "before being seen". Label and sentence now say "too faint to be seen",
  which is what the quiz item and the `note` already said. §C's wording
  ("too faint to be named") should be corrected to match; see
  recommendations.
- **Do not say what a source reported unless the book or the lesson can show
  it.** Lesson 5 said "Notice what Stratton reported and the model does not:
  no single moment at which the world turned back over." As written it was
  confusing (under the share rule the model has no single moment either) and
  it reported Stratton's paper, which the reader cannot check in Smith. It now
  says that the share rule never reaches 0° and that the chapter's own
  summary of Stratton (p. 285) gives no such moment either, listing what it
  does give, and keeps the hedge that how far Stratton's own reports support
  the chapter's reading "is something later readers still argue about".
- **Mark what comes from an opponent's own book.** Lesson 6 gave Berkeley's
  theory of signs learned by custom as if the chapter stated it; the chapter
  names Berkeley's conclusion and the Cartesians' natural geometry, and the
  sign theory is from the *New Theory of Vision*. One clause added: "in his
  own book rather than in anything the chapter quotes". The same holds for
  Descartes's *Optics* and the two sticks, which the lesson already presents
  as history ("the picture goes back to").
- **Gloss the instrument.** "The stereoscope" appeared in a quiz `why` with
  no gloss; now "the stereoscope, which gives each eye its own picture".

## What the course teaches well

- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names the product: faces and fractions
  "and state why the introduction calls the cube with six equal faces a
  limiting idea rather than a corrected view"; "name the two exits the chapter
  closes, the physical and the conscious, with the observation that closes
  each"; "the survivors on the table and on its subsets"; "say which feature
  of Wertheimer's or Stratton's reports each rule illustrates"; "explain why
  it calls convergence a motive and not a sign or a cause". The five course
  `outcomes` are the same acts, the fifth being the reading's: state the
  views the chapters answer and the reply to each.
- **One hard idea per lesson, in the book's order, with the splits §B fixed.**
  Sense Experience is cut where the chapter turns from the quality (lesson 2)
  to the subject of sensing (lesson 3) to the senses' distinction and unity
  (lesson 4); Space one lesson per section, with each lesson saying where its
  section begins and ends since Smith prints no headings. Lesson 4 carries
  thirty pages and is the course's heaviest; it manages by stating in
  `concepts_intro` that it argues "on two fronts at once", by summarising the
  closing pages on the temporal synthesis in one paragraph, and by saying in
  `not_covered` that Temporality will read them.
- **The misconceptions are refuted with the specific figure**, as quoted in
  the verdict. Two of them do something the pilot's could not: lesson 3's
  `passivity` preset lets the wrong view win on one observation and then says
  why one observation is not the chapter's argument; lesson 4's `sense-bound`
  preset computes the opponent's prediction (an empty core) and says "the
  empty core is not a finding: it is what the sense-bound coding put in".
  That is the second family used exactly as §0 intends: the count is exact,
  the coding is the lesson's, and the lesson says so three times (body,
  `panel_intro`, `note`).
- **The arithmetic is right, and each figure is attributed to its model.**
  Listed in the verdict. The `depth` lesson adds the comparison between
  presets in prose, since no tile may depend on comparing presets (§D.3):
  "the disparity falls to `13/6000`, a tenth"; "one eighty-fifth of the near
  figure"; and its `note` says the comparisons are the lesson's.
- **The labs earn their place, each for a stated reason.** The cube (family 1,
  geometry nobody disputes) computes "exactly the objector's procedure" and is
  used to show what the procedure yields and what it cannot. The arm (family
  1) computes a prediction of zero, and the lesson says that triviality is
  the point. The two `cases` tables (family 2) are honest about their weakest
  cell in the `note` ("the second observation in particular gives
  intellectualism an activity the chapter places in the body"; "the
  empiricist cell for the brush in particular is the lesson's"). The level
  (family 3) is introduced as "a model the lesson builds to illustrate this,
  and no theory says it", with the one feature taken from each report named
  (the suddenness is Wertheimer's; the halving is not Stratton's). Depth and
  motion (family 1) compute the opponent's figures and say in the same
  paragraph that "nobody has them" and "nothing crosses the gap".
- **Every tile the view prints is explained.** The `faces` view prints five
  and the lesson explains five, including the largest-view tile ("never more
  than 3") and the consistency tile's dash ("because no view here reports
  what it sees"). `level` prints three and the lesson says which period the
  slider shows. `cases` and `variation` print three each and the lesson walks
  each preset's values.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` or body asks for a
  comparison before the press ("Switch… and watch", "Compare presets" as a
  step); every quiz asks the same act on a fresh instance (`4 0 3`; 4 cm out
  and 2 cm in; the `activity` preset's split; four variants with `hard` in
  all; period 4 under the share; 65 cm and 50/100 cm; 6 cm at 120 ms; a
  four-row table with a `y, y` row). The distractors are the named errors:
  the swapped pair, sevenths "divide by the sum of the components", `2 cm`
  "subtracts deviations that go opposite ways", `10 rad` "the ratio upside
  down", `13/300` "uses the sum of the distances".
- **The chapters' own images are the chapters'.** The heart in the organism,
  the walk round the flat, the crossed fingers, the fire seen out of the back
  of the head, the fauna of a distant land, the sleeper and the sacrament,
  the sky, the hole and the hollow, the birth and the death, the concert
  hall, the sheets of paper in shadow, the gold and the wood, Helen Keller's
  sonata, the dubbed film, the word *warm*, the tilted stick, the inverted
  face, the ash-tray and the pencil, the road parallel in depth, the man at
  two hundred yards, the pen through the whiteness, the stone across the
  garden, the watch in the next room, the fakir's egg, the circle before
  Euclid, the greyish power of flight, Leibniz's ship, the train, Paris as a
  style, the bird and its twittering, night, the great bird shot down, the
  augur, the holiday village, the mountain landscape, the brush, the stone of
  the Tuileries wall, the flat stone that is a patch of sunlight, the fly near
  the eye: all where the lessons say they are, in Smith's words where quoted
  and in fair paraphrase where not.
- **The cross-references are right.** Schneider and the body schema to Part
  One; "a later section of Part Two, on depth" for the squares seen askew
  (p. 308, checked); the glass's single manner of being to Part Two Chapter 3,
  p. 372, as §C asks; the reversible cube to the depth section; lessons by
  title; the next course by its §B title.

## What it taught badly, or said wrongly

### Fidelity

- **`the-body-and-perception`, body and quiz 2 (where the objection
  begins):** as above. Repaired.
- **`the-motor-physiognomy-of-colours`, `faint` preset label and body ("too
  faint to be named"):** as above. Repaired. The `note` and quiz 3 already
  had it right.
- **`up-and-down`, body (what Stratton reported):** as above. Repaired.
- **`depth`, body (Berkeley's signs):** as above. Repaired.
- **`lived-space`, body (where the reply begins):** as above. Repaired.
- **`up-and-down`, `mistakes[0]`:** "At its strongest this is the realist's
  view". The chapter's words are "empiricist psychology" (p. 288) and "the
  realistic mistake" (p. 290); both are fair, and the lesson elsewhere calls
  it the associationist interpretation. Left; recorded so the author knows
  the word is the lesson's.
- **`the-unity-of-the-senses`, body:** "since space, for Kant, is the form
  under which anything can be an object". The chapter attributes the
  deduction to intellectualism and says "to use a Kantian expression"
  (p. 253) and "Kant" (p. 255); the attribution is standard and not wrong.
  Left; recorded.
- **`lived-space`, body:** "The distress some feel at night"; the text says
  "neuropaths" (p. 330). A softening, not an error. Left; recorded.

### Prose that left the lab, or the reader, unexplained

- **`depth`, quiz 4 `why`:** the stereoscope. Repaired.
- Nothing else: every tile, every preset and every term of art found on the
  eight pages (*quale*, *abduction*, *transcendental Ego*, *intentional*,
  *pre-personal*, *synergic*, *natural attitude*, *psychologism*, *limiting
  idea*, *spatialized and spatializing*, *anchoring points*, *motive*,
  *stroboscopic*, *lived distance*) is glossed in English on first use.

### Quiz

Every distractor on the thirty-two questions was argued for and could not be
defended. The two that came closest: lesson 4's "Whenever the stimulus is
weak" as when a separate quality appears, since pp. 244–245 do use weak
stimuli, but there they reveal a bodily attitude before any quality, not the
separated quality, so the item stands; and lesson 2's "Red can accentuate
reactions without the patient being aware of it" as the observation against
the physical exit, which the text uses against the other exit, and the `why`
says exactly that. Lesson 3's "What follows?" item, which asks what the
`passivity` preset's survivor proves about the chapter (nothing), is the best
conceptual item on the course, since it tests the one thing the second family
is most likely to be misread as doing.

### Speech

Every math run and key line on the eight pages was read from `data-say`. The
worked lines read well ("predicted difference, 0 minus 0 equals 0 cm",
"50 cm, 6.5 over 50 equals 13 over 100 equals 0.1300 rad", "period 3, the
level jumps to 45 degrees"). The one three-letter word at the head of a key
line, "gap:" in lesson 2, is read as the word *gap* and not spelled out, so
no change was needed. The preview lists no unspoken run, and
`content/spoken/phenomenology.py` needed no block for this course.

### Cross-references

Lessons are cited by title (“The Motor Physiognomy of Colours”, “The
Anonymous Subject of Sensing”, “The Unity of the Senses”, “Up and Down”,
“Depth”, “Movement”, “Lived Space”, each exactly as the lesson carries it);
the book by Part, chapter and section; the next course by its §B title. No
lesson is cited by number.

## Can a first-time reader follow the eight lessons?

Yes, with the help the course already gives, and the places a reader will
slow down are the places these chapters' readers slow down.

- **Lesson 1** is the right door into Part Two: the die, then the flat, then
  the objection at strength, then the reply from the definition of a cube
  ("*enclose* and *between* have their meaning from our experience as embodied
  subjects"). The two-dogmatisms paragraph is the hardest on the course and
  is kept to five sentences with analytical reflection glossed in the
  sentence. The `def` of a limiting idea ("sums up where a series tends
  without being a member of it") is the one a reader with no philosophy
  needs.
- **Lesson 2** moves from a clinical report to a redefinition of sensation in
  six pages and protects the reader by reading the findings twice: once as
  reported (directions, resting position, accuracy with a finger) and once as
  the chapter reads them (two attitudes, towards the world and away from
  it). The two exits closed ("not effects of light on the body as physics
  describes it… Nor effects of a quality clearly seen") give the reader the
  shape of the argument before its conclusion.
- **Lesson 3** is the course's most abstract and the lesson knows it: the sky
  comes before the word *anonymity*, the intellectualist's strongest case
  is put in three plain sentences, and the passage is read as two halves
  with the birth-and-death reason unpacked ("to do so I would have to exist
  before or after myself"). The retort that the sky is not a mind is raised
  and answered where the text raises it.
- **Lesson 4** is the heaviest. The von Senden paragraph and the sheets of
  paper are concrete enough to carry a first-time reader to "touching is not
  seeing" and "the separate quality is the product of an analytic attitude";
  the binocular-vision paragraph is the lesson's centre and is read
  carefully ("If the unity were a thought, it would come as soon as I noticed
  that the images were of one thing; in fact I wait"). What a first-time
  reader will still find fast is the closing paragraph on the temporal
  synthesis, which the lesson compresses to three sentences by design.
- **Lesson 5** gives the reader Stratton's week in one paragraph of plain
  facts before either interpretation, and the `def` of spatialized and
  spatializing space before Kant's alternative is argued. The lab's model is
  introduced as "no theory says it" and the `mistakes[2]` repeats the
  warning, so a reader cannot leave thinking the chapter subtracts angles.
- **Lesson 6** is the clearest statement of a classical theory on the
  course, because it lets the theory speak ("My table is near, the piano
  farther…") before the reply, and the death-and-journey `def` of a motive
  is exactly the everyday example §F asks for.
- **Lesson 7** is the best read-along on the course: the stone, Zeno, the
  passage, the rod, the logician's watch and fakir, the verdict that both are
  right, the circle before Euclid, the train. A reader with no philosophy
  can follow every step because each has a thing in it.
- **Lesson 8** has the most people in it and names each with their source;
  the objection in objective thought's voice is given at strength (the left
  and the right, the dreamer who must wake, "where is it?") before the
  either/or reply. The closing pages on illusion are summarised in two
  sentences, as `not_covered` promises.

The course protects the reader in two further ways later courses should
keep: the `how_to` tells them how to find the sections of Space without
headings, and every lesson says in `p`, `panel_intro` and `note` whose figure
each figure is, so a reader never takes `13/600` for something the chapter
says anyone sees.

## Repairs made in this pass

In `content/phenomenology/c5_sensing_space/part_a.py`:
`the-body-and-perception`, the objector paragraph ("the rest of that first
paragraph, which runs on to page 236") and quiz 2's `why` ("The sentence on
page 235 begins…"); `the-motor-physiognomy-of-colours`, the `faint` preset
label and the lab paragraph ("too faint to be seen"). In `part_b.py`:
`up-and-down`, the Stratton sentence in the two-rules paragraph; `depth`, the
Berkeley clause and the stereoscope gloss in quiz 4; `lived-space`, the first
sentence of the reply paragraph. Nothing in `__init__.py`. No preset id,
`expect`, slug, module, lab key, mode or view changed; the one label changed
(`faint`) keeps its id and its pinned tiles.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and
§C list them, including every "As built" and "Resolved against Smith" note in
the Course 5 entries: the `tour` preset with `3 0 4` as its cover view, the
`red-green` naming, observation 1 and 2 of the anonymous-subject table as
resolved, `tinkles` and the core `hard, brittle`, Stratton's week, the
`interval` preset's one eighty-fifth, the thresholds labelled as later
textbooks', and `brush-and-dream` in place of `patients`. The `faint`
label's wording is the one §C deviation this pass introduces.

`python3 scripts/preview_subject.py phenomenology --course
perception-sensing-and-space` reports OK: 9 pages, every lab executes and
survives the sweep, every pinned figure on the eight pages matches, no math
run without a spoken form. `phen_quotes.py c5_sensing_space` reports OK: no
span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **§C, lesson 2:** the `faint` preset is described as "red against green too
  faint to be named". The text (pp. 244–245) has the subjects naming the
  colour from a bodily attitude while seeing none; "too faint to be seen" is
  the chapter's phrase and now the lesson's. The author should correct the
  §C wording in the same way, since PLAN.md is outside this assessment's
  files.
- **`up-and-down`, `mistakes[0]`:** "the realist's view" could say "the
  empiricist's view, which the chapter also calls the realistic mistake", so
  that the word on the page matches the word in the lesson's own
  interpretation paragraph.
- **`the-unity-of-the-senses`:** the lesson carries thirty pages and four
  distinct moves (the a priori spatiality of the senses, von Senden, the
  separated quality and synaesthesia, binocular vision and the synergic
  body). It holds, but if any lesson on this course is ever split, it is this
  one, at p. 266 where the passage falls; §B fixed three lessons for the
  chapter, so this is recorded and not recommended now.
- **`movement`, `def`:** the lesson names the phi phenomenon in its own
  voice (§C allows it), and the second reviewer's edit now adds that Smith
  prints it "phenomenon ø" on p. 316 in the logician's voice, which spares a
  reader who looks for the word *phi* and does not find it. Done during this
  pass, not by it.
- **`depth`:** Descartes's *Optics* and the blind man's sticks are given as
  history in the lesson's voice; the footnote on p. 299 cites Malebranche
  only. True and standard, and now marked for Berkeley; a reader would be
  served by the same three words ("not in the chapter") for Descartes.
- **`the-anonymous-subject-of-sensing`, body:** "a purely verbal solution" is
  quoted as the chapter's phrase in paraphrase ("is, the chapter says, a
  purely verbal solution") without quotation marks. It is the text's wording
  (p. 247); with ten words of budget left the lesson could quote it, or
  reword to avoid the appearance of an unmarked quotation.
- **`lived-space`, dream cell:** intellectualism is coded `y` for the dream on
  the ground that objective thought places the fall, on waking, in the chest
  (p. 336). That is the objector's argument, which the chapter answers
  (p. 337–338); the lesson's `note` says the cells are its own, and the
  coding is defensible as "what the account would say". A reviewer who reads
  the cell as the chapter's own view of dreams would be wrong, and the lesson
  gives them no reason to; recorded only.
- **Course `summary`:** "Part Two of the book, The World as Perceived" matches
  Smith's part title (checked against the contents page); PLAN §B's text
  gives the Part's name as "The Perceived World". The summary is right and
  §B's aside is loose; no change needed on the course side.

## Lessons for the remaining authors

1. **Say where a voice begins and ends by page and paragraph, and check the
   paragraph break.** Both fidelity slips on this course were a paragraph off,
   not a page off; the reader with the book open notices a paragraph.
2. **A source's own report decides a label.** "Too faint to be named" sounded
   right and was the opposite of what Werner's subjects did. Read the
   subject's quoted words before labelling a preset after them.
3. **Do not report what a source wrote outside the book unless the lesson
   says that is what it is doing**, and never set it against the model as if
   the reader could check it. If the chapter summarises the source, cite the
   chapter's summary.
4. **Mark every opponent's doctrine that comes from his own book and not from
   the chapter**, in three words. The chapter names Berkeley, Descartes and
   Malebranche without giving their theories in full; the lessons may give
   them, and must say so.
5. **When a chapter has no printed headings, give the reader the first and
   last sentence of the section**, as `part_b` does for Space. Part Two
   Chapter 3 has the same problem.
6. **Keep saying "these are patients, and the lab codes the reports".** Three
   lessons here do it; Hallucination and Other Selves will need it more.
7. **Use a preset to let the wrong view win**, as `passivity` does, and then
   say why one observation is not the chapter's argument. It teaches what the
   second family is for better than a table on which nothing survives.
8. **Keep the preview and the checker green after every edit, re-read before
   each edit, and run `git diff --stat` at the end** so the report can say
   what is yours.

Final lines. Preview: `OK` (9 page(s) rendered; labcheck, every lab executes:
8 page(s) executed and swept, 0 failing; labcheck, pinned figures match: 8
page(s) executed and swept, 8 with pinned figures, 0 failing). Quotation
checker: `OK` (91, 85, 90, 71, 113, 102, 116, 91 quoted words; openings 36,
30, 45, 35, 65, 34, 62, 44).
