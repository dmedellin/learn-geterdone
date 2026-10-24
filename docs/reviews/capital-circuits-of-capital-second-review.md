# Second review — The Circuits of Capital (Capital, course 6)

An independent second read of `content/capital/c06_circuits/`
(`__init__.py`, `part_a.py`) on branch `feat/capital-subject`, after the
pedagogy pass. My findings were formed before I read
`docs/pedagogy/capital-circuits-of-capital.md`. The last section compares the
two.

## Method

- Every lesson was read in full against Volume II, Chapters 1–6 of
  `/mnt/project-files/capital-texts/volume-2-kerr.txt` (l. 340–1420). I also
  read Engels' account of the manuscripts in the preface (l. 191–203), the
  footnotes that mark which manuscript each part comes from (fn. 4–14), and
  the part of Chapter 19 behind the Adam Smith paragraph (l. 3812–3840).
- Every span in `&ldquo;…&rdquo;` was checked with
  `scratchpad/tools/strict_quotes.py c06_circuits 2`: 56 segments and 0 misses
  before my edits, 61 segments and 0 misses after them.
- Every figure in the prose, the worked lines, the quiz answers and the `why`s
  was recomputed by hand. Those figures include the three lots of Chapter 3 as
  fractions: 34596/125 = 276.768, 7254/125 = 58.032, 138384/25 = 5,535.36,
  29016/25 = 1,160.64, 6084/25 = 243.36, 1521/125 = 12.168.
- Every preset's tiles were read with `node scripts/labcheck.js --observe` on
  a fresh render, including the tiles nobody pins. The lesson 2 claim about
  the slider at 3 (the hoard reaching £234 and the capital becoming £656) is
  not observable at the shipped `periods = 1`. I checked it against `acRun` in
  `capkit.py` (l. 986–1006): 78, then 156, then 234 ≥ 200, so K = 422 + 234 =
  656. That is correct.
- Every quiz distractor was argued for.

## Verdict

The arithmetic is right everywhere except one quiz explanation. Every pinned
tile, every worked line and every quiz answer recomputes exactly. Every
quotation is in the Kerr text. The lesson 3 note on the Kerr table's misprints
is accurate:

- 1,160.740 for 1,160.640;
- 343.360 against 243.360 a few lines earlier;
- 7,450 for 7,440.

Two further slips, which no lesson uses, are not mentioned:

- 8.929 d. in Chapter 2 against 8.928 d. in Chapter 3;
- "100 per cent instead of 150" at l. 492, where it should be 156.

The defects are in what the lessons say Marx argues or replies, as in Course 1.
Three are substantive:

- the reply to Adam Smith;
- the reply to Say;
- a reply to Böhm-Bawerk, which Marx never made.

The rest are smaller verdicts the text does not contain.

## Findings and changes

### 1. The Circuit of Commodity Capital — the reply to Adam Smith was a computation Smith would accept (changed)

The body, `mistakes[0]` and the third quiz `why` answered Smith's resolution
of price into revenues with the spinner's own split: £372 of the £500 must buy
back means of production, so only £128 is income.

Smith grants that split for a single capital. Marx quotes him granting it for
corn and the farmer's horse (l. 3816). His claim is that the £372 is, in turn,
the cotton planter's and the machine-maker's wages, profit and rent. So the
split is not Marx's reply.

Marx's reply, in Chapter 19, has two parts:

- **The regress never ends.** Smith "refers us from one line of production to
  another". Each input's price contains its own constant part, so the chain
  never reaches pure revenue (l. 3820).
- **Two different totals.** Smith confuses the value of the annual product with
  the value newly produced in the year (l. 3838).

The quiz `why` also called £500 "Adam Smith's answer". Smith would not say the
spinner's whole £500 is the spinner's income.

**Changed:**

- **The body paragraph.** It now has Smith grant the split and name whose
  income the £372 is. It then gives Marx's two-part reply, with the Chapter 19
  phrase quoted, and presents this chapter's split as the first step of that
  reply, not the whole of it.
- **`mistakes[0]`.** Smith accepts the preset's split. Marx's reply is that the
  regress never ends in pure income, and only the new value, £128, is income.
