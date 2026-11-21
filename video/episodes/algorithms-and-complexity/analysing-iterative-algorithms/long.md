---
format: long
lesson: algorithms-and-complexity/analysing-iterative-algorithms
title: How to count the cost of loops
thumb: Nested loops multiply
---

@chapter The method
@title text="Analysing Iterative Algorithms" sub="Algorithms and Complexity" art=thumb
You're handed a piece of code with a few loops in it. How long does it take as the input grows? There's a short set of rules that answers this almost every time.

@words text="Count one dominant operation" sub="as a function of the input size"
Start by choosing one dominant operation. Comparisons for a search or a sort, multiplications for arithmetic. Then count it as a function of the input size. Counting everything else as well only changes the constant.

@chapter Blocks in sequence
@math heading="One loop, then another" items="for i = 1 to n:  …  →  n@n operations;;for j = 1 to n²:  …  →  n²@n squared operations;;total  n + n² = Θ(n²)@the total"
First rule. Here's a loop that does n operations, followed by a loop that does n squared operations. Add them, and the total is n plus n squared, which is Theta of n squared.

@art side-by-side-blocks
That's the sum rule from big O. Blocks in sequence add, so asymptotically the class is the maximum. A fast block before a slow one contributes nothing.

@chapter Nested loops
@art grid-loops
Second rule. Put a loop of m steps inside a loop of n steps, and the constant work inside runs n times m times. Nested loops multiply. If m equals n, that's Theta of n squared.

@math heading="Dependent nested loops" items="for i = 1 to n:  for j = 1 to i@the inner loop;;Σᵢ₌₁ⁿ i = n(n + 1)/2@the sum;;= Θ(n²)@Theta of n squared"
Third rule. Now suppose the inner loop runs from one to i, so it depends on the outer index. Then the count is the sum of i, from one to n, which is n times n plus one, over two. That's Theta of n squared.

@art triangle-loops
It's half as many iterations as the full square, so the constant is different, but the class isn't. And a triple nest like that gives the sum of i squared, which is Theta of n cubed.

@chapter Loops that multiply
@art doubling-hops
Fourth rule. Start i at one, and while i is less than n, double it. i takes the values one, two, four, eight, and so on, so the loop runs the ceiling of log two of n times.

@math heading="Inside a loop of n" items="for i = 1 to n:  j = 1; while j < n: j = j · 2@put that inside;;total  n · log₂ n = Θ(n log n)@n times log"
Put that inside an ordinary loop of n steps, and the total is n times log two of n, Theta of n log n. Any loop whose counter is multiplied or divided by a constant runs logarithmically many times. That's where log factors come from.

@chapter Worst, average and best
@art three-cases
There's one more question: which input? The worst case is the maximum cost over inputs of size n. The best case is the minimum. And the average case is the expected cost, over some distribution of inputs.

@list heading="Best · worst · average" items="Linear search: 1 · n · about n/2@Linear search|Insertion sort: n · n²/2 · n²/4@Insertion sort|Quicksort: n log n · n² · n log n@Quicksort|Merge sort: n log n in all three@Merge sort|Bubble sort: n²/2 in all three@bubble sort"
Linear search is one at best, n at worst, about n over two on average. Insertion sort is n, n squared over two, and n squared over four. Quicksort is n log n, n squared, and n log n. Merge sort is n log n in all three, and so is bubble sort, at n squared over two.

@words text="Same in all three cases" sub="for opposite reasons"
Merge sort and bubble sort have the same bound in every case, for opposite reasons. One is always efficient and the other is always wasteful, and neither looks at the data to decide how much work to do.

@art nearly-sorted
And quicksort's average and worst cases differ by a whole class. Its average assumes every ordering is equally likely, and real data often isn't. Nearly sorted input is the classic bad case for a naive pivot.

@chapter Where people slip
@list heading="Common slips" items="Multiplying bounds when the inner one depends on the outer@The first|Adding nested loop costs@The second|Not saying which case@The third"
The first slip is multiplying the loop bounds when the inner one depends on the outer. That over counts a triangle by a factor of two. The second is adding nested loop costs, when nesting multiplies. The third is not saying which case. Insertion sort is Theta of n on sorted input, and Theta of n squared on reversed input.

@chapter Try it
@words text="for i, for j ≤ i, for k ≤ j" sub="write the sum · check it's Θ(n³)"
Try a triple dependent nest. The outer loop runs i up to n, the next runs j up to i, and the innermost runs up to j. Write the count as a sum, evaluate it with the summation formulas, and check that you land on Theta of n cubed.

@end text="Count it, then classify it"
The full lesson on analysing iterative algorithms is on Learn. That's learn dot get er done dot I O.
