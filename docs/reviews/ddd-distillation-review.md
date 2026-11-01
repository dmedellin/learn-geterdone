# Review (accuracy and teaching): Domain-Driven Design, Course 8 — Distillation

Course `ddd-distillation` (`content/domain_driven_design/c8_distillation/`), five lessons.
Reviewed 2026-11-01 to `docs/domain-driven-design/REVIEW.md`. I read PDF pp. 247–271 and p. 301 of the
operator's copy with `page.py`, but not `site/`. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-distillation --out …/scratchpad/rev/ddd-distillation`:
  6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 6 quotations, all OK.** 8.1 p. 249 (16 words), 8.2 p. 252 (15), 8.3 p. 258 (20),
  8.4 p. 261 (13), 8.5 p. 264 (15) + p. 270 (6) = 21. Every lesson is under 40 for its opening quotation and under 60 in total.
- **`overlap.py … 8`: 7 runs.** 5 are counted quotations; 2 are the section title
  "When a Mechanism Is Part of the Core Domain" (part_a.py:1226, 1264). Nothing else.
- **Browser (chromium, `file://`):** every preset at 1280 px, every page at 375 px (no sideways
  scroll, no errors). All 11 presets' tiles match the prose and worked lines by my own count, including the
  cycles and most-coupled pairs. The core-boundary figures (7, then 5 inward) are in the table's
  `rebalancing` rows (out 5 + in 2; out 0 + in 5).
- **Exercises typed in:** the clinic gives 50 / 1/5 / 0 of 3; after the decisions 30 / 1/3 / 5; classes at 1 week
  each 1/3; the timetable changes 4 and 3; the seed bank B gives 3 / 4 / cycle (stock, viability). All agree with the quiz `why`s.
- **Lab data:** the lessons' own domains; book examples are only summarised in prose.

## MUST-FIX

1. **8.3 quiz 1 and exercise: the process rule is applied wrongly** (part_a.py:1011–1019, 1086–1099).
   The key equates "touches a flagged class" with "consult". Evans (p. 260), and the lesson at
   989–990, call for consultation only when the distillation document would have to change. A reader can argue
   that (b), one new rule, sits below the document's detail, so "(d) only" is defensible. Replacement: add to the exercise's second bullet "Changes (b) and (d)
   each alter what the distillation document says about the core's elements or their relationships; the
   others do not." Then change the `why` to "…both alter what the distillation document says, so each needs
   consulting on…"

2. **8.2: "buy or adopt" said to free weeks** (part_a.py:605–609, 692–693). Evans pairs a published
   design with an outsourced or in-house implementation (pp. 254, both options). Adopting a model
   does not take the building off the team's list. Replacement at 607: "the weeks a decision to buy or
   outsource each of them would take off the team's own list"; at 693 "a decision to buy or outsource
   could free". After 609 add: "A published model still has to be built, in house or outside, so mark such a part
   `build` or `outsource`, whatever the tile's label says."

3. **"The other strategic principle" implies there are only two** (`__init__.py`:110–112; part_a.py:1649–1650).
   Evans names three, context, distillation and large-scale structure (p. 301), and 8.1 rightly
   calls distillation the second. Replacement: "which Evans treats as the third strategic principle,
   after context and distillation" and "reads Evans's third strategic principle".

4. **8.5: Choosing Refactoring Targets misdescribed** (part_a.py:1585–1593, 1776–1777, 1797–1798).
   The rejected answers are the XP community's (p. 271), not simply "the usual" ones. Evans's third target is to purify
   *supporting* subdomains until they become generic, not "the purity of the generic subdomains". Replace
   1586 "the usual answers" with "the two answers the XP community tends to give". Replace each
   "the purity of the generic subdomains" with "purifying supporting subdomains until they are generic".

5. **8.1: close paraphrase of the Core Domain boxed statement** (part_a.py:345–349). It follows
   p. 249–250 clause by clause, keeping its opening verbatim and "by how it supports the". Replacement:
   "So the pattern, as you would apply it: decide which part of the model is the core, make it easy for
   anyone to see, and keep it as small as you can. Staff it with your best developers and hire with it in
   mind, aim its effort at deepening the model and making the design supple, and ask of every other investment what it does
   for the core."

