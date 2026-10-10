# Pedagogy assessment — Tense Tables (english, course 1), second version

Fresh assessment of the four-lesson course on branch `feat/english-v2`,
replacing the 2026-10-08 assessment of the two-lesson first version. Formed
from every lesson dict in `content/english/c1_tense_tables/` (`part_a.py`:
`five-forms-and-the-whole-table`, `scoring-a-rule-on-real-verbs`; `part_b.py`:
`when-the-last-letter-doubles`, `how-ed-and-s-are-said`; `__init__.py`, the
course dict), the design they were written to (`docs/english-v2/PLAN.md` §0,
§B, §C Course 1, §D `table`/`doubling`/`endings`, §E, §F), the kit they
render through (`scripts/mathpath/labs/english.py` modes `table`, `doubling`,
`endings` over `english_core.py`) and the data the kit inlines
(`scripts/wordlists/verbrules_cases.json`, `verbrules_raw.json`,
`doubling_verbs.json`, `verb_sounds.json`). All four lessons were read in full
before anything was changed.

Every figure below was read off the rendered page with `node
scripts/labcheck.js --observe` (rendered by `scripts/preview_subject.py english
--course tense-tables`) and recomputed from the data files with
`/usr/bin/python3`. The preview reported OK before and after the changes: four
labs execute and survive the control sweep, four pages carry pinned figures and
every pin matches. Band (`scripts/bandcheck.py`, floor 98%): course home
98.8%, lesson one 99.2% (no glossary term), lesson two 99.1% (one), lesson
three 99.7% (three), lesson four 99.7% (seven). Weight, gzipped: 16.5, 37.8,
38.2, 28.3 and 44.0 KB against the 67 KB ceiling. `tests/test_speech.py`: 15
of 16 pass; the one failure is two stale forms in `content/spoken/english.py`
recorded under *Remaining issues*. `tests/test_english_kit.py`: 28 of 28.

## Verdict

The course teaches what it says it teaches, every figure it states is one the
page prints, and after this pass every claim it makes about English is true.
A reader who finishes it can write the five forms of a regular verb by rule,
place *have*, *be* and *will* in front of them to fill a twelve-cell table,
read each of the three forming rules' hit rate off 1,210 printed verbs and sort
the misses into named kinds, apply the one spelling rule that needs the sound
of the word and say which of its eighteen misses are a second country's rule,
and say from a verb's last sound how its *-ed* and *-s* are pronounced, with
the two rules' scores read off the page.

The split the first assessment asked for has been made. The old lesson one
carried three hard ideas at the renderer's ceiling of 18 body blocks; it is now
`five-forms-and-the-whole-table` (build, 11 blocks) and
`scoring-a-rule-on-real-verbs` (score and refute, 15 blocks), sharing one lab
whose `focus: "score"` cfg moves the scoring half above the grid. The new
fourth lesson is the first pronunciation rule any A2 course teaches, and it is
scored on the page the way the spelling rules are.

Before this pass the course had three kinds of defect, all fixed below: five
escaped fields carried `<em>` markup that reached the reader as the literal
characters `<em>-s</em>` and the voice as "is less than e m is greater than
negative s"; the fourth lesson called *legged* "a true exception" when the rule
is right about the verb and the dictionary had answered about an adjective,
and said the dictionary gives "the noun first" for *close*, whose first reading
is the adjective; and the doubling lesson's key split one rule over three lines
so Listen read "a table, shown on the page. double when the last. part is the
strong. a table, shown on the page".

## What the course teaches well

