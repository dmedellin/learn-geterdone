---
format: long
lesson: availability-and-failure/correlated-failure
title: Correlated failure: when your second replica buys nothing
thumb: c only has to beat p²
---

@chapter The question
@title text="Correlated Failure" sub="Availability and Failure" art=thumb
Two machines, each ninety nine percent. Together, four nines. Every formula so far gave you that answer, and every one of them quietly assumed the machines fail independently. Here's what happens when they don't.

@art shared-cause
A common cause is one event that takes more than one component at once. A power feed. A rack. A network partition. An expired certificate. A configuration push. A deploy.

@chapter The model
@math heading="A pair with a common cause" items="P(both down) = c + (1 − c)p²@down together;;c = 0  →  p²  (independence)@c equals zero"
Call c the probability of such an event in the period, and p each machine's own failure probability. The pair is down together with probability c, plus one minus c times p squared. At c equals zero, that's just p squared, independence, the special case.

@words text="c is a probability" sub="never a count of machines"
And c is a probability between zero and one. It's never a count of machines, and never a count of incidents. Convert incidents to a probability per period first.

@chapter A thousandth is enough
@math heading="p = 1/100, p² = 0.0001" items="c = 0:  0.00010000  →  99.99000%@independence gives;;c = 1/10 000:  0.00019999  →  99.98000%@one in ten thousand;;c = 1/1000:  0.00109990  →  99.89001%@one in a thousand;;c = 1/100:  0.01009900  →  98.99010%@a hundredth"
With p of a hundredth, independence gives point oh oh oh one, four nines. A common cause of one in ten thousand doubles that. One in a thousand gives point oh oh one oh nine nine nine, two nines. And a hundredth drops the pair to one nine.

@art line-departs
So a common cause of one part in a thousand makes the pair eleven times worse than promised. Correlation doesn't need to be likely to dominate. It just needs to be likelier than a product of two small numbers. Here, c only has to beat p squared.

@chapter Break-even
@math heading="When is a pair no better than one?" items="c + (1 − c)p² = p@Set c plus;;c(1 − p²) = p(1 − p)@rearranging;;c(1 + p) = p@Divide;;c = p/(1 + p) = 1/101 ≈ 0.009901@one over a hundred and one"
When does a pair only match one machine? Set c plus one minus c times p squared equal to p. Rearranging gives c times one minus p squared equals p times one minus p. Divide, and c is p over one plus p. At p of a hundredth, one over a hundred and one.

@art worse-than-one
Above that value, the second machine is worse than useless. It adds cost, complexity and a failover path, and it lowers availability.

@chapter Two replicas in one rack
@math heading="Same rack, p = 1/100" items="2 power events in 36 months, 1 in 3 beats the batteries@twice in three years;;c ≈ 1/54 ≈ 0.01852  >  1/101@one in fifty four;;P(both down) = 0.018617  →  98.1383%@ninety eight point one"
Two replicas share a rack that lost power twice in three years. Say one in three of those beat the batteries, so c is about one in fifty four. That's above the break even of one in a hundred and one. The pair is ninety eight point one four percent, worse than one replica's ninety nine.

@art three-in-rack
What fixes it? Not a third replica in the same rack. That changes p squared to p cubed, and leaves c alone. Still about point oh one eight six, still worse than one machine.

@art split-racks
Moving the second replica to another rack attacks c directly. That's the whole of the improvement. Racks, power feeds, zones, deploy waves: each is an attempt to lower c.

@chapter Reporting it honestly
@words text="99.99% if independent · 99.89% if 1 in 1000 takes both"
You'll rarely know c, so bracket it. Two ninety nine percent machines give four nines if they fail independently, and ninety nine point eight nine if one event in a thousand takes both. Same arithmetic, a different and honest claim.

@art staged-deploy
The shared deploy catches teams with genuinely separate hardware. Five replicas, five racks, three zones, one bad configuration in ninety seconds. For that failure the fleet is one machine. Staged rollouts make c smaller by making the deploy not simultaneous.

@chapter Where people slip
@list heading="Common slips" items="Assuming independence silently@The first|Treating c as a count@The second|Answering correlation with another replica@The third"
The first slip is assuming independence by default, and silently. The second is treating c as a count of machines or incidents. The third is answering a correlation problem with another replica. Separating the failure domains is the move that changes the number.

@chapter Try it
@words text="different rack, same feed: c ≈ 1/500" sub="compare c with p² = 0.0001 first"
Your turn. Move the second replica to another rack on the same power feed, cutting c to about one in five hundred. Compare that with p squared first. Then work out the pair's availability, how far it still exceeds the independent promise, and the next c to attack.

@end text="Move c up from zero"
You can raise the common cause and watch the pair leave the independent line, on Learn. That's learn dot get er done dot I O.
