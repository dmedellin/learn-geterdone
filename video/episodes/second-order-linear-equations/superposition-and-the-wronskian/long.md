---
format: long
lesson: second-order-linear-equations/superposition-and-the-wronskian
title: Superposition and the Wronskian: when two solutions are enough
thumb: Is W(0) zero?
---

@chapter The question
@title text="Superposition and the Wronskian" sub="Second-Order Linear Equations" art=thumb
You've been adding solutions with constants in front all course. Two questions are hiding in that habit. Why is a combination a solution at all? And can two solutions always fit any start?

@chapter Superposition
@art two-curves-add
Here's the first answer. If y one and y two solve a y double prime plus b y prime plus c y equals zero, then so does C one y one plus C two y two, for any constants.

@math heading="y = C₁·y₁ + C₂·y₂" items="a·y″ + b·y′ + c·y@the left side;;= C₁·(a·y₁″ + b·y₁′ + c·y₁) + C₂·(a·y₂″ + b·y₂′ + c·y₂)@splits;;= C₁·0 + C₂·0 = 0@each bracket"
The rate of a sum is the sum of the rates, and constants come out. So the left side splits into C one times y one's bracket plus C two times y two's bracket. Each bracket is zero, because each is a solution.

@words text="linear,  and zero on the right"
That proof used two things: the equation is linear, and its right side is zero. The second one matters more than it looks.

@art level-lines
Take y double prime plus y equals one. Y equals one solves it, since its second rate is zero, and zero plus one is one. But double it to two, and you get zero plus two, which is two, not one. Superposition belongs to equations whose right side is zero.

@chapter Not always enough
@art scaled-copies
Now the second question. Take e to the minus t and two e to the minus t, for y double prime plus three y prime plus two y. Both are solutions. But every combination is just a multiple of e to the minus t.

@math heading="C₁·e^(−t) + C₂·2·e^(−t)" items="y(0) = C₁ + 2·C₂@The starting value;;y′(0) = −C₁ − 2·C₂@the starting rate;;y(0) = 1,  y′(0) = 0  ✗@a start at one"
The starting value is C one plus two C two. The starting rate is minus that, always. So a start at one with rate zero would need the same quantity to be one and zero together. No fit exists.

@chapter The Wronskian
@math heading="The Wronskian" items="W(t) = y₁·y₂′ − y₁′·y₂@W of t equals;;W(0) = 1·(−2) − 2·(−1) = 0@For that pair"
One number decides this. The Wronskian, W of t, equals y one times y two prime, minus y one prime times y two. At zero, it's the determinant of the fitting equations. For that pair, it's one times minus two, minus two times minus one, which is zero.

@art spanning-arrows
If W of zero isn't zero, then for every starting value and rate, there's exactly one pair of constants. Eliminate one constant, and W of zero times C one equals a known number. The same goes for C two. Divide by W of zero, and you're done.

@art collinear-arrows
When W of zero is zero, you can't divide, and some starts can't be fitted. That's exactly what happened with e to the minus t and its double.

@chapter The presets
@math heading="W(0) for each pair" items="e^(−t), e^(−2t):  W(0) = −1@e to the minus t and e to the minus two t;;cos(2t), sin(2t):  W = 2@cosine two t and sine two t;;e^(−2t), t·e^(−2t):  W = e^(−4t),  W(0) = 1@e to the minus four t;;roots (1 ± √5)/2:  W(0) = −√5@minus root five"
E to the minus t and e to the minus two t give minus one. Cosine two t and sine two t give two, for every t. E to the minus two t and t e to the minus two t give e to the minus four t, which is one at zero. And roots one plus or minus root five over two give minus root five, exactly.

@art cos-sin-pair
For two exponentials, W of zero is the second root minus the first. A repeated root would make it zero, which is why that case needed t e to the r t. For a complex pair, W of zero is beta.

@chapter Where people slip
@list heading="Common slips" items="Any two solutions fit any start@The first|Multiplying solutions together@The second|Reading meaning into the sign@The third"
The first slip is believing any two solutions can fit any start. The second is multiplying solutions: the product of e to the minus t and e to the minus two t is e to the minus three t, and its residual is two e to the minus three t. The third is reading meaning into the sign of W. Swap y one and y two, and it flips.

@chapter Try it
@words text="y″ + 4y = 0" sub="y₁ = cos(2t),  y₂ = sin(2t)"
Your turn. Work out W of zero for cosine two t and sine two t from the definition, and check you get two. Then swap them and see the sign change.

@end text="Is the Wronskian zero?"
You can compute the Wronskian for each pair of solutions, on Learn. That's learn dot get er done dot I O.
