---
format: long
lesson: reading-how-the-eyes-read/fixations-and-saccades
title: Your eyes don't glide when you read. They jump
thumb: Stop, jump, stop
---

@chapter The question
@title text="Fixations and Saccades" sub="Reading Faster · How the Eyes Read" art=thumb
Reading feels like a smooth slide along the line. But your eyes don't glide. They stop for about a quarter of a second, jump a few letters, and stop again. And the text is taken in during the stops.

@art stops-and-jumps
Watch someone else's eyes while they read, and you see jerks and pauses. The jumps were described in Emile Javal's laboratory around eighteen seventy nine. The observation was his colleague Lamare's, and Ewald Hering made it independently. Javal's word for them, saccade, is the one that stuck.

@chapter Three words
@list heading="Three words" items="Fixation: a stop, when text is taken in@A fixation|Saccade: the jump; vision is suppressed@A saccade|Regression: a jump back@A regression"
A fixation is a stop of the eyes, during which text is taken in. A saccade is the jump from one fixation to the next, and vision is suppressed while it happens. A regression is a saccade that goes back to text already passed.

@chapter Typical values
@list heading="Skilled adults, silent reading (Rayner 1998)" items="Fixations: about 200 to 250 ms@two hundred to two hundred and fifty|Saccades: 7 to 9 letter spaces, 20 to 35 ms@seven to nine|Regressions: about 10 to 15% of saccades@ten to fifteen percent"
Rayner's nineteen ninety eight review of twenty years of eye tracking gives the typical values. Fixations of about two hundred to two hundred and fifty milliseconds. Saccades of about seven to nine letter spaces, taking twenty to thirty five milliseconds. And regressions make up about ten to fifteen percent of saccades.

@art eye-dial
Put that together and the stops come about four times a second. Nearly all the reading happens in them.

@chapter The model
@math heading="A stated model" items="forward fixations per word = 6 / step@six over the step;;fixations per word = forward / (1 − regressions)@one minus;;time per word = fixations × (fixation + saccade)@time per word;;rate = 60,000 / time per word@sixty thousand"
Add a length for a word, six characters with the space, and you have a model. Forward fixations per word are six over the step. Divide by one minus the regression share to get all the fixations. The time per word is fixations times fixation plus saccade. And the rate is sixty thousand over the time per word.

@chapter The typical reader
@math heading="225 ms, 30 ms, 8 a step, 3/20 back" items="6 / 8 = 3/4@six over eight;;(3/4) / (17/20) = 15/17 ≈ 0.9@fifteen seventeenths;;15/17 × 255 = 225 ms a word@two hundred and twenty five milliseconds;;60,000 / 225 ≈ 266.7 wpm@two sixty six point seven"
Put in two twenty five milliseconds, thirty, eight characters a step, and a regression share of three twentieths. Six over eight is three quarters. Dividing by seventeen twentieths gives fifteen seventeenths, about point nine fixations. At two fifty five each, that's two hundred and twenty five milliseconds a word. So about two sixty six point seven words a minute.

@art four-hundred-stops
Read a four hundred and fifty three word passage at about two fifty a minute, and the model says your eyes stopped about four hundred times. It didn't feel like four hundred stops, did it?

@chapter One thing at a time
@math heading="Change one thing" items="no regressions: 0.75 × 255 = 191.25 ms → ≈ 313.7 wpm@no regressions;;300 ms stops: 15/17 × 330 ≈ 291.2 ms → ≈ 206.1 wpm@three hundred milliseconds"
Now change one thing at a time. With no regressions, it's point seven five fixations, one ninety one point two five milliseconds a word, about three thirteen point seven words a minute. Keep the regressions but lengthen each stop to three hundred milliseconds, and it's about two oh six point one.

@art budget-bar
A stop seventy five milliseconds longer costs about sixty words a minute. The length of a stop is where most of the budget goes. Cutting every regression buys far less, and the lesson Looking Back is about why you wouldn't want to.

@chapter What the model leaves out
@art regression-hop
The model counts a regression as one more fixation that doesn't advance. But a real one also travels back, and then the eyes must move forward again. So the model understates what looking back costs.

@art return-sweep
And at the end of each line there's a return sweep, a long jump back to the next line's start. It costs about one more fixation per line.

@words text="≈ 7.7 seconds a page" sub="30 lines of 64 characters"
On a line of sixty four characters at eight a step, that's about eight forward fixations and one more for the sweep. Over thirty lines, about thirty extra fixations: at two fifty five each, about seven point seven seconds a page.

@chapter Where people slip
@list heading="Common slips" items="Picturing the eyes gliding@The first|Reading the model's rate as yours@The second|Treating a regression as free@And the third"
The first slip is picturing the eyes gliding along the line. Any technique that promises to make the eyes flow is describing something the eyes don't do. The second is reading the model's rate as your rate. It's what five averages imply, not a measurement of anyone. And the third is treating a regression as free.

@chapter Try it
@words text="225 ms · 30 ms · 8 a step · no regressions" sub="time per word?"
Your turn. Fixations of two twenty five milliseconds, saccades of thirty, eight characters a step, no regressions, six characters a word. What's the time per word? You should get one ninety one point two five milliseconds. Then try watching someone's eyes as they read, and count the jumps across one line.

@end text="Move the model yourself"
You can move each of the five quantities and watch the rate change, on Learn. That's learn dot get er done dot I O.
