# Pedagogy assessment — The Turnover of Capital (Capital, course 7)

Formed from the eleven lesson dicts in `content/capital/c07_turnover/`
(`part_a.py`, lessons 1–6, Volume II, Chapters 7–12; `part_b.py`, lessons 7–11,
Chapters 13–17; `__init__.py`, the course dict), the Course 7 block of
`content/spoken/capital.py` (39 spoken forms), and the kit they render through
(`scripts/mathpath/labs/capkit_b.py`, mode `turnover` in views `time`, `fixed`,
`aggregate`, `classify`, `working`, `advance`, `annual`; and `capkit.py` mode
`circuit`, view `realise`, for the last lesson), on branch `feat/capital-subject`
before the Subject was wired. The design authority is `docs/capital/PLAN.md` §0,
§B, the Course 7 entries in §C, §D as summarised in `docs/capital/kit-b-report.md`,
§E (quotation) and §F (voice); Course 1 is the voice reference and
`docs/pedagogy/capital-commodities-and-money.md` the model for this document.

Every lesson was read in full before anything was changed. Every pinned tile
(49 strings on eleven pages) was read off the rendered page with `node
scripts/labcheck.js --observe` after `scripts/preview_subject.py capital --course
capital-turnover-of-capital`; every figure in prose, worked example, quiz item and
`mistakes` entry was recomputed by hand; every quotation and every phrase inside
`&ldquo;…&rdquo;` (87 segments) was run through the strict quotation checker
against `/mnt/project-files/capital-texts/volume-2-kerr.txt` and the three whose
first hit fell outside the chapter cited were located by hand; and Chapters 7–14
were read whole in the Kerr text, with the passages of Chapters 15–17 that the
lessons lean on read in place (the §1 example, the hollow skulls, the conclusions
and Engels' note of Chapter 15; capitals A, B and C, the Ricardian school and
§§2–3 of Chapter 16; Tooke, the four subterfuges, the farmer, the gold producers
and §2 of Chapter 17). Every math run on the twelve rendered pages was read from
its `data-say`. Lessons, in course order: `turnover-time-and-number-of-turnovers`,
`fixed-and-circulating-capital`, `aggregate-turnover`,
`physiocrats-and-adam-smith`, `ricardo-on-fixed-and-circulating-capital`,
`the-working-period` | `the-time-of-production`,
`the-time-of-circulation-in-turnover`, `turnover-time-and-capital-advanced`,
`the-turnover-of-variable-capital`, `the-circulation-of-surplus-value`. The bar
marks the seam between the two modules. The course assumes The Circuits of
Capital and the c/v/s of From Money to Surplus Value, and nothing else.

## Verdict

The course teaches its subject, and it does what the brief doubted could be
done: eleven lessons on the driest Part of Volume II stay alive without a single
invented scene, because every lively thing in them is Marx's own. A reader who
finishes it can time a turnover and count turnovers a year, including a count
below one; compute what a machine passes on by wear and what is left in it,
with repairs folded into the wear and with a cheaper machine of the same kind;
add the wear of fixed capital to the turnovers of circulating capital and divide
by the whole advance (`27/25`); sort one capital by Smith's cut and by Marx's
and say which cut fixes the surplus value; compute the circulating capital a
twelve-week working period ties up; separate working time from production time
and see a production period fall from 52 weeks to 8 with the work unchanged; add
four months out and four months back to a turnover; compute capital I, capital
II and the capital set free by Marx's rule, including the four-against-five case
where the excess alone (`£100`) is released; compute an annual rate of surplus
value as `s′·n` and tell it from the real rate, including Marx's `10/11`; and
follow the money that realises surplus value back to the capitalists' own
spending. Those are the acts the `standard` fields name and the quizzes measure;
no objective is "understand X". Every `mistakes[0]` is the §C misconception and
every one is refuted with a tile: `£1,600 turned over on £400 advanced`,
`£1,000 a year` that adds nothing new, five turnovers for the part against
`27/25` for the whole, `£600 fixed, £400 circulating` twice with `£200` and
`£250` of surplus value, `A £250, B £500` on identical fixed shares, `£1,200`
against `£100`, `13/14` against `13/3` with the same four weeks of work, once a
year instead of twice with nothing in the factory changed, `£1,200` not `£900`,
`1,000%` and `100%` on the same `£5,000`, and `£100` realised with no outsider in
the lab. All 49 pinned tile strings matched the lab, every figure quoted in
prose agreed with the lab or with a recomputation, and the two places the brief
said are easy to get wrong are right: Chapter 15's release follows conclusion B
exactly (the whole of capital II when the working period is longer; the outlay
for the excess over the largest multiple when circulation is longer; nothing for
equal periods or a whole multiple), and Chapter 16's annual rates are Marx's
`1000%`, `100%` and `90 10/11%`, with the mass of surplus value `£5,000` in all
three cases and `£50,000` when B is put on A's footing.

