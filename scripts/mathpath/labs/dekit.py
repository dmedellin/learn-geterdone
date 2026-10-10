"""dekit -- the differential-equations kit (PLAN section D.3).

This file builds the first-order modes (verify, field, euler, order, separable,
growth, autonomous, bifurcate) and dispatches the rest to dekit_b.MODES.
Placeholder until built; registered now so the registry is edited once.
"""

from . import dekit_b

MODES = {}


def dekit_lab(cfg):
    mode = cfg.get("mode")
    build = MODES.get(mode) or dekit_b.MODES.get(mode)
    if build is None:
        raise ValueError("dekit has no mode %r yet: docs/differential-equations/PLAN.md section D.3" % (mode,))
    return build(cfg)
