---
format: long
lesson: technical-indicators/indicator-divergence
title: Indicator divergence: a warning, not a trigger
thumb: Same bars, opposite swings
---

@chapter The question
@title text="Indicator Divergence" sub="Technical Indicators" art=thumb
Price makes a lower low, but the RSI makes a higher low. People call that a bullish divergence, and it's often treated as a buy signal. The lesson treats it very differently: as a warning that needs its own confirmation, and only after you've checked that the comparison is even valid.

@art price-and-oscillator
Divergence shows that price and the selected momentum measure changed differently between two swings. That's all it shows. It doesn't define an entry, an invalidation, or timing, by itself.

@chapter Aligned swings
@art aligned-anchors
A valid comparison uses two corresponding price swings, two lows or two highs, and the oscillator values at those same bars. Not the oscillator's own lowest points wherever they happen to be. The values at the bars where price made its swings.

@art unrelated-extrema
That's the first common mistake: connecting unrelated oscillator extrema. If the oscillator low you pick sits at a different bar from the price low, you're comparing two different moments, and the relationship you draw means nothing.

@words text="A relationship between two aligned swings"
The lesson's rule puts it plainly. Divergence is a relationship between two aligned swings. It isn't valid just because price and an oscillator seem to point in different directions somewhere on the chart. So the first job is always to pin down the two bars.

@chapter Regular divergence
@math heading="Regular divergence" items="Bullish: price lower low · oscillator higher low@Bullish;;Bearish: price higher high · oscillator lower high@bearish"
Regular divergence has two specific forms. Bullish divergence pairs a lower price low with a higher oscillator low. Bearish divergence pairs a higher price high with a lower oscillator high. Those exact higher and lower relationships are what make it a divergence.

@art bullish-divergence
Here's the bullish form. Price falls to a low, bounces, and falls to a lower low. Underneath, at those same two bars, the oscillator's second low is higher than its first. Price went further down. Momentum didn't follow it as far.

@art bearish-divergence
And the bearish form is the mirror. Price makes a higher high, but at those same two bars the oscillator makes a lower high. Price pushed further up, with less momentum behind it.

@words text="Not every disagreement is divergence"
Anything else is just disagreement. Calling every disagreement between price and an oscillator a divergence is the lesson's second common mistake. Regular bullish and bearish divergence have specific swing relationships, and nothing else qualifies.

@chapter Wait for price
@art confirm-trigger
Then wait. Divergence can persist, or fail, while price keeps going in its original direction. So require a predefined price structure or entry event after the divergence observation. Entering before price confirms is the third common mistake.

@list heading="Validate a divergence claim" items="Choose two price swings@two price swings|Align oscillator bars@align|Compare direction@compare|Wait for confirmation@wait"
So the method is: choose two price swings, low with low for bullish, high with high for bearish. Align the oscillator bars to those same two bars. Compare direction: did price make a higher or lower swing, and did the oscillator do the same or the opposite? And wait for confirmation.

@chapter Swing selection
@words text="Fixed synthetic anchor zones" sub="real detection needs a precise pivot rule"
One honest note about the lab. Divergence detection is sensitive to how swings are selected. This lesson uses fixed synthetic anchor zones for teaching. Automated detection in practice needs a precise pivot definition and a confirmation delay, because a swing low isn't known to be a swing low until price has moved away from it.

@chapter Where people slip
@list heading="Common mistakes" items="Connecting unrelated oscillator extrema@The first|Calling every disagreement divergence@The second|Entering before price confirms@The third"
So, the three mistakes once more. The first is connecting unrelated oscillator extrema. The second is calling every disagreement divergence. And the third is entering before price confirms.

@chapter Try it
@words text="Two aligned swings · values at the same bars · classify · the price event"
Your turn. Identify the two aligned price swings, and record the oscillator values at those same bars. Classify the higher and lower relationships. Then state the separate price event your rule requires before entry. Do it with the labels hidden, using either RSI or the MACD histogram, and only then reveal the answer to check yourself.

@end text="Classify before you reveal"
You can choose a scenario and an oscillator, and classify before revealing the answer, on Learn. That's learn dot get er done dot I O.
