# Pedagogy assessment — Listening (english, course 9, second version)

Formed on 2026-10-10 from the four lesson dicts in
`content/english/c4_listening/` (`part_a.py`, lesson 1; `part_b.py`, lessons
2–4), the course dict in `__init__.py`, the spoken forms in
`content/spoken/english_c4_listening.py`, the design in
`docs/english-v2/PLAN.md` (§0, §B course 9, §C course 9, §D `contractions` and
`linking`, §D.3) with its measurements in `docs/english-v2/measure/out/`, the
three kit modes (`listening` in `scripts/mathpath/labs/english.py`,
`contractions` and `linking` in `english_b.py`), the data they read
(`listening.json`, 46 weak forms and 303 stress patterns;
`wordorder_passage.json`, 944 words; `b_wilde_excerpt.json`, 1,975 words;
`b_passage_sounds.json`; the two modern documents), and the five pages as
`scripts/preview_subject.py` renders them, every preset's tiles read with
`labcheck.js --observe` and every `data-say` read off the built page. All four
lessons were read before any was changed. This replaces the assessment of the
two-lesson course; the fixes it recorded (2026-10-08) are all still in place.

Lessons, in course order: `why-it-sounds-too-fast` (rewrite),
`where-a-word-begins` (rewrite), `where-the-small-words-went` (new),
`why-words-run-together` (new). The first two share the `listening` lab and
the 944-word passage; the third has its own lab over three texts; the fourth
scores the same passage again by its sounds, which is the right economy — a
reader meets one page of Austen four times, each time asking it something new.

## Objectives and prerequisite order

- **Every objective is an act.** Pick the squashable words out of a written
  sentence and say their share; mark a strong part and say how often it
  starts a word; write the full form behind a contraction and say which kind
  of text contracts; mark three kinds of word boundary and read off their
  shares. The six course `outcomes` are the same acts with the page's own
  figures. No "understand" anywhere.
- **The course assumes nothing, and says so.** `assumes_short`,
  `assumes_long` and the path page agree it can be read first. The only
  forward reference is to Word Stress (course 8), by title, in lesson 2 and
  the course `not_covered`, exactly as PLAN §C 9.1–9.2 prescribes; the modern
  documents are credited to Word Order (course 5). Nothing points at course
  10. Inside the course the dependencies run forward: lesson 2 counts the
  words lesson 1 did not mark; lesson 3 opens on lesson 1's three vowel-less
  words (*is, will, not*); lesson 4 opens on lesson 2's "speech has no
  spaces". Each is stated in the lesson that depends on it.
- **The order is right and it is the plan's.** Weak forms first because they
  are the larger share and the quicker win; strong parts second because the
  count is defined on the remainder; contractions third because they are the
  weak forms written down; linking last because it is what fills the spaces
  lesson 2 removed. One hard idea per lesson: a closed list and its share; a
  boundary cue and its hit rate; a set of expansions and a speech/print
  contrast; three boundary kinds and their shares. No lesson carries two.

## Load, worked examples, retrieval and misconceptions

- **Worked → faded → independent, in every lesson.** Lesson 1: ten words in
  two columns, then the generalisation (one flat vowel), then four steps a
  reader does on paper with the printed list. Lesson 2: eight words
  strong-first against light-first, the generalisation (a front piece), four
  steps for a listener with no page. Lesson 3: the seven commonest short
  forms with their full forms, the one that hides its full form (*won't*),
  then four steps that end with the reader sorting *'d* and *'s* by hand on
  the lab's table. Lesson 4: five pairs from the passage with what a speaker
  does at each, then four steps that send the reader to say *take it* as one
  word. The lab is the independent practice in every case, and the course
  `how_to` sends the reader on to real speech in so many words.
- **Retrieval asks for the claims.** Sixteen quiz items; answers at 2,1,3,0 /
  1,3,0,2 / 2,1,3,0 / 3,0,2,1. Each asks for a share, a mechanism, an
  expansion or a classification the lesson made, and each `why` gives the
  figure or the reason. One distractor was arguable (below).
- **Misconceptions are named and refuted with a count.** "People speak too
  fast" (course title, lesson 1 first line, mistake 1); "I must catch every
  word" (lesson 2 steps and mistake 1); "contractions are careless" (lesson
  3 mistake 1, with 62.9% in a carefully written play against 7.7% in a
  carefully written novel); "a space is a gap" (lesson 4 mistake 1, *a
  napple*). Each is the §C misconception the plan asked for, in
  `mistakes[0]`. Lesson 4's mistake 2 ("16.7% is how often words run
  together") is a good one the plan did not ask for.

