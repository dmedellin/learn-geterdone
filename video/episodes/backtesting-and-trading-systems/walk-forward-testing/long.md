---
format: long
lesson: backtesting-and-trading-systems/walk-forward-testing
title: Walk-forward testing: train on the past, test on what comes next, repeat
thumb: Train, freeze, roll forward
---

@chapter The problem
@title text="Walk-Forward Testing" sub="Backtesting and Trading Systems" art=thumb
One train and test split gives you one verdict, from one stretch of history. But markets change. A parameter that suited a trend might not suit the balanced market that follows. So what you really want to know is whether your way of choosing parameters survives, again and again.

@words text="Adapt only with information available before each window"
That's what walk forward testing measures. It adapts only with information available before each test window. When the market shifts from trending to balanced, the selected parameter may change, and the test checks whether that adaptation holds up on the next unseen period.

@chapter Three pieces
@list heading="What to understand" items="Training window@training window|Forward window@forward window|Stitched result@stitched result"
There are three pieces. A training window: use only prior observations to select the current system state. A forward window: run that chosen state, without modification, on the next period. And a stitched result: combine only the forward window outcomes for the final evaluation.

@art rolling-windows
Picture it as a pair of windows sliding along the history. Train on one stretch, test on the stretch right after it. Then slide both forward, and do it again.

@art train-then-test
Each fold is a small honest experiment. The training window chooses, the forward window judges, and the forward window is always data the choice never saw. Repeat that across the whole history and you get many verdicts instead of one.

@chapter One fold at a time
@list heading="Advance chronologically" items="Train: compare allowed parameters@Train|Freeze: pick one by the documented rule@Freeze|Test and roll: apply, record, advance@Test and roll"
Every fold preserves the direction of time. Train: compare the allowed parameters using the historical window. Freeze: select one parameter using the documented rule. Test and roll: apply it to the next window, record the results, then advance.

@art frozen-parameter
The freeze matters. Once a fold's parameter is chosen, it doesn't change during the forward window, however that window goes. And document how you break ties, so the choice is mechanical, not a judgement made after the fact.

@chapter How many folds?
@math heading="350 bars · train 80 · forward 30 · step 30" items="(350 − 80 − 30) ÷ 30 = 240 ÷ 30 = 8@two hundred and forty;;8 + 1 = 9 forward windows@plus one"
Here's the lesson's example. Three hundred and fifty bars, an eighty bar training window, and a thirty bar forward window, advancing thirty bars each fold. Take three hundred and fifty, minus eighty, minus thirty. That's two hundred and forty, and divided by thirty is eight. Plus one for the first fold, which comes before any advance, gives nine forward windows.

@words text="Every bar after the first training window, exactly once" sub="9 × 30 = 270 = 350 − 80"
And check it. Nine windows of thirty bars is two hundred and seventy, which is exactly every bar after the first training window. Not eleven, because the first forward window can't start until eighty bars have trained.

@chapter The stitched curve
@art stitched-curve
Now stitch only the forward windows together into one forward simulation. Training returns don't belong in it. They were earned on the data that chose the parameter, so including them reports the fit as if it were a forecast. And every forward window is scored, not just the best fold.

@art short-window-noise
Window length is a real choice. A very short training window may produce unstable parameter selection. It adapts quickly to whatever it saw last, including noise. That's instability, not adaptation. A longer window gives steadier choices but adapts more slowly. There's no free setting, which is why the lab lets you try both.

@art regime-coverage
Look at coverage too. Do the forward windows, between them, span the trending, balanced and falling stretches of the history? A walk forward that only ever tested in one kind of market has only answered the question for that market.

@chapter Not a cure-all
@words text="Walk-forward doesn't remove all overfitting risk"
Does walk forward testing remove all overfitting risk? No. It keeps the future out of each fold's choice. But it still depends on choices, data, costs and repeated experimentation. If you change the candidate set after seeing the stitched curve, the future is back in.

@list heading="Common mistakes" items="Using future folds to choose earlier parameters@The first|Reporting only successful windows@The second|Changing candidates after each forward result@And the third"
The lesson's three mistakes. The first is using future folds to choose earlier parameters. The second is reporting only the successful windows. And the third is changing the candidate set after seeing each forward result.

@chapter Try it
@words text="Change the window lengths"
In the lesson's lab, which uses deterministic synthetic educational data, change the training and testing window lengths. Watch how stable the chosen parameter is, what the forward returns do, and how many regimes the folds cover.

@end text="Slide the windows yourself"
You can change the windows and watch the stitched forward curve, on Learn. That's learn dot get er done dot I O.
