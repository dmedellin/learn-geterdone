# Pedagogy assessment — Word Order (english, course 3)

Formed from the three lesson dicts in `content/english/c3_word_order/`
(`part_a.py`, `part_b.py`, `part_c.py`), the course dict in `__init__.py`, the
three lab modes they call (`svo`, `adverbs`, `questions` in
`scripts/mathpath/labs/english.py`, as the kit engineer left them on
2026-10-08), the three data files the labs inline
(`content/english/data/wordorder_passage.json`, `adverb_concordance.json`,
`question_concordance.json`) and the two modern documents
(`scotus_stanley.txt`, `census_aging.txt`), and the pages as
`scripts/preview_subject.py english --course word-order` renders them, with
every preset's tiles read off the built page by `labcheck.js --observe`. The
course may assume Tense Tables and Irregular Verbs and nothing else. All three
lessons were read before any was changed; the last two sections record what
was changed and what was not.

Lessons, in course order: `who-does-what-to-whom`, `where-the-adverb-goes`,
`asking-a-question`.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Name
  the two forms of five pronouns, state the rule, read its score off the
  printed passage and name each kind of apparent exception
  (`who-does-what-to-whom`); place *always*, *never*, *often*, state the three
  middle places and name the kinds of line that fall outside them
  (`where-the-adverb-goes`); build a question with a helping verb, add *do*,
  read the rule's score off the ninety printed questions and say which figures
  are counted and which are quoted (`asking-a-question`). The course
  `outcomes` are acts too: say why English can afford a fixed order, score the
  rule without marking anything up, put a frequency adverb where it belongs,
  say what a question actually looks like. None is "understand".
- **One method, taught three times, in the right order.** State a rule; count
  it on text printed on the page; sort what is left. The pronoun rule comes
  first because it is the strongest (90.0% on the passage, 88.7% on the novel)
  and its residue is three nameable things; the adverb rule second because it
  is weaker (70.8%) and its residue is mixed; the question rule last because
  it covers half, and the lesson's point is the other half. The course
  `syllabus_intro` says exactly this.
- **The residue is taught as content, not rounded away.** The speech tag
  (*said he*) is named as the one inversion English keeps and is placed as a
  story habit, not an order a learner should copy; a lexicon gap is named as a
  limit of the tool, not of the sentence; *never in my life* and *as soon as*
  are named as phrases the rule did not mean to cover. A learner leaves with
  the rule and a map of its edges, which is the thing a grammar book does not
  print.
- **The misconceptions are the real ones for the stated reader** (a speaker of
  a free-order or verb-final language) and each is refuted with the specific
  case: *said he* as a pattern to copy; *they both knew* as a break in the
  rule; moving words the way one's own language would; *she knew always*; the
  adverb between the verb and its object; forgetting that *be* works
  differently; asking by tone alone; *do you can go?*; believing a low score
  means the rule is wrong.
- **Every row is printed.** The passage, the 120 adverb lines and the 90
  questions are all on the page with the verdict beside each, and the
  `how_to` tells the reader to check a row and disagree with it. That is the
  Subject's promise kept at the level where it matters.
- **The modern-document comparison is now a computed finding, not an
  assertion.** The two documents are printed in full, named, and counted on
  each page (84.3 against 13.9 subject pronouns per thousand; 2 adverbs in
  1,723 words; zero question marks). The lesson draws the right conclusion
  from it: a learner who reads only formal prose does not meet the shapes
  speech needs.

## What the course taught badly, or wrongly, before this pass

