# Pedagogy assessment — Credit and Fictitious Capital (Capital, course 12)

Formed from the twelve lesson dicts in `content/capital/c12_credit/`
(`part_a.py`, lessons 1–6, Volume III Chapters 25–30; `part_b.py`, lessons
7–12, Chapters 31–36; `__init__.py`, the course dict) and the kit they render
through (`scripts/mathpath/labs/capkit.py` and `capkit_b.py`, modes `money`,
`interest`, `schemes`, `turnover`; views `payments`, `bounds`, `split`,
`circulate`, `capitalise`, `hoard`, `advance`, `bank-act`, `world`, `usury`), on
branch `feat/capital-subject` before the Subject was wired. The design
authority is `docs/capital/PLAN.md` §0, §B, the Course 12 entries in §C, §E,
§F and §G; the kit is as `docs/capital/kit-b-report.md` describes it; the
author's brief, including the two review-lesson sections, is
`docs/capital/AUTHORING.md`. Course 1, Commodities and Money, is the voice
reference, and `docs/pedagogy/capital-commodities-and-money.md` the model for
this document.

Every lesson was read in full before anything was changed. The course was
rendered with `scripts/preview_subject.py capital --course
capital-credit-and-fictitious-capital`; every pinned tile was read off the
rendered page with `node scripts/labcheck.js --observe`; every figure in prose,
worked example and quiz was recomputed by hand; every quotation and every
phrase in `&ldquo;…&rdquo;` (260 segments) was searched for in
`/mnt/project-files/capital-texts/volume-3-kerr.txt`, the Kerr text §E.3 makes
the Subject's only source, and Hubbard's table was read from the Kerr page 646
image. Beyond the quotations, some forty paraphrases and attributions ("a
Liverpool banker testified", "Engels, in a passage he added", "production
fell by a third", "Overstone, who had been his own firm's banker") were traced
to their lines. Lessons, in course order: `credit-and-fictitious-capital`,
`accumulation-of-money-capital`, `the-role-of-credit`,
`medium-of-circulation-and-capital`, `component-parts-of-bank-capital`,
`money-capital-and-real-capital-i` | `money-capital-and-real-capital-ii`,
`money-capital-and-real-capital-iii`,
`the-medium-of-circulation-in-the-credit-system`,
`the-currency-principle-and-the-bank-act`,
`precious-metal-and-the-rate-of-exchange`, `pre-capitalist-relationships`.
The bar marks the seam between the two modules. The course assumes Volumes I
and II and Volume III through Part IV, and is judged against that.

## Verdict

The course teaches its subject, and it does so honestly about what its subject
is. A reader who finishes it can net a set of bills and compute the cash a
settlement needs with and without a bank's purchase, a default or a bill for
nothing; split a profit into interest and profit of enterprise and find where
the rate of profit caps the rate of interest; compute a stock company's
dividend and salary and a borrower's return on his own capital; compute the
notes a circulation needs from prices and velocity and show that the label
"revenue" or "capital" changes nothing; price a claim to an income at a rate
and watch it move with the rate alone; compute the surplus product left unsold
when hoarders outnumber investors, and the circulating capital a contraction
releases; compute the Bank Act's cap, the reserve a drain takes and the demand
a panic leaves unmet; settle a balance of payments in bullion; and follow a
debt to the usurer year by year to the year it passes the holding. Those are
the acts the `standard` fields name and the quizzes measure; no objective is
"understand X". Every `mistakes[0]` is the §C misconception, refuted with a
tile: `£0` against `£100` for the discounted bill, `£0` of profit of
enterprise at a 10% rate of profit, `£200` of dividend and `£0` of enterprise,
the same `£100` of notes for wages and for cotton, `£2,000`, `£1,000` and
`£4,000` for the same `£100` a year, `+500` unsold with no spindle added,
`£600 released` with nobody saving, `£0` to `£100` with the goods unchanged,
`£50` flowing back, a cap falling from `£28,000,000` to `£22,000,000` while
the circulation's need does not, `£1,000,000 out` against production many times
larger, `£15` of interest against a surplus of `£10`. All pinned tiles on the
twelve pages matched the lab, every prose figure agreed with the lab or with a
recomputation, and all 260 quoted segments were found verbatim in the Kerr
text.

The question put to this review in particular, whether the course is honest
about the manuscript, is answered yes, and in more places than the brief asked
for. The `how_to` quotes Engels' preface ("no finished draft, nor even an
outline"); lesson 1 says in its third paragraph what kind of chapter Chapter
25 is; the `concepts_intro` of lessons 3, 4, 5 and 6 each repeat Engels' own
word on that chapter ("almost completely from the original manuscript",
"arranged differently in several places", "transpositions and eliminations"),
and each was checked against the preface at Kerr l. 308; lessons 10 and 11
open with Engels' sentences and say so in `read_intro` and in the body; lesson
9 marks the "twice as much currency" and "inconvertible notes" passages as
Engels' brackets; lesson 6 calls the "last cause of all real crises" sentence
"one sentence in a chapter Engels assembled from fragments" and refuses to
make it the chapter's theory. Where the course reads an argument through the
extracts it does so by quoting the extract and Marx's comment side by side
(Overstone's 3722 and "we remark, by the way"; Norman's "even if no money
existed" and "there would certainly be no general rate of interest"; Twells'
"operated splendidly" and Marx's "by no means of Overstone's opinion"), which
is the honest shape for these chapters. It does not invent coherence. The
nearest it comes is lesson 8's reading of the second clause of Kerr l. 4486,
which is now grounded (below) rather than offered as the lesson's own.

The defects were local and are repaired: a worked example in lesson 8 that
netted the wrong party after the default, a cross-reference in lesson 4 that
pointed two lessons forward when the lesson meant was five forward, an
Overstone figure given as "exports" where he said "commerce", a key line in
lesson 10 the read-out spelled "c A p", a quiz distractor the `why` admitted
had "no derivation", and a committee question number left bare in a note.
Nothing needs splitting, merging or reordering.

## The two alleged slips in the Kerr text

Both were checked carefully, as the brief asked, and both stand.

- **Kerr l. 3953, "the same price of money, for instance a five pound note".**
  The sentence is about one physical note passing between the two spheres;
  "price of money" makes no sense in it and "piece of money" makes exactly
  the sense the next clause needs ("the retail merchant can give to his
  capital the form of money which he receives from customers"). Marx's German
  is *dasselbe Geldstück*, a piece of money. The lesson quotes the text as
  printed and calls it a misprint; the parenthesis now names the German word
  as the ground, so a reader can see the claim is not a guess.
- **Kerr l. 4486, "it is by no means a demand for money as a means of
  payment".** As printed the second clause flatly contradicts the first
  ("a demand for means of payment and nothing else"). The chapter's own
  contrast, drawn at l. 4462, is between borrowing "only for the purpose of
  paying" in a crisis and borrowing "for the purpose of buying" in the
  recovery, and Marx's German has *Kaufmittel*, a means of purchase. The
  lesson's reading is right; what was wrong was its modesty. It said it
  "flags the reading as its own", which understated the evidence and left a
  reader thinking the lesson had rewritten Marx. It now says the German has
  *Kaufmittel* and that the slip is the translation's. The §C entry was
  brought into agreement in the same change.

## The voice, judged against Course 1

The register is Course 1's, and the course keeps every rule of §F.

**What works:**

- **The passage first, then its phrases in order.** Every body opens with the
  `<strong>Volume III, Chapter n.</strong>` block and then returns to it: "Go
  back through the passage. The bills 'circulate as means of payment'… While
  they do that they are 'commercial money in the strict meaning of the
  term'… And when they 'balance one another'…" (lesson 1); "Go through the
  passage. The 'loanable capital' is… A 'real accumulation of capital' is…"
  (lesson 6); "Read the passage as a sum" (lesson 11). Lesson 12's
  `read_title`, "The two victims first, then what usury does and does not
  change", is the move in six words.
- **Scenes only where the object is in the reader's life, and the Bank Act
  lesson opening on its figures.** The thirty-day invoice (lesson 1), "when
  a central bank raises its rate, someone always says that rates are high
  because the economy is strong" (lesson 2), the pension fund that holds
  shares (lesson 3), the five-pound note that is wages, then a shopkeeper's
  capital, then a manufacturer's (lesson 4), "bond prices fall when interest
  rates rise" (lesson 5), "interest rates are often lowest just when the news
  is worst" (lesson 6), the firm whose overdraft shrinks (lesson 7), "the
  news reports that firms cannot get cash, and some of those firms have
  warehouses full of goods" (lesson 8), the shopkeeper who banks his surplus
  by evening (lesson 9), "when the news says the pound has fallen" (lesson
  11), payday lenders (lesson 12). Each reaches the chapter's category in the
  same paragraph; none is invented. Lesson 10 opens, as §F rule 2 requires of
  the Bank Act lessons, by restating the passage's own rule.
- **The history as story with people in it, at strength.** Overstone is
  "banker, chief theorist of the Bank Act of 1844, and one of the richest
  men in England", and his position is given four sentences before Marx
  answers; Tooke is "a Russia merchant turned historian of prices" and
  Fullarton "a banker who had worked in India"; Wright is "thirty years a
  banker in Nottingham"; Gurney "the Quaker bill broker"; Hubbard "a former
  Governor of the Bank"; Twells "a Birmingham banker"; Child "the father of
  normal English bankerdom" in Marx's phrase. Every one of these was checked
  against the text or the record. Disraeli's dividend question (7%, then
  "Nine per cent.") is Marx's joke, pointed at before any of the lesson's
  own.
- **Second person in `p` and `worked.intro` only.** "You want the cash the
  settlement needs, then the cash once B has sold his bill to a bank" is the
  shape; `steps`, `standard`, quiz items and tile text stay impersonal.
- **The limit admitted.** Every `note` says what the lab cannot do: it
  "cannot tell a sound bill from a bill for goods that will never sell"
  (lesson 1), "does not model a falling profit" (lesson 2), "cannot see
  bonuses, share options" (lesson 3), "ignores risk, the expected growth of
  a dividend and the term of a bond" (lesson 5), "treats the reflux as
  immediate" (lesson 9), "ignores the timing Marx stresses" (lesson 11), "is
  kinder than the chapter's account of what usurers did" (lesson 12). The
  course `footer_lead` ends "No lab can tell you whether a crisis is a lack
  of money or a lack of capital", which is the course's question stated as
  its limit.
- **Pointing forward by title.** Every body ends with one sentence naming
  the next lesson by its title and its question; lesson 12 ends with the
  next course, Ground Rent, and its question.

**What to change in the courses that follow (and what was changed here):**

- **A three-letter word at the head of a key line is still spelled out.**
  Course 1's review recorded `due`, `out` and `use`; this course shipped
  `cap = fixed issue + gold in the Bank`, read "c A p equals". The course
  `key` had the same equation safely as "the Act's cap = …"; the lesson key
  now does too. The rule stands: a key line that is an equation starts with
  a word of four letters or more, or with the quantity's full name.
- **A worked example written from the story and not from the lab.** Lesson
  8's "A fails: A +100, B 0, C −100" and "which C must find" were what the
  author expected, not what the netting gives: with A's bill to B struck
  out, A keeps C's £100 and pays nothing, B pays C with nothing coming in,
  and C is square. The body paragraph had it right; the `worked.lines` did
  not. Every worked line should be read off the preset it claims to follow.
- **A forward reference by count, not by title.** "The lesson after next is
  his version of it" (lesson 4, on the reflux) pointed at Chapter 30 when
  the reflux is Chapter 33. §F rule 7 cites by title for this reason; the
  rule should cover every forward reference, not only the closing sentence.
- **A quiz distractor the `why` cannot explain.** Lesson 3's "60% has no
  derivation from these figures" is a confession, not a distractor. Every
  wrong answer should be a named error (here, 45%: the interest alone,
  reckoned on the borrower's own £100).

## What the course teaches well

- **The objectives are acts, and the drills measure them.** Every `standard`
  begins "Finish when you can…" and names the product; every quiz asks the
  same act on fresh figures (a circle of four £50 bills; £200 at 4% making
  12%; £5,000 of shares earning £600 with a £100 salary; £600 of wages and
  £900 between merchants at velocity 5; £30 a year at 6%; 800 accumulated
  with three quarters hoarding; 6 and 2 weeks at £80 then £60; a circle of
  £200 bills with the B→C bill unpaid; £900 at velocity 3 with £400 issued;
  14 + 10 against 26; 15 − 11 − 3; £40 at 25% with £10 to spare). The six
  course `outcomes` are the same acts, grouped.
- **One hard idea per lesson, across chapters that run together.** The three
  "Money Capital and Real Capital" chapters, which Engels says gave him the
  most trouble, are given three distinct computations with three distinct
  misconceptions: deposits that grow while nothing is built (`hoard`),
  loan capital that grows with nobody saving (`advance`), and a demand for
  means of payment that appears with nothing real changed (`payments`).
  Lesson 6 says in its second paragraph which of Marx's two questions it
  takes and which the next two take.
- **The misconceptions are the chapters', and they are positions people
  held.** Overstone's "value of capital" (lesson 2), the Currency School's
  "the bank decides how much money circulates" (lesson 9) and "a mixed
  currency should behave as a metallic one would" (lesson 10), the
  classical "capital is the result of saving" with Mill named (lesson 7),
  the mercantilist "a gold outflow means the country is poorer" with Hume's
  answer (lesson 11), Carey's comparison of usurer's and modern rates
  (lesson 12). Each is stated at strength and refuted with a number.
- **Marx's figures are kept apart from the lesson's.** The `note` of every
  lesson says which are which: Marx's £100 at 5%, his share at £200 and his
  change of rate to 10% and 2½% (all checked in Chapter 29); Chapter 29's 14,
  14, 28, 20, 8 and the 6-million drain; Volume II's 9 weeks and 3 at £100;
  Volume II's 4,000c + 1,000v + 1,000s; Newmarch's 12,670,000, 10,350,000
  and 3,700,000, with his 1,380,000 and the lab's `£0 (£1,380,000 in)`
  agreeing; Gurney's 4 to 5 millions hoarded; Luther's 40 per hundred;
  Hubbard's 10,471,000 at 2.75% and 2,684,000 at 6%, with eight prices up
  and five down, read from the page-646 image. Lesson 11 also tells the
  reader that Marx's own restatement of the India figures a page later
  (2,250,000 and 3,250,000) does not agree with Newmarch's, which is the
  honest thing to do with a rough manuscript.
- **Later writers are presented, not answered by Marx.** Berle and Means
  (lesson 3), Fisher (lesson 5), Mill and Robertson (lesson 7), Bagehot
  (lesson 8), Friedman (lesson 9), Thornton on real bills (lesson 1), Hume
  (lesson 11), Yunus and microfinance (lesson 12). Every one is followed by
  "what in the chapter bears on it" in those words or their equivalent, and
  not one by "Marx's answer". Lesson 3's close on Berle and Means ("Marx's
  chapter takes the salary at its face… and the lab does the same") and
  lesson 8's on Bagehot ("Whether lending that way prevents crises or only
  shortens them is not something the chapter settles") are the shape the
  AUTHORING brief asks for.
- **The seam at lesson 7 is invisible.** Lesson 6 ends "“Money Capital and
  Real Capital II” follows the routes by which money becomes loan capital
  without anyone saving"; lesson 7 opens on exactly that. Both modules use
  the same quotation conventions (stated in each docstring), the same
  `<strong>Volume III, Chapter n.</strong>` block, British spelling in prose
  and the translator's inside quotation marks.
- **Figures agree with the lab.** All pinned strings matched: `£0`/`£0`/`£0`,
  `£100`/`£100`/`£0`, `£100`/`£100`/`£100`; `£3`/`£7`, `£8`/`£2`, `£10`/`£0`
  with `breached: 10% ≥ 10%`; `£200`/`£0`, `£50`/`£150`, `£40`/`£160`;
  `£1,000`/`£100` twice, `£2,000`/`£200`, `£1,000`/`£40`; `£2,000`, `£1,000`,
  `£4,000`, `£200`; `0: hoarders' sales = investors' purchases`, `+500: 500
  of surplus product unsold`, `−250: 250 of demand without a product`;
  `£1,200 = I £900 + II £300` with `£600 released`, `£0 released`, `£600 more
  tied up`; `£0`/`£0`, `£100`/`£100`, `£300`/`£0`; `£150`/`£0`, `£150`/`£50`,
  `£300`/`£0`; `£28,000,000`/`£0`, `£22,000,000`/`£0`, `£22,000,000`/
  `£2,000,000`, `£24,000,000`/`£0`; `£0`, `£1,000,000 out`, `£0 (£1,380,000
  in)`; `£15 in year 1`/`year 6`, `£4 in year 1`/`repaid in year 3`, `£20 in
  year 1`/`year 4`, `£100 in year 1`/`year 12`. The usury debt path in the
  worked example (55, 61.5, 69.95, 80.94, 95.22, 113.78) was recomputed and
  is right; so are the artisan's repayment in year 3, the Leipzig peasant's
  ruin in year 4 and the lord's in year 12.

## What it taught badly, or said wrongly

### Fidelity

- **`accumulation-of-money-capital`, body:** "as it had from 45 to 120
  million pounds of exports under the Act". Overstone (Kerr l. 3765) said
  "the commerce of England grew from 45 to 120 million pounds" in the
  thirteen years of the Act. Now "English commerce had, Overstone told the
  committee, from 45 to 120 million pounds in the thirteen years of the Act".
- **Same lesson, body and `note`:** "3%, the Bank's rate in January 1847"
  and "10%, the Bank's rate in November 1847", and the note's "as the chapter
  lists them". Kerr l. 3753 lists ranges: "3 to 3½% in January", "November
  7 to 10%". Now "where the Bank's rate began in January 1847", "where the
  Bank's rate peaked in November 1847", and the note gives both ranges.
- **Same lesson, body:** "Marx's examiners put the ordinary rate at 'from 7
  to 10%'" made Marx the witness. The figure is the examiner's question 3729
  to Overstone. Now "the committee's examiner put the average rate at".
- **Same lesson, body:** "Marx is very angry in this chapter" was a claim
  about Marx's state of mind. Now "at his most sarcastic", which the
  comments on Overstone ("our banking lord", "posing as a schoolmaster")
  support.
- **`medium-of-circulation-and-capital`, body:** "the lesson after next is
  his version of it" (the reflux). The reflux is Chapter 33's lesson, five
  on. Now by title.
- **`money-capital-and-real-capital-iii`, body:** "This lesson reads it so,
  and flags the reading as its own." Now grounds the reading in the German
  (*Kaufmittel*); see above. The parallel parenthesis in lesson 4 now names
  *Geldstück*.
- **Verified and left standing:** "a Liverpool banker testified, goods were
  'almost unsaleable'" is Lister of the Union Bank of Liverpool, question
  2537 at l. 3699; "production in the English industrial districts fell by
  a third" is Marx's parenthesis at l. 4240; "Engels, in a passage he added
  to the next chapter" for "purely one of buying and selling" is inside the
  bracket that ends "[he was the banker of my firm in Manchester]" at
  l. 3810–3814; the Alkali Trust's "more than thirty" works, "about 5
  million" in shares and "about one million" of floating capital are at
  l. 3909–3911; "Every expert… Overstone at their head, congratulated the
  others" is l. 4234; Chapter 35's "one sole exception" to the maximum is
  13–30 November 1857 at l. 4937; the Act's third suspension in 1866 and
  Gurney and Chapman as partners of Overend, Gurney and Co. are matters of
  record the text does not contradict.

### Arithmetic and the lab

- **`money-capital-and-real-capital-iii`, `worked.lines` and `worked.after`:**
  "A fails: A +100, B 0, C −100" and "which C must find". The lab strikes
  bill 1 (A→B) and nets A +100, B −100, C 0; the body paragraph and Course
  1's `broken` preset both say B pays C with nothing coming in. Now "A
  +100, B −100, C 0" and "which B must find before the day his bill to C
  falls due". The pinned tiles were right throughout; the error was in the
  hand-written line.

### Speech

- **`the-currency-principle-and-the-bank-act`, `key[0]`:** `cap = fixed issue
  + gold in the Bank` was read "c A p equals fixed issue plus gold". Now
  `the Act's cap = …`, read as words; confirmed from the rendered `data-say`.
  No other run on the twelve pages spelled a word.

### Quiz

- **`the-role-of-credit`, quiz 3:** distractor "60%" replaced by "45%", the
  interest alone on the borrower's own £100, with the `why` saying so. Every
  other distractor on the course was argued for and could not be defended:
  £200 as the gross of the circle, £24 as the whole profit, 12% as profit
  before salary, £120 as wages alone, £180 as multiplying instead of
  dividing, +600 as the hoarders' sales alone, £480 as the new advance, £600
  as the bills' gross, £300 as what stays out, 12 and 16 as differences
  against one term, £4 million as leaving out the interest, and so on.

### Prose

- **`precious-metal-and-the-rate-of-exchange`, `note`:** "as the Kerr text
  gives them at 1786" left a committee question number bare. Now "in his
  answer to question 1786".

## Do twelve lessons earn their place?

Yes, though two pairs share a lab and a reader will notice.

- **Lessons 1 and 8** both run the A–B–C circle of £100 bills through the
  `payments` view. The repetition is designed: lesson 1 adds a bank and a
  bill for nothing, lesson 8 adds a default and a stop to credit, and both
  say they are Course 1's chain from “Hoards and Means of Payment”. The
  course `blurb` promises exactly this ("Settle a circle of bills with no
  cash, then break it"). Lesson 8's `cash-only` preset, which neither Course
  1 nor lesson 1 has, is what keeps it from being a repeat.
- **Lessons 4 and 9** both compute notes needed = prices / velocity, in the
  `circulate` and `bank-act` views. Lesson 4's point is that the label
  revenue/capital does not enter the sum; lesson 9's is the reflux and the
  halved velocity of a panic. Different misconceptions, different tiles
  (`moReturned` exists only in the second).
- **Lessons 2 and 3** share the `interest` mode but not a view (`bounds`,
  `split`) or a question (what a rising rate does to the borrower; where the
  profit goes when the owner is not the manager).
- **Lessons 6, 7 and 8** are three chapters with one title, and the course
  justifies three lessons by giving each its own mechanism and by saying,
  in lesson 6, which of Marx's two questions each takes. Chapter 32's first
  half repeats Chapter 31's account of where loan capital comes from, and
  lesson 8 handles that by giving it one paragraph and the plethora
  sentence, not a second lab.
- **Lesson 10** is the one lesson whose passage is Engels', not Marx's, and
  it says so three times. Its lab is the course's best: Marx's own 14 + 14 =
  28, 20 out, 8 reserve, a 6-million drain, from Chapter 29, run into
  Gurney's 4 millions hoarded. The one illustrative figure, the suspension's
  extra 2 millions, is marked as such and corrected by history in the next
  paragraph ("What actually happened was smaller").
- **Lesson 12** reads Chapter 36, the one fully elaborated chapter in the
  Part, and is the only lesson whose figures are wholly illustrative; the
  `note` says so and names Luther's 40% as the exception.

Nothing merges. The only candidate for removal would be lesson 8's lab in
favour of lesson 1's, and the `cash-only` preset and the default argue
against it.

## Can a reader who has done Courses 1–11 follow this?

Yes, with the help the course gives. The hard places are the places Engels
found hard.

- **Lesson 1** does the right thing with a chapter that is two pages of
  argument and twenty of extracts: it takes the two pages, quotes the
  extracts for what they show (Leatham, the Liverpool banker, Gilbart), and
  tells the reader in its third paragraph what kind of text this is before
  asking anything of it. Thornton's objection to real bills is given before
  the lab, so the reader does not take the backed/unbacked tile as a theory
  of sound banking.
- **Lesson 2** is an argument conducted in cross-examination, and the lesson
  gives Overstone four sentences at strength before Marx's one. The lab is
  the simplest in the course and that is right: the point is a subtraction,
  and the chapter's weight is in who was saying what.
- **Lesson 5** is where "fictitious capital" finally gets its meaning, and
  the lesson says so in `concepts_intro`. The bond, the wage and the share
  are taken in Marx's order, the share's "does not exist twofold" is given a
  paragraph of its own, and the modern objection ("information, not
  fiction") is given its due before the one point both sides accept.
- **Lesson 6** is the first of Engels' reconstructed chapters, and the
  reader is told so and told which question is taken here. The `hoard` view
  is the hardest lab in the course to read; the `panel_intro` and the four
  steps say exactly what the two groups do and what the sign means, and
  the `note` says what the model leaves out.
- **Lesson 8** asks the reader to accept a correction to the printed text.
  It now gives the ground (the German) rather than asking for trust.
- **Lesson 10** carries the most history, and keeps it in the order of the
  argument: the theory at strength, Marx's 1859 objection, Hubbard's table,
  the lab, the panic, the suspension, the bankers, Engels' verdict on both
  schools.

## Repairs made in this pass

In `content/capital/c12_credit/part_a.py`: `accumulation-of-money-capital`
body (the Overstone commerce figure, the examiner's question, the January and
November rates, "most sarcastic") and `note`; `the-role-of-credit` quiz 3
distractor and `why`; `medium-of-circulation-and-capital` body (the forward
reference by title, the *Geldstück* ground). In `part_b.py`:
`money-capital-and-real-capital-iii` body (the *Kaufmittel* ground) and
`worked.lines`/`worked.after`; `the-currency-principle-and-the-bank-act`
`key[0]`; `precious-metal-and-the-rate-of-exchange` `note`. In
`docs/capital/PLAN.md`: the Course 12 §C entry for lesson 8, so that it says
what the lesson now says about l. 4486. No preset, `expect`, slug, module,
lab key, mode or view changed; no other §C entry needed correcting.

Slugs, lesson count, modules and lab modes are as PLAN §B and §C list them,
and every `module` name matches the Kerr chapter heading. After the repairs
`scripts/preview_subject.py capital --course
capital-credit-and-fictitious-capital` reports OK: 13 pages rendered, 12 labs
executed and swept, 12 with pinned figures matching, 0 failing; the
quotation checker reports 260 segments, 0 misses.

## Remaining issues

- **The read-out spells three-letter words at the head of a key line.**
  Recorded in Course 1's assessment and met again here (`cap`). The fix in
  content is a wording rule; the fix in `scripts/mathpath/speech.py` belongs
  to the chrome-renderer tier and has not been made. Every course after this
  one should grep its rendered `data-say` for `[a-z] [A-Z] [a-z]` before
  reporting OK.
- **Lesson 8 reuses lesson 1's lab.** Acceptable for the reason given above,
  but if the kit ever gains a `payments` tile for the velocity of notes
  under a stopped credit, lesson 8's `cash-only` preset is where it would
  go, and the lesson would then stand further from lesson 1.
- **The German text is cited but not in the project's shared folder.** Both
  slip claims now rest on *Geldstück* and *Kaufmittel*. §E.3 makes Kerr the
  only source for quotations, and the lessons quote nothing else; but a
  reviewer who wants to check the German word has nothing in
  `/mnt/project-files/capital-texts/` to check it against. A plain-text MEW
  or MEGA extract of Volume III beside the Kerr files would close that gap
  for every course in the Subject.
- **Lesson 11's handling of Marx's own India figures** (2,250,000 and
  3,250,000 against Newmarch's 2,320,000 and 3,700,000) is correct and
  honest, but a parenthesis. A reader who wants to know whether the error is
  Marx's, Engels' or the translator's is not told, because the text does not
  say. Recorded, not changed.
