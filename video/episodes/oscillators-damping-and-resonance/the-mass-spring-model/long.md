---
format: long
lesson: oscillators-damping-and-resonance/the-mass-spring-model
title: The mass-spring model: where m·x'' + c·x' + k·x = 0 comes from
thumb: Stiffer is faster, heavier is slower
---

@chapter The model
@title text="The Mass–Spring Model" sub="Oscillators, Damping and Resonance" art=thumb
Every oscillator in this course is a version of one thing: a mass on a spring. Two laws turn it into an equation, and one number tells you how fast it swings.

@art mass-on-spring
Put a mass m on a spring and let it move along a line. Call x its position, measured from the spot where the spring is neither stretched nor squeezed. Units are left out. Any consistent set will do.

@chapter Two laws
@art stretch-and-pull
Hooke's law says the spring's force is minus k times x, where k is a positive spring constant. The force is proportional to the stretch and points the other way. A stiffer spring has a bigger k. Real springs obey it for small stretches, and here it's an assumption.

@words text="m·x″ = total force" sub="Newton's law"
Newton's law says mass times acceleration is the total force. Acceleration is x double prime, so m x double prime equals the spring's force plus anything else that acts.

@art damper-plunger
A damper, like a plunger in oil, opposes the motion with a force proportional to the speed. That's minus c times x prime, for a damping constant c that's zero or more.

@math heading="The equation" items="m·x″ = −k·x − c·x′@m x double prime;;m·x″ + c·x′ + k·x = 0@Move everything;;c = 0:  x″ = −(k/m)·x = −ω₀²·x@With no damper"
So m x double prime equals minus k x minus c x prime. Move everything to the left, and you get m x double prime plus c x prime plus k x equals zero. With no damper, c is zero, and x double prime equals minus k over m times x. Call k over m omega nought squared.

@chapter Free swinging
@math heading="ω₀² = k/m" items="x = C₁cos(ω₀t) + C₂sin(ω₀t)@the general solution;;T = 2π/ω₀@the period"
That's the equation from the last course, with omega nought in place of beta. So the general solution is C one cosine omega nought t plus C two sine omega nought t. And the period is two pi over omega nought.

@art same-period-two-heights
The period doesn't depend on the start. Replace t by t plus the period, and the argument grows by two pi, so cosine and sine repeat. The constants only multiply. Start at one or at five, and the curve is five times as tall with the same period.

@chapter A worked example
@math heading="m = 1,  k = 4" items="ω₀² = 4,  ω₀ = 2@omega nought squared is four;;T = 2π/2 = π ≈ 3.14159@The period;;x = cos(2t):  x″ = −4cos(2t) = −4x@Check"
Take m equals one and k equals four. Then omega nought squared is four, and omega nought is two. The period is two pi over two, which is pi, about three point one four one five nine, rounded. Check cosine of two t: its second rate is minus four cosine two t, which is minus four x.

@art stiff-vs-soft
Now change one number at a time. Stiffen the spring to k equals nine with m equals one, and omega nought is three. The period drops to two pi over three, shorter than pi.

@art heavy-vs-light
Double the mass instead, with k still four. Omega nought squared halves, omega nought is root two, and the period is two pi over root two, about four point four four two eight eight. Heavier is slower.

@words text="m = 2,  k = 5:  ω₀² = 5/2" sub="ω₀ = √(5/2) = √10/2"
And sometimes the frequency is a surd. With m equals two and k equals five, omega nought squared is five halves, and omega nought is root ten over two. The lab keeps five halves exact, and rounds only the value it prints beside the surd.

@chapter Where people slip
@list heading="Common slips" items="Heavier means faster@The first|Reading ω₀ as the period@The second|A bigger swing takes longer@The third"
The first slip is thinking a heavier mass swings faster because it has more energy. The mass isn't even in the energy of a release from rest. The second is reading omega nought as the period. With omega nought equals two, the period is pi, not two. The third is expecting a bigger swing to take longer.

@chapter Try it
@words text="m = 1,  k = 9" sub="ω₀ = 3,  T = 2π/3"
Your turn. Take m equals one and k equals nine. Find omega nought and the period, then check cosine of three t by substitution. Then double the mass and predict which way the period moves.

@end text="Stiffer is faster, heavier is slower"
You can change the mass and the spring and watch the period move, on Learn. That's learn dot get er done dot I O.
