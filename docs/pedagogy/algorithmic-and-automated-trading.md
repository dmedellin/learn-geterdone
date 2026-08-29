# Pedagogy assessment — Algorithmic and Automated Trading (trading, course 8)

First-pass assessment, formed from the sixteen lessons, the course home, the
published schema and the per-lesson lab scripts as they stand on `main` at
8443158. There is no prior assessment of this course, so there is no delta
section.

Course home: `site/algorithmic-and-automated-trading/index.html`. Lessons, in
course order: `algorithmic-and-automated-trading-fundamentals`,
`trading-system-architecture-and-components`,
`market-data-ingestion-and-normalization`,
`time-sessions-events-and-scheduling`, `signal-engine-and-strategy-state`,
`portfolio-position-and-risk-engine`, `broker-apis-and-order-lifecycle`,
`order-management-and-execution`, `paper-trading-and-forward-testing`,
`scanners-alerts-and-human-approval`,
`reliability-idempotency-retries-and-recovery`,
`observability-logging-and-auditability`,
`security-secrets-permissions-and-kill-switches`,
`deployment-environments-and-configuration`,
`ai-assisted-and-agentic-trading-workflows`,
`automated-trading-system-specification-and-production-readiness`. The
published asset `automated-trading-system-schema.json` is the export shape
lesson 16 claims.

As in course 7, each page ships its own lab: a shared block (helpers, the bar
generator, the two chart painters, the flow, event-log, status and check
renderers, the quiz engine) and an `initLabSpecific()` written per lesson.
Seven pages carried a participation-reading table and a four-argument
`marketRead`; nine carried neither, so the shared block existed in two
variants, and `behavior('bear')` on every page had been softened to "This
sample is generated with a downward drift; read the series in front of you
for what it actually did" to cover a bearish sample that rises (below). No
figure is written into the static HTML — every number the reader sees is
produced by script — so what can be wrong is the arithmetic, the labs'
verdicts, whether a control does what its label says, and whether a drill
measures what its lesson promised. Every number below was obtained by
executing the shipped script in a stub DOM, before and after, not by reading
it.

The home is honest about what the course assumes: "risk per trade, position
sizing, expectancy and out-of-sample validation already mean something to
you — courses 6 and 7 define them", and "it assumes nothing about distributed
systems: idempotency, reconciliation, traces, secret rotation and rollback are
introduced here". That holds. Lesson 08 uses basis points and a decision-price
benchmark the way course 7's cost lesson defined them; lesson 06 sizes by
stop distance the way course 6 does; nothing in the course reaches forward
except one phrase — lesson 04's process step asks for "idempotent run
identifiers" seven lessons before lesson 11 says what idempotent means. It
now carries a one-clause gloss and a pointer. Inside the course the order is
the dependency order the home states: the boundaries (02) are what the data
(03) and the clock (04) are delivered across, the state (05) and the limits
(06) are what the broker calls (07, 08) act on, the paper run (09) and the
approval gate (10) are what decide whether it may run, and reliability,
observability and security (11–13) presuppose having seen an order's status
arrive out of order. Every objective is already an act — separate, define,
receive and validate, use, convert, maintain, submit and reconcile, select and
measure, run and compare, screen and expire, design, measure, protect, build,
use, combine — and none says "understand"; what the course lacked was the
drill that measures the act, and the lab that produces the number the act is
about.

## What the course teaches well

- **The course home is the best-written page in the course.** It names the
  hazard of the subject in one sentence — automation "adds a second set of
  things that can go wrong: the system itself" — states the dependency chain
  between stages, and separates, in its own scope note, what the market is
  doing from what the system is doing. The lesson pages repeat that
  separation in every hero card.
