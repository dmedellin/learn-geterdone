# Second review (accuracy): Code Complete, Course 1 — Laying the Foundation

Course: `code-complete-laying-the-foundation` (`content/code_complete/c1_foundation/`),
three lessons. Brief: `docs/code-complete/SECOND-REVIEW.md`. Reviewed 2026-10-25
against the private extraction of the second edition (printed page = PDF page − 37),
reading every page the lessons cite (pp. 3–21, 23–44, 55–56, 58–63, 66–70) with
`pg.py`/`ccbook.py`.

**Scope note.** The orchestrator told this reviewer to write only this file and not
to edit lessons, so nothing in the course or in PLAN §C was changed. Every finding
below is a recommendation, with the exact fix where it is mechanical.

## Gates

- Preview: `python3 scripts/preview_subject.py code_complete --course code-complete-laying-the-foundation`
  → 4 pages; labcheck 3 pages executed, 3 with pinned figures, 0 failing; **OK**.
- `labcheck.js --observe`: every preset's tiles match the body prose, the worked
  lines, §C and my hand count (small-project 1,000 / 33/50 = 66% / coding and
  debugging 8/25 = 32% / 6 of 8; large-project 12,000 / 31/60 ≈ 51.7% / 9/40 = 22.5% /
  6 of 8; found-late 425–800 / 35 / 85/7 ≈ 12.1× to 160/7 ≈ 22.9×; found-early 35 / 35 /
  1×; requirements-late 100–1,000 / 10 / 10× to 100×; java 4,000; python
  5000/3 ≈ 1,666.67; visual-basic 20000/9 ≈ 2,222.22).
- Browser (Playwright, served locally): the exercise entered as the body asks gives
  lesson 1 300 / 3/5 = 60% / coding 3/10 = 30% / 5 of 7, lesson 2 80–800 / 8 /
  10× to 100×, and lesson 3's quiz-2 input (9,000, 6) gives 1,500. All agree with
  the quiz `why`s. The exercise answers do not appear in body prose.
- `# F` comments: **9** (F1 ×2, F30 ×2, F3 ×2, F4 ×3 including the combined F5/F4
  line, F5 within those). Every book figure in the course is covered by a comment
  on its lesson dict or block; each checked on the page (F1 p. 7, F3 p. 29 and
  p. 39, F30 p. 55, F4 and F5 p. 62). No figure lacks one.
- `cc_quotes.py`: 7 quotations, all **OK** — L1 p. 8 (21 words), p. 14 Brooks (8),
  p. 12 (6): total 35; L2 p. 59 (21), p. 26 (5): total 26; L3 p. 70 (32), p. 63 (2):
  total 34. All within 40 (opening) and 60 (lesson).
- `speechcheck.py` does not yet cover the code-complete subject (no row; `--list
  code-complete` prints nothing), so the read-out was checked by reading the
  rendered `data-say` attributes instead (finding 7).

## Findings

Ranked: **must-fix** (a claim about the book that is wrong), **should-fix**,
**consider**.

### Must-fix

1. **Key Construction Decisions — the opening quotation is not the "last" key
   point.** The body's first `p` ("It is the last of the chapter's key points") and
   `read_intro` ("The quotation is the last of the chapter's key points") are
   wrong: p. 70 has five key points, and the quotation is the fourth; the last is
   the one on the technology wave. Fix: "It is the fourth of the chapter's five key
   points" (body) and "one of the chapter's key points" (`read_intro`).

2. **Construction and Its Metaphors — Section 1.2 gives five reasons, not four.**
   The body ("Section 1.2 (p. 6) gives four reasons to concentrate on construction")
   and the dict comment ("the four reasons p. 7") drop one of the book's five
   (p. 7): that with a focus on construction an individual programmer's
   productivity can improve enormously, which the book supports with Sackman,
   Erikson and Grant (1968) and later studies. A count of the book's own structure
   is a misstatement of it. Fix: "gives five reasons"; either add one sentence on
   the productivity reason (citing it as the book cites Sackman, Erikson and Grant
   1968; note the book says 10 to 20 here, where §S.2 F29's figure is "about 10 to 1"
   from §28.5 and §33.1, so if a figure is given it needs a §S.2 row and a `# F`
   comment), or name it in a clause without a figure. Correct the comment.

