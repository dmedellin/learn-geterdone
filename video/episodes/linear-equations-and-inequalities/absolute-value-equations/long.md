---
format: long
lesson: linear-equations-and-inequalities/absolute-value-equations
title: Absolute value equations: two cases, and when there are none
thumb: Two places at distance k
---

@chapter A distance
@title text="Absolute Value Equations" sub="Linear Equations and Inequalities" art=thumb
Absolute value equations usually have two answers. Sometimes one, sometimes none. Once you read the bars as a distance, you'll always know which, and why.

@art distance-two
The absolute value of a is the distance from a to zero on the number line. No direction, just how far. So which numbers are at distance five from zero? Five, and minus five. There are no others.

@words text="|−4| = −(−4) = 4" sub="the minus reverses a sign, it doesn't impose one"
In cases, the absolute value of a is a when a is at least zero, and minus a when a is negative. That second case is easy to misread. If a is minus four, then minus a is minus minus four, which is four. The minus reverses a sign. It doesn't impose one.

@chapter The two-case rule
@list heading="|X| = k" items="k > 0:  X = k or X = −k@positive|k = 0:  X = 0@is zero|k < 0:  no solution@is negative"
Here's the rule. If k is positive, the absolute value of X equals k exactly when X equals k, or X equals minus k. If k is zero, X must be zero, a single case. And if k is negative, it's never true, because a distance is never negative.

@art bars-enclose
X can be any expression, like x minus three or two x plus one. The rule applies to the whole of what the bars enclose, not just to x.

@chapter Bars alone first
@math heading="3|x − 1| + 2 = 14" items="3|x − 1| = 12@subtract two;;|x − 1| = 4@divide by three"
Take three times the absolute value of x minus one, plus two, equals fourteen. The bars aren't alone yet, so isolate them. Subtract two: three times the absolute value equals twelve. Divide by three: the absolute value of x minus one equals four.

@art isolate-bars
That step isn't tidying up. The rule is stated for bars standing alone. Split too early and you produce numbers that fail the check.

@art split-two
Now split. Two cases means two equations, joined by or. x minus one equals four, or x minus one equals minus four. So x is five, or x is minus three.

@words text="{ 5, −3 }" sub="both check: 3(4) + 2 = 14"
Check both. Five gives three times four plus two, which is fourteen. Minus three gives the same. Both belong in the answer. Reporting just one isn't a smaller answer. It's a wrong one, because two numbers make the statement true.

@chapter When it isn't two
@math heading="Other counts" items="|2x + 1| = 0  →  x = −1/2@distance of zero;;|x + 4| = −2  →  no solution@x plus four equals minus two;;|x − 3| = |2x + 1|  →  x = −4, x = 2/3@equal or opposite"
A distance of zero happens in one place only, so the absolute value of two x plus one equals zero gives x equals minus one half. The absolute value of x plus four equals minus two has none. And two absolute values are equal when the insides are equal or opposite: minus four and two thirds.

@art no-solution-check
The no solution case repays a closer look. Split it mechanically anyway, and you get minus six and minus two. Substitute them. Both give an absolute value of two, and neither equals minus two. The split produced two numbers, and neither is a solution. That's exactly what the check is for.

@chapter A variable on the right
@math heading="|2x − 1| = x + 3" items="2x − 1 = x + 3  →  x = 4@case one;;check: |7| = 7 and 4 + 3 = 7@seven;;2x − 1 = −(x + 3)  →  x = −2/3@case two;;check: |−7/3| = 7/3 and −2/3 + 3 = 7/3@seven thirds"
When the right side contains x, its sign is unknown, so there's no guarantee. Split anyway, and check every candidate. Case one: two x minus one equals x plus three, so x is four. Both sides are seven. Case two: two x minus one equals minus x minus three, so x is minus two thirds. Both sides are seven thirds.

@art extraneous
Here both survived. But a candidate that fails the check is called extraneous. It isn't the mark of an arithmetic slip. The split can produce solutions the original never had, and only substitution finds out which.

@chapter Where people slip
@list heading="Common slips" items="Splitting before the bars are alone@The first|Reporting only one case@The second|Trusting the split when k isn't positive@The third"
Three slips. The first is splitting before the bars are alone. The absolute value of x, plus three, equals seven, is not x plus three equals seven or minus seven. That gives minus ten, which fails. The second is reporting only one case. The third is trusting the split when the right side isn't a positive number.

@chapter Try it
@words text="|x − 3| = 5" sub="find both solutions"
For practice, solve the absolute value of x minus three equals five. Eight is one answer. Don't stop there. Find the other, and check both in the original.

@end text="Split, then check"
You can split and check absolute value equations yourself on Learn. That's learn dot get er done dot I O. See you in the next one.
