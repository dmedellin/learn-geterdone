# Second review: Sensing and Space (`perception-sensing-and-space`, `c5_sensing_space`)

An independent read, done to `docs/phenomenology/SECOND-REVIEW.md` and to the
"Lessons from" sections of `docs/phenomenology/AUTHORING.md`. I checked every
lesson against Smith, pp. 235–347, page by page. I also checked p. 308 (the
cube's faces seen as squares askew) and p. 372 (the glass's single manner of
being). I recomputed every figure. I wrote these findings before reading the
pedagogy assessment.

**Concurrent edits.** Another agent, most likely the pedagogy reviewer, was
editing `part_a.py` and `part_b.py` while I was reading them. Between my read
and my first edit, `git diff` shows that agent changed these places:

- the objector's paragraph in lesson 1, and its quiz `why`;
- the `faint` label ("too faint to be seen");
- the Stratton paragraph in lesson 5;
- Berkeley's "own book" in lesson 6;
- the stereoscope in a lesson 6 `why`;
- the opening of the Binswanger paragraph in lesson 8.

Two of those overlap findings of mine (1.1 and 8.1 below). I made every edit of
my own as an exact-string replacement against a fresh read of the file. I also
messaged that agent the places I changed.

**Final checks after my edits:**

- `preview_subject.py … --course perception-sensing-and-space`: `OK`. Labcheck
  ran 8 pages with pinned figures, 0 failing.
- `phen_quotes.py c5_sensing_space`: `OK`. No misses, and every lesson is under
  the caps. The largest are Movement (116 words, opening 62) and Up and Down
  (113 words, opening 65).

## Overall

The course is accurate and careful. The arithmetic is all right, and every
figure is attributed to the model that computes it. The psychological sources
are named correctly and dated correctly where a date is given:

- Goldstein and Rosenthal;
- Werner, in Hamburg;
- von Senden, 1932;
- Stratton's two experiments;
- Wertheimer, 1912, for both the mirror and the stroboscopic experiments;
- Korte, 1915;
- Linke;
- Koffka and Guillaume;
- Minkowski, *Le Temps vécu*, 1933;
- Binswanger;
- Fischer;
- Straus.

In each case the voice is right where it matters most:

- the six-equal-sided cube is the objector's;
- the associationist reading of Stratton is "at least implicitly Stratton's
  own";
- the triangle of convergence is the traditional view's;
- the watch, the fakir and the circle are the logician's (Linke's);
- the respiratory reduction of the dream is objective thought's.

The errors I found are small. Most are a source's report placed in the wrong
mouth, or a paraphrase that says a little more than the page.

## Findings by lesson

### 1. The Theory of the Body Is Already a Theory of Perception

1.1 **Where the objector's voice begins.** The body said "the next paragraph is
in the objector's voice". The quiz `why` said "The paragraph begins &ldquo;It
will perhaps be objected&rdquo;". In Smith (pp. 235–236) the objection starts
in the middle of the first paragraph and fills the rest of it, and the reply is
the next paragraph. The concurrent editor fixed both before I reached them, and
I checked their wording against the page. No further change.

1.2 **Stratton was his own subject.** "Stratton's subject" is Smith's phrase,
p. 239, and the lesson is right to keep it. Lesson 5 names Stratton as the
wearer. *Recommend*: when lesson 1 first mentions him, add half a sentence
saying that Stratton wore the spectacles himself.

1.3 **The objection called intellectualism.** "At its strength this is the view
the Introduction called intellectualism" is the lesson's identification, not
the text's. It is defensible, since the objection constructs the cube by
conceiving the body as a mobile object. *Recommend*: "a view close to what the
Introduction called intellectualism".

1.4 **Figures checked.**

- 3 0 4 has length 5 and gives front 4/5, right 3/5.
- 1 2 2 has length 3 and gives right 1/3, above 2/3, front 2/3.
- In `tour`, the front goes 1, 4/5, 3/5, then nothing, and the right side goes
  nothing, 3/5, 4/5, 1. The four views present 2 of 6 faces, and the cover is
  "a little round (1 view)".
- Every figure is the projection's, and the lesson says so.
- The forward reference to Depth, with the side faces seen as squares seen
  askew, is supported by p. 308.

### 2. The Motor Physiognomy of Colours

2.1 **Smith's misprint, understated.** The lesson said page 243 prints
*abduction* twice, the second time where *adduction* is meant. Smith in fact
makes the slip twice:

- "blue and green abduction";
- in the next sentence, "of abduction that it turns away".