### Should-fix

3. **Construction and Its Metaphors — a self-contradicting sentence.** The body's
   lab paragraph says "on this illustration construction is mostly coding and
   debugging, as the chapter says, and still more than half other work." On the
   preset coding and debugging is 320 of 660 construction hours (48%), so it is
   not "mostly" construction; the worked `after` correctly says it is "less than
   half of that". Fix: "coding and debugging is the largest part of construction,
   as the chapter says, and still less than half of it."

4. **Upstream Prerequisites — `mistakes[0]` weakens McConnell's position.** "…and
   asks only that the most critical requirements and architecture be settled
   early." The book does not ask "only" that: p. 34 says a focus on prerequisites
   reduces cost whichever approach is used, and that an iterative project that
   ignores them can cost significantly more than a sequential one that attends to
   them; p. 28 asks even a highly iterative project to identify the critical
   requirements and architecture for each piece before constructing it; and the
   chapter's checklists are for every project, at a formality suited to it. The
   book's key point is "at least the most critical" (p. 34). Fix: "and asks that at
   least the most critical requirements and architecture be settled early." (The
   quiz-3 `why` already says "at least" and is right.)

5. **Key Construction Decisions — the provenance of Table 4-1 is overstated.** The
   body ("The ratios are averages over the programs those authors studied"), the
   panel intro ("an average over the programs they measured") and the `note`
   ("the book's averages over the programs Jones, Boehm and Prechelt measured")
   claim more than p. 62 says. The book calls them "typical ratios" and says the
   table is adapted from Jones 1998, Boehm 2000 and Prechelt 2000; only Prechelt's
   is a measurement of programs, and Jones's and Boehm's are estimation tables.
   Fix: "typical ratios, which the book adapts from Jones 1998, Boehm 2000 and
   Prechelt 2000; not constants of the languages" in all three places.

6. **Key Construction Decisions — the whole of Table 4-1 is set out in prose.** The
   §4.1 paragraph lists all eight ratios (C++, Java, Fortran 95, Visual Basic,
   Perl, Python, Smalltalk, and C by implication). PLAN §E.3 allows a table's
   figures "a few at a time"; the lesson uses three (Java, Python, Visual Basic).
   F4 registers all eight, but the register is not licence to reproduce the table.
   Fix: give the three the lab uses and "and the others in your copy". (Table 3-1's
   full twelve cells are §C's settled design, the lab's input, and not re-raised.)

7. **Upstream Prerequisites — the read-out says "is set to" for arithmetic.** In the
   rendered page the body run "10 × 10 = 100, 5" is spoken "10 times 10 is set to
   100, 5", and "20 × 10 = 200" "20 times 10 is set to 200": the code dialect is
   reading `=` in prose arithmetic as assignment, and the first run also swallows
   the ", 5" that begins the next clause. A listener hears an assignment where the
   lesson means equality. Fix in the lesson: write "10 × 10 is 100" and
   "20 × 10 is 200" in that paragraph (as the worked lines already do), or add
   spoken forms for those two runs in `content/spoken/code_complete.py`. Kit or
   renderer note for the orchestrator: a `=` inside a `×` run in prose should read
   "equals"; the same will recur in other courses' worked prose.

8. **Upstream Prerequisites and Construction and Its Metaphors — four quotations
   §C does not record.** Brooks's line (p. 14, 8 words), "an algorithm in a clown
   suit" (p. 12, 6), "Why Isn't Sam Coding Anything?" (p. 26, 5) and "disguised
   Fortran" (p. 63, 2) are correct and within the limits, but PLAN §C records only
   each lesson's opening **Quote**, and the brief counts an unrecorded quotation as
   a finding. Fix: add a line to each §C entry listing them with page and word
   count (the dict comments already carry exactly that).

