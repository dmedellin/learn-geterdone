---
format: long
lesson: ddd-patterns-and-refactoring/posting-rules
title: Posting Rules: the model hiding in a nightly batch
thumb: Entries from entries
---

@chapter A model inside the plumbing
@title text="Posting Rules and the Nightly Batch" sub="Domain-Driven Design, Chapter 11" art=thumb
Chapter eleven's second example begins where the first ended. With accounts and entries in place, the developer adapting the nightly batch starts to recognise its behaviour in concepts from Fowler's book.

@art batch-plumbing
Evans makes a general point of it. Some parts of a program grew one step at a time, and look like application plumbing, not domain logic. An analysis pattern can show you that a model has been hiding there all along.

@chapter The posting rule
@art two-views
Accounting systems often hold several views of the same money. One account tracks an amount, and another tracks something worked out from it. If the second has to follow the first automatically, the code for the two gets intertwined. Where most entries come from such rules, that code becomes a mess.

@art rule-object
So the first step is to make each rule an object. A new entry in its input account triggers it. It computes an amount by its calculation method. And it posts the result to its output account.

@chapter When rules fire
@list heading="Three firing modes" items="Eager: the moment an entry is posted@Eager firing|Account-based: when an account is told@Account based|Posting-rule-based: an outside agent says when@Posting rule based"
The harder part is timing. Fowler names three answers. Eager firing runs every rule the moment an entry is posted. It's obvious, and usually the least practical. Account based firing waits until an account is told to process its new entries. And posting rule based firing leaves it to an outside agent, which tells each rule to fire.

@words text="One clear point of initiation"
The modes can be mixed, but each set of rules needs one clear point of initiation. And Evans counts the three names as part of the pattern. In the Ubiquitous Language they make a hidden decision visible.

@art batch-loop
In the book, the developers choose posting rule based firing. Eager firing would suit the interest charges the batch creates, but not payments entered during the day. The batch shrinks to a loop that sends each asset a few plain messages and commits.

@chapter Keep the concept
@quote text="When you use a term from a well-known analysis pattern, take care to keep the basic concept it designates intact, however much the superficial form might change." cite="Evans, Domain-Driven Design, Chapter 11"
They departed from Fowler's details, and kept the concept. That's the one change Evans advises against breaking. When you use a term from a well known analysis pattern, take care to keep the basic concept it designates intact, however much the superficial form might change.

@words text="Change the meaning, change the name" sub="a pattern is a set of model parts, not a framework"
That way the Ubiquitous Language gains a term others already know. If the meaning drifts as the model evolves, change the name too. And remember, an analysis pattern isn't a framework. It's a set of parts for a model, aimed at the hardest decisions.

@chapter A theatre's takings
@code block=1 lines=11-19 focus="12@entries since|13-14@rounded to the cent|15-16@its negative"
Now the lab, on a theatre's takings. When the batch says fire, the rule finds its input entries since it last ran. It multiplies each by its share, rounded to the cent, posts that to the output, and posts its negative to the input.

@math heading="levy-and-commission" items="0.05 × 412.50 = 20.625 → 20.63@twenty point six two five;;0.05 × 96.30 = 4.815 → 4.82@four point eight one five;;0.12 × 180.00 = 21.60@twelve per cent;;ticket-income: 508.80 − 25.45 = 483.35@four eighty three"
The trust sets aside five per cent of ticket income for restoration. Five per cent of four hundred and twelve fifty is twenty point six two five, which rounds to twenty sixty three. Of ninety six thirty, four point eight one five, rounding to four eighty two. And an agency keeps twelve per cent of one eighty, twenty one sixty. Ticket income ends at four eighty three thirty five.

@math heading="rounding left" items="each pair nets to zero@nets to zero;;−0.005 − 0.005 = −0.01@a cent"
Each derived pair nets to zero, so the rules move money and never make it. But each share rounded up by half a cent. So the rounding left is minus a cent, one the fund holds that five per cent doesn't strictly give it.

@art derived-no-fire
Add a donation of two hundred straight to the fund, and a trust fee of ten per cent on what enters the fund. It fires once, on the donation, twenty to trust admin, and the fund is two hundred and five forty five. It doesn't fire on the levy's own entries, because the lab never lets a derived entry fire a rule.

@chapter Where people slip
@list heading="Common slips" items="Batch jobs as plumbing@The first|Keeping a name whose concept changed@The second|Leaving timing to the implementation@And the third"
The first slip is treating a batch job as plumbing with no model in it. The second is keeping a pattern's name for a concept that has changed. And the third is leaving the timing of derived updates to the implementation, when it belongs in the language.

@chapter Try it
@code block=2 lines=1-5 focus="1-2@two ticket entries|3@bar income|5@the rule"
Your turn: a matinee's takings, with two ticket entries, some bar income, and the restoration rule at five per cent. Write every entry the rule derives, rounding half away from zero. Then give ticket income's and the fund's balances after, and the rounding left.

@end text="Name the rule, name the timing"
Type the entries and the rule into the lab to check, on Learn. That's learn dot get er done dot I O.
