---
format: long
lesson: accelerate-culture/what-westrum-culture-predicts
title: What a generative culture predicts, and what it doesn't prove
thumb: Predicts is not causes
---

@chapter Does the score predict anything?
@title text="What Westrum Culture Predicts" sub="Accelerate, Chapter 3" art=thumb
You can turn culture into a score. But is that score good for anything? Chapter three tests it.

@art trust-network
Westrum's theory is that an organization whose information flows better works better. The authors give three reasons a culture score should stand for more than itself. It reflects trust and cooperation. It can indicate better decisions, which are easier to reverse in an open team. And problems get found and fixed faster.

@list heading="Three hypotheses" items="Better software delivery@software delivery|Better organizational performance@performing organization|More satisfied staff@satisfied staff"
From that they set three hypotheses: a higher culture score goes with better software delivery, a better performing organization, and more satisfied staff. The chapter says all three proved true.

@words text="Inferential predictive research"
Their footnote says what kind of claim that is: inferential predictive research. The data are consistent with a relationship the theory expected. It's not an experiment that changed culture and watched the result.

@chapter Three measures, not four
@art three-of-four
One precision is easy to miss. Chapter two had four delivery measures. When the authors tried to build a construct from all four, it didn't pass every test. Three of them, lead time, release frequency and time to restore, passed together.

@words text="Delivery performance = lead time · release frequency · time to restore" sub="change fail rate: strongly correlated, not in the construct"
So from here on, software delivery performance means that three measure construct. Change fail rate is still useful. It's strongly correlated with the construct.

@chapter Google's teams
@quote text="who is on a team matters less than how the team members interact, structure their work, and view their contributions" cite="Google, as quoted in Accelerate, Chapter 3"
The finding fits a study at Google: two years, over two hundred interviews, and more than one hundred and eighty teams. They expected the secret in individual skills. They found it in team dynamics: who is on a team matters less than how the team members interact, structure their work, and view their contributions.

@chapter Failure as a test
@art contributing-factors
Failure tells you a lot. A pathological organization looks for a throat to choke. But in complex systems, the authors write, an accident seldom comes from one person. It emerges from many contributing factors.

@quote text="Human error should, instead, be the start of the investigation" cite="Forsgren, Humble and Kim, Accelerate, Chapter 3"
So human error should, instead, be the start of the investigation, with the question of how information could have reached people sooner, or in a better form.

@chapter A correlation by hand
@art scatter-line
Now the count. The lesson's lab takes eight invented teams. Each has a culture score, and a delivery score the lesson invents: the mean of three coded answers on lead time, release frequency and time to restore.

@math heading="Pearson's r" items="r = Σ(dx·dy) / √(Σdx² · Σdy²)@r is the sum;;means: 34/8 = 4.25 · 30.5/8 = 3.8125@the means are"
Pearson's r is the sum of the products of the deviations, over the square root of the product of the two sums of squared deviations. For the eight teams, the means are four point two five for culture and three point eight one two five for delivery.

@math heading="Eight teams" items="Σ(dx·dy) = 10.625@ten point six two five;;r = 10.625 / √(10.5 × 12.46875) = 10.625 / 11.442 = 0.929@zero point nine two nine;;r² = 0.862 → 86.2% of the spread@eighty six point two"
The products sum to ten point six two five. The squares sum to ten point five and twelve point four six eight seven five. So r is ten point six two five over eleven point four four two: zero point nine two nine. And eighty six point two percent of the spread in delivery is accounted for by the line.

@art outlier-moves
Now change one number. The team highest in culture scores two on delivery instead of six. R falls to zero point three seven four. With eight teams, one team can move a correlation a long way. The book draws on over twenty three thousand responses.

@art three-stories
And neither result says culture causes delivery. Delivery could drive culture, or a third thing, like the age of the system, could drive both. The correlation is the same in all three stories.

@chapter Where people slip
@list heading="Common slips" items="Reading predicts as causes@The first|r² as a share of teams or of cause@The second|Counting change fail rate in the construct@the third"
The first slip is reading predicts as causes. The second is taking r squared for the share of teams, or the share of cause. And the third is counting change fail rate in the delivery construct.

@chapter Try it
@words text="v 3,3 · w 4,2 · x 5,4 · y 6,5 · z 7,6"
Your turn. Five teams, culture then delivery. Find the two means, the sum of products of deviations, and the sums of squares, then r and r squared. Then raise team w's delivery to four, and say whether r rises or falls.

@end text="Predicts is not causes"
You can move one team and watch the correlation swing, on Learn. That's learn dot get er done dot I O.
