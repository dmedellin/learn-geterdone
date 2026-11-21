---
format: long
lesson: induction-and-recursion/recursive-algorithms
title: Proving a recursive algorithm correct, with induction
thumb: Assume the calls work
---

@chapter Two obligations
@title text="Recursive Algorithms and Correctness" sub="Induction and Recursion" art=thumb
A recursive algorithm calls itself on smaller inputs. That makes it a recursive definition you can run, and its correctness proof is an induction.

@art flag-and-target
There are two separate things to prove. First, it terminates. Second, when it does stop, it returns the right answer. Either one alone is worthless.

@chapter Factorial
@math heading="FACTORIAL(n)" items="if n = 0:  return 1@zero, return one;;else:  return n × FACTORIAL(n − 1)@n times"
Start small. To compute factorial of n: if n is zero, return one. Otherwise, return n times factorial of n minus one.

@math items="termination:  n drops by 1, and can't go below 0@one smaller;;n = 0:  returns 1 = 0!@returns one;;assume FACTORIAL(n − 1) = (n − 1)!@assume the call;;returns n · (n − 1)! = n!@n factorial"
Termination: each call's argument is one smaller, and a natural number can't decrease past zero. Correctness, by induction on n: at zero it returns one, which is zero factorial. For larger n, assume the call returns n minus one factorial. Then it returns n times that, which is n factorial.

@chapter Binary search
@art shrinking-range
Binary search looks for x in a sorted array, between positions lo and hi. If the range is empty, report not found. Otherwise look at the middle. If it's x, return it. If it's less than x, search the upper half. If not, search the lower half.

@words text="hi − lo + 1 shrinks at every call" sub="the middle is excluded from both halves"
Termination: the size of the range, hi minus lo plus one, strictly shrinks at every call, because the middle is excluded from both halves. And it can't go below zero, where the first line returns.

@words text="strong induction on the range size"
Correctness is strong induction on the range size. An empty range can't contain x, so not found is right. If the middle holds x, that index is right.

@art sorted-bars
If the middle is less than x, then because the array is sorted, everything at or below the middle is less than x too. So x can only be in the upper half, and the hypothesis says the smaller call handles that.

@words text="Unsorted data: it stops, and it's confidently wrong"
Sortedness is doing the real work. It's what lets you throw away half the array. On unsorted data the algorithm still terminates, and returns confident wrong answers, which is the most dangerous kind of failure.

@chapter Merge sort
@art merge-zip
Merge sort: if the array has at most one element, return it. Otherwise split it into halves, sort each half recursively, and merge them. Each call gets an array of size at most n over two, rounded up, which is less than n. Arrays of size zero or one are already sorted.

@art trust-the-call
For bigger arrays, the hypothesis says both calls return sorted halves, and merging two sorted arrays gives a sorted array. Notice that nothing traced the recursion. You assume the smaller calls work and check the combining step. That's why these proofs are short.

@chapter Fast exponentiation
@math heading="POWER(a, n)" items="n = 0:  return 1@zero;;n even:  h = POWER(a, n/2),  return h × h@even;;n odd:  return a × POWER(a, n − 1)@odd"
Now a worked example: computing a to the n. If n is zero, return one. If n is even, compute h as a to the n over two, and return h times h. If n is odd, return a times a to the n minus one.

@math items="n even:  h × h = a^(n/2) · a^(n/2) = aⁿ@in the even case;;n odd:  a × aⁿ⁻¹ = aⁿ@In the odd case"
n shrinks at every call, so it stops. For correctness, in the even case, the hypothesis gives h as a to the n over two, and h times h is a to the n. In the odd case, a times a to the n minus one is a to the n.

@art squaring-ladder
Strong induction is essential here. The even branch reaches back to n over two, not n minus one, and ordinary induction would hand you a hypothesis about the wrong value. The payoff: it takes about log base two of n multiplications, rather than n.

@chapter Where people slip
@list heading="Common slips" items="Forgetting termination@forgetting termination|Tracing instead of assuming@Tracing|Overlooking a precondition@precondition"
Three slips. Proving correctness and forgetting termination. Correct if it terminates is worth nothing for an algorithm that never stops. Tracing the recursion instead of assuming the calls work, which never generalises past the input you traced. And overlooking a precondition, like binary search needing sorted input.

@end text="Count the comparisons"
On Learn you can run binary search against a straight scan. On thirty two items, the worst cases are thirty two comparisons and six. That's learn dot get er done dot I O.