- **The quiz `why`.** £500 now "counts that £372 as income as well, the step
  Marx says Adam Smith's resolution of price into revenues takes".

### 2. The Circuit of Productive Capital — the reply to Say and James Mill was not the text's (changed)

The lesson said Marx's "answer is the money stage they treat as a veil". It
then introduced the crisis passage of l. 763 with "The answer runs like this."

In the text, Marx's reply sits in the sentence just before the one quoted
(l. 753). Replacing one commodity by another in order to produce surplus value
"is a different matter than the exchange of products which is perfected merely
by means of money". The crisis passage is a separate paragraph several pages
on. Marx frames it as "important in a discussion of commercial crises", not as
a reply to anyone. The lesson had also said the crisis "shows first" in the
exchange of capital for capital. "First" is not in the text.

**Changed:** the paragraph now quotes the actual reply. The crisis paragraph
opens "A few pages on he shows how the circuit itself can hide a glut", and
"first" is gone.

### 3. The Circuit of Productive Capital — a verdict on the classical economists (changed)

"...which is `P…P`, and they were right about what it shows." This verdict is
the lesson's own and is in no line of the text. Marx's view of P…P as the
classical economists read it is harsher. In Chapter 3 (l. 956) he says it lets
"classic political economy ... pretend that production itself is the purpose",
"natural in the sense of a shallow rationalism".

**Changed:** I removed the verdict. The sentence now gives Marx's claim, made
in the next chapter, with that phrase quoted. `mistakes[0]`'s line about the
classical economists is supported by l. 956 and stays.

### 4. The Circuit of Productive Capital — "buying in order to use" (changed)

The first concept glossed P…P's circulation, `C–M–C`, as "buying in order to
use". Marx's point in the chapter is the opposite. In this circuit the
replacement of commodities serves the production of surplus value, and reading
it as exchange for use is the "vulgar economy" misreading he attacks (l. 699,
l. 713–715). `C–M–C` is, in Volume I's words, selling in order to buy.

**Changed to:** "the form of simple commodity circulation, selling in order to
buy."

### 5. The Time of Circulation — a reply Marx never made (changed)

"Marx's answer, on his definitions, is that waiting adds no labour..." follows
a paragraph on Böhm-Bawerk. Böhm-Bawerk published in 1884; Marx died in 1883.
The paragraph also described Böhm-Bawerk's theory as "waiting for their yield
is a real sacrifice". That is closer to Senior's abstinence, which Böhm-Bawerk
criticised. His own theory is the premium of present goods over future ones.

**Changed:**

- **Böhm-Bawerk's theory** is now roundaboutness, plus present goods worth more
  than future ones, with interest as the premium.
- **The reply** now says Böhm-Bawerk wrote after Marx's death, so the chapter
  answers the view, not the man. It quotes the chapter's own sentence (capital
  "produces neither commodities nor surplus-value" during circulation). It then
  points to the equalisation of profits, which is the text's first reason at
  l. 1237.

### 6. The Circuit of Money Capital — the monetary system's reading called "fair" (changed)

"It is a fair reading of `M…M′` alone that the gain is made in selling" put a
verdict on the reading in the lesson's voice. Marx does the opposite. He calls
the formula "in a certain sense, deceptive" because it invites that reading,
and calls the interpretation "illusive" (l. 626–628).

**Changed:** "...is the reading `M…M′` invites when it is taken alone, and that
is why Marx calls the formula 'in a certain sense, deceptive'."

### 7. The Circuit of Money Capital — the date of the monetary system (changed)

"The earliest mercantilist writers, of the seventeenth century". Marx's
"monetary system", bullionism, is the sixteenth- and early-seventeenth-century
stage that the developed mercantile system followed.

**Changed to:** "of the sixteenth and early seventeenth centuries".

### 8. The Circuit of Money Capital — "typical" glossed beyond the text (changed)

"Typical, for the same reason: it is how the capitalist sees his own business."
The text says the form is typical because its "aim and compelling motive ...
is thus most clearly revealed" (l. 615; compare l. 597, "the compelling
motive of capitalist production, the making of money, is most fittingly
expressed").

**Changed to:** "it shows most plainly the motive of the whole business, the
making of money."

