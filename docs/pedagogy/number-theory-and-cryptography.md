# Pedagogy assessment — Number Theory and Cryptography (discrete mathematics, course 6)

First assessment, formed from the fourteen lesson dicts in
`content/discrete_math/c6_number_theory/` (`part_a.py`, `part_b.py`,
`__init__.py`) and the two labs they render through in
`scripts/mathpath/labs/number.py` (the ten-mode number-theory workbench and
the RSA lab), as they stand on `main` at 79f8d0e. No prior assessment exists
for this course.

This is a generated course: the source is the content package, and every
finding below cites a lesson slug and the field it lives in. Lessons, in
course order: `divisibility-and-the-division-algorithm`,
`primes-and-factorisation`, `the-sieve-of-eratosthenes`,
`greatest-common-divisor`, `the-euclidean-algorithm`,
`bezout-and-modular-inverses`, `modular-arithmetic`,
`modular-exponentiation`, `linear-congruences`,
`chinese-remainder-theorem`, `fermat-and-euler`,
`hashing-and-pseudorandom-numbers`, `classical-ciphers`, `rsa-encryption`.
The course declares courses 1–3 as prerequisites ("proof technique and
induction") and points into courses 2, 4 and 5 as well, so it is judged
against what those teach: well-ordering (course 3 lesson 1), strong
induction (course 3 lesson 5), Binet's formula and `φⁿ` growth (course 3
lesson 10), loop invariants (course 3 lesson 12), equivalence relations and
partitions (course 2 lesson 8), well-definedness of a rule on classes
(course 2 lesson 10), the pigeonhole principle (course 2 lesson 14), the
product rule (course 4 lesson 1), inclusion–exclusion (course 4 lesson 9)
and the birthday problem (course 5 lesson 2). Every one of those pointers
was checked against the lesson it names and every one resolves. Every
figure quoted below was recomputed in exact integer arithmetic, and every
lab figure by executing the shipped JavaScript at the shipped preset.

## What the course teaches well

- **Every lesson closes on an act, and the act is the right one.** Prove
  `d | b` from `d | (a + b)` and `d | a` (`divisibility-and-the-division-
  algorithm`); factor 2520 and predict 48 divisors before listing
  (`primes-and-factorisation`); name the passes and the stopping point before
  sieving to 200 (`the-sieve-of-eratosthenes`); compute a gcd and an lcm
  without factoring (`greatest-common-divisor`); predict the step count of
  `gcd(144, 89)` before running it (`the-euclidean-algorithm`); produce
  `7⁻¹ mod 26` (`bezout-and-modular-inverses`); reduce before multiplying
  (`modular-arithmetic`); trace `5^117 mod 19` on paper
  (`modular-exponentiation`); state the solution count of `15x ≡ 25 (mod 35)`
  before finding one (`linear-congruences`); construct rather than search
  (`chinese-remainder-theorem`); reduce the exponent first
  (`fermat-and-euler`); check three divisibility conditions
  (`hashing-and-pseudorandom-numbers`); break an affine key from two
  frequencies (`classical-ciphers`); build a key and say what each step
  assumes, then break it (`rsa-encryption`). None is "understand X".
- **The course has one spine and says so at every joint.** `a = qb + r`
  is proved from well-ordering in lesson 1, and the linear-combination
  property `d | a, d | b ⟹ d | (ax + by)` is named there as "the step that
  appears in nearly every argument" — and it is: it proves consecutive
  integers coprime (lesson 4), the key identity of Euclid (lesson 5), the
  transitivity of congruence (lesson 7), and it is the whole of the
  infinitude-of-primes proof (lesson 2). Bézout is proved from
  well-ordering, Euclid's lemma from Bézout, and lesson 6 turns round to
  say that lesson 2's fundamental theorem therefore rests on it: "the most
  familiar fact in the course has the deepest justification".
- **The gcd/factoring asymmetry is taught as the point, not as a remark.**
  Lesson 4 gives the factorisation formula and immediately says it is not
  the method; lesson 5's worked example counts three divisions against
  eight; lesson 14's security argument is the same asymmetry at 2048 bits,
  and its lab breaks its own key by trial division to show that only size
  protects it.
