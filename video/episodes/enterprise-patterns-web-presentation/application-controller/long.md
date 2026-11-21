---
format: long
lesson: enterprise-patterns-web-presentation/application-controller
title: Application Controller: who decides which screen comes next?
thumb: Write the flow down once
---

@chapter The question
@title text="Application Controller" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
Who decides which screen comes next? And where is that decision written down? If the answer is everywhere, this pattern is for you.

@quote text="A good signal to use an Application Controller is if you find yourself having to make similar changes in lots of different places when your application's flow changes." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 14"
That's the whole of the signal Fowler gives. A good signal to use an Application Controller is if you find yourself having to make similar changes in lots of different places when your application's flow changes.

@chapter The flow
@art wizard-steps
Think of a wizard. The user is led through screens in a set order. Some screens appear only under conditions. And the choice of screen depends on earlier input. Input controllers can make those decisions, but as the application grows, several of them need the same knowledge, and the code gets duplicated.

@art central-flow
So the pattern puts all the flow logic in one object. The input controllers ask it which command to run against the model, and which view to show. It sits between the presentation and the domain, and it's a different thing from the controller of Model View Controller.

@art two-collections
It has two jobs: choosing the domain logic to run, and choosing the view. So it typically holds two collections of references, one of domain commands, and one of views.

@chapter Fowler's test
@words text="The application decides → use one" sub="the user decides → you don't need one"
Not every system needs one. Fowler's test fits in a line. When the application decides which screen the user sees next, you want an Application Controller. When the user decides, you don't.

@art user-led
Where a user can open screens in nearly any order, there are no rules for it to hold. It earns its place where much of the code is about which screen follows which.

@chapter Keep it clean
@art mediating-layer
Fowler prefers an Application Controller with no links to the interface. It doesn't read the HTTP session, forward to a server page, or call a rich client class. That makes it testable without the interface, which is why many people think of it as a layer in between.

@words text="Smokers get an extra screen" sub="application logic, or domain logic?"
He comes down hard against putting domain logic in it, then admits the line is murky. His case: an insurance form that shows extra questions only to smokers. A few such cases can live here. If they turn up in many places, the Domain Model should drive them.

@chapter Count the copies
@code block=1 lines=1-12 label=Java focus="2-4@after the address|8@no address|9-11@the same three"
Here are two checkout controllers. After the address, send the customer to customs, or approval, or payment. After the cart, first send a customer with no address back to the address screen, then the same three.

@math heading="flow-repeat" items="1 block, 6 lines@one block;;at lines 2–4 and 9–11@two to four"
The lab, with the same rule as Front Controller, finds one block, six lines, at lines two to four and nine to eleven. That's Fowler's signal, as a count.

@art duplicated-flow
Add a screen to the flow, say a gift message before payment, and the change must be made in both places. And in every other controller that knows the order.

@code block=2 lines=1-7 label=Java focus="3@asks the address question|4-5@customs|6@payment"
Now hold the flow in one method. nextScreen asks the address question, then customs, then approval, and otherwise it's payment. It returns a path instead of redirecting, so it has no link to the request or response. The lab prints zero blocks, zero lines.

@words text="afterCart ≠ afterAddress" sub="hasAddress is true after the address step"
But check before you move. The two weren't identical. nextScreen asks the address question every time. After the address step, hasAddress is true, so the answer is the same. The conditions are questions the order answers. The order they're asked in is the flow, and that's what moved.

@chapter Where people slip
@list heading="Common slips" items="Every app needs one@The first|It does the work@The second|One flow for every presentation@And the third"
The first slip is thinking every web app needs one. Only when the flow's rules repeat. The second is thinking it does the work. It decides what comes next, and the commands do the work. And the third is sharing one flow across every presentation. Different interfaces often need different flows.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="2-4@the assessor|8-9@photos"
Your turn. An insurance claim form. After the details: the assessor, medical, or the bank. After the photos, two photo checks first. Mark the lines that repeat, with their line numbers. Then write one method, nextStep, that returns the next screen's path.

@end text="Find the repeated flow"
You can paste controllers into the lab and find the flow they repeat, on Learn. That's learn dot get er done dot I O.
