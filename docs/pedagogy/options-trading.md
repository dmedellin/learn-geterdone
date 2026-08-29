# Pedagogy assessment — Options Trading (trading, course 3)

First-pass assessment, formed from the sixteen lessons, the course home and
the published schema as they stand on `main` at 817211c. There is no prior
assessment of this course, so there is no delta section.

Course home: `site/options-trading/index.html`. Lessons, in course order:
`options-contract-fundamentals`, `calls-and-puts`, `moneyness`,
`option-premium`, `option-chain-and-liquidity`, `expiration-and-time-decay`,
`implied-volatility`, `delta-and-gamma`, `theta-and-vega`,
`long-calls-and-long-puts`, `covered-calls`, `cash-secured-puts`,
`vertical-debit-spreads`, `vertical-credit-spreads`,
`exercise-assignment-and-expiration`, `options-trade-planning`. The published
asset `options-trade-plan-schema.json` is the export shape lesson 16 claims.

Courses 1 and 2 are the declared prerequisites and are assumed: a thesis with
a direction, a target and an invalidation level (course 2, `trade-thesis`), a
risk budget as a percentage of equity and "R" as the unit of planned risk
(course 2, `position-sizing`, `risk-to-reward`; course 1,
`invalidation-stops-risk-reward`), and one preview of the whole instrument in
course 1's `options-contract-selection`, which now has a terms card so the
vocabulary here has been seen once.

Every lesson ships one shared JavaScript prelude — a Black–Scholes core
(`optionModel`, with `r` fixed at 4.5% and no dividend), a payoff drawer, a
segment control and a quiz engine — then its own lab and drill. The static
HTML of every readout is also shipped, and script overwrites it on load. Those
statics are where much of what follows was found, because they are what a
reader without script sees and what the noscript note promises "still read
normally".

## What the course teaches well

- **The order is the order the idea has to be built in, and the home says
  why.** Contract (01) → the four positions' payoffs (02) → moneyness (03) →
  the premium split into intrinsic and extrinsic (04) → the chain it is quoted
  on (05) → the clock (06) → volatility (07) → the numbers on both (08–09) →
  five positions built from the parts (10–14) → what settles it (15) → the
  plan (16). "How to work through it" names the real dependencies — the
  Greeks only mean something after 04 has split the premium; 16 asks for a
  spread cost, a budget and an exit rule the earlier lessons produce — and
  they are true.
