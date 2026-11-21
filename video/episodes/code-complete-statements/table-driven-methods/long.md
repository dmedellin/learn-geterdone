---
format: long
lesson: code-complete-statements/table-driven-methods
title: Table-driven methods: put the logic in the data
thumb: Same key, two fees
---

@chapter The question
@title text="Table-Driven Methods" sub="Code Complete, chapter 18" art=thumb
When should a chain of tests become a table? Chapter eighteen's answer is that almost anything you can select with logic statements, you can select with a table instead.

@art chain-to-table
In simple cases the logic is easier. As the logic grows, the table gets more attractive. A routine that classifies characters with a long chain of comparisons can become one array lookup, indexed by the character. The program's knowledge then sits in its data, not in its tests.

@words text="How do you look it up? What do you store?"
Every table raises two questions. How do you look an entry up? And what do you store in it? That might be data, or in some languages, a routine to run.

@quote text="One key consideration in using a table is deciding how to access the table. You can access tables by using direct access, indexed access, or stair-step access." cite="McConnell, Code Complete, 2nd ed., Chapter 18, p. 430"
That's the second of the chapter's key points. One key consideration in using a table is deciding how to access the table. You can access tables by using direct access, indexed access, or stair step access.

@chapter Direct and indexed
@art direct-access
In direct access, the key leads straight to the entry. Days in a month by the month's number. Insurance rates by age. Where a key doesn't fit, you can fudge it. Duplicate entries so it does, or transform the key, and put that transformation in its own routine.

@art indexed-access
In indexed access, a large, mostly empty index maps the key to a position in a smaller main table. That saves space when the main entries are large, and it lets several indexes reach one table.

@chapter Stair steps
@art stair-steps
Stair step access is for entries that hold for ranges of keys. Store the upper end of each range, and search for the first one the key falls under. That's where the chapter's subtleties are. Watch the endpoints. Make sure keys at the top fall into the top range. And put the lookup in its own routine.

@code block=1 lines=1-11 label=Java focus="1@days below|2@fees|6@less than"
Here's the lesson's library. Nothing under seven days overdue, two under fourteen, five under thirty, ten under sixty, and twenty under three hundred and sixty five. As code, it's two arrays, the days below and the fees, and a loop that returns the first fee whose bound the key is less than.

@chapter One key, two fees
@math heading="20 days overdue" items="fee 5@pays five;;linear: 3 tests@three linear;;binary: 2 probes@two"
The lab looks keys up and counts. A book twenty days overdue pays five, after three linear tests. A binary search, testing the middle step and keeping the half where the answer lies, finds it in two.

@art endpoint-rule
Now sixty days. Under the rule below, sixty isn't below sixty, so the book falls to the last step. Under the rule at or below, sixty is at or below sixty, and it stops a step earlier.

@math heading="60 days overdue" items="below:  fee 20 · 5 tests · 3 probes@pays twenty;;at or below:  fee 10 · 4 tests · 3 probes@pays ten"
Below, it pays twenty, after five linear tests and three binary probes. At or below, it pays ten, after four tests and three probes. The table holds no logic, but the endpoint rule does. It's a decision about the library's policy, and the code has to state it.

@chapter When to halve
@art binary-halving
For a long table, consider a binary search. The lab's tax brackets are sixteen steps, a thousand wide, from zero percent up to seventy five. An income of fourteen thousand five hundred falls in the fifteenth, at seventy percent, after fifteen linear tests. Binary search takes four, and no key here takes more than five.

@words text="5 days: 1 linear test, 3 binary probes"
On a short table, though, binary search can lose. A book five days overdue needs one linear test, and three binary probes.

@chapter Where people slip
@list heading="Common slips" items="Thinking a table is just a faster if chain@The first|Assuming binary always beats linear@The second|Expecting a staircase to hold every key@the third"
The first slip is thinking a table is just a faster if chain. Speed's one reason, but the case is that knowledge moves into data, where it's easier to read and change. The second is assuming binary search always wins. And the third is expecting a stair step table to hold every key. That's direct access.

@chapter Try it
@code block=2 lines=1-3 label=Java focus="2@weight steps|3@prices"
Your turn. These two arrays are weight steps in kilograms and their prices. A parcel weighs five kilograms. What does it cost, and how many comparisons do linear and binary search make, under below and then at or below? And say what the two arrays leave unstated.

@end text="Climb the stairs yourself"
You can check both rules in the stairs lab, on Learn. That's learn dot get er done dot I O.
