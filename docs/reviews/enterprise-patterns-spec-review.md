# Enterprise Application Patterns — accuracy and pedagogy review of the specification

Reviewed: `docs/enterprise-patterns/PLAN.md` (with `earef.py`, `presets.py`,
`ccrun.js`), before any authoring. Two reviews in one pass: **A**, accuracy
against the book (every §C entry, §B names and chapter numbers, every §S.2
figure, the misconceptions, copyright); **B**, pedagogy and lab soundness
(does each count carry the chapter's argument, do the eakit models model the
situation honestly, do the presets follow from the stated rules, do quiz
distractors hold, do the snippets do what the lesson says, course order, the
cckit reuse).

Method. The book was read only through `eabook.py`/`eapage.py` at the pages
cited; quotations were re-checked with `ea_quotes.py` (44/44 OK) and each one's
first words were re-located to find its exact page. Pages below are PDF pages
of the operator's copy; book text is cited by a few words at most. Every eakit
preset and exercise in §C was re-derived by hand from §D.1's rules (perf,
finds, calls, boundary, payload, instances, identity, graph, tree, uow
commit/order, inherit, lock reads/timeline, session, money); `earef.py` and
`earef.py --cc` were then run and agree with §C everywhere except where noted
(MF-12). `SPLIT_CENTS`, `SERVERS_NEEDED` and the `Integer == int` comparison in
`TWO_CONTROLS` were compiled and run with javac 21. No file other than this
one was changed.

Labels: **CERTAIN** = read in the book at the page given; **COMPUTED** =
recomputed here; **JUDGEMENT** = the reviewer's reading.

## Verdict

The scaffolding is sound: chapter numbers, chapter and pattern titles, Part 2
page ranges, the 44 quotations, and 22 of the 23 §S.2 figures are right, and
the arithmetic of every eakit preset follows from its stated rule. The
problems are of five kinds:

1. **Copyright / own-rule breaches** (MF-1 to MF-4): three snippets follow a
   book listing or example closely (`UNIT_OF_WORK`, `SPLIT_CENTS`,
   `TAX_STUB`), and Course 5 uses the album/artist/track domain that §E.3 says
   stays in the book.
2. **Lessons that contradict the book** (MF-6 to MF-11): a Service Layer
   verdict Fowler explicitly declines to give; a Table Data Gateway "Also" the
   book refutes; a Page Controller fix that puts view choice in the model;
   Front Controller's duplication argument, which Fowler states only to
   qualify; Application Controller's "fixed flow" inverted; and the Gateway
   lesson's claim that a schema change still reaches every client.
3. **One kit model mis-models its pattern** (MF-5): pessimistic locking takes
   the lock at the edit, after the read. The book says to lock before loading
   the data, and the 6.2 presets and exercise change under that rule.
4. **Two spec errors in figures** (MF-12, MF-13).
5. A set of shoehorned or weakly argued labs, over-hardened readings, wrong
   pages and attribution slips (SHOULD-FIX, NOTE).

Counts: **13 MUST-FIX, 27 SHOULD-FIX, 14 NOTE.**

---

## MUST-FIX

### MF-1. `UNIT_OF_WORK` (4.1, §D.4) adapts the book's listing line by line — CERTAIN

The book's Unit of Work example (David Rice, PDF p. 179–180) keeps three lists.
Its register-removed method returns early if the object was new, removes it
from dirty and adds it to removed. Its register-dirty adds only if the object
is not new. Its commit inserts new, updates dirty, then deletes removed. The
snippet's `markDeleted` (`if (added.remove(e)) { return; }`, `changed.remove`,
`deleted.add`), `markChanged` (`if (!added.contains(e))`) and `commit`
(inserts, updates, deletes, in that order) follow it statement for statement.
§E.3 forbids this.
**Fix:** write a different shape. For example, one `Map<Entity, State>` with a
`transition(State, Op)` table (NEW+DELETE → remove; CLEAN+CHANGE → DIRTY;
any+DELETE → REMOVED), and a commit that iterates once and switches on state.
Or show only the client side (a script that registers changes, then
`uow.commit()`) and leave the class to prose.

