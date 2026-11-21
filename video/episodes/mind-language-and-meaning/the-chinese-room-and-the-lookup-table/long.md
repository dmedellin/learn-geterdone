---
format: long
lesson: mind-language-and-meaning/the-chinese-room-and-the-lookup-table
title: The Chinese room and the lookup table: counting conversations
thumb: 36 quadrillion entries
---

@chapter The question
@title text="The Chinese Room and the Lookup Table" sub="Mind, Language and Meaning" art=thumb
Could a machine pass a conversation test just by looking up its answers? Count the entries it would need, and two famous arguments come into focus.

@art lookup-table
A lookup table answers by finding its input in a list, and returning the reply stored beside it. It doesn't compute a reply. Every reply it will ever give is already written down.

@chapter Keyed on the whole conversation
@art whole-conversation
Suppose a machine passes the test this way. Its reply at any moment depends on everything said so far. So the table has to be keyed on the whole conversation, not on the last remark.

@math heading="n remarks per turn,  r turns" items="n · n · … · n  =  nʳ@n choices;;n = 24,  r = 12@twenty four;;24¹² = 36 520 347 436 056 576@thirty six quadrillion"
If at each turn the judge may say one of n things, and there are r turns, that's n choices, then n again, and so on: n to the power r. Set n to twenty four and r to twelve. That's over thirty six quadrillion entries.

@art exploding-tree
And that's a twelve turn conversation where the judge has only twenty four things to say. At three turns, it's thirteen thousand eight hundred and twenty four. Each further turn multiplies it by twenty four. A real conversation has far more remarks, and far more turns.

@chapter A table against a program
@art compress
Compare a program. A program that holds a rule for forming replies can be a few thousand lines, and meet every one of those conversations. It doesn't store them. It works them out. A table's size is the number of cases it covers. A program's size is the length of the idea behind them.

@chapter Block's table
@words text="Block: passing is not sufficient" sub="it looks up, and nothing in it is intelligent"
Block takes the table as a thought experiment. Build one anyway, in principle, with every sensible conversation of some length written in. It passes the test with a Bayes factor of one, and nothing in it is intelligent. It looks up. So passing isn't sufficient for intelligence, and behaviourism is false.

@art impossible-library
The reply is that a table that can't be built tells us little about what a buildable thing must be like. Block's rejoinder is that behaviourism was a claim about what's conceptually enough. And an in principle case refutes a claim of that strength.

@chapter Searle's room
@art chinese-room
Searle's room is different. A person who reads no Chinese sits in a room, with a rulebook for manipulating Chinese symbols, and passes out replies a Chinese speaker would accept. The room runs on rules, so its size is the size of the rulebook. The count doesn't touch it.

@list heading="Searle's argument" items="The person understands nothing@understands nothing|Reply: the whole system understands@the whole system|Rejoinder: memorise the rulebook@memorise the rulebook"
Searle argues that the person understands nothing, so following the rules can't be understanding. The standard reply is that the whole system, room and rulebook and person together, understands. Searle's rejoinder is to let the person memorise the rulebook, and work in the open. The lesson doesn't choose.

@words text="A realistic passer computes" sub="whether that is understanding is open"
What the count settles is narrow. A passing system of any realistic size isn't a table, so it generalises. Whether generalising amounts to understanding is the open question. And whether a table, if built, would think, the count doesn't settle.

@chapter Where people slip
@list heading="Common slips" items="Taking a lookup table for a small program@The first|Treating the room and the table as one argument@The second|Reading the count as a refutation of Block@And the third"
The first slip is taking a lookup table for a small program. A table has no rule, so its length is the number of cases. The second is treating the Chinese room and the lookup table as one argument. Block needs the table, and Searle needs the rulebook. And the third is reading the count as a refutation of Block. His claim was about what's possible in principle.

@chapter Try it
@words text="24³ = 13 824" sub="then add one turn at a time"
Work the count yourself. Start with twenty four remarks and three turns, and check you get thirteen thousand eight hundred and twenty four. Then add one turn at a time, multiplying by twenty four, and see how quickly no table could hold it.

@end text="How many conversations?"
You can slide the number of turns and watch the table grow, on Learn. That's learn dot get er done dot I O.
