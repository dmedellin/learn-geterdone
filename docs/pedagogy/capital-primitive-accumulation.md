# Pedagogy assessment — So-Called Primitive Accumulation (Capital, course 5)

Formed from the eight lesson dicts in `content/capital/c05_primitive/`
(`part_a.py`, lessons 1–4, Chapters 26 to 29; `part_b.py`, lessons 5–8,
Chapters 30 to 33; `__init__.py`, the course dict) and the kit they render
through (`scripts/mathpath/labs/capkit.py` and `capkit_b.py`; modes
`accumulate`, `workday`, `wages`, `money`, `circuit`, `interest`; views
`thrift`, `separate`, `statute`, `fixed-rent`, `market`, `capitalise`,
`centralise`, `colony`), on branch `feat/capital-subject` before the Subject
was wired into the site. The design authority is `docs/capital/PLAN.md` §0
(the paragraph "Historical chapters compute too"), §B, the Course 5 entries in
§C, §E.3, §F and §G; the kit as summarised in `docs/capital/kit-a-report.md`
and `kit-b-report.md`; the voice reference is Course 1 and its assessment in
`docs/pedagogy/capital-commodities-and-money.md`.

Every lesson was read in full before anything was changed, and so were
Chapters 26 to 33 of `/mnt/project-files/capital-texts/volume-1-kerr.txt`,
whole, not only the passages. Every pinned tile was read off the rendered
page with `node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py capital --course capital-primitive-accumulation`),
every figure in prose was recomputed by hand, every quotation and every
phrase in quotation marks (ninety-nine segments) was checked character by
character against the Kerr text with the strict checker, and every math run
on the nine rendered pages was read from its `data-say`. Every claim about a
historian was checked against what that historian wrote. Lessons, in course
order: `the-secret-of-primitive-accumulation`, `expropriation-from-the-land`,
`bloody-legislation`, `the-capitalist-farmer` | `the-home-market`,
`the-industrial-capitalist`, `the-historical-tendency`,
`the-modern-theory-of-colonisation`. The bar marks the seam between the two
modules. The course assumes Wages and Accumulation and is judged against
that.

## Verdict

The course teaches its subject, and it does the hardest thing Part Eight
asks of a read-along: it keeps a history that Marx tells as an indictment at
arm's length without flattening it. A reader who finishes it can time a
capital saved out of a wage and set it beside the five years in which simple
reproduction consumes one, compute the surplus labour a day holds for an
employer before and after a producer loses her land and scale it to an
estate, compute the gap a statutory maximum opens below the value of
labour-power and the rate it enforces, trace a rent fixed by lease through a
doubling of prices and split the farmer's gain between landlord and
labourers, compute the market a hundred households make when they must buy
what they used to grow and read it as the wage bill, price a claim on the
state from its interest and reprice it when the rate falls, tell
concentration from centralisation by what happens to the largest's share and
the count, and compute how long a land price keeps a colonist's workers for
hire. Those are the acts the `standard` fields name and the quizzes measure;
no objective is "understand X". All 20 pinned tile strings on the eight pages
matched the lab, every figure in prose agreed with the lab or with a
recomputation, and all 99 quoted segments were found in the Kerr text, none
differing by more than a page break.

