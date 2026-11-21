---
format: long
lesson: algorithms-and-complexity/growth-of-functions
title: Why growth rate beats a faster computer
thumb: A faster machine won't save you
---

@chapter The question
@title text="The Growth of Functions" sub="Algorithms and Complexity" art=thumb
Two algorithms solve the same problem. Which is faster? The honest answer is: it depends on the size of the input. What you really want to compare is how their costs grow.

@art growth-curves
So line up the usual suspects. Log n, n, n log n, n squared, and two to the n. At ten items they all look harmless. Two to the ten is only one thousand and twenty four.

@chapter At a million
@math heading="n = 1 000 000" items="n log₂ n ≈ 2.0 × 10⁷@n log n;;n² = 10¹²@n squared;;at 10⁹ per second: ≈ 1/50 s  vs  ≈ 15 min@a billion operations"
Now go to a million items. An n log n algorithm does about twenty million operations. An n squared one does ten to the twelve. At a billion operations a second, that's a fiftieth of a second against about a quarter of an hour.

@words text="Both polynomial" sub="and the gap is already decisive"
And both of those are polynomial. The gap between them is already decisive, long before anything exponential shows up.

@chapter Exponential is different
@math heading="2ⁿ at n = 100" items="2¹⁰⁰ ≈ 1.27 × 10³⁰@two to the hundred;;≈ 4 × 10¹³ years at 10⁹ per second@four times ten;;≈ 3000 × the age of the universe@three thousand times"
Here's two to the n at just a hundred items. Two to the hundred is about one point two seven times ten to the thirty. At a billion operations a second, that's about four times ten to the thirteen years, roughly three thousand times the age of the universe.

@art hourglasses
No hardware improvement fixes that. And you can make that precise, by asking what a faster machine actually buys you.

@chapter What a faster machine buys
@math heading="k times faster, same time" items="linear:  n → kn@linear;;quadratic:  kn² = (n√k)²,  so n → n√k@quadratic"
Say the machine gets k times faster, and you give each algorithm the same amount of time. A linear algorithm can now handle k times as much. For a quadratic one, k times n squared is n root k, all squared, so the size grows by a factor of root k.

@math heading="k times faster, same time" items="exponential:  k · 2ⁿ = 2ⁿ⁺ˡᵒᵍ₂ᵏ@exponential;;so n → n + log₂ k@added on"
For an exponential one, k times two to the n is two to the n plus log two of k. So the size only goes up by log two of k, added on. It's a constant, not a factor.

@art speedup-bars
Put in a thousandfold speed up. The linear algorithm handles a thousand times more data. The quadratic one handles about thirty two times more. The exponential one handles ten more items. That's the real meaning of polynomial versus exponential.

@art wall
A faster machine moves the wall. It doesn't remove it. Polynomial costs scale with hardware, and exponential ones don't. That's exactly why the line between P and NP, later in this course, is drawn where it is.

@chapter Lower-order terms
@math heading="f(n) = 3n² + 5n + 100" items="n = 10:  300 + 50 + 100 = 450  →  67%@at ten;;n = 100:  30 000 + 500 + 100 = 30 600  →  98%@at a hundred;;n = 1000:  3 000 000 + 5 000 + 100  →  99.8%@at a thousand"
Now take three n squared plus five n plus a hundred. At ten, the quadratic term is sixty seven percent of the total. At a hundred, it's ninety eight percent. At a thousand, it's ninety nine point eight percent.

@art dominant-term
So this function grows like n squared, and the three and the extra terms get dropped. Not because they don't exist, but because they don't change the comparison with an algorithm that grows at a different rate.

@art crossover
Constants still matter in practice, though. An n log n algorithm with a huge constant can lose to an n squared one on every input anyone will actually run. That's why real sorting code switches to insertion sort for small pieces.

@chapter The ladder
@words text="1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!"
Here's the ladder to remember. One, log n, root n, n, n log n, n squared, n cubed, two to the n, and n factorial. Constants and lower order terms never move a function to a different rung. And the step from polynomial to exponential is a difference of kind.

@chapter Where people slip
@list heading="Common slips" items="Comparing at one input size@The first|Ignoring constants entirely@The second|Believing hardware fixes exponential cost@The third"
The first slip is comparing at one input size. An algorithm that's faster at a hundred may be hopeless at a million. The second is ignoring constants entirely. They decide between algorithms in the same class, and where two different classes cross. The third is believing hardware fixes exponential cost.

@chapter Try it
@words text="k = 1 000 000" sub="linear? quadratic? exponential?"
Try it yourself. Instead of a thousandfold, imagine a machine a million times faster. Using the three rules, how much bigger can each kind of algorithm go?

@end text="Watch the curves pull apart"
The full lesson on the growth of functions is on Learn. That's learn dot get er done dot I O.
