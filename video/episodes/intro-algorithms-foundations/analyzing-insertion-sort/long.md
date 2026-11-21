---
format: long
lesson: intro-algorithms-foundations/analyzing-insertion-sort
title: Counting every line of insertion sort
thumb: Linear best, quadratic worst
---

@chapter What analysis means
@title text="Analyzing Insertion Sort" sub="Introduction to Algorithms, Section 2.2" art=thumb
Insertion sort is correct. But how long does it take? Section two point two answers by counting, line by line, and the answer depends a lot on the input.

@quote text="Analyzing an algorithm has come to mean predicting the resources that the algorithm requires." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 2.2"
It opens like this: analyzing an algorithm has come to mean predicting the resources that the algorithm requires. Usually, that resource is time.

@chapter A machine to count on
@art ram-machine
To count steps, you need a machine to count them on. The book's is the random access machine, the RAM. One processor runs instructions one after another, and arithmetic, loading, storing, branching and calling each take constant time. There's no sort instruction, and caches and virtual memory are left out.

@chapter Cost times count
@art line-counter
Now charge each line of insertion sort a constant cost every time it runs, and count how often each line runs. The running time is the sum of cost times count, over every line.

@words text="tⱼ = runs of the inner test in pass j" sub="= shifts in that pass + 1"
The count turns on one quantity, t j. It's the number of times the inner loop's test runs, in the pass that inserts A of j. A loop's test runs once more than its body, so t j is the shifts in that pass, plus one.

@math heading="Every cᵢ = 1" items="lines = n + 3·(n − 1) + Σtⱼ + 2·Σ(tⱼ − 1)@lines executed;;best, tⱼ = 1:  5n − 4@best case;;worst, tⱼ = j:  (3n² + 7n − 8)/2@worst case"
Set every cost to one, and the lines executed are n, plus three times n minus one, plus the sum of t j, plus twice the sum of t j minus one. In the best case, t j is one, and that's five n minus four. In the worst case, t j is j, and it's three n squared plus seven n minus eight, all over two.

@chapter Best, worst and average
@art best-worst
The best case is an array already sorted. Every test fails at once, and the time is linear. The worst case is an array in decreasing order. Each key is compared with the whole prefix, and the time is quadratic. Same algorithm, same n, two different functions.

@list heading="Why report the worst case" items="It's a guarantee@a guarantee|It happens often@happens often|The average is often as bad@the average case"
The book usually reports the worst case, for three reasons. It's an upper bound for every input of that size, a guarantee. For some algorithms it happens often, like a search for something absent. And the average case is often about as bad. On random input, t j is about j over two, still quadratic.

@art leading-term
The last step is one more abstraction. For large inputs, the rate of growth matters more than constants and smaller terms. So keep only the leading term, a n squared, drop its coefficient, and insertion sort's worst case is theta of n squared.

@chapter A worked count
@math heading="[6, 1, 8, 3, 7, 2, 5, 4]" items="tⱼ: 2, 1, 3, 2, 5, 4, 5  →  Σ = 22@summing to twenty two;;21 comparisons, 15 shifts@fifteen shifts;;81 lines  (best 36, worst 120)@eighty one lines"
Take six, one, eight, three, seven, two, five, four. The t j values are two, one, three, two, five, four and five, summing to twenty two. There are twenty one comparisons and fifteen shifts. And eighty one lines run, between the best case of thirty six and the worst of a hundred and twenty.

@art inversion-pairs
Here's a neat fact. The shifts equal the inversions of the array, the pairs of positions whose keys are out of order. They're the subject of the book's problem two four.

@art nearly-sorted
Sort those eight keys first, and exactly thirty six lines run. Reverse them, and exactly a hundred and twenty. Now swap just two adjacent pairs in a sorted array, and forty two lines run, close to the best. Insertion sort's cost tracks how unsorted its input is.

@words text="30 reversed keys: 1,451 lines" sub="146 if they arrived sorted"
That's why it's used on small or nearly sorted arrays. But even thirty keys in reverse take one thousand four hundred and fifty one lines, against a hundred and forty six sorted. The quadratic term is already doing most of the work.

@chapter Common slips
@list heading="Common slips" items="Reading Θ(n²) as the time on every input@The first|Taking tⱼ for comparisons or shifts@The second|Treating the line costs as known@the third"
The first slip is reading theta of n squared as the time on every input, when a sorted array is linear. The second is taking t j for the comparisons or shifts, when it's one more than the shifts. And the third is treating the line costs as known, when the order of growth doesn't depend on them.

@chapter Try it
@words text="[5, 9, 2, 6, 3]" sub="write tⱼ for j = 2 to 5"
Your turn. For five, nine, two, six, three, write down t j for j from two to five. Then evaluate the line cost sum with every cost equal to one, and compare it with the lab.

@end text="Count every line yourself"
You can count every line on arrays of your own, beside the best and worst cases, on Learn. That's learn dot get er done dot I O.
