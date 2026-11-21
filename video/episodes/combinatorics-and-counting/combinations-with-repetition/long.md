---
format: long
lesson: combinatorics-and-counting/combinations-with-repetition
title: Stars and bars: choosing with repetition, explained
thumb: n types need n − 1 bars
---

@chapter Choosing with repeats
@title text="Combinations with Repetition" sub="Stars and bars" art=thumb
A shop sells three kinds of doughnut, and you want five. You can take several of the same kind, and the order you pick them in doesn't matter. How many different boxes could you end up with?

@art doughnut-box
A selection like this is really just a count for each kind: how many glazed, how many jam, how many chocolate. So choosing five doughnuts from three kinds is solving x one plus x two plus x three equals five, in non negative integers.

@chapter Stars and bars
@art stars-bars
Here's the trick. Write each selection as a row of five stars and two bars. Stars before the first bar are glazed, stars between the bars are jam, and stars after the second bar are chocolate. Two glazed, no jam, three chocolate is star star, bar, bar, star star star.

@art empty-group
Empty groups are allowed. Two bars side by side just means none of that kind. Every selection gives exactly one row, and every row gives exactly one selection. So counting selections is counting rows.

@math heading="Five doughnuts, three kinds" items="5 stars + 2 bars = 7 symbols@seven symbols;;choose where the stars go: C(7, 5) = 21@twenty one"
A row is seven symbols, five of them stars. Choosing where the stars go is C of seven, five, which is twenty one.

@math heading="r items from n types" items="r stars, n − 1 bars@n minus one bars;;C(n + r − 1, r)@C of n plus r minus one"
In general, choosing r items from n types, with repetition and without order, takes r stars and n minus one bars. That's C of n plus r minus one, r.

@words text="n types → n − 1 bars" sub="n bars gives C(n + r, r), which is wrong"
Notice it's n minus one bars, not n. The bars go between the groups. Using n bars is the standard error, and it gives C of n plus r, r instead.

@chapter Lower bounds
@math heading="Positive solutions" items="every xᵢ ≥ 1@at least one;;give each variable 1 first@Give each variable one;;C(r − 1, n − 1)@C of r minus one"
What if every variable must be at least one? Give each variable one up front. That leaves r minus n to share out freely, which is the same problem again. The count comes out as C of r minus one, n minus one.

@art pre-assign
That trick works for any lower bound. Take x one plus x two plus x three equals twelve, with each at least two. Pre assign two to each, and substitute y i equals x i minus two. Each y is then at least zero, and the total shrinks by six.

@math heading="x₁ + x₂ + x₃ = 12, each xᵢ ≥ 2" items="y₁ + y₂ + y₃ = 12 − 6 = 6@twelve minus six;;C(3 + 6 − 1, 6) = C(8, 6) = 28@twenty eight;;without the bound: C(14, 12) = 91@ninety one"
Now y one plus y two plus y three equals twelve minus six, which is six. The count is C of eight, six, twenty eight. Without the constraint, it would be C of fourteen, twelve, ninety one.

@words text="lower bounds: free · upper bounds: inclusion–exclusion"
Lower bounds are free: pre assign and shrink the total. Upper bounds are not. Counting solutions with each x at most five means subtracting the violations, and that's inclusion and exclusion.

@chapter The four rules
@art four-quadrants
Now you have all four basic rules, and every basic counting problem in this course is one of them. Ordered without repetition is P of n, r. Unordered without repetition is C of n, r. Ordered with repetition is n to the r. And unordered with repetition is stars and bars.

@math heading="n = 5, r = 3" items="P(5, 3) = 60@sixty;;C(5, 3) = 10@ten;;5³ = 125@a hundred and twenty five;;C(7, 3) = 35@thirty five"
At n equals five and r equals three, they give sixty, ten, a hundred and twenty five, and thirty five. Classifying correctly matters far more than computing carefully.

@chapter Where people slip
@art labelled-boxes
Stars and bars needs interchangeable items and distinct types. Identical balls into labelled boxes is fine. Distinct objects into boxes is a different count, the multinomial one.

@list heading="Common slips" items="Using n bars instead of n − 1@The first|Applying it to distinguishable items@The second|Handling an upper bound by substitution@And the third"
The first slip is using n bars instead of n minus one. The second is applying stars and bars to distinguishable items. And the third is trying to handle an upper bound by substitution.

@chapter Try it
@words text="8 identical balls into 4 labelled boxes" sub="as an equation, as stars and bars, then compute"
Your turn. How many ways can you put eight identical balls into four labelled boxes? Restate it as an equation, then as a stars and bars diagram, then compute. All three descriptions are the same problem, and seeing that is the point.

@end text="List all twenty-one doughnut boxes"
You can list all twenty one doughnut boxes and match each one to its row of stars and bars, on Learn. That's learn dot get er done dot I O.
