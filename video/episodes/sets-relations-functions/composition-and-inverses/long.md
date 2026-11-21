---
format: long
lesson: sets-relations-functions/composition-and-inverses
title: Composition and inverse functions: chaining and undoing
thumb: Undo in reverse order
---

@chapter The question
@title text="Composition and Inverse Functions" sub="Sets, Relations and Functions" art=thumb
You put on socks, then shoes. To undo it, you take off shoes first, then socks. That small fact about mornings is the whole theory of inverting a chain of functions. Let's build up to it.

@art two-machines
Composition chains two functions. If f goes from A to B, and g goes from B to C, then g after f goes from A to C. You feed a into f, and feed the result into g. For that to work, f's outputs have to be legal inputs for g.

@math heading="Composition" items="(g ∘ f)(a) = g(f(a))@g of f of a"
In symbols, g after f, applied to a, is g of f of a. It reads right to left: f happens first. The notation looks backwards until you read it as substitution.

@chapter Order matters
@math heading="f(x) = 2x,  g(x) = x + 3" items="(g ∘ f)(x) = g(2x) = 2x + 3@g after f;;(f ∘ g)(x) = f(x + 3) = 2x + 6@f after g;;at x = 1:  5  versus  8@at x equals one"
Let f double, and g add three. g after f doubles first, then adds three: two x plus three. f after g adds three first, then doubles: two x plus six. At x equals one, that's five versus eight. Different functions.

@art swapped-order
So composition is not commutative. It is associative, though. Bracket three functions either way, and both send a to h of g of f of a.

@chapter What composition keeps
@list heading="Composition preserves" items="injective ∘ injective is injective@both injective|surjective ∘ surjective is surjective@if both are surjective|bijective ∘ bijective is bijective@if both are bijective"
If f and g are both injective, so is g after f. If g of f of x equals g of f of y, injectivity of g gives f of x equals f of y, and injectivity of f gives x equals y. The same holds if both are surjective, and so it holds if both are bijective.

@words text="g ∘ f injective ⟹ f injective" sub="but g need not be"
The converses are weaker. If g after f is injective, then f must be, but g need not be. If g after f is surjective, then g must be, but f need not be.

@chapter Inverses
@art round-trip
An inverse of f is a function g going back from B to A, so that g after f is the identity on A, and f after g is the identity on B. Go there and back, and you end where you started. When it exists, it's unique, and it's written f inverse.

@art identity-loops
The identity sends every element to itself. And the inverse is unique, by a short chain. If g and h are both inverses, then g equals g after the identity, which is g after f after h. Regroup, by associativity, and that's the identity after h, which is h.

@art no-way-back
And an inverse exists exactly when f is a bijection. If f isn't injective, two inputs share an output, and the inverse couldn't choose. If f isn't surjective, some output has no input, and the inverse would be undefined there.

@math heading="f(x) = 3x − 5" items="y = 3x − 5  ⟹  x = (y + 5)/3@solve;;f⁻¹(y) = (y + 5)/3@so f inverse;;f(f⁻¹(y)) = 3((y + 5)/3) − 5 = y@check"
To find one, set y equal to three x minus five, and solve: x is y plus five, over three. So f inverse of y is y plus five, over three. Check by substituting: three times that, minus five, is y. Solving gives you one identity. You should check the other too.

@chapter Undoing a chain
@art socks-shoes
Now the socks and shoes. The inverse of g after f is f inverse after g inverse. The order reverses. Undo the last thing first.

@math heading="f(x) = 2x,  g(x) = x + 3" items="(g ∘ f)⁻¹(y) = (y − 3)/2@g after f, inverted;;f⁻¹(g⁻¹(y)) = (y − 3)/2   agree@f inverse of g inverse;;g⁻¹(f⁻¹(y)) = y/2 − 3   does not@the other order"
Test it. g after f, inverted, is y minus three, over two. f inverse of g inverse of y is also y minus three, over two. They agree. But in the other order, you get y over two, minus three, a different function entirely.

@chapter Where people slip
@list heading="Common slips" items="Composing left to right@The first|Writing f⁻¹ for a non-bijection@The second|Checking only one inverse identity@the third"
The first slip is composing left to right. g after f applies f first. The second is writing f inverse for a function that isn't a bijection. And the third is checking only one of the two identities. One alone makes a left inverse, which is weaker.

@chapter Try it
@words text="f(x) = 3x + 1,  g(x) = x − 4"
Your turn. Compute g after f and its inverse directly. Then check that it equals f inverse after g inverse. If the two agree, you have the order right.

@end text="When does an inverse exist?"
You can build a bijection and read its arrows backwards, on Learn. That's learn dot get er done dot I O.
