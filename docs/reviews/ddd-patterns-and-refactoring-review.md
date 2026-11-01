# Review (accuracy and teaching): Domain-Driven Design, Course 6 — Analysis Patterns, Design Patterns and Refactoring

Course `ddd-patterns-and-refactoring` (`content/domain_driven_design/c6_patterns_and_refactoring/`),
four lessons, against PLAN §C Course 6 and the operator's copy, PDF pp. 181–204 read in full
with `page.py`. Reviewed 2026-11-01; I wrote only this file and did not read `site/`.

## Gates

- **Preview:** `python3 scripts/preview_subject.py domain_driven_design --course ddd-patterns-and-refactoring --out …/scratchpad/rev/ddd-patterns-and-refactoring`:
  5 pages, labcheck 4 executed, 4 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 4 quotations, all OK**: 6.1 p. 181 (20 words), 6.2 p. 190 (27), 6.3
  p. 200 (24), 6.4 p. 203 (17); one a lesson, page in each dict comment.
- **`overlap.py … 8`:** 10 runs, all titles ("Chapter 12, Relating Design Patterns to the
  Model", ×6) or the four counted quotations. Clean. At 5–7 words, see MF-3 and SF-6.
- **Browser (Playwright, chromium, `file://`).** All four lessons at 1280 and 375 px: no
  sideways scroll, no page or console errors. Every preset's tiles match the prose, the
  worked lines and my own count (ledger balances and nets, derived entries and −0.01,
  decisions 7 → 2 with depth 1 at line 4 / 2 at line 16, module touches 8 → 5).
- **Exercises typed in** all agree with their quiz `why`s: bar evening (b3 −0.50, total
  −0.50), matinee (1.89, 0.91, 53.00), `SEAT_SCHEMES` 6 and my three policies 2, timetable
  6 / 1 of 3 then 3 / 3 of 3.
- **Domains** are the lessons' own (theatre, bike-share, festival, clinic, school); no book
  domain, code or data.

## MUST-FIX

**MF-1. A figure in the prose the lab does not support: "four of the six decisions".**
`part_a.py:985–986` says "Four of the six decisions ask which plan the rider is on", and the
worked title at `:1087` says "Seven decisions, four of them on the plan". By the lab's own
breakdown the six decisions are the `if` and `&&` on line 3, the `if`s on lines 6 and 9, and
the `if` and `||` on line 16. Five of them test `r.plan()`; only the `&&` (minutes ≤ 45)
does not. The lab confirms it: 7 falls to 2, so five decisions leave. Replace with:
`:985` "Five of the six decisions ask which plan the rider is on, the `&&` on line 3 asking
about the ride instead, and a new plan would add a test to both methods." `:1087` "Seven
decisions, five of them on the plan". `:1101` "Lines 3, 6 and 9 test the plan once each and
line 16 twice; the second half of line 3 asks about the ride."

**MF-2. The lab's single pass presented as what distinguishes the firing modes.**
`part_a.py:726–730`, quiz `why` `:833–836`, mistake `:876–878`. The lesson says the lab's
"one pass started from one place" is unlike eager firing, which "would cascade", and that
"Under eager firing they would, and the fee would be larger". In the book (p. 187, Fowler's
modes as Evans summarises them) the modes differ in *when* rules fire and *who starts them*,
not in whether derived entries count. Under posting-rule-based firing the rule looks up all
entries made to its input accounts since it last fired, so trust-fee run after restore would
find the 20.63 and 4.82 too. That derived entries never fire is the kit's rule
(kit-report, ledger/post), not a property of any mode. Replace `:726–730` with: "It does
not fire on the 20.63 and 4.82 the first rule derived, because the lab never lets a derived
entry fire a rule. That is the lab's choice, not Fowler's: in a real system, whether a rule
sees entries other rules derived depends on the order and the point that starts it, which is
why each set of rules needs, as Evans puts it after Fowler, one clear point of initiation
and of responsibility for finding its input entries." Quiz `why` last sentence: "In a system
where trust-fee ran after restore and looked up every entry since its last run, they would,
and the fee would be larger." Mistake 3 last sentence: "The lesson's second preset shows
how much turns on whether a rule sees what other rules derived."

**MF-3. Close paraphrase of two boxed pattern statements (Strategy p. 192, Composite p. 195).**
- Strategy: the key line `:913` "factor the varying part of a process" is a 7-word run of
  the boxed statement, and `:965–968` rebuilds it clause by clause (factor the varying part
  of the process into a strategy object of the model / separate the rule from the behaviour
  it governs / each version one way of doing the process). Replace the key line with
  "pull the varying rule out of a process", and `:965–968` with "His remedy: make the
  variable part an object of the model in its own right, kept apart from the process it
  steers, with one such object for each way the process can go, built as the design
  pattern builds it."
- Composite: concept `:936–937`, body `:1005–1009`, quiz option `:1150–1151` ("deal with the
  abstract type and", a 6-word run) and `why` `:1153–1154` each follow the boxed statement
  sentence by sentence, and `:1005–1006` carries the 7-word run "is there a true whole-part
  hierarchy". Replace `:1005–1009` with "Evans's first question is whether the idea fits:
  are the parts really the same kind of thing as the whole? If so, give whole and part one
  shared type, let a whole answer a question from its parts and a single part from itself,
  so that a client asks the same question at any size." Concept: "…behind one shared type:
  a whole answers from its parts, a single part from itself, and a client asks either the
  same way." Quiz option D: "They use one shared type and need not know which they hold";
  `why` first sentence: "A whole answers from its parts and a single part from itself, so a
  client asks the same question at any level."

**MF-4. "the essential trait" (Why Not Flyweight?, p. 199).** Quiz `why` `:1143–1144` says
Evans "calls" applying to model and implementation "the essential trait of a domain
pattern". He calls it *an* essential trait, and the 6-word run is his. Replace with "Composite
applies to the model and to the implementation, which for Evans is what makes a pattern a
domain pattern."

## SHOULD-FIX

1. **Code blocks over §F's twenty lines.** `ACCOUNT_JAVA` (`:63–83`) is 21 lines,
   `POSTING_RULE_JAVA` (`:127–148`) 22. Drop the comment line, or fold the constructor.
2. **`POSTING_RULE_JAVA` contradicts its own comment.** It says "Posting-rule-based firing",
   but `fire(List<Entry> newInputEntries)` is handed its entries; in that mode the rule finds
   them itself (p. 187). Use `void fire()` with `for (Entry e : input.entriesSince(lastFired))`
   (which also fixes SF-1 if the constructor is folded).
3. **Posting Rule concept `:623`, "watches an input account".** "Watches" reads as eager
   firing, which the next concept says is only one mode. "An object tied to an input
   account: an entry there is its input…"
4. **Exploration teams (p. 202).** `:1268` "brainstorm for under two hours": the book gives
   half an hour to an hour and a half; say so. Concept `:1228–1229` makes the domain expert
   unconditional; the book brings one in "if there are subtleties", as the body (`:1267`)
   correctly says. Add "where there are subtleties".
5. **Chapter 13's opening list near-verbatim** (`:1248–1250`, p. 201): "keep looking at things
   a different way" is a 7-word run, and the three items follow the book's wording almost
   word for word without being counted. Paraphrase the middle item ("keep changing the angle
   you see it from") or count the list as quotation (13 words; the lesson total stays under 60).
6. **Near-runs outside boxed statements.** `:972` "the fastest route or the cheapest" (p. 192;
   use "the quickest or the least costly route"); `:370` "a model that is already expressive
   and" (p. 181; "a model that already communicates and can be built").
7. **The timetable exercise is not in the lab's input form** (`:285–295`, colon lists and
   two elements on one line), unlike 6.1's and 6.2's, and the after design's `Period,
   periods` element is only described. Give both designs as `element, module` and `change,
   element` records, as the body asks the reader to "enter both designs into the lab".

## NOTE

- Every other claim about what Evans or Fowler argues checks against pp. 181–204, including
  both Chapter 11 stories, Strategy's consequences, Composite's "only when it is needed",
  Flyweight, and every Chapter 13 section. Fowler and the Gang of Four are credited in place.
- `:1296–1298` names Eldredge and Gould; Evans does not. Right (1972), but say it is not his.
- The counts serve the arguments (conservation, rounding drift, "conditionals in every
  computation", p. 193). 6.4's modules count is the loosest fit, but the body says the count
  cannot price the refactoring, which is Timing's point. Every lesson closes on the material
  clause's gap and keeps Evans's limits.
- No wrong quiz answer holds up against the book or the lab once MF-2's `why` is fixed.
  Cross-referenced lesson titles all exist.

**Verdict:** accurate, with sound labs; fix MF-1 to MF-4 and it is ready to ship.
