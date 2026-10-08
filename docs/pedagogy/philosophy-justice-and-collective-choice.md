# Pedagogy assessment — Justice and Collective Choice (philosophy, course 7)

First assessment, formed from the ten lesson dicts in
`content/philosophy/c7_justice/` (`part_a.py`, lessons 1–5, and `part_b.py`,
lessons 6–10, by two authors; `__init__.py`), the empty spoken-forms file
`content/spoken/philosophy_c7_justice.py`, the design they were written from
(`docs/philosophy/PLAN.md` §C Course 7, §D.2 `decide`, `aggregate`, `simpson`
and `vote`), and the kit they render through
(`scripts/mathpath/labs/choicekit.py`), on branch `feat/philosophy` before the
Subject is wired into the site. No prior assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in course
order: `the-original-position-and-maximin`,
`the-difference-principle-and-leximin`,
`entitlement-patterns-and-the-gini-coefficient`,
`fairness-statistics-and-disparate-rates`,
`majority-rule-and-the-condorcet-paradox`, `plurality-runoff-and-borda`,
`independence-and-arrows-theorem`, `strategic-voting-and-manipulation`,
`the-discursive-dilemma`, `the-condorcet-jury-theorem`. The course declares
Ethics and the Arithmetic of Welfare as its prerequisite, and the path promises
that each course assumes the ones before it and nothing else, so the course is
judged against the first six courses only: maximin, Laplace and the value of
information from Decision and Rationality, the aggregation rules and the Gini
coefficient from Ethics and the Arithmetic of Welfare, the pooled and
standardised rates from Science, Induction and Causation, the money pump from
Decision and Rationality, independent witnesses from Knowledge and Evidence,
and free-riding from Games and the Social Contract. Every one of those is
referenced by title where it is used, and nothing is assumed from outside the
path.

Every figure quoted below was read off the rendered page with
`node scripts/labcheck.js --observe` (`scripts/preview_subject.py` rendering to
a scratch directory), not predicted, and then recomputed by hand. The preview
reported OK before any change was made: ten labs execute and survive the
control sweep, ten pages carry pinned figures and all of them match, and no
math run lacks a spoken form.

## What the course teaches well

- **Every lesson closes on an act, and the act is the one the lab measures.**
  Build the matrix and name the society each rule picks
  (`the-original-position-and-maximin`); sort, find the first difference, name
  the winner and state the incentive claim it rests on
  (`the-difference-principle-and-leximin`); compute a Gini before and after a
  round of payments and say which view treats the change as significant
  (`entitlement-patterns-and-the-gini-coefficient`); compute four rates, two
  pooled rates and the standardised pair, and name the claim about the mix the
  verdict depends on (`fairness-statistics-and-disparate-rates`); tabulate
  pairwise counts and write the cycle (`majority-rule-and-the-condorcet-paradox`);
  run four rules by hand and name a profile on which three disagree
  (`plurality-runoff-and-borda`); strike a loser, recount, and name two things
  the theorem does not claim (`independence-and-arrows-theorem`); name a bloc,
  the ranking it reports and the theorem (`strategic-voting-and-manipulation`);
  take the majorities column by column and give a profile where the procedures
  part (`the-discursive-dilemma`); write the majority's probability as a sum and
  say which way it moves (`the-condorcet-jury-theorem`). No `standard` says
  "understand".
- **One profile carries the middle of the course.** Four voters ranking A B C,
  three B C A and two C B A is laid out in `plurality-runoff-and-borda`
  (plurality A, every other rule B), and struck in
  `independence-and-arrows-theorem` (remove C and plurality elects B; remove B
  and it elects C). The reader meets the independence failure on ballots already
  counted, which is what keeps that lesson to one idea.
- **The prose figures and the lab agree.** Observed tiles: `rawls` prints equal
  and 5, `laplace` on the same table unequal and 10, `close-call` a tie at 5;
  `incentive` B ≻ A at worst 5 vs 6, `tie-at-the-bottom` A ≻ B at 2nd worst 8
  vs 6; `chamberlain` Gini 0 vs 3/40, `redistribute` 1/2 vs 1/5, `two-rounds`
  0 vs 3/20; the admissions tables 52/100 against 28/100 pooled and 2/5 against
  2/5 standardised, the reversal 58/100 against 25/100 pooled and 2/5 against
  7/16 standardised; the cycle A > B > C > A and the seven-voter Condorcet
  winner B; the three-winners profile A under plurality with C the Condorcet
  winner; `iia-borda` B with the removal of A flagged; the Borda bloc "voters
  ranking C B A gain by C A B"; the court premise-based T, conclusion-based F;
  the juries 81/125 and 12/25, 36791901/48828125 and 1959552/9765625, 44/125,
  12036224/48828125, 1/2 and 63/256. Every one is the number the body, the
  worked example or the quiz states, with the three exceptions below.
