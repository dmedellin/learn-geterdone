"""The passage bank: every text a Reading Faster drill times.

Written for this Subject (docs/reading/PLAN.md §P). bank_a holds P01-P24,
bank_b P25-P49 and the scanning and inspection texts, pool the Daily Drill's
Q01-Q30. A lesson's lab cfg carries the passage dicts it uses, so a page
ships its own texts and nothing else.
"""

from . import bank_a, bank_b, pool

PASSAGES = {**bank_a.PASSAGES, **bank_b.PASSAGES, **pool.PASSAGES}

# The Daily Drill serves these in order.
POOL = [pool.PASSAGES["Q%02d" % n] for n in range(1, 31)]
