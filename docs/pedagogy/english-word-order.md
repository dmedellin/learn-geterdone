# Pedagogy assessment — Word Order (english, course 5 of the v2 path)

Fresh assessment of 2026-10-10 for the second version of the English Subject
(`docs/english-v2/PLAN.md` §C Course 5; `COURSES.json` position 5, package
`c3_word_order`). It replaces the 2026-10-08 assessment of the three-lesson
course, which is summarised in one paragraph below so its findings are not
lost.

Formed from the four lesson dicts in `content/english/c3_word_order/`
(`part_a.py`, `part_b.py`, `part_c.py`), the course dict in `__init__.py`, the
three lab modes they call (`svo`, `adverbs`, `questions` in
`scripts/mathpath/labs/english.py`, with the verdict code in
`english_core.py`), the four data files the labs inline
(`content/english/data/wordorder_passage.json`, `adverb_concordance.json`,
`question_concordance.json` re-cut at sentence boundaries,
`wilde_questions.json`) and the two modern documents, and the pages as
`scripts/preview_subject.py english --course word-order` renders them. Every
tile was read off the built page with `node scripts/labcheck.js --observe`,
and every row of every table was read off the built page with a small node
harness over `labcheck.js`'s DOM shim (so the hand sorts below are of the
verdicts the shipped code prints, not of the data files). The course may
assume Tense Tables, Irregular Verbs and Helping Verbs (courses 1–3 in
`COURSES.json`) and nothing else. All four lessons were read before any was
changed.

Lessons, in course order: `who-does-what-to-whom`, `where-the-adverb-goes`,
`asking-a-question`, `how-people-really-ask`.

**The 2026-10-08 pass, in one paragraph.** It found the course promising
computation and delivering quotation (whole-novel figures stated as if
counted), a panel describing tiles that did not exist, a course key stating
91.9% when the tile read 90.0%, every quiz keyed to its first choice, a false
claim about *her*, a false claim about Spanish noun endings, *helping verb*
undefined, and `asking-a-question` scored on lines cut mid-sentence. All of
those are fixed and stay fixed; this pass checked each against the rebuilt
pages. The two it recorded as upstream work are done in v2: the question
concordance is re-cut at sentence boundaries (90 lines, none cut mid-word)
and the four-way sort has tiles.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Name
  the two forms of five pronouns, state the rule, read its score off the
  passage and name each kind of apparent exception (`who-does-what-to-whom`);
  state the three middle places, read how often they held on 120 lines and
  name what fell outside (`where-the-adverb-goes`); put a helping verb before
  the subject, add *do*, read the score off 90 questions, name the kinds the
  rule did not catch, and say which figures are counted and which quoted
  (`asking-a-question`); read the score off 256 questions from a play, name
  the five kinds the count names and the one it cannot, sort a new line by
  its first words, and say why a low score is not a reason to drop the rule
  (`how-people-really-ask`). None is "understand".
- **One method, four times, in the right order.** The pronoun rule first
  because it is strongest (72 of 80, 90.0%) and its residue is three nameable
  things; the adverb rule second because it is weaker (85 of 120, 70.8%) and
  its residue is mixed; the question rule third because it covers a little
  over half (52 of 90, 57.8%) and the lesson is the other half; the same rule
  on a play fourth because it covers a third (89 of 256, 34.8%) and the point
  is that the residue is what people say. The fourth lesson is the one the
  three-lesson course lacked: without it, "57.8% on 1813 prose" left a learner
  with no idea what questions look like when people talk.
- **The residue is content.** Every miss list is sorted into kinds with a
  reason the reader can use: the speech tag as a story habit, not an order to
  copy; the lexicon gap as a limit of the tool; *never in my life* and *as
  soon as* as phrases the rule never meant to cover; *How old are you?* as a
  limit of a count that reads one word after the wh-word; *A hand-bag?* as a
  thing repeated back, which the talk around it gives a meaning.
- **The misconceptions are the real ones for the stated reader** (a speaker
  of a free-order, verb-final or particle-marking language) and each is
  refuted with the specific case: *said he* as a pattern to copy; *they both
  knew* as a break in the rule; *she knew always*; the adverb between the verb
  and its object; forgetting that *be* works differently; asking by tone
  alone; *do you can go?*; reading 57.8% or 34.8% as a verdict on the rule;
  copying *A hand-bag?* without the talk around it; counting a question word
  and a phrase as a break in the rule. The §C misconception for lesson 4 is
  `mistakes[0]`.
