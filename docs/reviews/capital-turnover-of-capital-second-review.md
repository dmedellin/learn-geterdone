# Second review: The Turnover of Capital (`capital-turnover-of-capital`)

Reviewer: independent second read, 2026-10-24, against the Kerr Volume II text
(`/mnt/project-files/capital-texts/volume-2-kerr.txt`, Chapters 7–17, ll. 1428–3593),
with Volume I and III consulted where a lesson points to them.

Method: each chapter read whole; every sentence that says what Marx (or Smith,
Ricardo, Engels, a critic) argues checked against a line; every figure in prose,
worked lines, quizzes, `why`s, mistakes and notes recomputed; every preset's tiles
read with `node scripts/labcheck.js --observe`; quotation checker run before and
after the changes.

## Summary

- **Arithmetic:** all 37 presets' tiles agree with my own computation and with
  Marx's figures where the label claims them. One `why` was wrong (lesson 6).
  No other arithmetic error.
- **Misrepresentation and attribution:** nine places fixed, the two the brief
  named among them. The wine cellar (lesson 7) and Bailey and Torrens (lesson 10)
  were both presented as if from the chapter, and they are not. The most
  substantive new finding is in lesson 4: it presented a classification by
  Marx's turnover test as "Smith's split". In the same lesson it quoted Marx
  showing that on Smith's own test the whole mine would be fixed capital.
- **Quotations:** `strict_quotes.py c07_turnover 2` gives 87 segments with 0
  misses before the changes, and 88 with 0 misses after (one short quotation
  added). The only differences are conventions: the translator's inner double
  quotes are printed as single curly quotes (`the confounding of the categories
  'fixed capital…'`), and a few short spans match an earlier identical line
  first (`maintenance` l. 239, `under all circumstances` l. 2046,
  `From the point of view of the capitalist…` l. 869). Each also occurs at the
  cited line (ll. 1843ff, 2904, 1459).
- **Quiz:** one `why` corrected. I argued every distractor and none is
  defensible as a right answer.
- **Final preview:** `11 page(s) executed and swept, 11 with pinned figures,
  0 failing` / `OK`.

## Findings, by lesson

### 1. Turnover Time and the Number of Turnovers (Ch. 7)

- **Voice.** "His reason is agricultural, and a little quaint". "Quaint" was
  the lesson's own verdict on Marx. *Changed* to "His reason is agricultural:".
- **Note incomplete.** The note says the 9 + 4 split of three months is
  illustrative, but the `eighteen-months` preset splits 78 weeks into 65 + 13,
  which is just as invented. *Changed* the note to name both splits.
- Checked and right: n = T/t notation (l. 1455), C′…C′ unusable for turnover
  (l. 1442–1444), Newman and Chalmers (l. 1446), all tiles (13 weeks, 4, £1,600;
  52/5, £5,200; 2/3, £400 on £600).

### 2. Fixed Capital and Circulating Capital (Ch. 8)

- **Misstatement (concept "Wear and repair").** It said repairs "count as
  circulating capital". Marx calls the repair capital "a peculiar capital, which
  can be classed neither with the circulating nor the fixed capital, but still
  belongs with more justification to the former" (l. 1612). *Changed* to say
  they fit neither cleanly but belong with more justification to circulating
  capital.
- **Misattribution.** "Marx calls this virtual wear, later readers call it moral
  depreciation." Marx's own Volume I, Chapter 15 (Kerr vol. 1, l. 3078) calls it
  "a moral depreciation". *Changed* so that Marx is credited with both terms.
- **Voice / unsupported attitude.** "He records, with evident pleasure, how
  elastic the boundary…". Nothing in l. 1630 supports "pleasure". *Changed* to
  "He notes how elastic…".
- **Note loose.** "The £10,000 and the fifteen years booked as ten are his
  figures, which he says were chosen at random." What Marx says is that "the
  figures 10 and 15 are chosen at random" (l. 1616). *Changed*, adding that the
  `moral` preset's revaluation (the old machine is worth what a new one costs)
  follows Volume I's account of moral depreciation (vol. 1, l. 3078). The
  lesson had not given that rule a source.
- Checked and right: the passage (l. 1479), the ox (l. 1487), the fundamental
  mistake (l. 1499), the reserve fund (l. 1514), Lardner's £40,000/£30,000
  (l. 1564), 2,000/3 + 1,000/3 (l. 1614), all tiles, and the quiz repair
  allowance (£1,500 − £1,000 = £500).

