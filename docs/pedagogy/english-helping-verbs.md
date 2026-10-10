# Pedagogy assessment — Helping Verbs (english, course 3), first version

Fresh assessment for the English v2 build (`docs/english-v2/PLAN.md` §B
course 3, §C "Course 3", §D.2 `auxchain`), formed on branch `feat/english-v2`
from the six lesson dicts in `content/english/c5_helping_verbs/` (`part_a.py`,
`part_b.py`) and the course dict in `__init__.py`, the data the pages inline
(`content/english/data/long_passage.json`: Chapter XXVI, 2,351 words by the
kit's tokeniser, with its eight word classes built for the chapter's own
words; `MODERN_DATA`, the two modern documents), the kit mode the lessons
render through (`auxchain` in `scripts/mathpath/labs/english.py`, `AUX_JS` and
`SCAN_JS` in `english_core.py`), the designer's whole-novel output
(`docs/english-v2/measure/out/corpus.txt`, with `m_corpus.py` re-run for the
modal section) and the novel itself (`measure/data/pg1342.txt`). All six
lessons were read before any was changed.

Every page figure below was read off the rendered pages with
`node scripts/labcheck.js --observe` after `scripts/preview_subject.py english
--course helping-verbs` rendered them to a scratch directory, and every row
the six rules file was then printed under node by running the kit's own
shipped JavaScript (`SCAN_JS` + `AUX_JS` + the page's data) on the chapter and
on the modern documents, residue and hits alike, and read against the
chapter's text. The preview reported OK before any change and OK after.

Lessons, in course order: `the-s-belongs-to-he-she-and-it`,
`after-a-modal-the-verb-is-bare`, `have-is-two-words`,
`be-is-mostly-a-main-verb`, `where-not-goes`,
`which-of-the-twelve-boxes-get-used`.

## Verdict

The course is well shaped and its six rules are the right six for an A2–B2
learner: every objective is an act, every lesson runs state → steps → worked
example → lab → quiz, every `mistakes[0]` is the misconception the plan
named, and every page figure is one the page prints. What was wrong was the
reading of the residue, which is the part of the Subject's contract that
cannot be delegated to the scan. Four of the six lessons told the reader
something false about the printed rows, and one built its whole third concept
on that false reading:

- `have-is-two-words` said the "true split" was 20 helping verbs against 17
  main verbs and taught that the gap between the chapter's 45.9% and the
  novel's 59.5% was "a small sample at work". Four of the 17 rows filed as
  main verbs are perfects — two inverted conditionals (*had fortune permitted
  it*, *for had I really experienced*) and two with a phrase between (*had by
  some accident been lost*, *if he had at all cared*) — so by hand the chapter
  gives 24 helping verbs of 37, 64.9%, and the gap is the one-word scan, not
  the sample. The lesson, its key, its third concept, `mistakes[1]` and quiz 3
  now say so, and the two non-owning, non-helping rows (*had better*, *I would
  have you be*) are named.
- `after-a-modal-the-verb-is-bare` called all four "pronoun next" rows
  questions. Two are: *will you come*, *how can I promise*. The other two are
  the scan reading past a full stop (*better that he should not. I see*) and
  a comma (*Lizzy will, I am sure, be incapable*). The lesson also promised
  "the three as its named exceptions" over the novel and named none; the
  designer's script, re-run, shows all three are the same artefact (*as soon as
  he could, provided*; *as well as she could, said*; *as soon as we can, said
  Jane*), so the rule has no true exception in 2,738 rows, which is a stronger
  and truer claim than 0.1%.
