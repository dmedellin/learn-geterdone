---
format: long
lesson: induction-and-recursion/mathematical-induction
title: Mathematical induction: base case, step, and the line that matters
thumb: The step must use the hypothesis
---

@chapter The idea
@title text="Mathematical Induction" sub="Induction and Recursion" art=thumb
You want to prove something for every whole number from some starting point on. You can't check them all. Induction lets you prove all of them with two finite arguments.

@math heading="The principle" items="P(n₀) holds@starting value;;P(k) → P(k+1) for every k ≥ n₀@every k;;then P(n) holds for every n ≥ n₀@for every n"
Let P of n be a statement about integers from some starting value n nought. If P of n nought holds, and P of k implies P of k plus one for every k from n nought on, then P of n holds for every n from n nought on.

@art domino-chain
You've probably met the dominoes. The base case tips the first one, and the step guarantees each one knocks over the next. That's right, but slightly misleading. It suggests a process that takes time. The conclusion isn't that every case will eventually get proved. It's that every case is true.

@chapter Three parts
@list heading="Writing it" items="Base case: prove P(n₀)@base case|Step: assume P(k) for arbitrary k ≥ n₀, prove P(k+1)@inductive step|Conclude: P(n) for all n ≥ n₀@conclude"
Every induction proof has three parts. The base case: prove P of n nought. The inductive step: assume P of k for an arbitrary k, and prove P of k plus one. Then conclude that P of n holds from n nought on.

@art step-arrow
Be careful about what the step assumes. You aren't assuming P of k for all k. You're proving an implication, if P of k then P of k plus one, for an arbitrary k. That's a direct proof of a conditional.

@chapter A worked example
@math heading="1 + 2 + ⋯ + n = n(n+1)/2" items="n = 1:  left 1,  right 1 · 2 / 2 = 1@For n equals one;;assume 1 + 2 + ⋯ + k = k(k+1)/2@assume"
Let's prove the sum of the first n positive integers is n times n plus one, over two. Base case: for n equals one, the left side is one, and the right is one times two over two, which is one. They agree. Now let k be arbitrary, and assume the formula holds at k.

@math items="1 + ⋯ + k + (k+1)@add the next;;= k(k+1)/2 + (k+1)@replace the first;;= (k+1)(k+2)/2@k plus two over two"
Add the next term, k plus one. Using the hypothesis, replace the first k terms by k times k plus one, over two. Then the whole thing simplifies to k plus one, times k plus two, over two. That's exactly the claim at k plus one.

@art stacked-sum
Here's the line a reader looks for: this is where the hypothesis was used. It isn't padding. A proof that can't point to that sentence isn't an induction proof.

@chapter Three ways to get it wrong
@words text="P(n):  n = n + 1" sub="step: k = k+1  ⟹  k+1 = k+2"
First, no base case. Take the statement n equals n plus one. The step works fine: if k equals k plus one, adding one gives k plus one equals k plus two. And the statement is false for every n. The base case is what fails.

@art chain-anchor
Without a base case, the implications form a chain with nothing at the start. Second way wrong: the hypothesis is never used. Then you've proved P of k plus one from scratch, a direct proof in an induction wrapper. Often it means the step was misread.

@words text="P(3) → P(4) is not the step"
Third, the step is proved for one particular k. Checking that P of three implies P of four isn't the inductive step. k has to be arbitrary, just as in any proof about every value.

@chapter All horses are the same colour
@art horse-groups
Here's the classic bogus proof. All horses are the same colour. Base: one horse, trivially. Step: given k plus one horses, the first k share a colour by hypothesis, and so do the last k, so all of them agree.

@words text="k = 1:  the two groups don't overlap"
The flaw is at k equals one. Two horses split into two groups of one, which don't overlap, so nothing links them. The step works for every k but one, and that single failure breaks the whole chain. So check the step at the smallest values. It's a cheap habit.

@chapter Where people slip
@list heading="Common slips" items="Omitting the base case@leaving out|Never using the hypothesis@never using|Assuming P(k+1)@assuming"
To sum up the slips: leaving out the base case, which is one line, and the line that makes the rest mean something. Never using the inductive hypothesis. And assuming P of k plus one, which is circular. The hypothesis is P of k, and that distinction is the whole technique.

@chapter Try it
@math heading="1 + 3 + 5 + ⋯ + (2n − 1) = n²" items="n = 1:  1 = 1²@Check n equals one;;… + (2k−1) + (2k+1) = k² + (2k+1)@next odd number;;k² + 2k + 1 = (k+1)²@recognise"
Your turn: the sum of the first n odd numbers is n squared. Check n equals one. For the step, add the next odd number, two k plus one, and use the hypothesis on the rest. You'll get k squared plus two k plus one. Recognise it as k plus one, squared, and point to where the hypothesis went in.

@art odd-squares
In a picture, each odd number you add is one more layer, growing a k by k square into a k plus one by k plus one square.

@end text="Step through the proof"
You can check cases against the inductive step for each statement, and see why checking alone isn't proof, on Learn. That's learn dot get er done dot I O.
