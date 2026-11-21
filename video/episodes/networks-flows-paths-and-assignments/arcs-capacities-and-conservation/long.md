---
format: long
lesson: networks-flows-paths-and-assignments/arcs-capacities-and-conservation
title: Is this flow feasible? Two tests, node by node and arc by arc
thumb: Two tests, not one
---

@chapter The question
@title text="Arcs, Capacities and Conservation" sub="Networks, Flows, Paths and Assignments" art=thumb
Someone hands you a network and a plan for moving goods through it. Is the plan possible? To answer that, the network has to stop being a picture and become data.

@art directed-network
A directed network is a set of nodes and a list of arcs. Each arc has a tail and a head, a capacity, and a cost per unit. Each node has a supply: positive where goods enter, negative where they leave. A flow is one number for each arc, never negative.

@list heading="A flow is feasible when" items="It conserves at every node@conserves at every node|It respects every capacity@respects every capacity"
And a flow is feasible when it does two separate things. It conserves at every node, and it respects every capacity on every arc. Those are two different tests, and this whole lesson is about not mixing them up.

@chapter A worked check
@words text="Supplies: s = 4, t = −4" sub="arcs s→a, a→b, b→a, a→t, b→t"
Take the lesson's network. Node s supplies four units and node t takes four. There are five arcs: s to a, a to b, b to a, a to t, and b to t. The proposed flow sends four on s to a, two on a to b, nothing on b to a, and two each on a to t and b to t.

@art node-balance
The first test is conservation, and it's one equation per node. What leaves the node, minus what arrives, must equal that node's supply.

@math heading="Out − in = supply" items="s:  4 − 0 = 4  ✓@At s;;a:  2 + 2 − 4 = 0  ✓@At a;;b:  0 + 2 − 2 = 0  ✓@At b;;t:  0 − 4 = −4  ✓@at t"
At s, four minus nothing is four. At a, two plus two minus four is zero. At b, nothing plus two minus two is zero. And at t, nothing minus four is minus four. All four balance.

@math heading="Capacity, then cost" items="4 ≤ 5,  2 ≤ 4,  0 ≤ 3,  2 ≤ 3,  2 ≤ 4  ✓@every arc;;cost = 4·2 + 2·2 + 0·5 + 2·1 + 2·3 = 20@costs twenty"
Then the second test, on every arc: four is within five, two within four, nothing within three, two within three, and two within four. It passes. With the given prices, this flow costs twenty.

@chapter An arc has a direction
@art two-arrows
Notice that a to b and b to a join the same two nodes. They are not one edge. A to b holds up to four at a price of two. B to a holds up to three at a price of five. They're two separate variables.

@words text="1 forward, 2 back: 12 · 2 forward, 1 back: 9"
Send one unit forward and two back, and it costs twelve. Send two forward and one back, and it costs nine. Same total movement, different bill, because each direction is priced on its own.

@chapter Conservation fails locally
@art cancelling-errors
Now change one number. Make a to b carry one instead of two. Node a now takes in one more unit than it sends on, and node b sends on one more than it takes in. Those errors are equal and opposite.

@words text="Net outflows 4, −1, 1, −4" sub="against supplies 4, 0, 0, −4"
So the imbalances still add up to zero, and any check that adds them up will pass. That total is zero for every flow ever written, feasible or not. The useful answer names the failing nodes, a and b, one by one.

@chapter Capacity is a separate test
@art over-capacity
The opposite can happen too. Set the supplies to five and minus five, and send five on s to a, five on a to b, and five on b to t. Every node balances exactly. But a to b holds only four, and so does b to t. Conservation can't see this, because the node equations contain no capacities at all.

@chapter Check the data first
@art unbalanced-supply
Add up all the node equations. Every arc leaves one node and enters one, so each variable appears once with a plus and once with a minus, and cancels. What's left says the supplies must sum to zero. Set s to six and t to minus four, and the sum is two. No flow of any kind exists.

@words text="Six in, four out" sub="the network is fine; the demand doesn't match"
That diagnosis is worth having before any solver runs. Nothing is wrong with the network. The demand doesn't match the supply, and the fix is to say what happens to the surplus. And a flow may only name arcs that exist in the data.

@chapter Where people slip
@list heading="Common slips" items="Treating two opposite arcs as one edge@The first|Reading the summed imbalance as a verdict@The second|Modelling no bound as a huge constant@And the third"
The first slip is treating two opposite arcs as one edge. The second is adding the imbalances up and reading the total as a verdict. And the third is modelling an unbounded arc with a large constant. A capacity of a million is still a capacity: it adds a row, and it can bind.

@chapter Try it
@words text="a→b: 2 becomes 1" sub="which nodes fail, and by how much?"
Your turn. Start from the feasible flow, change a to b from two to one, and work out the net outflow at all four nodes. Name each node that fails and by how much. Then check whether the total of the imbalances could ever have told you.

@end text="Test a flow, node by node"
You can type in a network, propose a flow, and see exactly where it fails, on Learn. That's learn dot get er done dot I O.
