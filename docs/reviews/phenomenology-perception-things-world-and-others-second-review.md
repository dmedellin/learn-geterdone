# Second review: Things, the World and Others (`perception-things-world-and-others`)

Reviewer: independent second read, to `docs/phenomenology/SECOND-REVIEW.md`, held
also to the "Lessons from" sections of `docs/phenomenology/AUTHORING.md`.
Package `content/phenomenology/c6_things_others/` (seven lessons, `part_a.py`
lessons 1–4, `part_b.py` lessons 5–7). Every lesson was read whole against
Smith pp. 348–425, read in full (Part Two, Chapters 3 and 4), not only the
quoted passages. The findings below were written before the pedagogy
assessment was opened.

**Overall.** The course is careful. Every figure is right (with one wrong
`why`), every quotation is Smith's and in the voice the lesson says, the
reading ranges are exact, and the voice is the Subject's. The errors are the
kind the Course 1 review predicted: a view given a voice or a strength the
chapter does not give it, an example called something the chapter does not
call it, and one modern aside that put a reply in Merleau-Ponty's mouth.

Note on concurrency: the pedagogy reviewer was editing the same two files while
I worked. Four of my findings (the lamp-post `why`, the Koffka footnote, the
two boxes, and the Sartre attribution in lesson 7) had been fixed by them in
the file by the time my edits landed; I record them as findings and say where
the fix in the file is theirs.

## Checks run (final)

- `python3 -I …/tools/phen_quotes.py c6_things_others`: every span found;
  per-lesson totals 106 / 141 / 100 / 112 / 146 / 105 / 149 words, openings
  61 / 65 / 50 / 36 / 49 / 45 / 55; final line `OK`. No misses, no cap overruns,
  nothing convention-only to list.
- `python3 scripts/preview_subject.py phenomenology --course perception-things-world-and-others --out <scratch>/rev2-c6`:
  8 pages, 7 labs executed, 7 with pinned figures, 0 failing; final line `OK`.
- `node scripts/labcheck.js --observe` on every lesson page: every preset's
  tiles read and checked against the prose (below).

## Arithmetic and models (all recomputed)

- Lesson 1: 170 × 2/8 = 85/2; (85/2) × 8/2 = 170; (85/2) × 4/2 = 85;
  (160 − 85/2)/(170 − 85/2) = (235/2)/(255/2) = 47/51 ≈ 92.2%; `none` 0,
  `full` 1. The `misjudged` preset's Brunswik tile still reads 47/51 (the ratio
  uses the true size), which the prose does not claim otherwise. Correct.
  Quiz 1: 6 × 2/30 = 2/5; 6 × 30/2 = 90. **Wrong `why`:** the distractor 1/10
  was said to "forget the standard distance", but forgetting it gives 6/30 =
  1/5; 1/10 = 6/(30 × 2) divides by it. In the file now: the pedagogy reviewer
  changed the distractor to 1/5 with a matching `why`, which is also right.
- Lesson 2: 1/20 × 16 = 4/5; 4/5 ÷ 1/2 = 8/5; 1/20 ÷ 1/2 = 1/10; 4/5 × 16 =
  64/5; 4/5 ÷ 64/5 = 1/16. Quiz 1: 3/10 × 4 = 6/5, ÷ 2 = 3/5; each distractor's
  error is as the `why` says. Correct, and each figure is credited to the
  empiricist's luminance or to Wallach (1948), never to what is seen.
- Lesson 3: n,y / n,n / y,n gives 1 of 3, 2 failed each; split rows 1 and 3;
  `qualities` 0/2 vs 1/2, no survivor; `alien` empiricism survives. Correct.
- Lesson 4: 3, 2, 1 candidates; removed none, poplars, church. Correct.
- Lesson 5: cores and breaks as the tiles print; single-variant presets give
  `vrVary` none, which the prose says. Quiz 1 core p, D lacks p. Correct.
- Lesson 6: 8 rows / 1 counterexample / Invalid; 8 / 0 / Valid; 4 / 0 / Valid;
  `vaForm` "no catalogued form" for all three, as the prose says. Correct.
