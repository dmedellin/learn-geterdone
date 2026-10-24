# Pedagogy assessment — Average Profit and Its Fall (Capital, course 10)

Formed from the eight lesson dicts in `content/capital/c10_prices/`
(`part_a.py`, lessons 1–4, Volume III Chapters 8–11; `part_b.py`, lessons 5–8,
Chapter 12 and the three chapters of Part III; `__init__.py`, the course dict),
and the kit they render through (`scripts/mathpath/labs/capkit_b.py`, modes
`prices` and `tendency`, views `rates`, `production`, `wage-rise`, `law`,
`counter`, `overaccumulation`; and `capkit.py`'s `value` mode, view `market`,
for Chapter 10), on branch `feat/capital-subject` before the Subject was
wired. The design authority is `docs/capital/PLAN.md` §0, §B, the Course 10
entries in §C, §D.2–D.3 as summarised in `docs/capital/kit-b-report.md`, §E,
§F and §G; the author's brief is `docs/capital/AUTHORING.md`, whose two
closing sections list the errors Course 1 made, and this course is judged
against that list in particular. The voice reference is Course 1.

Every lesson was read in full before anything was changed. Every pinned tile
(26 preset strings over eight pages) was read off the rendered page with
`node scripts/labcheck.js --observe` after
`python3 scripts/preview_subject.py capital --course capital-prices-of-production`;
every figure in prose, worked lines, quiz answers and `why`s was recomputed
exactly; every quotation and every phrase inside `&ldquo;…&rdquo;` (84
segments) was checked against `/mnt/project-files/capital-texts/volume-3-kerr.txt`
with the strict quotation checker; every chapter the course reads was read in
the Kerr text, not only the quoted passages; and every `data-say` on the nine
rendered pages was read. Marx's Chapter 9 tables, which the plain text drops,
were read from the page images at
`/mnt/project-files/capital-texts/tables/volume-3/` (`lf0445-03-0183-t0001.png`,
`lf0445-03-0185-t0001.png`, `lf0445-03-0185-t0002.png`) and every figure the
author wrote from memory was checked against them. Lessons, in course order:
`different-compositions-different-rates`, `the-general-rate-of-profit`,
`market-value-and-surplus-profit`, `wages-and-prices-of-production` |
`supplementary-remarks-on-prices`, `the-law-as-such`,
`counteracting-influences`, `internal-contradictions-of-the-law`. The bar
marks the seam between the two modules. The course assumes Cost Price and the
Rate of Profit and, from Volume I, the rate of surplus value and the rising
composition of capital, and is judged against that.

## Verdict

The course teaches its subject, and it is the first of the Volume III courses
to carry a live dispute without taking a side in it. A reader who finishes it
can compute rates of profit at value for capitals of different composition
and say which difference drives the ranking, transform Marx's five spheres
into prices of production with inputs at value and check both totals, form a
market value as the average over every unit and read off each group's surplus
profit, reprice three spheres after a general wage rise with the new rate
taken over the enlarged capital, pay a premium out of a fixed total and watch
the base rate fall, run Marx's table of falling rates and his two-million
illustration, measure how much of a fall a rising s′ or a cheapening of c
offsets, and compute the rate under absolute over-accumulation and after a
devaluation. Those are the acts the `standard` fields name and the quizzes
measure; no objective is "understand X". The `mistakes[0]` of every lesson is
the §C misconception, each refuted with a tile: `16%` against `21%` for the
capital with a quarter of the exploitation; `values £422 = prices £422` with
deviations summing to nought; the market value moving from `4 h` to `9/2 h`
and `7/2 h` while nothing about demand changes; `£120, £900/7, £816/7` for a
wage rise that leaves one price alone, raises one and lowers one; `s £110 =
profit £110` with the general rate down from `22%` to `21%`; the mass at
`£3,000,000` while the rate falls to `1/6`; `25/3 of 25/3 points`; `1/15` with
the mass fixed at `£100`.

