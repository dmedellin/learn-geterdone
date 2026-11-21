---
format: long
lesson: oscillators-damping-and-resonance/resonance-and-beats
title: Resonance and beats: what happens when you push at the natural frequency
thumb: It climbs, and never stops
---

@chapter The question
@title text="Resonance and Beats" sub="Oscillators, Damping and Resonance" art=thumb
What happens if you push a spring at exactly its natural frequency? The amplitude formula from last time has a zero underneath. That isn't a large answer. It's no answer at all.

@math heading="ω = ω₀" items="m·(−ω₀²·A) + k·A = (k − m·ω₀²)·A = 0@Substitute;;0 = F₀  ✗@which is impossible"
Substitute A cosine omega nought t, and the left side is k minus m omega nought squared, times A. But k is m omega nought squared, so that's zero, for every A. You'd need zero to equal F nought, which is impossible.

@words text="multiply by t" sub="as for a repeated root"
The guess is already a solution of the free equation. That's the situation of a repeated root, and the cure is the same: multiply by t.

@chapter The resonant solution
@math heading="Try x_p = B·t·sin(ω₀t)" items="x_p″ = 2B·ω₀·cos(ω₀t) − B·ω₀²·t·sin(ω₀t)@the second rate;;m·x_p″ + k·x_p = 2m·B·ω₀·cos(ω₀t)@the t sine terms cancel;;B = F₀/(2m·ω₀)@So B"
Try B t sine omega nought t. By the product rule, the second rate is two B omega nought cosine omega nought t, minus B omega nought squared t sine omega nought t. Substitute, and the t sine terms cancel against the spring. That leaves two m B omega nought cosine, the very cosine the push needs. So B is F nought over two m omega nought.

@math heading="m = 1,  k = 4,  F₀ = 3" items="B = 3/(2·1·2) = 3/4@three over two times one times two;;x_p = (3/4)·t·sin(2t)@three quarters;;x_p″ + 4x_p = 3·cos(2t)@the push exactly"
With m one, k four and a push of three, omega nought is two. B is three over two times one times two, three quarters. So x p is three quarters t sine two t. Its second rate is three cosine two t minus three t sine two t, so x p double prime plus four x p is three cosine two t, the push exactly.

@art resonant-ramp
Started at rest, that's the whole motion. Its amplitude is three t over four: three at t equals four, and thirty at t equals forty. It has no bound, but it's finite at every moment.

@art climbing-steps
It doesn't leap to infinity when the push switches on. It climbs by the same amount in every unit of time. The model has no damper to stop the climb. A real structure has one, or breaks.

@chapter Beside resonance
@art two-close-waves
Now move the push to three halves. The previous lesson gives A equals twelve sevenths, and from rest the motion is A times cosine omega t minus cosine omega nought t. Two cosines of nearby frequency, drifting in and out of step.

@math heading="ω = 3/2" items="x = 2A·sin((ω₀ + ω)t/2)·sin((ω₀ − ω)t/2)@a product;;(ω₀ + ω)/2 = 7/4,   (ω₀ − ω)/2 = 1/4@seven quarters;;x = (24/7)·sin(7t/4)·sin(t/4)@twenty four sevenths"
An identity for the difference of two cosines turns that into a product. Here the half sum is seven quarters and the half difference is a quarter. So x is twenty four sevenths, times sine of seven t over four, times sine of t over four.

@art beats-wave
That's a fast sine inside a slow one. The slow factor is an envelope that swells and shrinks. That's a beat.

@chapter The beat period
@math heading="Beat period" items="2π/|ω₀ − ω|@two pi over;;ω = 3/2:  2π/(1/2) = 4π ≈ 12.5664@a half"
The beat period is two pi over the gap between the frequencies. For three halves, that's two pi over a half, four pi, about twelve point five six six four, rounded. The biggest swing is twenty four sevenths, twice the steady amplitude.

@art envelope-period
Careful here. The slow sine itself repeats every eight pi. But the size of the swing is its absolute value, and that repeats every four pi. Swell to swell is four pi.

@art stretching-beats
Move the push toward omega nought, and the swells grow taller and the beat period grows longer. The preset at seven quarters is taller and slower than at three halves. In the limit, the first swell never ends, and you're back on the ramp. The lab demonstrates that limit, and it isn't proved here.

@chapter Where people slip
@list heading="Common slips" items="Resonance is infinite at once@The first|The slow sine's period is the beat period@The second|A bigger cosine and sine will do@The third"
The first slip is thinking resonance means infinite amplitude at once. It's three t over four, finite at every moment. The second is taking the slow sine's period, eight pi, as the beat period. It's four pi. And the third is trying a bigger cosine and sine at resonance. They make the left side zero. The factor t is what does the work.

@chapter Try it
@words text="ω = 7/4" sub="beat period 2π/|2 − 7/4|"
Your turn. For the push at seven quarters, work out the beat period from the formula. Then compare it with four pi at three halves, and say which way it moved.

@end text="Ramp at resonance, beats beside it"
You can tune the push onto the spring and watch the beats stretch into a ramp, on Learn. That's learn dot get er done dot I O.