Marx is presented, not endorsed, and this is the course's chief
accomplishment. Every chapter's dispute is on the page with names and dates
on both sides: Weber and Crouzet against the parable of thrift; Chambers,
Allen and Richards on enclosure and the clearances; Davies, Beier and Thorold
Rogers on the vagrancy laws and the wage statutes; Bodin, Hamilton,
Outhwaite, Goldstone and Kerridge on the price revolution and the fixed rent;
Smith and de Vries on the home market; Williams, Engerman, O'Brien and
Inikori on slavery and industry, North, Weingast and Dickson on public
credit; Dühring, Engels, Bernstein, Popper and Baran and Sweezy on Chapter
32; Mill and Domar on Wakefield. The course `how_to` says "The lessons
present Marx's account; they do not ask you to accept it", `not_covered` says
none of the historians "is declared the winner", and every `note` names what
the lab cannot settle. The defects found were local and are repaired below:
three sentences that leaned toward a verdict on Marx ("deserves a fairer
hearing than Marx gives it", "precise", "exact"), four small misstatements of
the text (serfdom gone "in the fifteenth century" where Marx says the last
part of the fourteenth; Elizabeth and James I "added branding", which Edward
VI's statute already had; "the Dutch in Java" stealing men, where the men
were stolen in Celebes; the `closed` preset described as land unavailable
when the model has the worker saving nothing), two historians characterised
loosely (Goldstone lumped with the population-pressure account; Beier's
*Masterless Men* described as a study of what lawmakers feared when it is a
study of arrest records), one dispute with only one side named (the
defenders of Chapter 32), and one `mistakes[0]` title that stated the §C
misconception as a historical claim rather than as the misreading the tile
refutes. Nothing needs splitting, merging or reordering; the eight chapters
are eight lessons, and each carries one idea.

## The labs: do they earn their place?

This is the question §0 puts to a historical course ("a lab that merely
restates a narrative is decorative"), and the answer is yes for seven of the
eight, with the eighth earning its place differently.

- **`expropriation-from-the-land`, `workday`/`separate`** is the best lab on
  the course and the model for the Subject's other historical chapters. It
  holds the day at 12 hours and the necessary labour at 6 in every preset and
  moves only `own_land` and `count`, so the tiles isolate exactly the
  chapter's claim: the work does not change, the owner of the surplus does
  (`0 h` → `6 h` → `18,000 h`). The `def` says the model "changes no hour of
  the working day; it changes who the hours beyond the necessary ones are
  worked for", the `note` says the smallholder's zero is a model because real
  peasants owed rent and tithe, and `mistakes[2]` says the estate figure is
  what separation "makes available", not a census. That is a lab that
  computes the mechanism and says what it is not.
- **`the-capitalist-farmer`, `money`/`fixed-rent`** is the second best: the
  three presets are stable, prices double, wages lag, and the arithmetic
  splits the farmer's £20 of real gain into £10 from the landlord and £10
  from the labourers, which is exactly how Marx's last sentence splits it.
  The quiz's third item ("Who is worse off in real terms?") tests the idea
  and not the formula.
- **`the-historical-tendency`, `accumulate`/`centralise`** turns a famous
  passage into a distinction Marx's readers run together: `grow` leaves the
  largest at `1/10` of a total that grew; `merge` leaves it at `3/5` of a
  total that did not. `mistakes[1]` is the right guard: "no tile computes"
  the knell.
- **`the-modern-theory-of-colonisation`, `accumulate`/`colony`** makes Peel's
  anecdote a sum (`0` for hire with free land, `3,000` for four years at
  Wakefield's price) and uses the shipped `periods` slider as a teaching
  move: "move the slider to five and they are gone".
- **`the-home-market`, `circuit`/`market`** holds consumption at `1s 6d` in
  every preset so the market's rise from `0s` to `150s` is visibly a change of
  form and not of quantity, which is the chapter's point and the exact point
  de Vries disputes; the `note` says so.
- **`bloody-legislation`, `wages`/`statute`** and
  **`the-secret-of-primitive-accumulation`, `accumulate`/`thrift`** compute
  the direction of an effect (a ceiling a third below the value doubles the
  rate; thrift out of a wage takes six and a half centuries), and both say in
  the `panel_intro` and the `note` that every figure is illustrative. They
  are the two labs closest to decoration, because the chapter gives no
  figures to compute with; they stay on the right side of the line because
  each refutes a stated misreading with its tile (a wage law is a floor; a
  factory can be saved for) and because the prose uses the figure rather
  than displaying it.
- **`the-industrial-capitalist`, `interest`/`capitalise`** is honest about
  being one lever of four: "The lab computes the debt because it is the lever
  with a formula; the others are matters of evidence." The `bank-1694` preset
  uses Marx's 8% and the label says so. The `note` defines "capitalise"
  locally, as §C requires, since interest is not taught until Merchant's
  Capital and Interest.

Every preset id appears in a body paragraph with its figure (the rule the
Course 1 review laid down), every "Marx's figures" label is Marx's (3,000
Sutherland families, 8% in 1694, £50,000 and 3000 persons), and every
illustrative figure is called illustrative in `panel_intro`, `worked.after`
or `note`.

## Misconceptions: misreadings, not history

The brief for this course was that each `mistakes[0]` must be a misreading
refuted by a tile and never a historical or political claim. Judged one by
one:

- Lesson 2 ("what changed at the clearing was the work, not who it was done
  for"): a misreading, refuted by `0 h` → `6 h` with the day unchanged.
- Lesson 3 ("a wage law protects the worker by setting a floor"): a
  misreading of the statute, refuted by `1s below the value` and `2 = 200%`.
- Lesson 4 ("when all prices double, every party is where it was"): an
  arithmetical error, refuted by `£10` and `£100` against `£40`.
- Lesson 5 ("the home market grew because people became richer"): refuted by
  `1s 6d` holding in every preset while the market goes to `150s`; the
  lesson then names de Vries as a "real rival account" and says the lab
  shows only "how a market can grow without it". That is the right way to
  handle a misconception that is also a historian's position.
- Lesson 6 ("the national debt is part of the nation's wealth"): Marx's own
  target, named as such, refuted in figures (`£100` and `£150` from the same
  £3), with North and Weingast's reading held open in the same paragraph.
- Lesson 7 ("concentration and centralisation are the same thing"): a
  misreading, refuted by `1/10` against `3/5`.
- Lesson 8 ("capital is a thing that can be exported"): refuted by `0`
  workers for hire beside £50,000 of things.
- Lesson 1 was the one that failed the test as written. Its title, "Thinking
  the first capitalists became so by saving", is a claim about what happened,
  and the body itself conceded that in its stronger form (Weber, Crouzet) it
  is a position the lab cannot refute. The title now names the plain form
  the tile does refute ("the first capitals were saved out of wages, as the
  legend's plain form says"), the body keeps the stronger form at strength
  and leaves it open, and the §C entry in PLAN.md is corrected to agree.

The second and third mistakes on each lesson are also misreadings (the zero
as "no surplus at all", the estate figure as a hiring count, a law lowering
the value of labour-power, the market and the wage bill as two sums, the
colony chapter as about the colonies), each refuted with the page's own
figure or the chapter's own sentence.

## The disputes, checked

Every factual claim about a historian was checked against the work named.
What stood, and what was corrected:

- **Weber 1905, Crouzet on the first industrialists.** Correct: Crouzet's
  founders came from the middling ranks and grew by ploughing back profits,
  and the lesson rightly says neither claims capital was saved out of wages.
- **Chambers 1953** (enclosure raised the demand for farm labour; the
  workforce came from population growth) and **Allen 1992** (enclosure added
  little to output and moved income to landlords): correct, and Allen is
  rightly placed "closer to Marx's". **Richards** on Sutherland: the lesson
  said he "questions some of the figures Marx took from his sources"; now
  says he treats several figures in the contemporary accounts as exaggerated
  and reads the plan as a resettlement to coastal fishing and crofting that
  failed, which is what he argues.
- **Davies 1966** on the 1547 statute: repealed by 1550 (the lesson had
  "within about two years"), barely enforced. Correct now. **Beier**'s
  *Masterless Men* works from arrest records and finds a real, growing,
  mostly young and mobile vagrant population, which partly supports Marx's
  picture of people on the road and partly undercuts the statutes' picture
  of idlers. The lesson had him treating the statutes "as evidence of what
  lawmakers feared"; now stated as he argued it, and the paragraph says the
  record of enforcement was uneven rather than absent. **Thorold Rogers** on
  the fifteenth-century labourer: correct.
- **Bodin 1568, Hamilton 1934, Kerridge 1953**: correct. **Outhwaite** and
  **Goldstone** were lumped together as the population-pressure account;
  Goldstone's argument is that population growth and urbanisation raised
  the velocity of the money there already was. Separated now.
- **Williams 1944, Engerman and O'Brien, Inikori 2002, North and Weingast
  1989, Dickson's "financial revolution"**: all correct, and the lesson's
  summary of Inikori (demand for manufactures, "not its profits alone") is
  the right one. The Bank of England's 8% in 1694 and the consols of 1751
  are correct.
- **Dühring, Engels 1878, Bernstein 1899, Popper**: correct. The defenders of
  Chapter 32 were "those who defend the chapter" with no name; Baran and
  Sweezy's 1966 argument that the giant corporation had become the typical
  unit of capital is now there, and the paragraph says the lab computes "a
  mechanism and none of the record".
- **Mill on systematic colonisation, Domar 1970, Thomas Peel 1829, South
  Australia 1836, the New Zealand Company**: correct. Marx's own gloss that
  Wakefield called slavery the natural basis of colonial wealth is in the
  text.

Nothing in the course reads as advocacy for or against Marx after the three
sentences repaired below; the course's own `how_to` sentence, "The lessons
present Marx's account; they do not ask you to accept it", is kept to.

## The voice, judged against §F and Course 1

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume I, Chapter n.</strong>` block and returns to it: "Then the
  joke… 'Never mind!', Marx writes" (lesson 1); "Read the two freedoms
  against each other" (lesson 1); "The phrase 'set free' is ironic" (lesson
  5); "Read the 150s from the other side and it is the same number" (lesson
  5). Lessons 2 and 3 move the chapter's most computable passage to the
  front and say so in `read_intro` ("The second half of the chapter, on
  wages, comes first, because it is the half the lab computes"), which is
  the right call for a chapter whose first half is a catalogue.
- **Scenes only where the object is in the reader's life.** Lesson 4 opens
  with "If you have ever paid a fixed rent or a fixed-rate loan through a few
  years of rising prices, you know the mechanism" and reaches the chapter in
  the same paragraph; lesson 3 says "Wage laws you may know are the reverse:
  a minimum wage is a floor" and then refuses to compute whether a floor
  helps. The other six open with the text, as §F rule 2 asks when a scene
  would have to be invented. No scene is forced.
- **History as story with people in it.** Thiers "defended property against
  the socialists of 1848 with this very tale"; Bacon's phrase read by Marx
  "as an unwitting statement of what capital needed the opposite of"; the
  Duchess "well instructed in economy"; Whitbread and Pitt; Bodin in 1568 as
  "the first statement of the quantity theory"; Mirabeau and the
  *manufactures réunies*; Wakefield in the 1820s; the two Peels. Every
  opponent is given his fact before Marx answers, as Course 1 does with
  Böhm-Bawerk and Hume.
- **Second person in `p` and `worked.intro` only.** "You have watched, over
  the last courses, money become capital"; "You want the working days
  needed". `steps`, `standard`, quiz items and tile text are impersonal
  throughout; no "Let's", no first-person anecdote.
- **One light remark, and Marx's before the lesson's.** "Then the joke"
  (lesson 1), "Marx's sarcasm is doing the arguing here" (lesson 2), "What
  grim irony!" (lesson 3), "a different Peel's fiasco" and "That is Marx's
  joke, and the lesson needs no other" (lesson 8). None is at the reader's
  expense.
- **The limit admitted.** Every `note` names what the lab cannot show, and
  the closing move is varied as the Course 1 review asked: "The lab cannot
  decide between them" (lesson 2), "The law's aim and the law's effect are
  two different questions" (lesson 3), "The lab takes the price index as
  given and does not choose" (lesson 4), "it cannot show that the change was
  forced" (lesson 5), "an argument about evidence that it cannot enter"
  (lesson 6), "The lab computes a mechanism and none of the record" (lesson
  7).
- **Pointing forward by title.** Every body ends with the next lesson's title
  and its question, and lesson 8 ends with The Circuits of Capital and "the
  forms of money, production and commodities that it must pass through again
  and again". None summarises.

## What the course teaches well

- **Objectives are acts and the drills measure them.** Every `standard`
  begins "Finish when you can…" and names the product; the six course
  `outcomes` are the same acts. The `assumes_long` is honest ("the working
  day, the rate of surplus value, wages, and simple and expanded
  reproduction") and every lesson uses only that.
- **The circle of Chapter 26 is set up as a circle.** Lesson 1 starts from
  "each step presupposes the one before it", gives Smith's previous
  accumulation its sentence, and places the thrift sum before the
  chapter's main point ("But the sum is not the chapter's main point"), which
  is the honest shape of the chapter.
- **The numbering note is where §C puts it.** `how_to[3]` explains that
  English Chapters 26 to 32 are the seven sections of German Chapter 24 and
  Chapter 33 is German 25, and that "so-called" is Marx's.
- **The seam at lesson 5 is invisible.** Lesson 4 ends by asking "where its
  workers, its materials and its customers came from"; lesson 5 finds
  "three things set free by the expropriation, beside the people
  themselves". Both modules spell British, cite lessons by title and
  chapters by number, and keep the same tile vocabulary.
- **The arithmetic is right.** `60,000 / (3/10) = 200,000`; `/300 = 666 2/3`;
  `12 − 6 = 6`, `× 3,000 = 18,000`; `12 × 3s / 6 = 6s`, `(6 − 2)/2 = 200%`,
  `(6 − 4)/4 = 50%`; `200 − 80 − 20 = 100`, `/2 = 50`; `200 − 60 − 20 = 120`,
  `/2 = 60`, `40 − 30 = 10`; `1 + 3/12 + 3/12 = 1½`, `× 100 = 150`;
  `3/(3/100) = 100`, `3/(2/100) = 150`; `1.1^5 = 1.61051`; `600/1000 = 3/5`;
  `2/(1/2) = 4`. Every quiz distractor is a named error and none could be
  argued for: the plain-wage divisor (5,000), the rent doubled with prices
  (£60), the interest added to £100 (£105), the absorbed capitals counted
  alone (3/8), the share inverted alone (4).
- **The chapter's own figures are the chapter's.** 3,511,770 acres;
  794,000 acres; 6,000 acres at two an acre; 29 sheep farms; 131,000 sheep;
  2s 7½d for London tailors; £6,000,000 between 1757 and 1766; Liverpool's
  15 ships in 1730 and 132 in 1792; 80,000 to 18,000 at Banjuwangi; 8% in
  1694; £50,000 and 3000 persons: every one is in the text where the lesson
  says it is.

## What it taught badly, or said wrongly

### Verdicts on Marx

- **`the-secret-of-primitive-accumulation`, body:** "The legend deserves a
  fairer hearing than Marx gives it" judged Marx unfair. Now "The legend has
  holders more serious than Marx's parody allows, and it should be heard at
  strength", which says what the paragraph does without grading the author.
- **`the-industrial-capitalist`, body:** "His account of how the debt works
  is precise" endorsed it. Now "specific".
- **`the-home-market`, body:** "'set free' is ironic, and it is also exact"
  endorsed it. Now "and Marx also means it literally".

### Fidelity

- **`expropriation-from-the-land`, body:** "In the fifteenth century, Marx
  writes, serfdom had practically disappeared in England" conflated two
  sentences; Marx dates the disappearance to "the last part of the 14th
  century" and the free peasant majority to the fifteenth. Now says both.
- **`bloody-legislation`, body:** "Elizabeth and James I kept the whipping
  and added branding." Branding was already in 27 Henry VIII (half the ear)
  and Edward VI's statute (S and V with a hot iron). Now "kept the whipping
  and the branding, and death for the third offence", which is what the two
  statutes add.
- **`bloody-legislation`, `concepts[0]`:** "From Henry VIII to James I" where
  Marx says the legislation "began under Henry VII", and "people without work
  were… executed for being without work" repeated itself. Now "From Henry
  VII to James I… for it".
- **`the-industrial-capitalist`, body:** "The Dutch in Java ran a system of
  stealing men for slaves"; the men were stolen in Celebes "to get slaves for
  Java". Now says so.
- **`the-modern-theory-of-colonisation`, body:** "In the closed preset land
  cannot be had at all", but the preset sets `land_price_years` 2 and
  `saving_share` 0, so what the model holds is that the worker saves
  nothing. Now "the worker can save nothing, so land at any price is out of
  reach", which is what the tile `never` computes.

### Historians stated loosely

- **`bloody-legislation`:** Beier and Davies, as above. "The only floor ever
  proposed in the period" (a claim no one can make) is now "the one floor
  Marx records being proposed".
- **`the-capitalist-farmer`:** Goldstone separated from the population-
  pressure account, as above.
- **`the-historical-tendency`:** the defenders of Chapter 32 now have a
  name and a date (Baran and Sweezy, 1966).
- **`the-home-market`:** "Adam Smith argued that the market grows with the
  division of labour" reversed Smith's famous direction (the division of
  labour is limited by the extent of the market). Now "tied the market to
  the division of labour, each extending the other".

### Misconception as history

- **`the-secret-of-primitive-accumulation`, `mistakes[0]`** and PLAN §C
  entry 5.1, as above.

### Speech

Every math run on the nine pages was read from `data-say`. All read
correctly: `60, 000 over the quantity 3 over 10, equals 200, 000`, `pounds 3
over the quantity 3 over 100, equals pounds 100`, `2 over the quantity 1 over
2, equals 4 years`, `s over v equals the quantity value made minus wage, over
wage`. No key line begins with a three-letter word. Two shapes were improved:
`keeps = product·p − wages·w − rent` read "product times p minus wages times
w", single letters a listener cannot place, and is now `keeps = product −
wages − rent, at new prices`; and the prose run `100 × 1s 6d = 150s a day`
was split by the islands pattern so that it read "100 times 1 s 6 d equals"
and stopped, and is now "a hundred wages of 1s 6d, 150s a day".

### Cross-references

Lessons are cited by title and each exists: “Machinery and the Displaced
Worker” and “Simple Reproduction” (the carpet factory's £3,000 and the
£1,000 consumed in 5 years are both Marx's, from Chapters 15 and 23 as the
`note` says), “The General Law of Capitalist Accumulation” (for the
definitions of concentration and centralisation), the next course The
Circuits of Capital, and Merchant's Capital and Interest for the rate of
interest. Marx's chapters are cited by volume and number throughout, as §0's
first deviation requires.

## Can a reader who has finished Wages and Accumulation follow it?

Yes. The course asks for nothing it was not given: the working day split
into necessary and surplus labour (lessons 2 and 3), the rate of surplus
value (lessons 2 and 3), the value of labour-power as a day's subsistence
(lessons 3 and 5), simple reproduction's £1,000 (lesson 1), and
concentration and centralisation from Chapter 25 (lesson 7). The two places
a reader will slow down are the two the lessons prepare for: the two senses
of "free" in lesson 1, which the quiz tests with four people (a serf, a
peasant-proprietor, a loomless weaver, a hired-out slave), and
"capitalise" in lesson 6, which the `def` and the `note` define locally and
the quiz tests twice before asking for the four levers. Lesson 7's reading
of "the negation of the negation" is given in Marx's words and then
Dühring's, Engels's, Bernstein's and Popper's, which is as much as a first
reading can carry; no lesson pretends the knell is computed.

## Repairs made in this pass

In `content/capital/c05_primitive/part_a.py`:
`the-secret-of-primitive-accumulation` the Weber paragraph's first sentence
and `mistakes[0]` title and first clause; `expropriation-from-the-land` the
fourteenth-century sentence and the Richards sentences; `bloody-legislation`
`concepts[0]`, the Elizabeth sentence, the Davies–Beier paragraph and
`mistakes[0]`; `the-capitalist-farmer` `key[1]` and the Outhwaite–Goldstone
sentences. In `part_b.py`: `the-home-market` the "set free" sentence, the
wage-bill run and the Smith sentence; `the-industrial-capitalist` the
Celebes sentence and "precise"; `the-historical-tendency` the defenders
sentence; `the-modern-theory-of-colonisation` the `closed` preset sentence.
In `docs/capital/PLAN.md`: the Misconception line of §C entry 5.1. No
preset, `expect`, slug, module, lab key, mode or view changed; every
instance the lessons carry is the one §C records.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-primitive-accumulation` reports OK: 9 pages, every lab executes and
survives the sweep, 8 pages with pinned figures and 0 failing, no math run
without a spoken form; the strict quotation checker reports 99 segments, 0
misses.

## Remaining issues

- **The Peel figure.** The Kerr text prints "3000 persons" and the lesson's
  `note` says the 1887 Moore–Aveling printing reads 300, as PLAN §C records.
  Wakefield's own figure and the historical party were nearer three hundred;
  the lesson follows §E.3 (one source) and says the point does not depend on
  which. A reader who checks the Penguin will find 300; the `note` already
  warns. Not changed.
- **The `thrift` and `statute` labs compute direction only.** Both say so;
  both refute a stated misreading. They remain the two labs on the course a
  sceptic could call decoration, and a future kit view that let the `thrift`
  lab show simple reproduction beside the saving (the `regress` preset §C
  originally asked for) would make lesson 1's comparison a tile rather than
  a sentence. Recorded; the kit is not mine to change.
- **Marx's own history is not tested against Marx's sources.** The course
  `not_covered` says Eden, Price, Somers and the rest "appear where Marx
  quotes them" and that their reliability "is touched on only where a
  lesson's dispute turns on it". That is the right scope for a read-along,
  but it means the Sutherland figures reach the reader as Marx's with one
  historian's caution beside them. Enough for this course; a reader wanting
  the clearances themselves needs Richards, and the lesson names him.
- **The speech engine groups digits with a pause** (`3, 000`, `60, 000`).
  That is the engine's convention across the library, not a defect of this
  course, and is recorded here only so no one tries to fix it in content.
