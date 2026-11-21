---
format: long
lesson: code-complete-system-considerations/how-program-size-affects-construction
title: Why a bigger software project isn't just more of the same
thumb: Paths grow with the square
---

@chapter The question
@title text="How Program Size Affects Construction" sub="Code Complete, chapter 27" art=thumb
What happens when a project grows? The obvious answer is that everything grows with it. Chapter twenty seven argues the obvious answer is wrong.

@art ten-times
McConnell imagines a product whose next version is to be ten times the size. The effort, the errors, and the mix of work will each grow by a different, and larger, factor. A large project is a different kind of thing. And a team used to small ones can find its first large one getting out of hand.

@chapter Communication paths
@art team-web
Here's the first reason. One programmer has one path of communication, with the customer. Add people, and the paths don't add up. They multiply, because each new person may need to talk to everyone already there.

@math heading="Paths in a team of n" items="paths = n · (n − 1) / 2@n times n minus one;;2 → 1 · 3 → 3 · 4 → 6 · 5 → 10@two people;;10 people:  10 · 9 / 2 = 45@ten people"
Each pair of people is one path. That's n times n minus one, halved. Two people have one path, three have three, four have six, and five have ten. And ten people have ten times nine, halved, which is forty five.

@art documents
Every path is time spent talking, and a chance of being misunderstood. That's why large projects formalise communication in documents. Fifty people read and write documents, rather than talking in every combination.

@chapter Errors
@quote text="All other things being equal, a large project will have more errors per thousand lines of code than a small one." cite="McConnell, Code Complete, 2nd ed., Chapter 27, p. 659"
The second reason is errors. All other things being equal, a large project will have more errors per thousand lines of code than a small one.

@words text="Under 2K lines: 0–25 per KLOC · 512K and up: 4–100" sub="Table 27-1, after Jones"
As size grows, more errors come from requirements and design. Construction is about seventy five percent of the errors on small projects, and about fifty on larger ones. And density rises. Under two thousand lines, zero to twenty five errors per thousand lines. At five hundred and twelve thousand or more, four to a hundred.

@chapter Productivity
@art productivity-fall
Productivity falls. On small projects the biggest influence is the individual programmer's skill. As size grows, the team and its organisation matter more. The book's table gives two thousand to twenty five thousand lines per staff year at ten thousand lines, and seven hundred to ten thousand at a million.

@art work-shares
And the mix shifts. Construction takes up to sixty five percent of the time on a small project, about fifty on a medium one, and less again on a large one. Coding and unit testing grow roughly with size, while communication, planning, integration and system testing grow faster.

@chapter Three sizes
@math heading="The lab's three presets" items="3 people, 10K lines:  3 paths · 0–400 defects · 0.40–5 staff-years@three people;;10 people, 100K:  45 paths · 200–7,000 · 5–100@ten people;;50 people, 1,000K:  1,225 paths · 4,000–100,000 · 100 to about 1,429@fifty people"
The lab works the book's rows at three sizes. Three people on ten thousand lines: three paths, up to four hundred defects, point four to five staff years. Ten people on a hundred thousand: forty five paths. Fifty people on a million lines: one thousand two hundred and twenty five paths, and four thousand to a hundred thousand defects.

@words text="Team ×17 · paths ×400" sub="every productivity range: 10× wide or more"
The team grew about seventeenfold, and the paths about four hundredfold. But read the spread first. At every size the productivity range is at least ten times wide, so the staff years are too. The table's a snapshot of an industry, not a forecast for your project.

@chapter Methodology
@art light-to-heavy
Every team has a methodology, chosen or not. The book reports Boehm and Turner's advice that a light method scaled up tends to serve better than a heavy one pared down. The aim is a right weight method for the project in front of you.

@chapter Where people slip
@list heading="Common slips" items="Ten times larger is ten times the work@The first|Construction errors stop mattering@The second|Starting heavy and paring down@the third"
The first slip is thinking a ten times larger program is ten times the work. The second is thinking construction errors stop mattering on a large project. Half of a larger number is still a great many. And the third is starting from a heavy method and paring it down.

@chapter Try it
@words text="A team of 6 grows to 12"
Your turn. A team of six grows to twelve, and everyone may need to talk to everyone else. Compute the communication paths before and after, and how many times larger the second count is than the first.

@end text="Count a team's paths"
You can type each team size into the size lab to check, on Learn. That's learn dot get er done dot I O.
