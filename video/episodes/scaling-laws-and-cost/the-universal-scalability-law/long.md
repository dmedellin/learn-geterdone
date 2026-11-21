---
format: long
lesson: scaling-laws-and-cost/the-universal-scalability-law
title: The universal scalability law: when more machines mean less
thumb: Past the peak, it falls
---

@chapter Two more charges
@title text="The Universal Scalability Law" sub="Scaling Laws and Cost" art=thumb
Amdahl's law says adding machines eventually stops helping. The universal scalability law says something worse. Past a point, adding machines makes throughput fall.

@math heading="Relative capacity" items="C(N) = N / (1 + α(N − 1) + βN(N − 1))@C of N;;α:  contention@alpha is contention;;β:  coherency@beta is coherency"
C of N is capacity in multiples of one machine. It's N, over one, plus alpha times N minus one, plus beta times N times N minus one. Alpha is contention. Beta is coherency. And C of one is one, by construction.

@art three-charges
Read the denominator as three charges. The one is the work itself. Alpha times N minus one is contention, what the others cost you while queueing for something only one machine can hold. It's linear. And beta times N times N minus one is the cost of keeping every machine's state in agreement with every other's.

@art pair-mesh
That last term is the only quadratic one. N machines have N times N minus one over two pairs, and a protocol where each must reconcile with each pays for that count. The numerator grows like N. That term grows like N squared. One of them wins eventually.

@chapter Plateau, or peak
@art plateau-vs-peak
Take alpha as one fiftieth and beta as zero. The curve climbs toward one over alpha, fifty times, and never turns down. That's the plateau. Now set beta to one ten thousandth. At ten machines the new term is nothing. At two hundred, it's nearly half the denominator.

@chapter Finding the peak
@math heading="Compare neighbours" items="C(N + 1) ≤ C(N)  ⟺  β·N(N + 1) ≥ 1 − α@compare C of N plus one;;(1 − α)/β = (49/50)/(1/10000) = 9800@nine thousand eight hundred"
You don't need calculus. Compare C of N plus one with C of N, cross multiply, and almost everything cancels. What's left is: beta times N times N plus one is at least one minus alpha. Here one minus alpha over beta is nine thousand eight hundred.

@math heading="Two products" items="98 × 99 = 9 702 < 9 800@ninety eight times ninety nine;;99 × 100 = 9 900 ≥ 9 800@ninety nine times a hundred;;N* = 99@the peak is ninety nine"
Ninety eight times ninety nine is nine thousand seven hundred and two, short. So the ninety ninth machine still helps. Ninety nine times a hundred is nine thousand nine hundred, enough. So the hundredth doesn't. The peak is ninety nine, by comparing two products of integers.

@art neighbour-compare
At the peak, capacity is four hundred and ninety five thousand over nineteen thousand six hundred and fifty one, about twenty five point one nine times. And C of ninety eight and C of a hundred are the same exact fraction, ten thousand over three ninety seven. The hundredth machine gave back exactly what the ninety ninth bought.

@words text="√9800 = 98.9949  (rounded)"
The closed form, the square root of nine thousand eight hundred, is ninety eight point nine nine four nine. It agrees, but a machine count is a count, so the integer test is the claim and the root is a rounded gloss.

@chapter The descent, in money
@art descending-curve
Past the peak, the curve comes down. At a hundred and ninety eight machines, twice the bill, capacity is twenty two point three nine seven times, eighty eight point nine percent of the peak. At two hundred and sixty, it's twenty point one three three.

@art remove-to-test
The danger is that this looks like a capacity shortage. Throughput is low, so the fleet grows, and throughput falls further. The only test that tells them apart is the one nobody wants to run. Remove machines, and see whether throughput rises.

@words text="β is the protocol, not the hardware"
And beta comes from the protocol. A distributed lock, a write that waits for every copy, a gossip mesh. Faster machines move the curve up, not the peak. Removing the need for agreement moves the peak.

@chapter Where people slip
@list heading="Common slips" items="Reading the peak as a plateau@The first|Rounding the closed form and calling it the answer@The second|Treating β as a property of the hardware@the third"
The first slip is reading the peak as a plateau, when the machines past it are harmful. The second is rounding the closed form and calling it the answer. And the third is treating beta as a property of the hardware.

@chapter Try it
@words text="α = 1/50,  β = 1/2500" sub="first move: the target (1 − α)/β"
Your turn. Keep alpha at one fiftieth, and set beta to one in two thousand five hundred. Compute the target, find the peak by testing two neighbouring products, and evaluate capacity there. Predict first whether the peak is higher or lower than twenty five point one nine.

@end text="Compare the neighbours"
You can move alpha and beta and watch the curve peak and fall, on Learn. That's learn dot get er done dot I O.