- **Every row is printed and every figure in prose is on a tile or marked
  quoted.** The passage, the 120 lines, the 90 questions and the 256
  questions are on the page with a verdict beside each; the `how_to` tells the
  reader to check a row and disagree with it.
- **The prerequisite chain is now explicit by title.** Lesson 1 names Helping
  Verbs where the 25 helping verbs are introduced; lesson 2 says "as Helping
  Verbs calls them" and no longer defines the term itself; lesson 3 says the
  helping verbs are "the ones that Helping Verbs lists", calls the form after
  *do* the bare form "as Helping Verbs calls it", and now says *do* is "the
  same *do* that arrives to carry *not* in Helping Verbs"; lesson 4 cites
  Helping Verbs on *dare*.

## What the course taught badly, or wrongly, before this pass

1. **A linguistic error about Mandarin and Japanese** (`asking-a-question`,
   body, "The rule"). The page said the rule "matters most to a speaker of a
   language that asks by tone, such as Mandarin or Japanese". Neither asks by
   tone: Mandarin marks a yes-no question with the sentence-final particle
   *ma* (or an A-not-A form), Japanese with the particle *ka*. Mandarin's
   tones are lexical. The sentence now says "asks with a small word at the
   end of the sentence, such as Mandarin or Japanese, or by the voice alone",
   which is what concept 1 of the same lesson already said correctly.
2. **The worked block of `how-people-really-ask` was titled "Four lines,
   four kinds" and showed three.** Two of its four lines (*Finished what, may
   I ask?* and *A hand-bag?*) sit in the same box, *something else*, and the
   lab's two most populous residue boxes after the joining word, *a pronoun
   first* (27) and *a wh-word with no helping verb after it* (24), had one
   line and no line respectively; *no verb at all* (14) had none. A worked
   example that is meant to fade the sort procedure of the steps should show
   one line per box, in the order the lab tries them. It is now six lines,
   six kinds: a joining word, a wh-word with no helper straight after it (the
   *How old are you?* limit), a word of address, a pronoun first, no verb at
   all (*Your guardian?*) and something else (*A hand-bag?*, kept because its
   reason — *hand* and *bag* are on the verb lists — is the lesson's best
   illustration of what "no verb at all" means to the count). Each verdict
   was confirmed on the built table.
3. **Lesson 3 contradicted its own tile.** The body said *But why all this
   secrecy?* and *What, none of you?* have no verb at all; the tile called
   *no verb at all* reads 0. Nothing on the page said that the lab sorts by
   the first word first, so a verbless line beginning with *but* or *what* is
   counted under the joining word or the question word. Both panels now say
   "the boxes are tried in that order, so a line is counted once, under the
   first that fits", and lesson 3 has a paragraph saying why its box reads 0
   and that on the play it fills.
