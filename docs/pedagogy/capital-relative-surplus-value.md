# Pedagogy assessment — Relative Surplus Value (Capital, course 3)

Formed from the nine lesson dicts in `content/capital/c03_relative/` (`part_a.py`,
lessons 1–5: Chapters 12, 13 and 14 and the first two of three lessons on
Chapter 15; `part_b.py`, lessons 6–9: the third lesson on Chapter 15 and the three
chapters of Part V; `__init__.py`, the course dict), and the kit they render
through (`scripts/mathpath/labs/capkit.py`, modes `workday`, `machine` and
`surplus`; views `relative`, `cooperate`, `detail`, `adopt`, `intensity`,
`displace`, `classify`, `three`, `formulae`), on branch `feat/capital-subject`
before the Subject was wired. The design authority is `docs/capital/PLAN.md` §0,
§B, the Course 3 entries in §C, §D as summarised in `docs/capital/kit-a-report.md`,
§E and §F; the author's brief is `docs/capital/AUTHORING.md`, and the model for
this document is `docs/pedagogy/capital-commodities-and-money.md`, whose course is
also the voice reference.

Every lesson was read in full before anything was changed. Chapters 12, 13, 14,
16, 17 and 18 of `/mnt/project-files/capital-texts/volume-1-kerr.txt` were read
whole; of Chapter 15, sections 1, 2, 3, 4, 6 and 7 were read whole and sections 5,
8, 9 and 10 at the passages the lessons lean on (the ribbon-loom and the
Luddites, Smith's 48,000 needles, the education clauses, the soil and the
labourer). Every pinned tile on the nine pages was read off the rendered page
with `node scripts/labcheck.js --observe` through
`scripts/preview_subject.py capital --course capital-relative-surplus-value`;
every figure in prose, worked example and quiz was recomputed by hand; and every
phrase in `&ldquo;…&rdquo;` (ninety segments before this pass, ninety-seven
after it) was searched for character by character in the Kerr text with the
strict checker. Every `data-say` on the nine pages was read. Lessons, in course
order: `the-concept-of-relative-surplus-value`, `co-operation`,
`division-of-labour-and-manufacture`, `machinery-and-the-value-it-transfers`,
`machinery-and-the-worker` | `machinery-and-the-displaced-worker`,
`absolute-and-relative-surplus-value`, `price-of-labour-power-and-surplus-value`,
`formulae-for-the-rate-of-surplus-value`. The bar marks the seam between the
two modules, which falls inside Chapter 15. The course assumes From Money to
Surplus Value and is judged against a reader who has it.

## Verdict

The course teaches its subject, and after the repairs below it is fit to ship
with Course 1. A reader who finishes it can compute the rate of surplus value
when the necessaries cheapen and a fixed day's necessary part shrinks, and a
pioneer's extra surplus value before competition removes it; the constant
capital in each unit when means of production are shared and the combined
working day of twelve masons or a hundred harvesters; the workers each detail
operation needs for a manufacture to balance and the smallest shop with nobody
idle; the value a machine passes to each unit and the verdict of society's test
and the capitalist's; the labour in a day of given length and intensity and the
rate when ten denser hours replace twelve; the capital a machine sets free and
the most men its construction could employ; the classification of a change in
the day as absolute, relative or both; Marx's four cases for length, intensity
and productivity; and `s/v` against `s/(v + s)` for the same day with the
conversion between them. Those are the acts the `standard` fields name and the
quizzes measure; no objective is "understand X". Every `mistakes[0]` is the §C
misconception, named as a model someone holds and refuted with a tile: the
pioneer who gains `+12 h` while the general rate stays at `20%`; the wage bill
that does not move while constant capital per piece falls from `10d` to
`5/6 d`; the `4, 2, 1` that three rates compute and no market could; the
`£5,000` machine that saves `£6,000` of labour and is `not adopted`; the
ten-hour day at `6/5` that spends `12 h` and keeps the rate at `50%`; the `0 set
free` of the carpet factory; the sago-cutter whose rate goes from zero to `500%`
by an `absolute` change alone; the productivity preset that leaves the day at
12 hours of value and moves only its split; the `11/12` that is `1,100%`. All
76 pinned tile strings on the nine pages matched the lab.