1. **The course promised computation and delivered quotation.** The course
   `footer_lead` said "Every figure on this course is counted in your browser
   over text printed on the same page" and `how_to` said "Every figure here is
   computed from words on the same page", while the prose figures a reader
   actually meets — 5,990 and 88.7% and the 63/16/15/6 split
   (`who-does-what-to-whom`); 577, 81.8% and the 51/23/10/7/14 split
   (`where-the-adverb-goes`); 55.4% and 45% (`asking-a-question`); 4.5×, 4.4×,
   1,844 words and one question in 256 (all three) — were counts over the
   whole novel that no page carries. `asking-a-question` went further and
   shipped "STATED, not computed in your browser" in its key under that
   footer, while the kit's `questions` lab computes 48 of 90 on the page.
   This was the most serious defect: the Subject's one claim, false on its
   own course home. Fixed throughout. Every lab figure now leads; every
   whole-novel figure is kept only where it adds something (the scale of the
   check, the five-way residue) and is labelled quoted in the sentence that
   states it; the footer and `how_to` say that this is the arrangement. The
   figures the kit engineer could not reproduce from the novel (4.5×, 4.4×,
   one in 256) and the whitespace-token count (1,844) are gone, replaced by
   what the page computes (6.1× and 10.9×, 1.2 per thousand, zero in 1,723).
2. **`who-does-what-to-whom` described a lab that does not exist.** The panel
   said the passage had "126 subject pronouns"; the lab finds 80. It said "the
   next boxes are the four groups the misses fall into, and the last counts
   real order mistakes"; the boxes are *rule holds*, *share*, *word order
   broken*, *a modifier comes between*, and three per-thousand tiles. Worst,
   the key said "real order mistakes found 0" while the tile two inches below
   it read *word order broken: 1*, and nothing on the page connected the two.
   The 1 is the speech tag *"My dear sister," said he*, which the rule as
   stated does not cover. The panel, key, concepts and body now say that this
   is what the tile counts and why the lesson still calls it a habit rather
   than an error.
3. **The course key stated a number no page computes.** "subject pronoun then
   its verb 91.9%": the lab pins 90.0% and the novel figure is 88.7%. Now
   90.0%, with the adverb and question lines given to the same precision as
   their tiles (70.8%, 53.3%).
4. **`where-the-adverb-goes` promised a passage and a printed verb list it does
   not have.** The panel said "using the verb forms printed beside the
   passage"; the lab has no passage (120 cut lines) and the 249 verb forms are
   carried in the page's script, not printed as a list. It also said "the
   other boxes count each group of misses" when the lab sorts misses two
   ways, *a preposition follows* and *something else between*, not into the
   five whole-novel groups. The panel now says what is there, and the worked
   block sets the page's 35 misses beside the novel's 105 so the reader can
   see that the same kinds recur (five lexicon gaps, three *as soon as*, five
   adverbs before an adjective, clause-start, clause-end, one lone
   *Sometimes.*). The lab's nine adverbs include *soon*, *still* and
   *already*, which tell when rather than how often; the lesson discussed
   *still* and *already* and never mentioned *soon*. It now says all three
   take the same middle places and are scored with the rest. *Rarely* has
   no rows; the menu now leaves it out (fixed 2026-10-08).
5. **`asking-a-question` named the wrong largest group and did not know its
   data was cut.** The lesson said the joining-word group was "the largest by
   a long way". On the page it is 13 of 42; the box called *something else*
   holds 21. Reading those 21: sixteen begin in the middle of a sentence or
   of a word (*d Lydia; but while…*, *oment, should you…*) because the line
   was cut a fixed distance before the question mark, or at the full stop in
   *Mr.* or *Mrs.* (*Bennet, impossible…*, *Collins, I think?*), so their
   first word is not the question's first word; the five whole ones are two
   with a name first, two with a clause first and one statement with a
   question mark. The lesson now says this, in the concept, the panel, the
   worked block and the body, and lists the other two kinds the verdict
   column names (six question words with no helping verb after them, two
   address words). The whole-novel 45% stays as a quoted figure beside the
   page's 31.0%, with the sentence that 90 lines are a sample.
6. **Every quiz keyed the first answer.** Twelve questions, twelve `"c": 0`.
   Now 3/3/3/3 across the course (`[2, 0, 3, 1]`, `[1, 3, 0, 2]`,
   `[3, 1, 2, 0]`); no `why` refers to a choice by its letter. Two quiz
   questions were also rewritten because their premise was gone: "Why is the
   figure for questions stated and not computed?" and "What did the modern
   public documents show about questions? — None in 1,844 words, while Austen
   has one in about every 256".
