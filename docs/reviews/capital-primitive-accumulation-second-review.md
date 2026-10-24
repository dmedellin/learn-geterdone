# Second review: So-Called Primitive Accumulation (Capital, course 5)

This is an independent second read of `content/capital/c05_primitive/`
(`__init__.py`, `part_a.py` and `part_b.py`) on branch `feat/capital-subject`.
I wrote these findings before reading
`docs/pedagogy/capital-primitive-accumulation.md`. The last section compares the
two reviews.

## Method

- I read every lesson in full against Volume I, Chapters 26 to 33, of
  `/mnt/project-files/capital-texts/volume-1-kerr.txt` (lines 5245 to 5575).
  I read each chapter whole. For "Machinery and the Displaced Worker" I checked
  the carpet factory at l. 3323, and for "Simple Reproduction" I checked the
  £1,000 and £200 at l. 4254.
- I ran the strict checker:
  `strict_quotes.py c05_primitive 1`. It reports **99 segments and 0 misses**.
  One segment is reported as `l.?`. That is "disciplined, united, organised by
  the very mechanism…", and it is not located only because it crosses the page
  break at l. 5511–5513. This is a page-break split, so it is a convention, not
  a miss. Nothing needed fixing.
- I recomputed every figure in the prose, the worked lines, the quiz answers
  and the `why`s by hand.
- I rendered the course with `preview_subject.py` into my scratchpad. I read
  every preset's tiles with `labcheck.js --observe`, and every tile matches
  the prose.
- For each quiz question I tried to argue that each distractor was correct.
- I checked every historian against what I know of the literature. I had no
  sources in the sandbox, so every judgment about a historian below rests on my
  own knowledge. Where that knowledge was not firm enough, I left the text
  alone and say so.

## Verdict

The arithmetic is right throughout. None of the 42 pinned tile strings (24 presets) and none of
the quiz answers is wrong, and no quotation misses. The quotations are long,
and they are well chosen.

The defects are of two kinds:

- small infidelities to the text, where a paraphrase moved a cause or dropped a
  qualification;
- historians' positions stated a notch too strongly, or attributed to the wrong
  person.

There is no misrepresentation on the scale of the Course 1 findings. The
edits are findings 1 to 15, 17 and 21, twenty text replacements in all, every
one small. After them the preview prints **OK**.

## Findings and changes

### Fidelity to Marx

1. **`the-secret-of-primitive-accumulation`, body (Weber and Crouzet): an
   anachronism and a forward reference that did not hold.** The paragraph said
   "Marx's reply, which the next paragraphs compute, is that profits to plough
   back already presuppose people who work for wages."
   - Marx could not reply to Weber (1905) or Crouzet.
   - The next paragraphs compute the plain legend (saving out of a wage), not
     this reply.

   **Changed** to: "Marx wrote before either, but the chapter's opening circle
   is his answer to both: profits to plough back already presuppose people who
   work for wages." The circle at l. 5255 supports that.

2. **`expropriation-from-the-land`, body: the cause of the sheep-walks was
   misstated.** The lesson said "because Flemish wool had raised the price of
   English wool". Kerr l. 5285 has "The rapid rise of the Flemish wool
   manufactures, and the corresponding rise in the price of wool in England".
   It was Flemish *manufacture* that raised the price of English wool, not
   Flemish wool.
   **Changed** accordingly.

3. **`expropriation-from-the-land`, body: who disbanded the retainers.** The
   lesson said "the great lords disbanded their retainers". At l. 5285 the
   bands of retainers were broken up, and the royal power "forcibly hastened"
   that, though it was "by no means the sole cause". The great lords did
   something else: they drove the peasants off the land.
   **Changed** to "the bands of feudal retainers were broken up, and the great
   lords drove peasants from the land…".

