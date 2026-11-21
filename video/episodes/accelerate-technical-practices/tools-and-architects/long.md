---
format: long
lesson: accelerate-technical-practices/tools-and-architects
title: Let teams choose their tools, and what architects should ask
thumb: Who picks the tools?
---

@chapter Who should choose?
@title text="Allow Teams to Choose Their Own Tools" sub="Accelerate, Chapter 5" art=thumb
In many organizations, engineers must use tools from an approved list. Who should really choose? The last two sections of chapter five take up that question, and what architects should do instead.

@quote text="What tools or technologies you use is irrelevant if the people who must use them hate using them" cite="Forsgren, Humble and Kim, Accelerate, Chapter 5"
The authors put it bluntly. What tools or technologies you use is irrelevant if the people who must use them hate using them. And the tools must also achieve the outcomes you want.

@list heading="Reasons for an approved list" items="A simpler environment@simpler environment|Skills to manage it@skills|Buying power with vendors@buying power|Correct licences@licences"
They give the usual reasons for an approved list fairly: a simpler environment, the skills to manage the technology through its life, more buying power with vendors, and correct licences.

@chapter The finding
@art approved-list
The cost is that a fixed list stops teams choosing what suits their work, and from trying new approaches. In their analysis, teams deciding for themselves contributes to software delivery performance, and through it to organizational performance.

@words text="Tool choice: a driver of continuous delivery" sub="added in the 2017 analysis"
They find that unsurprising: the people who build and run systems choose on what serves their work and their users. It's the second of the two capabilities the twenty seventeen analysis added to the drivers of continuous delivery.

@chapter Room for standards
@art standard-platform
But they don't argue against standards. Some belong, especially in how infrastructure is architected and configured. They cite Steve Yegge's account of Amazon, which noted that debugging another team's code is nearly impossible without one standard way to run each service in a sandbox you can debug.

@art paved-road
On security, teams that build it into their work do better at continuous delivery. A key element is that security teams supply approved libraries, packages and toolchains that are easy to use. Tools that make life easier get adopted freely, and the freedom to decline keeps internal tool builders honest.

@chapter What architects should ask
@list heading="The wrong questions" items="Microservices or serverless?@microservices or serverless|Which orchestrator?@orchestrator|Which CI server, which language?@which language"
Then the architects. Discussions of architecture fixate on microservices or serverless, which orchestrator, which CI server or which language. The authors' research says those are the wrong questions.

@words text="Can teams change their services without waiting on others?"
What matters is enabling teams to change their products and services without waiting on other teams or systems. And architects should work closely with the engineers who build and run them.

@chapter Counting teams
@art shared-library
Now the count. An invented system has seven services and four teams. Three ties are real couplings inside a team's own area. Three more come from a shared library whose new version must be adopted at the same time by billing, signup, reports and the gateway.

@math heading="Preset lockstep" items="billing–invoices · billing–signup · signup–referrals@billing ties;;signup–reports · reports–export · reports–gateway@signup ties;;one group of 7 · none alone · 4 teams coordinate@four teams"
Follow the ties. Billing ties to invoices and signup. Signup ties to referrals and reports. Reports ties to export and the gateway. That's one group of all seven services, none deployable alone, and four teams that must coordinate every release.

@math heading="Remove signup–reports" items="billing, invoices, signup, referrals: 4 services, 2 teams@four services;;reports, export, gateway: 3 services, 2 teams@three services"
Now suppose signup and reports could take the new library at different times, say through a compatibility shim. Remove that tie, and the group splits: four services owned by two teams, and three services owned by two others.

@art team-pairs
So all four teams still coordinate, but now in pairs. Each group needs fewer people to agree before anything ships.

@art pinned-versions
Pin the library by version instead, so each service upgrades when its own team chooses, and the three library ties vanish. Four groups, the largest of two, the gateway deployable alone, and no group spans more than one team.

@words text="A lock-step upgrade turns a local decision into a cross-team one"
That's the chapter's point meeting the release. But a standard platform also removes some choices. Whether it serves its users or only its owners is something to ask the engineers who use it.

@chapter Where people slip
@list heading="Common slips" items="There should be no standards@The first|An architect picks the best technology@The second|Mandating a tool because it's good@the third"
The first slip is reading the chapter as saying there should be no standards. The second is thinking an architect's job is to pick the best technology. And the third is mandating a tool because it's good. A forced tool hides whether it's usable.

@chapter Try it
@words text="web, api (shop) · search, index (find) · ads (growth)"
Your turn. Five services, three teams, and a shared library tying api and search. Find the release groups and the teams that must coordinate. Then remove the tie between api and search, and do it again.

@end text="Who has to agree before it ships?"
You can count the teams in a release in the lab, on Learn. That's learn dot get er done dot I O.
