---
format: long
lesson: ddd-model-integrity/unifying-an-elephant
title: Unifying an Elephant: partial models, and choosing a strategy
thumb: A wall, a snake, a tree
---

@chapter The blind men
@title text="Unifying an Elephant" sub="Domain-Driven Design, Chapter 14" art=thumb
Evans opens with Saxe's poem, The Blind Men and the Elephant. Six blind men each touch one part of an elephant, and declare it a wall, a snake, a tree, a rope.

@art agree-on-location
His reading is generous to them. If they need no integration, it doesn't matter that their models disagree. If they need some, they gain most simply by recognising that they disagree, and stop talking at cross purposes. With separate contexts, they can agree on the one thing they all care about, perhaps where the elephant is.

@chapter Unifying means a new model
@quote text="Unifying multiple models almost always means creating a new model." cite="Evans, Domain-Driven Design, Chapter 14"
As they need to share more, one context is worth more, and harder to reach. None will give up his model, since the man holding the tail knows it's no tree. Unifying multiple models almost always means creating a new model.

@art crude-elephant
The first stage is part and whole. Relate the pieces, and you get a crude elephant: a wall on four trees, with a snake and a rope at the ends. Incoherent, but it may serve. Then a new requirement, the elephant walking, say, forces a deeper model, an animal with its parts in clear relationships.

@art snake-or-hose
The harder case is two people describing the same part differently, a snake against a fire hose. Neither model survives, and a new abstraction has to keep what's apt in each. Unification depends on minimalism. Lacking a feature is better than carrying a wrong one.

@chapter Choosing a strategy
@list heading="The forces" items="Larger: smoother flow, one model, one language@Larger contexts|Smaller: less overhead, easier integration, own jargon@Smaller ones"
Choosing a strategy starts from the current map. Evans lists the forces. Larger contexts give smoother flow between user tasks, one coherent model instead of two and a mapping, and a shared language. Smaller ones mean less communication overhead, easier Continuous Integration, and room for specialised jargons.

@art team-sizes
Toward external systems, consider Separate Ways first, then Conformist or an Anticorruption Layer. Inside, one context may do for a team of fewer than ten on closely related work. A larger team can break off parts, each under ten, joined by a kernel or as customer and supplier. Generally, one team to a context.

@words text="Map what is, then change in small pieces"
On a project already under way, first map the contexts as they really are. Tighten integration inside them, gather stray translation into the layers, name the contexts, and only then change boundaries, in small pieces. The trade is independence against smoother communication, and politics often decides.

@chapter Four views of a bike
@code block=1 lines=1-16 focus="1-4@workshop|5-8@van crews|9-12@billing|13-16@rider app"
Now the count. Four contexts at a bike share: the maintenance workshop, the van crews who rebalance bikes between stations, billing, and the rider app. Each has its own model of a bike.

@math heading="four-views" items="7 terms · 4 shared@seven terms;;false cognates: bike (4 meanings), trip (3), fault (2)@three are false cognates;;safe: station@station;;duplicates: trip = ride, fill = dock-count@two duplicate concepts"
The lab counts seven terms, four shared. Three are false cognates: bike, with four meanings, trip, with three, and fault, with two. One is safe to share, station. And there are two duplicate concepts: the paid ride, and the count of docked bikes.

@art bike-four-ways
This is the elephant. To the workshop, a bike is an asset to service. To the van crews, a unit to move. To billing, a class with a price. To the app, a pin on a map. None is wrong. And station is the elephant's location. If all they need is to agree where bikes are, translating that one concept is enough.

@art deeper-bicycle
Unifying would mean a new concept, bicycle, that every context uses alike. Each partial view is kept as a term of its own, test ride, van run, price band, and the duplicates get one name each.

@words text="9 terms · 4 shared · 0 false cognates · 0 duplicates"
The lab counts nine terms, four shared, all safe to share, no false cognates and no duplicates. No team's old bike survived. Whether they need it is the strategy question.

@chapter Where people slip
@list heading="Common slips" items="Letting one team's model win@The first|Every jargon its own context@The second|Planning on a deep model@And the third"
The first slip is thinking unification means one team's model wins. The second is treating every specialised jargon as worth a context of its own. And the third is planning on a deep model to resolve the conflicts. It comes late, if at all, and can't be scheduled.

@chapter Try it
@code block=2 lines=1-11 focus="1-3@shop|4-6@kitchen|7-9@delivery|10-11@accounts"
Your turn. A bakery's shop, kitchen, delivery round and accounts, four partial models of an order. Find the shared terms, the false cognates and the duplicate concepts, and say which term, if any, is safe to share. Then name the one concept a minimal integration would translate.

@end text="Know where you disagree"
Check your count in the lab, on Learn. That's learn dot get er done dot I O.
