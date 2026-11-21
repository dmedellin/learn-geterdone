---
format: long
lesson: ddd-model-integrity/bounded-context
title: Bounded Context: where does a model apply?
thumb: One word, two meanings
---

@chapter Two charges
@title text="Bounded Context" sub="Domain-Driven Design, Chapter 14" art=thumb
Chapter fourteen opens with a story. Two teams building parts of one system each needed a class for a charge. The second team found the first team's class, added the field it lacked, renamed its own idea to fit, and moved on.

@art crossed-charge
Days later, the first team's module was showing records nobody had entered, and crashing in a monthly tax report. One team had meant a charge to a customer. The other, a payment to a supplier. Their repair was two classes with two names. And after that, Evans notes, they carried on exactly as before.

@chapter One model for everything?
@art one-big-model
The most basic thing a model needs is internal consistency, which Evans calls unification. One unified model for a whole enterprise would be ideal. On a large system, it costs more than it's worth.

@list heading="Trying anyway" items="Too many replacements at once@too many|Coordination that outgrows the team@coordination|Applications forced onto one model@forced|A model swollen with options@swollen"
He lists what goes wrong when a project tries. Too many legacy replacements attempted at once. Coordination that outgrows the team. Specialised applications forced onto a model that doesn't serve them. And a model swollen with options to satisfy everyone.

@chapter Draw the line
@quote text="The model context is whatever set of conditions must apply in order to be able to say that the terms in a model have a specific meaning." cite="Evans, Domain-Driven Design, Chapter 14"
So the question becomes where each model applies. The model context is whatever set of conditions must apply in order to be able to say that the terms in a model have a specific meaning.

@art context-boundary
State where a model applies, and draw that line in three terms together: the team that owns it, the parts of the application that use it, and the code base and schema that embody it. Inside, hold the model strictly consistent. Across the line, expect translation, and design it.

@words text="Not the same as a Module"
A sidebar keeps this apart from Modules. Two models' objects usually sit in different Modules. But Modules also divide up a single model, and inside one context their separate name spaces can even hide the fragmentation the pattern exists to catch.

@chapter Two kinds of splinter
@art two-splinters
Evans names two ways a mixed model goes wrong. A duplicate concept is one idea held by two elements. Each change has to be made twice, in practice isn't, and the copies drift. A false cognate is one term two people use for different things, each sure the other means the same.

@art glossary-columns
He calls false cognates less common and more damaging, and the charge story is his example. The early warning of both is confused language, before any interface fails to fit.

@chapter A theatre's glossaries
@code block=1 lines=1-10 focus="1-5@Box Office|6-10@Venue Operations"
Now the lab, which reads glossaries: a context, a term used there, and the concept it stands for. The lesson's two contexts are a theatre's Box Office, which sells seats, and its Venue Operations team, which runs the building.

@math heading="two-teams" items="7 terms · 3 in both contexts@seven distinct terms;;false cognates: seat, hold@seat and hold;;safe to share: performance@performance;;duplicate: ticket-buyer = patron, guest@patron"
The lab counts two contexts and seven distinct terms, three of them used in both. Two are false cognates, seat and hold. One is safe to share, performance. And one concept is duplicated: the person who buys a ticket is a patron to the box office and a guest to the venue.

@art sold-broken-chair
A box office seat is a place in a performance that can be sold. A venue seat is a chair, which can break. A box office hold keeps seats back from sale. A venue hold takes a broken chair out of use. Share one Seat class, and one evening the box office sells a chair the venue had taken out.

@words text="renamed: 0 false cognates · 1 duplicate"
Now rename, as the story's teams did: the venue says chair and block. No false cognates now, but the duplicate stays, and that's allowed, since a translation across a boundary is fine. What renaming didn't do is draw a line, or set up a way to catch the next divergence.

@chapter Where people slip
@list heading="Common slips" items="One model for the whole enterprise@The first|Taking a context for a Module@The second|Thinking renaming repairs a splinter@And the third"
The first slip is setting out to give the whole enterprise one model. The second is taking a Bounded Context for a Module or package. And the third is thinking that renaming a class repairs a splinter. It removes one false cognate, and draws no boundary.

@chapter Try it
@code block=2 lines=1-10 focus="1-4@timetabling team|5-10@exams office"
Your turn. A school's timetabling team and its exams office, each with its own glossary. Find the terms both use, say which are false cognates and which are safe to share, and list the duplicate concepts with their two names.

@end text="Say where the model stops"
Paste the records into the lab to check your count, on Learn. That's learn dot get er done dot I O.
