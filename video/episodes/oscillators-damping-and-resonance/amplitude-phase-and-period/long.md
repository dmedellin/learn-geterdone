---
format: long
lesson: oscillators-damping-and-resonance/amplitude-phase-and-period
title: Amplitude and phase: one cosine for a whole swing
thumb: How far does it swing?
---

@chapter The question
@title text="Amplitude, Phase and Period" sub="Oscillators, Damping and Resonance" art=thumb
A mass on a spring starts at three and is moving outward. How far does it get? Not three. The answer here is five.

@art two-waves-sum
The last lesson ended with C one cosine omega nought t plus C two sine omega nought t. Nothing's wrong with it, but it hides the two things you'd want to know: how far the mass gets from rest, and when it gets there.

@chapter One cosine
@math heading="Amplitude and phase" items="x = A·cos(ω₀t − φ)@A times cosine;;A ≥ 0  amplitude,   φ  phase@the amplitude"
So write the motion as one cosine: A times cosine of omega nought t minus phi. A is the amplitude, the largest value of x. Phi is the phase.

@art amplitude-bar
The amplitude is the height of the swing, how far the mass ever gets from rest, on either side. It's always zero or more.

@art shifted-cosine
The phase shifts the cosine to the right by phi over omega nought units of time. And the period is still two pi over omega nought. Neither A nor phi enters it.

@math heading="Matching the two forms" items="A·cos(ω₀t − φ) = (A·cos φ)·cos(ω₀t) + (A·sin φ)·sin(ω₀t)@the subtraction identity;;C₁ = A·cos φ,   C₂ = A·sin φ@So C one"
The two forms are the same function, by the subtraction identity for cosine, which this path takes as given. Expand, and match the pieces. So C one is A cosine phi, and C two is A sine phi.

@chapter The amplitude squared
@math heading="From the start" items="C₁ = x₀@C one is the start;;C₂ = v₀/ω₀@C two is the starting velocity;;A² = C₁² + C₂² = x₀² + v₀²/ω₀²@Square and add"
At t equals zero, C one is the start, x nought. The velocity at zero is omega nought times C two, so C two is the starting velocity over omega nought. Square and add, and since cosine squared plus sine squared is one, A squared is x nought squared plus v nought squared over omega nought squared.

@art amplitude-triangle
You can picture it as a right triangle. The legs are C one and C two. The long side is the amplitude, and the angle is the phase.

@chapter Three starts, one spring
@math heading="m = 1,  k = 4,  ω₀ = 2" items="(3, 8):  C₁ = 3,  C₂ = 4,  A² = 25@Start at three;;(2, 0):  C₁ = 2,  C₂ = 0,  A² = 4@Start at two;;(1, 1):  C₁ = 1,  C₂ = 1/2,  A² = 5/4@Start at one, one"
Take m equals one and k equals four, so omega nought is two. Start at three with velocity eight: C one is three, C two is eight over two, four, and A squared is nine plus sixteen, twenty five. Start at two, zero: A squared is four. Start at one, one: C two is a half, and A squared is five quarters.

@art overshoot-start
So the first start reaches five, not three. The mass is already moving outward when it's released, so it overshoots. The tangent of the phase is four thirds, so phi is about zero point nine two seven two nine five, rounded.

@words text="A² = 5/4,   A = √5/2 ≈ 1.11803" sub="tan φ = 1/2"
For one, one, A squared is five quarters, exact. Its root, root five over two, is exact too, and the lab prints about one point one one eight zero three beside it. The root and the angle are the only things here that need rounding. The exact quantity to carry is A squared.

@words text="peak at t = φ/ω₀" sub="the quadrant of φ is the quadrant of (C₁, C₂)"
And the phase tells you when the cosine peaks: at t equals phi over omega nought. Pick the angle in the quadrant of the point C one, C two. It's rarely a neat multiple of pi, so the lab rounds it.

@art three-starts-one-period
Only the start two, zero has an amplitude equal to its starting displacement, because it starts at rest. And across all three, the period tile reads the same. Amplitude and phase belong to the start. The period belongs to the mass and the spring.

@chapter Where people slip
@list heading="Common slips" items="Amplitude is the starting displacement@The first|Adding x₀² + v₀² without dividing by ω₀@The second|Bigger amplitude, longer period@The third"
The first slip is taking the amplitude to be the starting displacement. The second is adding x nought squared and v nought squared without dividing by omega nought. Three squared plus eight squared is seventy three, not twenty five. And the third is thinking a bigger amplitude means a longer period.

@chapter Try it
@words text="start (1, 1),  ω₀ = 2" sub="check A² = 5/4 and tan φ = 1/2"
Your turn. From the start one, one on the same spring, find C one and C two yourself, remembering to divide by omega nought. Then check A squared and the tangent of the phase.

@end text="One cosine, one height, one shift"
You can try any start and read off its amplitude and phase, on Learn. That's learn dot get er done dot I O.
