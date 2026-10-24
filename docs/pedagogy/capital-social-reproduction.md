# Pedagogy assessment — Reproduction of the Social Capital (Capital, course 8)

Formed from the six lesson dicts in `content/capital/c08_reproduction/part_a.py`
(one each for Volume II, Chapters 18 and 19; two each for Chapters 20 and 21)
and the course dict in `__init__.py`, and the kit they render through
(`scripts/mathpath/labs/capkit_b.py`, mode `schemes` in views `sort`, `simple`,
`fixed`, `hoard` and `expanded`, and mode `revenue` in view `dogma`), on branch
`feat/capital-subject` before the Subject was wired. The design authority is
`docs/capital/PLAN.md` §0, §B, the Course 8 entries in §C, §E, §F and §G; the
kit as summarised in `docs/capital/kit-b-report.md`; the author's brief in
`docs/capital/AUTHORING.md`, whose two closing sections list the errors Course 1
made. `docs/pedagogy/capital-commodities-and-money.md` is the model for shape,
and Course 1 the voice reference.

Every lesson was read in full before anything was changed. Every pinned tile was
read off the rendered page with `node scripts/labcheck.js --observe` (rendered
through `scripts/preview_subject.py capital --course capital-social-reproduction`).
Every quoted span, sixty-nine of them, was searched for in
`/mnt/project-files/capital-texts/volume-2-kerr.txt` with the strict quotation
checker. Marx's reproduction schemes were recomputed in exact rational arithmetic
from the rule the lessons state, for the first illustration over four periods,
the second illustration over four, diagram b, and the `ii-short` case, and the
results compared with the Kerr text year by year, including the rounding Marx
announces in the fourth year and the two misprints discussed below. Every
`data-say` on the seven rendered pages was read. Lessons, in course order:
`the-object-of-the-inquiry`, `former-presentations`,
`simple-reproduction-the-three-exchanges`,
`simple-reproduction-fixed-capital-and-money`, `accumulation-and-money`,
`extended-reproduction`. The course is marked Advanced and assumes c, v, s and
the rate of surplus value from From Money to Surplus Value and the circuits
and turnover of the two earlier Volume II courses; it is judged against that.

## Verdict

The course teaches its subject. A reader who finishes it can sort a product list
into the two departments by use and total each, compute an annual product with
and without c and name the £6,000 Smith's account loses, test I(v + s) = IIc on a
two-department scheme and compute the three exchanges and the remainder when
the condition fails, compute the signed gap between Department II's renewals in
kind and the wear it hoards and name the short side while the value scheme
still balances, compute what is left unsold when Department I's hoarders and
investors do not match, and run Marx's enlarged scheme period by period,
computing Department II's forced accumulation and the growth of the product,
and say when Department II's surplus value is too small for the period to
balance. Those are the acts the `standard` fields name, the six course
`outcomes` repeat them, and the quizzes measure them on fresh instances. The
`mistakes[0]` of every lesson is the §C misconception and each is refuted with a
tile: `450` and `150` for coal filed as coal; `£3,000` against `£9,000`;
`+100` and `100 of Department I's product unsold`; `−100` with the balance tile
still at `I(v + s) = 2,000 = IIc`; `+500: 500 of surplus product unsold`;
`refused in period 1`.

The arithmetic is right, and the author's report of the text's figures is
right. All 36 pinned tile strings on the six pages match the lab. The exact
recomputation of Marx's first illustration gives 9,800, 10,780, 11,858 and
65,219/5 = 13,043⅘, against Marx's 9,800, 10,780, 11,858 and 13,033; the Kerr
total for Department II in the fourth year, 4,249, is indeed ten short of its
own parts 2,129 + 1,065 + 1,065, as the author says, and 13,033 = 8,784 + 4,249
carries the same slip, which the lesson now says, because rounding alone could
never move the figure by ten. The second illustration's first year is
16,250/3, 3,250/3, 4,750/3 and 947/3, which Marx rounds to 5,417, 1,083, 1,583
and 316 as the lesson says; Marx runs that illustration three years, and the
exact path agrees with his rounded capitals throughout except for one misprint
the author had not found: Kerr gives Department I's third-year constant capital
as 6,385 where 5,869 + 489 = 6,358, the figure Marx's own total 7,629 uses.
That is now in the lesson and in §C. Diagram b sums to 8,252 and closes at
1,750; the `ii-short` case needs 150 of Department II's 100 and is refused.

