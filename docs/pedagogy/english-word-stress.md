# Pedagogy assessment — Word Stress (english, course 8)

Formed from the four lesson dicts in `content/english/c9_word_stress/`
(`part_a.py`, lessons 1–2, and `part_b.py`, lessons 3–4), the course dict in
`__init__.py`, the course's place in `docs/english-v2/COURSES.json`, the design
in `docs/english-v2/PLAN.md` (§C course 8, §D `stress`, §E), the data the lab
reads (`scripts/wordlists/b_stress.json`, eighteen row sets, and the builder
`build_stress` in `scripts/wordlists/b_sounds.py`), the kit's `stress` mode in
`scripts/mathpath/labs/english_b.py`, CMUdict itself
(`docs/english-v2/measure/data/cmudict.dict`, the sha256 the plan records), and
the five pages as `scripts/preview_subject.py` renders them, with every
preset's tiles on all four lesson pages read by `labcheck.js --observe`
(eighteen presets, three list settings each). All four lessons were read before
any was changed. The last two sections record what was changed and what was not.

Lessons, in course order: `nouns-at-the-front-verbs-at-the-back`,
`endings-that-pull-the-stress`, `endings-that-leave-it-alone`,
`the-flat-vowel`. All four share one lab (the `stress` mode) and one word list
(the NGSL 2,800 against CMUdict's first pronunciation), which is the right
economy: every rule in the course is a function of a word's class or spelling,
and the dictionary is the one fact it is scored against.

## Prerequisites and place in the path

The course assumes Spelling to Sound (course 7, for what a dictionary mark is)
and Tense Tables (course 1, where "the strong part" was first needed, in the
doubling rule). Both are earlier in `COURSES.json`. Nothing in the four lessons
leans on a later course: `the-flat-vowel` points to Listening (course 9) by
title as a place where the same fact recurs, and the pointer is now worded as
"the next course" so a reader does not take it for something already met.
The one ordering fault in the path sits outside this course and is already
recorded in the plan: Small Words and Comparisons (course 6) counts parts for
`-er` against `more` before this course defines a part, and defines the word
inline. Nothing here needs to change for it.

## What the course teaches well

- **Every objective is an act.** Place the strong part of a two-part noun or
  verb from its class; say *record* both ways; place it in a word with an
  ending that pulls it; add an ending without moving it; say a weak part as
  the flat vowel; sort a rule's misses into kinds. Each lesson's `standard`
  names the act its lab and quiz measure. There is no "understand".
- **One hard idea per lesson, in the right order.** Class first (the rule a
  speaker needs in every sentence), then the endings that move the push, then
  the endings that do not, then what the rest of the word sounds like. Lesson
  2 carries seven endings but one mechanism, counting from the end, and
  teaches the mechanism rather than the list; `-ee` is kept as the contrast
  that puts the push on the ending itself.
- **The contract is honoured.** Every figure in the prose is a tile on the
  page, and every tile was re-read: nouns 207 of 231, verbs 134 of 150,
  adjectives 35 of 47, 49 pairs; `-tion/-sion` 151 of 152, `-ic` 28 of 28,
  `-ical` 16 of 16, `-ity` 27 of 27, `-ate` 36 of 36, `-ize` 13 of 14, `-ee`
  8 of 12; `-ly` 83 of 87, `-ness` 6 of 6, `-ment` 31 of 32, `-er` 48 of 50,
  `-ful` 7 of 7, `-able` 10 of 10; 2628 weak parts in 1779 words, 1387 /
  400 / 352 / 348. No whole-corpus figure is quoted anywhere, so nothing needs
  the "quoted" label; the derived shares (15.2%, 13.4%, 13.2%, 5.4%, 185 of
  192, 700 of 2628) are arithmetic on printed tiles and say so in the module
  docstrings.
- **The residue is content, and it is sorted with reasons a reader can use.**
  The 24 noun misses fall into nouns made from a verb (ten, and the verb is
  named for each), numbers and a month (three), and French loans with the push
  at the end (eleven, learned as a list). The 16 verb misses are mostly verbs
  whose second part is a weak ending (`-er`, `-en`). The `-ly` misses are the
  three words where a secondary beat becomes the main one and one mistake of
  reading (`perfectly` scored against the verb reading of `perfect`, which is
  CMUdict's first: `P ER0 F EH1 K T`, checked). `researcher` against the
  verb reading of `research` (`R IY0 S ER1 CH`, checked).
- **The misconception named in the plan is `mistakes[0]` in every lesson**,
  and each is refuted with a count rather than reassurance: "no rule" against
  nine in ten; *photograph*/*photography* against seven counted endings;
  "every ending moves it" against 185 of 192; "read every letter" against
  1387 of 2628.
- **The worked examples are the right shape.** Three words with class, rule
  and dictionary in columns, the third a miss (lesson 1); a word, its ending
  and the moved push, with the count from the end made explicit (lesson 2);
  four pairs that keep the push and the one that moves (lesson 3); four
  spellings and one sound (lesson 4). The steps then fade the guidance, and
  the lab is the independent practice, with the "words set aside" setting
  as the honest edge of each rule.
- **Retrieval practice asks for the lesson's claims.** Sixteen questions, four
  per lesson, correct positions 1 3 0 2 / 2 0 3 1 / 0 2 1 3 / 3 1 0 2. Each
  was argued for every distractor; each has one defensible answer, and each
  `why` gives the mechanism or the figure, not a restatement.

## What the course taught badly, or wrongly

1. **Five escaped fields carried `<em>` and the page showed the tags.** The
   renderer escapes `standard[0]`, a mistake's title and a course outcome's
   title, so `Say <em>record</em> both ways` (course home), `Finish when you
   can place the strong part in a word that ends in <em>-tion</em>…`
   (`endings-that-pull-the-stress`), the titles *Thinking the stress of
   `<em>`photograph`</em>`…* and *Thinking `<em>`-ee`</em>` works like the
   others* (same lesson) and `Finish when you can add <em>-ly</em>…`
   (`endings-that-leave-it-alone`) printed their tags literally, and Listen
   read each as "is less than e m is greater than … negative l y …". The tags
   are gone. `test_escaped_fields_carry_no_html` would have caught the four
   lesson fields on a full run; it does not look at course `outcomes`
   titles, which is how the course-home one survived.
2. **The flat-vowel key line was read as "a table, shown on the page".**
   `the flat vowel            1387  52.8%` is three wide-gapped cells, two
   numeric, which is the table detector's shape, so the one line that carries
   the lesson's headline figure said nothing. It now has a spoken form, and so
   do the three worked lines whose weak parts (*a*, *to*, *ten*) a voice would
   read as the article, the preposition and the number.
3. **The `-ee` misses were explained with a fact CMUdict does not have.**
   `endings-that-pull-the-stress` said that in *committee*, *employee* and
   *refugee* "the ending keeps only a lesser beat". In the first reading of
   all four misses the ending is `IY0`: no beat at all, said like the *-y* of
   *happy*. The paragraph now says that, names where the push actually falls
   (*coffee*, *refugee* first; *committee*, *employee* second), and tells
   the reader that many speakers, and British speech for *refugee*, put the
   push on the ending, which is the honest reason the rule looks weaker than
   a learner's ear says it is. It also says that *cheese* is the only `-ese`
   word on the list and is set aside, so that ending is named in the rule and
   never scored.
4. **The `-ize` tile scores `-ise` spellings and the lesson did not say so.**
   Five of the 14 rows are *advertise*, *compromise*, *exercise*, *enterprise*
   and *otherwise*; the last three are not built with the ending at all. All
   five fit the pattern, so the score is not wrong, but a reader told "the
   rule for `-ize`" would not know what was counted. The rule bullet and the
   score paragraph now disclose it.
5. **"One word appears in both lessons about endings" was false.** *career*
   is an `-eer` row in lesson 2 (scored right) and a false `-er` pair with
   *care* in lesson 3 (scored wrong); *engineer* is in both as well, and in
   lesson 3 it is a false pair with *engine*, which the lesson did not say.
   Both facts are now in `endings-that-leave-it-alone`, and the *career*
   miss is cross-referenced to the `-eer` rule that gets it right.
6. **"The false pairs work in the rule's favour as often as against it" was
   false.** Reading the rows: *beer/be, bother/both, shoulder/should,
   offer/off, flower/flow, only/on, early/ear, comment/come, capable/cap* and
   *business/bus* are all counted right; *career/care* is the one counted
   wrong. The paragraph now lists them and says the false pairs help the rule
   a little. The `-ness` paragraph says one of its six pairs is *business/bus*.
7. **The flat-vowel count was described as "every part that is not strong".**
   `build_stress` keeps only the parts CMUdict marks `0`; a part with a
   secondary beat (`2`, the first part of *education*) is neither strong nor
   counted, and a word whose other parts all carry one (*airline*,
   `EH1 R L AY2 N`) is not in the table at all. "That is 1779 words" was
   therefore not the count of two-part-or-longer words. Concept 1, the
   "What was counted" section and the lab panel now say what is counted and
   what is left out, and the "another vowel" row is explained (a part with no
   beat that keeps a clear vowel: *accept*, *employ*).
8. **The lesson 2 note gave a wrong example of reduction.** It said the first
   part of *education* "has lost the push it had in *educate*" and gone weak;
   it keeps a secondary beat and its full vowel (`EH2`). The note now uses
   *able* → *ability* (`EY1` → `AH0`, a real collapse to the flat vowel) and
   gives *educate* → *education* as the counter-example, which also prepares
   lesson 4's "smaller beat".
9. **The adjective rule's residue was never sorted.** The lesson scored it
   (35 of 47, "the weakest of the three") and said nothing about the twelve
   misses. All twelve begin with an unstressed front piece: *a-* or *un-* in
   six (*afraid, alive, ashamed, aware, unclear, unlike*) and a Latin prefix
   in six (*distinct, intense, precise, remote, severe, toward*). A new
   section gives that sort and restates the rule as "first, unless the word
   begins with a front piece", which is the form a learner can use.
10. **The blurb and the first lesson contradicted each other on what the
    error costs.** The course home said a learner who misplaces the push "is
    often not understood"; `nouns-at-the-front-verbs-at-the-back` opened with
    "is usually understood, but the word sounds less clear". A listener uses
    the strong part to find the word (the fact Listening's second lesson
    counts), so the stronger claim is the right one and the lesson now makes
    it.
11. **Smaller faults, all fixed.** *july* in lower case; "Four steps, and the
    last one is a check" over five steps; *agree/agreement* given as the
    example of a restored `-e` (it needs none; *argue/argument* does); the
    noun-from-verb list naming five of its ten verbs; the six verb misses
    that are not weak-ending verbs left without a reason (*license* and
    *premise* are nouns first, *locate* is the American reading, *argue*,
    *injure* and *marry* end in a light part); *city* set aside from `-ity`
    unmentioned; *television*'s British reading, which matches the rule,
    unmentioned; the 348 parts with the vowel of *see* said to be "mostly the
    `-y`" with no account of the rest (*i*/*e* before another vowel, as in
    *radio, area, create*, and the front piece *re-*); the `-teen` numbers
    listed as misses without the one use a learner has for the fact
    (*fifteen* against *fifty*).

## What was changed

- `__init__.py`: `outcomes[1]` title made plain; `outcomes[4]` "look-alike
  pair" (out of band) → "a false pair found by spelling".
- `part_a.py`, lesson 1: opening paragraph (the cost of the error);
  `steps_intro`; `read_intro` (adjective misses counted); the three noun-miss
  kinds (all ten verbs named, *July*, the `-teen`/*-ty* contrast, the French
  origin of the eleven, *exam* and *hello*); reasons for the six remaining
  verb misses; a new `h3` + `p` for the twelve adjective misses (body now 18
  blocks, the upper bound).
- `part_a.py`, lesson 2: `standard[0]`, `mistakes[0]` and `mistakes[2]`
  titles made plain; `-ize` bullet and score paragraph disclose the `-ise`
  rows; the asides paragraph names *city*; *television*'s British reading;
  the `-ee` paragraphs rewritten (no beat on the ending, *cheese* and `-ese`,
  the variant readings); the note's reduction example.
- `part_b.py`, lesson 3: `standard[0]` plain; *argue/argument*; the
  *business/bus* pair; *career* cross-referenced to `-eer`; the false-pair
  paragraph rewritten from the rows; "two words are scored in both lessons".
- `part_b.py`, lesson 4: concept 1 and the "What was counted" section say
  what a weak part is for the count and what is excluded; the lab
  `panel_intro` likewise; "another vowel" explained; the non-final-`-y`
  `/iː/` parts explained; "the next course, Listening".
- `content/spoken/english_c9_word_stress.py`: a form for the flat-vowel key
  line and for the *about*, *today* and *listen* worked lines; the docstring
  records the table-detector trap and the escaped-field rule.
- Module docstrings in both part files record which named words are not in
  the tables and which dictionary facts were checked.

Verification after the changes: `preview_subject.py english --course
word-stress` renders five pages, labcheck executes and sweeps all four labs,
and all eighteen pinned presets match (OK). `bandcheck.py --report`: home
98.5%, lessons 99.0 / 98.9 / 99.7 / 99.0%. Every `data-say` on the five pages
reads as words; no page contains a literal `&lt;em&gt;`. Gzipped page weight
16–38 KB against the 67 KB ceiling. `tests.test_english_kit` (28) and
`tests.test_site_invariants.TestLessonDataMatchesTheRenderer` (4) pass.

## What was not changed, and for whom

- `tests.test_speech` has one failure, `test_no_spoken_form_for_math_that_is_gone`
  on `english`, for two Tense Tables runs in `content/spoken/english.py`
  (`-s 1209 of 1210 right 99.92%`, `-ing 1202 of 1210 right 99.34%`) whose
  key lines the rewritten course no longer has. That is course 1's spoken
  data, not this course's.
- `test_escaped_fields_carry_no_html` does not check course-level `outcomes`
  titles, which is how `Say <em>record</em> both ways` reached the page. The
  invariants owner may want to add `course["outcomes"]` titles (and
  `how_to`/`not_covered` are inline, so not those) to the field list.
- The kit's default `stLimit` text and its `panel_intro` default describe the
  schwa count as "the weak parts"; the lesson's own panel text now says "the
  parts the dictionary marks with no beat at all". A one-line change in
  `english_b.py` would bring the kit's wording into line; it is not a course
  file and was left alone.
- `PLAN.md` §C course 8 gives the flat-vowel remainder as 4.8%; the page
  computes 141 of 2628 = 5.4%, and by the README's rule the page wins. The
  plan's figure should be corrected by its owner.
- CMUdict's first readings are American and sometimes the less common
  variant (*decade* `D EH0 K EY1 D`, *locate* `L OW1 K EY2 T`, *refugee*
  `R EH1 F Y UW0 JH IY0`, *employee* `EH0 M P L OY1 IY0`). The lessons say so
  where it changes an answer; a British learner will still find a few misses
  that are not misses in their own speech. Switching dictionaries is a design
  decision, not a lesson fix.
- Moby tags *license* and *premise* verb-only (the British noun spelling is
  *licence*; *premises* is the usual noun), which is why they are scored as
  verbs. The prose explains them as nouns used as verbs rather than
  changing the data.
