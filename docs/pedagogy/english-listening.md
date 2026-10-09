# Pedagogy assessment — Listening (english, course 4)

Formed from the two lesson dicts in `content/english/c4_listening/`
(`part_a.py`, lesson 1, and `part_b.py`, lesson 2), the course dict in
`__init__.py`, the course's entry on the path page in
`content/english/__init__.py`, the data the lab is built on
(`content/english/data/listening.json`, 55 weak forms and 303 stress
patterns, and `wordorder_passage.json`, the 949-word passage), the kit's
`listening` mode in `scripts/mathpath/labs/english.py`, and the pages as
`scripts/preview_subject.py` renders them, with every preset's tiles read off
the built page by `labcheck.js --observe`. The course assumes nothing from the
other three English courses and says so. Both lessons were read before either
was changed; the last two sections record what was changed and what was not.

Lessons, in course order: `why-it-sounds-too-fast`, `where-a-word-begins`.
Both share one lab (two presets of the `listening` mode) and one passage from
*Pride and Prejudice*, which is the right economy: the second lesson's count
is made on the words the first lesson did not mark.

## What the course teaches well

- **Every objective is an act, and the closing `standard` measures it.**
  Pick the words that can take a weak form out of a written sentence, say
  their share, give the squashed shape of the commonest, name the few that
  keep their shape (`why-it-sounds-too-fast`); mark the strong part of a
  written word, say how often the guess "a strong part starts a word" is
  right, and name the group where it fails (`where-a-word-begins`). Neither
  is "understand". The course `outcomes` are six acts of the same kind.