4. **`bloody-legislation`, worked `after`: the explanation of the doubled rate
   was incomplete.** The text said the rate doubles "because the shilling taken
   from the wage is added to a surplus value that was only 3s". That explains
   only 3 → 4, which gives 4/3, not 2. The rate doubles because the numerator
   rises (3s → 4s) and the denominator falls (3s → 2s) at once.
   **Changed** to say both.

5. **`the-home-market`, body: Marx's chief cause was turned into a minor one.**
   The lesson said that manufacture destroying rural industry in one branch and
   calling it up in another "is why" the peasantry keeps vanishing and turning
   up again. Kerr l. 5424 calls this "one, though not the chief, cause". The
   chief reason is that England alternated between corn and cattle.
   **Changed** to give both causes in Marx's order of weight.

6. **`the-home-market`, concepts: a claim the text does not make.** The lesson
   said "The land fed as many or more after the clearing". Marx's claim
   (l. 5418) is about output: "the soil brought forth as much or more produce".
   Whom that output fed is the chapter's whole point, so it cannot be stated as
   if settled.
   **Changed** to "The land yielded as much or more after the clearing."

7. **`the-industrial-capitalist`, body: Augier's half of the closing image was
   given to Marx.** The blood-stain on money's cheek is Augier's, and Marx says
   so ("according to Augier", l. 5499). The lesson also introduced the line as
   "an image you will not forget", which is performed.
   **Changed** to "Marx closes the chapter by finishing a sentence of Augier's:
   …".

8. **`the-modern-theory-of-colonisation`, summary and `mistakes[0]`: Wakefield's
   "discovery" was stated without Marx's qualification.** At l. 5533 Marx says
   at once that the economist "christens them capital under all
   circumstances… Thus is it with Wakefield". Wakefield calls the settlers' own
   means of production "equal division of capital".
   **Changed:**
   - the summary now says "on Marx's reading";
   - `mistakes[0]` now adds that Wakefield himself went on calling the
     settlers' tools capital.

9. **`the-industrial-capitalist`, `mistakes[2]`: a confusing title.** The
   title was "Reading the colonial chapter as only about consols". This course
   has a chapter on colonies, and it is Chapter 33, not 31.
   **Changed** to "Reading the chapter as only about consols".

### Historians: dates, positions and strength

10. **`bloody-legislation`: the Statute of Labourers' date.** Marx's "1349" is
    the Ordinance of Labourers. Parliament enacted the Statute of Labourers in
    1351. The lesson repeated "of 1349" in its own voice.
    **Changed** that sentence to: "Marx dates it 1349, the year of the royal
    Ordinance of Labourers; Parliament enacted it as a statute in 1351." The
    quotations and the quiz stem ("on Marx's account") keep his date.

11. **`bloody-legislation`: the combination laws.** In the lesson's own voice
    the laws "went… in 1825". The repeal was in 1824, and the 1825 Act partly
    restored the restrictions. Marx's text has "fell in 1825… only in part".
    **Changed** to "the laws against combinations, Marx says, fell in 1825, and
    only in part".

12. **`the-capitalist-farmer`: Bodin's priority.** The lesson called Bodin
    (1568) "the first statement of the quantity theory". That is too strong.
    Azpilcueta (Salamanca, 1556) and, earlier, Copernicus stated it before him.
    **Changed** to "the most famous early statement".

13. **`the-capitalist-farmer`, quiz 4 `why` and `mistakes[2]`: population
    pressure was attributed to Goldstone.** The distractor is "the population
    grew faster than food". That is the Malthusian account of Outhwaite and of
    Phelps Brown and Hopkins. Goldstone's 1984 argument, which the body states
    correctly, is that population growth and urbanisation raised the
    *velocity* of money.
    **Changed:**
    - the `why` now names Outhwaite;
    - `mistakes[2]` now names "Outhwaite and Goldstone" and "a growing
      population".

14. **`expropriation-from-the-land`, `mistakes[0]`: tense.** The lesson said
    Chambers and Allen "still argue". Chambers died in 1970.
    **Changed** to "on which historians such as Chambers and Allen have
    disagreed".

