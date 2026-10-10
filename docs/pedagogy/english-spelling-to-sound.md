# Pedagogy assessment — Spelling to Sound (english, course 7)

First assessment, formed from the five lesson dicts in
`content/english/c8_spelling_sound/` (`part_a.py`: `c-and-g-before-e-i-and-y`,
`the-silent-e-and-the-vowels-name`, `i-before-e-and-its-failure-rate`;
`part_b.py`: `letters-you-do-not-say`, `tion-sion-and-ture`), the course dict
in `__init__.py`, the design they were written from (`docs/english-v2/PLAN.md`
§B course 7, §C course 7, §D.2 `letters`, §E, §F), the one lab mode all five
call (`letters` in `scripts/mathpath/labs/english_b.py`), the data it inlines
(`scripts/wordlists/b_letters.json`, written by `b_sounds.py` from CMUdict's
first pronunciation of each NGSL headword), the spoken forms in
`content/spoken/english_c8_spelling_sound.py`, and the six pages as
`scripts/preview_subject.py english --course spelling-to-sound` renders them,
with every preset's tiles read off the built page by `labcheck.js --observe`
and every `data-say` read off the rendered HTML. All five lessons were read
before any was changed. The course sits seventh in the path and, by its own
`assumes_short`, may assume nothing; it is judged as such.

Every figure the prose states was checked three ways: against the tile the
page prints, against the rows in `b_letters.json`, and (for the words the
prose singles out) against the CMUdict entry the data was read from. The
preview reported OK before and after the changes; after them every page is
inside the NGSL band (course home 98.6%, lessons 99.5–99.9%, two to four
glossary terms each) and the heaviest page is 33.6 KB gzipped against the
67 KB ceiling.

## Verdict

The course does what the Subject promises: each lesson states a rule from
the spelling, the page runs that rule on every word of the 2,800 it can be
tried on, compares the answer with the dictionary, and prints the score and
every miss. Nothing is quoted; every figure is computed on the page, and the
prose figures match the tiles to the word (348 of 348; 177 of 187 with the
ten *g* words; 131 of 140 and 1 of 19; 36 of 58 and 14 of 18; 42 of 42,
19 of 19, 77 of 80, 5 sounds in 10 words; 123 of 127, 24 of 25, 19 of 20,
12 of 12). The residue is sorted into kinds with reasons on every page, which
is the Subject's method at its best: nine silent-*e* misses in three groups,
22 *ie/ei* misses in three groups, 42 *gh* words in two.

What was wrong was at the edges, and most of it was the kind of error the
Subject exists to catch. The course home read its own outcome titles aloud
as HTML ("is less than e m is greater than c"), because the renderer escapes
that field and the author had put `<em>` in it. Two Listen forms taught the
wrong sound: the hard *g* of *get* was read as "gee", which is the soft one.
A word the table does not score (*gym*, not in the list; *cycle*, set aside)
sat in a key labelled "Counted on the 2,800 words", and *cost*, which the
table sets aside for its *s*, was named among the 348 words it scored. The
lesson on the silent *e* said nine words break the rule without saying that
*live* is scored as a hit only because CMUdict's first entry is the adjective.
A worked example titled "Twelve words" listed eighteen and claimed nineteen.
The fifth lesson's title said four endings are "said one way" and its own
summary said one of them has two sounds. All of that is repaired below, and
the course now says nothing its page does not show.

## What the course teaches well

- **Every objective is an act the lab measures.** Say the sound of *c* and *g*
  from the next letter and name the ten words that break the *g* rule; read
  a CVCe word with the vowel's name and name the nine that break it; apply
  the famous saying, quote its score and sort its misses; find the six silent
  places; say four endings. Each `standard` names the act and the closing
  quiz asks for it. No lesson says "understand".
- **The method is taught by the first lesson and reused, not repeated.**
  `c-and-g-before-e-i-and-y` is where the reader learns what "set aside"
  means (a word with two *c*s, a *c* inside *ch/ck/sc*, a word with an *s*
  that could make the sound) and why a score counts only the words a rule
  can be tried on. Every later lesson leans on that without re-explaining it.
  Its second mistake, "Scoring every word that has a c or a g in it", is the
  measurement lesson the Subject is for.
- **Two rules that look alike and score differently.** Soft *c* at 100.0%
  and soft *g* at 94.7% are taught together so the reader learns that a
  perfect rule and a near-perfect rule are used differently: apply and stop,
  against apply and then check a list. The `note` says it in two sentences.
