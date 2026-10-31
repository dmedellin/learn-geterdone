# Review: Enterprise Application Patterns, Course 1 — Layers and Performance

Course: `enterprise-patterns-layers-and-performance`
(`content/enterprise_patterns/c1_layers_and_performance/__init__.py`, `part_a.py`),
five lessons; its block in `content/spoken/enterprise_patterns.py`; and `PATH` in
`content/enterprise_patterns/__init__.py`. Built to `docs/enterprise-patterns/PLAN.md`
§A, §C Course 1, §E, §F, §R and `docs/enterprise-patterns/AUTHORING.md`. Reviewed
2026-10-31 against the operator's private extraction, reading the pages behind every
claim about the book (Preface pp. 15–18; Introduction pp. 21–31; Chapter 1 pp. 33–38;
Chapter 18 pp. 420–423) with `eapage.py` and `eabook.py`. Nothing from the extraction
is reproduced here beyond the few-word phrases needed to identify a claim.

**Scope.** This file only. No course file, PLAN entry or kit was edited; every finding
is a recommendation with its fix.

Ranks: **MUST-FIX** — a claim about the book, a figure or the code that is wrong;
**SHOULD-FIX** — a hardening, a close paraphrase, an answer leak or a confusion a
careful reader would hit; **NOTE** — worth doing, not blocking.

## Gates

- **Preview:** `python3 scripts/preview_subject.py enterprise_patterns --course
  enterprise-patterns-layers-and-performance --out …/scratchpad/rev-c1` → 6 pages;
  labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`labcheck.js --observe`, every preset:** `due-day` 9 / "1 + if 5 + && 2 + || 1" /
  6–10 / 2 / line 12; `due-day-plain` 1 / 1 / 0–5 / 0 / line 3; `system-a-and-b`
  "a 0 ms a user; b 180 ms a user" / "a 1×; b 10×" / "a 500 ms; b 1,100 ms";
  `at-ten-users` same, pzAt "a 500 ms; b 200 ms"; `swordfish-and-camel` 20/40 a
  server, 15/10, "5 servers (both 80)", 3/1, 80/80; `need-120` … 8/9, 155/130;
  `rising-twice` 1 / 6 / "lines 3–5 and lines 11–13"; `rising-once` 0 / 0 / none;
  `mapper-in-domain` "1: mapper" / "3: mapper, order, screen"; `separated` "1: mapper"
  / "2: main, mapper". Every value matches the body prose, the worked lines, §C and my
  own count.
- **Playwright** (chromium, file URLs), 375 px and 1280 px: no page-level horizontal
  scroll at 375 (code blocks and tables scroll inside their boxes), no console or page
  errors. Every preset loaded through the select; every exercise typed in as the body
  asks:
  - 1.1 `LATE_FEE` → 8, "1 + if 4 + && 2 + || 1", 6–10, depth 1, line 5;
  - 1.2 north/south at 20 → "north 50 ms a user; south 5 ms a user", "north 7/2 ≈
    3.5×; south 10/9 ≈ 1.1×", "north 1,150 ms; south 975 ms"; at 5 → 400 / 900; A/B at
    25 → "outside its measured loads" with the no-extrapolation banner;
  - 1.3 heron/stork, need 60, at 6 → 30/45 a server, "heron 12; stork 6", "4 servers
    (heron 66, stork 63)", "heron 4; stork 4", "heron 90; stork 75";
  - 1.4 `OVERDUE_TWICE` → 1 / 4 / "lines 3–4 and lines 10–11";
  - 1.5 before → "1: pdfwriter", "3: invoice, pdfwriter, report"; after (`pdfwriter,
    invoice` + `main, pdfwriter`) → "1: pdfwriter", "2: main, pdfwriter".
  Each agrees with its quiz `why` and with §C's **Answer**.
- **Snippets:** all nine constants are byte-identical to `presets.py`'s `S[...]`; all
  ≤ 20 lines, ≤ 72 characters. `SERVERS_NEEDED` and `SEPARATED_FINDER` compiled with
  `javac --release 8`; `serversNeeded` returns 3, 1, 8, 9, 4, 4 on the six cases the
  course states. Every line number the prose cites is right (`DUE_DAY` 4, 7, 10, 11,
  12, 15; `SERVERS_NEEDED` guard 3–5, loop 8–11; `RISING_TWICE` 3–5, 6, 11–13, 14;
  `OVERDUE_TWICE` 3–4, 5, 10–11, 12; `SEPARATED_FINDER` 2–4, 7–11, 14–19). No snippet
  uses a book listing's domain or shape (the book has no Separated Interface listing;
  Layer Supertype's ID example is named, not coded).
