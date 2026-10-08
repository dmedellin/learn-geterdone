# Philosophy — the build specification

This is the curriculum, lab and authoring contract for the seventh Subject.
Everything an author, a kit engineer or a reviewer needs is here; nothing in it
is a suggestion. Where it says "exactly", a test or a gate enforces it. Where it
says "never", a published page has already been wrong for that reason somewhere
in this library.

Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight note;
`content/AGENTS.md` (all of it, and "Write math a voice can read" twice);
`scripts/mathpath/AGENTS.md` ("a preset's two claims"). This document does not
repeat them.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The ten courses, in order
- §C Every lesson: 108 entries
- §D The two lab kits: `argkit` (8 modes) and `choicekit` (10 modes), and the
  five existing modes reused
- §E Package layout and the author's field checklist
- §F Voice and style, with one exemplary paragraph
- §G What is left out, and why
- §H Wiring notes for the orchestrator

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For Philosophy the answer is "the structure of the position", and
that answer is only honest if every lesson's lab computes a verdict FROM the
lesson's stated premises, cases or payoffs, in exact arithmetic, that the reader
can change the inputs of and watch move. Eighteen kinds of verdict carry the
whole Subject:

| what the reader computes | mode | from |
| --- | --- | --- |
| whether an argument has a counterexample row | `argkit/validity` | premises and a conclusion |
| whether a set of claims can all be true, and which smallest subset cannot | `argkit/consistency` | a list of sentences |
| whether a syllogism's conclusion is forced by its premises' Venn regions | `argkit/syllogism` | two categorical premises |
| what a chain of tolerance conditionals delivers under four treatments of vagueness | `argkit/sorites` | a start count, an end count, a cutoff |
| the truth of `□`/`◇` claims at a world, and which modal axioms the frame validates | `argkit/kripke` | worlds, an accessibility relation, a valuation |
| the truth of a first-order sentence in a finite model, with its witness | `argkit/semantics` | a domain, extensions, names |
| whether a definition agrees with a table of cases, and which formulas would | `argkit/analysis` | conditions, cases, verdicts |
| whether a variable is a but-for cause, or a cause once something is held fixed | `argkit/structural` | Boolean structural equations |
| which act each decision rule picks, the value of information, the indifference probability | `choicekit/decide` | an act × state payoff table |
| exact posteriors, Bayes factors, predictive probabilities, best act after updating | `choicekit/update` | priors, likelihoods, data |
| what a belief threshold accepts, whether the accepted set is consistent, a Dutch book | `choicekit/credence` | a finite outcome space |
| exact partial sums, limits and remainders | `choicekit/series` | a first term, a ratio, a count |
| dominance, pure and mixed Nash equilibria, Pareto verdicts | `choicekit/game` | a bimatrix |
| round-by-round payoffs, a tournament, the discount threshold for cooperation | `choicekit/iterated` | PD payoffs and two strategies |
| the n-player dilemma's equilibrium, optimum, universalisation and replicator path | `choicekit/commons` | payoff polynomials in k |
| winners under six rules, Condorcet cycles, an IIA violation, a manipulation | `choicekit/vote` | a profile of rankings |
| rankings of two welfare distributions under six aggregation rules | `choicekit/aggregate` | two vectors |
| rates within groups against the pooled rate, and whether they reverse | `choicekit/simpson` | two 2×2 count tables |

Five existing modes are reused where they fit exactly: `truth_table`,
`quantifier`, `relation`, `bayes`, `counting`. Where a classic area has nothing
to compute it is taught through the checkable structure of its arguments, or
left out and named in §G. No lesson carries a decorative lab.

**Deliberate deviation from one-kit-per-course.** Philosophy's courses are
organised by topic and its computations cut across topics (ethics needs
`aggregate`, `commons`, `structural`, `consistency` and `decide`). So the rule
here is **one kit per lesson, two new kits for the Subject**, recorded in the
registry comment the way Operations Research records its two-kit courses.

---

## §A PATH fields (`content/philosophy/__init__.py`)

```
"slug": "philosophy",
"title": "Philosophy",
"level": "Beginner → Advanced",
"level_note": "school arithmetic only; the logic is taught inside",
```

**tagline** (the counts are checked against the package by
`test_the_tagline_and_description_state_the_real_counts`; re-verify at wiring):

> Arguments you can test, beliefs you can measure, choices you can rank:
> philosophy taught through the structures it is made of &mdash; validity,
> consistency, credence, expected value, equilibrium, collective choice and
> possible worlds &mdash; from the first argument to the hardest paradox. Ten
> courses and 108 lessons are available.

**description**:

> The Philosophy Subject: ten courses in one order, from arguments and validity
> through knowledge and evidence, science and causation, decision, games and the
> social contract, ethics, justice and collective choice, identity, modality and
> freedom, mind, language and meaning, to the paradoxes. Every lesson computes
> something from the premises, cases or payoffs it states &mdash; a
> counterexample row, a posterior, an equilibrium, a winner &mdash; in exact
> arithmetic in your browser. All ten courses and 108 lessons are available.

**key** (every line ≤ 46 characters, measured without combining marks; no line
carries a second column):

```
valid ⟺ no row: premises T, conclusion F
P(H | E) = P(E | H)·P(H) / P(E)
EU(a) = Σ P(s)·u(a, s)   take the largest
Nash: no player gains by moving alone
A beats B, B beats C, C beats A   a cycle
□p at w  ⟺  p at every world w can see
a paradox: valid, plausible, unacceptable
```

**material** (the hazard of learning THIS subject from interactive examples; it
must differ from the five existing clauses, and `tests/test_site_invariants.py`
needs a `PHIL_DISCLAIMER_RE` that matches it — proposed pattern
`r"only as good as the premises"`):

> every verdict on this path is computed in your browser from the premises,
> cases and payoffs the lesson states, and a verdict is only as good as the
> premises it was computed from &mdash; which is the part no lab can check, and
> the part philosophy is about.

**prerequisites** (paragraphs):

1. School arithmetic: fractions, percentages, and the willingness to add up a
   column. Every number on this path is a fraction or a whole number, and the
   labs do the arithmetic; what is asked of you is to read it.
2. No logic. Arguments and Validity teaches every piece of logic the Subject
   uses, starting from what an argument is. If you have met truth tables before
   you will move quickly through its first half; if you have not, it is where to
   start.
3. No probability. Knowledge and Evidence introduces credence and Bayes' rule
   from a table of a million people, and nothing later assumes more than that
   lesson gives. Discrete Probability on the Discrete Mathematics path covers
   the same ground more formally and is a fine companion, not a prerequisite.
4. Patience with premises. The hard part of philosophy is not following an
   argument but deciding which premise to doubt, and the labs cannot do that
   for you. They will tell you an argument is valid; whether to accept its
   conclusion or reject a premise is the question every lesson leaves open on
   purpose.

**why_order** (paragraphs):

1. Arguments come first because everything that follows is an argument.
   Validity, consistency and the counterexample are the three tools every later
   lesson reaches for, and a reader who cannot yet tell a valid argument from a
   persuasive one will misread the strongest positions in the Subject as the
   weakest.
2. Knowledge and evidence come second because credence is the currency of the
   next six courses. Updating on evidence is introduced there once, with exact
   fractions, and used without re-derivation in Science, Induction and
   Causation, in Decision and Rationality and in every paradox of probability
   at the end.
3. Decision precedes games, and both precede ethics and justice, because
   expected utility, equilibrium and the n-player dilemma are the instruments
   with which the ethical theories are compared rather than merely described.
   Utilitarianism is an aggregation rule; Kant's test is an outcome at
   universal adoption; the social contract is a game.
4. Metaphysics, mind and language come late because they need modal logic and
   first-order models, which are introduced where they are first used and
   nowhere earlier. Paradoxes come last because a paradox is where all of these
   tools are needed at once, and because by then the reader has met most of
   them in passing and can be asked to classify the exit.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Knowledge and
> Evidence uses the validity and consistency tests of Arguments and Validity;
> Decision and Rationality uses the credences of Knowledge and Evidence; Games
> and the Social Contract uses expected utility; Ethics and the Arithmetic of
> Welfare uses decision matrices, the n-player dilemma and the causal models of
> Science, Induction and Causation; Identity, Modality and Freedom introduces
> modal logic and Mind, Language and Meaning builds on it; Paradoxes and Their
> Exits uses all of it.

**footer_lead**:

> <strong>Educational course material.</strong> Every verdict on this path is
> computed in your browser from what the lesson states: a truth table is built
> by evaluating the formula under every assignment, a posterior is a ratio of
> exact fractions, an equilibrium is found by checking every cell, a winner by
> counting every ballot. Nothing is rounded except where a lesson says so. What
> the labs cannot do is tell you whether a premise is true, whether a case has
> been described fairly, or whether a payoff is the right number &mdash; and
> those are the questions the arguments turn on.

---

## §B The ten courses

Course slugs are global URL segments; none below collides with the 54 existing
course slugs. Release-contract check ids use the prefix `phil`, so
`phil-course10-lesson-` leaves 51 characters for a lesson slug; every slug here
is under 48. Levels use the library's vocabulary.

| n | slug | package | title | level | lessons |
| --- | --- | --- | --- | --- | --- |
| 1 | `arguments-and-validity` | `c1_arguments` | Arguments and Validity | Beginner | 12 |
| 2 | `knowledge-and-evidence` | `c2_knowledge` | Knowledge and Evidence | Beginner → Intermediate | 12 |
| 3 | `science-induction-and-causation` | `c3_science` | Science, Induction and Causation | Intermediate | 10 |
| 4 | `decision-and-rationality` | `c4_decision` | Decision and Rationality | Intermediate | 10 |
| 5 | `games-and-the-social-contract` | `c5_games` | Games and the Social Contract | Intermediate | 11 |
| 6 | `ethics-and-welfare` | `c6_ethics` | Ethics and the Arithmetic of Welfare | Intermediate → Advanced | 12 |
| 7 | `justice-and-collective-choice` | `c7_justice` | Justice and Collective Choice | Advanced | 10 |
| 8 | `identity-modality-and-freedom` | `c8_metaphysics` | Identity, Modality and Freedom | Advanced | 12 |
| 9 | `mind-language-and-meaning` | `c9_mind_language` | Mind, Language and Meaning | Advanced | 10 |
| 10 | `paradoxes-and-their-exits` | `c10_paradoxes` | Paradoxes and Their Exits | Advanced | 9 |

Total: 108 lessons, 10 course homes, 1 path page = 119 pages.

**1. Arguments and Validity** (Beginner; assumes nothing). What an argument is
and what it is for a conclusion to follow. Premises and conclusions in standard
form; validity against soundness; the connectives and the conditional by truth
table; validity as the absence of a counterexample row; equivalence and De
Morgan; consistency of a set of beliefs and the smallest subset that cannot all
be true; categorical statements, the square of opposition and syllogisms tested
on Venn regions, with existential import made a switch; quantifiers and their
order over a finite universe; the formal fallacies and the counterexample
method. Everything later is an application of this course.

**2. Knowledge and Evidence** (Beginner → Intermediate; assumes Arguments and
Validity). Knowledge analysed and the analysis tested against cases: the
tripartite account, Gettier, reliabilism and the clairvoyant; skepticism as a
valid argument and Moore's shift; the regress of justification as an
inconsistent set with four exits. Then credence: degrees of belief and the
Dutch book, conditional credence and base rates, updating on evidence,
testimony and independent witnesses, the reference-class problem, and the
lottery and preface paradoxes where belief and credence come apart.

**3. Science, Induction and Causation** (Intermediate; assumes Knowledge and
Evidence). Induction as updating under a prior and Hume's problem as the
absence of one; grue; confirmation as a Bayes factor; falsification as a
likelihood of zero; the ravens; the Duhem–Quine problem as a minimal
inconsistent subset; Mill's methods as a search over cases; correlation,
confounding and Simpson's paradox; causation as a counterfactual in a Boolean
structural model, with preemption and overdetermination computed rather than
described.

**4. Decision and Rationality** (Intermediate; assumes Knowledge and Evidence).
Preference and transitivity, with the money pump; the decision matrix;
dominance; the rules for ignorance (maximin, maximax, minimax regret); expected
value and expected utility; risk aversion and the value of information; the
Allais paradox; Ellsberg and ambiguity; Pascal's wager with the threshold
computed; Newcomb's problem with the predictor's accuracy as a dial; the St
Petersburg game as a partial sum with a bankroll cap.

**5. Games and the Social Contract** (Intermediate; assumes Decision and
Rationality). Strategic form and best responses; the prisoner's dilemma; Nash
equilibrium in pure and mixed strategies; coordination, convention and the stag
hunt; repeated games, reciprocity and the shadow of the future; Hume's farmers
and convention as repeated interaction; Hobbes' state of nature as a game whose
payoffs a sovereign changes; the tragedy of the commons, public goods and
free-riding as n-player games; the evolution of cooperation by exact replicator
steps.

**6. Ethics and the Arithmetic of Welfare** (Intermediate → Advanced; assumes
Decision and Rationality, Games and the Social Contract, Science, Induction and
Causation). Is and ought as a validity question; defining "good" against cases;
utilitarian aggregation, total against average and the repugnant conclusion;
priority, equality and levelling down; the trolley problem as a decision matrix
with a side constraint; Kant's universalisability as an n-player outcome; double
effect as a path in a causal model; doing, allowing and omissions as causes;
moral dilemmas as deontic inconsistency; virtue ethics through the structure of
the function argument; slippery slopes as sorites.

**7. Justice and Collective Choice** (Advanced; assumes Ethics and the
Arithmetic of Welfare). The original position as maximin against Laplace; the
difference principle as leximin; entitlement and patterns measured by the Gini
coefficient; fairness statistics and disparate rates; then social choice:
majority rule and the Condorcet paradox, plurality against Borda, independence
and Arrow's theorem on a profile, strategic voting, the discursive dilemma, and
the Condorcet jury theorem with the paradox of the pivotal voter.

**8. Identity, Modality and Freedom** (Advanced; assumes Arguments and Validity
and Science, Induction and Causation). Modal logic by possible-worlds models:
necessity, frames and the axioms they validate, modal fallacies and the sea
battle, the ontological argument in S5, Leibniz's law and the masked man. Then
identity over time: the ship of Theseus as a sorites, psychological continuity
as the ancestral of connectedness, fission as an inconsistent triad. Then
freedom: compatibility as consistency, the consequence argument as the K axiom,
Frankfurt cases in a causal model; and the problem of evil as an inconsistent
set.

**9. Mind, Language and Meaning** (Advanced; assumes Identity, Modality and
Freedom). Mind, only where it is checkable: the conceivability argument in a
Kripke model, behaviourism and the Turing test as a Bayes factor of one,
functionalism as the same function in different circuits, the Chinese room as
a lookup table whose size is counted, the knowledge argument formalised. Then
language: compositional truth conditions in a finite model, names and identity
statements, Russell's descriptions and the present King of France, scope
ambiguity, and vagueness.

**10. Paradoxes and Their Exits** (Advanced; assumes everything before it).
What a paradox is and the three exits; the barber; the liar; Zeno's dichotomy
and Achilles; Thomson's lamp; the two envelopes; Sleeping Beauty; Monty Hall;
Moore's paradox. Each lesson ends by asking the reader to name the exit, and
the course home says which paradoxes were met earlier (the sorites, the
lottery, Newcomb, Simpson, the ravens, grue, Gettier, Theseus, Condorcet) and
where.

---

## §C Every lesson

Format of each entry:

- **slug** — Title — *module*
- **Do:** the observable objective (what the reader can do at the end; the
  `standard` field measures it).
- **Lab:** key / mode; the presets by id with their instance; the shipped
  values of redraw-only controls; which tiles each preset must pin.
- **Misconception:** the one wrong model the lesson must name in `mistakes`.
- **Worked:** the single worked example, in one line.

Preset ids are suggestions an author may rename; the INSTANCES are not optional.
Every preset pins at least one tile; "pin" names the tiles that say why the
preset exists (rule 4 of `scripts/mathpath/AGENTS.md`). Expected strings are
read off the built page with `node scripts/labcheck.js --observe`, never
predicted — the formats in §D tell you what shape to expect.

Cross-references in prose are by TITLE, in curly quotes for lessons
(“Validity by Truth Table”) and plain for courses (Knowledge and Evidence).
Never a number.

### Course 1 — Arguments and Validity (`arguments-and-validity`, 12)

Modules: *What an argument is* (1–2), *Propositional logic* (3–7), *Categorical
logic* (8–10), *Quantifiers and fallacies* (11–12).

1. **premises-conclusions-and-standard-form** — Premises, Conclusions and Standard Form — *What an argument is*
   - Do: rewrite a passage as numbered premises and one conclusion, mark the sentences that do no work, and say which sentence the others are offered in support of.
   - Lab: `argkit`/`validity`. Presets: `bare` ({p, q} ⊢ p), `leap` ({p} ⊢ q), `padding` ({p, q, r} ⊢ p). No connectives in any preset — the point is the ROWS: a case is an assignment of true/false to the simple sentences, and the table lists every case. Shipped `show=all`. Pin `vaVerdict`, `vaCounter`.
   - Misconception: the conclusion is whatever sentence comes last.
   - Worked: "The streets are wet. Streets here are only wet after rain. So it rained." → P1, P2, C; `leap` shows the one row (p = T, q = F) where a premise can be true and the conclusion false.

