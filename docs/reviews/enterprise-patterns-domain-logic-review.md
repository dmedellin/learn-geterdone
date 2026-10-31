# Review (accuracy and teaching): Enterprise Patterns, Course 2 — Organizing Domain Logic

Course: `enterprise-patterns-domain-logic` (`content/enterprise_patterns/c2_domain_logic/`,
`__init__.py`, `part_a.py`, `part_b.py`), seven lessons. Built to
`docs/enterprise-patterns/PLAN.md` §C Course 2, §D.5, §E, §F, §R and
`docs/enterprise-patterns/AUTHORING.md`. Reviewed 2026-10-31 against the private
extraction of the operator's copy (PDF page = the copy's contents page), reading the
pages behind every sentence that says what Fowler or Stafford argues, with `eabook.py`
and `eapage.py`. I did not read the file whole and did not read `site/`.

**Scope.** I wrote only this file. Nothing in the course or in PLAN was changed. Each
finding is a recommendation, with replacement text where the fix is mechanical.

## Gates

- **Preview:** `python3 scripts/preview_subject.py enterprise_patterns --course enterprise-patterns-domain-logic --out …/scratchpad/rev2/prev`
  printed 8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`ea_quotes.py`: 7 quotations, all OK.** 2.1 p. 113 (35 words), 2.2 p. 39 (24),
  2.3 p. 42 (15), 2.4 p. 136 (31, said to be Stafford's), 2.5 p. 429 (17), 2.6 p. 432
  (18), 2.7 p. 438 (22). Each lesson quotes only its §C **Quote**, so every lesson is
  under 40 words and under 60. Each has its PDF page in the dict comment.
- **Browser (Playwright, chromium, `file://`).** All seven lessons at 375 px and 1280 px:
  no page scrolls sideways (scrollWidth equals clientWidth), no page errors, no
  console errors. I loaded every preset at 1280 px. The tiles match the body prose,
  the worked lines and §C:
  - `two-scripts` 1 / 6 / lines 3–5 and 12–14; `shared-subroutine` 0 / 0 / none.
  - `price-by-kind` 5 / 1 + if 3 + && 1 / 0–5 / 1 / line 5; `price-delegated` 2 /
    1 + if 1 / 0–5 / 2 / line 15.
  - `small-shop` 4 / 7,820 / 7,820 / 4 / line 6,000; `one-big-table` 2 / 250,400 /
    250,400 / 2 / reading 250,000.
  - `orders-twice` 1 / 10 / lines 4–8 and 13–17; `orders-served` 0 / 0 / none.
  - `mutable-range` 2, 2, 2, 2; `value-range` 2, 0, 3, 2.
  - Money: `nearest` 4, 2 / 6 / +1 / 7/2 = 3.50, 3/2 = 1.50 / 1/2 = 0.50;
    `round-down` 3, 1 / 4 / −1; `rest-to-last` 4, 1 / 5 / 0; `allocator` 4, 1 / 5 / 0;
    `three-ways` 33, 33, 33 / 99 / −1; `three-ways-allocated` 34, 33, 33 / 100 / 0 /
    2/3 ≈ 0.67; `pennies-to-last` 14 ×6, 16 / 100 / 0 / 12/7 ≈ 1.71.
  - `null-checks` 5 / 1 + if 2 + && 2 / 0–5 / 1 / line 4; `guest-customer` 1 / 1 / 0–5 /
    0 / line 3.
- **Exercises, typed or pasted into the lab as the body asks.** Each agrees with its
  quiz `why`:
  - `SHIPPING_TWICE`: 1 / 8 / lines 3–6 and 13–16.
  - `SHIPPING_BY_METHOD`: 7 / 1 + if 4 + && 1 + || 1 (band 6–10).
  - The clinic: 4 / 6,342 / 6,342 / 4 / visit 5,400.
  - `CANCEL_TWICE`: 1 / 10 / lines 3–7 and 13–17.
  - `QUANTITY_MUTABLE`: 3, 2, 3, 2.
  - Money, 100 in six: nearest 17 ×6 / 102 / +2; allocator 17, 17, 17, 17, 16, 16 /
    100 / 0; exact 50/3 ≈ 16.67.
  - `NULL_ADDRESS`: 5 / 1 + if 2 + && 1 + || 1.
- **Quiz claims tested in the lab.** 2.1 item 4 (`two-scripts` with `total` renamed
  to `price` in the second script) gives 0 / 0 / none, as the `why` says. 2.6 items 2
  and 4 (5 at 70 30 rounded up gives 4, 2, 6, +1; 10 at 1 1 1 by allocator gives
  4, 3, 3) and the `why`'s rest-to-last aside (17 ×5, 15) all match. 2.5 mistake 3
  (a private field with a public setter) counts 0 public fields, as the mistake says.
- **Answers only in the quiz.** No exercise answer appears in the page prose
  (`shippingFor`, 6,342, `cancelOrder`, the allocator's six shares and
  `UnknownAddress` are absent from the rendered text outside the quiz data). I clicked
  through every quiz on every page at 375 px. Feedback and Next work.
- **Money arithmetic, re-derived by hand.** Every figure in the body, the worked
  example, the quiz and the mistakes is right. 5 × 70/100 = 3.5 and 5 × 30/100 = 1.5.
  Nearest (half up) gives 4 + 2 = 6; down gives 3 + 1 = 4; up gives 6; rest-to-last
  gives 4 then 1. The allocator floors to 3 + 1 = 4 and gives the 1 left to the
  first share: 4, 1. 100/3 floors to 33 ×3 = 99 and gives 1 to the first: 34, 33, 33,
  a largest gap of 34 − 100/3 = 2/3. 100/7: six shares at nearest 14 = 84, and the
  last gets 16, a gap of 16 − 100/7 = 12/7. The claim that the allocator keeps every
  share within a cent holds: leftover = amount − Σ floor < n, so each share gains at
  most one cent, and floor(x) + 1 − x < 1. The lab's `allocator` is the rule of the
  book's ratio listing (floor each share, then one cent each to the first
  `remainder` shares), so "which is what the Foemmel and Fowler example does" is
  true. The panel also says the book allows other placements, which is right: the
  narrative's allocator scatters pennies "pseudo-randomly".
