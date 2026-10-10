"""dekit's first-order modes build every preset docs/differential-equations/PLAN.md section C sketches.

Fast and browserless. Every fixture is built through labs.build("dekit", cfg):
verify, field, euler, order, separable, growth, autonomous and bifurcate, one
entry per section C lesson that uses them. The markup and script are checked
for the controls, tiles and wiring D.3 names, for ES5, and for the absence of
a double quote in everything de_core and dekit add to a page. Each preset's
own page script then runs under node against a stub document and its pinned
tiles are compared (skipped when node is absent).

The `expect` figures were read off rendered fixture pages with
`node scripts/labcheck.js --observe` and checked by hand against section C's
worked lines (see the comments beside them); FIXTURES is importable, so a
fixture page can be rendered and gated by labcheck.js --expect.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from mathpath import labs  # noqa: E402
from mathpath.labs import de_core, dekit  # noqa: E402


def _p(pid, expect=None, **fields):
    out = {"id": pid, "label": pid.replace("-", " ")}
    out.update(fields)
    out["expect"] = expect or {}
    return out


W3 = ["-3", "3", "-3", "3"]
LOGI = "y(1 - y/4)"
CUBIC = "y^3 - 4y^2 + 3y"
TWO = "y^2 - 4y + 3"

# (section C lesson, cfg). One entry per lesson that uses these eight modes.
FIXTURES = [
    # 3.1: y' = 2t against t², t² + 3 and t³ (residual 3t² − 2t).
    ("3.1", {"mode": "verify", "presets": [
        _p("square", {"vfOrder": "1", "vfResidual": "0", "vfVerdict": "Solution"},
           equation="y' = 2t", candidate="t^2", ic=None),
        _p("shifted", {"vfOrder": "1", "vfResidual": "0", "vfVerdict": "Solution"},
           equation="y' = 2t", candidate="t^2 + 3", ic=None),
        _p("cube", {"vfOrder": "1", "vfResidual": "3t² − 2t", "vfVerdict": "Not a solution"},
           equation="y' = 2t", candidate="t^3", ic=None)]}),
    # 3.2: 4 − 2 − 2 = 0 for e^(2t); 1 − 1 − 2 = −2 for eᵗ; t·10t = 2·5t².
    ("3.2", {"mode": "verify", "presets": [
        _p("two-exps", {"vfLinear": "Linear", "vfResidual": "0", "vfVerdict": "Solution"},
           equation="y'' - y' - 2y = 0", candidate="e^(2t)", ic=None),
        _p("wrong-exp", {"vfLinear": "Linear", "vfResidual": "−2·e^t", "vfVerdict": "Not a solution"},
           equation="y'' - y' - 2y = 0", candidate="e^t", ic=None),
        _p("power", {"vfLinear": "Linear", "vfResidual": "0", "vfVerdict": "Solution"},
           equation="t y' = 2y", candidate="5t^2", ic=None),
        _p("nonlinear", {"vfLinear": "Nonlinear", "vfResidual": "0", "vfVerdict": "Solution"},
           equation="y' = y^2", candidate="1/(1 - t)", ic=None)]}),
    # 3.3: 1 + C = 5; C·e⁰ = 2; C = 1 and D = −2 from y(0), y′(0).
    ("3.3", {"mode": "verify", "presets": [
        _p("first", {"vfFamily": "C = 4 from y(1) = 5", "vfIC": "satisfied"},
           equation="y' = 2t", candidate="t^2 + C", ic=[1, 5]),
        _p("growth", {"vfFamily": "C = 2 from y(0) = 2", "vfIC": "satisfied"},
           equation="y' = 3y", candidate="C e^(3t)", ic=[0, 2]),
        _p("second", {"vfFamily": "C = 1, D = −2", "vfIC": "satisfied"},
           equation="y'' + y = 0", candidate="C cos(t) + D sin(t)", ic=[0, 1, -2])]}),
    # 7.2: x = t·cos t gives x″ + x = −2·sin t.
    ("7.2", {"mode": "verify", "presets": [
        _p("cos", {"vfResidual": "0", "vfVerdict": "Solution"}, equation="y'' + y = 0", candidate="cos(t)", ic=None),
        _p("combo", {"vfResidual": "0", "vfVerdict": "Solution"},
           equation="y'' + y = 0", candidate="3cos(t) - 2sin(t)", ic=None),
        _p("not", {"vfResidual": "−2·sin(t)", "vfVerdict": "Not a solution"},
           equation="y'' + y = 0", candidate="t cos(t)", ic=None),
        _p("fit", {"vfResidual": "0", "vfVerdict": "Solution", "vfFamily": "C = 1, D = −2"},
           equation="y'' + y = 0", candidate="C cos(t) + D sin(t)", ic=[0, 1, -2])]}),
    # 3.4: t − y at (1, 1) is 0; y at (0, 1) is 1; 2t at (1, 2) is 2.
    ("3.4", {"mode": "field", "grid": 15, "presets": [
        _p("t-minus-y", {"sfSlope": "0", "sfZero": "y = t"}, f="t - y", window=W3, start=None, point=[1, 1]),
        _p("y-only", {"sfSlope": "1", "sfZero": "y = 0"}, f="y", window=W3, start=None, point=[0, 1]),
        _p("t-only", {"sfSlope": "2", "sfZero": "none in y"}, f="2t", window=W3, start=None, point=[1, 2])]}),
    # 3.5: y(1 − y) at y = 1/2 is 1/4; t − y at (2, 0) is 2; y² at (0, 1) is 1.
    ("3.5", {"mode": "field", "grid": 15, "presets": [
        _p("logistic", {"sfEquil": "y = 0, y = 1", "sfSlope": "1/4"},
           f="y(1 - y)", window=[-1, 4, -1, 2], start=[0, "1/2"], point=[0, "1/2"]),
        _p("t-minus-y", {"sfEquil": "none", "sfSlope": "2"}, f="t - y", window=W3, start=[0, 2], point=[2, 0]),
        _p("square", {"sfEquil": "y = 0", "sfSlope": "1"},
           f="y^2", window=[-2, 2, -2, 4], start=[0, 1], point=[0, 1])]}),
    # 3.6: (5/4)⁴ = 625/256; Euler on 2t is the left sum 3/4, error 1/4.
    ("3.6", {"mode": "euler", "presets": [
        _p("growth", {"euLast": "625/256", "euLastDec": "≈ 2.44141", "euExact": "≈ 2.71828", "euError": "≈ 0.276876"},
           f="y", t0=0, y0=1, h="1/4", n=4, exact="e^t"),
        _p("ramp", {"euLast": "3/4", "euExact": "1", "euError": "1/4"}, f="2t", t0=0, y0=0, h="1/4", n=4, exact="t^2"),
        _p("mixed", {"euLast": "19/16", "euExact": "≈ 1.40601", "euError": "≈ 0.218506"},
           f="t - y", t0=0, y0=2, h="1/2", n=4, exact="t - 1 + 3e^(-t)")]}),
    # 3.7: E(h) = h on 2t; 11/96, 23/384, 47/1536 on t².
    ("3.7", {"mode": "order", "method": "euler", "presets": [
        _p("ramp", {"odE1": "1/4", "odRatio": "2, 2", "odOrder": "1"},
           f="2t", t0=0, y0=0, T=1, exact="t^2", hs=["1/4", "1/8", "1/16"]),
        _p("square", {"odE1": "11/96", "odRatio": "44/23, 92/47", "odOrder": "≈ 0.968973"},
           f="t^2", t0=0, y0=0, T=1, exact="t^3/3", hs=["1/4", "1/8", "1/16"]),
        _p("growth", {"odE1": "≈ 0.276876", "odRatio": "≈ 1.81561, ≈ 1.89783", "odOrder": "≈ 0.924354"}, f="y", t0=0, y0=1, T=1, exact="e^t", hs=["1/4", "1/8", "1/16"])]}),
    # 3.8: the trapezoid rule on t²: 1/96, 1/384, 1/1536.
    ("3.8", {"mode": "order", "method": "heun", "presets": [
        _p("square", {"odE1": "1/96", "odRatio": "4, 4", "odOrder": "2"},
           f="t^2", t0=0, y0=0, T=1, exact="t^3/3", hs=["1/4", "1/8", "1/16"]),
        _p("quartic", {"odE1": "53/2560", "odRatio": "848/213, 3408/853", "odOrder": "≈ 1.99831"}, f="t^4", t0=0, y0=0, T=1, exact="t^5/5", hs=["1/4", "1/8", "1/16"]),
        _p("growth", {"odE1": "≈ 0.0234261", "odRatio": "≈ 3.63727, ≈ 3.81482", "odOrder": "≈ 1.93162"}, f="y", t0=0, y0=1, T=1, exact="e^t", hs=["1/4", "1/8", "1/16"])]}),
    # 3.9: RK4 is Simpson on t³ (error 0) and h⁴/2880·24 on t⁴: 1/30720.
    ("3.9", {"mode": "order", "method": "rk4", "presets": [
        _p("cubic", {"odE1": "0", "odRatio": "—", "odOrder": "exact (error 0)"},
           f="t^3", t0=0, y0=0, T=1, exact="t^4/4", hs=["1/4", "1/8", "1/16"]),
        _p("quartic", {"odE1": "1/30720", "odRatio": "16, 16", "odOrder": "4"},
           f="t^4", t0=0, y0=0, T=1, exact="t^5/5", hs=["1/4", "1/8", "1/16"]),
        _p("growth", {"odE1": "≈ 7.18893e-5", "odRatio": "≈ 14.4239, ≈ 15.1898", "odOrder": "≈ 3.92503"}, f="y", t0=0, y0=1, T=1, exact="e^t", hs=["1/4", "1/8", "1/16"])]}),
    # 3.10: 5/4, 105/64, 37905/16384; y(3/4) = 4; the budget stops after step 11.
    ("3.10", {"mode": "euler", "presets": [
        _p("square", {"euLast": "37905/16384", "euExact": "4", "euError": "27631/16384"},
           f="y^2", t0=0, y0=1, h="1/4", n=3, exact="1/(1 - t)"),
        _p("past", {"euExact": "undefined at t = 5/4"}, f="y^2", t0=0, y0=1, h="1/4", n=5, exact="1/(1 - t)"),
        _p("budget", {"euStopped": "stopped after step 11: digit budget"},
           f="y^2", t0=0, y0=1, h="1/4", n=16, exact="1/(1 - t)")]}),
    # 4.1: y²/2 = t²/2 + 2; −1/y = t²/2 − 1; y³ = t² + t + 1.
    ("4.1", {"mode": "separable", "view": "solve", "presets": [
        _p("circle", {"spG": "y²/2", "spC": "2", "spImplicit": "y² = t² + 4"}, g="y", h="t", ic=[0, 2]),
        _p("recip", {"spG": "−1/y", "spC": "−1", "spImplicit": "−1/y = t²/2 − 1"}, g="1/y^2", h="t", ic=[0, 1]),
        _p("poly", {"spG": "y³", "spC": "1", "spImplicit": "y³ = t² + t + 1"}, g="3y^2", h="2t + 1", ic=[0, 1])]}),
    ("4.2", {"mode": "separable", "view": "check", "presets": [
        _p("circle", {"spCheck": "equal", "spImplicit": "y² = t² + 4"}, g="y", h="t", ic=[0, 2]),
        _p("recip", {"spCheck": "equal", "spImplicit": "−1/y = t²/2 − 1"}, g="1/y^2", h="t", ic=[0, 1]),
        _p("poly", {"spCheck": "equal", "spImplicit": "y³ = t² + t + 1"}, g="3y^2", h="2t + 1", ic=[0, 1])]}),
    # 4.3: y(0) = −2 picks the lower branch; y² = 1 − t²; y = 1/(1 − t).
    ("4.3", {"mode": "separable", "view": "solve", "presets": [
        _p("lower", {"spExplicit": "y = −√(t² + 4)", "spDomain": "all t"}, g="y", h="t", ic=[0, -2]),
        _p("hyperbola", {"spExplicit": "y = √(1 − t²)", "spDomain": "−1 < t < 1"}, g="y", h="-t", ic=[0, 1]),
        _p("blow", {"spExplicit": "y = 1/(1 − t)", "spDomain": "t < 1"}, g="1/y^2", h="1", ic=[0, 1])]}),
    # 4.4: (5/4)⁴ = 625/256; factor 9/8; (17/16)¹⁶ ≈ 2.63793.
    ("4.4", {"mode": "growth", "presets": [
        _p("unit", {"grFactor": "5/4", "grLast": "625/256", "grTrue": "≈ 2.71828"}, k=1, y0=1, A=0, h="1/4", n=4,
           target=None),
        _p("half", {"grFactor": "9/8", "grLast": "43046721/8388608", "grTrue": "≈ 5.43656"},
           k="1/2", y0=2, A=0, h="1/4", n=8, target=None),
        _p("fine", {"grFactor": "17/16", "grLast": "48661191875666868481/18446744073709551616", "grTrue": "≈ 2.71828"},
           k=1, y0=1, A=0, h="1/16", n=16, target=None)]}),
    # 4.5: (9/8)⁶ ≈ 2.027 ≥ 2 first; (7/8)⁶ ≈ 0.449 ≤ 1/2 first; 1.1⁸ ≈ 2.14 ≥ 2 first.
    ("4.5", {"mode": "growth", "presets": [
        _p("double", {"grT": "≈ 1.38629", "grHit": "step 6 (t = 3/2)"}, k="1/2", y0=1, A=0, h="1/4", n=8, target=2),
        _p("halve", {"grT": "≈ 1.38629", "grHit": "step 6 (t = 3/2)"}, k="-1/2", y0=8, A=0, h="1/4", n=8, target=4),
        _p("slow", {"grT": "≈ 6.93147", "grHit": "step 8 (t = 8)"}, k="1/10", y0=1, A=0, h=1, n=16, target=2)]}),
    # 4.6: 1 − 300/25000 = 247/250; ln 2/(3/25000) ≈ 5776.23.
    ("4.6", {"mode": "growth", "presets": [
        _p("carbon", {"grFactor": "247/250", "grT": "≈ 5776.23"}, k="-3/25000", y0=1, A=0, h=100, n=64, target="1/2"),
        _p("quarter", {"grFactor": "247/250", "grT": "≈ 5776.23"}, k="-3/25000", y0=1, A=0, h=100, n=64,
           target="1/4"),
        _p("fast", {"grFactor": "3/4", "grT": "≈ 2.77259"}, k="-1/4", y0=100, A=0, h=1, n=8, target=50)]}),
    # 4.7: 20 + 80·(3/4)⁴ = 725/16; 20 + 80·e^(−1) ≈ 49.4305.
    ("4.7", {"mode": "growth", "presets": [
        _p("coffee", {"grSteady": "20", "grLast": "725/16", "grTrue": "≈ 49.4304"}, k="-1/4", y0=100, A=20, h=1, n=4,
           target=None),
        _p("warming", {"grSteady": "20", "grLast": "1212305/65536"}, k="-1/2", y0=5, A=20, h="1/2", n=8, target=None),
        _p("fridge", {"grSteady": "4"}, k="-1/10", y0=25, A=4, h=1, n=8, target=None)]}),
    # 4.8: 200·(1 − e^(−1/2)) ≈ 78.6939.
    ("4.8", {"mode": "growth", "presets": [
        _p("tank", {"grSteady": "200", "grTrue": "≈ 78.6939", "grFactor": "19/20"}, k="-1/20", y0=0, A=200, h=1,
           n=10, target=None),
        _p("flush", {"grSteady": "0"}, k="-1/10", y0=50, A=0, h=1, n=10, target=None),
        _p("salt", {"grSteady": "300"}, k="-1/50", y0=100, A=300, h=1, n=10, target=None)]}),
    # 4.9: 11/8, 935/512, …; equilibria 0 and 4; f′ = 1 − y/2 is 0 at 2.
    ("4.9", {"mode": "autonomous", "view": "steps", "presets": [
        _p("four", {"auEquil": "0, 4", "auTypes": "0 unstable; 4 stable", "auInflect": "y = 2",
                    "auSteps": "11 exact steps, then digit budget"},
           f=LOGI, starts=[1], h="1/2", n=12, window=[6, -1, 7]),
        _p("above", {"auEquil": "0, 4", "auLimit": "→ 4", "auInflect": "y = 2"},
           f=LOGI, starts=[6], h="1/2", n=12, window=[6, -1, 7]),
        _p("small", {"auEquil": "0, 10", "auTypes": "0 unstable; 10 stable", "auInflect": "y = 5"},
           f="y(1 - y/10)", starts=["1/2"], h="1/2", n=12, window=[12, -1, 12])]}),
    # 4.10: y² − 4y + 3 = 0 at 1, 3; (y − 2)² at H = 1; none at H = 5/4.
    ("4.10", {"mode": "autonomous", "view": "line", "presets": [
        _p("light", {"auEquil": "1, 3", "auTypes": "1 unstable; 3 stable"},
           f=LOGI + " - 3/4", starts=[2], h="1/4", n=8, window=[6, -1, 5]),
        _p("critical", {"auEquil": "2", "auTypes": "2 semistable"},
           f=LOGI + " - 1", starts=[3], h="1/4", n=8, window=[6, -1, 5]),
        _p("heavy", {"auEquil": "none", "auTypes": "none"},
           f=LOGI + " - 5/4", starts=[2], h="1/4", n=8, window=[6, -1, 5])]}),
    ("5.1", {"mode": "autonomous", "view": "line", "presets": [
        _p("quad", {"auEquil": "−1, 1"}, f="y^2 - 1", starts=[0], h="1/4", n=8, window=[4, -3, 3]),
        _p("cubic", {"auEquil": "0, 1, 3"}, f=CUBIC, starts=[2], h="1/4", n=8, window=[4, -1, 4]),
        _p("golden", {"auEquil": "(1 ± √5)/2"}, f="y^2 - y - 1", starts=[0], h="1/4", n=8, window=[4, -2, 3])]}),
    # 5.2: f(−1) = −8, f(1/2) = 5/8, f(2) = −2, f(4) = 12.
    ("5.2", {"mode": "autonomous", "view": "line", "presets": [
        _p("cubic", {"auEquil": "0, 1, 3", "auTypes": "0 unstable; 1 stable; 3 unstable"},
           f=CUBIC, starts=[2], h="1/4", n=8, window=[4, -1, 4]),
        _p("quad", {"auEquil": "−1, 1", "auTypes": "−1 stable; 1 unstable"},
           f="y^2 - 1", starts=[0], h="1/4", n=8, window=[4, -3, 3]),
        _p("single", {"auEquil": "2", "auTypes": "2 stable"}, f="2 - y", starts=[0], h="1/4", n=8, window=[4, -1, 4])]}),
    # 5.3: y²(1 − y) is positive on both sides of 0.
    ("5.3", {"mode": "autonomous", "view": "line", "presets": [
        _p("cubic", {"auTypes": "0 unstable; 1 stable; 3 unstable", "auSlope": "f′(0) = 3; f′(1) = −2; f′(3) = 6"},
           f=CUBIC, starts=[2], h="1/4", n=8, window=[4, -1, 4]),
        _p("semi", {"auTypes": "0 semistable; 1 stable", "auSlope": "f′(0) = 0; f′(1) = −1"},
           f="y^2 - y^3", starts=["1/2"], h="1/4", n=8, window=[4, -1, 2]),
        _p("quad", {"auTypes": "−1 stable; 1 unstable", "auSlope": "f′(−1) = −2; f′(1) = 2"},
           f="y^2 - 1", starts=[0], h="1/4", n=8, window=[4, -3, 3])]}),
    ("5.4", {"mode": "autonomous", "view": "line", "presets": [
        _p("cubic", {"auSlope": "f′(0) = 3; f′(1) = −2; f′(3) = 6", "auTypes": "0 unstable; 1 stable; 3 unstable"},
           f=CUBIC, starts=[2], h="1/4", n=8, window=[4, -1, 4]),
        _p("flat-unstable", {"auSlope": "f′(0) = 0", "auTypes": "0 unstable"},
           f="y^3", starts=["1/2"], h="1/4", n=8, window=[4, -2, 2]),
        _p("flat-stable", {"auSlope": "f′(0) = 0", "auTypes": "0 stable"},
           f="-y^3", starts=["1/2"], h="1/4", n=8, window=[4, -2, 2])]}),
    # 5.5: from 4 with h = 1/4: 4 + (1/4)·3 = 19/4, then 409/64.
    ("5.5", {"mode": "autonomous", "view": "steps", "presets": [
        _p("two", {"auLimit": "→ 1", "auSteps": "11 exact steps, then digit budget"},
           f=TWO, starts=[0, 2, 4], h="1/4", n=12, window=[3, -1, 6]),
        _p("cubic", {"auLimit": "→ 1", "auSteps": "7 exact steps, then digit budget"},
           f=CUBIC, starts=["1/2", 2, "7/2"], h="1/4", n=12, window=[3, -1, 5]),
        _p("quad", {"auLimit": "→ −1", "auSteps": "11 exact steps, then digit budget"},
           f="y^2 - 1", starts=[-2, 0, 2], h="1/4", n=12, window=[3, -3, 4])]}),
    # 5.6: a + y² at a = −4 is y² − 4; the discriminant −4a is 0 at a = 0.
    ("5.6", {"mode": "bifurcate", "presets": [
        _p("saddle-node", {"bfEquil": "−2, 2", "bfCount": "2 equilibria", "bfCritical": "a = 0"},
           f="a + y^2", a=-4, range=[-4, 1]),
        _p("at-zero", {"bfEquil": "0", "bfCount": "1 equilibrium", "bfCritical": "a = 0"},
           f="a + y^2", a=0, range=[-4, 1]),
        _p("gone", {"bfEquil": "none", "bfCount": "no equilibria", "bfCritical": "a = 0"},
           f="a + y^2", a=1, range=[-4, 1])]}),
    # 5.7: y(a − y²) at a = 4: −2, 0, 2.
    ("5.7", {"mode": "bifurcate", "presets": [
        _p("pitchfork", {"bfEquil": "−2, 0, 2", "bfTypes": "−2 stable; 0 unstable; 2 stable", "bfCritical": "a = 0"},
           f="a y - y^3", a=4, range=[-2, 4]),
        _p("pitchfork-before", {"bfEquil": "0", "bfTypes": "0 stable", "bfCritical": "a = 0"},
           f="a y - y^3", a=-1, range=[-2, 4]),
        _p("transcritical", {"bfEquil": "0, 2", "bfTypes": "0 unstable; 2 stable", "bfCritical": "a = 0"},
           f="a y - y^2", a=2, range=[-2, 4])]}),
    # 5.8: y″ = (2y − 4)·f(y) changes sign at y = 2; 3y² − 8y + 3 has irrational roots.
    ("5.8", {"mode": "autonomous", "view": "curves", "presets": [
        _p("two", {"auInflect": "y = 2", "auEquil": "1, 3"},
           f=TWO, starts=[0, "3/2", "5/2", 4], h="1/4", n=8, window=[3, -1, 5]),
        _p("logistic", {"auInflect": "y = 2", "auEquil": "0, 4"},
           f=LOGI, starts=["1/2", 1, 6], h="1/2", n=8, window=[8, -1, 7]),
        _p("cubic", {"auInflect": "none rational", "auEquil": "0, 1, 3"},
           f=CUBIC, starts=["1/2", 2, "7/2"], h="1/4", n=8, window=[3, -1, 5])]}),
]

TILES = {
    "verify": ("vfPreset", ["vfOrder", "vfLinear", "vfResidual", "vfVerdict", "vfIC", "vfFamily"], "vfStatus"),
    "field": ("sfPreset", ["sfSlope", "sfSign", "sfZero", "sfEquil"], "sfStatus"),
    "euler": ("euPreset", ["euLast", "euLastDec", "euExact", "euError", "euDigits", "euStopped"], "euStatus"),
    "order": ("odPreset", ["odE1", "odE2", "odE3", "odRatio", "odOrder"], "odStatus"),
    "separable": ("spPreset", ["spG", "spH", "spC", "spImplicit", "spExplicit", "spDomain", "spCheck"], "spStatus"),
    "growth": ("grPreset", ["grFactor", "grLast", "grTrue", "grError", "grT", "grHit", "grSteady"], "grStatus"),
    "autonomous": ("auPreset", ["auEquil", "auTypes", "auSlope", "auLimit", "auSteps", "auInflect"], "auStatus"),
    "bifurcate": ("bfPreset", ["bfEquil", "bfTypes", "bfCount", "bfCritical"], "bfStatus"),
}

# ES5: one inline <script> carries every lab and the quiz, so a construct an
# older parser rejects kills the page. BigInt literals are allowed, as
# RATIONAL_JS uses them.
NOT_ES5 = [
    (re.compile(r"=>"), "arrow function"),
    (re.compile(r"(^|[\s;{(])(let|const)\s"), "let/const"),
    (re.compile(r"\bclass\s+[A-Za-z_$][\w$]*\s*(extends\b|\{)"), "class"),
    (re.compile(r"`"), "template literal"),
    (re.compile(r"\?\."), "optional chaining"),
    (re.compile(r"\?\?"), "nullish coalescing"),
    (re.compile(r"\(\?<[=!]"), "lookbehind"),
    (re.compile(r"\.\.\.[A-Za-z_\[]"), "spread"),
    (re.compile(r"\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon|importScripts)\b"), "network"),
]


def build(cfg, **extra):
    return labs.build("dekit", dict(cfg, **extra))


def own_script(script):
    """What de_core and dekit add to a page: algebra_core's blocks, which
    predate the no-double-quote rule, taken out."""
    for block in de_core.ALGEBRA_BLOCKS:
        script = script.replace(block, "")
    return script


class EveryLessonBuilds(unittest.TestCase):
    def test_every_mode_is_covered(self):
        self.assertEqual({cfg["mode"] for _, cfg in FIXTURES}, set(dekit.MODES))

    def test_every_section_c_lesson(self):
        for key, cfg in FIXTURES:
            mode = cfg["mode"]
            with self.subTest(lesson=key, mode=mode):
                lab = build(cfg)
                select, tiles, status = TILES[mode]
                html = lab.markup + lab.controls
                self.assertIn('id="%s"' % select, html)
                for tile in tiles:
                    self.assertIn('<strong id="%s">' % tile, html)
                self.assertIn('id="%s"' % status, html)
                for p in cfg["presets"]:
                    self.assertIn('<option value="%s"' % p["id"], html)
                    self.assertTrue(p["expect"], "%s %s pins nothing" % (key, p["id"]))
                    for tile in p["expect"]:
                        self.assertIn('<strong id="%s">' % tile, html, "%s pins a tile the page lacks" % p["id"])
                self.assertEqual(set(lab.expect), {select})
                self.assertEqual(set(lab.expect[select]), {p["id"] for p in cfg["presets"]})
                self.assertIn("window.redrawLab = redraw", lab.script)
                self.assertIn("DE_refuse(", lab.script)
                ids = re.findall(r'\bid="([^"]+)"', html)
                self.assertEqual(sorted({i for i in ids if ids.count(i) > 1}), [])

    def test_script_is_es5_apart_from_bigint(self):
        blocks = [dekit.DK_JS] + list(dekit.MODE_JS.values())
        blocks += [own_script(build(cfg).script) for _, cfg in FIXTURES]
        for i, js in enumerate(blocks):
            for rx, what in NOT_ES5:
                self.assertIsNone(rx.search(js), "%s in block %d" % (what, i))

    def test_no_double_quote_in_what_de_core_and_dekit_add(self):
        for block in [dekit.DK_JS] + list(dekit.MODE_JS.values()):
            self.assertNotIn('"', block)
        for key, cfg in FIXTURES:
            with self.subTest(lesson=key):
                self.assertNotIn('"', own_script(build(cfg).script))

    def test_each_preset_can_be_shipped(self):
        for key, cfg in FIXTURES:
            for p in cfg["presets"]:
                with self.subTest(lesson=key, preset=p["id"]):
                    lab = build(cfg, preset=p["id"])
                    self.assertIn('<option value="%s" selected>' % p["id"], lab.controls)

    def test_no_shipped_value_holds_markup_characters(self):
        for key, cfg in FIXTURES:
            lab = build(cfg)
            for value in re.findall(r'<input [^>]*value="([^"]*)"', lab.controls):
                with self.subTest(lesson=key, value=value):
                    self.assertFalse(set(value) & set("<>&"), value)

    def test_per_mode_assembly(self):
        """A page carries the blocks its mode calls, and no other mode's code."""
        names = {"verify": "vfCompute", "field": "sfCompute", "euler": "euCompute", "order": "odCompute",
                 "separable": "spCompute", "growth": "grCompute", "autonomous": "auCompute",
                 "bifurcate": "bfCompute"}
        needs = {"verify": ["MPparse", "EPfamily", "RFderiv", "DE_arrows"],
                 "field": ["MPparse", "RFtext", "quadroots", "DK_roots", "DE_arrows", "DE_rk4float"],
                 "euler": ["DE_euler", "EPparse", "RFeval", "DK_poleBetween", "DK_ratroots"],
                 "order": ["DE_heun", "DE_rk4", "DK_closed"],
                 "separable": ["Pintegral", "RFderiv", "DK_roots", "quadroots", "DE_rk4float"],
                 "growth": ["DE_dec", "DE_polyline"],
                 "autonomous": ["DE_euler", "DK_phase", "quadroots", "NumberLine"],
                 "bifurcate": ["DK_phase", "MPparse", "quadroots"]}
        for key, cfg in FIXTURES:
            script = build(cfg).script
            with self.subTest(lesson=key):
                for mode, fn in names.items():
                    (self.assertIn if mode == cfg["mode"] else self.assertNotIn)("function %s(" % fn, script)
                for fn in needs[cfg["mode"]]:
                    self.assertIn("function %s(" % fn, script)
        by = dict(FIXTURES)
        self.assertNotIn("function EPparse(", build(by["4.4"]).script)   # growth: SHOW and DRAW only
        self.assertNotIn("function MPparse(", build(by["4.4"]).script)
        self.assertNotIn("function DK_closed(", build(by["5.1"]).script)
        self.assertNotIn("function DE_euler(", build(by["3.1"]).script)
        self.assertNotIn("function quadroots(", build(by["3.6"]).script)   # euler: no surds
        self.assertNotIn("function DK_phase(", build(by["3.7"]).script)

    def test_redraw_only_defaults_come_from_cfg(self):
        by = dict(FIXTURES)
        self.assertIn('<option value="15" selected>', build(by["3.4"]).controls)
        self.assertIn('<option value="heun" selected>', build(by["3.8"]).controls)
        self.assertIn('<option value="rk4" selected>', build(by["3.9"]).controls)
        self.assertIn('<option value="check" selected>', build(by["4.2"]).controls)
        self.assertIn('<option value="curves" selected>', build(by["5.8"]).controls)
        self.assertIn('<option value="line" selected>', build(by["5.1"]).controls)


