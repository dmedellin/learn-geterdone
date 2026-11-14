# Review (accuracy and teaching): Leviathan, Course 2 — Reason, Science and the Passions

Course: `leviathan-reason-and-passions` (`content/leviathan/c2_reason_and_passions/`,
`part_a.py`, `part_b.py`), seven lessons. Reviewed 2026-11-14 against the operator's copy:
I read Chapters 5–9 (PDF 127–157), Chapter 21 at PDF 241–242, and the image of the table
of sciences (PDF 157). I did not read `site/`, and this file is the only one I wrote.

## Gates

- **Preview:** `python3 scripts/preview_subject.py leviathan --course leviathan-reason-and-passions --out …/scratchpad/rev/leviathan-reason-and-passions`
  printed 8 pages. Labcheck: 7 executed, 7 with pinned figures, 0 failing. **OK**.
- **`quotes.py`:** run on all of about 140 quoted spans. Every one is exact. The LOOSE/NEAR
  results are small capitals or OCR errors; I checked them on the images of PDF 130 and 137.
  The two MISS results are a page break (PDF 130/131) and a marginal note (PDF 241), and
  both are exact on the page. The longest opening is 109 words. Every source comment's
  pages are right.
- **Browser (Playwright):** I loaded all seven lessons at 375 and 1280 px. There is no
  sideways scroll and there are no errors. Every preset's tiles match the prose, and I
  recomputed every verdict, counterexample row and deliberation count by hand. Typed
  edits behave as the prose says, and the fix in MF-9 keeps every pin.

## MUST-FIX

1. **Cause numbers wrong.** `part_a.py:431-433` says faith is poured, extension is body and
   a creature is a genus are "his second, fourth and fifth causes". Hobbes's own example of
   the **second** cause is "extension is body" (PDF 131: "and that, extension is body").
   "A living creature is Genus" is the **fourth**. The fifth is names of accidents given to
   names. Replace with: "are his second cause twice and his fourth".
2. **"Six of the seven."** `part_a.py:363-364` says "Six of the seven are the same fault, a
   name put where it does not belong." The first and seventh causes are not that fault, and
   Hobbes introduces only the second to fifth as "unfit connexion of their names" (PDF 130).
   The body itself says "the next four" (`:399`). Replace with: "Four of them, the second
   to the fifth, are the same fault, a name of one kind put where a name of another belongs."
3. **"Rarely" for "not one".** `part_a.py:170` and `:392` say philosophers *rarely* begin
   from definitions. Hobbes says "there is not one of them that begins his ratiocination from
   the Definitions" (PDF 130). Replace "rarely begin" with "never begin", or with "none of
   them, he says, begins".
4. **Laughter misdefined.** `part_a.py:865` says "Laughter is 'Sudden Glory'". Hobbes says
   sudden glory "is the passion which maketh those Grimaces called LAUGHTER" (PDF 139).
   The passion is sudden glory and laughter is its grimace. Replace with: "Sudden glory is
   the passion whose grimace is laughter, and…"
5. **The shipmaster is not Chapter 6's case.** `part_a.py:1207` says "The storm preset is his
   own case about fear", and `:1216-1217` says "In Chapter 21 he returns to the example".
   Chapter 6 states the principle only (PDF 141). The goods thrown into the sea appear first
   in Chapter 21 (PDF 242). Replace with: "The storm preset is a case Hobbes himself uses,
   though not until Chapter 21." Then change "returns to the example" to "gives it".
6. **The schools' definition misattributed.** `part_a.py:1171-1173` says "He keeps the schools'
   ordinary thought, that the will is the appetite that results from a deliberation". That
   wording is Hobbes's proposed substitute, not the schools' view: "if in stead of a Rationall
   Appetite, we shall say an Appetite resulting from a precedent Deliberation, then the
   Definition is the same that I have given here" (PDF 140–141). Replace with: "He offers a
   repair: put 'an Appetite resulting from a precedent Deliberation' in place of 'rational
   appetite', and the schools' definition becomes his own."
7. **Wit preset misreads Hobbes's table.** `part_b.py:410-414`, the `wit` preset
   (`:542-543`) and mistake 1 (`:681-685`) say "His own examples make the lab's wit preset".
   The orator is defined as fancy only, so "the orator… does not [have wit]", and "the
   historian has no fancy". But in orations "the Judgement does but suggest" circumstances,
   and history uses fancy "in adorning the stile" (PDF 147). Hobbes never says the orator
   lacks wit. Use his own cases instead. Rename `the-orator` to `the-digresser` (fancy:
   "snatched from their purpose", PDF 147) and `the-historian` to `the-counsellor`
   (judgement: "in Councell… Judgement does all", PDF 148), and update the claims and pins. Prose:
   "His own cases make the preset: the counsellor, in whom judgement does all; the
   digresser, all fancy and no direction; and the poet, both."
