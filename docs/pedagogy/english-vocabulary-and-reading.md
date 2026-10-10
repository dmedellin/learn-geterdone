# Pedagogy assessment — Vocabulary and Reading (english, course 10)

First assessment, formed from the three lesson dicts in
`content/english/c10_vocabulary/part_a.py` (`how-much-of-a-page-you-know`,
`ten-words-are-a-quarter-of-the-page`, `word-or-word-family`), the course dict
in `__init__.py`, the spoken forms in `content/spoken/english_c10_vocabulary.py`,
the design they were written from (`docs/english-v2/PLAN.md` §B course 10, §C
course 10, §D `coverage`, §G), the kit they render through
(`scripts/mathpath/labs/english_b.py`, mode `coverage`, over `B_COVER_JS`) and
the data the kit inlines (`scripts/wordlists/ngsl.tsv`, 10,296 forms under
2,859 headwords in three bands; `content/english/data/wordorder_passage.json`;
`b_wilde_excerpt.json`; the two modern documents), on branch `feat/english-v2`
on 2026-10-10, before the second instalment is on main. No prior assessment of
this course exists; it is new in this instalment.

All three lessons were read in full before anything was changed. Every figure
below was read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py english --course
vocabulary-and-reading`); every table the lab prints — the words not covered,
the names, the family rows and the hundred commonest words, for each of the
three texts — was dumped from the running page with the `labcheck.js` DOM shim
and read row by row; and the two figures the lesson states as counted away from
the page (the 10,296 recorded forms; coverage by the forms list against
coverage by the rules) were recomputed in node by running the shipped
`cvBand` over `ngsl.tsv`. The preview reported OK before and after the
changes: three labs execute and survive the control sweep, three pages carry
pinned figures and every pin matches. After the changes `scripts/bandcheck.py`
reads course home 99.6% (no glossary term), lesson one 98.7% (three terms),
lesson two 99.2% (none), lesson three 98.3% (four), all above the 98% floor.
Page weight: 52.5 KB gzipped on the heaviest page, under the 67 KB ceiling
and over the plan's 48 KB per-page budget for English (§D.0), which is the
kit's business and not the course's: the three pages differ by one cfg key and
ship the same script.

The course is position 10 of the path and assumes Tense Tables, Irregular
Verbs, Nouns and Articles, and Small Words and Comparisons (`assumes_short`),
all earlier in `COURSES.json` order; it also names Listening and Helping Verbs
by title, both earlier. It is judged as such.

## Verdict

The course teaches what it says it teaches, and after this pass it says
nothing it does not compute or mark as quoted, and nothing about English that
the page's own data contradicts. A reader who finishes it can read the share
of a page the first 1,000, 2,000 and 2,800 headwords cover, read the share
once names are set apart, hold it against Nation's 98% and turn the gap into
"one word in N"; sort the 41 words the passage leaves into kinds and say why
each kind is there; rank a page's words and read what the top ten, fifty and
hundred cover; say what kind of word fills the top ten and why that quarter
of the page costs a reader nothing; and tell a flemma from a family, read what
the family step adds, and judge each row of the family table as a real family
or a cut that happened to land on a listed word.

Before this pass it did not quite. The course home said the passage was a
chapter of the novel and named the wrong chapter; the second lesson sorted
*that* and *was* into classes the passage's own tokens refute, and called
*was* a helping verb two courses after Helping Verbs taught that *be* is
mostly a main verb; the first lesson's worked example sorted 24 of the 41
words it said it was sorting; the third lesson's central worked row,
*notable*, was explained with the wrong root; and a number the lesson called
quoted had no source a reader could see. All of that is repaired below.

## What the course teaches well

- **Every objective is an act the lab measures.** `how-much-of-a-page-you-know`
  closes on "say what share of a page a word list covers, and what is
  missing"; the `coverage` lab prints the three band shares, the share with
  names, and every word not covered with its count. `ten-words-are-a-quarter-of-the-page`
  closes on "rank a page's words by count and say what the top ten, fifty and
  hundred cover"; the lab's ranked table prints rank, word, count and the
  share so far, and the three tiles read it off. `word-or-word-family` closes
  on "say what a flemma counts and what a family counts, and how far apart
  the two figures are"; the lab's `and names` and `and families` tiles stand
  side by side and the family table prints each row with the cut it made. No
  `standard` says "understand".
- **The method is the Subject's, and the capstone keeps it.** Every figure in
  prose is one a tile prints (944; 84.5 / 88.8 / 90.8 / 94.4 / 95.7%; 41;
  364; 25.4 / 54.4 / 67.6%; the play's 1,972 / 79.5 / 83.9 / 85.9 / 94.6 /
  95.4% / 91 / 605 / 24.9 / 50.5 / 63.3%; the modern documents' 1,685 / 76.0 /
  84.7 / 87.3 / 92.7 / 93.7% / 106 / 603 / 24.7 / 47.3 / 60.6%) or is
  introduced as quoted every time it appears (Nation's 98%, the NGSL authors'
  92%, the whole novel's 80.7 / 86.1 / 88.4 / 93.0 / 94.6% and 22.4 / 48.1 /
  58.9% over 6,308 distinct words, all of which match
  `docs/english-v2/measure/out/corpus.txt` lines 373–374).
- **The lab is the other courses' rules run backwards, and the lesson says
  so.** `how-much-of-a-page-you-know` names each reduction (`-s`, `-ed`,
  `-ing` with the spelling changes put back; the plural and the irregular
  plurals; `-er`, `-est`, `-ly`; *n't*; the irregular verbs) and the
  `assumes_long` tells a reader why the course is last. This is the
  pedagogical pay-off the plan promised (§0 item 8) and it is delivered.
- **The arithmetic a learner can reuse is taught as a step.** "Take the share
  from 100 and divide 100 by what is left" turns 94.4% into "one word in 18"
  and 98% into "one in 50"; quiz 2 of lesson one makes the reader do it on
  500 words and 25 unknowns. This is the one piece of number work in the
  course, and it is the piece a learner will use on their own pages.
- **The misconceptions are the real ones.** "2,800 words is enough to read a
  page" (lesson one, `mistakes[0]`, refuted by 85.9–90.8% and 92.7–94.6%
  against 98%); "the commonest words carry the meaning" (lesson two, refuted
  by the printed ten); "Nation's threshold and the lab's figure measure the
  same thing" (lesson three, refuted by the two tiles). Each is `mistakes[0]`
  as the plan asks.
- **The limits of the instrument are content.** Lesson one says the capital is
  the whole test for a name and that the lab cannot tell a name from a word
  that has one; lesson two's note says the lab ranks spellings (*light* the
  thing and *light* the quality are one word to it); lesson three's whole
  fourth step is "ask whether the meaning followed the spelling: the lab
  cannot, you can". A reader learns to read a tile as well as a rule.
- **The worked examples have the right shape.** Lesson one sorts a residue
  into kinds with a reason each; lesson two prints the lab's first ten rows
  and adds them up to the tile (30 + 29 + 27 + 26 + 26 + 25 + 21 + 20 + 19 +
  17 = 240, 240 of 944 = 25.4%); lesson three prints family rows with a
  reader's verdict beside the lab's. The steps then fade the guidance toward
  the reader's own text, which `how_to[2]` and the `own` preset make the
  independent practice.
- **The band is kept and the voice is right.** Short declaratives, British
  spelling, at most four glossary terms on a page (*headword*, *coverage*,
  *flemma*, *family*), and "counted on this page" or "quoted" beside every
  figure.

## What the course taught badly, or said wrongly

- **The passage was called a chapter, and the wrong chapter** (`__init__.py`
  `footer_lead`: "The passage is Chapter 26 of *Pride and Prejudice*"; blurb,
  summary, `how_to[2]`, `outcomes[0]` and lesson one's summary and body all
  said "a chapter"). The lab reads `wordorder_passage.json`, the 949-word
  passage the Word Order course prints, which is the end of Chapter 52
  (Elizabeth and Wickham in the garden) and the first lines of Chapter 53;
  the text itself carries the Gutenberg edition's `CHAPTER LIII.` heading and
  two `[Illustration …]` captions. Chapter 26 is `long_passage.json`, the
  Helping Verbs chapter, which this course never reads. Every one of those
  fields now says "a passage from a novel", and the footer names the end of
  Chapter 52 and the start of Chapter 53 and says it is the Word Order
  course's passage. The docstring records why the lab reads 944 words of a
  passage the menu calls 949: it keeps *don't* and *aunt's* as one word each
  (five such tokens), which lesson one now says in one sentence.
- **"*that*, which points" and "*was*, which helps a verb"**
  (`ten-words-are-a-quarter-of-the-page`, concept 2, worked `after`, body
  "What kind of word", steps 3, quiz 1). The passage has 17 *that*s: 14 join
  a verb to what follows (*persuaded that*, *I find that*, *I have heard that*)
  and 3 point (*on that point*, *as that*, *in that*). It has 20 *was*: not
  one is followed by an *-ing* verb (the one *-ing* word after *was* is
  *something*); they stand before an adjective (*was proud*, *was afraid*), a
  participle (*was roused*, *was overtaken*) or a noun (*there was a time*).
  Calling *was* a helping verb here contradicts "Be Is Mostly a Main Verb",
  which the reader met in Helping Verbs. The body now gives the 14 / 3 split
  and the 20 with examples, sends the reader to Helping Verbs by title, and
  every other place sorts the ten as four pronouns, two joining words, three
  words that stand before a noun or a verb, and the verb *be*.
- **The worked example sorted 24 of the 41 words it claimed to sort**
  (`how-much-of-a-page-you-know`, worked). The table prints 40 rows (41
  tokens; *oh* twice). The lines listed 23 words and the `after` said "Here
  are the words from the table"; *affectionate, affirmative, afterwards,
  commendation, conditionally, departure, exertion, interruption, palatable,
  provoked, quarrel, sensation, separation, sermons, solitary, steadfastly,
  twelvemonth* were missing. The lines now hold all 41 in seven kinds (10
  feeling and manners; 5 house and church; 11 verbs the list lacks, with the
  forms made from them; 2 British spellings; 4 made from listed words by a
  cut the lab does not make; 6 formal words; 3 the rest), the `after` adds
  the kinds to 41, and it makes the point the table forces: the table lists
  forms, so one missing verb fills two rows (*provoke*/*provoked*,
  *sermon*/*sermons*, *interrupt*/*interruption*) and the eleven are nine
  words to learn.
- **The 371 recorded forms the rules miss were misdescribed**
  (`how-much-of-a-page-you-know`, body "How the lab knows a form"). The
  lesson said "British spellings, misspellings and old or cut-short forms".
  Rerunning the shipped `cvBand` over `ngsl.tsv` confirms 10,296 / 9,925 /
  9,920 / 371 exactly, and the 371 are 152 British spellings, 74 spoken and
  cut-short forms (*gonna*, *comin*, the *didn* of *didn't*), 64 number words
  (*fourth* … *quintillionth*), 17 old or irregular forms (*cometh*, *bade*,
  *borne*, *gotten*, *farther*), 11 plurals from Latin and Greek (*crises*,
  *phenomena*) and 53 misspellings and oddities (*arguement*, *e-mail*,
  *web-site*); the five forms sent to the wrong headword are *emphasised* and
  its forms (to *emphasis*) and *won* (to *win*). The lesson now states the
  six kinds with their counts. It also said the rules give "slightly more"
  cover than the forms list on all three texts; on the play the gap is 2.3
  points (1,694 against 1,649 of 1,972), and the recomputation shows what it
  is: 46 tokens the rules cover and the forms list does not, of which 27 are
  contractions (*don't* eleven times, *couldn't*, *won't*, *isn't*, *I'd*,
  *I'll*, *shan't* …), nine are *-ly* adverbs the list does not record, and
  six are *Worthing*, a surname the *-ing* rule reads as a form of *worth*.
  The lesson now says so, false hit included.
- **Three bands that are not 1,000 / 1,000 / 800.** The list has 2,859
  headwords: 1,050 in band 1 (the ranked thousand and the fifty-odd numbers,
  days and months the NGSL adds as a supplement; 52 such words are in band 1
  of `ngsl.tsv`), 1,000 in band 2 and 809 in band 3. The lesson said "the
  commonest 1,000 … the next 1,000 … the rest"; it now gives the three counts
  and says the Subject calls 2,859 "2,800" everywhere.
- **The names paragraph put the test in the wrong order and hid what the
  table shows** (`how-much-of-a-page-you-know`, body "What counts as a
  name"). The lab asks the list first and the capital second, so a listed
  word with a capital is covered, not a name; lesson three's steps had this
  order and lesson one did not. The passage's 34 names include *Lord* (from
  *Oh, Lord!*) and *LIII*, the chapter number the printed edition carries
  inside the passage; the play's include *Ahem* three times. The paragraph
  now says all of this, so a reader who opens the names table is not
  surprised by a Roman numeral.
- **The course summary's range was wrong by a point** ("names bring each of
  them to between 93 and 95 in 100"; the modern documents' tile reads 92.7%).
  Now "between 92 and 95".
- **The central worked row of lesson three was explained with the wrong
  root.** The lab prints *notable (not + -able)* and the lesson said
  "*notable* has nothing to do with *not*" and filed the row as "a spelling
  only". The word is *note* + *-able* (worthy of note), *note* is on the
  list, and the lab printed *not* only because it tries the bare stem before
  the stem with *-e* restored and stops at the first listed word. So the row
  is right and the cut is wrong, which is a better lesson than the one the
  text taught. The worked example now says "right, by luck" and explains
  why, and takes its two "spelling only" rows from the play's family table,
  where they are unambiguous: *resides (re- + sides)* and *endure (end +
  -ure)*. The row *authority (author + -ity)*, which the lesson marked "a
  spelling only?" and then half-defended, is dropped from the worked example
  (it is a genuine derivation and a poor example of either kind). The steps,
  the second mistake, the third quiz and the body paragraph "What the step
  cannot see" are rewritten to match.
- **A figure called quoted had no source a reader could see**
  (`word-or-word-family`, note and body "Why the gap is small here"). "The
  Subject's own notes quote the cost … as three to six points" points at
  `docs/ENGLISH-SUBJECT.md` §4, which states the figure without a source.
  The number may well be right, but it is an estimate in a design document,
  not a published count, and "quoted" is the Subject's word for a published
  figure with a source. Both places now call it an estimate from the design
  notes "with no count behind it that you can see" and say nothing on the
  page measures it.
- **Prefixes do not change the kind of word** (`word-or-word-family`, concept
  2: "changes the kind of word with a beginning such as *un-* or *re-*, or an
  ending such as *-ful* …"). *Unhappy* is as much an adjective as *happy*. Now:
  a beginning turns the meaning, an ending changes the kind of word.
- **"The 41 words not covered are what stands between 94.4% and 98%"**
  (`ten-words-are-a-quarter-of-the-page`, quiz 4 `why`). Between 94.4% and
  98% stand 53 tokens: the 41 and the 12 the family step reaches
  (5.6% of 944 = 52.9). Now "the 41 words not covered, with the 12 the family
  step reaches".
- **"Five questions"** (`how-much-of-a-page-you-know`, `steps_intro`) over
  five steps of which two are questions. Now "Five steps".
- **Quiz positions.** Lesson two keyed 3 0 1 1 and lesson three 1 0 1 3; one
  question in each is reordered so the course now keys 2 0 3 1 / 3 0 1 2 /
  1 0 2 3. Every distractor was argued for and none could be defended: "95%
  rounds up to 98%" is false arithmetic; "Names are in the first 1,000
  words" is refuted by the names table (*Darcy* is in no band); "It reads the
  first forty words" is refuted by the page, which prints a dash and asks
  for fifty; "*delight* and *delightful*" is two flemmas by the lesson's own
  definition.

## Listen

The rendered pages carry two `data-say` attributes each, read before and
after the changes. Lesson one's key and worked block were read correctly by
the rules and still are (the new worked block reads as the sorted kinds).
Lesson two's worked block (ten ranked rows, four columns, mostly numbers) is
read as "a table, shown on the page", which is the house rule for a table row
(`speech.is_table_row`; `speechcheck.runs` excludes such a line, so a spoken
form keyed to one would fail `test_no_spoken_form_for_math_that_is_gone`);
the `after` prose repeats every count, so a listener loses nothing. Lesson
three's three key lines ("the passage          94.4%  to  95.7%") were also
read as "a table, shown on the page", which lost the lesson's central
figures to a listener; the double spaces round "to" made them four cells.
They are now "94.4% to 95.7%" and read as "the passage, 94.4 percent to 95.7
percent". The spoken file drops the *authority* row's form and adds forms for
the three new worked rows, with the hyphen-initial endings said as "the able
ending" and "the u r e ending"; its docstring, which claimed the ranked rows
"read correctly already", now says what actually happens and why.
`tests/test_speech.py` passes every test for this course's forms; its one
failure on this branch is the two stale Tense Tables runs the Nouns and
Articles review already recorded, which that course's pass owns.

## Quoted versus computed

Honest throughout after the fix above. Computed and read off a tile: every
share and count in the figures table below. Counted away from the page and
said so: 10,296 / 9,925 / 9,920 / 371 and the three by-forms shares (90.6 /
83.6 / 87.1%), each introduced as "checked away from this page". Quoted with
a source: Nation (2006) 98%; Browne, Culligan and Phillips 92%; the whole
novel's figures, introduced every time as "counted once over the whole novel,
which no page can carry". Called an estimate, no longer "quoted": the three
to six points.

## Where a learner gets stuck, and what is left for later

- **Lesson one carries the most.** Coverage, the three bands, the reductions,
  the forms-list check, the name test, the gap arithmetic and the reader's
  own text are one idea with six faces, in ten body blocks. The plan places
  them in one lesson and the steps serve the reader's own text, which is
  where a learner will spend their time. The forms-list paragraph is the
  densest on the page and is there because the plan requires the kit's
  reproduction to be stated (§D `coverage`, "Reproduction"); it is written
  as counts a reader can skip.
- **The family step's affix list is the kit's, and it is short** (ten
  beginnings, twenty-two endings). Lesson three says so twice and says a
  fuller count would add more; it cannot say how much more, because no
  fuller count is on the page. §G's refusal of a general letter alignment
  applies here too.
- **Band 1 is 1,050 headwords and the tile says "first 1,000"**. The lesson
  now gives the real count; the tile label is the kit's, and renaming it is a
  kit change.
- **The passage carries Gutenberg apparatus** (a chapter heading, two
  picture captions) and the play carries stage directions (*exit* twice,
  uncovered; *Ahem* as a name). Both are inherited from the texts the other
  courses print; the lesson names them so the tables are not a surprise.
  Cutting them is a data change outside this course.
- **Hyphenation breaks in the Supreme Court text** (*discrimina* and *tion*
  as two uncovered rows in the modern documents' table) are the same kind of
  inheritance and are not mentioned in the lesson; two rows of 106.

## Outside this course, found on the way

- `scripts/mathpath/labs/english_b.py` `_CV_TEXTS` labels the passage
  "the 949-word passage" while `cvN` prints 944; the lesson explains the
  difference, but the menu text is the kit's.
- The `coverage` lab's family step tries the bare stem before the stem with
  *-e*, which is why *notable* prints as *not + -able*. Trying the longer
  stem first would print *note* and change no tile. Kit's call.
- ~~`tests/test_speech.py` still fails on the two Tense Tables runs~~ —
  resolved when the spoken forms were merged into `content/spoken/english.py`.

## Figures stated, and where each comes from

| figure | lesson | source |
| --- | --- | --- |
| 944 words, 364 different | all three | `cvN`, `cvDistinct` on `passage` |
| 84.5 / 88.8 / 90.8%; 94.4% with names; 95.7% with families; 41 not covered | one, three, course home | `cvB1`, `cvB2`, `cvB3`, `cvNames`, `cvFam`, `cvOff` on `passage` |
| 1,972; 79.5 / 83.9 / 85.9 / 94.6 / 95.4%; 91; 605 | one, two, three | the same tiles on `wilde` |
| 1,685; 76.0 / 84.7 / 87.3 / 92.7 / 93.7%; 106; 603 | one, two, three | the same tiles on `modern` |
| 25.4 / 54.4 / 67.6%; 24.9 / 50.5 / 63.3%; 24.7 / 47.3 / 60.6% | two, course home | `cvTop10`, `cvTop50`, `cvTop100` |
| the passage's ten with counts and shares so far | two | the ranked table's first ten rows |
| the play's ten (*I* 89 … *is* 31); the modern documents' ten (*the* 117 … *that* 19; *age* 21) | two | the ranked tables |
| *Cecily* 64 = CECILY 44 + Cecily 20; *Algernon* 37 = 30 + 7 | two | the names table and the ranked table |
| the 41 in seven kinds (10 + 5 + 11 + 2 + 4 + 6 + 3) | one | the not-covered table, sorted by reading |
| 34 names; *Lord*, *LIII*; *Ahem* 3 | one | the names tables |
| 14 of 17 *that* join, 3 point; 20 *was*, none before an *-ing* verb | two | the passage text, every token read |
| 12 family rows, each once; 1.3 points = 12 in 944 | three | the family table on `passage` |
| *disability* 10, first row of the modern documents | three | the family table on `modern` |
| *resides (re- + sides)*, *endure (end + -ure)* | three | the family table on `wilde` |
| 2,859 headwords: 1,050 / 1,000 / 809 | one | `ngsl.tsv`, distinct headwords per band |
| 10,296 forms; 9,925 reached; 9,920 to their own headword; 371 in six kinds | one | shipped `cvBand` over `ngsl.tsv`, in node; checked away from the page |
| 90.6 / 83.6 / 87.1% by the forms list; the play's 46 extra tokens | one | the same run; checked away from the page |
| Nation 98%; Browne, Culligan and Phillips 92% | one, three | quoted, with authors |
| the novel: 80.7 / 86.1 / 88.4 / 93.0 / 94.6%; 22.4 / 48.1 / 58.9%; 6,308 | one, two, three | quoted; `measure/out/corpus.txt` lines 373–374 |
| three to six points | three | an estimate in `docs/ENGLISH-SUBJECT.md` §4, stated as such |
