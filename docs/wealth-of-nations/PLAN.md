# The Wealth of Nations, Read Along — the build specification

The curriculum, lab and authoring contract for the nineteenth Subject: a
read-along of Adam Smith, *An Inquiry into the Nature and Causes of the Wealth
of Nations* (first published 1776), all five Books in Smith's own order, one
lesson for a chapter or for a Part of a long one. The operator attached the
text and asked for it the same way as the previous read-alongs, all the way to
live.

It is built the way *Capital* (`docs/capital/PLAN.md`) and *Accelerate*
(`docs/accelerate/PLAN.md`) were, and adopts their conventions by reference
wherever this one is silent. Read before this: `AGENTS.md` §0, §1, §1a, §7, §8;
`content/AGENTS.md`; `docs/capital/AUTHORING.md` (its review lessons apply
here word for word, with Smith for Marx).

**Capital is this Subject's nearest neighbour, and the two must not repeat
each other.** Marx argues with Smith on nearly every page of Volume I, and
Capital's lessons introduce Smith at the moment Marx argues with him. Here
Smith speaks first and in his own terms: labour commanded, the component parts
of price, natural and market price, productive and unproductive labour. A
lesson that meets a point Capital takes up (the "dogma" that price resolves
into wages, profit and rent; productive labour; the division of labour in
manufacture) names the Capital lesson by title in one sentence and does not
repeat its prose or its argument.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit · §E package, text, quoting · §F voice · §G left out

---

## §0 The one question: what does the reader compute?

The Wealth of Nations reasons with numbers on almost every page: pins a day,
shillings a week, pence an ounce, years' purchase, a bounty of five shillings
the quarter, one man in a hundred under arms. The reader computes what Smith's
reasoning implies for stated quantities, Smith's own figures where the chapter
gives them and figures written for the lesson where it does not:

1. **Output and its division.** Produce per head from the share of people at
   useful work and the output of each; output per worker when an operation is
   divided; what two producers gain by each keeping to one trade; how many
   specialists a market of a given size can keep (Introduction, I.1–I.3).
2. **Money and the measure of value.** How many exchange ratios a market needs
   without money and with it; the silver in a penny as the pound is debased;
   a price in money against a price in labour or in corn over years (I.4–I.5).
3. **Price.** A price resolved into wages, profit and rent through the stages
   of production, and why a rise in profit raises it more than a rise in wages;
   the market price against the natural price when more or less is brought to
   market than the effectual demand (I.6–I.7, I.9).
4. **Wages, profit, employments.** A family's subsistence against a wage; the
   wage when the funds destined for maintaining labour grow faster or slower
   than the workers; population doubling; the net advantages of employments;
   the lottery of a profession; the apothecary's profit split into wages and
   profit (I.8–I.10).
5. **Rent and silver.** Rent as the residual after wages and ordinary profit,
   land by land and mine by mine; whether a tenant gains from an improvement
   under each tenure; the price of corn in silver averaged by period (I.11,
   III.2).
6. **Stock.** A stock divided into consumption, fixed and circulating parts;
   gross and net revenue; capital that grows by parsimony or shrinks by
   prodigality; the labour a capital puts in motion by how often it returns;
   what a great proprietor's revenue maintains (II, III.4).
7. **Banks.** The gold a paper currency displaces and the reserve it needs;
   the cost of raising money by drawing and redrawing bills (II.2).
8. **Trade policy.** The cost to a country of making at home what it could buy
   cheaper; a balance of trade, country by country; the cost of a bounty to
   the treasury and to consumers; a duty with a drawback (IV).
9. **The sovereign.** Soldiers a population can support; a teacher's or a
   judge's income by fees and by salary; tolls by weight; incidence of a tax on
   wages; revenue against the rate of a duty; a land tax on a fixed valuation;
   a public debt with a sinking fund; a debt repaid in a debased coin (V).
10. **The physiocrats' classes.** Which class, in a stated table, shows a
    produce beyond its own consumption and advances (IV.9).

**What the lab never does** is tell the reader what the eighteenth-century
economy was. Smith's own figures are his, gathered by him and often
second-hand; the labs take them as stated and work them through his reasoning.
A figure on this path shows what the chapter's reasoning implies for stated
quantities. Whether the reasoning describes how any economy worked, then or
now, is the argument of the book and of its critics, and every lesson closes
on that gap.

## §A PATH fields (`content/wealth_of_nations/__init__.py`)

```
"slug": "wealth-of-nations",
"title": "The Wealth of Nations, Read Along",
"level": "Beginner → Advanced",
"level_note": "school arithmetic only; no economics is assumed",
```

