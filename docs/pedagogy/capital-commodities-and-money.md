# Pedagogy assessment — Commodities and Money (Capital, course 1)

Formed from the eight lesson dicts in `content/capital/c01_commodities/`
(`part_a.py`, lessons 1–4, one per section of Volume I, Chapter 1; `part_b.py`,
lessons 5–8, Chapter 2 and three lessons on Chapter 3; `__init__.py`, the course
dict), and the kit they render through (`scripts/mathpath/labs/capkit.py`,
modes `value`, `form`, `money`; views `snlt`, `skill`, `ledger`, `stage`,
`count`, `circulate`, `payments`, `world`), on branch `feat/capital-subject`
before the Subject was wired into the site. The design authority is
`docs/capital/PLAN.md` §0 (the one question), §B, the Course 1 entries in §C,
§D as summarised in `docs/capital/kit-a-report.md`, §E (how a passage is
quoted) and §F (the voice). This course is the voice reference for the
thirteen that follow, so the voice is judged in more detail than usual.

Every lesson was read in full before anything was changed. Every pinned tile
was read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py capital --course
capital-commodities-and-money`), every figure in prose was recomputed by hand,
and every quotation and every phrase in quotation marks (eighty-five of them)
was searched for character by character in
`/mnt/project-files/capital-texts/volume-1-kerr.txt`, the Kerr text §E.3
makes the Subject's only source. Every math run on the nine rendered pages was
read from its `data-say`. Lessons, in course order:
`the-two-factors-of-a-commodity`, `the-twofold-character-of-labour`,
`the-form-of-value`, `the-fetishism-of-commodities` | `exchange`,
`money-as-measure-and-means-of-circulation`, `hoards-and-means-of-payment`,
`world-money`. The bar marks the seam between the two modules. The course
assumes nothing but school arithmetic and is judged against that.

## Verdict

The course teaches its subject, and it is fit to be the voice reference. A
reader who finishes it can compute socially necessary labour-time per unit from
several producers' hours and outputs and say how much of a slow producer's time
his product does not carry, separate the use-value side of a change in
productivity from the value side, read `20 yards of linen = 1 coat` and name
which commodity is speaking, write the expanded, general and money forms,
compute a ledger of hours and say in which settings the producers can read it,
count the ratios a market needs with and without one equivalent, price
commodities in gold and compute the money a day's sales need at a velocity, net
a circle of debts and recompute when one is unpaid, and settle a balance of
payments in bullion. Those are the acts the `standard` fields name and the
quizzes measure; no objective is "understand X". The `mistakes[0]` of every
lesson is the §C misconception, each refuted with a tile: `11/5` hours against
weaver C's 5, the day's output at `10 h` whether it is one coat or two, the
coat's new value of `10 h` appearing nowhere in `20 yards linen = 2 coat`, the
goat worth 10 fish on the island and in the village alike, the same `5` ratios
for cattle or gold, prices doubling to `£4` because gold's value halved, `£100`
of hard cash where no commodity changes hands, `£200` crossing the border as
metal. All 47 pinned tile strings on the eight pages matched the lab, and every figure
quoted in prose agreed with the lab or with a recomputation.

Fidelity to the chapter is high. Eighty of the eighty-five quoted phrases
were found verbatim in the Kerr text; four differ only in a line break, an initial capital
or a quotation mark the §E.3 convention converts. One was not in the text at
all: `money-as-measure-and-means-of-circulation` had Marx dismiss Hume's
quantity theory as "a one-sided observation", words that occur nowhere in the
chapter, and had Marx argue with Hume by name, when Hume is named only in a
footnote beside Vanderlint and Barbon. That is repaired below with Marx's
actual sentence. Marx is presented, not endorsed: Böhm-Bawerk, the
marginalists, Bailey, Say, Locke and Montesquieu, Hume and the mercantilists
each get two or three sentences at full strength before Marx answers, and
every `note` names what the lab cannot settle. The remaining defects were
local: a preset the prose never explained, a quiz distractor a reader could
argue for, three key lines the voice spelled out letter by letter, one
enumeration of Marx's cases that did not match his, and one paragraph where
the course's strongest critic was missing from the lesson his criticism most
concerns. Nothing needs splitting, merging or reordering within the URL space
the course has; one split is recorded under remaining issues.

## The voice, judged against §F

This course sets the register for thirteen more, so what works is named as
concretely as what does not.

**What works, and should be copied:**

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume I, Chapter n, §m.</strong>` block and then returns to it a
  few words at a time: "Read the answer phrase by phrase. 'Normal conditions
  of production' means… 'The average degree of skill and intensity' rules
  out… And 'prevalent at the time' means the standard moves"
  (`the-two-factors-of-a-commodity`); "Take the equation as a sentence. Its
  subject is the linen" (`the-form-of-value`); "Every local garb in that list
  is something earlier lessons built. The standard of price was… Coin was…
  Tokens and paper…" (`world-money`). This is §F rule 1 done exactly, and the
  `read_intro` fields say which passage is coming and why.