- **The misconceptions named are the real ones, at the point of error.**
  A negative remainder and the `%` operator; "Euclid's `N` is always
  prime", refuted with `30031 = 59 · 509`; sieving past `√n`; the product
  identity extended to three numbers (`gcd(2,4,8) · lcm(2,4,8) = 16`);
  cancelling without checking the gcd (`2·3 ≡ 2·8 (mod 10)`); reducing an
  exponent modulo `m`; reporting one solution of a congruence that has
  `g`; dividing only the coefficient by `g`; inverting `Mᵢ` modulo the
  wrong thing; applying Fermat to a non-coprime base (`2^{φ(4)} ≡ 0`);
  reading a Fermat pass as a primality proof (561); a power-of-two hash
  modulus; a full-period LCG taken as statistically good; a large key
  space taken as security; reusing a one-time pad; leaking `φ(n)`; equal
  or close primes; deploying textbook RSA.
- **The honesty about RSA is exactly right.** Security is "believed and
  not proved"; it is unproved that breaking RSA requires factoring; Shor's
  algorithm is named; textbook RSA is deterministic and not deployable;
  `not_covered` on the course home says the same. The RSA lab computes
  everything from the four inputs in BigInt and refuses non-primes, equal
  primes, an `e` not coprime to `φ(n)`, and `m ≥ n`, each with the reason.
- **The numbers are almost all right.** `−17 mod 5 = 3`, `30031 = 59·509`,
  the prime-count table to a million with `n/ln n = 72 382` and `li = 78 628`,
  one in 230 near `10¹⁰⁰`, `360 = 2³·3²·5` with 24 divisors, `48/180`,
  `84/264` both routes, `gcd(1071, 462) = 21` and its factorisations,
  `gcd(89, 55)` in nine divisions, `1071·(−3) + 462·7 = 21`,
  `17·2753 = 15·3120 + 1`, casting out nines on `4321 × 5678 = 24 534 638`,
  `7^100` ending in 1 with 85 digits, `7^128 ≡ 3 (mod 13)`, the eight-row
  table for `3^200 mod 50`, `x ≡ 4, 9, 14`, `x ≡ 19`, `45` and `95`, Sun
  Tzu's 23, `9 (mod 12)`, `φ(3120) = 768`, `3^{1234567} ≡ 87 (mod 100)`
  with over half a million digits, both LCG sequences, `H → R` and back,
  the recovered key `(15, 9)`, `n = 3233`, `d = 2753`, `65 → 2790 → 65` —
  all recomputed and all correct. The exceptions are items 1–3 below.

## What it teaches badly, or claims and does not deliver

### Facts a reader would trust that are wrong

1. **`rsa-encryption`'s worked example ships a wrong ciphertext and a
   false decryption.** The lines read `126·81 = 10206 ≡ 48; 48·9 = 432 ≡ 3
   (mod 143)`, `c = 3`, and `decrypt: 3^103 mod 143 = 9 ✓`. In fact
   `10206 = 71·143 + 53`, so `126·81 ≡ 53`, `53·9 = 477 ≡ 48`, and
   `9^7 mod 143 = 48`; `3^103 mod 143` is 16, not 9. The page's own lab,
   set to `p = 11, q = 13, e = 7, m = 9`, prints `c = 48` — so the worked
   example and the lab under it disagree, on the lesson whose `footer_lead`
   promises exact arithmetic. `48^103 mod 143 = 9` does hold, so the example
   is repairable in two lines.
2. **`fermat-and-euler`'s first mistake illustrates the error with a case
   where it makes no difference.** "Reducing the exponent modulo `m` … For
   `m = 100` those are 100 and 40, and the answers differ." They do not:
   every unit modulo 100 has order dividing 20, which divides 100, so for
   any coprime base `a^k ≡ a^{k mod 100} (mod 100)` always holds. On the
   lesson's own worked example, `1234567 mod 100 = 67` and `3^67 ≡ 3^7 ≡ 87`
   — the reader who tests the claim on the example above it finds the two
   methods agree and the mistake box wrong. `2^10 mod 7` separates them
   (`2^3 = 8 ≡ 1` by the wrong rule, `2^4 = 16 ≡ 2` by the right one,
   `1024 = 146·7 + 2`).
3. **`modular-exponentiation` gives three different counts for the same
   computation.** The `key` block says "`7^128 mod 13` in 8 squarings"; the
   body's example says "seven squarings give `7^128 ≡ 3`" (right: `2⁷ = 128`);
   the worked example's table lists seven squarings from `3^1` to `3^128` and
   then says "8 squarings and 3 multiplications"; the standard says
   `5^117 mod 19` takes "seven squarings" when `117 < 128` needs six; and the
   lab's KPI reports `2 × rows = 16` "multiplications" for the preset, with
   a status line that says `7^128` "would be an integer with thousands of
   digits" (it has 109).

