# Second review: Average Profit and Its Fall (`capital-prices-of-production`, `c10_prices`)

Reviewer: independent second read, per `docs/capital/SECOND-REVIEW.md`. I read
Volume III, Chapters 8 to 15 of the Kerr text whole (l. 1574 to 2580), and the three
Chapter 9 tables on Kerr pp. 183 and 185 (`tables/volume-3/lf0445-03-0183-t0001.png`,
`-0185-t0001.png`, `-0185-t0002.png`), before checking each lesson. I wrote these findings
before opening `docs/pedagogy/capital-prices-of-production.md`.

Where a finding relies on my own knowledge of the later literature (Bortkiewicz, Samuelson,
Steedman, the New Interpretation, TSSI, Okishio, Shaikh, Marshall, Carey and Bastiat), it says so.
I changed text on those points only where I am sure.

## Summary

- **Arithmetic:** no errors. I recomputed every figure in prose, worked lines, quiz answers
  and `why`s, and observed every preset's tiles with `labcheck.js --observe`. All 25 presets
  print what the prose says. The Chapter 9 figures match the p. 183 and p. 185 images; the
  scan artefacts the tables README warns about (30 printed as 80, 105 as 150, 37 as 87) are
  read correctly. Kerr misprints are handled correctly: Ch. 9 "8 + 18 + 26", Ch. 11 "16 1/12",
  "128 7/12" and "100 10/19", Ch. 13 "66 1/3%". The page citations (247 for the table, 250
  for the correct 66 2/3%) check against the text's page markers.
- **Quotations:** strict checker before my edits: 84 segments, 0 misses. After: 87 segments,
  0 misses. There was one convention-only issue, now fixed: "strictly speaking" was quoted in
  lower case, but Kerr l. 1906 has "Strictly speaking" (the checker had matched it to an
  unrelated line, l. 4970, in the Tooke evidence).
- **Misrepresentation of Marx:** I found five places, all fixed (findings 1 to 5); finding 6
  strengthens an accurate passage. The most serious is finding 3 (Chapter 12): the lesson said
  Marx reads grounds for compensation as "shares weighted more heavily", when his sentence says
  the opposite.
- **Critics and historians:** five places were inaccurate or loose, all fixed (findings 7 to
  11).
- **Quiz:** every question has one defensible answer. I fixed two `why`s (findings 12 and 13);
  finding 14 records the distractors I argued for.
- **Final preview:** `OK` (9 pages rendered; 8 executed and swept, 8 with pinned figures,
  0 failing).

## Findings and changes

### Misrepresentation of Marx

1. **The General Rate of Profit and Prices of Production: Marx's own answer on input prices
   was skipped.** The lesson quotes the l. 1759 admission ("the possibility of an error",
   "present analysis does not necessitate a closer examination") and moves on to the
   transformation problem. But Marx had already taken up this objection at l. 1709–1719. The
   inputs' prices contain other spheres' profits, yet "if we place the sum of the cost-prices
   of the whole country on one side, and the sum of its surplus-values... the calculation must
   come out right", and the deviations "mutually compensate one another". Leaving that out
   makes it look as if Marx only conceded the point. In fact he asserted that the totals
   survive, without redoing the table, and that assertion is what Bortkiewicz tested.
   **Changed:** one sentence in the transformation paragraph quoting l. 1709 and l. 1719, and
   saying that he asserts it for the whole and does not redo the table.

2. **The General Rate of Profit, concept "The two totals": "the law of value holding for
   the whole while it fails for each commodity".** "Fails" is stronger than Marx. In
   Chapter 10 (l. 1851, 1869) and Chapter 12 (l. 2074) he says the law of value still governs
   the movement of each price of production, because a change in labour-time moves it.
   **Changed** to "while each commodity's price departs from its value."

