"""choicekit builds every mode with the presets docs/philosophy/PLAN.md section C sketches.

Fast and browserless: each lab is built through labs.build("choicekit", cfg) and
the markup and script are checked for the controls, tiles and wiring D.2 names.
The figures in `expect` below were worked by hand from the spec's arithmetic;
this file does not run the page, but scripts/labcheck.js can compare them
against a rendered page (the fixtures are importable for that).
"""

import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from mathpath import labs  # noqa: E402
from mathpath.labs import choicekit  # noqa: E402


def _p(pid, expect=None, **fields):
    out = {"id": pid, "label": pid.replace("-", " ")}
    out.update(fields)
    out["expect"] = expect or {}
    return out


UMBRELLA = dict(acts=["take", "leave"], states=["rain", "dry"], payoffs=[[2, 1], [-3, 3]])
NEWCOMB = dict(acts=["one-box", "two-box"], states=["predicted one", "predicted two"],
               payoffs=[[1000000, 0], [1001000, 1000]])
URNS = dict(hyps=["urn 1", "urn 2"], outcomes=["red", "blue"], prior=["1/2", "1/2"],
            lik=[["3/4", "1/4"], ["1/4", "3/4"]])
WITNESS = dict(hyps=["it happened", "it did not"], outcomes=["yes", "no"],
               lik=[["9/10", "1/10"], ["1/10", "9/10"]])
COIN_SPACE = dict(kind="space", outcomes=["H", "T"], probs=["1/2", "1/2"],
                  events=[{"name": "heads", "set": ["H"]}, {"name": "tails", "set": ["T"]}], threshold=1)
DIE = ["1", "2", "3", "4", "5", "6"]
PD = [[[3, 3], [0, 5]], [[5, 0], [1, 1]]]
PGOOD = dict(payC="3*10*(k+1)/n - 10", payD="3*10*k/n")
THREE = [{"count": 4, "rank": "A B C"}, {"count": 3, "rank": "B C A"}, {"count": 2, "rank": "C B A"}]
CYCLE = [{"count": 1, "rank": "A B C"}, {"count": 1, "rank": "B C A"}, {"count": 1, "rank": "C A B"}]
KIDNEY = [{"name": "small", "a": [81, 87], "b": [234, 270]}, {"name": "large", "a": [192, 263], "b": [55, 80]}]


