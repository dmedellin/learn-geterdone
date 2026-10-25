# Second review: What Phenomenology Is (`perception-what-phenomenology-is`, `c1_preface`)

Independent second read, per `docs/phenomenology/SECOND-REVIEW.md`. I read the
whole Smith Preface (pp. vii–xxiv), plus the pages the lessons point to later in
the book (Introduction III, pp. 32 and 36; Part One introduction, p. 77; Part Two
Chapter 2, pp. 302 and 306). Then I checked every sentence in the four lessons
that says what Merleau-Ponty argues against those pages. I wrote these findings
before reading the pedagogy assessment.

Files changed: `content/phenomenology/c1_preface/part_a.py` only. Nothing in
§C had to change, because none of the fixes alters an instance, a misconception
or a worked line in `docs/phenomenology/PLAN.md`.

Final checks after the changes:

- `python3 scripts/preview_subject.py phenomenology --course perception-what-phenomenology-is --out <scratch>/sr-c1`:
  every lab executes on 4 pages, 4 with pinned figures, 0 failing. Final line: `OK`.
- `python3 -I <scratch>/tools/phen_quotes.py c1_preface`: 117 / 129 / 137 / 139 quoted
  words (openings 68 / 66 / 43 / 56), no misses. Final line: `OK`.

## Findings: what the text says

### 1. The Reduction and Its Limit: the Descartes remark taken out of its concession (fixed)

