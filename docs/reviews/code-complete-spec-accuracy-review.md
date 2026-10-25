# Code Complete, Read Along — accuracy review of the specification

Reviewed: `docs/code-complete/PLAN.md` (branch `feat/code-complete-subject`),
before any authoring. Scope: every preset instance and pinned figure in §C,
every formula and edge case in §D, every §S.2 figure (F1–F29), every section
title marked *(check)*, what the spec says McConnell argues, the Java
snippets, the copyright handling, and the counts and id lengths.

Method. The arithmetic was recomputed from scratch in exact rationals by
scripts written for this review (they are not committed). The reference
model the spec author used (`ccref.py`, `presets.py`) was not used to get any
figure. It was run once at the end to cross-check, and agrees with this
review everywhere they overlap. The snippets in §D.4 and in `presets.py` were
compiled with `javac` 21 against stub types, and the Java behaviours the
lessons claim were run. Mid-review the book itself arrived (the operator's
PDF, 952 pages). Every claim about the book below was checked against it,
and the **printed** page is given; the PDF page is printed page + 37. Quoted
book text is limited to a few words where it settles a finding. No file other
than this one was changed.

Confidence labels: **CERTAIN** = read in the book's text at the page given;
**COMPUTED** = recomputed here; **JUDGEMENT** = the reviewer's reading.

## Verdict

The spec is in good shape. Every chapter title and every section number it
lists, except four in Chapter 11, is the book's. Almost every figure in the
§S.2 register is the book's value at the place the spec believes. The
recomputed arithmetic matches §C in every pinned tile but one, and that one
is a prose miscount. The problems are of four kinds.

1. **Copyright.** Four lesson instances are adaptations of the book's own
   listings or examples, which §E.3 forbids. They are the `declared-at-top`
   live-time listing (book p. 247), the `kitchen-sink` `Program` class
   (p. 134), the `total-first`/`hidden` expense-ordering pair (p. 348) and the
   grade table's 50/65/75/90 breakpoints (p. 426).
2. **One preset would mis-teach the book.** `testing-only` prints a 72.7%
   combined rate for three test stages. The book, citing Jones, says testing
   combinations of this kind often catch **less than 60 percent** (p. 471,
   and again p. 500).
3. **Two lesson statements are wrong as written.** The Square/Rectangle
   exercise's arithmetic does not fail, and the `kitchen-sink`
   misconception's description contradicts its own tile.
4. **Two kit rules break their own presets.** The `double` "normal range"
   refusal rejects 0, and with it the `tenth-ten-times` preset. The `loop`
   view has a closed form that is wrong at `start == bound` and prints "never
   ends" for loops Java does end. There is also a set of zero-denominator
   cases §D never specifies.

All are cheap to fix, and replacement instances with recomputed figures are
given below.

---

## Must-fix

### MF-1. Four instances reproduce the book's examples (§E.3) — CERTAIN

§E.3 says "Never reproduce the book's code listings … Not retyped, not
'adapted' line by line". These four are adaptations.

**(a) `declared-at-top` / `declared-near-use` (Scope, Span and Live Time;
§D.4; the §F exemplary paragraph).** The book's own live-time listing
(§10.4, pp. 247–248) opens with the comment "initialize all variables". It
then initialises `recordIndex`, `total` and `done`, counts `recordIndex` up
in a `while (recordIndex < recordCount)` loop, and loops `while (!done)`
accumulating `total`. The spec's snippet has the same comment, the same three
roles (`index`, `total`, `done`), the same two loops, and the same
"moved-down" rewrite. Replace both listings with one written for the lesson.
This one has been checked to compile.

```java
void auditShipments(Shipment[] shipments, int limitKg) {
    int scanned = 0;
    int heaviestKg = 0;
    int overLimit = 0;
    printTitle();
    printLegend();
    for (Shipment s : shipments) {
        s.verify();
        scanned = scanned + 1;
    }
    printCount(scanned);
    for (Shipment s : shipments) {
        heaviestKg = Math.max(heaviestKg, s.weightKg());
        if (s.weightKg() > limitKg) {
            overLimit = overLimit + 1;
        }
    }
    printSummary(heaviestKg, overLimit);
}
```

`vars` = `scanned heaviestKg overLimit`. The figures, all COMPUTED:

- `declared-at-top`:
  - `scanned` is referenced on lines 2, 9 and 11: spans 6 and 1, live time 10.
  - `heaviestKg` is referenced on lines 3, 13 and 18: spans 9 and 4, live
    time 16.
  - `overLimit` is referenced on lines 4, 15 and 18: spans 10 and 2, live
    time 15.
  - Tiles: `coAvgSpan` **16/3 ≈ 5.33**, `coAvgLive` **41/3 ≈ 13.67**,
    `coLongest` **"heaviestKg: 16"**.
- `declared-near-use` moves `int scanned = 0;` to just before the first `for`
  (after `printLegend();`) and the other two to just before the second `for`
  (after `printCount(scanned);`). Line count is unchanged at 19.
  - `scanned` is referenced on lines 4, 7 and 9: spans 2 and 1, live time 6.
  - `heaviestKg` is referenced on lines 10, 13 and 18: spans 2 and 4, live
    time 9.
  - `overLimit` is referenced on lines 11, 15 and 18: spans 3 and 2, live
    time 8.
  - Tiles: `coAvgSpan` **7/3 ≈ 2.33**, `coAvgLive` **23/3 ≈ 7.67**,
    `coLongest` **"heaviestKg: 9"**.
- Worked line: "`heaviestKg` on lines 3, 13 and 18: spans 9 and 4; live time
  18 − 3 + 1 = 16."
- The Misconception's figures become "an average live time of 41/3 ≈ 13.7
  lines against 23/3 ≈ 7.7".
- The §F exemplary paragraph must be rewritten with these figures. It
  currently quotes the comment and the old line numbers.

The lesson may *cite* the book's own figures as facts, marked F10: an average
live time of 54 against 7 (p. 248).

**(b) `kitchen-sink` (Abstract Data Types and Interfaces).** The book's
example of a poor abstraction (§6.2, p. 134) is a C++ `class Program` whose
public routines are `InitializeCommandStack`, `PushCommand`, … report
formatting … `InitializeGlobalData`, `ShutdownGlobalData`. The spec's `Program`
class has the same name and the same three groups of routines. Replace it
with this class (17 lines, compiles):

