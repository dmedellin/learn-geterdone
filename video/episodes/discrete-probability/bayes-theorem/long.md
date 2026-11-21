---
format: long
lesson: discrete-probability/bayes-theorem
title: Bayes' theorem: why a 99% positive test can mean 2%
thumb: Mind the base rate
---

@chapter The question
@title text="Bayes' Theorem" sub="Discrete Probability" art=thumb
You take a test that catches a disease ninety-nine percent of the time, and it comes back positive. How worried should you be? The answer surprises almost everyone, and Bayes' theorem is how you get it.

@art flip-arrow
The test gives you the probability of a positive result given the disease. What you want is the reverse, the probability of the disease given a positive result. Bayes' theorem converts one conditional into the other.

@chapter Total probability
@art partition-strips
First, a tool. Suppose some events A one to A n split the sample space into pieces, each with positive probability. Then any event B is cut into disjoint slices, one inside each piece.

@math heading="Law of total probability" items="P(B) = Σᵢ P(B | Aᵢ) P(Aᵢ)@add up;;P(B) = P(B | A) P(A) + P(B | Ā) P(Ā)@two cases"
By additivity, you add up the slices, and the multiplication rule turns each slice into P of B given A i, times P of A i. With just two cases, A and not A, it's P of B given A times P of A, plus P of B given not A times P of not A.

@chapter The theorem
@math heading="Bayes' theorem" items="P(A ∩ B) = P(A | B) P(B) = P(B | A) P(A)@both equal;;P(A | B) = P(B | A) P(A) / P(B)@Divide by P of B"
The proof is one line. The probability of A and B is P of A given B times P of B, and it's also P of B given A times P of A. Both equal the same thing, so they equal each other. Divide by P of B, and that's Bayes' theorem.

@words text="P(A) prior · P(A | B) posterior"
P of A is called the prior, what you believed before. P of A given B is the posterior, what you believe after learning B. And the denominator is usually expanded by the law of total probability. That's where the base rate comes in.

@chapter The medical test
@art two-branch-tree
A disease affects one person in a thousand. A test detects it in ninety-nine percent of those who have it. And it gives a false positive in five percent of those who don't. You test positive.

@math heading="P(D | +)" items="P(D) = 0.001,  P(+ | D) = 0.99,  P(+ | D̄) = 0.05@the prior is zero point zero zero one;;P(+) = 0.99 × 0.001 + 0.05 × 0.999@times zero point nine nine nine;;= 0.00099 + 0.04995 = 0.05094@zero point zero five zero nine four;;P(D | +) = 0.00099 / 0.05094 ≈ 0.0194@about zero point zero one nine four"
So the prior is zero point zero zero one. The chance of a positive is zero point nine nine times zero point zero zero one, plus zero point zero five times zero point nine nine nine. That's zero point zero five zero nine four. Divide, and the answer is about zero point zero one nine four.

@words text="About 2%"
About two percent. A positive result on a ninety-nine percent sensitive test leaves you ninety-eight percent likely not to have the disease, because almost nobody tested has it.

@chapter Count it out
@art crowd-grid
If that's hard to believe, imagine a hundred thousand people. A hundred have the disease, and ninety-nine of them test positive. Ninety-nine thousand nine hundred don't, and four thousand nine hundred ninety-five of them test positive anyway.

@math heading="100 000 people" items="positives = 99 + 4 995 = 5 094@five thousand and ninety-four;;99 / 5 094 ≈ 2%@ninety-nine of them"
That's five thousand and ninety-four positives in all, and only ninety-nine of them actually have the disease. About two percent. The formula gives you the number, and the frequencies explain it.

@art positives-bar
The error this prevents is called base-rate neglect: reading the ninety-nine percent as if it were the probability of the disease given a positive. When the disease is rare, those two numbers are very far apart.

@chapter Same test, common disease
@art prior-shift
Now use the identical test where thirty percent of the people tested have the condition.

@math heading="P(D) = 0.30" items="P(+) = 0.99 × 0.30 + 0.05 × 0.70@times zero point three;;= 0.297 + 0.035 = 0.332@zero point three three two;;P(D | +) = 0.297 / 0.332 ≈ 0.895@zero point eight nine five"
The chance of a positive is zero point nine nine times zero point three, plus zero point zero five times zero point seven. That's zero point two nine seven plus zero point zero three five, which is zero point three three two. So the posterior is about zero point eight nine five.

@words text="2% → 89%" sub="same test, prior 0.001 → 0.30"
Same test. The prior moved from zero point zero zero one to zero point three, and the answer moved from two percent to eighty-nine. The test didn't change. The population it was applied to did.

@chapter Where people slip
@list heading="Common slips" items="Reporting the sensitivity as the answer@sensitivity|Dropping the false-positive branch@false positive branch|Skipping the frequency check@frequency check"
First, reporting the sensitivity as the answer. It's a property of the test, not of the patient. Second, dropping the false positive branch of the denominator, which for a rare condition is almost all of it. Third, skipping the frequency check. It takes thirty seconds, and it makes the answer believable.

@chapter Try it
@words text="1 in 1000 · 99% · 5%" sub="redo it with 1 000 000 people"
Your turn. Take the same rare disease and the same test, but imagine a million people. Count how many have it, how many of those test positive, and how many false positives there are. Then divide, and check you get the same two percent.

@end text="Always check the base rate"
The full lesson, with a lab where you can move the prevalence, is on Learn. That's learn dot get er done dot I O.