class Refusals(unittest.TestCase):
    def bad(self, cfg, needle):
        with self.assertRaises(ValueError) as ctx:
            labs.build("dekit", cfg)
        self.assertIn(needle, str(ctx.exception))

    def test_unknown_mode(self):
        self.bad({"mode": "integrate", "presets": [_p("x", f="t")]}, "no mode")

    def test_unknown_preset(self):
        self.bad(dict(FIXTURES[0][1], preset="nope"), "no preset 'nope'")

    def test_malformed_instances_name_the_preset(self):
        self.bad({"mode": "verify", "presets": [_p("eq", equation="y' 2t", candidate="t")]}, "'eq'")
        self.bad({"mode": "field", "presets": [_p("win", f="t", window=[3, -3, 0, 1], point=[0, 0])]}, "'win'")
        self.bad({"mode": "euler", "presets": [_p("n", f="y", t0=0, y0=1, h="1/4", n=65)]}, "'n'")
        self.bad({"mode": "euler", "presets": [_p("h", f="y", t0=0, y0=1, h="-1/4", n=4)]}, "'h'")
        self.bad({"mode": "order", "method": "rk4",
                  "presets": [_p("cap", f="y", t0=0, y0=1, T=4, exact="e^t", hs=["1/4", "1/8", "1/16"])]}, "'cap'")
        self.bad({"mode": "order", "presets": [_p("whole", f="y", t0=0, y0=1, T=1, exact="e^t",
                                                  hs=["1/3", "2/5", "1/16"])]}, "'whole'")
        self.bad({"mode": "separable", "presets": [_p("g", g="sin(y)", h="t", ic=None)]}, "'g'")
        self.bad({"mode": "growth", "presets": [_p("k0", k=0, y0=1, h=1, n=4)]}, "'k0'")
        self.bad({"mode": "autonomous", "presets": [_p("st", f="y", starts=[], h=1, n=4, window=[1, 0, 1])]}, "'st'")
        self.bad({"mode": "bifurcate", "presets": [_p("rg", f="a + y^2", a=0, range=[1, -1])]}, "'rg'")

    def test_bad_redraw_only_values(self):
        by = dict(FIXTURES)
        self.bad(dict(by["3.7"], method="midpoint"), "method")
        self.bad(dict(by["4.1"], view="graph"), "view")
        self.bad(dict(by["3.4"], grid=12), "grid")

    def test_missing_expect_is_not_a_build_error(self):
        build({"mode": "growth", "presets": [{"id": "x", "label": "x", "k": 1, "y0": 1, "h": 1, "n": 2}]})


