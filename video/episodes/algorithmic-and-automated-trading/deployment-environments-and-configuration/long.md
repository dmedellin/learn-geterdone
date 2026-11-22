---
format: long
lesson: algorithmic-and-automated-trading/deployment-environments-and-configuration
title: Deploying a trading system without betting the account on it
thumb: Small canary, fast rollback
---

@chapter The problem
@title text="Deployment, Environments, and Configuration" sub="Algorithmic and Automated Trading" art=thumb
You push a new version of your trading system. The market doesn't pause while you do it. If something's wrong, it's wrong with real orders, in a market that keeps moving.

@art volatility-burst
The lesson's warning is specific. During expanding volatility, a wrong position size setting, or a stale strategy version, can multiply losses before anyone notices the deployment was bad. So the question isn't only whether the new version works. It's how much damage a bad version could do before it's caught, and how quickly you can take it back.

@chapter Three ideas
@list heading="What to understand" items="Immutable artifact@Immutable artifact|External configuration@External configuration|Progressive rollout@Progressive rollout"
Three ideas. Immutable artifact: promote the same tested build through every environment, instead of rebuilding different code. External configuration: version the non secret strategy and environment settings separately from the binary. Progressive rollout: use paper, shadow, limited symbols, small size, canary instances, and fast rollback.

@art same-artifact
Why promote the same artifact? Because it reduces the differences between the code you tested and the code that runs live. Rebuilding can introduce dependency or source differences after testing. With one artifact, configuration is the only thing that can differ between environments.

@chapter Version everything
@art versioned-config
Code, strategy rules, configuration and schema should each have their own explicit version. Then when behaviour changes, you can say exactly which of them changed. Editing production parameters without an audit trail is a named mistake. So is using live credentials in development.

@list heading="Promote one verified change" items="Build and scan one reproducible artifact@Build|Verify: unit, integration, replay, paper, config@Verify|Promote gradually with gates and rollback@Promote"
The lesson's method. Build: create and scan one reproducible artifact. Verify: run unit, integration, replay, paper and configuration checks. Promote: deploy gradually, with health gates, monitoring and rollback criteria.

@art readiness-gate
Health gates include readiness. Readiness should become false when the service can't safely process new trading work, and an unready instance shouldn't receive any. A cosmetic change doesn't affect readiness. Being unable to take an order safely does.

@chapter The canary
@art canary-slice
A canary rollout limits the initial scope of a bad deployment. A small slice of the system gets the new version first. If it's bad, only that slice is hurt, and detection and rollback cost less. It won't prevent the strategy's ordinary losses once the deployment is good. It only bounds the deployment risk.

@math heading="Canary 10% · bad config −0.5% a minute · rollback 3 min" items="10% × 0.5% × 3 = 0.15% of the account@zero point one five;;full scope, 14-min manual rollback: 100% × 0.5% × 14 = 7%@seven percent"
The canary is ten percent of live capital. A bad configuration loses half a percent of the capital it controls, per minute. Automatic rollback takes three minutes. Ten percent, times half a percent, times three: zero point one five percent of the account. At full scope, with a fourteen minute manual rollback, the same bug costs seven percent.

@words text="Not 15% · not 1.5%"
Fifteen percent comes from multiplying the percentages as whole numbers. One point five percent is the canary's own loss, but the canary is a tenth of the account. So the account loses a tenth of that.

@chapter Where people slip
@list heading="Common mistakes" items="Live credentials in development@The first|Editing production parameters without audit@The second|Deploying everything at once@And the third"
The first mistake is using live credentials in development. The second is editing production parameters without an audit trail. And the third is deploying every strategy and symbol at the same time, which turns any bug into a whole account problem.

@art rollback
And plan the rollback before you need it. The lesson asks you to roll back without changing trading state unexpectedly. Going back to the old version mustn't forget the orders and positions the new one created. The code changes back. The trading state carries on, and the old version has to pick it up exactly where it stands.

@chapter Try it
@words text="Promotion · validation · canary · probes · rollback"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the artifact promotion, configuration validation, canary size, health probes and rollback behaviour. Then inject a bad configuration and see how far it gets before it's caught.

@end text="Inject a bad config, roll it back"
You can inject a bad configuration and watch the canary contain it, on Learn. That's learn dot get er done dot I O.
