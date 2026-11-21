---
format: long
lesson: sets-relations-functions/the-pigeonhole-principle
title: The pigeonhole principle: obvious, and surprisingly powerful
thumb: The art is choosing the boxes
---

@chapter The question
@title text="The Pigeonhole Principle" sub="Sets, Relations and Functions" art=thumb
Put five letters into four mailboxes, and some mailbox gets two. That's so obvious it hardly sounds like mathematics. And yet it proves things that are not obvious at all.

@art dots-in-boxes
Here's the principle. If n objects go into k boxes, and n is bigger than k, then some box holds at least two. The proof is one line. If every box held at most one, there'd be at most k objects, and there are more than k.

@words text="no injection A → B when |A| > |B|"
It's the previous lessons restated. Objects are the domain, boxes are the codomain, and a collision is two objects sharing a box. There's no injection from a larger finite set into a smaller one.

@chapter The generalised version
@art crowded-box
There's a sharper form. With n objects in k boxes, some box holds at least n over k, rounded up.

@math items="⌈20/6⌉ = ⌈3.33…⌉ = 4@twenty objects"
With twenty objects in six boxes, twenty over six is three point three three, so some box holds at least four. Round up, not down. The guarantee is four, not three.

@chapter Certainty, not chance
@art calendar
Among three hundred and sixty seven people, two share a birthday. The boxes are the three hundred and sixty six possible dates, and you need no assumption about how birthdays are spread. This isn't likely. It's certain, and it's a different claim from the birthday problem in probability.

@art remainder-wheel
Another. Among any n plus one integers, two leave the same remainder on division by n, because there are only n possible remainders. So their difference is divisible by n. A fact about divisibility, obtained by counting.

@words text="s₁, s₂, …, sₙ  mod n" sub="some consecutive block is divisible by n"
The same trick goes further. Take any n integers, and their n running totals. If some total leaves remainder zero, you're done. Otherwise n totals share the n minus one other remainders, so two match, and the block of numbers between them adds to a multiple of n.

@chapter The friends argument
@art friend-network
Now one worth studying. In any group of at least two people, two have the same number of friends in the group. Counts run from zero up to n minus one. That's n boxes for n people, which isn't enough.

@words text="0 and n − 1 can't both occur"
But zero and n minus one can't both happen. If someone knows nobody, nobody can know everybody. So only n minus one boxes are really available, and the principle applies. Spotting that two boxes exclude each other is what made it work.

@chapter Five points in a square
@art square-quarters
Show that among any five points in a unit square, two are within root two over two of each other. The boxes: cut the square into four quarters, each a half by a half. Five points, four quarters, so some quarter holds two points.

@math items="√(½² + ½²) = √(1/2) = √2 / 2 ≈ 0.707@the diagonal"
Two points in a small square are at most its diagonal apart. The diagonal is the square root of a half squared plus a half squared, which is root two over two, about zero point seven zero seven.

@words text="The boxes are the proof"
The choice of four quarters is the entire proof. Nine boxes would prove nothing for five points, and two halves would give a weaker bound. The principle never tells you what the boxes are. Choosing them is the skill.

@chapter Where people slip
@list heading="Common slips" items="Boxes that outnumber the objects@The first|Rounding the bound down@The second|Reading it as probability@the third"
The first slip is choosing boxes that outnumber the objects. You need strictly more objects than boxes, and a finer classification isn't a better one. The second is rounding the generalised bound down. And the third is reading the conclusion as probability. Pigeonhole gives certainty.

@chapter Try it
@words text="10 distinct integers from 1 to 100" sub="two subsets with the same sum"
Your turn. Prove that among any ten distinct integers between one and one hundred, two different subsets have the same sum. The objects are the subsets. The boxes are the possible sums. Count both, and the argument writes itself.

@end text="The principle, as a constraint on arrows"
You can watch the principle as a constraint on arrows, where no arrangement can avoid a collision, on Learn. That's learn dot get er done dot I O.
