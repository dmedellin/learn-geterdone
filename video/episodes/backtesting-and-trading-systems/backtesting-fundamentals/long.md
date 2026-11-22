---
format: long
lesson: backtesting-and-trading-systems/backtesting-fundamentals
title: What a backtest can and cannot tell you
thumb: Evidence, not a forecast
---

@chapter The question
@title text="Backtesting Fundamentals" sub="Backtesting and Trading Systems" art=thumb
You have a trading idea and years of price history. The obvious move is to run the idea over the history and see what it would have made. That's a backtest. The harder question is what the answer actually means.

@words text="Fixed rules · selected history · stated assumptions"
Here's the lesson's definition. A backtest measures how fixed rules behaved in selected historical conditions. Every word there matters. The rules are fixed. The history is selected. And the conditions include assumptions you chose.

@art evidence-not-proof
What a backtest doesn't do is prove that the same behaviour will continue. The result depends on the data you fed it, the execution you assumed, the costs you charged, and the market regimes that happened to be in the sample.

@chapter Rules before results
@art rules-then-history
So the first idea is rules before results. Before you look at a single performance number, you define the entries, the exits, the sizing, the costs, and the timing. All of it, written down.

@words text="Decide the rules, then look"
Why so strict? Because once you've seen the results, it's very tempting to nudge a rule until the losing stretch goes away. At that point the test is fitted to its answer. It tells you about your editing, not about the market.

@chapter Historical simulation
@art same-rule-every-bar
The second idea is consistency. The simulation applies the same rules to every eligible bar or event. No skipping the awkward days, and no manual exceptions. Each definition is kept operational, so it can be implemented and tested.

@art regimes
And look at the result by market regime, not just as one overall return. A rule that made all its money in one rising stretch, and gave some back everywhere else, is telling you something an overall total hides. The lesson's lab lets you switch the regime and watch this happen.

@words text="Synthetic data · no live market connection"
That lab runs on deterministic synthetic educational data, with no live market connection. You change the regime, the rule's parameters and the costs, and compare the strategy's result with the market behaviour that produced it.

@chapter A fixed order
@list heading="Backtest in a fixed order" items="Define: hypothesis and exact rules@Define|Simulate: timing, fills, costs, accounting@simulate|Evaluate: returns, drawdown, trades, regimes, stability@evaluate"
The lesson gives the work an order. Define: write the hypothesis and the exact rules. Then simulate: apply realistic timing, fills, costs and accounting. Then evaluate: review returns, drawdown, trade count, regimes and stability. Don't optimise the conclusion before the test is defined.

@chapter Returns compound
@art compounding-steps
Here's a small calculation from the lesson's quiz that catches a lot of people. A rule completes two trades. The first makes seven point five percent. The second loses one point one percent. What's the net return?

@math heading="+7.5% then −1.1%" items="1.075 × 0.989 = 1.0632@one point zero seven five;;net return ≈ +6.3%@six point three;;✗  7.5 − 1.1 = 6.4%@Adding them"
Multiply the growth factors. One point zero seven five, times zero point nine eight nine, is one point zero six three two. So the net return is about six point three percent. Adding them gives six point four, which is wrong.

@words text="The loss was taken on a bigger account"
Adding ignores that the one point one percent loss was taken on a larger account, the one the first trade left behind. And the average of the two, about three point two, is a different statistic altogether. The account's change is the product.

@chapter Where people slip
@list heading="Common mistakes" items="Treating historical profit as a prediction@The first|Changing rules after seeing losing periods@The second|Ignoring how assumptions created the result@And the third"
The first mistake is treating historical profit as a prediction. The second is changing the rules after seeing every losing period. And the third is ignoring how the assumptions created the result. Costs, fills and timing are part of the answer.

@art define-simulate-evaluate
So a strong historical result is best treated as evidence that needs further validation. Not proof that losses are impossible, and not a guarantee of live execution. Use a backtest to reject weak ideas and estimate behaviour, not to promise future profit.

@chapter Try it
@words text="Write the hypothesis first" sub="then rules · costs · timing · regimes"
Here's your practice. Take one idea and write its hypothesis before you test anything. Add realistic costs and execution timing. Then, in the lab, change the regime and ask whether the result came from your rule or from the market it ran in.

@end text="Change the regime, watch the result"
You can change the regime, the rule and the costs in the lab, on Learn. That's learn dot get er done dot I O.
