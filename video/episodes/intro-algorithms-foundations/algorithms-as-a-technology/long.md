---
format: long
lesson: intro-algorithms-foundations/algorithms-as-a-technology
title: Why a slow computer with a better algorithm wins
thumb: Algorithms beat hardware
---

@chapter The question
@title text="Algorithms as a Technology" sub="Introduction to Algorithms, Chapter 1" art=thumb
Suppose you could buy a computer a thousand times faster than the one you have. Would the choice of algorithm still matter? Chapter one of Introduction to Algorithms says yes, and it proves it with arithmetic.

@chapter What an algorithm is
@art sorting-instance
An algorithm takes an input, runs a sequence of well defined steps, and delivers an output. The problem is stated separately, as which outputs are acceptable for which inputs. The running example is sorting: given n numbers, put them in nondecreasing order. One particular sequence to sort is called an instance.

@list heading="Correct means" items="Halts on every instance@halts on every instance|With a right answer@with a right answer"
An algorithm is correct if it halts on every instance, and halts with a right answer. Notice the word every. A procedure that passed the tests you tried hasn't been shown correct. A test can show a procedure is wrong, but showing it right needs an argument about all inputs.

@chapter Infinitely fast computers
@words text="Infinitely fast, memory free?" sub="You'd still need correctness"
The authors clear the ground with a question. If computers were infinitely fast and memory were free, would algorithms still be worth studying? Yes, because you'd still need to show your method halts with the right answer. But then you'd use whichever correct method was easiest to write.

@art growth-curves
Real computers are fast but finite. So time and space are limited, and efficiency decides how much you use. Insertion sort takes time roughly c one times n squared. Merge sort takes roughly c two times n log n. Insertion sort usually has the smaller constant.

@math heading="Where the difference lives" items="c₁ · n · n@c one times n times n;;c₂ · n · lg n@c two times n times log n;;n  vs  lg n@a factor of n"
Write them as c one times n times n, and c two times n times log n. Now the difference is a factor of n against a factor of log n. However small c one is, once n is large enough, that gap makes up for it.

@art crossover-point
So there's always a crossover, a size beyond which merge sort is faster, and stays faster.

@chapter Two machines
@art two-machines
The lesson makes this concrete with two machines sorting five million keys. Machine A runs five billion instructions a second, and its program costs three n squared. Machine B runs only twenty million a second, and its program costs sixty n log n.

@math heading="5 million keys" items="A: 3 · (5·10⁶)² / (5·10⁹) = 15,000 s@machine A;;over four hours@over four hours;;B: 60 · 5·10⁶ · lg(5·10⁶) / (2·10⁷) ≈ 333.8 s@machine B;;under six minutes@under six minutes"
For machine A, three times five million squared, over five billion, is fifteen thousand seconds. That's over four hours. For machine B, sixty times five million times log of five million, over twenty million, is about three hundred and thirty four seconds. That's under six minutes.

@words text="B wins by about 45×" sub="A: 250× faster machine, 20× leaner code"
Machine A is two hundred and fifty times faster, and its code is twenty times leaner. It still loses, by a factor of about forty five. And the ratio of the two times keeps growing as n grows.

@chapter The edges of the argument
@words text="Crossover: n = 81,580" sub="1,000 keys: A about 49.8× faster"
That doesn't mean the better order wins at every size. These two programs cross over at n equals eighty one thousand five hundred and eighty. At a thousand keys, machine A is about forty nine point eight times faster. The crossover depends on the programs and machines, not on the n you ask about.

@art exponential-wall
Two more cases show the edges. If both programs cost n log n, there's no crossover at all. The ratio is a constant, five thousand, so the faster machine wins for good. And if A costs two to the n while B costs a hundred n cubed, the crossover is n equals thirty. At sixty, A would need over seven years.

@chapter A technology like any other
@art algorithms-below
The chapter ends by putting algorithms beside fast hardware, graphical interfaces and networking. Even a program with no algorithms of its own leans on them everywhere underneath. The hardware was designed with them, the network routes with them, and the compiler is full of them.

@quote text="Total system performance depends on choosing efficient algorithms as much as on choosing fast hardware." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 1.2"
As the authors put it: total system performance depends on choosing efficient algorithms as much as on choosing fast hardware.

@chapter Common slips
@list heading="Common slips" items="Faster hardware can't fix a worse order of growth@The first|The better order doesn't win at every size@The second|Passing tests isn't correctness@the third"
The first slip is believing faster hardware can make up for a worse algorithm. The second is expecting the better order of growth to win at every size. And the third is calling a procedure correct because it passed its tests.

@chapter Try it
@math heading="Find the crossover" items="A: 4n² at 2 billion per second@four n squared;;B: 100 n lg n at 50 million per second@a hundred n log n;;try n = 2¹⁰, 2¹¹, 2¹², …@two to the ten"
Your turn. Program A costs four n squared, on a machine doing two billion a second. Program B costs a hundred n log n, at fifty million a second. Try two to the ten, two to the eleven, two to the twelve and so on, and find the least power of two where B wins.

@end text="Race two programs yourself"
You can race two programs of your own and find their crossover on Learn. That's learn dot get er done dot I O.
