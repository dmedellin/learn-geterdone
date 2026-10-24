# Pedagogy assessment — Revenues and Their Sources (Capital, course 14)

Formed from the five lesson dicts in `content/capital/c14_revenues/part_a.py`
(one per chapter of Volume III, Part VII, Chapters 48–52) and the course dict
in `__init__.py`, and the kit they render through (`scripts/mathpath/labs/
capkit_b.py`, mode `revenue` in views `trinity`, `added-up` and `classes`, and
mode `schemes` in view `simple`), on branch `feat/capital-subject` before the
Subject was wired into the site. The design authority is `docs/capital/PLAN.md`
§0, §B, the Course 14 entries in §C, §D as summarised in
`docs/capital/kit-b-report.md`, §E (quotation), §F (voice) and §G (what is left
out); the author's brief is `docs/capital/AUTHORING.md`, whose closing sections
list the errors earlier courses made. This is the last course of the Subject,
so two questions are judged that no other course carries: whether it closes
the three-volume argument without inventing a conclusion Marx did not write,
and whether the last lesson ends where the manuscript does.

Every lesson was read in full before anything was changed, and so were the
five chapters, whole, in `/mnt/project-files/capital-texts/volume-3-kerr.txt`
(l. 6918–7420 with footnotes 144–155), and the table image for Kerr p. 996.
Every pinned tile was read off the rendered pages with `node scripts/labcheck.js
--observe` (rendered through `scripts/preview_subject.py capital --course
capital-revenues-and-their-sources`); every figure in prose was recomputed by
hand, including Marx's two rate tables in Chapter 50; every quotation and every
phrase in `&ldquo;…&rdquo;` (fifty-one spans) was checked against the Kerr text
with the strict quotation checker; and every math run on the six rendered pages
was read from its `data-say`. Lessons, in course order: `the-trinity-formula`,
`analysis-of-the-process-of-production`, `illusions-created-by-competition`,
`distribution-and-production-relations`, `classes`. The course assumes the
thirteen before it, above all the reproduction scheme of Reproduction of the
Social Capital, the split of profit in Merchant's Capital and Interest and the
rent of Ground Rent, and is judged against that.

## Verdict

The course teaches its subject and closes the Subject well. A reader who
finishes it can resolve a value product into wages, rent, interest and profit
of enterprise from c, v, s and two shares and show the four return v + s
whatever the shares; separate a year's product from a year's income on Marx's
9,000 and name the 4,000 that is nobody's revenue; divide a fixed value product
after a wage rise and say what adding the parts up would wrongly give; divide
the same £200 under three relations of production and say which features are
common to all three; and apply the source-of-revenue test to a list of people,
recount as the sources are made finer, and state the objection with which the
manuscript stops. Those are the acts the `standard` fields name and the quizzes
measure, and no objective is "understand X". Every `mistakes[0]` is the §C
misconception, each refuted with a tile: rent `£0` and profit of enterprise
`£80` with the sum still £200; the `4,000` within Department I against 9,000
of product and 3,000 of income; wages `£150` and the product still 650; profit
of enterprise `£0` in the co-operative with rent and interest unchanged; `3
groups`, then `5`, then `7`. All 46 pinned tile strings on the five pages
matched the lab, and every figure in prose agreed with the lab or with a
recomputation.