- **The misconceptions are the PLAN's, named as models and refuted with a
  number.** Maximin as risk aversion is refuted by a rule that never adds
  (`the-original-position-and-maximin`); the difference principle as equality
  by 6 against 5 with the 9 and 20 counting neither way
  (`the-difference-principle-and-leximin`); a just shape by 3/40 "whether the
  fans paid freely or were robbed"
  (`entitlement-patterns-and-the-gini-coefficient`); a pooled gap as unequal
  treatment by 13/25 against 7/25 over equal rates of 3/5 and 1/5
  (`fairness-statistics-and-disparate-rates`); majority rule always ranking by
  three 2–1 contests that go round (`majority-rule-and-the-condorcet-paradox`);
  most first places as the people's choice by a leader five of nine rank last
  (`plurality-runoff-and-borda`); Arrow as impossibility by what each real rule
  gives up (`independence-and-arrows-theorem`); strategic voting as lying about
  facts by a ranking no one else can observe
  (`strategic-voting-and-manipulation`); premise majorities as a conclusion
  majority by 2–1, 2–1 and 1–2 (`the-discursive-dilemma`); the wise crowd by
  44/125 and about 0.25 (`the-condorcet-jury-theorem`).
- **Positions are stated at their strongest and the lesson does not announce a
  winner.** Rawls's three features and Harsanyi's denial of the first each get
  a valid argument from their premise, and the lesson says the lab cannot choose
  between no probabilities and equal ones. The incentive argument is given as
  an argument with a premise the lab cannot check. Arrow's theorem is followed
  by three things it does not say; Gibbard–Satterthwaite by what it leaves
  open; the two judgment procedures are each costed; the jury theorem's two
  assumptions are named as strong.
- **Each lesson states the lab's limit where it leans on it**: the table
  describes no real society; the lab ranks the vectors typed and cannot see
  what produced them; the Gini does not know who paid whom; the mix is not in
  the table; the removal test is a cousin of Arrow's condition, not the
  condition; "none found" covers one profile and blocs of identical voters.
- **Cross-references are by title, never by number**, in both parts; spelling
  is British in both; the `x` shorthand reads as sentences.

## What the course teaches badly, or claims and does not teach

- **Two headings that print their own markup**
  (`independence-and-arrows-theorem` mistake 3,
  `strategic-voting-and-manipulation` mistake 3). The titles were written with
  `&ldquo;` and `&rdquo;`, and `mistakes` titles pass through `esc_inline`, so
  the rendered page read "Hearing &ldquo;dictator&rdquo; as a tyrant" with the
  entities visible. Real quotation marks now.
- **A note that tells the reader to move a number that moves nothing**
  (`the-original-position-and-maximin`, `note`). "Make the middle place much
  more likely than the other two and watch the verdict of the average rule
  move." The middle place pays 8 in the unequal society against 5 in the equal
  one, so weighting it more heavily keeps the unequal society ahead; the
  verdict does not move, and with unequal weights the rule is expected utility,
  not the average. Rewritten: weight the bottom place at 4/5 and the expected
  utility of the unequal society falls to 22/5, below 5.
- **A pinned figure with no story** (`the-original-position-and-maximin`,
  `harsanyi`). The PLAN asks this preset to ship under Laplace, but a page has
  one redraw-only rule and the page's is maximin, so the preset can pin only
  the value-of-information tile, which prints 1 — and the prose never mentioned
  it. One paragraph added: with equal chances the value of perfect information
  is the value of lifting the veil, 11 against 10, and the veil withholds
  exactly that from everyone. This is the closest correct thing to the PLAN's
  instruction, and the panel text already tells the reader to switch the rule.
- **A note whose claim is false on the lab**
  (`majority-rule-and-the-condorcet-paradox`, `note`). "Add a single voter to
  the cycle profile with the ranking A B C and watch the cycle disappear: a
  winner appears." With two A B C voters, one B C A and one C A B, A and C
  split 2–2 and nobody is undefeated; no Condorcet winner appears. Rewritten:
  change the C A B voter to C B A and B beats both rivals 2–1.
