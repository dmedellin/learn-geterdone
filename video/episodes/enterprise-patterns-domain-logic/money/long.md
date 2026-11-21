---
format: long
lesson: enterprise-patterns-domain-logic/money
title: Money: how splitting five cents loses a penny
thumb: Where did the penny go?
---

@chapter The missing type
@title text="Money" sub="Patterns of Enterprise Application Architecture, Chapter 18" art=thumb
Split five cents seventy thirty. It sounds trivial. Fowler's Money pattern shows that no simple rounding rule gets it right.

@art two-currencies
Fowler is puzzled that money isn't a first class type in any mainstream language, because its absence causes two kinds of trouble. The obvious one is currencies: adding dollars to yen. The subtle one is rounding. Amounts are usually rounded to the smallest unit, and it's easy to lose pennies doing it.

@chapter The pattern
@art coin-bundle
His answer is a Money class with an amount and a currency, together. The amount is an integral type or a fixed decimal. And he says to avoid any floating point type absolutely, because it brings back the rounding problems Money exists to avoid.

@words text="Ten cents ≈ 0.10, never exactly" sub="the lesson's own explanation"
The lesson adds the reason in one sentence. Binary floating point can't hold most decimal fractions exactly, so ten cents is stored as a number very near ten cents, and the error shows up in totals.

@list heading="Money is a Value Object" items="Equal by amount and currency@equality|Adding two currencies is an error@adding two currencies|Conversion goes through a convertor@convertor object"
Money is a Value Object, so its equality rests on the amount and the currency. Its arithmetic knows its currency. Most simply, adding two currencies is an error. Multiplying by a rate is ordinary. And converting goes through a convertor object, because some rules, like the fixed euro rates, round in their own way.

@chapter Foemmel's conundrum
@art split-bar
Here's the conundrum, which the book credits to Matt Foemmel. A rule says a sum must be split seventy percent to one account and thirty to another, and the sum is five cents.

@math heading="5 cents, split 70 : 30" items="exact: 3.5 and 1.5@exact shares;;nearest: 4 + 2 = 6 (+1)@to nearest;;down: 3 + 1 = 4 (−1)@both down;;up: 4 + 2 = 6@both up"
The exact shares are three and a half and one and a half. Round both to nearest, and you get four and two, a penny gained. Round both down, and it's four in all, a penny lost. Round both up, and it's six.

@quote text="There's no general rounding scheme I can apply to both that will avoid losing or gaining a penny." cite="Matt Foemmel, in Fowler, Patterns of Enterprise Application Architecture, Chapter 18"
As the conundrum ends: there's no general rounding scheme I can apply to both that will avoid losing or gaining a penny.

@chapter The ways out
@list heading="Ways out Fowler has seen" items="Ignore it@Ignore it|Last share takes the rest@last share|Caller picks each rounding@caller choose|An allocator@favourite"
Fowler lists the ways out he's seen. Ignore it, which worries accountants. Give the last share whatever is left. Let the caller choose a rounding for each share, which gets complicated across ten accounts. And his favourite, an allocator that takes the ratios and returns shares with no penny dropped.

@art allocator
The lab's allocator rounds every share down, then gives the cents left over one each to the shares, in order from the first. On five cents, that's three and one, then one more cent to the first: four and one, five in all.

@chapter More shares
@math heading="A dollar, three ways" items="nearest: 33 + 33 + 33 = 99 (−1)@by nearest;;allocator: 34 + 33 + 33 = 100@the allocator"
With two shares, last takes the rest and the allocator agree. You need more shares to see the difference. Split a dollar three ways by nearest, and you get thirty three three times, ninety nine, a cent lost. The allocator gives thirty four, thirty three, thirty three. A hundred.

@art pile-on-last
Now split a dollar seven ways, with the last share taking what's left. That's fourteen six times, then sixteen. The total is kept, but the last share is nearly two cents from its exact value. That's the fault the book names: pennies pile up on the last share. The allocator keeps every share within a cent.

@code block=1 lines=1-19 label=Java focus="8@leaves the splitting|15-17@add back up"
Here's the caller's side: a refund shared across the payments that paid for an order. It leaves the splitting to Money, then checks the parts add back up. Under nearest rounding, that check can fail. Under an allocator, it can't.

@chapter Where people slip
@art extra-penny
Why does this keep happening? Each share is rounded without regard to the others, so the errors don't cancel. That's Fowler's point: no rounding scheme applied to every share can promise they will.

@list heading="Common slips" items="Nearest keeps the total@The first|Use a double, round at the end@The second|Last takes the rest solves it@And the third"
The first slip is thinking rounding each share to nearest keeps the total. The second is using a double and rounding at the end. And the third is thinking the last share taking the rest solves it.

@chapter Try it
@words text="100 cents · six equal shares" sub="nearest, then the allocator"
Your turn. Split a hundred cents into six equal shares, first by nearest, then with the allocator. Work each share, the total, and the total less the amount, and the exact share, by hand.

@end text="Split a sum yourself"
You can try every rounding rule on any split, on Learn. That's learn dot get er done dot I O.