Fidelity to the five chapters is high. Fifty of the fifty-one quoted spans were
found verbatim in the Kerr text; the one the checker misses is the opening
word of the first quotation, which the Kerr text prints as a drop capital
(`CAPITAL—Profit`) and the module docstring says it prints as an ordinary
capital. Every sentence beginning "Marx says", "Marx argues" or "Marx's reply"
was traced to a line in the chapter; the one that went beyond the text (Marx
"credits the classical economists, Smith and above all Ricardo", where the
text says "classic economy" and names nobody) is repaired below. The critics
and the later positions are stated accurately and at strength: Say's three
productive services; Clark's marginal product and Wicksteed's 1894 result on
product exhaustion; Robinson and Sraffa on measuring capital and Samuelson's
1966 concession; Smith's natural price and the horse of footnote 148; Ricardo's
"Take a whole from a whole and nothing remains"; Leontief and Quesnay; Mill's
production-as-physics and distribution-as-institution; Mises, Lange and Hayek;
Lenin and Weber. None is answered in Marx's name; each is followed by what in
the chapter bears on it, in the chapter's words, and the lessons say three
times, in different words, that the arithmetic does not decide. The course does
not invent a conclusion for the book: `classes` recaps the three volumes as a
route, not a result, says that every step of it is contested and where, and
ends with the manuscript's last sentence, "owners of vineyards, farms, forests,
mines, fisheries."

The defects were local and are repaired below: a `math` block in lesson 2 that
rendered Marx's scheme one character per line and was read aloud as "I. 4. 0.
0. 0. c."; the overstatement about Smith and Ricardo; a misprinted table the
lesson cited without saying it was misprinted; a quiz distractor whose
explanation missed that 700 is also Marx's own figure; and a quiz answer and a
`note` in `classes` that said the relation to the means of production is
"not in the text", when the chapter's first sentence names the three classes
by exactly what their members own and only declines to say that this is what
constitutes a class. Nothing needs splitting, merging or reordering.

## Does the course close the Subject?

Yes, and in the right way. The three things a closing course has to do are
done, and the one thing it must not do is not done.

- **It gives the reader the shape of the whole.** The seventh body paragraph
  of `classes` ("Step back and see where the book has brought you") runs from
  the single commodity through the working day, the circuits and the two
  departments to profit, prices of production, interest and rent, and says
  what Part VII does with them: "puts the pieces back on the surface, where
  each looks like the fruit of its own source, and asks who lives on them."
  That is a structural summary of a route, and every clause of it is a lesson
  the reader has done. §F rule 7 forbids summarising the lesson; it does not
  forbid, at the end of fourteen courses, naming the road.
- **It says what is contested, and refuses the verdict.** The next paragraph
  names the labour theory against marginal utility, the transformation problem
  since Bortkiewicz, and the falling rate's record as "a matter of data", and
  then says what the lab did instead: "computed, from the same c, v and s,
  what follows on Marx's definitions." The course `how_to[3]` and the
  `footer_lead` make the same separation of accounting from verdict. That is
  §F's "presented, not endorsed" carried to the last page.
- **It ends where the manuscript does.** "Here the manuscript ends. These are
  its last words:" and then the quotation, to "fisheries." Nothing follows in
  the body. The `read_intro` says the passage is "most of" the chapter and the
  rest "is read at the end, where the manuscript ends". The `how_to` says
  Chapter 52 "stops after a page", and PLAN §C's observation that the Kerr
  text has no editorial "breaks off" note is respected: the lesson claims
  none. The quiz's last item asks what the chapter concludes and keys
  "Nothing: the manuscript breaks off after the objection", and the third
  `mistakes` entry is "Supplying the chapter's answer".
- **It does not invent a conclusion.** Lenin's and Weber's answers are in the
  `note` and `not_covered`, named and not argued; the lesson's own strongest
  sentence about Marx's intention is "Whatever answer Marx had in mind, it had
  to be something other than the source of revenue alone", which is exactly
  what the chapter's objection licenses and no more. The one place the course
  stepped past this, by saying the ownership answer is "not in the text", is
  corrected below so that the chapter's first sentence is given its due.

## The voice, judged against §F and Course 1

The register is Course 1's. What the model course does, this one does:

- **The passage first, then its phrases in order.** "Go back to the passage.
  In the first version capital yields profit… Then the formula shrinks"
  (lesson 1); "Read it the way the chapter does. Department II's workers…"
  (lesson 2); "Marx's reply goes through the passage" (lesson 4). The
  `read_intro` fields say where the passage sits in the chapter, and lesson 3's
  says honestly that the passage is "from its middle" and the example "comes
  earlier".
