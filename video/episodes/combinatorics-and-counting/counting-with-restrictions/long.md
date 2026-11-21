---
format: long
lesson: combinatorics-and-counting/counting-with-restrictions
title: Counting with restrictions: constrain first, split, or complement
thumb: Handle the hard position first
---

@chapter Why restrictions hurt
@title text="Counting with Restrictions" sub="Combinatorics and Counting" art=thumb
Restrictions make counting harder in one specific way. They break the product rule's promise that each stage has the same number of options, whatever came before. There are three repairs: apply the constraint first, split into cases, or count the complement.

@chapter Constrain first
@art digit-dials
How many four digit numbers are there? The first digit can't be zero, so choose it first: nine ways. Then ten, ten and ten for the rest.

@math items="9 · 10 · 10 · 10 = 9000@nine thousand;;✗  10⁴ counts 0123@ten to the fourth"
That's nine thousand. Work left to right without noticing the restriction, and you get ten to the fourth, which counts zero one two three as a four digit number.

@art two-ends
Now two constraints at once: the first digit is nonzero, and the last digit is even. Deal with both ends first. Nine for the first, five for the last, then ten and ten in the middle.

@math items="9 · 10 · 10 · 5 = 4500@four thousand five hundred"
That's four thousand five hundred. You can consider the positions in any order you like. What you can't change is which position each count belongs to.

@chapter A value comes back
@math heading="First digit nonzero, all digits distinct" items="9 · 9 · 8 · 7 = 4536@four thousand five hundred and thirty six"
Four digit numbers with a nonzero first digit and all digits distinct. Nine choices for the leading digit, then nine, then eight, then seven. That's four thousand five hundred and thirty six.

@art freed-value
Notice the second count is nine, not eight. The second digit can be anything except the first, and that includes zero. Zero becomes available exactly because it was kept out of the first position.

@chapter Split into cases
@art disjoint-cases
Sometimes two restrictions genuinely interact, and cases can't be avoided. How many strings of length four, over a, b and c, have at least two a's? Split by the number of a's. A string has one definite number of them, so the cases are disjoint.

@math heading="At least two a’s, by cases" items="exactly two: 6 · 4 = 24@exactly two;;exactly three: 4 · 2 = 8@exactly three;;exactly four: 1@all four;;24 + 8 + 1 = 33@thirty three"
Exactly two: six ways to pick their positions, and two times two for the others, so twenty four. Exactly three: four places for the one letter that isn't an a, and it's b or c, so eight. All four: one string. Total, thirty three.

@chapter Count the complement
@art complement-cut
Now the same question by complement. There are three to the fourth, eighty one strings in all. The ones that fail have zero a's or exactly one.

@math heading="At least two a’s, by complement" items="no a: 2⁴ = 16@no a at all;;exactly one: 4 · 2³ = 32@exactly one;;81 − 16 − 32 = 33@eighty one minus"
With no a at all: two to the fourth, sixteen. With exactly one: four positions times two cubed, thirty two. Eighty one minus sixteen minus thirty two is thirty three. Same answer.

@art two-routes
Two independent routes to thirty three. That agreement is the real check. One method giving a plausible number is no evidence that the classification was right.

@math heading="5-digit PINs with a repeated digit" items="all: 10⁵ = 100000@a hundred thousand;;all distinct: 10 · 9 · 8 · 7 · 6 = 30240@thirty thousand two hundred and forty;;100000 − 30240 = 69760@sixty nine thousand"
The complement is at its best on at least conditions. Five digit PINs with at least one repeat: a hundred thousand in all. All distinct: thirty thousand two hundred and forty. That leaves sixty nine thousand seven hundred and sixty.

@words text="“at least” → complement  ·  “exactly” → cases"
A useful signal. If the condition says at least, or not all, or some, the complement is usually one clean count. If it says exactly, cases are usually right.

@chapter Slips and checks
@list heading="Common slips" items="Ignoring the leading-digit restriction@ignoring|Forgetting a value freed for later@freed|Cases with an overlap or a gap@a gap"
Three slips are common. Ignoring the leading digit restriction. Forgetting that a value kept out of one position is freed for another. And cases with an overlap or a gap, which are both silent errors. Check that the cases add up to the unrestricted total once the restriction is removed.

@list heading="Before you trust it" items="Do the cases overlap?@overlap|Do they cover everything?@cover everything|Does a small instance check out?@small instance"
Before you trust a count, ask three things. Do the cases overlap? Then something was counted twice. Do they cover everything? A missing case is an undercount that never announces itself. And does a small instance check out, once you shrink it enough to list by hand?

@chapter Try it
@words text="4-digit numbers with at least one 7" sub="by complement, and by the position of the first 7"
Your turn. Count the four digit numbers, leading digit nonzero, that contain at least one seven. Do it by complement, and by cases on the position of the first seven. If the two totals agree, you have both the arithmetic and the classification right.

@end text="Check a count against the list"
You can check a restricted count against a full list of the objects, on Learn. That's learn dot get er done dot I O.
