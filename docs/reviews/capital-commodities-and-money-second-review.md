# Second review — Commodities and Money (Capital, course 1)

An independent second read of `content/capital/c01_commodities/`
(`__init__.py`, `part_a.py`, `part_b.py`) on branch `feat/capital-subject`,
after the pedagogy pass. My findings were formed before reading
`docs/pedagogy/capital-commodities-and-money.md`. The last section compares
the two.

## Method

- Every lesson was read in full against Volume I, Chapters 1–3 of
  `/mnt/project-files/capital-texts/volume-1-kerr.txt`. The footnotes behind
  the critics' paragraphs were read too: 25 (Bailey), 54–55 (Locke,
  Montesquieu), 88–89 (Vanderlint, Hume, Barbon, Ricardo), 116–117 (the double
  measure, the mercantilists) and the preface on Sedley Taylor.
- Every span in `&ldquo;…&rdquo;` was searched in the text. I used my own
  normalising checker and then the coordinator's strict checker
  (`scratchpad/tools/strict_quotes.py c01_commodities 1`).
- Every figure in prose, worked lines, quiz answers and `why`s was recomputed
  by hand.
- Every preset's tiles, including the unpinned ones, were read with
  `node scripts/labcheck.js --observe` on a fresh render.
- Every quiz distractor was argued for.

## Verdict

This is a careful course, and its arithmetic is right throughout. Every pinned
tile, every worked line and every quiz answer recomputes exactly. Every quoted
span is in the Kerr text. I found no wrong figure.

The defects were in fidelity, in places where a paraphrase said slightly more
or less than the text:

- the power-loom case;
- the "antagonistic movement";
- who the Sedley Taylor jibe belongs to;
- Marx's verdict on the mercantilists;
- how Marx's money-current sentence relates to a velocity;
- one refutation that misdescribed its own preset.

There was also one critic (Bailey) whose answer was missing. All of these are
fixed.

## Findings and changes

### Fidelity to Marx

1. **`the-two-factors-of-a-commodity`, body (lab paragraph): the power-loom
   case was misstated.** The lesson said "In Marx's own case the whole trade
   halves its time". Kerr l. 598 says the opposite for the hand-loom weavers:
   the power-loom "reduced by one half the labour required", while "the
   hand-loom weavers … continued to require the same time as before". That is
   exactly why their hour counts as half.
   **Changed** to: "the power-loom halves the labour socially required while
   the hand-loom weavers go on as before, so their hour falls to exactly half."

2. **`the-twofold-character-of-labour`, `mistakes[0]`: the "antagonistic
   movement" was attributed to a fall in value *per unit*.** At l. 651 the
   antagonism is that a larger mass of use-values can have a smaller total
   value, when productivity shortens the labour-time. A fall per unit is not
   antagonistic; it is the ordinary case.
   **Changed** to: "if the larger mass takes fewer hours its whole value
   falls: that is the 'antagonistic movement'…".

3. **`the-form-of-value`, body (Bailey): the critic's answer was missing, and
   "Marx's reply" was not the reply the text gives.** The lesson made the
   four-case computation Marx's reply to Bailey. But the computation (the
   ratio cannot tell which commodity changed) is exactly what Bailey accepts,
   so as a reply it begs the question. Marx's stated reply (l. 761, fn. 25) is
   a diagnosis: the equivalent form misled Bailey into seeing "merely a
   quantitative relation", because he confused the form of value with value.
   **Changed** the paragraph to:
   - give Marx's diagnosis, quoted;
   - present the computation as Marx's evidence;
   - add Bailey's answer at strength: asking which one changed can only mean
     against which third commodity.

   It now ends on where the disagreement actually lies.

4. **`the-fetishism-of-commodities`, body: the Sedley Taylor jibe.** The
   lesson correctly dated Taylor's attack to months after Marx's death. It
   then called the line "the closest the section comes to a smile", which
   leaves the reader to attribute to Marx a jibe at a man who attacked him
   after he died. The name is the 1887 English edition's. Engels edited that
   edition, and the German has a German economist, M. Wirth. That German
   reading is my knowledge of the German edition, not the Kerr text; it is
   not quoted on the page.
   **Changed:** one sentence added saying the name cannot be Marx's own and
   where it comes from.

5. **`world-money`, body (mercantilists): Marx's verdict was invented and
   pointed the wrong way.** The lesson said: "Marx's verdict is narrower: the
   mercantilists took the chief function of world money for the whole of what
   money is." That is not in Chapter 3. The footnote on the watchword
   (fn. 117) turns on the mercantilists' *opponents*, who "entirely
   misconceived the functions of money of the world". It names Ricardo, whose
   dogma was that an unfavourable balance "never arises but from a redundant
   currency".
   **Changed** to that, linked to the quantity-theory dispute two lessons
   back. Both phrases were checked verbatim.