- Lesson 7: analogy n,y,n,- → 1 absorbed, 2 failed, 1 silent; look y,y,n,y →
  3 / 1 / 0; split the baby only (silence excluded); `infant` the look
  survives; `dialogue` no survivor, no split. Correct.

## Findings by lesson

### 1. Size and Shape Constancy

1. **The second answer called "stronger".** The lesson said "The second answer
   is stronger". Smith p. 349 introduces it as what "would seem, at least at
   first glance, to be a way of evading the question", and p. 351 asks whether
   it has really left the psychologist's problems behind. A verdict between
   opponents in the lesson's own voice, and the opposite of the chapter's
   framing. **Changed** to "looks at first, the chapter says, like a way round
   the question".
2. **Kant as "the view's best advocate"; Helmholtz's computation stated "as
   Kant's".** The text says that following out the law view "we should, with
   Kant, see" a rigorously interrelated world (p. 351); the "constant product
   of the distance multiplied by the apparent size" is what the object is "for
   science and objective thought" (p. 351), not Kant's. The lesson said the
   chapter states the inference view "as Kant's and objective thought's", and
   `mistakes[0]` said "in Kant's terms". **Changed** both: Kant "is where the
   view leads"; the product is stated "for science and objective thought";
   the Helmholtz sentence now says the chapter does not name him and that the
   product it states is the same computation.
