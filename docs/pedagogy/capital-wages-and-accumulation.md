# Pedagogy assessment — Wages and Accumulation (Capital, course 4)

Formed from the nine lesson dicts in `content/capital/c04_accumulation/`
(`part_a.py`, lessons 1–5, Volume I Chapters 19–23; `part_b.py`, lessons 6–9,
Chapter 24 and three lessons on Chapter 25; `__init__.py`, the course dict),
and the kit they render through (`scripts/mathpath/labs/capkit.py`, modes
`wages` and `accumulate`; views `form`, `time`, `piece`, `national`, `simple`,
`expand`, `labour`, `composition`, `law`), on branch `feat/capital-subject`
before the Subject was wired into the site. The design authority is
`docs/capital/PLAN.md` §0, §B, the Course 4 entries in §C, §D as summarised in
`docs/capital/kit-a-report.md`, §E and §F; the model for this assessment is
`docs/pedagogy/capital-commodities-and-money.md`, and Course 1 is the voice
reference.

Every lesson was read in full before anything was changed. Every pinned tile
on the nine rendered pages was read off with `node scripts/labcheck.js
--observe` (rendered through `scripts/preview_subject.py capital --course
capital-wages-and-accumulation`); every figure in prose, steps, worked lines,
quiz items and mistakes was recomputed by hand, in shillings and pence where
the chapter reckons in them, and the five iterating presets were re-run in
Python against the engine's own rules (`acRun` in `capkit.py`) row by row.
Every quotation and every phrase in `&ldquo;…&rdquo;` (seventy-two spans after the repairs) was
searched for in `/mnt/project-files/capital-texts/volume-1-kerr.txt` with the
strict quotation checker; Chapters 19–25 were read whole in that text, Chapter
25 §§1–4 line by line and §5 for the passages the last lesson leans on
(Gladstone, Dr Smith, Dr Hunter, the gang system, Ireland). Lessons, in course
order: `value-of-labour-power-into-wages`, `time-wages`, `piece-wages`,
`national-differences-of-wages`, `simple-reproduction` |
`surplus-value-into-capital`, `accumulation-with-constant-composition`,
`the-reserve-army`, `the-general-law-of-accumulation`. The bar marks the seam
between the two modules. The course assumes Courses 1–3 and is judged against
them.

## Verdict

The course teaches its subject. A reader who finishes it can take a daily wage
and a working day and separate the apparent price of an hour from the value the
hour creates; compute the price of an hour from the normal day and the day's
wage for any hours worked, and say whether short time leaves the worker below
the value of his labour-power; compute a piece-rate from the normal output and
recompute it when the output doubles or the rate is cut; compare two countries'
wages per unit of output and their rates of surplus value; divide a capital by
the surplus value consumed to find Marx's years; run accumulation at a fixed
composition for five periods and find the original capital's share; follow the
demand for labour at a constant and at a rising composition and read off the
reserve; and compute the ratio of reserve to employed while the wage moves.
Those are the acts the `standard` fields name and the quizzes measure; no
objective is "understand X". The `mistakes[0]` of every lesson is the §C
misconception, each refuted with a tile: 3d paid against 6d created; the
ten-hour preset's higher rate and identical 3s; the cut preset's ¾d and 3s;
England's `3/4` and `5/3`; the `5 years`; the half preset's £1,000 consumed and
£1,000 added; the wage-rise preset's falling s; `300` employed while capital
triples; the boom's `£12` and `1/19`. All 24 pinned tile strings on the nine
pages matched the lab, and every figure in prose agreed with the lab or with a
recomputation except the two corrected below.

Fidelity to Chapters 19–25 is high. Sixty-seven of the seventy-two quoted
spans were found verbatim; the five the checker missed differ only in an
initial capital (`To put it mathematically`, `The lowest sediment`, `be his
payment`) or a drop capital (`ON the surface`, `WAGES by the piece`). No
phrase was invented. Chapter 25 is
read as Marx wrote it: the composition defined twice and held fixed, the
"independent variable" sentence quoted, his £6,000 → £18,000 sum and his
1:1 → 7:1 ratios used as the lab's own instance, the three forms and pauperism
in his order, the "absolute general law" quoted with its qualifying sentence,
Ortes and Townsend where he puts them, and Gladstone's 1863 budget speech
cited for the sentence Marx actually quotes from it. Marx is presented, not
endorsed: ten modern critics are named, each in two or three sentences at full
strength and each in the lesson his objection concerns; their dates were
checked and are right. The lab's wage-rise rule is flagged as the lab's model
and not Marx's in the lesson body, the `note` and the course `not_covered`.