- **Scenes only where the object is in the reader's life.** "Look around the
  room you are in. Nearly everything in it was bought" (lesson 1); "A coffee
  costs what it costs, the way it weighs what it weighs, and the people who
  grew, shipped and roasted it are nowhere in the number" (lesson 4); "Every
  price you have ever read is this function at work" (lesson 6); "Rent is paid
  at the end of the month for a flat you have already lived in; a supplier
  delivers now and sends an invoice due in thirty days" (lesson 7). Each
  reaches the chapter's category within the paragraph. `the-form-of-value` and
  `exchange`, whose objects are not in anyone's life, open with the text
  itself, which is what §F rule 2 asks when a scene would have to be invented.
- **The history of ideas as story with people in it.** Petty is "the
  seventeenth-century physician who surveyed Ireland and wrote some of the
  first English economics"; Böhm-Bawerk "argued in 1896 that Marx's process of
  elimination is rigged"; Bailey's 1825 *Critical Dissertation* is "a serious
  position, and close to how most economists still talk about relative
  prices"; Aristotle "got remarkably far with this… Then he stopped"; Hume's
  1752 essay "fits what people saw after the American silver and gold flowed
  into Europe"; Mun's view "was not foolish" in a world where only bullion
  settled accounts; Sedley Taylor is the Cambridge fellow who, months after
  Marx's death, accused him of falsifying a quotation. Every opponent is given
  the fact his view rests on before Marx replies. This is §F rule 3 and the
  "presented, not endorsed" rule at once.
- **Second person, warm, in `p` and `worked.intro` only.** "You want the value
  of 20 yards, and what weaver C loses on each of his" is the shape every
  worked intro takes. `steps`, `standard`, quiz items and tile text stay
  impersonal throughout; no "Let's", no "dive in", no first-person anecdote
  anywhere in the course.
- **One light remark, and Marx's before the lesson's.** Lesson 4 points at
  Marx's séance joke ("table-turning") and at Sedley Taylor and calls the
  latter "the closest the section comes to a smile"; lesson 5 names "a dry
  joke in the first sentence" of Chapter 2 and explains it; lesson 7 quotes
  Marx "at his most sardonic" about the hoarder. None is the lesson's own
  invention and none is at the reader's expense.
