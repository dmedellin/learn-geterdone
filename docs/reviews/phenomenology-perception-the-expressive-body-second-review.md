# Second review: The Expressive Body (`perception-the-expressive-body`, `c4_expressive_body`)

This is the independent second read, done to `docs/phenomenology/SECOND-REVIEW.md`
and held to the "Lessons from" sections of `docs/phenomenology/AUTHORING.md`.
I read all of Part One, Chapters 4 to 6, in Smith (pp. 171–232), and the Part Two
title pages (pp. 233–235). Then I checked every sentence in the four lessons
that says what Merleau-Ponty argues, and every sentence that reports a source,
against those pages. I wrote these findings before reading the pedagogy
assessment.

Files changed:

- `content/phenomenology/c4_expressive_body/part_a.py`
- `content/phenomenology/c4_expressive_body/__init__.py` (the summary only)
- one §C entry in `docs/phenomenology/PLAN.md` (Course 4, lesson 1, **Read**)

No instance, preset, pinned figure, misconception or worked line changed.

Final checks after the changes:

- `python3 scripts/preview_subject.py phenomenology --course perception-the-expressive-body --out <scratch>/sr-c4`:
  every lab executes on 4 pages, 4 with pinned figures, 0 failing. Final line: `OK`.
- `python3 -I <scratch>/tools/phen_quotes.py c4_expressive_body`: 106 / 121 / 111 / 114
  quoted words (openings 51 / 60 / 29 / 31), no misses. Final line: `OK`.

## Findings: what the text says

### 1. Course summary and The Spoken Word and Thought: two Part titles wrong (fixed)