**Changed**: the sentence now says the page makes the same slip in the next
sentence, and that the lesson quotes neither.

2.2 **The tile string.** The body said the predicted-difference tile prints
`0 − 0 = 0` cm. The tile prints `0 cm`, which I confirmed with `--observe`.
**Changed** to "prints `0` cm, since `0 − 0 = 0`".

2.3 **"The lab below codes the reports."** The sentence fits a `cases` lab, but
this lab is `stimulus/illusion`, which codes nothing. It puts illustrative
centimetres on directional reports. **Changed** to "the lab's centimetres
below are illustrative, not the patients' measurements".

2.4 **A verdict in the lesson's own voice.** "The strongest evidence is a test
anyone's account must meet" ranks the evidence where the chapter does not
(§F: do not praise one side). **Changed** to "The next evidence comes from
another psychologist." *Recommend* also softening "The faint preset makes the
point sharpest" later in the lesson.

2.5 **Checked and right.** Each of these matches the page:

- Goldstein and Rosenthal's findings, p. 242: the raised arm, red applied to
  the right eye, the privileged position, green bringing it nearer, and
  overshooting under red.
- The contrast blue, p. 243.
- "red may accentuate my reactions …", p. 244.
- Kandinsky and Goethe, quoted through Goldstein and Rosenthal.
- Werner's two subjects, pp. 244–245. Their words are quoted as theirs.
- The sleeper and the sacrament, pp. 245–246.

The arithmetic is 4 + 2 = 6, with a gap of 6 − 0 = 6. Each quiz distractor is
answered correctly. Werner as "a developmental psychologist then working in
Hamburg" is right for the *Untersuchungen* (1930).

### 3. The Anonymous Subject of Sensing

3.1 **Werner's spasm.** The lesson gave the spasm as "one of Werner's
subjects". On p. 248 it is Werner's general statement, quoted ("If a subject
tries to experience a specific colour …"), not a report of one subject.
**Changed** to "Werner reports that a subject who tries to see blue while
holding the bodily attitude of red feels a kind of spasm …".

3.2 **Coding of observation 2.** Observation 2 codes intellectualism `y` on
"the sensible beckons until taken up". The same paragraph on p. 248 denies
"that one confers significance on the other". The `note` already flags this
cell. I agree with flagging it rather than recoding it, because §C fixes the
coding.

3.3 **Checked and right.** These match the text, pp. 246–252:

- the intellectualist account, pp. 246–247;
- "a purely verbal solution";
- the sky and the retort;
- Hegel's hole in being;
- the mathematician;
- birth and death;
- "another self which has already sided with the world";
- incompleteness;
- the definition of a sense.

Every tile matches its pin, and the subset presets are explained in prose.

### 4. The Unity of the Senses

4.1 **Circle and rectangle.** The lesson said a von Senden patient tells "a
circle from a square". Smith, p. 259, says "a circle from a rectangle".
**Changed**.

4.2 **The mescalin report.** "Beneath it Werner found a primary layer … and
under mescalin a flute's sound gives a bluish-green colour" read as if the
mescalin report were Werner's. On p. 265 it is footnoted to Stein. **Changed**
to "in the mescalin reports of the chapter's other sources …".

4.3 **The paragraph before.** The lesson said "the paragraph before it says" of
gold and wood. Those are the sentences just before the passage, in the same
paragraph (p. 266). **Changed**.

4.4 **Naming the view rejected.** The sonata and Helen Keller, and Venus as the
common ground of the Morning and Evening Star, are views the chapter reports
from Specht and from Alain (pp. 267–268). *Recommend* naming Alain, the French
philosopher, when the lesson first mentions the view it rejects.

4.5 **Checked and right.** Each of these matches the page:

- von Senden, 1932, as a collection of reports;
- the patient blind for eighteen years who reaches for the sunlight, p. 261;
- "touching is not seeing", p. 260;
- the reduction screen, after Gelb and Katz, pp. 262–263;
- binocular vision, pp. 268–271;
- Herder, p. 273;
- the dubbed film;
- *warm* and *hard*.

The intersection figures are right, and the quiz core is `hard`.

### 5. Up and Down

5.1 **The French word *sens*.** The lesson said "the French word *sens*, the
translator notes, means both sense and direction". It is Merleau-Ponty who
points to the double use of *sens*, on p. 294; the translator's note only
glosses it. **Changed** to "the chapter points out".