### Labs that do not agree with their own lessons

4. **`classical-ciphers`' panel gives an instruction the lab refuses.** "Set
   the modulus to 26 and look at the multiplication table" — the `modtable`
   mode rejects any modulus above 16 ("Choose a modulus between 2 and 16 so
   the tables fit") and the page opens on `m = 12`. Nothing on the page
   encrypts a letter, checks `gcd(a, 26)`, or shows the two-to-one collapse
   the lesson's first mistake describes.
5. **`bezout-and-modular-inverses` promises a trace and prints a row.** The
   body says "the iterative form maintains the coefficients as it goes …
   it is what the lab runs and what every implementation uses"; the course
   home's `how_to` says "each mode prints the algorithm's trace rather than
   only its answer". The `bezout` mode prints one row — `a, b, x, y, gcd,
   check` — with no intermediate line. And its panel says "note that `x` is
   then the inverse of `a` modulo `b`" while the lab prints `x = −367` for
   the worked example's `(17, 3120)`, the unreduced coefficient the lesson's
   own first mistake warns about, and never shows 2753.
6. **`chinese-remainder-theorem`'s lab cannot show the lesson's central
   misconception.** The `crt` mode takes `m` and uses `m` and `m + 1`, so
   the moduli are always coprime by construction. The body's "Coprimality
   is not optional" section — the inconsistent `x ≡ 1 (mod 4), x ≡ 2 (mod 6)`
   and the consistent-but-modulo-the-lcm `x ≡ 1 (mod 4), x ≡ 3 (mod 6)` —
   cannot be entered, nor can Sun Tzu's `3, 5, 7` or the standard's
   `5, 7, 9`. The one case the lab can never produce is the one the first
   mistake names.
7. **`hashing-and-pseudorandom-numbers` has no lab that runs a generator.**
   The page shows the `modtable` with a panel saying repeated values in a
   composite row are "exactly the clustering a bad hash modulus produces",
   which is a metaphor rather than a demonstration. The worked example is
   two LCG runs at `m = 16` and the standard asks the reader to find
   parameters at `m = 100` that pass and fail Hull–Dobell; nothing on the
   page iterates `x ↦ (ax + c) mod m`, reports a period, or checks the
   three conditions.
8. **`fermat-and-euler`'s lab counts `φ(m)` by brute force**, looping
   `1 … m − 1` with a BigInt gcd each — enter `m = 10⁸` and the tab freezes
   — while the lesson's step 2 says to compute `φ` "from the factorisation
   of `m`, using multiplicativity". The lab opens on `a = 3, m = 7`, which
   is in neither the body (`7^1000 mod 13`, `2` modulo `4`) nor the worked
   example.
9. **`greatest-common-divisor` opens on the standard's exercise.** The lab
   preset is `(1071, 462)` — the pair the completion standard asks the reader
   to compute — with the panel saying "Enter two large numbers"; the lesson's
   own worked example, `gcd(84, 264) = 12` in two divisions, is not on the
   lab. `divisibility-and-the-division-algorithm` likewise opens on `(1071,
   462)` and asks the reader to "try a negative `a`" when its example is
   `−7 = (−3)(3) + 2`.
10. The panels on `primes-and-factorisation`, `the-sieve-of-eratosthenes`,
    `the-euclidean-algorithm`, `modular-arithmetic`, `linear-congruences`
    and `rsa-encryption` describe the lab correctly and quote none of its
    figures, so the reader is not told what to look for. Executed at the
    shipped presets: `360 = 2³ · 3² · 5` with 24 in the corner; 25 primes to
    100, with 91 "first crossed out as a multiple of 7"; three rows to
    `gcd = 21`; in `ℤ_12` the row for 4 reads `0, 4, 8` repeating and
    `4 · 3 = 0`; `x = 4, 9, 14` with "spaced 5 apart"; `65 → 2790 → 65`
    and the factor 53 recovered in the status line.

### Order: things used before they are taught

11. **`divisibility-and-the-division-algorithm`'s worked example borrows
    lesson 7's notation** — `10ⁱ ≡ 1 (mod 3)`, `n ≡ Σ dᵢ (mod 3)` — and says
    so ("arriving early because it makes the argument short"). The lesson's
    own property proves the digit-sum test directly: `10ⁱ − 1 = 99…9 =
    9 · 11…1` is a multiple of 3, so `n − (digit sum) = Σ dᵢ(10ⁱ − 1)` is a
    linear combination of multiples of 3, and `3 | n ⟺ 3 | digit sum` by
    `d | a, d | b ⟹ d | (a ± b)`. That is the property the standard then
    asks the reader to apply, demonstrated instead of deferred.
12. `primes-and-factorisation` proves uniqueness with Euclid's lemma from
    lesson 6. The forward reference is stated in the proof and closed in
    lesson 6, and the alternative — Bézout before primes — would put the
    sieve after the gcd. I have left the order and kept the note; the
    reader is told exactly what is owed and where it is paid.
13. Well-ordering is used in lessons 1 and 6 without naming course 3
    lesson 1, and strong induction in lesson 2 without naming course 3
    lesson 5.

### Distractors that are also true, and feedback that does not answer

14. **`modular-arithmetic` Q1 asks "`17 ≡ ? (mod 5)`" and offers 3, 2, 12,
    17.** `17 ≡ 12 (mod 5)` and `17 ≡ 17 (mod 5)` are both true
    congruences; only the operator `17 mod 5` has one answer, and the
    question does not ask for it.
15. **`divisibility-and-the-division-algorithm` Q2 offers "`d | ab` only"**
    as a wrong answer to "`d | a` and `d | b`. What follows?". `d | ab` does
    follow; the option is wrong only because of the word "only", which is a
    trick rather than a misconception.
16. **`linear-congruences` Q3 asks "When is the solution unique modulo
    `m`?"** and offers "when `m` is prime": for a prime modulus and
    `a ≢ 0` the solution is unique, so the reader can argue for it. The
    intended answer is the iff, and the question should say "exactly when".
17. Of the 42 `why` fields, almost all restate the rule and name no
    distractor. The reader who chose `−2` for `−17 mod 5` is not told it is
    what a truncating `%` returns, nor that 2 is `17 mod 5` with the sign
    dropped; who chose 36 for `gcd(12, 18)` is not told it is the lcm; who
    chose 14 for `φ(15)` is not told it is `m − 1`, Fermat's exponent
    applied to a composite; who chose "one solution mod 12" for the
    inconsistent system is not told that is the answer for remainders 1 and
    3; who chose "`m` is prime" for the inverse criterion is not shown 5
    invertible modulo 12; who chose "always prime" for Euclid's `N` is not
    shown `2·3 + 1 = 7` against `30031`; who chose 74 for the trial-division
    bound is not told it is `149/2` — none is answered.

### Misconceptions not named

18. **`greatest-common-divisor` never says that coprime numbers need not
    be prime.** "Coprime means no shared factor" is defined, and lesson
    10's Q1 `why` says "4 and 9 work fine", but the confusion of *coprime*
    with *prime* is the commonest error on the word and it is not named
    where the word is introduced.
19. **`rsa-encryption` never says `e` need not be prime.** The key-generation
    block requires `gcd(e, φ(n)) = 1`, the steps recommend 65537, and the
    lab's error message says "Try 17, or any prime that does not divide
    `φ(n)`"; a reader comes away believing primality of `e` is the
    requirement. 65537 is chosen prime because a prime is coprime to
    `φ(n)` unless it divides it (one check) and has two set bits (cheap
    `m^e`), and that reason should be on the page.

### Cognitive load and structure

20. `classical-ciphers` carries four ciphers (shift, affine, Vigenère,
    one-time pad) and VENONA. I have chosen not to split it: the act is one
    (validate and break an affine key), the worked example and the standard
    both measure it, and the shift and Vigenère are context for the two
    design requirements the summary names. What was wrong was the lab (item
    4), which one new mode repairs.
21. `fermat-and-euler` carries the totient, its formula, Euler, Fermat, the
    exponent rule and primality testing. The standard confines itself to the
    exponent rule and the key block to the four lines that matter; not
    split.
22. The course home lists four outcomes and omits the acts lessons 12 and
    13 close on — choose a hash modulus, check an LCG's period conditions,
    validate an affine key and break it — though `syllabus_intro` gives
    those lessons a third of the applications block. Its `how_to` promise
    that "each mode prints the algorithm's trace" is false for `bezout`
    (item 5).

## Where a learner gets stuck

- At `rsa-encryption`'s worked example, multiplying `126 · 81` by hand and
  getting 53 where the page says 48, then setting the lab to the same key
  and reading `c = 48` (item 1).
- At `fermat-and-euler`'s mistake box, testing "the answers differ" on the
  example above it and finding they do not (item 2).
- At `modular-exponentiation`, counting the squarings in the worked table
  (seven) against the caption (eight) and the lab (sixteen) (item 3).
- At `classical-ciphers`' lab, typing 26 and being refused (item 4).
- At `bezout-and-modular-inverses`' lab, looking for the trace the body
  says it runs, and reading `x = −367` where the panel promised the inverse
  (item 5).
- At `chinese-remainder-theorem`'s lab, trying to enter 4 and 6 (item 6).
- At `modular-arithmetic` Q1, having answered 12, which is a true
  congruence (item 14).
- At `divisibility-and-the-division-algorithm`'s worked example, meeting
  `≡ (mod 3)` six lessons early (item 11).

## Repairs made in this pass

All within the existing URL space; no lesson added, removed, renamed or
reordered, so the five URL declarations are untouched. Every content edit
is in `content/discrete_math/c6_number_theory/` and the fifteen pages under
the slug (fourteen lessons and the course home) are rebuilt from it. The
lab changes are in `scripts/mathpath/labs/number.py`; the arithmetic they
rest on (`NT_JS`: gcd, extended Euclid with its trace, modular power with
its trace, inverse, trial-division factorisation, totient, divisor count,
the two-modulus Chinese remainder solver for any moduli, the LCG runner,
the Hull–Dobell checks and the affine map) is now exercised by a
number-theory section in `scripts/mathcheck.js`, which was shown to fail
when the totient was deliberately broken and passes with it restored.
Every figure a panel now states was obtained by executing the shipped lab
JavaScript at the shipped preset.

Lab core (`number.py`):

- The workbench takes `a`, `b`, `m` and `n` presets in its config, so each
  lesson opens on its own example instead of `(1071, 462)`.
- A fourth input, relabelled per mode, so the Chinese remainder mode takes
  two remainders and two arbitrary moduli: coprime moduli show the
  lesson's construction (each term vanishing modulo the other modulus);
  non-coprime moduli are checked for consistency modulo the gcd and, when
  consistent, solved modulo the lcm with the status line saying why the
  product is the wrong modulus.
- `bezout` prints the extended algorithm's rows — `r, q, s, t` and the
  check `a·s + b·t = r` on every line — and, when the gcd is 1, reduces the
  coefficient into `[0, b)` and names it as the inverse.
- `modexp` counts what it did: squarings (`rows − 1`) and multiplications
  (one per set bit), and reports how many digits `a^b` itself would have.
- `fermat` computes `φ(m)` from the factorisation and prints the product
  formula it used, shows the powers up to `φ(m) + 1` so the return to 1 and
  the wrap-around are both on the page, and names the order of `a`.
- A new `lcg` mode: the sequence from a seed, the index where it first
  repeats, the period, and the three Hull–Dobell conditions each marked.
- A new `affine` mode: the 26-letter map as chips, collisions marked, the
  gcd, the inverse multiplier and the decryption rule.
- `factor` and `fermat` refuse inputs above `10¹²`, and the RSA lab refuses
  primes above `10⁷`, so trial division finishes instead of freezing the
  page; each refusal says why, which is lesson 14's point.

Lessons:

- `divisibility-and-the-division-algorithm`: the worked example proves the
  digit-sum test from the linear-combination property alone, with the
  congruence notation deferred to lesson 7; Q2's distractors are `ab | d`,
  `d = gcd(a, b)` and `a | b`, each refuted by `d = 1, a = 4, b = 6`;
  well-ordering points at course 3 lesson 1; the lab opens on `−7 ÷ 3`
  with the panel reading `q = −3, r = 2` and sending the reader to `−8`
  and `−9`; every `why` answers each distractor.
- `primes-and-factorisation`: strong induction points at course 3 lesson 5;
  the panel reads `2^3 · 3^2 · 5` and 24 and asks for 2520 with 48 predicted;
  every `why` answers each distractor, including `74 = 149/2` and `2·3 + 1
  = 7` against `30031`.
- `the-sieve-of-eratosthenes`: the panel reads 25 primes, 91 removed by 7,
  and sends the reader to `N = 30` for the worked example's ten; every
  `why` answers each distractor.
- `greatest-common-divisor`: the coprime definition says 8 and 9 are
  coprime and neither is prime; the lab opens on `(264, 84)`, the worked
  example, two divisions to 12; every `why` answers each distractor,
  including 36 as the lcm and `(4, 60)` against `(12, 20)`.
- `the-euclidean-algorithm`: the panel reads three rows to 21, sends the
  reader to `(89, 55)` for nine rows, then to `(890, 550)` for the same
  nine; the standard names `144 = F₁₂`, `89 = F₁₁`; every `why` answers
  each distractor, with `gcd(7, 3)` in two steps against the "two primes"
  option.
- `bezout-and-modular-inverses`: the lab opens on `(17, 3120)` with the
  trace, the panel reading the last nonzero row `1 = 17·(−367) + 3120·2`
  and the reduced 2753, and sending the reader to `(1071, 462)` for the
  body's `(−3, 7)`; every `why` answers each distractor, with 2 modulo 4,
  5 modulo 12 and 3 modulo 6 as the three counterexamples.
- `modular-arithmetic`: Q1 asks for `17 mod 5`; the panel reads the row for
  4 in `ℤ_12` and `4 · 3 = 0`, and sends the reader to `m = 7`; every `why`
  answers each distractor, including `a ≡ b (mod 3)` as what cancellation
  by 6 does give modulo 9.
- `modular-exponentiation`: the key block, the worked example's caption
  and the standard count seven, seven and six squarings; the cost paragraph
  says the last squaring is unused; the panel reads eight rows, seven
  squarings and one multiplication, and sends the reader to `(3, 200, 50)`
  for the worked table; every `why` answers each distractor, with
  `1000 = 1111101000₂` and its six set bits.
- `linear-congruences`: Q3 says "exactly when" and its `why` gives `6x ≡ 9
  (mod 15)` against "always" and `6x ≡ 1 (mod 15)` against `b = 1`; the
  panel reads 4, 9, 14 spaced 5 apart and sends the reader to `b = 7` and to
  `(14, 30, 100)`; every `why` answers each distractor.
- `chinese-remainder-theorem`: the lab opens on `x ≡ 2 (mod 3), x ≡ 3 (mod
  5)` giving 8 modulo 15; the panel sends the reader to `(1, 2; 4, 6)` for
  the inconsistent system, `(1, 3; 4, 6)` for 9 modulo 12, and `(8, 2; 15,
  7)` to finish Sun Tzu at 23; every `why` answers each distractor.
- `fermat-and-euler`: the first mistake uses `2^10 mod 7`; the lab opens on
  `(7, 13)`, the body's example, with the panel reading the return to 1 at
  `e = 12`, the row `e = 4` as 9, and the `φ` formula in the status line,
  and sending the reader to `(2, 4)`; every `why` answers each distractor,
  with 14 as Fermat's exponent on a composite.
- `hashing-and-pseudorandom-numbers`: the lab is the LCG at the worked
  example's `(5, 3, 16, 1)`, the panel reading period 16 and three passes,
  sending the reader to `a = 6` for `1, 9, 9, 9` and the failed second
  condition, then to `m = 100` for the standard; the pigeonhole pointer
  names course 2 lesson 14; every `why` answers each distractor.
- `classical-ciphers`: the lab is the affine map at the body's `(5, 8)`,
  the panel reading `H → R`, `5⁻¹ ≡ 21` and 26 distinct outputs, sending the
  reader to `a = 13` for two outputs and to `(15, 9)` for `E → R, T → I`;
  the standard gives `(3, 24)` to check against; every `why` answers each
  distractor.
- `rsa-encryption`: the worked example reads `126·81 = 10206 ≡ 53`,
  `53·9 = 477 ≡ 48`, `c = 48`, `48^103 mod 143 = 9`; step 3 says `e` need
  not be prime and why 65537 is chosen; the standard gives `e = 3`,
  `d = 235` to check against; the panel names the textbook figures and says
  how to reproduce the worked example's 48 on the lab; every `why` answers
  each distractor.
- Course home (`__init__.py`): a fifth outcome names the acts of lessons
  12 and 13; `outcomes_intro` includes it; `how_to` says every workbench
  mode opens on its lesson's own example and which lessons carry which
  mode.
