---
format: long
lesson: paradoxes-and-their-exits/thomsons-lamp-and-supertasks
title: Thomson's lamp: on or off at the end of the minute?
thumb: No last switch
---

@chapter The lamp
@title text="Thomson's Lamp and Supertasks" sub="Paradoxes and Their Exits" art=thumb
A lamp starts off. After half a minute, it's switched on. After a further quarter, it's switched off. After a further eighth, on again. Each switch comes after half the time that remains. At the end of the minute, is the lamp on, or off?

@list heading="Thomson's argument" items="Each switch changes the state@changes state|Infinitely many switches, all before the minute ends@infinitely many|At the end, it's on or off@on or off|It can't be on, and it can't be off@can't be on|So it's neither@neither"
At each switch, the lamp changes state. There are infinitely many switches, all over before the minute is up. At the end, the lamp is on or off. It can't be on, since every time it was switched on, it was later switched off. And it can't be off, by the same argument reversed. So it's neither.

@art lamp-flicker
That ends where no one can stay, a lamp that's neither on nor off. Thomson concluded that the setup is impossible, which denies the second premise. But first, look at what the setup does and doesn't fix.

@chapter Two sequences
@math heading="Switch n" items="time:  1 − 1/2ⁿ@the nth switch;;after 10 switches:  1023/1024,  off@ten switches;;after 11 switches:  2047/2048,  on@eleven"
The switches happen at the partial sums of the halves, so the nth switch is at one minus one over two to the n of the minute. After ten switches, that's one thousand and twenty three over one thousand and twenty four, and the lamp is off. After eleven, it's two thousand and forty seven over two thousand and forty eight, and the lamp is on.

@art two-sequences
The times converge to one, the end of the minute. But the states don't approach anything. On, off, on, off. Odd gives on, even gives off. So there's a limit time, and no limit state.

@chapter Premise four
@art no-last-switch
Now look at premise four. The setup gives a state for every moment before the end of the minute. It gives none for the end itself, because that moment isn't the time of any switch. And there's no last switch. Every switch has a successor.

@art minute-dial
A rule about how the state changes at each step, applied to every step, says nothing about what follows all of them. Every time it was switched on, it was later switched off, is true of every moment before the minute, and silent about the minute itself. Premise four reads the rule as if it fixed a state there.

@chapter Two exits
@art silent-moment
The standard reply is exit one, against premise four. The story is consistent. Its description before the minute is complete, and doesn't mention the end. A rule like, the lamp is on at the end, would be a further stipulation, and either choice is consistent. The price is a story that describes every moment but one, and owes nothing about that one.

@art impossible-switch
The case against that reply has force too. A physical lamp has a state at every moment. A reader who finds the silence unacceptable concludes, with Thomson, that the story describes nothing possible. That's exit one too, against premise two. Its price is saying which law forbids a body to be switched this way.

@words text="The series fixes the time, not the state" sub="the lesson's narrower claim"
The two replies deny different premises, and pay different prices. The lesson's claim is the narrower one the lab can check. The series fixes the time, and not the state.

@chapter Where people slip
@list heading="Common slips" items="Thinking a convergent series has a last action@The first|Reading the state as the limit of the states@The second|Counting silence as a contradiction@And the third"
The first slip is thinking a convergent series of actions has a last action. It doesn't. The end comes after all the switches, and is the time of none. The second is reading the state as the limit of the states. Importing a limit from the times to the states is what makes the question look answerable. And the third is counting silence as a contradiction.

@chapter Try it
@words text="30 switches" sub="within a billionth of the minute"
Move the lab's slider one step at a time, and watch the state alternate while the time creeps toward one. Then try thirty switches. The time is within a billionth of the minute, and the state is still one of two. Say which premise you'd deny, and its price.

@end text="Switch by switch"
You can switch the lamp step by step yourself, on Learn. That's learn dot get er done dot I O.
