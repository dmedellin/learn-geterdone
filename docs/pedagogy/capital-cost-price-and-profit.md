# Pedagogy assessment — Cost Price and the Rate of Profit (Capital, course 9)

Formed from the seven lesson dicts in `content/capital/c09_profit/` (`part_a.py`,
lessons 1–4, Volume III, Chapters 1–4; `part_b.py`, lessons 5–7, Chapters 5–7;
`__init__.py`, the course dict), and the kit they render through
(`scripts/mathpath/labs/capkit_b.py`, mode `profit`; views `cost`, `rate`,
`relation`, `turnover`, `economy`, `price`, `books`), on branch
`feat/capital-subject` before the Subject was wired into the site. The design
authority is `docs/capital/PLAN.md` §0, §B, the Course 9 entries in §C, §D as
summarised in `docs/capital/kit-b-report.md`, §E (how a passage is quoted), §F
(the voice) and §G; the author's brief is `docs/capital/AUTHORING.md`, whose
closing sections list the errors Course 1's two reviews found. Course 1,
Commodities and Money, is the voice reference, and
`docs/pedagogy/capital-commodities-and-money.md` the model for this document.

Every lesson was read in full before anything was changed. Every pinned tile
was read off the rendered page with `node scripts/labcheck.js --observe`
(rendered through `scripts/preview_subject.py capital --course
capital-cost-price-and-profit`); every figure in prose, label, step, worked
example, quiz and `mistakes` entry was recomputed by hand; every quotation and
every phrase in `&ldquo;…&rdquo;` (seventy-two segments) was checked character
by character against `/mnt/project-files/capital-texts/volume-3-kerr.txt`
with the strict quotation checker; Chapters 1–7 (Kerr l. 450–1570) and the
relevant pages of Engels' preface (l. 284–300) were read whole, not only at
the cited lines. Every math run on the eight rendered pages was read from its
`data-say`. Lessons, in course order: `cost-price-and-profit`,
`the-rate-of-profit`, `rate-of-profit-and-rate-of-surplus-value`,
`turnover-and-the-rate-of-profit` | `economy-in-constant-capital`,
`price-fluctuations-of-raw-materials`, `supplementary-remarks-on-profit`. The
bar marks the seam between the two modules. The course assumes the Volume I
courses and The Turnover of Capital, and is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can compute a cost
price and a profit and place a sale against the value; divide one surplus
value by v and by c + v and say what each ratio measures; split p′ into s′ and
v/C and name which factor moved it; compute an annual rate from s′, n, v and C;
recompute the rate after a saving in c or a change in the price of raw material
passed on in full, in part or not at all; and read one set of figures as a
capitalist's books do and as Marx's categories do. Those are the acts the
`standard` fields name, the six course `outcomes` repeat, and the quizzes
measure; no objective is "understand X". Each lesson's `mistakes[0]` is the §C
misconception and each is refuted with a tile: `£60` of profit on a sale `£40`
below value, `1/5 = 20%` three times over s′ of 50%, 100% and 200%,
`3/20 = 15%` beside `3/2 = 150%`, `5/22` on the unchanged 10,000 of fixed
capital, `5/24` whether the £20 saved was a boiler or a guard rail, `£0` of
profit when the dearer cotton is not passed on, `£100` of profit recorded by
the books on a sale at value. All 53 pinned tile strings on the seven pages
matched the observed lab, and every figure in prose agreed with the lab or a
recomputation.

The arithmetic is right, including the hardest figure on the course. Engels'
Manchester mill gives `(20/13) · (17/2) · (318/12,500) = 108,120/325,000 =
2,703/8,125 = 33.27%`, which is the pinned string; his check `4,160/12,500 =
33.28%` is what the formula returns with the exact turnover `2,704/318` in
place of 8½, since `(80/52) · (2,704/318) · (318/12,500) = 4,160/12,500`, and
the lesson says precisely that. His annual rate of surplus value `(20/13) ·
(17/2) = 1,307 9/13%` is "more than 1,300%", as quoted. Every capital labelled
"Marx's figures" or "Engels' figures" is in the chapter with those figures:
400c + 100v + 100s and the sales at 510 to 590; 80c + 20v + 20s and its six
variants; capitals A, B, I and III; 2,000c + 400v + 600s; businesses A and B;
£100 earning £20 re-priced as £150; 1,000, 2,000 and 500 at 20%.

