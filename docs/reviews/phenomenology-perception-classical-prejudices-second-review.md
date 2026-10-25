# Second review: Classical Prejudices (`perception-classical-prejudices`, `c2_prejudices`)

This is the independent second read, done to `docs/phenomenology/SECOND-REVIEW.md` and to
the "Lessons from" sections of `docs/phenomenology/AUTHORING.md`. I read the whole of
Smith's Introduction, pp. 3–74, including its footnotes, and the first page of Part One
(p. 77). Then I checked every sentence in the five lessons that says what Merleau-Ponty,
an opponent or a source argues against those pages. I recomputed every figure. I wrote
these findings before reading the pedagogy assessment.

Files changed: `content/phenomenology/c2_prejudices/part_a.py` only. Nothing in §C of
`docs/phenomenology/PLAN.md` had to change. No fix alters an instance, a misconception,
a preset or a worked line.

Final checks after the changes:

- `python3 scripts/preview_subject.py phenomenology --course perception-classical-prejudices --out <scratch>/sr-c2`:
  5 pages executed and swept, 5 with pinned figures, 0 failing. Final line: `OK`.
- `python3 -I <scratch>/tools/phen_quotes.py c2_prejudices`: 88 / 110 / 85 / 129 / 109
  quoted words (openings 48 / 40 / 47 / 56 / 68), no misses. Final line: `OK`.
- `node scripts/labcheck.js --observe` on all five pages: every preset's tiles agree with
  the prose, the worked lines and the pins (details under "Arithmetic" below).

