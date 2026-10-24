# Second review: From Money to Surplus Value (`capital-money-into-surplus-value`)

Course 2 of the Capital read-along, package `content/capital/c02_surplus_value`,
Volume I, Chapters 4 to 11. Reviewed 2026-10-24 against the Kerr text
(`/mnt/project-files/capital-texts/volume-1-kerr.txt`), following
`docs/capital/SECOND-REVIEW.md`. These findings were written before the
pedagogy assessment was opened; the last section records where the two differ.

## Summary

- **Chapter numbering.** Every `module` and every chapter reference matches the
  Kerr (English) numbering: Part II is Chapters IV to VI, Part III is VII to XI,
  and the module titles are the Kerr chapter titles (Chapter 10 "The Working Day",
  with no hyphen; Chapter 8 with none either). No German numbering has crept in.
- **Arithmetic.** Every figure in prose, worked lines, quiz answers and `why`s was
  recomputed. No errors. The tiles of all 33 presets were read with
  `labcheck.js --observe` and agree with hand computation and with Marx's figures
  (27s to 30s; 90/90; 16, 2 and 2 lb; 80/52 = 153 11/13%; 19/23 = 82 14/23%;
  29/23 = 126 2/23%; 56/84; 150s twice; 600s against 1,500s).
- **Quotations.** The strict checker finds 120 quoted segments and 0 misses,
  before and after my edits. Convention-only matches: drop capitals ("The",
  "It"), the translator's double quotes rendered as single curly quotes
  (Senior's "analysis", "last hour", the "inalienable rights of man"), and
  passages split by OLL page-break lines (the Moneybags "embryo capitalist"
  phrase and the "free in the double sense" passage, which the checker reports
  with `l.?`). Two short phrases match only outside the chapter but are also in
  it ("once for all" is at l. 2473 in Chapter 10, "essentially different" in
  Chapter 8); I checked both in place.
- **What Marx argues.** Seventeen places in the lessons, and one course field, said more
  than, or other than, the text supports. The most serious is lesson 7, which presented the equality of wages
  and net profit, on which the whole 100% rests, as "Senior's own figures": it
  is Marx's supposition. All are fixed in the course files.
- **Quiz.** Every distractor was argued for; each has one defensible answer.
- **Preview.** `python3 scripts/preview_subject.py capital --course
  capital-money-into-surplus-value` prints `OK` after the edits (10 pages
  executed and swept, 10 with pinned figures, 0 failing).

## Findings and changes

### 1. The General Formula for Capital

1. **The note gave Marx's reply to the merchant's-services objection the wrong
   address.** It said Marx's reply to "carriage, storage, risk and waiting
   ... comes only once labour-power is on the market". Labour-power is Marx's
   general answer to where surplus value comes from; his account of the
   merchant's profit specifically is Volume III, Part IV (the chapter itself
   says merchants' and interest-bearing capital are "derivative forms" to be
   explained later). *Changed:* "Marx's general answer begins once
   labour-power is on the market; his account of the merchant's own share waits
   for Volume III."

### 2. Contradictions in the General Formula

2. **"Two sentences from its end" was wrong.** The passage is followed by "We
   have, therefore, got a double result" and a four-sentence paragraph ending in
   "Hic Rhodus, hic salta!". *Changed* to "from its closing paragraphs".
3. **Condillac's reply was spliced.** "Commodities are not paid for twice over"
   is Marx's reply to the later economists who used Condillac's argument to show
   that commerce adds value (the "Commerce ... adds value to products" footnote
   24), not to Condillac directly. *Changed* to say so.
4. **The `merchants` preset was described as a chain.** The prose said "three
   dealers who each add 10% to a producer's goods move £10 from the one party
   who does not mark up". The lab is a ring: each dealer sells the goods he
   holds, and the £10 moves from the producer to the dealer he sells to (dealer
   1: +£10; dealers 2 and 3: £0). *Changed* the body sentence and the summary to
   describe the ring.

