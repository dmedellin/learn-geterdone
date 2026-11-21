---
format: long
lesson: gof-behavioral-requests/mediator
title: Mediator: untangle a group of objects, and what it costs
thumb: Everyone talks to one
---

@chapter The tangle
@title text="Mediator" sub="Design Patterns, chapter 5" art=thumb
Mediator is one of the easiest patterns to sell, because its benefit is easy to count. Its cost isn't, and the book is honest about that from the start. So let's keep both in view.

@quote text="The Mediator pattern trades complexity of interaction for complexity in the mediator." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the fifth of its consequences, and it's the whole trade. The Mediator pattern trades complexity of interaction for complexity in the mediator.

@art full-mesh
The motivation begins with a tension. Spreading behaviour over many objects helps reuse. But then the objects get connected to each other, in the worst case each to every other, and none can work without the rest. The system behaves as if it were one piece.

@art dialog-widgets
The book's example is a dialog box. A button is enabled only when a field has text. A list's selection fills the field. Rather than subclassing every widget for every dialog, one director object knows the widgets and coordinates them. Each widget knows only the director.

@chapter The pattern
@art star
So there's a mediator, which defines the interface colleagues use to talk to it. A concrete mediator implements the cooperation, and knows its colleagues. And each colleague holds a reference to its mediator only, and goes to it wherever it would have gone to a fellow colleague.

@art cake-form
Colleagues must tell the mediator when something happens. Either the mediator observes them, through Observer, or it offers a notification operation, and a colleague passes itself. The lesson's bakery form does the second.

@code block=1 lines=1-20 label=Java focus="4-8@knows only the form|12-15@if the flavour|16-17@the pickup"
Here's the lesson's cake order form. A field knows only the form, and when it changes, it tells the form, passing itself. The form decides what that means. If the flavour changed, it sets the earliest pickup day and the base price. If the pickup changed, it may add a rush fee.

@chapter Five consequences
@list heading="Consequences" items="Limits subclassing@limits subclassing|Decouples colleagues@decouples|Simplifies protocols@simplifies|Abstracts cooperation@abstracts|Centralizes control@centralizes control"
Five consequences. It limits subclassing, because changing the behaviour means subclassing the mediator alone. It decouples colleagues. It simplifies protocols, turning many to many into one to many. It abstracts how objects cooperate, so you can look at the interaction by itself. And it centralizes control, which is the warning.

@art monolith
The mediator can become more complex than any colleague, a monolith that's hard to maintain. The book's own sample admits that its director's change handler grows with the dialog.

@chapter Count it
@math heading="Five fields" items="pairwise: 5 × 4 ÷ 2 = 10 to build@five times four;;one changes: 5 − 1 = 4@five minus one;;mediated: 5 to build, 1 to change@through the form"
The cake form has five fields: size, flavour, pickup, message and price. Connected pairwise, that's five times four, over two: ten connections to build. When one field's interface changes, five minus one, four connections change. Through the form, it's five to build, and one to change.

@math heading="Eight fields" items="pairwise: 8 × 7 ÷ 2 = 28; 7 to change@eight times seven;;mediated: 8 to build, 1 to change@against eight;;28 ÷ 8 = 3.5× · 7×@three point five"
Add candles, a box and allergens, and there are eight. Pairwise, eight times seven over two, twenty eight to build and seven to change, against eight and one. That's three point five times as many to build, and seven times as many to change.

@art mesh-grows
Pairwise grows with the square of the colleagues, mediated with their number. That's the pattern's case, in a number. But the count leaves out the other side: every rule those twenty eight connections carried now lives in one method, and no tile measures that.

@chapter Where people slip
@list heading="Common slips" items="Counting only the connections saved@The first|Treating a facade as a mediator@The second|Assuming everyone talks to everyone@And the third"
The first slip is counting only the connections saved. The second is treating a facade as a mediator. A facade's protocol runs one way, and its subsystem doesn't know it exists. A mediator's colleagues call it, and it calls them back. And the third is assuming every colleague talks to every other. That's the worst case. Count the pairs that really interact.

@chapter Try it
@words text="A mixing desk: 7 controls" sub="fader · mute · solo · pan · eq · send · meter"
Your turn. A recording studio's mixing desk has seven controls that all affect one another. Give the connections to build, and to change when one control changes, pairwise and through a mediator. Then list two interactions the mediator's method would have to handle.

@end text="Count both ways"
Then type the names into the lab under each scheme, on Learn. That's learn dot get er done dot I O.
