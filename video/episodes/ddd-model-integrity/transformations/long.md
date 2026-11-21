---
format: long
lesson: ddd-model-integrity/transformations
title: Transformations: changing how contexts relate, one step at a time
thumb: Merge through a kernel
---

@chapter Decisions aren't final
@title text="Transformations" sub="Domain-Driven Design, Chapter 14" art=thumb
Decisions about contexts can be revisited, and often must be. Breaking a context up is fairly easy, Evans says. Merging contexts, or changing their relationship, is hard.

@quote text="These transformations are usually much too big to be taken in a single refactoring or possibly even in a single project iteration." cite="Evans, Domain-Driven Design, Chapter 14"
These transformations are usually much too big to be taken in a single refactoring or possibly even in a single project iteration.

@art merge-steps
So each of his four game plans is a series of manageable steps. He presents them as guidelines to adapt to your situation, not procedures to follow.

@chapter Separate Ways to a Shared Kernel
@art process-first
The first plan merges separate contexts into a Shared Kernel. Even if the goal is one context, go through a kernel. Check each context is unified inside first. Then set up the process before any shared code: how code is shared, how modules are named, at least weekly integration, and a test suite, which, being empty, is easy to pass at first.

@art first-subdomain
Choose a small subdomain duplicated in both, generic rather than core, ideally one already translated, so the translation is proven and thins as you go. Two to four developers from both teams work out its model in detail, with basic tests. Each team integrates, and translations no longer needed are removed. Then repeat.

@list heading="Three ways to merge" items="Adopt one model wholesale@wholesale|Take pieces from each@pieces|Find a deeper model@deeper"
For the merge itself, there are three approaches. Adopt one context's model wholesale. Take pieces from each, careful not to make a jumble. Or find a new model, deeper than both. And defer merging parts tailored to different users' jargons until a deep model can replace both.

@chapter Kernel to one context
@art circulate-people
From kernel to Continuous Integration is a change of people and language, as much as of code. Make each team's integration practices alike. Circulate people between the teams. Distil each model. Then merge the core domains into the kernel, quickly once begun, and raise integration to daily, then continuous.

@chapter Legacy and languages
@art legacy-shrink
Phasing out a legacy system starts with a testing strategy. Each iteration, pick functions one iteration can move, add what the anticorruption layer needs, deploy, then remove the parts of the layer and the legacy modules no longer used. The layer will shrink and swell. Other things equal, move first what makes it smaller.

@words text="Open Host → Published Language" sub="keep the language apart from the host's model"
And to turn an open host service into a published language, use an industry standard if one exists. Otherwise, sharpen the host's core into an interchange language, publish it, build translators and switch over. It has to be stable, so keep it apart from the host's model.

@words text="Contexts don't cure complexity"
The chapter ends with a warning. Sometimes a large model seems too complex, so it's cut into pieces, and integration is lost. If a large context is feasible apart from its complexity, look first to the next two chapters: distillation, and large scale structure.

@chapter Before and after
@code block=1 lines=1-4 focus="1@share a kernel|2@conforms|3@through a layer|4@finance"
Now the count. A theatre box office, and the membership scheme that went its separate way years ago. Marketing conforms to the box office and translates membership's data through a layer. Finance translates the box office's. After the first step, box office and membership share a kernel. The box office changes its model of a sale.

@math heading="one box office change" items="before:  1 model · 1 translator · 1 untouched@Before;;after:  2 models · 2 translators · 0 untouched@after the first step"
Before, it reaches one model, marketing, one translator, finance's, and leaves membership untouched. After the first step, it reaches two models, membership and marketing, and two translators, finance's and marketing's layer for membership. Nothing is untouched.

@art kernel-promise
The merger makes a change reach further, and that's not a defect. A kernel is a promise to change together, and it ties two contexts' releases. What the count doesn't show is what the merger bought: the duplicated concepts gone, and translation no longer needed.

@chapter Where people slip
@list heading="Common slips" items="Merging in one step@The first|Starting the kernel with the core@The second|Expecting the layer to shrink steadily@And the third"
The first slip is merging two contexts in one step. The second is starting the kernel with the Core Domain. The first merger sets up the process, so start simple. And the third is expecting the anticorruption layer to shrink steadily as legacy goes. It shrinks and swells.

@chapter Try it
@code block=2 lines=1-2 focus="1-2@When tickets changes"
Your turn. Suppose the plan runs to its end. Box office and membership are one context, tickets, under Continuous Integration, and marketing's layer for membership is gone. When tickets changes, find the models that must change and the translators to update, and compare with before and after.

@end text="Small steps, process first"
Check it in the lab, on Learn. That's learn dot get er done dot I O.
