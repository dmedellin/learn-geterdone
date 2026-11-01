# Review (accuracy and teaching): Domain-Driven Design, Course 1 — Putting the Domain Model to Work

Course `ddd-putting-the-model-to-work` (`c1_model_to_work/`), five lessons, plus `PATH`.
Reviewed 2026-11-01 against the operator's copy, pp. 2–35, with `book.py`/`page.py`. Only
this file was written.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-putting-the-model-to-work --out …/scratchpad/rev/ddd-putting-the-model-to-work`:
  6 pages, labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 8 quotations, all OK.** 1.1 p. 7 (19 words); 1.2 p. 8 (23); 1.3 p. 13 (8)
  + p. 14 (14) = 22; 1.4 p. 20 (9) + p. 21 (12) = 21; 1.5 p. 27 (20) + p. 35 (9) = 29. All
  openings ≤ 40, all lessons ≤ 60; PDF pages in the comments are right.
- **`overlap.py c1_model_to_work 8`:** 9 runs: the eight counted quotations and the
  subsection title "Documents Should Work for a Living and Stay Current" (p. 21). Clean.
  On a copy of `PATH`'s file: 1 run, the chapter title "The Life Cycle of a Domain Object". Clean.
- **Browser (Playwright, chromium, `file://`).** Every lesson at 1280 and 375 px: no sideways
  scroll (scrollWidth = clientWidth), no page or console errors. Every preset's tiles match
  the prose, the worked lines and my own count (20/2; 3 of 4, 2 of 4, 1 of 4; 17/2; 6/0 with
  the two gaps; 5 vs 9 and 6 vs 9). Exercises typed in: 7 / 2nd clause `load <= 195` /
  6 / 7 / 2 and 3 — each matches its quiz `why`, except the label in MUST-FIX 1.
- **PATH:** same keys as Enterprise Patterns'; 9 courses, 53 lessons, as tagline and
  description say; material clause is §A's verbatim. No findings.

## MUST-FIX

1. **part_a.py:327–332 and quiz 1 (408–419), lab prints a different audience.** The exercise
   names the audiences "curators, volunteers, code", but the lab's Audiences box still holds
   `curators growers developers`. Typed in, the tile reads `1: packet (growers: withdrawal,
   packet)`; the quiz's right answer is "the volunteers' packet". Replace 330–332 with:
   "…find the name one audience uses for two concepts. Then set the lab's Audiences to
   `curators volunteers code` and type the records in to check your count."

2. **part_a.py:1165–1168, overstated.** "it should be archived as history rather than kept
   current by willpower, since a document that plays no part is not worth the upkeep, and
   left in use it misleads." Evans (p. 22) says a document left behind *could* safely be
   archived, *could* cause confusion if left active, and that upkeep by willpower wastes
   effort *if it plays no important role*.
   Replace with: "it could be archived as history: left in use it may confuse, and if it
   plays no important part, keeping it current by willpower is wasted effort."

3. **part_a.py:1181–1183, the example misdescribed.** "which matches the classes only
   loosely and teaches more than they do." Evans (pp. 23–24) says the route picture does not
   match the class diagram in detail but brings out key points, and that the two *together*
   are easier to understand than either alone. Replace with: "…which does not match the
   classes in detail, and which, read beside the class diagram, makes both easier to follow."

4. **part_a.py:1574–1578 (worked `after`), the example misdescribed.** "the scripts that
   inferred buses from file names: the code is organised by when things run". The scripts
   inferred buses by sorting the net list and matching *net* names against a naming
   convention (pp. 30–31); "linked by anticipated paths of execution" is Evans's general
   remark on procedural code (p. 29), not on the scripts. Replace with: "That is the shape
   Evans finds in the scripts that inferred a bus from a sort of net names: the concept the
   engineers think in is in none of the code, only implied by where things happen to sit."

5. **part_a.py:1376 (`one_line`), overstated.** "mapped so literally that a change to
   either is a change to both". The pattern (p. 27) says a change to the code *may be* a
   change to the model. Replace with: "…mapped so literally that changing the code can
   change the model, and modelled by people who code."

