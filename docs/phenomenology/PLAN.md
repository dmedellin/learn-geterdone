# Phenomenology of Perception, Read Along — the build specification

This is the curriculum, lab and authoring contract for the eleventh Subject: a
read-along of Maurice Merleau-Ponty's *Phenomenology of Perception* (1945),
the whole book in its own order — the Preface, the Introduction and the three
Parts — one lesson per chapter section that carries a hard idea. Everything an
author, a kit engineer or a reviewer needs is here. Where it says "exactly", a
test or a gate enforces it. Where it says "never", a published page somewhere
in this library has already been wrong for that reason.

It is built the way *Capital, Read Along* was built (`docs/capital/PLAN.md`),
and adopts that document's conventions by reference wherever this one is
silent. Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight
note; `content/AGENTS.md` (all of it); `scripts/mathpath/AGENTS.md` ("a
preset's two claims"); `docs/philosophy/PLAN.md` §D.0 and §E; and
`docs/capital/PLAN.md` §0, §E and §F.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The seven courses
- §C Every lesson: 41 entries
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
decorative. The honest answer is different and, it turns out, just as good:

**The reader computes what the theories Merleau-Ponty argues against predict.**

The book is an argument with two opponents he names in the Introduction:
*empiricism*, for which perception is sensations caused point by point by
stimuli and joined by association, and *intellectualism*, for which perception
is a judgement that interprets those sensations. Both are, in his phrase,
"objective thought", and both make predictions that can be computed exactly from
a stimulus: the two lines of the Müller-Lyer figure are equal, so they should
look equal; the moon subtends the same angle at the horizon as overhead, so it
should look the same size, or else the mind must have inferred a distance; a
disc that sends the eye the light of white paper should look white; two lights
flashed in alternation are two lights, so nothing should move. Merleau-Ponty's
method is to put each prediction beside what perception actually gives and to
read the gap. The lab computes the prediction, exactly, from the quantities the
lesson states; the lesson reads the gap.

So the claim this Subject makes, and the only one it makes, is this: **every
figure is what a stated model of perception — usually one the chapter is
criticising — predicts from the stated stimulus, computed exactly in the
browser.** The lab never claims to compute an experience. That is the book's
whole point, and the material clause says so.

The second family of computations is the book's evidence. Merleau-Ponty
argues from cases — the phantom limb, anosognosia, Schneider, the aphasic who
cannot sort colours, Stratton's inverting spectacles, Wertheimer's tilted
mirror, Gelb's spotlit disc — and his procedure with each is the same: set out
what was observed, ask which account can absorb every observation, and find the
observation that splits them. That procedure is countable, and the `cases`
mode counts it.

Fifteen modes carry the whole of it:

| what the reader computes | mode | from |
| --- | --- | --- |
| the constancy hypothesis's prediction against a reported percept; Weber's just-noticeable difference | `stimulus` | stimulus magnitudes, a reported difference, a Weber fraction |
| how dots group by proximity, and which grouping a "pure sensation" account cannot predict | `grouping` | positions on a line, a gap ratio |
| which remembered words fit a partly seen word, before and after the context arrives | `cues` | candidates, a pattern of seen letters, a context |
| angular size, the size an unconscious inference would conclude, and a size-constancy ratio | `size` | object size, distance, an assumed distance, a reported size |
| which faces of a thing are visible from which places; two depth readings of one drawing; the ellipse a tilted disc projects | `perspective` | an object's faces and normals, viewpoints, a tilt |
| the invariant core of a set of free variations | `variation` | variants and their properties, which variants are still the thing |
| which account absorbs which observation; the observation that splits two accounts | `cases` | observations × accounts, each cell consistent, inconsistent or silent |
| where things are relative to the body rather than to the room; the reach of a habitual body and of a tool; an obstacle relative to a project | `schema` | body and object positions, segment lengths, a tool, a project's capacity |
| a categorical sort against a chain of concrete resemblances | `sorting` | colour samples with a hue name and a lightness |
| the tilt of the visual field against the spatial level, and the level's re-orientation | `level` | an image rotation, a starting level, an adaptation share per period |
| convergence and binocular disparity, and depth as the classical theory computes it | `depth` | interocular distance, two distances |
| the speed implied by two lights, and the band in which motion is seen without anything moving | `motion` | separation, interval, the thresholds of the lesson's source |
| luminance as reflectance × illumination, the ratio to the surround, Gelb's disc | `light` | reflectances, illuminations, a surround |
| the angles of a triangle through the construction of a parallel | `triangle` | two angles |
| a line of nows against the diagram of retention, and the depth at which a moment is held | `time` | moments, a present, a protention span |
| whether an argument's premises force its conclusion (the argument from analogy; the cogito as inference) | `argkit/validity` (reused) | premises, conclusion |

Every quantity is a whole number or a fraction. Angles are handled without
trigonometry: a rotation or a tilt is one of the Pythagorean angles the kit
lists (cosine and sine both rational), and an angular size is the ratio
size / distance, which is how a small angle is computed in radians and how the
lesson says it is computed. Where a degree figure is printed it is printed
beside its exact ratio and marked approximate.

**Where an instance comes from.** A case or an experiment is Merleau-Ponty's own
(he reports Gelb and Goldstein's Schneider, Stratton, Wertheimer, Gelb, Katz,
Goldstein and Rosenthal, Head, Lhermitte, Schilder and others). Where a preset
uses figures the book or its source reports, its label says so ("Stratton's
spectacles: 180°"); where it uses illustrative figures, the lesson says so in
prose. The `cases` cells are the lesson's reading of the chapter and the lesson
says that too: the count is exact, the coding is an interpretation, and a
reviewer checks each cell against the text.

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
4. **The labs mostly compute the opponents' predictions.** In every other
   Subject a lab computes the lesson's own claim. Here the lesson's claim is
   usually that the computed figure is not what is perceived. Each lesson says
   which model the lab computes, by name, in the lab's `panel_intro`.
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
> perception gives can be seen beside them. Seven courses and 41 lessons are
> available.

**description**:

> The Phenomenology Subject: a read-along of Merleau-Ponty's 1945 book in its
> own order, seven courses that follow its Preface, Introduction and three
> Parts. Each lesson reads a short passage first, then explains it line by
> line, then computes what a classical theory of perception predicts &mdash; the
> size of the moon, the length of two lines, the colour of a spotlit disc, the
> motion between two lights &mdash; or counts which account survives a
> clinical case. All seven courses and 41 lessons are available.

**key** (each line ≤ 46 characters):

```
angular size = size / distance
luminance = reflectance × illumination
lightness follows the ratio to the surround
perceived tilt = image tilt − spatial level
motion seen: lights alternate in the band
an account survives if no case refutes it
a ∠ sum = two right angles, by a parallel
```

**material** (must differ from every existing clause; proposed
`PHEN_DISCLAIMER_RE = r"what perception gives is not a figure"`):

> every figure on this path is what a stated model of perception predicts from
> a stated stimulus, or a count over the cases a lesson sets out, computed in
> your browser &mdash; and what perception gives is not a figure, which is the
> claim the book argues and the lab cannot settle.

**prerequisites** (paragraphs):

1. No philosophy. The Subject introduces Descartes, Kant, Husserl, Bergson,
   Sartre and the psychologists — the Gestalt school, Gelb and Goldstein,
   Stratton, Wertheimer — at the moment Merleau-Ponty argues with them, at
   their strongest. Words he uses in a sense of his own (*the body proper*,
   *motor intentionality*, *the phenomenal field*, *being-in-the-world*) are
   defined in the lesson that introduces them.
2. School geometry: a ratio, a right angle, the angles of a triangle, a point
   on a grid. The labs do the arithmetic; what is asked of you is to say what
   each figure is a prediction of.
3. A copy of the book is strongly recommended. The book is in copyright, so a
   lesson quotes only a short passage and the phrases it reads closely, with
   page references to the translation named in each course's `how_to` (§E).
   The rest is paraphrase, and a paraphrase is a reading: check it against
   the page.
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
   cogito. The book's claims about freedom rest on its claims about the body,
   and he says so.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Classical
> Prejudices uses the Preface's idea of description; The Lived Body uses the
> Introduction's two opponents; Habit, Sexuality and Speech extends the body
> schema; Sensing and Space and Things, the World and Others re-read
> perception from the body; The Cogito, Time and Freedom uses all of it.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what the lesson states: an angular size is a
> size over a distance, a luminance is a reflectance times an illumination, an
> account's record is a count over the cases. Nothing is rounded except where a
> lesson says so. Quotations are short extracts from the translation named in
> each course, quoted for commentary. What the labs cannot do is compute an
> experience &mdash; and that is what the book is about.

---

## §B The seven courses

| # | slug | title | the book | lessons | level |
| --- | --- | --- | --- | --- | --- |
| 1 | `perception-what-phenomenology-is` | What Phenomenology Is | Preface | 4 | Beginner |
| 2 | `perception-classical-prejudices` | Classical Prejudices | Introduction, I–IV | 5 | Beginner |
| 3 | `perception-the-lived-body` | The Lived Body | Part One, introduction and Chapters 1–3 | 7 | Intermediate |
| 4 | `perception-habit-sexuality-and-speech` | Habit, Sexuality and Speech | Part One, Chapters 4–6 | 4 | Intermediate |
| 5 | `perception-sensing-and-space` | Sensing and Space | Part Two, introduction and Chapters 1–2 | 7 | Intermediate |
| 6 | `perception-things-world-and-others` | Things, the World and Others | Part Two, Chapters 3–4 | 7 | Advanced |
| 7 | `perception-cogito-time-and-freedom` | The Cogito, Time and Freedom | Part Three, Chapters 1–3 | 7 | Advanced |

Total 41. Part One is split where the book turns from the body's spatiality
and motricity (Chapters 1–3) to the body's unity and its expressive life
(Chapters 4–6); Part Two where it turns from the senses and space to the thing
and other people. Every course name is the reader's, not the book's, because
the book's Parts are named *The Body*, *The Perceived World* and *Being-for-
Itself and Being-in-the-World*, and "The Body" alone would not tell a reader
which half they are in. The course `summary` names the Part exactly.

The `perception-` prefix keeps course slugs from colliding with generic names
other Subjects use and tells a reader landing on a course URL which book it
belongs to. Check ids take the form `php-course7-lesson-<lesson-slug>`; every
lesson slug in §C is at most 44 characters.

Each course's `module` names are the book's sections, as the translation
prints them: `Part One · Chapter 3 · The Spatiality of One's Own Body and
Motricity`. A module name over 60 characters is shortened at its end, never in
its middle.

---

## §C Every lesson

Format as `docs/capital/PLAN.md` §C:

- **slug** — Title — *module*
- **Read:** where the opening passage is, by section and subject. A pointer,
  never a quotation; the words on the page come only from the source text (§E).
- **Do:** the observable objective; `standard` measures it.
- **Lab:** mode/view; presets and their instances.
- **Misconception:** the wrong model `mistakes[0]` names and refutes.
- **Worked:** the single worked example, in one line.

Misconceptions are misreadings of the chapter — what Merleau-Ponty is taken to
say and does not — or the opponent's position stated at its strongest before
the chapter answers it. They are never verdicts on which school of philosophy
or psychology is right. Where a misconception is a position someone holds
(Descartes, Kant, Husserl, Sartre, the Gestalt psychologists, the
physiologists), the lesson names its holder.

Preset ids are suggestions; the INSTANCES are not optional. Where an entry
leaves an instance to the author, the author records it here in the same commit.

### Course 1 — What Phenomenology Is (`perception-what-phenomenology-is`, 4)

Preface. The four lessons follow the Preface's own four topics: description,
the reduction, essences, intentionality — and its closing claim about
rationality and the unfinished.

1. **description-not-explanation** — Description, Not Explanation — *Preface*
   - **Read:** the opening question "What is phenomenology?" and the demand to
     describe rather than explain or analyse; the geography-and-countryside
     comparison.
   - **Do:** compute the moon's angular size at the horizon and overhead and
     state which question the equal figures answer and which they do not.
   - **Lab:** `size/angle`. Presets: `horizon` (moon 3,474 km at 384,400 km —
     the lesson says the figures are modern astronomy's, not the book's),
     `zenith` (the same moon about one Earth radius nearer, 378,029 km —
     slightly *larger* in angle overhead), `coin` (a 1 cm-ish coin held at arm's
     length that covers it, illustrative: 7 mm at 77 cm). Pins the ratio tile.
   - **Misconception:** "Phenomenology rejects science." Refuted with the lab:
     the figures are correct and the lesson keeps them; the Preface's claim is
     that the scientific figure is a second-order expression of a world
     already perceived, "as geography is in relation to the countryside", not
     that it is false.
   - **Worked:** 3,474 / 384,400 ≈ 0.0090 rad, about half a degree, at the
     horizon; slightly more overhead; the horizon moon still looks larger.

2. **the-reduction-and-its-limit** — The Reduction and Its Limit — *Preface*
   - **Read:** the reduction as a loosening of the "intentional threads" that
     attach us to the world, so that they show; Fink's "wonder"; "the most
     important lesson the reduction teaches us is the impossibility of a
     complete reduction" (wording checked against the text).
   - **Do:** show that one drawing is consistent with two solids and name what
     the drawing does not decide.
   - **Lab:** `perspective/necker`. Presets: `cube` (a wire cube in oblique
     projection: both front-face readings project to the identical 12 edges),
     `box` (a 2 × 1 × 1 box, same result), `solid` (a cube with its hidden
     edges removed: one reading only). Pins the readings-count tile.
   - **Misconception:** "The reduction doubts the world exists, as Descartes
     doubted." Merleau-Ponty's Husserl suspends our *complicity* with the world
     in order to see it; it does not withdraw belief, and he says it cannot be
     completed. The lab: nothing about the drawing is doubted; what shows is
     the setting habit had supplied.
   - **Worked:** the twelve projected edges are identical for both readings;
     which square is in front is not in the drawing.

3. **essences-and-existence** — Essences and Existence — *Preface*
   - **Read:** essences as a means, not the end; the "Vienna Circle" remark
     about the word consciousness; "the world is not what I think, but what I
     live through" (wording checked).
   - **Do:** compute the invariant core of a set of free variations and say
     which variant left the kind.
   - **Lab:** `variation`. Presets: `sound` (a tone varied in pitch, loudness,
     timbre and duration; duration zero is no longer a sound — the lesson's
     illustration of Husserl's method, not the book's), `table` (a table varied
     in material, height, legs; a table with no top), `melody` (a melody
     transposed: every note changes, the intervals do not — the Gestalt
     psychologists' example, which the Introduction will use). Pins the
     invariant-core tile.
   - **Misconception:** "Phenomenology is the study of essences, so it ends
     where the invariant is found." The Preface says essences are the means by
     which existence is brought into view; the core the lab prints is a tool,
     and the melody preset shows why: what stays is a relation, not a part.
   - **Worked:** across five variations of the tone, pitch, loudness and timbre
     all vary; having some duration stays.

4. **intentionality-and-rationality** — Intentionality and Rationality — *Preface*
   - **Read:** act intentionality and "operative" intentionality; rationality as
     perspectives that confirm one another; the closing comparison with the
     work of Balzac, Proust, Valéry and Cézanne.
   - **Do:** compute which faces of a cube three viewpoints see and whether
     their views are consistent with one solid.
   - **Lab:** `perspective/faces`. Presets: `three` (front, right and above:
     five of six faces seen across them, no single view more than three),
     `two` (front and back: four faces), `conflict` (two views that cannot be
     faces of one cube — refused with a sentence). Pins the union and the
     consistency tiles.
   - **Misconception:** "Rationality is a viewpoint above all viewpoints." On
     the Preface's account there is no view from nowhere to check the views
     against; rationality is the fact that they confirm one another, which is
     all the lab can compute.
   - **Worked:** front sees 1 face, front-right-above sees 3; union of three
     views 5; no view sees 6.

### Course 2 — Classical Prejudices (`perception-classical-prejudices`, 5)

Introduction, sections I–IV. The two opponents are built up first and then
taken apart: empiricism's sensation, association and projection of memories;
intellectualism's attention and judgement.

1. **the-idea-of-pure-sensation** — The Idea of Pure Sensation — *Introduction · I · "Sensation"*
   - **Read:** the white patch on a homogeneous background; the
     perceptual "something" always in the middle of something else.
   - **Do:** compute the grouping proximity predicts for a row of dots and say
     what a pure-sensation account must add to get it.
   - **Lab:** `grouping`. Presets: `pairs` (dots at 0, 1, 4, 5, 8, 9: three
     pairs), `even` (0, 2, 4, 6, 8: one group), `shift` (one dot moved: the
     grouping changes everywhere). Pins the groups tile.
   - **Misconception:** "A sensation is the simplest thing perception gives,
     so experience is built from such units." The chapter's claim is that the
     unit is a construction: the simplest thing perceived is already a figure
     on a ground. The lab: the groups are relations between dots and are not
     in any dot.
   - **Worked:** gaps 1, 3, 1, 3, 1; with the threshold at twice the smallest
     gap, three pairs.

2. **the-constancy-hypothesis** — The Constancy Hypothesis — *Introduction · I · "Sensation"*
   - **Read:** the constancy hypothesis — that a stimulus and the elementary
     perception correspond point for point; the Müller-Lyer illusion, whose
     lines "are neither equal nor unequal" (wording checked).
   - **Do:** compute the constancy hypothesis's prediction for two stimuli and
     the gap to a reported percept; decide two weights by Weber's fraction.
   - **Lab:** `stimulus`, views `illusion` and `weber`. Presets: `muller`
     (shafts 10 cm and 10 cm, reported difference illustrative 2 cm — the
     lesson says the magnitude varies with the fins), `equal` (no fins:
     predicted and reported agree), `weber` (100 g against 102 g, Weber
     fraction 1/50 for lifted weight, illustrative: "just noticeable"),
     `under` (100 g against 101 g: below). Pins the predicted, reported and
     gap tiles, and the Weber verdict.
   - **Misconception:** "The Müller-Lyer lines really look unequal, so
     perception is simply mistaken." Merleau-Ponty's point is not that
     perception errs but that the question "equal or unequal?" belongs to the
     objective world; in the perceived field the lines are not yet comparable
     in that way. The lab can only print the objective comparison.
   - **Worked:** 10 cm and 10 cm predict a difference of 0; reported 2 cm;
     the gap is the illusion only if the measured lines are the standard.

3. **association-and-the-projection-of-memories** — Association and the Projection of Memories — *Introduction · II*
   - **Read:** association by contiguity and resemblance; reading a misprinted
     word, where memory is said to fill in what was not seen.
   - **Do:** count the remembered words that fit a partly seen word, then
     after the context arrives, and say which did the selecting.
   - **Lab:** `cues`. One remembered-word list for every preset (the author
     designs it; about twenty common four- and five-letter words). Presets:
     `misprint` (pattern `ho_se`: house and horse both fit; the printed word
     was "hoxse"), `wide` (pattern `_a_e`: many fit), `context` (the pattern
     `_a_e` with the context tag "a door": one fits — gate). Pins the count
     and the candidates tiles.
   - **Misconception:** "Memory supplies what the senses leave out." The
     chapter's objection is that to call up the right memory the perceived
     word must already have the shape that memory is said to give it; the lab
     shows the memories do not select themselves — the pattern and the context
     select.
   - **Worked:** `ho_se` fits two remembered words; the letters alone cannot
     choose, and the sentence the word sits in does.

4. **attention-and-judgment** — Attention and Judgment — *Introduction · III*
   - **Read:** attention as a searchlight that changes nothing it lights;
     judgement as what the intellectualist adds to sensation; Descartes seeing
     "hats and coats" from the window and judging there are men.
   - **Do:** compute the size an unconscious inference would conclude from an
     angular size and an assumed distance, and compare it with the size seen.
   - **Lab:** `size/infer`. Presets: `moon` (the horizon moon's angle, assumed
     distance doubled: twice the size), `person` (a person 170 cm at 5 m and at
     20 m: the angle quarters, the size seen does not), `afterimage` (an
     afterimage "projected" on a near and a far wall — Emmert's law; the
     lesson attributes it). Pins the inferred-size tile.
   - **Misconception:** "Intellectualism and empiricism are opposites, so
     refuting one confirms the other." The chapter's claim is that both start
     from the same objective world and differ only in who builds the
     percept — the stimulus or the mind. The lab computes the
     intellectualist's inference from exactly the figures the empiricist used.
   - **Worked:** 170 / 500 and 170 / 2,000: the angle quarters; an inference
     with the right distance recovers 170 cm both times.

5. **the-phenomenal-field** — The Phenomenal Field — *Introduction · IV*
   - **Read:** the return to the phenomenal field as the first step of
     phenomenology, and psychology's place in it.
   - **Do:** compute each account's record across the Introduction's cases and
     name the case that splits the two classical accounts.
   - **Lab:** `cases`. Observations: the white patch on a ground, the
     Müller-Lyer, the misprint, the moon, attention's selective field
     (author designs; each cell justified in prose). Accounts: empiricism,
     intellectualism, the phenomenal field. Presets: `intro` (all), `two`
     (empiricism and intellectualism only), `one` (the Müller-Lyer alone).
     Pins the record and the splitting-case tiles.
   - **Misconception:** "The phenomenal field is a private inner world of
     appearances." The chapter places it before the split into inner and
     outer: it is the world as it is lived, not a mental picture of it.
   - **Worked:** five cases; empiricism absorbs two, intellectualism three,
     the split is the moon (author confirms against the coding).

### Course 3 — The Lived Body (`perception-the-lived-body`, 7)

Part One, its introduction and Chapters 1–3.

1. **experience-and-objective-thought** — Experience and Objective Thought — *Part One · Introduction*
   - **Read:** the house seen from nowhere, and the lamp and objects that see
     each other; the object as a horizon of views.
   - **Do:** compute what a house's faces look like from four viewpoints and
     state that the house is the system of views, none of them privileged.
   - **Lab:** `perspective/faces` with a house (a box 4 × 3 × 2, author's
     figures). Presets: `street`, `garden`, `above`, `everywhere` (all four:
     every face seen, but by no single view). Pins union and per-view tiles.
   - **Misconception:** "The house itself is the view from nowhere, and each
     view is a distortion of it." The chapter reverses it: "the house seen from
     nowhere" is what objective thought puts in place of the house.
   - **Worked:** street sees front and roof; the four views together see every
     face; no view sees more than three.

2. **the-phantom-limb** — The Phantom Limb — *Part One · Chapter 1*
   - **Read:** the phantom limb, and the failure of both the physiological and
     the psychological explanations of it.
   - **Do:** compute each explanation's record over the chapter's observations
     and name the observation each one cannot absorb.
   - **Lab:** `cases`. Observations from the chapter: severing the afferent
     paths to the brain abolishes the phantom; an emotion or a memory of the
     circumstances of the injury brings it back; the phantom keeps the
     posture of the arm at the moment of injury; it shrinks and is absorbed
     over time (author checks each against the text). Accounts:
     physiological, psychological, Merleau-Ponty's being-in-the-world.
     Presets: `all`, `physiology` (the nerve cases alone: physiology absorbs
     all), `memory` (the emotion case alone). Pins records and splitter.
   - **Misconception:** "The phantom is a mix of a nerve signal and a memory, so
     a combination of the two explanations suffices." The chapter argues the
     two cannot be added: one is third-person and the other first-person, and
     there is no common ground on which they meet.
   - **Worked:** physiological absorbs the nerve cases and fails the emotion
     case; psychological the reverse; neither absorbs all four.

3. **the-habitual-body** — The Habitual Body — *Part One · Chapter 1*
   - **Read:** the layer of the habitual body and the layer of the present
     body; manipulable objects that "appeal" to a hand that is gone.
   - **Do:** compute which objects are within reach for the habitual body and
     for the present body and name those that appeal only to the first.
   - **Lab:** `schema/habitual`. Presets: `cup` (an amputee with a cup on the
     right, at 60 cm: within the habitual reach, not the present), `left`
     (the same cup moved left), `none` (no amputation: the two bodies agree).
   - **Misconception:** "The amputee does not know the arm is gone." The
     chapter says the patient knows it, as one knows a fact, and still
     counts on the arm, as one is open to a situation: two layers, not one
     ignorance. Anosognosia is read the same way.
   - **Worked:** habitual reach 70 cm includes the cup at 60 cm; present
     reach 0 cm on that side excludes it.

4. **the-permanence-of-ones-own-body** — The Permanence of One's Own Body — *Part One · Chapter 2*
   - **Read:** the body as never in front of me, always with me; its
     "permanence" against the permanence of objects; double sensations.
   - **Do:** compare the viewpoints available on an object with those
     available on one's own body and compute which faces each leaves unseen.
   - **Lab:** `perspective/own`. Presets: `object` (a box walked around: every
     side seen), `own` (one's own head, viewpoints restricted to where the
     eyes are: the back never), `mirror` (with a mirror: a reversed view, the
     lesson says the chapter discusses it). Pins the unseen-faces tile.
   - **Misconception:** "Touching one hand with the other is touching and
     being touched at once." The chapter says the two never coincide: the
     roles alternate, and the touched hand never becomes the touching one in
     the same moment.
   - **Worked:** the box: 6 seen across viewpoints; the head: the back face
     unseen from every available viewpoint.

5. **the-body-schema** — The Body Schema — *Part One · Chapter 3*
   - **Read:** the body schema as more than an image or association of parts;
     the spatiality of situation against the spatiality of position; "here".
   - **Do:** compute an object's position relative to the hand as the body
     moves, against its position in the room, and name which stays fixed.
   - **Lab:** `schema/coordinates`. Presets: `still`, `turn` (the body turns a
     right angle: the object's room coordinates fixed, its body coordinates
     rotated), `walk` (the body moves 1 m). Pins both coordinate tiles.
   - **Misconception:** "The body schema is a map of the body the brain
     consults." The chapter's claim is that it is the body's grip on its
     tasks, not a representation consulted before moving.
   - **Worked:** cup at room (2, 1); body at (0, 0) facing east, then turned
     north; relative to the hand the cup moves from ahead-left to ahead-right.

6. **schneider-concrete-and-abstract-movement** — Schneider: Concrete and Abstract Movement — *Part One · Chapter 3*
   - **Read:** Gelb and Goldstein's patient: he performs concrete movements
     (taking a handkerchief, swatting a mosquito) but cannot point to a part
     of his body on command or perform an abstract movement except by
     preparatory movements.
   - **Do:** set out the observations, compute which tasks require the
     abstract attitude, and name the task that separates grasping from
     pointing.
   - **Lab:** `cases` with tasks as observations and two capacities as
     accounts (concrete movement, abstract movement) — the author codes the
     chapter's tasks. Presets: `tasks`, `eyes` (with eyes closed), `prepared`
     (with preparatory movements allowed).
   - **Misconception:** "Schneider's trouble is a visual deficit, so it is a
     problem of seeing and not of moving." The chapter takes up this reading
     (his injury was occipital) and argues it does not cover the case: the
     deficit is in the power of projecting a motor situation.
   - **Worked:** taking a handkerchief: concrete, done; pointing to the nose
     on command: abstract, not done.

7. **the-intentional-arc** — The Intentional Arc — *Part One · Chapter 3*
   - **Read:** the "intentional arc" that projects around us our past, our
     future, our human setting; motricity as original intentionality; "I can".
   - **Do:** compute the three accounts' records over the Schneider cases and
     name what the empiricist and the intellectualist each fail to absorb.
   - **Lab:** `cases` (empiricism, intellectualism, motor intentionality over
     the previous lesson's tasks). Presets: `all`, `classical`, `pointing`.
   - **Misconception:** "Motor intentionality is a reflex dressed in new
     words." The chapter's claim is that it is directed — at a task, a
     situation — which a reflex arc is not.
   - **Worked:** empiricism fails the pointing case, intellectualism the
     concrete case; motor intentionality absorbs both.

### Course 4 — Habit, Sexuality and Speech (`perception-habit-sexuality-and-speech`, 4)

Part One, Chapters 4–6.

1. **habit-and-the-blind-mans-cane** — Habit and the Blind Man's Cane — *Part One · Chapter 4*
   - **Read:** the body as like a work of art; habit as knowledge in the
     hands; the woman with a feather in her hat, the car through a gate, the
     typist, the organist, the blind man's cane.
   - **Do:** compute the reach and clearance of a body extended by a tool and
     say what has changed when the habit is acquired.
   - **Lab:** `schema/tool`. Presets: `hand` (reach 70 cm), `cane` (cane 1 m:
     reach 170 cm), `hat` (a feather 30 cm above a 165 cm head under a 190 cm
     door: clears), `car` (a car 180 cm wide through a 200 cm gate).
   - **Misconception:** "Habit is a reflex learned by repetition, an
     association of stimulus and response." The chapter: acquiring a habit is
     grasping a significance; the organist learns a new organ in an hour
     without learning a new set of reflexes.
   - **Worked:** 70 + 100 = 170 cm; a kerb at 150 cm is within reach of the
     cane, not the hand.

2. **the-body-as-a-sexed-being** — The Body as a Sexed Being — *Part One · Chapter 5*
   - **Read:** Schneider's sexual life; sexuality as a way of being in the
     world; the young woman who lost her voice after being forbidden to see
     the man she loved.
   - **Do:** compute the three accounts' records over the chapter's cases and
     name what the existential account adds.
   - **Lab:** `cases` (physiological, Freud's, existential, over the
     chapter's cases; author codes). Presets: `schneider`, `aphonia`, `all`.
   - **Misconception:** "Merleau-Ponty reduces sexuality to existence, or
     existence to sexuality." He says neither; the chapter's word is that they
     are interfused, and he discusses Freud and historical materialism to make
     the point that one does not explain the other.
   - **Worked:** physiology absorbs the injury, fails the aphonia; the
     existential account absorbs both on the chapter's coding.

3. **speech-as-gesture** — Speech as Gesture — *Part One · Chapter 6*
   - **Read:** the word has a meaning; speech does not translate a ready-made
     thought but accomplishes it; Gelb and Goldstein's amnesic aphasia and the
     colour-sorting test.
   - **Do:** compute a categorical sort of colour samples and a chain of
     concrete resemblances, and name the sample where they part.
   - **Lab:** `sorting`. Presets: `samples` (eight samples, three hue names,
     varying lightness: the categorical sort gives three groups, the chain
     wanders), `lightness` (all the same hue: the two agree), `close` (one
     dark red nearer a brown than to the pale reds).
   - **Misconception:** "The aphasic has lost words, and the words are labels
     on categories that are still there." Gelb and Goldstein's reading, which
     Merleau-Ponty takes up and then criticises, is that the patient has lost
     the categorial attitude; Merleau-Ponty's own is that the word and the
     category are not two things.
   - **Worked:** categorical: reds, greens, blues; chain from pale red: pale
     red → pink → … ends in brown.

4. **the-spoken-word-and-thought** — The Spoken Word and Thought — *Part One · Chapter 6*
   - **Read:** the gestural meaning of words; emotions and their expression
     differ by culture; the "speaking" and the "spoken" word.
   - **Do:** compute which accounts of meaning survive the chapter's cases and
     name the case against the conventional-sign view.
   - **Lab:** `cases` (meaning as association, meaning as thought, meaning as
     gesture). Presets as the author designs.
   - **Misconception:** "If speech is gesture, words mean by resembling what
     they name." The chapter denies it: the gesture is not an imitation, and the
     arbitrariness of signs is not denied but placed.
   - **Worked:** author's figures.

### Course 5 — Sensing and Space (`perception-sensing-and-space`, 7)

Part Two, its introduction and Chapters 1 and 2.

1. **the-theory-of-the-body-is-a-theory-of-perception** — The Theory of the Body Is a Theory of Perception — *Part Two · Introduction*
   - **Read:** the cube with six equal faces, which no perspective presents.
   - **Do:** compute the face widths a cube projects from a turned viewpoint
     and say what "six equal faces" is a claim about.
   - **Lab:** `perspective/faces` with rotations from the Pythagorean list.
     Presets: `square` (face-on: one face), `turned` (turned 3-4-5: two faces,
     widths 3/5 and 4/5), `corner` (corner-on: three).
   - **Misconception:** "The equal faces are what the cube looks like, once
     the distortions are corrected." The six equal faces are never seen; they
     are the thought of a cube seen from nowhere, and the chapter's claim is
     that the body is what makes a cube seen from somewhere a cube.
   - **Worked:** turned by the 3-4-5 angle, the two visible faces project at
     3/5 and 4/5 of their width.

2. **the-motor-physiognomy-of-colours** — The Motor Physiognomy of Colours — *Part Two · Chapter 1*
   - **Read:** Goldstein and Rosenthal's patients: red and yellow favour
     outward movements of the arm, blue and green inward ones; sensation as a
     "communion".
   - **Do:** compute the accounts' records over the chapter's colour cases.
   - **Lab:** `cases` (sensation as quality, sensation as motor attitude).
   - **Misconception:** "The colour is seen first and then it affects the body."
     The chapter's claim is that the motor significance is part of the
     colour's appearance, not a consequence.
   - **Worked:** author's figures.

3. **the-unity-of-the-senses** — The Unity of the Senses — *Part Two · Chapter 1*
   - **Read:** the senses communicate; synaesthesia as the rule; the
     congenitally blind after an operation.
   - **Do:** compute which properties of a thing survive across two senses.
   - **Lab:** `variation` (a thing presented to sight and to touch;
     properties that persist across presentations). Presets as the author
     designs.
   - **Misconception:** "Each sense has its own world, and the mind joins
     them." The chapter: the senses are not juxtaposed; the operated blind
     must learn to see, but not to join two worlds.
   - **Worked:** author's figures.

4. **up-and-down** — Up and Down — *Part Two · Chapter 2 · A*
   - **Read:** Stratton's inverting spectacles; Wertheimer's mirror tilting a
     room by 45°, which rights itself in minutes; the spatial level.
   - **Do:** compute the perceived tilt as image tilt minus spatial level, and
     the level's re-orientation over periods.
   - **Lab:** `level`. Presets: `wertheimer` (45°, level shifting by halves:
     45, 22½, 11¼ …), `stratton` (180°, adaptation over days — the lesson says
     Stratton's account is of eight days), `none`. Pins the perceived-tilt
     tile at period 1 and 3.
   - **Misconception:** "Up is where the retinal image's top is." Stratton
     shows the image can be inverted and up re-established; Wertheimer that
     the level is not given by the image at all.
   - **Worked:** image 45°, level 0: perceived 45°; level 30: perceived 15°.

5. **depth** — Depth — *Part Two · Chapter 2 · B*
   - **Read:** depth is not breadth seen from the side; convergence and
     apparent size as "signs" of depth in the classical theory.
   - **Do:** compute convergence and disparity for two distances and state
     what the classical theory says the mind does with them.
   - **Lab:** `depth`. Presets: `near` (6.5 cm interocular, 50 cm and 60 cm),
     `far` (5 m and 6 m: disparity a hundredth), `equal`.
   - **Misconception:** "We see depth by calculating from convergence."
     That is the classical theory the chapter states and rejects; the lab
     computes the calculation it says nobody performs.
   - **Worked:** 6.5 / 50 against 6.5 / 60: disparity 6.5·(1/50 − 1/60).

6. **movement** — Movement — *Part Two · Chapter 2 · C*
   - **Read:** Wertheimer's stroboscopic movement; Zeno; movement without a
     moving thing.
   - **Do:** compute the implied speed and whether an interval falls in the
     band of seen motion.
   - **Lab:** `motion`, views `phi` and `positions`. Presets: `simultaneous`
     (interval 20 ms), `optimal` (60 ms), `succession` (250 ms), `zeno` (an
     arrow's positions at ten instants: a list with no motion in it).
     Thresholds are Wertheimer's 1912 figures as usually reported (about 30 ms
     and 200 ms); the lesson says so.
   - **Misconception:** "Motion is a succession of positions of a moving
     thing." Zeno's argument against motion assumes it; the phi phenomenon
     shows motion with no thing moving.
   - **Worked:** two lights 5 cm apart at 60 ms: in the band; 250 ms: two
     lights, no motion.

7. **lived-space** — Lived Space — *Part Two · Chapter 2 · D*
   - **Read:** night, dream, myth and the schizophrenic's space; space as the
     space of an existence.
   - **Do:** compute which spatial features the geometric and the lived
     accounts each absorb over the chapter's cases.
   - **Lab:** `cases`.
   - **Misconception:** "Lived space is a subjective distortion of real
     space." The chapter: geometric space is a later and thinner structure.
   - **Worked:** author's figures.

### Course 6 — Things, the World and Others (`perception-things-world-and-others`, 7)

Part Two, Chapters 3 and 4.

1. **size-and-shape-constancy** — Size and Shape Constancy — *Part Two · Chapter 3 · A*
   - **Read:** perceptual constancies; a coin seen obliquely; the size of a
     person approaching.
   - **Do:** compute the ellipse a tilted disc projects and a Brunswik
     constancy ratio from a reported size.
   - **Lab:** `size/constancy`. Presets: `near` (a person 170 cm at 2 m, the
     standard), `far` (the same person at 8 m: the angle is a quarter, the
     retinal-equivalent size at 2 m is 42½ cm; reported 160 cm, illustrative:
     Brunswik ratio 235/255), `none` (reported equal to the retinal size:
     ratio 0). The coin seen obliquely is computed in prose from the
     Pythagorean tilt (axes 1 and 3/5), with no second lab.
   - **Misconception:** "The real shape is inferred from the projected one."
     The chapter: the real shape is not behind the appearance but is how the
     thing appears when seen at its best.
   - **Worked:** a disc tilted by the 3-4-5 angle projects axes 1 and 3/5.

2. **colour-and-lighting** — Colour and Lighting — *Part Two · Chapter 3 · A*
   - **Read:** Gelb's experiment; the lighting as what we see by, not what we
     see; Katz's film and surface colours.
   - **Do:** compute luminances and ratios to the surround and name the change
     that makes Gelb's disc look black again.
   - **Lab:** `light`. Presets: `room`, `gelb` (a black disc in a hidden
     spotlight: its luminance equals white paper's in the room), `paper` (a
     scrap of white paper placed in the beam: the ratio falls).
   - **Misconception:** "The disc looks white because it sends the eye white
     paper's light." Then it should stay white when the paper is added.
   - **Worked:** reflectance 1/20 × illumination 16 = 4/5, a white's
     luminance; paper 4/5 × 16 = 64/5; ratio 1/16.

3. **the-thing-and-the-real** — The Thing and the Real — *Part Two · Chapter 3 · B*
   - **Read:** the thing as intersensory, its qualities expressing one manner of
     being (the book's example of glass — its brittleness, hardness,
     transparency and ring — author checks the wording); the thing "in itself
     for us"; Cézanne.
   - **Do:** compute what the presentations of a thing to different senses
     have in common as qualities, and name what unites them instead.
   - **Lab:** `variation`, one variant per sense. Presets: `glass` (seen,
     touched, tapped, dropped: no quality common to all four — the core is
     empty), `style` (the same four with the lesson's coding of a manner,
     "brittle", carried by each: the core is that manner), `one` (a single
     sense: everything is "common").
   - **Misconception:** "The real thing is the sum of its sensory qualities,
     held together by the mind." The empty core is the lab's half of the
     answer; the chapter's half is that the unity is a style the qualities
     share, which is not one more quality.
   - **Worked:** four presentations, no common quality; one common manner.

4. **the-natural-world** — The Natural World — *Part Two · Chapter 3 · C*
   - **Read:** the world as the horizon of all horizons; a perception corrected
     by another perception, never by leaving the world (the author takes the
     chapter's own example of a corrected illusion).
   - **Do:** count the interpretations consistent with the cues as they
     arrive, and say what was never among the candidates.
   - **Lab:** `cues`, view `sequence` (interpretations as candidates, cues
     arriving one by one, each cue removing those it contradicts). Presets
     from the chapter's example, `first` (the first cue only), `all`.
   - **Misconception:** "Because any perception may turn out an illusion, all
     of them might." The chapter's reply is that an illusion is unmasked only
     by another perception, which counts on the world; the lab's candidates
     are all interpretations *of something there*.
   - **Worked:** three interpretations after the first cue, one after the
     third; "nothing there" is never a candidate.

5. **hallucination** — Hallucination — *Part Two · Chapter 3 · D*
   - **Read:** the patients who say their voices or visions are not like what
     they perceive; hallucination as lacking the perceived world's texture.
   - **Do:** compute the records of three accounts over the chapter's cases
     and name the case the empiricist account cannot absorb.
   - **Lab:** `cases`. Accounts: empiricism (a sensation from an inner cause),
     intellectualism (a mistaken judgement or belief), the chapter's own (a
     pseudo-world). Observations as the chapter reports them, author codes.
   - **Misconception:** "A hallucination is a perception without an object, so
     it is experienced exactly as a perception." The chapter's patients say it
     is not.
   - **Worked:** author's figures, from the coding.

6. **the-cultural-world-and-others** — The Cultural World and Others — *Part Two · Chapter 4*
   - **Read:** cultural objects; the argument from analogy and its circle.
   - **Do:** set out the argument from analogy and decide whether its premises
     force its conclusion.
   - **Lab:** `argkit/validity`. Presets: `analogy` (my body expresses my mind;
     that body is like mine; so that body expresses a mind — invalid in the
     propositional form the lab can state), `valid` (a deductive repair that
     adds the premise the argument needs), `circle` (the repair's premise is
     the conclusion).
   - **Misconception:** "The argument from analogy fails only because it is
     inductive." The chapter's objection is that it presupposes what it
     should explain: I would need to perceive the other as a behaviour first.
   - **Worked:** the truth table's one countercase.

7. **the-truth-of-solipsism** — The Truth of Solipsism — *Part Two · Chapter 4*
   - **Read:** the other's grief, which I see and do not live; a "lived
     solipsism" that cannot be surpassed; the social as a permanent field.
   - **Do:** compute three accounts' records over the chapter's cases and name
     the case on which coexistence and solipsism agree.
   - **Lab:** `cases`. Accounts: solipsism, the argument from analogy,
     coexistence. Observations: the infant who imitates before it knows it has
     a face (author checks), the grief seen and not lived, the conversation in
     which my thought and the other's are woven together, the social before
     any thematic knowledge of it.
   - **Misconception:** "Merleau-Ponty refutes solipsism." He says there is a
     truth in it that cannot be overcome, and that coexistence is lived before
     and beneath it; both claims are in the chapter.
   - **Worked:** author's figures; the grief case is the one both accounts
     absorb.

### Course 7 — The Cogito, Time and Freedom (`perception-cogito-time-and-freedom`, 7)

Part Three, Chapters 1–3.

1. **the-cogito-and-the-certainty-of-seeing** — The Cogito and the Certainty of Seeing — *Part Three · Chapter 1*
   - **Read:** Descartes' distinction between seeing and the thought of seeing,
     which is certain even if the seeing is not; the chapter's reply that the
     two certainties cannot be separated.
   - **Do:** set out the cogito read as an inference and decide what it needs
     to be valid.
   - **Lab:** `argkit/validity`. Presets: `bare` ("I think, so I exist": the
     form p, so q — invalid as stated), `major` (adding "if I think, I
     exist": valid), `seeing` ("I think I see a lamp, so I see a lamp":
     invalid — the gap Descartes relies on).
   - **Misconception:** "The cogito is an inference from thinking to being."
     Descartes himself denied it in the Second Replies; the lab shows why an
     inference would need a premise he does not want, and the chapter reads it
     instead as the experience of thinking.
   - **Worked:** the `bare` table's one countercase; the `major` table's none.

2. **the-triangle** — The Triangle — *Part Three · Chapter 1*
   - **Read:** the geometer's proof that a triangle's angles equal two right
     angles, by drawing a parallel through one vertex; the claim that the
     construction is a motor grasp of the figure, not a deduction from its
     definition.
   - **Do:** compute the third angle and the two alternate angles of the
     construction, and name what the construction adds to the definition.
   - **Lab:** `triangle`. Presets: `classic` (60°, 70°), `right` (90°, 30°),
     `thin` (1°, 1°), `refuse` (100°, 90°: no such triangle, refused with a
     sentence).
   - **Misconception:** "The angle sum follows from the definition of a
     triangle, as a consequence follows from axioms." The chapter's point is
     that the proof needs the parallel to be drawn and the figure to be seen
     anew; whether that makes the proof synthetic is the old dispute with
     Kant, which the lesson names.
   - **Worked:** 60 + 70 = 130; the third angle 50; at the parallel, 60 + 50
     + 70 = 180, a straight angle.

3. **the-tacit-cogito** — The Tacit Cogito — *Part Three · Chapter 1*
   - **Read:** the spoken cogito, learned from books, and the tacit cogito
     beneath it, which words presuppose.
   - **Do:** compute the accounts' records over the chapter's cases about
     language and thought.
   - **Lab:** `cases`. Accounts: thought before language, language before
     thought, the tacit cogito. Observations from the chapter, author codes.
   - **Misconception:** "The tacit cogito is a silent inner voice that thinks
     in words before speaking." The chapter says it is not yet a thought in
     words at all.
   - **Worked:** author's figures.

4. **time-is-not-in-things** — Time Is Not in Things — *Part Three · Chapter 2*
   - **Read:** the image of time as a river, and why it smuggles in an
     observer; time as a line of nows.
   - **Do:** classify moments on a line of nows as past, present and future,
     then remove the present and see what is left.
   - **Lab:** `time/line`. Presets: `present` (moments 1 to 7, present at 4),
     `move` (present at 6), `none` (no present: every moment is just a
     position, and "past" is empty).
   - **Misconception:** "Past and future are in the world, and we only
     observe them." The chapter: in things there is only the present of each;
     past and future need someone for whom they are past and future.
   - **Worked:** present at 4: three past, three future; no present: none of
     either.

5. **the-field-of-presence** — The Field of Presence — *Part Three · Chapter 2*
   - **Read:** Husserl's diagram of retention and protention, which the
     chapter reproduces; the "field of presence".
   - **Do:** compute, for a present, the depth at which each earlier moment is
     retained, and the span of protention.
   - **Lab:** `time/diagram`. Presets: `three` (A, B, C, present C: A at
     depth 2, B at depth 1), `later` (present D: everything sinks one step),
     `span` (a protention span of 2).
   - **Misconception:** "Retention is short-term memory, a stored copy of the
     moment just past." The chapter, after Husserl, says retention is not a
     copy recalled but the past held in the present's own thickness; recall
     is a different act.
   - **Worked:** at C, A is held at depth 2 through B's retention of it.

6. **the-rock-and-the-project** — The Rock and the Project — *Part Three · Chapter 3*
   - **Read:** Sartre's absolute freedom, which the chapter states before
     criticising it; the rock that is unclimbable only for someone who means
     to climb it; the claim that some rocks look high even before any project.
   - **Do:** classify rocks as obstacles relative to a project and then
     relative to the body's own general level, and name the rock that is an
     obstacle on the second reckoning and not the first.
   - **Lab:** `schema/obstacle`. Presets: `climb` (project climb, capacity
     2 m: the 3 m rock is an obstacle), `pass` (project walk past: none is),
     `body` (no explicit project, the body's general level 2 m: the 3 m rock
     still stands out).
   - **Misconception:** "Merleau-Ponty agrees with Sartre that freedom is
     absolute because obstacles exist only for a project." He agrees with the
     first half and denies the conclusion: the body gives a general
     valuation before any chosen project, which is why freedom is always in a
     field.
   - **Worked:** 3 > 2: obstacle for climbing; no project: none on Sartre's
     reckoning; one on the body's.

7. **freedom-in-situation** — Freedom in Situation — *Part Three · Chapter 3*
   - **Read:** the worker who becomes revolutionary, neither by a decision
     from nowhere nor by objective conditions alone; the closing lines, which
     quote Saint-Exupéry.
   - **Do:** compute the records of determinism, absolute freedom and freedom
     in situation over the chapter's cases, and name the case each of the
     first two fails.
   - **Lab:** `cases`. Observations from the chapter, author codes.
   - **Misconception:** "Freedom in situation is a compromise: partly free,
     partly determined." The chapter rejects the arithmetic of a share; it
     says we are free in a situation, wholly, and never outside one.
   - **Worked:** determinism fails the case of the decision that reinterprets
     the conditions, absolute freedom the case of the weight of a past.
     The course ends where the book does.

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
fraction, marked `≈`. Each mode has one pure `<xx>Compute(view, inst, opts)`
that `scripts/mathcheck.js` calls in its own block, each case seen to fail when
its line is broken on purpose. `phenkit` joins `KITS_WITH_EXPECTATIONS` at
wiring. Page budget: ≤ 40 KB gzipped per lesson.

**The Pythagorean angles.** A rotation or tilt input is one of a fixed list
of named angles whose cosine and sine are both rational: `0` (1, 0),
`3-4-5` (4/5, 3/5), `4-3-5` (3/5, 4/5), `5-12-13` (12/13, 5/13), `12-5-13`
(5/13, 12/13), `8-15-17`, `15-8-17`, `90` (0, 1), `180` (−1, 0), `270`.
The tile prints the exact cosine and the approximate degrees (`3-4-5: cos
4/5, ≈ 36.87°`). Any other angle is refused with a sentence that lists the
allowed ones.

**Model names.** Every view's `panel_intro` names the model it computes
("the constancy hypothesis", "unconscious inference", "the ratio principle").
The kit itself carries no claim that the model is right.

### D.1 Modes (prefix, views, inputs, tiles)

#### stimulus (`st`)
- `illusion`: `a` and `b` (measured magnitudes, with `unit`), `reported` (the
  reported difference, signed). Tiles: stPredicted (`0 cm` — the constancy
  hypothesis predicts the measured difference), stReported (`2 cm`), stGap
  (`2 cm`).
- `weber`: `base`, `compare`, `fraction` (Weber's k). Tiles: stDiff (`2 g`),
  stJnd (`2 g` = base × k), stVerdict (`noticeable` | `not noticeable`,
  `noticeable` when |diff| ≥ jnd), stConstancy (`different` whenever the
  stimuli differ — what the constancy hypothesis predicts).

#### grouping (`gr`)
- `proximity`: `points` (≤ 16 positions on a line), `ratio` (default 2: a gap
  at least ratio × the smallest gap separates groups). Tiles: grGaps
  (`1, 3, 1, 3, 1`), grGroups (`{0, 1} {4, 5} {8, 9}`), grCount (`3`). A strip
  of dots is drawn, coloured by group.

#### cues (`cu`)
- `pattern`: `words` (≤ 40), `pattern` (letters and `_`), `context` (a tag;
  words carry tags in the list as `gate:door`). Tiles: cuCount (`2`),
  cuCandidates (`horse, house`), cuContext (`gate` or `—` when no context).
- `sequence`: `candidates` (≤ 8, each with the cue ids it is consistent with),
  `cues` (ordered), `step` (redraw-only range 1..cues). Tiles: cuCount,
  cuCandidates, cuRemoved (the candidates the last cue removed).

#### size (`sz`)
- `angle`: `size`, `distance`, `unit`. Tiles: szRatio (`3474/384400 = 0.0090
  rad`, the ratio reduced, printed with four decimals), szDegrees (`≈ 0.52°`).
- `infer`: `size`, `distance`, `assumed` (an assumed distance). Tiles:
  szRatio, szInferred (`size × assumed / distance`, e.g. `340 cm`).
- `constancy`: `size`, `distance`, `standard_distance`, `reported`. Tiles:
  szRetinal (the size that would subtend the same angle at the standard
  distance), szBrunswik (`(reported − retinal) / (true − retinal)` exact and
  as a percentage: `1` is full constancy, `0` none).

#### perspective (`pe`)
- `faces`: an object (`cube` or `box` with three dimensions), `views` (≤ 6,
  each a named direction from the list front, back, left, right, above,
  below, or a Pythagorean rotation of front about the vertical axis). Tiles:
  peVisible (per view, the faces seen and each face's projected width as a
  fraction of its true width), peUnion (faces seen by some view, `5 of 6`),
  peMax (`3`), peConsistent (`yes` / `no`: `no` when two views report widths
  no single box can give).
- `own`: as `faces`, with `restricted` (the viewpoints a body has on itself;
  the lesson lists them). Tiles: peUnion, peUnseen (`back`).
- `necker`: `object` (`cube` | `box` | `solid`), oblique projection offsets.
  Tiles: peEdges (`12`), peReadings (`2` for a wire figure, `1` for a solid),
  peSame (`identical drawings` when both readings project to the same edge
  set).
- `shape`: `tilt` (a Pythagorean angle), `diameter`. Tiles: peAxes
  (`1 and 3/5`), peRatio (`3/5`).

#### variation (`va`)
- `core`: `variants` (≤ 10, each `name: p1 p2 …; kind yes|no`). Tiles:
  vaCore (properties in every variant still of the kind, or `none`), vaVary
  (properties that vary), vaBreak (variants marked not of the kind, and the
  properties they lack from the core).

#### cases (`ca`)
- `table`: `accounts` (2 to 4 names), `observations` (≤ 10, each with one cell
  per account: `y` consistent, `n` inconsistent, `-` silent). Tiles: caRecord
  (per account `absorbs 3 of 4, fails 1, silent 0`), caSurvivors (accounts
  with no `n`, or `none`), caSplit (observations on which two named accounts
  differ, `y` against `n`), caPair (redraw-only select choosing the two
  accounts caSplit compares).

#### schema (`sc`)
- `coordinates`: `body` (position and a facing from the Pythagorean list),
  `objects` (≤ 6 room positions). Tiles: scRoom (`cup (2, 1)`), scBody (`cup
  ahead 1, left 2` — coordinates relative to the body).
- `habitual`: `habitual_reach`, `present_reach` (per side, left and right),
  `objects` (side and distance). Tiles: scHabitual (objects in habitual
  reach), scPresent, scAppeal (in the first and not the second).
- `tool`: `reach`, `tool` (length), `height`, `clearance`, `objects`
  (distances), `openings` (a width or height to pass). Tiles: scReach
  (`170 cm`), scWithin, scClears (`clears by 30 cm` | `does not clear`).
- `obstacle`: `rocks` (≤ 8 heights), `project` (`climb` | `pass` | `none`),
  `capacity`, `general_level`. Tiles: scProject (rocks that are obstacles for
  the project; for `pass`, none; for `none`, none), scBody (rocks above the
  body's general level, whatever the project).

#### sorting (`so`)
- `sort`: `samples` (≤ 12, each `name, hue, lightness`), `start`. Tiles:
  soCategorical (groups by hue name), soChain (the chain from `start`: at each
  step the unsorted sample nearest the last one picked, by |Δ lightness| plus
  1 if the hue differs, ties broken by list order — the rule is printed),
  soPart (the first sample where the chain leaves the start's hue).

#### level (`le`)
- `tilt`: `image` (degrees, a rational from −180 to 180 — no trigonometry is
  needed here, because a tilt of the field is subtracted, not projected),
  `level` (the starting level), `share` (the share of the remaining
  difference the level moves each period), `periods` range 1..10. Tiles:
  lePerceived (`image − level` at the shown period), leLevel, leSeries (the
  first five periods).

#### depth (`de`)
- `binocular`: `iod` (interocular distance), `near`, `far`. Tiles:
  deConvergence (per distance, `iod / d` exact, as radians with four
  decimals), deDisparity (`iod·(1/near − 1/far)`), deRatio (how many times
  smaller the disparity is at the second preset — computed within the
  preset as `near` and `far` scale).

#### motion (`mo`)
- `phi`: `separation`, `interval` (ms), `simultaneous` and `succession`
  thresholds (defaults 30 and 200, from the lesson's source). Tiles: moSpeed
  (`separation / interval`, e.g. `1/12 cm per ms`), moBand (`seen together` |
  `motion` | `seen in succession`).
- `positions`: `start`, `step`, `instants` (≤ 12). Tiles: moList (the
  positions), moMoving (`no position contains motion` — a fixed string printed
  under every input, which the lesson discusses: it is the lab's whole
  point).

#### light (`li`)
- `ratio`: `surfaces` (≤ 6, each `name, reflectance, illumination`),
  `surround` (the name of the surface that is the surround). Tiles:
  liLuminance (per surface), liRatio (each surface's luminance over the
  surround's), liBrightest.

#### triangle (`tr`)
- `parallel`: `a`, `b` (degrees, rationals). Refused unless 0 < a, 0 < b,
  a + b < 180. Tiles: trC (`180 − a − b`), trAlternate (`a and b`, the two
  alternate angles at the parallel), trStraight (`a + c + b = 180`). An SVG
  draws the triangle and the parallel.

#### time (`ti`)
- `line`: `moments` (≤ 9 names), `present` (a name or `none`). Tiles: tiPast,
  tiFuture, tiPresent.
- `diagram`: `moments`, `present`, `protention` (span). Tiles: tiRetained
  (`A at depth 2, B at depth 1`), tiProtended (`E, F`), tiColumn (the
  vertical of the diagram at the present). An SVG draws Husserl's diagram:
  the horizontal of nows, the obliques of sinking, the vertical at the
  present.

### D.2 `argkit/validity` reused

Exactly as `content/philosophy/c1_arguments/part_a.py` uses it: `premises`,
`conclusion`, `show`; tiles vaVerdict, vaCounter, vaRows. Sentence letters are
named in the lesson prose.

### D.3 What the kit must never do

- Print a figure that claims to be an experience ("perceived size: 340 cm"
  is printed as "the size an inference would conclude").
- Accept an angle that needs trigonometry.
- Decide a `cases` cell. The coding is the lesson's; the kit only counts.

---

## §E Package layout, the source text, and quoting a book in copyright

### E.1 Layout

```
content/phenomenology/
  __init__.py                       PATH, COURSES, numbering loop
  c1_preface/__init__.py            COURSE; lessons = part_a.LESSONS
  c1_preface/part_a.py
  c2_prejudices/ c3_lived_body/ c4_habit_speech/ c5_sensing_space/
  c6_things_others/ c7_cogito_time_freedom/
content/spoken/phenomenology.py     SPOKEN = {}
```

A course with more than six lessons splits into `part_a.py` and `part_b.py`
at its midpoint.

### E.2 The source text

The operator owns a physical copy; the edition the lessons cite, and how its
text reaches the authors, is recorded here when settled. Until it is, no
quotation is written, and lessons are not authored.

### E.3 Quoting

*Phenomenology of Perception* is in copyright in French (Gallimard, 1945) and
in both English translations (Colin Smith, Routledge, 1962; Donald A. Landes,
Routledge, 2012). The Subject quotes it for commentary, and keeps quotation
small:

- The opening passage is at most **70 words**, cited by page in the
  translation the course names.
- A lesson's quotations, the opening passage included, total at most **150
  words**, about one five-hundredth of the book per lesson.
- Every quoted phrase is copied from the source text, character for
  character, and its page is in a comment beside the lesson dict. Never from
  memory, never from another translation, never from a secondary source.
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
not endorsed.

What is different for this book:

1. **The lectures were about perception.** The first of them reads the *Tao
   Te Ching*'s first chapter through a theory of the mind as a prediction
   machine: a tomato a metre away is a hypothesis the brain builds from
   signals; a Roomba needs a model of the room and a model of itself to know
   where it fits; perception is "a controlled hallucination" (Anil Seth). The
   second turns to bodily learning and flow: practice that becomes second
   nature. These are exactly the views and the phenomena the book is about —
   and Merleau-Ponty would call the first "intellectualism" and the second
   the body's own knowledge. So a lesson may set the chapter beside the
   modern view the lectures voiced, once, at strength, where the chapter is
   about the same phenomenon: the constancy hypothesis and predictive coding;
   the body schema and the Roomba's model of itself; the phantom limb and
   Ramachandran's mirror box; habit and the expert's flow. Never more than one
   such aside per lesson, never as settling the chapter, and never in the
   form "science has proved Merleau-Ponty right" or "wrong".
2. **Everyday scenes are easy here, so ration them.** Perception is in the
   reader's life all the time; a lesson that opens with "look at the cup on
   your desk" every time becomes a formula. Open with a scene in at most half
   of a course's lessons; open the rest with the passage's own case — Schneider,
   Stratton, Gelb's disc.
3. **The cases are people.** Schneider was a soldier wounded in 1915; the
   amputees, the aphasics and the patients who hallucinate are patients. Name
   them as the book does, with the respect the book shows, and never for an
   effect.
4. **Merleau-Ponty is presented, not endorsed.** He is arguing with
   Descartes, Kant, Husserl, Sartre, Bergson and the psychologists, and every
   one of them is stated in their own terms and at strength before he answers.
   Where a reading of him is disputed (the reduction, the tacit cogito, his
   relation to Husserl), the lesson says it is disputed.

**One exemplary paragraph** (a `p` block for “The Constancy Hypothesis”, after
the passage):

> You have almost certainly seen the two lines with arrowheads, one with the
> fins turned out and one with them turned in, and been told that they are the
> same length. Measure them and they are. The lab does the measurement for
> you: ten centimetres and ten centimetres, so the theory Merleau-Ponty calls
> the constancy hypothesis — that each point of the stimulus produces its own
> point of sensation — predicts that you will see no difference at all. You
> see one. The usual way of putting this is that perception has made a
> mistake, and the textbook calls the figure an illusion. Merleau-Ponty's
> reply is stranger and more interesting: the mistake is in the question.
> "Equal" and "unequal" belong to a world where lines are laid side by side
> and measured; in the field you are looking at, the two lines are not yet
> the kind of thing that is either.

---

## §G What is left out, and why

- **Merleau-Ponty's other works**: *The Structure of Behaviour* (1942), *The
  Visible and the Invisible* (posthumous), the essays on Cézanne and on
  language. Named where the book points to them; not read.
- **The secondary literature's disputes** over the book's relation to Husserl
  (especially the late manuscripts), to Heidegger and to Sartre. A lesson
  says where its reading is disputed and goes no further.
- **The later status of the psychology.** Gelb and Goldstein's case of
  Schneider was re-examined in the 1980s and 1990s, and some of their
  findings have been questioned; the course `not_covered` says so, and the
  Schneider lessons say in a sentence that the book's argument concerns the
  case as reported. The modern experiments the lectures' views rest on are
  asides, never evidence the lab computes.
- **Psychophysics beyond what the chapter uses.** Weber's fraction appears
  because the constancy hypothesis is a psychophysical claim; Fechner's law,
  signal detection and the like do not.
- **Trigonometry.** The kit's Pythagorean angles are a deliberate limit, so
  that every figure stays exact.

---

## §H Wiring notes for the orchestrator

As `docs/capital/PLAN.md` §H and AGENTS.md §0's list, with these values:

- Package `phenomenology`; path slug `phenomenology`; check-id prefix `php`.
  Check ids take the form `php-course7-lesson-<lesson-slug>`.
- `PHEN_DISCLAIMER_RE = r"what perception gives is not a figure"`.
- `content/spoken/phenomenology.py`; `phenomenology_semantic_copy` in
  `test_public_copy`.
- Register `phenomenology` in `GENERATED_PATHS` at the start of the branch with
  every `COURSE = None`; add `"phenkit"` to `KITS_WITH_EXPECTATIONS` last.
- Eleven Subjects after wiring; every "ten Subjects" count is updated in the
  wiring commit.

---

## §R Review record

(Appended by the orchestrator.)
