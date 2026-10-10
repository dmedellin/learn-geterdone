# Pedagogy assessment — Small Words and Comparisons (english, course 6)

Formed from the four lesson dicts in `content/english/c7_small_words/`
(`part_a.py`, `part_b.py`), the course dict in `__init__.py`, the four lab
modes they call (`time_preps` and `wordrule` in
`scripts/mathpath/labs/english.py`; `compare` and `phrasal` in
`scripts/mathpath/labs/english_b.py`), the data the labs inline
(`content/english/data/time_concordance.json`, `b_compare_concordance.json`,
`b_phrasal_concordance.json`, `scripts/wordlists/ly_adjectives.json`) and the
two modern documents, and the pages as `scripts/preview_subject.py english
--course small-words-and-comparisons` renders them, with every preset's tiles
read off the built page by `labcheck.js --observe` and every residue claim
recomputed from the data file it rests on. The design is
`docs/english-v2/PLAN.md` §C course 6 and §D (`time_preps`, `compare`,
`wordrule`, `phrasal`). In path order the course is sixth; it may assume
Tense Tables, Irregular Verbs, Helping Verbs, Nouns and Articles and Word
Order, and the plan says it leans on Word Stress (eighth) only for the word
*part*, which the comparison lesson defines inline. All four lessons were read
before any was changed; the last two sections record what was changed and what
was not.

Lessons, in course order: `in-on-at-for-time`, `bigger-or-more-big`,
`happily-simply-truly`, `give-it-up-not-give-up-it`.

## What the tiles print, and what the data confirms

Every figure a lesson states is one the page prints, and none is quoted from a
text the page does not carry. Read with `--observe`:

| lesson | preset | tiles |
| --- | --- | --- |
| `in-on-at-for-time` | `all` | 109 lines, 103 of 109, 94.5%, 6 misses: *on Sunday night, on the evening, on Thursday night, on Wednesday night, at evening, on the morning* |
| | `austen` / `wilde` / `modern` | 77 of 79, 97.5% / 9 of 13, 69.2% / 17 of 17, 100.0% |
| `bigger-or-more-big` | `austen`, rule A | 367, 337 of 367, 91.8%, 30 wrong, the 19 forms listed |
| | `austen`, rule B | 341 of 367, 92.9%, 26 wrong (*gentlest, narrowest, nobler, noblest* gone) |
| | `wilde` / `modern` | 44 of 49, 89.8% (B: 45, 91.8%) / 32 of 32, 100.0% |
| `happily-simply-truly` | `plain` / `changes` | 98 of 126, 77.8%, 28 listed / 126 of 126, 100.0%; 27 of 153 with no adverb on both |
| `give-it-up-not-give-up-it` | `austen` | 473 lines; *go away 32, sit down 29, find out 20, come back 16, give up 12*; between 34, after 8, 81.0%; 347 preposition lines |
| | `wilde` | 149; *sit down 11, go out 9, break off 8, pick up 7, come up 5*; 16, 5, 76.2%; 93 |

Recomputed from the data files: the by-kind table (day 32 of 32; month 5;
year 16; season 7; part of the day 29 of 32; night, noon or midnight 7 of 10;
festival 3; clock time 4); the seven *on … morning* lines the named-day step
catches; the bare list (*the next morning* 17, *this morning* 13, *last night*
9 in the novel); the 17 modern lines as 16 years and one *June*; the parts
table (one part 268 and 2, two parts 54 and 15, three 0 and 18, four or more 0
and 10); the 28 plain misses sorted 12 *-le*, 8 *-ic*, 7 *-y*, *tall*; the 27
with no adverb; the eight novel lines with a pronoun after the particle
(*get over it* twice, *glancing over it*, five clause starts) and the play's
five (three clause starts, *a good influence over him*, *her hand over it*).
All agree with what the lessons say, with the exceptions in the next section.
Where the plan's design figures differ from the page (the plan's 73 time lines
and 439 phrasal tokens against the page's 109 and 473), the lessons state the
page, as the plan requires.

## What the course teaches well

- **Every objective is an act and the closing `standard` measures it.** Choose
  *in*, *on* or *at* by the kind of time word and tell a phrase that takes a
  small word from one that takes none; count the parts and choose *-er* or
  *more*, then name the two-part adjectives the novel inflects that a modern
  writer would not; make the *-ly* adverb with the five changes and name the
  adjectives that have none; place a pronoun by the particle-or-preposition
  test and read off which phrasal verbs a text uses. None is "understand".