## Correctness of every claim and every figure

Read off the built pages with `--observe` and checked against the prose:

| lesson | tiles | prose |
| --- | --- | --- |
| 1, 2 | `lsWeak` 388 of 944, `lsWeakPct` 41.1%, `lsTypes` 43, `lsMixed` 42, `lsFinal` 25 of 388, `lsStrong` 393 of 479, `lsStrongPct` 82.0% | every figure stated matches; "fewer than fifty" (46 listed, 43 on the page) |
| 3 | wilde `coNt` 22 `coNot` 13 `coPct` 62.9% `coK` 18.2 `coTypes` 't 22, 's 9, 'll 2, 've 2, 'd 1; austen 1 / 12 / 7.7% / 5.3; modern 0 / 10 / 0.0% / 9.9, 's 17 | 22 of 35, 1 of 13, 0 of 10, 9.9 per thousand, 9 *'s* in the play, 17 in the documents — all match |
| 4 | `lkN` 742 of 759 scored, `lkUnknown` 17, cv 124 / 16.7%, vv 53 / 7.1%, same 16 / 2.2% | all match; 193 marked and 549 unmarked add up |

The quoted figures (whole play 168 against 143 = 54.0%, 14.7 per thousand,
the seven commonest at 77/17/17/14/14/12/11; whole novel 12 against 1,397 =
0.9%, 644 *'s*; Cutler and Carter's nine in ten) match
`measure/out/corpus.txt` and are introduced as quoted every time they appear.
The lesson-3 `note` and the lesson-2 `note` say which figures are counted on
the page and which are not. Nothing is stated that the page does not print or
the plan does not source.

Recounted from the data: the nine *'s* in the excerpt are *it's* ×3 (all
*it is*), *he's* ×2 (one *has*, one *is*), *Worthing's* ×2, *girl's*,
*lover's*; the seventeen in the documents are all possessives (*Stanley's* ×4,
*City's* ×4, *Bureau's* ×3, *men's* ×2, *I's* ×2, *ADA's*, *generation's*);
the sixteen same-consonant boundaries are ten /t/, three /r/ (*poor Reynolds*,
*your resolution*, *for writing*), one each of /d/, /n/, /ð/; every worked
pair (*proud of*, *take it*, *in a*, *and honour*, *we are*, *I am*, *the
army*, *not to*, *ought to*, *submit to*) is in the kind the lesson gives it.
The 759 is right: 943 adjacent pairs on the passage, 184 with a mark between.

Linguistic claims verified and left alone: the ten weak forms (standard RP);
the short-*i* group (*he, she, we, his, him*); *is, will, not* losing their
vowel and the contractions that result; the rhotic difference for *for, her,
there, are, were, your*; *that/have/has/had* weak only in grammar use;
strong-initial *father, answer, carriage, happiness, market*, light-initial
*believe, again, return, another*; *record* as two words by stress; *address*
as the kind of word British and American stress differently (none such on
the page; checked a list of eighty); Cutler and Carter 1987 and how their
definition of "strong" differs from the lab's; the resyllabification account
of consonant-to-vowel linking, the glide at vowel-to-vowel, the single
lengthened consonant at *not to*; *hour* beginning with a vowel and *use*
with /j/; *won't* and *shan't* not containing their full forms.

### What was wrong

1. **Lesson 1 said a listed word is said in full when it ends the sentence,
   and the tile it quotes contradicts it.** `lsFinal` counts 25 listed words
   standing last before a mark; 13 of them are *him* (6), *her* (5), *he*,
   *you* — and the pronouns are the one class that keeps its weak form in
   final position (*I saw him* ends on /ɪm/; Roach, *English Phonetics and
   Phonology*, on weak forms). The rule holds for the prepositions and
   helping verbs (*what are you looking at?*, *yes, I can*), which is what
   the quiz item tests. Mistake 3, the body paragraph "What the count does
   and does not say" and quiz 4's `why` now say: a helping verb or a small
   word such as *at* keeps its full shape at the end; the words for people
   do not; about half of the 25 are *him, her, he* or *you*, checkable on the
   printed passage, so the number likely said in full is smaller still.