- **The market-data lab is a complete argument in one select.** Each of the
  five defects is injected at a known bar of a known series, and its reading
  says exactly what a chart can and cannot show about it: a late event
  changes nothing on the line and everything for a state machine; a duplicate
  reads as a pause; a swap reads as a bounce that never traded; a stale print
  understates a 0.92-point range to zero. All six readings were re-verified
  against `makeMarket('breakout',105,121)` (closes 97.54 → 97.51 → 96.83 at
  bars 23–25, the 95.13–100.81 band, the last close below it at bar 46, the
  104.66–110.74 band from bar 60, 110.39 at the end) and stand.
- **The AI lab draws the boundary in the right place.** Confidence gates
  whether a proposal exists (≥ 65%) and is never read again; freshness,
  evidence and unsupported-detail risk decide whether it may be acted on;
  the mode decides only what happens to a validated proposal. Its market
  reading refuses to let the chart vote: "A blocked proposal is the guardrail
  working, not a market call being overruled."
- **Misconceptions are named.** Every common-mistakes card names the
  predictable wrong model — a scheduled script called a system, a timeout
  treated as a rejection, an HTTP 200 treated as a fill, a new ID on every
  retry, arrival order treated as market order, a weekday check treated as a
  calendar, an entry on every qualifying bar, correlated positions counted
  as independent, paper profit treated as live proof, confidence treated as
  probability of profit, a kill switch that depends on the failing service,
  backtest approval treated as production approval.
- **The references are primary.** FINRA 15-09 and the SEC's own summary of
  Rule 15c3-5 for the regulatory lessons; OpenTelemetry, OWASP, Docker and
  Kubernetes for the engineering ones; a broker's own API pages where the
  subject is an API. No vendor selling execution.

## What the course teaches badly

### A "Bearish" regime that rises, under signals nobody generated