9. **Key Construction Decisions — the snippet is not recorded in §C.**
   `SEND_WITH_DEFAULT` (16 lines, no lab figures) is new to the lesson; AUTHORING.md
   asks for a new snippet to be recorded in the course's §C entry. Add one line to
   §C 1.3 ("body snippet `send` with a default, 16 lines; line 6 forwards
   `DEFAULT_RETRIES` from line 3 to lines 9–16"). The snippet itself is sound: it
   compiles as a class-body fragment (`Message` and `transmit` are named in the
   prose as stand-ins), the line numbers the prose names (6, 3, 9 to 16) are right,
   and it does what the prose says.

### Consider

10. **Construction and Its Metaphors — "the intuition is fairly accurate"** is
    attached to "filed all of it under programming". On p. 4 the "fairly accurate"
    intuition is that the main activity of informal work is what researchers call
    construction, not the lumping of every activity together. Suggest: "you
    probably grouped it all as programming, and the activity you thought of first is
    what the book calls construction: a fairly accurate intuition that lacks
    perspective."
11. **Construction and Its Metaphors — small strengthenings.** "Real projects skip
    requirements and design… and drop testing" (p. 7 says imperfect real-world
    projects often do); "The metaphor he finds most useful is building" (p. 16 says
    more useful than writing or growing); and `mistakes[0]`'s "throwing one away is
    the most expensive way to learn" is the lesson's phrase, not the book's (p. 14
    calls it poor advice and says get it right first time or take your chances while
    they are cheapest). Each is a word or two to soften.
12. **Upstream Prerequisites — "some of a project's success or failure is
    settled"** (body and summary): p. 23 says "much of". Suggest "much".
13. **Upstream Prerequisites — lists paraphrased in full.** The body paraphrases all
    six of §3.4's ways of handling requirements changes and five of the six criteria
    for a sequential approach (p. 35). Neither is one of the book's titled
    checklists, so §E.3's "two or three points" is not strictly breached, but the
    spirit argues for three of each and "the rest in your copy". (The §1.1 activity
    and task lists in lesson 1 are needed for the lesson's own count and §C directs
    them; keep.)