2. **Lesson 3's four step and mistake titles carried `<em>`.** Titles are
   headings and `render.esc_inline` escapes them, so the page showed the
   literal text `<em>won't</em>, <em>can't</em>` and Listen read it as "is
   less than e m is greater than won't is less than over e m…" (four
   `data-say` attributes on the built page). The titles are now plain:
   "Take care with won't, can't and shan't"; "When an ending has two
   answers, try each and keep the one that reads right"; "Reading every s
   after an apostrophe as is" (*apostrophe* is defined in concept 1, which
   precedes it); "Treating the short not as a small sound you can let go by".
   No `&lt;em&gt;` remains on the page and `speech.islands` finds nothing in
   the new titles.
3. **Lesson 4's key was unspoken.** Its three figure lines each have three
   wide-gapped columns with two numbers, which `speech.is_table_row` takes
   for a table; `say_block` collapsed them to "a table, shown on the page",
   so Listen gave the headline figures of the lesson no voice. Three spoken
   forms in `english_c4_listening.py` now read them ("a consonant then a
   vowel, 124 of the 742, 16.7 percent", …), and the built `data-say`
   confirms it.
4. **The *'s* rule of thumb was false.** "A noun after it means belonging"
   fails on the play's own *It's a very painful parting*. The body now says:
   with a noun after it, look at the word in front — *it, he, she, that,
   there* means *is* (*it's the excuse I've always given*), a name or a thing
   means belonging (*Mr. Worthing's ward*).
5. **"Every one stands for a word from the list in the first lesson" was
   false for the possessive *'s*,** which stands for no word. Now "every one
   but the belonging *'s*".
6. **Two cited phrases were not in the documents.** *the City's policy* and
   *Ms. Stanley's* appear nowhere in the opinion (it has *City's motion*,
   *Stanley's complaint*, and *Ms. Stanley* without *'s*). Mistake 2 and quiz
   2's `why` now cite *Stanley's complaint*, *the City's motion*, *men's
   share*, all present in the printed texts.
7. **The count's treatment of *cannot* was silent.** The lab counts the
   token *not*; *cannot* is one word and is left out, while *can't* is
   counted on the other side. The excerpt has *cannot* once (*I cannot help
   expressing a wish*). "What the count cannot tell" now says so and that
   putting it with the 13 moves the share a little and not far.
8. **"Text that is made to be read does not contract" and "a court opinion
   written last year"** were too strong and already stale by the course's own
   concept 2 ("contracts little"). Now "careful text that is made to be read
   contracts little … a court opinion from 2025".
9. **Lesson 2 said "half of them are small words said short" twice**
   (step 1, mistake 1) where every other sentence in the course says two in
   five. Fixed.
10. **One arguable distractor.** Lesson 1 quiz 3 offered "they are said
    faster than other words" against "most of them use the same flat vowel";
    a weak syllable is shorter, which a reader could defend as faster. Now
    "they are said louder than the words around them", which nothing in the
    lesson supports.
11. **"Its weak form is a single short sound"** (lesson 3 concept 1) — /nt/
    is two. Now "has no vowel left in it", which is the fact the lesson uses.
12. ***There*** was missing from the grammar-use caveat: it squashes in
    *there was a time* and not when it points at a place, and the passage
    has two of each. One sentence added to the lesson-1 paragraph on
    *that/have/has/had*, saying the lab does not count it apart.

### What it claims to teach but cannot, and says so

- The pages cannot make a sound. Every lesson, the course `how_to`,
  `not_covered` and the lesson-4 `note` say that what a speaker does at a
  boundary is "the usual account" and is not measured. That is the right
  honesty for a Subject whose contract is counting printed words.
- Lesson 3 counts *n't* where it is written and cannot say how often a
  reader of *do not* says /dəʊnt/; the body says so.
- The weak forms are southern British and the sounds American, and both
  lessons that depend on one say which.

## Listen

Every `data-say` on the five built pages was read. Lessons 1 and 2 are as the
first assessment left them (the IPA and stress runs read as words via
`english.py`). Lesson 3's key reads "how often not is written short, as in
don't, in three texts … won't means will not, and I'll means I will"; its
worked lines read as words. Lesson 4's key now reads all three figures; its
worked lines read as words. The four broken title readings are gone. The
bare *n't*, *'s*, *'d* in body prose are not islands and carry no `data-say`;
how a browser voice says them is the browser's, and the headings were worded
so none now depends on it.

## The band

After the edits: course home 98.4%, lesson 1 98.9%, lesson 2 99.0%, lesson 3
98.3%, lesson 4 98.4%. Lesson 3's off-band words are the contractions
themselves (*can't, don't, won't, shan't*), *Worthing*, *ward*, *aloud*,
*careless*, *thumb*; the one off-band word my first draft added (*painful*)
was swapped for *excuse*, which is in band. Page weights 16.7–40.5 KB
gzipped against the 67 KB ceiling.

## Changes made

- `part_a.py` (`why-it-sounds-too-fast`): mistake 3, the "What the count
  does and does not say" paragraph and quiz 4's `why` (the final-position
  rule, with the pronoun exception and the make-up of the 25); the
  *that/have/has/had* paragraph gains *there*; quiz 3's first distractor.
