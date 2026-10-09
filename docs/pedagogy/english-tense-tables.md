# Pedagogy assessment — Tense Tables (english, course 1)

First assessment, formed from the two lesson dicts in
`content/english/c1_tense_tables/` (`part_a.py`, `five-forms-and-the-whole-table`;
`part_b.py`, `when-the-last-letter-doubles`; `__init__.py`, the course dict),
the course's lines in the path dict (`content/english/__init__.py`, the `key`),
the design they were written from (`docs/ENGLISH-SUBJECT.md` §1, §3 and §5
Course 1), the kit they render through (`scripts/mathpath/labs/english.py`
modes `table` and `doubling`, over the rule code in `english_core.py`) and the
cleaned word lists the kit inlines (`scripts/wordlists/verbrules_cases.json`,
`doubling_verbs.json`, written by `clean_verbs.py`), on branch
`subject/english` (PR #28) after the kit engineer's pass of 2026-10-08 and
before the Subject is on main. The review of PR #28 is the brief; its items 3,
4, 5 and the two false claims it names are addressed here. No prior assessment
of this course exists.

This is a generated course and the first course of its path, so it may assume
nothing: the course dict says so (`assumes_short`: "Nothing. You need to read
English and to count."), and it is judged as such. Both lessons were read in
full before anything was changed. Every figure quoted below was read off the
rendered page with `node scripts/labcheck.js --observe` (rendered through
`scripts/preview_subject.py english --course tense-tables`), then recomputed
from the data files with `/usr/bin/python3`, and the preview reported OK
before and after the changes: two labs execute and survive the control sweep,
both pages carry pinned figures and every pin matches. Every page of this
course was also run through `scripts/bandcheck.py` after the changes: course
home 99.0%, lesson one 98.9% (one glossary term), lesson two 99.7% (three), all
above the 98% floor the Subject sets for itself.

## Verdict

The course now teaches what it says it teaches, and says nothing it does not
compute. A reader who finishes it can write the five forms of a regular verb by
rule, place *have*, *be* and *will* in front of them to fill a twelve-cell
table, say which of four rules fired and why, score each rule on 1,210 printed
verbs in the browser and read the words it misses, and apply the one rule that
needs the sound of the word (the doubling rule) to a verb they have never seen,
knowing which of its misses are British spellings, which are both-ways
spellings, and which four are true exceptions.

Before this pass it did not. The course home promised a count of "which boxes
English writers actually use", which no lesson delivers; lesson one quoted hit
rates (99.85 / 98.97 / 98.67%) that no page computed, over a list (1,356
verbs) that the page did not carry, and that on inspection scored invented
forms (*comed*, *maked*) as hits; lesson two taught *offer*, *suffer* and
*council* as exceptions to the doubling rule when they were misspellings and a
non-verb in the raw data; both lessons keyed every quiz answer to the first
choice; and lesson one said "nine of the boxes" take a small word when the
lab's own grid shows ten. All of that is repaired below.

## What the course teaches well

- **Every objective is an act the lab measures.** `five-forms-and-the-whole-table`
  closes on "build the full table for a verb you have never seen, and name the
  rule that made each form"; the table lab takes a typed verb, fills the twelve
  cells and prints the rule that fired (`tbRule`: "silent -e: drop it before
  -ing", "ends consonant-vowel-consonant, stressed: double it"). `when-the-last-letter-doubles`
  closes on "say, before writing it, whether a verb doubles its last letter,
  and why"; the doubling lab scores that decision three ways on 217 verbs. No
  `standard` says "understand".
- **The method is the Subject's, and both lessons keep it.** State a rule,
  measure it on printed text, show the residue. The table lab's `Score a rule
  on the list` menu runs each rule over the 1,210 verbs inlined on the page and
  prints the hit, the share and every missed word; the doubling lab prints every
  one of its 217 rows with every recorded spelling. The reader can recount
  anything the lesson asserts, which is the promise the path footer makes.
- **A refuted rule is shown, not described** (`five-forms-and-the-whole-table`).
  The *f* → *ves* rule is a menu option; choosing it drops the `-s` rule from
  1209/1210 to 1205/1210 and puts *brief*, *golf*, *proof*, *roof* in the
  misses. The lesson's closing paragraph ("a rule can sound right, come from a
  real pattern, and still cost you accuracy") is then a report of what the
  reader just did, which is the strongest form the point can take.
- **The second lesson earns its place by subtraction.** The `-ing` rule scores
  99.34% on the whole list, doubling included; the doubling lesson shows that on
  the 217 verbs where doubling is a question at all, the textbook rule is a
  coin toss (49.3% / 50.7%) and the stress condition lifts it to 91.7%. The
  lesson names this as a measurement error a reader should learn to avoid
  ("Scoring a rule on words it cannot touch"), which is a transferable skill
  and not only a fact about spelling.
- **The residue is read, not counted.** Both worked examples list the misses
  by name and sort them into kinds. The doubling lesson's "Eleven of the
  eighteen end in the same letter" turns an exception list into a second rule
  (British final *-l*), which is the move the Subject exists to teach.
- **The voice is right and the band is kept.** Short declaratives, no "In this
  lesson you will learn", and every page inside the NGSL 2,809 at 98.9% or
  better with at most three glossary terms.

## What the course taught badly, or said wrongly

- **Figures the page did not compute** (`five-forms-and-the-whole-table`,
  summary, concept 3, worked, body; course `key`, `outcomes`; path `key`).
  99.85 / 98.97 / 98.67% and "1,356 verbs" were measured offline over the raw
  NGSL list, which the page did not carry. The kit now inlines the cleaned list
  and scores it in the browser. Observed tiles: `-s` 1209 of 1210, 99.92%,
  missed *stomach*; `-ing` 1202 of 1210, 99.34%, missed *bus, format, initial,
  input, output, panic, traffic, up*; `-ed` 1201 of 1210, 99.26%, missed *bus,
  counsel, format, initial, output, panic, traffic, up*; before the `-o` fix
  1207 of 1210, 99.75%, *radio, stomach, video*; with *f* → *ves* 1205 of 1210,
  99.59%. Every one of those is now the figure the prose states, and the
  worked example tells the reader which menu option reproduces it.
- **Exceptions that were artefacts of dirty data** (`when-the-last-letter-doubles`,
  worked lines, body, note). *offer*, *suffer* and *council* sat in the residue
  because the raw list recorded *offerring*, *sufferring* and *councilling*;
  *metal* sat there as a non-verb. The cleaned list (`doubling_verbs.json`,
  217 rows) drops them, and the counts move: 232 → 217, 22 wrong → 18, 13
  ending in *-l* → 11, and "double all" and "double none" swap places (107
  against 110). The lesson now says plainly that the list carried misspellings,
  names the three words, and points at the lab rows where the removed spelling
  is shown beside the verb it came from.
- **"Nine of the boxes" take a small word** (`five-forms-and-the-whole-table`,
  key, concept 1, body; course `outcomes[0]`). The lab's 3 × 4 grid has two
  bare cells (present simple, past simple) and ten with *have*, *be* or *will*
  in front, future simple (*will walk*) among them. The arithmetic only gives
  nine if the `-s` form is given a box of its own, which the grid does not do.
  Corrected to two and ten everywhere, and the quiz distractor "Nine" became
  "Ten" with a `why` that says what ten counts.
- **"Every verb in English has five forms, and only five"**
  (`five-forms-and-the-whole-table`, body). *be* has eight; the small helping
  words have fewer. Now: a verb has five forms; *be* has eight, listed, and the
  second course sets it apart; *will* and its kind have fewer and only ever
  stand in front.
- **A stated rule that was not the rule the lab runs** (`five-forms-and-the-whole-table`,
  body list). "Double that last letter before any of the above" would double
  before `-s` (*stopps*); `vbThird` never doubles. The `-ed` rule said "add
  -ed, with the same -y change" and never mentioned that after a silent *-e*
  only *-d* is added (*hope*, *hoped*), which `vbEd` does. And the doubling
  test in `vbDoubles` refuses a final *w*, *x* or *y*, which the prose did not
  say. All three are now stated as the code runs them, and lesson two's first
  step carries the *w*, *x*, *y* clause too.
- **A silent default the page did not disclose** (`five-forms-and-the-whole-table`,
  lab panel). For a verb not on the printed list the page has no stress mark
  and treats the last part as strong (`VB_FINAL_STRESS[v] !== false`), so a
  typed *gallop* doubles. The panel intro now says so in one sentence.
- **Every quiz keyed the first choice.** Six questions, six `"c": 0`. Now 2, 0,
  3 in lesson one and 1, 3, 2 in lesson two; no `why` refers to a choice by
  letter (checked by grep).
- **A quiz example that contradicted the lab** (`when-the-last-letter-doubles`,
  quiz 2). "Why does *admit* double but *benefit* not?" — the lab lists
  *benefit* among the rule's misses, because the list records *benefitting* as
  well as *benefiting*. A reader who had just read the lab would be told the
  word does not double by a page that had just marked it as doubling. The
  example is now *visit* (stress early, *visiting* only), and the distractors
  are each refuted in the `why` ("both end in -t, and both have two parts").
- **Two distractors that were one** (`five-forms-and-the-whole-table`, quiz 1).
  "Twelve" and "One for each box" are the same wrong answer. The second is now
  "Ten".
- **A misdescribed residue** (`five-forms-and-the-whole-table`, worked `after`,
  body). "Several are words where British and American writers simply spell
  the same verb differently" fitted the old residue. The new one is mixed:
  *initial* and *counsel* are British/American; *panic* and *traffic* take a
  *-k* no stated rule knows; *format*, *input*, *output* double against the
  stress; *bus* is *busing* where the rule writes *bussing*; *stomach* ends in
  *-ch* that does not hiss; *up* has no consonant before its vowel. Each miss
  is now named with its reason, so a reader can tell a gap in the rule from a
  gap in the list.
- **Orientation that disagreed with the lab** (`five-forms-and-the-whole-table`,
  concept 1). "Three times across the top and four shapes down the side"; the
  lab grid has times down the side. Aligned to the lab.

## What it claimed to teach but did not

- **"Which boxes English writers actually use"** (course `summary`,
  `outcomes[5]` "Say which boxes are worth your time", `syllabus_intro`,
  `not_covered[0]`; path `key` "four of the twelve tense boxes carry most of
  real writing"). No lesson computes it. `docs/ENGLISH-SUBJECT.md` records the
  measurement (progressive 1.4% over 1,951 verb phrases) but no page carries
  the phrases or the count, and the course has two lessons, neither about
  usage. Every one of those sentences is removed or replaced with something the
  course delivers: the outcome is now "Tell a spelling difference from a
  mistake", the syllabus intro names the doubling lesson, and the path key's
  course-1 lines now carry the doubling figures (49.3% as the books give it,
  91.7% with the stress), which `when-the-last-letter-doubles` pins.
- **"The word list printed with this lesson"** (`five-forms-and-the-whole-table`,
  worked intro; course `assumes_long`, `footer_lead`). False before the kit
  pass, since the page carried six verbs; true now, since the table lab inlines
  all 1,210 with every recorded spelling under `List`. The sentences stand and
  are now true, and the worked intro tells the reader which menu to open.
- **"Say which rule made a form"** (course `outcomes[1]`). Delivered: the
  `tbRule` tile prints the rule for the typed verb. Left alone.

## Prerequisite order and cognitive load

The order inside the course is right: the forms and all four rules are stated
in `five-forms-and-the-whole-table`, including the doubling rule in full (CVC,
not *w/x/y*, stress on the last part), and `when-the-last-letter-doubles` then
isolates that one rule and measures it where it can fail. A reader meets the
stress condition twice, once as a stated clause and once as the thing that
lifts a coin toss to 91.7%, which is the right amount of repetition for the one
rule the course says learners get wrong most often.

Across the path nothing earlier exists to violate. Forward references are by
title and are honest: lesson one says *be* is set apart in "the second course",
and Irregular Verbs (`c2_irregular_verbs/part_b.py`) does say *be* stands
outside its six classes; lesson one's "the 90 verbs the second course calls
irregular" matches `irregular_verbs.json`. The reverse reference in
`c2_irregular_verbs/part_a.py` already quotes 99.92 / 99.34 / 99.26 and 1,210.

Lesson one is heavy. It carries the five-form construction, four rules with
their sub-cases, the scoring idea, the cleaning of the list and the refuted
rule: that is three hard ideas (build, score, refute), and the body sits at the
renderer's ceiling of 18 blocks. The design fixes the course at two lessons and
the URL space is pinned in five places, so this is recorded rather than split.
If the course is ever extended, the cut is after "The rules that make four of
the five": a lesson on building the table, then a lesson on scoring the rules
(with the cleaning and the refuted rule), then the doubling lesson. The
cleaning paragraph was kept to one block for this reason and says only what a
reader needs to trust the count: one test, applied the same way to every
spelling, every exclusion printed with its reason.

## Worked-example progression and retrieval practice

Each lesson runs worked example → faded guidance → independent practice in the
page's own order. `five-forms-and-the-whole-table` works *walk* through all
five forms in the key, states the rules with one example each, hands the reader
a lab preset per rule (*walk*, *stop*, *carry*, *hope*, *listen*, *go*) and
then a free text box, and finally the scoring menu where the reader reproduces
the lesson's figures. `when-the-last-letter-doubles` works *admit* against
*travel* in the body, gives four ordered questions as the method, and the lab
hands over the switch between three rules so the reader produces 49.3 / 50.7 /
91.7 themselves.

Retrieval is the quiz and the lab's refusal. The quizzes now have one
defensible answer each and the `why` texts address the wrong model rather than
restating the rule (quiz 2 of lesson one adds *admit, admitting* to refute
"only verbs with one part ever double"; quiz 2 of lesson two refutes each
distractor in turn). The lab refuses *123* and *running fast* with a visible
message, so a reader who types a sentence learns what the rule takes as input.
What is missing is a drill that asks the reader to predict before the lab
shows: the lesson text says "say the rule out loud before you look at the
answer" (`how_to`), and the kit has no hide-then-reveal control, so this rests
on the reader. Recorded below.

## Misconceptions

Named and corrected, each with a number: learning the table instead of the
rules (five forms against twelve boxes); doubling when the stress is early
(*listenning*); believing a rule because it sounds right (*f* → *ves*, 99.92 →
99.59%); using the half rule (49.3%); scoring a rule on words it cannot touch
(99.34% against 91.7%); treating a spelling difference as a mistake
(*travelling*). Two more are now addressed in prose because the renderer fixes
`mistakes` at three: that a hit rate can be wrong because the list is wrong
(lesson two, "Three exceptions that were never there"), and that the same verb
can pass one scoring and fail another because the two labs ask different
questions (lesson two, worked `after`: the table lab counts any recorded
spelling as a hit, so *traveling* is right; the doubling lab asks whether the
list ever records a doubled spelling, so *travel* is wrong). A reader who saw
*travel* pass on page one and fail on page two would otherwise have no way to
reconcile them.

Unaddressed and recorded: a learner from a language without final-consonant
doubling may treat *w*, *x* and *y* as consonants that double (*fixxing*,
*playying*). The rule now excludes them in both lessons, but no mistake card
names the error.

## Correctness of every claim about English

Each claim was checked against the shipped rule code, the cleaned data, and
standard reference spellings.

- A regular verb has five forms (base, *-s*, *-ing*, past, after-*have*);
  *be* has eight (*am, is, are, was, were, be, being, been*); modals have
  fewer and only stand in front. Correct.
- *-s*: *-es* after *s, sh, ch, x, z*; consonant + *-y* → *-ies*; consonant +
  *-o* → *-es* (*goes*); otherwise *-s*. Matches `vbThird` exactly. *goes* is
  the `-s` form of an irregular verb, but it follows this rule, which is all
  the sentence claims.
- *-ing*: drop a silent *-e*; double under the doubling rule. Matches `vbIng`,
  which also turns *-ie* into *-ying* and keeps *-ee/-oe/-ye*; the prose does
  not state those two sub-cases. Minor omission, recorded.
- *-ed*: *-d* after *-e*; consonant + *-y* → *-ied*; doubling. Matches `vbEd`.
- Doubling: CVC ending, last letter not *w/x/y*, stress on the last part,
  before *-ing* and *-ed* only. Matches `vbDoubles` and the call sites.
- *stomach* → *stomachs* because the *-ch* is /k/, not a hiss. Correct.
- *panic* → *panicking*, *traffic* → *trafficking*. Correct.
- *format*, *input*, *output* double against the stress; *input*/*output*
  inherit *put*'s doubling. Correct.
- *bus* → *busing* (list) where the rule writes *bussing*; both are in use.
  Correct.
- *initial* → *initialling/initialled* (British, the only forms the list
  records); *counsel* → *counselled* (British only in the *-ed* slot, both in
  *-ing*). Correct, and the lesson's "counsel in the past" is the exact slot.
- *up* has no consonant before its vowel, so the CVC test fails and the rule
  writes *uping*; the real form is *upping*. Correct.
- British writers double a final *-l* regardless of stress; the eleven named
  (*cancel, channel, counsel, label, level, model, panel, rival, signal, total,
  travel*) all have *-ll-* British forms. Correct. The one common British
  exception, *parallel* → *paralleled*, is a row the lab gets right under every
  rule and the lesson does not mention it; recorded, not worth a sentence.
- *benefit*, *focus*, *program* are recorded both ways (*benefitting*,
  *focussing*, *programing*). Correct as a statement about the list.
- *offerring*, *sufferring*, *councilling* are not English spellings; *council*
  is not a verb; *offer* and *suffer* obey the stress rule (*offering*,
  *suffering*). Correct.
- *f* → *ves* is a noun rule (*leaf*, *leaves*); *brief*, *golf*, *proof*,
  *roof* as verbs take *-s*. Correct.
- *have* looks back, *be* + *-ing* is still going on, *will* moves later.
  Simplifications a Foundational course may make; the course's `not_covered`
  says choosing between boxes is not taught.
- Nine of twelve boxes take a small word: **wrong**, now ten. See above.

## Changes made

In `content/english/c1_tense_tables/part_a.py` (`five-forms-and-the-whole-table`):
every figure updated to the pinned tiles (1,210; 99.92 / 99.34 / 99.26%; 1209,
1202, 1201; the residues; 99.75% and 99.59% for the two variant rules); the
key, concept 1, body and quiz 1 corrected from nine to ten; "and only five"
replaced with the *be* and modal sentences; the rule list restated as the code
runs it (*-d* after *-e*, no doubling before *-s*, *w/x/y* excluded); the
panel intro discloses the stress default for unlisted verbs and points at the
scoring menu; a paragraph "The list had to be cleaned first" with `dictionary`
as a `<dfn>`; the worked intro names the menu and the `after` names each miss
with its reason; the refuted-rule section quotes the lab's two variant scores;
quiz keys 2, 0, 3; "One for each box" replaced; `why` texts extended to refute
the distractors.

In `part_b.py` (`when-the-last-letter-doubles`): 232 → 217, 117/115 → 107/110
with the order flipped, 210 → 199, 90.5 → 91.7%, 22 → 18, 13 → 11, everywhere
(summary, key, concepts, steps, read intro, worked, note, mistakes, quiz,
body); the residue lists rebuilt from the lab's `wrong` rows (metal, council,
offer, suffer out); the worked `after` and body explain the two scoring
questions and sort the seven non-*-l* misses into three both-ways spellings,
three that double against the stress and *bus*; a section "Three exceptions
that were never there" says the list carried misspellings and names them;
concept 1 and mistake 2 now point at the previous lesson's 99.34% instead of
"all 1,356"; step 1 carries the *w/x/y* clause; the `standard` adds telling a
both-ways spelling from a true exception; quiz 2 uses *visit*; quiz keys 1, 3,
2.

In `c1_tense_tables/__init__.py`: 1,356 → 1,210 in the blurb; the summary,
`outcomes[5]`, `syllabus_intro` and `not_covered[0]` no longer promise a count
of which boxes writers use; `outcomes[2]` carries the new hit rates;
`outcomes[0]` says ten; the key's hit-rate line and `he, she, it`.

In `content/english/__init__.py`, the path key's two course-1 lines only: the
hit rates, and "four of the twelve tense boxes / carry most of real writing"
replaced with the doubling figures. The rest of that file belongs to the
Subject and was not touched.

In `docs/ENGLISH-SUBJECT.md`, the Course 1 section of §5 only: the new table,
the cleaning, the two variant scores, the 217-row doubling table with the
flipped order, the eighteen named, the two scoring questions, and a note that
the cell-usage measurement is not taught by any lesson.

## Read-out

The course's math runs are key lines and worked lines, and `say()` reads a
leading hyphen as "negative" and a slash as "over". The affix runs cannot be
rewritten away (the hyphen is the lesson's own notation), so they need spoken
forms in `content/spoken/english.py`, which the orchestrator owns. The exact
run texts, after this pass, and what each should say:

| run (exact) | should be spoken as |
|---|---|
| `base   he, she, it   -ing   past   after have` | base; he, she, it; the ing form; past; after have |
| `be + -ing form       still going on` | be plus the ing form, still going on |
| `-s 99.92%   -ing 99.34%   -ed 99.26%` | the s rule 99.92 percent, the ing rule 99.34 percent, the ed rule 99.26 percent |
| `-s 99.92%    -ing 99.34%    -ed 99.26%` (path key, four spaces) | the s rule 99.92 percent, the ing rule 99.34 percent, the ed rule 99.26 percent |
| `-ing form       walking` | the ing form, walking |
| `-s      1209 of 1210 right     99.92%` | the s rule, 1209 of 1210 right, 99.92 percent |
| `-ing    1202 of 1210 right     99.34%` | the ing rule, 1202 of 1210 right, 99.34 percent |
| `-ed     1201 of 1210 right     99.26%` | the ed rule, 1201 of 1210 right, 99.26 percent |
| `of the 18 still wrong, 11 end in -l` | of the 18 still wrong, 11 end in the letter l |
| `ending in -l   cancel, channel, counsel,` | ending in the letter l: cancel, channel, counsel |

`he/she/it` was rewritten as `he, she, it` in both keys so it no longer needs
a form; the doubling key's three figure rows (`double every one      107 / 217
49.3%` and its two siblings) are detected as table rows and read as a pointer
to the page, which is right.

## Remaining issues, for whoever next owns this course or the kit

- The preservation contract (`tests/content_preservation.json`) fingerprints
  `c1_tense_tables/__init__.py`, `part_a.py` and `part_b.py`; those entries are
  stale after this pass and the orchestrator regenerates them with
  `/usr/bin/python3` before committing. `scripts/build_paths.py` has not been
  run here (other agents work in the tree) and the two published pages are
  stale until it is.
- `content/spoken/english.py` says "there are none" and ships `SPOKEN = {}`;
  the table above is the course's share of what it needs. Its docstring's
  claim that no English run is ambiguous is false for the affix runs and should
  be rewritten when the forms land.
- Lesson one should be two lessons (see cognitive load). Recorded, not done:
  the course's lesson count and URLs are pinned in five places.
- The `-ie` → `-ying` and `-ee/-oe/-ye` sub-cases of `vbIng` are run but not
  stated. A clause in the `-ing` bullet would close the gap at the cost of one
  more sub-case on an already heavy page.
- No mistake card names *w/x/y* doubling (*fixxing*); the rule excludes them
  but the error is not called out. `mistakes` is fixed at three.
- The kit has no predict-then-reveal control, so "say the rule before you
  look" rests on the reader.
- *parallel* → *paralleled* is the one common exception to "British writers
  double a final -l whatever the strong part is"; the lab scores it right under
  every rule and the lesson does not mention it.
- The cell-usage measurement in `docs/ENGLISH-SUBJECT.md` (progressive 1.4%)
  is now taught nowhere. If a usage lesson is ever written, it needs the 1,951
  verb phrases printed on the page and a lab that counts them; until then the
  figure must not reappear in course or path copy.
- `docs/ENGLISH-SUBJECT.md` §5 Course 3 and §6 (4.5×, 4.4×, 1,844 words, one
  in 256) are the word-order course's and were left for its reviewer.