Fidelity to the text is high and the four defects found were all in what the
lessons said about the text rather than in any number. One was a strong claim
the text does not support: `supplementary-remarks-on-profit` told the reader
that "And he will do so" at Kerr l. 1544 "is the translation's slip". It is
not clearly one. The sentence before reads "the bourgeois will not consider his
profit as identical with the surplus-value", and "do so" takes up that refusal,
with the reasons that follow being reasons for *not* seeing it; the rendering
is awkward, not wrong, and the claim is removed below. The others were a
`how_to` line that inverted Engels' preface about the state of Part I's
manuscript, a sentence that gave Ricardo Marx's verdict without Marx's
qualification, and a preset labelled with Marx's figures whose c/v split Marx
does not give. Marx is presented, not endorsed: Torrens, Ramsay, Proudhon,
Marshall, Senior, Böhm-Bawerk, Ricardo, Tugan-Baranovsky, Okishio, Adam
Smith and Rodbertus each get two or three sentences at strength, no later
critic is "answered" by Marx, and every `note` names what the lab cannot
settle. Nothing needs splitting, merging or reordering.

## The voice, judged against §F and Course 1

- **The passage first, then its phrases in order.** Every body opens with
  `<strong>Volume III, Chapter n.</strong>` and returns to it: "Read the
  definition slowly. It does not introduce a new quantity" (lesson 2); "The
  phrase that carries the chapter is 'in the language of the capitalist, a
  saving in buildings'" (lesson 5); "The word 'alleged' is doing work"
  (lesson 1). Lessons 1, 2, 5 and 6 carry a second short quotation later in
  the body, placed where the argument reaches it, which is the shape §E.3
  allows and Course 1 uses; lessons 3, 4 and 7 quote inline instead, a few
  words at a time.
- **Scenes only where the object is in the reader's life.** "Think about how a
  price is usually explained to you: the maker's costs, plus a margin on top"
  (lesson 1); "If you put money in a savings account you think of the interest
  as a percentage of all of it. Nobody asks which pound earned it" (lesson 2);
  "You have seen this happen to a café when the price of coffee beans jumps"
  (lesson 6). Each reaches the chapter's category within the paragraph. Lessons
  3, 4, 5 and 7, whose objects are an equation, a formula, a list of economies
  and a refusal, open with the text itself, as §F rule 2 asks.
- **The history of ideas as story with people in it.** Torrens is "a Royal
  Marines officer turned economist who wrote in Ricardo's circle"; Ricardo
  "the stockbroker whose *Principles* of 1817 dominated English economics for a
  generation"; Rodbertus "the Prussian landowner and economist"; Samuel Moore
  the translator "who was better fitted to edit it 'since he graduated from
  Cambridge in mathematics'". Engels' own voice is heard in lesson 4, with the
  Bessemer process, alizarin and the Suez Canal, and the lesson says whose
  voice it is.
- **Second person in `p` and `worked.intro` only;** `steps`, `standard`, quiz
  items and tile text stay impersonal. No "Let's", no "dive in", no
  first-person anecdote.
- **One light remark, and Marx's or Engels' before the lesson's.** "Marx keeps
  his driest line for Proudhon" (lesson 1); "here Marx is at his driest: the
  first firms to use a new invention usually go bankrupt" (lesson 5); Engels'
  "certain brave soul" (lesson 4). None is the lesson's invention.
