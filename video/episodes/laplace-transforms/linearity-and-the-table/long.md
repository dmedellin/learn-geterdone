---
format: long
lesson: laplace-transforms/linearity-and-the-table
title: Laplace transforms by table: linearity and five families
thumb: Sums apart, constants out
---

@chapter The question
@title text="Linearity and the Table" sub="Laplace Transforms" art=thumb
Computing every transform from the integral would be slow. You don't have to. Two facts do almost all the work: the transform is linear, and a short table covers every signal this course uses.

@chapter Linearity
@math heading="Linearity" items="ℒ[c·f + d·g] = c·ℒ[f] + d·ℒ[g]@the transform of c f"
Here's the first fact. The transform of c f plus d g is c times the transform of f, plus d times the transform of g, wherever both exist.

@art sum-apart
Why? The transform is an integral. The integral of a sum is the sum of the integrals, and a constant factor comes outside. So you can split a signal into terms, transform each one, and put them back together.

@chapter The table
@art five-families
Now the table. It has just five families of signals, and together they cover every signal the rest of the course uses.

@list heading="Five families" items="ℒ[tⁿ] = n!/s^(n+1)@powers|ℒ[e^(at)] = 1/(s − a)@exponentials|ℒ[cos(bt)] = s/(s² + b²)@cosines|ℒ[sin(bt)] = b/(s² + b²)@sines|ℒ[t·e^(at)] = 1/(s − a)²@a power times"
For powers, t to the n goes to n factorial over s to the n plus one. For exponentials, e to the a t goes to one over s minus a. For cosines, s over s squared plus b squared. For sines, b over s squared plus b squared. And a power times an exponential, t e to the a t, goes to one over s minus a, squared.

@words text="ℒ[t] = 1/s²   ℒ[t²] = 2/s³   ℒ[t³] = 6/s⁴"
That factorial matters. n factorial is n times n minus one, and so on down to one. So t goes to one over s squared, t squared to two over s cubed, and t cubed to six over s to the fourth.

@art shift-s
Look at the last entry. Put a equal to zero and it becomes one over s squared, the transform of t. Multiplying the signal by e to the a t has replaced s by s minus a. The same move turns one over s into one over s minus a. That pattern is why the table can be so short.

@chapter A worked sum
@math heading="ℒ[3t² − 2e^(−t)]" items="= 3·ℒ[t²] − 2·ℒ[e^(−t)]@By linearity;;= 3·(2/s³) − 2·(1/(s + 1))@From the table;;= 6/s³ − 2/(s + 1)@six over s cubed;;= (6s + 6 − 2s³)/(s³·(s + 1))@common denominator"
Transform three t squared minus two e to the minus t. By linearity, it's three times the transform of t squared, minus two times the transform of e to the minus t. From the table, that's three times two over s cubed, minus two times one over s plus one, since a is minus one. So you get six over s cubed minus two over s plus one. Over the common denominator s cubed times s plus one, the numerator is six s plus six minus two s cubed.

@words text="large s:  ≈ −2/s"
Here's a free check. At a large s, the six over s cubed term is tiny, and the minus two over s plus one term dominates. So the fraction should be close to minus two over s. Both forms agree.

@chapter Sines and cosines
@art no-real-zero
Sines and cosines have one new feature. Their denominator, s squared plus b squared, has no real zero. For cos of two t the transform is s over s squared plus four, and its poles are plus or minus two i. The frequency two in the signal comes back as the square root of four.

@chapter What linearity doesn't cover
@math heading="f = g = 1" items="ℒ[1·1] = ℒ[1] = 1/s@one over s;;ℒ[1]·ℒ[1] = 1/s²@one over s squared"
Linearity says nothing about products. Take f and g both equal to one. Their product is one, which transforms to one over s. But the product of the transforms is one over s squared. Different functions.

@art product-trap
The same goes for t times e to the three t. Its transform is the table entry, one over s minus three, squared. Multiplying the separate transforms gives one over s squared times s minus three, which has a pole at zero that the real transform doesn't. The only real pole is at three.

@chapter Where people slip
@list heading="Common slips" items="ℒ[f·g] = ℒ[f]·ℒ[g]@The first|Dropping the factorial@The second|Flipping the sign of a@And the third"
The first slip is that product rule, which doesn't exist. The second is dropping the factorial. Write one over s cubed for t squared, and the term three t squared gives three over s cubed instead of six. And the third is flipping the sign of a. The transform of e to the minus t is one over s plus one. One over s minus one belongs to e to the t, and moves the pole from minus one to one.

@art table-cards
A table does the work of a computation, so check an entry before you trust it.

@chapter Try it
@words text="ℒ[5·cos(2t) + t³]"
Your turn. Transform five cos two t, plus t cubed. Split it into terms, name b and n, look each one up, scale by the constants, and add. Then put it over one common denominator.

@end text="Transform a signal term by term"
You can type any signal and check your fraction against the table on Learn. That's learn dot get er done dot I O.