- **Scenes only where the object is in the reader's life.** "A wage is paid
  for work. Money in a savings account earns interest… A flat let to a tenant
  earns rent" (lesson 1); the national income figure "every year" (lesson 2);
  "Wages go up, so the firm's costs go up, so prices go up" (lesson 3);
  "the minimum wage, taxes on income and inheritance, rent controls" (lesson
  4). `classes` opens with the manuscript instead, which is what §F rule 2
  asks when a scene would have to be invented.
- **The history of an idea with people in it.** Say "whose Treatise of 1803
  made Smith's ideas a system"; Roscher "whom Marx names"; Clark in 1899 and
  Wicksteed in 1894; Robinson and Sraffa "at Cambridge"; Leontief naming
  Quesnay; Mill drawing "a programme of reform" from his distinction; Mises,
  Lange and Hayek in three sentences; "a professor" is not here because none
  travels to Manchester in these chapters. Each is given his claim before Marx
  or the lesson answers.
- **Second person in `p` and `worked.intro` only.** "You want the four
  revenues and their sum"; `steps`, `standard`, quiz items and tile text stay
  impersonal. No "Let's", no "dive in", no first-person anecdote anywhere.
- **Marx's jokes before the lesson's.** "Mister Capital and Mistress Land" is
  pointed at ("Marx is enjoying himself, and he means it"); "competition has
  to shoulder the duty of explaining all inexplicable ideas of the economists"
  is "at his most sardonic". No joke of the lesson's own.
- **The limit admitted.** Every `note` names what the lab cannot decide: the
  marginal-productivity reading of the same four figures; the simple scheme's
  omissions; productivity and paper money; who decides, "which is the
  difference the chapter cares about"; what makes a class.
- **Pointing forward by title**, and the last lesson pointing nowhere, as §F
  rule 7 requires of “Classes” by name.

What Course 1's reviewers asked later authors to change, this author did:
every preset id is explained in a body paragraph with its figure (the
`one-sector`, `growing`, `rent-rise`, `fixed-value`, `cooperative` and
`landowners-split` presets each get a sentence); "This Subject does not settle
it" appears once, in lesson 1, and lessons 3 to 5 vary the move; no key line
begins with a three-letter word; `cwt.` does not occur; the standard objection
is named in the lesson it concerns (Clark in lesson 1, Sraffa in lesson 3,
Mises in lesson 4), not only the first time.

## What the course teaches well

- **The objectives are acts, and the closing drill measures them.** "Finish
  when you can resolve a value product into the four revenues"; "…separate a
  year's product from a year's income"; "…divide a fixed value product after a
  change in one of its parts"; "…divide one value product under different
  relations of production"; "…apply the source-of-revenue test and state what
  the chapter says about it." The five course `outcomes` are the same five
  acts, and `outcomes_intro` says the one thing they add up to: "say, in
  figures, which part of which value product it is."
- **One hard idea per lesson, in the chapter's order.** Lesson 1 carries the
  formula and nothing of the product–income gap; lesson 2 carries the gap and
  Volume II's answer and does not touch the adding-up theory; lesson 3 carries
  the adding-up theory and its circularity; lesson 4 the reverse-side thesis;
  lesson 5 the test and its failure. Lesson 3 is the heaviest, because
  Chapter 50 is, and it is paced: Marx's example and his rates, then the lab,
  then the exceptions (productivity, dear food, prices of production), then the
  circle, then the 125, then the five reasons the illusion is necessary.
