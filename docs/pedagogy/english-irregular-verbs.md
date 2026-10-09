# Pedagogy assessment — Irregular Verbs (english, course 2)

First assessment, formed from the three lesson dicts in
`content/english/c2_irregular_verbs/` (`part_a.py`, `part_b.py`, `part_c.py`,
one lesson each) and the course dict in `__init__.py`, the Subject's design in
`docs/ENGLISH-SUBJECT.md`, the data the pages inline
(`content/english/data/irregular_verbs.json`, 133 rows, and
`wordorder_passage.json`, the 949-word passage), and the three kit modes the
lessons render through (`irregular`, `classes` and `irrshare` in
`scripts/mathpath/labs/english.py`), on branch `subject/english` after the kit
engineer's pass that split `classes` from `irregular` and made the class count
computed. No prior assessment exists for this course. The course declares Tense
Tables as its prerequisite and the path promises counting and shares only, so it
is judged against Tense Tables and school arithmetic.

Every figure quoted below was read off the rendered page with
`node scripts/labcheck.js --observe` after `scripts/preview_subject.py english
--course irregular-verbs` rendered it to a scratch directory, and then recounted
in Python from the same data files. The preview reported OK before any change
and OK after. All three lessons were read before any was changed; the last
sections record what was changed and what was not.

Lessons, in course order: `the-verbs-that-break-the-rules`,
`six-patterns-not-one-hundred-and-eighty`, `how-much-of-english-is-irregular`.

## Verdict

The structure is sound and the English is almost all right, but the course did
not keep the Subject's own promise on its last lesson: every figure in
`how-much-of-english-is-irregular` was a whole-novel count made offline, while
the page computes a different set of figures on a printed passage, and the
panel copy said "in the novel". Lesson one opened on a sentence that became
false when the kit stopped scoring irregular verbs as regular ("the words they
missed … this course is that list"), and carried four offline figures
(183, 132, 697.5, 44%) with no label. Every quiz keyed answer A. All of that is
fixed below. One defect remains that is the kit's, not the course's: the
`irrshare` matcher cannot see `was`, `were`, `is`, `am`, `are`, `has` or
`does`, so its central tile undercounts *be*; the lesson now says so and
reports it as the residue, and the fix is recorded at the end.

## What the course teaches well

- **Every objective is an act, and the lab or quiz measures it.** Run the
  four-step test and say regular or irregular (`the-verbs-that-break-the-rules`,
  `standard`, `steps`, quiz 1 and 4); sort a verb by asking the questions in
  order and stop at the first yes (`six-patterns-not-one-hundred-and-eighty`,
  `steps`, every quiz question); read two shares off the lab and say which the
  page computed and which it quoted (`how-much-of-english-is-irregular`,
  `standard`, quiz 1 and 4). No `standard` says "understand".
- **The definition is a test a computer can run, and the lab runs it.** An
  irregular verb is one whose past or participle is not what the *-ed* rule
  builds (`the-verbs-that-break-the-rules`); a class is a statement about which
  of three strings are equal (`six-patterns-not-one-hundred-and-eighty`). The
  `classes` widget asks the lesson's four questions of every printed row and
  the tiles agree with the prose everywhere: 60 / 37 / 21 / 9 / 4 / 1, *be*
  outside (`clOutside` 1), the vowel preset 7 with 6 in the class of nine and
  1 (*begin*) in the class of 37. The `irregular` widget's `irClasses` tile now
  reads 6, which the prose always said.
- **The near-miss is the right teaching device.** *Know/knew/known* against
  *go/went/gone* makes the point that a string rule says exactly what it does
  not cover, and *begin/began/begun* against *sing/sang/sung* shows a second
  pattern (vowels) laid across the first (letters). Both are computed on the
  page and both are stated in prose, worked example and quiz.
- **The flattering number is taken apart rather than repeated.** Lesson three
  gives the headline share, then shows that three verbs are half of it, then
  shows the top-twenty figure falling from 87.65% to 73.89% when those three
  leave. The `note` and `mistakes[0]` name the exact misreading (twenty equal
  workers) and the four `steps` are a reusable procedure for reading any share.
- **The frequency explanation is attributed and bounded.** Pinker is named for
  the 180 and for the memory account; the lesson calls the account "an
  observation more than a proof" and the `note` calls 180 "a count of
  judgement, not of measurement". That is the right epistemic register for a
  claim the page cannot check.
- **Cross-references are by title** (*Tense Tables*, "the next lesson"), the
  glossary terms (`irregular`, `participle`, `vowels`) are each defined with
  `<dfn>` before use, and every page sits above the 98% band:
  99.3 / 99.6 / 99.0% for the three lessons, 99.4% for the course home.

## What the course teaches badly, or claims and does not teach

- **The whole of lesson three was quoted, and the page said it was computed**
  (`how-much-of-english-is-irregular`). The `irrshare` lab counts irregular
  forms in the 949-word printed passage and pins 106 forms, 11.2% of the words,
  54 of them *be/have/do* (50.9%), 52 and 5.5% without them. Not one of those
  numbers appeared in the lesson. The lesson's numbers (15,192 forms, 12.29%,
  5,873 / 2,343 / 821, 9,037 = 59.5%, 6,155 = 4.98%, top twenty 87.65% and
  73.89%) are a single offline count over the novel, which at about 700,000
  characters cannot be inlined. The `panel_intro` said "the irregular verb
  forms in the novel, counted from its words" and the body said "the lab lets
  you check each one"; both were false. The course `footer_lead` said "every
  share is counted in your browser against it". Rewritten so that the passage
  count leads (summary, key, concepts, worked example, body and two quiz
  questions now carry 106 / 11.2% / 54 / 50.9% / 52 / 5.5%), every novel
  figure is introduced with "quoted" or "counted once", and a new fourth step
  ("Was it counted here, or somewhere else?") and a new quiz question make the
  distinction itself the thing retrieved. The arithmetic of the quoted figures
  was recomputed and is right (9,037/15,192 = 59.5%; 15,192/123,611 = 12.29%;
  6,155/123,611 = 4.98%; 5,873/123,611 = 4.75%).
