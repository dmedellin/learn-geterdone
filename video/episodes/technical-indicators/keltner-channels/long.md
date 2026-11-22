---
format: long
lesson: technical-indicators/keltner-channels
title: Keltner Channels: an ATR envelope around an EMA
thumb: Touch, trade or close?
---

@chapter The question
@title text="Keltner Channels" sub="Technical Indicators" art=thumb
A Keltner Channel looks a lot like Bollinger Bands. A line in the middle, a band above, a band below. So are they interchangeable? No. They measure volatility in different ways, and they can widen and narrow at different times.

@words text="EMA ± multiplier × ATR"
The modern formulation this course uses fits in one line. An exponential moving average in the middle, and bands a fixed multiple of average true range above and below it.

@chapter The centerline
@art ema-center
A common modern Keltner formulation centers the channel on an exponential moving average. You choose its source and its period. The period controls how quickly the center responds to price.

@chapter The ATR envelope
@art atr-bands
The outer bands are placed a selected ATR multiple above and below the basis. ATR is average true range, the smoothed measure of movement that includes gaps. This course uses Wilder style ATR. You choose its period, and the multiplier that sets how far out the bands sit.

@math heading="Keltner Channel" items="Basis = EMA(close, n)@the basis;;Upper = EMA + m · ATR@the upper band;;Lower = EMA − m · ATR@the lower band"
The basis is the EMA of the close over n bars. The upper band is the EMA plus m times ATR. The lower band is the EMA minus m times ATR. Three settings in all: the EMA period, the ATR period, and the multiplier m.

@words text="Other definitions exist"
Other Keltner definitions exist, historical ones and platform variants. So document the exact formulation you use, and verify the implementation before comparing values with anyone else's.

@chapter The settings
@art multiplier-width
Period and multiplier control how quickly the center and the envelope respond. A shorter EMA period makes the centerline follow price more closely. A shorter ATR period makes the band width react faster to a change in movement. And a larger multiplier simply pushes both bands further from the center, so price reaches them less often.

@art gap-response
And because ATR is built from true range, a gap feeds straight into the width. When a bar opens far from the previous close, its true range is measured from that close, so the gap counts, even if the bar itself is narrow. Standard deviation of closes sees that same gap in a different way.

@chapter Keltner versus Bollinger
@art keltner-vs-bollinger
Here's the real difference. Keltner Channels use average true range. Bollinger Bands use standard deviation. ATR and standard deviation respond differently to gaps and to dispersion, so the two envelopes can contract and expand differently on the same data. The lab can draw both on one chart so you can compare their widths.

@words text="Not interchangeable"
That's why treating them as interchangeable is one of the lesson's common mistakes. A rule tested on one envelope is a rule about that envelope.

@chapter Define the event
@art touch-trade-close
Now the word breakout. A touch of the band, a trade beyond it during the bar, and a completed close outside it are three different events. Calling a channel touch a confirmed breakout is another common mistake.

@list heading="Build a Keltner Channel" items="Choose the centerline@centerline|Calculate ATR@calculate ATR|Set the multiplier@multiplier|Define the event@define the event"
So build it step by step. Choose the centerline: the EMA source and period. Calculate ATR, with its smoothing period and convention. Set the multiplier, placing both bands at a fixed ATR multiple from the EMA. And define the event: an exact close, an intrabar touch, a re entry, a slope, or a width condition, rather than the word breakout alone.

@chapter Where people slip
@list heading="Common mistakes" items="Assuming every implementation is identical@The first|Calling a touch a confirmed breakout@The second|Keltner and Bollinger as interchangeable@The third"
The first mistake is assuming every implementation is identical. The basis type, the ATR period, the multiplier and historical formulations can all differ. The second is calling a channel touch a confirmed breakout. And the third is treating Keltner and Bollinger envelopes as interchangeable.

@chapter Try it
@words text="EMA basis · ATR · both bands · compare with Bollinger"
Your turn. Calculate the EMA basis and the ATR. Place both bands. Compare the channel's width with Bollinger Bands on the same data, and notice where the two disagree. And state the exact event your rule uses.

@end text="Reproduce the full channel"
You can change the EMA period, ATR period and multiplier, and overlay Bollinger Bands, on Learn. That's learn dot get er done dot I O.