- **The limit admitted.** Every `note` names one thing: the lab "subtracts; it
  cannot say whether the £100 is unpaid labour or a return the capital earned";
  "the lab treats c as the constant capital advanced, so a preset must put the
  whole fixed capital in it"; "the lab, like Engels, turns the circulating
  constant capital over with v and assumes no credit"; "it cannot price a lost
  life"; "it does not model the stocks a capital holds".
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson by its exact title; lesson 7 ends with Average Profit and Its
  Fall and its question, "profit and surplus value part company sphere by
  sphere". The closing "this Subject does not settle it" is varied, as the
  Course 1 review asked: "this Subject leaves it open", "the lab computes both
  rates", "the lab computes it on them and cannot test them", "an empirical
  question the lab cannot answer", "the lab cannot test that".

What differs from Course 1, and should: Volume III's Part I is argumentative
rather than definitional, so the lessons spend more of their length on what
the capitalist sees and why, and less on building a quantity. That is the
chapters' own proportion.

## What the course teaches well

- **The objectives are acts and the closing drill measures them.** "Given c, v
  and s and a selling price, compute the cost price, the value and the profit,
  and state whether the sale is at, above or below value and whether it is
  above or below cost price" (lesson 1); "given two capitals with equal rates
  of profit, state what further figure decides whether their rates of surplus
  value are equal" (lesson 2); "state which factor moved p′ and whether the
  factors reinforced, opposed or offset each other" (lesson 3); "compute the
  year's surplus value and the annual rate of profit on the capital advanced"
  (lesson 4); "state whether the saving came from scale, cheaper inputs, reused
  waste or the conditions of work" (lesson 5); "compute the new cost price, the
  profit and the rate of profit, and compare the rate with the rate before"
  (lesson 6); "state the same profit as surplus value with its rate s′, and for
  two capitals with equal v and s, compute and explain their different rates"
  (lesson 7).
