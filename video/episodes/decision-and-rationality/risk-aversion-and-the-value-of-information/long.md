---
format: long
lesson: decision-and-rationality/risk-aversion-and-the-value-of-information
title: Why refusing a fair bet can be rational, and what a forecast is worth
thumb: Each extra unit adds less
---

@chapter Refusing a fair bet
@title text="Risk Aversion and the Value of Information" sub="Decision and Rationality" art=thumb
A fair bet is one whose average gain is zero. If you score money at face value, you'd be indifferent to it, and refusing it would be a mistake. But expected utility doesn't score money. It scores utilities.

@art concave-curve
A chooser is risk averse when she prefers a sure amount to a gamble with the same average. With expected utility, that holds exactly when the utility of wealth is concave. It rises, but each extra unit adds less. The first thousand is worth more to you than the ten thousandth.

@chapter Square roots
@math heading="u(wealth) = √wealth" items="wealth 100:  utility 10@a hundred;;wealth 196:  utility 14@a hundred and ninety six;;wealth 4:  utility 2@wealth four"
Take utility equal to the square root of wealth. Wealth of a hundred has utility ten. A hundred and ninety six has utility fourteen. And wealth four has utility two.

@art two-outcomes
Now offer a choice. Keep a hundred for sure. Or flip a fair coin: heads, you end with a hundred and ninety six. Tails, you end with four.

@math heading="Keep 100, or flip for 196 or 4?" items="flip:  14 · 1/2 + 2 · 1/2 = 8@expected utility is fourteen;;keep:  10@keeping"
The flip averages a hundred, the same as keeping a hundred for sure. But its expected utility is fourteen times a half, plus two times a half, which is eight. Keeping scores ten. So the rule prefers to keep. And gambling would only win if heads had probability above two thirds.

@art utility-of-average
Here's the key. The utility of the average isn't the average of the utilities. So convert each outcome first, then average. Do it the other way round and you erase the curvature the whole example turns on.

@chapter Insurance
@math heading="Wealth 100, fire 1/4 costs 75, cover costs 19" items="insure:  hold 81,  utility 9@Insured;;risk:  10 · 3/4 + 5 · 1/4 = 35/4 = 8.75@Uninsured"
Now insurance. Wealth is a hundred, and a fire, with probability a quarter, would cost seventy five. Cover costs nineteen. Insured, you hold eighty one whatever happens, utility nine. Uninsured, you hold a hundred, utility ten, or twenty five, utility five. That scores thirty five quarters, eight point seven five. So insuring wins.

@art smaller-pot
Look again. The cover costs nineteen, and the expected loss is eighteen point seven five. In money, the policy is slightly unfavourable. It's still worth buying, because the lost seventy five comes out of a smaller pot, where each unit is worth more to you. Someone who scored money at face value would decline.

@chapter What a forecast is worth
@words text="VPI = expected best − best expected"
The same machinery prices information. The best expected payoff is the highest expected utility of any act right now. The expected best is the average, over states, of the best payoff available in each state. Their difference is the value of perfect information.

@math heading="The umbrella, rain at 1/3" items="expected best:  2 · 1/3 + 3 · 2/3 = 8/3@two times a third plus;;best expected:  EU(take) = 4/3@four thirds;;VPI:  8/3 − 4/3 = 4/3@eight thirds minus"
On the umbrella, take is best in rain, at two, and leave is best when dry, at three. So the expected best is two times a third plus three times two thirds, which is eight thirds. The best expected is four thirds, from take. So a forecast that never misses is worth eight thirds minus four thirds, which is four thirds.

@art best-per-column
With a perfect forecast, you'd pick the best act in each column: the umbrella in rain, nothing when it's dry. That's what the expected best averages. Without one, you're stuck with a single row for every state.

@art forecast-ceiling
That figure is a ceiling. A forecast that's sometimes wrong gives less than a perfect one, so no forecast is worth more than four thirds here. And if one act is best in every state, knowing the state gains nothing, and the value is zero.

@chapter Where people slip
@list heading="Common slips" items="Calling refusal of a fair bet irrational@The first|Averaging the money, then converting@The second|Paying for a forecast because it's accurate@the third"
The first slip is calling the refusal of a fair bet irrational. It would be a mistake only if the utility of money were a straight line, and nothing requires that. The second is averaging the money and then converting to utility. And the third is paying for a forecast because it's accurate. A forecast is worth what acting on it gains, and an accurate one is worth nothing if you'd choose the same act whatever it said.

@chapter Try it
@words text="cover at utility 8 instead of 9" sub="insure, or risk it?"
Here's one to try. Make the cover dearer, so that being insured has utility eight instead of nine. Compare it with the eight point seven five of risking it. Which does the rule recommend now?

@end text="Utilities in, values out"
You can change the utilities and probabilities, and price a forecast yourself, on Learn. That's learn dot get er done dot I O.
