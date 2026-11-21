---
format: long
lesson: accelerate-surveys-and-data/tests-of-the-measurement-model
title: Tests of the measurement model: when is a construct fit to use?
thumb: Every test must pass
---

@chapter All must pass
@title text="Tests of the Measurement Model" sub="Accelerate, Appendix C" art=thumb
Before the authors of Accelerate test any claim, they test their measures. A construct goes into the analysis only if it clears every one of a list of tests.

@quote text="All of the above tests must pass for a construct to be considered suitable for use in further analysis." cite="Forsgren, Humble and Kim, Accelerate, Appendix C"
In their words. All of the above tests must pass for a construct to be considered suitable for use in further analysis.

@art two-stages
They work in two stages, following Gefen and Straub, twenty oh five. First, validate the measures and form the latent constructs. Then, with only the constructs that pass, test the hypotheses.

@chapter The tests
@list heading="The appendix's thresholds" items="Item loadings above 0.60, no cross-loading@should load|Average variance extracted above 0.50@variance extracted|√AVE above the construct's correlations@square root|Correlations between constructs below 0.85@below nought point eight five|Reliability at least 0.70@reliability"
Here's the list. Items should load on their construct above nought point six, and not cross load. The average variance extracted should be above nought point five. Its square root should beat the construct's correlations with the others. Those correlations should be below nought point eight five. And reliability should be at least nought point seven.

@art loadings
The loadings come from principal components analysis with varimax rotation. The authors almost always used the exploratory kind, which finds the structure without imposing one. The exception was transformational leadership, whose items are well established, so they used the confirmatory kind.

@math heading="From standardized loadings (standard formulas)" items="AVE = (λ₁² + … + λₖ²) ÷ k@mean of the squared loadings;;root test: √AVE > |r|, or AVE > r²@r squared;;CR = (Σλ)² ÷ ((Σλ)² + Σ(1 − λ²))@composite reliability"
The appendix gives no formula, so the lab uses the standard ones. AVE is the mean of the squared loadings. The root test is the same as asking that AVE exceed r squared. And composite reliability is the squared sum of loadings, over that plus each item's leftover error.

@art short-scale
Why composite reliability? Cronbach's alpha, with its cutoff of nought point seven, is biased against short scales with few items. So the authors ran both, and every construct met one of the two cutoffs.

@chapter Two sound constructs
@math heading="release-confidence: 0.85, 0.80, 0.75, 0.70" items="squares sum to 2.415; AVE = 2.415 ÷ 4 ≈ 0.604@two point four one five;;CR = 9.61 ÷ (9.61 + 1.585) ≈ 0.858@nought point eight five eight;;√AVE ≈ 0.777 > r = 0.45@nought point seven seven seven"
Now the lab. Release confidence has loadings nought point eight five, nought point eight, nought point seven five and nought point seven. Their squares sum to two point four one five, so AVE is about nought point six oh four. Composite reliability is nought point eight five eight. The root, nought point seven seven seven, beats the correlation of nought point four five with team trust. With team trust passing too, it's fourteen of fourteen tests.

@chapter A weak construct
@art weak-legs
Swap in tool fit, with loadings nought point seven, nought point six and nought point five five. Its AVE is nought point three eight four, below one half. Its CR is nought point six four nine, below nought point seven. And two loadings aren't above nought point six.

@art gates
Yet its root, nought point six two, beats its correlation of nought point three, and nought point three is below nought point eight five. So two tests pass for a construct that fails three kinds of test. The lab counts ten of fourteen. That's why all must pass.

@chapter Too close
@art overlapping
Now pair release confidence with release readiness. Each passes its loadings, AVE and reliability. They correlate at nought point eight, below nought point eight five, so the correlation test passes.

@math heading="The root test fails" items="r² = 0.80² = 0.64@nought point six four;;0.64 > AVE 0.604@above;;√0.604 ≈ 0.777 < 0.80@fails"
But nought point eight squared is nought point six four, which is above release confidence's AVE of nought point six oh four. So its root, nought point seven seven seven, is below nought point eight, and the root test fails. The construct shares as much with another as with its own items.

@chapter Where people slip
@list heading="Common slips" items="One test passed, so it's valid@valid|The 0.85 limit and the root test are one test@one test|AVE scores how good a construct is@how good"
Three slips. Passing one test and calling the construct valid. Treating the nought point eight five limit and the root test as one test. And reading AVE as a score of how good a construct is. Passing shows items hang together in one sample, not that the name fits.

@chapter Try it
@words text="scope: 0.80, 0.70, 0.65 · pace: 0.90, 0.85, 0.80 · r = 0.75"
Your turn. Scope has loadings nought point eight, nought point seven and nought point six five. Pace has nought point nine, nought point eight five and nought point eight. They correlate at nought point seven five. Compute scope's AVE and CR, test every threshold, and find the one that fails.

@end text="Every test must pass"
Then type the records into the lab, on Learn. That's learn dot get er done dot I O.
