---
format: long
lesson: volume-and-order-flow/volume-and-order-flow-trading-rules
title: Turning volume and order flow into rules you can test
thumb: Context, evidence, confirmation
---

@chapter The question
@title text="Volume and Order Flow Trading Rules" sub="Volume and Order Flow" art=thumb
You've now got a whole toolkit. Relative volume, VWAP, delta, C V D, the tape, and the book. But a pile of readings isn't a rule. This lesson is about turning them into something explicit, that you could hand to someone else and test.

@art rule-parts
A useful rule separates five things. Context, evidence, trigger, invalidation, and exit. Each part answers a different question, and none of them should quietly do another's job.

@words text="Flow confirms who is making progress"
And here's the boundary. Volume and order flow should confirm who is making price progress. They shouldn't replace market structure, risk limits, or execution rules.

@chapter Context, evidence, confirmation
@list heading="The building blocks" items="Context: trend, range, level, value, anchor@Context is|Evidence: RVOL, VWAP, delta, CVD, tape, depth@Evidence is|Confirmation: observable price action@confirmation is"
Context is where the setup is valid: a trend, a range, a breakout level, a value location, or an event anchor. Evidence is the flow reading: relative volume, VWAP location, delta, C V D, tape, or depth behaviour. And confirmation is observable price action that proves the aggressive side is making progress.

@chapter Make it measurable
@art vague-vs-measurable
Which of these conditions is measurable? Strong volume. Buyers look confident. Or relative volume of at least one and a half, over the prior twenty comparable bars.

@words text="RVOL ≥ 1.5 over the prior 20 comparable bars"
Only the last. Strong compared with what? Without a baseline and a threshold, two people reading the same bar would disagree. And confidence isn't observable in data. A rule needs a quantity, an operator, and a baseline.

@chapter Contradictions
@art contradiction
Now a long rule that requires price below VWAP, and sustained acceptance above VWAP, at the same bar. What is that? Contradictory. Both can't be true under a clear definition, and the lab's validator flags the pair.

@words text="Not a no-trade condition"
It isn't a no trade condition either. A no trade condition names situations to stand aside. This is two entry conditions that exclude each other, a rule that can never fire.

@art absorbed-break
Here's a subtler one. A long rule uses buying absorbed at the ask as its flow evidence, and a close above resistance as its confirmation. The validator calls it a conflict. Ask side absorption describes buying that failed to move price.

@words text="Asks the buying to fail and succeed at once"
So the rule asks the buying to fail and succeed at once. The problem isn't the resistance level. A long confirmed by a close above resistance is the standard breakout shape. The conflict is in the flow condition.

@chapter What flow should confirm
@words text="Which side is making progress" sub="in the stated context"
So what should order flow confirm? Which side is making price progress, in the stated context. Flow is evidence about current behaviour, not certainty.

@words text="Not returns · not your preference"
It can't confirm guaranteed future returns. Nothing in the exported rule contains a performance figure. Whether a rule earns anything is a question for the Backtesting and Trading Systems course. And it shouldn't confirm your preferred direction. A rule written to confirm what you already want fires on every chart. The flow condition should be able to say no.

@chapter Where people slip
@list heading="Common mistakes" items="Vague words without thresholds@The first|Several versions of the same evidence@The second|Optimising a rule on one chart@the third"
Three mistakes. The first is using vague words, like strong or heavy, without thresholds. The second is combining multiple versions of the same evidence. And the third is optimising a rule on one chart.

@art stacked-same
The second is easy to miss. Three conditions that all measure the same thing look like three pieces of evidence, but they're really one, counted three times.

@art overfit
That last one feels like progress. You tweak the rule until it catches every move on the chart in front of you. But a rule tuned to one chart has only been tested on that chart.

@chapter Try it
@list heading="Build it in order" items="Define context@define context|Require participation and flow@require participation|Require price confirmation@require price confirmation"
The lab builds a rule in three steps. First, define context: state where the setup is valid. Second, require participation and flow, with measurable thresholds and a side. Third, require price confirmation. Add entry, invalidation, target, and no trade conditions.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. Write one rule, let the validator check it for contradictions, then export it to test in Backtesting and Trading Systems.

@end text="Write it down, then test it"
You can build and validate your own rule in the lab, on Learn. That's learn dot get er done dot I O.