2. **validity-and-soundness** — Validity and Soundness — *What an argument is*
   - Do: classify an argument as valid or invalid by looking for a case, and separately as sound or unsound by asking whether the premises are true; explain why the lab can do the first and not the second.
   - Lab: `argkit`/`validity`. Presets: `same` ({p} ⊢ p: valid, sound iff p), `other` ({q} ⊢ p: invalid), `both` ({p, q} ⊢ q). Pin `vaVerdict`, `vaRows`.
   - Misconception: a valid argument has a true conclusion.
   - Worked: "All whales are fish; all fish fly; so whales fly" — valid, unsound; the lab checks the first word and the world settles the second.

3. **truth-values-and-the-connectives** — Truth Values and the Connectives — *Propositional logic*
   - Do: build the truth table of a formula in ¬, ∧, ∨ and read off the row where inclusive and exclusive "or" differ.
   - Lab: `truth_table` (existing). cfg `formulas: ["p & q", "p | q", "~p", "p ^ q", "~p & ~q"]`, `compare_with: "p ^ q"`, `mode: "one"`.
   - Misconception: "or" is exclusive.
   - Worked: "You may have soup or salad" — four rows; the T,T row is where the menu means ⊕ and logic means ∨.

4. **the-conditional** — The Conditional — *Propositional logic*
   - Do: fill the four rows of `p → q`, translate "only if", "unless", "necessary" and "sufficient", and show `p → q` and `q → p` differ in exactly one row.
   - Lab: `truth_table`, `mode: "two"`, `formulas: ["p -> q", "q -> p", "~p | q", "~q -> ~p", "~p -> ~q"]`, `compare_with: "~p | q"`.
   - Misconception: a conditional with a false antecedent has no truth value, or is false.
   - Worked: "If it rains, the match is off" — the match is off and it did not rain; the promise is kept, the row is T.

5. **validity-by-truth-table** — Validity by Truth Table — *Propositional logic*
   - Do: lay premises and conclusion in one table, find or rule out the counterexample row, and name modus ponens, modus tollens, affirming the consequent and denying the antecedent on sight.
   - Lab: `argkit`/`validity`. Presets: `mp`, `mt`, `ac`, `da` (the four forms on p, q). Pin `vaVerdict`, `vaForm`, `vaCounter`.
   - Misconception: a row where the premises are false and the conclusion false is a counterexample.
   - Worked: "If God exists, life has meaning; life has meaning; so God exists" — affirming the consequent; the row p = F, q = T has true premises and a false conclusion.

6. **equivalence-de-morgan-and-contraposition** — Equivalence, De Morgan and Contraposition — *Propositional logic*
   - Do: decide whether two formulas are equivalent by comparing columns, apply De Morgan to "not both" and "neither", and give the contrapositive of a conditional without producing its converse or inverse.
   - Lab: `truth_table`, `mode: "two"`, `formulas: ["~(p & q)", "~p | ~q", "~p & ~q", "~(p | q)", "p -> q", "~q -> ~p", "q -> p"]`, `compare_with: "~p | ~q"`.
   - Misconception: ¬(p ∧ q) is ¬p ∧ ¬q.
   - Worked: "It is not the case that she is both rich and famous" → ¬(r ∧ f) ≡ ¬r ∨ ¬f; the two columns agree in all four rows.

7. **consistency-and-belief-sets** — Consistency and Belief Sets — *Propositional logic*
   - Do: decide whether a set of sentences can all be true, list a model if so, and if not identify the smallest subset that cannot all be true — then say what "you must give something up" does and does not tell you about which.
   - Lab: `argkit`/`consistency`. Presets: `triad` ({p → q, p, ¬q}), `four` ({p → q, q → r, p, ¬r}), `fine` ({p ∨ q, ¬p, q → r}). Shipped `coDrop = keep all`. Pin `coVerdict`, `coMis`, `coModels`.
   - Misconception: an inconsistent set contains a sentence you can identify as the false one.
   - Worked: {p → q, q → r, p, ¬r} has no model; the minimal inconsistent subset is all four, so any one of them may be dropped and the lab shows the model that appears.

8. **categorical-statements-and-immediate-inference** — Categorical Statements and Immediate Inference — *Categorical logic*
   - Do: write All/No/Some/Some-not statements as claims about regions of a two-circle Venn diagram, and test conversion, obversion and contraposition by asking whether the conclusion's regions are forced.
   - Lab: `argkit`/`syllogism` with ONE premise. Presets: `convert-e` (No S are P ⊢ No P are S: valid), `convert-a` (All S are P ⊢ All P are S: invalid), `contrapose-a` (All S are P ⊢ All non-P are non-S: valid), `convert-o` (Some S are not P ⊢ Some P are not S: invalid). Shipped `import = boolean`. Pin `syVerdict`, `syCounter`.
   - Misconception: "All S are P" converts to "All P are S".
   - Worked: "All squares are rectangles" → the region squares-not-rectangles is empty; "All rectangles are squares" needs rectangles-not-squares empty, which nothing forces — the counterexample region is drawn.

9. **the-square-of-opposition-and-existential-import** — The Square of Opposition and Existential Import — *Categorical logic*
   - Do: state which pairs on the square are contradictories, contraries and subalterns under the Boolean reading and under the Aristotelian one, and say which inferences appear only when every term is assumed non-empty.
   - Lab: `argkit`/`syllogism`. Presets: `subalt` (All S are P ⊢ Some S are P: invalid on the Boolean reading, valid on the Aristotelian), `contradictory` (All S are P ⊢ Some S are not P: invalid on both — the two can never agree, which the counterexample pattern shows), `converse-accidens` (All S are P ⊢ Some P are S: valid only with import), `unicorns` (All unicorns are white ⊢ Some unicorns are white). Shipped `import = boolean`; the lesson instructs switching the reading. Pin `syVerdict` and `syCounter` under the shipped reading on every preset; the Aristotelian verdict is read in the status banner and cannot be pinned (rule 6).
   - Misconception: "All S are P" implies "Some S are P".
   - Worked: "All unicorns are white" is true on the Boolean reading because there are no unicorns in the S-not-P region or any other; subalternation fails until a unicorn is assumed.

10. **syllogisms-tested-by-venn-regions** — Syllogisms Tested by Venn Regions — *Categorical logic*
    - Do: test a three-term syllogism by enumerating the region patterns the premises allow and checking the conclusion in each; name Barbara, Celarent, Darii and Ferio; recognise the undistributed middle.
    - Lab: `argkit`/`syllogism`. Presets: `barbara` (All M are P; All S are M ⊢ All S are P), `darii`, `ferio`, `undistributed` (All P are M; All S are M ⊢ All S are P), `illicit-major` (All M are P; No S are M ⊢ No S are P). Pin `syVerdict`, `syForm`, `syModels`.
    - Misconception: a syllogism with true premises and a true conclusion is valid.
    - Worked: "All cats are mammals; all dogs are mammals; so all dogs are cats" — AAA-2; the counterexample pattern has dogs outside cats, inside mammals.

11. **quantifiers-and-their-order** — Quantifiers and Their Order — *Quantifiers and fallacies*
    - Do: read ∀ and ∃ over a finite universe, distinguish ∀x∃y from ∃y∀x on a grid, and spot the quantifier shift in "everything has a cause, so something causes everything".
    - Lab: `quantifier` (existing), `preset: "succ"`, `size: 4`.
    - Misconception: ∀x∃y P(x, y) implies ∃y∀x P(x, y).
    - Worked: on "y = x + 1" every x has a successor, but no single y is everyone's successor — the full-row/full-column distinction, and the cosmological argument's shift named as exactly this.

12. **fallacies-and-the-counterexample-method** — Fallacies and the Counterexample Method — *Quantifiers and fallacies*
    - Do: refute an invalid form by producing an argument of the same form with true premises and a false conclusion; recognise hypothetical syllogism, disjunctive syllogism and constructive dilemma as valid and affirming a disjunct as not.
    - Lab: `argkit`/`validity`. Presets: `hs`, `ds`, `cd`, `affirm-disjunct` (p ∨ q, p ⊢ ¬q), `da`. Pin `vaVerdict`, `vaForm`.
    - Misconception: an argument with a false conclusion must be invalid (and one with a true conclusion valid).
    - Worked: "Either the butler or the maid did it; the butler did it; so the maid did not" — affirming a disjunct; the row p = T, q = T is the counterexample, and the same form with "it is raining or it is Tuesday" makes the fallacy audible.

### Course 2 — Knowledge and Evidence (`knowledge-and-evidence`, 12)

Modules: *Analysing knowledge* (1–3), *Justification* (4–5), *Credence* (6–9),
*Evidence and belief* (10–12).

1. **belief-truth-and-justification** — Belief, Truth and Justification — *Analysing knowledge*
   - Do: state the tripartite analysis as three individually necessary and jointly sufficient conditions, and test a proposed definition against a case table by finding the row where definition and verdict disagree.
   - Lab: `argkit`/`analysis`. Preset `jtb`: conditions J, T, B; cases: ordinary perception (1,1,1 → knows), lucky guess (0,1,1 → no), confident error (1,0,1 → no), unbelieved truth (1,1,0 → no); definition `J & T & B`. Shipped `search = off`. Pin `anAgree`, `anVerdict`.
   - Misconception: a definition is a list of typical features rather than conditions each of which must hold.
   - Worked: the four-case table; `J & T & B` agrees 4 of 4, and dropping any one condition produces a disagreeing row the lab names.