- `part_b.py` (`where-a-word-begins`): "half" → "two in five" in step 1 and
  mistake 1. (`where-the-small-words-went`): four titles de-tagged and
  reworded; concept 1; the seven-endings paragraph; "Which kind of text
  contracts"; the *'s* rule of thumb; "What the count cannot tell" gains
  *cannot*; mistake 2's example; quiz 2's `why`. (`why-words-run-together`):
  nothing.
- `content/spoken/english_c4_listening.py`: three readings for lesson 4's
  key lines; docstring.
- `__init__.py`: nothing. Its figures match the tiles; `"number": 9` is
  kept because `content/english/__init__.py` has no numbering loop yet and
  four other courses write theirs the same way.
- Nothing in the kit, the data, `english.py` or `COURSES.json` was touched.
  `preview_subject.py english --course listening` reports OK after the
  edits; every pinned figure was re-read with `--observe` and is unchanged.

## Remaining issues

- **The passage carries Gutenberg furniture.** `wordorder_passage.json`
  contains `[Illustration: “Mr. Darcy with him.” ] CHAPTER LIII.
  [Illustration]` inside the text, so the 944 includes *Illustration* ×2,
  *CHAPTER*, *LIII*, and one of the 25 `lsFinal` tokens is the caption's
  *him*. The file is shared with Word Order and every figure on it is pinned
  in two courses; cutting the caption is a data change for whoever owns
  `scripts/wordlists/concordance.py`, with the pins re-read afterwards. The
  effect on any share here is under half a point.
- **The lab cannot show the make-up of the 25.** "About half are *him, her,
  he* or *you*" is checkable on the printed passage but not printed as a
  tile; a `lsFinalPron` tile would let the lesson state 13 of 25 as computed.
- **Pronouns at the end are weak, but the strict rule is intonational,**
  not sentence-final: a helping verb before a comma (*if you can, come*) is
  strong, a pronoun before one is not. The lesson's "left standing at the
  end" is the standard classroom statement and the tile's definition
  (before any of `. , ; : ? !`) is a little wider than it. Recorded, not
  fixed: the page has no intonation to count.
- **`tests.test_speech.test_no_spoken_form_for_math_that_is_gone` fails on
  `english`** for two Tense Tables runs (`-ing 1202 of 1210 right 99.34%`,
  `-s 1209 of 1210 right 99.92%`) whose text another agent is changing in
  parallel. Not a Listening defect; noted so nobody attributes it here.
- **How a browser voice reads a bare *n't*** in body prose is out of the
  content's hands; `speech.islands` does not treat an apostrophe-initial
  ending as an island, so no `data-say` can be attached without a kit change.
- **`cannot` is not in the tile.** The honest count of "*not* written in
  full" on the excerpt is 14, not 13, and the share 22 of 36. The prose now
  says so; counting *cannot* as *not* in `_contractions` would make the tile
  say it.