Fidelity to Chapters 12–18 is high. All ninety quoted segments on the course as
received were found verbatim in the Kerr text, with the chapter and section
cited correctly each time; the module names are the Kerr chapter titles
(including the "Formulæ" of Chapter 18); and the figures that matter are
Marx's where the lesson says they are: the 12-hour day with 10 necessary, the
24 articles at 10d, 5s falling to 3s; twelve masons and 144 hours, a hundred
harvesters and 1,200 hours; founders, breakers and rubbers at 2,000, 4,000 and
8,000; the five-man "hole"; the £3,000 machine and the 150 men; Baynes's 450
spindles and 27,000 hours; 8 necessary hours, `6 2/3` and `3 1/3`; Gardner's
eleven hours; the carpet factory at £30, £1,500 and £1,000; the £500 capital at
two-fifths and four-fifths; the sago-cutter's 12 hours a week and five days of
surplus labour; 4s to 3s and 2s to 3s; 6s to 8s; 12 to 14 and 16; Lavergne's
quarter; Mill's 20% that is 4%. Marx is presented, not endorsed: the
compensation theorists, Smith on the two divisions of labour, Mill on
durability, Ricardo on the three laws, the marginal-productivity account of the
wage, Schumpeter on the innovator's lead, Coase on why firms exist and the
economists who read `s/(v + s)` as a partnership each get their case at
strength before Marx answers, and every `note` names what the lab cannot show.

Four things were wrong or missing, and are repaired below. One arithmetic
figure in `the-concept-of-relative-surplus-value` was Marx's own slip copied
into a worked line as if it were a product of the line (`12 h · 5/8 = 7 1/5 h`;
it is `7 1/2`). Two of the critics the brief asks for, Babbage and Ure, were
absent, and with Babbage went the one mechanism by which Chapter 14 says
manufacture produces relative surplus value, the hierarchy of labour-powers.
One quiz item could be argued against by a reader who remembered Marx's
proviso about the value of money. One cross-reference named a lesson that does
not exist. Nothing needs splitting, merging or reordering.

## The voice, judged against Course 1 and §F

The register is Course 1's, and the course should be read as confirming that
the reference voice carries into a chapter that is mostly history.