- **`ea_quotes.py`: 6 quotations, all OK.** 1.1 p. 24 (18) + "half baked" p. 29 (2) =
  20; 1.2 p. 27 (16); 1.3 p. 28 (12); 1.4 p. 36 (12); 1.5 p. 421 (15). All within 40
  and 60; each opening one is §C's **Quote** with its page in the dict comment. No
  other quotation marks enclose book text.
- **`# F` comments:** F1, F2 (1.1), F3 (1.2), F4, F5 (1.3), F6, F7 (1.4), each checked
  on its page. No book figure in the course is without one.
- **Shape:** course and lesson keys identical to Code Complete's; 3 concepts, 4 steps,
  3 mistakes per lesson; bodies 13, 12, 12, 15, 13 blocks; quizzes 4, 4, 4, 4, 3; every
  key line ≤ 46 characters. Each `steps[-1]` is §C's **Own**. Each last `p` names the
  next lesson (1.5 names the next course and its first lesson, Transaction Script).
- **`speechcheck.py`:** the Subject is not in its report yet (not wired). I generated
  the read-out of every key line, worked line and prose backtick run with
  `speech.say_code` and the SPOKEN block; findings 13–14.
- **PATH** (`content/enterprise_patterns/__init__.py`): tagline, description,
  sequence_intro, footer_lead and material are character-identical to §A; why_order
  (4) and prerequisites (5) match §A, with only the internal "(§D.5)" dropped, as it
  should be; the six key lines are 38–45 characters; the field list and order are
  exactly `content/code_complete/__init__.py`'s (slug, title, level, level_note,
  speech, tagline, description, key, sequence_intro, why_order, prerequisites,
  material, footer_lead, courses), with `"speech": "code"` and the same
  filter-and-number loop. See finding 20.

## MUST-FIX

1. **1.4 Layering — Chapter 1 does not have five sections.** `read_intro`: "Read
   Chapter 1, Layering, in your own copy first, all five of its sections." Evidence:
   the contents (PDF p. 1) and pp. 33–38 give an untitled opening and three sections,
   The Evolution of Layers in Enterprise Applications, The Three Principal Layers, and
   Choosing Where to Run Your Layers. Fix: "Read Chapter 1, Layering, in your own copy
   first: its opening and its three sections."

2. **1.1 Enterprise Applications, quiz item 2 `why` — attributes to the section what it
   does not say.** "…and that many use a Web presentation rather than a rich client."
   Evidence: Enterprise Applications (pp. 23–24) says nothing about Web against rich
   client; the only presentation remarks in the Introduction are in Kinds of Enterprise
   Application (p. 25: a Web presentation for the retailer and the expense tracker, a
   rich client often wanted for the leasing system). Fix: drop the clause, and say of
   the fourth option instead: "A rich client is not one of the marks; Kinds of
   Enterprise Application gives a Web presentation to two of its three examples."

3. **1.1 Enterprise Applications, body `p` on Patterns — "Every pattern in Part 2 has
   the same parts".** Evidence: The Structure of the Patterns closes (p. 31) by saying
   that not every section appears in every pattern, and that those without a good
   example or motivation leave it out. Fix: "Each pattern in Part 2 is written to the
   same form — a name, an intent and a sketch, a motivating problem, How It Works, When
   to Use It, further reading and examples — though a pattern leaves out a section it
   has nothing good to put in."

## SHOULD-FIX

4. **1.2 Thinking About Performance, `mistakes[0]` — the crossover at 12 is the lab's,
   not the illustration's.** "Fowler's illustration says otherwise: B answers sooner at
   10 users and degrades so much that A answers sooner from about 12 users up." The
   book (p. 28) gives only 10 and 20 users; "about 12" is the lab's straight line,
   which the body itself calls the lab's assumption. Fix: "Fowler's illustration says
   otherwise: B answers sooner at 10 users and ten times slower at 20, where A is
   faster. On the lab's straight line the two meet a little below 12 users." (The
   last sentence of the mistake is already correctly marked "read on the lab's line".)