# (lesson, cfg). One entry per section C lesson that uses choicekit.
FIXTURES = [
    # ---------------------------------------------------------------- decide
    ("4.2 dominance", {"mode": "decide", "rule": "dominance", "presets": [
        _p("umbrella", {"deChoice": "none"}, **UMBRELLA),
        _p("dominated", {"deChoice": "none"}, acts=["take", "leave", "stay"], states=["rain", "dry"],
           payoffs=[[2, 1], [-3, 3], [1, 0]]),
        _p("weak", {"deChoice": "take"}, acts=["take", "leave"], states=["rain", "dry"], payoffs=[[2, 1], [2, 0]]),
    ]}),
    ("4.3 maximin and regret", {"mode": "decide", "rule": "maximin", "presets": [
        _p("umbrella", {"deChoice": "take", "deValue": "1"}, **UMBRELLA),
        _p("disagree", {"deChoice": "a", "deValue": "3"}, acts=["a", "b"], states=["s1", "s2"],
           payoffs=[[3, 3], [2, 10]]),
    ]}),
    ("4.4 expected value", {"mode": "decide", "rule": "eu", "presets": [
        _p("umbrella-p", {"deChoice": "take", "deValue": "4/3", "deFlip": "p(rain) = 2/7"}, probs=["1/3", "2/3"],
           **UMBRELLA),
        _p("bet", {"deChoice": "bet, decline", "deValue": "0", "deFlip": "p(win) = 1/2"}, acts=["bet", "decline"],
           states=["win", "lose"], payoffs=[[1, -1], [0, 0]], probs=["1/2", "1/2"]),
        _p("lottery-ticket", {"deChoice": "skip", "deValue": "0"}, acts=["buy", "skip"], states=["win", "lose"],
           payoffs=[[99, -1], [0, 0]], probs=["1/1000", "999/1000"]),
    ]}),
    ("4.5 utility and information", {"mode": "decide", "rule": "eu", "presets": [
        _p("insurance", {"deChoice": "risk", "deVpi": "4/5"}, acts=["insure", "risk"], states=["fire", "no fire"],
           payoffs=[[8, 8], [0, 10]], probs=["1/10", "9/10"]),
        _p("vpi", {"deChoice": "take", "deVpi": "4/3"}, probs=["1/3", "2/3"], **UMBRELLA),
    ]}),
    ("4.6 allais", {"mode": "decide", "rule": "eu", "presets": [
        _p("allais-a", {"deChoice": "gamble", "deValue": "103/10"}, acts=["sure", "gamble"],
           states=["ticket 1", "tickets 2-11", "tickets 12-100"], payoffs=[[10, 10, 10], [0, 14, 10]],
           probs=["1/100", "10/100", "89/100"]),
        _p("allais-b", {"deChoice": "y", "deValue": "7/5"}, acts=["x", "y"],
           states=["ticket 1", "tickets 2-11", "tickets 12-100"], payoffs=[[10, 10, 0], [0, 14, 0]],
           probs=["1/100", "10/100", "89/100"]),
    ]}),
    ("4.7 ellsberg", {"mode": "decide", "rule": "eu", "presets": [
        _p("ellsberg-1", {"deChoice": "bet black", "deFlip": "p(red) = 1/2"}, acts=["bet red", "bet black"],
           states=["red", "black"], payoffs=[[1, 0], [0, 1]], probs=["1/3", "2/3"]),
    ]}),
    ("4.8 pascal", {"mode": "decide", "rule": "eu", "presets": [
        _p("pascal", {"deChoice": "wager, abstain", "deValue": "0"}, acts=["wager", "abstain"],
           states=["god", "no god"], payoffs=[[999, -1], [0, 0]], probs=["1/1000", "999/1000"]),
        _p("pascal-wins", {"deChoice": "wager", "deValue": "1/1000"}, acts=["wager", "abstain"],
           states=["god", "no god"], payoffs=[[1000, -1], [0, 0]], probs=["1/1000", "999/1000"]),
        _p("many-gods", {"deChoice": "abstain"}, acts=["wager on A", "wager on B", "abstain"],
           states=["god A", "god B", "none"], payoffs=[[10, -20, -1], [-20, 10, -1], [0, 0, 0]],
           probs=["1/1000", "1/1000", "998/1000"]),
    ]}),
    ("4.9 newcomb", {"mode": "decide", "rule": "evidential", "presets": [
        _p("newcomb-90", {"deChoice": "one-box", "deValue": "900000"},
           conditional={"one-box": ["9/10", "1/10"], "two-box": ["1/10", "9/10"]}, **NEWCOMB),
        _p("newcomb-coin", {"deChoice": "two-box", "deValue": "501000"},
           conditional={"one-box": ["1/2", "1/2"], "two-box": ["1/2", "1/2"]}, **NEWCOMB),
    ]}),
    ("6.6 trolley", {"mode": "decide", "rule": "constrained", "presets": [
        _p("switch", {"deChoice": "divert", "deValue": "−1"}, acts=["divert", "do nothing"], states=["certain"],
           payoffs=[[-1], [-5]], probs=[1]),
        _p("footbridge", {"deChoice": "do nothing", "deValue": "−5"}, acts=["push", "do nothing"],
           states=["certain"], payoffs=[[-1], [-5]], probs=[1], forbidden=["push"]),
    ]}),
    ("7.1 original position", {"mode": "decide", "rule": "maximin", "presets": [
        _p("rawls", {"deChoice": "equal", "deValue": "5"}, acts=["equal", "unequal"],
           states=["position 1", "position 2", "position 3"], payoffs=[[5, 5, 5], [2, 8, 20]]),
        _p("close-call", {"deChoice": "unequal", "deValue": "6"}, acts=["equal", "unequal"],
           states=["position 1", "position 2", "position 3"], payoffs=[[5, 5, 5], [6, 8, 20]]),
    ]}),
    ("7.1 laplace", {"mode": "decide", "rule": "laplace", "presets": [
        _p("harsanyi", {"deChoice": "unequal", "deValue": "10"}, acts=["equal", "unequal"],
           states=["position 1", "position 2", "position 3"], payoffs=[[5, 5, 5], [2, 8, 20]]),
    ]}),
    # ---------------------------------------------------------------- update
    ("2.8 updating", {"mode": "update", "presets": [
        _p("urns", {"upPost": "3/4", "upBF": "3"}, data=["red"], **URNS),
        _p("two-draws", {"upPost": "9/10", "upBF": "9"}, data=["red", "red"], **URNS),
        _p("bias", {"upPost": "1/9", "upBF": "1/8", "upConf": "Disconfirms"}, hyps=["fair", "two-headed"],
           outcomes=["heads", "tails"], prior=["1/2", "1/2"], lik=[["1/2", "1/2"], [1, 0]],
           data=["heads", "heads", "heads"]),
    ]}),
    ("2.9 testimony", {"mode": "update", "presets": [
        _p("witness", {"upPost": "1/12", "upBF": "9", "upConf": "Confirms"}, prior=["1/100", "99/100"],
           data=["yes"], **WITNESS),
        _p("two-witnesses", {"upPost": "9/20", "upBF": "81"}, prior=["1/100", "99/100"], data=["yes", "yes"],
           **WITNESS),
        _p("miracle", {"upPost": "1/1002", "upBF": "999"}, hyps=["it happened", "it did not"],
           outcomes=["yes", "no"], prior=["1/1000000", "999999/1000000"],
           lik=[["999/1000", "1/1000"], ["1/1000", "999/1000"]], data=["yes"]),
    ]}),
    ("3.1 succession", {"mode": "update", "presets": [
        _p("succession", {"upPred": "43735/44346", "upPost": "0"}, hyps=["bias 0", "bias 1/4", "bias 1/2", "bias 3/4",
                                                                       "bias 1"],
           outcomes=["s", "f"], prior=["1/5"] * 5,
           lik=[[0, 1], ["1/4", "3/4"], ["1/2", "1/2"], ["3/4", "1/4"], [1, 0]], data=["s"] * 10),
        _p("skeptic", {"upPost": "0"}, hyps=["bias 0", "bias 1/2", "bias 1"], outcomes=["s", "f"],
           prior=["8/10", "1/10", "1/10"], lik=[[0, 1], ["1/2", "1/2"], [1, 0]], data=["s"] * 10),
    ]}),
    ("3.2 grue", {"mode": "update", "presets": [
        _p("grue", {"upBF": "1", "upConf": "Neutral"}, hyps=["green", "grue"], outcomes=["green", "blue"],
           prior=["1/2", "1/2"], lik=[[1, 0], [1, 0]], data=["green"] * 100),
        _p("tell", {"upBF": "infinite", "upConf": "Proves"}, hyps=["green", "grue"], outcomes=["green", "blue"],
           prior=["1/2", "1/2"], lik=[[1, 0], [0, 1]], data=["green"]),
    ]}),
    ("3.3 confirmation", {"mode": "update", "presets": [
        _p("surprising", {"upBF": "10", "upConf": "Confirms", "upPost": "10/11"}, hyps=["H", "not H"],
           outcomes=["E", "not-E"], prior=["1/2", "1/2"], lik=[[1, 0], ["1/10", "9/10"]], data=["E"]),
        _p("expected", {"upBF": "10/9", "upConf": "Confirms", "upPost": "10/19"}, hyps=["H", "not H"],
           outcomes=["E", "not-E"], prior=["1/2", "1/2"], lik=[[1, 0], ["9/10", "1/10"]], data=["E"]),
        _p("neutral", {"upBF": "1", "upConf": "Neutral", "upPost": "1/2"}, hyps=["H", "not H"],
           outcomes=["E", "not-E"], prior=["1/2", "1/2"], lik=[["1/2", "1/2"], ["1/2", "1/2"]], data=["E"]),
    ]}),
    ("3.4 falsification", {"mode": "update", "presets": [
        _p("popper", {"upConf": "Refutes", "upPost": "0"}, hyps=["H", "not H"], outcomes=["o1", "o2", "o3"],
           prior=["1/2", "1/2"], lik=[["1/2", "1/2", 0], ["1/3", "1/3", "1/3"]], data=["o3"]),
        _p("unfalsifiable", {"upConf": "Neutral", "upPost": "1/2"}, hyps=["H", "not H"], outcomes=["o1", "o2", "o3"],
           prior=["1/2", "1/2"], lik=[["1/3", "1/3", "1/3"], ["1/3", "1/3", "1/3"]], data=["o1"]),
        _p("risky", {"upConf": "Confirms", "upPost": "3/4"}, hyps=["H", "not H"], outcomes=["o1", "o2", "o3"],
           prior=["1/2", "1/2"], lik=[[1, 0, 0], ["1/3", "1/3", "1/3"]], data=["o1"]),
    ]}),
    ("3.5 ravens", {"mode": "update", "presets": [
        _p("nonblack", {"upBF": "901/900"}, hyps=["H", "not H"], outcomes=["raven", "non-raven"],
           prior=["1/2", "1/2"], lik=[[0, 1], ["1/901", "900/901"]], data=["non-raven"]),
        _p("ravens", {"upBF": "10/9"}, hyps=["H", "not H"], outcomes=["black", "white"], prior=["1/2", "1/2"],
           lik=[[1, 0], ["9/10", "1/10"]], data=["black"]),
    ]}),
    ("9.2 turing test", {"mode": "update", "presets": [
        _p("mimic", {"upBF": "1"}, hyps=["machine", "human"], outcomes=["a", "b"], prior=["1/2", "1/2"],
           lik=[["1/2", "1/2"], ["1/2", "1/2"]], data=["a"] * 10),
        _p("tell", {"upBF": "1/9", "upPost": "1/10"}, hyps=["human", "machine"], outcomes=["odd", "plain"],
           prior=["1/2", "1/2"], lik=[["1/10", "9/10"], ["9/10", "1/10"]], data=["odd"]),
    ]}),
    ("10.6 two envelopes", {"mode": "update", "presets": [
        _p("interior", {"upBest": "switch: 10", "upPost": "1/2"}, hyps=["pair 4 and 8", "pair 8 and 16"],
           outcomes=["see8"], prior=["1/2", "1/2"], lik=[[1], [1]], data=["see8"],
           payoffs={"switch": [4, 16], "keep": [8, 8]}),
        _p("top", {"upBest": "keep: 8", "upPost": "1"}, hyps=["pair 4 and 8", "pair 8 and 16"], outcomes=["see8"],
           prior=[1, 0], lik=[[1], [1]], data=["see8"], payoffs={"switch": [4, 16], "keep": [8, 8]}),
    ]}),
    ("10.7 sleeping beauty", {"mode": "update", "presets": [
        _p("halfer", {"upPost": "1/2", "upBF": "1"}, hyps=["heads", "tails"], outcomes=["awake"],
           prior=["1/2", "1/2"], lik=[[1], [1]], data=["awake"]),
        _p("thirder", {"upPost": "1/3", "upBF": "1/2"}, hyps=["heads", "tails"], outcomes=["this", "other"],
           prior=["1/2", "1/2"], lik=[["1/2", "1/2"], [1, 0]], data=["this"]),
    ]}),
    ("10.8 monty hall", {"mode": "update", "presets": [
        _p("monty", {"upPost": "1/3", "upBest": "switch: 2/3"}, hyps=["car 1", "car 2", "car 3"],
           outcomes=["opens2", "opens3"], prior=["1/3", "1/3", "1/3"], lik=[["1/2", "1/2"], [0, 1], [1, 0]],
           data=["opens3"], payoffs={"stay": [1, 0, 0], "switch": [0, 1, 0]}),
        _p("random-host", {"upPost": "1/2", "upBest": "stay, switch: 1/2"}, hyps=["car 1", "car 2", "car 3"],
           outcomes=["opens3-goat", "other"], prior=["1/3", "1/3", "1/3"],
           lik=[["1/2", "1/2"], ["1/2", "1/2"], [0, 1]], data=["opens3-goat"],
           payoffs={"stay": [1, 0, 0], "switch": [0, 1, 0]}),
    ]}),
    # -------------------------------------------------------------- credence
    ("2.6 dutch book", {"mode": "credence", "presets": [
        _p("coin", {"crBook": "loss 1/5 per unit"}, typed={"heads": "3/5", "tails": "3/5"}, **COIN_SPACE),
        _p("die", {"crBook": "loss 1/6 per unit"}, kind="space", outcomes=DIE, probs=["1/6"] * 6,
           events=[{"name": "even", "set": ["2", "4", "6"]}, {"name": "one", "set": ["1"]},
                   {"name": "even or one", "set": ["1", "2", "4", "6"]}],
           typed={"even": "1/2", "one": "1/6", "even or one": "1/2"}, threshold=1),
        _p("coherent", {"crBook": "none found", "crAccepted": "0 of 2"}, typed={"heads": "1/2", "tails": "1/2"},
           **COIN_SPACE),
    ]}),
    ("2.11 lottery", {"mode": "credence", "presets": [
        _p("hundred", {"crAccepted": "100 of 100", "crConsistent": "Inconsistent", "crPAll": "0"}, kind="lottery",
           n=100, threshold="99/100"),
        _p("thousand", {"crAccepted": "1000 of 1000", "crConsistent": "Inconsistent"}, kind="lottery", n=1000,
           threshold="999/1000"),
        _p("strict", {"crAccepted": "0 of 100", "crConsistent": "Consistent", "crPAll": "1"}, kind="lottery", n=100,
           threshold="999/1000"),
    ]}),
    ("2.12 preface", {"mode": "credence", "presets": [
        _p("book", {"crAccepted": "100 of 100", "crConsistent": "Consistent",
                    "crPAll": "%d/%d" % (99 ** 100, 100 ** 100)}, kind="independent", n=100, p="99/100",
           threshold="95/100"),
        _p("short", {"crPAll": "3486784401/10000000000"}, kind="independent", n=10, p="9/10", threshold="9/10"),
        _p("certain", {"crPAll": "1", "crAccepted": "100 of 100"}, kind="independent", n=100, p=1,
           threshold="95/100"),
    ]}),
    ("2.6 space threshold", {"mode": "credence", "presets": [
        _p("die-accept", {"crAccepted": "2 of 3", "crPAll": "2/3", "crConsistent": "Consistent"}, kind="space",
           outcomes=DIE, probs=["1/6"] * 6,
           events=[{"name": "not six", "set": ["1", "2", "3", "4", "5"]}, {"name": "not one", "set": DIE[1:]},
                   {"name": "even", "set": ["2", "4", "6"]}], threshold="2/3"),
    ]}),
    # ---------------------------------------------------------------- series
    ("4.10 st petersburg", {"mode": "series", "kind": "petersburg", "presets": [
        _p("uncapped", {"srSum": "20", "srLimit": "none"}, n=20),
        _p("cap-1024", {"srSum": "11263/1024", "srLimit": "11"}, n=20, cap=1024),
        _p("cap-million", {"srSum": "20", "srLimit": "21"}, n=20, cap=1048576),
    ]}),
    ("10.3 dichotomy", {"mode": "series", "kind": "geometric", "presets": [
        _p("halves", {"srSum": "1023/1024", "srRemain": "1/1024", "srLimit": "1"}, a="1/2", r="1/2", n=10),
        _p("thirds", {"srSum": "29524/59049", "srLimit": "1/2", "srRemain": "1/118098"}, a="1/3", r="1/3", n=10),
        _p("twenty", {"srSum": "1048575/1048576"}, a="1/2", r="1/2", n=20),
    ]}),
    ("10.4 achilles", {"mode": "series", "kind": "geometric", "presets": [
        _p("ten-to-one", {"srLimit": "1000/9", "srSum": "11111/100"}, a=100, r="1/10", n=5),
        _p("close-race", {"srLimit": "1000"}, a=100, r="9/10", n=10),
        _p("tortoise-wins", {"srLimit": "none", "srSum": "1000"}, a=100, r=1, n=10),
    ]}),
    ("10.5 lamp", {"mode": "series", "kind": "lamp", "presets": [
        _p("lamp", {"srTerm": "−1 (off)", "srSum": "1023/1024"}, n=10),
        _p("odd", {"srTerm": "+1 (on)", "srSum": "2047/2048"}, n=11),
        _p("long", {"srRemain": "1/1073741824"}, n=30),
    ]}),
    # ------------------------------------------------------------------ game
    ("5.1 best responses", {"mode": "game", "view": "best", "presets": [
        _p("coordination", {"gaPure": "(L, L); (R, R)"}, rows=["L", "R"], cols=["L", "R"],
           payoffs=[[[1, 1], [0, 0]], [[0, 0], [1, 1]]]),
        _p("unique", {"gaPure": "(D, D)"}, rows=["C", "D"], cols=["C", "D"], payoffs=PD),
        _p("none-pure", {"gaPure": "none", "gaMixed": "row H: 1/2, col H: 1/2"}, rows=["H", "T"], cols=["H", "T"],
           payoffs=[[[1, -1], [-1, 1]], [[-1, 1], [1, -1]]]),
    ]}),
    ("5.2 prisoner's dilemma", {"mode": "game", "view": "dominance", "presets": [
        _p("pd", {"gaDom": "D dominates for both", "gaPure": "(D, D)",
                  "gaPareto": "(D, D) is dominated by (C, C)"}, rows=["C", "D"], cols=["C", "D"], payoffs=PD),
        _p("not-pd", {"gaPure": "(C, C); (D, D)", "gaDom": "none"}, rows=["C", "D"], cols=["C", "D"],
           payoffs=[[[4, 4], [0, 3]], [[3, 0], [1, 1]]]),
        _p("iterated", {"gaDom": "iterated elimination leaves (Up, Middle)", "gaMixed": "—"},
           rows=["Up", "Down"], cols=["Left", "Middle", "Right"],
           payoffs=[[[1, 0], [1, 2], [0, 1]], [[0, 3], [0, 1], [2, 0]]]),
    ]}),
    ("5.3 mixed", {"mode": "game", "presets": [
        _p("chicken", {"gaMixed": "row Swerve: 9/10, col Swerve: 9/10",
                       "gaPure": "(Swerve, Straight); (Straight, Swerve)"}, rows=["Swerve", "Straight"],
           cols=["Swerve", "Straight"], payoffs=[[[0, 0], [-1, 1]], [[1, -1], [-10, -10]]]),
        _p("stag", {"gaMixed": "row Stag: 3/4, col Stag: 3/4", "gaPareto": "(Hare, Hare) is dominated by (Stag, Stag)"},
           rows=["Stag", "Hare"], cols=["Stag", "Hare"], payoffs=[[[4, 4], [0, 3]], [[3, 0], [3, 3]]]),
    ]}),
    ("5.8 hobbes", {"mode": "game", "presets": [
        _p("anarchy", {"gaDom": "Attack dominates for both"}, rows=["Peace", "Attack"], cols=["Peace", "Attack"],
           payoffs=PD),
        _p("sovereign", {"gaDom": "Peace dominates for both", "gaPure": "(Peace, Peace)"}, rows=["Peace", "Attack"],
           cols=["Peace", "Attack"], payoffs=[[[3, 3], [0, 1]], [[1, 0], [-3, -3]]]),
    ]}),
    # -------------------------------------------------------------- iterated
    ("5.5 tournament", {"mode": "iterated", "a": "TFT", "b": "ALLD", "rounds": 10, "presets": [
        _p("tft-alld", {"itScoreA": "9", "itScoreB": "14"}, R=3, S=0, T=5, P=1),
        _p("tft-tft", {"itScoreA": "30", "itScoreB": "30"}, R=3, S=0, T=5, P=1, a="TFT", b="TFT"),
        _p("grim-pavlov", {"itScoreA": "30", "itScoreB": "30"}, R=3, S=0, T=5, P=1, a="GRIM", b="PAVLOV"),
    ]}),
    ("5.6 shadow of the future", {"mode": "iterated", "presets": [
        _p("standard", {"itThresh": "GRIM 1/2, TFT 2/3: δ = 9/10 sustains"}, R=3, S=0, T=5, P=1, delta="9/10"),
        _p("low-delta", {"itThresh": "GRIM 1/2, TFT 2/3: δ = 1/4 does not"}, R=3, S=0, T=5, P=1, delta="1/4"),
        _p("high-temptation", {"itThresh": "GRIM 4/9, TFT 2/3: δ = 3/5 sustains GRIM only"}, R=6, S=0, T=10,
           P=1, delta="3/5"),
    ]}),
    ("5.7 hume's farmers", {"mode": "iterated", "presets": [
        _p("farmers-once", {"itScoreA": "0", "itScoreB": "5"}, R=3, S=0, T=5, P=1, rounds=1),
        _p("farmers-season", {"itScoreA": "36", "itScoreB": "36"}, R=3, S=0, T=5, P=1, rounds=12, a="TFT", b="TFT"),
        _p("farmers-suspicious", {"itScoreA": "30", "itScoreB": "30"}, R=3, S=0, T=5, P=1, rounds=12, a="STFT",
           b="TFT"),
    ]}),
    # --------------------------------------------------------------- commons
    ("5.10 public goods", {"mode": "commons", "presets": [
        _p("public-goods", {"cmDom": "Defect dominates", "cmUniv": "alone +7, everyone −20",
                            "cmOpt": "all 10 cooperate: total 200", "cmEq": "k* = 0"}, n=10, **PGOOD),
        _p("small-group", {"cmDom": "Cooperate dominates", "cmUniv": "alone −5, everyone −20"}, n=2,
           **PGOOD),
        _p("threshold", {"cmDom": "neither", "cmOpt": "all 10 cooperate: total 900",
                         "cmEq": "k* = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"}, n=10, payC="10*10*(k+1)/n - 10",
           payD="10*10*k/n"),
    ]}),
    ("5.11 evolution", {"mode": "commons", "gens": 5, "presets": [
        _p("pd-evolve", {"cmShare": "3/17"}, n=2, payC="3k", payD="4k + 1", x0="1/2", gens=2),
        _p("stag-evolve", {"cmDom": "neither"}, n=2, payC="4k", payD="3", x0="4/5"),
    ]}),
    ("6.7 universalisation", {"mode": "commons", "presets": [
        _p("false-promise", {"cmUniv": "alone +3, everyone −2", "cmDom": "neither", "cmEq": "k* = 4"}, n=10,
           payC="2", payD="5k/(n - 1)"),
    ]}),
    ("5.9 herders", {"mode": "commons", "presets": [
        _p("herders", {"cmDom": "Defect dominates"}, n=10, payC="(20 - (n - k - 1)) * 1", payD="(20 - (n - k)) * 2"),
    ]}),
    # ------------------------------------------------------------------ vote
    ("7.5 condorcet", {"mode": "vote", "rule": "condorcet", "presets": [
        _p("cycle", {"voCondorcet": "cycle: A > B > C > A", "voWinner": "none"}, kind="ranking", profile=CYCLE),
        _p("winner", {"voCondorcet": "B", "voWinner": "B"}, kind="ranking", profile=THREE),
    ]}),
    ("7.6 rules disagree", {"mode": "vote", "rule": "plurality", "presets": [
        _p("three-winners", {"voWinner": "A", "voCondorcet": "B"}, kind="ranking", profile=THREE),
        _p("spoiler", {"voWinner": "A"}, kind="ranking", profile=[{"count": 5, "rank": "A B C"},
                                                                  {"count": 4, "rank": "B A C"},
                                                                  {"count": 2, "rank": "C B A"}]),
    ]}),
    ("7.7 arrow", {"mode": "vote", "rule": "plurality", "remove": "nobody", "presets": [
        _p("iia-plurality", {"voIIA": "violated (remove B)", "voWinner": "A"}, kind="ranking", profile=THREE),
        _p("dictator", {"voIIA": "holds", "voWinner": "A"}, kind="ranking", profile=[{"count": 1, "rank": "A B C"}]),
    ]}),
    ("7.7 remove C", {"mode": "vote", "rule": "plurality", "remove": "C", "presets": [
        _p("iia-plurality", {"voIIA": "violated (remove C)", "voWinner": "B"}, kind="ranking", profile=THREE),
    ]}),
    ("7.8 manipulation", {"mode": "vote", "rule": "borda", "presets": [
        _p("safe", {"voManip": "none found", "voWinner": "A"}, kind="ranking",
           profile=[{"count": 3, "rank": "A B"}, {"count": 2, "rank": "B A"}]),
        _p("borda-manip", {"voWinner": "A"}, kind="ranking",
           profile=[{"count": 3, "rank": "A B C"}, {"count": 2, "rank": "B A C"}]),
    ]}),
    ("7.9 judgment", {"mode": "vote", "presets": [
        _p("court", {"voWinner": "premise-based: T; conclusion-based: F", "voCondorcet": "premises T, T; conclusion F"},
           kind="judgment", atoms=["p", "q"], formula="p&q", voters=[[1, 1, 1], [1, 0, 0], [0, 1, 0]]),
        _p("consistent-court", {"voWinner": "premise-based: T; conclusion-based: T"}, kind="judgment",
           atoms=["p", "q"], formula="p&q", voters=[[1, 1], [1, 1], [0, 1]]),
        _p("disjunction", {"voWinner": "premise-based: F; conclusion-based: T"}, kind="judgment", atoms=["p", "q"],
           formula="p|q", voters=[[1, 0], [0, 1], [0, 0]]),
    ]}),
    ("7.10 jury", {"mode": "vote", "presets": [
        _p("three", {"voJury": "81/125", "voPivot": "12/25"}, kind="jury", n=3, p="3/5"),
        _p("eleven", {"voPivot": "%d/%d" % (252 * 6 ** 5, 25 ** 5)}, kind="jury", n=11, p="3/5"),
        _p("incompetent", {"voJury": "44/125", "voPivot": "12/25"}, kind="jury", n=3, p="2/5"),
    ]}),
    # ------------------------------------------------------------- aggregate
    ("6.3 utilitarianism", {"mode": "aggregate", "rule": "total", "presets": [
        _p("equal-vs-skewed", {"agVerdict": "B ≻ A", "agScores": "30 vs 33", "agGini": "0 vs 58/99"},
           A=[10, 10, 10], B=[1, 30, 2]),
        _p("sacrifice", {"agVerdict": "B ≻ A", "agScores": "30 vs 31"}, A=[10, 10, 10], B=[0, 15, 16]),
    ]}),
    ("6.4 population", {"mode": "aggregate", "rule": "total", "presets": [
        _p("repugnant", {"agRepug": "n* = 301"}, A=[10, 10, 10], B=[10, 10, 10], eps="1/10"),
        _p("mere-addition", {"agVerdict": "B ≻ A", "agScores": "30 vs 34"}, A=[10, 10, 10], B=[10, 10, 10, 2, 2]),
    ]}),
    ("6.5 priority", {"mode": "aggregate", "rule": "prioritarian", "presets": [
        _p("levelling-down", {"agVerdict": "A ≻ B", "agScores": "27 vs 15"}, A=[10, 10, 10], B=[5, 5, 5], knee=8),
        _p("priority", {"agVerdict": "A ~ B", "agScores": "17 vs 17"}, A=[6, 14], B=[9, 9], knee=8),
    ]}),
    ("7.2 difference principle", {"mode": "aggregate", "rule": "leximin", "presets": [
        _p("incentive", {"agVerdict": "B ≻ A", "agScores": "worst 5 vs 6"}, A=[5, 5, 5], B=[6, 9, 20]),
        _p("tie-at-the-bottom", {"agVerdict": "A ≻ B", "agScores": "2nd worst 5 vs 3"}, A=[2, 5, 9], B=[2, 7, 3]),
        _p("pure-equality", {"agVerdict": "A ~ B", "agScores": "equal at every rank"}, A=[4, 4], B=[4, 4]),
    ]}),
    ("7.3 entitlement", {"mode": "aggregate", "rule": "total", "presets": [
        _p("chamberlain", {"agGini": "0 vs 3/40", "agVerdict": "A ~ B"}, A=[10, 10, 10, 10], B=[9, 9, 9, 13]),
    ]}),
    ("sufficiency", {"mode": "aggregate", "rule": "sufficientarian", "presets": [
        _p("below", {"agScores": "below 1 vs 2", "agVerdict": "A ≻ B"}, A=[3, 6, 9], B=[4, 4, 20], threshold=5),
    ]}),
    # --------------------------------------------------------------- simpson
    ("2.10 reference class", {"mode": "simpson", "weight": "pooled", "presets": [
        _p("kidney", {"siPooled": "A 273/350 vs B 289/350: B higher", "siGroup1": "A higher", "siGroup2": "A higher"},
           names=["A", "B"], groups=KIDNEY),
    ]}),
    ("3.8 simpson", {"mode": "simpson", "weight": "pooled", "presets": [
        _p("kidney", {"siVerdict": "Reversal", "siAdjusted": "A 273/350 vs B 289/350: B higher"}, names=["A", "B"],
           groups=KIDNEY),
        _p("no-reversal", {"siVerdict": "No reversal"}, names=["A", "B"],
           groups=[{"name": "g1", "a": [8, 10], "b": [6, 10]}, {"name": "g2", "a": [4, 10], "b": [2, 10]}]),
    ]}),
    ("7.4 berkeley", {"mode": "simpson", "weight": "standardised", "presets": [
        _p("berkeley", {"siVerdict": "No reversal", "siAdjusted": "men 1/2 vs women 1/2: equal",
                        "siPooled": "men 84/120 vs women 36/120: men higher"}, names=["men", "women"],
           groups=[{"name": "dept 1", "a": [80, 100], "b": [16, 20]}, {"name": "dept 2", "a": [4, 20], "b": [20, 100]}]),
        _p("kidney-standardised", {"siAdjusted": "A 634983/762700 vs B 6231/8000: A higher", "siVerdict": "Reversal"},
           names=["A", "B"], groups=KIDNEY),
    ]}),
]

