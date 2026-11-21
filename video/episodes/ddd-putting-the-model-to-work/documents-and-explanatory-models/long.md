---
format: long
lesson: ddd-putting-the-model-to-work/documents-and-explanatory-models
title: Documents and diagrams: what they're for in Domain-Driven Design
thumb: The model is not the diagram
---

@chapter Diagrams
@title text="Documents, Diagrams and Explanatory Models" sub="Domain-Driven Design, Chapter 2" art=thumb
Every team draws diagrams and writes documents. Evans asks a sharper question: what is each one actually for?

@art small-sketch
He draws constantly in meetings, and gives diagrams their due. A sketch of three to five objects at the centre of the question keeps a discussion focused, puts everyone on the same names, and changes as fast as the talk does.

@art overgrown-diagram
The trouble starts when a diagram tries to hold the whole model. It becomes too complete to read, and it still leaves out half the story: what the concepts mean, and what the objects are for. No box and line can say that.

@quote text="Always remember that the model is not the diagram." cite="Evans, Domain-Driven Design, Chapter 2"
So he closes the section with a reminder. Always remember that the model is not the diagram.

@art text-with-sketches
He turns the usual arrangement inside out. Instead of a diagram annotated with text, he writes text illustrated with a few small, simplified diagrams, and lets the code hold the detail. Skeletons of ideas, not specifications.

@chapter Two guidelines
@quote text="A document shouldn't try to do what the code already does well." cite="Evans, Domain-Driven Design, Chapter 2"
The first guideline: documents should complement code and speech. Evans states the Extreme Programming case fairly, that running code doesn't lie. But code can bury a reader in detail, and developers aren't its only readers. A document shouldn't try to do what the code already does well. It should give meaning, the large structure and the core.

@art stale-page
The second guideline is that documents should work for a living and stay current. The test is the language. Is it written in the words the team speaks now, and in the words of the code? If the language moves on and the document doesn't, it could be archived as history.

@chapter Executable bedrock
@words text="Code's behaviour can't be argued with." sub="its message can still be wrong"
Evans qualifies the code only position too. The behaviour of code can't be argued with, but its message can be wrong. A method's name can be vague, misleading or out of date. Still, code is closer to the ground than any other document, and it must use the same language as the team.

@chapter Explanatory models
@art route-two-ways
One model drives the code, the design and the talk. But other models can teach the domain, and they're better not drawn as object models. Evans sets a class diagram of a shipping route beside a picture of the same route as handling, storage and transport. Read together, both are easier to follow.

@chapter The bike-share
@code block=1 lines=1-7 label=Records focus="3@trip|4@rebalancing|5@membership|6-7@day pass"
Here's a city bike-share, with a design document written at launch a year ago. Each record is a concept, then the document's term, the word the team speaks now, and the code's name. A dash means no name. Look at trip, rebalancing and membership, then the day pass and the morning peak.

@math heading="last-years-document" items="7 concepts · 2 named alike@seven concepts;;rental · redistribution · subscription@rental;;3 stale terms × 2 = 6 translations@six in all"
The lab finds seven concepts, two named alike by all three. The document says rental for a ride, redistribution for rebalancing, and subscription for a membership. Speech and code agree each time, and the document alone differs: two translations each, six in all. Those are the stale terms.

@art two-gaps
There are two gaps, and they're different. The document has no word for the day pass, a product added after launch. And the code has no name for the morning peak, and shouldn't. Riders flowing downhill before nine is an explanatory model the team reasons with, not a class.

@math heading="revised-document" items="3 stale terms replaced@replaced;;0 translations@no translation;;one gap left: the code's morning peak@morning peak"
After a morning's work, the three stale terms are replaced and the day pass gets a paragraph. Now there's no translation between document, speech and code on any concept all three name. The only gap left is the morning peak, by design.

@chapter Where people slip
@list heading="Common slips" items="Taking the diagram for the model@The first|Keeping every document current by willpower@The second|The code is the only document@And the third"
The first slip is taking the diagram for the model. The second is keeping every document current by willpower, even one that plays no real part. And the third is concluding the code is the only document a team needs.

@chapter Try it
@code block=2 lines=1-4 label=Records focus="1@fault|3@e bike|4@battery swap"
Your turn. Four concepts from the repair workshop. Count the translations by hand, and name the stale document terms, like fault and e bike, where speech and code agree and the document differs. Then say what's different about the battery swap.

@end text="Find the stale terms"
Check your answer in the lab, on Learn. That's learn dot get er done dot I O.
