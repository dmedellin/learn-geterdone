# Pedagogy assessment — Knowledge and Evidence (philosophy, course 2)

Formed from the twelve lesson dicts in `content/philosophy/c2_knowledge/`
(`part_a.py`, lessons 1–6, and `part_b.py`, lessons 7–12, written by two
authors from `docs/philosophy/PLAN.md` §C), the course dict in `__init__.py`,
the spoken forms in `content/spoken/philosophy_c2_knowledge.py`, and the pages
as `scripts/preview_subject.py` renders them, with every preset's tiles read
off the built page by `labcheck.js --observe`. The course may assume
Arguments and Validity and nothing else. All twelve lessons were read before
any was changed; the last section records what was changed and what was not.

Lessons, in course order: `belief-truth-and-justification`,
`gettier-cases-and-the-fourth-condition`, `reliabilism-and-the-clairvoyant`,
`skepticism-and-the-closure-argument`, `the-regress-of-justification`,
`credence-and-the-dutch-book` | `conditional-credence-and-base-rates`,
`updating-on-evidence`, `testimony-and-independent-witnesses`,
`reference-classes-and-statistical-evidence`, `the-lottery-paradox`,
`the-preface-paradox`. The bar marks the seam between the two authors.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.** Find
  the disagreeing row and name its direction
  (`belief-truth-and-justification`); build the row with all three conditions
  and a verdict of no, then the row the repair cannot separate
  (`gettier-cases-and-the-fourth-condition`); say which direction each case
  pushes a theory (`reliabilism-and-the-clairvoyant`); say what the lab has
  not decided (`skepticism-and-the-closure-argument`); name the position for
  each deletion (`the-regress-of-justification`); write the bets, not just
  the word "incoherent" (`credence-and-the-dutch-book`); fill the table before
  dividing (`conditional-credence-and-base-rates`); update twice and name the
  factor each time (`updating-on-evidence`); say what a witness is worth in a
  number (`testimony-and-independent-witnesses`); say which class each rate
  is a rate of (`reference-classes-and-statistical-evidence`); show the
  accepted set has no model (`the-lottery-paradox`); say why the set is
  consistent and the conjunction is not accepted (`the-preface-paradox`).
  None is "understand".
- **The method of cases is taught once and reused twice, which is the right
  shape.** `belief-truth-and-justification` fixes the procedure (verdict
  first, definition second, first disagreeing row, direction), and the next
  two lessons run it unchanged on harder tables. The tables themselves are
  well chosen: Smith's coins and the stopped clock are identical rows with
  different verdicts from ordinary perception, and the lesson says plainly
  that no formula over those columns can separate them; fake barns repeats
  the trick one column later. The chicken sexer, left out of the table in
  `reliabilism-and-the-clairvoyant`, is the right closing move: it shows that
  the choice of rows decides what fits.
- **Positions are stated at their strongest and the lab stops where it
  should.** The skeptic's modus tollens and Moore's modus ponens are both
  shown valid over one shared conditional, Dretske's zebra is given as the
  third exit with its own counterexample row, and the lesson says what each
  of the three costs without choosing (`skepticism-and-the-closure-argument`).
  The regress is a six-sentence set whose minimal inconsistent subset is the
  whole set, so each deletion is a named position with its model
  (`the-regress-of-justification`). Hume's miracle argument is a comparison
  of two weights "and not a ban", with the three-witness preset showing what
  would clear it (`testimony-and-independent-witnesses`). The twin's
  justification verdict is flagged as the reader's to record
  (`reliabilism-and-the-clairvoyant`, `note`).
- **The arithmetic is right and the prose agrees with the tiles.** Every
  figure in the prose was checked against the page: 11/566 and 297/332 and
  1/94906 in `conditional-credence-and-base-rates`; 3/4, 9/10, 8/107 in
  `updating-on-evidence`; 1/12, 9/20, 1/1002 and 998001/999002 in
  `testimony-and-independent-witnesses`; the six class rates and the
  273/350 vs 289/350 reversal in `reference-classes-and-statistical-evidence`;
  the loss of 1/5 and 1/6 per unit in `credence-and-the-dutch-book`;
  "2: first R & E" in `reliabilism-and-the-clairvoyant`. The two-urn example
  is small enough to finish on paper and the worked example does so.
- **The misconceptions are the real ones and are refuted with the specific
  row or number**: a valid argument compels assent (the three-sentence
  inconsistent set); "reliable" means "right this time" (the stranger's
  guess has R = 0); credence 1/2 means "no idea" (six halves sum to 3); a
  90%-reliable witness makes the claim 90% likely (1/12); a bigger threshold
  cures the lottery (1,000 tickets at 999/1000).
- **The seam is nearly invisible.** The two authors agree on vocabulary
  (credence, verdict, "the lab reports"), on British spelling, on the shape
  of the panel text and on the voice. Lesson 8 opens by naming what lesson 7
  computed; lesson 9 names "the error of the previous lessons".

## What the course teaches badly, or wrongly