### 3. The Aggregate Turnover of Advanced Capital (Ch. 9)

- **Overstatement.** "Moral depreciation shortens the life of fixed capital as
  fast as engineering lengthens it". Marx says only that it is "on the other side
  shortened" (l. 1718), not at the same rate. *Changed* "as fast as" to "even as".
- Checked and right: 108,000/100,000 = 27/25 (about 11.1 months); the "1+2.25"
  slip; £72,000 and nine years (l. 1714); the hedge (l. 1718); Scrope's second
  case 1,250 + 12,500 + 50,000 = 63,750 (ll. 1734–1744), and Marx's real quarrel
  with Scrope (l. 1750). The lesson does not repeat Marx's "Scrope, an American
  economist" (Scrope was English, adapted by Potter); good. The heavy and light
  presets (69/200, 201/50) are right.

### 4. The Physiocrats and Adam Smith on Fixed Capital (Ch. 10)

- **Misrepresentation (the main finding of this review).** The body said:
  "Then compare Smith's farmer with a copper mine. Both split £600 fixed and £400
  circulating." The summary said: "Sort the same productive capital by Smith's
  two categories". The `farm` preset was labelled "Smith's farmer: … fodder,
  seed and wages circulating". But Smith says "The whole value of the seed, too,
  is a fixed capital… it never changes masters" (l. 1851), and Marx spends a
  paragraph refuting it (ll. 1853–1855). On the mine, the lesson itself quotes
  Marx: "According to Adam Smith's own definition, the entire capital employed in
  mining would consist only of fixed capital" (l. 1814). The £600/£400 splits
  are Marx's turnover test applied to Smith's examples, not Smith's split.
  *Changed:*
  - The body now says both are sorted by Marx's test, not Smith's; that Smith
    called the seed fixed because it "never changes masters"; and that on his
    test the mine would be all fixed.
  - The preset label now reads "sorted by Marx's test".
  - The summary now reads "as fixed or circulating".
  - The §C entry in `docs/capital/PLAN.md` is corrected to match.

  The mill paragraph's "Smith's split" stays. There Smith and Marx agree: the
  machine is fixed, and materials and wages are circulating (l. 1807).
- Checked and right: Quesnay's avances (l. 1764), Smith "far inferior" (l. 1770),
  capital of circulation (l. 1788), the machine-maker's machine (l. 1802), wages
  and the labour fund (ll. 1952–1954). Mill's recantation of the wage-fund
  doctrine (1869) is accurate. It is the lesson's history, not the chapter's,
  and is plainly offered as such.

### 5. Ricardo on Fixed and Circulating Capital (Ch. 11)

- **Lesson's own verdict given as Marx's ground.** "Marx's test is the manner in
  which value passes to the product, and on that test the line can be drawn
  exactly." The chapter does not claim exactness, and Chapter 8 concedes that the
  repair/renewal boundary "is more or less shifting" (l. 1630). *Changed* to "a
  test of the part a thing plays in production and not of how long it lasts".
  This is l. 1999–2005 and l. 2056.
- **Voice.** Ricardo "honestly lists the exceptions" was the lesson's own
  praise. *Changed* to "then lists the exceptions".
- Checked and right: the two differences run together (l. 1968), "contribute
  equally" (l. 1970), raw material disappears (l. 1975), Ricardo's definition and
  disclaimer (ll. 2023–2025), farmer and baker (l. 2054) with Marx's reply
  (l. 2056). The lesson's Sraffa paragraph states the opposing case at strength
  and correctly says Marx concedes it for prices of production.

### 6. The Working Period (Ch. 12)

- **Arithmetic in a `why`.** In the ship question, "£6,250 is a quarter of the
  right answer, as if the period were 25 weeks". £6,250 is 5/8 of £10,000, not a
  quarter. *Changed* to "£6,250 multiplies by 25 weeks instead of 40".
- **Date loose.** "By the 1850s a London contractor told a parliamentary
  committee". The text names the banking committee of 1857 (l. 2116, l. 2118).
  *Changed* to "In 1857 … the parliamentary committee on the Bank Acts".