```java
public abstract class Kiosk {
    public String location;
    public Printer printer;
    private int ticketsIssued;
    private int refundsToday;
    private Forecast forecast;
    private String forecastCity;
    private Writer auditLog;
    private int auditLines;
    private boolean maintenanceMode;

    public abstract Ticket issueTicket(Fare fare);
    public abstract void refundTicket(Ticket ticket);
    public abstract Forecast fetchForecast(String city);
    public abstract void showForecast();
    public abstract void openAuditLog();
    public abstract void closeAuditLog();
}
```

The tiles are unchanged: `coFields` 9, `coPublicFields` 2, `coRoutines` 6,
`coPublicRoutines` 6. Under the class view's rule, a depth-1 line with `(`
ending in `;` is a routine.

**(c) `total-first` / `in-order` / `hidden` (Organizing Straight-Line Code).**
The book's §14.1 example (p. 348) is `ComputeMarketingExpense`,
`ComputeSalesExpense`, `ComputeTravelExpense`, … then a display of the
summary. The spec's marketing/sales/travel ledger is that example. Replace
the domain, for example a parcel quote. `total-first`:

```java
double shippingQuote(Parcel parcel) {
    double total = base + surcharge + insurance;
    double base = parcel.baseRate();
    double surcharge = parcel.fuelSurcharge();
    double insurance = parcel.insuranceFee();
    return total;
}
```

`hidden` becomes `quote.loadRates(); quote.addSurcharges();
quote.addInsurance(); quote.print();`. Every figure is unchanged in shape:

- `total-first`:
  - `coAnomalies` 6.
  - `coUsedBeforeSet` "base (line 2), surcharge (line 2), insurance (line 2)".
  - `coDeps` "1→3, 1→4, 1→5, 2→6". See SF-9: the spec does not state this
    tile at all.
- `in-order`: 0 anomalies, `coDeps` "1→2, 1→3, 1→4, 2→5, 3→5, 4→5, 5→6".
- `hidden`: 0 anomalies, `coDeps` "1→2, 1→3, 1→4, 1→5".

**(d) The grade table (Table-Driven Methods).** The book's stair-step example
(§18.4, p. 426) is a grade scale with breaks at 90.0, 75.0, 65.0 and 50.0
percent. The spec's instance `50, F; 65, D; 75, C; 90, B; 101, A` uses the
same breakpoints. Use a domain the book does not, for example a
late-return fee by days overdue: `7, 0; 14, 2; 30, 5; 60, 10; 365, 20`. The
presets keep every count (COMPUTED):

| new preset | old preset | `seValue` | `seLinear` | `seBinary` |
| --- | --- | --- | --- | --- |
| `days-20` | `grade-72` | 5 | 3 | 2 |
| `days-60-below` | `grade-90-below` | 20 | 5 | 3 |
| `days-60-atmost` | `grade-90-atmost` | 10 | 4 | 3 |

The Worked line becomes: "20 is not below 7 or 14 and is below 30: fee 5,
after 3 comparisons; binary search tests 30, then 14: 2."

Lesser overlaps, listed under **Consider** (C-8): the busiest-loop numbers,
the character-classification chain, and the payroll domain of `overtime`.
They are figures or domains, not listings, but the busiest-loop numbers
must at least be attributed (SF-12).

### MF-2. `testing-only` contradicts the book it reads along with (Software-Quality Landscape) — CERTAIN / COMPUTED

The preset computes 1,000 × 0.70 × 0.65 × 0.60 = 273 left, so a combined
**72.7%**. The arithmetic is right. But §20.3 says that Jones finds a
combination of unit, functional and system testing "often results in a
cumulative defect detection of less than 60 percent" (p. 471). §22.1 repeats
it: "less than 60 percent of the errors present (Jones 1998)" (p. 500).

A lesson that shows 72.7% beside "testing is how you get quality" teaches
the reader a figure 13 points above what the book reports. The independence
assumption is exactly what makes the product optimistic: stages tend to find
the same easy defects.

**Replacement.** Keep the preset, which is honest arithmetic. Add to the
Misconception or `note`: "The product assumes each stage's misses are
independent of the last. The book reports that real combinations of
testing alone often catch less than 60 percent (Jones, p. 471), and that a
typical test-heavy organisation reaches about 85 percent overall against 95
percent or more for those that combine unlike techniques (Jones 2000,
p. 470). Read 72.7% as an upper bound."

The book itself does this multiplication for Extreme Programming's practices
in **Table 20-3** (p. 472: ~74%, ~90%, ~97%). Cite that as the source of the
method, and do not reproduce the table. F17 should be updated to match (see
§S.2 below).

### MF-3. The Square/Rectangle exercise does not break (Inheritance, Containment and Members) — COMPUTED

As written, `Square` "overrides `setWidth` to set the height too". A caller
does `setWidth(4)`, which sets w = h = 4. It then does `setHeight(5)`, which
is not overridden, so h = 5. The area is **20**, exactly what the caller
expected. This was confirmed by running it. Only a square that overrides
**both** setters breaks this caller: area 25.

**Replacement:** "a `Square` that extends `Rectangle` and overrides
`setWidth` and `setHeight` so that each sets both sides breaks a caller that
sets the width to 4, then the height to 5, and expects an area of 20: it
gets 25."

The LSP is in §6.3, pp. 144–145, citing Liskov 1988 — CERTAIN. The year is
right, so the `(check year as cited)` can be resolved.

### MF-4. `kitchen-sink` Misconception contradicts its own tile (Abstract Data Types) — COMPUTED

"`kitchen-sink`'s routines have no fields in public but six unrelated
abstractions in one class" is wrong on both counts. The preset's own pinned
`coPublicFields` is **2**. Its six routines fall into **three** groups
(command stack, report, global data; in the MF-1(b) replacement: tickets,
forecast, audit log).

**Replacement:** "`kitchen-sink` exposes two fields and six public routines
that serve three unrelated abstractions — tickets, the weather forecast and an
audit log — in one class; no accessor discipline fixes that."

### MF-5. Two class snippets exceed the line limits — COMPUTED

§C requires snippets of at most 20 lines unless an entry says otherwise, and
only `nested-shipping` is excepted. R1 (§H.1) caps a `code` block at 30
lines, enforced by a test.

- `private-fields` is 24 lines.
- `kitchen-sink` is 35 lines. As specified it cannot render: the test raises.

**Fix:**

- `private-fields`: delete its four blank lines. That gives 20 lines, and the
  tiles are unchanged (5, 0, 4, 3).