### 3. The Buying and Selling of Labour-Power

5. **A verdict not in the text.** "Marx then says something that the economists
   he is reading did not" has no support in Chapter 6; what the text says is
   that the question "has no interest for the owner of money ... And for the
   present it interests us just as little." *Changed* to "Marx then adds a point
   that does not interest Moneybags at all."
6. **Rossi: Marx's reply reordered and slightly overstated.** The lesson had Marx
   "agree that the two cannot be separated", then add the digestion line as an
   afterthought. In the text the digestion line *is* the reply (Rossi conflates
   capacity with labour), followed by "we do not abstract from the necessary
   means of subsistence. On the contrary, their value is expressed in its value."
   *Changed* to that order.

### 4. The Labour Process and the Production of Surplus Value

7. **"Marx mocks it rather than refuting it here."** Marx does answer the
   capitalist in Chapter 7, twice: there is nothing to reward abstinence with
   because "the value of the product is merely the sum of the values of the
   commodities that were thrown into the process"; and "there is here no question
   of service ... here we are dealing with exchange-value". The lesson's line made
   Marx look as if he had only jeered. *Changed* to give both replies, and to keep
   open the question whether the twelve-hour 3s rewards waiting.
8. **Böhm-Bawerk was given marginal productivity.** The paragraph ran the
   productivity view (capital goods are productive, so part of the product is
   theirs) into Böhm-Bawerk's, which is about time preference and was written
   against naive productivity theories. *Changed* to state the two separately.
9. **"The factory's 'penal code of his own'".** The "his" is the capitalist's
   (l. 1795: "our friend has a penal code of his own"). *Changed.*

### 5. Constant Capital and Variable Capital

10. **"Marx's own objection to his term".** The objection that £90 of v is "a given
    and therefore a constant quantity" is raised (and answered) in Chapter 9, §1,
    not Chapter 8. *Changed* to "a difficulty Marx raises against his own term in
    the next chapter".
11. **"In the sixfold case the machine multiplies the yarn."** Marx's sixfold case
    is "some invention", not a machine. *Changed* to "an instrument helps make
    use-values, and an invention like the one in the sixfold case multiplies the
    yarn".

### 6. The Rate of Surplus Value

12. **"All the cotton's value is concentrated in the first 16."** In the text the
    cotton's value is in 13 1/3 lb and the 16 lb carry cotton and wear together;
    Marx says the transferred value was "intercepted in order to be incorporated
    in the 16 lbs. first spun". *Changed* to "all the value of the cotton and the
    wear is concentrated in the other 16". Also: the 1871 mill's £378 is cotton,
    wear, rent, coal, gas and oil; the lesson's "cotton, wear, rent and coal" now
    names all six.

### 7. Senior's "Last Hour"

13. **Marx's supposition presented as Senior's figures (the serious one).**
    Senior's £20,000 lumps "raw material and wages" together; his figures do not
    show wages. Marx's reply is conditional: "If the professor then found, that in
    accordance with the calculation of the manufacturers, the workman reproduced
    or replaced his wages in 2 half-hours, in that case, he should have continued
    his analysis thus" (Kerr l. 2037). The 5¾ / 5¾ split and the 100% rest on that
    supposition. The lesson said "On Senior's own figures" in the concepts, the
    body, the worked intro, a quiz stem, the note and the `one_line`. That makes
    Marx's reply look like a computation from Senior's data, which is stronger
    than what Marx claims, and hides the one step a defender of Senior would
    contest. *Changed* all six to name it as Marx's supposition about what the
    manufacturers' figures would show once wages are separated; the note now says
    the 100% rests on it. The arithmetic (19/23, 29/23, 17/23) is unchanged.

### 8. The Working Day: Its Limits and the Greed for Surplus Labour

