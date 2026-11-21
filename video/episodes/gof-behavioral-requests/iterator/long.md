---
format: long
lesson: gof-behavioral-requests/iterator
title: Iterator: one tree, three orders, and who's in control
thumb: Walk it without looking inside
---

@chapter Taking the walk out
@title text="Iterator" sub="Design Patterns, chapter 5" art=thumb
You use iterators every day, in every for loop. But the pattern behind them asks two questions most people never think about: who controls the walk, and who decides the order. Let's take them in turn.

@quote text="The key idea in this pattern is to take the responsibility for access and traversal out of the list object and put it into an iterator object." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That sentence from the motivation is the whole pattern. The key idea is to take the responsibility for access and traversal out of the list object, and put it into an iterator object.

@art list-cursor
A list should let you reach its elements without showing how it keeps them. So an iterator keeps track of the current element, and offers operations to start, advance, test for the end, and read the current item.

@art two-walks
And because each iterator keeps its own state, you can walk one list in different ways, or twice at once, without adding an operation to the list for every kind of walk. Each list creates its own iterator through a factory method.

@chapter The pattern
@list heading="Three consequences" items="The walk can vary@can vary|The aggregate's interface stays small@stays small|Several walks at once@more than one"
The authors list three consequences, all benefits. The walk can vary, since replacing the iterator changes the order. The aggregate's own interface stays small. And more than one walk can be under way at once.

@code block=1 lines=1-18 label=Java focus="3@a stack|11@pops|13-15@the first child ends on top"
Here's the lesson's pre order iterator. It keeps a stack of pending parts. Next pops the top part, pushes its children in reverse, so the first child ends on top, and returns the part. Swap the stack for a queue, adding children at the back, and the same shape gives level order.

@chapter Who's in control
@code block=2 lines=1-8 label=Java focus="2-5@drives the loop|8@hands the aggregate"
That's an external iterator. The client drives the loop, and may stop, or compare. With an internal iterator, the client hands the aggregate an operation, and the iterator writes the loop for you.

@art external-internal
External is more flexible. The authors say comparing two collections element by element is easy with one, and practically impossible with an internal one. Internal is easier to use. And here the book shows its date: it calls internal iterators weak in C plus plus, which in nineteen ninety five had no closures. Java's lambdas make internal the short form.

@art changed-midwalk
Then there's robustness. Change an aggregate while you're walking it, and you can visit an element twice, or miss one. A robust iterator copes with insertions and removals without copying the aggregate. Most Java collection iterators detect the change and throw instead.

@chapter Three orders
@art tree-preorder
Now the lab, a quiz app's question bank. The quiz holds a warmup, a main section, and question six. The main section holds a bonus section, and the bonus holds question four, the deepest node. Ten nodes in all.

@math heading="The quiz's question bank" items="pre: quiz, warmup, q1, q2, main, q3, bonus, q4, q5, q6@pre order;;post: q1, q2, warmup, q3, q4, bonus, q5, main, q6, quiz@post order;;level: quiz, warmup, main, q6, q1, q2, q3, bonus, q5, q4@level order"
Pre order writes a node, then each child's subtree: quiz, warmup, q one, q two, main, and on down. Post order walks the children first, and writes the node after, so the quiz comes last. And level order writes the root, then every node one level down, then the next.

@art tree-levelorder
So where's question four? Eighth in pre order. Fifth in post order. And tenth, last, in level order. Pre order suits a contents page, post order totalling marks from the bottom up, and level order showing the top level first.

@words text="A flat list: the orders almost agree"
On a single section of four questions, pre order and level order coincide. The orders only part company when the structure has depth, which is why composites often need more than one kind of iterator.

@chapter Where people slip
@list heading="Common slips" items="Thinking a tree has one natural order@The first|Changing it while walking@The second|Every traversal on the aggregate@And the third"
The first slip is thinking a tree has one natural order. The second is changing an aggregate while walking it. And the third is putting every traversal on the aggregate's own interface, instead of in iterators it creates.

@chapter Try it
@words text="A library catalogue" sub="fiction: f1, f2 · science: s1 · maps"
Your turn. A catalogue holds a fiction shelf with two books, a science shelf with one, and a book of maps. Write its pre order, post order and level order, and where s one lands in each.

@end text="Walk the tree three ways"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