The lesson quoted p. x, "methodical doubt does not deprive us of anything", as
"the Preface's own remark on Descartes". It then drew from it that "Descartes's
doubt withdraws assent to find a firmer ground". In Smith the sentence sits
inside a concession made to the idealists ("It is true that … And in Descartes
…"), and the objection follows at once: "But the relations between subject and
world are not strictly bilateral". If they were, the world's certainty would be
given with the Cogito's. What the cogito wins back is the world labelled
"thought of". As written, the lesson used a remark that says doubt loses nothing
to support the claim that doubt withdraws something, and it dropped the
objection that is the Preface's actual point.

**Changed:** the paragraph now presents the remark as the concession it is,
states the objection (the world comes back only as thought), and then draws the
contrast with the reduction "on the Preface's reading". The quotation is
unchanged.

### 2. Description, Not Explanation: the cardboard-tube test given to the book (fixed)

"The book's own version of the test is a cardboard tube or a telescope, through
which, it reports, the horizon moon looks no bigger than at the zenith." On
p. 32 that claim is in the intellectualist's voice ("The moon on the horizon is
not, and is not seen to be, bigger…"). On p. 36 Merleau-Ponty turns it round:
from the tube "the conclusion cannot be drawn" that free vision is invariable,
because the tube gives analytic, attentive perception. So the lesson presented
an opponent's inference as the book's report. It is the very case AUTHORING
warns about.

**Changed:** the sentence now says the book reports the old test in
Introduction III, that the intellectualist takes it to show the size never
changed, and that Merleau-Ponty replies that the tube makes a different kind of
looking and settles nothing about the moon seen freely.

### 3. Description, Not Explanation: "the point of view" without "consciousness" (fixed)

The paraphrase of p. ix said scientific points of view take for granted "the
point of view through which a world first forms round me". Smith says "the
other point of view, namely that of consciousness". Leaving out "consciousness"
hides the very word that makes the next page's distinction from idealism
necessary, and mistake 3 depends on that distinction. **Changed:** the paraphrase
now reads "the other point of view, that of consciousness".

### 4. Description, Not Explanation: "field of vision … noises and touches" (fixed)

Smith p. xi has "field of perception … a play of colours, noises and fleeting
tactile sensations". A field of vision holds no noises. **Changed:** "field of
perception is full of flickers of colour, noises and passing touches".

### 5. Description, Not Explanation: the reader pressed for time (fixed, minor)

The lesson said this reader "might decide" the philosophy is a myth or a fashion.
Smith says he "will wonder whether" it is. **Changed:** the lesson now says "will
wonder whether".

### 6. The Reduction and Its Limit: a quiz distractor that is defensible (fixed)

Q1, "what does the reduction suspend?", offered "Our belief that the world
exists" as a wrong answer. But p. xv says that we "suspend for a moment our
recognition" of the certainties of common sense, and the world's existence is
one of them. Husserl's epoché likewise *suspends*, without denying, the general
thesis of the world. A careful reader can defend that option under the
question's own verb, and the `why` answered it only by switching to "withdrawn".
**Changed:** the distractor is now "Our belief that the world exists, until doubt
has proved it", which is the Cartesian reading the lesson refutes, and the
`why` says so.

### 7. The Reduction and Its Limit: "the paragraph before / that follows the passage" (fixed, minor)

The sentences on complicity and *ohne mitzumachen*, the passage itself, and the
lines on the impossibility of a complete reduction are all one paragraph in
Smith (pp. xiv–xvi). **Changed:** `read_intro` now says "the rest of its
paragraph", and the body says "The sentences before the passage".

### 8. Intentionality and Rationality: the act of initiative left without its justification (fixed)

The lesson quoted rationality as established "by an act of initiative which has
no guarantee in being" and stopped there. Smith goes straight on: "its
justification resting entirely on the effective power which it confers on us of
taking our own history upon ourselves". Cut off there, the view sounds
arbitrary, which makes the Preface weaker than it is. **Changed:** the clause is
added in paraphrase. No words were added to the quotation.

### 9. Intentionality and Rationality: why the unfinished was inevitable (fixed)

Mistake 3 gave the reason as "given a task like the novelist's or the
painter's". Smith p. xxiv gives the reason as "because phenomenology's task was
to reveal the mystery of the world and of reason". The comparison with Balzac,
Proust, Valéry and Cézanne is a separate sentence about how painstaking the
work is. **Changed:** the stated reason is now the text's, and the comparison is
kept as a comparison.

### 10. Intentionality and Rationality: Marx and the doctrine's explanations (fixed, minor)

The lesson joined two sentences of p. xxi and gave the second one the first one's
reason. Smith says economic and psychological explanations are true "since the
thinker never thinks from any starting-point but the one constituted by what he
is". The condition "provided that they are not isolated … the unique core of
existential meaning" belongs to the earlier sentence, about all the angles on
history. **Changed:** each claim now has its own reason.

### 11. Intentionality and Rationality: summary ambiguity (fixed, minor)

"a rationality that is the agreement of perspectives, guaranteed from nowhere
above them" can be read as asserting a guarantor in a "nowhere". **Changed:**
"guaranteed by no standpoint above them".

### 12. Essences and Existence: "The section ends by saying…" (fixed, minor)

The sentences on sensationalism and transcendental idealism are on p. xvii. The
section runs on to p. xix (the facticity of the world, phenomenological
positivism). **Changed:** "Near its end the section says…".

### Checked and correct

These match the text: the opening question and the "contradictions" (p. vii–viii);
the foreswearing of science; "I cannot shut myself up"; second-order expression;
naïve and dishonest; the geography passage; analytical reflection, including the
concession on Kant (pp. ix–xi); the red book and Peter and Paul (p. xii);
complicity, *ohne mitzumachen*, Fink and wonder, the most important lesson,
absolute mind, perpetual beginner, existential philosophy (pp. xiv–xvi);
*Dasein* to *Wesen*, the Vienna Circle, the fisherman's net, Wahl, the separated
essences, sensationalism, "what I live through", phenomenological positivism
(pp. xvi–xix); Kant's Refutation and the *Critique of Judgement*, act and
operative intentionality (pp. xix–xx); the passage and absolute Spirit, the
impartial spectator, rationality not a problem, relearning to look, the closing
comparison (pp. xxii–xxiv).

The lesson correctly treats the "impartial spectator" (*uninteressierter
Zuschauer*) as the phenomenologist who *establishes* rationality, not as the
view from nowhere under attack. A careless reading of §C L4 could have got this
the wrong way round. The p. 302 old explanation of the horizon moon, the p. 306
Fig. 1 description (two cubes or a mosaic of ten triangles and a square) and
p. 77 for the house seen from nowhere are all accurate.

## Opponents, sources and historians

All checked and accurate, and stated at strength:

- Husserl trained as a mathematician, and "to the things themselves" is his.
- Fink became Husserl's assistant in 1928. His 1933 Kant-Studien defence carries
  Husserl's foreword endorsing it, and it is the essay cited in footnote 6.
- Descartes's *Meditations* (1641). Husserl introduced the epoché by way of
  Cartesian doubt while distinguishing the two.
- Kant's "I think" and the Refutation of Idealism.
- Brentano, 1874, as Husserl's teacher.
- The Vienna Circle, with Schlick, Carnap and Neurath, and its verification
  criterion.
- Jean Wahl on Kierkegaard and on Hegel's unhappy consciousness, and *Vers le
  concret*.
- Ehrenfels (1890) and transposition. The Gestalt psychologists' debt to him.
- Marx on history standing on its feet.

Recommendation, not changed: the Vienna Circle paragraph's steelman is built on
the Preface's own characterisation (a concept's semantic history), which is
idiosyncratic. The Circle's own objection to "consciousness" talk would have
been verificationist. One clause saying the description is the Preface's, not
the Circle's self-description, would be fairer. The lesson already says "The
Preface puts their view this way", so this is taste.

No clinical cases appear in this course.

## Quotations

