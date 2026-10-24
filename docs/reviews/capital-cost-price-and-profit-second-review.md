# Second review: Cost Price and the Rate of Profit (`capital-cost-price-and-profit`)

Course 9, package `content/capital/c09_profit`, Volume III, Part I (Chapters 1 to 7).
Reviewed against the Kerr text (`volume-3-kerr.txt`, ll. 450 to 1571, and Engels'
preface, ll. 288 to 300) on 2026-10-24, following `docs/capital/SECOND-REVIEW.md`.
I wrote the findings below before reading the pedagogy assessment.

## Summary

- **Arithmetic: no errors.** I recomputed every figure in the prose, the worked
  lines, the quiz answers and the `why`s, and read every preset's tiles with
  `labcheck.js --observe`. All 27 presets agree with my own arithmetic and with
  Marx's and Engels' figures where a label says the figures are theirs. Engels'
  Manchester mill is exact: annual p′ = 2,703/8,125 = 33.27% at n = 8½. His check
  figure 4,160/12,500 = 33.28% is what the exact n = 2,704/318 gives.
- **Quotations: 72 segments, 0 misses** (strict checker, before and after my edits).
  No convention-only cases were flagged.
- **Misrepresentation: six places where a sentence said more than the text does.**
  The worst are a characterisation of Ricardo that the chapter does not make, a
  mistake text that gives Marx the capitalist's phrase "a saving in buildings",
  and a Chapter 6 paragraph that made Marx seem to deny that a high price calls
  out new supply, which he explicitly grants. All six are fixed.
- **Quiz:** one distractor in “The Effect of Turnover on the Rate of Profit” could
  be argued for. Fixed.
