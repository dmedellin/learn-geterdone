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
- §C Every lesson: 118 entries
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

> Karl Marx's *Capital*, read chapter by chapter, all three volumes &mdash; with
> the arithmetic Marx does on the page done in front of you: value and money,
> the working day, surplus value, wages, accumulation, turnover, reproduction,
> profit, prices of production, interest and rent. Fourteen courses and 118
> lessons are available.

**description**:

> The Capital Subject: a read-along of all three volumes in Marx's own order,
> fourteen courses that follow his Parts, one lesson for every chapter and more
> for the long ones. Each lesson reads a passage first, then explains it, then
> computes what the chapter computes &mdash; a commodity's value, a rate of
> surplus value, a reproduction scheme that balances or does not, a price of
> production, a rent schedule &mdash; in exact arithmetic in your browser. All
> fourteen courses and 118 lessons are available.

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
   passage it reads from the public-domain English translations (Moore and
   Aveling for Volume I, Untermann for Volumes II and III), which are free
   online. Chapter numbers follow the English edition of Volume I; where the
   German numbering differs, the lesson says so.
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
> are from the public-domain English translations. What the labs cannot do is
> tell you whether Marx's definitions are the right ones &mdash; and that is
> what the book is arguing about.

---

## §B The fourteen courses

Volumes and Parts are Marx's. Courses group short Parts and never split one,
except Volume III's Part Five, which is sixteen chapters long and divides where
Marx's own manuscript changes subject (from interest to the credit system).

| # | slug | title | Marx | lessons |
| --- | --- | --- | --- | --- |
| 1 | `capital-commodities-and-money` | Commodities and Money | Vol I, Part I (ch. 1–3) | 8 |
| 2 | `capital-money-into-surplus-value` | From Money to Surplus Value | Vol I, Parts II–III (ch. 4–11) | 9 |
| 3 | `capital-relative-surplus-value` | Relative Surplus Value | Vol I, Parts IV–V (ch. 12–18) | 9 |
| 4 | `capital-wages-and-accumulation` | Wages and Accumulation | Vol I, Parts VI–VII (ch. 19–25) | 9 |
| 5 | `capital-primitive-accumulation` | So-Called Primitive Accumulation | Vol I, Part VIII (ch. 26–33) | 8 |
| 6 | `capital-circuits-of-capital` | The Circuits of Capital | Vol II, Part I (ch. 1–6) | 6 |
| 7 | `capital-turnover-of-capital` | The Turnover of Capital | Vol II, Part II (ch. 7–17) | 11 |
| 8 | `capital-social-reproduction` | Reproduction of the Social Capital | Vol II, Part III (ch. 18–21) | 6 |
| 9 | `capital-cost-price-and-profit` | Cost Price and the Rate of Profit | Vol III, Part I (ch. 1–7) | 7 |
| 10 | `capital-prices-of-production` | Average Profit and Its Fall | Vol III, Parts II–III (ch. 8–15) | 8 |
| 11 | `capital-merchants-and-interest` | Merchant's Capital and Interest | Vol III, Parts IV–V (ch. 16–24) | 9 |
| 12 | `capital-credit-and-fictitious-capital` | Credit and Fictitious Capital | Vol III, Part V (ch. 25–36) | 12 |
| 13 | `capital-ground-rent` | Ground Rent | Vol III, Part VI (ch. 37–47) | 11 |
| 14 | `capital-revenues-and-their-sources` | Revenues and Their Sources | Vol III, Part VII (ch. 48–52) | 5 |

Total 118. The `capital-` prefix keeps course slugs from colliding with the
generic names other Subjects already use and tells a reader landing on a course
URL which book it belongs to.

Each course's `module` names are the book's chapters: `Chapter 1 · Commodities`.
A course's `summary` names the Part; its `assumes_long` names earlier courses by
title. Course `key` lines are drawn from that course's own formulas.

Chapter splits (one hard idea per lesson): Volume I Chapter 1 (four lessons,
one per section), Chapter 3 (three), Chapter 10 (two), Chapter 15 (three),
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

Preset ids are suggestions; the INSTANCES are not optional. Tile ids are fixed by
§D. Expected strings are read off the built page with `node scripts/labcheck.js
--observe`, never predicted. "Marx's figures" means the instance is the one in
the chapter and the label says so ("Marx's spinning mill: 10 lb cotton").

### Course 1 — Commodities and Money (`capital-commodities-and-money`, 8)

1. **the-two-factors-of-a-commodity** — The Two Factors of a Commodity — *Chapter 1 · Commodities*
   - Read: §1, the opening sentence ("The wealth of those societies…") and the paragraph on "a common something" in exchange.
   - Do: given several producers' hours and outputs, compute the socially necessary labour-time per unit and the value of a lot, and say why the slow producer's extra hours add nothing.
   - Lab: `value`. Presets: `linen` (three weavers, 1 h, 2 h, 3 h per yard, outputs 40, 40, 20 yards), `steam` (the power-loom: the same weavers after productivity doubles for the two largest), `lazy` (one weaver at 5 h per yard, output 1 yard). Pin `vaSnlt`, `vaLotValue`.
   - Misconception: a commodity made more slowly is worth more.
   - Worked: 100 yards made in 180 hours in all is 9/5 hour a yard; the weaver who needed 3 hours a yard sells at 9/5 like everyone else.

