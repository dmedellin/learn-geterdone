---
format: long
lesson: gof-behavioral-requests/chain-of-responsibility
title: Chain of Responsibility: who takes the request?
thumb: Pass it on until someone takes it
---

@chapter The problem
@title text="Chain of Responsibility" sub="Design Patterns, chapter 5" art=chain-thumb
Here's a design problem that turns up in almost every user interface. By the end of this video you'll know the pattern that solves it, what it buys you, and the one thing it quietly gives up.

@art chain-click-help
You click on a button and ask for help. Maybe the button has its own help text. Maybe it doesn't, and the help should come from the panel around it. Or from the window around that. Or, in the end, from the application itself.

@words text="Who answers?" sub="The button can't know."
So who answers? The button that got the click has no idea. And you don't want it to know, because then every button would be wired to every possible helper.

@quote text="Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, 1995"
That's the first sentence of the pattern in the book. Avoid coupling the sender of a request to its receiver, by giving more than one object a chance to handle the request.

@chapter The chain
@art chain-handlers
Here's the idea. Line up every object that might handle the request. Each one knows only the next one in line, its successor. A request goes to the first. If that object can deal with it, it does. If not, it passes the request along.

@list heading="Three roles" items="Handler@a handler|Concrete handler@each concrete|Client@and the client"
There are three roles. A handler declares the operation that handles a request, and holds the link to the next one. Each concrete handler takes the requests it's responsible for and passes on everything else. And the client sends the request to the head of the chain, and knows nothing more than that.

@chapter The code
@code block=1 lines=1-11 label=Java focus="2@holds a reference|5-8@if there is a next|9@falls off the end"
In Java, the base class is small. It holds a reference to the next handler, and nothing else. Its handle method is the default: if there is a next handler, pass the request on. If there isn't, the request falls off the end, unhandled.

@code block=1 lines=12-20 label=Java focus="14@overrides handle|15-16@if the topic is renew|18@everything else"
A concrete handler, like this self service kiosk, overrides handle. If the topic is renew, the kiosk deals with it. Everything else goes to the base class, which passes it down the line. A handler with no interest in a request doesn't even have to mention it.

@code block=2 lines=1-6 label=Java focus="2-4@three constructor calls|6@to the head"
And the client builds the chain with three constructor calls, librarian, then desk, then kiosk, and sends every request to the head. Want a different chain? That's three different constructor calls, even while the program runs.

@chapter What it costs
@art chain-coupling
So what does this buy you? Coupling drops. The sender and the receiver know nothing about each other, and each handler keeps one reference, to its successor, instead of a reference to every candidate. You can add a handler, or move one, just by rewiring the chain.

@art chain-falls-off
But there's a price, and the book is honest about it. Receipt is not guaranteed. Nobody is the explicit receiver, so a request can travel all the way down the chain and fall off the end, with nobody handling it at all.

@chapter Count it
@words text="9 requests · 3 handlers" sub="kiosk → desk → librarian"
The lesson's lab makes that concrete with a library help desk. Three handlers, in order. A kiosk that renews loans. A desk that renews, places holds, and takes fines. And a librarian who handles holds, inter library loans, and lost items. Nine requests go to the kiosk.

@list heading="What happens" items="7 of 9 handled@seven of the nine|Kiosk 2 · Desk 3 · Librarian 2@the kiosk takes two|11 hand-offs@eleven times|2 donations fall off the end@the two donations"
Seven of the nine get handled. The kiosk takes two, the desk takes three, and the librarian takes two. Requests are passed along eleven times in all. And the two donations? Nobody takes them. Each is passed on twice, and falls off the end. That's the liability, as a number.

@art chain-catch-all
One fix is a catch all at the end. Add a manager who takes everything, and now all nine are handled, but the two donations travel one step further, so the hand offs rise to thirteen.

@art chain-order
And order matters. Put the desk ahead of the kiosk, and the kiosk takes nothing at all, because every renewal stops at the desk. The order of the chain decides who does the work, and the sender can't see it.

@chapter Where people slip
@list heading="Common slips" items="Assuming every request is handled@The first|Forgetting that order decides the work@The second|Wiring the chain into the sender@The third"
Three things trip people up. The first is assuming every request will be handled. It won't, unless you put something at the end to catch it. The second is forgetting that order decides who does the work. And the third is wiring the chain into the sender, which brings back exactly the coupling the pattern was meant to remove.

@chapter Try it
@words text="A bakery's order line" sub="counter → baker → owner"
To practise, try the bakery at the end of the lesson. A counter, a baker, and an owner, and six orders. Trace each one by hand. Who takes it, and how many times was it passed on? Then move the owner to the front, and say who loses work.

@end text="Run the chain yourself"
You can send the library's requests down the chain yourself, and change the order, on Learn. That's learn dot get er done dot I O. See you in the next one.