Overall the course is faithful. The numbers are all right, the voice attributions of the
quotations are right, and the course is careful throughout to say whose test the moon in
the tube is (Alain's, p. 32 n. 2 and p. 36 n. 12). The errors below are small. Most are
paraphrases that overstate the text or drop a qualifier that carries the argument.

## Findings: what the text says

### 1. The Constancy Hypothesis: two concessions presented as conflicts (fixed)

The lesson listed "Red and green shown together give grey, and an object's apparent size
varies with its apparent distance" among the conflicts with the hypothesis, alongside
the three cases on p. 8. On p. 9 Smith sets these two apart: in them "it is conceded"
that central factors are at work, and the defenders admit that the sensory processes
are not immune to central influences. The chapter's argument is then that the same
conclusion should be drawn from the first three cases. Leaving that out weakens the
opponent, because it hides that the hypothesis's own defenders already grant these
cases. It also skips the step the chapter's argument rests on.

**Changed:** after those two cases the lesson now says that "in these last two cases,
the chapter notes, the hypothesis's own defenders concede that central processes
intervene".

### 2. The Constancy Hypothesis: "scrupulously fair" and "cannot be refuted" (fixed)

"And a footnote is scrupulously fair" was praise of the author in the lesson's own
voice, which AUTHORING forbids. Smith's own words in n. 13 are "It is only fair to add".
The same sentence then said the hypothesis "cannot be refuted by induction"; n. 13 says
"cannot be *completely* refuted". **Changed:** "And a footnote concedes, in fairness,
that there is no crucial experiment against the hypothesis, as there is none for any
theory, and that it cannot be completely refuted by induction."

### 3. The Constancy Hypothesis: the scientist "has to give up" the world in itself (fixed)

p. 11 says the scientist "must learn to criticize the idea of an external world in
itself", because the facts prompt him to abandon the body as transmitter. The lesson's
"has to give up the idea of a world in itself" claimed more than the text does.
**Changed:** "must learn to criticise the idea of an external world in itself, because
the facts prompt him to give up the body as a transmitter of messages."

### 4. Association and the Projection of Memories: Brunschvicg given Bergson's claim (fixed)

The lesson said the projection of memories is held "by the French philosophers Léon
Brunschvicg and Henri Bergson among others: in reading, the eye moves too fast…". On
p. 22 the footnotes split these claims. Brunschvicg (n. 8) is cited for talk of "the
contributions of memory" outside empiricism. Bergson (n. 9, *L'Effort intellectuel*) is
cited for the reading argument. **Changed:** "a way of talking found outside empiricism
too: the French philosopher Léon Brunschvicg speaks of the contributions of memory, and
Henri Bergson argues that in reading the eye moves too fast to take in every letter, so
memory fills the gaps."

### 5. Association and the Projection of Memories: "hoxse, its third letter unreadable" (fixed)

A printed *x* can be read; it is misprinted, not unreadable. The lesson's own model
only works because it treats the misprinted letter as one the eye did not take in. That
is the projection theory's own procedure on p. 25, which reconstitutes "the elements
actually seen" from eye movements and reading speed. As written, the body and the
preset label described a different case from the one the model computes.
**Changed:** the body now says "The model counts the misprinted third letter as not
seen, as the projection theory counts the letters the eye skipped, so the pattern is
`ho_se`". The label now reads "its misprinted third letter taken as unseen". No pinned
figure changes.

### 6. Attention and Judgment: "the reply comes three pages later" (fixed)

The tube is on p. 32 and the reply is on p. 36, four pages later. **Changed:** "the
reply comes on page 36".

### 7. Attention and Judgment: the intellectualist's argument cut off from its empiricist premise (fixed)

The lesson gave the intellectualist's strongest argument as "once vision is defined as
a quality impressed by the stimulus, the least illusion … proves that perception is a
judgement". Smith p. 38 has "Once vision is defined *in the empiricist way* as the
possession of a quality impressed upon the body by the stimulus". That qualifier is the
chapter's thesis in small: intellectualism thrives on the refutation of empiricism and
borrows its notion of sensation (pp. 37, 45). Dropping it hid the very dependence the
lesson's passage announces. **Changed:** "once vision is defined in the empiricist way,
as a quality impressed on the body by the stimulus, the least illusion…".

### 8. The Phenomenal Field: the "one true subject" step given only to classical philosophy (fixed)

The lesson said that "the classical transcendental philosopher" would complete the
analysis with one true subject, the thinking Ego, and that "the chapter refuses". On
p. 70 Smith calls this the ordinary perspective of a transcendental philosophy "and
also, to all appearances at least, the programme of a transcendental phenomenology".
n. 12 adds that it is set out in these terms in most of Husserl's works. The point
matters: §F.4 lists his relation to Husserl among the disputed readings, and the lesson
had dropped the sentence where the chapter turns that criticism on Husserl. **Changed:**
the lesson now adds that this is "to all appearances the programme of Husserl's
transcendental phenomenology too, as most of his works set it out", and says the chapter
refuses "the step". It still keeps the transcendental *field*, as p. 71 does.

### 9. The Phenomenal Field: "perception is the phenomenal field" (fixed, minor)

In the paragraph that gives Merleau-Ponty's account in prose, "perception is the
phenomenal field" was loose. On pp. 66–67 the phenomenal field is the layer of lived
experience through which things are first given, and "the immediate" becomes the
meaning, the structure and the arrangement of parts. **Changed:** "what perception first
gives is the phenomenal field, the meaning and the arrangement given together".

### Checked and correct (no change)

These points could have gone wrong, and each one checks against the text:

- **The Idea of Pure Sensation**
  - The two definitions of sensation (pp. 3–5).
  - The ape and the hen (p. 4).
  - The objection "in the empiricist's voice". It is an unnamed "one may object", and
    the reading is fair.
  - The Gestalt finding extended rather than rejected (p. 4).
  - The woolly red credited to Sartre's *L'Imaginaire* (n. 2).
  - The experience error.
  - The two ways of mistaking quality, and the retina-and-blackness construction (p. 6).
  - Attention as an auxiliary hypothesis (p. 7).
  - The warning on Wertheimer's laws (p. 19, n. 4).
  - Wertheimer's 1923 paper does list proximity first.
- **The Constancy Hypothesis**
  - The receiver–transmitter–station (p. 8).
  - Köhler's 1913 paper (n. 7) and Stumpf (n. 8). Köhler did take his doctorate under
    Stumpf.
  - The choice on p. 9.
  - The touch lesions and the colour losses (p. 10).
  - "different", not "unequal" (p. 13).
  - Children's constancy (Hering, Jaensch).
  - Scheler's net (n. 27).
  - The modern aside is in the one place §F.1 allows. It states both readings of
    predictive processing and does not settle the chapter.
- **Association**
  - "I read 'deduction'…" is presented, correctly, "as the theory itself describes it"
    (p. 23).
  - Lewin's syllables (pp. 20–21). They are reported accurately, including the
    reproduction intention.
  - Hering's memory colour.
  - The dilemma of p. 24 and the tardy correction (pp. 24–25).
  - "On this footing empiricism cannot be refuted", and reflection as closed as
    insanity (pp. 26–27).
  - The human world and the policeman (p. 27).
- **Attention and Judgment**
  - The searchlight and the wax (pp. 30–31).
  - "Too poor … too rich" and the two ignorances (pp. 32–33).
  - Head, and J. Stein's reports (n. 4).
  - The infants' nine months (p. 34).
  - Descartes's window (n. 16, Second Meditation).
  - Lagneau's two eyes (n. 19).
  - The box, the cube, and true and false perception (pp. 39–40).
  - The natural judgement of the Sixth Meditation, and the chapter's grant that it may
    be "the ultimate significance of Cartesianism", followed by "only by transforming
    itself radically" (pp. 48–51).
  - The motive and the steeple (p. 56).
  - "We pass from absolute objectivity…" (p. 45).
  - The ship (p. 20) is Merleau-Ponty's own first-person description, not an
    opponent's, and the lesson says it borrows the case from Chapter II.
- **The Phenomenal Field**
  - Herder, Koffka's wheel and candle (nn. 1–2).
  - Alain and Brunschvicg on incipient science (n. 7).
  - Bergson and the immediate data.
  - The sun at two hundred yards (p. 71).
  - The two mirrored mistakes (p. 72).
  - "neither without psychology nor with psychology alone" (p. 73).
  - The next-course pointer matches Course 3 lesson 1's title.

## Quotations

The checker finds no misses and no cap overruns (largest lesson 129 words, largest
opening 68). It reports no convention-only items for this course. I checked by eye that
each quotation is in the voice the lesson gives it:

- **In an opponent's voice, labelled as such:**
  - "Hence we have in principle a point-by-point correspondence…" (p. 8) is the
    physiologist's premise. The lesson says so: "physiology's premise, as the chapter
    states it".
  - "I read 'deduction' when the word printed is 'destruction'" (p. 23) is the projection
    theory's reasoning. The lesson says so.
  - "as evening leads one to expect night" (p. 17) is presented as where empiricism leads
    "followed through".
- **In Merleau-Ponty's own voice:** every other quotation. That includes "undifferentiated,
  instantaneous, dotlike impact", which he gives in exposition of the definition he is
  testing, and the lesson frames it as what pure sensation "would then be". The lesson
  quotes around Smith's typo "Pute sensation", correctly.

## Arithmetic and models

Every figure was recomputed by hand and against `--observe`:

- **Grouping.**
  - The gaps are 1, 3, 1, 3, 1, with threshold 2·1, giving three pairs.
  - With the dots evenly spaced the gaps are 2, the threshold is 4, and there is one
    group.
  - In the shift case the gaps are 1, 3, 2, 2, 1, giving `{0, 1} {4} {6} {8, 9}`.
  - Quiz Q1 has gaps 2, 1, 4, 1, giving `{0} {2, 3} {7, 8}`.
- **Stimulus.**
  - 10 − 10 = 0 and the gap is 2.
  - The context preset gives −1.
  - Q1 gives 0 and 3.
  - Q2 gives a prediction of 9 − 10 = −1 and a gap of 1 − (−1) = 2.
- **Cues/pattern.**
  - `ho_se` matches 2 words.
  - `_a_e` matches 18 of the 20; only house and horse fail.
  - With door the count is 1 (gate).
  - Q1 (water) gives lake.
- **Cues/sequence.** In the ship preset the count is 2 at both steps, and the shipped
  step 3 is clamped to 2. Close gives 1 at step 3, with the forest removed. Q1 gives a
  count of 2, with the shadow removed.
- **Cases.**
  - Intro: 1 of 8, failing 7; 2 of 8, failing 5, silent 1. Survivors none. The split is
    rows 2, 4 and 5.
  - Sensation: 0 of 3 against 1 of 3, failing 1, silent 1. The split is the misprint.
  - Attention: 1 of 3 each. The split is rows 4 and 5.
  - Shared: split none.
  - Q1 has survivors none and splits rows 1 and 2.

Each figure is attributed to a model, never to perception. The labels and the
`panel_intro`s name the proximity rule (with the ratio called the lesson's), the
constancy hypothesis, the associationist account, the judgement-from-signs model and
"the lesson's coding". The reported tiles are called illustrative reports. Course 1's
recurring error, a lab figure read as what someone sees, is absent: Mistake 2 in
lessons 1, 2 and 4 says it outright.

**The `cases` coding**, checked cell by cell against the text:

- Müller-Lyer, intellectualism n: by Zöllner, p. 41, which is a fair transfer.
- Misprint, intellectualism y: arguable, and the `note` says so.
- Ship, intellectualism `-`: p. 20 aims the case at association and credits Kant.
- The two attention rows: p. 33, exactly.
- Attention making a new object, n/n: p. 33, "attention creates nothing" for both.
- Moon, n/n: p. 36 names both.
- Cube, empiricism n: defensible from p. 40. The "sensible elements … like the stimuli,
  remain constant", so a stimulus-bound account cannot give the change either.

## Quiz

I tried to argue for every distractor, and none is defensible on the text. The closest
are these two:

- In The Constancy Hypothesis Q3, "equal in sensation, the difference added by a
  judgement" is the repair that p. 9 offers ("additional factors — attention and
  judgement"). The chapter does not assert it; it is the view the chapter answers, so
  the distractor holds.
- In The Phenomenal Field Q3, "Something consciousness forgets in favour of the things
  it presents" is true of the field (pp. 67–68). That is correct for a "which is it
  *not*" question, and the `why` says so.

## Voice (§F)

The voice is warm and unperformed, and goes line by line. Two lessons open with an
everyday scene (the Müller-Lyer figure in lesson 2, which is §F's own exemplary
paragraph, and proofreading in lesson 3), inside the half-of-lessons ration. There is
one modern aside, in the permitted place. These are taste recommendations, not changed:

- **R1.** Two inline glosses of *posit* read as bolted on. In lesson 1: "free to posit
  impressions beneath it, to set them down as there". In lesson 4: "whether Descartes
  posited it, set it down as his doctrine". Gloss the term once, in a separate clause, or
  in lesson 4 simply say "whether Descartes made it his doctrine".
- **R2.** Lesson 5 mistake 1, "In the lab the point shows as an absence…", is a stretch.
  The lab cannot show that the field is not an inner world, and the paragraph half-admits
  it. I would cut the lab sentences from that mistake, or replace them with a plain
  statement that the table cannot show this.
- **R3.** "Merleau-Ponty allows himself a dry comparison" (lesson 3) and "a reversal you
  might not expect" (lesson 2) are within the one light remark per lesson. They are
  fine, but they are the course's only flourishes of that kind; keep at most one.
- **R4.** In lesson 4 the closing quotation "We pass from absolute objectivity…" (p. 45)
  comes after the motive paragraph (p. 56), so a reader may think the chapter ends on it.
  A page reference in that sentence ("back on page 45") would keep the order honest.
- **R5.** In lesson 3, "The chapter's evidence against association as a force is an
  experiment by … Lewin". Gottschaldt's camouflaged figures (p. 21) are the evidence
  against association by resemblance. One clause naming them would make the paragraph
  complete. `not_covered` already names Gottschaldt.

## Where I disagree with the pedagogy assessment

The pedagogy assessment did not exist when this review was finished.
`docs/pedagogy/phenomenology-perception-classical-prejudices.md` was not in the tree, so
I have nothing to compare. Whoever reconciles the two should check this list against it.
In particular they should check whether it praises the paragraphs changed in findings 1,
4, 7 and 8, which are the kind of passage the Capital second reviews found praised and
wrong.
