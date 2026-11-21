---
format: long
lesson: separable-equations-growth-and-decay/harvesting-and-the-threshold
title: Harvesting and the threshold: when a population collapses
thumb: One step past the peak, collapse
---

@chapter The question
@title text="Harvesting and the Threshold" sub="Separable Equations, Growth and Decay" art=thumb
Take a logistic population that grows to four, and remove a fixed amount of it every unit of time. Fishing and logging are the usual pictures. How large can that harvest be before the population no longer survives?

@chapter The harvested equation
@math heading="Harvested logistic" items="y′ = r·y·(1 − y/K) − H@minus H;;r = 1, K = 4:  y′ = −y²/4 + y − H@r equals one"
Subtract a constant harvest H from the logistic equation: y prime equals r y times one minus y over K, minus H. The harvest is taken at the same rate whatever the population is. That's an assumption about the fishery. With r equals one and K equals four, it's minus y squared over four, plus y, minus H.

@art growth-minus-harvest
Picture the natural growth as a hump, and the harvest as a flat line across it. The population grows where the hump is above the line, and shrinks where it's below.

@chapter Counting equilibria
@math heading="Equilibria" items="y² − 4y + 4H = 0@y squared minus four y;;discriminant 16·(1 − H)@The discriminant"
The equilibria solve y squared minus four y plus four H equals zero. The discriminant is sixteen times one minus H. For H less than one there are two roots, at H equals one there's one, and for H greater than one there are none.

@math heading="Three harvests" items="H = 3/4:  (y − 1)(y − 3) = 0,  y = 1, 3@three quarters;;H = 1:  (y − 2)² = 0,  y = 2@H equals one;;H = 5/4:  16 − 20 < 0,  none@five quarters"
With H equals three quarters, it factors as y minus one times y minus three, so y is one or three. With H equals one, it's y minus two all squared, one root at two. With H equals five quarters, sixteen minus twenty is negative, so there are none.

@chapter A harvest of three quarters
@art two-equilibria
With three quarters, the rate is negative below one, positive between one and three, and negative above three. So a population between one and three grows to three, one above three falls to three, and one below one falls further.

@words text="1 unstable;  3 stable" sub="f′(1) = 1/2 > 0,  f′(3) = −1/2 < 0"
The harvest hasn't removed the attracting level. It's moved it from four down to three, and it's created a repelling one at one. The slopes agree. The slope at one is a half, positive, so nearby populations move away. At three it's minus a half, so they move towards it.

@math heading="Just below the lower level" items="growth at 1 = 3/4 = harvest@exactly three quarters;;growth at 9/10 = 279/400 < 300/400@nine tenths"
That repelling level is the dangerous one. At one, the natural growth is exactly three quarters, the harvest, so nothing changes. At nine tenths, the growth is two hundred seventy nine over four hundred, less than three hundred over four hundred. So the population shrinks, and the less there is, the less growth to pay for the harvest.

@art bad-year
A harvest the population can replace today may not be one it can replace after a bad year.

@chapter At the threshold, and past it
@art semistable
At H equals one, the rate is minus y minus two squared, over four, which is never positive. A population above two falls back to two. One below two falls away, and so does one that dips just under it. It attracts from one side only, so it's called semistable.

@words text="H = r·K/4 = 1·4/4 = 1" sub="the peak of the natural growth"
Where does the threshold come from? The natural growth peaks at half of K, where it equals r K over four. A harvest above that peak is more than the population can replace at any size. Here that's one times four over four, one.

@art moving-line
Raise the harvest line, and its two crossings with the hump slide together. At the peak they meet in one point. Above it, the line misses the hump entirely.

@art collapse
At five quarters the rate is negative everywhere, and every start falls without bound, even below zero, since the equation doesn't know a population can't be negative. Read a negative value as the stock already gone.

@chapter Where people slip
@list heading="Common slips" items="Any harvest below the growth is safe@The first|Expecting a gradual decline@The second|Treating negative values as fish@The third"
The first slip is believing any harvest below the natural growth is sustainable. At nine tenths it isn't. The second is expecting the population to shrink gradually as the harvest grows. The stable level goes four, three, two. Then, past one, there's nothing left to settle on. The third is treating the negative values as a population.

@chapter Try it
@words text="y′ = y·(1 − y/4) − 3/4" sub="what happens from 2? from 4? from 1/2?"
Your turn. With a harvest of three quarters, decide where a population starting at two goes, then one starting at four, then one starting at a half. Use the signs of the rate between the equilibria one and three.

@end text="Find the threshold"
You can raise the harvest and watch the two equilibria meet and vanish, on Learn. That's learn dot get er done dot I O.
