# Pedagogy review: Laying the Foundation (`code-complete-laying-the-foundation`)

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, after authoring,
against the `pedagogical-expert` brief, `docs/code-complete/PLAN.md` (§0, §B,
the course's three §C entries, §E.4, §F), `docs/code-complete/AUTHORING.md`
and the pre-authoring review `docs/reviews/code-complete-spec-pedagogy-review.md`.
Source: `content/code_complete/c1_foundation/__init__.py` and `part_a.py`. All
three lessons were read in full. The course was rendered with
`scripts/preview_subject.py` (4 pages; labcheck OK, 3 pages with pinned
figures, 0 failing) and every page was opened in Chromium through Playwright
at 390 px and 1280 px: no horizontal overflow on any page, no console errors,
every lab driven with the exercise's own input and with malformed input, every
quiz item clicked through, and the read-out's transcript dumped by the page's
own text builder. Claims about the book were checked against the operator's
text with `ccbook.py`; nothing from the text is reproduced here.

## Verdict

The course delivers what the specification promised, and in two places more.
Every lesson opens with the chapter's own key point, sets out the argument
section by section in paraphrase that names whose claim it is, and turns in its
second half to a count the reader can do by hand; every `mistakes[0]` is the
§C misconception and the later agile view sits in Upstream Prerequisites'
`note`, stated at strength and left open, exactly as finding #15 asked; every
last step sends the reader to their own calendar, tracker or language with an
observable result (#3); the `language` view is one tile with the caveat in
prose (#9); the writing-metaphor and missing-keyword misconceptions have real
holders (#17); the merged first lesson works (#21), and the Chapter 2 story,
Brooks moving from "throw one away" to incremental development, is the best
paragraph in the course. The labs behave: the exercise inputs give
`3/5 = 60%`, `80–800` with `10× to 100×`, and `1,500`; a tag other than `c`,
a word where a number should be, an impossible stage pair (`cons, req`) and a
ratio of 0 each produce a sentence that names the entry and what it should be.

What is wrong is concentrated in the second lesson's exercise, two factual or
near-factual slips, and the read-out, which mangles the course's key lines
and one paragraph of arithmetic. None of it needs a structural change.

## Must-fix

**M1. `upstream-prerequisites`: the exercise skips the act the lesson itself
calls the hard part.** The body's lab paragraph ends: "What the lab cannot do
is tell you which phase a defect was introduced in. That is a judgement made
by reading the defect, and it is the hard part of using the table at all."
The first step is "Place each defect". The exercise is then `req, post, 8`:
one record, both phases given, times a cell printed two paragraphs earlier
(10 to 100), and the `requirements-late` preset on the same page already shows
the identical cell and the identical ratio, 10× to 100×, on 10 defects instead
of 8. The reader multiplies by 8 and learns nothing the preset had not shown;
the one judgement the chapter asks for is never practised; and the quiz item's
answer is, in all but the multiplier, on the page, which §B's rule exists to
prevent. This is §C's exercise as written, so the fix is a §C change recorded
in the same commit.

*Replacement.* Keep the `ul` as three defect descriptions and make placing
them the exercise:

> ("ul", [
>   "A refund is rounded to the nearest cent; the customer meant, and the sign-off said in a footnote nobody read, round half to even. Found by an auditor a year after release.",
>   "Tax is computed in the order screen and again in the invoice service, and the two disagree on a boundary date. Found by a customer.",
>   "A loop that totals a basket skips its last line. Found by a customer.",
> ]),
> ("p", "Three defects in a released system. For each, decide the phase it was introduced in by Sections 3.3 to 3.5: a rule the specification got wrong is a requirements defect, a responsibility placed in two modules is an architecture defect, a mistake inside a routine is a construction defect. Then price the three by Table 3-1 as the lesson gives it, against the 3 units they would have cost found where each was made, and state the ratio. When you have an answer, enter your three records in the lab to check the arithmetic; it cannot check the placing."),

Answer, for §C and the first quiz item's `why`: requirements (10–100),
architecture (25–100), construction (10–25); 45–225 units against 3; a ratio of
15× to 75×. The quiz item becomes:

> q: "In the lesson's exercise, three defects are found after release: a rounding rule the specification got wrong, a tax calculation placed in two modules, and a loop that skips its last line. Placed by Sections 3.3 to 3.5 and priced by Table 3-1 as the lesson gives it, what do they cost against the 3 units of finding each where it was made?"
> a: ["30 to 300 units, 10× to 100×", "45 to 225 units, 15× to 75×", "30 to 75 units, 10× to 25×", "45 to 125 units, 15× to about 41.7×"]
> c: 1
> why: "The rounding rule is a requirements defect, 10 to 100; tax computed in two places is an architecture defect, the two modules sharing a responsibility, 25 to 100; the loop is a construction defect, 10 to 25. The sum is 45 to 225 against 3, a ratio of 15× to 75×. 30 to 300 prices all three as requirements defects; 30 to 75 prices all three as construction defects; 45 to 125 places the tax defect in construction. The cells are the book's synthesis after Fagan 1976 and others (p. 29), and p. 39 says that on smaller projects the post-release multiplier is closer to 5 to 10."

Each distractor differs from the answer by one placing, which is §E.4 item 5's
rule applied to a classification. The `standard` should then read "Given
short descriptions of defects and the phase each was found in, place each by
the chapter's sections, compute the total cost range by Table 3-1's cells and
its ratio to finding each where it was made, without the lab." The body stays
at 14 blocks. If the author prefers to keep §C's instance, the minimum is to
drop the `requirements-late` preset's ratio from the body paragraph and add
one described defect to place; but the version above is what the chapter
teaches.

**M2. `construction-and-its-metaphors`: "they are the two shortest chapters in
the book" is false.** The contents page gives Chapter 1 pp. 3–8 and Chapter 2
pp. 9–22; Chapter 14 is pp. 347–354 and Chapter 4 pp. 61–72, both shorter
than Chapter 2. A read-along that is wrong about the book in its first
paragraph loses the reader's trust for the figures that matter. *Replacement*
(first `p`): "Read Chapters 1 and 2 in your own copy first, pages 3 to 21;
Chapter 1 is the shortest chapter in the book and Chapter 2 is not much
longer, and the lesson goes back through them a section at a time."

**M3. The read-out speaks the course's key lines wrongly.** The `key` lines
are spoken through the code dialect, which reads a lone `a` as the identifier
A: the transcript has "fix A defect near where it was made", "program into A
language, not in it", "A ratio counts statements, not hours", and the course
page's "a count is a reason to look" will go the same way. A listener hears
the letter. This is a dialect defect the renderer should fix for every
Subject with `"speech": "code"` (a single-letter English article inside a
run of English words is a word), and until it does the lesson can avoid it.
*Replacements:* course `key` "fix defects near where they were made",
"program into the language, not in it", "counts say where to look"; lesson 2
`key` "fix defects near where they were made"; lesson 3 `key` "program into
the language, not in it", "ratios count statements, not hours". All under 46
characters. Report the dialect bug to the renderer task either way.

## Should-fix

**S1. `upstream-prerequisites`: inline arithmetic is spoken as assignment and
swallows the next clause.** The lab paragraph's `10 × 10 = 100, 5` is picked
up as a run and spoken "10 times 10 is set to 100, 5", and `20 × 10 = 200` as
"is set to 200"; meanwhile lesson 1's `33/50 = 66%` and `8/25 = 32%` in the
same position are not picked up at all and go to the voice raw. Whatever the
run detector does, prose arithmetic reads cleanly only in words.
*Replacement:* "10 requirements defects found in system test cost 10 × 10,
that is 100; 5 architecture defects found after release cost 5 × 25 to
5 × 100, that is 125 to 500; and 20 construction defects found in system test
cost 20 × 10, that is 200." In lesson 1, "the share tile 33/50, that is 66
percent" and "at 8/25, that is 32 percent". The `worked.lines` already use
"is" and are spoken correctly; this is only the body `p`s.

**S2. `construction-and-its-metaphors`: "user documentation" is not settled by
Section 1.1's list, and the exercise says to mark "by Section 1.1's lists".**
The section's outside list is management, requirements development,
architecture, user-interface design, system testing and maintenance; user
documentation is in neither list, so the "second look" the body promises
cannot be resolved from the chapter, and a reader who counts it gets 210/300,
which is not a quiz option. *Replacement:* "user-interface design, 30 hours",
which the section places outside explicitly and which a programmer is
tempted to count. The answer stays 180/300; the `why` becomes "...
requirements, system testing and user-interface design are not, the last by
name in Section 1.1's list of what construction excludes."

**S3. `upstream-prerequisites`, quiz item 3: the right answer is the only
qualified, two-clause option, and two distractors are unarguable.** "It pays
less for late defects, and pays in smaller instalments, but the cost is not
removed" is twice the length of the others, and "pays the after-release
multiplier on every defect" has no holder. *Replacement:*

> q: "By Section 3.2, what does an iterative approach do to the cost of defects found late?"
> a: ["Removes it, because each iteration finds its own defects", "Lowers it and spreads it over the project, without removing it", "Leaves it unchanged, whatever the order of the work", "Raises it, because each iteration reworks what the last one built"]
> c: 1
> why: "Iteration finds defects nearer the time they were made, so each costs less by Table 3-1, and absorbs the rework piecemeal instead of at the end; the defects are still found after the work that made them, so the cost is lowered, not removed. The chapter calls the view that iterative projects need no prerequisites misinformed, and adds that an iterative project which ignores them can cost more than a sequential one that attends to them."

The last sentence is the sharpest thing §3.2 says against the lesson's
misconception and the body does not use it; add it to the §3.2 paragraph too
("...and an iterative project that skips them can cost more than a sequential
one that does not").

**S4. `key-construction-decisions`: the snippet's two-line comment breaks
mid-sentence, and on a phone it is the first thing the reader sees clipped.**
At 390 px the listing scrolls (654 px of content in 308 px) and lines 1–2 show
"// Java has no default argumen" and "// full version holds the logi"; the
read-out speaks "The team's convention the. line 2, comment, full version
holds the logic, and each shorter one forwards to it.." Each comment line
should be a sentence. *Replacement:*

> // Java has no default arguments.
> // Each shorter send forwards to the full one.

Two lines still, so every line number in the prose (3, 6, 9 to 16) holds.

**S5. `construction-and-its-metaphors`, quiz item 3: the length tell again.**
The correct option is three lines; the distractors are one. *Replacement:*
a: ["A good technique with a poor image", "The book's preferred picture of
incremental development", "Adequate for one person's work and small projects
only", "A sign that incremental development is a mistake"]; the `why` already
carries the explanation.

## Consider

**C1. `upstream-prerequisites` has two light remarks (the Aztek, WISCA) and
`construction-and-its-metaphors` two histories (Kekulé, the ether and
Galileo; then Brooks).** §F allows one of each per lesson. All four are
McConnell's own, which is the preference, and none is long; if one goes, cut
the ether sentence, which is the least load-bearing, and keep Galileo, whose
"measured different things" is the chapter's point.

**C2. `key-construction-decisions`: the exercise's last sentence points the
reader at the quiz.** "The lab has nothing to say about this exercise; the
first question of the quiz does." The answer is only shown after a choice, so
the rule holds, but the sentence invites skipping ahead. "Write your three
conventions down before you reach the quiz, whose first item checks the
first of them" says the same and asks for the commitment.

**C3. The lab's generic headings on a phone.** The lab section opens "Where
the time goes · each entry's share of the total" (lesson 1), "Defect
arithmetic", "Project arithmetic": the kit's mode titles, above the lesson's
own panel title. On a phone the first thing under the exercise is the mode
title and a table whose third column header is clipped to "Sh" (the table
scrolls inside a region, with no visible cue). Renderer and kit matters, not
the author's; recorded so the second review does not mistake them for lesson
defects.

**C4. The read-out says "p. 8" and "pp. 36–55" as written.** Most voices read
"p" and "p p". A dialect rule mapping "p." to "page" and "pp." to "pages"
would fix it across the Subject; the lesson should not spell it out, since
the printed form is the book's.

**C5. `scripts/speechcheck.py` does not yet see this Subject** because it
enumerates `GENERATED_PATHS` and Code Complete is not wired in. §E.4 item 9
cannot be run until the orchestrator's wiring commit; the author's report
should say so rather than claim the check passed.

**C6. Reading length.** Bodies are 1,720, 1,631 and 1,387 words (about 9, 8
and 7 minutes at 200 words a minute, 15, 15 and 12 in §C with the lab and
quiz). Within §E.4 item 7. Lesson 1 is the one to watch if anything is
added.

## What was checked and is right

- Every opening quotation is the §C one, and the extra quotations (Brooks's
  line, "an algorithm in a clown suit", "disguised Fortran", "Why Isn't Sam
  Coding Anything?") are in the text at the pages the comments give; totals
  35, 26 and 34 words, under §E.3's 60.
- The paraphrase is at the book's strength: the writing metaphor "adequate"
  for small work; farming a good technique with a poor image; the accretion
  metaphor's strength that it does not overpromise; "misinformed" for the
  view that iterative projects need no prerequisites; the 5–10 post-release
  multiplier on smaller projects (p. 39); Gries 1981 as the source of
  in/into; "critical to understanding this book" (p. 69); construction
  planning and reviewing teammates' code inside §1.1's construction.
- F1, F3, F4, F5 and F30 carry their ids and pages in comments and are
  written as the book's synthesis after the sources it names. No other
  figure is attributed to the book.
- The three labs: presets named in body `p`s with their figures; every tile
  explained once (`pfPareto` in words in lesson 1); `worked` works a preset
  and the exercise's answer is in one quiz `why` and nowhere else, except as
  M1 notes for lesson 2.
- The Java snippet compiles as a fragment, does what the prose says, and the
  line numbers in the prose match the rendered listing and the `data-say`
  read-out ("line 6, return send of message, default retries"); `<=` is
  spoken "is at most" and `++` "is incremented".
- Misconceptions: three per lesson, the first §C's, each refuted from the
  chapter with the lab's illustration said to illustrate ("on the lesson's
  illustration"); the §F.4 aside is in the `note` of the lesson named as its
  home and nowhere else in the course.
- Quiz distractors in the other nine items each differ from the answer by an
  integer, a cell or a section's claim, and the `why` names each one.
- `not_covered` and `how_to` are honest about the course having almost no
  code and about the figures being other people's averages.

## Summary of must-fix items

1. Upstream Prerequisites' exercise must make the reader place defects by
   phase before pricing them (M1), with the §C entry, quiz item 1 and the
   `standard` changed together.
2. Lesson 1's "two shortest chapters in the book" is false; reword (M2).
3. The read-out spells the article "a" as the letter in the course's and two
   lessons' key lines; reword the lines now and report the dialect bug (M3).
