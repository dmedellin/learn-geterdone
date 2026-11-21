---
format: long
lesson: markov-chains-decisions-and-queues/finite-buffers-blocking-and-the-admitted-rate
title: Finite buffers, blocking, and the rate that actually gets in
thumb: Divide by who got in
---

@chapter A queue with a wall
@title text="Finite Buffers, Blocking and the Admitted Rate" sub="Markov Chains, Decisions and Queues" art=thumb
Real queues often have a limit. A waiting room with a few chairs, a buffer with K slots. When it's full, the next arrival is turned away. That changes two things you might think you know.

@art buffer-wall
Stop the chain at state K, with no arrival out of the top. An arrival finding it full is lost. Now the truncation isn't an approximation. It's the model, and it comes with no error term.

@words text="ρ ≥ 1 is fine"
First change: stability stops being a question. A queue that can't grow can't run away. So even with arrivals faster than service, the chain has a perfectly good distribution.

@chapter Overloaded and fine
@words text="λ = 6 · μ = 5 · K = 5" sub="ρ = 6/5"
The lesson's example: arrivals at six, service at five, room for five. Rho is six fifths, which would sink an unbounded queue. Here, nothing about rho needs checking before you trust the numbers.

@art rising-pi
Every cut ratio is six fifths, so the distribution rises toward the top. The system is usually nearly full. The blocking probability, pi five, is seven seven seven six over thirty one thousand and thirty one, about twenty five point oh six percent.

@words text="Closed form: 7776/31031 exactly"
The closed form for this finite queue gives exactly the same fraction. Here both describe the same finite system, so it's an exact equality, a stronger check than any unbounded model could offer.

@chapter The admitted rate
@art admitted-split
Second change. The rate that actually gets in isn't lambda. It's lambda times one minus the blocking probability. Here that's about four point four nine six, out of six. A quarter of the arrivals never enter, and any figure divided by six is quietly counting them.

@math heading="Little's law, two ways" items="L = 93750/31031 ≈ 3.021172@L is;;W = L / admitted ≈ 0.671899@divide by the admitted;;L / λ ≈ 0.503529  ✗@divide by lambda"
L is about three point oh two. Divide by the admitted rate, and the time in the system is about point six seven two. Divide by lambda instead, and you get about point five oh four. That's too small, by exactly one minus pi K.

@art two-divisions
The wrong one credits the system with serving customers it never let in. And the error always runs the same way, worst where blocking is highest, exactly where the answer matters most.

@chapter Buying room
@math heading="λ = 6, μ = 5" items="K = 1:  blocking 54.545%,  W 0.20000@room for one;;K = 5:  25.059%,  0.67190@At five;;K = 8:  20.673%,  1.08488@At eight"
With room for one, blocking is fifty four point five percent, and the wrong division is out by more than double. At five, blocking is about twenty five percent. At eight, about twenty point seven, and W has climbed past one.

@art room-trade
So more room buys throughput and costs waiting, in the same breath. The customers who used to be turned away are now waiting instead. Which you want is a question about the system, but the model gives you both columns exactly.

@chapter Customers who balk
@art balking-bars
Now let arrivals balk. Someone who finds n waiting joins with probability one over n plus one. The rates depend on the state, so the blocking queue's closed form doesn't apply. The cut equations need no change at all.

@words text="Balking: blocking 0.6255% · L = 1.192494" sub="vs 25.0588% and 3.021172"
The distribution now falls steeply. Blocking drops to about point six percent, and L is about one point one nine, against three point oh two. The model the textbooks have no formula for cost exactly as much work as the others.

@chapter Where people slip
@list heading="Common slips" items="Dividing L by λ on a lossy system@The first|Demanding ρ < 1 with a wall@The second|Reaching for a closed form when rates vary@And the third"
The first slip is dividing L by lambda on a lossy system. The second is carrying the stability condition into a bounded model, which rejects exactly the systems a buffer exists for. And the third is reaching for a closed form when the rates vary.

@chapter Try it
@words text="λ = 6 · μ = 5 · K = 2"
Your turn. With room for two, find the weights, the blocking probability, the admitted rate and W. You should get blocking of about thirty nine point five six percent, and W of about point three oh nine.

@end text="Divide by the rate that gets in"
You can change the buffer size and watch blocking, throughput and waiting move together, on Learn. That's learn dot get er done dot I O.