1. **`belief-truth-and-justification` states the two directions of failure
   backwards.** The second body paragraph says that a definition "wrong in
   the first way" (a condition is not necessary) "lets in cases that are not
   knowledge and is called too broad", and that one wrong in the second way
   (the conditions are not jointly sufficient) is too narrow. It is the
   reverse: a condition that is not necessary excludes a case of knowledge
   that lacks it, which is too narrow; conditions that are not sufficient let
   in a case that has them all and is not knowledge, which is too broad. The
   lesson's own concepts ("Sufficient means no exceptions above … the claim
   that later lessons break") and its worked example (dropping a necessary
   condition makes the pair too broad) are right, and Gettier cases are
   failures of sufficiency that the next lesson correctly calls too broad, so
   the paragraph contradicts everything around it. A reader who learns the
   directions from this paragraph fails the closing standard of this lesson
   and of the next two. This was the most serious defect in the course.
2. **`the-lottery-paradox` promises three principles and three exits that
   do not correspond.** The body lists three principles (accept what is
   probable enough; never accept a set known not to be all true; accept the
   conjunction of what you accept) and says "the exits are the three ways to
   give one up". But the three exits it then lists are: give up the
   threshold; give up closure; deny that statistical evidence yields
   acceptance, which is a restriction of the threshold rule, not a rejection
   of the second principle. Nobody gives up the second principle; the exit
   that keeps the threshold gives up closure and the second principle at
   once. The quiz, the course `how_to` ("which of two reasonable principles
   to give up") and the preface lesson all assume two principles. The
   framing has been rewritten as two principles and one fact, with the third
   exit named as a restriction of the first principle.
3. **The seam shows in notation.** `conditional-credence-and-base-rates`
   defines conditional credence as `c(A | B) = c(A ∧ B) / c(B)`, then uses
   `P(D | +)` for the rest of the lesson, and `updating-on-evidence` uses
   `P(H | E)` without comment; the course key and the path key both use P.
   Two letters for one quantity in one lesson, with no sentence bridging
   them, is a stall for a reader meeting probability notation for the first
   time, which the path's prerequisites say this reader is. The four spoken
   forms in `content/spoken/philosophy_c2_knowledge.py` existed only to
   pronounce the lower-case c. Unified on P, with one sentence saying that
   credences are written with P because they obey the probability rules.
4. **Odds are used before they are defined.** `updating-on-evidence` says the
   posterior odds equal the prior odds times the factor and then converts
   "3 to 1" into 3/4 as if the reader knew how; `testimony-and-independent-witnesses`
   leans on the conversion in its worked example and in three quiz
   explanations ("without turning odds into a credence"). Nothing earlier in
   the path defines odds. One sentence in the Bayes-factor definition now
   does.
5. **Lab syntax quoted as math is read aloud as mathematics.** "The lab takes
   `~` for `¬`" (`gettier-cases-and-the-fourth-condition`), "Type `->` for
   `→` and `~` for `¬`" (`skepticism-and-the-closure-argument`, panel) and
   "the lab takes `&` for `∧`" (`belief-truth-and-justification`) render the
   tilde as a math run whose read-out is "is approximately", which the built
   page confirms (`data-say="is approximately"`). PLAN §D.4 forbids exactly
   this; the syntax is now described in words.
6. **Small inaccuracies.** `the-regress-of-justification` says "a set of
   claims over six letters"; there are five letters and six sentences.
   `gettier-cases-and-the-fourth-condition` says "the lab confirms … no
   formula over J, T and B can fit this table", but the lab's search tries
   formulas of at most two conditions; the general claim follows from the
   duplicate rows, not from the search, and the sentence now says so (the
   same overclaim in its second mistake is fixed). `updating-on-evidence`
   says "the factor does not depend on the prior", which is true only with
   two hypotheses, as the definition one paragraph earlier implies. The
   course `assumes_long` lower-cased the title of Arguments and Validity,
   which PLAN §E says to name by title; `how_to` said "the last four
   lessons" and listed three. `reference-classes-and-statistical-evidence`
   had "has the higher success rate than".
7. **A quiz distractor that is partly true.** In
   `conditional-credence-and-base-rates`, the friend who says "99% accurate,
   so 99% chance" is asked what is missing, and one distractor is "the
   specificity, because only the sensitivity was used". The friend's
   reasoning does omit the false positive rate as well as the base rate, so a
   careful reader can argue for it. Replaced by a distractor that is wrong
   for a reason the lesson teaches (that `P(D | +)` is a share of the
   negatives).

## What it claims to teach but does not, and where a learner gets stuck

- **`credence-and-the-dutch-book` shows four tiles and explains one.** The
  credence lab prints Accepted, P(all accepted), The accepted set and Dutch
  book; with the threshold at 1 the first three read "0 of 2", "1" and
  "Consistent", and the lesson never mentions a threshold or acceptance. A
  reader on the first credence lesson has no way to know those tiles belong
  to lessons five and six ahead. The panel text now says which tile to read
  and whose the others are. The same applies to Adjusted and Verdict in
  `reference-classes-and-statistical-evidence`, whose "Reversal" on the
  kidney preset the body explains only obliquely; the panel now names it.
- **`reliabilism-and-the-clairvoyant` carries two targets.** The knows-table
  and the justified-table are the right pair of tables, but the lesson asks
  the reader to hold two definitions, two targets, four cases and a fifth
  case outside the table. It is within the PLAN's design and the structure is
  the one taught in the two lessons before, so it is left as it is; a reader
  who skipped `belief-truth-and-justification` will stall here, and the
  course `how_to` already says to work forward.
- **The lottery and preface labs share a kit, and the preface tile prints a
  200-digit fraction.** The exact value of (99/100)¹⁰⁰ is pinned, and the
  lesson says "the lab prints the exact fraction"; it does, and it is
  unreadable. This is the kit's honesty rather than a defect of the lesson,
  and the prose gives "about 0.37" beside it.

## Prerequisite order

Checked backwards against Arguments and Validity: validity and the form names
(`skepticism-and-the-closure-argument`) are taught in “Validity by Truth
Table”; models, consistency and the minimal inconsistent subset
(`the-regress-of-justification`) in “Consistency and Belief Sets”; the
connectives in `P(A ∧ B)` in “Truth Values and the Connectives”. Within the
course, credence is defined before conditional credence, conditional credence
before updating, the Bayes factor before the witness, and the threshold rule
before the lottery. The only internal gap was odds (item 4 above). No
violation sits in the earlier course.

## Philosophical accuracy

Positions are attributed correctly where they are attributed: Gettier's
coins, Russell's stopped clock, BonJour's Norman (unnamed as BonJour's, which
is fine), Dretske's zebra, Moore's proof, Agrippa's trilemma, Hume on
miracles. The fake barns are given without Goldman's name, the lottery without
Kyburg's and the preface without Makinson's, which the course's `not_covered`
licenses. Reliabilism gets its reply to Norman (no reason to doubt the
faculty) and to the twin (record the verdict as no); the skeptic gets a valid
argument and the charge that Moore begs the question is reported as a charge,
not a verdict. The Dutch book argument's own controversial premise is stated
in the lesson's note. The one accuracy defect was the reversed directions in
lesson 1, above.

## Changes made

- `__init__.py`: `assumes_long` names Arguments and Validity by title;
  `how_to` says "the last three lessons".
- `belief-truth-and-justification`: the too-broad / too-narrow paragraph now
  runs the right way and says which claim this lesson tests and which the
  next breaks; the ampersand is described in words.
- `gettier-cases-and-the-fourth-condition`: the search's scope stated
  honestly in the body and in the second mistake; the tilde described in
  words.
- `reliabilism-and-the-clairvoyant`: both fitting formulas named (`R ∧ E`
  and `E ∧ T`) where the body reports the search.
- `skepticism-and-the-closure-argument`: the panel describes the lab's
  syntax in words.
- `the-regress-of-justification`: "six claims over five letters".
- `credence-and-the-dutch-book`: the panel says which tile this lesson reads
  and where the other three are explained.
- `conditional-credence-and-base-rates`: the definition written with P and a
  sentence saying why; the partly-true quiz distractor replaced and its
  explanation rewritten.
- `updating-on-evidence`: odds defined inside the Bayes-factor definition;
  "with two hypotheses" added to the prior-independence claim.
- `reference-classes-and-statistical-evidence`: "a higher success rate";
  the panel names the Verdict and Adjusted tiles.
- `the-lottery-paradox`: the principles paragraph, the exits list, the fifth
  step and the standard rewritten around two principles and one fact.
- `part_b.py`: straight apostrophes in prose replaced by the typographic
  apostrophe `part_a.py` uses throughout (case names that reach tiles are
  untouched).
- `content/spoken/philosophy_c2_knowledge.py`: the four lower-case-c entries
  removed with the notation they pronounced; the file documents that every
  run in the course is now spoken by the rules.

## Remaining issues

- `reliabilism-and-the-clairvoyant` is the heaviest lesson in the course
  (two targets, two theories, a case outside the table). It is one lesson by
  PLAN §C and the URL space is fixed; if the Subject is ever re-cut, the
  justified-table and the chicken sexer are the natural second half.
- The `credence` kit prints every tile in every kind, so the Dutch book
  lesson and the lottery lesson each show tiles that belong to the other;
  the panel text now explains them, but a kit change (hide the tiles the
  kind does not compute) would remove the need. That is `@lab` work, not
  course work.
- `credence-and-the-dutch-book` uses "even", "one", "even or one" for the die
  preset where PLAN §C says "even", "at least five", "even or at least
  five". The instance differs in the events, not in what it shows (a gap of
  1/6 on three events), and the pinned tile is read from the page; left as
  written and recorded here.
- The preview had to be run through a shim: another course's `part_b.py` was
  mid-edit with a syntax error at the time, which breaks the import of the
  whole package. Nothing in this course depends on it.