2. **gettier-cases-and-the-fourth-condition** — Gettier Cases and the Fourth Condition — *Analysing knowledge*
   - Do: construct a case where J, T and B hold and the verdict is "does not know", classify the failure as "too broad", propose a fourth condition and find the case that breaks it.
   - Lab: `argkit`/`analysis`. Presets: `gettier` (J, T, B; cases incl. Smith's coins and the stopped clock, both 1,1,1 → no), `lemma` (J, T, B, L = "relies on a false lemma"; cases incl. the coins (L = 1) and fake barns (L = 0, verdict no); definition `J & T & B & ~L`). Shipped `search = pairs` on `lemma`. Pin `anFail`, `anVerdict`, `anCands`.
   - Misconception: Gettier shows knowledge is impossible or that justification is irrelevant.
   - Worked: Smith's coins: J = 1, T = 1, B = 1, verdict no — the definition says "knows", so it is too broad; adding `~L` fixes that row and fake barns (no false lemma, still no knowledge) breaks the fix.

3. **reliabilism-and-the-clairvoyant** — Reliabilism and the Clairvoyant — *Analysing knowledge*
   - Do: test "justified iff produced by a reliable process" against ordinary perception, Norman the clairvoyant and the brain in a vat, and say which direction each failure runs.
   - Lab: `argkit`/`analysis`. Preset `norman`: conditions R (reliable process), E (has accessible evidence), T, B; cases: perception (1,1,1,1 → yes), Norman (1,0,1,1 → no), envatted twin (0,1,0,1 → verdict as the lesson argues), lucky testimony; definitions `R & T & B` and `E & T & B` as two presets `reliabilist`, `evidentialist`. Shipped `search = pairs`. Pin `anFail`, `anCands`.
   - Misconception: "reliable" means "right this time".
   - Worked: Norman: reliable, no evidence, believes truly; reliabilism says justified, the verdict says not — too broad, and the search finds `R & E` fits every listed case.

4. **skepticism-and-the-closure-argument** — Skepticism and the Closure Argument — *Justification*
   - Do: formalise the brain-in-a-vat argument, show it is modus tollens, formalise Moore's reply as modus ponens on the same conditional, and state what choosing between them requires that validity cannot supply.
   - Lab: `argkit`/`validity`. Presets: `closure` ({h → b, ¬b} ⊢ ¬h, where h = "I know I have hands", b = "I know I am not a brain in a vat"), `moore` ({h, h → b} ⊢ b), `deny-closure` ({¬b} ⊢ ¬h: invalid without the conditional). Pin `vaVerdict`, `vaForm`.
   - Misconception: a valid argument compels you to accept its conclusion.
   - Worked: the skeptic and Moore share the premise h → b and disagree about which of ¬b and h is more certain; the lab says both arguments are valid and nothing more.

5. **the-regress-of-justification** — The Regress of Justification — *Justification*
   - Do: write Agrippa's trilemma as a set of claims that cannot all be true, find that its minimal inconsistent subset is the whole set, and name the position each single deletion yields (foundationalism, coherentism, infinitism, skepticism).
   - Lab: `argkit`/`consistency`. Preset `agrippa`: {j, j → n, n → (c ∨ f ∨ i), ¬c, ¬f, ¬i} with j = some belief is justified, n = every justified belief needs a justified supporter, c/f/i = circles/finite unsupported foundations/infinite chains are acceptable. Also `foundationalist` (drop ¬f). Pin `coVerdict`, `coMis`, `coWitness`.
   - Misconception: "circular" and "infinite" are the same complaint.
   - Worked: the six sentences have no model; the MIS is all six; dropping ¬f gives the model where a foundation stops the chain — foundationalism as a line of a truth table.

6. **credence-and-the-dutch-book** — Credence and the Dutch Book — *Credence*
   - Do: assign degrees of belief to the events of a small outcome space, check them against the probability rules, and construct the set of bets that loses for certain when they break additivity.
   - Lab: `choicekit`/`credence`, kind `space`. Presets: `coin` (outcomes H, T at 1/2 each; events "heads", "tails"; typed credences 3/5 and 3/5), `die` (six outcomes; events "even", "at least five", "even or at least five"; typed credences violating additivity), `coherent` (typed credences equal to the probabilities). Shipped `threshold = 1`. Pin `crBook`.
   - Misconception: credence 1/2 means "I have no idea".
   - Worked: c(heads) = 3/5 and c(tails) = 3/5 → sell both bets at those prices and lose 1/5 per unit whatever happens.

7. **conditional-credence-and-base-rates** — Conditional Credence and Base Rates — *Credence*
   - Do: compute P(D | +) from a population table of a million people, and explain why a 99%-sensitive test on a 1-in-1000 condition leaves most positives false.
   - Lab: `bayes` (existing). cfg `prev: 1000, sens: 99, fpr: 5`.
   - Misconception: P(+ | D) is P(D | +).
   - Worked: 1,000 have it, 990 test positive; 999,000 do not, 49,950 test positive; P(D | +) = 990/50,940 = 99/5,094, under 2%.

8. **updating-on-evidence** — Updating on Evidence — *Credence*
   - Do: update a prior on an observation using likelihoods, read the Bayes factor as the weight of the evidence, and update twice in sequence.
   - Lab: `choicekit`/`update`. Presets: `urns` (urn 1: 3 red 1 blue; urn 2: 1 red 3 blue; prior 1/2; data "red"), `two-draws` (data "red red"), `bias` (hypotheses coin fair / two-headed; data "heads heads heads"). Shipped `upHyp = first`. Pin `upPost`, `upBF`.
   - Misconception: evidence that fits a hypothesis proves it.
   - Worked: one red draw → P(urn 1) = 3/4, Bayes factor 3; a second red → 9/10, Bayes factor 9.

9. **testimony-and-independent-witnesses** — Testimony and Independent Witnesses — *Credence*
   - Do: compute what a witness of stated reliability does to a prior, show two independent witnesses multiply Bayes factors, and state Hume's argument about miracles as a comparison of two likelihoods.
   - Lab: `choicekit`/`update`. Presets: `witness` (prior 1/100; reliability 9/10), `two-witnesses` (data "yes yes"), `miracle` (prior 1/1,000,000; reliability 999/1000). Pin `upPost`, `upBF`, `upConf`.
   - Misconception: a 90%-reliable witness makes the claim 90% likely.
   - Worked: prior 1/100, reliability 9/10 → posterior 9/108 = 1/12; a second independent witness → 81/180 = 9/20.

10. **reference-classes-and-statistical-evidence** — Reference Classes and Statistical Evidence — *Evidence and belief*
    - Do: compute the rate of an outcome in two reference classes and in their pooled union, and state why "the probability for this individual" depends on the class chosen.
    - Lab: `choicekit`/`simpson`. Presets: `smoker-cyclist` (two classes, one factor), `kidney` (the kidney-stone tables, previewing Simpson). Shipped `siWeight = pooled`. Pin `siPooled`, `siGroup1`, `siGroup2`.
    - Misconception: the pooled rate is "the" probability.
    - Worked: a 60-year-old smoker who cycles daily belongs to a class with rate 1/5 and one with rate 1/20; the pooled rate is neither, and the lab prints all three.

11. **the-lottery-paradox** — The Lottery Paradox — *Evidence and belief*
    - Do: apply a belief threshold to "ticket i loses" for every ticket, show every one is accepted, and show the accepted set has no outcome in common.
    - Lab: `choicekit`/`credence`, kind `lottery`. Presets: `hundred` (100 tickets, threshold 99/100), `thousand` (1000, 999/1000), `strict` (100 tickets, threshold 999/1000: nothing accepted). Pin `crAccepted`, `crConsistent`, `crPAll`.
    - Misconception: rational belief is closed under conjunction.
    - Worked: 100 tickets, threshold 99/100: all 100 "loses" claims accepted, their conjunction has probability 0, and no ticket survives.

12. **the-preface-paradox** — The Preface Paradox — *Evidence and belief*
    - Do: show that many independent well-supported claims have a conjunction of low probability while remaining jointly consistent, and contrast this with the lottery.
    - Lab: `choicekit`/`credence`, kind `independent`. Presets: `book` (100 claims at 99/100, threshold 95/100), `short` (10 claims at 9/10), `certain` (100 claims at 1). Pin `crPAll`, `crConsistent`, `crAccepted`.
    - Misconception: an author who believes each sentence must believe the book has no errors.
    - Worked: 100 independent claims at 99/100 each: all accepted, all could be true, and P(all true) = (99/100)¹⁰⁰, about 0.37 — the lab prints the exact fraction.

### Course 3 — Science, Induction and Causation (`science-induction-and-causation`, 10)

Modules: *Induction* (1–2), *Confirmation* (3–6), *Causation* (7–10).

1. **enumerative-induction-and-humes-problem** — Enumerative Induction and Hume's Problem — *Induction*
   - Do: show that "the sun has risen n times, so it will rise tomorrow" is invalid by truth table and gains force only under a prior over hypotheses; compute the predictive probability under a uniform prior and under a prior that favours a change.
   - Lab: `choicekit`/`update`. Presets: `succession` (hypotheses: bias 0, 1/4, 1/2, 3/4, 1 with uniform prior; data: ten successes), `skeptic` (same hypotheses, prior weighted towards 0). Pin `upPred`, `upPost`.
   - Misconception: a large sample makes induction deductively valid.
   - Worked: ten sunrises under the five-hypothesis uniform prior give a predictive probability the lab prints as an exact fraction just under 1; the same data under the skeptic's prior give a smaller one — the data did not change, the prior did.

2. **grue-and-the-new-riddle** — Grue and the New Riddle — *Induction*
   - Do: define "grue", show two hypotheses that agree on every observation before t have a Bayes factor of exactly 1, and conclude that projectibility is a fact about priors, not data.
   - Lab: `choicekit`/`update`. Presets: `grue` (H-green, H-grue; identical likelihood rows; data: 100 green emeralds), `tell` (a likelihood that differs on one outcome). Pin `upBF`, `upConf`.
   - Misconception: more green emeralds favour "green" over "grue".
   - Worked: 100 green emeralds; Bayes factor 1; posterior ratio equals prior ratio to the digit.

3. **confirmation-and-the-weight-of-evidence** — Confirmation and the Weight of Evidence — *Confirmation*
   - Do: define confirmation as raising probability, measure weight by the Bayes factor, and show surprising evidence confirms more than expected evidence.
   - Lab: `choicekit`/`update`. Presets: `surprising` (P(E | ¬H) = 1/10), `expected` (P(E | ¬H) = 9/10), `neutral` (P(E | H) = P(E | ¬H)). Pin `upBF`, `upConf`, `upPost`.
   - Misconception: evidence consistent with H confirms H.
   - Worked: the same prior 1/2 and P(E | H) = 1; Bayes factor 10 against 10/9.

4. **falsification-and-what-a-theory-forbids** — Falsification and What a Theory Forbids — *Confirmation*
   - Do: identify the outcomes a hypothesis assigns likelihood 0 to, show one such observation drives its posterior to 0 whatever the prior, and show a hypothesis that forbids nothing never changes its probability.
   - Lab: `choicekit`/`update`. Presets: `popper` (H forbids outcome 3; data "o3"), `unfalsifiable` (a hypothesis with no zero likelihood and uniform rows), `risky` (H forbids two of three outcomes; data "o1"). Pin `upConf`, `upPost`.
   - Misconception: a theory confirmed many times is proven.
   - Worked: P(o3 | H) = 0; one observation of o3 → P(H | data) = 0 from a prior of 99/100.

5. **the-raven-paradox** — The Raven Paradox — *Confirmation*
   - Do: state Nicod's condition and the equivalence condition, derive that a white shoe confirms "all ravens are black", and compute how little by sampling from the non-black objects.
   - Lab: `choicekit`/`update`. Presets: `nonblack` (sample a non-black object; H: raven 0, non-raven 1; ¬H: 1/901, 900/901; data "non-raven"), `ravens` (sample a raven; H: black 1; ¬H: black 9/10; data "black"). Pin `upBF`.
   - Misconception: confirmation is all-or-nothing.
   - Worked: a white shoe gives Bayes factor 901/900; a black raven gives 10/9 — both confirm, and the asymmetry is in the sampling.

6. **the-duhem-quine-problem** — The Duhem–Quine Problem — *Confirmation*
   - Do: write a failed prediction as an inconsistent set {H, A₁, A₂, bridge, ¬E}, show its minimal inconsistent subset is the whole set, and conclude that the observation refutes the conjunction and nothing smaller.
   - Lab: `argkit`/`consistency`. Presets: `duhem` ({h, a, b, (h ∧ a ∧ b) → e, ¬e}), `neptune` (drop a: the auxiliary "no unseen planet"). Pin `coVerdict`, `coMis`.
   - Misconception: a failed test refutes the theory.
   - Worked: Uranus's orbit against Newton: dropping "there is no eighth planet" restores consistency; so did dropping Newton, and the arithmetic cannot say which.

7. **mills-methods-and-the-common-factor** — Mill's Methods and the Common Factor — *Causation*
   - Do: apply the methods of agreement and difference to a case table, find the factor present in every positive case and absent in every negative one, and say why that factor is a candidate and not yet a cause.
   - Lab: `argkit`/`analysis`. Presets: `diners` (five diners, foods A–E, verdict sick/well; definition the suspected food), `two-causes` (a table where no single factor fits and a disjunction of two does). Shipped `search = pairs`. Pin `anCands`, `anVerdict`.
   - Misconception: the factor common to the cases is the cause.
   - Worked: the oysters are in every sick diner's meal and no well diner's; the search returns the single literal and the lesson lists what it did not rule out.

8. **correlation-confounding-and-simpsons-paradox** — Correlation, Confounding and Simpson's Paradox — *Causation*
   - Do: compute success rates within two groups and pooled, show the pooled comparison reverse, and name the confounder.
   - Lab: `choicekit`/`simpson`. Presets: `kidney` (small stones A 81/87 vs B 234/270; large stones A 192/263 vs B 55/80), `no-reversal` (balanced groups), `berkeley` (two departments). Shipped `siWeight = pooled`. Pin `siVerdict`, `siPooled`, `siAdjusted`.
   - Misconception: a higher overall rate means a better treatment.
   - Worked: A wins in both groups; pooled, B has 289/350 against A's 273/350 because A took the harder cases.

9. **counterfactual-causation-and-the-but-for-test** — Counterfactual Causation and the But-For Test — *Causation*
   - Do: write a situation as Boolean structural equations, compute the actual values, and test a variable as a cause by flipping it and recomputing.
   - Lab: `argkit`/`structural`. Presets: `match` (F = S ∧ O; S = 1, O = 1; cause S), `oxygen` (same, cause O), `chain` (A → B → C). Pin `stButFor`, `stKind`, `stActual`.
   - Misconception: a cause is what made the difference "in the circumstances", as opposed to a background condition — the but-for test cannot tell them apart and says so.
   - Worked: striking the match and the presence of oxygen are both but-for causes of the fire; the lab reports both, and the distinction between them is pragmatic.

10. **preemption-and-overdetermination** — Preemption, Overdetermination and Redundant Causes — *Causation*
    - Do: build the two-assassins model, show the but-for test fails for the actual cause, and recover it by holding the preempted path fixed; show two simultaneous rocks fail individually and pass jointly.
    - Lab: `argkit`/`structural`. Presets: `preemption` (SH = ST; BH = BT ∧ ¬SH; shattered = SH ∨ BH; cause ST), `overdetermination` (SH = ST; BH = BT; shattered = SH ∨ BH; cause ST), `trumping`. Pin `stButFor`, `stHP`, `stKind`.
    - Misconception: if the effect would have happened anyway, nothing caused it.
    - Worked: Suzy's throw is not a but-for cause (Billy's rock would have hit); holding "Billy's rock hits" at its actual value 0, flipping Suzy's throw flips the shattering — a cause once something is held fixed.

### Course 4 — Decision and Rationality (`decision-and-rationality`, 10)

Modules: *Preference* (1), *Ignorance* (2–3), *Risk* (4–7), *Puzzles of expected value* (8–10).

1. **preference-transitivity-and-the-money-pump** — Preference, Transitivity and the Money Pump — *Preference*
   - Do: state the completeness and transitivity conditions on preference, build a cyclic preference on the relation grid and read the pair that breaks transitivity, and compute what a cycle costs per lap.
   - Lab: `relation` (existing), `preset: "lt"`, `size: 5`; the lesson has the reader add one pair to make a cycle and read the witness.
   - Misconception: transitivity is a matter of taste.
   - Worked: A ≻ B ≻ C ≻ A with a willingness to pay ε per swap loses 3ε every lap, for ever.

2. **the-decision-matrix-and-dominance** — The Decision Matrix and Dominance — *Ignorance*
   - Do: lay acts against states with payoffs, identify a dominated act, and say why dominance decides nothing when no act dominates.
   - Lab: `choicekit`/`decide`. Presets: `umbrella` (take: 2, 1; leave: −3, 3; no dominance), `dominated` (a third act worse in every state), `weak` (equal in one state). Shipped `rule = dominance`, `probs` empty. Pin `deChoice`.
   - Misconception: the act with the best possible outcome is the best act.
   - Worked: taking the umbrella is better in rain and worse in sun — no dominance; add "take a coat" at (1, 0) and it is dominated by the umbrella.

3. **maximin-maximax-and-minimax-regret** — Maximin, Maximax and Minimax Regret — *Ignorance*
   - Do: apply the three rules for ignorance to one matrix, build the regret table, and find an instance where maximin and minimax regret disagree.
   - Lab: `choicekit`/`decide`. Presets: `umbrella` (shipped `rule = maximin`), `disagree` (a matrix where maximin and regret pick differently; shipped rule maximin, the regret verdict read by switching). Pin `deChoice`, `deValue`.
   - Misconception: minimax regret is maximin on a different table — it is, but the table is relative and shifting one column changes the answer.
   - Worked: umbrella: maximin picks take (min 1 against −3); regret table take (0, 2), leave (5, 0); minimax regret also take; `disagree` shows them part.

4. **expected-value-and-expected-utility** — Expected Value and Expected Utility — *Risk*
   - Do: compute expected utility from probabilities and a payoff table, find the act it recommends, and compute the indifference probability at which the recommendation flips.
   - Lab: `choicekit`/`decide`. Presets: `umbrella-p` (probs 1/3, 2/3), `bet` (a fair bet against not betting), `lottery-ticket`. Shipped `rule = eu`. Pin `deChoice`, `deValue`, `deFlip`.
   - Misconception: expected value is the value you expect.
   - Worked: EU(take) = 4/3, EU(leave) = 1 at p(rain) = 1/3; the flip is at p = 2/7.

5. **risk-aversion-and-the-value-of-information** — Risk Aversion and the Value of Information — *Risk*
   - Do: show a concave utility makes a sure thing beat a fair gamble, and compute the value of perfect information as expected best minus best expected.
   - Lab: `choicekit`/`decide`. Presets: `insurance` (utilities as the payoff table; the premium that is worth paying), `vpi` (the umbrella with probabilities). Shipped `rule = eu`. Pin `deVpi`, `deChoice`.
   - Misconception: refusing a fair bet is irrational.
   - Worked: umbrella at p(rain) = 1/3: expected best = 8/3, best expected = 4/3, so a perfect forecast is worth 4/3.

6. **the-allais-paradox-and-the-sure-thing-principle** — The Allais Paradox and the Sure-Thing Principle — *Risk*
   - Do: state the two Allais choices, show the EU difference in each is the same expression, and conclude that the common pattern violates expected utility whatever the utilities.
   - Lab: `choicekit`/`decide`. Presets: `allais-a` (1M sure against 1% 0 / 89% 1M / 10% 5M), `allais-b` (11% 1M against 10% 5M; both in utilities u(0) = 0, u(1M) = 10, u(5M) = 14). Shipped `rule = eu`. Pin `deValue`, `deChoice`.
   - Misconception: a sure thing is always worth a premium under expected utility.
   - Worked: EU(A) − EU(B) and EU(C) − EU(D) print the same fraction; preferring A and D is choosing both signs of one number.

7. **ambiguity-and-the-ellsberg-urn** — Ambiguity and the Ellsberg Urn — *Risk*
   - Do: set up the Ellsberg urn with the unknown proportion as a probability dial, find the proportion at which the two bets tie, and show the common choice pattern is inconsistent with any single proportion.
   - Lab: `choicekit`/`decide`. Presets: `ellsberg-1` (bet red against bet black; probs 1/3 and p), `ellsberg-2` (red-or-yellow against black-or-yellow), `maximin-view` (rule maximin shipped). Pin `deFlip`, `deChoice`.
   - Misconception: ambiguity aversion is risk aversion.
   - Worked: betting red over black is consistent only with p(black) < 1/3, betting black-or-yellow over red-or-yellow only with p(black) > 1/3.

8. **pascals-wager** — Pascal's Wager — *Puzzles of expected value*
   - Do: lay out the wager as a decision matrix with a finite reward M, compute the threshold M* = c/p at which wagering wins, and state what an infinite payoff would do to every act with positive probability.
   - Lab: `choicekit`/`decide`. Presets: `pascal` (p = 1/1000, cost 1, M = 1000: tie), `pascal-wins` (M = 1001), `many-gods` (three states, two incompatible wagers). Shipped `rule = eu`. Pin `deChoice`, `deValue`.
   - Misconception: a tiny probability can be ignored.
   - Worked: EU(wager) = p·M − c = 1000/1000 − 1 = 0 at M = 1000; one unit more and wagering wins.

9. **newcombs-problem** — Newcomb's Problem — *Puzzles of expected value*
   - Do: compute the evidential expected value of one-boxing and two-boxing from the predictor's accuracy, show two-boxing dominates, and find the accuracy at which evidential reasoning switches.
   - Lab: `choicekit`/`decide`. Presets: `newcomb-90` (accuracy 9/10; shipped `rule = evidential`), `newcomb-coin` (accuracy 1/2), `dominance-view` (shipped rule dominance). Pin `deChoice`, `deValue`.
   - Misconception: the predictor's past accuracy is irrelevant because the boxes are already filled — or is decisive because it is high; the lesson names both and computes the threshold.
   - Worked: one-boxing wins evidentially iff a > 1001/2000; at a = 9/10, EU(one) = 900,000 against EU(two) = 101,000, while two-boxing dominates row by row.

10. **the-st-petersburg-game** — The St Petersburg Game — *Puzzles of expected value*
    - Do: write the game's expected value as a sum whose every term is 1, show the partial sum grows without bound, and compute the finite value once the bank's bankroll is capped.
    - Lab: `choicekit`/`series`, kind `petersburg`. Presets: `uncapped` (n = 20, no cap), `cap-1024` (bankroll 1024), `cap-million` (1,048,576). Pin `srSum`, `srLimit`.
    - Misconception: an infinite expected value means you should pay any price.
    - Worked: twenty terms of 1 sum to 20; with a bankroll of 1024 the whole series sums to 11.

### Course 5 — Games and the Social Contract (`games-and-the-social-contract`, 11)

Modules: *One-shot games* (1–4), *Repeated games* (5–7), *Many players* (8–11).

1. **strategic-form-and-best-responses** — Strategic Form and Best Responses — *One-shot games*
   - Do: read a bimatrix, mark each player's best response to each strategy of the other, and find where the marks meet.
   - Lab: `choicekit`/`game`. Presets: `coordination` (two pure equilibria), `unique` (one), `none-pure` (matching pennies). Shipped `view = best responses`. Pin `gaPure`.
   - Misconception: a player should pick the row with the biggest number anywhere in it.
   - Worked: in the coordination game both diagonal cells are mutual best responses; the off-diagonal cells are not.

2. **the-prisoners-dilemma** — The Prisoner's Dilemma — *One-shot games*
   - Do: show defection strictly dominates, locate the unique equilibrium, and show it is Pareto-dominated by mutual cooperation.
   - Lab: `choicekit`/`game`. Presets: `pd` (3,3 / 0,5 / 5,0 / 1,1), `pd-mild` (smaller temptation), `not-pd` (payoffs where cooperation is an equilibrium). Shipped `view = dominance`. Pin `gaDom`, `gaPure`, `gaPareto`.
   - Misconception: the dilemma arises from distrust and vanishes between people who trust each other.
   - Worked: D dominates C for both; (D, D) is the only equilibrium; (C, C) gives each 3 against 1.

