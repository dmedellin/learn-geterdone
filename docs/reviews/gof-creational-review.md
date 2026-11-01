# Review (accuracy and teaching): Design Patterns, Course 3 — Creational Patterns

Course: `gof-creational` (`content/design_patterns/c3_creational/`), six lessons.
Reviewed 2026-11-01 against the private extraction (PDF page = printed + 20) with
`book.py`/`page.py`. I read the pages behind every claim, including the Factory Method
and Abstract Factory Sample Code and the Discussion (pp. 155–156). I did not read the
file whole or `site/`, and I wrote only this file.

## Gates

- **Preview:** `preview_subject.py design_patterns --course gof-creational --out …/scratchpad/rev/gof-creational`:
  7 pages, 6 labs executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 8 quotations, all OK.** 3.1 p. 101 (7 words); 3.2 p. 117 (20); 3.3
  p. 127 (15); 3.4 p. 137 (19) + p. 141 (11) = 30; 3.5 p. 147 (16); 3.6 p. 155 (16) +
  p. 156 (23) = 39. Every opening quotation ≤ 40, every lesson ≤ 60.
- **`overlap.py … 8`:** only the book's title, the authors' names and the eight counted
  quotations. Clean.
- **Browser (Playwright, chromium, `file://`).** Every preset of every lesson at 1280 px;
  every tile matches the prose and the worked lines, and every exercise typed in agrees
  with its quiz `why` (15, +3/3 edits; 7 and 7, +2/+1; 10, +2/0; 4 see/3 surprised, then
  1/0; 128 and 52; 15/20/11). No errors; no sideways scroll at 375 px.

## MUST-FIX

**MF-1. Lesson 6 presents the kit's Factory Method convention as the book's comparison**
(`part_b.py:134–140`, `:210–212`, `:249–256`, `:293–297`). The prose says that with two
or more kinds per family "the counts move", the exercise's `why` concludes "Abstract
Factory is no longer as large as Factory Method: its factories make matched sets", and
mistake 1 says "the counts part". The 20 against 15 comes only from the kit's deviation
(kit-report: one abstract creator *per kind*, 2(K + F·K)). The
book's own Factory Method with several kinds is one creator with a factory method per
part and one subclass per variant (Sample Code, pp. 134–135; introduction, p. 105). That design counts 1 + F + K + F·K, the same as Abstract Factory, which
the book says outright: Abstract Factory "is often implemented with factory methods"
(Factory Method, Related Patterns, p. 136; Abstract Factory, Implementation 2, p. 110).
The Discussion never compares class counts across kinds. Its argument is subclassing
against composition, the cascade, and Factory Method needing only "a new operation"
(pp. 155–156). Distractor 2 of quiz 1 (15/15/11) is what the book's design gives. Replace:

- `:134–140` → "Two things are worth noticing about the comparison. It is made for one
  framework, with one kind of product per tool, and the authors say plainly that the
  best choice turns on many factors. Their reason Abstract Factory gains little is its
  factory hierarchy, as large as the tool subclasses it replaces. With two kinds per family
  the lab's Factory Method count grows faster, but only because the lab gives each kind a
  creator hierarchy; the book's own Factory Method sample, one factory method per part,
  has exactly Abstract Factory's count. What separates the two in the authors' argument is
  where the choice is made, in a subclass of the creator or in an object passed to it."
- `:211–212` → "With one kind per family, Abstract Factory costs as much as Factory Method.
  With several, a factory per family and a creator with one factory method per kind
  still count the same; the lab's Factory Method, with a creator per kind, counts more."
- `:252–256`, after "and edits none." → "A creator per type overriding two factory
  methods, the shape of the book's own sample, would count 15, like Abstract Factory; the
  20 is the lab's convention of a creator per kind, not a difference the authors argue."
- `:296–297` → "…both count 10 classes. Give each type two kinds and the lab's counts part,
  15 against 20, only because its Factory Method gives every kind a creator hierarchy;
  a creator with one factory method per kind, the book's own sample, counts 15 too."

**MF-2. Factory Method's disadvantage is misapplied to the lesson's own sketch**
(`part_a.py:998–1001`, `:1082–1086`). The prose says the new zone's "creator subclass is
there only to make one product", and the worked `after` says "Three of the four creating
classes exist only to make one product each". But in `ZONE_JAVA`, `LawnZone` also
overrides `valves()`, so each zone subclass would exist anyway. That is the case the
authors call harmless: subclassing "is fine when the client has to subclass the Creator
class anyway" (Consequences, p. 129). Replace `:998–1001` with "Nothing written changes, and since a pot zone also
supplies its own valves, its creator subclass is the harmless case the authors name, one
the client needed anyway; had zones differed only in schedules, it would exist just to
make one product. The preset". Worked `after` → "Each zone subclass
also supplies its valves, the harmless case; one that existed only to pick a schedule
would be the disadvantage, and a template or a prototype the way round it."