5. **1.3 Capacity and Scalability — capacity is "maximum effective", not "most
   effective".** The concept, the body and the key line say "the most effective
   throughput"; the book (p. 28) says maximum effective throughput or load. "Most
   effective" reads as the throughput that is most effective, which is a different
   idea. Fix: concept and body "the maximum effective throughput or load"; key line
   "capacity: the maximum effective throughput" (43 characters).

6. **1.4 Layering — an example threshold made a definition.** Body: "extreme
   performance requirements, which the book puts at more than 100 transactions a
   second". The book (p. 38, *F7*) gives 100 tps as an example ("such as"), not as
   where extreme begins (§F.2: keep his hedges). Fix: "…extreme performance
   requirements, for which the book's example is more than 100 transactions a
   second." The quiz `why` ("more than 100 transactions a second in the book") is
   acceptable but would read better as "for example more than 100…".

7. **1.5 Layer Supertype and Separated Interface, `mistakes[0]` — "usually has one
   implementation … not from substitution".** The book does not say a Separated
   Interface usually has one implementation, and its When to Use It (p. 423) gives
   multiple independent implementations as the second of the two reasons to have a
   separate interface in an application, which quiz item 2 correctly teaches. The
   mistake as written contradicts the lesson's own quiz. Fix: "Separated Interface can
   have a single implementation and still earn its place: Fowler's case for it is the
   direction of the dependency between packages (When to Use It begins with breaking a
   dependency); several implementations are a second reason, not a requirement."

8. **1.5 quiz item 1 — the stem gives away the exercise's design answer.** The
   exercise asks the reader to "name the interface and its package, rewrite the
   dependency it reverses, add the class that wires the two"; the stem then supplies
   all three ("an interface InvoiceRenderer in the invoice package, implemented by
   pdfwriter and wired by main"), outside the `why`. Fix: stem "In the exercise,
   `fontlib` changes. What does it reach before the interface, and after the
   Separated Interface the exercise asks for?" and move the design (InvoiceRenderer in
   the invoice package; `pdfwriter, invoice`; `main, pdfwriter`) into the `why`, which
   already explains the reversed edge.

9. **1.1 — four agreements, eight decision points, with no bridge.** The body calls
   `DUE_DAY` "a due date with four agreements in it", then says "The eight points
   between the two listings are the agreements", and `mistakes[0]` repeats "eight of
   the due date's nine". A careful reader counts four agreements and wonders where the
   other four points come from, and the exercise asks exactly this mapping ("name the
   agreement each `if` encodes"). Fix: one sentence after the breakdown: "The four
   agreements cost eight points between them: government one (`if`), the northern
   customers two (`if`, `&&`), the late retail or online invoice three (two `if`s and
   the `||`), and the cap two (`if`, `&&`)."

10. **1.1 — the Preface paragraph tracks the book sentence by sentence.** The second
    body `p` follows the Preface's first three paragraphs (p. 15) in order and nearly
    clause for clause: the spring of 1999, Chicago, ThoughtWorks, the back-end leasing
    system, the four things that happen after signing in the book's order, the
    variations that win deals, each victory adding complexity, then the database, the
    UI, remote applications, third-party packages and J2EE nobody had experience of.
    Each phrase is reworded, but the sequence is the book's (§E.3: no close
    paraphrase). Fix: compress to two sentences in the lesson's own order, e.g. "The
    Preface starts from a leasing system Fowler worked on with ThoughtWorks in 1999,
    whose rules grew one won deal at a time and which had to be stored, given screens,
    opened to other programs and built on a platform nobody yet knew. The book is
    written for that situation, in two parts: …"

11. **1.3 — Fowler's hedge on hardware cost hardened.** Body: "still holds that
    hardware usually costs less than the programmers it would take…". The book (p. 28)
    says often, twice. Fix: "often costs less".