- **The limit admitted.** Every `note` names the one thing the lab cannot
  show: the weighted average is "a model of Marx's 'normal conditions', not
  his definition"; the skill multiplier "would be assuming the number it
  printed"; the form lab "cannot show the qualitative point of the section";
  the ledger "sees quantities and not appearances"; the count "shows why one
  equivalent is needed, and nothing more"; the circulation lab "cannot decide
  between that direction and Hume's, because both read the same correlation".
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson's question by the next lesson's title, and `world-money` ends
  with the next course by title and its question ("how money laid out can
  come back as more money"). None summarises, none says "next week".

**What to change in the courses that follow (and what was changed here):**

- **Do not quote Marx from memory.** The one fabricated phrase on the course
  ("a one-sided observation") was a plausible paraphrase of a footnote's sense
  that acquired quotation marks. §E.3 says quote by search; the rule should be
  read to cover every phrase in `&ldquo;…&rdquo;`, not only the opening
  passage. Eighty-five were checked here and one was invented; at that rate
  the Subject would ship fifteen or so.
- **When a preset is on the page, the body must say what it shows.** The
  `power-loom` preset in lesson 1 was labelled with Marx's example and never
  mentioned in the prose, so a reader who had just read that a hand-loom
  weaver's hour "represented only half an hour's social labor" pressed the
  preset and saw `6/5 h`, a figure the lesson nowhere connects to the
  sentence. Repaired below; the rule for later authors is that every preset
  id appears in a body paragraph with its figure and what it is a figure of.
- **Name the standard objection in the lesson it concerns, not only the first
  time.** Böhm-Bawerk appears in lesson 1 against the abstraction argument,
  but his best-known point, that the reduction of skilled to simple labour is
  circular, belongs to lesson 2, where the lesson discussed the multiplier
  for a paragraph without him. Added below.
- **Short words at the head of a key-line equation are spelled out.** `due`,
  `out` and `use-value` at the start of a run read as "d u e", "o u t" and
  "u s e-value". Key lines that are equations should start with a word of
  four letters or more, or with the quantity's full name.
- **Math in `steps` goes in backticks**, as every other Subject writes it; a
  plain `n·(n − 1)/2` in a step is split at its spaces by the islands pattern
  and read as "n times n minus".
- **"This Subject does not settle that dispute"** appears, in slightly
  different words, at the end of two critics' paragraphs (lessons 1 and 4).
  Once a lesson is right; once a course would be better. Later courses
  should vary the move or let the `note` carry it.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names the product: a lot valued
  from several producers' hours, "and how much of one producer's own time per
  unit the product does not carry" (lesson 1); value per unit and of the
  period's output, "and which of the two moved" (lesson 2); the relative and
  equivalent forms named, the movement computed, the four forms written
  (lesson 3); hours per unit and a ratio, "and for a given setting whether the
  producers see the hours or only the ratio" (lesson 4); both counts, and
  "what sets one commodity apart as money" (lesson 5); prices, the sum and the
  money needed, "again after a change in gold's value or in the velocity"
  (lesson 6); money needed with credit, and the cash a chain of bills needs
  "again when one is not paid" (lesson 7); the bullion shipped, its direction
  and its function (lesson 8). The six course `outcomes` are the same acts.
- **One hard idea per lesson, and the four sections of Chapter 1 kept apart.**
  Lesson 1 carries value and socially necessary time and nothing of the form;
  lesson 2 carries only the two sides of labour and refuses to compute the
  skill multiplier; lesson 3 carries the equation and its forms and says the
  qualitative point is in the prose; lesson 4 does "no new arithmetic" and
  says so in its `concepts_intro`. The `how_to` warns that Chapter 1 is slow
  and tells a reader who loses "The Form of Value" to read "The Fetishism of
  Commodities" and come back, which is good advice.
- **The misconceptions are refuted with the specific figure.** Weaver C's yard
  "is worth `11/5` hours, the same as everyone's", and "of his 40 extra hours
  his own yards carry 8" (lesson 1). The doubled preset "refutes it in one
  line: the day's output goes from 1 coat to 2 and stays worth 10 hours"
  (lesson 2). The coat's new value "of 10 hours appears nowhere in" the
  equation (lesson 3). "Weight would stay with the goat if every person
  vanished; its value would not" (lesson 4). "It is the same 5 ratios for
  cattle or gold, so nothing in the convenience of an equivalent decides which
  commodity it is" (lesson 5). "Prices double to £4 and the money needed
  doubles to £4 because the prices did" (lesson 6). "No commodity changes hands
  at all, and yet £100 of hard cash is needed" (lesson 7). "The £200 does not
  cross the border as pounds" (lesson 8).
- **The arithmetic is right, and the lab's model is kept apart from Marx's
  definition.** `40·1 + 40·2 + 20·3 = 180` over `100` is `9/5`; `220/100` is
  `11/5`; C's 20 yards go from 36 to 44 hours, 8 of his 40 extra, the other 32
  over the 80 yards he did not make (`80 · 2/5 = 32`); with A and B halved,
  `20 + 40 + 60 = 120` over `100` is `6/5`. The lesson says, three times, that
  the output-weighted average is the lab's stand-in for "normal conditions"
  and not the definition, and the `note` cites Volume III, Chapter 10 for a
  regulating value that is not the mean. The money lessons say which figures
  are Marx's (£2 each, velocity 4, the four commodities, the Lyons virements,
  A–B–C) and which are illustrative (every hour, every £100 bill).
