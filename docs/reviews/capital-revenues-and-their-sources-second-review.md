# Second review: Revenues and Their Sources (Course 14)

Course `capital-revenues-and-their-sources`, package `content/capital/c14_revenues/`,
Volume III, Part VII, Chapters 48–52. Reviewed against the Kerr text
(`volume-3-kerr.txt`, l. 6918–7417 and footnotes 144–155; Volume II l. 5200–5232
for the accumulation diagram) and the table image for Kerr p. 996. I wrote these
findings before reading the pedagogy assessment.

## Summary

- **Arithmetic:** every figure in the prose, worked lines, quiz answers and `why`s
  recomputes exactly. All 15 preset tile sets read with `labcheck --observe` match
  the prose. Marx's own rates in Chapter 50 check out (45/550 = 8 2/11%, 55/550 = 10%,
  100/550 = 18 2/11%, 150/550 = 27 3/11% against Kerr's misprinted 27 8/11%), and so
  does the 125 / 137½ example.
- **Quotations:** 51 segments, 1 miss. The miss is convention only: the drop capital
  in "CAPITAL—Profit" (l. 6924). "the true realm of freedom" is split by a page
  break (l. 6966–6968) and passes under `l.?`. Nothing needed fixing.
- **Misrepresentation:** I found five places that misstate Marx or the source, and
  fixed them. Two of them are in Chapter 48's presets and quiz, where the lesson's
  account of an owner-farmer contradicts Marx's own categories.
- **Last lesson:** the summary of the three volumes claims nothing the book does not
  argue, and the body ends on the Kerr text's last words, "…mines, fisheries."
  (l. 7417). It passes.
- **Final preview line:** `OK` (5 pages executed and swept, 5 with pinned figures,
  0 failing).

## Findings and changes

### 1. The Trinity Formula: the owner-farmer's £30 is not profit of enterprise on Marx's account (fixed)

The `no-landlord` preset sets rent to 0. The body said that "the farmer owns his
land: rent is £0 and profit of enterprise £80", and quiz 2's keyed answer was that
the £30 "lands in profit of enterprise". On Marx's own categories that is wrong.
Chapter 50 (l. 7330–7332) says of a small farmer that "to himself as a landlord he
pays his rent", and that this way of counting is "to a certain extent not
incorrectly" applied once capitalist production is general. Chapter 23
(l. 3411, 3413) says the same of interest: a capitalist working with his own capital
still splits his gross profit into interest and profit of enterprise. So the tile
shows who receives the money, not the category. The lesson's own point (ownership
moves the shares and the £200 does not move) survives, but as written the lesson
taught a categorisation that the next lesson but one quotes Marx rejecting.

**Changed:** the body now says that the tiles follow the money, not Marx's
categories, and that he would still count £30 of the £80 as rent the farmer pays
to himself (citing Chapters 50 and 23). Quiz 2's keyed answer is now "It stays in
the value product of £200 and goes to the farmer, who owns the land", and its `why`
says what Marx would call the £30. `mistakes[0]` now says the £30 "goes to the farmer
instead", not that profit of enterprise rises. Tiles and pins are unchanged.

### 2. The Trinity Formula: Roscher's "view" was quoted as if it were his own words (fixed)

The body said that Roscher "held that profit comes from the means of production and
&ldquo;rent from the earth, or nature, represented by the landlord&rdquo;". Those
quoted words are Marx's description of the view, with "(Roscher)" in brackets after
them (l. 7008). They are not Roscher's words. **Changed:** "Roscher is the one Marx
names, in brackets, for the view that…".

### 3. The Trinity Formula: "the use-value and not the value" (fixed)

"Marx … claims that [land and machines] help to make the use-value and not the
value." For land, l. 6950 supports that sentence. For machines it is wrong: means of
production pass their value on to the product (c). What Marx denies is that they
create *new* value. **Changed:** "help to make the use-value but add no new value".

### 4. Concerning the Analysis of the Process of Production: the wrong half of the answer was attached to "four with three" (fixed)

Marx's riddle at l. 7127 is about the commodities "passing over into the total
consumption" of the revenue-receivers: how can revenues of three buy consumer goods
worth four? The lesson answered, "They do not buy it all; 4,000 is bought and sold
among the capitalists of Department I and never meets a consumer." That is the
answer to the other half of the problem. The revenues *do* buy all of Department
II's 3,000, and the riddle is resolved because the 2,000 of constant capital in
those consumer goods equals Department I's revenue (l. 7096). **Changed:** the
paragraph now gives both halves: IIc 2,000 is paid for by I's revenue, and Ic 4,000
circulates within Department I.

### 5. Concerning the Analysis…: what becomes of Department I's 500 in Volume II (fixed)

