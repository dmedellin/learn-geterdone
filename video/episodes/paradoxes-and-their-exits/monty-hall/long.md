---
format: long
lesson: paradoxes-and-their-exits/monty-hall
title: Monty Hall: why switching wins two thirds of the time
thumb: Count the host's choices
---

@chapter The game
@title text="Monty Hall" sub="Paradoxes and Their Exits" art=thumb
A game show has three doors. Behind one is a car, behind the other two, goats. You choose door one. The host, who knows where the car is, always opens another door to show a goat. If both others hide goats, he picks at random. He opens door three. Should you switch to door two?

@art three-doors
Most people say it makes no difference. Two doors are closed, the car's behind one, so each has chance one half. That reasoning treats the news as, door three is empty. But the news wasn't that. It was that the host opened door three.

@chapter The host's act as evidence
@list heading="Chance the host opens door 3" items="Car at 1: one half@behind door one|Car at 2: certain@behind door two|Car at 3: zero@behind door three"
Let the hypotheses be the car's three places, each with prior one third. If the car is behind door one, he may open two or three, so he opens three with probability one half. If it's behind door two, he can't open two or your door, so he must open three. Probability one. And if it's behind door three, he can't open it. Probability zero.

@math heading="Update on the host's act" items="likelihoods:  1/2,  1,  0@likelihoods;;prior × likelihood:  1/6,  1/3,  0@Multiply;;total:  1/2@total;;posterior:  1/3,  2/3,  0@posterior"
The likelihoods are one half, one, and zero. Multiply by the priors of one third, and you get one sixth, one third, and zero. The total is one half. So the posterior is one third, two thirds, and zero.

@art forced-move
So door two holds the car with probability two thirds, and staying wins one third. Door one gave the host a free choice, and door two gave him none. Seeing him open door three is twice as probable if the car is behind door two.

@chapter Another way to count
@art grouped-doors
Here's another way. Door one holds the car with chance one third, and nothing the host does can change that, because he never opens your door, and never opens the car. The other two doors together hold two thirds. The host has shown one of them is empty, so the whole two thirds falls on the other.

@chapter Which exit?
@art car-behind
Set out as a paradox, every premise is part of the setup, and every step is valid. The conclusion just felt wrong. So the exit is the third: accept it. The argument for one half wasn't the paradox. It was a mistake. The price is small. You lose the habit of treating an empty door as the whole of the evidence.

@chapter A different host
@math heading="A host who opens at random" items="likelihoods:  1/2,  1/2,  0@at random;;posterior:  1/2,  1/2,  0@one half each"
Now suppose the host doesn't know where the car is. He opens one of the other two doors at random, and it happens to show a goat. The likelihood is one half if the car's at one, one half if it's at two, and zero at three. The posterior is one half each, and switching is worth no more than staying.

@art random-host
Same sight, door three open and empty, different answer. The host's rule did the work. A problem without the rule has two correct answers, one for each rule. That's why the standard statement gives it.

@chapter Four doors
@art four-doors
Add a door, and the same reasoning holds.

@math heading="Four doors, host opens 4" items="likelihoods:  1/3,  1/2,  1/2,  0@Door one;;posterior:  1/4,  3/8,  3/8,  0@The posterior"
With four doors, you choose one, and the informed host opens door four. Door one gave him a choice of three, so the likelihood is one third. Doors two and three gave him a choice of two, so one half. The posterior is one quarter for door one, and three eighths for each of the others.

@chapter Where people slip
@list heading="Common slips" items="Two doors remain, so each is one half@The first|Treating the empty door as the whole evidence@The second|Assuming the answer holds without the rule@And the third"
The first slip is thinking that two doors remain, so each is one half. Count the host's choices, not the doors. A forced move is stronger evidence. The second is treating the sight of an empty door as the whole of the evidence. Ask what the host would have done under each hypothesis. And the third is assuming the answer holds without the host's rule.

@chapter Try it
@words text="informed host → random host" sub="edit the likelihood rows"
Start with the informed host's likelihoods, one half, one, and zero, and check switching wins two thirds. Then edit them toward the random host's, one half, one half, and zero, and watch the best act change.

@end text="Count the host's choices"
You can change the host's rule and watch the answer move, on Learn. That's learn dot get er done dot I O.