# ---------------------------------------------------------------------------
# The arithmetic: each preset's own page script, run against a stub document
# with every control at the value the markup ships, then each pinned tile read
# back. scripts/labcheck.js --expect on rendered fixture pages is the full gate
# (sweep included); this is the same check in a second.
# ---------------------------------------------------------------------------

PAGE_RUNNER = r"""
var vm = require('vm');
var jobs = JSON.parse(require('fs').readFileSync(0, 'utf8')), fails = [], seen = {};
function El(id, value) {
  this.id = id; this.value = value === undefined ? '' : value; this.textContent = ''; this.innerHTML = '';
  this.style = {}; this.attrs = {}; this.listeners = {};
}
El.prototype.addEventListener = function (k, fn) { (this.listeners[k] = this.listeners[k] || []).push(fn); };
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return k in this.attrs ? this.attrs[k] : null; };
El.prototype.appendChild = function (c) { return c; };
El.prototype.remove = function () {};
jobs.forEach(function (job) {
  var els = {};
  Object.keys(job.values).forEach(function (id) { els[id] = new El(id, job.values[id]); });
  var doc = {
    getElementById: function (id) { return els[id] || null; },
    createElementNS: function () { return new El(''); },
    createElement: function () { return new El(''); }
  };
  var box = { document: doc, Math: Math, console: console };
  box.window = box;
  try {
    vm.runInNewContext(job.script, box, { timeout: 20000 });
  } catch (e) { fails.push(job.name + ': ' + e.message); return; }
  var got = {};
  job.tiles.forEach(function (tile) { got[tile] = els[tile] ? els[tile].textContent : '(no tile)'; });
  seen[job.name] = got;
  Object.keys(job.expect).forEach(function (tile) {
    if (got[tile] !== job.expect[tile]) fails.push(job.name + ' #' + tile + ': got ' + got[tile] + ', want ' + job.expect[tile]);
  });
  if (/Refused/.test(els[job.status].innerHTML)) fails.push(job.name + ': ' + els[job.status].innerHTML);
});
if (process.env.DEKIT_SHOW) console.error(JSON.stringify(seen, null, 1));
console.log(fails.length ? fails.join('\n') : 'OK');
"""


