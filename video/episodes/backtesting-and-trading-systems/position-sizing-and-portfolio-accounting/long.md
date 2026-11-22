---
format: long
lesson: backtesting-and-trading-systems/position-sizing-and-portfolio-accounting
title: Position sizing in a backtest: could you actually afford that trade?
thumb: Could you fund it then?
---

@chapter The problem
@title text="Position Sizing and Portfolio Accounting" sub="Backtesting and Trading Systems" art=thumb
Test one trade at a time and every signal gets taken. But a real account has one pile of cash. On a strong day, several good signals can arrive together, and the account can't hold them all.

@words text="Could each position be funded when it opened?"
That's the lesson's standard. A portfolio backtest must prove that each position could be funded at the time it was opened. Cash, risk limits and shared exposure decide which trades the account can actually hold.

@art signals-arrive-together
A test that opens every signal without checking cash can create impossible exposure. The simulated portfolio ends up spending capital it doesn't have. That isn't diversification, either. It concentrates the account in whatever signals happened to arrive together.

@chapter Three ideas
@list heading="What to understand" items="Sizing rule@sizing rule|Capital constraint@capital constraint|Portfolio state@portfolio state"
The lesson names three ideas. A sizing rule: fixed shares, fixed dollars, volatility sizing and fixed risk all create different exposures. A capital constraint: orders must respect available cash, leverage and reserved risk. And portfolio state: every fill updates quantity, cost basis, cash, equity and open risk.

@art sizing-methods
Those four sizing rules give four different positions from the same signal. Fixed shares ignores price. Fixed dollars ignores how far the stop is. Fixed risk sizes the position so that the loss at the stop is a set fraction of equity. Volatility sizing scales the position to how much the instrument tends to move. Same signal, four different exposures.

@chapter Fixed-risk sizing
@words text="quantity = affordable loss ÷ risk per share"
Here's how fixed risk works. Quantity is the loss you can afford, divided by the risk per share. So quantity changes whenever the stop distance or the equity changes. The symbol name, or the colours on the chart, have nothing to do with it.

@math heading="Equity $50,000 · risk 1% · entry $50.00 · stop $2.00 away" items="$50,000 × 1% = $500@five hundred dollars;;$500 ÷ $2.00 = 250 shares@two hundred and fifty shares;;250 × $50.00 = $12,500 notional@twelve thousand five hundred"
Let's do the lesson's example. Equity is fifty thousand dollars, risk per trade is one percent, and the stop is two dollars from a fifty dollar entry. One percent of fifty thousand is five hundred dollars. Five hundred divided by two is two hundred and fifty shares. And two hundred and fifty times fifty is twelve thousand five hundred dollars of notional.

@art risk-box
Notice the position is a quarter of the account, but the planned loss is only one percent. A thousand shares would spend the whole account. Five hundred shares would double the planned loss to two percent of equity.

@chapter Update the ledger
@list heading="After every event" items="Size from the capital or risk rule@Size|Validate cash, leverage, concentration, open risk@Validate|Account fills, fees, positions, cash, equity@account"
Portfolio state must be calculated in chronological order. For each event: size, by calculating quantity from the selected rule. Validate, by checking cash, leverage, concentration and open risk limits. Then account, by updating fills, fees, positions, cash and mark to market equity.

@art ledger-rows
Open positions matter here too. Unrealised profit and loss changes current equity and exposure right now, before the trade has an outcome. So the next trade's size depends on what the open ones are worth today.

@chapter Where people slip
@list heading="Common mistakes" items="Sizing from ending equity, not current equity@The first|Ignoring rejected orders@The second|Adding trade P/L without portfolio overlap@And the third"
The first mistake is sizing from ending equity instead of current equity, which uses money the account didn't have yet. The second is ignoring rejected orders. And the third is combining individual trade profits without the portfolio level overlap between them.

@art rejected-order
Rejected orders are results, not noise. When capital is limited, process signals in a documented order, and record which ones the account turned away. Apply the same sizing rule throughout each test.

@art cash-flow
It helps to picture the account as one pool of cash feeding every position. Each fill draws from it, each fee drains it a little, and each exit pours money back. If the pool can't cover an order at the moment it arrives, that order doesn't happen, however good the signal was.

@chapter Try it
@words text="Same signals · four sizing rules"
In the lesson's lab, which runs on deterministic synthetic educational data, apply different sizing methods to the same simultaneous signals. Watch the exposure, the rejected trades and the final equity change.

@end text="Size the same signals four ways"
You can size simultaneous signals and watch trades get rejected, on Learn. That's learn dot get er done dot I O.