7. **A false claim about *her*.** `who-does-what-to-whom` said "*her* is only
   ever the one it happens to". *Her* is also the possessive (*her book*),
   which is exactly why the kit's object preset leaves it out. The example now
   uses *them*, and the body and the first step say what *her* does.
8. **A false claim about Spanish.** "The ending on the noun or the small word
   before it says who did the biting." Spanish nouns carry no case endings;
   the personal *a* and verb agreement carry the job. The sentence now gives
   Spanish its *a* and agreement, Russian its noun endings, Japanese and
   Korean their small word after the noun.
9. **A term used across two lessons and never defined.** "Helping verb" runs
   through `where-the-adverb-goes` and `asking-a-question`; Tense Tables calls
   the same words "the small word in front" and never uses the term. It is
   now a `<dfn>` at first use in lesson two, tied back to *have*, *be* and
   *will* from Tense Tables, and lesson three bridges the kit's own labels
   ("auxiliary", "wh-word") to it.
10. **Markup in an escaped field.** `mistakes[0].title` in
    `who-does-what-to-whom` was "Treating <em>said he</em> as a new word
    order", which rendered a stray `;` and read aloud as "is less than e m".
    Now "Treating the speech tag as a new word order".
11. **The modern documents were unnamed.** "A US Supreme Court opinion and a
    Census Bureau story" is not a citation. Each lesson now names *Stanley v.
    City of Sanford*, 606 U.S. 46 (2025), and the Census Bureau's "U.S.
    Population Aging as Nation Turns 250" (9 April 2026) wherever their
    figures appear, as the data files and the printed `<details>` do.

## What it claims to teach but does not, and where a learner gets stuck

- **Two of the four kinds of miss in `asking-a-question` have no tile.** The
  lab prints boxes for the joining words and for *something else*; the six
  question-word misses and the two address-word misses are read off the
  verdict column (42 − 13 − 21 = 8, split 6/2 by reading). The worked intro
  says so. A kit change would make the lesson's four-way sort a four-way set
  of tiles; it is `@lab` work.
- **The passage's own residue is tiny.** Eight misses out of 80 cannot teach
  the shape of the residue on their own, which is why the quoted whole-novel
  split (63/16/15/6) is kept. The lesson gives the page's 5/2/1 beside it so
  the learner sees the same three kinds at both scales, and says which is
  which. A reader who wants to check the 63% cannot; the sentence says so.
- **The tokenizer has one visible quirk.** The scan's idea of a word stops at
  the typographic apostrophe, so *I don't know* is scored as *I don*, a next
  word not in the list. The worked block explains it; it is a limit a reader
  will meet in the table and should not be left to puzzle over.
- **Cognitive load.** `who-does-what-to-whom` carries two pronoun sets, two
  scales of count and a tile whose name contradicts the lesson's thesis; the
  key now holds the passage figure, the quoted novel figure and the one
  broken case in three lines, and the body takes them in that order.
  `asking-a-question` carries four kinds of miss plus a data limit; the worked
  block lists them in order of size with one example each, and the data limit
  is given its own sentence rather than being folded into a kind. Neither
  lesson needs splitting; the URL space is fixed and each carries one rule.
- **Worked-example progression.** Each lesson runs concept → four steps (the
  procedure) → lab (every row printed, the reader free to disagree) → worked
  residue (the faded example: how the misses sort, with one line from the page
  for each kind) → mistakes → quiz. The lab is independent practice on the
  rule; the worked block is the guided reading of what the lab left over.
  That is the right shape for a rule-and-residue lesson and it is the same on
  all three pages.
- **Retrieval practice.** Each `why` answers the specific error rather than
  restating the rule: the distractor "13, which is 31.0%" in lesson three is
  explained as the joining-word count and its share of the misses; "There are
  exactly none, proved over every case" in lesson one is answered with what
  was and was not read; "Words in the wrong place" in lesson two is answered
  with the tool's limit.

## Prerequisite order

