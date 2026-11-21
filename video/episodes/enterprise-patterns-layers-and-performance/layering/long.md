---
format: long
lesson: enterprise-patterns-layers-and-performance/layering
title: Layering: the one rule about which way dependencies run
thumb: Never depend on the page
---

@chapter Why layers
@title text="Layering" sub="Patterns of Enterprise Application Architecture, Chapter 1" art=thumb
Martin Fowler's favourite architectural pattern is layers, and his first chapter is about them. It has exactly one fixed rule, and a neat test for when you've broken its spirit.

@art protocol-stack
He starts with network protocols: FTP on TCP, on IP, on ethernet. A higher layer uses the services of the one below, and the lower layer is unaware of the higher. That's what buys the benefits. You can understand one layer without knowing much about the others, replace a layer, and build many services on one lower layer.

@art ripple-field
There are two costs. Layers don't encapsulate everything, so a new field that has to be shown and stored ripples through every layer in between. And extra layers can harm performance. The hardest part, he says, is deciding what the layers are.

@chapter How we got three
@words text="Screens that knew SQL" sub="client–server, 1990s"
In the nineteen nineties, client server tools made two layers easy, with widgets that knew SQL. That worked while the job was showing and updating rows. But domain logic written into the screens got duplicated. Written as stored procedures, it was poorly structured and tied to one vendor.

@words text="Then came the Web"
The object community's answer was a third layer for the domain. It made little headway until the Web. Suddenly every application with its logic in a rich client had to be rewritten for a browser, while a well layered one needed only a new presentation.

@chapter Three layers
@art three-layers
Fowler names them presentation, domain and data source. Presentation is how a user, or a program, interacts with the software. Data source talks to databases, messaging systems and other packages. And domain is the work itself: calculation, validation, and choosing which data source logic to run.

@quote text="The domain and data source should never be dependent on the presentation." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 1"
And here's the rule. The domain and data source should never be dependent on the presentation. Notice which way it runs. The presentation reading the data source directly is less tidy, but Fowler concedes it's often the better choice.

@chapter The second presentation test
@art two-presentations
How do you tell domain logic from presentation logic? Fowler's check: imagine adding a radically different presentation, like a command line to a web application. Whatever you'd have to duplicate is domain logic that has leaked into the presentation.

@code block=1 lines=1-15 label=Java focus="3-5@lines three to five|11-13@eleven to thirteen|6@line six|14@fourteen"
His example is a product list where any product whose sales rose more than ten percent is coloured red. Here it is in two presentations. The same three lines appear twice: lines three to five, and eleven to thirteen. Line six and line fourteen differ, because each shows the result in its own way.

@code block=2 lines=1-14 label=Java focus="2-4@isRising|7-9@web page|11-14@command line"
So move the rule into the domain, as isRising. Now the web page and the command line both ask it. One passes a flag, the other appends a star. The domain decides whether there's something to highlight. Each presentation decides how.

@art copied-lines
Fowler isn't dogmatic. A reviewer, Alan Knight, wondered whether the rule in the page was the start of a decline, or a reasonable shortcut. Fowler's answer is that it's both, and the test tells you which side you're on.

@chapter Where to run them
@art one-process
A layer isn't a tier. Running everything on servers is simplest, because there's one place to upgrade and fix. Keep domain logic on the server, and keep the code in one process if you can, because separate processes cost performance and complexity.

@chapter Where people slip
@list heading="Common slips" items="Three layers need three machines@The first|A rule in one page is harmless@The second|The page must never touch the data source@And the third"
The first slip is thinking three layers need three machines. The second is thinking a rule in the page is harmless while there's only one page. The second presentation shows it isn't. And the third is thinking the presentation must never touch the data source. The rule forbids calls into the presentation, not every call that skips a layer.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="3-4@report screen|10-11@nightly export"
Your turn. Here's a report screen and a nightly export. Mark the lines the second presentation forced you to copy, counting only identical lines, at least two in a row. Then write the domain method both would call instead, on the class it belongs to.

@end text="Find the copied lines yourself"
You can paste two presentations into the lab and see what they share, on Learn. That's learn dot get er done dot I O.
