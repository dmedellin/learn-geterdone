---
format: long
lesson: intro-algorithms-strings-geometry-hardness/set-cover-randomization-and-subset-sum
title: Greedy set cover, random assignments and trimming subset sums
thumb: Trade time for accuracy
---

@chapter Three kinds of guarantee
@title text="Set Cover, Randomization and Subset Sum" sub="Introduction to Algorithms, Sections 35.3–35.5" art=thumb
The last sections of the read along offer three new kinds of guarantee: a ratio that grows slowly with the input, a ratio that holds on average, and a ratio you can buy down with time.

@chapter Greedy set cover
@art set-family
Set cover gives you a finite set X and a family of subsets whose union is X. Find the smallest subfamily that still covers X. It generalizes vertex cover, so it's NP hard. Greedy repeatedly takes the set covering the most elements not yet covered.

@art charges
To bound it, charge each element one over k when it's first covered by a set that brings in k new elements. The charges add up to the number of sets greedy takes. And the elements of any one set pay at most the harmonic number of its size in total.

@math heading="Theorem 35.4" items="H(d) = 1 + 1/2 + … + 1/d@the harmonic number;;ratio ≤ H(max |S|) ≤ ln |X| + 1@gives the bound"
The harmonic number H of d is one plus a half, plus a third, up to one over d. That gives the bound.

@art harmonic-steps
Summing over an optimal cover, greedy is within H of the largest set's size, which is at most the natural log of the size of X, plus one.

@math heading="1 2 3 4 · 5 6 7 8 · 1 2 5 6 7" items="S3 first: 5 new, 1/5 each@takes S three;;S1: adds 3, 4 at 1/2 each@then S one;;S2: adds 8, charged 1@then S two;;charges 3 · optimum 2 · ratio 3/2@add to three"
On the lesson's family, greedy takes S three first, five new elements at a fifth each. Then S one, adding three and four at a half each. Then S two, adding only eight, charged one. The charges add to three, the optimum is two, and the ratio is three halves. The book's bound is two times H of five, about four point five seven.

@chapter A random assignment
@art coin-flips
For max three CNF satisfiability, set each variable true with probability one half. A clause of three distinct literals fails only if all three are false, with probability one eighth. By linearity of expectation, seven eighths of the clauses are satisfied on average.

@words text="expected ratio ≤ 8/7" sub="Theorem 35.6"
No assignment satisfies more than all of them, so the expected ratio is at most eight sevenths. That's about the algorithm's coin flips, on average, not a promise for every run.

@art lp-rounding
A second technique is linear programming. Relax weighted vertex cover to fractions between zero and one, solve it, and take every vertex whose value is at least a half. Every edge forces one end to a half or more, and rounding at most doubles the cost.

@chapter Trimming subset sums
@quote text="That is, we can trade computation time for the quality of the approximation." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 35"
The chapter's opening says this of approximation schemes. That is, we can trade computation time for the quality of the approximation.

@art trimmed-list
Subset sum here asks for the largest subset sum not exceeding t. The exact method keeps every reachable sum, and the list can double with each element. The scheme trims it: drop any sum within a factor one plus delta of a sum already kept, with delta equal to epsilon over two n.

@math heading="S = {12, 20, 31, 45} · t = 70 · ε = 0.4 · δ = 0.05" items="after 31: drop 32, since 32 ≤ 1.05 · 31@drops thirty two;;after 45: drop 45 and 65@forty five and sixty five;;kept: 0, 12, 20, 31, 43, 51, 57, 63@It keeps;;answer 63 · optimum 65@the answer"
On the lesson's numbers, after thirty one the list drops thirty two, within five per cent of thirty one. After forty five, it drops forty five and sixty five. It keeps zero, twelve, twenty, thirty one, forty three, fifty one, fifty seven and sixty three. So the answer is sixty three, against an optimum of sixty five.

@words text="lost ≈ 3% · allowed 40%" sub="65 was within 5% of 63"
The trim threw away the optimum itself, because sixty three was within five per cent of it. The answer lost about three per cent, where epsilon allowed forty.

@chapter Where people slip
@list heading="Common slips" items="Greedy must be optimal@The first|8/7 holds on every run@The second|Accuracy is free@the third"
The first slip is expecting greedy to be optimal because it's greedy. Here its first choice is in no optimal cover. The second is reading eight sevenths as a guarantee on every run. And the third is thinking accuracy is free. Each halving of epsilon roughly doubles the lists and the time.

@chapter Try it
@code block=1 lines=1-1 focus="1@three sets"
Your turn. Run greedy set cover by hand on these three sets, giving the charge each element pays. Find the optimum, the realised ratio, and the book's bound, two times H of the largest set's size.

@end text="Charge every element"
You can run greedy set cover and add up the charges, on Learn. That's learn dot get er done dot I O.