Checked backwards against the two earlier courses. *Have*, *be* and *will* as
"the small word in front" of the verb are Tense Tables (`five-forms-and-the-whole-table`);
lesson two names them helping verbs and says where they came from. The
verb forms the scans match against are the forms Tense Tables builds and
Irregular Verbs lists, as the course `assumes_long` says; the labs carry their
own lists of the forms the printed text contains, so nothing is assumed about a
reader's recall. Within the course: *pronoun*, *subject*, *verb*, *modifier*
and *speech tag* are defined in lesson one before use; *adverb* and *helping
verb* in lesson two; lesson three uses only those and bridges the kit's
"auxiliary" and "wh-word". The adverb rule's "after the first helping verb"
needs the helping-verb notion, so adverbs before questions is right, and the
question rule moves that same helping verb, so it comes last. Listening (course
four) assumes nothing from this course and this course assumes nothing from it.
No violation sits in an earlier course.

## Accuracy of the English

Checked claim by claim. Subject and object forms of *I, he, she, we, they* and
the invariance of *you* and *it*: right. *Her* as both object and possessive:
right now (item 7). Old English noun case largely lost: right. Quotation-tag
inversion (*said he*) as a narrative device confined to reported speech, not a
productive order: right. The mid-position rule — before the main verb, after
the first auxiliary, after *be* as a main verb — is the standard account, and
the lesson's hedge that frequency adverbs can also stand first or last, while
*always* and *never* normally do not, is right. *Still*, *already* and *soon*
are mid-position adverbs of time rather than frequency: right, and now said.
Subject–auxiliary inversion with *do*-support, wh-fronting, and no inversion
when the wh-word is the subject (*who went?*): right. *What say you?* as the
older pattern without *do*-support: right. Declarative questions by intonation
and their pragmatic colouring (surprise, checking): right. Spanish personal *a*
and agreement, Russian case endings, Japanese and Korean particles after the
noun: right now (item 8). Mandarin and Japanese question particles at the end
of the clause: right; "an ending on the verb" is Korean, and the lesson leaves
it unnamed. One claim was softened rather than removed: "*me, him, us, them*
are never the subject" now carries "in careful English", because
*me and him went* is heard. "*I, he, she, we, they* are always the subject"
carries the same hedge; *it is I* makes *I* a complement, which the hedge
covers for this reader.

## Changes made

- `__init__.py`: `summary` says the question rule covers half and the course
  prints the other half; `how_to[0]` and `footer_lead` say that lab figures
  are counted on the page and whole-novel figures are quoted and labelled;
  the key reads *he or him* (not a slash a voice reads as "over"), 90.0%,
  70.8% and 53.3% to match the tiles.
- `who-does-what-to-whom`: module docstring; `standard`, `summary`, key and
  all three concepts lead with 72 of 80 and label 88.7% quoted; the first step
  and the body explain *her*; the panel describes the real tiles, the 80
  pronouns, the *word order broken* tile, the excluded *her*, and names the
  two modern documents; the worked block sets the page's 5/2/1 beside the
  novel's 63/16/15/6 with one line from the passage for each, and explains
  *interrupt* and *don't*; `note` says 90.0%; `mistakes[0].title` is plain
  text; quiz keys `[2, 0, 3, 1]`, question two asks about the eight on the
  page, question three's `why` gives 84.3 against 13.9 and names the
  documents; the body opens with the corrected Spanish/Russian/Japanese/Korean
  sentence, gives the page's score before the quoted one, counts *you* and
  *it* (46, left out), reports 6.1× and 10.9× from the tiles, and cites both
  documents.
