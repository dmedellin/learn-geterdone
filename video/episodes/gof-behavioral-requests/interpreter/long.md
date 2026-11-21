---
format: long
lesson: gof-behavioral-requests/interpreter
title: Interpreter: a small language as a tree of objects
thumb: One class per rule
---

@chapter A language of your own
@title text="Interpreter" sub="Design Patterns, chapter 5" art=thumb
When the same kind of problem keeps coming back, sometimes the best move is a tiny language. Interpreter is how the Gang of Four build one out of objects, and they're careful about where it stops.

@quote text="But the Interpreter pattern should be reserved for those cases in which you want to think of the class hierarchy as defining a language." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
The authors write this near the end, after admitting that almost any operation over a Composite could be called an interpreter. But the Interpreter pattern should be reserved for those cases in which you want to think of the class hierarchy as defining a language.

@art recurring-problem
The motivation: describing each case in a small language, and evaluating the descriptions, can beat writing a fresh algorithm every time. The book's example matches strings against regular expressions. The lesson uses arithmetic over named values, enough to price a print job.

@chapter The grammar
@code block=1 lines=1-3 label=Grammar focus="1@an expression|2@a term|3@a factor"
Here's the grammar. An expression is terms joined by plus or minus. A term is factors joined by times or divide. And a factor is a number, a name, a negated factor, or an expression in brackets.

@list heading="Participants" items="Abstract expression@abstract expression|Terminal expression@terminal|Nonterminal expression@nonterminal|Context@the context|Client@the client"
The pattern gives each rule a class. An abstract expression declares interpret. A terminal expression handles a symbol that isn't broken down, like a number or a name. A nonterminal holds an expression for each part, and interprets them. The context carries what every node needs. And the client builds the tree and calls interpret on the root.

@art context-card
The context is worth a moment. It's information global to the interpretation, here the value of each name, and it's passed to every node. The same tree in another context gives another result.

@code block=2 lines=1-17 label=Java focus="4-10@a terminal|11-17@a nonterminal"
In Java, a variable is a terminal: it just looks its name up in the context. Add is a nonterminal. It interprets its left side, interprets its right side, and adds them. The other operators follow the same shape.

@chapter The tree
@code block=3 lines=1-7 label=Java focus="2-5@builds the print|7@ninety"
And here the client builds the print job's tree by hand, no parser: setup, plus copies times, pages times per page, plus binding. Then one interpret call on the root gives ninety for the first job.

@art syntax-tree
Notice the brackets left no node. The tree's shape records what they meant. In the lab's tree there are nine nodes: five variables, two adds and two multiplies. It's four deep, down through the brackets to pages.

@math heading="The print job" items="pages × per_page = 48 × 0.05 = 2.4@forty eight;;2.4 + binding = 2.4 + 1.5 = 3.9@plus binding;;copies × 3.9 = 20 × 3.9 = 78@twenty copies;;setup + 78 = 12 + 78 = 90@plus setup"
Interpret from the leaves. Forty eight pages at nought point nought five is two point four. Plus binding, one point five, is three point nine. Twenty copies is seventy eight. And plus setup, twelve, is ninety.

@art interpret-up
Each node is interpreted exactly once, so that's nine interpret calls: one from the client on the root, and eight from nodes to their operands. The terminals end the recursion.

@art two-contexts
Now keep the tree and change only the context, to fifty copies. Same nine nodes, same nine calls. The value becomes two hundred and seven. The tree is the sentence, built once. The context is what it's interpreted against.

@chapter Benefits and limits
@list heading="Consequences" items="Easy to change and extend@easy to change|Easy to implement@easy to implement|New ways to interpret@new way|Complex grammars are hard@liability"
The benefits: the grammar is easy to change and extend, since each rule is a class. It's easy to implement, since the node classes are alike. And a new way of interpreting, like printing a sentence, is one more operation. The liability is that a complex grammar, at a class or more per rule, is hard to maintain.

@art big-grammar
For those, the authors point to parser and compiler generators. And the pattern says nothing about parsing at all. A parser, or the client, builds the tree. If new interpretations keep arriving, put them in a Visitor.

@chapter Where people slip
@list heading="Common slips" items="Calling every tree operation an interpreter@The first|Expecting the pattern to parse@The second|Growing a large grammar class by class@And the third"
The first slip is calling every operation over a tree an interpreter. Totalling a hamper's items is Composite. Evaluating a pricing rule written in a grammar is Interpreter. The second is expecting the pattern to parse. And the third is growing a large grammar one class at a time.

@chapter Try it
@words text="A museum ticket" sub="fee * (adults + children / 2) - discount"
Your turn. A museum's ticket price, where children pay half. The fee is eight, three adults, four children, and a discount of five. Draw the tree, count its nodes by class, its depth and its calls, and interpret it.

@end text="Build the tree"
Then type it into the lab and check, on Learn. That's learn dot get er done dot I O.
