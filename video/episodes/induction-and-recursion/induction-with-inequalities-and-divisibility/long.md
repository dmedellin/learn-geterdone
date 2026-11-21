---
format: long
lesson: induction-and-recursion/induction-with-inequalities-and-divisibility
title: Induction with inequalities and divisibility: when the base case moves
thumb: Start where it starts holding
---

@chapter The base case moves
@title text="Inequalities and Divisibility" sub="Induction and Recursion" art=thumb
Not every induction proof starts at n equals one. Some claims are false for small n and only start holding later. And some claims are about divisibility, which changes what the algebra is aiming for.

@art crossing-curves
Take two to the n, against n squared. Two to the n is bigger at zero and one. But it fails at two, three and four. From five on, it wins for good. So the claim is two to the n greater than n squared, for n at least five.

@art starting-cell
Finding the right base case is part of the problem. Try n equals one, two, three, and so on until the claim starts holding. The inductive step is what guarantees it never fails again.

@chapter Two to the n beats n squared
@math heading="2ⁿ > n²  for n ≥ 5" items="n = 5:  2⁵ = 32 > 25 = 5²@thirty two;;assume 2ᵏ > k²,  k ≥ 5@assume;;2ᵏ⁺¹ = 2 · 2ᵏ > 2k²@two times"
Base case: at five, two to the five is thirty two, and that's more than twenty five. For the step, let k be at least five, and assume two to the k is more than k squared. Then two to the k plus one is two times two to the k, which is more than two k squared, by the hypothesis.

@math heading="It remains: 2k² ≥ (k+1)²" items="2k² ≥ k² + 2k + 1@Expanding;;k² − 2k − 1 ≥ 0@subtract;;(k − 1)² ≥ 2,  true for k ≥ 3@k minus one"
Now you need two k squared to be at least k plus one, squared. Expanding, that's two k squared at least k squared plus two k plus one. Subtract, and you get k squared minus two k minus one at least zero, which is k minus one squared at least two. That's true for every k from three on.

@art bridge
So chain them: two to the k plus one beats two k squared, which is at least k plus one squared. Notice that second half has nothing to do with induction. Induction supplied one fact, and ordinary algebra supplied the bridge. That bridge is where the proof actually lives.

@chapter Bernoulli's inequality
@math heading="(1 + x)ⁿ ≥ 1 + nx,  x ≥ −1" items="n = 0:  1 = 1@both sides are one;;(1+x)ᵏ⁺¹ ≥ (1 + kx)(1 + x)@multiply;;= 1 + (k+1)x + kx² ≥ 1 + (k+1)x@k x squared"
Bernoulli's inequality: for x at least minus one, one plus x to the n is at least one plus n x. At n equals zero, both sides are one. For the step, multiply the hypothesis by one plus x. You get one plus k plus one x, plus k x squared, and dropping the k x squared, which isn't negative, finishes it.

@art flip-seesaw
Where was x at least minus one used? Exactly once: it makes one plus x non-negative, so multiplying by it keeps the inequality facing the same way. Multiply by a negative number and the inequality flips. That step is easy to do silently, and wrong without the condition.

@chapter Divisibility
@math heading="3 | (n³ + 2n)" items="n = 0:  0 is divisible by 3@zero;;k³ + 2k = 3m@three m;;(k+1)³ + 2(k+1) = (k³ + 2k) + 3(k² + k + 1)@regroup;;= 3(m + k² + k + 1)@three times"
Now divisibility. Claim: three divides n cubed plus two n. At zero, you get zero, which three divides. Assume k cubed plus two k is three m. Expand the k plus one case and regroup it as the k case, plus three times k squared plus k plus one. That's three times m plus k squared plus k plus one.

@art grouped-threes
That regrouping is the whole technique. Write the k plus one case as the k case plus a remainder, and show the remainder is visibly a multiple. If it isn't visibly a multiple, the regrouping was wrong, not the claim.

@chapter Where people slip
@list heading="Common slips" items="Starting at n = 1 out of habit@out of habit|Multiplying by a possibly negative factor@possibly negative|Leaving the remainder unfactored@unfactored"
Three slips. Starting at n equals one out of habit, which can make the theorem false as written. Multiplying an inequality by a possibly negative factor, which flips its direction. And leaving the remainder unfactored. Three k squared plus three k plus three is only convincing once you write it as three times k squared plus k plus one.

@chapter Try it
@words text="n! > 2ⁿ for n ≥ 4" sub="n = 1, 2, 3:  1 < 2,  2 < 4,  6 < 8"
Your turn. Prove that n factorial is greater than two to the n, for n at least four. It fails at one, two and three. At four, four factorial is twenty four, and two to the four is sixteen.

@art factorial-race
For the step, write k plus one factorial as k plus one times k factorial, and use the hypothesis. Say why multiplying by k plus one is safe: it's positive. Then use k at least four to get past two times two to the k.

@end text="Find where the claim starts"
You can see exactly where two to the n starts beating n squared on Learn. That's learn dot get er done dot I O.
