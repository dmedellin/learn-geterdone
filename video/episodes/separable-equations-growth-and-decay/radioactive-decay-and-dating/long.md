---
format: long
lesson: separable-equations-growth-and-decay/radioactive-decay-and-dating
title: Radioactive decay and dating: counting half-lives
thumb: A quarter left means two half-lives
---

@chapter The question
@title text="Radioactive Decay and Dating" sub="Separable Equations, Growth and Decay" art=thumb
How can the amount of something left in a sample tell you its age? Carbon dating rests on one observation, and the rest is the growth equation run backwards.

@art atoms
A radioactive atom has the same chance of decaying in any given year, whatever its age. So the number of atoms that decay in a year is proportional to the number still there. That's a rate proportional to the size, with the direction reversed.

@chapter The decay equation
@math heading="Radioactive decay" items="y′ = −k·y,  k > 0@y prime equals minus k y;;y = y₀·e^(−kt)@the solution;;e^(−kT) = 1/2@halved when;;k·T = ln 2@k times T"
Write it as y prime equals minus k y, with k positive, so k is the size and the minus sign carries the direction. The solution is y nought times e to the minus k t. It has halved when e to the minus k T is one half, and taking logarithms gives k times T equals ln two.

@art decay-curve
Each half life takes the same time, whatever amount you start from, just like doubling.

@words text="T = ln 2/k    k = ln 2/T"
So a half life and a rate are one fact. Give either and the other follows. And because ln two is irrational, a measured half life gives a rounded rate, and a rational rate gives a rounded half life.

@chapter The lab's rate
@math heading="k = 3/25000 per year" items="T = (25000/3)·ln 2@twenty five thousand over three;;≈ 5776.23 years@about five thousand"
A half life for carbon fourteen is commonly quoted as about five thousand seven hundred thirty years. The lab instead uses k equals three over twenty five thousand per year. Then T is twenty five thousand over three, times ln two, about five thousand seven hundred seventy six years.

@words text="close to the measured value, not equal" sub="chosen so every Euler step is exact"
That's close to the measured half life, and not equal to it. A rational rate keeps every Euler step exact. The difference is the cost of that choice, so the lab's age shouldn't be read as a measurement.

@chapter From what's left to an age
@art halving-squares
Each half life halves what's there. After one, a half is left. After two, a quarter. After three, an eighth. So a fraction that's a power of one half just counts half lives.

@math heading="Age from the fraction left" items="e^(−kt) = f@e to the minus k t;;t = ln(1/f)/k@the age is;;1/8 < 15% < 1/4@fifteen percent;;so 2T < age < 3T@between two"
In general, if a fraction f is left, then e to the minus k t equals f, and the age is ln of one over f, over k. But a quick bracket needs no logarithm. Fifteen percent left lies between an eighth and a quarter, so the age is between two and three half lives.

@art age-bracket
That bracket comes before any rounded figure. A rounded answer outside it is wrong.

@chapter The exact sequence
@math heading="A quarter left,  h = 200 years" items="age = 2T ≈ 11552.5 years@twice the half life;;Euler: step 58,  t = 11600@step fifty eight"
With a step of one century, the Euler factor is two hundred forty seven over two hundred fifty, exact. Now aim for a quarter, with a step of two hundred years. The age is twice the half life, about eleven thousand five hundred fifty two point five years. The sequence gets there at step fifty eight, eleven thousand six hundred, within one step.

@math heading="Round numbers: rate 1/4" items="factor 3/4@three quarters;;(3/4)² = 9/16 > 1/2@nine sixteenths;;(3/4)³ = 27/64 < 1/2@twenty seven;;half-life 4·ln 2 ≈ 2.77259@four ln two"
The same arithmetic with round numbers. A rate of a quarter, start at a hundred, target fifty. The factor is three quarters. Three quarters squared is nine sixteenths, still above a half. Cubed, it's twenty seven sixty fourths, below it. So the sequence crosses at step three, while the half life is four ln two, about two point seven seven.

@chapter What dating assumes
@art sealed-sample
Say what dating assumes as plainly as what it computes. The sample began with a known amount. Nothing entered or left except by decay. And the rate constant hasn't changed. Whether those hold for a real sample is something no formula can tell you.

@chapter Where people slip
@list heading="Common slips" items="Two half-lives leave nothing@The first|Typing the decay rate as positive@The second|Taking 1/k for the half-life@The third"
The first slip is believing that after two half lives nothing is left. Half of a half is a quarter, not zero. The second is typing the decay rate without its minus sign, which makes a growth equation. The half life tile reads the same and hides it. The third is taking one over k for the half life.

@art one-over-e
One over k is twenty five thousand over three, about eight thousand three hundred thirty three years, the time to fall to one over e. The half life carries the factor ln two, so it's shorter. The check: k times T must equal ln two, not one.

@chapter Try it
@words text="1/8 left,  k = 3/25000" sub="how many half-lives? what age?"
Your turn. A sample has an eighth of its original amount left, with the lab's rate. Count the half lives, then use the half life of about five thousand seven hundred seventy six years to find the age.

@end text="Count the half-lives"
You can set the target and the step, and see where the exact sequence crosses, on Learn. That's learn dot get er done dot I O.