- **The arithmetic is right, and the slip in Kerr is real.** On 400c + 100v +
  150s = 650: wages 20 per cent of 500, s 30 per cent, 4 and 6 hours of 10.
  After the rise, 150/550 = 3/11 = 27 3/11 per cent, where the Kerr text
  prints 27 8/11; 45/550 = 8 2/11, 55/550 = 10, 100/550 = 18 2/11 per cent;
  s/v falls from 150 to 66 2/3 per cent and the rate of profit from 30 to
  18 2/11; the rate of profit falls by more than a third (39.4 per cent) and
  less than the rate of surplus value (55.6 per cent), as Marx says. The 125
  example: 100 + 10 + 15, shares 4/5, 2/25, 3/25; at 110 wages, 11 and 16½
  make 137½. The scheme: 9,000; 3,000 of revenue; 2,000 each way; 4,000
  within Department I; `growing` gives I(v + s) 2,000 against IIc 1,500 and
  the 500 Volume II accumulates, and the Volume II figures (vol. 2 l. 5210–
  5214) are as the lesson says. The co-operative: 3/5 and 2/5 of 50 are 30 and
  20, and 150 + 30 + 20 + 0 = 200.
- **The misconceptions are refuted with the specific figure, and held at
  their holders' strength first.** "This is Say's three productive services
  and, in its modern form, Clark's marginal productivity, and on those
  accounts it is no mistake" (lesson 1); "Smith's argument… makes it seem so,
  and Say drew the conclusion" (lesson 2); "It is Smith's natural price and
  every business's costing, and for one firm facing given wages it describes
  what it sees" (lesson 3); "This is Mill's position, and reforms of
  distribution are real" (lesson 4); "It is the answer Marx tries first,
  because the trinity formula suggests it" (lesson 5). Then the tile.
- **The chapter's broken text is handled as text.** Lesson 1 says the chapter
  is three fragments, where the folio is missing and where the manuscript
  "stops short", and (now) that the last sentence is unfinished; lesson 3
  reports the 27 8/11 and the garbled table on p. 996; lesson 5 says the
  chapter is a page long and ends with it. A reader with the Kerr edition open
  will find what the lessons say he will find.
- **The lab's names are not passed off as Marx's categories.** Lesson 4's
  `panel_intro` says the tile names "are those of a capitalist economy; in the
  association preset read the wages tile as the producers' consumption and the
  profit of enterprise tile as the common fund", and the body says those are
  "the wrong names, and that is the chapter's point". Lesson 3's note says the
  equal split of the reduced s "is a simplification of his 45 and 55". This
  is the kit's limit stated where the lesson leans on it, which §F rule 6
  asks for.
- **Worked example, faded guidance, independent practice.** Each `worked` is
  the first or the illustrative preset by hand; each `panel_intro` asks for a
  comparison before the press ("add the four revenue tiles each time";
  "Compare that tile with the whole product in the status line"); each quiz
  asks the same act on the chapter's own instance (Marx's 650; the 125; the
  physician and the official). Distractors are the named errors: £70 for "s
  after rent", 700 for "the wage rise on top", 9,000 for "Say's figure for
  income", `3/2` for "the rate before the rise".
- **Cross-references are by title and exist.** “Wage Changes and Prices of
  Production” is Course 10's Chapter 11 lesson; “The Trinity Formula” and
  “Classes” are this course's; Marx's chapters are cited by volume and number,
  as §0's first deviation requires; the schemes lesson points at Volume II,
  Chapters 20 and 21, where the figures are.

## What it taught badly, or said wrongly

### Rendering and speech

- **`analysis-of-the-process-of-production`, body:** Marx's two scheme lines
  were written as two `math` blocks each holding a bare string. The block
  renderer iterates its payload, so each line rendered one character per line
  on the page (`I`, `:`, ` `, `4`, `0`, `0`, `0`, `c`…) and was read aloud as
  "I. 4. 0. 0. 0. c. 1. 0. 0. 0. v…". Course 8 writes the same scheme as one
  block holding a list. Repaired to one block holding both lines; the page now
  shows the scheme as two lines and reads "I, 4000 c plus 1000 v plus 1000 s
  equals 6000. II, 2000 c plus 500 v plus 500 s equals 3000". The preview's
  own checks did not flag it, since every character is a word a voice can say;
  later authors should know that a `math` payload is a list of lines, never a
  string.

