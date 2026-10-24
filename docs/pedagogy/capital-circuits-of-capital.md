# Pedagogy assessment — The Circuits of Capital (Capital, course 6)

Formed from the six lesson dicts in `content/capital/c06_circuits/part_a.py`
(one per chapter of Volume II, Part I) and the course dict in `__init__.py`,
and the kit they render through (`scripts/mathpath/labs/capkit.py`, modes
`circuit` views `stages` and `costs`, `accumulate` view `expand`, `surplus`
view `parts`; `capkit_b.py`, mode `turnover` views `phases` and `time`), on
branch `feat/capital-subject` before the Subject was wired into the site. The
design authority is `docs/capital/PLAN.md` §0, §B, the Course 6 entries in §C,
§E (how a passage is quoted), §F (the voice) and §G; the kit as described in
`docs/capital/kit-a-report.md` and `kit-b-report.md`; the author's brief in
`docs/capital/AUTHORING.md`. Course 1, Commodities and Money, is the voice
reference and its assessment (`capital-commodities-and-money.md`) the model.

Every lesson was read in full before anything was changed, and so were the
six chapters of the Kerr Volume II (`/mnt/project-files/capital-texts/
volume-2-kerr.txt`, lines 336–1424), whole and not only the passages. Every
pinned tile was read off the rendered page with `node scripts/labcheck.js
--observe` (rendered through `scripts/preview_subject.py capital --course
capital-circuits-of-capital`), every figure in prose was recomputed by hand,
and every phrase inside `&ldquo;…&rdquo;` (fifty-six distinct spans, after
the repairs below) was searched for character by character in the Kerr text.
Every math run on the seven rendered pages was read from its `data-say`.
Lessons, in course order: `the-circuit-of-money-capital`,
`the-circuit-of-productive-capital`, `the-circuit-of-commodity-capital`,
`the-three-formulas-of-the-circuit`, `the-time-of-circulation`,
`the-costs-of-circulation`. The course assumes the five Volume I courses, and
above all the spinning mill and the rate of surplus value, and is judged
against that.

## Verdict

The course teaches its subject, and it does the harder thing Part I of
Volume II asks of a teacher: it makes six chapters that are mostly the same
movement written three ways into six distinct acts, each with a figure a
reader can check. A reader who finishes it can trace Marx's £422 through
money, productive and commodity capital and say that `M′ − M` is `£78` when
all 10,000 lb sell, `£0` at 8,440 lb, `−£50` at 7,440 lb and `−£422` with
nothing sold, and that none of those figures changes the £500 the yarn is
worth; restart production at £422, at £480 with Marx's £58 capitalised, or
hold £78 a week as a hoard until £234 clears a £200 minimum; cut 10,000 lb of
yarn into 7,440, 1,000 and 1,560 lb and each of Marx's three lots the same
way, and say that only `£128` of the `£500` is anyone's income; divide a
continuous capital a third, a third, a third, or a quarter, a quarter, a half
when selling slows; compute a 12-week turnover with half of it in
circulation, and a 26-week one with `10/13`; and sort a book-keeper's £10
from a carter's £10 so that one leaves `£90` of surplus value and the other
`£100`. Those are the acts the `standard` fields name and the quizzes
measure; no objective is "understand X". The `mistakes[0]` of every lesson is
the §C misconception and each is refuted with a tile. All 23 pinned tile
strings on the six pages matched the lab, and every figure in prose agreed
with the lab or with a recomputation.

Fidelity to the chapters is high. Of the fifty-six distinct quoted spans,
every one is in the Kerr text; three are split by a page-break marker in the
plain-text file and one is two sentences joined with an ellipsis across an
omitted paragraph (the Chapter 3 opening), which §E.3's "character for
character" tolerates but which the next author should avoid where one
sentence will do. Nothing is quoted from memory. The three slips in the Kerr
tables of Chapter 3 that the lesson names (`1,160.740`, `343.360`, `7,450`)
are really there, in the lines the lesson says. Marx is presented, not
endorsed: the monetary and mercantile systems, Say and James Mill, Adam
Smith twice, Quesnay, Bailey, Böhm-Bawerk, and the national-accounts view of
services each get two or three sentences at full strength before Marx
answers, and every `note` names what the lab cannot settle. The defects were
local and all were repaired: two places where the lesson had Marx arguing
with people the chapter does not name without saying so, one key line and
two sets of Roman numerals that the read-out spelled as letters, one
simplification of Chapter 6's storage section that dropped half of what Marx
says, and two cross-references by course where the library's rule asks for
the lesson's title or Marx's chapter number. Nothing needs splitting, merging
or reordering.

