---
format: long
lesson: intractability-and-approximation/numbers-as-gadgets
title: Subset sum is NP-hard, even though it has a dynamic programme
thumb: Digits that never carry
---

@chapter A reduction made of digits
@title text="Numbers as Gadgets, and Weak Hardness" sub="Intractability and Approximation" art=thumb
This reduction doesn't build a graph. It builds a list of numbers, digit by digit. And it explains why a problem with a table filling algorithm can still be NP hard.

@words text="subset sum" sub="is there a sublist adding to the target exactly?"
Subset sum gives a list of positive integers and a target, and asks whether some sublist adds up to the target exactly. The input is the digits of the numbers. Ten numbers of a thousand digits each is a large input.

@chapter The construction
@art digit-table
Use one column per variable and one per clause, in base ten. For each variable, make two numbers, one for true and one for false. Each has a one in its variable's column, and a one in every clause column its literal satisfies.

@list heading="Slack and target" items="Two slack numbers per clause: 1 and 2 in its column@two slack numbers|Target: 1 in every variable column@a one in every variable|Target: 4 in every clause column@a four in every clause"
For each clause, add two slack numbers, with a one and a two in that clause's column. The target has a one in every variable column, and a four in every clause column.

@chapter Why it works
@art columns-no-carry
Every column's digits add up to at most six across all the rows, and six is less than ten. So no column can ever carry into the next. That means hitting the target is hitting each column separately.

@list heading="Column by column" items="Variable column needs 1: pick exactly one of true or false@exactly one|Clause column needs 4: literals give 0 to 3, slack gives 0 to 3@the literals give|Unsatisfied clause: slack alone reaches only 3@only three"
A variable column needs exactly one, so you pick exactly one of true or false. That's an assignment. A clause column needs four. The literals give between zero and three, and the slack gives zero to three. If the clause is satisfied, one slack choice makes up the rest. If it isn't, the slack reaches only three. So target subsets are exactly satisfying assignments.

@chapter Two clauses
@math heading="(x₁ ∨ x₂) ∧ (¬x₁ ∨ x₂)" items="8 numbers of 4 digits,  target 1144@eight numbers;;column totals 2, 2, 5, 5,  base 10@column totals;;2 subsets  =  2 satisfying assignments@two subsets"
The lab loads x one or x two, and not x one or x two. That's eight numbers of four digits, and the target one one four four. The column totals are two, two, five and five, comfortably under ten. Two subsets hit the target, matching two satisfying assignments, and the map is a bijection.

@art subset-rows
Pick the rows, then add down each column. Nothing spills over.

@math heading="One subset" items="1001 + 0111 + 0010 + 0020 + 0002 = 1144@one thousand and one;;⟹  x₁ = F,  x₂ = T@x one false"
Here's one of them. x one false is one thousand and one. x two true is one one one. Then three slack numbers, ten, twenty and two. They add to one one four four, and read back as x one false, x two true.

@art two-routes
Beside the enumeration, the panel runs the dynamic programme on the same numbers, and requires both to agree. They share no code. Two exhaustive routes that agree is evidence.

@chapter Weakly NP-hard
@art table-explodes
But wait. Subset sum has a dynamic programme. Its table has one row per number, and one column per value up to the target. Doesn't that make it easy? No. That's polynomial in the target as a number, and exponential in its digits. Here the target has one digit per variable and per clause, so the table has about ten to the n plus m columns.

@words text="weakly NP-hard" sub="hard only when the numbers are large"
A problem that's NP hard, but has an algorithm polynomial in the numeric values, is weakly NP hard. Subset sum is the standard example.

@art small-vs-large
If it stays hard even when the numbers are bounded by a polynomial in the input length, it's strongly NP hard. Only weakly NP hard problems can have the approximation scheme coming later in this course, and that's no coincidence. The scheme works by making the numbers small enough for the table to fit.

@chapter Where people slip
@list heading="Common slips" items="Assuming no carry instead of computing it@The first|Reading the table as a contradiction@The second|Counting numbers instead of digits@And the third"
The first slip is assuming there's no carry, instead of adding the columns. A base that's too small still produces plausible numbers. The second is reading the dynamic programme as a contradiction. Say which quantity it's polynomial in. And the third is counting numbers instead of digits. The input length counts digits.

@end text="Digits that never carry"
Add up every column of the construction yourself, on Learn. That's learn dot get er done dot I O.