- `be-is-mostly-a-main-verb` said "none of [the 19 'something else' rows] is an
  -ing form, because the scan finds those by their ending, so the 3.6%
  stands". The scan finds `-ing` forms by a 52-word list, not by ending, and
  two progressives sit in the noun-phrase group (*his marriage was now fast
  approaching*, *he was now rendering himself agreeable*: *fast* and
  *rendering* are in the chapter's noun list). By hand it is 7 of 137, 5.1%.
  It also called all three "pronoun next" rows questions; one is.
- `which-of-the-twelve-boxes-get-used` called a group of 4 "passive" when
  three of its four rows (*satisfied*, *resolved*, *convinced*) read as
  states, left the 27 rows the lab prints as *modal, other* (nearly half of
  the 57 "with a modal") unexplained, gave the wrong reason for *we all
  expect* landing in *no verb found*, and quoted the novel's progressives as
  1.5% where the designer's own counts sum to 143 of 8,864 = 1.6%.
- `the-s-belongs-to-he-she-and-it` quoted 1,152 third-person forms after
  *he/she/it* in the novel; the designer's output gives 1,081 + 133 = 1,214
  against 37. It also said the 37 "are of this kind" (*were*); 22 are, and the
  other 15 (and all 5 after *you/we/they*) are the one-word scan misreading
  *could she have seen* and *believing it are*.
- The course home printed `&lt;em&gt;be&lt;/em&gt;` literally in three outcome
  titles and in `assumes_long`, because the renderer escapes those fields, and
  Listen read them as "is less than e m is greater than b e …".

All of these are fixed in the course files. Nothing structural was changed:
slugs, lesson count, modules, presets and pinned figures are as COURSES.json
and the kit have them.

## What the course teaches well

- **Observable objectives.** Every `standard` names the act the quiz and lab
  measure: choose the form that agrees (lesson 1), list the nine and allow
  *not* or an adverb between (lesson 2), sort a *have* by the next word
  (lesson 3), sort what follows *be* and say why a passive and an adjective
  cannot be told apart (lesson 4), place *not* and add *do* (lesson 5), sort a
  phrase into its box and say which boxes carry most of a page (lesson 6). No
  `standard` says "understand"; the course `outcomes` are the same six acts.
- **The rule is a test the lab runs.** Agreement, the bare form, the perfect,
  what follows *be*, where *not* sits, the chain of helpers: each is a
  statement about the next word, and `AUX_JS` asks exactly that of every row
  and prints the verdict beside it, with *Show: every row* for the hits. The
  lesson prose names rows the reader can find in the table (checked: every
  row cited as a chapter row is one — *you could not do better*, *we shall
  often meet*, *had already written*, *her brother is the cause*, *do not
  think me obstinate*, *she has been acting*).
- **The flattering number is never left alone.** Lesson 2's 85.5% is explained
  as a measure of the scan ("the number that tests the rule is the box that
  counts a verb with an ending after a modal: none"); lesson 1's one broken
  pair is read in context (*if I were not afraid of judging*) and set aside
  by name; lesson 5's five "old order" rows are read one by one and only one
  (*said not a word*) is 1813.
- **Quoted against computed is labelled every time.** Every whole-novel and
  play figure is introduced as "counted once over the whole novel, which no
  page can carry, and quoted here"; the `footer_lead` says what was counted
  where; the panel intros say the chapter is 1813 prose and name the two
  modern documents.
- **Misconceptions are the ESL ones.** *They walks* and *the -s means plural*;
  *she can goes*, *must to go*; *have* means own; *be* is the progressive's
  helper first; *I know not*, *did not be*, *did not regretted*; the
  progressive is the ordinary present. Each `why` on a quiz addresses the
  specific wrong model rather than restating the rule.
- **Prerequisites are honoured and cross-references are by title.** Only
  Tense Tables (the forms) and Irregular Verbs (*participle*) are assumed; the
  question inversion that Word Order (course 5) teaches is observed in lesson
  2 and explained inline, not assumed. Glossary terms (*pronoun*, *tense*,
  *bare*, *modal*, *adverb*, *participle*, *adjective*, *progressive*,
  *passive*, *preposition*, *contraction*) are each defined with `<dfn>` on
  the page that uses them; the pages carry 3–7 terms.

## What was wrong, verified, and fixed

- **`have-is-two-words`: the true split and the explanation of the gap.**
  All 37 rows were read against the chapter. The scan's 17 helping verbs are
  all perfects. Its 3 "something else" rows (*might have foreseen*, *has
  proved you right*, *had subsided*) are perfects with a participle the `pp`
  list lacks (`pp` holds *cared, permitted, experienced, lost* but not
  *foreseen, proved, subsided*). Its 17 "main verb" rows hold four perfects
  (*had by some accident been lost* — *by* is in the chapter's Moby noun list;
  *if he had at all cared* — *at* is; *had fortune permitted it*, *for had I
  really experienced* — inverted conditionals, *fortune* and *i* are nouns to
  Moby), eleven that mean own or hold (*I have nothing to say*, *if he had the
  fortune*, *the fortune he ought to have*, *you have sense*, *another
  favour*, *had as much to say*, *had no pleasure*, *having any such fears*,
  *such pleasant accounts*, *had such to send*, *must have something to live
  on*), the fixed phrase *had better*, and the causative *I would have you be
  on your guard*. By hand: 24 helping verbs, 11 own, 2 other; 24 + 13 = 37;
  24/37 = 64.9%. The lesson's `summary`, `key` (now "the scan: 17 of 37
  helping verb, 17 main" / "read by hand: 24 of 37 helping verb"),
  `concepts[2]` (retitled "A one-word scan can give a wrong idea"),
  `steps[0]` (a subject can move in behind *had*), `read_title`, `worked`
  (a sixth line, *word between*), `note`, `mistakes[0]`, `mistakes[1]`
  (retitled "Reading the scan's count as the answer"), quiz 3 (rewritten:
  where does the gap come from; correct index 1, so the lesson's positions
  are 2, 0, 1) and three body paragraphs now say this. The modern documents'
  residue is named too: one *have to* (*had to do*) and three perfects with
  unknown participles (*had violated*, *has diminished*, *has morphed*).
- **`after-a-modal-the-verb-is-bare`: the four "questions" and the three
  novel exceptions.** The four `axQ` rows are *how can I promise*, *will you
  come*, *that he should not I see* and *dearest Lizzy will I am*. The chapter
  reads "it will be better that he should not. I see the imprudence of it"
  and "My dearest Lizzy will, I am sure, be incapable". `panel_intro`,
  `worked` (a line *past a stop*), `worked.after`, `mistakes[2]`, quiz 3's
  `why` and the body paragraph "The eleven others" now say two and two. The
  seven "something else" rows were checked and the lesson's four kinds are
  right (*endeavour*, *consent* not in `base`; *could not but be*; *you
  certainly shall* with the verb left out; *no longer* ×2 and *at present*
  not in the adverb list). The body's example *you will certainly come* was
  not a chapter row and is replaced by *we shall often meet*, which is. The
  designer's `m_corpus.py` modal section, re-run with its formed rows printed,
  gives the three novel rows named in the verdict; the body's last paragraph
  names them and draws the right conclusion (no true exception), replacing
  "worth stated simply, with the three as its named exceptions". The modern
  residue row *changes in May. New subcounty* is a sentence boundary, as the
  lesson already said.
- **`be-is-mostly-a-main-verb`: two hidden progressives and two
  non-questions.** A regex scan of the chapter for a form of *be* followed
  within three words by an `-ing` word gave 18 matches; read in context, seven
  are progressives (the scan's five plus *was now fast approaching* and *was
  now rendering himself agreeable*), and the other eleven are *afraid of
  speaking*, *the means of making*, *most interesting* and the like. The 19
  "something else" rows were read: *I am sure* ×5, *I am certain*, *tempted*
  ×2, *deceived* ×2, *resented*, *quitted*, *likely*, *intimate*, *duped*,
  *seldom withheld*, *what had been rather than*, *what was Charlotte's
  first*, *herself to be though*; none has an `-ing` word next, as the lesson
  said, but the reason it gave was false. The three `axQ` rows are *how am I
  even to know* (a question), *as it is—you must* (a dash) and *were I
  distractedly in love* (the *were* form of lesson 1). `summary`, `key` (an
  eighth line, "read by hand: 7 of 137   5.1%"), `concepts[0]` (*be* before a
  participle is a helper only when the participle says what was done),
  `note`, `mistakes[0]`, quiz 4 (question and `why`) and the body (a new
  section "Two the scan filed as a noun phrase"; the pronoun paragraph) are
  corrected. One ESL misconception the lesson's own data refutes was missing
  and is added to the body: *I am agree*, *she is work here* — all 137 rows
  were read and none has a bare verb after *be*.
- **`which-of-the-twelve-boxes-get-used`: the 57, the 4, the 42 and the
  1.5%.** The lab's box table (read under node) gives modal simple 28, modal
  other 27, modal perfect 1, modal progressive 1 = 57. The 27 *modal, other*
  rows were read: 16 are *be* as the main verb after a modal (*I should be
  miserable*, *it will be as well*…), one *would have been his only*, one
  *would have you be*, two *do* as the main verb (*could not do better*, *will
  do my best*), two unknown bare verbs (*consent*, *endeavour*), four gaps
  (*should not. I see*, *certainly shall and*, *could no longer*, *should at
  present*) and *might have foreseen*. The 4 "passive" rows are *you are
  warned*, *you are satisfied*, *I was perfectly resolved*, *I am now
  convinced*. The *no verb found* rows include five *I cannot* (the kit does
  not read *cannot* as *can* + *not*) and *we all expect*, where *all* stops
  the scan, not a missing verb. The body's "Where the 216 land" is split into
  two paragraphs that say all this, the key line "passive" is now "be +
  participle", `concepts[0]`, `concepts[1]`, `summary`, `read_intro`,
  `mistakes[0]`, quiz 1 and quiz 4 say "the lab files" where the figure is the
  scan's, and a new section "The rare boxes, read by hand" gives 3 of 216
  (1.4%) and reconciles the five/seven `-ing` forms of the *be* lesson with
  the two/three here (this lab reads only pronoun subjects; *this is being*,
  *my aunt is going*, *Mrs. Hurst were going* and *his marriage was
  approaching* have none). The novel's progressive share is quoted as 143 of
  8,864, 1.6% (63 + 47 + 13 + 10 + 10 in `corpus.txt`).
- **`the-s-belongs-to-he-she-and-it`: 1,152 → 1,214, and what the 37 are.**
  `corpus.txt` "Agreement", Austen, he/she/it: is/has/does/was 1,081, -s form
  133, are/were/have/do 36, am 1; the "against the rule" list sums to 37 (*it
  were* 12, *she were* 6, *he were* 4, *she have* 4, *it are* 3, *he have* 3,
  *he do* 2, *it do* 2, *it am* 1). The novel was grepped for the non-*were*
  pairs: *could she have seen*, *what would she have said*, *could he have
  Colonel*, *believing it are*, *received it are*, *may it do them*; after
  *you*: *required of you is*, *cautioning you is*, *opinion of you was* — all
  an inverted helper or an object pronoun. `worked.after`, `note`, the body
  and the docstring now quote 1,214 of 1,251 and describe the 37 and the 5
  honestly. `worked.intro` said "the first two rows follow the rule, the third
  does not" of a five-line block whose third line follows it; now "the first
  three … the last". Quiz 4's correct option named only "a modal or a past
  form" as the reason 141 pairs are unscored; *to use it your father* and
  *she thus went* are neither, so it now reads "a past form, a modal or not a
  verb at all".
- **`where-not-goes`: *cannot*, a non-row, and an ambiguous share.** The
  `not` rule matches the token *not* and `/n't$/`; *cannot* (5 in the
  chapter) is one token and is not counted, while the body said "the text
  writes *cannot* and *do not* in full" as if both were among the 39. The
  body now says *cannot* is written as one word five times and is not among
  the 39. *I do not think* was cited as a chapter row; the chapter has *do not
  think me obstinate* and *I do not at all comprehend*, and the former is now
  cited. "86% after a helping verb, with 53.5% of them written as the
  contraction" read as 53.5% of the 86%; `corpus.txt` has *n't* 53.5% of all
  314 *not*s plus 32.5% after a full helper = 86.0%, and the sentence now
  says "more than half of all the play's *not*s, 53.5%, are the contraction".
  *Contraction* gets its `<dfn>` there.
- **Course home (`__init__.py`).** `outcomes[2]`, `[3]`, `[4]` titles and
  `assumes_long` lose their `<em>` (render.py passes titles through
  `esc_inline` and `assumes_long` through `esc`); the course home now has no
  literal `&lt;em&gt;` and its one `data-say` reads as words. `outcomes[2]`,
  `[3]` and `[5]` carry the hand counts beside the scan's; `outcomes[3]`'s
  "an a word" typo and `assumes_long`'s " ; " are fixed; `outcomes[5]`'s
  "after *he*, *she* and *I*" (the lab reads all seven pronouns) is "after
  each pronoun".

## Correctness of the English, verified and left alone

- Agreement: the lab's hit set (third-person form after *he/she/it*; *are,
  were, have, do* or a base form after *you/we/they*; *am, was, have, do* or
  a base form after *I*) is right, including *I was*. The designer's novel
  script counts *I was* (68) as "against the rule", a bug in `m_corpus.py`
  that touches no figure the lesson quotes (only the *he/she/it* and
  *you/we/they* rows are quoted).
- The nine modals are the standard closed class; *ought*, *need*, *dare* as
  marginal modals are named in lesson 2 and lesson 5 consistently (the lab
  does not count them; *need not* is current English). *Have to* as "neither
  the helping verb nor quite the main verb" is a fair A2 statement.
- Lesson 4's five jobs of *be* and the passive/adjective ambiguity (*was
  pleased*, *was satisfied*) are right and the lesson is careful not to
  resolve it. *This is being serious* is correctly described as *being* with
  an adjective (the progressive of *be*).
