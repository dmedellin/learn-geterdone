---
format: long
lesson: knowledge-and-evidence/credence-and-the-dutch-book
title: Credence as a price, and the Dutch book that loses whatever happens
thumb: Lose whichever way it lands
---

@chapter Belief comes in degrees
@title text="Credence and the Dutch Book" sub="Knowledge and Evidence" art=thumb
You don't just believe or disbelieve that it'll rain. You're more or less confident. That degree of belief is called a credence. And there's a neat way to measure it: as a price.

@art bet-ticket
Picture a ticket that pays one if an event happens, and nothing if it doesn't. Your credence in the event is the price at which you'd buy that ticket, or equally sell it. If you'd pay a half for a ticket on heads, and sell one for a half, your credence in heads is a half.

@chapter Three fifths on each
@art coin-two-bets
Take a coin that lands heads or tails, and nothing else. Someone gives credence three fifths to heads, and three fifths to tails. At their own prices, they should be willing to buy a bet on heads for three fifths, and a bet on tails on the same terms.

@math heading="Buy both bets" items="price paid:  3/5 + 3/5 = 6/5@six fifths;;payout, heads:  1@If heads;;payout, tails:  1@if tails;;net either way:  1 − 6/5 = −1/5@minus one fifth"
Together, the two bets cost six fifths. If heads, one bet pays one. If tails, the other pays one. Exactly one wins either way. So the net is one minus six fifths, which is minus one fifth, whichever way the coin falls.

@art dutch-book
A set of bets with a sure loss like that is called a Dutch book. And no information about the coin could change it. The fault is in the prices, not in any belief about the world.

@chapter The rules of coherence
@list heading="Coherent credences" items="Each lies between 0 and 1@between zero and one|A certain event gets 1@certain event|Exclusive events add@cannot both happen"
A set of credences is coherent when it obeys three rules. Each credence lies between zero and one. A certain event gets one. And for two events that cannot both happen, the credence in A or B is the credence in A plus the credence in B.

@art sum-gauge
The coin example breaks the third rule in its simplest form. Heads and tails exclude each other and exhaust the outcomes, so their credences should sum to one. The size of the loss is the distance of the sum from one.

@math heading="Too low, too" items="1/3 + 1/3 = 2/3@a third and a third;;sell both for 2/3, pay out 1:  lose 1/3@sells both bets"
If the sum is below one, as with a third and a third, the book runs the other way. The person sells both bets for two thirds in total, and pays out one whichever wins, losing a third.

@math heading="The die" items="even: 1/2@Even;;one: 1/6@one;;even or one: 1/2, should be 2/3@even or one"
Here's a case with three events, on a die. Even has credence a half. One has a sixth. And even or one also has credence a half. But even and one are exclusive, so the third should be two thirds, and that gap of a sixth allows a book.

@chapter What a half means
@art die-halves
A credence of a half in heads is a statement of price. It's the credence of someone who knows the coin is fair, and the same price can come from someone who knows nothing about it. It doesn't mean no idea. You couldn't write a half for each face of a die, since six halves sum to three.

@chapter Coherent isn't reasonable
@art coherent-absurd
And the result runs one way only. If your credences break a rule, you can be exploited. If they obey the rules, there's no book, whether they're sensible or not. Ninety nine hundredths for heads on a fair coin, and one hundredth for tails, is coherent, and absurd. Coherence is necessary for rational credence, not enough.

@chapter Where people slip
@list heading="Common slips" items="Reading a half as I have no idea@The first|Thinking a book shows the credences are false@The second|Assuming coherence is enough@the third"
The first slip is reading credence a half as, I have no idea. The second is thinking a Dutch book shows the credences are false. It shows they can't all be acted on at their own prices. And the third is assuming coherence is enough. The rules never mention the world.

@chapter Try it
@words text="rain: 1/3 · no rain: 1/3" sub="Is there a book?"
Here's one to try. Someone gives a third to rain and a third to no rain. Is there a Dutch book? Say which bets to buy or sell, write the net in each outcome, and check it's the same loss either way.

@end text="Type your credences, find the book"
You can type your own credences and see the book and the loss, on Learn. That's learn dot get er done dot I O.
