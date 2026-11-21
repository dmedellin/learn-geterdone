---
format: long
lesson: accelerate-the-science/several-views-and-rogue-data
title: Validity, reliability, and the item that went with the wrong group
thumb: Find the stray item
---

@chapter Tests come first
@title text="Several Views, and a Safeguard Against Rogue Data" sub="Accelerate, Chapter 13" art=thumb
A construct's score is only worth reporting if its items behave. How would you know they belong together? And what do you do when some don't?

@quote text="Taken together, validity and reliability statistical tests confirm our measures. They come before any analysis." cite="Forsgren, Humble and Kim, Accelerate, Chapter 13"
In the authors' words. Taken together, validity and reliability statistical tests confirm our measures. They come before any analysis.

@chapter Three kinds of test
@list heading="Before any analysis" items="Convergent validity: related items are related@Convergent|Discriminant validity: unrelated items are unrelated@Discriminant|Reliability: people read the items alike@Reliability"
Three kinds of test. Convergent validity makes sure items that should be related are, so culture items really measure culture. Discriminant validity makes sure items that shouldn't be related aren't. Reliability, also called internal consistency, gives assurance that people read and interpret the items alike.

@art gate
They're an order of work. Constructs are confirmed first, and only those that pass go forward to the analyses on the rungs above. The model case is culture: seven items on the seven point scale, which passed and are, the authors say, statistically valid and reliable.

@chapter A rogue data alarm
@art alarm
The tests have a second use. A construct that passes today may not pass tomorrow. So the authors recommend retesting the good ones periodically, especially if you suspect the system or its environment has changed. A construct that fails after passing is a rogue data alarm: something about the data has changed.

@chapter One construct became two
@art split-in-two
Their example wasn't so well behaved. Five items asked how teams learn of failures: two about being told by people outside the automated process, like customers, and three about alerts and monitoring from systems. In a pilot with about twenty professionals, the items loaded together.

@list heading="In the larger data collection" items="Notice from outside the automated processes@outside|Notice from systems: proactive failure notification@proactive"
But in the final, larger collection the tests revealed two constructs. Notification from outside the automated processes, and notification from systems, which the authors call proactive failure notification. They found the second predictive of software delivery performance. One question would have hidden that where the notice comes from matters.

@chapter Read the matrix
@art matrix
Now the lab, in outline. Six invented items in two constructs. A one to A three measure confidence in releasing. B one to B three measure the burden of being on call. Each cell is the correlation of two items across the people who answered.

@math heading="Preset one-stray-item" items="first construct: (0.72 + 0.68 + 0.64) ÷ 3 = 0.68@nought point six eight;;second construct: (0.70 + 0.20 + 0.24) ÷ 3 = 0.38@nought point three eight;;across the two: 2.70 ÷ 9 = 0.3@nought point three"
The first construct's items average nought point six eight with each other. The second's only nought point three eight. And across the two constructs, the nine cross pairs average nought point three. The first holds together; the second doesn't.

@math heading="Item by item" items="A1: 0.7 with its own · 0.317 with the other@nought point seven;;B3: 0.22 with its own@nought point two two;;B3: 1.57 ÷ 3 ≈ 0.523 with the first construct@nought point five two three"
Item by item shows why. A one averages nought point seven with its own construct and about nought point three one seven with the other, a wide gap. But B three averages only nought point two two with its own, and about nought point five two three with the first construct. So the lab lists B three as the item that goes with the wrong group.

@art move-item
Move it where it belongs. With B three written into the first construct, that construct averages about nought point six oh two, and the average across the two falls to nought point one nine six two five. Nothing in the numbers changed. The items had been mislabelled.

@art magnifier
The lab is a picture of the test, not the test. Appendix C runs principal components with varimax rotation, asks for loadings above nought point six, and more. A stray item can hide in an average that looks fine.

@chapter Where people slip
@list heading="Common slips" items="One well-worded question is enough@well worded|Passed once means settled@passed once|Several views make you immune@immunity"
Three slips. Thinking one well worded question is enough. Treating a construct that passed once as settled: it's passing, not proven. And reading several views as immunity from a bad source. They make it harder to skew results, and easier to notice. Neither is a guarantee.

@chapter Try it
@words text="P1–P2 0.65 · P1–P3 0.60 · P2–P3 0.55 · Q1–Q2 0.60 · P3–Q1 0.60 · P3–Q2 0.65"
Your turn. Items P one to P three, and Q one and Q two. Within P the correlations are nought point six five, nought point six, and nought point five five. Q one with Q two is nought point six. P three goes nought point six and nought point six five with the Qs. The other cross pairs are low. Which item will the lab list?

@end text="Read the matrix item by item"
Check your table in the lab, on Learn. That's learn dot get er done dot I O.
