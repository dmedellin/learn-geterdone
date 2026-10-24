# Pedagogy assessment — Merchant's Capital and Interest (Capital, course 11)

Formed from the nine lesson dicts in `content/capital/c11_interest/`
(`part_a.py`, lessons 1–5, Volume III, Part IV, Chapters 16–20, one chapter
each; `part_b.py`, lessons 6–9, the first four chapters of Part V, Chapters
21–24; `__init__.py`, the course dict), and the kit they render through
(`scripts/mathpath/labs/capkit_b.py`, modes `turnover` view `merchant`,
`prices` views `merchant` and `merchant-turnover`, `interest` views `split`,
`bounds` and `compound`; `capkit.py`, mode `circuit` view `formula`), on branch
`feat/capital-subject` before the Subject was wired into the site. The design
authority is `docs/capital/PLAN.md` §0, §B, the Course 11 entries in §C, §D as
summarised in `docs/capital/kit-b-report.md`, §E (how a passage is quoted), §F
(the voice) and §G (what is left out); the author's brief is
`docs/capital/AUTHORING.md`, whose two closing sections list the errors the
Course 1 reviews found. Course 1, `capital-commodities-and-money`, is the voice
reference and its assessment is the model for this one.

Every lesson was read in full before anything was changed, and so were
Chapters 16–24 of `/mnt/project-files/capital-texts/volume-3-kerr.txt` (Kerr
lines 2583–3595) with footnotes 77–83. Every pinned tile was read off the
rendered page with `node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py capital --course capital-merchants-and-interest`),
every figure in prose was recomputed by hand, every one of the ninety phrases
in `&ldquo;…&rdquo;` was searched for character by character with the strict
quotation checker, and every math run on the ten rendered pages was read from
its `data-say`. The table index in `capital-texts/tables/README.md` lists no
Volume III image between Kerr pages 185 and 646, so no table bears on these
chapters. Lessons, in course order: `commercial-capital`,
`commercial-profit`, `the-turnover-of-merchants-capital`,
`money-dealing-capital`, `history-of-merchants-capital` |
`interest-bearing-capital`, `the-rate-of-interest`,
`interest-and-profit-of-enterprise`, `interest-bearing-capital-as-a-thing`.
The bar marks the seam between the two modules, which is also Marx's seam
between Part IV and Part V. The course is Advanced and assumes Cost Price and
the Rate of Profit and Average Profit and Its Fall; it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can size a merchant's
capital from its turnovers and invert for the capital a trade needs, recompute
the general rate of profit with merchant's and money-dealing capital in the
averaging and price the manufacturer's sale and the merchant's sale with and
without the merchant's costs, find the addition to each sale from the annual
rate and the turnovers and show the annual rate unchanged, compute a
pre-capitalist merchant's gain and say what does and does not limit it, split
the profit on a borrowed £100 into interest and profit of enterprise, test a
rate of interest against its bounds and read a breach, take a manager's salary
out of profit of enterprise and name what is left, and compound a claim
beside a growing product and compare their sizes. Those are the acts the
`standard` fields name and the quizzes measure; no objective is "understand
X". The `mistakes[0]` of every lesson is the §C misconception, each refuted
with a tile: `£3,000` changing owner and still worth `£3,000`; the merchant
selling at `£1,080`, the value, because the manufacturers sold at `£1,062`;
`3%` five times against `15%` once, 15 a year either way; the goods still at
`£1,080` with the manufacturers at `£1,044`; `+£40` on £60 and `+£75` on £25
against `+£18` on £100; the `£20` unmoved while the split goes from `£5`/`£15`
to `£10`/`£10`; `£12` left from 16 and 4 and the same `£12` from Marx's 20
and 8; a `£6` manager leaving `£9`; 37 digits against 7. All 51 pinned tile
strings on the nine pages matched the lab, and every figure quoted in prose
agreed with the lab, with the Kerr text or with a recomputation.