Fidelity is high. All 87 quoted segments are in the Kerr text, and the lessons'
many borrowed asides were each found where the lesson says they are: Newman and
Chalmers (l. 1446), the ox and the seed, the railway lifetimes and Lardner's
`£40,000` to `£30,000` (l. 1557, 1564), the inflated dividends (l. 1630), the
"1+2.25" slip (l. 1710), Scrope's second case `1,250 + 12,500 + 50,000 = 63,750`
(l. 1732–44), the copper mine (l. 1814), the labour fund (l. 1954), Ricardo's
farmer and baker (l. 2054), Belgravia (l. 2118), Bakewell's sheep (l. 2142),
Kirchhof's 50–60 + 65–80 + 55–75 working days (l. 2170), Russia's 130–150
(l. 2174), Hodgskin (l. 2181), the 150-year forest (l. 2189), the Liverpool
sailings (l. 2234), the five London banks of 1866 and Engels' Suez bracket
(l. 2246), the hollow skulls (l. 2372), `2-9` (l. 2887), Engels' note
(l. 2889–2908), `£450` (l. 2912), the Ricardian school (l. 3052), and the
opponent of Tooke (l. 3381). The one fidelity slip found was in
`the-circulation-of-surplus-value`, where Marx's four "plausible subterfuges"
were given as three, the one left out being the one Marx treats as the most
direct begging of the question, and the quoted phrase that belongs to the first
was attached to all of them. Repaired below. Marx is presented, not endorsed:
Smith, Ricardo, McCulloch and James Mill, Scrope, Engels against Marx, and
Luxemburg against Marx each get their case at strength before the reply. The
remaining defects were local: a tile the body never explained, a key line the
voice spelled out and English would not say, a cross-reference to "the last
lesson" that pointed at the wrong lesson, a gloss on Chapter 17 §2 that said
something the section does not quite say, and three §C entries whose presets
still had no recorded instance. Nothing needs splitting, merging or reordering.

## The voice, judged against §F and Course 1

The brief for this Part is §F rule 2's exception: these lessons "open with the
passage's own figures instead" of a scene, and they do. What keeps them alive is
what §F rule 3 asks for and Course 1 established, the history of the idea told
with people in it, and here the people are all in the chapters.

**What works, and matches Course 1:**

- **Passage first, then phrase by phrase.** Every body opens with the
  `<strong>Volume II, Chapter n.</strong>` block and returns to it in order:
  "Now read the notation as Marx uses it. T is the year, t the turnover time of
  one capital, n the turnovers" (lesson 1); "Read Smith's definition phrase by
  phrase and the trouble shows. Fixed capital yields a profit 'without changing
  masters'. Circulating capital, then, is capital that does change masters"
  (lesson 4); "Read the first sentence carefully: every working hour is
  production time, and not the other way round" (lesson 7); "Notice how much
  Marx gives away in the example. The goods are made to order; they are paid
  for on arrival; there is no waiting in a warehouse at all. And still the
  capital is gone for eight months" (lesson 8). Course 1's "Read the answer
  phrase by phrase" is the same move.
- **People, from the chapter.** Quesnay "physician to the court of Louis XV"
  with his 1758 Tableau; Smith "took the distinction over in 1776 and made it
  general"; Ricardo "a stockbroker who made a fortune in government loans,
  retired to the country, and wrote the most rigorous economics of his day";
  Lardner "the Irish writer on science and railway economy"; Hodgskin "the
  radical journalist"; Bakewell "a farmer at Dishley Grange"; the London
  contractor before the 1857 committee; Tooke "the historian of prices and the
  leading critic of the Currency School"; and Engels, who in lesson 9 is given
  his own passage ("Then, in the middle of the section, the editor speaks").
  Every one of these is in the chapter the lesson reads, which is the test §F
  rule 2 sets for a scene: nothing was invented to make the Part interesting.
