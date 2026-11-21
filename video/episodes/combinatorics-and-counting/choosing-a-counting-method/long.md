---
format: long
lesson: combinatorics-and-counting/choosing-a-counting-method
title: How to choose a counting method, and check your answer
thumb: Classify, compute, check
---

@chapter Classify first
@title text="Choosing a Counting Method" sub="Combinatorics and Counting" art=thumb
Most counting errors aren't arithmetic errors. They're classification errors: a correct calculation of the wrong quantity. So this lesson is a procedure. Classify the problem, apply the rule, then verify. Two sentences of classification, said out loud, prevent most wrong answers.

@chapter Order and repetition
@art decision-fork
Start with two questions. Does order matter? Ask what makes two outcomes different. If rearranging the same objects gives a new outcome, order matters: podiums and passwords, yes; committees and hands, no. And is repetition allowed? If an object can be used twice, it is.

@art rule-grid
Those two answers pick one of four formulas. Order without repetition: P of n, r. No order, no repetition: C of n, r. Order with repetition: n to the r. And no order, with repetition: C of n plus r minus one, r.

@math heading="n = 5, r = 3" items="P(5, 3) = 60@sixty;;C(5, 3) = 10@ten;;5³ = 125@a hundred and twenty five;;C(7, 3) = 35@thirty five"
At n equals five and r equals three, they give sixty, ten, a hundred and twenty five and thirty five. Four different answers, to four different questions.

@chapter Restrictions
@list heading="Restrictions" items="Constrained position → choose it first@constrained position|Varying counts → split into cases@cases|At least one → complement@complement|Overlapping conditions → inclusion–exclusion@Overlapping|Adjacency required → glue into a block@glue|Adjacency forbidden → arrange others, choose gaps@choose gaps"
Then handle the restrictions. A constrained position: choose it first. Varying counts: split into cases. At least one: count the complement. Overlapping conditions: inclusion and exclusion. Adjacency required: glue into a block. Adjacency forbidden: arrange the others, then choose gaps.

@chapter The toolkit
@art toolkit-tray
Some problems have a shape you'll recognise. Identical objects into distinct boxes is stars and bars. Distinct objects into distinct boxes is a multinomial coefficient. Circular seating is n minus one factorial. No fixed points is a derangement.

@words text="every n → generating function · identity → double count · existence → pigeonhole"
If you need the answer for every n, try a generating function. If you have an identity to prove, double count or find a bijection. And if the question is whether something exists, rather than how many, think pigeonhole.

@chapter One problem, fully classified
@math heading="5-letter strings: no repeat, at least one vowel" items="order? yes · repetition? no ⟹ P(26, 5)@P of twenty six, five;;all: 26·25·24·23·22 = 7 893 600@seven million"
Five letter strings, with no repeated letter and at least one vowel. Order matters and repetition doesn't, so the base rule is P of twenty six, five: seven million, eight hundred and ninety three thousand, six hundred.

@math items="no vowel: P(21, 5) = 2 441 880@no vowel;;answer: 7 893 600 − 2 441 880 = 5 451 720@five million"
At least one vowel means complement. With no vowel, it's P of twenty one, five: two million, four hundred and forty one thousand, eight hundred and eighty. Subtract, and you get five million, four hundred and fifty one thousand, seven hundred and twenty.

@math heading="Check" items="5 451 720 < 7 893 600  ✓@smaller;;1 − 2441880/7893600 ≈ 0.691  ✓@point six nine one;;small case: P(4,2) − P(3,2) = 12 − 6 = 6@small case"
Now check. It's smaller than the total. The proportion is about point six nine one: plausible, with five vowels and five chances to hit one. And a small case: length two from a, b, c and d, with vowel a, gives twelve minus six, which is six.

@art magnifier-list
List them: a b, b a, a c, c a, a d, d a. Six. Listing takes ten seconds, and it confirms the formula counts what you meant, which no amount of re reading the arithmetic can.

@chapter Verify
@list heading="Verify" items="Shrink and enumerate@Shrink|Count a second way@second way|Check the magnitude@magnitude|Check the extremes@extremes"
So the last step is always to verify. Shrink the problem and enumerate. Count a second way, so cases and complement agree. Check the magnitude: never above the unrestricted count, never below zero. And check the extremes, r equals zero and r equals n.

@art two-routes-agree
Wrong classifications feel exactly as sound as right ones. That's what makes them dangerous, and it's why the check is worth doing, even when the reasoning felt fine.

@art boundary-ruler
A formula checked at its boundaries, and against one small list, is very unlikely to be the right calculation of the wrong quantity. That's the habit worth keeping.

@chapter Try it
@words text="PINs · podium · hands · doughnuts · BANANA" sub="order? repetition? then the rule"
Your turn. Take five problems from this course: four digit PINs, a podium from ten runners, five card hands, five doughnuts from three kinds, and the arrangements of BANANA. For each, answer order and repetition before computing anything. Then verify the doughnuts by listing them.

@end text="All four rules, side by side"
You can see all four rules side by side, with the lists behind them, on Learn. That's learn dot get er done dot I O.
