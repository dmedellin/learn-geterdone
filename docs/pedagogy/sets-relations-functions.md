# Pedagogy assessment — Sets, Relations, and Functions (discrete mathematics, course 2)

First assessment, formed from the fourteen lesson dicts in
`content/discrete_math/c2_sets/` (`part_a.py`, `part_b.py`, `__init__.py`)
and the lab kits they render through (`scripts/mathpath/labs/sets.py` for
the set, relation and function labs; `scripts/mathpath/labs/counting.py`
for the two lessons that borrow course 4's counting lab), as they stand on
`main` at c604a92. No prior assessment exists for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `sets-and-membership`, `subsets-and-power-sets`,
`set-operations`, `set-identities`, `cartesian-products-and-tuples`,
`binary-relations`, `properties-of-relations`,
`equivalence-relations-and-partitions`, `partial-orders`, `functions`,
`injective-surjective-bijective`, `composition-and-inverses`,
`cardinality-and-countability`, `the-pigeonhole-principle`. The course
declares course 1 as its only prerequisite ("quantifiers and proof
technique"), so it is judged against what `logic-and-proof` actually
teaches: `∀`/`→` and vacuous truth, direct proof of a conditional,
contraposition, the equivalence laws, and the `a | b` divisibility notation
from its lesson 12.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** The
  `standard` field names something the reader does: convert `{2, 4, 6, 8,
  10}` to set-builder and `{x ∈ ℤ : x² < 10}` to a roster, with the check
  "if you got seven you remembered the negatives" (`sets-and-membership`);
  translate `(A △ B) \ C` into a membership condition (`set-operations`);
  prove the symmetric-difference identity once by double inclusion and once
  by chaining laws (`set-identities`); describe the `P(A) ↔ {0,1}ⁿ`
  bijection in both directions (`cartesian-products-and-tuples`); write the
  matrix, the digraph and `R ∘ R` for a stated relation and check one
  presentation against another (`binary-relations`); name the witness for
  every verdict on five named relations (`properties-of-relations`); go
  from the partition `{{1,4}, {2}, {3,5}}` to its relation and back
  (`equivalence-relations-and-partitions`); draw the Hasse diagram of
  `P({a,b,c})` and find the least, greatest and an incomparable pair
  (`partial-orders`); name domain, codomain and image separately for
  `n ↦ n²` on `ℤ` (`functions`); classify `n² − n` with a witness for each
  failure (`injective-surjective-bijective`); invert a composition and
  check it against `f⁻¹ ∘ g⁻¹` (`composition-and-inverses`); run the
  diagonal argument from memory including why the digits 4 and 5 are chosen
  (`cardinality-and-countability`); invent the boxes for the ten-integers
  subset-sum problem (`the-pigeonhole-principle`). None of these is
  "understand X", and each is what the lesson's worked example demonstrated.
- **The labs compute rather than assert, and they name the witness.** The
  set lab evaluates both expressions from the current membership and shows
  the separating elements as a row, not a verdict; its status text says
  outright that one membership is "a failed attempt at a counterexample",
  which is the correct epistemics for `set-identities`. The relation lab
  decides each of the four properties by evaluating its definition and
  prints the offending pair — the exact discipline `properties-of-relations`
  step 4 and the standard demand — and reports equivalence classes only when
  all three properties hold, so the classes visibly cease to exist when one
  is broken (`equivalence-relations-and-partitions`' panel says this and it
  is true). The function lab names the colliding pair and the unhit element,
  and reports "no injection exists at all" from the sizes before the reader
  hunts, which is the pigeonhole principle in its bare form
  (`injective-surjective-bijective`, `the-pigeonhole-principle`). Warshall's
  closure is computed in the lab and proved in the text
  (`properties-of-relations`).
- **The set-operations-are-connectives correspondence is made load-bearing,
  not decorative.** `set-operations` gives the table (`∪`/`∨`, `∩`/`∧`,
  complement/`¬`, `\`/`∧¬`, `△`/`⊕`, `⊆`/`→`) and says "this is not an
  analogy"; `set-identities` then proves De Morgan for sets by applying De
  Morgan for propositions to the membership condition, and lists the laws
  beside course 1 lesson 5's. That is prerequisite order used as content,
  and it halves what has to be memorised, as the lesson says.
- **The worked examples are chosen to expose the error.** `set-operations`
  checks element 4 individually because it fails the first term and passes
  the second; `properties-of-relations` classifies "divides" and then shows
  antisymmetry failing over all of `ℤ` (`2 | −2`, `−2 | 2`); `partial-orders`
  draws the Hasse diagram of divisibility on `{1,2,3,4,6,12}` and explains
  why the edge `1 – 4` is absent; `functions` includes a rule stated through
  a representative and proves it well defined; `injective-surjective-bijective`
  classifies `2n + 3` on `ℤ` precisely so that "`|ℤ| = |ℤ|` and injectivity
  still did not give surjectivity" lands; `composition-and-inverses` tests
  the order-reversal law rather than asserting it, by computing both
  `f⁻¹ ∘ g⁻¹` and `g⁻¹ ∘ f⁻¹`; `the-pigeonhole-principle` explains why four
  quarters and not nine ninths.
- **Misconceptions are named at the point of error, and they are the real
  ones.** `∈` versus `⊆` (`sets-and-membership`, `subsets-and-power-sets`);
  `{∅}` read as empty; proving one inclusion and claiming equality; `A \ B =
  B \ A`; complementing without a universe; distributing a complement
  without flipping the operation; `A × B = B × A`; composing left to right
  (twice, for relations and for functions); antisymmetric read as "not
  symmetric" and irreflexive as "not reflexive"; checking reflexivity only
  on elements that appear in pairs; calling a relation an equivalence after
  two properties; minimal confused with least; image confused with codomain;
  deciding surjectivity without the codomain; `f⁻¹` written for a
  non-bijection; a proper subset "must be smaller"; dense confused with
  uncountable; diagonalising against one specific list; the pigeonhole
  conclusion read as probabilistic. Each is corrected with an instance.
- **Prerequisite order across the path is sound.** Every back-reference
  from a later course lands on a lesson that teaches what is cited: course
  4 lesson 1 cites `|A × B| = |A|·|B|` from lesson 5 and lesson 4 cites `2ⁿ`
  from lesson 2; course 4 lesson 13 cites lesson 11's criteria; course 6
  lessons 7 and 14 cite lesson 8's partition and lesson 10's
  well-definedness; course 7 lessons 5, 6 and 10 cite lessons 8 and 9; course
  6 lesson 12 cites lesson 14's pigeonhole. Inside the course, the modules
  (sets 1–5, relations 6–9, functions 10–12, counting 13–14) are in the only
  order that works, and `the-pigeonhole-principle` is correctly presented as
  lesson 11's cardinality theorem restated.
- **The proofs are right.** `∅ ⊆ A`; `|P(A)| = 2ⁿ`; inclusion–exclusion for
  two sets; De Morgan by double inclusion; both chain proofs; `|A × B| =
  |A|·|B|`; the composition example (`S ∘ R = {(1,1),(2,3)}`, `R ∘ S =
  {(2,2)}`); the successor powers and their union; Warshall's invariant;
  classes equal or disjoint (each property doing a distinct job, as the
  lesson notes); uniqueness of least; the finite injective-iff-surjective
  theorem; composition preserving both properties; inverses exist exactly
  for bijections and are unique; `ℤ` and `ℚ` countable; the generalised
  pigeonhole bound; the five-points worked example. The arithmetic checks
  (`26⁴ = 456 976`; `2⁹ = 512`; `⌈20/6⌉ = 4`; the Bell numbers `1, 1, 2, 5,
  15, 52, 203`; `√(½² + ½²) = √2/2`).

## What it teaches badly, or claims and does not deliver

### Order: an idea used one lesson before it is taught

1. **`subsets-and-power-sets` proves things about `∩` and `∪` one lesson
   before `set-operations` defines them.** The lesson's only worked example
   is "Prove `A ∩ B ⊆ A ∪ B`", whose lines read "By definition of
   intersection" and "By definition of union" — definitions the course has
   not given. The completion standard is "Prove `A ∩ (A ∪ B) = A` by double
   inclusion", the absorption law, using both operations. Meanwhile the
   lesson's own method (step 2: "If `A = {x : P(x)}`, then `x ∈ A` means
   `P(x)`. The proof is then a propositional argument from `P(x)` to
   `Q(x)`") describes a proof about set-builder sets — exactly what lesson 1
   just taught and what the reader has — and no example of that kind is
   given. The worked example does not demonstrate the method it sits under.
   This is the same class of defect the sibling assessment found in course
   1's `truth-tables`, and the repair is the same: work an example in the
   vocabulary the reader has (lesson 1's own set `{x ∈ ℤ : x = 3k + 1}`
   against a second description of it), keep the one-way-containment
   counterexample, and let lesson 3 own its operations.

### Facts a reader would trust that are wrong

2. **`binary-relations`: "there are `2^(n²)` relations on an `n`-element set
   — 512 on a three-element set, and over half a billion on a five-element
   one."** `2^(5²) = 2^25 = 33 554 432`, thirty-three million. "Over half a
   billion" is `2^29`. The 512 is right.
3. **`cardinality-and-countability`'s diagonal argument, as written, never
   diagonalises against the first entry of the list.** The list is
   `r₀, r₁, r₂, …`, the digits of `rₙ` are `dₙ₁dₙ₂dₙ₃…`, and `xₖ` is chosen
   against `dₖₖ` for `k = 1, 2, …`; the text then says `x` "differs from
   `r₁` in the first decimal place, from `r₂` in the second". Nothing
   handles `r₀`. The constructed `x` may equal `r₀`, and the proof has a
   hole — in the one argument the lesson's standard asks the reader to
   reproduce from memory. The fix is one character: index the list from
   `r₁`.
4. **`set-identities` contradicts itself about Venn diagrams, and the course
   home sides with the wrong half.** Concept 3 says a diagram "establishes
   nothing on its own"; the summary says it "illustrates without proving";
   the course outcome says "know that a Venn diagram illustrates an identity
   without proving it". The body says the opposite, correctly: "A three-set
   Venn diagram shows eight regions, which is every possible membership
   pattern, so shading it does establish a three-set identity", and quiz
   question 3 marks "proves it for three sets, since all eight membership
   regions appear" as the right answer and "proves nothing at all" as wrong.
   The body is right — an identity built from `∪ ∩ ‾ \` depends only on
   which region an element is in, so a check over all eight regions is a
   case proof — and what a diagram cannot do is generalise, be written as a
   chain of named steps, or handle four sets (the usual picture is missing
   regions). A reader who takes the concept card at face value fails the
   lesson's own quiz.
5. **Three cross-course references point at the wrong lesson.**
   `set-operations` sends the reader to "course 4 lesson 10" for
   inclusion–exclusion (that is lesson 9; lesson 10 is derangements);
   `the-pigeonhole-principle`'s note sends them to "course 4 lesson 12" for
   the generalised principle (lesson 11; lesson 12 is generating functions);
   `partial-orders` twice says "course 7 lesson 12 produces [topological
   sorts] from a directed graph" and "gives the algorithm" — course 7 lesson
   12 is spanning trees, and course 7's own home says topological sorting is
   only "noted where" it arises, which is lesson 8's depth-first search.
   `cartesian-products-and-tuples` twice calls the `P(A) ↔ {0,1}ⁿ` bijection
   "a preview of lesson 12's argument style" and "the pattern lesson 12
   formalises"; lesson 12 is composition and inverses. Bijection is defined
   in lesson 11 and made the definition of size in lesson 13.
6. `subsets-and-power-sets`' note promises "Cantor's theorem, which lesson 13
   proves for the case that matters". Lesson 13 states Cantor's theorem as a
   theorem box with no proof following it; what it proves is `|ℕ| < |ℝ|`,
   which is not a case of `|A| < |P(A)|` without a further bijection the
   course never gives. The four-line proof is the diagonal argument again
   (`D = {a : a ∉ f(a)}`), belongs in the lesson whose standard is "run the
   diagonal argument from memory", and costs no new idea.

### Distractors that are also true

The recurring failure the content package's own `AGENTS.md` warns about.
The quiz shows one explanation for every wrong answer, so a distractor that
is defensible is marked wrong with an explanation that does not address it.

7. **`partial-orders`, question 3: "A poset has three minimal elements. How
   many least elements can it have?"** with options "Three", "One", "Zero",
   "At most one, and here zero". The correct index is the last; option (c),
   "Zero", is exactly right for the poset described. A reader who reasoned
   correctly and answered "Zero" is told "Not quite".
8. **`injective-surjective-bijective`, question 2: "`|A| = 5`, `|B| = 7`.
   Which is impossible?"** Option (d) is "an injection `B → A`" — seven into
   five — which is impossible, and the `why` concedes it in a parenthesis
   ("also impossible, for the mirror reason — but the question asks for
   `A → B`"). The question does not ask for `A → B`; it asks which is
   impossible.
9. `set-identities`, question 2 ("To prove `A = B` by double inclusion you
   must show: … `A ∩ B = A ∪ B`") has a distractor the `why` admits "is
   actually equivalent to `A = B` as well", and the question itself tests
   nothing beyond the phrase "double inclusion". The lesson's named mistake
   3 — a chain step you cannot name — is never drilled; a question that asks
   which law licenses a given line of the lesson's own chain would test the
   act.

### Labs that do not agree with their own lessons

10. **`set-operations`' lab opens on lesson 4's identity.** The default pair
    is `A ∪ (B ∩ C)` against `(A ∪ B) ∩ (A ∪ C)` — the distributive law,
    which `set-identities` lists and proves. The lesson's own concept 3,
    example and mistake 1 are that `A \ B ≠ B \ A` and that their union is
    `A △ B`; the lab's "difference" row is literally `A △ B` of the two
    expressions. With `A \ B` against `B \ A` at the shipped membership the
    row reads `{1, 2, 3, 7, 8, 9}`, which is the lesson's example on the
    lab's numbers. The right lab is attached to the wrong default.
11. **`sets-and-membership`'s lab panel gives the reader nothing to do with
    this lesson's idea.** The lab compares expressions `A` and `B` and its
    status text speaks of identities and counterexamples (lesson 4's
    language). The lesson's single idea is extensionality, and the lab's
    "Equal?" figure is extensionality made visible — it reads "yes" exactly
    when the two membership lists agree, and the difference row lists what
    stops it. The panel does not say so.
12. **`binary-relations`' lab reports lesson 7's verdicts, unexplained.**
    The relation lab's property table (reflexive, irreflexive, symmetric,
    antisymmetric, transitive) and its status line ("Not an equivalence
    relation and not a partial order. Failing: …") are on the page one
    lesson before any of those words is defined. The panel could name them
    as next lesson's and point the reader at what is this lesson's: the
    matrix, and the transitive-closure selector, which completes the
    successor preset into `a < b` — the worked example's last line, on five
    elements instead of four.
13. **`subsets-and-power-sets` and `cartesian-products-and-tuples` borrow
    course 4's counting lab and the panels do not fence it.** The lab shows
    four rows — `nʳ`, `P(n, r) = n!/(n−r)!`, `C(n, r)`, `C(n+r−1, r)` —
    with factorial formulas the reader meets in course 4. Lesson 2's panel
    says "the C column" (it is a row) and describes a sum over `r` without
    asking the reader to do it; lesson 5's panel correctly identifies the
    `nʳ` row but says nothing about the other three. Neither says which rows
    belong to this course. The `P` row at `n = 3, r = 4` reads 0, which is
    lesson 5's worked example's second count, and the panel does not say so.
14. `functions`' lab panel says, correctly, that the control cannot build a
    non-function; it says nothing about the one figure on the lab that is
    this lesson's — "Image size `k / |B|`", which is image against codomain,
    the lesson's concept 2 and mistake 1. The property table underneath is
    lesson 11's.
15. `cardinality-and-countability`'s panel says "the lab enforces" `|A| =
    |B|` for a bijection. The lab enforces nothing; it reports that no
    injection or surjection exists when the sizes differ. "Reports" is what
    the lesson wants anyway — a verdict from counting, not a control that
    refuses.

### Quiz feedback that does not answer the wrong answer

16. The `why` fields are good where they are specific, and many name the
    distractors (`set-operations` Q3 on the double count;
    `composition-and-inverses` Q1 on the other order; `the-pigeonhole-principle`
    Q1 on birthdays and ages). Where they do not, the reader who picked a
    particular wrong answer gets a restatement of the rule:
    `sets-and-membership` Q1 says nothing about `∅ = {∅}`; `subsets-and-power-sets`
    Q1 says nothing about `{2} ⊆ A` (false because `2 ∉ A`) or `{1} ∈ A`;
    `set-operations` Q1 says nothing about `{1,2,3,4}` (the union) or
    `{1,2}` (`A \ B` alone); `cartesian-products-and-tuples` Q2 says "the
    first three are all false" without a reason each; `binary-relations` Q1
    says nothing about 9 (that is `|A × A|`, the pairs, not the relations);
    `properties-of-relations` Q1 says nothing about why `≤` and "divides"
    fail symmetry or why `=` is transitive;
    `equivalence-relations-and-partitions` Q3 says nothing about 8 (`2³`)
    or 512 (all relations); `partial-orders` Q3 after repair needs to say
    why "three" is wrong; `injective-surjective-bijective` Q2 after repair
    needs to say why a surjection `B → A` is fine.

### Cognitive load and structure

17. **`properties-of-relations` carries the four properties and the three
    closures, with Warshall's algorithm proved.** By the one-hard-idea rule
    it is the strongest split candidate in the course. I have chosen not to
    split it: the closures are "repair" for the properties, the lab shows
    both on one grid (the amber cells are the closure of the relation whose
    verdicts sit underneath), the worked example in `binary-relations` has
    already computed a transitive closure by hand, and the quiz keeps its
    weight on the properties (two of three questions) with the third on the
    closure bound. Recorded as a judgement.
18. `cardinality-and-countability` is the heaviest page and the course home
    says so ("Pay attention to lesson 13"). Four theorems, two of them
    surprising. Adding the four-line proof of Cantor's theorem (item 6) is
    justified because it is the diagonal argument a second time, not a fifth
    idea, and the `read_intro` — "the three positive results, and the one
    negative one" — miscounts what is on the page (two positive theorems, a
    third in the worked example, two negative). Not split.
19. `set-identities` teaches two proof routes and when to pick each; that is
    one idea (the choice) and the lesson says so in its method. Not split.
20. The course home's `how_to` says to "use the relation lab as a
    counterexample machine … a three-element example", but every relation
    lab on the course is five elements, and a reader who builds a
    three-element example leaves elements 4 and 5 with no loops, so
    reflexivity fails for a reason unrelated to the claim being tested. The
    advice is right and needs one sentence about starting from the empty
    preset and remembering the untouched elements. The `footer_lead` says
    "a property that holds on the twelve elements you can see", which is the
    set lab; the relation lab has five and the function lab at most six.
21. The course outcomes name four acts and omit the pigeonhole principle,
    which is one of the two lessons the syllabus says "course 4 builds on"
    and whose standard ("invent the boxes yourself") is the most transferable
    act in the course.

## Where a learner gets stuck

- At `subsets-and-power-sets`' worked example, at "by definition of
  intersection", with no definition of intersection to look up (item 1);
  and again at its standard, asked to prove absorption before meeting `∩`.
- At `set-identities`' concept card versus its quiz: the card says a
  diagram proves nothing, the quiz marks that answer wrong (item 4).
- At `binary-relations`' lab, reading "antisymmetric: no" and "Not an
  equivalence relation and not a partial order" one lesson early (item 12).
- At `cardinality-and-countability`'s standard, reproducing the diagonal
  argument from a text whose list starts at `r₀` and whose diagonal starts
  at `r₁` (item 3).
- At `partial-orders` question 3, having answered "Zero" for the right
  reason (item 7); at `injective-surjective-bijective` question 2, having
  answered that an injection `B → A` is impossible, which it is (item 8).
- At `subsets-and-power-sets`' lab, in front of `n!/(n−r)!` two courses
  early with no sentence saying which row is theirs (item 13).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every edit is in
`content/discrete_math/c2_sets/` and the pages are rebuilt from it. Each
figure a panel now states was recomputed by hand from the lab's shipped
membership and presets (`A = {1,…,6}`, `B = {4,…,9}`, `C = {2,3,6,7,10,11}`;
successor and `<` on `{1,…,5}`; the `C(4, r)` row).

- `subsets-and-power-sets`: worked example rebuilt as a double-inclusion
  proof that lesson 1's set `{x ∈ ℤ : x = 3k + 1}` equals
  `{x ∈ ℤ : x = 3m − 2}` — each direction unfolds a set-builder condition
  and rewrites, which is the method's step 2 and course 1's direct proof —
  followed by `{x : 6 | x} ⊆ {x : 3 | x}` with `3` refuting the reverse;
  standard changed to the odd integers described two ways
  (`2k + 1` against `2m − 1`); the absorption law is now met in lesson 4,
  where `∩` and `∪` exist; the counting-lab panel names the `C` row as this
  lesson's and the other three as course 4's, and asks for the sum
  `1 + 4 + 6 + 4 + 1 = 16 = 2⁴` with the slider; the note now says lesson
  13 proves Cantor's theorem in four lines, which it now does; question 1's
  `why` answers `{2} ⊆ A` and `{1} ∈ A`.
- `set-operations`: lab default changed to `A \ B` against `B \ A`, with a
  panel that says the difference row is `A △ B`, reads `{1, 2, 3, 7, 8, 9}`
  at the shipped membership, and invites the reader to move 4 into `A` only
  and watch it join; the inclusion–exclusion pointer now says course 4
  lesson 9; question 1's `why` answers the union and `A \ B`; question 3's
  `why` answers 14 and 9.
- `set-identities`: concept 3, summary and `one_line` reconciled with the
  body and the quiz — a three-circle diagram correctly shaded is a case
  check over all eight regions and does establish a three-set identity; it
  cannot generalise, cannot be written as named steps, and the four-circle
  picture is missing regions; question 2 replaced by "which law licenses
  `A ∩ (Ā ∪ B̄) = (A ∩ Ā) ∪ (A ∩ B̄)`" with De Morgan, absorption and
  complement as the distractors, each answered; the lab panel points at
  `Ā ∪ B̄` in the second dropdown as the wrong De Morgan the difference row
  separates.
- `sets-and-membership`: lab panel rewritten around extensionality — the
  "Equal?" figure reads yes exactly when `A` and `B` have the same members,
  the difference row names what stops it, and the reader is asked to make
  them equal by cycling; question 1's `why` answers `∅ = {∅}`; question 3's
  `why` names the domain.
- `cartesian-products-and-tuples`: the two references to "lesson 12" now
  point at lesson 11 (bijection) and lesson 13 (bijection as size); the
  counting-lab panel fences the other three rows as course 4's and points
  out that at `r = 4` the `nʳ` row reads 81 and the `P` row reads 0 — the
  worked example's two counts; question 2's `why` gives a reason for each
  of the three false options.
- `binary-relations`: "over half a billion" corrected to "over thirty-three
  million" (`2^25 = 33 554 432`); the lab panel names the property table
  and the status line as lesson 7's, tells the reader to read the grid as
  the matrix now, and to choose the transitive closure to see the amber
  cells complete `b = a + 1` into `a < b` on five elements; question 1's
  `why` says what 9 counts.
- `properties-of-relations`: the lab panel now says what the `a < b` preset
  fails (reflexivity only) and that the reflexive closure turns it into
  `≤`, a partial order; question 1's `why` answers each of `=`, `≤` and
  "divides".
- `equivalence-relations-and-partitions`: question 3's `why` answers 8, 512
  and 3.
- `partial-orders`: question 3's options rebuilt so that only one is right
  ("None: a least element would be comparable to all three, so it would be
  the only minimal element"), with "three, one for each minimal", "exactly
  one, the smallest of the three" and "it depends on whether the poset is
  finite" as distractors, each answered; the two topological-sort pointers
  now say course 7 lesson 8 (depth-first search) notes where one comes
  from, matching what course 7 does.
- `functions`: lab panel now points at the image-size figure as this
  lesson's (image against codomain), asks the reader to make two arrows
  collide and watch it drop below `|B|`, and names the property table as
  lesson 11's.
- `injective-surjective-bijective`: question 2's option (d) replaced by
  "a surjection `B → A`", which exists; the `why` says why and no longer
  apologises for the question.
- `cardinality-and-countability`: the diagonal argument's list now starts
  at `r₁`, so `x` differs from `rₖ` in the `k`th place for every entry;
  Cantor's theorem now has its proof (`D = {a ∈ A : a ∉ f(a)}`, `d ∈ D ⟺
  d ∉ D`), introduced as the diagonal argument a second time; `read_intro`
  counts what is on the page; the lab panel says "reports", not "enforces".
- `the-pigeonhole-principle`: the note's pointer now says course 4 lesson
  11.
- Course home (`__init__.py`): outcome 1 now says when a Venn diagram is a
  case check and when it is only a picture; a fifth outcome names the
  pigeonhole act (invent the classification, count both sides); `how_to`
  item 2 tells the reader to start from the empty preset and that the
  untouched elements still count for reflexivity; `footer_lead` no longer
  says "twelve elements" of labs that have five.