The quiz 3 `why` said Department II "needs only 1,500 of means of production", and
`mistakes[2]` said the 500 is product "that Department II does not buy and
Department I must accumulate". In Volume II, Chapter 21 (vol. 2, l. 5216–5226),
Department I accumulates 500. Of that, 400 stays in Department I as constant
capital, and **100 is sold to Department II**, whose constant capital becomes 1,600.
The money from that sale pays Department I's extra workers. **Changed:** the body
paragraph, the quiz `why` and `mistakes[2]` now say this. The keyed answer
("Department I accumulates it as additional means of production") still stands,
because all 500 serves as means of production.

Also reworded in the same lesson: the one-sector preset is no longer called "the
world the error assumes". The dogma does not assume that there is no Department I;
it loses c. The lesson now says "as if no one had to make means of production,
which is where the error's arithmetic leads".

### 6. Illusions Created by Competition: the p. 996 table (softened)

The PNG shows the rate columns as "80 %" and "66 1/8%". At the scan's resolution
these 8s could be worn 3s. The lesson had called them flatly "misprinted".
**Changed:** the lesson now says that "in the scan" the columns read 80 and
sixty-six and one eighth, that the 8s may be broken 3s, and that even then the
second figure would still be wrong. This matters little, because the lesson uses the
text's figures, but a reader who opens a clean copy should not find the lesson
wrong about it.

### 7. Distribution Relations and Production Relations: two misattributions (fixed)

- "Earlier, in Chapter 48, Marx had said what the surplus is ultimately for." The
  realm-of-freedom passage (l. 6964–6968) does not say what the surplus is for; it
  says the realm of freedom lies beyond necessity and that its premise is a shorter
  working day. **Changed:** "Marx had looked past the realm of necessity … to the
  true realm of freedom beyond it".
- "The chapter ends on the conflict he expects between the two sides". In this
  lesson "the two sides" reads as distribution against production. At l. 7402 the
  conflict is between "the material development of production and its social form",
  that is, the productive forces against the historical form of production *and*
  distribution together. **Changed** to say so.

### 8. Distribution Relations…: Mill stated in Marx's terms, not his own (fixed)

`mistakes[0]` called "distribution can be changed without changing production
relations" "Mill's position". "Relations of production" is Marx's concept, not
Mill's. Mill put property among the institutions of distribution (*Principles*,
Book II) and hoped for workers' co-operatives (Book IV, ch. 7). That is a change
Marx would call a change in production relations. So this is Marx's reading of Mill,
and AUTHORING's rule is to describe each critic in his own terms. **Changed:** "This
is how Marx reads Mill … Mill's own line fell elsewhere: he counted property among
the institutions of distribution and hoped for workers' co-operatives."

## Checked and found sound

- **Chapter 48:** the three fragments (fn. 144), the missing folio (l. 6984), "stops
  short" (l. 6952) and the unfinished last sentence (l. 7036) are all as the lesson
  says. The Smith sentence is footnote 146. "Monsieur le Capital and Madame la
  Terre" is correct for the German edition. Credit to classic economy, with its
  limit, is l. 7030. Say's *Traité* (1803), Clark (1899), Wicksteed (1894), Robinson
  and Sraffa, and Samuelson's 1966 concession are dated and stated correctly. The
  `note` presents the marginal-productivity reading at strength.
- **Chapter 49:** the two questions, the two difficulties, the two reasons for
  returning to the problem, the scheme (l. 7092–7094), "chosen at random",
  gross/net output and income (l. 7104–7112), "the dream of men like Say",
  Ricardo's "Take a whole from a whole" (fn. 147), Smith's horse (fn. 148) and
  "revenue for one man and capital for another" are all accurate.
- **Chapter 50:** the 650 example and its rates, the effect-not-cause case, dearer
  food in agriculture leaving the yarn at 650 (l. 7224–7226), the circularity of the
  price of labour, competition and the 10/20/100%, the 125 example (4/5, 2/25, 3/25,
  then 137½), the persistence of the illusion without competition (point 3), the
  small farmer, and the cross-reference to "Wage Changes and Prices of Production"
  (Course 10 has that title). Sraffa (1960) is stated correctly.
- **Chapter 51:** the thesis, the misstatement, the two traits, profit as a factor of
  production, the landlord as "usurer in land", the Indian communes and the
  Peruvians, the foundations passage at the end of Chapter 50, the accounting remark
  at the end of Chapter 49, and Mises (1920), Lange (1936) and Hayek. Footnote 153
  names Mill's *Some Unsettled Questions* (Kerr prints "1884" for 1844). The lesson
  quotes the *Principles* for the view, which is accurate as two separate claims.
- **Chapter 52 and the course's close:** the three classes (l. 7408), England and the
  middle and transition stages (l. 7410), the question and the first answer
  (l. 7412–7415), and the objection that ends the book (l. 7417), quoted to its last
  word. In the three-volume summary, every clause is something the book argues:
  labour-time as value, surplus labour in the working day, circuits and turnover,
  proportionate reproduction of two departments, profit on the whole capital,
  prices of production, merchants, interest and profit of enterprise, rent. Quiz 4's
  keyed answer ("Nothing: the manuscript breaks off") and `mistakes[2]` correctly
  refuse to supply an answer. Lenin's 1919 definition ("A Great Beginning") and
  Weber's market situation are named in the `note` and not argued.
