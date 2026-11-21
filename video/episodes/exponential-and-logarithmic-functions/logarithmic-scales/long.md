---
format: long
lesson: exponential-and-logarithmic-functions/logarithmic-scales
title: Decibels, pH and magnitude: one idea, three scales
thumb: Equal steps, equal factors
---

@chapter One construction, three times
@title text="Logarithmic Scales" sub="Exponential and Logarithmic Functions" art=thumb
Decibels, pH and earthquake magnitude look like three different topics. They're one construction used three times: report the logarithm of a ratio, instead of the ratio. Then equal steps on the scale stand for equal factors in the quantity.

@art squashed-range
Here's why you'd want that. Sound you can hear runs from about ten to the minus twelve watts per square metre, at the threshold of hearing, to about ten squared, where damage starts. That's fourteen powers of ten. On a linear axis the quiet end is invisible. Report the exponent instead, and the range becomes zero to a hundred and forty.

@chapter Three scales
@math heading="Three scales" items="L = 10·log(I / I₀),     I₀ = 10⁻¹² W/m²@Decibels;;pH = −log[H⁺]@pH is minus;;M = log(A / A₀)@Magnitude"
Decibels are ten times the log of the intensity over a fixed reference, ten to the minus twelve. pH is minus the log of the hydrogen ion concentration. Magnitude is the log of the recorded amplitude over a reference amplitude.

@art acid-drops
The minus sign in pH makes ordinary solutions positive: a concentration of ten to the minus seven gives pH seven. It also flips the direction. A lower pH means more hydrogen ions.

@words text="S = k·log(Q / Q₀)" sub="k = 10 for dB,    −1 for pH,    1 for magnitude"
All three have one shape: S equals k times the log of Q over Q nought. The reference makes the argument a pure number, which it must be before a logarithm can touch it. And k sets the size of a step: ten for decibels, minus one for pH, one for magnitude.

@chapter A difference is a ratio
@math heading="The reference cancels" items="S₂ − S₁ = k·log(Q₂ / Q₁)@S two minus S one;;Q₂ / Q₁ = 10^((S₂ − S₁) / k)@So the ratio"
Subtract two readings and the reference cancels, by the quotient law. S two minus S one is k times the log of Q two over Q one. So the ratio of the quantities is ten to the difference over k. That's why anyone can compare two readings.

@math heading="Three comparisons" items="60 dB → 90 dB:    10^(30/10) = 1000× the intensity@Sixty to ninety;;pH 6 → pH 3:    10^(−3/−1) = 1000× the [H⁺]@pH six;;magnitude 5 → 7:    10² = 100× the amplitude@Magnitude five;;energy:    10^(1.5·2) = 1000×@the energy"
Sixty to ninety decibels is a difference of thirty, so the intensity ratio is ten to the thirty over ten, a thousand. pH six down to pH three is ten to the minus three over minus one, a thousand times the hydrogen ions. Magnitude five to seven is a hundred times the amplitude. And the energy is a thousand times.

@art seismograph
That energy figure comes from a separate relation, found by measurement: energy scales as ten to the one point five times the magnitude. Either way, magnitude seven isn't two more than five in any physical sense. It's a hundred times the amplitude.

@chapter Two machines aren't double
@art sound-waves
Two identical machines each measure sixty decibels. Run them together. The intensities add, so you have twice the intensity, and the level is sixty plus ten log two. That's about sixty three point oh one decibels, not a hundred and twenty.

@words text="2 sources: +3.01 dB        10 sources: +10 dB"
Ten identical machines give exactly seventy, since ten log ten is ten. Adding the readings would mean multiplying the intensities, because a sum of logarithms is the log of a product. Add the intensities first, then take the log once.

@chapter Reading a log axis
@art log-axis
On a log axis, the gridlines in each decade are unevenly spaced, and the pattern repeats. Between one and ten, the mark for two sits thirty point one percent of the way along, and the mark for five sits sixty nine point nine percent along. The same pattern appears between ten and a hundred.

@art straight-on-log
If y is a times b to the x, then log y is log a plus x log b, which is linear in x. So an exponential plotted on a log vertical axis is a straight line, with slope log b. A straight line there is evidence of a constant ratio per step.

@chapter Where people slip
@list heading="Common slips" items="Reading a difference as a factor@The first|Adding readings when the quantities add@The second|Reading pH the intuitive way round@The third"
The first is reading a difference as a factor, as if magnitude seven were twice magnitude five, or just two more. The second is adding readings when the quantities add. The third is reading pH the intuitive way round. pH two is more acidic than pH six, and a higher pH means fewer hydrogen ions.

@chapter Try it
@words text="72 dB → 92 dB" sub="difference 20,    k = 10"
Your turn. A sound rises from seventy two to ninety two decibels. The difference, twenty, and k, ten, are given. Finish the intensity ratio, ten to the twenty over ten, and explain why neither twenty nor ninety two over seventy two answers the question.

@end text="From a factor to a step, and back"
You can move a quantity and watch the reading, or move the reading and watch the quantity, on Learn. That's learn dot get er done dot I O.