### MF-2. `SPLIT_CENTS` (2.6) adapts `allocate(long[] ratios)` — CERTAIN

The book's allocator (PDF p. 436) sums the ratios in a loop, fills a results
array with amount·ratio/total while tracking what is left, then adds one cent
to each of the first `remainder` results. `SPLIT_CENTS` has the same three
loops in the same order, with `given` in place of `remainder`. The lab's rule
may stay (it is the rule, not the listing).
**Fix:** write the snippet differently. For example, compute the exact shares
as `cents*w[i]` against `sum`, sort the indices by remainder (largest first,
which is a different rule) or by position, and hand out the leftover in one
pass. Or make the lesson's code the *caller*: a test that checks
`split(5, {70, 30})` sums to 5, which is what Fowler's test listing does in
spirit but not in form. Whichever rule the snippet uses must match
`allocator`'s stated rule, or the panel must say the two differ.

### MF-3. `TAX_STUB` (7.5) is the book's Service Stub example — CERTAIN

The book's Service Stub example (Rice, PDF pp. 445–447) is a sales-tax
service: an interface, a flat-rate stub, and a Plugin (PDF p. 443) that reads
an implementation class name from properties and calls `Class.forName(...)`.
`TAX_STUB` is an interface `TaxPolicy`, a `FlatTaxStub` returning a flat rate,
and a factory doing `config.getProperty(...)` then `Class.forName(...)`. That
is the book's example domain and structure, which §E.3 keeps out.
**Fix:** change the domain: a postcode or address-validation service, an
exchange-rate feed, or a credit check. Show the Plugin in a form that is not the book's
property-to-`Class.forName` listing, such as a `switch` on an environment name
that is read once. Rename the presets' nodes (`taxpolicy`,
`realtax`, `stubtax`) to match.

### MF-4. Course 5 uses the book's album/artist/track domain — CERTAIN

§0 deviations and §E.3 both say the album and artist pages stay in the book.
Yet:

- `ALBUM_MODEL` (5.1) is `Album` and `AlbumView`, and 5.1's presets are
  `album`, `albumpage` and `albumreport`;
- 5.5's presets are `albumpage`, `artistpage`, `trackpage`, `album` and
  `artist`;
- `TRACK_ROW` (5.4) renders a track's title and minutes as a table row. That
  is the book's Transform View example, an album's track list rendered as
  rows of title and time (PDF p. 329).

The Chapter 14 examples are all Artist/Album controllers and helpers (PDF
pp. 304–323).
**Fix:** move Course 5 to one domain of its own (the concert/booking domain
5.2 already uses would do): `Concert`/`ConcertView`; `concertpage`,
`venuepage`, `tourpage`; a `SetlistRow` or `TicketRow` in 5.4. The only album
reference left should be 5.2's quotation (classical and jazz albums), which
is a quotation.

### MF-5. `lock/timeline` pessimistic rule takes the lock at the edit; the book says lock before loading (§D.1, 6.2, 6.5) — CERTAIN / COMPUTED

Pessimistic Offline Lock (Rice, PDF p. 384) says the lock should be acquired
before loading the data, since otherwise there is no guarantee of the latest
version. §D.1 has "an edit takes a lock … a read takes no lock". This has two
consequences.

- **(a) The 6.2 story is not the pattern's.** Martin reads at 0 and David at
  1. Under the book's rule, Martin, who will edit, locks at 0, and David is
  refused at minute 1 having lost 0 minutes. Under §D.1, David locks at 5 and
  Martin is refused at 6, losing 6 minutes. The 6.2 exercise changes the same
  way: ann locks at 0, bo is refused at 2 with 0 minutes redone, where §C
  says bo is refused at 4 and redoes 2.
- **(b) The model allows the lost update the pattern exists to prevent, and
  does not count it.** Take A read x; B edit x; B commit; A edit x (the lock
  is free); A commit. This succeeds under "pessimistic" with
  `olLostUpdates` 0.

**Fix:** under `pessimistic`, a session's first read of a group it edits
later in the timeline takes the lock at that read. A read of a group it never
edits takes none, which is still the exclusive write lock. State the rule in
the panel with the book's reason. Then recompute:

- 6.2 `pessimistic` → `olCommitted` "1: martin", `olRefused` "1: david",
  `olRedo` 0, `olPeakLocks` 1;
- 6.2 exercise → ann commits, bo refused at 2, 0 minutes.

Reword 6.2's misconception refutation and Worked line to match: pessimistic
loses *no* work here. 6.5's presets have no reads and are unchanged.

### MF-6. 2.4 misconception gives a verdict the book declines to give — CERTAIN

The misconception is "The Service Layer is where the business logic goes",
refuted with "Fowler keeps domain logic in the domain … turns the Domain
Model beneath it anaemic". But:

- Chapter 2 (PDF p. 44) gives the thin layer as Fowler's *preference* and
  then concedes it: many good designers always use a Service Layer with a
  fair bit of logic, readers may ignore him on this, and Randy Stafford has
  had success with a rich Service Layer. He also presents "most business logic
  in Transaction Scripts inside the Service Layer" as one end of a legitimate
  range.
- The pattern itself is Stafford's (PDF p. 133). His two variants (p. 134)
  include the operation script, a thicker service that implements
  *application* logic.
- "Anaemic" is not in the book.

**Fix:** make the misconception one the chapter does refute: "domain logic
and application logic are the same thing, so it does not matter which layer
holds a rule" (Stafford, p. 134, separates them). State Fowler's thin-layer
preference *as a preference*, with his concession. Attribute the pattern, and
the quotation (p. 136), to Stafford.

### MF-7. 3.1 lab and misconception say a gateway leaves a schema change reaching every client — JUDGEMENT, against CERTAIN text

The misconception's refutation reads `dgAffected` "5: admin, cart, checkout,
pricegateway, report" as "it still reaches all four classes … every class is
still reached and still retested". That is an artefact of `deps/ripple`'s
transitive closure, which treats any change as changing the dependency's
interface. The pattern's point, and this lesson's own quotation (PDF p. 46,
"needs to know nothing about SQL"), is that a column rename stops at the
gateway when its interface is unchanged. As written, the lesson teaches the
reader to disbelieve the claim it quotes.
**Fix:** read `dgDirect` (4 → 1) as the lesson's count, and say in the panel
that `dgAffected` is an upper bound: what *would* be reached if the gateway's
interface had to change. Replace the misconception with one the count
refutes, for example "a gateway is one more class, so a schema change costs
more", which goes from 4 edits to 1.

### MF-8. 3.1 "Also" is contradicted by the book — CERTAIN

The "Also" says "Table Data Gateway returns domain objects" is a
misconception, because "it returns record sets, or plain data". But Table
Data Gateway (PDF p. 142) says that with a Domain Model the gateway can return
the appropriate domain object. Its p. 141 discussion offers maps, DTOs and
Record Sets as alternatives.
**Fix:** drop it. Or use "a Table Data Gateway is one object per row", which
is Row Data Gateway, and which the page refutes. Correct the Read line
("returning record sets") to "returning a Record Set, a map, a DTO or, with a
Domain Model, domain objects".

### MF-9. 5.2 moves view selection into the model — CERTAIN

`CONCERT_PAGE_SPLIT` calls `Concert.viewFor(c)`, which returns a JSP name. The
Standard asks the reader to "write the model method that picks the view". This
contradicts several things:

- 5.1's own rule (the model never refers to the view);
- Chapter 1's (PDF p. 36, the domain never depends on the presentation);
- Page Controller (PDF pp. 302–303), where deciding the view is the
  controller's job, with *helper objects* for the logic;
- Front Controller (p. 313), where the commands choose the view.