- `kitchen-sink`: the MF-1(b) replacement is 17 lines.

### MF-6. `run/arith` refuses zero, and so refuses its own preset (§D.1) — JUDGEMENT on the wording

"`double` … refuses … results outside the normal range". Zero is not a
normal binary64 number. `tenth-ten-times` starts at `0`, and `cents` is
`int`, so it is unaffected. Read literally, the rule refuses
`tenth-ten-times`.

**Replacement:** "refuses division by zero, a result whose magnitude exceeds
`Double.MAX_VALUE`, and a non-zero result smaller in magnitude than
`Double.MIN_NORMAL` (a subnormal), each with a sentence; zero is a normal
result."

While here: Java does **not** throw on `double` division by zero; it prints
`Infinity` or `NaN`. The refusal sentence should say so ("Java would print
Infinity; this lab does not model it"). The lesson should not imply an
exception.

---

## Should-fix

### SF-1. Chapter 11 section numbers (The Power of Variable Names) — CERTAIN

Chapter 11 has seven sections (contents and p. 259):

| section | title |
| --- | --- |
| 11.1 | Considerations in Choosing Good Names |
| 11.2 | Naming Specific Types of Data |
| 11.3 | The Power of Naming Conventions |
| 11.4 | Informal Naming Conventions |
| 11.5 | Standardized Prefixes |
| 11.6 | Creating Short Names That Are Readable |
| 11.7 | Kinds of Names to Avoid |

The Read line should say "§11.3–11.4, naming conventions and informal
conventions; §11.5, standardized prefixes; §11.6, short names; §11.7, kinds
of names to avoid", and the Sources line "§§11.1–11.7".

Every other section number and title in §B and §C was checked against the
contents and the chapter openings, and is the book's: all 35 chapter titles,
and every split in §B. Basis testing is in §22.3, before data-flow testing,
so the Chapter 22 split holds. **All *(check)* marks on section titles can be
removed.**

### SF-2. The "only 0 and 1" rule is §12.1, not §12.7 — CERTAIN

The rule is on p. 292 ("Numbers in General"). Move it from the Named
Constants and Other Types Read line to Integers and Floating Point's §12.1
item, or keep the lesson and say "the rule of §12.1". Set F12's "where" to
§12.1 (p. 292).

### SF-3. Programmer variation (F29) is in §28.5 and §33.1 — CERTAIN

- §28.5 "Individual Variation", p. 682: Sackman, Erikson and Grant 1968 found
  coding time about 20:1, debugging over 25:1, program size 5:1, execution
  speed about 10:1, among programmers averaging 7 years' experience. They
  found no relation between experience and quality or productivity.
- §33.1, p. 820: "Study after study" finds about 10:1 in creation time,
  debugging time, size, speed, error rate and errors detected (Sackman et al.
  1968; Curtis 1981; …).

Personal Character can keep it (cite §33.1, p. 820). F29's "where" becomes
"§33.1 p. 820; detail in §28.5 p. 682".

### SF-4. Routine Length worked line miscounts (Routine Length and Parameters) — COMPUTED

"nine parameters, six of which describe the line or its tax" is wrong.

- The line takes six: `sku`, `description`, `quantity`, `unitPriceCents`,
  `discountPercent` and `taxable`. `taxable` belongs to the line, as
  `line.isTaxable()` shows.
- The tax rule takes one: `taxRatePermille`.
- The format takes two: `currency`, `showSku`.

That is **seven** for the line or its tax. **Replacement:** "nine parameters,
seven of which describe the line or its tax, become two objects and a
format."

The pinned tiles (`coParams` 9/3, `coCode` 9/5, `coLines` 10/6) are right.

### SF-5. `expireSessions` exercise: the obvious fix is itself a defect (Pseudocode Programming Process) — COMPUTED

The missing step is "remove it from the live list". Writing
`sessions.remove(s);` inside the enhanced `for` over `sessions` throws
`ConcurrentModificationException`. Add to the answer: "the code the step
needs must remove through an `Iterator` (`it.remove()`), since the enhanced
`for` cannot remove from the list it iterates". The step count (4, line 10
empty) is right.

### SF-6. `run/loop` closed form is wrong at the edges and against Java (§D.1) — COMPUTED

- `ne` "ends only when (bound − start) is a **positive** multiple of step".
  With `start == bound` the loop runs **0** times and ends. Say "a
  non-negative multiple (0 included)".
- `lt` (and `le`, `gt`, `ge`) with the step pointing away from the bound is
  said to "never end". In Java `int` it ends after the index wraps past
  `Integer.MIN_VALUE`: `for (int i = 0; i < 10; i -= 1)` runs 2,147,483,649
  times.

  Since overflow "is not modelled", the tile must not assert a Java fact it
  has not computed. Print "never ends without overflow" (or "runs until `i`
  overflows"), and keep plain "never ends" for the `ne` case. There, Java
  really does loop for ever, because every value of `i` keeps the parity of
  `start` and never meets `bound`. That makes `skips-the-bound` correct as
  pinned.
- State the zero-iteration case: `lt` with `start ≥ bound` gives
  `lpIterations` 0, `lpLast` "—", `lpAfter` = start (and the mirror cases).
- "step ≤ 0" contradicts "non-zero integers"; say "step < 0".

All four presets recomputed: `fencepost` 11/10/11, `half-open` 10/9/10,
`counting-down` 11/0/−1, `skips-the-bound` never ends. The exercise
(10, gt, 0, −3) gives 4 iterations, last value 1, −2 after. All right.

### SF-7. `nuJava` formatting in §C contradicts §D.0 — COMPUTED

§D.0 says `nuJava` prints ASCII `-`. §C writes `nuJava` −2147483648 and
−2147479015 with U+2212. The pinned strings must be `-2147483648` and
`-2147479015`. The values are right: 2³¹ wraps, and 46341² = 2,147,488,281 =
2³¹ + 4,633 wraps to −2,147,479,015. The exercise is also right:
`365*24*60*60*1000` prints `1471228928` against 31,536,000,000, confirmed by
running it. The `nuExact` for `int-division` will print `7/2 = 3.50` under
§D.0's format, not "7/2"; state it.

### SF-8. Zero denominators are unspecified across §D — COMPUTED

§D.0 requires hostile input to blank tiles with a red banner, but these
lawful inputs divide by zero, and §D does not say what the kit prints:

| view | tile | zero case |
| --- | --- | --- |
| `removal` | `dfCombined` | `injected` = 0 |
| `pipeline` | `dfPerDefect` | nothing found |
| `speedup` | `pfSpeedup`, `pfSaved` | all times 0 |
| `shares` | `pfTagged`, `pfTop` | total 0 |
| `cost` | `dfRatio` | all counts 0 |
| `language` | `pjEquivalent`, `pjDays` | `ratio` or `rate` 0 |
| `scale` | `pjStaffYears` | `prodLow` 0 |
| `coupling` | `dgConnected` | one module: 0 pairs |
| `chain` | `seExpected` | all frequencies 0 |
| `span` | `coAvgSpan` | every variable referenced once: no spans |
| `names` | `coAvgLen` | no counted names |
| `size` | `coDensity` | no code lines |
| `effort` | `pjProduct` | no records |

**Add to §D.0:** "A share or mean whose denominator is zero prints `—` with a
banner sentence naming why (for example 'no spans: each variable is
referenced once'); an input that is a divisor (`ratio`, `rate`, `prodLow`,
`prodHigh`) must be positive and is refused otherwise." `mathcheck.js` should
get one zero case per view.

### SF-9. Three pinned tiles have no stated value in §C — COMPUTED

§C says "Pins …" without giving the value for:

- `total-first` `coDeps`: **"1→3, 1→4, 1→5, 2→6"**. Line 2's reads find no
  earlier set; lines 3–5 read the parameter; line 6 reads `total`.
- `everything-talks` `dgFanIn`: **"billing 4"**. All five tie at 4, so the
  alphabetical rule applies and the banner names all five.
- `shallow` `dgDeepest`: **"Circle"**. Three-way tie at depth 2, the banner
  names `Circle, Square, Triangle`.

Record them, so that the tie rule is pinned deliberately rather than
discovered.

### SF-10. `range` evaluation points must include each literal itself (§D.1) — JUDGEMENT

"every literal c ± 1" should read "every literal c and c ± 1 (clamped to
`int`)". For `==` and `!=` the value c is where the check changes. A literal
outside `int` is a Java compile error, so it should be refused. All six
range presets were recomputed:

| preset | check | `cdDisagree` | `cdExposed` |
| --- | --- | --- | --- |
| `correct` (month) | `month < 1 \|\| month > 12` | none | none |
| `off-by-one` | `month < 0 \|\| month > 12` | 0 | 0 |
| `wrong-operators` | `month <= 1 \|\| month >= 12` | 1, 12 | 1, 12 |
| `correct` (qty) | `qty >= 1 && qty <= 99` | none | none |
| `strict-top` | `qty > 0 && qty < 99` | 99 | 99 |
| `no-lower-check` | `qty <= 99` | 0 and below | 0 |

Both exercises were also recomputed:

- Ages: the check accepts everything, `cdDisagree` "−1 and below, 121 and
  above", exposed −1 and 121.
- Passwords: the check is wrong at 8 only.

### SF-11. Register corrections (F2, F3, F7, F8, F16, F17, F18, F21, F25, F26, F28) — CERTAIN

See the §S.2 table below for each. The material ones:

- **F2**: the book's figures are not in §1.2. They are in §22.4 and §27.3
  (pp. 520–521, 652).
- **F7**: McConnell calls Riel's six levels "grossly optimistic" and says
  most people manage two or three (p. 147). The `deep` preset's depth of 7
  should be read against his figure, not Riel's.
- **F16**: the source is Jones **1986a**, 1996 and Shull et al. 2002, not
  Jones 2000.
- **F18**: Microsoft's 3 h against 12 h is to "find **and fix**". IBM's 3.5
  against 15–25 h is to find.
