---
format: long
lesson: accelerate-technical-practices/version-control-and-test-automation
title: Version control, test automation and test data: what worked
thumb: Who writes the tests matters
---

@chapter What works
@title text="Version Control, Test Automation and Test Data" sub="Accelerate, Chapter 4" art=thumb
Which technical practices actually go with performance? Chapter four's section What Works and What Doesn't is full of nuances. Here are the first three practices: version control, test automation, and test data.

@chapter Version control
@art config-in-vc
On version control, the survey asked whether application code, system configuration, application configuration, and the scripts that automate build and configuration were all in it. Together, those predict performance, and form a key part of continuous delivery.

@quote text="keeping system and application configuration in version control was more highly correlated with software delivery performance than keeping application code in version control." cite="Forsgren, Humble and Kim, Accelerate, Chapter 4"
And here's the surprise. Keeping system and application configuration in version control was more highly correlated with software delivery performance than keeping application code in version control.

@words text="Configuration is not secondary"
Configuration is usually treated as secondary to code. The authors say the data shows that's a misconception.

@chapter Reliable tests
@art flaky-quarantine
Test automation gets the longest treatment. Tests only help if they're reliable. A pass should mean the software is releasable, and a failure should mean a real defect. Many suites are flaky, so the authors advise moving unreliable tests to a separate quarantine suite, or even deleting them, since version control keeps them.

@chapter Who writes them
@art developer-tests
The second finding is about who writes the tests. Teams where developers chiefly create and maintain the acceptance tests, and can reproduce and fix them on their own machines, did well.

@words text="Tests chiefly by QA or outsourced: not correlated with performance"
Where tests were chiefly made by a QA team or an outsourcing partner, the practice was not correlated with performance. Not negatively correlated. Just not correlated.

@list heading="The theory offered" items="Developers who write tests write testable code@easier to test|Developers who own tests maintain them@maintaining"
The theory is that developers who write tests write code that's easier to test, which is why test driven development matters. And developers who own the tests care about maintaining them.

@art testers-alongside
That's not an argument for dismissing testers. They do exploratory, usability and acceptance testing by hand, and help grow the automated suites alongside developers. Then run the tests often: every commit should trigger a build and some quick tests, developers should see a fuller acceptance and performance suite every day, and testers should get the current builds.

@chapter Test data
@art test-data
A test is only as good as the data it runs against. Without the right data, a fully automated suite can't run, and teams end up skipping the tests they most need.

@words text="Enough · on demand · never the limit"
Test data is the last of the three. Successful teams had enough test data to run their fully automated suites, could get it when they needed it, and found it didn't limit which tests they could run.

@chapter Times as likely
@math heading="Invented teams: who owns the tests" items="developers own: 28 / 40 = 70%@twenty eight of forty;;separate QA: 20 / 50 = 40%@twenty of fifty;;ratio: 70 / 40 = 1.75@one point seven five;;difference: 30 points@thirty points"
Now the count, with invented teams and a failed change goal they each set. Twenty eight of forty teams whose developers own the tests met it, seventy percent. Twenty of fifty with a separate QA team did, forty percent. The ratio is one point seven five, and the difference is thirty points.

@math heading="The odds ratio" items="odds: 28 / 12 = 7/3 · 20 / 30 = 2/3@seven thirds;;odds ratio: (7/3) ÷ (2/3) = 3.5@three point five"
Now the odds. Twenty eight to twelve is seven thirds. Twenty to thirty is two thirds. Their ratio is three point five, twice the one point seven five that answers how many times as likely. People mistake one for the other all the time.

@words text="config: 75% vs 50% → ratio 1.5 · odds ratio 3"
Same arithmetic on the configuration finding. Forty five of sixty teams with config in version control met the goal, seventy five percent, against twenty of forty without, fifty percent. Ratio one point five, odds ratio three.

@art confounder
These are invented counts. And the survey's finding is a correlation too. Teams with developer owned tests might differ in other ways, like being smaller or newer, which would also make the shares differ.

@chapter Where people slip
@list heading="Common slips" items="The book wants testers gone@The first|Configuration matters less than code@The second|A ratio is the effect of the practice@the third"
The first slip is concluding the book wants testers gone. The second is treating configuration as a lesser concern than code. And the third is reading a ratio of shares as the effect of the practice.

@chapter Try it
@words text="every commit: 20 of 25 · now and then: 10 of 25"
Your turn. Twenty of twenty five teams that test on every commit met the goal, against ten of twenty five that test now and then. Find each share, the ratio, the difference and the odds ratio. Which one answers how many times as likely?

@end text="Times as likely, or odds?"
You can type in two groups and compare all three numbers, on Learn. That's learn dot get er done dot I O.
