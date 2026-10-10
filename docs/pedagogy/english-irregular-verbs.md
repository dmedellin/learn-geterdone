# Pedagogy assessment — Irregular Verbs (english, course 2), second version

Fresh assessment for the English v2 build (`docs/english-v2/PLAN.md` §B
course 2, §C "Course 2", §D.3 `irrshare`), replacing the 2026-10-08 review.
Formed on branch `feat/english-v2` from the three lesson dicts in
`content/english/c2_irregular_verbs/` (`part_a.py`, `part_b.py`, `part_c.py`)
and the course dict in `__init__.py`, the data the pages inline
(`content/english/data/irregular_verbs.json`, 133 rows;
`wordorder_passage.json`, the printed passage), the three kit modes the lessons
render through (`irregular`, `classes`, `irrshare` in
`scripts/mathpath/labs/english.py`, with `ENGLISH_VERB_JS` and `SCAN_JS` from
`english_core.py`), and the novel itself (`docs/english-v2/measure/data/pg1342.txt`,
sha256 `3f6bb9d6…`, as `measure/README.md` pins it). All three lessons were read
before any was changed.

Every page figure below was read off the rendered pages with
`node scripts/labcheck.js --observe` after `scripts/preview_subject.py english
--course irregular-verbs` rendered them to a scratch directory, and then
reproduced under node by running the kit's own shipped JavaScript (the
`irrshare` form table over `wordsOf`) on the passage and on the novel. The
preview reported OK before any change and OK after.

Lessons, in course order: `the-verbs-that-break-the-rules`,
`six-patterns-not-one-hundred-and-eighty`, `how-much-of-english-is-irregular`.

## Verdict

