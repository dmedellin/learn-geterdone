# Capital, Read Along — the build specification

This is the curriculum, lab and authoring contract for the tenth Subject: a
read-along of Karl Marx's *Capital*, all three volumes, one lesson per chapter
(more where a chapter carries more than one hard idea). Everything an author, a
kit engineer or a reviewer needs is here. Where it says "exactly", a test or a
gate enforces it. Where it says "never", a published page somewhere in this
library has already been wrong for that reason.

Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight note;
`content/AGENTS.md` (all of it); `scripts/mathpath/AGENTS.md` ("a preset's two
claims"); and `docs/philosophy/PLAN.md` §D.0 and §E, whose conventions this
document adopts by reference and does not repeat.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The fourteen courses, in order
- §C Every lesson: 119 entries
- §D The lab kit: `capkit` (17 modes)
- §E Package layout, the author's checklist, and how a passage is quoted
- §F Voice: the read-along, after the three lectures
- §G What is left out, and why
- §H Wiring notes for the orchestrator
- §R Review record

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For a reading of *Capital* the answer is unusually good, because Marx
does his own arithmetic on the page and asks the reader to check it. The spinning
mill of Chapter 7 is a ledger in shillings; the working day of Chapter 10 is a line
cut into two segments; the reproduction schemes of Volume II are a two-sector
balance that either closes or does not; the five spheres of Volume III, Chapter 9
are a table whose column sums Marx asserts are equal; the four soils of Chapter 39
are a rent schedule. A read-along that skips the arithmetic skips the argument.

So the claim this Subject makes, and the only one it makes, is this: **every
figure is computed in the browser from the quantities the lesson states, in exact
rational arithmetic, using the definitions Marx gives in the chapter being
read.** The lab does not claim those definitions describe any actual economy.
Whether labour-time determines value, whether the rate of profit tends to fall in
fact, whether a reserve army disciplines wages today — those are the questions the
Subject leaves open on purpose, and it says so in the material clause.

Eighteen kinds of computation, in seventeen modes, carry the whole of it:

| what the reader computes | mode | from |
| --- | --- | --- |
| socially necessary labour-time per unit, a commodity's value, an exchange ratio | `value` | producers' hours and outputs, a skill multiplier |
| the elementary, expanded, general and money forms of one set of values | `form` | labour-values of up to six commodities and a chosen equivalent |
| prices in gold, the money needed in circulation, net payments, the drain abroad | `money` | values, gold's value, velocity, credit and payments |
| what circulation adds to the sum of values, and what buying labour-power adds | `circuit` | sellers' mark-ups, the value of a day's subsistence, hours worked |
| the value of a product, s, the rate s/v, the product in parts, the mass of s | `surplus` | materials, wear, wages, hours, workers |
| necessary and surplus labour on one working day, absolute and relative change | `workday` | length of day, value of labour-power, productivity, intensity |
| what co-operation, detail labour and machines transfer and displace | `machine` | workers, outputs, machine value and life, the wage bill |
| the price of labour, time-rates, piece-rates and their hidden lengthening | `wages` | value of labour-power, normal day, output per hour |
| capital period by period: consumed, accumulated, composition, the reserve army | `accumulate` | capital, s/v, share accumulated, rise in c/v, labour supply |
| turnover time, turnovers a year, fixed and circulating, capital advanced | `turnover` | working, production and circulation periods, lifetimes |
| whether a two-department economy reproduces itself, and its growth path | `schemes` | Department I and II c, v, s and accumulation shares |
| cost price, the rate of profit, and its relation to s/v and turnover | `profit` | c, v, s, turnovers, price changes in c |
| the general rate of profit and prices of production across spheres | `prices` | up to six spheres' c, v, used-up c, s/v; a merchant's capital |
| the rate of profit under a rising composition, and what counteracts it | `tendency` | starting c/v, s/v, the rise per period, offsets |
| interest and profit of enterprise; the price of a claim on income | `interest` | profit, the rate of interest, an income stream |
| differential rent I and II, absolute rent, the price of land | `rent` | soils' outputs and capitals, the regulating price, the rate of interest |
| the annual product as c + v + s and the trinity formula's missing c | `revenue` | the product's value parts and the split of s |
| the gap between a rule's two classifications of the same capital | `turnover` (view `classify`) | a capital's items, tagged fixed/circulating and constant/variable |

Every quantity is a whole number or a fraction. Money is in the units the chapter
uses — shillings, pounds, or "hours" when Marx reckons in labour-time — and a
tile never converts between them silently.

**Historical chapters compute too, from the mechanism they describe.** Part
Eight of Volume I and the historical chapters of Volume III (20, 36, 47) are
narrative. Each is paired with the mode that computes the mechanism the narrative
is about: expropriation is the moment a smallholder's whole working day becomes a
day with a surplus in it (`workday`); the price revolution of Chapter 29 is a money
rent fixed while gold cheapens (`money`); the national debt of Chapter 31 is a
claim capitalised at the rate of interest (`interest`); labour rent in Chapter 47
is the working day split between the lord's field and one's own (`workday`).
Where a preset uses Marx's own figures it says so in its label; where it uses
illustrative figures the lesson says so in prose. No lesson carries a decorative
lab, and a lab that merely restates a narrative is decorative.

**Deliberate deviations from the library's conventions, recorded here so no
reviewer has to rediscover them:**

1. **Cross-references to *Capital* are by volume and chapter number.** The
   library's rule is "by title, never by number". For a read-along the chapter
   number is the reader's page reference, and the lesson is useless without it.
   Lessons on this path are still cross-referenced by title (“The Working Day”);
   Marx's chapters are cited by number ("Volume I, Chapter 10").
2. **One kit for the Subject**, not one per course. Every course reuses the same
   seventeen modes because Volume III re-reads Volume I's categories at a higher
   level of concreteness, and the kit should make that visible: the rate of
   profit is computed from the same c, v and s the reader built in the spinning
   mill.
3. **The passage comes first.** The read-along needs the text in front of the
   reader before it is explained, the way the lectures read the chapter whole
   before going line by line. This uses the existing structure, with no renderer
   change: the first `body` block is a `p` holding the quotation and its
   citation (§E.3), and `read_title`/`read_intro` say that the passage comes first.
4. **The voice** (§F) is warmer and more spoken than the library's default, by
   the operator's instruction. It keeps every hard rule of §F in the philosophy
   plan that concerns correctness and drops the ones that concern register.

---

## §A PATH fields (`content/capital/__init__.py`)

```
"slug": "capital",
"title": "Capital, Read Along",
"level": "Beginner → Advanced",
"level_note": "school arithmetic only; no economics is assumed",
```

**tagline** (counts re-verified at wiring by
`test_the_tagline_and_description_state_the_real_counts`):

> Karl Marx&rsquo;s <em>Capital</em>, read chapter by chapter, all three volumes &mdash; with
> the arithmetic Marx does on the page done in front of you: value and money,
> the working day, surplus value, wages, accumulation, turnover, reproduction,
> profit, prices of production, interest and rent. Fourteen courses and 119
> lessons are available.

**description**:

> The Capital Subject: a read-along of all three volumes in Marx's own order,
> fourteen courses that follow his Parts, a lesson for every chapter and more
> for the long ones. Each lesson reads a passage first, then explains it, then
> computes what the chapter computes &mdash; a commodity's value, a rate of
> surplus value, a reproduction scheme that balances or does not, a price of
> production, a rent schedule &mdash; in exact arithmetic in your browser. All
> fourteen courses and 119 lessons are available.

**key** (each line ≤ 46 characters, no second column):

```
value of product = c + v + s
rate of surplus value  s′ = s / v
day = necessary + surplus labour
simple reproduction: I(v + s) = II c
rate of profit  p′ = s / (c + v)
price of production = k + k · p̄′
price of land = rent / rate of interest
```

**material** (must differ from every existing clause; proposed
`CAP_DISCLAIMER_RE = r"only as good as the definitions"`):

> every figure on this path is computed in your browser from the quantities a
> lesson states and the definitions Marx gives in the chapter being read, and a
> figure is only as good as the definitions it was computed from &mdash; whether
> they describe the economy you live in is the question the book argues and the
> lab cannot settle.

**prerequisites** (paragraphs):

1. School arithmetic: fractions, percentages and a willingness to add up a
   column. Marx's examples are in shillings, pounds and hours, and every one of
   them is a sum or a ratio. The labs do the arithmetic; what is asked of you is
   to say what each number means.
2. No economics. The Subject introduces every category it uses in the chapter
   where Marx introduces it, and it introduces the classical economists Marx is
   arguing with — Smith, Ricardo, Say, Senior, Mill — at the moment he argues
   with them. If you have studied modern economics, expect to unlearn some
   vocabulary: "capital", "profit" and "value" do not mean here what they mean
   in a textbook, and the first lessons say exactly how.
3. A copy of the book is welcome but not required. Every lesson quotes the
   passage it reads from the public-domain Kerr editions: Volume I in the Moore
   and Aveling translation as revised by Ernest Untermann, Volumes II and III in
   Untermann's translation. Chapter numbers follow the English edition of
   Volume I, which differs from the German from Chapter 4 on; the two places
   where that matters say so.
4. Patience with abstraction. Volume I assumes that commodities sell at their
   values; Volume III takes that assumption away. A reader who stops after
   Volume I has read the first half of an argument, and several lessons say so
   on purpose.

**why_order** (paragraphs):

1. The order is Marx's, and it is the order of the argument. Volume I studies
   capital in production, under the simplifying assumption that everything sells
   at its value; Volume II studies capital in circulation, where time and
   balance enter; Volume III puts the two together and lets competition, credit
   and landed property break the simplifications one by one.
2. Commodities and money come first because every later category is built from
   them. Surplus value cannot be stated before value is, and capital cannot be
   distinguished from money before money is.
3. The historical Part Eight of Volume I comes after accumulation, not before,
   because Marx wants the reader to see the mechanism first and then ask where
   the first capital came from. Read in the book's order, the history answers a
   question the reader already has.
4. Volume III's profit, interest and rent come last because each is a share of
   surplus value under another name. Read without Volume I they look like three
   separate incomes from three separate sources, which is exactly the
   appearance the last course, Revenues and Their Sources, takes apart.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. From Money to Surplus
> Value uses the value of Commodities and Money; Relative Surplus Value uses the
> working day; Wages and Accumulation uses all of Volume I's arithmetic; the three
> Volume II courses add time and the balance of two departments; the Volume III
> courses re-read every one of those categories as profit, prices of production,
> interest and rent; Revenues and Their Sources uses all of it.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what the lesson states: a value is total hours
> over total output, a rate of surplus value is a ratio of two sums, a scheme
> balances or it does not, a price of production is a cost price plus the
> average profit. Nothing is rounded except where a lesson says so. Quotations
> are from the public-domain Kerr editions, as published in the Online Library
> of Liberty. What the labs cannot do is
> tell you whether Marx's definitions are the right ones &mdash; and that is
> what the book is arguing about.

---

## §B The fourteen courses

Volumes and Parts are Marx's. Courses group short Parts and never split one,
except Volume III's Part Five, which is sixteen chapters long and divides where
Marx's own manuscript changes subject (from interest to the credit system).

| # | slug | title | Marx | lessons | level |
| --- | --- | --- | --- | --- | --- |
| 1 | `capital-commodities-and-money` | Commodities and Money | Vol I, Part I (ch. 1–3) | 8 | Beginner |
| 2 | `capital-money-into-surplus-value` | From Money to Surplus Value | Vol I, Parts II–III (ch. 4–11) | 10 | Beginner |
| 3 | `capital-relative-surplus-value` | Relative Surplus Value | Vol I, Parts IV–V (ch. 12–18) | 9 | Intermediate |
| 4 | `capital-wages-and-accumulation` | Wages and Accumulation | Vol I, Parts VI–VII (ch. 19–25) | 9 | Intermediate |
| 5 | `capital-primitive-accumulation` | So-Called Primitive Accumulation | Vol I, Part VIII (ch. 26–33) | 8 | Intermediate |
| 6 | `capital-circuits-of-capital` | The Circuits of Capital | Vol II, Part I (ch. 1–6) | 6 | Intermediate |
| 7 | `capital-turnover-of-capital` | The Turnover of Capital | Vol II, Part II (ch. 7–17) | 11 | Intermediate |
| 8 | `capital-social-reproduction` | Reproduction of the Social Capital | Vol II, Part III (ch. 18–21) | 6 | Advanced |
| 9 | `capital-cost-price-and-profit` | Cost Price and the Rate of Profit | Vol III, Part I (ch. 1–7) | 7 | Intermediate |
| 10 | `capital-prices-of-production` | Average Profit and Its Fall | Vol III, Parts II–III (ch. 8–15) | 8 | Advanced |
| 11 | `capital-merchants-and-interest` | Merchant's Capital and Interest | Vol III, Parts IV–V (ch. 16–24) | 9 | Advanced |
| 12 | `capital-credit-and-fictitious-capital` | Credit and Fictitious Capital | Vol III, Part V (ch. 25–36) | 12 | Advanced |
| 13 | `capital-ground-rent` | Ground Rent | Vol III, Part VI (ch. 37–47) | 11 | Advanced |
| 14 | `capital-revenues-and-their-sources` | Revenues and Their Sources | Vol III, Part VII (ch. 48–52) | 5 | Advanced |

Total 119. "So-Called" in Course 5's title is Marx's German (*Die sogenannte ursprüngliche Akkumulation*); the 1887 English edition's Part is titled "Primitive Accumulation", and the course summary says so. The `capital-` prefix keeps course slugs from colliding with the
generic names other Subjects already use and tells a reader landing on a course
URL which book it belongs to.

Each course's `module` names are the book's chapters: `Chapter 1 · Commodities`.
A course's `summary` names the Part; its `assumes_long` names earlier courses by
title. Course `key` lines are drawn from that course's own formulas.

Chapter splits (one hard idea per lesson): Volume I Chapter 1 (four lessons,
one per section), Chapter 3 (three), Chapter 9 (two: the rate, and Senior's last hour), Chapter 10 (two), Chapter 15 (three),
Chapter 25 (three); Volume II Chapters 20 and 21 (two each). Every other
chapter is one lesson. Two adjacent chapters are never merged into one lesson;
where a chapter is short (Volume II Chapter 18, Volume III Chapter 7) its lesson
is short.

---

## §C Every lesson

Format of each entry:

- **slug** — Title — *module* (= chapter)
- **Read:** the passage the lesson opens with, located by section (the author
  fetches it verbatim; §E.3).
- **Do:** the observable objective; the `standard` field measures it.
- **Lab:** mode; presets by id with their instance; pins.
- **Misconception:** the wrong model `mistakes[0]` must name and refute.
- **Worked:** the single worked example, in one line.

Preset ids are suggestions; the INSTANCES are not optional. Where an entry
gives only an id, the id is a placeholder: the author designs the instance, records it in this
section in the same commit as the lesson, and a reviewer rejects a lesson whose entry still
carries a bare id.

**Read** lines locate the passage by section and subject. Their wording is a pointer, never
a quotation to copy: the words quoted on the page come only from the Kerr text (§E.3).
Where an entry says "Kerr wording to be checked", the reviewers found the spec's phrasing
absent from the text they checked.

**Misconceptions** (`mistakes[0]`) are misreadings of the chapter's definitions or arithmetic,
refuted by a tile. They are never claims about what happened in history, what is just, or
which school of economics is right. Where the misconception is a position someone holds
(Hume's quantity theory, Say's law, the Currency School, the compensation theorists), the
lesson names its holder and states it at full strength before Marx's reply.

**Do** lines are acts the quiz measures: compute, classify, name, compare. "Say why" belongs
in the prose, not in the objective. Tile ids are fixed by
§D. Expected strings are read off the built page with `node scripts/labcheck.js
--observe`, never predicted. "Marx's figures" means the instance is the one in
the chapter and the label says so ("Marx's spinning mill: 10 lb cotton").

### Course 1 — Commodities and Money (`capital-commodities-and-money`, 8)

1. **the-two-factors-of-a-commodity** — The Two Factors of a Commodity — *Chapter 1 · Commodities*
   - Read: §1, the opening sentence ("The wealth of those societies…"), and the definition of socially necessary labour-time ("…under the normal conditions of production, and with the average degree of skill and intensity prevalent at the time").
   - Do: given several producers' hours and outputs, compute the socially necessary labour-time per unit and the value of a lot, and compute how much of the slowest producer's extra hours his own product carries (only his share of the average: in `slow`, 8 of his 40 extra hours). *Corrected in authoring: on the lab's weighted average the slow producer's hours are not "nothing"; they raise every unit's value by his share of output.*
   - Lab: `value`, view `snlt`, `qty_unit` yards, lot 20 yards. Presets: `linen` (three weavers at 1 h, 2 h, 3 h a yard, outputs 40, 40, 20 yards: `9/5 h`, `36 h`), `slow` (the same three weavers, the slowest now at 5 h a yard: `11/5 h`, `44 h`), `power-loom` (Marx's example: after the power-loom, a hand-loom weaver's hour counts as half an hour; the two largest producers at half their hours: `6/5 h`, `24 h`). Pin `vaSnlt`, `vaLotValue`.
   - Misconception: a commodity made more slowly is worth more.
   - Worked: 100 yards made in 180 hours in all is 9/5 hour a yard; the weaver who needed 3 hours a yard sells at 9/5 like everyone else.
   - Note to author: the lab's weighted average is a model of "normal conditions", not Marx's definition; Volume III, Chapter 10 shows the regulating value need not be the average, and the `note` says so.

2. **the-twofold-character-of-labour** — The Twofold Character of Labour — *Chapter 1 · Commodities*
   - Read: §2, the full sentence ending "…this point is the pivot on which a clear comprehension of political economy turns".
   - Do: separate the useful-labour side (coats, yards) from the value side (hours) for one industry, and compute what a change in productivity does to each.
   - Lab: `value`, view `skill` with `skill` fixed at 1, `basis` total, the lot = the day's output. Presets: `coat` (tailor 10 h for 1 coat: `10 h`, `10 h`), `doubled` (tailoring productivity doubles: 2 coats in 10 h: per unit `5 h`, lot `10 h`), `halved` (it halves: ½ coat in 10 h: per unit `20 h`, lot `10 h`). Pin `vaLotValue`, `vaPerUnit`. *Changed in authoring: `coat-linen` became `coat`, because the `value` mode averages over producers of one product, so a tailor and a weaver cannot share an instance; the linen comparison (a coat at 5 h is worth 10 yards) is in prose.*
   - Misconception: more useful things always means more value.
   - Worked: double the productivity of tailoring and two coats now carry the value one did; the use-values doubled, the value did not.
   - Skilled labour as "multiplied simple labour" is stated in prose and in `note` as an assumption the chapter makes; it is not a preset, because the reduction is not computed from anything.

3. **the-form-of-value** — The Form of Value — *Chapter 1 · Commodities*
   - Read: §3, "20 yards of linen = 1 coat, or: 20 yards of linen are worth 1 coat".
   - Do: write the elementary, expanded, general and money forms for a set of commodities from their labour-values, name the relative and the equivalent form, and compute how the linen's relative value moves when only the coat's value changes.
   - Lab: `form`, view `stage`, shipped `stage = elementary`. Presets: `marx` (Marx's figures: 20 yards linen = 1 coat = 10 lb tea = 40 lb coffee = 1 quarter corn = 2 oz gold = ½ ton iron, each lot 20 h so the equations hold; equivalent linen: `20 yards linen = 1 coat`, `1 coat`), `coat-cheapens` (the coat's hours halve to 10, the linen's do not: `20 yards linen = 2 coat`), `gold` (gold as the equivalent and listed second, so the elementary form is Marx's price form: `20 yards linen = 2 ounces gold`). Pin `foEquation`, `foRelative`.
   - Misconception: in "20 yards of linen = 1 coat" the coat's value is what is being expressed.
   - Worked: halve the hours in a coat and 20 yards of linen now fetch 2 coats: the linen's value is expressed differently though nothing about linen changed.

4. **the-fetishism-of-commodities** — The Fetishism of Commodities — *Chapter 1 · Commodities*
   - Read: §4, "A commodity appears, at first sight, a very trivial thing…" and Robinson Crusoe's ledger.
   - Do: compute the hours behind each product in Robinson's ledger and the association's shares, and compare them with the ratios the village's prices give.
   - Lab: `value`, view `ledger`. Presets (illustrative hours): `robinson` (goats 10 h for 2, fish 15 h for 30, furniture 12 h for 2, tools 3 h for 1: `40 h`), `village` (four households, 30 h each on one product, same hours per unit: `120 h`), `association` (an association's output, 45/40/42/33 h for 9/80/7/11: `160 h`); `vaPerUnit` is `goats 5 h, fish 1/2 h, furniture 6 h, tools 3 h` in all three. Pin `vaTotalHours`, `vaPerUnit`. *The ledger view shows no prices and no allocation to members; the village's ratios and the association's shares by hours are in prose.*
   - Misconception: value is a physical property of the thing, like weight.
   - Worked: Robinson's table and the market's prices give the same ratios; only one of them tells you whose hours they were.

5. **exchange** — Exchange — *Chapter 2 · Exchange*
   - Read: "It is plain that commodities cannot go to market and make exchanges of their own account."
   - Do: count the bilateral ratios a market of n owners needs with and without a single equivalent.
   - Lab: `form`, view `count`. Presets: `four` (four commodities, linen as equivalent: `6`, `3`), `six` (six, cattle as equivalent: `15`, `5`), `six-gold` (six, gold as equivalent: `15`, `5`; identical to `six` on purpose, since the count does not depend on which commodity is the equivalent). Pin `foPairs`, `foWithEquivalent`.
   - Misconception: money is a mere symbol fixed by convention.
   - Worked: six owners need fifteen ratios to trade by barter and five once one commodity is everyone's equivalent. The count shows why one equivalent is needed; Marx's point is how it arises — "a social act" of the owners, who "acted and transacted before they thought" — and the `note` says the lab cannot show that.

6. **money-as-measure-and-means-of-circulation** — Money as Measure and Means of Circulation — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §1 on price as "the money-name of the labour realised in a commodity"; §2(b) on the quantity of money in circulation.
   - Do: compute prices from values and gold's value, and the money needed to circulate a day's sales at a given velocity; then compute prices again after gold's value changes and no commodity's does.
   - Lab: `money`, view `circulate`. Each commodity 20 h, £1 = 10 h (illustrative hours, Marx's prices). Presets: `marx` (Marx's figures: 1 quarter wheat, 20 yards linen, a bible, 4 gallons brandy at £2 each, velocity 4 when they change hands in sequence: `£8`, `£2`), `side-by-side` (added in authoring: Marx's other case, the four sold simultaneously, velocity 1: `£8`, `£8`), `gold-falls` (gold's value halves, £1 = 5 h: `£16`, `£4`), `faster` (velocity 8: `£8`, `£1`). Pin `moNeeded`, `moPriceSum`.
   - Misconception (as Marx frames it, against Hume and Ricardo): with gold coin, prices are set by the quantity of money in circulation. State Hume's version at full strength; Marx argues the causation runs the other way for metal, and in §2(c) agrees that paper issued beyond the gold it represents raises prices. The measure of value is kept apart from the standard of price, and §2(a)'s point — that sale and purchase can come apart, the first possibility of crisis — is stated in prose and carried into the next lesson.
   - Worked: four commodities at £2 each, sold one after another by the same two sovereigns' worth of coin: price sum £8, velocity 4, money needed £2.

7. **hoards-and-means-of-payment** — Hoards and Means of Payment — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §3(b), the law of the quantity of money once payments fall due.
   - Do: compute money needed with credit sales and mutually cancelling payments, and say why a chain of debts makes a crisis a money crisis.
   - Lab: `money`, view `payments`, velocity 1, three goods of £100. Presets: `cash` (no credit: `£300`, `£0`), `chain` (credit sales 300, due 300, cancelling 300; bills A→B, B→C, C→A £100 each: `£0`, `£0`), `broken` (the same chain, bill 1 unpaid; due 200, cancelling 100: `£100`, `£100`). Pin `moNeeded`, `moNetted`.
   - Misconception: money only matters as a medium of exchange.
   - Worked: £300 of debts in a circle cancel to £0 in cash; break one link and £100 is suddenly needed in hard money.

8. **world-money** — World Money — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §3(c), "When money leaves the home sphere of circulation, it strips off the local garbs…".
   - Do: compute the balance between two countries' payments and the bullion that settles it.
   - Lab: `money`, view `world`. Presets: `balanced` (imports and exports £1,000: `£0`), `deficit` (imports £1,000, exports £800: `£200 out`), `drain` (the same and £100 owed abroad, other receipts −100: `£300 out`). Pin `moDrain`.
   - Misconception: world money is just a currency exchanged at a rate.
   - Worked: imports of £1,000 against exports of £800 leave £200 to be shipped in bullion, the "universal medium of payment" (Kerr's wording; corrected from "means").

### Course 2 — From Money to Surplus Value (`capital-money-into-surplus-value`, 10)

1. **the-general-formula-for-capital** — The General Formula for Capital — *Chapter 4 · The General Formula for Capital*
   - Read: "The simple circulation of commodities — selling in order to buy — is a means of carrying out a purpose unconnected with circulation…".
   - Do: tell C–M–C from M–C–M′ by what is at either end, and compute the increment ΔM for given purchases and sales.
   - Lab: `circuit`, view `formula`. Presets: `cmc` (Marx's ch. 4 example: a quarter of corn sold for £3, clothes bought for £3), `mcm` (£100 of cotton sold for £110), `mcm-loss` (sold for £90). Pin `ciDelta`, `ciForm`.
   - Misconception: selling to buy and buying to sell are one circulation seen from two starting points.
   - Worked: corn → £3 → clothes ends where it started in value, ΔM = 0; £100 → cotton → £110 makes sense only because of the £10.

2. **contradictions-in-the-general-formula** — Contradictions in the General Formula — *Chapter 5 · Contradictions in the General Formula of Capital*
   - Read: the sentence ending "…it is equally impossible for it to originate apart from circulation" (verbatim from the Kerr text).
   - Do: show that if every seller marks up by the same percentage the total value in hands does not change, and that one cheat's gain is another's loss.
   - Lab: `circuit`, view `markup`. Presets: `ten` (three traders holding £100 each, every seller 10% above value: £300 before and after), `one-cheat` (Marx's A, wine £40 at a mark-up of 1/4, and B, corn £50 at value: £90 before and after), `merchants` (a producer selling £100 at value to three dealers who each add 10%: £400 before and after, the producer −£10, the first dealer +£10; in a ring of dealers alone the preset would repeat `ten`, so a party who does not mark up is added). Pin `ciTotalBefore`, `ciTotalAfter`.
   - Misconception: profit comes from selling above value.
   - Worked: A sells wine worth £40 to B and gets corn worth £50 in exchange (Marx's barter); the total value held by A and B is £90 before and after.

3. **buying-and-selling-labour-power** — The Buying and Selling of Labour-Power — *Chapter 6 · The Buying and Selling of Labour-Power*
   - Read: the labourer "free in the double sense", and the departure from "this noisy sphere… a very Eden of the innate rights of man".
   - Do: compute the daily value of labour-power from the value of a worker's means of subsistence, including weekly, yearly and generational items.
   - Lab: `circuit`, view `labour-power`. Money unit hours. Presets: `daily` (food and fuel 4 h every day, clothes 7 h every 7 days, furniture 365 h every 365 days: 6 h, Marx's figure), `family` (add children's upkeep, 2 h a day: 8 h), `training` (add 2,190 h of training over 10,950 days, Marx's 30-year working life: 31/5 h). Pin `ciLpValue`.
   - Misconception: the worker sells labour; the capitalist buys hours of work done.
   - Worked: 4 hours of daily needs + 7 hours a week of clothes + 365 hours a year of furniture is 4 + 1 + 1 = 6 hours a day, Marx's 6 hours, priced at his 3s. (Corrected from 6 + 1 + 1 = 8 so the total is the chapter's own figure.)

4. **the-labour-process-and-surplus-value** — The Labour Process and the Production of Surplus Value — *Chapter 7 · The Labour-Process and the Process of Producing Surplus-Value*
   - Read: §2, Marx's spinning mill, "Our capitalist stares in astonishment."
   - Do: compute the value of the yarn from cotton, spindle wear and labour, first for 6 hours and then for 12, and compute the difference between the value of a day's labour-power and the value a day's labour adds.
   - Lab: `surplus`, view `mill`. Presets: `six` (Marx's figures: 10 lb cotton 10s, spindle wear 2s, labour-power 3s a day, 6 hours of spinning adding 3s), `twelve` (12 hours: 20 lb cotton 20s, wear 4s, labour-power still 3s, 12 hours adding 6s), `waste` (12 hours, 22s of cotton of which 2s is beyond the socially necessary: product 30s, surplus 1s). Pin `suProduct`, `suS`.
   - Misconception: the surplus is the machine's contribution.
   - Worked: 27s advanced, yarn worth 30s: 20 + 4 for means of production carried over, 6 of new value against 3 paid. On the chapter's accounting every input was bought at its value.

5. **constant-capital-and-variable-capital** — Constant Capital and Variable Capital — *Chapter 8 · Constant Capital and Variable Capital*
   - Read: "That part of capital, then, which is represented by the means of production… does not, in the process of production, undergo any quantitative alteration of value."
   - Do: classify the parts of a capital as c or v and compute the value a machine transfers per day from its value and life.
   - Lab: `surplus`, view `transfer`. Money unit £; every preset is one 12-hour mill day with £6 of wages (6 h necessary) adding £12. Presets: `machine` (Marx's £1,000 machine, 1,000 days, with £10 of cotton: transferred £11, product £23), `sixfold` (replaces `raw`: Marx's sixfold rise in productivity, £60 of cotton spun in the same day: £61, £73, new value unchanged), `price-rise` (cotton bought at £10 worth £20 when spun: £21, £33). `suTransfer` is machine wear plus materials, so the raw material's whole passage shows in every preset. Pin `suTransfer`, `suProduct`.
   - Misconception: constant capital is fixed capital.
   - Worked: a £1,000 machine with a 1,000-day life passes £1 a day into the product, however much the product is.

6. **the-rate-of-surplus-value** — The Rate of Surplus Value — *Chapter 9 · The Rate of Surplus-Value*
   - Read: §1, s/v "is therefore an exact expression for the degree of exploitation of labour-power by capital".
   - Do: compute s/v from c, v and s, and the product's value in proportional parts of the product.
   - Lab: `surplus`, view `rate`. Money unit s, qty lb. Presets: `yarn` (Marx's §2: c 24s, v 3s, s 3s, 20 lb: 100%, 16/2/2 lb), `whole-capital` (the misreading: all 27s advanced entered as v: 1/9 = 11.11%), `six` (the six-hour day: c 12s, v 3s, s 0, 10 lb: 0%, 8/2/0 lb). Kit gap: the money unit is lab-wide, so Marx's £410/£90/£90 cannot share a lab with the 30s of yarn; it is computed in the body and the worked lines, and the status line prints s over the whole capital for every preset. Pin `suRate`, `suParts`.
   - Misconception: the rate of exploitation is s divided by all the capital.
   - Worked: s = 90 on v = 90 is 100%, "not 90/500"; the 20 lb of yarn splits as c 16 lb, v 2 lb, s 2 lb.

7. **seniors-last-hour** — Senior's "Last Hour" — *Chapter 9 · The Rate of Surplus-Value*
   - Read: §3, Senior's claim that "the whole net profit is derived from the last hour".
   - Do: compute the rate of surplus value on an 11½-hour day and after one hour is cut, and compare it with Senior's prediction that the profit vanishes.
   - Lab: `surplus`, view `senior`. Presets: `senior` (Marx's figures: an 11½-hour day, 5¾ hours necessary: 100%, an hour off 19/23), `thirteen` (replaces `ten-and-a-half`, whose rate `senior`'s `suLastHour` already shows: Senior's 13 hours, Marx's 126 2/23% = 29/23), `ten` (the 10-hour day, 1½ hours cut: 17/23 = 73.91%). The Kerr text prints the one-hour figure as "82 14/32%", a misprint for 82 14/23%, and introduces it as a cut "from 11½ to 10" while computing a one-hour cut; the lesson says both. Pin `suRate`, `suLastHour`.
   - Misconception: the last hour of the day produces the whole profit, so a shorter day abolishes it.
   - Worked: 5¾ surplus hours on 5¾ necessary is 100%; cut an hour and 4¾ on 5¾ is 19/23 = 82.61%, not zero.

8. **the-working-day-and-surplus-labour** — The Working Day: Its Limits and the Greed for Surplus Labour — *Chapter 10 · The Working Day* (the Kerr chapter title has no hyphen)
   - Read: §1, "Capital is dead labour, that, vampire-like, only lives by sucking living labour".
   - Do: compute s/v for a given day and necessary time, and the lengthening that doubles it.
   - Lab: `workday`, view `absolute`. Presets: `seven` (Marx's working day I: 7 hours, 6 necessary, 1/6), `six-six` (12-hour day, 6 necessary), `fifteen` (15-hour day), `eighteen` (18 hours). Pin `wdRate`, `wdSurplus`.
   - Misconception: the length of the day is fixed by nature or contract and is not a quantity capital can move.
   - Worked: 6 necessary hours of 12 is 100%; stretch the day to 15 and the same worker gives 150%.

9. **the-struggle-for-a-normal-working-day** — The Struggle for a Normal Working Day — *Chapter 10 · The Working Day*
   - Read: §5, "The establishment of a normal working day is the result of centuries of struggle between capitalist and labourer", and §7, "a protracted civil war, more or less dissembled, between the capitalist class and the working class" (both verbatim in the Kerr text).
   - Do: compute what a legal limit does to s/v at a fixed value of labour-power, and what the relay system does to the limit.
   - Lab: `workday`, view `limit`. Every preset: the employer's 12-hour day, 6 necessary. Presets: `before` (the 12-hour limit of 1844: 100%), `ten-hours` (the 1847 Act's ten hours, in force from May 1848: 2/3), `relay-dodge` (relays: the only checkable limit is the 15-hour factory day, so the 12 hours return: 100%), `act-1850` (added: the compromise of 5 August 1850, 10½ hours: 3/4). Pin `wdRate`, `wdSurplus`.
   - Misconception: a legal limit on hours leaves the rate of surplus value where it was.
   - Worked: cut a 12-hour day with 6 necessary to 10 and s/v falls from 100% to 2/3 = 66.67%.

10. **rate-and-mass-of-surplus-value** — Rate and Mass of Surplus Value — *Chapter 11 · Rate and Mass of Surplus-Value*
    - Read: the first law, "the mass of the surplus-value produced is equal to the amount of the variable capital advanced, multiplied by the rate of surplus-value".
    - Do: compute the mass of surplus value from s/v, the value of one labour-power and the number of workers, and the day a smaller workforce needs to yield the same mass.
    - Lab: `surplus`, view `mass`. Presets: `marx` split in two, `marx-hundred` (Marx's 100 workers at 3s on a 9-hour day, 50%: 150s) and `marx-fifty` (his 50 workers on a 12-hour day, 100%: 150s), `hundred` (100 workers at 3s, 100%: 300s), `limit` (50 workers at 200%: with 6 necessary hours that is an 18-hour day: 300s). Pin `suMass`, `suRate`.
    - Misconception: more workers always means more surplus value.
    - Worked: 100 workers at 3s and 100% give 300s; 50 workers must be worked at 200% to give the same, which needs an 18-hour day.

### Course 3 — Relative Surplus Value (`capital-relative-surplus-value`, 9)

1. **the-concept-of-relative-surplus-value** — The Concept of Relative Surplus Value — *Chapter 12*
   - Read: "The surplus value produced by prolongation of the working day, I call absolute surplus value. On the other hand, the surplus value arising from the curtailment of the necessary labour-time… I call relative surplus value."
   - Do: compute the new s/v when productivity in the wage-goods industries cuts necessary time, and the extra surplus value of a single innovating capitalist.
   - Lab: `workday`, view `relative`. Presets: `given` (Marx's 12-hour day, 10 necessary: `1/5 = 20%`, `0 h`), `cheaper` (necessary falls 10 to 9 hours: `1/3 = 33.33%`, `0 h`), `pioneer` (one capitalist doubles productivity and sells at the social value: `20%`, `+12 h`), `general` (the method has spread; labour-power falls from 5s to 3s, necessary 6 hours: `1 = 100%`, `0 h`). Pin `wdRate`, `wdExtra`. *Changed in authoring: `given` added as the base case. The kit's pioneer sells at the full social value; Marx's sale at 10d (below social, above individual value) is worked in prose.*
   - Misconception: a capitalist innovates in order to lower the value of labour-power.
   - Worked: Marx's 12 shillings of output a day becomes 24 articles for one innovator, who sells above individual value and pockets the difference until competition generalises it.

2. **co-operation** — Co-operation — *Chapter 13*
   - Read: "the special productive power of the combined working day is, under all circumstances, the social productive power of labour", and "this power costs capital nothing".
   - Do: compute the constant capital per unit when means of production are used in common, and the combined working day of many workers delivered at once.
   - Lab: `machine`, view `cooperate`, money `s`, qty `pieces`. Presets: `one` (one worker, 10s of tools and room, 12 pieces: `alone 10d, together 10d`, `12 h`), `masons` (Marx's 12 masons sharing 10s of tackle: `together 5/6 d`, `144 h`), `workshop` (a room for twelve at 60s: `together 5d`, `144 h`), `harvest` (Marx's hundred harvesters, 5s each alone against 100s shared: `alone 6d, together 1 1/5 d`, `1,200 h`). Pin `maCPerUnit`, `maCombinedDay`. *Changed in authoring: `one` added as the base case; the shilling figures are illustrative, the masons, 144 hours and hundred harvesters are Marx's. Kit gap: `cooperate` computes only the economy of shared means of production, not the extra output of combined labour, which is in prose.*
   - Misconception: co-operation's extra product is paid for in wages because each worker is paid fully.
   - Worked: a workshop worth 10s used by one worker costs 10s/12 per unit of a day's output of 12; used by 12 it costs 10s/144; no wage is paid for the difference.

3. **division-of-labour-and-manufacture** — Division of Labour and Manufacture — *Chapter 14*
   - Read: §3 on the "collective labourer" and the fixed proportions between detail workers.
   - Do: compute the number of detail workers each step needs for the steps' rates to match, and the smallest workshop that keeps every worker busy.
   - Lab: `machine`, view `detail`. Presets: `type` (Marx's type-founding figures: founders 2,000 an hour, breakers 4,000, rubbers 8,000: `founders 4, breakers 2, rubbers 1`, `7`), `pins` (three illustrative steps, drawing 3,000, cutting 2,000, pointing 1,200: `drawers 2, cutters 3, pointers 5`, `10`), `bottle` (the glass-house hole, five steps at one illustrative pace: 1 each, `5`), `better-mould` (founders cast 4,000: `2, 2, 1`, `5`). Pin `maWorkers`, `maMinimum`. *Changed in authoring: Smith gives no per-step rates, so `pins` uses illustrative rates and its label says so; the prose notes Smith's shop also had ten men (Kerr gives Smith's figure as 48,000 needles, l. 3452). `better-mould` added to show the ratio is a fact about technique.*
   - Misconception: the division of labour inside the workshop is the same thing as the division of labour in society.
   - Worked: if a caster makes 2,000 an hour, a breaker 4,000 and a polisher 8,000, the smallest balanced shop is four founders and two breakers to one rubber, as Marx says.

4. **machinery-and-the-value-it-transfers** — Machinery and the Value It Transfers — *Chapter 15 · Machinery and Modern Industry*
   - Read: §2, "machinery, like every other component of constant capital, creates no new value, but yields up its own value to the product".
   - Do: compute the value a machine adds per unit, and apply both tests for adopting it: the capitalist's (machine cost against the wages it displaces) and society's (against the labour it saves).
   - Lab: `machine`, view `adopt`, money £, qty `yards`, shipped `test = capitalist`. Presets: `marx` (Marx's £3,000 machine against £3,000 of wages and £6,000 of labour, illustrative life of 10,000 yards: `£3/10`, not adopted), `society` (a £5,000 machine saving the same £6,000 of labour: `£1/2`, not adopted on the capitalist's test), `cheap-labour` (wages £2,000: not adopted), `dear-labour` (wages £4,500: adopted). Pin `maPerUnit`, `maVerdict`. *Changed in authoring: `society` instantiated as a £5,000 machine; `dear-labour` added. The kit's test is strict, so Marx's machine costing exactly the wages it displaces is "not adopted", which the prose explains (it saves the capitalist nothing).*
   - Misconception: a machine is used whenever it saves labour.
   - Worked: a machine that saves more labour than it embodies is still not bought if it costs more than the wages it displaces; the capitalist pays for labour-power, not labour.

5. **machinery-and-the-worker** — Machinery and the Intensity of Labour — *Chapter 15 · Machinery and Modern Industry*
   - Read: §3(c), the intensification of labour once the working day is shortened by law.
   - Do: compute how intensification raises s/v and the labour spent without lengthening the day.
   - Lab: `workday`, view `intensity`, necessary 8 hours (Marx's figures, Kerr l. 3104). Presets: `twelve` (12 hours at normal intensity: `12 h`, `4 h`, 50%), `ten-only` (10 hours, no change in intensity: `10 h`, `2 h`, `1/4 = 25%`), `ten-denser` (10 hours at 6/5: `12 h`, `4 h`, 50%), `twelve-denser` (12 hours at 4/3: `16 h`, `8 h`, `1 = 100%`). Pin `wdLabour`, `wdSurplus`, `wdRate`. *Changed in authoring: `same-day`, `intense` and `shorter-but-denser` renamed and set to Marx's own 12-hour, 8-necessary day; `ten-only` added for the manufacturers' case. Kit gap: the kit allows intensity on any day and holds the value of labour-power fixed, which the `note` states.*
   - Misconception: a shorter working day always means less surplus value.
   - Worked: cut the day from 12 to 10 hours but raise intensity by 1/5 and the worker spends as much labour as before.
   - The family's labour-power spread over several earners (§3a) is stated in prose; it is a wages fact and is not computed here.

6. **machinery-and-the-displaced-worker** — Machinery and the Displaced Worker — *Chapter 15 · Machinery and Modern Industry*
   - Read: §6, "The theory of compensation as regards the workpeople displaced by machinery".
   - Do: compute the capital "set free" by a machine and the workers that capital can re-employ, and show why compensation is not automatic.
   - Lab: `machine`, view `displace`, money £. Presets: `marx` (Marx's carpet factory, 100 workers at £30, £1,500 into machinery, machine-building materials four times wages (illustrative): `50`, `10 = 0 set free + 10 in machine-building`), `cheaper-machine` (Marx's £1,000 variant: `70/3 = 50/3 set free + 20/3 in machine-building`), `compensation` (the most favourable case, all £1,500 paid as machine-builders' wages, composition 0: `50 = 0 set free + 50 in machine-building`). Pin `maDisplaced`, `maReemployed`. *Changed in authoring: `machine-builders` merged into `marx`; `cheaper-machine` added; `compensation` is the most favourable case rather than "£1,500 set free", since the kit computes what is set free. Kit gap: the kit omits the machine-builders' surplus value, so its re-employed figure is an upper bound, as the `note` says.*
   - Misconception: the capital freed by a machine re-employs the workers it displaced. State the compensation theorists (James Mill, McCulloch, Torrens, Senior, J. S. Mill) at strength first: cheaper products release purchasing power that creates employment elsewhere. Marx's carpet factory answers the narrower "capital set free" version, and the lesson says so.
   - Worked: 100 workers at £30 is £3,000 of variable capital; after the change £1,500 pays 50 and £1,500 sits in machinery: nothing was set free, a fund for wages became constant capital.

7. **absolute-and-relative-surplus-value** — Absolute and Relative Surplus Value — *Chapter 16*
   - Read: "From one standpoint, any distinction between absolute and relative surplus-value appears illusory."
   - Do: classify a change in s/v as absolute or relative and say when the distinction matters.
   - Lab: `workday`, view `classify`, from a 12-hour day of 6 necessary. Presets: `lengthen` (to 14: absolute, `4/3 = 133.33%`), `cheapen` (necessary to 5: relative, `7/5 = 140%`), `both` (14 and 5: both, `9/5 = 180%`), `sago` (Marx's sago-cutter, 2 necessary hours, the day from 2 to 12: absolute, `5 = 500%`). Pin `wdKind`, `wdRate`. *Changed in authoring: `sago` added for the chapter's natural-conditions passage.*
   - Misconception: surplus value needs a natural surplus of the soil.
   - Worked: from 12/6 to 14/5: 2 more hours are absolute, 1 fewer necessary hour is relative; s/v goes from 100% to 180%.

8. **price-of-labour-power-and-surplus-value** — Changes in the Price of Labour-Power and in Surplus Value — *Chapter 17 · Changes of Magnitude in the Price of Labour-Power and in Surplus-Value*
   - Read: the three determinants, "the length of the working day… the normal intensity of labour… the productiveness of labour".
   - Do: run Marx's cases — one factor varying, the others constant — and predict the direction of s/v and of the price of labour-power.
   - Lab: `workday`, view `three`, shipped `hold = combined`. Presets (Marx's figures, at 6d an hour): `productivity` (12 hours, 8 necessary, productivity 4/3: `6 h`, 100%), `intensity` (12 hours, 6 necessary, intensity 4/3: `6 h`, `5/3 = 166.67%`), `length` (to 14: `6 h`, `4/3 = 133.33%`), `combined` (productivity 3/4, day 16: `8 h`, 100%), `dearer-food` (productivity 3/4, day 12: `8 h`, `1/2 = 50%`). Pin `wdLpValue`, `wdRate`. *Changed in authoring: `hold` is a redraw-only select a preset cannot set, so it ships as `combined` and each preset shows its own case; `dearer-food` added.*
   - Misconception: higher productivity raises the value of what the worker produces each day.
   - Worked: double productivity with the day fixed at 12 and the value produced is still 12 hours; only its split between v and s can move.

9. **formulae-for-the-rate-of-surplus-value** — Formulae for the Rate of Surplus Value — *Chapter 18 · Various Formulae for the Rate of Surplus-Value*
   - Read: the "derivative formulae", surplus labour over the whole working day.
   - Do: compute s/v and s/(v + s) for the same day and show why the second can never reach 100%.
   - Lab: `surplus`, view `formulae`, 12-hour day. Presets: `half` (6/6: `1 = 100%`, `1/2 = 50%`), `two-thirds` (4/8: 200%, `2/3 = 66.67%`), `lavergne` (Lavergne's quarter, 3/9: 300%, `3/4 = 75%`), `extreme` (1/11: `11 = 1,100%`, `11/12 = 91.67%`). Pin `suRate`, `suFalse`. *Changed in authoring: `lavergne` added. The chapter's formula displays are missing from the plain text; the lesson quotes only the prose around them.*
   - Misconception: s/(v + s) measures exploitation.
   - Worked: 8 surplus hours in 12 is 200% by s/v and 2/3 by the "derivative" formula.

### Course 4 — Wages and Accumulation (`capital-wages-and-accumulation`, 9)

1. **value-of-labour-power-into-wages** — The Value of Labour-Power Becomes Wages — *Chapter 19 · The Transformation of the Value (and Respectively the Price) of Labour-Power into Wages*
   - Read: "On the surface of bourgeois society the wage of the labourer appears as the price of labour, a certain quantity of money that is paid for a certain quantity of labour."
   - Do: compute the "value of labour" that the wage form appears to pay and show it is the value of labour-power divided by the hours, not the value the hours create.
   - Lab: `wages`, view `form`, `money_unit` s. Presets: `marx` (3s for 12 hours, an hour creates 6d: `3d`, `6s in 12 h (6d an hour)`), `equivalents` (6s paid for the 12 hours: `6d`, the same value created), `dearer` (labour-power worth 4s: `4d`), `cheaper` (2s: `2d`). Pin `waHourPrice`, `waValueCreated`. *Changed in authoring: `value-created` and `irrational` became `equivalents`, `dearer` and `cheaper`. The value created is a tile in every preset, and "the value of labour" as 3s/12 hours is the `marx` preset itself, so neither was a separate instance. `equivalents` shows what the wage form claims, the hour paid at the value it creates and no surplus value; `dearer` and `cheaper` show the apparent price of an hour moving with the value of labour-power while the 6s created does not.*
   - Misconception: the wage is the price of the work done.
   - Worked: 3s for a 12-hour day looks like 3d an hour paid for 3d of value; each hour creates 6d.

2. **time-wages** — Time-Wages — *Chapter 20 · Time-Wages*
   - Read: "If, e.g., the habitual working-day is 10 hours and the daily value of the labour-power 3s., the price of the working hour is 3 3/5d. It falls to 3d. as soon as the working-day rises to 12 hours, to 2 2/5 d. as soon as it rises to 15 hours."
   - Do: compute the hourly price from the daily value of labour-power and the normal day, and the effect of overtime and short time.
   - Lab: `wages`, view `time`, `money_unit` s. Presets, all with Marx's figures: `normal` (3s, normal day 12 h, 12 worked: `3d`, `3s`), `ten-hour` (normal day 10 h: `3 3/5 d`, `3s`), `overtime` (normal day 10 h, 12 worked at the same price: `3 3/5 d`, `3s 7 1/5 d`), `short-time` (normal day 12 h, 6 worked: `3d`, `1s 6d`). Pin `waHourPrice`, `waDaily`. *Changed in authoring: `ten-hour` added so that the lab gives Marx's 3 3/5d beside the 3d of `normal`; overtime is worked from the 10-hour normal day so its figure is Marx's. The lab has no separate overtime rate, so overtime at a higher rate is in prose only.*
   - Misconception: a higher hourly rate means a better-paid worker.
   - Worked: 3s for a 12-hour normal day is 3d an hour; work 6 hours at 3d and the worker gets 1s 6d, below the value of labour-power. *As shipped, the worked lines run Marx's 10, 12 and 15-hour days (3 3/5d, 3d, 2 2/5d) and the 10-hour price paid for 12 hours (3s 7 1/5d); short time is in the `short-time` preset and the mistakes.*

3. **piece-wages** — Piece-Wages — *Chapter 21 · Piece-Wages*
   - Read: "Wages by the piece are nothing else than a converted form of wages by time, just as wages by time are a converted form of the value or price of labour-power."
   - Do: compute the piece-rate from the hourly price and the normal output, and the hidden speed-up when the rate is cut after output rises.
   - Lab: `wages`, view `piece`, `money_unit` s, `qty_unit` pieces. Presets: `marx` (Marx's figures: 24 pieces in 12 hours, 3s a day: `1½d`, `3s`), `faster` (Marx's figures: 48 pieces at the old rate: `1½d`, `6s`), `cut` (48 pieces become the normal output: `¾d`, `3s`), `speed-up` (illustrative: 30 pieces, the rate cut to 1 1/5d: `1 1/5 d`, `3s`). Pin `waPieceRate`, `waDaily`. *Changed in authoring: `cut` sets the normal output to 48 rather than cutting the rate by hand, because that is how Marx says the rate falls (the rate follows the normal output); `speed-up` added to show `rate_cut_to`, the cut that leaves the day's wage where it was while effort rises.*
   - Misconception: piece-wages pay for the worker's actual effort.
   - Worked: 3s for 24 pieces is 1½d a piece; at 48 pieces the rate is cut to ¾d and the day pays 3s again.

4. **national-differences-of-wages** — National Differences of Wages — *Chapter 22 · National Differences of Wages*
   - Read: "The average intensity of labour changes from country to country; here it is greater, there less. … The more intense national labour, therefore, as compared with the less intense, produces in the same time more value, which expresses itself in more money."
   - Do: compute two countries' wages per unit of output (the relative wage) and their rates of surplus value from money wages, intensity and productivity.
   - Lab: `wages`, view `national`, `money_unit` s, `qty_unit` lb. Instance (illustrative): England pays 6d an hour, the Continent 4d; a pound of yarn is worth 8d. Presets: `england-continent` (England makes 2 lb an hour, the Continent 1: `3/4`, `England 5/3 = 166.67%, Continent 1 = 100%`), `same-intensity` (1 lb an hour each: `3/2`, `England 1/3 = 33.33%, Continent 1 = 100%`), `cheaper-goods` (as `england-continent`, the pound's value falls to 6d: `3/4`, `England 1 = 100%, Continent 1/2 = 50%`). Pin `waRelative`, `waRate`. *Changed in authoring: the plan named the presets only; the instance values above are the author's.*
   - Misconception: a country with higher money wages has a lower rate of surplus value.
   - Worked: wages 1½ times as high for twice the output make the relative wage 3/4 of the other country's, and the rate of surplus value higher.

5. **simple-reproduction** — Simple Reproduction — *Chapter 23 · Simple Reproduction*
   - Read: "After the lapse of a certain number of years the capital value he then possesses is equal to the sum total of the surplus-value appropriated by him during those years, and the total value he has consumed is equal to that of his original capital." (Verified against the Kerr text, l. 4256, with the sentence before it.)
   - Do: compute how many years of consumed surplus value equal the capital advanced, and say what that means for "the capitalist's own" capital.
   - Lab: `accumulate`, view `simple`. Presets: `marx` (Marx's figures: £1,000 capital, £200 surplus a year consumed: `5 years`), `faster` (£250 a year: `4 years`), `slower` (Marx's figures: half consumed, £100: `10 years`). Pin `acYears`.
   - Misconception: the capital remains the capitalist's original property however long it runs.
   - Worked: £1,000 advanced and £200 a year consumed: after 5 years the capitalist has consumed the original sum, and on Marx's reckoning what remains is capitalised surplus value. The `note` says this is a way of reckoning and gives the standard objection its sentence: one could as well say the capitalist consumed only the surplus.

6. **surplus-value-into-capital** — Surplus Value into Capital — *Chapter 24 · Conversion of Surplus-Value into Capital*
   - Read: "Accumulate, accumulate! That is Moses and the prophets!"
   - Do: run accumulation period by period with a share of s added to capital, and compute original capital as a share of the present capital.
   - Lab: `accumulate`, view `expand`. Presets: `marx` (Marx's figures: £10,000 at 4:1 c to v, 100%, all of s capitalised as £1,600c and £400v: `£124,416/5`, `3,125/7,776 = 40.19%`), `half` (illustrative: half of s accumulated: `£161,051/10`, `100,000/161,051 = 62.09%`), `consume-all` (none: simple reproduction: `£10,000`, `1 = 100%`). Shipped `periods = 5`. Pin `acCapital`, `acShareOriginal`. *Changed in authoring: `abstinence` renamed `consume-all`. A preset named for the doctrine the lesson disputes would read as the lab endorsing it, and the preset is the opposite case: the capitalist abstains from nothing.*
   - Misconception: accumulation is the capitalist's "abstinence" from consumption.
   - Worked: after one year at Marx's figures the capital is £12,000, of which £2,000, a sixth, is capitalised surplus value; the lab carries it on for five years.

7. **accumulation-with-constant-composition** — Accumulation with Constant Composition — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §1, "Accumulation of capital is, therefore, increase of the proletariat." (Shipped with the sentence that opens the paragraph, "As simple reproduction constantly reproduces the capital-relation itself…", and an ellipsis.)
   - Do: compute the demand for labour as accumulation proceeds at constant c/v, and when it outruns the labour supply and wages rise.
   - Lab: `accumulate`, view `labour`. Instance (illustrative): £5,120 at c/v 1, s/v 100%, half of s capitalised, a wage of £10, 300 workers at first. Presets: `steady` (supply +100 a period: `625`, `75`, `£15,625`), `tight` (supply +40; demand overtakes it in period 3: `460`, `0`, `£26,525/2`), `wage-rise` (supply fixed at 300; the wage rises every period: `300`, `0`, `£81,825/8`). Shipped `periods = 5`. Pin `acDemand`, `acReserve`, `acCapital`. *Changed in authoring: `acCapital` pinned as well, so that the slower growth the misconception turns on is a pinned figure; instance values are the author's, chosen so `steady` grows by exactly a quarter a period.*
   - Misconception: rising wages show that accumulation benefits the worker without limit.
   - Worked: v grows by half of s each year; when it exceeds the workers available the reserve is empty and wages rise until accumulation slows.

8. **the-reserve-army** — The Reserve Army of Labour — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §3, "a relatively redundant population of labourers, i.e., a population of greater extent than suffices for the average needs of the self-expansion of capital". *Changed in authoring: the plan's phrase "the progressive production of a relative surplus population or industrial reserve army" is the section's title, not a sentence in the Kerr text; the lesson quotes the sentence that opens "But in fact, it is capitalistic accumulation itself that constantly produces…".*
   - Do: compute employment when capital grows while c/v rises, and the surplus population that results. The prose covers §2, concentration and centralisation as the source of the rising composition.
   - Lab: `accumulate`, view `composition`. Instance: £6,000 at c/v 1, all of s capitalised, a wage of £10, 300 workers at first. Presets: `rising` (Marx's ratios: c/v 1:1 rising by 1 a period to 5:1, s/v 100%, supply +30: `300`, `120`), `fast-growth` (the same rise at s/v 200%, supply +100: `700`, `0`), `constant` (no rise, supply +30: `420`, `0`). Shipped `periods = 5`. Pin `acDemand`, `acReserve`. *Changed in authoring: `rising` runs Marx's own ratios 1:1, 2:1, 3:1, 4:1, 5:1 from his £6,000 (§2) instead of 4 to 6. That matches the worked line's starting ratio of 1, and at s/v 100% with everything capitalised it gives the starkest form of the chapter's claim: v stays at £3,000 and employment at 300 while capital triples.*
   - Misconception: accumulation always increases employment.
   - Worked: capital doubles while c/v goes from 1 to 3; v falls from half to a quarter of capital and employment stays flat. *As shipped, the worked lines carry on to period 5: capital triples, from £6,000 to £18,000, while c/v goes from 1 to 5 and v stays £3,000. The prose sets Marx's own §2 sum (£18,000 at 4:1, v £3,600) beside it.*

9. **the-general-law-of-accumulation** — The General Law of Capitalist Accumulation — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §4, "Accumulation of wealth at one pole is, therefore, at the same time accumulation of misery… at the opposite pole".
   - Do: compute the ratio of reserve to active workers period by period while wages per worker rise.
   - Lab: `accumulate`, view `law`. Instance: £6,000 at c/v 1, a wage of £10, 300 workers at first. Presets: `boom` (s/v 200%, c/v +1 a period, wage +£½ a period, supply +50: `1/19 = 5.26%`, `25`, `475`), `slump` (£4,200, nothing capitalised, c/v +½, supply +30: `3 = 300%`, `315`, `105`), `long-run` (Marx's ratios, c/v +1, supply +30: `2/5 = 40%`, `120`, `300`). Shipped `periods = 5`. Pin `acRatio`, `acReserve`, `acDemand`. The floating, latent and stagnant forms and pauperism, "the lowest sediment", are named in prose and asked in the quiz. *Changed in authoring: `long-run` runs five periods, not ten. `periods` is a lesson setting the kit does not let a preset override, and the other two presets read best at five; the lesson says that the periods slider set to 10 gives a ratio of 9/10. `acDemand` pinned as well.* *Changed in second review: `slump` starts from £4,200 instead of £6,000. At £6,000 with c/v rising by ½ its period-4 variable capital was £6,000/3.5 and employment a fractional 171 3/7; at £4,200 every period employs a whole number (210, 168, 140, 120, 105). `boom` is unchanged: it shows the reserve only in period 5, but a bounded search (capitals £3,000 to £30,000, s/v 100% to 300%, c/v rising by ½ or 1, wage steps of 1s to £10, a range of supplies) of instances with a rising composition and a wage rising by a fixed step found none that keeps every period's employment a whole number and the ratio rising over several periods, so the lesson says plainly that the reserve forms only in the last period.*
   - Misconception: the law predicts that real wages must always fall.
   - Worked: in `boom` the ratio of reserve to employed rises while wages per worker rise. Marx adds that the labourer's lot "must grow worse" be his payment high or low; whether that means relative or absolute worsening is argued, and the lab computes only the ratio.

### Course 5 — So-Called Primitive Accumulation (`capital-primitive-accumulation`, 8)

1. **the-secret-of-primitive-accumulation** — The Secret of Primitive Accumulation — *Chapter 26*
   - Read: "This primitive accumulation plays in Political Economy about the same part as original sin in theology", and the "diligent, intelligent, and, above all, frugal elite".
   - Do: compute how long a frugal worker would save to assemble a capital of a stated size, and compare it with the simple-reproduction result that any capital is consumed in a computable number of years.
   - Lab: `accumulate`, view `thrift`. Presets: `carpet` (a worker on 3s a day saving a tenth, against the £3,000 wage bill of the carpet factory in “Machinery and the Displaced Worker”), `mill` (the same saving against £600: 40,000 days), `whole-wage` (the whole 3s saved, against £3,000: 20,000 days). Pin `acDaysToTarget`. Wage and target in shillings (£3,000 = 60,000s). As authored: `regress` is replaced by `whole-wage` because the `thrift` view cannot show simple reproduction (that is the `simple` view, and a lab has one view); the comparison with Chapter 23's £1,000 consumed at £200 a year in 5 years is made in prose and the quiz.
   - Misconception: the first capitals were saved out of wages (the legend in its plain form, which the tile refutes). The stronger form, that capital grew by thrift and reinvested profit (Weber, Crouzet), is a historical position: named, stated at strength, and left open, as §C's rule on misconceptions requires.
   - Worked: saving 3.6d a day, £3,000 takes 200,000 working days; and a capital assembled that way would still need workers who own nothing.
   - Numbering: the English edition (followed here, and by Penguin) differs from the German from Chapter 4 on; German Chapter 4 contains English Chapters 4–6, so English Chapter n is German n − 2 for Chapters 7–25, and English Chapters 26–33 are German Chapters 24 and 25, inside German Part Seven. Said once in From Money to Surplus Value's `how_to` and once here.

2. **expropriation-from-the-land** — Expropriation of the Agricultural Population — *Chapter 27*
   - Read: from Chapter 27 itself — the clearing of the estates (the Sutherland clearances).
   - Do: compute the smallholder's working day before expropriation (all labour for the household) and the same person's day as a wage-worker, and the surplus that separation makes available to an employer, for one person and for a cleared estate.
   - Lab: `workday`, view `separate`. Presets: `smallholder` (12 hours, all for the household), `labourer` (12 hours, 6 necessary), `clearing` (Marx's 3,000 Sutherland families, one wage-worker each, 12 hours with 6 necessary: 18,000 h). Pin `wdSurplus`, `wdRate`.
   - Misconception: enclosure was only a change in farming technique, with no effect on who had to work for wages.
   - Worked: the same 12-hour day yields 0 hours of surplus to anyone else on one's own land and 6 to an employer after the clearing. Whether enclosure also raised yields is a separate, debated question that Marx says he sets aside ("We leave on one side here the purely economic causes of the agricultural revolution").

3. **bloody-legislation** — Bloody Legislation and the Forcing Down of Wages — *Chapter 28*
   - Read: the Statute of Labourers of 1349 (Kerr l. 5386; the phrase "laws for the compulsion of labour" is not in the Kerr text, which has "laws for keeping them down").
   - Do: compute the gap between a statutory maximum wage and the value of labour-power, and the rate of surplus value the law enforces.
   - Lab: `wages`, view `statute`. Presets: `statute` (illustrative statutory maximum below value), `market` (wage at value), `combination` (masons combine for 4s, 1s above a 3s value, which the statutes forbade: 50%). Instances as authored: 12-hour day, 6 necessary, value of labour-power 3s; `statute` 2s (200%), `market` 3s (100%). Pin `waGap`, `waRate`. The lesson says the figures are illustrative.
   - Misconception: a wage law protects the worker by setting a floor.
   - Worked: a legal maximum one-third below the value of labour-power turns a 100% rate into one of 200%.

4. **the-capitalist-farmer** — Genesis of the Capitalist Farmer — *Chapter 29*
   - Read: "The progressive fall in the value of the precious metals, and therefore of money, brought the farmers golden fruit." (Kerr wording checked: identical, l. 5408.)
   - Do: compute a money rent fixed by long lease while prices rise, its real value, and the farmer's gain when wages lag.
   - Lab: `money`, view `fixed-rent`. Presets: `price-revolution` (prices double over the lease), `stable`, `wages-lag` (prices double, money wages rise by half). Instances as authored: rent £20, product £100 and wages £40 at old prices; stable keeps £40, price-revolution £100 (£50 real), wages-lag £120 (£60 real: £10 from the landlord, £10 from the labourers). Pin `moRealRent`, `moFarmerGain`.
   - Misconception: when all prices double, every party is where it was.
   - Worked: a £20 rent fixed while prices double now costs the farmer half as much in corn.

5. **the-home-market** — The Home Market for Industrial Capital — *Chapter 30*
   - Read: "The expropriation and expulsion of the agricultural population… set free… their former means of nourishment".
   - Do: compute the market created when households that produced their own subsistence must buy it, and the variable capital that now circulates.
   - Lab: `circuit`, view `market`. Presets: `before` (100 households, self-supplied), `after` (the same households as wage-earners), `cottage` (wage-earners who still grow their food). Instances as authored, in shillings: subsistence 1s 6d a day (food 1s a day, cloth 3s and fuel 3s every 12 days); markets 0s, 150s, 50s. `half` is replaced by `cottage`, which ties to the four-acre cottage laws of Chapter 27. Pin `ciMarket`, `ciLpValue` (the market created equals the wage bill that now circulates: one number from two sides).
   - Misconception: the home market grew because people became richer.
   - Worked: 100 households that spun their own yarn now buy it: the same use-values, newly commodities, a market where none was.

6. **the-industrial-capitalist** — Genesis of the Industrial Capitalist — *Chapter 31*
   - Read: "Force is the midwife of every old society pregnant with a new one", with Marx's list of levers: the colonies, the national debt, the modern mode of taxation and the protectionist system.
   - Do: name the four levers and compute one of them: the capitalised value of a state debt from its annual interest and the tax that services it.
   - Lab: `interest`, view `capitalise`. Presets: `consols` (£3 a year at 3%), `cheap-money` (rate falls to 2%), `bank-1694` (Marx's rate: the Bank of England lends to the state at 8%, £8 a year on £100). Pin `inPrice`. As authored: `tax` is replaced by `bank-1694` because the `capitalise` view has no tax field; taxation is in prose.
   - Misconception (Marx's own target): the national debt is part of the nation's wealth. His sarcasm: the only part of the so-called national wealth that enters the collective possession of modern peoples is their national debt.
   - Worked: £3 a year at 3% is a £100 claim; nothing was built, but £100 is now capital in its owner's books.
   - The `note` defines "capitalise" locally (a yearly £3 is called a £100 claim because £100 at 3% pays £3; why that rate exists is Volume III's question), since interest is not taught until Merchant's Capital and Interest.
   - The prose gives the colonial system and the slave trade their place; the chapter is not only about consols.

7. **the-historical-tendency** — Historical Tendency of Capitalist Accumulation — *Chapter 32*
   - Read: "The knell of capitalist private property sounds. The expropriators are expropriated."
   - Do: compute concentration (every capital growing) and centralisation (capitals merging) for a set of capitals over several periods, and the share held by the largest.
   - Lab: `accumulate`, view `centralise`. Presets: `ten` (ten equal capitals), `merge` (the largest absorbs the smallest each period), `grow` (all grow at the same rate, no merger). Instances as authored: ten capitals of £100, five periods; `ten` no growth and no merging (1/10, 10), `grow` at 1/10 a period (1/10, 10), `merge` (3/5, 5). Pin `acTopShare`, `acCount`.
   - Misconception: concentration and centralisation are the same thing.
   - Worked: ten equal capitals where the largest absorbs the smallest each period leave one holding 6/10 after five periods; if all simply grow, the largest still holds 1/10.

8. **the-modern-theory-of-colonisation** — The Modern Theory of Colonisation — *Chapter 33*
   - Read: Mr. Peel who took £50,000 and 3,000 workers to the Swan River, and was "left without a servant to make his bed".
   - Do: compute the labour supply left to a colonial capitalist when workers can take free land, and Wakefield's land price that restores it.
   - Lab: `accumulate`, view `colony`. Presets: `peel` (Marx's figures as printed in the Kerr text: £50,000 and 3,000 workers, free land; the 1887 Moore–Aveling printing reads 300, and the `note` says so), `wakefield` (land at two years' wages, half the wage saved: 4 years), `closed` (land at two years' wages, nothing saved: never). Shipped `periods` = 4, so `wakefield` shows 3,000 for hire; a preset cannot set `periods`. Pin `acReserve`, `acYearsToLand`.
   - Misconception: capital is a thing — money and machines — that can be exported.
   - Worked: with free land every worker leaves; at a price of 4 years' savings the labour market is restored for 4 years per worker.

### Course 6 — The Circuits of Capital (`capital-circuits-of-capital`, 6)

Volume II's Part One. Prose cites Volume II chapters as "Volume II, Chapter n". Module names use
the Kerr chapter titles (Untermann's "circulation" and "rotation" for *Kreislauf*): Chapter 1 · The
Circulation of Money-Capital, Chapter 2 · The Rotation of Productive Capital, Chapter 3 · The
Circulation of Commodity-Capital, Chapter 4 · The Three Diagrams of the Process of Circulation,
Chapter 5 · The Time of Circulation, Chapter 6 · The Expenses of Circulation. Lesson titles keep
"circuit", and lesson 1 says once why.

1. **the-circuit-of-money-capital** — The Circuit of Money Capital — *Chapter 1*
   - Read: the formula M–C…P…C′–M′ (Kerr l. 353) and the passage calling the circuit of money-capital "the most one-sided, and thus the most convincing and typical form" (Kerr l. 615; Kerr has "convincing", not "striking").
   - Do: trace a capital through its three stages, give the value in each form, and compute s from M and M′.
   - Lab: `circuit`, view `stages`. Presets (all Marx's figures, Kerr l. 472, 492): `marx` (£422 = £372 + £50, product £500, all 10,000 lb sold: `ciMprime` £500, `ciS` £78), `partly` (8,440 lb sold, `sold_share` 211/250: £422, £0), `constant` (7,440 lb sold, 93/125: £372, −£50), `unsold` (0: £0, −£422). The text replaced the earlier "half sold" instance: Marx gives the two partial sales himself. Pin `ciMprime`, `ciS`.
   - Misconception: the money at the end is where the surplus is made.
   - Worked: £422 becomes yarn worth £500 inside P; selling it only changes £500's form.

2. **the-circuit-of-productive-capital** — The Circuit of Productive Capital — *Chapter 2*
   - Read: "The rotation of productive capital has the general formula P...C'-M'-C...P" (Kerr l. 652); second passage, the minimum sum for m (Kerr l. 809).
   - Do: run the productive circuit under simple reproduction and under accumulation, compute the capital that re-enters P, and the money held back until it is large enough to invest.
   - Lab: `accumulate`, view `expand`, shipped `periods = 1`; capital 422, `c_v` 186/25, `s_rate` 39/25. Presets: `simple` (share 0: `acCapital` £422, `acHoard` £0), `accumulate` (Marx's figure, Kerr l. 693: £58 of the £78, share 29/39: £480, £0), `hoard` (share 1, `invest_threshold` £200, illustrative: £422, £78; at 3 periods £656). The text replaced the earlier "half of s" instance. Pin `acCapital`, `acHoard`.
   - Misconception: the productive circuit is the money circuit started at a different point.
   - Worked: with £78 of s, simple reproduction restarts P at £422; capitalising £58 of it, Marx's figure, restarts it at £480.

3. **the-circuit-of-commodity-capital** — The Circuit of Commodity Capital — *Chapter 3*
   - Read: "C'—M'—C...P...C'" and C'' (Kerr l. 847–853); the aggregate capital (Kerr l. 995).
   - Do: split C′ into the parts that return as means of production, as wages and as capitalists' consumption.
   - Lab: `surplus`, view `parts`, `money_unit` £, `qty_unit` lb. Presets (all Marx's figures, Kerr l. 883–889): `marx` (c 372, v 50, s 78, 10,000 lb: `c: 7,440 lb, v: 1,000 lb, s: 1,560 lb`), `lot-1` (7,440 lb worth £372: c 34596/125, v 186/5, s 7254/125), `lot-2` (1,000 lb worth £50: c 186/5, v 5, s 39/5), `lot-3` (1,560 lb worth £78: c 7254/125, v 39/5, s 1521/125). These replace `consumed` and `accumulated`, which the `parts` view cannot distinguish; the three lots add back to the whole and correct the slips in the Kerr tables (1,160.740, 343.360, 7,450). Pin `suParts`, `suProduct`.
   - Misconception: the commodity product is all revenue to be consumed (Adam Smith's resolution of price into revenues, stated at strength).
   - Worked: of £500 of yarn, £372 must buy back means of production; only £128 is anyone's income.

4. **the-three-formulas-of-the-circuit** — The Three Formulas of the Circuit — *Chapter 4*
   - Read: Kerr l. 1049: "The actual rotation of industrial capital in its continuity is therefore not alone the unity of the processes of production and circulation, but also the unity of its three cycles."
   - Do: compute how a capital divides at any moment among money, productive and commodity forms when each stage takes a stated time.
   - Lab: `turnover`, view `phases`. Presets: `even` (4, 4, 4 weeks: each `1/3 = 33.33%`), `slow-sale` (4, 4, 8: `1/4 = 25%`, `1/4 = 25%`, `1/2 = 50%`), `fast` (2, 6, 2: `1/5 = 20%`, `3/5 = 60%`, `1/5 = 20%`). Pin `tuMoney`, `tuProductive`, `tuCommodity`.
   - Misconception: a capital is in one form at a time.
   - Worked: with 4 weeks in each stage, a continuous business always has a third of its capital in each form.

5. **the-time-of-circulation** — The Time of Circulation — *Chapter 5*
   - Read: Kerr l. 1233: "The time of circulation and time of production mutually exclude one another." (checked: Kerr has "one another", not "each other").
   - Do: compute turnover time as production time plus circulation time, and the share of the turnover spent in circulation.
   - Lab: `turnover`, view `time`, no `capital` (so `tuAggregate` prints —). Presets (illustrative; the chapter gives no figures): `spinning` (6 + 2 weeks: `8 weeks`, `1/4 = 25%`), `slow-sale` (6 + 6: `12 weeks`, `1/2 = 50%`), `distant-market` (6 + 20: `26 weeks`, `10/13 = 76.92%`). Pin `tuTurnover`, `tuCirculationShare`.
   - Misconception: a capital is producing value for as long as it is tied up.
   - Worked: 6 weeks of production and 6 of circulation is a 12-week turnover, half of it in circulation.
   - Working time against production time (wine, timber) is left to “The Time of Production”.

6. **the-costs-of-circulation** — The Costs of Circulation — *Chapter 6*
   - Read: the general law (Kerr l. 1398, §3) and transport adding value (Kerr l. 1406); §1 and §2 in the body. Kerr's term for the pure costs is "dead expenses"; "faux frais" does not occur in the Kerr text.
   - Do: classify circulation costs as pure costs (deductions from surplus value) or as costs that add value (transport, necessary storage), and compute the deduction.
   - Lab: `circuit`, view `costs`, M 400, product 500 (illustrative). Presets: `clerks` (pure £10: `ciSNet` £90), `transport` (value-adding £10: £100), `stockpile` (£5 necessary storage, £5 for goods that would not sell: £95). Pin `ciS`, `ciSNet`.
   - Misconception: everything a business must pay for adds to the value of its product.
   - Worked: a bookkeeper paid £10 leaves £90 of s; a carter paid £10 adds £10 to the value delivered.

### Course 7 — The Turnover of Capital (`capital-turnover-of-capital`, 11)

1. **turnover-time-and-number-of-turnovers** — Turnover Time and the Number of Turnovers — *Chapter 7*
   - Read: the passage making the year the natural unit for measuring turnovers (l. 1453), and the turnover time as the time the capitalist must advance his capital (l. 1459). *Corrected in authoring: Kerr's notation is T for the year, t for the turnover time and n = T/t, not U/u.*
   - Do: compute n = T/t for given turnover times, and the value turned over on a capital advanced.
   - Lab: `turnover`, view `time`. Presets: `three-months` (13 weeks, 9 of production and 4 of circulation, £400), `five-weeks` (4 + 1, £500), `eighteen-months` (78 weeks, £600). Shipped `year_weeks = 52`. Pin `tuTurnover`, `tuTurnovers`, `tuAggregate`. *Changed in authoring: `two-years` became `eighteen-months`, Marx's own example (l. 1457: "completes only two-thirds of its turn-over in one year").*
   - Misconception: a capital that turns over twice a year has twice the capital.
   - Worked: £400 with a 3-month turnover turns over 4 times a year: £1,600 of value turned over, still £400 of capital.

2. **fixed-and-circulating-capital** — Fixed Capital and Circulating Capital — *Chapter 8*
   - Read: §1, fixed capital's exchange-value "circulates… gradually and piecemeal" (l. 1479); §2, Marx's £10,000 over ten years and repairs (l. 1598).
   - Do: compute the annual value transferred by fixed capital from value and life, and the value still locked in after so many years, with repairs and moral depreciation.
   - Lab: `turnover`, view `fixed`. Presets: `ten-years` (£10,000 machine, 10 years, at year 4), `repairs` (Marx's 15-year machine booked at 10, `repairs_per_year` 1,000/3, at year 3), `moral` (a machine of the same kind costing £5,000 appears in year 4, `replacement_value`, `appears_year`). Pin `tuWear`, `tuRemaining`.
   - Misconception: fixed and circulating are the same distinction as constant and variable.
   - Worked: a £10,000 machine on a 10-year life transfers £1,000 a year and still has £6,000 of value locked in after four.

3. **aggregate-turnover** — The Aggregate Turnover of Advanced Capital — *Chapter 9*
   - Read: Marx's own figures (l. 1710) and the cycle of turnovers as a material basis for crises (l. 1718). The Kerr text prints the result as "1+2.25", a typesetting slip for 1 2/25; the lesson says so and does not quote it as a figure.
   - Do: compute the aggregate turnover of a capital with fixed and circulating parts and the time the whole capital takes to turn over once.
   - Lab: `turnover`, view `aggregate`. Presets: `marx` (fixed £80,000 on a 10-year life, circulating £20,000 turned 5 times a year), `heavy-fixed` (£95,000 and £5,000), `light-fixed` (£20,000 and £80,000). Pin `tuAggregate`, `tuAverage`, `tuWear`.
   - Misconception: a capital's turnover time is the turnover time of its circulating part.
   - Worked: £8,000 of wear plus £100,000 of circulating capital is £108,000 turned over on £100,000 advanced, 27/25 turnovers a year.

4. **physiocrats-and-adam-smith** — The Physiocrats and Adam Smith on Fixed Capital — *Chapter 10*
   - Read: Smith's definition of fixed capital as what yields a profit "without changing masters" (l. 1800). *Corrected in authoring: Kerr's Smith says "without changing masters", not "without circulating".*
   - Do: classify the same capital by Smith's fixed/circulating and by constant/variable, and show which split determines surplus value.
   - Lab: `turnover`, view `classify`. Presets: `mill` (£500 machine, £100 cotton, £100 wages), `farm` (Smith's farmer, sorted by Marx's turnover test: implements £400 and labouring cattle £200 fixed; fodder £100, seed £100 and wages £200 circulating; Smith himself called the seed fixed, l. 1851, and the lesson says so), `mine` (Marx's copper mine: no raw material, l. 1814; machinery £600, coal £150, wages £250). All at 100%. Pin `tuFixed`, `tuVariable`, `tuS`. *Changed in authoring: `smith` became `mine`, Marx's own counter-example to Smith; the wages-with-materials point is made by every preset.*
   - Misconception: wages and raw materials are the same kind of capital because both circulate.
   - Worked: £100 of cotton and £100 of wages are both circulating, but only the second creates new value.

5. **ricardo-on-fixed-and-circulating-capital** — Ricardo on Fixed and Circulating Capital — *Chapter 11*
   - Read: Ricardo's use of the distinction to explain exceptions to the law of value (l. 1962), and his definition by durability (l. 2025).
   - Do: compute two capitals with the same fixed share and different wage bills, and the surplus value each produces at the same s′.
   - Lab: `turnover`, view `classify`. Presets: `same-fixed` (two £1,000 capitals, both a quarter fixed, wages 250 and 500), `different-fixed` (£600/£150/£250 against £100/£650/£250), `farmer-and-baker` (Ricardo's seed wheat and bread wheat, l. 2054: each £500 fixed, £400 of wheat, £100 of wages). All at 100%. Pin `tuFixed`, `tuVariable`, `tuS`. *Changed in authoring: `durable` and `equal` became `different-fixed` (the converse test: different fixed shares, same s) and Ricardo's own farmer and baker.*
   - Misconception: the fixed/circulating split explains where profit comes from.
   - Worked: same fixed share, different wage bills, different s at 100%: the fixed share cannot tell them apart.

6. **the-working-period** — The Working Period — *Chapter 12*
   - Read: the locomotive's 100 working days as one connected act (l. 2090), and "twelve times more circulating capital" (l. 2082).
   - Do: compute capital tied up over a long working period paid weekly, and the advance needed before any return.
   - Lab: `turnover`, view `working`. Presets: `cotton` (a week), `locomotive` (12 weeks), `ironclad` (52 weeks). All at £100 a week. Pin `tuAdvance`. *Changed in authoring: the cotton period is Marx's week, not a day; `railway` became Marx's `ironclad`, "a year or more".*
   - Misconception: a long working period is only a question of patience.
   - Worked: £100 a week for a 12-week working period ties up £1,200 before anything can be sold.

7. **the-time-of-production** — The Time of Production — *Chapter 13*
   - Read: working time is always production time, not vice versa (l. 2154); tanning by the air-pump (l. 2164).
   - Do: compute the working-time share of a production period and its effect on turnovers a year.
   - Lab: `turnover`, view `time`. Presets: `wheat` (39 weeks, 13 worked, 13 of circulation), `timber` (100 years = 5,200 weeks, 26 worked, no circulation), `tanning-old` (52 weeks in the pits, 4 worked, 4 of circulation), `tanning-air-pump` (8 weeks, the same 4 worked and 4 of circulation). Pin `tuTurnover`, `tuTurnovers`, `tuWorkingShare`. *Changed in authoring: `brewing` became the two tanning presets, Marx's own example of production time cut with no labour saved.*
   - Misconception: shortening production time is always shortening labour time.
   - Worked: a crop needing 3 months of work over 9 months, with 3 months to sell, turns over once a year.

8. **the-time-of-circulation-in-turnover** — The Time of Circulation in the Turnover — *Chapter 14*
   - Read: the time of selling, "relatively the most decisive" section of circulation time, and distance from market (l. 2228, l. 2244).
   - Do: compute how distance and selling time lengthen turnover, and the effect of a faster passage.
   - Lab: `turnover`, view `time`. Presets: `near` (four months' production, two months out and back), `india` (four months out, four back), `faster-passage` (two each way). Production is entered as 52/3 weeks. Pin `tuTurnover`, `tuTurnovers`, `tuCirculationShare`. *Changed in authoring: `railway` became `faster-passage`; the worked example is Marx's India (8 months of circulation on 4 of production, one turnover a year) instead of a 6-week sale.*
   - Misconception: circulation time is wasted only for the merchant.
   - Worked: four months' production and eight months out to India and back is one turnover a year, two-thirds of it in circulation.

9. **turnover-time-and-capital-advanced** — Turnover Time and the Capital Advanced — *Chapter 15*
   - Read: §1, the working period of 9 weeks and the circulation period of 3, and the additional capital (l. 2284); Engels' note on the arithmetic (l. 2889).
   - Do: compute the additional capital a continuous business needs when its working and circulation periods differ, and the capital "set free".
   - Lab: `turnover`, view `advance`. Presets: `marx` (9-week working period at £100 a week, 3-week circulation, a 50-week year), `equal` (5 and 5), `longer-circulation` (4 and 5), `faster-sale` (6 weeks, circulation 3 → 2), `prices-halve` (6 and 3, then £50 a week). Pin `tuAdvance`, `tuFreed`, `tuTurnovers`. *Added in authoring: `faster-sale` and `prices-halve`, Marx's own figures (l. 2881, l. 2912).*
   - Misconception: a capital needs only enough to cover one working period.
   - Worked: 9 weeks at £100 is capital I of £900; to keep working while it circulates for 3 weeks needs capital II of £300.

10. **the-turnover-of-variable-capital** — The Turnover of Variable Capital — *Chapter 16*
    - Read: §1, capitals A and B and "the annual rate of surplus-value" (l. 3032).
    - Do: compute the annual rate of surplus value s′·n and show why it differs between capitals with the same real s′.
    - Lab: `turnover`, view `annual`. Presets: `marx-a` (£500 variable, 4 + 1 week turnover in a 50-week year, 100%), `marx-b` (£5,000 for the 50-week year), `marx-c` (£5,500 over 55 weeks), `b-at-a-pace` (B's £5,000 spent every 5 weeks). Pin `tuTurnover`, `tuTurnovers`, `tuAnnualRate`, `tuMassS`. *Changed in authoring: `same-mass` became Marx's capital C (an annual rate of 10/11, his "90 10-11%") and B on A's footing (£50,000 of s), which show the same point without a two-capital view; A's 4 + 1 split is the text's (l. 3016).*
    - Misconception: a capital that turns over faster exploits its workers harder.
    - Worked: capital A's annual rate is 1,000% and B's 100%; the workers in both are exploited at 100% and produce the same mass of s.

11. **the-circulation-of-surplus-value** — The Circulation of Surplus Value — *Chapter 17*
    - Read: the question where the money comes from to realise the surplus value, and Marx's answer that the capitalist class itself throws it into circulation (§1, l. 3385 and l. 3395).
    - Do: compute the money the capitalist class must spend on its own consumption and the surplus value realised when it returns.
    - Lab: `circuit`, view `realise`. Presets: `class` (£500 as capital, £100 spent), `farmer` (Marx's farmer: £5,000 advanced, £1,000 spent on living), `half-spent` (£50 spent: only £50 of s returns as money). Pin `ciReturned`, `ciS`. *Changed in authoring: `gold` and `credit` cannot be expressed in the `realise` view (it has no gold producer and no credit); the gold producers are treated in prose, credit is left to Volume III, and the presets are Marx's class and farmer and a short-spending case.*
    - Misconception: surplus value cannot be realised in money unless someone outside the capitalist class supplies the money.
    - Worked: Marx's farmer spends £1,000 on living during the year; the same £1,000 returns as the money form of £1,000 of s. Whether this answer also covers accumulation is the question Luxemburg reopened; the `note` says so.

### Course 8 — Reproduction of the Social Capital (`capital-social-reproduction`, 6)

Volume II's Part III. Module names use the Kerr chapter titles: Chapter 18 · Introduction, Chapter
19 · Former Discussions of the Subject, Chapter 20 · Simple Reproduction, Chapter 21 · Accumulation
and Reproduction on an Enlarged Scale (Kerr has "Enlarged", not "Extended"). The lab tiles print
bare numbers, as Marx does; only lesson 2 prices in pounds. All six lessons are in `part_a.py`.

1. **the-object-of-the-inquiry** — The Object of the Inquiry — *Chapter 18 · Introduction*
   - Read: "This total process comprises both the productive consumption…" (Kerr l. 3609).
   - Do: sort a society's product into means of production and means of consumption and say why the individual capital's circuit cannot answer the social question.
   - Lab: `schemes`, view `sort`. Presets: `two-dept` (machines 300, mill coal 100, bread 150, kitchen coal 50, illustrative: `scDeptI` `400: machines, coal for a mill`, `scDeptII` `200: bread, coal for kitchens`), `misclassified` (kitchen coal filed as means of production: 450, 150), `marx-totals` (Marx's 6,000 and 3,000). Pin `scDeptI`, `scDeptII`.
   - Misconception: for society as a whole the entire product is income, the distinctions of the single capital cancelling out (Say, taken over by Proudhon, Kerr l. 3941-3943; Marx's reply at l. 4419: taken as a unit, society is "the aggregate capitalist", not a body that has lost its capitalist character). Corrected in the second review: Marx does not reject treating society as one unit, which he does himself, so "the economy is one big firm" was not Proudhon's error as Marx states it.
   - Worked: the same coal is Department I sold to a mill and Department II sold to a kitchen.

2. **former-presentations** — Former Discussions: Quesnay and Smith — *Chapter 19 · Former Discussions of the Subject*
   - Read: §2, Adam Smith's dogma, the passage beginning "The dogma of Adam Smith" (Kerr l. 3787); "The first mistake of Adam Smith…" (Kerr l. 3838) in the body. Title follows Kerr's chapter title; slug unchanged.
   - Do: compute the annual product's value with and without c, and show where Smith's account loses the constant capital.
   - Lab: `revenue`, view `dogma`, `money_unit` £. Presets: `marx-scheme` (6,000 / 1,500 / 1,500: `rvTotal` £9,000, `rvSmith` `v + s = £3,000; c = £6,000 missing`), `one-firm` (Marx's spinner, 372 / 50 / 78: £500, £372 missing), `tableau` (illustrative, 200 / 100 / 200: £500, £200 missing; Marx gives no Tableau figures in this chapter). Pin `rvTotal`, `rvSmith`.
   - Misconception: the whole price of the annual product is resolved into incomes. Sraffa's reduction to dated labour is stated at strength; the lesson says Marx wrote against Smith, not Sraffa, and what in the chapter bears on it (the one-year period).
   - Worked: 9,000 of annual product against 3,000 of incomes; Smith's account has lost 6,000 of means of production.

3. **simple-reproduction-the-three-exchanges** — Simple Reproduction: The Three Great Exchanges — *Chapter 20 · Simple Reproduction*
   - Read: the recapitulation, "I. 4000 c+1000 v+1000 s = 6000…" (Kerr l. 4031–4037); the condition I(v + s) = IIc (Kerr l. 4076) in the body.
   - Do: check whether a two-department scheme reproduces itself (I(v + s) = IIc) and compute each of the three exchanges.
   - Lab: `schemes`, view `simple`. Presets: `marx` (`scBalance` `I(v + s) = 2,000 = IIc`, `scIExchange` `2,000 each way`), `too-much-in-i` (I s 1,100: gap +100, 100 of Department I's product unsold), `too-little-in-i` (I s 900: gap −100, 1,900 each way, 100 of Department II's product unsold), `diagram-b` (Marx's diagram b from Chapter 21, I 4,000c + 875v + 875s, II 1,750c + 376v + 376s: 1,750 = IIc). Ids are lowercase because the kit requires it; `diagram-b` added because Marx gives a second balanced scheme. Pin `scBalance`, `scIExchange`.
   - Misconception: each department's product only needs a buyer, not a buyer in the other department.
   - Worked: I(1,000v + 1,000s) = 2,000 = IIc; the scheme closes; raise I's s by 100 and 100 of means of production find no buyer.

4. **simple-reproduction-fixed-capital-and-money** — Simple Reproduction: Fixed Capital and Money — *Chapter 20 · Simple Reproduction*
   - Read: §11, Kerr l. 4567 (the money received for wear, a fund for renewing fixed capital in kind; "productive capital suspended in the form of money", Kerr l. 4565, in the body); the crisis passage, Kerr l. 4780: "in spite of the fact that reproduction had taken place on the same scale" (Kerr wording, replacing the planned paraphrase).
   - Do: compute the signed gap between the wear Department II hoards in money and the renewals it buys in kind, and say which side is short.
   - Lab: `schemes`, view `fixed`, Marx's departments, wear 200. Presets: `balanced` (`0: renewals = wear hoarded`), `short-renewals` (100: `−100: 100 of Department I's product unsold`), `bunched` (300: `+100: Department I 100 short`), `marx-180` (Marx's case, Kerr l. 4753: `−20: 20 of Department I's product unsold`; Marx counts 20 on each side, 40 in all, and the body says so). Pin `scFixedGap`.
   - Misconception: depreciation is a cost that balances automatically every year.
   - Worked: renewals of 100 against 200 hoarded leave 100 of Department I's product without a buyer, while the balance tile still reads I(v + s) = 2,000 = IIc; renewals of 300 leave Department I 100 short.

5. **accumulation-and-money** — Accumulation in Department I and the Money It Needs — *Chapter 21 · Accumulation and Reproduction on an Enlarged Scale*
   - Read: §1, Kerr l. 4998 (A's hoard as "a new potential money-capital"; Kerr l. 5002 has "an addition to the potential money-capital"); Engels' note on "latent" and "potential" (Kerr l. 5496).
   - Do: compute the surplus product left unsold when the capitalists of Department I who hoard and those who invest do not balance.
   - Lab: `schemes`, view `hoard`, I 4,000c + 1,000v + 1,000s accumulating 1/2. Presets: `balanced` (hoarders 1/2: `0: hoarders' sales = investors' purchases`), `all-hoard` (1: `+500: 500 of surplus product unsold`), `all-invest` (0: `−500: 500 of demand without a product`). Pin `scHoardGap`.
   - Misconception (Say's law, stated at strength first): every sale is a purchase, so saving automatically becomes investment. The section does not name Say; the lesson says what in it bears on the law. The loanable-funds view and Keynes are stated in their own terms, and the lesson says the text does not answer them.
   - Worked: if every capitalist in Department I hoards at once, 500 of surplus product is unsold.

6. **extended-reproduction** — Reproduction on an Enlarged Scale — *Chapter 21 · Accumulation and Reproduction on an Enlarged Scale*
   - Read: §3, the rule "If things are to proceed normally, accumulation in II must take place more rapidly than in I…" (Kerr l. 5286); the initial diagram I 4,000c + 1,000v + 1,000s, II 1,500c + 750v + 750s as math blocks in the body. Title follows Kerr; slug unchanged.
   - Do: run the expanded scheme for several periods, with Department I accumulating half its s and Department II adjusting, and compute the growth path.
   - Lab: `schemes`, view `expanded`, shipped `periods = 4` (the kit's name for the plan's `years`). Presets: `marx` (`scYear2` `I 4,400c + 1,100v; II 1,600c + 800v`, `scGrowth` `9,000 to 65,219/5: 20,219/45,000 = 44.93%`; Marx prints 13,033, rounding in the fourth year, and Kerr's II total 4,249 is ten short of its parts), `marx-second` (Marx's second illustration, I 5,000c + 1,000v + 1,000s, II 1,430c + 285v + 285s, composition 5 in both: `I 16,250/3c + 3,250/3v; II 4,750/3c + 947/3v`, which Marx rounds to 5,417, 1,083, 1,583, 316; Marx runs it three years and the lab agrees to rounding, except that Kerr prints I's third-year c as 6,385 for 5,869 + 489 = 6,358, which Marx's total 7,629 confirms), `ii-short` (II s 100: `refused in period 1`). `marx-second` replaces the planned `half-half`: Marx gives a second example himself. Pin `scBalance`, `scYear2`, `scGrowth`.
   - Misconception: the two departments can grow at any rates they like. Tugan-Baranovsky and Luxemburg are stated at strength, as later readers; the lesson says what in the chapter bears on their dispute, not Marx's answer.
   - Worked: from I 4,000c + 1,000v + 1,000s and II 1,500c + 750v + 750s, year one ends at I 4,400c + 1,100v and II 1,600c + 800v.

### Course 9 — Cost Price and the Rate of Profit (`capital-cost-price-and-profit`, 7)

Volume III's Part One. Prose cites "Volume III, Chapter n".

1. **cost-price-and-profit** — Cost Price and Profit — *Chapter 1*
   - Read: the opening formula C = c + v + s and its subtraction of s (Kerr l. 456: "produced by capitalist methods is represented by the formula"), then the sale at a profit below value (l. 539).
   - Do: compute cost price k = c + v and profit, and say why profit looks like the offspring of the whole capital.
   - Lab: `profit`, view `cost`. Presets: `marx` (Marx's figures: 400c + 100v + 100s = 600, cost price 500), `cheap-sale` (sold at 560: profit 60, 40 below value), `proudhon` (sold at cost price 500: profit 0), `below-cost` (sold at 480: profit −20). Pin `prCost`, `prProfit`.
   - Misconception: a commodity sold above its cost price is sold above its value.
   - Worked: 600 of value, 500 of cost price: a sale at 560 is profitable and still 40 below value.

2. **the-rate-of-profit** — The Rate of Profit — *Chapter 2*
   - Read: the two sentences defining the rate of surplus value against v and the rate of profit against the total capital (Kerr wording).
   - Do: compute p′ = s/(c + v) beside s′ = s/v for the same capital.
   - Lab: `profit`, view `rate`. Presets: `marx` (400c + 100v + 100s: 20%, 100%), `labour-heavy` (300c + 200v + 100s: 20%, 50%), `capital-heavy` (450c + 50v + 100s: 20%, 200%), `machinery` (Marx's ch. 1 figures with the £1,200 of instruments advanced, 1,580c + 100v + 100s: 5/84, 100%). Pin `prRate`, `prSRate`.
   - Misconception: the rate of profit measures exploitation.
   - Worked: 100s on 400c + 100v is 100% s′ and 20% p′.

3. **rate-of-profit-and-rate-of-surplus-value** — The Rate of Profit and the Rate of Surplus Value — *Chapter 3*
   - Read: the formula p′ = s′·v/C as the Kerr text prints it.
   - Do: vary s′ and the composition one at a time and predict the effect on p′.
   - Lab: `profit`, view `relation`. Presets, all Marx's figures: `base` (80c + 20v + 20s: 20%), `vary-s` (80c + 20v + 40s: 40%, s′ 200%), `vary-composition` (100c + 20v + 20s: 1/6), `both-offset` (104c + 16v + 24s: 20%, s′ 150%), `s-up-p-down` (90c + 10v + 15s: 15%, s′ 150%). Pin `prRate`, `prSRate`.
   - Misconception: a rising rate of surplus value must raise the rate of profit.
   - Worked: s′ up from 100% to 150% while c/v rises from 4 to 6.5: p′ stays at 20%.

4. **turnover-and-the-rate-of-profit** — The Effect of Turnover on the Rate of Profit — *Chapter 4*
   - Read: from Engels' text of the chapter; Engels' preface says Marx left only the title, and the lesson says so in its first paragraph.
   - Do: compute the annual rate of profit from s′, n, v and C.
   - Lab: `profit`, view `turnover`. Presets: `ten-times` (Engels' capital I: 10,500c + 500v, s 500, n = 10: 5/11), `once` (capital III: 6,000c + 5,000v, n = 1: 5/11), `halved` (capital I at n = 5: 5/22), `engels` (the Manchester mill, labelled "Engels' figures": c 12,182, v 318, s per turnover 318 · 80/52, n = 8½: 2,703/8,125 = 33.27%, Engels' figure; his check 4,160/12,500 = 33.28% is the exact turnover 2,704/318). Pin `prAnnual`.
   - Misconception: turnover affects only the circulating capital's profit.
   - Worked: v = 100 turned 5 times at 100% on C = 1,000 gives an annual p′ of 50%.

5. **economy-in-constant-capital** — Economy in the Use of Constant Capital — *Chapter 5*
   - Read: the close of §1 (Kerr l. 1143), "Such economies are: The overcrowding…"; the phrase this entry first quoted is the title of §2 ("Economies in the conditions of labor at the expense of the laborers"), not a sentence of §1.
   - Do: compute the rise in p′ when c is cut with s and v unchanged, and say at whose cost the saving often comes.
   - Lab: `profit`, view `economy`. Presets, illustrative, on 400c + 100v + 100s: `shared-building` (c − 100: 25%), `waste-reuse` (c − 40: 5/23), `unsafe` (guards and ventilation not bought, c − 20: 5/24). Pin `prRate`, `prCost`.
   - Misconception: economy in constant capital is only good management.
   - Worked: cutting c from 400 to 300 with 100v and 100s raises p′ from 20% to 25%.

6. **price-fluctuations-of-raw-materials** — Price Fluctuations of Raw Materials — *Chapter 6*
   - Read: §1 (Kerr l. 1290-1292), the rate of profit falls and rises "inversely as the price of raw material"; second passage l. 1300-1302, the product's price does not follow in full.
   - Do: compute p′ when the raw material's price rises, with and without the product's price following.
   - Lab: `profit`, view `price`. Presets, illustrative, on 400c + 100v + 100s with £100 of cotton: `passed-on` (cotton doubles, passed on 1: 1/6), `half-passed` (passed on 1/2: 1/12, profit 50), `cotton-famine` (passed on 0: profit 0), `cheaper` (cotton halves, passed on 1: 2/9). Pin `prRate`, `prProfit`.
   - Misconception: a raw material price rise is always passed on in full.
   - Worked: c rises from 400 to 500; if the price follows to 700, p′ = 100/600 = 1/6; if it stays at 600, profit is 0. `price_passed_on` moves between the two.

7. **supplementary-remarks-on-profit** — Supplementary Remarks on Profit — *Chapter 7*
   - Read: the chapter's opening, Kerr l. 1544-1546, "Nevertheless the bourgeois will not consider his profit as identical with the surplus-value…" (the phrase "practical notion" is not in the Kerr chapter).
   - Do: reconcile the capitalist's book-keeping view (profit on capital, cost price) with Marx's categories for the same numbers.
   - Lab: `profit`, view `books`. Presets: `ledger` (ch. 1's 400c + 100v + 100s sold at value: profit 100, 20%), `business-a` (Marx's 9,000c + 1,000v + 1,000s: 10%), `business-b` (11,000c + 1,000v + 1,000s: 1/12), `gold` (Marx's £100 earning £20 re-priced as £150, 120c + 30v + 30s: profit 30, 20%; Marx gives no split of the £150 into c and v, so the split is illustrative and the lesson says so). Pin `prProfit`, `prRate`.
   - Misconception: a capitalist who sells at value makes no profit.
   - Worked: sold at its value of 600, the commodity yields a profit of 100 over its cost price of 500; the books and the analysis agree on every figure and disagree only about what the 100 is.

### Course 10 — Average Profit and Its Fall (`capital-prices-of-production`, 8)

Kerr's plain text omits Chapter 9's three tables (printed as tables in the book):
the five spheres at value on Kerr p. 183 (`tables/volume-3/lf0445-03-0183-t0001.png`)
and, on p. 185, the same spheres with used-up c, cost prices and values, and their
prices of production and deviations (`lf0445-03-0185-t0001.png`, `-t0002.png`). The
figures used are read from those images and agree with every total and deviation the
text prints (l. 1681–1693); the lessons cite the pages. Kerr misprints, kept in quotations and named in the
lessons: Chapter 9 "8 + 18 + 26" (for 8 + 18 = 26), Chapter 11 "16 1/12" and
"128 7/12" (exact 16 1/14 and 128 4/7) and "100 10/19" (87½ + 23 1/38 = 110 10/19),
Chapter 13 "66 1/3%" (for 66 2/3%).

1. **different-compositions-different-rates** — Different Compositions, Different Rates of Profit — *Chapter 8*
   - Read: "If a capital, consisting of percentages of 90 c + 10 v…" (Kerr l. 1633).
   - Do: compute the rate of profit of capitals with different compositions and rates of surplus value, and state what selling at value would imply for them.
   - Lab: `prices`, view `rates`. Presets: `marx` (90c + 10v against 10c + 90v at 100%: 10%, 90%), `copper` (Marx's 200c + 100v against 400c + 100v at 100%: 33.33%, 20%), `europe-asia` (Marx's European 84c + 16v at 100% against the Asian 16c + 84v at 25%: 16%, 21%), `equal-composition` (£100 and £1,000 at 80c + 20v: 20%, 20%). Pin `ppRates`.
   - Misconception: a higher rate of surplus value always means a higher rate of profit.
   - Worked: the Asian capital's s′ is a quarter of the European's and its rate of profit is higher: 21% against 16%. (Kerr's l. 1643 calls the Asian 25% a "rate of profit"; its own clause makes it s′, and the lesson says so.)

2. **the-general-rate-of-profit** — The General Rate of Profit and Prices of Production — *Chapter 9*
   - Read: "The aggregate price of the commodities of I to V would be equal to their aggregate value…" (Kerr l. 1707).
   - Do: compute the average rate of profit and each sphere's price of production, and check that total profit equals total surplus value and total price equals total value.
   - Lab: `prices`, view `production`. Presets: `marx` (I–V: 80c + 20v, 70c + 30v, 60c + 40v, 85c + 15v, 95c + 5v at 100%, used-up c 50, 51, 51, 40, 10), `all-used-up` (the same spheres, all c used up: five prices of 122, totals 610), `three` (Marx's l. 1751–1755: 80c + 20v, 90c + 10v, 70c + 30v; three prices of 120, totals 360). Pin `ppAverage`, `ppPrices`, `ppTotals`.
   - Misconception: prices of production abolish the law of value because no commodity sells at its value.
   - Worked: values 90, 111, 131, 70, 20; average rate 22%; prices of production 92, 103, 113, 77, 37; both sum to 422.

3. **market-value-and-surplus-profit** — Market Value and Surplus Profit — *Chapter 10*
   - Read: the market value as the average value of a sphere's commodities and the individual value of its bulk (Kerr l. 1861); the second case, l. 1898.
   - Do: compute a market value as the weighted average of individual values and each group's surplus profit or loss.
   - Lab: `value`, view `market`. Presets (illustrative, 10,000 pieces each): `average-dominates` (1,000 at 3 h, 8,000 at 4 h, 1,000 at 5 h: 4 h), `worst-dominates` (1,000, 3,000, 6,000: 9/2 h — Marx's "strictly speaking" reading of his second case, the average over the mass; the kit does not model demand letting the worst regulate outright), `best-dominates` (6,000, 3,000, 1,000: 7/2 h). Pin `vaMarketValue`, `vaSurplus`.
   - Misconception: supply and demand determine value.
   - Worked: 1,000 units at 3 h, 8,000 at 4 h and 1,000 at 5 h: market value 4 hours; the best group earns 1 hour of surplus profit per unit.

4. **wages-and-prices-of-production** — Wage Changes and Prices of Production — *Chapter 11*
   - Read: "Let wages rise by 25%…" to "the new average rate of profit" (Kerr l. 2010).
   - Do: recompute prices of production after a general wage rise, with the new rate taken over the enlarged capital, and classify each sphere's price as rising, falling or unchanged.
   - Lab: `prices`, view `wage-rise`. Presets: `marx` (80c + 20v named as the average, 50c + 50v, 92c + 8v at 20%; wages rise 25%: 1/7; £120, £900/7, £816/7), `two-spheres` (70c + 30v and 90c + 10v, the whole as the average: 1/7; £860/7, £820/7, summing to 240), `fall` (Marx's l. 2038–2044, wages fall by a quarter: 5/19; £120, £2,100/19, £2,352/19). Pin `ppPrices`, `ppAverage`.
   - Misconception: a general wage rise raises all prices.
   - Worked: profit of 15 on the enlarged 105 is 14 2/7%; the average sphere stays at 120, the low-composition sphere rises to 128 4/7, the high-composition one falls to 116 4/7. The body and `mistakes` say that Marx's text prints 16 1/12 and 128 7/12 (§C formerly asked for this in the `note`).

5. **supplementary-remarks-on-prices** — Supplementary Remarks on Prices of Production — *Chapter 12*
   - Read: §3, "The capitalist simply forgets…" to "the total surplus-value" (Kerr l. 2110).
   - Do: list the compensations (risk, turnover) a capitalist claims and show each as a redistribution within a fixed total profit.
   - Lab: `prices`, view `production`. Presets: Marx's five spheres of Chapter 9 with `none` (22%), `risk-premium` (5% extra for sphere V: base 21%, prices 91, 102, 112, 76, 41), `turnover-premium` (10% extra for sphere I: base 20%, prices 100, 101, 111, 75, 35). Pin `ppTotals` (with `ppAverage`, `ppPrices`).
   - Misconception: each compensation adds new profit.
   - Worked: give sphere V a 5% premium and the base rate falls from 22% to 21%: V gains 4, the other four lose 1 each, total profit stays 110. (Changed from a 2% premium so that every price is whole.)

6. **the-law-as-such** — The Falling Rate of Profit: The Law as Such — *Chapter 13*
   - Read: the table "c = 50, and v = 100 … c = 400, and v = 100, then p' = 100/500, or 20%" (Kerr l. 2122–2128; Kerr prints 66 1/3% for 66 2/3%).
   - Do: compute p′ for a rising c/v at constant s′, and the mass of profit when total capital grows.
   - Lab: `tendency`, view `law`, 4 periods. Presets: `marx` (c 50 rising by 50, 100, 100, 100 on v 100: 1/5, £100), `mass-rises` (Marx's 4c + 2v + 2s to 15c + 3v + 3s, in pounds as millions, the change made in the first of four periods: 1/6, £3,000,000), `steady` (800c + 200v doubling each period: 1/5, £3,200). Pin `teRate`, `teMass`.
   - Misconception: a falling rate of profit means falling profits.
   - Worked: from 4c + 2v + 2s to 15c + 3v + 3s the rate falls from 33⅓% to 16⅔% while the mass of profit rises by half.

7. **counteracting-influences** — Counteracting Influences — *Chapter 14*
   - Read: the opening, "How is it that this fall is not greater and more rapid?" (Kerr l. 2284); the Kerr headings run from "Raising the Intensity of Exploitation" to "The Increase of Stock Capital".
   - Do: apply each counteracting influence to the law's sequence and compute how much of the fall it offsets.
   - Lab: `tendency`, view `counter`, 4 periods, all from 300c + 100v at 100% with c rising 50 a period. Presets: `rising-s` (s′ up 1/8 a period: 25%, offset 25/3 of 25/3 points), `cheap-c` (c cheapens 1/14, 1/15, 1/16, 1/17, halving each rise in its value: 20%, 10/3 of 25/3), `combined` (s′ up 1/16 a period and the same cheapening: 25%, 25/3 of 25/3). Pin `teRate`, `teOffset` (with `teMass`).
   - Misconception: the counteracting influences are either exceptions that leave the law untouched or a refutation of it; Marx's own claim is narrower: they make the fall a tendency.
   - Worked: raising s′ from 100% to 150% holds p′ at 25% when c/v rises from 3 to 5. Marx argues a rising s′ cannot offset a rising c/v without limit; whether that is so is the most argued question about Part III (Okishio, 1961), and the lab does not settle it.

8. **internal-contradictions-of-the-law** — The Internal Contradictions of the Law — *Chapter 15*
   - Read: §2, "The real barrier of capitalist production is capital itself." (Kerr l. 2437); §3, the 1,000 and 1,500 (l. 2453).
   - Do: compute when additional capital adds no additional profit (absolute over-accumulation) and the devaluation that restores the rate.
   - Lab: `tendency`, view `overaccumulation`. Presets: `marx` (Marx's 1,000 yielding 100, split 900c + 100v by the lab, grows to 1,500: 1/15, £100), `devalue` (a third of the 1,500 destroyed: 1/10), `mild` (1,000 grows to 1,100: 1/11). Pin `teMass`, `teRate`.
   - Misconception: crises come from a shortage of capital.
   - Worked: 1,000 yielding 100 grows to 1,500 still yielding 100: p′ falls from 10% to 6⅔%, and the additional 500 has added nothing to profit.

### Course 11 — Merchant's Capital and Interest (`capital-merchants-and-interest`, 9)

Instances as authored (2026-10-24). Corrections the Kerr text forced are marked **Text:**; other changes are marked **Changed:**.

1. **commercial-capital** — Commercial Capital — *Chapter 16*
   - Read: the sentence calling commercial capital a changed form of a portion of the capital of circulation (Kerr l. 2596: "a changed form", not "transmuted" or "converted").
   - Do: compute the commodity capital a merchant takes off the manufacturers' hands from his advance and turnovers, and the merchant's capital a year's trade needs.
   - Lab: `turnover`, view `merchant`. Presets: `no-merchant` (capital 0: £0), `merchant` (Marx's £3,000 of linen, once a year: £3,000), `faster-merchant` (£3,000 four times: £12,000). Pin `tuFreed`.
   - Misconception: merchants produce value by moving goods from hand to hand.
   - Worked: **Changed:** Marx's £3,000 turned over four times carries £12,000 of linen a year, which would need £12,000 turned once (the §C figure of £100 five times is the same arithmetic; the lesson uses the chapter's merchant).

2. **commercial-profit** — Commercial Profit — *Chapter 17*
   - Read: Kerr l. 2717, "720 c + 180 v + 162 s = 1,062 … 1,062 + 18 = 1,080".
   - Do: compute the general rate of profit including the merchant's capital, the price at which the industrialist sells to the merchant, and the merchant's selling price.
   - Lab: `prices`, view `merchant`, one sphere 720c + 180v, s/v = 1. Presets: `marx` (merchant 100: 9/50 = 18%, industrial £1,062, merchant £1,080), `no-merchant` (1/5 = 20%, £1,080 and £1,080), `with-costs` (Marx's 50 of costs, l. 2772: 6/35 = 17.14%, industrial £7,380/7 = 1,054 2/7, merchant £1,130). Pin `ppAverage`, `ppMerchantPrice`.
   - Misconception: the merchant's profit is a mark-up added on top of value.
   - Worked: 180 of s on 1,000 of capital is 18%; the industrialist sells at 1,062, the merchant at 1,080, which is the value.

3. **the-turnover-of-merchants-capital** — The Turnover of Merchant's Capital — *Chapter 18*
   - Read: Kerr l. 2930, 15% a year, once (115) and five times (103; "500 sold 515").
   - Do: compute the mark-up per turnover from the general rate and the merchant's turnovers a year.
   - Lab: `prices`, view `merchant-turnover`. Presets: `marx` (3/20, five turnovers: 3%, sells at £103), `once` (15%, £115), `ten` (1.5%, £203/2). Pin `ppMarkup`, `ppMerchantPrice`.
   - Misconception: a faster-turning merchant earns a higher rate of profit.
   - Worked: at 15% a year, a merchant who turns over five times sells at 103 each time, 3% a turnover.

4. **money-dealing-capital** — Money-Dealing Capital — *Chapter 19* (Kerr title "Financial Capital"; the module keeps it)
   - Read: **Text:** Kerr l. 2966-2968, the "purely technical labor of paying money and receiving money" organised as a special department. The §C phrase "movements that money undergoes" is not Kerr's; l. 2960 reads "purely technical movements performed by money" and opens on a drop capital, so it is quoted inline.
   - Do: compute the general rate with a money-dealer's capital in the averaging, the dealer's share and the manufacturers' price.
   - Lab: `prices`, view `merchant`; Marx's 900 industrial and 100 merchant, with the money-dealer's capital entered in `merchant_capital` beside the merchant's (the view has one field for capital in circulation). Presets: `none` (100: 18%, £1,062), `cashier` (100 + 125: 4/25 = 16%, £1,044; cashier draws 20), `exchange` (100 + 125 + 75: 3/20 = 15%, £1,035; dealers draw 30). Pin `ppAverage`, `ppMerchantPrice`.
   - Misconception: money-dealing creates value because it handles value.
   - Worked: **Changed:** a cashier's 125 beside Marx's 900 and 100 gives 16%; the cashier draws 20, the manufacturers 144, the merchant 16. (§C's "50 draws 9 at 18%" is not consistent: adding 50 to Marx's 1,000 gives 6/35, not 18%.)

5. **history-of-merchants-capital** — Historical Facts about Merchant's Capital — *Chapter 20*
   - Read: **Text:** Kerr l. 3079, "The merchants' capital is at first merely the intervening movement between extremes not controlled by it and between premises not created by it."
   - Do: compute a pre-capitalist merchant's gain from buying cheap in one community and selling dear in another, beside the capitalist merchant's share of an average rate.
   - Lab: `circuit`, view `formula`, start money. Presets: `venice` (60 to 100: +£40), `dutch` (a monopoly company, 25 to 100: +£75), `capitalist` (100 to 118: +£18). Pin `ciDelta` (and `ciForm`).
   - Misconception: a merchant's profit is always a share of an average rate of profit.
   - Worked: buying at 60 and selling at 100 between communities yields 40 that no general rate limits; the capitalist merchant of “Commercial Profit” gets 18 on 100.

6. **interest-bearing-capital** — Interest-Bearing Capital — *Chapter 21*
   - Read: Kerr l. 3133, "a man having 100 p.st. at his disposal … is called interest".
   - Do: compute what the lender's £100 lets a borrower make at the average rate and the interest paid out of it.
   - Lab: `interest`, view `split`. Presets: `marx` (£100, 1/5, 1/20: £5, £15), `high-rate` (1/10: £10, £10), `low-rate` (1/50: £2, £18). Pin `inInterest`, `inEnterprise`.
   - Misconception: interest is the price of money.
   - Worked: £100 makes £20 at the average rate; £5 goes to the lender and £15 stays with the borrower as profit of enterprise.

7. **the-rate-of-interest** — The Rate of Interest — *Chapter 22*
   - Read: Kerr l. 3349, "there is no such thing as a 'natural' rate of interest" (also l. 3291 in Chapter 21).
   - Do: compute interest and profit of enterprise across rates and show the bounds 0 < i < p′.
   - Lab: `interest`, view `bounds`, capital £100. Presets: `normal` (Marx's l. 3311 figures, 4/25 and 1/25: £12, `0 < 4% < 16%`), `plenty` (1/5 and 3/200, the 1½% of September 1843: £37/2, `0 < 3/2% < 20%`), `crisis` (1/20 and 2/25, the 8% of 1847: −£3, `breached: 8% ≥ 5%`). Pin `inEnterprise`, `inBound`.
   - Misconception: there is a natural rate of interest set by productivity.
   - Worked: **Changed:** Marx's own pair from l. 3311, 20% and 8% against 16% and 4%: both leave £12.

8. **interest-and-profit-of-enterprise** — Interest and Profit of Enterprise — *Chapter 23*
   - Read: Kerr l. 3454, "wages of superintendence of labor".
   - Do: split gross profit into interest and profit of enterprise and separate the wages of a hired manager from both.
   - Lab: `interest`, view `split`, £100 at 1/5 and 1/20. Presets: `owner` (principal 0: £0, £20; the owner's reckoning of interest to himself is in the prose), `borrower` (£5, £15), `manager` (salary £6: £5, £9). Pin `inEnterprise`, `inInterest`.
   - Misconception: profit of enterprise is the capitalist's wage for managing.
   - Worked: with £5 of interest and £15 of profit of enterprise, a £6 manager's salary leaves £9 that, on Marx's account, is paid for owning and directing capital, not for any work of superintendence.

9. **interest-bearing-capital-as-a-thing** — Interest-Bearing Capital as a Thing — *Chapter 24*
   - Read: **Text:** Kerr l. 3561, Price quoted by Marx: "A penny, loaned at the birth of our Savior at compound interest at 5%…". The §C wording ("put out at our Saviour's birth") is not Kerr's. Source in fn. 81 (l. 7579): Price's *Appeal*, 1772.
   - Do: compute Price's compound sum and compare it with the accumulation of real capital at a stated rate, and say why the first is impossible.
   - Lab: `interest`, view `compound`, `money_unit` s. Presets: **Changed:** `price` (1d at 5% for 1,772 years, real growth 1%: 37 digits against 7), `child` (Josiah Child's £100 = 2,000s at 10% for 70 years, l. 3573, real growth 2%: 7 digits against 4), `ten-years` (2,000s at 5% for ten years, real growth 5%: equal). The `real` preset's instance, "a capital growing with the product", is the `inReal` tile of every preset, so `child` takes its place. Pin `inCompound`, `inReal`.
   - Misconception: money left at interest grows by itself.
   - The `note` cross-references “Compound Interest and Continuous Growth” on the Algebra path.
   - Worked: **Changed:** Child's £100 at 10% for 70 years, about £78,975 yearly (his 102,400 is £100 doubled ten times), against about £400 at 2%.

### Course 12 — Credit and Fictitious Capital (`capital-credit-and-fictitious-capital`, 12)

1. **credit-and-fictitious-capital** — Credit and Fictitious Capital — *Chapter 25*
   - Read: bills of exchange as "commercial money".
   - Do: compute the cash a chain of bills needs when settled, and the claims left standing against nothing when a bill has no sale behind it.
   - Lab: `money`, view `payments`. Presets: `bills` (three backed bills of £100 in a circle: £0), `discounted` (B sells his bill on A to a bank: £100 of cash, the bank's own), `accommodation` (the circle plus a £100 bill A accepts for B with no sale behind it: £100 needed, £100 unbacked). Pin `moNeeded`, `moNetted`, `moUnbacked`.
   - Misconception: a bill of exchange is a loan of money.
   - Worked: three bills of £100 in a circle settle with no cash; one accommodation bill leaves £100 of claims against nothing.

2. **accumulation-of-money-capital** — Accumulation of Money Capital and the Rate of Interest — *Chapter 26*
   - Read: Overstone's evidence before the Committee of 1857.
   - Do: compute what a rise in the rate of interest does to profit of enterprise and to the borrowing industrialist.
   - Lab: `interest`, view `bounds`. Presets: `low` (interest 3%), `high` (8%), `crisis` (interest at 10%, equal to the profit rate: the bound is reached, profit of enterprise £0; the view cannot go above the profit rate). State Overstone's evidence at strength. Pin `inEnterprise`.
   - Misconception: a high rate of interest shows a scarcity of capital in general.
   - Worked: at a 10% average rate, moving interest from 3% to 8% cuts profit of enterprise from 7 to 2 per 100.

3. **the-role-of-credit** — The Role of Credit in Capitalist Production — *Chapter 27*
   - Read: Kerr l. 3899-3901, the transformation of the capitalist into "a mere manager" and of the owner into "mere money-capitalists"; then l. 3913, "This is the abolition of the capitalist mode of production within capitalist production itself" (Kerr wording).
   - Do: compute a stock company's profit paid out as dividend, the manager's salary, and what each looks like: interest on the shares and wages.
   - Lab: `interest`, view `split`. Presets: `stock-company` (£1,000 of shares, 22% profit, dividend at 20%, a £20 salary: enterprise £0), `owner-managed` (20% profit, 5% interest: £50 and £150), `leveraged` (£800 of the £1,000 borrowed at 5%: £40 and £160). Pin `inInterest`, `inEnterprise`.
   - Misconception: in a stock company the profit of enterprise stays with the people who run it.
   - Worked: £200 of profit is paid out as dividend and looks like interest on £1,000; the manager is paid a salary; the figure of the owner-entrepreneur has split in two, "a mere manager" and "a mere money-capitalist".

4. **medium-of-circulation-and-capital** — Medium of Circulation and Capital: Tooke and Fullarton — *Chapter 28*
   - Read: the distinction between money as currency and money as capital.
   - Do: classify payments as circulation of revenue or transfer of capital and compute the notes each needs.
   - Lab: `money`, view `circulate`. Presets: `revenue` (wages spent in shops, £1,000 at velocity 10: £100), `capital` (payments between capitalists, £1,000: £100), `mixed` (£2,000: £200), `credit` (the capital payments at velocity 25: £40). Pin `moNeeded`. Kerr l. 3953 prints "price" for "piece"; the lesson quotes it as printed and says so.
   - Misconception: the quantity of notes measures the quantity of capital.
   - Worked: £1,000 of wage spending at velocity 10 needs £100 of notes; £1,000 lent to a manufacturer needs none extra once it is spent.

5. **component-parts-of-bank-capital** — The Component Parts of Bank Capital — *Chapter 29*
   - Read: "The formation of a fictitious capital is called capitalisation."
   - Do: compute the price of a claim to a yearly income at a rate of interest, and what a change in the rate does to it with nothing real changing.
   - Lab: `interest`, view `capitalise`. Presets: `marx` (Marx's figures: £100 a year at 5%: £2,000), `rate-up` (10%: £1,000), `rate-down` (2½%: £4,000), `share` (Marx's share, £10 a year at 5%: £200). Pin `inPrice`.
   - Misconception: the price of a security measures real capital invested.
   - Worked: £100 a year at 5% is £2,000; at 10% the same claim is £1,000 and nothing has been destroyed.

6. **money-capital-and-real-capital-i** — Money Capital and Real Capital I — *Chapter 30*
   - Read: Kerr l. 4238, "Not every augmentation of loanable capital indicates a real accumulation of capital or expansion of the process of reproduction."
   - Do: compute the money that piles up in hoards while no real accumulation takes place.
   - Lab: `schemes`, view `hoard`. Presets: `balanced` (Volume II's Department I, 4,000c + 1,000v + 1,000s, half of s accumulated, half the accumulators hoard: 0), `stagnant` (all hoard: +500), `boom` (a quarter hoard: −250). Pin `scHoardGap`.
   - Misconception: a pile of bank deposits means plenty of real capital.
   - Worked: 500 of surplus product unsold is 500 of money hoarded and lent to the bank; loanable capital has grown and real accumulation has not.

7. **money-capital-and-real-capital-ii** — Money Capital and Real Capital II — *Chapter 31*
   - Read: Kerr l. 4316, loan capital accumulated "by mere technical means"; the contraction case is l. 4312 ("the money-capital, which was formerly employed in production and commerce, appears as unemployed loan capital"), and Chapter 32 (l. 4406) adds capital released by a fall in prices, which Course 7's `prices-halve` preset shows.
   - Do: compute the circulating capital set free when a business contracts, which becomes loan capital without anyone saving.
   - Lab: `turnover`, view `advance`. Presets: `contract` (Marx's 9 + 3 weeks at £100, then £50 a week: £600 released), `steady` (£100: £0 released), `expand` (£150: £600 more tied up). Pin `tuAdvance`, `tuFreed`.
   - Misconception: loan capital is only savings out of income.
   - Worked: halving the business releases £600 of circulating capital to the money market; nobody saved a penny.

8. **money-capital-and-real-capital-iii** — Money Capital and Real Capital III — *Chapter 32*
   - Read: the demand for means of payment in times of crisis.
   - Do: compute the cash a chain of payments needs before and after one default, with the sum of prices unchanged.
   - Lab: `money`, view `payments`. Presets: `prosperity` (the chain clears: £0), `crisis` (bill 1 defaulted, Course 1's `broken` chain: £100), `cash-only` (credit stopped, every sale in cash at velocity 1: £300; replaces `recovery`, since Chapter 32's recovery is borrowing to buy, which this view cannot show). Pin `moNeeded`, `moNetted`. Read: Kerr l. 4486; its second clause, "by no means a demand for money as a means of payment", reads as a slip for means of purchase (Marx's German has *Kaufmittel*), and the lesson says the slip is the translation's.
   - Misconception: in a crisis capital is scarce.
   - Worked: the same commodities and prices need £0 of cash while the chain holds and £100 once it breaks: what is scarce is money as means of payment, not capital.

9. **the-medium-of-circulation-in-the-credit-system** — The Medium of Circulation in the Credit System — *Chapter 33*
   - Read: Kerr l. 4579, "Hence only the requirements of business itself exert an influence on the quantity of circulating money—notes and gold."
   - Do: compute the notes the circulation needs and what happens to an over-issue.
   - Lab: `money`, view `bank-act` (not `circulate`: only `bank-act` has `issue` and `moReturned`; its cap is set high enough never to bind). Presets: `needs` (£600 of goods at velocity 4: £150 needed, £150 issued), `over-issue` (`issue` £200: £50 flows back), `crisis-demand` (velocity 2, Wright's "twice as much currency": £300). Pin `moNeeded`, `moReturned`.
   - Misconception (the Currency School's view, stated at strength: Overstone held that note issue determines the circulation and through it prices): the bank decides how much money circulates.
   - Worked: issue £200 of notes where circulation needs £150 and £50 flows back as deposits or repayments.

10. **the-currency-principle-and-the-bank-act** — The Currency Principle and the Bank Act of 1844 — *Chapter 34*
    - Read: Kerr l. 4839, Engels' sentence on the mechanism ("For every five pounds in gold..."); most of Chapter 34 is Engels' brackets round a quotation from the Contribution of 1859, and the lesson says so.
    - Do: compute the note issue the 1844 Act allowed against gold, and the gap in a drain when the circulation's needs do not fall.
    - Lab: `money`, view `bank-act`. Presets in pounds, Marx's figures from Chapter 29 (l. 4159): `normal` (14m fixed + 14m gold: cap £28m, 20m out), `drain` (6m of gold exported: cap £22m), `panic` (demand 24m, Gurney's 4m hoarded: £2m unmet), `suspension` (fixed issue raised by 2m, illustrative: gap £0). Pin `moCap`, `moGap`. Hubbard's first table (Kerr p. 646) supplies two rows.
    - Misconception (Overstone and the Currency School at strength: a mixed currency should behave exactly as a metallic one would): tying notes to gold stabilises the circulation. Marx sides with Tooke and Fullarton, and the lesson presents it as his reply.
    - Worked: 14 + 14 = 28; a 6m drain cuts the cap to 22 and the banking reserve from 8 to 2; a panic demand of 24 leaves 2 unmet.

11. **precious-metal-and-the-rate-of-exchange** — Precious Metal and the Rate of Exchange — *Chapter 35*
    - Read: Kerr l. 5018, "The barometer for the international movement of the money metals is the rate of exchange." This is Engels' bracket, not Marx; the lesson says so.
    - Do: compute the net balance and the bullion shipped when exchanges move past the gold points.
    - Lab: `money`, view `world`. Presets: `balanced` (imports 8m, exports 6m, other receipts 2m: £0), `harvest-failure` (imports 9m: £1m out), `india` (Newmarch's 1855 figures, l. 5042-5044: imports from India 12,670,000, exports 10,350,000, India House drafts 3,700,000: £1,380,000 in). Pin `moDrain`.
    - Misconception: a gold outflow means the country is getting poorer.
    - Worked: £9m of imports against £6m of exports and £2m of other receipts leaves £1m to be paid in gold (the harvest-failure preset).

12. **pre-capitalist-relationships** — Pre-Capitalist Relationships — *Chapter 36*
    - Read: Kerr l. 5206, "it undermines and ruins small peasants' and small burghers' production".
    - Do: compute a small producer's debt year by year when the usurer's interest exceeds the surplus, and the year the debt exceeds the holding.
    - Lab: `interest`, view `usury`. Presets (in £): `peasant` (surplus 10 a year, debt 50 at 30%, holding 100: year 6), `artisan` (20 at 20%, surplus 10: repaid in year 3), `leipzig` (the peasant at Luther's 40%: year 4), `lord` (1,000 at 10%, 50 to spare, estate 2,000: year 12). Pin `inInterest`, `inYearsToRuin`.
    - Misconception: usury is high interest on loans for production.
    - Worked: 15 of interest against a surplus of 10 adds 5 in the first year and more each year after, because the unpaid interest itself bears interest; the lab prints the year the debt passes 100.

### Course 13 — Ground Rent (`capital-ground-rent`, 11)

Instances as authored (2026-10-24). Corrections the Kerr text forced are marked **Text:**; other changes are marked **Changed:**. Every preset was checked against Marx's printed tables (images in `tables/volume-3/`, Kerr pp. 764–858) as well as the sentences around them. **Changed:** the `dr1`/`dr2` labs reckon in shillings throughout (`money_unit` s, `qty_unit` quarter): Marx's £2½ is 50s and his £3 a quarter is 60s; `price`, `waterfall` and `absolute` stay in £.

1. **introductory-remarks-on-rent** — Introductory Remarks on Ground Rent — *Chapter 37*
   - Read: **Text:** Kerr l. 5379, "Ground-rent so capitalised forms the purchase price or value of the land, a category which is on its face irrational…"; the §C phrase is Kerr's at l. 5393 ("is nothing but the capitalised income from the lease of the land") and is quoted inline.
   - Do: compute the price of land from rent and the rate of interest, and separate true rent from interest on capital sunk in the land.
   - Lab: `rent`, view `price`. Presets: `marx` (£200 at 5%: `£4,000`, `£200`), `rate-falls` (4%: `£5,000`), `improvements` (£50 of the £200 is interest on land-capital: `£4,000`, true rent `£150`). Pin `rtPrice`, `rtTrueRent`.
   - Misconception: rent is the return on the land's value.
   - Worked: £200 a year at 5% is a price of £4,000; when the rate falls to 4% the same land costs £5,000.

2. **differential-rent-general** — Differential Rent: General Remarks — *Chapter 38*
   - Read: Kerr l. 5545, "The natural power is not the source of the surplus profit, but only its natural basis…".
   - Do: compute the surplus profit of the capital with a monopolisable natural advantage both ways Marx does, and the rent it becomes.
   - Lab: `rent`, view `waterfall`. Presets: `marx` (100 on steam, 90 on water, 15%: `£115`; `£10 … ; £11½ …`), `two-falls` (cost 80: £20; £23), `steam-cheapens` (steam's cost falls to 90: `£207/2`, surplus £0). Pin `rtPrice`, `rtSurplusProfit`.
   - Misconception: the waterfall creates the surplus profit.
   - Worked: as planned (115 − 90 − 15 = 10; 115 − 103½ = 11½).

3. **differential-rent-i** — Differential Rent I — *Chapter 39*
   - Read: Table I, Kerr p. 764, read with l. 5600–5610.
   - Do: as planned.
   - Lab: `rent`, view `dr1`. Presets: `marx` (Table I: `60s a quarter`, `0s, 60s, 120s, 180s`, `360s`), `descending` (D, C, B in use, the middle step of Marx's descending succession: 30s; 0s, 30s, 60s; 90s), `better-added` (Table II, p. 768, four of its seven soils: A at 1⅓ quarters, B, C, D: 45s; 0s, 30s, 75s, 120s; 225s), `improved` (Table III, p. 768: 2, 4, 7, 10 quarters: 30s; 0s, 60s, 150s, 240s; 450s). **Changed:** `improved` added because Table III is printed in full. Pin `rtPrice`, `rtRents`, `rtTotal`.
   - **Text:** Table II has seven soils (A 1⅓, A′ 1⅔, B 2, B′ 2⅓, B″ 2⅔, C 3, D 4; rent 345s); the lab holds six, so the lesson gives the other three in prose. Kerr l. 5651 says Table III's rental rises "from 18 pounds sterling to 22, a growth of 22 1/9%" and that rent is "doubled upon C"; the table prints 450s (£22½, +25%) and C's rent goes from 120s to 150s. The lesson names both slips.
   - Misconception: as planned.
   - Worked: as planned.

4. **differential-rent-ii** — Differential Rent II — *Chapter 40*
   - Read: Kerr l. 5823 ("differential rent No. II is but a different expression of differential rent No. I").
   - Lab: `rent`, view `dr2`. **Changed:** presets `side-by-side` (Table I: 360s), `same-acre` (Marx's four £2½ portions on one acre of D yielding 4, 3, 2, 1: rent `360s`), `second-on-d` (A–D with a second 50s on D yielding 3: 0s, 60s, 120s, 300s; 480s) replace `diminishing`, `constant`, `increasing`, because Marx's own test in this chapter is the same capital laid side by side or on one acre. The §C worked example (180s and 120s on D's two doses) holds in `second-on-d`.
   - **Text:** Kerr l. 5833 reckons D's rent as "10-2 = 8 quarters … or 12 pounds sterling", setting four doses against one; dose by dose at £1½ it is £3. The lesson says so.
   - Misconception, Worked: as planned.

5. **dr-ii-constant-price** — Differential Rent II at a Constant Price of Production — *Chapter 41*
   - Lab: `rent`, view `dr2`, `price_case = constant`. Presets: `proportional` (Table II, p. 802: 0s, 120s, 240s, 360s; 720s), `slower` (Table III, p. 803: second doses 1½, 2, 3½ on B, C, D: 0s, 90s, 180s, 330s; 600s, Marx's £30), `faster` (illustrative: 3, 4, 5: 900s). Pin `rtPrice`, `rtRents`, `rtTotal`.
   - **Text:** D's second dose has three yields in the text: Ch. 40 (l. 5884) says D raises 6 quarters in all, its own rents (l. 5884–5886, table p. 800) need 7, and Ch. 41's Table III prints 7½. The lab follows Table III; the lesson and `mistakes[2]` explain.
   - Misconception, Worked: as planned (worked on B: 60s → 90s, 120% → 90%).

6. **dr-ii-falling-price** — Differential Rent II at a Falling Price of Production — *Chapter 42*
   - Lab: `rent`, view `dr2`, `price_case = falling`. **Changed:** presets `a-drops-out` (Table IV, p. 811: Table II's soils, market 18 quarters: 30s; 0s, 0s, 60s, 120s; 180s), `iv-d` (Table IV d, p. 814: D five doses: 360s), `rent-rises` (table p. 817: D 44 quarters from £27½, market 54: C 60s, D 660s; 720s). `rent-falls` is dropped: `a-drops-out` is the falling case. D's eleven doses exceed the kit's six, so `rent-rises` enters D as one 550s capital yielding 44 quarters, the same 15s a quarter. Pin `rtPrice`, `rtRents`, `rtTotal`.
   - **Text:** Kerr l. 5956 says "D and its price of production of 30 shillings" would regulate; it is B (Table IV). The p. 817 table prints C's grain rent as 3 and the grain total as 25 (2 and 24). Table V (p. 820) prices B at its average over two doses (1 5/7) and is described, not computed.
   - Misconception, Worked: as planned.

7. **dr-ii-rising-price** — Differential Rent II at a Rising Price of Production — *Chapter 43*
   - Read: **Text:** the chapter's opening is Engels' (it begins at l. 6094 in Engels' brackets; the manuscript had "only its title", l. 6123); the Read passage is Marx's conclusion, l. 6398–6400. Engels' twenty-one tables (VII–X a, XI–XXIV, pp. 829–839) mostly price a soil at its average and are described, not computed.
   - Lab: `rent`, view `dr2`, `price_case = rising`. **Changed:** presets `worse-investment` (B's further £5 yields 1½ at £4, Marx's table p. 849, entered as two ¾-quarter doses: 80s; 20s, 160s; 180s), `new-soil` (A−1 and A−2, l. 6352: 120s; 60s, 300s, 60s, 0s; 420s), `ricardo-case` (illustrative ¾ quarter on D: 80s; 560s). `results` dropped: the chapter's "Results" are argument, not a table.
   - Misconception, Worked: as planned (worked on A−1, A−2).

8. **rent-on-the-worst-soil** — Differential Rent Also on the Worst Cultivated Soil — *Chapter 44*
   - Read: Kerr l. 6418.
   - Lab: `rent`, view `dr2`, `price_case = worst-soil`. Presets: `marx` (Marx's second table, p. 858: A 1, B 2 + 1½ + extra dose at £3½ (entered as 6/7 quarter on 50s), C 3 + 2½, D 4 + 3½: 70s; 10s, 125s, 265s, 405s; 805s = £40¼), `on-a` (A's own second dose at £3¾: 75s; 15s, 142s 6d, 292s 6d, 442s 6d), `both` (both extra doses offered, market 257/14 quarters: as `marx`). **Changed:** `none` dropped: the worst-soil case check refuses a preset in which A pays no rent. Pin `rtPrice`, `rtRents`, `rtTotal`.
   - **Text:** Engels' bracketed correction (l. 6422–6424) prices B's whole product at its average including the old rent: A pays 1/9 pound, B stays £4½. Kerr prints that average as "3½ pounds sterling" twice; 14/4½ is 3 1/9. The lesson states both rules; the lab computes Marx's.
   - Misconception, Worked: as planned.

9. **absolute-ground-rent** — Absolute Ground Rent — *Chapter 45*
   - Read: **Text:** Kerr l. 6641, "Private property in land prevents such an equalization among capitals invested in the soil…" (the §C wording is not Kerr's).
   - Lab: `rent`, view `absolute`. Presets: `marx` (`£120`, `up to £5`), `average-composition` (`£115`, `up to £0`), `market-limited` (market bears 122: `up to £2`). Pin `rtPrice`, `rtAbsolute`.
   - Misconception, Worked: as planned; "would disappear" is Kerr l. 6591.

10. **building-rent-mining-rent-land-price** — Building Rent, Mining Rent, the Price of Land — *Chapter 46*
    - Read: **Text:** Kerr l. 6651, "toward which he contributes nothing and for which he risks nothing" (wording confirmed), quoted inline; the opening block is l. 6651's "This form of rent is distinguished…".
    - Lab: `rent`, view `price`. **Changed:** presets `town-before` (£50 at 5%: `£1,000`), `town-grows` (£150: `£3,000`), `capps` (Capps's ground, £300 raised to £400, l. 6655: `£8,000`), `mine` (Smith's Scottish mine that pays no rent: `£0`); `speculation` became `capps`, Marx's own builder. Pin `rtPrice`, `rtTrueRent`.
    - Misconception, Worked: as planned.

11. **genesis-of-capitalist-ground-rent** — Genesis of Capitalist Ground Rent — *Chapter 47*
    - Read: **Text:** Kerr l. 6769 reads "is still separated by space and time from his labor for the landlord" ("by", not "in"); the opening block is l. 6769.
    - Lab: `workday`, view `corvee`, `money_unit` hours. **Changed:** presets `two-days` (Marx's two days a week for the lord, l. 6779: `1/2 = 50%`), `three-three` (`1 = 100%`), `four-two` (`2 = 200%`); `money-rent` dropped because the corvée view cannot express rent in kind or money rent, which the lesson treats in prose. Pin `wdSurplus`, `wdRate`.
    - Misconception, Worked: as planned.

### Course 14 — Revenues and Their Sources (`capital-revenues-and-their-sources`, 5)

Module names use Untermann's chapter titles (§E.3): The Trinitarian Formula; A Contribution to the
Analysis of the Process of Production; The Semblance of Competition; Conditions of Distribution and
Production; The Classes. Lesson titles are as below.

1. **the-trinity-formula** — The Trinity Formula — *Chapter 48*
   - Read: the opening statement of the trinitarian formula and its reduction to Capital—Interest, Land—Ground-Rent, Labor—Wages (Kerr vol. 3, l. 6924–6926).
   - Do: decompose a year's v + s into wages, profit of enterprise, interest and rent, and show that all three "revenues" come from one value product.
   - Lab: `revenue`, view `trinity`. Presets (all illustrative, c 100, v 100, s 100): `english` (rent 3/10 of s, interest 1/5: half the capital borrowed), `no-landlord` (rent 0, interest 1/5), `all-borrowed` (rent 3/10, interest 2/5). Pin `rvWages`, `rvRent`, `rvInterest`, `rvProfitShare` (and `rvTotal` on `english`).
   - Misconception: each factor of production creates its own income.
   - Worked: a value product of 200 is 100 wages, 30 rent, 20 interest and 50 profit of enterprise; by the chapter's accounting land and capital add nothing to the 200. The `note` states the opposing account at strength: Say's three factors and Clark's marginal productivity, on which each factor is paid what it adds at the margin.

2. **analysis-of-the-process-of-production** — Concerning the Analysis of the Process of Production — *Chapter 49*
   - Read: the two questions on how a value of wages plus profit plus rent buys a product worth that plus C (l. 7060–7062).
   - Do: compute the part of the annual product that is replaced inside Department I and is never anyone's revenue.
   - Lab: `schemes`, view `simple`. Presets: `marx` (Marx's figures, I 4,000c + 1,000v + 1,000s, II 2,000c + 500v + 500s, l. 7092–7094), `growing` (Marx's figures: Volume II, Chapter 21's initial diagram for accumulation, II 1,500c + 750v + 750s, vol. 2 l. 5210–5214), `one-sector` (illustrative: Department I set to 0, Department II as in `marx`). Pin `scWithinI`, `scBalance` (and `scIExchange` on `growing`).
   - Misconception: annual income equals the annual product.
   - Worked: of 9,000 of annual product, 4,000 (Ic) is means of production exchanged among Department I's own capitalists and never enters anyone's income.

3. **illusions-created-by-competition** — Illusions Created by Competition — *Chapter 50*
   - Read: the passage in which the value of commodities "exists first" and the wrong conception makes wages, profit and rent independent magnitudes (l. 7248).
   - Do: compute price both ways — value resolved into parts, and parts added up — and show the second is circular.
   - Lab: `revenue`, view `added-up`. Presets: `wage-rise` (Marx's figures, 400c + 100v + 150s with wages up 50, l. 7198–7204; rent 1/2 of s and interest 0, so the lab splits the reduced s 50/50 where Marx says "say" 45 profit and 55 rent), `rent-rise` (illustrative: c 100, v 100, s 100, rent 1/2, interest 1/5, no wage change), `fixed-value` (illustrative: c 100, v 100, s 100, rent 3/10, interest 1/5, wages up 20). Pin `rvWages`, `rvRent`, `rvProfitShare` (and `rvInterest` on the two illustrative presets).
   - Misconception: a wage rise raises prices because wages are a component added to them.
   - Worked: with value product fixed at 200, a wage rise from 100 to 120 cuts profit, interest and rent by 20 together.
   - Text note: the Kerr text prints wages after the rise as 27 8/11% of the capital advanced; 150/550 is 27 3/11%. The lesson says so. Marx's summary table of the two cases is on Kerr p. 996 (image `tables/volume-3/lf0445-03-0996-t0001.png`); the lesson cites it for the 650 and 250, which agree with the text. Its rate columns read 66 1/8% and 80% in the image, where the text (l. 7214) has 66 2/3% and 30%; the lesson uses the text's figures.

4. **distribution-and-production-relations** — Distribution Relations and Production Relations — *Chapter 51*
   - Read: the passage in which the conditions of distribution are the "reverse side" of the conditions of production (Kerr's wording, l. 7354), with l. 7358.
   - Do: compute the same product's distribution under two production relations (a wage relation and an association of producers) and say what changes and what does not.
   - Lab: `revenue`, view `trinity`. Presets (illustrative, c 100 and value product 200 in each): `capitalist` (v 100, s 100, rent 3/10, interest 1/5), `cooperative` (workers own the firm but rent its land and borrow its capital: v 150, s 50, rent 3/5, interest 2/5, so rent 30, interest 20, profit of enterprise 0), `association` (v 150 consumed, s 50 common fund, no rent or interest). Pin `rvWages`, `rvRent`, `rvInterest`, `rvProfitShare`.
   - Misconception: distribution can be changed without changing production relations.
   - Worked: the association preset keeps c for replacement and a fund for expansion; only the split of v + s and who decides it change.

5. **classes** — Classes — *Chapter 52*
   - Read: "The first question to be answered is this: What constitutes a class?" — and where the manuscript breaks off.
   - Do: group a small society's people by source of revenue, and count the groups as the sources are made finer.
   - Lab: `revenue`, view `classes`. Presets: `three-classes` (two spinners on wages, a mill owner and a manufacturer on profit, a landlord on rent: 3 groups), `doctor-and-official` (the same five plus a physician on medical fees and an official on a salary: 5 groups), `landowners-split` (a spinner, a mill owner, and owners of vineyards, farms, forests, mines and fisheries each on their own rent: 7 groups). Pin `rvClassCount`.
   - Misconception: a class is defined by its source of income alone.
   - Worked: group by source of revenue and physicians and officials become classes, and landowners split into several; the manuscript breaks off there, and so does the lesson. The Kerr text has no editorial "breaks off" note; the chapter simply ends at "fisheries."

---

## §D The lab kit: `capkit`

### D.0 Conventions

Every convention of `docs/philosophy/PLAN.md` §D.0 applies unchanged: exact
arithmetic on `algebra_core.RATIONAL_JS`; per-mode script assembly; presets as
lesson data with `expect`; one preset menu (`<select id="XXPreset">`) whose
handler rewrites only instance inputs; redraw-only selects shipped from a named
cfg key; build-time `ValueError` naming the preset on a malformed instance; the
hostile-input sweep; tiles as `<strong id>` written by `textContent`; a status
banner (`XXStatus`) in the Subject's voice; a `mathcheck.js` case per pure
function, seen to fail; printed, specific refusals.

Additions for this Subject:

- **Files.** `scripts/mathpath/labs/capkit.py` (modes `value`, `form`, `money`,
  `circuit`, `surplus`, `workday`, `machine`, `wages`, `accumulate`) and
  `scripts/mathpath/labs/capkit_b.py` (`turnover`, `schemes`, `profit`, `prices`,
  `tendency`, `interest`, `rent`, `revenue`), split as `dekit`/`dekit_b` are.
  One registry key, `"capkit"`, whose entry `capkit_lab(cfg)` dispatches on
  `cfg["mode"]` to either module and raises on an unknown mode or view.
- **Views.** Most modes have several `view`s (listed below). A view is chosen by
  the lesson (`cfg["view"]`), not by the reader: it fixes which inputs and tiles
  the page shows. In this kit `view` is never a control, which is the opposite
  of its use in `argkit`. An unknown view raises.
- **Redraw-only selects** in this kit ship from these cfg keys only: `stage`
  (`form`), `hold` (`workday/three`), `test` (`machine/adopt`: `capitalist` or
  `society`). Each defaults to its first option.
- **Units.** Every mode takes `cfg["money_unit"]` from `{"hours", "s", "£"}`
  and, where it counts things, `cfg["qty_unit"]` (free text: `lb`, `yards`,
  `qr`, `pieces`). Money prints with its unit (`30s`, `£422`, `9/5 h`). For
  `money_unit: "s"` the formatter prints shillings and pence the way Marx does:
  `3s`, `3d`, `1s 6d`, `1½d`, `¾d` (12d to the shilling; halves and quarters as
  ½ and ¼, any other fraction of a penny as `n/m d`), so a sub-shilling amount
  is printed in pence rather than refused. Quantities print with `qty_unit`.
  A tile never converts between money and quantity.
- **Percentages.** A rate prints as the exact fraction and its percentage to
  at most two decimals when it is not whole: `1 = 100%`, `2/3 = 66.67%`,
  `11/50 = 22%` (the fraction is `Rtext`'s output). Marx's `66⅔%` is quoted in prose, never produced by a tile.
- **Periods.** Modes that iterate (`accumulate`, `schemes`, `tendency`) take a
  shipped `periods` (1–10) and print one row per period in a table
  (`XXTable`), plus the pinned tiles for the last period. More than 10 periods
  is refused. `interest/compound`'s `years` is a closed-form parameter, not an
  iteration, and the limit does not apply to it.
- **Tile ids** are unique within the kit. Before freezing them, the kit engineer
  greps `scripts/mathpath/labs/*.py` for each id and records in a comment that
  none collides with an existing kit's module-level JS names.
- **Size limits.** At most 8 producers, 6 commodities, 6 spheres, 6 soils, 10
  capitals, 12 ledger items. Exceeding a limit is refused with the limit named.

### D.1 Modes (capkit.py)

Each entry: cfg instance fields; views; tiles (id: format).

#### value
- Instance: `producers: [{name, hours, output}]` (hours per unit or total, as
  `basis: "per-unit" | "total"`), `skill` (multiplier for complex labour,
  default 1), `lot` (units valued), for view `ledger` `items: [{name, hours,
  output}]`, for view `market` `groups: [{units, hours}]`.
- Views: `snlt` (default), `skill` (shipped `skill = 1` unless a lesson says otherwise), `ledger`, `market`.
- Tiles: `vaSnlt` (`9/5 h` per unit), `vaLotValue` (`lot × snlt`), `vaPerUnit`,
  `vaTotalHours`, `vaMarketValue`, `vaSurplus` (per group, comma-separated in
  input order, signed: `+1 h, 0 h, −1 h`).

#### form
- Instance: `goods: [{name, qty, unit, hours}]`, `equivalent` (a good's name).
- Views: `stage` with shipped `stage` ∈ `elementary | expanded | general |
  money` (a redraw-only select, cfg key `stage`), and `count`.
- Tiles: `foEquation` (the equations of the selected stage, `;`-separated,
  quantities exact), `foGeneral` (the general equivalent's name), `foRelative`
  (how much of the second good the first good's lot now fetches), `foPairs`
  (bilateral ratios needed, n·(n − 1)/2), `foWithEquivalent` (n − 1).
- Build-time check: every equation in `marx` must balance in hours; a preset
  whose quantities do not balance is refused, which is how Marx's figures are
  kept honest.

#### money
- Instance: `goods: [{name, value_hours}]`, `gold_hours_per_unit`, `velocity`,
  `credit_sales`, `payments_due`, `cancelling`, `bills: [{from, to, amount,
  backed}]`, `default` (a bill that is not paid), `issue`, `imports`,
  `exports`, `other_receipts`, `rent`, `price_index`, `wage_index`, `product`,
  `wages`, `reserve`, `fiduciary`, `demand`.
- Views: `circulate`, `payments`, `world`, `fixed-rent`, `bank-act`.
- Tiles: `moPriceSum`, `moNeeded` (the kit's formalisation of ch. 3, §2(b)
  and §3(b): (price sum − credit sales + payments due − cancelling payments) /
  velocity; the banner says it is a formalisation of Marx's sentence, which
  speaks of subtracting the circuits a coin makes), `moUnbacked` (bills with
  no sale behind them),
  `moNetted`, `moDrain` (imports − exports − other receipts, floored at 0, with
  the direction stated), `moRealRent` (rent / price index), `moFarmerGain` (product × price index −
  wages × wage index − rent),
  `moReturned` (issue − needed, floored at 0), `moCap` (fiduciary + reserve),
  `moGap` (demand − cap, floored at 0).

#### circuit
- Instance: `M`, `mp` (means of production), `lp` (labour-power), `product`,
  `sold_share`, `sellers: [{name, value, markup}]`, `subsistence: [{item,
  hours, every_days}]`, `households`, `self_supplied_value`, `pure_costs`,
  `value_adding_costs`, `consumption_advance`.
- Views: `formula`, `markup`, `labour-power`, `stages`, `market`, `costs`,
  `realise`.
- Tiles: `ciForm` (`C–M–C` or `M–C–M′`), `ciDelta`, `ciTotalBefore`,
  `ciTotalAfter`, `ciLpValue` (Σ hours/every_days, per day), `ciMprime`, `ciS`,
  `ciMarket`, `ciSNet` (s − pure costs), `ciReturned`.

#### surplus
- Instance: `materials`, `wear`, `wage`, `hours`, `necessary_hours`, `output`
  (units of product), `workers`, `c`, `v`, `s`, `machine_value`,
  `machine_days`, `waste` (materials used beyond the socially necessary,
  carried at zero value).
- Views: `mill`, `transfer`, `rate` (shows `suRate` and `suParts`), `parts`,
  `senior`, `mass`, `formulae`.
- Tiles: `suProduct` (c + v + s), `suS`, `suRate` (s/v), `suParts` (the product
  in parts: `c: 16 lb, v: 2 lb, s: 2 lb` for Marx's 20 lb of yarn),
  `suLastHour` (the rate after the day is shortened by one hour, with Senior's
  prediction of zero printed beside it),
  `suTransfer`, `suMass` (s′ × v × workers), `suFalse` (s/(v + s)).

#### workday
- Instance: `day`, `necessary`, `productivity` (factor on wage-goods),
  `intensity` (factor), `limit` (legal hours), `pioneer_productivity`,
  `family_workers`, `own_land` (boolean: all hours necessary to the producer),
  `lord_days`, `own_days`.
- Views: `absolute`, `limit`, `relative`, `intensity`, `classify`, `three`
  (with redraw-only `hold`), `separate`, `corvee`.
- Tiles: `wdSurplus`, `wdRate`, `wdExtra` (the pioneer's extra surplus value
  per day), `wdLpValue`, `wdLabour` (hours × intensity), `wdKind`
  (`absolute`, `relative`, `both`, `none`). `separate` also takes `count`
  (households) and multiplies `wdSurplus` by it.
- Draws the day as one bar cut at the necessary time, with the surplus part
  labelled; the bar is SVG in the existing lab chrome, both themes.

#### machine
- Instance: `workers`, `output_each`, `shared_c` (means of production used in
  common), `c_each_if_alone`, `hours`, `steps: [{name,
  rate}]`, `machine_value`, `machine_life_units`, `wages_displaced`,
  `labour_saved_value`, `capital`, `variable`, `wage_each`, `discharged`,
  `machine_spend`, `mb_composition` (machine-building's c/v).
- Views: `cooperate`, `detail`, `adopt`, `displace`.
- Tiles: `maOutput`, `maCPerUnit` (constant capital per unit of output, alone
  and together), `maCombinedDay` (workers × hours delivered in one day),
  `maWorkers` (per step, comma-separated),
  `maMinimum`, `maPerUnit`, `maVerdict` (`adopted`, `not adopted`, under the
  shipped `test`: the capitalist's is machine cost < wages displaced, society's
  is machine labour < labour saved; the tile names the test), `maDisplaced`,
  `maReemployed`. A typed co-operation gain is never an input: the kit computes
  only what follows from shared means of production and simultaneity.

#### wages
- Instance: `lp_value` (daily), `normal_hours`, `hours_worked`,
  `value_per_hour`, `pieces_normal`, `pieces_actual`, `rate_cut_to`, for view
  `national` two countries' `{wage, output_per_hour}`, for view `statute`
  `{statutory_wage, lp_value, day, necessary}`.
- Views: `form`, `time`, `piece`, `national`, `statute`.
- Tiles: `waHourPrice`, `waValueCreated`, `waDaily`, `waPieceRate`,
  `waRelative` (wage per unit of output, country A over country B), `waGap`,
  `waRate` (the rate of surplus value: under the statute in `statute`, for each
  country in `national`).

#### accumulate
- Instance: `capital`, `c_v` (composition), `s_rate`, `accumulate_share`,
  `consumed_per_year`, `composition_rise` (added to c/v per period),
  `labour_supply`, `supply_growth`, `wage_per_worker`, `capitals: [n]`
  (for `centralise`), `merge_rule` (`largest-absorbs-smallest | none`),
  `colonists`, `land_price_years`, `invest_threshold`, `wage`, `saving_share`,
  `target`.
- Views: `simple`, `expand`, `labour`, `composition`, `law` (reserve/employed
  ratio for every period), `centralise`, `colony`, `thrift`.
- Tiles: `acYears` (capital / consumed per year), `acCapital`,
  `acShareOriginal` (original capital as a share of the present capital),
  `acDemand` (workers employed: v / wage), `acReserve` (supply − demand,
  floored at 0), `acRatio` (reserve / employed), `acTopShare`, `acCount`,
  `acYearsToLand`, `acHoard` (money held back below `invest_threshold`),
  `acDaysToTarget` (target / (wage × saving_share), in working days).

### D.2 Modes (capkit_b.py)

#### turnover
- Instance: `working_weeks`, `production_weeks`, `circulation_weeks`,
  `weekly_outlay`, `stage_weeks: [money, productive, commodity]`, `fixed:
  [{name, value, life_years}]`, `circulating`, `circ_turnovers`, `variable`,
  `s_rate`, `items: [{name, value, fixed: bool, variable: bool}]`,
  `merchant_capital`, `merchant_turnovers`, `year_weeks` (default 52; Marx's
  Volume II figures use 50, and every preset with Marx's figures sets it), and
  per fixed item `repairs_per_year`, `replacement_value`, `appears_year`.
- Views: `time`, `phases`, `fixed`, `aggregate`, `classify`, `working`,
  `advance`, `annual`, `merchant`.
- Tiles: `tuTurnover` (weeks), `tuTurnovers` (year_weeks / turnover weeks,
  exact, with the year length printed), `tuCirculationShare`,
  `tuWorkingShare`, `tuMoney`, `tuProductive`, `tuCommodity` (shares), `tuWear`,
  `tuRemaining`, `tuAggregate`, `tuAverage`, `tuFixed`, `tuVariable` (sums by
  each classification), `tuS` (s at `s_rate` on the variable items),
  `tuAdvance`, `tuFreed`, `tuAnnualRate` (s′·n),
  `tuMassS`.

#### schemes
- Instance: `I: {c, v, s}`, `II: {c, v, s}`, `I_accumulate_share`,
  `composition_I`, `composition_II`, `products: [{name, use: "production" |
  "consumption"}]`, `wear_set_aside`, `renewals`, `hoarders_share`.
- Views: `sort`, `simple`, `fixed`, `hoard`, `expanded` (shipped `periods`).
- Rule for `expanded`: Marx's first example — Department I accumulates the
  stated share of s at its own composition; Department II accumulates exactly
  what balances I(v + Δv + s/k) = II(c + Δc), at its own composition. The
  status banner states the rule. If balance requires Department II to
  accumulate more than its s, the period is refused and the banner says so.
- `simple` also prints `scWithinI` (Ic: means of production exchanged within
  Department I, never anyone's revenue).
- `fixed`: `scFixedGap` is signed and names the short side: renewals below the
  hoarded wear leave Department I's product unsold; renewals above it leave
  Department I short.
- Tiles: `scDeptI`, `scDeptII`, `scBalance` (`I(v + s) = 2,000 = IIc` or the
  signed gap), `scIExchange`, `scFixedGap`, `scHoardGap`, `scYear2` (both
  departments after the first period, in Marx's notation:
  `I 4,400c + 1,100v; II 1,600c + 800v`), `scGrowth` (growth of total product
  over the periods, exact).

#### profit
- Instance: `c`, `v`, `s`, `sale_price`, `turnovers`, `c_change`,
  `price_passed_on` (share).
- Views: `cost`, `rate`, `relation`, `turnover`, `economy`, `price`, `books`.
- Tiles: `prCost` (c + v), `prProfit`, `prRate` (s/(c + v)), `prSRate`,
  `prAnnual`.

#### prices
- Instance: `spheres: [{name, c, v, c_used}]`, `s_rate`, `wage_rise`,
  `merchant_capital`, `merchant_costs`, `merchant_turnovers`,
  `premiums: [{sphere, rate}]`.
- Views: `rates`, `production`, `wage-rise`, `merchant`, `merchant-turnover`.
- Tiles: `ppRates` (each sphere's rate, comma-separated in input order),
  `ppAverage`, `ppPrices` (each sphere's price of production, comma-separated),
  `ppTotals` (`values 422 = prices 422; s 110 = profit 110`), `ppMerchantPrice`
  (`industrial 1,062; merchant 1,080`), `ppMarkup`.
- The wage-rise rule is stated in the banner: the money wage rises by the
  stated share, the extra wages come out of surplus value, and the new average
  rate is recomputed over the capital advanced after the rise (Marx: 15 on 105
  is 14 2/7%). The lesson checks the
  resulting directions against Marx's text before pinning.

#### tendency
- Instance: `c`, `v`, `s_rate`, `c_step`, `capital_growth`, `s_rate_step`,
  `c_cheapening`, `added_capital`, `devalued_share`.
- Views: `law`, `counter`, `overaccumulation`.
- Tiles: `teRate`, `teMass`, `teOffset` (percentage points of the fall
  offset), all for the last period, with the table.

#### interest
- Instance: `capital`, `profit_rate`, `interest_rate`, `manager_salary`,
  `income`, `years`, `principal`, `real_growth`, `surplus`, `debt`,
  `holding_value`.
- Views: `split`, `bounds`, `capitalise`, `compound`, `usury`. (A `cycle` view
  taking deposits and investment by phase was removed at review: it echoed
  typed narratives, which D.3 forbids. Volume III, Chapters 30–32 use
  `schemes/hoard`, `turnover/advance` and `money/payments`.)
- Tiles: `inInterest`, `inEnterprise`, `inBound` (`0 < i < p′` with the
  values, or `breached` with the values: not an error), `inPrice` (income /
  rate), `inCompound`, `inReal`, `inYearsToRuin` (first year debt > holding,
  or `never within n years`). `usury` compounds unpaid interest and states the
  rule in the banner.
- `compound` prints its sum with BigInt numerators and, beside the exact value,
  the number of decimal digits — a penny at 5% for 1,780 years is not a number
  to print in full.

#### rent
- Instance: `soils: [{name, capital, outputs: [qr per investment]}]`,
  `profit_rate`, `price_case` (`constant | falling | rising | worst-soil`; the
  only name for this key),
  `regulating` (which investment regulates, or `auto` = least productive in
  use), `rent`, `interest_rate`, `improvement_interest`, `cost_steam`,
  `cost_water`, `agri: {c, v}`, `s_rate`, `market_limit`.
- Views: `price`, `waterfall`, `dr1`, `dr2`, `absolute`.
- Tiles: `rtPrice` (land price or regulating price, by view), `rtTrueRent`,
  `rtSurplusProfit` (in `waterfall`, both of Marx's measures:
  `10 against the steam user's profit; 11½ against its own price of production`), `rtRents` (per soil, in input order), `rtTotal`,
  `rtAbsolute`.

#### revenue
- Instance: `c`, `v`, `s`, `split: {interest, rent}` (shares of s),
  `wage_change`, `people: [{name, wages, profit, rent}]`.
- Views: `trinity`, `dogma`, `added-up`, `classes`.
- Tiles: `rvTotal` (c + v + s), `rvSmith` (v + s, the dogma's total, with the
  missing c), `rvWages`, `rvRent`, `rvInterest`, `rvProfitShare` (profit of
  enterprise), `rvClassCount` (the number of groups when people are grouped
  by source of revenue at the preset's fineness: the count grows as sources
  are split, which is the chapter's objection).

### D.3 What the kit must never do

- **Decide a question the book argues.** No tile says "exploitation",
  "unfair" or "crisis". A tile states a quantity; a banner states what was
  computed and from what; the lesson's prose does the arguing.
- **Simulate history.** Historical presets are mechanisms with stated
  quantities, not reconstructions. A preset label never claims a historical
  figure the lesson has not quoted from the text.
- **Solve the transformation problem.** `prices` transforms values into prices
  of production the way Volume III, Chapter 9 does — inputs at value — and the
  lesson on that chapter says so, names the later controversy (Bortkiewicz and
  after) in one paragraph, and does not compute an iterative solution.

---

## §E Package layout, the author's checklist, and how a passage is quoted

### E.1 Layout

```
content/capital/
  __init__.py                       PATH, COURSES (filter COURSE = None), numbering loop
  c01_commodities/__init__.py       COURSE dict; lessons = part_a.LESSONS (+ part_b)
  c01_commodities/part_a.py         LESSONS = [...]
  c02_surplus_value/ … c14_revenues/  same shape; split a course over 6 lessons at its midpoint
content/spoken/capital.py           SPOKEN = {run: words}   starts empty
```

Mirror `content/philosophy/__init__.py` for the package and
`content/philosophy/c1_arguments/__init__.py` for a course. Course and lesson
fields are exactly those of `docs/philosophy/PLAN.md` §E — same table, same
ranges, same enforcement. Nothing about the page shape changes.

### E.2 Per-lesson procedure

As in `docs/philosophy/PLAN.md` §E, with two additions:

1. Before writing, fetch the chapter (§E.3) and read the whole of it, not only
   the passage. A lesson that explains a chapter its author has not read is
   the most likely way this Subject goes wrong.
2. Every "Marx's figures" preset is checked against the fetched text before it
   is written. If the text differs from §C, the text wins and §C is corrected
   in the same commit.

### E.3 Quoting the passage

- **Sources: the Kerr editions, and nothing else.** Volume I: the Moore–Aveling
  translation as revised and amplified by Ernest Untermann from the fourth German
  edition (Chicago: Charles H. Kerr, 1906/1909). Volume II: Untermann's
  translation (Kerr, 1907). Volume III: Untermann's translation (Kerr, 1909).
  All three are in the public domain. Plain-text copies extracted from the Online
  Library of Liberty ePubs are in the project's shared folder at
  `/mnt/project-files/capital-texts/volume-{1,2,3}-kerr.txt`, with a README
  giving the OLL source URLs (titles 965, 966, 967).
- **Never quote** the marxists.org HTML of Volumes II and III (the Lasker 1956
  and Progress 1959 translations, in which rights are asserted) or the Fowkes and
  Fernbach Penguin translations (in copyright). The marxists.org Volume I HTML is
  the 1887 Moore–Aveling text and is public domain, but it differs from the
  Kerr revision in places (Peel's "300" against "3000"); quote the Kerr text so
  the Subject has one source.
- **Quote by search, not from memory.** `grep -n` the Kerr text for the
  passage, copy it character for character, keep it under 120 words, and record
  the line number in a comment beside the lesson dict. The Kerr wording of a
  chapter or section title is the title the `module` name uses.
- **Shape.** The first `body` block is a `p`:
  `<strong>Volume I, Chapter 1, §1.</strong> &ldquo;…&rdquo;` — volume,
  chapter and section, then the quotation, nothing else. A second short
  quotation may appear later in the body the same way.
- **Attribution.** The path's `prerequisites` name the editions; each course's
  `how_to` carries OLL's attribution line once: "Quotations are from the
  Kerr editions in the Online Library of Liberty, hosted by Liberty Fund, Inc."
- **Translator's spellings stand** inside quotation marks; the lesson's own
  prose uses the Subject's spellings (British; "labour-power"; "surplus value"
  unhyphenated as a noun).
- **Engels.** Volumes II and III are Engels' edition of Marx's manuscripts, and
  Volume III, Chapter 4 is Engels' own text; the lessons that lean on that say
  so once.

---

## §F Voice: the read-along, after the three lectures

The operator asked for this Subject to take its tone from three lectures he
recorded in May 2026: a Spanish-language series reading the *Tao Te Ching* one
chapter at a time. They are the model for how a lesson moves, not for what it
says, and they are in another language: the aim is the same manner in natural
English, not a translation of their phrases. "Do not force it" is the brief,
and it is the first rule below.

What the lectures do, and what that means here:

1. **They read the text first, whole, then go back through it line by line.**
   ("It's a poem; it wouldn't be right to interrupt it at every verse. So
   first I'll read it complete, and then we'll go verse by verse.") Here: the
   passage opens the body; the body then returns to its phrases in order,
   quoting a few words at a time and saying what each does.
2. **They open with the reader's own world, not with the definition.** The
   chapter on non-duality starts with the minute that is short when you hit
   snooze and endless when you hold a plank. Here: open with a scene only where
   the chapter's object is already in the reader's life — wages, rent, prices,
   interest, debt, a mortgage — and reach the chapter's category within the
   paragraph. The Volume II turnover lessons, the reproduction schemes and the
   Bank Act lessons open with the passage's own figures instead. A scene that
   has to be invented is a forced one; leave it out.
3. **They tell the history of an idea as a story with people in it.** Thales
   sees water everywhere; Laplace tells Napoleon he had no need of that
   hypothesis. Here: when Marx argues with Smith, Ricardo, Senior or Say, the
   lesson tells who they were and what they claimed in two or three sentences,
   at full strength, before Marx answers. Senior's "last hour" is a scene: a
   professor travels to Manchester to be taught that profit comes from the
   final hour of the day.
4. **They talk to "you", warmly and directly.** "Consider…", "Think about…",
   "You know this one." Here: second person is allowed and encouraged in
   `p` blocks and `worked.intro`; never in `steps`, `standard`, quiz items or
   tile text, which stay exact and impersonal.
5. **They are funny in passing, and never at the reader's expense.** A dry
   aside about Laplace's arrogance, the "hipster monkeys" who didn't like honey.
   Here: at most one light remark per lesson, and only where Marx himself is
   being sardonic (he very often is: "Moses and the prophets", the capitalist
   who "stares in astonishment"). Point at Marx's own jokes before making new
   ones.
6. **They admit the limit of what can be said.** The lectures end by
   confessing that the words are "a finger pointing at the moon". Here: every
   lesson's `note` names the one assumption or limit that lesson leans on — the
   illustrative figures are illustrative, a disputed reading is disputed, the
   lab sees quantities and not meanings. "Commodities sell at their values" is
   said only in the lessons that lean on it (“The Labour Process and the
   Production of Surplus Value”, “The Rate of Surplus Value”, “Cost Price and
   Profit”, the two lessons opening Average Profit and Its Fall), not sixty
   times.
7. **They close by pointing forward.** Each lecture ends with what next week
   is about. Here: the last `p` of the body names the question the next
   chapter answers, in one sentence and by the next lesson's title. The last
   lesson of a course points to the next course by title. “Classes” ends where
   the manuscript does. It never says "next week" and never summarises the
   lesson.

What does not carry over:

- **No slang, no profanity, no regional idiom.** The lectures' register is
  colloquial Mexican Spanish; its English equivalent would sound forced. Warm
  and plain is the target.
- **No personal anecdotes in the first person.** The lectures' "when I lived
  in the forest" belongs to their author. A lesson may use an everyday
  second-person scene instead.
- **No claims the lectures can make and a lesson cannot.** Neuroscience asides,
  cosmology and the like are out unless the chapter is about them.

Every correctness rule of `docs/philosophy/PLAN.md` §F stands: say what is
computed and from what; name the act, not the understanding; one hard idea per
lesson; name the misconception as a model someone holds and refute it with a
number; state positions at their strongest — Marx's and his opponents'; state
the lab's limit where the lesson leans on it; math a voice can read; quiz
questions test the idea; no filler. What is relaxed is register: "Let's" is
still out, but "you" is in, one rhetorical question may open a paragraph, and a
sentence may be short for effect.

**Marx is presented, not endorsed.** A lesson explains what the chapter
argues, does the chapter's arithmetic, and states the strongest objection where
there is a standard one (the transformation problem, the falling rate's
empirical record, the labour theory of value against marginal utility). It
never tells the reader what to conclude about capitalism. The lectures take
sides on the *Tao Te Ching*; this Subject does not take sides on *Capital*.

**One exemplary paragraph** (a `p` block for “The Labour Process and the
Production of Surplus Value”, after the passage):

> Think about the last thing you bought that was made in a factory. Its price
> had to cover the materials, the wear on the machines and the wages, and you
> would expect it to cover them exactly if nobody cheated. That is the puzzle
> Marx sets up with his spinner. Ten pounds of cotton at 10s, 2s of wear on the
> spindle, six hours of spinning: the yarn is worth 15s, and the capitalist who
> paid 3s for a day's labour-power and 12s for the rest has made nothing. He
> "stares in astonishment", Marx writes, and starts to talk about his
> abstinence. Then the day is lengthened to twelve hours. The lab does the same
> sum twice: 27s goes in, yarn worth 30s comes out, and on the chapter's
> accounting every input was bought at its value. On Marx's definitions the 3s
> is the difference between what a day of labour-power costs and what a day of
> labour adds — which is exactly the step an economist who prices labour by its
> marginal product would refuse, and the next lessons keep that refusal in
> view.

---

## §G What is left out, and why

- **The *Grundrisse*, *Theories of Surplus Value*, the 1861–63 manuscripts and
  the "Results of the Immediate Process of Production".** The Subject reads
  *Capital* as published; where Volumes II and III are Engels' edit of Marx's
  manuscripts the lesson says so once, in the course's `how_to`.
- **The transformation problem's solutions** (Bortkiewicz, Sraffa, the "New
  Interpretation", temporal single-system). Named in the Chapter 9 lesson's
  `note` and in its course's `not_covered`. Computing one would take a side in
  a live dispute.
- **Empirical tests of the falling rate of profit, of the reserve army, of
  immiseration.** Data is not computed here; the lessons say the law is stated
  as a tendency and that whether it holds is argued with data this path does
  not carry.
- **Marx's biography, the reception of *Capital*, later Marxisms.** Not a
  history of Marxism. Engels' role as editor is named where it matters.
- **Exact historical figures beyond those Marx quotes.** Presets on historical
  chapters are mechanisms with illustrative quantities, and say so.
- **History told as story.** Philosophy's §G excludes the history of
  philosophy; this Subject tells the history of the argument (Smith, Ricardo,
  Senior, Say, Overstone) because the book is that argument. Both choices are
  deliberate; neither is a defect for a later reviewer to "fix".
- **Exchange within Department II between necessities and luxuries** (Volume
  II, Chapter 20, §4): named in Reproduction of the Social Capital's
  `not_covered`.
- **Modern monetary systems.** Volume III's money chapters are read as about
  gold-backed banking in the 1840s–60s; a lesson may say in one sentence what
  is different now, and does not model fiat money.

---

## §H Wiring notes for the orchestrator

As `docs/philosophy/PLAN.md` §H, with these values:

- Package `capital`; path slug `capital`; check-id prefix `cap`. Check ids
  take the form `cap-course12-lesson-<lesson-slug>`, so a lesson slug may be at
  most 52 characters under the 72-character cap; every slug in §C is at most
  46, inside the 48 the lesson table allows.
- `CAP_DISCLAIMER_RE = r"only as good as the definitions"`.
- `content/spoken/capital.py`; `capital_semantic_copy` in `test_public_copy`.
- Register `capital` in `GENERATED_PATHS` at the start of the branch with every
  `COURSE = None`; add `"capkit"` to `KITS_WITH_EXPECTATIONS` last.
- Ten Subjects after wiring; every "nine Subjects" count in the repository
  (AGENTS.md §0 and §1, README, `site/index.html`, tests) is updated in the
  wiring commit.
- `site/index.html` gets a subject card and one search entry per course.

---

## §R Review record

The process that produced the last four Subjects: an advisor pass on the
curriculum spine, a reconciliation pass against every existing path, and this
specification. For this Subject the reviews are run by two different models
(see the operator's instruction), each independently, before any lesson is
authored, and again per course after authoring. Each review's findings and the
resolution of each are appended here.

### Pre-authoring review, 2026-10-24

Two independent reviews of the first draft, each by a different model, neither
seeing the other's findings:

- **Fable (pedagogical-expert role)**: instructional design and reconciliation
  with the library. 35 findings; the full text was kept in the session
  scratchpad. Two were blocking: mode names corrupted by a prefix rename
  (`rtnt`, `rvvenue`) and a description sentence ("one lesson for every
  chapter") that the counts test would read as "1 lesson".
- **Opus (independent scholarly review)**: accuracy against the text of
  *Capital*, checked chapter by chapter. 42 findings, including that the
  marxists.org Volume II and III pages are not Untermann's translation.

Resolutions, by theme:

1. **Corrupted names and counting sentence**: fixed.
2. **Source text**: the Subject quotes only the Kerr editions, now held
   locally (§E.3). Read lines in §C are pointers, never quotations.
3. **German numbering**: corrected (it differs from Chapter 4 on, not only in
   Part Eight).
4. **Figures**: every figure the Opus review found wrong or not Marx's was
   corrected or relabelled illustrative: the 50-week year (`year_weeks`), Vol III
   ch. 6, 13 and 15, Vol I ch. 21, 22, 24 and 32, Vol II ch. 9 and 20 §11, Vol III
   ch. 8, 11, 18, 36, 38 and 45, the 16 lb of `suParts`. Peel stays at 3,000 because
   that is the Kerr text; the 1887 reading of 300 is noted.
5. **Misconceptions**: rewritten wherever they were historical or political
   judgments, the reverse of Marx's claim, or a live dispute presented as an
   error (Factory Acts, enclosure, the capitalist farmer, centralisation,
   merchant's capital, ground rent's genesis, the quantity theory, Luxemburg,
   Say's law, the Currency School, Okishio). Register rule added to §C.
6. **Decorative labs**: co-operation recomputed from shared means of
   production; the `interest/cycle` view removed and Chapters 30–32 moved to
   mechanisms; the form of value and the home market given a moving quantity.
7. **Cognitive load**: Senior's last hour split into its own lesson (119
   lessons); the family wage dropped from the intensity lesson; skilled labour
   moved to prose.
8. **Duplicates**: Chapter 49 now computes Ic within Department I instead of
   repeating Chapter 19's lab; Ricardo's chapter computes s from wage bills;
   Chapter 5 no longer pre-empts Chapter 13.
9. **Presented, not endorsed**: the exemplary paragraph and the trinity, profit
   of enterprise, stock company and general-law entries now attribute
   conclusions to the chapter's accounting and name the opposing account.
10. **Voice**: scenes only where the chapter's object is in the reader's life;
    course-end and “Classes” exceptions to the forward pointer; the
    sell-at-value note confined to the lessons that need it.

Not adopted: Fable's suggestion to give every bare preset an instance in this
document now. Instead §C states that a bare id is a placeholder the author must
instantiate and record here in the same commit, and the per-course review
rejects any that remain.
