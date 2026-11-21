---
format: long
lesson: arguments-and-validity/syllogisms-tested-by-venn-regions
title: Testing syllogisms with three circles, and why true parts prove nothing
thumb: Every picture, not one
---

@chapter Three terms
@title text="Syllogisms Tested by Venn Regions" sub="Arguments and Validity" art=thumb
All cats are mammals. All dogs are mammals. So all dogs are cats. Something's obviously gone wrong. But what, exactly? Three circles will show you.

@art three-terms
A categorical syllogism has two premises and a conclusion, over three terms. The minor term, S, is the conclusion's subject. The major term, P, is its predicate. And the middle term, M, appears in both premises, but not in the conclusion.

@words text="Mood + figure = form" sub="AAA · figure 1 to 4"
The mood is the three letters of the premises and conclusion, like A A A. The figure, one to four, says where M sits in the premises. Together they fix the form.

@chapter The test
@art eight-regions
Three circles divide the plane into eight regions. Each region is empty or occupied, so a pattern is one of two hundred and fifty six. The test keeps every pattern in which both premises hold, and checks the conclusion in each. Valid means the conclusion is true in every one.

@chapter Barbara
@math heading="Barbara" items="All M are P:  M outside P is empty@The first premise;;All S are M:  S outside M is empty@The second;;so S outside P is empty:  All S are P@so the region"
Here's Barbara. All M are P, all S are M, so all S are P. The first premise empties M outside P. The second empties S outside M. Anything in S outside P would be inside M, which the first forbids, or outside it, which the second forbids. So the region is empty in every allowed pattern.

@list heading="Four valid moods of figure one" items="Barbara: AAA@Barbara|Celarent: EAE@Celarent|Darii: AII@Darii|Ferio: EIO@Ferio"
Barbara is one of four valid moods in the first figure. Celarent: no M are P, all S are M, so no S are P. Darii and Ferio each have a particular minor premise, some S are M.

@art forced-into-p
In Darii, some S are M occupies a region inside S and M. All M are P empties the part of M outside P, so that occupied region has to be inside P. In Ferio, no M are P empties the part inside P, so it's forced outside.

@chapter Two that fail
@math heading="Cats, dogs and mammals" items="All cats are mammals:  P inside M@All cats;;All dogs are mammals:  S inside M@All dogs;;counterexample: dogs inside mammals, outside cats@outside the cats"
Back to the cats. Let S be dogs, P cats, and M mammals. All cats are mammals puts P inside M. All dogs are mammals puts S inside M. Nothing relates the two circles, so S can lie in M outside the cats. That's the undistributed middle, A A A in figure two.

@art illicit-major
The second failure is the illicit major. All M are P, no S are M, so no S are P. The conclusion makes a claim about every P, but the major premise tells you nothing about P outside M. Let S and P overlap outside M, and both premises hold while the conclusion fails.

@chapter Truth doesn't decide it
@art cats-dogs-fish
And truth in the world plays no part. No cats are fish. No dogs are fish. So no dogs are cats. All three are true, and the argument is invalid, because its form allows cats and dogs to overlap outside fish. A true conclusion is a coincidence of subject matter, and no evidence of form.

@chapter Where people slip
@list heading="Common slips" items="Calling it valid because all parts are true@The first|Drawing one picture and stopping@The second|Naming the form from the typed order@the third"
The first slip is calling a syllogism valid because its parts are all true. The second is drawing one picture and stopping. A diagram where everything holds is easy to draw for almost any syllogism, and proves nothing unless the conclusion holds in every picture. And the third is naming the form from the order the premises are typed. The major premise is the one with P, whichever line it's on.

@art one-picture
That's why the test keeps every allowed pattern, not one. And it's why the traditional rules, like the rule that the middle term must be distributed at least once, are just summaries of these region facts. They're quick when they apply, and opaque when they don't. Where a rule and the patterns seem to disagree, the patterns have the definition.

@chapter Try it
@words text="No M are P · All S are M" sub="∴ ?"
Here's one to try. From no M are P, and all S are M, what follows on the Boolean reading? Mark the emptied regions, check the possible conclusions, and name the mood.

@end text="Every pattern, checked"
You can run these syllogisms and see each counterexample region drawn, on Learn. That's learn dot get er done dot I O.