- **The residue is content, every time.** The nine silent-*e* misses are
  sorted by what the vowel does instead, with a reason for the first group
  (*have*, *give*: the *e* is there for the *v*). The 22 *ie/ei* misses are
  *eigh* (8), *cie* (9) and five loners, and the lesson shows the reader that
  the famous saying's second half is its weaker half (2 of 11 after *c*). The
  42 *gh* words are split into 35 silent and 7 said as *f*, and the lesson
  points out that a perfect score for "never *g*" still leaves a choice the
  rule does not make. The ten *ough* words are printed with five sounds and
  honestly called a count, not a rule.
- **The narrowed rule is shown, not asserted.** `i-before-e-and-its-failure-rate`
  has two presets: the saying on every pair (36 of 58) and the saying only
  where the letters say *ee* (14 of 18). The reader sees that the rule's
  claim was always about one sound, and sees exactly what was set aside and
  why (14 words whose letters and parts do not line up, 26 said with another
  sound).
- **The dictionary's limits are stated where they bite.** Every lab says it
  reads CMUdict's first pronunciation and that the dictionary is American;
  `tion-sion-and-ture` tells the reader that *intention* is a miss only
  because of that first entry and to trust their ear; `letters-you-do-not-say`
  says the list spells *honor* and *neighbor* the American way.
- **The voice and the band.** Short declaratives, the act named, no "In this
  lesson". The sounds are written as plain words (*shun*, *zhun*, *chur*,
  *shul*, *oo*, *ay*) rather than IPA, so the pages carry no sound islands
  at all and every Listen line is a sentence a voice can say.

## What the course taught badly, or wrongly, before this pass