- Lesson 5's placement rule, *do*-support, *be* as the exception, *need not*,
  *not to*, and *not* before a noun phrase are right; *said not a word* is
  correctly the only 1813 order in the chapter. The sentence "*not* cannot
  follow a main verb in modern English" is a teaching simplification the
  lesson immediately qualifies with *need not* and *determined not to*.
- Lesson 6's box classification (`axChain`) matches `m_corpus.py`
  `classify_chain` as the plan requires; *she has been acting* is correctly
  present perfect progressive and the only three-part phrase; *we must have
  met* is correctly the chapter's one modal perfect; *will* and a bare verb
  is correctly described as where the table's future lives.
- All whole-novel and play figures quoted (2,738 modals and their shares;
  2,339 *have*, 59.5 / 32.1 / 1.1; the play's 50.1 / 42.0 / 2.9; 5,858 *be*
  and its seven shares, the play's 5.6%; 1,440 *not*, 78.8 / 6.3, the play's
  86 and 53.5; 8,864 pronoun subjects and the box shares; 7 and 19 question
  tags) match `corpus.txt` exactly, except the two corrected above (1,152;
  1.5%).
- Modern-document figures in prose (14 of 14; 16 of 17, 94.1%; 16 of 23,
  69.6%, 3 main; 2 of 36, 5.6%, 5 participles; 8 of 10, 80.0%,
  *acknowledged not every*; 34 pronoun subjects, 14 simple 41.2%, 3 perfect
  8.8%, 0 progressive) match the `_AX_MODERN` pins and the node run.