8. **Wit quiz has an arguable distractor.** `part_b.py:637-638`, Q1 "According to Hobbes,
   what is wit?" Option A, "Fancy, the noticing of likenesses that others rarely see", is
   supported by the text: those who notice rare similitudes "are sayd to have a Good Wit, by
   which, in this occasion, is meant a Good Fancy" (PDF 146). Reword the question as "Which
   does Hobbes say is wit, and which is not?" Replace A with "Fancy without judgement" and
   keep B as the answer.
9. **The table misstated (navigation).** `part_b.py:868-869` says "navigation is mathematics
   is false, since it lacks the branch called determined". In the printed table (PDF 157,
   image) mechanics and cosmography hang under "Consequences from Motion, and Quantity
   *determined*", beside mathematics. What separates them from mathematics is the branch
   "by Figure / by Number". The defs at `:906-912` and `:945-950` encode the error. Fix: add
   `determined` to `cosmography` and `mechanics`, add a simple `figure-or-number` to
   `mathematics`'s parts, and add it to `simple` in both presets. I tested this in the lab
   and all 16 verdicts stay as pinned. Prose: "…is false, since it lacks the branch of figure
   and number that mathematics hangs from."
10. **Giddiness is not a middle grade.** `part_b.py:436-438` ("three grades of passion") and
    `:690-691` ("dullness and madness at opposite ends and giddiness between them") misstate
    the list. Hobbes's giddiness is "Passions indifferently for every thing" (PDF 150): passion
    spread wide, not passion of middling strength. The preset does not place it between
    either. Replace with: "dullness and madness are weak and vehement passion, and giddiness
    is passion spread over everything", and in the mistake: "The wit preset puts dullness and
    madness at opposite ends, and giddiness off that scale."
11. **Suárez: a chapter title, not a sentence.** `part_b.py:491-492` says "a sentence from the
    Jesuit Francisco Suárez, which he translates". Hobbes says the words "are the Translation of
    the Title of the sixth chapter of Suarez first Booke" (PDF 155). Replace with: "the title of
    a chapter of the Jesuit Francisco Suárez, which he translates".

## SHOULD-FIX

1. `part_a.py:477-479`: "three of them turn insignificant". Only two turn: the
   transubstantiate claim was already insignificant. Replace with: "two more turn
   insignificant, three in all".
2. Lesson 2 never says that the four-way split is the lab's. Hobbes treats "Absurd,
   Insignificant, and Non-sense" as one (PDF 130; and PDF 126). Lesson 6 says so, but
   lesson 2 introduces the verdicts. Add to the note at `:716-722`:
   "Hobbes uses absurd and insignificant for the same fault; the split between a clash and an
   empty name is the lab's."
3. `part_a.py:474-476`: "it follows… that a creature is not a man". On the lab's rule "false"
   means a part is missing, not that the negation follows. Replace with: "and that a creature
   is a man does not follow".
4. `part_a.py:1203-1206`: "it is why he can say that the schools' rational appetite makes no
   difference". He says the definition "is not good", for a different reason. Replace with:
   "and it is why the schools' rational appetite has no place in his definition".
5. `part_a.py:122-125`: "his remark… explains why the failure tempts people" is a gloss
   given as Hobbes's. Write "can be turned to explain".
6. `part_b.py:396-397`: "wit is judgement" is the conclusion of one comparison. Natural wit
   is "Celerity of Imagining… and steddy direction" (PDF 146). Say so once.
7. `part_b.py:435`: "Madness… is the same thing as wit, turned up". On Hobbes's account it
   is *passion* turned up. Replace "wit" with "the passions that make wit".
8. `part_b.py:740`: "the shortest of the five lessons' sources" should read "the shortest of
   the five chapters this course reads".

## NOTE

- `part_a.py:510`: the virtue-and-vice names are at the end of Chapter 4, on the page where
  Chapter 5 begins (PDF 127). Better: "at the end of Chapter 4".
- `part_a.py:1132-1133`: the will comes four paragraphs after deliberation, not "the next but one".
- `part_a.py:1161`: "surprised many readers" is unsourced. Cut it.
- `part_a.py:501`: "The Light of humane minds…" comes before the sapience paragraph, so it is
  not the chapter's conclusion.
- `part_a.py:875`: Butler preached the sermons in 1726 and became a bishop in 1738, so "later
  a bishop" is more accurate.
- `part_a.py:98`: Leviathan does not describe the middle term cancelling. Say "as the lab
  models it", not "as Hobbes counts it".
- Strengths: critics are put at strength and with people in them. The Chapter 8 Scripture
  passage is fair. The labs carry the argument, not decoration. Each lesson closes on the gap.

**Verdict:** sound and well taught. The eleven MUST-FIXes are local misreadings, each with a
mechanical replacement. Fix them and the course is ready.
