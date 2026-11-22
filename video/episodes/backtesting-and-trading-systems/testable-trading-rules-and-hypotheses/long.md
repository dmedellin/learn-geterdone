---
format: long
lesson: backtesting-and-trading-systems/testable-trading-rules-and-hypotheses
title: Turning a trading idea into a rule you can actually test
thumb: Same data, same decision
---

@chapter The problem
@title text="Testable Trading Rules" sub="Backtesting and Trading Systems" art=thumb
Buy strong stocks. It sounds like a plan, but try to code it. What counts as strong? Strong compared with what, over how long, and when exactly do you buy?

@art vague-cloud
That's the problem with most trading ideas. They're written in words that two people would read differently. And a computer can't read them at all. The lesson's claim is simple: a trading idea becomes testable only when every decision has an explicit condition.

@chapter Three ideas
@list heading="What to understand" items="Hypothesis@a hypothesis|Deterministic rule@a deterministic rule|Complete lifecycle@the complete lifecycle"
There are three pieces. First, a hypothesis: a statement of why a repeatable market behaviour might produce an edge. Second, a deterministic rule: the same inputs must always produce the same signal. And third, the complete lifecycle of a trade, from start to finish.

@art same-input-same-output
Deterministic is the key word. Feed the rule the same bars twice, and it must give the same answer twice. If a person has to make a judgement call in the middle, the test is measuring that person, not the rule.

@chapter What a full rule states
@list heading="A valid system states" items="Data and threshold@the data|Timing and order@the timing|Size@the size|Exit@the exit|No-trade conditions@no-trade"
So what does a complete rule say? It states the data it reads and the threshold it compares against. It states the timing, and the kind of order. It states the size. It states the exit. And it states the no-trade conditions, the situations where it stays out.

@art lifecycle-loop
Put another way, a full lifecycle covers no-trade, entry, sizing, management, exit and invalidation. An entry with no exit isn't a trade, and a test of it has nothing to measure.

@chapter From observation to condition
@list heading="Convert observations into conditions" items="Observe price and volume behaviour@Observe|Specify measurable conditions@specify|Reject words that can't be calculated@reject"
The lesson gives a method. Observe: describe the price and volume behaviour you've noticed. Specify: translate it into measurable conditions, with exact values and event timing. Then reject ambiguity: remove any discretionary word that can't be calculated.

@words text="strong · weak · near" sub="no value, no rule"
Words like strong, weak or near are the usual suspects. Each one needs a number, or it has to go.

@chapter A worked example
@words text="Buy next open when close > prior 20-bar high"
Here's a statement that passes. Buy at the next open when the close exceeds the prior twenty bar high. It names the data, the threshold, and when the order executes.

@art breakout-threshold
The threshold is a line you can draw: the highest point of the last twenty bars. Either the close is above it or it isn't. Compare that with buy when the chart looks strong, or buy when sentiment feels positive. Neither has anything to compute.

@math heading="Close 104.20 · prior 20-bar high 104.00" items="104.20 > 104.00  →  signal@one hundred and four point two;;signal known at the close@known at the close;;earliest fill: tomorrow's open@tomorrow's open"
Now put numbers on it. Today's close is one hundred and four point two, and the prior twenty bar high is one hundred and four. The close is higher, so there's a signal. But that signal is only known at the close. So the earliest price the rule can fill at is tomorrow's open.

@art next-open-fill
Not today's close, because by the time you know it, that price has gone. And not one hundred and four, because that's just the level you compared against. The rule has to say when the signal is known and when the order is placed.

@chapter Where people slip
@list heading="Common mistakes" items="Strong, weak or near with no values@The first|Testing entries without exits@The second|Manual exceptions during the test@The third"
Three mistakes come up again and again. The first is using words like strong, weak or near without values. The second is testing entry rules without exits. And the third is allowing manual exceptions during the test, which quietly turns the rule back into judgement.

@art hypothesis-first
And write the hypothesis first. It won't guarantee a positive result, and it doesn't replace the data. What it does is explain what market behaviour the rule is meant to capture, so you know what the test is really testing.

@chapter Try it
@words text="Pick one idea · write every condition" sub="data · threshold · timing · size · exit · no-trade"
For practice, take an idea you've heard, and write it as a rule. Use exact thresholds and time references. Say when the signal is known and when the order goes in. Add conditions that prevent a trade. Then ask whether two people would make the same trade from it.

@end text="Build a rule, check it's complete"
You can build a long or short rule and check that it's complete enough to test, on Learn. That's learn dot get er done dot I O.