- **Worked example, faded guidance, independent practice.** Every worked
  example is the first preset by hand; every `panel_intro` asks for a
  prediction before the press ("compare weaver C's own hours per yard in the
  table with the socially necessary time in the tile"; "watch the two tiles:
  one moves with productivity, the other does not"; "Compare the gold-falls
  preset with Marx's: only gold's value changed"); every quiz asks the same
  act on a fresh instance (two weavers at 2 and 4 hours; five commodities at
  £3 and five moves; a circle of £50 debts with B defaulting). The distractors
  are the named errors: the plain average of 2 and 4 (3 hours) against the
  weighted one (`5/2`); `£15` for "sold at once" against `£3`; `£150` for
  "each debt paid in coin" against `£0`.
- **The chapter's own figures are the chapter's.** The expanded form's list
  (`1 coat`, `10 lb tea`, `40 lb coffee`, `1 quarter corn`, `2 ounces gold`,
  `½ ton iron`) is Marx's in his order; the four cases of relative value are
  his; `£2` for "nearly ½ oz. of gold" is his, so `¼` and `1/8` of an ounce in
  the paper-money paragraph are his; the Bible, the brandy, the weaver "of the
  good old stamp", the "salto mortale", the sheriff, "money alone is a
  commodity!", the double current of gold, bank reserves as "an indication of
  stagnation" are all in the text where the lessons say they are.
- **Marx's opponents are stated at strength and his critics are named.**
  Böhm-Bawerk's elimination objection and the marginalists' alternative in
  lesson 1 ("with no labour content behind them at all"); Bailey against any
  absolute value in lesson 3; Jevons and Menger again in lesson 4 ("nothing
  lies behind it to be uncovered"), with Lukács on the other side; Locke and
  Montesquieu with "a fact Marx accepts: coins wear thin and keep circulating"
  in lesson 5; Say's followers in lesson 6; Hume with the American silver
  behind him; Mun with the gold-settled world behind him. Each is followed by
  Marx's reply as a reply, and the course `how_to` and `not_covered` say the
  verdict is not the lesson's to give.
- **The seam at lesson 5 is invisible.** `the-fetishism-of-commodities` ends
  "they cannot walk to market by themselves"; `exchange` opens "Chapter 2
  opens by pointing out that they cannot walk" and recalls "coats acting as
  mirrors and commodities talking about themselves". Both modules spell
  British, cite lessons by title and chapters by number, use the same
  `<strong>Volume I, Chapter n.</strong>` block, and keep the same tile
  vocabulary.
- **Figures agree with the lab.** Every pinned tile on the eight pages matched
  the observed tile: `9/5 h`/`36 h`, `11/5 h`/`44 h`, `6/5 h`/`24 h`;
  `10 h`/`10 h`, `5 h`/`10 h`, `20 h`/`10 h`; `20 yards linen = 1 coat`,
  `= 2 coat`, `= 2 ounces gold`; `40 h`, `120 h`, `160 h` with `goats 5 h,
  fish 1/2 h, furniture 6 h, tools 3 h` on all three; `6`/`3`, `15`/`5`,
  `15`/`5`; `£8`/`£2`, `£8`/`£8`, `£16`/`£4`, `£8`/`£1`; `£300`/`£0`,
  `£0`/`£0`, `£100`/`£100`; `£0`, `£200 out`, `£300 out`. The ledger table's
  last column is "units of goats it equals", as the `panel_intro` says.

## What it taught badly, or said wrongly

### Fidelity

- **`money-as-measure-and-means-of-circulation`, body:** "Hume's reading, he
  says, came from 'a one-sided observation' of the same facts." No such phrase
  is in Chapter 3; the only "one-sided" in the chapter is the "one-sided
  metamorphoses" of §2(b) and the weaver whose labour is "one-sided". Hume is
  not named in the chapter's text at all; footnote 88 quotes Vanderlint, says
  Hume "made use of Vanderlint's work", and adds that "the opinion that prices
  are determined by the quantity of the circulating medium, was also held by
  Barbon and other much earlier writers." What Marx says in the text is that,
  given the sum of values and the velocity, "the quantity of precious metal
  current as money depends on the value of that precious metal", and that the
  contrary opinion "was based by those who first beheld it, on the absurd
  hypothesis that commodities are without a price, and money without a value,
  when they first enter into circulation." Repaired: the paragraph now quotes
  those two sentences and says the footnote names Hume after Vanderlint and
  Barbon. The `mistakes[0]` title and the §C misconception ("as Marx frames
  it, against Hume and Ricardo") stand: footnote 117 of the same chapter
  names Ricardo's "erroneous dogma" on the same point.
- **`__init__.py`, `how_to[1]`:** "Marx said himself that beginnings are
  difficult" paraphrased the preface's "Every beginning is difficult, holds in
  all sciences." Now quotes it.
- **`the-form-of-value`, body:** "Marx takes four cases. If the linen's value
  doubles… If the coat's value doubles… If both change in the same
  proportion… And the case the lab is built around" listed four instances
  that are not Marx's four cases (I. the linen varies; II. the coat varies;
  III. both vary alike; IV. both vary differently); a reader following in the
  book would look for a fourth case and find the lab's inside the second. Now
  names his four and places the coat-halves instance "inside the second
  case".
- **`the-two-factors-of-a-commodity`, `concepts[0]`:** "whether the want
  'spring from the stomach or from fancy'" was ungrammatical around the
  quotation (Marx's subject is plural). Now "whether such wants".

### Prose that left the lab, or the reader, unexplained

- **`hoards-and-means-of-payment`, `note`:** the `broken` preset sets
  `payments_due` to 200 against the `chain` preset's 300, counting the unpaid
  bill as no longer falling due so that the formula returns the `£100` the
  netting of the bills returns; nothing on the page said so in words, and a
  reader comparing the two presets' inputs would see a figure change with no
  reason given. One sentence added to the `note`.
- **`the-two-factors-of-a-commodity`, body:** the `power-loom` preset,
  labelled "Power-looms: weavers A and B at half their hours", had no sentence
  in the body. Its tile, `6/5 h`, is not the "half an hour" of Marx's
  sentence two paragraphs above it, because only two of the three weavers
  halve their time; on the instance, C's hour falls from `3/5` to `2/5` of a
  social hour, two-thirds and not half. One paragraph added saying exactly
  that, and that Marx's own case, in which the whole trade halves its time,
  gives exactly half. The §C instance is unchanged.
- **`the-twofold-character-of-labour`, body:** the paragraph on "multiplied
  simple labour" said the book never computes the multiplier and stopped.
  Böhm-Bawerk's objection, that the only evidence for the ratio is the
  exchange ratio of the products, which the reduction was meant to explain,
  is the standard one and belongs here. Two sentences added, with the
  chapter's own answer quoted ("are established by a social process that goes
  on behind the backs of the producers").

### Quiz

- **`exchange`, quiz 4, distractor 4:** "Trading with no equivalent at all"
  was offered as a change that alters the tiles, and the `why` said it "is
  what the barter tile already counts". But trading with no equivalent
  changes no input of the lab, so a reader could argue it leaves both tiles
  unchanged, which is the keyed answer's property. Replaced with "Taking the
  cattle out of the market altogether", which drops `n` to 5 and both tiles
  to `10` and `4`; the `why` says so. Every other distractor on the course
  was argued for and could not be defended: the plain average, `£15`,
  `£150`, `20 hours` for two coats at the old value, "the coffee's" in
  `10 lb of tea = 40 lb of coffee`, and the rest.

### Speech

Every math run on the nine rendered pages was read from `data-say`. The
`capkit` figures read well: `9 over 5`, `11 over 5`, `n times the quantity n
minus 1, over 2`, `C to M to C`, `M to C to M prime`, `pounds 8 over 4 equals
pounds 2`, `5 over the quantity 1 over 2, equals 10 fish`. Four shapes read
wrongly, none flagged by the checker because each is all words, and all four
were repaired in the content rather than with spoken forms, since other
authors are writing to `content/spoken/capital.py` concurrently:

- **Three-letter words at the head of a key equation read as letters.**
  `use-value: a useful thing, by its body` read "u s e-value", `need = prices
  − credit + due − cancelled` read "d u e", `out = imports − exports − other
  receipts` read "o u t". Now `a use-value: …`, `need = prices − credit +
  payable − cancelled` and `bullion out = imports − exports − receipts`
  (which is also the course `key`'s wording). Lesson 2's `concrete labour
  makes use-values` was already read correctly, which is how the rule was
  found.
- **`cwt.` read "cwt,".** The run `1 quarter corn = x cwt. iron` is Marx's
  notation but not a quotation; now `x hundredweight iron`.
- **Plain math in `steps` split at its spaces.** `n·(n − 1)/2` and `n·(n − 1)`
  in `exchange`'s steps read "n times n minus" twice. Now in backticks, as
  the other Subjects write math in steps.

### Cross-references

Lessons are cited by title (“The Twofold Character of Labour”, “The Form of
Value”, “The Fetishism of Commodities”, “Exchange”, “Money as Measure and
Means of Circulation”, “Hoards and Means of Payment”, “World Money”), each
title exactly as the next lesson carries it; Marx's chapters by volume and
number, as §0's first deviation requires; the next course by its §B title,
From Money to Surplus Value. Volume III, Chapter 10 is cited in lesson 1's
`note` for the regulating value, which is where Marx discusses it. No lesson
is cited by number.

## Can a first-time reader of Chapter 1 follow the four lessons?

Yes, with the help the course already gives, and the places a reader will
slow down are the places Marx's readers slow down.

- **Lesson 1** moves from a room full of bought things to the opening
  sentence, from the obvious factor to the turn ("Then the turn"), gives the
  abstraction argument in six sentences with its one equation, and then,
  before the definition, gives Böhm-Bawerk's objection. That order is right:
  a reader who has just been told value is labour is forming the objection
  and is told at once that it has been made by someone serious. The
  socially-necessary definition arrives as Marx's answer to "the objection
  you are probably already forming", which is the honest shape of §1, and the
  "phrase by phrase" paragraph is the best single paragraph on the course.
  The one gap, the power-loom preset, is closed.
- **Lesson 2** is the lightest of the four and is correctly light. Its one
  move, that the same hours give the same value at any productivity, is made
  with one tailor and three presets, and the coat-against-linen paragraph
  ("a coat is worth 5 hours and so only 10 yards") hands the reader exactly
  the fact lesson 3's `coat-cheapens` preset will compute. A reader who has
  not met Smith and Ricardo is told in two sentences who they were.
- **Lesson 3** is where readers give up, and the lesson says so in its second
  paragraph and says what the section is for before doing it ("turn a coat
  over as long as you like and you will not find its value"). It then takes
  the equation "as a sentence", which is the right first move for a reader
  who has never seen `=` mean anything but arithmetic, and reads it
  backwards to show the roles swap. The four cases are now Marx's four. The
  expanded, general and money forms are given one paragraph and the lab's
  `foStage` select, which rewrites the equations before the reader's eyes;
  that is enough for a first reading, and the `note` says what the lab
  cannot show. What a first-time reader will still miss is the three
  "peculiarities" of the equivalent form (use-value becomes the form of
  value, concrete labour the form of abstract labour, private labour the form
  of social labour), of which the lesson gives only the first in its own
  words. That is a deliberate choice for cognitive load and is recorded
  below, not repaired.
- **Lesson 4** is the easiest to read and the hardest to compute anything
  for, and the lesson is honest about both: "It does no new arithmetic." The
  coffee paragraph gives the reader the experience before the word, the
  table-turning paragraph gives Marx's joke and the argument in one, and
  Robinson's ledger is used for what Marx uses it for, a place where the
  hours are not hidden. The quiz's fourth item asks what the lab cannot show,
  which is the section's point, and is the right question to end on.

The course also protects the reader in two ways later courses should keep:
the `how_to` names "The Form of Value" as the hardest lesson and gives a
route around it, and every lesson says which hours are illustrative, so a
reader never mistakes the lab's three weavers for a claim about weaving.

## Repairs made in this pass

In `content/capital/c01_commodities/__init__.py`: `how_to[1]`. In `part_a.py`:
`the-two-factors-of-a-commodity` `key[0]`, `concepts[0]`, the `1 quarter corn`
run, the lab paragraph (the power-loom sentences);
`the-twofold-character-of-labour` the multiplied-simple-labour paragraph
(Böhm-Bawerk); `the-form-of-value` the four-cases paragraph. In `part_b.py`:
`exchange` `steps[1]`, `steps[2]`, quiz 4 distractor and `why`;
`money-as-measure-and-means-of-circulation` the Hume paragraph;
`hoards-and-means-of-payment` `key[2]` and `note`; `world-money` `key[2]`. No preset,
`expect`, slug, module, lab key, mode or view changed, and no §C entry needed
correcting: every instance the lessons carry is the one §C records, and the
one change to how a preset is explained (the power-loom) is to prose, not to
the instance.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-commodities-and-money` reports OK: 9 pages, every lab executes and
survives the sweep, every pinned figure on the eight pages matches, no math
run without a spoken form; and a second pass over every `data-say` on the
nine pages finds no spelled-out word, no "cwt", and no split step.

## Remaining issues

- **`the-form-of-value` would be two lessons.** The elementary form with its
  two poles, the equivalent's peculiarities and the four quantitative cases
  are one hard idea; the expanded, general and money forms are another, and
  Marx gives them half the section. PLAN §B puts §3 under one slug. The
  natural split is "The Elementary Form of Value" / "From the General Form to
  Money", which the URL space does not have. Not done; recorded for the
  orchestrator.
- **The three peculiarities of the equivalent form** are given only in the
  lesson's own words for the first ("being exchangeable looks like a property
  of the coat"). The second and third (concrete labour counting as abstract,
  private labour counting as social) are what lesson 4's fetishism rests on,
  and a reader who reaches lesson 4 has not been told them. A `def` block
  naming all three would fit the split above; in the present lesson it would
  push the body past the load it can carry. Recorded, not changed.
- **The speech engine spells short words at the head of an equation.** `due`
  and `out` and `use` are not variables anywhere in this library's key lines,
  yet the engine reads them as letter groups when they open or follow `=` in
  a run. The three cases here were reworded; the next course whose key line
  begins `s = …` or `day = …` is safe (single letters and four-letter words
  read correctly), but one beginning `tax =` or `net =` will not be. A
  `speech.py` rule that treats a word of three letters as a word when it is
  in the engine's common-word list belongs to the chrome-renderer tier.
  Recorded, not changed.
- **The form lab prints `2 coat`** where Marx and the prose write "2 coats";
  the `foRelative` tile pluralises nothing. Harmless on this course (the
  `mistakes[0]` body writes "2 coats" and the pinned string is the lab's),
  and a kit change was not made.
