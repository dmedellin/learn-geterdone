---
format: long
lesson: first-order-linear-equations/circuits-tanks-and-loans
title: Circuits, tanks and loans: one equation, three stories
thumb: Why 100 over 6 is wrong
---

@chapter The question
@title text="Circuits, Tanks and Loans" sub="First-Order Linear Equations" art=thumb
A charging capacitor, a salt tank, and a loan being paid down look like three different problems. They're one equation with different letters. And the loan hides a surprise about how long it takes to pay off.

@art skeleton
All three have the same skeleton. An unknown quantity, a constant source, and a loss or gain proportional to the unknown. Write the rate as what comes in minus what goes out, collect the unknown on the left, and you have y prime plus a y equals b.

@list heading="Three situations" items="capacitor:   a = 2,   b = 5,   steady 5/2@capacitor|tank:   a = 1/20,   b = 10,   steady 200@tank|loan:   a = −1/20,   b = −6,   steady 120@loan"
For the capacitor, a is two, b is five, and the steady state is five halves. For the tank, a is one twentieth, b is ten, and the steady state is two hundred. For the loan, a is minus one twentieth, b is minus six, and the steady state is a hundred twenty.

@chapter The capacitor
@math heading="R·q′ + q/C = V" items="R = 1,  C = 1/2,  V = 5@capacitance;;q′ + 2q = 5@dividing by R;;steady state C·V = 5/2@five halves"
A capacitor with capacitance C charges through a resistor R from a source of voltage V. The charge obeys R q prime plus q over C equals V. With R equals one, C equals a half and V equals five, dividing by R gives q prime plus two q equals five. The steady state is C times V, five halves.

@art capacitor
That's the charge at which the capacitor's voltage equals the source's. From empty, the charge approaches five halves, and is below it at every finite time.

@chapter The tank
@art tank
A tank holds twenty litres of brine. Brine at ten units per litre flows in at one litre a minute, and the mix flows out at the same rate. The salt gains ten a minute and loses y over twenty, since a twentieth of the tank leaves each minute. So y prime plus y over twenty equals ten, with steady state two hundred.

@chapter The loan
@math heading="Balance 100,  5% interest,  pay 6 a year" items="B′ = B/20 − 6@gains;;B′ − B/20 = −6@Moving;;a = −1/20,   b = −6,   steady 120@a hundred twenty"
A balance of a hundred earns five percent a year, charged continuously, and is repaid at six a year. It gains B over twenty and loses six, so B prime equals B over twenty minus six. Moving the B term to the left changes its sign. So a is minus one twentieth, b is minus six, and the steady state is a hundred twenty.

@art knife-edge
At a hundred twenty, the interest is exactly six a year, the payment, so the balance neither falls nor grows. But a is negative, so it repels. It's a knife edge, not a destination. The loan starts at a hundred, below it, so the gap is minus twenty, and grows.

@math heading="When is it paid off?" items="B = 120 − 20·e^(t/20)@a hundred twenty minus;;e^(t/20) = 6@set B to zero;;t = 20·ln 6 ≈ 35.8352 years@twenty ln six"
So B is a hundred twenty minus twenty e to the t over twenty. Set B to zero, and e to the t over twenty equals six. So t is twenty ln six, about thirty five point eight years, rounded.

@chapter Why 100 over 6 is wrong
@words text="100/6 ≈ 16.6667 years" sub="at year 17: ≈ 73.2071 still owed"
The naive estimate is a hundred over six, about sixteen point seven years, if no interest were charged. But at year seventeen, the closed form still gives about seventy three point two owed. The real payoff is more than twice as long, because the balance earns interest all the way down.

@art balance-down
In the lab's Euler view with a step of one year and at least thirty six steps, the rounded closed form column falls through zero between year thirty five and year thirty six.

@math heading="Start at 130 instead" items="gap +10@plus ten;;B = 120 + 10·e^(t/20)@grows without limit"
Start the same loan at a hundred thirty. The gap to a hundred twenty is plus ten, so B is a hundred twenty plus ten e to the t over twenty, and the balance grows without limit. The interest on a hundred thirty is six and a half, and the payment is only six.

@chapter Where people slip
@list heading="Common slips" items="Taking 100/6 as the payoff time@The first|Reading 120 as where the balance ends@The second|Moving the interest without its sign@The third"
The first slip is taking a hundred over six as the payoff time. The second is reading the loan's steady state as where the balance ends up. It repels. The third is moving the interest term without changing its sign. That gives a steady state of minus a hundred twenty, attracting, and a payoff at about twelve point one years.

@art impossible-payoff
That's sooner than even the no interest estimate. Interest can't clear a loan faster than paying with no interest at all, and that impossibility is the sign a term crossed over unchanged.

@chapter Try it
@words text="B′ = B/20 − 6,  B(0) = 100" sub="find B at t = 20"
Your turn. Using B equals a hundred twenty minus twenty e to the t over twenty, work out the balance after twenty years, and say whether it's closer to the naive picture or the real payoff.

@end text="Find the steady state, then its sign"
You can run the capacitor, the tank and the loan side by side, on Learn. That's learn dot get er done dot I O.