- **Voice:** warm and plain throughout. There is one lesson-voice verdict ("made the
  argument carefully"), now neutral.

Final preview line after the edits: `OK` (8 pages rendered; labcheck 7 pages
executed, 7 with pinned figures, 0 failing).

## Findings and changes

### 1. The Rate of Profit and the Rate of Surplus Value: Ricardo's reasoning (fixed)

**Was:** "Ricardo … reasoned as if the composition of capital stood still" (body),
and in `mistakes[0]`: "It holds only if the composition stays put, and Ricardo
reasoned as though it did."

**Problem:** The chapter (l. 849) says only that the wage case, with composition,
working day *and* intensity constant, "is the only one in which Ricardo's
assumption is correct". It does not describe how Ricardo reasoned. The lesson also
narrowed Marx's three conditions to one. Ricardo did in fact discuss unequal
proportions of fixed and circulating capital (Principles, ch. 1, §§4–5), so a
general verdict about how he reasoned is open to dispute, and it is not Marx's here.

**Changed to:** "Ricardo was the stockbroker whose *Principles* of 1817 dominated
English economics for a generation; on this chapter's reckoning his rule is one case
among many." In `mistakes[0]`: "It holds only if the composition stays put, the one
case in which, Marx says, Ricardo's rule that profits rise as wages fall is correct."

### 2. Economy in the Use of Constant Capital: "a saving in buildings" is the capitalist's phrase (fixed)

**Was** (`mistakes[0]`): "which is why Marx files the crowded room under 'a saving
in buildings'."

**Problem:** At l. 1143 Marx reports the phrase as "the language of the capitalist",
in irony. The lesson made it Marx's own classification. The body paragraph had it
right.

**Changed to:** "which is why, in Marx's phrase, the capitalist calls the crowded
room 'a saving in buildings'."

### 3. Economy in the Use of Constant Capital: Adam Smith and the 1829 report (fixed)

**Was:** "Adam Smith argued that wages vary with the hardship and danger of a trade,
so that dangerous work is paid a premium and the risk is priced …" followed by "The
evidence it sets against the idea is the 1829 report it quotes".

**Problems:**

- Smith's five circumstances (Wealth of Nations, I.x) begin with "the ease or
  hardship, the cleanliness or dirtiness" of an employment. On danger in particular
  he argued the opposite of the lesson's claim: through "the contempt of risk",
  soldiers and sailors are *not* paid in proportion to the danger. The view that
  risk is priced belongs to the later theory of compensating differentials. The
  lesson said that theory was built on Smith, which is right, but it put the
  theory's conclusion in Smith's mouth.
- "sets against the idea" makes Marx answer Smith, and the next sentence says the
  chapter does not take up Smith.
- The report Kerr dates "April 21, 1829" is the Children's Employment Commission's
  First Report (Mines), published in 1842. The date in the text is wrong, and the
  lesson repeated it as fact.

**Changed to:** Smith's own wording for the circumstance ("the ease or hardship, the
cleanliness or dirtiness"), with the premium-for-danger conclusion given to the later
economists. Then "What in it bears on the idea is the mines report it quotes, dated
1829 in the text (the Children's Employment Commission reported on the mines in
1842) …". The quotations from the report are unchanged.

### 4. Price Fluctuations of Raw Materials: Marx grants that price calls out supply (fixed)

**Was:** "Economists who trust prices to balance the two hold that the high price
itself calls out new supply … What the chapter sets against that is its observation
that the supply … is extended 'only convulsively'." The same paragraph said
machinery "can be multiplied in a year".

**Problem:** At ll. 1390–1392 Marx lists exactly that response: a high price brings
raw material from greater distances, increases production "which, however, for
natural reasons, will not be felt until the following year", and draws in "remote
and hitherto little noted" regions. He does not deny that price calls out supply.
His claim is that the supply comes late and all at once, overshoots and collapses.
As written, the lesson gave Marx a weaker position than his own and set up the
economists against a claim he does not make. "In a year" is not in the text, which
says "a very short time".

**Changed to:** "… and Marx grants the first step: a dear raw material is shipped
from further away and planted more widely, though the new crop is not felt until the
following year, and the inspectors' figures show Indian and Egyptian cotton arriving.
What the chapter adds is that the supply comes late and all at once, so that the
production of raw materials is extended 'only convulsively' …". "In a year" became
"in a very short time".

### 5. Supplementary Remarks on Profit: "at least, in part" (fixed)

**Was** (concept "Business ability"): "it persuades him that his profit comes from
his own activity."

**Problem:** Marx (l. 1550) says the capitalist concludes that his profits are due
"at least, in part" to circumstances other than exploitation. The concept dropped the
qualifier. The body quotes the sentence correctly.

**Changed to:** "… that his profit comes, at least in part, from his own activity."

### 6. Cost Price and Profit: a lesson-voice verdict on Torrens (fixed)

**Was:** "Robert Torrens … made the argument carefully."

**Problem:** This is a verdict in the lesson's own voice. Marx's own description
(l. 547) is that the illusion "was reaffirmed by Torrens … as an advance of political
economy beyond Ricardo", which is not praise.

**Changed to:** "put the argument this way."

### 7. The Effect of Turnover on the Rate of Profit, quiz 2: a defensible distractor (fixed)

**Was:** the distractor "Because its rate of surplus value is 200%" to the question
of why capital A's annual rate is 40%.

**Problem:** Capital A's *annual* rate of surplus value, s′n, is exactly 200%, and
`p′ = s′n·v/C = 2 · 20/100 = 40%`. That makes the distractor a correct explanation
in the chapter's own terms (Engels' S′). The `why` says "s′ is still 100% per
turnover", so the intended reading was the per-turnover rate.

**Changed to:** "Because its rate of surplus value per turnover is 200%", which is
false. The keyed answer (40 on the 100 advanced, not on the 200 turned over) is
still the only defensible one.

### 8. Small accuracy edits (fixed)

- Price Fluctuations of Raw Materials, quiz 1 `why`: "33.33% divides by c alone".
  The new c is 400, which gives 25% and is the second distractor. 33.33% is 100/300,
  the *old* c. Now "divides by the old c alone".
- Economy in the Use of Constant Capital, quiz 3: the keyed answer said "in cotton
  growing and transport". At l. 1090 the sentence says "the cultivation of cotton and
  the building of machinery". Transport economies are a separate case that the
  chapter postpones (l. 1102). Now "in cotton growing, outside the spinnery".

