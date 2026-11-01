# Review (accuracy and teaching): Domain-Driven Design, Course 9 — Large-Scale Structure and Strategy

Course: `ddd-large-scale-structure` (`content/domain_driven_design/c9_large_scale_structure/`,
`__init__.py`, `part_a.py`, `part_b.py`), six lessons. Built to
`docs/domain-driven-design/PLAN.md` §C Course 9 and `AUTHORING.md`. Reviewed 2026-11-01
against the private extraction (PDF pages of the operator's copy). I read pp. 272–314
behind every claim with `page.py`; I did not read the book whole or `site/`.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-large-scale-structure --out …/scratchpad/rev/ddd-large-scale-structure`
  rendered 7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 7 quotations, all OK.** 9.1 p. 275 (18 words), 9.2 p. 285 (14), 9.3 p. 288
  (13, Fowler's definition as Evans quotes it, attributed correctly), 9.4 p. 299 (17),
  9.5 p. 305 (15), 9.6 p. 308 (10) and p. 312 (12): 22 in that lesson. Each lesson is under
  40 for its opening quotation and under 60 in total (9.1 adds the two-word term "naive
  metaphor"). The PDF pages in the source comments are right.
- **`overlap.py <dir> 8`:** 7 runs, all of them the counted quotations above. No other run.
- **Browser (Playwright, chromium, `file://`).** All six lessons at 375 px and 1280 px:
  no sideways scroll, no page or console errors. I loaded every preset, and every tile
  matches the prose and the worked lines by my own count.
- **Exercises typed into the lab.** Each matches its quiz `why` (the gym needs `Pilates,
  booking` added to the elements, as the exercise implies; the nine-context one-way 72
  cannot be checked under `directed: no`, which the exercise admits).
- **Book examples as lab data:** none; the book's examples appear in prose summaries only.

## MUST-FIX

1. **part_a.py:840–841, Knowledge Level concepts intro: wrong credit.** "the second
   Buschmann's". The second term is *Operations level*, and that is Fowler's term. Evans's
   comparison table (PDF p. 292) gives Fowler's Knowledge/Operations Level against POSA's
   Meta/Base Level. Replace with: "Three terms carry the lesson. The first two are
   Fowler's, as Evans uses them (Buschmann's names for them are meta level and base level);
   the third is the lab's."

2. **part_a.py:939–948, Knowledge Level: the claim is credited to Evans, and the lab's own
   figures contradict it.** "That is Evans's warning in a figure: the knowledge level absorbs
   the changes its designer foresaw and makes the others harder". On the presets,
   exam-amnesty reaches 2 modules under *both* designs, so the count shows nothing made
   harder. Evans's warnings (p. 292) are also different ones: obscurity from the
   indirection, a superuser who needs a meta-level programmer's skills, data migration,
   and a design that must hold up for every future configuration. Replace from "That is
   Evans's warning…" with: "The subclass design also needed 2 modules for this change, so
   the knowledge level does not make the amnesty harder. It just does not make it easier: a
   new kind of rule is still new code, now in the knowledge level itself. Evans's warnings
   cover what the count leaves out: the superuser who must now configure amnesties
   correctly, the loans already out when the rule changes, and a design that must hold up
   for any configuration users later choose." For the same reason, change step 3
   (1007–1009, "It is the one the knowledge level makes harder") and the
   `__init__.py:71–72` outcome to "the requirement a knowledge level does not absorb". The
   gym exercise (1 → 3) can keep "harder".

3. **part_a.py:1494–1496, Bringing the Strategy Together: overstatement.** "Every structure
   in the previous chapter lived inside one context". Evans (p. 301) says only that the
   *Responsibility Layers* examples were confined to one context. Chapter 16 says System
   Metaphor can map across several contexts (p. 277) and puts multiple contexts behind a
   Pluggable Component Framework's interfaces (p. 295). Replace with: "The previous
   chapter's examples of Responsibility Layers were confined to one context, the easiest way
   to explain the idea and a common use, and such a local structure raises how much
   complexity one unified model can carry."

4. **part_b.py:283–297, quiz 6.1: the third option can be defended.** An anticorruption layer
   translates *into* the downstream model (Ch 14), so when rentals' model changes, a real
   ACL from payment-provider would usually need updating. "2 models, 1 translator, 1
   untouched" is therefore a fair answer. The `why`'s "reads the edge the wrong way round"
   is wrong; the kit report's deviations list this as a lab convention ("A downstream's own
   ACL is not counted as changing when only its own model changes"). Change the question to
   "…by the lab's rule (a translator is counted where a change arrives from upstream), how
   many…". Replace the why's last sentence with: "The lab does not count rentals' own ACL,
   because the change did not come from payment-provider. In a real system that layer
   translates into rentals' model and may well need updating, which is one of the things a
   team reading the map should ask."