15. **`the-home-market`, body: Smith's position.** The lesson said Smith "tied
    the market to the division of labour, each extending the other". The
    mutual-extension formulation is Allyn Young's (1928). Smith's own claim
    (Wealth of Nations I.3) is that the division of labour is limited by the
    extent of the market.
    **Changed** to say that.

16. **The other positions and dates, checked and left as written.** All of
    these rest on my own knowledge. For each, the date and the position stated
    match that knowledge.

    | Historian or writer | Date | Position as the lesson states it |
    | --- | --- | --- |
    | Weber | 1905 | The essays appeared in 1904–05. 1905 is the usual citation and is acceptable. |
    | Crouzet | — | Founders came from the middling ranks; firms grew by ploughing back profits. |
    | Chambers | 1953 | Enclosure raised the demand for labour; population growth supplied the workforce. |
    | Allen | 1992 | Small effect on output; the main effect was redistribution to landlords. |
    | Davies | 1966 | The 1547 Act was repealed by 1550 and barely enforced. |
    | Beier | — | The masterless men were young and mobile, and were looking for work. |
    | Thorold Rogers | — | High real wages in the century after the Black Death. |
    | Hamilton | 1934 | American treasure and Spanish prices. |
    | Outhwaite | — | Population. |
    | Kerridge | — | Rents 1540–1640 outran prices through fines and new leases. |
    | de Vries | — | The industrious revolution, seventeenth and eighteenth centuries. |
    | Williams | 1944 | Profits of slavery helped finance industrialisation. |
    | Inikori | 2002 | Demand from the Atlantic trade. |
    | North and Weingast | 1989 | Credible commitment after 1688. |
    | Dickson | 1967 | The term "financial revolution". |
    | Dühring and Engels | 1878 | *Anti-Dühring*: the process is shown first, the dialectical label after. |
    | Bernstein | 1899 | Property-owners multiplying; small firms persisting. |
    | Popper | — | Historical laws classed as prophecy. |
    | Baran and Sweezy | 1966 | The giant corporation as the typical unit of capital. |
    | Domar | 1970 | Of free land, free peasants and non-working landowners, any two exclude the third. |
    | Mill | — | Systematic colonisation as an exception to laissez-faire. |
    | Wakefield | — | 1829–33 writings; South Australia 1836. |
    | Consols | 1751 | Year of issue. |
    | Peel's party | 1829 | Year it sailed. |

17. **`the-industrial-capitalist`: Engerman and O'Brien were written up as if
    they wrote together.** They made the argument separately: Engerman in 1972,
    O'Brien in 1982.
    **Changed** to "in separate studies of 1972 and 1982". These dates are from
    my own knowledge.

18. **`expropriation-from-the-land`: Richards. Not changed; this rests on my
    own knowledge.** Richards does read the Sutherland plan as a resettlement
    scheme that failed. He questions some details of the contemporary accounts
    (Sellar was acquitted in 1816 over the Strathnaver death). He puts the
    removals at roughly 6,000–10,000 between 1807 and 1821, against Marx's
    15,000.
    - Marx's "794,000 acres" comes from Sismondi, and the estate was larger.
    - "Treats several figures… as exaggerated" is fair as a summary.
    - **Recommend** that a reviewer with the books open confirm the wording
      before release.

19. **`the-capitalist-farmer`: an omission.** The body gives the
    quantity-theory and demographic explanations of the Tudor price rise. It
    leaves out Henry VIII's Great Debasement of 1544–51, which Outhwaite and
    most English historians treat as a major proximate cause. **Recommend** one
    clause. I did not add it because it is an addition, not a correction.

20. **`the-modern-theory-of-colonisation`: Peel's numbers. Not changed; this
    rests on my own knowledge.** Historically Peel landed some 300–400 people.
    The 1887 printing's "300" is therefore closer to the record than the Kerr
    "3000". The `note` already flags the discrepancy, and the Kerr text is the
    Subject's source. **Recommend** adding "and the historical figure was
    nearer 300" to the note if the author can confirm it.

