---
format: long
lesson: technical-indicators/macd
title: MACD: three lines, three different measurements
thumb: Three parts, three questions
---

@chapter The question
@title text="MACD" sub="Technical Indicators" art=thumb
MACD shows up as two lines and a row of bars, and it's easy to boil all of that down to bullish or bearish. But it's really three different calculations, each answering its own question. Name them separately and the indicator gets a lot clearer.

@art three-layers
The three are the MACD line, the signal line, and the histogram. Each one is built from the one before it, and all three come from the same closing prices.

@chapter The MACD line
@art two-emas
Start with two exponential moving averages of the close, a fast one and a slow one. The fast period has to be below the slow period. The MACD line is simply the difference between them.

@math heading="MACD line" items="MACD = EMA(fast) − EMA(slow)@fast EMA minus;;MACD > 0 → fast EMA above slow@above zero;;MACD < 0 → fast EMA below slow@below zero"
MACD is the fast EMA minus the slow EMA. When it's above zero, the fast EMA is above the slow one. When it's below zero, the fast EMA is below. So the sign of the MACD line tells you which average is higher, and crossing zero means the two averages crossed.

@art zero-cross
That makes a zero line cross a familiar event. It's the same as the fast moving average crossing the slow one, the crossover from an earlier lesson, just drawn as one line instead of two.

@chapter The signal line
@art macd-signal
The signal line is an EMA of the MACD line itself. That adds another layer of smoothing. So when MACD crosses its signal line, it tells you that MACD changed relative to its own smoothed average. It's a different event from a zero line cross.

@math heading="Signal line" items="Signal = EMA(MACD, signal period)@E M A of the MACD;;Seeded from the first complete simple average@seeded"
The signal is an E M A of the MACD line, over the signal period. In this course, each of these EMAs is seeded from the first complete simple average, so the exact warm up timing can differ across implementations.

@chapter The histogram
@art histogram-bars
The histogram is MACD minus signal. It shows the distance between those two lines. When the bars grow, the separation is expanding. When they shrink, it's contracting. And when a bar crosses zero, MACD has crossed its signal line.

@words text="Histogram = MACD − signal" sub="not volume"
And it is not volume. That's the first common mistake. The bars look like a volume chart, but there's no volume anywhere in the calculation. It's MACD minus its signal line, and that's all.

@chapter Change the periods
@art short-long-settings
In the lab you can change all three periods. Keep the fast period below the slow one, and watch what happens as you shorten the settings. Shorter settings increase how often events occur. Longer settings make them rarer, and later.

@words text="Three events, three meanings" sub="zero-line cross · signal-line cross · histogram turn"
So there are three different events you could build a rule on. A zero line cross, where the averages swap. A signal line cross, where MACD passes its own average. And a turn in the histogram, where the separation starts shrinking. They happen at different times, and they mean different things.

@chapter Use price context
@list heading="Interpret each part" items="Compare fast and slow EMAs@compare the fast|Compare MACD with signal@compare MACD|Read histogram direction@histogram direction|Use price context@price context"
So read each part for its own question. Compare the fast and slow EMAs, through the sign of the MACD line. Compare MACD with its signal. Read the histogram direction for changing separation. And use price context. Is the event happening in a trend, a range, near a structural level, or after a large move that's already done?

@chapter Where people slip
@list heading="Common mistakes" items="Calling the histogram volume@The first|Every crossover as independent evidence@The second|Ignoring delayed confirmation@The third"
The first mistake is calling the histogram volume. The second is treating every crossover as independent evidence. MACD and its signal come from the same closing price series, so they're highly related. And the third is ignoring delayed confirmation. A crossover can arrive after a substantial part of the move has already happened.

@chapter Try it
@words text="Fast EMA · slow EMA · difference · signal · histogram"
Your turn. Identify the fast and slow EMAs and calculate their difference. Derive the signal line, compute the histogram, and describe the exact event your rule uses: a zero line cross, a signal line cross, or a change in histogram direction.

@end text="Change all three periods"
You can change the fast, slow and signal periods, and watch the events change, on Learn. That's learn dot get er done dot I O.