- **A note that says "change one count" where four must change**
  (`fairness-statistics-and-disparate-rates`, `note`). Moving ten women's
  applications between departments while keeping the rates means rewriting
  both women's cells. Rewritten with the cells (18 of 30, 14 of 70) and the
  resulting pooled rate, 32/100.
- **A preset id used as if the reader could see it**
  (`fairness-statistics-and-disparate-rates`, quiz 1, mistake 1, `note`). "The
  berkeley table" names the preset's id; the reader sees its label, "Equal rates
  in both departments, different application mixes", and the body never says
  what Berkeley is. The references now say "the lesson's table", and one
  paragraph attributes the pattern to Bickel, Hammel and O'Connell's study of
  Berkeley's 1973 graduate admissions, which is where it comes from.
- **Distractors that are true.** `majority-rule-and-the-condorcet-paradox`
  quiz 3 offered "A is last for four of the seven voters" as a wrong answer to
  why B is the Condorcet winner; four of the seven do rank A last. Replaced by
  "A is ranked first by fewer voters than B", which is false (3 against 2).
  `fairness-statistics-and-disparate-rates` quiz 2 offered "the selective
  department admits fewer people" as a wrong explanation of the pooled gap; it
  is half of the true explanation, since with equal department rates no mix
  could open a gap. Replaced by "fewer women than men applied in all", false
  at a hundred each. `the-difference-principle-and-leximin` quiz 4 offered
  "the total of the second distribution is larger" as a wrong answer to what
  the incentive argument needs; against an equal distribution a higher floor
  entails a larger total, so a careful reader could argue for it. Replaced by
  the claim the argument must deny, that the top would produce as much if paid
  5, and the `why` says why.
- **A question that asks the lesson to pick a winner**
  (`the-difference-principle-and-leximin`, quiz 3). "Which is right?" of the
  egalitarian and the difference principle, when the correct answer describes
  what each prefers. Now "What does each prefer?". Likewise
  `the-original-position-and-maximin` quiz 4 asked which reason "the lesson
  defends"; the lesson defends none, it reports Rawls's grounds, and the
  question now says so.
- **Rawls's principle misplaced** (`the-difference-principle-and-leximin`,
  body). "Rawls's second principle of justice, the difference principle": the
  difference principle is the second part of the second principle, beside fair
  equality of opportunity. Corrected. The same lesson used the lexical form
  without saying that Rawls described it and set it aside as a refinement his
  argument did not need; the "limits" paragraph now says so, since a reader
  who meets leximin here should not take it for Rawls's own statement.