TILES = {
    "decide": ["deChoice", "deValue", "deVpi", "deFlip"],
    "update": ["upPost", "upBF", "upConf", "upPred", "upBest"],
    "credence": ["crAccepted", "crPAll", "crConsistent", "crBook"],
    "series": ["srTerm", "srSum", "srLimit", "srRemain"],
    "game": ["gaPure", "gaMixed", "gaDom", "gaPareto"],
    "iterated": ["itScoreA", "itScoreB", "itWinner", "itThresh"],
    "commons": ["cmDom", "cmEq", "cmOpt", "cmUniv", "cmShare"],
    "vote": ["voWinner", "voCondorcet", "voIIA", "voManip", "voJury", "voPivot"],
    "aggregate": ["agVerdict", "agScores", "agGini", "agRepug"],
    "simpson": ["siPooled", "siGroup1", "siGroup2", "siAdjusted", "siVerdict"],
}
CONTROLS = {
    "decide": ["dePreset", "deActs", "deStates", "deMatrix", "deProbs", "deCond", "deForbid", "deRule"],
    "update": ["upPreset", "upPrior", "upLik", "upData", "upPay", "upHyp"],
    "credence": ["crPreset", "crKind", "crN", "crP", "crThreshold", "crEvents", "crTyped"],
    "series": ["srPreset", "srKind", "srA", "srR", "srN", "srCap"],
    "game": ["gaPreset", "gaRows", "gaCols", "gaMatrix", "gaView"],
    "iterated": ["itPreset", "itPay", "itA", "itB", "itRounds", "itDelta"],
    "commons": ["cmPreset", "cmN", "cmPC", "cmPD", "cmX0", "cmGens"],
    "vote": ["voPreset", "voKind", "voProfile", "voRule", "voRemove"],
    "aggregate": ["agPreset", "agA", "agB", "agRule", "agKnee", "agThresh", "agEps"],
    "simpson": ["siPreset", "siNames", "siTable", "siWeight"],
}
PREFIX = {"decide": "de", "update": "up", "credence": "cr", "series": "sr", "game": "ga", "iterated": "it",
          "commons": "cm", "vote": "vo", "aggregate": "ag", "simpson": "si"}


