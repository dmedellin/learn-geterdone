# Pedagogy assessment — The Lived Body (Phenomenology of Perception, course 3)

Formed from the eight lesson dicts in `content/phenomenology/c3_lived_body/`
(`part_a.py`, the introduction to Part One, Chapter 1 in two lessons and
Chapter 2; `part_b.py`, Chapter 3 in four lessons; `__init__.py`, the course
dict) and the kit they render through (`scripts/mathpath/labs/phenkit.py`,
modes `perspective/faces`, `cases/table` twice, `schema/habitual`,
`perspective/own`, `schema/coordinates` twice, `schema/tool`), on branch
`feat/phenomenology-subject` before the Subject was wired into the site. The
design authority is `docs/phenomenology/PLAN.md` §0 (the one question and the
three families of lab), §B, the Course 3 entries in §C, §D as summarised in
`docs/phenomenology/kit-report.md`, §E (how a book in copyright is quoted), §F
(the voice, including the one modern aside §F.1 allows this course) and §G
(what is left out: the later status of Schneider's case). The brief in
`docs/phenomenology/AUTHORING.md`, with its two "Lessons from" sections, and
the Course 1 assessment (`docs/pedagogy/phenomenology-perception-what-
phenomenology-is.md`) are the standards the course is judged against.

Every lesson was read in full before anything was changed. The whole of
Part One's introduction and Chapters 1 to 3 (Smith pp. 77–170) was read
first, chapter by chapter, then each lesson's passage and the pages it reads
line by line. Every pinned tile was read off the rendered page with `node
scripts/labcheck.js --observe` (rendered through `scripts/preview_subject.py
phenomenology --course perception-the-lived-body`), every figure in prose,
worked lines and quiz `why`s was recomputed by hand, the `data-say` of every
worked line was read, and all the quoted spans on the eight pages were run
through the Subject's quotation checker (`phen_quotes.py`) and the opening
passages checked by eye against the page. Lessons, in course order:
`experience-and-objective-thought`, `the-phantom-limb`, `the-habitual-body`,
`the-permanence-of-ones-own-body`, `the-body-schema`,
`schneider-concrete-and-abstract-movement`, `the-intentional-arc`,
`habit-and-the-blind-mans-cane`. The course assumes Classical Prejudices and
school geometry and fractions, and is judged against that.

A second reviewer was reading the same course at the same time and changed
the same two files while this pass was under way. Five of the fidelity
findings below were repaired by that reviewer, in wording that agrees with
this assessment, between this pass finding them and reaching the file; they
are reported as findings and not claimed as repairs.

## Verdict

The course teaches Part One's first half and does it in the pilot's voice. A
reader who finishes it can list the faces a set of whole-number view
directions reaches on a box, take the union, find the smallest cover and say
what no set of views supplies; score two opponent accounts over a coded table
of reported observations, find the survivors and the split, and explain a
survivor that survives on a short table or by silence; compute which objects
lie within a habitual reach and a present reach and name what appeals only
to the first; convert a room position into the body's frame as the body
turns and walks and classify a target by the frame it is given in; and add a
cane to an arm and a feather to a head and compare the sum with a kerb or a
door. Those are the acts the eight `standard` fields name and the quizzes
measure. Every `mistakes[0]` is the §C misconception, refuted with the
lesson's own figure: the street reaches `2 of 6` and four views `5 of 6`,
never the house; the hybrid theory fails no row and is still "fundamentally
obscure"; the cup at 60 cm within a habitual 70 and outside a present 0; the
body's `3 of 6` that walking does not change; `ahead 2, left 1` as "such a
map"; the command target as the one that needs converting; the mosquito and
the ruler as one stimulus and two acts; `195 < 200` as the comparison the
woman does not make. All 53 pinned tile strings on the eight pages match the
lab, every figure in prose agrees with the lab or with a recomputation, and
the quotation checker reports every span in Smith's text with budgets of
106, 115, 114, 113, 106, 139, 133 and 132 words of 150 (openings 49, 58, 32,
45, 50, 53, 36 and 37 of 70).

Fidelity is high and the voice is right, and the defects found were local.
Three were of the kind the Course 1 review warned about, a lesson placing a
sentence of the book where it is not: the introduction's reservation ("But,
once more") was read as "the next sentence" after the passage when a
paragraph on time comes between; Chapter 2 was called "the shortest in Part
One" when Chapter 4 is shorter; and the symbolic function was given to
Cassirer at the page where the chapter's note credits Head. Two were
paraphrases a shade off the page (an emotion "one can neither face nor
leave"; Schneider lacking "the power of projection between them"). One was
a coding stated without its reason (why the physiological explanation fails
the posture of the injury). One was structural and the largest: all 31 quiz
items carried the correct answer in the first position, and the renderer
keeps source order, so a reader who noticed would never need to read an
option again. All are repaired. Nothing needs splitting, merging or
reordering, and no §C instance was changed.

## The voice, judged against §F

The pilot set the register; this course keeps it across eight lessons and
three chapters of very different texture, which is the harder test.

**What works, and should be copied:**

- **The passage first, then the chapter in its own order.** Every body opens
  with `<strong>Part One, Chapter n, p. m.</strong>`, the passage, the page,
  and the exact pages to read whole "in your own copy before going on", and
  the ranges are the ranges the lesson then reads: 77–83; 84 to the paragraph
  on 92 "that closes on the union of the psychic and the physiological"; the
  paragraph on 92 "that begins by returning to the problem of the phantom" to
  102; 103–111; 112 to the paragraph on 117 "that closes the argument about
  bodily and external space"; the sentence on 117 "that announces an example
  of morbid motility" to the paragraph on 138 "that closes on the basic
  disturbance"; the paragraph on 138 to the one on 164 "that ends on motility
  as the primary sphere of meaning"; the paragraph on 164 to 170. Each was
  checked and each stops where it says. This is the Course 1 lesson 2
  ("exact page range, no shorter") done eight times.
- **Reading forward to the passage, and past it.** Where the passage is a
  conclusion the lesson reads the argument up to it first: "The Phantom Limb"
  follows the reports that defeat each explanation and reaches the passage
  on p. 89 with "Now the passage"; "The Intentional Arc" scores the two
  accounts before reading the sentence that names the third term on
  p. 156–7; "Habit and the Blind Man's Cane" sets out the two accounts the
  chapter refuses before the feather. And where the passage is not the last
  word the lesson says so: "Now read on, because the passage is not the
  introduction's last word" (lesson 1). That is §F rule 1 and the Course 1
  rule about concessions together.
- **Scenes rationed to the chapter's own.** Two of eight lessons open with
  a scene, and both are the book's: "Rest your arm on the table. You would
  never say it is beside the ashtray" (Chapter 3's first sentence) and "You
  go through a doorway without measuring it against your shoulders" (p. 165).
  The other six open with the text or with the patient. §F.2's ceiling is
  half; the course is at a quarter.
- **The history of ideas as a story with people in it.** Leibniz, "for whom
  every substance reflects the whole universe from a point of view of its
  own"; Lhermitte, "the French neurologist whose book on the body image the
  chapter follows", 1939; Sartre's in-itself and for-itself "two years
  before"; Henry Head and the first definition of the body image; Köhler,
  Koffka and Wertheimer for "a form in the sense of Gestalt psychology";
  Gelb and Goldstein "working in Frankfurt, published on him from 1918";
  John Stuart Mill, "the Victorian logician's rules for finding a cause by
  what varies with what"; Bergson, "the French philosopher of duration and
  memory"; Jacques Chevalier's book on habit for the organist; Fischer for
  the intentional arc; Husserl's unpublished "I can". One sentence each,
  before the reply, and each was checked against the footnote it rests on.
- **Whose voice.** The course `how_to` tells the reader to "watch whose
  voice a sentence is in", and the lessons do: "Then an objection, in the
  voice of the physiologist the chapter is about to answer" (p. 87); "The
  chapter then answers an objection at its strongest. Surely, the objector
  says, figure and background already presuppose objective space" (p. 116);
  "Then the objection, at its strongest. Science looks beneath phenomena for
  causes, and here the cause seems known" (p. 129); "that is the
  intellectualist reading" (p. 139); "That is the mechanistic physiologist's
  view at strength" (`mistakes[0]`, lesson 7). Each opponent is stated with
  the fact on its side before the chapter answers, which is §F.4 done
  without fuss.
- **The patients are patients.** Schneider is "the man the book calls
  Schneider", a soldier, with the shell splinter where the book puts it
  (p. 145); the amputee is "the patient", "the person"; the chapter's word
  "cripple" (p. 94) is not repeated. Lesson 6 says in one sentence what §G
  requires, that the case was re-examined after the war and that modern
  reviews read it as a visual form agnosia, and that "the book's argument
  concerns the case as Gelb and Goldstein reported it, and so does this
  lesson"; lessons 2, 3 and 7 say the reports are Lhermitte's, Gelb and
  Goldstein's and their students', and that "the lab codes the reports, not
  the patients". Nothing is used for effect.
- **The one modern aside, in its one home, fair to both sides.** §F.1 gives
  this course Ramachandran's mirror box in "The Phantom Limb" and nowhere
  else, with two caveats, and the lesson gives both: "reviews of the trials
  judge the evidence mixed and mostly of low quality", and Ramachandran's
  own explanation "is close to the reading of the body schema as an image
  that Chapter 3 rejects". It ends "Nothing in the experiment settles which",
  and the `note` repeats that the dispute "is not settled here". It is in a
  late `p`, not the opening. No other lesson carries one.
- **Second person, warm, in `p` and `worked.intro` only.** "Lean on your
  desk with both hands and only the hands are stressed, the rest of you
  trailing behind like the tail of a comet"; "Your hand on the pipe does not
  consult ahead 2, left 1"; "You can know how to type without being able to
  say where the letters are". `steps`, `standard`, quiz items and tile text
  stay impersonal; no "let's", no first-person anecdote, no exclamation
  mark. No light remark is forced; the one near-joke, "the plainest sentence
  in the chapter" for "My head is presented to my sight only to the extent
  of my nose end", is the book's own plainness and not the lesson's wit.
- **The lab turned against itself where that is the point.** This is the
  course's best habit and the one the Subject's §0 asks for. "The Body
  Schema" says "the lab computes what the schema is not" and makes it a quiz
  item; "The Habitual Body" says the cup "does not appeal by being 60 cm away
  but by being a cup"; "Habit and the Blind Man's Cane" says the lab "does
  exactly the arithmetic the chapter says the habit does without" and the
  `panel_intro` says "It makes the comparison the chapter says a habit does
  not make"; "The Permanence of One's Own Body" counts the mirror's face as
  a view and then says "it is a count the chapter would not accept as a
  count of observations". Every `note` names what the lab cannot do and, for
  the two `cases` tables, that "Merleau-Ponty's own account is not in the
  table at all".
- **Family and model named.** Every `panel_intro` says what it computes and
  whose: "parallel projection, ordinary geometry that nothing in the chapter
  disputes"; "the lesson's coding of the chapter's reports"; "the lesson's
  model". The Course 1 recommendation that a family-1 label meaning
  "undisputed geometry" should say so is met in both perspective lessons
  and both schema lessons. The course `footer_lead` ends "None of them is
  the lived body, which is what Part One is about", the material clause in
  one line.
- **Pointing forward by title.** Every body ends by naming the next lesson's
  question by its title, and lesson 8 names the next course by its §B title,
  "The Expressive Body", and its first object.

**What to change in the courses that follow (and what was changed here):**

- **"The next sentence" must be the next sentence.** Lesson 1 said the
  passage's correction is taken back by "the next sentence", which "begins
  with 'But'". On p. 79 the next sentence is "What we have just said about
  the spatial perspective could equally be said about the temporal", and the
  reservation ("But, once more, my human gaze never posits more than one
  facet") opens a paragraph on p. 80 after a paragraph on time. The
  `read_intro`, a quiz question and its `why`, and `mistakes[1]` repeated the
  placement. Repaired by the second reviewer before this pass reached the
  file: the body now reads the paragraph on time in a sentence and then "The
  one after it begins with 'But, once more'". The §C entry for this lesson
  still says the text "at once adds, p. 80"; see recommendations.
- **A superlative about the book is a claim about the book.** "Chapter 2 is
  the shortest in Part One" (lesson 4, `concepts_intro`) is false: Chapter 2
  runs pp. 103–111 and Chapter 4 pp. 171–177. Repaired by the second
  reviewer to "the shortest of the three chapters this course reads", which
  is true (Chapter 1 is nineteen pages, Chapter 3 fifty-nine).
- **A footnote names whose term it is.** Lesson 7 wrote "a categorial
  attitude, Gelb and Goldstein's term, or a symbolic function, Cassirer's".
  On p. 139 the chapter's notes credit "categorial attitude" to Gelb and
  Goldstein (n. 50) and "symbolical function" to Head (n. 51); Cassirer
  enters on p. 143 ("There is no 'general symbolic faculty', says Cassirer")
  and p. 144 for the pathology of symbolic consciousness. §C's "the loss of
  the symbolic function — Cassirer" is a fair summary of pp. 143–5 and not
  of p. 139. Repaired by the second reviewer: "a phrase the chapter's note
  gives to Head and which Cassirer made the centre of a pathology of
  symbolic consciousness".
- **A paraphrase of a definition keeps both halves.** "An emotion is a
  situation one can neither face nor leave" (lesson 3) for p. 99's "a
  situation which one is not managing to face and from which, nevertheless,
  one does not want to escape": the second half is a wanting, not an
  inability. Repaired by the second reviewer to "cannot manage to face and
  does not want to escape".
- **Do not fuse two pages into one phrase.** "What Schneider lacks, it says,
  is neither motility nor thought, but the power of projection between
  them" (lesson 6, and quiz 4's answer). On p. 126–7 what lies "between
  movement as a third person process and thought as a representation of
  movement" is a motor project, a motor intentionality; "projection" is
  p. 128's name for "the normal function which makes abstract movement
  possible". Repaired by the second reviewer, in body, answer and `why`:
  "something between them, a motor project or motor intentionality; the
  normal power that makes abstract movement possible it calls projection".
- **Say why a cell is coded as it is when the page does not say it
  outright.** Lesson 2's table fails the physiological explanation on "it
  keeps the posture of the injury", but the body listed the posture among
  modern physiology's own facts against the peripheral theory (p. 88) and
  never said why a physiology of the brain fails it too. The reason is on
  the same page: "a central theory would get us no further if it added no
  more … than cerebral symptoms. For a collection of cerebral symptoms could
  not represent the relationships in consciousness which enter into the
  phenomenon." One clause added to the coding paragraph, in this pass.
- **Count what the text counts.** Lesson 5's `read_intro` promised "the
  three definitions of the body schema"; the chapter reports two
  (associationist, p. 113; Gestalt, p. 114) and then settles its own sense
  ("an attitude directed towards a certain existing or possible task"), which
  it does not call a definition. Reworded in this pass to "the two
  definitions of the body schema the chapter reports and the sense it
  settles on". The same Course 1 rule ("three consequences").
- **The word the chapter asks about is the word the lesson asks about.**
  Lesson 5 had the reply to the objection on p. 116 turn on "the word 'on'
  in 'the object is on the table'". The chapter's question is "what meaning
  could the word 'against' have for a subject not placed by his body face to
  face with the world?", and "on" comes next, with the observation that to
  say an object is on a table "I always mentally put myself either in the
  table or in the object". Reworded in this pass to carry both.
- **Never let the correct answer sit in one position.** All 31 quiz items in
  the course had `"c": 0`, and `scripts/mathpath/labs/common.py`'s
  `QUIZ_SCRIPT` renders options in source order, so the first option was
  always right. (The pilot was skewed the same way, 20 of 32, and Capital's
  courses are spread across all four positions.) Repaired in this pass: the
  correct option of lesson n's item i now sits at position (n + i) mod k, so
  each lesson's items spread across all positions; option texts, questions
  and `why`s are unchanged, which a script checked by parsing both files
  before and after. The brief should say it in one line: distribute the
  correct answer, because the page does not shuffle.

## What the course teaches well

- **One hard idea per lesson, and the book's own joints.** The split is
  §B's and it holds: the introduction's house; the phantom limb against two
  explanations; the chapter's own account (two layers); Chapter 2 whole;
  the body schema and "here"; Schneider's case and the visual explanation;
  the two classical accounts and the intentional arc; habit. Chapter 3's
  four lessons read it in order, and the long middle of the chapter on
  perception, stories and number (pp. 150–5) is summarised in one paragraph
  of lesson 7, which the course `not_covered` promises.
- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names a product: "count what a set of
  views reaches and say what no set supplies"; "score two explanations over
  the reports and say what the score leaves open"; "find what appeals only
  to the habit-body and say why the patient both knows and does not";
  "classify a task by how its target is given and say what the visual
  explanation misses". The five course `outcomes` are the same acts plus
  the reading's: state each opponent and the book's reply.
- **The arithmetic is right and attributed.** `0 3 4` has length 5 and
  reaches front 4/5 and above 3/5; `1 2 2` has length 3 and reaches front
  2/3, right 1/3, above 2/3; union 5 of 6, cover east and west. The cup at
  (2, 1): facing east ahead 2, left 1; facing north ahead 1, right 2; from
  (1, 0) ahead 1, left 1. The `turned` preset moves every target with the
  body, so the handkerchief at (1/4, 0) facing north is still ahead 0, right
  1/4 and the nose at (0, 1/10) still ahead 1/10, left 0, which is what the
  body says. `70 + 100 = 170`; `165 + 30 = 195`; `200 − 195 = 5`;
  `200 − 180 = 20`; `170 − 180 = −10`. The two `cases` tables give
  physiological absorbs 1, fails 2, silent 1 / psychological 3, 1, 0,
  survivors none, split the first three; and physiology 1, 2, 1 /
  intellectualism 1, 3, 0, survivors none, split the first two, with
  `thinking` surviving "by silence", which the body and a quiz item explain.
  Every figure is labelled "illustrative" where it is, and lesson 8's `note`
  says the book gives none "except the organist's hour".
- **The codings are the chapter's procedure, and the lesson says so.** Both
  `cases` lessons code "each account, made consistent", which is p. 141–2's
  argument ("Every 'physiological explanation' tends to become
  generalized… it is impossible also to set limits to consciousness"), and
  the one cell §C got wrong — analogies for intellectualism — was corrected
  by the author from p. 147 ("not that he is incapable of… subsuming them
  under some category, but on the contrary, that he can relate them only by
  a quite explicit subsumption") and recorded in §C. Checked against the
  page: right. The `nerves` and `memory` presets, each making one
  explanation survive, teach the thing a count can teach, that a survivor on
  a chosen table proves nothing, and the lesson says the chapter's
  procedure "is to refuse that choice".
- **The labs earn their place, each for a stated reason.** The faces lab
  (family 1, geometry) counts views so the reader can see that "a set of
  views, however well they agree, is still a set of views" (p. 80). The two
  `cases` tables (family 2) do what §0 says the chapter does, set out the
  observations and find the one each account cannot absorb. The three
  schema labs and the `own` perspective lab (family 3) each compute "the
  kind of representation the chapter says the body does not consult", and
  say so. The weakest is `schema/habitual`, whose arithmetic is a single
  comparison; the lesson knows it ("its arithmetic is simple on purpose",
  "The model is a crude one") and spends the lesson on the text instead,
  which is the right call for Chapter 1's second half.
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first or fullest preset by hand; every `panel_intro` asks
  for a comparison before the press ("Compare the all preset with the nerves
  preset"; "Turn the body and walk it, and watch which tile moves"); every
  quiz asks the same act on a fresh instance (the cup facing north; a wall
  at 180 cm) or the reading's own question with the named errors as
  distractors ("Because Schneider's sight was normal"; "That habits are
  innate"; "Because the hybrid ignores the cut nerves").
- **Terms glossed on first use.** *Partes extra partes* ("its parts outside
  one another"), *anosognosia* ("the failure or refusal to recognise a
  disability"), *allocheiria* ("a touch on one hand is felt on the other"),
  *presumptive* ("a confidence that runs ahead of what has been confirmed"),
  *categorial attitude*, *Greifen* and *Zeigen*, *incorporation*, and Smith's
  "body image" for *schéma corporel*, said once where it is introduced, as
  §E.2 asks, and again at p. 164 where Smith prints "corporeal schema".
- **The cross-references are right.** The house seen from nowhere is cited
  to Leibniz as the text does; the insect to *The Structure of Behaviour*;
  the nose to Goldstein's cerebellar case (p. 119 n. 12); the organist to
  Chevalier; Bergson's "fossilized residue" to the chapter's note (p. 165
  n. 105); the late work's reversibility kept out of this book by the
  `note`, as §F.4 requires. Lessons are cited by title, chapters by Part and
  number.

## What it taught badly, or said wrongly

### Fidelity

- **`experience-and-objective-thought`, body, `read_intro`, quiz 3,
  `mistakes[1]` ("the next sentence… begins with 'But'"):** as above. Found
  in this pass; repaired by the second reviewer. Checked against the page:
  faithful.
- **`the-permanence-of-ones-own-body`, `concepts_intro` ("the shortest in
  Part One"):** as above. Repaired by the second reviewer.
- **`the-intentional-arc`, body ("a symbolic function, Cassirer's"):** as
  above. Repaired by the second reviewer.
- **`the-habitual-body`, body ("neither face nor leave"):** as above.
  Repaired by the second reviewer.
- **`schneider-concrete-and-abstract-movement`, body and quiz 4 ("the power
  of projection between them"):** as above. Repaired by the second reviewer.
- **`the-body-schema`, `read_intro` ("three definitions") and body ("the
  word 'on'"):** as above. Repaired in this pass.
- **`the-phantom-limb`, body (the posture cell):** as above. Repaired in
  this pass.
- **`the-phantom-limb`, `concepts` ("Being-in-the-world: Heidegger's
  phrase"):** true and standard (the Preface names Heidegger's
  *In-der-Welt-Sein*), but Chapter 1 does not name Heidegger where it takes
  the phrase up (p. 90); the only Heidegger on these pages is the
  translator's note on *ek-stase*, p. 81. Left; recorded so the authors know
  the attribution is the lesson's.
- **`the-intentional-arc`, body ("Goldstein's student Hochheimer"):** the
  chapter says only that Hochheimer's study was "published under their
  editorship" (p. 130 n. 36). "Student" is the lesson's word. Left.
- **`schneider-concrete-and-abstract-movement`, body ("wounded in 1915",
  "published on him from 1918"):** both are §F.3's facts and not the
  book's; the lesson attributes only the splinter to the book, which is
  right. Left.

### Prose that left the lab, or the reader, unexplained

Nothing. Every tile each view prints is in a body paragraph with what it is
a figure of, including the dash the `peConsistent` tile prints when no view
reports, the `no object has a given frame` tile in "The Body Schema", and
the `no opening` tile on the `hand` and `cane` presets. Every preset id
appears in prose with its figure.

### Quiz

Every distractor on the 31 items was argued for. The one that came closest
was lesson 4's "That it is always perceived" as what makes an object an
object: a reader who remembers that the chapter opens with classical
psychology's mark of the body, "constantly perceived", could reach for it,
but the question asks what makes an *object* an object, and the chapter's
sentence is that an object "can be moved away from me, and ultimately
disappear from my field of vision" (p. 103); the distractor is the body's
mark, which the lesson has just contrasted, and the `why` says so. Lesson
7's analogies item is the best conceptual item on the course: its
distractor "He cannot subsume anything under a category" is exactly the
intellectualist's expectation the page reverses. The positional defect is
described above and repaired.

### Speech

Every worked line was read from `data-say`. "own body, front, right, left"
and "the car, 200 minus 180 equals 20 cm, clears" read as words, not
letters; "60 ≤ 70" reads as "60 is at most 70"; the fractions read "ahead 1
over 10, left 0". No step is split at its spaces, and the preview lists no
unspoken run.

### Cross-references

Lessons are cited by title (“The Phantom Limb”, “The Habitual Body”, “The
Permanence of One's Own Body”, “The Body Schema”, “Schneider: Concrete and
Abstract Movement”, “The Intentional Arc”, “Habit and the Blind Man's
Cane”, each as the lesson carries it); the book by Part, chapter and page;
the next course by its §B title. No lesson is cited by number.

## Can a first-time reader of Part One follow the eight lessons?

Yes, and the places they will slow down are the places Part One's readers
slow down.

- **Lesson 1** is the gentlest entry to objective thought a reader could
  have: the house, the film close-up for horizons, the lamp for "every
  object is the mirror of all others", and the passage only then. The
  paragraph on "Objective thought is what happens next" is the densest and
  is kept to the text's own sentences (a host of eyes; my eyes as bits of
  matter). A first-time reader will not notice that the lab's fractions are
  foreshortening and not appearance unless told, and the lesson tells them
  three times, in body, `mistakes[2]` and `note`.
- **Lesson 2** carries the course's one piece of philosophy of mind (two
  orders with no common ground), and does it with the chapter's own
  comparison, two components and a resultant. The `cases` table makes the
  argument's shape visible before the passage. The mirror-box paragraph is
  the one place a reader with no philosophy meets a name they know, and it
  is handled as §F.1 asks.
- **Lesson 3** is where Chapter 1 is hardest (repression, the former
  present, the cut nerves "in the perspective of being in the world"), and
  the lesson protects the reader with the friend who has died, the piano
  still to be played, and the paradox sentence quoted whole. The lab is
  small and the lesson says so.
- **Lesson 4** reads four descriptions and a question, and the box model
  gives a reader something to count while the chapter argues that counting
  is not the point; the `note` is honest that the box "leaves out what
  matters most".
- **Lesson 5** gives the comet and the pipe before "here", and the
  coordinate lab is the right kind of wrong: a reader who has just
  computed "ahead 2, left 1" is in the best position to see what the chapter
  means by saying the body does not.
- **Lesson 6** is the course's longest reading (pp. 117–138) and the lesson
  is longest too. It is carried by the case's own details (the handkerchief,
  the salute, the imaginary mirror, the leather "to be cut up") and by
  stating the visual explanation at full strength before the three-stage
  reply. The Mill paragraph is the hardest history on the course and is
  four sentences.
- **Lesson 7** is the hardest lesson and the chapter's hardest stretch, and
  the lesson's order is the right one for a first reader: the intellectualist
  reading, the mosquito and the ruler, the table, the analogies, then "less
  false than abstract", the fountain pen, and only then the intentional arc.
  A reader will still find "each account, made consistent, spreads" abstract
  until the mosquito sentence, which is why the lesson quotes it whole.
- **Lesson 8** is the lightest and the most quoted in the secondary
  literature, and the lesson spends its quotation budget on the right lines
  (motor grasping of a motor significance; the stick not "a middle term";
  knowledge in the hands; the organist's hour). The last paragraph, on a new
  meaning of "meaning", is the chapter's summary of Part One so far and the
  lesson reads it as such.

## Repairs made in this pass

In `content/phenomenology/c3_lived_body/part_a.py`: `the-phantom-limb`, the
coding paragraph (why the posture cell is `n` for physiology, from p. 88).
In `part_b.py`: `the-body-schema`, `read_intro` (two definitions and the
sense settled on) and the objection paragraph ("against", then "on"). In
both files: every quiz item's options reordered so the correct answer is
spread across positions, with `"c"` updated, by a script that parsed both
files before and after and checked that every question, option set,
correct option text and `why` is unchanged. Nothing in `__init__.py`. No
preset, `expect`, slug, module, lab key, mode or view changed, and no §C
instance needed correcting: every instance the lessons carry is the one §C
records, including the "As authored" notes for the house, the `own` views,
the `turned` preset and the analogies cell.

The second reviewer's concurrent changes (the "But, once more" paragraph
and its `read_intro`, quiz and mistake; "shortest of the three chapters
this course reads"; "cannot manage to face and does not want to escape";
the motor project and projection sentence and its quiz answer; the Head and
Cassirer clause; and smaller rewordings) were read after they landed and
are consistent with the text and with this assessment; none is claimed
here.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and
§C list them. `python3 scripts/preview_subject.py phenomenology --course
perception-the-lived-body` reports OK: 9 pages, every lab executes and
survives the sweep, every pinned figure on the eight pages matches, no math
run without a spoken form. `phen_quotes.py c3_lived_body` reports OK: no
span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **§C's lesson 1 entry says the text "at once adds, p. 80" that a human
  gaze posits one facet at a time.** The addition comes after a paragraph on
  the temporal perspective (p. 79–80). The lesson is now right and the §C
  entry is a sentence behind it; the author should correct the entry in the
  same way ("after a paragraph on time, p. 80"). PLAN.md is outside this
  assessment's files.
- **"Heidegger's phrase" in lesson 2's `concepts`** and **"Goldstein's
  student Hochheimer" in lesson 7** are the lessons' attributions, not the
  chapter's. A clause ("the phrase the Preface takes from Heidegger";
  "Hochheimer, whose study appeared under Gelb and Goldstein's editorship")
  would mark whose words they are.
- **Lesson 8 says Smith's "corporeal schema" (p. 164) and "body image" are
  "the same French term".** This pass could not check the French; the claim
  is standard (*schéma corporel* throughout) and is presented in the
  lesson's voice. If an author with the French confirms it, a "(checked)"
  in the lesson's comment would close it.
- **The "three stages" of the chapter's reply to the visual explanation**
  (lesson 6: "The chapter's reply comes in stages") is the lesson's
  structure, not a numbered list in the text; the text's own numbering is
  the twofold objection on p. 132–3 (1 and 2, then (i) and (ii)). The
  lesson does not say "three", so no reader will go looking, but a sentence
  tying the stages to the chapter's own 1, 2, (i), (ii) would let a reader
  follow in the book.
- **`schema/habitual` is a one-comparison lab.** It is honest and the
  lesson is strong without it, but the courses that follow should not take
  it as a licence: where a chapter gives the lab nothing to compute but a
  single inequality, the lesson's prose has to carry the lesson, as this one
  does.
- **The quiz positions in Course 1** (20 of 32 at position 0) were not
  touched here, since that course is outside this assessment's files, and
  the same one-line fix would serve it.

## Lessons for the remaining authors

1. **"The next sentence", "the next paragraph", "right after" are claims
   about the page.** Open the book at the passage and read on before
   writing them; the one fidelity error of weight in this course was a
   paragraph on time that a lesson skipped over.
2. **A superlative about the book is a fact to check.** "The shortest
   chapter", "the most quoted line", "the only place the book names X" each
   need a page count or a grep.
3. **Footnotes name whose term it is.** The chapter credits categorial
   attitude, symbolic function, representative function and projection to
   four different sources in four notes on one page; a lesson that gives
   them to one philosopher is wrong on that page even when it is right
   about the chapter.
4. **When a table codes a cell the body has not argued, add the clause
   that argues it**, from the page. A reviewer checks every cell, and so
   will a reader.
5. **Spread the correct answer.** The page keeps source order. Lesson n,
   item i at position (n + i) mod k is a rule that needs no thought.
6. **Keep the pilot's habits that this course kept**: exact page ranges
   that stop where the lesson stops; the opponent at strength before the
   reply; the patient named as the book names them, with §G's sentence; the
   lab's model named and the lab turned against itself where the chapter's
   point is that the figure is not the experience; the one modern aside in
   its one home with both caveats.
7. **Keep the quotation checker and the preview green after every edit, and
   re-read before each edit when another agent is in the file.** Five of
   this pass's thirteen edits failed on first try because the second
   reviewer had just written the same file; all five turned out to be fixes
   of the same findings.

Final lines. Preview: `OK` (9 pages rendered; labcheck, every lab executes:
8 page(s) executed and swept, 0 failing; labcheck, pinned figures match: 8
page(s) executed and swept, 8 with pinned figures, 0 failing). Quotation
checker: `OK` (106, 115, 114, 113, 106, 139, 133, 132 quoted words;
openings 49, 58, 32, 45, 50, 53, 36, 37).
