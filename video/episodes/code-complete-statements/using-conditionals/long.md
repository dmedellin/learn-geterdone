---
format: long
lesson: code-complete-statements/using-conditionals
title: If-else chains: the order costs, the last else catches
thumb: Common case first, trap the rest
---

@chapter The question
@title text="Using Conditionals" sub="Code Complete, chapter 15" art=thumb
Given a decision, how should you lay out the statement that makes it? That's chapter fifteen's question, and it has more answers than you'd expect.

@art nominal-path
Start with the plain if. Write the nominal path first, the one normally taken, and the unusual cases after it. McConnell shows a routine whose error cases sit sometimes in the if and sometimes in the else, then rewrites it so the normal path runs straight down and the errors collect at the bottom.

@list heading="The plain if" items="Normal case after the if, not the else@normal case|Branch correctly on equality@on equality|No empty if clause: negate the test@empty"
So put the normal case after the if rather than after the else. Branch correctly on equality, because greater than where you meant greater than or equal is the conditional's own off by one error. And don't leave an if clause empty just to act in the else. Negate the test instead.

@chapter Chains
@list heading="If-then-else chains" items="Complicated test → well-named boolean function@well named|Most common cases first@most common|Cover every case with a final else@final else|Use a case statement where one fits@case statement"
Chains of tests get their own guidelines. Replace a complicated test with a call to a well named boolean function. Put the most common cases first. Make sure every case is covered, with a final else. And where a case statement fits, use it instead.

@words text="Most common first" sub="1. the reader finds it  2. fewer tests"
The chapter gives two reasons for common first, in this order. A reader finds the usual case without wading through the exceptions. And the code makes fewer tests to reach it.

@chapter Count the tests
@code block=1 lines=1-13 label=Java focus="2@hundreds digit|3-4@server errors|9-10@success|12@final return"
Here's the lesson's classifier. It sorts HTTP status codes by the hundreds digit. It tests server errors first and success last. The four tests are mutually exclusive, so any order gives the same answers. The final return is where the error trap goes.

@art chain-steps
Reaching the first condition costs one test, the second two, and so on. Weight each by how often it happens. The lesson's frequencies are illustrative: five percent server errors, ten client errors, fifteen redirects, and seventy percent successes.

@math heading="Expected tests" items="0.05·1 + 0.10·2 + 0.15·3 + 0.70·4 = 3.50@as written;;0.70·1 + 0.15·2 + 0.10·3 + 0.05·4 = 1.50@best order;;3.50 − 1.50 = 2 saved@two tests"
As written, the chain makes three point five tests per status on average, because the most common answer is tested last. In the best order, it makes one point five. That's two tests per status saved.

@chapter Where the else goes
@art else-bucket
Now move the final else. Test success first and let server errors fall to the else, and it's one point four five tests, already the best order, nothing saved. But test the three other classes and leave success to the else, and it costs two point eight.

@math heading="Success left to the else" items="written: 14/5 = 2.80@two point eight;;best reordering: 13/5 = 2.60@two point six;;saved: 1/5 = 0.20@point two"
As written, that's two point eight. Reorder those three conditions as well as you can, and you only get to two point six, a saving of point two. Seventy percent of the cases still pass all three tests on the way to the else. The cure isn't reordering. It's testing the common case by name.

@chapter Case statements
@art case-switch
Section fifteen point two is the case statement, one value fanning out to its cases.

@list heading="Case statements" items="Order cases meaningfully@order|Keep each action short@short|Don't invent a variable to switch on@invent|Default: a real default or an error trap@default clause|End every case explicitly@end explicitly"
For case statements, order the cases alphabetically, numerically, normal first, or by frequency. Keep each action short. Don't invent a variable just to switch on it. Use the default clause for a real default or to detect errors, never to hold the last real case. And in the C family, every case must end explicitly.

@art fall-through
Otherwise control drops into the next case. McConnell says a deliberate fall through is useful about as often as you find someone who'd rather have a used Pontiac Aztek than a new Corvette. Where you do write one, comment it.

@art trap-net
And the default, like the last else, is a net. It catches every value no branch handled, and reports it in a message meant for the programmer, not the user.

@quote text="To trap errors, use the default clause in a case statement or the last else in a chain of if-then-else statements." cite="McConnell, Code Complete, 2nd ed., Chapter 15, p. 366"
That's one of the chapter's key points. To trap errors, use the default clause in a case statement or the last else in a chain of if then else statements.

@chapter Where people slip
@list heading="Common slips" items="Thinking order never matters@The first|A chain is complete if it handles what you thought of@The second|Reordering tests that depend on each other@the third"
The first slip is thinking the order of exclusive tests doesn't matter. Not to the result, but to the cost and the reader. The second is calling a chain complete because it handles every case you thought of. And the third is reordering range tests, like status at least five hundred then at least four hundred, which only work in their order.

@chapter Try it
@code block=2 lines=1-12 label=Java focus="3@tests four methods|11@what happens"
Your turn. This router tests four methods. Name a request no branch handles, say what happens to it, and write the change that traps it. Then a second router tests DELETE, POST, then GET, at five, fifteen and eighty percent. Work out its tests per request, as written and by frequency.

@end text="Weigh a chain's order"
You can type your frequencies into the chain lab and check your answers, on Learn. That's learn dot get er done dot I O.