The defects were local and are repaired below: one share of capital given as
"five ninths" where the lab prints 59.8%; one boom-preset paragraph that
described the wage column as a smooth +10s a period when the lab's own rule
pushes it off that path in periods 2 and 3; Solow's model credited with raising
wages "as far as you like"; a misspelled Eden; a Mandeville sentence
attributed to "none of them"; one quiz whose distractors were not named
errors; one tile left unexplained. Nothing needs splitting, merging or
reordering within the URL space the course has; one load problem is recorded
under remaining issues.

## The voice, judged against §F and Course 1

**What matches the reference, and should be kept:**

- **The passage first, then its phrases in order.** Every body opens with the
  `<strong>Volume I, Chapter n.</strong>` block and goes back through it: "Read
  the middle sentence twice. Labour, the activity, does not exist yet when the
  bargain is struck" (lesson 1); "Now the passage. The numerator is 3s, which
  is 36d, and it does not move" (lesson 2); "Read it as a sum. At half and
  half, £6,000 has £3,000 variable" (lesson 8); "Now the passage. 'Be his
  payment high or low' is the phrase to hold on to" (lesson 9). Lessons 5–9,
  whose chapters are long, use two passages each and say where in the chapter
  each sits ("The passage comes from the third section, after the story of the
  Manchester manufacturers").
- **Scenes only where the object is in the reader's life.** Part VI is about
  wages, so the four wage lessons open with the payslip ("If you have ever been
  paid by the hour, you know this sentence from the inside"), two jobs at the
  same weekly wage, piece-work ("If you have been paid per delivery, per item
  packed or per article written") and wages compared across countries ("You
  have probably heard wages compared across countries, usually by the day or
  the hour"). Part VII's lessons open with the text itself, which is what §F
  rule 2 asks when a scene would have to be invented. Course 1 did the same.
- **The history of ideas as a story with people in it.** Smith half-finds
  labour-power and "kept the wrong name for it"; the full-priced London bakers
  complain to Parliament; Cowell of the 1833 Factory Commission and Redgrave's
  spindle table; Potter's letter to the *Times* and the *Times*'s reply; Dr
  Aikin's four periods of Manchester; Senior "the Oxford professor of the last
  hour, who a year before that discovery had announced another"; Bellers in
  1696, Mandeville, Eden; Merivale moving from Oxford to the Colonial Office;
  the Wiltshire farmers who "did not wait for the labourers to multiply";
  Gladstone at the dispatch box. Every opponent is given the fact his view
  rests on before Marx answers.
- **Second person in `p` and `worked.intro` only.** "You want the apparent
  price of an hour and what the day leaves unpaid"; "You want the capital after
  one year and after five". `steps`, `standard`, quiz items and tile text stay
  impersonal. No "Let's", no "dive in", no first-person anecdote. The one "we"
  on the course ("here, Marx says, we find 'the sources of the sufferings…'")
  is Marx's own.
- **One light remark, and Marx's before the lesson's.** "Marx calls their
  complaint a jeremiad and enjoys it" (lesson 2); "He adds, dryly, that the
  capitalist rightly knocks such pretensions on the head" (lesson 3); the
  `read_title` "Marx at his most sardonic" over "Moses and the prophets"
  (lesson 6); "28 4/7 per cent, 'which sounds very fine'" (lesson 8). None is
  the lesson's own invention.
- **The limit admitted.** Every `note` names what the lab cannot do: the 6d an
  hour creates "is an input: the lab takes it from the chapter and does not
  derive it"; the lab "does not model a separate overtime rate"; it "values
  both countries' output at one world-market price per unit, which is Marx's
  claim"; the years are "a way of reckoning, not a fact the ledger records";
  the wage rule is "the lab's model of Marx's 'wages may rise'; the chapter
  states the direction and the limit, not a formula"; "it does not measure
  misery, and it holds no data on real wages or unemployment".
- **Pointing forward by title.** Each body ends by naming the next lesson's
  question by the next lesson's title, and the last lesson ends with the next
  course by its §B title and its question ("where the first capital came
  from").
- **The "this Subject does not settle it" move is varied**, as the Course 1
  review asked: "cannot decide between the two" (1), "a question about
  particular firms that this chapter's arithmetic cannot answer" (3), "the
  disagreement is over the second tile" (4), "Readers who find the
  accountant's description equally good are not making an arithmetic mistake"
  (5), "The two accounts do not disagree about the arithmetic below; they
  disagree about what it rewards" (6), "The lab builds that claim in, so it
  cannot test it" (7), "The lab assumes the rise you give it and computes the
  consequence" (8), "This course leaves the question open" (9).

**Where it differs from Course 1, and whether that is a defect:**

- Course 1's bodies are eleven or twelve paragraphs; lessons 6–9 here run to
  thirteen or fourteen, because Chapters 24 and 25 are long and the author
  chose to carry their minor sections (Chapter 24 §§2, 4, 5; Chapter 25 §2's
  centralisation) in prose rather than drop them. The `how_to` warns the reader
  that "Part VII is long, and Chapter 25 is the longest in Volume I". That is
  the right trade for a read-along, and it is recorded, not changed.
- Course 1 names each opponent once and in the lesson his criticism concerns;
  this course does the same, and adds a modern critic to every lesson, which
  §F's "presented, not endorsed" rule asks for and Course 1 could not always
  do (Chapter 1 has fewer modern antagonists than Chapter 25).

## The modern critics, checked

Each was checked for who he was, what he claimed, whether the claim is stated
at strength, and the date.

- **J. B. Clark, 1899** (lesson 1): *The Distribution of Wealth*; under
  competition the wage equals the marginal product of labour, so nothing is
  unpaid and the remainder is capital's product. Right, at strength, and
  placed where it bites (the 6s against 3s).
- **Lionel Robbins, 1930** (lesson 2): "On the Elasticity of Demand for Income
  in Terms of Effort", *Economica*; a wage rise can lengthen or shorten the
  hours a worker chooses. Right, and the lesson says fairly that Marx's
  chapter assumes the normal day is set by employer, custom and law.
- **Edward Lazear, 2000** (lesson 3): "Performance Pay and Productivity",
  *American Economic Review*, the Safelite windscreen study; output per worker
  rose substantially, roughly half from effort and half from sorting, and pay
  rose. Right; the ratchet effect is correctly named as the same literature's
  version of Marx's point.
- **Henry Carey** (lesson 4): the *Essay on the Rate of Wages* is 1835, which
  Marx calls "one of his first economic writings"; the date has been added.
  Carey's premise is restated as the unit-labour-cost comparison economists
  make today, which is generous and correct.
- **Marshall, Böhm-Bawerk, Fisher** (lesson 6): "waiting" is Marshall's term
  in the *Principles* (1890); Böhm-Bawerk's *Positive Theory of Capital* is
  1889 and Fisher's *Rate of Interest* 1907. Dates added. The time-preference
  account is given its strongest form ("gives up something real, present
  consumption") before Marx's class-level reply.
- **Robert Solow, 1956** (lesson 7): "A Contribution to the Theory of Economic
  Growth". The lesson said capital deepening raises the real wage "as far as
  you like"; in the model the rise is bounded by diminishing returns and the
  steady state. Reworded: nothing in the model pushes wages back down, and the
  brake is diminishing returns, not a squeeze on unpaid labour. That is the
  contrast with Marx's second case, stated accurately.
- **Nicholas Kaldor, 1961** (lesson 8): "Capital Accumulation and Economic
  Growth", the stylised facts, including a roughly constant capital–output
  ratio. Right, and the inference (a constant K/Y with a constant labour share
  implies a constant value composition) is sound; the lesson also gives
  Marx's own qualification about the cheapening of means of production, which
  is the defenders' reply.
- **Eduard Bernstein, 1899** (lesson 9): *Die Voraussetzungen des
  Sozialismus*; falling-real-wage reading contradicted by British wages. Right.
- **Gladstone, 1863** (lesson 9): "While the rich have been growing richer, the
  poor have been growing less poor" is from the Budget speech of 16 April 1863
  as Marx quotes it (Kerr l. 4815), and Marx's "relatively just as poor" is
  his reply to it (l. 4817). Right.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** Every
  `standard` begins "Finish when you can…" and names the product: "separate the
  price of an hour from the value it creates" (1); "compute an hourly price and
  a day's wage from a time-wage" and say whether it is below, at or above the
  daily value (2); "compute a piece-rate and the day's wage it pays" and
  recompute when the output changes or the rate is cut (3); "compare two
  countries' wages per unit of output" (4); "compute the years in which a
  capital is consumed" and say what the remainder then represents (5); "run
  accumulation for several periods by hand" (6); "follow demand for labour as
  capital accumulates" and identify the period demand first exceeds supply
  (7); "compute employment and the reserve under a rising composition" (8);
  "compute the reserve ratio and say what it does and does not show" (9). The
  five course `outcomes` are the same acts.
- **One hard idea per lesson, and the chapters' arithmetic kept apart.** The
  wage lessons each carry one fraction: 3s over the hours; 3s over the normal
  day times the hours worked; 3s over the normal pieces; wage over output.
  Lesson 5 is one division, lesson 6 one geometric growth, lesson 7 adds the
  supply, lesson 8 adds the rise in c/v, lesson 9 adds the wage path and the
  ratio. Each `key` list is the chapter's arithmetic in five or six lines and
  nothing else.
- **The misconceptions are refuted with the specific figure.** "At 3s for 12
  hours the apparent price of an hour is 3d while the hour creates 6d" (1);
  "The ten-hour preset pays 3 3/5d an hour, more than the normal preset's 3d,
  and its day's wage is the same 3s" (2); "the worker makes twice as many
  pieces and the day pays 3s, exactly as before, because the rate fell from
  1½d to ¾d" (3); "England pays 1½ times the wage for twice the output, its
  relative wage is 3/4, and its rate of surplus value is 166.67% against the
  Continent's 100%" (4); "The half preset consumes £1,000 of the first year's
  surplus value and still adds £1,000 to capital" (6); "capital triples and
  employs 300 workers from first period to last" (8); "the wage rises from £10
  to £12 while the ratio of reserve to employed rises from 0 to 1/19" (9).
- **The arithmetic is right, in shillings and pence.** `36/10` is 3 3/5d,
  `36/15` is 2 2/5d, 12 × 3 3/5d is 43 1/5d = 3s 7 1/5d, 6 × 3 3/5d is 1s
  9 3/5d, 8 × 3d is 2s; `36/24` is 1½d and `36/48` is ¾d, 30 × 1 1/5d is 3s;
  England's `(2·8 − 6)/6 = 10/6`; 10,000 × (6/5)⁵ = 24,883.2 = £24,883 4s
  and 10,000 × 1.1⁵ = £16,105 2s, with shares `3,125/7,776` and
  `100,000/161,051`; £5,120 at c/v 1 with half of s capitalised grows by
  exactly a quarter a period, giving 256, 320, 400, 500, 625 workers; Marx's
  £18,000 at 4:1 is `18,000/5 = 3,600`; the slump's 150 against 270 is `9/5`;
  the long run's ten periods give `9/10`. The tight preset's "s is £3,600
  instead of £4,000" and the wage-rise preset's "£2,800 in period 2 to about
  £1,181 in period 5" were confirmed from the engine's own rule (value per
  worker = (1 + s′) × the first period's wage; wage = v / supply when demand
  exceeds supply).
- **The lab's model is kept apart from Marx's definition.** The wage rule is
  called "the lab's own model" in the body of lesson 7, "the lab's model of
  Marx's 'wages may rise'" in its `note`, and "one simple rule" that the labs
  "never let … fall back" in the course `not_covered`; the step that states
  the rule now says "by the lab's rule". The boom's wage rise is called "an
  input, not the result of the reserve's absorption that Marx describes".
  Which figures are Marx's (3s, 12 hours, 6d; 24 and 48 pieces; £1,000 and
  £200; £10,000 at 4:1; £6,000; 1:1 to 5:1) and which are the author's
  (England's 6d and 2 lb; £5,120; £10 a worker; 300 workers) is said in every
  preset label and `note`.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` asks for a prediction
  ("Compare normal with ten-hour, and then overtime and short time with the
  day they depart from"; "Watch the wage and s columns in the tight preset
  from period 3"; "Read the capital and v columns of the rising preset
  together: one triples, the other does not move"); every quiz asks the same
  act on a fresh instance (4s over 12 hours; 36 pieces; 9d for 3 lb against 4d
  for 1 lb; £1,500 and £300; £8,000 at c/v 1; £12,000 at c/v 3; 400 employed
  and 100 idle). Distractors are the named errors: dividing the whole capital
  by the wage, dividing by 3 instead of 4, the old rate on the new output.
- **Chapter 25 is three lessons with a clean seam.** Lesson 7 is §1 and
  nothing else; lesson 8 is §2 and §3 ("Begin with §2, which supplies the
  cause"); lesson 9 is §4 with §5 summarised and one exchange quoted, as the
  course `how_to` and `not_covered` promise. Each ends where the next begins
  ("Marx immediately drops the assumption"; "A reserve army has been produced;
  Marx now asks who is in it").
- **The seam at lesson 6 is invisible.** `simple-reproduction` ends "asks what
  happens when the capitalist does not"; `surplus-value-into-capital` opens
  with the capitalist who does. Both modules spell British, cite lessons by
  title and chapters by number, and use the same tile vocabulary.

## What it taught badly, or said wrongly

### Arithmetic

- **`surplus-value-into-capital`, `mistakes[0]`:** "after five periods of the
  marx preset five ninths of the capital was never anybody's to abstain
  from". The original's share is `3,125/7,776 = 40.19%`, so the capitalised
  part is 59.81%, nearly three fifths; five ninths is 55.6%. Now "nearly three
  fifths".
- **`the-general-law-of-accumulation`, body:** "the wage rises by 10s a
  period, from £10 to £12. Employment grows from 300 to 475, and still the
  supply … outruns it … Wages and the reserve rise together." The engine's
  wage column for the boom is 10, 11 3/7, 11 9/16, 11½, 12: in periods 2 and 3
  demand exceeds the supply, so the lab's rule sets the wage to v/supply,
  above the +10s path, and the reserve is 0 in every period but the fifth. A
  reader following the panel's instruction to "read the wage and reserve
  columns together" would have seen neither the smooth rise nor the reserve
  rising with it. Now says what the columns show: the set path, the two
  periods pushed above it, the return to the path at £11 10s, and the reserve
  of 25 appearing only in period 5, with the comparison made between the
  first period and the last. The pinned tiles, the worked example (period 5),
  the quiz and `mistakes[0]` were already correct at the endpoints and stand.
- **`accumulation-with-constant-composition`, body and `mistakes[0]`:** "the
  wage climbs every period" in the wage-rise preset; it is £10 in period 1,
  where 256 are wanted of 300, and climbs from period 2. Now says so.

### Fidelity

- **`accumulation-with-constant-composition`, body:** "What none of them saw,
  Marx says" generalised to Bellers, Mandeville and Eden a remark Marx makes
  of Mandeville alone ("What Mandeville, an honest, clear-headed man, had not
  yet seen"). Now attributes it to Mandeville with Marx's epithet quoted.
- **Same lesson:** "Sir Frederic Eden" for Sir Frederick Morton Eden (Kerr:
  "Sir F. M. Eden"). Corrected.
- **Same lesson, the Solow paragraph:** see the critics section above.

### Prose that left the lab unexplained

- **`surplus-value-into-capital`, `panel_intro`:** the expand view carries a
  third tile, `acHoard`, which prints `£0` in every preset because
  `invest_threshold` is 0; nothing on the page said what it was. One sentence
  added.

### Quiz

- **`simple-reproduction`, quiz 1:** the distractors 3, 4½ and 6 were, as the
  `why` admitted, numbers that "come from no division of these two figures",
  so they tested nothing. Now 3, 10 and 6, where 10 is the half-consumed case
  and 6 divides the capital with one year's surplus added; the `why` names
  each. Every other distractor on the course was argued for and could not be
  defended.

### Dates

- Carey (1835), Marshall (1890), Böhm-Bawerk (1889) and Fisher (1907) were
  named without dates where the other critics had them; added, so that §F
  rule 3 ("who they were and what they claimed") is met uniformly.

### Speech

Every math run on the nine rendered pages was read from `data-say`. The
shillings and pence read well ("3 shillings over 12 hours equals 3 pence an
hour", "36 pence over 10 equals 3 and 3 fifths pence"), `s′` reads "s prime",
`lb` reads "pound", and no key line begins with a word the engine spells out;
the "the" that opens two key lines in lesson 1 is read as a word. Nothing to
repair.

### Cross-references

Lessons are cited by title (“Time-Wages”, “Piece-Wages”, “National Differences
of Wages”, “Simple Reproduction”, “Surplus Value into Capital”, “Accumulation
with Constant Composition”, “The Reserve Army of Labour”, “The General Law of
Capitalist Accumulation”), each as the next lesson carries it; Marx's chapters
by volume and number; earlier courses by their §B titles (Commodities and
Money; From Money to Surplus Value; Relative Surplus Value); the next course as
“So-Called Primitive Accumulation”. Chapter 15 and Chapter 17 are cited by
number where Marx cites them.

## Can a reader who has finished Courses 1–3 follow the accumulation lessons?

Yes. The hard step is lesson 7, where a reader who has only ever added s to
capital must also divide v by a wage, compare with a supply, and accept a rule
for what happens when the comparison fails. The lesson gives the rule in the
steps, flags it as the lab's, and chooses an instance (£5,120, a quarter a
period) in which every figure before the shortage is a round number, so the
reader can check 256, 320, 400 by hand and see 400 pass 380. Lesson 8 then
removes one assumption (constant c/v) and keeps everything else, and the
rising preset is built so that v is £3,000 in every row, which a reader can
verify in a line. Lesson 9's boom asks the most of the reader, and its worked
example honestly starts from period 5's capital rather than deriving it; the
corrected paragraph now tells the reader what the wage column will show and
why, which is the explanation the panel's instruction needed.

## Repairs made in this pass

In `part_a.py`: `national-differences-of-wages` (Carey's date);
`simple-reproduction` quiz 1 distractors and `why`. In `part_b.py`:
`surplus-value-into-capital` the Marshall paragraph (dates), `panel_intro`
(the hoard tile), `mistakes[0]` (three fifths);
`accumulation-with-constant-composition` the Bellers–Mandeville–Eden
paragraph (Mandeville, Frederick), the tight/wage-rise paragraph, the Solow
paragraph, `steps[2]`, `mistakes[0]`; `the-general-law-of-accumulation` the
boom paragraph. No preset, `expect`, slug, module, lab key, mode or view
changed, and no §C entry needed correcting: every instance the lessons carry is
the one §C records.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-wages-and-accumulation` reports OK: 10 pages, 9 labs executed and
swept, 9 with pinned figures, 0 failing, no math run without a spoken form; the
strict quotation checker finds 72 spans and 5 misses, all five a difference of
initial or drop capital only.

## Remaining issues

- **`the-general-law-of-accumulation`'s boom preset is a weak demonstration
  of its own point.** It is meant to show the reserve ratio rising while wages
  rise, and on the lab's rule the ratio is 0 for four periods and `1/19` in
  the fifth, because the shortage in periods 2–3 pushes the wage above the set
  path. An instance in which the supply stays ahead of demand throughout (so
  the wage follows its path and a small reserve is present from period 2)
  would make the same point in every row; with integer workers it needs new
  figures and a §C change, so it is left to the author and recorded here.
- **The slump preset prints a fractional worker.** At c/v rising by ½ from
  £6,000, period 4 has v = 6,000/3.5 and employs 171 3/7 workers. The prose
  never mentions period 4 and the pinned tiles are period 5's integers, but a
  reader looking at the table sees `1,200/7` workers. A capital of £4,200
  (divisible by 2, 2.5, 3, 3.5 and 4 into tens) would give integers
  throughout; it changes three pinned strings and the §C instance. Recorded.
- **Lesson 8 carries the most.** Rising composition, concentration against
  centralisation, the reserve as a condition of production, over-work swelling
  the reserve, the Wiltshire wages, the compensation theory and Kaldor are one
  lesson because §B gives Chapter 25 three slugs. The natural fourth would be
  "Concentration and Centralisation" (§2's second half), which the URL space
  does not have. Not done; recorded for the orchestrator.
- **The wage rule never lets wages fall back.** Marx's second case in §1 (the
  reaction: accumulation slackens, the disproportion vanishes, wages fall) is
  the half of the alternative the lab cannot show, and lessons 7 and 9 say so.
  A `wage_floor`/relaxation rule would be a kit change and is out of scope
  here.
- **Lesson 9's worked example starts from a given capital.** "The capital laid
  out in period 5 is £34,200" is handed to the reader because deriving it
  requires the wage rule applied four times. It is honest, but it is the one
  worked example on the course a reader cannot reproduce from the lesson's
  inputs alone without the table.