## Prerequisite order

Checked backwards against `docs/english-v2/COURSES.json`. The course assumes
Tense Tables (the base, `-ing` and "form after *have*" of "Five Forms Make
Twelve"; the `-s` rule) and Irregular Verbs (*participle*, which lesson 3
defines again as the plan asks). Nothing is assumed from Nouns and Articles,
Word Order, Small Words, Spelling to Sound, Word Stress, Listening or
Vocabulary, all later in the path. Lesson 5 names *n't* and *contraction*
(Listening, course 9) and defines the term; lesson 2 observes the question
inversion that Word Order (course 5) later scores, and explains it in one
sentence rather than assuming it. Lesson 4 and lesson 6 send the reader back
to "The -s Belongs to He, She and It" and "After a Modal, the Verb Is Bare" by
title, inside this course.

## Cognitive load

One hard idea per lesson: agreement; the bare form; two *have*s; what follows
*be*; *not* and *do*; the boxes. Lesson 5 carries *not*-placement and
*do*-support together, which is the plan's design and the right one (the
second exists because of the first; `concepts` present them in the order a
sentence uses them). Lesson 6 is the heavy page — twelve boxes plus five
extra groups and now two hand-read corrections — and sits at 16 of the 18
body blocks; the load is held by the lab's own box table, by the worked
example's six one-line rows, and by the `note` saying the boxes are a way to
build, not a ranking. Lesson 3's new material (four more misfiled rows)
replaced a false explanation rather than adding to the page; it is at 10 body
blocks.

