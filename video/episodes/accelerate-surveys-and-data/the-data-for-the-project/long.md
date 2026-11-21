---
format: long
lesson: accelerate-surveys-and-data/the-data-for-the-project
title: Who Accelerate asked: snowball sampling and its limits
thumb: The seeds shape the snowball
---

@chapter Who was asked?
@title text="The Data for the Project" sub="Accelerate, Chapter 15" art=thumb
Chapter fourteen made the case for asking people. Chapter fifteen answers the next question: who did the authors actually ask? There's no list of everyone who builds and runs software, so they needed a method that works without one.

@quote text="Snowball sampling is a method well suited for studying specific groups whose populations cannot be easily identified." cite="Forsgren, Humble and Kim, Accelerate, Chapter 15"
Here's the method, in their words. Snowball sampling is a method well suited for studying specific groups whose populations cannot be easily identified.

@chapter The target population
@art target-circle
The research began in twenty fourteen, cross sectional, one point in time each year, for four years. The target was people and organizations that knew the word DevOps, or would at least open an invitation that used it. That focused the survey on people delivering software, who already knew terms like continuous integration.

@words text="Tight focus · limited comparisons"
The chapter states the trade off. People unfamiliar with these practices probably perform worse than the authors' lowest performers, so the comparisons don't show how large a change could be. In return, a tight definition buys explanatory power. And they asked about practices, like whether automated tests run on check in, not whether a team did continuous integration.

@chapter No list, no random sample
@art no-list
Probability sampling needs every member of the population known, with an equal chance of being asked. No list of the world's DevOps professionals exists. So the authors emailed their own lists, Puppet's marketing databases, their readers, and professional groups, with care to reach underrepresented groups. They posted on social media. Then they asked recipients to refer others.

@list heading="Why snowball sampling fitted" items="The population is hard to identify@hard or impossible|The population is averse to being studied@averse"
That's snowball sampling, and it fitted for two reasons. The population is hard or impossible to identify: no certifying body, and titles that vary. And it's often averse to being studied, after studies that led to workforce cuts.

@art vouch-chain
A referral lets a colleague vouch for the questions and the researchers, so the invitation arrives from someone you trust.

@list heading="Three limitations, and the remedies" items="First invitees may not represent their communities@first may not|The sample is shaped by the first invitations@shaped|Findings may not represent the industry@industry"
The authors name three limitations. The people invited first may not represent their communities. The sample is strongly shaped by those first invitations. And the findings may not represent the industry. The remedies: an initial set as large and diverse as possible, outside experts reviewing hypotheses, the literature, and the community's input.

@chapter Three seeds
@art snowball-tree
Now twenty invented people. A person with no referrer is a seed. The preset three-seeds has three: ana from retail, bo from a bank, and cy from health.

@math heading="Preset three-seeds, 20 people" items="ana's tree: 8 of 20 = 40%@forty percent;;bo's tree: 9 of 20 = 45%@forty five percent;;cy's tree: 3 of 20 = 15%@fifteen percent;;bank 45% · retail 30% · health 15% · startup 10%@by community"
Ana's tree holds eight of the twenty, forty percent. Bo's holds nine, forty five percent. Cy's holds three, fifteen percent. And by community, the sample is forty five percent bank, thirty percent retail, fifteen percent health and ten percent startup.

@chapter Six seeds
@art six-seeds
Now six seeds across the same four communities, again twenty people. No seed's tree holds more than five, a quarter. The shares are twenty five percent retail, twenty five bank, thirty health and twenty startup. Same size, different picture. More varied invitations changed it, not a bigger sample.

@chapter A missing seed
@math heading="Preset without-cy" items="lost: cy, ida, quin → 17 left@seventeen;;health: 0@no one;;bank: 45% → 52.9%@fifty two point nine;;retail: 30% → 35.3%@thirty five point three"
Drop cy, as if the health list had never been used. Cy, ida and quin are lost, leaving seventeen, and health has no one left. Bank rises from forty five to fifty two point nine percent, and retail from thirty to thirty five point three, though nobody was added. The denominator changed.

@art lost-branch
These are shares of the sample. With no list, nobody can say what the population's shares are, and the lab records only who answered, not who was asked and didn't.

@chapter Where people slip
@list heading="Common slips" items="A big snowball is a random sample@random|Size makes the first invitations irrelevant@irrelevant|The target population was hidden@hid"
Three slips. Treating a large snowball sample as a random sample of the industry. Believing a big sample makes the first invitations irrelevant. And reading the target population as something the authors hid. They stated it openly, with its cost.

@chapter Try it
@words text="a, b: seeds · c, d ← a · e ← b · f, g ← c · h ← e" sub="east: a c d f g · west: b e h"
Your turn. Eight people. a and b are seeds. a referred c and d, b referred e, c referred f and g, and e referred h. a's tree is east, b's is west. Count the waves and the shares. Then drop seed b and say what happens to the west.

@end text="Count who a seed reaches"
Type the records into the lab, on Learn. That's learn dot get er done dot I O.