(No `"speech"` key: the lessons are prose with arithmetic, as Capital's are.)

Catalog (`scripts/catalog.py`): `short_title` `"The Wealth of Nations"`,
`"kind": "Read along"`, group `philosophy` (Philosophy and close reading),
placed **immediately before Capital**: Smith comes first, and Capital argues
with him. Card: "Adam Smith&rsquo;s <em>Wealth of Nations</em>, all five
Books in his order, with the arithmetic on his pages worked through: the
division of labour, price, wages, rent, stock, trade and taxes." The group
note's second sentence becomes "The three read-alongs go through one book
chapter by chapter." Course slug prefix `wealth-`; check-id prefix `won`;
package `wealth_of_nations` → slug `wealth-of-nations` is the package name
with `-` for `_`, so it needs no `PACKAGE_OF_SLUG` entry.

**material** (unique; required by `TestGeneratedPathIsCurrent`; the smoke
marker is the apostrophe-free phrase "what the reasoning of the chapter
implies for those quantities"):
"every figure on this path is computed in your browser from the quantities a
lesson states, Smith&rsquo;s own or written for the lesson, and shows what the
reasoning of the chapter implies for those quantities; whether that reasoning
describes any economy, then or now, is what the book argues and its critics
dispute, and no lab can settle it."

**footer_lead**: "<strong>Educational course material.</strong> Every figure
on this path is computed in your browser from what the lesson states: a
produce per head, a price resolved into its parts, a wage from a fund and a
number of workers, a rent as what is left after wages and ordinary profit, a
capital after years of saving, a tax and who pays it. Nothing is rounded
except where a lesson says so. Quotations are from the public-domain text of
the Electronic Classics Series edition (Pennsylvania State University, 2005).
What the labs cannot do is tell you whether Smith's reasoning describes the
economy you live in &mdash; and that is what the book is arguing about."

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). The tagline names
the book with `<em>`, says the arithmetic on Smith's pages is worked in front
of you, and ends "Thirteen courses and N lessons are available." The
description ends "All thirteen courses and N lessons are available."

`key` (path): `produce per head = share at work × output each`,
`price = wages + profit + rent`, `market price vs natural price`,
`wage = funds for labour / workers`, `rent = price − wages − ordinary profit`,
`capital × returns a year = labour put in motion`,
`price of land = rent × years' purchase`.

`why_order`, `prerequisites`, `sequence_intro`: course 1's author writes them
(Capital's are the shape). Prerequisites: school arithmetic (pounds, shillings
and pence explained once: 12 pence to the shilling, 20 shillings to the pound;
a quarter of corn is eight bushels); no economics; a copy of the book welcome,
not required; patience with Smith's long examples, which are the argument.

## §B The thirteen courses

| # | slug | title | Book, chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `wealth-division-of-labour` | The Division of Labour | Introduction, I.1–3 | 4 | `c01_division` |
| 2 | `wealth-money-and-measure` | Money and the Measure of Value | I.4–5 | 4 | `c02_money` |
| 3 | `wealth-component-parts-of-price` | The Component Parts of Price | I.6–7 | 3 | `c03_price` |
| 4 | `wealth-wages-and-profits` | Wages and Profits | I.8–9 | 5 | `c04_wages` |
| 5 | `wealth-different-employments` | Wages and Profit in Different Employments | I.10 | 5 | `c05_employments` |
| 6 | `wealth-rent-of-land` | The Rent of Land | I.11 | 6 | `c06_rent` |
| 7 | `wealth-stock-and-money` | Stock, Money and Banks | II Intro, II.1–2 | 5 | `c07_stock` |
| 8 | `wealth-accumulation` | Accumulation and the Employments of Capital | II.3–5 | 5 | `c08_accumulation` |
| 9 | `wealth-progress-of-opulence` | The Progress of Opulence | III.1–4 | 4 | `c09_opulence` |
| 10 | `wealth-mercantile-system` | The Mercantile System | IV.1–6 | 6 | `c10_mercantile` |
| 11 | `wealth-colonies-and-agricultural-systems` | Colonies and the Agricultural Systems | IV.7–9, Appendix | 5 | `c11_colonies` |
| 12 | `wealth-expenses-of-the-sovereign` | The Expenses of the Sovereign | V.1 | 6 | `c12_expenses` |
| 13 | `wealth-taxes-and-public-debts` | Taxes and Public Debts | V.2–3 | 7 | `c13_taxes` |

65 lessons. Module labels (the `module` field) are Smith's Book and chapter,
e.g. `"Book I, Chapter 1 · Of the Division of Labour"`; the Introduction is
`"Introduction and Plan of the Work"`; a Part of a chapter is
`"Book V, Chapter 1, Part 2 · Of the Expense of Justice"`. Chapter titles may
be shortened by dropping Smith's "Of the" only where the title would not fit.

## §C Every lesson

Format: slug — Title — text (line numbers in
`/mnt/project-files/wealth-texts/wealth-of-nations-psu.txt`, approximate:
find the boundaries yourself with `grep -n`) — lab `wonkit/mode` `view` —
focus. Smith's own figures may be preset data (the text is public domain), and
at least one preset per lesson should be his where the chapter gives figures;
cite the passage in prose and the line in a source comment. Figures written
for the lesson are labelled as such ("a weaver's stock, written for this
lesson"). Never present an invented figure as Smith's or as history.

### Course 1 — The Division of Labour (Introduction, Book I Chapters 1–3)

1. `the-annual-labour-of-every-nation` — The Annual Labour of Every Nation — Introduction and Plan (l. 107–183) — `wonkit/division` `supply` — produce per head of a nation from population, the number at useful labour and output per worker; Smith's contrast between "savage nations" where nearly all work and are poor, and "civilized" ones where many do not work and the poorest are better supplied; the plan of the five Books.
2. `the-pin-factory` — The Pin Factory — I.1 (l. 191–473) — `wonkit/division` `pins` — Smith's ten workers, eighteen operations, upwards of 48,000 pins a day against perhaps not one, certainly not twenty, each alone; the multiple; the three causes (dexterity, time saved passing between tasks, machines); the woollen coat.
3. `the-propensity-to-truck-and-barter` — The Propensity to Truck, Barter and Exchange — I.2 (l. 474–603) — `wonkit/division` `exchange` — self-love not benevolence (the butcher, the brewer, the baker); the bow-and-arrow maker; talents as effect not cause (the philosopher and the porter); two producers' output self-sufficient and specialised. The rules sentence names comparative cost as Ricardo's later rule (1817) and says Smith's own case is one where each is better at one thing.
4. `the-extent-of-the-market` — The Extent of the Market — I.3 (l. 604–753) — `wonkit/division` `market` — the porter who cannot live in a village; the country carpenter; how many specialists a demand keeps; water carriage widening the market (London to Edinburgh by wagon and by ship, Smith's figures in prose).

### Course 2 — Money and the Measure of Value (Book I Chapters 4–5)

1. `the-origin-and-use-of-money` — The Origin and Use of Money — I.4 (l. 754–965) — `wonkit/money` `barter` — the want of a double coincidence (the butcher, brewer and baker again); exchange ratios with and without a common measure; cattle, salt, shells, nails as money; stamped coin; debasement named, worked next lesson; value in use and value in exchange (water and diamonds) as the chapter's closing question.
2. `labour-the-real-measure` — Labour, the Real Measure of Value — I.5 first part (l. 966–1100, with the Canton and London passage l. 1223–1269) — `wonkit/price` `real` — "toil and trouble"; labour commanded; real and nominal price; equal quantities of labour of equal value to the labourer; a price in money and in days of labour over years (Smith's examples, and an invented series labelled as such).
3. `corn-rents-and-money-rents` — Corn Rents and Money Rents — I.5 middle (l. 1101–1222: the perpetual rent, the colleges, corn and silver) — `wonkit/price` `real` (corn as the measure) — corn the better measure from century to century, silver from year to year; the statute of Elizabeth reserving a third of college rents in corn; a fixed money rent against its corn value as silver falls.
4. `gold-silver-and-copper-coin` — Gold, Silver and Copper Coin — I.5 end (l. 1270–1549; the debasement of the pound is l. 876–925, in I.4) — `wonkit/money` `coin` — the pound that was a pound weight of silver; the silver in a penny over reigns; the legal ratio of gold to silver; why a creditor paid in a debased coin is defrauded.

### Course 3 — The Component Parts of Price (Book I Chapters 6–7)

1. `wages-profit-and-rent` — Wages, Profit and Rent — I.6 (l. 1553–1784) — `wonkit/price` `parts` — the beaver and the deer in the "early and rude state"; profit not wages of inspection; rent once land is private property; a price resolved through the stages of production into wages, profit and rent; the three original sources of every revenue. Names Capital's lesson that argues with this resolution, by title, in one sentence.
2. `natural-and-market-price` — Natural and Market Price — I.7 first part (l. 1785–1960) — `wonkit/price` `market` — the natural rates; effectual demand; quantity brought to market above or below it; the market price gravitating to the natural; which component's rate is pushed above or below its natural rate.
3. `monopoly-and-the-natural-price` — Monopoly and the Natural Price — I.7 end (l. 1960–2092) — `wonkit/price` `market` (a monopolist's schedule) — keeping the market under-stocked; the price of monopoly "the highest which can be got"; secrets in trade, corporations and natural scarcity (the French vineyard).

### Course 4 — Wages and Profits (Book I Chapters 8–9)

1. `the-masters-and-the-workmen` — The Masters and the Workmen — I.8 first part (l. 2093–2241) — `wonkit/wages` `subsistence` — the produce of labour its natural wages; the contract and combinations of masters and of workmen; the lowest rate consistent with common humanity; a family's subsistence against a stated wage (Smith's Cantillon passage: double the labourer's own maintenance).
2. `the-funds-destined-for-maintaining-labour` — The Funds Destined for Maintaining Labour — I.8 (l. 2242–2396) — `wonkit/wages` `fund` — wages rise with the increase, not the size, of national wealth; North America, China, Bengal; a fund and a number of workers growing at stated rates over years, and the wage each year.
3. `the-liberal-reward-of-labour` — The Liberal Reward of Labour — I.8 end (l. 2397–2869) — `wonkit/wages` `growth` — population doubling in twenty or five-and-twenty years in the colonies; the Highland mother of twenty children with two alive; the liberal reward as effect and cause of increasing wealth; piece-work and overwork; dear and cheap years.
4. `the-profits-of-stock` — The Profits of Stock — I.9 first part (l. 2870–3203) — `wonkit/interest` `profit` — profit hard to know, interest its index; interest over reigns (Smith's legal rates: 10, 8, 6, 5 percent); Holland; double interest as a reasonable profit; what is left to the borrower for risk and trouble.
5. `high-profits-raise-prices` — High Profits Raise Prices More Than High Wages — I.9 end (l. 3204–3237) — `wonkit/price` `parts` (with a wage rise and a profit rise) — a rise of wages adds to price like simple interest, a rise of profit like compound interest through the stages; merchants complain of wages and are silent about profits.

### Course 5 — Wages and Profit in Different Employments (Book I Chapter 10)

1. `the-five-circumstances` — The Five Circumstances — I.10 Part I, circumstances one to four (l. 3238–3435) — `wonkit/advantage` `net` — agreeableness, cost of learning, constancy, trust, probability of success; whole advantages and disadvantages tend to equality; the education of a skilled workman as an expensive machine to be replaced with ordinary profit.
2. `the-lottery-of-the-professions` — The Lottery of the Professions — I.10 Part I (probability of success; l. 3436–3649) — `wonkit/advantage` `lottery` — the law, where perhaps one in twenty succeeds; the overweening conceit of men in their abilities; soldiers and sailors; a profession as a lottery whose prizes do not repay its tickets.
3. `the-apothecary-and-the-grocer` — The Apothecary and the Grocer — I.10 Part I on profits and the three conditions (l. 3650–3927) — `wonkit/advantage` `profit` — the apothecary's "thousand per cent", which is the reasonable wages of his labour; the grocer in a village and in a town; risk and the rate of profit; the three conditions for the tendency to equality (well known, in its ordinary state, the sole employment).
4. `apprenticeship-and-corporations` — Apprenticeship and Corporations — I.10 Part II, first and second ways (l. 3928–4447) — `wonkit/advantage` `net` (with entry restricted) — seven years' apprenticeship; corporations; "people of the same trade seldom meet together"; how restricting entry keeps a trade's wage above the others'.
5. `the-law-of-settlements` — The Law of Settlements — I.10 Part II, third way, and the close (l. 4448–4727) — `wonkit/advantage` `net` (two parishes) — obstructions to the free circulation of labour; the poor laws and settlements; wages differing between neighbouring places where stock moves freely; assessed wages.

### Course 6 — The Rent of Land (Book I Chapter 11)

1. `rent-as-a-monopoly-price` — Rent as a Monopoly Price — I.11 introduction (l. 4728–4811) — `wonkit/rent` `residual` — rent the highest the tenant can afford; what is left after wages and ordinary profit; high or low price the cause, not the effect, of rent.
2. `produce-which-always-affords-rent` — Produce Which Always Affords Rent — I.11 Part I (l. 4812–5333) — `wonkit/rent` `residual` (fertility and situation) — food always affords rent; lands by fertility and distance; good roads and canals; the vineyard, sugar, tobacco, rice and potatoes.
3. `produce-which-sometimes-affords-rent` — Produce Which Sometimes Affords Rent — I.11 Part II (l. 5334–5801) — `wonkit/rent` `residual` (mines) — materials of clothing and lodging; coal mines; "the most fertile coal mine regulates the price"; mines of silver in Peru; precious stones.
4. `the-value-of-silver-over-four-centuries` — The Value of Silver over Four Centuries — the Digression, first period (l. 5867–6377) — `wonkit/rent` `silver` — the price of wheat in silver from 1350; why prices fell to about 1570; Smith's averaging of Windsor market prices; the error of reading a fall in money prices as a fall in the value of corn.
5. `silver-from-america` — Silver from America — the Digression, second and third periods and the variations in the proportion between gold and silver (l. 6377–7240) — `wonkit/rent` `silver` (periods) — the fall in the value of silver from about 1570 to 1640; its steadiness after; whether the value of silver was then falling; the ratio of gold to silver.
6. `improvement-and-the-three-orders` — Improvement and the Three Great Orders — I.11 Part III's three sorts of rude produce and the conclusion of the chapter (l. 5802–5866 and 7241–8484; the Conclusion of the Digression is only touched and the tables at 8485–8830 are left to the book) — `wonkit/rent` `residual` (a price that rises with improvement) — cattle, poultry and hogs rising in price as cultivation spreads; the effects of improvement on real price; rent, wages and profit and the interests of the three orders; the interest of dealers "always in some respects different from, and even opposite to, that of the public".

### Course 7 — Stock, Money and Banks (Book II Introduction, Chapters 1–2)

1. `stock-must-be-accumulated-first` — Stock Must Be Accumulated First — II Introduction (l. 8834–8908) — `wonkit/stock` `division` — the weaver who must have a stock of food, materials and tools before his web is sold; accumulation previous to division.
2. `fixed-and-circulating-capital` — Fixed and Circulating Capital — II.1 (l. 8909–9162) — `wonkit/stock` `division` (a society's stock) — the stock reserved for immediate consumption; fixed capital (machines, buildings, improvements, acquired abilities); circulating capital (money, provisions, materials, finished work).
3. `gross-and-net-revenue` — Gross and Net Revenue — II.2 first part (l. 9163–9500) — `wonkit/stock` `revenue` — the gross revenue of a society and the net after maintaining fixed capital and money; money as the great wheel of circulation, no part of the revenue.
4. `paper-money-and-the-scottish-banks` — Paper Money and the Scottish Banks — II.2 (l. 9500–9990) — `wonkit/bank` `paper` — Smith's million of gold and silver, the bank notes that replace it and the reserve the banks keep; the gold sent abroad; why paper beyond the circulation returns on the bank.
5. `drawing-and-redrawing` — Drawing and Redrawing — II.2 end (l. 9990–10767) — `wonkit/bank` `redraw` — discounting real bills; the cost of a circular bill, interest and commission each round; the Ayr bank; why the projector's capital comes dearest of all; the freedom of banking with notes above small sums.

### Course 8 — Accumulation and the Employments of Capital (Book II Chapters 3–5)

1. `productive-and-unproductive-labour` — Productive and Unproductive Labour — II.3 first part (l. 10768–11000) — `wonkit/stock` `accumulate` (a share spent on unproductive hands) — the manufacturer's workman and the menial servant; the sovereign, the army, churchmen, lawyers, players; the annual produce divided between capital and revenue. Names Capital's lesson that takes up productive labour, by title, in one sentence.
2. `parsimony-and-the-prodigal` — Parsimony and the Prodigal — II.3 rest (l. 11000–11404) — `wonkit/stock` `accumulate` — "capitals are increased by parsimony"; the prodigal who encroaches on capital; private frugality against public prodigality; a capital over years at stated saving shares.
3. `stock-lent-at-interest` — Stock Lent at Interest — II.4 (l. 11405–11689) — `wonkit/interest` `purchase` — the borrower's capital, not the money; the fall of interest as stocks increase; usury laws and the legal rate a little above the lowest market rate; the price of land in years' purchase.
4. `the-four-ways-of-employing-capital` — The Four Ways of Employing Capital — II.5 first part (l. 11690–11950) — `wonkit/stock` `turnover` — agriculture, manufactures, wholesale, retail; the quantity of productive labour each puts in motion; nature labours along with man in agriculture (Smith's ranking stated and later disputed, said so).
5. `home-foreign-and-carrying-trade` — The Home, the Foreign and the Carrying Trade — II.5 rest (l. 11950–12230) — `wonkit/stock` `turnover` (returns a year) — a capital returned three or four times a year in the home trade (correction: the text says "three or four", not "four or five"; one capital doubles in the year against two replaced, giving Smith's 24 to 1) and once in two or three years in a distant foreign trade; the carrying trade; Smith's ordering and its later critics.

### Course 9 — The Progress of Opulence (Book III)

1. `the-natural-progress-of-opulence` — The Natural Progress of Opulence — III.1 (l. 12234–12386) — `wonkit/division` `exchange` (town and country) — the great commerce between town and country; agriculture, then manufactures, then foreign commerce as the natural order; Europe's order inverted.
2. `primogeniture-entails-and-tenants` — Primogeniture, Entails and Tenants — III.2 (l. 12387–12763) — `wonkit/rent` `tenure` — great estates and why great proprietors seldom improve; slaves, metayers and farmers; whether an improvement pays the one who must make it under each tenure; leases and security.
3. `the-rise-of-towns` — The Rise of Towns — III.3 (l. 12764–13133) — `wonkit/tax` `land` (a fixed farm of the town's taxes) — burghers who were once servile; the town that farms its own taxes at a fixed sum; order and good government in towns before the country.
4. `how-commerce-improved-the-country` — How the Commerce of Towns Improved the Country — III.4 (l. 13134–13574) — `wonkit/stock` `spend` — the great lord's hospitality and retainers; "a pair of diamond buckles"; a revenue spent on a thousand retainers against the same spent on goods that each pay a small share of many workers' maintenance; independence of the tenants and the fall of the barons.

### Course 10 — The Mercantile System (Book IV Chapters 1–6)

1. `wealth-does-not-consist-in-money` — Wealth Does Not Consist in Money — IV.1 (l. 13592–14356) — `wonkit/trade` `balance` — the popular notion of wealth; the Tartar who asks how many cattle; exports and imports country by country; why gold and silver flow to where they are wanted.
2. `the-invisible-hand` — Restraints on Importation and the Invisible Hand — IV.2 (l. 14357–15037) — `wonkit/trade` `make` — the home trade preferred; "led by an invisible hand"; the tailor and the shoemaker; grapes grown in Scotland at thirty times the cost; the two cases for a restraint (defence: the Navigation Act; a home tax) and retaliation.
3. `the-balance-of-trade-and-banks-of-deposit` — The Balance of Trade and Banks of Deposit — IV.3 (l. 15038–15945, with the Digression on the Bank of Amsterdam) — `wonkit/trade` `balance` (exchange) — restraints against France; the exchange as a measure of the balance; bank money and its agio; the balance of produce and consumption, which is the one that matters.
4. `drawbacks` — Drawbacks — IV.4 (l. 15946–16118) — `wonkit/trade` `drawback` — duties repaid on re-exportation; why drawbacks are reasonable and bounties are not.
5. `bounties-and-the-corn-trade` — Bounties and the Corn Trade — IV.5 with the Digression concerning the Corn Trade and Corn Laws (l. 16119–17454) — `wonkit/trade` `bounty` — the bounty of five shillings the quarter on exported corn; its cost to the public in the bounty and in the higher home price; the inland dealer, the exporter, the importer and the carrier; the fear of engrossing.
6. `treaties-of-commerce` — Treaties of Commerce — IV.6 (l. 17455–17849) — `wonkit/trade` `make` (a preferential duty) — the Methuen treaty, Portuguese wine at two-thirds of the French duty; who gains by a preference; seignorage named.

### Course 11 — Colonies and the Agricultural Systems (Book IV Chapters 7–9 and Appendix)

1. `motives-for-new-colonies` — The Motives for New Colonies — IV.7 Part I (l. 17852–18166) — `wonkit/advantage` `lottery` (gold mines) — Greek and Roman colonies; the search for gold; "of all those expensive and uncertain projects … there is none perhaps more perfectly ruinous than the search after new silver and gold mines" (check the words in the text).
2. `the-prosperity-of-new-colonies` — The Prosperity of New Colonies — IV.7 Part II (l. 18167–19059) — `wonkit/wages` `growth` — plenty of good land and liberty to manage their own affairs; high wages, cheap land and a doubling population; English colonies against Spanish and Portuguese.
3. `the-monopoly-of-the-colony-trade` — The Monopoly of the Colony Trade — IV.7 Part III (l. 19060–20843) — `wonkit/stock` `turnover` (a distant trade against a near one) — the advantages Europe drew from America and the East Indies; the monopoly raising the rate of profit and turning capital from near trades with frequent returns to a distant one; "a nation of shopkeepers"; the case for union or separation.
4. `the-conclusion-of-the-mercantile-system` — The Conclusion of the Mercantile System — IV.8 (l. 20844–21524) — `wonkit/trade` `bounty` (a prohibition's cost to consumers) — "consumption is the sole end and purpose of all production"; the prohibition of the export of wool; who contrived the system.
5. `the-agricultural-systems` — The Agricultural Systems — IV.9 with the Appendix (l. 21525–22502) — `wonkit/system` `classes` — Quesnay and the économistes: proprietors, cultivators, and the "barren" class; the net product; Smith's objection that artificers and merchants are not barren; "the obvious and simple system of natural liberty" and the sovereign's three duties.

### Course 12 — The Expenses of the Sovereign (Book V Chapter 1)

1. `the-expense-of-defence` — The Expense of Defence — V.1 Part I (l. 22509–23096) — `wonkit/public` `soldiers` — hunters, shepherds, husbandmen and civilized nations at war; not more than one in a hundred as soldiers; militia and standing army; the expense of firearms.
2. `the-expense-of-justice` — The Expense of Justice — V.1 Part II (l. 23097–23523) — `wonkit/public` `fees` (a judge's income) — authority from age, fortune, birth; justice as a source of revenue; fees of court and the salaries of judges; the separation of the judicial from the executive power.
3. `public-works-and-tolls` — Public Works and Tolls — V.1 Part III, Article I, first section (l. 23524–23824) — `wonkit/public` `tolls` — roads, bridges and canals paid by those who use them; tolls by weight; the luxurious vanity of the rich paying for the poor.
4. `trading-companies` — Regulated and Joint-Stock Companies — V.1 Part III, Article I, second section (l. 23825–24684) — `wonkit/advantage` `profit` (the East India Company's dividends of 6, 10 and 12.5 per cent. on its £3,200,000 stock, Smith's figures; the chapter gives no profit "without the monopoly", so the lab does not show one [author correction, Course 12]) — forts for the African trade; regulated companies; joint-stock companies and "negligence and profusion"; the four trades a joint-stock company can manage without a monopoly (banking, insurance, canals, water).
5. `the-education-of-youth` — The Education of Youth — V.1 Part III, Article II (l. 24685–25554) — `wonkit/public` `fees` (a teacher's income) — endowments and the diligence of teachers; Oxford, where "the greater part of the public professors have, for these many years, given up altogether even the pretence of teaching" (checked); fees against salaries; the education of women; and, from l. 25334 to the end of Article II, the torpor of the labourer whose life is spent in a few simple operations, the parish school paid partly by the public, and the three measures (facilitate, encourage, impose) [author correction, Course 12: the torpor and the parish school are in Article II, not Article III].
6. `the-instruction-of-people-of-all-ages` — The Instruction of People of All Ages — V.1 Part III, Article III, Part IV and the Conclusion (l. 25555–26563) — `wonkit/public` `fees` (a clergyman's living: the church of Scotland's £68,514 for 944 ministers, and three clergies written for the lesson) — teachers of religion paid by their hearers or by a stipend; the Hume passage and Smith's reply from the number of sects; the cost of an established church; the dignity of the sovereign; which expenses should fall on the whole society. [author correction, Course 12: the labourer's torpor and the parish school belong to lesson 5, since they are in Article II.]

### Course 13 — Taxes and Public Debts (Book V Chapters 2–3)

1. `the-funds-of-the-sovereign` — The Funds of the Sovereign — V.2 Part I (l. 26570–26862) — `wonkit/interest` `purchase` (crown lands sold) — stock and land as sovereign funds; the crown lands of Europe and what they would fetch at years' purchase against what they yield.
2. `the-four-maxims-of-taxation` — The Four Maxims of Taxation — V.2 Part II introduction (l. 26863–26955) — `wonkit/tax` `land` — equality, certainty, convenience, economy; a tax by fixed valuation against one that follows the rent.
3. `taxes-upon-rent-and-profit` — Taxes upon Rent and Profit — V.2 Part II, Articles I and II and the Appendix (l. 26956–28305) — `wonkit/tax` `land` (a land tax on rents that change) — the land tax of England on a fixed valuation; tithes; a tax on house rents; taxes on profit and on interest; stamp duties.
4. `taxes-upon-wages` — Taxes upon the Wages of Labour — V.2 Part II, Article III (l. 28306–28416) — `wonkit/tax` `incidence` — a direct tax on wages raises them by more than the tax: Smith's one-fifth that raises wages by one-fourth; who finally pays.
5. `taxes-upon-consumable-commodities` — Taxes upon Consumable Commodities — V.2 Part II, Article IV (l. 28417–29827) — `wonkit/tax` `arithmetic` — capitation taxes; necessaries and luxuries; the excise and the customs; Swift's saying that in the arithmetic of the customs two and two sometimes make only one; revenue at each rate of duty.
6. `public-debts` — Public Debts — V.3 first part (l. 29828–30700) — `wonkit/debt` `sinking` — the sovereign who saves nothing; anticipations and perpetual funding; the sinking fund; a debt with interest and a yearly payment, year by year.
7. `the-debasement-of-the-coin` — Bankruptcy Disguised as Debasement — V.3 end and the close of the book (l. 30700–end) — `wonkit/debt` `debase` — "when national debts have once been accumulated to a certain degree, there is scarce, I believe, a single instance of their having been fairly and completely paid" (check the words); raising the denomination of the coin as a pretended payment; the colonies and the empire that is "not an empire, but the project of an empire" (check the words).

## §D The new kit: wonkit

Two families, one seam. `scripts/mathpath/labs/wonkit_core.py` is written
already and is the seam: `mode_lab`, the family sentence, the caution
(`CAUTION`), `WNK_CORE_JS` (`wnkStatus`), and re-exports of acckit's field
kinds and printers. **Read `docs/accelerate/kit-contract.md` sections 1–4 for
the spec dict and field kinds: wonkit uses them unchanged.** Every lab is
built through `wonkit_core.mode_lab`; every view's status line ends through
`wnkStatus` (never `aktStatus`).

- Family A, `scripts/mathpath/labs/wonkit.py`, owns the entry point
  `wonkit_lab(cfg)` (dispatching its own modes and, through a lazy import,
  `wonkit_b.MODES`), the registry line in `scripts/mathpath/labs/__init__.py`
  (`"wonkit": wonkit.wonkit_lab`), and the `KITS_WITH_EXPECTATIONS` entry in
  `scripts/build_paths.py`.
- Family B, `scripts/mathpath/labs/wonkit_b.py`, exposes `MODES` (mode name →
  builder) and touches nothing else outside its own file, its mathcheck block
  and its report.

### D.0 Rules for every view

- **Exact.** Every figure is a whole count or an exact BigInt rational, printed
  with eakit's printers; a percentage is exact or to two places, stated. No
  floating point anywhere a reader sees a number. Compounding over years is
  exact by repeated multiplication (years are whole, at most 200).
- **Money.** Amounts are typed as decimals or fractions in one money unit the
  preset names (`money_unit` cfg key, a short plain word or symbol such as
  `£`, `s`, `d`, `oz silver`; default `£`), and printed in that unit. A view
  that needs pounds, shillings and pence may take a `£sd` cell (`1.2.6` =
  £1 2s 6d) and print `£1 2s 6d`; if you add that cell kind, add it in
  `wonkit.py` and let family B import it. Do not invent a currency word.
- **Names.** Every record names its row with `ea.NAME`-shaped names
  (`weaver`, `north-america`). Nothing typed is evaluated as script.
- **Refusals.** Every text box survives `''`, `banana`, `0`, `-1`, `1/0` and
  `A>B`: the page paints a red sentence and blanks the tiles to `—`; the
  Python `check` raises the same sentence at build time for a preset.
- **Rules sentence.** Each view's `rules` says what is computed, the formula
  in words, how ties and orders go, and where Smith gives the rule and where
  the lab adds one (a rule the lab adds is said to be the lab's).
- **Status line.** One sentence of the result, then the caution via
  `wnkStatus`.
- **Size.** At most 12 records per list unless stated. A page ships only its
  own mode's base block and its own view's block.
- **Never**: print a figure the inputs do not determine; claim a historical
  fact; grade a policy; carry hidden data (every number on the page is one
  the reader can see in a box).

### D.1 Family A (`wonkit.py`): Book I

| mode (prefix) | view | inputs | tiles (at least) |
|---|---|---|---|
| `division` (wdv) | `supply` | `nations`: records `nation, population, workers, output` (output per worker per year, in the preset's `qty_unit`, cfg, default `units`) | per nation: share at work (exact %), annual produce, produce per head; which nation is better supplied per head; the ratio of the two best (or first two) |
|  | `pins` | `workers`, `operations` (whole), `together` (the team's output a day), `alone` (one worker's output a day alone, rational ≥ 0; 0 allowed: "perhaps not one") | output per worker divided; the team's output if each worked alone; the multiple (per worker divided / alone; "no finite multiple" when alone is 0); extra output a day; operations per worker |
|  | `exchange` | `goods` (two names), `producers`: records `producer, hours, a, b` (hours available; hours per unit of each good) | self-sufficient: each splits hours to make equal quantities of both (q = hours / (a + b)), totals; specialised: each makes only the good of the lower relative cost (a/b against the other's), totals; gain in each good; who makes what; the rules sentence names the relative-cost rule as Ricardo's and says when it agrees with Smith's (each better at one good); ties (equal relative cost) refused with a sentence |
|  | `market` | `places`: records `place, demand` (units a year), `output` (one specialist's units a year), `days` (optional working days, default 300) | per place: specialists the demand keeps (whole, floored), share of one specialist's year the place takes, whether a full-time trade can live there (yes when ≥ 1); units a day for one specialist |
| `money` (wmo) | `barter` | `goods` (2–12 names); optional `traders`: records `trader, has, wants` | ratios to quote without money n(n−1)/2 and with a common measure n−1; with traders: pairs who can trade directly (A has what B wants and B has what A wants), traders who can trade only through a money (has something someone wants) |
|  | `coin` | `periods`: records `period, coined` (pence coined from one pound weight of silver, e.g. 240 then 744), optional `sum` (a fixed money sum in pence) | per period: silver per penny as a fraction of the first period's; the first period's pound in later pence; a fixed sum's silver against the first period (exact %); the loss to a creditor paid the same sum |
| `price` (wpr) | `real` | `years`: records `year, price, measure` (the money price of the good, and the money price of the measure: a day's labour or a quarter of corn, `measure_unit` cfg e.g. `days of labour`) | per year: real price = price / measure (in the measure's unit); change first → last in money (exact %) and in the measure (exact %); whether the money price and the real price moved the same way |
|  | `parts` | `stages`: records `stage, wages, rent, rate` (wages and rent paid at the stage; rate = the profit rate on everything advanced at the stage, % ); optional `wage_rise` (%, applied to every stage's wages) and `profit_rise` (percentage points added to every stage's rate) | price after each stage = (previous price + wages + rent) × (1 + rate); final price; resolved into total wages, total rent, total profit and their shares (exact); with a rise: the new price and the rise caused by each (wages alone, profit alone), so a profit rise compounds and a wage rise adds |
|  | `market` | `natural` (natural price a unit), `effectual` (effectual demand, units at the natural price), `brought` (units brought to market); optional `buyers`: records `price, quantity` (what buyers would take at each price, written for the lesson; quantities not increasing as price rises) | above/at/below the natural price (from brought against effectual); shortfall or excess in units; with buyers: the market price = the highest listed price at which buyers take at least the quantity brought (the lab's rule, said so), its gap to the natural price per unit and over the quantity brought; without buyers "no schedule given" |
| `wages` (wwg) | `subsistence` | `items`: records `item, cost` (a family's needs, per `period` cfg word, default `week`), `wage` (per the same period), optional `maintenance` (the worker's own) and `multiple` (e.g. 2, Cantillon's double) | family subsistence; wage against it (covers / short by); with maintenance × multiple: that minimum and the wage against it |
|  | `fund` | `fund` (funds destined for maintaining labour, a year), `workers`, `fund_growth`, `worker_growth` (% a year, may be negative), `years` (0–50) | each year's fund, workers (exact, not rounded: a rate of population, said so) and wage = fund / workers; wage first and last; whether it rises, holds or falls; the rule that the wage follows the increase of the fund against the workers, not its size |
|  | `growth` | `population`, `doubling` (years), `years` (whole, a multiple of the doubling time — refused otherwise with the reason: a part of a doubling needs a root the lab does not take), optional second `doubling2` to compare | doublings; population after; the factor; with a second doubling time the two compared |
| `advantage` (wad) | `net` | `employments`: records `employment, wage, days, learning, years, other` (wage a day, days worked a year, cost of learning, working years over which it is replaced, other: a stated money value a year for agreeableness, risk or disgrace, signed); optional `profit` (%: the ordinary profit the cost of learning must also earn, default 0); optional `limit`: records `employment, entrants` (a cap on entry, with `pay_rise` per capped employment) | per employment: money wage a year; learning replaced a year (learning / years, plus profit on it); net advantage; ranking; spread between highest and lowest; with a limit, the net advantage with the capped trade's raised pay |
|  | `lottery` | `entrants`, `succeed` (how many win), `prize` (income a year of one who succeeds), `years` (working years), `cost` (each entrant's cost of education) | chance of success (exact fraction and %); total prizes = succeed × prize × years; total cost = entrants × cost; expected prize per entrant; prizes against cost (fair, short or over, and by how much); what the prize would need to be to repay the tickets |
|  | `profit` | `sales`, `cost` (stock laid out), `wages` (what the trader's own labour would earn as wages), optional `stock` (capital employed if different from cost) | apparent profit (sales − cost) and its rate on stock; true profit after the wages of the trader's labour, and its rate; the share of the apparent profit that is wages |
| `rent` (wre) | `residual` | `lands`: records `land, output, wages, stock` (per year: units produced, wages paid, other stock advanced), `price` (a unit), `rate` (ordinary profit %, on wages + stock), optional `price2` | per land: produce value, wages + stock + ordinary profit, rent (if negative, "no rent" and the loss); total rent; lands yielding no rent; each land's lowest price that affords rent ((wages+stock)(1+rate)/output); with price2: each land's rent at it |
|  | `tenure` | `cost` (an improvement's cost), `added` (produce it adds a year), `years` (years the improver gets the benefit, e.g. a lease), `tenures`: records `tenure, share, bears` (share of the added produce the occupier keeps; bears = the share of the cost the occupier pays) | per tenure: occupier's gain over the years = share × added × years − bears × cost; whether the occupier improves (gain > 0); the landlord's part; the tenures under which the improvement is made |
|  | `silver` | `prices`: records `year, price` (price of a quarter of wheat, in `money_unit`, e.g. oz silver or shillings), `periods`: records `period, from, to` (year ranges) | per period: years in it, average price (exact, to 2 places), ratio to the first period; the value of silver in corn (quarters per unit = 1 / average); periods with no years listed refused |
| `interest` (wit) | `purchase` | `rent` (a year), `rate` (%), optional `rate2` (%), optional `yield` (what the asset yields its present owner a year, for the crown-lands case) | years' purchase = 100 / rate; price = rent × years' purchase; with rate2 both; with yield, what the asset fetches against what it yields (years of its present yield) |
|  | `profit` | `rows`: records `period, interest` (market rate %), `multiple` (profit as a multiple of interest, default 2: "double interest"), optional `profit` (a stated profit rate %) | per period: the implied ordinary profit (interest × multiple); with a stated profit, what is left after interest; the fall from first to last |

### D.2 Family B (`wonkit_b.py`): Books II to V

| mode (prefix) | view | inputs | tiles (at least) |
|---|---|---|---|
| `stock` (wst) | `division` | `parts`: records `part, amount, kind` where kind is one of `consumption`, `fixed`, `circulating` | totals by kind and shares (exact %); capital (fixed + circulating) against the whole stock; the largest part of each kind |
|  | `revenue` | `gross` (annual produce), `fixed` (maintenance of fixed capital a year), `money` (maintenance of the money in circulation a year), optional `saving` (a reduction of the money's maintenance, e.g. by paper) | net revenue = gross − fixed − money; share of gross; with saving, the new net revenue and the gain |
|  | `accumulate` | `capital`, `return` (% of capital produced a year as revenue above replacing it), `saved` (% of that revenue added to capital; negative for a prodigal who spends capital), `years` (0–50), optional `wage` (a year's maintenance of one productive worker) | capital each year (exact, shown to 2 places); after the years; labour maintained (capital / wage) first and last; a frugal and a prodigal path side by side when two presets, or `saved2` |
|  | `turnover` | `trades`: records `trade, capital, returns` (returns a year as a fraction, e.g. 4, 1/2, 1/3), optional `wage` | per trade: capital put to work over a year = capital × returns; productive labour it can maintain (/ wage); ordering; the ratio of the most to the least |
|  | `spend` | `revenue`, `maintenance` (one person's yearly maintenance), `purchases`: records `trade, amount, makers` (what is spent on one trade's goods, and how many workers' produce it buys from) | retainers the revenue could maintain directly; per purchase: the share of each maker's maintenance it pays (amount / makers / maintenance, exact); the number of people partly maintained; no one wholly dependent when every share is under one |
| `bank` (wbk) | `paper` | `circulation` (gold and silver needed to circulate the produce), `notes` (paper issued), `reserve` (% of notes kept in coin) | coin kept; coin replaced and free to go abroad = circulation − reserve coin, when notes ≤ circulation; notes beyond the circulation that return on the bank; the reserve needed |
|  | `redraw` | `sum`, `interest` (% a year), `commission` (% a draw), `months` (each bill's term), `years` (whole) | draws a year; cost a year as a share of the sum (simple: interest + commission × draws; compound: the sum grown by (1 + interest·months/12 + commission) per draw), exact; total over the years; the excess over the stated interest |
| `trade` (wtr) | `make` | `goods`: records `good, quantity, home, foreign, duty` (cost a unit at home, price abroad delivered, duty a unit if bought abroad) | per good: cost if bought abroad (foreign + duty), cost if made at home, the cheaper; what a prohibition (forcing home make) costs the country a year; with a duty, the duty revenue and the cost to buyers |
|  | `balance` | `countries`: records `country, exports, imports` | balance each (signed); total; the countries with an unfavourable balance; the total two-way trade; the rules sentence states the "balance" is the mercantile measure Smith rejects, computed for reading |
|  | `bounty` | `exported`, `bounty` (a unit), `home`, `rise` (price rise a unit at home that the lesson attributes to the bounty) | cost to the treasury = exported × bounty; cost to home buyers = home × rise; total; per unit exported |
|  | `drawback` | `quantity`, `duty` (a unit), `exported` (units re-exported), `share` (% of the duty drawn back) | duty paid; drawn back; net duty; net per unit kept at home |
| `tax` (wtx) | `incidence` | `wage` (before the tax), `rate` (% of the wage taken) | the wage that leaves the worker the same subsistence = wage / (1 − rate); the rise (exact %), which exceeds the rate; the tax paid; who advances it (the employer) |
|  | `arithmetic` | `rows`: records `duty, quantity` (the quantity that pays at each rate, written for the lesson) | revenue each = duty × quantity; the highest-yielding duty; rows where a higher duty yields less |
|  | `land` | `valuation` (fixed assessed rent), `rate` (% of the valuation), `rents`: records `year, rent` | per year: tax = valuation × rate; as a share of the actual rent; against a tax of the same rate on the actual rent; the difference over the years |
| `debt` (wdb) | `sinking` | `debt`, `interest` (%), `payment` (a year, covering interest first), `years` (0–200), optional `borrow`: records `year, amount` (new loans in stated years) | debt each year; years to pay off within the horizon or "not paid off"; total interest paid; refuses a payment below the first year's interest with the reason (the debt grows) |
|  | `debase` | `debt` (nominal), `old` (silver in a unit of coin before), `new` (after raising its denomination) | silver owed; silver paid; the share the creditor loses; the pretended payment |
| `public` (wpb) | `soldiers` | `population`, `share` (fraction under arms, e.g. 1/100), optional `cost` (a soldier a year) | soldiers; with cost, the yearly cost; per head of the population |
|  | `fees` | `people`: records `person, salary, pupils, fee` (or suitors and fee) | per person: income from fees, from salary, the share from fees; the extra income from one more pupil; who depends most on diligence |
|  | `tolls` | `carriages`: records `carriage, weight, trips` (tons, trips a year), `toll` (a ton a trip) | toll each and total; share paid by the heaviest; per ton |
| `system` (wsy) | `classes` | `classes`: records `class, produce, consumption, advances` | per class: produce − consumption − advances (net product); classes with a net product; the "barren" classes (net product 0) under the stated figures; the rules sentence states that the figures are the table's assumption, not a measurement |

**Reports.** Each family writes `docs/wealth-of-nations/kit-report-a.md` /
`kit-report-b.md` in the shape of `docs/capital/kit-a-report.md`: every mode,
view, cfg field, tile id with an example string read off a built page, every
build-time refusal. Authors configure lessons from the reports, never from the
code.

**mathcheck.** Each family adds a block to `scripts/mathcheck.js`, in the
shape of acckit's (`// ---- wonkit (Wealth of Nations), family A ----` …
`// ---- end wonkit family A ----`), one case per view, each seen to fail when
its computation is broken on purpose.

## §E Package, text, quoting

Package `content/wealth_of_nations/`, one directory per course (§B), each with
`__init__.py` (COURSE dict, same fields as
`content/capital/c01_commodities/__init__.py`) and `part_a.py` (and
`part_b.py` past five lessons). Spoken forms in
`content/spoken/wealth_of_nations.py`, one block per course.

**The text** is the public-domain Electronic Classics Series edition (Jim
Manis, ed., Pennsylvania State University, 2005), as plain text at
`/mnt/project-files/wealth-texts/wealth-of-nations-psu.txt` (read-only). The
extraction repeats some headings and running heads ("CHAPTER XI CHAPTER XI",
"T II.") and hyphenates across lines ("fortyfour"); quote only clean running
text, and where a line break split a word, join it as the printed book does.
Cite by Book, chapter and Part in prose; put the line number beside the lesson
dict (`# PSU text l. 1234`).

**Quoting.** The text is public domain, so quotation follows Capital's rule:
copied character for character from the file, at most 120 words in any one
quotation; every phrase in `&ldquo;…&rdquo;` must be in the text. Never quote
from memory or another edition. Smith's spelling is kept inside quotations
("labour", "shew", "compleat" where the text has them).

## §F Voice

Capital's §F and `docs/capital/AUTHORING.md` "Voice, in short" apply, with
Smith for Marx. The teacher reads the passage whole, then goes through it;
tells the history of ideas as a story with people in it (Mandeville,
Cantillon, Hume, Quesnay, Turgot before; Ricardo, Malthus, Marx after);
reaches for an everyday example; talks to the reader as "you"; is warm and
lets one light remark through. Smith is presented, not endorsed. Where a claim
is contested (productive and unproductive labour, the ranking of employments
in II.5, the labour theory in I.5–6, the invisible hand's one appearance and
its later fame), the lesson says who contests it and why, at strength. Do not
make Smith a modern libertarian or a modern anything: say what the chapter
says, including the passages on the merchants' interest, the labourer's
torpor and public education. Smith died in 1790 and cannot answer anyone who
wrote later. The `note` says what the lesson's arithmetic cannot settle. The
last `p` of the body points to the next lesson (at a course's end, the next
course).

## §G What is left out, and why

- The publisher's front matter of the PSU edition.
- Most of the Digression on silver's tables of Windsor prices: the lessons use
  a handful of years as preset data, cited, and say the full tables are in the
  book.
- The long historical narratives of Book III and of Book V Part I are read in
  outline; each lesson says what it skips.
- Book IV Chapter 7's detailed accounts of each colony and of the East India
  Company, beyond what the lessons need.
- The Appendix to Book IV (the herring bounty accounts) is pointed to in the
  Agricultural Systems lesson.
