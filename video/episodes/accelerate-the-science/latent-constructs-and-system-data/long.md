---
format: long
lesson: accelerate-the-science/latent-constructs-and-system-data
title: Every measure is a proxy: Cronbach's alpha on system signals
thumb: When one signal goes rogue
---

@chapter Surveys and systems alike
@title text="Latent Constructs and System Data" sub="Accelerate, Chapter 13" art=thumb
If you trust what your toolchain records more than what people say, chapter thirteen of Accelerate closes with a section for you. Its ideas carry over from surveys to the data a system produces.

@quote text="Latent constructs give us one mechanism to protect ourselves against bad measures or bad agents." cite="Forsgren, Humble and Kim, Accelerate, Chapter 13"
The authors make the argument about surveys and system data in the same breath. Latent constructs give us one mechanism to protect ourselves against bad measures or bad agents.

@chapter Several measures
@art many-readings
The advice has two parts. Collect several measures and look for the same pattern across them. And think through what you're really trying to proxy. Response time is one measure of a system's performance, but what you care about may be better captured by several related measures than by one.

@art proxy-shadow
Then comes the sentence the chapter stresses. All measures are proxies, and that's as true of system data as of survey data.

@art changed-collector
The risk of one measure is concrete. A change to the code that collects a metric can alter it, and if it's your only one, the chance of noticing is low. With several, a shift in one stands out against the rest. And measures that pass today should still be checked from time to time.

@chapter Cronbach's alpha
@math heading="Cronbach's alpha" items="α = k ÷ (k − 1) · (1 − Σσᵢ² ÷ σₜ²)@k over k minus one;;acceptable cutoff: 0.70@nought point seven"
How would you know several measures agree? Appendix C gives Cronbach's alpha: k over k minus one, times one minus the sum of the item variances over the variance of the total. Its acceptable cutoff is nought point seven.

@art moving-together
Read it as a comparison. If the items moved independently, the total's variance would be about the sum of theirs, and alpha would be near zero. If they move together, the total's variance is larger, and alpha gets closer to one.

@math heading="Same agreement, more items (r = 0.5)" items="two items: 0.667@two items;;three items: 0.75@three;;four items: 0.80@four"
Appendix C also warns that alpha runs low on short scales. With an average correlation of nought point five, a textbook relation gives nought point six six seven for two items, nought point seven five for three, and nought point eight for four. So the authors also ran composite reliability, and every construct met the cutoff on one or the other.

@chapter Four signals agree
@art four-signals
Now the lab. Eight days of four signals about the strain on one invented service, each banded from one to seven.

@math heading="Preset four-signals-agree" items="signals' spreads: 151 + 140 + 95 + 112 = 498@four hundred and ninety eight;;totals' spread: 1612@sixteen hundred and twelve;;α = (4/3)(1 − 498/1612) = 1114/1209 ≈ 0.921@nought point nine two one"
Using sums of squares, the four signals' spreads add to four hundred and ninety eight, and the daily totals' spread is sixteen hundred and twelve. So alpha is four thirds times one minus that fraction: nought point nine two one, which meets the cutoff. Leaving out any one signal keeps it high.

@chapter One collector changes
@math heading="Preset collector-changed" items="signal 4 reads 7, 1, 1, 3 after day 4@seven, one, one, three;;α = 712/1167 ≈ 0.610@nought point six one oh;;drop signal 1, 2 or 3: 0.245, 0.448, 0.320@falls further;;drop signal 4: 0.923@back to"
Now suppose the fourth signal's collector changed after day four, and it reads seven, one, one, three. Alpha falls to nought point six one oh, below the cutoff. Leave out signal one, two or three and it falls further. Leave out signal four and it's back to nought point nine two three. The table points at the one that moved.

@chapter What alpha can't do
@art frozen-signal
Don't read more into it. Alpha measures consistency, not validity: four signals that all follow daily traffic would agree whether or not they measure strain. And it doesn't catch every failure. If the fourth collector froze at four, alpha here would be nought point nine two four. A stuck signal that contradicts nothing doesn't pull it down.

@list heading="Common slips" items="A high alpha proves validity@proof|Alpha catches every broken signal@every broken|Short scales judged by alpha alone@alone"
So three slips. Reading a high alpha as proof that the signals measure strain. Expecting alpha to catch every broken signal. And judging a short scale by alpha alone.

@chapter Try it
@words text="d1 7,1,7 · d2 4,2,5 · d3 6,4,7 · d4 5,4,5 · d5 4,1,3"
Your turn. Five days of three signals. Day one: seven, one, seven. Day two: four, two, five. Day three: six, four, seven. Day four: five, four, five. Day five: four, one, three. Find alpha, then alpha with each signal left out. Which would you look at first?

@end text="Check your signals agree"
Then check your arithmetic in the lab, on Learn. That's learn dot get er done dot I O.
