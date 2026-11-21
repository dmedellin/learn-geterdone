---
format: long
lesson: oscillators-damping-and-resonance/energy-and-the-phase-ellipse
title: Energy and the phase ellipse: why an undamped spring never slows down
thumb: The energy never leaves
---

@chapter The question
@title text="Energy and the Phase Ellipse" sub="Oscillators, Damping and Resonance" art=thumb
At the end of each swing, the mass stops dead for an instant. So where did its energy go? Nowhere. It's in the spring.

@art energy-trade
An undamped swing trades energy between the moving mass and the stretched spring. At the ends of the swing, the mass is still and it's all in the spring. Passing through rest, the spring is relaxed and it's all in the motion. In between, it's shared.

@math heading="Energy" items="E = ½m·v² + ½k·x²@E equals;;E₀ = ½m·v₀² + ½k·x₀²@its starting value"
The energy is E equals a half m v squared, plus a half k x squared. Kinetic energy, plus the energy stored in the spring. Its starting value, E nought, uses the starting position and velocity.

@words text="½" sub="check it first, in both terms"
That factor of a half appears in both terms, and it's the first thing to check. Leave it out and the ratio is still right, but the number is twice the true energy.

@chapter It's conserved
@math heading="Differentiate" items="(½m·v²)′ = m·v·x″@a half m v squared;;(½k·x²)′ = k·x·v@a half k x squared;;E′ = v·(m·x″ + k·x) = 0@So E prime"
Differentiate with the chain rule. The rate of a half m v squared is m v times x double prime. The rate of a half k x squared is k x times v. So E prime is v times the bracket m x double prime plus k x, and by the equation, that bracket is zero.

@words text="with a damper:  E′ = −c·v² ≤ 0"
So E never changes. With a damper, the bracket is minus c x prime instead, and E prime is minus c v squared, which is never positive. Then the energy only falls, which is the next module.

@chapter The first start
@math heading="m = 1,  k = 4,  start (3, 8)" items="E₀ = ½·64 + ½·4·9 = 32 + 18 = 50@a half of sixty four;;x = 5, v = 0:  ½·4·25 = 50@At x equals five;;x = 0, v = 10:  ½·100 = 50@at x equals zero"
With m equals one, k equals four, and a start at three, eight, E nought is a half of sixty four plus a half of four times nine. Thirty two plus eighteen, fifty. At x equals five and v equals zero, it's a half of four times twenty five, fifty. And at x equals zero and v equals ten, a half of a hundred, fifty.

@art turning-point
That turning point at five is where people think energy is lost, because the mass stops. But the kinetic part has become spring energy, all fifty of it. A moment later the mass is moving again.

@chapter The ellipse
@math heading="Divide by E₀" items="x²/(2E₀/k) + v²/(2E₀/m) = 1@Divide the energy;;x²/A² + v²/(A·ω₀)² = 1@an ellipse"
Now plot each instant as a point, position against velocity. Divide the energy equation by E nought. The first denominator is exactly A squared, and the second is A omega nought, squared. So the path is an ellipse.

@art ellipse-axes
Its semi-axis along x is the amplitude, A. Along v it's A times omega nought, the peak speed. For the first start, those are five and ten.

@art phase-ellipse
The point goes round once per period, clockwise. At the top, where v is positive, x is increasing, so the point moves right. The shape is set by omega nought alone, and the size by the start.

@words text="m = 2,  k = 5,  start (1, 0)" sub="E₀ = 5/2,   A² = 2E₀/k = 1"
A heavier mass, released from rest: m equals two, k equals five, start at one, zero. E nought is five halves, and A squared is two E nought over k, one, which is x nought squared, as it should be. For a start at rest, the mass isn't in E nought at all.

@chapter Where people slip
@list heading="Common slips" items="Energy is lost at the turning points@The first|The ellipse is a graph against time@The second|The ellipse should be a circle@The third"
The first slip is believing energy is lost at the turning points. The second is reading the ellipse as a graph of x against time. The third is expecting a circle.

@art ellipse-vs-time
The ellipse has no time axis. Each point is a state, and time is how fast the point goes round, once per period. The graph of x against t is the cosine from the last lesson, a different picture of the same motion.

@art circle-vs-ellipse
It's a circle only when A and A omega nought are equal, which needs omega nought equals one. On the first start they're five and ten.

@chapter Try it
@math heading="x²/25 + v²/100 = 1" items="start (3, 8):  9/25 + 64/100 = ?@nine over twenty five"
Your turn. The first start's ellipse is x squared over twenty five plus v squared over a hundred equals one. Check that the starting point three, eight is on it: work out nine over twenty five plus sixty four over a hundred. If it isn't one, there's a slip in E nought, A or omega nought.

@end text="Trade, never lose"
You can watch the point go round its ellipse while the energy holds still, on Learn. That's learn dot get er done dot I O.
