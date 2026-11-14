# Review (accuracy and teaching): Leviathan, Course 1 — Sense, Imagination and Speech

Course: `leviathan-sense-and-speech` (`content/leviathan/c1_sense_and_speech/`,
`__init__.py`, `part_a.py`), five lessons, plus `PATH` in
`content/leviathan/__init__.py`. Reviewed 2026-11-14 against the operator's copy
(PDF pages as `page.py` numbers them), to `docs/leviathan/REVIEW.md`. I read every
page behind the course (PDF 99–100, 105–107, 109–120, 120–127, and Ch. 5 p. 129 for
the absurdity passage). I did not read `site/` or the text file whole, and I used
nothing from Tuck's apparatus. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py leviathan --course leviathan-sense-and-speech`
  rendered 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**
  (re-run after the container restart, still OK).
- **Quotations:** I extracted 128 `&ldquo;…&rdquo;` spans (110 distinct). All are
  OK or OCR noise confirmed on the image (p. 105 *artificiall Joynts*, *Automata*;
  p. 113 "I know I dreame not"; p. 121 *Quiddity*; p. 123 "A man… 7ruth"), **except
  three** (MF-4, MF-5). Opening quotations: L1 57 words, L2 59, L3 103, L4 68, L5 76,
  all under 120. The source comments' PDF pages are right (L1 105, L2 110, L3 117,
  L4 120, L5 123).
- **Browser (Playwright, chromium, `file://`):** all five lessons at 375 px and
  1280 px have no sideways scroll and no console or page errors. Every preset
  matches the prose and my own computation: bare 8/1 (p=T q=T r=F), bridged 0,
  without-looking 1 (p=T q=F r=F); echo 0 and modus tollens, no-conditional 1
  (a=T b=F), pressed 1, analogy 0; one 4/5, 4, 17/25; three 64/65, 64, 257/325; mixed
  4/5, 4, 17/25; many 4096/4097, 4096, 3277/4097 (= 16385/20485, a little under
  4/5). Reckon: vocab 3/3, breadth 3/2, compound 3/1, bad-definition 1/3,
  absurd-and-empty 1/1/1/1, just-by-law true, just-by-might false. Expansions check
  by hand.
- **Counts:** 9 courses, 55 lessons (by `grep -c '"slug"'` and by import). The
  tagline and description both say nine and 55.

## MUST-FIX

**MF-1. Lesson 5 says a false affirmation is not absurd, and Hobbes says the opposite.**
`part_a.py:1545–1549` (mistake 1): "A false affirmation can be sensible: man is a
horse is false, and one could understand it." Chapter 4 (PDF p. 126–127) says the
reverse: "of absurd and false affirmations, in case they be universall, there can be
no Understanding". *Man is a horse* is a universal affirmation, so on Hobbes's
account it cannot be understood. Chapter 5 (p. 129) says a false general inference,
"though it be commonly called Error, it is indeed an ABSURDITY, or senslesse
Speech." Replacement:
> ("Thinking the lab's three verdicts are Hobbes's three kinds", "The lab keeps false, absurd and insignificant apart, and that is the lesson's way of sorting them. Hobbes does not sort them that way. For him a contradictory name such as round quadrangle signifies nothing *because* the affirmation 'a quadrangle is round' is false, and of absurd and false universal affirmations alike he says there can be no understanding. In Chapter 5 he calls a false general inference an absurdity.")

**MF-2. The quotation on understanding drops "and false".** `part_a.py:1402`: "so of
absurd universal affirmations &ldquo;there can be no Understanding…&rdquo;". The text
(p. 126–127) reads "of absurd and false affirmations, in case they be universall".
Cutting the words changes what Hobbes says on exactly the point the lesson is
teaching. Replacement: "so &ldquo;of absurd and false affirmations, in case they be
universall, there can be no Understanding; though many think they understand, then,
when they do but repeat the words softly&rdquo;."

**MF-3. In Chapter 4 the contradictory name is the second sort of insignificant name,
and the lesson presents it as a separate kind that is "not false".** The concept
(`:1286–1290`) and the passage at `:1361–1366` are right: Hobbes says "All other
Names, are but insignificant sounds; and those of two sorts" (p. 126), and the
second sort is the name made of contradictory names. But `:1372–1374` says of the
lab's absurd and insignificant claims: "They are not false, and they differ from
one another". The text then says: "whensoever any affirmation is false, the two
names of which it is composed, put together and made one, signifie nothing at all".
On Hobbes's account, "round quadrangle" is a mere sound *because* "a quadrangle is
round" is false. He calls in-powred vertue "as absurd and insignificant, as a round
quadrangle", using the two words together. The caveat at `:1374–1378` admits part of
this, but mistake 1, quiz 2's `why` and the key lines then teach the lab's scheme as
Hobbes's. Fix these places:
- `:1370–1378`, replace from "The lab keeps these apart." with: "Both, for Hobbes, are insignificant sounds, and he ties the second sort to falsehood: if it is false that a quadrangle is round, then round quadrangle 'signifies nothing'. The lab gives the two sorts different labels. In the absurd-and-empty preset round and quadrangle are declared opposed, so round-quadrangle is man is marked absurd: the lab's word for Hobbes's second sort, a name made of names that cannot be added. Quiddity has no definition and is not simple, so quiddity is man is marked insignificant, his first sort. Keeping these apart from false is the lab's sorting, not Hobbes's. He makes the empty name follow from the false affirmation, and in Chapter 5 he will call a false general inference an absurdity."
- `:1517–1520` (quiz 2 `why`), replace the last clause with: "…which is quiddity is man. The fourth goes beyond Chapter 4, though Chapter 5 says something close to it for general inferences; the question asks why the lab marks this claim absurd." Option 4 is otherwise arguable from Ch. 5 (p. 129). Better still, change option 4 to "Because round-quadrangle is not one of the simple names", which is plainly wrong, since the name is defined.
- `:1265–1266` key lines: "absurd: names that cannot be added" and "insignificant: a name that names nothing" should be "insignificant: undefined or contradictory" and "false affirmation → its compound signifies nothing".
- `__init__.py:31` key "absurd names cannot be added" should be "contradictory names signify nothing". `__init__.py:57` outcome should be "…and tell a name with no definition, or one made of contradictory names, from a sensible one, as Hobbes and the lab each sort them."