3. **Supplementary Remarks on Prices of Production: the grounds for compensation were given
   the opposite of Marx's reading.** The body said that read together the claims are "the
   stock company of Chapter 9 with some shares weighted more heavily". The `def` called a
   ground for compensation "a profit above the general rate", and the `one_line` called it "a
   larger share of a fixed total". Kerr l. 2110 says the claims "repeat in another way the idea
   that all capitalists are entitled, in proportion to the magnitude of their respective
   capitals, to equal shares of the common loot". The capitalists think the allowances "create
   the profit itself", but in fact they serve to "equalise their participation". A slow-turnover
   capital "should nevertheless charge the profit it loses in this way" (l. 2108). The allowance
   brings it up to the equal share; it does not lift it above that share. **Changed:** the
   `one_line`, the paragraph on Marx's reading (now quoting "repeat in another way"), the
   `def`, and `mistakes[1]` ("Marx says capitalists reckon slow turnover and danger into their
   prices"). I added one sentence after the risk-premium figures: the lab does not model what
   the allowance makes good (the cargoes lost, the turnover not completed), only where its
   money comes from. **Not changed:** the presets and their figures. Read as "what an
   allowance in one price does to everyone else's rate when the total is fixed", they compute
   correctly and illustrate l. 2110's point that no allowance creates profit.

4. **The Internal Contradictions of the Law: "with no fall in exploitation at all".** In
   Marx's thought experiment (l. 2449), the over-accumulated capital earns no more because
   wages rise: the fall is due "to a rise in the money-value of the variable capital (on
   account of the increased wages) and the corresponding reduction in the proportion of
   surplus-labor to necessary labor". The 1,000/1,500 figures are his second alternative, in
   which the capital at work keeps "producing value at the old rate" and part of the capital
   lies fallow (l. 2451–2453). The lesson's paragraph introducing the figures left out the
   cause. The preset paragraph then said the rate fell "with no fall in exploitation at all",
   which contradicts the chapter's own explanation. **Changed:** the paragraph before the
   §3 quotation now gives Marx's cause (rising wages), mentions the fallow capital, and says
   the figures suppose the capital at work produces at the old rate. The preset sentence now
   says the capital at work is exploited as before because the extra 500 lies idle, and that
   the rise in wages is not modelled. This is consistent with the lesson's own `note` and with
   quiz item 4's `why`, which already said this.

5. **Market Value and Surplus Profit, concept "Surplus profit": an exception was dropped.**
   Kerr l. 2002 says every market price carries a surplus profit for the best placed "With the
   exception of crises, and of over-production in general". **Changed:** added "crises and
   general overproduction aside".

6. **Market Value and Surplus Profit: Marx's second case.** The lesson is accurate. I
   strengthened it by quoting the sentence that opens the strict reading ("The lot produced
   under the worst conditions decides the question.", l. 1906) and fixed the case of "Strictly
   speaking" (see Summary). `panel_intro` now says "the reading Marx calls strict" without a
   lower-case quotation.

### Critics and historians

7. **The General Rate of Profit: the New Interpretation was misdescribed.** The lesson said
   the New Interpretation and the TSSI both reply that "both totals hold". *My own
   knowledge, which I am sure of:* the New Interpretation (Duménil 1980, Foley 1982) defines the
   value of money from the net product and the value of labour-power as the money wage, so
   total profit equals total surplus value and the year's new value equals its price, but gross
   price does not in general equal gross value. The TSSI (Kliman, Freeman and others) does keep
   both aggregate equalities. **Changed:** the paragraph now separates the two.

8. **The General Rate of Profit: Bortkiewicz.** "In his solution the rate of profit can be
   found, but in general only one of Marx's two totals survives." *My own knowledge:* in
   Bortkiewicz's solution the price rate of profit generally differs from the value rate (it
   depends only on Departments I and II). With gold as the numéraire, both totals may fail;
   one can be kept only by choosing the normalisation. **Changed** to "though in general it
   differs from the rate computed in values, and Marx's two totals cannot in general both
   hold"; `mistakes[2]` now says "breaks at least one" of the equalities.

9. **Market Value and Surplus Profit: Marshall's scissors.** The lesson had Marshall asking
   "whether supply or demand governs value". *My own knowledge (Principles, Book V, ch. III
   §7):* the sentence is about whether value is governed "by utility or cost of production".
   **Changed:** the paragraph now says that and adds that demand and supply are the two blades.

