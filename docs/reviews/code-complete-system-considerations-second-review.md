# Second review (accuracy): Code Complete, Course 6 — System Considerations

Course: `code-complete-system-considerations` (`content/code_complete/c6_system_considerations/`),
four lessons (Chapters 27–30). Brief: `docs/code-complete/SECOND-REVIEW.md`. Reviewed
2026-10-25 against the private extraction of the second edition (printed page = PDF
page − 37), reading the pages each lesson cites (pp. 649–659, 661–688, 689–708,
709–725) with `pg.py`/`ccbook.py`.

**Scope note.** The orchestrator told this reviewer to write only this file and not to
edit lessons, so nothing in the course or in PLAN §C was changed. Every finding below
is a recommendation, with the exact fix where it is mechanical.

## Gates

- Preview: `python3 scripts/preview_subject.py code_complete --course code-complete-system-considerations`
  → 5 pages; labcheck 4 pages executed, 4 with pinned figures, 0 failing; **OK**.
- `labcheck.js --observe`: every preset's tiles match the body prose, the worked lines,
  §C and my hand count. small-team 3 / 0–400 / 2/5 = 0.40 to 5 / 25/2 = 12.50; medium
  45 / 200–7,000 / 5–100 / 20; large-team 1,225 / 4,000–100,000 / 100 to 10000/7 ≈
  1,428.57 / 100/7 ≈ 14.29. strong-team 1349/2500 ≈ 0.54 / 53.96; weak-team 4757/2500 ≈
  1.90 / 190.28; hard-product 1035213/250000 ≈ 4.14 / ≈ 414.09 (1.74 × 1.63 × 1.46 =
  4.140852). top-down 5 stubs, 0 drivers; bottom-up 0, 5; risk-first 3 (db, ui,
  widgets), 2 (orders, pricing), each traced by hand through the order. header 2 / 3;
  source 1 / 2.
- Browser (Playwright, served locally), each exercise entered as the body says: lesson 1
  People 6 → 15, 12 → 66; lesson 2 Nominal 50 with 1.34 and 0.78 → 2613/2500 ≈ 1.05,
  52.26; lesson 3 the four pairs and `app ui core store` → 3: core, store, ui / 0: none;
  lesson 4 `util.c` → 1: util.o / 2: app, util.o; lesson 4 quiz 2's added `test` target
  → 4: app, main.o, test, util.o. All agree with the quiz `why`s. No console errors. The
  box names the body uses (People, Nominal effort, Factors, Calls, Integration order,
  What changes) are the labels on the page. No exercise answer appears in body prose.
- Code: `INTEGRATION_EXERCISE` compiles with `javac` as given (four package-private
  classes; static calls) and its calls are exactly the exercise's four pairs.
  `MAKEFILE_EXERCISE` is valid make dependency syntax and is the same six records as
  `BUILD_EDGES`. No §D.4 snippet is used; no excluded Java feature appears.
- `# F` comments: **6** (F1 p. 654, F2 p. 652, F24 p. 652, F25 p. 653, F26 p. 674, F29
  p. 682), each checked on the page. Every research figure in the course is covered;
  see consider-13 for two rule-of-thumb numbers without a comment.
- `cc_quotes.py`: 11 quotations, all **OK** — L1 p. 659 (21), p. 658 "right-weight" (1):
  total 22; L2 p. 688 (35), p. 683 "religious" (1): total 36; L3 p. 708 (21), p. 691
  "big bang integration" (3), p. 696 "dump truck full of stubs" (5), p. 702 "smokes"
  (1): total 30; L4 p. 725 (14), p. 722 "Tool Fantasyland" (2, the section title),
  p. 706 "too much of a good thing" (6): total 22. All within 40 (opening) and 60
  (lesson). Each opening quotation is a bullet of its chapter's Key Points, as the body
  says. Bookkeeping gaps in should-fix 8.
- `speechcheck.py` has no row for code-complete yet, so the read-out was checked from
  the rendered `data-say` attributes and with `speech.say_code` directly (must-fix 1,
  should-fix 9).

## Findings

Ranked: **must-fix** (a claim about the book that is wrong, or a read-out that states
the wrong thing), **should-fix**, **consider**.

