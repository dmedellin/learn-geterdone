---
format: long
lesson: combinatorics-and-counting/sum-and-product-rules
title: The sum and product rules: when to add and when to multiply
thumb: Add for or, multiply for then
---

@chapter Two rules
@title text="The Sum and Product Rules" sub="Combinatorics and Counting" art=thumb
Almost all of counting rests on two rules. The arithmetic in them is easy. The hard part, and really the whole lesson, is deciding which one applies.

@art two-piles
The sum rule is for alternatives. If a task can be done in one of n one ways, or in one of n two ways, and no way appears in both lists, then there are n one plus n two ways in total.

@math heading="Sum rule" items="|A ∪ B| = |A| + |B|@the size of a union;;only when A ∩ B = ∅@only when"
In set language, the size of a union is the sum of the sizes, but only when the sets are disjoint, when nothing is in both. That condition is the part people forget.

@art branching-tree
The product rule is for stages. If a task is a first choice with n one options, and then, for each of those, a second choice with n two options, there are n one times n two ways. With more stages, you multiply all the stage counts.

@words text="|A × B| = |A| · |B|" sub="n yes-or-no choices → 2ⁿ truth-table rows"
That's where the size of a Cartesian product comes from. It's also why a truth table has two to the n rows: n successive yes or no choices.

@chapter Both in one problem
@art string-slots
Here's a problem that needs both rules. How many strings of length three, over the twenty six letters, start with a vowel or end with z?

@math items="vowel first: 5 · 26 · 26 = 3380@five times twenty six;;ends in z: 26 · 26 · 1 = 676@twenty six times twenty six times one"
Strings that start with a vowel: five times twenty six times twenty six, which is three thousand three hundred and eighty. Strings that end in z: twenty six times twenty six times one, six hundred and seventy six.

@art overlapping-circles
Adding those would give four thousand and fifty six. But the two sets overlap. A string can start with a vowel and end in z, and the sum rule would count it twice.

@math heading="Remove the overlap" items="both: 5 · 26 · 1 = 130@five times twenty six times one;;3380 + 676 − 130 = 3926@three thousand nine hundred and twenty six"
There are five times twenty six times one of those, a hundred and thirty. Subtract them once, and the answer is three thousand nine hundred and twenty six, not four thousand and fifty six.

@words text="over-count = the overlap" sub="inclusion–exclusion, arriving early"
Using the sum rule on sets that overlap over counts by exactly the size of the overlap. That subtraction is the inclusion exclusion principle arriving early. It gets a lesson of its own later in the course.

@chapter When the second count varies
@words text="26 · 25 = 650" sub="ordered pairs of distinct letters"
People often say the product rule needs independent choices. That's imprecise. What it needs is that the number of second choices is the same, whichever first choice you made. An ordered pair of distinct letters has twenty six first choices, and always twenty five second ones. That's six hundred and fifty.

@art case-split
When the second count really does change with the first, split into cases where it doesn't. Count each case with the product rule, then add the cases with the sum rule. That repair is what makes the two rules a complete toolkit.

@chapter Count the complement
@art complement-box
Sometimes the things you want are hard to count, and the things you don't want are easy. Then count the failures, and subtract them from the total.

@math heading="PINs with at least one 7" items="all: 10⁴ = 10000@ten to the fourth;;no 7: 9⁴ = 6561@nine to the fourth;;10000 − 6561 = 3439@three thousand four hundred and thirty nine"
How many four digit PINs contain at least one seven? All PINs: ten to the fourth, ten thousand. PINs with no seven: nine to the fourth, six thousand five hundred and sixty one. So the answer is three thousand four hundred and thirty nine.

@words text="“at least one” → total − none"
Counting that directly would need cases for one, two, three or four sevens. At least one is almost always a signal to count the complement. Total minus none is one subtraction, and it can't double count.

@chapter Both rules at scale
@math heading="Passwords: length 6 to 8, at least one digit" items="length 6: 36⁶ − 26⁶@length six;;length 7: 36⁷ − 26⁷@seven;;length 8: 36⁸ − 26⁸@and eight;;total = 2 684 483 063 360@about two point six eight trillion"
Passwords of length six to eight, from twenty six letters and ten digits, with at least one digit. A password has exactly one length, so split by length six, seven and eight, and add. Inside each length, take every string minus the all letter ones. The total is about two point six eight trillion.

@chapter Where people slip
@list heading="Common slips" items="Adding when the cases overlap@The first|Multiplying when the second count varies@The second|Counting “at least one” directly@And the third"
The first slip is adding when the cases overlap; the over count is exactly the size of the intersection. The second is multiplying when the second count varies; split into cases instead. And the third is counting at least one directly, which almost always makes overlapping cases.

@chapter Try it
@words text="4-digit PINs with at least two identical digits" sub="by complement, then say why"
Your turn. Count the four digit PINs with at least two identical digits. Do it by complement, and then say, in one sentence, why the direct count would be harder. That sentence is the skill.

@end text="Check the product rule by listing"
You can list all one hundred and twenty five strings behind the product rule and check the formula yourself, on Learn. That's learn dot get er done dot I O.