12. **1.2 → 1.3 — "never extend the line" then extend it.** 1.2's step 3 says "never
    extend the line past the last measurement", and its lab refuses to; 1.3's lab and
    worked example project past the last measurement as the core of the lesson. 1.3's
    body and `mistakes[2]` justify the projection (the book's own supposition), but
    never connect it to the rule the reader just learned. Fix: one clause in 1.3's lab
    `p`: "Unlike the last lesson's lab, which reads only between measurements, this one
    carries on past them, because Fowler's illustration states the gain for every
    further server."

13. **Spoken — the dependency records lose their pairs.** In 1.5, `report, invoice;
    invoice, pdfwriter; pdfwriter, fontlib` is read "report, invoice, invoice,
    pdfwriter, pdfwriter, fontlib": a listener cannot tell which name depends on which,
    and this is the exercise's input. Course 3's block already reads such records as
    "a uses b". Fix: add to this course's SPOKEN block `"report, invoice; invoice,
    pdfwriter; pdfwriter, fontlib": "report uses invoice, invoice uses pdf writer, pdf
    writer uses fontlib"`, and the same for `invoice, pdfwriter` ("invoice uses pdf
    writer"), `pdfwriter, invoice`, `main, pdfwriter`, and `dependent, dependency`
    ("dependent, then what it depends on").

## NOTE

14. **Spoken, smaller items.** `system, users, ms` and `system, servers, tps` are read
    with "ms" and "tps" as letters (the course's own block spells them out elsewhere);
    the worked lines `swordfish at n: 20 + 15 * (n - 1)`, `camel at n: …` and `equal
    when 5 * (n - 1) is 20: n is 5` are read "times, open bracket, n minus 1, close
    bracket" where the block's style is "the quantity n minus 1"; `jdbc` is read as a
    word here and "J D B C" in Course 3's block. The two measurement records read
    acceptably, since each triple starts with its system's name.

15. **1.4 Layering — "in his experience, the better choice in practice".** The book
    (p. 35) says the presentation reading the data store directly is less pure but
    "tends to" work better. The body, the quiz `why` and `mistakes[2]` ("he finds")
    are near enough; "tends to work better in practice" keeps the hedge exactly.

16. **1.4 — Alan Knight's comment paraphrased close to his words.** "a slide into
    disorder or … a sensible shortcut only a purist would mind" follows the quoted
    comment (p. 36) closely, ending on four of its words. Either quote a short phrase
    of it (it is a quotation the book makes, so it counts against the lesson's 60; the
    lesson is at 12) or loosen it: "wondered whether it was the start of a decline or a
    reasonable shortcut, and Fowler's answer is that it is both."

17. **1.4 — `RISING_ONCE` and the exercise answer put the rule in different shapes.**
    The preset's domain rule is `isRising(Product p)`, a method that takes the
    product; the exercise answer is `isOverdue()` on `Invoice`. Fowler's wording (p.
    36) is a domain method saying whether a product's sales are improving, which
    either fits, and the quiz options do not trap the reader. Consider a sentence in
    the `rising-once` `p` that `isRising` would sit on `Product` in a Domain Model, and
    is written as a function here to keep both presentations visible in one listing.

18. **1.5 — "the interface in its own package".** The `separated` `p` says `order` uses
    `finder`, "the interface in its own package"; "its" can be read as `finder`'s own
    (a third package), while the snippet puts `OrderFinder` in the domain package with
    `Order`. Fix: "the interface in the domain package".

19. **1.2 — "Load sensitivity is one of several words Fowler says are used
    loosely".** The book (p. 27) says many performance terms are used inconsistently
    and singles out scalability; it does not name load sensitivity. "Fowler says many
    of these words are used loosely; scalability is the worst" is exact.

20. **PATH.** Complete and correct against §A and Code Complete's shape. The short
    title "Enterprise Application Patterns" is not a PATH field (Code Complete's lives
    in `scripts/catalog.py`, and §H.3 leaves the catalog entry to wiring), so its
    absence here is right. The path page itself was not rendered by `--course`, so the
    prerequisites' backtick runs (`if`, `List`, `Connection`, `SELECT`) were checked
    only in source; check them on the path page at wiring, since Code Complete's
    prerequisites carry none.

21. **Kit strings (not the author's to change).** 1.2's banner says "The response
    times are the lesson's figures" while the preset is the book's illustration (the
    source line says so correctly). The ratio tile prints "north 7/2 ≈ 3.5×" on the
    exercise, a form the body never shows (its presets print whole ratios); one
    clause in 1.2's lab `p` ("a ratio that is not whole prints as a fraction and its
    decimal") would cover it. At 375 px the perf tables' captions are clipped at the
    right edge ("…by system and server c"), though the table scrolls.

22. **Minor hardenings, 1.1.** Kinds of Enterprise Application: the retailer "must
    above all scale" (the book asks for efficient and scalable); the opening `p`'s
    "rules nobody can simplify" (the book: rules you cannot change without political
    effort). Neither misleads; both read closer to the book with "must scale" and
    "rules nobody can derive".

## Counts

MUST-FIX 3 · SHOULD-FIX 10 · NOTE 9.
