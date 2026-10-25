# Phenomenology spec: pedagogical-expert review (pre-authoring)

Reviewed: `docs/phenomenology/PLAN.md` (branch `feat/phenomenology-subject`),
read against `docs/capital/PLAN.md` §0, §B, §E, §F, §R, `docs/capital/AUTHORING.md`,
`AGENTS.md` §0, §1a, §8, `content/AGENTS.md`, `docs/FUTURE-SUBJECTS.md`,
`docs/philosophy/PLAN.md` §D.0 and §E, and the enforced ranges in
`tests/test_site_invariants.py` (slug ≤ 48, key line ≤ 46, check id ≤ 72,
`TestAPathCountsItsOwnCourses`).

Findings are numbered; each is marked BLOCKING or not and carries a fix.
Blocking means: authoring or kit build should not start until the spec is
changed. Everything else can be fixed in the same pass or during authoring.

Summary: 31 findings, 9 blocking (1, 2, 5, 9, 15, 17, 18, 19, 23).

---

## A. §0 — is "what the reader computes" honest?

**1. BLOCKING — `cases` as used is a scoreboard on which the chapter's own account always wins, and that is both decorative and an endorsement.**
§0 promises that "the lab computes the prediction of the theories he argues against"
and that the chapter's claim is read in the gap. But in 10 of the 12 `cases`
lessons the third account is Merleau-Ponty's own (the phenomenal field,
being-in-the-world, motor intentionality, the existential account, meaning as
gesture, the pseudo-world, coexistence, the tacit cogito, freedom in situation),
coded by the author, and the Worked line already announces the result
("motor intentionality absorbs both", "the existential account absorbs both on
the chapter's coding", "neither absorbs all four"). A reader can see from the
y/n table that the column with no `n` survives; `caRecord` counts what the
author typed. That is the FUTURE-SUBJECTS definition of decorative, and it
breaks §F's "presented, not endorsed" structurally: every such lab is a
tally in which the book's view has a clean sheet because the lesson coded it so.
*Fix:* make the rule match §0. A `cases` table carries the **opponents'**
accounts only (two, occasionally three), and the chapter's own account is in
prose. The computable, non-obvious result is then `caSplit` (which observation
separates the two opponents) and `caSurvivors` printing `none` (both opponents
fail somewhere) — which is exactly the book's move: find the observation
neither classical account absorbs. Allow the chapter's account as a column only
where the chapter itself scores it against the others and says an opponent has
a truth it cannot absorb (`the-truth-of-solipsism`, where the grief case is
absorbed by both; `the-phantom-limb`, where the two explanations are the
chapter's explicit targets). Rewrite the Do and Worked lines of 2.5, 3.7, 4.2,
4.4, 5.2, 5.7, 6.5, 7.3, 7.7 accordingly ("name the observation on which both
classical accounts fail").

**2. BLOCKING — §0's table over-claims for about a third of the modes; name the third family honestly.**
`stimulus`, `size`, `depth`, `light`, `motion/phi`, `perspective` and
`argkit/validity` compute what a named model predicts. `cases`, `variation`,
`cues` count the lesson's own coding. `schema`, `level`, `time`, `triangle`
compute a toy model the *lesson* invents (no theory predicts "perceived tilt =
image − level"; no theory of the body says reach = arm + cane). The material
clause covers the first two families ("a stated model … or a count over the
cases"); the third is honest only if each lesson's `panel_intro` says "the
lesson's own model". *Fix:* add a third paragraph to §0 naming the three
families and the rule for the third: the `panel_intro` says the model is the
lesson's illustration, the `note` says what it leaves out, and the label
never attributes it to the book or an opponent. Add a line to §D.3: "Never
print a lesson's own toy model under an opponent's name."

**3. Not blocking — labs that restate the narrative (lesson by lesson).**
Checked all 41. These are the ones whose lab adds nothing the reader could not
see without it, with a proposal for each:
- **1.2 the-reduction-and-its-limit** (`perspective/necker`): `peReadings` is a
  lookup by object type (`cube`/`box` → 2, `solid` → 1), not a computation.
  *Proposal:* compute it. Project the eight vertices under both depth
  assignments and compare the two 2-D edge sets (`peSame`); for `solid`, do
  hidden-face removal by the sign of normal · view (rational for axis and
  Pythagorean directions) and show that the two assignments now draw different
  edge sets, so one reading. Then the tile is earned.
- **3.1 experience-and-objective-thought** duplicates 1.4's computation
  (union of faces over views). *Proposal:* add a tile `peCover` — the smallest
  subset of the given views whose union is every face — so the lesson computes
  "the house is the system of views" as a minimum cover (two opposite corner
  views suffice for a box; no single view does). Pin `peCover` and `peMax`.
- **5.6 movement, view `positions`**: the spec itself says the tile is "a
  fixed string printed under every input". A fixed string is not a
  computation. *Proposal:* drop the `positions` view; Zeno's arrow goes in
  prose; keep `phi`, which computes a real band test. (Also saves page weight.)
- **7.2 the-triangle**: `trC = 180 − a − b` and `trStraight = a + c + b = 180`
  are tautologies of each other; the SVG is the lesson. *Proposal:* add a
  redraw-only select `trVertex` (which vertex the parallel passes through) so
  the reader sees three different constructions give the same straight angle,
  and the tiles `trAlternate` change while `trC` does not. Modest, but it is
  what the chapter says the geometer does.
- **7.4 time-is-not-in-things**: counting moments before and after an index,
  with `none` printing empty tiles, is a classification whose outcome is fixed
  by the preset. *Proposal:* merge into 7.5 (`time/diagram` subsumes the line
  as its horizontal, and `present: none` can be a preset there), or accept this
  as the Subject's weakest lab and say so in its `note`. Merging gives Course 7
  six lessons and removes a part_b split; Subject becomes 40 lessons (update
  tagline, description, §B).
- **5.3 the-unity-of-the-senses** duplicates 6.3 (`variation` over the senses,
  properties common to presentations). *Proposal:* 5.3 uses `stimulus/illusion`
  on the chapter's intersensory cases (a sound changes a seen colour; the
  constancy hypothesis predicts a difference of 0; reported difference
  non-zero), which is exactly the §0 pattern, and leaves `variation` to 6.3.
- **5.2 the-motor-physiognomy-of-colours** (`cases`, two accounts, no
  instances): Goldstein and Rosenthal's observations are magnitudes (the
  arm's deviation under red and blue). *Proposal:* `stimulus/illusion` with
  `a`, `b` the two colour conditions, predicted motor difference 0 under
  "sensation as quality", reported the deviation (illustrative figures, labelled).
  No `cases` here.
- **6.5 hallucination** (`cases`, author codes): the chapter's content is what
  the hallucination *lacks* (horizons, confirmability, insistence). That is
  the `variation/core` computation already built for 1.3: variants "a
  perceived lamp" and "a hallucinated lamp" with properties; `vaBreak` prints
  what the hallucination lacks from the core. *Proposal:* use it; the lab then
  computes the chapter's own list.
- **4.4 the-spoken-word-and-thought** (`cases`, undesigned): the chapter's
  case is anger expressed differently in Japan and the West. *Proposal:*
  `variation/core` over expressions of one emotion across cultures: no bodily
  sign is in the core (`vaCore: none`); what is common is the situation, which
  is in prose. Same computation as 6.3's empty core, so it also prepares 6.3.
- **Where none exists:** 3.2 (phantom limb), 4.2 (sexed being), 5.7 (lived
  space), 6.7 (solipsism), 7.3 (tacit cogito), 7.7 (freedom). These chapters
  have no quantity in them. Keep `cases` under the rule in finding 1, with the
  observations listed in §C (finding 9).

---

## B. The `cases` mode

**4. Not blocking — `cases` is overused: 12 of 41 lessons (29%), two of them on the same observation table.**
With findings 1 and 3 adopted it falls to 7 (2.5, 3.2, 3.7, 4.2, 5.7, 6.7,
7.3, 7.7 minus one of 3.6/3.7 — see 5), which is tolerable for a book argued
from cases. Add a sentence to §0: "`cases` is used only where the chapter has
no quantity and sets at least two accounts against at least three
observations; every other lesson computes a prediction."

**5. BLOCKING — 3.6 and 3.7 run `cases` over the same Schneider tasks twice.**
3.6's "accounts" (concrete movement, abstract movement) are not accounts but
the observation itself (done / not done), so `caRecord` counts the data; 3.7
then recodes the same tasks under three theories. *Fix:* give 3.6 a
computation of its own. The chapter's distinction is between a target given in
the body's situation (the mosquito on the skin, the handkerchief in the hand)
and a target given objectively on command ("point to your nose"). Extend
`schema/coordinates` with a per-object field `given: body | room`: the tile
`scFrame` prints, per task, whether reaching it needs a conversion from room
to body coordinates, and the Pythagorean rotation of the body makes the
conversion visible as in 3.5. 3.7 keeps the three-account `cases` (opponents
only per finding 1: empiricism and intellectualism; motor intentionality in
prose, `caSurvivors: none`).

**6. Not blocking — `cases` presets that change the account set break the §D.0 convention.**
2.5 `two` (drops the third account) and `one`, 3.2 `physiology`/`memory`
change the *accounts*, but `caPair` is a redraw-only select whose options are
built from cfg and "a preset menu's change handler never touches a redraw-only
select". A pair naming an account the preset lacks is undefined. *Fix:*
`accounts` is a cfg key, fixed per lesson; presets vary only `observations`.
Rewrite 2.5's presets as observation subsets (`intro`, `illusion-only`,
`attention-only`) and 3.2's likewise.

---

## C. Cognitive load, sequencing, thin lessons

**7. Not blocking — four lessons on the Preface is the hardest possible opening for a Beginner course.**
The Preface was written last, is the most Husserlian twenty pages of the book,
and none of its four labs comes from its text (the moon, the Necker cube, a
tone's variations, a cube's faces are all illustrations). Most teachers read
the Introduction first. *Fix:* either (a) three lessons — merge
`essences-and-existence` into `the-reduction-and-its-limit` (the Preface
treats them as one movement) — or (b) keep four and say in Course 1's
`how_to` and `why_order` that the Preface was written after the book and may
be read after it, and that Course 2 does not depend on Course 1's labs. I
recommend (b) plus the honesty in (a)'s spirit: Course 1's `summary` should say
its labs are illustrations of the method, not of the Preface's cases.

**8. Not blocking — the moon is used twice (1.1 `horizon`/`zenith` and 2.4 `moon`) and "a person at two distances" twice (2.4 `person`, 6.1 `near`/`far`).**
Repetition across courses is fine when it is announced; here each lesson
treats the figure as new. *Fix:* 2.4 drops `moon` (keep `person` and
`afterimage`); 6.1 says in prose that 2.4 computed the angle and this lesson
computes the constancy ratio from it.

**9. BLOCKING — seven `cases` lessons have neither observations nor a worked example, and a `cases` table cannot be reviewed until its observations exist.**
`docs/capital/PLAN.md` §R let bare preset ids stand as placeholders, and this
spec inherits that; but for `cases` the *observations are the lesson's
content* — "a reviewer checks each cell against the text" (§0), which is
impossible when no cell is named. Entries with `Worked: author's figures` and
no observation list: 4.4, 5.2, 5.7, 6.5, 7.3, 7.7; 4.2 names presets but no
observations. *Fix (before authoring):* for each one that stays `cases` after
findings 1 and 3 (4.2, 5.7, 7.3, 7.7), list in §C at least three observations
from the chapter by section and the two opponent accounts, and write the
Worked line as "both fail; the split is X". For 2.5, 3.2, 3.7, 6.7 the
observations are listed already — keep that standard. Preset ids may stay
bare under the Capital rule; observations may not.

**10. Not blocking — thin non-`cases` entries that need an instance before authoring.**
- 5.3 `variation` "presets as the author designs" (replaced by finding 3).
- 6.4 `cues/sequence` "presets from the chapter's example" — the example is not
  named. *Fix:* name the passage in the Read line (Part Two, Chapter 3, §C,
  the illusion corrected by a closer look) and give the three candidate
  interpretations and the three cues in §C.
- 5.4 `level` preset `none` is undefined (image 0? level 0? share 0?). *Fix:*
  `none` = image 0, level 0: perceived 0 at every period.
- 3.4 `perspective/own`: "viewpoints restricted to where the eyes are" would
  see no face of one's own head at all. *Fix:* state the object (the whole
  body as a box), the restricted list (front, below, left, right — not back,
  not above) and that the mirror adds `front` reversed, so `peUnseen` = back,
  above. Or drop `mirror`.

**11. Not blocking — one hard idea per lesson: three entries carry two.**
- 2.2 carries the constancy hypothesis *and* Weber's fraction (two views, two
  misconceptions' worth). Weber is justified by §G but costs a Beginner lesson
  its focus. *Fix:* keep `weber` as one preset in prose and the `note`, pin
  only the `illusion` tiles; or move Weber to 5.2 (which, per finding 3, uses
  `stimulus`).
- 6.1 carries size constancy (lab) and shape constancy (a second computation
  "in prose", with its own Worked line). *Fix:* the Worked line must be the
  lab's (Brunswik), not the prose's ellipse; or make `perspective/shape` a
  second preset family and pin both — but then the title's two ideas are two
  labs, which the format forbids. Recommend the first.
- 4.3 states two disputes in the misconception (the naive "labels" view, then
  Gelb–Goldstein against Merleau-Ponty). See finding 13.

**12. Not blocking — course boundaries are right; the split sizes are uneven at the end.**
Courses 3–7 at 7/4/7/7/7 are fine. Course 4 (four lessons for Chapters 4–6,
of which Chapter 6 on speech is the most cited chapter in the book) is thin
against Course 6's five lessons for Chapter 3. *Fix:* no change required; if
finding 3's merge of 7.4 into 7.5 is taken, consider giving Chapter 6 a third
lesson on the "speaking word" and the acquisition of language (the child, the
first word), with `cues/pattern` as its lab (the word's meaning fixed by the
sentence), to keep 41.

---

## D. Misconceptions

**13. Not blocking — verdicts and straw men.** Most of the 41 are misreadings
stated fairly. These need work:
- **3.7** "Motor intentionality is a reflex dressed in new words" — no holder,
  stated as a sneer. *Fix:* name the holder (the mechanistic physiology the
  chapter cites, or a behaviourist) and state it at strength: "every
  directed movement is a chain of reflexes triggered by stimuli; 'directedness'
  is the observer's description of the chain."
- **1.4** "Rationality is a viewpoint above all viewpoints" — a slogan. *Fix:*
  name it as the *pensée de survol* the book attacks and give it a holder
  (the Kantian or absolute-idealist "spectator"), at strength.
- **4.2 Worked** "the existential account absorbs both on the chapter's coding"
  and **3.7 Worked** "motor intentionality absorbs both" are verdicts the lab
  manufactures (finding 1). *Fix:* per finding 1.
- **4.3** the misconception is the naive view, but the refutation then
  switches to the Gelb–Goldstein vs Merleau-Ponty dispute, which is not what
  `mistakes[0]` names. *Fix:* make `mistakes[0]` Gelb and Goldstein's reading
  stated at strength ("the patient has lost the categorial attitude; words
  are intact"), which the chapter takes up and answers; the naive view can be
  `mistakes[1]`.
- **5.5** "We see depth by calculating from convergence" — needs its holders
  (Descartes' *Dioptrics*, Berkeley's *New Theory of Vision*) named, as §C's
  own rule requires.
- **6.4** "Because any perception may turn out an illusion, all of them
  might" — name the holder (the Cartesian sceptic of the First Meditation).
- **1.1** "Phenomenology rejects science. Refuted with the lab" — the lab
  cannot refute a claim about phenomenology; the Preface's sentence does.
  *Fix:* "refuted by the Preface's geography comparison; the lab keeps the
  figures to show nothing is denied."

---

## E. Kit spec §D: buildable and exact?

**14. Not blocking — the arithmetic in §C that is wrong as written.**
- **4.1 `hat`:** 165 cm + 30 cm = 195 cm under a 190 cm door *does not clear*;
  the entry says "clears". Either make the door 200 cm, or keep 190 and make
  the point the chapter's (she ducks without calculating).
- **5.5 `far`:** 6.5·(1/500 − 1/600) = 13/6000 against 6.5·(1/50 − 1/60) =
  13/600: the disparity is a *tenth*, not "a hundredth".
- **6.1 `far`:** Brunswik (160 − 42.5)/(170 − 42.5) = 235/255 reduces to
  47/51, which is what `Rtext` will print; the entry pins 235/255.
- **1.4 `three`** (front, right, above): three axis views see three faces, not
  "five of six"; and the Worked line's "front-right-above sees 3" is a corner
  view the input syntax cannot express. See finding 15.
- **1.1 `szRatio`** "3474/384400" — the tile prints the reduced fraction
  (1737/192200); say so in the Worked line or print unreduced by rule.

**15. BLOCKING — `perspective/faces` cannot produce the views §C relies on.**
§D allows a view to be one of six axis directions or a Pythagorean rotation
about the vertical. That sees at most two faces, so `peMax: 3`, "corner-on:
three" (5.1), "no view sees more than three" (3.1) and the `three`/`conflict`
presets of 1.4 are impossible. *Fix:* define a view as a direction with
integer components whose norm is an integer — the six axis directions, the
Pythagorean rotations in the horizontal plane, and named **Pythagorean
quadruples** for corner views: `(1, 2, 2)/3`, `(2, 3, 6)/7`, `(1, 4, 8)/9`,
`(4, 4, 7)/9`, with signs. A face is visible when its outward normal has a
positive dot product with the view; its projected width fraction is
|component| / norm, exact. List them in D.0 beside the angles.

**16. Not blocking — `peConsistent` has no input that could make it `no`.**
Views are directions; the faces and widths are *computed* from them, so two
computed views can never contradict a box. The `conflict` preset of 1.4 needs
an input of *reported* faces. *Fix:* add an optional per-view `reports` field
(the faces a view claims to see); `peConsistent` is `no` when a view reports
a face its direction cannot see, or two views report two opposite faces from
the same side. Or drop `conflict` and `peConsistent`.

**17. BLOCKING — "no trigonometry" contradicts the SVGs the spec orders.**
`triangle` draws a triangle from angles 60° and 70°; `level` draws a 45° and
22½° tilt; neither is Pythagorean, and no rational construction gives them.
Ten shipped kits already use `Math.cos`/`Math.sin` for pixel placement, so
there is a precedent. *Fix:* state in D.0: "Tiles are exact. An SVG may use
floating-point trigonometry for pixel coordinates only; no tile, status
sentence or expectation is ever derived from a drawing." Also say in §G that
"no trigonometry" means no figure, not no picture.

**18. BLOCKING — the tilt convention is undefined, and §C uses it both ways.**
D.0 lists `3-4-5` as (cos 4/5, sin 3/5). 5.1 says the cube turned 3-4-5 shows
widths 3/5 and 4/5 (both appear, fine). 6.1 and D.1 `shape` say a disc tilted
by 3-4-5 projects axes 1 and 3/5 — but if tilt is the angle between the disc's
normal and the line of sight the minor axis is cos = 4/5; if it is the angle
between the disc's plane and the line of sight it is sin = 3/5. *Fix:* define
tilt once ("the angle between the surface's normal and the line of sight;
projected extent = cos"), and correct 6.1 to axes 1 and 4/5 for `3-4-5` (or
use `4-3-5` for 3/5).

**19. BLOCKING — tiles that compare across presets, and selects whose range depends on the preset.**
- `depth` `deRatio` "how many times smaller the disparity is at the second
  preset" — a tile sees one preset. *Fix:* each preset carries two pairs
  (`near`, `far`, `near2`, `far2`) and `deRatio` = disparity₁ / disparity₂
  within it; or drop the tile and put the tenth in prose.
- `cues/sequence` `step` is a redraw-only range 1..cues, but `first` has one
  cue and `all` has three. *Fix:* the range's max is the cfg's longest cue
  list; a step past a preset's last cue clamps to it and the banner says so.
- `cases` `caPair` — finding 6.

**20. Not blocking — tile ids and prefixes.**
- `scBody` means body-relative coordinates in `coordinates` and "rocks above
  the body's level" in `obstacle`. *Fix:* `scLevel` for the latter.
- `variation` uses prefix `va`, which is also `argkit/validity`'s prefix
  (`vaVerdict`, `vaRows`) and `capkit/value`'s. No page carries two, but the
  mathcheck blocks and the kit reports will read badly. *Fix:* `vr`.
- `light` `liBrightest` has a tie in the one preset that matters (`gelb`: disc
  and paper both 4/5). *Fix:* print every tied name in list order, and say so.
- `motion/phi` `moBand` boundaries: say whether `interval = simultaneous`
  is "seen together" or "motion" (recommend: `< simultaneous` together,
  `≤ succession` motion, else succession).
- `sorting` `lightness`: state the scale (integers 0–10) so `|Δ lightness| + 1`
  is commensurable.
- `level` `image` "a rational from −180 to 180": say whether −180 and 180 are
  the same tilt (they are) and which the tile prints.
- `cases` cell syntax: records are `a, 1, 2; b, 3, 4`; a cell of `-` is fine
  but `-1` is in the hostile sweep — state that a cell is exactly one of
  `y`, `n`, `-` and anything else reddens the banner.

**21. Not blocking — `cues/pattern` word list.** "The author designs it; about
twenty common four- and five-letter words" with tags like `gate:door`. The
`context` preset claims "one fits — gate" for `_a_e` + "a door". With twenty
common words (`gate, game, gave, have, hate, lake, make, name, same, take…`)
the lesson's claim depends entirely on which tags the author attaches, and a
reader can see that. *Fix:* record the list in §C now (it is lesson data, not
a kit detail), tag at most one word per context, and let the `wide` preset's
count (≥ 8) be the point: the letters alone cannot choose.

**22. Not blocking — page weight.** Fifteen modes with per-mode assembly
(philosophy D.0, which this spec adopts by reference) and three small SVGs will
sit in Philosophy's range (30–36 KB gzipped). The 40 KB budget is safe *only*
if `phenkit_lab` emits the active mode's block alone; say so explicitly in D.0
rather than by reference, since the Algebra pattern (ship every mode) would put
a 15-mode kit near 60 KB. Dropping `motion/positions` (finding 3) helps.

**23. BLOCKING — §E.2: the source text is unsettled, and the spec says authoring cannot start until it is.**
"Until it is, no quotation is written, and lessons are not authored." This is
the right rule and it is currently unmet. It also leaves the *translation*
unnamed, and the two English translations paginate differently, so "cited by
page in the translation the course names" could name two translations across
seven courses. *Fix:* settle one translation for the whole Subject in §E.2
(name it, how its text reaches authors, and that it is never quoted from
memory), name it in the PATH `prerequisites` once, and make every course's
`how_to` carry the same attribution line, as Capital does with the Kerr line.
Record that the spec was reviewed with §E.2 open.

---

## F. Voice §F and quoting §E.3

**24. Not blocking — the quoting rules are workable; two things are tight.**
70 words for the opening passage plus 150 in all leaves about 80 words for the
line-by-line return, which at "a few words at a time" is roughly fifteen short
phrases: enough. But (a) Read lines in §C already carry near-quotations
("the most important lesson the reduction teaches us…", "neither equal nor
unequal", "the world is not what I think, but what I live through"), each
flagged "wording checked", and Capital's §R found exactly this kind of
from-memory phrase on the page. *Fix:* strip quotation marks from Read lines
and keep them as pointers, as Capital §C does. (b) Module names "as the
translation prints them" and §B's "shortened at its end" — section titles
differ between Smith and Landes; this resolves with finding 23.

**25. Not blocking — §F.1's "modern view" aside is the one forced element.**
Mapping lecture one to intellectualism and lecture two to the body's knowledge
is neat, and the guard ("never as settling the chapter") is right. But
"the phantom limb and Ramachandran's mirror box" and "the constancy
hypothesis and predictive coding" are evidence claims, and once per lesson
across 41 lessons the Subject will read as a running comparison with
neuroscience the book cannot answer. *Fix:* "at most one such aside per
*course*, in the lesson whose chapter is about the same phenomenon", and
always in the `note` or a late `p`, never in the opening. Keep the list of
four as the only four.

**26. Not blocking — the exemplary paragraph is good and matches the rules;
one line will fail the misconception rule in the same lesson.** "The usual way
of putting this is that perception has made a mistake, and the textbook calls
the figure an illusion" is 2.2's `mistakes[0]` stated in the body before the
mistakes block — fine — but "Merleau-Ponty's reply is stranger and more
interesting" is the lesson's own voice praising one side, which Capital's
second review forbade ("Do not praise one side in the lesson's own voice").
*Fix:* "Merleau-Ponty's reply is different: the mistake is in the question."

**27. Not blocking — "The cases are people" (§F.3) should name the limit on Schneider.**
§G says the Schneider lessons say in a sentence that the argument concerns
the case as reported. Put that sentence's obligation in §F.3 too, so the voice
rule and the content rule meet in the same place, and extend it to the
amputees and the patients of 6.5.

---

## G. Enforced ranges

**28. Not blocking — the slug claim in §B is false; nothing fails.**
"every lesson slug in §C is at most 44 characters" — 5.1
`the-theory-of-the-body-is-a-theory-of-perception` is 48 (the cap exactly;
passes ≤ 48), check id 67 (passes ≤ 72). Longest check id otherwise 61
(`association-and-the-projection-of-memories`). *Fix:* either shorten 5.1 to
`the-body-and-perception` and keep the sentence, or change the sentence to
"at most 48, and every check id at most 67".

**29. Not blocking — key lines, counts, material clause all pass as written.**
Key lines are 30–43 characters (cap 46). `∠` has a spoken form ("angle") in
`speech.py`. Tagline "Seven courses and 41 lessons" and description "seven
courses … 41 lessons" parse to 7 and 41; "three Parts" and "Each lesson" do
not match the claim regex. `PHEN_DISCLAIMER_RE` phrase appears verbatim in the
material clause and nowhere in another Subject's. Note that §B's "Total 41"
and both PATH sentences must move together if findings 3 or 12 change the
count — the test reads the PATH, not §B.

**30. Not blocking — `level_note` and `level` match Capital's keys; `module`
names over 60 characters.** `Part One · Chapter 3 · The Spatiality of One's Own
Body and Motricity` is 67 characters, and §B's rule "shortened at its end" will
cut inside the title. *Fix:* drop the Part from the module name (`Chapter 3 ·
The Spatiality of One's Own Body and Motricity`, 50) — the course `summary`
already names the Part.

**31. Not blocking — the check-id prefix `php`.** Legal and short, but it is
also the name of a programming language and will mislead a grep across
`release/contract.json`. *Fix:* `phen` (4 characters; longest id becomes 68,
still under 72).
