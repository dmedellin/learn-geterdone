---
format: long
lesson: data-structures/arrays-linked-lists-and-the-cost-model
title: Arrays vs linked lists: which one is actually cheaper?
thumb: The workload decides
---

@chapter The question
@title text="Arrays, Linked Lists, and the Cost Model" sub="Data Structures" art=thumb
An array and a linked list can both hold a sequence. Same operations, same answers. So which one is cheaper? The honest answer is that it depends, and by the end you'll know exactly on what.

@words text="What it does ≠ what it costs"
An abstract data type tells you what the operations are. It says nothing about what they cost. The cost belongs to the representation, and these two representations disagree about almost everything.

@chapter The cost model
@list heading="Word-RAM: what costs 1" items="Read or write a word at a known address@read or write|Arithmetic on a word@arithmetic|Nothing else is charged@nothing else"
First we need a ruler. In the word RAM model, memory is an array of words. A read or write at a known address costs one, arithmetic costs one, and nothing else is charged. There's no cache and no notion of one address being nearer than another.

@art array-index
So indexing an array costs one. The address is computed from i, and you jump straight there.

@art list-walk
A linked list can't do that. The only way to the i-th node is through the ones before it, so reaching it costs i plus one.

@chapter Two price lists
@math heading="Dynamic array" items="index i:  1@index costs one;;insert front:  n + 1@n plus one;;insert end:  1@the end costs one;;delete at i:  n − i@n minus i"
Here's the dynamic array. Index costs one. Insert at the front costs n plus one, because every element shifts up a place and then the new one is written. Insert at the end costs one, and delete at position i costs n minus i, for the elements that shift down.

@art array-shift
That's the array's whole story. Finding a position is free. Making room is what it pays for.

@math heading="Doubly-linked list" items="index i:  i + 1@i plus one;;insert front:  1@just one;;insert end:  1@at the end;;delete at i:  i + 2@i plus two"
Now the doubly linked list. Index costs i plus one. Insert at the front costs just one, since two pointers change. Insert at the end is one too, and delete at i costs i plus two: i plus one to arrive, and one splice.

@art list-splice
So the list is the mirror image. Making room is cheap. Arriving is what it pays for.

@chapter One run, counted
@words text="n = 8: insert at front" sub="array 9 · list 1"
With eight elements, inserting at the front costs the array nine and the list one. That's the most quoted comparison in the subject. And it's where the mistake starts, because the next operation in a real sequence is usually a lookup.

@math heading="16 operations from n = 16" items="index ×4:  array 4,  list 38@index;;insert front ×4:  array 74,  list 4@front;;insert end ×4:  array 4,  list 4@the end;;delete middle ×4:  array 40,  list 46@the middle;;total:  array 122,  list 92@In total"
So run a real mix. Index, insert at the front, insert at the end, and delete from the middle, four times each, from sixteen elements. Indexing: four against thirty eight. The front: seventy four against four. The end: four and four. The middle: forty against forty six. In total, a hundred and twenty two against ninety two.

@words text="Find the row with the biggest gap" sub="front inserts: a gap of 70 in a contest settled by 30"
The list wins. But look at why. The front insertions alone have a gap of seventy, in a contest settled by thirty. The rest is noise. That's how to read any cost comparison: find the row with the biggest gap.

@chapter The verdict flips
@art two-scales
Now change nothing but the mix. Three front insertions and one index, four times over from twenty four: the array costs three hundred and seventy, the list seventy eight. Three indexes and one insert at the end: the array costs sixteen, the list two hundred and fifty.

@words text="A workload decides" sub="the representation doesn't win or lose"
Same structures, same model. A factor of nearly five one way, and fifteen the other. The representation doesn't win or lose. A workload decides.

@chapter Where people slip
@list heading="Common slips" items="Calling list insertion constant time@The first|Picking a sequence that suits one side@The second|Treating a measured total as a bound@And the third"
The first slip is calling list insertion constant time. The splice is constant, but arriving isn't. The second is comparing on a sequence chosen to suit one side, which is an advertisement, not an analysis. And the third is treating a measured total as a bound.

@art array-regrow
That last one hides even in the table. Insert at the end on an array is written as one, but when the spare room runs out, every element is copied. The one is an amortised cost, an average over a run of insertions. A hundred and twenty two and ninety two are facts about sixteen operations, not a bound.

@chapter Try it
@words text="Three indexes + one end insert, ×4" sub="from n = 24: array 16 · list 250"
Your turn. Take the cost table and work out why three indexes and one insert at the end give sixteen against two hundred and fifty. Then name the row that decided it.

@end text="Run both counters yourself"
You can type your own sequence and watch both counters climb, on Learn. That's learn dot get er done dot I O.
