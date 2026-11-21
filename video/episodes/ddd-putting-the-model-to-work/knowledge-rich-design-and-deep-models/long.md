---
format: long
lesson: ddd-putting-the-model-to-work/knowledge-rich-design-and-deep-models
title: Knowledge-Rich Design: give the business rule a name
thumb: The rule, as an object
---

@chapter Past the nouns
@title text="Knowledge-Rich Design" sub="Domain-Driven Design, Chapter 1" art=thumb
You've probably heard the advice: find the nouns in the requirements, and make each one a class. Evans says that's only half the job.

@quote text="Business activities and rules are as central to a domain as are the entities involved; any domain will have various categories of concepts." cite="Evans, Domain-Driven Design, Chapter 1"
Business activities and rules are as central to a domain as are the entities involved. Any domain will have various categories of concepts.

@art tangled-rules
And rules are where crunching gets hard, because they can contradict each other. Experts are rarely aware how much they reconcile and fill in with common sense. Software can't do that. So the rules have to be stated, completed, reconciled, or put out of scope, with the developers.

@chapter The hidden rule
@art overbooked-ship
Evans's example comes from shipping. The business deliberately accepts more bookings than a voyage can carry, because some always cancel. The requirements carry that rule as one short line.

@art buried-guard
The first code puts it as a guard clause in the booking method, a comparison against capacity times a factor. Evans has two objections. No business expert could read that code to check the rule. And a developer who isn't a business person would struggle to connect the requirement to it.

@art policy-object
So he moves the rule into its own policy class, which the booking method asks. He borrows the name from the Strategy pattern, but not to swap rules. The concept simply is a policy. The real gain is understanding: everyone had to see it as a business rule, not an obscure calculation.

@chapter A clinic's rule
@code block=1 lines=1-9 label=Java focus="3@load|4@more than thirty|5@not urgent"
Here's a rule of the lesson's own. A clinic's evening session is a hundred and eighty minutes, but it lets bookings run to a hundred and ninety-five, because a few patients never come. This first version buries it all in one condition: more than thirty minutes, or the load over the allowance, or not urgent with less than a day's notice.

@code block=2 lines=1-16 label=Java focus="3-5@fitsStandardSlot|6-8@withinAllowance|9-11@hasStanding|12-15@admits"
The second gives the rule a home, and its clauses names. fitsStandardSlot. withinAllowance. hasStanding. And admits, which joins them. A member of the clinic's staff could be walked through this, and the rule can be found by its name.

@chapter Clause by clause
@math heading="routine-booking" items="minutes ≤ 30: 15 ✓@fifteen;;load ≤ 195: 150 ✓@hundred and fifty;;urgent = yes ✗ · notice ≥ 1: 3 ✓@three days;;admitted@admitted"
The lab reads the rule as four clauses. On the routine booking, a fifteen minute request into a session that would hold a hundred and fifty, with three days' notice. Three clauses are true. Urgent is false, but its partner in the or holds, so the request is admitted.

@math heading="over-allowance" items="load ≤ 195: 205 ✗@two hundred and five;;notice ≥ 1 ✗, covered by urgent@covers;;refused on load ≤ 195@refused"
Now an urgent twenty minute request that would take the session to two hundred and five. The load clause is false, and so is notice, but urgency covers that. So it's refused, and the first false clause is the allowance.

@math heading="long-same-day" items="minutes ≤ 30: 45 ✗@forty-five;;urgent ✗ · notice ≥ 1 ✗@both halves;;refused on minutes ≤ 30@first"
And a forty-five minute request, no notice, not urgent, into a session at a hundred and ninety. Three clauses are false: the slot first, then both halves of the or.

@art named-refusal
The buried version gives the same answers. But each refusal there is one compound condition coming out true, with nothing to say which part did it. The policy says which part of the rule refused, in the clinic's own words.

@chapter Deep models
@art handover-chain
Evans goes further. Useful models seldom lie on the surface. On that shipping project, the model of cargo and itineraries worked, but the experts weren't satisfied. Months later the team saw that the business thought of shipping as a chain of handovers of responsibility, governed by documents like the bill of lading. Crunching is exploration.

@chapter Where people slip
@list heading="Common slips" items="It's in the code, so it's in the model@The first|Make every condition a policy@The second|Strategy means swappable rules@And the third"
The first slip is thinking a rule is in the model because it's in the code. The second is making every condition a policy object. Evans says plainly he doesn't recommend that for every detail. And the third is reading the Strategy name as a promise of interchangeable rules.

@chapter Try it
@words text="minutes=30 · load=196 · urgent=no · notice=2"
Your turn. A thirty minute request, into a session that would then hold a hundred and ninety-six, from a patient who isn't urgent and gave two days' notice. Take the four clauses in order. Is it admitted, and what's the first false clause?

@end text="Check the rule clause by clause"
Then type it into the lab and check, on Learn. That's learn dot get er done dot I O.
