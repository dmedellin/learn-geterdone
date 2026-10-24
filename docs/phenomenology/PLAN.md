# Phenomenology of Perception, Read Along — the build specification

This is the curriculum, lab and authoring contract for the eleventh Subject: a
read-along of Maurice Merleau-Ponty's *Phenomenology of Perception* (1945),
the whole book in its own order — the Preface, the Introduction and the three
Parts — one lesson per chapter, or per section where a chapter carries more
than one hard idea. Everything an author, a kit engineer or a reviewer needs is
here. Where it says "exactly", a test or a gate enforces it. Where it says
"never", a published page somewhere in this library has already been wrong for
that reason.

It is built the way *Capital, Read Along* was built (`docs/capital/PLAN.md`),
and adopts that document's conventions by reference wherever this one is
silent. Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight
note; `content/AGENTS.md` (all of it); `scripts/mathpath/AGENTS.md` ("a
preset's two claims"); `docs/philosophy/PLAN.md` §D.0 and §E; and
`docs/capital/PLAN.md` §0, §E and §F.

**Status: authoring.** The source edition is settled (§E.2): Colin Smith's
translation, Routledge Classics pagination, chosen by the operator on
2026-10-24.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The seven courses, and the module short forms
- §C Every lesson: 44 entries
- §D The lab kit: `phenkit` (15 modes), and `argkit/validity` reused
- §E Package layout, the source text, and quoting a book in copyright
- §F Voice: the read-along, after the three lectures
- §G What is left out, and why
- §H Wiring notes for the orchestrator
- §R Review record

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For *Capital* the answer was easy, because Marx does arithmetic on
the page. Merleau-Ponty does none, and a lab that pretended he did would be
decorative. The honest answer comes in three parts, and each lab says which
part it belongs to.

**First family: what the theories Merleau-Ponty argues against predict.** The
book is an argument with two opponents he names in the Introduction:
*empiricism*, for which perception is sensations caused point by point by
stimuli and joined by association, and *intellectualism*, for which perception
is a judgement that interprets those sensations. He groups both under the name
*objective thought* (the book's term; wording to be checked against the text),
and both make predictions that can be computed exactly from a stimulus: the two
lines of the Müller-Lyer figure are equal, so on the constancy hypothesis they
should look equal; a disc that sends the eye the light of white paper should
look white; a person four times as far away subtends a quarter of the angle, so
on a retinal-image account should look a quarter of the size, and on an
unconscious-inference account should be judged exactly full size; two lights
flashed in alternation are two lights, so nothing should move. Merleau-Ponty's
method is to put each prediction beside what perception actually gives and to
read the gap. The lab computes the prediction, exactly, from the quantities the
lesson states; the lesson reads the gap. Modes: `stimulus`, `grouping`, `cues`,
`size`, `perspective`, `depth`, `motion`, `light`, and `argkit/validity`.

**Second family: a count over the lesson's coding of the chapter's cases.**
Merleau-Ponty argues from cases — the phantom limb, Schneider, the aphasic who
cannot sort colours, Binswanger's patient who lost her voice, the infant who
opens its mouth — and his procedure with each is the same: set out what was
observed, ask which classical account can absorb every observation, and find
the observation that neither absorbs. That procedure is countable, and the
`cases` mode counts it. A `cases` table carries **the opponents' accounts
only** — two, occasionally three. The computed result is `caSplit` (the
observations on which the two opponents part) and `caSurvivors`, which on every
table in this Subject prints `none`: each opponent fails somewhere. Merleau-
Ponty's own account is stated in the lesson's prose, after the table, and is
**never a column and never scored** — a column the lesson coded for him would
have a clean sheet because the lesson coded it so, which is a decoration and an
endorsement at once. `cases` is used only where the chapter has no quantity and
sets at least two accounts against at least three observations; every
observation is listed in §C before the lesson is authored. `variation` belongs
to this family too: it computes what is common to a set of variants the lesson
codes. In both modes the count is exact and the coding is an interpretation;
the lesson says so, and a reviewer checks each cell against the text.

**Third family: the lesson's own illustrative model.** Some chapters have no
opponent's prediction to compute and no list of cases, but do describe a
structure the reader can manipulate: the body's coordinates and reach (`schema`),
the spatial level (`level`), the lines and columns of Husserl's time diagram
(`time`), the parallel of the geometer's proof (`triangle`), the chain of
concrete resemblances (`sorting`). There the lab computes a model the *lesson*
builds to illustrate the chapter. No theory says that perceived tilt is image
tilt minus a level, or that reach is an arm plus a cane. For these labs the
`panel_intro` says "the lesson's model", the `note` says what the model leaves
out, and no label ever attributes the model to the book or to an opponent.

So the claim this Subject makes, and the only one it makes, is this: **every
figure is what a stated model predicts from a stated stimulus — an opponent's,
a later psychologist's, or the lesson's own, and the lab says which — or a
count over the cases the lesson sets out, computed exactly in the browser.**
The lab never claims to compute an experience. That is the book's whole point,
and the material clause says so.

Fifteen `phenkit` modes and one reused mode carry the whole of it:

| what the reader computes | family | mode | from |
| --- | --- | --- | --- |
| the constancy hypothesis's prediction against a reported percept; a "pure quality" account's prediction of no motor effect | 1 | `stimulus` | two measured magnitudes, a reported difference |
| how dots group by proximity (the Gestalt rule), which no single dot contains | 1 | `grouping` | positions on a line, a gap ratio |
| which remembered words fit a partly seen word; which interpretations a judgement-from-signs account keeps as cues arrive | 1 | `cues` | candidates, a pattern of seen letters, a context, ordered cues |
| angular size; the retinal-image and the unconscious-inference predictions of size, and a Brunswik ratio | 1 | `size` | object size, distance, an assumed distance, a reported size |
| which faces of a box are visible from which directions, and their foreshortening; the smallest set of views that sees every visible face; two depth readings of one drawing | 1 | `perspective` | a box, view directions with whole-number length, reported faces |
| convergence and binocular disparity, as the classical theory computes them | 1 | `depth` | interocular distance, two distances |
| the speed implied by two lights, and the band in which motion is reported | 1 | `motion` | separation, interval, thresholds as later reported |
| luminance as reflectance × illumination, and each surface's ratio to the surround | 1 | `light` | reflectances, illuminations, a surround |
| whether an argument's premises force its conclusion (the argument from analogy; the cogito as inference) | 1 | `argkit/validity` (reused) | premises, conclusion |
| the observations on which two opponent accounts part, and whether either absorbs every observation | 2 | `cases` | observations × the opponents' accounts, each cell consistent, inconsistent or silent |
| the invariant core of a set of variants | 2 | `variation` | variants and their properties, which variants are still of the kind |
| where things are relative to the body rather than the room; the frame a task's target is given in; the reach of a habitual body and of a tool; an obstacle relative to a project and to the body | 3 | `schema` | body and object positions, a facing, reaches, a tool, a project's capacity |
| a categorical sort against a chain of concrete resemblances | 3 | `sorting` | colour samples with a hue name and a lightness 0–10 |
| perceived tilt as image tilt minus the spatial level, with a sudden or a gradual re-anchoring | 3 | `level` | an image tilt, a starting level, a rule |
| past and future along the river from two standpoints; the depth at which a moment is retained; one moment across many presents | 3 | `time` | positions or moments, a present, a protention span |
| the angles of a triangle through a parallel drawn at any vertex | 3 | `triangle` | two angles |

Every quantity is a whole number or a fraction, and every tile is exact.
Directions and turns are handled without trigonometry: a turn or a tilt is one
of the Pythagorean angles the kit lists (cosine and sine both rational), a view
direction is a whole-number triple whose length is a whole number, and an
angular size is the ratio size / distance, which is how a small angle is
computed in radians and how the lesson says it is computed. Where a degree
figure is printed it is printed beside its exact ratio and marked approximate.
Drawings may place pixels by floating-point trigonometry; no tile is ever
derived from a drawing (§D.0).

**Where an instance comes from.** A case or an experiment is Merleau-Ponty's own
report of his sources: Gelb and Goldstein's Schneider, Goldstein and Rosenthal,
Stratton, Wertheimer, Gelb, Katz, Head, Lhermitte, Schilder, Binswanger,
Minkowski, von Senden, Köhler, Koffka, Ehrenfels, and the philosophers
Descartes, Kant, Husserl, Heidegger, Scheler, Cassirer, Bergson and Sartre.
Where a preset uses figures the book or its source reports, its label says so
("Stratton's 1897 spectacles: 180°"); where it uses illustrative figures, the
label says "illustrative" and the lesson says so in prose. Where a lab computes
a measure or a rule that came later than the book (Brunswik's ratio, Wallach's
ratio principle, the textbook thresholds for Wertheimer's bands), the label
names it as the lesson's addition. The `cases` and `variation` cells are the
lesson's reading of the chapter, and the lesson says that too.

**Deliberate deviations from the library's conventions, recorded so no reviewer
has to rediscover them:**

1. **Cross-references to the book are by Part, chapter and section** ("Part
   One, Chapter 3"), as *Capital* cites volume and chapter. Lessons on this path
   are cross-referenced by title.
2. **One kit for the Subject**, plus `argkit/validity` for the two lessons whose
   object is literally an inference (the argument from analogy for other minds,
   and the cogito read as an inference).
3. **The passage comes first**, exactly as in *Capital* (§E.3 there), but the
   passage is short — this book is in copyright (§E).
4. **Most labs compute someone else's model.** In every other Subject a lab
   computes the lesson's own claim. Here the lesson's claim is usually that the
   computed figure is not what is perceived. Each lab's `panel_intro` names, by
   name, the model it computes: the opponent's ("the constancy hypothesis"),
   a later psychologist's ("Wallach's ratio principle, later than the book"),
   or, in the third family, "the lesson's model".
5. **The voice** (§F) is the *Capital* voice, after the same three lectures.

---

## §A PATH fields (`content/phenomenology/__init__.py`)

```
"slug": "phenomenology",
"title": "Phenomenology of Perception, Read Along",
"level": "Beginner → Advanced",
"level_note": "no philosophy is assumed; school geometry is enough for the labs",
```

**tagline** (counts re-verified at wiring):

> Maurice Merleau-Ponty&rsquo;s <em>Phenomenology of Perception</em>, read
> section by section from the Preface to Freedom &mdash; with the predictions of
> the theories he argues against computed in front of you, so that what
> perception gives can be seen beside them. Seven courses and 44 lessons are
> available.

**description**:

> The Phenomenology Subject: a read-along of Merleau-Ponty's 1945 book in its
> own order, seven courses that follow its Preface, Introduction and three
> Parts. Each lesson reads a short passage first, then explains it line by
> line, then computes what a classical theory of perception predicts &mdash; the
> length of two lines, the size of a person across a room, the colour of a
> spotlit disc, the motion between two lights &mdash; or finds the clinical
> observation on which the classical accounts part. All seven courses and 44
> lessons are available.

**key** (each line ≤ 46 characters):

```
angular size = size / distance
luminance = reflectance × illumination
ratio = luminance / surround's luminance
perceived tilt = image tilt − spatial level
motion seen: lights alternate in the band
an account survives if no case refutes it
a ∠ sum = two right angles, by a parallel
```

**material** (must differ from every existing clause; proposed
`PHEN_DISCLAIMER_RE = r"what perception gives is not a figure"`):

> every figure on this path is what a stated model of perception predicts from
> a stated stimulus, or a count over the cases a lesson sets out, or a lesson's
> own illustration, computed in your browser &mdash; and what perception gives
> is not a figure, which is the claim the book argues and the lab cannot
> settle.

**prerequisites** (paragraphs):

1. No philosophy. The Subject introduces Descartes, Kant, Husserl, Heidegger,
   Scheler, Cassirer, Bergson, Sartre and the psychologists — the Gestalt
   school (Köhler, Koffka, Wertheimer), Gelb and Goldstein, Stratton,
   Binswanger, Minkowski — at the moment Merleau-Ponty argues with them or
   draws on them, at their strongest. Words he uses in a sense of his own
   (*the body proper*, *motor intentionality*, *the phenomenal field*,
   *being-in-the-world*, which he takes from Heidegger) are defined in the
   lesson that introduces them.
2. School geometry: a ratio, a right angle, the angles of a triangle, a point
   on a grid. The labs do the arithmetic; what is asked of you is to say what
   each figure is a prediction of, and whose.
3. A copy of the book is strongly recommended. The book is in copyright, so a
   lesson quotes only a short passage and the phrases it reads closely, with
   page references to Colin Smith's translation (Routledge Classics, 2002,
   the 1962 translation repaginated), the
   one translation every lesson cites (§E.2). The rest is paraphrase, and a
   paraphrase is a reading: check it against the page.
4. Patience with a style. Merleau-Ponty writes long, looping paragraphs that
   state an opponent's view in its own words for pages before turning on it.
   A sentence quoted out of its paragraph can say the opposite of what he
   means; every lesson says whose voice a quoted sentence is in.

**why_order** (paragraphs):

1. The order is the book's, and it is the order of an argument. The Preface
   says what phenomenology is; the Introduction clears away two theories of
   perception; Part One finds, in the lived body, what both of them missed;
   Part Two re-reads sensing, space, things and other people from there; Part
   Three asks what this makes of the thinking subject, of time and of freedom.
2. The Introduction comes before the body because the body is the answer to a
   question the Introduction poses: if perception is neither a sum of
   sensations nor a judgement, what is it? Read first, Part One looks like a
   collection of clinical curiosities; read second, every case is an
   argument.
3. Part Three comes last because Merleau-Ponty wants the reader to have lived
   through the perceived world before being told what it implies about the
   cogito. The book's claims about freedom rest on its claims about the body
   and about time, and he says so.
4. The Preface is the hardest place to begin, and the Subject begins there
   only because the book does. It is commonly said to have been written after
   the rest (check against the edition's front matter), and it may be read
   after the book; Classical Prejudices does not depend on its labs.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Classical
> Prejudices uses the Preface's idea of description; The Lived Body uses the
> Introduction's two opponents; The Expressive Body extends the body schema;
> Sensing and Space and Things, the World and Others re-read perception from
> the body; The Cogito, Time and Freedom uses all of it.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what the lesson states: an angular size is a
> size over a distance, a luminance is a reflectance times an illumination, an
> account's record is a count over the cases. Nothing is rounded except where a
> lesson says so. Quotations are short extracts from Colin Smith&rsquo;s translation,
> quoted for commentary. What the labs cannot do is compute an experience
> &mdash; and that is what the book is about.

---

## §B The seven courses

| # | slug | title | the book | lessons | level |
| --- | --- | --- | --- | --- | --- |
| 1 | `perception-what-phenomenology-is` | What Phenomenology Is | Preface | 4 | Beginner |
| 2 | `perception-classical-prejudices` | Classical Prejudices | Introduction, I–IV | 5 | Beginner |
| 3 | `perception-the-lived-body` | The Lived Body | Part One, introduction and Chapters 1–3 | 8 | Intermediate |
| 4 | `perception-the-expressive-body` | The Expressive Body | Part One, Chapters 4–6 | 4 | Intermediate |
| 5 | `perception-sensing-and-space` | Sensing and Space | Part Two, introduction and Chapters 1–2 | 8 | Intermediate |
| 6 | `perception-things-world-and-others` | Things, the World and Others | Part Two, Chapters 3–4 | 7 | Advanced |
| 7 | `perception-cogito-time-and-freedom` | The Cogito, Time and Freedom | Part Three, Chapters 1–3 | 8 | Advanced |

Total 44. Part One is split where the book turns from the body's spatiality,
motricity and habit (Chapters 1–3, habit closing Chapter 3) to the body's unity
and its expressive life (Chapters 4–6: the body as a work of art, as sexed, as
expression and speech); Part Two where it turns from the senses and space to
the thing and other people. Every course name is the reader's, not the book's,
because the book's Parts are named *The Body*, *The Perceived World* and
*Being-for-Itself and Being-in-the-World*, and "The Body" alone would not tell
a reader which half they are in. The course `summary` names the Part exactly,
and gives each chapter's full title as the source edition prints it.

Chapter splits (one hard idea per lesson): Preface (four lessons), Part One
Chapter 1 (two), Chapter 3 (four: the schema, Schneider, the intentional arc,
habit), Chapter 6 (two); Part Two Chapter 1 (three), Chapter 2 (four, one per
section), Chapter 3 (five), Chapter 4 (two); Part Three Chapter 1 (three),
Chapter 2 (three), Chapter 3 (two). Every other chapter, and each untitled Part
introduction, is one lesson. Two adjacent chapters are never merged into one
lesson; where a chapter is short (Part One Chapter 4) its lesson is short.

The `perception-` prefix keeps course slugs from colliding with generic names
other Subjects use and tells a reader landing on a course URL which book it
belongs to. Check ids take the form `phen-course7-lesson-<lesson-slug>`
(20 characters before the slug); every lesson slug in §C is at most 42
characters, so every check id is at most 62, inside the 72-character cap, and
every slug is inside the 48 the lesson table allows.

**Module names.** A module name is never shortened by cutting. Each is the
book locator and a fixed short form from the table below, every one at most 60
characters. The short forms are the spec's; the full titles are copied from the
Smith table of contents into the course `summary` (§E.2), and where the
edition's heading differs from the wording given in the right-hand column
(Smith's and Landes's headings differ in places: "Up and Down" may read "High
and Low"), the module keeps the short form and the summary carries the
edition's wording. The French has no lettered sections; the module names below
do not use letters.

| book | module name |
| --- | --- |
| Preface | `Preface` |
| Introduction, I | `Introduction · I · Sensation` |
| Introduction, II | `Introduction · II · Association and Memory` |
| Introduction, III | `Introduction · III · Attention and Judgment` |
| Introduction, IV | `Introduction · IV · The Phenomenal Field` |
| Part One, introduction | `Part One · Experience and Objective Thought` |
| Part One, Chapter 1 | `Part One · 1 · The Body as Object` |
| Part One, Chapter 2 | `Part One · 2 · The Experience of the Body` |
| Part One, Chapter 3 | `Part One · 3 · Spatiality and Motility` |
| Part One, Chapter 4 | `Part One · 4 · The Synthesis of One's Own Body` |
| Part One, Chapter 5 | `Part One · 5 · The Body in its Sexual Being` |
| Part One, Chapter 6 | `Part One · 6 · Expression and Speech` |
| Part Two, introduction | `Part Two · The Theory of the Body` |
| Part Two, Chapter 1 | `Part Two · 1 · Sense Experience` |
| Part Two, Chapter 2, its four sections | `Part Two · 2 · Space · Up and Down`, `· Depth`, `· Movement`, `· Lived Space` |
| Part Two, Chapter 3, constancies | `Part Two · 3 · The Thing · Constancies` |
| Part Two, Chapter 3, the thing | `Part Two · 3 · The Thing · The Real` |
| Part Two, Chapter 3, the natural world | `Part Two · 3 · The Thing · The Natural World` |
| Part Two, Chapter 3, hallucination | `Part Two · 3 · The Thing · Hallucination` |
| Part Two, Chapter 4 | `Part Two · 4 · Other Selves and the Human World` |
| Part Three, Chapters 1–3 | `Part Three · 1 · The Cogito`, `Part Three · 2 · Temporality`, `Part Three · 3 · Freedom` |

---

## §C Every lesson

Format as `docs/capital/PLAN.md` §C:

- **slug** — Title — *module*
- **Read:** where the opening passage is, by section and subject.
- **Do:** the observable objective; `standard` measures it.
- **Lab:** mode/view; presets and their instances; the model the `panel_intro`
  names.
- **Misconception:** the wrong model `mistakes[0]` names and refutes.
- **Worked:** the single worked example, in one line.

**Read lines are pointers, never quotations.** This document puts no words of
the book in quotation marks; its quotation marks enclose a misconception's
wording, a preset's sentence, a lab label or a model's name, never the book's. Where it names a phrase the lesson will read
closely, it gives it in italics as a term or paraphrases it, and marks it
*(wording to be checked against the text)*; the words on the page come only
from the source edition (§E.2), copied from it. "Check against text" after a
location or an observation means the accuracy review was not certain of it
and the author settles it from the edition before the lesson is written.

Misconceptions are misreadings of the chapter — what Merleau-Ponty is taken to
say and does not — or the opponent's position stated at its strongest before
the chapter answers it. They are never verdicts on which school of philosophy
or psychology is right. Where a misconception is a position someone holds
(Descartes, Kant, Husserl, Sartre, the Gestalt psychologists, the
physiologists), the lesson names its holder.

Preset ids are suggestions; the INSTANCES are not optional. Where an entry
leaves an instance to the author, the id is a placeholder: the author designs
the instance, records it here in the same commit, and a reviewer rejects a
lesson whose entry still carries a bare id. **For `cases` this does not
apply: the accounts and at least three observations are listed below now**,
because they are the lesson's content. The cells marked "proposed coding" are
a starting point for the author, who checks each against the text and records
any change here.

In every `cases` entry the accounts are a cfg key fixed for the lesson; presets
vary only which observations are shown (§D, `cases`).

### Course 1 — What Phenomenology Is (`perception-what-phenomenology-is`, 4)

Preface. The four lessons follow the Preface's own topics: description, the
reduction, essences, intentionality — and its closing claim about rationality
and the unfinished. None of the Preface's four labs comes from its text; the
Preface has no cases or figures. The course `summary` says the labs illustrate
the method rather than the Preface's own examples, and its `how_to` says the
Preface may be read after the book and that Classical Prejudices does not
depend on its labs.

1. **description-not-explanation** — Description, Not Explanation — *Preface*
   - **Read:** the opening question, what phenomenology is, and the demand to
     describe rather than explain or analyse; the comparison of scientific
     knowledge with geography and of the perceived world with the countryside
    ; the Preface's charge that a
     science which forgets the perceived world it presupposes is both naïve and
     dishonest.
   - **Do:** compute the moon's angular size at the horizon and overhead and
     state which question the figures answer and which they do not.
   - **Lab:** `size/angle` (family 1: geometric optics). The moon is the
     lesson's illustration, not the Preface's: the prose says so and says the
     book treats the horizon moon later, in both places (checked against Smith:
     Introduction III, pp. 32 and 36, where it is first the intellectualist's
     example and then turned against both opponents; Part Two Chapter 2, Depth,
     p. 302). Presets: `horizon` (moon 3,474 km at 384,400 km — modern
     astronomy's figures, labelled so), `zenith` (the same moon about one Earth
     radius nearer, 378,029 km: slightly *larger* in angle overhead), `disc` (a
     7 mm disc held at 77 cm, illustrative: `1/110` rad covers the horizon
     moon's `0.0090` and falls just short of the overhead moon's `0.0092`).
     Pins the ratio and degree tiles.
   - **Misconception:** "Phenomenology rejects science." Refuted by the
     Preface's geography comparison: the scientific figure is a second-order
     expression of a world already perceived — naïve and dishonest when it
     forgets that, but not false. The lab keeps the figures to show that
     nothing in them is denied.
   - **Worked:** 3,474 / 384,400 = 1737/192200 ≈ 0.0090 rad ≈ 0.52° at the
     horizon; 3,474 / 378,029 ≈ 0.0092 rad ≈ 0.53° overhead; the horizon moon
     still looks larger.

2. **the-reduction-and-its-limit** — The Reduction and Its Limit — *Preface*
   - **Read:** the reduction as a loosening of the threads that attach us to
     the world, so that they show (*intentional threads*, wording to be checked
     against the text); Eugen Fink's remark about wonder before the world; the
     claim that the most important lesson of the reduction is the
     impossibility of a complete reduction *(wording to be checked against the
     text)*.
   - **Do:** show that one drawing is consistent with two solids and name what
     the drawing does not decide.
   - **Lab:** `perspective/necker` (family 1: parallel projection). The
     reversible cube is the lesson's illustration of what habit had supplied;
     the Preface has no drawing. The prose cites the book's own reversible
     figure: Part Two Chapter 2, Depth, p. 306, Fig. 1 (checked against Smith:
     a cube seen from below, from above, or as a flat mosaic of ten triangles
     and a square). Presets: `cube` (a wire
     cube, offset 1/2: both readings draw the identical 12 edges), `box` (a wire
     2 × 1 × 1 box: the same), `solid` (a solid cube: 9 edges drawn, and the
     other reading draws a different 9: one reading only). Pins the
     readings-count tile.
   - **Misconception:** "The reduction doubts the world exists, as Descartes
     doubted." Merleau-Ponty's Husserl suspends our complicity with the world
     in order to see it; it does not withdraw belief, and he says it cannot be
     completed. The lab: nothing about the drawing is doubted; what shows is
     the setting habit had supplied.
   - **Worked:** the cube and its mirror image in the plane across the line of
     sight draw the same twelve edges; which square is in front is not in the
     drawing.

3. **essences-and-existence** — Essences and Existence — *Preface*
   - **Read:** essences as a means, not the end; the remark about the Vienna
     Circle and the word *consciousness* (checked: p. xvi); the world as
     what I live through rather than what I think *(wording to be checked
     against the text)*.
   - **Do:** compute the invariant core of a set of free variations and say
     which variant left the kind.
   - **Lab:** `variation` (family 2). Presets: `sound` (a tone varied in pitch,
     loudness, timbre and duration; duration zero is no longer a sound — the
     lesson's illustration of Husserl's free variation, not the book's),
     `table` (a table varied in material, height and legs; a table with no top),
     `melody` (a melody transposed: every note changes, the intervals do not —
     Christian von Ehrenfels's example (1890), taken up by the Gestalt
     psychologists). Pins the invariant-core tile. As authored: `sound` is five
     tones (pitch 220 or 880, soft or loud, flute or violin, each with
     `some-duration`) and a sixth, `no duration`, marked no; `table` is oak,
     steel and tripod tables and `no top`, marked no; `melody` is the first
     three notes in C (C E G), D (D F-sharp A) and B flat (B-flat D F), each
     `major-third-up minor-third-up`, chosen so that no note is shared with
     the C version, plus `C notes backwards` (G E C), marked no: every note
     kept and the core lost. Pins vrCore and vrBreak.
   - **Misconception:** "Phenomenology is the study of essences, so it ends
     where the invariant is found." The Preface says essences are the means by
     which existence is brought into view; the core the lab prints is a tool,
     and the melody preset shows why: what stays is a relation, not a part.
   - **Worked:** across five variations of the tone, pitch, loudness and timbre
     all vary; having some duration stays.

4. **intentionality-and-rationality** — Intentionality and Rationality — *Preface*
   - **Read:** act intentionality and *operative* intentionality (checked:
     Smith's terms are *intentionality of act* and *operative
     intentionality*, p. xx);
     rationality as perspectives that confirm one another (p. xxii); the
     closing comparison with Balzac, Proust, Valéry and Cézanne (checked:
     p. xxiv).
   - **Do:** compute which faces of a cube several viewpoints see, and whether
     what each viewer reports seeing is consistent with one cube.
   - **Lab:** `perspective/faces` (family 1). Presets: `three` (views
     `1 2 2` front-right-above, `-2 1 -2` back-left-above and `front`: 3, 3
     and 1 faces; union 5 of 6; no view sees `below`), `two` (`front` and
     `back`: 1 face each, union 2), `conflict` (the `three` views, with the
     first viewer reporting `front, right, below`: inconsistent, and the tile
     names the face that view cannot see). Pins the union and the consistency
     tiles.
   - **Misconception:** "Rationality is guaranteed by a viewpoint above all
     viewpoints, from which each view can be checked." This is the absolute
     spectator of idealist reflection, which the Preface attacks: a mind that
     places itself at the origin of the world and surveys it from nowhere
     (checked: Smith's Preface does not use *pensée de survol* or a
     rendering of it; it names the *impartial spectator*, p. xxii, and the
     idealism of p. xiii, and the lesson describes the view in those terms.
     The *house seen from nowhere* is Part One's introduction, p. 77). On the Preface's
     account there is no view from nowhere to check the views against;
     rationality is the fact that they confirm one another, which is all the
     lab can compute.
   - **Worked:** `1 2 2` sees right, above and front, foreshortened 1/3, 2/3,
     2/3; `-2 1 -2` sees left, above and back; together 5 of 6; no view sees 6.

### Course 2 — Classical Prejudices (`perception-classical-prejudices`, 5)

Introduction, sections I–IV. The two opponents are built up first and then
taken apart: empiricism's sensation, association and projection of memories;
attention, as both accounts conceive it, and intellectualism's judgement. The
Introduction's thesis is that the two fail symmetrically, from one shared
prejudice in favour of the objective world, and the course's last lesson is
coded so as not to say otherwise.

1. **the-idea-of-pure-sensation** — The Idea of Pure Sensation — *Introduction · I · Sensation*
   - **Read:** the white patch on a homogeneous background; the perceptual
     something that is always in the middle of something else (check against
     text).
   - **Do:** compute the grouping proximity predicts for a row of dots and say
     what a pure-sensation account must add to get it.
   - **Lab:** `grouping` (family 1: the Gestalt proximity rule, Wertheimer
     1923, named as such). Presets: `pairs` (dots at 0, 1, 4, 5, 8, 9: three
     pairs), `even` (0, 2, 4, 6, 8: one group), `shift` (0, 1, 4, 6, 8, 9 —
     the dot at 5 moved to 6: gaps 1, 3, 2, 2, 1, and the middle pair breaks
     into two single dots: four groups). Pins the groups tile.
   - **Misconception:** "A sensation is the simplest thing perception gives,
     so experience is built from such units." The chapter's claim is that the
     unit is a construction: the simplest thing perceived is already a figure
     on a ground. The lab: the groups are relations between dots and are not
     in any dot.
   - **Worked:** gaps 1, 3, 1, 3, 1; with the threshold at twice the smallest
     gap, three pairs.

2. **the-constancy-hypothesis** — The Constancy Hypothesis — *Introduction · I · Sensation*
   - **Read:** the constancy hypothesis — that a stimulus and the elementary
     perception correspond point for point — under Köhler's name for it
     (*Konstanzannahme*, 1913), which Merleau-Ponty adopts; the Müller-Lyer
     figure, whose lines the chapter describes as neither equal nor unequal
     *(wording to be checked against the text)*.
   - **Do:** compute the constancy hypothesis's prediction for two stimuli and
     the gap to a reported percept.
   - **Lab:** `stimulus/illusion` (family 1: "the constancy hypothesis
     (Köhler's term)"). Presets: `muller` (shafts 10 cm and 10 cm with fins,
     reported difference 2 cm, illustrative — the lesson says the magnitude
     varies with the fins), `equal` (no fins: predicted and reported agree),
     `context` (one shaft 10 cm shown first with outward fins, then with
     inward: the same local stimulus, two reports — exactly what the hypothesis
     forbids). Pins the predicted, reported and gap tiles.
   - **Misconception:** "The Müller-Lyer lines really look unequal, so
     perception is simply mistaken." Merleau-Ponty's point is not that
     perception errs but that the question of equal or unequal belongs to the
     objective world; in the perceived field the lines are not yet comparable
     in that way. The lab can only print the objective comparison.
   - **Worked:** 10 cm and 10 cm predict a difference of 0; reported 2 cm;
     the gap is "the illusion" only if the measured lines are the standard.
   - This course's one modern aside (§F.1), if used, is here, in the `note`:
     predictive-processing theories also reject the constancy hypothesis,
     because expectations shape the percept; they differ from Merleau-Ponty,
     and among themselves, on whether what replaces it is inference.

3. **association-and-the-projection-of-memories** — Association and the Projection of Memories — *Introduction · II · Association and Memory*
   - **Read:** association by contiguity and resemblance; reading a word with
     a misprint or a missing letter, where memory is said to fill in what was
     not seen (check against text).
   - **Do:** count the remembered words that fit a partly seen word, then
     after the context arrives, and say which did the selecting.
   - **Lab:** `cues/pattern` (family 1: the associationist account). One
     remembered-word list for every preset, recorded here: `house, horse,
     gate:door, game, gave, have, hate, lake:water, make, name, same, take,
     cake, late, sale, tale, wave, cane, date, page:book` (20 words; a context
     tag is attached to at most one word). Presets: `misprint` (pattern
     `ho_se`; the printed word was *hoxse*: house and horse fit, 2),
     `wide` (pattern `_a_e`: 18 fit), `context` (pattern `_a_e`, context
     `door`: 1 fits — gate). Pins the count and the candidates tiles.
   - **Misconception:** "Memory supplies what the senses leave out." The
     chapter's objection is that to call up the right memory the perceived
     word must already have the shape that memory is said to give it; the lab
     shows the memories do not select themselves — the pattern and the context
     select.
   - **Worked:** `ho_se` fits two remembered words and `_a_e` eighteen; the
     letters alone cannot choose, and the sentence the word sits in does.

4. **attention-and-judgment** — Attention and Judgment — *Introduction · III · Attention and Judgment*
   - **Read:** attention as the empiricist's searchlight that changes nothing
     it lights, and as the intellectualist's discovery of what was already
     constituted — sterile in both; judgement as what the intellectualist adds
     to sensation; Descartes seeing hats and coats from the window and judging
     there are men, beside the wax (check against text); the walk along a shore
     towards a stranded ship whose masts and funnel merge with the forest
     behind it until, suddenly, they become part of the ship (check against
     text for the details).
   - **Do:** count the interpretations a judgement-from-signs account keeps as
     the cues arrive, and name the step at which the book's reorganisation
     happens with no cue to decide it.
   - **Lab:** `cues/sequence` (family 1: "perception as a judgement from
     signs"). Candidates: *trees at the forest's edge* (consistent with c1, c2),
     *masts and funnel of a ship* (c1, c2, c3). Cues: c1 tall vertical forms
     against the forest; c2 the same forms, nearer, no new detail; c3 a hull
     beneath them. Presets: `ship` (cues c1, c2: the model keeps 2 candidates
     at every step), `hull` (c1, c2, c3: 1 candidate at step 3). The step range
     runs 1..3 for every preset; in `ship` a step past 2 is clamped and the
     banner says so. Pins the count tile at steps 2 and 3.
   - **Misconception:** "Intellectualism and empiricism are opposites, so
     refuting one confirms the other." The chapter's claim is that both start
     from the same objective world and differ only in who builds the
     percept — the stimulus or the mind. The lab: on the judgement model the
     ship can only be concluded from a sign that excludes the trees; on the
     chapter's description the unity arrives before any such sign.
   - **Worked:** `ship`: 2 candidates after c1 and after c2 — the model never
     chooses, where the walker on the beach already sees a ship; `hull`: 1
     after c3.

5. **the-phenomenal-field** — The Phenomenal Field — *Introduction · IV · The Phenomenal Field*
   - **Read:** the return to the phenomenal field as the first step of
     phenomenology, and psychology's place in it.
   - **Do:** compute each classical account's record across the Introduction's
     cases, name the observations on which they part, and state the
     observation on which both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): empiricism, intellectualism.
     Observations (each to be checked against the text; proposed coding
     empiricism / intellectualism): (1) the Müller-Lyer lines (I): n / n — the
     constancy hypothesis predicts equality, and a judgement of inequality
     would be a judgement that deceives about what it sees; (2) the misprinted
     word read as the right word (II): n / y — association needs the shape it
     claims to supply, a judgement can interpret; (3) attention (III): n / n —
     sterile in both, it finds what was already there; (4) the ship on the
     beach (III): y / n — association can follow the details as they are
     added, a judgement has nothing new to conclude from. Presets (observation
     subsets): `intro` (all four), `sensation` (1 and 2), `judgement` (3 and
     4). The moon is not among these cases unless the author finds it in the
     Introduction. Pins the survivors and the splitting-case tiles.
   - **Misconception:** "The phenomenal field is a private inner world of
     appearances." The chapter places it before the split into inner and
     outer: it is the world as it is lived, not a mental picture of it.
   - **Worked:** four cases; survivors none; caSplit the misprint and the ship;
     both fail the Müller-Lyer and attention, where — the prose adds — both
     assume the objective world. The record is not a ranking, and the lesson
     says the split is its coding, not the book's.

### Course 3 — The Lived Body (`perception-the-lived-body`, 8)

Part One, its introduction and Chapters 1–3, habit included: the
acquisition of habit closes Chapter 3.

1. **experience-and-objective-thought** — Experience and Objective Thought — *Part One · Experience and Objective Thought*
   - **Read:** the house seen from nowhere, and the objects that see each
     other (the lamp; check against text); the object as a horizon of views.
   - **Do:** compute which faces of a house four views see, find the smallest
     set of views that sees every face any of them sees, and state that the
     house is the system of views, none of them privileged.
   - **Lab:** `perspective/faces` (family 1) with a house (a box 4 wide,
     3 deep, 2 high; the author's figures). Presets: `street` (`0 3 4`, from a
     window across the street: front and roof), `garden` (`0 3 -4`: back and
     roof), `above` (`above`: roof only), `everywhere` (`0 3 4`, `0 3 -4`,
     `1 2 2` named east, `-1 2 -2` named west: union 5 of 6 — every face but the
     one it stands on).
     Pins peUnion, peMax and peCover.
   - **Misconception:** "The house itself is the view from nowhere, and each
     view is a distortion of it." The chapter reverses it: the house seen from
     nowhere is what objective thought puts in place of the house.
   - **Worked:** `everywhere`: union 5 of 6 (the ground face never); no view
     sees more than 3; the smallest cover is the two corner views, east and
     west.

2. **the-phantom-limb** — The Phantom Limb — *Part One · 1 · The Body as Object*
   - **Read:** the phantom limb, and the failure of both the physiological and
     the psychological explanations of it.
   - **Do:** compute each explanation's record over the chapter's observations
     and name the observation each cannot absorb.
   - **Lab:** `cases` (family 2). Accounts (cfg): the physiological
     explanation, the psychological explanation — the chapter's explicit
     targets. Observations (each to be checked against the text; proposed
     coding physiological / psychological): (1) cutting the sensory paths to
     the brain abolishes the phantom: y / n; (2) an emotion, or a circumstance
     that recalls the wound, makes a phantom appear in a patient who had none:
     n / y; (3) the phantom keeps the posture of the arm at the moment of the
     injury: n / y; (4) the phantom shrinks and is absorbed into the stump
     over time: - / y. Presets: `all`, `nerves` (1 only), `memory` (2 and 3).
     Merleau-Ponty's account — the phantom as a refusal of mutilation by a
     being-in-the-world that keeps its field of action open — is in the prose.
     Pins the survivors and the splitting-case tiles.
   - **Misconception:** "The phantom is a mix of a nerve signal and a memory, so
     a combination of the two explanations suffices." The chapter argues the
     two cannot be added: one is third-person and the other first-person, and
     there is no common ground on which they meet.
   - **Worked:** physiological fails cases 2 and 3, psychological fails case 1;
     survivors none; split 1, 2, 3.
   - This course's one modern aside (§F.1), if used, is here: Ramachandran's
     mirror box, with both caveats — the evidence for mirror therapy is mixed
     and mostly of low quality, and Ramachandran's explanation (visual feedback
     remapping a body image) is closer to the *image* reading of the body
     schema that Chapter 3 rejects.

3. **the-habitual-body** — The Habitual Body — *Part One · 1 · The Body as Object*
   - **Read:** the layer of the habitual body and the layer of the present
     body; manipulable objects that appeal to a hand that is gone (*appeal*,
     wording to be checked against the text); anosognosia.
   - **Do:** compute which objects are within reach for the habitual body and
     for the present body and name those that appeal only to the first.
   - **Lab:** `schema/habitual` (family 3: the lesson's model). Presets: `cup`
     (habitual reach 70 cm both sides; present reach right 0, left 70; a cup on
     the right at 60 cm: within the habitual reach, not the present), `left`
     (the same cup on the left: both), `none` (no amputation: the two bodies
     agree).
   - **Misconception:** "The amputee does not know the arm is gone." The
     chapter says the patient knows it, as one knows a fact, and still counts
     on the arm, as one is open to a situation: two layers, not one
     ignorance. Anosognosia is read the same way.
   - **Worked:** habitual reach 70 cm includes the cup at 60 cm; present
     reach 0 cm on that side excludes it; the cup appeals only to the habitual
     body.

4. **the-permanence-of-ones-own-body** — The Permanence of One's Own Body — *Part One · 2 · The Experience of the Body*
   - **Read:** the body as never in front of me, always with me; its
     permanence against the permanence of objects; double sensations.
   - **Do:** compare the views available on an object with those available on
     one's own body and compute which faces each leaves unseen.
   - **Lab:** `perspective/own` (family 3: the lesson's model of the body as a
     rigid box seen from its own eyes). Presets: `object` (a box walked
     round: the six axis views; unseen none), `own` (the body as a box, seen
     only from where its eyes are: `0 3 4` down the front, `3 4 0` down the
     right side, `-3 4 0` down the left side; unseen back and below). Pins the
     unseen-faces tile. The `note` says what the rigid box leaves out (a foot
     can be lifted into view; the face cannot).
   - **Misconception:** "Touching one hand with the other is touching and
     being touched at once." The chapter says the two never coincide: the
     roles alternate, and the touched hand never becomes the touching one in
     the same moment. The `note` says the late work (*The Visible and the
     Invisible*, on reversibility) develops this differently, so that a reader
     who knows it does not read it back into this book.
   - **Worked:** the box: 6 of 6 seen across the views; one's own body: 4 of 6,
     back and below never.

5. **the-body-schema** — The Body Schema — *Part One · 3 · Spatiality and Motricity*
   - **Read:** the body schema as more than an image or an association of
     parts; the spatiality of situation against the spatiality of position;
     *here*.
   - **Do:** compute an object's position relative to the body as the body
     turns and moves, against its position in the room, and name which stays
     fixed.
   - **Lab:** `schema/coordinates` (family 3). Presets: `still` (body at
     (0, 0) facing east, cup at room (2, 1)), `turn` (the body turns to face
     north: the cup's room coordinates fixed, its body coordinates turned),
     `walk` (the body moves 1 m east, facing east). Pins both coordinate tiles.
   - **Misconception:** "The body schema is a map of the body the brain
     consults." The chapter's claim is that it is the body's grip on its
     tasks, not a representation consulted before moving. The lab's own
     coordinates are such a map, and the `note` says so: the lab computes what
     the schema is *not*.
   - **Worked:** cup at room (2, 1); facing east it is ahead 2, left 1; facing
     north, ahead 1, right 2; after walking 1 m east, ahead 1, left 1.

6. **schneider-concrete-and-abstract-movement** — Schneider: Concrete and Abstract Movement — *Part One · 3 · Spatiality and Motricity*
   - **Read:** Gelb and Goldstein's patient: he performs concrete movements
     (taking a handkerchief from his pocket, reaching the place where a
     mosquito bites) but cannot point to a part of his body on command or
     perform an abstract movement except by preparatory movements. The lesson
     says in a sentence that the book's argument concerns the case as Gelb and
     Goldstein reported it (§G).
   - **Do:** classify each task by the frame its target is given in, compute
     the conversion an objectively given target needs, and name the task that
     separates grasping from pointing.
   - **Lab:** `schema/coordinates` with the per-object field `given`
     (family 3: the lesson's model of the chapter's distinction between a
     target given in the body's situation and a target given as a position in
     objective space). Presets: `tasks` (handkerchief in the pocket, `given:
     body`; the bitten place, `given: body`; the nose, on command, `given:
     objective`), `turned` (the same, with the body turned a right angle: the
     objective target's body coordinates must be recomputed, the body-given
     ones need none), `eyes` (the command target alone). Pins `scFrame`.
   - **Misconception:** "Schneider's trouble is a visual deficit, so it is a
     problem of seeing and not of moving." The chapter takes up this reading
     (his injury was occipital) and argues it does not cover the case: the
     deficit is in the power of projecting a motor situation, of taking the
     body as a place among places on command.
   - **Worked:** the handkerchief and the bite: given in the body's situation,
     no conversion; the nose on command: given as an objective position,
     conversion needed — the one task, on Gelb and Goldstein's report, he
     cannot do.

7. **the-intentional-arc** — The Intentional Arc — *Part One · 3 · Spatiality and Motricity*
   - **Read:** the *intentional arc* that projects around us our past, our
     future and our human setting; motricity as original intentionality; the
     *I can*; Schneider's thinking — he cannot grasp an analogy or the point of
     a story unless he reconstructs it explicitly (check against text).
   - **Do:** compute the two classical accounts' records over the Schneider
     cases and name the observations each fails.
   - **Lab:** `cases` (family 2). Accounts (cfg): mechanistic physiology
     (movement as chains of reflexes along damaged or intact pathways);
     intellectualism (the loss of the symbolic function — Cassirer — or of the
     categorial attitude, Gelb and Goldstein's own term). Observations (each to
     be checked against the text; proposed coding physiology /
     intellectualism): (1) concrete movements are done: y / n — if every
     movement needs a representation, these should be lost too; (2) he cannot
     point on command to a part of his body: n / y — the same muscles and the
     same lesion serve both acts; (3) abstract movements succeed only after
     preparatory movements of the whole body: n / n; (4) he grasps an analogy
     or a story only by explicit reconstruction: - / y. Presets: `all`,
     `movement` (1–3), `thinking` (4). Motor intentionality is in the prose.
     Pins the survivors and the splitting-case tiles.
   - **Misconception:** the mechanistic physiologist's view at strength:
     "Every directed movement is a chain of reflexes triggered by stimuli;
     *directedness* is the observer's description of the chain." The chapter's
     claim is that the movement is directed — at a task, a situation — in a way
     the chain cannot be, because the same stimulus produces different
     movements as the task changes.
   - **Worked:** physiology fails 2 and 3, intellectualism fails 1 and 3;
     survivors none; split 1 and 2; both fail the preparatory movements.

8. **habit-and-the-blind-mans-cane** — Habit and the Blind Man's Cane — *Part One · 3 · Spatiality and Motricity*
   - **Read:** the closing pages of Chapter 3 on acquiring a habit as a
     reworking of the body schema: the woman with a feather in her hat, the
     car through a gateway, the typist, the organist who adapts to an
     unfamiliar organ in a short practice, the blind man's stick (check the
     organist's figures against the text).
   - **Do:** compute the reach and clearance of a body extended by a tool and
     a hat, and say what has changed when the habit is acquired.
   - **Lab:** `schema/tool` (family 3: the lesson's model). Presets: `hand`
     (reach 70 cm), `cane` (cane 100 cm: reach 170 cm), `hat` (a 165 cm head
     with a 30 cm feather, 195 cm, under a 200 cm door: clears by 5 cm), `car`
     (a car 180 cm wide through a 200 cm gateway: clears by 20 cm). The prose
     says the lab does the comparison the chapter says she does not make: she
     clears the door without calculating.
   - **Misconception:** "Habit is a reflex learned by repetition, an
     association of stimulus and response" (the associationist and
     conditioned-reflex psychology of habit). The chapter: acquiring a habit is
     grasping a significance, a knowledge in the hands; the organist learns a
     new organ without learning a new set of reflexes.
   - **Worked:** 70 + 100 = 170 cm; a kerb at 150 cm is within reach of the
     cane, not the hand.

### Course 4 — The Expressive Body (`perception-the-expressive-body`, 4)

Part One, Chapters 4–6.

1. **the-body-as-a-work-of-art** — The Body as a Work of Art — *Part One · 4 · The Synthesis of One's Own Body*
   - **Read:** the body's unity, which is neither that of a physical object
     whose parts lie side by side nor that of a law; the comparison of the
     body with a work of art, a knot of living meanings *(wording to be checked
     against the text)*; the intersensory unity of the body; perceptual habit,
     and the stick again, now as an instrument of perception.
   - **Do:** compute what stays the same when one learned movement is made by
     different limbs, and name what does not.
   - **Lab:** `variation` (family 2). Presets: `signature` (one's signature
     written small on paper with the fingers, large on a blackboard with the
     arm, with the left hand, with a foot in sand; properties the muscles used,
     the letter shapes, the order of the strokes, their rhythm: the core is the
     shapes, the order and the rhythm, never a muscle), `muscles` (the same four
     coded only by the muscles used: core none), `tracing` (a slow tracing of
     the signature by someone else, marked not of the kind: it lacks the
     rhythm). The author checks whether the book's own example of a movement
     transferred across limbs is in this chapter; if not, the preset is the
     lesson's illustration and says so.
   - **Misconception:** "The body is one thing because its parts are joined
     like a machine's, or because the mind synthesises them under a law, as it
     unifies any object." The chapter rejects both: the unity is like a
     painting's or a piece of music's, in which the meaning is not separable
     from the parts that carry it.
   - **Worked:** four variants; the muscles vary in every one; the shapes, the
     order and the rhythm stay.

2. **the-body-as-a-sexed-being** — The Body as a Sexed Being — *Part One · 5 · The Body as a Sexed Being*
   - **Read:** Schneider's sexual life; sexuality as a way of being in the
     world; Binswanger's patient, the young woman who lost her voice after her
     mother forbade her to see the man she loved, and recovered it when the
     prohibition was lifted (check against text); the chapter's discussion of
     Freud.
   - **Do:** compute the two classical accounts' records over the chapter's
     cases and name the case both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): sexuality as an automatism
     (a reflex apparatus set off by stimuli); sexuality as representation (a
     consciousness of pleasure and of ideas that sets the apparatus going).
     Observations (each to be checked against the text; proposed coding
     automatism / representation): (1) Schneider: neither the sight of a body
     nor talk of sexual matters arouses him, though the apparatus is intact,
     and he can represent sex abstractly: n / n; (2) the aphonia goes when the
     prohibition is lifted: n / y — an idea changes and the symptom goes;
     (3) during the aphonia she cannot speak even when she wants to: y / n —
     no decision of hers holds the voice back. Presets: `schneider` (1),
     `aphonia` (2 and 3), `all`. The existential account — sexuality as an
     atmosphere coextensive with life, neither explaining existence nor
     explained by it — is in the prose, as is Freud, whom the chapter reads as
     already moving towards it.
   - **Misconception:** "Merleau-Ponty reduces sexuality to existence, or
     existence to sexuality." He says neither; the chapter's word is that they
     are interfused (*interfusion*, wording to be checked against the text),
     and he discusses Freud and historical materialism to make the point that
     one does not explain the other.
   - **Worked:** survivors none; split the two aphonia observations; both fail
     Schneider.

3. **speech-as-gesture** — Speech as Gesture — *Part One · 6 · Expression and Speech*
   - **Read:** the word has a meaning; speech does not translate a ready-made
     thought but accomplishes it; Gelb and Goldstein's amnesic aphasia and the
     colour-sorting test.
   - **Do:** compute a categorical sort of colour samples and a chain of
     concrete resemblances, and name the sample where they part.
   - **Lab:** `sorting` (family 3: the lesson's model of a sort by concrete
     resemblance, with its rule printed). Presets: `samples` (pale red red 9,
     mid red red 6, dark red red 3, pale green green 8, mid green green 5, brown
     brown 2, dark brown brown 1; start pale red), `lightness` (pale, mid and
     dark red only: the two sorts agree), `close` (dark red red 2, pale red red
     9, light red red 8, brown brown 2; start dark red: the chain goes to brown
     first).
   - **Misconception:** Gelb and Goldstein's reading, stated at strength:
     "The patient has lost the categorial attitude; his words are intact, but
     he can no longer subsume a sample under a category, so he sorts by
     concrete resemblance." The chapter takes this up and answers it: the word
     and the category are not two things, and the patient's loss of the word's
     living use is not a loss of an intellectual function behind it. The naive
     view — words are labels on categories that are still there — is
     `mistakes[1]`.
   - **Worked:** categorical: reds, greens, browns; the chain from pale red:
     pale red → pale green → mid red → mid green → dark red → brown → dark
     brown, leaving red at its first step.

4. **the-spoken-word-and-thought** — The Spoken Word and Thought — *Part One · 6 · Expression and Speech*
   - **Read:** the gestural meaning of words; emotions and their expression
     differ by culture — the angry Japanese who smiles, the Westerner who goes
     red and stamps or goes pale and hisses (check against text); the
     *speaking* and the *spoken* word (wording to be checked against the
     text).
   - **Do:** compute what bodily sign, if any, is common to the expressions of
     one emotion, and say what the common sign would have to be for the
     natural-sign view to hold.
   - **Lab:** `variation` (family 2). Presets: `anger` (three expressions of
     anger, each with its bodily signs: core none), `west` (the two Western
     expressions only: core none — even within one culture no sign is fixed),
     `smile` (a smile in anger and a smile in pleasure, the second marked not
     anger: the core of the anger variants is the smile, and vrBreak shows the
     pleasure smile lacks none of it — the sign does not decide the emotion).
     Prepares the honey and the hallucination lessons, which compute cores
     too.
   - **Misconception:** "Emotional gestures are natural signs, the same in
     every body, and words are conventional; so speech cannot be gesture"
     (the classical division of natural and conventional signs). The chapter:
     the gesture is no more a natural sign than the word is a mere convention;
     the arbitrariness of signs is not denied but placed.
   - **Worked:** three expressions of anger; no bodily sign in all three; the
     core is empty.

### Course 5 — Sensing and Space (`perception-sensing-and-space`, 8)

Part Two, its introduction and Chapters 1 and 2.

1. **the-body-and-perception** — The Theory of the Body Is Already a Theory of Perception — *Part Two · The Theory of the Body*
   - **Read:** the cube with six equal faces, which no perspective presents;
     the *already* of the title, which points back to Part One.
   - **Do:** compute the faces and foreshortenings a cube presents from three
     directions and say what "six equal faces" is a claim about.
   - **Lab:** `perspective/faces` (family 1). Presets: `square` (`front`: one
     face, foreshortening 1), `turned` (`3 0 4`, the view turned about the
     vertical by 3-4-5: front 4/5, right 3/5), `corner` (`1 2 2`: three faces,
     front 2/3, above 2/3, right 1/3).
   - **Misconception:** "The equal faces are what the cube looks like, once
     the distortions are corrected." The six equal faces are never seen; they
     are the thought of a cube seen from nowhere, and the chapter's claim is
     that the body is what makes a cube seen from somewhere a cube.
   - **Worked:** turned by 3-4-5, the two visible faces are foreshortened to
     4/5 and 3/5; from the corner, three faces, none at its true size.

2. **the-motor-physiognomy-of-colours** — The Motor Physiognomy of Colours — *Part Two · 1 · Sensing*
   - **Read:** Goldstein and Rosenthal's patients: with the arm held out and
     the eyes closed, red and yellow make it deviate outward, blue and green
     inward (check against text); sensation as communion (*communion*, wording
     to be checked against the text).
   - **Do:** compute what a pure-quality account predicts for the arm under
     two colours, and the gap to the deviation reported.
   - **Lab:** `stimulus/illusion` (family 1: "sensation as a pure quality,
     with no motor effect of its own"). Presets: `red-blue` (the arm's starting
     position the same, 0 cm, under both colours: predicted difference 0;
     reported difference, outward under red against inward under blue, 6 cm,
     illustrative), `same` (blue against blue: 0 and 0), `faint` (the colour
     too faint to be named, deviation still reported, illustrative; the
     author checks whether the chapter reports this). Pins the predicted and
     gap tiles.
   - **Misconception:** "The colour is seen first and then it affects the body."
     The chapter's claim is that the motor significance is part of the
     colour's appearance, not a consequence of it.
   - **Worked:** the pure-quality account predicts a difference of 0 cm; the
     reported deviation differs by 6 cm (illustrative); the gap is the motor
     physiognomy.

3. **the-anonymous-subject-of-sensing** — The Anonymous Subject of Sensing — *Part Two · 1 · Sensing*
   - **Read:** sensation as pre-personal and anonymous: one perceives in me,
     rather than I perceive *(wording to be checked against the text)*; I am
     no more the author of my sensations than of my birth or my death (check
     against text); sensing as a coexistence of sentient and sensible, the
     blue of the sky to which I give myself up (check against text for the
     wording about being the sky itself); the critique of reflective analysis.
   - **Do:** compute the two classical accounts' records over the chapter's
     observations about who senses, and name the observation both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): empiricism (sensation as an
     impression undergone, a state of the organism); intellectualism
     (sensation as a quality posited by a thinking subject, the *I think* that
     must be able to accompany it). Observations (each to be checked against
     the text; proposed coding empiricism / intellectualism): (1) I do not
     decide to see blue, and cannot date the act of seeing it in my personal
     history: y / n; (2) the sensible solicits an attitude of the body before
     it is a quality — to see blue I must look in a certain way: n / y — the
     mind's act gives the quality its sense; (3) sensing is a coexistence in
     which the sensible and the sentient each give the other what it has, and
     neither is first: n / n. Presets: `all`, `passivity` (1), `activity` (2
     and 3).
   - **Misconception:** "If one perceives in me, there is no subject of
     perception at all." The chapter's subject is not abolished but placed
     below the personal one: a bodily, general subject that has already taken
     sides with the world before I do.
   - **Worked:** survivors none; split 1 and 2; both fail the coexistence.

4. **the-unity-of-the-senses** — The Unity of the Senses — *Part Two · 1 · Sensing*
   - **Read:** the senses communicate; synaesthesia as the rule; the glass
     whose hardness and brittleness are seen and whose breaking sound is
     carried by the visible glass, beside the steel and the plane blade (check
     against text; the author also finds where the sentence about the glass's
     single manner of being falls and, if it is in Part Two Chapter 3 too,
     cites both pages); von Senden's congenitally blind patients after the
     operation.
   - **Do:** compute what is common to the glass as it is given to four
     senses, on two codings, and say which coding the chapter describes.
   - **Lab:** `variation` (family 2). Presets: `sense-bound` (the glass seen,
     touched, tapped, dropped, each coded with only the qualities of its own
     sense — transparent; smooth, cold; rings; shatters with a sound: core
     none), `chapter` (the same four coded as the chapter describes them, the
     hardness and brittleness seen, heard and felt: core brittle, hard).
   - **Misconception:** "Each sense has its own world, and the mind joins
     them." The `sense-bound` coding is that view, and its empty core is what
     it predicts; the chapter's description is the other coding. The operated
     blind must learn to see, but not to join two worlds.
   - **Worked:** sense-bound: no quality in all four; the chapter's coding:
     brittle and hard in all four.

5. **up-and-down** — Up and Down — *Part Two · 2 · Space · Up and Down*
   - **Read:** the chapter's opening rejection of space as a container or a
     form, and its distinction between spatialised and spatialising space
     (check against text); Stratton's inverting spectacles; Wertheimer's
     mirror, which shows a room tilted by 45° that after a few minutes
     suddenly rights itself; the spatial level.
   - **Do:** compute the perceived tilt as image tilt minus spatial level,
     period by period, under a sudden and under a gradual re-anchoring.
   - **Lab:** `level` (family 3: the lesson's model). Presets: `wertheimer`
     (image 45°, level 0, rule `switch` at period 3 — the period is
     illustrative, the suddenness is the book's: perceived 45, 45, 0, 0, 0),
     `stratton` (image 180°, level 0, rule `share` 1/2 per period —
     Stratton's 1897 experiment, eight days with the lens over one eye; the
     shorter 1896 trial is mentioned in prose; the gradual halving is the
     lesson's illustration, labelled so, and the prose says Stratton reported
     no clean re-inversion and that Merleau-Ponty reads him selectively:
     perceived 180, 90, 45, 45/2, 45/4), `none` (image 0, level 0: perceived 0
     at every period). Pins the perceived-tilt tile at periods 1 and 3.
   - **Misconception:** "Up is where the retinal image's top is." Stratton
     shows the image can be inverted and up re-established; Wertheimer that
     the level is not given by the image at all, and is re-anchored as a whole,
     not corrected bit by bit.
   - **Worked:** `wertheimer`: period 1, image 45°, level 0, perceived 45°;
     period 3, the level has jumped to 45°, perceived 0°.

6. **depth** — Depth — *Part Two · 2 · Space · Depth*
   - **Read:** depth is not breadth seen from the side; convergence and
     apparent size as signs of depth in the classical theory.
   - **Do:** compute convergence and disparity for two distances and state
     what the classical theory says the mind does with them.
   - **Lab:** `depth` (family 1: the classical theory of depth from signs).
     Presets: `near` (6.5 cm interocular, 50 cm and 60 cm), `far` (500 cm and
     600 cm), `interval` (500 cm and 510 cm), `equal` (50 cm and 50 cm:
     disparity 0). The prose compares presets; no tile does: `far`'s disparity
     is a tenth of `near`'s, and `interval`, the same 10 cm depth interval as
     `near` five metres off, gives 1/85 of it.
   - **Misconception:** "We see depth by calculating from convergence" —
     the theory of Descartes' *Dioptrics* and, with signs learned by
     association, of Berkeley's *New Theory of Vision*, which the chapter
     states and rejects; the lab computes the calculation it says nobody
     performs.
   - **Worked:** convergence 6.5 / 50 = 13/100 and 6.5 / 60 = 13/120 rad;
     disparity 6.5 · (1/50 − 1/60) = 13/600 ≈ 0.0217 rad.

7. **movement** — Movement — *Part Two · 2 · Space · Movement*
   - **Read:** Wertheimer's stroboscopic movement and his conclusion that it
     is a movement without a moving thing (*pure phi*); the chapter's answer —
     there is always something that moves, but it is not an object posited
     apart from the movement, and has no identity outside it (check against
     text); Zeno.
   - **Do:** compute the implied speed and whether an interval falls in the
     band in which motion is reported.
   - **Lab:** `motion/phi` (family 1: Wertheimer's bands). Presets:
     `simultaneous` (lights 5 cm apart, interval 20 ms), `optimal` (60 ms),
     `succession` (250 ms). The thresholds are labelled "as later textbooks
     report Wertheimer (1912); not in Merleau-Ponty", and the prose adds that
     the bands depend on distance and intensity (Korte's laws). Zeno's arrow
     is in prose, not in the lab.
   - **Misconception:** "Motion is a succession of positions of one identical
     thing" — the assumption Zeno's argument trades on and the classical theory
     keeps. The chapter does not answer it with Wertheimer's motion of nothing:
     what moves is indeterminate, given only in its moving.
   - **Worked:** 5 cm at 60 ms: 1/12 cm per ms, in the band; 250 ms: two
     lights, no motion.

8. **lived-space** — Lived Space — *Part Two · 2 · Space · Lived Space*
   - **Read:** night, the dream, myth and the space of patients Minkowski and
     Binswanger describe (Minkowski's *dark space*; check against text); space
     as the space of an existence.
   - **Do:** compute the two classical accounts' records over the chapter's
     cases and name the observation both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): empiricism (lived spatial
     meanings are feelings associated with a geometric percept);
     intellectualism (there is one space, constituted by thought; the lived
     spaces are confused thoughts of it). Observations (each to be checked
     against the text; proposed coding empiricism / intellectualism):
     (1) night is not an object before me but envelops me, a depth with no
     things in it: n / n; (2) for a patient the landscape closes in and
     threatens, though nothing in it has moved or changed size: y / n — a
     feeling can be associated with an unchanged percept, a confused thought of
     the one space cannot make space itself close; (3) in the dream, rising and
     falling carry the dreamer's mood and desire: n / y — the dream is an
     imagined representation, but no sensation in it is associated. Presets:
     `all`, `night` (1), `patients` (2 and 3).
   - **Misconception:** "Lived space is a subjective distortion of real
     space." The chapter: geometric space is a later and thinner structure,
     drawn from the space of an existence.
   - **Worked:** survivors none; split 2 and 3; both fail the night.

### Course 6 — Things, the World and Others (`perception-things-world-and-others`, 7)

Part Two, Chapters 3 and 4.

1. **size-and-shape-constancy** — Size and Shape Constancy — *Part Two · 3 · The Thing · Constancies*
   - **Read:** perceptual constancies; a coin seen obliquely; the size of a
     person across a room.
   - **Do:** compute what the retinal-image account and the unconscious-
     inference account each predict for the size of a distant person, and a
     Brunswik ratio from a reported size.
   - **Lab:** `size/constancy` (family 1: the retinal-image account and
     Helmholtz's unconscious inference, named; Brunswik's ratio named as the
     lesson's addition, later than the book). The prose says Description, Not
     Explanation computed an angular size and this lesson computes the two
     predictions from one. Presets: `far` (a person 170 cm at 8 m,
     standard distance 2 m, the distance assumed correctly; reported 160 cm,
     illustrative), `misjudged` (the same, distance assumed to be 4 m),
     `none` (reported 85/2 cm: ratio 0), `full` (reported 170 cm: ratio 1). A
     distance equal to the standard distance is refused with a sentence
     (nothing to correct). The coin is in prose: a disc tilted by 4-3-5
     (cos 3/5) projects axes 1 and 3/5.
   - **Misconception:** "The real shape and size are inferred from the
     projected ones" (Helmholtz). The chapter: the real size is not behind the
     appearance but is how the thing appears when seen at its best; the lab
     shows that the inference, done right, predicts full constancy, which is
     not what is reported either.
   - **Worked:** retinal-equivalent size at 2 m: 170 × 2/8 = 85/2 cm; inferred
     170 cm; reported 160 cm; Brunswik (160 − 85/2) / (170 − 85/2) = 47/51
     ≈ 92%.

2. **colour-and-lighting** — Colour and Lighting — *Part Two · 3 · The Thing · Constancies*
   - **Read:** Gelb's experiment (1929); the lighting as what we see by, not
     what we see; Katz's film and surface colours.
   - **Do:** compute luminances and ratios to the surround and name the change
     that makes Gelb's disc look black again.
   - **Lab:** `light` (family 1: luminance as the empiricist's sensation;
     the ratio to the surround named as Wallach's principle (1948), the
     lesson's addition). Reflectances illustrative, labelled so. Presets:
     `room` (white paper 4/5 × 1, black disc 1/20 × 1, wall surround 1/2 × 1),
     `gelb` (the disc in a hidden spotlight, 1/20 × 16 = 4/5; the white paper
     in the room, 4/5; the wall surround 1/2: disc and paper tie for
     brightest), `paper` (a scrap of white paper placed in the beam, 4/5 × 16
     = 64/5, as the surround: the disc's ratio falls to 1/16).
   - **Misconception:** "The disc looks white because it sends the eye white
     paper's light." Then it should stay white when the paper is added.
   - **Worked:** reflectance 1/20 × illumination 16 = 4/5, white paper's
     luminance in the room; its ratio to the wall 8/5, the paper's own; with
     the paper in the beam, (4/5) / (64/5) = 1/16.

3. **the-thing-and-the-real** — The Thing and the Real — *Part Two · 3 · The Thing · The Real*
   - **Read:** the thing as intersensory; honey, taken from Sartre's analysis
     of the viscous (check against text); the red of a woolly carpet, which
     would not be the same red if it were not woolly (check against text);
     the thing *in-itself-for-us* (wording to be checked against the text),
     which ignores us and rests in itself; Cézanne. The glass belongs to
     Sensing (The Unity of the Senses), and this lesson does not reuse it.
   - **Do:** compute the two classical accounts' records over the chapter's
     observations about the thing and name the observation each fails.
   - **Lab:** `cases` (family 2). Accounts (cfg): empiricism (the thing as a
     sum of sensory qualities, associated); intellectualism (the thing as a
     unity posited by thought, a law of its appearances). Observations (each to
     be checked against the text; proposed coding empiricism /
     intellectualism): (1) honey's slow fall, its stickiness and its sweetness
     are one way of being: n / y — the understanding can unify the qualities
     under a concept; (2) the carpet's red is a woolly red, not a red plus a
     woolliness: n / n; (3) the thing presents itself as indifferent to us,
     alien, resting in itself, as Cézanne paints it: y / n — sensations are
     given, not made, but a unity posited by thought is for thought. Presets:
     `all`, `qualities` (1 and 2), `alien` (3).
   - **Misconception:** "The real thing is the sum of its sensory qualities,
     held together by the mind." The table is the lab's half of the answer;
     the chapter's half, in prose, is that the unity is a style the qualities
     share, which is not one more quality and not a concept.
   - **Worked:** survivors none; split 1 and 3; both fail the woolly red.

4. **the-natural-world** — The Natural World — *Part Two · 3 · The Thing · The Natural World*
   - **Read:** the world as the horizon of all horizons; a perception corrected
     by another perception, never by leaving the world; the illusion of the
     broad flat stone on a sunken road that turns out to be a patch of
     sunlight (check against text: it may be in Part Three Chapter 1; if it is
     not in this chapter, the author uses this chapter's own example and does
     not import the stone without saying so).
   - **Do:** count the interpretations consistent with the cues as they
     arrive, and say what was never among the candidates.
   - **Lab:** `cues/sequence` (family 1: the sceptic's picture of perception
     as an interpretation that may always be false), the view Attention and
     Judgment used for the ship. Candidates: *a flat stone* (c1), *a puddle*
     (c1, c2), *a patch of sunlight* (c1, c2, c3). Cues (the second and third
     illustrative): c1 a pale flat shape on the road; c2 no edge lifts from
     the ground as I come near; c3 it trembles as the leaves above it move.
     Presets: `first` (c1 only), `all` (c1–c3). The step range runs 1..3 for
     both; in `first` a step past 1 is clamped and the banner says so.
   - **Misconception:** the Cartesian sceptic of the First Meditation:
     "Because any perception may turn out an illusion, all of them might."
     The chapter's reply is that an illusion is unmasked only by another
     perception, which counts on the world; the lab's candidates are all
     interpretations *of something there*.
   - **Worked:** three interpretations after c1, two after c2, one after c3;
     *nothing there* is never a candidate.

5. **hallucination** — Hallucination — *Part Two · 3 · The Thing · Hallucination*
   - **Read:** the patients who say their voices or visions are not like what
     they perceive; hallucination as lacking the perceived world's texture
     and depth, a pseudo-world (check against text).
   - **Do:** compute what every perceived thing has in common and what the
     hallucination lacks of it.
   - **Lab:** `variation` (family 2: the lesson's coding of the chapter's
     report). Presets: `voice` (a voice heard from the next room and a
     hallucinated voice), `vision` (a lamp seen and a hallucinated figure),
     `all` (three perceived things and one hallucination). Properties (the
     chapter's list, to be checked against the text): placed in the one
     public space, explorable, inexhaustible in detail, confirmed by the other
     senses, present to me. The empiricist account (a sensation from an inner
     cause) and the intellectualist account (a false judgement or belief) are
     stated at strength in prose; both make the hallucination a perception
     with something added or missing, where the patients report a different
     kind of thing.
   - **Misconception:** "A hallucination is a perception without an object, so
     it is experienced exactly as a perception." The chapter's patients say it
     is not.
   - **Worked:** `all`: the core of the perceived things is all five
     properties; the hallucination lacks the first four and keeps only
     *present to me*.
   - This course's one modern aside (§F.1), if used, is here, with both sides:
     Anil Seth's description of perception as a controlled hallucination (a
     phrase he credits to earlier users; check the attribution before
     printing) runs the other way from this chapter, which argues that a
     hallucination lacks what perception has, not that perception is a
     hallucination kept in check.

6. **the-cultural-world-and-others** — The Cultural World and Others — *Part Two · 4 · Others and the Human World*
   - **Read:** cultural objects; the argument from analogy and its circle.
   - **Do:** set out the argument from analogy and decide whether its premises
     force its conclusion.
   - **Lab:** `argkit/validity` (family 1). Presets: `analogy` (my body
     expresses my mind; that body is like mine; so that body expresses a
     mind — invalid in the propositional form the lab can state), `valid` (a
     deductive repair that adds the premise the argument needs), `circle` (the
     repair's premise is the conclusion).
   - **Misconception:** "The argument from analogy fails only because it is
     inductive." The chapter's objection is that it presupposes what it
     should explain: I would need to perceive the other as a behaviour first.
   - **Worked:** the `analogy` table's one countercase.

7. **the-truth-of-solipsism** — The Truth of Solipsism — *Part Two · 4 · Others and the Human World*
   - **Read:** the other's grief, which I see and do not live; a solipsism
     rooted in lived experience that cannot be surpassed (*lived solipsism*,
     wording to be checked against the text); the look that objectifies,
     Sartre's, and the chapter's answer that it does so only if both of us
     withdraw into our thinking natures (check against text); the social as a
     permanent field.
   - **Do:** compute two opponent accounts' records over the chapter's cases,
     name the case both absorb and the case both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): the argument from analogy
     (the other known by inference from behaviour like mine); Sartre's look
     (the other given directly, as a look that makes me an object). Scheler is
     named in prose. Observations (each to be checked against the text;
     proposed coding analogy / look): (1) the fifteen-month-old baby who opens
     its mouth when I playfully take its finger between my teeth, though it
     has hardly seen its own face: n / y; (2) the other's grief, which I see
     and do not live: y / y; (3) a conversation in which my thought and the
     other's are woven into one fabric: n / n; (4) the stranger's look that
     makes me feel an object, and stops doing so when we speak: - / y.
     Presets: `all`, `infant` (1), `dialogue` (2 and 3).
   - **Misconception:** "Merleau-Ponty refutes solipsism." He says there is a
     truth in it that cannot be overcome, and that coexistence is lived before
     and beneath it; both claims are in the chapter, and coexistence is in the
     prose, not the table.
   - **Worked:** survivors none; both absorb the grief — the truth in
     solipsism; both fail the dialogue; split the infant.

### Course 7 — The Cogito, Time and Freedom (`perception-cogito-time-and-freedom`, 8)

Part Three, Chapters 1–3.

1. **the-cogito-and-the-certainty-of-seeing** — The Cogito and the Certainty of Seeing — *Part Three · 1 · The Cogito*
   - **Read:** Descartes' distinction between seeing and the thought of seeing,
     which is certain even if the seeing is not; the chapter's reply that the
     two certainties cannot be separated; true and false feelings — a love
     that turns out not to have been love — showing that the certainty of an
     inner state is not given in advance either (check against text).
   - **Do:** set out the cogito read as an inference and decide what it needs
     to be valid.
   - **Lab:** `argkit/validity` (family 1). Presets: `bare` ("I think, so I
     exist": the form p, so q — invalid as stated), `major` (the instance, for
     me, of Descartes' general premise that whatever thinks exists: "if I
     think, I exist; I think; so I exist" — valid; the lab is propositional,
     so it states the instance, and the prose gives the general premise),
     `seeing` ("I think I see a lamp, so I see a lamp": invalid — the gap
     Descartes relies on).
   - **Misconception:** "The cogito is an inference from thinking to being."
     Descartes himself denied it in the Second Replies, calling it a simple
     intuition of the mind and saying the general premise is learned from the
     particular case (in the *Principles*, I.10, he allows the general premise
     as presupposed; the prose gives both). The lab shows why an inference
     would need a premise he treated as derived, and the chapter reads the
     cogito instead as the experience of thinking.
   - **Worked:** the `bare` table's one countercase; the `major` table's none.

2. **the-triangle** — The Triangle — *Part Three · 1 · The Cogito*
   - **Read:** the geometer's proof that a triangle's angles equal two right
     angles, by drawing a parallel through one vertex; the claim that the
     construction is a motor grasp of the figure, not a deduction from its
     definition.
   - **Do:** compute the third angle and the alternate angles of the
     construction at each vertex, and name what the construction adds to the
     definition.
   - **Lab:** `triangle` (family 3: Euclid's construction, drawn). Presets:
     `classic` (60°, 70°), `right` (90°, 30°), `thin` (1°, 1°), `refuse`
     (100°, 90°: no such triangle, refused with a sentence). The redraw-only
     `trVertex` select moves the parallel to each vertex in turn.
   - **Misconception:** "The angle sum follows from the definition of a
     triangle, as a consequence follows from axioms." Kant used exactly this
     proof, the parallel drawn through a vertex, as his example of
     construction in intuition (*Critique of Pure Reason*, A716–17/B744–45);
     Merleau-Ponty's reading competes with Kant's on Kant's own example: the
     proof needs the parallel to be drawn and the figure seen anew, and he
     reads that as the body's grasp, not as pure intuition.
   - **Worked:** 60 + 70 = 130; the third angle 50; at the parallel through
     the third vertex, 60 + 50 + 70 = 180, a straight angle; at either other
     vertex, a different pair of alternate angles and the same 180.

3. **the-tacit-cogito** — The Tacit Cogito — *Part Three · 1 · The Cogito*
   - **Read:** the spoken cogito, learned from books, and the tacit cogito
     beneath it, which words presuppose; expression and the eternal truths
     (Hegel, Valéry; check against text).
   - **Do:** compute two opponent accounts' records over the chapter's cases
     about language and thought, and name the case both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): thought before language
     (thought complete in itself, words its clothing); language before thought
     (thought nothing but words, inner speech). Observations (each to be
     checked against the text; proposed coding thought-first /
     language-first): (1) I understand Descartes' written cogito only because
     I already am a thinking being for whom it can mean something: y / n;
     (2) a speaker or a writer does not know what he thinks until he has said
     it: n / y; (3) I can be mistaken about my own feelings, as in a false
     love: n / - — an inner state is not transparent in advance. Presets:
     `all`, `books` (1), `expression` (2 and 3). The tacit cogito is in the
     prose.
   - **Misconception:** "The tacit cogito is a silent inner voice that thinks
     in words before speaking." The chapter says it is not yet a thought in
     words at all. The `note` says the reading is disputed by Merleau-Ponty
     himself: a working note of *The Visible and the Invisible* calls the tacit
     cogito impossible (check the wording before quoting).
   - **Worked:** survivors none; split 1 and 2; thought-first fails the false
     love, language-first is silent on it.

4. **time-is-not-in-things** — Time Is Not in Things — *Part Three · 2 · Temporality*
   - **Read:** the image of time as a river, and why it smuggles in an
     observer: what is past or future for me is present in the world, the
     water that will pass tomorrow already at its source (check against
     text).
   - **Do:** classify the river's water as past and future from two
     standpoints, then remove the standpoint and see what is left.
   - **Lab:** `time/river` (family 3: the lesson's model of the chapter's
     river). Presets: `bank` (water at positions 1 to 7 downstream, an
     observer on the bank at 4: the water downstream has passed — past 5, 6,
     7; future 1, 2, 3), `current` (the same water, the observer carried with
     it: the water ahead downstream is future — past 1, 2, 3; future 5, 6, 7),
     `none` (no observer: every parcel is present where it is, and past and
     future are empty).
   - **Misconception:** "Past and future are in the world, and we only
     observe them." The chapter: in things there is only the present of each;
     past and future need someone for whom they are past and future, and the
     two standpoints the lab computes give opposite answers from the same
     water.
   - **Worked:** observer at 4: on the bank, past 5–7 and future 1–3; with the
     current, the reverse; no observer, none of either.

5. **the-field-of-presence** — The Field of Presence — *Part Three · 2 · Temporality*
   - **Read:** Husserl's diagram of retention and protention, which the
     chapter reproduces; the *field of presence* (wording to be checked against
     the text).
   - **Do:** compute, for a present, the depth at which each earlier moment is
     retained, and the span of protention.
   - **Lab:** `time/diagram` (family 3: Husserl's diagram as the lesson's
     model). Presets: `three` (A, B, C, present C: A at depth 2, B at depth 1),
     `later` (present D: A 3, B 2, C 1), `span` (present C, a protention span
     of 2: D, E).
   - **Misconception:** "Retention is short-term memory, a stored copy of the
     moment just past." The chapter, after Husserl, says retention is not a
     copy recalled but the past held in the present's own thickness; recall
     is a different act.
   - **Worked:** at C, A is held at depth 2 through B's retention of it.

6. **time-as-subject** — Time as Subject — *Part Three · 2 · Temporality*
   - **Read:** the chapter's thesis that time must be understood as the
     subject and the subject as time *(wording to be checked against the
     text)*; passive synthesis; self-affection, with Kant and Heidegger;
     the priority of the present and the future (check against text).
   - **Do:** compute the diagram's column at each present in turn and show
     that one moment is held at a different depth in each while the order of
     moments never changes.
   - **Lab:** `time/ekstasis` (family 3: the lesson's model). Presets: `walk`
     (moments A–D, presents B, C, D in turn), `long` (A–F, presents B–F),
     `one` (a single present: the column alone, which the lesson says is
     what a line of nows mistakes for time).
   - **Misconception:** "The subject is in time as a thing is, or outside time
     looking on." The chapter: the subject is neither; it is the passage
     itself, which affects itself, and no single column is *the* time.
   - **Worked:** A is at depth 1 under B, 2 under C, 3 under D; in every
     column the order A, B, C is the same.

7. **the-rock-and-the-project** — The Rock and the Project — *Part Three · 3 · Freedom*
   - **Read:** a theory of absolute freedom, recognisably Sartre's in *Being
     and Nothingness* — the chapter states it largely without naming him in
     its body text (check against text and notes) — and the rock, Sartre's
     own example, that is unclimbable only for someone who means to climb it;
     the chapter's reply that some mountains look high even to someone with no
     plan to climb them (check against text).
   - **Do:** classify rocks as obstacles relative to a project and then
     relative to the body's own general level, and name the rock that is an
     obstacle on the second reckoning and not the first.
   - **Lab:** `schema/obstacle` (family 3: the lesson's model). Rocks 1 m,
     2 m and 3 m in every preset. Presets: `climb` (project climb, capacity
     2 m: the 3 m rock is an obstacle), `pass` (project walk past: none is),
     `body` (no explicit project, the body's general level 2 m: the 3 m rock
     still stands out).
   - **Misconception:** "Merleau-Ponty agrees with the theory of absolute
     freedom that obstacles exist only for a project." He agrees with the
     first half and denies the conclusion: the body gives a general valuation
     before any chosen project, which is why freedom is always in a field.
   - **Worked:** 3 > 2: an obstacle for climbing; with no project, none on the
     absolute-freedom reckoning and one on the body's.

8. **freedom-in-situation** — Freedom in Situation — *Part Three · 3 · Freedom*
   - **Read:** the worker who becomes revolutionary, neither by a decision
     from nowhere nor by objective conditions alone; the closing lines, which
     quote Saint-Exupéry.
   - **Do:** compute the records of determinism and absolute freedom over the
     chapter's cases, and name the case each fails and the case both fail.
   - **Lab:** `cases` (family 2). Accounts (cfg): determinism (conduct caused
     by objective conditions); absolute freedom (conduct chosen by a
     consciousness outside every situation). Observations (each to be checked
     against the text; proposed coding determinism / absolute freedom):
     (1) a man who has built his life for twenty years on an inferiority
     complex is unlikely to undo it by a decision in a moment: y / n; (2) the
     same hardship does not produce a revolutionary consciousness in everyone
     or at every time, and becomes unbearable only when a change is in view:
     n / y; (3) the day labourer finds himself a revolutionary before he has
     decided anything, in his coexistence with other labourers: n / n;
     (4) the prisoner who does not speak under torture holds out with his
     comrades, not alone: n / n. Presets: `all`, `past` (1), `class` (2 and
     3). Freedom in situation is in the prose.
   - **Misconception:** "Freedom in situation is a compromise: partly free,
     partly determined." The chapter rejects the arithmetic of a share
     without returning to totality: there is never determinism and never
     absolute choice, and I am free not in spite of my motives but by means
     of them *(wording to be checked against the text)*.
   - **Worked:** survivors none; split 1 and 2; both fail the labourer and the
     prisoner. The course ends where the book does.

---

## §D The lab kit: `phenkit`

### D.0 Conventions

Everything in `docs/philosophy/PLAN.md` §D.0 and the capkit conventions as
implemented (`docs/capital/kit-a-report.md`, "Conventions as implemented")
holds: one function `phenkit_lab(cfg)`; cfg keys `mode`, `view`, `presets`,
`preset`, `title`, `panel_title`, `panel_intro`; inputs are text boxes with id
`<prefix>In<Field>`; records are `a, 1, 2; b, 3, 4`; a preset menu
`<prefix>Preset`, a banner `<prefix>Status`, a table `<prefix>Table`; every
text box survives `''`, `banana`, `0`, `-1`, `1/0`, `A>B` with a red banner
and tiles blanked to `—`; build-time refusals for a preset key that is not an
input of its view, a size limit exceeded, an unknown view. Exact rationals
over BigInt (RATIONAL_JS); a percentage or degree printed beside its exact
fraction, marked `≈`; a fraction is always printed reduced. Each mode has one
pure `<xx>Compute(view, inst, opts)` that `scripts/mathcheck.js` calls in its
own block, each case seen to fail when its line is broken on purpose.
`phenkit` joins `KITS_WITH_EXPECTATIONS` at wiring.

**Page weight.** `phenkit_lab` emits the JavaScript of the active mode only,
plus the shared rational and banner helpers — never every mode's block. Page
budget: ≤ 40 KB gzipped per lesson.

**Exact tiles, approximate pixels.** Tiles are exact. An SVG may use
floating-point trigonometry for pixel coordinates only (the triangle's
vertices, the level's tilted room); no tile, status sentence or expectation is
ever derived from a drawing.

**No tile and no control depends on comparing presets.** A tile sees one
instance. A redraw-only control's options and range are fixed by the cfg, never
by the preset: a range's maximum is the largest any preset of the lesson needs,
a value past the current preset's data is clamped to its last value and the
banner says so in a sentence, and a preset's change handler never touches a
redraw-only control.

**The Pythagorean angles.** A turn or tilt input is one of a fixed list of named
angles whose cosine and sine are both rational. The name a-b-c means
cos = b/c, sin = a/c: `0` (1, 0), `3-4-5` (4/5, 3/5), `4-3-5` (3/5, 4/5),
`5-12-13` (12/13, 5/13), `12-5-13` (5/13, 12/13), `8-15-17` (15/17, 8/17),
`15-8-17` (8/17, 15/17), `90` (0, 1), `180` (−1, 0), `270` (0, −1). The tile
prints the exact cosine and the approximate degrees (`3-4-5: cos 4/5, ≈ 36.87°`;
`4-3-5` ≈ 53.13°, `5-12-13` ≈ 22.62°, `12-5-13` ≈ 67.38°, `8-15-17` ≈ 28.07°,
`15-8-17` ≈ 61.93°). Any other angle is refused with a sentence that lists the
allowed ones.

**One tilt convention.** A turn of a view about the vertical by θ is the
direction (sin θ, 0, cos θ) in the coordinates below. A tilt of a surface by θ
is the angle between the surface's normal and the line of sight; the surface's
extent along the tilt projects to cos θ of its true extent. So a disc tilted by
`3-4-5` projects axes 1 and 4/5, and by `4-3-5`, axes 1 and 3/5. A facing in
the plane (`schema`) is measured counter-clockwise from east: facing θ has
ahead-vector (cos θ, sin θ) and left-vector (−sin θ, cos θ).

**View directions.** Coordinates: x to the right, y up, z towards a viewer of
the front face. A view is one of the six names `front` (0 0 1), `back`
(0 0 −1), `right` (1 0 0), `left` (−1 0 0), `above` (0 1 0), `below` (0 −1 0),
or a whole-number triple `x y z`, each |component| ≤ 20, not all zero, whose
length √(x² + y² + z²) is a whole number, pointing from the object towards the
viewer. Every Pythagorean turn is one (`3 0 4`), and so is every Pythagorean
quadruple, which gives the corner views that see three faces: `1 2 2` (length
3), `2 3 6` (7), `1 4 8` (9), `4 4 7` (9), with any signs and in any order. Any
other triple is refused with a sentence that gives these as examples. A face is
visible from a view when its outward normal has a positive dot product with
the view; its foreshortening — its projected area as a fraction of its true
area, which for a face turned about one axis is its projected width — is that
dot product over the view's length, exact.

**Model names.** Every view's `panel_intro` names the model it computes (§0,
deviation 4), and in the third family says "the lesson's model". The kit
itself carries no claim that any model is right.

### D.1 Modes (prefix, views, inputs, tiles)

#### stimulus (`st`)
- `illusion`: `a` and `b` (the two measured magnitudes, with `unit`),
  `reported` (the reported difference, signed). Tiles: stPredicted (`a − b`,
  e.g. `0 cm` — what the named model predicts), stReported (`2 cm`), stGap
  (`reported − predicted`, `2 cm`).

#### grouping (`gr`)
- `proximity`: `points` (≤ 16 positions on a line), `ratio` (default 2: a gap
  at least ratio × the smallest gap separates groups). Tiles: grGaps
  (`1, 3, 1, 3, 1`), grGroups (`{0, 1} {4, 5} {8, 9}`), grCount (`3`). A strip
  of dots is drawn, coloured by group.

#### cues (`cu`)
- `pattern`: `words` (≤ 40, a word optionally tagged `gate:door`), `pattern`
  (letters and `_`), `context` (a tag or empty). Tiles: cuCount (`2`),
  cuCandidates (`horse, house`, in list order), cuContext (`gate`, or `—` when
  there is no context).
- `sequence`: `candidates` (≤ 8, each with the cue ids it is consistent with),
  `cues` (ordered, ≤ 6), `step` (redraw-only range 1..the longest cue list in
  the lesson's presets; clamped per D.0). Tiles: cuCount, cuCandidates,
  cuRemoved (the candidates the last cue removed, or `none`).

#### size (`sz`)
- `angle`: `size`, `distance`, `unit`. Tiles: szRatio (the ratio reduced,
  printed with four decimals: `1737/192200 ≈ 0.0090 rad`), szDegrees
  (`≈ 0.52°`).
- `constancy`: `size`, `distance`, `standard_distance`, `assumed` (the distance
  an inference assumes; default `distance`), `reported`. Refused when
  `distance = standard_distance`. Tiles: szRetinal (the size that would
  subtend the same angle at the standard distance — the retinal-image
  account's prediction, `85/2 cm`), szInferred (`size × assumed / distance` —
  the unconscious inference's prediction, `170 cm`), szBrunswik
  (`(reported − retinal) / (size − retinal)`, exact and as a percentage: `1` is
  full constancy, `0` none; `47/51 ≈ 92.2%`).

#### perspective (`pe`)
- `faces`: `object` (`cube`, or `box` with three dimensions), `views` (≤ 6,
  each a view direction, D.0, with an optional name and an optional
  `reports` list of the faces its viewer claims to see). Tiles: peVisible (per
  view, the faces seen and each one's foreshortening), peUnion (faces seen by
  some view, `5 of 6`), peMax (`3`), peCover (the smallest subset of the views
  whose union equals peUnion; among equal sizes, the first in list order:
  `east, west (2 views)`), peConsistent (`yes`, or `no` naming each view whose
  reports include a face its direction cannot see; `—` when no view carries
  reports).
- `own`: as `faces`, with the views restricted to the list the lesson gives.
  Tiles: peUnion, peUnseen (`back, below`).
- `necker`: `object` (`wire cube` | `wire box` with dimensions | `solid cube`),
  `offset` k (a rational, default 1/2). The drawing is the parallel projection
  along d = (k, k, 1) onto the picture plane, (x, y, z) ↦ (x − kz, y − kz).
  Reading A is the object; reading B its mirror image in the plane through the
  object's centre perpendicular to d (exact, since d is rational), which
  projects point for point onto A's drawing. A wire figure draws every edge; a
  solid draws only the edges of faces whose outward normal has a positive dot
  product with d. Tiles: peEdges (edges in A's drawing: `12`, or `9` for the
  solid cube), peReadings (`2` when B's drawing is the identical edge set,
  else `1`), peSame (`identical drawings` | `different drawings`).

#### variation (`vr`)
- `core`: `variants` (≤ 10, each `name: p1 p2 …; kind yes|no`). Tiles:
  vrCore (properties in every variant of the kind, or `none`), vrVary
  (properties some variants of the kind have and others lack), vrBreak (each
  variant marked not of the kind, and the core properties it lacks, or `none
  of the core`).

#### cases (`ca`)
- `table`: `accounts` is a **cfg key** (2 or 3 names, fixed for the lesson; a
  preset cannot change it). `observations` (≤ 10, each with one cell per
  account, each cell exactly one of `y` consistent, `n` inconsistent, `-`
  silent; anything else reddens the banner). Tiles: caRecord (per account
  `absorbs 3 of 4, fails 1, silent 0`), caSurvivors (accounts with no `n`, or
  `none`), caSplit (observations on which the two compared accounts differ,
  `y` against `n`, or `none`), caPair (redraw-only select over the cfg's
  accounts choosing the two caSplit compares; with two accounts it has one
  option).

#### schema (`sc`)
- `coordinates`: `body` (position and a facing, D.0), `objects` (≤ 6, each a
  room position, with an optional `given`: `body` | `objective`). Tiles:
  scRoom (`cup (2, 1)`), scBody (`cup ahead 2, left 1` — coordinates relative
  to the body), scFrame (per object with `given`: `given in the body's
  situation: no conversion` | `given as a position in objective space:
  converted to ahead 1, right 2`).
- `habitual`: `habitual_reach`, `present_reach` (per side, left and right),
  `objects` (side and distance). Tiles: scHabitual (objects in habitual
  reach), scPresent, scAppeal (in the first and not the second).
- `tool`: `reach`, `tool` (length), `height`, `clearance` (what is added above
  the head), `objects` (distances), `openings` (a width or height to pass).
  Tiles: scReach (`170 cm`), scWithin, scClears (`clears by 5 cm` | `does not
  clear by 5 cm`).
- `obstacle`: `rocks` (≤ 8 heights), `project` (`climb` | `pass` | `none`),
  `capacity`, `general_level`. Tiles: scProject (rocks taller than the
  capacity, for `climb`; `none` for `pass` and for `none`), scLevel (rocks
  taller than the body's general level, whatever the project).

#### sorting (`so`)
- `sort`: `samples` (≤ 12, each `name, hue, lightness`, lightness a whole number
  0–10), `start`. Tiles: soCategorical (groups by hue name, in list order),
  soChain (the chain from `start`: at each step the unsorted sample nearest the
  last one picked, by |Δ lightness| plus 1 if the hue differs, ties broken by
  list order — the rule is printed), soPart (the first sample where the chain
  leaves the start's hue).

#### level (`le`)
- `tilt`: `image` (degrees, a rational in (−180, 180]; −180 is read as 180 —
  no trigonometry is needed, because a tilt of the field is subtracted, not
  projected), `level` (the starting level), `rule` (`switch` | `share`), `at`
  (for `switch`: the period at which the level jumps to the image), `share`
  (for `share`: the fraction of the remaining difference the level moves each
  period), `period` (redraw-only range 1..10). The level at period 1 is the
  starting level. Under `switch` it stays there until period `at`, where it
  becomes the image tilt; under `share`, level(n + 1) = level(n) + share ×
  (image − level(n)). Tiles: lePerceived (`image − level`, normalised to
  (−180, 180], at the shown period), leLevel, leSeries (the first five
  periods' perceived tilts).

#### depth (`de`)
- `binocular`: `iod` (interocular distance), `near`, `far`. Tiles:
  deConvergence (per distance, `iod / d` exact, as radians with four
  decimals — the small-angle form the lesson states), deDisparity
  (`iod · (1/near − 1/far)`).

#### motion (`mo`)
- `phi`: `separation`, `interval` (ms), `simultaneous` and `succession`
  thresholds (defaults 30 and 200, labelled as later textbook figures).
  Tiles: moSpeed (`separation / interval`, e.g. `1/12 cm per ms`), moBand
  (`seen together` when interval < simultaneous; `motion` when simultaneous ≤
  interval ≤ succession; `seen in succession` when interval > succession).

#### light (`li`)
- `ratio`: `surfaces` (≤ 6, each `name, reflectance, illumination`),
  `surround` (the name of the surface that is the surround). Tiles:
  liLuminance (per surface), liRatio (each surface's luminance over the
  surround's), liBrightest (every surface with the greatest luminance, tied
  names in list order).

#### triangle (`tr`)
- `parallel`: `a`, `b` (the angles at A and B, degrees, rationals). Refused
  unless 0 < a, 0 < b, a + b < 180. `trVertex` (redraw-only select: A, B or C,
  default C). Tiles: trC (`180 − a − b`), trAlternate (the two alternate angles
  at the parallel through the chosen vertex: at C, `a and b`; at A, `b and
  c`; at B, `a and c`), trStraight (the three angles at that vertex summing to
  180). An SVG draws the triangle and the parallel.

#### time (`ti`)
- `river`: `parcels` (≤ 9, each a name and a position downstream), `observer`
  (a position, or `none`), `standpoint` (`bank` | `current`). Tiles:
  tiWorld (every parcel and where it is now — all present), tiPast (on the
  bank, the parcels downstream of the observer; with the current, those
  upstream; `none` with no observer), tiFuture (the reverse).
- `diagram`: `moments` (≤ 9 names, in order), `present`, `protention` (span).
  Tiles: tiRetained (`A at depth 2, B at depth 1`), tiProtended (`D, E`),
  tiColumn (the vertical of the diagram at the present). An SVG draws
  Husserl's diagram: the horizontal of nows, the obliques of sinking, the
  vertical at the present.
- `ekstasis`: `moments`, `presents` (an ordered list of presents). Tiles:
  tiColumns (per present, its column: `B: A 1`, `C: A 2, B 1`, `D: A 3, B 2,
  C 1`), tiDepths (per moment, its depth under each later present: `A: 1, 2,
  3`), tiOrder (`the order A, B, C is the same in every column`, computed by
  comparing the columns, or the first column where it is not).

### D.2 `argkit/validity` reused

Exactly as `content/philosophy/c1_arguments/part_a.py` uses it: `premises`,
`conclusion`, `show`; tiles vaVerdict, vaCounter, vaRows. Sentence letters are
named in the lesson prose. (`variation` uses `vr` so that no page and no
mathcheck block carries two meanings of `va`.)

### D.3 What the kit must never do

- Print a figure that claims to be an experience ("perceived size: 170 cm" is
  printed as "the size an inference would conclude").
- Print a lesson's own model under an opponent's or the book's name.
- Derive a tile from trigonometry, or from a drawing.
- Show a tile, or offer a control, whose meaning depends on comparing presets.
- Let a preset change a `cases` table's accounts.
- Decide a `cases` or `variation` cell. The coding is the lesson's; the kit
  only counts.

---

## §E Package layout, the source text, and quoting a book in copyright

### E.1 Layout

```
content/phenomenology/
  __init__.py                       PATH, COURSES, numbering loop
  c1_preface/__init__.py            COURSE; lessons = part_a.LESSONS
  c1_preface/part_a.py
  c2_prejudices/ c3_lived_body/ c4_expressive_body/ c5_sensing_space/
  c6_things_others/ c7_cogito_time_freedom/
content/spoken/phenomenology.py     SPOKEN = {}
```

A course with more than six lessons (Courses 3, 5, 6 and 7) splits into
`part_a.py` and `part_b.py` at its midpoint.

### E.2 The source text

The Subject's single source edition is **Maurice Merleau-Ponty,
*Phenomenology of Perception*, translated by Colin Smith (London and New York:
Routledge, Routledge Classics 2002; first published by Routledge & Kegan Paul,
1962)**, with the Routledge Classics pagination (Preface vii–xxiv,
Introduction from p. 3, Part One from p. 77, Part Two from p. 235, Part Three
from p. 429). The operator owns Donald A. Landes's 2012 translation in print,
but chose on 2026-10-24 to build the Subject on Smith, the text the authors
have in full, and to correct errors once it is live. Every quotation, every
page reference, every module's full title and every course's `how_to`
attribution line comes from Smith. The two translations are never mixed.

The authors work from a private plain-text extraction of the operator's PDF
(its path is given in `docs/phenomenology/AUTHORING.md`; the text is never
copied into the repository or the project files). Page numbers are the
printed Routledge Classics page numbers, found from the running heads.

**Smith's vocabulary.** Where Smith's English is a known problem, the lesson
quotes Smith and says what the French says, once, in its own words: Smith
renders *schéma corporel* as "body image" (the lessons call it the *body
schema*, and say Smith's word in the lesson that introduces it, because
"image" suggests a picture, the very reading Merleau-Ponty rejects); *corps
propre* as "one's own body"; *motricité* as "motility"; *le sentir* as "sense
experience". The spec's other terms (*motor intentionality*, *intentional
arc*, *phenomenal field*, *being-in-the-world*) are Smith's too. Smith's
chapter titles, used in every course `summary`: Introduction 1 The
'Sensation' as a Unit of Experience, 2 'Association' and the 'Projection of
Memories', 3 'Attention' and 'Judgement', 4 The Phenomenal Field; Part I,
Experience and Objective Thought. The Problem of the Body; 1 The Body as
Object and Mechanistic Physiology; 2 The Experience of the Body and Classical
Psychology; 3 The Spatiality of One's own Body and Motility; 4 The Synthesis
of One's own Body; 5 The Body in its Sexual Being; 6 The Body as Expression,
and Speech; Part II, The Theory of the Body is already a Theory of
Perception; 1 Sense Experience; 2 Space; 3 The Thing and the Natural World;
4 Other Selves and the Human World; Part III, Being-for-Itself and
Being-in-the-World; 1 The Cogito; 2 Temporality; 3 Freedom.

A phrase is never quoted from memory, from the other translation or from a
secondary source. Every *(check against text)* in §C is resolved by the
course's author against Smith, and the §C entry corrected where the text
differs.

Every course's `how_to` carries the same attribution line, as *Capital*'s carry
the Kerr line.

### E.3 Quoting

*Phenomenology of Perception* is in copyright in French (Gallimard, 1945) and
in both English translations (Colin Smith, Routledge, 1962; Donald A. Landes,
Routledge, 2012). The Subject quotes Smith for commentary, and keeps quotation
small:

- The opening passage is at most **70 words**, cited by page in the source
  edition.
- A lesson's quotations, the opening passage included, total at most **150
  words**, well under a thousandth of the book (which runs to some 200,000
  words or more) per lesson.
- Every quoted phrase is copied from the source text, character for
  character, and its page is in a comment beside the lesson dict. Never from
  memory, never from another translation, never from a secondary source, and
  never from this document, which quotes nothing.
- Everything else is paraphrase, and a paraphrase says whose view it
  states. Merleau-Ponty often voices his opponents at length; a sentence in
  the opponent's voice is never quoted as his.
- The opening `p` block says, after the passage, which pages the passage
  comes from and invites the reader to read the whole section in their copy
  first — the lectures read the text whole before going line by line, and
  with a book in copyright the reader's own copy is where that happens.

---

## §F Voice: the read-along, after the three lectures

`docs/capital/PLAN.md` §F holds in full: read the passage first, then line by
line; open with the reader's own world only where the chapter's object is
already in it; tell the history of an idea as a story with people in it;
"you", warmly; at most one light remark, preferably pointing at the author's
own; the `note` names the lesson's one limit; the last `p` points to the next
lesson by title; no slang, no first-person anecdotes, no "let's"; presented,
not endorsed; never praise one side in the lesson's own voice.

What is different for this book:

1. **The lectures were about perception, and the modern view is disputed
   ground.** The first lecture reads the *Tao Te Ching*'s first chapter
   through a theory of the mind as a prediction machine: a tomato a metre away
   is a hypothesis the brain builds from signals; a Roomba needs a model of
   the room and of itself to know where it fits; perception is a controlled
   hallucination, in Anil Seth's phrase. The second turns to bodily learning
   and flow. These are close to what the book is about, but their relation to
   it is a live dispute, not a mapping. On one reading predictive processing is
   Helmholtz's unconscious inference again — the intellectualism of
   Introduction III. On another, its active-inference and enactive forms sit
   close to Merleau-Ponty (Clark, Gallagher, Kirchhoff, Bruineberg and
   Rietveld, and Dreyfus's reading of the body's *maximal grip*). And
   predictive processing also rejects the constancy hypothesis, as he does,
   because expectations shape the percept. So a lesson may set the chapter
   beside a modern view **at most once per course**, in the lesson whose
   chapter is about the same phenomenon, in the `note` or a late `p` and never
   in the opening, stating both sides fairly, never as settling the chapter
   and never in the form "science has proved Merleau-Ponty right" or "wrong".
   The permitted asides and their single homes are: Classical Prejudices, in
   The Constancy Hypothesis (both reject the constancy hypothesis, and differ
   on whether what replaces it is inference); The Lived Body, in The Phantom
   Limb (Ramachandran's mirror box, with the caveats in that entry);
   Things, the World and Others, in Hallucination (Seth's phrase against the
   chapter's argument, with both sides). The other courses carry none. The
   Roomba's model of itself is not used as an analogue of the body schema —
   for Merleau-Ponty the schema is precisely not a model consulted before
   moving — and the lectures' flow is not paired with habit.
2. **Everyday scenes are easy here, so ration them.** Perception is in the
   reader's life all the time; a lesson that opens with "look at the cup on
   your desk" every time becomes a formula. Open with a scene in at most half
   of a course's lessons; open the rest with the passage's own case — Schneider,
   Stratton, Gelb's disc.
3. **The cases are people.** Schneider was a soldier wounded in 1915 by
   splinters to the back of the head, and Gelb and Goldstein published on him
   from 1918; the amputees, the aphasics, Binswanger's patient and the
   patients who hallucinate are patients. Name them as the book does, with the
   respect the book shows, and never for an effect. A lesson built on a
   clinical report says in a sentence that the book's argument concerns the
   case as it was reported: for Schneider, that the case was later questioned
   (§G); for the amputees and the patients of Hallucination, that the reports
   are the book's sources' and the lab codes the reports, not the patients.
4. **Merleau-Ponty is presented, not endorsed.** He is arguing with
   Descartes, Kant, Husserl, Sartre, Bergson and the psychologists, and every
   one of them is stated in their own terms and at strength before he answers.
   His own account is stated in prose and never scored (§0). Where a reading
   of him is disputed — the reduction, his relation to Husserl, the tacit
   cogito (which he himself later called impossible), the double sensation
   (which the late work recasts as reversibility) — the lesson says it is
   disputed.

**One exemplary paragraph** (a `p` block for “The Constancy Hypothesis”, after
the passage):

> You have almost certainly seen the two lines with arrowheads, one with the
> fins turned out and one with them turned in, and been told that they are the
> same length. Measure them and they are. The lab does the measurement for
> you: ten centimetres and ten centimetres, so the theory Köhler named the
> constancy hypothesis — that each point of the stimulus produces its own
> point of sensation, the same wherever it occurs — predicts that you will see
> no difference at all. Most people report one. The usual way of putting this
> is that perception has made a mistake, and the textbook calls the figure an
> illusion. Merleau-Ponty's reply is different: the mistake is in the
> question. *Equal* and *unequal*, he argues, belong to a world where lines
> are laid side by side and measured; in the field you are looking at, the two
> lines are not yet the kind of thing that is either.

---

## §G What is left out, and why

- **Merleau-Ponty's other works**: *The Structure of Behaviour* (1942), *The
  Visible and the Invisible* (posthumous), the essays on Cézanne and on
  language. Named where the book points to them, or where a lesson's `note`
  says the late work revises a claim (the tacit cogito, the double
  sensation); not read.
- **The secondary literature's disputes** over the book's relation to Husserl
  (especially the late manuscripts), to Heidegger and to Sartre. A lesson
  says where its reading is disputed and goes no further.
- **The later status of the psychology.** Gelb and Goldstein's case of
  Schneider was re-examined by neurologists in 1949 (Bay, Lauenstein and
  Cibis; Jung), who questioned the reliability of the reports and the
  diagnosis; modern reviews (Goldenberg, 2003, in *Classic Cases in
  Neuropsychology* II; Marotta and Behrmann, 2004, *Neuropsychologia* 42) read
  the case as a visual form agnosia and judge that the theoretical conclusions
  went beyond the data. These citations are checked before they are printed.
  The course `not_covered` says so, and the Schneider lessons say in a sentence
  that the book's argument concerns the case as reported. The modern
  experiments the lectures' views rest on are asides (§F.1), never evidence
  the lab computes.
- **Psychophysics beyond what the chapter uses.** Weber's law is not used: the
  Introduction does not discuss it, and a threshold does not refute a
  point-for-point theory, so setting the two side by side would present a
  strawman as the hypothesis. Fechner's law and signal detection are not used
  either. Brunswik's ratio and Wallach's ratio principle are used, named as
  the lessons' additions and later than the book.
- **Trigonometry in the figures.** The kit's Pythagorean angles and
  whole-number view directions are a deliberate limit, so that every figure
  stays exact. It means no trigonometry in any figure, not no picture: a
  drawing may use it for pixels (§D.0).

---

## §H Wiring notes for the orchestrator

As `docs/capital/PLAN.md` §H and AGENTS.md §0's list, with these values:

- Package `phenomenology`; path slug `phenomenology`; check-id prefix `phen`.
  Check ids take the form `phen-course7-lesson-<lesson-slug>`; every slug in
  §C is at most 42 characters, so every check id is at most 62.
- `PHEN_DISCLAIMER_RE = r"what perception gives is not a figure"`.
- `content/spoken/phenomenology.py`; `phenomenology_semantic_copy` in
  `test_public_copy`.
- Register `phenomenology` in `GENERATED_PATHS` at the start of the branch with
  every `COURSE = None`; add `"phenkit"` to `KITS_WITH_EXPECTATIONS` last.
- The PATH's tagline and description say "Seven courses and 44 lessons"; the
  counts test reads the PATH, not §B, so §B's total and both PATH sentences
  move together if a lesson is added or removed.
- Eleven Subjects after wiring; every "ten Subjects" count is updated in the
  wiring commit.

---

## §R Review record

The reviews are run by two different models, each independently, before any
lesson is authored, and again per course after authoring, as for *Capital*.
Each review's findings and the resolution of each are appended here.

### Pre-authoring review, 2026-10-24

Two independent reviews of the first draft (41 lessons), each by a different
model, neither seeing the other's findings, both done with §E.2 open and
without the book's text in the environment:

- **Fable (pedagogical-expert role)**: instructional design, the lab kit's
  buildability, and reconciliation with the library and its enforced ranges.
  31 findings, 9 blocking (1, 2, 5, 9, 15, 17, 18, 19, 23).
  `docs/reviews/phenomenology-spec-pedagogy-review.md`.
- **Opus (independent scholarly review)**: accuracy against the book and its
  sources, from the reviewer's knowledge (Smith 1962, Landes 2012, Gallimard
  1945), each finding marked CERTAIN, LIKELY or CHECK-AGAINST-TEXT. 50
  findings. `docs/reviews/phenomenology-spec-accuracy-review.md`.

Resolutions, by theme:

1. **`cases` (Fable 1, 4, 5, 6, 9, 13; Opus 24, 29, 31)**: a table now carries
   the opponents' accounts only; the computed result is caSplit and
   caSurvivors (`none` on every table); Merleau-Ponty's account is in prose and
   never a column. The accounts are a cfg key, presets vary only the
   observations, and caPair's options come from the cfg. Every lesson that
   keeps `cases` (ten: The Phenomenal Field, The Phantom Limb, The Intentional
   Arc, The Body as a Sexed Being, The Anonymous Subject of Sensing, Lived
   Space, The Thing and the Real, The Truth of Solipsism, The Tacit Cogito,
   Freedom in Situation) lists its accounts and three or four observations,
   with a proposed coding marked to be checked against the text. The
   Introduction's table is coded so that both opponents fail, and the lesson
   says any split is its coding. Replaced where a review's alternative was
   better: Schneider's lesson now computes the frame a target is given in
   (`schema/coordinates`, `given`, `scFrame`) instead of recoding the tasks
   twice; the motor physiognomy of colours computes a pure-quality
   prediction (`stimulus`); the spoken word computes an empty core over
   expressions of anger (`variation`); hallucination computes what the
   hallucination lacks (`variation`). Sartre's look, the infant, Schneider's
   thinking (analogies and stories) and Cassirer are now observations or
   accounts.
2. **§0 (Fable 2, 4)**: three families named — opponents' (and later
   psychologists') predictions, counts over the lesson's coding, the lesson's
   own illustrative model — with the rule that a third-family `panel_intro`
   says "the lesson's model"; the §0 table gains a family column; D.3 forbids
   printing a lesson's model under an opponent's name; the material clause
   names the third family.
3. **Kit buildability (Fable 3, 15–22; Opus 36)**: view directions are
   whole-number triples of whole-number length, so Pythagorean quadruples give
   exact corner views that see three faces; `reports` makes peConsistent
   computable; peCover added; `necker` now computes both readings by an exact
   mirror reflection and compares the drawn edge sets; floating-point
   trigonometry is allowed for SVG pixels only; one tilt convention and one
   facing convention are defined (so the 3-4-5 disc projects 4/5, and the coin
   uses 4-3-5 for 3/5); `deRatio` dropped and the depth comparisons moved to
   prose; `cues/sequence` and every redraw-only range are fixed by the cfg and
   clamp with a banner; `motion/positions` dropped (a fixed string is not a
   computation); `trVertex` added; `level` has a `switch` rule and a defined
   `none` preset; `scBody`/`scLevel`, `va`/`vr`, liBrightest ties, moBand
   boundaries, the lightness scale, the ±180 tilt and the exact `cases` cell
   syntax are specified; the page-weight rule (active mode only) is stated in
   D.0; `own` uses a stated restricted view list, and its `mirror` preset is
   dropped.
4. **Arithmetic (Fable 14; Opus 34–38)**: the hat clears a 200 cm door by
   5 cm; `far` depth is a tenth of `near` (13/6000 against 13/600), and the
   fixed-interval preset gives 1/85 (Opus's "≈ 1/98" was itself off: the ratio
   is 3000/255000); the Brunswik ratio is 47/51; face counts are recomputed
   for the corner views (5 of 6; the house "every face but the one it stands
   on"); the body-coordinates example is ahead 2, left 1; the moon's ratio is
   printed reduced, 1737/192200; the coin is a 7 mm disc; the `shift` grouping
   is recomputed (four groups, not "everywhere"); the `_a_e` count is 18 on the
   recorded list.
5. **Structure (Opus 1, 2, 3, 25–28, 33; Fable 3, 12)**: habit moved to the end
   of Part One Chapter 3 (The Lived Body, now 8); Chapter 4 has its own lesson,
   The Body as a Work of Art, opening Course 4, renamed The Expressive Body
   (`perception-the-expressive-body`); the glass moved to The Unity of the
   Senses, and The Thing and the Real uses honey, the woolly carpet and
   Cézanne; the ship on the beach is in Attention and Judgment, as its lab;
   The Anonymous Subject of Sensing added (Part Two Chapter 1: one perceives
   in me, coexistence); Time as Subject added (Part Three Chapter 2); the
   Space chapter's opening argument is in Up and Down's Read. 41 lessons
   become 44 (Courses 3, 5 and 7 gain one each); tagline, description, §B,
   §C headers, Contents, E.1 and §H updated. No two adjacent chapters are
   merged.
6. **Misplacement and misrepresentation (Opus 4–8, 10–17, 20–23, 30, 32)**:
   the moon, the Necker cube and the melody are labelled as the lesson's
   illustrations, with the book's own locations to be found; the melody is
   Ehrenfels's; attention is criticised under both accounts; module names drop
   the edition-dependent letters; the Part Two introduction's title keeps
   *Already*; phi is Wertheimer's interpretation, which the chapter
   qualifies; Wertheimer's mirror rights itself suddenly, so the preset uses
   `switch`, and the halving is kept only as Stratton's labelled illustration
   (1897 experiment); "wholly" removed from Freedom in Situation; the absolute
   freedom of the rock lesson is "recognisably Sartre's", the chapter mostly
   not naming him; the Preface's charge of naïveté and dishonesty is in
   Description, Not Explanation; Köhler is credited with the constancy
   hypothesis; Descartes' premise is the general one, with the Second
   Replies and *Principles* I.10; Kant's own use of the triangle proof is
   named; the tacit cogito's later disavowal and the double sensation's later
   recasting are in `note`s; true and false love is in the Cogito lessons;
   Heidegger, Binswanger, Minkowski, von Senden, Cassirer, Scheler, Köhler,
   Koffka and Ehrenfels are named.
7. **Quotations (Fable 24; Opus 18, 19, 44)**: every phrase the first draft put
   in quotation marks as the book's words is now a pointer, a term in
   italics, or marked *(wording to be checked against the text)*; "(wording
   checked)" is removed everywhere, since it could not have been checked
   against one edition; §C states that this document quotes nothing; the
   quotation ceiling is "well under a thousandth of the book".
8. **Source text (Fable 23; Opus 18)**: §E.2 names the Landes translation as
   the single source edition, pending the operator's confirmation; the PATH
   prerequisites and footer and every course's `how_to` name it; authoring
   stays blocked until the edition is confirmed and its route recorded.
9. **Voice (Fable 25–27; Opus 45–48)**: the modern aside is at most once per
   course, in three named homes, fair to both sides (predictive processing
   also rejects the constancy hypothesis; active-inference and enactive
   readings sit near Merleau-Ponty; Seth's phrase runs against the
   hallucination chapter; the mirror box's mixed evidence and image-like
   explanation); the exemplary paragraph no longer praises one side; §F.3
   carries the obligation to say the argument concerns the case as reported;
   the Roomba is not an analogue of the schema.
10. **Ranges and names (Fable 28–31)**: check-id prefix `phen`; the long Part
    Two slug becomes `the-body-and-perception` (every slug ≤ 42, every check id
    ≤ 62); module names are a locator and a fixed short form from the §B
    table, never truncated; key lines re-measured (≤ 46).
11. **Misconceptions (Fable 7, 8, 10, 11, 13; Opus 9, 39–43, 49, 50)**: holders
    named for the reflex view, the absolute spectator, depth by convergence
    (Descartes, Berkeley) and the sceptic; Gelb and Goldstein's reading is
    `mistakes[0]` of Speech as Gesture; Description, Not Explanation is refuted
    by the Preface, not the lab; Course 1 says its labs illustrate the method
    and that the Preface may be read last; the moon is computed once; size
    constancy's Worked line is the lab's (Brunswik), the coin in prose;
    Wertheimer's thresholds, Gelb's reflectances and Stratton's adaptation are
    labelled; the natural-world example and its cues are named; the
    Schneider re-examination is dated 1949, with the modern reviews to be
    checked before printing.

Declined, and why:

- **Fable 1, the exception for The Truth of Solipsism and The Phantom Limb**
  (allowing Merleau-Ponty's account as a column where the chapter scores it):
  declined by the orchestrator's rule that his view is never scored. Both
  lessons keep two opponent columns, and the solipsism table still computes
  the case both absorb.
- **Fable 3 (7.4), merging Time Is Not in Things into The Field of Presence**:
  declined. Opus 26 required a lesson on time as subject, and the river lesson
  now computes the opposite past/future assignments of two standpoints over
  the same water, which is the chapter's river argument and is not fixed by an
  index.
- **Fable 3 (5.3), `stimulus/illusion` for The Unity of the Senses**: declined
  because the glass belongs in this chapter (Opus 2) and the variation over
  two codings computes what the chapter's description and the sense-bound
  view each yield; `stimulus` would also have repeated the motor-physiognomy
  lab two lessons earlier.
- **Fable 7(a), merging Essences and Existence into The Reduction**: declined;
  option (b) taken instead (Course 1's `how_to` and `why_order`).
- **Fable 11, keeping Weber as a preset in prose or moving it to The Motor
  Physiognomy of Colours**: superseded. Weber is dropped (Opus 17: not in the
  Introduction, and a threshold does not refute the hypothesis); Opus 40 on
  Weber's own fraction is therefore moot.
- **Fable 12, a third Chapter 6 lesson on the speaking word**: declined. The
  count already rose to 44 for coverage the accuracy review found missing, and
  Chapter 6 keeps two lessons.
- **Fable 25, keeping the four lecture pairings as the only four**: partly
  declined. The pairings are now three, one per course in three courses: the
  Roomba is not an analogue of the body schema (Opus 48), and flow is not
  paired with habit (Dreyfus, the better partner, is secondary literature,
  §G).
- **Fable 30, dropping the Part from module names**: applied in a different
  form. The orchestrator asked for a standard short form per chapter, so the
  Part stays and the title is a fixed short form within 60 characters.
- **Opus 25, 26 and 33, merges to keep 41 lessons** (the two Schneider
  lessons; the tacit cogito into the certainty of seeing; the two Freedom
  lessons): declined. Each pair carries a different hard idea, Fable 5 had
  already given the Schneider lessons different computations, and the
  orchestrator allowed the count to change.
- **Opus 3, the ship as a second preset only**: applied more fully — the ship
  is Attention and Judgment's whole lab, replacing the unconscious-inference
  size computation, which moved into Size and Shape Constancy.
- **Opus 35's alternative figure for the fixed-interval preset** ("≈ 1/98 of
  near"): not adopted; the exact ratio is 1/85.

Left for the book's text (the author settles each from the confirmed edition
and records it here): every observation and cell in the ten `cases` tables;
where the moon, the reversible cube, the melody, the misprint, the corrected
stone-and-sunlight illusion, the glass's single manner of being, the honey and
the woolly carpet fall; whether *pensée de survol* is in this book; whether
the Freedom chapter names Sartre; the organist's figures; Goldstein and
Rosenthal's directions and whether a too-faint colour still deviates the arm;
the gesture transferred across limbs in Chapter 4; the Japanese smile; the
chapter's list of what a hallucination lacks; the edition's section headings;
every phrase marked *(wording to be checked against the text)*; and the
Schneider and Seth citations.