6. **Copyright, close paraphrase of the Model-Driven Design boxed statement (p. 27).**
   part_a.py:1442–1446 ("Design a part of the system to reflect the domain model so
   literally that the mapping is obvious; revisit the model so that it can be implemented
   naturally…; and demand one model that serves both") and 1403–1405 (concept) follow the
   statement clause by clause (4–6-word near-runs). E.g. 1442–1446: "The pattern binds the two. Some part of the code is written to be the
   model, class for concept, so that anyone can see which is which; when the model resists
   that, the model is reworked as well as the code, and deepened as it goes; and one model
   has to carry both jobs and the team's language too." Concept 1403–1405: "…one model
   serving both analysis and design: part of the code is the model, readably, and the model
   is reshaped until it can be."

7. **Copyright, close paraphrase of the Hands-On Modelers boxed statement (p. 35).**
   part_a.py:1473–1474 and 1647–1649 ("anyone shaping/who shapes the model should/must …
   touch/spend time in the code, and anyone changing the code should/must learn to express
   the model …"). Replace 1473–1474 with: "From this the pattern follows: whoever helps
   shape the model also works in the code, and whoever works in the code learns to make it
   say what the model says." Replace 1647–1649 with: "…it says that modelling and coding
   cannot be handed to different people: the modeller works in the code, and the
   programmer makes the code carry the model."

8. **Copyright, close paraphrase of the Ubiquitous Language boxed statement (p. 14).**
   Quiz 2 option and `why` (1010–1011, 1015–1016: "rename the classes, methods and modules
   to match / so that the code follows the new model"), body 866–872 ("make the model the
   backbone of the team's language … renames the classes and methods to match") and key
   line 818. Suggested: option "Treat it as a change to the model, and change the code's
   names along with the talk"; `why` "The pattern's statement asks the team to carry a new
   word into the code's names at once and to treat a change in the language as a change to
   the model…"; body 866: "The pattern's answer is to build the team's language on the
   model…"; key line "build the language on the model".

## SHOULD-FIX

1. **part_a.py:396–400.** "the kind of collision Evans says the first meetings spend
   their time ironing out." On p. 3 the collisions ironed out were in the *experts'*
   terminology, during the diagram sessions, not the first meetings. Suggested: "…is the
   kind of collision Evans and the engineers ironed out as they sketched together."
2. **part_a.py:872–874.** "The boxed statement ends with" — the statement continues past
   that sentence (domain experts should object…). Say "The boxed statement includes".
3. **part_a.py:622–624.** "it gives each one as a single false condition" is confusing: the
   guard is one compound condition, *true* when it refuses. Suggested: "…but each refusal
   is one compound condition coming out true, with nothing to say which part did it".
4. **Unquoted 5–7-word near-runs, Chapter 2 (not boxed statements, but tighter than the rest
   of the course).** Quiz 3 `why` 1315–1316 ("could safely be archived as history",
   "left active it could create confusion", both 6-word runs of p. 22) and its option c;
   quiz 4 `why` 1327–1330 ("the assertions of a test are rigorous", "the story told by
   names"); quiz 2 `why` 1303 ("pretty good at relationships and fair at interactions").
   Quote one (1.4 has 39 words spare) or reword.
5. **part_a.py:730 (1.2 quiz 2, distractor c)** "It broke the layering, and it duplicated the
   rule": its first half is arguable from p. 9 (Evans says Layered Architecture would move
   the rule). The `why` covers it, but a cleaner distractor is "It was too slow, and it
   hard-coded the clinic's name".

## NOTE

1. Lesson 1.2's clinic rule (bookings allowed to 195 of 180 minutes because some patients
   never arrive) is the overbooking rule's shape in a new domain. The domain is the lesson's
   own, so it is within PLAN §C; the parallel is deliberate and well signposted.
2. part_a.py:527: "making each one a class of data" goes a little past "goes beyond 'find
   the nouns'" (p. 8); harmless, the "not a data schema" idea is ingredient 3's.
3. part_a.py:1117–1120: the concept says "In the lab, a stale term", but the lab has no
   stale tile; the reader derives it from the table. Consider "In this lesson".
4. part_a.py:1509: "add the records to the lab's changes" — appending or replacing both give
   `student_loans 2` / `3`, so it works; "replace" would make the totals match too.
5. Fairness is good throughout (the feature-only iterative project, XP's position, the
   analysis model's motive, specialised roles), and every `note` closes on what the count
   cannot decide; 1.5's lab is nearer Chapter 5's Modules than to literal mapping, but the
   prose ties it to the pattern adequately.

**Verdict:** accurate and well made. eight one-sentence MUST-FIXes (a lab label, four
overstatements, three boxed-statement paraphrases).
