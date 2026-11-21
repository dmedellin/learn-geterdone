---
format: long
lesson: ddd-implicit-concepts/breakthrough
title: Breakthrough: when small refactorings open onto a deeper model
thumb: Not a technique, an event
---

@chapter Not linear
@title text="Breakthrough" sub="Domain-Driven Design, Chapter 8" art=thumb
Refactoring usually pays a little for a little. A responsibility moved here, an association adjusted there. Evans's point in Chapter 8 is that the returns aren't linear.

@art stepping-curve
Each refinement gives the team a clearer view. And that clarity is what makes a sudden, larger insight possible, after which the model is both more powerful and simpler.

@quote text="This sort of breakthrough is not a technique; it is an event." cite="Evans, Domain-Driven Design, Chapter 8"
This sort of breakthrough is not a technique. It is an event. What a team controls is the steady work beforehand. The challenge is to see the moment for what it is.

@chapter The story
@art adjustments-pile
The story comes from a project for an investment bank. After a winter of refactoring, each lender's part of a loan followed its fixed share of the agreement behind it. But exceptions kept arriving: lenders putting in more or less than their share on a given draw. The team added adjustment objects. Complexity grew, and rounding discrepancies wouldn't go away.

@art share-pie
Then, one week, the team saw that the two sets of shares could change independently, and that shares of any divisible value were one concept. Evans drew a small abstract model of shares, a share pie, and the special cases fell away.

@words text="A constraint that wasn't true" sub="and a class the experts never recognised"
The new model removed a constraint that wasn't true of the business, and kept the true ones. And one old class turned out not to be a banking term at all. The experts had said they didn't understand it. It had been invented by a team that hadn't yet understood the domain.

@chapter A sobering decision
@list heading="Four questions" items="How long to get back? About three weeks@How long|Solvable without it? Probably, no way to be sure@without the change|Will the next release suffer? Yes@next release|Is it right? Yes, lower risk long-term@the right thing"
The new model worked, and the whole team felt sick. The project was late, with no automated tests. The manager asked four questions. How long to get back? About three weeks. Could the problems be solved without the change? Probably, with no way to be sure. Would the next release suffer? Yes. And was it the right thing? Yes.

@art payoff
He let them go ahead, and it took three weeks. The surprising requirement changes stopped, the rounding settled down, and the share pie became part of the language that developers, experts, and even the marketing people used.

@chapter A shared kitchen
@words text="Ownership 50 · 30 · 20" sub="Hours used: 9 · 7 · 5"
Now a model of the lesson's own. Three caterers share a kitchen. They own its equipment fifty, thirty, twenty. This month they used it nine, seven and five hours. The lease is split by ownership, the gas bill by hours. A first design rounds each part to the nearest cent.

@math heading="lease-nearest · 9,999¢" items="4,999.5 · 2,999.7 · 1,999.8@exact parts;;5,000 · 3,000 · 2,000 = 10,000@ten thousand;;+1¢@one cent more"
The lease is nine thousand nine hundred and ninety-nine cents. The exact parts are four thousand nine hundred ninety-nine point five, two thousand nine hundred ninety-nine point seven, and one thousand nine hundred ninety-nine point eight. Rounded, they total ten thousand. One cent more than the bill.

@math heading="gas-nearest · 4,000¢" items="1,714 · 1,333 · 952 = 3,999@seventeen fourteen;;−1¢@a cent short"
The gas bill is four thousand cents. Split nine, seven, five, that's seventeen fourteen, thirteen thirty-three, and nine fifty-two. A total of three thousand nine hundred and ninety-nine, a cent short.

@art kitchen-split
Each part was rounded without knowing what the others did. Nobody's fault in particular. It's the kind of discrepancy the bank's team kept fighting with ever cleverer code.

@code block=1 lines=1-20 label=Java focus="11@rounds every part down|15-17@left over"
Now give the split to one concept: a share pie. It rounds every part down, then hands out the cents left over, one each, from the first member.

@math heading="share pie" items="lease: 5,000 · 3,000 · 1,999 = 9,999@the lease becomes;;gas: 1,715 · 1,333 · 952 = 4,000@the gas;;0 off · largest gap 0.8¢@nothing off"
The lease becomes five thousand, three thousand, and nineteen ninety-nine. The gas, seventeen fifteen, thirteen thirty-three, and nine fifty-two. Both totals match, nothing off. The price is a slightly less even part: the third caterer falls point eight of a cent short of exact.

@art two-pies
Keep it in proportion. A cent isn't why Evans's team changed its model. The rounding was a symptom. The change was the discovery that shares were a concept, and one supposed rule was false.

@chapter Focus on basics
@list heading="Don't wait for it" items="Keep crunching knowledge@crunching|Keep the language sharp@language|Make implicit concepts explicit@explicit|Make the design suppler@suppler"
And Evans's advice is modest. Don't sit waiting for a breakthrough. Keep crunching knowledge, keep the language sharp, make implicit concepts explicit, and make the design suppler. One breakthrough, he adds, made the next visible.

@chapter Try it
@words text="10,000¢ · ratios 3 3 1" sub="nearest, then the share pie"
Your turn. A cleaning contract of ten thousand cents, split three, three, one by floor space. Work out the exact parts, then each caterer's part and the total under both rules.

@end text="Split the bill both ways"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