- **Quiz:** I tried to argue for every distractor in all 20 questions. After the
  Lesson 1 quiz 2 change, each has exactly one defensible answer. Lesson 4 quiz 2
  ("which appears in all three presets") could also be answered "a fund above
  consumption", but that is not among the options.

## Recommendations (taste; not changed)

1. **Lesson 3, `rent-rise` preset.** This preset uses the `added-up` view with
   `wage_change: 0`, so the kit's status line reads "…they would make £200, not the
   £200 that the year's labour produced", and it reports the old profit of
   enterprise at the *new* rent share. Either move the rent comparison to a `trinity`
   lab, or ask the kit owner to suppress the adding-up sentence when `wage_change`
   is 0. This is a kit matter, so I left it alone.
2. **Lesson 4, Mill paragraph.** "The tax-and-transfer states of the twentieth
   century were built on the same distinction" is the lesson's own sweeping
   historical claim. "Later arguments for redistribution have often rested on the
   same distinction" says what is needed without the verdict.
3. **Lesson 5.** "Argued over since Bortkiewicz" could read "since Böhm-Bawerk and
   Bortkiewicz", because Böhm-Bawerk's 1896 critique is where the dispute starts in
   most histories. In the same lesson, "finds it wanting" (`mistakes[2]`) is a
   little stronger than the text, which raises an objection and stops. "Raises an
   objection to it" would match the text more closely.
4. **Lesson 2.** "The weaver's yarn is the spinner's revenue" would be more exact
   as "part of the weaver's yarn is the spinner's profit" (l. 7166–7168).
5. **Lesson 1.** "Most economists teach some form of it today" and "Most economists
   still use the marginal theory" come one sentence apart and repeat each other;
   one could go.
6. **Voice.** I found nothing preachy or performed. "Marx is enjoying himself, and he
   means it" and "at his most sardonic" are the lessons' one light remark each, and
   each points at Marx's own joke, as §F asks. The second-person openings (savings
   account, national income, fairness arguments) are in the reader's world and
   reach the chapter's category within the paragraph.

## Where I disagree with the pedagogy assessment

Read after the findings above were written. The assessment's arithmetic, its
repairs (the scheme `math` block, "classic economy", footnote 146, the unfinished
last sentence, quiz 1's 700, the `classes` note) and its reading of the last lesson
agree with mine. Where we differ:

1. **The no-landlord preset (my finding 1).** The assessment cites "rent `£0` and
   profit of enterprise `£80` with the sum still £200" as the tile that refutes
   `mistakes[0]`, and it lists quiz 2 among the questions with sound answers. The
   sum is right, but putting the £30 into profit of enterprise contradicts Marx's
   own treatment of the owner-farmer (Ch. 50, l. 7330) and of the owner-capitalist
   (Ch. 23, l. 3411). The lesson should not teach that category in his name.
2. **Mill (my finding 8).** The assessment praises "This is Mill's position, and
   reforms of distribution are real" as stating a holder at strength. It states
   Mill in Marx's vocabulary ("production relations"), which AUTHORING's Course 1
   rule forbids. Mill himself put property on the distribution side and argued
   for co-operatives.
3. **The growing preset (my finding 5).** The assessment says the Volume II
   figures are "as the lesson says". The figures are, but the lesson's account of
   what happens to the 500 was not. Volume II sells 100 of it to Department II,
   and the quiz `why` said Department II "needs only 1,500".
4. **"Four with three" (my finding 4).** The assessment does not mention this. The
   lesson answered Marx's riddle about consumer goods with the Ic 4,000, which
   answers a different question.
5. **Roscher (my finding 2).** The assessment repeats "Roscher 'whom Marx names'"
   as good history-with-people. The quoted words were Marx's, not Roscher's.
6. **Chapter 48 → 51, realm of freedom and "the two sides" (my finding 7).** The
   assessment does not mention either. Both gave Marx a sentence the text does not
   contain.
7. **The p. 996 table.** The assessment treats "80" and "66 1/8" as certain
   misprints, and had the lesson say so. On the zoomed scan the 8s could be worn
   3s. I softened the lesson rather than reversing it.
8. **Footnote 144, "Part VI".** The assessment suggests this may be a Kerr
   misprint for Part VII. My understanding, which I did not check here, is that
   Engels' German note also says the fragments were found in the manuscript for
   Part VI (ground rent). If so, Kerr is faithful and the lesson's wording,
   which leaves the Part out, is the right choice either way.

I agree with its remaining issues on the `cooperative` preset's fitted shares
(3/5 and 2/5) and on the kit's "Annual product" label. My recommendation 1 (the
`rent-rise` preset's status line on the `added-up` view) is a related kit matter
that the assessment did not raise.