- **Lesson one's opening became false when the data was cleaned**
  (`the-verbs-that-break-the-rules`, `body[0]`, `summary`). "The words they
  missed were a short list. This course is that list." The kit now scores the
  three forming rules on 1,210 regular verbs only; its misses are regular verbs
  with a spelling twist (*stomach*, *bus*, *panic*, *format*), not irregular
  verbs, and the 90 irregular verbs that were in the raw list were set aside
  before scoring. Rewritten: the rules were right 99.92 / 99.34 / 99.26% on the
  regular verbs, the irregular verbs were put aside first, and this course is
  the set that was put aside. The old 99.85 / 98.97 / 98.67 are gone.
- **Four offline figures with no label** (`the-verbs-that-break-the-rules`:
  183 collected, 132 in the common list, median rank 697.5, 44% in the top
  500). The page cannot recompute any of them: it does not carry the 183, and
  the NGSL file it is built from carries a band per word, not a rank. Each is
  now introduced as made once when the course was built and quoted here. The
  lab holds 133, one more than the 132 that passed the filter; the prose now
  says the list was settled by hand after the check and that all 133 are in
  the common list (verified against `scripts/wordlists/ngsl.tsv`: every base is
  in band 1–3).
- **A worked example that did not demonstrate the method**
  (`the-verbs-that-break-the-rules`). The `steps` teach a four-step test and
  the `worked` block then told the frequency story instead, so the lesson
  explained the test and never showed it. The worked example now runs the test
  on *walk*, *show* and *bring* (guess against written, one failure is enough),
  which is the faded-guidance step between the procedure and quiz 1 and 4. The
  frequency evidence stays in the body under its heading, labelled quoted.
- **A false claim about the -s and -ing forms** (`the-verbs-that-break-the-rules`,
  `steps[0]`): "follow the rules from that course even for irregular verbs".
  *Have* makes *has* and *be* has *am*, *is*, *are*; the step now names those
  two exceptions. (*Do/does* and *say/says* are spelled by the rule.)
- **Every quiz keyed answer A** (all three lessons, 10 of 10 with `"c": 0`).
  Choices reordered; positions are now 2, 1, 3, 0 / 3, 1, 2 / 1, 3, 0, 2, which
  is 2 / 3 / 3 / 3 across the four slots. No `why` named a choice by letter
  before or after; the one `why` that listed "the other figures" in order
  (`how-much-of-english-is-irregular`, quiz 1) was rewritten to name each
  figure by what it is a share of.
- **Be's forms listed wrongly** (`six-patterns-not-one-hundred-and-eighty`,
  body): "Its forms (am, is, are, was, were, been)" gave six of eight. Now "It
  has eight forms (be, am, is, are, being, was, were, been), with two in the
  past alone", which is also the count Tense Tables' "five forms" claim needs
  corrected against.
- **A loose superlative** (`six-patterns-not-one-hundred-and-eighty`, body):
  "*Gone* and *done* … are the two best-known verbs in English". *Be* is.
  Now "*go* and *do* are two of the commonest verbs in English".