## Worked-example progression and retrieval practice

Each lesson: four `steps` → a `worked` block on chapter rows → the lab with
the lesson's preset selected and every row printed → three or four quiz
items. Lesson 3's worked block now runs helping verb → main verb → unknown
participle → word between, which is the order of the `steps`. Lesson 6's runs
the six boxes a reader meets most. Quiz positions are 2 1 3 0 / 1 2 3 0 /
2 0 1 / 3 0 1 2 / 3 0 1 2 / 0 2 1 3, four distinct choices each, and each
distractor was argued for and refused (lesson 3's new quiz 3: "the chapter is
a small sample" is true and is not where the gap comes from, which is the
point of the item; lesson 1's quiz 1 has one grammatical sentence; lesson 5's
quiz 3 has one *old order* row among the five).

## Misconceptions

Named and corrected, each tied to a count on the page: the `-s` is a plural
(lesson 1 `mistakes[0]`, 0 pairs after *you/we/they* take it); *he have*,
*she do not* (`[1]`); one broken row makes a weak rule (`[2]`); *she can
goes* (lesson 2, 0 of 76 and 0 true exceptions in 2,738); *must to go*
(`[1]`); 85.5% as a failure rate (`[2]`); *have* means own (lesson 3, 24 of
37 do not); the scan's count as the answer (`[1]`, rewritten); a fixed phrase
read as its parts (`[2]`); *be* is the progressive's helper first (lesson 4,
7 of 137 by hand); every participle is a passive (`[1]`); rare means skip
(`[2]`); *I know not* (lesson 5, 1 row in 39); *did not be* (`[1]`); *did not
regretted* (`[2]`); the progressive is the ordinary present (lesson 6, 3 of
216 by hand, 143 of 8,864 in the novel); twelve equal boxes (`[1]`); *no verb
found* as the lab's failure (`[2]`). **Added this pass**: *I am agree*, *she
is work here* (lesson 4 body), the commonest misuse of *be* by learners
whose first language marks the present with a copula, refuted by the 137
rows. **Not addressed, and not computable from printed words**: *I have 20
years* for age, and *since/for* with the perfect; both are meaning, and §G of
the plan excludes tense choice.