6. **`hoards-and-means-of-payment`, `note`: Marx's sentence was misread.** The
   note said Marx "speaks of subtracting the circuits a coin makes rather than
   dividing by a velocity; the two agree when each coin does the same number
   of jobs". Marx's sentence (l. 1383) takes the velocity as *given* ("given
   the rapidity of currency"). Its last subtraction removes the circuits in
   which the same coin serves first as means of circulation and then of
   payment, so that it is not counted twice. It is not a velocity term. The
   body paragraph already had this right ("less again for coins that do
   several jobs in turn").
   **Changed** the note to say this, and that the lab has no term for that
   overlap, which is zero in its presets.

7. **`hoards-and-means-of-payment`, `mistakes[0]`: the refutation misdescribed
   its preset.** It said "In the broken preset no commodity changes hands at
   all". In that preset three £100 sales were made, on credit
   (`credit_sales: 300`, sum of prices tile `£300`).
   **Changed** to: "every sale was made on credit, so the sales themselves
   need no coin, and yet £100 of hard cash is needed."

### Quotations

All spans are in the text. The strict checker reported seven misses.

**Three are only convention**, and are left as they are:

- the opening "The wealth of those societies…" (drop capital `THE`, footnote
  numeral 10, nested quotes printed as single curly quotes);
- "It is plain that commodities…" (drop capital `IT`);
- 'from "meuble" into "immeuble"' (nested quotes as single curly quotes).

All three are allowed by the course docstring.

**Four changed the case of the text's first word**, which the docstring does
not allow. All are reworded so that the span matches the text exactly:

- `the-two-factors-of-a-commodity`: "Normal conditions of production" became
  "The 'normal conditions of production' are…", and "The average degree of
  skill and intensity" became "The 'average degree of skill and intensity'
  rules out…".
- `the-twofold-character-of-labour`, quiz 4 `why`: "for simplicity's sake"
  (Kerr: "For simplicity's sake…", sentence-initial) became "henceforth
  account every kind of labour to be unskilled, simple labour", from the same
  sentence.
- `exchange`, body: "a born leveller and a cynic" (Kerr: "A born leveller…")
  became "'A born leveller and a cynic', Marx calls the commodity".

After the changes the strict checker reports 132 segments and 3 misses: the
three convention cases above.

Lesson titles written in “…” (cross-references) are not quotations. My
normalising checker flags them and the strict checker does not.

### Arithmetic

Every figure was recomputed and all of them hold. Tiles observed:

| lesson | figures |
| --- | --- |
| 1 | `9/5 h`/`36 h`, `11/5 h`/`44 h`, `6/5 h`/`24 h`; C's 8 of 40 extra hours (`20 · 2/5`), 32 on the other 80 yards; C's hour `3/5` → `2/5` of a social hour; quiz `100/40 = 5/2` |
| 2 | `10 h`/`10 h`, `5 h`/`10 h`, `20 h`/`10 h` (vaSnlt equals vaPerUnit throughout) |
| 3 | `20 yards linen = 1 coat`, `= 2 coat`, `= 2 ounces gold`; quiz `20/40 = 1/2` |
| 4 | `40 h`, `120 h`, `160 h`, per unit `5, 1/2, 6, 3` in all three; quiz `6 / (1/2) = 12` |
| 5 | `6`/`3`, `15`/`5`, `15`/`5`; quizzes `10`, `6` |
| 6 | `£8`/`£2`, `£8`/`£8`, `£16`/`£4`, `£8`/`£1`; quiz `£15 / 5 = £3` |
| 7 | `£300`/`£0`, `£0`/`£0`, `£100`/`£100`, moUnbacked `£0` throughout; quiz `(500 − 200 + 150 − 50)/2 = 200`; the £50 circle `£0`, then `£50` when B defaults |
| 8 | `£0`, `£200 out`, `£300 out`; quizzes `−150` in and `£250` |

### Quiz

Every distractor was argued for. Two questions could be argued against as
written, and both are fixed:

- **`the-twofold-character-of-labour`, quiz 3.** It asked which change alters
  "the value created in a ten-hour day", and the keyed answer was "Working
  twelve hours instead of ten", which is no longer a ten-hour day. **Reworded:**
  "A tailor works a ten-hour day. Which change alters the value his day's work
  creates…".
- **`the-form-of-value`, quiz 1.** It asked whose value is expressed in
  "10 lb of tea = 40 lb of coffee". The distractor "Neither; it is only a
  ratio" is Bailey's position, which the lesson presents as serious. **Added**
  "on Marx's reading".

### Voice (§F)

The voice is natural and close to the target:

- the passage comes first and is read phrase by phrase;
- scenes appear only where the object is in the reader's life;
- critics are given at strength, with dates and people.

I found nothing performed or preachy. Two small evaluative touches lean
toward endorsement, and I left both as recommendations below.

## Recommendations (taste, or outside this course's files)

1. **`world-money`:** "Marx adds a sign worth remembering: bank reserves far
   above their usual level are… a sign of stagnation". "Worth remembering"
   endorses the claim. Suggest "Marx adds an observation".
2. **`hoards-and-means-of-payment`:** "one of the section's best passages"
   is the lesson's own verdict. It is harmless, but "a passage Marx clearly
   enjoyed writing" or plain description would present rather than rate it.
3. **`the-fetishism-of-commodities`:** the village preset assumes the
   households exchange at the ratio of their hours ("The hours per unit are
   identical, so the exchange ratios are too"). On Marx's account in §4,
   isolated producers' exchange ratios only gravitate to labour-time "in the
   midst of all the accidental and ever fluctuating exchange relations".
   Suggest one clause in the `note` that the village exchanges at its hours
   by assumption.
4. **Form lab, money stage (kit).** With the `marx` preset (equivalent
   linen), stepping `foStage` to `money` shows `foGeneral = linen (as money)`.
   That contradicts the lesson's own "Put gold where linen stood… That is the
   money form". The `panel_intro` steers readers to the gold preset for the
   money stage, which mitigates it. A kit change (refuse or relabel the money
   stage when the equivalent is not gold) is for the kit owner.
5. **Form lab prints `2 coat`** (agreeing with the pedagogy review). This is a
   kit matter.
6. **`the-form-of-value` split, and the three peculiarities of the equivalent
   form.** I agree with the pedagogy review on both, as recorded there.

## Where I disagree with the pedagogy assessment

- **The power-loom.** The assessment's repair wrote that in "Marx's own case
  … the whole trade halves its time". The text says the hand-loom weavers did
  not change their time, and that is the whole point of the example. Fixed
  (finding 1).
- **"No commodity changes hands at all, and yet £100 of hard cash is
  needed".** The assessment cites this as a model refutation of lesson 7's
  misconception. It misdescribes the preset, whose sales were made on credit.
  Fixed (finding 7).
- **Bailey "stated at strength".** The assessment lists Bailey among critics
  given full strength "followed by Marx's reply as a reply". The reply given
  was a computation Bailey accepts. Marx's actual reply in the text (a
  diagnosis of confusing form with value) and Bailey's rejoinder were both
  absent. Fixed (finding 3).
- **Mun and the mercantilists.** The assessment praises the paragraph but
  does not notice that its closing "Marx's verdict" is not in the text, and
  that fn. 117 aims the other way, at Ricardo. Fixed (finding 5).
- **The Sedley Taylor line** is praised as Marx's joke ("Marx's before the
  lesson's"). The jibe is the English edition's. Fixed (finding 4).
- **The `note` sentence on the formula.** The assessment's repair kept the
  claim that Marx's last subtraction is a velocity that "agrees when each coin
  does the same number of jobs". It is a correction for double counting.
  Fixed (finding 6).
- **Initial capitals.** The assessment accepted spans whose first-word case
  differed from the text as conforming to the §E.3 convention. The course
  docstring allows only drop capitals and nested quotes. I reworded the four
  such spans (see Quotations).
- I agree with everything else in the assessment, including its Hume repair
  (footnote 88 does name Hume after Vanderlint and Barbon, and fn. 89 names
  "Ricardo and his disciples"), its four-cases repair, and its arithmetic.

## Files changed

- `content/capital/c01_commodities/part_a.py`: lesson 1 body (phrase-by-phrase
  paragraph, power-loom sentence); lesson 2 `mistakes[0]`, quiz 3 `q`, quiz 4
  `why`; lesson 3 body (Bailey paragraph), quiz 1 `q`; lesson 4 body (Sedley
  Taylor).
- `content/capital/c01_commodities/part_b.py`: lesson 5 body (born leveller);
  lesson 7 `mistakes[0]`, `note`; lesson 8 body (mercantilists).

No preset, `expect`, slug, mode, view or figure changed. No other course, and
nothing in `scripts/`, `tests/` or the kit, was touched. Nothing was committed.

Final preview (`python3 scripts/preview_subject.py capital --course
capital-commodities-and-money`): 9 pages rendered; every lab executes (8
pages, 0 failing); pinned figures match (8 pages, 8 with pins, 0 failing);
**OK**.