6. **8.2: close paraphrase of the Generic Subdomains statement** (part_a.py:633–639). The 7-word
   near-run is "Once they are separated, give their development lower priority than", with the rest
   in the book's order. Replacement: "The pattern, as you would apply it: find the subdomains that support the
   project without being its point, and give each a generic model in a Module of its own that holds nothing
   peculiar to your business. Then rank their work below the core's, keep the core's developers elsewhere,
   because they would learn little of the business there, and check whether a package or a published model
   would serve before you build."

7. **8.3: close paraphrases of the Domain Vision Statement and Highlighted Core statements**
   (part_a.py:946–949, 964–966, 980–982). The near-runs are "show how the model serves and balances",
   "keep it narrow; write it early and revise it", and "as long as a developer can see effortlessly what
   is in". Replacements: 946–949 "So the pattern: about a page on the core and its worth to the business,
   leaving out whatever any similar model would also say, showing how competing interests are weighed,
   narrow in scope, drafted at the start and rewritten as understanding grows." 980–982 "…will do, provided
   a developer can tell at a glance whether an element is core." For 964–966, keep "three to seven
   pages" as a fact but recast the sentence: "a short document, a handful of pages, on the core and how its
   elements work together."

8. **8.4: close paraphrase of the Cohesive Mechanisms statement** (part_a.py:1244–1250; concept
   1205–1209). "watch especially for formalisms and well-documented families of algorithms" is a
   near-run of p. 261. Replacement: "The pattern, as you would apply it: give the coherent part of the
   computation a small framework of its own, look first for a known formalism or a textbook family of
   algorithms that already covers it, and let the model reach it only through operations named for what they
   answer. The domain classes then say what the problem is, and the framework works out the answer…"

9. **8.5: close paraphrases of the Segregated Core and Abstract Core statements and the steps**
   (part_a.py:1545–1550, 1507–1511, 1552–1559). The near-runs are "Refactor the model to separate the"
   (6 verbatim), "express most of the interaction between the significant", and "named for the concept
   that". Replacements: 1545 "So work from the other direction: pull the core's concepts away from
   everything that only helps them, vague helpers included, so that the core hangs together more tightly
   and leans less on the rest, and push what is generic or supporting into other classes and packages,
   even when that pulls apart classes that were closely tied." 1508 "The model's deepest concepts made into
   abstract types through which most of the traffic between the main parts flows, kept in a module of
   their own, with the detailed classes left in modules by subdomain." 1553–1554 "collect its classes in a
   new module whose name says what unites them".

## SHOULD-FIX

1. **8.1:370–372** "should buy software outright": Evans says to *consider* a lower-risk route such
   as buying (p. 251). Use "should look at buying software to integrate with your own". At **355**, "Most
   applications" should be "Many applications" (p. 250).
2. **8.3:959–962**: "rarely practical straight away" should be "not always possible in the short term". "a reflection
   on the model, not part of it" should be "not necessarily part of it" (p. 258). At **1151**, "often impractical"
   should be "not always practical at first".
3. **8.4:1437–1438**: "when a coherent formalism emerges" should be "when some part of the computation proves
   coherent in its own right". Evans does not require a formalism (p. 261).
4. **8.5 lab names** (1657) "before the step"/"after the step" mislabel `abstract-core`, where both
   packagings are the redesigned model (vertical, then horizontal). Use `["first packaging", "second packaging"]`.
   The prose already says which is which.
5. **8.5 exercise** (1632–1643) never says which module is the core. Add "`viability` is the core's module."
6. **8.5 concept 1513–1516**: point to the table: "the core module's row: out to others plus in from
   others".
7. **8.3 lab**: `ddsBuilt` prints "Generic parts built in house: 2: Rider, Payment" and `ddsFree` prints "5" for
   classes. Add to the panel intro: "The last two tiles count generic classes and mean nothing here."

## NOTE

- 8.4 quiz 3 `why`, "Either can be bought or built": Evans expects most mechanisms built new (p. 261).
- Seed-bank packaging A also has a cycle (ops, stock); the `why` could mention it.
- The course is fair where Evans is (off-the-shelf successes, Full Circle, segregation's costs). Every
  lesson closes on the gap, and 8.4 says plainly that its count is narrower than Evans's claim about reading.

**Verdict:** accurate and well taught; fix the 8.3 consultation quiz, the "adopt frees weeks" claim
and the five boxed-statement paraphrases before release.
