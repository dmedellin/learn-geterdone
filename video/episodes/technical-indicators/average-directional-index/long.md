---
format: long
lesson: technical-indicators/average-directional-index
title: ADX: trend strength is not trend direction
thumb: Strong isn't bullish
---

@chapter The question
@title text="Average Directional Index" sub="Technical Indicators" art=thumb
The ADX is high and rising. Is that bullish? It's one of the most common readings people get wrong. A high ADX can show up in a strong uptrend, and it can show up just as easily in a strong downtrend.

@art three-dials
The indicator gives you three separate outputs for three separate questions. Which way is the movement dominant? How strong is the trend? And is that strength rising or falling? The lesson's whole point is to keep those questions apart.

@chapter Directional movement
@art dm-bars
Start with directional movement. Compare the current bar's high and low with the prior bar's. If the high has pushed further up than the low has pushed down, that's positive directional movement. If the low has pushed further down, that's negative directional movement.

@art true-range-span
Then normalize. Directional movement is divided by smoothed true range, which is a bar's own high to low span, or its distance from the previous close, whichever is largest. That's the same quantity the Average True Range lesson builds ATR from.

@math heading="The two DI lines" items="+DI = smoothed +DM ÷ smoothed TR@plus D I;;−DI = smoothed −DM ÷ smoothed TR@minus D I;;Both as percentages of the movement available@percentages"
So plus D I is smoothed positive directional movement over smoothed true range, and minus D I is smoothed negative directional movement over smoothed true range. Both are percentages of the movement available, which makes them comparable across instruments.

@chapter Direction
@art di-lines
Compare the two lines and you get direction. When plus D I is above minus D I, upward movement dominates. When minus D I is above, downward movement dominates. That's directional dominance, and it's the only part of this indicator that has a direction. Everything else is about how strong, or how persistent, that dominance is.

@chapter Strength
@math heading="From DI to ADX" items="DX = relative separation of +DI and −DI@relative separation;;ADX = smoothed DX@smooth it"
ADX comes from the gap between the two DI lines. Take their relative separation, then smooth it. This course uses Wilder style smoothing for true range, directional movement, D X and ADX. The long warm up and the seeding conventions can create small differences between platforms.

@art adx-both-trends
Because ADX is built from the size of the gap, not which line is on top, it measures directional persistence, not bullish or bearish direction. A steady fall pushes minus D I far above plus D I, and ADX climbs, exactly as it would in a steady rise.

@chapter Thresholds
@words text="20 or 25: a rule choice" sub="not a universal boundary"
People often use a threshold like twenty or twenty five to separate trending from not trending. The lesson's view is firm: a threshold like that is a rule choice, not a universal boundary. Its usefulness depends on the instrument, timeframe, method and rule design.

@art range-low-adx
In a sideways range, neither DI line dominates for long, the separation stays small, and ADX tends to stay low. Whether ADX is rising or falling also needs context. A falling ADX says the persistence is fading, not which way price will go next.

@chapter Read all three
@list heading="Read ADX and DI together" items="Dominant DI line@dominant|ADX against the threshold@threshold|ADX rising or falling@rising or falling|None of these alone is an entry@none of"
So read all three. The dominant DI line, for direction. ADX against your chosen threshold, for strength. Whether ADX is rising or falling, for the change in strength. And remember that none of those alone is an entry.

@chapter Where people slip
@list heading="Common mistakes" items="Calling high ADX bullish@The first|Treating a threshold as universal truth@The second|Using ADX alone for entries@The third"
The first mistake is calling high ADX bullish. The second is treating a threshold as universal truth. And the third is using ADX alone for entries. The indicator doesn't define price location, invalidation, or even direction by itself. It tells you about the character of the movement, and a rule still needs the rest.

@chapter Try it
@words text="Direction and strength, separately"
Your turn. Identify the dominant DI line. Compare ADX with the threshold, and say whether it's rising or falling. Then explain why none of those observations alone is an entry. In the lab, switch the scenario and confirm that a high ADX can occur in either an uptrend or a downtrend.

@end text="Separate direction from strength"
You can change the scenario, the period and the threshold, on Learn. That's learn dot get er done dot I O.