14. **"The Russian-drafted code of 1831".** Marx says the Règlement organique was
    proclaimed by the Russian general Kisseleff but "of course dictated by the
    Boyards themselves". *Changed* to say both. Also softened figures restored:
    the Nottingham lace children (nine or ten years old) were at work "at two,
    three, or four o'clock in the morning ... until ten, eleven, or twelve at
    night"; the lesson had trimmed this to "two or three ... ten or eleven".
    *Changed* to the full range.

### 9. The Struggle for a Normal Working Day

15. **"Through the 1850s and 1860s".** The text says "the comparatively rapid
    advance since 1860": dye- and bleach-works 1860, lace 1861, earthenware and
    matches after the 1863 report; the bakeries came under a separate Act of 1863.
    *Changed* to "From 1860 the Factory Acts reached ... and an Act of 1863 reached
    the bakeries."

### 10. Rate and Mass of Surplus Value

16. **"Defers the solution to Volume III."** Chapter 11 says only that "many
    intermediate terms are as yet wanted"; its footnote 168 points to *Theories of
    Surplus-Value* for the Ricardians, not to Volume III. *Changed* to say what
    Marx says, and then that Volume III supplies the terms.
17. **The note overstated the exception.** It said that where the two assumptions
    fail "the mass no longer grows with the number of workers". The text: "There
    are exceptional cases in which the surplus-value produced does not increase in
    proportion to the number of labourers exploited, but then the value of the
    labour-power does not remain constant." *Changed* to that.

### Course fields

18. **`not_covered` had Marx arguing with Böhm-Bawerk.** "stated at their
    strongest where Marx argues with them" covered Böhm-Bawerk, who wrote after
    Marx. *Changed* to "where the lessons meet them", with a clause saying
    Böhm-Bawerk's are objections to the book, not positions it answers.

## Checked and found right

Worth recording because each is a place where a misstatement would be easy:
the three-party structure of both circuits; the coin, or the commodity, that
changes hands twice; Torrens and the towns of Asia Minor; Franklin and
Aristotle; Moneybags's double condition; the 365A + 52B + 4C average; the
physical minimum as below value; the worker who "gives credit to the capitalist";
the 6- and 12-hour mill sums and eighteenpence a pound; gold and steel spindles;
the self-acting mule; devil's dust (15 in 115); the £150 machine; land, wind and
water; the cotton at sixpence and a shilling and the speculators; £1,054 of
machinery giving £1,500 and £1,590; Jacob's acre (£3 11s on £3 10s, "assuming
that the price of the product is the same as its value"); 8 h, 1 h 36 min,
1 h 12 min, 1 h 12 min; Senior's £100,000, £115,000 and 23 half-hours, and his
three predictions; the "82 14/32%" misprint and the "11½ to 10" slip; James
Wilson in *The Economist*, 15 April 1848; working days I to III; the worker's
1/10,950 against 1/3,650; the corvée's 14, 42 and 56 days and 56/84; Horner's
5 h 40 min and 27 days; "one thousand a year"; William Wood, the bakers'
42, Mary Anne Walkley (20, 26½ hours), the blacksmith's 37 for 50; the
Sanderson evidence on idle furnaces; 1349 and 1496; the "House of Terror";
five Acts 1802–1833 with no money for enforcement; the Act of 1833's 5.30 to
8.30 and its 12 and 8 hours; 1844's adult women and public clock; 25% wage cuts;
Horner's 70%; the relay hours of 13½ and 15; Eskrigge's magistrates; the
Exchequer, 8 February 1850; 10½ and 7½ hours between 6 and 6; Baltimore
(16 August 1866) and Geneva; France's 12-hour law; Chapter 11's three laws,
its 150s, 1,500s, 600s and 1,200s, the 8-hour worker and the eightfold minimum,
Hegel, and Carlile of Paisley in the *Glasgow Daily Mail*, 25 April 1849.

External facts checked: Senior was the first Drummond Professor (1825) and the
abstinence theorist; *Letters on the Factory Act* is 1837; Wilson founded *The
Economist*; Böhm-Bawerk's *Karl Marx and the Close of His System* is 1896;
Condillac and Rossi (Collège de France) are described accurately.