3. **nash-equilibrium-in-pure-and-mixed-strategies** — Nash Equilibrium in Pure and Mixed Strategies — *One-shot games*
   - Do: define equilibrium as mutual best response, find a game with no pure equilibrium, and compute the mixed equilibrium of a 2×2 game exactly.
   - Lab: `choicekit`/`game`. Presets: `pennies` (mixed 1/2, 1/2), `chicken` (two pure, mixed with column swerving 9/10), `stag` (two pure, mixed 3/4). Pin `gaPure`, `gaMixed`.
   - Misconception: equilibrium means the best outcome for the group.
   - Worked: chicken: swerve/straight payoffs (0,0 / −1,1 / 1,−1 / −10,−10); the column player swerves with probability 9/10 at the mixed equilibrium.

4. **coordination-conventions-and-the-stag-hunt** — Coordination, Conventions and the Stag Hunt — *One-shot games*
   - Do: distinguish the payoff-dominant from the risk-dominant equilibrium in the stag hunt, define a convention as a self-sustaining equilibrium of a coordination game, and compute the belief threshold at which hunting stag is best.
   - Lab: `choicekit`/`game`. Presets: `stag` (4,4 / 0,3 / 3,0 / 3,3), `driving` (left/left, right/right), `sexes`. Pin `gaPure`, `gaMixed`, `gaPareto`.
   - Misconception: a convention is an agreement.
   - Worked: stag is best only if the other hunts stag with probability at least 3/4 — the mixed equilibrium's number read as a threshold.

5. **repeated-games-and-reciprocity** — Repeated Games and Reciprocity — *Repeated games*
   - Do: play the prisoner's dilemma for a stated number of rounds between two named strategies, read the round-by-round record, and read the round-robin tournament's winner.
   - Lab: `choicekit`/`iterated`. Presets: `tft-alld` (TFT against ALLD, 10 rounds), `tft-tft`, `grim-pavlov`. Shipped `a = TFT`, `b = ALLD`, `rounds = 10`. Pin `itScoreA`, `itScoreB`, `itWinner`.
   - Misconception: the strategy that beats every opponent wins the tournament.
   - Worked: TFT against ALLD loses the first round and ties the rest: 9 against 14 over ten rounds, and TFT still wins the tournament.

6. **the-shadow-of-the-future** — The Shadow of the Future — *Repeated games*
   - Do: compute the discount factor above which cooperation is sustainable against GRIM and against TFT, and state why a known last round unravels it.
   - Lab: `choicekit`/`iterated`. Presets: `standard` (3, 0, 5, 1; δ = 9/10), `low-delta` (δ = 1/4), `high-temptation` (T = 10). Pin `itThresh`.
   - Misconception: cooperation needs a long game; it needs an uncertain end.
   - Worked: with (R, S, T, P) = (3, 0, 5, 1), GRIM sustains cooperation for δ ≥ 1/2 and TFT for δ ≥ 2/3; δ = 9/10 clears both.

7. **humes-farmers-and-convention** — Hume's Farmers and Convention — *Repeated games*
   - Do: model the two farmers' harvests as a one-shot and as a repeated exchange, and show when the second farmer's help becomes rational.
   - Lab: `choicekit`/`iterated`. Presets: `farmers-once` (1 round), `farmers-season` (12 rounds, TFT against TFT), `farmers-suspicious` (STFT against TFT). Pin `itScoreA`, `itScoreB`.
   - Misconception: Hume's farmers fail because they are selfish; they fail because the game is played once.
   - Worked: one round: nobody helps; twelve rounds: TFT against TFT cooperates throughout and each collects 36.

8. **hobbes-and-the-state-of-nature** — Hobbes and the State of Nature — *Many players*
   - Do: write the state of nature as a two-player game, show the equilibrium under anarchy, and show a sovereign's penalty for aggression moves the equilibrium.
   - Lab: `choicekit`/`game`. Presets: `anarchy` (attack dominates), `sovereign` (penalty 4 on attacking), `assurance` (the state of nature as a stag hunt). Pin `gaPure`, `gaDom`.
   - Misconception: Hobbes thought people are wicked; the model needs only that they are rational and unsure.
   - Worked: under anarchy attack dominates; subtract a penalty of 4 from every attack payoff and (peace, peace) becomes the equilibrium.

9. **the-tragedy-of-the-commons** — The Tragedy of the Commons — *Many players*
   - Do: write each herder's payoff as a function of how many others add an animal, find the symmetric equilibrium and the social optimum, and read the gap.
   - Lab: `choicekit`/`commons`. Presets: `herders` (n = 10; payoff polynomials with declining value per animal), `small-commons` (n = 3), `regulated` (a fee added to D). Shipped `gens = 0`. Pin `cmEq`, `cmOpt`, `cmDom`.
   - Misconception: the tragedy requires greed; it requires only that the cost of my animal falls on others.
   - Worked: ten herders: every herder adds, the equilibrium total is lower than the optimum the lab prints, and no herder can improve alone.

10. **public-goods-and-free-riding** — Public Goods and Free-Riding — *Many players*
    - Do: set up the public-goods game with a contribution and a multiplier, show not contributing dominates when the multiplier is below the group size, and compute what a lone free-rider gains and what universal free-riding loses.
    - Lab: `choicekit`/`commons`. Presets: `public-goods` (n = 10, c = 10, m = 3), `small-group` (n = 2, m = 3: contributing dominates), `threshold` (m = n). Pin `cmDom`, `cmUniv`, `cmOpt`.
    - Misconception: if everyone benefits from the good, everyone will pay for it.
    - Worked: C(k) = 3k − 7, D(k) = 3k; defecting dominates by 7; all cooperate gives 20 each, all defect 0, and a lone defector 27.

11. **the-evolution-of-cooperation** — The Evolution of Cooperation — *Many players*
    - Do: run the exact replicator step on the two-player dilemma and on the stag hunt, and read where each population goes from a stated starting share.
    - Lab: `choicekit`/`commons`. Presets: `pd-evolve` (n = 2, PD payoffs; x₀ = 1/2; gens 5), `stag-evolve` (x₀ = 4/5 against x₀ = 1/2), `assortment` (payoffs with a bonus for meeting a cooperator). Shipped `gens = 5`. Pin `cmShare`.
    - Misconception: natural selection favours what is good for the group.
    - Worked: from a cooperator share of 1/2 in the PD, one generation leaves 1/3; in the stag hunt from 4/5 the share rises.

### Course 6 — Ethics and the Arithmetic of Welfare (`ethics-and-welfare`, 12)

Modules: *Metaethics in outline* (1–2), *Consequentialism* (3–6), *Deontology* (7–10), *Virtue and method* (11–12).

1. **is-and-ought** — Is and Ought — *Metaethics in outline*
   - Do: show that an argument whose premises contain no "ought" and whose conclusion does has a counterexample row, and that adding a bridging premise makes it valid — then say what the bridging premise costs.
   - Lab: `argkit`/`validity`. Presets: `hume` ({p, q} ⊢ o), `bridged` ({p, q, (p ∧ q) → o} ⊢ o), `searle` (the promising argument with its bridge). Pin `vaVerdict`, `vaCounter`.
   - Misconception: Hume's point is that moral claims are false.
   - Worked: "Jones promised; promising creates an obligation; so Jones ought to pay" is valid only with the second premise, and the second premise is an "ought".

2. **defining-good-and-the-open-question** — Defining "Good" and the Open Question — *Metaethics in outline*
   - Do: test "good = pleasant" and "good = desired" against a case table (the experience machine, the deceived life, the satisfied sadist) and classify each failure.
   - Lab: `argkit`/`analysis`. Presets: `hedonism` (conditions P pleasant, D desired, A authentic/true-belief; cases with verdicts), `desire` (definition `D`). Shipped `search = pairs`. Pin `anVerdict`, `anFail`, `anCands`.
   - Misconception: a counterexample to a definition of "good" is a disagreement about taste.
   - Worked: the experience machine: pleasant, desired by the user, not authentic, verdict not good — hedonism is too broad, and the search finds `P & A` fits the listed cases.

3. **utilitarianism-and-the-sum-of-welfare** — Utilitarianism and the Sum of Welfare — *Consequentialism*
   - Do: rank two distributions of welfare by total, show the ranking ignores who gets what, and state the theory as a rule of aggregation.
   - Lab: `choicekit`/`aggregate`. Presets: `equal-vs-skewed` (A = 10,10,10; B = 1,30,2), `transfer`, `sacrifice` (one person far below). Shipped `rule = total`. Pin `agVerdict`, `agScores`.
   - Misconception: utilitarianism recommends the greatest good for the greatest number as two separate aims.
   - Worked: A totals 30, B totals 33; total says B, and B's worst-off has 1.

4. **total-average-and-the-repugnant-conclusion** — Total, Average and the Repugnant Conclusion — *Consequentialism*
   - Do: compare total and average on populations of different sizes, compute the smallest population at a tiny welfare level that beats a flourishing one by total, and state mere addition.
   - Lab: `choicekit`/`aggregate`. Presets: `repugnant` (A = 10,10,10; ε = 1/10), `mere-addition` (B = A plus extra people at 2), `average-trap` (average prefers a smaller population). Shipped `rule = total`. Pin `agRepug`, `agVerdict`.
   - Misconception: averaging avoids the problem.
   - Worked: three people at 10; at ε = 1/10 the total is beaten by 301 people; average, meanwhile, prefers one person at 11 to a million at 10.

5. **priority-equality-and-levelling-down** — Priority, Equality and Levelling Down — *Consequentialism*
   - Do: apply a prioritarian weighting and the Gini coefficient to two distributions, and show equality can prefer a distribution that is worse for everyone while priority does not.
   - Lab: `choicekit`/`aggregate`. Presets: `levelling-down` (A = 10,10,10; B = 5,5,5), `priority` (knee at 8; A = 6,14 against B = 9,9), `gini` (A = 10,10,10; B = 1,30,2). Shipped `rule = prioritarian`. Pin `agVerdict`, `agGini`.
   - Misconception: prioritarianism is egalitarianism.
   - Worked: Gini of (1, 30, 2) is 58/99 against 0 for (10, 10, 10); levelling everyone to 5 brings the Gini to 0 and priority still says no.

6. **the-trolley-problem-as-a-decision-matrix** — The Trolley Problem as a Decision Matrix — *Consequentialism*
   - Do: lay the switch and footbridge cases as acts against outcomes, apply total welfare, then apply a side constraint that forbids an act and see which recommendation changes.
   - Lab: `choicekit`/`decide`. Presets: `switch` (divert / do nothing; shipped `rule = eu`, certainty), `footbridge` (push forbidden; shipped `rule = constrained`), `loop`. Pin `deChoice`.
   - Misconception: the two cases differ in their numbers.
   - Worked: the numbers are five against one in both; under total welfare both say act; with "using a person as a means" forbidden, footbridge flips and switch does not.

7. **kant-and-the-universalisability-test** — Kant and the Universalisability Test — *Deontology*
   - Do: model a maxim as the defecting strategy in an n-player game, compute the free-rider's gain when alone and the loss when everyone adopts it, and state the contradiction-in-conception test as the collapse of the practice at universal adoption.
   - Lab: `choicekit`/`commons`. Presets: `false-promise` (honest C(k) = 2; lie D(k) = 5k/(n − 1); n = 10), `tax`, `queue-jumping`. Pin `cmUniv`, `cmDom`.
   - Misconception: the test asks what would happen if everyone did it, as a consequence.
   - Worked: alone among honest promisers the liar gains 3; when all lie, no promise is believed and the lie pays 0 against honesty's 2 — the maxim's point vanishes at universal adoption.

