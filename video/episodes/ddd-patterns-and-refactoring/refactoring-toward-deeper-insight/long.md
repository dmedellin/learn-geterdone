---
format: long
lesson: ddd-patterns-and-refactoring/refactoring-toward-deeper-insight
title: Refactoring Toward Deeper Insight: change the model when you learn more
thumb: Don't wait for proof
---

@chapter More than tidy code
@title text="Refactoring Toward Deeper Insight" sub="Domain-Driven Design, Chapter 13" art=thumb
Chapter thirteen gathers Part three into one account. Evans opens with three things to focus on. Live in the domain. Keep changing the angle you look at it from. And keep an unbroken dialogue with the domain experts.

@art keyboard-and-model
The classic picture of refactoring is a developer or two at the keyboard, improving code in small steps, with unit tests to confirm nothing broke. That should go on all the time, Evans says. But it isn't the whole story.

@chapter Where it starts
@list heading="Triggers, even when the code looks tidy" items="An awkwardness rooted in the model@awkwardness|Language drifted from the experts'@drifted|Requirements that don't fit@don't fit naturally|A developer who has learned more@learned more"
This expanded kind may begin with a problem in the code, an awkwardness whose root is in the model. But unlike the conventional kind, it can also begin when the code looks tidy. When the model's language has drifted from the experts'. When new requirements don't fit naturally. Or when a developer has simply learned more.

@art exploration-team
When a change needs more than a few hours, the initiators gather a few people who know the area, with a domain expert where there are subtleties. They brainstorm for half an hour to an hour and a half, then code what they found, or sleep on it and meet again a couple of days later.

@list heading="Exploration teams" items="Self-determination@Self determination|Scope and sleep@scope and sleep|Exercising the Ubiquitous Language@exercising"
Evans names three keys. Self determination: the team forms and disbands with no standing structure. Scope and sleep: a few short meetings, and if you're stuck, a smaller piece of the problem. And exercising the Ubiquitous Language, whose refinement is what goes back into the code.

@chapter Timing
@quote text="If you wait until you can make a complete justification for a change, you've waited too long." cite="Evans, Domain-Driven Design, Chapter 13"
Teams are too cautious, he says. They notice the danger of touching code, and miss the danger of living with a clumsy design. Demanding a justification first tends to stop refactoring, or drive it underground, because the costs and benefits can't be calculated. If you wait until you can make a complete justification for a change, you've waited too long.

@list heading="When, and when not" items="Refactor: the design no longer says what you understand@no longer says|Refactor: an implicit concept you can make explicit@implicit|Not the day before a release@the day before a release|Not technique that misses the core@show off technique"
So refactor when the design no longer says what the team now understands, when an important concept is implicit and you see how to make it explicit, or when you can make an important part suppler. And he fences it. Not the day before a release. Not designs that show off technique but miss the core.

@chapter Crisis as opportunity
@art punctuated
He closes with biology. For a century after Darwin, evolution was pictured as steady change. Later it came to be seen as long stability broken by short bursts. Refactoring toward deeper insight has that rhythm. A breakthrough often arrives looking like a crisis, a model suddenly seen to be wrong, and then steady refinement starts again.

@chapter A clinic's cancellations
@art rule-in-three-places
Now the lab, on a clinic's appointment system. Its rule for late cancellation is a twenty four hour window, with urgent visits exempt. But it's nowhere a concept. The booking screen, the reminder job and the invoice run each work it out, and urgency is a flag on the patient record.

@math heading="rule-implicit" items="window 48 hours: 3 · urgent exempt: 3@forty eight;;fee amount: 1 · reminder text: 1@new fee;;3 + 3 + 1 + 1 = 8 touches, 2 confined@eight module touches"
Four change requests. Widening the window to forty eight hours touches three modules. Exempting urgent visits, three. A new fee amount, one, and a new reminder text, one. That's eight module touches, with two changes confined to one module.

@art rule-explicit
Then the refactoring makes the rule explicit: a cancellation policy, in a module of its own that the other three call.

@code block=1 lines=1-19 focus="3@window|9-11@last free cancellation|13-17@is late"
It holds the window, works out the last free cancellation, and decides whether a cancellation is late, with urgent visits exempt.

@math heading="rule-explicit" items="1 + 2 + 1 + 1 = 5 touches, 3 confined@five module touches;;largest: 2, the urgent exemption@the screen"
Now the window change touches one module. The urgent exemption touches two, because the screen still has to show it. The other two, one each. Five module touches, three confined. But that's only these four requests. Nobody could have calculated the gain in advance.

@chapter Where people slip
@list heading="Common slips" items="Waiting for full justification@The first|Refactoring only when code smells@The second|Licence for any change@And the third"
The first slip is waiting to refactor until the change can be fully justified. The second is refactoring only when the code smells. And the third is taking the case for refactoring as licence for any change. Lean toward refactoring, Evans says, but don't be dogmatic.

@chapter Try it
@code block=2 lines=1-13 focus="1-7@before|8-13@after"
Your turn. A school timetable, before and after the length of a period becomes a Period class in its own module. For each design, give the modules each change touches, the total module touches, and the changes confined to one module.

@end text="Lean toward refactoring"
Enter both designs in the lab to check, on Learn. That's learn dot get er done dot I O.