def _values(html):
    out = {}
    for m in re.finditer(r'<(input|select|div|strong|span|svg|label)\b([^>]*)>', html):
        idm = re.search(r'\bid="([^"]+)"', m.group(2))
        if idm:
            val = re.search(r'\bvalue="([^"]*)"', m.group(2))
            out[idm.group(1)] = val.group(1) if (val and m.group(1) == "input") else ""
    for m in re.finditer(r'<select id="([^"]+)">(.*?)</select>', html):
        chosen = re.search(r'<option value="([^"]*)" selected>', m.group(2)) or \
            re.search(r'<option value="([^"]*)"', m.group(2))
        out[m.group(1)] = chosen.group(1) if chosen else ""
    return out


def page_jobs():
    jobs = []
    for key, cfg in FIXTURES:
        for p in cfg["presets"]:
            lab = build(cfg, preset=p["id"])
            select, tiles, status = TILES[cfg["mode"]]
            jobs.append({"name": "%s %s/%s" % (key, cfg["mode"], p["id"]), "script": lab.script,
                         "values": _values(lab.markup + lab.controls), "expect": p["expect"],
                         "tiles": tiles, "status": status})
    return jobs


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class EveryPresetPrintsItsFigures(unittest.TestCase):
    def test_each_page_script_prints_the_pinned_tiles(self):
        run = subprocess.run(["node", "-e", PAGE_RUNNER], input=json.dumps(page_jobs()), capture_output=True,
                             text=True, timeout=240)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")


