---
format: long
lesson: code-complete-high-quality-code/abstract-data-types-and-interfaces
title: One class, one abstraction: what a good interface shows
thumb: One class, one abstraction
---

@chapter The problem
@title text="Abstract Data Types and Interfaces" sub="Code Complete, chapter 6" art=thumb
You've probably met a class like this. An Employee whose fields are all public, because every caller needed one of them once, and it was quicker to open them up than to ask what the callers were doing.

@code block=1 lines=1-15 label=Java focus="2-6@all public|12-14@monthly pay"
Here it is. Five fields, all public. A constructor, and one routine that works out the monthly pay. Chapter six is about why this class gets hard to change, and its answer starts with an idea older than classes.

@chapter The abstract data type
@art font-example
An abstract data type is a collection of data, and the operations that work on it. McConnell's example is a font. Without one, code all over the program sets a size field to sixteen, leaving you to guess whether that's pixels or points, and turns bold on with a bit mask. With one, it just calls the font's own routine.

@list heading="What you get" items="Details hidden@details hidden|Changes stay local@change is limited|An interface that says what it means@says what it means|Real-world entities, not low-level ones@real world"
The benefits follow. Implementation details hidden. The effect of a change is limited. An interface that says what it means. And a program that works with real world entities, not low level ones. A class, he says, is an abstract data type plus inheritance and polymorphism.

@chapter A consistent abstraction
@quote text="Class interfaces should provide a consistent abstraction. Many problems arise from violating this single principle." cite="McConnell, Code Complete, 2nd ed., Chapter 6, p. 160"
That leads to one of the chapter's key points. Class interfaces should provide a consistent abstraction. Many problems arise from violating this single principle.

@art mixed-drawer
Each class should implement one abstract data type and no more. The book's bad examples include a class that runs a command stack, formats reports, prints them and initialises global data, all at once. And interfaces erode under maintenance, one convenient routine at a time. So ask whether each new public routine fits.

@art one-panel
What you want is a class whose public routines all serve one idea, at one consistent level of abstraction. Callers see a single clean panel, and nothing else.

@chapter Encapsulation
@art locked-box
Encapsulation is the stronger idea. Abstraction lets you ignore the details. Encapsulation stops you looking. Minimise accessibility, expose no member data, and keep implementation details out of the interface.

@art reaching-behind
And be wary of semantic violations: callers who rely on how the class happens to work, rather than what its interface promises. Skipping a call because another routine is known to do it, for example. A caller who reads the code to learn how to use a class is programming through its interface, not to it.

@chapter Count it
@code block=2 lines=1-20 label=Java focus="2-6@private|11-16@two public readers|17-19@private helper"
Here's the same data, private, and typed by what it means. A name, an address, a phone number, and money for the salary. There's a constructor, two public readers, and one private helper. Five fields, none public, four routines, three public.

@math heading="Three versions of one design" items="public-fields: 5 fields · 5 public · 2 routines · 2 public@public fields;;private-fields: 5 fields · 0 public · 4 routines · 3 public@private fields;;kitchen-sink: 9 fields · 2 public · 6 routines · 6 public@kitchen sink"
The lab counts all three versions. The public fields Employee has five fields, all five public, and two routines, both public. The private fields one has five fields, none public, four routines, three public. And the kitchen sink, a Kiosk class, has nine fields, two public, and six routines, all public.

@code block=3 lines=1-18 label=Java focus="2-3@two public fields|12-17@six public routines"
Nine is past the book's guideline of about seven fields, a reason to look. And the two public fields break the no public data rule outright. But the counts can't answer the real question. Do these six public routines present one abstraction? Read their names and decide.

@chapter Where people slip
@list heading="Common slips" items="A getter and setter for every field@The first|Taking private for hidden@The second|A class as a bag of data@the third"
The first slip is thinking a getter and setter for every field makes a good interface. Accessors can't turn six routines into one abstraction. The second is taking private for hidden. Private fields don't stop semantic violations. And the third is treating a class as a bag of data with routines, a class in name only.

@chapter Try it
@art grouped-routines
Your turn. Take the kiosk's six public routines and group them by the abstraction each serves. How many classes are hiding in there, and which routines go in each?

@code block=4 lines=1-11 label=Java focus="2-4@fields|6-10@distance"
Then do this Point. Give its fields, and its public fields, and say what a caller would need if x and y were made private. The distance routine already reads them, but what about everyone else?

@end text="Count what a class exposes"
You can paste a class into the lab and count what it exposes, on Learn. That's learn dot get er done dot I O.