5.1's "Also" ("the controller … picks the view") contradicts 5.2 directly.
**Fix:** move the decisions to a presentation-side helper (`ConcertPageHelper
.viewFor(c)`, which is Fowler's helper). The model keeps its domain predicates
(`isSoldOut`, `isSeated`, `hasSeatMap`). Restate the Standard as "write the
helper method that picks the view". Do the same in the 5.2 exercise answer:
the seat range and the paid-and-not-refundable rule belong to `Booking`, and
the forward choice belongs to the helper.

### MF-10. 5.3 teaches as Fowler's reason a view he states only to qualify — CERTAIN

Front Controller, When to Use It (PDF p. 314), calls removing code duplicated
across Page Controllers a "commonly stated advantage". It then answers it:
much of it can be done with a superclass Page Controller. Fowler's own reasons
are different:

- one handler to configure;
- dynamic commands added without changes;
- a new command per request, so no thread-safety worries;
- decorators, as Intercepting Filter.

The lab (`pages-repeat` → `front-handler`) and the "Also" ("the repetition is
the reason to change, as the lab shows") present the qualified view as the
conclusion. The Read's "worth it when the common behaviour is real" is not
the book's test either.
**Fix:** add a third preset, `page-superclass`: the two page controllers
extending a `SecurePage` Layer Supertype that runs the three lines, giving
`coDupBlocks` 0. Say in the body that duplication alone does not choose
between the patterns, and give Fowler's four reasons. Reword the "Also" to
"Front Controller is the only way to remove what page controllers repeat".

### MF-11. 5.6 inverts when Application Controller is not worth having — CERTAIN

The Read ("when the flow is simple and fixed, it is not worth having") and the
misconception ("with a fixed flow it adds a layer for nothing") have it
backwards. Application Controller, When to Use It (PDF p. 346), says there is
little value when screens can be visited in pretty much any order. Its
strength comes from *definite rules* about the order of pages. A fixed flow
is exactly where it helps.
**Fix:** "when any screen can be visited in any order, it adds little; its
value is definite rules about page order and views that depend on object
state". The `FLOW_REPEAT` lab already shows definite rules, so it can stay.

### MF-12. 4.3 `every-order-used` instance is not what §C says — COMPUTED

§C describes the preset as "(all used → '6 statements, 20 rows', …)". But
`presets.py` line 1209 also changes `o2` from 0 children to 1. On
`orders-and-lines` with only the `used` flags changed, the figures are:

| tile | presets.py | §C's described instance |
| --- | --- | --- |
| `ldLazy` | 6 statements, 20 rows | 6 statements, 19 rows |
| `ldBatched` | 4 statements, 20 rows | 4 statements, 19 rows |
| `ldTwoQueries` | 2 statements, 20 rows | 2 statements, 19 rows |
| `ldJoin` | 1 statement, 15 rows | 1 statement, 15 rows |

An author following §C pins the wrong figures, or a test fails.
**Fix:** either write the instance in §C in full (`o1, 3, yes; o2, 1, yes; o3,
5, yes; o4, 2, yes; o5, 4, yes`), or keep `o2, 0` and pin the 19-row figures.
Keeping `o2, 0` is better: lazy and two queries then return the same 19 rows,
and the reader sees that the only difference left is 6 statements against 2,
which is the misconception's refutation.

### MF-13. 3.4 misconception's "one more class" is wrong by the lab's own word — COMPUTED

The misconception says "On the lesson's illustration a domain change reaches
one more class than before". The lab's "reaches" is `dgAffected`. Before (the
`active-record` design, `account` changed) the change reaches 2: report,
screen. With the mapper it reaches 4: main, mapper, report, screen. That is
two more. Only `dgDirect` (2 → 3) is one more. No preset runs the "before"
case, so the reader cannot check the claim.
**Fix:** add preset `active-record-domain-change` (`account` changed →
`dgDirect` "2: report, screen", `dgAffected` "2: report, screen"). Then
write "one more direct dependent (the mapper), and two more classes reached
(the mapper and the main that wires it)".

---

## SHOULD-FIX

### Accuracy

- **SF-1. Co-authors' patterns are attributed to Fowler** (§F; 2.4, 2.6, 4.1,
  4.8, 6.4, 6.5, 7.5) — CERTAIN. The by-lines are:
  - Service Layer: Stafford (p. 133);
  - Optimistic Offline Lock (p. 374), Pessimistic Offline Lock (p. 382),
    Implicit Lock (p. 400) and Service Stub (p. 445): Rice;
  - Coarse-Grained Lock (p. 391) and Plugin (p. 441): Rice and Foemmel;
  - Repository (p. 294): Hieatt and Mee;
  - the Unit of Work example (p. 178): Rice;
  - the Money example (p. 433) and the allocation conundrum (p. 432):
    Foemmel;
  - Chapter 5 (p. 72): Fowler and Rice.

  §C says "Fowler's lock manager" (6.5) and "Fowler's Plugin" (7.5), and
  quotes Stafford and Rice as Fowler. **Fix:** add to §F: "where the book
  names a pattern's author, the lesson names them" (the pattern by Rice, in
  Fowler's book). Correct the phrases above.