- **Second person where §F allows it.** "You know the working day from Volume
  I" (lesson 1); "Think of a spinning machine" (lesson 2); "Begin with the
  people" (lesson 4); "Put B on A's footing to see it" (lesson 10). Every
  `worked.intro` ends "You want…". `steps`, `standard`, quiz and tile text stay
  impersonal; no "Let's", no first-person anecdote.
- **One light remark, and Marx's before the lesson's.** The year's agricultural
  basis is "a little quaint"; Marx records the dividend trick "with evident
  pleasure" and lists the working periods "with relish"; "Marx's comment is
  dry" introduces Ricardo's "logical instinct"; the "hollow skulls" are quoted
  rather than paraphrased. None is at the reader's expense and no lesson has
  more than one.
- **The limit admitted, and varied.** Every `note` names the lab's one
  assumption: identical turnovers all year; wear spread evenly and the whole
  machine revalued at once; the capitalist's own averaging adopted "for
  comparison only"; the rate of surplus value taken as given, "exactly what an
  economist who explains profit by the productivity of all capital would
  reject"; Engels' disagreement left where it is; no credit, no hoards, no gold
  mine. The "this Subject does not settle it" move appears three times in
  eleven lessons and in three different forms ("this path computes none of
  them", "does not settle that disagreement", "the lab cannot settle it"),
  which is what the Course 1 review asked for.
- **Pointing forward by title.** Every body ends with one sentence naming the
  next lesson's question by its title; `the-circulation-of-surplus-value` names
  Reproduction of the Social Capital and its question. The seam between modules
  is invisible: lesson 6 ends "The next lesson, 'The Time of Production', turns
  to products that spend part of their making with no work done on them at
  all", and lesson 7's `concepts_intro` opens "The last chapter was about
  products that take a long time to make. This one is about products that take
  a long time while hardly being made at all."

**Where the voice is thinner than Course 1, and why that is right.** Lessons 1,
3, 9 and 10 have no everyday scene at all and open, after the passage, with the
figures. That is §F rule 2 applied to this Part; the alternative would have been
a forced scene. The one place a scene was available and taken is lesson 7's
Russian winter and lesson 6's Belgravia, both Marx's.

## What the course teaches well

- **Objectives are acts, and the drills measure them.** "Finish when you can
  count a capital's turnovers in a year" (1); "compute what a fixed capital
  transfers and keeps" (2); "total the turnover of a capital with fixed and
  circulating parts" (3); "sort a capital both ways and say which sort fixes
  surplus value" (4); "show that the fixed share does not fix the surplus
  value" (5); "compute the capital a working period ties up" (6); "separate
  working time from production time and time a turnover" (7); "compute what
  distance does to a turnover" (8); "compute the capital a business must advance
  to work without a break" (9); "compute an annual rate of surplus value and
  tell it from the real rate" (10); "say where the money for surplus value comes
  from, with figures" (11). The six course `outcomes` are the same acts.
- **One hard idea per lesson, in Marx's order.** The two economists' chapters are
  kept apart, lesson 4 carrying "where the terms came from" and lesson 5 only
  "durability against variable capital"; the three times of Chapters 12–14 get
  a lesson each; Chapter 15 is confined to capital I, capital II and the rule,
  with Marx's abandoned tables named in `not_covered` and not reproduced;
  Chapter 16's §§2–3 are given one paragraph and sent to the next course.
- **Misconceptions refuted with the figure.** "At no moment does the capitalist
  hold more than £400 of capital in this business" (1); "the machine transfers
  £1,000 a year and adds nothing new" (2); "Adding the £80,000 machine would
  give £180,000, as if the machine were replaced every year" (3); "The farm and
  mine presets split identically into £600 fixed and £400 circulating and
  produce £200 and £250" (4); "The variable capital predicts the surplus value
  every time; the fixed share never does" (5); "Not an hour of labour was saved;
  the capital simply waited less" (7); "The equal preset shows £500 and £500 and
  £0 set free" (9); "The annual rate measures how little money had to be
  advanced, not how hard anyone worked" (10). Each lesson also carries two
  further mistakes a reader actually makes: timing by production alone,
  durability as the test, adding the whole fixed capital, defining circulating
  as "changes hands", speed of return taken for fixity, confusing working period
  with working day, counting natural processes as labour, forgetting the journey
  back, dividing by the variable capital employed, calling the consumption money
  an advance.
- **The arithmetic is right.** `52/13 = 4`, `4 · 400 = 1,600`; `52/78 = 2/3`,
  `600 · 2/3 = 400`; `10,000/15 = 2,000/3` wear with `1,000/3` of repairs
  booked as `1,000`, `10,000 − 3 · 2,000/3 = 8,000`; `5,000 · 6/10 = 3,000`;
  `8,000 + 100,000 = 108,000`, `108/100 = 27/25`, `9,500 + 25,000 = 34,500 =
  69/200` of `100,000`, `2,000 + 400,000 = 402,000 = 201/50`; `1,250 + 12,500 +
  50,000 = 63,750`; `39 + 13 = 52`, `13/39 = 1/3`, `13/52 = 1/4`; `26/5,200 =
  1/200`; `52 + 4 = 56`, `52/56 = 13/14`, `4/52 = 1/13`, `4/56 = 1/14`; `8 + 4 =
  12`, `52/12 = 13/3`; `52/3 + 104/3 = 52`, `(104/3)/52 = 2/3`, `52/(104/3) =
  3/2`; `9 · 100 = 900`, `3 · 100 = 300`, `50/12 = 25/6`; `4 · 100 + 5 · 100 =
  900` with `100` set free as the outlay for `5 − 4`; `6 · 100 + 2 · 100 = 800`
  and `900 − 800 = 100` on the money market; `1,100 − 900 = 200 = 2/9 · 900`;
  `900/2 = 450`; `50/5 = 10`, `100% · 10 = 1,000%`; `50/55 = 10/11`, `5,500 ·
  10/11 = 5,000`; `5,000 · 10 = 50,000`; `500 + 100 = 600`, `500 + 50 = 550`.
  Every quiz figure recomputes: `12/4 = 3`; `(10 + 3) → 52/13 = 4`; `6,000/12 =
  500`; `12,000/8 − 12,000/12 = 500`; `3,000 + 40,000 = 43,000`, `43/40`; `200 +
  100 = 300`, `s = 100`; `D: 900`; `250 · 40 = 10,000`; `26 + 26 = 52`;
  `13/39`; `52/20 = 13/5`; `8 · 200 + 4 · 200 = 2,400`, `800` set free; `4` and
  `8`: nothing; `900 → 800`; `100% · 5 = 500%`, `2,000`; `50/100 = 1/2 → 50%`;
  `800 + 200 → 200`; `800 + 120 → 120`.
- **Marx's figures are Marx's, and labelled.** Capital A's `£2,500` circulating,
  a fifth variable, 4 + 1 weeks (l. 3016); B's `£5,000` for 50 weeks; C's
  `£5,500` over 55; the 9 + 3 weeks at `£100`; the 5 + 5 and 4 + 5 cases; 6
  weeks with circulation `3 → 2` and prices halving; `£80,000` on ten years and
  `£20,000` five times; the `£10,000` machine and 15 years booked as 10 ("chosen
  at random", and the `note` says so); the farmer's `£5,000` and `£1,000`; the
  class's `£500` and `£100`. Where an instance is illustrative (the 9/4 split of
  three months, the `£100` a week, the mill, farm and mine, the nearer market,
  the `£50`) the `note` says so.
- **Critics at strength.** Smith: "For the manager reading the books, wages and
  cotton really do come back together, with each sale, and the machine really
  does not. Marx grants all of that" (4). Ricardo: "Ricardo's position has a
  strong modern form, and it is worth stating… Piero Sraffa's edition of Ricardo
  and his own 1960 book rebuilt exactly that argument. Marx does not deny it"
  (5), and the `note` says the lab "cannot weigh Ricardo's actual question". The
  McCulloch–Mill case "at its strongest: if value is labour and the wine's value
  rose, something must have laboured" (7). Engels is quoted doubting Marx's
  release of capital and the lesson "leaves their disagreement where it is" (9).
  Luxemburg's objection is given its own paragraph with Bukharin's reply (11).
  The one critic named from outside the chapters, Bailey and Torrens as the
  Ricardians' critics of the 1820s (10), is presented as history and not as
  something Marx says, and is the history Marx tells elsewhere.
- **Worked example, faded guidance, independent practice.** Each `worked` is the
  first preset by hand; each `panel_intro` asks for a prediction ("Compare the
  last tile with the capital you typed: one moves, the other does not"; "Compare
  the second tile with the 5 you typed"; "the first tile is the same, the third
  is not"; "one tile moves a great deal, and the working time does not move at
  all"; "the third tile differs tenfold, the fourth not at all"); each quiz asks
  the same act on a fresh instance with the named errors as distractors.
- **Figures agree with the lab.** All 49 pinned strings on eleven pages matched
  the observed tiles, from `13 weeks` / `4 a year (a 52-week year)` / `£1,600
  turned over on £400 advanced` through `£1,200 = I £900 + II £300` / `£300
  each working period` / `25/6 a year (a 50-week year)` and `10 = 1,000%` /
  `10/11 = 90.91%` to `£550` / `£50`.

## What it taught badly, or said wrongly

### Fidelity

- **`the-circulation-of-surplus-value`, body:** "He disposes of three evasions
  first. That the same coins serve many purchases…; that wages flow back…; that
  money spent on fixed capital stays out for years. Each, he says, 'assumes that
  money as existing whose existence it is called upon to explain'." Chapter 17
  §1 (l. 3403–3416) gives four: the coins that serve alternately, of which alone
  Marx says the quoted sentence (l. 3408); that capitalist B's consumption
  monetises A's commodity-capital, of which he says the solution "is still more
  directly assumed… Whence does B get the money?"; the wages that flow back; and
  the fixed capital. Now four, with the quotation on the first and the second
  described in the lesson's words.
- **Same lesson, the accumulation paragraph:** "faster circulation, dishoarding
  and more gold supply the extra money" is not what §2 says first. Marx's first
  point (l. 3526) is that the additional money capital "is supplied by that
  portion of the realized surplus-value, which is thrown into circulation by the
  capitalists as money-capital, not as the money-form of their revenue. The
  money is already present in the hands of the capitalists. Only its employment
  is different." Now says so, with hoards and new gold as "the rest".

### Prose that left the lab, or the reader, unexplained

- **`fixed-and-circulating-capital`, body:** the `moral` preset's first tile,
  `£500 a year`, had no sentence; the body gave only the `£3,000` left. One
  clause added: "it passes on £500 a year instead of £1,000".
- **`the-time-of-production`, body and preset label:** the `timber` preset pins
  `tuWorkingShare` at `1/200 = 0.5%` from 26 working weeks in 5,200, and the
  body said only "turns over once a century" while the label said "a few months
  of work". Now "with six months of work in it… only `1/200` of its production
  time is work", and the label says six months.
- **`aggregate-turnover`, body:** "Point 4 then repeats the rule of the last
  lesson with new numbers" sent the reader to Fixed Capital and Circulating
  Capital for a rule (the advance is not changed by the number of turnovers)
  that belongs to Turnover Time and the Number of Turnovers. Now cited by title.

### Speech

Every math run on the twelve pages was read from `data-say`. The 39 spoken forms
the author added all do one job, reading a grouped number ungrouped (`108,000 /
100,000 = 27/25` as "108000 over 100000 equals 27 over 25", `wear = £80,000 / 10
= £8,000` as "wear equals pounds 80000 over 10 equals pounds 8000"), and every
grouped run in a key line, worked line or body is covered; no run was left
unspoken and no comma reached the voice as a pause. The `capkit_b` notation reads
well: `n = T / t` as "n equals T over t", `M…M′` as "M and so on M prime",
`S′ = s′·n` as "S prime equals s prime times n", `2/9`, `25/6`, `13/14`. One
shape read wrongly and has been repaired in the content: lesson 2's key line
`left after a years = value · (life − a)/life` read "life minus A" and was not
English either; now `left = value · (life − years used)/life`, which reads "left
equals value times the quantity life minus years used, over life". The
three-letter-word rule from the Course 1 review was checked: `set free: II, when
working > circulation` reads "set free" correctly because the word is followed
by another word rather than `=`.

### Cross-references and PLAN §C

Lessons are cited by title throughout and chapters by volume and number; the next
course by its §B title. Three §C entries carried presets with no recorded
instance, which §C says a reviewer rejects: entry 4's `farm` and `mine`, entry
5's `farmer-and-baker`, and entry 7's `timber` and the circulation weeks of the
two tanning presets. The instances the lessons use are now recorded in
`docs/capital/PLAN.md` beside those ids. No instance in the lessons disagrees
with §C; the authoring changes §C already records (`eighteen-months`, `mine`,
`different-fixed`, `ironclad`, the tanning pair, `faster-passage`, `faster-sale`
and `prices-halve`, `marx-c` and `b-at-a-pace`, the `realise` presets) are all
what the lessons carry.

## Can a first-time reader of Part II follow the eleven lessons?

Yes, and the places a reader will slow down are the places Marx's readers slow
down, which the course names.

- **Lessons 1–3** build one thing each: a period that repeats and is counted
  (1); a part of capital whose value comes back piecemeal (2); how to add the
  two speeds by putting both in money (3). Lesson 3's "Notice what happened to
  the speed" paragraph, where five turnovers for the part become `27/25` for
  the whole "because four-fifths of it is in a machine that returns a tenth of
  its value a year", is the course's best single paragraph and the one a reader
  will remember.
- **Lessons 4–5** are history and they are the lessons most likely to lose a
  reader who came for arithmetic; the course keeps them by making the lab the
  argument (the same `£600 fixed, £400 circulating` producing `£200` and `£250`)
  and by giving Smith and Ricardo their reasons before Marx's.
- **Lessons 6–8** are the three times, and they are deliberately light; a reader
  who has lesson 1 can do all three. The honest sentence in lesson 8, that Marx
  sets the selling time to zero "precisely to isolate distance", is the kind of
  reading help the Part needs.
- **Lesson 9** is where readers of Chapter 15 give up, and the lesson says so
  ("the longest and most arithmetical chapter of Part II, and Engels says it
  gave him the most trouble"), gives three concepts and one rule, and lets
  Engels speak against Marx. The crossing of the two capitals in week 13 is
  explained in one paragraph that a reader can check against the `£300 each
  working period` tile.
- **Lesson 10** rests on one distinction, advanced against employed, and makes
  it with Marx's own device of putting B on A's footing; a reader who has
  followed lesson 9 has already met capital advanced and will not confuse the
  two. Capital C is given so that "below one" is seen, not asserted.
- **Lesson 11** changes mode (to `circuit`) and changes question (from value to
  its money), and the `concepts_intro` warns of both. The farmer carries the
  argument; the `half-spent` preset is the lab's stipulation and the `note` says
  so.

## Repairs made in this pass

In `content/capital/c07_turnover/part_a.py`: `fixed-and-circulating-capital`
`key[3]` and the `moral` sentence of the lab paragraph; `aggregate-turnover` the
"Point 4" cross-reference. In `part_b.py`: `the-time-of-production` the timber
sentence and the `timber` preset label; `the-circulation-of-surplus-value` the
evasions paragraph and the accumulation gloss. In `docs/capital/PLAN.md`: the
preset instances for Course 7 entries 4, 5 and 7. No preset instance, `expect`,
slug, module, lab key, mode or view changed, and no spoken form was added or
altered. `scripts/preview_subject.py capital --course capital-turnover-of-capital`
reports OK: 12 pages, every lab executes and survives the sweep, every pinned
figure on the eleven pages matches, no math run without a spoken form.

## Remaining issues

- **Bailey and Torrens in `the-turnover-of-variable-capital`** are not in
  Chapter 16; Marx names only "the Ricardian school since the beginning of the
  twenties". The lesson presents them as history, which they are (both argued in
  the 1820s that equal capitals earn equal profits whatever their turnover), but
  a reader checking the chapter will not find them. Left as it is; a reviewer
  who wants the Subject to name only what the chapter names would cut the
  clause.
- **The wine in the cellar** (lesson 7) is McCulloch's standard case, and it is
  the case Marx has in mind, but the chapter itself names only "senseless
  theories" and promises Volume III. The lesson says "the old puzzle" rather
  than attributing the example to the chapter. Left as it is.
- **`capital I` and `II` in key lines and worked lines** are Marx's notation and
  are read by the voice as letters ("capital I", "I I"). No spoken form fixes
  this without rewriting Marx's labels; recorded, not changed.
- **Lesson 9's `tuAdvance` for the four-against-five case** prints `I £400 + II
  £500`, where Marx splits the same `£900` as I `£400`, II `£400`, III `£100`
  (l. 2837). The lesson's definition of capital II as "the weekly outlay times
  the weeks of circulation" is Marx's §1 definition and the tile is consistent
  with it; a reader following the chapter's own tables will meet a capital III
  the lesson does not name. One sentence in the `note` would close it; not
  added, because the `note` is already carrying Engels.
