---
format: long
lesson: intro-algorithms-algebraic-topics/polynomials-and-the-fft
title: The FFT: multiply polynomials by changing how you write them
thumb: Values, not coefficients
---

@chapter Multiplying polynomials
@title text="Polynomials and the FFT" sub="Introduction to Algorithms, Chapter 30" art=thumb
Chapter thirty starts with signals, then sets them aside for a cleaner problem with the same mathematics.

@quote text="The most common use for Fourier transforms, and hence the FFT, is in signal processing." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 30"
The most common use for Fourier transforms, and hence the FFT, is in signal processing. But the chapter's problem is multiplying two polynomials.

@art schoolbook-grid
Adding two polynomials of degree bound n takes theta of n time. Multiplying them the schoolbook way, every coefficient against every coefficient, takes theta of n squared.

@chapter Two representations
@art point-values
A polynomial can also be stored by its values at n distinct points. Theorem thirty point one says those values determine it uniquely. And in that form, multiplication is easy: multiply the values point by point, in linear time.

@list heading="The plan" items="evaluate at 2n points@evaluate|multiply pointwise@multiply|interpolate@interpolate"
One catch. The product has degree bound two n minus one, so each factor must be evaluated at two n points. Then the plan is evaluate, multiply pointwise, and interpolate. The question is whether evaluating and interpolating can beat quadratic time.

@chapter The roots of unity
@art unit-circle
They can, if you choose the points well. Use the complex n th roots of unity, the n powers of omega n, spaced evenly round the unit circle. Squaring them gives the n over two roots of order n over two, each twice. That's the halving lemma.

@art even-odd-split
Split A into its even and odd coefficients. Then A of x equals A even of x squared, plus x times A odd of x squared.

@math heading="The FFT's split" items="A(x) = A_e(x²) + x·A_o(x²)@By the halving lemma;;y_k = e_k + ωᵏ·o_k@y k;;y_(k+n/2) = e_k − ωᵏ·o_k@y k plus n over two;;T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)@T of n"
By the halving lemma, you need each half at only n over two points. Then y k is e k plus omega to the k times o k, and y k plus n over two is the same with a minus. T of n is two T of n over two plus linear, which is n log n.

@chapter A transform of size four
@math heading="a = (2, 0, −1, 3) · ω₄ = i" items="even (2, −1) → (1, 3)@even part;;odd (0, 3) → (3, −3)@odd part;;y₀ = 4 · y₂ = −2@y zero;;y₁ = 3 − 3i · y₃ = 3 + 3i@y one"
Take two minus x squared plus three x cubed, with omega four equal to i. The even part, two and minus one, transforms to one and three. The odd part, zero and three, to three and minus three. Combining, y zero is four and y two is minus two. Y one is three minus three i, and y three, three plus three i.

@chapter Back again, and butterflies
@words text="inverse DFT = FFT with ω⁻¹, then ÷ n" sub="Theorem 30.7"
Interpolation turns out to be the same computation. Run the FFT with omega inverse in place of omega, and divide by n. That's theta of n log n too.

@art butterfly
The two updates share one product, omega to the k times o k. Compute it once, form the sum and the difference, and that's a butterfly. A transform of size n is log n stages of n over two butterflies.

@chapter Counting in the lab
@math heading="Schoolbook vs FFT" items="cubic, n = 8: 16 mults vs 36 butterflies + 8@cubic;;sixteen, n = 32: 256 vs 240 + 32@sixteen coefficients;;five, n = 16: 25 vs 96 + 16@five coefficients"
In the lab, the cubic times one plus four x plus two x cubed pads to eight: sixteen schoolbook multiplications, against thirty six butterflies and eight pointwise products. Two polynomials of sixteen coefficients: two fifty six against two forty butterflies. And squaring five coefficients pads to sixteen, ninety six butterflies against twenty five multiplications.

@art rounding
The FFT runs in floating point, so each coefficient is rounded. With coefficients near a million, the unrounded values miss integers by about one point eight times ten to the minus four. Rounding is safe while that stays well under a half.

@chapter Where people slip
@list heading="Common slips" items="The FFT is always faster@The first|Evaluating at only n points@The second|Trusting floating point as exact@the third"
The first slip is thinking the FFT is always faster. Padding and constants matter at small sizes. The second is evaluating each factor at only n points. The product needs two n. And the third is trusting floating point output as exact.

@chapter Try it
@words text="(1 + x)²" sub="evaluate at 1, i, −1, −i · square · inverse with ω⁻¹ = −i, ÷ 4"
Your turn. Multiply one plus x by itself through the transform, by hand. Evaluate at the four fourth roots of unity, square the four values, and interpolate with omega inverse equal to minus i, dividing by four.

@end text="Count the butterflies"
You can multiply polynomials both ways and count the work, on Learn. That's learn dot get er done dot I O.
