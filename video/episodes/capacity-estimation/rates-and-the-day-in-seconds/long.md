---
format: long
lesson: capacity-estimation/rates-and-the-day-in-seconds
title: The day has ten to the five seconds, and what that shortcut costs
thumb: 13.6% low, every time
---

@chapter The question
@title text="Rates: the Day Has 10⁵ Seconds" sub="Capacity Estimation" art=thumb
You know how many requests a service gets in a day. How many is that per second? It's one division, and that division is where a lot of estimates quietly go wrong.

@art volume-to-rate
Start from a population. Daily users times actions per user per day gives you a volume per day. Then divide by the seconds in a day. Do the division last, because the daily volume is a number worth reading, and it's usually one you can check against something somebody measured.

@chapter The unit chain
@math heading="Let the units decide" items="req/day ÷ s/day = req/s@divided by seconds;;✗  req/day × s/day = req·s/day²@multiply instead"
A rate is a quantity per unit of time. Requests per day, divided by seconds per day, gives requests per second. The day cancels. Multiply instead and you get request seconds per day squared, a unit nobody wants. That's the visible sign of the most common error here.

@math heading="Ten million users, a hundred actions" items="10⁷ · 100 = 10⁹ req/day@a billion;;10⁹ ÷ 86 400 = 11 574.074 req/s@eighty six thousand four hundred;;10⁹ ÷ 10⁵ = 10 000 req/s@ten to the five"
Ten million users doing a hundred actions each is a billion requests a day. Divide by eighty six thousand four hundred and you get eleven thousand five hundred and seventy four point zero seven four a second. Divide by ten to the five and you get ten thousand a second, a number you can hold in your head.

@chapter The shortcut day
@art clock-dial
Eighty six thousand four hundred is sixty times sixty times twenty four, and there's nothing approximate about it. What's approximate is what everyone does next: divide by a hundred thousand, because a power of ten is easy at a whiteboard. That shortcut day is longer than a real one.

@art two-days
Put the two days side by side, and the shortcut one is clearly the longer of the two.

@math heading="Exact fractions" items="10⁵ / 86 400 = 125/108@a hundred and twenty five over;;86 400 / 10⁵ = 108/125 = 0.864@a hundred and eight over"
A hundred thousand over eighty six thousand four hundred is a hundred and twenty five over a hundred and eight. Flip it, and a hundred and eight over a hundred and twenty five is exactly zero point eight six four. Going from the shortcut rate back to the true rate, you multiply by a hundred and twenty five over a hundred and eight.

@chapter Two percentages
@art spread-thinner
Spread the same day's volume over a longer day and it arrives more slowly. So the shortcut rate is always the smaller one, for every input.

@math heading="Same shortcut, two numbers" items="125/108 − 1 = 17/108 = 15.74%@longer;;1 − 108/125 = 17/125 = 13.6%@lower"
The shortcut day is seventeen over a hundred and eight, or fifteen point seven four percent, longer. But the rate is seventeen over a hundred and twenty five, or thirteen point six percent, lower. Same numerator, different denominators, so they can't be equal. A percentage isn't preserved when you take a reciprocal.

@words text="×2 up is +100% · ÷2 down is −50%"
It's the same asymmetry as a factor of two being plus one hundred percent upward and minus fifty percent downward, just at a smaller scale.

@chapter When it matters
@art bias-carried
Usually it doesn't. Inside a range sixty four times wide, a thirteen point six percent shortfall is invisible. But it compounds: multiply by a retention window, then a replication factor, and it rides along unchanged.

@art band-and-shift
And it doesn't average out. A range is symmetric around its centre, and a bias isn't. The shortcut lands low every time, so ten estimates made this way are all low together. It's a shift, not a wider error bar, so report it separately.

@chapter Where people slip
@list heading="Common slips" items="Multiplying by 86 400@The first|Saying the rate is 15.74% low@The second|Folding the bias into the error bar@The third"
The first slip is multiplying by eighty six thousand four hundred when you should divide. Check by multiplying your answer back and seeing whether the daily volume returns. The second is saying the rate is fifteen point seven four percent low. It's thirteen point six. And the third is folding the bias into the error bar.

@chapter Try it
@words text="5·10⁶ users × 20 actions" sub="daily volume: 10⁸ requests"
Your turn. Five million daily users doing twenty actions each. The daily volume is ten to the eight requests. Work out both rates, predict their ratio before you compute it, and say what the shortcut rate needs multiplying by to get the true one.

@end text="Use the shortcut, and say you used it"
You can set the users and actions and see both rates side by side, on Learn. That's learn dot get er done dot I O.
