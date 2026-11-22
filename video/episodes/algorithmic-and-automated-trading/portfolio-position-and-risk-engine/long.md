---
format: long
lesson: algorithmic-and-automated-trading/portfolio-position-and-risk-engine
title: The risk engine: approve, resize or reject before the broker sees it
thumb: Risk the portfolio, not the order
---

@chapter The problem
@title text="Portfolio, Position, and Risk Engine" sub="Algorithmic and Automated Trading" art=thumb
Five strategies each send a perfectly reasonable buy. Each one, alone, is within its limits. Together, they can add up to one exposure you'd never have accepted.

@words text="Valid signals · unacceptable portfolio"
That's the lesson's starting point. Several individually valid signals can combine into one unacceptable portfolio exposure. Someone has to look at the whole account before any order goes out.

@art correlated-positions
And it's worse when positions are related. When buyers lift many correlated stocks together, separate long positions can behave like one large market bet. Apparent diversification can disappear when related instruments respond the same way to the same event.

@chapter Three ideas
@list heading="What to understand" items="Position state@position state|Risk budget@risk budget|Pre-trade decision@pre-trade decision"
Three ideas. Position state: track settled and unsettled quantity, average cost, open orders and available buying power. Risk budget: limit loss per trade, total open risk, gross exposure, net exposure and concentration. And the pre trade decision: approve, resize, or reject the proposed order, before it reaches the broker.

@art pending-orders
Notice open orders are in there. An order that's live at the broker can fill at any moment, and when it does, the exposure was already committed. Nothing cancels an order except an instruction or an expiry. So pending orders count in exposure calculations, because they may become positions.

@chapter An actionable answer
@art approve-resize-reject
The engine's output must be actionable and auditable. An explicit approval, a resize, or a rejection. Not a chart colour, which nothing downstream can act on. And not a price prediction. The engine judges whether a proposal fits the account, not where price is going.

@list heading="Risk the portfolio, not isolated orders" items="Reconcile positions, cash, orders, buying power@Reconcile|Evaluate incremental and resulting risk@Evaluate|Decide, with a recorded reason@Decide"
Every proposal is evaluated against current and pending exposure. Reconcile: load confirmed positions, cash, open orders and broker buying power. Evaluate: calculate the incremental risk, and the resulting portfolio risk. Decide: approve, resize or reject, with a recorded reason.

@chapter Sizing a proposal
@math heading="$50,000 account · 1% risk · entry $118 · stop $114" items="$50,000 × 1% = $500 at risk@five hundred dollars;;$500 ÷ ($118 − $114) = 125 shares@one hundred and twenty five;;125 × $118 = $14,750 notional@fourteen thousand;;= 29.5% of the account@twenty nine point five"
The lesson's example: a fifty thousand dollar account risks one percent, five hundred dollars. Entry one eighteen, stop one fourteen, so four dollars a share. Five hundred over four is one hundred and twenty five shares. Times a hundred and eighteen, that's fourteen thousand, seven hundred and fifty dollars of notional. That's twenty nine point five percent of the account.

@art risk-budget
And that's before any exposure cap is applied. The trade risks one percent, but it ties up almost thirty percent of the account. Sizing by the stop is a loss to survive, not a purchase to make. Five hundred shares would put two thousand dollars at risk, not five hundred.

@chapter Independent limits
@words text="Risk limits live outside strategy code"
The lesson asks for risk limits that are independent from strategy code. If the strategy can change its own limits, they aren't limits.

@art reconcile-first
And reconcile broker and internal positions before you size anything. If the engine's records say one thing and the broker's say another, every number that follows is built on the wrong account. Find the mismatch first, then size from what the account really holds.

@art shared-account
Every strategy shares one account. Letting each strategy assume it owns the full account is one of the lesson's named mistakes. Five strategies each sized against the whole fifty thousand would commit five times what's there.

@chapter Where people slip
@list heading="Common mistakes" items="Risk checks only after fills@The first|Correlated positions counted as independent@The second|Each strategy assuming the full account@And the third"
The first mistake is applying risk checks only after fills, when the exposure already exists. The second is counting correlated positions as independent, which looks like diversification right up until the event that moves them all together. And the third is letting each strategy assume it owns the full account.

@chapter Try it
@words text="Simultaneous signals · limits · correlation"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, process simultaneous signals under account, exposure, concentration, correlation and risk per trade limits. Watch which proposals are approved, resized, or rejected, and why.

@end text="Send five signals through one gate"
You can send simultaneous signals through the risk gate yourself, on Learn. That's learn dot get er done dot I O.