### Fidelity

- **`the-trinity-formula`, body:** "He credits the classical economists,
  Smith and above all Ricardo, with having seen through this". The passage
  (l. 7030) says "It is the great merit of classic economy to have dissolved
  this false appearance" and names no one; "above all Ricardo" was the
  lesson's. Now "He credits what he calls classic economy, the school of
  Smith and Ricardo".
- **`the-trinity-formula`, body:** Smith's sentence on the "three original
  sources" is in footnote 146, not the text; "in a sentence Marx quotes" is
  now "in a sentence Marx quotes in a footnote". The same paragraph said the
  Kerr text marks a missing folio and a place where the manuscript stops
  short, which it does; it did not say that the chapter's last sentence
  ("Only when the capitalist mode of production…") is also unfinished. One
  clause added.
- **`illusions-created-by-competition`, body:** the lesson cited the table on
  Kerr p. 996 for the 650 and 250 without saying that the table's rate
  columns are misprinted (the image reads 80 per cent for the first rate of
  gross profit and 66 1/8 for the second rate of surplus value, where the
  text has 30 and 66 2/3). A reader sent to the page would meet two numbers
  the lesson had just told him were 30 and 66 2/3. Now says so, in words a
  voice reads ("sixty-six and one eighth"; a backticked `66 1/8` was read "66
  1 over 8"). PLAN §C's text note already recorded the misprint; the lesson
  and the plan now agree.
- **`classes`, quiz 4 `why` and `note`:** both said the relation to the means
  of production is "a later reader's answer, not the chapter's" and "Neither
  is in the text". The chapter's first sentence defines the three classes as
  "The owners of mere labor-power, the owners of capital, and the landlords",
  and its third paragraph says the tendency of capitalist production is to
  turn "labor into wage labor and the means of production into capital". What
  is not in the text is the claim that ownership is what *constitutes* a
  class. Both now say that: the chapter names the classes by what their
  members own and does not say whether that is what makes them classes.

### Quiz

- **`illusions-created-by-competition`, quiz 1, distractor 700:** the `why`
  said only that 700 "adds the wage rise on top". It is also Marx's own figure
  for 450c + 100v + 150s (l. 7222), the case of dearer means of production
  with wages unchanged, and a reader who had just read that paragraph could
  argue the distractor was in the chapter. Now says both. Every other
  distractor on the course was argued for and could not be defended: £70, the
  "£230" of a rent added on top, "Ground-rent" for "happily eliminated", the
  average product, 2,000 and 6,000 for the 4,000, "Department II buys it as
  consumer goods" for the 500, `3/2` and `2/11`, "dearer bread" for a change in
  the yarn's value, £200 for the co-operative's pay, "both historical" for
  Mill, 5 for the three groups, and "houses, shops and factories" for Marx's
  list.

## Can a reader who has done the thirteen courses follow the five lessons?

Yes, and the places he slows down are the places Marx's readers slow down.

- **Lesson 1** moves from three familiar incomes to the formula, explains
  "happily eliminated" in the formula's own terms (profit "still points back
  to the factory"), and gives the marginal-productivity account two full
  paragraphs before the lab, so a reader forming the objection "but land and
  machines are productive" is told at once that serious people hold it and
  how. The lab is then shown doing exactly one thing, moving shares under a
  fixed sum, and the paragraph after it says a marginalist "would read the
  same tiles differently". That is the honest shape of the chapter.
- **Lesson 2** is the one that leans on an earlier course, and it leans
  correctly: the scheme is Course 8's with Marx's own figures, the `growing`
  preset is Course 8's accumulation diagram, and the lesson re-reads both for
  what they say about income rather than reteaching them. A reader who skipped
  Reproduction of the Social Capital will need its third lesson; the
  `assumes_long` says so.
- **Lesson 3** is the hardest and the lesson says why: the appearance "is not
  a mistake anyone makes by carelessness". Marx's example is done once by
  hand with every rate, the slip is reported, and only then do the
  illustrative presets appear, so the reader meets the chapter's own numbers
  first. The 125 example is the one place a reader may lose the thread, since
  it is the adding-up theory's arithmetic and not Marx's; the lesson frames
  it as "He adds a small sum to show where the additions really come from",
  which is enough.
- **Lesson 4** asks the reader to accept a kit that has only capitalist names
  and to read them against the grain in the `association` preset. The
  `panel_intro`, the body and `mistakes[2]` all say so, and the chapter's
  small farmer who pays himself wages, profit and rent is used to show that
  this mislabelling is the chapter's own subject. That turns a kit limit into
  the lesson's point, which is the best that could be done without a new
  view.
- **Lesson 5** is short because the chapter is, and the lab is a counting
  exercise because the chapter's test is. The recap paragraph and the
  contested-steps paragraph come before the last words, not after, so the
  page ends on Marx and not on the course.

## Repairs made in this pass

In `content/capital/c14_revenues/part_a.py`: `the-trinity-formula` the
fragments paragraph (unfinished last sentence), the Smith paragraph (footnote),
the classic-economy sentence; `analysis-of-the-process-of-production` the
scheme `math` block (two strings to one list); `illusions-created-by-competition`
the table sentence and quiz 1 `why`; `classes` quiz 4 `why` and `note`. No
preset, `expect`, slug, module, lab key, mode or view changed, and no §C entry
needed correcting: every instance the lessons carry is the one §C records, the
`wage-rise` preset's departure from Marx's 45 and 55 is the one §C specifies,
and §C's text note on the p. 996 table is what the lesson now says.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-revenues-and-their-sources` reports OK: 6 pages, every lab executes and
survives the sweep, every pinned figure on the five pages matches, no math run
without a spoken form; a second pass over every `data-say` on the six pages
finds no spelled-out word and no character-by-character block. The strict
quotation checker reports 51 segments and 1 miss, the drop capital.

## Remaining issues

- **A `math` block with a string payload renders and reads one character
  per line, and nothing catches it.** The preview passed because every
  character is sayable. A check in the content renderer (reject a `math`
  payload that is not a list, or wrap a string in one) belongs to the
  chrome-renderer tier and was not made here. Other courses should be grepped
  for `("math", "` before wiring.
- **Mixed numbers in backticks read as "66 1 over 8".** `66 2/3` has a spoken
  form somewhere upstream and reads "66 and 2 thirds"; `27 3/11` and `18 2/11`
  read "27 and 3 elevenths", "18 and 2 elevenths"; `66 1/8` did not. The
  mixed-number rule in `speech.py` seems to cover some denominators and not
  others. Worked around in words here; the rule belongs to chrome-renderer.
- **Lesson 4's `cooperative` preset reaches its figures through shares of s
  that are chosen to fit** (3/5 and 2/5 of a surplus of 50, so that rent and
  interest come out at the capitalist preset's £30 and £20). The body explains
  the result and not the construction, and a reader who opens the inputs will
  see shares that differ from lesson 1's for no stated reason. A `revenue`
  view that takes rent and interest as amounts rather than shares would remove
  the contrivance; recorded for the kit owner, not changed.
- **The `trinity` view's `rvTotal` tile is labelled "Annual product
  c + v + s"**, which is the chapter's term for the whole society's product
  and is used here for one capital's. Harmless on this course, where the
  presets are illustrative; a kit relabel ("Product c + v + s") was not made.
- **The three "fragments" footnote** (144) says the fragments were found in
  the manuscript "for Part VI", which is Engels' note and may be a Kerr
  misprint for Part VII. The lesson says "different places of the manuscript"
  and avoids the question, correctly.