## Recommendations (taste; not changed)

- **Lesson 7, "The question of whether the arithmetic of the last hour is right
  is settled".** True on the lesson's assumptions, but it is the lesson's own
  verdict in a paragraph that otherwise states Senior's side at strength. Consider
  "On the lab's assumptions the arithmetic of the last hour is settled".
- **Lesson 3, "one of the most quoted in the book".** A harmless lesson verdict;
  the passage needs no billing.
- **Lesson 6's closing line** names the next lesson as Senior's "last hour" rather
  than by its title, Senior's “Last Hour”; §F asks for the title.
- **Course `how_to`, "the next five lessons all return to it".** Lessons 5 and 7
  use a £ mill and Senior's mill, not the 3s spinner. "Most of the next lessons"
  would be exact.
- **Lesson 9's `ten-hours` preset label** ("ten hours from May 1848") and the
  1847 Act's 11 hours from July 1847 are both right; a reader may want an
  `eleven` preset (2/3 would become 5/6) to see the staged cut, but it is not
  needed for the lesson's objective.
- **Lesson 3, the `training` preset** calls 2,190 hours "a year of training"; that
  is 365 six-hour days. Saying so in the label would stop a reader dividing by
  eight or ten.

## Where I disagree with the pedagogy assessment

Read after the findings above were written
(`docs/pedagogy/capital-money-into-surplus-value.md`). We agree on the
arithmetic, the quiz, the speech, the two Chapter 9 misprints, and on its
remaining issues about the `senior` view's second tile and the 7-day week. As
with Course 1, the disagreements are all in passages the assessment praised.

- **Senior "on his own figures".** The assessment's verdict says a reader can
  "recompute Senior's last hour on his own figures", and it recommends the
  Senior lesson as the template for later courses because it gives "the
  opponent's own figures, Marx's recomputation". The equality of wages and net
  profit is not in Senior's figures; Marx introduces it with "If the professor
  then found..." (finding 13). The template is good, but only once the
  supposition is named, which it now is.
- **Condillac.** The assessment repaired the case of "commodities are not paid
  for twice over" and kept the sentence that made it Marx's reply to Condillac.
  It is his reply to the later economists who argued that commerce adds value
  (finding 3).
- **Lesson 4's objection paragraph.** The assessment lists "Böhm-Bawerk's
  interest theory behind the abstinence joke" among the positions stated at
  strength. The paragraph gave Böhm-Bawerk the productivity view he argued
  against, and said Marx "mocks it rather than refuting it", when Chapter 7
  contains two replies (finding 7, 8).
- **The `merchants` preset.** Praised for "showing where the £10 came from";
  the prose said the dealers "each add 10% to a producer's goods", which is
  not what the ring computes (finding 4).
- **Rossi.** Listed among the opponents given the fact their view rests on.
  The opponent was stated fairly; Marx's answer was reordered and had him
  "agree that the two cannot be separated" (finding 6).
- **History in lessons 8 and 9.** The assessment says every historical figure
  is "where the lessons say they are". Three were not quite: the 1831 code was,
  in Marx's words, "dictated by the Boyards themselves", not "Russian-drafted";
  the Nottingham hours were trimmed; the extensions of the Acts came "since
  1860", not "through the 1850s and 1860s" (findings 14, 15).
- **"Marx's peasant" (its first remaining issue).** I disagree that the word is
  the lesson's: Kerr l. 1437 has "in the hands of the peasant who sells corn".
  The label is Marx's and should stay.
- **"Every body ends with one sentence naming the next lesson by its exact
  title."** Lesson 6 names it as Senior's "last hour", not by title (left as a
  recommendation).
- **Counts.** The assessment says 31 pinned strings; the ten pages pin 63 (33
  presets, two tiles each except lesson 3's one). It also counts 119 quoted
  segments; after my edits there are 120 (the word "service" in lesson 4).