- **The residue is the lesson, and it is sorted into kinds with a reason the
  reader can use.** Six time misses become three kinds (a named day before
  *night*; a day picked out by words after the time word, which the scan
  cannot see; *evening parties*, which is not a time phrase). Thirty
  comparison misses become three (22 two-part adjectives the novel inflects,
  3 *oftener*, 5 the other way). The 28 plain *-ly* misses become four
  endings, each with its own change. The eight phrasal "exceptions" become
  clause boundaries and *over* as a preposition, and the rule stands. That is
  the Subject's method, and it is applied the same way four times.
- **The age of the text is said where it changes the answer.**
  `bigger-or-more-big` is the clearest case in the Subject so far: *handsomer*
  and *pleasanter* are 1813, the modern documents show the other side, and the
  lesson says plainly that the lab cannot sort *quieter* (still good English)
  from *handsomer* (not) because that sort is a judgement.
- **The limits of a dictionary check are taught, not hidden.** *Tally* is a
  word and is not the adverb of *tall*; *hardly* is a word and does not mean
  *hard*; the *-ue* change is never tested because no word in the list ends in
  *-ue*. A learner leaves knowing what "100.0%" does and does not prove.
- **The misconceptions are the real A2–B1 ones** and each `mistakes[0]` is the
  plan's: *in Monday morning*; *more* as always safe (*more big*); add *-ly*
  and you are done (*angryly*, *capablely*, *dramaticly*); *look at it* proving
  *give up it*. Each is refuted with the specific case and a count from the
  page, not a restatement of the rule.
- **Prerequisites are honoured.** *Noun* comes from Nouns and Articles;
  the doubling in *bigger* points to "When the Last Letter Doubles" by title;
  *helping verb* (for *may*) comes from Helping Verbs; *part* is defined
  inline with `<dfn>` before Word Stress is named, exactly as the plan asks;
  *preposition*, *adjective*, *adverb*, *pronoun*, *particle*, *phrasal verb*,
  *vowel*, *consonant* and *dictionary* are each `<dfn>` at first use on the
  page that needs them.
- **The pages are light and in band.** About 30, 38, 28 and 41 KB gzipped
  against the 67 KB ceiling. After this pass the four lessons are 99.2%,
  98.5%, 98.3% and 99.7% in the NGSL band with one to seven glossary terms
  each, and the home is 99.1% with eight (it was 95.8% with none; item 2
  below).

## What the course taught badly, or wrongly, before this pass

1. **Markup printed as text, and read aloud as symbols.** The renderer escapes
   concept, step and mistake titles and the course home's outcome titles, and
   twenty-three of them carried `<em>`. The reader saw `<em>-ly</em>` on the
   page, and the island detector, seeing `<` and `>`, wrapped each one in a
   `data-say` of "is less than e m is greater than negative l y is less than
   over e m is greater than". `happily-simply-truly` had nine such headings
   (both concept titles with an ending, all five steps, two mistakes);
   `bigger-or-more-big` four, `give-it-up-not-give-up-it` four,
   `in-on-at-for-time` two, the home four. The Word Order review had already
   recorded this failure for one title. All twenty-three are plain text now.
2. **The course home was outside the band.** 95.8% in band, 714 words, 30
   off-list tokens, 0 glossary terms, against a floor of 98% that
   `bandcheck.py` applies to every English page including course homes. The
   tokens were the course's own grammar words (*adverb* 4, *pronoun* 4,
   *adjectives* 4, *adjective* 2, *particle* 2, *preposition* 2, *phrasal* 2)
   plus *handsomer* 3, *noisy*, *honestly*, *idiom*. The home now glosses the
   five grammar terms with `<dfn>` where it first uses them (`outcomes_intro`
   and the sixth outcome), as the Word Order home does for *pronoun* and
   *adverb*; "too noisy to count honestly" is "too mixed to count well", and
   "Idiom and register" is "How a form sounds".
3. **A false count in `in-on-at-for-time`.** The body and the fourth quiz's
   `why` said *at night* alone is right "on the other seven" lines of the
   *night, noon or midnight* kind. Six are *at night*; the seventh is the
   play's *at midnight the perambulator was discovered*. Both now say six *at
   night* and one *at midnight*.