- **One hard idea per lesson, and the seven chapters kept apart.** Lesson 1 is
  k and p as amounts and refuses the ratio ("Cost price and profit are amounts.
  The next lesson turns the profit into a ratio"); lesson 2 is one division
  two ways; lesson 3 is one equation and its cases; lesson 4 adds n and nothing
  else; lessons 5 and 6 each move c once, by quantity and then by price; lesson
  7 is the capitalist's reading of figures already computed. Marx's own 400c +
  100v + 100s runs through lessons 1, 2, 5, 6 and 7, so each change is seen
  against the same capital, as the `how_to` promises.
- **The misconceptions are refuted with the specific figure**, and the second
  and third `mistakes` are the chapter's own further errors: Proudhon's cost
  price as value and the whole £1,680 in the cost price (lesson 1); profit and
  surplus value differing in amount, and dividing by the cost price (lesson
  2); percentages read as amounts, with Marx's `27,000c + 3,000v` (lesson 3);
  dividing by the capital turned over, and more turnovers always meaning a
  higher rate (lesson 4); a saving in c producing more surplus value (lesson
  5); a rise in raw material always hurting the capitalist, against the stocks
  at Blackburn (lesson 6); Rodbertus (lesson 7).
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` asks for a comparison before
  the press ("Compare cheap-sale with marx: the profit falls, and stays
  positive, while the sale is below value"; "Compare ten-times with once: ten
  turnovers against one, and the same annual rate"; "Compare passed-on with
  cotton-famine: the same dearer cotton, and a rate of `1/6` against 0"); every
  quiz asks the act on a fresh instance (300c + 150v + 150s; 600c + 200v;
  80c + 20v with c to 180; 400c + 100v at four turnovers; 300c + 100v + 50s
  saving £100; 300c + 100v + 100s with £100 more for material). Distractors
  are the named errors: `£600` for cost price, `s′ = 12.5%, p′ = 50%` for the
  swapped denominators, `20%` for the capital turned over, `50%` for s′ taken
  as the rate, `33.33%` for dividing by c alone, `£20 and 13.33%` for a profit
  not re-priced. Every distractor was argued for and none could be defended.
- **The two Engels lessons say what is Engels'.** Lesson 4 opens "These are
  Engels' words, not Marx's", quotes the preface ("Nothing was available for
  chapter IV but the title"; "I have elaborated it myself"), and names the
  brackets and the signature; lesson 3 tells the story of the equations
  manuscript and Samuel Moore. Lesson 7 names Engels' bracketed note at the
  blank and tells the reader "You are reading a draft".
- **The chapter's own figures and phrases are the chapter's.** The sales at
  510 to 590; 1,666 2/3 working days is left out, correctly, as a step the lab
  does not need; Torrens' 100 and 120 quarters; the 20 lb of yarn at 30s with
  2 lb for the buyer; Ramsay, Malthus and the phlogiston; the spinner with 6
  hours of wages and 12 of work; 16 2/3% and 25%; capital A at 40% and B at
  20%; 45 5/11% and 22 8/11%; "one week is stretched into one and a half"; £4
  4s and £44 a ton; 15 men a week; £50,000 at 2s per horse-power; £9 1s against
  £11 on 110 horse-power; 263 against 100; ½d, 1d and 6d of waste; Greg in
  1837 and the Ten Hours Bill; 4d to 6d in 1847; 5d or 6d to 2s; 50.7% of
  Lancashire and Cheshire's cotton workers idle; "only convulsively"; 8 1/3%;
  150 : 30 = 100 : 20. All are in the text where the lessons say they are, and
  the inline comments give the line numbers.
- **The seam at lesson 5 is invisible.** Lesson 4 ends "turns from the speed of
  capital to its size: how a capitalist raises his rate of profit by spending
  less on c"; lesson 5 opens on Chapter 5's list of savings and says "That is
  the rule, and it is Chapter 3's third case put to work". Both modules spell
  British, cite lessons by title and chapters by volume and number, and share
  the quotation conventions their docstrings state.

## What it taught badly, or said wrongly

### Fidelity

- **`supplementary-remarks-on-profit`, body:** "'And he will do so' is the
  translation's slip; the sense is that he will not." The Kerr sentence runs
  "Nevertheless the bourgeois will not consider his profit as identical with
  the surplus-value, that is to say, with unpaid surplus-labor. And he will do
  so, for the following reasons. 1) He forgets the process of production in the
  process of circulation." Read as English, "do so" takes up the whole
  predicate before it, the refusal, and the enumerated reasons are reasons for
  the refusal; the rendering is clumsy, and a reader may stumble on it, but
  telling the reader the translator erred needs a clear error and there is
  none. Repaired: the paragraph now says "Read 'And he will do so' as taking up
  the refusal: what follows are the reasons he will not see it", which gives
  the reader the same help without the charge.
- **`__init__.py`, `how_to[1]`:** "For Part I Engels had a fuller draft than
  for much of the rest." The preface says the opposite: "For the first part,
  the main manuscript was serviceable only with considerable restrictions";
  Chapter 1 came from "two attempts of Marx at rewriting", Chapter 2 from the
  main manuscript, Chapter 3 from the equations manuscript and Moore's
  summary, Chapter 4 from nothing but the title, and only "Beginning with
  chapter V, the main manuscript is the sole basis"; for Parts II to IV "I
  could follow the original manuscript throughout". Now says Part I gave
  Engels the most trouble and lists what each chapter came from.
- **`rate-of-profit-and-rate-of-surplus-value`, body:** "With v/C fixed, p′
  moves in exactly the same proportion as s′. This, Marx says, is the only case
  in which David Ricardo was right…" gave Ricardo the whole v/C-fixed case.
  Marx (Kerr l. 835–849) says s′ can differ between capitals of equal
  composition in three ways, by wages, by intensity or by the length of the
  day, and that the first, "in which the percentages of composition of the
  capital, the working day, the intensity of labor, are constant, while the
  rate of surplus-value varies on account of the variation of wages, is the
  only one in which Ricardo's assumption is correct". The quiz's fourth item
  already had the qualification; the body did not. Now names the three ways
  and gives Ricardo the first alone.
- **`supplementary-remarks-on-profit`, `gold` preset and `note`:** the preset
  is labelled with Marx's £100 earning £20 re-priced as £150 and is built as
  `120c + 30v + 30s`, a split Marx does not give (Kerr l. 1552–1554 has only
  the totals), and the `note` said "The figures are Marx's". A reader who
  checked the book would look for the 120 and 30 and not find them. The body
  now says the split is illustrative and that any split with the same £30 of
  profit gives the same 20%; the `note` carries the exception; the §C entry in
  `docs/capital/PLAN.md` says the same, so the two agree.

### Everything else checked and found sound

- **Prose that explains every preset.** Every preset id on the course appears
  in a body paragraph with its figure: marx, cheap-sale, proudhon, below-cost;
  marx, labour-heavy, capital-heavy, machinery; base, vary-s,
  vary-composition, both-offset, s-up-p-down; ten-times, once, halved, engels;
  shared-building, waste-reuse, unsafe; passed-on, half-passed, cotton-famine,
  cheaper; ledger, business-a, business-b, gold. The Course 1 defect (a
  labelled preset with no sentence) does not recur.
- **The lab's model is kept apart from the definition.** Lesson 2 says the lab
  "treats c as the constant capital advanced, so a preset must put the whole
  fixed capital in it", which is why the `machinery` preset carries 1,580 and
  not 400; lesson 4 says the lab "turns the circulating constant capital over
  with v", as Engels assumes "for the sake of simplicity"; lesson 7 says the
  books view's rate is "on cost", which equals s/(c + v) only because the lab
  consumes all of c, and the worked example writes both. Lesson 6 says the
  "share passed on" is the lab's control and not Marx's quantity.
- **Illustrative figures are called illustrative.** The £500 capitals of lesson
  2 ("Marx gives none in this chapter"), the savings of lesson 5, the cotton of
  lesson 6 and the worked example of lesson 4 are each so marked in the `note`
  or the body.
- **Critics are given at strength and never answered by a dead man.** Marshall
  (1890) is "a modern reader's objection" and the lesson says "Marx died before
  Marshall wrote. What in the chapter bears on the point is…"; Böhm-Bawerk's
  time preference is stated in its own terms, not as Senior's abstinence;
  Tugan-Baranovsky and Okishio are dated and the lesson says "This chapter does
  not settle that argument; it supplies the arithmetic both sides use". Lesson
  5 names Adam Smith's compensating differentials, says "The chapter does not
  take up Smith", and sets against it only what the chapter quotes (the 1829
  report's miners "whose numbers generally exceed the demand"). Lesson 7 states
  "the capitalist may simply be right" and says the chapter "does not argue
  that point".
- **Speech.** Every math run on the eight pages was read from `data-say`. The
  profit-mode figures read well: "5 over 84", "2,703 over 8,125" is not spoken
  (tiles are not runs), "s prime times n times v over C", "p prime is to s
  prime as v is to C", "150 is to 30 as 100 is to 20", "22 and 8 elevenths".
  No key line begins with a three-letter word; `S = s · n in a year` opens
  with a single letter and reads as one. No `cwt.`, no step with bare math.
  The one run added in this pass, `120c + 30v`, reads "120 c plus 30 v".
- **Cross-references.** Lessons by exact title, chapters by "Volume III,
  Chapter n", Volume I and II chapters by number where Marx cites them, the
  next course by its §B title. Modules carry the Kerr chapter titles
  ("The Effect of the Turn-Over on the Rate of Profit", "Additional Remarks").

## Can a reader who has done the Volume I and II courses follow it?

Yes, and the places a reader slows are the places Marx's readers slow.

- **Lesson 1** is the course's best. It takes a reader from "costs plus a
  margin" to k, does Marx's two experiments (c to 600, v to 150) so the reader
  sees why the difference between c and v vanishes in k, adds the fixed capital
  so the £100 is "as much an increase of the whole £1,680 as of the £500", and
  only then lets the chapter's sharpest claim land: a sale below value at a
  profit. Torrens, Ramsay and Proudhon are stories with people in them, and
  Marshall arrives exactly where a reader trained on modern accounting will
  have objected.
- **Lesson 2** is light and correctly light. Its one move, the same £100 over
  v and over c + v, is made with three capitals of £500 and one of £1,680, and
  the savings-account opening gives the reader the capitalist's reason before
  Marx's. The order-of-explanation paragraph is the hardest in the course, and
  it is placed after the arithmetic rather than before.
- **Lesson 3** is where a reader may tire: five presets, a proportion and two
  twentieth-century critics. It is nonetheless one idea, and the three cases
  arrive in Marx's order (s′ fixed, v/C fixed, both), each on Marx's figures,
  with the offset case worked by hand. The "Absolute figures" concept, with
  Marx's warning about percentages, is the right thing to carry out of the
  chapter and few readers would find it unaided.
- **Lesson 4** does the one thing a reader needs, n, and then does Engels'
  calculation for a real mill, which is the moment the course's arithmetic
  meets the world. The lesson is honest about the 8½ and the hundredth of a
  point it costs, which a reader checking the book will want to know.
- **Lesson 5** carries the most evidence and the least arithmetic, and says so
  in its `concepts_intro`. The three presets are deliberately indistinguishable
  in their figures, and the fourth quiz item asks the reader to notice that,
  which is the chapter's point.
- **Lesson 6** is the clearest use of the lab on the course: a control the
  reader moves between two of Marx's sentences. The history of the cotton
  famine is kept to a paragraph and the `not_covered` says where the rest is.
- **Lesson 7** is short because the chapter is, and the lesson says the chapter
  is a draft. The books view makes the course's one recurring claim, that the
  figures agree and the names differ, visible on a single page.

## Repairs made in this pass

In `content/capital/c09_profit/__init__.py`: `how_to[1]`. In `part_a.py`:
`rate-of-profit-and-rate-of-surplus-value`, the Ricardo sentence in the
second-case paragraph. In `part_b.py`: `supplementary-remarks-on-profit`, the
paragraph after the passage (the "slip" claim), the Rodbertus paragraph (the
gold split) and the `note`. In `docs/capital/PLAN.md`: the Course 9, lesson 7
`gold` entry. No preset, `expect`, slug, module, lab key, mode or view changed,
and no instance differs from its §C entry.

`scripts/preview_subject.py capital --course capital-cost-price-and-profit`
reports OK: 8 pages, every lab executes and survives the sweep, every pinned
figure on the seven pages matches, no math run without a spoken form. The
strict quotation checker over `c09_profit` against Volume III reports 72
segments, 0 misses.

## Remaining issues (recommended, not changed)

- **Lesson 4 skips Engels' capital II** (9,000 fixed, 1,000 circulating c,
  1,000 v, five turnovers, also 45 5/11%). The lesson's point stands on
  capitals I and III, and a fifth preset would crowd the panel, but a reader
  following in the book will meet II between them and find it nowhere on the
  page. One clause in the capitals paragraph would close it.
- **Lesson 5's `note` says a saving by lengthening the working day "is
  described here but not computed".** The `workday` mode of the kit computes
  exactly that, and a cross-reference to the lesson on it in From Money to
  Surplus Value would give the reader a place to go. Not a defect; an
  opportunity.
- **The books view's `prRate` label is "Rate of profit on cost".** It equals
  s/(c + v) because the lab consumes all of c, and the lesson says so, but
  the label invites a reader to think the books divide by something other
  than the capital. A kit change ("Rate of profit, as the books show it")
  belongs to the kit's owner.
- **Lesson 3's load.** If the course is ever reshaped, the Tugan-Baranovsky and
  Okishio paragraph would sit better in Average Profit and Its Fall, where the
  law it concerns is taught; here it is the one paragraph a first reader can
  skip without loss, and it is placed last for that reason.
