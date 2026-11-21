---
format: long
lesson: availability-and-failure/replica-loss-and-durability
title: Replica loss and durability: why the repair window matters so much
thumb: Halve the window, quarter the risk
---

@chapter The question
@title text="Replica Loss and Durability" sub="Availability and Failure" art=thumb
Three copies of your data. How likely are you to lose all three in a year? And which matters more, a fourth copy or a faster rebuild? The answer surprises most people.

@art three-copies
One copy failing is routine. The system notices and rebuilds it. Data is lost only when every remaining copy also fails before that rebuild finishes. All N copies, gone inside one repair window.

@chapter The first-order estimate
@math heading="Annual loss, per placement group" items="P ≈ N! × fᴺ × (R/8760)ᴺ⁻¹@the annual probability"
Say each device fails independently at rate f a year, and a lost copy is rebuilt within R hours. To first order, the annual probability of losing the item is N factorial, times f to the N, times R over eight thousand seven hundred and sixty, to the N minus one.

@art window-chain
Here's where that shape comes from. Any of the N copies can fail first. The next must fail inside the window, with probability about f times R over the hours in a year. The one after that, likewise. Count the orderings and you get the factorial.

@chapter Three copies, one day
@math heading="N = 3, f = 0.02, R = 24 h" items="R/8760 = 24/8760 = 0.00273973@twenty four over;;P ≈ 6 × 0.000008 × 0.0000075061@six times;;= 3.603 × 10⁻¹⁰ per group per year@three point six oh three"
Three copies, a two percent annual failure rate, a twenty four hour window. The window fraction is twenty four over eight seven six oh. Six times point oh oh oh oh oh eight, times that fraction squared, gives three point six oh three times ten to the minus ten per group per year.

@words text="10 000 groups: one loss every 2.776 × 10⁵ years"
Across ten thousand placement groups, that's one loss every two hundred and seventy seven thousand six hundred years or so. And this is the one rounded figure on the course. What's approximate is the model, not the arithmetic.

@chapter The window has an exponent
@math heading="Halve R" items="R = 24 h  →  3.603 × 10⁻¹⁰@twenty four hours;;R = 12 h  →  9.007 × 10⁻¹¹@twelve;;factor 2ᴺ⁻¹ = 4@a factor of"
The repair window appears N minus one times. So cut it from twenty four hours to twelve, and the risk falls from three point six oh three times ten to the minus ten to nine point oh oh seven times ten to the minus eleven. A factor of two to the N minus one, four. At four copies, eight.

@art rebuild-lever
So rebuild speed isn't an operational detail. At three copies it's as powerful as cutting the device failure rate by the same factor, twice over. And it's usually the lever an operator can actually move.

@chapter Two copies or three
@math heading="f = 0.02 · 10 000 groups" items="N = 2, R = 24 h:  2.192 × 10⁻⁶  →  one every 45.6 years@two copies;;N = 3, R = 24 h:  3.603 × 10⁻¹⁰@The third copy;;third copy: × 6083@about six thousand;;N = 3, R = 168 h:  1.765 × 10⁻⁸ = × 49@a week"
Two copies with a one day rebuild lose an item across the fleet about every forty five and a half years. The third copy is worth a factor of about six thousand. But a week long rebuild costs a factor of forty nine. Seven squared, because R appears twice.

@art exponent-stack
So three copies isn't three times the durability. Each copy multiplies the probability by two small numbers, so the improvement is exponential in N. Linear intuition is wrong by orders of magnitude.

@chapter What the number is about
@art correlated-loss
This number assumes independent devices failing at a constant rate, and rebuilds that always finish in time. Real losses come from elsewhere. Deletion bugs. A bad deploy that corrupts all three copies identically. A fleet wide operator command. None are in the model, and all are correlated. That's why backups with a different failure domain exist.

@art stalled-rebuild
And a rebuild that doesn't finish isn't a slow repair. It's an infinite R. A group with a stalled rebuild has left the formula's world entirely. Monitoring under replicated groups is the condition under which the arithmetic is true.

@chapter Where people slip
@list heading="Common slips" items="Reading durability as proportional to copies@The first|Treating the repair window as a detail@The second|Quoting the figure without its model@The third"
The first slip is reading durability as proportional to the copy count. The second is treating the repair window as an operational detail. The third is quoting the figure to eleven significant figures without the model it came from.

@chapter Try it
@words text="N = 3 · R = 24 h · f: 2% → 5%" sub="f appears 3 times: × (5/2)³"
Your turn. Keep three copies and a one day window, but the failure rate is revised from two to five percent. F appears three times, so it's five halves cubed. Find the new probability and fleet expectation, then the repair window that restores the original figure.

@end text="Halve the window, see the exponent"
You can change copies, failure rate and repair window and read the loss probability, on Learn. That's learn dot get er done dot I O.
