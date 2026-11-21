---
format: long
lesson: linear-programming-models/covering-diet-and-minimisation-models
title: Diet models: an endless region with a perfectly good minimum
thumb: Endless region, finite cost
---

@chapter The question
@title text="Covering and Diet Models" sub="Linear Programming Models" art=thumb
Some models aren't about running out. They're about meeting requirements as cheaply as you can. And their regions go on forever, which looks alarming, and usually isn't.

@art feed-ration
A feed merchant blends grain and pellets into a ration. A kilogram of grain gives one gram of protein and two of fibre. A kilogram of pellets gives three grams of protein and one of fibre.

@words text="≥ 9 g protein · ≥ 8 g fibre" sub="grain 2 a kg · pellets 3 a kg"
The ration must carry at least nine grams of protein and at least eight of fibre. Grain costs two a kilogram, and pellets cost three.

@chapter The model
@math heading="The diet model" items="minimise 2G + 3P@minimise;;G + 3P ≥ 9@G plus three P;;2G + P ≥ 8@two G plus P;;G, P ≥ 0@both at least zero"
So you minimise two G plus three P. Subject to: G plus three P at least nine, for protein. Two G plus P at least eight, for fibre. And G and P both at least zero.

@words text="supply ≥ requirement"
A requirement is a row with at least, not at most. And the gap it leaves isn't slack. Nothing is left unused. It's over delivery.

@chapter Surplus
@art requirement-bar
Picture each requirement as a mark on a bar. The ration has to reach the mark, and anything past it is extra. With packing rows you measured what was left. Here you measure how far you went over, and that difference in sign starts to matter later in the course.

@math heading="Surplus" items="surplus = a·x − b@minus the requirement;;at (4, 2):  protein 10 − 9 = 1@one gram;;at (4, 2):  fibre 10 − 8 = 2@two grams"
That gap is called a surplus: the usage minus the requirement. At four of grain and two of pellets, the protein surplus is one gram and the fibre surplus is two grams. The ration over delivers both.

@chapter The cheapest ration
@math heading="Corners" items="(0, 8):  cost 24@twenty four;;(3, 2):  cost 12@twelve;;(9, 0):  cost 18@eighteen"
The corners are zero and eight, costing twenty four. Three and two, costing twelve. And nine and zero, costing eighteen.

@art corner-minimum
The cheapest is three kilograms of grain and two of pellets. That supplies exactly nine grams of protein and exactly eight of fibre. Both surpluses are zero, because exceeding a requirement would cost money and buy nothing.

@chapter The region runs forever
@art open-region
There's no boundary to the north east. Feed ten kilograms of each, and both requirements still hold. If you've been warned about unbounded problems, you might worry. But walking forever is a fact about the region. Whether the cost falls forever as you walk is a fact about the objective.

@math heading="Directions out" items="(1, 0):  +2 a step@by two;;(0, 1):  +3 a step@by three;;(1, 1):  +5 a step@by five"
Walk along one, zero and the cost rises by two a step. Along zero, one, it rises by three. Along one, one, by five. Every step out costs money, so the minimum sits at a corner.

@art ray-cone
Three directions are evidence, though, not a proof. The real rule covers every direction the region runs in. The cost runs away exactly when some such direction lowers it. That's arithmetic, not a look at the picture. So the lab prints each tested direction, and separately, a verdict over all of them.

@chapter A disposal credit
@math heading="Cost 2G − P" items="same rows, same region@same two rows;;(0, 1):  −1 a step@minus one;;no cheapest ration@no cheapest"
Now suppose the merchant is paid one a kilogram to take pellets away. The cost is two G minus P. The region hasn't changed at all, same two rows. But along zero, one the cost now changes by minus one a step. It falls forever, so there's no cheapest ration.

@art falling-ray
And the lab reports no value, rather than the last point its search stood on. An unbounded region with a non negative cost is normal. An unbounded problem needs a direction that improves the objective.

@chapter Where people slip
@list heading="Common slips" items="Unbounded region means unbounded problem@The first|A few directions as a certificate@The second|Writing a requirement as a ceiling@The third"
The first slip is concluding that an unbounded region means an unbounded problem. The second is testing a few directions and calling it a certificate. And the third is writing at most where you meant at least. The cheapest answer then is to do nothing at all, and nothing in the solve objects. Read each row aloud with its units.

@chapter Try it
@words text="Swap the pellet cost for −1" sub="find the direction that lowers it"
Your turn. Change the cost to two G minus P. Find the direction the region contains that lowers the cost, and say why there's no answer.

@end text="Test the directions yourself"
You can test directions and get the verdict over the whole cone, on Learn. That's learn dot get er done dot I O.
