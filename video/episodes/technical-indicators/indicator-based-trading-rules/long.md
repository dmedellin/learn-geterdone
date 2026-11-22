---
format: long
lesson: technical-indicators/indicator-based-trading-rules
title: Indicator trading rules: writing conditions a program can run
thumb: True or false, every bar
---

@chapter The question
@title text="Indicator-Based Trading Rules" sub="Technical Indicators" art=thumb
Buy when momentum is strong near support. It sounds like a rule. But could two people apply it to the same chart and mark exactly the same bars? Could a program? If not, it isn't a rule yet.

@words text="Inputs · parameters · timing · conditions · state · exit"
The lesson's rule sets the bar. A machine readable indicator rule must specify its inputs, parameters, bar timing, Boolean conditions, state handling, and exit logic, all before it can be tested.

@chapter Boolean conditions
@art true-false
Every condition has to resolve to true or false, from known bar data and explicit parameters. Not strong momentum, but RSI above a stated threshold, on a stated period. Not near support, but a close above a specific rolling boundary.

@words text="“Strong momentum” · “near support”"
Phrases like strong momentum or near support can't be executed consistently without numerical definitions. Writing subjective conditions is the lesson's first common mistake.

@chapter Filter, trigger, exit
@art filter-trigger-exit
A complete rule has three separate parts. A filter defines when a setup is allowed. A trigger defines the event. And an exit defines when the position state ends. Keep them separate, and you can see exactly which part did what. A filter on its own never opens a position, and a trigger on its own ignores whether conditions suit it.

@list heading="The simulator's pieces" items="Direction@direction|Trend filter@trend filter|Entry trigger@entry trigger|Strength and volatility filters@strength|Exit rule@exit rule"
The lesson's simulator builds a rule from exactly those pieces. A direction. A trend filter, such as an EMA. An entry trigger, such as an RSI threshold or a Donchian breakout. Optional strength and volatility filters, using an ADX threshold and a minimum ATR percent. And an exit rule, which can include a maximum number of holding bars.

@chapter Data, timing and state
@art completed-bars
Define the data and the timing first: the instrument, the timeframe, the adjusted data policy, and completed bar timing. The simulator uses synthetic completed bars. A rule that fires on a half formed bar can produce events that vanish by the close.

@art state-machine
Then define the state. While a position is active, the rule must prevent duplicate entries, and it has to specify exact exit, reset and invalidation behavior. Otherwise the same trend can trigger entry after entry, and nobody can say which one the rule meant.

@chapter Contradictions
@art contradiction
A rule can also be internally inconsistent even though the code runs. A long system that uses only bearish filters or triggers is the example the lesson gives. Combining a contradictory direction and trigger is the second common mistake. The simulator checks for contradictory combinations like that.

@chapter No performance claim
@words text="Logically complete ≠ profitable"
And a logically complete rule can still lose money. This simulator deliberately doesn't calculate returns, slippage, fees, position sizing, or statistical significance. Those belong to Trading Risk Management, and Backtesting and Trading Systems.

@words text="Data integrity before profitability"
The third mistake is evaluating profitability before data integrity. A backtest is meaningless if adjustment, warm up, timing, and signal state rules are undefined. Get the rule reproducible first. Only then is it worth testing.

@chapter Write the specification
@list heading="Rule specification" items="Define the data and timing@data and timing|Define filters@filters|Define the trigger@trigger|Define state and exit@state and exit"
So the specification has four sections. Define the data and timing. Define the filters: trend, strength, volatility, and any market regime requirements. Define the trigger, as an exact crossover, threshold transition, or rolling boundary event. And define state and exit.

@chapter Try it
@art spec-export
The simulator exports the finished rule as a machine readable specification. That file is the test of everything above. If something is missing from it, a period, a threshold, a timing choice, then the rule depended on something only you knew.

@words text="Export · check · reproduce"
Your turn. Build a rule and export the specification. Verify that every condition and parameter is explicit, and inspect contradictory combinations. Then confirm that the same bar sequence produces the same entries and exits. You're done when another person, or a program, can reproduce every event.

@end text="Build a deterministic rule"
You can choose filters, triggers and exits, and export the rule, on Learn. That's learn dot get er done dot I O.
