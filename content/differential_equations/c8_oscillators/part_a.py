"""Oscillators, Damping and Resonance -- the first half.

The mass on a spring, its amplitude and phase, its conserved energy and the
phase-plane ellipse; then the three kinds of damping and the underdamped
envelope.

Every figure below is read off the lab, scripts/mathpath/labs/dekit_b.py (mode
oscillator), by executing its shipped JavaScript under node, and pinned in
`expect`. A figure that is rounded is printed with the approximation sign and
says so; a surd is exact and is printed with its rounded value beside it;
everything else is an exact fraction.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "the-mass-spring-model",
        "title": "The Mass–Spring Model",
        "module": "Free oscillation",
        "one_line": "Turn Newton's law and Hooke's law into m·x″ + c·x′ + k·x = 0, and read the frequency ω₀² = k/m and the period off it.",
        "summary": (
            "A mass on a spring is the model every oscillator in this course is a "
            "version of. Newton's law says mass times acceleration is the total force, "
            "Hooke's law says the spring pulls back in proportion to the stretch, and "
            "the result is `m·x″ = −k·x` when nothing else acts. Its solutions swing at "
            "the natural frequency `ω₀`, where `ω₀² = k/m`, so a stiffer spring swings "
            "faster and a heavier mass slower."
        ),
        "key": [
            "m·x″ = −k·x − c·x′     Newton, Hooke, drag",
            "m·x″ + c·x′ + k·x = 0",
            "ω₀² = k/m    natural frequency",
            "x = C₁cos(ω₀t) + C₂sin(ω₀t)  when c = 0",
            "period  T = 2π/ω₀",
        ],
        "key_label": "One equation for the whole course",
        "concepts_intro": (
            "Three ideas, in the order they are used: where the equation comes from, what "
            "its frequency is, and what the period is made of."
        ),
        "concepts": [
            ("The equation is Newton's law with two forces in it",
             "Let `x` be how far the mass is from where the spring is relaxed, positive to "
             "the right. Newton's law says `m·x″` is the sum of the forces. Hooke's law "
             "gives the spring's force as `−k·x`: proportional to the stretch and "
             "pointing back toward rest, which is what the minus sign records. A damper "
             "gives `−c·x′`, proportional to the speed and opposing it. Moving everything "
             "to the left gives `m·x″ + c·x′ + k·x = 0`."),
            ("ω₀² = k/m is the whole story of free swinging",
             "With no damper, `c = 0`, divide by `m` to get `x″ = −(k/m)·x`. Call "
             "`k/m` the number `ω₀²`. The previous course showed that `x″ = −ω₀²·x` has "
             "the solutions `C₁cos(ω₀t) + C₂sin(ω₀t)`. A bigger `k` makes the pull "
             "stronger and `ω₀` larger; a bigger `m` is harder to accelerate with the same pull, so `ω₀` is smaller."),
            ("The period is 2π over ω₀, and it is rounded",
             "Cosine and sine repeat after `2π` in their argument, so the motion repeats "
             "when `ω₀·t` has grown by `2π`: the period is `T = 2π/ω₀`. When `ω₀` is "
             "rational the period is a rational multiple of `π`; when it is a surd "
             "the period is a rational multiple of `π` over a square root. In either "
             "case it is irrational, and the lab prints it with `≈`."),
        ],
        "read_title": "From two laws to one equation, and from one equation to a period",
        "read_intro": "The forces, the equation they give, the frequency in the undamped case, and a proof that the period does not depend on how far the mass is pulled.",
        "body": [
            ("p", "Hang a mass `m` on a spring and let it move along a line. Call `x` its "
                  "position measured from the spot where the spring is neither stretched "
                  "nor squeezed. Units are left out throughout: any consistent set of "
                  "units will do, and the numbers in the lab are pure."),
            ("def", ("Hooke's law",
                     "The force a spring exerts on the mass is `−k·x`, where `k > 0` is the "
                     "<strong>spring constant</strong>. The force is proportional to the "
                     "displacement and points the other way.",
                     "A stiffer spring has a larger `k`. The law is an approximation that "
                     "real springs satisfy for small stretches, and in this course it is "
                     "an assumption.")),
            ("p", "Newton's law says that mass times acceleration is the total force. "
                  "Acceleration is `x″`, so `m·x″` equals the spring's force plus whatever "
                  "else acts. A damper, such as a plunger in oil, opposes the motion with a "
                  "force proportional to the speed `x′`, which is `−c·x′` for a "
                  "<strong>damping constant</strong> `c ≥ 0`."),
            ("math", [
                "m·x″ = −k·x − c·x′",
                "m·x″ + c·x′ + k·x = 0",
                "c = 0:   x″ = −(k/m)·x = −ω₀²·x",
            ]),
            ("h3", "The undamped case"),
            ("p", "This lesson takes `c = 0`; the damper arrives in the lessons after "
                  "next. With no damper the equation is `x″ + ω₀²·x = 0` where "
                  "`ω₀² = k/m`. That is the equation of &ldquo;Complex Roots and "
                  "Oscillation&rdquo; in the previous course, with `ω₀` in the place of "
                  "`β`, and its general solution is `x = C₁cos(ω₀t) + C₂sin(ω₀t)`. "
                  "Two constants, fixed by a start."),
            ("thm", ("The period does not depend on the start",
                     "Every solution of `x″ + ω₀²·x = 0` satisfies `x(t + T) = x(t)` for "
                     "`T = 2π/ω₀`, whatever the constants `C₁` and `C₂`.")),
            ("proof", ["Replace `t` by `t + T` in `cos(ω₀t)`. The argument becomes "
                       "`ω₀t + ω₀T = ω₀t + 2π`, and cosine and sine repeat after `2π`.",
                       "So both terms, and any combination of them, take the same value "
                       "at `t + T` as at `t`. The constants `C₁` and `C₂` come out as "
                       "multipliers and never enter. This is why a larger start does not "
                       "make a slower swing."]),
            ("example", ("A unit mass on a stiff spring",
                         "Take `m = 1` and `k = 4`. Then `x″ = −4x`, `ω₀² = 4`, "
                         "`ω₀ = 2`, and the solutions are `C₁cos(2t) + C₂sin(2t)`. The "
                         "period is `2π/2 = π`, which is about `3.14159` and is rounded.",
                         "Check by substituting `x = cos(2t)`: `x″ = −4cos(2t) = −4x`. The "
                         "residual is zero, so it is a solution, and the lab's tiles for "
                         "the first preset show `ω₀² = 4` and the period `π`.")),
            ("p", "Now change one number at a time and see which way it moves. Doubling "
                  "the mass, with the same spring, divides `ω₀²` by `2`. The new frequency "
                  "is `ω₀ = √2`, the period is `2π/√2`, and the period has been "
                  "multiplied by `√2`: the heavier mass is <em>slower</em>. Stiffening the "
                  "spring to `k = 9` with `m = 1` gives `ω₀ = 3` and the period `2π/3`, "
                  "shorter than `π`."),
            ("example", ("A frequency that is a surd",
                         "Take `m = 2` and `k = 5`. Then `ω₀² = 5/2`, which has no "
                         "rational square root. The frequency is `ω₀ = √(5/2)`, written "
                         "`√10/2` after clearing the fraction under the root, and the "
                         "period is the irrational number the lab prints with `≈`.",
                         "The lab keeps `ω₀² = 5/2` exact and prints `ω₀` as a surd with "
                         "its rounded value beside it. Only the second is rounded.")),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "unit",
            "presets": [
                {"id": "unit", "label": "m = 1, k = 4",
                 "m": 1, "c": 0, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "undamped", "osOmega0Sq": "4", "osOmega0": "2", "osPeriod": "π ≈ 3.14159"}},
                {"id": "heavy", "label": "m = 2, k = 5",
                 "m": 2, "c": 0, "k": 5, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "undamped", "osOmega0Sq": "5/2", "osOmega0": "√10/2 ≈ 1.58114", "osPeriod": "4π/√10 ≈ 3.97384"}},
                {"id": "stiff", "label": "m = 1, k = 9",
                 "m": 1, "c": 0, "k": 9, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "undamped", "osOmega0Sq": "9", "osOmega0": "3", "osPeriod": "2π/3 ≈ 2.0944"}},
                {"id": "double", "label": "m = 2, k = 4",
                 "m": 2, "c": 0, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "undamped", "osOmega0Sq": "2", "osOmega0": "√2 ≈ 1.41421", "osPeriod": "2π/√2 ≈ 4.44288"}},
            ],
            "panel_title": "Change m or k and watch the frequency",
            "panel_intro": (
                "Pick a preset, then read ω₀² and the period in the tiles. The mass-and-spring "
                "pair m = 1, k = 4 and the pair m = 2, k = 4 differ only in the mass, so compare "
                "their periods first. The drawn curve is made by stepping in floating point and "
                "is a picture; the tiles are the exact figures."),
        }),
        "steps_title": "From a mass and a spring to a frequency and a period",
        "steps_intro": "Four moves, then a check. The check is the one that catches a mass and a spring constant entered the wrong way round.",
        "steps": [
            ("Name the forces and fix the direction",
             "Take positive to the right, so a stretch is `x > 0`. The spring's force is "
             "`−k·x` and a damper's is `−c·x′`. Each force opposes what the mass is "
             "doing, which is why each has a minus sign."),
            ("Write Newton's law and collect",
             "`m·x″` equals the sum of the forces. Move every term to the left to get "
             "`m·x″ + c·x′ + k·x = 0`. For this lesson `c = 0`."),
            ("Divide by m and name ω₀²",
             "`x″ = −(k/m)·x`, and `ω₀² = k/m` is a fraction you compute exactly. Keep "
             "it as a fraction. Take its root only when you need `ω₀`, and keep that as a "
             "surd if the root is not rational."),
            ("Write the period as a symbol, then as a rounded number",
             "`T = 2π/ω₀`. Leave `π` and the root in the symbol, and round only once, at "
             "the end, with `≈`. The lab prints both."),
            ("Check the direction of change",
             "A larger `k` or a smaller `m` must make `ω₀` larger and the period "
             "shorter. If your answer moves the other way, `m` and `k` have been swapped."),
        ],
        "worked": {
            "title": "m = 1, k = 4, and then the mass doubled",
            "intro": [
                "Start with `m = 1` and `k = 4`, the first preset. Then double the mass "
                "and compare.",
            ],
            "lines": [
                "x″ = −4x         ω₀² = k/m = 4",
                "ω₀ = 2           T = 2π/2 = π ≈ 3.14159",
                "x = C₁cos(2t) + C₂sin(2t)",
                "double m:  ω₀² = 4/2 = 2",
                "ω₀ = √2          T = 2π/√2 ≈ 4.44288",
                "T grows by the factor √2",
            ],
            "after": [
                "The first period is exact as `π` and the lab prints it with `≈`. The "
                "second is the lab's `double` preset. Its period is `√2` times larger "
                "because `ω₀` is `√2` times smaller, and no other figure in the lesson "
                "needs rounding.",
            ],
        },
        "quiz_title": "Frequency, period and what moves them",
        "quiz": [
            {"q": "A mass `m = 3` hangs on a spring with `k = 12` and no damper. What is `ω₀²`?",
             "a": ["`36`", "`4`", "`1/4`", "`15`"],
             "c": 1,
             "why": "`ω₀² = k/m = 12/3 = 4`. Multiplying gives `36`, which is `m·k` and "
                    "has nothing to do with the equation. `1/4` swaps the mass and the "
                    "spring constant. `15` adds them, but they appear as a quotient."},
            {"q": "The mass is multiplied by `4` and the spring is unchanged. What happens to the period?",
             "a": ["It is halved", "It is multiplied by `4`", "It is unchanged", "It is doubled"],
             "c": 3,
             "why": "`ω₀² = k/m` is divided by `4`, so `ω₀` is halved and `T = 2π/ω₀` "
                    "is doubled. It is not multiplied by `4`, because the period follows "
                    "the square root of the mass. It is not unchanged, because `m` is in "
                    "`ω₀`, and it is not halved, which is what a mass four times smaller "
                    "would do."},
            {"q": "Why does Hooke's law have a minus sign, `−k·x`?",
             "a": ["The force points opposite to the displacement, back toward rest",
                   "The force always points to the left",
                   "Springs lose energy, so the force is negative",
                   "The sign makes the period come out positive"],
             "c": 0,
             "why": "A stretch (`x > 0`) is answered by a pull the other way and a "
                    "squeeze (`x < 0`) by a push the other way, so force and displacement "
                    "have opposite signs. The force has no fixed direction in space. The "
                    "sign is not about energy loss, which belongs to the damper, and the "
                    "period is positive for its own reasons."},
            {"q": "Which single change gives the shortest period?",
             "a": ["Doubling `m`", "Halving `k`", "Pulling the mass twice as far at the start",
                   "Doubling `k`"],
             "c": 3,
             "why": "`ω₀² = k/m`: doubling `k` doubles `ω₀²` and shortens the period by "
                    "`√2`. Doubling `m` and halving `k` both lengthen it. The size of the "
                    "start enters only the constants `C₁` and `C₂`, never the period, as "
                    "the proof in this lesson shows."},
        ],
        "mistakes": [
            ("Believing a heavier mass oscillates faster because it has more energy",
             "The energy of a mass released from rest at `x₀` is `½·k·x₀²`, the quantity "
             "&ldquo;Energy and the Phase Ellipse&rdquo; defines, and the mass "
             "does not appear in it. What the mass changes is how hard the same pull is "
             "to move: `ω₀² = k/m` falls as `m` rises. The lab shows it: with `k = 4`, "
             "`m = 1` has period `π` and `m = 2` has period `2π/√2`, about `4.44288`. "
             "Heavier is slower."),
            ("Reading ω₀ as the period",
             "`ω₀` is an angular frequency, in radians per unit time, and the period is "
             "`2π/ω₀`. With `m = 1` and `k = 4` the frequency is `ω₀ = 2` but the "
             "period is `π`, not `2`. A reader who takes `2` as the period has the "
             "motion repeating faster than the lab draws it."),
            ("Expecting a bigger swing to take longer",
             "The period `2π/ω₀` has no `x₀` in it. Start the first preset at `x(0) = 1` "
             "or at `x(0) = 5` and the curve is five times as tall with the same period "
             "`π`, because the constants `C₁` and `C₂` multiply the solution and cannot "
             "stretch the time axis. The proof in this lesson is that argument written "
             "out."),
        ],
        "standard": (
            "Finish when you can go from a mass and a spring constant to a frequency and a period.",
            "You should be able to write m·x″ + c·x′ + k·x = 0 from Newton's law and "
            "Hooke's law, compute ω₀² = k/m exactly, give ω₀ as an integer or a surd, "
            "and give the period 2π/ω₀ as a symbol and as a rounded number marked ≈."),
        "note": 'The solution <em>C₁cos(ω₀t) + C₂sin(ω₀t)</em> has two constants, fixed by a start. The next lesson turns the two constants into the two numbers a physicist actually reads off a swing, in &ldquo;Amplitude, Phase and Period&rdquo;.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "amplitude-phase-and-period",
        "title": "Amplitude, Phase and Period",
        "module": "Free oscillation",
        "one_line": "Rewrite C₁cos(ω₀t) + C₂sin(ω₀t) as a single cosine A·cos(ω₀t − φ), and compute A² = x₀² + v₀²/ω₀² exactly.",
        "summary": (
            "The two constants of an undamped swing are fixed by where the mass starts "
            "and how fast it is going. A physicist reads the same motion differently: as "
            "one cosine with a height, the amplitude `A`, and a shift in time, the phase "
            "`φ`. The height squared is an exact fraction, `A² = x₀² + v₀²/ω₀²`, and it "
            "is not the starting displacement unless the mass starts at rest."
        ),
        "key": [
            "x = C₁cos(ω₀t) + C₂sin(ω₀t) = A·cos(ω₀t − φ)",
            "C₁ = x₀      C₂ = v₀/ω₀",
            "A² = C₁² + C₂² = x₀² + v₀²/ω₀²",
            "tan(φ) = C₂/C₁      φ is rounded",
            "A is not x₀ unless v₀ = 0",
        ],
        "key_label": "Two constants become a height and a shift",
        "concepts_intro": (
            "Three ideas, one per symbol: what the constants are in terms of the start, "
            "what the amplitude is in terms of the constants, and what the phase "
            "records."
        ),
        "concepts": [
            ("The constants are the start, with one divided by ω₀",
             "Put `t = 0` in `x = C₁cos(ω₀t) + C₂sin(ω₀t)` and `x(0) = C₁`, so `C₁ = x₀`. "
             "The velocity is `x′ = −ω₀C₁sin(ω₀t) + ω₀C₂cos(ω₀t)`, so `x′(0) = ω₀·C₂` and "
             "`C₂ = v₀/ω₀`. The division by `ω₀` is easy to forget and it is the "
             "reason the answer to the amplitude question is not `x₀² + v₀²`."),
            ("The amplitude squared is a sum of two squares",
             "Write `C₁ = A·cos(φ)` and `C₂ = A·sin(φ)`. Squaring and adding, and using "
             "`cos(φ)² + sin(φ)² = 1`, gives `C₁² + C₂² = A²`. So `A² = x₀² + v₀²/ω₀²`, "
             "an exact fraction when the start and `ω₀²` are fractions. The amplitude "
             "`A` is a square root of it and is a surd or an integer."),
            ("The phase is an angle and is rounded",
             "Dividing the two equations gives `tan(φ) = C₂/C₁`, and the quadrant of "
             "`φ` is the quadrant of the point `(C₁, C₂)`. The angle is rarely a "
             "rational multiple of `π`, so the lab prints it with `≈`. It says when "
             "the cosine peaks: at `t = φ/ω₀`, so the motion lags a pure "
             "`cos(ω₀t)` by that amount of time."),
        ],
        "read_title": "From two constants to a height and a shift",
        "read_intro": "The identity behind the conversion, the exact formula for the height, three starts that show the different cases, and the one start where the height is the starting displacement.",
        "body": [
            ("p", "The previous lesson ended with `x = C₁cos(ω₀t) + C₂sin(ω₀t)`. Nothing is "
                  "wrong with it, but it hides the two things you would want to know about "
                  "the swing: how far the mass gets from rest, and when it gets there. "
                  "A single cosine shows both."),
            ("def", ("Amplitude and phase",
                     "A motion `x = A·cos(ω₀t − φ)` with `A ≥ 0` has <strong>amplitude</strong> "
                     "`A`, the largest value of `x`, and <strong>phase</strong> `φ`, the "
                     "angle that shifts the cosine to the right by `φ/ω₀` units of time.",
                     "Its period is still `2π/ω₀`: neither `A` nor `φ` enters it.")),
            ("p", "The two forms are the same function, by the subtraction identity of "
                  "trigonometry, `cos(θ − φ) = cos(θ)·cos(φ) + sin(θ)·sin(φ)`, which this "
                  "path takes as given and does not derive, as it takes the rates of sine "
                  "and cosine. Applied to `θ = ω₀t`:"),
            ("math", [
                "A·cos(ω₀t − φ) = (A·cos(φ))·cos(ω₀t) + (A·sin(φ))·sin(ω₀t)",
                "so   C₁ = A·cos(φ)      C₂ = A·sin(φ)",
            ]),
            ("thm", ("The amplitude squared of a free swing",
                     "If `x″ + ω₀²·x = 0` with `x(0) = x₀` and `x′(0) = v₀`, then the "
                     "swing is `A·cos(ω₀t − φ)` with `A² = x₀² + v₀²/ω₀²`.")),
            ("proof", ["The constants are `C₁ = x₀` and `C₂ = v₀/ω₀`, from putting `t = 0` "
                       "into the solution and its derivative.",
                       "Squaring `C₁ = A·cos(φ)` and `C₂ = A·sin(φ)` and adding gives "
                       "`C₁² + C₂² = A²·(cos(φ)² + sin(φ)²) = A²`. So "
                       "`A² = x₀² + (v₀/ω₀)² = x₀² + v₀²/ω₀²`."]),
            ("h3", "Three starts on one spring"),
            ("p", "Take `m = 1` and `k = 4`, so `ω₀ = 2` and `ω₀² = 4`. The same spring, "
                  "started three ways, has three amplitudes and one period."),
            ("math", [
                "start (3, 8):   C₁ = 3   C₂ = 8/2 = 4   A² = 9 + 16 = 25",
                "start (2, 0):   C₁ = 2   C₂ = 0       A² = 4",
                "start (1, 1):   C₁ = 1   C₂ = 1/2     A² = 1 + 1/4 = 5/4",
            ]),
            ("example", ("A start with a velocity",
                         "For `x(0) = 3` and `x′(0) = 8`: `A² = 25` and `A = 5`. The "
                         "tangent of the phase is `C₂/C₁ = 4/3`, so `φ` is the angle in "
                         "the first quadrant with that tangent, about `0.927295`, and "
                         "rounded. The mass starts at `3` and reaches `5`.",
                         "The amplitude `5` is larger than the starting displacement "
                         "`3` because the mass is already moving outward when it is "
                         "released.")),
            ("example", ("A surd amplitude",
                         "For `x(0) = 1` and `x′(0) = 1`: `A² = 5/4` is exact. Its root "
                         "`A = √5/2` is exact too, and the lab prints it with its "
                         "rounded value, about `1.11803`, beside it. The phase has "
                         "`tan(φ) = 1/2`.",
                         "The exact quantity to carry is `A²`. The root and the angle are "
                         "the two things in this lesson that need `≈`.")),
            ("p", "The start `(2, 0)` is the only one of the three where the amplitude "
                  "equals the starting displacement, and the reason is `v₀ = 0`: a mass "
                  "released from rest is at its largest displacement at the moment of "
                  "release, so `A = |x₀|` and `φ = 0` when `x₀ > 0`. Whenever the mass "
                  "has a velocity at `t = 0` it travels further than where it began."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "five",
            "presets": [
                {"id": "five", "label": "start (3, 8), k = 4",
                 "m": 1, "c": 0, "k": 4, "ic": [3, 8], "F0": 0,
                 "expect": {"osAmpSq": "25", "osAmp": "5", "osPhase": "≈ 0.927295"}},
                {"id": "pure-cos", "label": "start (2, 0), k = 4",
                 "m": 1, "c": 0, "k": 4, "ic": [2, 0], "F0": 0,
                 "expect": {"osAmpSq": "4", "osAmp": "2", "osPhase": "0"}},
                {"id": "surd", "label": "start (1, 1), k = 4",
                 "m": 1, "c": 0, "k": 4, "ic": [1, 1], "F0": 0,
                 "expect": {"osAmpSq": "5/4", "osAmp": "√5/2 ≈ 1.11803", "osPhase": "≈ 0.463648"}},
            ],
            "panel_title": "Start the same spring three ways",
            "panel_intro": (
                "The mass and the spring are fixed; only the start changes. Read A² and A in the "
                "tiles and compare each with the starting displacement. The period tile does not "
                "move, and neither does the shape of the curve, which is a cosine every time."),
        }),
        "steps_title": "From a start to an amplitude and a phase",
        "steps_intro": "Five moves. The third is where the division by ω₀ is made.",
        "steps": [
            ("Compute ω₀² and ω₀",
             "`ω₀² = k/m`. Keep the fraction; take the root only if you need it for "
             "`C₂`. For `m = 1` and `k = 4` it is `ω₀ = 2`."),
            ("Read the start",
             "The two numbers are `x₀ = x(0)` and `v₀ = x′(0)`, the displacement and the "
             "velocity, in that order. A start such as `(3, 8)` means displacement `3` and "
             "velocity `8`."),
            ("Find the constants",
             "`C₁ = x₀` and `C₂ = v₀/ω₀`. This is the step that divides the velocity "
             "by the frequency. For `(3, 8)` with `ω₀ = 2` the constants are `3` and `4`."),
            ("Add the squares",
             "`A² = C₁² + C₂²`, exactly. For `(3, 8)` it is `9 + 16 = 25`. Only now take "
             "a root for `A`, as an integer, a surd, or a rounded number marked `≈`."),
            ("Find the phase if it is asked for",
             "`tan(φ) = C₂/C₁`, in the quadrant of `(C₁, C₂)`. Its value is rounded. If "
             "`C₂ = 0` and `C₁ > 0` the phase is `0` exactly."),
        ],
        "worked": {
            "title": "x″ + 4x = 0 started at 3 with velocity 8",
            "intro": [
                "The first preset: `m = 1`, `k = 4`, `x(0) = 3`, `x′(0) = 8`.",
            ],
            "lines": [
                "ω₀² = 4        ω₀ = 2",
                "C₁ = x₀ = 3",
                "C₂ = v₀/ω₀ = 8/2 = 4",
                "A² = 9 + 16 = 25      A = 5",
                "tan(φ) = C₂/C₁ = 4/3    φ ≈ 0.927295",
                "x = 5·cos(2t − φ)     period π",
            ],
            "after": [
                "Check the amplitude from the original form: `3cos(2t) + 4sin(2t)` is "
                "largest when `cos(2t) = 3/5` and `sin(2t) = 4/5`, and then it is "
                "`9/5 + 16/5 = 5`. The check uses only fractions, as it should, because "
                "`A²` is an exact fraction; only the angle is rounded.",
            ],
        },
        "quiz_title": "Amplitude, phase and what they depend on",
        "quiz": [
            {"q": "For `x″ + 9x = 0` with `x(0) = 0` and `x′(0) = 6`, what is the amplitude `A`?",
             "a": ["`0`, the starting displacement", "`6`, the starting velocity",
                   "`2`", "`3`, the frequency"],
             "c": 2,
             "why": "`ω₀ = 3`, so `C₁ = 0` and `C₂ = 6/3 = 2`, and `A² = 0 + 4 = 4`. The "
                    "amplitude is `2`. It is not the starting displacement, because the "
                    "mass moves out from there, and it is not the velocity, which must "
                    "be divided by `ω₀` first. The frequency `3` is a separate quantity."},
            {"q": "For `x″ + 4x = 0` with `x(0) = 3` and `x′(0) = 8`, what is `A²`?",
             "a": ["`11`", "`73`", "`25`", "`17`"],
             "c": 2,
             "why": "`C₁ = 3` and `C₂ = 8/2 = 4`, so `A² = 9 + 16 = 25`. `73` is "
                    "`3² + 8²`, which forgets to divide the velocity by `ω₀`. `11` is "
                    "`3 + 8`, with nothing squared, and `17` is `9 + 8`, with only the "
                    "displacement squared; neither is a sum of two squares of the constants."},
            {"q": "Doubling the starting velocity `v₀` of a free swing, with `x₀` and the spring unchanged, changes which of these?",
             "a": ["The amplitude, but not the period", "The period, but not the amplitude",
                   "Both the amplitude and the period", "Neither"],
             "c": 0,
             "why": "`A² = x₀² + v₀²/ω₀²` contains `v₀`, so the amplitude changes (unless "
                    "`v₀ = 0`, when doubling it changes nothing). The period `2π/ω₀` contains neither `x₀` nor `v₀`, "
                    "so it is untouched. This is the same fact as in the previous "
                    "lesson, seen from the amplitude."},
            {"q": "A mass is released from rest at `x(0) = 2` on the spring `m = 1`, `k = 4`. What does the lab print for the phase `φ`?",
             "a": ["`π/2`", "`0`", "`≈ 0.927295`", "`2`"],
             "c": 1,
             "why": "With `v₀ = 0` the sine term is absent, `C₂ = 0`, and "
                    "`x = 2·cos(2t)` is already a cosine with no shift: `φ = 0`. `π/2` "
                    "would turn the cosine into a sine, `≈ 0.927295` belongs to the "
                    "start `(3, 8)`, and `2` is the amplitude, not an angle."},
        ],
        "mistakes": [
            ("Taking the amplitude to be the initial displacement",
             "On the first preset the mass starts at `x(0) = 3` and the lab prints "
             "`A² = 25`, so it reaches `5`. The amplitude is the largest displacement "
             "over the whole swing, and a mass that is moving when released overshoots "
             "its starting point. The two agree only when `v₀ = 0`, as in the second "
             "preset, where `A = x₀ = 2`."),
            ("Adding the squares of x₀ and v₀ without dividing by ω₀",
             "`3² + 8² = 73` is not `25`. The velocity has units of displacement per "
             "unit time and cannot be added to a displacement until it is divided by "
             "the frequency; `v₀/ω₀` has the units of displacement. On the spring with "
             "`ω₀ = 2` the correct quantity is `8/2 = 4`."),
            ("Thinking a larger amplitude means a longer period",
             "Across the three presets, `A²` is `25`, `4` and `5/4`, and the period tile "
             "reads the same every time. The period is `2π/ω₀` and is a property of the "
             "mass and the spring alone. Amplitude and phase are properties of the "
             "start."),
        ],
        "standard": (
            "Finish when you can turn a start into an amplitude and a phase for a free swing.",
            "You should be able to compute C₁ = x₀ and C₂ = v₀/ω₀, compute A² = C₁² + C₂² "
            "exactly, give A as an integer, a surd or a rounded number marked ≈, read the "
            "phase from tan(φ) = C₂/C₁ as a rounded number, and say why the period does "
            "not change with the start."),
        "note": 'The amplitude was computed from the start, but there is a second way to find it that needs no constants at all: the quantity that the swing keeps fixed. That is the subject of &ldquo;Energy and the Phase Ellipse&rdquo;.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "energy-and-the-phase-ellipse",
        "title": "Energy and the Phase Ellipse",
        "module": "Free oscillation",
        "one_line": "Compute E₀ = ½m·v₀² + ½k·x₀², show it does not change along the motion, and read the ellipse it draws in the plane of position against velocity.",
        "summary": (
            "An undamped swing trades energy between the moving mass and the stretched "
            "spring and never loses any. The total, `½m·v² + ½k·x²`, is the same at "
            "every instant and equals its starting value `E₀`. Plotted as a path in the "
            "plane of position against velocity, that conservation is an ellipse with "
            "semi-axes `A` and `A·ω₀`, traced once per period."
        ),
        "key": [
            "E = ½m·v² + ½k·x²       v = x′",
            "E′ = v·(m·x″ + k·x) = 0   when c = 0",
            "E₀ = ½m·v₀² + ½k·x₀²",
            "x²/A² + v²/(A·ω₀)² = 1   an ellipse",
            "A² = 2E₀/k     the lab's A² and E₀ agree",
        ],
        "key_label": "A quantity the swing keeps",
        "concepts_intro": (
            "Three ideas: the two kinds of energy, the proof that their sum is fixed, "
            "and the picture the proof draws."
        ),
        "concepts": [
            ("Two energies that trade",
             "The moving mass carries kinetic energy `½m·v²` where `v = x′`; the stretched "
             "spring stores potential energy `½k·x²`. At the ends of the swing the mass is "
             "momentarily still, `v = 0`, and the energy is all in the spring. Passing "
             "through the rest position, `x = 0`, the spring is relaxed and the energy "
             "is all in the motion. In between it is shared."),
            ("Their sum is constant when there is no damper",
             "Differentiate `E = ½m·v² + ½k·x²` with the chain rule, using `x′ = v` and "
             "`v′ = x″`. The rate of change is `E′ = m·v·x″ + k·x·v = v·(m·x″ + k·x)`, "
             "and the bracket is zero by the equation. So `E` has the value `E₀` it "
             "had at the start, for ever."),
            ("The ellipse is the same fact as a picture",
             "Plot each instant as the point `(x, v)`. Because `E` is fixed, the points "
             "satisfy `½m·v² + ½k·x² = E₀`, which is an ellipse centred on the origin, "
             "and the mass travels round it once in each period. The plane of `x` "
             "against `v` is the <em>phase plane</em>; &ldquo;From Second Order to a "
             "System&rdquo; in the previous course first drew it, and the next course "
             "returns to it in earnest."),
        ],
        "read_title": "A conserved quantity, proved and drawn",
        "read_intro": "The energy, the proof that it is fixed, the ellipse it gives, and two starts that show where the energy sits at the ends and the middle of a swing.",
        "body": [
            ("def", ("Energy of the oscillator",
                     "For the mass on a spring with position `x` and velocity `v = x′`, "
                     "the <strong>energy</strong> is `E = ½m·v² + ½k·x²`: kinetic energy "
                     "plus the energy stored in the spring.",
                     "Its starting value is `E₀ = ½m·v₀² + ½k·x₀²`, an exact fraction when "
                     "the mass, the spring constant and the start are fractions.")),
            ("p", "The factor `½` appears in both terms and it is the first thing to check "
                  "in any answer. Without it the two terms are still in the right ratio, "
                  "but the number is twice the true energy."),
            ("thm", ("Energy is conserved without damping",
                     "If `m·x″ + k·x = 0`, then `E = ½m·v² + ½k·x²` is constant along "
                     "every solution: `E(t) = E₀` for all `t`.")),
            ("proof", ["With `v = x′`, the derivative of `½m·v²` is `m·v·v′ = m·v·x″` by the "
                       "chain rule, and the derivative of `½k·x²` is `k·x·x′ = k·x·v`.",
                       "So `E′ = v·(m·x″ + k·x)`. By the equation the bracket is `0`, "
                       "so `E′ = 0` and `E` does not change. With a damper the bracket "
                       "is `−c·x′` and `E′ = −c·v²`, which is never positive: the "
                       "energy only falls, and it is the subject of the next module."]),
            ("h3", "The ellipse"),
            ("p", "Divide `½m·v² + ½k·x² = E₀` by `E₀`. The result is "
                  "`x²/(2E₀/k) + v²/(2E₀/m) = 1`. The first denominator is exactly "
                  "`A²`, because `A² = 2E₀/k`, and the second is `A²·k/m = (A·ω₀)²`. So the "
                  "path is"),
            ("math", [
                "x²/A² + v²/(A·ω₀)² = 1",
                "semi-axis in x:  A       semi-axis in v:  A·ω₀",
            ]),
            ("p", "The mass goes round it clockwise: where `v > 0`, at the top, `x` is "
                  "increasing, so the point moves to the right. The shape of the ellipse "
                  "is set by `ω₀` alone, and its size by the start."),
            ("example", ("The first start",
                         "With `m = 1`, `k = 4`, start `(3, 8)`: `E₀ = ½·64 + ½·4·9 = "
                         "32 + 18 = 50`. The semi-axes are `A = 5` and `A·ω₀ = 10`.",
                         "Check the ends: at `x = 5` and `v = 0` the energy is "
                         "`½·4·25 = 50`, and at `x = 0` and `v = 10` it is `½·100 = 50`. "
                         "Both are `E₀`, so both points are on the ellipse.")),
            ("example", ("A heavier mass, released from rest",
                         "With `m = 2`, `k = 5`, start `(1, 0)`: `E₀ = ½·2·0 + ½·5·1 = 5/2`. "
                         "The amplitude squared is `A² = 2E₀/k = 1`, which is `x₀²` as "
                         "it should be for a release from rest. The ellipse is "
                         "tall and thin or short and wide according to `ω₀`.",
                         "The mass does not appear in `E₀` for a start at rest. It "
                         "appears only in how fast the energy is exchanged.")),
            ("p", "Everything the previous lesson computed about a swing can now be read "
                  "off the ellipse. The amplitude is where it crosses the position axis, "
                  "the peak speed is where it crosses the velocity axis, and "
                  "the area it encloses, `π·A·(A·ω₀) = 2π·E₀/√(mk)`, is fixed by the "
                  "energy, the mass and the spring."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "phase",
            "preset": "five",
            "presets": [
                {"id": "five", "label": "m = 1, k = 4, start (3, 8)",
                 "m": 1, "c": 0, "k": 4, "ic": [3, 8], "F0": 0,
                 "expect": {"osEnergy": "50", "osAmpSq": "25"}},
                {"id": "pure-cos", "label": "m = 1, k = 4, start (2, 0)",
                 "m": 1, "c": 0, "k": 4, "ic": [2, 0], "F0": 0,
                 "expect": {"osEnergy": "8", "osAmpSq": "4"}},
                {"id": "heavy", "label": "m = 2, k = 5, start (1, 0)",
                 "m": 2, "c": 0, "k": 5, "ic": [1, 0], "F0": 0,
                 "expect": {"osEnergy": "5/2", "osAmpSq": "1"}},
            ],
            "panel_title": "Watch the point go round the ellipse",
            "panel_intro": (
                "The view is set to the phase plane: position across, velocity up. Read E₀ and "
                "A² in the tiles, then compute the semi-axes A and A·ω₀ yourself and compare them "
                "with where the drawn curve crosses the axes. The curve is drawn by stepping in "
                "floating point; the tiles are exact."),
        }),
        "steps_title": "From a start to its energy and its ellipse",
        "steps_intro": "Four moves. Check the factor of one half at the first of them.",
        "steps": [
            ("Compute the energy at the start",
             "`E₀ = ½m·v₀² + ½k·x₀²`. Square first, then multiply, then halve. For "
             "`m = 1`, `k = 4`, start `(3, 8)` it is `32 + 18 = 50`."),
            ("Find the amplitude squared from the energy",
             "`A² = 2E₀/k`. It must agree with `x₀² + v₀²/ω₀²` from the previous lesson; "
             "for `E₀ = 50` and `k = 4` it is `25`."),
            ("Write the semi-axes",
             "`A` along the position axis and `A·ω₀` along the velocity axis. Here "
             "`5` and `10`, so the ellipse is twice as tall as it is wide."),
            ("Check two points",
             "At the position axis (`v = 0`, `x = A`) and the velocity axis "
             "(`x = 0`, `v = A·ω₀`) recompute the energy. Both must equal `E₀`."),
        ],
        "worked": {
            "title": "The ellipse of the first preset",
            "intro": [
                "The first preset: `m = 1`, `k = 4`, `x(0) = 3`, `x′(0) = 8`.",
            ],
            "lines": [
                "E₀ = ½·1·8² + ½·4·3² = 32 + 18 = 50",
                "A² = 2·50/4 = 25          A = 5",
                "ω₀ = 2         A·ω₀ = 10",
                "ellipse:  x²/25 + v²/100 = 1",
                "x = 5, v = 0:  ½·4·25 = 50",
                "x = 0, v = 10: ½·1·100 = 50",
            ],
            "after": [
                "Both ends check. The starting point `(3, 8)` is on the ellipse too: "
                "`9/25 + 64/100 = 36/100 + 64/100 = 1`. A point that failed this "
                "would mean an arithmetic slip in `E₀`, `A` or `ω₀`.",
            ],
        },
        "quiz_title": "Energy, its conservation and its picture",
        "quiz": [
            {"q": "For `m = 1`, `k = 4` and the start `(3, 8)`, what is `E₀`?",
             "a": ["`50`", "`32`", "`18`", "`82`"],
             "c": 0,
             "why": "`E₀ = ½·1·64 + ½·4·9 = 32 + 18 = 50`. `32` is the kinetic term "
                    "alone and `18` the spring term alone. `82` is `64 + 18`, which "
                    "drops the `½` from the kinetic term."},
            {"q": "At the moment a free mass reaches its greatest displacement `x = A` and is momentarily at rest, where is the energy?",
             "a": ["All of it is in the spring, and it equals `E₀`",
                   "It has been lost, because the mass has stopped",
                   "Half is in the spring and half is in the motion",
                   "All of it is in the motion"],
             "c": 0,
             "why": "At `v = 0` the kinetic term `½m·v²` is zero, so `½k·x² = E₀`: the "
                    "spring holds all of it. Nothing is lost, because `E` is conserved "
                    "without damping. A half-and-half split happens where `x² = A²/2`, "
                    "part of the way round, not at the ends, and the energy is in the motion "
                    "only when the spring is relaxed."},
            {"q": "The same start on `m = 1`, `k = 4` has `A = 5`. What are the semi-axes of its ellipse in the position and velocity directions?",
             "a": ["`5` and `5`", "`5` and `10`", "`25` and `100`", "`5` and `5/2`"],
             "c": 1,
             "why": "The position semi-axis is `A = 5` and the velocity semi-axis is "
                    "`A·ω₀ = 5·2 = 10`. They would be equal only if `ω₀ = 1`. The squares "
                    "`25` and `100` are the denominators in the equation, not the "
                    "semi-axes. Dividing by `ω₀` instead of multiplying gives `5/2`."},
            {"q": "For `m = 2`, `k = 5` and the start `(1, 0)`, what is `E₀`?",
             "a": ["`5`", "`1`", "`5/4`", "`5/2`"],
             "c": 3,
             "why": "`E₀ = ½·2·0 + ½·5·1 = 5/2`. `5` forgets the `½`. `1` is `A²`, a "
                    "different quantity. `5/4` takes the half of the half, as if "
                    "`½` had been applied twice."},
        ],
        "mistakes": [
            ("Believing the energy is lost at the turning points because the mass stops",
             "At the turning point `x = 5`, `v = 0`, the lab's first preset has "
             "`½m·v² = 0` but `½k·x² = ½·4·25 = 50 = E₀`. The kinetic energy has not "
             "vanished: it has become spring energy. A moment later the mass is moving "
             "again and the spring is relaxing. The sum is `50` at every instant, and "
             "the proof above is the reason."),
            ("Reading the ellipse as a graph of x against time",
             "The ellipse has no time axis. Each point `(x, v)` is a state, and time is "
             "the speed at which the point goes round, once per period `2π/ω₀`. The "
             "graph of `x` against `t` is the cosine of the previous lesson, a different "
             "picture of the same motion."),
            ("Expecting the ellipse to be a circle",
             "It is a circle only when the two semi-axes `A` and `A·ω₀` are equal, "
             "which needs `ω₀ = 1`. On the first preset they are `5` and `10`. Rescaling "
             "the velocity axis by `ω₀` would make a circle, which is one reason the "
             "frequency `ω₀` is the natural unit of angular speed."),
        ],
        "standard": (
            "Finish when you can compute the energy of an undamped swing and say what it does.",
            "You should be able to compute E₀ = ½m·v₀² + ½k·x₀² exactly, show that "
            "E′ = v·(m·x″ + k·x) is zero, write the ellipse x²/A² + v²/(A·ω₀)² = 1 "
            "with its semi-axes, and say where the energy sits at the ends and the "
            "middle of a swing."),
        "note": 'Conservation holds because the equation has no <em>c</em>. With a damper the derivative of the energy is <em>−c·v²</em>, which is negative whenever the mass is moving, and the ellipse becomes a spiral inward. How quickly it does, and what shape it takes, is the question of &ldquo;Overdamped, Critical and Underdamped&rdquo;.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "overdamped-critical-and-underdamped",
        "title": "Overdamped, Critical and Underdamped",
        "module": "Damping",
        "one_line": "Classify the motion from the sign of c² − 4mk, write the solution form for each case, and compute the critical damping 2√(mk).",
        "summary": (
            "Add a damper and the characteristic equation `m·r² + c·r + k = 0` has a "
            "discriminant `c² − 4mk` whose sign sorts every oscillator into one of three "
            "kinds. Positive, and there are two real decays and no oscillation. Zero, "
            "and the motion is critically damped, the borderline. Negative, and it "
            "still oscillates inside a shrinking envelope. The damping that makes the "
            "discriminant zero is `c_crit = 2√(mk)`."
        ),
        "key": [
            "m·r² + c·r + k = 0     roots decide the motion",
            "c² − 4mk > 0   overdamped, two real decays",
            "c² − 4mk = 0   critical, (C₁ + C₂·t)·e^(rt)",
            "c² − 4mk < 0   underdamped, still oscillates",
            "c_crit = 2√(mk)",
        ],
        "key_label": "One sign sorts every damped oscillator",
        "concepts_intro": (
            "Three ideas: the sign that decides, the three solution forms it chooses "
            "between, and the damping at which the choice changes."
        ),
        "concepts": [
            ("The discriminant decides the kind",
             "Substitute `x = e^(rt)` into `m·x″ + c·x′ + k·x = 0` and divide by `e^(rt)`: "
             "`m·r² + c·r + k = 0`. The quadratic formula gives "
             "`r = (−c ± √(c² − 4mk))/(2m)`. The sign of `c² − 4mk` says whether the "
             "roots are two real numbers, one repeated real number, or a complex pair, "
             "exactly as in &ldquo;The Characteristic Equation&rdquo; in the previous "
             "course. Here every root has a negative real part, so every motion dies away."),
            ("Each kind has its own solution form",
             "Overdamped: two negative real roots `r₁` and `r₂`, and "
             "`x = C₁·e^(r₁t) + C₂·e^(r₂t)`. Critical: one repeated root "
             "`r = −c/(2m)`, and `x = (C₁ + C₂·t)·e^(rt)`. Underdamped: a complex "
             "pair `α ± β·i` with `α = −c/(2m)`, and an oscillation inside the decay "
             "`e^(αt)`. The previous course derived all three; this lesson reads them as "
             "statements about a damper."),
            ("Critical damping is the value of c where the sign flips",
             "Set `c² − 4mk = 0` and `c = 2√(mk)`. Below it the damper is too weak to stop "
             "the oscillation, and above it the damper is strong enough that the mass "
             "never swings through rest and back. For `m = 1` and `k = 4` the "
             "critical value is `c = 2√4 = 4`. The lab calls it `c_crit` and prints it "
             "exactly, as a surd when `m·k` is not a perfect square."),
        ],
        "read_title": "Three kinds of damped motion and the damping between them",
        "read_intro": "The characteristic equation again, the three cases with a lab preset each, the borderline value, and the reason the strongest damping is not the quickest.",
        "body": [
            ("p", "A damper turns the free oscillator into the general equation "
                  "`m·x″ + c·x′ + k·x = 0`. It is a second-order linear equation with "
                  "constant coefficients, and the previous course solved all of them: "
                  "look for `e^(rt)`, and the roots of `m·r² + c·r + k` decide the "
                  "rest. What this lesson adds is what the three outcomes mean for a "
                  "spring."),
            ("def", ("Overdamped, critically damped, underdamped",
                     "With `c > 0`, the motion is <strong>overdamped</strong> when "
                     "`c² − 4mk > 0`, <strong>critically damped</strong> when "
                     "`c² − 4mk = 0`, and <strong>underdamped</strong> when "
                     "`c² − 4mk < 0`.",
                     "The lab also calls `c = 0` <strong>undamped</strong>; there the "
                     "roots are `±ω₀·i` and the previous module applies.")),
            ("math", [
                "m·r² + c·r + k = 0",
                "r = (−c ± √(c² − 4mk)) / (2m)",
                "c_crit = 2√(m·k)     where  c² − 4mk = 0",
            ]),
            ("h3", "One spring, three dampers"),
            ("p", "Keep `m = 1` and vary the damper. The three presets of the lab are the "
                  "three kinds, and the discriminant tile says which is which."),
            ("math", [
                "k = 4, c = 5:   r² + 5r + 4 = (r + 1)(r + 4)",
                "                disc 9, roots −1 and −4, overdamped",
                "k = 4, c = 4:   r² + 4r + 4 = (r + 2)²",
                "                disc 0, root −2 twice, critical",
                "k = 5, c = 2:   r² + 2r + 5 = 0",
                "                disc −16, roots −1 ± 2i, underdamped",
            ]),
            ("example", ("Overdamped, c = 5",
                         "`c² − 4mk = 25 − 16 = 9`, positive. The roots are `−1` and `−4`, "
                         "so `x = C₁·e^(−t) + C₂·e^(−4t)`. Neither term oscillates, and "
                         "both decay. The mass slides back toward rest and may pass "
                         "through it once at most.",
                         "The lab's `c_crit` for `m = 1`, `k = 4` is `4`, and `c = 5` is "
                         "above it. That is the meaning of overdamped: more damping "
                         "than the critical amount.")),
            ("example", ("Underdamped, c = 2 with k = 5",
                         "`c² − 4mk = 4 − 20 = −16`, negative. The roots are "
                         "`−1 ± 2i`, so `x = e^(−t)·(C₁cos(2t) + C₂sin(2t))`: the "
                         "oscillation of the earlier lessons inside a decay. The critical "
                         "value for this mass and spring is `2√5`, about `4.47214` and "
                         "rounded, and `c = 2` is well below it.",
                         "The pattern in the three examples is one comparison: "
                         "`c` against `c_crit`. Below it, the mass oscillates; at it, "
                         "the roots merge; above it, they separate into two real decays.")),
            ("h3", "Stronger damping is not always quicker"),
            ("p", "It is natural to expect that a bigger damper brings the mass to rest "
                  "sooner. It does not, once the damping passes the critical value. In "
                  "the overdamped case the two roots are `r₁` and `r₂`, and the "
                  "slow one controls how long the motion takes. For `c = 5` it is `−1`, "
                  "giving `e^(−t)`. The critical case, `c = 4`, has the repeated root "
                  "`−2`, giving `(C₁ + C₂·t)·e^(−2t)`. Eventually `e^(−2t)` is far smaller "
                  "than `e^(−t)`, even with the factor `t` in front of it."),
            ("p", "The lab's fourth preset pushes this further. For `c = 10` and `k = 4` the "
                  "discriminant is `100 − 16 = 84`, the roots are `−5 ± √21`, and the slow "
                  "root `−5 + √21` is between `−1` and `0`, because `4 < √21 < 5`. Ten units "
                  "of damper make the return slower than five. The damper holds the "
                  "mass so firmly that it creeps."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "over",
            "presets": [
                {"id": "over", "label": "c = 5, k = 4",
                 "m": 1, "c": 5, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "overdamped", "osDisc": "9", "osCcrit": "4"}},
                {"id": "critical", "label": "c = 4, k = 4",
                 "m": 1, "c": 4, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "critically damped", "osDisc": "0", "osCcrit": "4", "osCross": "none for t > 0"}},
                {"id": "under", "label": "c = 2, k = 5",
                 "m": 1, "c": 2, "k": 5, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "underdamped", "osDisc": "−16", "osCcrit": "2√5 ≈ 4.47214"}},
                {"id": "very-over", "label": "c = 10, k = 4",
                 "m": 1, "c": 10, "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osType": "overdamped", "osDisc": "84", "osCcrit": "4"}},
            ],
            "panel_title": "Move the damper and read the class",
            "panel_intro": (
                "Pick each preset and read the class and the discriminant before you look at the "
                "curve. Then change c alone in the damping box and find the value at which the "
                "class changes. The critical damping tile tells you where to look. The curve is "
                "drawn by stepping in floating point; the discriminant and the critical damping "
                "are exact."),
        }),
        "steps_title": "Classifying a damped oscillator",
        "steps_intro": "Four moves. Compute the discriminant as a number before you name the class.",
        "steps": [
            ("Write the characteristic equation",
             "`m·r² + c·r + k = 0`, with the three numbers read from the equation. "
             "For `x″ + 5x′ + 4x = 0` it is `r² + 5r + 4 = 0`."),
            ("Compute c² − 4mk",
             "Square the damping, subtract four times the product of mass and spring "
             "constant. Do it as a number: `25 − 16 = 9`. It is the first number the lab "
             "prints."),
            ("Read the sign and name the class",
             "Positive: overdamped. Zero: critically damped. Negative: underdamped. "
             "Write the solution form for that class and the roots that go into it."),
            ("Compute the critical damping and compare",
             "`c_crit = 2√(mk)`. Compare `c` with it: smaller is underdamped, equal is "
             "critical, larger is overdamped. This check must agree with the sign of the "
             "discriminant."),
        ],
        "worked": {
            "title": "m = 1, k = 4, with three dampers",
            "intro": [
                "Take `m = 1` and `k = 4`. First find the critical damping, then classify "
                "`c = 5`, and then take a lighter damper `c = 2` with the spring changed "
                "to `k = 5` to see the third kind.",
            ],
            "lines": [
                "c_crit = 2√(1·4) = 2·2 = 4",
                "c = 5:  disc = 25 − 16 = 9 > 0",
                "        (r + 1)(r + 4) = 0, r = −1, −4",
                "        overdamped: C₁e^(−t) + C₂e^(−4t)",
                "k = 5, c = 2:  disc = 4 − 20 = −16 < 0",
                "        r = −1 ± 2i, underdamped",
            ],
            "after": [
                "The two checks agree. `c = 5` exceeds `c_crit = 4` and has a positive "
                "discriminant. For `k = 5` the critical damping is `2√5`, which is "
                "larger than `2`, and the discriminant is negative. Whenever the "
                "comparison with `c_crit` and the sign of `c² − 4mk` disagree, one of "
                "them has a slip in it.",
            ],
        },
        "quiz_title": "Classifying and comparing",
        "quiz": [
            {"q": "For `m = 1`, `c = 6`, `k = 4`, how is the motion classified?",
             "a": ["Underdamped", "Critically damped", "Undamped", "Overdamped"],
             "c": 3,
             "why": "`c² − 4mk = 36 − 16 = 20 > 0`, so it is overdamped. It is not "
                    "critical, because the discriminant is not zero. It is not "
                    "underdamped, because that needs a negative discriminant, and it "
                    "is not undamped, since `c ≠ 0`."},
            {"q": "What is the critical damping for `m = 2` and `k = 8`?",
             "a": ["`4`", "`8`", "`16`", "`2`"],
             "c": 1,
             "why": "`c_crit = 2√(m·k) = 2√16 = 8`. At `c = 8` the discriminant is "
                    "`64 − 64 = 0`. `4` is `√16`, missing the factor `2`; `16` is `m·k`, "
                    "missing the root; and `2` is just the mass."},
            {"q": "Which roots belong to `x″ + 2x′ + 5x = 0`?",
             "a": ["`−1` and `−5`", "`−1 ± 2i`", "`1 ± 2i`", "`−2` and `−5`"],
             "c": 1,
             "why": "`r² + 2r + 5 = 0` gives `r = (−2 ± √(4 − 20))/2 = −1 ± 2i`. A "
                    "positive real part `1 ± 2i` would make the motion grow, which "
                    "damping cannot do. The pair `−1` and `−5` would multiply to "
                    "`5` but add to `−6`, not `−2`, and `−2` and `−5` fail the product "
                    "as well."},
            {"q": "With `m = 1` and `k = 4`, compare `c = 4` and `c = 5`. Which statement about the long run is correct?",
             "a": ["`c = 5` returns to rest faster, because its damper is stronger",
                   "They return at the same rate, because both are non-oscillating",
                   "`c = 4` returns faster in the long run: its decay is `e^(−2t)` against `e^(−t)` for `c = 5`",
                   "`c = 4` oscillates and `c = 5` does not, so `c = 5` is quicker"],
             "c": 2,
             "why": "The critical case decays like `(C₁ + C₂·t)·e^(−2t)`, and the "
                    "overdamped case is dominated by its slow root `−1`, so it decays like "
                    "`e^(−t)`. A stronger damper does not mean faster return. The "
                    "rates differ, so they are not the same, and `c = 4` is critically "
                    "damped and does not oscillate."},
        ],
        "mistakes": [
            ("Believing more damping always means a quicker return to rest",
             "Past the critical value the opposite happens. With `k = 4`, `c = 4` decays "
             "like `e^(−2t)`, `c = 5` like `e^(−t)` and `c = 10`, whose slow root is "
             "`−5 + √21`, between `−1` and `0`, even more slowly. The damper "
             "slows the mass as it approaches rest, and one slow exponential dominates "
             "the long run. Critical damping is the quickest of the non-oscillating "
             "cases, not the strongest."),
            ("Calling any damped motion that does not cross zero critically damped",
             "The class is decided by the sign of `c² − 4mk` and nothing else. The "
             "first preset, `c = 5`, never crosses zero from the start `(1, 0)`, "
             "but its discriminant is `9`, not `0`: it is overdamped. Critical is the "
             "single value `c = 2√(mk)` between the two kinds."),
            ("Reading the underdamped roots as growing because of the plus sign",
             "The roots `−1 ± 2i` have real part `−1`. The `±` belongs to the imaginary "
             "part, which makes the cosine and sine, and the real part makes the decay "
             "`e^(−t)`. A damper cannot make the motion grow: `−c/(2m)` is negative "
             "whenever `c > 0`."),
        ],
        "standard": (
            "Finish when you can classify a damped oscillator and find the damping that separates the kinds.",
            "You should be able to compute c² − 4mk exactly, name the motion overdamped, "
            "critical or underdamped from its sign, write the solution form and the "
            "roots for each, compute c_crit = 2√(mk) as an integer or a surd, and say "
            "why more damping is not always a quicker return."),
        "note": 'The underdamped case still oscillates, but not at the natural frequency. The new frequency, and the curve the peaks follow as they shrink, are the subject of &ldquo;Underdamped Motion and the Envelope&rdquo;.',
    },

    # ---------------------------------------------------------------- 05
    {
        "slug": "underdamped-motion-and-the-envelope",
        "title": "Underdamped Motion and the Envelope",
        "module": "Damping",
        "one_line": "Compute the pseudo-frequency ω_d² = k/m − c²/(4m²) exactly, the envelope rate c/(2m), and the ratio of successive peaks.",
        "summary": (
            "An underdamped oscillator keeps oscillating while it fades. The oscillation "
            "has its own frequency, the pseudo-frequency `ω_d`, which is lower than "
            "the natural frequency `ω₀`, and it sits inside a pair of exponential curves "
            "that shrink at the rate `c/(2m)`. Successive peaks are one pseudo-period "
            "apart, and each is smaller than the last by one fixed factor."
        ),
        "key": [
            "x = e^(αt)·(C₁cos(ω_d t) + C₂sin(ω_d t))",
            "α = −c/(2m)     envelope ±A·e^(αt)",
            "ω_d² = k/m − c²/(4m²)  <  ω₀²",
            "pseudo-period  T_d = 2π/ω_d",
            "peaks shrink by e^(α·T_d) = e^(−c·T_d/(2m))",
        ],
        "key_label": "Slower than the spring, inside a shrinking envelope",
        "concepts_intro": (
            "Three ideas: the new frequency, the curve that bounds the motion, and the "
            "fixed factor between peaks."
        ),
        "concepts": [
            ("The frequency falls to ω_d",
             "The roots are `α ± ω_d·i` with `α = −c/(2m)`, and the quadratic formula "
             "gives `ω_d = √(4mk − c²)/(2m)`. Squared, "
             "`ω_d² = k/m − c²/(4m²) = ω₀² − (c/(2m))²`. The damper subtracts a "
             "square from `ω₀²`, so `ω_d < ω₀` for every `c > 0`: damping slows the "
             "oscillation as well as shrinking it."),
            ("The envelope bounds the motion",
             "Write the solution as `e^(αt)·(C₁cos(ω_d t) + C₂sin(ω_d t))`. The bracket "
             "is a swing of constant amplitude `A`, so the whole is at most `A·e^(αt)` in "
             "size. The curves `±A·e^(αt)` are the <em>envelope</em>, with decay rate "
             "`c/(2m)`. The lab draws them with the motion."),
            ("Successive peaks differ by a fixed factor",
             "The bracket repeats every pseudo-period `T_d = 2π/ω_d`, and the decay "
             "multiplies by `e^(α·T_d)` over that time. So every peak is "
             "`e^(−c·T_d/(2m))` times the one before it, whatever the start. The factor "
             "is irrational and the lab prints it with `≈`."),
        ],
        "read_title": "A lower frequency inside a falling envelope",
        "read_intro": "The roots again, the pseudo-frequency, the envelope, the fixed ratio of peaks, and three presets with a different damping each.",
        "body": [
            ("p", "The previous lesson ended with the underdamped roots. This lesson "
                  "reads them as numbers. For `m·r² + c·r + k = 0` with "
                  "`c² − 4mk < 0` the roots are a complex pair, and writing out the real "
                  "and imaginary parts gives the three quantities that describe the "
                  "motion."),
            ("math", [
                "r = −c/(2m)  ±  i·√(4mk − c²)/(2m)",
                "α = −c/(2m)       ω_d = √(4mk − c²)/(2m)",
                "ω_d² = k/m − c²/(4m²)",
            ]),
            ("def", ("Pseudo-frequency and envelope",
                     "In the underdamped solution "
                     "`x = e^(αt)·(C₁cos(ω_d t) + C₂sin(ω_d t))` the number `ω_d` is the "
                     "<strong>pseudo-frequency</strong> and `T_d = 2π/ω_d` the "
                     "<strong>pseudo-period</strong>. The motion is not periodic, since it "
                     "keeps shrinking, which is why the prefix.",
                     "The curves `±A·e^(αt)` are the <strong>envelope</strong>; the "
                     "rate `c/(2m) = −α` says how fast it falls.")),
            ("thm", ("The ratio of successive peaks",
                     "In an underdamped motion, the value of `x` one pseudo-period "
                     "later is `e^(α·T_d)` times its value now, at every `t`.")),
            ("proof", ["The bracket `C₁cos(ω_d t) + C₂sin(ω_d t)` has period "
                       "`T_d = 2π/ω_d`, so replacing `t` by `t + T_d` leaves it "
                       "unchanged.",
                       "The factor `e^(αt)` becomes `e^(αt)·e^(α·T_d)`. So "
                       "`x(t + T_d) = e^(α·T_d)·x(t)` for every `t`, and differentiating "
                       "both sides gives the same for the rate: "
                       "`x′(t + T_d) = e^(α·T_d)·x′(t)`. If `x` has a peak at `t₁`, "
                       "where `x′(t₁) = 0`, then `x′(t₁ + T_d) = 0` as well, so the next "
                       "peak is exactly one pseudo-period later and is "
                       "`e^(α·T_d) = e^(−c·T_d/(2m))` times the first. The peaks of `x` "
                       "are not where the bracket peaks: each comes a little earlier, "
                       "where the bracket's rate balances the decay. They are spaced by "
                       "`T_d` all the same."]),
            ("example", ("c = 2, k = 5, started at 2",
                         "With `m = 1`: `ω₀² = 5`, `c/(2m) = 1`, and "
                         "`ω_d² = 5 − 1 = 4`, so `ω_d = 2` and `T_d = 2π/2 = π`. The "
                         "envelope falls like `e^(−t)`, and each peak is `e^(−π)` times "
                         "the one before, which the lab prints as about `0.0432139` and "
                         "rounded.",
                         "That is a very fast fade, and the lab marks it rounded. Compare the undamped period of this spring, `2π/√5`, "
                         "about `2.80993`, with the pseudo-period `π`, about "
                         "`3.14159`. The damped oscillation is slower.")),
            ("example", ("A light damper",
                         "Take `m = 1`, `c = 1/2`, `k = 4`. Now `c/(2m) = 1/4`, and "
                         "`ω_d² = 4 − 1/16 = 63/16`. The pseudo-frequency "
                         "`ω_d = √63/4` is a surd, barely below `ω₀ = 2`.",
                         "A light damper changes the frequency by very little and the "
                         "peaks by a modest factor: the lab prints the ratio as "
                         "about `0.453116`, rounded. Damping shows first in the "
                         "envelope and only second in the frequency.")),
            ("example", ("A heavier mass",
                         "Take `m = 2`, `c = 2`, `k = 5`. The rate is "
                         "`c/(2m) = 1/2`, and `ω_d² = 5/2 − 1/4 = 9/4`, so "
                         "`ω_d = 3/2` exactly. The pseudo-period is `4π/3`.",
                         "Compared with the first preset, doubling the mass halves the "
                         "envelope rate for the same damper (`c/(2m)` has `m` in the "
                         "denominator), so the heavy mass fades more slowly: the lab's "
                         "ratio of successive peaks is about `0.123145`, rounded, "
                         "against `0.0432139`.")),
            ("p", "The same three quantities are all that describe a ringing bell, a "
                  "plucked string heard as a decaying tone, or a car's suspension after a "
                  "bump. The frequency tells you the note, the envelope rate tells you how "
                  "long it rings, and the ratio of peaks is how much quieter it is each "
                  "time round."),
        ],
        "lab": ("dekit", {
            "mode": "oscillator",
            "view": "motion",
            "preset": "two-five",
            "presets": [
                {"id": "two-five", "label": "c = 2, k = 5",
                 "m": 1, "c": 2, "k": 5, "ic": [2, 0], "F0": 0,
                 "expect": {"osOmegaD": "ω_d² = 4", "osEnvelope": "c/(2m) = 1; peaks shrink by ≈ 0.0432139", "osPeriod": "2π/√5 ≈ 2.80993"}},
                {"id": "light", "label": "c = 1/2, k = 4",
                 "m": 1, "c": "1/2", "k": 4, "ic": [1, 0], "F0": 0,
                 "expect": {"osOmegaD": "ω_d² = 63/16", "osEnvelope": "c/(2m) = 1/4; peaks shrink by ≈ 0.453116", "osPeriod": "π ≈ 3.14159"}},
                {"id": "heavy", "label": "m = 2, c = 2, k = 5",
                 "m": 2, "c": 2, "k": 5, "ic": [1, 0], "F0": 0,
                 "expect": {"osOmegaD": "ω_d² = 9/4", "osEnvelope": "c/(2m) = 1/2; peaks shrink by ≈ 0.123145", "osPeriod": "4π/√10 ≈ 3.97384"}},
            ],
            "panel_title": "Read the frequency, the envelope and the peak ratio",
            "panel_intro": (
                "The motion is drawn with its envelope as the two outer curves. Read the "
                "pseudo-frequency squared and the envelope tile for each preset, then compare "
                "the undamped period with the period you get from the pseudo-frequency. The "
                "curve is drawn by stepping in floating point; the squared frequency and the "
                "envelope rate are exact, and the peak ratio behind ≈ is rounded."),
        }),
        "steps_title": "From m, c and k to the three numbers of an underdamped motion",
        "steps_intro": "Five moves. The first is the check that the case is underdamped at all.",
        "steps": [
            ("Confirm that c² − 4mk is negative",
             "If it is not, there is no oscillation and there is no pseudo-frequency; "
             "go back to the previous lesson's classification."),
            ("Compute the envelope rate c/(2m)",
             "A fraction. For `m = 1`, `c = 2` it is `1`; for `m = 2`, `c = 2` it is `1/2`."),
            ("Subtract its square from ω₀²",
             "`ω_d² = k/m − (c/(2m))²`. This is the formula the lab prints. Take a "
             "root only if you need the frequency itself, and keep it as a surd if the "
             "root is not rational."),
            ("Write the pseudo-period",
             "`T_d = 2π/ω_d`, a symbol with `π`; round it only at the end, with `≈`."),
            ("Find the ratio of successive peaks",
             "`e^(−(c/(2m))·T_d)`, rounded and marked `≈`. For the first preset the "
             "exponent is `−1·π`, and the ratio is `e^(−π)`."),
        ],
        "worked": {
            "title": "x″ + 2x′ + 5x = 0",
            "intro": [
                "The first preset: `m = 1`, `c = 2`, `k = 5`, started at `x(0) = 2` "
                "with `x′(0) = 0`.",
            ],
            "lines": [
                "disc = 4 − 20 = −16 < 0     underdamped",
                "c/(2m) = 1       ω₀² = 5",
                "ω_d² = 5 − 1 = 4          ω_d = 2",
                "T_d = 2π/2 = π",
                "roots −1 ± 2i:  x = e^(−t)·(C₁cos(2t) + C₂sin(2t))",
                "peak ratio e^(−1·π) = e^(−π) ≈ 0.0432139",
            ],
            "after": [
                "The pseudo-frequency `2` is below the natural frequency `√5`, as it "
                "must be, since `ω_d² = 5 − 1`. The constants for the start `(2, 0)` "
                "are `C₁ = 2` and `C₂ = 1`, from `x′(0) = −C₁ + 2·C₂ = 0`; "
                "the lab does not fit them, but the envelope it draws is built from "
                "them.",
            ],
        },
        "quiz_title": "Frequency, envelope and peaks",
        "quiz": [
            {"q": "For `m = 1`, `c = 2`, `k = 10`, what is `ω_d²`?",
             "a": ["`6`", "`10`", "`9`", "`8`"],
             "c": 2,
             "why": "`c/(2m) = 1`, so `ω_d² = 10 − 1 = 9`. `10` ignores the damping, "
                    "which is the claim that damping does not change the frequency. `6` "
                    "subtracts `c²/m² = 4` instead of `c²/(4m²) = 1`. `8` subtracts `c = 2`, "
                    "which is not squared."},
            {"q": "For `m = 2` and `c = 2`, what is the envelope rate `c/(2m)`?",
             "a": ["`2`", "`1`", "`1/4`", "`1/2`"],
             "c": 3,
             "why": "`c/(2m) = 2/4 = 1/2`. `1` is `c/(2m)` with the mass forgotten "
                    "(`c/2`), `2` is `c` alone, and `1/4` divides by `4m` instead of `2m`."},
            {"q": "The envelope is `e^(−t)` and the pseudo-period is `π`. By what factor is each peak smaller than the one before?",
             "a": ["`e^(−1)`, one unit of time's decay", "`e^(−π) ≈ 0.0432139`, because the peaks are `π` apart",
                   "`e^(−2π)`", "No fixed factor: it depends on the start"],
             "c": 1,
             "why": "Peaks are one pseudo-period apart, so the envelope falls by "
                    "`e^(−1·π) = e^(−π)` between them. `e^(−1)` is the fall over one unit "
                    "of time, not over one period. `e^(−2π)` is the fall over two periods. "
                    "The factor does not depend on the start, because `x(t + T_d)` is "
                    "`e^(−π)·x(t)` for every solution."},
            {"q": "How does the pseudo-frequency `ω_d` compare with the natural frequency `ω₀` for an underdamped oscillator with `c > 0`?",
             "a": ["`ω_d` is the same", "`ω_d` is larger", "`ω_d` is smaller",
                   "It depends on the start"],
             "c": 2,
             "why": "`ω_d² = ω₀² − (c/(2m))²` is `ω₀²` minus a positive square, so "
                    "`ω_d < ω₀`. It is not the same, which is the common misconception, "
                    "it is not larger, and the start fixes the constants and the "
                    "amplitude but not the frequency."},
        ],
        "mistakes": [
            ("Believing damping changes the amplitude but not the frequency",
             "On the first preset the natural frequency is `ω₀ = √5`, with period "
             "`2π/√5`, about `2.80993`. With the damper, `ω_d² = 5 − 1 = 4`, so "
             "`ω_d = 2` and the pseudo-period is `π`, about `3.14159`: the oscillation "
             "is measurably slower. The change is small for a light damper, "
             "`63/16` against `4` in the second preset, and large when `c` is near "
             "`c_crit`, where `ω_d` falls to zero."),
            ("Measuring the envelope rate as c instead of c/(2m)",
             "The decay rate is `−α = c/(2m)`, half of `c` per unit mass. For `m = 1` and "
             "`c = 2` it is `1`, and for `m = 2` and `c = 2` it is `1/2`. Using "
             "`c` would make the envelope fall twice as fast for a unit mass and "
             "four times as fast for the heavier one."),
            ("Using the natural period to compute the ratio of peaks",
             "The peaks are one <em>pseudo</em>-period apart. For the first preset the ratio "
             "is `e^(−π) ≈ 0.0432139` from `T_d = π`. The natural period "
             "`2π/√5` would give `e^(−2π/√5)`, a different and wrong number, because "
             "the damped oscillation does not run at the natural frequency."),
        ],
        "standard": (
            "Finish when you can describe an underdamped motion by its frequency, its envelope and its peak ratio.",
            "You should be able to compute ω_d² = k/m − c²/(4m²) exactly, the envelope "
            "rate c/(2m), and the pseudo-period 2π/ω_d, give the ratio of successive "
            "peaks as a rounded number marked ≈, and say why ω_d is below ω₀."),
        "note": 'A designer rarely wants an oscillation at all. The border between this lesson and the one before it, where the oscillation disappears just as the damping reaches its critical value, is a choice in engineering, taken up in &ldquo;Critical Damping and Design&rdquo;.',
    },
]