- **SF-2. F3 is on p. 28, not p. 27** (§S.2, 1.2 Read) — CERTAIN. Response
  time, responsiveness, latency and throughput are on p. 27. Load, load
  sensitivity and the A/B illustration are on p. 28.
- **SF-3. 7.5's quotation is on PDF p. 446, not 445** — CERTAIN.
  `ea_quotes.py` passes it only because it checks the next page too. The same
  check could mask other one-page errors, so re-run the page location with
  `eabook.py` for every Quote.
- **SF-4. Table 5.1 is on p. 81, not p. 82** (6.3) — CERTAIN.
- **SF-5. 2.1 misconception cites the wrong passage** — CERTAIN. Making a
  Choice (pp. 42–43) does not "recommend it wherever the logic is simple". It
  says Fowler sees no reason for Transaction Script on .NET, that the better
  the team the more he leans to Domain Model, and that if you start with
  Transaction Script you should not hesitate to refactor toward Domain Model.
  Cite Transaction Script's own When to Use It (p. 113, the lesson's
  quotation), and keep the Making a Choice qualifications.
- **SF-6. 2.6 Money's floating-point reason is a gloss** — CERTAIN. The book
  says the amount is an integral *or fixed decimal* type (p. 431), and that
  floating point should be avoided because it brings the rounding problems
  Money exists to avoid. The p. 433 example shows a float sum. "Binary
  floating point cannot hold most decimal fractions" is a true fact, but it
  is not the book's stated reason. **Fix:** in the Read, write "integral or
  fixed decimal". In the "Also", give the book's reason and mark the binary
  explanation as the lesson's.
- **SF-7. 2.7 misconception overreaches** — CERTAIN. "Not failures, which
  should still throw" is contradicted by the book's own IEEE NaN example
  (p. 439), which is a divide-by-zero failure returned as a Special Case.
  **Fix:** refute with what the page says: a Special Case is for an expected
  case with a sensible default, and callers can still test for it explicitly
  (p. 440).
- **SF-8. 2.7 code uses the book's example vocabulary** — CERTAIN.
  "occupant" and `MissingCustomer` are the book's (p. 438: the utility's
  unknown customer called "occupant", Special Cases for a missing and an
  unknown customer). **Fix:** rename them (for example `GuestCustomer`,
  "friend").
- **SF-9. 4.2 Read and "Also" over-harden Identity Map's scope** — CERTAIN.
  The page (p. 185) allows read-only Identity Maps held in a process context.
  **Fix:** add "except for read-only data, which Fowler allows to be shared
  across sessions". As written, a careful reader can defend the distractor.
- **SF-10. 4.4 omits Fowler's first advice on ordering** — CERTAIN. Mapping
  Relationships (p. 55) says that if the database can defer referential
  integrity checks to the end of the transaction, there is no reason not to
  use it. A topological sort is offered for when it cannot. **Fix:** state
  the deferral first in the Read and the body, and say the `uw/order` lab
  models a database that checks each statement.
- **SF-11. 3.5's quotation does not state the section's argument** (§E.3) —
  CERTAIN. It is a parenthetical aside in Double Mapping (p. 58) about
  copy-and-paste schemas. **Fix:** choose a sentence carrying the argument.
  The advice that model-first applies only within short iterations, from the
  same page, is the one *F12* uses.
