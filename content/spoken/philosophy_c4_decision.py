"""Spoken forms for the math runs of Philosophy course 4, Decision and Rationality.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
"""

SPOKEN = {
    'EU(a) = Σ P(s)·u(a, s)   take the largest': 'the expected utility of a equals the sum over states s of the probability of s times the utility of a in s. Take the largest',
    'u(a, s): payoff of act a in state s': 'u of a and s is the payoff of act a in state s',
    'EU(a) = Σ P(s)·u(a, s)': 'the expected utility of a equals the sum over states s of the probability of s times the utility of a in s',
    'u(wealth) rises, but ever more slowly': 'the utility of wealth rises, but ever more slowly',
    'u(0)': 'the utility of nothing',
    'u(1M)': 'the utility of one million',
    'u(5M)': 'the utility of five million',
    'u(0) = 0': 'the utility of nothing is 0',
    'u(1M) = 10': 'the utility of one million is 10',
    'u(5M) = 14': 'the utility of five million is 14',
    '11/10·u(1M)': 'eleven tenths times the utility of one million',
    'EU(A) − EU(B) = 11/100·u(1M) − 10/100·u(5M) − 1/100·u(0)': 'the expected utility of A minus that of B equals eleven hundredths times the utility of one million, minus ten hundredths times the utility of five million, minus one hundredth times the utility of nothing',
    'EU(C) − EU(D) = 11/100·u(1M) − 10/100·u(5M) − 1/100·u(0)': 'the expected utility of C minus that of D equals eleven hundredths times the utility of one million, minus ten hundredths times the utility of five million, minus one hundredth times the utility of nothing',
    'red in I needs p(black) < 1/3': 'red in decision one needs the probability of black below one third',
    'black or yellow in II needs p(black) > 1/3': 'black or yellow in decision two needs the probability of black above one third',
}