The arithmetic is right throughout, including the four Kerr misprints the
author reports (Chapter 9's "8 + 18 + 26", Chapter 11's "16 1/12" and
"128 7/12" for 16 1/14 and 128 4/7 and "100 10/19" for 110 10/19, Chapter 13's
"66 1/3%"): each is a real misprint in the Kerr text, each is kept inside the
quotation and named outside it, and the lab prints the exact figure. All 26
pinned strings match the lab; every figure in prose agrees with the lab or
with a recomputation. The Chapter 9 presets agree with the page images in
every cell: used-up c 50, 51, 51, 40, 10; cost prices 70, 81, 91, 55, 15;
values 90, 111, 131, 70, 20; prices 92, 103, 113, 77, 37; deviations +2, −8,
−18, +7, +17; and the first table's values 120, 130, 140, 115, 105 summing to
610. (In the scan of the second table the digit 3 prints like an 8, so sphere
V's price reads "87" and sphere II's capital "70 c + 80 v"; the deviation
column, +17 on a value of 20, settles it as 37.)

Fidelity to the chapters is high and the later dispute is stated accurately
and at strength: Böhm-Bawerk (1896), Bortkiewicz (1906–07), Samuelson (1971)
and Steedman (1977) after Sraffa, the New Interpretation of Duménil and
Foley, the temporal single-system school, Marshall's scissors, Knight's
uncertainty, Robinson and Sweezy (1942), Okishio (1961), Shaikh, Luxemburg,
Baran and Sweezy, Keynes. No reply is put in Marx's mouth to anyone after
1883: every critic's paragraph ends with "what in the chapter bears on it",
in the chapter's words, which is the rule the Course 1 second review set. The
defects were local and are repaired below: one worked example that
misreported the size of Marx's Asian advantage, one phrase quoted as
Chapter 13's that is in Chapter 10, one claim pinned to "the end of Chapter
15" that the chapter's end does not make, one "the text does not reprint the
table" that should have cited the page the table is on, one quiz `why` whose
arithmetic was wrong, one sentence that gave the anonymous author of 1821
Marx's conclusion, and one read-intro that misread what Marx calls plain as
daylight. Nothing needs splitting, merging or reordering.

## The voice, judged against §F and Course 1

- **The passage first, then the phrases in order.** Every body opens with the
  `<strong>Volume III, Chapter n.</strong>` block. Lesson 1 returns to it ("Now
  read the sentence again. In 90c + 10v, ten pounds of wages employ ten
  workers"); lesson 4 ("Read the passage line by line. The labour bought is
  the same, so it still adds 40"); lesson 8 ("Read the passage line by line.
  Marx says that 'capital and its self-expansion' are the starting and closing
  point"). Lesson 2 opens with the claim about the totals and reaches the
  definition second, which the `read_intro` says it will do. This is Course
  1's shape.
- **Scenes only where the object is in the reader's life.** The power station
  and the cleaning company (lesson 1), the two apple growers (lesson 3), the
  wage rise in the news (lesson 4), the shipowner's insurance (lesson 5), the
  recession (lesson 8) each reach the chapter's category within the paragraph.
  Lessons 2, 6 and 7, whose objects are a table, a table and a list, open with
  the text, as §F rule 2 asks.
- **The history of the argument as story with people in it.** Carey "in
  Philadelphia" and Bastiat "in Paris", "the leading economists of harmony in
  the 1850s"; Böhm-Bawerk's 1896 title; Bortkiewicz who "took the procedure on
  its own terms"; Marshall, whose Principles "appeared in 1890, before Engels
  published this volume"; Smith's component parts against Ricardo's 1817
  reply; Knight's 1921 title; "the Japanese economist Nobuo Okishio"; Keynes
  "writing in 1936 with no reference to Marx's law". Each is given his ground
  before the chapter's bearing on him is stated.
- **Second person in `p` and `worked.intro` only.** "Think of two businesses
  you could put £100 into"; "You know this from any market stall"; "There is
  one sentence every reader should find before going further"; "You want its
  value, its price of production and the gap between them". `steps`,
  `standard`, quiz items and tile text stay impersonal. No "Let's", no
  anecdote.
- **Marx's own jokes before the lesson's.** "The common loot", "so many
  stockholders in a stock company", "a fight of hostile brothers" are quoted;
  the lesson adds none of its own. Lesson 5's "the stock company of Chapter 9
  with some shares weighted more heavily" is the one dry remark and it is
  Marx's image.
- **The limit admitted.** Every `note` names what the lab cannot settle, and
  they differ: inputs at value is "the step the transformation problem
  disputes"; the market lab "does not model his further point that a slight
  excess of demand lets the worst group's value regulate the price outright";
  the wage lab "knows nothing of money or of monetary policy"; the premium lab
  cannot test whether "the total is fixed in the way the chapter assumes";
  the law lab "holds s′ fixed, which is the step the standard objection
  disputes"; the counter lab "says nothing about the long run, which is where
  Marx and his critics disagree".
- **Pointing forward by title.** Each body ends by naming the next lesson's
  question by its title, and lesson 8 ends with Merchant's Capital and
  Interest and the merchant "who takes part in the general rate of profit
  without making any of the goods he sells".
- **Presented, not endorsed.** The course `how_to` says "No lab here takes a
  side", and the lessons keep to it. The closing move varies ("This Subject
  does not take a side", "Whether it reaches Marshall's is disputed", "this
  course does not decide it", "argued with data this course does not carry"),
  which is what the Course 1 assessment asked for.

## What the course teaches well

- **The objectives are acts and the drills measure them.** Every `standard`
  begins "Finish when you can…" and names the product and the judgement that
  goes with it: "state which differences in composition or in s′ account for
  the ranking" (lesson 1); "check that total price equals total value and
  total profit equals total surplus value" (lesson 2); "state which group's
  share pulls the market value toward its own value" (lesson 3); "classify
  each as rising, falling or unchanged" (lesson 4); "check that total profit
  still equals total surplus value" (lesson 5); "state how fast the capital
  must grow for the mass to stay the same or rise" (lesson 6); "the part of
  it offset" (lesson 7); "state the share that restores the old rate" (lesson
  8). The five course `outcomes` are the same acts.
