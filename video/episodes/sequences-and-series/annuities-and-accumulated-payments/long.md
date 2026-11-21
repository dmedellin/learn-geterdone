---
format: long
lesson: sequences-and-series/annuities-and-accumulated-payments
title: Annuities: regular payments are a geometric series
thumb: Every payment has its own clock
---

@chapter Equal payments
@title text="Annuities and Accumulated Payments" sub="Sequences and Series" art=thumb
Put the same amount into savings every year. What's it worth at the end? Each payment earns interest for a different length of time, and together they make a geometric series.

@art timeline-payments
An annuity is a sequence of equal payments at equal intervals. In an ordinary annuity, each payment falls at the end of its period. The rate per period, i, is written as a fraction, so ten percent is i equals one tenth.

@chapter Five payments, one by one
@math heading="P = 1000,   i = 1/10,   n = 5" items="payment 1:   1000(11/10)⁴ = 1464.10@the first payment;;payment 2:   1000(11/10)³ = 1331.00@thirteen thirty one;;payment 3:   1000(11/10)² = 1210.00@twelve ten;;payment 4:   1000(11/10) = 1100.00@eleven hundred;;payment 5:   1000@the last"
Take five payments of a thousand, at the end of each year, at ten percent. The first payment then sits for four more years, growing to fourteen sixty four point one. The next grows to thirteen thirty one, then twelve ten, then eleven hundred. And the last arrives as the account closes, and earns nothing.

@art growing-stacks
Read that list from the bottom up: a thousand, eleven hundred, twelve ten, thirteen thirty one. That's geometric, with first term P and ratio one plus i. Reading backwards is the whole trick.

@chapter The formula
@math heading="Accumulated value" items="S = P[(1 + i)ⁿ − 1] / i@S equals;;= 1000[(11/10)⁵ − 1] / (1/10)@a thousand times;;= 6105.10@six thousand one hundred and five"
So the geometric sum formula applies, with one minus r equal to minus i. Flip both signs, and S equals P times one plus i to the n, minus one, over i. Here, that's a thousand times eleven tenths to the fifth, minus one, over one tenth: six thousand one hundred and five point one.

@words text="n = 1  →  S = P          S ≥ nP = 5000" sub="two free checks"
Two checks are free. With one payment, the formula gives P. And at a positive rate, the total can't be below the payments themselves, five thousand here. The extra eleven hundred and five point one is interest.

@words text="r = 1 + i  >  1" sub="fine: a finite sum only needs r ≠ 1"
Notice the ratio is bigger than one. That's allowed. The condition that r is less than one belongs to infinite sums. A finite sum only needs r not to equal one.

@chapter Valued today
@art discount-back
The other question is what the payments are worth now. A payment of P in k periods is worth P over one plus i to the k today, because that amount, left to grow, becomes P. Those also form a geometric series, with ratio one over one plus i.

@math heading="Present value" items="A = P[1 − (1 + i)⁻ⁿ] / i@present value A;;100/(5/4) + 100/(5/4)² = 80 + 64 = 144@eighty plus sixty four;;100[1 − (4/5)²] / (1/4) = 144@the formula"
The present value A is P times one minus one plus i to the minus n, over i. Two payments of a hundred at twenty five percent are worth eighty plus sixty four today: a hundred and forty four. The formula gives the same.

@chapter Payments for ever
@art perpetuity-row
A perpetuity pays P at the end of every period, for ever. Now it's an infinite series, and the ratio, one over one plus i, is less than one whenever i is positive. So the sum exists, and it's P over i.

@math heading="1000 a year for ever, at 10%" items="A = 1000/(1/10) = 10000@ten thousand;;first 10 payments  ≈ 6144.57@ten payments;;first 50  ≈ 9914.81@fifty;;the 50th alone  ≈ 8.52@the fiftieth"
A thousand a year for ever, at ten percent, is worth ten thousand. The first ten payments are worth about six thousand one hundred and forty four today. The first fifty, about nine thousand nine hundred and fifteen. The fiftieth alone is about eight point five two. Later payments count for less and less.

@chapter Common slips
@art shifted-clock
The classic slip is giving the last payment a period of interest. That multiplies everything by one plus i, and turns six thousand one hundred and five point one into six thousand seven hundred and fifteen point six one. That's the answer for payments at the start of each year, which is why it survives a glance.

@art unit-mismatch
The rate must be the rate per payment period. Three hundred monthly payments of a hundred at one two hundredth a month grow to about sixty nine thousand three hundred. Use the annual six percent with that monthly count, and you get roughly sixty five billion.

@words text="round once, at the end" sub="360 half-cents = 1.80"
And keep the fractions. Round each of three hundred and sixty terms to the cent, and you can be out by one point eight.

@chapter Try it
@words text="3 payments of 200,  25% a year" sub="first term 200/(5/4),  ratio 4/5"
Your turn. Value three end of year payments of two hundred today, at twenty five percent a year. The first term is two hundred over five quarters, and the ratio is four fifths. Add the three directly, then use the formula, and check you're below six hundred.

@end text="Payments, and what they grow to"
You can set a payment, a rate and a term, and watch each payment grow, on Learn. That's learn dot get er done dot I O.