**MF-4. Misquotation: "Wisedome".** `part_a.py:1392`: the image of p. 127 reads "For
one man calleth *Wisdome*, what another calleth *feare*". Replace "Wisedome" with
"Wisdome".

**MF-5. Two `&ldquo;` spans are not in the text.** `part_a.py:185`
"&ldquo;whosoever does this will find that&rdquo;" is a made-up template. `:129`
"&ldquo;the passions are the same in all men&rdquo;" does not match the text, which
reads "Passions, which are the same in all men" (p. 106). Replace the first with
"Four moves, for any passage that says that whoever does one thing will find
another." and the second with "Let `p` be <em>the passions are the same in all
men</em>".

**MF-6. The prose cites a lab figure no preset prints: incorporeal and body.**
`:1386` "The lab can say only what follows once the pair is declared opposed" and
`:1555` "It shows that if incorporeal and body are declared opposed, then a name
joining them is absurd". No preset has `incorporeal`. Add to absurd-and-empty:
`simple` + `"incorporeal"`; `opposed` + `["body","incorporeal"]`; claim
`["c5","incorporeal body","living-creature"]`. I checked against the kit rules: c1
and c2 are unaffected. Expect `lrkVerdicts` "c1 true; c2 false; c3 absurd; c4
insignificant; c5 absurd" and `lrkCounts` "1 true, 1 false, 2 absurd, 1
insignificant". Mention c5 in the paragraph at `:1361`. The alternative is to rewrite
both sentences as "were the pair declared opposed, as round and quadrangle are…".

## SHOULD-FIX

1. `:1363` "and he names &ldquo;Entity, Intentionality, Quiddity…&rdquo;". That list
   is from the Adam paragraph (p. 121), not the paragraph on insignificant sounds.
   Change it to "and earlier in the chapter he had named…".
2. `:1335–1341` and the worked example at `:1470ff`: "Man is rational flips from true
   to false… (were true)". No preset shows these claims as true. Add a
   `good-definition` preset (the lesson 4 defs, the same four claims, 4 true) before
   bad-definition, so the reader can see the flip.
3. Lesson 4 worked title and last line (`:1155`, "peter is just… false"). The vocab
   preset has no such claim. Add `["c7","peter","just"]` to vocab (verdicts gain "c7
   false"; counts 3 true, 4 false) or say that it is computed by hand.
4. `:1181` quiz `why` "so every part of Peter is not in man" should be "so not every
   part of Peter is in man".
5. `:1203` quiz `why` refers to an option ("declaring a will one does not have")
   that is not offered, and to "the other two" when there are three. Rewrite it as:
   "Concealing one's thoughts is nearest the third abuse, declaring a will one does
   not have; raising a likeness and proving existence are not in his list."
6. `__init__.py:70` "Each preset is a single change against the one before it". This
   is not true of pressed after no-conditional, breadth after vocab, or many after
   mixed. Change it to "Most presets change one thing against another…".
7. `:699` In the text the sweeping of a room and the spaniel are similes for seeking
   *within a known place* (p. 118), not for the regulated train in general. Change
   to "and when a man knows the place within which to seek, he likens it to sweeping
   a room for a jewel, &ldquo;as a Spaniel…&rdquo;".

## NOTE

1. The confusion in MF-1 and MF-3 starts upstream. PLAN §0.1 and the `reckon` kit
   define absurd and insignificant as exclusive of false. The kit cannot be changed
   here. The tile labels are fixed, so the lessons must say in words that this is
   the lab's sorting. The plan's owner may want to note this for Courses 2 (Ch. 5)
   and 8–9 (Chs. 34, 46), where the same verdicts return.
2. Lesson 4 handles the truth rule fairly. Hobbes's "the later name… signifie all
   that the former… signifieth" (p. 123) is about extent, and the lab's parts test
   inverts it into content. The lesson flags this and the man/rational limit, which
   is good.
3. PATH: every claim checks against the text and PLAN §A. The tagline's ending, the
   edition attribution, "theorems" of reason and the Review's purpose are all fine.
   `why_order` says Hobbes "means" Parts III–IV "as the application". That is an
   interpretation, so consider "they apply".
4. History checked: Paris, April 1651; left England 1640; Charles executed 1649;
   Descartes's *Meditations* 1641 and Hobbes's objections; Bramhall, Paris debate
   and *The Catching of Leviathan* 1658; Hume born after 1679. The frontispiece
   description is right.
5. Voice meets PLAN §F throughout: the passage is read whole and then gone through,
   it is addressed to "you", and critics are given at strength (the realist, Hume,
   Bramhall). Each lesson closes on the gap the material clause names.

**Verdict:** the gates pass and Lessons 1–4 are accurate. Lesson 5 must stop
teaching the lab's false/absurd/insignificant split as Hobbes's (MF-1–3), and needs
one quotation corrected and two quotation marks removed before it ships.
