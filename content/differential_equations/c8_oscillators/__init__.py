"""Oscillators, Damping and Resonance."""


from . import part_a, part_b


COURSE = {
    "slug": "oscillators-damping-and-resonance",
    "title": "Oscillators, Damping and Resonance",
    "level": "Advanced",
    "summary": (
        "One equation, `m·x″ + c·x′ + k·x = F₀·cos(ωt)`, read as a mass on a spring: free "
        "motion first, with its frequency, amplitude, phase and conserved energy; then the "
        "three kinds of damping and what each does to the motion; then a push applied from "
        "outside, the response it produces, the resonance where that response outgrows any "
        "bound, and the damped version where the peak is finite and sits somewhere other "
        "than the natural frequency. Every coefficient is a fraction and every quantity "
        "that can be exact is."
    ),
    "blurb": (
        "The previous course solved `a·y″ + b·y′ + c·y = 0` as a piece of algebra: find the "
        "roots of one quadratic, and the roots decide the shape. This course gives the "
        "letters their meanings. `m` is a mass, `k` a spring, `c` a drag, and the roots of "
        "the quadratic become frequencies and decay rates you can name and compare. The "
        "questions change with the meaning: how fast does it swing, how big, how long until "
        "it is still, and what happens when something keeps pushing. The lab for the whole "
        "course is one oscillator whose exact quantities appear as tiles &mdash; `ω₀²`, "
        "`c² − 4mk`, the critical damping, the amplitude squared, the forced response &mdash; "
        "with the motion itself drawn by stepping in floating point and labelled as a drawing. "
        "A figure that involves `π`, a square root or an exponential is rounded to six "
        "figures and marked `≈`; everything else is a fraction."
    ),
    "key": [
        "m·x″ + c·x′ + k·x = F₀·cos(ωt)",
        "ω₀² = k/m     period 2π/ω₀",
        "c² − 4mk:  > 0 over, 0 critical, < 0 under",
        "ω_d² = k/m − c²/(4m²)   envelope e^(−ct/(2m))",
        "A = F₀/(m·(ω₀² − ω²))   fails at ω = ω₀",
        "ω_r² = k/m − c²/(2m²), not k/m",
    ],
    "assumes_short": "Second-Order Linear Equations",
    "assumes_long": (
        "Second-Order Linear Equations, which supplies the characteristic equation, the three "
        "kinds of roots and the solutions they give, and the fitting of two initial "
        "conditions, and through it First-Order Linear Equations for undetermined "
        "coefficients. From Algebra, Quadratics and Complex Numbers for the quadratic "
        "formula and `i`"
    ),
    "outcomes_intro": (
        "By the end you can take a mass, a damper and a spring from their three numbers to "
        "the shape of the motion without solving anything, and you can predict how a steady "
        "push is answered. Each outcome is something you can compute and check against the "
        "lab."
    ),
    "outcomes": [
        ("Derive the oscillator equation and its frequency",
         "Write `m·x″ + c·x′ + k·x = 0` from Newton's law and Hooke's law, compute "
         "`ω₀² = k/m` exactly, and give the period as a symbol and as a rounded number."),
        ("Convert and read free motion",
         "Turn `C₁cos(ω₀t) + C₂sin(ω₀t)` into `A·cos(ω₀t − φ)`, compute `A²` exactly, and "
         "state the conserved energy and the phase-plane ellipse it draws."),
        ("Classify the damping",
         "Decide from the sign of `c² − 4mk` whether the motion is overdamped, critical or "
         "underdamped, compute the critical damping `2√(mk)`, and write each solution form."),
        ("Compute what damping does to an oscillation",
         "Find the pseudo-frequency, the envelope rate and the ratio of successive peaks, "
         "and say whether a critically damped motion crosses zero."),
        ("Fit the response to a forcing",
         "Compute the undamped forced amplitude exactly, read its sign, write the resonant "
         "solution that grows linearly, and find a beat period."),
        ("Locate the peak of a damped response",
         "Compute the steady amplitude squared and the resonant frequency of a damped "
         "oscillator, and say why the peak is not at the natural frequency."),
    ],
    "syllabus_intro": (
        "Three modules of three lessons each. Free oscillation first, because it fixes the "
        "frequency, the amplitude and the energy that everything later is compared with. "
        "Damping second: one sign decides the kind of motion, and the two lessons after it "
        "say what each kind does and which one a designer wants. Forcing last, where the "
        "natural frequency meets a frequency from outside."
    ),
    "how_to": [
        "Say what the letters mean before you compute with them. `m` is a mass, `k` a "
        "spring constant, `c` a damping constant and `F₀` the size of a push. Units are "
        "left out, because any consistent set will do, but every answer in this course is "
        "a statement about a physical motion, and a negative `k` or `m` is a refusal rather "
        "than a curiosity.",
        "Predict the class of the motion from `c² − 4mk` before you press anything. The "
        "lab prints that number as a tile, and a surprise in it is almost always a slip in "
        "`4mk`.",
        "Read the tier of every number. Fractions in a tile are exact. A figure behind "
        "`≈` is rounded to six figures, and a surd such as `√5` is exact and printed "
        "with its rounded value beside it. The curve itself is drawn by stepping in "
        "floating point, and nothing in a tile comes from that drawing.",
        "Change one number at a time. The labs take any rational `m`, `c` and `k`, and "
        "the lessons are written so that moving a single one &mdash; the mass, the "
        "damping, the forcing frequency &mdash; shows a single effect.",
    ],
    "not_covered": [
        "Real springs. The model assumes a force exactly proportional to the stretch and a "
        "drag exactly proportional to the speed. Real springs stiffen or soften at large "
        "stretch and real drag often grows with the square of the speed, and either "
        "change makes the equation nonlinear and outside this course.",
        "Forcing other than a cosine. A square wave, an impulse or a force that switches on "
        "and off needs either a Fourier series, which is not here, or the Laplace transform, "
        "which is the last course. The cosine is the case undetermined coefficients can "
        "verify exactly.",
        "The transient in a forced damped system. The lab reports the steady amplitude, "
        "which the motion settles to; the way it settles, and how long it takes, is the "
        "damped free solution of the earlier lessons added to it.",
        "Coupled oscillators and normal modes. Two masses on three springs is a system of "
        "two equations, and the next course is where systems begin.",
        "Modelling as a skill. The spring, the door closer and the bridge are stated with "
        "their equations given. Choosing `m`, `c` and `k` for a real structure is the work "
        "of an engineer with measurements, not something a lab can tell you.",
    ],
    "footer_lead": (
        "Every frequency squared, every discriminant, every amplitude squared and every "
        "energy in this course is an exact fraction, and every closed form the lessons "
        "write is checked by substituting it into the equation, line by line, never by "
        "evaluating it; the lab computes the exact quantities and draws the motion. "
        "<strong>The figures that are not "
        "rational say so</strong>: a period involving `π`, a square root, a phase angle and "
        "a ratio of successive peaks are printed rounded to six figures and marked `≈`. "
        "The curves are drawn by stepping in floating point. What the lab cannot do is "
        "tell you that a real spring is linear, or that a real damper is proportional to "
        "speed: it computes what follows from the equation, and the equation is the "
        "assumption."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