### The lesson's own verdicts (Marx presented, not endorsed)

21. **`the-historical-tendency`: three superlatives in the lesson's own voice.**

    | Field | Before | After |
    | --- | --- | --- |
    | `read_intro` | "The most famous passage in Volume I" | "One of the best-known passages in Volume I" |
    | body | "This chapter has drawn more argument than any other in the volume" | "Few chapters of the volume have drawn more argument." |
    | `note` | "the most argued question in the book" | "one of the most argued questions in the book" |

    None of the three is a verdict on Marx. Each is an unverifiable ranking,
    and each is softened as shown.

### Arithmetic (all verified, nothing changed)

Every worked line, quiz answer, `why` and pinned tile below recomputes exactly.

| Lesson | Figures checked |
| --- | --- |
| 1 | 3s × 1/10 = 3.6d; 60,000 / (3/10) = 200,000 days (666 2/3 years at 300 days); 12,000s gives 40,000 days (133 years); the whole wage gives 20,000 days (66 2/3 years); £1,000 / £200 = 5 years. Quiz: 20,000; 5. Each distractor's derivation in the `why` checks. |
| 2 | 12 − 6 = 6 h, rate 100%; 3,000 × 6 = 18,000 h. Quiz: 6 h; 3/2 = 150%; 200 × 5 = 1,000. |
| 3 | 12 × 3/6 = 6s of value. Wage 2s gives 200%, 3s gives 100%, 4s gives 50%. Quiz: 6/4 = 150%; gap 1s. |
| 4 | Stable 40. Price revolution: 200 − 80 − 20 = 100 (50 real). Wages lag: 200 − 60 − 20 = 120 (60 real; 10 from the landlord and 10 from the labourers). Quiz: £10; £70, with £60, £30 and £80 each correctly derived. |
| 5 | 1 + 3/12 + 3/12 = 1s 6d; markets 0s, 150s and 50s. Quiz: 300s; 1s 3d. |
| 6 | £100, £150 and £100. Quiz: £125; £250, with the distractor £62 10s correct as half of £125. |
| 7 | 100 × 1.1⁵ = 161.051, total £1,610.51, share 1/10. Merging gives 200…600, 5 left, 3/5. Quiz: 1/2, with 5 left; 1/10. |
| 8 | 2 / (1/2) = 4 years; 3,000 for hire through period 4. Quiz: 3 / (1/4) = 12; 0. |

### Labs

22. **`the-industrial-capitalist`, preset `bank-1694`: the preset is close to
    decorative.** It prices £8 a year at 8% as £100, which is the definition of
    an 8% loan on £100. It records Marx's rate but moves nothing. **Recommend**
    one of these:
    - price the Bank's £8 at a later, lower rate (say 4%: £200), which shows
      the 1694 lenders' gain as rates fell;
    - or say plainly in the prose that the preset only records the rate.

    Left as written.

### Quiz

23. **The quiz holds.** Every question has exactly one defensible answer. The
    nearest call is `the-industrial-capitalist` Q4, distractor B: "His capital,
    which the state spends and never repays". Consols were perpetual and never
    repaid, so B is half-true as history. The stem says "On Marx's account", and
    Marx's line is "actually give nothing away", so C is the only answer on the
    stem's terms. **Recommend** no change, or "and loses" in place of "never
    repays" to close the gap entirely.

### Voice

24. The voice is warm and plain and reads line by line, as §F asks. Every
    scene sits where the object is in the reader's life (the fixed rent and the
    fixed-rate loan in Chapter 29). The jokes are mostly Marx's own.

    Two mild cases of performance:
    - "an image you will not forget" (fixed under finding 7);
    - "That is Marx's joke, and the lesson needs no other." in
      `the-modern-theory-of-colonisation`, which comments on its own restraint.
      **Recommend** cutting the second clause. Left as taste.

