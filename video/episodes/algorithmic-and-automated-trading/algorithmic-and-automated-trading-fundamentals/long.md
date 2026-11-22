---
format: long
lesson: algorithmic-and-automated-trading/algorithmic-and-automated-trading-fundamentals
title: What automation does to a trading strategy, and what it doesn't
thumb: Automation isn't an edge
---

@chapter The question
@title text="Algorithmic and Automated Trading Fundamentals" sub="Algorithmic and Automated Trading" art=thumb
You've got a strategy with a tested rule. Hand it to a computer and let it trade on its own, and surely it gets better? Faster, tireless, no emotions. The lesson's answer is more careful than that.

@words text="Automation changes how decisions reach the market"
Automation changes how decisions reach the market. It does not create an edge by itself. What it adds is repeatable execution of defined decisions. If the logic has no edge, automation just repeats a losing decision faster.

@art pipeline-stages
And a system should trade only when its defined signal, risk and execution conditions are all satisfied. Even when buyers keep accepting higher prices and the move looks obvious. The conditions decide, not the mood of the chart.

@chapter Three ideas
@list heading="What to understand" items="Algorithm@algorithm|Automation level@automation level|Control boundary@control boundary"
Three ideas. An algorithm: a deterministic procedure that converts defined inputs into outputs. An automation level: alert only, approval required and automatic execution each carry different operational risk. And a control boundary: risk checks must stay independent from the strategy that requests the trade.

@art risk-gate
That last one is worth slowing down on. A signal can be perfectly valid while the trade it proposes breaks an account or portfolio limit. So the component that should be able to block a valid signal is the risk engine. Letting the strategy bypass pre trade risk checks is one of the lesson's named mistakes.

@chapter The pipeline
@list heading="Keep the pipeline explicit" items="Observe: validated data, updated state@Observe|Decide: signal, then portfolio and risk checks@Decide|Act: alert, request approval, or submit@Act"
The lesson lays the pipeline out in three stages, each with one responsibility and a recorded result. Observe: receive validated market data and update strategy state. Decide: generate a signal, then apply portfolio and risk checks. Act: alert, request approval, or submit an order through the broker adapter.

@art script-vs-system
Recording each stage is what lets you answer, later, why the system did what it did. A scheduled script that buys on a condition isn't a complete trading system. It's missing the boundaries, the state and the record.

@chapter Automation levels
@art automation-levels
Think of the three levels as three amounts of authority. Alert only tells a person. Approval required asks a person before anything goes to the broker. Automatic execution acts alone. Authority is granted in stages, and each stage has to be earned.

@words text="One week of paper evidence · an untested kill switch"
Here's a question from the lesson. A strategy has one week of paper evidence, and a kill switch that's never been tested. Which level fits? Alert only, or approval required, until the switch is tested and the evidence is longer. A small size limits the loss, not the need for a person.

@chapter Count the orders
@math heading="5 signals · feed 2 s old, limit 3 s · daily limit 2 · alert-only" items="feed fresh: 2 s < 3 s@two seconds;;risk gate passes 2 of 5@passes two;;alert-only: 2 alerts, 0 orders@zero orders"
Now a worked one. A rule fires five times in a session. The feed is two seconds old against a three second limit, so the data is fresh. The daily limit is two new positions, so the risk gate passes two of the five. And automation is alert only. So it sends two alerts, and submits zero orders.

@art alert-only
Not five, because three never pass the daily limit. And not two, because alert only has no execution authority at all. The level decides the last step, and nothing before it.

@chapter Where people slip
@list heading="Common mistakes" items="A scheduled script called a complete system@The first|Letting the strategy bypass risk checks@The second|Assuming faster automation fixes a weak strategy@And the third"
The first mistake is calling a scheduled script a complete trading system. The second is letting the strategy bypass pre trade risk checks. And the third is assuming faster automation improves a weak strategy. It can only repeat what it was given.

@art separated-roles
So keep data, strategy, risk and execution as separate responsibilities. Record every stage. And start with alerts or approval before you enable automatic orders.

@chapter Try it
@words text="Regime · automation level · data delay · risk gate"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the market regime, the automation level, the data delay and the risk gate. Watch which signals become approvals, and which approvals become orders.

@end text="Follow a signal to the broker"
You can follow a signal through the risk gate and the automation level, on Learn. That's learn dot get er done dot I O.