Fidelity is high. All sixty-nine quoted spans are in the Kerr text; none was
written from memory. The economists are stated at strength and in their own
terms: Quesnay with the seed that "does not circulate", Smith with his own
answer to the fourth-portion objection before Marx's reply, Say with his 1817
sentence and the Mac-Culloch joke pointed at as Marx's, Storch, Destutt de
Tracy, Proudhon; Sraffa's reduction to dated labour, the loanable-funds view,
Keynes, Tugan-Baranovsky, Luxemburg, Bauer and Bukharin are each given their
claim and their date, the lesson says in each case that they wrote after 1883,
and no reply is put in Marx's mouth to any of them: the lessons say what in
the chapter bears on the dispute and stop. Two paraphrases of Marx overreached
slightly and are repaired below; one `read_intro` placed the passage after the
wrong year. The remaining defects were in the read-out, where the department
notation was spoken as letters and a function and one display block was spoken
digit by digit; both are repaired. Nothing needs splitting, merging or
reordering.

## The voice, judged against §F and Course 1

**What matches the reference:**

- **The passage first, then its phrases in order.** Every body opens with the
  `<strong>Volume II, Chapter n, §m.</strong>` block and goes back through it:
  "Now read the passage phrase by phrase. First, 'the productive consumption'
  is production itself… The metamorphoses 'which promote it' are… Then comes
  the new item" (`the-object-of-the-inquiry`); "Read it slowly, because the two
  phrases sound alike. The annual product in values is… The value of the annual
  product also includes…" (`former-presentations`). The `read_intro` fields say
  which passage is coming and why, as Course 1's do.
- **Openings by the passage's own figures, not an invented scene.** §F rule 2
  names the reproduction schemes as the lessons that open with figures, and
  they do: the recapitulation of 9,000, the wear hoarded by Mr. X, capitalist
  A's hoard, the initial diagram. The one everyday opening, "Why save up at
  all? Because a new machine or a new mill comes in lumps"
  (`accumulation-and-money`), reaches the chapter's category in the same
  sentence. No scene is forced.
- **The history of ideas with people in it.** Quesnay is "a court physician
  who turned to economics in his sixties"; Smith "saw the objection and
  answered it"; Say's law is given "its full strength" with Ricardo and James
  Mill behind it; Tugan-Baranovsky "read these schemes in 1894 as proof that
  capitalism can expand without limit"; Luxemburg "asked who buys the growing
  product". Each opponent gets the fact his view rests on before Marx or the
  text answers.
- **Second person in `p` and `worked.intro` only.** "You want each exchange and
  the test of the condition"; "Here is the difficulty." `steps`, `standard`,
  quiz items and tile text are impersonal throughout; no "Let's", no "we", no
  first-person anecdote anywhere on the course.
- **Marx's own jokes before the lesson's.** "the Says and Mac-Cullochs", "200
  p. st. fall every year from the clouds", "the pleasure felt by some men"
  about loanable capital: each is Marx's and each is pointed at, not added to.
  "Marx is pleased with this" (lesson 4) is the one remark in the lesson's own
  voice, and the text supports it ("This illustration … is convincing").
- **The limit admitted.** Every `note` names the one thing the lab cannot show:
  "it cannot know who will buy the coal"; "it cannot settle whether Marx's
  division of value into c, v and s is the right one"; "the lab cannot show
  how, or whether, an unplanned economy comes to meet it"; "it does not model
  machines of different ages, credit or stocks"; "no credit, no interest rate
  and no Department II"; "whether Department II can be relied on to follow is
  what Luxemburg and others disputed". The move is varied, as the Course 1
  review asked.
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson by its exact title; `extended-reproduction` ends with the next
  course, Cost Price and the Rate of Profit, and its question.

**What differs from Course 1, and is right to:** the course is drier, because
the chapters are. Chapter 20 and 21 are arithmetic, and the lessons let the
arithmetic carry the prose rather than warming it. The `how_to` tells the
reader what kind of text Part III is (Engels' edit of manuscripts II and VIII,
"with fractions rounded off and the odd slip in a sum"), which is the right
preparation for a reader who will check Marx's sums and find one wrong.

## What the course teaches well

- **The objectives are acts.** Every `standard` begins "Finish when you can…"
  and names a computation and a classification: "sort a product list into the
  two departments by use"; "compute an annual product with and without c and
  name what Smith loses"; "check a two-department scheme for simple
  reproduction and compute its exchanges"; "compute the gap between renewals
  and wear hoarded and name the short side"; "compute what is left unsold when
  hoarders and investors do not balance"; "run a two-department scheme of
  accumulation and compute its growth".
