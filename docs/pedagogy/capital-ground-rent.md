# Pedagogy assessment — Ground Rent (Capital, course 13)

Formed from the eleven lesson dicts in `content/capital/c13_rent/` (`part_a.py`,
lessons 1–6, Chapters 37–42; `part_b.py`, lessons 7–11, Chapters 43–47;
`__init__.py`, the course dict) and the kit they render through
(`scripts/mathpath/labs/capkit_b.py`, mode `rent`, views `price`, `waterfall`,
`dr1`, `dr2`, `absolute`; and `capkit.py` mode `workday`, view `corvee` for the
last lesson), on branch `feat/capital-subject` before the Subject was wired.
The design authority is `docs/capital/PLAN.md` §0, §B, the Course 13 entries in
§C, §D as summarised in `docs/capital/kit-b-report.md`, §E (how a passage is
quoted), §F (the voice) and §G; the author's brief is `docs/capital/AUTHORING.md`
with its two review-lesson sections. Course 1 is the voice reference.

Every lesson was read in full before anything was changed. Every pinned tile
was read off the rendered page (`scripts/preview_subject.py capital --course
capital-ground-rent`, then `node scripts/labcheck.js --observe`), every figure
in prose was recomputed by hand, and every quotation and quoted phrase (150 of
them, 151 after the repairs) was searched for character by character in
`/mnt/project-files/capital-texts/volume-3-kerr.txt` with the strict checker.
Because this Part's arithmetic lives in tables the plain text does not carry,
every "Marx's figures" preset was also checked against the printed table as an
image (`tables/volume-3/`, Kerr pp. 764, 768, 774–775, 800, 802, 803, 811, 814,
817, 820, 849, 858), and every slip the lessons attribute to the text was
checked against both the sentence and the image. Lessons, in course order:
`introductory-remarks-on-rent`, `differential-rent-general`,
`differential-rent-i`, `differential-rent-ii`, `dr-ii-constant-price`,
`dr-ii-falling-price` | `dr-ii-rising-price`, `rent-on-the-worst-soil`,
`absolute-ground-rent`, `building-rent-mining-rent-land-price`,
`genesis-of-capitalist-ground-rent`. The bar marks the seam between the two
modules. The course assumes Volume I, Volume II and Volume III Parts I–II, and
is judged against that.

## Verdict

The course teaches its subject, and it does the hardest thing a read-along of
Part VI has to do: it keeps six chapters of tables apart. A reader who finishes
it can price land from a rent and a rate of interest and strip the interest on
drains out of a lease payment; compute a natural advantage's surplus profit by
both of Marx's measures; rebuild Table I from four yields and a profit rate and
say what happens when the worst soil is replaced or all four improve; lay the
same four capitals on one acre and get the same 360s; add a second dose to every
soil at a constant price and say which of rent per acre and rate of rent moved;
let the market quantity throw A out and compute the rent at the new price in
money and in grain; price a dearer dose and revalue every rent at it, the old
regulating soil's included; find the rent the worst soil pays when a dose on B
regulates, by Marx's rule and by Engels'; compute the gap between agriculture's
value and its price of production and the absolute rent it allows; price a
building plot before and after the town arrives; and compute the rate of labour
rent from days on the lord's land and days on one's own. Those are the acts the
`standard` fields name and the quizzes measure; no objective is "understand X".
All 89 pinned tile strings, on 35 presets across the eleven pages, matched the lab, and every
figure quoted in prose agreed with the lab, with a recomputation, or with the
printed table.

Fidelity is high. All 150 quoted spans are in the Kerr text, and the ones the
checker found first in another chapter ("By no means", "identical", "would
disappear", "one pound sterling", "determined in the same way as the
agricultural rent") are also at the lines the lessons cite (6548, 6759, 6591,
6432, 6661). The presets are the tables: Table I (p. 764), four of Table II's
seven soils and all of Table III (p. 768), Chapter 41's Tables II and III
(pp. 802–803), Chapter 42's Table IV and IV d (pp. 811, 814) and the 44-quarter
table (p. 817), the p. 849 table behind the worse-investment case, and both
p. 858 tables. The slips the lessons attribute to the text are all real and are
all stated in the right register ("the Kerr text prints…"); none is invented
and none is Marx's figure misread. Ricardo is given his biography, his 1815
company, his Corn Law politics and his best argument before Marx replies, four
times over; Bortkiewicz and Clark are stated in their own terms and nothing in
the course has Marx answer either.