- **Voice.** "Marx lists it with relish". *Changed* to "Marx lists it".
- **Recommendation (not changed).** "A crisis that halts a ship or a house
  half-built wastes all of it." Marx says the means and labour expended "are
  wasted", and that "even if work is resumed, a deterioration has taken place"
  (ll. 2092–2094). "All of it" reads more absolutely than the second clause
  allows. Consider "wastes it, or spoils it even if the work resumes".
- Checked and right: the passage (l. 2090), twelve times the circulating capital
  (l. 2082), the steam engine (l. 2096), the contractor's "twenty to fifty times"
  and Belgravia (ll. 2116–2118), railway armies (l. 2124), Bakewell (l. 2142),
  and the tiles £100, £1,200, £5,200.

### 7. The Time of Production (Ch. 13)

- **Material attributed to the chapter that is not in it (brief's item).** The
  lesson told the wine-cellar puzzle as if Chapter 13 discussed it: "John Ramsay
  McCulloch and James Mill … faced the old puzzle of wine that is worth more
  after years in a cellar … Marx calls these 'senseless theories' … and promises
  the answer in Volume III, where profit on the waiting capital is explained by
  the equalisation of profit rates". Chapter 13 has one sentence on them
  (l. 2210) and no cellar. The chapter's wine is only grape juice that must
  ferment (l. 2158) and "(wine, seed grain)" in a list (l. 2208). The cellar is
  from Mill's *Elements* and McCulloch's own writings. Volume III as published
  (Kerr) never returns to MacCulloch or James Mill on this. McCulloch appears
  there only as Ricardo's editor (vol. 3, ll. 849, 7487, 7489), and its "wine in
  a cellar" (vol. 3, l. 3551) is about interest-bearing capital. The original
  also merged the two men's positions.

  *Changed* the paragraph so that:
  - it quotes the chapter's one sentence;
  - it says the promised Volume III treatment does not take them up by name;
  - it says the cellar case comes from their own books;
  - it separates Mill (the year in the cellar reckoned as more labour) from
    McCulloch (nature's operations count as labour);
  - it leaves the equalisation of profit rates as where, on Marx's terms, the
    answer lies.

  *Changed* to match: the quiz `why` ("the wine in the cellar, their standard
  case, comes from their own writings, not from this chapter") and mistake 3
  (now McCulloch's way out, "one of the theories Marx calls senseless").
- Checked and right: the passage (ll. 2154, 2158), tanning (l. 2164), Bessemer
  and fixed capital (l. 2166), shoe-lasts (l. 2168), Kirchhoff's 170–215 days
  (50+65+55, 60+80+75; ll. 2171–2172), Russia (l. 2174), Hodgskin (l. 2181),
  forestry (l. 2191), and every tile (1, 1/3, 1/4; 1/100, 1/200; 13/14, 1/13,
  1/14; 13/3, 1/2, 1/3).

### 8. The Time of Circulation in the Turnover (Ch. 14)

- **Overstatement.** "Trade with the East ran on bills of exchange of six or ten
  months, and the turnover was the reason". Marx calls turnover differences "one
  of the material bases of the various terms of credit" (l. 2244). *Changed* to
  "turnover was part of the reason".
- **Attribution unsafe.** "Engels adds in a bracket that the Suez canal has
  since revolutionised all of it." The Kerr text prints the sentence in plain
  parentheses (l. 2246) with no "F. E.". Manuscript II dates from around
  1868–70, and the canal opened in 1869, so Marx could have written it.
  *Changed* to "a bracketed sentence adds".
- **Attribution to the wrong chapter.** Mistake 1: "If a merchant buys the goods,
  Marx notes, he simply advances that additional capital in the manufacturer's
  place." That is Chapter 16, §3 (l. 3268), not Chapter 14. *Changed* to "Marx
  notes in Chapter 16".
- **Ambiguity.** "A market two months away and back" could be read as two months
  each way. The preset is 26/3 weeks in all, a month each way. *Changed* the body
  to "a month away, two months there and back", and the worked `after` to "a
  month each way".
- Checked and right: the India passage (ll. 2228, 2244), "fettered" (l. 2232),
  the railway and relative distance (l. 2232), sailings (l. 2234), the 1866
  usance episode (l. 2246), wool auctions (l. 2264), money capital forgotten
  (l. 2274), and the tiles 26, 2, 1/3; 52, 1, 2/3; 104/3, 3/2, 1/2. The panel's
  "last-but-one tile" is right, because the time view prints an empty "Value
  turned over" tile last.

### 9. Turnover Time and the Capital Advanced (Ch. 15)

- **Overstatement of Engels.** "Engels says it gave him the most trouble." His
  note says "no small amount of difficulties" (l. 2889). *Changed* to "preparing
  it gave him no small trouble".
- Checked and right:
  - the opening example (l. 2284);
  - £75 a week (l. 2288);
  - 300 as a quarter of 1,200 (l. 2298);
  - £300 set free (l. 2312);
  - the "hollow skulls" (l. 2372);
  - one part in production, one in circulation (l. 2374);
  - the rule (ll. 2851–2857), which the lesson states correctly in its
    multiple-of-working-period form;
  - 900 → 800 (l. 2881);
  - 2/9, which is £200 (l. 2887);
  - Engels' note, his "under all circumstances" (l. 2904) and "a considerable
    portion … in the form of money" (l. 2906);
  - prices halve, £450 (l. 2912).

  All five presets' tiles agree with the rule. The course `how_to`'s "kept only
  the figures that were arithmetically correct" is a fair paraphrase of "I have
  preserved only the simplest and arithmetically correct data".

### 10. The Turnover of Variable Capital (Ch. 16)

- **Material attributed to the chapter that is not in it (brief's item).** "Their
  critics, Samuel Bailey and Robert Torrens among them, pressed exactly that
  point." Neither name appears in Chapter 16. Bailey appears nowhere in Volume
  II's main text. Chapter 16 says only that the phenomenon "has completely routed
  the Ricardian school since the beginning of the twenties" (l. 3052).
  *Changed:* "Marx names no one here; histories of the school usually count
  Samuel Bailey and Robert Torrens among the critics who pressed that kind of
  point." The sentence before it says the issue was the equal annual return of
  capitals with different turnovers. It is the lesson's gloss on "the annual
  rate of profit" and I left it.
- **Softened paraphrase.** "A society that planned, Marx says, would reckon in
  advance". The text: "If we assumed that society were not capitalistic, but
  communistic … society must calculate beforehand" (l. 3254). *Changed* to "A
  communist society, Marx says".
- Checked and right:
  - capital A's £2,500, a fifth variable, 4 + 1 weeks (ll. 3014–3016);
  - the passage (l. 3034);
  - B (l. 3044);
  - the 900% (l. 3050);
  - B on A's footing, £50,000 (l. 3058);
  - S′ = s′n (l. 3153);
  - C at 10/11, "90 10-11%" (l. 3173);
  - every tile and quiz figure.

### 11. The Circulation of Surplus Value (Ch. 17)

- **Paraphrase wrong.** "On the other side gold arrives without having been a
  product first." The text: "surplus-value in the form of gold without the
  previous transformation of products into gold" (l. 3518). The point is about
  the gold producers' surplus value, which needs no sale to become money.
  *Changed* to "the gold producers' surplus value arrives already as gold,
  without first being a product that has to be sold".
- Checked and right:
  - Tooke's opponent (l. 3381);
  - "neither Tooke nor any one else" (l. 3393);
  - the 500/600 question (l. 3395);
  - the four evasions in order (ll. 3403–3416);
  - "the problem itself does not exist" (l. 3418);
  - the class throws in the money (l. 3430);
  - the farmer (ll. 3432–3434);
  - accumulation offers "no new problem" (l. 3526);
  - hoards and gold (ll. 3532–3540).

  Luxemburg (1913) and Bukharin's reply are accurate and stated at strength.
  Tiles: £600/£100, £6,000/£1,000, £550/£50.
- **Recommendation (not changed).** The `half-spent` preset (£50 spent, £50
  realised) is a lab case, not Marx's. For the whole class under simple
  reproduction, Marx says the sum spent "must be correct" equal to the surplus
  value (l. 3442). The note already calls the £50 illustrative. One clause in
  the body ("Marx's assumption makes the two equal for the class as a whole")
  would stop a reader taking the short-spending case for a possibility Marx
  entertains.

## Voice, overall (§F)

The course reads as a person who has read the chapters closely. The openings use
the passage's own figures, as §F asks for Volume II, and the history is told with
people in it (Quesnay, Ricardo, Bakewell, the London contractor, Tooke's
opponent). The performed or evaluative touches are the ones listed above
("quaint", "with evident pleasure", "with relish", "honestly"), each now removed.
Two remain, and I leave them as taste:

- "Marx's comment is dry" (lesson 5) points at Marx's own sardonic line, which
  §F allows.
- "the hollow skulls of the capitalists" is Marx's own joke, quoted.

## Where I disagree with the pedagogy assessment

*(Written after the findings above, on reading
`docs/pedagogy/capital-turnover-of-capital.md`.)*

The assessment is careful on arithmetic, speech and the Chapter 15 rule. I agree
with its repairs: the four evasions in Chapter 17, the §2 accumulation gloss, the
"Point 4" cross-reference, and the timber and `moral` sentences. It does not
anchor on the lab. As with Course 1, the disagreements are about what the
lessons say Marx (or his opponents) said, and several are in passages the
assessment praised.

1. **"Sort one capital by Smith's cut and by Marx's" (Verdict; lesson 4).** The
   assessment counts "`£600 fixed, £400 circulating` twice with `£200` and `£250`
   of surplus value" as a refutation on Smith's terms. It is not Smith's cut. On
   Smith's own words the seed is fixed (l. 1851) and the whole mine is fixed
   (l. 1814, a line the lesson itself quotes). The lesson contradicted itself
   between two paragraphs. Fixed here; see lesson 4 above.
2. **Bailey and Torrens (Remaining issues; "Critics at strength").** The
   assessment says the clause "is presented as history and not as something Marx
   says". As written, "Ricardo's followers could not explain … ; their critics,
   Samuel Bailey and Robert Torrens among them, pressed exactly that point"
   followed straight on from a quotation from the chapter. Nothing told the
   reader the names were not Marx's. The brief asks that such material be found
   in the chapter or sourced. The assessment's "the history Marx tells
   elsewhere" means *Theories of Surplus Value*, which §G puts outside the
   Subject's reading. The clause now says Marx names no one.
3. **The wine in the cellar (Remaining issues; "Critics at strength").** The
   assessment says the lesson "says 'the old puzzle' rather than attributing the
   example to the chapter", and that it is "the case Marx has in mind". The
   paragraph began "The chapter also names the people who got this wrong" and
   went straight into the cellar, so it did attribute the case to the chapter. It
   also said Marx "promises the answer in Volume III, where profit on the waiting
   capital is explained by the equalisation of profit rates". Volume III (Kerr)
   never returns to McCulloch or James Mill on this. It also gave the two men
   one position, which is not right: Mill reckoned the time as so much labour,
   McCulloch counted nature's operations as labour. The "case at its strongest"
   that the assessment praised is kept; its source is now given.
4. **The light remarks (Voice).** The assessment lists "a little quaint", "with
   evident pleasure" and "with relish" as §F rule 5 done well. Rule 5 asks the
   lesson to point at Marx's own jokes before making new ones. These three are
   not jokes of Marx's. They are the lesson's verdict on Marx's reasoning, or
   states of mind the text does not show. The "pleasure" and the "relish" in
   particular put an attitude in Marx's mouth. All three removed. "Marx's comment
   is dry" and the hollow skulls are fine and stay.
5. **"Engels' Suez bracket" (Fidelity list).** Kerr prints the sentence in plain
   parentheses with no "F. E.", and the dates allow it to be Marx's. The lesson
   no longer names Engels as its author.
6. **"Engels says it gave him the most trouble" (lesson 9, quoted approvingly
   under "Can a first-time reader…").** Engels says "no small amount of
   difficulties". Softened.
7. **"Every quiz figure recomputes" (`250 · 40 = 10,000`).** The figure does, but
   its `why` called £6,250 "a quarter of the right answer". It is five-eighths.
   Fixed.
8. **Lesson 2's concepts and body were not flagged.** Repairs "count as
   circulating capital" overstated a hesitant classification (l. 1612). "Later
   readers call it moral depreciation" denied Marx a term he uses himself in
   Volume I (vol. 1, l. 3078). Both fixed.
9. **Lesson 9, capital III (assessment's Remaining issues).** I agree that Marx
   divides the four-against-five case into capitals I, II and III (l. 2837),
   that the tile's I £400 + II £500 is consistent with §1's definition, and that
   one sentence in the `note` would warn the reader. I did not add it, since the
   assessment chose not to and it is a matter of taste. I second the
   recommendation.