The course teaches what it claims: a definition that is a test, six string
classes a computer checks, and a share taken apart in front of the reader.
Objectives are acts, the worked examples demonstrate the steps, every page
figure is computed and labelled, and the pages sit at 99.1–99.7% of the band.
Three things were wrong and are fixed. The whole-novel figures the third
lesson quotes (12.29%, 4.98%, 15,192 of 123,611) came from a tokeniser that
split every typographic apostrophe into two words (*Bennet’s* → *Bennet*, *s*)
and kept the 1894 printing's picture captions; recounted with the page's own
matcher over the novel text only they are 12.39%, 5.01%, 15,147 of 122,294,
and the lesson now quotes those. One of the passage's 149 matches is not a
verb (*by no means*), and the lesson's residue paragraph said every homograph
on the page was a verb; it now names the false match. The *-s*/*-ing* claim in
lesson one omitted *being*. Beyond that, the course lacked the one ESL
misconception its own classification explains, *have went*, and lesson two now
states it with the count of verbs it can touch (51) and cannot (81).

## What the course teaches well

- **Observable objectives, measured by the lab or quiz.** Run the four-step
  test and say regular or irregular (`the-verbs-that-break-the-rules`:
  `standard`, `steps`, quiz 1 and 4); sort a verb by asking four questions in
  order and stopping at the first yes (`six-patterns-not-one-hundred-and-eighty`:
  `steps`, every quiz item); read two shares off the lab and say which figure
  the page computed and which it quoted (`how-much-of-english-is-irregular`:
  `standard`, `steps[3]`, quiz 1 and 4). No `standard` says "understand". The
  one weak outcome title on the course home ("Know which pattern…") is now
  "Name the pattern worth learning first".
- **The definition is a test the lab runs.** An irregular verb is one whose
  past or participle is not what the *-ed* rule builds; a class is a statement
  about which of three strings are equal. The `classes` widget asks the
  lesson's four questions of every printed row and the tiles agree with the
  prose everywhere: 60 / 37 / 21 / 9 / 4 / 1, `clOutside` 1 (*be*), the vowel
  preset 7 with 6 in the class of nine and 1 (*begin*) in the class of 37;
  `irClasses` reads 6.
- **The near-miss is the right device.** *Know/knew/known* against
  *go/went/gone* shows that a string rule says exactly what it does not cover;
  *begin/began/begun* against *sing/sang/sung* shows a second pattern (vowels)
  laid across the first (letters). Both are computed, stated in prose, worked
  and quizzed.
- **The flattering number is taken apart, and now compared on the page.** The
  headline share, then three verbs as 61.1% of it, then the top-twenty figure
  falling from 87.66% to 73.90% when they leave. The new `shTop` tile gives
  the same question a computed answer on the passage (95.3% / 93.1%), and the
  lesson explains the gap honestly: a 944-word page meets 27 distinct
  irregular verbs (24 without the three), so twenty of them cannot help
  covering nearly everything; the novel meets 112 (109). Quiz 3 retrieves
  exactly this reading.
- **Quoted against computed is labelled every time.** The key, the worked
  example and the body keep the two sets of figures in the same three-row
  shape (all / the three / the others), each novel figure is introduced as
  quoted, the course `footer_lead` says what was counted where, and quiz 4
  asks which figure the page computes.
- **Cross-references are by title** (*Tense Tables*; the Helping Verbs course
  named at the end of lesson three, which is correct now that Helping Verbs is
  course 3 and follows this course); the glossary terms (`irregular`,
  `participle`, `vowels`) are each defined with `<dfn>` before use; no sound or
  stress mark is written into prose.

## What was wrong, verified, and fixed

- **The quoted novel figures had a wrong denominator and an unclean text**
  (`how-much-of-english-is-irregular`, docstring, `summary`, `key`,
  `concepts[2]`, `worked`, `mistakes[0]`, quiz 2–4, body; `__init__.py`
  `outcomes[5]`). `docs/ENGLISH-SUBJECT.md` §5 documents 123,611 as "letters
  and apostrophes only". It is exactly the `[A-Za-z]+` count of the raw
  Gutenberg slice, which has 733 typographic apostrophes (U+2019) and no
  straight ones, so every *don’t* and *Darcy’s* was two words; the kit's
  `wordsOf`, which normalises U+2019 (PLAN §D.0), gives 122,936 on the same
  slice. The slice also carries 154 `[Illustration: …]` captions from the 1894
  George Allen edition; with them removed it has 122,294 words, which is the
  designer's own novel word count in PLAN §C 4.2. The recount with the shipped
  matcher over that text: 15,147 irregular forms (12.39%); *be* 5,858 (4.79% of
  all words), *have* 2,339, *do* 820, together 9,017 = 59.5%; the rest 6,130 =
  5.01%; the twenty commonest verbs 13,278 of 15,147 = 87.66% with the three
  and 4,530 of 6,130 = 73.90% without. PLAN §C 3.3 and 3.4 independently
  measured *have* at 2,339 and *be* at 5,858 over the novel, which confirms the
  slice. The old 15,192 / 5,873 / 9,037 / 6,155 / 87.65% / 73.89% were within
  0.1 point of these and are gone; "about one word in eight" still holds.
  The prose no longer says "about 700,000 letters" (the slice has 541,287
  letters and 694,178 characters) but "about 120,000 words, some 130 times
  the passage", which is in the band and is the comparison the lesson needs.
- **One of the 149 matches is a noun** (`how-much-of-english-is-irregular`,
  "What a match does not prove"). Every matched token on the passage was read
  in context. *left* (*it was left you conditionally*) and both *saw*s are
  verbs, as the lesson said; *means* in *by no means* is counted as the
  *he/she* form of *mean* and is not a verb. The paragraph now names it, gives
  148 of 149 and 15.7% against 15.8%, and sends the reader to the *mean* row
  of the table. The matcher is spellings-only by the Subject's contract, so
  this is residue to print, not a bug to fix.
- **`being` was missing from the two exceptions** (`the-verbs-that-break-the-rules`
  `steps[0]`; `how-much-of-english-is-irregular` body). The rules were run on
  all 133 bases under node: `vbThird` and `vbIng` build the recorded form for
  every verb except *be* (*is*, *being*; the rule would give *bing*) and *have*
  (*has*). "Every irregular verb but two" is right; the list of what *be*
  needs now includes *being*, which the kit itself writes out (`VB_IRREG`).
- **An overclaim in a one-line summary** (`the-verbs-that-break-the-rules`
  `one_line`): "they are the verbs you use most" is false of *want*, *like*,
  *look*, *use*; now "they include most of the verbs you use every day".
- **A loose key line** (`__init__.py` `key`): "half of the trouble" for 61.1%
  on the page and 59.5% on the novel is now "more than half of the trouble"
  (43 characters). `outcomes[5]` said the top twenty cover a share "of these
  words"; it is a share of the irregular forms and says so.

## Correctness of the English, verified and left alone

- Pinker's "about 180" (Words and Rules, 1999) is attributed and hedged as a
  count of judgement; 183 − 133 = 50 ("about fifty rarer ones left out") and
  183 − 132 = 51 are consistent; 132/183 = 72.1%.
- Every one of the 133 bases is a headword of `scripts/wordlists/ngsl.tsv`
  (2,859 headwords in bands 1–3). The lesson's "2,809 most common words" is
  the NGSL 1.2 count; the file adds the list's 50-word supplement (days,
  months, seasons, number words, all confirmed present), none of them a verb,
  so both figures are right and no change was made.
- The six classes partition the 132 non-*be* verbs exactly as the prose,
  key, lab labels and quizzes state. Every example is in the class named:
  *blow, grow, throw, fly, break, speak, steal, write* in the *-n* class;
  *do, go, undergo* and *drink, ring, sing, sink, spring, swim* in the class of
  nine; *become, come, overcome, run* with base = participle; *beat* alone;
  *put, hit, cut, read* with all three the same.
- Passage figures reproduced under node: 149 matches, 15.8%; *be* 49 (*was*
  20, *be* 9, *were* 6, *been* 5, *are* 5, *am* 2, *is* 2), *have* 25, *do*
  17 = 91, 61.1%; without them 58, 6.1%; *say* 7, *know* 6, *see* 5 lead;
  top twenty 142 of 149 and 54 of 58; 27 and 24 distinct verbs; 944 tokens.
  The share of words falls "by more than half" (15.8 → 6.1, 12.39 → 5.01).
- Lesson two's *be* has eight forms with two in the past; *read* in the class
  of 21 by letters with a pronunciation note; *went* as an old form that
  survived (the past of *wend*).

## Prerequisite order

Checked backwards against `docs/english-v2/COURSES.json`. The course assumes
Tense Tables only: the *-ed* rule and its doubling change (quiz 1 of lesson
one: *plan/planned*, *stop/stopped*), the *-s* and *-ing* rules (lesson one
`steps[0]`, lesson three body), and the three forming scores 99.92 / 99.34 /
99.26% on 1,210 verbs, which are the pins of "Scoring a Rule on 1,210 Real
Verbs". Lesson two needs "the same string of letters" and a last letter.
Lesson three needs a share as a division, promised by the path's
`prerequisites`. Helping Verbs is named only as what comes next, by title,
and nothing from it is assumed. Nothing is assumed from Word Order or
Listening, which now come later.

## Cognitive load

One hard idea per lesson: the definition as a test; the string classes; the
denominator trap. Lesson two's second idea (the vowel pattern across two
classes) comes after the six classes are settled, under its own heading and
preset. Lesson three now carries three parallel figures per text (share with,
share without, top twenty) for two texts, and sits at the body ceiling of 18
blocks; the load is held down by the identical three-row shape in key and
worked example and by making "which one is counted here" a step and a quiz
item. Nothing was added to its body; the residue paragraph was rewritten in
place.

## Worked-example progression and retrieval practice

Lesson one: `steps` (the four-step test) → `worked` on *walk*, *show*, *bring*
→ the lab printing the written forms of all 133 → quiz 1 and 4. Lesson two:
the four questions → the worked near-miss (*know*, *go*, *sing*) → a lab whose
summary table shows the questions' output for every class → quizzes sorting
*cut*, *gone*, *come*. Lesson three: four questions to ask of a share → a
worked example that applies them to the passage, then to the novel, with a
line per menu option → a lab whose menu is the "count again without the
biggest items" step → quiz 1, 3 and 4. Every `why` addresses the specific
wrong model (what each distractor is a share of; what the *-n* rule actually
looks at; why a short page concentrates). Quiz positions are 2, 1, 3, 0 /
3, 1, 2 / 1, 3, 0, 2, every item has four distinct choices, and each
distractor was argued for and refused ("Its base is not the same as its past"
is true of *go* and of *know*, so it separates nothing; "The novel has fewer
irregular verbs than the passage" is the reverse of what the table shows).

## Misconceptions

Named and corrected: a verb is irregular because it sounds odd (lesson one
`mistakes[0]`, *show*); the odd forms are errors that stuck (`mistakes[1]`);
a list in alphabetical order (`mistakes[2]`); the class gives the letters
(lesson two `mistakes[0]`); *go* belongs with *know* (`mistakes[1]`); a class
of one is a rule (`mistakes[2]`); twenty equal workers (lesson three
`mistakes[0]`); one old novel is English (`mistakes[1]`); a share of words is
a share of verbs (`mistakes[2]`). **Added this pass** (lesson two, "What a
class does not do"): the past put where the participle belongs, *have went*,
*have saw*, *have came*, the commonest error learners make with these verbs,
which the course defined the participle for and never named. It is tied to
the lesson's own counts: only a verb whose past and participle differ can be
got wrong that way, the 46 plus the four plus *beat* = 51; for the 60 and the
21 the two forms are one word and the error cannot happen.

## Listen

Every `key` and `worked.lines` block was read off the rendered `data-say`.
The runs that read badly by the rules (slash lists, `-n`, `-ed`) already
carry forms in `content/spoken/english.py` from the first instalment and the
lines are unchanged, so those forms still apply; `content/spoken/english_c2_irregular_verbs.py`
now lists them and stays empty so no run gets a second reading. The third
lesson's new lines hold words, counts and percentages only and read as
written ("top 20 cover 87.66 percent with, 73.90 percent without"). The
speech-island detector (`speech.islands` with `_IPA`/`_STRESS`) finds nothing
in the course's prose.

## Band and weight

`scripts/bandcheck.py --report` on the preview: course home 99.1% (2 defined),
`the-verbs-that-break-the-rules` 99.3%, `six-patterns-not-one-hundred-and-eighty`
99.7%, `how-much-of-english-is-irregular` 99.1%. Gzipped: 16.3 / 30.0 / 29.8 /
36.7 KB, under the 48 KB kit budget and the 67 KB ceiling. The rendered pages
carry no numbered cross-reference ("lesson 2", "course 1").

## Changes made

- `part_a.py`: `one_line`; `steps[0]` adds *being*.
- `part_b.py`: opening sentence; the *have went* misconception with its 51/81
  count in "What a class does not do".
- `part_c.py`: docstring (the recount and its provenance); every whole-novel
  figure (12.39%, 5.01%, 87.66%, 73.90%, 15,147 / 122,294, 5,858 / 2,339 /
  820 / 9,017 / 6,130, 4.79%) in `summary`, `key`, `concepts[2]`, `worked`,
  `mistakes[0]`, quiz 2–4 and body; "matches a form" in the summary and
  "counts as one irregular form" in the body; *being*; the *by no means*
  residue; "about 120,000 words, some 130 times the passage".
- `__init__.py`: `outcomes[2]` title, `outcomes[5]` figures and wording,
  `key[7]`, `footer_lead`.
- `content/spoken/english_c2_irregular_verbs.py`: docstring; `SPOKEN` stays `{}`.
- Verified after: `preview_subject.py english --course irregular-verbs` OK (3
  labs executed and swept, 3 pinned, 0 failing); `TestLessonDataMatchesTheRenderer`
  reports no failure for this course; band and weight as above.

## How the novel figures were recounted (so the count can be made again)

Under node, with the repository's own code: `ENGLISH_VERB_JS` + `SCAN_JS`
from `scripts/mathpath/labs/english_core.py`; the form table built exactly as
`_irrshare` builds it (`VB_IRREG = {be: {third: 'is', ing: 'being'}, have:
{third: 'has'}}`, `SH_ALSO = {be: ['am', 'are']}`, base + `vbThird` + `vbIng`
+ every `/`-split past and participle from `irregular_verbs.json`); the text
`measure/data/pg1342.txt` from `"It is a truth universally acknowledged"` to
the last `"uniting them."`, with every `\[Illustration[^\]]*\]` removed; tokens
`lower(wordsOf(text))`; a match is a token in the table; `be/have/do` counted
apart; verbs ranked by count with ties alphabetical and the first twenty
summed; shares with `share1` and `vbPct2`. Results: 122,294 tokens; 15,147
matches; *be* 5,858, *have* 2,339, *do* 820; without them 6,130; top twenty
13,278 and 4,530; distinct verbs 112 and 109. With the captions left in the
same code gives 122,936 / 15,183 / 5,865; with `[A-Za-z]+` on the raw text the
denominator is 123,611, which is where the old figure came from.

## Remaining issues, for whoever next owns this course, the kit or the data

- **`docs/ENGLISH-SUBJECT.md` §5 and `docs/english-v2/PLAN.md` §0 / §C 2.3
  still carry 12.29%, 4.98%, 87.65%, 73.89% and 123,611.** The page wins and
  the plan is corrected (PLAN, "How to read a figure"); the orchestrator owns
  both documents. `tests/content_preservation.json` `english_semantic_copy`
  quotes the old `outcomes[5]` text and is already marked for regeneration
  (PLAN §H.6).
- **The printed passage contains a caption and a chapter heading**
  (`content/english/data/wordorder_passage.json`): `[Illustration: “Mr. Darcy
  with him.” ] CHAPTER LIII. [Illustration]`, eight tokens of the 944 that are
  not Austen's prose, between "they entered the house" and "Mr. Wickham was so
  perfectly satisfied". No irregular form is among them, so no figure on this
  course moves, but the file's note says "novel text only" and the same
  passage carries the Word Order and Listening pages. The data owner should
  re-cut it as `concordance.py` cuts the chapter (captions removed) and every
  page that pins 944 re-read.
- **The `irrshare` markup ships static tile text** (`scripts/mathpath/labs/english.py`,
  `_irrshare`): `149`, `15.7%`, `91`, `61.1%` are written into the `<strong>`
  elements and overwritten on load, so with scripting off a reader sees 15.7%
  where the page computes 15.8%. The other modes ship `&mdash;`. Kit
  engineer's, one line.
- **The recount harness is not committed.** The recipe above is complete, but
  `scripts/wordlists/english_check.js` or `docs/english-v2/measure/` is where
  it belongs, so the next tokeniser change re-reads the quoted figures as
  PLAN §D.3 requires for the pinned ones.
- The 183-verb source list is still not in the repository, so 132 / 72.1% and
  the rank figures (697.5, 44%) can only be quoted.
- `__init__.py` still writes `"number": 2`; PLAN §A replaces it with the
  path's numbering loop, which is the orchestrator's wiring step (§H.1), and
  the value is the course's true position, so nothing is wrong meanwhile.
