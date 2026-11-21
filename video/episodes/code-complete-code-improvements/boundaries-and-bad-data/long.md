---
format: long
lesson: code-complete-code-improvements/boundaries-and-bad-data
title: Boundary testing: why bugs live at the edges
thumb: Below, on, above
---

@chapter The question
@title text="Boundaries and Bad Data" sub="Code Complete, chapter 22" art=thumb
Once your basis tests have made every decision go both ways, what's left to test? The second half of chapter twenty two answers: the data.

@quote text="You can generate many test cases deterministically by using basis testing, data-flow analysis, boundary analysis, classes of bad data, and classes of good data." cite="McConnell, Code Complete, 2nd ed., Chapter 22, p. 533"
That's the chapter's summary. You can generate many test cases deterministically by using basis testing, data flow analysis, boundary analysis, classes of bad data, and classes of good data.

@chapter Data flow and classes
@art define-use
Data use is at least as error prone as control flow. The book adds Boris Beizer's estimate that at least half of all code is data declarations and initialisations. A variable is defined, used, and sometimes killed. Data flow testing adds a case for each pairing of a place a variable is set with a place that value's used.

@art equivalence-buckets
Equivalence partitioning says two tests that flush out the same errors needn't both be run. So each class of inputs a routine treats alike needs one test.

@chapter Boundaries
@words text="Error guessing" sub="test where experience says errors are"
Error guessing is a lowbrow name, the book says, for a sensible idea. Test where your experience says errors are. And the most fruitful place is the boundary, where off by one errors live, like greater than or equal written where greater than was meant.

@art boundary-ticks
So boundary analysis tests each boundary three times. Just below it, on it, and just above it. For a range from a low value to a high one, that's three at each end. On integers, six tests.

@math heading="Valid order: 1 to 99 items" items="0 · 1 · 2@zero, one, two;;98 · 99 · 100@ninety eight"
Take an order of one to ninety nine items. The boundary tests are zero, one, two, and ninety eight, ninety nine, a hundred.

@chapter Which test catches it
@math heading="Three checks" items="qty >= 1 && qty <= 99:  no difference@at least one;;qty > 0 && qty < 99:  wrong at 99@less than ninety nine;;qty <= 99:  wrong at 0 and below@at most ninety nine"
The lab tries three checks. Quantity at least one and at most ninety nine is right, and agrees everywhere. Quantity above zero and less than ninety nine refuses ninety nine, the largest valid order. And quantity at most ninety nine, with no lower check, accepts zero and every negative.

@art typical-passes
Now try a typical order of fifty. It passes all three checks. Only the boundary tests tell the right check from the two wrong ones. Ninety nine exposes the strict top, and zero exposes the missing lower check.

@chapter Bad data and good data
@art bad-data
Boundaries can also be compound, involving several variables at once. Two large numbers multiplied together, or every string at its longest. And beyond the edges, there's data a routine should refuse or survive.

@list heading="Classes of data" items="Too little data, or none@too little|Too much@too much|The wrong kind or size@wrong kind|Uninitialised data@never initialised|Nominal, smallest and largest normal@good data"
Then come the classes of bad data. Too little data, too much, the wrong kind or the wrong size, and data never initialised. And classes of good data, from the nominal case to the smallest and largest normal configurations.

@words text="Choose values you can check by hand"
A practical aside. Choose test values you can check by hand. An ugly number is no more likely to find an error than a round one in the same class, and much more likely to spoil your arithmetic.

@chapter Where errors cluster
@art error-cluster
Errors aren't spread evenly. The book reports about eighty percent are found in twenty percent of a project's classes or routines, and about half in five percent. Construction causes at least thirty five percent of all defects, and about three quarters on small projects.

@words text="Test data has errors too" sub="your own records beat anyone's averages"
It also warns that error taxonomies disagree wildly between studies, and that test data is often as likely to contain errors as the code it tests. Your own records are worth more than anyone's averages. And regression testing, the book says, is only practical when it's automated.

@chapter Where people slip
@list heading="Common slips" items="One typical value per case is enough@The first|Testing only with good data@The second|Expecting errors spread evenly@the third"
The first slip is thinking one typical value per case is enough. A class's errors are at its edges. The second is testing only with good data, when bad data is a class of tests of its own. And the third is expecting errors to be spread evenly, when they cluster.

@chapter Try it
@code block=1 lines=1-5 label=Java focus="1@eight to sixty four|4@the check"
Your turn. A password must be eight to sixty four characters long. Write the six boundary tests for that range, say what the check returns for each, and name each test it gets wrong.

@end text="Test the edges"
You can type the check into the boundaries lab with the range's ends, on Learn. That's learn dot get er done dot I O.