### Must-fix

1. **Read-out: the path formula is read as "n negative".** Wherever `n·(n − 1)/2` sits
   in prose, the renderer marks only the island `n·(n −` and reads it in the code
   dialect as "n times, open bracket, n negative". The TTS voice then reads the rest,
   ` 1)/2`, as raw text. That happens 9 times: in `footer_lead` on all five pages, in
   the course outcome on the index page, and in lesson 1's first concept, its `def`
   block and the lab paragraph ("Communication paths is n·(n − 1)/2"). This is the
   course's central formula, and the reading says "negative" where the page says minus.
   Kit cause: `speech.islands` stops at the space before `1`, and `say_code` reads
   U+2212 after a space as unary negation. Fix in the content, either:
   - put it in a backtick run, `n * (n - 1) / 2`, which reads "n times, open bracket,
     n minus 1, close bracket, divided by 2"; or
   - write it in words, "n times (n − 1), halved", which gives no island and reads
     cleanly.

   In the same family, lesson 1's key line `paths = n·(n − 1)/2` reads "n times n minus
   1, divided by 2", which loses the grouping (it could be heard as n² − 1). Write
   "paths: n times (n − 1), halved" there.

2. **Course `not_covered`: Chapter 28 cannot point to "McConnell's own later work".**
   "Estimation as a discipline. Chapter 28 points to whole books on it, among them
   McConnell's own later work". The chapter's estimation references (p. 671 margin,
   pp. 677–678) are Boehm 1981, Boehm et al. 2000, Humphrey, Conte et al., Gilb and
   McConnell's *Rapid Development* (1996). The book on estimation that PLAN §G means
   ("McConnell's later book on estimation") came after 2004, so the 2004 chapter
   cannot point to it. Fix: "Chapter 28 points to whole books on it, among them Boehm's
   on Cocomo II and McConnell's own *Rapid Development*; the lesson does only …".

### Should-fix