- **The course home spoke HTML** (`__init__.py`, `outcomes`). The renderer
  passes an outcome's title through `esc_inline`, so `Say <em>c</em> and
  <em>g</em>` was shown with its tags and read aloud as "S A y is less than
  e m is greater than c is less than over e m is greater than". Six outcome
  titles; four carried tags. All six are now plain text. (The sibling course
  `c7_small_words` has the same defect in its `outcomes`; it is not this
  course's file and is recorded in Remaining issues.)
- **Two spoken forms taught the wrong sound** (`content/spoken/english_c8_spelling_sound.py`).
  `get, give, girl   g before e, i: said g, a miss` was read "said gee, a
  miss": *gee* is the name of the letter, and it begins with the soft sound
  the line says these words do *not* have. `gh after a vowel never says g`
  was read "never says gee", the same inversion. Both now say "the hard g of
  go". The *j* lines, read "jay", now say "j, as in judge"; the *s* and *k*
  lines say "s, as in city" and "k, as in cat".
- **Words the table does not score, in a key labelled "Counted on the 2,800
  words"** (`c-and-g-before-e-i-and-y`, `key`, body). *gym* is not an NGSL
  headword; *cycle* is in the list but set aside (two *c*s). The key now
  shows *policy* and *energy*, both scored, both with the letter before *y*,
  both hits. The body named *cost* among the words the *c* rule gets right;
  the table sets *cost* aside because its *s* could make the sound. Now
  *cold*. The third mistake ("Leaving out the y") keeps *cycle* as the
  unscored example and names the four scored *y* words (*policy*, *agency*,
  *energy*, *strategy*).
- **"The c in each is said as sh"** (`c-and-g-before-e-i-and-y`, body) for
  the eight words set aside with both sounds or neither. CMUdict's first
  entry for *ancient* is `EY1 N CH AH0 N T`: the *church* sound, not *sh*.
  Now "in seven of them … for *ancient* the dictionary's first entry gives
  the sound at the start of *church*."
- **The computation was described as running on the whole list**
  (`c-and-g-before-e-i-and-y`, body). The page does not carry 2,800 words;
  the words with a *c* or a *g* were picked out and their sounds read from
  the dictionary before the page was built, and the page runs the rule on
  those rows and compares. The paragraph "What the table counts" now says so
  in that order. The figure is still computed on the page over printed rows,
  so nothing is quoted; the sentence is now true about where each step
  happens.
- **Nine misses, and a tenth the first-entry rule hides**
  (`the-silent-e-and-the-vowels-name`). *live* is a CVCe headword in the
  list and the table scores it as a hit because CMUdict's first entry is the
  adjective (`L AY1 V`, *live music*); the verb, which a learner uses far
  more, has the short vowel of *give* and would be a tenth miss in the first
  group. The page cannot know which *live* a reader means, and the lesson
  now says exactly that in one paragraph, keeps the page's nine, and tells
  the reader to add the tenth by ear.
- **"English words do not end in v"** (`the-silent-e-and-the-vowels-name`,
  worked, body, quiz). *rev*, *spiv*, *chav*, *Slav* exist. Now "almost
  never", in all four places; the explanation of *have* and *give* stands.
- **"Part" used for syllable without a definition**
  (`the-silent-e-and-the-vowels-name`, `i-before-e-and-its-failure-rate`).
  The course assumes nothing and the plan reserves *part* as the Subject's
  word for syllable, to be defined with `<dfn>` where used. The silent-*e*
  lesson now defines it at first use in the body ("said in one beat, as
  *hop* is and *hoping* is not"); the *ie* lesson defines "the parts of the
  word, the beats it is said in" where its second preset depends on them.
- **A rule to keep that did not cover its own cases**
  (`i-before-e-and-its-failure-rate`, "What to keep"). "c followed by *ient*
  or *ience* is written *ie*" covers *ancient*, *efficient*, *sufficient*,
  *science*, *scientific*, *scientist* and misses *efficiency*, *society*,
  *species*, three of the nine *cie* words. Now: after *c* the saying is
  right only where the pair says *ee* (*receive*, *perceive*); in the nine
  *cie* words the *i* and *e* are said apart (*science*, *society*) or the
  *c* is part of a *sh* sound (*efficient*, *species*). That is what the
  data shows (the `ie_ee` set-aside table lists *science* and *society*
  under "do not line up" and *efficient* under "said other than ee").
- **"Ten common words end in ough"** (`letters-you-do-not-say`, concept 3,
  mistake 3). *throughout*, *roughly* and *ought* do not end in it. Now "have
  *ough* in them", which is what the body already said.
- **A worked example that miscounted itself** (`letters-you-do-not-say`,
  `worked`). Titled "Twelve words", it listed 18 under the six silent places
  plus three *h* words, and its closing text called the 18 "the 19 words of
  the second rule". The nineteenth, *damn*, was in the body and the table
  but not the line. It is now in the line, the count is 19 as stated, and
  the title is "Twenty-two words and the letter each one drops".
- **The h rule left out of the "still learn words" sentence**
  (`letters-you-do-not-say`, `note`). It said only *gh* and *ough* leave
  words to learn; *h* leaves three. Added.
- **"These letters were said once, long ago"** (`letters-you-do-not-say`,
  body). True of *kn-*, *wr-*, *-mb*, *-lk*, *-lm* in older English; the *n*
  of *autumn* and *column* was Latin's and was never said in English. Now
  "Most of these letters".
- **A title that contradicted the lesson** (`tion-sion-and-ture`). "Four
  Endings Said One Way", while the summary, a concept, a step and a quiz
  question all teach that *-sion* has two sounds chosen by the letter before
  it. The title is now the plan's and `COURSES.json`'s, "-tion, -sion and
  -ture", and the `one_line` says three endings said one way and one said
  two ways. (The lesson also scores *-cial/-tial*, as the plan's §C entry
  specifies; the title names the three the module is about.)
- **"Said with two sounds, sh and then a weak un"** (`tion-sion-and-ture`,
  concept 1). *shun* is three sounds; the count was wrong and unnecessary.
  Now "said as *sh* followed by a weak *un*".
- **A miss with a reason the lesson did not give** (`tion-sion-and-ture`,
  body). *mature* was "a different sound" and nothing more. The table prints
  *choor*; the reason is that the last part is the strong one, so its vowel
  is not weakened, and the lesson now says so and points at Word Stress by
  title. Likewise *version*: the lesson now says American speech does the
  same after *r* in *conversion* and British speech says *shun* in both, so
  the reader knows the miss is a dialect fact, not noise. And *question*,
  *suggestion*: "after *s*, *-tion* is said *chun*", with *digestion* as the
  outside-the-list check.
- **The course home contradicted itself about what it teaches**
  (`__init__.py`). `outcomes_intro` promised "say a new word from its
  spelling" and `not_covered[0]` disclaimed "how to say a word you have never
  heard". The exclusion is really about other accents, and now says so.
  `assumes_long` said "No course on this site comes before this one", which
  is false for the seventh course of a ten-course path; now "No other course
  … is needed before this one". The summary's "a little over half the time"
  for 62.1% is now "about six times in ten", the figure the lesson uses.
  `outcomes[2]` said the three groups make up "most of" the failures; they
  make up all 22. `outcomes[4]` said four endings are "each said one way";
  it now separates *-sion*.
- **Quiz positions.** `the-silent-e-and-the-vowels-name` keyed two of four
  answers to the second choice; `letters-you-do-not-say` two to the fourth.
  One question in each was re-ordered. Every lesson now spreads its four
  answers over three or four positions, and every distractor was argued for
  and found wrong: *age* for the *g* rule, *move* for the silent *e*,
  *receive* against *science*, "gh is said as f in it" against what the
  rule actually claims, *mature* against *picture*.

## What it claims to teach but does not, and where a learner gets stuck

- **"Say a new word from its spelling with a number behind each guess"**
  (`outcomes_intro`) is true for the five rule families and no further: a
  reader who finishes the course can say *c*, *g*, a CVCe vowel, *ie/ei*,
  six silent places, *gh*, *h*, and five endings. Vowel pairs (*ea*, *oo*,
  *ou*), the short vowels in closed syllables, *th*, *-ed* and *-s* (taught in
  Tense Tables), and stress are not here, and the course does not pretend
  they are: `not_covered` says five rules were chosen because each can be
  scored on whole words.
- **The dictionary's first entry is a rule the reader must carry.** Three
  pages now explain a specific consequence (*ancient*, *live*, *intention*).
  A learner who skips those paragraphs will take "the dictionary says" as
  "English says". The limit sentence under every lab (`ltLimit`) and the
  panel intros repeat the point, which is as much as a page can do.
- **Load in `letters-you-do-not-say`.** Four presets (one loose rule, one
  six-place rule, one near-perfect rule, one count) is the heaviest lesson
  in the course, and the lesson count is fixed by `COURSES.json`. It holds
  together because every preset is the same question ("is this letter
  said?") and the worked example lays the six places out in five lines. A
  reader who finds it long should take the *gh* and *ough* halves on a second
  pass; the `steps` are written so each half can be used alone.
- **Where the reader gets stuck: "set aside".** The first lesson's second
  concept and second mistake carry the idea; a reader who skips to the lab
  will see 400 words set aside for *c* and may read that as the rule failing.
  The `ltAside` tile is labelled "set aside" and the `aside` view prints
  every reason, so the page answers the question, but only if the reader
  opens that view. The `how_to` on the course home tells them to.

## Prerequisite order

The course assumes nothing and now relies on nothing. *vowel*, *consonant*,
*dictionary* and *part* are defined with `<dfn>` on the pages that use them.
Its only forward references are by title: Word Stress for *mature* and for
"where the strong part falls" (`not_covered`), and the last lesson of this
course for the *sh* words set aside in the first. The plan places Word
Stress after this course "for what a CMUdict mark is", and this course does
teach that: a dictionary records how a word is said, the page reads its
first entry, and the entry is American. Nothing in the six courses before it
is needed, and nothing in it reaches back.

One cross-course observation for the orchestrator, not a defect here: Tense
Tables' fourth lesson (`how-ed-and-s-are-said`) and this course both teach
"the dictionary's first pronunciation" as a limit; the two should use the
same sentence when both are final.

## Accuracy of the claims about English

Checked against CMUdict (the data's source) and against general knowledge of
English phonology.

- Soft *c*/*g* before *e, i, y*: correct as a rule of English orthography;
  the ten *g* exceptions are the standard Germanic set (*get, give, girl,
  gift, begin, forget, gear, target, together, altogether*). The data's
  "one-source" filter (one *c*, not in *ch/ck/sc/cc/cq/qu*, no *s k q x z*)
  is sound and is explained to the reader.
- Silent *e*: the CVCe generalisation and its nine common exceptions are
  right; *have/give* as a *v*-spelling convention is the standard account;
  *r*-colouring as the reason the rule fails before *r* is right, and the
  page's sort of the 18 *r* misses (9 as in *bed*, 6 as in *or*, 2 as in
  *book*, *mere* as in *sit*) was recounted from the rows and is exact.
  *live* scored by the adjective entry is the one place the data misleads,
  and it is now named.
- *i before e*: 36 of 58 on NGSL headwords is consistent with every
  published count that finds the saying unreliable; the three groups are the
  right groups; "the saying was made for one sound" is the standard fuller
  form of the mnemonic. The *cie* explanation (two parts, or *ci* as *sh*)
  is correct.
- Silent letters: *kn-*, *wr-*, *-mb*, *-mn*, *-lk*, *-lm* are the standard
  set; *gh* never /g/ after a vowel is correct; the *f* set (*cough, enough,
  laugh, laughter, rough, roughly, tough*) is exact; *h* silent in *hour,
  honest, honor* (plus *heir*, and *herb* in American speech, now named as
  outside the list) is correct. "Letters said once" is now "most", because
  the *-mn* letters are Latin spelling, not lost English speech.
- Endings: *-tion* as /ʃən/ with /tʃən/ after *s* (*question, suggestion*)
  is right; *equation* as /ʒ/ is the one *-tion* with /ʒ/ in common use;
  *intention* with /tʃ/ is a CMUdict artefact and the lesson says so.
  *-sion*: /ʒ/ after a vowel letter, /ʃ/ after a consonant, with *-rsion*
  as /ʒ/ in American and /ʃ/ in British speech, is the correct account.
  *-ture* as /tʃər/ when unstressed and *mature* as the stressed exception
  is right. *-cial/-tial* as /ʃəl/ is right on all twelve.

## Changes made

In `content/english/c8_spelling_sound/__init__.py`: six outcome titles made
plain text; `outcomes[2]` and `outcomes[4]` bodies corrected; `summary`
("about six times in ten"); `assumes_long` ("No other course … is needed";
"sums" for "arithmetic", for the band); `blurb` ("student" for "learner",
for the band); `not_covered[0]` rewritten to the real exclusion.

In `part_a.py`: lesson 1 key (*policy*, *energy*), "What the table counts"
paragraph, *cold* for *cost*, the *ancient* sentence, italics on the five
*g* examples, mistake 3; lesson 2 `<dfn>part</dfn>`, "almost never" in four
places, the *live* paragraph, quiz 4 re-ordered (answer now third); lesson 3
`<dfn>parts</dfn>`, "What to keep" third fact.

In `part_b.py`: lesson 4 concept 3 and mistake 3 ("have *ough* in them"),
worked title and *mn* line (*damn*), note (*h* leaves three), "Most of these
letters", *heir*/*herb* sentence, quiz 4 re-ordered (answer now third);
lesson 5 title and `one_line`, concept 1, note (*chun* after *s*,
*digestion*), *version*/*conversion*, *mature* and the strong part.

In `content/spoken/english_c8_spelling_sound.py`: the two inverted *g*
readings fixed; *j*, *s*, *k* given "as in" words; the two key runs and the
*mn* worked run re-keyed to the new text; the docstring records the rule
that a sound is never given as a letter's name. 36 forms; every key was
checked against the rendered pages and none is dead.

Verification after the changes: `preview_subject.py english --course
spelling-to-sound` OK (5 labs execute and survive the sweep, 5 pages with
pinned figures, every pin matches); `bandcheck.py` 98.6% / 99.9 / 99.8 /
99.5 / 99.5 / 99.6%; heaviest page 33.6 KB gzipped; every `data-say` on the
six pages read and found to say what the line means.

## Remaining issues

- **`tests/test_speech.py` fails on Tense Tables, not on this course.**
  `test_no_spoken_form_for_math_that_is_gone` reports two dead keys in
  `content/spoken/english.py` (`-ing    1202 of 1210 right     99.34%`,
  `-s      1209 of 1210 right     99.92%`), left by the parallel rewrite of
  `scoring-a-rule-on-real-verbs`. Not this course's file; the orchestrator's
  merge step (§H.9) removes them.
- **The per-course spoken file is not yet merged.** `speechcheck.subjects()`
  loads `content/spoken/english.py` only, so the forms in
  `english_c8_spelling_sound.py` are applied by the renderer (which merges
  every file in the directory) but not checked by `tests/test_speech.py`
  until merged. The dead-key check was done by hand here.
- **`c7_small_words/__init__.py` has `<em>` in its outcome titles** and will
  show tags on its course home and read them aloud, exactly as this course
  did. Its reviewer should make them plain.
- **The course home is at 98.6% of the band** with no glossary terms
  (*vowel*, *consonant*, *dictionary*, *ough*, *shun*, *chur* are its
  off-list words). A course home has no `<dfn>` convention; anyone adding
  prose there should re-run `bandcheck.py`.
- **`PLAN.md` §C 7.2 marks `magic_r` (k)** and §C 7.3 marks the `ie_ee`
  definition (k). Both are now pinned and stated (1 of 19; 14 of 18 with
  the one-to-one alignment, against the design's rough 23 of 31 by "an *ee*
  anywhere"); the plan's figures should be corrected to the page's, as §0
  says they must.
- **`live` is scored by its adjective entry.** The lesson now says so. If
  the kit engineer ever lets `b_sounds.py` prefer a verb reading for CVCe
  headwords Moby tags verb-only, the count becomes 130 of 140 and the lesson
  must be re-read against the page.
