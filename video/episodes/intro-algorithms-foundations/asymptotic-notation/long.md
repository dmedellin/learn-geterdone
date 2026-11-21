---
format: long
lesson: intro-algorithms-foundations/asymptotic-notation
title: Big O, Omega and Theta, with real witnesses
thumb: A bound needs a witness
---

@chapter Why precision
@title text="Asymptotic Notation" sub="Introduction to Algorithms, Chapter 3" art=thumb
For two chapters, the book has said things like insertion sort is theta of n squared. Chapter three makes that precise.

@quote text="We should make sure, however, to understand the precise meaning of the notation so that when we abuse, we do not misuse it." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 3"
The authors put it this way. We should make sure, however, to understand the precise meaning of the notation so that when we abuse, we do not misuse it.

@words text="Notation describes functions" sub="not only running times"
The notations describe how a function grows as n grows without bound, once constants and smaller terms stop mattering. And they describe functions, not only running times. They can describe space, or anything else.

@chapter Theta, O and Omega
@art sandwich
Theta of g is a set of functions. f belongs to it if there are positive constants c one, c two and n nought, so that from n nought on, f sits between c one times g and c two times g. It's sandwiched.

@math heading="Three sets" items="Θ(g):  c₁·g(n) ≤ f(n) ≤ c₂·g(n)@theta keeps both;;O(g):  0 ≤ f(n) ≤ c·g(n)@O keeps only the upper;;Ω(g):  0 ≤ c·g(n) ≤ f(n)@omega keeps only the lower;;for all n ≥ n₀@from n nought on"
Theta keeps both inequalities. O keeps only the upper one, so f is capped by a multiple of g. Omega keeps only the lower one, so f is floored. And each must hold for every n from n nought on.

@art upper-cap
O is only an upper bound, and the book insists on that. n is O of n squared, and that's true. Some writers use O to mean a tight bound, but the book doesn't. And by theorem three point one, f is theta of g exactly when it's both O of g and omega of g.

@art lower-floor
For running times, an O bound on the worst case bounds every input. So insertion sort is O of n squared on every input. An omega bound bounds the best case, so it's also omega of n. Both are as tight as possible.

@chapter A witness
@math heading="3n² + 10n = Θ(n²)" items="c₁ = 3,  c₂ = 4,  n₀ = 10@c one three;;at n₀:  400 ≤ 400  ✓@four hundred;;n₀ = 5:  125 > 100  ✗@from five"
Constants that prove a claim are called a witness. Take three n squared plus ten n equals theta of n squared, with c one three, c two four, and n nought ten. It holds at every value the lab tries, and at ten, the upper side is four hundred against four hundred. Start from five, though, and it fails at once, a hundred and twenty five above a hundred.

@words text="The claim is still true" sub="only that witness is wrong"
The claim is still true. Only that witness is wrong. A claim is false only when no witness exists at all.

@chapter The trap of checking
@art witness-breaks
Now the one to remember. Claim n log n is O of n, with c a hundred and n nought one. The lab checks ten thousand values, and it holds at every one. But the claim is false. n log n stays under a hundred n only until log n passes a hundred, near two to the hundred.

@words text="A finite check can refute, never prove" sub="n lg n = Θ(n²) breaks at n = 997"
Another false claim, n log n is theta of n squared with c one a hundredth, survives all the way from two to nine hundred and ninety six, then breaks. A finite check can refute a witness. It can never establish a bound.

@chapter Strict bounds and the menu
@art incomparable
Little o and little omega are the strict versions. They hold for every positive constant, not just one. The five notations behave like comparing numbers, less than or equal, greater than or equal, equals, less than and greater than. But one property fails. Two functions need not be comparable at all.

@art growth-ladder
Section three point two surveys the usual functions. Any exponential with base above one beats any polynomial. Any positive power of n beats any power of log n. And the iterated log, log star, is only five at two to the sixty five thousand five hundred and thirty six.

@math heading="Slowest first" items="1   lg* n   lg n   n   n lg n@one, log star;;n²   n³   F(n)   2ⁿ   n!@n squared"
So the lab's menu runs one, log star n, log n, n, n log n, then n squared, n cubed, the Fibonacci numbers, two to the n, and n factorial.

@chapter Common slips
@list heading="Common slips" items="Reading O as a tight bound@The first|Taking a range check as a proof@The second|Assuming any two functions compare@the third"
The first slip is reading O as a tight bound. The second is taking a witness that held on a range as a proof. And the third is assuming any two functions are comparable. n and n to the one plus sine n aren't.

@chapter Try it
@math heading="Find n₀" items="n² − 50n ≥ n²/2@n squared minus fifty n"
Your turn. Show by hand that n squared minus fifty n is omega of n squared with c one a half. Find the least n nought from which n squared minus fifty n is at least n squared over two. Then try it in the lab, and try one less.

@end text="Test a witness yourself"
You can test claimed witnesses at ten thousand sizes and watch false ones break, on Learn. That's learn dot get er done dot I O.
