---
format: long
lesson: enterprise-patterns-web-presentation/front-controller
title: Front Controller: one handler, many commands
thumb: One door for every request
---

@chapter The question
@title text="Front Controller" sub="Patterns of Enterprise Application Architecture, Chapters 4 and 14" art=thumb
Every request to a site needs some of the same work: security, a locale, an audit record. Where should that code live, if not in every page?

@art many-pages-repeat
A complex site does similar things on every request. If that controller behaviour is spread across many objects, much of it ends up duplicated, and it's hard to change at run time. Front Controller is Fowler's answer, and he's careful to say it's a more complicated design than Page Controller.

@chapter One handler
@art one-handler
Every request goes through one handler object. It does the common work, then dispatches to a command for the part that's particular to this request. The handler is a class, not a server page, because it renders no page of its own.

@list heading="Choosing the command" items="Statically: conditional logic on the URL@statically|Dynamically: a command class named in the URL@dynamically"
It can choose the command statically, by parsing the URL with conditional logic. That's plain to read, and the compiler checks the dispatch. Or dynamically, by creating a command class from part of the URL, so you can add commands without touching the handler.

@art filter-chain
A useful companion is Intercepting Filter, which the book cites from Alur, Crupi and Malks: decorators wrapped round the handler in a chain, for authentication, logging and locale. And whichever way it's built, the commands choose the view. Once the handler has chosen the command, it plays no further part.

@art thin-web-part
Fowler also tells of a variation Rob Mee showed him. Split the handler in two: a thin web part that pulls the data out of the request, and a dispatcher that knows nothing of the web server. Now tests can drive the dispatcher directly.

@chapter Four advantages
@quote text="Only one Front Controller has to be configured into the Web server; the Web handler does the rest of the dispatching." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 14"
Fowler lists advantages, because he thinks the pattern needs them. The first: only one Front Controller has to be configured into the web server, and the web handler does the rest of the dispatching.

@art fresh-command
Second, with dynamic commands, new ones are added without changing anything. Third, a new command object is made for each request, so the commands needn't be thread safe, though they mustn't share other objects, like the model. And fourth, decorators can be added at run time.

@chapter Count the copies
@code block=1 lines=1-13 label=Java focus="2-4@reads the session's user|9-11@the invoice page"
The advantage most often claimed is removing duplicated code. Let's count it. Here are two page controllers. Each one reads the session's user, redirects to login if there's none, and writes an audit record. Then the invoice page does the same three lines.

@math heading="pages-repeat" items="1 block@one block;;6 lines in the copies@six lines;;at lines 2–4 and 9–11@two to four"
The lab compares statement lines as text and reports any run of two or more that appears more than once. It finds one block, six lines in all, at lines two to four and nine to eleven.

@code block=2 lines=1-20 label=Java focus="3-8@runs the shared steps|11-20@each page"
Now remove them with a superclass. SecurePage, a Layer Supertype, runs the shared steps and then calls show, which each page overrides. The lab reads all three classes and prints zero blocks, zero lines.

@code block=3 lines=1-8 label=Java focus="3@looks the path up|5@unless the command is public|7@runs the command"
Or with one handler. It looks the path up in a table of commands, sends a visitor with no session to login unless the command is public, writes the audit record, and runs the command. Again zero, zero.

@chapter What the count can't see
@art superclass
So the count can't choose between them. Both reach zero. Fowler grants that, to be fair, a superclass Page Controller can do much of this. His reasons for one handler are the one configuration, the dynamic commands, the fresh command per request, and the decorators. A count of repeated lines sees none of them.

@chapter Where people slip
@list heading="Common slips" items="One huge controller@The first|Only a Front Controller removes copies@The second|Letting the handler pick the view@And the third"
The first slip is picturing one huge controller. It's one small handler and many small commands. The second is thinking only a Front Controller removes what pages repeat. A superclass does it too. And the third is letting the handler pick the view. The commands do that.

@chapter Try it
@code block=4 lines=1-13 label=Java focus="2-3@a cache header|9-10@the stock report"
Your turn. Two report pages. Each sets a cache header and finds the locale before its own work, and the stock report does the same. Mark the lines that repeat by the lab's rule, with their line numbers, and how many lines the copies hold. Then say what a superclass or a front handler would do with them.

@end text="Count the copies yourself"
You can paste controllers into the lab and find what they repeat, on Learn. That's learn dot get er done dot I O.