### 9. The Circuit of Money Capital — quiz 2 `why` (changed)

The `why` read: "The last option is the view Marx is arguing against". That
option is that the £78 is the capitalist's wage. The chapter does not argue
against it.

**Changed to:** "a view Marx rejects elsewhere, and this chapter's accounts
give the capitalist no wage."

### 10. The Three Formulas of the Circuit — quiz 2 `why` miscounted (changed)

The `why` said the distractor 2/3 "counts the selling weeks against the other
eight". That gives 8/8 = 1, not 2/3. The distractor is 8/12, the eight selling
weeks over the old 12-week circuit.

**Changed** to say so. This is the only arithmetic error in the course.

### 11. The Circuit of Commodity Capital — two small overstatements (changed)

- **"Marx credits one economist with seeing this first."** The text credits
  Quesnay with "great discrimination" in choosing C′…C′ (l. 1013), not with
  priority. Changed to "with choosing this circuit".
- **"One consequence closes the chapter."** The point about the surplus product
  existing in material form is the penultimate paragraph; the Quesnay sentence
  closes the chapter. Changed to "comes at the chapter's end".

### 12. Course `how_to` — "the last drafts Marx wrote" (changed)

Part I draws on Manuscripts V–VII (1877–78) and on Manuscript IV, which is
earlier and more finished (fn. 4–14; preface l. 191–197). But a note in
Chapter 6 comes from Manuscript VIII, which is later. And "the last drafts Marx
wrote", unqualified, reads as his last writing on anything.

**Changed to:** "the last drafts Marx wrote of it". Engels calls Manuscript V
"the last complete presentation of this most important first section".

The comment headers beside lessons 1–3 now also give the line numbers of the
new quotations: l. 626, l. 956 and l. 3820.

### Recommendations (taste; not changed)

- **The Three Formulas of the Circuit.** Calling Bailey's *Critical
  Dissertation* "the sharpest attack on Ricardo's theory of value" is a
  judgement, though a common one. "The best-known attack of its day" would be
  safer.
- **The Costs of Circulation.** "This line is among the most argued-over in the
  book" is the lesson's own verdict. It is defensible and harmless, but it could
  be cut without loss.
- **The Three Formulas of the Circuit.** The rule "share of capital in a form =
  share of the circuit's time" is the lesson's model, not Marx's arithmetic.
  The note says the weeks are illustrative; it might also say the rule is the
  lab's, since Chapter 4 gives no such formula.
- **The Costs of Circulation.** The storage paragraph handles Marx's double
  verdict well: necessary storage enters value "in part" and is still a "dead
  expense" socially. The concept tile "its cost enters the value" could add
  "in part" to match.

### Checked and found right

- **Lesson 1.** The Russian landowners (1861, communal land, "free"
  wage-workers) and the transport formula `M–C…P–M′` match the text. So do the
  £110 example, "more rational and less difficult to understand", the class
  relation in `M–L`, and the split being fixed by the labour to be absorbed.
- **Lesson 2.** The text supports the 480/500 figures, the 211/240 share (tile
  `211/240 = 87.92%`), and latent and sterile money capital. It also supports
  the reserve fund coming out of the £78, and P′ rather than L′ and Pm′ because
  the composition changes.
- **Lesson 3.** The London builders, the weaver's "malignant intention" and
  the avances and reprises match the text, and the lots' arithmetic is exact.
  Quesnay's 1758 *Tableau* is dated correctly.
- **Lesson 4.** The text supports the Chinese artisan, "blocked by their
  predecessors", Bailey's sentence and Marx's reply about value compared with
  itself across non-contemporary phases, and "sells dearer".
- **Lesson 5.** Production time longer than labour time, the three reasons for
  the deception, the sale more important than the purchase, and the
  breweries and dairies all match the text.
- **Lesson 6.** The text supports the Greek-meets-Greek line, the combustion
  image, the salesman's 8 and 10 hours, book-keeping more necessary under
  co-operation, money as a dead expense, Smith on the supply, the railway
  magnates, and transport adding value and surplus value. Shaikh and Tonak's
  *Measuring the Wealth of Nations* (1994) is dated correctly.
