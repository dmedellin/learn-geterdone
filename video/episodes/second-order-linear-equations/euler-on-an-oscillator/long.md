---
format: long
lesson: second-order-linear-equations/euler-on-an-oscillator
title: Why Euler's method spirals off an oscillator, exactly
thumb: Exact fractions, wrong answer
---

@chapter The question
@title text="Euler on an Oscillator" sub="Second-Order Linear Equations" art=thumb
Here's a puzzle. Run Euler's method on the simplest oscillator, with every number an exact fraction, and the answer is still wrong. Not a little off from rounding. Exactly wrong.

@math heading="x″ + x = 0 as a system" items="x′ = v,  v′ = −x@x prime equals v;;x = cos t,  v = −sin t@From one, zero;;x² + v² = cos² t + sin² t = 1@cosine squared plus sine squared"
Written as a system, the oscillator is x prime equals v, and v prime equals minus x. From one, zero, the solution is x equals cosine t and v equals minus sine t. So x squared plus v squared is cosine squared plus sine squared, which is one.

@art unit-circle-path
The point moves round a circle of radius one and never leaves it. You can see that without the solution: the rate of x squared plus v squared is two x v plus two v times minus x, which is zero. That's what the equation conserves.

@chapter The Euler step
@math heading="Euler's method" items="xₙ₊₁ = xₙ + h·vₙ@x next equals;;vₙ₊₁ = vₙ − h·xₙ@v next equals"
Euler's method steps the pair forward. X next equals x plus h times v. V next equals v minus h times x. Both use the old values.

@art tangent-step
Each step moves along the tangent, in a straight line. And the tangent to a circle lies outside it.

@chapter Exactly how much
@math heading="Square and add" items="(xₙ + h·vₙ)² = xₙ² + 2h·xₙ·vₙ + h²·vₙ²@Square the first;;(vₙ − h·xₙ)² = vₙ² − 2h·xₙ·vₙ + h²·xₙ²@square the second;;sum = (1 + h²)·(xₙ² + vₙ²)@Add them"
How far outside? Square the first: x squared plus two h x v plus h squared v squared. Square the second: v squared minus two h x v plus h squared x squared. Add them, and the middle terms cancel. What's left is one plus h squared, times x squared plus v squared.

@words text="× (1 + h²) every step" sub="for every starting point"
So every step multiplies x squared plus v squared by exactly one plus h squared. That's pure algebra, and it holds for any starting point.

@art radius-triangle
And x squared plus v squared is the square of the point's distance from the centre. So a factor bigger than one, for every positive h, means every step pushes the point further from the circle.

@chapter Two steps by hand
@math heading="(1, 0),  h = 1/4" items="x₁ = 1,  v₁ = −1/4,  x₁² + v₁² = 17/16@The first step;;x₂ = 15/16,  v₂ = −1/2@The second;;x₂² + v₂² = 225/256 + 64/256 = 289/256 = (17/16)²@two hundred and twenty five"
Start at one, zero with h equals one quarter. The first step gives x one equals one, v one equals minus a quarter, so x squared plus v squared is seventeen sixteenths. The second gives fifteen sixteenths and minus a half. Squared and added, that's two hundred and twenty five over two fifty six, plus sixty four over two fifty six.

@words text="289/256 = (17/16)²" sub="the same factor again"
That's two eighty nine over two fifty six, which is seventeen sixteenths squared. The same factor, again.

@art euler-spiral
The point is outside the circle after the first step. And the polygon the lab draws spirals outward from the circle the true solution stays on.

@chapter Three step sizes
@math heading="To t = 6" items="h = 1/2,  12 steps:  5/4 per step,  (5/4)¹² ≈ 14.5519@h equals one half;;h = 1/4,  24 steps:  17/16,  (17/16)²⁴ ≈ 4.28444@h equals one quarter;;h = 1/8,  48 steps:  65/64,  (65/64)⁴⁸ ≈ 2.10476@h equals one eighth"
The three presets run to t equals six. With h equals one half, twelve steps of five quarters give about fourteen point five five. With h equals one quarter, twenty four steps of seventeen sixteenths give about four point two eight. With h equals one eighth, forty eight steps of sixty five sixty fourths give about two point one zero, all rounded.

@art three-spirals
The total gain falls as h falls, but it never reaches one. The natural log of the gain roughly halves each time h does, which is how a method whose error is proportional to h behaves. A smaller step slows the growth. It can't remove it.

@chapter Where people slip
@list heading="Common slips" items="Euler keeps what the equation keeps@The first|One plus h squared is negligible@The second|Blaming rounding@The third"
The first slip is assuming Euler's method conserves what the equation conserves. It doesn't know about it. The second is calling one plus h squared negligible because it's close to one. It compounds. And the third is blaming rounding.

@art compounding-bars
Seventeen sixteenths is only a sixteenth more than one, but after twenty four steps the radius at t equals six is about two point zero seven times what it should be. As for rounding, seventeen sixteenths is exact. The growth is in the recipe.

@chapter Try it
@words text="h = 1/2 from (1, 0)" sub="x₁² + v₁² should be 5/4"
Your turn. Take the first Euler step from one, zero with h equals one half, by hand. Check that x squared plus v squared comes out as five quarters, exactly one plus h squared.

@end text="Exact arithmetic, approximate method"
You can step the oscillator and watch the polygon leave the circle, on Learn. That's learn dot get er done dot I O.