- **F26**: Table 28-1, p. 674, prints **percentages**, for example programmer
  capability −24%/+34%. They equal the COCOMO II multipliers 0.76/1.34, so
  `effort`'s presets are correct. Use the book's factor names ("Requirements
  analyst capability", "Use of software tools").

### SF-12. The busiest-loop preset is the book's own example — CERTAIN

§26.2, p. 623, has exactly the outer 100 and inner 5 loops: 600 against 505
iterations, "about … 16 percent", then measured savings of 33% (C++), 34%
(Java), 12% (PHP) and 4% (Python). `busiest-outside` and the Misconception
("16% of iterations is not 16% of time") are that passage.

That is a fair use of the figures, but the lesson must say they are the
book's example (F23, p. 623), not "illustrative". The book's measured row
may be quoted as facts, a few at a time. The `three-levels` preset and the
exercise are the lesson's own. All the figures were recomputed:

| preset | `lpBody` | `lpIterations` | `lpBest` | `lpSaved` |
| --- | --- | --- | --- | --- |
| `busiest-outside` | 500 | 600 | 505 | 19/120 ≈ 15.8% |
| `three-levels` | 1,000 | 1,550 | 1,022 | 264/775 ≈ 34.1% |

The exercise gives 4,000 against 3,003.

### SF-13. Sources the book does not cite — CERTAIN

The book's bibliography and text were searched for each §S.1 work.

- **Feldman 1979 (make) is not cited** (not in the bibliography or
  anywhere in the text). Drop it from Programming Tools, or cite it as the
  lesson's own reference, outside "as the book cites it".
- **Goldberg 1991 is not cited.** Drop it from Integers and Floating Point.
- **Brooks's law** is cited from the 1995 anniversary edition (p. 676), so
  say "Brooks 1995".
- **Boehm 1987** is "1987b" in the book.
- **Miara et al. 1983** is spelled "Miaria" in the book (p. 737 and the
  bibliography). Keep the correct spelling and note it.
- **Wicked problems** are Rittel and Webber 1973 (p. 74), with Peters and
  Tripp 1976. Simon 1996 is cited in Chapter 5 for a different point.
  Replace "Simon 1996 and Rittel on wicked problems" with "Rittel and Webber
  1973, as the book cites them".
- **Add to §S.1** works the register now needs:
  - Jones 1986a (*Programming Productivity*);
  - Shen et al. 1985;
  - Card and Glass 1990;
  - Yourdon 1986a and 1986b;
  - Freedman and Weinberg 1982;
  - Putnam and Meyers 1997;
  - Cusumano et al. 2003;
  - Dunn 1984;
  - Myers 1976, Marca 1981, Ledgard and Tauer 1987a (nesting).
- **Kaplan 1995 and Moore 1992** are cited in the text (pp. 472–473, 521) but
  are not in the book's bibliography. Cite them "as the book cites them" and
  do not give titles.

---

## Consider

- **C-1. Ternary operator.** Table 19-2 (p. 458) counts "if while repeat for
  and or, or their equivalents". `?:` is the expression equivalent of `if`,
  and most tools count it. Either count it (one point, and say so in the
  rule), or keep the kit's choice and word the banner as the kit's choice,
  not the book's.
- **C-2. Band boundary.** The book's bands are "0–5", "6–10", "10+" (p. 458):
  10 sits in two bands. The kit's "above 10" puts 10 in the middle band. Say
  that in the `coBand` banner.
- **C-3. Support for the Nesting misconception.** The book says directly
  that moving part of a routine into another doesn't reduce the overall
  complexity of the program (p. 458). Cite it in Nesting and Complexity's
  Misconception; it is the book's own point.
- **C-4. Test-first is endorsed, not contested.** McConnell calls test-first
  "one of the most beneficial software practices" (§22.2, p. 504). The
  "modern aside" in Structured Basis Testing should not frame TDD as a later
  view against the book. Frame it as what the practice became.
- **C-5. Compile errors the lessons can use.**
  - `count-unset` (as the spec says) is rejected by `javac`.
  - `total-first` is rejected ("cannot find symbol"): the compiler catches
    the *visible* order dependency.
  - Declaring and Initializing's exercise is rejected ("variable result might
    not have been initialized").

  All three compile errors were confirmed. Saying so strengthens both
  lessons: the lab misses the exercise, and Java's definite-assignment rule
  catches it. The `clamp` unreachable-statement claim is right.
- **C-6. Data-flow anomalies come from §22.3.** "Defined-defined",
  "used-before-defined" and the rest are the book's data-flow testing
  (§22.3). Cite that section where `dataflow` is introduced, as well as
  §10.3.
- **C-7. Metaphors.** McConnell calls the farming metaphor "terrible" and
  "weak", and is critical of the writing metaphor (§2.3). The Read line
  should say he rejects both, not list them neutrally.
- **C-8. Lesser overlaps with the book's examples.**
  - The `search/chain` cases (digit, punctuation, space, letter) are the
    book's character-classification example (§15.1, p. 359). Use other cases,
    for example HTTP status classes.
  - The `overtime` payroll domain echoes the basis-testing example (pp.
    506–507). The code differs; acceptable.
- **C-9. `access-routines` (Structures, Pointers and Global Data).** It
  drops the six caller routines, so `dgCoupled` 0 is true by construction.
  Consider keeping the callers as readers and writers of the access routines'
  names, so the lab shows that coupling moves behind one owner rather than
  vanishing. Otherwise the note should say the callers are left out. The
  `globals` figures (3 globals, 6 routines, 9 of 15 pairs, "current, 5
  routines") and the worked 7 + 1 + 1 are right.
- **C-10. `nuJava` for `double` and Java versions.** "Shortest decimal that
  rounds back" is `Double.toString` only from JDK 19 (JDK-4511638). Earlier
  JDKs print longer strings for some values. Also name Java's form: "1.0"
  not "1", and scientific notation below 10⁻³ and from 10⁷. Say "as JDK 19
  or later prints it".
- **C-11. `recursion` values against Java `long`.** For `factorial` with n ≥
  21, a Java `long` overflows, while `lpValue` prints the exact value. Say so,
  or cap `factorial` at 20. Fibonacci to 90 fits in `long`.
- **C-12. A ready-made exercise for Code-Tuning Strategies.** Bentley's
  square-root case (p. 592): 80% of time in one routine made three times
  faster gives 0.2 + 0.8/3 = 7/15 of the time, a speedup of 15/7 ≈ 2.14.
- **C-13. Effort lesson misconception.** "Who is on the team moves the
  estimate by more than how many" is not something the `effort` lab
  computes, since it has no team-size input. Reword it to what the tiles show
  (capability factors move effort by roughly 0.54× to 1.90× in the presets),
  or drop it.

---

## §S.2 register — verified against the book

Printed page numbers; all **CERTAIN** unless marked.

| id | spec's belief | the book | verdict and correction |
| --- | --- | --- | --- |
| F1 | 30–80% of project time | "30 to 80 percent of the total time", depending on size (§1.2, p. 7). §27.5 (p. 654): as much as 65% on small projects, about 50% on medium | correct |
| F2 | construction errors as a share, "§1.2" | Not in §1.2. §22.4 (pp. 520–521): at least 35% of all defects regardless of size; Figure 22-2 caption 45–75% even on the largest projects. §27.3 (p. 652): about 75% on small projects, ~50% larger, up to 75% at 500,000 lines (Grady 1987) | **move to §22.4/§27.3** |
| F3 | Table 3-1 values; sources | Table 3-1 p. 29, values exactly as the spec gives them | values correct. **Add Dunn 1984** to the sources. Tables 3-3/3-4 (pp. 33–34) support the iterative-projects Misconception |
| F4 | ratios; Jones 1998, Prechelt 2000 | Table 4-1 p. 62, values exact; source Jones 1998, Boehm 2000, Prechelt 2000 | correct; **add Boehm 2000** |
| F5 | ~30% with 3+ years | p. 62, Cocomo II data, Boehm et al. 2000 | correct |
| F6 | > about 7 data members | §6.3 p. 143–144, Miller 1956 and Riel 1996 | correct; add Riel |
| F7 | shallow; six levels cited | §6.3 p. 147. Riel suggests six; McConnell: "grossly optimistic", most people manage 2–3. Basili, Briand and Melo 1996: deep trees significantly associated with fault rates | **state McConnell's 2–3** |
| F8 | tolerate ~100–200 lines | §7.4 pp. 173–174: allow growth "up to 100–200 lines" (a noncomment, nonblank line); careful past 200. Studies: Basili and Perricone 1984; Shen et al. 1985; Card, Church and Agresti 1986 / Card and Glass 1990 (≤32 lines not cheaper; ≥65 cheaper per line); Selby and Basili 1991 (<143 statements: 23% more errors per line, 2.4× cheaper to fix); Lind and Vairavan 1989 (100–150); Jones 1986a (>500 most error-prone) | correct; **add Shen 1985, Card and Glass 1990**; note the book's line excludes comments and blanks while `coCode` counts braces |
| F9 | about seven parameters | §7.5 p. 178, Miller 1956 | correct |
| F10 | definitions; book's example figures | §10.4 pp. 245–248: span = lines between references; average span = mean of the spans; live time counts first through last line inclusive; book's example averages 54 against 7 | correct. The spec's pooled `coAvgSpan` over several variables is the lab's extension; say so. Listing numbering counts the comment line, supporting §D.0 |
| F11 | 10–16 best; 8–20 almost as good | §11.1 p. 262, Gorla, Benander and Benander 1990. About the *average* over a program, not each name | correct; the `coShort` per-name list is the lab's reading, so say so |
| F12 | only 0 and 1 | §12.1 p. 292 | correct value; **location §12.1** (SF-2) |
| F13 | loop short enough to see; ≤3 levels | §16.2 p. 385: one screen (50 lines) or one page; "rarely … longer than 15 or 20 lines"; limit nesting to three levels (Yourdon 1986a) | correct |
| F14 | rule and bands | Table 19-2 p. 458, exactly as the spec says; bands 0–5 / 6–10 / 10+ (§19.6) | correct; see C-1, C-2. Chapter 22's basis rule (p. 506) adds "+1 if a case statement has no default" — the spec's `basis` view is right |
| F15 | >3 levels of nested ifs | §19.4 p. 445: Chomsky and Weinberg via Yourdon 1986a; 3–4 levels (Myers 1976, Marca 1981, Ledgard and Tauer 1987a) | correct |
| F16 | Table 20-2 rates | Table 20-2 p. 470: all 13 rows exactly as the spec gives them | values correct; **source is Jones 1986a, 1996; Shull et al. 2002** (not 2000) |
| F17 | none >75%; average ~40%; combination for 95% | p. 470: modal never above 75%, average about 40%; typical test-heavy orgs ~85%, leading orgs ≥95% (Jones 2000); p. 471: unit + functional + system testing often <60%; Myers 1978b; Table 20-3 (p. 472) multiplies rates for XP: ~74/~90/~97% | correct, **add the <60% and Table 20-3** (MF-2) |
| F18 | 3.5 vs 15–25 h (IBM); 3 vs 12 (Microsoft) | §20.3 pp. 472–473: Kaplan 1995 (find); Moore 1992 (find **and fix**) | correct; location §20.3 |
| F19 | 1–25/KLOC; Microsoft; cleanroom; 80/20 | §22.4 p. 521: industry 1–25 per KLOC delivered; Microsoft 10–20 in-house / 0.5 released (Moore 1992); cleanroom 3 / 0.1 (Cobb and Mills 1990); space shuttle; TSP ~0.06. p. 517: 80% of errors in 20% of classes or routines (Endres 1975, Gremillion 1984, Boehm 1987b, Shull 2002); 50% in 5% (Jones 2000) | correct |
| F20 | fastest ~⅓ the time, fewer new defects | §23.1 p. 537, Gould 1975: 5.0 against 14.1 minutes; defects not found 0.7 against 1.7; defects made correcting 3.0 against 7.7 | correct |
| F21 | one-line changes high error rate | §24.4 pp. 580–581: Figure 24-1 (Weinberg 1983): chance of a bad change *rises* from one to five lines, then falls; reviews of one-line changes cut errors 55% → 2% (Freedman and Weinberg 1982); first attempt at a change >50% wrong (Yourdon 1986b) | **reword**: "small changes (one to five lines) are more error-prone than larger ones" |
| F22 | 20/80; <4% → >50% | §25.2 p. 592: Boehm 1987b; Knuth 1971 | correct |
| F23 | per-language timings | e.g. §26.2 p. 623, the busiest-loop table | exists; see SF-12 |
| F24 | Table 27-1 | p. 652, values exact; sources Jones 1977, Jones 1998 | correct; add Jones 1977 |
| F25 | Table 27-2 | p. 653, ranges exact (Cocomo II nominal in parentheses: 4,000 / 3,200 / 2,600 / 2,000 / 1,600) | values correct; **sources: Putnam and Meyers 1992, 1997; Boehm et al. 2000; Cusumano et al. 2003** (not Jones 1998) |
| F26 | COCOMO II ranges | Table 28-1 p. 674 gives percentages from Boehm et al. 2000. Programmer capability −24%/+34%; requirements analyst −29%/+42%; product complexity −27%/+74%; time constraint 0/+63%; storage 0/+46%; tools −22%/+17%; personnel continuity −19%/+29% | values correct (they are the multipliers); the book *does* give a table; use its factor names |
| F27 | 2–4 spaces best | §31.2 p. 737: subjects scored 20–30% higher with two-to-four-space indentation than none; lowest no indentation, second lowest six spaces ("Miaria et al. 1983") | correct |
| F28 | ~1 comment per 10 statements | §32.4 "Optimum Number of Comments", p. 792: IBM studies via Jones 2000; fewer *and* more reduced understandability | correct; **source Jones 2000** |
| F29 | ~10:1 | §33.1 p. 820 and §28.5 p. 682 | correct value; **location** (SF-3) |

The other *(check)* items in §C:

| item | resolution |
| --- | --- |
| Liskov 1988 | correct (p. 144; bibliography "SIGPLAN Notices, May 1988") |
| Stevens, Myers and Constantine 1974 | cited for cohesion (§7.2) — correct |
| Yourdon 1986 (F13, F15) | "1986a" |
| Goldberg 1991 | not cited (SF-13) |
| Feldman 1979 | not cited (SF-13) |
| Simon 1996 / Rittel | see SF-13 |
| Basis testing in Chapter 22's first half | yes: §22.3 p. 505ff, before data-flow testing |
| Table numbers | 3-1, 4-1, 19-2, 20-2, 20-3, 27-1, 27-2 and 28-1 are all right where the spec names them |

## What the spec says McConnell argues — chapter by chapter

Checked against the text. Agreed unless noted.

- **Chapters 1–4.** The construction activities, construction's share (F1),
  and the source code as the only accurate description are all right.
  - Metaphors: see C-7.
  - Prerequisites: the cost table and the iterative argument are right
    (Tables 3-3/3-4). §3.6 gives a figure the lesson could use: 10–20% of
    effort and 20–30% of schedule upstream (p. 55).
  - Language choice, conventions and "programming into a language" (§4.3)
    are right.
- **Chapter 5.** Wicked problem (Rittel and Webber), essential and accidental
  difficulties (Brooks 1987, the book's "No Silver Bullets"), managing
  complexity as the primary technical imperative (p. 77), the desirable
  characteristics, levels of design, the heuristics list, and Parnas on
  information hiding are all right.
- **Chapters 6–9.** ADT benefits, interfaces, containment before
  inheritance, LSP, 7±2 data members, routine reasons, cohesion, length and
  parameters are right (F6–F9). The defensive-programming technique list and
  the PPP steps are right.
- **Chapters 10–13.** Span and live time (F10), name length (F11), magic
  numbers (F12) and the global-data argument are right. Table 13-1 compares
  direct access with access routines; do not reproduce it.
- **Chapters 14–19.**
  - Order dependencies (but see MF-1(c)).
  - Frequency ordering of tests (§15.1; also §26.1).
  - Loop guidance (F13).
  - "Don't use recursion for factorials or Fibonacci numbers" (p. 397), the
    goto debate, and the stair-step endpoints (§18.4, but see MF-1(d)).
  - DeMorgan (Table 19-1), nesting (F15), structured programming (Böhm and
    Jacopini 1966) and McCabe (F14).
- **Chapters 20–26.**
  - Quality characteristics, Table 20-2/20-3 and "improving quality reduces
    cost" (§20.5).
  - Inspections: Fagan; 21.1 repeats 55%/60% for design and code inspections.
  - Basis testing and its rule (p. 506), boundaries (Myers 1979), typical
    errors (F19), the scientific method of debugging, binary search and
    time-boxed brute force (§23.2), refactoring safely (F21), Pareto (F22),
    and "measure every change" (§26) are right.
- **Chapters 27–28.**
  - Communication paths n(n−1)/2, and Tables 27-1/27-2 (F24, F25).
  - Construction's falling share (65% to 50%, p. 654).
  - Brooks's law qualified: "if a project's tasks are partitionable" adding
    people can help (p. 676).
  - Effort factors (F26) and individual variation (F29).
- **Chapters 29–35.**
  - Integration strategies: top-down, bottom-up, sandwich, risk-oriented
    ("hard part first"), feature-oriented and T-shaped.
  - Daily build and smoke test, tool fantasyland, and the Fundamental
    Theorem of Formatting (p. 732).
  - Comment density (F28), and laziness as writing a tool to do an unpleasant
    task (§33.7, p. 830, the third of the book's three kinds).
  - The nine themes, whose titles match §34.1–34.9.

## Arithmetic recomputed (all COMPUTED, all agree with §C)

| lesson | preset | figures |
| --- | --- | --- |
| What Software Construction Is | `small-project` | 1,000; 33/50 = 66%; 8/25 = 32% |
| | `large-project` | 12,000; 31/60 ≈ 51.7%; 9/40 = 22.5% |
| | exercise | 180/300 = 3/5 |
| | `pfPareto` | 6 of 8 entries in both presets |
| Metaphors for Software | ripple (`foundation`, `middle`, `paint`) | "1: db" / "5: billing, db, orders, reports, ui"; "2: billing, ui" ×2; "0: none" |
| | exercise | direct `db`, `logging`; 4 in all |
| Upstream Prerequisites | `found-late` | 425–800; 35; 85/7 ≈ 12.1× to 160/7 ≈ 22.9× |
| | `found-early` | 35, 35, 1× |
| | `requirements-late` | 100–1,000; 10; 10×–100× |
| Key Construction Decisions | three language presets | 4,000 / 80 / 200; 5000/3, 100/3, 200; 20000/9, 400/9, 200 |
| | exercise | 12,000; 200 against 500 |
| Design Challenges and Complexity | coupling presets | 5, 20, 10, 1; 7, 10, 7/10, db 3; 5, 10, 1/2, db 2 |
| | exercise | 15 pairs |
| Design Heuristics and Information Hiding | `exposed` / `hidden` | 5 and 6; 1 and 7 |
| Inheritance, Containment and Members | tree presets | 2, 4 classes, 3 leaves; 7, ChristmasHolidaySavings, 8, 2 |
| | exercise | 5 at `Puppy` |
| Abstract Data Types and Interfaces | class presets | 5/5/2/2; 5/0/4/3; 9/2/6/6 |
| Reasons to Create a Routine | dupes presets | 0; 1 block, 6 lines, "lines 3–5 and lines 7–9"; 0 |
| Routine Length and Parameters | size presets | 9/9/10 and 3/5/6 |
| | exercise | 8 parameters to 4 |
| Defensive Programming | `cond/range` | see SF-10 |
| The Pseudocode Programming Process | `free-slot` | 5, 7, "line 14", "3 lines, under line 8" |
| | `complete` | 5, 8, none |
| Declaring and Initializing Variables | dataflow presets | 1 / 0 / 3 with the stated lists |
| Scope, Span and Live Time | old snippet | 11/4, 11, "total: 14"; 1/2, 5, "total: 7" — but see MF-1(a) |
| | exercise | 15/4, live times 11 and 10 |
| The Power of Variable Names | names presets | 7, 4/3, six short names; 7, 28/3, none |
| | exercise | 1; 53/5 = 10.6, only `months` short |
| Integers and Floating Point | `run/arith` | see SF-7 |
| | `tenth-ten-times` | `nuStored` 9007199254740991/9007199254740992, confirmed by running Java |
| Named Constants and Other Types | `magic` | 5, 3, "0.0725 (line 2), 12 (lines 2, 3), 360 (lines 4, 5)" |
| | `named` | 0 |
| Structures, Pointers and Global Data | shared presets | 3, 6, 9 of 15, "current, 5 routines"; 3, 3, 0 |
| | exercise | 2, 3, 3 |
| Using Conditionals | `search/chain` | 7/2, 3/2, 2; 29/20, 29/20, 0; 14/5, 13/5, 1/5 |
| | exercise | 11/4 and 5/4 |
| Controlling Loops | `run/loop` | see SF-6 |
| Unusual Control Structures | `run/recursion` | 10/10/3,628,800/9; 2,692,537/30/832,040/29; 331,160,281/40/102,334,155/39 |
| | exercise | 21,891/20/6,765/19 |
| | check | 2·F(n+1) − 1 equals the call count for every n |
| Table-Driven Methods | grade presets | C 3 2; A 5 3; B 4 3 |
| | `brackets` | 70%, 15, 4 |
| | exercise | 15 (3 linear); 9 (2 linear; 3 binary) |
| Boolean Expressions | truth presets | yes; "no, on 2 of 4 rows", "done = T, error = F"; yes; yes |
| | exercise | equivalent |
| Nesting and Complexity | `nested-shipping` | 9, "1 + if 5 + for 1 + && 1 + \|\| 1", depth 5 at line 14 |
| | `guard-clauses` | 6, depth 1 |
| | `discountPercent` | 7, depth 2 |
| Themes of Craftsmanship | `retry-delay` | 7, depth 2, 16 lines |
| The Software-Quality Landscape | removal presets | 727/273/72.7%; 47543/50, 2457/50, ≈95.1%; 300/700/30% |
| | exercise | 7/10 and 657/1000 |
| Collaborative Construction | pipeline presets | 58, 42, 1,160, 20; 83.2, 16.8, 674, 1685/208 ≈ 8.10; 83.2, 16.8, 458.4, 573/104 ≈ 5.51 |
| | exercise | 37.5, 12.5, 225, 6 |
| Structured Basis Testing | basis presets | 5 with the stated points; 6 with no default 1 |
| | `archiveOld` | 4 |
| Boundaries and Bad Data | `cond/range` | see SF-10 |
| Debugging as Science | `commit-637` | 10 steps with the exact interval list |
| | `commit-63` | 9/10 |
| | `sixty-four` | 6/6 |
| | exercise | 20 and 7 |
| | check | worst case over all k equals bit_length(n − 1) |
| Refactoring Safely | extract presets | "fees, balance" / none / 2; "account, balance, fees" / "balance, fees" / 3; "account" / "balance, fees" / 1 |
| | `printInvoice` | right |
| Code-Tuning Strategies | speedup presets | 910, 100/91; 700, 10/7, 30%; 17003/20, 20000/17003, 2997/20000 ≈ 15.0% |
| | exercise | 999/20000, 19/40 |
| Code-Tuning Techniques | `run/nested` | see SF-12 |
| How Program Size Affects Construction | scale presets | 3, 0–400, 2/5–5; 45, 200–7,000, 5–100; 1,225, 4,000–100,000, 100–10000/7 |
| | exercise | 15 to 66 |
| Managing Construction | effort presets | 1349/2500 and 53.96; 1.9028 and 190.28; 1035213/250000 and ≈ 414.09 |
| | exercise | 1.0452, 52.26 |
| Integration Order | stub and driver presets | "5: db, orders, pricing, ui, widgets" / "0: none"; 0 / 5; "3: db, ui, widgets" / "2: orders, pricing" |
| | exercise | 3 stubs, 0 drivers |
| Programming Tools | ripple presets | 2/3 and 1/2 |
| | exercise | `util.o`, `app` |
| Layout and Style | `dangling-else` | 2, "5, 6" |
| | `two-statements` | 1, "4" |
| | `braced` | 0 |
| | `clamp` | 1, "6" |
| | check | `javac` rejects line 7 |
| Self-Documenting Code | density presets | 7, 5, 5/7; 7, 1, 1/7 |
| Personal Character | breakeven presets | 35, 7/2, 340/3; 18, 72, −29/15; 267, 267/5, −1 |
| | exercise | 24, 24/5, 59/3 |

## Java snippets

Every §D.4 snippet and every `presets.py` snippet compiles under Java 21 with
stub types, except those meant not to:

| snippet | `javac` error | expected? |
| --- | --- | --- |
| `count-unset` | not initialized | yes |
| `clamp` | unreachable statement | yes |
| `total-first` | cannot find symbol | not mentioned in the spec |
| Declaring and Initializing exercise | not initialized | not mentioned in the spec |

See C-5 for the two the spec does not mention. Each lesson's "defect" is a
real defect, with one exception: the Square exercise does not demonstrate
one (MF-3). Each has one defensible answer, with these caveats:

- `expireSessions` (SF-5).
- `free-slot`'s missing step is missing *behaviour* (no log line), which is
  fair under the PPP.
- `notify(User)` overloads `Object.notify()` legally. Renaming it
  `notifyUser` avoids a reader's double-take.

Snippet line lengths:

- `problem-names`' header is 80 characters. That is inside R1's 80, but
  scrolls at 360 px; consider wrapping the parameters.
- Every other snippet is ≤ 72 characters a line.

## Copyright handling

§E.3's rules are sound: 40-word opening quotation, 60 words per lesson,
figures as facts a few at a time, no listings, checklists or tables.
Applying them found MF-1's four adaptations. Two lessons come close to
reproducing a table by quoting many of its cells:

- The Software-Quality Landscape uses five of Table 20-2's thirteen modal
  rates.
- Managing Construction uses up to seven of Table 28-1's factors.

Five values is within "a few", but the lesson should not set them out as a
table. Do not put Table 20-3's six rows into a preset either; cite its three
totals.

## Counts and ids

| check | result |
| --- | --- |
| lessons per course (§C) | 4, 8, 6, 7, 8, 4, 4 = 41, matching §A and §B |
| views | 12 + 5 + 2 + 3 + 4 + 3 + 2 + 4 = 35 |
| longest lesson slug | `design-heuristics-and-information-hiding`, 40 characters; check id 58 ≤ 72 |
| course slugs | ≤ 36 characters |
| §H.3 counts | 113 + 7 = 120 courses; 1,100 + 41 = 1,141 lessons; 1,230 + 49 = 1,279 pages; 160 + 8 = 168 modes; 23 + 1 = 24 kits — all consistent with `AGENTS.md` and `README.md` today |

## Summary of must-fix items

1. **MF-1.** Replace four adaptations of the book's examples with the given
   instances and recomputed figures:
   - the live-time listing, `auditShipments`: 16/3 and 41/3 against 7/3 and
     23/3;
   - the `Program` class, replaced by `Kiosk`: 9/2/6/6;
   - the expense-ordering trio, replaced by a parcel quote;
   - the grade breakpoints, replaced by a late-fee table: same counts.
2. **MF-2.** `testing-only`'s 72.7% must be set beside the book's "less than
   60 percent" for testing combinations (p. 471) and the 85%/95% figures, and
   the lesson must cite Table 20-3 as the book's own use of the product.
3. **MF-3.** The Square/Rectangle exercise only breaks if both setters are
   overridden: area 25, not 20.
4. **MF-4.** The `kitchen-sink` Misconception says no public fields and six
   abstractions; the tile says 2 public fields, and there are three
   abstractions.
5. **MF-5.** `private-fields` (24 lines) and `kitchen-sink` (35 lines) break
   the 20-line rule, and `kitchen-sink` breaks R1's 30-line cap.
6. **MF-6.** `run/arith`'s "outside the normal range" refusal rejects zero and
   therefore `tenth-ten-times`; reword it, and say Java prints `Infinity`
   rather than throwing on `double` division by zero.
