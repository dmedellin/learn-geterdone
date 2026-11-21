---
format: long
lesson: linear-programming-models/decision-variables-objective-and-constraints
title: From a paragraph to a linear programme, in three questions
thumb: Decide, want, stop
---

@chapter The question
@title text="From a Situation to a Linear Program" sub="Linear Programming Models" art=thumb
A paragraph describes a workshop, and you want to know what it should make. Before any algebra, you need a model. And a model comes from three questions, asked in a fixed order.

@list heading="Three questions" items="What do I decide?@what do I decide|What do I want?@what do I want|What stops me?@what stops me"
What do I decide, what do I want, and what stops me. The first answer is a list of variables, each with a unit. The second is one linear expression in those variables. The third is one row for every limit.

@art three-lists
Why that order? Because the second and third answers are both written in terms of the first. Until you know your variables, there's nothing to write.

@chapter What linear means
@math heading="Linear or not" items="3C + 5T  ✓@three C plus five T;;3CT  ✗@three C T;;C²  ✗@C squared;;C / T  ✗@C over T"
A linear programme has an objective and finitely many constraints, all linear. Linear means every variable is multiplied by a constant and then added. Three C plus five T is linear. Three C T isn't, and neither is C squared, or C over T.

@chapter The workshop
@art workshop-shops
Here's the paragraph. A workshop makes chairs and tables. A chair takes one bench hour in carpentry and three hours on assembly. A table takes two hours in finishing and two on assembly.

@words text="4 bench · 12 finishing · 18 assembly" sub="chair £3 · table £5"
The week has four bench hours, twelve finishing hours and eighteen assembly hours. A chair earns three pounds and a table earns five.

@words text="C chairs, T tables" sub="units made this week"
The decisions are C, the chairs, and T, the tables, both counted in units made this week. Nothing else is a decision. The hours a chair takes belong to the product, and the hours available belong to the week.

@chapter The model
@math heading="The workshop" items="maximise 3C + 5T@maximise;;C ≤ 4@C is at most four;;2T ≤ 12@two T is at most twelve;;3C + 2T ≤ 18@three C plus two T;;C, T ≥ 0@both at least zero"
So you maximise three C plus five T, in pounds a week. Subject to: C is at most four, two T is at most twelve, three C plus two T is at most eighteen, and C and T both at least zero.

@art unit-check
Now read one row across and check its units. In carpentry, each chair uses one bench hour, so the left side is bench hours. The right side is four bench hours. They agree. It's the cheapest check there is that a row means what you think.

@chapter Testing a point
@math heading="Point (2, 6)" items="2 ≤ 4  ✓@two is at most four;;12 ≤ 12  ✓@twelve is at most twelve;;18 ≤ 18  ✓@eighteen is at most eighteen;;3·2 + 5·6 = 36@thirty six"
A model is worth solving once you can test a point by hand. Try two chairs and six tables. The rows read two is at most four, twelve is at most twelve, eighteen is at most eighteen. The signs hold, and the profit is thirty six.

@math heading="Point (4, 6)" items="3·4 + 5·6 = 42@forty two;;3·4 + 2·6 = 24 ≤ 18  ✗@twenty four;;over by 6 hours@over by six"
Now try four and six. The profit is forty two, which is bigger. But the assembly row reads twenty four, against eighteen. That's over by six hours. This isn't a worse plan. It isn't a plan at all, and it fails with a row's name attached.

@chapter Signs are rows too
@art sign-rows
Why is C at least zero a constraint, not just a convention? A workshop can't make minus two chairs, and the lab checks the sign restrictions in the same shape as every other row.

@art runaway-region
Drop the two sign restrictions and the region runs away to the south west. The model happily unmakes tables to free up assembly hours for chairs. Those two lines are two of the five things a point must satisfy.

@chapter Where people slip
@list heading="Common slips" items="Profit as a variable@The first|Dropping the sign restrictions@The second|Turning data into a decision@The third"
The first slip is making profit a variable, with a row saying P equals three C plus five T. It adds a letter and no information. Ask whether the number could be an instruction. Make two chairs is one. Earn thirty six pounds isn't. The second slip is dropping the sign restrictions. The third is promoting given data, like the eighteen assembly hours, into a decision.

@art target-row
A related move is writing a target as a row: three C plus five T at least five hundred. That's legal, but it's a different question. It asks whether five hundred can be reached, not what the best profit is.

@chapter Try it
@words text="Write three lists first" sub="decide · want · stop"
Take any small paragraph that describes a decision. Write the three lists separately before any algebra. Then pick a point, substitute it into every row, and name the row that fails, if one does.

@end text="Test a point against every row"
You can type a point and watch every row, sign restrictions included, give its verdict, on Learn. That's learn dot get er done dot I O.
