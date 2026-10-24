# Pedagogy assessment — The Cogito, Time and Freedom (Phenomenology of Perception, course 7)

Formed from the eight lesson dicts in
`content/phenomenology/c7_cogito_time_freedom/` (`part_a.py`, the three Cogito
lessons and the first Temporality lesson; `part_b.py`, the rest of Temporality
and the two Freedom lessons; `__init__.py`, the course dict) and the kits they
render through (`argkit/validity` for the cogito as an inference;
`scripts/mathpath/labs/phenkit.py` modes `triangle/parallel`, `cases/table`
twice, `time/river`, `time/diagram`, `time/ekstasis`, `schema/obstacle`), on
branch `feat/phenomenology-subject`. The design authority is
`docs/phenomenology/PLAN.md` §0, §B, the Course 7 entries in §C, §D as
summarised in `docs/phenomenology/kit-report.md`, §E and §F, with
`docs/phenomenology/AUTHORING.md` and its two "Lessons from" sections, and the
Course 1 assessment (`phenomenology-perception-what-phenomenology-is.md`) as
the model. This is the Subject's last course, so the assessment also asks
whether it closes the Subject.

Every lesson was read in full before anything was changed. The whole of Part
Three (Smith pp. 429–530) was read first, chapter by chapter, then each
lesson's passage and the pages it reads line by line. Every pinned tile was
read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py phenomenology --course
perception-cogito-time-and-freedom`), including the tiles no preset pins (the
diagram's `tiProtended: none`, the obstacle lab's two tiles across the three
presets, the validity lab's four tiles under both the preset and the `show`
menus); every figure in prose, worked lines and quiz `why`s was recomputed by
hand; every `data-say` on the eight pages was read; and all 68 spans in
`&ldquo;…&rdquo;` were run through the Subject's quotation checker
(`phen_quotes.py c7_cogito_time_freedom`), with the opening passages and the
in-body quotations checked by eye against the page they cite. Lessons, in
course order: `the-cogito-and-the-certainty-of-seeing`, `the-triangle`,
`the-tacit-cogito`, `time-is-not-in-things`, `the-field-of-presence`,
`time-as-subject`, `the-rock-and-the-project`, `freedom-in-situation`. The
course is marked Advanced and assumes the earlier courses, but the lessons are
judged, as the Subject promises, against a reader with no philosophy and
school geometry.

A second reviewer was reviewing this course at the same time; each file was
re-read immediately before each edit, and no edit conflicted.

## Verdict

The course teaches its subject and closes the Subject well. A reader who
finishes it can write an argument in sentence letters, find its counterexample
rows and name the premise that would make it valid, and say why the chapter
does not read the cogito as an inference; compute a triangle's third angle and
the alternate and straight angles of the parallel construction at any vertex,
refuse an impossible pair, and say what the construction adds to the
definition; code a chapter's cases against two opponent accounts, compute each
record, the survivors, the split and the cases both fail, and state the
chapter's own account without scoring it (done twice, for language and for
conduct); classify a river's water from two standpoints and with none; read
Husserl's diagram at any present and follow one moment across several; and
reckon an obstacle against a project and against a body. Those are the acts
the eight `standard` fields name and the quizzes measure. The `mistakes[0]` of
every lesson is the §C misconception, each refuted with the lesson's own
figure or the chapter's own sentence: the cogito's one countercase row, `p
true, q false`; the alternate angles `60° and 70°` that appear "only once the
line is drawn"; the tacit cogito that "is a cogito only when it has found
expression for itself"; the river's `w5, w6, w7` past from the bank and the
reverse from the boat; retention at `depth 2` that is "the past held in the
present's own thickness"; the single column that "holds every depth and no
passing"; the `body` preset's `none` beside `3 m`; and "never determinism and
never absolute choice". All 8 pages' pinned tiles match the lab (the preview
reports OK), and every figure in prose agrees with the lab or with a
recomputation.

Fidelity to Part Three is high, and higher than the pilot's, because the
authors have learned the pilot's one lesson: whose voice. Every one of the 68
quoted spans is in Smith's text character for character (the checker reports
OK with no misses; the quotation budget is 126, 114, 111, 107, 92, 114, 113
and 130 words of the 150 allowed; openings 60, 60, 38, 45, 48, 43, 46 and 42
of 70). The Cogito's six idealist pages are read as "the voice of an
idealist", with Lachièze-Rey named from the footnotes; the feeling objector's
sentence on p. 439 is marked as "the objector's, and the next one turns on
it"; the geometry objector on p. 447 is "the objector"; the idealist's class
argument on p. 514 "comes first in the idealist's voice"; and Freedom's opening
pages are "in that theory's voice, not Merleau-Ponty's", with Sartre's single
appearance in the body text (p. 509) and the footnote citations counted
correctly. Every "the chapter says" or "concludes" was traced to a page, and
all but a handful were on the page named. Merleau-Ponty is presented, not
endorsed: Descartes (Second Replies and Principles I.10, both given), Kant
(A716–17/B744–45, named as the lesson's comparison), Husserl, Bergson,
Heidegger and Sartre each get their position at strength before the reply,
and four disputes are flagged where §F.4 asks for them and in the right
places: the tacit cogito (Merleau-Ponty's own working note), the reading of
Husserl's flow through Fink and the manuscripts, the fairness to Heidegger's
primacy of the future, and whether the theory of absolute freedom is Sartre's
or a sharpened Sartre (with Beauvoir's 1955 charge correctly tied to the later
book, not this chapter). No modern aside, as §F.1 requires of this course.

The defects found were local, and all those with a determinate answer are
repaired: a reading instruction in the rock lesson that stopped "at the end of
the paragraph on fatigue on page 513" when that paragraph runs to p. 514 and
contains the next lesson's first case; the first sentence of Freedom, which
Merleau-Ponty shares, listed among the theory of absolute freedom's claims; a
concept that said the chapter states absolute freedom "in its own voice",
readable as the chapter's; a quiz `why` that called 105° "the exterior angle"
of a 40°–75° triangle (the exterior angle at the third vertex is 115°; 105° is
the exterior angle at the 75° vertex, and the `why` now says so); Gurwitsch
described as "then teaching in Paris" when he had left for the United States
in 1940, and Wertheimer's "alternately" collapsed into "at once"; a closing
sentence that said the book "asks" to have its Preface read first, which
nothing in the book says; the course `how_to` counting three family-3 labs
when there are four; and three terms a reader with no philosophy would meet
unglossed (*constitutes*, *transcendental idealism* and *absolute realism*,
*positing thought*). Nothing needs splitting, merging or reordering.

## The voice, judged against §F

**What works:**

- **The passage first, then the chapter in its own order.** Every body opens
  with `<strong>Part Three, Chapter n, p. m.</strong>` and the passage, names
  the page, gives an exact range to read in the reader's own copy, and then
  goes back to where the chapter starts and walks forward. Lesson 1 does this
  best: it reads the desk on p. 429, the six idealist pages, the "middle
  course" on p. 435, and only then "So, to the passage." Lesson 7 reads the
  theory in its own voice for three paragraphs, the rock, the theory's
  self-inflicted trouble (pp. 507–510), the concession on p. 510, and only then
  "The reply is the passage." That is the lectures' order and §F rule 1 done
  exactly.
- **Whose voice, on every page.** The course `how_to` warns the reader to
  "watch whose voice a sentence is in" and names the two places it matters
  most; the lessons deliver: "in the voice of an idealist"; "That sentence is
  the objector's, and the next one turns on it"; "The objector concludes";
  "The second case comes first in the idealist's voice"; "in that theory's
  voice, not Merleau-Ponty's"; "the theory's rejoinder is". The pilot's one
  fidelity error was a paraphrase in the wrong voice; this course has none of
  that kind.
- **Scenes rationed to three of eight.** The school proof ("You were probably
  shown this proof at school"), the bridge ("Stand on a bridge and watch the
  water") and the valley path with boulders. Each reaches the chapter's own
  case within the paragraph, and the other five open with the text's own
  object: Descartes's doubt, the reader with a book, the diagram (twice), the
  sentence about a life. Under §F.2's half.
- **The history of ideas with people in it.** Descartes "set out in his
  Meditations of 1641 to doubt everything that could be doubted"; Lachièze-Rey
  is "a French interpreter of Kant"; Scheler "the German phenomenologist of
  value"; Wertheimer "who studied how people solve problems by seeing a figure
  anew"; Husserl's 1905 lectures "which Martin Heidegger edited for publication
  in 1928"; Bergson "the most widely read French philosopher of the century's
  first decades"; Sartre "who had known Merleau-Ponty since the École normale
  and in 1945 became his co-editor of the review Les Temps modernes"; Voltaire's
  Micromégas "of 1752 about a giant from Sirius"; Saint-Exupéry who "flew a
  reconnaissance mission over Arras in May 1940". One sentence each, before the
  reply, as the pilot asked.
- **Second person, warm, in `p` and `worked.intro` only.** "You were probably
  shown this proof at school"; "Stand on a bridge"; "If you mean to scramble up
  one, each is suddenly easy or hard, a handhold or a wall"; "read it again
  now". `steps`, `standard`, quiz items and tiles stay impersonal. No "let's",
  no "dive in", no exclamation mark, no first-person anecdote in the course.
- **The light touch, once, and the author's before the lesson's.** "a sliver
  of a triangle with the parallel almost on its long side"; the chapter's own
  "I say the Alps are molehills"; "The lab can only state the premise for me."
  Nothing performs friendliness.
- **The limit admitted and the lab turned on itself where that is the
  point.** Every `note` names what the lab cannot do, and three lessons make
  the limit the lesson: the triangle lab "computes the third angle from the
  theorem itself… It illustrates the construction and proves nothing";
  "Notice how the lab knows"; the ekstasis lab "can lay columns side by side,
  but it cannot pass from one to the next, which is what the chapter says the
  subject is"; the counterexample row "is a line in a truth table, not anyone's
  experience". That is the Subject's material clause worked into the teaching,
  and the right use of a lab in a Part of the book that has no quantities.
- **Family and model named.** Every `panel_intro` says what is computed and
  whose: "classical propositional logic, which nothing here disputes"; "the
  lesson's model… Nothing in the geometry is disputed"; "the lesson's coding…
  the tacit cogito is in the prose, not in a column"; "Husserl's diagram, as
  the lesson's model… The depth is a count of steps, not a measure of how far
  away anything feels"; "The heights are illustrative." The `cases` tables
  carry the opponents only, as §0 requires, and both lessons say so in the
  `after`, a mistake and the `note`.
- **Pointing forward by title, and the Subject closed.** Every body ends with
  the next lesson by title; lesson 8 ends where the book does, on
  Saint-Exupéry, and then sends the reader back to the first lesson of the
  first course by title, with the reason: it "will read differently after the
  body, the perceived world and time." That is the right close for a Subject
  whose Preface was written last.

**What was changed, and the rule for the record:**

- **A reading range that ended inside a paragraph was called a paragraph's
  end.** The rock lesson said "to the end of the paragraph on fatigue on page
  513"; that paragraph begins on p. 512 and ends on p. 514, and its second half
  is the inferiority complex, the next lesson's first case. Both lessons now
  name "the sentences on sedimentation in the middle of page 513" as the
  boundary, and the rock lesson says the paragraph runs on into the next
  lesson's first case. The rule from the pilot stands: the instruction gives
  the range the lesson then reads, and a boundary inside a paragraph is named
  as one.
- **A claim the chapter shares was listed among the opponent's.** "No causal
  relation is conceivable between the subject and his body, world or society"
  is the first sentence of Freedom (p. 504) and is Merleau-Ponty's own view
  (he repeats it in his own voice on p. 515: "there is no cause which can act
  from outside upon a consciousness"); what the theory of absolute freedom
  adds is the next step, rejecting motivation as well (p. 505, with Sartre in
  the note). The paragraph now says the first sentence is one he shares and
  that "the theory goes on from there." The converse of the pilot's rule: a
  sentence in the opponent's pages is not thereby the opponent's.
- **"In its own voice" was ambiguous.** The absolute-freedom concept said the
  chapter "states it in its own voice for several pages", which a reader can
  take as the chapter's voice. Now "in the theory's own voice".
- **A quiz `why` named the wrong angle.** For a 40°–75° triangle the
  distractor 105° was called "the exterior angle"; 105° is 180° − 75°, the
  exterior angle at the second vertex, and the exterior angle at the third
  vertex is 115°. The `why` now says which, so the distractor is still the
  named error (subtracting one angle alone) and the explanation is right.
- **Gurwitsch's dates, and Wertheimer's word.** Aron Gurwitsch lectured in
  Paris from 1933 and left for the United States in 1940; "then teaching in
  Paris" was wrong for a book of 1945. And the chapter says Wertheimer's proof
  sees the sum "alternately" as equal to the triangle's angles and to two
  right angles, with Gurwitsch's addition that "the first survives for me
  while the second is in process of establishing itself" (p. 447); the lesson
  had fused the two into "two groupings at once". Both repaired.
- **"As the book asks."** The closing paragraph said the reader read the
  Preface first "as the book asks". The book does not ask it; the Preface was
  written last and Course 1's `how_to` says it may be clearer afterwards.
  Removed.
- **The lab count in the course `how_to`.** "three are the lesson's models of
  the chapter's images" counted river, diagram and ekstasis and forgot the
  obstacle lab (family 3, "the lesson's model"); with the triangle, the
  validity lab and the two `cases` tables that made seven labs for eight
  lessons. Now four. The `footer_lead` now also names the rocks.
- **Terms glossed on first use.** *Constitutes* (lesson 1, the idealist
  reading) now carries "builds each one up out of its own resources";
  *transcendental idealism* and *absolute realism* (lesson 1, the p. 437
  dilemma) each carry a clause; *positing thought* (lesson 3, p. 470) carries
  "the kind that sets an object before itself". *Ek-stase*, *self-affection*,
  *passive synthesis*, *retention*, *protention*, *Abschattung*,
  *intentionality*, *facticity*, *analytic necessity* and *acosmic* were
  already glossed in the sentence or in a `concepts` entry.

## What the course teaches well

- **One hard idea per lesson, and the chapter splits where PLAN §B says.**
  The Cogito in three (the certainty of seeing and of feeling, the triangle,
  the tacit cogito), Temporality in three (the river, the field of presence,
  time as subject), Freedom in two (the rock, freedom in situation). Lesson 1
  stops at the middle of p. 446 "where the triangle begins"; lesson 2 at the
  end of the paragraph on p. 451; lesson 3 summarises pp. 459–464 (evidence,
  Spinoza, contingency) in one sentence, which the course `not_covered` says
  it will. The chapter's own hinge sentences are used as hinges: "The
  non-temporal is the acquired" (p. 457) is "the hinge to the next chapter, on
  time"; "the basis of our freedom" (p. 503) hands over to Freedom.
- **The objectives are acts and the drill measures them.** Each `standard`
  begins "Finish when you can…" and names a product the quiz then asks for on
  a fresh instance: a 40°–75° triangle; water at 1–7 with the observer at 2;
  moments A–E with E present; B's depths under C, D and E; rocks of 1–4 m with
  capacity 3 and level 2; the records from a stated coding. The distractors
  are the named errors (the row with p false; counting the silent cell as a
  failure; a rock equal to the capacity; the exterior angle).
- **The arithmetic is right and each figure is attributed.** `180 − 130 =
  50`; `60 + 50 + 70 = 180`; `1 + 178 + 1 = 180`; `100 + 90 = 190` refused;
  `180 − 115 = 65`. Observer at 4 on the bank: past 5–7, future 1–3; in the
  current, the reverse; at 2, past 3–7. A at depth 2 under C and 3 under D;
  B at 1, 2, 3 under C, D, E. Thought-first `y, n, n` absorbs 1 of 3 and
  fails 2; language-first `n, y, -` absorbs 1, fails 1, silent 1; split on 1
  and 2, the third `n` against silent "is not a split". Determinism `y, n, n,
  n` and absolute freedom `n, y, n, n`, each 1 of 4; both fail 3 and 4. Rocks
  strictly taller than 2: the 3 m rock, in every preset; strictly taller than
  3: only the 4 m rock. The validity lab's four rows and one countercase are
  stated and the tile strings named. Every figure is called the lesson's or
  illustrative where it is.
- **The labs earn their place, each for a stated reason.** The validity lab
  (family 1, propositional logic) shows "the cost of the inference reading"
  and is honest that it "can only state the premise for me" and "cannot
  decide whether the cogito is an inference at all." The triangle lab
  (family 3) is used against itself, as above. The two `cases` tables carry
  opponents only and are read back honestly: "Each survives only the cases
  chosen for it"; "a third column would not be a mixture of the two." The
  river lab is the course's best illustration: the same seven parcels, three
  presets, and the `none` preset's two `none` tiles beside a full world tile,
  which is the chapter's sentence that "What is past or future for me is
  present in the world" made visible; and the lesson says where the model
  departs from the chapter (the boatman's future "in the landscape, not the
  water") three times, in body, mistake and `note`. The diagram lab reads
  Husserl's notation (`C, B′, A′′`) and says what the caption calls the
  verticals and what the lab reads them as. The ekstasis lab exists to show
  what no column holds, and the `one` preset is designed for that. The
  obstacle lab's two tiles make the chapter's "whether or not I have decided
  to climb them" a comparison the reader can run, and the lesson says the 2 m
  "is the lesson's illustrative figure".
- **Worked example, then faded guidance, then independent practice.** Every
  worked example is the first preset by hand; every `panel_intro` asks for a
  comparison before the press ("Compare the bare and major presets"; "Move
  the parallel with the vertex menu"; "Switch from the bank preset to the
  none preset"; "Compare the walk and one presets"; "Switch from the climb
  preset to the body preset"); every quiz asks the same act on a fresh
  instance.
- **The chapter's own best lines carry the summaries.** "To see is to see
  something"; "it is not because I think I am that I am certain of my
  existence"; "The construction is a gesture"; "The subject of geometry is a
  motor subject"; "One thinks, therefore one is"; "I am a field, an
  experience"; "Time presupposes a view of time"; "The objective world is too
  much of a plenum for there to be time"; "Time is not a line, but a network
  of intentionalities"; "as I see a pebble through the mass of water which
  moves over it"; "time is someone"; "What does not pass in time is the
  passing of time itself"; "I am not the creator of time any more than of my
  heart-beats"; "There is an autochthonous significance of the world"; "We
  choose our world and the world chooses us"; "by means of them". The budget
  was spent where the pilot said to spend it.
- **The cases are people and the respect is kept.** The hysterical patient,
  Scheler's girl, the day labourer "with no farm and no tools", the prisoner
  under torture are named as the book names them and never for effect; the
  prisoner lesson says in its `note` that the coding is "an interpretation,
  especially for the prisoner, whom the chapter does not set against
  determinism in so many words", which is exactly right: the chapter sets him
  against "a solitary and unsupported decision" (p. 527), and the determinism
  cell is the lesson's.
- **The cross-references are right.** Scheler's examples to pp. 441–442, the
  dots and the cube to p. 511 (the chapter's own back-reference to p. 263),
  Swann to pp. 493–494 with Sartre credited from the note, the Beauvoir
  charge to 1955 and the later book, the Russian peasants and Bonaparte left
  out as `not_covered` says. Chapters are cited by Part and number, lessons
  by title, the first course by its §B title.

## What it taught badly, or said wrongly

### Fidelity

- **`the-rock-and-the-project`, body (the first sentence of Freedom):** as
  above. Repaired.
- **`the-rock-and-the-project`, concepts ("in its own voice"):** as above.
  Repaired.
- **`the-triangle`, body (Gurwitsch; "at once"):** as above. Repaired.
- **`freedom-in-situation`, body ("as the book asks"):** as above. Repaired.
- **`the-tacit-cogito`, body:** "the chapter raises that conclusion itself on
  page 468" — the question is the last sentence of p. 467 and the answer the
  first of p. 468. Now "pages 467–468". Trivial, repaired.
- **`the-field-of-presence`, body:** the lesson says the caption "calls the
  vertical lines the successive shadings of one and the same present moment"
  and that "the lab reads the vertical through a present as what that present
  holds". Both are true as Smith prints the caption, and the lesson is right
  to say that its column is its own reading rather than claim the caption for
  it. Left; recorded because a reader with Husserl's diagram in another
  edition may find the obliques and verticals labelled the other way round.
- **`the-cogito-and-the-certainty-of-seeing`, body:** "Every sign was noticed,
  the impatience, the silence, the waiting" paraphrases p. 442 ("the quickened
  drive of my present towards my future… that emotion which left me
  speechless… my impatience for the arrival of the day we were to meet"). Fair
  and left.

### Prose that left the lab, or the reader, unexplained

- **Three unglossed terms in lesson 1 and one in lesson 3.** Repaired, as
  above.
- **`the-rock-and-the-project`, reading instruction.** Repaired, as above.
- **Every tile on every page is explained.** The diagram lab's `tiProtended`
  prints `none` on two presets and the lesson says why ("with a protention
  span of 0 there are none"); the obstacle lab's `scLevel` prints `3 m` on
  all three and the lesson says so twice; the validity lab's `show` menu
  changes no tile and the lesson does not mention it, which is right.

### Quiz

Every distractor on the thirty-two questions was argued for. One `why` was
wrong and is repaired (the exterior angle). Two others came close and were
left. Lesson 6's "Because a single column leaves out the future" (why the
`one` preset's column is not time): a column at D with no protention does
leave out the future, but the question asks "on the chapter's account", and
the chapter's reason is the cross-section, which the `why` says and then
closes with "Adding a protention would not supply that either." Lesson 1's
second question asks what Descartes said in the Second Replies, which is a
question about Descartes and not the chapter; the body paragraph on the
Replies supports it fully and the course `not_covered` admits "the lessons'
few references to them"; left, and see recommendations. Lesson 3's
expression-preset question ("What does that show?") is the best conceptual
item on the course, because its right answer is a sentence about what a
survivor count is and its three distractors are the three ways a reader
misreads a `cases` table.

### Speech

Every math run and every key line on the eight pages was read from
`data-say`. The key lines read well: "bare, p, so q, 4 rows, 1 counterexample";
"180 minus 130 equals 50"; "column at C, C, B prime, A prime prime"; "climb, 3
is greater than 2, so the 3-metre rock is an obstacle"; "determinism, y, n, n,
n, absorbs 1 of 4, fails 3". No key line begins with a three-letter word ("at
B" and "at C" are two letters and read as words), no step is split at its
spaces, and the preview lists no unspoken run. The prime notation reads as
"B prime", "A prime prime", "A prime prime prime", which is how a lecturer
would say it.

### Cross-references

Lessons are cited by title (“The Triangle”, “The Tacit Cogito”, “Time Is Not
in Things”, “The Field of Presence”, “Time as Subject”, “The Rock and the
Project”, “Freedom in Situation”, “Description, Not Explanation”), the book by
Part and chapter, the first course by its §B title. Every page reference in
the eight bodies was checked against the page: 429, 435, 436, 437, 439, 440,
441–442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 455, 457, 466,
468, 470, 473, 475, 477, 478, 479–480, 481–482, 483, 484, 485, 486, 488, 489,
490, 491, 492, 494, 496, 497, 501, 503, 505, 507, 509, 510, 511, 512, 513,
514, 515, 516, 518, 527, 528, 529 and 530 are all where the lessons say.

## Can a first-time reader of Part Three follow the eight lessons?

Yes, and the places they will slow down are the places Part Three's readers
slow down.

- **Lesson 1** is the course's densest and handles it by order: Descartes's
  doubt in one paragraph, the idealist six pages in one, then the passage a
  phrase at a time, then the p. 437 dilemma (now glossed), then the feelings
  pages with Scheler's girl as the everyday case. The `def` block on the
  cogito as an inference arrives before the lab, and the lab's three presets
  are each read back in a paragraph of their own. The paragraph on the Second
  Replies is the hardest history on the course and is honest that "Readers of
  Descartes still argue over which passage states his view."
- **Lesson 2** is the lightest to read because the proof is the reader's own
  from school, and the lesson uses that: "You were probably shown this
  proof." The Kant paragraph gives his view "at its strength" before the
  chapter's, and the `note` lists the three candidates (concept, pure
  intuition, the body's grasp) without a verdict.
- **Lesson 3** is where readers of The Cogito give up, in the pages on
  expression, and the lesson protects them by reading the Second Meditation
  case on p. 466 first, then going back for the account of speech, then the
  sleet, then the passage. The `cases` table gives the reader two named
  positions to hold while the tacit cogito is described in prose, and the
  Visible and the Invisible paragraph tells them, before anyone else does,
  that the author later doubted it.
- **Lesson 4** is the course's clearest, because the river is everyone's and
  the lab's three presets are the chapter's three moves. The Leibniz and
  Augustine paragraph is the one place a first-time reader may need the
  `def` block, and it is there.
- **Lesson 5** moves slowly through the diagram, as it should; the "Smith
  prints protections" sentence will save a reader with the book open a
  puzzled minute, and the pebble sentence is given in full where the chapter
  gives it.
- **Lesson 6** is the hardest chapter in the book, and the lesson says in its
  `concepts_intro` that it "draws on Husserl, Heidegger and Kant at once". It
  is kept followable by the lab: three columns the reader can count, and one
  sentence of what no column holds, repeated in body, worked `after`, mistake
  and `note` until it lands. The self-affection paragraph and the Heidegger
  paragraph each state the borrowed view before the chapter's use of it, and
  both say the reading is disputed.
- **Lesson 7** gives the reader the theory in its strongest form ("At its
  strength the view explains a great deal") and three concrete things it
  explains before the chapter answers, which is §F.4 done properly, and the
  valley path makes the rock the reader's before it is Sartre's.
- **Lesson 8** reads four cases in four paragraphs, codes them in a fifth,
  and then reads the conclusion, Hegel, the psychoanalyst and the last page in
  order. The Saint-Exupéry paragraph tells the reader who he was and what
  the passage is about, which the book does not, and the closing paragraph
  sends them back to the Preface. A first-time reader finishes the Subject
  knowing where they started.

## Repairs made in this pass

In `content/phenomenology/c7_cogito_time_freedom/part_a.py`:
`the-cogito-and-the-certainty-of-seeing`, the idealist paragraph
(*constitutes* glossed) and the p. 437 paragraph (*transcendental idealism*
and *absolute realism* glossed); `the-triangle`, the Wertheimer–Gurwitsch
sentences and the first quiz `why`; `the-tacit-cogito`, the page reference
for the half-truth sentence and the gloss of *positing thought*. In
`part_b.py`: `the-rock-and-the-project`, the reading instruction, the first
sentence of Freedom, and the absolute-freedom concept; `freedom-in-situation`,
the reading instruction and the closing sentence. In `__init__.py`: the lab
count in `how_to` and the rocks in `footer_lead`. No preset, `expect`, slug,
module, lab key, mode or view changed, and no §C entry needed correcting:
every instance the lessons carry is the one §C records, including the "As
authored" capacities and levels in the rock lesson, the `span` preset's A–E,
and the ash-tray conditional in the `seeing` preset.

`python3 scripts/preview_subject.py phenomenology --course
perception-cogito-time-and-freedom` reports OK: 9 pages rendered, every lab
executes and survives the sweep, every pinned figure on the eight pages
matches, no math run without a spoken form. `phen_quotes.py
c7_cogito_time_freedom` reports OK: no span outside the text, no cap exceeded.
`python3 -m unittest tests.test_site_invariants -k Lesson` runs 9 tests, OK.

## Remaining issues and recommendations (taste, not changed)

- **Lesson 1's Second Replies quiz item is about Descartes, not the
  chapter.** It is well supported by the body, but it is the only question on
  the course whose answer is in a book the course `not_covered` says is not
  read. A question on the chapter's reversal ("it is not because I think I am
  that I am certain of my existence", p. 445), which the lesson quotes and the
  first mistake turns on, would measure the lesson's own idea instead.
- **The diagram caption.** Lesson 5 is faithful to Smith's caption and honest
  about its own reading of the verticals. A clause saying that editions of
  Husserl's lectures label the lines differently, so the reader should follow
  the lesson's reading of the column rather than try to reconcile it with
  the caption, would save a careful reader some time. Not a correction.
- **Lesson 7's "three concrete things" the theory explains** are the
  lesson's selection (fatigue, deliberation after decision, relief at giving
  up), and all three are on pp. 506 and 513; the first is credited to Sartre
  via the note on p. 513 later in the lesson, but at its first appearance the
  reader may take it for the chapter's. "which the chapter itself credits to
  Sartre" at the first mention would close the gap.
- **The prisoner's determinism cell.** The `note` says the coding is an
  interpretation "especially for the prisoner"; the body gives the reason
  ("the pain that would cause him to talk does not"). A reader could argue
  that the chapter leaves determinism silent on him, which would make the
  cell `-` and the case a split rather than a both-fail; the "both fail" line
  in §C and the key line would then change. The lesson's reading is
  defensible (p. 512: pain and fatigue "can never be regarded as causes which
  'act' upon my liberty", a remark the chapter accepts before qualifying it)
  and is flagged; recorded so the
  authors know it is the one cell on the course that a second reader may
  code differently.
- **The obstacle lab prints `3 m` for the level tile in all three presets**,
  as §C records and the lesson says twice. A fourth preset with a general
  level of 3 m (no rock stands out) would let the reader see the level tile
  change, which the project tile does and the level tile never does. The
  `standard` and the quiz already vary the level, so nothing is untaught.
- **Lesson 6's second mistake title, "Hearing time as the subject as
  idealism"**, reads aloud as a run of small words; "Taking time as the
  subject for idealism" would read better. Harmless.

## Lessons for the authors' brief (confirming and extending the pilot's)

1. **A sentence in the opponent's pages is not thereby the opponent's.** The
   first sentence of Freedom is Merleau-Ponty's own and the theory begins one
   step later. Read the opponent's pages for the point at which the chapter
   stops agreeing, and say where it is.
2. **A reading boundary inside a paragraph must be named as one.** "To the
   end of the paragraph on fatigue" sent the reader a page too far; "to the
   sentences on sedimentation in the middle of page 513" does not.
3. **Say what a wrong answer is, exactly.** A `why` that names an angle must
   name the right one; a distractor that is "the exterior angle" at one
   vertex is a different error from the exterior angle at another.
4. **Count the labs in the course `how_to` from the lesson files, not from
   memory.** Seven for eight lessons went unnoticed through authoring and
   review.
5. **Gloss on first use even in an Advanced course.** The Subject promises a
   reader with no philosophy, and this course's four misses were all in the
   two Cogito lessons that use the most terms of art.
6. **Where the lab's reading of a diagram differs from the printed caption,
   say so once in a clause**, as lesson 5 does for Smith's "protections"; the
   same courtesy for the verticals would cost one sentence.
7. **Keep the closing of the last course as it is.** Ending on the book's own
   last line and sending the reader back to the first lesson of the first
   course, by title and with a reason, is the right shape for a Subject built
   on a book whose Preface was written last.

Final lines. Preview: `OK` (9 pages rendered; labcheck, every lab executes: 8
page(s) executed and swept, 0 failing; labcheck, pinned figures match: 8
page(s) executed and swept, 8 with pinned figures, 0 failing). Quotation
checker: `OK` (126, 114, 111, 107, 92, 114, 113, 130 quoted words; openings
60, 60, 38, 45, 48, 43, 46, 42).
