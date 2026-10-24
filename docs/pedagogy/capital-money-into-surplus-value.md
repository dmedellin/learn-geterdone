# Pedagogy assessment — From Money to Surplus Value (Capital, course 2)

Formed from the ten lesson dicts in `content/capital/c02_surplus_value/`
(`part_a.py`, lessons 1–5, Chapters 4 to 8; `part_b.py`, lessons 6–10, two
lessons on Chapter 9, two on Chapter 10, one on Chapter 11; `__init__.py`, the
course dict), and the kit they render through (`scripts/mathpath/labs/capkit.py`,
modes `circuit`, `surplus`, `workday`; views `formula`, `markup`,
`labour-power`, `mill`, `transfer`, `rate`, `senior`, `absolute`, `limit`,
`mass`), on branch `feat/capital-subject` before the Subject was wired into the
site. The design authority is `docs/capital/PLAN.md` §0, §B, the Course 2
entries in §C, §D as summarised in `docs/capital/kit-a-report.md`, §E (how a
passage is quoted) and §F (the voice); the model for this document is
`docs/pedagogy/capital-commodities-and-money.md`, and Course 1 is the voice
reference.

Every lesson was read in full before anything was changed. Every pinned tile
(31 strings on ten pages) was read off the rendered page with `node
scripts/labcheck.js --observe` after `scripts/preview_subject.py capital
--course capital-money-into-surplus-value`; every figure in prose, worked
lines and quiz was recomputed by hand; and every phrase in `&ldquo;…&rdquo;`
(119 segments) was searched for character by character in
`/mnt/project-files/capital-texts/volume-1-kerr.txt` with a case- and
punctuation-sensitive checker. Every `data-say` on the ten pages was scanned
for a spelled-out word. Lessons, in course order:
`the-general-formula-for-capital`, `contradictions-in-the-general-formula`,
`buying-and-selling-labour-power`, `the-labour-process-and-surplus-value`,
`constant-capital-and-variable-capital` | `the-rate-of-surplus-value`,
`seniors-last-hour`, `the-working-day-and-surplus-labour`,
`the-struggle-for-a-normal-working-day`, `rate-and-mass-of-surplus-value`.
The bar marks the seam between the two modules. The course assumes
Commodities and Money and school arithmetic with fractions, and is judged
against that.

## Verdict

The course teaches its subject and is fit to ship. A reader who finishes it
can name a circuit from what stands at its ends and compute ΔM; show that a
ring of mark-ups leaves the sum of values where it was and that a cheat's gain
is another's loss; value a day's labour-power from a bundle bought on three
schedules, with children and training; do Marx's yarn arithmetic for six hours
and for twelve and find the 3s; classify a capital's outlays as c or v and
compute what a £1,000 machine with a 1,000-day life passes into a day's
product; compute s/v and divide 20 lb of yarn into 16, 2 and 2; recompute
Senior's last hour on his own figures; compute the rate for any day and the
day that gives a stated rate; compute what a legal limit does to the rate at a
fixed value of labour-power; and compute the mass of surplus value and the day
a halved workforce would need, up to the day that cannot exist. Those are the
acts the `standard` fields and the six course `outcomes` name; no objective is
"understand X". Every `mistakes[0]` is the §C misconception and each is refuted
with a tile: `£0` for the corn against `−£10` for the cotton let go cheap;
`£300` before and after; `6 h` "whatever length of day follows"; `0s` in the
six-hour preset with the spindle and cotton present; `£10` passed in a day and
`£1` passed in a day, both constant; `1/9 = 11.11%` against `1 = 100%`;
`19/23 = 82.61% (Senior: 0)`; `1/6`, `1 = 100%`, `2 = 200%` on 7, 12 and 18
hours; `2/3 = 66.67%` under the ten-hour limit; `150s` twice from 100 workers
at 50% and 50 at 100%. All 31 pinned strings matched the lab, and every figure
in prose agreed with the lab, with a recomputation, or with the Kerr text.

