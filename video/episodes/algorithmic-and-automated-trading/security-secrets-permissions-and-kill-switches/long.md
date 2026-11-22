---
format: long
lesson: algorithmic-and-automated-trading/security-secrets-permissions-and-kill-switches
title: Broker keys, least privilege and a kill switch that actually works
thumb: A key is authority
---

@chapter The problem
@title text="Security, Secrets, Permissions, and Kill Switches" sub="Algorithmic and Automated Trading" art=thumb
Somewhere in your trading system there's a broker key. Whoever holds it can place orders in your account. Not suggest them, place them. That's worth sitting with for a moment.

@art leaked-key
Broker credentials are direct authority to create financial actions. The market may be balanced, bullish or bearish. Compromised credentials can submit orders unrelated to any valid market condition. No signal, no risk check and no backtest protects you from a key that's in the wrong hands, or a service holding more authority than it needs.

@chapter Three ideas
@list heading="What to understand" items="Least privilege@Least privilege|Secret lifecycle@Secret lifecycle|Kill switch@kill switch"
Three ideas. Least privilege: grant only the account, environment, symbol, strategy and action permissions that are needed. Secret lifecycle: store secrets centrally, inject them at runtime, audit their use, rotate and revoke them, and never put them in code. And a kill switch: immediately stop new orders, cancel eligible open orders, and enter a controlled state.

@art secret-store
Where should a broker secret live? In a managed secret store. Not in a configuration file anyone can read. And never in source control, where it's copied to every clone and every backup. A secret there isn't stored, it's published. Never log secrets either.

@chapter Least privilege
@art scoped-keys
A paper trading service should have no live order permission at all. A paper service that can reach live has the blast radius of a live one. And sharing one unrestricted key across every service means one leak everywhere, with no way to tell which service used it.

@list heading="Secure the authority path" items="Protect: managed, revocable credentials@Protect|Restrict: separate read, paper and live@Restrict|Stop: test the switch and revocation@Stop"
Every identity that can request, approve or submit an order needs explicit scope. Protect: use managed secret storage, and short lived or revocable credentials where supported. Restrict: separate read, paper and live execution permissions. Stop: test kill switches, revocation and incident procedures regularly.

@art environments-separate
In practice that means separate credentials for development, paper and live. And no write access for read only analytics, which is one of the lesson's named mistakes.

@chapter The kill switch
@art kill-switch
A kill switch should be independent, fast, tested and audited. Not a hidden code edit, which needs the right person, a working deploy and time, none of which are guaranteed during an incident. Not available only after the close, either. It has to stop new risk when the normal pipeline is unreliable.

@words text="Independent of the failing service"
That's why designing a kill switch that depends on the failing strategy service is a named mistake. If the strategy is what's broken, the switch can't live inside it.

@chapter Counting the damage
@math heading="Broad key · ~6 unintended orders a minute" items="untested switch, 15 min: 6 × 15 = 90 orders@ninety;;tested switch, 2 min: 6 × 2 = 12 orders@twelve;;scoped key, 1 a minute, 2 min: 2 orders@two"
Here's the lesson's example. A broad permission key can submit about six unintended orders a minute. The kill switch is defined but untested, and it takes fifteen minutes to find and throw. Six times fifteen is ninety unintended orders. Tested, the same switch takes two minutes, and the number is twelve. Scoped down to one order a minute, it's two.

@art damage-shrinks
Each control cuts the damage. Testing the switch shrinks the time. Scoping the key shrinks the rate. Together they take ninety down to two. Neither one needed the strategy to be right about the market. Security controls work by limiting what can go wrong, not by predicting it.

@chapter Where people slip
@list heading="Common mistakes" items="One live key shared across services@The first|Write access for read-only analytics@The second|A kill switch inside the failing service@And the third"
The first mistake is sharing one live key across all services. The second is granting write access to read only analytics. And the third is designing a kill switch that depends on the failing strategy service. Test your switches and your credential revocation, before you need them.

@chapter Try it
@words text="Storage · scope · isolation · exposure · switch coverage"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the secret storage, permission scope, environment isolation, network exposure and kill switch coverage. Watch the residual risk change with each control you add.

@end text="Shrink the blast radius"
You can change each control and watch the residual risk, on Learn. That's learn dot get er done dot I O.