The checker reports no misses and every lesson is under both caps (largest: 139
of 150; openings at most 68 of 70). By eye, every quoted span is in the voice
the lesson gives it:

- "Husserl separates essences from existence" is attributed to Wahl.
- *ohne mitzumachen* and "a perpetual beginner" are attributed to Husserl, the
  second through the unpublished works.
- "impartial spectator" is the Husserl/Fink term.
- "it does not think with its feet" is Merleau-Ponty's addition to Marx.
- The Preface's first-person sentences ("I am the absolute source", "I cannot
  shut myself up…") are his own voice. Mistake 3 handles them correctly.

None of the quotations depends on a matching convention alone.

## Arithmetic and models

I recomputed every figure, and each matches the `--observe` output for every preset.

- 3474/384400 = 1737/192200 = 0.009037 rad = 0.518°.
- 384400 − 6371 = 378029, and 3474/378029 is already in lowest terms
  (3474 = 2·3²·193; 378029 is divisible by neither 3 nor 193). It is
  0.009190 rad = 0.527°.
- 7/770 = 1/110 = 0.009091 rad = 0.521°. That covers 0.009037 and falls short
  of 0.009190.
- The quiz coin: 9/990 = 1/110, and 9/99 = 1/11.
- "By about two per cent": the true figure is 1.7%. That is acceptable.
- The cube: 12 edges in a wire drawing, 9 in a solid one. The reflection across
  the plane perpendicular to the line of sight leaves a parallel projection
  unchanged, so the wire drawing fits 2 readings.
- The variation sets, with their cores and lacks: tones vary in pitch, loudness
  and timbre, and the core is `some-duration`. Tables vary in material, height
  and legs, and the core is `top`. C E G, D F♯ A and B♭ D F share no note with
  C E G, and each rises a major third then a minor third. G E C falls a minor
  third then a major third.
- Faces: 1 2 2 has length 3 and sees right 1/3, above 2/3, front 2/3. −2 1 −2
  sees left 2/3, above 1/3, back 2/3. The union is 5 of 6. The 1 2 2 + front
  quiz gives 3 of 6.

**Model attribution (fixed).** Lesson 4 said a viewer "sees the front at 2/3 of
its true size", along with "the top seen at 2/3 and at 1/3", "at what fraction
of its true size does the top appear?" and the same in a step and in the
worked example. The fraction is the parallel projection's area factor. It is
not what a perceiver sees, and Merleau-Ponty's account of constancy later in
the book denies precisely that a face is seen at its projected size. Each place
now attributes the figure to "the lab's projection", which "draws" the face at
that fraction "of its true area". The changes are in the body paragraph, the
step, the worked intro and after, quiz Q2 and its `why`, and mistake 1. The
tile strings are unchanged.

Lesson 1 already attributes the moon's figures to the angle ("by the angle the
overhead moon is the larger") and to geometric optics. Lessons 2 and 3 attribute
theirs to the projection and to the lesson's coding.

## Quiz

I argued for every distractor in all sixteen questions. The only one that held
up is lesson 2 Q1's "Our belief that the world exists", now fixed (finding 6).
Two others are on the edge but hold:

- L3 Q3 "a word's meaning, to be handled with care": the Preface attributes to
  the Vienna Circle the view that we relate only to meanings, and p. xvii
  contrasts the essence with the *Wortbedeutung*. It is defensible as wrong.
- L4 Q3 "the application of the understanding's categories": this is act-side
  on the Preface's account of the first *Critique*. It is defensible as wrong.

## Voice (§F)

Two of the four lessons open (after the passage) with an everyday scene: the
moon over the roofs, and the cereal box. That is within the ration. There is no
modern aside, which is correct, because Course 1 has none permitted. There is
one light remark, the Marx joke "borrowed and then improved", and it points at
the author's own wit, as §F prefers. The voice is warm and unperformed
throughout. Each last `p` points on by title.

Recommendations, not changed:

- L4 "Nobody sees the bottom, and nobody needs to, to see a cube" is the lesson
  speaking for perception. "and, on the Preface's account, nobody needs to"
  would keep it presented rather than endorsed.
- L3 "The net is not the catch. You throw it to bring up what is alive" is a
  gloss in the lesson's own voice. It is faithful to p. xvii and fine, but it
  sits on the edge of the lesson praising the side it presents.
- L4: the `three` preset's cover tile shows that the two oblique views alone
  see all five faces, so the straight-front viewer adds nothing to the union.
  The lesson never says so, and a reader who reads `peCover` may wonder why the
  third viewer is there. It could say one sentence on it: it is there to show
  the front confirmed twice.

## Where I disagree with the pedagogy assessment

`docs/pedagogy/phenomenology-perception-what-phenomenology-is.md` did not exist
when these findings were finished, so this section is skipped.