Fidelity to Chapters 4–11 is high. 115 of the 119 quoted segments were found
verbatim; the other four differed only in the capital that opens a clause, and
are now exact. Nothing was quoted from memory. The author's two reports about
the Kerr text of Chapter 9 are both confirmed at line 2043: the rate after a
one-hour cut is printed "82 14/32%", which is a misprint for 82 14/23% (19/23
= 0.82609), and the cut is introduced as "a reduction of the hours of labour
from 11½ to 10" while the sum that follows takes one hour, 5¾ to 4¾. The
lesson says both, the §C entry says both, and the lab shows both cuts. Marx is
presented, not endorsed: the merchant's services and risk (lesson 1),
Condillac, Torrens and the marginal-utility reading of gains from trade
(lesson 2), the marginal-productivity theory of wages and the "custom" reading
of the historical and moral element (lesson 3), Böhm-Bawerk's interest theory
behind the abstinence joke (lesson 4), the productivity of machines (lesson
5), the two readings of "exploitation" (lesson 6), Senior's stronger form and
the mill-owners' fixed costs (lesson 7), the labour–leisure account of hours
and the ironmasters' frankness about idle furnaces (lesson 8), the employers'
petitions, the Tory motive and the historians' additions (lesson 9), and
Böhm-Bawerk's 1896 attack on the Volume III solution (lesson 10) are each
given two or three sentences at strength before Marx's reply, and no lesson
tells the reader what to conclude. The repairs needed were small: four case
mismatches inside quotation marks and one quiz distractor whose `why` named a
figure the arithmetic does not produce. Nothing needs splitting, merging or
reordering.

## The voice, judged against §F and Course 1

The course keeps the register Course 1 set, and in two places improves on it.

- **The passage first, then its phrases in order.** Every body opens with the
  `<strong>Volume I, Chapter n[, §m].</strong>` block and returns to it:
  "Now read the passage clause by clause. First, 'as a free man he can
  dispose of his labour-power'… Then, 'he has no other commodity for sale'"
  (lesson 3); "Read the twelve-hour sum line by line" (lesson 4); "Read the
  passage now. Capital is 'dead labour'" (lesson 8); "Read the passage's last
  clause again: a 'compound ratio' of two factors" (lesson 10). Lesson 2
  opens with the chapter's verdict and reads backwards through the cases
  that lead to it, and its `read_intro` says so, which is the right shape
  for a chapter that is a process of elimination.
- **Scenes only where the object is in the reader's life, and none forced.**
  "You sell something you no longer need, an old bicycle say" (lesson 1);
  "Shops mark goods up" (lesson 2); "Think about the last thing you bought
  that was made in a factory" (lesson 4, the §F exemplary paragraph, used
  nearly as written); "Every company report gives its profit as a percentage
  of the capital employed" (lesson 6); "Most people's working day is set by a
  contract, a law and a habit, and so it feels like a fixed quantity, like
  the length of an hour" (lesson 8). Each reaches the chapter's category in
  the same paragraph. Lessons 5, 7, 9 and 10, whose objects are not in
  anyone's life, open with the text or with a person, as §F rule 2 asks.
- **The history of the argument as a story with people in it.** This is the
  course's best feature and it is better than Course 1's. Senior gets the
  full scene §F rule 3 asks for: Drummond Professor, the 1833 Act and the
  ten-hours agitation, the Letters of 1837, the 23 half-hours, "The
  exclamation mark is Marx's", and Wilson raising the cry again in the
  Economist in 1848. Condillac is "the eighteenth-century French philosopher"
  who built a theory of trade on gains in use-value; Torrens "the economist
  and soldier"; Rossi "the Italian economist who taught at the Collège de
  France" who called labour-power apart from subsistence a phantom; Carey
  "the American economist who argued that the interests of capital and
  labour are in harmony"; the Paisley thread manufacturer who wrote to a
  Glasgow paper in 1849 that a ten-hour law would shrink every 12 spindles to
  10. Each is given the fact his view rests on before Marx replies.
- **Second person, warm, in `p` and `worked.intro` only.** "You want each
  circuit's name and its increment"; "You want the yarn's value and the
  surplus"; "You want the mass now, and the day the 50 must work". `steps`,
  `standard`, quiz items and tile text stay impersonal. No "Let's", no "dive
  in", no first-person anecdote anywhere on the course.
- **One light remark, Marx's before the lesson's.** Lesson 4 gives the
  capitalist's comic scene ("ducks and drakes", the overlooker and manager
  hiding their smiles, the professors "who are paid for it") and adds
  nothing of its own; lesson 3 points at the digestion joke; lesson 7 at
  "all bosh" and "think on the Oxford Professor"; lesson 6 at the "pleasant
  surprise to Mr. Carey". None is at the reader's expense.