## Final preview line

```
python3 scripts/preview_subject.py capital --course capital-primitive-accumulation --out <scratch>
  8 page(s) executed and swept, 8 with pinned figures, 0 failing
OK
```

Strict quotation checker: `segments 99, misses 0`.

## Where I disagree with the pedagogy assessment

(Written after the findings above.)

1. **Smith.** The assessment rewrote the Smith sentence to "tied the market to
   the division of labour, each extending the other", and calls that a
   correction of a reversal. The mutual-extension formulation is Allyn Young's
   (1928), not Smith's. Smith's claim is the one-way limit: the division of
   labour is limited by the extent of the market. I changed it again, to
   Smith's own direction (finding 15).
2. **Bodin.** The assessment quotes "the first statement of the quantity
   theory" approvingly, as history told with people in it. The priority claim
   is wrong (Azpilcueta in 1556, and Copernicus before him), so I softened it
   (finding 12).
3. **Goldstone.** The assessment separated Goldstone from the
   population-pressure account in the body. It left two places unchanged:
   - quiz 4's `why`, which still named him as giving "population pressure";
   - `mistakes[2]`.

   I made those two agree with the body (finding 13).
4. **"Every claim about a historian was checked against what that historian
   wrote."** No historian's work is available in this environment. I have
   marked my own judgments about historians as resting on my own knowledge.
   The assessment's claim is stronger than any check that could be run here.
   The Richards wording in particular should be confirmed with the books open
   (finding 18).
5. **Fidelity defects the assessment did not catch, all in passages it read as
   correct:**

   | Defect | Finding |
   | --- | --- |
   | Flemish wool against Flemish wool *manufactures* | 2 |
   | Who broke up the retainers | 3 |
   | The incomplete explanation of the doubled rate | 4 |
   | Marx's "not the chief cause" turned into "is why" | 5 |
   | "Fed as many" against "as much or more produce" | 6 |
   | Augier's half of the closing image | 7 |
   | Wakefield's discovery without Marx's qualification | 8 |
   | The Ordinance of 1349 against the Statute of 1351 | 10 |
   | The 1824/1825 combination laws | 11 |

   The assessment also kept "Marx's reply, which the next paragraphs compute"
   in the Weber paragraph it had rewritten. That sentence is anachronistic,
   and its forward reference does not hold (finding 1).
6. **The `bank-1694` preset.** The assessment counts it as honest use of
   Marx's 8%. I agree the figure is Marx's. But a preset that prices £8 at 8%
   as £100 only restates the definition of the loan. It is the nearest thing
   to a decorative tile on the course (finding 22). The assessment instead
   names `thrift` and `statute` as the labs closest to decoration. I think both
   of those earn their place, as it says.
7. **"Every quiz distractor… none could be argued for."** One distractor can
   be half-argued: Lesson 6, Q4(B), since consols were never repaid. The stem's
   "On Marx's account" saves the question, so I did not change it (finding 23).
8. **Voice.** The assessment lists "That is Marx's joke, and the lesson needs
   no other" among the good light remarks. I read it as the lesson commenting
   on its own restraint, which is mildly performed. "An image you will not
   forget" was not mentioned, and I changed it. The assessment also passed the
   three superlatives in the Chapter 32 lesson ("the most famous passage", "more
   argument than any other", "the most argued question"). They are the
   lesson's own unverifiable rankings, so I softened them (finding 21).
9. **Counts.** The assessment says "All 20 pinned tile strings". The eight labs
   pin 42 strings across 24 presets: lesson 1 pins one tile per preset, lesson
   6 one, and the other six lessons two each. Every one matches.

I agree with the rest of the assessment:

- its repairs (serfdom's date, branding, Celebes, the `closed` preset, Beier,
  Davies, Baran and Sweezy, the `mistakes[0]` of lesson 1);
- its judgment that the `separate` and `fixed-rent` labs are the course's best;
- its judgment that Marx is presented and not endorsed.
