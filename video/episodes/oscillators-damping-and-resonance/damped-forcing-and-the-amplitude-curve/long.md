---
format: long
lesson: oscillators-damping-and-resonance/damped-forcing-and-the-amplitude-curve
title: Damped forcing: where the amplitude curve really peaks
thumb: The peak is not at ω₀
---

@chapter The question
@title text="Damped Forcing and the Amplitude Curve" sub="Oscillators, Damping and Resonance" art=thumb
Push a damped spring steadily. At which frequency does it respond most? Not at its natural frequency. The peak sits lower, and with a heavy enough damper, there's no peak at all.

@art damped-pushed-mass
Put the damper back: m x double prime plus c x prime plus k x equals F nought cosine omega t. Every free solution dies away, so after a while only the part fixed by the push remains.

@art settling-response
That's the steady state, and its size is the steady amplitude. The lab reports that amplitude only, not the way the motion settles into it.

@chapter The steady amplitude
@math heading="x_p = G·cos(ωt) + H·sin(ωt)" items="P = k − m·ω²,   Q = c·ω@Write P;;cosines:  P·G + Q·H = F₀@the cosines;;sines:  −Q·G + P·H = 0@the sines"
The damper turns a cosine into a sine, so try G cosine omega t plus H sine omega t. Substitute and write P for k minus m omega squared, and Q for c omega. Matching the cosines gives P G plus Q H equals F nought. Matching the sines gives minus Q G plus P H equals zero.

@math heading="Solve" items="G = F₀·P/(P² + Q²),   H = F₀·Q/(P² + Q²)@Eliminate;;A² = G² + H² = F₀²/(P² + Q²)@The amplitude squared"
Eliminate, and G is F nought P over P squared plus Q squared, and H is F nought Q over the same thing. The amplitude squared is G squared plus H squared, which comes to F nought squared over P squared plus Q squared.

@words text="P² + Q² > 0" sub="Q² = (c·ω)² is positive once c > 0"
P can be zero, at the natural frequency, but Q squared is positive for every positive omega. So the denominator never reaches zero, and the divergence of the last lesson is gone.

@math heading="m = 1,  c = 2,  k = 5,  F₀ = 3,  ω = 1" items="P = 4,  Q = 2,  P² + Q² = 20@five minus one;;G = 3/5,  H = 3/10@G is three fifths;;A² = 9/25 + 9/100 = 9/20@nine twenty fifths"
Take m one, c two, k five, a push of three at omega equals one. P is five minus one, four, and Q is two, so the denominator is twenty. G is three fifths and H is three tenths, and A squared is nine twenty fifths plus nine hundredths, nine twentieths, exact.

@chapter Where the peak is
@art upward-parabola-min
The amplitude is largest where the denominator is smallest. Written in u equals omega squared, that denominator is an upward parabola.

@math heading="The peak" items="ω_r² = k/m − c²/(2m²)@least at;;A_max² = F₀²/(c²·ω_d²)@the peak;;ω_r² < ω_d² < ω₀²@three different numbers"
It's least at omega r squared equals k over m minus c squared over two m squared. There, the peak amplitude squared is F nought squared over c squared omega d squared, with the ringing frequency. And the peak, the ringing and the natural frequency are three different numbers, in that order.

@math heading="m = 1,  c = 2,  k = 5" items="D = u² − 6u + 25 = (u − 3)² + 16@u squared minus six u;;ω_r² = 3,  D = 16@omega r squared is three;;A_max² = 9/16,  A_max = 3/4@nine sixteenths"
For the preset, the denominator is u squared minus six u plus twenty five, which is u minus three, squared, plus sixteen. So omega r squared is three, where the denominator is sixteen. A max squared is nine sixteenths, so A max is three quarters.

@art three-frequencies
So here the three numbers are three, four and five. The peak at omega squared equals three, the free ringing at four, and the natural frequency at five.

@art amplitude-curve-peak
The natural frequency squared is five, above the peak. At five itself, the denominator is twenty, and A squared is nine twentieths, less than nine sixteenths. The natural frequency doesn't give the largest response.

@chapter No peak at all
@words text="peak needs c² < 2mk" sub="ringing needs c² < 4mk"
The peak needs omega r squared to be positive, which means c squared less than two m k. Free ringing only needs c squared less than four m k. That's a stricter condition for the peak.

@art no-peak-curve
With m one, k four and c three, the motion is underdamped, since nine is less than sixteen. But nine is above eight, so there's no peak. The amplitude just falls steadily from F nought over k. A damper can be light enough to ring and heavy enough to remove the peak.

@chapter Where people slip
@list heading="Common slips" items="The peak is at ω₀@The first|A peak whenever it rings@The second|Using ω₀ in the peak height@The third"
The first slip is believing the peak is at omega nought. Even at c equals a half and k four, it's at thirty one eighths against four. The second is expecting a peak whenever the motion rings. And the third is using omega nought in the peak height. It's F nought over c omega d, three quarters here.

@chapter Try it
@words text="ω = 7/4" sub="P = 31/16,  Q = 7/2"
Your turn. Root three is irrational, so try omega equals seven quarters, just above it. P is thirty one sixteenths and Q is seven halves. Square them, then add, then divide, and check A squared is twenty three oh four over four oh nine seven, just under nine sixteenths.

@end text="Find the real peak"
You can sweep the push frequency and watch the peak move below omega nought, on Learn. That's learn dot get er done dot I O.