Fidelity to the chapters is high. All ninety quoted phrases are in the Kerr
text; none was written from memory. The nine misconceptions, the figures
(3,000 pounds of linen, 720c + 180v + 180s, 900 and 100, 1,062 and 1,080, 50 of
costs and 17 1/7%, 15% once and five times, the sugar at £1 and 1s, Massie,
the 1842–1847 rates, 20 and 8 beside 16 and 4, the hatter's 115, Price's penny
and Child's £100, the 15% that a 5% interest presupposes) are the chapters',
and each lesson says which figures are illustrative (the four turnovers, the
cashier's 125, the venice and dutch prices, the rates of real growth, the
crisis preset's 5% profit). Later writers are stated at strength and none is
answered by Marx: Böhm-Bawerk and Fisher, Wicksell, Schumpeter and Knight,
Pirenne, Sweezy, Dobb and Brenner, Piketty each get two or three sentences and
then "what in the chapter bears on it", in those words, never "Marx's answer
to". The defects were local and are repaired below: the read-out split every
grouped number at its comma ("pounds 3, 000"; "1, 062"; "1, 772 years") and
spelled "mark-up" as "mark-u p" in two key lines; one paragraph wrote the
sugar example in pounds that were sometimes money and sometimes weight; one
sentence called the money-dealer's capital "lent"; one quiz item named
Roscher where the body had not; one date (Pitt's Act) disagreed with Marx's;
one quiz distractor was obscure; and one worked example closed with a verdict
in the lesson's own words rather than Marx's. Nothing needs splitting, merging
or reordering.

## The voice, judged against §F and Course 1

**What matches the reference, and should stay:**

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume III, Chapter n.</strong>` block and returns to it a few
  words at a time: "Take the passage a phrase at a time. The phrase 'this
  capital of circulation' means… 'A portion' is said with care… And 'a changed
  form' is the claim of the chapter" (`commercial-capital`); "Go through the
  passage. The rate of 15 per cent is 'yearly' and 'general'"
  (`the-turnover-of-merchants-capital`); "The man holds 'a power'… And the £5
  is paid 'out of the produced profit'" (`interest-bearing-capital`). The
  `read_intro` fields say where in the chapter the passage sits and why it was
  chosen, as Course 1's do.
- **Scenes only where the object is in the reader's life**, and interest,
  shops and payrolls are: "Think of any shop. It buys a jacket for one price
  and sells it for more" (`commercial-profit`); "You know two kinds of shop.
  One sells furniture… the other sells groceries"
  (`the-turnover-of-merchants-capital`); "Think of the payroll office of a
  large firm, or the payment processor behind a card"
  (`money-dealing-capital`); "You have met interest from both sides: on a
  savings account… and on a loan or a mortgage" (`interest-bearing-capital`);
  "Interest rates are news" (`the-rate-of-interest`); "Her accountant tells
  her to count a return on the money she has put in"
  (`interest-and-profit-of-enterprise`); "the savings advertisement with a
  curve that bends upward forever" (`interest-bearing-capital-as-a-thing`).
  Each reaches the chapter's category within the paragraph.
  `history-of-merchants-capital`, whose object is not in anyone's life, opens
  on the text, which is what §F rule 2 asks.
- **The history of ideas as story with people in it.** Proudhon "the French
  socialist, whose 1850 debate with the economist Frédéric Bastiat he cites";
  Massie "the eighteenth-century writer… whom Marx credits with first seeing
  that interest is part of profit"; Price "an eighteenth-century minister and
  actuary… Pitt believed him"; Child "the father of modern banking" in Marx's
  words, "the seventeenth-century merchant and writer on trade" in the
  lesson's; Pirenne "in the 1920s", Sweezy "debating the British economist
  Maurice Dobb" "in the 1950s", Brenner after; Wicksell "in *Interest and
  Prices* (1898)"; Böhm-Bawerk "in the 1880s", Fisher "in his 1930 *Theory of
  Interest*"; Schumpeter "in 1911", Knight "in 1921"; Piketty "(2013)". Every
  one is given the fact his view rests on.
- **Second person in `p` and `worked.intro` only.** "You want the general rate
  and the two prices" is the shape every worked intro takes; `steps`,
  `standard`, quiz items and tile text are impersonal throughout; no "Let's",
  no first-person anecdote anywhere.
- **Marx's jokes before the lesson's.** The shopkeeper who follows "small
  profits and quick returns" "on principle"; "What a pretty theoretical
  introduction to the national debt of England!"; the directors whose wages
  of superintendence "were inversely proportioned to the actual
  superintendence performed". The lesson's own light remark, the quicker bus
  that "makes nothing at the office, but you get more hours there"
  (`commercial-capital`), is one and is apt.
- **The limit admitted, and varied.** Each `note` names what its lab cannot
  show, and the closing move on the standard dispute is different each time:
  "computes on his side of it"; "leaves both disputes where they stand"; "a
  question about real markets this lab does not carry"; "goes no further";
  "cannot decide between the two accounts"; "cannot settle that"; "cannot say
  what it rewards"; "nothing about how long it can last". This answers
  Course 1's note that the move was repeated there.
- **Pointing forward by title.** Each body ends by naming the next lesson's
  question by its title, and `interest-bearing-capital-as-a-thing` ends with
  the next course by its §B title, Credit and Fictitious Capital, and its
  question ("claims on future income are bought and sold as if they were
  capital themselves").

**What differed from the reference, and what was changed:**

- **Grouped numbers.** Course 1's figures were small; this course's are
  Marx's 1,062 and 1,080 and Child's 102,400, and the read-out splits every
  grouped number at its comma. The convention earlier Capital reviews set
  (The Circuits of Capital, The Turnover of Capital, Average Profit and Its
  Fall) is a spoken form per run in `content/spoken/capital.py`; this course
  had no block. Added, see Speech below.
- **"mark-up" at the head of a key equation and at the end of a key line read
  "mark-u p"**, the same engine behaviour Course 1 met with `due` and `out`.
  Reworded in content rather than given spoken forms, as Course 1 did.
- **One scare quotation.** `the-rate-of-interest` wrote that economists argue
  over where the rate &ldquo;should&rdquo; be; the word is in the text, so
  the checker passed it, but on this Subject every `&ldquo;…&rdquo;` is read
  as Marx's. Now "ought to be", unquoted.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names the product: "size a
  merchant's capital from its turnovers"; "price the manufacturer's and the
  merchant's sale"; "find the mark-up per turnover… and show that the annual
  rate on his capital is the general rate"; "share out surplus value with a
  money-dealer in the averaging"; "compute a merchant's gain with and without
  a general rate"; "split the profit on borrowed capital… and state which of
  them the rate of interest changes"; "place a rate of interest within its
  bounds"; "split gross profit with a manager's salary… and state which part
  pays for labour"; "compare a compound claim with the growth of a product…
  and state from what the interest would have to be paid". The five course
  `outcomes` are the same acts.
- **One hard idea per lesson, and the chapters' own order.** Chapter 16 is
  only the form (commodity capital in other hands, `M–C–M′`, the same linen
  sold twice) and defers the profit to Chapter 17 by name; Chapter 17 is only
  the averaging; Chapter 18 only the inverse law of mark-up and turnover,
  with the `concepts` setting industrial turnover beside merchant's turnover
  so the reader sees the two work in opposite ways before the arithmetic;
  Chapter 19 is Chapter 17's averaging again with one more capital in it,
  and says so ("Four steps, extending those of 'Commercial Profit'"); Chapter
  20 steps outside the average; Chapter 21 is the split, Chapter 22 its
  bounds, Chapter 23 the manager, Chapter 24 the fetish. The `how_to` tells
  the reader to "Keep Marx's 900 and 100 in view" because three lessons use
  them, which is the right advice.
- **Marx's own figures, recomputed and right.** `180 / (900 + 100) = 9/50`;
  `900 + 162 = 1,062`; `1,062 + 18 = 1,080`; with 50 of costs `180 / 1,050 =
  6/35 = 17 1/7%`, `900 · 6/35 = 154 2/7`, `1,054 2/7 = 7,380/7`, and `1,130
  = 1,080 + 50`, all as Kerr l. 2717 and l. 2772 print them; 15% once is 115,
  five times is 103 and `500 sold 515`, ten times `£203/2`; 15% of £1 is 3s
  and 15% of 1s is 1⅘d, as l. 2883–2885; £100 at 20% and 5% is £20, £5 and
  £15; 20 and 8 and 16 and 4 both leave 12, as l. 3311; the 4½%, 2%, 1½% and
  8% of 1842–1847 are l. 3323's. For Chapter 24: `log10(1.05) · 1772 −
  log10(12) = 36.5`, so a penny at 5% for 1,772 years has 37 digits in
  shillings, and at 1%, `7.66 − 1.08 = 6.6`, 7 digits; `(21/20)^1772 /
  (101/100)^1772 = 10^29.9`, "thirty orders of magnitude"; `1.1^70 = 789.75`,
  so Child's £100 becomes about £78,975 (1,579,494s, 7 digits), against his
  `2^10 · 100 = 102,400`, which the lesson correctly reads as doubling every
  seven years; `1.02^70 = 4.00`, about £400, 4 digits in shillings; `78,975 /
  400 = 197`; `2,000 · (21/20)^10 = 3,257.79s = £162 17s 9½d`, which the tile
  prints exactly. Marx's footnote, that 5% interest presupposes 15% profit
  (5 paid, 5 spent, 5 capitalised), is given as his.
- **The misconceptions are refuted with the specific figure**, as listed in
  the Verdict, and the second and third `mistakes` catch the predictable
  neighbours: transport and storage confused with selling; a larger capital
  taken for more trade; the general rate reckoned on industry alone; costs
  taken to add value because they raise the price; the merchant thought to
  choose his margin; the merchant's law carried over to industry;
  "financial capital" read as lending; the old merchant's gain read as an
  exchange of equivalents; the lender's money thought to produce the
  interest; a breach of the ceiling treated as impossible; all supervision
  treated as coordination; compound arithmetic thought wrong; Price's sinking
  fund read as a way to abolish debt.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` says what goes in and
  which figures are Marx's; every quiz asks the same act on a fresh instance
  (£2,000 three times; 800 of industry, 200 of surplus value, 200 of
  merchants; 12% over four turnovers; a dealer's 200 beside Marx's 900 and
  100; £50 bought and £80 sold; £200 at 4% and 15%; 18% and 6%; £200 at 15%
  and 5% with an £8 manager; £100 at 10% for two years). Every distractor is
  a named error and was argued for: `£666⅔` divides where it should
  multiply; `25%` leaves the merchant out and `40%` adds his capital to the
  surplus value; `75` charges 15% on every sale; `36` uses the rate that held
  without the dealer; `3/8` divides by the sale price; `£38` adds the
  interest; `£24` adds them; `22` forgets the interest; `£120` is simple
  interest. None could be defended.
- **Marx is presented, not endorsed, and his critics are named where they
  belong.** Smith and the national accounts against "trade adds no value" in
  `commercial-capital`; the retailer's service and the transformation problem
  in `commercial-profit`; pricing strategy in
  `the-turnover-of-merchants-capital`; payment services as output in
  `money-dealing-capital`; Pirenne, Sweezy, Dobb and Brenner in
  `history-of-merchants-capital`, with Marx's own grant ("the discoveries of
  the sixteenth and seventeenth centuries… helped destroy feudal barriers",
  l. 3099) given before his denial; Böhm-Bawerk and Fisher in
  `interest-bearing-capital`, with time preference stated in their terms and
  not Senior's; Wicksell in `the-rate-of-interest`, with the natural rate
  defined as he defined it and "Wicksell's followers would answer that the
  level is fixed by saving and investment"; Schumpeter and Knight in
  `interest-and-profit-of-enterprise`, with the honest admission that "what
  in the chapter bears on them is limited: it does not discuss risk or
  innovation as sources of profit"; Piketty in
  `interest-bearing-capital-as-a-thing`, kept apart from Price ("It is a
  claim about shares, not Price's claim"). Every "Marx says" was traced to a
  line: the two elements that make the merchant a capitalist (l. 2624–2628),
  the first corollary (l. 2733), the clerks' wages falling with schooling
  (l. 2840), crises breaking out in wholesale trade and banking (l. 2871),
  the extra profit and the rent for a good location (l. 2956), the
  money-dealer's lack of a special form of circulation (l. 3010), the two
  roads (l. 3105), the hatter (l. 3204), the doubled profit (l. 3271), the
  ceiling, the floor and the exceptional cases (l. 3305), Massie and Hume
  (l. 3421), the owner lending to himself (l. 3411), the orchestra (l. 3484),
  Aristotle and O'Connor (l. 3495, l. 3499–3503), the co-operative factories
  (l. 3519), the pear tree (l. 3537), Pitt (l. 3569), the two reasons
  compounding stops (l. 3585–3588).
- **The seam at lesson 6 is Marx's.** `history-of-merchants-capital` ends
  "Part V begins with a capital even older than the merchant's and even
  further from production"; `interest-bearing-capital` opens "Part V opens
  with the lender". Both modules spell British, cite lessons by title and
  chapters by number, use the same `<strong>Volume III, Chapter n.</strong>`
  block, print Marx's formulas inside quotations as Kerr prints them
  (`M—M—C—M'—M'`) and in their own prose as `M–M′`, and say so in their
  module docstrings.
- **Figures agree with the lab.** Every pinned tile on the nine pages matched
  the observed tile: `£0`, `£3,000`, `£12,000`; `9/50 = 18%` with
  `industrial £1,062; merchant £1,080`, `1/5 = 20%` with `£1,080; £1,080`,
  `6/35 = 17.14%` with `industrial £7,380/7; merchant £1,130`; `3/100 = 3%`
  and `sells at £103`, `3/20 = 15%` and `£115`, `3/200 = 1.5%` and
  `£203/2`; `4/25 = 16%` with `£1,044`, `3/20 = 15%` with `£1,035`;
  `M–C–M′` with `+£40`, `+£75`, `+£18`; `£5`/`£15`, `£10`/`£10`,
  `£2`/`£18`; `£12` with `0 < 4% < 16%`, `£37/2` with `0 < 3/2% < 20%`,
  `£8`, `−£3` and `breached: 8% ≥ 5%`; `£0`/`£20`, `£5`/`£15`, `£5`/`£9`;
  the three compound tiles. Where a tile prints a fraction the prose reads
  it out (`£203/2`, "which is £101½"; `£37/2`, "which is £18½"; `£7,380/7`,
  "which is Marx's 1,054 2/7").

## What it taught badly, or said wrongly

### Fidelity

- **`interest-bearing-capital-as-a-thing`, body:** "Pitt believed him and in
  1786 set aside a sum each year". The Kerr text (l. 3569) dates the
  resolution to 1788 and cites "Act 26, George III, chap. 22"; 26 George III
  is 1786, so the lesson's date is the Act's and Marx's is the text's, and a
  reader following in the book would find them disagreeing. Now gives the
  chapter's figures instead of a date: the Act "set aside £250,000 a year to
  accumulate at compound interest until the fund should reach £4,000,000 a
  year".
- **`interest-and-profit-of-enterprise`, `worked.after`:** the £9 left after
  the manager's salary "rewards owning or commanding capital, not any work of
  superintendence". The chapter's words for the residue are "mere
  surplus-value, a value for which no equivalent was paid, realised unpaid
  labor" (l. 3525); "commanding capital" was the lesson's gloss. Now "is
  surplus value, unpaid labour, and not the price of any work of
  superintendence". The §C worked line, which paraphrases the same point in
  its own words, is a design pointer and was left.
- **`money-dealing-capital`, body:** "A capital lent to this business must
  earn the general rate". Lending is exactly what Chapter 19 sets aside for
  Part V, and the lesson says so two paragraphs earlier. Now "put into".
- **`the-rate-of-interest`, body:** the scare-quoted &ldquo;should&rdquo;,
  described above, removed.

### Prose that left the reader unexplained

- **`the-turnover-of-merchants-capital`, body:** "At 1 pound a pound of
  sugar, 100 pounds buys 100 lb… the same 100 pounds buys 2,000 lb" used
  "pound" for money and weight in one sentence. Now "At £1 for a pound of
  sugar, £100 buys 100 lb… the same £100 buys 2,000 lb… to make his £15",
  which is also how Kerr l. 2883 reads (1 p.st., 100 p.st.).
- **`the-turnover-of-merchants-capital`, quiz 3 `why`:** named "Roscher's
  'prudence and humanity'" as what Marx calls ridiculous, but no body
  paragraph had introduced Roscher. One clause added after the Dutch East
  India Company sentence: Marx "names one economist who had not seen it:
  Wilhelm Roscher of Leipzig, who could still imagine selling prices changed
  by a merchant's 'prudence and humanity' rather than by a change in
  production" (l. 2893).

### Quiz

- **`interest-bearing-capital`, quiz 2, distractor 2:** "Money in exchange
  for the borrower's promissory goods" was not a wrong model anyone holds,
  only an odd phrase. Now "Money in exchange for goods of equal value", the
  sale that Marx says lending is not, and the `why` already refutes it ("No
  equivalent is exchanged, so it is not a sale of money for goods").

### Speech

Every math run on the ten rendered pages was read from `data-say`. The
`capkit` fractions and formulas read well: `9 over 50`, `pounds 7380 over
7`, `M to M to C to M prime to M prime`, `0 is less than 4 percent is less
than 16 percent`, `compound sum equals c times the quantity 1 plus i, to the
power n`, `pounds 100 times the quantity 11 over 10, to the power 70`. Two
shapes read wrongly, neither flagged by the checker because each is all
words:

- **Grouped numbers split at the comma.** Twenty-two runs read "pounds 3,
  000", "1, 062", "17 1 over 7 percent", "154 2 over 7", "1, 772 years",
  "pounds 102, 400". Following the convention the Circuits, Turnover and
  Average Profit reviews set, a block headed `# Merchant's Capital and
  Interest` was appended to `content/spoken/capital.py` with the same
  twenty-two runs ungrouped and the two mixed numbers in words ("17 and 1
  seventh percent", "154 and 2 sevenths"), each spoken form generated by the
  engine from the ungrouped run and then read. The file was re-read
  immediately before the append and only the new block was written.
- **"mark-up" read "mark-u p"** at the head of the key equation `mark-up =
  annual rate / turnovers` (in the course `key` and the lesson's) and at the
  end of `faster turnover, smaller mark-up`. Now `addition per sale = annual
  rate / turnovers` and `faster turnover, a smaller addition per sale`,
  which is Marx's own term ("the mercantile addition to the price"). The
  worked line `mark-up:  15% / 5 = 3% a turnover` already read correctly and
  stands; the tile label "Mark-up on each turnover" is not a run.

A second pass over every `data-say` on the ten pages after the changes finds
no split number, no spelled word and no two-number mixed fraction.

### Cross-references

Lessons are cited by title (“Commercial Profit”, “The Turnover of Merchant's
Capital”, “Money-Dealing Capital”, “Historical Facts about Merchant's
Capital”, “Interest-Bearing Capital”, “The Rate of Interest”, “Interest and
Profit of Enterprise”, “Interest-Bearing Capital as a Thing”), each exactly as
the next lesson carries it; “The Costs of Circulation” is the title of the
Circuits of Capital lesson and “Compound Interest and Continuous Growth” of
the Algebra lesson they point to; Marx's chapters by volume and number, as
§0's first deviation requires; earlier courses by their §B titles (Cost Price
and the Rate of Profit, Average Profit and Its Fall, The Circuits of Capital)
and the next course by its, Credit and Fictitious Capital. No lesson is cited
by number. Chapter 19's `module` keeps Untermann's "Financial Capital" as
§E.3 requires and the lesson says once why its own prose does not.

## Can a reader who has finished Average Profit and Its Fall follow the nine lessons?

Yes, and the places a reader slows are the places Marx's readers slow.

- **Lesson 1** has the least arithmetic in the course and is right to: the
  chapter's one quantity is how much commodity capital a merchant carries,
  and the lesson spends its weight on the form, on "what changes hands
  twice", which the reader will need for Chapter 21's `M—M—C—M'—M'`. The
  qualification "at least not directly" is given its own quotation block and
  a paragraph, and that is the paragraph in which the standard objection
  belongs and is.
- **Lesson 2** is where the course turns and the lesson says so: "the rate
  itself must be worked out again". A reader who has just left Chapter 9's
  averaging is told that the averaging was done "before merchant's capital
  existed in the analysis", and then watches the 180 spread over 1,000. The
  `no-merchant` preset gives the Part II rate back so the difference is seen
  as a difference. The 50 of costs are a second hard idea on the same page;
  the lesson keeps them to one paragraph and one preset and explains the
  fraction the tile prints, which is the right amount.
- **Lesson 3** will be the one readers argue with, because firms do choose
  margins, and the lesson gives the objection a paragraph of its own and
  Marx's reply as Marx's. The sugar example is now readable aloud. The two
  qualifications (extra profit above the line's average, and merchants
  running ahead of consumption) keep the law honest without a second lab.
- **Lesson 4** is honest about its lab: one field for the capital in
  circulation, the split done in prose at the common rate, "The money-dealers'
  capitals are illustrative", "Marx gives no figures in this chapter". The
  default preset is `cashier`, so the reader lands on the figure that is new.
- **Lesson 5** is the course's narrative lesson and computes the mechanism
  §0 asks for: the same `M–C–M′` with and without a general rate behind it.
  The `capitalist` preset's `+£18` ties it back to Lesson 2.
- **Lesson 6** does the course's second turn, from averaging to splitting,
  with Marx's own £100 and one new idea: that the £20 does not move and
  "What the rate of interest decides is only who gets how much of it". The
  Proudhon paragraph is a model of §F rule 3.
- **Lesson 7** teaches a negative result, that there is no law, which is
  hard to make a lesson of; it does so by giving the reader the one thing
  that can be computed (the bounds) and a preset in which they are breached,
  and by letting the barometer image carry the chapter's irony.
- **Lesson 8** has one honest tension between the lab and the chapter: the
  `owner` preset books `£0` of interest, which is what the kit computes,
  while Marx's point is that the owner reckons £5 to himself. The lesson
  explains the difference in the body, in `mistakes[1]` and in the `note`,
  and the manager preset carries the lesson's real argument. See Remaining
  issues.
- **Lesson 9** ends the course on a sum a reader can feel, and the
  `ten-years` preset is the pedagogical key: the two tiles print the same
  number, so the reader sees what Price's claim would need (a product growing
  at the rate of interest) before being told it cannot be had for 1,772
  years. The Algebra cross-reference tells a reader where the formula was
  derived.

## Repairs made in this pass

In `content/capital/c11_interest/__init__.py`: `key[1]`. In `part_a.py`:
`the-turnover-of-merchants-capital` `key[1]`, `key[4]`, the sugar paragraph,
the Dutch East India Company sentence (Roscher); `money-dealing-capital` the
"Then the profit" paragraph. In `part_b.py`: `interest-bearing-capital` quiz
2 distractor; `the-rate-of-interest` the "Interest rates are news"
paragraph; `interest-and-profit-of-enterprise` `worked.after`;
`interest-bearing-capital-as-a-thing` the Pitt sentence. In
`content/spoken/capital.py`: a new block of twenty-two spoken forms headed
`# Merchant's Capital and Interest`, appended after a fresh re-read; no
other course's block touched. No preset, `expect`, slug, module, lab key,
mode or view changed, and no §C entry needed correcting: every instance the
lessons carry is the one §C records.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-merchants-and-interest` reports OK: 10 pages, 9 labs executed and
swept, 9 with pinned figures, 0 failing, no math run without a spoken form;
the strict quotation checker reports 90 segments, 0 misses.

## Remaining issues

- **The `interest`/`split` view books interest only on `principal`**, so
  Chapter 23's owner, who "divides the gross profit into interest due to
  himself as its owner lending it to himself", is shown with `£0` of interest
  where the chapter's point is `£5`. The lesson explains it three times, but
  a reader who presses `owner` sees the lab contradict the paragraph above
  it. A `reckoned` field or a third tile ("interest reckoned to the owner")
  belongs to the kit, not to this course. Recorded, not changed.
- **The `prices`/`merchant` view has one field for capital in circulation**,
  so `money-dealing-capital` enters the merchant's 100 and the dealer's 125
  as 225 and splits the profit in prose. A second field, or a `dealer_capital`
  that the tile reports separately, would let the lesson pin the cashier's
  20. Recorded for the kit.
- **The read-out splits every grouped number at its comma.** Six Capital
  courses now carry a spoken block whose only job is to read "1,062" as
  "1062". A rule in `speech.py` that reads a digit-comma-three-digits group
  as one number is chrome-renderer work and would retire all six blocks.
  Recorded, as the Turnover review recorded it.
- **"mark-up" is spelled out when it opens or closes a run.** The two cases
  here were reworded; the next course whose key line begins with a hyphenated
  word ending in a short syllable will meet it again. Same tier as above.
- **The `compound` view's exact sum prints a fractional penny as
  `9 602934603/1280000000 d`**, which the kit report already lists as a
  requested change to `capMoney`. The lesson reads it out as "about £162 17s
  9½d", so no reader is stranded; a kit change was not made.