- **"What this is normally read as" is on every lab that draws a shape**, and
  it is honest about what a synthetic payoff can carry: the one participation
  fact an option chart genuinely has is the counterparty, and the blocks say
  so ("every contract exists because two sides agreed a premium for an
  obligation"). The decay and theta/vega blocks open by stating that nothing
  on the chart is directional. In `implied-volatility` the block is keyed to
  the measured relation between the two IV inputs, not to the preset button,
  so it stays true after the reader edits the fields.
- **The strategy lessons ask the same four questions of every structure**
  (cost, breakeven, most it can make, most it can lose) and the live
  arithmetic is right: covered call $1,050 / $97.50 / $1,050 at $112;
  cash-secured put $9,500 reserved / $92.75 / $225 / −$275 at $90; debit
  spread $350 / $650 / $103.50 / +$450 at $108; credit spread $250 / $750 /
  $97.50 / +$250 at $103; the fundamentals decoder +$600 / $104.00; the
  expiration simulator +$300 and $10,000 at strike. All recomputed.
- **The Greeks lessons make the reader watch a linear estimate fail.**
  `delta-and-gamma` prints delta-only, delta-plus-gamma and full repricing
  side by side; `theta-and-vega` prints the theta × days and vega × points
  attribution against the repriced change and names the residual. The
  misconception "Greeks are P/L" is experienced rather than described.
- **The common-mistakes cards are specific and in the author's voice**:
  "treating the quoted premium as the total contract cost" (01); "being ITM
  does not mean profitable" (02, 03); "calling all premium time value" (04);
  "buying the cheapest premium" (05); "assuming decay is linear" (06);
  "treating high IV as a directional forecast" (07); "delta as a
  probability" (08); "IV change as a decimal with quoted vega" (09); "buying
  far OTM because it is cheap" (10); "calling a covered call downside
  protection" (11); "premium as free income" (12); "the short strike beyond a
  realistic target" (13); "focusing only on probability of profit" (14); "an
  OTM option can never be exercised" (15); "starting with a chain instead of
  a thesis" (16).
- **Lesson 16's third preset is a deliberately bad plan** and the checks
  reject it (45/100): 7 DTE against an 8-day thesis, a 29% spread, $1,100 at
  risk against a $250 budget, long premium held through a high-IV event, no
  exit rule. Its reading block is keyed to the strategy rather than the
  preset so the page never reads an endorsement onto a plan it is teaching
  the reader to throw away.
- **Lesson 15 models the shares-owned dimension**, so "uncovered assignment"
  is a concrete outcome (short stock, or a purchase the account may not
  cover) rather than a warning.

## What it teaches badly, or claims and does not deliver

### Numbers a reader will trust

1. **Every static readout in lessons 04–10 disagrees with the model the page
   ships.** Recomputed from the shipped `optionModel` at each lesson's
   defaults:
   - `option-premium` (100 / 105 call, 30 DTE, IV 30%): page says $2.30
     premium; model $1.67.
   - `option-chain-and-liquidity` (100 call, 30 DTE): page says $3.80 / $4.00,
     5.1% spread, $400 entry, $20 friction, limit 3.90; the chain generator
     produces $3.31 / $3.46, 4.4%, $346, $15, limit 3.38.
   - `expiration-and-time-decay` (100 / 100 call, 45 DTE, IV 30%): page says
     $4.38 now, $4.32 tomorrow, theta −$0.06; model $4.47, $4.42, −0.053.
   - `implied-volatility` (event preset, 60% → 30%, $100 → $104): page says
     $7.05 → $5.18, −$187; model $7.03 → $6.10, −$92. The claim the lesson
     rests on — right direction, still a loss — holds; the number does not.
   - `delta-and-gamma` (100 / 100 call, 30 DTE, IV 30%, +$5): page says delta
     0.52, gamma 0.046, delta after 0.72, +$320, and "delta-only +$260;
     delta-plus-gamma +$318; full model +$320"; model 0.534, 0.0462, 0.743,
     +$322, and +$267 / +$325 / +$322.
   - `theta-and-vega` (45 DTE, IV 35%, 5 days, −10 points): page says vega
     0.11, actual −$140, estimate −$140; model 0.139, −$162, −$169.
   - `long-calls-and-long-puts` (exit $108, 20 DTE, IV 30%): page says exit
     value $9.12 and +$462; model $8.72 and +$422.
   - `options-contract-fundamentals`: the static badge says ATM for a 100 call
     with the stock at $110.
   The same drift course 1's `options-contract-selection` had, from the same
   cause: the statics were written by hand and never checked against the
   code. Script overwrites all of them on load, but the noscript note on every
   page says the written panels still read normally, and a reader who checks
   the page against Cboe's calculator — which the course home tells them to
   do — finds the page wrong.
2. **The course has two definitions of at-the-money and they contradict each
   other on the next page.** `moneyness` labels the *nearest listed strike*
   ATM: with the stock at $102 the 100 strike reads "ATM" with call intrinsic
   $2.00, and the rule text under it says "Closest listed strike". The shared
   helper `moneyness()` used by 01, 05 and 15 calls a strike ATM only within
   0.5% of the stock, so the same 100 strike at $102 is ITM one lesson later
   in the chain. `option-premium`'s drill then marks "ATM and OTM options
   have zero intrinsic value" correct. A reader who took lesson 03 at its
   word has just seen an ATM option with $2.00 of intrinsic value.
3. **Lesson 16's export does not satisfy the schema the course publishes.**
   `options-trade-plan-schema.json` requires `schemaVersion`, `thesis`,
   `contract`, `risk`, `management` and `evaluation.decision` (an enum of
   `approved` / `revise` / `reject`). The page exports `schema`, `inputs`,
   `metrics` and `evaluation.grade`. Every file lesson 16 has ever produced
   fails the document the course home calls "the contract for that shape"
   and invites the reader to build a spreadsheet against. The home also says
   the plan is scored "across seven checks"; the page runs ten.
4. **Lesson 16's risk-budget check makes the two share-backed strategies
   impossible to plan.** For a covered call it compares the stock-to-zero
   loss (basis − premium, ×100) with the budget, so a 100-share covered call
   at $100 needs $9,750 of budget — 1% of $975,000. Course 2 defined planned
   risk as the loss if the invalidation is hit (`position-sizing`), and
   lesson 16's own reading says "the red invalidation line rather than the
   premium is what defines where the downside thesis has failed". The check
   does not use the line the lesson draws. A reader who arrives from lesson
   11 selects "Covered call" and is told the plan fails at any size.
5. **`vertical-credit-spreads` mislabels the maximum loss for most premium
   pairs.** The status compares `pnl <= -maxLoss` with floating-point
   arithmetic; for short 1.05 / long 0.20 it computes −914.9999… against −915
   and prints "Partial outcome" — with the "partial" reading block — at the
   maximum loss. 1,647 of the 5,900 premium pairs probed at 5-cent steps
   fail the same way.
6. **The model's rate is never stated.** Every page says "fixed rate
   assumptions"; the code fixes `r` at 4.5%. A reader reproducing a number
   with the calculator the home recommends cannot match it.

### Prerequisite order inside the course

7. **Implied volatility is a slider three lessons before it is defined.**
   `option-premium` asks the reader to move "Implied volatility" from 10% to
   100% and its hero says the lesson shows how IV affects the estimate; IV is
   introduced in `implied-volatility` (07). Nothing on 04 says what the
   number is.
8. **Delta and IV are columns four lessons early.** `option-chain-and-liquidity`
   shows Delta and IV in every row, and its process card says "use moneyness
   and Greeks to match the intended directional sensitivity"; the Greeks are
   08–09. `moneyness`'s hero illustration also carries a delta column.
9. **`long-calls-and-long-puts` asks for an exit IV without giving the entry
   IV.** The entry premium is typed ($4.50) and the exit IV is a number (30%);
   the reader cannot tell whether that is a contraction or an expansion.
   (Backed out of the model, $4.50 at 45 DTE is 30.2%, so the default exit
   is "unchanged" — which nothing says.)
10. **`implied-volatility`'s "rough expected move" is a one-standard-deviation
    figure** and the page never says so; a reader takes ±$17.20 as a range
    the stock stays inside.

### Objectives half-stated, or stated once for sixteen lessons

11. **The completion standard is the same sentence on all sixteen pages**
    ("State the contract, premium, breakeven, maximum risk, time exposure,
    volatility exposure, assignment exposure, and exit condition"). On
    `moneyness` there is no premium; on `option-chain-and-liquidity` no
    breakeven; on `options-trade-planning` the act is scoring a plan. The
    "Core concepts" subtitle and the lab header are likewise identical on
    every page ("Change the inputs and inspect how the contract, value,
    payoff, or obligation changes" on a moneyness ladder and on a plan
    scorer). Course 2 had the same defect and fixed it.
12. **Three heroes state no act**: `options-contract-fundamentals` ("Learn the
    underlying…"), `expiration-and-time-decay` ("Observe how… and understand
    why theta is not constant").
13. The course home's "What it teaches" is a table of contents.

### Retrieval practice and feedback

14. **Every drill gives the same feedback for every wrong answer.** The shared
    engine renders `item.explanation` whatever was chosen, so a reader who
    answers "$32.50" to the multiplier question (01) — the specific error of
    multiplying by 10 — reads the rule for the reader who answered "$3.25".
    Courses 1 and 2 have both been repaired for this; course 3 has the same
    engine unrepaired.
15. **Filler distractors that diagnose nothing.** "Only for calls", "Only at
    expiration", "Only for puts", "Only at 30 DTE", "Only on expiration
    morning", "Only after assignment", "Only when deep ITM" appear as the
    wrong answers on `moneyness`, `option-chain-and-liquidity`,
    `expiration-and-time-decay`, `implied-volatility`, `delta-and-gamma` and
    `exercise-assignment-and-expiration`. They are not things anyone believes,
    so choosing the right answer requires no understanding and choosing a
    wrong one reveals none.
16. **Objectives the drills do not measure.** Position delta with the
    multiplier (08, concept card 2 and process card 2; never asked). The
    downside of a covered call (11, the lesson's own common mistake 2; never
    asked). The stock-to-zero loss of a cash-secured put (12). The breakeven
    of either spread (13, 14 — each lesson lists it first). The split-leg
    expiration risk (15, common mistake 3). The round-trip cost of the spread
    (05 — the course home's stage 1 copy promises "the bid-ask spread you
    pay on the way in and again on the way out" and the lesson never says
    it). The decomposition of an ITM premium (04 — the drill only asks the
    OTM case).
17. **`option-chain-and-liquidity`'s evaluator is pre-answered and fights the
    reader.** `renderChain` writes the mid price into the limit field on every
    render, so "Evaluate selection" passes 4/4 on the default row without a
    decision, and a limit the reader typed is wiped the moment the stock
    slider moves.
18. **No lesson shows a worked example.** Each lab opens on a default state
    and a readout, and the drill then asks for arithmetic the page has
    demonstrated nowhere in prose: `calls-and-puts` asks for a breakeven,
    `delta-and-gamma` for a delta-dollar estimate, `theta-and-vega` for
    vega × points, the spread lessons for width − debit. The readouts state
    results; nothing states the working.

### Misconceptions the course is silent on

19. **"A vertical spread is worth its maximum as soon as the stock passes the
    short strike."** Both spread lessons draw expiration payoffs only and
    neither says that before expiration the short leg still has extrinsic
    value, so a spread that is fully in the money weeks early shows well
    under its width. This is the most common surprise a first spread
    produces.
20. **Theta per share versus per contract.** `theta-and-vega` names the vega
    unit trap; `expiration-and-time-decay` prints theta per share and says
    nothing about the ×100 a position statement will show.

### Load and structure

21. Cognitive load is acceptable throughout: one new hard idea per lesson,
    with 15 carrying four operational dimensions (side, type, style, shares
    owned) that are all mechanical. No split or merge is warranted, and the
    URL space should not change.

## Where a learner gets stuck

- **On `moneyness` with the slider at $102**, reading "ATM" over a $2.00
  intrinsic value, then on `option-premium`'s drill being told ATM options
  have none (item 2).
- **On `option-premium`'s IV slider**, with no idea what the number is
  (item 7).
- **On `option-chain-and-liquidity`**, pressing Evaluate before deciding
  anything and passing; then typing a limit and watching it vanish (item 17).
- **On `long-calls-and-long-puts`**, setting an exit IV with nothing to
  compare it to (item 9).
- **On `vertical-credit-spreads`**, entering premiums like 1.05 / 0.20,
  sliding to the long strike and reading "Partial outcome" at the maximum
  loss (item 5).
- **On `options-trade-planning`**, choosing the covered call from lesson 11
  and failing the budget check at every size (item 4); then downloading the
  plan, opening the schema beside it and finding no field in common (item 3).
- **On any drill**, choosing the specific wrong answer and being told the
  rule (item 14).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, split, merged
or renamed, so the five URL declarations are untouched. The published schema
is edited in place (optional fields added; the required shape and the
`options-trade-plan-v1` const are unchanged).

- **Shared quiz engine (all sixteen pages, one identical edit):** a choice may
  be an object with a `why`; when a wrong answer is chosen its own `why` is
  shown, falling back to the question's explanation. Every distractor on every
  page now carries one, written against the error that distractor is. Filler
  distractors replaced with misconceptions; the untested objectives in item 16
  each gain a question (position delta, covered-call downside, cash-secured
  put maximum loss, both spread breakevens, split-leg expiration, round-trip
  spread cost, ITM premium decomposition, and the plan's risk figure).
- **Static readouts recomputed from the shipped model** on 01, 04, 05, 06,
  07, 08, 09 and 10 (the figures in item 1), so the page without script
  agrees with the page with it.
- **Model scope note on all sixteen pages** states the fixed 4.5% annual
  rate and no dividend.
- `moneyness`: the ladder's badge now uses the same 0.5% tolerance as the
  rest of the course; the nearest strike carries a separate "nearest" mark;
  the concept card and side-panel copy explain that "ATM" by convention names
  the nearest strike, which can carry a little intrinsic value, while ATM in
  the strict sense means stock equal to strike.
- `option-premium`: implied volatility glossed at the slider and in the
  concept card, with a pointer to lesson 07; a worked decomposition of the
  108 / 100 call from the model ($9.20 = $8.00 + $1.20).
- `option-chain-and-liquidity`: delta and IV columns glossed as context for
  lessons 07–08; the process card no longer asks for Greeks; the limit field
  is filled only when the selected strike changes, so a typed limit survives;
  the evaluator reports the round trip at the market and what a mid-price
  limit saves; a worked reading of the default row.
- `expiration-and-time-decay`: hero restated as an act; theta per contract
  glossed; the ×100 trap added to common mistakes.
- `implied-volatility`: expected move defined as one standard deviation under
  the model.
- `delta-and-gamma` and `theta-and-vega`: worked attribution cards using the
  defaults (+$267 / +$325 / +$322; −$30 − $139 = −$169 against −$162).
- `long-calls-and-long-puts`: the entry IV backed out of the entry premium
  and shown beside the exit IV, so the reader can see whether the exit is a
  contraction; the status names the relation.
- `vertical-debit-spreads`, `vertical-credit-spreads`: the pre-expiration
  misconception added to common mistakes; worked spread arithmetic from the
  default legs; the credit-spread outcome test uses a one-cent tolerance.
- `exercise-assignment-and-expiration`: a split-leg question.
- `options-trade-planning`: the export now matches the schema
  (`schemaVersion`, `thesis`, `contract`, `risk`, `management`,
  `evaluation.decision` with `checks`); the risk-budget check uses the loss
  at the invalidation level for covered calls and cash-secured puts and says
  so, with the stock-to-zero figure reported separately; "loss at
  invalidation" and "target R" added to the readout; the grade vocabulary
  matches the decision enum; the schema documents the added optional fields.
- **Completion standard, core-concepts subtitle and lab header on every page**
  rewritten to name what that lesson's lab shows and its drill measures; the
  two heroes in item 12 restated as acts.
- Course home: "What it teaches" rewritten as outcomes; "seven checks"
  corrected to ten.