3. **Koffka footnote.** "the note concludes" that constancy is existential: the
   note (p. 353 n. 2) opens with that sentence. Fixed in the file (the
   pedagogy reviewer's wording, "the note begins by saying", landed first).
4. **Brunswik undated.** The def named Brunswik without a date; PLAN §C says
   the ratio dates from about 1930 and the lesson must not call it later than
   the book. **Changed:** "who proposed it around 1930". (Brunswik's ratio
   comes from his constancy work of 1929–33; Egon Brunswik, 1903–1955.)
   The tile label no longer says "later than the book" (checked on the page).
5. Quiz 1 `why` (above, arithmetic).
6. Helmholtz's *Treatise on Physiological Optics* (1856–67) and "unconscious
   inference": accurate. Kant's Dialectic/Analytic remark (p. 354), the pen,
   the oblique square, the optimum distance, the "tension which fluctuates
   round a norm" (p. 352): all on the pages given.

### 2. Colour and Lighting

1. **Gaslight put under the screen.** The lesson said a screen with a small
   window turns one mode into the other, giving as its examples the bluish-grey
   wall *and* the gaslit blue paper. In Smith p. 357 the gaslit paper is a
   photometer case in free vision (Hering's), the screen case is the wall.
   **Changed:** the two are separated and the photometer named.
2. **Gelb's disc in the beam set against the empiricist's prediction.** The
   lesson said that if luminance were colour the disc would have the paper's
   colour, and then "As the chapter reports it, what is seen is a faintly lit
   disc", which reads as a refutation. Smith p. 358 does not say the disc does
   not look white (the PLAN §C entry notes it does not say it does either); the
   standard report of Gelb's effect is that it does. The failure of the
   empiricist's model comes with the paper. **Changed:** the sentence now
   reports p. 358 and says "nothing yet shows a black disc under a strong
   light. The test comes with the paper."
3. **The two boxes.** "Put a white paper in the black box and at once it
   appears black" left "it" open to the paper. Smith: "the former appears as
   black and strongly illuminated", the former being the black box. Fixed in
   the file (the pedagogy reviewer's "the box", landed first).
4. Hering's *Gedächtnisfarbe* (p. 354 n. 3), Katz's *Flächenfarben* /
   *Oberflächenfarbe* (p. 356) and the further modes, Gelb's boxes and disc
   (pp. 358, 363; Gelb, *Die Farbenkonstanz der Sehdinge*, 1929), Scheler
   (p. 355), Wallach 1948: accurate. Gelb and Katz are undated in the lesson;
   that is acceptable, and a recommendation only (Katz's *Der Aufbau der
   Farbwelt*, the book cited, is 1930).

### 3. The Thing and the Real

1. **"The two accounts the passage is aimed at".** The passage rejects a
   substratum, a vacant X, a subject of inherence: the traditional
   substance picture, not the Introduction's two accounts. Those are named on
   p. 370 (a collection of attributes, or the notion of it). **Changed** to
   "The two accounts these pages set aside".
2. Coding of the three cells checked against pp. 372, 376, 379–80; it is
   defensible and the `note` says the hot object could be coded silent.
   Novotny, Sartre's *L'Imaginaire* (p. 377 n. 58), the die's four reductions
   (pp. 378–9), the pebble (p. 380): accurate.

### 4. The Natural World

1. **Chartres called "a corrected perception".** The last `p` called the town
   "this chapter's own example of a corrected perception". In Smith p. 384 it
   is two appearances with no common measure, welded by the judgement "It is
   Chartres"; nothing is corrected. **Changed:** "two appearances welded by a
   judgement rather than an illusion corrected", with the stone (p. 346) as
   the book's best-known corrected illusion.
2. "the section ends" with the mystery: the mystery is p. 388–9, and the
   section runs on a paragraph. **Changed** to "says near its end".
3. Descartes's First Meditation is paraphrased accurately ("prudent never to
   trust wholly"). Recommendation: the mistake's "at strength" could add that
   Descartes himself grants some sense reports are hard to doubt and needs the
   dream argument to go further; not changed (taste).
4. The model is called both "the lesson's model" and "the sceptic's picture";
   it is family 1 (an opponent's). Recommendation: "The lab's model is the
   sceptic's picture" in body paragraph 6.

### 5. Hallucination, and the modern aside

1. **The Seth aside put a reply in Merleau-Ponty's mouth.** "The chapter would
   answer that…" (the file also briefly had "Seth would see his view in that",
   which the pedagogy reviewer had already reworded to "a reader of Seth can
   point to that"). Merleau-Ponty answers nobody who wrote later
   (AUTHORING, Lessons from Capital). **Changed** to what in the chapter bears
   on it: "Against him, what the chapter says perception has is a place in a
   world shared with others and a fullness of detail".
2. **Seth's side not quite at strength, and the chapter's nearest sentence
   missing.** Seth's own corollary, that hallucination is perception less
   held in check by the senses, was absent, and so the "other way" contrast
   looked starker than his view is. And the chapter's footnote on p. 395
   (n. 74) repeats, without objection, Palágyi's description of perception as
   a "direct phantasm" and hallucination as an "inverse phantasm", the
   closest thing in the book to Seth's phrase. **Changed:** both added; the
   lesson's quotation total rises from 142 to 146 (cap 150). "sets this
   chapter in an unexpected light" (performed) became "runs close to this
   chapter and the other way from it".
3. **Attribution of the phrase.** "a phrase he did not coin" is accurate:
   Seth disclaims the coinage and credits earlier users. I could not confirm
   from here which earlier user is first, so the lesson rightly names none. Placement (second-last `p`, after the
   chapter's conclusion) and the single aside per course: as §F.1 requires.
   Both sides are now stated, and neither is said to settle it.
4. The patients: named as the book names them (schizophrenics, the old woman
   with senile dementia, delirium tremens), the reports credited to the
   sources (Zucker, Minkowski, Schröder, Specht, Jaspers), and the §F.3
   sentence that the lab codes the reports is present twice. Sartre's
   mescaline self-observation (p. 397 n. 78) correctly attributed. Respectful
   throughout.

### 6. The Cultural World and Others

1. **The circle presented as "the chapter's objection".** The chapter's
   objection (p. 410) is that the perception of others is anterior to the
   comparisons and correlations. That q (that body *behaves* as mine) already
   requires r is the lesson's reconstruction of it, a fair one, but a
   reading. **Changed:** "the lesson's way of setting the chapter's objection
   out in the lab's terms", and "On this reading, that is what presupposing…
   amounts to".
2. **Quiz 2 distractor partly supported.** "It compares bodies that are in
   fact unlike" is something the chapter partly says (the baby's teeth are not
   like mine, p. 410), so a reader could defend it. **Changed** to "It fails
   because no two bodies ever behave exactly alike", with the `why` adjusted.
3. Mill 1865 (*Examination of Sir William Hamilton's Philosophy*), Scheler's
   *Sympathiegefühle* 1913 / *Wesen und Formen der Sympathie* 1923, Piaget at
   about twelve (p. 414), Hegel's struggle (p. 414), "two modes of being" as
   objective thought's (p. 407): accurate.

### 7. The Truth of Solipsism, and Sartre

1. **Sartre stated as the chapter's target.** The body said "That is the
   analysis Jean-Paul Sartre gave in *Being and Nothingness*… and the chapter
   answers it". The chapter names no one: "it is asserted" (p. 420), as "it is
   said" a line earlier. PLAN §C requires "widely read as Sartre's". The
   concept, the `note` and `not_covered` already hedged; the body did not.
   Fixed in the file (the pedagogy reviewer's "That is widely read as the
   analysis…" landed first). The summary of Sartre (the look reveals me as an
   object in his world, felt as shame; the theft of my world) is accurate and
   at strength.
2. The look's language also occurs on pp. 410–11 and 416 in the chapter's
   statement of the difficulty ("The cogito of another person strips my own
   cogito of all value"; the other's gaze has "stripped me of part of my
   being"). `mistakes[1]` handles p. 416 well. Recommendation only.
3. Paul (p. 415), the unequal couple and the chessboards (p. 416), "solipsism
   rooted in living experience" (p. 417), Spinoza (p. 418), Valéry (p. 420 n.),
   the stranger and the dog (p. 420), Péguy, the peasants of 1917, Fabrice
   (Stendhal's, correctly glossed) and Waterloo (p. 422), death and the social
   atmosphere (pp. 424–5): accurate. The concept title "Lived solipsism" is
   the lesson's label for Smith's "rooted in living experience"; acceptable.

### Course dict (`__init__.py`)

1. `how_to` said the chapters state the objectifying look's view "at length";
   it is stated in two sentences (p. 420). **Changed** to "in their own words,
   some of them at length".
2. `not_covered` said Scheler, Husserl and Hegel are "each named where the
   chapter draws on him" on other minds; Husserl is not named in these pages
   on other minds, nor in lessons 6–7. **Changed:** "Scheler and Hegel are
   named…".
3. `not_covered` headed Brunswik under "The psychology of constancy since the
   book"; Brunswik's ratio is about 1930. **Changed** to "beyond the chapter".
4. "Part Two, The World as Perceived" is Smith's Part II title (contents p.;
   PLAN §E.2 lists only the Part's introduction title). Correct.

## Outside this course (not changed; reported)

- PLAN §G and the §0 table say Brunswik's ratio is "later than the book". It is
  not (about 1930); §C for this course already says so. §G is shared, so I
  did not edit it.

## Quiz: every distractor argued

All 28 questions were tried. One distractor was defensible (lesson 6 Q2,
changed); one `why` was wrong (lesson 1 Q1, fixed). The rest have exactly one
answer the text supports.

## Voice

Natural and warm; the corridor (lesson 1) is the only everyday opening, well
within §F.2. The one performed phrase was "an unexpected light" (changed).
"the chapter's strongest sentence" (lesson 7) is a verdict on the chapter's
own rhetoric, not on a side; left. No slang, no first person, no "let's".
Every last `p` points to the next lesson by title; lesson 7 to Course 7's
first lesson, "The Cogito and the Certainty of Seeing", which exists.

## Where I disagree with the pedagogy assessment

`docs/pedagogy/phenomenology-perception-things-world-and-others.md` did not
exist when these findings were finished, so there is nothing to compare yet.
Its author was evidently working in the same files at the same time: four of
the fixes above (lamp-post `why`, Koffka note, the two boxes, Sartre hedged in
lesson 7) and the softening of "Seth would see his view in that" are theirs in
the file, and agree with my findings. Whoever reconciles the two reviews
should check that their later edits did not reintroduce any wording changed
here (final checker and preview runs after my last edit: both `OK`).
