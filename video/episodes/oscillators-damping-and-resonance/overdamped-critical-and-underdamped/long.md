---
format: long
lesson: oscillators-damping-and-resonance/overdamped-critical-and-underdamped
title: Overdamped, critical or underdamped? One discriminant decides
thumb: Compare c with 2√(mk)
---

@chapter The question
@title text="Overdamped, Critical and Underdamped" sub="Oscillators, Damping and Resonance" art=thumb
Add a damper to a spring, and does it still swing? One number decides, and you can compute it before solving anything.

@art damper-strengths
With a damper, the equation is m x double prime plus c x prime plus k x equals zero. The previous course solved every equation like that. Look for e to the r t, and the roots of m r squared plus c r plus k decide the rest. What's new is what those roots mean for a spring.

@chapter Three kinds
@math heading="The characteristic equation" items="m·r² + c·r + k = 0@m r squared;;r = (−c ± √(c² − 4mk)) / (2m)@the roots are;;c_crit = 2√(m·k)@The critical damping"
The quadratic is m r squared plus c r plus k equals zero, so the roots are minus c, plus or minus the square root of c squared minus four m k, all over two m. The critical damping is the c that makes that discriminant zero: two times the square root of m k.

@list heading="With c > 0" items="c² − 4mk > 0:  overdamped@Positive|c² − 4mk = 0:  critically damped@zero|c² − 4mk < 0:  underdamped@negative"
Positive, and the motion is overdamped. Zero, and it's critically damped, the borderline. And negative, and it's underdamped. With no damper at all, the lab calls it undamped.

@art three-dampers
Here are all three from the same start. Two real decays and no oscillation, the borderline, and a swing inside a shrinking envelope.

@chapter One spring, three dampers
@math heading="m = 1" items="k = 4, c = 5:  (r + 1)(r + 4),  disc 9@c equals five;;k = 4, c = 4:  (r + 2)²,  disc 0@c equals four;;k = 5, c = 2:  r = −1 ± 2i,  disc −16@c equals two"
Keep m equals one. With k equals four and c equals five, the quadratic factors as r plus one times r plus four, and the discriminant is nine. With c equals four, it's r plus two, squared, and the discriminant is zero. With k equals five and c equals two, the discriminant is minus sixteen, and the roots are minus one plus or minus two i.

@art overdamped-creep
The first is overdamped. The roots are minus one and minus four, so x is C one e to the minus t plus C two e to the minus four t. Neither term oscillates. The mass slides back toward rest, passing through it once at most. Its critical value is four, and five is above it.

@art underdamped-wave
The third is underdamped. X is e to the minus t, times C one cosine two t plus C two sine two t, an oscillation inside a decay. Its critical value is two root five, about four point four seven two one four, and two is well below it.

@words text="c  vs  c_crit" sub="below: oscillates · at: roots merge · above: two real decays"
So it's one comparison, c against the critical value. Below it, the mass oscillates. At it, the roots merge. Above it, they separate into two real decays.

@chapter Stronger is not quicker
@art critical-return
You'd expect a bigger damper to stop the mass sooner. Past the critical value, it doesn't. The slow root controls how long it takes. For c equals five it's minus one, giving e to the minus t. Critical damping, c equals four, has minus two twice, giving C one plus C two t, times e to the minus two t. Eventually that's far smaller.

@math heading="k = 4,  c = 10" items="disc = 100 − 16 = 84@a hundred minus sixteen;;r = −5 ± √21@minus five plus or minus;;−1 < −5 + √21 < 0@between minus one and zero"
The lab's fourth preset pushes further. With c equals ten, the discriminant is a hundred minus sixteen, eighty four, and the roots are minus five plus or minus root twenty one. Root twenty one is between four and five, so the slow root is between minus one and zero.

@art creeping-return
Ten units of damper make the return slower than five. The damper holds the mass so firmly that it creeps.

@chapter Where people slip
@list heading="Common slips" items="More damping always means quicker@The first|Not crossing zero means critical@The second|The plus sign means growth@The third"
The first slip is believing more damping always means a quicker return. Critical damping is the quickest of the non-oscillating cases, not the strongest. The second is calling any motion that doesn't cross zero critical. C equals five doesn't cross zero from one, zero, but its discriminant is nine. The third is reading minus one plus or minus two i as growing. The real part is minus one.

@chapter Try it
@words text="m = 1,  k = 4,  c = 5" sub="c_crit = 2√(1·4) = 4"
Your turn. Take m equals one and k equals four, and work out the critical damping. Then classify a damper of five twice, once by the sign of the discriminant and once by comparing it with the critical value. The two checks should agree. If they don't, one has a slip.

@end text="Compare c with 2√(mk)"
You can slide the damper through all three kinds and watch the roots move, on Learn. That's learn dot get er done dot I O.