- `where-the-adverb-goes`: module docstring; `summary` defines *helping verb*
  with `<dfn>` and leads with 85 of 120; the key reads "120 printed lines: 85
  in the middle 70.8%" and "whole novel, quoted: 472 of 577 81.8%" (the old
  three-column lines were read aloud as "a table, shown on the page");
  concepts name *soon*, *still*, *already*, *still better*, *as soon as*, and
  the lab's two-way sort; the panel describes the 120 lines, the 249-form list
  the page carries, the two miss tiles and the one-adverb menu, and names the documents; the worked block adds the page's 6/29 with
  examples and names the five lexicon gaps; `note` gives both scales;
  `mistakes[2]` says "every other main verb"; quiz keys `[1, 3, 0, 2]`,
  question two is placed in the whole-novel run, question three asks about
  70.8%, question four asks what the lab finds (2 in 1,723, 1.2 per thousand)
  and names the documents; the body gives the page's score word by word
  (*always* 15 of 16, *never* 14, *sometimes* 7), labels the novel's figures
  quoted, adds a section on the 35 misses on the page, and gives 1.2 per
  thousand against about 4.7 (577 in about 122,400, both quoted).
- `asking-a-question`: rewritten from "stated, not computed" to "the rule
  that covers only half". Docstring, `module`, `one_line`, `standard`,
  `summary`, key ("90 printed questions: 48 follow it 53.3%", "whole novel,
  quoted 55.4%"), all three concepts (the rule; the four kinds of miss with
  the page's counts; counted against quoted, and the sixteen cut lines), the
  fourth step, the panel (what the tiles are, the eight misses in no box, the
  cut lines, the modern-document search, both documents named), `read_intro`,
  the worked block (page counts with one example per kind, then the quoted
  45%), `note`, `mistakes[2]`, quiz keys `[3, 1, 2, 0]` with questions two to
  four rewritten around the page's 48 of 90, 13 of 42 and 0 in 1,723, and the
  body (score, the four kinds with the cut-line explanation, which figures are
  counted and which quoted, the modern documents named, 53.3% in the closing
  line).
- `docs/ENGLISH-SUBJECT.md` §5 Course 3 and §6 second landmine: the
  whole-novel figures are marked quoted and the page figures are tabulated
  from the tiles; the 4.5×/4.4×/256/1,844 figures are recorded as not
  reproduced and no longer stated. The Course 1 lines are left to the Tense
  Tables pass.

## Remaining issues

- **The path footer and `material` in `content/english/__init__.py`** still
  say every figure on the path is computed in the browser. The course footer
  is now true; the path's is not, for the quoted whole-novel figures this
  course keeps, and that file is not this course's to edit. The same file's
  `sequence_intro` ("each needs the last") and `why_order` ("Word Order comes
  last"; Listening is fourth and has no entry) are the review's SHOULD item
  and are also out of this course's scope.
- **`question_concordance.json` carries 27 lines of 90 that begin
  mid-sentence**, sixteen of them in the *something else* bucket. The lesson
  now says so honestly, but the honest fix is upstream: re-cut the lines at
  sentence boundaries that do not take *Mr.*, *Mrs.* or *Miss* for the end of
  a sentence. That is data work; it would move the pinned 48 of 90 and the
  kit's `expect`.
- ~~`adverb_concordance.json` has no *rarely* rows~~ — fixed 2026-10-08: the
  menu is built only from adverbs that have rows.
- **The `svo` tile *word order broken*** counts the speech tag; the lesson
  explains it, but a kit relabel ("verb before its pronoun, a speech tag")
  would remove the need for the explanation.
- **The quoted whole-novel figures** (5,990, 88.7%, 63/16/15/6, 88%; 577,
  81.8%, 51/23/10/7/14; 55.4%, 45%) rest on the design record in
  `docs/ENGLISH-SUBJECT.md` §5. The kit engineer neither reproduced nor
  disputed them. If anyone re-runs the novel and gets other numbers, the
  sentences to change are the ones that say "quoted".
- **`tests/content_preservation.json`** pins an AST hash and two or more
  approved clauses for each of the four files in this course; this pass
  changed every hash and seven of the fourteen clauses (the two summaries,
  the three notes, lesson three's summary and "Only the 45% was counted"
  paragraph). The orchestrator regenerates those entries before committing.
- **Read-out.** The four arrow lines in `asking-a-question`'s key read "you
  know, to, do you know"; the spoken forms belong in
  `content/spoken/english.py`, which the orchestrator owns. The table is in
  this pass's return.