# ---------------------------------------------------------------------------
# The shared helpers, by running the shipped blocks: cases a wrong
# implementation passes by accident.
# ---------------------------------------------------------------------------

ARITH = r"""
var out = [];
function eq(label, got, want) { if (String(got) !== String(want)) out.push(label + ': got ' + got + ', want ' + want); }
function Q(s) { return DE_rat(s); }
function P(list) { return list.map(Q); }
/* DK_ratroots: POLY_JS misses 4 in y − y²/4 (constant term 0) */
eq('ratroots', DK_ratroots(P(['0', '1', '-1/4'])).map(DE_q).join(','), '0,4');
eq('ratroots double zero', DK_ratroots(P(['0', '0', '-12', '3'])).map(DE_q).join(','), '0,4');
/* DK_roots: rational roots, then a surd pair; the open case */
var rr = DK_roots(P(['0', '-1', '-1', '1']));               /* y³ − y² − y = y(y² − y − 1) */
eq('roots list', rr.list.map(function (x) { return x.text; }).join(' | '), '(1 − √5)/2 | 0 | (1 + √5)/2');
eq('roots text', DK_eqText(rr), '0, (1 ± √5)/2');
eq('roots open', DK_roots(P(['-2', '0', '0', '1'])).open, true);   /* y³ − 2 */
eq('roots prefix', DK_eqText(DK_roots(P(['-2', '0', '1'])), 'y = '), 'y = −√2, y = √2');
/* DK_rootOne and DK_surdEval: f′ = 2y − 1 at (1 − √5)/2 is −√5 */
eq('rootOne', DK_rootOne(Q('1/2'), Q('-3/2'), 2n), '(1 − 3√2)/2');
var ph = DK_phase(P(['-1', '-1', '1']));
eq('phase golden types', DK_typesText(ph), '(1 − √5)/2 stable; (1 + √5)/2 unstable');
eq('phase golden slopes', ph.slopes.join('; '), '−√5; √5');
/* DK_phase: semistable from equal signs; the double root of (y − 2)² */
eq('phase semi', DK_typesText(DK_phase(P(['0', '0', '1', '-1']))), '0 semistable; 1 stable');
eq('phase double', DK_typesText(DK_phase(P(['4', '-4', '1']))), '2 semistable');
eq('phase none', DK_typesText(DK_phase(P(['5', '-4', '1']))), 'none');
eq('limit up', DK_limit(DK_phase(P(['3', '-4', '1'])), Q('4')), '→ +∞');
eq('limit down', DK_limit(DK_phase(P(['3', '-4', '1'])), Q('2')), '→ 1');
eq('limit at', DK_limit(DK_phase(P(['3', '-4', '1'])), Q('3')), 'at equilibrium');
eq('limit surd', DK_limit(DK_phase(P(['-1', '-1', '1'])), Q('0')), '→ (1 − √5)/2');
/* DK_ptext and DK_big */
eq('ptext', DK_ptext(P(['1', '0', '-1']), 't'), '1 − t²');
eq('ptext lead', DK_ptext(P(['-1', '0', '1']), 't'), 't² − 1');
eq('big', DK_big(R(10n ** 60n + 1n, 3n)), '≈ 3.33333e59 (exact: 61 digits over 1)');
/* DK_poleBetween: the pole of 1/(1 − t) lies between 0 and 5/4, not between 0 and 3/4 */
eq('pole past', DK_poleBetween(P(['-1', '1']), Q('0'), Q('5/4')), true);
eq('pole before', DK_poleBetween(P(['-1', '1']), Q('0'), Q('3/4')), false);
eq('pole at end', DK_poleBetween(P(['-1', '1']), Q('0'), Q('1')), true);
eq('pole surd', DK_poleBetween(P(['-2', '0', '1']), Q('0'), Q('3/2')), true);
eq('pole surd short', DK_poleBetween(P(['-2', '0', '1']), Q('0'), Q('7/5')), false);
eq('pole cubic', DK_poleBetween(P(['-2', '0', '0', '1']), Q('1'), Q('2')), true);
eq('pole zero', DK_poleBetween(P(['0', '0', '1', '1']), Q('-1/2'), Q('1/2')), true);
/* verify: the residual over RF and over EP, and the family fit */
eq('vf cube', vfCompute('y\' = 2t', 't^3', '').residual, '3t² − 2t');
eq('vf nonlinear', vfCompute('y\' = y^2', '1/(1 - t)', '').residual, '0');
eq('vf ep', vfCompute('y\'\' - y\' - 2y = 0', 'e^t', '').residual, '−2·e^t');
eq('vf variable coefficient', vfCompute('t y\' = 2y', 'C t^2', '1 3').family, 'C = 3 from y(1) = 3');
eq('vf fit', vfCompute('y\'\' + y = 0', 'C cos(t) + D sin(t)', '0 1 -2').family, 'C = 1, D = −2');
eq('vf ic fails', vfCompute('y\' = 2t', 't^2 + 3/2', '0 1').icText, 'fails: y(0) = 3/2');
eq('vf forced', vfCompute('y\' + 2y = 6', '3 + C e^(-2t)', '0 0').family, 'C = −3 from y(0) = 0');
eq('vf family residual', vfCompute('y\' = y', 't + C e^t', '').residual, '−t + 1');
eq('vf points', vfCompute('y\' = y^2', 'e^t', '').verdict, 'Checked at 5 points only');
/* order: a power of two prints an integer, anything else rounded */
eq('pow2', odPow2(Q('16')), 4);
eq('pow2 frac', odPow2(Q('1/8')), -3);
eq('pow2 not', odPow2(Q('92/47')), null);
/* separable */
var sp = spCompute('y', '-t', '0 1');
eq('sp hyperbola', sp.explicit + ' for ' + sp.domain, 'y = √(1 − t²) for −1 < t < 1');
sp = spCompute('1/y^2', 't', '0 1');
eq('sp recip', sp.explicit + ' for ' + sp.domain, 'y = 2/(2 − t²) for −√2 < t < √2');
sp = spCompute('2y + 2', '2t', '0 1');                       /* y² + 2y = t² + 3: y = −1 + √(t² + 4) */
eq('sp shifted', sp.explicit + '; ' + sp.check, 'y = −1 + √(t² + 4); equal');
sp = spCompute('1/y', '2t', '1 3');
eq('sp ln', sp.explicit + '; ' + sp.C, 'y = 3·e^(t² − 1); ln 3 − 1');
/* growth: the hit from below and from above */
eq('gr hit', grCompute('1/2', '1', '0', '1/4', 8, '2').hit, 'step 6 (t = 3/2)');
eq('gr never', grCompute('-3/25000', '1', '0', '100', 64, '1/4').hit, 'never within 64 steps');
eq('gr coffee', DE_q(grCompute('-1/4', '100', '20', '1', 4, '').last), '725/16');
/* autonomous: 5.5's worked steps from 4 with h = 1/4, and 4.9's from 1 with h = 1/2 */
var run = DE_euler(MPparse('y^2 - 4y + 3', ['y']), R0, Q('4'), Q('1/4'), 2);
eq('au steps two', run.rows.map(function (r) { return DE_q(r.y); }).join(', '), '4, 19/4, 409/64');
run = DE_euler(MPparse('y(1 - y/4)', ['y']), R0, Q('1'), Q('1/2'), 12);
eq('au steps four', DE_q(run.rows[1].y) + ', ' + DE_q(run.rows[2].y) + '; ' + run.steps + (run.stopped ? ' stopped' : ''), '11/8, 935/512; 11 stopped');
/* autonomous: the inflection rule */
eq('au inflect', auInflect(P(['3', '-4', '1']), P(['-4', '2'])), 'y = 2');
eq('au inflect irr', auInflect(P(['0', '3', '-4', '1']), P(['3', '-8', '3'])), 'none rational');
eq('au inflect eq', auInflect(P(['0', '0', '1', '-1']), P(['0', '2', '-3'])), 'y = 2/3');
eq('au inflect lin', auInflect(P(['2', '-1']), P(['-1'])), 'none');
/* bifurcate: discriminants from the resultant */
eq('bf saddle', DE_ptext(bfDisc(bfCoeffs(MPparse('a + y^2', ['y', 'a']))), 'a'), '4a');
eq('bf pitchfork', Prationalroots(bfDisc(bfCoeffs(MPparse('a y - y^3', ['y', 'a'])))).map(DE_q).join(','), '0');
eq('bf cubic', Prationalroots(bfDisc(bfCoeffs(MPparse('y^3 - 3y + a', ['y', 'a'])))).map(DE_q).join(','), '−2,2');
eq('bf two', bfCompute('y^2 - y + a', '0', '-1 1').crit, 'a = 1/4');
eq('bf end', bfCompute('a + y^2', '0', '0 1').crit, 'a = 0');
eq('bf none', bfCompute('y^2 + a', '-1', '1 2').crit, 'none rational in [1, 2]');
/* cases added after a mutation sweep found the ones above passing a broken function */
var sq = DK_surdEval(P(['0', '0', '1']), { p: Q('1/2'), q: Q('1/2'), k: 5n });
eq('surdEval square', DE_q(sq.a) + ' ' + DE_q(sq.b), '3/2 1/2');                 /* ((1 + √5)/2)² = (3 + √5)/2 */
eq('vf forced residual', vfCompute('y\' + 2y = 6', '3 + C e^(-2t)', '').residual, '0');
eq('vf forced wrong', vfCompute('y\' + 2y = 6', '2 + C e^(-2t)', '').residual, '−2');
eq('vf product nonlinear', vfEquation('y y\'\' = 1').linear, false);
eq('vf fit from y prime', vfCompute('y\'\' = 0', 'C t + 1', '0 1 3').family, 'C = 3 from y′(0) = 3');
eq('sf equil gcd', sfCompute('t y^2 - t y + y - 1', '-3 3 -3 3', '', '0 0').equil, 'y = 1');
eq('sf equil t y', sfCompute('t y', '-3 3 -3 3', '', '1 1').equil, 'y = 0');
eq('sp recip negative', spCompute('1/y^2', 't', '0 -1').explicit, 'y = −2/(t² + 2)');
eq('sp nearest roots', spCompute('1/y^2', '4t^3 - 10t', '0 -1/4').domain, '−1 < t < 1');
eq('sp C at t0', spCompute('y', 't', '1 2').implicit, 'y² = t² + 3');
eq('gr hit exactly', grCompute('1', '1', '0', '1', 4, '4').hit, 'step 2 (t = 2)');
eq('au inflect all excluded', auInflect(P(['4', '-4', '1']), P(['-4', '2'])), 'none');
console.log(out.length ? out.join('\n') : 'OK');
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class Arithmetic(unittest.TestCase):
    def test_shipped_blocks_compute_the_worked_figures(self):
        src = de_core.script("SURD", "MPOLY", "RF", "EP", "STEP", "DRAW",
                             extra=dekit.DK_JS + "".join(dekit.MODE_JS.values()))
        run = subprocess.run(["node", "-"], input=src + ARITH, capture_output=True, text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")


if __name__ == "__main__":
    unittest.main()