class TestEveryModeBuilds(unittest.TestCase):
    def test_every_mode_is_covered(self):
        self.assertEqual(sorted({cfg["mode"] for _, cfg in FIXTURES}), sorted(choicekit.MODES))

    def test_every_fixture_builds(self):
        for name, cfg in FIXTURES:
            with self.subTest(lesson=name):
                lab = labs.build("choicekit", cfg)
                mode, pre = cfg["mode"], PREFIX[cfg["mode"]]
                page = lab.markup + lab.controls
                for tile in TILES[mode]:
                    self.assertIn('<strong id="%s">' % tile, page)
                for control in CONTROLS[mode]:
                    self.assertIn('id="%s"' % control, page)
                self.assertIn('id="%sStatus"' % pre, page)
                self.assertIn('class="kpi-grid"', page)
                self.assertIn("window.redrawLab = redraw;", lab.script)
                self.assertIn("var PRESETS = ", lab.script)
                self.assertEqual(list(lab.expect), ["%sPreset" % pre])
                self.assertEqual(list(lab.expect["%sPreset" % pre]), [p["id"] for p in cfg["presets"]])
                for p in cfg["presets"]:
                    self.assertIn('<option value="%s"' % p["id"], lab.controls)
                # no control ships a value containing ">"
                for value in re.findall(r'value="([^"]*)"', lab.controls):
                    self.assertNotIn(">", value)

    def test_a_page_ships_one_mode(self):
        lab = labs.build("choicekit", FIXTURES[0][1])
        self.assertIn("function deDecide", lab.script)
        for other in ("function upSolve", "function voWinners", "function gaMixed", "function cmParse"):
            self.assertNotIn(other, lab.script)

    def test_script_is_es5_apart_from_bigint(self):
        blocks = [choicekit.CK_COMMON_JS, choicekit.DECIDE_JS, choicekit.UPDATE_JS, choicekit.CREDENCE_JS,
                  choicekit.SERIES_JS, choicekit.GAME_JS, choicekit.ITERATED_JS, choicekit.COMMONS_JS,
                  choicekit.VOTE_JS, choicekit.AGGREGATE_JS, choicekit.SIMPSON_JS, choicekit._HEAD, choicekit._TAIL]
        for _, cfg in FIXTURES:
            blocks.append(labs.build("choicekit", cfg).script)
        for i, js in enumerate(blocks):
            for token in ("=>", "`", "?.", "??", "fetch(", "XMLHttpRequest"):
                self.assertFalse(token in js, "block %d contains %r" % (i, token))
            self.assertIsNone(re.search(r"\b(let|const|class)\s", js), "block %d" % i)
            self.assertIsNone(re.search(r"\(\?<[=!]", js), "block %d" % i)

