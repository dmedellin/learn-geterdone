---
format: long
lesson: exponential-and-logarithmic-functions/growth-and-decay
title: Growth and decay: the percentage is the base in disguise
thumb: The base tells the whole story
---

@chapter One formula, two stories
@title text="Growth and Decay" sub="Exponential and Logarithmic Functions" art=thumb
The same formula, a times b to the x, describes an amount that keeps multiplying up and one that keeps shrinking. Which one you've got is decided entirely by the base. And the percentage in a word problem is that base in disguise.

@art growth-decay-pair
With a positive starting value a, the base b is called the growth factor. If b is bigger than one, the function increases, and that's growth. If b is between zero and one, it decreases, and that's decay. And b equals one gives the constant a, which is neither.

@chapter A percentage is a multiplier
@words text="f(x + 1) − f(x) = (b − 1)·f(x)"
One step multiplies by b, so the change across a step is b minus one, times the current value. That's the same fraction of the current value at every step. Write the fraction as a percentage, and you have the rate.

@math heading="Percent → base" items="up 5%:   b = 1 + 5/100 = 21/20@up five percent;;up 100%:   b = 2@up a hundred percent;;down 20%:   b = 1 − 20/100 = 4/5@down twenty percent;;down 10%:   b = 9/10@down ten percent"
So up five percent means b equals one plus five hundredths, which is twenty one twentieths. Up a hundred percent is b equals two, doubling each step. Down twenty percent is one minus twenty hundredths, four fifths. And down ten percent is nine tenths.

@art percent-multiplier
The one matters. It's the amount you keep, and the percentage is what's added or taken away. Keep the base as a fraction, too. Twenty one twentieths raised to a power is exact. One point oh five on a machine is not, and after ten steps the difference shows in the fourth or fifth decimal place.

@chapter A worked decay
@math heading="500 g, down 20% a year" items="A(n) = 500·(4/5)ⁿ@The model;;n = 1:   400      lost 100@After one year;;n = 2:   320      lost 80@after two;;n = 5:   163.84      lost 40.96@after five"
Take five hundred grams losing twenty percent a year. The model is five hundred times four fifths to the n. After one year, four hundred, so a hundred grams lost. Then three hundred and twenty after two, with eighty lost. And after five, one hundred sixty three point eight four, with forty point nine six lost that year.

@art shrinking-losses
The percentage lost is twenty every single year. The amount lost keeps falling, because twenty percent of a smaller number is a smaller number. A model that says loses a hundred grams a year gets year one right, and is at zero after five years, which is badly wrong.

@chapter Doubling time and half-life
@words text="doubling:  bⁿ = 2      half-life:  bⁿ = 1/2"
The doubling time is the number of steps n with b to the n equal to two. The half-life is the n with b to the n equal to one half. Both depend on b alone.

@art doubling-steps
Moving n steps multiplies by b to the n, wherever you start. So a quantity takes exactly as long to go from a thousand to two thousand as from one to two. The doubling time belongs to the base, not to the starting point.

@math heading="b = 101/100   (up 1%)" items="(101/100)⁶⁹ ≈ 1.9869@sixty nine;;(101/100)⁷⁰ ≈ 2.0068@and seventy;;exact  n ≈ 69.6607@The exact answer"
At one percent, the powers step across two between sixty nine, at about one point nine eight six nine, and seventy, at about two point zero zero six eight. The exact answer is irrational, near sixty nine point six six zero seven. Finding it needs a logarithm.

@math heading="Rule of 70:   about 70 / r" items="1%:   70   vs   69.6607@At one percent;;5%:   14   vs   14.2067@at five;;10%:   7   vs   7.2725@at ten"
There's a shortcut. For a rise of r percent a step, the doubling time is close to seventy over r. At one percent that's seventy, against a true sixty nine point six six. At five, fourteen against fourteen point two one. And at ten, seven against seven point two seven. For now it's a checked shortcut, not a derived rule.

@chapter Decay is growth reflected
@art mirror-curves
One over b, to the x, is the same as b to the minus x. So the decay curve with base one over b is the growth curve with base b, reflected in the vertical axis. One shape, seen twice.

@art linear-vs-decay
It also means decay never reaches zero. Something losing ten grams a year from a hundred grams is empty in ten years. Something losing ten percent a year never is.

@chapter Where people slip
@list heading="Common slips" items="Taking the percentage of the original@The first|Using the rate as the base@The second|Mixing the units of base and exponent@The third"
The first is taking the percentage of the original each time. Down twenty percent twice from five hundred is three hundred and twenty, not three hundred. The second is using the rate as the base: a five percent rise is one point oh five, not point oh five. The third is mixing units. Going monthly isn't five percent divided by twelve.

@chapter Try it
@words text="240 units, up 12% an hour" sub="b = 1 + 12/100 = 28/25"
Your turn. Take two hundred and forty units growing twelve percent an hour. The base is given: one plus twelve hundredths, twenty eight twenty fifths. Write the function with its time unit, find the amount after two hours without rounding the base, and explain why the second hour's gain differs from the first.

@end text="Watch the percentage stay put"
You can change the base and watch the percentage stay put while the amount moves, on Learn. That's learn dot get er done dot I O.
