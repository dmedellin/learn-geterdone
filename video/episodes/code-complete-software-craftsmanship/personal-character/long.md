---
format: long
lesson: code-complete-software-craftsmanship/personal-character
title: What makes a great programmer? Character, not talent
thumb: Lazy, if it pays
---

@chapter The question
@title text="Personal Character" sub="Code Complete, chapter 33" art=thumb
Is a programmer's character off the topic of a book on construction? McConnell's answer is no. In software, the building material is the programmer's intellect, and the main tool is the programmer. So studying the tool means studying people.

@art unsupervised
Programming is close to unsupervisable. Nobody else really knows what you're working on, and an employer often can't judge whether you're good. If you want to be great, it's up to you.

@words text="Differences of about 10 to 1" sub="Sackman, Erikson and Grant, 1968, and later studies"
And the room to improve is large. The book reports differences of the order of ten to one among programmers, in the time to write and debug a program, and the size, speed and error rate of the result. Those are other people's measurements.

@quote text="The characteristics of a superior programmer have almost nothing to do with talent and everything to do with a commitment to personal development." cite="McConnell, Code Complete, 2nd ed., Chapter 33, p. 835"
That character matters more than intelligence is McConnell's own claim. The characteristics of a superior programmer have almost nothing to do with talent and everything to do with a commitment to personal development.

@chapter Humility and curiosity
@art small-skull
Intelligence first. In his nineteen seventy two Turing Award lecture, The Humble Programmer, Dijkstra argued that most of programming makes up for the strictly limited size of our skulls. Short routines, reviews, tests and conventions all lighten the load. The humble programmer who leans on them makes fewer errors than the clever one who refuses them.

@list heading="Curiosity" items="Learn how you develop software@how you develop|Experiment with a short program@experiment|Analyse before you act@analyse|Study good programmers' work@good programmers"
Curiosity is next. Learn how you develop software. Experiment with a short program when you're unsure how a feature works. Analyse before you act. And study the work of good programmers.

@chapter Honesty
@art honest-estimate
Intellectual honesty means admitting mistakes, understanding a compiler warning rather than suppressing it, and giving realistic estimates. Bert lets his manager talk his estimate down, and he'll lose credibility when the project takes as long as it takes. An estimate can be revised to be more accurate, but not negotiated.

@words text="Conventions free creativity" sub="in the areas that don't matter, for the ones that do"
Communication comes down to writing code for the person who must change it. And creativity and discipline aren't opposed. Conventions in the areas that don't matter free your creativity for the ones that do.

@chapter Three kinds of laziness
@list heading="Laziness" items="Putting it off: true laziness@putting off|Doing it at once: enlightened@at once|Writing a tool: long-term laziness@writing a tool"
Then laziness, in three kinds. Putting off an unpleasant task is true laziness, and hardly ever helps. Doing it at once to get it over with is the enlightened kind. And the third is writing a tool so you never do it again.

@art tool-loop
That's long term laziness, the most productive kind, McConnell says, provided the tool ends up saving time.

@chapter Does the tool pay?
@math heading="The lesson's model" items="runs to pay back = build minutes ÷ minutes saved per run@build time;;weeks = runs ÷ runs per week@runs per week"
That proviso is a sum. The chapter gives no formula, so the lab's model is the lesson's own. Runs to pay back is the build time in minutes, divided by the saving per run, rounded up. Weeks to pay back is those runs, divided by runs per week.

@math heading="Weekly report" items="15 min → 1 min, 10 a week · 8 hours to build@fifteen minutes;;480 ÷ 14 → 35 runs · 3.5 weeks@thirty five runs;;first year: about 113.33 hours saved@a hundred and thirteen"
A report takes fifteen minutes by hand, ten times a week. A script takes eight hours to write, and one minute to run. Each run saves fourteen minutes, so it pays back in thirty five runs, three and a half weeks. In the first year, it saves about a hundred and thirteen hours.

@art payback-curve
Now take the same eight hours to automate a thirty minute job, cut to two minutes, that comes round once every four weeks. It needs eighteen runs, and at that rate eighteen runs take seventy two weeks. The first year ends about two hours down.

@words text="40 hours to build · 53.4 weeks to pay back"
And a big tool, forty hours to save nine minutes on a task done five times a week, takes fifty three point four weeks, and its first year ends an hour down. The model leaves out upkeep, errors avoided and what you learn. But it's honesty, applied to your own enthusiasm for a tool.

@chapter Traits that matter less
@art all-nighter
Some traits matter less than you'd think. Persistence is mostly stubbornness when you're stuck. Ten years of experience can be one year's experience ten times. And all night heroics install defects that take weeks to remove. You become a good programmer, after Aristotle, by programming well.

@chapter Where people slip
@list heading="Common slips" items="Automating a task always saves time@The first|Intelligence makes a programmer good@The second|Years of experience as skill@the third"
The first slip is thinking automating a task always saves time. Do the arithmetic first. The second is thinking intelligence is what makes a programmer good. And the third is counting years of experience as skill, when what counts is reflecting and learning.

@chapter Try it
@words text="2 hours to build · saves 5 minutes · 5 times a week"
Your turn. A script takes two hours to write, and saves a five minute task every working day, five times a week. Compute the runs to pay back, the weeks to pay back, and the hours saved in the first year of fifty two weeks.

@end text="Check a tool's payback"
You can enter the four figures in the payback lab to check, on Learn. That's learn dot get er done dot I O.