- **One hard idea per lesson, and Chapters 20 and 21 split where §B says.**
  Lesson 3 carries the three exchanges and the condition and defers fixed
  capital explicitly ("treats all constant capital as used up within the
  year. The next lesson … lets the machines last"); lesson 4 carries only the
  wear-against-renewals gap and keeps the balance tile fixed to show that the
  value scheme is not the question; lesson 5 carries only the one-sided sales
  and purchases and leaves Department II to lesson 6; lesson 6 carries the
  rule and its consequences.
- **The misconceptions are refuted with the figure, and the second and third
  `mistakes` are the chapter's own.** "Reading Ic as somebody's income" with
  "more than two fifths of the annual product"; "Supposing the gap can run
  only one way" with the `bunched` preset; "Thinking the hoard is new wealth"
  with Marx's gold producer; "Reading Marx's rounded figures as exact" with
  13,043⅘ against 13,033.
- **Worked example, faded guidance, independent practice.** Every worked
  example is a preset by hand; every `panel_intro` asks for something to watch
  before the press ("Watch the balance tile stay where it is"; "Compare the
  two-dept and misclassified presets: one line changes, and only its use");
  every quiz asks the same act on a fresh instance (malt and beer; 220 against
  200 by Marx's count; 1,600 against 1,500). The distractors are the named
  errors: `9,000` for the dogma's total, "Department I 100 short" for the
  wrong sign, "It is absorbed in the exchange within Department I".
- **Every preset is in the prose with its figure.** The Course 1 rule holds on
  all six pages: `two-dept`, `misclassified`, `marx-totals`; `marx-scheme`,
  `one-firm`, `tableau`; `marx`, `too-much-in-i`, `too-little-in-i`,
  `diagram-b`; `balanced`, `short-renewals`, `bunched`, `marx-180`;
  `balanced`, `all-hoard`, `all-invest`; `marx`, `marx-second`, `ii-short`,
  each with the tile it shows.
- **The chapter's own figures are the chapter's.** The 6,000 and 3,000, the
  £1,500 that circulates £5,000, the 200 and 1,800, the 220 and 180 with
  "commodities valued at 40", A, A′, A″ and B, B′, B″, the 500 that leaves "an
  overproduction in department II", 8,252, 400c + 100v, 100c + 50v, 600 of
  750, 9,800, and the 1,583 and 316 of the second illustration are all where
  the lessons say they are.
- **Marx's opponents and later critics are kept apart from his replies.**
  Lesson 2 says "Marx wrote against Smith, not Sraffa"; lesson 5 says "The
  section does not name Say, but it bears on his law" and "The text here does
  not answer that view"; lesson 6 says "All of them wrote after Marx's death
  in 1883. What in the chapter bears on their dispute is the rule this lesson
  opened with… but the chapter does not show what makes it do so." That is
  the AUTHORING rule applied exactly.

## What it taught badly, or said wrongly

### Fidelity

- **`extended-reproduction`, `read_intro`:** "The passage is the rule he draws
  after the second year of it." Marx draws "If things are to proceed
  normally…" immediately after the first year's product of 9,800 and before
  he runs the second (Kerr l. 5284–5290). Now "after the first year of it,
  before he runs the second".
- **`simple-reproduction-the-three-exchanges`, body:** "Marx's own view,
  stated in the next chapter, is that in this mode of production such a
  balance comes about only by accident" generalised a remark Marx makes about
  the one-sided purchases and sales that money brings into reproduction
  (Kerr l. 5038) into a verdict on I(v + s) = IIc itself. Now names what the
  remark is about and quotes it: "a balance is an accident".
- **`former-presentations`, body:** value-creating labour "created only a
  third of their value" put the scheme's 3,000/9,000 into a sentence that
  paraphrases Chapter 19, which says only that the year's labour "did not
  create all the value" (Kerr l. 3842). Now "only part of their value: a third
  of it, in the scheme of Chapter 20".
- **`extended-reproduction`, body and `mistakes[2]`:** the lesson said Marx
  "rounds off fractions" in the fourth year and that Kerr's 4,249 is ten short
  of its parts, both true, but left a reader to suppose rounding explained
  the gap between 13,033 and 13,043⅘. Rounding four figures cannot move a sum
  by ten; 13,033 = 8,784 + 4,249 and carries the misprint. Both places now
  say so.
- **`extended-reproduction`, body:** Marx runs the second illustration for
  three years (Kerr l. 5412–5440) and Kerr prints "6385 c" for Department I's
  third-year constant capital where 5,869 + 489 = 6,358 and Marx's total 7,629
  confirms 6,358. A reader following the `marx-second` preset's table in the
  book would meet that figure. One sentence added, and the §C entry for the
  preset records it.

### Prose that left the lab unexplained

- **`accumulation-and-money`, `note`:** the `all-invest` preset prints "−500:
  500 of demand without a product" although Marx's Department I has 500 of
  surplus product for accumulation on the page; the kit counts only the two
  one-sided acts against each other, so money hoarded in earlier years meets
  no one-sided seller this year. Nothing on the page said that in words. One
  sentence added to the `note`.

### Speech

Every math run on the seven rendered pages was read from `data-say`. Two
shapes were wrong, and the task's own list named both.

- **Marx's department notation.** `I(v + s)` was read "I of the quantity v
  plus s", `IIc` as "IIc" or "I I c", and a key line beginning `I 4000c + …`
  as the letter I. Thirty-nine spoken forms are added to
  `content/spoken/capital.py` in a block headed `# Reproduction of the Social
  Capital`, reading the departments as "Department one" and "Department two"
  and `I(v + s)` as "Department one's v plus s", matching the forms the
  Revenues course already uses for its own runs; none duplicates a key in
  another block.
- **A trailing apostrophe read as a prime.** The key line `hoarders' sales −
  investors' buys` was read "hoarders prime sales minus investors prime
  buys". Given a spoken form.
- **A display block spoken digit by digit.** The two `("math", "I.  4000c +
  …")` blocks in `extended-reproduction` passed a string where the renderer's
  `_mathblock` expects a list of lines, so each character was treated as a
  line and the `data-say` read "I. 4. 0. 0. 0. c. 1. 0. 0. 0…". Now one
  `("math", [line, line])` block, spoken "Department one, 4000 c plus 1000 v
  plus 1000 s equals 6000. Department two, …". The same string form is used
  in `c02_surplus_value/part_b.py` (lines 1070–1071) and
  `c14_revenues/part_a.py` (lines 377–378) and will read the same way there;
  those are other courses and are recorded under remaining issues.

Grouped numbers never appear inside a math run on this course: the module
docstring says runs keep thousands ungrouped (`4000c`) so the read-out does not
split them, and every run was checked. The prose groups them (4,000c + 1,000v),
which is the Subject's convention and is not read by the engine.

### Quiz

Every distractor on the course was argued for. None could be defended: `9,000`
for Smith's total is Marx's answer, `6,000` is the c the dogma loses; "Both in
Department I, because both were made in factories" is the mistake the lesson
names; "Department II buys it and expands its constant capital" is ruled out
by simple reproduction in the stem; "The scheme no longer satisfies I(v + s) =
IIc" is what the fixed-capital lesson exists to deny; "Saving always exceeds
investment" contradicts Say; `150` is Department II's whole accumulation, not
its added c. No change.

## Cross-references

Lessons are cited by title (“The Object of the Inquiry”, “Former Discussions:
Quesnay and Smith”, “Simple Reproduction: The Three Great Exchanges”, “Simple
Reproduction: Fixed Capital and Money”, “Accumulation in Department I and the
Money It Needs”, “Reproduction on an Enlarged Scale”, “The Twofold Character
of Labour”, The Circuits of Capital), each as the lesson or course carries it;
Marx's chapters by volume and number, as §0's first deviation requires; the
next course by its §B title. The spinner's £372 + £50 + £78 in lesson 2 is the
instance The Circuits of Capital uses. The modules carry Kerr's chapter
titles, "Former Discussions of the Subject" and "Accumulation and Reproduction
on an Enlarged Scale", as §C requires.

## Can a reader who has done the Volume I courses follow the six lessons?

Yes, and the places where a reader will slow are the places Marx's readers
slow.

- **Lesson 1** has the least to compute and says so ("mostly a statement of
  the problem"). Borrowing the two departments from Chapter 20 so that
  Chapter 18 has a sort to do is honest about the borrowing in the `note`, and
  the coal that goes to a mill and a kitchen is exactly the right first
  example, because it makes "by use, not by what the thing is" a fact about
  one colliery's invoice.
- **Lesson 2** is the history lesson and reads as one. The horse paragraph is
  the best in the course: Smith's own answer, then Marx's "He refers us from
  one line of production to another", then Sraffa's stronger version of
  Smith's reply, then the one thing in the chapter that bears on it. A reader
  meets "the annual product in values" against "the value of the annual
  product" with the warning that the two phrases sound alike.
- **Lesson 3** is where the course's real work starts, and it is paced for
  it: the scheme, then the three exchanges one paragraph each, then the
  condition as a quotation, then the money put back in, then the lab, then
  the connection back to Smith. The seam to lesson 4 is explicit.
- **Lesson 4** is the hardest chapter in Part III and the lesson protects the
  reader by keeping the balance tile fixed in every preset, so the one thing
  that moves is the one thing the section is about. Section 1 and section 2
  are Marx's labels and are used as he uses them.
- **Lesson 5** is the lightest and correctly so; its work is the Say's-law
  paragraph, which is given at strength, and the honest sentence that the
  text sets credit aside.
- **Lesson 6** asks the most and gives the most help: Marx's first year in
  prose, in `steps`, in the worked example and in the quiz, all with the same
  figures, and the growth path as something the reader can check against
  Marx's own 9,800, 10,780, 11,858. The Luxemburg paragraph tells the reader
  exactly which step of the lab's rule is the disputed one.

## Repairs made in this pass

In `content/capital/c08_reproduction/part_a.py`: `former-presentations` the
"first mistake" paragraph; `simple-reproduction-the-three-exchanges` the
standard-objection paragraph; `accumulation-and-money` the `note`;
`extended-reproduction` the `read_intro`, the two `math` blocks (now one list),
the 13,033 paragraph, the `marx-second` paragraph (the three years and the
6,385 misprint) and `mistakes[2]`. In `content/spoken/capital.py`: a new block
`# Reproduction of the Social Capital` of thirty-nine spoken forms; no other
block touched. In `docs/capital/PLAN.md`: the `marx-second` instance in
Course 8's lesson 6 entry records the 6,385 misprint. No preset, `expect`,
slug, module, lab key, mode, view or instance changed, so no other §C entry
needed correcting.

`scripts/preview_subject.py capital --course capital-social-reproduction`
reports OK: 7 pages, every lab executes and survives the sweep, all 36 pinned
figures on the six pages match, no math run without a spoken form; the strict
quotation checker finds 69 segments and 0 misses; `tests/test_speech.py`
passes.

## Remaining issues

- **`("math", "<string>")` in two other courses.** `_mathblock` in
  `scripts/mathpath/render.py` iterates its payload as lines, so a bare string
  is spoken one character at a time. `content/capital/c02_surplus_value/part_b.py`
  lines 1070–1071 and `content/capital/c14_revenues/part_a.py` lines 377–378
  have the same shape this course had and will read the same way; their
  authors should wrap the lines in a list. A one-line guard in the renderer
  (`if isinstance(lines, str): lines = [lines]`) would close the hole for
  good; that belongs to the chrome-renderer tier and was not made.
- **The `hoard` view's `all-invest` case is a stylised reading of §1.** The
  kit scores the two one-sided acts against each other and prints "500 of
  demand without a product" when no capitalist is hoarding, although Marx's
  Department I has 500 of surplus product for accumulation. The `note` now
  says what the tile counts; a tile label such as "hoarders' one-sided sales
  less investors' one-sided purchases" would make it unnecessary, and is a kit
  change.
- **The second illustration's growth tile runs a period Marx does not.** Marx
  gives capitals after three rounds of accumulation; the lab's four periods go
  one further, so `9,000 to 2,690,893/216: … 38.42%` is the lab's extension of
  Marx's rule, not a figure in the text. The lesson pins it as the lab's and
  says the table agrees with Marx's rounded figures where he gives them; a
  reader will not mistake it for Marx's, and the preset is kept.
- **Lesson 1's objective ends in a "say why".** The `standard` asks the reader
  to "state why a single firm's circuit can leave this question to the market
  and society's capital cannot", which §C's Do line also asks. It is a
  justification rather than a computation, and the quiz measures it with one
  item. Acceptable for an introduction whose chapter computes nothing; recorded
  because §C's own rule prefers the act.
- **The speech engine's department notation.** `I(v + s)` and `IIc` are now
  spoken through overrides on this course and on Revenues and Their Sources;
  every later run of the notation on either course, or on Average Profit and
  Its Fall where the schemes return, needs its own entry. A `speech.py` rule
  for Roman-numeral department prefixes would retire the entries; that is
  chrome-renderer work.
