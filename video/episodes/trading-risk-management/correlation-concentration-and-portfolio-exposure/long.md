---
format: long
lesson: trading-risk-management/correlation-concentration-and-portfolio-exposure
title: Correlation and concentration: when three trades are really one
thumb: Count drivers, not tickers
---

@chapter The question
@title text="Correlation, Concentration, and Portfolio Exposure" sub="Trading Risk Management" art=thumb
You hold three positions in three different stocks. That sounds diversified. But if all three are long technology names, a single piece of bad sector news can hit them all at once. Are they three risks, or one?

@words text="Different tickers can fall together"
Different tickers can fall together when the same market factor controls them. Three bullish technology positions aren't three independent risks if they respond to the same index, sector, or macro event.

@chapter Concentration and correlation
@art concentration
Concentration is when a large share of equity or risk is committed to one asset, sector, direction, or event. It's having too much riding on one thing.

@art correlated-lines
Correlation is when positions tend to move together, especially during broad market stress. So three long semiconductor stocks are best viewed as potentially correlated exposure. They can respond to the same sector and market factors.

@words text="Not independent by default"
They're not fully independent by default. Three tickers in one sector answer to the same news, and independence is the assumption stress breaks first. And yes, there's portfolio risk. The question is whether they're three risks, or one.

@chapter Portfolio heat
@art heat
Portfolio heat is the combined planned loss across active positions, adjusted for overlapping exposure. It's total planned active risk: how much of your equity is exposed to active stops. Not unrealised profit, and not the number of symbols on your watchlist.

@chapter When the gap comes
@art sector-gap
Here's the lesson's example. Three positions, each with a four hundred dollar planned loss to its stop. Portfolio heat is twelve hundred dollars. Then a sector gap opens each of them two and a half stop distances below entry. What's the loss?

@math heading="3 positions · $400 each to the stop · gap 2.5 stop-distances" items="heat = 3 × $400 = $1,200@twelve hundred;;each: 2.5 × $400 = $1,000@a thousand dollars;;together: 3 × $1,000 = $3,000@three thousand"
Three positions at four hundred gives heat of twelve hundred. But each position loses two and a half times four hundred, a thousand dollars. And because all three share the driver, they lose it together. Three thousand dollars, two and a half times the heat.

@math heading="Not these" items="✗  $1,200: the heat, filled at the trigger@the heat;;✗  $2,000: a gap of 1.67 stop-distances@two thousand"
Twelve hundred is the heat, what the stops would have cost if they'd filled at the trigger. And two thousand would be a gap of about one point six seven stop distances. Here each position lost a thousand, all at once.

@words text="Slippage reserve: per position" sub="correlation cap: across positions"
A slippage reserve handles the gap per position. The multiple across positions is what a correlation cap limits.

@chapter Diversification's limits
@art broad-decline
Does diversification guarantee no loss? No. Diversification reduces the part of risk that's specific to one position. But a broad decline reaches all of them. And the count isn't the test. Ten positions with the same driver are one position ten times.

@words text="Reduces some risk · can't remove broad loss"
So diversification can reduce some concentration risk. It can't remove broad market loss. That's why the useful question isn't how many positions you hold. It's how many different things could hurt them.

@chapter Where people slip
@list heading="Common mistakes" items="Counting tickers instead of risk factors@The first|Assuming historical correlation is fixed@The second|Ignoring options on the same underlying@the third"
Three mistakes. The first is counting tickers instead of risk factors. The second is assuming historical correlation is fixed. Don't assume historical low correlation will hold during a shock. And the third is ignoring options exposure to the same underlying or index.

@list heading="Practical rules" items="Group by common risk driver@group positions|Cap directional and sector exposure@cap total|Stress correlations higher in shocks@stress correlations"
So group positions by common risk driver. Cap total directional and sector exposure. And stress correlations higher during market shocks.

@chapter Try it
@art groups
The lab's first step is to group shared drivers. Sector, index, currency, rate, volatility, and event dependencies. Sort your positions by what actually moves them, not by their names.

@list heading="Lab steps" items="Group shared drivers@group shared drivers|Stress positions together@stress positions together|Cap combined risk@cap combined risk"
Then the other steps follow. Group shared drivers. Stress positions together, as if the shock hits them all at once. And cap combined risk, reducing quantity or choosing fewer trades when exposures overlap.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, rework the gap example with four positions of three hundred dollars each, and a gap of two stop distances.

@end text="Three tickers, one driver?"
You can group and stress positions together in the lab, on Learn. That's learn dot get er done dot I O.
