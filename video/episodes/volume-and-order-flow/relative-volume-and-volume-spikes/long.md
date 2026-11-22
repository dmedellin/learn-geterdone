---
format: long
lesson: volume-and-order-flow/relative-volume-and-volume-spikes
title: Relative volume and volume spikes: what a big bar really means
thumb: The response tells you
---

@chapter The question
@title text="Relative Volume and Volume Spikes" sub="Volume and Order Flow" art=thumb
A volume bar shoots up, far taller than anything around it. It's tempting to treat that as a signal. But a spike only tells you one thing for sure, and it's not the thing most people assume.

@words text="A spike says activity changed" sub="price response says what it meant"
A volume spike says activity changed. Price response says what it meant. Keep those two apart, and the rest of this lesson follows.

@chapter Relative volume
@art rvol-ratio
First, how big is big? Raw volume can't tell you, because every instrument and timeframe has its own normal. So you normalise. Relative volume, or R V O L, is current volume divided by a comparable historical baseline.

@math heading="RVOL" items="RVOL = current ÷ baseline@current volume divided;;180,000 ÷ 100,000 = 1.80@a hundred and eighty thousand"
In symbols, R V O L equals current volume divided by baseline volume. If current volume is a hundred and eighty thousand and the baseline is a hundred thousand, R V O L is one point eight.

@math heading="Not these" items="✗  100,000 ÷ 180,000 = 0.56@point five six;;✗  2.80 would need 280,000@two point eight"
Watch the order. Point five six is baseline over current, upside down. And two point eight would need a bar of two hundred and eighty thousand. This bar is one point eight times its baseline, not two point eight.

@chapter A fair baseline
@art session-curve
The baseline has to be fair. Compare the same timeframe, and for intraday data, similar times of day. Why? Because volume has a session pattern. The open and close commonly trade more than midday.

@words text="Open ≠ midday"
So if you compare an opening bar with a midday average, nearly every opening bar looks like a spike. A fair baseline removes that known bias. It can't make R V O L a certainty, since news, auctions and expiries still distort any single bar.

@chapter Does it qualify?
@art threshold
Once you have a ratio, you can set a threshold. The lab's example uses a twenty bar baseline averaging one thousand contracts, and a threshold of one and a half times.

@math heading="Baseline 1,000 · threshold 1.5×" items="2,400 ÷ 1,000 = 2.4×@twenty four hundred;;2.4× > 1.5×@above the threshold;;✗  2,400 − 1,000 = 1,400 → 1.4×@the excess"
A bar prints twenty four hundred. Twenty four hundred divided by one thousand is two point four times, above the threshold, so it qualifies as a spike. Don't use the excess. Twenty four hundred minus one thousand is fourteen hundred contracts, not a ratio of one point four. And one thousand over twenty four hundred, point four two, inverts it.

@words text="Qualifies ≠ meaningful" sub="what it meant depends on the bars after it"
So the bar qualifies. But qualifying only means the activity was unusual. What it meant still depends on the bars after it. That's the next step, and it's the one people skip.

@chapter What the spike meant
@art spike-progress
Now the important part. What happened next? A spike with clear price progress supports the aggressive side. Volume rose, and price kept making directional progress. That's expansion.

@art spike-stall
But a spike with little progress is different. Extreme volume appears, and price stalls, rejects, or quickly reverses. That suggests absorption, or a temporary climax. Orders are active, but the aggressive side isn't moving price far.

@words text="Possible absorption or balance" sub="not strong progress · not no participation"
So a large spike with almost no price movement is not strong directional progress. Price barely moved. And it's not a lack of participation either. A spike is the most participation in the window. What's missing is the price response.

@chapter Where people slip
@list heading="Common mistakes" items="Comparing the open with midday@The first|Calling every spike institutional buying@The second|Ignoring news, auctions and expiration@the third"
Three mistakes. The first is comparing the market open with midday volume. The second is calling every spike institutional buying. And the third is ignoring news, auctions, and expiration effects.

@art judge-next
The rules that fix them are short. Use comparable bars for the baseline. Treat a spike as an event, not a directional signal. And judge the next price response, not only the spike bar.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. Follow its steps. Build a fair baseline. Locate the spike, and measure how far it exceeds normal participation. Then inspect the response.

@words text="Continue, stall, or reverse?"
Did price continue, stall, or reverse after the spike? Answer that before you decide what the spike meant.

@end text="Find the spike, then read the response"
You can build a baseline and test your spike readings in the lab, on Learn. That's learn dot get er done dot I O.