- **SF-12. 6.3 misconception is not refuted by the chapter** — JUDGEMENT.
  "Serializable is the default" is a claim about databases that the chapter
  does not address. The refutation answers a different claim. **Fix:**
  "Serializable prevents every read error, so use it always" is refuted at
  strength by the quotation's next sentence on liveness (p. 81).
- **SF-13. 4.1 misconception's wording is false as written** — JUDGEMENT.
  "Until then nothing has touched the database" is wrong, because the loads
  read it. **Fix:** say "nothing has been written".
- **SF-14. Module rule broken for 3.6** (§B) — CERTAIN. The rule makes a
  lesson's module the Part 2 chapter of its patterns. 3.6 reads Registry
  (Chapter 18) but is filed under `Chapter 3 · Mapping to Relational
  Databases`. Either change the module or state the exception.
- **SF-15. Two snippets track book lines closely** — CERTAIN.
  - `LAZY_LINES` (`if (lines == null) { lines = mapper.findForOrder(id); }`)
    is the book's lazy-initialization example with the names swapped (p. 189,
    `findForSupplier`).
  - `OPTIMISTIC_SAVE` throws `ConcurrencyException("invoice " + inv.id())`
    on a zero row count, which mirrors the book's mapper (pp. 379–380).

  Both are short idioms and low risk. Rename the method and exception, and
  change the message form, so that neither reads as a transcription.

### Pedagogy and lab soundness

- **SF-16. 3.5's lab does not illustrate Building the Mapping** (§D.5) —
  JUDGEMENT. The section is about the three schema situations and double
  mapping. A dupes count of two finders is a mapping-code count, and it
  repeats 4.8's lab. **Fix:** aim the dupes lab at double mapping, which the
  page says leads to a lot of duplication (p. 58). Use two mappers for two
  sources (a table and a message), repeating the field-to-object code; the
  cure is a logical-store step (two-step mapping).
- **SF-17. 4.8's lab sells Query Object where the book advises against it** —
  CERTAIN. Query Object, When to Use It (p. 290), says most projects with a
  hand-built data source layer do not use it, and that it is really needed
  only with Domain Model, Data Mapper and Metadata Mapping. **Fix:** frame
  the dupes lab as *Metadata Mapping* (Chapter 3's "simple and repetitive"
  mapping, which the quotation supports), and state Query Object's
  conditions in prose.
- **SF-18. 3.3's `code/class` count is shoehorned** — JUDGEMENT.
  `coPublicRoutines` (1 vs 0) records an arbitrary visibility choice, and
  `coRoutines` (3 vs 2) records "one more method". The kit cannot tell
  database access from domain logic, as §C admits. **Fix:** pin `coRoutines`
  only, and say the reader does the classifying. Or count with
  `deps/ripple` what a schema change reaches when domain code calls
  `canWithdraw` on an Active Record against on a domain object fed by a Row
  Data Gateway.
- **SF-19. 2.4's `dgConnected` falls mostly because the denominator grows** —
  COMPUTED. Pairs go from 10 to 15 when a module is added. Direct coupling
  stays at 60% with a third client while the service case drops to 28.6%,
  partly because there are 7 modules. **Fix:** pin `dgEdges` (6 → 5; 9 → 6)
  and drop `dgConnected` from the pins. Better still, use `code/dupes` on
  application logic (reserve, confirm, mail) copied into two clients, which
  is Stafford's argument (p. 136).
