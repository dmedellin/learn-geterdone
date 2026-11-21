---
format: long
lesson: intro-algorithms-foundations/solving-recurrences
title: Solving recurrences: substitution, trees and the master theorem
thumb: Root against the leaves
---

@chapter Three methods
@title text="Solving Recurrences" sub="Introduction to Algorithms, Sections 4.3 to 4.5" art=thumb
Divide and conquer algorithms come with recurrences, like T of n equals two T of n over two plus n. Chapter four gives three ways to solve them. Two work widely and ask more of you. The third is quick, and has gaps.

@chapter Substitution
@art guess-and-prove
The substitution method has two steps. Guess the form of the solution, then prove it by induction, finding constants that make it hold. The guess is substituted for T on the smaller arguments, which gives the method its name.

@math heading="A false proof" items="T(n) ≤ 2c·(n/2) + n@two c times n over two;;= c·n + n@c n plus n;;✗  = O(n)@O of n"
Watch out for this one. From T of n at most two c times n over two, plus n, you get c n plus n. It's tempting to call that O of n and stop. But the induction promised T of n at most c n, with the same c, and c n plus n is bigger than that.

@words text="Subtract a lower-order term" sub="a stronger guess, an easier induction"
And when a guess is right in form but fails by a lower order term, the cure is surprising. Subtract a lower order term from the guess. That makes the induction stronger, not weaker.

@chapter Recursion trees
@art recursion-tree-levels
The recursion tree draws each call as a node, labelled with its own cost of dividing and combining. Add across each level, then add the levels. The book mostly uses it to get a guess, and tolerates some sloppiness, because substitution checks the guess afterwards.

@art uneven-tree
Uneven splits, say a third and two thirds, give trees whose leaves sit at different depths. The section reads a guess of O of n log n off such a tree, and then verifies it by substitution.

@chapter The master theorem
@quote text="To use the master method, you will need to memorize three cases, but once you do that, you will easily be able to determine asymptotic bounds for many simple recurrences." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 4"
The third method comes with a promise. To use the master method, you will need to memorize three cases, but once you do that, you will easily be able to determine asymptotic bounds for many simple recurrences.

@math heading="T(n) = a·T(n/b) + f(n)" items="f = O(n^(log_b a − ε))  →  Θ(n^(log_b a))@polynomially smaller;;f = Θ(n^(log_b a))  →  Θ(n^(log_b a) · lg n)@the same order;;f = Ω(n^(log_b a + ε)), regular  →  Θ(f(n))@polynomially larger"
Compare f of n with n to the log base b of a. If f is polynomially smaller, the answer is theta of n to the log base b of a. If they're the same order, multiply by log n. If f is polynomially larger, and regular, the answer is theta of f.

@art root-vs-leaves
Think of it as a contest. There are n to the log base b of a leaves, so that measures the bottom of the tree, and f measures the top. If the leaves win, they set the answer. If the root wins, it does. If they tie, every level costs about the same, and there are log n levels.

@chapter The cases in action
@math heading="Examples" items="2T(n/2) + n:  case 2, Θ(n lg n)@two T of n over two plus n;;7T(n/2) + n²:  case 1, Θ(n^(lg 7))@seven T;;2T(n/2) + n²:  case 3, Θ(n²)@n squared, the root;;T(n/2) + 1:  case 2, Θ(lg n)@T of n over two plus one"
Two T of n over two plus n is case two, theta of n log n. Seven T of n over two plus n squared, Strassen, is case one, theta of n to the log seven. Two T of n over two plus n squared, the root dominates, so case three, theta of n squared. And T of n over two plus one is case two, theta of log n.

@art ratio-settles
The lab computes T exactly at powers of b, and divides by the predicted growth. For merge sort with T of one equal to one, T of one thousand and twenty four is eleven thousand two hundred and sixty four. That's exactly n log n plus n, and the ratio is eleven tenths, heading for one.

@chapter The gaps
@art gap
Now try four T of n over two plus n squared log n. It's larger than n squared, but only by a logarithm, not a polynomial factor. So no case applies. The exact value tracks n squared log squared n, not what case three would predict.

@words text="T(1) = 50: same case, same answer" sub="exact value about 22× bigger"
And boundary values? Run Strassen's recurrence with T of one equal to fifty. The exact value grows about twenty two fold, but the case and the solution don't move. That's why the chapter leaves boundary conditions out.

@chapter Common slips
@list heading="Common slips" items="Using case 3 whenever f is larger@The first|Absorbing the extra term into O@The second|Expecting T(1) to change the growth@the third"
The first slip is using case three whenever f is larger. It must be larger by a polynomial factor, and regular. The second is absorbing the extra term into O inside an induction. And the third is expecting T of one to change the order of growth.

@chapter Try it
@math heading="T(n) = 3T(n/2) + n,  T(1) = 1" items="T(2), T(4), T(8), T(16), T(32)@T of two"
Your turn. With T of n equal to three T of n over two plus n, and T of one equal to one, compute T of two, four, eight, sixteen and thirty two by hand. Say which case applies and what it predicts, then check both in the lab.

@end text="Watch the ratios settle"
You can evaluate recurrences exactly at large n, beside the master method's verdict, on Learn. That's learn dot get er done dot I O.
