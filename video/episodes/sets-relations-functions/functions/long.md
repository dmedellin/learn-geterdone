---
format: long
lesson: sets-relations-functions/functions
title: What is a function, really? Domain, codomain and image
thumb: Exactly one output
---

@chapter The question
@title text="Functions" sub="Sets, Relations and Functions" art=thumb
You've used functions for years. But what is one, as an object? In this course the answer is a relation, a set of pairs, with one extra condition.

@art arrow-machine
A function f from A to B is a relation between A and B in which every element of A has exactly one partner in B. That partner is written f of a. Every input, one arrow out.

@math heading="f : A → B" items="for every a ∈ A, exactly one b ∈ B with (a, b) ∈ f@exactly one b;;that b is written f(a)@gets the name"
So for every a in A, there's exactly one b with a, b in f. And that b gets the name f of a.

@chapter Two ways to fail
@art broken-rules
Exactly one packs two conditions. At least one output means the function is total. At most one means it's well defined. A rule can fail either way.

@math items="f(x) = 1/x  on ℝ:  nothing at 0  ✗@one over x;;f(x) = 1/x  on ℝ \ {0}  ✓@without zero;;a square root of x:  two values for 4  ✗@square root"
One over x isn't a function on the reals, because nothing is assigned to zero. On the reals without zero, it's fine. The rule and the domain together make the function. And a square root of x gives two values for four, two and minus two. Choose the non negative root and it becomes a function.

@math heading="Is it a function, from ℝ to ℝ?" items="f(x) = 2x + 1   ✓@two x plus one;;f(x)² = x   ✗@squared equals x"
A quick test. f of x equals two x plus one, from the reals to the reals: yes, one output each. But a rule saying f of x, squared, equals x fails both ways at once. It gives two values for four, and none at all for minus one.

@chapter Domain, codomain, image
@art image-inside
In f from A to B, A is the domain, where inputs come from. B is the codomain, where outputs are declared to live. And the image is where the outputs actually land. The image sits inside the codomain, but it needn't fill it.

@art parabola
Take f of x equals x squared, from the reals to the reals. The codomain is all the reals. But squares are never negative, and every non negative real is a square, so the image is zero to infinity.

@math heading="Same rule, three functions" items="f : ℝ → ℝ,  image [0, ∞) ≠ ℝ@from the reals to the reals;;g : ℝ → [0, ∞),  image = codomain@g goes;;h : [0, ∞) → [0, ∞),  also one-to-one@and h"
So one formula, three functions. f goes from the reals to the reals, and its image is smaller than its codomain. g goes from the reals to zero to infinity, and its image equals its codomain. And h, from zero to infinity to itself, is also one to one. The codomain is part of the function.

@chapter Defining through a representative
@art class-check
A subtler failure appears when a function is defined on classes. Define f of a class mod four as a mod two. Since one and five are the same class, f must agree on them, and it does: both are odd.

@math items="f([a]₄) = a mod 3?@a mod three;;1 mod 3 = 1,  5 mod 3 = 2  ✗@one mod three"
But try a mod three instead. One mod three is one, and five mod three is two. Same input, two answers, so it isn't well defined.

@words text="4 | (a − b)  ⟹  2 | (a − b)"
The mod two version needed an argument, not just a look. If a and b agree mod four, four divides a minus b, so two does too, so they agree mod two.

@chapter Preimages
@art preimage
For a set T in the codomain, the preimage is everything in A that lands in T. It's defined for every function and every T, and it may be empty. The notation looks like an inverse, but it doesn't need one. A real inverse exists only for a bijection.

@chapter Where people slip
@list heading="Common slips" items="Treating image and codomain as the same@The first|Ignoring where a rule is undefined@The second|Skipping the well-definedness check@the third"
The first slip is treating image and codomain as the same set. They coincide exactly when the function is onto, which is the next lesson's question. The second is ignoring where a rule is undefined. And the third is defining a function on classes without checking it's well defined.

@chapter Try it
@words text="f : ℤ → ℤ,  f(n) = n²"
Your turn. For f from the integers to the integers, with f of n equal to n squared, name the domain, the codomain and the image. Then say what changes if the codomain is narrowed to the perfect squares.

@end text="Assign each input an output"
You can draw a function's arrows and watch the image shrink inside the codomain, on Learn. That's learn dot get er done dot I O.