- **One hard idea per lesson, in Marx's order.** Lesson 1 carries unequal
  rates at value and nothing of the equalisation; lesson 2 carries the
  equalisation and one paragraph on the dispute; lesson 3 carries market
  value within a sphere and only sketches the movement between spheres;
  lesson 4 is "mostly arithmetic" and says so; lesson 5 is three remarks and
  the lab computes one; lesson 6 keeps s′ fixed and names that as the step
  the next lesson relaxes; lesson 7 lets it move; lesson 8 adds capital and
  destroys it. The seam between the modules is at the end of Part II's
  arithmetic and the start of its coda, which is where Marx's own break falls.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset done by hand (Europe against Asia; sphere V; the
  worst-dominates mix; the three spheres after a 25% rise; a 5% premium for
  V; two million workers become three; the rising-s end point; Marx's 1,000
  and 1,500); every `panel_intro` asks for a comparison before the press
  ("Compare the europe-asia preset's rates of surplus value with its rates of
  profit"; "Compare each sphere's composition with the sign of its
  price − value"; "Watch the totals tile as the premiums change"); every quiz
  asks the same act on a fresh instance (70c + 30v; 60c + 40v with 51 used
  up; 2,000 at 2 h and 2,000 at 4 h; a 50% wage rise; a 10% premium; 300c +
  100v; 600c + 100v held at 20%; 2,000 growing to 2,500). The distractors are
  the named errors: `30/70` for s over c, `£122` for all of c used up, the
  plain 3 hours for a 2-and-4 mix, `1/10` for the rate on the old capital,
  `12%` for the premium subtracted from the rate, `25/3 of 10/3` for offset
  and fall reversed.
- **The misconceptions are the chapter's and are refuted with the figure.**
  Beyond the eight `mistakes[0]`: profit "on the cost price instead of the
  capital advanced" (V's 22% of 15 "would be 3.3; its profit is 22"); surplus
  profit "as cheating or as a mark-up" (the 3-hour group "sells at the same
  price as everyone"); "Reckoning the new rate on the old capital" ("15 on
  105, not 15 on 100"); "Taking the printed 128 7/12 as exact" ("a quotation
  is not a calculation"); "Thinking the chapter calls the allowances
  illegitimate" (Marx "already allots profit in proportion to turnover");
  "Thinking accumulation by itself lowers the rate" (the steady preset at
  `1/5` four times); "Reading a higher rate of exploitation as a lower rate
  of profit"; "Reading over-accumulation as too many goods for people's
  needs" with Marx's own denial quoted.
- **The transformation problem is handled as PLAN §D.3 and §G prescribe.**
  The lab does what Chapter 9 does, inputs at value; the lesson finds the
  sentence in which Marx grants "the possibility of an error" and quotes it;
  one paragraph names the controversy from Böhm-Bawerk to the temporal
  single-system school with dates and the direction each took; `mistakes[2]`
  is "Believing the lab has solved the transformation problem"; the course
  `not_covered` says why no solution is computed. Bortkiewicz's result is
  stated correctly ("in general only one of Marx's two totals survives") and
  the New Interpretation and TSSI are stated as replies ("read with different
  definitions, both totals hold"), not as refutations.
- **The falling rate is Marx's, with his two-sided claim kept whole.** Lesson
  6 gives the table, then spends its middle on the mass rising while the rate
  falls, with Marx's own rule ("the multiplier of the capital must equal the
  divisor of the rate") and his own counter-example ("100 at 25% make 25,
  while 400 at 5% make only 20"). Lesson 7's `teOffset` tile is the right
  quantity to compute for Chapter 14, and the lesson is careful that an
  offset of "25/3 of 25/3 points" over four periods "shows nothing about what
  happens over a longer run". Lesson 8 models the case Marx actually computes
  ("the mass of profits remaining the same") and the `note` now says so.
- **Okishio is stated as a theorem, with its premises.** "Suppose capitalists
  adopt a new technique only if it lowers their costs at current prices, and
  the real wage stays the same. Then… the rate of profit cannot fall, and it
  rises if the change touches goods that enter, directly or indirectly, into
  every other." Quiz 4 of lesson 7 tests the premise, not the conclusion. The
  replies (Shaikh on fixed capital; Kliman and Freeman on valuing inputs and
  outputs at the same prices) are each one sentence and attributed. The
  chapter's bearing is Marx's own premise in Chapter 15, that "No capitalist
  voluntarily introduces a new method of production… so long as it reduces
  the rate of profit", and the lesson says that premise is "close to
  Okishio's" without claiming Marx answered him.
- **The Kerr misprints are handled exactly as §C asks.** Each is quoted as
  printed, named as a misprint or a rounding in the body and in a `mistakes`
  entry where it matters, and the lab's exact figure is given beside it.
  Chapter 8's "rate of profit" for the Asian 25% is read as the rate of
  surplus value its own clause makes it, and the lesson says so in a
  parenthesis rather than correcting the quotation.
- **Cross-references are right.** Lessons by title (“The General Rate of
  Profit and Prices of Production”, “Market Value and Surplus Profit”, “Wage
  Changes and Prices of Production”, “Supplementary Remarks on Prices of
  Production”, “The Falling Rate of Profit: The Law as Such”, “Counteracting
  Influences”, “The Internal Contradictions of the Law”), each exactly as the
  lesson carries it; Marx's chapters by volume and number; the previous course
  by its §B title; the next course by its §B title. Lesson 1's turnover
  paragraph sends the reader back to Cost Price and the Rate of Profit for
  what that course computed.

## What it taught badly, or said wrongly

### Fidelity

- **`the-law-as-such`, body:** "The rate falls; and Marx says so 'in the long
  run'". The phrase is not in Chapter 13; the only "in the long run" between
  Chapters 13 and 15 is Chapter 10's, about the price of production as "a
  prerequisite of supply". What Chapter 13 says, in parenthesis after the
  table, is that the fall "does not manifest itself in an absolute form, but
  rather as a tendency toward a progressive fall." Repaired with that
  sentence.
- **`the-law-as-such`, body:** "Marx makes the same point at the end of
  Chapter 15: accumulation lowers the rate only when it changes the
  proportions of c and v." The end of Chapter 15 is the passage on the
  capitalist who refuses a method that lowers his rate; it does not say this.
  Chapter 13 does: "The fall of the rate of profit is not due to an absolute,
  but only to a relative decrease of the variable part of the total capital".
  Repaired with that sentence, cited to the chapter being read.
- **`the-law-as-such`, body:** the Robinson–Sweezy paragraph gave as the
  chapter's bearing only the "only within certain limits" of the mass of
  profit per commodity. The chapter has a sentence that bears more directly:
  "With the exception of a few cases… the rate of profit will fall in spite of
  the increased rate of surplus-value". Added.
- **`the-law-as-such`, body:** "66 2/3%, which is how the text writes it two
  pages later" — the table is on Kerr page 247 and the corrected figure on
  page 250. Now "a few pages later (Kerr page 250, against the table's 247)".
- **`the-general-rate-of-profit`, body:** "The text does not reprint the
  table, but it does print the deviations it produces". The plain text does
  not; the book does, on page 185, with the deviations as the table's last
  column, and the first table on page 183. The author wrote the presets from
  memory of the tables and the lesson should cite where they are. Repaired:
  the body names page 183 for the first table (with its values 120, 130, 140,
  115, 105) and page 185 for the two tables the `marx` preset reproduces; the
  `note` cites both pages; `__init__.py`'s `how_to[1]` cites them; the
  `part_a.py` docstring names the three image files; and the §C header for
  Course 10 in `docs/capital/PLAN.md` now says three tables, names the files
  and says the figures were read from them.
- **`internal-contradictions-of-the-law`, body:** "Marx ends the chapter on a
  different note" introduced the passage at Kerr l. 2553; the chapter runs
  to l. 2583. Now "Near the chapter's end Marx strikes a different note."
- **`market-value-and-surplus-profit`, body:** "He quotes an anonymous
  English writer of 1821 who admits that… and draws the conclusion that the
  price is fixed independently of them." As written, the writer draws the
  conclusion; in the text the Observations admits the two natural prices and
  Marx draws the conclusion. Now "and Marx draws the conclusion".
- **`different-compositions-different-rates`, `read_intro`:** "Marx states
  the difficulty in one sentence and then calls it as plain as daylight."
  What Marx calls plain as daylight is not the difficulty but the consequence
  of denying it: that value "must have an entirely different source than
  labor". Rewritten to say so.

### Arithmetic

- **`different-compositions-different-rates`, `worked.after`:** "The rate of
  profit is a fifth higher in Asia". 21 against 16 is 5/16, 31¼% higher; Marx
  writes "higher by more than 25%". Now "higher in Asia by more than a
  quarter, as Marx says (5 on 16)".
- **`internal-contradictions-of-the-law`, quiz 1, `why`:** "12.5% divides the
  old capital by the new" — 2,000/2,500 is 80%, not 12.5%, and no natural
  error gives 12.5%. The distractor is now 40%, the profit divided by the
  added 500 alone, and the `why` says so; the 2% distractor's explanation
  ("divides it by the old capital times five") is now right as well.

Every other figure was recomputed and stands: 85 5/7% and 14 2/7% for Marx's
A and B; 33 1/3% and 20% for copper and iron; 16% and 21%; 22%, 92, 103, 113,
77, 37, 422, 110; 122 five times, 610; 120 three times, 360; 4 h, 9/2 h, 7/2 h
with gains +1, 0, −1; +3/2, +1/2, −1/2; +1/2, −1/2, −3/2; 15/105 = 1/7;
112½ · 8/7 = 900/7 = 128 4/7; 102 · 8/7 = 816/7 = 116 4/7 (Marx's "14 4/7
(approximately)" on 102 is in fact exact); 25/95 = 5/19; 87½ · 24/19 =
2,100/19 = 110 10/19; 98 · 24/19 = 2,352/19 = 123 15/19; 860/7 + 820/7 = 240;
21% and 91, 102, 112, 76, 41; 20% and 100, 101, 111, 75, 35; 1/3 to 1/6 with 2
to 3 million; 1/4 held at 500c + 100v and 150%; 325, 350, 375, 400 under the
cheapening list 1/14, 1/15, 1/16, 1/17; 1/15, 1/10, 1/11; 7½ on 112½ = 6 2/3%;
140/700 = 1/5; 10/110 = 1/11.

### Prose, quiz and speech

- **`counteracting-influences`, `worked.after`:** "Whether s′ can keep rising
  enough is the question Marx answers no and Okishio's theorem answers
  differently." Okishio's theorem is not about s′ rising; it is about
  cost-reducing technical change at a constant real wage. Now "Whether the
  checks can hold the rate without limit is the question Marx answers no, in
  Chapter 15, and Okishio's theorem, on its own assumptions, answers
  differently."
- **`internal-contradictions-of-the-law`, `note`:** said the lab holds the
  mass of profit fixed "where Marx's text has wages rising until it does",
  without saying that the 1,000-to-1,500 example is Marx's own second
  alternative, "the mass of profits remaining the same". One clause added, so
  a reader does not take the lab's case for a simplification of Marx's.
- **Quiz distractors.** Every distractor on the course was argued for. Two
  are weak rather than wrong and were left: lesson 4's "1/6 is not any of the
  quantities" (a distractor that is nothing in particular teaches nothing,
  but it cannot be defended either) and lesson 3's "Because Marshall had
  shown it". Recorded below.
- **Speech.** All 65 math runs on the nine pages read correctly from
  `data-say`: `p prime equals s over the quantity c plus v`, `the sum of
  prices equals the sum of values`, `delta C adds no s`, `base rate equals the
  quantity the sum of s minus premiums, over the sum of C`, `25 over 3 of 25
  over 3 points`. No key line begins with a three-letter word; `at value` and
  `so the law` are read as words. Nothing needed a spoken form.

### What was checked and found right, against the Course 1 review's list

- Every phrase inside `&ldquo;…&rdquo;` is in the Kerr text: 84 segments,
  0 misses, after the changes (81 before). The six Chapter 14 headings match
  the text's.
- Every preset id appears in a body paragraph with its figure: `marx`,
  `copper`, `europe-asia`, `equal-composition`; `marx`, `all-used-up`, `three`;
  `average-dominates`, `worst-dominates`, `best-dominates`; `marx`,
  `two-spheres`, `fall`; `none`, `risk-premium`, `turnover-premium`; `marx`,
  `mass-rises`, `steady`; `rising-s`, `cheap-c`, `combined`; `marx`, `devalue`,
  `mild`.
- No verdict is given to Marx that the text does not contain. "Marx's
  verdict on the alternative is the sentence itself" (lesson 1) is the
  sentence quoted; "Marx says Carey and Bastiat would get backwards" is
  "would come to the opposite conclusion"; "Marx calls it secondary, and also
  the only relevant question Ricardo treated" is at l. 2052; "Marx mentions
  only empirically… and calls it one of the most important checks" is at
  l. 2312; "every capitalist has a direct interest in the exploitation of the
  whole working class" is at l. 1988.
- No reply is put in Marx's mouth to anyone after 1883. Böhm-Bawerk,
  Bortkiewicz, Marshall, Knight, Robinson, Sweezy, Okishio, Shaikh, Kliman,
  Freeman, Luxemburg, Baran and Keynes are each followed by "what in the
  chapter bears on it", or by a sentence that the course does not decide it.
- Critics are described in their own terms: Böhm-Bawerk's objection is about
  the totals as "an empty statement about a sum nobody trades", not about
  abstinence; Samuelson and Steedman's is that values are "a detour", not
  that they are wrong; Okishio's is a theorem with premises; Knight's profit
  is "the reward for bearing an uncertainty no insurance covers", not Senior's
  abstinence.
- The lesson's own voice praises no side. "Deserves its full strength", "the
  strongest modern objection", "the opposing view should be heard at full
  strength" are about hearing an objection, which §F asks for, not about who
  is right.

## Can a reader who has done Course 9 follow the eight lessons?

Yes. The places a reader slows are the places Marx's readers slow.

- **Lesson 1** is the easiest in the course and is correctly placed: it is
  Course 9's rate of profit applied to two capitals side by side, and its one
  surprise, the Asian capital, is given a worked example and a quiz item of
  its own. A reader who has not met Carey and Bastiat is told who they were.
- **Lesson 2** is where the course's load peaks, and the lesson manages it:
  the first table, the "not all cost-prices are equal to 100" turn, the
  second table, the definition, the smaller three-sphere table, the totals,
  and then the dispute, each with its preset. The paragraph on the dispute is
  one paragraph, as §D.3 prescribes, and the reader is sent to find "one
  sentence" in the chapter before it. A first-time reader will not follow
  Bortkiewicz; the lesson does not pretend he will, and `mistakes[2]` tells
  him exactly what the lab did not do.
- **Lesson 3** is the longest chapter in the Part and the lesson is honest
  about it ("it moves from one trade to the economy and back"). The three
  cases are given as presets with the same 10,000 pieces, so the reader sees
  that only the mix changed, and the "strictly speaking" reading is named as
  the lab's rule. The movement of capital between spheres is sketched, not
  computed, and the `not_covered` says so.
- **Lesson 4** is arithmetic and the lesson says so; the `def` gives the
  formula once and the worked example multiplies by 8/7 three times. A reader
  who stumbles on 14 2/7% is given "Adding the rate of 1/7 to a cost price is
  multiplying it by 8/7".
- **Lesson 5** is light, and correctly light after lesson 4. Its lab reuses
  the Chapter 9 spheres, so the only new input is the premium.
- **Lesson 6** is the second peak. The table is quoted misprint and all, the
  mass-against-rate distinction is given three ways (Marx's rule, his
  counter-example, the steady preset), and the standard objection arrives
  after the reader has done the arithmetic that the objection does not
  dispute, which is the right order.
- **Lesson 7** asks the reader to hold two sequences in mind at once; the
  `teOffset` tile does that for him, and the `def` says what the figure is.
  The four causes the lab does not compute are given a sentence each.
- **Lesson 8** is the easiest to compute and the hardest to read, and the
  lesson does the reading for him: production against realisation, the
  passage line by line, the thought experiment, the hostile brothers, the
  economists who deny overproduction, the critics, the closing passage.

## Repairs made in this pass

In `content/capital/c10_prices/__init__.py`: `how_to[1]`. In `part_a.py`: the
module docstring; `different-compositions-different-rates` `read_intro` and
`worked.after`; `the-general-rate-of-profit` the first-table paragraph, the
second-table paragraph and the `note`; `market-value-and-surplus-profit` the
Observations sentence. In `part_b.py`: `the-law-as-such` the misprint
sentence, the "in the long run" sentence, the steady-preset paragraph and the
Robinson–Sweezy paragraph; `counteracting-influences` `worked.after`;
`internal-contradictions-of-the-law` the closing-passage lead, quiz 1 and the
`note`. In `docs/capital/PLAN.md`: the Course 10 header paragraph of §C, which
now names the three table images and says the figures were read from them. No
preset, `expect`, slug, module, lab key, mode or view changed, and no §C
instance needed correcting: every instance the lessons carry is the one §C
records.

`python3 scripts/preview_subject.py capital --course
capital-prices-of-production` reports OK: 9 pages, every lab executes and
survives the sweep, all 8 lesson pages' pinned figures match, no math run
without a spoken form. The strict quotation checker reports 84 segments and 0
misses. Slugs, lesson count, modules, lab keys and modes are as PLAN §B and
§C list them.

## Recommendations not acted on

- **`wages-and-prices-of-production`, quiz 1:** the distractor "1/6" is
  explained as "not any of the quantities". A distractor that names an error
  teaches more; "3/20" (15 on the old 100, Marx's figure reckoned the wrong
  way) would do it, but it duplicates the error quiz item 1's `1/10`
  already names for the 50% case, so the choice is left to the author.
- **`market-value-and-surplus-profit`, quiz 4:** "Because Marshall had shown
  it" is a joke distractor; no reader will pick it, so the item is effectively
  three options. Harmless; recorded.
- **The closing "this course does not decide it" move** appears, in varied
  words, in lessons 2, 3, 6, 7 and 8. Each is in the lesson that takes the
  disputed step, which is the rule, and the words vary; but five in eight is
  near the limit of what a reader will not notice. Taste, not defect.
- **The `all-used-up` preset's label** ("Marx's five spheres, all c used up in
  the year") could name the page-183 table as the body now does; labels are
  pinned nowhere and the body carries the citation, so it was left.
- **`the-general-rate-of-profit`** tells the reader the New Interpretation and
  TSSI hold "both totals… read with different definitions". For the New
  Interpretation the equalities are of the net product and of profit at a
  monetary expression of labour-time; a reader who follows the reference will
  find the claim narrower than "both totals". One clause ("for the net
  product, with a monetary expression of labour-time") would make it exact at
  the cost of a term the course has not defined. Left for the second review.
- **The scan of the page-185 table** prints 3 as 8 in two cells; a note in
  `tables/README.md` would save the next reader the check. That file is
  outside this course's remit.
