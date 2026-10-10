"""dekit's second half (linear1, stiff, char, oscillator, phase, jacobian, laplace).

Built from the presets docs/differential-equations/PLAN.md section C names, each
through labs.build("dekit", cfg). Fast and browserless: the markup and script
are checked for the controls and tiles D.3 names, for ES5 and for the absence
of a double quote in everything dekit_b and de_core add to a page; then each
preset's own page script is run against a stub document (node) and every
pinned tile is compared. The pinned figures were read off rendered fixture
pages with `node scripts/labcheck.js --observe` and checked by hand against
section C. FIXTURES is importable, so a fixture page can be rendered and gated
by labcheck.js --expect.
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
from mathpath.labs import de_core, dekit_b  # noqa: E402


def _p(pid, expect=None, **fields):
    out = {"id": pid, "label": pid.replace("-", " ")}
    out.update(fields)
    out["expect"] = expect or {}
    return out


# (section C lesson, cfg). One entry per lesson that uses these modes.
FIXTURES = [
    ("6.1", {"mode": "linear1", "view": "solve", "presets": [
        _p("scaled", {"lfMu": "e^(3t)", "lfYh": "C·e^(−3t)"}, equation="2y' + 6y = 4t", ic=None),
        _p("power", {"lfMu": "1/t²", "lfYh": "C·t²"}, equation="t y' - 2y = 0", ic=None),
        _p("constant", {"lfMu": "e^(2t)", "lfYh": "C·e^(−2t)", "lfSteady": "2"}, equation="y' = 4 - 2y", ic=None)]}),
    ("6.2", {"mode": "linear1", "view": "steps", "presets": [
        _p("three", {"lfSteady": "3", "lfSolution": "y = 3 − 3·e^(−2t)", "lfLast": "45/16"},
           equation="y' + 2y = 6", ic=[0, 0], h="1/4", n=4),
        _p("from-above", {"lfSteady": "3", "lfSolution": "y = 3 + 2·e^(−2t)", "lfLast": "25/8"},
           equation="y' + 2y = 6", ic=[0, 5], h="1/4", n=4),
        _p("negative", {"lfSteady": "−2 (repelling)", "lfSolution": "y = −2 + 2·e^t", "lfLast": "369/128"},
           equation="y' - y = 2", ic=[0, 0], h="1/4", n=4)]}),
    ("6.3", {"mode": "linear1", "view": "solve", "presets": [
        _p("t-squared", {"lfMu": "t²", "lfSolution": "y = t³/5 + (4/5)/t²", "lfC": "4/5"},
           equation="y' + (2/t) y = t^2", ic=[1, 1]),
        _p("exp", {"lfMu": "e^(2t)", "lfSolution": "y = (1/3)·e^t + C·e^(−2t)", "lfC": "—"},
           equation="y' + 2y = e^t", ic=None),
        _p("t-one", {"lfMu": "t", "lfSolution": "y = t/2 + (3/2)/t", "lfC": "3/2"},
           equation="y' + y/t = 1", ic=[1, 2])]}),
    ("6.4", {"mode": "linear1", "view": "parts", "presets": [
        _p("ramp", {"lfYh": "C·e^(−3t)", "lfYp": "(2/3)·t − 2/9", "lfC": "11/9"}, equation="y' + 3y = 2t", ic=[0, 1]),
        _p("constant", {"lfYh": "C·e^(−2t)", "lfYp": "3", "lfC": "—"}, equation="y' + 2y = 6", ic=None),
        _p("exp", {"lfYh": "C·e^(−2t)", "lfYp": "(1/3)·e^t", "lfC": "−1/3"}, equation="y' + 2y = e^t", ic=[0, 0])]}),
    ("6.5", {"mode": "linear1", "view": "parts", "presets": [
        _p("square", {"lfYp": "t² − 2t + 2"}, equation="y' + y = t^2", ic=None),
        _p("line", {"lfYp": "−2t − 1"}, equation="y' - 2y = 4t", ic=None),
        _p("cubic", {"lfYp": "t³ − 3t² + 6t − 6"}, equation="y' + y = t^3", ic=None)]}),
    ("6.6", {"mode": "linear1", "view": "parts", "presets": [
        _p("cosine", {"lfYp": "(2/5)·cos(t) + (1/5)·sin(t)",
                      "lfSolution": "y = (2/5)·cos(t) + (1/5)·sin(t) + C·e^(−2t)"}, equation="y' + 2y = cos(t)", ic=None),
        _p("exp", {"lfYp": "(1/3)·e^t", "lfSolution": "y = (1/3)·e^t + C·e^(−2t)"}, equation="y' + 2y = e^t", ic=None),
        _p("resonant", {"lfYp": "t·e^(−2t)", "lfSolution": "y = t·e^(−2t) + C·e^(−2t)"},
           equation="y' + 2y = e^(-2t)", ic=None)]}),
    ("6.7", {"mode": "linear1", "view": "solve", "presets": [
        _p("rc", {"lfSteady": "5/2", "lfSolution": "q = 5/2 − (5/2)·e^(−2t)"}, equation="q' + 2q = 5", ic=[0, 0]),
        _p("loan", {"lfSteady": "120 (repelling)", "lfSolution": "B = 120 − 20·e^(t/20)"},
           equation="B' - B/20 = -6", ic=[0, 100]),
        _p("tank", {"lfSteady": "200", "lfSolution": "y = 200 − 200·e^(−t/20)"}, equation="y' + y/20 = 10", ic=[0, 0])]}),
    ("6.8", {"mode": "stiff", "scheme": "forward", "presets": [
        _p("grows", {"skFactor": "−3/2", "skVerdict": "oscillates and grows", "skLimit": "h < 2/5", "skLast": "6561/256",
                     "skTrue": "≈ 2.06115e-9", "skBackward": "2/7"}, a=5, y0=1, h="1/2", n=8),
        _p("wobbles", {"skFactor": "−1/4", "skVerdict": "oscillates and decays", "skLimit": "h < 2/5"},
           a=5, y0=1, h="1/4", n=8),
        _p("fine", {"skFactor": "1/2", "skVerdict": "decays", "skLimit": "h < 2/5", "skLast": "1/256"},
           a=5, y0=1, h="1/10", n=8)]}),
    ("7.3", {"mode": "char", "view": "roots", "presets": [
        _p("distinct", {"ceDisc": "1", "ceKind": "two real roots", "ceRoots": "−2, −1"}, a=1, b=3, c=2, ic=None),
        _p("repeated", {"ceDisc": "0", "ceKind": "one repeated root", "ceRoots": "−2 (repeated)"}, a=1, b=4, c=4, ic=None),
        _p("complex", {"ceDisc": "−16", "ceKind": "complex pair", "ceRoots": "−1 ± 2i"}, a=1, b=2, c=5, ic=None),
        _p("surd", {"ceDisc": "5", "ceKind": "two real roots (irrational)", "ceRoots": "(1 ± √5)/2"},
           a=1, b=-1, c=-1, ic=None)]}),
    ("7.4", {"mode": "char", "view": "solution", "presets": [
        _p("decay", {"ceRoots": "−2, −1", "ceGeneral": "C₁·e^(−t) + C₂·e^(−2t)", "ceC": "C₁ = 2, C₂ = −1",
                     "ceSolution": "2·e^(−t) − e^(−2t)"}, a=1, b=3, c=2, ic=[1, 0]),
        _p("mixed", {"ceRoots": "−1, 1", "ceGeneral": "C₁·e^t + C₂·e^(−t)", "ceSolution": "e^(−t)"},
           a=1, b=0, c=-1, ic=[1, -1]),
        _p("grow", {"ceRoots": "2, 3", "ceGeneral": "C₁·e^(3t) + C₂·e^(2t)", "ceSolution": "−2·e^(3t) + 3·e^(2t)"},
           a=1, b=-5, c=6, ic=[1, 0])]}),
    ("7.5", {"mode": "char", "view": "solution", "presets": [
        _p("critical", {"ceKind": "one repeated root", "ceGeneral": "(C₁ + C₂·t)·e^(−2t)", "ceC": "C₁ = 1, C₂ = 3",
                        "ceSolution": "3·t·e^(−2t) + e^(−2t)"}, a=1, b=4, c=4, ic=[1, 1]),
        _p("zero-root", {"ceKind": "one repeated root", "ceGeneral": "C₁ + C₂·t", "ceC": "C₁ = 1, C₂ = 1"},
           a=1, b=0, c=0, ic=[1, 1]),
        _p("third", {"ceKind": "one repeated root", "ceGeneral": "(C₁ + C₂·t)·e^(−t/3)", "ceC": "C₁ = 1, C₂ = 1/3"},
           a=9, b=6, c=1, ic=[1, 0])]}),
    ("7.6", {"mode": "char", "view": "solution", "presets": [
        _p("damped", {"ceRoots": "−1 ± 2i", "ceGeneral": "e^(−t)·(C₁·cos(2t) + C₂·sin(2t))",
                      "ceSolution": "e^(−t)·sin(2t)"}, a=1, b=2, c=5, ic=[0, 2]),
        _p("pure", {"ceRoots": "±2i", "ceGeneral": "C₁·cos(2t) + C₂·sin(2t)", "ceSolution": "cos(2t)"},
           a=1, b=0, c=4, ic=[1, 0]),
        _p("growing", {"ceRoots": "1 ± i", "ceGeneral": "e^t·(C₁·cos(t) + C₂·sin(t))",
                       "ceSolution": "e^t·cos(t) − e^t·sin(t)"}, a=1, b=-2, c=2, ic=[1, 0])]}),
    ("7.7", {"mode": "char", "view": "solution", "presets": [
        _p("decay", {"ceC": "C₁ = 1, C₂ = −1", "ceSolution": "e^(−t) − e^(−2t)"}, a=1, b=3, c=2, ic=[0, 1]),
        _p("damped", {"ceC": "C₁ = 2, C₂ = 1", "ceSolution": "2·e^(−t)·cos(2t) + e^(−t)·sin(2t)"},
           a=1, b=2, c=5, ic=[2, 0]),
        _p("surd", {"ceC": "—", "ceSolution": "—"}, a=1, b=-1, c=-1, ic=[1, 0])]}),
    ("7.8", {"mode": "char", "view": "wronskian", "presets": [
        _p("decay", {"ceW": "−1"}, a=1, b=3, c=2, ic=None),
        _p("pure", {"ceW": "2"}, a=1, b=0, c=4, ic=None),
        _p("repeated", {"ceW": "1"}, a=1, b=4, c=4, ic=None),
        _p("surd", {"ceW": "−√5"}, a=1, b=-1, c=-1, ic=None)]}),
    ("8.1", {"mode": "oscillator", "view": "motion", "presets": [
        _p("unit", {"osType": "undamped", "osOmega0Sq": "4", "osOmega0": "2", "osPeriod": "π ≈ 3.14159"},
           m=1, c=0, k=4, ic=[1, 0]),
        _p("heavy", {"osType": "undamped", "osOmega0Sq": "5/2", "osOmega0": "√10/2 ≈ 1.58114",
                     "osPeriod": "4π/√10 ≈ 3.97384"}, m=2, c=0, k=5, ic=[1, 0]),
        _p("stiff", {"osType": "undamped", "osOmega0Sq": "9", "osPeriod": "2π/3 ≈ 2.0944"}, m=1, c=0, k=9, ic=[1, 0])]}),
    ("8.2", {"mode": "oscillator", "view": "motion", "presets": [
        _p("five", {"osAmpSq": "25", "osAmp": "5", "osPhase": "≈ 0.927295"}, m=1, c=0, k=4, ic=[3, 8]),
        _p("pure-cos", {"osAmpSq": "4", "osAmp": "2", "osPhase": "0"}, m=1, c=0, k=4, ic=[2, 0]),
        _p("surd", {"osAmpSq": "5/4", "osAmp": "√5/2 ≈ 1.11803"}, m=1, c=0, k=4, ic=[1, 1])]}),
    ("8.3", {"mode": "oscillator", "view": "phase", "presets": [
        _p("five", {"osEnergy": "50", "osAmpSq": "25"}, m=1, c=0, k=4, ic=[3, 8]),
        _p("pure-cos", {"osEnergy": "8", "osAmpSq": "4"}, m=1, c=0, k=4, ic=[2, 0]),
        _p("heavy", {"osEnergy": "5/2", "osAmpSq": "1"}, m=2, c=0, k=5, ic=[1, 0])]}),
    ("8.4", {"mode": "oscillator", "view": "motion", "presets": [
        _p("over", {"osType": "overdamped", "osDisc": "9", "osCcrit": "4"}, m=1, c=5, k=4, ic=[1, 0]),
        _p("critical", {"osType": "critically damped", "osDisc": "0", "osCcrit": "4"}, m=1, c=4, k=4, ic=[1, 0]),
        _p("under", {"osType": "underdamped", "osDisc": "−16", "osCcrit": "2√5 ≈ 4.47214"}, m=1, c=2, k=5, ic=[1, 0])]}),
    ("8.5", {"mode": "oscillator", "view": "motion", "presets": [
        _p("two-five", {"osOmegaD": "ω_d² = 4", "osEnvelope": "c/(2m) = 1; peaks shrink by ≈ 0.0432139"},
           m=1, c=2, k=5, ic=[2, 0]),
        _p("light", {"osOmegaD": "ω_d² = 63/16", "osEnvelope": "c/(2m) = 1/4; peaks shrink by ≈ 0.453116"},
           m=1, c="1/2", k=4, ic=[1, 0]),
        _p("heavy", {"osOmegaD": "ω_d² = 9/4", "osEnvelope": "c/(2m) = 1/2; peaks shrink by ≈ 0.123145"},
           m=2, c=2, k=5, ic=[1, 0])]}),
    ("8.6", {"mode": "oscillator", "view": "motion", "presets": [
        _p("no-cross", {"osType": "critically damped", "osCcrit": "4", "osDisc": "0", "osCross": "none for t > 0"},
           m=1, c=4, k=4, ic=[1, 1]),
        _p("one-cross", {"osType": "critically damped", "osCcrit": "4", "osDisc": "0", "osCross": "t = 1/3"},
           m=1, c=4, k=4, ic=[1, -5]),
        _p("compare-over", {"osType": "overdamped", "osCcrit": "4", "osDisc": "9"}, m=1, c=5, k=4, ic=[1, 0])]}),
    ("8.7", {"mode": "oscillator", "view": "motion", "presets": [
        _p("below", {"osForced": "A = 1"}, m=1, c=0, k=4, ic=[0, 0], F0=3, w=1),
        _p("above", {"osForced": "A = −3/5"}, m=1, c=0, k=4, ic=[0, 0], F0=3, w=3),
        _p("near", {"osForced": "A = 12/7"}, m=1, c=0, k=4, ic=[0, 0], F0=3, w="3/2")]}),
    ("8.8", {"mode": "oscillator", "view": "motion", "presets": [
        _p("resonant", {"osForced": "resonance: (3/4)·t·sin(2t)", "osPeriod": "π ≈ 3.14159"},
           m=1, c=0, k=4, ic=[0, 0], F0=3, w=2),
        _p("beats", {"osForced": "A = 12/7", "osPeriod": "4π ≈ 12.5664"}, m=1, c=0, k=4, ic=[0, 0], F0=3, w="3/2"),
        _p("far", {"osForced": "A = 4/5", "osPeriod": "4π/3 ≈ 4.18879"}, m=1, c=0, k=4, ic=[0, 0], F0=3, w="1/2")]}),
    ("8.9", {"mode": "oscillator", "view": "amplitude", "presets": [
        _p("curve", {"osForced": "A² = 9/20", "osResonant": "ω_r² = 3; A_max = 3/4"}, m=1, c=2, k=5, ic=[0, 0], F0=3, w=1),
        _p("at-peak", {"osForced": "A² = 2304/4097", "osResonant": "ω_r² = 3; A_max = 3/4"},
           m=1, c=2, k=5, ic=[0, 0], F0=3, w="7/4"),
        _p("overdamped-no-peak", {"osForced": "A² = 9/25", "osResonant": "none"}, m=1, c=4, k=4, ic=[0, 0], F0=3, w=1)]}),
    ("7.9", {"mode": "phase", "view": "field", "presets": [
        _p("decay", {"ppTrace": "−3", "ppDet": "2", "ppEig": "−2, −1", "ppType": "stable node"},
           A=[[0, 1], [-2, -3]], start=[1, 0], h="1/4", n=8),
        _p("pure", {"ppTrace": "0", "ppDet": "4", "ppEig": "±2i", "ppType": "centre"},
           A=[[0, 1], [-4, 0]], start=[1, 0], h="1/4", n=8),
        _p("damped", {"ppTrace": "−2", "ppDet": "5", "ppEig": "−1 ± 2i", "ppType": "stable spiral"},
           A=[[0, 1], [-5, -2]], start=[1, 0], h="1/4", n=8)]}),
    ("7.10", {"mode": "phase", "view": "exact", "presets": [
        _p("quarter", {"ppRatio": "17/16", "ppType": "centre",
                       "ppLast": "(535788072480961/281474976710656, 7152073883955/8796093022208)"},
           A=[[0, 1], [-1, 0]], start=[1, 0], h="1/4", n=24),
        _p("eighth", {"ppRatio": "65/64", "ppType": "centre"}, A=[[0, 1], [-1, 0]], start=[1, 0], h="1/8", n=48),
        _p("coarse", {"ppRatio": "5/4", "ppType": "centre", "ppLast": "(11753/4096, 1287/512)"},
           A=[[0, 1], [-1, 0]], start=[1, 0], h="1/2", n=12)]}),
    ("9.1", {"mode": "phase", "view": "field", "presets": [
        _p("saddle", {"ppTrace": "0", "ppDet": "−1", "ppLast": "(390625/65536, 6561/65536)"},
           A=[[1, 0], [0, -1]], start=[1, 1], h="1/4", n=8),
        _p("rotate", {"ppTrace": "0", "ppDet": "1", "ppLast": "(−31679/65536, −2415/2048)"},
           A=[[0, 1], [-1, 0]], start=[1, 0], h="1/4", n=8),
        _p("decay", {"ppTrace": "−3", "ppDet": "2", "ppLast": "(6561/32768, 1/128)"},
           A=[[-1, 0], [0, -2]], start=[2, 2], h="1/4", n=8)]}),
    ("9.2", {"mode": "phase", "view": "field", "presets": [
        _p("symmetric", {"ppEig": "1, 3", "ppVectors": "(1, −1), (1, 1)"}, A=[[2, 1], [1, 2]], start=[1, 0], h="1/4", n=8),
        _p("saddle", {"ppEig": "−2, 3", "ppVectors": "(2, −3), (1, 1)"}, A=[[1, 2], [3, 0]], start=[1, 0], h="1/4", n=8),
        _p("surd", {"ppEig": "(1 ± √5)/2", "ppVectors": "—"}, A=[[1, 1], [1, 0]], start=[1, 0], h="1/4", n=8)]}),
    ("9.3", {"mode": "phase", "view": "solution", "presets": [
        _p("symmetric", {"ppGeneral": "C₁·e^t·(1, −1) + C₂·e^(3t)·(1, 1)", "ppC": "C₁ = 1/2, C₂ = 1/2"},
           A=[[2, 1], [1, 2]], start=[1, 0], h="1/4", n=8),
        _p("saddle", {"ppGeneral": "C₁·e^(−2t)·(2, −3) + C₂·e^(3t)·(1, 1)", "ppC": "C₁ = 3/5, C₂ = 9/5"},
           A=[[1, 2], [3, 0]], start=[3, 0], h="1/4", n=8),
        _p("node", {"ppGeneral": "C₁·e^(−2t)·(0, 1) + C₂·e^(−t)·(1, 0)", "ppC": "C₁ = 2, C₂ = 2"},
           A=[[-1, 0], [0, -2]], start=[2, 2], h="1/4", n=8)]}),
    ("9.4", {"mode": "phase", "view": "field", "presets": [
        _p("saddle", {"ppType": "saddle", "ppDisc": "25"}, A=[[1, 2], [3, 0]], start=[1, 0], h="1/4", n=8),
        _p("node", {"ppType": "stable node", "ppDisc": "1"}, A=[[-1, 0], [0, -2]], start=[1, 0], h="1/4", n=8),
        _p("spiral", {"ppType": "unstable spiral", "ppDisc": "−16", "ppEig": "1 ± 2i"},
           A=[[1, 2], [-2, 1]], start=[1, 0], h="1/4", n=8),
        _p("centre", {"ppType": "centre", "ppDisc": "−16", "ppEig": "±2i"}, A=[[0, 2], [-2, 0]], start=[1, 0], h="1/4", n=8),
        _p("degenerate", {"ppType": "degenerate node", "ppDisc": "0"}, A=[[-1, 1], [0, -1]], start=[1, 0], h="1/4", n=8)]}),
    ("9.5", {"mode": "phase", "view": "field", "presets": [
        _p("stable-spiral", {"ppType": "stable spiral", "ppTrace": "−2", "ppDet": "5"},
           A=[[-1, 2], [-2, -1]], start=[1, 0], h="1/4", n=8),
        _p("centre", {"ppType": "centre", "ppTrace": "0", "ppDet": "4"}, A=[[0, 2], [-2, 0]], start=[1, 0], h="1/4", n=8),
        _p("unstable-node", {"ppType": "unstable node", "ppTrace": "4", "ppDet": "3"},
           A=[[2, 1], [1, 2]], start=[1, 0], h="1/4", n=8),
        _p("saddle", {"ppType": "saddle", "ppTrace": "1", "ppDet": "−6"}, A=[[1, 2], [3, 0]], start=[1, 0], h="1/4", n=8)]}),
    ("9.6", {"mode": "jacobian", "view": "field", "search": "off", "presets": [
        _p("parabola", {"jbCheck": "is an equilibrium"}, f="y - x^2", g="x - y", points=[[0, 0], [1, 1]]),
        _p("wrong", {"jbCheck": "f = 0, g = −2: not an equilibrium"}, f="y - x^2", g="x - y", points=[[2, 4]]),
        _p("search", {"jbCheck": "is an equilibrium", "jbFound": "—"}, f="y - x^2", g="x - y", points=[[0, 0], [1, 1]])]}),
    ("9.7", {"mode": "jacobian", "view": "linearised", "presets": [
        _p("parabola-origin", {"jbJ": "0 1; 1 −1", "jbType": "saddle", "jbTrace": "−1", "jbDet": "−1"},
           f="y - x^2", g="x - y", points=[[0, 0], [1, 1]]),
        _p("parabola-one", {"jbJ": "−2 1; 1 −1", "jbType": "stable node", "jbEig": "(−3 ± √5)/2"},
           f="y - x^2", g="x - y", points=[[1, 1], [0, 0]]),
        _p("inconclusive", {"jbJ": "0 −1; 1 0", "jbType": "centre (linearisation inconclusive)"},
           f="-y + x^3", g="x + y^3", points=[[0, 0]])]}),
    ("9.8", {"mode": "jacobian", "view": "trajectory", "presets": [
        _p("classic", {"jbCheck": "is an equilibrium", "jbJ": "0 −1; 2 0",
                       "jbType": "centre (linearisation inconclusive)"},
           f="2x - x y", g="-y + x y", points=[[1, 2], [0, 0]], start=[1, 1]),
        _p("slow", {"jbCheck": "is an equilibrium", "jbType": "centre (linearisation inconclusive)"},
           f="x - x y/2", g="-y/2 + x y/4", points=[[2, 2], [0, 0]], start=[1, 1]),
        _p("start-near", {"jbCheck": "is an equilibrium", "jbType": "centre (linearisation inconclusive)"},
           f="2x - x y", g="-y + x y", points=[[1, 2], [0, 0]], start=[1, 2])]}),
    ("9.9", {"mode": "jacobian", "view": "linearised", "presets": [
        _p("exclusion", {"jbCheck": "is an equilibrium", "jbJ": "−1 −2; −1 −1", "jbDet": "−1", "jbType": "saddle"},
           f="x(3 - x - 2y)", g="y(2 - x - y)", points=[[1, 1], [0, 0], [3, 0], [0, 2]]),
        _p("exclusion-corner", {"jbCheck": "is an equilibrium", "jbJ": "−3 −6; 0 −1", "jbDet": "3",
                                "jbType": "stable node"},
           f="x(3 - x - 2y)", g="y(2 - x - y)", points=[[3, 0], [0, 0], [0, 2], [1, 1]]),
        _p("coexist", {"jbCheck": "is an equilibrium", "jbDet": "4/3", "jbType": "stable node"},
           f="x(2 - x - y/2)", g="y(2 - y - x/2)", points=[["4/3", "4/3"], [0, 0]])]}),
    ("9.10", {"mode": "jacobian", "view": "trajectory", "presets": [
        _p("outbreak", {"jbExtra": "R₀ = 9/5; I peaks at S = 1/2", "jbType": "non-isolated equilibria"},
           f="-S I/2", g="S I/2 - I/4", vars=["S", "I"], points=[["9/10", 0]],
           start=["9/10", "1/10"], extra="sir", window=[0, 1, 0, "1/2"]),
        _p("contained", {"jbExtra": "R₀ = 9/20; I falls from the start", "jbType": "non-isolated equilibria"},
           f="-S I/2", g="S I/2 - I", vars=["S", "I"], points=[["9/10", 0]],
           start=["9/10", "1/10"], extra="sir", window=[0, 1, 0, "1/2"]),
        _p("everyone-susceptible", {"jbExtra": "R₀ = 99/50; I peaks at S = 1/2", "jbType": "non-isolated equilibria"},
           f="-S I/2", g="S I/2 - I/4", vars=["S", "I"], points=[["99/100", 0]],
           start=["99/100", "1/100"], extra="sir", window=[0, 1, 0, "1/2"])]}),
    ("10.1", {"mode": "laplace", "presets": [
        _p("one", {"lpF": "1/s"}, kind="table", f="1"),
        _p("exp", {"lpF": "1/(s − 2)"}, kind="table", f="e^(2t)"),
        _p("ramp", {"lpF": "1/s²"}, kind="table", f="t")]}),
    ("10.2", {"mode": "laplace", "presets": [
        _p("mixed", {"lpF": "(−2s³ + 6s + 6)/(s³(s + 1))", "lpPartial": "6/s³ − 2/(s + 1)"},
           kind="table", f="3t^2 - 2e^(-t)"),
        _p("cosine", {"lpF": "s/(s² + 4)"}, kind="table", f="cos(2t)"),
        _p("shifted", {"lpF": "1/(s − 3)²"}, kind="table", f="t e^(3t)")]}),
    ("10.3", {"mode": "laplace", "presets": [
        _p("exp", {"lpF": "1/(s − 2)", "lpY": "2/(s − 2)", "lpEqual": "equal"}, kind="derivative", f="e^(2t)"),
        _p("sine", {"lpF": "1/(s² + 1)", "lpY": "s/(s² + 1)", "lpEqual": "equal"}, kind="derivative", f="sin(t)"),
        _p("poly", {"lpF": "2/s³", "lpY": "2/s²", "lpEqual": "equal"}, kind="derivative", f="t^2")]}),
    ("10.4", {"mode": "laplace", "presets": [
        _p("decay", {"lpY": "(s + 3)/((s + 1)(s + 2))", "lpPartial": "2/(s + 1) − 1/(s + 2)",
                     "lpSolution": "2·e^(−t) − e^(−2t)"}, kind="solve", equation="y'' + 3y' + 2y = 0", ic=[1, 0]),
        _p("first-order", {"lpY": "6/(s(s + 2))", "lpPartial": "3/s − 3/(s + 2)", "lpSolution": "3 − 3·e^(−2t)"},
           kind="solve", equation="y' + 2y = 6", ic=[0]),
        _p("damped", {"lpY": "2/((s + 1)² + 4)", "lpPartial": "2/((s + 1)² + 4)", "lpSolution": "e^(−t)·sin(2t)"},
           kind="solve", equation="y'' + 2y' + 5y = 0", ic=[0, 2])]}),
    ("10.5", {"mode": "laplace", "presets": [
        _p("two-linear", {"lpPartial": "2/(s + 1) − 1/(s + 2)", "lpSolution": "2·e^(−t) − e^(−2t)"},
           kind="partial", F="(s + 3)/(s^2 + 3s + 2)"),
        _p("repeated", {"lpPartial": "1/s − 1/(s + 1) − 1/(s + 1)²", "lpSolution": "1 − t·e^(−t) − e^(−t)"},
           kind="partial", F="1/(s (s + 1)^2)"),
        _p("quadratic", {"lpPartial": "(1/5)/s − (s/5 + 2/5)/((s + 1)² + 4)",
                         "lpSolution": "1/5 − (1/5)·e^(−t)·cos(2t) − (1/10)·e^(−t)·sin(2t)"},
           kind="partial", F="1/(s (s^2 + 2s + 5))")]}),
    ("10.6", {"mode": "laplace", "presets": [
        _p("stable", {"lpPoles": "−2, −1", "lpSolution": "1/2 − e^(−t) + (1/2)·e^(−2t)"},
           kind="solve", equation="y'' + 3y' + 2y = 1", ic=[0, 0]),
        _p("oscillatory", {"lpPoles": "−1 ± 2i", "lpSolution": "1 − e^(−t)·cos(2t) − (1/2)·e^(−t)·sin(2t)"},
           kind="solve", equation="y'' + 2y' + 5y = 5", ic=[0, 0]),
        _p("unstable", {"lpPoles": "−1, 2", "lpSolution": "(1/3)·e^(2t) − 1 + (2/3)·e^(−t)"},
           kind="solve", equation="y'' - y' - 2y = 2", ic=[0, 0])]}),
    ("10.7", {"mode": "laplace", "presets": [
        _p("switch-on", {"lpY": "e^(−2s)/(s(s + 1))", "lpSolution": "0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2"},
           kind="step", equation="y' + y = u(t - 2)", ic=[0]),
        _p("pulse", {"lpY": "e^(−s)/(s(s + 1)) − e^(−3s)/(s(s + 1))",
                     "lpSolution": "0 for t < 1; 1 − e^(−(t − 1)) for 1 ≤ t < 3; −e^(−(t − 1)) + e^(−(t − 3)) for t ≥ 3"},
           kind="step", equation="y' + y = u(t - 1) - u(t - 3)", ic=[0]),
        _p("second-order", {"lpY": "e^(−s)/(s(s² + 4))", "lpSolution": "0 for t < 1; 1/4 − (1/4)·cos(2(t − 1)) for t ≥ 1"},
           kind="step", equation="y'' + 4y = u(t - 1)", ic=[0, 0])]}),
    ("10.8", {"mode": "laplace", "presets": [
        _p("constant-force", {"lpSolution": "2 − 4·e^(−t) + 2·e^(−2t)", "lpCheck": "residual 0",
                              "lpPartial": "2/s − 4/(s + 1) + 2/(s + 2)"},
           kind="solve", equation="y'' + 3y' + 2y = 4", ic=[0, 0]),
        _p("cosine-force", {"lpSolution": "cos(t) − cos(2t)", "lpCheck": "residual 0",
                            "lpPartial": "s/(s² + 1) − s/(s² + 4)"},
           kind="solve", equation="y'' + 4y = 3cos(t)", ic=[0, 0]),
        _p("exp-force", {"lpSolution": "(1/3)·e^t − (1/3)·e^(−2t)", "lpCheck": "residual 0"},
           kind="solve", equation="y' + 2y = e^t", ic=[0])]}),
]

TILES = {
    "linear1": ("lfPreset", ["lfMu", "lfYh", "lfYp", "lfC", "lfSteady", "lfSolution", "lfLast"], "lfStatus"),
    "stiff": ("skPreset", ["skFactor", "skVerdict", "skLimit", "skLast", "skTrue", "skBackward"], "skStatus"),
    "char": ("cePreset", ["ceDisc", "ceKind", "ceRoots", "ceGeneral", "ceC", "ceSolution", "ceW"], "ceStatus"),
    "oscillator": ("osPreset", ["osType", "osDisc", "osOmega0Sq", "osOmega0", "osPeriod", "osAmpSq", "osAmp",
                                "osPhase", "osCcrit", "osOmegaD", "osEnvelope", "osForced", "osResonant",
                                "osEnergy", "osCross"], "osStatus"),
    "phase": ("ppPreset", ["ppTrace", "ppDet", "ppDisc", "ppEig", "ppType", "ppVectors", "ppGeneral", "ppC",
                           "ppRatio", "ppLast"], "ppStatus"),
    "jacobian": ("jbPreset", ["jbCheck", "jbJ", "jbTrace", "jbDet", "jbEig", "jbType", "jbFound", "jbExtra"],
                 "jbStatus"),
    "laplace": ("lpPreset", ["lpF", "lpPoles", "lpY", "lpPartial", "lpSolution", "lpCheck", "lpEqual"], "lpStatus"),
}

MODE_JS = {
    "linear1": dekit_b.LINEAR1_JS, "stiff": dekit_b.STIFF_JS, "char": dekit_b.CHAR_JS,
    "oscillator": dekit_b.OSCILLATOR_JS, "phase": dekit_b.PHASE_JS, "jacobian": dekit_b.JACOBIAN_JS,
    "laplace": dekit_b.LAPLACE_JS,
}
SHARED_JS = [dekit_b.DB_JS, dekit_b.DB_TAB_JS, dekit_b.DB_ROOT_JS, dekit_b.DB_EQ_JS, dekit_b.DB_MAT_JS]
COMPUTE = {"linear1": "lfSolve", "stiff": "skCompute", "char": "ceSolve", "oscillator": "osCompute",
           "phase": "ppCompute", "jacobian": "jbCompute", "laplace": "LP_solve"}

# ES5: one inline <script> carries every lab and the quiz. BigInt literals are
# allowed, as RATIONAL_JS uses them.
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
    """What de_core and dekit_b add to a page: algebra_core's blocks, which
    predate the no-double-quote rule, taken out."""
    for block in de_core.ALGEBRA_BLOCKS:
        script = script.replace(block, "")
    return script


class EveryLessonBuilds(unittest.TestCase):
    def test_every_mode_is_covered(self):
        self.assertEqual({cfg["mode"] for _, cfg in FIXTURES}, set(dekit_b.MODES))
        self.assertEqual(set(TILES), set(dekit_b.MODES))

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
                    for tile in p["expect"]:
                        self.assertIn('<strong id="%s">' % tile, html, "%s pins a tile the page lacks" % p["id"])
                self.assertEqual(set(lab.expect), {select})
                self.assertEqual(set(lab.expect[select]), {p["id"] for p in cfg["presets"]})
                self.assertIn("window.redrawLab = redraw", lab.script)
                self.assertIn("DE_refuse(", lab.script)
                ids = re.findall(r'\bid="([^"]+)"', html)
                self.assertEqual(sorted({i for i in ids if ids.count(i) > 1}), [])

    def test_script_is_es5_and_offline(self):
        blocks = SHARED_JS + list(MODE_JS.values()) + [own_script(build(cfg).script) for _, cfg in FIXTURES]
        for i, js in enumerate(blocks):
            for rx, what in NOT_ES5:
                self.assertIsNone(rx.search(js), "%s in block %d" % (what, i))

    def test_no_double_quote_in_what_dekit_b_and_de_core_add(self):
        for block in SHARED_JS + list(MODE_JS.values()):
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

    def test_per_mode_assembly(self):
        """A page carries its own mode's code and no other mode's."""
        for key, cfg in FIXTURES:
            script = build(cfg).script
            with self.subTest(lesson=key):
                for mode, fn in COMPUTE.items():
                    (self.assertIn if mode == cfg["mode"] else self.assertNotIn)("function %s(" % fn, script)
        by = dict(FIXTURES)
        self.assertNotIn("function EPparse(", build(by["6.8"]).script)      # stiff: SHOW and DRAW only
        self.assertNotIn("function MPparse(", build(by["9.1"]).script)      # phase: no polynomials
        self.assertIn("function DE_eulerSys(", build(by["9.8"]).script)     # jacobian steps exactly

    def test_redraw_only_selects_ship_the_lesson_value(self):
        by = dict(FIXTURES)
        self.assertIn('<option value="steps" selected>', build(by["6.2"]).controls)
        self.assertIn('<option value="wronskian" selected>', build(by["7.8"]).controls)
        self.assertIn('<option value="amplitude" selected>', build(by["8.9"]).controls)
        self.assertIn('<option value="exact" selected>', build(by["7.10"]).controls)
        self.assertIn('<option value="trajectory" selected>', build(by["9.10"]).controls)
        self.assertIn('<option value="off" selected>', build(by["9.6"]).controls)

    def test_laplace_disables_the_inputs_its_kind_does_not_use(self):
        by = dict(FIXTURES)
        table = build(by["10.1"]).controls
        self.assertRegex(table, r'id="lpEq"[^>]*disabled')
        self.assertNotRegex(table, r'id="lpFIn"[^>]*disabled')
        solve = build(by["10.4"]).controls
        self.assertRegex(solve, r'id="lpFIn"[^>]*disabled')


class Refusals(unittest.TestCase):
    def bad(self, cfg, needle):
        with self.assertRaises(ValueError) as ctx:
            labs.build("dekit", cfg)
        self.assertIn(needle, str(ctx.exception))

    def test_unknown_mode(self):
        self.bad({"mode": "nonsense", "presets": [_p("x", a=1)]}, "mode")

    def test_unknown_preset(self):
        self.bad(dict(FIXTURES[0][1], preset="nope"), "no preset 'nope'")

    def test_malformed_instances_name_the_preset(self):
        self.bad({"mode": "linear1", "presets": [_p("two", equation="y' = 1 = 2")]}, "'two'")
        self.bad({"mode": "linear1", "presets": [_p("noprime", equation="y = t")]}, "'noprime'")
        self.bad({"mode": "stiff", "presets": [_p("neg", a=-1, y0=1, h="1/2", n=8)]}, "'neg'")
        self.bad({"mode": "stiff", "presets": [_p("many", a=1, y0=1, h="1/2", n=65)]}, "'many'")
        self.bad({"mode": "char", "presets": [_p("flat", a=0, b=1, c=1)]}, "'flat'")
        self.bad({"mode": "oscillator", "presets": [_p("w", m=1, c=0, k=4, ic=[1, 0], F0=3)]}, "'w'")
        self.bad({"mode": "phase", "presets": [_p("shape", A=[[1, 2, 3], [4, 5, 6]])]}, "'shape'")
        self.bad({"mode": "jacobian", "presets": [_p("vars", f="x", g="y", vars=["p", "q"], points=[[0, 0]])]}, "'vars'")
        self.bad({"mode": "jacobian", "presets": [_p("seven", f="x", g="y", points=[[0, 0]] * 7)]}, "'seven'")
        self.bad({"mode": "laplace", "presets": [_p("kind", kind="fourier", f="1")]}, "'kind'")
        self.bad({"mode": "laplace", "presets": [_p("letter", kind="partial", F="1/(z + 1)")]}, "'letter'")

    def test_bad_redraw_only_values(self):
        self.bad(dict(dict(FIXTURES)["6.1"], view="graph"), "view")
        self.bad(dict(dict(FIXTURES)["6.8"], scheme="midpoint"), "scheme")
        self.bad(dict(dict(FIXTURES)["9.6"], search="all"), "search")

    def test_missing_expect_is_not_a_build_error(self):
        build({"mode": "stiff", "presets": [{"id": "x", "label": "x", "a": 5, "y0": 1, "h": "1/2", "n": 8}]})


# ---------------------------------------------------------------------------
# The arithmetic, by running the shipped blocks under node. Each case was seen
# to fail with the function it tests broken on purpose.
# ---------------------------------------------------------------------------

ARITH = r"""
var out = [];
function eq(label, got, want) { if (String(got) !== String(want)) out.push(label + ': got ' + got + ', want ' + want); }
function Q(s) { return DE_rat(s); }
function throws(label, fn, needle) {
  try { fn(); out.push(label + ': did not throw'); }
  catch (e) { if (String(e.message).indexOf(needle) < 0) out.push(label + ': threw ' + e.message); }
}
/* shared helpers */
eq('intvec', DB_intvec(Q('-2'), Q('4/3')).map(DE_q).join(' '), '3 −2');
eq('exp 1', DB_exp(Q('1')), 'e^t');
eq('exp -1/20', DB_exp(Q('-1/20')), 'e^(−t/20)');
eq('join', DB_join(['3', '−2t', '', 't²']), '3 − 2t + t²');
eq('type spiral', DB_type(Q('-2'), Q('5'), Q('-16'), false), 'stable spiral');
eq('type star', DB_type(Q('-2'), Q('1'), Q('0'), true), 'star node');
eq('i root', DB_roottext(quadroots(R1, R0, Q('2'))), '±i√2');
/* linear1 */
var L = lfSolve('2y\' + 6y = 4t', '');
eq('lf p', RFtext(L.p, 't'), '3');
eq('lf yp ramp', lfSolve('y\' + 3y = 2t', '0 1').ypText, '(2/3)·t − 2/9');
eq('lf C ramp', DE_q(lfSolve('y\' + 3y = 2t', '0 1').C), '11/9');
eq('lf resonant', lfSolve('y\' + 2y = e^(-2t)', '').ypText, 't·e^(−2t)');
eq('lf cosine', lfSolve('y\' + 2y = cos(t)', '').ypText, '(2/5)·cos(t) + (1/5)·sin(t)');
eq('lf t-squared', lfSolve('y\' + (2/t) y = t^2', '1 1').solution, 'y = t³/5 + (4/5)/t²');
eq('lf a=0', lfSolve('y\' = 3t^2', '0 1').solution, 'y = t³ + 1');
eq('lf steps', DE_q(lfSteps(lfSolve('y\' + 2y = 6', '0 0'), Q('1/4'), 4).rows[4].y), '45/16');
eq('lf negative power', lfSolve('y\' + y/t = 1', '1 0').solution, 'y = t/2 − (1/2)/t');
eq('lf t0 = 2', lfSolve('y\' + (2/t) y = t^2', '2 1').solution, 'y = t³/5 − (12/5)/t²');
eq('lf double sign', RFtext(lfSolve('y\' + -2y = 0', '').p, 't'), '−2');
throws('lf function', function () { lfSolve('y\' = sin(y)', ''); }, 'inside a function');
throws('lf nonlinear', function () { lfSolve('y\' = y^2', ''); }, 'not linear');
throws('lf second order', function () { lfSolve('y\'\' + y = 0', ''); }, 'second order');
throws('lf p form', function () { lfSolve('y\' + t^2 y = 0', ''); }, 'this lab solves a constant p');
throws('lf bracket', function () { lfSolve('y\' + 2(y + 1) = 0', ''); }, 'multiply out');
throws('lf ln', function () { lfSolve('y\' - y/t = 1', ''); }, 'ln t');
throws('lf over t', function () { lfSolve('t y\' - y = 1', ''); }, 'negative power');
/* stiff */
eq('sk -1', skVerdict(Q('-1')), 'oscillates without decaying');
eq('sk grows', DE_q(skCompute('5', '1', '1/2', 8, 'forward').rows[8]), '6561/256');
eq('sk backward', DE_q(skCompute('5', '1', '1/2', 2, 'backward').rows[2]), '4/49');
/* char */
var C1 = ceSolve('1', '3', '2', '1 0');
eq('ce C', DE_q(C1.C[0]) + ' ' + DE_q(C1.C[1]), '2 −1');
eq('ce residual', EPzero(C1.residual) && C1.icOK, true);
eq('ce W surd', ceSolve('1', '-1', '-1', '').W, '−√5');
eq('ce W pure', ceSolve('1', '0', '4', '').W, '2');
eq('ce irrational frequency', ceSolve('1', '0', '2', '1 0').C, null);
/* oscillator */
var O = osCompute('1', '2', '5', '0 0', '3', '1');
eq('os forced', O.forced, 'A² = 9/20');
eq('os resonant', O.resonant, 'ω_r² = 3; A_max = 3/4');
eq('os resonance', osCompute('1', '0', '4', '0 0', '3', '2').forced, 'resonance: (3/4)·t·sin(2t)');
eq('os cross', osCompute('1', '4', '4', '1 -5', '0', '').cross, 't = 1/3');
eq('os period', osCompute('2', '0', '5', '1 0', '', '').period, '4π/√10 ≈ 3.97384');
/* phase */
var P = ppCompute('0 1; -1 0', '1 0', '1/4', 2);
eq('pp ratio', P.ratio, '17/16');
eq('pp last', P.last, '(15/16, −1/2)');
eq('pp vectors', ppCompute('1 2; 3 0', '3 0', '1/4', 1).vectors, '(2, −3), (1, 1)');
eq('pp C', (function () { var M = ppCompute('1 2; 3 0', '3 0', '1/4', 1); return DE_q(M.C[0]) + ' ' + DE_q(M.C[1]); })(), '3/5 9/5');
eq('pp degenerate', ppCompute('-1 1; 0 -1', '1 0', '1/4', 1).general, 'e^(−t)·(C₁·(1, 0) + C₂·(t·(1, 0) + (0, 1)))');
/* jacobian */
var J = jbCompute('y - x^2', 'x - y', ['x', 'y'], '2 4', 0, 'grid', null, '');
eq('jb check', J.checks[0].text, 'f = 0, g = −2: not an equilibrium');
eq('jb grid', J.found.text, 'found 2: (0, 0), (1, 1)');
eq('jb grid whole', jbCompute('x - 10', 'y', ['x', 'y'], '0 0', 0, 'grid', null, '').found.text, 'found 1: (10, 0)');
eq('jb grid thirds', jbCompute('3x - 1', 'y', ['x', 'y'], '0 0', 0, 'grid', null, '').found.text, 'found 1: (1/3, 0)');
eq('jb sir', jbCompute('-S I/2', 'S I/2 - I/4', ['S', 'I'], '9/10 0', 0, 'off', 'sir', '9/10 1/10').sir.text, 'R₀ = 9/5; I peaks at S = 1/2');
eq('jb inconclusive', jbCompute('-y + x^3', 'x + y^3', ['x', 'y'], '0 0', 0, 'off', null, '').type, 'centre (linearisation inconclusive)');
/* laplace */
eq('lp two quads', LP_solve('y\'\' + 4y = 3cos(t)', '0 0').solution, 'cos(t) − cos(2t)');
eq('lp step', LP_solve('y\' + y = u(t - 2)', '0').solution, '0 for t < 2; 1 − e^(−(t − 2)) for t ≥ 2');
eq('lp check', LP_solve('y\'\' + 3y\' + 2y = 4', '0 0').check, 'residual 0');
var F = RFparse('1/(s (s + 1)^2)', 's'), fz = LP_factor(F.den, []);
eq('lp partial repeated', LP_ptext(LP_partial(F, fz)), '1/s − 1/(s + 1) − 1/(s + 1)²');
eq('lp inverse repeated', EPtext(LP_invert(F, fz)), '1 − t·e^(−t) − e^(−t)');
throws('lp irrational frequency', function () { var G = RFparse('1/(s^2 + 2)', 's'); LP_factor(G.den, []); }, 'irrational');
throws('lp irrational roots', function () { LP_solve('y\'\' - y\' - y = 0', '1 0'); }, 'irrational');
throws('lp cubic', function () { var G = RFparse('1/(s^3 + s + 1)', 's'); LP_factor(G.den, []); }, 'degree 3 or more');
throws('lp step at 0', function () { LP_solve('y\' + y = u(t)', '0'); }, 'c > 0');
console.log(out.length ? out.join('\n') : 'OK');
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class Arithmetic(unittest.TestCase):
    def test_shipped_blocks_compute_the_worked_figures(self):
        src = de_core.script("SURD", "MPOLY", "RF", "EP", "STEP", "DRAW", extra="".join(SHARED_JS) + "".join(MODE_JS.values()))
        run = subprocess.run(["node", "-"], input=src + ARITH, capture_output=True, text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")


# A page's own script, run against a stub document: every control at the value
# the markup ships for that preset, then each pinned tile read back. The full
# gate, sweep included, is scripts/labcheck.js --expect on rendered pages.
PAGE_RUNNER = r"""
var vm = require('vm');
var jobs = JSON.parse(require('fs').readFileSync(0, 'utf8')), fails = [];
function El(id, value, attrs) {
  this.id = id; this.value = value === undefined ? '' : value; this.textContent = ''; this.innerHTML = '';
  this.style = {}; this.attrs = attrs || {};
}
El.prototype.addEventListener = function () {};
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return k in this.attrs ? this.attrs[k] : null; };
El.prototype.appendChild = function (c) { return c; };
El.prototype.remove = function () {};
jobs.forEach(function (job) {
  var els = {};
  Object.keys(job.values).forEach(function (id) { els[id] = new El(id, job.values[id], job.attrs[id]); });
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
  Object.keys(job.expect).forEach(function (tile) {
    var got = els[tile] ? els[tile].textContent : '(no tile)';
    if (got !== job.expect[tile]) fails.push(job.name + ' #' + tile + ': got ' + got + ', want ' + job.expect[tile]);
  });
  if (/Refused/.test(els[job.status].innerHTML)) fails.push(job.name + ': ' + els[job.status].innerHTML);
});
console.log(fails.length ? fails.join('\n') : 'OK');
"""


def _values(html):
    out, attrs = {}, {}
    for m in re.finditer(r'<(input|select|div|strong|span|svg|label)\b([^>]*)>', html):
        idm = re.search(r'\bid="([^"]+)"', m.group(2))
        if idm:
            val = re.search(r'\bvalue="([^"]*)"', m.group(2))
            out[idm.group(1)] = val.group(1) if (val and m.group(1) == "input") else ""
            rng = re.search(r'\bmin="([^"]*)" max="([^"]*)"', m.group(2))
            if rng:
                attrs[idm.group(1)] = {"min": rng.group(1), "max": rng.group(2)}
    for m in re.finditer(r'<select id="([^"]+)">(.*?)</select>', html):
        chosen = re.search(r'<option value="([^"]*)" selected>', m.group(2)) or re.search(r'<option value="([^"]*)"', m.group(2))
        out[m.group(1)] = chosen.group(1) if chosen else ""
    return out, attrs


def page_jobs(fixtures):
    jobs = []
    for key, cfg in fixtures:
        for p in cfg["presets"]:
            lab = build(cfg, preset=p["id"])
            values, attrs = _values(lab.markup + lab.controls)
            jobs.append({"name": "%s %s/%s" % (key, cfg["mode"], p["id"]), "script": lab.script, "values": values,
                         "attrs": attrs, "expect": p["expect"], "status": TILES[cfg["mode"]][2]})
    return jobs


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class EveryPresetPrintsItsFigures(unittest.TestCase):
    def run_jobs(self, jobs):
        run = subprocess.run(["node", "-e", PAGE_RUNNER], input=json.dumps(jobs), capture_output=True,
                             text=True, timeout=300)
        self.assertEqual(run.returncode, 0, run.stderr[-2000:])
        self.assertEqual(run.stdout.strip(), "OK")

    def test_each_page_script_prints_the_pinned_tiles(self):
        self.run_jobs(page_jobs(FIXTURES))

    def test_the_grid_search_when_a_lesson_ships_it_on(self):
        cfg = dict(dict(FIXTURES)["9.6"], search="grid")
        cfg["presets"] = [_p("on", {"jbFound": "found 2: (0, 0), (1, 1)"}, f="y - x^2", g="x - y", points=[[0, 0]])]
        self.run_jobs(page_jobs([("9.6 grid", cfg)]))


if __name__ == "__main__":
    unittest.main()
