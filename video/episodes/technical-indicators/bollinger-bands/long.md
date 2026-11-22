---
format: long
lesson: technical-indicators/bollinger-bands
title: Bollinger Bands: width and %B are two different answers
thumb: A touch isn't a signal
---

@chapter The question
@title text="Bollinger Bands" sub="Technical Indicators" art=thumb
Price touches the upper Bollinger Band. Sell? Or is the band just telling you that volatility has changed? The bands give you two separate outputs, width and percent B, and a touch is neither one of them on its own.

@words text="Volatility · relative position · price behavior"
The lesson splits Bollinger Bands into three things. Volatility, shown by the width. Relative position, shown by percent B. And price behavior at the envelope. Each one needs to be read separately.

@chapter Build the envelope
@art basis-bands
The middle band, the basis, is a moving average. The outer bands are placed a chosen number of standard deviations above and below it. In this lesson, the basis is a simple moving average, and the standard deviation is computed over the same window.

@math heading="Bollinger Bands" items="Basis = SMA(close, n)@the basis;;σ = √( average of (close − basis)² )@standard deviation;;Upper = basis + k · σ@upper band;;Lower = basis − k · σ@lower band"
The basis is the simple moving average of the close over n bars. The standard deviation is the square root of the average squared distance of each close from the basis. The upper band is the basis plus k times that standard deviation, and the lower band is the basis minus k times it.

@words text="Population standard deviation" sub="platforms can differ"
This lesson uses the population standard deviation, over the same period as the basis. Some platforms offer different basis types, sources, or standard deviation conventions, so check yours before comparing values.

@art multiplier-coverage
Two settings shape the envelope: the basis period and the deviation multiplier. A bigger multiplier pushes the bands further out, so fewer closes land outside them. A smaller one pulls them in, and closes outside become common. Both settings change coverage and width together.

@chapter Band width
@art squeeze-expand
The distance between the bands expands and contracts with recent dispersion around the average. When closes cluster tightly around the basis, the bands squeeze together. When they spread out, the bands widen. Width is a volatility reading.

@art squeeze-either-way
A squeeze is tempting to read as a sign that a breakout is coming in a particular direction. It isn't. Contraction describes low recent dispersion. Which way price breaks, if it breaks at all, needs separate evidence.

@chapter Percent B
@math heading="%B" items="%B = (close − lower) ÷ (upper − lower) × 100@close minus;;Close on the lower band → 0@lower band;;Close on the upper band → 100@upper band;;Outside the bands → below 0 or above 100@outside"
Percent B expresses the close relative to the two bands. It's the close minus the lower band, divided by the distance between the bands, times one hundred. A close on the lower band gives zero, and on the upper band, one hundred. A close outside the envelope gives a value below zero, or above one hundred.

@art percent-b-outside
That's position, and it's a different output from width. Price can sit at the top of a narrow envelope, or the top of a wide one, and percent B reads the same in both cases. So read width and percent B as two separate answers.

@chapter Band touches in a trend
@art walk-the-band
And now the touch. In a strong trend, price can move repeatedly along the upper band, or even outside an expanding upper band. Selling every upper band touch means selling into exactly that kind of trend. That's the lesson's first common mistake.

@list heading="Interpret Bollinger Bands" items="Calculate the basis@calculate the basis|Calculate dispersion@dispersion|Place the bands@place the bands|Choose the observation@choose the observation"
So build them carefully. Calculate the basis with a documented period and source. Calculate dispersion over the same window. Place the bands at the chosen multiple. And choose the observation: width, percent B, a close outside, a re entry, or another exact condition.

@chapter Where people slip
@list heading="Common mistakes" items="Selling every upper-band touch@The first|Assuming a squeeze predicts direction@The second|Changing the multiplier to fit one chart@The third"
The first mistake is selling every upper band touch. The second is assuming a squeeze predicts direction. And the third is changing the multiplier to fit one chart. A wider or narrower envelope changes how often events occur, so the multiplier has to be chosen before evaluation, not after.

@chapter Try it
@words text="Basis · bands · width percentile · %B · the exact event"
Your turn. Calculate the basis and the bands. Identify the current band width percentile, and compute percent B. Then state the exact price event your rule requires. Width and percent B, as two separate outputs.

@end text="Change the window and multiplier"
You can change the basis period and the deviation multiplier, on Learn. That's learn dot get er done dot I O.
