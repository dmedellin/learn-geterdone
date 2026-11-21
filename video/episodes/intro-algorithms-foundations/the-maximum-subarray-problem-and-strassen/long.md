---
format: long
lesson: intro-algorithms-foundations/the-maximum-subarray-problem-and-strassen
title: Maximum subarray and Strassen's method, by divide-and-conquer
thumb: Seven products, not eight
---

@chapter The shape of a recursion
@title text="Maximum Subarray and Strassen" sub="Introduction to Algorithms, Sections 4.1 and 4.2" art=thumb
Chapter four applies divide and conquer twice. Once to find the best stretch of an array, and once to multiply matrices. Both times, the shape of the recursion decides the cost.

@chapter The stock problem
@art stock-prices
Section four point one starts with a story. You may buy one share of a stock once, and sell it later, and you're allowed to know the future prices. The obvious rule, buy at the bottom or sell at the top, doesn't always work. The lowest price may come after the highest.

@art price-changes
So look at the daily changes in price instead. The best trade is the stretch of consecutive days whose changes have the greatest sum. That's a maximum subarray: a contiguous, nonempty run with the largest possible sum.

@math heading="Changes" items="[5, −8, 3, 4, −2, 6, −9, 7, −1, 2, −6, 1]@five, minus eight;;A[3..6]: 3 + 4 − 2 + 6 = 11@three plus four"
On five, minus eight, three, four, minus two, six, and so on, the answer is A three to six. Three plus four minus two plus six is eleven. Buy before the third day's change, and sell after the sixth.

@chapter Divide at the middle
@art three-cases
Brute force tries every pair of ends, about n squared over two of them. Divide and conquer does better. Split at the midpoint. Any subarray lies entirely in the left half, entirely in the right half, or across the middle.

@art crossing-scan
The two halves are solved recursively. The crossing one isn't a smaller copy of the problem, and that restriction makes it easy. Scan left from the middle keeping the best sum so far, scan right the same way, and add the two. That takes linear time.

@math heading="The recurrence" items="T(n) = 2T(n/2) + Θ(n)@two T of n over two;;= Θ(n lg n)@n log n"
So T of n equals two T of n over two, plus theta of n. That's merge sort's recurrence, and the answer is theta of n log n.

@words text="78 sums · 23 calls, 44 elements · 12 reads" sub="brute force · divide-and-conquer · one pass"
On the twelve changes, all three methods in the lab find sum eleven. Brute force takes seventy eight sums. Divide and conquer makes twenty three calls, and its scans add forty four elements. A single linear pass, from exercise four point one dash five, reads just twelve.

@chapter Multiplying matrices
@art quarters
Section four point two multiplies n by n matrices. The definition takes theta of n cubed. Split each matrix into four quarters, and each quarter of the product is two products of quarters added together. That's eight half size products.

@math heading="Quarters" items="T(n) = 8T(n/2) + Θ(n²)@eight T of n over two;;= Θ(n³)@n cubed"
So T of n is eight T of n over two, plus theta of n squared, which solves to theta of n cubed. Divide and conquer alone bought nothing. That eight isn't a constant factor of the answer. It decides how bushy the tree is.

@chapter Strassen's seven
@quote text="The key to Strassen’s method is to make the recursion tree slightly less bushy." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 4.2"
In the book's words: the key to Strassen's method is to make the recursion tree slightly less bushy.

@art bushy-trees
Strassen forms ten sums and differences of the quarters, computes only seven half size products, and assembles the answer with eight more additions and subtractions. The additions cost only n squared.

@math heading="Strassen" items="T(n) = 7T(n/2) + Θ(n²)@seven T of n over two;;= Θ(n^(lg 7)),  lg 7 ≈ 2.807@log seven;;n = 16:  4,096 vs 2,401@sixteen"
So T of n is seven T of n over two plus theta of n squared, which is theta of n to the log seven, about n to the two point eight oh seven. At n equals sixteen, that's two thousand four hundred and one scalar multiplications instead of four thousand and ninety six.

@chapter Common slips
@list heading="Common slips" items="Buying at the bottom or selling at the top@The first|Expecting division alone to speed things up@The second|Taking Strassen to win at every size@the third"
The first slip is expecting the best trade to buy at the bottom or sell at the top. The second is expecting divide and conquer to beat brute force by itself. And the third is taking Strassen to win at every size. Its constant is larger, so fast libraries switch to the simple method below a crossover.

@chapter Try it
@words text="[−3, 4, −1, 2, −6, 5, −2, 3, −4]" sub="split at mid = 5"
Your turn. Take minus three, four, minus one, two, minus six, five, minus two, three, minus four. Split at mid equals five, find the best crossing subarray by scanning out from the middle, and compare it with the best of each half.

@end text="Race three algorithms"
You can compare brute force, divide and conquer and one pass on arrays of your own, on Learn. That's learn dot get er done dot I O.
