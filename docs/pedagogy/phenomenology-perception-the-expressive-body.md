# Pedagogy assessment — The Expressive Body (Phenomenology of Perception, course 4)

Formed from the four lesson dicts in `content/phenomenology/c4_expressive_body/`
(`part_a.py`, one lesson for Chapter 4, one for Chapter 5, two for Chapter 6;
`__init__.py`, the course dict) and the kit they render through
(`scripts/mathpath/labs/phenkit.py`, modes `variation/core`, `cases/table`,
`sorting/sort`, `variation/core`), on branch `feat/phenomenology-subject`
before the Subject was wired into the site. The design authority is
`docs/phenomenology/PLAN.md` §0 (the one question and the three families of
lab), §B, the Course 4 entries in §C, §D as summarised in
`docs/phenomenology/kit-report.md`, §E (how a book in copyright is quoted) and
§F (the voice), with `docs/phenomenology/AUTHORING.md` and its three "Lessons
from" sections, which this course is the first to be written under in full.
The Course 1 assessment (`phenomenology-perception-what-phenomenology-is.md`)
is the model for shape and depth.

Every lesson was read in full before anything was changed. The three chapters
were read whole first, Smith pp. 171–232, footnotes included (the long
footnote on historical materialism, pp. 198–201, among them), then each
lesson's passage and the pages it reads line by line. Every pinned tile was
read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py phenomenology --course
perception-the-expressive-body`), every chain, core and record in prose,
worked lines and quiz `why`s was recomputed by hand, every `data-say` on the
four pages was read, and all quoted spans were run through the Subject's
quotation checker (`phen_quotes.py`) and the opening passages checked by eye
against the page. Lessons, in course order: `the-body-as-a-work-of-art`,
`the-body-as-a-sexed-being`, `speech-as-gesture`,
`the-spoken-word-and-thought`. The course assumes The Lived Body and no
philosophy beyond it, and is judged against that.

A second reviewer was reading the same course at the same time and made
changes to the same file while this pass was under way (chiefly to the lab
paragraphs of `the-body-as-a-sexed-being`). Those changes were re-read after
they landed, are noted where they bear on a finding, and are not claimed here.

## Verdict

The course teaches its three chapters and is fit to publish. A reader who
finishes it can intersect a coded set of ways of making one movement to find
the core, list what varies and name what an excluded variant lacks, and say
why the chapter will not let the core stand for the body's unity; count two
classical accounts against the lesson's coding of Schneider and of
Binswanger's patient, read off each record, the survivors and the split, and
state in prose the account the chapter gives instead; compute a sort by hue
name beside a chain of nearest resemblances over colour samples and name the
sample where the chain leaves the category; and look for the bodily sign
common to three expressions of anger, find none, and say what an empty core
does and does not show. Those are the acts the four `standard` fields name
and the quizzes measure; no objective is "understand X". The `mistakes[0]` of
every lesson is the §C misconception, each refuted with the lesson's own
figure: the telephone's core `hand-at-the-telephone` with every posture on
the list of what varies; the `all` table's `none` survivors with each account
failing Schneider; the `samples` chain leaving red at `pale green` on its
first step; the `anger` core `none`. All 12 presets' pinned strings match the
lab, and every figure in prose agrees with the lab or with a recomputation.

Fidelity is high, and this is the course where it is hardest, because
Chapters 5 and 6 are the book's longest stretches of ventriloquism:
Merleau-Ponty states the mosaic theory of affectivity for a page, the
verbal-image theory for a page, Gelb and Goldstein's categorial reading for a
page and the natural-sign objection for a page before he answers any of them.
The lessons name the voice every time ("Then he states the usual view";
"giving the view it is about to reject"; "the chapter first states it as if
it were its own, answering it only later"; "then it states the objection at
length"), and every quoted span is in Smith character for character (the
checker reports OK; the quotation budget is 106, 121, 111 and 114 words of
150, the openings 51, 60, 29 and 31 of 70). Every "the chapter says" was
traced to a page. Merleau-Ponty is presented, not endorsed: the mechanist, the
intellectualist, Freud, Gelb and Goldstein, Scheler, Darwin, Bergson and
Descartes each get their position before the reply, and the lesson on
sexuality says twice that the chapter's Freud may be a reading of Freud.
Every `note` names what the lab cannot settle, and every `panel_intro` names
the family and says the coding or the rule is the lesson's.

The defects found were local and are repaired: one quiz distractor and its
`why` that misplaced the chapter's "second order object" (the stick, where
the text says the external thing); a reading of the aphasia pages that
hardened "he never adopts any [principle of classification]" into "follows no
rule at all", which says more than the text and sits oddly beside the
chapter's own remark that the patient's experience is probably one of
immediate relationships; and three unglossed words in a course that promises
to assume no philosophy (*aphonia*, *phonemes*, and Casanova unnamed as a
person). Nothing needs splitting, merging or reordering, and no §C instance
is missing from the pages.

## The voice, judged against §F

**What works, and should be copied:**

- **The passage first, then the chapter in its own order.** Every body opens
  with `<strong>Part One, Chapter n, p. …</strong>` and the passage, names the
  page, and gives the exact range to read in the reader's own copy before
  going on: "pages 171 to 177"; "pages 178 to 201, the long footnote at its
  end included"; "from its first page, 202, to the end of the paragraph on
  page 214, and then pages 221 to 225"; "from page 214 … to the end of the
  chapter on page 232". Each range is the range the lesson then reads, no
  shorter, which is the Course 1 lesson applied. Then the lesson goes back to
  the chapter's first page and walks forward, returning to the passage where
  the chapter reaches it ("Go back to the passage. The body is comparable to
  a work of art in exactly that sense, and the next sentence says what it
  rules out"; "Now the passage. The reason that keeps existence from being
  reduced to sexuality…"; "That is the passage's second sentence: speech
  accomplishes thought").
- **The opponent read whole before the refusal.** Lesson 3 gives the
  verbal-image theory its evidence ("Aphasia … can strike spoken language and
  spare written language, or the reverse … so it seemed to be built of
  independent pieces") and Gelb and Goldstein's reading its strength ("one
  deficit explains both the lost names and the failed sort") before
  Merleau-Ponty's kinship argument. Lesson 4 states the natural-sign
  objection at the chapter's length, keyboard and all, and gives a `def`
  block to the classical division before either reply. Lesson 2 states the
  mosaic theory and its own test ("any sexual incapacity ought to be either a
  loss of certain representations or a weakening of the capacity for
  pleasure") before Schneider. That is §F.4 done as the lectures do it.
- **Scenes rationed.** One of four lessons opens with a scene of the reader's
  own (two people at a café table you cannot hear), and it reaches the
  chapter's question in four sentences. The other three open with the text,
  and lesson 1's telephone is introduced as "a scene from the book". That is
  under the half §F.2 allows.
- **The history of ideas as a story with people in it.** Gelb "a
  psychologist" and Goldstein "a neurologist, who studied brain-injured
  soldiers together in Frankfurt during and after the First World War";
  Binswanger "a Swiss psychiatrist, a friend and correspondent of Freud's, who
  directed a sanatorium at Kreuzlingen and was then turning Heidegger's
  analysis of existence into a psychiatry"; Scheler, who "in the 1910s and
  1920s wrote on sympathy and on how we know other minds"; Koffka "one of the
  founders of Gestalt psychology"; Steinfeld as "a third author" on
  Schneider; Darwin "the naturalist who wrote on the expression of the
  emotions"; Descartes's letter "of 1643 to Princess Elisabeth of Bohemia".
  One sentence each, and the case is real before the reply.
- **Whose voice, every time.** Beyond the quotations, the paraphrases are
  attributed: "the chapter says, giving the view it is about to reject"
  (the stick); "A strictly Freudian reading would refer it to the oral
  phase"; "the chapter first states it as if it were its own" (the
  categorial reading); "This, the chapter says, is what is commonly expressed
  by calling gesture a natural sign"; "with a probably" for the chapter's
  conjecture about the original form of a language. Lesson 2 says of Freud
  that "whether this is Freud or a reading of him is disputed", in `p` and
  again in `mistakes[2]`, and the course `how_to` tells the reader to "watch
  whose voice a sentence is in". The one place a paraphrase overstated the
  text is recorded below and repaired.
- **The cases are people.** Schneider is "the soldier wounded in 1915 by
  splinters to the back of the head", and both Schneider lessons say in a
  sentence that the argument concerns the case as reported and that the
  reports were later questioned. The girl is called what the book calls her,
  and the lesson says "The reports themselves are Binswanger's; the lab codes
  the reports, not the patient", once in `p` and again in `note`. Nothing is
  done for effect.
- **Second person in `p` and `worked.intro`, impersonal elsewhere.** "You are
  sitting at a table and want to reach the telephone"; "You cannot see your
  foot inside your shoe, and yet, the chapter says, as you contract it you
  can see it"; "When you look at something in the half-light and say *it's a
  brush*". No "let's", no "dive in", no first-person anecdote, no exclamation
  mark on the course. The one light remark is the book's own: "the
  prohibition she cannot, literally, swallow".
- **The lab turned on itself where that is the point.** Lesson 1's "Notice
  what the lab has done, though" paragraph says that an invariant across
  variants "is very nearly what the passage says the body is not: the law for
  a certain number of covariant terms", and that the core "is a list drawn up
  by someone looking at four signatures from outside, the position the chapter
  says I am never in towards my own body". That is the right use of a lab in
  this Subject and should be the model for every family-2 lesson that
  follows: the count is exact and says something negative and true (no part
  is shared), and the lesson says what the count cannot be.
- **Family and model named.** Every `panel_intro` says "This lab counts the
  lesson's coding" or "computes the lesson's model, not the book's and not
  Gelb and Goldstein's", and names the rule ("a chain that always takes the
  sample nearest the last, by a rule printed in the banner"). The course
  `footer_lead` ends "None of the figures is an experience, which is what
  these chapters are about", the Subject's material clause in one line.
- **Pointing forward by title.** Every body ends by naming the next lesson's
  question and title; lesson 4 ends with the next course by its §B title,
  Sensing and Space, and Part Two's title as Smith prints it.
- **No modern aside.** §F.1 gives Course 4 none, and it has none.

**What to change in the courses that follow (and what was changed here):**

- **A clause in a quiz `why` must be as faithful as the body.** Lesson 1's
  body reads the stick passage correctly ("reads the pressures as signs of
  the stick and the stick as a sign of the object"), but quiz 3's distractor
  called the stick "a second-order object built up from sensations in the
  hand" and the `why` repeated it. On p. 176 the stick is built up from the
  pressures and "the latter then mediate a second order object, the external
  thing". The distractor was wrong either way, so the item had one answer;
  but a reader who checked the `why` against the page would have found the
  lesson misreporting it. Repaired: the distractor and the `why` now place
  the second-order object where the text does.
- **"The chapter's last word" must be the chapter's words.** Lesson 3 three
  times rendered p. 223's "in reality he never adopts any" (principle of
  classification) as "the patient follows no rule at all" / "the chapter's
  last word on the patients". The text's correction is narrower, and the same
  page says the patient's experience is "probably" one of immediate
  relationships, which is not nothing. Repaired in the body, the worked
  `after` and `mistakes[2]`: "the chapter's corrected description … is that
  they adopt no principle of classification at all". The habit for the brief:
  when the lesson summarises a correction the chapter makes to itself, quote
  or paraphrase the correction's own object.
- **Gloss the clinical and the proper names, not only the philosophy.**
  *Aphonia* was a preset id and appeared in the body without the word "loss
  of voice" beside it; *phonemes* appeared bare; Casanova appeared as a name
  a reader with no eighteenth century might not place. All three now carry a
  gloss of a few words in the sentence. The course glosses its philosophy
  well (*partes extra partes*, *cogitatio/cogitatum*, *pithiatism*,
  *co-existence*, *interfusion*, *anarthria*, *productive imagination*, the
  *categorial attitude*), and the rule should be read to cover the medicine
  and the history too.

## What the course teaches well

- **The objectives are acts, and the drill measures them.** Every `standard`
  begins "Finish when you can…" and names the product: the core, what varies
  and "what each excluded variant lacks"; each account's record, "the
  survivors and the split", with "the page on which the chapter rejects each
  account at each case"; the categorical sort, the chain and "the sample
  where they part"; the common sign and "what an expression marked not of the
  emotion lacks". The five course `outcomes` are the same four acts plus the
  reading's: state each chapter's opponents and its reply.
- **One hard idea per lesson, and the chapters' own joints.** Chapter 4 is
  the shortest in the book (seven pages, as the lesson says; measured against
  every chapter heading in the extraction) and gets one lesson that stays with
  the comparison to a work of art and the stick. Chapter 5 gets one lesson
  that carries Schneider, Freud, the girl and interfusion and summarises the
  footnote on historical materialism in one paragraph, which the course
  `not_covered` says it will. Chapter 6 is split where the book turns from
  the word to the gesture (p. 214, "The spoken word is a gesture, and its
  meaning, a world"), and the split is honest about the chapter's own return
  to aphasia on pp. 221–225: lesson 3 reads those pages because they correct
  its case, and lesson 4 tells the reader they "were read in the last
  lesson". The reader is never asked to hold two chapters' ideas at once.
- **The misconceptions are refuted with the specific figure.** "The telephone
  preset makes the first point in the lab's terms: the core is
  `hand-at-the-telephone`, and every posture varies" (lesson 1). "In the lab,
  neither classical account survives the three observations, and the
  chapter's account is stated in prose rather than scored" (lesson 2). "The
  `samples` preset's categorical sort uses the hue names as its rule; nothing
  in the patient's behaviour, as reported, works like that" (lesson 3). "The
  `anger` preset's empty core is the passage's case in the lab's terms"
  (lesson 4). `mistakes[1]` and `[2]` are each a real misreading a first
  reader makes: hearing the work-of-art comparison as a claim about beauty;
  reading the lost voice as a message she means to send; taking the chain's
  rule for what the patient does; taking the empty core to show that gestures
  have no meaning.
- **The arithmetic is right, and each figure is attributed to its model.**
  The `samples` chain from pale red at 9: pale green costs `|9 − 8| + 1 = 2`
  against mid red's `3`, so pale green; from pale green at 8, mid red
  `2 + 1 = 3` ties mid green `3` and the tie goes to the first listed; then
  mid green (`1 + 1 = 2` against dark red's `3`), dark red (`2 + 1 = 3`
  against brown's `4`), brown (`1 + 1 = 2` against dark brown's `3`), dark
  brown. The `close` chain from dark red at 2 goes to brown at cost `0 + 1`
  before light red at `7`, then light red (`7`) before pale red (`8`), then
  pale red. The `ribbons` chain reaches pale blue at 8 and takes pale green
  (`0 + 1`) over pale pink (`1 + 1`), which is the pale-green-after-pale-blue
  of p. 204 in the lesson's figures. The `all` table gives each account
  `1 of 3` absorbed and `2` failed, the split is both of the girl's
  observations, and the quiz's fourth observation coded y/y leaves the
  failures at 2. The grief quiz's core is `tears`; the door quiz's is
  `door-opens`; the dark-green quiz's chain goes to dark blue at cost `2`
  before pale green at `7`. Every lesson says the lightness figures, the
  chain's rule and every cell are the lesson's.
- **The labs earn their place, each for a stated reason.** Lesson 1
  (`variation`, family 2) computes an invariant and then says, in the body,
  `steps[4]`, `mistakes[1]` and `note`, that an invariant is what the chapter
  says the body's unity is not; its `telephone` preset is the chapter's own
  example and is labelled so, and the signature set is labelled the lesson's
  in `label`, `p` and `note`. Lesson 2 (`cases`, family 2) is the Subject's
  first `cases` table on a published course, and it does what §0 asks: the
  accounts are the opponents' only, Merleau-Ponty's account "is not a column,
  because a column the lesson coded for it would come out clean by
  construction", and each cell is given its page. The second reviewer's
  paragraph that makes the mapping explicit (p. 187's pair is paralysis and
  simulation; the lesson reads paralysis as what a bodily mechanism would
  make of the symptom and a deliberate silence as what a representing
  consciousness would, "the dilemma p. 180 already named"; "the mapping is
  the lesson's") is exactly the honesty §0 requires of a coded table, and is
  the sentence this course should hand on to Course 6's hallucination
  tables. Lesson 3 (`sorting`, family 3) computes "the lesson's model of a
  sort by concrete resemblance", a model nobody in the book states, and uses
  it only to show *where* two kinds of sort come apart, which is the one
  thing a model like that can show; the `lightness` preset, where the two
  sorts agree and the third tile prints `none`, is a well-designed control.
  Lesson 4 (`variation`) asks a yes-or-no question the chapter's own sentence
  poses (is there a sign anatomy ties to anger?) and the `smile` preset asks
  it the other way round (does the sign decide the emotion?), with `vrBreak`
  printing `smile in pleasure lacks none of the core`.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` asks for a comparison
  before the press ("Compare the signature and muscles presets"; "Compare the
  schneider and aphonia presets"; "Compare the ribbons and lightness
  presets"; "Compare the anger and smile presets"); every quiz asks the same
  act on a fresh instance (three ways of opening a door; a fourth observation
  coded y/y; three greens and a blue; three expressions of grief). The
  distractors are the named errors (`push-bar, door-opens` for a reader who
  intersects only the first two; "Each absorbs 2 of 4 and fails 1" for a
  reader who thinks a y removes a failure; "none: it never leaves green" for
  a reader who sorts by hue first).
- **The book's own images are the book's.** The telephone, the foot in the
  shoe, the photograph and the filmed walk, the cube's law, Leibniz's
  effective law, Cézanne's pictures, the poem and the cry, the stick, Koffka's
  child; the mosaic, the occipital wound, the sexual schema, Casanova, the
  stripes and the house number, the sleeper's posture, the name on the tip of
  the tongue, "no God could
  sound our hearts"; the electric lamp, the patient's *no*, the blue ribbons,
  the brush in the half-light, the writers who begin a book, the words behind
  my back, the viscosity of the heap; the carpet, the dog and the praying
  mantis, the fireplace, the caress, the keyboard, *nuit* and *lumière*, the
  kiss and Japan, paternity, Darwin's brows, the sky is black, the fortune
  already made, Cézanne's blue and brown touches, Descartes's letter. All
  were checked against the page and are where the lessons say they are, in
  Smith's words where quoted and in fair paraphrase where not.
- **The cross-references are right.** The Lived Body is named for the body
  schema (with Smith's "body image" given once, in lesson 1 and in the course
  `how_to`), for Schneider, the intentional arc and the stick; Chapter 3's
  "representation of movement" is recalled where p. 209 recalls it; the
  footnote citations (Steinfeld, Binswanger with its misprint noted in the
  source comment, Scheler, Sartre, Koffka, Benary, Gasquet, the letter to
  Elizabeth) are to the right pages. Lessons are cited by title, chapters by
  Part and number, the next course by its §B title.

## What it taught badly, or said wrongly

### Fidelity

- **`the-body-as-a-work-of-art`, quiz 3 (the second-order object):** as
  above. Repaired.
- **`speech-as-gesture`, body, worked `after` and `mistakes[2]` ("follows no
  rule at all"):** as above. Repaired.
- **`the-body-as-a-work-of-art`, body:** "This is the answer an
  intellectualist, one of Kant's heirs, gives for any object". On p. 173 the
  text asks the cube question in its own voice ("Are we then to say that we
  perceive our body in virtue of its law of construction…?"); the attribution
  to intellectualism rests on p. 171 ("Intellectualism clearly sees that the
  'motif of the thing' and the 'motif of space' are interwoven", with
  Cassirer in the footnote) and on §C's misconception. Not wrong, and the
  history is right (Cassirer was a Kantian); recorded so the authors know
  "one of Kant's heirs" is the lesson's phrase.
- **`speech-as-gesture`, body:** "the chapter first states it as if it were
  its own, answering it only later". Exact: p. 204 states the categorial
  reading in indirect speech and p. 205 opens "These analyses and other
  similar ones lead us, it would seem, to the antithesis of the theory of the
  verbal image". `mistakes[0]` says the same thing as "reports it in its own
  voice on pp. 204 and 205", which a reader could hear as "endorses". Left;
  see recommendations.

### Prose that left the lab, or the reader, unexplained

- **`the-body-as-a-sexed-being`:** *aphonia* unglossed. Repaired.
- **`the-spoken-word-and-thought`:** *phonemes* unglossed. Repaired.
- **`the-body-as-a-sexed-being`:** Casanova unplaced. Repaired.
- Every tile each view prints is explained in prose: `vrCore`, `vrVary` and
  `vrBreak` in lessons 1 and 4 (the `tracing` preset's `vrVary`, `fingers,
  arm`, is the one tile string on the course not named in a body paragraph,
  and it is the obvious one); `caRecord`, `caSurvivors` and `caSplit` in
  lesson 2, each named with what it counts; `soCategorical`, `soChain` and
  `soPart` in lesson 3, with the chain's rule and the banner it is printed in.

### Quiz

Every distractor on the sixteen questions was argued for and could not be
defended. Two came closest. Lesson 3's "They sorted at random, by no
resemblance at all" (as Gelb and Goldstein's *first* explanation) could tempt
a reader who remembers the chapter's correction that the patient adopts no
principle; but the question asks for Gelb and Goldstein's first reading, and
p. 204 says it is "the experience of an immediate resemblance" that guides
them, so the distractor fails on the question's own terms. Lesson 2's "Her
throat and mouth may have been particularly sensitive" (as what shows the
loss of voice is not a paralysis) is on p. 186 as part of why the emotion
took this form, and the `why` says so; it does not show anything about
paralysis. Lesson 2's `why` for quiz 3 has one tangled clause ("Being unable
to speak at will is what shows it is not a deliberate silence, which would
fit a paralysis"): true, since an inability fits a paralysis and so cannot
tell against one, but a reader has to work to see it. Left; see
recommendations. Lesson 1's door question and lesson 4's grief question are
clean instances of the act, and lesson 3's dark-green question is the best
computational item on the course, because its correct answer is the sample
of *another* hue, which is what `soPart` means and what a reader sorting by
hue first gets wrong.

### Speech

Every `data-say` on the four pages was read. The key lines read as prose
("the body is of space, not merely in it. movements share a meaning, not
muscles"), the worked lines read in order ("from pale red 9, pale green costs
1 plus 1, mid red 3. from pale green 8, mid red and mid green both 3. tie, mid
red is listed first, so it comes next"), and the `→` of the chain is spoken
"goes to". No three-letter word at the head of a key line is spelled out
(`tie:` is read as the word), no `=` is followed by a short word, and the
preview lists no unspoken run. Two lines carry a question mark inside the
spoken form ("a limb in all four ?, no"; "a sign in all three ?, none"),
which reads as a pause rather than a word. Harmless.

### Cross-references

Lessons are cited by title (“The Body as a Sexed Being”, “Speech as Gesture”,
“The Spoken Word and Thought”, each exactly as the lesson carries it); the
book by Part and chapter, as §0's first deviation requires; the previous
course by its §B title, The Lived Body, and the next by Sensing and Space. No
lesson is cited by number.

## Can a first-time reader of these chapters follow the four lessons?

Yes, and the places a reader will slow down are the places the chapters'
readers slow down.

- **Lesson 1** is the shortest and the one most likely to be read in one
  sitting with the chapter open. Its second paragraph (the Cartesian and
  Kantian tradition, *partes extra partes*, anosognosia and the phantom) is
  the course's densest and comes early; the `concepts` block has already
  given *partes extra partes* in plain English, and the paragraph ends on the
  two-patient summary ("anosognosia shows that the place is not enough, the
  phantom that it is not even needed"), which is the sentence a first reader
  needs. The telephone comes next and is the chapter's own, so the reader has
  something in hand before the cube and Leibniz. The work-of-art paragraphs
  are the best on the course: the Cézanne sentence ("leaves you choosing
  among several possible Cézannes, and only the pictures give you the one
  there is") carries the whole comparison for a reader who has not read the
  page. The "Notice what the lab has done, though" paragraph is where a
  reader learns something the lab alone would have taught wrongly.
- **Lesson 2** is the longest and the hardest, as the chapter is, and it
  protects the reader three ways: it names the two accounts before Schneider
  and keeps to them; it puts the Freud paragraph *between* Schneider and the
  girl, where the chapter puts it, and says in one sentence what Freud's
  theory itself said so the reader can see what the chapter is reading
  against; and it gives the girl's case in the chapter's order (the
  prohibition, the earlier episodes, the oral phase, co-existence, the two
  refused readings, forgetting, the field of possibilities, the conversion of
  the body). A first reader will still find the "difficulty in its own
  reading" paragraph (tautology or reflection) abstract; the Casanova example
  is what makes it land, which is why he is now placed. The second reviewer's
  mapping paragraph makes the table harder to read and more honest, and the
  `def`-free structure of this lesson means the `concepts` block has to carry
  *co-existence* and *interfusion*; it does.
- **Lesson 3** moves from the lamp to the ribbons to the kinship argument to
  the brush and then jumps seventeen pages. The jump is announced in the
  opening `p`, the `read_intro` and a body sentence ("Later, on page 221,
  the chapter comes back to the patients"), and the reader is told why: the
  chapter corrects its own first description. The `def` block that separates
  the categorial from the concrete attitude arrives before the lab, so the
  reader meets the chain knowing which attitude it is a model of. What a
  first-time reader may miss is that the chain is, roughly, the lesson's
  picture of what Gelb and Goldstein's *first* reading described; the lesson
  says "a sort by concrete resemblance" and leaves the reader to connect it.
  Recorded below.
- **Lesson 4** has the most ground (gesture, the objection, two replies,
  sediment, Darwin, Schneider's speech, the speaking and the spoken word,
  Descartes) and keeps each to a paragraph. The café opening gives the reader
  Scheler's point before Scheler. The two-reply structure is the chapter's,
  not imposed: p. 217 answers the convention half and p. 219 the natural-sign
  half, and the lesson marks them "First" and "Second, and here the passage's
  case comes in". A first reader will manage the "speaking word and spoken
  word" paragraph because the `concepts` block has defined both and the
  fortune image is the chapter's. The Descartes paragraph is four sentences
  and names the letter.

The course protects the reader in two further ways later courses should
keep: the `how_to` says the chapters lean on The Lived Body and that the
lessons recall rather than re-teach, and every lesson says in `p`,
`panel_intro` and `note` which instances are the book's and which the
lesson's, so a reader never mistakes a signature in sand or a lightness of 8
for a claim about Gelb and Goldstein.

## Repairs made in this pass

In `content/phenomenology/c4_expressive_body/part_a.py`:
`the-body-as-a-work-of-art` quiz 3 (the third distractor and its `why`, the
second-order object placed as p. 176 places it); `the-body-as-a-sexed-being`
the tautology paragraph (Casanova placed in a clause) and the `aphonia`
paragraph (*aphonia* glossed); `speech-as-gesture` the closing body paragraph,
the worked `after` and `mistakes[2]` ("adopts no principle of classification"
for "follows no rule at all"); `the-spoken-word-and-thought` the first-reply
paragraph (*phonemes* glossed). Nothing in `__init__.py`. No preset,
`expect`, slug, module, lab key, mode, view or `accounts` changed, and no §C
instance needed correcting: every instance the lessons carry is the one §C
records, including the resolutions §C already notes (the telephone as first
preset, the two account names, the ribbons preset, the anger signs limited to
p. 219's).

The second reviewer's concurrent changes to the same file (the lab paragraphs
of `the-body-as-a-sexed-being`, which now say each observation is "the
lesson's one-line summary of what the chapter reports", make the
paralysis/simulation mapping explicit and note p. 189 on how the treatment
works; the worked `after` of `speech-as-gesture`, which now says the samples
chain "has the shape of the report's pale green after a pale blue, which the
ribbons preset codes directly") were read after they landed and are
consistent with the text and with this assessment; none is claimed here.

Slugs, lesson count, modules, lab keys, modes and views are as PLAN §B and §C
list them. `python3 scripts/preview_subject.py phenomenology --course
perception-the-expressive-body` reports OK: 5 pages, every lab executes and
survives the sweep, every pinned figure on the four pages matches, no math
run without a spoken form. `phen_quotes.py c4_expressive_body` reports OK: no
span outside the text, no cap exceeded.

## Remaining issues and recommendations (taste, not changed)

- **Say what the chain is a model *of*.** Lesson 3 calls the chain "the
  lesson's model of a sort by concrete resemblance" and separately states
  Gelb and Goldstein's first reading ("it is an immediate resemblance that
  guides them"). One clause joining them, in the chain paragraph or
  `steps[3]`, would tell the reader whose description the chain pictures: the
  chain is the lesson's picture of the sort Gelb and Goldstein's first reading
  describes, the categorical sort is the task's, and the chapter's correction
  is that the patient adopts neither as a principle. That also answers the
  Subject's question for this lab in one line (what the reader computes, and
  whose).
- **Spend the quotation budget on the chapter's own summary lines.** Lesson 3
  has 39 words left and lesson 4 36. Candidates the lessons already
  paraphrase: "The spoken word is a genuine gesture, and it contains its
  meaning in the same way as the gesture contains its" (p. 213), which is the
  sentence lesson 3 hands to lesson 4; "the meaning inhabits the word"
  (p. 224), lesson 3's conclusion; "Everything is both manufactured and
  natural in man" (p. 220), lesson 4's reply to the whole division.
- **`speech-as-gesture`, `mistakes[0]`:** "The chapter reports it in its own
  voice on pp. 204 and 205" can be heard as "endorses". "The chapter states
  it on pp. 204 and 205 without yet naming its authors, and then answers it"
  says what the body says.
- **`the-body-as-a-sexed-being`, quiz 3 `why`:** untangle "which would fit a
  paralysis": "Being unable to speak at will fits a paralysis, so it cannot
  tell against one; it is what shows the silence is not deliberate."
- **§C still carries a marker the lesson has resolved.** The Course 4 lesson 1
  entry says "a knot of living meanings *(wording to be checked against the
  text)*"; Smith's word is *nexus* ("a nexus of living meanings", p. 175),
  and the lesson quotes it correctly. AUTHORING makes the §C correction the
  author's, and PLAN.md is outside this assessment's files; the author should
  replace "knot" with "nexus" and strike the marker.
- **Course `key`, "the body: a work of art, not a machine".** The chapter's
  own contrast is with "a physical object" and *partes extra partes*;
  "machine" is §C's word for the misconception and the lesson's `mistakes[0]`
  uses it with "the Cartesian picture". Accurate as a gloss of the Cartesian
  body; recorded so no one looks for the word on p. 174.
- **`the-body-as-a-work-of-art`, "one of Kant's heirs":** see Fidelity. "the
  intellectualist account, in the tradition the chapter calls Cartesian and
  Kantian" would tie it to p. 171.
- **The `tracing` preset's `vrVary` tile** (`fingers, arm`) is on the page
  and is not named in prose. Harmless; recorded so the stronger rule is not
  read as broken.

## Lessons for the remaining authors

1. **When the chapter corrects itself, carry the correction's own object.**
   "He never adopts any" is about a principle of classification; "follows no
   rule at all" is a stronger claim the text does not make and the same page
   half-contradicts. Three places on one lesson said the stronger thing.
2. **A quiz `why` is a reading of the text, and is checked like one.** The
   course's one misplacement of the text's words was in a `why`, where the
   body had it right. Check every `why` against the page, not against the
   body.
3. **Where a `cases` table maps the chapter's pair onto the lesson's accounts,
   say so in the body, with the page for each.** Chapter 5's pair on p. 187
   is paralysis and simulation, not the two accounts of p. 179; the lesson now
   says how it reads one onto the other and that the mapping is the lesson's.
   Course 6's hallucination tables and Course 7's cogito will need the same
   sentence.
4. **A family-3 model should be named as a model of someone's description.**
   "The lesson's model of a sort by concrete resemblance" is honest; "the
   lesson's picture of the sort Gelb and Goldstein's first reading describes"
   is honest and tells the reader whose prediction the figure is.
5. **Gloss the medicine and the history as carefully as the philosophy**:
   aphonia, anarthria, alexia, paraphasia, pithiatism, engram; Casanova,
   Balzac, Stendhal, the Trobriand Islanders. One clause each.
6. **The "lab turned on itself" paragraph is the pattern for family 2.** An
   invariant is a spectator's summary; the chapters of Part One say the body
   is not available to a spectator that way. Say what the exact count shows
   (negative, and true) and what it cannot be.
7. **Keep the reading range exact and the jumps announced.** Lesson 3's
   "pages 202 to the end of the paragraph on page 214, and then 221 to 225"
   is the model for a lesson that reads a chapter in two pieces.
8. **One scene in four is enough** when the chapters' own cases are as
   concrete as the telephone, the ribbons and the smiling Japanese.
9. **Keep the checker and the preview green after every edit, and re-read the
   file before each edit when another agent is in it.** This course was
   reviewed by two agents at once; the file changed under both, and every
   edit here was made against a fresh read of its lines.

Final lines. Preview: `OK` (5 pages rendered; labcheck, every lab executes: 4
page(s) executed and swept, 0 failing; labcheck, pinned figures match: 4
page(s) executed and swept, 4 with pinned figures, 0 failing). Quotation
checker: `OK` (106, 121, 111, 114 quoted words; openings 51, 60, 29, 31).