- **The limit admitted.** Every `note` names what the lab cannot show, and
  the moves are varied as the Course 1 review asked: the lab "cannot say
  where the £10 came from, and Chapter 4 does not either" (1); the ring "is
  the lab's model of Marx's assumption that every seller is also a buyer"
  (2); "The bundle is the lab's input, not its output" (3); the accounting
  "assumes commodities sell at their values, and this lesson leans on it"
  (4, and 6, the two lessons §F rule 6 names for it); the machine "wears out
  evenly, a thousandth a day, which is Marx's average and not a fact about
  machines" (5); interest and obsolescence "are the strongest part of the
  manufacturers' case" (7); "The lab holds the value of labour-power fixed,
  and the history did not: wages were cut by a quarter as the hours fell"
  (9). "This Subject does not settle it" appears nowhere; the course `how_to`
  carries the point once.
- **Pointing forward by title.** Every body ends with one sentence naming
  the next lesson by its exact title; lesson 10 ends with the next course,
  Relative Surplus Value, and its question ("leave the day alone and shorten
  the necessary part of it"). The seam between the modules is invisible:
  lesson 5 ends "the surplus can be measured against the part of capital
  that produced it", and lesson 6 opens with that measure.

What later courses should copy from here rather than from Course 1: the
Senior lesson as the template for a chapter that is an argument with a named
opponent (scene, the opponent's own figures, Marx's recomputation, the
opponent's stronger form, the lab doing both), and the `note` fields' habit of
naming the simplification in the lab's own terms ("the relay preset models
evasion as a limit that falls back to the 15-hour factory day").

## What the course teaches well

- **One hard idea per lesson, and Marx's own chapter splits respected.**
  Chapter 9 is two lessons, the rate and Senior, as §B requires, and the
  first ends exactly where Senior's error begins ("an easy step from it to a
  very wrong belief, which is the next lesson"). Chapter 10 is split at §5,
  the limits of the day and then the struggle over them; the second lesson
  says in its `concepts_intro` that "The arithmetic is short; the dates
  matter", which is honest about what the lab can carry.
- **Marx's own figures, checked, and labelled as his.** Every "Marx's" preset
  label carries the chapter's instance and the text confirms each: the
  quarter of corn for £3 and the 2000 lb of cotton for £100 and £110; A's £40
  of wine for B's £50 of corn; 6 hours and 3s; 10 lb of cotton at 10s, 2s of
  wear, and the twelve-hour 27s → 30s; the £1,000 machine over 1,000 days;
  c 410 / v 90 / s 90 and 20 lb of yarn as 16/2/2; 11½ hours and 5¾, 126
  2/23% and 19/23; working days I and III of 7 and 12 hours on 6 necessary;
  the 12-hour limit of 1844, ten hours from 1 May 1848, 10½ from 5 August
  1850; 100 workers at 50% and 50 at 100% giving 150s. The 1871 mill (£378,
  £52, £510, 80/52 = 153 11/13%), Jacob's acre (£3 11s on £3 10s), the
  Wallachian 56/84, Horner's 70%, the 25% wage cut, the Court of Exchequer on
  8 February 1850, William Wood at 7 years 10 months from 6 a.m. to 9 p.m.,
  Walkley's 26½ hours and the master's "thousand a year" are all where the
  lessons say they are. Illustrative figures (the 15- and 18-hour days, the
  three dealers, the split of the 6-hour bundle) are called illustrative.
- **The misconceptions are the chapter's, refuted with the specific figure.**
  Lesson 2's ring is the right model for "every seller is also a buyer", and
  the `merchants` preset answers the obvious reply ("but the dealers do mark
  up") by adding the one party who does not and showing where the £10 came
  from. Lesson 6's `whole-capital` preset makes the 90/500 error visible on
  the yarn (`1/9`) and the status line prints s over the whole capital for
  every preset, so the two ratios are side by side as the `panel_intro`
  promises. Lesson 10's two Marx presets print the same `150s` with different
  rates, and the `limit` preset stops at 18 hours with the lab's refusal past
  24 named in the prose.
- **Worked example, faded guidance, independent practice.** Every worked
  example is Marx's own case by hand; every `panel_intro` asks for an
  observation before the press ("Watch which tile moves in each preset";
  "Try leaving out the clothes and the furniture"; "Try 50 workers and keep
  lengthening the day"); every quiz asks the same act on a fresh instance
  (cloth at £200 and £230; four traders at 10%; a bundle of 4, 14/14 and
  730/730; a loom of £600 over 1,200 days; 40 workers at 3s). The
  distractors are the named errors: the half-increment `+£15`, the `£440`
  that counts mark-ups received and not paid, the `18%` and `About 22%` that
  are s over C and s over c, `23/19` divided the wrong way, `24 hours` for
  doubling the whole day, `5/6` as the ratio of the two days. Every one was
  argued for and could not be defended.
- **The arithmetic is right throughout.** Spot checks: 20 · 20/30 = 13 1/3
  lb of yarn for the cotton and 20 · 4/30 = 2 2/3 for the wear; 8 h, 1 h 36
  m, 1 h 12 m, 1 h 12 m sum to the 12-hour day; 13 − 5¾ = 7¼, 29/23 =
  126.087%; 10 − 5¾ = 4¼, 17/23 = 73.91%; 200% on 5¾ necessary is a 17¼-hour
  day; 3,650/10,950 = 1/3; 60 min × 5 + 40 = 340 min = 5 h 40 m, × 50 weeks
  ÷ 10½ h = 27 days; 100 workers × 24 h × ½s = 1,200s; 500 × 6 = 3,000
  surplus hours against 100 × 18 = 1,800; 25 workers need 400% and 6 + 24 =
  30 hours. The lab's `suS` is product less capital advanced, so the waste
  preset's `1s` (30 − 29) is computed as the lesson explains it.
- **Prerequisites run forward correctly.** C–M–C and value as labour-time are
  taken from Course 1 and named; "The Twofold Character of Labour" is cited
  by title where Chapter 8 leans on it; fixed and circulating capital are
  named as Volume II's and deferred; the composition of capital, relative
  surplus value, wages as price and prices of production are each named,
  deferred to the course that carries them, and listed in `not_covered`.

## What it taught badly, or said wrongly

### Fidelity

- **Four quotations differed from the text in case only**, all in `part_a.py`:
  "Commodities are not paid for twice over…" (Kerr l. 1521 has "But
  commodities are not…"); "As a free man he can dispose of his labour-power"
  and "He has no other commodity for sale" (l. 1592, both lower-case clauses
  inside Marx's sentence); "the process disappears in the product" (l. 1669,
  "The process…"). None is a misquotation of sense, and the module docstring
  reserves the right to print a drop capital as an ordinary capital, but
  these are not drop capitals: three promote a clause to a sentence and one
  demotes a sentence to a clause. Repaired: the Condillac sentence now runs
  "…together, and that 'commodities are not paid for twice over…'"; the
  clause-by-clause paragraph now reads "First, 'as a free man…' … Then, 'he
  has no other commodity for sale'"; and "At the end, 'The process
  disappears in the product'." The checker reports 119 segments, 0 misses.
- **The Chapter 9 misprints** the author reports are confirmed at Kerr l. 2043
  and are correctly described in the lesson, its `note` and §C. No change.

### Quiz

- **`buying-and-selling-labour-power`, quiz 1, distractor 2:** "18 hours" was
  explained in the `why` as "spreads only the furniture", but 4 + 14 + 730/730
  is 19, not 18; a reader who made exactly that error would find no option
  for it and could argue the keyed set was incomplete. Now "19 hours", and
  the `why` says it "spreads only the furniture and counts the clothes
  whole". Every other distractor on the course was recomputed and stands.

### Speech

Every `data-say` on the ten rendered pages was scanned. No run is spelled out
letter by letter: the course's key lines open with `C–M–C`, `ΔM`, `value`,
`rate`, `mass`, `s / v`, `working day`, `labour-power`, `free`, `plus`,
`relays`, years and hours, never a three-letter word; `cwt` does not occur;
math in `steps` is in backticks where it is math (`c/(c + v + s)`). Nothing to
repair.

## Can a first-time reader of Chapters 4–11 follow the ten lessons?

Yes, and the course is easier going than Course 1 because the chapters are.
The places a reader will slow down are the right ones.

- **Lessons 1–2** are light and correctly light: one quantity each (ΔM; the
  totals before and after). Lesson 2 carries the most history (Condillac,
  Torrens, Franklin, Aristotle, Asia Minor, Rhodes) and keeps it to a
  sentence or two each, which is the chapter's own proportion.
- **Lesson 3** is where the Subject's central distinction is made, and the
  lesson makes it twice: once in the `def` (capacity, not use) and once in
  `mistakes[0]`, with the tile that cannot move. The averaging paragraph
  gives Marx's 365A + 52B + 4C over 365 in words before the lab's simpler
  per-item spreading, and the `note` says where the two differ (7 days
  against 52/365).
- **Lesson 4** is the hinge of the course and is the best lesson on it. The
  §F exemplary paragraph opens, the labour process is given its one paragraph
  and its one joke (the architect and the bee), the six-hour and twelve-hour
  sums are each read line by line, and the comic scene is placed between
  them where Marx puts it. The marginal-product refusal is named here, as §F
  says it should be, and the next lessons do keep it in view.
- **Lesson 5** asks the reader to hold two properties of one act of labour
  apart, and the two "change one thing at a time" paragraphs (sixfold
  productivity; sixfold price) do that before the definitions arrive. The
  constant-not-fixed misconception is refuted with the preset in which
  cotton passes `£10` in a day and the machine `£1`.
- **Lesson 6** is where readers argue about the word "exploitation", and the
  lesson stops to argue it fairly. The 8/10ths passage and the time
  reckoning are both given, and the time reckoning is explicitly the bridge
  to Senior.
- **Lesson 7** is a scene, and reads as one. The reader is given Senior's
  arithmetic in full before Marx's, which is what makes the recomputation
  land.
- **Lessons 8–9** carry the chapter's weight of testimony, and the lessons
  select rather than summarise: Wood, the bakers, Walkley, the blacksmith,
  the minutes table, the ironmasters; then the statutes, the five Acts, 1844,
  1847, the relays, the Exchequer and the compromise. The arithmetic in each
  is one line, and the lessons say so.
- **Lesson 10** multiplies and finds the ceiling, and closes the course where
  Marx closes Part III, pointing at Volume III's contradiction and at the
  next course's other way of enlarging the surplus.

## Repairs made in this pass

In `content/capital/c02_surplus_value/part_a.py`:
`contradictions-in-the-general-formula` the Condillac paragraph (quotation
case); `buying-and-selling-labour-power` the clause-by-clause paragraph (two
quotation cases) and quiz 1's second distractor and `why`;
`the-labour-process-and-surplus-value` the Section 1 paragraph (quotation
case). Nothing in `part_b.py` or `__init__.py` needed changing. No preset,
`expect`, slug, module, lab key, mode or view changed, and no §C entry needed
correcting: every instance the lessons carry is the one §C records, and the
two Chapter 9 textual notes in §C are confirmed against the text.

Slugs, lesson count, modules, lab keys and modes are as PLAN §B and §C list
them. `scripts/preview_subject.py capital --course
capital-money-into-surplus-value` reports OK: 11 pages rendered, 10 labs
executed and swept, 10 with pinned figures, 0 failing; the strict quotation
checker reports 119 segments, 0 misses.

## Remaining issues (recommended, not changed)

- **"Marx's peasant" is the lesson's character, not Marx's.** Chapter 4's
  corn-seller is an "I" with a quarter of corn; the lesson, the preset label
  and the worked lines call him a peasant. Harmless and within §F's licence
  for a scene, but a reader following in the book will not find the word. If
  a later pass prefers strictness, "Marx's corn-seller" fits the label and
  the lines without touching any `expect`.
- **`the-struggle-for-a-normal-working-day` has the thinnest lab on the
  course.** Its four presets are one 12-hour day under four limits, and the
  `relay-dodge` preset is the `before` preset with a larger limit. The lesson
  is honest that "the arithmetic is short; the dates matter", and §C fixes
  the instance, so nothing was changed; but a `limit` view that took a wage
  cut as an input (necessary hours falling with the wage) would let the lab
  show the thing the `note` says it cannot, that the manufacturers cut wages
  25% as the hours fell. That is a kit change and belongs to the kit's
  owner.
- **The `senior` view's second tile always cuts one hour.** For the
  `thirteen` and `ten` presets `suLastHour` prints a further hour cut (25/23,
  13/23), which is correct and labelled "After cutting one hour", but no
  sentence in the lesson explains those two strings and a reader pressing
  those presets sees figures the prose never names. The two pinned strings
  are the lab's and are right; one sentence in the lab paragraph ("the second
  tile takes a further hour off whichever day is set") would close the gap.
  Left for the author, since the §C pins are `suRate` and `suLastHour` for
  all three presets and the author may prefer to say it in the
  `panel_intro`.
- **The week-to-day conversion in lesson 3** is the lab's (an item lasting 7
  days) rather than Marx's (52 weeks over 365 days), and the `note` says so.
  A `labour-power` view that accepted "every 7 days" as 52/365 would match
  the text exactly; the difference is 1 part in 365 and does not reach any
  pinned tile. Recorded for the kit's owner.