## The voice, judged against §F and against Course 1

**What is done as Course 1 does it:**

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume II, Chapter n.</strong>` block and returns to it: "One-sided,
  because it starts and ends in money… Typical, for the same reason"
  (`the-circuit-of-money-capital`); "Start from the yarn. It is not the
  capital that was advanced, it is that capital plus what production added"
  (`the-circuit-of-commodity-capital`); "Transport is the exception because a
  product's use is where it is consumed" (`the-costs-of-circulation`). Each
  lesson carries a second short passage the same way, and the `read_intro`
  says where in the chapter each comes from.
- **No invented scenes.** §F rule 2 says the Volume II lessons open with the
  passage's own figures, and five of the six do: "Same spinner, same £422,
  same £500 of yarn. But begin the story in the mill." The one scene is in
  `the-costs-of-circulation`, "Think of the price of almost anything you buy.
  Some of it paid for making the thing, some for moving it to the shop, and
  some for advertising, sales staff, accounts, card fees and the shop's own
  margin", and it reaches the chapter's line within the paragraph. That is
  the one chapter of the six whose object is in the reader's life, and the
  course knew it.
- **The history of ideas as story with people in it.** The Russian landowners
  after 1861 with their two complaints; Say and James Mill and the argument
  that "every sale is also a purchase"; Smith's resolution of price into
  revenues with its reasoning given ("the cotton was grown with paid labour,
  the spindle was made with paid labour"); Quesnay "court physician at
  Versailles" drawing the Tableau in 1758; Bailey "the Sheffield writer whose
  1825 Critical Dissertation was the sharpest attack on Ricardo's theory of
  value", with "modern economics largely agrees with him"; Böhm-Bawerk's
  roundabout production and "later theories of the time value of money";
  Shaikh and Tonak's 1994 remeasurement. Each opponent gets the fact his view
  rests on before Marx's reply.
- **Second person, warm, in `p` and `worked.intro` only.** "which you can
  check: `78/50 = 156/100`"; "What changes is where you stand to watch it";
  "Check his totals and you will find slips in the Kerr text's tables". Every
  worked intro is "You want…". `steps`, `standard`, quiz items and tile text
  stay impersonal; no "Let's", no first person.
- **Marx's jokes before the lesson's.** "Marx's dry aside" on nations "seized
  periodically by a feverish attempt to make money without the mediation of
  the process of production"; the buyer's "malignant intention"; the railway
  magnates with "a greater talent for inventing fantastic species than
  botanists and zoologists", introduced as "Marx is sardonic". None is the
  lesson's own, none is at the reader's expense, and lessons 2, 4 and 5 make
  none, which is right for chapters that have none.
- **The limit admitted.** Every `note` names one thing: sale at value and no
  change of value during circulation (lesson 1); the same composition each
  week, against Marx's own warning about P′ (lesson 2); the lab "cannot say
  who will buy each part" (lesson 3); time-share equals capital-share "only
  when production runs evenly" (lesson 4); circulation time taken as given
  (lesson 5); the carter adds value but no surplus value, "to keep the one
  distinction in view" (lesson 6). The course `how_to` says Volume II is
  Engels' assembly of Marx's manuscripts and quotes Engels' "to make
  something", which is in the preface.
- **Pointing forward by title.** Every body ends with the next lesson's title
  and its question, and lesson 6 with The Turnover of Capital and "how much
  capital it takes to keep production going".

**What differs from Course 1, and should be copied by later courses:**

- **The course tells the reader what kind of book this is.** `how_to[1]`
  says Marx did not finish it, who assembled it, from which manuscripts, and
  that "in places it reads like notes, repeated and unpolished". A reader who
  hits Chapter 4's repetitions has been warned. Later Volume II and III
  courses should carry the same sentence once.
- **The course says which figures are Marx's and which are not, course-wide
  and per lesson.** `how_to[2]`: the first three lessons use Marx's figures
  throughout; "The last three need weeks and costs the chapters do not give;
  there the figures are illustrative, and each lesson says so." Each does.
- **The course corrects the text where the text is wrong, and shows its
  work.** Lesson 3 names the three misprints in the Kerr tables and adds the
  lots exactly: `5,535.36 + 744 + 1,160.64 = 7,440`. That is exactly what §0
  asks a read-along to do.

## What the course teaches well

- **One hard idea per lesson, and six distinct acts from one movement.** The
  danger of Part I is that Chapters 1 to 4 are the same circuit from three
  points, and a course can end up teaching the same arithmetic four times.
  This one does not: lesson 1 is the partial sale (produced against
  realised), lesson 2 is what the surplus value does next (spent, invested,
  hoarded), lesson 3 is the product in parts (and the three lots), lesson 4
  is the division of a continuous capital by time. The `concepts_intro` of
  lesson 4 says so in one line: "Chapter 4 adds nothing new to the circuit.
  It adds time, and the fact that a real business does not stop."
- **The misconceptions are refuted with the specific figure.** "With nothing
  sold, the table still shows a product worth £500 against £422 advanced,
  while the tile for money returned is £0" (lesson 1). "`P…P` under simple
  reproduction runs from £422 to £422, as the simple preset's tile shows"
  (lesson 2). "Of 10,000 lb, 7,440 lb carry £372 that must buy back cotton,
  coal and wear" (lesson 3). "In the slow-sale preset half of it is unsold
  product while a quarter is at work" (lesson 4). "Tied up for 26 weeks and
  producing for 6 of them" (lesson 5). "The goods are worth £500 with or
  without the book-keeper, so his £10 can only come out of the £100 of
  surplus value" (lesson 6).
- **The arithmetic is right and the lab's model is kept apart from the
  chapter.** `78/50 = 156/100`; `8,440 s = £422`; `211/250` and `93/125` as
  shares of 10,000 lb; `422/480 = 211/240`; `3 · 78 = 234 ≥ 200`;
  `34596/125 = 276.768`, `138,384/25 = 5,535.36`, `7254/125 = 58.032`,
  `1521/125 = 12.168`; `6/10 = 3/5`; `52/26 = 2`; `£510 − £410 = £100`. Lesson
  4's `note` says the proportional model is the lab's and not Marx's; lesson
  5's panel says why one tile prints `—`.
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first preset by hand with a second case in `after`; every
  `panel_intro` asks for a comparison before the press ("Compare the unsold
  preset's table with its tiles: the product is worth £500 either way"; "Add
  the three lots' tiles and compare them with the whole"); every quiz asks
  the same act on a fresh instance (2, 6, 2 weeks; 6 and 20 weeks; a carter
  on £500 that cost £400). The distractors are the named errors: `£578` for
  adding the surplus value twice, `£442` for adding the £20 spent instead of
  the £58 invested, `26/3` for ignoring circulation time, `£80` for deducting
  the clerk twice. Every wrong answer was argued for and none could be
  defended.
- **Every preset id is in a body paragraph with its figure.** All sixteen
  preset ids on the six pages appear in prose with the tile they show, which
  Course 1's review asked for and this course did from the start.
- **The chapter's own stories are used for what Marx uses them for.** The
  Russian landowners for the class relation in `M–L`; the £110 example for
  money's homogeneity; the machine that "cannot be divided into capital-value
  and surplus-value without breaking it to pieces" and the London builders
  for ideal division; the Chinese artisan for production in jumps; the
  salesman paid eight hours and working ten for the pure cost; the buyer's
  "So much the worse for you" for the unsaleable stock.

## What it taught badly, or said wrongly

### Fidelity

- **`the-circuit-of-money-capital`, the mercantilist paragraph and
  `mistakes[0]`:** "The mercantilist writers of the seventeenth and
  eighteenth centuries… it is a fair reading of `M…M′` alone that the gain is
  made in selling, by selling dear." Chapter 1 is more exact than that: it
  is the "so-called monetary system" that reads `M–C–M′` as "a movement
  which takes place exclusively in the circulation" and so "cannot explain
  the two phases M-C and C-M' in any other way than by declaring that C is
  sold above its value", while "a more highly developed mercantile system"
  puts production inside the formula. The paragraph now quotes those
  sentences and makes the distinction; `mistakes[0]` names the monetary
  system.
- **`the-circuit-of-productive-capital`, the Say paragraph:** "Jean-Baptiste
  Say and James Mill built a famous argument on that look… Marx's comment on
  the argument is brief". The chapter says only "some economists use this
  sort of exchange as a proof that there can be no overproduction" and names
  no one. Naming Say and Mill is right history and belongs here; saying Marx
  commented on their argument is not. Now "Marx does not name them in this
  chapter; his comment is one sentence".
- **`the-costs-of-circulation`, the storage paragraph:** the lesson had
  necessary storage simply "enter its value", and Chapter 6, §II is not that
  simple: the costs of a supply "enter in part into the value of the
  commodities", and the same paragraphs call them "dead expenses" and
  "deductions from the social wealth, although they are one of its
  requirements". The binary the lab needs is the lesson's, not Marx's. Two
  sentences added quoting both halves and saying the lab keeps the first.
- **`__init__.py`, `how_to[1]`:** checked against Engels' preface and the
  editorial footnotes: Chapters 1–4 are from Manuscripts V, VI and VII of
  1877–78 with a note of 1877 or 1878 closing Chapter 4, Chapters 5 and 6
  from Manuscript IV; "to make something" is Engels' own quotation of Marx.
  Correct as written; nothing changed.

### Cross-references

- **`the-circuit-of-commodity-capital`, the Smith paragraph:** "Marx's reply
  takes a whole chapter later in the volume" named neither the chapter nor
  the lesson. §0's first deviation asks for Marx's chapters by number and the
  library's rule for lessons by title. Now "Volume II, Chapter 19, read in
  Reproduction of the Social Capital as “Former Presentations: Quesnay and
  Smith”".
- **`the-time-of-circulation`, the production-time paragraph:** "That
  difference has its own lesson in The Turnover of Capital" now names the
  lesson, “The Time of Production”, as §C's own entry does.

### Speech

Every math run on the seven rendered pages was read from `data-say`. The
circuit notation reads well: `M to C and so on P and so on C prime to M
prime`, `P and so on Tc and so on P`, `C prime and so on C prime`; grouped
numbers lose their commas and read `10000 times 372 over 500 equals 7440 lb`
and `5535.36 plus 744 plus 1160.64 equals 7440`, which a voice reads as
numbers. Three shapes read wrongly, none flagged by the checker, all repaired
in the content:

- **`M = mp + lp` read "M equals m p plus l p".** The lowercase pair were
  the lab's field names, not Marx's letters. The key line is now `M = Pm +
  L: £422 = £372 + £50`, which reads "M equals P m plus L", Marx's own
  symbols, and the body's first-stage paragraph now introduces `M–Pm` and
  `M–L` by name so the reader has met them.
- **Roman numerals in a run read as letter groups.** The course `key`'s
  `I.`, `II.`, `III.` and lesson 4's `I M…M′, II P…P, III C′…C′` read "I",
  "I I", "I I I". Now `first,`/`second,`/`third,` on the course home and
  `M…M′, P…P, C′…C′: three circuits, one capital` on the lesson.
- `its` after `=` in `share in a form = its weeks / all weeks` was checked
  and reads as the word; Course 1's three-letter rule does not bite here.

## Can a reader who finished Volume I follow these six lessons?

Yes, and the course does the two things that make Part I readable: it keeps
one example in view and it tells the reader what each chapter adds.

- **Lesson 1** is carried by the spinner, whose £422, £372, £50 and £500 the
  reader met in From Money to Surplus Value, so the first stage is a
  purchase of things already known. The partial sale is the chapter's one
  piece of arithmetic and the lesson makes it the lab, with Marx's own two
  partial sales as presets. The £110 paragraph gives the reader the chapter's
  real point, that money "carries no mark" of which part was advanced, before
  the verdict passage that depends on it. The Russian landowners arrive where
  Marx puts them, as the fact behind `M–L`.
- **Lesson 2** is where Volume II's dryness bites, and the lesson gives the
  reader a reason to care: the Say paragraph and the crisis paragraph ("the
  old bills fall due, and dealers sell at any price to pay them") show what
  rides on the money stage being more than a veil. The hoard is taught with
  the chapter's one figure, a pound a spindle, and a three-week slider the
  reader is told to move.
- **Lesson 3** is the course's best. It takes Marx's three lots seriously,
  finds the misprints, adds the lots back, and uses the aggregate-capital
  passage to show the reader why a chapter about one spinner's yarn ends in
  a society's annual product. Smith's resolution of price into revenues is
  given as a serious position with its reasoning, which is what the
  reproduction schemes will need.
- **Lesson 4** could easily be the dullest, since Chapter 4 repeats itself;
  the lesson says in its `concepts_intro` that the chapter adds only time,
  gives the Chinese artisan as the business that does stop, and then gives
  the reader a lab with a figure to move. Bailey is answered where Marx
  answers him. What a first reading will miss is Chapter 4's supply-and-
  demand passage (the capitalist whose demand is `80c + 20v` against a supply
  of `80c + 20v + 20s`), which is computable and is left out; recorded below.
- **Lesson 5** gives the three reasons political economy "takes this negative
  effect for a positive one" in one paragraph each, which is the chapter's
  own argument, and names Böhm-Bawerk as the strongest opponent in the lesson
  where his view bears. The lab's blank `tuAggregate` tile is explained in
  the panel.
- **Lesson 6** opens with the reader's receipt and closes with Shaikh and
  Tonak, and in between gives all three of Chapter 6's sections their due,
  including the storage ambivalence now that it is there.

The course also protects the reader in two ways: `how_to[1]` says what kind
of text Volume II is, and `how_to[2]` says which figures are Marx's, so a
reader never mistakes the lab's weeks for a claim about spinning.

## Repairs made in this pass

In `content/capital/c06_circuits/__init__.py`: `key[0]`, `key[1]`, `key[2]`
(Roman numerals to words). In `part_a.py`: `the-circuit-of-money-capital`
`key[1]`, the first-stage paragraph (`M–Pm` and `M–L` introduced), the
monetary-system paragraph, `mistakes[0]`; `the-circuit-of-productive-capital`
the Say paragraph; `the-circuit-of-commodity-capital` the Smith paragraph
(Chapter 19 and the lesson title); `the-three-formulas-of-the-circuit`
`key[0]`; `the-time-of-circulation` the production-time paragraph (lesson
title); `the-costs-of-circulation` the storage paragraph. No preset, `expect`,
slug, module, lab key, mode or view changed, and no §C entry needed
correcting: every instance the lessons carry is the one §C records.

Slugs, lesson count, module names (Untermann's chapter titles, with
"circulation" and "rotation" as §C requires and lesson 1 explaining once),
lab keys and modes are as PLAN §B and §C list them. After the repairs
`scripts/preview_subject.py capital --course capital-circuits-of-capital`
reports OK: 7 pages, every lab executes and survives the sweep, all 23 pinned
figures on the six pages match, no math run without a spoken form; and a
second pass over every `data-say` on the seven pages finds no spelled-out
word.

## Remaining issues

- **The Chapter 3 opening quotation is two sentences joined by `&hellip;`
  across an omitted paragraph.** Both halves are verbatim and the splice is
  honest, but §E.3's "copy it character for character" is best read as one
  continuous span. The first sentence alone would do; not changed, since the
  second sentence (C′′) is what the lesson's first paragraph explains.
- **Chapter 4's supply-and-demand passage is not taught.** "The limit of the
  maximum demand of the capitalist is C, equal to c plus v, but his supply
  for the market is c plus v plus s" is the one computable thing in Chapter 4
  the lesson leaves out, and it is the seed of the realisation problem the
  reproduction schemes take up. It would overload a lesson whose one idea is
  the division of a continuous capital. Recorded for Reproduction of the
  Social Capital's author, whose Chapter 20 lessons could point back to it.
- **The `hoard` preset's three-period figure (`£656`) is stated in prose and
  §C but cannot be pinned**, because `expect` pins only the shipped period.
  The sweep exercises the slider and the arithmetic is `422 + 3 · 78`; a kit
  change that let a preset pin a figure at a stated period would make it
  checkable. Recorded, not changed.
- **Lesson 4's time-share model is the lab's, not Marx's.** The `note` says
  so. Chapter 5's own sentence ("the part performing continually the
  function of productive capital must be so much smaller, the longer the
  aliquot parts of capital-value remain in the sphere of circulation") is
  the textual warrant and could be quoted in lesson 4's `note`; left as is to
  keep the note to one limit.
- **The read-out spells Roman numerals.** `II` and `III` in a run read as
  letters. The two cases here were reworded; a `speech.py` rule for Roman
  numerals belongs to the chrome-renderer tier and would matter for Volume
  II's Departments I and II in Course 8. Recorded, not changed.
