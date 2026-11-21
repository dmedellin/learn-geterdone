---
format: long
lesson: ddd-putting-the-model-to-work/model-driven-design-and-hands-on-modelers
title: Model-Driven Design: one model for the analysis and the code
thumb: The code is the model
---

@chapter Two projects
@title text="Model-Driven Design" sub="Domain-Driven Design, Chapter 3" art=thumb
Evans opens Chapter 3 with two projects that went wrong in opposite ways, and ended up in the same place.

@art wall-model
On the first, analysts and experts spent months on a detailed model, printed across a wall. It captured real knowledge. But its tangle of associations gave the developers no units they could store and change safely. So they built an ad hoc design instead.

@art bloated-code
The second was rewriting an old program that had never had a model at all. Both ended with working, bloated software whose code said little about what the system was for.

@chapter The diagnosis
@art drifting-models
Evans blames the analysis model, made to understand the domain without regard to software, with a design loosely related to it. Much of what it learned is lost when coding begins. It misses things only implementation reveals, so it's soon abandoned. And keeping a complex mapping current is, in practice, impossible.

@chapter The pattern
@quote text="MODEL-DRIVEN DESIGN discards the dichotomy of analysis model and design to search out a single model that serves both purposes." cite="Evans, Domain-Driven Design, Chapter 3"
His answer is the heart of the chapter. Model driven design discards the dichotomy of analysis model and design, to search out a single model that serves both purposes.

@art class-for-concept
Some part of the code is written to be the model, class for concept, so anyone can see which is which. When the model resists that, the model is reworked as well as the code. And because the code now expresses the model, editing the code can amount to editing the model.

@chapter The right tools
@art bus-object
That needs a language that can express the model directly. Object languages can. So can Prolog for rules and facts. In the circuit board domain, engineers had written scripts that inferred a bus of nets without ever naming it. Evans's model makes the bus an object that carries rules, and the rest becomes nearly trivial.

@words text="Show users the model, not an illusion." sub="bookmarks that are secretly files"
Letting the bones show turns to the user. A browser's bookmarks look like a list of names but are stored as files, so names a file system rejects get altered. One model fixes it: show that bookmarks are files, or store them so they follow the rules of what they name.

@chapter Hands-on modelers
@quote text="Programmers are modelers, whether anyone likes it or not." cite="Evans, Domain-Driven Design, Chapter 3"
Evans tells his own story here. Kept from coding, he watched a sound model lose its intent in the hand off, until the developers built without it. Programmers are modelers, whether anyone likes it or not. Whoever shapes the model works in the code, and whoever codes makes it say what the model says.

@chapter Count the reach
@code block=1 lines=1-9 label=Records focus="1-3@loan|4-6@hold|7-9@fine"
Here's a library's lending code, in nine pieces: three for a loan, three for a hold, three for a fine. Each record gives its module when code follows the model, and its module in a design built screen by screen and job by job.

@math heading="Following the model" items="1 + 1 + 1 + 2 = 5 touches@one, one, one and two;;3 changes in one module@three changes;;largest: renewal rule, 2@renewal"
Four changes touch the code: a shorter loan period, a pickup window for holds, a cap on fines, and no renewal while someone holds the item. Following the model, they reach one, one, one and two modules. Five touches in all, three changes in one module. The largest is the renewal rule.

@math heading="Following screens and jobs" items="2 + 2 + 3 + 2 = 9 touches@two, two, three and two;;0 changes in one module@none;;largest: fine cap, 3@fine cap"
Following screens and jobs, they reach two, two, three and two. Nine touches, none confined to one module. The largest is the fine cap, spread over the nightly job, the checkout screen and the desk screen.

@art scattered-change
The renewal rule reaches two modules either way, because it joins loans and holds. Following the model doesn't make a change local when the model says it isn't.

@math heading="model-drifts" items="fine cap moved into loans@into the loans;;fine cap change: 1 → 2 modules@two modules;;total: 5 → 6@five to six"
And here's the warning. A developer puts the fine cap into the loans code to save a call. The fine cap change now reaches two modules, and the total rises from five to six. The model is weaker, and nothing in the code says so.

@chapter Where people slip
@list heading="Common slips" items="Keep analysis apart from the code@The first|Modellers shouldn't code@The second|Give users a friendlier illusion@And the third"
The first slip is keeping the analysis model apart, so implementation can't muddy it. The second is treating modelling as a senior role that shouldn't touch code. And the third is giving users a friendlier model than the one underneath.

@chapter Try it
@code block=2 lines=1-3 label=Records focus="1@due date|2@daily fine|3@renewal"
Your turn. Student loans, with their own due date, their own daily fine and their own renewal limit. Using the module map, count the modules the change reaches both ways.

@end text="Count how far a change reaches"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
