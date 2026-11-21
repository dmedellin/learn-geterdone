---
format: long
lesson: oscillators-damping-and-resonance/forced-oscillation
title: Forced oscillation: why a fast push moves the mass the wrong way
thumb: With the push, or against it?
---

@chapter The question
@title text="Forced Oscillation" sub="Oscillators, Damping and Resonance" art=thumb
Push a mass on a spring back and forth. Does it move with your push? Below a certain frequency it does. Above it, it moves the opposite way.

@art pushed-mass
Until now, every oscillator equation had zero on the right, and the motion was whatever the start left it. Now add an outside force that alternates with frequency omega and size F nought. Keep the damper off, so nothing carries the answer away.

@math heading="The forced equation" items="m·x″ + k·x = F₀·cos(ωt)@m x double prime;;x = x_p + C₁cos(ω₀t) + C₂sin(ω₀t)@the whole motion"
The equation is m x double prime plus k x equals F nought cosine omega t. And the whole motion is one particular solution, x p, plus the free motion, whose constants come from the start. The part fixed by the push alone is x p.

@chapter Finding the amplitude
@math heading="Try x_p = A·cos(ωt)" items="x_p″ = −ω²·A·cos(ωt)@Its second rate;;m·(−ω²·A) + k·A = F₀@Substitute;;A = F₀/(k − m·ω²) = F₀/(m·(ω₀² − ω²))@So A"
Try A cosine omega t. Its second rate is minus omega squared A cosine omega t, a multiple of itself. Substitute, and match the cosines: m times minus omega squared A, plus k A, equals F nought. So A is F nought over k minus m omega squared, which is F nought over m times omega nought squared minus omega squared.

@words text="ω² ≠ ω₀²" sub="no sine term needed"
A sine term would need k minus m omega squared times B to be zero, so B is zero. And dividing is allowed exactly when omega squared isn't omega nought squared. That's why the next lesson exists.

@chapter Four pushes
@math heading="m = 1,  k = 4,  F₀ = 3,  ω₀ = 2" items="ω = 1:  A = 3/(4 − 1) = 1@omega equals one;;ω = 3/2:  A = 3/(4 − 9/4) = 12/7@three halves;;ω = 7/4:  A = 3/(4 − 49/16) = 16/5@seven quarters;;ω = 3:  A = 3/(4 − 9) = −3/5@omega equals three"
Take m one, k four and a push of size three, so omega nought is two. At omega equals one, A is three over four minus one, which is one. At three halves, three over four minus nine quarters, twelve sevenths. At seven quarters, sixteen fifths. And at omega equals three, three over four minus nine, minus three fifths.

@art in-step-waves
Below the natural frequency, A is positive. At omega equals one, x p is cosine t, and the mass peaks when the push peaks.

@math heading="From rest, ω = 1" items="x = cos(t) − cos(2t)@cosine t minus cosine two t;;x″ + 4x = 3cos(t)@check"
Started at rest at the rest position, the whole motion is cosine t minus cosine two t. Check it: the cosine two t terms cancel and three cosine t is left. The lab draws that sum, and reports the first cosine, the part fixed by the push.

@art two-cosine-sum
So the curve you actually see from rest is the push's part and the free part together, two frequencies at once. Neither cosine on its own is the whole motion.

@art against-push-waves
Above the natural frequency, A is negative. At omega equals three, the response is minus three fifths cosine three t. When the force pulls right, the mass goes left. It's too sluggish to follow, still going the old way when the force turns.

@chapter Making sense of it
@art slow-pull
At the extremes the formula makes sense. As omega falls toward zero, the push becomes a slow steady pull, and A tends to F nought over k, the stretch Hooke's law gives for that force.

@art amplitude-vs-frequency
As omega rises, the amplitude shrinks toward zero from below. Inertia wins. And near omega nought, the denominator is small and the amplitude is large, twelve sevenths and then sixteen fifths.

@chapter Where people slip
@list heading="Common slips" items="The response is always in step@The first|It swings at its own frequency@The second|Subtracting frequencies, not squares@The third"
The first slip is believing the response is always in step with the push. The second is expecting the forced part to swing at its own natural frequency. It runs at the pushing frequency. And the third is subtracting the frequencies instead of their squares.

@math heading="ω = 3/2" items="✓  3/(4 − 9/4) = 12/7@the right answer;;✗  3/(2 − 3/2) = 6@would give six"
For omega equals three halves, the right answer is three over four minus nine quarters, twelve sevenths. Using omega nought minus omega, a half, would give six, more than three times too large. The second rate brings down omega squared, so the squares belong there.

@chapter Try it
@words text="ω = 7/4" sub="4 − 49/16 = 15/16"
Your turn. Work out A for the push at seven quarters yourself, as a fraction. Do the subtraction underneath first, then divide, and check you get sixteen fifths. Then say whether the mass moves with the push.

@end text="Read the sign of A"
You can tune the push and watch the amplitude change sign, on Learn. That's learn dot get er done dot I O.