**MF-3. Prototype: "hardest" is misattributed** (`part_a.py:1183–1185`, `:1223–1225`).
The book says the hardest part is "implementing the Clone operation correctly", tricky
above all with circular references. Shallow against deep copy is one problem inside that
issue (Implementation 2, p. 141). Summary → "…which removes the factory classes and brings
what the authors call its hardest part, implementing the copy correctly, and with it the
question of what a clone shares." Body → "…then turns to what the authors call the
pattern's hardest part, implementing the clone operation correctly, and to the question
inside it of what a clone shares with its prototype, and counts…"

**MF-4. Singleton: Applicability closely paraphrased** (`part_a.py:1541–1544`). It shares
the five-word runs "there must be exactly one instance" and "instance should be
extensible by subclassing", plus "well-known access point" and "use … extended instance"
(p. 147). That is a close paraphrase of both bullets (PLAN §E). Replace with "Singleton
fits, in the authors' list, when a second instance would be an error and every client
needs one known place to find the first, and when that one object may later belong to a
subclass, chosen without touching the clients' code."

## SHOULD-FIX

**SF-1. Factory Method, `zones-new-kind`** (`part_a.py:1002–1009`). Honest that 8 added,
0 edited follows the lab's rules, but it calls the book's own shape "If instead". Add after "none edited.": "That is the lab's convention, a creator
hierarchy per kind. The book's own Factory Method sample does the other thing: one
creator with a factory method per part. The Discussion's remark that Factory Method needs
only a new operation describes that design." Keep the rest.

**SF-2. Lesson 6, the "1 prototype manager"** (`part_b.py:146–155`). The drawing editor
has no manager, and neither does the lesson's `CloningTool`: each tool holds its
prototype (pp. 137, 155). The lab also leaves the tool out as the client under Abstract
Factory and Prototype but counts it as the abstract creator under Factory Method, so the
sketch's own classes are 10, 11 and 6. Add: "The lab's 1 under Prototype is a prototype
manager, which the sketch does without; and it counts the tool only under Factory Method.
The authors' 'equally large' is the factory hierarchy, 5 against 5."

**SF-3. "Abstract Factory is no better"** (`part_b.py:116`). The book says it "doesn't
offer much of an improvement" (p. 155). Use "offers little improvement".

**SF-4. Near-paraphrases of other Applicability bullets.** AF `part_a.py:323–325`
("how its products are created … and represented", p. 108) → "when a system should be
insulated from the way its products are made and put together". Builder `:626–629`
("must allow different representations", p. 118) → "…and when one construction process
has to yield more than one representation". FM `:927–928` (p. 128) → "when a class
passes work to a helper whose subclass varies, and the choice of subclass should be made
in one place". Prototype `:1239` ("hierarchy of factories that … the hierarchy of
products", p. 138) → "when you want no factory classes shadowing the product classes
one for one".

**SF-5. `MAP_STYLE_JAVA` does not compile** (`part_a.py:46–52`). `MapView` calls an
undeclared `draw`. Within 20 lines: drop line 35's comment, make `MapView` an
`abstract class` and add `abstract void draw(Object part);`.

**SF-6. Abstract Factory mistake 2** (`part_a.py:538`). The authors attach the
prototype-based factory to "many product families" (p. 110), and "differ only slightly"
is the cost of the factory-method way. The fix: "Where many families are possible, the
authors suggest a factory given prototypes of its products…".

## NOTE

- Abstract Factory's counts agree with Consequences 2 and 4 (p. 110): a new kind edits
  1 + F, a new family edits 0. The prose stops short of a verdict ("no count tells you
  which growth a design will meet").
- Prototype's 1 + K + F·K agrees with the Discussion's "reduces the number of classes"
  (p. 156) and "Reduced subclassing" (p. 140); `part_b.py:160–163` honestly says
  value-only products would cut it further.
- Singleton draws its costs from Implementation and labels the testing aside as later
  opinion; fair. The chapter indeed never mentions threads.
- I could not argue for any other wrong quiz answer. No lab uses a book domain, and
  every lesson closes on the count-is-not-a-verdict gap.

**Verdict:** gates clean, labs exact; fix MF-1 to MF-4 before release.