- **The book's listings.** `REFUND_SPLIT` does not follow the shape of the book's
  `allocate(long[] ratios)`. It has no ratio total, no floor-and-remainder loop and
  no loop handing out pennies. It is a caller that builds weights, calls `splitBy`,
  sums the parts and checks them. MF-2 holds. None of the other snippets uses the
  book's example domains: no revenue recognition, no employee, no utility occupant.
- **Snippets and cited line numbers.** I numbered every listing by hand. Every line
  cited in prose, worked lines and `why`s is right: 2.1 lines 3–5/12–14, braces 6/15,
  7/16; 2.2 lines 4, 6, 8 and depth lines 5 and 15; 2.4 lines 3/12 and 4–8/13–17,
  and the exercise's 2/12; 2.5 "line 13" (the comparison in `equals`); 2.7 lines
  3 and 7, and the exercise's 4 and 7. `PRICE_DELEGATED` gives every price
  `PRICE_BY_KIND` gives: Book −5%, Alcohol +20%, Food −10% over 10, and the default
  unchanged.
- **Spec-review fixes.**
  - MF-6 (2.4's verdict) holds. The misconception is now the
    domain-logic/application-logic confusion that Stafford's Kinds of "Business Logic"
    refutes. Fowler's thin layer is given as his preference, with his concession
    (p. 44). The pattern and the quotation are Stafford's.
  - SF-5 holds: 2.1's refutation cites When to Use It (p. 113) and gives Making a
    Choice's qualifications correctly (pp. 42–43).
  - SF-6 holds (p. 431). SF-7 holds: 2.7 cites When to Use It, the explicit test and
    the IEEE example (pp. 439–440).
  - SF-23 holds. N-6 holds (`pennies-to-last`).
- **Attributions.** Service Layer is Stafford's (p. 133). The conundrum is "Matt
  Foemmel's" (p. 432), and the example is "by Matt Foemmel and Martin Fowler" (p. 433).
  Woolf's Null Object, the pun, and Evans "in preparation" (references, p. 453) are
  all right. Chapter titles are right: 9 Domain Logic Patterns (p. 111), 18 Base
  Patterns (p. 412). So are the section names: Down to the Data Source Layer and
  Starting with the Domain Layer (Chapter 8, pp. 101–102), Making a Choice and
  Service Layer (Chapter 2, pp. 42–44), Kinds of "Business Logic" (p. 134).
- **`speechcheck.py`:** enterprise-patterns 0 unresolved.
- **Shape (§E.1).** Every lesson has 3 concepts, 4 steps, 3 mistakes and 4 quiz
  items, with 13–15 body blocks. The last `p` of each names the next lesson. There is
  one modern aside (Evans, 2.2), as §F.3 places it.

## Findings

Ranked **MUST-FIX** (a claim about the book or the code that is wrong, or a breach
of §E.3), **SHOULD-FIX**, **NOTE**.

### MUST-FIX

**M1. Table Module, and Making a Choice: Making a Choice is not "at the end of
Chapter 2".**
The first body `p` says "That is from Making a Choice, at the end of Chapter 2". In
the copy, Chapter 2's section Service Layer (p. 44) follows Making a Choice
(pp. 42–43), and Chapter 3 starts on p. 45. The course contradicts itself here:
lesson 2.4 reads "Chapter 2's section on the layer", and the course
`syllabus_intro` gives the order correctly. **Fix:** "That is from Making a Choice,
the section of Chapter 2 that follows the three patterns and comes before Service
Layer, which this lesson reads last."

**M2. Several lessons: stretches of the book, unquoted, verbatim or nearly so
(§E.3).**
§E.3 and AUTHORING forbid copying "any stretch of the text" outside a counted,
quotation-marked quotation. A 6-word shingle scan of every lesson string against
the extraction, with the quotations removed, finds these runs. The first column is
the run of identical words. Where a run is only one of the book's sentences with a
word or two swapped, the second column gives the share of the book's words kept.
Each needs rewording, or quoting within the 60-word budget with a page comment.

| lesson | where | the lesson's text | verbatim run / words kept | fix |
| --- | --- | --- | --- | --- |
| 2.3 | `concepts[1]` Record Set | "An in-memory representation of tabular data that looks exactly like the result of a SQL query but can be built and changed by other parts of the program." | first 6 words are Record Set's intent line; the rest is p. 449's sentence with "generated and manipulated … system" → "built and changed … program" (17/21) | "Tabular data held in memory in the shape a query returns, which other code can also create and edit. It usually comes with the platform, such as a data set or a row set." |
| 2.3 | `concepts[0]` Table Module | "A single object that handles the business logic for all the rows of a table or view." | Table Module's intent line (p. 126) with "instance" → "object" (15/17) | "One object that carries the business logic for a whole table or view. It has no object for each row, so to act on one row you pass the module that row's key." |
| 2.3 | body `p` 2 | "A Table Module organises domain logic with one class for each table in the database, and a single instance holds the procedures that act on that table's data." | 9-word run; p. 126's sentence | "A Table Module gives each table one class, and one instance of it carries every operation on that table's data." |
| 2.3 | body `p` 4 | "It looks exactly like the result of a database query" | 10 words, p. 449 | "It has the shape of a query's result" |
| 2.7 | `concepts[0]` Special Case | "A subclass that provides special behaviour for a particular case" | Special Case's intent line (p. 438), 10/10 words in order | "A subclass that stands in for one particular situation, such as a missing customer, …" |
| 2.2 | `concepts[0]` Domain Model | "An object model of the business area that holds both behaviour and data." | Domain Model's intent line (p. 118) with "domain" → "business area" (10/13) | "A model of the business made of objects, each holding its data and the behaviour that uses it." |
| 2.6 | body `p` 3 | "Fowler uses Money for pretty much all numeric calculation in object-oriented environments" | 11 words, p. 433 | Quote it with `# PDF p. 433` (lesson total 18 + 9 = 27), or "Fowler reaches for Money in nearly every calculation an object-oriented program does" |
| 2.6 | body `p` 4 and `note` | "precise rules for where the pennies go are hard to enforce" / "precise rules about where the pennies go are hard to enforce" | 8 words in the `note`, p. 432 | body: "…that you must remember to use it, and that it is hard to guarantee which share gets each spare penny." `note`: "Fowler says the allocator cannot easily guarantee where the spare pennies land." |
| 2.4 | body `p` 3 | "Randy Stafford has had a lot of success with a rich one" | 11 words, p. 44 | "Stafford has done well with a rich layer" |
| 2.4 | body `p` 4 | "writing those interactions separately in each interface causes a lot of duplication" | 10 words, p. 133 | "and coding them again in each interface duplicates them" |
| 2.1 | body `p` 3 | "it is a simple procedural model most developers understand; it works well with a simple data source layer" | 12 words, p. 39 | "most developers already know the procedural style; it sits easily on a simple data source layer, …" |
| 2.2 | body `p` 4 and 5, and When to Use It | "a whole layer of objects that model the business"; "in the field. A simple Domain Model looks very"; "from the order is harder to find, so people"; "simple not-null checks and a couple of sums" | 9 words each, pp. 118–120 | "adds a layer of objects that stand for the business area"; "Fowler sees two styles in practice. In the simple one the model mirrors the database design …"; "behaviour kept apart from the order is easy to miss, so it gets written a second time"; "a few checks for missing values and some totals" |

Shorter identical runs, 6–7 words ("and the best bet for most cases", "of thin facades
over a Domain Model", "most languages have no special facility for", "after a
conditional check for a particular"), are borderline. Reword them in the same pass.

**M3. Transaction Script: the exercise answer's subroutine cannot hold "those four
lines".**
Quiz item 1's `why` says: "A subroutine `long shippingFor(long cents)` holding those
four lines and returning the shipping is what both scripts would call." Line 3 of
`SHIPPING_TWICE` is `long cents = cart.totalCents();`. A routine that takes `cents`
as a parameter cannot contain the line that computes it. Both scripts also still
need `cents` after the shared lines (line 8 `cents + shipping`, line 18
`page.write(cents, shipping)`), so line 3 has to stay in each script. A reader who
writes the subroutine as the `why` describes will find it does not work. (The worked
`memberPrice` does hold all three of its lines, because `total` is its result. That
is the contrast the `why` misses.) **Fix:** "…A subroutine `long shippingFor(long
cents)` holding lines 4 to 6 and returning the shipping is what both scripts would
call. Each script keeps line 3, since both still need `cents`: one adds it to the
order, the other writes it to the page. The lab then finds no repeated run, because
one identical line is shorter than the minimum."

### SHOULD-FIX

**S1. Service Layer: "Four of the five repeated lines are application logic" can be
argued against.**
The worked `after` says this, and body `p` 7 counts "reserving the stock inside
it" as application logic. Stafford's application logic is about the application's
responsibilities: notifying administrators and integrated applications, and
transacting the response (pp. 134–136). Reserving stock is a rule about the stock,
which is domain logic by his definition, even though the service must coordinate
it. A careful reader will count 3 and 2, not 4 and 1. PLAN §C itself names only
"the transaction and the mail" as application logic around "one domain call
(`confirm`)". **Fix (worked `after`):** "Three of the five repeated lines are plainly
application logic: the transaction's begin and commit, and the mail. Two are calls
into the domain, `inventory.reserve` and `order.confirm()`, which the response must
run together inside the transaction. Stafford's operation script takes all five,
because together they are the use case's response; the rules themselves stay in
`reserve` and `confirm`." **Fix (body `p` 7):** "Read what repeats with Stafford's
distinction. The transaction and the mail are application logic. Inside them are
two domain calls, reserving the stock and `order.confirm()`, each already in one
place on its own object. What each client has had to write for itself is the
response that coordinates them, and a third kind of client would write it a third
time."

**S2. Special Case: "here they are gone" contradicts the course's own Domain Model
misconception and this lesson's worked example.**
Body `p` 6 says: "Unlike the Domain Model lesson, where the decisions moved into the
classes, here they are gone." Two other places in the course say otherwise. 2.2's
second mistake ("Thinking polymorphism removes the decisions … the question of which
kind a product is moves to wherever the object is made"), and this lesson's own
worked `after` ("The finder now makes that decision once, by returning a guest").
The decision whether there is a customer moves to the finder, as the kind decision
moved to the object's construction in 2.2. **Fix:** "Unlike the Domain Model lesson,
where each branch moved into the class it concerned, here the guarded answers all
move into one class and the decision moves to one place, the finder that returns the
guest. It leaves every caller, because the answer was the same wherever the question
was asked."

**S3. Special Case: "deepest nesting 0, first at line 3" does not fit the
explanation 2.2 gave.**
2.2 explains `price-delegated`'s depth 2 at line 15 "because the lab counts braces
from the top of the listing and that line sits inside a method inside a class". On
`guest-customer`, line 3 also sits inside a class, yet the tile says 0. The cause is
in cckit: `base = L.header ? 1 : 0`, where the header is the first depth-0
`type name(params)` statement. `GUEST_CUSTOMER` has one at line 7 (`greeting`), so
every depth is measured one lower, and the class's one-line methods read 0.
`PRICE_DELEGATED` has no depth-0 header. The figures are right, but a reader who
compares the two lessons will be puzzled. **Fix:** either drop the nesting figures
from 2.7's body `p` 6 (they are not pinned), or add: "The lab finds a routine header
here, `greeting` on line 7, so it measures depth from inside a routine, as it did on
`price-by-kind`, and the class's one-line methods above it read as 0."

**S4. Hedges hardened (§F rule 2).**
- 2.3 body `p` 9: "from scripts, do not hesitate to refactor toward a Domain Model;
  the other way is rarely worth it." The book (p. 43) says going the other way is
  *usually less worthwhile unless you can simplify your data source layer*. **Fix:**
  "the other way is usually less worth it, unless it lets you simplify the data
  source layer."
- 2.3 body `p` 2: "The difference from a Domain Model, Fowler says, is the whole
  pattern". He calls it the primary distinction (p. 126). **Fix:** "The main
  difference from a Domain Model, Fowler says, is this:".
- 2.2 body `p` 3: "which, he says, a significant minority of developers never
  make". He says they *seem to be unable* to make the shift (p. 40). **Fix:** "and
  which, he says, a significant minority of developers seem unable to make".

**S5. Domain Model: quiz item 1's `why` rules out a valid design.**
The `why` ends "The staff rule belongs in the default class, beside `COLLECT`." That
is not required. A design with `Post`, `Courier` (with its weight test), a `Collect`
class charging 0, and a default class charging 0 for staff and 999 otherwise also
keeps every price. A staff parcel sent by any method other than post or courier
reaches either `Collect` (0) or the default (0). The exercise asks the reader to
name the classes, and the `why` would mark this answer wrong. The keyed option D is
still the only correct option, and option C is wrong because its default charges a
flat 999. Only the closing sentence overreaches. **Fix:** "The staff rule belongs in
the default class. `COLLECT` can sit beside it there, or have a `Collect` class of
its own charging 0, as long as the default still charges a staff parcel nothing."

### NOTE

**N1. Service Layer, quiz item 3's `why`.** "He recommends the layer even in an
undistributed architecture when those conditions do not hold." Stafford's "even in
an undistributed architecture" sentence (p. 136) needs *both* more than one kind of
client *and* multi-resource responses. The quotation's "as soon as" uses *or*.
Suggest: "…and as soon as there is a second kind of client or a second
transactional resource, he says it pays to design the layer in, even in an
undistributed architecture."

**N2. Money, the floating-point explanation "of this lesson's own".** This is
accurate about the narrative (p. 431 gives only "rounding problems"). The book's
Foemmel–Fowler example (p. 433), however, opens by showing that ten additions of
0.10 do not equal 1.00. The body, the second mistake and quiz item 3 all say the
explanation is the lesson's. That is defensible, because the book shows the effect
and does not explain binary representation. Consider "The example that follows
shows the effect; the reason, in one sentence of this lesson's own, is…". Do not
describe the code.

**N3. Special Case, third mistake.** "Charges against an account nobody has
identified must still be kept apart" restates the book's utility "occupant" example
(pp. 438–439), which §E.3 keeps out, without crediting it. It is prose, not code, so
this is acceptable. Better: credit it ("the book's own case is a utility customer
nobody has identified, whose charges must still be kept apart") or use a different
example. The body's "an unknown customer's last bill is an unknown bill" is also
close to p. 439. Reword it, for example: "a special case's methods often hand back
further special cases, so what an unknown customer owes is itself unknown".

**N4. Table Module, and Making a Choice, body `p` 8: "apologises for it".**
Fowler says such graphs irritate him and uses the sketch anyway, because it helps
show his sense of the comparison (p. 42). That is closer to a disclaimer than an
apology. Suggest "and disowns it in advance, as one of the unquantified graphs that
irritate him in slides".

**N5. Domain Model, last `p`.** "A Domain Model gives each row of the database an
object of its own" sits badly with the lesson's own point that a rich model need not
mirror the tables. Suggest "A Domain Model gives each thing the business tracks an
object of its own."

**N6. Money, body `p` 4.** The conundrum's arithmetic follows the book's sentence
order: nearest, then down, then up (p. 432). The figures are F9 and allowed. The
list of solutions that follows is a sentence-by-sentence summary of p. 432's four
bullets. This is acceptable after M2's fixes. Reordering (state the exact shares,
then down, nearest, up) would distance it further.

**N7. Transaction Script.** The domain of the exercise scripts (`checkOut`,
`showBasket`) echoes Chapter 2's retailing illustration: checkout, shopping cart,
delivery status (p. 39). That is a narrative illustration, not a listing domain, so
§E.3 allows it. No change needed.

**N8. Special Case, voice.** Body `p` 2 ("as he notes drily, you get a stack trace
for your trouble") and body `p` 4 ("pardoning what Fowler calls the pun") are two
light remarks, and §F allows one. Both point at the author's own wit. The pun is
§F's named example, so drop "drily" from the first.
