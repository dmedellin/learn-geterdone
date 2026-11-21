---
format: long
lesson: ddd-distillation/domain-vision-statement-and-highlighted-core
title: Domain Vision Statement and Highlighted Core: show everyone the core
thumb: One page, a few flags
---

@chapter Before there's a model
@title text="Domain Vision Statement and Highlighted Core" sub="Domain-Driven Design, Chapter 15" art=thumb
Most of Chapter fifteen's techniques change the model and the code. These two change only a document. And they answer needs that arrive before any deep model does.

@art forgotten-vision
At the start, there's no model yet, but its development already needs a direction. Later, people need the system's value explained without studying the model. Many teams write a vision document for management, Evans notes, and it's usually forgotten once the funding arrives.

@chapter A Domain Vision Statement
@art vision-page
Evans's version keeps that form, but it's about the domain model and the value it brings, and managers and developers alike use it all the way through.

@list heading="About one page" items="The core, and its worth to the business@its worth|Leave out what any model would say@Leave out|How competing interests are weighed@competing interests|Rewritten as understanding grows@rewritten"
It's about a page on the core and its worth to the business. Leave out whatever any similar model would also say. Show how competing interests are weighed. Draft it at the start, and keep it rewritten as understanding grows.

@words text="In: forecast demand, plan the fewest van moves" sub="Out: load in two seconds · sign in by phone"
For a bike share, a sentence that belongs says the model forecasts each station's demand by hour, and plans the fewest van moves that keep bikes where riders will want them. One that doesn't, however true, says the app must load in under two seconds. That's a requirement, not the model's value.

@chapter Highlighted Core
@quote text="The mental labor of constantly filtering the model to identify the key parts absorbs concentration better spent on design thinking" cite="Evans, Domain-Driven Design, Chapter 15"
A vision statement names the core in broad terms, and each reader decides which elements it means. Different people won't pick the same ones. The mental labor of constantly filtering the model to identify the key parts absorbs concentration better spent on design thinking.

@art distillation-doc
Restructuring the code is the ideal way to show the core, but it isn't always possible soon. So mark it. The first technique is a distillation document: three to seven sparse pages on the core and how its elements work together. An entry point that sends you to the code, not a complete design document. Write it for the nontechnical members of the team too.

@art flagged-pages
The second is the flagged core. On his first day with an insurer, Evans was given a two hundred page industry model. With a business analyst, he marked the few sections that held the essential concepts. It doesn't depend on paper. A stereotype on a diagram or a structured comment will do, as long as you can tell at a glance what's core.

@chapter A rule for consulting
@art consult-first
The document also works as a process tool. On a team where any pair may change any code, some changes still need consultation. The rule: if a change would force the distillation document to change, consult first, then tell the whole team and send round the new document. Otherwise, go ahead.

@chapter Narrow or broad
@math heading="flagged-narrowly" items="core: forecast, plan, move = 3 of 12 classes@three of the twelve;;core weeks: 6 + 6 + 2 = 14 of 40@fourteen of the forty;;strongest on core: 2 of 3@two of the three"
Now the bike share's twelve classes. Flag just the three the vision sentence is about: the demand forecast, the rebalancing plan, and a move. A newcomer reads three of the twelve classes first, a quarter of the model. They carry fourteen of the forty weeks spent, and two of the three strongest developers work on them.

@math heading="flagged-broadly" items="+ Station, Dock, Bike, VanRun@stations and vans;;core: 7 of 12 classes · 27 of 40 weeks@seven of the twelve"
Now flag every class to do with stations and vans too. The core becomes seven of the twelve classes and twenty seven of the forty weeks, more than half the model.

@art broad-flag
And that flag tells a newcomer little that the class list didn't. A broad flag costs the reading it was meant to save. Whether a station belongs in the core is the team's call. Evans's advice is to keep the core small.

@chapter Where people slip
@list heading="Common slips" items="A vision of features and technology@The first|A distillation document for the whole design@The second|Only restructuring can show the core@And the third"
The first slip is writing the vision statement as a list of features and technology. The second is expecting a distillation document to describe the whole design. And the third is thinking the core can only be shown by restructuring the code.

@chapter Try it
@words text="Core: UrgencyScore · TriageRule · Booking" sub="+ 6 other classes · 5 proposed changes"
Your turn. A clinic's model has three core classes flagged, and six others. Five changes are proposed, each touching some classes. Find the share of the classes a newcomer reads first, and which of the five changes call for consultation under the process rule.

@end text="Keep the core small and visible"
Type the classes into the lab to check, on Learn. That's learn dot get er done dot I O.