8. **double-effect-means-and-side-effects** — Double Effect, Means and Side Effects — *Deontology*
   - Do: build the switch and loop trolley cases as structural equations, and test whether the good outcome depends on the harm by intervening on the harm.
   - Lab: `argkit`/`structural`. Presets: `switch` (harm not on the path: remove the man and the five still live), `loop` (the man's body stops the trolley: remove him and the five die), `bomber`. Pin `stButFor`, `stKind`.
   - Misconception: double effect is about intentions the lab can read.
   - Worked: in the loop, flipping "the man is hit" flips "the five survive" — the harm is a but-for cause of the good, a means; in the switch it is not.

9. **doing-allowing-and-omissions-as-causes** — Doing, Allowing and Omissions as Causes — *Deontology*
   - Do: model a rescue not performed as a variable, show the omission is a but-for cause of the death, and show two would-be rescuers make neither a but-for cause.
   - Lab: `argkit`/`structural`. Presets: `lifeguard` (R = L ∧ W; D = ¬R), `two-rescuers` (R = W₁ ∨ W₂), `shallow-pond`. Pin `stButFor`, `stHP`, `stKind`.
   - Misconception: an omission cannot be a cause.
   - Worked: the lifeguard was there and unwilling; flipping willingness flips the drowning; with two rescuers each unwilling, neither alone is but-for and the pair is a joint cause.

10. **moral-dilemmas-and-deontic-consistency** — Moral Dilemmas and Deontic Consistency — *Deontology*
    - Do: write a dilemma as {Op, Oq, agglomeration, ought-implies-can, ¬C(p ∧ q)}, show the set is inconsistent, and name the principle each resolution rejects.
    - Lab: `argkit`/`consistency`. Presets: `dilemma` ({op, oq, (op ∧ oq) → opq, opq → cpq, ¬cpq}), `drop-agglomeration`, `drop-can`. Pin `coVerdict`, `coMis`.
    - Misconception: a genuine dilemma is a situation in which you do not know what to do.
    - Worked: the five sentences have no model and the minimal inconsistent subset is all five; a dilemma is real exactly when every exit costs a principle.

11. **virtue-ethics-and-the-function-argument** — Virtue Ethics and the Function Argument — *Virtue and method*
    - Do: formalise Aristotle's function argument, find the premise that must be added for it to be valid, and state honestly that the doctrine of the mean has no structure a lab can test.
    - Lab: `argkit`/`validity`. Presets: `function` ({f → g, r} ⊢ h with the bridge omitted: invalid), `function-bridged` (adding r → f), `enthymeme`. Pin `vaVerdict`, `vaCounter`.
    - Misconception: an argument from a great philosopher is valid as written.
    - Worked: "a thing's good is performing its function well; the human function is reason; so the human good is reasoning well" needs a premise identifying the human function with the function in the first premise, and the counterexample row shows where.

12. **slippery-slopes-and-small-differences** — Slippery Slopes and Small Differences — *Virtue and method*
    - Do: write a slippery-slope argument as a chain of tolerance conditionals, and show the four treatments of such a chain give four different verdicts on the conclusion.
    - Lab: `argkit`/`sorites`. Presets: `weeks` (n₀ = 40, n₁ = 0, cutoff 24), `cents` (a price raised a cent at a time), `grains`. Shipped `treatment = classical`. Pin `soSteps`, `soConc`, `soCond`.
    - Misconception: a slippery slope is always a fallacy.
    - Worked: forty one-week steps each "making no moral difference" deliver an absurd conclusion classically; a cutoff at 24 falsifies exactly one step; degrees spread the loss across all forty.

### Course 7 — Justice and Collective Choice (`justice-and-collective-choice`, 10)

Modules: *Distributive justice* (1–4), *Collective choice* (5–9), *Democracy* (10).

1. **the-original-position-and-maximin** — The Original Position and Maximin — *Distributive justice*
   - Do: model the original position as a choice between societies with the chooser's position as the unknown state, and show maximin and equal-probability expected utility pick different societies from the same matrix.
   - Lab: `choicekit`/`decide`. Presets: `rawls` (equal: 5,5,5; unequal: 2,8,20; shipped `rule = maximin`), `harsanyi` (same matrix, shipped `rule = laplace`), `close-call`. Pin `deChoice`, `deValue`.
   - Misconception: Rawls assumes people are risk-averse about money.
   - Worked: maximin picks the equal society (worst 5 against 2); Laplace picks the unequal one (10 against 5).

2. **the-difference-principle-and-leximin** — The Difference Principle and Leximin — *Distributive justice*
   - Do: rank distributions by leximin, show an unequal distribution that raises the worst-off beats an equal one, and state the incentive argument the principle allows.
   - Lab: `choicekit`/`aggregate`. Presets: `incentive` (A = 5,5,5; B = 6,9,20), `tie-at-the-bottom` (equal worst, decided at the second), `pure-equality`. Shipped `rule = leximin`. Pin `agVerdict`, `agScores`.
   - Misconception: the difference principle demands equality.
   - Worked: (6, 9, 20) beats (5, 5, 5) under leximin because 6 > 5, however large the 20.

3. **entitlement-patterns-and-the-gini-coefficient** — Entitlement, Patterns and the Gini Coefficient — *Distributive justice*
   - Do: compute the Gini coefficient before and after a round of voluntary transfers, and state Nozick's point that liberty upsets patterns as a number.
   - Lab: `choicekit`/`aggregate`. Presets: `chamberlain` (A = 10,10,10,10; B = 9,9,9,13), `redistribute`, `two-rounds`. Shipped `rule = total`. Pin `agGini`, `agVerdict`.
   - Misconception: a just distribution is one with a just shape.
   - Worked: four people at 10 pay 1 each to watch Wilt play: Gini goes from 0 to 3/40 by nobody's injustice.

4. **fairness-statistics-and-disparate-rates** — Fairness, Statistics and Disparate Rates — *Distributive justice*
   - Do: compute acceptance rates by group within departments and pooled, show equal treatment within each department coexisting with unequal overall rates, and name the two notions of fairness that come apart.
   - Lab: `choicekit`/`simpson`. Presets: `berkeley` (two departments with equal within-department rates and different application mixes), `reversal`, `equal-everywhere`. Shipped `siWeight = standardised`. Pin `siVerdict`, `siAdjusted`, `siPooled`.
   - Misconception: a disparity in the pooled rate is a disparity in treatment.
   - Worked: both departments admit men and women at the same rate; women apply to the harder department; the pooled rate differs and the standardised rate does not.

5. **majority-rule-and-the-condorcet-paradox** — Majority Rule and the Condorcet Paradox — *Collective choice*
   - Do: tabulate pairwise majorities from a profile, find a Condorcet winner where one exists, and build the three-voter profile where majority preference cycles.
   - Lab: `choicekit`/`vote`, kind `ranking`. Presets: `cycle` (A>B>C; B>C>A; C>A>B), `winner` (a profile with a Condorcet winner), `near-cycle`. Shipped `rule = condorcet`. Pin `voCondorcet`, `voWinner`.
   - Misconception: majority rule always produces a ranking.
   - Worked: A beats B 2–1, B beats C 2–1, C beats A 2–1; transitive voters, intransitive majority.

6. **plurality-runoff-and-borda** — Plurality, Runoff and Borda — *Collective choice*
   - Do: run plurality, runoff, instant runoff and Borda on one profile and show they elect different candidates; say what each rule is counting.
   - Lab: `choicekit`/`vote`. Presets: `three-winners` (4: A B C; 3: B C A; 2: C B A), `spoiler`, `borda-sweep`. Shipped `rule = plurality`. Pin `voWinner`, `voCondorcet`.
   - Misconception: the candidate with the most first choices is the people's choice.
   - Worked: plurality A (4 firsts), runoff B (5–4), Borda B (12 against 8 and 7), Condorcet B.

7. **independence-and-arrows-theorem** — Independence and Arrow's Theorem — *Collective choice*
   - Do: state unanimity, independence of irrelevant alternatives and non-dictatorship; show on a profile that removing a losing candidate changes the plurality winner; state the theorem and what it does and does not say.
   - Lab: `choicekit`/`vote`. Presets: `iia-plurality` (the three-winners profile; remove C), `iia-borda`, `dictator` (one voter's ranking always wins). Shipped `rule = plurality`, `remove = nobody`. Pin `voIIA`, `voWinner`.
   - Misconception: Arrow proved democracy is impossible.
   - Worked: with C on the ballot plurality elects A; remove C and B wins — the ranking of A and B changed without any voter changing their mind about A and B.

8. **strategic-voting-and-manipulation** — Strategic Voting and Manipulation — *Collective choice*
   - Do: find a group of voters who gain by misreporting their ranking under a stated rule, and state the Gibbard–Satterthwaite theorem.
   - Lab: `choicekit`/`vote`. Presets: `borda-manip` (a profile where burying a rival pays), `plurality-manip` (the spoiler voters switching), `safe` (two candidates: no manipulation). Shipped `rule = borda`. Pin `voManip`, `voWinner`.
   - Misconception: strategic voting is dishonest voting about facts; it is misreporting a ranking.
   - Worked: the voters ranking C first move B to the bottom and Borda elects C.

9. **the-discursive-dilemma** — The Discursive Dilemma — *Collective choice*
   - Do: aggregate three judges' verdicts on two premises and their conjunction, show the majority on the premises implies a conclusion the majority rejects, and name premise-based and conclusion-based procedures.
   - Lab: `choicekit`/`vote`, kind `judgment`. Presets: `court` (p, q, p∧q; judges 1,1,1 / 1,0,0 / 0,1,0), `consistent-court`, `disjunction`. Pin `voWinner`, `voCondorcet`.
   - Misconception: if a majority accepts each premise, a majority accepts the conclusion.
   - Worked: p carries 2–1, q carries 2–1, p ∧ q fails 1–2.

10. **the-condorcet-jury-theorem** — The Condorcet Jury Theorem — *Democracy*
    - Do: compute the probability a majority of n independent voters each right with probability p is right, show it rises with n when p > 1/2 and falls when p < 1/2, and compute the probability a single voter is pivotal.
    - Lab: `choicekit`/`vote`, kind `jury`. Presets: `three` (n = 3, p = 3/5), `eleven`, `incompetent` (p = 2/5). Pin `voJury`, `voPivot`.
    - Misconception: a large electorate is wise whatever the voters' competence.
    - Worked: three voters at 3/5: majority right with probability 81/125; a given voter is pivotal with probability 12/25, and the pivotal probability shrinks fast as n grows.

### Course 8 — Identity, Modality and Freedom (`identity-modality-and-freedom`, 12)

Modules: *Modality* (1–5), *Identity over time* (6–8), *Freedom* (9–11), *God and evil* (12).

1. **necessity-possibility-and-possible-worlds** — Necessity, Possibility and Possible Worlds — *Modality*
   - Do: evaluate □p and ◇p at a world from the worlds it can see, and show necessity is relative to the accessibility relation.
   - Lab: `argkit`/`kripke`. Presets: `two-worlds` (w1 sees w2; p at w2 only; formula `[]p` at w1), `blind` (w1 sees nothing: `[]p` true, `<>p` false), `self` (reflexive). Shipped `at = w1`. Pin `krValue`, `krWorlds`.
   - Misconception: "necessarily p" means "p is true and certain".
   - Worked: w1 sees only w2 where p holds: □p is true at w1 though p is false there — necessity without truth, until the frame is reflexive.

2. **frames-axioms-and-what-necessity-obeys** — Frames, Axioms and What Necessity Obeys — *Modality*
   - Do: compute which of T, D, B, 4 and 5 hold on a frame, and match each to the frame property that produces it.
   - Lab: `argkit`/`kripke`. Presets: `reflexive` (T holds, 4 fails), `s4` (reflexive and transitive), `s5` (an equivalence relation), `serial-only`. Formula `[]p -> p` at w1. Pin `krFrame`, `krAxioms`.
   - Misconception: the modal axioms are truths about necessity rather than choices about the frame.
   - Worked: add the arc w1→w1 and T appears in the tile; add transitivity and 4 appears; the correspondence is computed, not announced.

3. **modal-fallacies-and-the-sea-battle** — Modal Fallacies and the Sea Battle — *Modality*
   - Do: evaluate □(p ∨ ¬p) and □p ∨ □¬p at a world that sees a p-world and a ¬p-world, and name the scope shift in the fatalist's argument.
   - Lab: `argkit`/`kripke`. Presets: `sea-battle` (w1 sees w2 (p) and w3 (¬p); formulas as two presets `wide` and `narrow`), `determined` (w1 sees only p-worlds). Pin `krValue`, `krWorlds`.
   - Misconception: "necessarily, either there will be a sea battle or not" entails that one of them is necessary.
   - Worked: □(p ∨ ¬p) is true at every world; □p ∨ □¬p is false at w1 — the fatalist moved □ inside the disjunction.

4. **the-ontological-argument-in-s5** — The Ontological Argument in S5 — *Modality*
   - Do: evaluate ◇□G → □G on an S5 frame and on a reflexive transitive frame without symmetry, and locate the premise the argument needs the frame to supply.
   - Lab: `argkit`/`kripke`. Presets: `s5` (equivalence relation; G at every world of one class), `no-symmetry` (w1 sees w1, w2; w2 sees w2; G at w2 only; formula `<>[]G -> []G` at w1), `b-axiom`. Pin `krValue`, `krAxioms`.
   - Misconception: the modal ontological argument is invalid.
   - Worked: on the frame without symmetry ◇□G is true at w1 and □G false; add the arc w2→w1 and the conditional holds — the argument is valid in S5 and the question is whether S5 is the right logic for God.

5. **leibnizs-law-and-the-masked-man** — Leibniz's Law and the Masked Man — *Modality*
   - Do: evaluate "I know my father is here" and "I know the masked man is here" in an epistemic model where the masked man is the father, and show substitution inside □ fails while Leibniz's law outside it holds.
   - Lab: `argkit`/`kripke`, reading `epistemic`. Presets: `masked-man` (w1 sees w1, w2; f at both; m at w1 only; formulas `[]f`, `[]m`, `f <-> m` as presets), `extensional`. Pin `krValue`.
   - Misconception: Leibniz's law is refuted by the masked man.
   - Worked: □f true, □m false, f ↔ m true at w1 — the properties "is known by me to be here" differ, and the law applies only to properties of the man, not of my knowledge.

6. **the-ship-of-theseus** — The Ship of Theseus — *Identity over time*
   - Do: write "replacing one plank preserves identity" as a tolerance conditional, run the chain to a ship with no original planks, and state what each treatment of the chain says about the reassembled ship.
   - Lab: `argkit`/`sorites`. Presets: `planks` (n₀ = 1000, n₁ = 0; shipped `treatment = classical`), `cutoff-half`, `degrees`. Pin `soSteps`, `soConc`.
   - Misconception: there is a fact about which ship is the original that the arithmetic can find.
   - Worked: a thousand single-plank steps classically deliver "the all-new ship is the original"; a cutoff at 500 falsifies exactly one replacement; degrees give the all-new ship identity 0.

7. **personal-identity-and-psychological-continuity** — Personal Identity and Psychological Continuity — *Identity over time*
   - Do: distinguish connectedness from continuity as a relation from its transitive closure, and show Reid's brave officer breaks the first and not the second.
   - Lab: `relation` (existing), `preset: "succ"`, `size: 5`; the lesson has the reader apply the transitive closure control.
   - Misconception: memory connects every stage of a life to every other.
   - Worked: the officer remembers the boy, the general remembers the officer, the general does not remember the boy: succ is not transitive; its closure is, and identity is the closure.

8. **fission-and-what-matters** — Fission and What Matters — *Identity over time*
   - Do: write fission as the inconsistent set {A is continuous with me, B is continuous with me, continuity suffices for identity, identity is one-one}, find the minimal inconsistent subset, and name Parfit's exit.
   - Lab: `argkit`/`consistency`. Presets: `fission` ({ca, cb, ca → ia, cb → ib, ¬(ia ∧ ib)}), `no-branching` (continuity suffices only when unbranched), `parfit` (drop the sufficiency claims). Pin `coVerdict`, `coMis`.
   - Misconception: one of the two survivors must be me.
   - Worked: the five sentences have no model; dropping either sufficiency claim restores one; Parfit drops the question.

9. **free-will-determinism-and-compatibility** — Free Will, Determinism and Compatibility — *Freedom*
   - Do: write {determinism, free will, incompatibilism} as a set, show it is inconsistent, and name the three positions as the three deletions; then show two definitions of free will under which the set is and is not consistent.
   - Lab: `argkit`/`consistency`. Presets: `triad` ({d, f, d → ¬f}), `compatibilist` (free will defined as acting on one's own desires: {d, f, f ↔ a, d → ¬o} consistent), `libertarian`. Pin `coVerdict`, `coMis`, `coWitness`.
   - Misconception: compatibilism denies determinism.
   - Worked: hard determinism drops f, libertarianism drops d, compatibilism drops the conditional — three positions, one table.

10. **the-consequence-argument** — The Consequence Argument — *Freedom*
    - Do: read "no one has power over" as a box, show the transfer principle is the K axiom, and evaluate it as valid on every frame — so the dispute is about the premises.
    - Lab: `argkit`/`kripke`. Presets: `transfer` (`([]p & [](p -> q)) -> []q` at w1 on an arbitrary frame; krWorlds "all"), `premise-one` (□ past), `premise-two`. Pin `krWorlds`, `krValue`.
    - Misconception: the consequence argument can be escaped by denying its logic.
    - Worked: □p ∧ □(p → q) → □q holds at every world of every frame the reader builds; what remains is whether the past and the laws are beyond anyone's power.

11. **frankfurt-cases-and-the-ability-to-do-otherwise** — Frankfurt Cases and the Ability to Do Otherwise — *Freedom*
    - Do: build the counterfactual intervener as a structural model, show the agent's decision is not a but-for cause of the act, and show it is a cause once the intervener's inaction is held fixed.
    - Lab: `argkit`/`structural`. Presets: `frankfurt` (B = ¬D; A = D ∨ B; D = 1; cause D), `no-intervener`, `intervener-acts`. Pin `stButFor`, `stHP`, `stKind`.
    - Misconception: responsibility requires that the agent could have done otherwise.
    - Worked: Jones decides and acts; Black would have forced him; flipping Jones's decision leaves the act in place, but holding Black's inaction fixed, the decision flips the act — Jones is the cause though he could not have done otherwise.

12. **the-problem-of-evil-as-an-inconsistent-set** — The Problem of Evil as an Inconsistent Set — *God and evil*
    - Do: write the logical problem of evil as {omnipotent, omniscient, wholly good, evil exists, bridging premise}, show it is inconsistent, and show which deletion each theodicy makes.
    - Lab: `argkit`/`consistency`. Presets: `mackie` ({o, k, g, e, (o ∧ k ∧ g) → ¬e}), `free-will-defence` (bridge weakened to `(o ∧ k ∧ g) → ¬u` with u = unnecessary evil), `evidential`. Pin `coVerdict`, `coMis`, `coWitness`.
    - Misconception: the problem of evil is a probabilistic argument only.
    - Worked: the five sentences have no model and every one is in the minimal inconsistent subset; the free-will defence changes the bridge and a model appears.

### Course 9 — Mind, Language and Meaning (`mind-language-and-meaning`, 10)

Modules: *Mind* (1–5), *Language* (6–10).

1. **dualism-and-the-conceivability-argument** — Dualism and the Conceivability Argument — *Mind*
   - Do: evaluate "necessarily, pain iff C-fibres fire" in a model containing a world with pain and no C-fibres, and locate the step from conceivable to possible as the choice to include that world.
   - Lab: `argkit`/`kripke`. Presets: `zombie` (w1 sees w1, w2; p and c at w1; p only at w2; formula `[](p <-> c)` at w1), `no-zombie-world` (w2 removed). Pin `krValue`, `krWorlds`.
   - Misconception: conceivability is possibility.
   - Worked: with a pain-without-fibres world accessible, □(p ↔ c) is false; without it, true — the argument's work is done by admitting the world.

2. **behaviourism-and-the-turing-test** — Behaviourism and the Turing Test — *Mind*
   - Do: model the judge as an updater whose hypotheses are "human" and "machine", show a perfect mimic gives a Bayes factor of 1 on every answer, and compute what one tell does.
   - Lab: `choicekit`/`update`. Presets: `mimic` (identical likelihood rows; data: ten answers), `tell` (one answer with likelihood 1/10 under "human", 9/10 under "machine"), `prior-heavy`. Pin `upBF`, `upPost`.
   - Misconception: passing the test proves thought, or failing it disproves it.
   - Worked: ten answers from a perfect mimic leave the posterior where the prior was; one tell moves it by a factor of 9.

3. **functionalism-and-multiple-realisability** — Functionalism and Multiple Realisability — *Mind*
   - Do: write two different circuits that compute the same function, show their truth tables agree in every row, and state functionalism as the claim that the state is the function.
   - Lab: `truth_table` (existing), `mode: "two"`, `formulas: ["(p & q) | (p & r)", "p & (q | r)", "~(~p | ~q)", "p & q", "(p -> q) & (q -> p)", "p <-> q"]`, `compare_with: "p & (q | r)"`.
   - Misconception: same behaviour means same mechanism.
   - Worked: `(p ∧ q) ∨ (p ∧ r)` and `p ∧ (q ∨ r)` differ as circuits and agree in all eight rows.

4. **the-chinese-room-and-the-lookup-table** — The Chinese Room and the Lookup Table — *Mind*
   - Do: count the entries a lookup table needs to answer every conversation of r turns with n possible replies, and state Block's and Searle's arguments in terms of that number.
   - Lab: `counting` (existing), `rule: "pr"`, `n: 24`, `r: 12`.
   - Misconception: a lookup table is a small program.
   - Worked: 24 replies over 12 turns is 24¹², a table no room could hold — so the room, if it passes, is not a table.

5. **the-knowledge-argument** — The Knowledge Argument — *Mind*
   - Do: formalise Mary's argument, show it is valid when "knows all the physical facts" and "knows what red looks like" are independent atoms, and show the physicalist's reply as a denial of the second premise rather than of validity.
   - Lab: `argkit`/`validity`. Presets: `mary` ({a → ¬n, n} ⊢ ¬a, with a = physicalism and n = Mary learns a new fact on release: modus tollens, valid), `ability-reply` ({a → ¬n, k} ⊢ ¬a, with k = Mary gains a new ability: invalid, the atom changed), `equivocation` (the two readings of "knows" as two atoms in one argument). Pin `vaVerdict`, `vaForm`.
   - Misconception: the knowledge argument is invalid.
   - Worked: modus tollens; the reply denies that Mary learns a new fact, not that the argument is valid.

6. **compositional-truth-conditions** — Compositional Truth Conditions — *Language*
   - Do: evaluate a sentence of predicate logic in a finite model from the values of its parts, and change one extension to change the value.
   - Lab: `argkit`/`semantics`. Presets: `orbits` (domain a, b, c; Planet: a, b; Orbits: ab, bc; sentence `Ax (Planet(x) -> Ey Orbits(x, y))`), `everyone-loves`, `no-witness`. Pin `seValue`, `seWitness`.
   - Misconception: a sentence is true or false on its own.
   - Worked: every planet orbits something in the model; remove the pair bc and the sentence fails at x = b.

7. **names-reference-and-identity-statements** — Names, Reference and Identity Statements — *Language*
   - Do: assign two names one referent, evaluate `h = p` as true, and explain why the sentence can be informative when the model says it is trivially true — sense against reference.
   - Lab: `argkit`/`semantics`. Presets: `hesperus` (names h, p → a; sentence `h = p`), `distinct` (h → a, p → b), `twin-earth` (two presets with the same sentence, different extensions). Pin `seValue`.
   - Misconception: if a = b is true, "a" and "b" mean the same.
   - Worked: `h = p` is true in the model and `Ax (x = h -> x = p)` with it; the astronomer's discovery is not visible in the model, which is Frege's point.

8. **definite-descriptions-and-the-king-of-france** — Definite Descriptions and the Present King of France — *Language*
   - Do: evaluate "the F is G" by Russell's expansion in a model, and read the three cases: denotes, denotes nothing, not unique.
   - Lab: `argkit`/`semantics`. Presets: `king` (King: nobody; sentence `[the x: King(x)] Bald(x)`), `author` (unique), `two-kings`. Pin `seValue`, `seDesc`.
   - Misconception: "the present King of France is bald" has no truth value on Russell's account.
   - Worked: no king in the domain → Russell: false; the description denotes nothing, which Strawson reads as a failed presupposition, and the tile prints both.

9. **scope-ambiguity-and-negation** — Scope Ambiguity and Negation — *Language*
   - Do: evaluate "the King is not bald" with negation outside and inside the description, and "everyone loves someone" with the quantifiers in both orders, in one model.
   - Lab: `argkit`/`semantics`. Presets: `wide` (`~[the x: King(x)] Bald(x)`), `narrow` (`[the x: King(x)] ~Bald(x)`), `loves` (`Ax Ey Loves(x, y)` against `Ey Ax Loves(x, y)`). Pin `seValue`, `seDesc`.
   - Misconception: a sentence has one logical form.
   - Worked: with no king, the wide reading is true and the narrow reading false — one sentence, two values, one model.

10. **vagueness-and-the-sorites** — Vagueness and the Sorites — *Language*
    - Do: run the heap argument under the four treatments, state what each gives up, and state higher-order vagueness as the problem the cutoff and range treatments inherit.
    - Lab: `argkit`/`sorites`. Presets: `heap` (n₀ = 10,000, n₁ = 0; shipped `treatment = degrees`), `heap-cutoff`, `heap-range` (indeterminate between 50 and 200). Pin `soCond`, `soConc`.
    - Misconception: vagueness is ignorance of a sharp boundary.
    - Worked: ten thousand conditionals each with value 9999/10000 deliver a conclusion with degree 0 — every premise almost true, the conclusion wholly false.

### Course 10 — Paradoxes and Their Exits (`paradoxes-and-their-exits`, 9)

Modules: *Method* (1–2), *The infinite* (3–5), *Probability* (6–8), *Belief* (9).

1. **the-barber-and-the-anatomy-of-a-paradox** — The Barber and the Anatomy of a Paradox — *Method*
   - Do: define a paradox as a valid argument from plausible premises to an unacceptable conclusion, name the three exits, and show the barber's defining sentence is false in every model the reader builds.
   - Lab: `argkit`/`semantics`. Presets: `barber` (`Ax (Shaves(b, x) <-> ~Shaves(x, x))` in a three-individual model), `barber-two`, `honest-barber`. Pin `seValue`, `seWitness`.
   - Misconception: a paradox is a contradiction.
   - Worked: the sentence fails at x = b in every model; the exit is to deny the premise that such a barber exists.

2. **the-liar** — The Liar — *Method*
   - Do: show `p ↔ ¬p` has no satisfying row, state why the liar is not thereby dissolved, and describe Tarski's hierarchy as the exit that forbids the sentence.
   - Lab: `truth_table` (existing), `mode: "one"`, `formulas: ["p <-> ~p", "p -> ~p", "~p -> p", "p | ~p"]`.
   - Misconception: the liar is simply false.
   - Worked: the table has two rows and the formula is F in both: a contradiction; the liar sentence asserts exactly that formula of itself.

3. **zenos-dichotomy** — Zeno's Dichotomy — *The infinite*
   - Do: write the halves as a geometric series, compute partial sums exactly, and show the remainder shrinks below any stated fraction.
   - Lab: `choicekit`/`series`, kind `geometric`. Presets: `halves` (a = 1/2, r = 1/2, n = 10), `thirds`, `twenty`. Pin `srSum`, `srRemain`, `srLimit`.
   - Misconception: infinitely many steps take infinitely long.
   - Worked: ten halves sum to 1023/1024 with 1/1024 to go; the limit is 1.

4. **achilles-and-the-tortoise** — Achilles and the Tortoise — *The infinite*
   - Do: compute the successive gaps as a geometric series with ratio the speed ratio, and find the meeting point as its limit.
   - Lab: `choicekit`/`series`, kind `geometric`. Presets: `ten-to-one` (a = 100, r = 1/10), `close-race` (r = 9/10), `tortoise-wins` (r = 1: no limit). Pin `srLimit`, `srSum`.
   - Misconception: Achilles never catches the tortoise because the gaps never reach zero.
   - Worked: head start 100, speeds 10 and 1: gaps 100, 10, 1, …; the sum is 1000/9 and Achilles passes there.

5. **thomsons-lamp-and-supertasks** — Thomson's Lamp and Supertasks — *The infinite*
   - Do: show the switching times sum to a finite limit while the lamp's state after n switches alternates, and state why the series settles the time and not the state.
   - Lab: `choicekit`/`series`, kind `lamp`. Presets: `lamp` (n = 10), `odd` (n = 11), `long`. Pin `srTerm`, `srSum`.
   - Misconception: a convergent series of actions has a last action.
   - Worked: after ten switches the lamp is off and 1023/1024 of the minute has passed; after eleven it is on; the series fixes the minute and leaves the state undefined.

6. **the-two-envelopes** — The Two Envelopes — *Probability*
   - Do: compute the expected value of switching given the observed amount under a bounded prior, show it exceeds the amount in the interior and falls short at the top, and locate the step the "always switch" argument cannot make.
   - Lab: `choicekit`/`update`. Presets: `interior` (hypotheses: pair is (x/2, x) or (x, 2x) at 1/2 each; payoffs switch x/2, 2x; keep x, x; x = 8), `top` (prior 1, 0), `bottom`. Pin `upBest`, `upPost`.
   - Misconception: the symmetry argument shows switching is always better.
   - Worked: at x = 8 in the interior, switching is worth 10 against 8; at the largest amount the prior on "the other is 2x" is 0 and switching is worth 4.

7. **sleeping-beauty** — Sleeping Beauty — *Probability*
   - Do: state the halfer and thirder answers as two likelihood models for "I am awake", compute both posteriors, and say what the disagreement is about.
   - Lab: `choicekit`/`update`. Presets: `halfer` (P(awake | H) = P(awake | T) = 1), `thirder` (P(this awakening | H) = 1/2, P(this awakening | T) = 1), `told-monday`. Pin `upPost`, `upBF`.
   - Misconception: the coin is fair, so the answer must be 1/2.
   - Worked: the halfer model gives Bayes factor 1 and posterior 1/2; the thirder model gives Bayes factor 1/2 and posterior 1/3.

8. **monty-hall** — Monty Hall — *Probability*
   - Do: compute the posterior over doors from the host's rule, and show the answer changes when the host opens a door at random.
   - Lab: `choicekit`/`update`. Presets: `monty` (car at 1, 2, 3 at 1/3; host opens 3: likelihoods 1/2, 1, 0), `random-host` (likelihoods 1/2, 1/2, 0 — the host might have revealed the car), `four-doors`. Pin `upPost`, `upBest`.
   - Misconception: two doors remain, so each is 1/2.
   - Worked: P(car behind 2 | host opens 3) = 2/3; with a random host, 1/2.

9. **moores-paradox-and-what-cannot-be-believed** — Moore's Paradox and What Cannot Be Believed — *Belief*
   - Do: show `p ∧ ¬□p` is satisfiable while `□(p ∧ ¬□p)` is true at no world of a reflexive frame, and state why "it is raining but I do not believe it" can be true and cannot be believed.
   - Lab: `argkit`/`kripke`, reading `epistemic`. Presets: `moore-true` (`p & ~[]p` at w1; w1 sees w1, w2; p at w1 only), `moore-believed` (`[](p & ~[]p)`; krWorlds "none"), `not-reflexive`. Pin `krValue`, `krWorlds`.
   - Misconception: Moore's sentence is a contradiction.
   - Worked: at w1 the sentence is true; prefix the box and no world of the frame satisfies it.

---

## §D The lab kits

### D.0 Conventions every mode obeys

- **Files.** `scripts/mathpath/labs/argkit.py` and `scripts/mathpath/labs/choicekit.py`;
  registry keys `"argkit"` and `"choicekit"`; both join
  `build_paths.KITS_WITH_EXPECTATIONS` as the LAST step (rule 7). Entry points
  `argkit_lab(cfg)` and `choicekit_lab(cfg)` dispatch on `cfg["mode"]` and
  RAISE on an unknown mode, exactly as `markov_lab` does.
- **Exact arithmetic.** Reuse `algebra_core.RATIONAL_JS` (`R`, `Radd`, `Rmul`,
  `Rcmp`, `Rtext`, `Rparse`, …). Nothing is a float except where a lesson says
  "about" and the tile prints the fraction beside it. BigInt counts where
  `n^r` or binomial sums can overflow.
- **Per-mode script assembly.** A page ships `RATIONAL_JS` + the shared block
  the mode needs (`logic.PARSER_JS` for the propositional modes) + that mode's
  block only — the Algorithms kits' pattern, not Algebra's. Budget: ≤ 40 KB
  gzipped per Philosophy lesson page, measured with the snippet in `AGENTS.md`
  before the kit is called done.
- **Presets are lesson data.** Every mode takes `cfg["presets"]`, a list of
  `{"id", "label", …instance fields…, "expect": {tile: text}}`, and
  `cfg["preset"]` (the id selected at load; default the first). The kit builds
  the `<select id="XXPreset">`, writes the instances into a JS table via
  `cfg_literal`, and returns `Lab(expect={"XXPreset": {id: expect}})`. A preset
  menu's change handler rewrites ONLY the instance text inputs; it never
  touches a redraw-only `<select>`. The shipped value of a redraw-only select
  comes from a cfg key named in the mode spec (`rule`, `treatment`, `view`,
  `show`, `import`, `search`, `kind`, `at`, `remove`, `weight`), defaulting to
  the first option. No second preset menu, ever.
- **A `label` names the instance; an outcome goes in `expect`.** Rule 1.
- **Build-time validation.** The kit raises `ValueError` naming the lesson's
  preset id when an instance is malformed (ragged matrix, probabilities not
  summing to 1, more variables than the limit, an unknown strategy name). It
  does NOT raise on a missing `expect`; labcheck owns that gate.
- **Text inputs survive the hostile sweep** (`''`, `banana`, `0`, `-1`, `1/0`,
  `A>B`): every parse is inside a try/catch that paints the status banner red
  and sets every tile to `—`; the render path is never inside that catch. No
  control's shipped value may contain `>`.
- **Tiles.** `<strong id="…">` in a `kpi-grid`, written by `textContent`, never
  with an entity. Formats below are exact; a fraction is `Rtext` (`3/4`, `2`);
  a verdict is one of a fixed vocabulary; a list is comma-separated in a stated
  canonical order. "—" is the em dash character.
- **Status banner.** Every mode writes one sentence saying what was computed
  and from what, in the library's voice (`id="XXStatus"`).
- **mathcheck.** Each mode's pure functions are module-level, named, and have at
  least one `scripts/mathcheck.js` case that was seen to FAIL when the function
  was broken on purpose (`scripts/mathpath/AGENTS.md`).
- **Refusals** are printed, specific and never silent: the banner says what was
  refused and the limit.

### D.1 `argkit` — eight modes

#### validity
- Purpose: decide whether a propositional argument is valid; show every counterexample row; name the form.
- cfg: `mode`, `preset`, `presets[{id, label, premises: [str], conclusion: str, expect}]`, `show` (`all` | `counter`), `panel_title`, `panel_intro`.
- Controls: `vaPreset` (preset menu); `vaPremises` (text, premises separated by `;`); `vaConclusion` (text); `vaShow` (redraw-only select: all rows | counterexample rows only).
- Syntax: `logic.PARSER_JS` (`~ & | ^ -> <->`, single-letter variables, `⊤ ⊥`).
- Computation: variables = union over premises and conclusion, sorted; rows = all assignments (≤ 6 variables, else refuse); a counterexample row makes every premise true and the conclusion false; valid iff none. Also computed for the banner: premises jointly unsatisfiable ("valid because the premises cannot all be true"), conclusion a tautology. Form: unify premises (as a set, any order) and conclusion against a catalogue of patterns with metavariables binding any subformula: modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, constructive dilemma, simplification, conjunction, addition, contraposition, affirming the consequent, denying the antecedent, affirming a disjunct, converse.
- Tiles: `vaRows` (integer); `vaCounter` (integer); `vaVerdict` (`Valid` | `Invalid`); `vaForm` (catalogue name | `no catalogued form`).
- Refusals: parse error; > 6 variables; > 6 premises; empty conclusion.
- Serves: 1.1, 1.2, 1.5, 1.12, 2.4, 6.1, 6.11, 9.5.

#### consistency
- Purpose: is a set of sentences jointly satisfiable; how many models; one model; every minimal inconsistent subset.
- cfg: `presets[{id, label, sentences: [str], expect}]`.
- Controls: `coPreset`; `coSentences` (text, `;`-separated, ≤ 8 sentences, ≤ 6 variables); `coDrop` (redraw-only select: `keep all` | `drop 1` … `drop n`, options rebuilt by the sentence input's handler; the preset handler resets it to `keep all`).
- Computation: models = assignments satisfying every kept sentence. MIS: enumerate subsets of the kept sentences by increasing size (≤ 256); a subset is inconsistent iff no assignment satisfies all of it; minimal iff no proper subset is. Stage lists all MIS and up to 16 models as columns.
- Tiles: `coModels` (`3 of 16`); `coVerdict` (`Consistent` | `Inconsistent`); `coMis` (`none` | the smallest MIS, ties broken lexicographically, as `{1, 3, 4}` using 1-based sentence numbers); `coWitness` (`p=T q=F r=T` in variable order | `none`).
- Serves: 1.7, 2.5, 3.6, 6.10, 8.8, 8.9, 8.12.

#### syllogism
- Purpose: categorical statements as region constraints; validity by enumerating region patterns; Venn drawing of the counterexample; existential import as a switch.
- cfg: `presets[{id, label, premises: [str] (1 or 2), conclusion: str, expect}]`, `import` (`boolean` | `aristotelian`).
- Controls: `syPreset`; `syP1`, `syP2` (text; `syP2` may be empty); `syC` (text); `syImport` (redraw-only select).
- Grammar: `All X are Y` (A), `No X are Y` (E), `Some X are Y` (I), `Some X are not Y` (O); terms are words (letters, hyphens), case-insensitive, prefix `non-` allowed for complements; at most 3 distinct terms.
- Computation: regions 2^t for t terms; a pattern is a set of nonempty regions; A empties X∧¬Y, E empties X∧Y, I requires a nonempty region in X∧Y, O in X∧¬Y; Aristotelian import requires every term nonempty. Enumerate all patterns (≤ 256), keep those satisfying the premises, test the conclusion in each. Counterexample: the first failing pattern with the fewest nonempty regions, then lexicographic. Form: mood letters + figure and the traditional name when the argument is a standard-form syllogism.
- Tiles: `syVerdict` (`Valid` | `Invalid`, under the selected reading); `syForm` (`AAA-1 Barbara` | `AAA-2 (no name)` | `immediate inference` | `not standard form`); `syModels` (integer: patterns satisfying the premises); `syCounter` (`none` | regions as `S; S+M` — term initials joined by `+`, regions separated by `; `).
- Stage: two or three circles; shaded = empty, × = nonempty, the counterexample pattern drawn when invalid.
- Serves: 1.8, 1.9, 1.10.

#### sorites
- Purpose: a chain of tolerance conditionals from a base case to a conclusion, under four treatments of vagueness.
- cfg: `presets[{id, label, start: int, end: int, predicate: str, cutoff: int, range: [lo, hi], expect}]`, `treatment` (`classical` | `cutoff` | `range` | `degrees`).
- Controls: `soPreset`; `soStart`, `soEnd` (text integers, 0 ≤ end < start ≤ 10⁶); `soCutoff` (text integer, end < cutoff ≤ start); `soRange` (text `lo-hi`); `soTreat` (redraw-only select); `soPred` (text, display only).
- Computation: steps = start − end. classical: every conditional true, conclusion true. cutoff c: the conditional F(c) → F(c−1) false, others true, conclusion false. range [lo, hi]: conditionals with lo ≤ k ≤ hi indeterminate, the universal tolerance premise super-false, conclusion super-false. degrees: δ = 1/steps; v(F(k)) = (k − end)/steps; each conditional has value 1 − δ (Łukasiewicz); conclusion's lower bound by chained modus ponens max(0, 1 − steps·δ) = 0.
- Tiles: `soSteps` (integer); `soCond` (`all 10000 true` | `one false, at k = 50` | `150 indeterminate (51–200)` | `each 9999/10000`); `soConc` (`True` | `False` | `Super-false` | `0`).
- Stage: the first five and last five conditionals listed with their values under the treatment, the cutoff or range marked on a strip.
- Serves: 6.12, 8.6, 9.10.

#### kripke
- Purpose: possible-worlds models; evaluate modal formulas; frame properties; which axioms the frame validates.
- cfg: `presets[{id, label, n: int, access: [[i, j]], valuation: {letter: [worlds]}, formula: str, expect}]`, `at` (world, default 1), `reading` (`alethic` | `epistemic` | `deontic`).
- Controls: `krPreset`; `krN` (range 1–6); `krAccess` (text, pairs `1-2 2-3 3-3`); `krVal` (text, `p: 1 2; q: 3`); `krFormula` (text; `[]` for □, `<>` for ◇, plus the propositional syntax); `krAt` (redraw-only select, options rebuilt by `krN`); `krReading` (redraw-only select; changes only the words in the banner).
- Computation: standard Kripke semantics at every world. Frame properties: reflexive, serial, symmetric, transitive, euclidean. Axiom validity on the frame: for each of D (`[]p -> <>p`), T (`[]p -> p`), B (`p -> []<>p`), 4 (`[]p -> [][]p`), 5 (`<>p -> []<>p`) enumerate every valuation of `p` (2^n) and every world; valid iff true throughout. K is valid on every frame and is not listed.
- Tiles: `krValue` (`True at w1` | `False at w1`); `krWorlds` (`all` | `none` | `w1, w3`); `krFrame` (comma list in the order reflexive, serial, symmetric, transitive, euclidean | `none of the five`); `krAxioms` (comma list in the order `D, T, B, 4, 5` | `none`).
- Stage: the worlds drawn as nodes with arcs, atoms listed inside each node, the evaluated world highlighted and the worlds where the formula holds marked.
- Refusals: n > 6; a world index out of range; parse error; a formula over more than 4 atoms.
- Serves: 8.1, 8.2, 8.3, 8.4, 8.5, 8.10, 9.1, 10.9.

#### semantics
- Purpose: a finite first-order model; evaluate a sentence; witness or counterexample; Russell's description operator with presupposition status.
- cfg: `presets[{id, label, domain: [letters], names: {name: letter}, predicates: {Name: [letters] | [[l, l]]}, sentence: str, expect}]`.
- Controls: `sePreset`; `seDomain` (text, single letters `a b c`, ≤ 6); `seExt` (text, `Planet: a b; Orbits: ab bc; King:`); `seNames` (text, `h=a p=a`); `seSentence` (text).
- Grammar: predicates are capitalised words with 1 or 2 arguments; terms are variables `x y z`, names (lowercase words from `seNames`) or domain letters; `=`; `~ & | -> <->`; quantifiers `Ax`/`∀x`, `Ex`/`∃x`; description `[the x: F(x)] G(x)` expanded to `Ex (F(x) & Ay (F(y) -> y = x) & G(x))`, nested in any position so negation may scope over it or under it.
- Computation: recursive evaluation; the outermost quantifier's witness (first individual in domain order) or counterexample; for a description, whether its restrictor is satisfied by exactly one, none, or several individuals.
- Tiles: `seValue` (`True` | `False`); `seWitness` (`x = b` | `fails at x = c` | `—`); `seDesc` (`no description` | `denotes a` | `denotes nothing` | `not unique: a, b`); `seSat` (`2 of 3 satisfy` for the outermost quantified matrix | `—`).
- Refusals: unknown predicate or name; arity mismatch; > 6 individuals; quantifier depth > 3.
- Serves: 9.6, 9.7, 9.8, 9.9, 10.1.

#### analysis
- Purpose: a definition tested against a case table (the method of cases, Mill's methods); the formulas that would fit.
- cfg: `presets[{id, label, conditions: [letters], target: str, cases: [{name, values: [0/1], verdict: 0/1}], definition: str, expect}]`, `search` (`off` | `singles` | `pairs`).
- Controls: `anPreset`; `anDef` (text, a formula over the condition letters); the case table in the stage with clickable value and verdict cells; `anSearch` (redraw-only select).
- Computation: evaluate the definition on every case; agreement count; first disagreeing case in table order and its direction (definition true, verdict false = too broad; the reverse = too narrow); candidates: `singles` tries every literal, `pairs` every conjunction and disjunction of two literals on distinct conditions; a candidate matches all cases.
- Tiles: `anAgree` (`5 / 6`); `anFail` (`none` | `Smith: too broad` | `Norman: too narrow`); `anVerdict` (`Adequate` | `Too broad` | `Too narrow` | `Too broad and too narrow`); `anCands` (`none` | `3: first J & ~L` | `—` when search is off).
- Refusals: > 6 conditions; > 10 cases; a row of the wrong length; parse error.
- Serves: 2.1, 2.2, 2.3, 3.7, 6.2.

#### structural
- Purpose: Boolean structural causal models; actual values; but-for; Halpern–Pearl (modified) with a witness set; joint causes.
- cfg: `presets[{id, label, equations: {Var: formula}, exogenous: {Var: 0/1}, cause: Var, effect: Var, expect}]`.
- Controls: `stPreset`; `stEqs` (text, `D = S1 | S2; F = D & ~G`); `stExo` (text, `S1=1 S2=1 G=0`); `stCause`, `stEffect` (redraw-only selects, options rebuilt from the equations).
- Computation: variables = exogenous ∪ left-hand sides; the dependency graph must be acyclic. Evaluate in topological order. But-for: set the cause to its negation, re-evaluate, does the effect change. HP: over every subset W of the other endogenous variables (≤ 8 variables), hold W at actual values, flip the cause, re-evaluate; a cause iff some W flips the effect; witness = the smallest such W, lexicographic. Joint: if no single W works, try flipping the cause together with each other single variable; report the partner.
- Tiles: `stActual` (`D = 1`); `stButFor` (`Yes` | `No`); `stHP` (`Yes, holding nothing` | `Yes, holding {BH}` | `No`); `stKind` (`but-for cause` | `cause (holding fixed)` | `joint cause with BT` | `not a cause`).
- Stage: the equation table with three value columns — actual, cause flipped, cause flipped with the witness held.
- Refusals: a cycle; an undefined variable; parse error; > 8 variables.
- Serves: 3.9, 3.10, 6.8, 6.9, 8.11.

### D.2 `choicekit` — ten modes

#### decide
- Purpose: a decision matrix under every rule the course teaches.
- cfg: `presets[{id, label, acts: [str], states: [str], payoffs: [[rational]], probs: [rational] | null, conditional: {act: [rational]} | null, forbidden: [act], expect}]`, `rule` (`dominance` | `maximin` | `maximax` | `regret` | `laplace` | `eu` | `evidential` | `constrained`).
- Controls: `dePreset`; `deActs`, `deStates` (text); `deMatrix` (text, rows `;`, entries spaces); `deProbs` (text, empty for ignorance); `deCond` (text, `one: 9/10 1/10; two: 1/10 9/10`, empty when none); `deForbid` (text, act names); `deRule` (redraw-only select).
- Computation (exact): dominance — the acts not strictly dominated (a dominates b iff ≥ in every state and > in some), choice = the single act dominating all others, else `none`; maximin/maximax on row min/max; regret = column max − entry, minimax over rows; Laplace = row average; `eu` = Σ probs·payoff; `evidential` = Σ conditional[act]·payoff; `constrained` = `eu` over acts not forbidden; VPI = Σ_s p_s·max_a u − max_a EU (probs required); indifference probability for 2-state problems: p(state 1) at which the top two acts by EU tie.
- Tiles: `deChoice` (act | `take, leave` tie in act order | `none`); `deValue` (the rule's score of the choice | `—`); `deVpi` (fraction | `—`); `deFlip` (`p(rain) = 2/7` | `none` | `—`).
- Refusals: ragged matrix; > 5 acts or states; probabilities or any conditional row not summing to 1; a rule needing probabilities with none given (tiles `—`, banner says which).
- Serves: 4.2–4.9, 6.6, 7.1.

#### update
- Purpose: exact Bayesian updating over a finite set of hypotheses; Bayes factor; predictive probability; best act after updating.
- cfg: `presets[{id, label, hyps: [str], prior: [rational], outcomes: [str], lik: [[rational]] (rows = hyps), data: [outcome], payoffs: {act: [rational per hyp]} | null, expect}]`.
- Controls: `upPreset`; `upPrior` (text); `upLik` (text matrix); `upData` (text, outcome names separated by spaces); `upPay` (text, `switch: 2 1/2; keep: 1 1`, empty when none); `upHyp` (redraw-only select: which hypothesis the tiles report; default the first).
- Computation: sequential exact updates; Bayes factor of the selected hypothesis H against its negation = P(data | H) / P(data | ¬H) with P(data | ¬H) the prior-weighted mixture over the others; `infinite` when the denominator is 0; predictive distribution of the next outcome; expected payoff of each act under the posterior.
- Tiles: `upPost` (fraction); `upBF` (fraction | `infinite`); `upConf` (`Confirms` | `Disconfirms` | `Neutral` | `Refutes` (posterior 0) | `Proves` (posterior 1)); `upPred` (predictive probability of the FIRST outcome); `upBest` (`switch: 5/4` | `—`).
- Refusals: prior or a likelihood row not summing to 1; a datum not among the outcomes; data impossible under every hypothesis.
- Serves: 2.8, 2.9, 3.1–3.5, 9.2, 10.6, 10.7, 10.8.

#### credence
- Purpose: a belief threshold over a finite space; consistency of the accepted set; the probability of its conjunction; a Dutch book from typed credences.
- cfg: `presets[{id, label, kind: space | lottery | independent, outcomes: [str], probs: [rational], events: [{name, set: [outcome]}], n: int, p: rational, threshold: rational, typed: {event: rational}, expect}]`.
- Controls: `crPreset`; `crKind` (set by the preset; redraw-only); `crN` (range 2–1000); `crP` (text); `crThreshold` (text); `crEvents` (text, `even: 2 4 6; high: 5 6`, space kind only); `crTyped` (text, `heads=3/5 tails=3/5`).
- Computation: space — P(event) from the distribution; accepted = P ≥ threshold; conjunction = intersection of accepted events; consistent iff nonempty. lottery — n equiprobable outcomes, events "ticket i loses"; conjunction empty iff all accepted. independent — n claims each with probability p; accepted iff p ≥ threshold; P(all) = p^n exactly; always consistent. Dutch book (space kind, typed credences): a credence outside [0, 1]; complementary pair with sum ≠ 1 → loss |1 − sum| per unit; disjoint A, B with A∪B listed and c(A∪B) ≠ c(A) + c(B) → loss of the difference. Else `none found`.
- Tiles: `crAccepted` (`100 of 100`); `crPAll` (fraction); `crConsistent` (`Consistent` | `Inconsistent`); `crBook` (`none found` | `loss 1/5 per unit`).
- Serves: 2.6, 2.11, 2.12.

#### series
- Purpose: exact partial sums.
- cfg: `presets[{id, label, kind: geometric | harmonic | petersburg | lamp, a, r, n, cap, expect}]`.
- Controls: `srPreset`; `srKind` (redraw-only); `srA`, `srR` (text); `srN` (range 1–60); `srCap` (text integer, empty for none).
- Computation: geometric — term a·r^(n−1), S_n = a(1 − rⁿ)/(1 − r), limit a/(1 − r) when |r| < 1 else `none`, remainder = limit − S_n. harmonic — exact S_n, limit `none`. petersburg — term_k = min(2^k, cap)/2^k (1 when uncapped), S_n, limit K + cap/2^K with K = ⌊log₂ cap⌋ when capped, else `none`. lamp — term ±1 (state after n switches, +1 on), S_n of the switching times 1 − 1/2^n, limit 1.
- Tiles: `srTerm` (fraction | `+1 (on)` | `−1 (off)`); `srSum` (fraction); `srLimit` (fraction | `none`); `srRemain` (fraction | `—`).
- Serves: 4.10, 10.3, 10.4, 10.5.

#### game
- Purpose: a bimatrix game up to 4×4.
- cfg: `presets[{id, label, rows: [str], cols: [str], payoffs: [[[r, c]]], expect}]`, `view` (`best` | `dominance` | `pareto`).
- Controls: `gaPreset`; `gaRows`, `gaCols` (text); `gaMatrix` (text, `3,3 0,5; 5,0 1,1`); `gaView` (redraw-only select, recolours the stage).
- Computation: best responses; pure equilibria; strict and weak dominance per player; iterated elimination of strictly dominated strategies; the completely mixed equilibrium of a 2×2 game when both probabilities lie strictly in (0, 1); Pareto-efficient cells; whether each pure equilibrium is Pareto-dominated.
- Tiles: `gaPure` (`(D, D)` | `(C, C); (D, D)` in row-major order | `none`); `gaMixed` (`row C: 1/2, col C: 1/2` | `none` | `—` for larger games); `gaDom` (`D dominates for both` | `D dominates for row` | `iterated elimination leaves (B, Y)` | `none`); `gaPareto` (`(D, D) is dominated by (C, C)` | `every equilibrium is efficient` | `—`).
- Serves: 5.1, 5.2, 5.3, 5.4, 5.8.

#### iterated
- Purpose: the repeated prisoner's dilemma.
- cfg: `presets[{id, label, R, S, T, P, rounds, a, b, delta, expect}]`.
- Controls: `itPreset`; `itPay` (text `3 0 5 1` = R S T P); `itA`, `itB` (redraw-only selects over ALLC, ALLD, TFT, GRIM, PAVLOV, TF2T, STFT); `itRounds` (range 1–50); `itDelta` (text).
- Computation: requires T > R > P > S and 2R > T + S (else refuse); play the rounds; round-robin tournament of all seven strategies against each other and themselves over the same number of rounds; thresholds δ_GRIM = (T − R)/(T − P), δ_TFT = max(δ_GRIM, (T − R)/(R − S)).
- Tiles: `itScoreA`, `itScoreB` (integers or fractions); `itWinner` (`TFT: 273` | `TFT, GRIM: 273`); `itThresh` (`GRIM 1/2, TFT 2/3: δ = 9/10 sustains` | `…: δ = 1/4 does not`).
- Serves: 5.5, 5.6, 5.7.

#### commons
- Purpose: the n-player symmetric binary-choice game; universalisation; replicator steps.
- cfg: `presets[{id, label, n, payC: str, payD: str, x0: rational, gens: int, expect}]`, `gens`.
- Controls: `cmPreset`; `cmN` (range 2–50); `cmPC`, `cmPD` (text: polynomials in `k` (others cooperating) and `n` with rational coefficients, operators `+ - * / ^` and parentheses, evaluated exactly); `cmX0` (text); `cmGens` (range 0–40).
- Computation: C(k), D(k) for k = 0…n−1; dominance; symmetric equilibria k* (no cooperator wants to switch: C(k*−1) ≥ D(k*−1); no defector wants to switch: D(k*) ≥ C(k*)); social optimum over k of k·C(k−1) + (n−k)·D(k); universalisation numbers: alone = D(n−1) − C(n−1), everyone = D(0) − C(n−1); replicator: x' = x·fC / (x·fC + (1−x)·fD) with fC = C(x·(n−1)), fD = D(x·(n−1)) evaluated at the rational k.
- Tiles: `cmDom` (`Defect dominates` | `Cooperate dominates` | `neither`); `cmEq` (`k* = 0` | `k* = 0, 10` | `none`); `cmOpt` (`all 10 cooperate: total 200` | `7 cooperate: total 63`); `cmUniv` (`alone +7, everyone −20`); `cmShare` (fraction after `gens` generations).
- Serves: 5.9, 5.10, 5.11, 6.7.

#### vote
- Purpose: collective choice in three kinds.
- cfg: `presets[{id, label, kind: ranking | judgment | jury, cands, profile: [{count, rank}], atoms, formula, voters: [[0/1]], n, p, expect}]`, `rule`, `remove`.
- Controls: `voPreset`; `voKind` (set by the preset); `voProfile` (text: `4: A B C; 3: B C A; 2: C B A` | `p q p&q: 1 1 1; 1 0 0; 0 1 0` | `n=3 p=3/5`); `voRule` (redraw-only: plurality | runoff | irv | borda | condorcet | copeland); `voRemove` (redraw-only: `nobody` | each candidate; options rebuilt from the profile).
- Computation: ranking — ≤ 5 candidates, ≤ 60 voters; winners under the six rules; pairwise matrix; Condorcet winner or the top cycle; IIA: recompute the selected rule's winner with each losing candidate removed; manipulation: for each distinct ranking group try every permutation (≤ 120) and report the first that elects a candidate the group ranks above the sincere winner. judgment — majority per atom, the formula evaluated at the majority assignment, against the majority on the formula's value. jury — P(majority correct) = Σ_{k>n/2} C(n,k)p^k(1−p)^{n−k} exactly; pivotal = C(n−1,(n−1)/2)·(p(1−p))^((n−1)/2) for odd n.
- Tiles: `voWinner` (`B` | `B, C (tie)` | judgment `premise-based: T; conclusion-based: F` | `—`); `voCondorcet` (`A` | `cycle: A > B > C > A` | `none` | judgment `premises T, T; conclusion F` | `—`); `voIIA` (`holds` | `violated (remove C)` | `—`); `voManip` (`none found` | `voters ranking C B A gain by C A B` | `—`); `voJury` (fraction | `—`); `voPivot` (fraction | `—`).
- Serves: 7.5–7.10.

#### aggregate
- Purpose: two welfare distributions under six rules; inequality; the repugnant conclusion's n*.
- cfg: `presets[{id, label, A: [rational], B: [rational], knee, threshold, eps, expect}]`, `rule` (`total` | `average` | `prioritarian` | `maximin` | `leximin` | `sufficientarian`).
- Controls: `agPreset`; `agA`, `agB` (text vectors, ≤ 12 entries); `agRule` (redraw-only); `agKnee`, `agThresh`, `agEps` (text).
- Computation: total; average; prioritarian Σ g(x) with g(x) = x for x ≤ knee, knee + (x − knee)/2 above; maximin; leximin (sorted ascending, lexicographic); sufficientarian (fewer below threshold, then smaller total shortfall, then total); Gini = Σᵢⱼ|xᵢ − xⱼ| / (2n²·mean); n* = smallest n with n·eps > total(A).
- Tiles: `agVerdict` (`A ≻ B` | `B ≻ A` | `A ~ B`); `agScores` (`30 vs 33`; leximin prints `worst 10 vs 1`); `agGini` (`0 vs 58/99`); `agRepug` (`n* = 301` | `—`).
- Serves: 6.3, 6.4, 6.5, 7.2, 7.3.

#### simpson
- Purpose: rates within two groups and pooled; reversal; standardised rates.
- cfg: `presets[{id, label, names: [A, B], groups: [{name, a: [s, t], b: [s, t]}], expect}]`, `weight` (`pooled` | `standardised`).
- Controls: `siPreset`; `siNames` (text); `siTable` (text, `small: 81/87 234/270; large: 192/263 55/80`); `siWeight` (redraw-only).
- Computation: rates per cell as exact fractions; pooled rates; within-group comparisons; reversal iff the pooled comparison disagrees with both within-group comparisons; standardised rate = Σ_g w_g·rate_g with w_g the group's share of all trials.
- Tiles: `siPooled` (`A 273/350 vs B 289/350: B higher`); `siGroup1`, `siGroup2` (`A higher` | `B higher` | `equal`); `siAdjusted` (same format as `siPooled`); `siVerdict` (`Reversal` | `No reversal`).
- Serves: 2.10, 3.8, 7.4.

### D.3 Existing modes reused (exact keys and cfg)

| key | cfg used here | lessons |
| --- | --- | --- |
| `truth_table` | `formulas`, `compare_with`, `mode` (`one`/`two`), `panel_title`, `panel_intro` | 1.3, 1.4, 1.6, 9.3, 10.2 |
| `quantifier` | `preset: "succ"`, `size: 4` | 1.11 |
| `relation` | `preset: "lt"` (4.1), `preset: "succ"` (8.7), `size: 5` | 4.1, 8.7 |
| `bayes` | `prev: 1000, sens: 99, fpr: 5` | 2.7 |
| `counting` | `rule: "pr", n: 24, r: 12` | 9.4 |

None of these kits is in `KITS_WITH_EXPECTATIONS`, so their pages carry no
pinned tiles; labcheck still sweeps their controls. Not reused, and why:
`sets` (its expression menu is fixed and the categorical reading needs
shading, which `syllogism` draws); `duality/game` (zero-sum only, and its page
is 60 KB gzipped — `game` solves 2×2 mixed equilibria in closed form);
`distribution` (shows the binomial pmf, not the majority tail `vote/jury`
needs); `induction` (mathematical induction, not Hume's).

### D.4 Listen: the speech changes the kits need

`scripts/mathpath/speech.py` SYMBOLS (chrome-renderer tier, one commit, before
any modal lesson is built):

- `"□": "necessarily"` — currently `"end of proof"`; no content uses `□` in a
  math run today (verified by grep), and the proof block emits `&#9633;` as
  markup, not through speech.
- `"◇": "possibly"` — currently absent, so a run with it would fail
  `tests/test_speech.py` as unspoken.
- `"≻": "is preferred to"`, `"≽": "is weakly preferred to"` — absent today.

Authors never write `~` for negation in prose or math blocks (`~` is spoken
"is approximately"); write `¬`. Never `⊃` for the conditional (spoken "is a
proper superset of"); write `→`. Quote lab syntax in words ("a tilde for
not"), never as a math run. Runs that still read wrongly get a line in
`content/spoken/philosophy.py`.

---

## §E Package layout and the author's checklist

```
content/philosophy/
  __init__.py                 PATH, COURSES (filter COURSE = None), numbering loop
  c1_arguments/__init__.py    COURSE dict; lessons = part_a.LESSONS + part_b.LESSONS
  c1_arguments/part_a.py      LESSONS = [...]   lessons 1–6
  c1_arguments/part_b.py      LESSONS = [...]   lessons 7–12
  c2_knowledge/ … c10_paradoxes/   same shape; split a course at its midpoint
content/spoken/philosophy.py  SPOKEN = {run: words}   starts empty
```

Mirror `content/operations_research/__init__.py` exactly for the package
`__init__`, and `content/discrete_math/c1_logic/__init__.py` for a course
`__init__`. A course not yet written exports `COURSE = None`.

**Course fields** (all required; `assumes_short` is consumed nowhere but every
existing course carries it — carry it): `slug`, `title`, `level`, `summary`,
`blurb`, `key` (4–8 lines, each ≤ 46 characters, no second column),
`assumes_short`, `assumes_long` (lowercase start, no trailing period, names
courses by TITLE), `outcomes_intro`, `outcomes` (4–6 pairs), `syllabus_intro`,
`how_to` (3–4 paragraphs), `not_covered` (3–6 paragraphs; the honest list from
§G for that course), `footer_lead`, `lessons`.

**Lesson fields** — every one required; the renderer uses `.get` for some but
`TestLessonDataMatchesTheRenderer` reads them directly:

| field | shape | enforced |
| --- | --- | --- |
| `slug` | lowercase, hyphens, ≤ 48 chars, unique in the course | URL space |
| `title` | plain text, no backticks, no entities | `test_fields_that_reach_metadata_stay_plain`, `test_escaped_fields_carry_no_html` |
| `module` | plain text, one of the course's module names | same |
| `one_line` | one sentence, no entities/tags | escaped |
| `summary` | 2–4 sentences, prose (entities and `x` runs allowed) | metadata via `plain()` |
| `key` | 3–8 lines, each ≤ 46 chars, no entities, no second column | range (3, 8) |
| `key_label` | plain | escaped |
| `concepts_intro` | prose | — |
| `concepts` | EXACTLY 3 `(title, body)`; titles plain | exact |
| `read_title`, `read_intro` | plain / prose | escaped / — |
| `body` | 7–18 blocks of kinds `p h3 math ul ol def thm example proof`; `h3` and `math` lines plain | range (7, 18) |
| `lab` | `(key, cfg)`; cfg per §D | `TestEveryLabBuilds`, labcheck |
| `steps_title`, `steps_intro` | plain / prose | escaped |
| `steps` | 4–5 `(title, body)` | range (4, 5) |
| `worked` | `{title (plain), intro: [prose], lines: [plain, ≤ 60 chars], after: [prose]}` | escaped |
| `quiz_title` | plain | escaped |
| `quiz` | 3–4 items `{q, a: [exactly 4 distinct], c: index, why}`; one defensible answer | `test_every_quiz_question_is_answerable` |
| `mistakes` | EXACTLY 3 `(title, body)`; the first is the §C misconception | exact |
| `standard` | `(head plain, body prose)` | escaped |
| `note` | prose | — |

Prose fields may use `&mdash;`, `&ldquo;`, `<strong>`, `<em>` and the `x`
math shorthand. Escaped fields take real characters (—, “ ”) and no shorthand.

**Per-lesson procedure.**

1. Write the dict from the §C entry. The §C misconception is `mistakes[0]`.
2. Write the presets with `expect` left as `{}`.
3. `python3 scripts/build_paths.py` (Philosophy must already be in
   `GENERATED_PATHS` on the branch — §H).
4. `node scripts/labcheck.js --observe site/<course>/<lesson>/index.html`; copy
   the tile strings the preset exists to show into `expect`; rebuild.
5. `node scripts/labcheck.js site/<course>/<lesson>/index.html` and
   `/usr/bin/python3 scripts/speechcheck.py`; fix any unspoken run with a line
   in `content/spoken/philosophy.py`.
6. Check every quiz distractor by trying to argue for it; if you can, rewrite.
7. Read the page aloud in your head: every `x` run must read as a sentence.

---

## §F Voice and style

This library is written in careful prose by someone who has thought about the
thing and is telling you what they found. Not a textbook, not a lecture, not a
chat. The rules that follow are what that sounds like.

- **Say what is computed and from what, in the sentence that reports it.** "The
  lab finds the row p = F, q = T" rather than "the lab shows the argument is
  invalid".
- **Name the act, not the understanding.** Objectives, `standard` heads and
  outcome titles are verbs the closing check can measure: classify, construct,
  compute, locate, formalise. "Understand" is a defect.
- **One hard idea per lesson.** Everything else in the lesson serves it. If a
  second hard idea appears, it is the next lesson's.
- **The misconception is named as a model someone holds**, then corrected with
  the specific row, case or number that refutes it. "A common error is…" without
  the refutation is a defect.
- **Positions are stated at their strongest.** The skeptic, the hedonist and
  the one-boxer each get a valid argument; the lab shows it valid; the lesson
  says what accepting the conclusion or rejecting a premise costs. The reader
  decides. A lesson that announces the winner has stopped being philosophy.
- **The lab's limit is stated in the lesson that leans on it.** Validity is
  checked; soundness is not. A model has the worlds you gave it. A payoff is a
  number you chose. Say so where it matters, once, plainly.
- **Cross-references by title, never by number.** “Validity by Truth Table”
  for a lesson, Knowledge and Evidence for a course, Discrete Probability on
  the Discrete Mathematics path for another Subject. Relative prose ("the next
  course", "earlier in this course") is fine.
- **Math a voice can read.** Products written with `·`; `P(H | E)` with spaces
  around the bar; `¬` not `~`; `→` not `⊃`; `□`, `◇`, `≻` only after the speech
  change in §D.4; tables in `math` blocks, one cell per column, never along a
  line of prose.
- **Quiz questions test the idea, not the vocabulary**, and every wrong choice
  gets the reason it is wrong in `why`.
- **No filler.** No "In this lesson we will", no "Let's", no exclamation marks,
  no rhetorical questions in a row, no emoji. British or American spelling as
  the author pleases but consistent within a course.

**One exemplary paragraph** (a `p` block for “Validity by Truth Table”):

> A counterexample is a row, and only a row. It is an assignment of truth
> values to the simple sentences under which every premise comes out true and
> the conclusion comes out false; nothing about the world is being claimed,
> only that such a case is describable. So an argument is valid when no such
> row exists, and invalid when one does, and the second verdict needs exactly
> one row to establish it. For `p → q, q ∴ p` the lab finds the row `p = F,
> q = T`: the premises hold, the conclusion fails, and no argument about the
> other three rows can rescue the form &mdash; which is why "if God exists
> life has meaning; life has meaning; so God exists" is settled by a table and
> not by theology.

---

## §G What is left out, and why

Stated here so every course's `not_covered` can draw on it, and so no author
invents a decorative lab to fill a gap.

- **History of philosophy as history.** No lesson is about what a philosopher
  said; several are about an argument a philosopher made, taught as the
  argument. Dates, schools and influence are not computable and are not here.
- **Phenomenology, existentialism, hermeneutics, critical theory.** Their
  claims are not of a shape a lab can test without misrepresenting them, and a
  lesson that misrepresents a tradition to get a widget is worse than silence.
- **Aesthetics**, except that "defining art" is a legitimate instance of the
  method of cases and an author of Ethics and the Arithmetic of Welfare may use
  it as a preset in “Defining ‘Good’ and the Open Question”'s mode. No course
  of its own.
- **Virtue ethics beyond the function argument.** The doctrine of the mean,
  practical wisdom and moral education have no checkable structure; the lesson
  says so.
- **Metaethics beyond is/ought and the open question**: expressivism,
  error theory, moral realism's arguments. The Frege–Geach problem is
  computable in principle (validity of arguments with embedded moral terms)
  and is a candidate for a future lesson; not built.
- **Natural deduction and proof systems.** The Subject decides validity by
  truth table and by countermodel; it does not derive. Logic and Proof on the
  Discrete Mathematics path is where proof technique lives.
- **First-order validity in general** (undecidable). `semantics` evaluates in
  the model you build; it does not search for a countermodel across all
  models. The barber lesson is honest about this: "false in every model you
  build here" is the computed claim.
- **Infinite outcome spaces and continuous priors.** Every update is over
  finitely many hypotheses; the rule of succession appears as its five-point
  discretisation and says so. No densities, no integrals.
- **Statistics as inference**: significance tests, confidence intervals,
  regression. Simpson's paradox is computed from counts; nothing is estimated.
- **Sen's liberal paradox, the Gibbard–Satterthwaite proof, Arrow's proof.**
  The theorems are stated; their conditions are checked on profiles; the proofs
  are not reproduced.
- **Kripke semantics for quantified modal logic, counterpart theory, temporal
  logic.** The sea battle is treated as a modal scope fallacy, not with a
  tense logic.
- **Causal inference from data** (do-calculus, identifiability). Structural
  models here are Boolean and given, not learned.
- **Philosophy of mathematics, philosophy of physics, philosophy of
  religion beyond the three arguments taught** (ontological, cosmological
  shift, evil) and Pascal.
- **Personal identity's bodily and narrative criteria**, except as prose
  beside the psychological criterion.
- **The surprise examination, the unexpected hanging, Curry's paradox, the
  Ross–Littlewood paradox, Pascal's mugging.** Each needs machinery not built
  (epistemic logic with announcements, a non-classical consequence relation, a
  set-theoretic limit, unbounded utilities). Named in Paradoxes and Their
  Exits' `not_covered`.

---

## §H Wiring notes for the orchestrator

Not an author's job; recorded so nobody asks.

- Register `philosophy` in `scripts/build_paths.py` `GENERATED_PATHS` at the
  START of the branch, with every course `COURSE = None`, so authors can build
  and observe pages as they land. `tests/test_review_remediation.py`
  `content_errors` will demand `content_preservation.json` entries for every
  `.py` in the package from that moment; generate them with `/usr/bin/python3`
  via `content_fingerprint` imported from the test module, never re-derived.
- `tests/test_site_invariants.py`: `PHIL_DISCLAIMER_RE`, the path page constant
  and its entry in `PATH_MATERIAL_DISCLAIMER`, course home constants, the slug
  tuples, `TestLessonDataMatchesTheRenderer.setUpClass` and
  `TestEveryLabBuilds.setUpClass` import lists (they import only two paths
  today; the newer Subjects are checked elsewhere — extend whichever the
  pattern is), `REQUIRED_PAGES`.
- `test_public_copy`'s `philosophy_semantic_copy` block, derived from RENDERED
  text.
- The two dozen declaration sites in `AGENTS.md` §0, with the check-id prefix
  `phil`.
- `KITS_WITH_EXPECTATIONS`: add `"argkit", "choicekit"` only after every preset
  on the branch carries `expect` (rule 7).
- `speech.py` symbol additions (§D.4) land before the first modal lesson.
- Page weight re-measured and the table in `AGENTS.md` updated.
- `docs/philosophy/COURSES.json` is the fan-out manifest for authors; it and
  §C must agree (a script generated both lists from one table).
