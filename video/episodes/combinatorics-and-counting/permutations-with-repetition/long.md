---
format: long
lesson: combinatorics-and-counting/permutations-with-repetition
title: Permutations with repetition: n to the r, and MISSISSIPPI
thumb: Divide out the identical copies
---

@chapter Two problems, one name
@title text="Permutations with Repetition" sub="Combinatorics and Counting" art=thumb
Two different situations share this name. In one, you draw from a set and you're allowed to repeat. In the other, you arrange objects that are already repeated, like the letters of a word. They have different answers, so it pays to tell them apart.

@chapter Drawing with replacement
@art open-slots
First, sequences of length r from n options, with repetition allowed. Each position is filled independently, with all n options available every time. The product rule gives n times n, and so on, r times.

@math heading="Ordered, repetition allowed" items="n · n ⋯ n = nʳ@n to the r;;length 4 from {a, b, c}: 3⁴ = 81@eighty one"
That's n to the r. Strings of length four from a, b and c: three to the fourth, eighty one. Watch the base and the exponent. Four cubed, sixty four, is the classic swap.

@words text="functions from an r-set to an n-set: nʳ" sub="{0,1}ⁿ has 2ⁿ elements"
It's also the number of functions from an r element set to an n element set, and of strings of length r over an alphabet of size n. That's why the bit strings of length n number two to the n.

@chapter Arranging a multiset
@art letter-tiles
Now the other problem. How many distinguishable ways can you arrange the letters of MISSISSIPPI? Eleven letters: one M, four I's, four S's and two P's.

@art swap-identical
Pretend for a moment that the copies are labelled, so all eleven letters are distinct. Then there are eleven factorial arrangements. But swap two identical S's, and the word doesn't change. Each real arrangement was counted once for every way of permuting the labels within each letter.

@math heading="MISSISSIPPI" items="11! / (1! · 4! · 4! · 2!)@eleven factorial over;;= 39 916 800 / 1152@thirty nine million;;= 34 650@thirty four thousand six hundred and fifty"
So divide. Eleven factorial over one factorial, four factorial, four factorial and two factorial. That's thirty nine million, nine hundred and sixteen thousand, eight hundred, over one thousand one hundred and fifty two: thirty four thousand six hundred and fifty.

@math heading="n objects of k types" items="n! / (n₁! n₂! ⋯ n_k!)@n factorial over"
In general, it's n factorial over the factorial of each repetition count. The divisor is the symmetry you're dividing out, just like the rotations at a round table.

@chapter Same problem, different clothes
@art in-out-row
Choosing a subset is a two type arrangement. Arrange r copies of in and n minus r copies of out, and you get n factorial over r factorial times n minus r factorial. That's exactly C of n, r.

@art card-deal
The same formula distributes objects into labelled boxes. Deal fifty two cards to four players, thirteen each: fifty two factorial over thirteen factorial to the fourth, about five point three six times ten to the twenty eight. Giving each card a player is arranging thirteen copies of four labels.

@chapter No two adjacent
@math heading="BANANA" items="3 A, 2 N, 1 B@three A's;;6! / (3! · 2! · 1!) = 720 / 12 = 60@sixty"
How many arrangements of BANANA have no two A's next to each other? BANANA has three A's, two N's and one B. All arrangements: six factorial over three factorial times two factorial. Seven hundred and twenty over twelve, which is sixty.

@art gap-insert
Place the letters that aren't A first. B, N, N can be arranged in three ways. That creates four gaps, including the two ends. Then choose three of the four gaps for the A's, and no two of them can touch.

@math heading="No two A’s adjacent" items="arrange B, N, N: 3!/2! = 3@Three ways;;choose the gaps: C(4, 3) = 4@which is four;;3 × 4 = 12@Twelve;;60 − 12 = 48 have two A’s together@forty eight"
Three ways, times C of four, three, which is four. Twelve arrangements with no two A's adjacent. So forty eight of the sixty do have two A's together.

@chapter Where people slip
@list heading="Common slips" items="Confusing the two situations@The first|Missing a repeated letter@The second|Counting m − 1 gaps instead of m + 1@And the third"
The first slip is confusing the two situations. Drawing with repetition gives n to the r; arranging repeated objects gives a quotient. The second is missing a repeated letter, so count each one before dividing. And the third is the gap count: m objects make m plus one gaps, counting both ends.

@chapter Try it
@words text="MISSISSIPPI, no two S’s adjacent" sub="arrange the other 7, then choose 4 gaps"
Your turn. Count the arrangements of MISSISSIPPI with no two S's adjacent. Arrange the other seven letters, count the gaps, and choose four of them. Both halves, the arrangement and the gaps, are this lesson.

@end text="Find aab, aba and baa"
You can find the three arrangements of a, a, b in the full list of strings, on Learn. That's learn dot get er done dot I O.
