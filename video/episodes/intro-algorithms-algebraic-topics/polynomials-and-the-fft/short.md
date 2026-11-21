---
format: short
lesson: intro-algorithms-algebraic-topics/polynomials-and-the-fft
title: Multiply polynomials without multiplying coefficients
---

@art point-values
Multiplying polynomials is slow. Multiplying their values is fast.

@words text="Θ(n²) → Θ(n)" sub="if you know the values at the same points"
Store each polynomial by its values at enough points, and the product is just the values multiplied, point by point.

@art unit-circle
The trick is getting there and back. At the complex roots of unity, the FFT evaluates and interpolates in n log n time.

@end text="Full lesson on Learn"
Count the butterflies in the full lesson on Learn.
