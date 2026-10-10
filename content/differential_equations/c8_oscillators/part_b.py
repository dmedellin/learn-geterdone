"""Oscillators, Damping and Resonance -- the second half.

Critical damping as a design choice; then the steady push applied from outside:
the undamped forced response, resonance and beats, and the damped response with
its finite peak.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py (mode
oscillator), by executing its shipped JavaScript under node, and pinned in
`expect`. A figure that is rounded is printed with the approximation sign and
says so; a surd is exact and is printed with its rounded value beside it;
everything else is an exact fraction.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "critical-damping-and-design",
        "title": "Critical Damping and Design",
        "module": "Damping",
        "one_line": "Write the critically damped solution (C₁ + C₂·t)·e^(rt), decide exactly whether and when it crosses zero, and say why a door closer is set at critical damping.",
        "summary": (
            "At critical damping the characteristic equation has one repeated root, and "
            "the motion is a straight line in `t` times a decaying exponential. A straight "
            "line has at most one zero, so the motion crosses its rest position at most "
            "once, and two constants fitted from the start decide whether it does. "
            "Critical damping has the fastest long-run decay of any damper, which is why "
            "it is the target for a door closer, and it is not the quickest in every sense."
        ),
        "key": [
            "x = (C₁ + C₂·t)·e^(rt)     r = −c/(2m)",
            "C₁ = x₀            C₂ = v₀ − r·x₀",
            "zero at t = −C₁/C₂, only if t > 0",
            "at most one crossing, never two",
            "no other c decays faster in the long run",
        ],
        "key_label": "A line times a decay, and the damping a designer picks",
        "concepts_intro": (
            "Three ideas: the solution and its two constants, the count of zeros that the "
            "form allows, and what a designer gets by sitting on the border."
        ),
        "concepts": [
            ("The solution is a straight line times a decay",
             "At `c² = 4mk` the quadratic `m·r² + c·r + k` has the single root "
             "`r = −c/(2m)`, and &ldquo;Repeated Roots&rdquo; in the previous course gave "
             "the solution `x = (C₁ + C₂·t)·e^(rt)`. Put `t = 0` in it and in its rate "
             "and the constants follow from the start: `C₁ = x₀` and `C₂ = v₀ − r·x₀`. "
             "The second constant is not the starting velocity. It is the velocity with "
             "the decay's own contribution taken off."),
            ("A straight line has one zero, so there is at most one crossing",
             "The exponential `e^(rt)` is never zero, so `x = 0` exactly when "
             "`C₁ + C₂·t = 0`. That is `t = −C₁/C₂` when `C₂ ≠ 0`, and it counts only if it "
             "is positive. An underdamped motion crosses zero again and again; a "
             "critically damped one cannot, whatever the start."),
            ("Critical damping is the border, and the border is a design target",
             "Below `c_crit` the motion oscillates; above it, it creeps because the slow "
             "root moves toward zero. At `c_crit` the slow root is as far from zero as "
             "any damper can put it, so the long-run decay is the fastest there is. A "
             "door closer is built toward this value: the door shuts without swinging "
             "back and without taking all afternoon."),
        ],
        "read_title": "The border between ringing and creeping",
        "read_intro": "The solution form and its constants, the count of crossings with a proof, two starts on one damper, and the reason the damper on a door sits at the border.",
        "body": [
            ("p", "&ldquo;Overdamped, Critical and Underdamped&rdquo; sorted dampers into "
                  "three kinds by the sign of `c² − 4mk`, and the lesson after it followed "
                  "the underdamped kind. This lesson takes the middle kind, the single value "
                  "`c = 2√(mk)` where the sign is zero, and asks what it is good for. The "
                  "answer has two parts: a form of solution simple enough to settle exactly "
                  "whether the mass crosses its rest position, and a reason a designer wants "
                  "to land there."),
            ("def", ("Critically damped motion",
                     "When `c² = 4mk` the characteristic equation `m·r² + c·r + k = 0` has "
                     "the double root `r = −c/(2m)`, and the motion is "
                     "`x = (C₁ + C₂·t)·e^(rt)`. It does not oscillate.",
                     "For `m = 1`, `c = 4`, `k = 4` the root is `r = −2`. At critical "
                     "damping the root is also `−ω₀`, minus the natural frequency.")),
            ("math", [
                "x = (C₁ + C₂·t)·e^(rt)",
                "x′ = (C₂ + r·C₁ + r·C₂·t)·e^(rt)",
                "x(0) = C₁                x′(0) = C₂ + r·C₁",
                "C₁ = x₀                  C₂ = v₀ − r·x₀",
            ]),
            ("thm", ("A critically damped motion crosses zero at most once",
                     "If `x = (C₁ + C₂·t)·e^(rt)` is not the zero function, there is at most "
                     "one `t > 0` with `x = 0`, and there is one exactly when `C₁` and "
                     "`C₂` are both nonzero and have opposite signs.")),
            ("proof", ["The factor `e^(rt)` is positive for every `t`, so `x = 0` exactly "
                       "where the factor `C₁ + C₂·t` is zero.",
                       "That factor is a straight line. If `C₂ = 0` it is the constant "
                       "`C₁`, which is zero only if the whole motion is zero. If "
                       "`C₂ ≠ 0` it is zero only at `t = −C₁/C₂`, which is positive "
                       "exactly when `C₁` and `C₂` have opposite signs, and a line cannot "
                       "meet the axis twice."]),
            ("h3", "Two starts on one damper"),
            ("p", "Take `m = 1`, `k = 4` and `c = 4`, which is `c_crit = 2√4`. The root is "
                  "`r = −2`, and the lab's tile for the zero crossing says when, or that "
                  "there is none. The only thing that changes between the two starts is the "
                  "velocity."),
            ("math", [
                "start (1, 1):   C₁ = 1   C₂ = 1 − (−2)·1 = 3",
                "                x = (1 + 3t)·e^(−2t)     zero at t = −1/3",
                "start (1, −5):  C₁ = 1   C₂ = −5 − (−2)·1 = −3",
                "                x = (1 − 3t)·e^(−2t)     zero at t = 1/3",
            ]),
            ("example", ("Pushed outward: no crossing",
                         "Release the mass at `x = 1` moving outward at speed `1`. The "
                         "constants are `C₁ = 1` and `C₂ = 3`, both positive, so the line "
                         "`1 + 3t` is positive for every `t > 0` and its zero, `−1/3`, "
                         "lies in the past. The lab reports no zero for `t > 0`.",
                         "The mass drifts out a little further and then decays to rest "
                         "from above. It never reaches the rest position.")),
            ("example", ("Pushed hard inward: one crossing",
                         "Release it at `x = 1` moving inward at speed `5`. Now "
                         "`C₂ = −5 + 2 = −3`, which has the opposite sign to `C₁ = 1`. The "
                         "line `1 − 3t` is zero at `t = 1/3`, which the lab prints. The "
                         "mass passes through the rest position once, goes to the far "
                         "side, and creeps back from below.",
                         "Critical damping does not forbid an overshoot. It forbids a "
                         "second crossing, because the form has room for only one.")),
            ("h3", "Why a door closer sits at the border"),
            ("p", "Model the door as a mass, the closing spring as `k`, and the oil "
                  "damper as `c`. Let `x` be the angle from shut, so that `x = 0` is the "
                  "door at its frame. Someone opens the door and lets go, which is a start "
                  "from rest, `v₀ = 0`. Then `C₂ = −r·x₀ = (c/(2m))·x₀`, which has the same "
                  "sign as `C₁ = x₀`, so by the theorem the door never crosses shut. A "
                  "weaker damper would swing it through the frame and back; "
                  "a stronger one would close it slowly."),
            ("p", "The word &ldquo;slowly&rdquo; can be measured. For `m = 1` and `k = 4` the "
                  "long-run decay is `e^(−t)` at `c = 2` (the envelope rate `c/(2m)`), "
                  "`e^(−2t)` at `c = 4`, and `e^(−t)` again at `c = 5`, whose slow root is "
                  "`−1`. The rate rises to a maximum at `c_crit` and then falls. The "
                  "reason is that the two roots multiply to `k/m = 4`: past the border, "
                  "raising `c` pushes the fast root outward and the slow root toward zero."),
            ("p", "That is a claim about the long run, and only about the long run. A "
                  "damper a little below critical reaches the rest position in finite "
                  "time, which a critically damped door released from rest never does, "
                  "and it then overshoots. So the designer is trading one failure for the "
                  "other, and critical damping is where neither one happens."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "no-cross",
            "presets": [
                {"id": "no-cross", "label": "c = 4, start (1, 1)",
                 "m": 1, "c": 4, "k": 4, "ic": [1, 1], "F0": 0,
                 "expect": {"osType": "critically damped", "osDisc": "0", "osCcrit": "4", "osCross": "none for t > 0"}},
                {"id": "one-cross", "label": "c = 4, start (1, −5)",
                 "m": 1, "c": 4, "k": 4, "ic": [1, -5], "F0": 0,
                 "expect": {"osType": "critically damped", "osDisc": "0", "osCcrit": "4", "osCross": "t = 1/3"}},
                {"id": "from-rest", "label": "c = 4, released from rest",
                 "m": 1, "c": 4, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "critically damped", "osDisc": "0", "osCcrit": "4", "osCross": "none for t > 0"}},
                {"id": "compare-over", "label": "c = 5, released from rest",
                 "m": 1, "c": 5, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "overdamped", "osDisc": "9", "osCcrit": "4"}},
                {"id": "compare-under", "label": "c = 3, released from rest",
                 "m": 1, "c": 3, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "underdamped", "osDisc": "−7", "osCcrit": "4"}},
            ],
            "panel_title": "Fit a critically damped motion and find its zero",
            "panel_intro": (
                "The first three presets share one damper and differ only in the start. Read "
                "the zero-crossing tile for each, then compare the curves of the last two "
                "with the border: c = 5 is overdamped and creeps, c = 3 is underdamped and "
                "swings through zero. The curve is drawn by stepping in floating point; the "
                "class, the discriminant and the crossing time are exact."),
        }),
        "steps_title": "From a critical damper and a start to a crossing time",
        "steps_intro": "Five moves. The third is the one where a velocity is most often used as a constant.",
        "steps": [
            ("Confirm that c² − 4mk is zero",
             "Compute it as a number. If it is not zero the motion is not critically "
             "damped and this solution form does not apply."),
            ("Find the double root",
             "`r = −c/(2m)`. For `m = 1` and `c = 4` it is `−2`; the solution is "
             "`(C₁ + C₂·t)·e^(−2t)`."),
            ("Fit the two constants",
             "`C₁ = x₀`, and `C₂ = v₀ − r·x₀`. The second is the starting velocity with "
             "`r·x₀` taken off, because the derivative of `e^(rt)` contributes `r·C₁` at "
             "`t = 0`. For the start `(1, −5)`: `C₂ = −5 + 2 = −3`."),
            ("Decide the crossing",
             "If `C₂ = 0` there is no zero. Otherwise the candidate is `t = −C₁/C₂`, and it "
             "is a crossing only if it is positive: that is, only if `C₁` and `C₂` have "
             "opposite signs."),
            ("Check the fit against the start",
             "Put `t = 0` back: `x(0) = C₁` must be `x₀`, and `C₂ + r·C₁` must be `v₀`. If "
             "the second check fails, the velocity was used where `v₀ − r·x₀` belongs."),
        ],
        "worked": {
            "title": "x″ + 4x′ + 4x = 0 started at 1 with velocity −5",
            "intro": [
                "The lab preset with start `(1, −5)`: `m = 1`, `c = 4`, `k = 4`, `x(0) = 1`, "
                "`x′(0) = −5`.",
            ],
            "lines": [
                "disc = 16 − 16 = 0      critical,  r = −4/2 = −2",
                "x = (C₁ + C₂·t)·e^(−2t)",
                "C₁ = x₀ = 1",
                "x′(0) = C₂ + r·C₁ = C₂ − 2 = −5",
                "C₂ = −3           x = (1 − 3t)·e^(−2t)",
                "1 − 3t = 0 at t = 1/3 > 0:  one crossing",
            ],
            "after": [
                "Check by substituting: `x′ = (6t − 5)·e^(−2t)` and "
                "`x″ = (16 − 12t)·e^(−2t)`, and then `x″ + 4x′ + 4x` has the bracket "
                "`16 − 12t + 24t − 20 + 4 − 12t = 0`. The lab prints the crossing time "
                "`t = 1/3` in the zero-crossing tile. With the start `(1, 1)` the same "
                "damper gives `C₂ = 3` and no crossing.",
            ],
        },
        "quiz_title": "Constants, crossings and the border",
        "quiz": [
            {"q": "A critically damped motion has `m = 1`, `c = 6`, `k = 9`, `x(0) = 2` and `x′(0) = 1`. What is `C₂`?",
             "a": ["`1`", "`−5`", "`4`", "`7`"],
             "c": 3,
             "why": "`r = −3`, so `C₂ = v₀ − r·x₀ = 1 + 6 = 7`. `1` takes the "
                    "velocity as the constant and forgets `r·x₀`. `−5` is "
                    "`v₀ + r·x₀`, which has the sign of the correction wrong. `4` is "
                    "`v₀ − r`, which leaves out the factor `x₀`."},
            {"q": "With `m = 1`, `c = 4`, `k = 4` the start is `x(0) = 2`, `x′(0) = −7`. When does the mass cross its rest position?",
             "a": ["At `t = 2/3`", "At `t = −2/3`", "At `t = 7/2`", "Never"],
             "c": 0,
             "why": "`r = −2`, `C₁ = 2` and `C₂ = −7 + 4 = −3`. The zero of `2 − 3t` is "
                    "`t = 2/3`, positive, so it is a crossing. `−2/3` drops the sign of "
                    "`C₂`. `7/2` is `−v₀/x₀`, which ignores the decay. And `C₁` and "
                    "`C₂` have opposite signs, so it does cross."},
            {"q": "Which statement about critical damping, for a fixed `m` and `k`, is correct?",
             "a": ["It brings the mass to the rest position in the shortest time",
                   "It guarantees no crossing of the rest position, whatever the start",
                   "No other damping constant gives a faster decay in the long run",
                   "It makes the motion oscillate faster than any other damping constant"],
             "c": 2,
             "why": "The long-run rate is `c/(2m)` below the border and the slow root "
                    "above it, and it peaks at `c_crit`. A critically damped mass released "
                    "from rest never reaches the rest position at all, while an underdamped "
                    "one does in finite time. A start with inward velocity can make "
                    "the critical motion cross once. And a critically damped motion does "
                    "not oscillate."},
            {"q": "A door is released from rest at `x₀ = 1` with critical damping. How many times does it cross the closed position `x = 0`?",
             "a": ["Once", "Never", "Twice", "Infinitely often"],
             "c": 1,
             "why": "From rest, `C₂ = −r·x₀ = (c/(2m))·x₀`, which has the same sign as "
                    "`C₁ = x₀`, so `−C₁/C₂` is negative and there is no crossing. One "
                    "crossing needs an inward start; two are impossible in this form; "
                    "infinitely many belong to an undamped or underdamped door."},
        ],
        "mistakes": [
            ("Believing critical damping is the quickest in every sense",
             "It wins one race, the long-run rate. With `m = 1` and `k = 4` the rate is "
             "`1` at `c = 2`, `3/2` at `c = 3`, `2` at `c = 4` and `1` again at `c = 5`, "
             "so it rises to the border and falls past it. In other senses it loses: "
             "released from rest, the underdamped `c = 3` in the lab reaches the rest "
             "position in finite time and a critical motion never does, and the start "
             "`(1, −5)` makes even the critical motion overshoot once."),
            ("Assuming a critically damped motion never crosses zero",
             "It crosses at most once, and exactly once when `C₁` and `C₂` have opposite "
             "signs. The lab's preset with start `(1, −5)` has `C₁ = 1`, `C₂ = −3` and crosses at "
             "`t = 1/3`. What is true is narrower: a start from rest, as for the door, "
             "never crosses, and the form never allows a second crossing."),
            ("Taking C₂ to be the starting velocity",
             "The rate of `(C₁ + C₂·t)·e^(rt)` at `t = 0` is `C₂ + r·C₁`, not `C₂`. For "
             "the start `(1, −5)` the wrong constant `−5` puts the crossing at "
             "`t = 1/5`, instead of the correct `1/3`. Released from rest, the wrong "
             "constant is `0`, which says the motion is a plain exponential; the correct "
             "`C₂` is `2`."),
        ],
        "standard": (
            "Finish when you can fit a critically damped motion and say whether and when it crosses zero.",
            "You should be able to confirm that c² − 4mk is zero, write (C₁ + C₂·t)·e^(rt) "
            "with r = −c/(2m), compute C₁ = x₀ and C₂ = v₀ − r·x₀ exactly, decide the "
            "crossing time t = −C₁/C₂ and whether it is positive, and explain why a door "
            "closer is built near critical damping."),
        "note": 'Nothing so far has pushed the mass from outside. The next lesson adds a steady, repeating push to the right-hand side and asks how the mass answers it, in &ldquo;Forced Oscillation&rdquo;.',
    },

    # ---------------------------------------------------------------- 07
    {
        "slug": "forced-oscillation",
        "title": "Forced Oscillation",
        "module": "Forcing",
        "one_line": "Fit x_p = A·cos(ωt) to m·x″ + k·x = F₀·cos(ωt), compute A = F₀/(m·(ω₀² − ω²)) exactly, and read its sign.",
        "summary": (
            "Push an undamped mass with a force `F₀·cos(ωt)` and it answers at the "
            "frequency of the push, with an amplitude that is an exact fraction, "
            "`A = F₀/(m·(ω₀² − ω²))`. The sign of `A` says whether the mass moves with the "
            "push or against it, and the size of `A` grows as the push frequency "
            "approaches the natural one."
        ),
        "key": [
            "m·x″ + k·x = F₀·cos(ωt)",
            "x_p = A·cos(ωt)",
            "A = F₀/(m·(ω₀² − ω²)) = F₀/(k − m·ω²)",
            "A > 0 when ω < ω₀, with the push",
            "ω > ω₀:  A < 0, against the push",
        ],
        "key_label": "The push sets the frequency; the spring sets the size",
        "concepts_intro": (
            "Three ideas: why a cosine is the right guess, what the amplitude is made of, "
            "and what its sign records."
        ),
        "concepts": [
            ("A push at frequency ω is answered at frequency ω",
             "The second derivative of `cos(ωt)` is `−ω²·cos(ωt)`, a multiple of itself, "
             "so a cosine of the same frequency as the push can balance it. This is "
             "undetermined coefficients, as in &ldquo;Exponential and Sinusoidal "
             "Forcing&rdquo;. With no damper only even derivatives appear, so no sine "
             "term is needed."),
            ("The amplitude is a fraction with ω₀² − ω² underneath",
             "Substituting `A·cos(ωt)` gives `A·(k − m·ω²) = F₀`. Dividing by `m`, "
             "`A = F₀/(m·(ω₀² − ω²))`. Every symbol in it is a fraction in the lab, so "
             "`A` is exact. Note the squares: it is `ω₀² − ω²` and not `ω₀ − ω`."),
            ("The sign of A says in step or against",
             "If `ω < ω₀` the denominator is positive and `A` has the sign of "
             "`F₀`: the mass peaks when the push peaks. If `ω > ω₀` it is negative, and "
             "the mass is at its most negative when the push is at its most positive. "
             "A fast push on a mass that cannot keep up is answered the wrong way round."),
        ],
        "read_title": "A steady push on a free spring",
        "read_intro": "The forced equation, the substitution that fixes the amplitude, the theorem with its check, and pushes that show the three behaviours.",
        "body": [
            ("p", "Until now the right-hand side of every oscillator equation was zero and "
                  "the motion was whatever the start left it. Add a force from outside "
                  "that alternates with frequency `ω` and size `F₀`, and the equation "
                  "becomes `m·x″ + c·x′ + k·x = F₀·cos(ωt)`. This lesson and the next "
                  "keep the damper off, `c = 0`, so that the mass answers the push and "
                  "nothing carries the answer away. The last lesson of the course puts the "
                  "damper back."),
            ("math", [
                "m·x″ + k·x = F₀·cos(ωt)",
                "x = x_p + C₁cos(ω₀t) + C₂sin(ω₀t)",
            ]),
            ("p", "The second line is the structure from &ldquo;Homogeneous Plus "
                  "Particular&rdquo;: any one solution `x_p` of the forced equation, plus the "
                  "free motion of the unforced one. The free part carries the constants "
                  "`C₁` and `C₂` and is fixed by the start. The part fixed by the push "
                  "alone is `x_p`, and it is the subject of this lesson."),
            ("math", [
                "x_p = A·cos(ωt)",
                "x_p″ = −ω²·A·cos(ωt)",
                "m·(−ω²·A) + k·A = F₀",
                "A·(k − m·ω²) = F₀",
                "A = F₀/(k − m·ω²) = F₀/(m·(ω₀² − ω²))",
            ]),
            ("thm", ("The forced amplitude",
                     "If `ω² ≠ ω₀²` then `x_p = A·cos(ωt)` with "
                     "`A = F₀/(m·(ω₀² − ω²))` is a solution of "
                     "`m·x″ + k·x = F₀·cos(ωt)`, and it is the only solution of the form "
                     "`A·cos(ωt) + B·sin(ωt)`.")),
            ("proof", ["Substitute: `m·x_p″ + k·x_p = (k − m·ω²)·A·cos(ωt)`, and "
                       "`(k − m·ω²)·A = m·(ω₀² − ω²)·A = F₀`, so the left side is "
                       "`F₀·cos(ωt)`.",
                       "For a sine term `B·sin(ωt)` the same substitution gives "
                       "`(k − m·ω²)·B·sin(ωt)`, which must be zero, and `k − m·ω² ≠ 0`, so "
                       "`B = 0`. Dividing by `k − m·ω²` is allowed exactly when `ω² ≠ ω₀²`, "
                       "which is why the next lesson exists."]),
            ("h3", "Four pushes on one spring"),
            ("p", "Take `m = 1`, `k = 4` and `F₀ = 3`, so `ω₀² = 4` and `ω₀ = 2`. The "
                  "push `3·cos(ωt)` is tried at four frequencies, the lab starts the "
                  "mass at rest at the rest position each time, and the tile "
                  "reads the amplitude."),
            ("math", [
                "ω = 1:    A = 3/(4 − 1) = 1",
                "ω = 3/2:  A = 3/(4 − 9/4) = 12/7",
                "ω = 7/4:  A = 3/(4 − 49/16) = 16/5",
                "ω = 3:    A = 3/(4 − 9) = −3/5",
            ]),
            ("example", ("Below the natural frequency",
                         "For `ω = 1`, `x_p = cos(t)`, and `A = 1`. Started at rest at "
                         "the rest position, the whole motion is "
                         "`x = cos(t) − cos(2t)`: it has `x(0) = 0` and `x′(0) = 0`, and "
                         "`x″ + 4x = −cos(t) + 4cos(2t) + 4cos(t) − 4cos(2t) = 3cos(t)`.",
                         "The curve the lab draws is that sum of two cosines. The tile "
                         "reports the first one, the part fixed by the push, and it "
                         "moves with the push.")),
            ("example", ("Above the natural frequency",
                         "For `ω = 3`, `A = −3/5`. The push is `3·cos(3t)`, and the "
                         "response is `−(3/5)·cos(3t)`: when the force is pulling the mass "
                         "to the right, the response is to the left. The whole motion from "
                         "rest is `−(3/5)·cos(3t) + (3/5)·cos(2t)`.",
                         "The mass is too sluggish to follow a push this fast. It is still "
                         "going the old way when the force turns, and the spring "
                         "reverses it before the next push.")),
            ("p", "The two extremes make sense of the formula. As `ω` falls toward zero "
                  "the push becomes a slow steady pull, and `A` tends to `F₀/k`, the "
                  "stretch Hooke's law gives for that force. As `ω` rises the amplitude "
                  "shrinks toward zero from below: inertia wins. Between them, near "
                  "`ω₀`, the denominator `ω₀² − ω²` is small and the amplitude is large, "
                  "as the pushes at `3/2` and `7/4` show: `12/7` and then `16/5`."),
            ("p", "One tile will look odd. While the push is on, the lab's period tile "
                  "reads the beat period of the two cosines when the natural frequency is "
                  "rational. It means something specific, and the next lesson explains it."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "below",
            "presets": [
                {"id": "below", "label": "ω = 1, below ω₀",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": 1,
                 "expect": {"osOmega0Sq": "4", "osForced": "A = 1"}},
                {"id": "near", "label": "ω = 3/2, near ω₀",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": "3/2",
                 "expect": {"osOmega0Sq": "4", "osForced": "A = 12/7"}},
                {"id": "closer", "label": "ω = 7/4, nearer ω₀",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": "7/4",
                 "expect": {"osOmega0Sq": "4", "osForced": "A = 16/5"}},
                {"id": "above", "label": "ω = 3, above ω₀",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": 3,
                 "expect": {"osOmega0Sq": "4", "osForced": "A = −3/5"}},
            ],
            "panel_title": "Push the same spring at four frequencies",
            "panel_intro": (
                "Mass, spring and force are fixed; only the frequency of the push changes. Read "
                "the forced-response tile for each preset and say whether the sign puts the "
                "mass with the push or against it, then type your own frequency and predict "
                "the tile before you read it. The curve is drawn by stepping in floating "
                "point; the amplitude A is an exact fraction."),
        }),
        "steps_title": "From a push to an amplitude and a sign",
        "steps_intro": "Five moves. The second is the one that decides whether the formula can be used at all.",
        "steps": [
            ("Read the five numbers",
             "The mass `m`, the spring constant `k`, the size of the push `F₀` and its "
             "frequency `ω`, with the damper absent. Compute `ω₀² = k/m` as a fraction."),
            ("Compare ω² with ω₀²",
             "If they are equal, stop: the formula divides by zero and the next lesson "
             "takes over. Otherwise note which is larger, because that will be the sign."),
            ("Compute the amplitude",
             "`A = F₀/(k − m·ω²)`. Do the subtraction in the denominator as a fraction "
             "first, then divide. For `ω = 3/2`: `4 − 9/4 = 7/4`, and `3/(7/4) = 12/7`."),
            ("Read the sign",
             "Positive: the mass moves with the push. Negative: against it. The size is "
             "`|A|`, and it is the larger the closer `ω²` is to `ω₀²`."),
            ("Check by substitution",
             "`m·(−ω²·A) + k·A` must equal `F₀`. For `ω = 3`, `A = −3/5`: "
             "`−9·(−3/5) + 4·(−3/5) = 27/5 − 12/5 = 3`."),
        ],
        "worked": {
            "title": "x″ + 4x = 3cos(t), and then the push at ω = 3",
            "intro": [
                "The lab presets for `ω = 1` and `ω = 3`: `m = 1`, `k = 4`, `F₀ = 3`, started "
                "at rest at the rest position.",
            ],
            "lines": [
                "ω₀² = 4,  F₀ = 3",
                "ω = 1:  x_p = A·cos(t),  x_p″ = −A·cos(t)",
                "        −A + 4A = 3         A = 1",
                "ω = 3:  x_p = A·cos(3t),  x_p″ = −9A·cos(3t)",
                "        −9A + 4A = 3        A = −3/5",
                "x_p = −(3/5)·cos(3t):  against the push",
            ],
            "after": [
                "Both amplitudes are exact fractions, and the lab prints them as "
                "`A = 1` and `A = −3/5`. The first is positive because `1 < 2`; the "
                "second is negative because `3 > 2`. Nothing in either figure is "
                "rounded.",
            ],
        },
        "quiz_title": "Amplitude, size and sign",
        "quiz": [
            {"q": "A mass `m = 2` on a spring `k = 8` is pushed by `6·cos(t)`. What is the amplitude `A` of the response?",
             "a": ["`2`", "`3`", "`1`", "`−1`"],
             "c": 2,
             "why": "`A = F₀/(k − m·ω²) = 6/(8 − 2) = 1`. `2` is `F₀/(ω₀² − ω²) = 6/3`, "
                    "which forgets the mass. `3` is `F₀/m`, which forgets the spring. "
                    "`−1` has the wrong sign: `ω² = 1` is below `ω₀² = 4`, so the "
                    "denominator is positive."},
            {"q": "The natural frequency is `ω₀ = 2` and the push has `ω = 5`. What can you say about the response before computing anything?",
             "a": ["It is in step with the push, because the push is stronger",
                   "It is exactly against the push, because `ω > ω₀` makes `A` negative",
                   "It has the natural frequency `2`, not the pushing frequency",
                   "It is zero, because the push is faster than the spring"],
             "c": 1,
             "why": "`ω² = 25 > ω₀² = 4`, so `ω₀² − ω²` is negative and `A = F₀/(m·(ω₀² − ω²))` "
                    "is negative. The response is at the pushing frequency `5`, not at "
                    "`2`, so the third choice is wrong. It is small but not zero, and "
                    "the sign has nothing to do with how strong the push is."},
            {"q": "For `m = 1`, `k = 9`, `F₀ = 10` and `ω = 2`, what is `A`?",
             "a": ["`10/13`", "`10`", "`2`", "`−2`"],
             "c": 2,
             "why": "`A = 10/(9 − 4) = 2`. `10/13` adds the squares, `9 + 4`, instead of "
                    "subtracting them. `10` is `10/(3 − 2)`, which subtracts the frequencies "
                    "and not their squares. `−2` has the sign reversed, but `ω = 2` is "
                    "below `ω₀ = 3`."},
            {"q": "For `ω₀ = 2`, `m = 1` and `F₀ = 3`, which push frequency gives the largest `|A|`?",
             "a": ["`ω = 1`", "`ω = 3/2`", "`ω = 3`", "`ω = 7/2`"],
             "c": 1,
             "why": "`|A|` is `1` at `ω = 1`, `12/7` at `3/2`, `3/5` at `3`, and "
                    "`12/33 = 4/11` at `7/2`. The nearer `ω²` is to `ω₀² = 4`, the "
                    "larger `|A|`, and `ω² = 9/4` is the nearest of the four."},
        ],
        "mistakes": [
            ("Believing the response is always in step with the push",
             "It is in step only below the natural frequency. For `ω = 1` the amplitude "
             "is `A = 1` and the mass peaks with the push. For `ω = 3` it is "
             "`A = −3/5`: when the force is at its largest in one direction, the "
             "response is at its largest in the other. The formula carries this in the "
             "sign of `ω₀² − ω²` and needs nothing added."),
            ("Expecting the forced mass to swing at its own frequency",
             "The part of the motion fixed by the push is `A·cos(ωt)`, at the pushing "
             "frequency, and the natural frequency appears only in the free part, whose "
             "constants come from the start. The lab's curve from rest is the sum of "
             "both, `cos(t) − cos(2t)` for the push at `ω = 1`. Neither term is the "
             "answer on its own."),
            ("Subtracting the frequencies instead of their squares",
             "The denominator is `ω₀² − ω²`, because the second derivative brings down "
             "`ω²`. For `ω = 3/2` the right answer is `A = 3/(4 − 9/4) = 12/7`; using "
             "`ω₀ − ω = 1/2` would give `A = 6`, more than three times too large."),
        ],
        "standard": (
            "Finish when you can compute the amplitude of a forced undamped oscillator and say which way it moves.",
            "You should be able to write x_p = A·cos(ωt) for m·x″ + k·x = F₀·cos(ωt), "
            "compute A = F₀/(m·(ω₀² − ω²)) exactly as a fraction, say from its sign "
            "whether the mass moves with the push or against it, and check the answer by "
            "substituting it."),
        "note": 'The formula divides by zero when the push has exactly the natural frequency, and it is large just beside that. What replaces it, and what the motion does, is the subject of &ldquo;Resonance and Beats&rdquo;.',
    },

    # ---------------------------------------------------------------- 08
    {
        "slug": "resonance-and-beats",
        "title": "Resonance and Beats",
        "module": "Forcing",
        "one_line": "Show that the fitted amplitude fails when ω = ω₀, write the resonant solution (F₀/(2m·ω₀))·t·sin(ω₀t), and compute the beat period 2π/|ω₀ − ω| near resonance.",
        "summary": (
            "When the push has exactly the natural frequency, `A·cos(ωt)` cannot be a "
            "solution, and the answer that works is a sine multiplied by `t`: the "
            "amplitude grows in a straight line and never settles. A push just beside "
            "the natural frequency produces beats, a fast oscillation inside a slow "
            "swelling and shrinking envelope whose period is `2π/|ω₀ − ω|`."
        ),
        "key": [
            "ω = ω₀:  A·cos(ωt) cannot work",
            "x_p = (F₀/(2m·ω₀))·t·sin(ω₀t)",
            "amplitude F₀·t/(2m·ω₀): linear growth",
            "ω near ω₀:  beats, period 2π/|ω₀ − ω|",
            "x = 2A·sin((ω₀+ω)t/2)·sin((ω₀−ω)t/2)",
        ],
        "key_label": "Growth at the natural frequency, beats beside it",
        "concepts_intro": (
            "Three ideas: why the guess fails, what replaces it, and what the motion looks "
            "like when the push is near the natural frequency and not on it."
        ),
        "concepts": [
            ("At ω = ω₀ the guess is already a solution of the free equation",
             "When `ω² = ω₀²`, the substitution gives `m·(−ω₀²·A) + k·A = 0` for every "
             "`A`, so `A·cos(ω₀t)` and `B·sin(ω₀t)` both make the left side zero and "
             "neither can equal `F₀·cos(ω₀t)`. It is the situation of a repeated "
             "root in &ldquo;Repeated Roots&rdquo;: the guess is already a free solution, "
             "so it is multiplied by `t`."),
            ("Multiplying by t makes the amplitude grow, and it grows linearly",
             "Try `B·t·sin(ω₀t)`. Its second derivative contains `2B·ω₀·cos(ω₀t)`, "
             "the very cosine the push needs, and the other terms cancel against the "
             "spring. The result is `B = F₀/(2m·ω₀)`, and the amplitude `B·t` grows in "
             "proportion to `t`. It is finite at every moment and has no bound."),
            ("Beside resonance the motion beats",
             "From rest, the response to a push at `ω` is "
             "`A·(cos(ωt) − cos(ω₀t))`, two cosines of nearby frequency. The identity for "
             "the difference of two cosines turns it into a fast sine inside a slow one. "
             "The slow one is an envelope that swells and shrinks, and the swelling "
             "repeats every `2π/|ω₀ − ω|`."),
        ],
        "read_title": "When the push finds the natural frequency",
        "read_intro": "The failure of the amplitude formula, the resonant solution with its check, the beats just beside it, and how the two descriptions join.",
        "body": [
            ("p", "The amplitude `A = F₀/(m·(ω₀² − ω²))` of the previous lesson grows as "
                  "`ω` approaches `ω₀`, and at `ω = ω₀` it has a zero in the denominator. "
                  "That is not a large answer. It is no answer: the form `A·cos(ωt)` "
                  "does not solve the equation at all when the push has the natural "
                  "frequency."),
            ("math", [
                "ω = ω₀:   m·(−ω₀²·A) + k·A = (k − m·ω₀²)·A = 0",
                "           0 = F₀   is impossible for F₀ ≠ 0",
            ]),
            ("p", "The cure is the one used for a repeated root: multiply by `t`. "
                  "Try `x_p = B·t·sin(ω₀t)` and differentiate with the product rule."),
            ("math", [
                "x_p = B·t·sin(ω₀t)",
                "x_p′ = B·sin(ω₀t) + B·ω₀·t·cos(ω₀t)",
                "x_p″ = 2B·ω₀·cos(ω₀t) − B·ω₀²·t·sin(ω₀t)",
                "m·x_p″ + k·x_p = 2m·B·ω₀·cos(ω₀t) + B·(k − m·ω₀²)·t·sin(ω₀t)",
            ]),
            ("thm", ("The resonant solution",
                     "For `ω = ω₀`, the function "
                     "`x_p = (F₀/(2m·ω₀))·t·sin(ω₀t)` solves "
                     "`m·x″ + k·x = F₀·cos(ω₀t)`.")),
            ("proof", ["Since `k = m·ω₀²`, the last term of the display above is "
                       "`B·(k − m·ω₀²)·t·sin(ω₀t) = 0`, so "
                       "`m·x_p″ + k·x_p = 2m·B·ω₀·cos(ω₀t)`.",
                       "Setting `2m·B·ω₀ = F₀` gives `B = F₀/(2m·ω₀)`, and then the "
                       "left side is `F₀·cos(ω₀t)`."]),
            ("example", ("Resonance with m = 1, k = 4, F₀ = 3",
                         "Here `ω₀ = 2`, and the push is `3·cos(2t)`. Then "
                         "`B = 3/(2·1·2) = 3/4` and `x_p = (3/4)·t·sin(2t)`. The check: "
                         "`x_p″ = 3·cos(2t) − 3t·sin(2t)`, so `x_p″ + 4x_p = 3·cos(2t)`, "
                         "the push exactly.",
                         "Started at rest at the rest position, the whole motion is "
                         "`x_p`, because `x_p` and its rate are both zero at `t = 0`. The lab prints it "
                         "in the forced-response tile.")),
            ("p", "The amplitude of this motion is `3t/4`: it is `3` at `t = 4` and `30` "
                  "at `t = 40`. It grows without bound, and it is finite at every moment. "
                  "It does not leap to infinity when the push is switched on; it climbs by "
                  "the same amount in every unit of time. The model has no damper to stop "
                  "the climb, and a real structure has one, or breaks."),
            ("h3", "Beside resonance: beats"),
            ("p", "Move the push to `ω = 3/2` and keep `m = 1`, `k = 4`, `F₀ = 3`. The "
                  "previous lesson gives `A = 12/7`, and from rest the motion is "
                  "`x = A·(cos(ωt) − cos(ω₀t))`. The identity "
                  "`cos(θ) − cos(ψ) = 2·sin((θ + ψ)/2)·sin((ψ − θ)/2)`, which follows from "
                  "the addition and subtraction formulas for the cosine that &ldquo;Amplitude, "
                  "Phase and Period&rdquo; took as given, rewrites it as a product."),
            ("math", [
                "x = 2A·sin((ω₀ + ω)t/2)·sin((ω₀ − ω)t/2)",
                "ω = 3/2:   (ω₀ + ω)/2 = 7/4     (ω₀ − ω)/2 = 1/4",
                "x = (24/7)·sin(7t/4)·sin(t/4)",
            ]),
            ("def", ("Beat period",
                     "In a motion `2A·sin(p·t)·sin(q·t)` with `q` much smaller than `p`, "
                     "the factor `2A·sin(q·t)` is a slowly varying <strong>envelope</strong> "
                     "for the fast factor. The size of the oscillation swells and shrinks, "
                     "and the interval between one swell and the next is the "
                     "<strong>beat period</strong>, `π/q`.",
                     "Here `q = (ω₀ − ω)/2`, so the beat period is `2π/|ω₀ − ω|`.")),
            ("p", "For `ω = 3/2` that is `2π/(1/2) = 4π`, about `12.5664` and rounded, "
                  "which is what the lab prints in the period tile when the push is on. "
                  "The envelope `(24/7)·sin(t/4)` itself repeats every `8π`, but the "
                  "size of the swing, which is its absolute value, repeats every `4π`. The "
                  "largest the swing reaches is `2A = 24/7`, twice the steady amplitude."),
            ("p", "The two descriptions join. Move `ω` toward `ω₀`: the swell height `2A` "
                  "grows without bound and the beat period `2π/|ω₀ − ω|` lengthens without "
                  "bound, so the first swell stretches until it never ends. While `t` is "
                  "small, `sin((ω₀ − ω)t/2)` is close to `(ω₀ − ω)t/2`, and the envelope "
                  "is close to `F₀·t/(m·(ω₀ + ω))`, which tends to the resonant ramp "
                  "`F₀·t/(2m·ω₀)` as `ω → ω₀`. The lab preset for `ω = 7/4` shows "
                  "the swell taller and slower than at `3/2`; the preset at `ω = 2` is the "
                  "limit. That the ramp is the limit is what the lab demonstrates, and it "
                  "is not proved here."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "resonant",
            "presets": [
                {"id": "resonant", "label": "ω = 2 = ω₀",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": 2,
                 "expect": {"osOmega0Sq": "4", "osForced": "resonance: (3/4)·t·sin(2t)"}},
                {"id": "beats", "label": "ω = 3/2",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": "3/2",
                 "expect": {"osForced": "A = 12/7", "osPeriod": "4π ≈ 12.5664"}},
                {"id": "closer", "label": "ω = 7/4",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": "7/4",
                 "expect": {"osForced": "A = 16/5", "osPeriod": "8π ≈ 25.1327"}},
                {"id": "far", "label": "ω = 1/2",
                 "m": 1, "c": 0, "k": 4, "ic": [0, 0], "F0": 3, "w": "1/2",
                 "expect": {"osForced": "A = 4/5", "osPeriod": "4π/3 ≈ 4.18879"}},
            ],
            "panel_title": "Tune the push toward the natural frequency",
            "panel_intro": (
                "Start with the preset at resonance and watch the peaks climb in a straight line. "
                "Then go through the other presets in order of how close the push is to the natural "
                "frequency, and read the beat period beside the amplitude. The curve is drawn by "
                "stepping in floating point; the amplitude is an exact fraction and the beat "
                "period behind ≈ is rounded."),
        }),
        "steps_title": "From a push to resonance or to beats",
        "steps_intro": "Five moves. The first decides which of the two descriptions applies.",
        "steps": [
            ("Compare ω² with ω₀² = k/m",
             "If they are equal the motion is resonant. If they are close but unequal "
             "it beats, and the amplitude of the previous lesson applies."),
            ("At resonance, compute B",
             "`B = F₀/(2m·ω₀)`, and the solution is `B·t·sin(ω₀t)`. For `m = 1`, "
             "`k = 4`, `F₀ = 3`: `ω₀ = 2` and `B = 3/4`. When `ω₀` is a surd, keep it "
             "as a surd in `B`."),
            ("Check by substitution",
             "Find `x_p″` by the product rule and confirm that `m·x_p″ + k·x_p` is "
             "exactly the push. The `t·sin(ω₀t)` terms must cancel and the cosine must "
             "remain."),
            ("Beside resonance, compute the beat period",
             "`2π/|ω₀ − ω|`, using the difference of frequencies, not of squares. For "
             "`ω₀ = 2` and `ω = 3/2` it is `4π`, rounded to `12.5664` with `≈`."),
            ("Read the envelope",
             "The swing reaches `2·|A|` at the top of each beat, with `A` from the "
             "previous lesson. For `ω = 3/2` that is `24/7`."),
        ],
        "worked": {
            "title": "x″ + 4x = 3cos(2t), and then the push at ω = 3/2",
            "intro": [
                "The lab presets for `ω = 2` and `ω = 3/2`: `m = 1`, `k = 4`, `F₀ = 3`, "
                "started at rest at the rest position.",
            ],
            "lines": [
                "ω₀² = 4, ω² = 4:  equal, so resonance",
                "B = F₀/(2m·ω₀) = 3/(2·1·2) = 3/4",
                "x_p = (3/4)·t·sin(2t)",
                "x_p″ = 3·cos(2t) − 3·t·sin(2t)",
                "x_p″ + 4·x_p = 3·cos(2t):  residual 0",
                "ω = 3/2:  beat period 2π/(2 − 3/2) = 4π",
            ],
            "after": [
                "At resonance the amplitude `3t/4` has no bound and no jump: it is `3` at "
                "`t = 4`. Beside it, with `ω = 3/2`, the swing is bounded by `24/7` and "
                "repeats every `4π`, about `12.5664` and rounded. The first is the limit of "
                "the second as the push is tuned onto the spring.",
            ],
        },
        "quiz_title": "Resonance, growth and beats",
        "quiz": [
            {"q": "For `m = 1`, `k = 9` and a push `6·cos(3t)`, what is the coefficient `B` in the resonant solution `B·t·sin(3t)`?",
             "a": ["`1`", "`2`", "`6`", "`1/3`"],
             "c": 0,
             "why": "`B = F₀/(2m·ω₀) = 6/(2·1·3) = 1`. `2` is `F₀/ω₀`, missing the factor "
                    "`2m`. `6` is `F₀` alone. `1/3` divides by `F₀` instead of by "
                    "`2m·ω₀`."},
            {"q": "At exact resonance with no damper, how does the amplitude of the response behave?",
             "a": ["It is infinite as soon as the push starts",
                   "It grows in proportion to the time, with no bound",
                   "It settles at `F₀/k`",
                   "It swells and shrinks with a fixed beat period"],
             "c": 1,
             "why": "The amplitude is `F₀·t/(2m·ω₀)`, a straight line in `t`: finite at "
                    "each moment and without bound. It is not infinite at once. `F₀/k` is "
                    "the response to a push of frequency near zero. And swelling and "
                    "shrinking is the behaviour beside resonance, not on it."},
            {"q": "A spring with `ω₀ = 4` is pushed at `ω = 7/2`. What is the beat period?",
             "a": ["`4π/15`", "`π`", "`8π`", "`4π`"],
             "c": 3,
             "why": "`2π/|ω₀ − ω| = 2π/(1/2) = 4π`. `4π/15` uses the sum `15/2` in "
                    "place of the difference. `π` is `2π/2`, which would need a "
                    "difference of `2`, and `8π` is the period of the sine factor alone, "
                    "`2π/((ω₀ − ω)/2)`, whose absolute value repeats twice as often."},
            {"q": "The push frequency is moved closer and closer to `ω₀`, but never reaches it. What happens to the beats?",
             "a": ["The beat period shrinks and the swing gets smaller",
                   "The beat period lengthens and the swing stays the same",
                   "Both the beat period and the largest swing grow without bound",
                   "The beats disappear when the frequencies are close"],
             "c": 2,
             "why": "The beat period is `2π/|ω₀ − ω|`, which grows as the difference "
                    "shrinks, and the largest swing is `2|A|` with `|A| = F₀/(m·|ω₀² − ω²|)`, "
                    "which grows as well. Beats do not vanish near resonance; they are "
                    "slowest and tallest there."},
        ],
        "mistakes": [
            ("Believing resonance means the amplitude becomes infinite at once",
             "The amplitude at resonance is `F₀·t/(2m·ω₀)`, which is `3t/4` for the lab's "
             "preset at `ω = 2`. It is `3` at `t = 4` and `30` at `t = 40`: it climbs "
             "steadily and has no ceiling, but at every moment it is a finite number. "
             "&ldquo;Infinite&rdquo; is what the formula of the previous lesson says "
             "when it is applied where it does not hold."),
            ("Taking the period of the slow sine as the beat period",
             "The envelope factor `sin((ω₀ − ω)t/2)` has period `4π/|ω₀ − ω|`, which is "
             "`8π` for `ω = 3/2`. But the swing is the absolute value of it, and a "
             "swell is followed by the next swell after `2π/|ω₀ − ω|`, which is `4π`. That is "
             "the beat period, and the lab's period tile prints `4π ≈ 12.5664`."),
            ("Trying a bigger cosine and sine at resonance",
             "A guess `A·cos(ω₀t) + B·sin(ω₀t)` makes the left side exactly zero for "
             "every `A` and `B`, since both terms solve the free equation, and no "
             "choice can produce `F₀·cos(ω₀t)`. The factor `t` is not decoration: "
             "it is what produces the term `2B·ω₀·cos(ω₀t)` in the second derivative."),
        ],
        "standard": (
            "Finish when you can solve the push at the natural frequency and find the beat period beside it.",
            "You should be able to show that A·cos(ωt) fails when ω = ω₀, write "
            "x_p = (F₀/(2m·ω₀))·t·sin(ω₀t) and check it by substitution, say that its "
            "amplitude grows linearly and is finite at every moment, and compute the "
            "beat period 2π/|ω₀ − ω| as a symbol and as a rounded number marked ≈."),
        "note": 'Every damper removes the divergence. What it does to the peak, and where it moves the peak, is the subject of &ldquo;Damped Forcing and the Amplitude Curve&rdquo;.',
    },

    # ---------------------------------------------------------------- 09
    {
        "slug": "damped-forcing-and-the-amplitude-curve",
        "title": "Damped Forcing and the Amplitude Curve",
        "module": "Forcing",
        "one_line": "Compute the steady amplitude squared A² = F₀²/((k − m·ω²)² + (c·ω)²) exactly, the resonant frequency ω_r² = k/m − c²/(2m²), and the peak amplitude.",
        "summary": (
            "With a damper, the response to a steady push settles to a fixed amplitude "
            "whose square is an exact fraction, so the divergence of the previous lesson "
            "is gone and the peak is finite. The peak is not at the natural frequency: it "
            "sits at `ω_r² = k/m − c²/(2m²)`, below it, and for a heavy enough damper it "
            "does not exist."),
        "key": [
            "A² = F₀²/((k − m·ω²)² + (c·ω)²)",
            "ω_r² = k/m − c²/(2m²)  <  ω₀² = k/m",
            "peak:  A_max² = F₀²/(c²·ω_d²)",
            "no peak when c² ≥ 2mk",
            "ω_d² = k/m − c²/(4m²), as before",
        ],
        "key_label": "A finite peak, below the natural frequency",
        "concepts_intro": (
            "Three ideas: what the response needs once there is a damper, why its "
            "amplitude is finite, and where the peak is."
        ),
        "concepts": [
            ("With a damper the response needs a sine as well as a cosine",
             "The damper's force `−c·x′` turns a cosine into a sine, so the steady "
             "response is `G·cos(ωt) + H·sin(ωt)`. The two coefficients solve two "
             "linear equations, one from the cosines and one from the sines, and the "
             "amplitude of the pair is `√(G² + H²)`."),
            ("The amplitude squared has a denominator that cannot reach zero",
             "The result is `A² = F₀²/D` with `D = (k − m·ω²)² + (c·ω)²`. The first square "
             "can be zero, at `ω = ω₀`, but the second is positive for every `ω > 0` "
             "once `c > 0`. So `D > 0`, `A²` is finite, and the divergence of the "
             "undamped case is gone."),
            ("The peak is at ω_r, and ω_r is not ω₀",
             "The peak is where `D` is least. Written in terms of `u = ω²`, `D` is a "
             "parabola, least at `u = k/m − c²/(2m²)`. The damper subtracts from "
             "`ω₀²` and moves the peak down. If that number is zero or negative, "
             "there is no peak at all."),
        ],
        "read_title": "Where the damped response is largest",
        "read_intro": "The steady response and its amplitude with a derivation, the least value of the denominator, presets on three kinds of curve, and why the peak is not at the natural frequency.",
        "body": [
            ("p", "Put the damper back: `m·x″ + c·x′ + k·x = F₀·cos(ωt)` with `c > 0`. "
                  "Every free solution of this equation dies away, as the damping lessons "
                  "showed, so after a while only the part fixed by the push remains. "
                  "That is the <strong>steady state</strong>, and its size is the "
                  "<strong>steady amplitude</strong>. The way the motion settles to it "
                  "is the damped free solution added on, which this lesson does not "
                  "compute; the lab reports the steady amplitude only."),
            ("math", [
                "x_p = G·cos(ωt) + H·sin(ωt)",
                "x_p′ = −G·ω·sin(ωt) + H·ω·cos(ωt)",
                "x_p″ = −ω²·(G·cos(ωt) + H·sin(ωt))",
            ]),
            ("p", "Substitute into the equation and collect the cosines and the sines "
                  "separately. Write `P = k − m·ω²` and `Q = c·ω`."),
            ("math", [
                "cosines:   P·G + Q·H = F₀",
                "sines:    −Q·G + P·H = 0",
            ]),
            ("thm", ("The steady amplitude squared",
                     "The steady response of `m·x″ + c·x′ + k·x = F₀·cos(ωt)` has "
                     "amplitude `A` with `A² = F₀²/(P² + Q²)`, where `P = k − m·ω²` and "
                     "`Q = c·ω`.")),
            ("proof", ["Multiply the first equation by `P` and the second by `Q`, and "
                       "subtract: `(P² + Q²)·G = F₀·P`. Multiply the first by `Q` and the "
                       "second by `P`, and add: `(P² + Q²)·H = F₀·Q`.",
                       "So `G = F₀·P/(P² + Q²)` and `H = F₀·Q/(P² + Q²)`, and "
                       "`G² + H² = F₀²·(P² + Q²)/(P² + Q²)² = F₀²/(P² + Q²)`. The "
                       "amplitude of `G·cos(ωt) + H·sin(ωt)` is `√(G² + H²)`, as in "
                       "&ldquo;Amplitude, Phase and Period&rdquo;. With `c = 0` it reduces to "
                       "the square of the previous lessons' `A`."]),
            ("example", ("A damped response, c = 2, k = 5, ω = 1",
                         "With `m = 1` and `F₀ = 3`: `P = 5 − 1 = 4`, `Q = 2`, and "
                         "`P² + Q² = 20`. The coefficients are `G = 3·4/20 = 3/5` and "
                         "`H = 3·2/20 = 3/10`, and `A² = 9/25 + 9/100 = 9/20`.",
                         "The lab prints `A² = 9/20`, an exact fraction. It prints the "
                         "square and not `A`, because `A` is a square root and is "
                         "not needed for what comes next.")),
            ("h3", "Where the denominator is least"),
            ("p", "The amplitude is largest where `D = P² + Q²` is smallest. Expand it "
                  "in `u = ω²`: `D = m²·u² + (c² − 2mk)·u + k²`, an upward parabola. "
                  "It is least at `u = (2mk − c²)/(2m²)`, and there its value is "
                  "`c²·ω_d²` with the `ω_d²` of &ldquo;Underdamped Motion and the "
                  "Envelope&rdquo;."),
            ("math", [
                "ω_r² = k/m − c²/(2m²)",
                "D_min = c²·(k/m − c²/(4m²)) = c²·ω_d²",
                "A_max² = F₀²/(c²·ω_d²)",
                "ω_r² < ω_d² < ω₀²",
            ]),
            ("p", "The last line is the point. The frequency of the peak, the frequency "
                  "of the free ringing and the natural frequency are three different "
                  "numbers, in that order. The peak needs `u > 0`, which is "
                  "`c² < 2mk`. When `c² ≥ 2mk` the parabola is increasing for all "
                  "`u > 0`, the amplitude falls steadily from `F₀/k` at `ω = 0`, and the "
                  "lab prints `none`."),
            ("example", ("The preset curve, c = 2",
                         "For `m = 1`, `c = 2`, `k = 5`: `D = u² − 6u + 25 = (u − 3)² + 16`. "
                         "It is least at `u = 3`, so `ω_r² = 3`, with `D = 16` and "
                         "`A_max² = 9/16`, `A_max = 3/4`. The natural frequency squared "
                         "is `5`, so the peak is lower than `ω₀`.",
                         "At `ω₀² = 5` itself, `D = 0 + 4·5 = 20` and `A² = 9/20`, "
                         "which is below `9/16`. The natural frequency does not give the "
                         "largest response.")),
            ("example", ("Typing ω near the peak",
                         "`ω_r = √3` is irrational, and the lab takes a rational `ω`, so "
                         "a convenient one to try is `ω = 7/4`, a little above `√3`. Then "
                         "`P = 5 − 49/16 = 31/16` and `Q = 7/2`, and "
                         "`A² = 2304/4097`. That is just under `9/16`: "
                         "`2304·16 = 36864` while `9·4097 = 36873`.",
                         "A rational push can come as near to the peak as you like and "
                         "never reach it. The exact tile tells you how near you are.")),
            ("example", ("No peak at all",
                         "For `m = 1`, `c = 4`, `k = 4`, `ω_r² = 4 − 8 = −4`, and the lab "
                         "prints `none`. Here `D = (ω² + 4)²`, so `A = F₀/(ω² + 4)` "
                         "falls steadily. The lab preset with `c = 3` lies between: it "
                         "is still underdamped, since `9 < 16`, but `c² = 9` is above "
                         "`2mk = 8`, and it has no peak either.",
                         "Free ringing and a resonant peak are different properties. A "
                         "damper can be light enough to ring and heavy enough to remove "
                         "the peak.")),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "amplitude",
            "preset": "curve",
            "presets": [
                {"id": "curve", "label": "c = 2, k = 5, ω = 1",
                 "m": 1, "c": 2, "k": 5, "ic": [0, 0], "F0": 3, "w": 1,
                 "expect": {"osForced": "A² = 9/20", "osResonant": "ω_r² = 3; A_max = 3/4"}},
                {"id": "at-peak", "label": "c = 2, k = 5, ω = 7/4",
                 "m": 1, "c": 2, "k": 5, "ic": [0, 0], "F0": 3, "w": "7/4",
                 "expect": {"osForced": "A² = 2304/4097", "osResonant": "ω_r² = 3; A_max = 3/4"}},
                {"id": "light", "label": "c = 1/2, k = 4, ω = 2",
                 "m": 1, "c": "1/2", "k": 4, "ic": [0, 0], "F0": 3, "w": 2,
                 "expect": {"osForced": "A² = 9", "osResonant": "ω_r² = 31/8; A_max = 8√7/7 ≈ 3.02372"}},
                {"id": "gap", "label": "c = 3, k = 4, ω = 1",
                 "m": 1, "c": 3, "k": 4, "ic": [0, 0], "F0": 3, "w": 1,
                 "expect": {"osType": "underdamped", "osForced": "A² = 1/2", "osResonant": "none"}},
                {"id": "no-peak", "label": "c = 4, k = 4, ω = 1",
                 "m": 1, "c": 4, "k": 4, "ic": [0, 0], "F0": 3, "w": 1,
                 "expect": {"osForced": "A² = 9/25", "osResonant": "none"}},
            ],
            "panel_title": "Find the peak of the amplitude curve",
            "panel_intro": (
                "The curve shows the steady amplitude against the pushing frequency, with the "
                "chosen frequency and the resonant frequency marked. Read the forced-response "
                "tile and the resonant tile for each preset, then move ω in the box and watch "
                "the amplitude squared approach its peak. The curve is drawn by stepping in "
                "floating point; the squared amplitude and the resonant frequency squared are "
                "exact, and a figure behind ≈ is rounded."),
        }),
        "steps_title": "From a damped oscillator to its amplitude curve",
        "steps_intro": "Five moves. The third decides whether there is a peak to find.",
        "steps": [
            ("Compute P and Q",
             "`P = k − m·ω²` and `Q = c·ω`, as fractions. For `m = 1`, `c = 2`, `k = 5` at "
             "`ω = 1`: `P = 4` and `Q = 2`."),
            ("Compute the amplitude squared",
             "`A² = F₀²/(P² + Q²)`. Square first, then add, then divide: "
             "`9/(16 + 4) = 9/20`. Adding before squaring is the usual slip."),
            ("Compute ω_r² and test it",
             "`ω_r² = k/m − c²/(2m²)`. If it is zero or negative the curve has no peak, "
             "and the lab prints `none`. Here `5 − 2 = 3`."),
            ("Compute the peak",
             "`A_max² = F₀²/(c²·ω_d²)` with `ω_d² = k/m − c²/(4m²)`. Here "
             "`ω_d² = 4`, so `A_max² = 9/16` and `A_max = 3/4`."),
            ("Compare with the natural frequency",
             "At `ω₀` the amplitude squared is `F₀²/(c²·ω₀²)`, here `9/20`. It must be "
             "below the peak, and `ω_r²` must be below `ω₀²`."),
        ],
        "worked": {
            "title": "m = 1, c = 2, k = 5, F₀ = 3",
            "intro": [
                "The lab preset with `c = 2`, `k = 5` and `ω = 1`, read as a function of the frequency squared.",
            ],
            "lines": [
                "A² = 9/((5 − ω²)² + 4ω²)",
                "u = ω²:  D = u² − 6u + 25 = (u − 3)² + 16",
                "least at u = 3:  ω_r² = 3,  D = 16",
                "A_max² = 9/16          A_max = 3/4",
                "at ω₀² = 5:  D = 0 + 20,  A² = 9/20 < 9/16",
                "ω_r² = 3  <  ω_d² = 4  <  ω₀² = 5",
            ],
            "after": [
                "The peak is lower in frequency than the natural frequency and "
                "higher in amplitude than the response at it. The lab prints "
                "`ω_r² = 3; A_max = 3/4` in the resonant tile. Because `ω_r = √3` is "
                "not rational, the lab preset uses `ω = 7/4` and the tile shows an "
                "amplitude squared a hair below `9/16`.",
            ],
        },
        "quiz_title": "Amplitude, peak and no peak",
        "quiz": [
            {"q": "For `m = 1`, `c = 2`, `k = 5`, `F₀ = 3` and `ω = 2`, what is `A²`?",
             "a": ["`9/17`", "`9/25`", "`9/5`", "`9`"],
             "c": 0,
             "why": "`P = 5 − 4 = 1` and `Q = 2·2 = 4`, so `A² = 9/(1 + 16) = 9/17`. `9/25` "
                    "adds before squaring, `(1 + 4)²`. `9/5` uses `c²` where `(c·ω)²` "
                    "belongs. `9` drops the damper entirely."},
            {"q": "For `m = 2`, `c = 2`, `k = 5`, what is `ω_r²`?",
             "a": ["`5/2`", "`9/4`", "`3`", "`2`"],
             "c": 3,
             "why": "`ω_r² = k/m − c²/(2m²) = 5/2 − 4/8 = 2`. `5/2` is `ω₀²`, which "
                    "ignores the damper. `9/4` is `ω_d² = 5/2 − 1/4`, the ringing "
                    "frequency, which has `4m²` in place of `2m²`. `3` is the answer for "
                    "the unit mass."},
            {"q": "With `m = 1` and `k = 4`, which damping constant gives an amplitude curve with a peak at some `ω > 0`?",
             "a": ["`c = 3`", "`c = 5`", "`c = 2`", "`c = 4`"],
             "c": 2,
             "why": "A peak needs `c² < 2mk = 8`. `c = 2` has `4 < 8`. `c = 3` has `9 > 8` "
                    "and is underdamped, but its curve has no peak, so it is not the "
                    "same thing as ringing. `c = 4` and `c = 5` are further past the "
                    "limit."},
            {"q": "For `m = 1`, `c = 1`, `k = 5/4` and `F₀ = 3`, what is the peak amplitude `A_max`?",
             "a": ["`9`", "`3`", "`3/2`", "`6`"],
             "c": 1,
             "why": "`ω_d² = 5/4 − 1/4 = 1`, so `A_max² = F₀²/(c²·ω_d²) = 9/1 = 9`, and "
                    "`A_max = 3`. `9` is the square left unrooted. `3/2` and `6` come "
                    "from a stray factor of `2` that is not in the formula."},
        ],
        "mistakes": [
            ("Believing the resonant frequency of a damped oscillator is ω₀",
             "On the lab preset with `c = 2` and `k = 5`, `ω₀² = 5` but the peak is at `ω_r² = 3`, and "
             "the amplitude squared at `ω₀` is `9/20`, less than the peak value `9/16`. "
             "Only with no damper do the two coincide, and then the peak is infinite. "
             "The lighter the damper, the nearer: at `c = 1/2`, `k = 4` the peak is at "
             "`31/8` against `ω₀² = 4`. It is never exactly at `ω₀`."),
            ("Expecting a peak whenever the motion rings freely",
             "Free ringing needs `c² < 4mk`; a peak needs `c² < 2mk`, which is "
             "a stricter condition. With `m = 1` and `k = 4`, `c = 3` is underdamped, "
             "with discriminant `−7`, and still the lab's resonant tile reads `none`: "
             "the amplitude falls steadily from `F₀/k` at `ω = 0`. The two "
             "thresholds differ by a factor of `√2`."),
            ("Putting the natural frequency in the height of the peak",
             "The peak height is `F₀/(c·ω_d)`, with the ringing frequency. For "
             "`c = 2`, `k = 5`, `ω_d = 2` gives `3/4`. Using `ω₀ = √5` instead would give "
             "`3/(2√5)`, which is not what the lab prints and is not the maximum "
             "of anything. Adding the squares `P` and `Q` before squaring them, in "
             "`A²`, is the other slip to look out for."),
        ],
        "standard": (
            "Finish when you can compute where a damped oscillator's response is largest and how large it is.",
            "You should be able to compute P = k − m·ω² and Q = c·ω, the steady amplitude "
            "squared F₀²/(P² + Q²) as an exact fraction, the resonant frequency squared "
            "ω_r² = k/m − c²/(2m²), the peak A_max² = F₀²/(c²·ω_d²), and say why there "
            "is no peak when c² ≥ 2mk and why the peak is not at ω₀."),
        "note": 'This is the last lesson of the course. The next course takes up the two-equation form that &ldquo;From Second Order to a System&rdquo; introduced, and reads the motion of this equation and many others as a path in a plane, in Systems and the Phase Plane.',
    },
]
