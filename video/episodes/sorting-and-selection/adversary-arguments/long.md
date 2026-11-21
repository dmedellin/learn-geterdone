---
format: long
lesson: sorting-and-selection/adversary-arguments
title: Adversary arguments: proving no algorithm can do better
thumb: Keep the most outcomes alive
---

@chapter The question
@title text="Adversary Arguments" sub="Sorting and Selection" art=thumb
How do you prove that no algorithm can find the maximum in fewer than n minus one comparisons? You can't test every algorithm. You need an argument that covers all of them, including ones nobody has written yet.

@chapter The adversary
@art adversary-answers
Here's the trick. Imagine an adversary who holds no array. Whenever the algorithm asks a comparison, the adversary answers, choosing whatever keeps the most outcomes possible. Its only rule is consistency. There must always be at least one input that agrees with every answer.

@words text="Two answers still possible ⟹ not done yet"
If, after fewer than B comparisons, two different answers are still consistent with everything said, the algorithm can't have determined the result. So B is a lower bound, for every algorithm at once.

@chapter The maximum
@art unbeaten
Call an element unbeaten if it hasn't lost a comparison. At the start, all n are unbeaten. The algorithm can only report a maximum when exactly one is left, because if two were, the adversary could make either one the largest.

@math heading="Finding the maximum" items="each comparison removes ≤ 1 unbeaten@at most one;;n → 1 unbeaten:  ≥ n − 1 comparisons@n minus one;;a single scan:  exactly n − 1@single scan"
And each comparison removes at most one element from the unbeaten set, since only the loser leaves. Going from n to one takes at least n minus one comparisons. A single scan makes exactly that many, so the bound is tight.

@chapter Both ends at once
@art two-scans
Now find the minimum and the maximum together. The obvious way is two scans, one for each end. That's n minus one each, two n minus two in all.

@art pairing
But pair the elements first, and compare within each pair. The winners are the only candidates for maximum, and the losers the only candidates for minimum.

@math heading="Minimum and maximum, n = 8" items="pairs:  ⌊n/2⌋ = 4@pairs;;min of losers:  3 · max of winners:  3@losers;;total:  10 = ⌈3n/2⌉ − 2@ten;;two scans:  14@Two separate scans"
At eight elements, the pairs cost four. The minimum among the four losers costs three, and the maximum among the winners costs three. That's ten, which is the ceiling of three n over two, minus two, and the bound says you can't do better. Two separate scans would cost fourteen.

@chapter The second largest
@art tournament
The second largest must have lost to the maximum, because it lost to nobody else. So find the maximum first, then find the best among the elements it beat. A knockout tournament makes that set as small as possible.

@math heading="Second largest, n = 8" items="tournament:  n − 1 = 7@seven;;winner played ⌈log₂ n⌉ = 3 rounds@three rounds;;best of those 3:  2 more@two more;;total:  9 = n + ⌈log₂ n⌉ − 2@nine"
At eight, the tournament takes seven comparisons. The winner played three rounds, so only three elements ever lost to it. Picking the best of those costs two more. Nine in all, which is n plus the ceiling of log two of n, minus two. That's the lower bound, met exactly.

@words text="keep the best two while scanning:  up to 2n − 3 = 13" sub="measured 11 on the lab's array"
The natural approach is to scan, keeping the best two. That costs up to two n minus three, thirteen at eight keys. The tournament's saving is that it remembers who lost to the winner, so there are only three candidates instead of seven.

@art every-arrangement
The lab runs the tournament on every arrangement of up to eight keys, all forty thousand three hundred and twenty of them at eight. None exceeds nine, and none returns the wrong element. That's a claim about every input of that size. It's still not a claim about every algorithm. Only the adversary gives that.

@words text="⌈log₂ n!⌉ for sorting" sub="the same kind of claim"
And the sorting bound, the ceiling of log two of n factorial, is the same kind of statement. It's proved by counting the leaves a decision tree needs, and this course uses it as a floor to compare against.

@chapter Where people slip
@list heading="Common slips" items="Assuming the second largest costs about 2n@The first|Proving a lower bound by testing@The second|Suspecting the adversary of cheating@And the third"
The first slip is assuming the second largest costs about two n. The second is trying to prove a lower bound by testing algorithms. A measurement can refute an upper bound, never establish a lower one. And the third is suspecting the adversary of cheating. It never contradicts itself, and at the end, it can produce an array.

@chapter Try it
@words text="n = 6: min and max, second largest" sub="compute both bounds, then meet them"
Your turn. For six elements, work out the bound for finding the minimum and maximum together, and for the second largest. Then describe an algorithm that meets each one.

@end text="Play against the adversary"
You can run the tournament and the pairing trick and check them against the bounds, on Learn. That's learn dot get er done dot I O.
