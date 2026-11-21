---
format: long
lesson: mind-language-and-meaning/behaviourism-and-the-turing-test
title: The Turing test as Bayesian updating
thumb: A Bayes factor of 1
---

@chapter Behaviourism
@title text="Behaviourism and the Turing Test" sub="Mind, Language and Meaning" art=thumb
Behaviourism about the mind says that to be in a mental state is to be disposed to behave in certain ways. On its strongest version, nothing is left over. There's no inner fact about whether a thing thinks, beyond what it would say and do.

@art screen-judge
Turing's proposal replaces the question. A judge converses in writing with two parties, one human and one machine, and must say which is which. If the judge can't do better than chance, the machine has passed. Turing himself set aside the original question as too ill defined. Read as a test of thought, his game is behaviourism put to work.

@chapter The judge as updater
@art two-hypotheses
Model the judge as what a judge is, an updater. There are two hypotheses about who's behind the screen, human and machine. Each answer is data, and each hypothesis assigns a probability to each kind of answer.

@math heading="A machine with a tell" items="plain:  human 9/10,  machine 1/10@a plain answer;;tell:  human 1/10,  machine 9/10@a tell"
Take two kinds of answer. A plain answer has probability nine tenths if human, and one tenth if machine. A tell, an answer the machine gives more often, like arithmetic too fast or a reply too even in tone, has one tenth if human and nine tenths if machine.

@math heading="One tell" items="Bayes factor:  (1/10) / (9/10) = 1/9@The Bayes factor;;prior 1/2  →  posterior 1/10@a prior of one half"
The Bayes factor of one tell, for the hypothesis human, is one tenth over nine tenths, which is one ninth. The answer is nine times as probable if it's a machine. Starting from a prior of one half, the posterior for human after one tell is one tenth.

@chapter The perfect mimic
@art identical-rows
Now the perfect mimic. Give the machine the human's row exactly. A plain answer with nine tenths, and a tell with one tenth, whoever it is. Every answer is exactly as probable under one hypothesis as the other. So every answer has a Bayes factor of one.

@words text="Ten answers: factor 1" sub="the posterior is the prior"
And ten answers together have a factor of one. The posterior is the prior. The judge has learned nothing about who's behind the screen. That's all a pass is. Those ten answers aren't weak evidence. They're no evidence, because the rows are the same.

@chapter The prior matters
@math heading="Same tell, different judges" items="prior 9/10  →  posterior 1/2@starts at nine tenths;;prior 1/2  →  posterior 1/10@starts at one half"
A judge who starts at nine tenths for human and meets one tell lands at one half. The factor of one ninth exactly cancels the odds of nine to one. A judge who starts at one half lands at one tenth. The same tell is the same evidence, and it moves different judges to different places.

@chapter What a pass measures
@art imitation-mask
Two consequences for the claim that the test measures thought. A pass isn't a proof. A factor of one says the judge couldn't tell the parties apart, which is a fact about how well the machine imitates. And a very good imitation of a thinking person need not think.

@art odd-manner
A failure isn't a disproof either. A tell shows the parties differ in style, and a person with an odd manner of answering would show one too. The behaviourist closes the gap by definition, because for the behaviourist there's nothing for the test to miss. The Chinese room shows what that costs.

@chapter Where people slip
@list heading="Common slips" items="Reading a pass as proof, a failure as disproof@The first|Counting ten answers as ten pieces of evidence@The second|Thinking one tell settles it@And the third"
The first slip is reading a pass as proof of thought, and a failure as disproof. Only a bridge premise about behaviour and mind turns either into a verdict on thought. The second is counting ten answers as ten pieces of evidence. Ten times one is one. And the third is thinking one tell settles the question. A confident judge needs more.

@chapter Try it
@art moving-needle
Start with the mimic, two identical rows, and change the answers heard. Watch the posterior stay put. Then change one entry in the machine's row, and see how far a single answer now moves the judge. Remember, the hypotheses are human and machine, not thinks and doesn't think.

@end text="What should the judge believe?"
You can set the rows and the prior yourself, on Learn. That's learn dot get er done dot I O.
