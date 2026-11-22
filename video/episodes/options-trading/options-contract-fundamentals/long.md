---
format: long
lesson: options-trading/options-contract-fundamentals
title: Options contract fundamentals: rights, obligations and the multiplier
thumb: Read the contract first
---

@chapter The question
@title text="Options Contract Fundamentals" sub="Options Trading" art=thumb
Before you look at a chart or pick a strategy, there's a simpler question. What does one option contract actually say? Who gets a right, who takes on an obligation, and how many dollars move when you trade it?

@art contract-card
An option is a contract, and a contract has terms. Read them first, the way you'd read a lease before signing it. Everything else in options trading is built on top of these few lines.

@list heading="Contract terms" items="Underlying@an underlying|Call or put@a type|Strike@a strike price|Expiration@an expiration|Multiplier@a multiplier|Exercise style and settlement@exercise style"
Every option specifies an underlying, the security it's tied to. It has a type, call or put. It has a strike price and an expiration. And it has a multiplier, an exercise style, and settlement terms.

@chapter Call or put
@words text="Call → buy at the strike · Put → sell at the strike"
The type tells you which way the deal runs. A call relates to buying the underlying at the strike. A put relates to selling the underlying at the strike. Keep that one sentence in your head and the rest of the course gets much easier.

@chapter Holder and writer
@art holder-writer
Every contract has two sides. The holder buys a right. The writer receives the premium and, in return, accepts an obligation if they're assigned. Money and risk flow in opposite directions.

@list heading="Long or short" items="Long = holder rights@Long means|Short = writer obligations@Short means|Assignment exposure@assignment"
That's what long and short mean here. Long means you hold the rights. Short means you've written the contract, so you carry the obligations, and with them assignment exposure.

@words text="The holder chooses" sub="The writer can be assigned"
And notice the difference. The holder chooses whether to exercise. The writer doesn't choose. Under the contract rules, the writer can be assigned. Confusing a right with an obligation is one of the most common early mistakes.

@chapter The multiplier
@art share-block
Now the dollars. Standard equity contracts commonly represent one hundred shares. That number is the contract multiplier, and it's what turns a quote on your screen into real money.

@math heading="Quote to contract dollars" items="Premium quoted: $4.00 per share@four dollars;;$4.00 × 100 × 1 contract = $400@times one hundred;;$4.00 × 100 × 3 contracts = $1,200@three contracts"
Equity option premiums are normally quoted per share. So a premium quoted at four dollars is four dollars times one hundred, times one contract: four hundred dollars. Buy three contracts and it's twelve hundred dollars.

@art quote-to-dollars
The same rule applies to the payoff. Multiply the per share premium and the per share payoff by the multiplier and by the quantity. Treating the quoted premium as the total cost is the first mistake the lesson warns about.

@chapter Adjusted contracts
@art adjusted-deliverable
But one hundred shares is an assumption, not a law. Corporate actions can change what a contract delivers. An adjusted contract can represent a different number of shares, or cash, or another deliverable altogether. So confirm the security, and the exact deliverable, before you trust the standard math.

@chapter Cash at the open, P and L at expiration
@art expiry-payoff
Here's the full picture for one contract line. At the open, the holder pays the premium and the writer receives it. At expiration, what each side ends up with depends on where the stock finishes compared with the strike.

@math heading="Long 100 call, $4.00, one contract" items="Pay at the open: $4.00 × 100 = $400@pays four hundred;;Stock $110: (10 − 4) × 100 = +$600@one hundred and ten;;Writer at $110: −$600@the writer"
Take a long call with a one hundred strike, bought at four dollars. The holder pays four hundred dollars at the open. If the stock is one hundred and ten at expiration, the payoff is ten minus four, times one hundred: six hundred dollars. And the writer, on the other side, is down six hundred.

@chapter Where people slip
@list heading="Common mistakes" items="Quoted premium as total cost@The first|Ignoring adjusted contracts@The second|Confusing a right with an obligation@And the third"
The first mistake is treating the quoted premium as the total contract cost, and forgetting the multiplier. The second is ignoring adjusted contracts, where the deliverable isn't the standard one hundred shares. And the third is confusing a right with an obligation.

@chapter Try it
@words text="Side · type · strike · premium · quantity"
To finish, take one contract line: side, type, strike, premium and quantity. Say the right or obligation, the cash that moves at the open, and the P and L at expiration for a given price. Do it before the decoder shows you, and without anyone handing you the multiplier.

@words text="A simplified model" sub="European Black–Scholes · 4.5% rate · no dividends"
One note on the numbers. The lesson's theoretical values come from a simplified model, with a fixed four point five percent rate and no dividends. Real listed products, early exercise, fees and market conditions can produce different prices and outcomes.

@end text="Decode a contract line yourself"
You can pick a side and a type, and watch the dollars move, on Learn. That's learn dot get er done dot I O.
