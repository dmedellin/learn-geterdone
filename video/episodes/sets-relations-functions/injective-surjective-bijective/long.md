---
format: long
lesson: sets-relations-functions/injective-surjective-bijective
title: Injective, surjective, bijective: no collisions, no gaps
thumb: No collisions, no gaps
---

@chapter The question
@title text="Injective, Surjective, Bijective" sub="Sets, Relations and Functions" art=thumb
A function sends every input to exactly one output. But that still leaves two things it might do badly. Two inputs might crash into the same output. Or some outputs might never be hit at all. Those two questions have names.

@art collision
Injective, or one to one, means no collisions. If f of x equals f of y, then x equals y. Distinct inputs always get distinct outputs. To refute it, you name the two inputs that collide.

@art gap
Surjective, or onto, means no gaps. Every element of the codomain is hit by something. Equivalently, the image is the whole codomain. To refute it, you name the element nothing maps to.

@art perfect-pairing
And bijective means both. A bijection pairs the elements of A with the elements of B so that nothing is left over on either side.

@chapter How to prove each
@math heading="Injective" items="f(x) = f(y)  ⟹  x = y@assume f of x"
The definitions are stated the way you use them. To prove injective, assume f of x equals f of y, and derive x equals y. That's a direct proof.

@math heading="Surjective" items="∀b ∈ B  ∃a ∈ A :  f(a) = b@take an arbitrary b"
To prove surjective, take an arbitrary b in the codomain and construct an a that maps to it. That's an existence proof, and it's usually the harder one.

@chapter Same rule, different verdicts
@math heading="x ↦ x²" items="ℝ → ℝ:  neither@the reals to the reals;;[0, ∞) → ℝ:  injective only@from zero to infinity into;;ℝ → [0, ∞):  surjective only@onto zero to infinity;;[0, ∞) → [0, ∞):  bijective@to itself"
Squaring, from the reals to the reals, is neither. Two and minus two collide, and nothing maps to minus one. From zero to infinity into the reals, it's injective only. From the reals onto zero to infinity, it's surjective only. And from zero to infinity to itself, it's a bijection. The formula never changed.

@chapter Counting first
@art too-many
Sometimes you know the answer before you look at the rule. An injection needs the size of A to be at most the size of B. A surjection needs it to be at least. With five inputs and three targets, no injection exists, whatever the rule. With three inputs and five targets, no surjection does. That's the pigeonhole principle.

@words text="|A| = |B| finite  ⟹  injective ⟺ surjective"
And on finite sets of equal size, the two properties imply each other. An injection's image has as many elements as A, all inside B, so it fills B. A surjection needs every target hit, and with only as many inputs as targets, each gets exactly one.

@chapter Infinite sets break it
@art shift-chain
On infinite sets, that equivalence fails. Take n plus one, from the naturals to the naturals. It's injective, but nothing maps to zero, so it isn't surjective, even though domain and codomain are the same set. A set is infinite exactly when it injects into a proper subset of itself.

@chapter A worked classification
@math heading="f : ℤ → ℤ,  f(n) = 2n + 3" items="2m + 3 = 2n + 3  ⟹  m = n   injective@suppose f of m;;b = 0:  a = −3/2 ∉ ℤ   not surjective@zero"
Take f of n equals two n plus three, on the integers. Injective? Suppose f of m equals f of n. Subtract three, divide by two, and m equals n. Yes. Surjective? Solving two a plus three equals b gives a equals b minus three, over two. For b equal to zero, that's minus three halves, not an integer. No.

@art odd-targets
In fact the image is exactly the odd integers. So f is injective, not surjective, and not a bijection. Change the codomain to the odd integers, and it becomes one.

@chapter Where people slip
@list heading="Common slips" items="Deciding surjectivity without the codomain@The first|Assuming injective implies surjective@The second|Refuting without a witness@the third"
The first slip is deciding surjectivity without the codomain. It isn't a property of the formula alone. The second is assuming injective implies surjective. That's only true for finite sets of equal size. And the third is refuting a property without a witness. The witness is the proof.

@chapter Try it
@words text="f : ℤ → ℤ,  f(n) = n² − n" sub="f(0) = f(1) = 0"
Your turn. Classify f of n equals n squared minus n, on the integers. Give a proof or a specific witness for each property. Here's a start: f of zero and f of one are both zero, which settles one of them immediately.

@end text="Try to build each kind"
You can try to build each kind of function, and see when the sizes rule one out, on Learn. That's learn dot get er done dot I O.