- **Counts that folded *be* into the six classes** (course `blurb`, `key`,
  lesson one `key`, `summary`, `concepts[1]`, body). "133 verbs in 6 classes"
  when 132 are in the classes and *be* is outside, as the `clOutside` tile
  prints. Every such sentence now says 132 in six classes and *be* outside.
- **Course-home promises** (`__init__.py`). `outcomes[5]` stated 87.65% and
  73.89% as if the page produced them; it now says "over the whole novel,
  counted once and quoted … the page cannot recount either", and is retitled
  to the act it measures ("Tell a figure the page computes from one it
  quotes"). `outcomes[4]` now carries the page's 54 of 106 and 11.2% to 5.5%.
  The `footer_lead` now distinguishes the shares the lab prints (counted in
  the browser on the printed passage) from the whole-novel figures (counted
  once, offline, marked quoted where they appear).

## Prerequisite order

Checked backwards. Lesson one uses the *-ed* rule, its "small changes"
(doubling, as in *plan/planned*, *stop/stopped* in quiz 1) and the *-s* and
*-ing* rules, all of Tense Tables; it defines *participle* itself and does not
assume the word. Lesson two needs only "the same string of letters" and the
last letter of a word. Lesson three needs a share as a division and a
percentage, which the path's `prerequisites` promise; "median" is not used, and
the one sentence that needs the idea explains it inline ("half of them sit
among the 700 commonest"). Nothing is assumed from Word Order or Listening.
One cross-course dependency to record rather than fix: lesson one says "Four
rules build the five forms of any regular verb", which is true of regular
verbs; the Tense Tables sentence "Every verb in English has five forms, and
only five" is false of *be* and is that course's reviewer's to fix, and lesson
two here now states *be*'s eight.

## Cognitive load

One hard idea per lesson: the definition-as-test (one), the string classes
(two), the denominator trap (three). Lesson two carries a second, smaller idea
(the vowel pattern across two classes) and places it after the six classes
are settled, in its own heading and its own lab preset, which is the right
order. Lesson three now carries two parallel sets of numbers (passage and
novel); the load is kept down by giving them the same three-row shape in the
key and the worked example (all / the three / the others) so the reader
compares like with like, and by making "which one is counted here" a step and
a quiz item rather than a footnote.

## Worked-example progression

Lesson one: procedure (`steps`) → worked demonstration on three verbs (new) →
the lab, which prints the written forms for 133 verbs so a reader can build the
guess for any row → quiz 1 and 4 on *bring* and *show*. Lesson two: the four
questions → the worked near-miss (*know*, *go*, *sing*) → a lab whose summary
table shows the questions' output for every class → quizzes that sort *cut*,
*gone* and *come*. Lesson three: the four questions to ask of a share → a
worked example that applies them to the passage and then the novel → a lab
whose menu is the "count again without the biggest items" step → quiz 1 and 4.
Each lesson now demonstrates what its steps describe.

## Retrieval practice

Every quiz `why` addresses the specific wrong model rather than restating the
rule: quiz 1 of lesson one says why the three regular pairs are regular
(doubling), lesson two's *gone* question says what the rule actually looks at,
lesson three's first question says what each distractor is a share of. The
labs each ask for an act: search for a verb you use every day; read the last
letter of every row in the class of nine; search the passage for *was* and see
which tile does not move. Distractors were tried for a defensible reading;
none was found. "Its base is not the same as its past" (lesson two, quiz 2) is
true of *go* but also of *know*, so it is not a reason that separates them.

## Misconceptions

Named and corrected: a verb is irregular because it sounds odd (lesson one,
`mistakes[0]`, with *show*); irregular forms are errors that stuck
(`mistakes[1]`); the class tells you the letters (lesson two, `mistakes[0]`);
*go* belongs with *know* (`mistakes[1]`); a class of one is a rule
(`mistakes[2]`); a top-twenty share means twenty equal workers (lesson three,
`mistakes[0]`); one novel is English (`mistakes[1]`); a share of words is a
share of verbs (`mistakes[2]`). Added by this pass, as prose rather than a
`mistakes` entry: that a figure printed beside a lab was necessarily computed
by it (lesson three, `steps[3]`, quiz 4).

## English accuracy, verified and left alone

Pinker's figure of about 180 irregular verbs (Words and Rules, 1999) is
correctly attributed and correctly hedged. The six classes partition the 132
non-*be* verbs and the examples named are in the classes named: *blow, grow,
throw, fly, break, speak, steal, write* in the *-n* class; *drink, ring, sing,
sink, spring, swim* and *do, go, undergo* in the class of nine; *become, come,
overcome, run* with base = participle; *beat* alone; *put, hit, cut, read* with
all three the same (`read` with its pronunciation note). *Went* as an old form
that survived is right (it is the past of *wend*). The *-o* rule gives *does*
and the base rule gives *says*, so the two exceptions named in `steps[0]` are
the only two among the 133. The passage count was checked by hand: *have* 24,
*do* 16, *be* 14 as the page counts them; *say* 7, *know* 6, *see* 5 after.

## Changes made

- `part_a.py`: summary and opening paragraph rewritten (set aside before
  scoring; 99.92 / 99.34 / 99.26 on 1,210 regular verbs; *panic/panicking* as
  the kind of miss the rules make); `steps[0]` names *has* and *am/is/are*;
  key, concepts[1] and body say 132 in six classes and *be* outside; new
  worked example on *walk*, *show*, *bring* with `read_title`/`read_intro` to
  match; 183 / 132 / 72.1% / 697.5 / 44% kept in the body and labelled as
  counted once and quoted, with the 133-against-132 gap explained; lab
  `panel_intro` says the tiles are counted from the printed rows; quiz
  positions 2, 1, 3, 0.
- `part_b.py`: *be*'s eight forms; "two of the commonest verbs"; lab
  `panel_intro` points at the summary table and the vowel preset; quiz
  positions 3, 1, 2.
- `part_c.py`: docstring, `one_line`, `standard`, `summary`, `key_label`,
  `key`, all three `concepts`, `steps[0]` and a new `steps[3]`, lab
  `panel_title`/`panel_intro`, `read_title`/`read_intro`, `worked`, `note`,
  `mistakes[2]`, quiz (four questions, positions 1, 3, 0, 2) and body
  rewritten around the passage count, with every novel figure labelled quoted
  and a new section on what the matcher counts and leaves out. Body trimmed to
  18 entries.
- `__init__.py`: blurb, summary, outcomes[4] and [5], key[0], footer_lead.
- Verified: `preview_subject.py english --course irregular-verbs` OK (3 labs
  executed and swept, 3 pinned, 0 failing); `TestLessonDataMatchesTheRenderer`
  and `tests.test_english_kit` OK (14 tests); `bandcheck.py --report` 99.0% or
  better on all four pages; `labcheck.js --observe` tiles unchanged.

## Read-out

The spoken runs are the `key` and `worked.lines` blocks. The ones that read
badly, with the words they should be spoken as, are listed in the return to
the orchestrator, who owns `content/spoken/english.py`; in short, every slash
list (`walk / walked / walked`) is read "over", every `-n`/`-ed` is read
"negative", `go` is spelled out as "g o", and the key lines of lesson two drop
their bracketed examples. The lesson-three worked lines were reworded so that
no line is detected as a table row.

## Remaining issues, for whoever next owns this course or the kit

- The 183-verb source list is not in the repository, so the 132 / 72.1% figure
  and the rank figures (697.5, 44%) can only ever be quoted; if the rank-ordered
  NGSL were added to `scripts/wordlists/`, the lab could compute the median
  rank of the 133 and the prose could drop the label.
- `scripts/wordlists/ngsl.tsv` carries 2,859 headwords in bands 1–3; the
  Subject says "2,809" throughout. Not this course's figure to change, but the
  two should be reconciled by whoever owns the band contract.
- The top-twenty figures (87.65%, 73.89%) have no computed counterpart. A
  `shTop` tile (share of the passage's irregular forms covered by its top
  twenty verbs, with and without the three) would let the lesson's central
  comparison be made on the page as well as quoted.

## Fixes, 2026-10-08

- **The `irrshare` matcher now counts every form of the listed verbs.**
  `_irrshare` splits slash spellings (`was/were`), adds the present forms
  through the kit's own `vbThird` (so *goes*, *does*), writes out the two the
  rules cannot make (*am*, *is*, *are* for *be*; *has* for *have*), and builds
  `-ing` with the kit's `vbIng` (drop a silent *e*, double by the stress
  rule), with *being* as the one override. The page now reads 149 forms,
  15.7%; *be/have/do* 91, 61.1%; without them 58, 6.1% (read with
  `labcheck.js --observe`, and `_SH_PRESETS` pins all four tiles). *Be*
  alone is 49, *was* 20 of them. `part_c.py` and `outcomes[4]` follow; the
  section that disclosed the old blind spot is replaced by "What a match does
  not prove" (spellings, not meanings: *left*, *saw*). The page share is now
  above the novel's quoted 12.29%, and the worked example says so rather than
  calling the two the same; computed and quoted figures stay labelled apart.
