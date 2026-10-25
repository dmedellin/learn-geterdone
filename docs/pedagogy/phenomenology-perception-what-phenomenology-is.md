# Pedagogy assessment — What Phenomenology Is (Phenomenology of Perception, course 1)

Formed from the four lesson dicts in `content/phenomenology/c1_preface/`
(`part_a.py`, one lesson per theme of the Preface; `__init__.py`, the course
dict) and the kit they render through (`scripts/mathpath/labs/phenkit.py`,
modes `size/angle`, `perspective/necker`, `variation/core`,
`perspective/faces`), on branch `feat/phenomenology-subject` before the
Subject was wired into the site. The design authority is
`docs/phenomenology/PLAN.md` §0 (the one question and the three families of
lab), §B, the Course 1 entries in §C, §D as summarised in
`docs/phenomenology/kit-report.md`, §E (how a book in copyright is quoted) and
§F (the voice). This course is the pilot: the six that follow will be written
from it, so the voice and the reading are judged in more detail than usual,
and the findings are written for the authors' brief.

Every lesson was read in full before anything was changed. The whole Preface
(Smith pp. vii–xxiv) was read first, then each lesson's passage and the pages
it reads line by line, then the five pages outside the Preface the lessons
cite (Introduction III pp. 32 and 36 for the moon through a tube, Part Two
Chapter 2 pp. 302 and 306 for the enlarged moon and the reversible figure,
Part One p. 77 for the house seen from nowhere). Every pinned tile was read
off the rendered page with `node scripts/labcheck.js --observe` (rendered
through `scripts/preview_subject.py phenomenology --course
perception-what-phenomenology-is`), every figure in prose, worked lines and
quiz `why`s was recomputed by hand, every `data-say` on the four pages was
read, and all 58 spans in `&ldquo;…&rdquo;` were run through the Subject's
quotation checker (`phen_quotes.py`) and the opening passages checked by eye
against the page. Lessons, in course order: `description-not-explanation`,
`the-reduction-and-its-limit`, `essences-and-existence`,
`intentionality-and-rationality`. The course assumes no philosophy and school
geometry, and is judged against that.

A second reviewer was reading the same course at the same time and made
changes to the same file while this pass was under way. Those changes are
noted where they bear on a finding and are not claimed here.

## Verdict

The course teaches its subject and is fit to be the voice reference for the
Subject. A reader who finishes it can compute an angle subtended from a size
and a distance and say which question about the moon that figure answers and
which it leaves open; show that one line drawing fits two solids by comparing
each reading's edges with its mirror image's and name what a viewer who saw
one reading supplied; intersect a coded set of variants to find a core, list
what varies and name what each excluded variant lacks; and compute which
faces of a cube several whole-number directions see, their foreshortening,
the faces no view sees and whether a report fits its direction. Those are the
acts the four `standard` fields name and the quizzes measure; no objective is
"understand X". The `mistakes[0]` of every lesson is the §C misconception,
each refuted with the lesson's own figure: the overhead moon at
`3474/378029 ≈ 0.0092` rad, larger than the horizon moon's `0.0090` and the
one that looks small; the wire cube's exact `12` edges with nothing doubted
and the front "never in it"; the sound core `some-duration`, true of every
tone and silent about the one you hear; the `conflict` verdict reached "from
nowhere", which is the one thing a perceiver never has. All 30 pinned tile
strings on the four pages match the lab, and every figure in prose agrees
with the lab or with a recomputation.