14. **Key Construction Decisions — the listing's spoken comment.** Line 1's comment
    is read "The team's convention the. line 2, comment, full version holds…": the
    sentence runs across two comment lines and the read-out ends line 1 on "the".
    Rewording the comment so each line ends a phrase ("// Java has no default
    argument values. Team convention:" / "// the full version holds the logic; each
    shorter one forwards to it.") would read cleanly.
15. **Course `how_to`** says the book's figures are syntheses "from the 1970s to
    2003"; the Table 3-1 sources run to Boehm and Turner 2004. Trivial; "to 2004".

### Checked and right

- The pages, section numbers and titles the lessons cite; Chapter 1's activity and
  task lists; the nonconstruction list and the "coding" passage (pp. 4–6); F1
  (p. 7, "typically", 30 to 80 percent); Kekulé, the ether, Galileo and "worse to
  better" (pp. 9–11); searchlight, heuristic and the line-of-code sentence
  (pp. 11–12); writing, Brooks 1975 and 1995 (both dates are the book's, pp. 14 and
  16), farming's lack of control (p. 15), accretion, building and the toolbox and
  combining (pp. 15–20).
- Chapter 3: the three reasons preparation is skipped and WISCA (pp. 25–26); the
  three appeals (pp. 27–29); every Table 3-1 cell, the $1,000/$15,000 example and the
  sources (p. 29); p. 39's smaller-projects remark and its "on large projects"
  framing (which supports the `note`'s "many of them large"); §3.2's "misinformed",
  its illustrative tables (the iterative project with prerequisites cheapest, $550K),
  "useful much more often" and the two ways to go wrong (pp. 33–36); problem
  definition and the calculator example (p. 37); requirements and the myth of
  stability (pp. 38–41); architecture's conceptual integrity and error cost (p. 44);
  F30 and requirements as its own project (pp. 55–56); Beck 2000 in the chapter's
  further reading (p. 58).
- Chapter 4: tool belt and truck (p. 61); F5 and F4 (p. 62); Sapir-Whorf and the
  Fortran story (p. 63); the painting and retrofitting (p. 66); the wave dates and
  "even more" (p. 67); Gries 1981 (p. 68 and the bibliography); the Visual Basic
  convention and "intellectually manageable" (pp. 68–69); "critical to understanding
  this book" (p. 69); §4.4's either-combination sentence and three checklist points
  paraphrased (pp. 69–70).
- Quiz: every distractor checked. L1 Q1 (90, 160, 230 each name the misreading it
  is), L1 Q2–Q4, L2 Q1 (40–80 is the construction cell, 80 the system-test cell),
  L2 Q2–Q4, L3 Q1–Q4 (2,000, 3,600 and 54,000 are the other ratios and the
  inversion) each have exactly one defensible answer; no verdict is quizzed; every
  book figure asked is asked at §S.2's strength with its source in the `why`.
- §F: one opening scene in three lessons (Upstream Prerequisites); the course's
  one modern aside is in Upstream Prerequisites' `note`, states the agile view and
  the book's §3.2 position each at strength and settles neither; no language war,
  no "outdated"; each lesson's last `p` names the next lesson or course.
- Presets' instances equal §C's; the exercise is never a preset; `worked` works a
  preset in every lesson.

## Claims not settled against the page

- None of the lesson's claims about the book remain unsettled. Two statements go
  beyond the book and were judged from general knowledge, not checked online:
  Java gained `assert` in 1.4 and `enum` in 5 (both well established), and the
  `note`'s characterisation of the agile view (that practices making change cheap
  flatten the cost-of-change rise) is a fair summary of Beck's *Extreme Programming
  Explained*; neither is attributed to McConnell.

## Disagreement with the pedagogy assessment

No pedagogy assessment exists yet for this course
(`docs/pedagogy/code-complete-laying-the-foundation.md` is absent), so there is
nothing to compare. Whoever writes it should note findings 1 and 2, which sit in
the lessons' framing sentences a pedagogy read is likely to praise.

## Author's response

Both reviews (this one and `code-complete-laying-the-foundation-pedagogy-review.md`)
were applied in `content/code_complete/c1_foundation/`, with the §C entries for the
course updated in the same change. Preview afterwards: OK, 3 pages pinned, 0 failing.

**Applied from this review:** 1 (the fourth of five key points; `read_intro` "one of");
2 (five reasons, the productivity reason named with Sackman, Erikson and Grant 1968 and
no figure; comment corrected); 3; 4 ("at least"); 5 ("typical ratios, which the book
adapts from…", in body, panel intro and note, and the concept and step wording); 6 (three
ratios, "the others in your copy"); 7 ("that is 100", "that is 200"); 8 and 9 (§C now
records the other quotations and the snippet); 10; 11 (all three softened); 12 ("much
of", body and summary); 13 (three points of each list and "the rest in your copy");
14 (the comment lines are now one sentence each, per the pedagogy review's S4, so line
numbers hold); 15 ("to 2004").

**Applied from the pedagogy review:** M1, M2, M3, S1–S5, C1 (the ether sentence cut),
C2. Two deviations in M1: the first described defect was reworded ("the specification
says refunds are rounded half up; the customer's contracts require half to even") so
that its phase cannot be read as construction; and the reviewer's fourth option,
"45 to 125 … places the tax defect in construction", does not add up (that placing gives
30 to 150), so the fourth option is "45 to 150 units, 15× to 50×", which places the
rounding rule in construction. Answer 45 to 225 against 3, 15× to 75×, checked in the
lab with `req, post, 1; arch, post, 1; cons, post, 1`. In S2 the exercise's seventh
activity is now user-interface design; the answer is unchanged (3/5 = 60%, checked).

**Declined, with reasons:**
- Pedagogy C3 (the kit's mode titles above the panel; the clipped table header on a
  phone) and C4 ("p." and "pp." spoken as written): kit and read-out matters, outside
  the course files. Passed to the orchestrator.
- Pedagogy C5: agreed, not a change. `speechcheck.py` cannot see the Subject until it
  is wired; the read-out was checked by `say_code` on every run and the rendered
  `data-say`, and the author's report says so.
- Pedagogy M3's dialect bug (a lone "a" read as the letter) is being fixed in
  `speech.py` by the renderer engineer; the key lines were reworded anyway, since the
  new wording is no worse on the page.
