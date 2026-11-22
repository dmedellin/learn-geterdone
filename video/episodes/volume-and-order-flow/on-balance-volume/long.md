---
format: long
lesson: volume-and-order-flow/on-balance-volume
title: On-Balance Volume: a running total, worked by hand
thumb: Add up closes, subtract down
---

@chapter The question
@title text="On-Balance Volume" sub="Volume and Order Flow" art=thumb
A volume bar tells you how much traded, but not on which kind of bar. On Balance Volume, or O B V, tries to keep that bookkeeping for you. It's simple enough to compute by hand, so let's do exactly that.

@words text="Is volume piling up on up closes or down closes?"
O B V tracks whether volume is accumulating on up closes or down closes. Rising O B V means more volume is being added on up closing bars. Falling O B V means more is being subtracted on down closing bars.

@chapter The rule
@art add-subtract
The rule has three parts. When a bar closes above the prior close, add that bar's volume. When it closes below the prior close, subtract it. And when the close is equal, leave the total unchanged.

@words text="The whole bar's volume" sub="whatever its high and low did"
Notice it's the entire bar's volume, every time. An up close adds all of it, whatever the bar's high and low did. And O B V never resets on a close. It's cumulative, so the running total simply continues.

@chapter Worked by hand
@art obv-steps
Here's the lesson's example. Four bars. The closes are one hundred, one oh one, one hundred, and one oh two. The volumes are five hundred, eight hundred, three hundred, and four hundred. Start O B V at zero.

@math heading="Closes 100, 101, 100, 102 · volumes 500, 800, 300, 400" items="Bar 1: no prior close → 0@has no prior close;;Bar 2: 101 > 100 → +800@closes up;;Bar 3: 100 < 101 → −300@closes down;;Bar 4: 102 > 100 → +400@up again;;800 − 300 + 400 = +900@nine hundred"
The first bar has no prior close to compare with, so it contributes nothing. Bar two closes up, from one hundred to one oh one, so add eight hundred. Bar three closes down, so subtract three hundred. Bar four closes up again, add four hundred. Eight hundred minus three hundred plus four hundred is plus nine hundred.

@math heading="Two wrong totals" items="✗  +1,500: added the down close@fifteen hundred;;✗  +2,000: total volume of all four@two thousand"
Two wrong answers are common. Fifteen hundred adds every bar, including the down close. And two thousand is just the total volume of all four bars. O B V adds up closes, subtracts down closes, and ignores the first bar.

@chapter What to read
@art two-levels
So what matters most about O B V? Not its absolute value. The level depends on where the sum started, so only its changes and swings carry information. And never compare one instrument's O B V with another's. They're sums of unrelated volumes from unrelated start points.

@words text="Direction and swings"
What matters is O B V's direction, and how its swings line up with price. Compare matching price points and O B V points over the same bars.

@chapter Confirmation and divergence
@art confirmation
When price and O B V make compatible highs or lows, that supports the observed trend. Price makes a higher high, and so does O B V. Volume participation is going along with the move.

@art divergence
Divergence is when price progresses but O B V fails to confirm. Price makes a new high, and O B V doesn't. That points to weaker volume participation behind the move.

@words text="A non-confirmation warning" sub="not an entry · not proof of manipulation"
So what is that divergence? A non confirmation warning. It isn't an automatic short entry. Divergence is a reason to look harder, and price confirmation is still required. And it isn't proof of manipulation. It only says the recent up closes carried less volume than the down closes.

@chapter Where people slip
@list heading="Common mistakes" items="Calling OBV true buy and sell volume@The first|Comparing OBV across symbols@The second|Trading every small divergence@the third"
Three mistakes. The first is calling O B V true buy and sell volume. It doesn't identify any trade's aggressor. It only sorts whole bars by their close. The second is comparing O B V values across symbols. And the third is trading every small divergence.

@art small-wiggles
Not every small wiggle deserves a reaction. Treat a divergence as a warning, not an entry by itself.

@chapter Try it
@list heading="Reading steps" items="Read price structure@read price structure|Read OBV structure@read O B V structure|Describe agreement@describe agreement"
The lab gives you three steps. First, read price structure. Mark higher highs, lower lows, or a range. Then read O B V structure, its swings over the same bars. Then describe agreement. Does participation confirm price, or diverge from it?

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. Before you open it, try one more by hand. Extend the example with a fifth bar that closes level with the fourth, and say what happens to the total.

@end text="Keep the running total yourself"
You can watch O B V build bar by bar in the lab, on Learn. That's learn dot get er done dot I O.