5.2 **Tile name.** The body called a tile "perceived-tilt", but the kit labels
it "Predicted tilt (image − level)". By the Course 1 lesson, a lab figure is
what the model predicts. **Changed** to "predicted-tilt" in that sentence.

The key line and the model statement keep "perceived tilt = image tilt −
level". It is flagged throughout as the lesson's model, as PLAN §0 does, so I
left it.

5.3 **Dates for Stratton.** Stratton's experiments now carry their dates:

- the short first trial, 1896 ("Some preliminary experiments", which Smith
  cites at p. 617);
- the week-long second, 1897 ("Vision without inversion of the retinal image",
  Smith p. 350).

**Changed**, in the voice of history.

5.4 **Checked and right.**

- Every Stratton report against p. 285: day two, days three to seven, actions
  from day five, sounds placed correctly only when seen, and the queer world
  when the spectacles came off.
- Footnote 4, the interpretation that is "at least implicitly" Stratton's.
- Wertheimer's mirror, p. 289, from the 1912 *Experimentelle Studien*.
- Anchoring points.
- Nagel's stick, cited through Wertheimer.
- "wherever there is something to be done", p. 291.
- Systematic yet piecemeal, and the tune sung in another key, p. 292.
- The inverted face, p. 294.
- The first level and its nausea, p. 296.

The concurrent editor's rewrite of the Stratton paragraph is supported by
p. 285. The figures are right:

- the mirror: 45°, 45°, 0°, 0°, 0°;
- Stratton: 180°, 90°, 45°, 45/2°, 45/4°.

### 6. Depth

6.1 **Berkeley's second form.** The second form of Berkeley's argument is the
chapter's conjecture: "Berkeley would probably reply", p. 297. The lesson had
dropped the hedge and presented it as Berkeley's. **Changed** to "Berkeley
would probably reply, the chapter supposes, …".

6.2 **Whose observation.** "The chapter's first objection is that nobody has
them. I am not expressly aware of my eyes' convergence …" The observation is
the Gestalt psychologists' (p. 300, Koffka and Guillaume), and the chapter
reports and adopts it. **Changed** to say it is an observation the chapter
takes from them. The next paragraph's "had already seen" still reads
correctly.

6.3 **Checked and right.**

- "For God …", p. 298.
- The triangle, given in the traditional view's voice with Malebranche in the
  footnote, p. 299.
- The blind man's two sticks, which the chapter footnotes to Malebranche and
  which go back to Descartes's *Dioptrique* (1637) as history. The lesson says
  this.
- The natural geometry, as Platonic myth, p. 300.
- Motives, pp. 301–302.
- The ash-tray, the road and "anterior to equality and inequality", pp.
  303–304.
- "disparity only for a subject …", p. 305.
- The pen pushing through whiteness and the level of distances, p. 310.

The figures are right:

- 6.5/50 = 13/100, and 6.5/60 = 13/120;
- disparity 13/600;
- `far` 13/6000, a tenth;
- `interval` 13/51000, which is 1/85 of `near`;
- the quiz figures 1/10 and 13/200.

The note's claim that the exact angles differ "in the fourth decimal place" is
true:

| | small-angle form (rad) | exact (rad) |
| --- | ---: | ---: |
| convergence at 50 cm | 0.1300 | 0.1298 |
| convergence at 60 cm | 0.1083 | 0.1082 |
| disparity | 0.0217 | 0.0216 |

### 7. Movement

7.1 **Linke.** The lesson made Paul Linke "a German philosopher of Husserl's
school". That overstates a school membership. Linke trained under Wundt; he
was close to phenomenology and published on phenomenology and experiment in
the perception of movement. **Changed** to "a German philosopher close to
Husserl's phenomenology who wrote on phenomenology and experiment in the
perception of movement".

7.2 **The name *phi*.** The definition said "Wertheimer called the pure case …
the phi phenomenon". Wertheimer's φ names the impression of movement, and the
objectless case is *pure* φ. The definition also gave the reader no way to
find the term in Smith. Smith prints it "phenomenon ø", in the logician's
voice, on p. 316. **Changed**: phi, pure phi, and where Smith prints it.

7.3 **Checked and right.**

- Each paraphrase matches pp. 311–326: the stone, Zeno (p. 313), the passage
  (pp. 313–314), the rod C, the workmen and the pencil.
- The watch and the fakir as Linke's (footnotes 38–40).
- The psychologist's "passing effect" as Wertheimer's (p. 316).
- Both sides vindicated, p. 317.
- "identical in them", p. 318.
- The style, and the greyish power of flight.
- Bergson in note 47.
- Leibniz's ship and Koffka's train, p. 326.
- "a phenomenon of levels", and motion as absolute once anchored.