## Listen

Every `key` and `worked.lines` block on the seven rendered pages was read
off `data-say`. Lines that read wrongly by the rules carry forms in
`content/spoken/english_c5_helping_verbs.py` (a line-initial *be* is spelled
"b e"; `-ing` is "negative i n g"): the five *be +* key lines, the two `-ing`
lines, the two *no helping verb? add do* lines, and the new `be + participle
4 of 216` key line of lesson 6, read "be plus a participle, 4 of 216". Every
other line, including the new *a question / past a stop*, *unknown word /
word between*, *the scan: … / read by hand: …* lines, reads as written ("read
by hand, 7 of 137, 5.1 percent"). The course home's `<em>` titles no longer
produce a math island. The speech-island detector finds no sound or stress
mark in the course's prose. The per-course file's keys are all present as
runs, and none appears in another Subject.

## Band and weight

`scripts/bandcheck.py --report` on the final preview: course home 99.2%,
`the-s-belongs-to-he-she-and-it` 99.7% (4 defined),
`after-a-modal-the-verb-is-bare` 99.5% (6), `have-is-two-words` 98.9% (3),
`be-is-mostly-a-main-verb` 98.8% (7), `where-not-goes` 99.5% (4),
`which-of-the-twelve-boxes-get-used` 99.3% (7). The off-list words on the two
lowest pages are the chapter's own residue quoted (*rendering*, *foreseen*,
*subsided*, *tempted*, *deceived*, *agreeable*), which the contract requires
the page to print. Gzipped: 16.9 / 45.5 / 45.4 / 45.5 / 45.5 / 45.1 / 45.6
KB, under the 48 KB kit budget and the 67 KB ceiling. The rendered pages
carry no numbered cross-reference.