class TestRefusals(unittest.TestCase):
    def bad(self, cfg, needle):
        with self.assertRaises(ValueError) as ctx:
            labs.build("choicekit", cfg)
        self.assertIn(needle, str(ctx.exception))

    def test_unknown_mode(self):
        self.bad({"mode": "nope"}, "unknown mode")
        self.bad({}, "unknown mode")

    def test_ragged_and_bad_probabilities_name_the_preset(self):
        self.bad({"mode": "decide", "presets": [_p("rag", acts=["a", "b"], states=["x", "y"],
                                                   payoffs=[[1, 2], [3]])]}, "'rag'")
        self.bad({"mode": "decide", "presets": [_p("sum", probs=["1/2", "1/3"], **UMBRELLA)]}, "'sum'")
        self.bad({"mode": "update", "presets": [_p("lik", hyps=["a"], outcomes=["x", "y"], prior=[1],
                                                   lik=[["1/2", "1/3"]])]}, "'lik'")
        self.bad({"mode": "decide", "presets": [_p("six", acts=list("abcdef"), states=["x"],
                                                   payoffs=[[1]] * 6)]}, "'six'")

    def test_unknown_strategy_and_non_dilemma(self):
        self.bad({"mode": "iterated", "presets": [_p("s", R=3, S=0, T=5, P=1, a="NICE")]}, "unknown strategy")
        self.bad({"mode": "iterated", "presets": [_p("t", R=3, S=0, T=10, P=1)]}, "2R > T + S")

    def test_a_preset_never_sets_a_redraw_only_control(self):
        self.bad({"mode": "decide", "presets": [_p("r", rule="eu", **UMBRELLA)]}, "redraw-only")
        self.bad({"mode": "series", "kind": "geometric", "presets": [_p("k", kind="lamp")]}, "redraw-only")

    def test_bad_lesson_level_choice(self):
        self.bad({"mode": "decide", "rule": "vibes", "presets": [_p("u", **UMBRELLA)]}, "vibes")
        self.bad({"mode": "vote", "remove": "Z", "presets": [_p("v", kind="ranking", profile=THREE)]}, "remove")

    def test_missing_expect_is_not_a_build_error(self):
        lab = labs.build("choicekit", {"mode": "game", "presets": [{"id": "x", "label": "x", "rows": ["a", "b"],
                                                                     "cols": ["c", "d"], "payoffs": PD}]})
        self.assertEqual(lab.expect, {"gaPreset": {"x": {}}})


if __name__ == "__main__":
    unittest.main()