10. **Counteracting Influences, its `note`, and the course's `not_covered`: Okishio's
    "general-equilibrium model".** *My own knowledge:* Okishio (1961) works in a linear model of
    production prices with a uniform rate of profit and a given real wage, not a
    general-equilibrium model in the usual (Walrasian) sense. **Changed** in both places. In the
    body, "enough cheapening to more than offset it" became "to offset it at least": a change in
    a non-basic sector leaves the rate unchanged.

11. **Different Compositions, Different Rates: Carey and Bastiat "in the 1850s".** Bastiat
    died in December 1850, the year his *Harmonies économiques* appeared. **Changed** to "around
    1850". *My own knowledge:* the description of their shared view (capital's share falls as
    capital grows, labour's rises) is accurate. The lesson rightly says Marx does not spell out
    their reasoning, and labels its reconstruction as such.

### Quiz

12. **Different Compositions, quiz item 2 `why`:** "This is Marx's copper and iron case:
    200c + 100v and 400c + 100v". In the chapter, copper and iron illustrate technical against
    value composition (l. 1604), and the 200/400 example is a separate paragraph (l. 1625) that
    names no metal. The body states this correctly. **Changed** to "Marx's case of dearer means
    of production". The preset id `copper` stays.

13. **The Law as Such, quiz item 4 `why`:** "A rising composition is the premise both sides
    grant." It is not: Robinson and Sweezy both questioned whether the composition in value
    rises. **Changed** to "Critics also ask whether the composition in value rises as fast as
    in mass, but none says it cannot rise", which still rules out the distractor.

14. I tried every distractor. None is also true. Two I checked closely:
    - Supplementary Remarks, quiz item 3, "The commodity's own price of production rose": this
      describes a possible consequence, not something that must have happened.
    - Counteracting Influences, quiz item 4: Okishio's constant real wage does not hold s′ fixed.

### Smaller fixes

15. **Counteracting Influences, combined preset:** "both act at half strength" was wrong for
    the cheapening, which is the same as in cheap-c. **Changed** to "s′ rises half as fast as in
    rising-s". The prose "Cheapening c depreciates existing capital" was listed among effects
    that "cut both ways" without saying which ways. **Changed** to "which checks the fall in the
    rate but can shrink the capital that yields a profit" (l. 2322).

## Recommendations (taste; not changed)

- Different Compositions: "This is the point at which most critics of the book have chosen to
  stand" is the lesson's own verdict about the critics. "Here the trouble is plain" is enough.
- Wage Changes: "The chapter's lesson for a reader of the news is narrow but sharp" leans
  toward performance. Consider "On this accounting, a general wage rise..." without the frame.
- Internal Contradictions: "How is it resolved? Not peacefully." is the one place the voice
  dramatises. It is defensible, since Marx's "fight of hostile brothers" follows, but it reads
  as performed.
- Counteracting Influences, `key`: "so the law is a tendency, not a fact". Marx's word is
  that the effects show "only under certain conditions and in the course of long periods"
  (l. 2344). "A tendency, shown over long periods" would be closer.
- Internal Contradictions: "where Marx's text has wages rising until it does" in the
  objections paragraph is now partly redundant with the corrected §3 paragraph. It could be
  cut.
- Market Value: the chapter's claim that values are historically prior to prices of
  production (l. 1849–1855), and that "the law of value dominates" price movements (l. 1851,
  1869), is the passage critics of the "historical transformation" reading argue over. One
  sentence would strengthen the lesson's answer to its own misconception.
- The Law as Such: the chapter itself concedes (l. 2264) that "The rate of profit might even
  rise, if a rise in the rate of surplus-value were accompanied by a considerable reduction in
  the value of the elements of constant... capital. But in reality... the rate of profit will
  fall in the long run." This is the closest the chapter comes to Okishio's question, and
  Counteracting Influences could quote it.
- Supplementary Remarks: the risk-premium preset models danger as a profit premium. Marx's
  own example (l. 2110) turns it into an insurance premium, a cost recovered in price. The
  lesson's insurance paragraph tells this correctly, and the lab's reading is now flagged. A
  later revision could label the preset "an allowance for danger" rather than "5% extra for
  danger".

## Where I disagree with the pedagogy assessment

Read after the findings above were written.