The textbook thresholds and Korte's laws (1915) are labelled as later than the
book. The figures are right: 5/20 = 1/4, 5/60 = 1/12 and 5/250 = 1/50, and the
quiz's 6/120 = 1/20.

### 8. Lived Space

8.1 **The order of the reply.** The lesson said "The chapter's reply begins
with a patient of Binswanger's." In Smith the reply begins on p. 337, with the
argument against analytical reflection and its either/or. The brush comes only
on p. 339, after the myth. The concurrent editor had already changed the
opening to "runs from page 337 to page 339, and its sharpest case, near its
end, is …", which removes the false claim.

*Recommend*: put the paragraph in the text's order (analytical reflection and
the either/or first, then the brush), and drop "sharpest", which is a verdict.

8.2 **Who takes food with his hand.** The person who still takes food with his
hand (p. 329) is the subject under mescalin, not a schizophrenic patient.
**Changed** to "the subject under mescalin".

8.3 **Natural space gloss.** The concept gloss "geometrical space is objective
thought's explicit version of it" says a little more than pp. 342–343. Those
pages say only that natural space is not geometrical space and that objective
thought draws on the unreflective. *Recommend*: "and is not geometrical space,
which objective thought makes explicit from it".

8.4 **Checked and right.**

- Mescalin, cited to Mayer-Gross and Stein.
- Fischer's bird and twittering, and his mountain patient, p. 334 (footnote 71),
  and the landscape space after Straus.
- Minkowski as the source of the night, p. 330 (footnote 60).
- *Le Temps vécu*, 1933.
- Lived distance as Minkowski's term, p. 333.
- Binswanger's "direction of significance", p. 332, from *Traum und Existenz*.
- The brush, p. 339, from *Das Raumproblem*.
- The objection in objective thought's voice, pp. 335–336.
- "understanding myth …", p. 341.
- The Tuileries stone and both closing quotations, p. 342.
- Illusion: the stone on the path and the fly, pp. 344–345.

The cases mode's record, survivors and split were recomputed for every preset.
The quiz split is B, C.

## Course files

- **`__init__.py` docstring.** It said part_a reads the introduction and
  Chapter 1 "in three lessons", but part_a holds four. **Changed**.
- **Part Two's title.** The `summary` gives "The World as Perceived". That is
  Smith's title for Part Two (p. 233), where PLAN §B's prose says "The
  Perceived World". The course follows the edition, as §E.2 requires, so I
  left it.
- **No modern aside**, as §F requires for this course.
- **Opening scenes.** Lessons 1, 3, 4 and 7 open with a scene. Lesson 7's
  stone is the chapter's own, so the scenes stay within half.
- **Last `p`.** Every lesson's last `p` points on, and the last points to the
  next course.

## Quiz

I argued for every distractor. None is defensible as right. There is one near
miss: in lesson 2, Werner's subjects do infer the colour, from the bodily
attitude ("I clenched my teeth, and so I know"). The distractor's "from a
faint sensation of it" is what makes it wrong. The distinction is fine but
holds, so I left it.

## Quotations

- The checker reports `OK`: no misses, and no lesson over the 70- or 150-word
  caps.
- **Convention-only items.** Lesson 7's "Zeno’s arguments" keeps Smith's curly
  apostrophe, which the checker accepts. Lesson 4's opening splits across
  pp. 266–267 with an ellipsis-free break, marked "and, over the page".
- **Voice of each quotation.** I checked the speaker of every quotation by eye:
  - the objector's sentence appears only in a quiz `why`, framed as his;
  - "The distance is the height of a triangle …" is framed as the traditional
    view's;
  - "the landscape space" is attributed to Straus;
  - Werner's subject is quoted as the subject;
  - the rest are Merleau-Ponty's own.

## Where I disagree with the pedagogy assessment

`docs/pedagogy/phenomenology-perception-sensing-and-space.md` did not exist when this review was finished (checked 2026-10-24, after the findings above were written), so there is nothing yet to compare. The pedagogy reviewer was evidently at work on the course files at the same time (see the note on concurrent edits); its fixes to lesson 1's objector paragraph and lesson 8's Binswanger paragraph agree with findings 1.1 and 8.1 here, and its Stratton rewrite in lesson 5 is supported by p. 285. Where I part from its lesson 8 wording, "its sharpest case" is a verdict the text does not give (8.1).
