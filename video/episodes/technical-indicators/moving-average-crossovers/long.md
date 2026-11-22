---
format: long
lesson: technical-indicators/moving-average-crossovers
title: Moving average crossovers: state, event and whipsaw
thumb: Confirmation, not prediction
---

@chapter The question
@title text="Moving Average Trend Filters and Crossovers" sub="Technical Indicators" art=thumb
A fast moving average crosses above a slow one. Is that a prediction that a trend is starting? Or a confirmation, arriving after part of the move has already happened? The lesson's answer is the second, and that changes how you use it.

@words text="State · event · whipsaw"
Three separate ideas live inside a crossover rule. The state, the event, and the whipsaw. Keep them apart and the rule becomes clear. Blur them, and you'll count things that never happened.

@chapter The state
@art fast-above-slow
Take two moving averages of the same price, one fast and one slow. When the fast one is above the slow one, that's one trend state. When it's below, that's the opposite state. The rule is explicit, and it's delayed, because both averages are built from past prices.

@chapter The event
@art cross-point
A crossover is an event, not a state. It happens only when the relative order changes, the first completed bar where the fast average moves from one side of the slow one to the other. Every bar after that, while it stays on the same side, is the same state, not a new crossover.

@words text="Completed bars only"
And notice the word completed. In this lesson, crossovers are evaluated on completed synthetic bars. In real time, a cross that appears in the middle of a bar can disappear before the bar closes, depending on the rule and the platform.

@chapter Define the rule
@art rule-card
A crossover is useful only when its state, its event and its exit behavior are unambiguous. Two people reading the same chart should mark the same bars.

@list heading="Define a crossover rule" items="Set fast and slow periods@Set|Choose SMA or EMA@Choose|Define the event@define the event|Measure whipsaws@measure"
Set the fast and slow periods, with the fast period shorter, and record both values. Choose SMA or EMA, and don't mix calculation methods unless the rule explicitly requires it, because an EMA reacts faster than an SMA of the same period. Define the event as that first completed bar. And measure whipsaws.

@chapter Whipsaw
@art range-whipsaw
Here's where crossovers get expensive. In a sideways or rapidly alternating market, price oscillates around both averages, and the averages cross back and forth. You get repeated crossings without any durable trend. That's a whipsaw.

@art trend-clean
Now run the same settings on a trending series. The fast average crosses once, and then stays on one side for a long stretch. Same rule, same periods, completely different behavior. That's why the lesson's lab compares the rule in a trend and in a range.

@words text="Count rapid opposite crosses"
So measuring whipsaws means counting rapid opposite crosses, and evaluating the rule separately in trending and ranging conditions. A rule that looks clean on a trend can produce a run of small reversals in a range.

@chapter Delayed confirmation
@art late-signal
Because both averages lag, the cross usually comes after the turn in price. It's a delayed confirmation rule, not an early reversal prediction. That's not a flaw to fix. It's what the rule is: a trade of speed for clarity.

@words text="Shorter: sooner, more whipsaw · Longer: later, cleaner"
And the periods set that trade. A shorter pair of periods crosses sooner but whipsaws more. A longer pair crosses later but more cleanly. The choice belongs to the rule, made before you look at the result.

@chapter Where people slip
@list heading="Common mistakes" items="Counting every bar above as a crossover@The first|Periods from one successful chart@The second|Ignoring range behavior@The third"
The first mistake is counting every bar above as a crossover. The event happens once, when the order changes. The second is selecting periods from one successful chart. A visually perfect pair can be overfit to a single path, and fail in other regimes. And the third is ignoring range behavior, where repeated crossings are common.

@chapter Try it
@words text="Current state · true crossovers · rapid reversals"
Your turn. Identify the current fast versus slow state. Mark each true crossover, and count the rapid reversals. Then explain why the same settings behave differently in a range and in a trend. Remember that the lab's bars are synthetic, built for teaching.

@end text="Test a crossover in a trend and a range"
You can change the average type and both periods, and count the crossovers, on Learn. That's learn dot get er done dot I O.
