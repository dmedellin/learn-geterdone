---
format: long
lesson: lines-functions-and-graphs/point-slope-and-standard-form
title: Point-slope and standard form: building a line from what you know
thumb: One point, one slope, done
---

@chapter The problem
@title text="Point-Slope and Standard Form" sub="Lines, Functions and Graphs" art=thumb
You know one point on a line, and you know its slope. How do you write down its equation? With point slope form, you just write it. No solving at all.

@art point-and-slope
The point fixes where the line is. The slope fixes which way it points. Together they pin down exactly one line.

@words text="y − y₁ = m(x − x₁)" sub="through (x₁, y₁), slope m"
The line through the point x one, y one, with slope m, is y minus y one equals m times x minus x one.

@chapter Where it comes from
@art general-point
It isn't a new fact to memorise. Take any other point x, y on the line. The slope from x one, y one to x, y has to be m. So y minus y one, over x minus x one, equals m.

@math items="(y − y₁)/(x − x₁) = m@Multiply both sides;;y − y₁ = m(x − x₁)@that's the form"
Multiply both sides by x minus x one, and that's the form. As a bonus, multiplying up lets in the point x one, y one itself, which the fraction had to leave out.

@words text="through (−2, 1):  y − 1 = m(x + 2)"
The derivation also explains the minus signs. The form subtracts x one, so a negative coordinate gives a double negative. Through minus two, one, you get y minus one equals m times x minus minus two, which is x plus two.

@chapter From two points
@math heading="(−2, 1) and (4, 10)" items="m = (10 − 1)/(4 − (−2)) = 9/6 = 3/2@slope first;;y − 1 = (3/2)(x + 2)@minus two, one;;y − 1 = (3/2)x + 3@distribute;;y = (3/2)x + 4@add one"
Two points is the usual start. Find the slope first: nine over six, three halves. Then use either point. With minus two, one, you get y minus one equals three halves times x plus two. Distribute, to get three halves x plus three. Then add one: y equals three halves x plus four.

@math heading="using (4, 10) instead" items="y − 10 = (3/2)(x − 4)@four, ten;;y − 10 = (3/2)x − 6@minus six;;y = (3/2)x + 4@the same line"
Start from four, ten instead. y minus ten equals three halves times x minus four. That's three halves x minus six. Add ten, and you get y equals three halves x plus four. It's the same line.

@art two-routes
So either point works. If your answer looks different from a printed one, put both into slope intercept form and compare. That form is unique for a given line, so it settles the question.

@chapter Standard form
@words text="Ax + By = C" sub="integers · A positive"
The other form is standard form. A x plus B y equals C, with A, B and C whole numbers, A and B not both zero. By convention, you clear fractions and make A positive.

@math heading="y = (3/2)x + 4" items="2y = 3x + 8@multiply by two;;−3x + 2y = 8@move the x term;;3x − 2y = −8@negate"
To convert, multiply by two to get two y equals three x plus eight. Move the x term across, minus three x plus two y equals eight. Then negate everything so A is positive: three x minus two y equals minus eight.

@math heading="check both points" items="(−2, 1):  −6 − 2 = −8  ✓@minus two, one;;(4, 10):  12 − 20 = −8  ✓@four, ten"
Now check both points. Minus two, one gives minus six minus two, minus eight. True. Four, ten gives twelve minus twenty, minus eight. True. And four, ten was never used after the slope, so that's real evidence.

@art vertical-line
Standard form is the only one of the three that handles every line. x equals five is one x plus zero y equals five. Point slope needs a slope, and slope intercept needs to solve for y, so both fail on vertical lines.

@chapter Which form, when
@art three-forms
None of these forms replaces the others. Given a point and a slope, or two points, reach for point slope. For a question about shape, steepness or comparing lines, use slope intercept. For intercepts, or a system you'll solve by elimination, use standard form.

@chapter Where people slip
@list heading="Common slips" items="Dropping the built-in minus signs@The first|Distributing over only the first term@The second|Treating standard form as unique@the third"
The first slip is dropping the minus signs built into the form, so x plus two becomes x minus two. The second is distributing over only the first term. And the third is treating standard form as unique.

@art same-line-twice
Three x minus two y equals minus eight, and six x minus four y equals minus sixteen, are the same line. So compare lines in slope intercept form instead.

@chapter Try it
@words text="(−3, 5) and (1, −3)" sub="slope given: m = −2"
Try this pair: minus three, five, and one, minus three. The slope is given, minus two. Build point slope form from minus three, five. Convert it to slope intercept and standard form. Then use one, minus three as your check.

@end text="Build the line yourself"
The full lesson, with every step worked, is on Learn. That's learn dot get er done dot I O.
