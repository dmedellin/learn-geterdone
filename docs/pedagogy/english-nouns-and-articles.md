# Pedagogy assessment — Nouns and Articles (english, course 4)

First assessment, formed from the four lesson dicts in
`content/english/c6_nouns_articles/` (`part_a.py`: `one-noun-two-nouns`,
`nouns-with-no-plural`; `part_b.py`: `a-or-an-by-sound-not-by-letter`,
`the-before-the-only-one`; `__init__.py`, the course dict), the spoken forms in
`content/spoken/english_c6_nouns_articles.py`, the design they were written
from (`docs/english-v2/PLAN.md` §B course 4, §C course 4, §D `wordrule`, `an`,
`the_super`, §G), the kit they render through (`scripts/mathpath/labs/english.py`
modes `wordrule`, `an` and `the_super`, over the rule code in
`english_core.py`) and the data the kit inlines (`scripts/wordlists/plural_nouns.json`,
`an_sounds.json`; `content/english/data/an_concordance.json`,
`superlative_concordance.json`), on branch `feat/english-v2` on 2026-10-10,
before the second instalment is on main. No prior assessment of this course
exists; it is new in this instalment.

All four lessons were read in full before anything was changed. Every figure
below was read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py english --course
nouns-and-articles`), then recomputed from the data files with
`/usr/bin/python3`, and the preview reported OK before and after the changes:
four labs execute and survive the control sweep, four pages carry pinned
figures and every pin matches. Every page was run through `scripts/bandcheck.py`
after the changes: course home 100.0% (one glossary term), lesson one 98.8%
(five terms), lesson two 99.8% (three), lesson three 99.7% (three), lesson four
99.4% (three), all above the 98% floor. Page weight: the heaviest page
(`a-or-an-by-sound-not-by-letter`) is 42.1 KB gzipped, under the 67 KB
ceiling and under the plan's 48 KB budget.

The course is position 4 of the path and assumes Tense Tables, for the `-s`
rule, and nothing else (`assumes_short`); it is judged as such.

## Verdict

The course teaches what it says it teaches, and after this pass it says nothing
it does not compute or mark as quoted. A reader who finishes it can make the
plural of a noun they have not seen by a three-part rule, read that rule's
score on 1,887 printed nouns, name the five short lists it misses and the
reason for each, show with the lab that two "improvements" to the rule lower
its score and a narrower third raises it by two words; read the 75 nouns the
word list records no plural for and sort them into mass nouns, nouns that are
already plural or the same both ways, day and month names, and three that need
care; choose *a* or *an* by the first sound of the next word and read both
rules' scores off 493 printed lines; and put *the* or a possessive before an
*-est* word or *same*, read the four scores off 405 lines from the novel, and
tell the *most* that means *very* from the one that makes a superlative.

Before this pass it did not quite. Three claims about English were wrong or
contradicted the page's own dictionary; every step title, mistake title and
outcome title that carried `<em>` printed the tag as text and fed the read-out
voice "is less than e m is greater than"; three glossary terms were marked
`<dfn>` and never defined; and the course home sat at 96.6%, below the band the
Subject sets for itself. All of that is repaired below.

## What the course teaches well

- **Every objective is an act the lab measures.** `one-noun-two-nouns` closes
  on "write the plural of a noun you have not seen before, and say which rule
  you used"; the `wordrule` lab prints the rule that fired beside every noun
  and the dictionary's form beside that. `nouns-with-no-plural` closes on
  "say, for a noun, whether it has a plural, and which small words you may not
  put in front of it"; the same lab lists all 75. `a-or-an-by-sound-not-by-letter`
  closes on "choose a or an by saying the next word"; the `an` lab runs both
  rules on the same lines and the reader watches the misses go.
  `the-before-the-only-one` closes on "put the right small word before a
  superlative, same or next, and say when most does not make a superlative";
  the `the_super` lab prints the word before every one of 405 lines. No
  `standard` says "understand".
- **The method is the Subject's, and all four lessons keep it.** State a rule,
  measure it on printed text, show the residue. Every figure in prose is one a
  tile prints (1866 of 1887, 98.9%; 75 of 683; 486 and 493 of 493; 127 of
  142, 69 of 69, 49 of 72, 40 of 122) or is introduced as quoted every time it
  appears (the novel's 2,266 *a/an* lines, its ten nouns with no *a* and no
  plural in 122,294 words, *a time* 10 and *times* 19, *hopes* 23).
- **A refuted rule is shown, not described** (`one-noun-two-nouns`). The
  *-oes* rule and the *f → ves* rule are menu options; choosing them drops the
  score from 1866 to 1864 to 1861 and puts *photo, piano, pro* and then
  *belief, brief, chief, golf, proof, relief, roof, safe* in the misses. The
  lesson's "the count shows that; the feeling that a rule is good does not" is
  then a report of what the reader just did. This is the move the Tense Tables
  review praised, applied to its other home ground, and it is the strongest
  thing in the course.
- **The residue is sorted into kinds with a reason each.** The 21 plural misses
  are nine old forms, five *f* words, five from Greek and two single cases
  (*potato*, *stomach*, whose *ch* is said *k*), and 9 + 5 + 5 + 2 = 21 against
  the printed tile. The 75 no-plural nouns are 47 + 9 + 16 + 3, and every one
  of the 75 is in exactly one kind (checked by hand against
  `plural_nouns.json`). The 15 *-est* lines that fail the one-word scan are
  4 + 3 + 2 + 6; the 23 other *next* lines are 7 + 4 + 8 + 4; 15 of the 37
  other *most* lines follow a form of *be* or *seemed* (all recounted from
  `superlative_concordance.json` with the kit's own `tsClass` logic).
- **The limits of the instrument are content, not footnotes.** Lesson two
  says plainly that "no plural in the list" is a statement about the list
  (*Mondays* exists; *bases* exists and the list does not record it), and that
  the second half of its rule (no *a/an*) is a quoted count because the
  printed list holds no sentences. Lesson four's worked example is entirely
  about lines the one-word scan calls misses that are not misses (*the two
  youngest*, *the best and safest*). Lesson three lists the 17 next words the
  dictionary lacks and says they are not errors. A reader learns to read a
  tile as well as a rule.
- **The misconceptions are the real ones at A2.** *f → ves* as the rule;
  *informations* and *advices*; *an university* and *a hour*; *a most agreeable
  man* read as a superlative. Each is `mistakes[0]`, as the plan asks, and each
  is refuted by a number the page prints.
- **The voice is right and the band is kept.** Short declaratives, "counted on
  this page" beside every computed figure, "quoted" beside every other, British
  spelling throughout, at most five glossary terms on a page.

## What the course taught badly, or said wrongly

- **"Nine old plural forms that change the middle of the word"**
  (`one-noun-two-nouns`, concept 2, body "Reading the 21"). Seven of the nine
  do (*man, woman, foot, tooth, mouse, chairman, gentleman*); *child → children*
  adds an ending of its own and *die → dice* changes nothing in the middle.
  Now: nine old forms that no ending makes, seven of them vowel changes, and
  *child* and *die* named apart.
- **"Hell has hells"** (`nouns-with-no-plural`, worked `after`, body). The
  page's own dictionary (SCOWL `american-english`) has no *hells* and no
  *sakes*; both nouns are on the list rightly. *Basis* is the one genuine
  limit of the list (*bases* exists; the word list records no form). And
  *tennis* was filed as "left over" when it is a plain mass noun, as
  uncountable as *golf* would be if *golf* were not also a verb. The sort is
  now 47 mass nouns, 9 already plural or the same both ways, 16 days and
  months, 3 that need care (*basis, hell, sake*), with each of the three given
  its own reason; the worked lines, concept 2 and the body all carry the same
  numbers.
- **One of the nine "already plural" nouns was never named.** *Personnel* is
  on the list and in that kind, and the body listed eight. It is now named,
  with the one clause it needs (a group word used as a plural), so a reader
  can find all nine in the printed list.
- **A page number the data does not carry** (`a-or-an-by-sound-not-by-letter`,
  body). The lesson said the lab sets aside "a page number *26a*"; the
  markers table the reader sees says "part of a page number such as 21a".
  Now 21a.
- **A hit that is an artefact, passed off as a second spelling**
  (`one-noun-two-nouns`, note). The note grouped *knife* with *hero* and
  *index* as a noun "the dictionary spells both ways". The dictionary confirms
  *knifes* because it is the verb (*he knifes*), so the rule's *knifes* counts
  as right on the page although the plural a reader should write is *knives*.
  The note now says exactly that, and ties it to the lab's own limit sentence
  (spellings, not meanings). This is the same lesson the Tense Tables review
  drew from *mans* and *foots*; a learner who meets it twice will trust the
  dictionary column less and the word column more, which is right.
- **Tags in escaped fields** (all four lessons; course home). The renderer
  escapes step titles, mistake titles, outcome titles, `one_line` and
  `assumes_long` (`render.py`, `esc_inline` and `esc`), so every `<em>` in
  those fields printed as the literal text `<em>y</em>` in a heading, and the
  speech island detector, seeing `&lt;`, read it aloud as "is less than e m is
  greater than y". Nineteen fields were affected (6 + 4 + 3 + 6 on the lessons,
  5 on the course home). Every one is now plain, as the Helping Verbs course
  writes them. The rendered pages carry eight `data-say` attributes, all of
  them the intended spoken forms.
- **Glossary terms with no definition.** `<dfn>consonant</dfn>` and
  `<dfn>vowel</dfn>` (`one-noun-two-nouns`, concept 1; `a-or-an-by-sound-not-by-letter`,
  summary and concept 1) and `<dfn>adjective</dfn>` (`the-before-the-only-one`,
  concept 3) were marked and never glossed; the plan says both sound terms are
  defined on the doubling page and must be defined again where used. Each now
  carries a one-clause gloss at the mark.
- **The course home was below the band** (96.6%, floor 98%). Off-list:
  *plural(s)*, *hiss*, *consonant*, *ies*, *sensible*, *learner*,
  *superlative*, *agreeable*, *prose*, *irregular*. Fixed by defining
  *plural* with `<dfn>` in the blurb (the first prose on the page), writing the
  rule in `outcomes[0]` by example (*boxes*, *cities*) rather than by term,
  and replacing the other words with in-band ones; lesson four's `one_line`
  now quotes *a most interesting young man*, which is a real line of the
  novel, in place of *a most agreeable man*. The page reads at 100.0%.
- **A residue named without its kinds** (`the-before-the-only-one`, worked
  `after`, body). The 23 *next* lines the rule misses were explained by one
  example (*next week*); the printed rows hold four kinds (a time standing
  alone, *next to*, *next* after a verb, *the* a word or two earlier) and the
  lesson now gives each with its count. The 15 *-est* lines likewise now carry
  the count of each of their four kinds.
- **A forward dependency with no pointer** (`the-before-the-only-one`, quiz
  2). "*-est* goes on a short adjective" is the rule Small Words and
  Comparisons scores two courses later; the `why` now says so by title, as
  the house rule for cross-references asks.
- **Quiz positions.** Lesson one keyed 2, 1, 2, 0; the first question is
  reordered so the four lessons now key 3 1 2 0 / 1 0 3 1 / 1 2 3 3 / 1 3 1 2.
  Every distractor was argued for and none could be defended: *Mondays* is in
  the dictionary, so "the dictionary does not have *Mondays*" is false as the
  key says; *the tallest girl* has *the* directly before and fits the rule;
  *union* begins with the sound of *you*.

## What the course claims to teach and does

Each course-home outcome was checked against a lesson and a tile. The
plural rule's 1,866 of 1,887 is `wrHit` on `r0`; the 21 and their kinds are
lesson one's body; the two rules that lower the score are `r1` and `r2`; the
75 are `wrNone`; 493 of 493 against 486 are `anHit` on `sound` and `letter`;
127 of 142, 40 of 122 and the 45 with *a* are `tsHit` on `est` and `most` and
`tsA`. Nothing on the course home lacks a page.

## Where the plan and the page differ, and the page won

Every figure in `PLAN.md` §C course 4 is marked (m) "to be re-read", and the
plan says the page wins. The differences, each with its cause in the data
script's note or the kit's code:

- Plural list 1,936 → **1,887** rows; rule 99.1% → **98.9%**; residue 18 →
  **21**. The data script set aside 208 headwords with a reason each (number
  words, pronouns, *do* and *go*, whose NGSL forms are the verb's) and
  overrode *mans, foots, mouses* with the irregular plurals, so *men, feet,
  mice* and *life, die* join the residue and *does, goes* leave it.
- The *-oes* rule "gains one and loses five" → gains one and **loses three**
  (*no* and *two* are among the words set aside).
- No-plural nouns 99 of 738 → **75 of 683** (the stoplist).
- *a/an*: the modern documents 39 → **29** lines (ten `(a)` list markers and
  page-number *a*s are set aside and printed with their reason); the passage
  9 → 9 of **10** (*twelvemonth* is not in CMUdict).
- §C 4.3 names "*a history*, *a hundred*" as letter-rule losses on the novel.
  The designer's own output (`measure/out/cmudict.txt`) lists the novel's
  letter-rule residue as *hour, honour, honourable, one*; *history* and
  *hundred* begin with a consonant letter and the letter rule gets them right.
  The lesson never stated them. The plan entry should be corrected by its
  owner; this review did not edit the plan.
- `the_super`: every figure matches the plan as measured (142 / 127 / 93 / 34;
  69; 72 / 45; 122 / 37 / 3 / 45 / 37).

## Where a learner gets stuck, and what is left for later

- **Lesson one carries two hard ideas**: apply a rule and score it; then test
  three changes to it on the whole list. The plan places both in one lesson
  and the steps section serves only the first. The body breaks between them
  with its own heading and the quiz tests both, so the load is accepted here
  as the plan's design; a reader who stalls should be sent to the lab's menu
  before the prose, which `how_to[2]` already says.
- **"Most has two jobs" is a question of meaning**, and the page says so: it
  counts the word before and leaves the second step to the reader. That is the
  honest boundary §G draws, and the lesson draws it in the same words.
- **Much/many, few/little** are a sentence in lesson two and are not scored;
  §G records why (the design count was too noisy to state). `not_covered`
  says so.
- **The narrow *ves* rule names *-eaf* and *-olf*** for *leaf* and *wolf*,
  neither of which is in the 1,887, so two of its four endings fix nothing on
  this list; the lesson now says this in one sentence. (*-olf* is also inside
  *-lf*; that redundancy is the kit's, in `plR3`, and is harmless.)

## Outside this course, found on the way

- `tests/test_speech.py` fails one test on this branch,
  `test_no_spoken_form_for_math_that_is_gone`, on two Tense Tables runs
  (`-ing    1202 of 1210 right     99.34%`, `-s      1209 of 1210 right
  99.92%`) whose forms are keyed to lines that course's rewrite has moved.
  Not this course's; the Tense Tables pass owns it.
- `content/english/c1_tense_tables/part_b.py` carries two mistake titles with
  `<em>` ("Saying `<em>-ed</em>` as a part of its own every time", "Saying
  `<em>-s</em>` as `<em>s</em>` every time"), which will print the tags as text
  and garble the read-out exactly as this course's did. The Tense Tables pass
  owns it.

## Figures stated, and where each comes from

| figure | lesson | source |
| --- | --- | --- |
| 1866 of 1887, 98.9%, 21 misses | one-noun-two-nouns, course home | `wrHit`, `wrPct`, `wrMiss` on `r0` |
| 1864 (photo, piano, pro lost; potato gained) | one-noun-two-nouns | `r1` |
| 1861 (five fixed, eight broken) | one-noun-two-nouns | `r2` |
| 1868, 99.0% (golf the one new miss) | one-noun-two-nouns | `r3` |
| 75 of 683 | nouns-with-no-plural, course home | `wrNone`, `wrNoneOf` |
| 47 / 9 / 16 / 3 | nouns-with-no-plural | the printed list, sorted by reading |
| ten nouns with no *a/an* and no plural in 122,294 words | nouns-with-no-plural | quoted; `measure/out/corpus.txt` |
| *a time* 10, *times* 19; *hopes* 23 | nouns-with-no-plural | quoted; `corpus.txt` |
| 493 of 510; letter 486 (98.6%); sound 493 (100.0%); 7 misses | a-or-an | `anN`, `anHit`, `anPct`, `anFirst` on `all` |
| play 455: 448 and 455; modern 29 of 29; passage 9 of 9 | a-or-an | `anSource` wilde / modern / passage |
| 17 next words not in the dictionary; 10 markers | a-or-an | `anUnknown`; `AN_MARKERS` |
| novel 2,266: letter 2,239 (98.8%), sound 2,263 (99.9%), *an union* ×2, *an uniform* | a-or-an | quoted; `measure/out/cmudict.txt` |
| -est 142: 127 (93 + 34), 15 other | the-before-the-only-one | `tsN`, `tsHit`, `tsThe`, `tsPoss`, `tsOther` on `est` |
| same 69 of 69 | the-before-the-only-one | `same` |
| next 72: 49 (45 + 4), 23 other | the-before-the-only-one | `next` |
| most 122: 40 (37 + 3), 45 *a*, 37 other | the-before-the-only-one | `most`, `tsA` |
| 4 + 3 + 2 + 6; 7 + 4 + 8 + 4; 15 of 37 | the-before-the-only-one | the printed rows, sorted by reading |
