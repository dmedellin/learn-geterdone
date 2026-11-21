---
format: long
lesson: accumulation-and-the-integral/the-integral-sign-and-its-rules
title: The integral sign, its two rules, and the one that fails
thumb: Sums pass through, products don't
---

@chapter A short name
@title text="The Integral Sign and Its Rules" sub="Accumulation and the Integral" art=thumb
Every lesson in this course has used the same long phrase: the total change the rate f produces from a to b. It's time for a short form. And once you have one, you can write down rules.

@art sum-to-area
The short form is built from the sums. A left sum adds f of t times h over the pieces. The integral sign is a stretched S, for the adding. F of t is the rate, and the limits a and b are the ends.

@art thin-strip
And d t stands where the width h stood, to recall rate times width.

@math heading="The integral from a to b" items="∫ₐᵇ f(t) dt = F(b) − F(a)@the integral from a to b"
So the integral from a to b of f of t, d t, is F of b minus F of a. It's the total change, a number, and it's the number the sums of f approach.

@words text="∫₀² 3t² dt = ∫₀² 3s² ds = 8" sub="t is a placeholder"
The t inside is only a placeholder. The integral from zero to two of three t squared, d t, is eight, and so is the same thing written with s. Neither depends on a variable t.

@chapter Reading one aloud
@math heading="∫₀² (3t² + 2t) dt" items="F = t³ + t²@F equal to t cubed;;F(2) − F(0) = (8 + 4) − 0 = 12@F of two"
Here's one read aloud: the integral from zero to two of three t squared plus two t, d t. In words, it's the total change from zero to two of a quantity whose rate is three t squared plus two t. With F equal to t cubed plus t squared, it's F of two minus F of zero: twelve.

@chapter Linearity
@math heading="Linearity" items="∫ₐᵇ (c·f + d·g) dt = c·∫ₐᵇ f dt + d·∫ₐᵇ g dt@c times f;;∫₀² 3t² dt = 8,   ∫₀² 2t dt = 4@is eight;;8 + 4 = 12@Eight plus four"
The first rule is linearity. The integral of c times f plus d times g is c times the integral of f, plus d times the integral of g. Check it. The integral of three t squared from zero to two is eight, and of two t, four. Eight plus four is twelve.

@art stacked-areas
Why? If F prime is f and G prime is g, then c F plus d G has derivative c f plus d g, by the sum and constant rules. So it's an antiderivative of the combination, and its end values regroup into the two separate integrals.

@chapter Cutting the interval
@math heading="Additivity" items="∫ₐᵐ f dt + ∫ₘᵇ f dt = ∫ₐᵇ f dt@from a to m;;∫₀¹ = 2,   ∫₁² = 10@Cut at one;;2 + 10 = 12@two plus ten"
The second rule is additivity. For m between a and b, the integral from a to m, plus the integral from m to b, is the integral from a to b. Cut at one. From zero to one gives two, from one to two gives ten, and two plus ten is twelve.

@art cut-interval
The proof is one line. F of m minus F of a, plus F of b minus F of m. The two F of m cancel, leaving F of b minus F of a. Both proofs lean on the fundamental theorem, and they're only as strong as that claim.

@chapter The rule that fails
@art product-mismatch
Here's a tempting third rule, and it's false. Take f and g both equal to t, from zero to one. The product is t squared, and its integral is a third. Each factor's integral is a half, and a half times a half is a quarter. A third isn't a quarter.

@words text="(F·G)′ = f·G + F·g,  not f·g"
Linearity worked because c F plus d G differentiates to c f plus d g. A product doesn't. By the product rule, F times G differentiates to f G plus F g, so F G isn't an antiderivative of f g.

@chapter Where people slip
@list heading="Common slips" items="∫ f·g = ∫ f · ∫ g  ✗@the product|Dropping the coefficients@coefficients|Treating the integral as a function of t@a function of t"
Three slips. The first is the product rule that isn't. The second is dropping the coefficients when you split a combination. The third is treating the integral as a function of t. The integral from zero to two of three t squared is eight. Writing t cubed stops one step early, at F.

@art scaled-area
For the coefficients, take six t squared minus two t, from zero to one. That's six times a third, minus two times a half, which is one. Drop the six and the two, and you get a third minus a half: minus one sixth.

@chapter Try it
@words text="∫₀¹ (6t² − 2t) dt" sub="first ∫₀¹ t² dt and ∫₀¹ t dt"
Your turn, on the scaled preset. Compute the integrals of t squared and of t, from zero to one, separately. Combine them with six and minus two. Then compute the whole integral directly, and check they agree.

@end text="Sums and constants pass through"
You can check each rule, both sides as exact fractions, on Learn. That's learn dot get er done dot I O.