- **Supplementary Remarks (finding 3).** The assessment praises "the stock company of Chapter 9
  with some shares weighted more heavily" as "Marx's image" and the lesson's one dry remark. It is
  not Marx's image; it inverts it. Kerr l. 2110 says the claims for compensation repeat the idea
  of *equal* shares in proportion to capital, and that they *equalise* participation rather than
  create profit. This is the same kind of error the Course 1 second review found: a passage the
  assessment praised, saying what Marx does not.
- **The General Rate of Profit, Bortkiewicz (finding 8).** The assessment says Bortkiewicz's
  result "is stated correctly ('in general only one of Marx's two totals survives')". On my reading
  of the literature (not checkable in this repository), the two totals cannot in general both hold.
  Which one, if either, survives depends on the normalisation; with Bortkiewicz's own (gold as
  numéraire) neither need hold. His price rate of profit also differs in general from the value
  rate. Changed.
- **The New Interpretation (finding 7).** The assessment saw the problem and left it for this
  review, with the remark that a fix would need an undefined term. I fixed it without one: "total
  profit equals total surplus value and the year's new value equals its price, though not gross
  price and gross value".
- **The General Rate of Profit, Marx's own reply on input prices (finding 1).** The assessment
  says the transformation problem is handled "as PLAN §D.3 and §G prescribe", and lists the "one
  sentence every reader should find". It does not notice that the chapter answers the objection
  itself at l. 1709–1719 ("the calculation must come out right"). Leaving that out made Marx look
  as if he only conceded.
- **"No verdict is given to Marx that the text does not contain."** Two exceptions: Chapter 12's
  weighting (above) and Chapter 9's concept saying the law of value "fails for each commodity"
  (finding 2). Marx says the law of value governs the movement of every price of production
  (l. 1851, 1869, 2074).
- **Internal Contradictions (finding 4).** The assessment's repair to the `note` was right, but
  it left the body sentence "the rate has fallen from 10% to 6 2/3% with no fall in exploitation
  at all". Marx's own account of absolute over-accumulation (l. 2449) puts the cause in a rise of
  wages and a fall in surplus labour relative to necessary labour. The body now agrees with the
  `note`.
- **Okishio "general-equilibrium model" (finding 10)** in the `note` and in `not_covered`: not
  raised by the assessment. Changed.
- **Marshall's scissors (finding 9) and Carey and Bastiat "in the 1850s" (finding 11).** The
  assessment quotes both as examples of history told well. Both are slightly inaccurate. Changed.
- **"Strictly speaking".** The assessment reports 84 segments and 0 misses. The checker passed
  the lower-case quotation only by matching it to an unrelated line in Chapter 35 (l. 4970). Fixed (finding 6).
- **Counts.** The assessment says "26 preset strings over eight pages". I count 25 presets and
  55 pinned tile strings. This does not affect any finding.

I agree with the assessment on the arithmetic, the handling of the four Kerr misprints, the
page-image reading of the Chapter 9 tables, the shape and voice of the lessons, the order of
presentation, and its two weak-distractor recommendations (lesson 4's "1/6", lesson 3's
"Because Marshall had shown it"). Neither is wrong, and I left both.

## Files changed

- `content/capital/c10_prices/part_a.py`: lessons 1 (critic dates, quiz 2 `why`), 2 (concept 3,
  transformation paragraphs, `mistakes[2]`), 3 (concept 2, second-case paragraph, Marshall,
  `panel_intro`).
- `content/capital/c10_prices/part_b.py`: lessons 5 (`one_line`, Marx's-reading paragraph,
  risk-premium paragraph, `def`, `mistakes[1]`), 6 (quiz 4 `why`), 7 (combined paragraph, depreciation
  sentence, Okishio sentence, `note`), 8 (§3 lead-in, marx-preset paragraph).
- `content/capital/c10_prices/__init__.py`: `not_covered[2]`.
- No preset, `expect`, slug, module, mode or view changed; no §C entry needed changing.

Final checks: strict quotation checker 87 segments, 0 misses; `python3 scripts/preview_subject.py
capital --course capital-prices-of-production` prints `OK` (9 pages rendered; every lab executes;
8 pages with pinned figures, 0 failing).