The course `summary` opened "Part One, Experience and Objective Thought. The
Problem of the Body, its last three chapters". In Smith's contents that is the
title of Part One's *introduction*. The Part itself is "The Body" (p. v). PLAN
§B says the summary names the Part exactly, and the sister courses do (C3:
"Part One, The Body: its introduction, …"; C5: "Part Two of the book, The World
as Perceived: its introduction, …").

The last `p` of lesson 4 had the same error for Part Two. It said Part Two's
"title in Smith is The Theory of the Body is already a Theory of Perception".
Smith's Part II title page (p. 233) reads "The World as Perceived". The other
phrase is the title of the Part's introduction (p. 235).

**Changed:** the summary now reads "Part One, The Body, its last three chapters:
…". The pointer now reads "begins Part Two, The World as Perceived, with its
introduction, The Theory of the Body is already a Theory of Perception."

### 2. The Spoken Word and Thought: the "celebrated distinction" is not speaking/spoken (fixed)

The lesson said: "Restating a celebrated distinction it does not name, the
chapter draws 'a distinction between a speaking word and a spoken word'."

On p. 229 these are two separate steps. "Restating a celebrated distinction"
introduces the first: languages, the constituted systems of vocabulary and
syntax, are the repository and residue of acts of speech. This is recognisably
Saussure's *langue* and *parole*, though the chapter does not name him. The
speaking/spoken distinction then comes with "Or again one might draw…", as a
second way of putting it. As written, the lesson made the unnamed celebrated
distinction the speaking/spoken one, and gave the chapter a citation it does
not make.

**Changed:** the paragraph now states the first distinction in a clause, then
introduces the quoted one with the chapter's own "Or again". The quotation is
unchanged.

### 3. The Body as a Sexed Being: the girl's pair is paralysis and simulation, and the mapping was silent (fixed)

§C records that on p. 187 the chapter sets the aphonia against paralysis and
simulation, not against the two accounts of sexuality on p. 179. The prose did
not say so. Instead:

- `concepts_intro` said the chapter "tests them on two patients";
- the lab paragraph coded the girl's observations against "a bodily mechanism"
  and "a representing consciousness" as though the chapter did.

The y cell for the representing consciousness was also justified with "since
an idea has changed and the symptom has gone". That reason is the lesson's, and
the chapter pushes against it two pages later. On p. 189 psychological medicine
does not act by making the patient know the origin of the illness; sometimes a
touch of the hand restores speech. On p. 191 the voice comes back "not by an
intellectual effort".

**Changed:**

- `concepts_intro` now says the chapter tests the two accounts on Schneider and
  meets the same pair in Binswanger's patient under other names, paralysis and
  simulation.
- The lab paragraph now says the mapping is the lesson's: paralysis as what a
  bodily mechanism would make of the symptom, a deliberate silence as what a
  representing consciousness would. It ties the pair to p. 180's "between
  automatic response and representation".
- The y cell is now justified from the simulation reading: a silence kept on
  purpose would end when the prohibition did. The paragraph adds that the
  chapter concedes the recovery rules out paralysis, and that p. 189 denies the
  cure works by knowing.

The cells and the pinned figures are unchanged.

### 4. The Body as a Sexed Being: "each observation is a sentence from the reports" (fixed)

The observations are the lesson's one-line paraphrases, for example "for
Schneider after a small occipital wound sight and touch have lost much of their
sexual significance". They are not sentences from Steinfeld or Binswanger.
**Changed:** "Each observation is the lesson's one-line summary of what the
chapter reports".

### 5. Speech as Gesture: a reported patient behaviour denied (fixed)

`mistakes[1]` ended: "the samples preset's categorical sort uses the hue names
as its rule; nothing in the patient's behaviour, as reported, works like that."
That is false, and the lesson's own body reports the counter-case. On pp.
223–224 certain patients sort through language: they name the model's colour
and collect what the name fits, without looking back at the model. The chapter
calls this an abnormal procedure, in which language and thought are both cut
off from their living significance.

**Changed:** the mistake now says that some patients do sort by naming, and
that the chapter calls it an abnormal procedure.

### 6. Speech as Gesture: the "no" case misread (fixed)

The lesson said the patient could find the word *no* "to refuse something the
doctor asked". On pp. 203–204 he finds it "in answer to the doctor's
questions", when he means to deny something from his present experience, and
cannot say it as an exercise without vital bearing. The point is the contrast
between a denial that means something now and one that is an exercise. A
refused request is a different scene. **Changed** to match the text.

### 7. Speech as Gesture: whose voice on pp. 204–205 (fixed)

The body was careful here: the chapter "first states it as if it were its own,
answering it only later". `mistakes[0]` then said "the chapter reports it in its
own voice on pp. 204 and 205". A reader takes "its own voice" to mean the view
is Merleau-Ponty's, which is the very error the mistake warns against. On p. 204
the interpretation is unmarked in the prose, and the footnote assigns it to
Gelb and Goldstein. **Changed:** "sets it out on pp. 204 and 205 without
marking it as another's, with Gelb and Goldstein in the footnote, and then
answers it."

### 8. The Body as a Work of Art: "not learnt piece by piece" softened the text (fixed)

Smith p. 172 says flatly that the co-ordination of the body's parts "is not
learnt". The lesson wrote "not learnt piece by piece", in the body and in the
`why` of quiz question 4. That weakens the claim into a near-truism. The "not
forged gradually and cumulatively" on p. 173 is about the links between the
parts and the senses, not about learning. **Changed:** body "their
co-ordination, the chapter says flatly, is not learnt"; `why` "that
co-ordination is learnt".

### 9. The Body as a Work of Art: Chapter 5's area is affective life, not "desire" (fixed)

The closing pointer said Chapter 5 looks "in the one area of experience that
has significance only for us: desire". On p. 178 the area is "our affective
life". Desire and love are the ways a being comes to exist through it. The
course and lesson 2 summaries already had this right. **Changed:** the area is
now affective life, and the pointer asks how something comes to exist through
desire or love.

### 10. Speech as Gesture: the worked example's analogy (fixed, minor)

The worked `after` called the samples preset's red → pale green step "the
pale-green-after-pale-blue of the report, in the lesson's figures". It is a
different instance with the same shape. The pale-blue case is the `ribbons`
preset. **Changed:** "It has the shape of the report's pale green after a pale
blue, which the ribbons preset codes directly."

### 11. The Spoken Word and Thought: Darwin is inside the aphasia pages (fixed, minor)

"After the pages on aphasia, the chapter shows…" introduced Darwin's knitted
brows. They are on p. 225, inside the pages lesson 3 reads. **Changed** to "At
the end of the pages on aphasia and just after them".

### 12. The Body as a Sexed Being: the historical-materialism footnote at strength (fixed)

`mistakes[0]` said the footnote shows of economics and history that "neither
explains the other". The footnote is more careful. "Every cultural phenomenon
has, among others, an economic significance". History "never transcends, any
more than it is reducible to, economics". Economics can be the dominant
significance of a period (pp. 200–201). **Changed:** "neither is reduced to the
other, though every cultural fact has an economic significance among others."

### 13. PLAN §C, Course 4 lesson 1: an unresolved "(check against text)" (fixed)

The **Read** line still had "a knot of living meanings *(wording to be checked
against the text)*". Smith p. 175 has "a nexus of living meanings", which is
what the lesson quotes. **Changed** the §C entry to "a nexus of living meanings
(Smith's wording, p. 175)".

## Checked and found right

- **Every quotation:** the checker passes, and I checked each one by eye for
  voice. Each quotation said to be Merleau-Ponty's is in his voice in Smith, and
  none is an opponent's view he is about to reject:
  - p. 176 "an instrument with which he perceives" comes after the "But habit…"
    reply, not in the tempted view;
  - p. 214 "it is anger itself" is his own sentence after the report of modern
    psychology;
  - the p. 223 "Categorial behaviour…" sentence is said to be quoted from Gelb
    and Goldstein, which it is (footnote 26).
- **The views he rejects:** the lessons present each in its owner's voice, in
  the right place:
  - the stick read as signs (p. 176);
  - the cube's law (p. 173);
  - the mosaic view of affectivity (pp. 178–179);
  - the Gelb–Goldstein interpretation (p. 204);
  - the natural/conventional division ("what is commonly expressed", p. 217).
  The smile that has joy in it (p. 217) is handled with care. It is in the
  objection's set-up, and the lesson says the chapter does not deny it.
- **Figures:** I recomputed every one.
  - Every core, every vary list, every break, every case record and split, and
    every chain under the printed rule (the four sorting presets, the worked
    lines' costs 1 + 1 against 3 and the 3–3 tie, quiz 1 in lessons 1, 2, 3 and
    4) is right.
  - The `labcheck --observe` strings agree with the pinned ones and with the
    prose, preset by preset.
  - No figure is attributed to perception. The lab's figures are always "the
    lesson's coding" or "the lesson's model". Lesson 1 sees, rightly, that its
    own invariant is close to the "law for covariant terms" the passage denies
    the body is, and says so.
- **Quiz:** I tried to argue for each distractor and could not make one stand.
  Quiz 3 in lesson 2 is close but holds. "She cannot speak even when she wants
  to" tells against simulation, not paralysis, and the `why` says so.
- **Sources:**
  - Schneider is the 1915 occipital wound, with Steinfeld (p. 179 n. 1) and
    Benary (p. 228 n. 36).
  - Binswanger's case is from *Über Psychotherapie*. Smith's footnote misprints
    the name "Rinswanger", and the code comment notes it.
  - Gelb and Goldstein are Frankfurt, *Über Farbennamenamnesie*.
  - Koffka's *Growth of the Mind* (p. 177) and Scheler (p. 214 n. 13) are right.
  - Sartre on the caress is p. 216 n. 14.
  - Descartes to Elisabeth is 28 June 1643 (p. 231 n. 40).
  - The kiss footnote and the Trobriand paternity footnote (p. 220) are right.
  - Chapter 4 is the shortest chapter in the book, seven pages (pp. 171–177),
    as lesson 1 says.
- **Clinical cases:** they are treated with respect. Each lesson that uses a
  report says the lab codes the report, not the patient, and the Schneider
  lessons say his reports were later questioned.

## Recommendations (taste, not changed)

- **Who they were, on first mention.** Leibniz (lesson 1), Steinfeld and
  Casanova (lesson 2), Benary and Sartre (lesson 4) get no gloss; the other
  sources do. Steinfeld and Benary are only names in Smith's footnotes, so
  "who wrote on Schneider's case" would do. Sartre may already be glossed in an
  earlier course.
- **"Making human existence walk on its head".** Lesson 2 says the phrase
  "recalls Marx turning Hegel the right way up". The gloss is plausible, and the
  footnote's "turning history upside down" (p. 199) supports it. But it is the
  lesson's association, and "the phrase is in quotation marks in Smith, and
  recalls…" would show that.
- **Smith's "natural convention" (p. 217).** Smith prints "the word a 'natural
  convention'", which looks like a slip for "conventional sign". The lesson
  paraphrases ("the word a convention"), which is right. If the line is ever
  quoted, the oddity needs a word.
- **The tracing preset's vary tile** (`fingers, arm`) is not named in the prose.
  It is obvious from the two signatures it keeps, so it is not worth a sentence
  unless the pedagogy pass wants every tile named.
- **Voice.** The voice is warm and unperformed throughout. One scene opening is
  the café in lesson 4, and the telephone in lesson 1 is the book's own scene,
  so the course is well inside §F's ration. There is no modern aside, which is
  correct for this course. "Notice what the lab has done, though" (lesson 1) is
  the best move in the course.

## Where I disagree with the pedagogy assessment

The pedagogy assessment, `docs/pedagogy/phenomenology-perception-the-expressive-body.md`,
did not exist when I finished these findings. I checked for it before writing
and again after the final preview run, and it was not there either time. So I
have recorded no disagreements. If it appears, findings 2, 3 and 5 are the ones
to compare it against: each is a passage that reads well and misstates the text.
