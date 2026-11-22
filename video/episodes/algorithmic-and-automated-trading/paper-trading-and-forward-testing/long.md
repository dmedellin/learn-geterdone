---
format: long
lesson: algorithmic-and-automated-trading/paper-trading-and-forward-testing
title: Paper trading and shadow mode: testing live without risking capital
thumb: Paper fills flatter you
---

@chapter The problem
@title text="Paper Trading and Forward Testing" sub="Algorithmic and Automated Trading" art=thumb
Your backtest is done. The obvious next step is to switch the system on with real money. The lesson says don't, not yet. There's a stage in between, and it tests things the backtest never could: the system itself, running on today's market.

@words text="Tests the live workflow · fills still differ"
Paper trading tests the live workflow, but simulated fills still differ from real execution. The market can show sustained buyer control, while the paper account reports fills that would have been slower, partial, or unavailable with real size.

@chapter Three ideas
@list heading="What to understand" items="Forward test@Forward test|Paper environment@Paper environment|Shadow mode@Shadow mode"
Three ideas. Forward test: run fixed rules on new events that weren't available during strategy development. Paper environment: use broker like APIs and simulated order handling, without routing live orders. And shadow mode: calculate live decisions and intended orders, while preventing submission.

@art workflow-end-to-end
So what is paper trading actually good for? Testing the current end to end workflow. The live data, the scheduler, the signals, the orders and the monitoring, all running together now. It can't prove live profitability, and it isn't about historical data quality.

@chapter Why paper is optimistic
@art queue-position
Why can paper fills be optimistic? Because the simulator may not reproduce queue position and market impact. Paper prices are the live prices. What differs is what the simulator assumes about getting filled at them. Real execution depends on available liquidity, the queue, and your order size.

@art shadow-mode
Shadow mode closes part of that gap. It produces decisions and intended orders, without live submission. It touches no account. But it must keep logs, because the intended orders are its whole output. Without them, there's nothing to compare.

@chapter Promote in stages
@list heading="Promote evidence in stages" items="Freeze strategy, parameters, data contract, limits@Freeze|Run: signals, intended orders, fills, telemetry@Run|Compare and explain the differences@Compare"
Don't move straight from historical results to automatic live execution. Freeze: version the strategy, parameters, data contract and risk limits. Run: collect forward signals, intended orders, simulated fills and system telemetry. Compare: explain the differences from the backtest before approving the next validation stage.

@art frozen-rules
Freezing is the part people rush. The version of the strategy that runs on paper must be exactly the one you'd deploy, with the same parameters, the same data contract and the same risk limits. Otherwise the forward test is evidence about a system you're not going to run.

@art stage-ladder
Each stage earns the next. Changing parameters during the same evaluation window is a named mistake, because then you're not testing the frozen system any more. And define measurable promotion criteria in advance, so the decision to move on isn't made by feel.

@chapter The execution gap
@math heading="12 signals · backtest 2 bps per fill · shadow 11 bps per fill" items="gap per fill: 11 − 2 = 9 bps@nine basis points;;12 × 9 = 108 bps@twelve times nine;;≈ 1.1% before compounding@one point one"
Here's the lesson's example. Twelve signals. The backtest assumed two basis points of cost per fill, and the shadow estimate is eleven. The gap per fill is eleven minus two, nine basis points. Twelve times nine is a hundred and eight basis points, about one point one percent, before compounding.

@art fill-gap
A hundred and thirty two charges the shadow's full eleven twelve times, but the backtest already counted two. Nine is the gap on one fill, and there are twelve. And every basis point of that gap should have a named cause before the next stage.

@chapter Where people slip
@list heading="Common mistakes" items="Treating paper profit as live proof@The first|Changing parameters mid-window@The second|Skipping shadow mode for a new broker@And the third"
The first mistake is treating paper profit as live proof. The second is changing parameters during the same evaluation window. And the third is skipping shadow mode for a new broker or a new deployment. Freeze the rules before a forward test, and record intended orders even when submission is disabled.

@chapter Try it
@words text="Latency · fill realism · spread · partial fills"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the latency, fill realism, spread and partial fill assumptions. Then compare the historical, paper and live like shadow results, and try to name the cause of each difference.

@end text="Compare backtest, paper and shadow"
You can compare backtest, paper and shadow results side by side, on Learn. That's learn dot get er done dot I O.
