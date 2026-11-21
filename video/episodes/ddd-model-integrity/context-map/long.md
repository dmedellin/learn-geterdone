---
format: long
lesson: ddd-model-integrity/context-map
title: Context Map: every model, every contact, as it is today
thumb: Map the terrain first
---

@chapter No global view
@title text="Context Map" sub="Domain-Driven Design, Chapter 14" art=thumb
One Bounded Context gives you no view of the others. People on other teams don't know where its edges are, and blur them without meaning to. Where two contexts have to connect, they tend to bleed into each other.

@art bleeding-edges
Reusing code across a boundary is a hazard, Evans says. Functionality and data should cross it through a translation. And the boundaries follow the teams. People who work closely share a model. People who don't talk, even on one team, drift into separate ones.

@chapter The pattern
@list heading="Draw the map" items="List every model in use@every model|Name each context@name|Mark where they touch@touch|Describe it as it stands@as it stands"
So list every model the project really uses, including unstated ones inside subsystems that aren't object oriented. Give each context a name, and let those names enter the Ubiquitous Language. Mark where the models touch, with the translation explicit. And describe the situation as it stands.

@art terrain-map
The map takes whatever form the team will share: a diagram, text, or talk. It has to name every context and make every contact clear. If a relationship doesn't match one of the chapter's patterns, don't force it. Describe what's there.

@quote text="Map the existing terrain. Take up transformations later." cite="Evans, Domain-Driven Design, Chapter 14"
That's the last line of the pattern. Map the existing terrain. Take up transformations later.

@art unknown-country
Two warnings follow. Where you find a splinter, mark it as unknown country and finish the rest first. Fix only outright contradictions until everything sits in some context. And once the map is clear, change it only after the reality has changed.

@chapter Test the boundaries
@art translator-tests
Evans's example is a routing feature, where the route finding team needed a quite different model, built for fast network algorithms. The two became separate contexts, joined by one translator that both teams maintain. Contact points deserve the most tests, because translation is subtle, and communication is thinnest there.

@words text="Say the model's name" sub="not a colleague's"
Organizing and documenting the map has only two points. Contexts have names in the language, and everyone knows where the boundaries lie. So when you talk about a change, say the model's name, not a colleague's.

@chapter A theatre's seven contexts
@code block=1 lines=1-6 focus="1@shared kernel|2@customer supplier|3@conformist|4-5@anticorruption|6@open host"
Now the lab. It reads a map: upstream, downstream, and the kind of relationship. A Shared Kernel carries a change both ways. Conformist and Customer Supplier carry it downstream. An anticorruption layer or an open host service stops it at a translator, which changes instead.

@art change-spread
The map is a theatre's seven contexts. Programming, which plans the season. The venue. The box office. Marketing. Finance. An outside payments provider. And the agencies that resell tickets. Now follow one change across it.

@math heading="change-programming" items="must change: venue, boxoffice, marketing@three models;;translators: finance, resellers@two translators;;4 reached · 2 untouched@four contexts reached"
The season planners change their model of a performance. It reaches the venue through the kernel, the box office as its customer, and marketing, which conforms to the box office. Three models must change. It stops at two translators, finance's layer and the host service for resellers. Four contexts reached, two untouched.

@math heading="change-payments" items="0 models · 1 translator@no models;;1 reached · 5 untouched@five are untouched"
Change the outside payments provider instead. Its only edge is the box office's anticorruption layer. So no models must change, one translator updates, one context is reached, and five are untouched.

@art say-it-in-language
That's the map doing its job. Before anyone touches code, the team can say, in the language, that a change to the Programming model means changing Venue, Box Office and Marketing and two translators. And a change at Payments means one translator.

@chapter Where people slip
@list heading="Common slips" items="Drawing the map you want@The first|Naming contexts after people@The second|Reusing code across a boundary@And the third"
The first slip is drawing the map you want instead of the one you have. The second is naming contexts after people or teams. Say the model's name, so the sentence tells you which translator must change. And the third is reusing code across a boundary to save a translation.

@chapter Try it
@code block=2 lines=1-5 focus="1@catalogue|2@members|3@events|4-5@feed"
Your turn. A public library: catalogue, lending, members, events, a supplier's feed of new titles, and an old fines system. The catalogue team changes its model of a title. Find the models that must change, the translators to update, and the contexts untouched. Watch the Shared Kernel's direction.

@end text="Name it, mark it, follow it"
Load the map into the lab to check, on Learn. That's learn dot get er done dot I O.