3. **"Putnam and Meyers" → "Putnam and Myers".** Lesson 1's productivity concept, the
   lab's `panel_intro` and the lesson comment follow the source line under Table 27-2
   (p. 653), which misprints the name. The book's own bibliography (pp. 878–879) gives
   Lawrence H. Putnam and **Ware Myers**, and so does PLAN §S.1. Use "Putnam and Myers"
   (S.2 F25's "Meyers" should be corrected to match).

4. **Lesson 4 quiz 4: one distractor is partly the book's position.** The distractor "A
   five-hour job done once" is the book's own case for building a tool. Section 30.5
   (p. 721) says most good programmers would spend 4 h 45 min building a tool for a
   one-off five-hour job, and p. 722 calls a script "a tool that automates a repetitive
   chore". The `why`'s answer, "about building a tool … not a script", splits a hair
   the book does not split. Replace the distractor with one the rule clearly excludes,
   e.g. "A three-character command typed a few times a day" (the off-by-one of the
   "longer than about five characters" condition), and say so in the `why`.

5. **Lesson 3 `one_line`: "every incremental order pays for itself in stubs, drivers or
   both".** "Pays for itself" means it earns back its cost, the opposite of what is
   meant. Fix: "… and every incremental order pays for it in stubs, drivers or both."

6. **Lesson 1 concepts overstate the tables' monotonicity.**
   - "both ends of the range rise as the size does" is not quite true of Table 27-1. Its
     low ends are 0, 0, 0.5, 2, 4, so the first two bands share the low end.
   - "the ranges fall as the size grows" is not quite true of Table 27-2. Its high end is
     25,000 at both 1K and 10K.

   Fix: "and from the smallest band to the largest both ends rise" and "and from the
   smallest row to the largest both ends fall". These match the book's "general trend"
   (p. 653).

7. **Lesson 2: "the survey the book cites found delays growing toward a project's end"
   should name the survey.** §F.5 forbids "studies show" without the study. The book
   (p. 675) gives van Genuchten 1991, a survey of over 300 projects. Write "a survey of
   over 300 projects that the book cites (van Genuchten 1991) found …", and add van
   Genuchten 1991 to §S.1 "as the book cites it".

8. **Quotation bookkeeping.** All the quotations are on the page, but the records
   don't match them:
   - Lesson 2's comment says "the lesson quotes nothing else", but the body quotes
     "religious" (p. 683, not 682; total 36 words).
   - Lesson 3's comment omits "smokes" (p. 702; total 30, not 29).
   - None of the short phrases is recorded in §C's Course 6 entries: "right-weight",
     "religious", "big bang integration", "dump truck full of stubs", "smokes", "too
     much of a good thing". The second-review brief counts an unrecorded quotation as a
     finding. Add them to the "As authored" note under Course 6 in §C, with pages, and
     fix the two comments.

9. **Read-out: the article "a" is read as the letter "A" in key and worked lines.** In
   the code dialect, `speech.py` (lines 497–507) reads a lone `a` as the variable. So
   these lines say the letter "A":
   - lesson 1's key "construction: a smaller share";
   - lesson 3's key "one piece at a time";
   - lesson 3's worked line "calls widgets, a stub";
   - lesson 4's keys "a build redoes what depends on a change" and "a header reaches
     every file including it".

   The same read-out drops semicolons, so lesson 3's worked line is heard as "already
   in calls widgets" and "… widgets drivers none". Reword without the article ("one
   piece each time", "construction: smaller share as size grows", "each header reaches
   every file including it"), and split each semicolon line into two lines. Kit fault
   to record: the article heuristic does not apply on key/worked lines.

### Consider

10. **Lesson 1 `mistakes[1]`: "Half of a larger number of errors is still the largest
    single share."** The book (p. 652) says requirements and architecture "make up the
    difference" and does not split that half. "Largest single share" is the lesson's
    inference. Safer: "and half of a larger number of errors is still a great many".

11. **Lesson 2 paraphrases all six steps of the estimation procedure the book adapts
    from Boehm 1981** (pp. 671–672), and quiz 4 reuses three of them. This is prose,
    not a checklist, so §E.3's two-or-three-point limit does not strictly apply.
    Trimming the body to three steps (several techniques, low level of detail,
    re-estimate) would keep well inside its spirit.

12. **Lesson 2: "a manager how construction looks from the developer's chair".** The
    book (p. 661) says "how management looks to developers". Fix: "and a manager how
    management looks from the developer's chair".

13. **Lesson 4 uses two of the book's numbers without a page comment.** These are the
    4 h 45 min / 15 min tool example (p. 721) and the "about five characters, more than
    a few times a day" rule (p. 722), and the lesson comment says "No figure from the
    book is used". They are rules of thumb, not research figures, so no §S.2 id is owed,
    but a page comment would make the claim checkable.

## What I checked and found right

These are checked on the page, so a later reviewer does not re-raise them.

**Lesson 1**
- Figure 27-1's 1/3/6/10/45 paths (p. 650), and the 50 people reading and writing
  documents.
- The Gigatron opening (p. 649): 30× effort, 15× errors, 25×/40× activities, and the
  first larger project getting out of hand.
- §27.2's team and programmer shares (p. 651).
- F2 including Grady's "up to 75 percent" at 500,000 lines (p. 652); F24; F25 and "vary
  dramatically" (p. 653).
- F1, the 512K cut-off "to protect my job" (p. 654), and the activity list (pp. 654–655).
- The methodology passage (p. 657) and Boehm and Turner on scaling up (p. 658).

**Lesson 2**
- The woolly mammoth and the architect-set standards (p. 662).
- Two people on every part, reviewing every line, routing good code and public assets
  (pp. 662–663).
- The change-control definition and "change control" (p. 664); overcontrol (p. 665).
- Change requests in groups, estimating cost and ripple, and volume as a warning sign
  (p. 666); "10 times as often" no change control (p. 667); testing a restore (p. 669).
- The estimation approaches and Boehm 1981 (pp. 671–672).
- Table 28-1, including "time constraint (of the application itself)", which supports
  the `hard-product` gloss (p. 674).
- Brooks's law, the baby analogy, the partitionable qualification and reducing scope
  (p. 676). Brooks managed OS/360 (p. 658).
- Measurement and outliers (pp. 678–679); Sackman et al. (p. 682); the religious-issues
  list (p. 683); educating the manager or finding another job (p. 686).

**Lesson 3**
- The University of Washington stadium in "the Pacific Northwest, where I live" (pp.
  689–690).
- Phased integration as "big bang" (p. 691), and two or three classes "if you're lucky"
  (p. 692).
- Top-down: control logic early, a visible system, the tricky system interfaces last
  (p. 695); the dump truck, error-prone stubs, nearly impossible purely, vertical slices
  (p. 696).
- Bottom-up needs the whole design first (p. 697); sandwich after Myers 1976 (p. 698).
- "Making these names up" and heuristics rather than procedures (p. 702).
- The daily build, broken builds and automation (pp. 702–705); continuous integration
  "too much of a good thing" for most projects (p. 706).

**Lesson 4**
- Kinds not brands (p. 709).
- The source-code tools in the lesson's list (pp. 710–715).
- The build tool's purpose and make/ant (p. 716); the Word group's full rebuild
  (p. 717).
- The UNIX tools (p. 720).
- The tool-building example, tool groups and project tools (p. 721); scripts (p. 722).
- Fortran, the 3GL–visual-programming list, essential difficulty, and "run!" or smile
  (pp. 722–723).
- The modern aside states the book's position at strength and the later practice
  fairly, and leaves it unsettled (§F.4). It is the course's only one, in the lesson
  §F names.

## Claims I could not settle against the page

None. Every claim in the four lessons was found on the cited pages. I did not consult
an original study: every figure in the course is used as the book prints it, with the
book's citation.

## Disagreements with the pedagogy assessment

None to record. No pedagogy assessment for this course exists yet: neither
`docs/pedagogy/code-complete-system-considerations.md` nor
`docs/reviews/code-complete-system-considerations-pedagogy-review.md` was present when
this review was written.

## Author's response

All must-fix and should-fix items of both reviews (this one and
`code-complete-system-considerations-pedagogy-review.md`) are applied, and so
are most of the consider items. After the changes, preview prints `OK`, with 4
pages pinned and 0 failing.

**Applied from this review**
- 1: the path formula is written in words in prose (concepts[0], the `def`, the
  lab paragraph, the course outcome and the course `footer_lead`). The symbolic
  form stays only in key lines with spoken forms, which now say "n times the
  quantity n minus 1, halved". The shared `footer_lead` in
  `content/code_complete/__init__.py` has no formula, so it was not touched.
- 2: `not_covered` now names Boehm on Cocomo II and McConnell's *Rapid
  Development* (1996).
- 3: Putnam and Myers, in the lesson and in PLAN §S.2 F25.
- 4, 5, 6: done as proposed.
- 7: van Genuchten 1991 is named in the prose, "as the book cites it".
- 8: the quotation comments are corrected, and every short quotation is
  recorded in §C's "As authored" note.
- 9: the key and worked lines are reworded without the article "a", and each
  line with a semicolon is split in two.
- Consider items 10, 11 (the body keeps three of the procedure's steps), 12
  and 13 (page comments) are applied.

**Applied from the pedagogy review**
- MF-1 to MF-3, SF-1 to SF-4.
- C-2: the woolly mammoth is cut.
- C-3: the new distractor is "a program whose classes were each unit-tested
  first".
- C-5: one sentence gives Cocomo II's nominal figure at 100K.

**Declined, with reasons**
- Adding van Genuchten 1991 to §S.1: that section is outside this author's
  write scope while the Subject is being wired. The prose cites the survey as
  the book does. The orchestrator can add the row.
- Pedagogy C-1 (`=` in quiz `why` text): the quiz has no `data-say` and is not
  read aloud. The text is left as arithmetic, and the item is noted for whoever
  adds read-out to quizzes.
- Pedagogy C-4 (paths per person): it would need a new quiz item or option
  set, and lesson 1 is already the heaviest in the course.
- Kit and read-out faults are left for the engineers, not fixed in content:
  - the "1 people" banner;
  - the key block wrapping at phone width;
  - the integration table's fourth column being cut at phone width;
  - the article and semicolon heuristics on key and worked lines;
  - the island split at a spaced minus.
