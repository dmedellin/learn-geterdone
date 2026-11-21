---
format: long
lesson: dynamic-programming/combinations-or-ordered-sequences
title: Swap two loops, and 541 becomes a 23-digit number
thumb: Same cost, different question
---

@chapter The question
@title text="Combinations, or Ordered Sequences" sub="Dynamic Programming and Optimal Substructure" art=thumb
How many ways can you make a hundred from ones, twos and fives? Write the obvious table, and you'll get an answer. But swap its two loops, and the answer changes from five hundred and forty one to a twenty three digit number. Same cost. Different question.

@art multiset-vs-list
There are two things you might be counting. A combination is a multiset, how many of each coin, with no order. An ordered sequence is a list, where two lists that differ only in order are different. Once more than one coin type is used, the counts are never equal.

@chapter Counting with a sum
@words text="min → sum · base case 0 → 1"
Counting recurrences swap the minimum for a sum. And the empty amount has exactly one way to be made, take nothing, so the base case is one, not zero. Get that wrong, and every count is zero.

@math heading="Two recurrences" items="C(i, v) = C(i − 1, v) + C(i, v − c(i))@C of i, v;;S(v) = Σ over coins c ≤ v of S(v − c)@S of v"
C of i, v counts combinations from the first i coin types. Use none of coin i, and that's C of i minus one, v. Use at least one, remove a copy, and that's C of i, v minus c i. S of v splits on the last coin: the sum of S of v minus c, over coins that fit.

@chapter Five from 1, 2 and 5
@list heading="4 combinations" items="5@just a five|2 + 2 + 1@two plus two plus one|2 + 1 + 1 + 1@two plus one plus one plus one|1 + 1 + 1 + 1 + 1@five ones"
Make five from one, two and five. There are four combinations: just a five. Two plus two plus one. Two plus one plus one plus one. And five ones.

@math heading="9 ordered sequences" items="5  →  1@The five;;2 + 2 + 1  →  3 arrangements@three arrangements;;2 + 1 + 1 + 1  →  4 arrangements@four arrangements;;1 + 1 + 1 + 1 + 1  →  1@five ones;;1 + 3 + 4 + 1 = 9@nine"
Now count orderings. The five has just one. Two plus two plus one has three arrangements. Two plus one plus one plus one has four arrangements. And five ones has one. One plus three plus four plus one is nine.

@art arrangements
So the ratio between the two counts isn't a constant, and it isn't a factorial. It depends on how many copies of each coin each combination uses.

@chapter Which loop is outside
@art coins-outside
Here's the code difference. Put the coin types on the outside loop, and every combination is built in one fixed order: all the ones, then the twos, then the fives. A multiset has exactly one such order, so it's counted once.

@art amounts-outside
Put the amounts on the outside, and any coin can be the last one added at any step. So one then two, and two then one, are different histories, and both get counted. That's the count of ordered sequences.

@list heading="Coins 1, 2, 5  ·  amount 100" items="Coins outside: 541@Coins outside|Amounts outside: 91 197 869 007 632 925 819 218@Amounts outside|Both: 295 reads@Both loops"
For a hundred: coins outside gives five hundred and forty one. Amounts outside gives a twenty three digit number, about ninety one sextillion. Both loops read the table exactly two hundred and ninety five times. Same cells, same arithmetic, twenty orders of magnitude apart.

@art same-cost
There's no performance argument for either, and you can't tell them apart by watching them run. The defence is a second route: the panel runs a memo free recursion for each count, and lists the actual objects where they fit.

@chapter Twenty three digits
@art digit-strip
That answer has twenty three digits. The largest whole number a double holds exactly has sixteen, about nine quadrillion. In floating point, you'd print a number that's merely close, leading digits right, tail invented. So every count here is an exact big integer, never converted.

@words text="295 reads · Θ(nk) operations" sub="but each addition is 23 digits long"
And that bends the cost model. Theta of n k counts arithmetic operations as constant time. Here each addition is on numbers up to twenty three digits long, and on this instance, it's the addition that dominates.

@chapter Where people slip
@list heading="Common slips" items="Writing the sequence loop while meaning combinations@The first|Initialising the empty amount to zero@The second|Printing a count a double can't hold@The third"
The first slip is writing the sequence loop when you mean combinations. It feels natural, filling amounts left to right. The second is setting the empty amount to zero. The third is printing a count a double can't hold. It's wrong in its last seven digits, and nothing notices.

@chapter Try it
@words text="make 4 from 1 and 2"
Your turn. Make four from ones and twos. List the combinations, then all the ordered sequences. Then run both loop orders by hand and check each gives the count you listed.

@end text="Swap the loops yourself"
You can swap the two loops and see both counts and their objects, on Learn. That's learn dot get er done dot I O.