## Checked and found right

These are claims a careful reader would test. Each one has its supporting line.

- Chapter 1: the £500/£1,200/£1,680/£1,780 accounts (ll. 456–533); the price
  changes in c (£700/£800) and in v (£550, value unchanged at 600) (l. 484); Marx's
  five sales £510–£590 (l. 541); "peculiar market combinations" below cost (l. 537);
  Torrens' corn and Ramsay's reply (ll. 549–551); the Proudhon yarn, 20 lb at 30s,
  2 lb surplus (ll. 557–559); Marx's opening on "the surface of society" (l. 454).
  Marshall's normal profits in the supply price (1890) are stated fairly, and the
  lesson says that Marx could not answer him.
- Chapter 2: both definitions, "lumps them all together", "no basis", "the same
  thing and numerically equal", the Ricardian school's two-way error, the fixed and
  circulating distinction as "the only one which obtrudes itself" (ll. 569–613). The
  list Ramsay, Malthus, Senior, Torrens is in the chapter. Senior's abstinence and
  Böhm-Bawerk's time preference are each in their author's own terms.
- Chapter 3: every capital in the presets and prose is Marx's (ll. 749, 841, 930,
  938). 90c + 10v + 15s against 80c + 20v + 20s is his case 4. The "accidental
  coincidence" and "as a rule" between countries are right (ll. 938–942). Engels'
  preface on Samuel Moore is right (l. 300). Okishio (1961) is stated accurately.
- Chapter 4: Engels' authorship and brackets ("F. E."), capitals A and B, I and III,
  the halved case, the cash-box, the Manchester mill (£10,000, £2,500, 2,182/318,
  2,704, 8½, 153 11/13%, 33.27/33.28%), the "brave soul", and the American Census
  close (ll. 966–1058).
- Chapter 5: 18 hours for 12; scale, social labour and "the capitalist thus
  appropriates"; c = 0 as the maximum (l. 1110); 15 deaths a week; the single shaft;
  the National Association (1854; £50,000 in March 1855 at 2s per horse-power); the
  Glasgow £9 1s against £11 on 110 horse-power; "killing is no murder"; 263 per 100
  in Manchester; rags £4 4s to £44; gas-tar into aniline; the bankrupt first
  inventors (ll. 1143–1272).
- Chapter 6: the law and its qualification, the waste figures (½d, 1d, 6d at 2s),
  Greg and the Ten Hours Bill, the stocks that may "more than make good that loss",
  2,000c + 400v + 600s at 25% against 2,000c + 500v + 500s at 20%, 4d to 6d in 1847,
  Blackburn's stocks, and 50.7% unemployed in Lancashire and Cheshire in October
  1862 (ll. 1290–1500).
- Chapter 7: Engels' blank; businesses A and B at 10% and 8 1/3%; "wholly to a
  difference in business ability"; Rodbertus and the two cases (gold; nC and C/n at
  constant composition) (ll. 1544–1558). The gold preset's 120c + 30v split is
  correctly flagged as illustrative.
- `how_to`'s account of Engels' sources for Part I matches the preface (l. 298:
  two eight-page rewrites for Chapter 1, Chapter 2 from the main manuscript,
  Chapter 3 from the 1870s equations via Moore, Chapter 4 only a title).
- Module names match the Kerr chapter titles.

## Recommendations (taste, or not certain enough to change)

1. **Tugan-Baranovsky's date** (The Rate of Profit and the Rate of Surplus Value).
   The lesson says "argued in 1901". His sustained critique of the falling rate of
   profit is usually cited from *Theoretische Grundlagen des Marxismus* (1905). The
   1901 *Studien* is mainly about crises and disproportion. I am not sure enough to
   change it. Please check the source; if it cannot be confirmed, "in the early
   1900s" is safe.
2. **Price Fluctuations of Raw Materials, `summary`:** "where the case with no profit
   left was the real one" goes further than the inspectors' reports. They record short
   time, closures and materials "quoted above the price at which they could be
   worked", not a measured zero profit. Suggested wording: "where mills ran short time
   or stopped because the dearer cotton could not be worked at a profit".