4. **Lesson 3 overstated the re-cut.** Concept 3 said "each line starts where
   its own sentence starts, so its first word is the question's first word".
   Thirteen of the 90 lines begin in lower case because they begin where
   quoted speech resumes after a speech tag, and in one of them, *"But what,"
   said she, after a pause, "can have been his motive?"*, the cut falls after
   the tag and the lab counts the line from *can*, as a hit. The claim is now
   "in all but one line", with that line named. (The verdict is still right
   for the rule — the question is a wh-word then a helping verb — but the
   first word is not the question's first word, and the lesson said it was.)
5. **Lesson 3 mislabelled one of its nine *something else* lines.** "The
   other six are long sentences that end in a question, such as *Your
   father's estate is entailed on Mr. Collins, I think?*" — that example is
   not a long sentence ending in a question; it is a statement with a
   question mark whose first word is a noun, which is exactly why the pronoun
   box could not catch it. Now five long sentences and one noun-first
   statement, in the worked block and the body.
6. **Lesson 4 described *How dare you?* as if *dare* were an ordinary verb.**
   "*How dare you?* puts the verb straight after the question word", and the
   quiz `why` called it "a question word with no helping verb after it". In
   *How dare you?* *dare* is the inverted auxiliary (it takes no *do*, it
   precedes the subject), and Helping Verbs itself says *ought*, *need* and
   *dare* "work much the same way" as the nine modals while its lab does not
   count them. The lab's `QU_AUX` list carries the nine modals and not
   *dare*, so the verdict is a limit of the count, and the lesson now says
   so: "Helping Verbs says *dare* works much like *can* and *must*, and the
   count does not list it with them."
7. **Lesson 4's residue was named loosely where it could be named exactly.**
   "Some of the 24 are like this, and some are not"; "some are statements
   with a tag…, some begin with a noun…, some begin with a phrase…". Read off
   the built table: of the 24 wh-lines, twelve follow the rule after a short
   phrase, three have the wh-word as subject (*What brings you up to town?*,
   *What else should bring one anywhere?*, *Which of us should tell them?*),
   eight have no verb but begin with a wh-word (*Why cucumber sandwiches?*),
   one is *How dare you?*. Of the 47 *something else* lines: nine statements
   with a tag, twelve noun- or phrase-first statements with a question mark,
   nine with a lead-in word the count does not list (*yes*, *now*, *really*,
   *of course*, *by the way*), five phrase-first questions that then follow
   the rule, eleven short echoes filed here because a word in each is on the
   verb lists (*A hand-bag?*, *The fools?*, *Finished what, may I ask?*), and
   one, *Algy, could you wait for me till I was thirty-five?*, whose name the
   cast list spells *Algernon*. Of the 27 pronoun-first lines, nine carry a
   tag. Of the 35 joining-word lines, two begin with *for* as a preposition
   (*For the last three months?*), which the count lists as a joining word.
   Of the 14 *no verb at all*, one (*Never forgive me?*) has a verb the
   printed lists do not hold. All of this is now stated, with one example per
   kind, as the voice guide requires ("exceptions alone is a defect").
8. **Lesson 2's page residue was half-sorted.** "A few are at the end…, or at
   the start…" left about ten of the 29 *something else* lines unaccounted
   for. Read off the table: five verbs the list does not hold, three *as soon
   as*, five before an adjective, four at the end of their clause, five at the
   start of one, six with a word after the adverb that the lab's seven-word
   preposition list does not hold (*often without*, *so soon after*, *not
   often much*) or in a phrase of their own (*how soon*, *soon afterwards*),
   and one *Sometimes.* alone: 29. The lesson now gives all seven kinds, and
   says the preposition list is seven words, since a reader who sees *often
   without* under *something else* would otherwise think the count is wrong.
9. **Two course-home sentences were false about the labs.** `assumes_long`
   said "the adverb and question rules move a helping verb"; the adverb rule
   moves nothing, it places a word after one. `not_covered` on question tags
   said "the lessons print the lines that carry one and do not score them";
   the questions lab scores every printed line by its first words, tag or
   not (*It's very pretty, isn't it?* is a scored *something else*). Both
   corrected.
10. **Two glossary terms used without definition on their first page.**
    *preposition* and *clause* appear in `where-the-adverb-goes` (and
    *clause* on the course home) with no `<dfn>`; the plan says to define
    again where used. Both are now defined at first use in concept 3, with a
    gloss a reader at A2 can use. `how-people-really-ask` fell below the band
    (97.8%) when its residue was named exactly; defining *pronoun* and *tag*
    on that page, as lesson 1 defines *pronoun*, and swapping one example
    (*Cake or bread and butter?* for *The fools?*) brought it to 98.5%.
11. **Step 2 of lesson 1 stated the noun order as unconditional.** "With
    nouns, the one before the verb is the subject" is false of a passive
    (*the man was bitten by the dog*), which Helping Verbs has by then
    taught as "Be Is Mostly a Main Verb". Now "in a plain statement with
    nouns".

## What it claims to teach but does not, and where a learner gets stuck

- **The passage's own residue is tiny.** Eight misses out of 80 cannot teach
  the shape of the residue on their own, which is why the quoted whole-novel
  split (63/16/15/6) is kept beside the page's 5/2/1. The lesson says which
  is which every time; a reader who wants to check the 63% cannot, and the
  sentence says so.
- **The `svo` tile *word order broken*** counts the speech tag; the lesson
  explains that the verb does come before its pronoun and that the course
  still calls it a habit, not an error. A kit relabel ("verb before its
  pronoun: a speech tag") would remove the need for the explanation. Not
  this pass's file.
- **The adverbs tile *something else between*** holds lines where nothing is
  "between" (*Sometimes.* alone, *and me never*). The lesson sorts them in
  prose; the label is the kit's.
- **The questions count reads one or two words.** The lesson says so three
  times and builds a misconception on it. What it cannot do, and says it
  cannot: tell *How old are you?* from *Why cucumber sandwiches?*; see a
  pronoun with *'s* or *'ll* stuck to it (*It's very pretty, isn't it?*,
  *You'll never break off our engagement again, Cecily?* are both
  *something else*); hear a rising voice.
- **Cognitive load.** Lesson 1 carries two pronoun sets, two scales of count
  and a tile whose name sits against the thesis; the key holds the page
  figure, the quoted figure and the one broken case in three lines, in that
  order. Lesson 4 carries six boxes plus the count's limits; the steps give
  the sort as four decisions in the order the lab makes them, the worked
  block gives one line per box in that order, and the body gives the hand
  sort of what is left. Neither needs splitting; the URL space is fixed and
  each carries one rule.
- **Worked-example progression.** Each lesson runs concepts → steps (the
  procedure) → lab (every row printed, the reader free to disagree) → worked
  residue (the faded example: how the misses sort, one printed line per kind)
  → mistakes → quiz. Lesson 4's worked block now matches its steps and its
  tiles one for one, which it did not.
- **Retrieval practice.** Each `why` answers the specific error: "16, which
  is 42.1%" is explained as the joining-word count and its share of the
  misses; "There are exactly none, proved over every case" is answered with
  what was and was not read; "Words in the wrong place" with the tool's
  limit; "The line has no verb at all" (for *How old are you?*) with what the
  count read.

## Prerequisite order

Checked backwards across the path order in `COURSES.json`. *Have*, *be*,
*will* and the modals as helping verbs, the bare form after *do*, and *do*
arriving to carry *not*: Helping Verbs (course 3). The verb forms the scans
match against: Tense Tables and Irregular Verbs (courses 1–2); the labs carry
their own lists of the forms the printed text contains, so nothing is assumed
about recall. Nouns and Articles (course 4) is earlier and not assumed.
Within the course: *pronoun*, *subject*, *verb*, *modifier*, *speech tag*
defined in lesson 1; *adverb*, *preposition*, *clause* in lesson 2; *pronoun*
and *tag* again in lesson 4. Nothing in this course is needed by a course
before it; Listening (course 9) and Vocabulary and Reading (course 10) do not
assume it. No violation sits in an earlier course.

## Accuracy of the English

Checked claim by claim against the data and the built tables.

- Subject and object forms of *I, he, she, we, they*; *you* and *it*
  invariant; *her* both object and possessive: right. "In careful English"
  hedges *me and him went* and *it is I*: right for this reader.
- Spanish personal *a* and verb agreement, Russian case endings, Japanese
  and Korean particles after the noun: right.
- Quotation-tag inversion (*said he*) confined to reported speech, not a
  productive order: right.
- Mid-position rule — before the main verb, after the first auxiliary, after
  *be* as main verb — the standard account; *always* and *never* do not
  normally stand last, *often* and *sometimes* may: right. *Still*, *already*,
  *soon* as time rather than frequency adverbs taking the same places: right.
- Subject–auxiliary inversion, *do*-support with the bare form, wh-fronting,
  no inversion when the wh-word is the subject (*who went?*, *What brings you
  up to town?*): right. *What say you?* as the older pattern without *do*:
  right. Declarative questions by intonation carrying a checking or surprised
  colour: right.
- Mandarin and Japanese question particles at the end of the clause: right
  now (item 1 above); "by the voice alone" covers the languages that do ask
  by intonation. Spanish and Russian inverting with no auxiliary: right.
- *Dare* in *How dare you?* as a modal-like auxiliary the count does not
  list: right now (item 6).
- Figures the prose states, against the tiles (`--observe`, 2026-10-10):

| lab | preset | tile | page prints | prose states |
|---|---|---|---|---|
| `svo` | subject | soHit / soPct / soBroken / soMod | 72 of 80 / 90.0% / 1 / 5 | 72 of 80, 90.0%, 1 speech tag, 5 modifier, 2 not in list |
| `svo` | subject | soHereK / soModK / soTimes | 84.7 (80 in 944) / 13.9 (24 in 1,723) / 6.1 | 84.7, 13.9, 6.1 |
| `svo` | object | soHit / soPct / soHereK / soModK / soTimes | 16 of 18 / 88.9% / 19.1 / 1.7 / 11.0 | 19.1 against 1.7, 11.0 |
| `adverbs` | all | avHit / avPct / avPrep / avOther / avModN / avModK | 85 of 120 / 70.8% / 6 / 29 / 2 in 1,723 words / 1.2 | all stated |
| `adverbs` | always / never / sometimes | avHit | 15 of 16 / 14 of 16 / 7 of 16 | stated |
| `questions` | austen | quHit / quPct / quConn / quConnPct / quWh / quAddr / quStmt / quFrag / quOther / quModQ / quModW | 52 of 90 / 57.8% / 16 / 16 of 38, 42.1% / 7 / 2 / 4 / 0 / 9 / 0 / 1,723 | all stated, including the 0 |
| `questions` | wilde | same | 89 of 256 / 34.8% / 35 / 35 of 167, 21.0% / 24 / 20 / 27 / 14 / 47 / 0 / 1,723 | all stated |

Hand sorts within a box (lesson 2's 5/3/5/4/5/6/1 = 29; lesson 3's 16 =
13 + 3, 7 = 3 + 1 + 1 + 1 + 1, 4 = 3 + 1, 9 = 2 + 1 + 5 + 1; lesson 4's 24 =
12 + 3 + 8 + 1, 47 = 9 + 12 + 9 + 5 + 11 + 1, 27 with 9 tags, 35 with 2
*for*) were made over the verdict column of the built table and each sums to
its tile. Counts of things in the data (141 verb forms, 25 helping verbs, 249
forms, 8 adverbs with rows, 46 *you* and *it*, 13 *her*, three *I beg your
pardon?*, the seven-word preposition list, the cast list without *Algy*) were
checked against the JSON and the kit source.

## Quoted versus computed

Every whole-text figure is introduced as quoted in the sentence that states
it, every time: 5,990 and 88.7%, 63/16/15/6 and 88%, 677 or so, 122,396
words (lesson 1); 577, 472, 81.8%, 51/23/10/7/14, about 4.7 per thousand
(lesson 2); 55.4% and 45% (lesson 3); 13.1 and 3.9 question marks per
thousand words (lesson 4, and the course home); 7 and 19 question tags
(course home). The first three sets rest on `docs/ENGLISH-SUBJECT.md` §5 and
have not been re-run since 2026-10-06; the last two are (m) in
`docs/english-v2/measure/out/corpus.txt`. Nothing on a tile is called quoted
and nothing quoted is placed where a tile could be read as its source.

## Quizzes

Sixteen questions, one defensible answer each; the distractors were argued
for and none survived. Keyed positions `[2, 0, 3, 1]`, `[1, 3, 0, 2]`,
`[3, 1, 2, 0]`, `[2, 0, 3, 1]`: each lesson spreads over all four slots, and
no slot dominates across the course (4/4/4/4). Two `why`s were corrected
(bare form; *dare*).

## Listen

Every `data-say` on the four built pages and the course home was read. Key
lines read as intended ("subject, I, he, she, we, they"; "before the main
verb, she always knew"; "he or him, she or her, they or them"). The four
arrow lines of `asking-a-question` keep their forms in
`content/spoken/english.py` ("you know becomes do you know"). The default
rules put a space before a question mark at the end of a quoted play line
("marry me ?"), which a voice treats as punctuation; no form is needed. The
one line that misreads, *A hand-bag?* (the hyphen made *bag* be spelt out),
keeps its form in `content/spoken/english_c3_word_order.py`; the new worked
lines of lesson 4 were read aloud and need none. `tests/test_speech.py` has
one failure on the English path, and it is Tense Tables' (`-ing 1202 of 1210
right 99.34%`, `-s 1209 of 1210 right 99.92%` have forms but no run), not
this course's.

## The band

`scripts/bandcheck.py --report` on the rebuilt preview: course home 98.6%
(1 defined), `who-does-what-to-whom` 98.9% (7), `where-the-adverb-goes`
98.9% (3), `asking-a-question` 98.5% (0), `how-people-really-ask` 98.5% (2).
Page weight 37.1–40.0 KB gzipped against the 67 KB ceiling.

## Changes made

- `__init__.py`: `assumes_long` (the adverb rule places, the question rule
  moves); `not_covered[1]` (a tag line is sorted by its first words like any
  other; no lesson scores the tag itself).
- `part_a.py`: step 2, "In a plain statement with nouns".
- `part_b.py`: concept 3 defines `<dfn>clause</dfn>` and
  `<dfn>preposition</dfn>` and sorts the misses "two ways"; the panel names
  the seven-word preposition list; `worked.after[2]` and the body's "What the
  35 misses on this page are" give all seven kinds of the 29 with one example
  each (5/3/5/4/5/6/1).
- `part_c.py`, `asking-a-question`: concept 1 ties *do* to Helping Verbs;
  concept 3 states the one line cut after a speech tag; step 2 and quiz 1 say
  "bare form, as Helping Verbs calls it"; the panel states the sort order
  with *But why all this secrecy?* as the example; `worked.after[3]` and the
  body's *something else* item split 5 long sentences from the noun-first
  statement; the wh item names all seven; a new paragraph explains the 0 in
  *no verb at all*; the Mandarin/Japanese sentence is corrected.
- `part_c.py`, `how-people-really-ask`: the summary defines
  `<dfn>pronoun</dfn>`; the panel states the sort order; the worked block is
  "Six lines, six kinds", one per box, with new `after` paragraphs; the five
  body items give the hand sort of each box (*for* and *then* among the
  joining words, nine tags among the pronoun lines, 12/3/8/1 among the
  wh-lines with *dare* explained, *oh*/*well*/*my dear fellow* among the
  address words, *Never forgive me?* among the verbless); the *something
  else* paragraph gives 9/12/9/5/11/1 with one example each; "What the count
  cannot tell" adds *it's* and *you'll*; `mistakes[2]` and quiz 2's `why`
  corrected; `<dfn>tag</dfn>` at first use.
- `content/spoken/english_c3_word_order.py`: docstring records the re-read
  and why the question-mark spacing needs no form; the one form is unchanged.
- Module docstring of `part_c.py` records where the row-level claims come
  from.

## Remaining issues

- **`docs/english-v2/PLAN.md` §C 5.4 says 167 questions from the play; the
  shipped data has 256.** The designer's cut (`measure/m_corpus.py`) and the
  committed `scripts/wordlists/concordance.py` cut differently (the shipped
  one keeps every question of two words or more from where its sentence or
  the speech starts, with a stage direction starting a new sentence). By the
  plan's own rule the page wins and the plan is corrected; that file is the
  orchestrator's. The lesson states 256 and 89 of 256, which is what the
  page prints.
- **Four kit limits the lessons now explain rather than fix** (`@lab`
  work, not this pass's files): `QU_CONN` takes *for* and *then* as joining
  words; `QU_PRON` does not match *it's* or *you'll*; the cast list lacks
  *Algy*; `QU_AUX` lacks *dare*, *need*, *ought*. Each moves a handful of
  lines between boxes and would move the pinned tiles.
- **The Austen lab's `Lab.title`**, "Ninety real questions, and a rule that
  does not cover them", overstates a 57.8% rule; it is kit text in
  `english.py`.
- **`content/english/__init__.py`** still says "Four courses" in
  `sequence_intro` and "Word Order comes third" in `why_order`; path-level
  text, not this course's file, and presumably the wiring agent's.
- **`tests/content_preservation.json`** pins clauses this course no longer
  carries (it still quotes "48, which is 53.3%"); the orchestrator regenerates
  those entries before committing, as the 2026-10-08 note said.
- **The speech test failure in Tense Tables** (two `-ing`/`-s` forms with no
  run) is another agent's, in a file this pass did not touch.
- **The whole-novel quoted figures** (5,990, 88.7%, 63/16/15/6, 88%; 577,
  81.8%, 51/23/10/7/14; 55.4%, 45%) still rest on `docs/ENGLISH-SUBJECT.md`
  §5 and nobody has re-run them since 2026-10-06. If anyone does and gets
  other numbers, the sentences to change are the ones that say "quoted".
