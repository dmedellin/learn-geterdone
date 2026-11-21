---
format: long
lesson: code-complete-variables/named-constants-and-other-types
title: Be a fanatic about literals: named constants and other types
thumb: Name every literal but 0 and 1
---

@chapter The question
@title text="Named Constants and Other Types" sub="Code Complete, chapter 12" art=thumb
What's wrong with a number in the middle of your code? It hides what it means, and it hides where else it has to change. The second half of chapter twelve runs through several kinds of data, but its sharpest advice is about literals.

@quote text="Even if you think a literal is safe, use named constants instead. Be a fanatic about rooting out literals in your code." cite="McConnell, Code Complete, 2nd ed., Section 12.7, p. 309"
Here it is. Even if you think a literal is safe, use named constants instead. Be a fanatic about rooting out literals in your code.

@chapter Strings, booleans, enums
@art magic-string
Section twelve point four starts with characters and strings. Avoid magic ones. A literal string may need to change, may need translating, and says nothing about why it's there. A constant called escape is clearer than the character code it stands for.

@art boolean-sentence
Section twelve point five uses boolean variables to document a program. Assign each part of a complicated test to a boolean whose name says what it checks, and the if statement reads like a sentence.

@art enum-palette
Section twelve point six prefers enumerated types to schemes where one stands for red and two for green. They're more readable, they make parameters clear, and they let you check a value is one of the allowed ones. Java added enum in version five.

@chapter Named constants
@art single-dial
Section twelve point seven is the centre. A named constant puts something that might change where it can be changed once. McConnell calls this single point control. Use constants in declarations too, like the length of an array.

@art safe-bet
And avoid literals even when they seem safe. A loop to twelve is probably over months. But would you bet on it? A constant removes the doubt. Use each constant consistently, because a constant here and the same literal there is a change waiting to be missed.

@words text="Only 0 and 1 in the body"
The rule of thumb from section twelve point one is that the only literals in a program's body should be zero and one. This is where many readers part company with McConnell, over the two in a midpoint. His position is plain: name even the safe ones.

@chapter Count the magic numbers
@list heading="monthlyPayment, with literals" items="rate = 0.0725 / 12@point zero seven two five|months = years × 12@years times twelve|if months > 360, months = 360@three hundred and sixty"
Here's a routine that computes a monthly mortgage payment. The rate is point zero seven two five over twelve. The months are years times twelve. And if months is over three hundred and sixty, it's capped at three hundred and sixty.

@math heading="Magic numbers" items="0.0725 (line 2)@line two;;12 (lines 2, 3)@twelve on lines;;360 (lines 4, 5)@three sixty;;5 magic numbers · 3 distinct@five magic"
The lab counts every literal but zero and one. Point zero seven two five on line two. Twelve on lines two and three. Three sixty on lines four and five. That's five magic numbers, three distinct. The ones in one plus rate are part of the formula, and aren't counted.

@art repeated-literal
The two twelves mean the same thing, months in a year. The two three sixties mean the longest term. Change the term in one place, and you have to remember the other. And the single rate isn't repeated, but it still doesn't say it's an annual interest rate.

@code block=2 lines=1-10 label=Java focus="1-3@three constants|6@annual rate over months per year|7@min"
Now declare three constants at the top. The rate line becomes annual rate over months per year. And the cap on the term is one line, with min. The lab finds no magic numbers at all.

@words text="TWELVE would pass" sub="name it for what it stands for"
What the lab can't see is whether a name is good. A constant called TWELVE would pass, and tell you nothing the literal didn't. Name a constant for what it stands for, not its value.

@chapter Where people slip
@list heading="Common slips" items="A literal used once is harmless@The first|Naming a constant after its value@The second|Overlooking magic strings@the third"
The first slip is thinking a literal used only once is harmless. It still doesn't say what it means. The second is naming a constant after its value. And the third is overlooking magic strings and characters, which deserve names just as much.

@chapter Try it
@code block=3 lines=1-10 label=Java focus="4@temperature|5@raises an alert|8@then sleeps"
Your turn. This loop watches the patients on a ward. It checks each temperature, raises an alert, then sleeps. List every magic number with its line, say how many are distinct, and write a static final declaration with a good name for each.

@end text="Root out the literals"
You can paste a routine into the lab and list its magic numbers, on Learn. That's learn dot get er done dot I O.
