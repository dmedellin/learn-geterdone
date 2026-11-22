---
format: long
lesson: technical-indicators/donchian-channels
title: Donchian Channels: which bars define the breakout?
thumb: Test against the prior channel
---

@chapter The question
@title text="Donchian Channels" sub="Technical Indicators" art=thumb
Here's a rule that sounds perfectly reasonable. Buy when the close is above the highest high of the channel. Written the wrong way, that rule can never fire, not once. The reason is a question about which bars the channel includes.

@words text="Which bars define the boundary?"
That's the heart of this lesson. Donchian Channels are simple to calculate, but a breakout rule built on them is only as good as its answer to one question. Which bars define the boundary that a close is tested against?

@chapter Rolling extremes
@art upper-lower
The upper channel is the highest high over the selected lookback. The lower channel is the lowest low over the same lookback. That's all. No averaging, no smoothing, just the rolling extremes.

@math heading="Donchian Channel" items="Upper = highest high of the last n bars@highest high;;Lower = lowest low of the last n bars@lowest low"
The upper channel is the highest high of the last n bars, and the lower channel is the lowest low of the last n bars. You choose n, the number of completed bars used to establish the high and low. A longer lookback sets the boundaries further apart, so a close outside them is a rarer event.

@chapter Stepwise updates
@art step-levels
Because the channel is made of extremes, it moves in steps. Levels can stay flat for many bars, and then jump when a new extreme enters the window, or when an old extreme drops out of it. A flat line on a Donchian chart isn't a calculation error. It's the method.

@chapter Current or prior channel
@art self-test
Now the trap. Suppose the channel includes the current bar. Then the upper channel is at least that bar's own high. And a close is never above its own high. So a close above rule written against that channel can never fire.

@art prior-channel
The fix is to use the channel calculated through the previous bar. Then the current close is tested against an already known boundary, one that the current bar didn't help to set. In this lesson's lab, the display can show either channel, but the signal markers always compare the close against the previous bar's completed lookback.

@words text="State whether the current bar participates"
So for any signal, say explicitly whether the current bar participates in the boundary calculation. Leave that unstated, and two people can code the same idea and get completely different results.

@chapter Define the breach
@list heading="Define a Donchian breakout" items="Choose the lookback@Choose the lookback|Choose current or prior channel@current or prior|Define the breach@breach|Define re-entry and exit@re entry"
Make the rolling boundary and the bar timing explicit. Choose the lookback. Choose current or prior channel. Define the breach: a high above, a close above, a touch, or a completed close. And define re entry and exit, including how the rule handles repeated closes outside, opposite breakouts, and channel changes.

@art repeated-closes
That last part matters for counting. If price closes above the channel three bars in a row, is that one breakout or three? Decide whether only the first transition outside counts as an event, or whether repeated bars matter. Otherwise you'll double count a single state.

@chapter Where people slip
@list heading="Common mistakes" items="Using the current high to test itself@The first|Counting every close above as new@The second|Assuming a breakout must continue@The third"
The first mistake is using the current high to test itself. The second is counting every close above as a new breakout. And the third is assuming a breakout must continue. Donchian Channels identify new rolling extremes, not guaranteed acceptance beyond them.

@art failed-breakout
That third one deserves a picture. Price closes above the prior channel, a genuine new rolling high, and then falls straight back inside. The channel did its job. It identified a new extreme. Whether price is accepted beyond it is a separate question, which is why the rule still needs a confirmation and an exit.

@chapter Try it
@words text="Current and prior levels · the comparison · events without double counting"
Your turn. Calculate the current and prior Donchian levels, and identify the breakout comparison. Count events without double counting states. Then state the confirmation and exit your rule requires. In the lab, change the lookback and compare signal frequency in a range and in a trend.

@end text="Test a rolling breakout boundary"
You can change the lookback and switch between the current and prior channel, on Learn. That's learn dot get er done dot I O.