- **Every objective is an act the lab measures, and none says "understand".**
  `five-forms-and-the-whole-table` closes on "build the full table for a verb
  you have never seen, and name the rule that made each form"; the table lab
  fills twelve cells for a typed verb and prints the rule that fired
  (`tbRule`). `scoring-a-rule-on-real-verbs` closes on reading a hit rate off
  the list and naming the reason for each miss; the `tbScore` menu prints
  `1209 of 1210`, `99.92%` and `stomach`. `when-the-last-letter-doubles` closes
  on deciding, before writing, whether a verb doubles; the doubling lab scores
  that decision three ways on 217 verbs. `how-ed-and-s-are-said` closes on
  saying an ending from a last sound; the `enWord` box answers for any verb on
  the list ("walk ends in k (voiceless), so the rule says walked ends in t; the
  dictionary says t").
- **The method is the Subject's, and all four lessons keep it.** State a rule,
  measure it on printed text, show the residue. Every list a lab scores is
  printed under the lab (`List` → every verb; `Show` → every verb; `List` →
  every word), every miss is named in a tile and sorted into kinds in the
  prose, and the two rules the kit also runs in their refuted form (`-o` before
  the fix, `f → ves`) are menu options, so the reader produces the worse
  score rather than being told about it.
- **The split lands the load where it belongs.** Lesson one states the four
  rules exactly as the code runs them (including `-ie → -ying`, `-ee/-oe/-ye`
  keep the *e*, `-d` after a silent *-e*, no doubling before *-s*, *w/x/y*
  never double) and states no hit rate; the only figure it carries is 1,210
  as the list the next lesson scores. Lesson two carries every scoring figure
  and nothing about building. A reader meets the doubling condition three
  times — as a stated clause in lesson one, as the thing that lifts a coin toss
  to 91.7% in lesson three, and as the `tbRule` text "ends
  consonant-vowel-consonant, stressed: double it" — which is the right amount
  for the rule the course says learners get wrong most often.
- **The residue is content, every time.** Lesson two's nine past-rule misses
  are sorted into five kinds with a reason each (British spelling, a *-k* no
  rule knows, doubling against the strong part, both spellings in use, no
  consonant before the vowel). Lesson three's eighteen are eleven British *-l*
  spellings (a second rule, not eleven exceptions), three both-ways spellings,
  three that double against the stress and *bus*. Lesson four's seven are now
  all one lesson: none is a verb that breaks the rule; the dictionary answered
  about a different word every time.
- **Two scoring questions are told apart on the page.** The table lab counts a
  hit when the rule's form is any recorded spelling, so *traveling* is right
  there; the doubling lab asks whether the list ever records a doubled
  spelling, so *travel* is wrong there. Lesson three's worked `after` and body
  say so explicitly, because a reader sees the same verb pass one page and
  fail the next.
- **The voice is right.** Short declaratives, counted claims ("Counted on this
  page, the *-ed* rule is right for 1111 of 1118 verbs, 99.4%"), no "In this
  lesson", British spelling throughout, grammar words kept to the glossary
  budget (*strong part*, *part*, *hiss*, *voiced*, *voiceless*, *dictionary*).

## What the course taught badly or said wrongly (fixed in this pass)

- **Markup in escaped fields** (`five-forms-and-the-whole-table` mistakes[2]
  title; `how-ed-and-s-are-said` standard[0], mistakes[0] and mistakes[2]
  titles; course `outcomes[5]` title). The renderer escapes headings, mistake
  titles, the completion standard's first line and outcome titles
  (`render.esc_inline`), so `<em>-s</em>` shipped as six visible characters and
  the read-out script, seeing `<` and `>`, spoke "is less than e m is greater
  than negative s is less than over e m is greater than". The English Subject
  is not yet in the import list of `TestLessonDataMatchesTheRenderer`
  (`test_escaped_fields_carry_no_html`), which is why nothing caught it. All
  five fields now carry plain text ("Putting -s or -ed on the verb behind
  will"; "Saying the -s ending as s every time"; "Say how -ed and -s are said").
- **"This one is a true exception"** (`how-ed-and-s-are-said`, body, the
  *legged* bullet). It is not. The verb *leg* (*he legged it*) takes *d*, as
  the rule says; CMUdict's first reading of *legged* is the adjective
  (*four-legged*), which is said with *id* after the *g* the way a handful of
  adjectives are. That makes it the same kind of miss as the other six — the
  dictionary answered about a different word — and the lesson now says so,
  with the heading sentence changed from "Six of the seven are one kind of
  miss" to "Not one of the seven is a verb that breaks the rule".
- **"The dictionary gives the noun first"** (same bullet list). True of
  *abuse*, *excuse*, *house* and *use*; false of *close*, whose first reading
  /kloʊs/ is the adjective (*close by*), not a noun. The quiz already said "a
  noun or an adjective"; the body now does too, naming the adjective *close*
  beside the nouns *house* and *use*.
- **A miss stated without its other half** (`how-ed-and-s-are-said`, the
  *knives* paragraph). The list records both *knifes* and *knives* for the verb
  *knife*; the sounds file scored *knives* because CMUdict does not carry
  *knifes*. The lesson now says the list also records *knifes*, which follows
  the rule, so a reader is not left believing *he knives* is the only form.
- **A read-intro that overclaimed in the other direction** ("Almost every
  miss is the rule reading a sound that the verb does not have"). Now: every
  miss is the rule being given a sound the form does not have, either because
  the dictionary's first reading is another word or because the last sound
  itself turns voiced before the ending (*knives*, *mouths*, *paths*,
  *youths*).
- **"as in mouth"** (the plural paragraph) explained *mouths* by pointing at
  *mouth*. The paragraph now says what the three plural misses share: a final
  sound at the start of *think* that turns into the one at the start of *then*
  when the noun means more than one, so the ending is *z*.
- **The doubling key read aloud as nonsense** (`when-the-last-letter-doubles`,
  key). The third rule was split over three lines of the hero key to fit 46
  characters, and `speech.say_block` read the two fragments as prose and the
  figure rows as "a table, shown on the page". The key now holds one rule per
  line (`double if last part strong  199 / 217   91.7%`, 45 characters) and
  the three rows have spoken forms in `content/spoken/english_c1_tense_tables.py`
  ("double only when the last part is the strong part, 199 of 217, 91.7
  percent"), so Listen reads the key's whole content.
- **"the six verbs marked as broken ones"** (`five-forms-and-the-whole-table`,
  panel intro). The tile says "irregular: looked up, not formed"; the intro
  now uses the word the page uses.
- **"were wrong spellings in the list itself"** (course `outcomes[4]`) for
  *offer*, *suffer* and *council* — the first two were misspellings, the third
  a non-verb given a verb form. Now "were mistakes in the list itself", which
  the summary already said.

## What it claims to teach, and whether it does

Every outcome on the course home is delivered by a lesson: build any verb's
table (lesson one, `tbGrid`); say which rule made a form (lesson one,
`tbRule`); quote a hit rate and the misses (lesson two, `tbScore` tiles);
tell a rule that helps from one that only sounds right (lesson two, the `ves`
option); tell a spelling difference from a mistake (lesson three, the eleven
*-l* verbs and the three removed misspellings); say how *-ed* and *-s* are said
(lesson four, `enPreset`). `not_covered` is honest: choosing between boxes,
sounds beyond the two endings, every irregular verb, and rare or old forms
are named as not taught and pointed at the courses that teach them.

Nothing in this course is quoted. Every figure in prose — 1209/1202/1201 of
1210 and 99.92/99.34/99.26%; 1207 and 1205 (99.75%, 99.59%) for the two
variant rules; 146 left out, 90 irregular; 107/110/199 of 217 and
49.3/50.7/91.7%; 18 wrong, 11 in *-l*; 1111 of 1118 (99.4%), 1187 of 1189
(99.8%), 1820 of 1823 (99.8%); 92, 21 and 45 skipped — is printed by a tile
on the same page and was read off that tile. The prose says "counted on this
page" where a reader might wonder. The course has no whole-novel figure to
label.

## Prerequisite order and cognitive load

The course is first in `docs/english-v2/COURSES.json` and assumes nothing;
the course dict says so and the arithmetic never goes past counting and a
share. Inside the course the order is right: forms and all four rules (one),
the rules scored (two), the one rule that needs the sound isolated and scored
where it can fail (three), the sound of the endings (four). Lesson four needs
*voiced* and *voiceless*, which it defines with the finger-on-the-throat
test before the rule uses them, and *part* for syllable, which lessons one
and three have already used in "the last part is the strong part".

Every forward reference is by title to a course that exists in COURSES.json:
Irregular Verbs (*be* set apart; the 90 excluded verbs), Helping Verbs (*has*,
*was*, *been*), Word Stress ("Nouns at the Front, Verbs at the Back", where the
strong part is taught), Nouns and Articles (the plural rule's other home),
Spelling to Sound and Listening (course `not_covered`). None reaches back,
because there is nothing earlier.

Load: one hard idea per lesson now — build; score; the stress condition; the
voicing rule. Lesson four sits at 18 body blocks, the ceiling, because it
carries two rules (*-ed* and *-s*) plus their residue; the two rules are one
mechanism (voicing) with one extra case each (*t/d*; the hiss), so this is one
idea stated twice rather than two ideas, and the key and the worked example
present them side by side on purpose.

## Worked-example progression and retrieval practice

Each lesson runs worked example → faded guidance → independent practice in the
page's own order. Lesson one works *walk* through five forms and four boxes in
the key and worked block, states the rules with one example each, hands the
reader a preset per rule (*walk*, *stop*, *carry*, *hope*, *listen*, *go*) and
then a free text box. Lesson two works the nine past-rule misses sorted into
kinds, gives a four-step method ("choose the rule; read the count and the
share; read every word it missed; sort the misses into kinds"), and the menu
lets the reader reproduce every figure and the two refuted variants. Lesson
three works *admit* against *travel*, gives four ordered questions, and the
switch between three rules produces 49.3 / 50.7 / 91.7 in the reader's hands.
Lesson four works *walk*, *play*, *want* through the three sounds, gives a
four-step method ending in the finger test, and the `enWord` box lets the
reader name a verb's last sound and check it against the dictionary before
reading the table; the panel intro now tells the reader that box is there, which
it did not before.

Retrieval is the quiz plus the lab's refusals. Every quiz has one defensible
answer and positions are spread (lesson one 2, 0, 3, 1; two 3, 1, 0, 2; three
1, 3, 2; four 2, 0, 3, 1). Each `why` addresses the wrong model rather than
restating the rule: lesson one's "Only verbs with one part ever double" is
refuted with *admit, admitting*; lesson three's *admit* against *visit*
refutes "ends in -t" and "has two parts" in turn; lesson four's *played*
against *walked* refutes "ends in a consonant letter" by making the point that
letters are the wrong thing to read. The labs refuse `123` and `running fast`
with a visible message, and `enWord` refuses a word not on the list with "not
on the printed list: the page cannot hear it".

## Misconceptions

Named as `mistakes[0]` and matching §C of the plan in every lesson: the twelve
boxes are twelve things to learn (one); a rule that sounds right is right —
the *f → ves* rule drops the *-s* score from 1209 to 1205 (two); the short
rule most books print, right half the time (three); *-ed* is always a part of
its own (four). The other eight mistake cards each carry a number or a named
word: doubling with the stress early (*listenning*), *-s* or *-ed* after
*will*, scoring against a wrong list (*offerring*), reading 99.26% as
finished, scoring a rule on words it cannot touch (99.34% against 91.7%),
treating *travelling* as a mistake, reading the last letter instead of the
last sound (*laugh*, *love*), saying *-s* as *s* every time (*plays*, *needs*,
*loves* end in *z*).

## Correctness of every claim about English

Checked against the shipped rule code (`vbThird`, `vbIng`, `vbEd`,
`vbDoubles`, `enEdSound`, `enSSound`), the data files, and standard reference
pronunciations and spellings.

- A regular verb has five forms; *be* has eight (*am, is, are, was, were, be,
  being, been*); modals have fewer and only stand in front. Correct.
- *-s*: *-es* after *s, sh, ch, x, z*; consonant + *-o* → *-es* (*goes*);
  consonant + *-y* → *-ies*; else *-s*. Matches `vbThird` line for line.
- *-ing*: *-ie* → *-ying*; drop a silent *-e* except after *-ee/-oe/-ye*;
  double under the doubling rule. Matches `vbIng`.
- *-ed*: *-d* after *-e*; consonant + *-y* → *-ied*; doubling. Matches `vbEd`.
- Doubling: CVC, last letter not *w/x/y*, last part strong, before *-ing* and
  *-ed* only. Matches `vbDoubles` and its call sites. *Stop* and *plan* double;
  *listen*, *visit*, *travel*, *offer*, *suffer* do not. Correct.
- The residues as printed: *stomach* (*-ch* said as *k*); *initial* and
  *counsel* (the list records only British *-ll-* in the past slot:
  `initialled`, `counselled`; *counsel* has both spellings in *-ing*, hence
  eight *-ing* misses against nine *-ed*); *panic*, *traffic* (*-k*); *format*,
  *input*, *output* (double against the stress; the last two inherit *put*);
  *bus* (`busing` in the list, `bussing` from the rule; both in use); *up*
  (no consonant before the vowel, so the CVC test fails). All correct, and
  all verified in `verbrules_cases.json`.
- Raw-list artefacts named: `offerring`, `sufferring`, `commiting`,
  `councilling`, `comed`, `maked` are all in `verbrules_raw.json`; 146
  excluded, 90 of them irregular, in `verbrules_cases.json`. Correct.
- *f → ves* is a noun rule; *brief*, *golf*, *proof*, *roof* as verbs take
  *-s*. Correct.
- The eleven *-l* verbs all have British *-ll-* forms; British writers double a
  final *-l* regardless of stress (the common exception, *parallel →
  paralleled*, is a row the lab gets right under every rule and the lesson
  does not need). *benefit*, *focus*, *program* recorded both ways. Correct.
- Voiceless sounds *p, k, f, s, t*, the sounds at the start of *think*, *ship*
  and *church*; every vowel voiced; *b, d, g, l, m, n, r, v, z* voiced. Matches
  `EN_VOICELESS` (p k f θ s ʃ tʃ t) and is correct.
- *-ed*: *id* after *t/d*, *t* after another voiceless sound, *d* otherwise.
  *-s*: *iz* after a hiss (*s, z*, the sounds of *ship*, *measure*, *church*,
  *judge*), *s* after another voiceless sound, *z* otherwise. Correct;
  matches `enEdSound`/`enSSound`. *judges*, *faces* take *iz* with only *-s*
  spelled. Correct.
- The seven *-ed* misses: *abuse, excuse, house, use* (noun /s/, verb /z/),
  *close* (adjective /s/, verb /z/), *mouth* (noun /θ/, verb /ð/), *legged*
  (adjective /ɪd/, verb /d/). After this pass, all correctly described as the
  dictionary's first reading being a different word. `verb_sounds.json` rows
  confirm the recorded last sound and form sound for each.
- *knives* /naɪvz/, *mouths* /maʊðz/, *paths* /pæðz/, *youths* /juːðz/ in
  CMUdict's first reading: the voiceless final turns voiced. Correct, and the
  lesson now says the list also has *knifes*.
- 92 past forms, 21 *-s* forms and 45 plurals not in CMUdict, listed and not
  counted; 1118 + 92 = 1189 + 21 = 1210. *blogged* is in the skipped list.
  Correct.
- "The sounds are American, from the dictionary's first reading" — stated as
  a limit on the page (`enLimit`) and in the prose. Correct and necessary.

## Listen

Every math run on the five pages was read from the rendered `data-say`. The
hero keys and worked blocks of all four lessons and the course home now read
as words: "base, walk. he, she, it, walks. the ing form, walking…"; "the s
rule 99.92 percent, the ing rule 99.34 percent, the ed rule 99.26 percent";
"the ed rule, 1201 of 1210 right, 99.26 percent. British spelling, initial,
counsel. a k that no rule knows, panic, traffic…"; "double every one, 107 of
217, 49.3 percent. double none of them, 110 of 217, 50.7 percent. double only
when the last part is the strong part, 199 of 217, 91.7 percent. of the 18
still wrong, 11 end in the letter l"; "the ed ending after t or d is said id,
as in wanted…". No page carries an IPA letter or a stress mark in prose; the
sounds that have no safe letter are written as "the sound at the start of
*think*/*ship*/*church*/*then*", as §E requires. No `<span data-say>` remains
on any heading.

`content/spoken/english_c1_tense_tables.py` carries the course's forms (plain
words, digits and percent only); `tests/test_speech.py` passes
`test_spoken_forms_are_words`, `test_one_reading_per_run`,
`test_no_spoken_form_for_a_bare_tuple`, `test_no_spoken_form_for_a_lone_symbol`,
`test_every_sound_in_prose_is_spoken` and `test_nothing_is_guessed` with them
loaded.

## Changes made

`content/english/c1_tense_tables/part_a.py`: mistakes[2] title of
`five-forms-and-the-whole-table` made plain; panel intro says "the six verbs
the page marks irregular".

`content/english/c1_tense_tables/part_b.py`: `when-the-last-letter-doubles`
key rebuilt as one rule per line (five lines, widest 45). `how-ed-and-s-are-said`:
standard[0] and two mistake titles made plain; panel intro names the `enWord`
box; read intro restated; the seven-miss section rewritten (noun or adjective
first; *mouthed* and *legged* as the dictionary answering about another word,
not as exceptions); the *knives*/*mouths* paragraph rewritten with the
*knifes* note; the plural paragraph rewritten.

`content/english/c1_tense_tables/__init__.py`: outcomes[5] title made plain;
outcomes[4] "mistakes in the list itself".

`content/spoken/english_c1_tense_tables.py`: three spoken forms for the new
doubling key rows; docstring corrected (five lines, not two, already have
forms in `english.py`) and the reason for the key forms recorded.

Slugs, lesson count and lab modes are unchanged from `COURSES.json`.

## Remaining issues, for whoever next owns this course or the kit

- `content/spoken/english.py` still carries `-s      1209 of 1210 right
  99.92%` and `-ing    1202 of 1210 right     99.34%`, forms for runs this
  rewrite removed; `test_no_spoken_form_for_math_that_is_gone` fails on
  exactly those two until the orchestrator's merge drops them (the spoken file's
  docstring says so). Not touched here: the file is the orchestrator's.
- English is not in the import lists of `TestLessonDataMatchesTheRenderer`,
  so `test_escaped_fields_carry_no_html` does not run on it; that is how five
  `<em>` tags reached three published-to-be pages. Adding the Subject there
  would have caught this pass's largest defect before a human did.
- `tests/content_preservation.json` fingerprints `c1_tense_tables/__init__.py`,
  `part_a.py` and `part_b.py`; those entries are stale after this pass and
  must be regenerated with `/usr/bin/python3` before commit.
- The kit's `enWordSays` matches a typed word against the base or the form
  but reports in the fixed shape "X ends in … so the rule says Y ends in …"; a
  reader who types *walked* is answered about *walk*, which is right but not
  echoed. Cosmetic.
- No mistake card names *w/x/y* doubling (*fixxing*, *playying*); the rule
  excludes them in lessons one and three but `mistakes` is fixed at three.
- The kit has no predict-then-reveal control, so "say the rule out loud before
  you look at the answer" (`how_to`) rests on the reader.
- The `endings` lab's "the same -s rule on the plurals of nouns" preset is a
  preview of Nouns and Articles; it is pinned (`1820 of 1823`) and the lesson
  spends one paragraph on it, which is right for a preview, but the figure
  will have to be kept in step if `plural_nouns.json` is rebuilt.
- The two British-only slots (*initialled*, *counselled*) and the both-ways
  slots (*counseling/counselling*) depend on what SCOWL's American list plus
  the British-variant test confirmed on 2026-10-08; a dictionary update could
  move *counsel* between the eight and the nine, and both lessons state the
  split from the tiles, so re-read the tiles before trusting the prose after
  any data rebuild.