Fidelity to the Preface is high, and this is the finding that matters most
for the authors' brief, because the Preface is the book's most quoted and
most misquoted twenty pages. Every one of the 58 quoted spans is in Smith's
text character for character (the checker reports OK with no misses, and the
quotation budget is 117, 129, 137 and 139 words of the 150 allowed; opening
passages 68, 66, 43 and 56 of 70). The paraphrases that say what
Merleau-Ponty "says", "replies" or "concludes" each have a page behind them.
Merleau-Ponty is presented, not endorsed: Descartes, Kant, the Vienna Circle,
Jean Wahl and the idealist's argument for a standpoint above the views each
get their position stated at strength before the Preface answers, and every
`note` names what the lab cannot settle. The defects found were local, and
most are repaired: one sentence in the moon lesson that reported the
intellectualist's observation as the book's (found and repaired by the second
reviewer during this pass); a reading instruction that stopped two pages
short of what the lesson then reads; a Husserl phrase restructured as three
consequences when the text unfolds one; a claim about the Preface ("nobody
occupies" the view from nowhere) that is true of the Preface but was not
tied to the sentence that makes it so; one tile on the page the prose never
mentioned; and two unglossed terms (*natural attitude*, *posits*) in a course
that promises to assume no philosophy. Nothing needs splitting, merging or
reordering.

## The voice, judged against §F

This course sets the register for six more, so what works is named as
concretely as what does not.

**What works, and should be copied:**

- **The passage first, then the phrases in order.** Every body opens with
  `<strong>Preface, p. n.</strong>` and the passage, then names the page,
  then tells the reader which pages to read whole in their own copy before
  going on, which is what §E.3 asks of a book in copyright. Then it returns
  to the passage a few words at a time: "Now the passage. Reflection 'does
  not withdraw from the world'… It 'steps back', which is a different thing:
  you step back from a painting to see it, not to stop looking"
  (`the-reduction-and-its-limit`); "'The essence is here not the end, but a
  means': the eidetic step is taken for the sake of something else. What
  that is comes next" (`essences-and-existence`); "'Perspectives blend,
  perceptions confirm each other, a meaning emerges': three verbs, none of
  them a verdict from outside" (`intentionality-and-rationality`). This is
  §F rule 1 done exactly, and each `read_intro` says which passage is coming
  and in what order the lesson will move.
- **The book read whole before the passage.** Lessons 1 and 3 go back to the
  Preface's first page before reading their own passage ("The Preface's
  first page had said two things that seemed to pull apart"), and lesson 2
  reads the idealist presentation of the reduction (the red book, Peter and
  Paul) before the passage that rejects it, so the reader meets the view
  being refused before the refusal. That is the order the lectures take and
  the one the authors should keep.
- **Scenes rationed, and only where the object is in the reader's life.**
  Two of four lessons open with a scene: the full moon behind the roofs, and
  a cereal box between two people at a table. The other two open with the
  text. That is exactly the half §F.2 allows, and both scenes reach the
  chapter's category within the paragraph ("That, in a kitchen, is what the
  passage calls rationality").
- **The history of ideas as a story with people in it.** Fink is "Husserl's
  assistant in Freiburg from 1928", whose 1933 defence Husserl prefaced; the
  Vienna Circle is "Moritz Schlick, Rudolf Carnap and Otto Neurath among
  them", with their caution about the word *consciousness* given its best
  form before the Preface's "flat" reply; Jean Wahl "had written on
  Kierkegaard and on Hegel's unhappy consciousness and had called for a
  philosophy turned towards the concrete" and "was making a serious charge";
  Ehrenfels in 1890 "asked what stays the same when a melody is transposed";
  Brentano in 1874 "made directedness at an object the mark of the mental".
  Each opponent gets the fact his view rests on before the Preface replies,
  which is §F rule 3 and "presented, not endorsed" at once.
- **Whose voice.** The course `how_to` warns the reader to "watch whose voice
  a sentence is in", and the lessons do it: the red-book regress is "the
  reading it sets aside"; the Vienna Circle's view is "as the Preface states
  it"; the argument for a standpoint above the views is "the idealist's
  argument", "at its strongest". Lesson 2 says three times, in `p`, `def`
  and `note`, that the reduction here is "the Preface's reading" and that
  how far it is Husserl's "is still disputed", which is §F.4 done without
  fuss.
- **Second person, warm, in `p` and `worked.intro` only.** "You saw a cube
  with a front at once. Which square is in front is not in the lines; it was
  your contribution"; "A thread pulled tight is invisible from inside the
  pull. Let it go slack and you see it"; "The net is not the catch. You throw
  it to bring up what is alive." `steps`, `standard`, quiz items and tile
  text stay impersonal; no "let's", no "dive in", no first-person anecdote,
  no exclamation mark anywhere in the course.
- **One light remark, and the author's before the lesson's.** Lesson 4
  points at the Preface's own joke ("history does not walk on its head… it
  does not think with its feet") and calls it "borrowed and then improved".
  Nothing else in the course tries to be funny.
- **The limit admitted, and the lab turned against itself where that is the
  point.** Every `note` names the one thing the lab cannot do: it "cannot
  compute how large the moon looks"; it "counts readings as solids" and
  cannot show the book's third, flat reading; its core "is only as good as
  the lesson's coding"; it "can only check a report against a complete cube
  it holds in advance, the view from nowhere". Lesson 4 makes that last
  limit the lesson ("Notice how the lab knows"), which is the right use of a
  lab in a Subject whose claim is that the figure is not the experience.
- **Family and model named.** Every `panel_intro` says what the lab computes
  and whose: "geometric optics in its small-angle form", "parallel
  projection", "the lesson's coding". The course `footer_lead` says which
  figures are astronomy's and which illustrative, and ends "None of them is
  an experience, which is what the Preface is about." That sentence is the
  Subject's material clause in one line and should be copied.
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson's question by its title, and lesson 4 ends with the next
  course by its §B title, Classical Prejudices, and its first object, "the
  idea of a pure sensation".
- **No modern aside.** §F.1 gives Course 1 none, and it has none.

**What to change in the courses that follow (and what was changed here):**

- **An observation Merleau-Ponty concedes is not an observation he makes.**
  The moon lesson said "the book's own version of the test is a cardboard
  tube or a telescope, through which, it reports, the horizon moon looks no
  bigger than at the zenith". On p. 32 that sentence is the intellectualist's
  ("The moon on the horizon is not, and is not seen to be, bigger than at its
  zenith"), and on p. 36 Merleau-Ponty grants the observation in a
  conditional and denies the conclusion drawn from it. The second reviewer
  rewrote the sentence during this pass so that it names the intellectualist
  and gives the reply. The rule for the brief: the Introduction and Part One
  are full of sentences in which the book states, for a page, the view it is
  about to reject, and AUTHORING already says so for quotations; it must be
  read to cover paraphrases that begin "the book reports" or "the book
  says" too.
- **Tell the reader exactly which pages to read, and make it the pages the
  lesson then reads.** Lesson 1 asked for pp. vii to the end of the
  geography paragraph on p. x, then read on through the analytical-reflection
  pages to "the background from which all acts stand out" on p. xii.
  Repaired: the instruction now runs to the first paragraph of p. xii, "just
  before the reduction is introduced". Lessons 2, 3 and 4 already give exact
  page ranges and should be the model.
- **Gloss the Preface's terms the first time, not the second.** *Natural
  attitude* appeared in lesson 1 unglossed and was defined in lesson 2's
  `concepts`; *posits* appeared in lesson 4 unglossed. Both now carry a
  gloss of a few words in the sentence. A reader with no philosophy, which
  the course `assumes_long` promises to serve, should never meet
  *transcendence*, *antepredicative*, *eidetic*, *facticity*, *posit* or
  *natural attitude* without an English phrase beside it on first use; this
  course does that for every other term.
- **When a tile is on the page, the body must say what it shows.** The
  `faces` lab prints five tiles, and the `three` preset's cover tile
  ("front-right-above, back-left-above (2 views)") was explained nowhere.
  One clause added. The rule from Capital holds here in the stronger form:
  every preset *and every tile* the view prints appears in a body paragraph
  with what it is a figure of.
- **Tie a claim about the Preface to the sentence that makes it.** "The
  standpoint the Preface says nobody occupies" was true, but the Preface
  never uses those words; what it says is that if we were absolute mind the
  reduction would present no problem, and that "there is no thought which
  embraces all our thought" (p. xv). The body now says so and names the
  section. The habit to copy: when a lesson says the Preface "says",
  "denies" or "concludes" something, it should be able to point at the page
  and, ideally, name the sentence in the lesson's own words.
- **Do not restructure the text's own order into a list the text does not
  have.** Lesson 2 said "the section draws three consequences, and the first
  is Husserl's own"; on p. xv the three are all glosses of one phrase from
  the unpublished work, "a perpetual beginner", and the text says "It means…
  It means also… and finally". Reworded so that the phrase is unfolded as
  the text unfolds it. Harmless here, but a reader following in the book
  looks for the list and does not find it, as Capital's reader looked for a
  fourth case.

## What the course teaches well

- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names the product: an angle "as a ratio
  and in degrees… and which question about the object the figures answer and
  which they leave to description"; the readings a drawing fits "by
  comparing each reading's edges with its mirror image's"; a core, what
  varies and "what each excluded variant lacks"; the faces each direction
  sees and "whether each report fits its direction". The five course
  `outcomes` are the same acts, with a fifth that is the reading's: state
  each opponent and the Preface's reply.
- **One hard idea per lesson, and the Preface's own order kept.** Lesson 1
  carries description against explanation and against analytical reflection
  and nothing of the reduction; lesson 2 carries the reduction and its limit
  and says in one line that the next lesson asks what the step back is for;
  lesson 3 carries essences as means and stops at "what I live through";
  lesson 4 carries intentionality and rationality and summarises the pages
  on history in one paragraph, which the course `not_covered` says it will
  do. The `how_to` tells the reader the Preface is a summary of a book they
  have not read and may be clearer afterwards, which is true and kind.
- **The misconceptions are refuted with the specific figure.** "The overhead
  moon subtends `3474/378029`, about `0.0092` rad, more than the horizon
  moon's `0.0090`, and nothing in the Preface says otherwise" (lesson 1).
  "Nothing about the drawing is doubted, and its 12 edges are exact; what
  shows is that which square is in front was never in it" (lesson 2). "The
  sound preset's core is `some-duration`, true of every tone and silent
  about the one you hear, and the melody's core is a pair of intervals, a
  relation" (lesson 3). "The conflict preset's verdict… is reached by
  checking against a complete cube the lab holds from nowhere, which is the
  one thing a perceiver never has" (lesson 4).
- **The arithmetic is right, and each figure is attributed to its model.**
  `3474/384400 = 1737/192200 ≈ 0.009037` rad, `≈ 0.52°`; `384400 − 6371 =
  378029`, `3474/378029 ≈ 0.009190` rad, `≈ 0.53°`, larger by 1.7%, "about
  two per cent"; `7/770 = 1/110 ≈ 0.009091`, which covers the horizon moon
  and falls short of the overhead one, as the prose says; `9 mm / 990 mm =
  1/110` in the quiz. The wire cube's `4 + 4 + 4 = 12`, the solid's `12 − 3 =
  9`. The melody's intervals are right (C–E–G, D–F♯–A, B♭–D–F each a major
  third then a minor third; G–E–C the reverse), and the D and B♭ versions
  share no note with C, as §C requires. `1 2 2` has length 3 and sees right
  1/3, above 2/3, front 2/3; `−2 1 −2` sees left 2/3, above 1/3, back 2/3;
  union 5 of 6, no view below. The lesson says each time that the moon's
  figures are astronomy's and the rest illustrative, that the foreshortening
  is "the lab's projection", and that the coding is "the lesson's".
- **The labs earn their place, each for a different reason, and the lesson
  says which.** The moon (family 1, geometric optics) computes a figure
  nobody disputes and uses it to show what a figure is not: "They are the
  map, and the moon over the roofs is the countryside", which is the
  Preface's own comparison carried into the lab. The cube (family 1,
  parallel projection) computes what a drawing does not contain, and the
  lesson is honest that the reduction is illustrated "in small" and that
  the book's own reversible figure (p. 306) has a third reading the lab
  cannot draw. The variation lab (family 2, the lesson's coding) is the
  best of the four: the melody preset makes a real point the Preface's
  "fisherman's net" needs, that what stays can be a relation and not a part,
  and the `C notes backwards` variant, which keeps every note and loses the
  core, is a well-designed instance. The faces lab (family 1) is used
  against itself, as above.
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first preset by hand; every `panel_intro` asks for a
  comparison before the press ("Compare the horizon and zenith presets";
  "Switch from the cube preset to the solid preset and watch the readings
  tile"; "Compare the sound and melody presets"); every quiz asks the same
  act on a fresh instance (a 9 mm coin at 99 cm; three cups; `1 2 2` with a
  front view). The distractors are the named errors: `1/11` for mixed units,
  `2/9` for dividing by the squared length, "A solid cube has only 9 edges".
- **The Preface's own images are the Preface's.** The sparks from a fire,
  the slackened threads, the red book, Peter and Paul, the fisherman's net,
  the gears, history's head and feet, Balzac, Proust, Valéry and Cézanne are
  all where the lessons say they are, in Smith's words where quoted and in
  fair paraphrase where not.
- **The cross-references are right.** The moon is cited to Introduction III
  (pp. 32 and 36) and Part Two Chapter 2 on depth (p. 302); the reversible
  figure to p. 306, Fig. 1, with its three readings as the book lists them;
  the house seen from nowhere to Part One, Experience and Objective Thought
  (p. 77). All five were checked against the page. Lessons are cited by
  title, chapters by Part and number, the next course by its §B title.

## What it taught badly, or said wrongly

### Fidelity

- **`description-not-explanation`, body (the tube and the telescope):** as
  above. Found in this pass; repaired by the second reviewer before this
  pass reached the file, with wording that names the intellectualist and
  gives the p. 36 reply. Checked against the page: faithful.
- **`the-reduction-and-its-limit`, body ("three consequences"):** as above.
  Repaired.
- **`intentionality-and-rationality`, body ("the standpoint the Preface says
  nobody occupies"):** as above. Repaired by tying the claim to p. xv.
- **`intentionality-and-rationality`, body:** "in absolute Spirit, as Hegel
  would have it". The Preface says "absolute Spirit" and does not name Hegel
  in that sentence (it names "the Idea in the Hegelian sense" two pages
  earlier). The attribution is standard and not wrong; left, and recorded so
  the authors know the words are the lesson's.

### Prose that left the lab, or the reader, unexplained

- **`intentionality-and-rationality`, body:** the cover tile. Repaired.
- **`description-not-explanation`, body:** the reading instruction. Repaired.
- **`description-not-explanation` and `intentionality-and-rationality`:**
  *natural attitude* and *posits* unglossed. Repaired.

### Quiz

Every distractor on the sixteen questions was argued for and could not be
defended. The one that came closest was lesson 2's "Our belief that the world
exists" as what the reduction suspends: a reader who knows Husserl's own
word for the epoché, the bracketing of the general thesis of the natural
attitude, could argue for it, but the question asks "on the Preface's
reading", and the Preface says the reduction is "not because we reject the
certainties of common sense". The second reviewer tightened the distractor to
"until doubt has proved it" during this pass, which closes the gap. Lesson
3's cup question is a clean instance of the act (core `holds liquid`), and
lesson 4's operative-intentionality question is the best conceptual item on
the course: its three distractors are the three kinds of act the Preface
names.

### Speech

Every math run on the four pages was read from `data-say`. The figures read
well: "3474 over 384400 equals 1737 over 192200 is approximately 0.0090 rad",
"1 plus 4 plus 4 equals 9, so its length is 3", "right 1 over 3, above 2 over
3". No short word at the head of a key line is spelled out (the authors
avoided `due`, `out` and their kind; every key line starts with a word of
four letters or more, or a full name), no step is split at its spaces, and
the preview lists no unspoken run. One line reads clumsily rather than
wrongly: "in degrees, is approximately 0.52 degrees low, is approximately
0.53 degrees high". Left; see recommendations.

### Cross-references

Lessons are cited by title (“The Reduction and Its Limit”, “Essences and
Existence”, “Intentionality and Rationality”, each exactly as the lesson
carries it); the book by Part, chapter and section, as §0's first deviation
requires; the next course by its §B title. No lesson is cited by number.

## Can a first-time reader of the Preface follow the four lessons?

Yes, with the help the course already gives, and the places a reader will
slow down are the places the Preface's readers slow down.

- **Lesson 1** moves from the moon behind the roofs to the Preface's opening
  question, lists the apparent contradictions as the text lists them, gives
  the "manner or style of thinking" answer, and only then reads the passage.
  The `def` block that separates describing, explaining and analysing is the
  one a first-time reader needs and arrives before the hard paragraph on
  Descartes and Kant. That paragraph is the course's densest, and it is
  handled by stating the idealist's point "at its strength" in one plain
  sentence ("whatever world there is, it is a world for someone") before the
  objection. The map-and-countryside paragraph is the best single paragraph
  on the course and should be the model for the "phrase by phrase" move.
- **Lesson 2** is where readers of the Preface give up, and the lesson
  protects them three ways: it says who Fink was and why it matters that the
  reading leans on him; it reads the red-book regress as the view being set
  aside, so the reader is not asked to hold it as true; and it gives the
  painting ("you step back from a painting to see it, not to stop looking")
  and the thread as everyday images for *step back* and *slacken*. The
  Descartes paragraph, in the second reviewer's revision, now gives the
  concession and the objection from p. x in order, which is more faithful
  and slightly harder; a first-time reader will manage it because the `def`
  block that follows restates the result in two lines.
- **Lesson 3** is the lightest to read and the lesson says why: the Preface
  "names the eidetic step but not this procedure", so the lab is the only
  place the reader meets free variation, and it is introduced as the
  lesson's own. The Vienna Circle and Wahl paragraphs give a reader with no
  philosophy two real opponents in two paragraphs. The melody paragraph is
  the one place the course teaches something the reader did not know and
  could not have guessed, and it lands.
- **Lesson 4** moves fastest, as the Preface's last pages do, and the lesson
  says so in `concepts_intro`. The cereal box gives the reader rationality
  before the word; the Brentano–Kant–*Critique of Judgement* paragraph is
  the hardest history on the course and is kept to four sentences; the
  "three verbs, none of them a verdict from outside" reading of the passage
  is exactly right for a reader who has never seen a definition that
  refuses to be one. What a first-time reader will still miss is the
  Preface's own summary sentence, that phenomenology has "united extreme
  subjectivism and extreme objectivism", and its most quoted line, that
  "we are condemned to meaning". Recorded below, not repaired.

The course protects the reader in two further ways later courses should
keep: the `how_to` says the Preface may be read after the book and that the
next course does not depend on these labs, and every lesson says in `p`,
`panel_intro` and `note` that its instance is the lesson's and not the
Preface's, so a reader never mistakes the cube for a claim about Husserl.

## Repairs made in this pass

In `content/phenomenology/c1_preface/part_a.py`: `description-not-explanation`
the opening `p` (reading instruction to p. xii) and the opening-question
paragraph (*natural attitude* glossed); `the-reduction-and-its-limit` the
"perpetual beginner" paragraph; `intentionality-and-rationality` the
Kant paragraph (*posits* glossed), the `three` preset paragraph (the cover
tile), and the `conflict` paragraph (the p. xv sentence). Nothing in
`__init__.py`. No preset, `expect`, slug, module, lab key, mode or view
changed, and no §C entry needed correcting: every instance the lessons carry
is the one §C records, including the "As authored" sound, table and melody
sets.

The second reviewer's concurrent changes to the same file (the tube
paragraph, the Descartes concession-and-objection paragraph, "true size" to
"true area" throughout the faces lesson, the quiz 1 distractor in lesson 2,
and several smaller rewordings) were read after they landed and are
consistent with the text and with this assessment; none is claimed here.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and
§C list them. `python3 scripts/preview_subject.py phenomenology --course
perception-what-phenomenology-is` reports OK: 5 pages, every lab executes
and survives the sweep, every pinned figure on the four pages matches, no
math run without a spoken form. `phen_quotes.py c1_preface` reports OK: no
span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **§C still carries "(wording to be checked against the text)" on four
  phrases the lessons have now checked**: the geography comparison and
  "naïve and dishonest" (lesson 1), "intentional threads" and "the
  impossibility of a complete reduction" (lesson 2), "what I live through"
  (lesson 3). All four are quoted correctly on the pages. AUTHORING makes
  the §C correction the author's, in the same change; it was not done, and
  PLAN.md is outside this assessment's files. The author should strike the
  markers and add "(checked: p. n)" as the lesson 3 and 4 entries already
  do.
- **The Preface's two summary sentences are missing from lesson 4.** "The
  chief gain from phenomenology is to have united extreme subjectivism and
  extreme objectivism" (p. xxii) is the sentence before the passage and is
  the best one-line answer to the course title; "we are condemned to
  meaning" (p. xxii) is the line most readers know. Lesson 4 has eleven
  words of quotation budget left, enough for the second. A sentence each,
  in the history paragraph and the "Now the passage" paragraph, would cost
  nothing in load.
- **The worked line "in degrees:  ≈ 0.52° low, ≈ 0.53° high"** reads aloud
  as "in degrees, is approximately 0.52 degrees low, is approximately…".
  "in degrees:  about 0.52° low and 0.53° high" would read naturally and
  keep the approximation. A key-line convention for the brief: put the `≈`
  once, at the head of the line, or say "about".
- **Lesson 2's necker lab is listed as family 1 in §C and its `panel_intro`
  says "parallel projection"**, but nothing in it is an opponent's
  prediction; it is the lesson's own illustration, as the prose says. The
  model name is honest and the tile is exact, so nothing is wrong on the
  page; but the brief should say that where a family-1 label means "the
  geometry, which nobody disputes" rather than "the constancy hypothesis",
  the `panel_intro` should say so in a clause, as lesson 1's does ("the
  figures are exact, and neither is a report of how large the moon looks").
- **"as Hegel would have it"** in lesson 4 attributes "absolute Spirit" to
  Hegel in the lesson's voice. True and standard, but the Preface does not
  say it there; "absolute Spirit, Hegel's term" would mark whose words they
  are.
- **The faces lab's `peMax` tile** ("Most faces one view sees: 3") is on the
  page and is obvious, and is not named in prose. Harmless; recorded so the
  stronger rule above is not read as broken.

## Lessons for the remaining authors

1. **Read the whole section before the passage, and name the voice of every
   sentence you paraphrase.** The one fidelity error on the pilot was a
   paraphrase of the intellectualist's observation as the book's report.
   The Introduction and Part One state the opponent's view for a page at a
   time; "the book says" is not enough, and "the book reports" is worse.
2. **Give the reader an exact page range to read in their own copy, and
   make it the range the lesson then reads.** Lessons 2 to 4 do this; lesson
   1 did not, and was the one a reader would have found themselves beyond.
3. **Every claim that the Preface "says", "denies" or "concludes" something
   should be able to point at a sentence.** If the sentence is in another
   section or another Part, say where ("in the section on the reduction";
   "at the start of Part One").
4. **Do not impose a list the text does not have.** "Three consequences",
   "four cases", "two reasons" send a reader to the book to count.
5. **Gloss every term of art on first use, in English, in the sentence**:
   natural attitude, transcendence, eidetic, facticity, posit, antepredicative,
   noesis and noema, hylè, Sinngebung. The pilot does this well for most and
   missed two.
6. **Every tile the view prints, not only every preset, appears in a body
   paragraph with what it is a figure of.** `faces` prints five; the pilot
   explained four.
7. **Say which family the lab is in and whose model it computes, in the
   `panel_intro`, and when the "model" is only geometry say that nothing in
   it is disputed.** The pilot's moon lab is the pattern.
8. **Ration scenes to half the course's lessons and open the rest with the
   text**; the pilot's two-of-four is the ceiling, not the floor.
9. **Name the people**: who Fink was and when; who was in the Vienna Circle;
   what Wahl had written. One sentence each is enough and makes the
   opponent real before the reply.
10. **Let the Preface's own best lines carry the summary** where the budget
    allows; the pilot's lesson 4 left eleven words unspent and two of the
    Preface's most useful sentences unquoted.
11. **Keep the quotation checker and the preview green after every edit**,
    and re-read the file before each edit when another agent is in it; the
    pilot was reviewed by two agents at once and the file changed under both.

Final lines. Preview: `OK` (5 pages rendered; labcheck, every lab executes:
4 page(s) executed and swept, 0 failing; labcheck, pinned figures match: 4
page(s) executed and swept, 4 with pinned figures, 0 failing). Quotation
checker: `OK` (117, 129, 137, 139 quoted words; openings 68, 66, 43, 56).