The defects were local: three quiz explanations that did not derive the figure
they explained, two runs the read-out spelled letter by letter, a Latin tag
credited to Marx that is Horace's, a slip called a misprint when the text
cannot say whose it is, a paraphrase of Marx that attributed a reaction to
unnamed historians, and a gloss of Petty and Cantillon looser than the
sentence it glosses. Nothing needs splitting, merging or reordering within the
URL space the course has. The one structural gap is in the kit, not the
lessons, and is recorded under remaining issues.

## Do the eleven lessons earn their places?

Yes, and the question matters most for Chapters 39–44, six lessons on
differential rent, four of them on differential rent II. The test is whether
each lesson has a quantity of its own, a misconception of its own and a tile
that refutes it, and whether a reader coming from the lesson before can say
what is new. Lesson by lesson:

- **`differential-rent-general`** (Ch. 38): one example, two measures of one
  surplus, and the claim the whole Part leans on ("not the source … only its
  natural basis"). The `steam-cheapens` preset is the refutation of
  `mistakes[0]`. Distinct from Ch. 39 because there is no soil in it yet.
- **`differential-rent-i`** (Ch. 39): the regulating price, Table I, and the
  thesis that rent needs unequal soils, not worsening ones, carried by three
  tables. This is the anchor lesson and the heaviest: eleven body paragraphs,
  four presets, Ricardo's biography, Table II's three extra soils in prose,
  two text slips and the false social value. It is one hard idea (the rule and
  what the rule does not require) told through the chapter's own three cases,
  and the five lessons after it reuse its soils and its price rule. The course
  `how_to` now says to read it slowly.
- **`differential-rent-ii`** (Ch. 40): one test, Table I's four capitals on
  one acre of D, and one difference, the lease. The `same-acre` preset's 360s
  against `side-by-side`'s 360s is the whole point in one comparison. The
  chapter's slip ("10-2 = 8 quarters … 12 pounds") is explained, not hidden.
- **`dr-ii-constant-price`** (Ch. 41): the quantity is rent per acre against
  rate of rent, and the `slower` preset shows one rising while the other
  falls (B: 60s to 90s; 120% to 90%). Nothing in Ch. 40 computed a rate of
  rent; nothing in Ch. 42 needs it.
- **`dr-ii-falling-price`** (Ch. 42): the quantity is the market limit, which
  the `dr1` view never had, and the second quantity is grain rent against
  money rent. Three presets give the same 30s price with total rent at 180s,
  360s and 720s, which is the chapter's argument ("a falling price decides
  nothing on its own") as three tiles.
- **`dr-ii-rising-price`** (Ch. 43): the quantity is `former_price`, and the
  idea is that the dearer source regulates. What the lesson adds beyond
  "price up, rents up" is the lease argument in the passage, which is Marx's
  qualification of Ricardo and belongs to no other lesson, and Engels'
  authorship of the first half, which a reader of the book needs to know.
- **`rent-on-the-worst-soil`** (Ch. 44): the regulator is a dose on a *better*
  soil, with nothing worse in use, and the lesson says in its `concepts_intro`
  exactly what is new ("Until now A paid no rent unless something worse came
  in below it"). Engels' correction is a second rule for the same instance, and
  the lesson states both and says which the lab computes.

Where 43 and 44 could blur is that both end with soil A paying rent. The
lessons mark the seam on both sides: 43 closes "finds a way for A to pay rent
with nothing worse in use at all", and 44 opens with the sentence above. The
one idea that recurs across four lessons is the acre's individual average
price (Ch. 40's `note`, Ch. 42's Table V paragraph, Ch. 43's third concept and
passage paragraph, Ch. 44's Engels paragraph). Each lesson leans on it, each
says the lab does not compute it, and 44 cites it back to 43 ("which the last
lesson met"), so it reads as one rule met from four sides rather than as four
rules. It is also the course's one real kit gap; see remaining issues.

Chapters 45, 46 and 47 each carry a different mode or view (`absolute`,
`price` again with the Part's additions, `workday/corvee`) and a different
quantity (a value–price gap, a site's price before and after, a rate of
surplus labour), and none could be folded into another.

## The slips attributed to the text, verified

The lessons name six places where a figure in the Kerr text does not follow
from the yields it gives. Each was checked against the sentence and the
printed table:

1. **Ch. 39, l. 5651:** "the total rental would increase from 18 pounds
   sterling to 22, a growth of 22 1/9%", and "be doubled upon C". Table III
   (p. 768) prints 450s, which is £22 10s and 25% on £18; C's rent goes from
   120s to 150s. Both slips are real; the lesson's figures are the table's.
   (The same sentence says "more than doubled upon D": 180s to 240s is not,
   either. The lesson does not mention it; recorded below.)
2. **Ch. 40, l. 5833:** "10-2 = 8 quarters, at 1½ pounds sterling per quarter,
   or 12 pounds sterling" for D's four doses yielding 4 + 1 + 3 + 2 with B
   regulating at £1½. Dose by dose, 10 quarters at 30s are 300s against four
   doses' 240s: £3. Real; the lesson says what the text did (set four doses
   against one).
3. **Ch. 40, l. 5884 and 5888, against p. 800 and p. 803:** "D, 6 quarters",
   then "two quarters instead of three" and "from 9 pounds sterling to 15",
   which need 7; the p. 800 table gives D's second dose a rent of £6 (so 3
   quarters); Chapter 41's Table III prints 4 + 3½ = 7½ and £16½. All three
   figures are as the lesson states them, and the lab follows Table III, as
   the §C entry says.
4. **Ch. 42, l. 5956:** "D and its price of production of 30 shillings would
   become regulating." Table IV (p. 811) has B at £1½ regulating and D at
   15s. Real. The lesson called it "a misprint"; the text cannot say whether
   it is the printer's, the translator's or the manuscript's, so it now says
   "a slip", which is the register the other five use.
5. **Ch. 42, p. 817 table:** prints C's grain rent as 3 quarters and the grain
   total as 25, against money rents of £3 and £33, where £3 at 30s is 2
   quarters and the total 24. Real, and visible only in the image.
6. **Ch. 44, l. 6422 and 6424 (Engels' bracket):** "average per quarter 3½
   pounds sterling" and "4½ quarters at 3½ pounds sterling make 14 pounds
   sterling". 14 over 4½ is 3 1/9, and only 3 1/9 leaves A the 1/9 pound
   Engels states; 4½ × 3½ is 15¾. Real; the lesson's parenthesis is exactly
   right and the p. 858 table confirms the 4½ quarters and £9½.

## The figures, recomputed

Every figure on the eleven pages was recomputed: £200/(1/20) = £4,000 and
/(1/25) = £5,000, true rent 150; 115, 25 − 15 = 10, 90 · 23/20 = 103½,
115 − 103½ = 11½, 80 → 20 and 23, 90 · 23/20 = 207/2; Table I 60s, 0/60/120/180,
360; the descending step 30s, 0/30/60, 90; Table II's A at 4/3 → 45s,
0/30/75/120, 225, with 15s, 45s, 60s on A′, B′, B″ and 345s in all; Table III
30s, 0/60/150/240, 450; 240s cost against 600s sold; D's 4, 3, 2, 1 → 360s;
second dose of 3 on D → 300s and 480s; Chapter 41's 720s (180% on 400s against
180% on 200s), 600s (B 90s, 90% against 120%), 900s; Chapter 42's market of 18
→ B regulates, 0/0/60/120, 180s (£9); five doses on D, market 30 → 360s and 12
quarters; 44 quarters on 550s, market 54 → 660s and 720s; IV c's 550s against
IV d's 450s of capital; Table V's 6/3½ = 1 5/7 and 9 3/7; Chapter 43's ¾-quarter
doses → 80s, A 20s, B 160s against 0s and 90s; A−2 at 120s → A 60s, B 300s,
A−1 60s, 420s (Marx's £3 and £15); D's ¾ → 80s, 20/100/180/260, 560s; the
p. 849 losses of £1½ and £3 against £4½ of rent; Chapter 44's 6/7 quarter →
70s, 10/125/265/405, 805s = £40¼; A's 4/5 → 75s, 15s, 142s 6d, 292s 6d,
442s 6d; 14/4½ = 3 1/9 (≈ 62s), 1/9; 115 and 125, 40/200 = 20%, 120, 5; 122 →
2; 85c + 15v → 115, 0; 80c + 20v and 60c + 40v → 140, 30%, 130, 10; £50 →
£1,000, £150 → £3,000, £3,750 at 4%; £400 → £8,000 (and £300 → £6,000 in
prose); £0; 60s → two quarters at 40s = 80s, a third more; 2/4 = 50%, 3/3,
4/2, 2/6 = 1/3; 1/5 = 20%. Every quiz answer and every distractor was derived
or, where it could not be, repaired (below).

## The voice, judged against §F and Course 1

- **The passage first, then the phrases.** Every body opens with the
  `<strong>Volume III, Chapter n.</strong>` block, and the lessons that have a
  dense passage go back through it in order: "Read that phrase by phrase. The
  price is the price 'of the ground-rent' … It is calculated 'on the ordinary
  rate of interest' … And the order of explanation runs one way"
  (`introductory-remarks-on-rent`); "take it phrase by phrase. First, it is 'not
  the source' … It is 'only its natural basis'" (`differential-rent-general`).
  The table chapters quote the passage and then build the table it summarises,
  which is the right move for a passage that is itself a summary of a table.
- **Scenes only where the object is in the reader's life.** "If you rent a
  flat, or know someone who farms rented land" (lesson 1); "Think of the
  difference between farming more land and farming the same land harder"
  (lesson 4); "If you have watched a field at the edge of a town become a
  street of houses, you have watched this chapter" (lesson 10), the best
  opening on the course. The table lessons open with the tables, as §F rule 2
  asks when a scene would have to be invented.
- **History as story with people in it.** Ricardo the stockbroker, the four
  authors of 1815, the Corn Laws; Anderson the Scottish farmer; Carey, North,
  Locke and Turgot on rent and interest; Palmerston's "house of landlords";
  Capps before the Select Committee; Engels on 1846 and the prairies; Henry
  George; Petty, Cantillon and the physiocrats; Clark in 1899. Each is given
  what his view rests on before Marx is heard.
- **Second person in `p` and `worked.intro` only.** "You want its price, and
  its price when the rate of interest falls to 4%" is the shape every worked
  intro takes; `steps`, `standard`, quiz items and tile text stay impersonal.
- **Marx's jokes before the lesson's.** Horace's "fruges consumere nati",
  Palmerston, the manufacturer buying "more of his own yarn", poverty "more
  lucrative than the mines of Potosi"; none is the lesson's own.
- **The limit admitted, and varied.** Every `note` names what its lab cannot
  show, and the "this Subject leaves it open" move is worded differently each
  time it appears ("without deciding which account is right"; "the question the
  Subject leaves open"; "the dispute is about what that price measures"; "the
  tables cannot answer it"; "the assumption, named, and the case in which it
  fails"). The Course 1 lesson about repeating the move was applied.
- **Pointing forward by title.** All eleven bodies end with the next lesson's
  question by the next lesson's title; the last ends with Revenues and Their
  Sources and its question.

## What the course teaches well

- **Objectives are acts, and the drills measure them.** Every `standard`
  begins "Finish when you can…" and names the product; the six course
  `outcomes` are the same acts, and `outcomes_intro` says what the whole course
  is for ("rebuild Marx's rent tables from the figures in his sentences").
- **One quantity per lesson, and the lab's unit kept constant.** The decision
  to reckon the `dr1`/`dr2` labs in shillings throughout, against Marx's
  change to pounds after Chapter 39, is explained once in `how_to`, again at
  the first lesson that needs it, and lets every table be compared with the
  last; the lessons give Marx's pound figures beside the tiles each time.
- **Misconceptions refuted with the specific figure.** Rent is not the return
  on the land's value: £200 stays while £4,000 becomes £5,000. The waterfall
  does not create the surplus: steam at 90 and the rent is 0. Rent does not
  need worsening land: the price halves to 30s and total rent rises to 450s.
  DR II is not a different source: 4, 3, 2, 1 on one acre is 360s. More output
  does not lower rent per acre: B goes from 60s to 90s. A falling price does
  not settle rent: 180s, 360s, 720s. Rent is not the cause of dear bread: the
  price is 80s because the extra quarters cost 80s. The worst soil can pay:
  10s with nothing worse in use. Absolute rent is bounded: at most 5, or 2 with
  the market limit, 0 at the average composition. A dearer plot is not a
  better plot: the owner "contributes nothing". The wage-worker's unpaid hours
  are the serf's days: 100% either way.
- **Engels' hand is marked where it matters.** The Chapter 43 opening, the
  twenty-one bushel tables, the 1846 note and the Chapter 44 bracket are each
  attributed, and `mistakes[2]` of the rising-price lesson exists to stop a
  reader taking Engels' opening for Marx's. The `how_to` says in advance what
  kind of text Part VI is.
- **The kit's limits are stated at the point of use.** Table II's seventh
  soil, D's eleven doses, Marx's unequal extra dose, the averaging rule, the
  market limit against Marx's assumption that A drops out: each is named in
  the lesson that meets it and in `not_covered`.
- **Opponents at strength, critics in their own terms.** Ricardo in lessons 3,
  4, 7 and 9; the marginal-productivity account in 1, 2, 7, 8 and 11 ("remove
  it and output falls, so it earns its rent as machines earn theirs");
  Bortkiewicz in 9 ("the assumption the transformation debate after
  Bortkiewicz questions"); Clark in 11 ("no hour is unpaid; the corvée
  peasant's lost days are a coercion a free labour market does not have").
  In each case what follows is "what the chapter says bears on it", never
  "Marx's answer".

## What it taught badly, or said wrongly

### Quiz explanations that did not derive their distractors

- **`differential-rent-i`, quiz 1:** "240s forgets the profit" and "120s is the
  middle soil's figure" were both wrong: forgetting the profit on 100s gives
  150s, and the middle soil's rent is 60s. 240s is `5 · 60 − 60`, Marx's cost
  and profit used instead of the question's 120s; 120s is the cost and profit
  itself. Repaired to say so.
- **`differential-rent-ii`, quiz 1:** "240s forgets the profit on the capital"
  gives 210s, not 240s; 240s is `360 − 120`, two doses' cost and profit
  deducted instead of three. Repaired.
- **`differential-rent-general`, quiz 1:** the distractor 38 had no derivation
  ("subtracts only the water user's own profit" does not produce it).
  Replaced by 40, the water user's whole profit, which is the error a reader
  actually makes, with the `why` saying so.
- **`introductory-remarks-on-rent`, quiz 2:** "£3,200 multiplies instead of
  dividing" was too vague to correct the error; it is £4,000 cut by a fifth,
  the price moved with the rate instead of against it. Repaired.

### Fidelity

- **`introductory-remarks-on-rent`, body:** "Marx's dry Latin for the
  landowners is 'fruges consumere nati'". The line is Horace's (Epistles I.2);
  Marx quotes it. Now "Marx borrows Horace's Latin".
- **`dr-ii-falling-price`, body:** "A misprint on the way" asserted an origin
  for the "D" at l. 5956 that the text cannot support. Now "A slip on the way".
- **`genesis-of-capitalist-ground-rent`, body:** "the thing some historians
  found surprising" attributed a reaction to no one in particular and is not in
  the chapter; what Marx says (l. 6785) is that "the possibility of a certain
  economic development" is open to the serf. Now quotes that phrase, reworded
  around its capital. In the same lesson "profit hardly existed" for Petty and
  Cantillon is looser than l. 6725, where profit "is still vaguely combined with
  wages"; now "profit not yet a category of its own, still mixed up with wages".

### Speech

Every math run on the eleven pages was read from `data-say`. The author had
already added a Ground Rent block to `content/spoken/capital.py` covering the
shilling figures, the grouped thousands, "IV d" and "A−1", and those read
well ("Table four d, 360 shillings again at half the price"; "soils A minus 1
and A minus 2 brought in"). Two shapes were missed and are repaired in the
content rather than in spoken forms, since another agent is editing the speech
engine and the kit concurrently:

- **`differential-rent-ii`, `key[0]` and `key[4]`:** "DR II: successive
  capitals on one field" and "harder to fix in a lease than DR I" were read
  "D R". Now "second form: …" and "… than the first form"; the mistake title
  that used the abbreviation now spells it out too.
- **`differential-rent-ii`, worked line 2:** "(the 4th dose)" was read "the
  4 t h dose". Now "(dose 4)".

### Course home

- **`how_to`** did not say which lesson is the hardest or that the later
  lessons reuse it, which Course 1's `how_to` does for "The Form of Value".
  One sentence added to `how_to[2]`: Differential Rent I is the lesson to read
  slowly, because the five lessons after it reuse its four soils and its price
  rule.

### Cross-references

Lessons are cited by title (“Differential Rent: General Remarks”,
“Differential Rent I”, “Differential Rent II”, “Differential Rent II at a
Constant Price of Production”, … “Genesis of Capitalist Ground Rent”), each as
the next lesson carries it; Marx's chapters by volume and number; the earlier
courses by their §B titles (Average Profit and Its Fall, Merchant's Capital and
Interest); the next course as Revenues and Their Sources. Every `module` name
is the Kerr chapter title. No lesson is cited by number.

## Can a reader follow the six differential-rent lessons?

Yes, with two conditions the course now states. The first is that
`differential-rent-i` is read slowly, because it is the only place the
regulating-price rule is built from nothing and everything after it assumes
the rule. The second is that the reader accepts the lab's one simplification,
valuing every dose by itself at the regulating price, as a model and not as
Marx's practice; the lessons say so at every point where Marx averages
instead, and `not_covered` says so for the course. Within those conditions
the sequence is a progression in the textbook sense: each lesson adds one
input to the same lab (`dr1` → `dr2` → `price_case` → `market_limit` →
`former_price` → the worst-soil case) and one quantity to read off it, and
the worked examples fade from a full table by hand (Table I) to one soil
(B's two doses), one route (A−1 and A−2) and one comparison (Marx's rule
against Engels').

The place a reader will still slow down is the Chapter 43 lesson's passage
paragraph, where Marx's argument needs the acre's average price that the lab
does not compute, so the figures there (losses of 30s and 60s against 90s of
rent) are read from the text rather than pressed in the lab. The lesson is
honest about this and gives the p. 849 figures exactly; it cannot do more
without the kit change below.

## Repairs made in this pass

In `content/capital/c13_rent/__init__.py`: `how_to[2]`. In `part_a.py`:
`introductory-remarks-on-rent` the Horace sentence and quiz 2's `why`;
`differential-rent-general` quiz 1's fourth option and `why`;
`differential-rent-i` quiz 1's `why`; `differential-rent-ii` `key[0]`,
`key[4]`, worked line 2, `mistakes[0]` title and quiz 1's `why`;
`dr-ii-falling-price` "misprint" → "slip". In `part_b.py`:
`genesis-of-capitalist-ground-rent` the labour-rent paragraph (Marx's phrase in
place of the historians) and the Petty–Cantillon sentence. No preset,
`expect`, slug, module, lab key, mode, view or `price_case` changed, and no §C
entry needed correcting: every instance the lessons carry is the one §C
records, and every **Text:** note in §C was confirmed against the text and the
image.

`scripts/preview_subject.py capital --course capital-ground-rent` reports OK:
12 pages, every lab executes and survives the sweep, every pinned figure on
the eleven pages matches, no math run without a spoken form; the strict
quotation checker reports 151 segments and 0 misses; and a second pass over
every `data-say` finds no spelled-out word.

## Remaining issues

- **The kit cannot price an acre at its average.** Marx's own rule in Chapters
  43 and 44 (and Table V of Chapter 42, and the whole of Engels' twenty-one
  tables) prices a soil's whole product at its individual average cost over
  its doses, and the lease argument that is the Chapter 43 passage turns on
  it. The `dr2` view values each dose separately, so the two subtlest
  arguments of the Part are told in prose with Marx's figures and cannot be
  pressed. An `average_per_acre` switch on `dr2` (price each soil's product at
  its summed cost and profit over its summed output; with `former_rent` for
  Engels' Chapter 44 rule) would let `dr-ii-rising-price` compute the p. 849
  table and `rent-on-the-worst-soil` compute 3 1/9 and 1/9 beside 70s and 10s.
  That is a kit change for the chrome-renderer tier; recorded, not made.
- **Six soils and six doses.** Table II's seven soils and D's eleven doses are
  worked round (four soils in prose; one 550s capital), and both lessons say
  so. A `dr1` that took eight soils would let Table II be pressed whole.
- **One more slip in the l. 5651 sentence.** "More than doubled upon D"
  (180s → 240s) is as wrong as "doubled upon C", and the lesson names only the
  latter. A reader checking the sentence will find it; not changed, since the
  paragraph already names two slips in one sentence and a third would crowd it.
- **`differential-rent-i` is at the edge of its load.** Eleven paragraphs, four
  presets, Ricardo's biography, Table II's three extra soils, the two slips and
  the false social value in one lesson. It is the chapter's own shape and the
  URL space does not allow a split; the `how_to` warning is the mitigation.
  Were the space to open, "Differential Rent I" / "What Differential Rent Does
  Not Require" (Tables II and III, the Ricardo quarrel, false social value) is
  the natural seam.
- **Two quiz items ask about the page rather than a fresh instance.**
  `dr-ii-falling-price` quiz 2 ("In which preset does the total rent rise…")
  and `differential-rent-i` quiz 2 ("In the improved preset…") test recall of
  the presets; each is defensible because the `why` makes the reader reason
  about why, but a fresh instance would be stronger retrieval practice.