**What works:**

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume I, Chapter n.</strong>` block, and the return to it is
  explicit: "Now read the passage again. Casting is slow, breaking twice as
  fast, polishing four times as fast" (`division-of-labour-and-manufacture`);
  "Now the passage, line by line. A 'denser hour' has fewer pores"
  (`machinery-and-the-worker`); "Now the passage. Relative surplus value is
  'absolute' because…" (`absolute-and-relative-surplus-value`); "Read the
  passage now. A derivative formula divides a part of the day by the whole"
  (`formulae-for-the-rate-of-surplus-value`). The `read_intro` fields say
  where in the chapter the passage sits and why it was chosen ("the one place
  in the chapter where Marx gives the arithmetic").
- **Scenes only where the object is in the reader's life.** "Think of how this
  looks from inside a firm. Nobody who introduces a better loom is thinking
  about the national value of labour-power" (lesson 1); "Think of a pay rise in
  a year when prices also rose, and the question of whether you are better
  off" (lesson 8); "Suppose you are told that a company's workers receive a
  quarter of what they produce and its owners three-quarters. That sounds like
  75%" (lesson 9). The lessons whose objects are not in anyone's life
  (co-operation, manufacture, the displaced worker) open with the text, as §F
  rule 2 asks.
- **The history of ideas as story with people in it.** Quesnay is "the court
  physician who founded the Physiocrats"; Ferguson is "whom Marx calls Smith's
  master"; Ricardo "accepted this for years and then, in the third edition of
  his *Principles* in 1821, added a chapter saying he had been wrong"; Lavergne
  is "the French economist"; West and Ricardo "read the dear bread of 1799 to
  1815 as proof that the rate of surplus value fell". After this pass Babbage
  is "the Cambridge mathematician who designed a calculating engine" and Ure
  "a Glasgow chemist". Each opponent is given the fact his view rests on
  before Marx replies, and the reply is given as a reply.
- **Second person in `p` and `worked.intro` only.** "You want his surplus value
  and the hours in which the wage is replaced" is the shape of every worked
  intro; `steps`, `standard`, quiz items and tile text are impersonal
  throughout. No "Let's", no "dive in", no first-person anecdote anywhere on
  the course (the only "I" on it is inside Marx's quotation).
- **One light remark, and Marx's before the lesson's.** Lesson 6 gives Bill
  Sikes before the jury and calls it "Marx's light moment"; lesson 7 gives the
  bird's nest and says "Marx's reply is the lesson's one joke, and it is his";
  lesson 1 points at Quesnay's riddle; lesson 3 at "one immense factory". None
  is the lesson's invention.
- **The limit admitted.** Every `note` names the one thing the lab cannot do:
  it "treats all the necessaries as one good"; it "computes only the economy
  of means of production used in common"; it "assumes every worker at a step
  works at exactly its rate, which is manufacture's own assumption"; it
  "spreads a machine's value evenly over its lifetime output"; it "holds the
  value of labour-power fixed when intensity rises"; its re-employment figure
  "is an upper bound, as Marx's 'at the best' says"; it "cannot tell whether a
  shorter necessary time came from higher productivity or from a wage below
  value". The `footer_lead` says the figures are illustrative except where a
  preset says otherwise.
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson's question by the next lesson's title; lesson 9 names Wages and
  Accumulation and its first lesson, “The Value of Labour-Power Becomes Wages”,
  exactly as Course 4's §C carries it. None summarises.
- **"This Subject does not settle it" is varied**, as the Course 1 assessment
  asked: "what it is a lead in is the dispute" (lesson 1); "the gap is not
  there to find" (lesson 4); "the choice of formula does not settle it; it
  only decides which side's language the number is written in" (lesson 9).

**What to carry forward:**

- **Check Marx's arithmetic as well as copying it.** The `7 1/5` of Chapter 12
  is in the Kerr text, in the German, and in every English edition; it is
  still wrong, and the lesson had built a worked line on it. A figure copied
  from the book is a quotation and must be marked as one; a figure in a worked
  line is the lesson's and must be right. Where the two part, say so in one
  sentence, as the lesson now does.
- **Name the critic in the lesson his criticism concerns**, even when §C does
  not list him. §C's Course 3 entries name the compensation theorists and
  Smith; the chapters also argue with Babbage and Ure by name, and a reader
  who knows the "Babbage principle" from any history of economics would have
  looked for it in the manufacture lesson and found nothing.

## What the course teaches well

- **The objectives are acts, and the course `outcomes` are the same acts.**
  Every `standard` begins "Finish when you can…" and names the product; the
  six `outcomes` map one-to-one onto lessons 1, 2–3, 4 and 6, 5, 7–8 and 9.
- **One hard idea per lesson, and Chapter 15 cut where it should be.** The
  three lessons on Chapter 15 take value transferred (§1–2), intensity (§3, with
  §3a and §3b stated in prose), and compensation (§6, with §7–10 stated).
  `machinery-and-the-worker` says in its `concepts_intro` that it "computes the
  third and states the other two", and `not_covered` says plainly that the
  family's labour-power is not computed "because the chapter gives no figures
  for it". The seam between the modules falls between lessons 5 and 6, inside
  the chapter, and is invisible: lesson 5 ends "asks what becomes of the hands
  no longer needed, and of the economists' promise", and lesson 6 opens with
  the economists' promise.
- **Prerequisites are right and are named.** Lesson 1 recalls the a–b–c line
  of Chapter 12 and the two lessons on Chapter 10; lesson 4 recalls “Constant
  Capital and Variable Capital” for the rule that a machine passes on only
  what it loses; lesson 5 recalls “The Struggle for a Normal Working Day” for
  the legal limit; lesson 7 recalls the rate of profit only to say it is
  computed in Cost Price and the Rate of Profit. Nothing is used before it is
  taught, and nothing from a later course is leaned on.
- **The misconceptions are refuted with the specific figure**, and each
  `mistakes[0]` is a position someone holds: "Marx says the reverse of the
  individual: he 'by no means necessarily aims' at it" (lesson 1); "the
  capitalist 'does not pay for the combined labour-power of the hundred'"
  (lesson 2); "Smith thought the difference was only how much an observer can
  see" (lesson 3); "That is society's test. The capitalist's test is narrower"
  (lesson 4); "the case the manufacturers argued from" (lesson 5); "The
  compensation theorists' strongest case is… and Marx answers that those jobs
  need new capital" (lesson 6); "Nature can shorten the necessary time; it
  cannot make anyone work past it" (lesson 7); "It raises the number of things
  produced, not their value" (lesson 8); "It measures the share of the day the
  capitalist receives" (lesson 9). The second and third mistakes are real
  errors too: a wage cut counted as relative surplus value, shared means
  "worth less", the fastest step given the most workers, a machine as a source
  of new value, labour measured by the clock alone, the necessaries counted
  as capital, the rate of surplus value equated with the rate of profit, the
  two formulae taken for different days.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand with Marx's figures (24 articles at 10d; twelve
  masons; founders, breakers and rubbers; the £3,000 machine; ten denser
  hours; the carpet factory; twelve-and-six to fourteen-and-five; dearer bread
  and a longer day; eight surplus hours in twelve). Every `panel_intro` asks
  the reader to watch a specific tile before the press. Every quiz asks the
  same act on a fresh instance: 600, 300 and 200 an hour; a 10s room against a
  100s room; £1,200 over 6,000 units; a 9-hour day at `4/3`; 60 workers at £40
  and a £600 machine; 10 hours with 5 then 4 necessary; a 10-hour day with 2
  necessary. The distractors are the named errors: the surplus divided by the
  whole day instead of the necessary time (`1/4` for `1/3`); the inverted
  division (`£5` for `£1/5`); the intensity added instead of multiplied
  (`10 1/3` for `12`); the wages saved with the machine's cost forgotten
  (`£800` for `£200`); the share written as a rate (`80%` for `400%`).
- **Illustrative and Marx's own are kept apart, in label, prose and `note`.**
  Labels say "Marx's day", "Marx's 12 masons", "Marx's type-founding", "Marx's
  £3,000 machine", "Marx's carpet factory", "Marx's case I" where the instance
  is his, and "A pin workshop at illustrative rates (Smith gives none)",
  "Marx's glass-house 'hole': five steps at one pace", "A £5,000 machine", "12
  hours, 6 necessary, lengthened to 14" where it is not. The `panel_intro` of
  `co-operation` says "The money figures are illustrative; the numbers of
  workers and hours in the masons and harvest presets are Marx's"; that of
  `machinery-and-the-displaced-worker` says "The carpet factory is Marx's; the
  c/v of 4 in machine-building is illustrative"; that of
  `machinery-and-the-value-it-transfers` says "The 10,000 yards of life is
  illustrative". Every `note` repeats the split. A reader cannot mistake the
  pin workshop's rates or the 10,000 yards for figures in the book.
- **The arithmetic agrees with the lab and with the text.** `10 − 9 = 1`,
  `3/9 = 1/3`; `12 · (2 − 1) = 12 h`, Marx's 6s at 6d an hour; `10/(5/3) = 6`,
  `6/6 = 100%`; `24 · 10d = 20s`, `24 · 6d = 12s`, `8s − 5s = 3s`; `10s/12 =
  10d`, `10s/144 = 5/6 d`, `60s/144 = 5d`, `5s/10 = 6d`, `100s/1000 = 1 1/5 d`;
  `1/2000 : 1/4000 : 1/8000 = 4 : 2 : 1`, `1/3000 : 1/2000 : 1/1200 = 2 : 3 : 5`;
  `£3000/10000 = £3/10`, `£5000/10000 = £1/2`; `10 · 6/5 = 12`, `8/(6/5) =
  6 2/3`, `4/(6/5) = 3 1/3`, `12 · 4/3 = 16`; `50 · £30 − £1500 = £0`,
  `£1500/5/£30 = 10`, `£500/£30 = 50/3`, `£1000/5/£30 = 20/3`, `£1500/£30 =
  50`; `8/6`, `7/5`, `9/5`, `10/2 = 5`; `20/500 = 4%`; `8/(4/3) = 6`,
  `12 · 4/3 − 6 = 10`, `10/6 = 5/3`, `6/(3/4) = 8`, `(16 − 8)/8 = 1`, `4/8`;
  `6/6` and `6/12`, `8/4` and `8/12`, `9/3` and `9/12`, `11/1` and `11/12`.
  Marx's §7 figures (£500 at two-fifths pays 300 at £1; four-fifths pays 100;
  £1,500 pays 300; £2,000 pays 400 against 1,200) and his Chapter 17 figures
  (a quarter down, a half up; 33 1/3% more surplus labour at 16 hours) are
  given as his and are right.
- **The kit's limits are reported where they bite, not hidden.** The `relative`
  view's pioneer sells at the full social value; the prose works Marx's 10d by
  hand and says the preset counts at the full value. The `adopt` view's test is
  strict, so Marx's machine costing exactly the wages it displaces is "not
  adopted"; the prose says "it saves him nothing", which is Marx's point. The
  `displace` view omits the machine-builders' surplus value; the note says the
  figure is therefore an upper bound, and the `compensation` preset is
  explicitly "the most favourable case there could be". The `three` view's
  `hold` select cannot be set by a preset; the lab ships with all three
  factors on and the prose tells the reader what the menu does.

## What it taught badly, or said wrongly

### Arithmetic

- **`the-concept-of-relative-surplus-value`, body, worked line and `after`:**
  "the worker replaces his 5s wage in `7 1/5` hours instead of 10", with the
  worked line `wage replaced in: 12 h · 5/8 = 7 1/5 h`. Five-eighths of 12 is
  `7 1/2`. The `7 1/5` is Marx's: the Kerr text (l. 2625) has "instead of 10
  hours, the labourer need now work only 7 1/5 hours", and "His surplus-labour
  is, therefore increased 2 4/5 hours", which are consistent with each other
  and with nothing else in the passage. Marx's own ratio of necessary to
  surplus labour, "now only 5:3", and his own articles, 6 for the necessary
  labour out of the `9 3/5` that represent the day, both give `7 1/2` hours to
  `4 1/2`. A worked line that prints `7 1/5` as the product of `12 · 5/8` would
  fail any reader who checked it, which is the reader this Subject wants.
  Repaired: the prose and the worked line now say `7 1/2`, and the `after`
  says the book prints `7 1/5`, that it is a slip in the text and not in the
  method, and why.

### Fidelity

- **`division-of-labour-and-manufacture`, body:** Chapter 14 §3 ends with the
  one mechanism by which manufacture lowers the value of labour-power: the
  hierarchy of labour-powers and the scale of wages, the new class of
  unskilled workers "which handicraft industry strictly excluded", the
  vanishing or shrinking cost of apprenticeship, and the sentence "In both
  cases the value of labour-power falls" (l. 2814–2816). The lesson computed
  the proportions and argued the two divisions of labour, and never said how
  the chapter's title mechanism produces relative surplus value, which is the
  course's subject. The standard account of that gain is Babbage's, quoted by
  Marx in footnote 50: by dividing the work the master "can purchase exactly
  that precise quantity of both which is necessary for each process". One
  paragraph added after the detail-labourer paragraph, giving Babbage at
  strength, Marx's two sentences, and the statement that the lab does not
  compute the hierarchy because its workers all stand at one rate and one
  wage. The §C misconception, instance and pins are unchanged.
- **`machinery-and-the-worker`, body:** Chapter 15 §4 is Marx's argument with
  Andrew Ure, "the Pindar of the automatic factory", and §5 quotes Ure on the
  self-acting mule as "A creation destined to restore order among the
  industrious classes". The lesson summarised §4 and §5 in four sentences
  without him. Ure's position is the strongest contemporary case for the
  factory: it lightens toil, its discipline (Arkwright's) is the real
  invention, and each improvement that makes a skilled hand unnecessary ends a
  strike before it starts. The paragraph now gives that case first, then
  Marx's reply from the same section, "The lightening of the labour, even,
  becomes a sort of torture". Nothing else in the lesson moved.
- **`the-concept-of-relative-surplus-value`, body:** 'In “The Working Day” of
  the previous course the point c moved' cited a lesson that does not exist;
  Course 2's two lessons on Chapter 10 are “The Working Day: Its Limits and
  the Greed for Surplus Labour” and “The Struggle for a Normal Working Day”.
  Now "the previous course's two lessons on Chapter 10", which is a chapter
  citation by number, as §0's first deviation allows.

### Quiz

- **`price-of-labour-power-and-surplus-value`, quiz 1:** "Productivity doubles
  in every industry, with the length and intensity of the day unchanged. What
  value does the day create now?" keyed `6s`. Chapter 17's first law holds
  "the value of money being assumed to be constant" (Marx says so in Chapter
  12, l. 2629, and the assumption runs through Chapter 17); if productivity
  doubled in gold-mining too, the same 12 hours would be expressed in 12s, and
  a careful reader could argue for the second option. Now "in the industries
  that make the worker's necessaries, with the length and intensity of the
  day and the value of money unchanged". Every other distractor on the course
  was argued for and could not be defended.

### Speech

Every `data-say` on the nine pages was read. The capkit figures and the
course's key lines read well: `cut it by cheapening necessaries`, `set free
equals wages saved minus machine cost`, `not the surplus that is extracted`
and `per unit equals machine value over lifetime output` are each read as
words, so the three-letter-word hazard the Course 1 assessment recorded (`due`,
`out`, `use`) does not fire on `cut`, `set`, `not` or `per`; the rule is
narrower than "three letters" and is still owned by the chrome-renderer tier.
`pounds 3000 is less than pounds 3000 is false, no saving` and `6 h over the
quantity 3 over 4, equals 8 h` read correctly. No `cwt`, no split step, no
spoken form was needed and none was added to `content/spoken/capital.py`.

## Do the labs show the ideas, or decorate them?

Seven of the nine show the lesson's idea directly; two show a part of it, and
both say so.

- **Show it.** `relative` (lesson 1) puts the pioneer's extra and the general
  rate on the same page, so the misconception is refuted by watching one tile
  move and the other not. `detail` (lesson 3) computes the "fixed mathematical
  ratio" from the rates and nothing else, and `better-mould` shows the ratio
  is a fact about technique. `adopt` (lesson 4) has the two tests as a
  redraw-only switch, so the same machine is seen to pass one and fail the
  other, which is the whole of §2's edge. `intensity` (lesson 5) prints
  labour in normal hours beside clock hours, and `ten-only` against
  `ten-denser` is the manufacturers' case against Marx's in two presses.
  `displace` (lesson 6) prints "set free" and "in machine-building" as two
  addends, so `0 set free + 10` is read as Marx reads it. `classify` (lesson
  7) names the kind of change, which is the lesson's objective, and `sago`
  makes the natural-basis argument an arithmetic fact. `three` (lesson 8) is
  Chapter 17 itself. `formulae` (lesson 9) prints the two ratios side by side,
  and `extreme` shows one racing while the other crawls.
- **Show a part.** `cooperate` (lesson 2) computes the economy of shared means
  of production, which is the chapter's second effect; its first and third,
  averaging and the new collective power, are stated in prose because Marx
  gives no figure for either, and the `note` says output per worker "is an
  input here, the same alone and together". The lesson uses the lab honestly
  for the chapter's turn (the wage bill moves with neither figure), but a
  reader should know that the headline claim of Chapter 13 is not what the
  tiles compute. `displace` (lesson 6) answers the narrow "capital set free"
  claim and not the compensation theorists' strongest form, and the lesson
  says so three times (body, `mistakes[0]`, `note`).

No lab is decorative.

## Can a reader who has finished Course 2 follow it?

Yes. The hard places are the chapter's hard places, and the course marks them.

- **Lesson 1** has to make a reader see that "cheaper necessaries" and "lower
  wages" are different things when both leave 3 surplus hours in the day. It
  does this by letting Marx raise the wage cut first ("The obvious way to move
  b is to pay less, and Marx raises it himself") and giving it `mistakes[1]`.
  The pioneer is the second hard idea, and the lesson keeps it apart: the
  `given`–`cheaper` pair is the chapter's definition, the `pioneer`–`general`
  pair is its motive. The slip in Marx's arithmetic is now flagged where a
  checking reader would hit it.
- **Lesson 3** is the one where the lab is simplest and the chapter longest.
  The lesson does the type-founding sum in four lines and spends its prose on
  the two divisions of labour, which is where Marx's argument is. With the
  Babbage paragraph a reader now also learns why the chapter is in Part IV.
- **Lesson 4** is the course's hinge and gets the two-test idea in one
  sentence ("he pays for labour-power, not labour") before the lab, and the
  worked example makes the "no saving" verdict a `<` that is false rather than
  a kit quirk.
- **Lesson 6** carries the most history and keeps the arithmetic to one
  example. The order is right: the economists' best case, then Marx's narrow
  test, then his wider reply, then §7's concession that factory employment
  can rise, then the statement that the long-run question is about data the
  path does not carry.
- **Lessons 7–9** are a review of Parts III–V and read as one. A reader who
  has done the eight before will find nothing new to compute in lesson 7
  except the word "both", and that is the lesson's point.

## Repairs made in this pass

In `content/capital/c03_relative/part_a.py`:
`the-concept-of-relative-surplus-value` the a–b–c paragraph (the Chapter 10
citation), the 10d paragraph (`7 1/2`), `worked.lines[4]` and `worked.after`;
`division-of-labour-and-manufacture` one new `p` after the detail-labourer
paragraph (Babbage; the hierarchy of labour-powers) and its line-number
comment; `machinery-and-the-worker` the §4–5 paragraph (Ure) and its
line-number comment. In `part_b.py`:
`price-of-labour-power-and-surplus-value` quiz 1's question. No preset,
`expect`, slug, module, lab key, mode or view changed, and no §C entry needed
correcting: every instance the lessons carry is the one §C records, and the
Course 3 entries already carry the authoring changes (`given`, `one`, the
pioneer at social value, `better-mould`, `society` as a £5,000 machine,
`dear-labour`, the renamed intensity presets, `cheaper-machine`, `sago`,
`dearer-food`, `lavergne`).

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. The seven new quoted segments were each searched for in the Kerr text
before they were written, and the strict checker reports no misses.

## Remaining issues

- **`the-concept-of-relative-surplus-value`, `pioneer` preset label:** "One
  capitalist doubles productivity (Marx's 24 articles)" prints `+12 h`, which
  is 6s at the full social value, where Marx's pioneer sells at 10d and gains
  2s. The prose and `note` explain the difference and the §C entry records
  it. A `pioneer_price` field on the `relative` view would let the lab show
  Marx's own 3s; that is a kit change and was not made.
- **`co-operation`:** the chapter's headline claim, that a combined day
  produces more use-values than the same hours apart, is not computed, and
  cannot be from the chapter's figures. The lesson is honest about this. If a
  later revision of `cooperate` added a `combined_output` input, the `masons`
  preset could show Marx's "much more progress with the building"; recorded,
  not changed.
- **`absolute-and-relative-surplus-value`, `sago` label:** "Marx's
  sago-cutter: 2 hours a day for himself, then a 12-hour day" names Marx's
  example, but the 2 hours a day is the lesson's spreading of his 12 hours a
  week over six days, as the `note` says. The label could say "spread as 2
  hours a day"; left as it is because the `note` carries it and the label is
  already long.
- **`machinery-and-the-displaced-worker`, body:** the prose writes "Bill
  Sikes", Dickens's spelling; the Kerr text has "Bill Sykes". The quotation
  itself does not include the name, so nothing in quotation marks differs
  from the text. Harmless; left as Dickens spelt it.
- **The `7 1/5`** is in every edition of Volume I and will be in the Kerr text
  this Subject quotes. A later reviewer who finds the lesson's `7 1/2`
  disagreeing with the book should read `worked.after` before "correcting" it
  back.
