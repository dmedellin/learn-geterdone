---
format: long
lesson: oscillators-damping-and-resonance/underdamped-motion-and-the-envelope
title: Underdamped motion: the pseudo-frequency, the envelope and the peak ratio
thumb: It rings, and it fades
---

@chapter The question
@title text="Underdamped Motion and the Envelope" sub="Oscillators, Damping and Resonance" art=thumb
An underdamped oscillator keeps swinging while it fades. Three numbers describe it completely: how fast it swings, how fast it fades, and how much smaller each peak is than the last.

@art ringing-bell
They're the same three numbers that describe a ringing bell or a car's suspension after a bump. The frequency is the note, the envelope rate is how long it rings, and the peak ratio is how much quieter it gets each time round.

@chapter Reading the roots
@math heading="c² − 4mk < 0" items="r = −c/(2m) ± i·√(4mk − c²)/(2m)@the roots are;;α = −c/(2m)@The real part;;ω_d² = k/m − c²/(4m²)@squared"
With c squared minus four m k negative, the roots are minus c over two m, plus or minus i times the square root of four m k minus c squared, over two m. The real part, alpha, is minus c over two m. The imaginary part is the pseudo-frequency, omega d. Squared, it's k over m minus c squared over four m squared.

@words text="ω_d² = ω₀² − (c/(2m))²" sub="so ω_d < ω₀ for every c > 0"
That's omega nought squared minus a square. So damping doesn't only shrink the swing. It slows it down too. The pseudo-period is two pi over omega d. It's called pseudo because the motion keeps shrinking, so it never truly repeats.

@art envelope-wave
The solution is e to the alpha t, times C one cosine omega d t plus C two sine omega d t. The bracket is a swing of constant size A, so the whole thing stays inside the curves plus and minus A e to the alpha t. That's the envelope, falling at the rate c over two m.

@chapter The peak ratio
@art peak-ratio
Here's the neat part. The bracket repeats every pseudo-period. Over that time, the exponential multiplies by e to the alpha T d. So x one pseudo-period later is e to the alpha T d times x now, at every t. And the same holds for its rate.

@words text="each peak = e^(α·T_d) × the last" sub="= e^(−c·T_d/(2m))"
So if x has a peak, where its rate is zero, the next peak is exactly one pseudo-period later, and e to the alpha T d times as big. Each one comes a little earlier than the bracket's own peak, but they're still evenly spaced.

@chapter Three presets
@math heading="m = 1,  c = 2,  k = 5" items="ω₀² = 5,  c/(2m) = 1@omega nought squared is five;;ω_d² = 5 − 1 = 4,  ω_d = 2,  T_d = π@five minus one;;peak ratio e^(−π) ≈ 0.0432139@e to the minus pi"
The first preset: m one, c two, k five. Omega nought squared is five and the rate is one. Omega d squared is five minus one, four, so omega d is two and the pseudo-period is pi. Each peak is e to the minus pi times the last, about zero point zero four three two one three nine. That's a very fast fade.

@art slower-swing
Compare the undamped period of this spring, two pi over root five, about two point eight one, with the pseudo-period pi, about three point one four. The damped oscillation is slower.

@math heading="m = 1,  c = 1/2,  k = 4" items="c/(2m) = 1/4@the rate is a quarter;;ω_d² = 4 − 1/16 = 63/16@four minus a sixteenth;;peak ratio ≈ 0.453116@about zero point four five"
A light damper: m one, c a half, k four. The rate is a quarter, and omega d squared is four minus a sixteenth, sixty three sixteenths. Barely below four. And the peak ratio is about zero point four five three one one six. Damping shows first in the envelope, and only second in the frequency.

@art heavy-mass-fade
Now a heavier mass: m two, c two, k five. The rate is c over two m, a half, and omega d squared is five halves minus a quarter, nine quarters, so omega d is three halves. Doubling the mass halved the envelope rate, so it fades more slowly. The peak ratio is about zero point one two three, against zero point zero four three.

@chapter Where people slip
@list heading="Common slips" items="Damping leaves the frequency alone@The first|Taking c as the envelope rate@The second|Using the natural period for the ratio@The third"
The first slip is thinking damping changes the amplitude but not the frequency. The second is taking c as the envelope rate, instead of c over two m. And the third is using the natural period to compute the peak ratio. The peaks are one pseudo-period apart, so e to the minus two pi over root five is the wrong number.

@art light-damper
The frequency change is small for a light damper, sixty three sixteenths against four. But near the critical damping, omega d falls all the way to zero.

@chapter Try it
@words text="m = 2,  c = 2,  k = 5" sub="T_d = 4π/3"
Your turn. For the heavier mass, the pseudo-period is four pi over three. Write the peak ratio as e to a power, using the rate a half, and check it against the lab's zero point one two three.

@end text="Swing, fade, and the ratio"
You can watch the envelope and measure the peak ratio, on Learn. That's learn dot get er done dot I O.