4. **The learner's procedure gave an answer the lesson itself called right
   only in the residue.** Step two said *night* takes *at* and stopped there,
   so a learner following the steps writes *at Sunday night*, while the body
   says the three writers who wrote *on Sunday night* were not wrong. Step two
   now carries the care (a day named before *night* wins, as it does for a
   morning in the last step) and says that the lab's rule stops short of it
   and loses three lines for that.
5. **Two words in the "no adverb" list are not adjectives.** `happily-simply-truly`
   listed *through* and *toward* among "the seven that remain", as adjectives
   with no *-ly* adverb. They are there because the Moby list tags them
   adjective-only; in ordinary use they are a preposition and a preposition.
   The body, the third concept and the lab panel now say the list was sorted
   by a part-of-speech list at build time, that it is not perfect, and name
   the two.
6. **A second *tally* the lesson did not know about.** *Unlike* is one of the
   126 adjectives, its dictionary-confirmed *-ly* spelling is *unlikely*, and
   *unlikely* is an adjective (it is also in the lesson's own list of 27 with
   no adverb). Both rules count it as a hit. The "honest 100% with two limits"
   paragraph now has three, and the *tally* warning in the worked block names
   *unlike* as the same case.
7. **A tie hidden by a tile.** `give-it-up-not-give-up-it` said "the novel's
   five commonest are … and *give up* 12" and "the play's are … *come up* 5".
   *Set off* also has 12 and *go over* also has 5; the `phTop` tile shows one
   of each pair because the kit breaks a tie by spelling. The concept and the
   body now say so. The fourth quiz (*go away* 32) is unaffected.
8. **Quiz questions with two defensible readings.** `bigger-or-more-big` asked
   for "the comparison of *happy*" and rejected *happiest* as "not the
   comparison", on a page that counts *-est* and *most* forms among its 367
   "comparisons"; it now asks for the *-er* form. `happily-simply-truly` asked
   which word "ends in *-ly* and has no *-ly* adverb" — *quickly* has none
   either, being one; it now asks which is an adjective and not an adverb.
   `in-on-at-for-time` asked "which kind of time word had lines the rule got
   wrong" when two kinds did and one was offered; now "which of these kinds".
   The keyed option of `give-it-up-not-give-up-it`'s third question was a
   two-line sentence beside three short ones; it is one line, and the detail
   is in the `why`.
