---
format: long
lesson: games-and-the-social-contract/strategic-form-and-best-responses
title: Game tables and best responses: answer the move, not the table
thumb: Fix their move, then compare
---

@chapter A game is a table
@title text="Strategic Form and Best Responses" sub="Games and the Social Contract" art=thumb
Two people each choose once, without seeing the other's choice. What should each do? Before you can answer, you need the game written down, and one simple habit for reading it.

@art bimatrix
A game in strategic form lists the players, the strategies open to each, and a payoff for each player at every combination. With two players, the row player's strategies run down the side, the column player's run across the top, and each cell shows the row payoff, then the column payoff.

@words text="A payoff is what the outcome is worth to the player."
A payoff is a number that stands for how much the outcome is worth to the player who gets it. Where the numbers come from is a separate question. Every verdict here is a verdict about the payoffs as stated.

@chapter The meeting game
@art two-paths
Here's the smallest interesting case. Two people must each take the left path or the right path to a meeting point, and they can't talk. Both left, and they meet somewhere both like very much. Both right, somewhere they like less. Choose differently, and they don't meet.

@math heading="The meeting game" items="L, L:  2, 2@Both left;;L, R:  0, 0  ·  R, L:  0, 0@choose differently;;R, R:  1, 1@both right"
In numbers: both left gives each of them two. If they choose differently, both get zero. Both right gives each of them one.

@chapter Best responses
@words text="Best response" sub="no other strategy of yours pays more against it"
A strategy is a best response to the other player's strategy when no other strategy of your own pays more against it. Ties are allowed. A best response just has to be among the largest.

@math heading="The row player, column by column" items="column plays L:  row L 2, row R 0  →  L@If the column player takes L;;column plays R:  row L 0, row R 1  →  R@If the column player takes R"
To find the row player's best responses, go column by column. If the column player takes L, the row player compares two for L with zero for R. L is the best response. If the column player takes R, it's zero for L against one for R. R is the best response.

@art column-scan
That's the step people skip. Hold the other player's choice fixed, and look only inside that one column. The row player can't change what the other has chosen. They can only answer it. So compare your own two numbers there, and nowhere else.

@art marks-meet
The column player's marks are found the same way, going row by row. And the cells where both players' marks fall are left, left and right, right. In each of those, both players are already doing the best they can against the other. The other two cells carry no pair of marks.

@chapter The model to drop
@art biggest-number
Here's a tempting shortcut: find the row with the biggest number anywhere in it, and play that. In this table the biggest number is two, in row L. But against column R, row L pays zero and row R pays one. The row with the biggest number is the worse reply.

@words text="What's best, given what the other does?"
A row is judged against a column, never alone. The question to ask is, what's best, given what the other does? And the answer can differ from column to column.

@chapter Two other tables
@art matching-pennies
Some games have only one marked cell. And some have none. In matching pennies, one player wins if the two coins match, and the other wins if they don't. So in every cell, exactly one player would rather have chosen otherwise. Best responses exist everywhere. They just never agree.

@chapter Where people slip
@list heading="Common slips" items="Playing the row with the biggest number@The first|Comparing numbers in the wrong direction@The second|Expecting a cell with both marks@the third"
The first slip is playing the row with the biggest number in it. The second is comparing numbers in the wrong direction. The row player compares down a column, the column player along a row, and each looks only at their own number. And the third is expecting every game to have a cell with both marks.

@chapter Try it
@words text="Raise one payoff until row L wins both columns"
Here's one to try. In the meeting game, raise a single payoff until row L is the best response to both columns. Then ask: does the row player still need to guess what the other will do?

@end text="Mark the best responses"
You can change any payoff and watch the best response marks move, on Learn. That's learn dot get er done dot I O.