## Changes made

- `__init__.py`: `assumes_long` (punctuation; no `<em>`); `outcomes[2]`,
  `[3]`, `[4]` titles without `<em>`; `outcomes[2]`, `[3]`, `[5]` wording and
  hand counts.
- `part_a.py`: docstring (figures, hand reads, provenance); lesson 1
  `worked.intro`, `worked.after`, `note`, body (1,214 / 1,251; the 37 and the
  5), quiz 4; lesson 2 `panel_intro`, `worked` (six lines), `worked.after`,
  `mistakes[2]`, quiz 3 `why`, body ("we shall often meet"; "The eleven
  others"; the three novel rows named); lesson 3 `summary`, `key`,
  `concepts[2]`, `steps[0]`, `read_title`, `read_intro`, `worked` (six
  lines), `worked.after`, `note`, `mistakes[0]`, `mistakes[1]`, quiz 3, body
  ("The seven the scan missed", "A small count and a large one", "Two phrases
  the scan reads as their parts").
- `part_b.py`: docstring; lesson 4 `summary`, `key` (eight lines),
  `concepts[0]`, `note`, `mistakes[0]`, quiz 4, body (the pronoun rows; *I am
  agree*; "Two the scan filed as a noun phrase"); lesson 5 body (*cannot*;
  *do not think me obstinate*; the play's 53.5%; `<dfn>contraction</dfn>`);
  lesson 6 `summary`, `key` ("be + participle"), `concepts[0]`, `concepts[1]`,
  `read_intro`, `mistakes[0]`, quiz 1, quiz 4, body ("Where the 216 land" in
  two paragraphs; "The rare boxes, read by hand"; "Why the group for the rest
  matters"; 143 of 8,864, 1.6%).
- `content/spoken/english_c5_helping_verbs.py`: docstring; one new form
  (`be + participle             4 of 216`).
- Verified after: `preview_subject.py english --course helping-verbs` OK (6
  labs executed and swept, 6 pinned, 0 failing); `TestLessonDataMatchesTheRenderer`
  passes; shapes 3 / 3 / 4 / 3–4 / key 6–8 / body 10–16 / worked 5–6; every
  key line ≤ 46 characters, every worked line ≤ 60; band and weight as above.

## How the hand counts were made (so they can be made again)

Under node, with the repository's own code: `SCAN_JS + AUX_JS` from
`scripts/mathpath/labs/english_core.py`, `AX_DATA = _payload(LONG_PASSAGE,
"passage", "classes")` and `MODERN = MODERN_DATA` from `english.py`;
`axRun(rule, text, AX_DATA)` for each of the six rules on the chapter and on
the joined modern texts; every row printed with its verdict and read against
`long_passage.json`'s `passage` with ninety characters of context. The
`-ing` scan: `\b(am|is|are|was|were|be|been|being)\b(\s+\S+){0,3}?\s+\S+ing\b`
over the chapter, 18 matches, each read. The novel contexts: the Gutenberg
text sliced on the novel's first and last sentence with `[Illustration…]`
removed, grepped for each pair in `corpus.txt`'s "against the rule" list. The
three modal rows: `m_corpus.py`'s modal section run with `PYTHONPATH` set to
`docs/english-v2/measure` and `toks[i-4:i+5]` appended for each formed row.

## Remaining issues, for whoever next owns this course, the kit or the plan

- **`docs/english-v2/PLAN.md` §C 3.1 says 1,152 third-person forms after
  *he/she/it*; `measure/out/corpus.txt` gives 1,081 + 133 = 1,214.** The
  lesson quotes 1,214 of 1,251. §C 3.6's "all progressives together 1.5%" is
  the sum of five rounded shares; the counts sum to 143 of 8,864 = 1.6%, which
  the lesson quotes. Both are the orchestrator's to correct in the plan.
- **`m_corpus.py` agreement counts *I was* as against the rule** (68 in the
  novel); the "against the rule" list in `corpus.txt` is therefore
  misleading, though no quoted figure depends on it.
- **Kit (`auxchain`), in order of what it cost this course.** (1) The
  chapter's Moby-derived `noun` class holds *i, by, at, as, all, well, long,
  better, fast, rendering*, so `have` files inverted conditionals and
  phrase-between perfects as main verbs, `axQ` can never fire for *have* (*i*
  is a noun first), and `be` files two progressives as noun phrases; a
  stoplist of function words on the noun class, and "-ing in the chapter and
  not noun-only" for the `ing` class, would move the page's 17 and 5 towards
  the hand counts. (2) The scan ignores punctuation, so *he should not. I
  see*, *will, I am sure, be*, *changes in May. New* and the three novel
  "formed" rows are all one artefact; stopping a chain at `.`, `?`, `!`, `;`
  or `—` would remove it. (3) *cannot* is not read as *can* + *not* by `not`,
  `boxes` or `modal` (five rows in the chapter land in *no verb found*).
  (4) The `boxes` label *modal, other* holds 27 of the chapter's 57; a class
  "modal + *be* as the main verb" would name 16 of them. (5) The `modal`
  verdict "a pronoun next: a question" is wrong for a sentence boundary;
  "a pronoun next" alone would be honest. (6) `_AX_LIMITS["agree"]` cites
  *put it down*, which is not in the chapter; *to use it your father* is.
  (7) The `adj` class is Moby adjective-only, so *sure*, *certain*, *likely*
  fall to *something else*; the lesson says so.
- **Renderer.** `course["outcomes"][i][0]` and `course["assumes_long"]` are
  escaped, so `<em>` prints literally; `TestLessonDataMatchesTheRenderer`'s
  literal-markup check covers lesson fields only. Extending it to course
  fields would have caught this before a reviewer did.
- **Speech.** `tests/test_speech.py` `test_no_spoken_form_for_math_that_is_gone`
  fails on this branch for two Tense Tables runs still in
  `content/spoken/english.py` (`-s 1209 of 1210 right 99.92%`, `-ing 1202
  of 1210 right 99.34%`), which `english_c1_tense_tables.py`'s docstring
  already asks the merge to delete; this course's forms are not yet merged
  into `english.py` (the preview reads every file in `content/spoken/`, so the
  pages are right; the test reads only `english.py`).
- ~~`__init__.py` still writes `"number": 3`~~ — resolved at wiring: course
  numbers now come from the path's numbering loop.