- **SF-20. 2.3's `ldRatio` is a meaningless average** — JUDGEMENT. "1,955 rows
  per module" averages four unrelated tables, and the exercise answer
  ("1,585.50 rows each") invites a reader to treat it as a property of Table
  Module. **Fix:** drop `ldRatio`, or replace it with the largest table's
  rows (what one module object's Record Set holds).
- **SF-21. 4.3's row count makes the join look strictly best** — COMPUTED.
  The join returns 15 rows on both presets, fewer than every other strategy,
  because the lab counts rows and not width. The "Also" (a join repeats the
  parent's columns) is therefore not visible in the lab. Reading in Data's
  three-or-four limit is about joins per query, which does not apply to one
  join. **Fix:** add a cells tile (rows × columns, with the parent and child
  column counts as inputs), or drop the "Also" and its p. 52 citation.
- **SF-22. 4.5's per-level and per-node counts use different rules** —
  COMPUTED. Per-node counts the queries that find a leaf has no children
  (1 + 8 = 9). Per-level stops at the depth (4) without the query that finds
  level 5 empty. **Fix:** set `ldPerLevel` to depth + 1 (5; exercise 6), or
  set `ldPerNode` to 1 + non-leaf nodes (4; exercise 5) and state the
  assumption (children counts are known). Either way, state it in the panel.
- **SF-23. 2.2's snippets are not equivalent refactors** — JUDGEMENT.
  - `PRICE_DELEGATED` drops `ALCOHOL` and the default kind, so part of the
    5 → 2 fall in decision points is lost behaviour.
  - The `SHIPPING_BY_METHOD` answer moves `p.isStaff()` into `Collect`. In
    the original, a staff parcel by any method other than POST or COURIER
    pays 0, including the default, so the answer changes behaviour.

  **Fix:** add `Alcohol` (merge `unitCents` into a field to stay within 20
  lines). Put the staff rule where it applies to every non-POST, non-COURIER
  class (the default class too), or rewrite the exercise so that the rule
  belongs to one method.
- **SF-24. 7.3 misconception is undercut by its own exercise** — JUDGEMENT.
  The misconception "Send only what the screen needs" is refuted with "the
  DTO … still arrives in a quarter of the time". But the exercise's
  screen-shaped DTO, which sends only what the screen needs in one call, is
  the fastest design (10.04 ms). The misconception confuses fewer bytes with
  fewer calls. **Fix:** "Fetch each value only when the screen asks for it",
  which is refuted by 5 calls at 102.07 ms against 26.07 ms. Keep the
  exercise as the limit of the book's advice.
- **SF-25. 1.2 misconception is true at a stated load** — JUDGEMENT. "The
  faster system is the one with the lower response time" holds at any one
  load, so a careful reader can defend the distractor. **Fix:** "The system
  with the lower response time at one load is faster at every load".
- **SF-26. 7.4's prose mislabels the boundaries** — COMPUTED.
  `service-split-off` puts the boundary *above* the Service Layer (page →
  service, 2 calls). `domain-split-off` puts it *under* the Service Layer
  (service → domain, 40 calls), not "through the middle of the domain".
  **Fix:** correct the body sentence. Also say that one `remoteUs` prices the
  browser hop and the database hop alike. The exercise's conclusion ("the
  three calls from the phone … the case for a Remote Facade") ignores that
  its four database calls cost 200,000 µs of the 350,050, because the phone's
  50 ms is applied to the database too. Give the database hop its own cost
  (two remote rates), or change the exercise's question.
- **SF-27. 4.1 banner names the wrong lesson, and §C line counts disagree
  with §D.4** — CERTAIN.
  - The `uow/commit` banner says "the order view is the next lesson's", but
    it is 4.4, three lessons on.
  - §C's line counts are wrong for six snippets: `SHARED_SUBROUTINE` (§C 15,
    actual 16), `ORDER_ROW` (19/18), `LAZY_LINES` (17/18), `TRACK_HELPER`
    (10/11), `SECOND_STAGE` (19/20) and `TAX_STUB` (17/18).

---

## NOTE

- **N-1.** Example page starts are off by one (source comments only):
  - Unit of Work examples start p. 178, not 179;
  - Lazy Load examples start p. 189, not 190;
  - Chapter 3's Inheritance heading is p. 55, not 56.
- **N-2.** 1.1's "Also" cites Kinds of Enterprise Application. The "not all
  enterprise applications are large" point is in Enterprise Applications,
  p. 24.
- **N-3.** 4.4's misconception drops the hedge on the same page as "a rare
  stand" (p. 201): small or very stable systems may get away with meaningful
  keys. Add it.
- **N-4.** 3.2: the batched (`IN`-list) strategy is the lab's, not the book's.
  Say so. The Read's "a join is usually better than several queries"
  overstates p. 52, which says joins can really speed things up.
- **N-5.** 6.6: the book calls *F19* a completely unrealistic thought
  experiment with perfectly balanced requests (p. 88). The panel should say
  so, beside its "average" caveat.
- **N-6.** 2.6: the `rest-to-last` preset shows a 0 difference and hides the
  fault the book names for it, pennies piling onto the last share (p. 432).
  Add a preset that shows it (for example 100 in `1 1 1 1 1 1 1` by
  `last`).
- **N-7.** 3.6's lab covers one sentence of Some Miscellaneous Points.
  Database Connections and Registry, the lesson's title, get no count. That
  is acceptable, but `how_to` should say it.
- **N-8.** 3.6's misconception refutation ("the work is the same") is the
  model's assumption. Real batching can also save parse and commit work, so
  mark it as the lab's.
- **N-9.** 1.3's Standard says measurements are at one and two servers. The
  exercise gives measurements at 1 and 3. Align them. `SERVERS_NEEDED`
  loops forever when `extraTps ≤ 0`, so a guard or a comment is wanted.
- **N-10.** Course order:
  - 1.5 reads Chapter 8's Other Layering Schemes, whose mappings name
    Application Controller, Data Mapper, Service Layer and DTO before the
    reader has met any of them. Consider moving it to 7.4.
  - 7.5 comes after the book's summary (7.4). Consider swapping them so that
    the course ends on Putting It All Together.
- **N-11.** `MAP_TWICE`, `HAND_QUERIES` and `QUERY_OBJECT` use `SELECT *`.
  That is consistent with p. 63, which objects to positional column access,
  not to `*` with named columns. Since 3.6 teaches the point, one sentence
  saying why these are fine would prevent a confused reader.
- **N-12.** §S.1 lacks Kirtland (the Microsoft DNA scheme, p. 107, read in
  1.5) and Knight and Dai (the source of Application Controller's ideas,
  p. 346).
- **N-13.** `TWO_CONTROLS`' `versions.get(file) == versionWhenRead` unboxes,
  which is correct (checked), but it throws a NullPointerException for an
  unknown file. A null check (or `getOrDefault`, which is Java 8) would
  stop a reader copying the bug.
- **N-14.** cckit reuse, case by case:
  - Sound: 1.4, 1.5, 2.1, 2.7, 3.4, 5.1, 5.4, 5.5, 5.6 and 7.5. Each count is
    the one the chapter makes.
  - Acceptable: 1.1 (decision points stand for "illogical" rules, as the
    body says) and 2.5 (but pinning `coRoutines` teaches nothing; pin
    `coPublicFields` only).
  - Shoehorned or misleading: 2.4 (SF-19), 3.1 (MF-7), 3.3 (SF-18), 3.5
    (SF-16), 4.8 (SF-17), 5.2 (MF-9) and 5.3 (MF-10).

  With those fixed, the 20/44 share (§H.4 q. 3) is defensible.

---

## Checked and right (no finding)

- Chapter numbers and titles; every Part 2 pattern name and its page range
  against the contents (PDF pp. 1–4). Every Part 2 pattern is read in some
  lesson.
- *F1*, *F2* and *F4* to *F23* at the pages given and at the stated strength.
- The 44 quotations: wording OK, and pages right except 7.5's (SF-3).
- Recomputed by hand and matching §C:
  - 1.2 (B overtakes A at 11⅔ users);
  - 1.3 (crossovers at 5 and at 4; needs 3/1, 8/9, 4/4);
  - 2.3; 2.6 (all rules); 3.2; 3.6; 4.1 (all three scripts); 4.2; 4.4;
  - 4.6 and 4.7 (all tiles, including both exercises); 6.1 and 6.3 (all
    `olLevel` cases follow the p. 80 retelling); 6.4; 6.5;
  - 6.6; 6.7; 7.1; 7.2 (40/41); 7.3 (both presets and both exercise
    variants); 7.4 (all four).
- Every cckit preset and exercise in §C matches `earef.py --cc`.
- `SPLIT_CENTS` gives [4, 1] and [17, 17, 17, 17, 16, 16], and
  `SERVERS_NEEDED` gives 4, 4, 8 and 9 on the lesson's figures (run).