5. **part_a.py:267–270, System Metaphor: close paraphrase of the boxed statement**
   (p. 277). The sentence follows the box clause by clause ("captures the … imagination",
   "lead thinking", "organise the design around", "for over-extension", and the exact run
   "be ready to drop it"). Replace with: "So the pattern is conditional. Evans would take up
   a metaphor only when one has turned up that the team finds compelling and that points
   its thinking somewhere productive. Then it shapes the design and enters the Ubiquitous
   Language, and because no analogy is exact it stays under review, to be abandoned once it
   misleads." At 470–472 (mistake 2), replace "The pattern applies … gets in the way." with:
   "The pattern is for the case where a compelling analogy has already turned up, and it
   tells the team to abandon the analogy once it misleads."

6. **part_a.py:1188–1192 and 1160–1162, Pluggable Component Framework: close paraphrase of
   the boxed statement** (p. 295). Both passages follow its two sentences in order
   ("implementations of those interfaces", "be freely substituted", "any application …
   strictly through the … interfaces", "so long as it"). Body replacement: "The pattern, in
   the lesson's words: make the Abstract Core's interfaces and their interactions the only
   contract, so that one component can be swapped for any other that honours it, and an
   application can work with any component without knowing which one it has." Concept
   replacement: "A structure in which every component is written against the Abstract
   Core's interfaces and every application reaches components only through them, so that
   one component can replace another."

## SHOULD-FIX

1. **part_a.py:62–75 against 49–54, Responsibility Layers.** The snippet's `Booking` holds
   `List<Ticket>`, but `THEATRE_DEPS_FIRST` has no `Booking, Ticket`. A reader counting
   from the code finds 11 dependencies and 3 within a layer, where the lab shows 10 and 2.
   Either add `Booking, Ticket` to both dependency lists (the figures become 11/6/3/2 and
   10/7/3/0) and update 612, 615–617, 628 and the worked lines, or add "the model lists
   only the dependencies the lesson discusses" after "like this".
2. **part_a.py:561–564: near-run with the Responsibility Layers box and its lead-in**
   (pp. 278–279): "conceptual layers … around major responsibilities", "each object,
   aggregate and module to fit inside one". Suggest: "Name a few broad responsibilities the
   domain itself shows, far wider than any object's, and refactor until every object,
   aggregate and module belongs to exactly one of them."
3. **part_a.py:220–222: near-run with the large-scale structure box** (p. 274), "its place
   in the whole". Suggest "…and let anyone say what a part is for without reading its
   details."
4. **part_a.py:1231: Minimalism slightly garbled.** Evans says to address the most serious
   concerns and leave *the rest* to case by case (p. 299). Change to "address only the most
   serious concerns and leave the rest to be settled case by case; start loose."
5. **part_b.py:153–154: Evant is a company, not a team.** Suggest: "And Evant, an
   inventory-management software company cut to four developers after the dot-com crash,
   survived because a supple design let those four scale the product for one of the world's
   largest retailers."

## NOTE

- Lesson 4's lab labels the framework scheme "published" ("a published language" in the
  status line), while the prose says "framework interface". The book allows a Published
  Language as the plug-in interface (p. 295), so the label is defensible. A one-clause gloss
  in the prose would help ("the lab calls the framework scheme *published*").
- Lesson 4's "the interface changes: all 6" (worked line) and "12 of 12" are hand
  reasoning that the lab does not print. The prose says so ("What the lab does not
  count"), so this is not a MUST-FIX.
- part_a.py:530: Relaxed Layered System could be credited to Buschmann et al. (p. 278).
- The teaching holds up. Each lab count follows one of Evans's arguments, every lesson
  closes on what the count cannot settle, and the lessons keep Evans's conditions (a
  structure is optional, a poor fit is worse than none, use a Knowledge Level sparingly,
  apply a framework late, and an architecture team is not rejected as such).

**Verdict:** accurate and well taught overall. Fix the two misattributions, the Knowledge
Level claim the lab contradicts, the arguable map quiz and the two close paraphrases of
boxed statements before release.