- **Nozick's critics given less than their strength**
  (`entitlement-patterns-and-the-gini-coefficient`, body). The "three replies"
  paragraph promised three and delivered one and a half: a sentence about the
  starting point, a garbled sentence ("a rich man's wealth can be taken to be
  earned by the same process as Chamberlain's"), and the floor-only point. The
  strongest reply, Rawls's, that the difference principle governs the rules of
  the basic structure and not the pattern after each exchange, so that a tax is
  one of the rules the fans paid under, was absent. Rewritten with the three
  replies and Nozick's rejoinder on taxation, so the dispute is left where it
  stands. "No tile here can verdict on it" is also gone.
- **An attribution missing** (`the-discursive-dilemma`, body). The court is
  Kornhauser and Sager's doctrinal paradox and the name is Pettit's; the lesson
  credited only List and Pettit's theorem. One sentence added.
- **The bloc the lab moves is not the bloc the prose moves**
  (`strategic-voting-and-manipulation`, body). The body has two of the three
  C B A voters bury B; the lab switches the whole bloc, which the reader may
  check and find different totals (7, 6, 8). One clause added so both are on
  the page.
- **Course key lines that state what the course does not establish**
  (`__init__.py`, `key`). "No rule is fair, sincere and decisive too" is a
  slogan for neither theorem, and "majority is right with probability above p"
  is false below p = 1/2. Now "no rule meets Arrow's three on every profile"
  and "p above 1/2: a majority beats one voter". A lesson key line in
  `entitlement-patterns-and-the-gini-coefficient` ("free transfers change the
  Gini, not the right") and one in `strategic-voting-and-manipulation` ("no
  ranking can pay") were reworded to say what they mean.
- **A prerequisite named by title** (`entitlement-patterns-and-the-gini-coefficient`,
  concept 3). The Gini coefficient was redefined without saying where the
  reader met it; the concept now names “Priority, Equality and Levelling Down”.

## The seam between part A and part B

The two parts are in one voice: British spelling throughout, the same "the lab
prints" idiom, the same habit of stating the position before its cost. Part A
ends with the Condorcet paradox and tells the reader the next lesson reads the
same profile under the other rules; part B opens by saying the previous lesson
found that majorities sometimes cannot be assembled into a ranking, and does
exactly what was promised. Part B's docstring states the convention the pinned
tiles follow (a redraw-only control keeps its shipped value when a preset is
chosen), and part A's `harsanyi` preset obeys it. The one drift found is in
quotation: part A writes curly quotes directly in prose and part B writes
`&ldquo;` entities, which is harmless in prose fields and was the cause of the
two broken headings above. Part B's one relative reference to "the lesson on
strategic voting" is now by title.

## Where a learner gets stuck

- `plurality-runoff-and-borda` carries four rules and the Condorcet comparison,
  as the PLAN asks. The arithmetic is laid out in two tables and the worked
  example runs all five counts, so the load is on the reader's working memory
  rather than on anything unexplained; a reader who skips the Borda table will
  not know where 12 came from. The lesson count is fixed by `COURSES.json`, so
  this is recorded rather than split.
- `independence-and-arrows-theorem` asks the reader to hold three conditions,
  a removal test that is only a cousin of one of them, a theorem and three
  non-claims. The lesson is honest about the cousinhood, which is the right
  call, but the gap between "the winner changed" and "the ranking of a pair
  depends on a third candidate" is where a reader will stall. The removal test
  is what the kit computes; a tile for the group's ranking of the pair before
  and after would close the gap and is recorded below.
- `the-condorcet-jury-theorem` leans on "as many such sets as ways to choose
  which k are right" without a binomial coefficient, which keeps the path's
  promise of school arithmetic only; the lab does the counting, so a reader who
  does not move the slider has one worked case and a claim about eleven jurors
  on trust.

## Verified correct and left alone

Rawls's three features for maximin (no basis for probabilities, little care
for gains above the minimum, an unacceptable worst case) and Harsanyi's
equiprobability reply are stated as each author stated them. Nozick's phrase
"liberty upsets patterns", the entitlement theory's three parts including
rectification, Condorcet in the eighteenth century, Arrow's theorem with
unrestricted domain and transitivity made explicit in the `thm` block, the
exemption of two candidates, single-peaked preferences as the restriction that
lets majority rule work, the Gibbard–Satterthwaite theorem with resoluteness and
non-imposition stated, List and Pettit's four conditions with the premise-based
procedure giving up systematicity, and the jury theorem's three cases were
each checked against the sources and are right. The Gini figures 1/2 and 1/5
for (2, 4, 6, 28) and (6, 8, 10, 16), the standardised rates 2/5 and 7/16, the
Borda totals 8, 12, 7 and 8, 8, 11 and 6, 11, 10, the burying arithmetic (one
voter alone leaves B and C tied at 8, two suffice), the discursive-dilemma
uniqueness claim in the `note` (with three judges and a conjunction the only
inconsistent pattern is both, p only, q only), and the jury fractions were each
recomputed by hand. Every `note` instruction on the other seven lessons does
what it says: the Borda winner on the first Arrow preset survives every
removal; moving one C B A voter to B C A leaves B the Borda winner with nothing
to find; one judge changed restores agreement; n = 1 gives the voter; the
spoiler profile goes to a three-way tie when one voter moves.

## Remaining issues, for whoever next owns this course or the kit

- The `decide` mode has one redraw-only rule per page, so a PLAN entry that
  asks two presets on one page to ship under different rules
  (`the-original-position-and-maximin`, `rawls` under maximin and `harsanyi`
  under Laplace) cannot be built as written. The page ships maximin and the
  prose directs the switch; a per-preset shipped rule would let the preset show
  its own point.
- The `vote` mode's independence tile reports a change of winner, not a change
  in the group's ranking of a pair. A tile printing the pairwise count of the
  former winner against the new one, before and after removal, would let
  `independence-and-arrows-theorem` show Arrow's condition rather than its
  cousin.
- `plurality-runoff-and-borda` would be two lessons (plurality and the
  runoffs; Borda and the Condorcet comparison) if the course is ever extended.
- The jury lesson could use a tile for the single voter's competence beside the
  majority's, so the comparison "81 against 75 out of 125" is on the page and
  not only in the prose.