- **The quizzes.** Apart from finding 10, every quiz has exactly one defensible
  answer. On the lab's accounting, the carter question's £110 distractor is
  excluded by the wording "on the lab's accounting", and the note admits that
  on Marx's full account carriage adds surplus value too.
- **Voice.** It is natural and unforced. The one light remark per lesson points
  at Marx's own sarcasm (the railway magnates, the "malignant intention", the
  "feverish attempt"). I found nothing preachy.

Final preview line after the edits:
`python3 scripts/preview_subject.py capital --course capital-circuits-of-capital --out …/rev2-c06`
printed `OK`: 6 pages executed and swept, 6 with pinned figures, 0 failing.

## Where I disagree with the pedagogy assessment

Read after the findings above were written. The assessment is careful about
the voice, the speech read-out and cross-references, and its repairs are
sound. As in Course 1, the disagreements fall in passages it praised.

- **The Adam Smith reply (my finding 1).** The assessment counts lesson 3's
  `mistakes[0]` among the misconceptions "refuted with the specific figure"
  ("Of 10,000 lb, 7,440 lb carry £372 that must buy back cotton, coal and
  wear"). It also calls the Smith paragraph a "serious position with its
  reasoning". The position was serious, but the refutation was a computation
  Smith accepts. Its own repair to that paragraph (adding the Chapter 19
  cross-reference) left the argument as it was.
- **The Say paragraph and the crisis (my finding 2).** The assessment praises
  them for showing "what rides on the money stage being more than a veil".
  That framing was the lesson's, not Marx's. His reply to the "some
  economists" is the sentence before the one quoted. The crisis passage is a
  separate observation about merchants' stocks.
- **The mercantilist paragraph (my findings 6 and 7).** The assessment
  repaired the monetary-system distinction well, but it kept "it is a fair
  reading of `M…M′` alone", a verdict in the lesson's voice. Marx calls the
  formula "in a certain sense, deceptive" and the reading "illusive". It also
  kept a dating ("the seventeenth century") that puts the monetary system
  after its time.
- **Böhm-Bawerk (my finding 5).** The assessment lists Böhm-Bawerk among the
  opponents who get their strongest case "before Marx answers". Marx could not
  answer him, since he died before Böhm-Bawerk published. The lesson's
  "Marx's answer" was a reply constructed for him. Böhm-Bawerk's theory was
  also described with a word, "sacrifice", that belongs to Senior.
- **"They were right about what it shows" (my finding 3)** and **"buying in
  order to use" (finding 4)** are not mentioned in the assessment. Both put a
  view in the lesson that the text contradicts. The first is a verdict Marx
  does not give, and his actual phrase is "shallow rationalism". The second
  glosses `C–M–C` with the very reading Chapter 2 calls vulgar economy.
- **"One-sided… Typical, for the same reason"** is quoted in the assessment as
  a model of going back through the passage. The gloss on "typical" ("how the
  capitalist sees his own business") was not in the text; my finding 8
  replaced it with the text's "compelling motive".
- **"Every figure in prose agreed" and "every wrong answer was argued for and
  none could be defended."** I agree about the answers. But one `why`
  explained a distractor with a miscount (lesson 4 quiz 2, "against the other
  eight", which is 8/8, not 2/3; my finding 10).
- **`how_to[1]`, "correct as written".** It is substantially correct.
  Footnote 14 shows that the opening of Chapter 6 is from a note at the end of
  Manuscript VIII, so Chapter 6 is not purely Manuscript IV, and "the last
  drafts Marx wrote" needed "of it". This is minor.
- **A count.** The assessment reports "all 23 pinned tile strings on the six
  pages". There are 43: 8, 6, 8, 9, 6 and 6 per lesson. All match, so the
  conclusion stands.

I agree with the assessment's remaining issues:

- Chapter 4's supply-and-demand passage is a computable seed for Course 8.
- The `£656` hoard figure cannot be pinned at a non-shipped period. I verified
  it against `acRun` instead.
- Lesson 4's `note` could quote Chapter 5's sentence as the warrant for the
  time-share model.
- Bailey's "sharpest attack" and the storage ambivalence are handled
  acceptably.