- **One hard idea per lesson, and the right one first.** Lesson 1 carries
  one idea (a closed list of small words is half of running speech and is
  said in a reduced shape); lesson 2 carries one (speech has no spaces, and a
  strong part is the listener's clue to a boundary). The order is right: the
  weak-form list is the larger share and the quicker win, as the
  `syllabus_intro` says, and lesson 2's count is defined on the words lesson 1
  removed. The course is two lessons because it has two computable claims,
  and `docs/ENGLISH-SUBJECT.md` §1–2 is honest that nothing else about
  hearing English passes the Subject's test.
- **The misconception is named in the first line and refuted with a count.**
  "People speak too fast" is the belief every learner arrives with; the
  course's title, blurb, first concept and first mistake all take it on, and
  the refutation is a number the reader can recount (452 of 949 on the
  printed passage) rather than reassurance. The second lesson does the same
  with "I must catch every word" (`steps[0]`, `mistakes[0]`).
- **The worked example is the right shape for a language lesson.** Ten words
  in two columns, written and said (`why-it-sounds-too-fast`, `worked`),
  then the generalisation (one flat vowel) in the `after`; eight words in two
  columns, start-strong against start-light, then the generalisation (the
  failures begin with a front piece) (`where-a-word-begins`, `worked`). The
  steps then fade the guidance: lesson 1's four steps can be done on paper
  with the printed list, lesson 2's four are for a listener with no page at
  all. Independent practice is the lab's second preset in lesson 1 and the
  reader's own listening in lesson 2, which the `how_to` says in so many
  words.
- **The lab prints what it counts.** The passage is printed word by word with
  the marks on it, the words counted are listed with their shape and their
  count, and the stress pattern of every marked word is printed beside it.
  A reader can recount every tile by hand, which is the path's promise.
- **The quoted figure is quoted.** Cutler and Carter's nine-in-ten is given
  in the `note` of `where-a-word-begins` as quoted and not counted, with the
  lab's own 82.3% beside it.
- **The retrieval practice asks for the lesson's claims, not trivia.** The
  six quiz questions ask for the share, the size of the list, the reason the
  forms blur, why boundaries are hard, the strong-start rate and the shape of
  the failures. Each `why` gives the figure or the mechanism, not a
  restatement.

## What the course teaches badly, or wrongly

1. **The headline count was described as something it is not.** The tile
   counts every token of a 55-word list of small grammar words, and the
   lesson said "452 of them get squashed", "47.6% of a page gets squashed".
   Nine words on that list have no weak form in any standard account (Roach,
   *English Phonetics and Phonology*, ch. 12 lists about forty weak-form
   words; *it, in, on, by, with, my, did, they, who* are not among them), and
   the data file itself records them unchanged (`ɪt`, `ɪn`, `ɒn`, `bai`,
   `wɪð`, `mai`, `dɪd`, `ðei`). Eight of them appear on the passage, 64
   tokens by the table's own counts, so the honest figure for words said in
   a squashed shape is 388 of 949, two in five, not one in two. A further 42
   tokens (*that, have, has, had*) squash only in their grammar use, which
   the kit now counts in a separate pinned tile. The prose now states 452 as
   the upper bound ("the most it could be"), names the eight words that keep
   their shape, derives 64 and 388 from the printed table so a reader can
   check them, and reports the 42. The course blurb, key and outcomes now say
   "fifty small words ... most of them get squashed" rather than "47.6% gets
   squashed". The review's wording "words that can take a weak form" is used
   for the count everywhere.
2. **"Every squashed form uses the same vowel" was false.** On the page, 294
   of the 452 tokens take the schwa; the pronouns *he, she, we, his, him*
   (and *be, been*) take a short *i*; *is, will* and *not* lose their vowel
   altogether (`'s`, `'ll`, `n't`); and the eight words above do not change.
   The `worked.after`, the body and quiz 3 now say "most", name the *i*
   group, and use the three vowel-less words to explain where *it's*, *I'll*
   and *don't* come from, which is a teaching point the lesson was missing.
3. **The weak forms are non-rhotic and the stress data is American, and the
   course did not say so.** `fə` for *for*, `ə` for *her*, `ðə` for *there*,
   `wə` for *were*, `ə` for *are* and `jə` for *your* are southern-British
   shapes; an American speaker keeps an r-colour in all six. The stress
   marks come from CMUdict, which is American. The `worked.after` of
   `why-it-sounds-too-fast` now says which accent the shapes are written in
   and what an American speaker does with the six words; the body of
   `where-a-word-begins` names CMUdict as American and says that British and
   American speech place the strong part alike in nearly every word, with
   *address* as the kind of exception, and that no such word is on the page
   (checked against the 303 entries). The course `not_covered` and
   `footer_lead` say the same.
4. **"485 words that are not squashed" was off by twelve.** The passage has
   949 tokens, 452 on the list, so 497 others; 485 of those carry a stress
   mark and twelve (names such as *Meryton* and *Pemberley*, and rare words
   such as *repine* and *twelvemonth*) carry none and are counted in neither
   tile. The key, summary, body and quiz 2 of `where-a-word-begins` now say
   "485 other words with their strong part marked", and the panel says that
   a few names and rare words are left unmarked.
5. **The small `s` was printed and never explained.** The lab prints three
   marks (`S`, `.`, `s`), the lesson defined two. Seventeen tokens on the
   page begin with a secondary-stressed part (*conversation* `s.S.`,
   *understood* `s.S`, *indeed* `sS`) and the lab counts them as starting
   light, which is a stricter test than Cutler and Carter's, who count any
   part with a full vowel as strong. The key now has a line for the small
   `s`, the panel defines it, the `worked.after` explains the strict test and
   that many strong-start words are one-part words with nowhere else to put
   the stress, and the `note` says how the quoted test differs.
6. **Every quiz question keyed the first choice.** All six had `"c": 0`, and
   the quiz script compares the index without shuffling, so a reader who
   noticed answered the course without reading it. The correct answers are
   now at positions 2, 1, 3 and 1, 3, 0; no `why` refers to a choice by
   letter (the quiz has no letters). Two distractors in lesson 1 quiz 3 were
   partly true: "spoken more quietly" is roughly what unstressed means, and
   "they have no vowel at all" is true of *is, will, not* once the lesson
   says so. Both replaced ("written differently when squashed"; "longer than
   the words around them").
7. **The course home said "nothing here makes a sound" one paragraph after
   "press Listen and the browser reads it out".** The Listen feature exists;
   `how_to[1]` now says the reading voice is a reading voice and the course
   is only useful carried to a person talking.
8. **The passage was never named on these pages.** Both lessons said "a
   novel" and "written in 1813"; the lab prints the passage but not its
   source. The panel intro, note and `footer_lead` now cite *Pride and
   Prejudice* (Jane Austen, 1813, public domain), as the Word Order course
   does.
9. **The front-piece list included one the page does not show.** The
   `worked.after` named *be-, a-, re-, in-, de-*; no light-initial word on the
   page begins with *in-* (every *in-* word on it, *into*, *indeed*,
   *interrupt*, starts strong or with a small `s`). The list is now the one
   the page shows: *be-, a-, re-, un-, de-, con-* (69 light-initial tokens,
   of which about sixty begin with one of these or a similar piece;
   *Elizabeth*, *herself* and *himself* are the rest).

## What it claims to teach but does not, and where a learner gets stuck

- **The course cannot teach the sound, and says so.** Both lessons and the
  course `not_covered` repeat that the page's voice is a reading voice that
  squashes less than a speaker would. That is honest; a learner who expects
  the Listen button to demonstrate weak forms will be disappointed, and the
  `how_to` now sends them to real speech in so many words.
- **"Only fifty words" is a round number, and the course leans on it.** The
  list has 55 entries and 51 appear on the page; "about fifty" is used
  throughout and the exact 51 is given where the tile is. That is the right
  balance for a foundational course. The `outcomes` entry "printed in full"
  was not true (51 of 55 appear) and now says which are printed.
- **The 82.3% rests partly on one-part words.** 249 of the 485 marked words
  are monosyllables and start strong by necessity. The lesson now says so in
  the `worked.after` without giving the figure (it is not computed on the
  page); the figure is recorded here for whoever gives the kit a tile for it.
- **A learner who reads IPA-like shapes (`tə`, `əv`, `ðə`) for the first time
  gets no key to the letters.** The lesson avoids the word "schwa" and calls
  it "the flat vowel in the middle of the mouth", which is within the band and
  enough for the purpose; the two unfamiliar consonant letters (`ð`, `ʃ`) are
  never explained. Left as it is: explaining them would add a glossary the
  lesson does not need, since the reader is told to listen for the shape, not
  to read it. Recorded as the place a first-time reader will pause.

## Prerequisite order

The course assumes nothing from Tense Tables, Irregular Verbs or Word Order,
and nothing in it uses a verb form, a class or a word-order rule. The only
internal dependency runs forward: `where-a-word-begins` counts on "the other
words", which `why-it-sounds-too-fast` defines, and its first step, concept
3 and body all say so. The path page's `sequence_intro` said "each needs the
last" of all four courses and its `why_order` had no entry for Listening; both
are now fixed in `content/english/__init__.py` (the first three in order, the
fourth apart and readable first). No violation sits in an earlier course.

## Accuracy of the claims about English

Verified and left alone: the weak forms given for *and, the, to, of, was,
that, have, can, you* (standard RP weak forms); *to* as `tə` being the normal
unstressed form and the full form the special case; *record* as two words by
stress; *father, answer, carriage, happiness, market* strong-initial and
*believe, again, return, another* light-initial (all match the stress data
and ordinary dictionaries); "speech has no spaces" as the listener's problem;
Cutler and Carter (1987), *Computer Speech and Language* 2, as the source of
the nine-in-ten figure for conversational English, with their definition of
"strong" now stated. Corrected: items 1–5 and 9 above. The claim "the words
that get squashed have not changed since 1813" was softened to "the small
words that take a weak form are the same ones today", which is what the
course can stand behind.

## Changes made

- `__init__.py` (course): blurb, summary, key, outcomes and `how_to` now
  describe the count as fifty small words of which most are squashed;
  `how_to[1]` no longer denies the Listen feature; `not_covered[1]` says
  which accent the shapes are written in; `footer_lead` cites the passage,
  says the words counted are listed beside the count, attributes only the
  strong-part marks to CMUdict, and names the accent of the squashed shapes;
  `<dfn>squashed</dfn>` defined on the course home.
- `why-it-sounds-too-fast`: module, one_line, standard, summary, key,
  concepts 1–2, step 3, panel title and intro (cites the passage), worked
  lines ("all ten" for "every one"), `worked.after` (most, the *i* group, the
  vowel-less three and the contractions, the accent paragraph), note (names
  the novel), mistake 3 replaced (squashing every listed word every time),
  quiz choices reordered to 2, 1, 3 with two distractors replaced, body: a
  new section "What the count does and does not say" with the eight
  unchanged words, 64, 388 and the 42, and "most" where "every" was.
- `where-a-word-begins`: summary, key (485 other words, strong part marked;
  a line for the small `s`), concept 3, step 1, panel intro (three marks,
  unmarked names), `worked.after` (front pieces the page shows; the small
  `s` and the strict test; one-part words), note (Cutler and Carter 1987 and
  how their test differs), mistake 1, quiz choices reordered to 1, 3, 0 and
  quiz 2 reworded, body: the 485 explained, a paragraph on CMUdict and
  accent, "small words" where "squashed" stood alone.
- `content/english/__init__.py`: `sequence_intro` no longer says each of the
  four needs the last; `why_order` says Word Order comes third and gains a
  Listening entry.
- Nothing in `scripts/mathpath/labs/english.py`, `content/english/data/` or
  `content/spoken/english.py` was changed. The pinned tiles (452 of 949,
  47.6%, 42, 399 of 485, 82.3%) are unchanged and were re-read with
  `labcheck.js --observe` after the edits.

## Remaining issues

- **The quoted comparison is still a little loose.** Cutler and Carter's
  figure is over tokens of spoken British English with any full-vowel
  syllable as strong; the lab's is over written prose with primary stress
  only. Under their test the page gives 416 of 485 (85.8%). That figure is
  not computed on the page and so is not stated; a kit option "count a small
  s as strong" would let the lesson print it.
- **The read-out of the IPA-like runs and the stress marks is in the
  orchestrator's hands** (`content/spoken/english.py`): the key and worked
  lines read `tə` as "t ə" and drop the `.` in `S.` and `.S` altogether, so
  "S = said hardest   . = said lightly" is spoken as "S equals said hardest,
  equals said lightly". The exact runs and the words to say are in the
  return of this pass.
- **The noscript sentence takes the lab title as a noun** ("The why it sounds
  too fast, marked on the page is computed in your browser"). That is chrome
  (`render.py`), shared by every lesson, and not a course defect.
- **`release/contract.json` has no `english_semantic_copy` yet**, though
  `tests/test_public_copy.py` reads one. When it is generated it must be from
  the course home as rendered after these edits, since blurb, `how_to`,
  `not_covered` and `footer_lead` all changed.

## Fixes, 2026-10-08

- **The nine words with no weak form are off the list.** *it, in, on, by,
  with, my, did, they, who* were removed from `listening.json["weak"]` (46
  entries remain). Read with `labcheck.js --observe`: `lsWeak` 388 of 949,
  `lsWeakPct` 40.9%, `lsTypes` 43, all pinned in `_LS_PRESETS`; `lsMixed`
  (42) and the strong-part tiles (399 of 485, 82.3%) did not move, because
  none of the nine is in the stress table. Both lessons and the course home
  now say "two words in five" and "fewer than fifty" where they said "nearly
  half" and "fifty", name the nine as common words that are NOT on the list,
  and the "keeps its shape" mistake now teaches the real exception (a listed
  word said in full when stressed or sentence-final). Lesson two notes that
  short grammar words such as *it*, *in*, *with* are neither squashed nor
  marked (the stress table does not carry them), so they sit in neither count.