9. **The modern documents were unnamed** ("a census report and a court
   opinion"; "a report from a count of the people"), which the Word Order
   review made a defect. The lab panel of `in-on-at-for-time` and the body of
   `bigger-or-more-big` now name *Stanley v. City of Sanford*, 606 U.S. 46
   (2025), and the Census Bureau story "U.S. Population Aging as Nation Turns
   250" (2026), as the other courses do.
10. **"Both older texts are old"** in the first lab panel; now "The two older
    texts are 1813 and 1895 English".
11. **One word, two senses.** *Clause* meant a part of a rule five times in
    `in-on-at-for-time` and once in `bigger-or-more-big`, and a grammatical
    clause in `give-it-up-not-give-up-it` ("five begin a new sentence or
    clause"). For a learner the second is the only sense the word has. The
    first two lessons now say "step" and "the rule's *-y* line".
12. **A fraction that disagreed with itself.** The `one_line` of
    `happily-simply-truly` says the plain rule is right "on four words in
    five"; its first concept title said the rule has "a quarter missing". 28
    of 126 is 22.2%, a fifth. The title now says "about a fifth".

## What it claims to teach but does not, and where a learner gets stuck

- **The "adjectives and nothing else" list has no set-aside table.** The
  `wordrule` mode offers an *excluded, and why* list for plurals and none for
  `ly`, so the two mis-tags are named in prose only; a reader who finds
  *through* in the lab's "no adverb" list has to have read the paragraph.
  A kit change (an `excluded` list for `ly`, with reasons, as `plural_nouns.json`
  carries) would let the page show it.
- **The fixed time rule is never scored.** The lesson teaches the named-day
  step for *night* as the residue's lesson, which is right, but no preset runs
  the rule with that step, so the reader cannot see what it would score. A
  second rule in `time_preps` (with *night* under the named-day step) would
  make the lesson's conclusion a tile.
- **The tie in `phTop`.** A tile that printed both members of a tie would
  remove the need for the sentence in item 7.
- **The modern comparison sample tests one side of the comparison rule.** The
  32 modern forms are 27 one-part and 5 two-part *-er/-est* forms and no *more*
  or *most* at all. The lesson says so twice and draws only the conclusion the
  data allows (nothing in them breaks the rule; it does not show a modern
  preference for *more handsome*). Nothing more can be done with this data.
- **The *-ue* and *-ll* changes are tested on zero and one word**, and the one
  is *tall*. The lesson says so. The plan's own examples (*true*, *full*) are
  not in the list because the word list files them under another part of
  speech; the note says that too.
- **Three of the phrasal lines are not verbs.** *Any great advantage over the
  country*, *a good influence over him*, *her hand over it*: the data script
  took *advantage*, *influence* and *hand* as verb forms. The lesson names the
  first as an example of a soft row and reads the other two correctly as nouns
  among the play's five; the counts 473 and 149 include them and the lesson
  does not pretend otherwise.
- **Cognitive load.** Each lesson carries one rule. `in-on-at-for-time` adds
  the list of time words with no preposition, a fourth idea; it is short, it
  is the third concept and the third mistake, and a learner who adds *in* to
  *this morning* needs it. `bigger-or-more-big` carries two rules (A and B)
  and keeps B to one paragraph and one quiz question, as a rule built to fit
  the novel. No lesson needs splitting.
- **Worked-example progression.** Concepts → four or five steps → lab (every
  row printed, the reader free to disagree) → worked residue with one line per
  kind → mistakes → quiz, then the body. The same shape as the first five
  courses.
- **Retrieval practice.** Twelve of the sixteen quiz questions ask the reader
  to apply a rule or read a figure the page prints; the `why` of each answers
  the specific distractor (*happyer* skips the spelling change; *more happy*
  is what the rule replaces; "the lab counted wrongly" is answered with what
  the eight lines are). Keys are spread: `[1, 3, 0, 2]`, `[2, 0, 3, 1]`,
  `[3, 2, 1, 0]`, `[1, 2, 3, 0]`.

## Prerequisite order

Checked backwards along the path. *Noun* (Nouns and Articles) is used from the
first sentence of `in-on-at-for-time` and defined nowhere here, rightly.
*Helping verb* appears once (*may* is left out of the months because it is
also a helping verb), from Helping Verbs. The doubling in *bigger* is sent to
"When the Last Letter Doubles" by title. *Part* for syllable is defined with
`<dfn>` in the first concept of `bigger-or-more-big` and Word Stress is named
as the course that goes further, which is the plan's arrangement for a
prerequisite that sits later in the path. Within the course: *preposition* is
defined in lessons one and four, *adjective* in two and three, *adverb* in two
(for *oftener*) and three, *pronoun*, *particle* and *phrasal verb* in four,
*vowel* and *dictionary* in two, *consonant* in three. Vocabulary and Reading
(tenth) runs this course's *-er/-est* and *-ly* rules as reductions, and the
`compare` and `wordrule` code they would reuse is what these pages run. No
violation sits in an earlier course.

One label is wrong and is the plan's: `happily-simply-truly` sits in the
module *Making a comparison* (PLAN §C course 6: modules 2–3). Making an
adverb is not a comparison; the course `syllabus_intro` gives the real
grouping ("the two lessons that build a new word from an old one"). The module
names are the designer's and are not changed here.

## Accuracy of the English

Checked claim by claim. *At* with a clock time, *night*, *noon*, *midnight*
and a festival; *on* with a day; *in* with a month, a year, a season and a
part of the day; a named or picked-out day turning *in the morning* into *on
Monday morning* and *on the following morning*: right. *At Christmas* is
British, and the course is British; American English says *on Christmas Day*,
which names a day and falls under the rule as stated. *This morning*, *last
night*, *every morning*, *next Tuesday* with no preposition: right. The
comparison rule (one part *-er*; two parts in *-y* *-ier*; otherwise *more*)
and rule B's *-ow*, *-le*, *-er* extension are the standard textbook account;
*quieter* and *narrower* as still current and *handsomer*, *pleasanter* as
dated; *oftener* as an adverb; *more likely* as the usual modern form; *more
strange* and *most sure* as a writer's choice: right. The five *-ly* changes
(consonant + *-y* → *-ily*; consonant + *-le* → *-ly*, so *sole → solely* is
untouched; *-ic → -ically* except *publicly*; *-ue → -uly*; *-ll → -lly*) and
the facts that *hardly*, *lately* and *highly* have moved away from *hard*,
*late* and *high*, that *fast* and *hard* are adverbs with no ending, and that
*elderly*, *ugly*, *friendly* and *unlikely* are adjectives: right. The
particle-against-preposition test by the pronoun's place, a noun object on
either side of a particle, *over* as both, *her* excluded as a possessive:
right. Two hedges are in place and were left: "no *-ly* adverb the dictionary
knows" covers *sorrily*, *numerously* and *unclearly*, which exist in some
dictionaries and not in the one used; "in any ordinary use" covers *a through
train*.

## Changes made

- `__init__.py`: the four outcome titles are plain text; `outcomes_intro`
  glosses *preposition*, *adjective* (and *adjectives*), *adverb* and
  *pronoun* with `<dfn>`; the sixth outcome glosses *particle* and *phrasal
  verb*; `not_covered[1]` and `not_covered[3]` reworded. Nothing in the key or
  the footer changed.
- `in-on-at-for-time`: `summary`, worked `after` and two body sentences say
  "step" for "clause"; step two's title is plain and its body carries the
  named-day care for *night* and says the lab's rule stops short of it; the
  lab panel names the two older texts' dates and the two modern documents;
  the body's "other seven" and the fourth quiz's `why` give six *at night* and
  one *at midnight*; the first mistake's title is plain; the second quiz asks
  "which of these kinds".
- `bigger-or-more-big`: two step titles and two mistake titles plain; the
  first quiz asks for the *-er* form and its `why` says why *happiest* is not
  the answer; "the *-y* clause" is "the rule's *-y* line"; the body paragraph
  on the modern documents names them; the `note` points to the names.
- `happily-simply-truly`: both concept titles with an ending, all five step
  titles and both mistake titles plain; the first concept says "about a
  fifth"; the third concept, the lab panel, the second body paragraph and the
  "no adverb" paragraph say the list came from a part-of-speech list and name
  *through* and *toward* as its two mistakes; the "honest 100%" paragraph has
  three limits and the worked block names *unlike → unlikely* beside *tall →
  tally*; the third quiz asks which word is an adjective, not an adverb.
- `give-it-up-not-give-up-it`: three step titles and the first mistake's
  title plain; the third concept and the body say that *set off* ties *give
  up* at 12 and *go over* ties *come up* at 5 and that the tile shows the
  first by spelling; the third quiz's keyed option is one line.
- `content/spoken/english_c7_small_words.py`: unchanged. Every key and worked
  line on the four pages was read from `data-say` on the built pages; the
  fourteen forms in the file cover every run with an ending or a date, and
  the only wrong readings on the pages were the escaped-title islands, which
  the markup fix removes rather than a spoken form.

## Remaining issues

- **The module label** for `happily-simply-truly` (above) is the plan's to
  correct.
- **Three kit items**, none of which blocks the course: an *excluded* list
  for `wordrule`'s `ly` list; a `time_preps` rule that includes the named-day
  step for *night*; and a `phTop` tile that prints both members of a tie.
- **The spoken file is per-course.** `speechcheck.py` loads
  `content/spoken/english.py` by name and does not see
  `english_c7_small_words.py`; `render.py` merges every file, so the pages
  read correctly. The orchestrator merges the fourteen entries into
  `english.py` at wiring (PLAN §H.9); none clashes with an existing run.
- **`tests/content_preservation.json`** will need fresh fingerprints for the
  three course files once English's `content_errors` entries are generated;
  the orchestrator owns that.
- **The home carries *Happily* and *happyly* off-list by design** (the lesson
  title and the blurb's deliberate error), three *handsomer* and one
  *dictionary*; at 99.1% it is in band with room to spare after the glosses.
- **`tests.test_speech` fails today on two Tense Tables runs**
  (`-ing    1202 of 1210 right     99.34%` and `-s      1209 of 1210 right
  99.92%`) whose spoken forms in `content/spoken/english.py` outlive the
  lines, which that course's rewrite is moving. Nothing in this course is
  involved; the fix belongs to the Tense Tables pass or the orchestrator's
  merge of the spoken files.
