---
format: long
lesson: markov-chains-decisions-and-queues/markov-decision-processes-and-policy-iteration
title: Policy iteration: solve exactly, improve greedily, stop for a reason
thumb: Stops for a reason
---

@chapter Adding choices
@title text="Markov Decision Processes and Policy Iteration" sub="Markov Chains, Decisions and Queues" art=thumb
Give a Markov chain a choice of action in every state, and a reward for each choice. Now it's a decision problem. Which action should you take, where?

@art two-actions
That's a discounted Markov decision process. Each action has its own transition matrix, and each state and action pair has a reward. Future rewards are discounted by gamma, between zero and one.

@art policy-picks
A policy picks one action per state. And once you fix it, the transition matrix is determined. So a policy is just an ordinary Markov chain with a reward attached, and the problem is which of finitely many chains to be.

@chapter Evaluate exactly
@math heading="Value of a policy" items="v = r_d + γ·P_d·v@v equals"
A policy's value solves v equals r d plus gamma P d v. That's n linear equations in n unknowns, solved exactly, the same elimination as the steady state. It has one solution because the discount is below one.

@chapter Improve greedily
@math heading="Improvement" items="q(s, a) = r(s, a) + γ Σ P(s′|s, a) v(s′)@q of s"
Then improve. For each state, compute q of s and a, the reward for action a plus the discounted expected value, using the v you just solved for. Switch each state to its best action. If no state switches, stop.

@art evaluate-improve
That's one round: evaluate, then improve, every state against the same value vector. Updating as you go is a different algorithm, and the proof below doesn't cover it.

@chapter A worked problem
@words text="Two states · two actions · γ = 9/10" sub="action 1 r = (1, 3) · action 2 r = (2, 1)"
Here's the lesson's problem. Two states, two actions, discount nine tenths. Action one pays one and three, action two pays two and one.

@math heading="Round 1: action 1 everywhere" items="v = (670/31, 750/31)@six seventy;;state 1:  670/31 vs 683/31  → switch@switch;;state 2:  750/31 vs 670/31  → keep@keep"
Round one: action one everywhere. Solving gives six seventy over thirty one, and seven fifty over thirty one. At state one, action two gives six eighty three over thirty one, which is better, so switch. At state two, keep.

@math heading="Round 2" items="v = (265/11, 285/11)@two sixty five;;state 1:  47/2 vs 265/11  → keep@forty seven halves;;nothing changed — stop@stop"
Round two. Solve again: two sixty five over eleven, and two eighty five over eleven. At state one, the alternative is forty seven halves, which is less. At state two, keep. Nothing changed, so stop. Four policies in total, two rounds.

@chapter Why it stops
@art staircase-up
Greedy improvement never lowers any state's value. If nothing changes, you're optimal. If something does, the value strictly rose somewhere, so the policy is new. With finitely many policies, that can only happen finitely often. That's a proof, not a tolerance.

@art vi-from-below
Compare value iteration. It climbs from zero: two, then about four, then about five point nine five. After twelve steps, state one is at about seventeen point oh three, still about seven point oh six short. It approaches from below and never arrives.

@words text="15-digit denominators vs 265/11"
And watch its denominators. They grow from one digit to fifteen by step twelve, while the exact answer has a two digit denominator. The iteration piles up complexity approaching a number that was simple all along.

@chapter Discounts and swings
@words text="γ = 19/20: still 2 rounds" sub="value iteration 27.02 short at 12 steps"
Raise the discount to nineteen twentieths and policy iteration still takes two rounds. Value iteration is now twenty seven point oh two short after twelve steps. Rounds depend on the policies, and the iteration's speed depends on gamma.

@art swing-back
And a three state stock example takes three rounds. The middle round swings every state to restock, then swings the first state back. Stopping at the first improvement would have been wrong by fifteen to eighteen in every state.

@chapter Where people slip
@list heading="Common slips" items="Updating values mid-sweep@The first|Stopping value iteration on the step size@The second|Comparing policies in floating point@And the third"
The first slip is updating values mid sweep. The second is stopping value iteration when the steps get small, and calling that the answer. And the third is comparing policies in floating point. Here they differ by thirteen twenty seconds, but near a discount of one, they can be much closer.

@chapter Try it
@words text="γ = 9/20" sub="value (1330/341, 1770/341)"
Your turn. Run policy iteration on the two state problem at a discount of nine twentieths. You should stop in two rounds, with values thirteen thirty and seventeen seventy, both over three forty one.

@end text="Evaluate, improve, stop"
You can change the discount and watch policy iteration beat value iteration, on Learn. That's learn dot get er done dot I O.