2. **the-twofold-character-of-labour** — The Twofold Character of Labour — *Chapter 1 · Commodities*
   - Read: §2, "the two-fold nature of the labour contained in commodities… is the pivot on which a clear comprehension of Political Economy turns".
   - Do: separate concrete (useful) labour from abstract labour in a coat and in linen, and reduce skilled labour to simple labour with a stated multiplier.
   - Lab: `value`, view `skill`. Presets: `coat-linen` (tailor 10 h, weaver 10 h, multiplier 1), `skilled` (tailor's hour counts as 2 simple hours), `doubled` (productivity doubles: twice the coats, same value in total). Pin `vaLotValue`, `vaPerUnit`.
   - Misconception: more useful things always means more value.
   - Worked: double the productivity of tailoring and two coats now carry the value one did; the use-values doubled, the value did not.

3. **the-form-of-value** — The Form of Value — *Chapter 1 · Commodities*
   - Read: §3, "20 yards of linen = 1 coat, or: 20 yards of linen are worth 1 coat".
   - Do: write the elementary, expanded, general and money forms for a set of commodities from their labour-values, and say which side is the relative form and which the equivalent.
   - Lab: `form`. Presets: `marx` (Marx's figures: 20 yards linen = 1 coat = 10 lb tea = 40 lb coffee = 1 quarter corn = 2 oz gold = ½ ton iron, values stated in hours so the equations hold), `two` (linen and coat only), `gold` (the same with gold as equivalent). Shipped `stage = elementary`. Pin `foEquation`, `foGeneral`.
   - Misconception: in "20 yards of linen = 1 coat" the coat's value is what is being expressed.
   - Worked: from 20 yards = 1 coat to "1 coat = 2 oz gold" every equation is one labour-time on both sides; the money-form only picks one commodity to stand on the right.

4. **the-fetishism-of-commodities** — The Fetishism of Commodities — *Chapter 1 · Commodities*
   - Read: §4, "A commodity appears, at first sight, a very trivial thing…" and Robinson Crusoe's ledger.
   - Do: read Robinson's ledger and the "association of free men" as the same labour-time accounting done openly, and say what the price tag hides that the ledger shows.
   - Lab: `value`, view `ledger`. Presets: `robinson` (Robinson's week: hours on goats, fishing, furniture; products), `village` (four households trade by the same hours, prices shown), `association` (the same output allocated by hours contributed). Pin `vaTotalHours`, `vaPerUnit`.
   - Misconception: value is a physical property of the thing, like weight.
   - Worked: Robinson's table and the market's prices give the same ratios; only one of them tells you whose hours they were.

5. **exchange** — Exchange — *Chapter 2 · Exchange*
   - Read: "It is plain that commodities cannot go to market and make exchanges of their own account."
   - Do: show why direct barter among many owners needs a common equivalent, by counting the bilateral ratios with and without one.
   - Lab: `form`, view `count`. Presets: `four` (four commodities), `six` (six), `six-gold` (six, one chosen as equivalent). Pin `foPairs`, `foWithEquivalent`.
   - Misconception: money was invented by agreement because it was convenient.
   - Worked: six owners need fifteen ratios to trade by barter and five once one commodity is everyone's equivalent.

6. **money-as-measure-and-means-of-circulation** — Money as Measure and Means of Circulation — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §1 on price as "the money-name of the labour realised in a commodity"; §2(b) on the quantity of money in circulation.
   - Do: compute prices from values and gold's value, and the money needed to circulate a day's sales at a given velocity; then change the value of gold and see prices move without any commodity changing.
   - Lab: `money`, view `circulate`. Presets: `marx` (Marx's figures: 1 quarter wheat, 20 yards linen, a bible, 4 gallons brandy at £2 each, velocity 4 when they change hands in sequence), `gold-falls` (gold's value halves), `faster` (velocity 8). Pin `moNeeded`, `moPriceSum`.
   - Misconception: prices rise because there is more money (the quantity theory Marx is arguing against).
   - Worked: four commodities at £2 each, sold one after another by the same two sovereigns' worth of coin: price sum £8, velocity 4, money needed £2.

7. **hoards-means-of-payment-and-world-money** — Hoards, Means of Payment and World Money — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §3(b), the law of the quantity of money once payments fall due.
   - Do: compute money needed with credit sales and mutually cancelling payments, and say why a chain of debts makes a crisis a money crisis.
   - Lab: `money`, view `payments`. Presets: `cash` (no credit), `chain` (A owes B owes C owes A, equal sums), `broken` (the same chain with one default). Pin `moNeeded`, `moNetted`.
   - Misconception: money only matters as a medium of exchange.
   - Worked: £300 of debts in a circle cancel to £0 in cash; break one link and £100 is suddenly needed in hard money.

8. **commodities-and-money-in-review** — Commodities and Money in Review — *Chapter 3 · Money, or the Circulation of Commodities*
   - Read: §3(c), "When money leaves the home sphere of circulation, it strips off the local garbs…".
   - Do: settle a trade balance in gold between two countries and connect it back to value, the forms of value and price.
   - Lab: `money`, view `world`. Presets: `balanced`, `deficit` (one side imports more), `drain` (deficit plus a payment due). Pin `moDrain`.
   - Misconception: world money is just a currency exchanged at a rate.
   - Worked: imports of £1,000 against exports of £800 leave £200 to be shipped in bullion, the "universal means of payment".

### Course 2 — From Money to Surplus Value (`capital-money-into-surplus-value`, 9)

1. **the-general-formula-for-capital** — The General Formula for Capital — *Chapter 4*
   - Read: "The simple circulation of commodities – selling in order to buy – is a means of carrying out a purpose unconnected with circulation…".
   - Do: tell C–M–C from M–C–M′ by what is at either end, and compute the increment ΔM for given purchases and sales.
   - Lab: `circuit`, view `formula`. Presets: `cmc` (sell linen £3, buy bible £3), `mcm` (£100 cotton sold for £110), `mcm-loss` (sold for £90). Pin `ciDelta`, `ciForm`.
   - Misconception: M–C–M is pointless unless it ends with more money, so all trade is M–C–M′.
   - Worked: £100 → cotton → £110: the circuit only makes sense because of the £10.

2. **contradictions-in-the-general-formula** — Contradictions in the General Formula — *Chapter 5*
   - Read: "Capital cannot therefore arise from circulation, and it is equally impossible for it to arise apart from circulation."
   - Do: show that if every seller marks up by the same percentage the total value in hands does not change, and that one cheat's gain is another's loss.
   - Lab: `circuit`, view `markup`. Presets: `ten` (every seller 10% above value), `one-cheat` (A cheats B by £10), `merchants` (three dealers, each adds 10%). Pin `ciTotalBefore`, `ciTotalAfter`.
   - Misconception: profit comes from selling above value.
   - Worked: A sells wine worth £40 to B for £50; the total value held by A and B is £90 before and after.

3. **buying-and-selling-labour-power** — The Buying and Selling of Labour-Power — *Chapter 6*
   - Read: the "doubly free" labourer, and the departure from "this noisy sphere… a very Eden of the innate rights of man".
   - Do: compute the daily value of labour-power from the value of a worker's means of subsistence, including weekly, yearly and generational items.
   - Lab: `circuit`, view `labour-power`. Presets: `daily` (food daily, clothes weekly, furniture yearly), `family` (add children's upkeep), `training` (add a training cost spread over a working life). Pin `ciLpValue`.
   - Misconception: the worker sells labour; the capitalist buys hours of work done.
   - Worked: 6 hours of daily needs + 7 hours a week of clothes + 365 hours a year of rent is 6 + 1 + 1 = 8 hours a day.

4. **the-labour-process-and-valorisation** — The Labour Process and the Valorisation Process — *Chapter 7*
   - Read: §2, Marx's spinning mill, "Our capitalist stares in astonishment."
   - Do: compute the value of the yarn from cotton, spindle wear and labour, first for 6 hours and then for 12, and locate where the surplus value comes from.
   - Lab: `surplus`, view `mill`. Presets: `six` (Marx's figures: 10 lb cotton 10s, spindle wear 2s, labour-power 3s a day, 6 hours spinning, 6 hours of labour = 3s), `twelve` (the same day lengthened to 12 hours: 20 lb cotton 20s, wear 4s, 12 hours = 6s), `waste` (12 hours with careless use of cotton beyond the socially necessary). Pin `suProduct`, `suS`.
   - Misconception: the surplus is the machine's contribution.
   - Worked: 27s advanced, yarn worth 30s: 20 + 4 for means of production carried over, 6 of new value against 3 paid.

5. **constant-capital-and-variable-capital** — Constant Capital and Variable Capital — *Chapter 8*
   - Read: "That part of capital, then, which is represented by the means of production… does not, in the process of production, undergo any quantitative alteration of value."
   - Do: classify the parts of a capital as c or v and compute the value a machine transfers per day from its value and life.
   - Lab: `surplus`, view `transfer`. Presets: `machine` (£1,000 machine, 1,000 days), `raw` (raw material consumed whole), `price-rise` (cotton's price doubles after purchase). Pin `suTransfer`, `suProduct`.
   - Misconception: constant capital is fixed capital.
   - Worked: a £1,000 machine with a 1,000-day life passes £1 a day into the product, however much the product is.

6. **the-rate-of-surplus-value** — The Rate of Surplus Value — *Chapter 9*
   - Read: §1, s/v "is therefore an exact expression for the degree of exploitation of labour-power by capital".
   - Do: compute s/v and the product's value in parts, and do Senior's "last hour" arithmetic to show where it goes wrong.
   - Lab: `surplus`, view `rate`. Presets: `marx` (Marx's figures: c = £410, v = £90, s = £90), `parts` (the product in parts: 20 lb yarn shown as cotton, wear, necessary and surplus pounds), `senior` (Senior's 11½-hour day and the "last hour"). Pin `suRate`, `suParts`.
   - Misconception: the rate of exploitation is s divided by all the capital.
   - Worked: s = 90 on v = 90 is 100%, not the 90/500 = 18% that a rate on the whole capital would say.

7. **the-working-day-and-surplus-labour** — The Working Day: Its Limits and the Greed for Surplus Labour — *Chapter 10 · The Working Day*
   - Read: §1, "Capital is dead labour, that, vampire-like, only lives by sucking living labour"; §3–4 on night work and relays.
   - Do: compute s/v for a given day and necessary time, and the lengthening that doubles it.
   - Lab: `workday`, view `absolute`. Presets: `six-six` (12-hour day, 6 necessary), `fifteen` (15-hour day), `relay` (24-hour plant on two shifts). Pin `wdRate`, `wdSurplus`.
   - Misconception: the length of the day is fixed by nature or contract and is not a quantity capital can move.
   - Worked: 6 necessary hours of 12 is 100%; stretch the day to 15 and the same worker gives 150%.

8. **the-struggle-for-a-normal-working-day** — The Struggle for a Normal Working Day — *Chapter 10 · The Working Day*
   - Read: §6–7, the Factory Acts and "the creation of a normal working day is… the product of a protracted civil war".
   - Do: compute what a legal limit (the Ten Hours Act) does to s/v at a fixed value of labour-power and say why the limit is fought over.
   - Lab: `workday`, view `limit`. Presets: `before` (12 hours), `ten-hours` (the 1847 Act's 10 hours), `relay-dodge` (the "false relay" system: legal 10 hours stretched by shifts). Pin `wdRate`.
   - Misconception: the Factory Acts were humanitarian gifts from above.
   - Worked: cut a 12-hour day with 6 necessary to 10 and s/v falls from 100% to 67%; that is the money the struggle is about.

9. **rate-and-mass-of-surplus-value** — Rate and Mass of Surplus Value — *Chapter 11*
   - Read: the first law, "the mass of the surplus value produced is equal to the amount of the variable capital advanced, multiplied by the rate of surplus value".
   - Do: compute the mass of surplus value from s/v, the value of one labour-power and the number of workers, and show the trade-off between fewer workers and a longer day.
   - Lab: `surplus`, view `mass`. Presets: `hundred` (100 workers, 3s each, 100%), `fewer` (50 workers, the rate raised to 200%), `limit` (the rate cannot exceed 24 hours less necessary time). Pin `suMass`.
   - Misconception: more workers always means more surplus value.
   - Worked: 100 workers at 3s and 100% give 300s; 50 workers must be worked at 200% to give the same.

### Course 3 — Relative Surplus Value (`capital-relative-surplus-value`, 9)

1. **the-concept-of-relative-surplus-value** — The Concept of Relative Surplus Value — *Chapter 12*
   - Read: "The surplus value produced by prolongation of the working day, I call absolute surplus value. On the other hand, the surplus value arising from the curtailment of the necessary labour-time… I call relative surplus value."
   - Do: compute the new s/v when productivity in the wage-goods industries cuts necessary time, and the extra surplus value of a single innovating capitalist.
   - Lab: `workday`, view `relative`. Presets: `cheaper` (necessary falls 10 to 9 hours of a 12-hour day), `pioneer` (one capitalist doubles productivity and sells at the social value), `general` (everyone catches up). Pin `wdRate`, `wdExtra`.
   - Misconception: a capitalist innovates in order to lower the value of labour-power.
   - Worked: Marx's 12 shillings of output a day becomes 24 articles for one innovator, who sells above individual value and pockets the difference until competition generalises it.

2. **co-operation** — Co-operation — *Chapter 13*
   - Read: "the special productive power of the combined working day is, under all circumstances, the social productive power of labour".
   - Do: compute the combined working day of many workers and the productivity gain co-operation brings, and say who appropriates it.
   - Lab: `machine`, view `cooperate`. Presets: `twelve` (12 masons separately, 12 together at a stated gain), `hundred` (the law of large numbers: individual deviations average out), `chain` (bricks passed hand to hand). Pin `maOutput`, `maGain`.
   - Misconception: co-operation's extra product is paid for in wages because each worker is paid fully.
   - Worked: 12 workers each paid for a day produce together what 14 would apart; the 2 extra days are a free gift to capital.

3. **division-of-labour-and-manufacture** — Division of Labour and Manufacture — *Chapter 14*
   - Read: §3 on the "collective labourer" and the fixed proportions between detail workers.
   - Do: compute the number of detail workers each step needs for the steps' rates to match, and the smallest workshop that keeps every worker busy.
   - Lab: `machine`, view `detail`. Presets: `type` (type-founding: casters, breakers, polishers at Marx's rates), `pins` (Smith's pin factory), `bottle` (glass bottle workshop). Pin `maWorkers`, `maMinimum`.
   - Misconception: the division of labour inside the workshop is the same thing as the division of labour in society.
   - Worked: if a caster makes 2,000 an hour, a breaker 4,000 and a polisher 8,000, the smallest balanced shop is 4 casters, 2 breakers, 1 polisher.

4. **machinery-and-the-value-it-transfers** — Machinery and the Value It Transfers — *Chapter 15 · Machinery and Modern Industry*
   - Read: §2, "machinery, like every other component of constant capital, creates no new value, but yields up its own value to the product".
   - Do: compute the value a machine adds per unit and the capitalist's limit for adopting it (the wage bill it displaces), against society's limit (the labour it saves).
   - Lab: `machine`, view `adopt`. Presets: `adopt` (machine cost below the displaced wages), `cheap-labour` (wages so low the machine is not adopted, Marx's English and continental case), `society` (the machine saves labour-time but not wages). Pin `maPerUnit`, `maVerdict`.
   - Misconception: a machine is used whenever it saves labour.
   - Worked: a machine costing £1,000 that displaces £800 of wages is not used, though it saves more labour than it costs; the capitalist pays for labour-power, not labour.

5. **machinery-and-the-worker** — Machinery and the Worker — *Chapter 15 · Machinery and Modern Industry*
   - Read: §3, the appropriation of women's and children's labour, the prolongation and the intensification of the working day.
   - Do: compute how adding family members to the labour market divides the value of labour-power, and how intensification raises s/v without lengthening the day.
   - Lab: `workday`, view `intensity`. Presets: `family` (value of the family's labour-power spread over four workers), `intense` (the same day at 4/3 intensity), `shorter-but-denser` (a 10-hour day of 12 hours' labour). Pin `wdRate`, `wdLpValue`.
   - Misconception: a shorter working day always means less surplus value.
   - Worked: cut the day from 12 to 10 hours but raise intensity by 1/5 and the worker spends as much labour as before.

6. **machinery-and-the-displaced-worker** — Machinery and the Displaced Worker — *Chapter 15 · Machinery and Modern Industry*
   - Read: §6, "The theory of compensation as regards the workpeople displaced by machinery".
   - Do: compute the capital "set free" by a machine and the workers that capital can re-employ, and show why compensation is not automatic.
   - Lab: `machine`, view `displace`. Presets: `marx` (Marx's figures: a carpet factory with 100 workers at £30 a year, £3,000 variable capital; 50 discharged and £1,500 spent on machinery), `compensation` (the economists' claim that £1,500 is "set free" to employ the 50 elsewhere), `machine-builders` (the jobs the £1,500 of machinery gives in machine-building, at that industry's composition). Pin `maDisplaced`, `maReemployed`.
   - Misconception: the capital freed by a machine re-employs the workers it displaced.
   - Worked: 100 workers at £30 is £3,000 of variable capital; after the change £1,500 pays 50 and £1,500 sits in machinery: nothing was set free, a fund for wages became constant capital.

7. **absolute-and-relative-surplus-value** — Absolute and Relative Surplus Value — *Chapter 16*
   - Read: "From one standpoint the distinction between absolute and relative surplus value appears illusory."
   - Do: classify a change in s/v as absolute or relative and say when the distinction matters.
   - Lab: `workday`, view `classify`. Presets: `lengthen`, `cheapen`, `both`. Pin `wdKind`, `wdRate`.
   - Misconception: surplus value needs a natural surplus of the soil.
   - Worked: from 12/6 to 14/5: 2 more hours are absolute, 1 fewer necessary hour is relative; s/v goes from 100% to 180%.

8. **price-of-labour-power-and-surplus-value** — Changes in the Price of Labour-Power and in Surplus Value — *Chapter 17*
   - Read: the three determinants, "the length of the working day… the normal intensity of labour… the productiveness of labour".
   - Do: run Marx's cases — one factor varying, the others constant — and predict the direction of s/v and of the price of labour-power.
   - Lab: `workday`, view `three`. Presets: `productivity`, `intensity`, `length`, `combined`. Shipped `hold = others`. Pin `wdRate`, `wdLpValue`.
   - Misconception: higher productivity raises the value of what the worker produces each day.
   - Worked: double productivity with the day fixed at 12 and the value produced is still 12 hours; only its split between v and s can move.

9. **formulae-for-the-rate-of-surplus-value** — Formulae for the Rate of Surplus Value — *Chapter 18*
   - Read: the "derivative formulae", surplus labour over the whole working day.
   - Do: compute s/v and s/(v + s) for the same day and show why the second can never reach 100%.
   - Lab: `surplus`, view `formulae`. Presets: `half` (6/6), `two-thirds` (4/8), `extreme` (1/11). Pin `suRate`, `suFalse`.
   - Misconception: s/(v + s) measures exploitation.
   - Worked: 8 surplus hours in 12 is 200% by s/v and 2/3 by the "derivative" formula.

### Course 4 — Wages and Accumulation (`capital-wages-and-accumulation`, 9)

1. **value-of-labour-power-into-wages** — The Value of Labour-Power Becomes Wages — *Chapter 19*
   - Read: "On the surface of bourgeois society the wage of the labourer appears as the price of labour, a certain quantity of money that is paid for a certain quantity of labour."
   - Do: compute the "value of labour" that the wage form appears to pay and show it is the value of labour-power divided by the hours, not the value the hours create.
   - Lab: `wages`, view `form`. Presets: `marx` (3s for 12 hours), `value-created` (12 hours create 6s), `irrational` ("the value of labour" as 3s/12 hours). Pin `waHourPrice`, `waValueCreated`.
   - Misconception: the wage is the price of the work done.
   - Worked: 3s for a 12-hour day looks like 3d an hour paid for 3d of value; each hour creates 6d.

2. **time-wages** — Time-Wages — *Chapter 20*
   - Read: the "price of labour" falls as the day lengthens while the daily wage stays.
   - Do: compute the hourly price from the daily value of labour-power and the normal day, and the effect of overtime and short time.
   - Lab: `wages`, view `time`. Presets: `normal`, `overtime` (paid at the same hourly rate), `short-time` (hours cut, hourly rate kept). Pin `waHourPrice`, `waDaily`.
   - Misconception: a higher hourly rate means a better-paid worker.
   - Worked: 3s for a 12-hour normal day is 3d an hour; work 6 hours at 3d and the worker gets 1s 6d, below the value of labour-power.

3. **piece-wages** — Piece-Wages — *Chapter 21*
   - Read: "Piece-wage is nothing else than a converted form of the time-wage."
   - Do: compute the piece-rate from the hourly price and the normal output, and the hidden speed-up when the rate is cut after output rises.
   - Lab: `wages`, view `piece`. Presets: `marx` (Marx's figures: 24 pieces in 12 hours, 3s a day, so 1½d a piece), `faster` (output rises to 36), `cut` (rate cut back to the old day's pay). Pin `waPieceRate`, `waDaily`.
   - Misconception: piece-wages pay for the worker's actual effort.
   - Worked: 3s for 24 pieces is 1½d a piece; at 36 pieces the rate is cut to 1d and the day pays 3s again.

4. **national-differences-of-wages** — National Differences of Wages — *Chapter 22*
   - Read: "the more intensive national working-day… is represented by more money".
   - Do: compare two countries' money wages with their intensity and productivity, and compute the relative wage.
   - Lab: `wages`, view `national`. Presets: `england-continent`, `same-intensity`, `cheaper-goods`. Pin `waRelative`.
   - Misconception: a country with higher money wages has a lower rate of surplus value.
   - Worked: wages twice as high for 1½ times the output per hour mean a lower relative wage and a higher rate of surplus value.

5. **simple-reproduction** — Simple Reproduction — *Chapter 23*
   - Read: "after a longer or shorter period, the value of the capital advanced becomes equal to the surplus value appropriated…".
   - Do: compute how many years of consumed surplus value equal the capital advanced, and say what that means for "the capitalist's own" capital.
   - Lab: `accumulate`, view `simple`. Presets: `marx` (Marx's figures: £1,000 capital, £200 surplus a year consumed), `faster` (£250 a year), `slower` (£100). Pin `acYears`.
   - Misconception: the capital remains the capitalist's original property however long it runs.
   - Worked: £1,000 advanced and £200 a year consumed: after 5 years the capitalist has eaten the original sum, and what remains is capitalised surplus value.

6. **surplus-value-into-capital** — Surplus Value into Capital — *Chapter 24*
   - Read: "Accumulate, accumulate! That is Moses and the prophets!"
   - Do: run accumulation period by period with a share of s added to capital, and separate original capital from capitalised surplus value.
   - Lab: `accumulate`, view `expand`. Presets: `marx` (Marx's figures: £10,000 at 4:1 c to v, 100%, half of s accumulated), `all` (all of s accumulated), `abstinence` (none: simple reproduction). Shipped `periods = 5`. Pin `acCapital`, `acShareOriginal`.
   - Misconception: accumulation is the capitalist's "abstinence" from consumption.
   - Worked: after five years at the Marx preset, a stated share of the capital is capitalised surplus value; the lab prints it.

7. **accumulation-with-constant-composition** — Accumulation with Constant Composition — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §1, "Accumulation of capital is, therefore, increase of the proletariat."
   - Do: compute the demand for labour as accumulation proceeds at constant c/v, and when it outruns the labour supply and wages rise.
   - Lab: `accumulate`, view `labour`. Presets: `steady` (supply grows faster than demand), `tight` (demand overtakes supply in period 3), `wage-rise` (the rise slows accumulation). Pin `acDemand`, `acReserve`.
   - Misconception: rising wages show that accumulation benefits the worker without limit.
   - Worked: v grows by half of s each year; when it exceeds the workers available the reserve is empty and wages rise until accumulation slows.

8. **the-reserve-army** — The Reserve Army of Labour — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §3, "the progressive production of a relative surplus population or industrial reserve army".
   - Do: compute employment when capital grows while c/v rises, and the surplus population that results.
   - Lab: `accumulate`, view `composition`. Presets: `rising` (c/v from 4 to 6 over five periods), `fast-growth`, `constant` (no rise). Pin `acDemand`, `acReserve`.
   - Misconception: accumulation always increases employment.
   - Worked: capital doubles while c/v goes from 1 to 3; v falls from half to a quarter of capital and employment stays flat.

9. **the-general-law-of-accumulation** — The General Law of Capitalist Accumulation — *Chapter 25 · The General Law of Capitalist Accumulation*
   - Read: §4, "Accumulation of wealth at one pole is, therefore, at the same time accumulation of misery… at the opposite pole".
   - Do: name the floating, latent and stagnant forms of the reserve army in a given population, and compute the ratio of reserve to active workers the law speaks of.
   - Lab: `accumulate`, view `law`. Presets: `boom`, `slump`, `long-run`. Pin `acReserve`, `acRatio`.
   - Misconception: the law predicts that real wages must always fall.
   - Worked: the law is about the relative size of the reserve, which can grow while employed workers' wages rise.

### Course 5 — So-Called Primitive Accumulation (`capital-primitive-accumulation`, 8)

1. **the-secret-of-primitive-accumulation** — The Secret of Primitive Accumulation — *Chapter 26*
   - Read: "This primitive accumulation plays in Political Economy about the same part as original sin in theology."
   - Do: use the simple-reproduction result to show that accumulation presupposes a capital it cannot itself explain, and say what Marx offers instead of the "nursery tale".
   - Lab: `accumulate`, view `simple`. Presets: `regress` (any starting capital consumed in n years), `thrift` (a "diligent elite" saving 10% a year of a wage), `separation` (a capital that starts with workers separated from means of production). Pin `acYears`.
   - Misconception: the first capitalists became so by saving.
   - Worked: a worker saving 10% of a 3s wage would need 1,000 days to hoard £15; the mill of Chapter 7 needs far more and a workforce besides.
   - (Volume I's English edition numbers Part Eight as Chapters 26–33; the German edition has them as sections of Chapter 24 and Chapter 25. The lesson says so once.)

2. **expropriation-from-the-land** — Expropriation of the Agricultural Population — *Chapter 27*
   - Read: "the history of this, their expropriation, is written in the annals of mankind in letters of blood and fire" (Chapter 26) and the clearing of the estates.
   - Do: compute the smallholder's working day before expropriation (all labour for themselves) and the same person's day as a wage-worker, and locate the surplus that separation creates.
   - Lab: `workday`, view `separate`. Presets: `smallholder` (12 hours, all for the household), `labourer` (12 hours, 6 necessary), `clearing` (many smallholders made labourers). Pin `wdSurplus`.
   - Misconception: enclosure mattered because it made farming more efficient.
   - Worked: the same 12-hour day yields 0 hours of surplus to anyone else on one's own land and 6 to an employer after the clearing.

3. **bloody-legislation** — Bloody Legislation and the Forcing Down of Wages — *Chapter 28*
   - Read: the Statute of Labourers of 1349 and "laws for the compulsion of labour".
   - Do: compute the gap between a statutory maximum wage and the value of labour-power, and the rate of surplus value the law enforces.
   - Lab: `wages`, view `statute`. Presets: `statute` (illustrative statutory maximum below value), `market` (wage at value), `combination` (wages after combination laws). Pin `waGap`, `waRate`. The lesson says the figures are illustrative.
   - Misconception: wage labour was always freely contracted.
   - Worked: a legal maximum one-third below the value of labour-power turns a 100% rate into one of 200%.

4. **the-capitalist-farmer** — Genesis of the Capitalist Farmer — *Chapter 29*
   - Read: "The fall in the value of the precious metals, and therefore of money, brought the farmer golden fruit."
   - Do: compute a money rent fixed by long lease while gold's value falls and prices rise, and the farmer's gain at the landlord's and labourer's expense.
   - Lab: `money`, view `fixed-rent`. Presets: `price-revolution` (prices double over the lease), `stable`, `wages-lag` (wages rise by half as much). Pin `moRealRent`, `moFarmerGain`.
   - Misconception: the capitalist farmer grew rich by working harder than the yeoman.
   - Worked: a £20 rent fixed while prices double now costs the farmer half as much in corn.

5. **the-home-market** — The Home Market for Industrial Capital — *Chapter 30*
   - Read: "The expropriation and expulsion of the agricultural population… set free… their former means of nourishment".
   - Do: compute the market created when households that produced their own subsistence must buy it, and the variable capital that now circulates.
   - Lab: `circuit`, view `market`. Presets: `before` (100 households, self-supplied), `after` (the same households as wage-earners), `half`. Pin `ciMarket`.
   - Misconception: the home market grew because people became richer.
   - Worked: 100 households that spun their own yarn now buy it: the same use-values, newly commodities, a market where none was.

6. **the-industrial-capitalist** — Genesis of the Industrial Capitalist — *Chapter 31*
   - Read: "The public debt becomes one of the most powerful levers of primitive accumulation."
   - Do: compute the capitalised value of a state debt from its annual interest, and the tax burden that services it.
   - Lab: `interest`, view `capitalise`. Presets: `consols` (£3 a year at 3%), `cheap-money` (rate falls to 2%), `tax` (interest paid from taxes on necessaries). Pin `inPrice`.
   - Misconception: public debt is wealth the nation owes itself and so costs nothing.
   - Worked: £3 a year at 3% is a £100 claim; nothing was built, but £100 is now capital in its owner's books.

7. **the-historical-tendency** — Historical Tendency of Capitalist Accumulation — *Chapter 32*
   - Read: "The knell of capitalist private property sounds. The expropriators are expropriated."
   - Do: compute concentration and centralisation for a set of capitals over several periods and the share held by the largest.
   - Lab: `accumulate`, view `centralise`. Presets: `ten` (ten capitals, equal), `merge` (the largest absorbs the smallest each period), `grow` (all grow, no merger). Pin `acTopShare`, `acCount`.
   - Misconception: Marx's tendency is a forecast with a date.
   - Worked: ten equal capitals where the largest absorbs the smallest each period leave one capital holding half the total after five periods.

8. **the-modern-theory-of-colonisation** — The Modern Theory of Colonisation — *Chapter 33*
   - Read: Mr. Peel who took £50,000 and 3,000 workers to the Swan River, and was "left without a servant to make his bed".
   - Do: compute the labour supply left to a colonial capitalist when workers can take free land, and Wakefield's land price that restores it.
   - Lab: `accumulate`, view `colony`. Presets: `peel` (Marx's figures: 3,000 workers, free land), `wakefield` (a land price that takes years of wages to pay), `closed` (no free land). Pin `acReserve`, `acYearsToLand`.
   - Misconception: capital is a thing — money and machines — that can be exported.
   - Worked: with free land every worker leaves; at a price of 4 years' savings the labour market is restored for 4 years per worker.

### Course 6 — The Circuits of Capital (`capital-circuits-of-capital`, 6)

Volume II's Part One. Prose cites Volume II chapters as "Volume II, Chapter n".

1. **the-circuit-of-money-capital** — The Circuit of Money Capital — *Chapter 1*
   - Read: the formula M–C…P…C′–M′ and "the circuit of money-capital is… the most one-sided… form".
   - Do: trace a capital through its three stages, give the value in each form, and compute s from M and M′.
   - Lab: `circuit`, view `stages`. Presets: `marx` (Marx's figures: £422 advanced as £372 means of production and £50 labour-power; product 10,000 lb yarn worth £500), `unsold` (C′ not yet sold), `partly` (half sold). Pin `ciMprime`, `ciS`.
   - Misconception: the money at the end is where the surplus is made.
   - Worked: £422 becomes yarn worth £500 inside P; selling it only changes £500's form.

2. **the-circuit-of-productive-capital** — The Circuit of Productive Capital — *Chapter 2*
   - Read: "the circuit of productive capital has the general formula P…C′–M′–C…P".
   - Do: run the productive circuit under simple reproduction and under accumulation and compute the capital that re-enters P.
   - Lab: `accumulate`, view `simple`, with `circuit = productive`. Presets: `simple` (all of s spent), `accumulate` (half of s re-enters P), `hoard` (s accumulated as a money hoard until it is large enough to invest). Pin `acCapital`.
   - Misconception: the productive circuit is the money circuit started at a different point.
   - Worked: with £78 of s, simple reproduction restarts P at £422; accumulating half restarts it at £461.

3. **the-circuit-of-commodity-capital** — The Circuit of Commodity Capital — *Chapter 3*
   - Read: "C′–M′–C…P…C″" and why this circuit is the one that shows the whole social product.
   - Do: split C′ into the parts that return as means of production, as wages and as capitalists' consumption.
   - Lab: `surplus`, view `parts`, applied to the commodity product. Presets: `marx` (the £500 of yarn), `consumed`, `accumulated`. Pin `suParts`.
   - Misconception: the commodity product is all revenue to be consumed.
   - Worked: of £500 of yarn, £372 must buy back means of production; only £128 is anyone's income.

4. **the-three-formulas-of-the-circuit** — The Three Formulas of the Circuit — *Chapter 4*
   - Read: "The circuit of industrial capital… is not only a unity of circulation and production, but also of all its three circuits."
   - Do: compute how a capital divides at any moment among money, productive and commodity forms when each stage takes a stated time.
   - Lab: `turnover`, view `phases`. Presets: `even` (4 weeks each), `slow-sale` (selling takes 8), `fast` (2, 6, 2). Pin `tuMoney`, `tuProductive`, `tuCommodity`.
   - Misconception: a capital is in one form at a time.
   - Worked: with 4 weeks in each stage, a continuous business always has a third of its capital in each form.

5. **the-time-of-circulation** — The Time of Circulation — *Chapter 5*
   - Read: "The time of circulation and the time of production mutually exclude each other."
   - Do: compute turnover time as production time plus circulation time, and production time as working time plus the time the product only waits (wine maturing, corn growing).
   - Lab: `turnover`, view `time`. Presets: `spinning`, `wine` (production time well above working time), `distant-market`. Pin `tuTurnover`, `tuWorkingShare`.
   - Misconception: every week in which capital is tied up is a week of labour.
   - Worked: wine worked for 4 weeks and cellared for 48 has a production time of a year and creates value for 4 weeks of it.

6. **the-costs-of-circulation** — The Costs of Circulation — *Chapter 6*
   - Read: §1, the costs of buying and selling and of book-keeping, "faux frais"; §2, storage; §3, transport.
   - Do: classify circulation costs as pure costs (deductions from surplus value) or as costs that add value (transport, necessary storage), and compute the deduction.
   - Lab: `circuit`, view `costs`. Presets: `clerks` (£10 of pure costs on £100 of s), `transport` (£10 of carriage), `stockpile` (storage beyond the necessary). Pin `ciSNet`.
   - Misconception: everything a business must pay for adds to the value of its product.
   - Worked: a bookkeeper paid £10 leaves £90 of s; a carter paid £10 adds £10 to the value delivered.

### Course 7 — The Turnover of Capital (`capital-turnover-of-capital`, 11)

1. **turnover-time-and-number-of-turnovers** — Turnover Time and the Number of Turnovers — *Chapter 7*
   - Read: "the year is the natural unit of measure for the turnovers of functioning capital".
   - Do: compute n = U/u for given turnover times.
   - Lab: `turnover`, view `time`. Presets: `three-months`, `five-weeks`, `two-years`. Pin `tuTurnovers`.
   - Misconception: a capital that turns over twice a year has twice the capital.
   - Worked: a turnover of 3 months gives 4 turnovers a year of the same capital.

2. **fixed-and-circulating-capital** — Fixed Capital and Circulating Capital — *Chapter 8*
   - Read: §1, fixed capital "circulates… piecemeal, in proportion to its wear and tear".
   - Do: compute the annual value transferred by fixed capital from value and life, and the circulating capital's turnover in the same year.
   - Lab: `turnover`, view `fixed`. Presets: `ten-years` (£10,000 machine, 10 years), `repairs` (with repair costs), `moral` (moral depreciation: a cheaper machine appears in year 4). Pin `tuWear`, `tuRemaining`.
   - Misconception: fixed and circulating are the same distinction as constant and variable.
   - Worked: a £10,000 machine on a 10-year life transfers £1,000 a year and still has £6,000 of value locked in after four.

3. **aggregate-turnover** — The Aggregate Turnover of Advanced Capital — *Chapter 9*
   - Read: "the value turned over… is the sum of the value of the fixed and circulating capital that has turned over".
   - Do: compute the aggregate turnover of a capital with fixed and circulating parts and the average turnover time.
   - Lab: `turnover`, view `aggregate`. Presets: `marx` (Marx's figures for fixed and circulating capital, verified from the text), `heavy-fixed`, `light-fixed`. Pin `tuAggregate`, `tuAverage`.
   - Misconception: a capital's turnover time is the turnover time of its circulating part.
   - Worked: the lab prints the value turned over in a year and the months the whole capital takes to turn over once.

4. **physiocrats-and-adam-smith** — The Physiocrats and Adam Smith on Fixed Capital — *Chapter 10*
   - Read: Smith's definition of fixed capital as what yields a profit "without circulating".
   - Do: classify the same capital by Smith's fixed/circulating and by constant/variable, and show which split determines surplus value.
   - Lab: `turnover`, view `classify`. Presets: `farm` (the Physiocrats' avances), `mill`, `smith` (wages counted with raw materials as circulating). Pin `tuFixed`, `tuVariable`.
   - Misconception: wages and raw materials are the same kind of capital because both circulate.
   - Worked: £100 of cotton and £100 of wages are both circulating, but only the second creates new value.

5. **ricardo-on-fixed-and-circulating-capital** — Ricardo on Fixed and Circulating Capital — *Chapter 11*
   - Read: Ricardo's use of durability to explain departures from labour values.
   - Do: compute two capitals with equal totals and different fixed shares and show what the fixed/circulating split explains and what it hides.
   - Lab: `turnover`, view `classify`. Presets: `durable`, `wages-heavy`, `equal`. Pin `tuFixed`, `tuVariable`.
   - Misconception: the fixed/circulating split explains where profit comes from.
   - Worked: two £1,000 capitals with the same fixed share but different wage bills produce different s; the fixed share cannot tell them apart.

6. **the-working-period** — The Working Period — *Chapter 12*
   - Read: "a locomotive… is the product of… a working period" and the capital tied up until it is finished.
   - Do: compute capital tied up over a long working period paid weekly, and the advance needed before any return.
   - Lab: `turnover`, view `working`. Presets: `cotton` (a day), `locomotive` (3 months), `railway` (a year). Pin `tuAdvance`.
   - Misconception: a long working period is only a question of patience.
   - Worked: £100 a week for a 12-week working period ties up £1,200 before anything can be sold.

7. **the-time-of-production** — The Time of Production — *Chapter 13*
   - Read: the interruptions of the labour process — seasons, growth, drying — that are still production time.
   - Do: compute the working-time share of a production period and its effect on turnovers a year.
   - Lab: `turnover`, view `time`. Presets: `wheat` (9 months, 3 worked), `timber` (years), `brewing`. Pin `tuWorkingShare`, `tuTurnovers`.
   - Misconception: shortening production time is always shortening labour time.
   - Worked: a crop needing 3 months of work over 9 months turns over once a year at most.

8. **the-time-of-circulation-in-turnover** — The Time of Circulation in the Turnover — *Chapter 14*
   - Read: distance from market and "the period of selling".
   - Do: compute how distance and selling time lengthen turnover, and the effect of a railway.
   - Lab: `turnover`, view `time`. Presets: `near`, `india` (Marx's cotton goods to India), `railway`. Pin `tuTurnover`, `tuTurnovers`.
   - Misconception: circulation time is wasted only for the merchant.
   - Worked: a 6-week sale on a 6-week production halves the turnovers of the same capital.

9. **turnover-time-and-capital-advanced** — Turnover Time and the Capital Advanced — *Chapter 15*
   - Read: §1–3, the working period of 9 weeks and the circulation period of 3, and the additional capital.
   - Do: compute the additional capital a continuous business needs when its working and circulation periods differ, and the capital "set free".
   - Lab: `turnover`, view `advance`. Presets: `marx` (Marx's figures: 9-week working period at £100 a week, 3-week circulation), `equal` (working = circulation), `longer-circulation`. Pin `tuAdvance`, `tuFreed`.
   - Misconception: a capital needs only enough to cover one working period.
   - Worked: 9 weeks at £100 is capital I of £900; to keep working while it circulates for 3 weeks needs capital II of £300.

10. **the-turnover-of-variable-capital** — The Turnover of Variable Capital — *Chapter 16*
    - Read: §1, "the annual rate of surplus value".
    - Do: compute the annual rate of surplus value s′·n and show why it differs between capitals with the same real s′.
    - Lab: `turnover`, view `annual`. Presets: `marx-a` (Marx's figures: £500 variable, 10 turnovers, 100%), `marx-b` (£5,000 variable, 1 turnover, 100%), `same-mass` (both). Pin `tuAnnualRate`, `tuMassS`.
    - Misconception: a capital that turns over faster exploits its workers harder.
    - Worked: capital A's annual rate is 1,000% and B's 100%; the workers in both are exploited at 100% and produce the same mass of s.

11. **the-circulation-of-surplus-value** — The Circulation of Surplus Value — *Chapter 17*
    - Read: "where does the money come from" to realise the surplus value.
    - Do: compute the money the capitalist class must throw into circulation for its consumption and show it returns as realised s.
    - Lab: `circuit`, view `realise`. Presets: `consumption` (£100 spent on consumption ahead of sales), `gold` (gold producers' s), `credit`. Pin `ciReturned`.
    - Misconception: there is never enough money to realise surplus value, so capitalism needs constant outside demand.
    - Worked: capitalists spend £100 on consumption during the year; the same £100 returns as the money form of £100 of s.

### Course 8 — Reproduction of the Social Capital (`capital-social-reproduction`, 6)

1. **the-object-of-the-inquiry** — The Object of the Inquiry — *Chapter 18*
   - Read: "the movement of the total social capital… comprises the productive consumption… and the individual consumption".
   - Do: sort a society's product into means of production and means of consumption and say why the individual capital's circuit cannot answer the social question.
   - Lab: `schemes`, view `sort`. Presets: `two-dept` (a small product list), `marx-totals`, `misclassified` (coal used at home). Pin `scDeptI`, `scDeptII`.
   - Misconception: the economy is one big firm.
   - Worked: the same coal is Department I sold to a mill and Department II sold to a kitchen.

2. **former-presentations** — Former Presentations: Quesnay and Smith — *Chapter 19*
   - Read: §2, Adam Smith's resolution of price into v + s, "the dogma".
   - Do: compute the annual product's value with and without c, and show where Smith's account loses the constant capital.
   - Lab: `revenue`, view `dogma`. Presets: `marx-scheme` (the simple reproduction totals), `one-firm`, `tableau` (Quesnay's classes in outline). Pin `rvTotal`, `rvSmith`.
   - Misconception: the whole price of the annual product is resolved into incomes.
   - Worked: 9,000 of annual product against 3,000 of incomes; Smith's account has lost 6,000 of means of production.

3. **simple-reproduction-the-three-exchanges** — Simple Reproduction: The Three Great Exchanges — *Chapter 20 · Simple Reproduction*
   - Read: §2–5, the scheme "I. 4,000c + 1,000v + 1,000s = 6,000; II. 2,000c + 500v + 500s = 3,000".
   - Do: check whether a two-department scheme reproduces itself (I(v + s) = IIc) and compute each of the three exchanges.
   - Lab: `schemes`, view `simple`. Presets: `marx` (Marx's figures), `too-much-I` (I's v + s exceeds IIc), `too-little-I`. Pin `scBalance`, `scIExchange`.
   - Misconception: each department's product only needs a buyer, not a buyer in the other department.
   - Worked: I(1,000v + 1,000s) = 2,000 = IIc; the scheme closes; raise I's s by 100 and 100 of means of production find no buyer.

4. **simple-reproduction-fixed-capital-and-money** — Simple Reproduction: Fixed Capital and Money — *Chapter 20 · Simple Reproduction*
   - Read: §11, the replacement of fixed capital, and §12, the reproduction of the money material.
   - Do: compute the balance between capitals hoarding for wear and capitals renewing their machines in Department II, and the crisis when they diverge.
   - Lab: `schemes`, view `fixed`. Presets: `balanced` (wear set aside = renewals bought), `bunched` (renewals all fall in one year), `gold`. Pin `scFixedGap`.
   - Misconception: depreciation is a cost that balances automatically every year.
   - Worked: 200 of wear set aside against 200 of renewals: balanced; let renewals bunch to 300 and 100 of Department I's product cannot be sold.

5. **accumulation-and-money** — Accumulation in Department I and the Money It Needs — *Chapter 21 · Accumulation and Reproduction on an Extended Scale*
   - Read: §1, the hoard as "virtual new money-capital".
   - Do: compute how one-sided sales (hoarding) and purchases (investing) must balance for accumulation to proceed.
   - Lab: `schemes`, view `hoard`. Presets: `balanced` (sellers and buyers of surplus product equal), `all-hoard`, `all-invest`. Pin `scHoardGap`.
   - Misconception: saving automatically becomes investment.
   - Worked: if every capitalist in Department I hoards at once, 500 of surplus product is unsold.

6. **extended-reproduction** — Reproduction on an Extended Scale — *Chapter 21 · Accumulation and Reproduction on an Extended Scale*
   - Read: §3, the schematic presentation, "I. 4,000c + 1,000v + 1,000s = 6,000; II. 1,500c + 750v + 750s = 3,000".
   - Do: run the expanded scheme for several years, with Department I accumulating half its s and Department II adjusting, and compute the growth path.
   - Lab: `schemes`, view `expanded`. Presets: `marx` (Marx's figures: the first example), `ii-leads` (Department II tries to set the pace), `half-half`. Shipped `years = 4`. Pin `scYear2`, `scGrowth`.
   - Misconception: the two departments can grow at any rates they like.
   - Worked: from I 4,000c + 1,000v + 1,000s and II 1,500c + 750v + 750s, year one ends at I 4,400c + 1,100v and II 1,600c + 800v.

### Course 9 — Cost Price and the Rate of Profit (`capital-cost-price-and-profit`, 7)

Volume III's Part One. Prose cites "Volume III, Chapter n".

1. **cost-price-and-profit** — Cost Price and Profit — *Chapter 1*
   - Read: "The value of every commodity produced in the capitalist way is represented in the formula C = c + v + s."
   - Do: compute cost price k = c + v and profit, and say why profit looks like the offspring of the whole capital.
   - Lab: `profit`, view `cost`. Presets: `marx` (Marx's figures: 400c + 100v + 100s = 600, cost price 500), `cheap-sale` (sold at 560, still a profit), `below-cost`. Pin `prCost`, `prProfit`.
   - Misconception: a commodity sold above its cost price is sold above its value.
   - Worked: 600 of value, 500 of cost price: a sale at 560 is profitable and still 40 below value.

2. **the-rate-of-profit** — The Rate of Profit — *Chapter 2*
   - Read: "the rate of surplus value measured against the variable capital is called rate of surplus value; measured against the total capital it is called rate of profit".
   - Do: compute p′ = s/(c + v) beside s′ = s/v for the same capital.
   - Lab: `profit`, view `rate`. Presets: `marx`, `labour-heavy`, `capital-heavy`. Pin `prRate`, `prSRate`.
   - Misconception: the rate of profit measures exploitation.
   - Worked: 100s on 400c + 100v is 100% s′ and 20% p′.

3. **rate-of-profit-and-rate-of-surplus-value** — The Rate of Profit and the Rate of Surplus Value — *Chapter 3*
   - Read: "p′ = s′ v/C".
   - Do: vary s′ and the composition one at a time and predict the effect on p′.
   - Lab: `profit`, view `relation`. Presets: `vary-s`, `vary-composition`, `both-offset` (a rise in s′ exactly offset by a rise in c/v). Pin `prRate`.
   - Misconception: a rising rate of surplus value must raise the rate of profit.
   - Worked: s′ up from 100% to 150% while c/v rises from 4 to 6.5: p′ stays at 20%.

4. **turnover-and-the-rate-of-profit** — The Effect of Turnover on the Rate of Profit — *Chapter 4*
   - Read: the annual rate of profit and the turnover of the variable capital.
   - Do: compute the annual rate of profit from s′, n, v and C.
   - Lab: `profit`, view `turnover`. Presets: `once`, `ten-times`, `faster-sale`. Pin `prAnnual`.
   - Misconception: turnover affects only the circulating capital's profit.
   - Worked: v = 100 turned 5 times at 100% on C = 1,000 gives an annual p′ of 50%.

5. **economy-in-constant-capital** — Economy in the Use of Constant Capital — *Chapter 5*
   - Read: §1, "economy in the conditions of labour at the expense of the labourers".
   - Do: compute the rise in p′ when c is cut with s and v unchanged, and say at whose cost the saving often comes.
   - Lab: `profit`, view `economy`. Presets: `shared-building`, `waste-reuse`, `unsafe` (ventilation cut). Pin `prRate`.
   - Misconception: economy in constant capital is only good management.
   - Worked: cutting c from 400 to 300 with 100v and 100s raises p′ from 20% to 25%.

6. **price-fluctuations-of-raw-materials** — Price Fluctuations of Raw Materials — *Chapter 6*
   - Read: §1, "fluctuations in the price of raw material… affect the rate of profit".
   - Do: compute p′ when the raw material's price rises, with and without the product's price following.
   - Lab: `profit`, view `price`. Presets: `cotton-famine` (cotton doubles), `passed-on`, `cheaper`. Pin `prRate`.
   - Misconception: a raw material price rise is always passed on in full.
   - Worked: if raw material in c rises by 100 and the product's price does not, p′ falls from 20% to 1/6.

7. **supplementary-remarks-on-profit** — Supplementary Remarks on Profit — *Chapter 7*
   - Read: the capitalist's "practical notion" of profit and why it must differ from s.
   - Do: reconcile the capitalist's book-keeping view (profit on capital, cost price) with Marx's categories for the same numbers.
   - Lab: `profit`, view `books`. Presets: `ledger`, `marx-view`, `both`. Pin `prProfit`, `prRate`.
   - Misconception: the two accounts disagree about the numbers.
   - Worked: the books and the analysis agree on every figure; they disagree only about what the 100 is.

### Course 10 — Average Profit and Its Fall (`capital-prices-of-production`, 8)

1. **different-compositions-different-rates** — Different Compositions, Different Rates of Profit — *Chapter 8*
   - Read: the five capitals with "the same rate of surplus value" and "very different rates of profit".
   - Do: compute the rate of profit of each of five spheres from c, v and a common s′, and state the problem it creates for selling at value.
   - Lab: `prices`, view `rates`. Presets: `marx` (Marx's figures: 80c+20v, 70c+30v, 60c+40v, 85c+15v, 95c+5v at 100%), `two`, `equal-composition`. Pin `ppRates`.
   - Misconception: competition already makes rates of profit equal at values.
   - Worked: at 100% s′ the five rates run from 5% to 40%.

2. **the-general-rate-of-profit** — The General Rate of Profit and Prices of Production — *Chapter 9*
   - Read: the table of five spheres, with used-up c, and "the sum of the prices of production… is equal to the sum of their values".
   - Do: compute the average rate of profit and each sphere's price of production, and check that total profit equals total surplus value and total price equals total value.
   - Lab: `prices`, view `production`. Presets: `marx` (Marx's figures with used-up c of 50, 51, 51, 40, 10), `all-used-up`, `three`. Pin `ppAverage`, `ppPrices`, `ppTotals`.
   - Misconception: prices of production abolish the law of value because no commodity sells at its value.
   - Worked: values 90, 111, 131, 70, 20; average rate 22%; prices of production 92, 103, 113, 77, 37; both sum to 422.

3. **market-value-and-surplus-profit** — Market Value and Surplus Profit — *Chapter 10*
   - Read: the three groups of producers, and the market value "regulated" by the mass produced under average conditions.
   - Do: compute a market value as the weighted average of individual values and each group's surplus profit or loss.
   - Lab: `value`, view `market`. Presets: `average-dominates`, `worst-dominates` (demand forces the worst to regulate), `best-dominates`. Pin `vaMarketValue`, `vaSurplus`.
   - Misconception: supply and demand determine value.
   - Worked: 1,000 units at 3 h, 8,000 at 4 h and 1,000 at 5 h: market value 4 hours; the best group earns 1 hour of surplus profit per unit.

4. **wages-and-prices-of-production** — Wage Changes and Prices of Production — *Chapter 11*
   - Read: "a general rise in wages… the price of production of commodities from a capital of lower composition rises".
   - Do: recompute prices of production after a general wage rise and show which prices rise, which fall and which stay.
   - Lab: `prices`, view `wage-rise`. Presets: `marx` (Marx's figures: social average 80c + 20v, a 25% rise in wages), `three-spheres`, `fall`. Pin `ppPrices`, `ppAverage`.
   - Misconception: a general wage rise raises all prices.
   - Worked: the average-composition sphere's price is unchanged; the labour-heavy sphere's rises and the capital-heavy sphere's falls.

5. **supplementary-remarks-on-prices** — Supplementary Remarks on Prices of Production — *Chapter 12*
   - Read: §3, "the capitalist's grounds for compensation".
   - Do: list the compensations (risk, turnover, skill) a capitalist claims and show each as a redistribution within a fixed total profit.
   - Lab: `prices`, view `production`. Presets: `risk-premium`, `turnover-premium`, `none`. Pin `ppTotals`.
   - Misconception: each compensation adds new profit.
   - Worked: give one sphere a 2% risk premium and the others' share of total s falls by the same amount.

6. **the-law-as-such** — The Falling Rate of Profit: The Law as Such — *Chapter 13*
   - Read: the table "s′ = 100%: c = 50, v = 100 → p′ = 66⅔%; c = 100 → 50%; c = 200 → 33⅓%; c = 300 → 25%; c = 400 → 20%".
   - Do: compute p′ for a rising c/v at constant s′, and the mass of profit when total capital grows.
   - Lab: `tendency`, view `law`. Presets: `marx` (Marx's figures), `growing-mass` (capital doubling while p′ falls), `steady`. Pin `teRate`, `teMass`.
   - Misconception: a falling rate of profit means falling profits.
   - Worked: 66⅔% falls to 20% while the mass of profit can double if capital more than triples.

7. **counteracting-influences** — Counteracting Influences — *Chapter 14*
   - Read: "Increasing intensity of exploitation… Depression of wages… Cheapening of elements of constant capital… Relative over-population… Foreign trade… The increase of stock capital".
   - Do: apply each counteracting factor to the law's sequence and compute how much of the fall it offsets.
   - Lab: `tendency`, view `counter`. Presets: `rising-s`, `cheap-c`, `combined`. Pin `teRate`, `teOffset`.
   - Misconception: the counteracting factors refute the law.
   - Worked: raising s′ from 100% to 150% holds p′ at 25% when c/v rises from 3 to 5 — and cannot go on doing so indefinitely.

8. **internal-contradictions-of-the-law** — The Internal Contradictions of the Law — *Chapter 15*
   - Read: "The real barrier of capitalist production is capital itself."
   - Do: compute when additional capital adds no additional profit (absolute over-accumulation) and the devaluation that restores the rate.
   - Lab: `tendency`, view `overaccumulation`. Presets: `marx` (the case where extra capital C yields no more than before), `devalue` (a third of capital destroyed), `mild`. Pin `teMass`, `teRate`.
   - Misconception: crises come from a shortage of capital.
   - Worked: add 100 to a capital of 500 and get the same 100 of profit: p′ falls from 20% to 1/6, and "superfluous" capital follows.

### Course 11 — Merchant's Capital and Interest (`capital-merchants-and-interest`, 9)

1. **commercial-capital** — Commercial Capital — *Chapter 16*
   - Read: "Commercial capital… is nothing but the converted form of a portion of… capital in circulation."
   - Do: compute the capital an industrialist saves by selling to a merchant and the merchant capital needed to circulate a product.
   - Lab: `turnover`, view `merchant`. Presets: `no-merchant`, `merchant`, `faster-merchant`. Pin `tuAdvance`.
   - Misconception: merchants produce value by moving goods from hand to hand.
   - Worked: a merchant who turns over £100 five times frees £500 of the industrialists' circulating capital.

2. **commercial-profit** — Commercial Profit — *Chapter 17*
   - Read: the example "720c + 180v + 180s… merchant's capital of 100".
   - Do: compute the general rate of profit including the merchant's capital, the price at which the industrialist sells to the merchant, and the merchant's selling price.
   - Lab: `prices`, view `merchant`. Presets: `marx` (Marx's figures: industrial 900, merchant 100, s = 180), `no-merchant`, `with-costs` (merchant's own circulation costs). Pin `ppAverage`, `ppMerchantPrice`.
   - Misconception: the merchant's profit is a mark-up added on top of value.
   - Worked: 180 of s on 1,000 of capital is 18%; the industrialist sells at 1,062, the merchant at 1,080, which is the value.

3. **the-turnover-of-merchants-capital** — The Turnover of Merchant's Capital — *Chapter 18*
   - Read: the merchant's turnover and "the commercial profit on each turnover".
   - Do: compute the mark-up per turnover from the general rate and the merchant's turnovers a year.
   - Lab: `prices`, view `merchant-turnover`. Presets: `once`, `ten`, `grocer`. Pin `ppMarkup`.
   - Misconception: a faster-turning merchant earns a higher rate of profit.
   - Worked: at 15% a year, a merchant who turns over 10 times adds 1½% to each sale.

4. **money-dealing-capital** — Money-Dealing Capital — *Chapter 19*
   - Read: "the purely technical movements that money undergoes".
   - Do: compute the money-dealer's share of profit from the capital tied up in payments, cash-keeping and exchange.
   - Lab: `prices`, view `merchant`. Presets: `cashier`, `exchange`, `none`. Pin `ppAverage`.
   - Misconception: money-dealing creates value because it handles value.
   - Worked: money-dealing capital of 50 joins the averaging and draws 9 at 18%.

5. **history-of-merchants-capital** — Historical Facts about Merchant's Capital — *Chapter 20*
   - Read: "Merchant's capital is originally merely the intervening movement between extremes which it does not control."
   - Do: compute a pre-capitalist merchant's profit from buying cheap in one community and selling dear in another, beside the capitalist merchant's average profit.
   - Lab: `circuit`, view `markup`, with `between = communities`. Presets: `venice`, `dutch`, `capitalist`. Pin `ciDelta`.
   - Misconception: merchant capital always tended to develop into industrial capital.
   - Worked: buying at 60 and selling at 100 in a market with no equalisation yields 40, which no general rate limits.

6. **interest-bearing-capital** — Interest-Bearing Capital — *Chapter 21*
   - Read: "a man has £100 at his disposal… the capacity of producing a profit of £20".
   - Do: compute what the lender's £100 lets a borrower make at the average rate and the interest paid out of it.
   - Lab: `interest`, view `split`. Presets: `marx` (Marx's figures: £100, 20% average profit, £5 interest), `high-rate`, `low-rate`. Pin `inInterest`, `inEnterprise`.
   - Misconception: interest is the price of money.
   - Worked: £100 makes £20 at the average rate; £5 goes to the lender and £15 stays with the borrower as profit of enterprise.

7. **the-rate-of-interest** — The Rate of Interest — *Chapter 22*
   - Read: "There is no such thing as a natural rate of interest."
   - Do: compute interest and profit of enterprise across rates and show the bounds 0 < i < p′.
   - Lab: `interest`, view `bounds`. Presets: `crisis` (interest near the profit rate), `plenty` (interest near zero), `normal`. Pin `inEnterprise`, `inBound`.
   - Misconception: there is a natural rate of interest set by productivity.
   - Worked: at a 20% average rate the rate of interest can be anything below 20%; competition, not nature, decides where.

8. **interest-and-profit-of-enterprise** — Interest and Profit of Enterprise — *Chapter 23*
   - Read: the "wages of superintendence" and the capitalist who borrows.
   - Do: split gross profit into interest and profit of enterprise and separate the wages of a hired manager from both.
   - Lab: `interest`, view `split`. Presets: `owner`, `borrower`, `manager` (a hired manager paid a salary). Pin `inEnterprise`, `inInterest`.
   - Misconception: profit of enterprise is the capitalist's wage for managing.
   - Worked: with £5 of interest and £15 of profit of enterprise, a £6 manager's salary leaves £9 that no one worked for.

9. **interest-bearing-capital-as-a-thing** — Interest-Bearing Capital as a Thing — *Chapter 24*
   - Read: Dr. Price's "one penny, put out at our Saviour's birth at 5 per cent compound interest".
   - Do: compute Price's compound sum and compare it with the accumulation of real capital at a stated rate, and say why the first is impossible.
   - Lab: `interest`, view `compound`. Presets: `price` (a penny at 5% over a stated span), `real` (a capital growing with the product), `ten-years`. Pin `inCompound`, `inReal`.
   - Misconception: money left at interest grows by itself.
   - Worked: the compound sum outgrows any real product in a few centuries; interest can only be a share of a surplus that labour produces.

### Course 12 — Credit and Fictitious Capital (`capital-credit-and-fictitious-capital`, 12)

1. **credit-and-fictitious-capital** — Credit and Fictitious Capital — *Chapter 25*
   - Read: bills of exchange as "commercial money".
   - Do: compute the circulation of a chain of bills and the cash needed when they are settled or discounted.
   - Lab: `money`, view `payments`. Presets: `bills`, `discounted`, `accommodation` (bills drawn without a sale behind them). Pin `moNeeded`, `moNetted`.
   - Misconception: a bill of exchange is a loan of money.
   - Worked: three bills of £100 in a circle settle with no cash; one accommodation bill with no sale leaves £100 of claims against nothing.

2. **accumulation-of-money-capital** — Accumulation of Money Capital and the Rate of Interest — *Chapter 26*
   - Read: Overstone's evidence before the Committee of 1857.
   - Do: compute what a rise in the rate of interest does to profit of enterprise and to the borrowing industrialist.
   - Lab: `interest`, view `bounds`. Presets: `overstone-low`, `overstone-high`, `crisis`. Pin `inEnterprise`.
   - Misconception: a high rate of interest shows a scarcity of capital in general.
   - Worked: at a 10% average rate, moving interest from 3% to 8% cuts profit of enterprise from 7 to 2 per 100.

3. **the-role-of-credit** — The Role of Credit in Capitalist Production — *Chapter 27*
   - Read: "Formation of stock companies", "the abolition of the capitalist mode of production within the capitalist mode of production itself".
   - Do: compute dividends paid as interest on share capital and the profit of enterprise that remains, and say what that does to the figure of the owner.
   - Lab: `interest`, view `split`. Presets: `stock-company`, `owner-managed`, `leveraged` (most capital borrowed). Pin `inEnterprise`, `inInterest`.
   - Misconception: joint-stock companies are owned and run by their shareholders as a capitalist runs a firm.
   - Worked: when shareholders get 5% on £1,000 of a 20% business, £150 a year stays with the company and its managers.

4. **medium-of-circulation-and-capital** — Medium of Circulation and Capital: Tooke and Fullarton — *Chapter 28*
   - Read: the distinction between money as currency and money as capital.
   - Do: classify payments as circulation of revenue or transfer of capital and compute the notes each needs.
   - Lab: `money`, view `circulate`. Presets: `revenue` (wages spent in shops), `capital` (payments between capitalists), `mixed`. Pin `moNeeded`.
   - Misconception: the quantity of notes measures the quantity of capital.
   - Worked: £1,000 of wage spending at velocity 10 needs £100 of notes; £1,000 lent to a manufacturer needs none extra once it is spent.

5. **component-parts-of-bank-capital** — The Component Parts of Bank Capital — *Chapter 29*
   - Read: "The formation of a fictitious capital is called capitalisation."
   - Do: compute the price of a claim to a yearly income at a rate of interest, and what a change in the rate does to it with nothing real changing.
   - Lab: `interest`, view `capitalise`. Presets: `marx` (Marx's figures: £100 a year at 5%), `rate-up`, `rate-down`. Pin `inPrice`.
   - Misconception: the price of a security measures real capital invested.
   - Worked: £100 a year at 5% is £2,000; at 10% the same claim is £1,000 and nothing has been destroyed.

6. **money-capital-and-real-capital-i** — Money Capital and Real Capital I — *Chapter 30*
   - Read: "the accumulation of loan capital… is not identical with real accumulation".
   - Do: compute idle money capital in a slump against real capital stock, and show they can move in opposite directions.
   - Lab: `interest`, view `cycle`. Presets: `slump` (deposits high, investment low), `boom`, `crash`. Pin `inLoanCapital`, `inRate`.
   - Misconception: a pile of bank deposits means plenty of real capital.
   - Worked: in the slump preset loan capital doubles while production falls by a fifth.

7. **money-capital-and-real-capital-ii** — Money Capital and Real Capital II — *Chapter 31*
   - Read: "the transformation of money into loan capital".
   - Do: trace how a hoard, a revenue and a release of circulating capital each become loan capital, and compute the total.
   - Lab: `interest`, view `cycle`. Presets: `hoards`, `revenues`, `released`. Pin `inLoanCapital`.
   - Misconception: loan capital is only savings out of income.
   - Worked: circulating capital set free as a business contracts becomes loan capital without anyone saving a penny.

8. **money-capital-and-real-capital-iii** — Money Capital and Real Capital III — *Chapter 32*
   - Read: the demand for means of payment "in times of crisis".
   - Do: compute the rate of interest the crisis preset reports beside the profit rate and the scramble for cash.
   - Lab: `interest`, view `cycle`. Presets: `prosperity`, `crisis`, `recovery`. Pin `inRate`, `inEnterprise`.
   - Misconception: in a crisis capital is scarce.
   - Worked: in the crisis preset commodities are abundant and money as means of payment is not; interest rises above the rate of profit.

9. **the-medium-of-circulation-in-the-credit-system** — The Medium of Circulation in the Credit System — *Chapter 33*
   - Read: "the quantity of notes in circulation… determined by the requirements of business".
   - Do: compute the notes the circulation needs and what happens to an over-issue.
   - Lab: `money`, view `circulate`. Presets: `needs`, `over-issue` (notes return to the bank), `crisis-demand`. Pin `moNeeded`, `moReturned`.
   - Misconception: the bank decides how much money circulates.
   - Worked: issue £200 of notes where circulation needs £150 and £50 flows back as deposits or repayments.

10. **the-currency-principle-and-the-bank-act** — The Currency Principle and the Bank Act of 1844 — *Chapter 34*
    - Read: Overstone's currency principle and the suspension of the Act in 1847 and 1857.
    - Do: compute the note issue the 1844 Act allowed against gold, and the gap in a drain when the circulation's needs do not fall.
    - Lab: `money`, view `bank-act`. Presets: `normal`, `drain` (gold leaves), `suspension`. Pin `moCap`, `moGap`.
    - Misconception: tying notes to gold stabilises the circulation.
    - Worked: a fixed fiduciary issue plus gold reserve caps notes; a £5m drain cuts the cap by £5m when the demand for means of payment is rising.

11. **precious-metal-and-the-rate-of-exchange** — Precious Metal and the Rate of Exchange — *Chapter 35*
    - Read: §2, "the rate of exchange… the barometer for the international movement of the money metals".
    - Do: compute the net balance and the bullion shipped when exchanges move past the gold points.
    - Lab: `money`, view `world`. Presets: `balanced`, `india-drain`, `harvest-failure`. Pin `moDrain`.
    - Misconception: a gold outflow means the country is getting poorer.
    - Worked: £8m of imports against £6m of exports and £1m of other receipts leaves £1m to be paid in gold.

12. **pre-capitalist-relationships** — Pre-Capitalist Relationships — *Chapter 36*
    - Read: "Usurer's capital… ruins this small-scale production".
    - Do: compute a small producer's surplus against the usurer's interest and the point at which the producer's means of production are forfeit.
    - Lab: `interest`, view `usury`. Presets: `peasant` (illustrative: a holding producing a small surplus, debt at a usurious rate), `artisan`, `lord` (a spendthrift landlord). Pin `inYearsToRuin`.
    - Misconception: usury is high interest on loans for production.
    - Worked: a surplus of 10 a year against interest of 15 on a debt of 50 adds 5 a year to the debt; the lab prints the year the debt exceeds the holding.

### Course 13 — Ground Rent (`capital-ground-rent`, 11)

1. **introductory-remarks-on-rent** — Introductory Remarks on Ground Rent — *Chapter 37*
   - Read: "the price of land… is nothing but the capitalised rent".
   - Do: compute the price of land from rent and the rate of interest, and separate true rent from interest on capital sunk in the land.
   - Lab: `rtnt`, view `price`. Presets: `marx` (Marx's figures: rent £200 at 5%), `improvements` (part of the payment is interest on drains and buildings), `rate-falls`. Pin `rtPrice`, `rtTrueRent`.
   - Misconception: rent is the return on the land's value.
   - Worked: £200 a year at 5% is a price of £4,000; when the rate falls to 4% the same land costs £5,000.

2. **differential-rent-general** — Differential Rent: General Remarks — *Chapter 38*
   - Read: the waterfall: the factory with water power against those on steam.
   - Do: compute the surplus profit of the capital with a monopolisable natural advantage and say why it becomes rent.
   - Lab: `rtnt`, view `waterfall`. Presets: `marx` (Marx's figures: cost price 100 on steam against 90 on water, average profit 15%), `two-falls`, `steam-cheapens`. Pin `rtSurplusProfit`.
   - Misconception: the waterfall creates the surplus profit.
   - Worked: price of production 115 against a cost of 90: the 15% average profit on 90 and the remainder a surplus profit that the owner of the fall can claim.

3. **differential-rent-i** — Differential Rent I — *Chapter 39*
   - Read: the table of soils A, B, C, D.
   - Do: compute rent on each of four soils from equal capitals and unequal yields at the price regulated by the worst soil, and the total rent.
   - Lab: `rtnt`, view `dr1`. Presets: `marx` (Marx's figures: 1, 2, 3, 4 quarters; 60s a quarter), `descending` (worse soil added last), `better-added`. Pin `rtRents`, `rtTotal`.
   - Misconception: rent arises because the worst land is too poor to farm without it.
   - Worked: at 60s a quarter, A pays no rent, B 60s, C 120s, D 180s; 360s of rent in all.

4. **differential-rent-ii** — Differential Rent II — *Chapter 40*
   - Read: successive investments of capital "on the same land".
   - Do: compute rent from successive equal investments on one plot with falling or rising yields, against the regulating price.
   - Lab: `rtnt`, view `dr2`. Presets: `diminishing`, `constant`, `increasing`. Pin `rtRents`, `rtTotal`.
   - Misconception: DR II is a different source of rent from DR I.
   - Worked: two investments on soil D yielding 4 and 3 quarters pay 180s and 120s of surplus profit at 60s.

5. **dr-ii-constant-price** — Differential Rent II at a Constant Price of Production — *Chapter 41*
   - Read: "First case: constant price of production".
   - Do: compute total rent when added capital raises output and the regulating price does not change.
   - Lab: `rtnt`, view `dr2`, `case = constant`. Presets: `proportional`, `faster`, `slower`. Pin `rtTotal`.
   - Misconception: more output always lowers rent per acre.
   - Worked: doubling the capital on each rent-bearing soil at the same productivity doubles the rent per acre.

6. **dr-ii-falling-price** — Differential Rent II at a Falling Price of Production — *Chapter 42*
   - Read: "Second case: falling price of production".
   - Do: compute rents when the additional investment is more productive and the regulating price falls.
   - Lab: `rtnt`, view `dr2`, `case = falling`. Presets: `a-drops-out`, `rtnt-rises`, `rtnt-falls`. Pin `rtTotal`, `rtPrice`.
   - Misconception: a falling price must lower total rent.
   - Worked: the lab prints a case in which price falls and total rent still rises.

7. **dr-ii-rising-price** — Differential Rent II at a Rising Price of Production — *Chapter 43*
   - Read: "Third case: rising price of production. Results".
   - Do: compute rents when the additional investment is less productive and the regulating price rises.
   - Lab: `rtnt`, view `dr2`, `case = rising`. Presets: `worse-investment`, `new-soil`, `rtsults`. Pin `rtTotal`, `rtPrice`.
   - Misconception: rent is the cause of high food prices.
   - Worked: price rises because the least productive investment regulates it; rent follows the price, not the other way round.

8. **rent-on-the-worst-soil** — Differential Rent Also on the Worst Cultivated Soil — *Chapter 44*
   - Read: the case in which the least productive investment is on a better soil.
   - Do: compute when the worst soil A pays a differential rent because price is regulated by a second, less productive investment elsewhere.
   - Lab: `rtnt`, view `dr2`, `case = worst-soil`. Presets: `marx`, `none`, `both`. Pin `rtRents`.
   - Misconception: the worst soil can never pay differential rent.
   - Worked: if the regulating investment is a second dose on B yielding less than A's first, A pays rent too.

9. **absolute-ground-rent** — Absolute Ground Rent — *Chapter 45*
   - Read: "landed property… prevents the equalisation of capitals".
   - Do: compute value and price of production for agriculture with a lower composition and the absolute rent the difference allows.
   - Lab: `rtnt`, view `absolute`. Presets: `low-composition` (60c + 40v at 100%, average rate 20%), `average-composition` (no absolute rent possible), `market-limited`. Pin `rtAbsolute`.
   - Misconception: absolute rent is a monopoly price that can be set at will.
   - Worked: value 140 against price of production 120: up to 20 of absolute rent without any price above value.

10. **building-rent-mining-rent-land-price** — Building Rent, Mining Rent, the Price of Land — *Chapter 46*
    - Read: "the land-owner… pockets the fruits of social development without contributing anything".
    - Do: compute a building plot's rent and price as the city grows, and a mine's rent from its deposit.
    - Lab: `rtnt`, view `price`. Presets: `town-grows`, `mine`, `speculation`. Pin `rtPrice`.
    - Misconception: a rising land price reflects improvements made by the owner.
    - Worked: a plot's rent rises from £50 to £150 as the town reaches it; at 5% its price goes from £1,000 to £3,000.

11. **genesis-of-capitalist-ground-rent** — Genesis of Capitalist Ground Rent — *Chapter 47*
    - Read: §2, labour rent: "the labour of the direct producer for himself and his labour for the landlord are… separated by time and space".
    - Do: compute the rate of exploitation in labour rent (days on the lord's land against days on one's own), and compare rent in kind and money rent.
    - Lab: `workday`, view `corvee`. Presets: `three-three` (3 days for the lord, 3 for oneself), `four-two`, `money-rent`. Pin `wdRate`.
    - Misconception: feudal exploitation was hidden while capitalist exploitation is visible.
    - Worked: 3 days for the lord and 3 for oneself is visibly 100%; the wage-worker's 6 hours in 12 is the same rate, invisible.

### Course 14 — Revenues and Their Sources (`capital-revenues-and-their-sources`, 5)

1. **the-trinity-formula** — The Trinity Formula — *Chapter 48*
   - Read: "Capital — profit (profit of enterprise plus interest), land — ground rent, labour — wages, this is the trinity formula".
   - Do: decompose a year's v + s into wages, profit of enterprise, interest and rent, and show that all three "revenues" come from one value product.
   - Lab: `rvvenue`, view `trinity`. Presets: `english` (illustrative), `no-landlord`, `all-borrowed`. Pin `rvWages`, `rvRent`, `rvInterest`.
   - Misconception: each factor of production creates its own income.
   - Worked: a value product of 200 is 100 wages, 30 rent, 20 interest and 50 profit of enterprise; land and capital have added nothing to the 200.

2. **analysis-of-the-process-of-production** — Analysis of the Process of Production — *Chapter 49*
   - Read: the annual product's value and the annual revenue, and "the dogma".
   - Do: compute the annual product's c + v + s against revenues v + s, and show why the product cannot all be bought out of revenues.
   - Lab: `rvvenue`, view `dogma`. Presets: `marx-scheme`, `growing`, `one-sector`. Pin `rvTotal`, `rvSmith`.
   - Misconception: annual income equals the annual product.
   - Worked: 9,000 of product against 3,000 of revenue; the 6,000 is constant capital that must be replaced from the product itself.

3. **illusions-created-by-competition** — Illusions Created by Competition — *Chapter 50*
   - Read: price "appears" to be formed by adding wages, profit and rent.
   - Do: compute price both ways — value resolved into parts, and parts added up — and show the second is circular.
   - Lab: `rvvenue`, view `added-up`. Presets: `wage-rise`, `rvnt-rise`, `fixed-value`. Pin `rvWages`, `rvProfitShare`.
   - Misconception: a wage rise raises prices because wages are a component added to them.
   - Worked: with value product fixed at 200, a wage rise from 100 to 120 cuts profit, interest and rent by 20 together.

4. **distribution-and-production-relations** — Distribution Relations and Production Relations — *Chapter 51*
   - Read: "the so-called distribution relations… are the reverse side of these production relations".
   - Do: compute the same product's distribution under two production relations (a wage relation and an association of producers) and say what changes and what does not.
   - Lab: `rvvenue`, view `trinity`. Presets: `capitalist`, `association`, `cooperative`. Pin `rvWages`, `rvProfitShare`.
   - Misconception: distribution can be changed without changing production relations.
   - Worked: the association preset keeps c for replacement and a fund for expansion; only the split of v + s and who decides it change.

5. **classes** — Classes — *Chapter 52*
   - Read: the manuscript's last lines, "What makes a class?" — and where it breaks off.
   - Do: classify incomes in a small society by their source (wages, profit, rent) and say why Marx's answer cannot be "the source of income" alone.
   - Lab: `rvvenue`, view `classes`. Presets: `three-classes`, `doctor-and-official`, `mixed-incomes`. Pin `rvClassCount`.
   - Misconception: a class is defined by the size of its income.
   - Worked: a doctor and a factory owner may have equal incomes from different sources; the chapter stops as Marx says so.

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
  the page shows. It is not a `<select>`. An unknown view raises.
- **Units.** Every mode takes `cfg["unit"]` from `{"hours", "s", "d", "£",
  "qr"}` and prints it after every money or time figure (`30s`, `£422`,
  `9/5 h`). Mixed units inside one preset are refused at build time. Shillings
  and pence are separate units; a preset never mixes them. A tile never
  converts.
- **Percentages.** A rate prints as the exact fraction and its percentage to
  at most two decimals when it is not whole: `1/1 = 100%`, `2/3 = 66.67%`,
  `11/50 = 22%`. Marx's `66⅔%` is quoted in prose, never produced by a tile.
- **Periods.** Modes that iterate (`accumulate`, `schemes`, `tendency`) take a
  shipped `periods` (1–10) and print one row per period in a table
  (`XXTable`), plus the pinned tiles for the last period. More than 10 periods
  is refused.
- **Size limits.** At most 8 producers, 6 commodities, 6 spheres, 6 soils, 10
  capitals, 12 ledger items. Exceeding a limit is refused with the limit named.

### D.1 Modes (capkit.py)

Each entry: cfg instance fields; views; tiles (id: format).

#### value
- Instance: `producers: [{name, hours, output}]` (hours per unit or total, as
  `basis: "per-unit" | "total"`), `skill` (multiplier for complex labour,
  default 1), `lot` (units valued), for view `ledger` `items: [{name, hours,
  output}]`, for view `market` `groups: [{units, hours}]`.
- Views: `snlt` (default), `skill`, `ledger`, `market`.
- Tiles: `vaSnlt` (`9/5 h` per unit), `vaLotValue` (`lot × snlt`), `vaPerUnit`,
  `vaTotalHours`, `vaMarketValue`, `vaSurplus` (per group, comma-separated in
  input order, signed: `+1 h, 0 h, −1 h`).

#### form
- Instance: `goods: [{name, qty, unit, hours}]`, `equivalent` (a good's name).
- Views: `stage` with shipped `stage` ∈ `elementary | expanded | general |
  money` (a redraw-only select, cfg key `stage`), and `count`.
- Tiles: `foEquation` (the equations of the selected stage, `;`-separated,
  quantities exact), `foGeneral` (the general equivalent's name), `foPairs`
  (bilateral ratios needed, n·(n − 1)/2), `foWithEquivalent` (n − 1).
- Build-time check: every equation in `marx` must balance in hours; a preset
  whose quantities do not balance is refused, which is how Marx's figures are
  kept honest.

#### money
- Instance: `goods: [{name, value_hours}]`, `gold_hours_per_unit`, `velocity`,
  `credit_sales`, `payments_due`, `cancelling`, `imports`, `exports`,
  `other_receipts`, `rent`, `price_index`, `wage_index`, `reserve`,
  `fiduciary`, `demand`.
- Views: `circulate`, `payments`, `world`, `fixed-rent`, `bank-act`.
- Tiles: `moPriceSum`, `moNeeded` (Marx's ch. 3 §3b formula: (price sum −
  credit sales + payments due − cancelling payments) / velocity),
  `moNetted`, `moDrain` (imports − exports − other receipts, floored at 0, with
  the direction stated), `moRealRent` (rent / price index), `moFarmerGain`,
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
- Views: `mill`, `transfer`, `rate`, `parts`, `mass`, `formulae`.
- Tiles: `suProduct` (c + v + s), `suS`, `suRate` (s/v), `suParts` (the product
  in parts: `c: 20 lb, v: 2 lb, s: 2 lb` style, units from the instance),
  `suTransfer`, `suMass` (s′ × v × workers), `suFalse` (s/(v + s)).

#### workday
- Instance: `day`, `necessary`, `productivity` (factor on wage-goods),
  `intensity` (factor), `limit` (legal hours), `pioneer_productivity`,
  `family_workers`, `own_land` (boolean: all hours necessary to the producer),
  `lord_days`, `own_days`.
- Views: `absolute`, `limit`, `relative`, `intensity`, `classify`, `three`
  (with redraw-only `hold`), `separate`, `corvee`.
- Tiles: `wdSurplus`, `wdRate`, `wdExtra` (the pioneer's extra surplus value
  per day), `wdLpValue`, `wdKind` (`absolute`, `relative`, `both`, `none`).
- Draws the day as one bar cut at the necessary time, with the surplus part
  labelled; the bar is SVG in the existing lab chrome, both themes.

#### machine
- Instance: `workers`, `output_each`, `cooperation_gain`, `steps: [{name,
  rate}]`, `machine_value`, `machine_life_units`, `wages_displaced`,
  `labour_saved_value`, `capital`, `variable`, `wage_each`, `discharged`,
  `machine_spend`, `mb_composition` (machine-building's c/v).
- Views: `cooperate`, `detail`, `adopt`, `displace`.
- Tiles: `maOutput`, `maGain`, `maWorkers` (per step, comma-separated),
  `maMinimum`, `maPerUnit`, `maVerdict` (`adopted`, `not adopted`: the
  capitalist's test is machine cost < wages displaced, and the tile says which
  test), `maDisplaced`, `maReemployed`.

#### wages
- Instance: `lp_value` (daily), `normal_hours`, `hours_worked`,
  `value_per_hour`, `pieces_normal`, `pieces_actual`, `rate_cut_to`, for view
  `national` two countries' `{wage, output_per_hour}`, for view `statute`
  `{statutory_wage, lp_value, day, necessary}`.
- Views: `form`, `time`, `piece`, `national`, `statute`.
- Tiles: `waHourPrice`, `waValueCreated`, `waDaily`, `waPieceRate`,
  `waRelative` (wage per unit of output, country A over country B), `waGap`,
  `waRate` (the rate of surplus value the statute enforces).

#### accumulate
- Instance: `capital`, `c_v` (composition), `s_rate`, `accumulate_share`,
  `consumed_per_year`, `composition_rise` (added to c/v per period),
  `labour_supply`, `supply_growth`, `wage_per_worker`, `capitals: [n]`
  (for `centralise`), `merge_rule` (`largest-absorbs-smallest | none`),
  `colonists`, `land_price_years`.
- Views: `simple`, `expand`, `labour`, `composition`, `law`, `centralise`,
  `colony`.
- Tiles: `acYears` (capital / consumed per year), `acCapital`,
  `acShareOriginal` (original capital as a share of the present capital),
  `acDemand` (workers employed: v / wage), `acReserve` (supply − demand,
  floored at 0), `acRatio` (reserve / employed), `acTopShare`, `acCount`,
  `acYearsToLand`.

### D.2 Modes (capkit_b.py)

#### turnover
- Instance: `working_weeks`, `production_weeks`, `circulation_weeks`,
  `weekly_outlay`, `stage_weeks: [money, productive, commodity]`, `fixed:
  [{name, value, life_years}]`, `circulating`, `circ_turnovers`, `variable`,
  `s_rate`, `items: [{name, value, fixed: bool, variable: bool}]`,
  `merchant_capital`, `merchant_turnovers`.
- Views: `time`, `phases`, `fixed`, `aggregate`, `classify`, `working`,
  `advance`, `annual`, `merchant`.
- Tiles: `tuTurnover` (weeks), `tuTurnovers` (52 / turnover weeks, exact),
  `tuWorkingShare`, `tuMoney`, `tuProductive`, `tuCommodity` (shares), `tuWear`,
  `tuRemaining`, `tuAggregate`, `tuAverage`, `tuFixed`, `tuVariable` (sums by
  each classification), `tuAdvance`, `tuFreed`, `tuAnnualRate` (s′·n),
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
  rate is recomputed over the same total capital. The lesson checks the
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
  `holding_value`, `deposits_by_phase`, `investment_by_phase`, `phase`.
- Views: `split`, `bounds`, `capitalise`, `compound`, `cycle`, `usury`.
- Tiles: `inInterest`, `inEnterprise`, `inBound` (`0 < i < p′` with the
  values, or the breach), `inPrice` (income / rate), `inCompound`, `inReal`,
  `inLoanCapital`, `inRate`, `inYearsToRuin` (first year debt > holding, or
  `never within n years`).
- `compound` prints its sum with BigInt numerators and, beside the exact value,
  the number of decimal digits — a penny at 5% for 1,780 years is not a number
  to print in full.

#### rent
- Instance: `soils: [{name, capital, outputs: [qr per investment]}]`,
  `profit_rate`, `price_case` (`constant | falling | rising | worst-soil`),
  `regulating` (which investment regulates, or `auto` = least productive in
  use), `rent`, `interest_rate`, `improvement_interest`, `cost_steam`,
  `cost_water`, `agri: {c, v}`, `s_rate`, `market_limit`.
- Views: `price`, `waterfall`, `dr1`, `dr2`, `absolute`.
- Tiles: `rtPrice` (land price or regulating price, by view), `rtTrueRent`,
  `rtSurplusProfit`, `rtRents` (per soil, in input order), `rtTotal`,
  `rtAbsolute`.

#### revenue
- Instance: `c`, `v`, `s`, `split: {interest, rent}` (shares of s),
  `wage_change`, `people: [{name, wages, profit, rent}]`.
- Views: `trinity`, `dogma`, `added-up`, `classes`.
- Tiles: `rvTotal` (c + v + s), `rvSmith` (v + s, the dogma's total, with the
  missing c), `rvWages`, `rvRent`, `rvInterest`, `rvProfitShare` (profit of
  enterprise), `rvClassCount` (people grouped by their largest source).

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

- **Sources.** Volume I: the Moore–Aveling translation (1887). Volumes II and
  III: the Untermann translation (Kerr, 1907 and 1909). Both are in the public
  domain and both are on marxists.org (`/archive/marx/works/1867-c1/`,
  `1885-c2/`, `1894-c3/`), whose chapter files name their translators. Never
  quote the Fowkes or Fernbach (Penguin) translations: they are in copyright.
- **Fetch, then quote.** Fetch the chapter page with WebFetch, ask for the
  passage verbatim, and fetch it a second time with a differently worded
  request. Quote only text the two fetches agree on character for character.
  Keep the quotation under 120 words.
- **Shape.** The first `body` block is a `p`:
  `<strong>Volume I, Chapter 1, §1.</strong> &ldquo;…&rdquo;` — volume,
  chapter and section, then the quotation, nothing else. A second short
  quotation may appear later in the body the same way.
- **Translator's spellings stand** inside quotation marks ("labour-power",
  "valorisation" is not in Moore–Aveling: they write "creation of
  surplus-value"); the lesson's own prose uses the Subject's spellings
  (British, "labour-power", "surplus value" unhyphenated as a noun).

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
   snooze and endless when you hold a plank. Here: a lesson may open its
   explanation with one concrete scene — a payslip, a rent cheque, a till
   receipt, a mortgage — and must reach the chapter's category within the
   paragraph.
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
   lesson's `note` says what the chapter assumes and what the lab cannot
   settle — that commodities sell at value until Volume III, that the
   illustrative figures are illustrative, that a disputed reading is disputed.
7. **They close by pointing forward.** Each lecture ends with what next week
   is about. Here: the last `p` of the body names the question the next
   chapter answers, in one sentence and by the next lesson's title. It does not
   say "next week" and it does not summarise the lesson.

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
Valorisation Process”, after the passage):

> Think about the last thing you bought that was made in a factory. Its price
> had to cover the materials, the wear on the machines and the wages, and you
> would expect it to cover them exactly if nobody cheated. That is the puzzle
> Marx sets up with his spinner. Ten pounds of cotton at 10s, 2s of wear on the
> spindle, six hours of spinning: the yarn is worth 15s, and the capitalist who
> paid 3s for a day's labour-power and 12s for the rest has made nothing. He
> "stares in astonishment", Marx writes, and starts to complain about his
> abstinence. Then the day is lengthened to twelve hours. The lab does the same
> sum twice: 27s goes in, yarn worth 30s comes out, and every input was bought
> at its value. Nobody cheated. The 3s came from the difference between what a
> day of labour-power costs and what a day of labour makes.

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