3. **Chapter 7's `prRate` label in the books view** reads "Rate of profit on cost".
   For business A and B Marx's rate is on the capital advanced. The figures coincide
   only because the lab treats c as wholly consumed. The `note` could say so in one
   clause, the way the Chapter 2 note does for fixed capital.
4. **The Effect of Turnover on the Rate of Profit, worked lines** print `£1000` while
   the prose prints `£1,000`. This was presumably done so the read-out does not split
   the number at the comma. A spoken form for `C = 900 + 100 = £1,000` would let the
   grouping match the rest of the course.
5. **Price Fluctuations of Raw Materials:** the Blackburn line is quoted inside the
   paragraph on §2 ("The second section … The inspectors saw it"). The passage is
   actually in §3, the history (the October 1862 report). That is harmless, but
   "Later, in the history, the inspectors saw it in Blackburn" would place it.
6. **The Effect of Turnover on the Rate of Profit, `mistakes[0]`** ("turnover affects
   only the circulating capital's profit"): the refutation is correct, but it shows the
   whole-capital rate moving rather than saying why the fixed capital's share cannot be
   separated out. One sentence would make it bite: the 10,000 of fixed capital is in
   the denominator whatever the turnover, so no separate "fixed capital's rate"
   exists to stay put.

## Where I disagree with the pedagogy assessment

I read `docs/pedagogy/capital-cost-price-and-profit.md` after writing everything above.
We agree on the arithmetic, the quotations, the speech, the Engels framing and the
four repairs it made. We also agree on two recommendations: the books view's "on
cost" label (my recommendation 3), and, with one clause, Engels' capital II in
lesson 4. I disagree in these places:

1. **Adam Smith and the 1829 report.** The assessment praises lesson 5 for naming
   "Adam Smith's compensating differentials" and for setting against them "only what
   the chapter quotes (the 1829 report …)". Both halves of that passage were wrong.
   On danger, Smith argued that risk is *under*-paid, through "the contempt of risk",
   not that it is priced. The report is the Children's Employment Commission's of
   1842, which the Kerr text misdates. "Sets against" also had Marx answering Smith,
   which the next sentence denied (finding 3).
2. **"Every distractor was argued for and none could be defended."** One could be:
   capital A's annual rate of surplus value is 200%, and that explains its 40% in
   Engels' own formula (finding 7).
3. **Ricardo.** The assessment repaired the scope of Marx's "only one" case, which
   was right. But the sentence it left beside that repair, "Ricardo … reasoned as if
   the composition of capital stood still", and the same claim in `mistakes[0]`,
   still give Ricardo a verdict the chapter does not contain. The assessment lists
   Ricardo among the critics "at strength". I do not think he was (finding 1).
4. **"Only convulsively" and the supply response.** The assessment lists the phrase
   among the figures and phrases that are "in the text where the lessons say they
   are". The words are, but the paragraph around them set economists who say price
   calls out supply against Marx, when Marx grants that step in the same pages. It
   was faithful in its quotation and unfaithful in its argument, which is the kind
   of error these second reviews exist to catch (finding 4).
5. **"A saving in buildings."** The assessment quotes lesson 5's body use of the
   phrase approvingly. The `mistakes[0]` use of it, which made the phrase Marx's own
   classification, was not caught (finding 2).
6. **Tugan-Baranovsky.** The assessment counts him among the critics who are "dated".
   I am not confident that 1901 is the right date for his falling-rate critique
   (recommendation 1).
7. **Lesson 4's `mistakes[0]`.** The assessment says every `mistakes[0]` is refuted
   with a tile. That is true, but in lesson 4 the tile shows the whole-capital rate
   moving without saying why no separate "fixed capital's rate" exists. This is a
   recommendation, not a defect (recommendation 6).
8. **Lesson 3's critic paragraph.** The assessment suggests that the Tugan-Baranovsky
   and Okishio paragraph could move to Average Profit and Its Fall. I would keep it
   here. It is where the chapter's arithmetic, s′ up and p′ down, is first available,
   and it is short. This is taste.
