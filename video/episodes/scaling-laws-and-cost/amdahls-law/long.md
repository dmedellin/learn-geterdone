---
format: long
lesson: scaling-laws-and-cost/amdahls-law
title: Amdahl's law: five percent serial caps you at twenty times
thumb: The ceiling is 1/(1 − p)
---

@chapter The part you can't share
@title text="Amdahl's Law" sub="Scaling Laws and Cost" art=thumb
Double the machines, halve the runtime. That's the plan, and here's why it breaks. Some of every job can't be shared out, and that part decides how fast the whole thing can ever go.

@art split-job
Split a job's runtime on one machine into two parts. A fraction p can be spread across machines. The rest, one minus p, is serial. It can't.

@art shrinking-parallel
Add machines, and the parallel part shrinks to p over n. The serial part stays exactly as it was. It's not a percentage that shrinks with the rest. It's a fixed stretch of wall clock time, and with enough machines, it's nearly the whole runtime.

@math heading="Speedup on n machines" items="time = (1 − p) + p/n@one minus p plus p over n;;S(n) = 1 / ((1 − p) + p/n)@the speedup"
So the time on n machines is one minus p, plus p over n, of the original. And the speedup is one over that. The model assumes perfect division, identical machines and free coordination. All three are generous, so this curve is an upper bound.

@chapter The ceiling
@math heading="As n grows" items="p/n → 0@p over n goes to zero;;S(n) → 1/(1 − p)@one over one minus p;;p = 19/20:  ceiling 20×@twenty times"
As n grows, p over n goes to zero, so the speedup climbs toward one over one minus p, and never reaches it. Five percent serial, p of nineteen twentieths, gives a ceiling of twenty times. No machine count changes that number.

@art ceiling-curve
Two machines give one point nine oh five times. Four, three point four seven eight. Eight, five point nine two six. Each doubling adds less than the last. And the number they're heading for, you can write down before you buy a single machine.

@chapter Thirty two machines
@math heading="p = 19/20,  n = 32" items="(1/20) + (19/20)/32 = 32/640 + 19/640 = 51/640@fifty one over six hundred and forty;;S(32) = 640/51 = 12.549×@twelve point five four nine;;62.75% of the ceiling@sixty two point seven five"
At thirty two machines: one twentieth, plus nineteen twentieths over thirty two, is fifty one over six hundred and forty. So the speedup is six forty over fifty one, twelve point five four nine times. That's sixty two point seven five percent of the ceiling.

@art straight-vs-curve
A team that measured the first few rows and drew a straight line through them would expect thirty two times. That overstates the real figure by two point five five.

@chapter Efficiency
@art idle-machines
Divide the speedup by n and you get efficiency, the share of each machine you're actually using. At thirty two machines, it's twenty over fifty one, thirty nine point two two percent. Three fifths of the fleet is waiting on the serial part, and every machine is paid for in full.

@chapter Ninety percent of the ceiling
@math heading="Want S(n) ≥ f · 1/(1 − p)" items="n ≥ (f/(1 − f)) · (p/(1 − p))@n is at least;;f = 9/10:  9 × 19 = 171 machines@a hundred and seventy one;;S(171) = 3420/190 = 18 = 0.9 × 20  ✓@exactly eighteen"
Since you never reach the ceiling, ask how many machines get you a share f of the way. One cross multiplication gives n is at least f over one minus f, times p over one minus p. For ninety percent, that's nine times nineteen, a hundred and seventy one. Substitute back and you get exactly eighteen, nine tenths of twenty.

@art odds-times-ratio
Read the two factors. The first is the odds of the target, nine for ninety percent, ninety nine for ninety nine. The second is parallel work over serial work. Tighten the target from ninety to ninety nine percent, and you need eleven times the machines. And at a hundred and seventy one machines, efficiency is just ten and a half percent.

@chapter Where people slip
@list heading="Common slips" items="Reading the ceiling off the largest n you tried@The first|Treating p as a share of the code@The second|Quoting a speedup without its efficiency@the third"
The first slip is reading the ceiling off the largest n you tried. The second is treating p as a share of the code. It's a share of runtime. A lock held for five percent of the wall clock is a twenty times ceiling, even if it's two lines. And the third is quoting a speedup without its efficiency.

@chapter Try it
@words text="p = 4/5" sub="ceiling, S(8), S(64), and n for 90%"
Your turn. Take p as four fifths. Write down the ceiling, then the speedup at eight and at sixty four machines as fractions, the efficiency at each, and the machine count for ninety percent. Predict first which speedup is nearer half the ceiling.

@end text="Invert the serial fraction first"
You can move the parallel fraction and the machine count and watch the ceiling, on Learn. That's learn dot get er done dot I O.