`algorithmic-and-automated-trading-fundamentals`: the regime select offers
"Bearish" and `makeMarket('bear',100,101)` opens at 99.65 and closes at
100.58 — 0.9% higher, with its high at bar 37 and its low at bar 15. The
readings table had noticed (its comment says "NO ENTRY FOR bear … there is no
decline on that chart to read") and the shared `behavior('bear')` had been
hedged to cover it, but the option was still offered under a name it did not
deserve. Worse, the lab's "Signals" were the bars 28, 57 and 79 in every
regime (one, bar 57, in a range); "Risk approved" was signals minus one when
the gate was on; "Orders submitted" under approval was approved minus one;
and the "Data delay" slider changed a label from "Current feed" to "Delayed
feed" and nothing else. The first lab of a course about pipelines was a
pipeline with no input, a gate that blocked a constant, and a control that
did nothing. The bear series is now seed 31 — 100.13 → 88.93, −11.2%, each
third with a lower high and a lower low (100.81 / 98.31 / 92.70; 95.59 /
91.92 / 87.80), largest rally 1.9% — with a reading written from it, and
`behavior('bear')` is a reading again. The proposals come from a rule stated
on the page (a close above the prior 20-bar high proposes a long, below the
prior 20-bar low a short, at least 15 bars apart): bull 5 (bars 22, 37, 73
and 88 long, 57 short — a short inside an uptrend, which the reading now
explains is what a rule that knows nothing about the trend produces), bear
5 shorts (27, 44, 60, 75, 91), range 4, volatile 5. The gate applies two
stated limits — a 3-second feed-age limit, which is what the delay slider
now crosses, and a daily limit of two new positions — and every proposal
carries the reason it was blocked. Under "Approval" the reader approves each
passed proposal with a button, so "Orders submitted" is the count of what
they approved; under "Alert" it is zero, and the worked block says why. The
readings for bull, range and volatile keep their verified structure figures
(121.88 and +22.0%; 98.50–104.60 and 102.89; 2.09-point average range, 4.75
widest, 7.0% setback, 127.02) and lose the sentence about "the three markers
at bars 28, 57 and 79".

### A clock that prints 09:60

`time-sessions-events-and-scheduling`: the event log's times were
`09:${30 + j × frequency}`, so at the default five-minute interval the
seventh row read "09:60", at ten minutes the rows ran 09:60, 09:70, 09:80,
09:90, and at fifteen "09:120". A lesson whose subject is the clock printed
minutes past sixty. The same lab's log recorded the planned time and never
the actual one, though concept card 3 asks for "planned run, actual run,
skipped run, lateness"; its "Late" KPI counted every job as late once the
delay slider passed 3 minutes and then ran them all anyway, against practical
rule 2 ("Define maximum signal and job age") and quiz question 2; and the
objective's first two words — "exchange calendars" — had no control at all,
so "Ignoring early closes and daylight-saving changes" was a common mistake
the lab could not show. The clock is now explicit (one bar is five minutes,
bar 0 is 08:30 New York, the open is bar 12, a 14:00 release is bar 66) and
formatted; jobs are planned across the extended day (109 at five minutes)
and the log prints planned time, actual time and lateness per row; a job
later than the stated 3-minute maximum age is skipped and re-evaluated, not
replayed; and a calendar select adds an early close (session 09:30–13:00:
43 run instead of 72) and an exchange holiday (0 run, and the market reading
says whatever the chart shows is yesterday). The worked block prints the
arithmetic ("08:30 + 12 × 5 min = 09:30"; "skipped 37: 31 outside the
session, 6 inside the 13:45–14:15 blackout") and ends with the one
time-zone fact the drill measures: 13:30 UTC is 09:30 in New York in summer
and 08:30 in winter.

### A time-sliced order that ignores the thirty-six bars it works through

`order-management-and-execution`: every policy's average fill was the
decision price times a formula. The time-sliced policy reported 3.9 bps of
slippage on the bull sample while the price rose 409 bps (110.23 → 114.74)
across the window it was slicing through; the range reading had been written
to admit it ("the same average fill is reported whether the marked window
rose or fell") and the bull reading to say the fill "is not read off that
path". A lesson whose objective is to "measure fill quality against the
decision price" measured a formula against itself. The path now prices the
policies that live on it: eight time-sliced children fill at the closes of
bars 46, 51, …, 81 plus a stated half-spread and child impact, and a
participation order takes at most the 900 shares at the touch per bar until
done or an 8-bar deadline. Checked by execution: time-sliced +286.3 bps in
the bull sample (children averaging 113.35), −96.0 in the range, −44.9 in
the bear; participation +116.5, +72.7 and +89.3 (three bars in each, and in
the bear sample the three bars after the decision rise before the decline);
market 5.7 bps everywhere, because it never sees the path; limit −1.5 bps on
the 43% (bull) or 90% (range, bear) that fills. A "Time to complete" KPI
replaces the "Spread" KPI, which restated a slider, the worked block prints
each policy's arithmetic, and all three readings are rewritten from the new
figures — the bear reading now says in words that the resting limit fills and
is then carried lower, which is the adverse selection the path still does
not charge for.

### Two latencies for one incident

`observability-logging-and-auditability`: the chart drew end-to-end latency
at 80–115 ms and added 220 ms during the incident window, so the line read
about 320 ms; the trace waterfall under it printed spans of 36, 30, 90, 33
and 45 ms — 234 ms in total, 180 at baseline. Two figures for one quantity
on a page whose subject is telemetry that explains itself, and a second line
(errors per minute, scaled × 8) on the same axis with no legend. The chart and
the waterfall are now one model: five stage times that sum to the 99 ms
baseline (20 + 17 + 20 + 18 + 24), the incident's milliseconds added to one
stage, and the line drawn from that sum plus noise. Checked by execution: the
latency incident's trace sums to 319 ms and the line averages 322 ms inside
the window against 98 outside; the data incident 149 against 152; the broker
incident 219 against 222. The badge names both lines and their scale, and
the worked block prints the sum, the difference, and what the detection and
uncorrelated-event figures are made of (6 + 7 + 4).

### A readiness gate that opens at 87.5%

`automated-trading-system-specification-and-production-readiness`: eight
checks, `Math.round(passed / 8 × 100)`, and "Ready for limited rollout" when
that was ≥ 88 — so 7 of 8 (87.5, rounding to 88) printed "Ready for limited
rollout" beside "Independent risk: requires action", and did so with
automation set to "Automatic", the case the hero exists to forbid. The export
exported regardless. The `ai` section wrote `mode: "direct"` with
`directExecution: false` — the course home says those two fields exist "because
'an AI is involved' and 'an AI can place an order' are different claims and
the specification is not allowed to blur them", and the builder blurred them.
The home also says lesson 16 "takes the identity and version you gave the
system"; there was no name or version control, and `killSwitch` and
`shadowMode` were constants while lessons 13 and 09 are about them. Readiness
is now a gate: ten checks (kill switch tested and shadow mode run added),
"Ready" only when every one is met, and "Not ready · N" otherwise, with the
worked block saying that 9 of 10 "is a system with one hole, and the hole is
where the loss comes from". Name and version are inputs; `killSwitch` and
`shadowMode` come from controls; `directExecution` is `mode === 'direct'`.
Export is refused while the system has no name or version, and while
automatic execution is requested without any of the five controls it requires
(independent risk, 20 days of paper evidence, idempotent orders, a tested kill
switch, an AI kept off the broker), and the button says which. Alert-only and
approval systems still export unfinished, because a document can record an
unfinished system honestly when nothing in it can submit an order. Validated
after the change: 1,505 exports (the defaults, each slider's extremes, and
1,500 random combinations of every control including empty and blank names
and versions) against the published schema with Draft 2020-12 semantics —
676 exportable and valid, 829 blocked and (for want of a name or version)
invalid, 0 exportable and invalid; and in no export did `ai.mode` and
`ai.directExecution` disagree.

### A crash that cannot duplicate, and a reconciliation that says MATCH over two orders

`reliability-idempotency-retries-and-recovery`: with idempotency off, a
timeout produced `retries − 1` duplicates, duplicate delivery produced
`retries`, and a crash after send produced zero — though "Restarting without
checking open external orders" is the lesson's own common mistake. None of
the three arithmetics was explained, and with two duplicate orders on the
page the reconcile row still read "Query broker by client order ID … MATCH".
The three failures now have three stated arithmetics: a timeout after send
means the broker probably has attempt one, so each of R retries with a fresh
identity is a new order (R duplicates); duplicate delivery is the transport's
doing — one attempt, delivered twice, one duplicate, and retries do not enter
into it; a crash is recovered from the durable intent, which has no broker ID,
so the restart sends once more (two attempts, one duplicate). With the same
key all three collapse to one order. Reconciliation with duplicates present
now lists open orders, finds N for one intent, and reports "REPAIRED" with the
caveat that a filled duplicate cannot be un-filled; with reconciliation off
the KPI says "undetected".

### A late event that arrives and does nothing

`signal-engine-and-strategy-state`: the "Late-event policy" control, set to
Accept, drew a marker labelled LATE at bar 43 and a log row reading APPLY, and
changed no state — the lab promised "contradictory signals" and produced a
decoration. The threshold, 101.5, sat inside the 97.95–102.30 band the first
forty bars held, so the "breakout" entry fired at bar 4 of a forty-bar range
and was stopped out at bar 7; the reading had been written to admit that too.
The EXIT PENDING and COOLDOWN pills were never active. The threshold is now
102.30, the top of the band, and the engine's transitions are entries at bars
48, 69 and 98 (two closes above the level each time) and exits at 61 and 89
(closes of 101.45 and 101.46 against a 101.50 level): five transitions, each
with a reason code. The late event is a real record: bar 45's close (100.99,
below the exit level) arriving at bar 50. Rejected, its event time is compared
with the last transition and it is logged as LATE_REJECTED; accepted, it is
applied as an exit the market did not produce, the cooldown holds until 58,
and the engine re-enters — seven transitions, two of them contradictory,
which the worked block says in words: "The same inputs in a different order
gave a different position." The stateless setting emits 33 entries, 32 of
them duplicates. The final-state pill can now be COOLDOWN (at a 20-event
cooldown it is), and the reading is rewritten from the new run.

### Rejections without reasons and an engine that cannot resize

`portfolio-position-and-risk-engine`: concept card 3 and quiz question 3 say
the engine returns "approve, resize, or reject"; the lab could only accept or
reject, the table said "REJECT" and not why, and the correlation rule — the
first three names are one group — was visible nowhere. Each row now carries
its group, its risk per share, the shares proposed and taken, and the limit
that bound it: at the defaults TECH-A accepted ($500 ÷ $4.00 = 125 shares,
$14,750), TECH-B and INDEX rejected ("correlation: equity beta already held
via TECH-A"), ENERGY accepted, and BANK resized from 333 to 224 shares
because $8,750 of room under the $35,000 cap divided by $39 is 224. Gross
exposure 70.0%, open risk $1,336 (2.67%), and the cap is drawn as a dashed
line on the chart. With the correlation limit ignored the equity-beta names
are three independent positions and the worked block says that is "how
apparent diversification disappears in the same market event".

### A partial fill that changed a percentage

`broker-apis-and-order-lifecycle`: quiz question 3 says a partial fill
updates "filled quantity, remaining quantity, cash, and position"; the lab
printed "Filled quantity 55%". A ledger now prints all four at every step —
55 × $108.53 = $5,968.92 of cash consumed, 45 open, position 55 — and the
prices are honest about the order type: the limit rests at the submit price
(108.53) and fills only because the market touched 108.31 at bar 44 before
leaving, so the rest stays open at 111.07; the market order takes the first
55 at 108.58 and the rest at 108.64, average 108.60, and completes. The
UNKNOWN state after a timeout now says the one thing the lesson is for: do
not resubmit; query by the client order ID.

### A spread charged at a tenth of a basis point per basis point

`paper-trading-and-forward-testing`: the "Spread" control was labelled in
basis points and charged `spread × 0.00001` — a 5 bps spread cost half a
basis point — on every seventh step, for no stated reason, with a
"Conservative" realism setting worth 1.3 bps. Divergence was 0.58% and
nothing on the page said what it was made of. The model is now stated and
printed: 12 signals in 90 days, the same 12 in all three columns because the
rules are frozen; the backtest charges its own assumed 2 bps a fill; the
paper account charges the half-spread it crosses (2.5 bps) plus 0.5 bps per
second of delay; the shadow estimate adds 0, 5 or 10 bps of queue and impact
the simulator does not see, and 3 bps for partial fills when modelled;
12 × (11 − 2) = 108 bps → 1.07% divergence at the defaults, 2.96% at the
conservative extreme, and −0.18% at the optimistic one — which the worked
block names as a flattering simulator rather than a better strategy.

### "Approved = candidates − stale − 1"

`scanners-alerts-and-human-approval`: the approved count subtracted one for
no stated reason (one candidate, nothing stale, zero approved), duplicates
were always shown though "Deduplicate alerts by setup and state transition"
is the lesson's first practical rule, and the review queue (each later
candidate reviewed two minutes after the previous) was invisible. An "Alert
on" control now chooses between the transition and the condition: the
condition stays true for twenty minutes, a five-minute scan sees it four
times, so 4 × 3 = 12 alerts against 3; the review times are printed per
candidate (4, 6, 8 min against a 10-minute expiry; at a 12-minute delay all
three expire), the unexplained subtraction is gone, and the price at alert
and at review is printed with its change.

### A chart of nothing, and a rotation that was never modelled

`security-secrets-permissions-and-kill-switches`: the chart was a fixed ramp
scaled by the score, with no unit; the score's weights were unstated; the
objective's "rotate secrets" and "audit access" had no control. The chart is
now the blast radius in orders: a scoped key can submit about one unintended
order a minute and a broad one six, until the kill switch stops it — 2
minutes tested, 15 untested, never when there is none — so 2, 12, 90 or 360
orders, printed with the multiplication. A credential-lifetime control adds
rotation (−14 when static) and the worked block prints the deduction
arithmetic ("100 − 45 (credentials in source or files) − 28 (broad account
authority) = 27") with the caveat that the weights are the lab's.

### A loss computed and thrown away

`deployment-environments-and-configuration`: `impact = canary × 1.8` was
computed and never used, "Config drift: Detected late" was a constant, and the
rollback node's title was the raw value `auto`. The lab now states its model
— a bad configuration loses 0.5% of the capital it controls per minute, for
as long as it runs — and prints it: 10% × 0.5%/min × 3 min = 0.15% at the
defaults with drift, 7.00% at full scope with a 14-minute manual rollback,
9.00% when no readiness probe takes the instance out of rotation (four
minutes longer), 35.00% with no rollback over the 70-minute window. A
"Loss before rollback" KPI replaces the constant, and the chart marks the
rollback.

### Smaller repairs

- `trading-system-architecture-and-components`: "Duplicate-order risk: 2
  possible" had no mechanism; it is now 1, and the worked block gives the
  mechanism (intent in memory, restart, the strategy proposes again, the
  order service submits again). In the modular system a data-feed failure
  left the strategy marked ok; it is now marked as waiting in a safe state,
  because containment is not immunity. The latency decomposition is printed
  (112 + 160 = 272 ms, and the penalty is the same in both architectures).
- `market-data-ingestion-and-normalization`: "Detected defects: 8" for four
  injected duplicates, because a duplicate touches two records; the KPI is
  now the injected count and the worked block explains the record count. A
  12-second feed age in the normalized view scored 100% with no consequence,
  against practical rule 3; a 5-second limit now degrades the trading state
  in both views and the reading says a clean stream that is old is still not
  tradable. A dead variable (`lat`) is gone; the duplicate copy is listed
  after its original; the late row prints its lateness (receive − event = 8
  bars).
- `ai-assisted-and-agentic-trading-workflows`: the authority node's title
  was the raw mode value; the check lines now print the figure against the
  limit; a worked block walks the decision in three lines.

### Drills that do not test what the lesson promised

Forty-seven of the course's forty-eight questions had the correct answer as
the first choice. A reader who noticed learned to click the first button; a
reader who did not was still never asked for a number the lesson's own lab
produces. Each lesson gains one question whose answer is a figure the lesson's
formula yields, worked in the feedback and here, and the choices are rotated
so the correct position is 23 / 20 / 21 across the 64 questions:

| lesson | question | answer |
| --- | --- | --- |
| 01 | rule fires 5×, feed 2 s ≤ 3 s, daily limit 2, alert-only | **0 orders**; 2 alerts |
| 02 | 112 ms of hops, broker +160 ms during a timeout, modular | **272 ms**; only the order service degraded |
| 03 | event 10:15:02.000, received 10:15:09.500, limit 5 s | **7.5 s late**; keep by event time, flag, degrade |
| 04 | open 09:30 NY scheduled at 13:30 UTC year-round, in November | **08:30**, an hour early (EST is UTC−5) |
| 05 | condition true on 12 consecutive events | stateless **12**, stateful **1** |
| 06 | $50,000 × 1%, entry $118, stop $114 | $500 ÷ $4 = **125 shares**, $14,750 |
| 07 | 100-share limit at $108.53, 55 filled | cash **−$5,968.92**, 45 open, position 55 |
| 08 | decision $110.23, children average $113.38 | **286 bps** |
| 09 | 12 signals, backtest 2 bps, shadow 11 bps | 12 × 9 = **108 bps** ≈ 1.1% |
| 10 | true for 20 min, 5-min scan, 3 candidates | **12** on the condition, **3** on the transition |
| 11 | timeout after send, 3 retries with new IDs | **up to 4** orders |
| 12 | spans 20, 17, 240, 18, 24 ms | **319 ms**; open the strategy span |
| 13 | 6 orders/min, untested switch, 15 min | **90** orders |
| 14 | canary 10%, 0.5%/min, rollback 3 min | **0.15%** of the account |
| 15 | confidence 95%, source 12 min > 5, guardrail on, automatic | **Blocked** |
| 16 | 9 of 10 met, independent risk missing, automatic | **Not ready**; export blocked |

The quiz engine showed one explanation per question, so the reader who
picked "Guaranteed profitability" and the one who picked "Knowledge of
future prices" were told the same thing. The engine now accepts a `data-why`
on each choice and, on a wrong pick, prefixes the feedback with that choice's
own correction; every distractor on every page has one (64 questions, 128
distractors, checked by parse, no correct choice carries one).

### No lab showed its arithmetic being done

Only the risk lab printed a table a reader could check by hand, and it
omitted the division. Every lab now prints a worked block under its chart —
the rule, the gate and the level (01); the latency sum and the duplicate
mechanism (02); the record counts and the freshness comparison (03); the
clock arithmetic and the skip breakdown (04); the confirmation closes, the
cooldown subtraction and the late event's two timestamps (05); the sizing
division and the room under the cap (06); the fill products (07); each
policy's fill arithmetic (08); the per-fill costs and their sum (09); the
scan count and the review queue (10); the attempt and delivery counts (11);
the trace sum against the metric (12); the deductions and the blast-radius
product (13); share × rate × minutes (14); the three-line decision (15); the
gate and the export verdict (16) — so the progression is worked example (the
lab), faded (the reading, which quotes the figures), independent (the quiz).

### Two shared blocks, one of them hedged

Seven pages carried the readings machinery and nine did not, and the nine's
`marketRead` took three arguments. All sixteen now carry the same shared
block (one hash, with the readings literal excluded), `participationHTML`
and the four-argument `marketRead` on every page, a `workedHTML` helper, the
course-7 quiz engine, and an unhedged `behavior('bear')`. Pages whose price
line is scenery — a failure marker over a volatile sample, a range under four
pipeline stages — carry an empty readings table on purpose, and the block's
comment says why.

## What it claims to teach but does not

- `algorithmic-and-automated-trading-fundamentals` promised signals, a gate
  and a delay and had placed markers, a subtraction and a label. Fixed as
  above.
- `time-sessions-events-and-scheduling` names exchange calendars and
  daylight-saving in its objective and its common mistakes and had neither.
  Fixed as above.
- `signal-engine-and-strategy-state` promised contradictory signals from
  stale events and applied none. Fixed as above.
- `portfolio-position-and-risk-engine` names "resize" and had no resize.
  Fixed as above.
- `order-management-and-execution` promises fill quality against the
  decision price and available liquidity; the fills did not depend on the
  path. Fixed as above.
- `security-secrets-permissions-and-kill-switches` names rotation and audit
  and had no control for either. Rotation is added; "audit access" is a
  clause in the rotation check line and no more. Left, and recorded here: an
  access-audit control would be a checkbox with no arithmetic behind it.
- `automated-trading-system-specification-and-production-readiness` promised
  an identity you gave it and a readiness gate; it had constants and a
  score. Fixed as above.
- `trading-system-architecture-and-components`'s objective is to "define the
  services, boundaries, data stores, messages, and ownership"; the lab shows
  an architecture and lets the reader break it, but does not let them draw
  one. Left: a boundary-drawing tool is a different lab, and the lesson's
  own process card ("Map, Assign, Contain") is the drill for that objective.
- `observability-logging-and-auditability`'s objective lists "positions,
  risk" among the things to measure; the lab measures latency and errors.
  Left: the domain metrics are named in the check lines, and adding a
  position gauge to a lab about traces would put a sixth thing on the page.
- `ai-assisted-and-agentic-trading-workflows` names research, extraction and
  classification as advisory tasks; the lab models one proposal. Left: the
  boundary is the same for all four, and the proposal is the one that
  reaches the broker.

## Where a learner gets stuck

- **Lesson 01, "Bearish"**: the chart rises. Fixed.
- **Lesson 01, the delay slider**: nothing changes but a label. Fixed.
- **Lesson 04, the log**: "09:60". Fixed.
- **Lesson 04, "Late: 23"**: every job is late and every job ran. Fixed.
- **Lesson 05, "Accept" the late event**: a marker appears and the state
  does not move. Fixed.
- **Lesson 06, "REJECT"**: five rows, three rejections, no reason. Fixed.
- **Lesson 08, "Time-sliced"**: 3.9 bps of slippage through a 4% move. Fixed.
- **Lesson 11, "Crash after send", idempotency off**: 0 duplicates. Fixed.
- **Lesson 12, the waterfall**: 234 ms under a chart reading 320. Fixed.
- **Lesson 16, risk bypassed, automatic**: "Ready for limited rollout".
  Fixed.
- **Every quiz**: the first answer. Fixed.

## Structural changes considered

None made. Each lesson carries one hard idea, and the three lessons whose
titles list four things (04, 11, 13) are one idea each under four names —
the clock the system must not assume, the command that may arrive more than
once, the credential that is authority. The order is the dependency order the
home states, and the one forward reference (04 → 11) is now glossed rather
than reordered, because the scheduler's identifier is where a reader first
needs the word. No URL is added, removed or renamed; the five declarations
are untouched; no CSS was added, so the last-`</style>` landmine was never in
play.

## Verification performed

- Every lab's arithmetic executed from the shipped script in a stub DOM,
  before and after, for every control position that changes a verdict: the
  pipeline under four regimes, three levels, feed ages 0–8 and both gate
  states, with the approval buttons clicked; the architecture under both
  designs, four failures and both stores; the data lab's six defects at
  counts 1–5, both views and feed ages to 12; the scheduler at 1, 3, 5, 10 and
  15 minutes, delays 0–10, both sessions, three calendar days and both
  blackout states; the signal engine stateful and stateless, confirmation
  1–3, cooldown 0–20 and both late-event policies; the risk gate at four
  account sizes, risk 0.25–3%, caps 70 and 120% and both correlation states;
  the lifecycle stepped through every state under both order types and three
  network results, plus reconcile; execution for all twelve policy/regime
  pairs at 200, 2,000 and 8,000 shares; the paper lab at the defaults and
  both extremes; the scanner at five intervals, three thresholds, both alert
  modes and delays 0–25; reliability for all sixteen failure/idempotency/
  reconciliation states at 0–5 retries; observability under four incidents
  and every telemetry toggle; security across every control; deployment with
  and without drift at 10 and 100% scope, three rollbacks and both probe
  states; the AI lab at four confidence/freshness pairs, both guardrail
  states and three modes; the builder at the defaults, each slider's extremes
  and 1,500 random combinations including empty identities.
- 1,505 specification exports validated against the published schema: 0
  exportable and invalid, before and after; `ai.mode` and `ai.directExecution`
  never disagree after (they did before).
- Every quiz answer index checked against its choices after the rewrite;
  every distractor carries a `why`; no correct choice does; positions
  23 / 20 / 21; every worked answer recomputed by hand in this document.
- The sixteen shared script blocks are identical with the readings literal
  excluded (one md5); the last `</style>` on every page is still the
  `<noscript>` one.
- `scripts/add_progress_marks.py` re-run: 129 visited, 0 rewritten.
- The gates in AGENTS.md §7–8 and the CI steps run locally, listed in the
  commit message. `labcheck.js` on the sixteen course-8 pages fails in the
  shim's documented gap (`querySelector` returns null for the theme toggle),
  exactly as it does on an untouched course-7 page; the stub DOM used for
  this assessment executes every one of them.
