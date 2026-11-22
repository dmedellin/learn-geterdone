---
format: long
lesson: backtesting-and-trading-systems/in-sample-validation-and-out-of-sample-data
title: In-sample, validation, out-of-sample: keeping one test you haven't seen
thumb: Look once, at the end
---

@chapter The problem
@title text="In-Sample, Validation, and Out-of-Sample Data" sub="Backtesting and Trading Systems" art=thumb
You try twenty settings for a parameter and keep the best. Then you report how well that best setting did, on the same data. Of course it did well. You chose it because it did well there.

@words text="The data that chose the system can't also grade it"
That's the lesson's core idea. The data used to choose the system cannot also provide an unbiased final estimate of that system. You need a separate piece of history that played no part in the choice.

@art trend-then-flat
Here's how it goes wrong. A parameter can capture buyer persistence in a trending training period, and then fail when the next period turns balanced or bearish. It learned the trend, not a repeatable behaviour.

@chapter Three segments
@art three-segments
So split the history into three parts, in time order. In sample: develop rules and estimate parameters. Validation: compare alternatives and make limited design decisions. And out of sample: evaluate the frozen system once, on data that wasn't used for selection.

@list heading="Protect the final test" items="Develop on in-sample data@Develop|Select on validation data@Select|Freeze, then test@Freeze and test"
The workflow follows the split. Develop: use in sample data for hypotheses and parameter candidates. Select: use validation data for a controlled comparison. Freeze and test: lock the system completely before revealing out of sample performance.

@chapter Counting the split
@math heading="260 bars, split 50 / 25 / 25" items="260 × 50% = 130 in-sample@two hundred and sixty times;;260 × 25% = 65 validation@twenty five percent;;remaining 65 out-of-sample@remaining sixty five"
Here's the lesson's example. Two hundred and sixty bars, split fifty, twenty five, twenty five. Two hundred and sixty times fifty percent is one hundred and thirty in sample bars. Twenty five percent is sixty five for validation. And the remaining sixty five are out of sample.

@art time-order
Two things about that split. It's set before any candidate is scored, so you can't pick the split that gives the best chart. And it runs in chronological order. Random splits that break time order are one of the lesson's named mistakes for time series trading.

@chapter The one-look rule
@art peeking-leak
Now the hard part. Repeatedly checking out of sample data turns it into training data. Look at the final test after every change, and information leaks back into development. The supposedly unseen data starts shaping the rules.

@art frozen-system
Freezing means everything. The rules, the parameter, the costs, the sizing. Nothing is allowed to change once you've decided to look, because any change made after looking is a change made with the answer in hand.

@words text="After the first look, it's no longer unseen"
So the final parameter is chosen from training or validation data, under the process you defined. Never from the final test, repeatedly. Each look to choose a parameter uses it up. And not only the best month either: a period chosen for its result is just selection bias with a date on it.

@chapter Reading the gap
@art is-oos-gap
When you finally look, compare in sample and out of sample results. A large gap suggests possible overfitting, or regime dependence. The selected rule may be fitting noise, or conditions unique to the development data.

@words text="The out-of-sample figure is the one to believe"
A gap doesn't mean live success, and it isn't a reason to stop. It's the signal to ask why. And when you report, report every split, including the weak ones.

@chapter Where people slip
@list heading="Common mistakes" items="Choosing the split with the best chart@The first|Retuning after each final-test failure@The second|Random splits that break time order@And the third"
The first mistake is choosing the split that gives the best chart. The second is retuning after each final test failure, which quietly turns the final test into another validation set. And the third is using random splits that break time order. Set split dates before optimising, and keep the final test out of reach during development.

@chapter Try it
@words text="Optimise · validate · reveal"
The lesson's lab uses deterministic synthetic educational data. Optimise a parameter in training, inspect it on validation, then reveal the untouched out of sample result. Notice how you feel about the number before you see it, and how tempting it would be to go back and adjust just one thing. That temptation is exactly what the freeze is protecting you from.

@end text="Freeze it, then reveal it"
You can optimise, freeze and reveal the final test yourself, on Learn. That's learn dot get er done dot I O.
