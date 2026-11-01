"""Parallel, Matrix, Linear and Number Algorithms, lessons 6-7 -- Chapter 31.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Chapter 31, Number-Theoretic Algorithms, sections 31.1-31.8
(pp. 926-975), with 31.9 named. Every quotation is copied from the operator's
copy with its printed page in the comment beside the lesson. The numbers are
written for these lessons; the book's examples (gcd(99, 78), 14x = 30
(mod 100), the CRT modulo 65, RSA with p = 11 and q = 29, a = 7 against
n = 561) and its exercises are not used. Every figure the prose attributes to
a lab was read off the running kit.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS 31.1-31.6, pp. 926-958. Quote: printed p. 926, 15 words,
    # quotes.py OK. Lesson total: 15 words. Lab: number, mode bezout, with
    # the lesson's a = 1147 and b = 851; the same panel's euclid, congr, crt
    # and modexp modes are used in the prose. Input size in bits (p. 927);
    # Euclid, Lemma 31.10, Lame's theorem 31.11, the Fibonacci worst case and
    # O(lg b) calls (pp. 933-936); EXTENDED-EUCLID (pp. 937-938); groups,
    # Z_n^*, Euler's phi (pp. 939-945); Theorem 31.20 and Corollaries,
    # MODULAR-LINEAR-EQUATION-SOLVER (pp. 946-950); the Chinese remainder
    # theorem, Theorem 31.27 (pp. 950-953); MODULAR-EXPONENTIATION, its
    # invariant, O(beta) operations (pp. 954-958).
    {
        "slug": "number-theoretic-algorithms",
        "title": "GCD and Modular Arithmetic",
        "module": "Chapter 31 · Number-Theoretic Algorithms",
        "one_line": "Euclid's algorithm finds a gcd in a number of steps proportional to the number of digits, its extended form writes the gcd as a combination of the inputs, and that combination solves modular equations, combines remainders, and sits beside repeated squaring at the heart of modular arithmetic.",
        "summary": (
            "Sections 31.1 to 31.6: why input size is counted in bits, Euclid's algorithm and "
            "Lamé's theorem that it makes O(lg b) recursive calls, the extended algorithm that "
            "returns x and y with ax + by = gcd(a, b), the solutions of ax ≡ b (mod n), the "
            "Chinese remainder theorem, and modular exponentiation by repeated squaring. Run "
            "the extended algorithm on the lesson's pair in the lab, then switch the same "
            "panel to congruences, remainders and powers."
        ),
        "key": [
            "size is bits: β = ⌈lg(n + 1)⌉",
            "gcd(a, b) = gcd(b, a mod b)",
            "Lamé: O(lg b) recursive calls",
            "Fibonacci pairs are the worst case",
            "extended Euclid: ax + by = gcd",
            "ax ≡ b (mod n): d solutions if d | b",
            "a^b mod n by repeated squaring",
        ],
        "key_label": "Sections 31.1 to 31.6 in seven lines",
        "concepts_intro": (
            "Three ideas: the measure of size that makes these algorithms polynomial, the "
            "combination Euclid's algorithm returns, and the arithmetic it is used in."
        ),
        "concepts": [
            ("Input size in bits",
             "A number n takes about lg n bits to write, so an algorithm on numbers of β bits "
             "is polynomial if it runs in time polynomial in β. Trial division up to √n takes "
             "about `2^(β/2)` steps, exponential in β; Euclid's algorithm takes O(β) "
             "arithmetic operations."),
            ("Bézout coefficients",
             "Integers x and y with `ax + by = gcd(a, b)`. They always exist, the gcd is the "
             "smallest positive number of that form, and EXTENDED-EUCLID returns a pair along "
             "with the gcd at no extra asymptotic cost."),
            ("Modular arithmetic",
             "Arithmetic on the remainders 0 to n − 1, where `a ≡ b (mod n)` means n divides "
             "a − b. Addition and multiplication carry over; division by a works only when "
             "`gcd(a, n) = 1`, and then the inverse of a comes from the Bézout coefficients."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 31.1 to 31.6 in your own copy; 31.2, 31.4 and 31.6 are the "
            "algorithmic ones, and 31.3 is the group theory they lean on. The lesson sets out "
            "each algorithm in its own words, runs it by hand on numbers written for the "
            "lesson, and checks the hand work in the lab."
        ),
        "body": [
            ("p", "&ldquo;Number theory was once viewed as a beautiful but largely useless "
                  "subject in pure mathematics.&rdquo; Chapter 31 explains the change: "
                  "cryptography rests on two facts about large numbers, that primes are easy to "
                  "find and that their products are hard to factor. This lesson reads sections "
                  "31.1 to 31.6, the arithmetic the next lesson's RSA cryptosystem and primality "
                  "test are made of."),
            ("p", "Section 31.1 changes the unit of size. An input here is a few large numbers, "
                  "and a number n is written in `β = ⌈lg(n + 1)⌉` bits, so an algorithm is "
                  "efficient when its cost is polynomial in β, not in n. The authors count "
                  "arithmetic operations and, where it matters, bit operations. By that measure "
                  "trial division, which tries every divisor up to √n, is exponential: √n is "
                  "about `2^(β/2)`."),
            ("p", "Section 31.2's EUCLID rests on one identity, `gcd(a, b) = gcd(b, a mod b)`, "
                  "true because a number divides a and b exactly when it divides b and "
                  "`a − ⌊a/b⌋·b`. The recursion stops at `gcd(a, 0) = a`. How many calls? Each "
                  "call's second argument becomes the next call's first, and the authors show by "
                  "induction that if EUCLID(a, b) with `a > b ≥ 1` makes k ≥ 1 recursive calls, "
                  "then a is at least the Fibonacci number `F_(k+2)` and b at least `F_(k+1)` "
                  "(Lemma 31.10)."),
            ("thm", ("Lamé's theorem (Theorem 31.11), in short",
                     "If `a > b ≥ 1` and `b < F_(k+1)`, then EUCLID(a, b) recurses fewer than k "
                     "times. Consecutive Fibonacci numbers meet the bound exactly, and "
                     "since `Fₖ` grows like `φᵏ/√5`, the number of calls is `O(lg b)`.")),
            ("p", "EXTENDED-EUCLID returns the gcd d together with x and y such that "
                  "`ax + by = d`. On the way back from the recursive call on `(b, a mod b)`, "
                  "which returned `d = b·x′ + (a mod b)·y′`, it rewrites `a mod b` as "
                  "`a − ⌊a/b⌋·b` and collects terms: `x = y′` and `y = x′ − ⌊a/b⌋·y′`. The number "
                  "of calls is the same as EUCLID's. The lab runs the same algorithm forward, "
                  "keeping for every remainder r its own pair s and t with `r = a·s + b·t`, which "
                  "gives the same coefficients without a second pass."),
            ("math", [
                "the lesson's pair: a = 1147, b = 851",
                "",
                "1147 = 1 · 851 + 296",
                "851  = 2 · 296 + 259",
                "296  = 1 · 259 + 37",
                "259  = 7 · 37 + 0",
                "",
                "gcd = 37, in 4 recursive calls",
                "1147 · 3 + 851 · (−4) = 3441 − 3404 = 37",
            ]),
            ("p", "Lamé's bound for this pair: 851 lies between `F₁₅ = 610` and `F₁₆ = 987`, so "
                  "with `k + 1 = 16` the theorem promises fewer than 15 calls; there are 4. The "
                  "bound is about the worst pair of that size, and the worst pairs are "
                  "consecutive Fibonacci numbers: `(89, 55)` takes 9 divisions, every quotient 1 "
                  "until the last, the most for any b below 89."),
            ("p", "Section 31.3 supplies the algebra: the integers modulo n under addition form "
                  "a group, and the remainders coprime to n form a group `Zₙ*` under "
                  "multiplication, with `φ(n)` elements, Euler's phi function. Section 31.4 "
                  "solves `ax ≡ b (mod n)`. Let `d = gcd(a, n)`. The multiples of a modulo n are "
                  "exactly the multiples of d, so a solution exists exactly when d divides b, and "
                  "then there are exactly d solutions modulo n, spaced `n/d` apart. "
                  "MODULAR-LINEAR-EQUATION-SOLVER finds them from EXTENDED-EUCLID: if "
                  "`d = ax′ + ny′`, the first solution is `x′·(b/d) mod n`."),
            ("example", ("Seven solutions modulo 35",
                         "Solve `21x ≡ 14 (mod 35)`. Here `d = gcd(21, 35) = 7`, which divides "
                         "14, so there are 7 solutions, 5 apart. Extended Euclid gives "
                         "`21·2 + 35·(−1) = 7`, so `x′ = 2` and the first solution is "
                         "`2·(14/7) mod 35 = 4`: indeed `21·4 = 84 = 2·35 + 14`. The others are "
                         "9, 14, 19, 24, 29 and 34. With `d = 1`, the same recipe computes a "
                         "modular inverse.")),
            ("p", "Section 31.5's Chinese remainder theorem says that when n₁, …, nₖ are "
                  "pairwise coprime with product n, a number modulo n is the same thing as its "
                  "list of remainders modulo each nᵢ, and arithmetic can be done on either side. "
                  "To go back from remainders to the number, set `mᵢ = n/nᵢ`, let "
                  "`cᵢ = mᵢ·(mᵢ⁻¹ mod nᵢ)`, and add `Σ aᵢ·cᵢ` modulo n: each cᵢ is 1 modulo nᵢ and "
                  "0 modulo the others. For `x ≡ 4 (mod 7)` and `x ≡ 6 (mod 9)`: `c₁ = 9·4 = 36`, "
                  "`c₂ = 7·4 = 28`, and `4·36 + 6·28 = 312 ≡ 60 (mod 63)`."),
            ("p", "Section 31.6 computes `aᵇ mod n` by repeated squaring. "
                  "MODULAR-EXPONENTIATION reads the bits of b from the most significant down, "
                  "squaring its running value at each bit and multiplying by a at each 1 bit; "
                  "its loop invariant is that the value is `aᶜ mod n` where c is the prefix of "
                  "b's bits read so far. That is O(β) multiplications of numbers below n, and "
                  "reducing modulo n after each one keeps them small."),
            ("p", "Now the lab, the one the Discrete Mathematics Subject's lesson Bézout's "
                  "Identity and Modular Inverses uses. It opens in its extended-Euclid mode on "
                  "the lesson's pair: the gcd tile reads 37 and the coefficients tile `3, -4`, "
                  "and the table has one row per remainder, 1147, 851, 296, 259, 37 and 0, each "
                  "with its pair s and t and the check `r = 1147·s + 851·t`. The status line adds "
                  "that 1147 has no inverse modulo 851, because every combination of the two is a "
                  "multiple of 37."),
            ("p", "The panel has other modes in its menu. Euclid's mode on 1147 and 851 reports "
                  "4 divisions, and on 89 and 55 reports 9. The congruence mode on a = 21, b = 14, "
                  "m = 35 lists the seven solutions of the example, each checked. The Chinese "
                  "remainder mode on remainders 4 and 6 with moduli 7 and 9 gives 60 modulo 63. The "
                  "exponentiation mode on 5, 117 and 391 gives 201 in 6 squarings and 5 "
                  "multiplications, against 116 multiplications done one at a time. It counts "
                  "differently from MODULAR-EXPONENTIATION: it reads the bits of 117, binary "
                  "1110101, from the least significant end and skips the square it would never "
                  "use, while the book's procedure reads from the most significant end and "
                  "squares once for each of the 7 bits, the first time squaring 1. Both multiply "
                  "once for each 1 bit, 5 times here."),
            ("h3", "Exercise"),
            ("p", "Run EXTENDED-EUCLID by hand on `(377, 233)`, two consecutive Fibonacci "
                  "numbers, count the recursive calls, and compare with Lamé's bound. Then solve "
                  "`15x ≡ 9 (mod 24)` and compute `3^45 mod 101` by repeated squaring, writing "
                  "45 in binary first. Check all three in the lab's modes."),
            ("p", "The next lesson, RSA and Primality Testing, uses every piece of this one: "
                  "an inverse modulo φ(n) for the key, repeated squaring to encrypt, and the "
                  "Chinese remainder theorem to prove it decrypts."),
        ],
        "lab": ("number", {
            "mode": "bezout",
            "a": 1147,
            "b": 851,
            "panel_title": "Extended Euclid, then the rest of the toolkit",
            "panel_intro": (
                "The panel opens on the lesson's pair in extended-Euclid mode: every remainder "
                "is written as a combination of the two inputs, so the last nonzero row is "
                "the gcd with its coefficients. Change the mode to run Euclid, solve a linear "
                "congruence, combine remainders, or raise to a power modulo m."
            ),
        }),
        "steps_title": "Extended Euclid by hand",
        "steps_intro": "Keep three columns beside the remainders: q, s and t.",
        "steps": [
            ("Start two rows",
             "Write `a = a·1 + b·0` and `b = a·0 + b·1`: remainders a and b, with s and t "
             "equal to 1, 0 and then 0, 1."),
            ("Divide and subtract",
             "Take the quotient q of the last two remainders. The new row is the older row "
             "minus q times the newer one, in r, s and t alike."),
            ("Stop at zero",
             "When the remainder reaches 0, the row above holds the gcd and its "
             "coefficients. Check `a·s + b·t` on that row."),
            ("Use the coefficients",
             "If the gcd is 1, s reduced modulo b is the inverse of a modulo b. For "
             "`ax ≡ c (mod n)`, scale by c/d and list the d solutions n/d apart."),
            ("Do it on a pair of your own",
             "Choose two four-digit numbers of your own with a common factor, run the table by "
             "hand, then type them into the lab and compare every row."),
        ],
        "worked": {
            "title": "The lesson's pair, back-substituted",
            "intro": [
                "EXTENDED-EUCLID works upward from the last call. Start from `37 = 37·1 + 0·0` "
                "at the call on (37, 0) and apply `x = y′`, `y = x′ − ⌊a/b⌋·y′` at each level.",
            ],
            "lines": [
                "(37, 0):     d = 37, x = 1, y = 0",
                "(259, 37):   q = 7; x = 0, y = 1 − 7·0 = 1",
                "(296, 259):  q = 1; x = 1, y = 0 − 1·1 = −1",
                "(851, 296):  q = 2; x = −1, y = 1 − 2·(−1) = 3",
                "(1147, 851): q = 1; x = 3, y = −1 − 1·3 = −4",
                "check: 1147·3 + 851·(−4) = 37",
            ],
            "after": [
                "The same pair the lab's forward table reaches. Each level costs a constant "
                "number of operations, so the whole computation is as cheap as EUCLID: O(lg b) "
                "calls by Lamé's theorem.",
            ],
        },
        "quiz_title": "Gcds, congruences and powers",
        "quiz": [
            {"q": "How many solutions modulo 24 does `15x ≡ 9 (mod 24)` have?",
             "a": ["3", "1", "0", "24"],
             "c": 0,
             "why": "`d = gcd(15, 24) = 3` divides 9, so there are exactly 3 solutions, 8 apart: "
                    "7, 15 and 23 (`15·7 = 105 = 4·24 + 9`). One solution is the case d = 1. No "
                    "solution would need d not to divide 9. 24 would mean every x works, which "
                    "only happens when a and b are both multiples of n."},
            {"q": "When `a > b` and b is below `F₁₂ = 144`, what is the largest number of "
                  "recursive calls EUCLID(a, b) can make?",
             "a": ["10", "11", "144", "7"],
             "c": 0,
             "why": "With `b < F_(k+1) = F₁₂`, k is 11, and Lamé's theorem gives fewer than 11 "
                    "calls; `EUCLID(144, 89)`, two consecutive Fibonacci numbers, makes exactly "
                    "10, so the bound is reached. 11 misreads the index by one. 144 confuses the "
                    "bound on b with a count of calls. 7 is about lg 144, but the logarithm in "
                    "the true count has base φ, not 2, and the Fibonacci pairs need more."},
            {"q": "MODULAR-EXPONENTIATION computes `aᵇ mod n` for b = 45, binary 101101. How "
                  "many times does it multiply by a, beyond the squarings?",
             "a": ["4", "6", "45", "44"],
             "c": 0,
             "why": "It squares once per bit and multiplies by a once per 1 bit, and 101101 has "
                    "four 1s. 6 is the number of bits, the number of squarings. 44 is the "
                    "multiplications of the naive method, a times itself 44 times, and 45 is b "
                    "itself."},
            {"q": "Which pair x, y satisfies `1147x + 851y = 37`, the gcd?",
             "a": ["`x = 3, y = −4`", "`x = −4, y = 3`", "`x = 23, y = −31`", "`x = 1, y = 1`"],
             "c": 0,
             "why": "`1147·3 − 851·4 = 3441 − 3404 = 37`. Swapping gives `−4588 + 2553 = −2035`. "
                    "`x = 23, y = −31` is the zero row's pair with its signs flipped: "
                    "`1147·23 − 851·31 = 26381 − 26381 = 0`, a combination of value 0, not 37. `1147 + 851 = 1998`, which is "
                    "`54·37`, a multiple of the gcd but not the gcd."},
        ],
        "mistakes": [
            ("Measuring a number algorithm by the size of the number",
             "An input n is about lg n bits long, and running time is judged against that. A "
             "loop that runs n or √n times is exponential in the input's length, which is why "
             "trial division is no way to factor a 300-digit number while Euclid's algorithm, "
             "with O(lg b) calls, handles one easily. In the lab, 1147 and 851 take 4 divisions "
             "and no Fibonacci pair below 1,000 takes more than 14."),
            ("Expecting a linear congruence to have one solution",
             "`ax ≡ b (mod n)` has no solution when `d = gcd(a, n)` does not divide b, and "
             "exactly d solutions modulo n when it does. The lesson's `21x ≡ 14 (mod 35)` has "
             "seven, and the lab's congruence mode lists them; dividing through by d leaves one "
             "solution modulo n/d, which lifts to d of them."),
            ("Computing the power first and reducing at the end",
             "`5^117` has 82 digits, and `2^1000` has 302, though each fits below a small "
             "modulus after reduction. Reducing after every squaring and multiplication keeps every "
             "intermediate below n², and repeated squaring needs only about 2·lg b "
             "multiplications instead of b − 1."),
        ],
        "standard": (
            "Finish when you can run the chapter's algorithms by hand.",
            "Run EXTENDED-EUCLID on two numbers and check the coefficients, bound its calls "
            "with Lamé's theorem, solve a linear congruence with all its solutions, combine "
            "two remainders by the Chinese remainder theorem, and compute a modular power by "
            "repeated squaring with its count of multiplications."
        ),
        "note": (
            "The lab runs each algorithm exactly with integers of any size and prints its "
            "trace; its exponentiation mode reads the bits of b from the least significant "
            "end and makes one squaring fewer than MODULAR-EXPONENTIATION, which squares "
            "once per bit; the multiplications agree. Lamé's theorem "
            "and the O(β) bounds are the book's proofs; the counts are facts about the "
            "numbers typed."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS 31.7-31.8, pp. 958-975, 31.9 named. Quote: printed p. 959,
    # 29 words, quotes.py OK. Lesson total: 29 words. Lab: random/witness,
    # kit preset psp2047 (n = 2047 = 23 x 89 is not in the book); the
    # lesson's RSA numbers p = 43, q = 67, e = 5 and its exercise n = 1387 are
    # its own. Public-key systems and signatures (pp. 958-962); the RSA steps
    # and Theorem 31.36 (pp. 962-964); hybrid systems (pp. 963-964); prime
    # number theorem and ln n trials (pp. 965-966); trial division, base-2
    # pseudoprimes, 22 below 10,000, Carmichael numbers (pp. 966-968);
    # WITNESS, MILLER-RABIN (pp. 968-971); Theorem 31.38 (n - 1)/2,
    # Theorem 31.39 2^-s, Bayes, s = 50, the (n - 1)/4 remark (pp. 971-975).
    {
        "slug": "rsa-and-primality-testing",
        "title": "RSA and Primality Testing",
        "module": "Chapter 31 · Number-Theoretic Algorithms",
        "one_line": "RSA publishes n = pq and an exponent e and keeps the inverse of e modulo (p − 1)(q − 1), so encryption is one modular power and decryption another; finding the large primes it needs takes a randomized test that is wrong with probability at most 2^(−s).",
        "summary": (
            "Section 31.7 builds the RSA public-key cryptosystem from the last lesson's "
            "arithmetic and proves that decryption inverts encryption. Section 31.8 finds the "
            "primes it needs: random numbers near n are prime about once in ln n tries, Fermat's "
            "test is fooled by pseudoprimes and Carmichael numbers, and the Miller-Rabin test, "
            "which also looks for nontrivial square roots of 1, errs with probability at most "
            "2^(−s) after s random bases. Count the witnesses for a composite in the lab."
        ),
        "key": [
            "n = pq, φ(n) = (p − 1)·(q − 1)",
            "e coprime to φ(n), d = e⁻¹ mod φ(n)",
            "encrypt Mᵉ mod n, decrypt Cᵈ mod n",
            "Fermat's test is fooled by pseudoprimes",
            "a nontrivial root of 1 proves n composite",
            "at least (n − 1)/2 bases are witnesses",
            "error after s bases: at most 2^(−s)",
        ],
        "key_label": "Sections 31.7 and 31.8 in seven lines",
        "concepts_intro": (
            "Three ideas: a key anyone may know, the evidence that proves a number composite, "
            "and the error a randomized test leaves."
        ),
        "concepts": [
            ("Public and secret keys",
             "Each participant publishes one key and keeps the other. Applying the public key "
             "and then the secret one, or the other way round, returns the message; the "
             "system is secure only if the secret transformation cannot be computed from the "
             "public one in any practical time."),
            ("Witness",
             "A base a that proves an odd number n composite. In the Miller-Rabin test, a is "
             "a witness if `aⁿ⁻¹` is not 1 modulo n, which Fermat's theorem forbids for a "
             "prime, or if squaring along the way reveals a square root of 1 other than ±1, "
             "which no prime modulus has. A base that is not a witness proves nothing."),
            ("One-sided error",
             "The test's answer composite is always right; its answer prime can be wrong, "
             "when every base it tried happens not to be a witness. Each independent random "
             "base is a witness with probability at least 1/2 for a composite, so s bases "
             "leave an error of at most `2^(−s)`."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 31.7 and 31.8 in your own copy first, and the opening of 31.9 if you "
            "want to know why factoring is believed hard. The lesson sets out RSA and the "
            "Miller-Rabin test in its own words, builds one RSA key by hand, and counts "
            "witnesses in the lab."
        ),
        "body": [
            ("p", "&ldquo;The RSA public-key cryptosystem relies on the dramatic difference "
                  "between the ease of finding large prime numbers and the difficulty of "
                  "factoring the product of two large prime numbers.&rdquo; Section 31.7 builds "
                  "the system and Section 31.8 supplies the easy half, a fast way to find "
                  "primes. Section 31.9, on factoring, is starred and named here only; it is "
                  "the hard half, and no fast method is known."),
            ("p", "A public-key cryptosystem gives each participant a public key P and a secret "
                  "key S that describe inverse permutations of the set of messages. To send "
                  "Alice a message, Bob applies her public key; only Alice can apply the secret "
                  "inverse. To sign, Alice applies her secret key, and anyone can check the "
                  "signature with her public one. The section's whole difficulty is to publish "
                  "a function without revealing how to invert it."),
            ("thm", ("RSA, in five steps",
                     "Choose two large primes p and q and let `n = pq`. Compute "
                     "`φ(n) = (p − 1)·(q − 1)`. Choose a small odd e coprime to φ(n). Let d be "
                     "the inverse of e modulo φ(n), by extended Euclid. Publish `(e, n)`, keep "
                     "`(d, n)`; encrypt by `C = Mᵉ mod n` and decrypt by `M = Cᵈ mod n`.")),
            ("p", "Why does decryption work? Theorem 31.36 checks it modulo p and modulo q "
                  "separately. Since `ed = 1 + k·(p − 1)·(q − 1)`, modulo p the power `M^(ed)` "
                  "is M times a power of `M^(p−1)`, which is 1 by Fermat's theorem when p does "
                  "not divide M, and both sides are 0 when it does. The same holds modulo q, and "
                  "the Chinese remainder theorem joins the two into `M^(ed) ≡ M (mod n)`. "
                  "Encryption and decryption are each one modular exponentiation, and in practice "
                  "RSA encrypts only a short key for a faster symmetric cipher, which the authors "
                  "describe as a hybrid system."),
            ("example", ("A key small enough to check",
                         "Take p = 43 and q = 67: `n = 2881` and `φ(n) = 42·66 = 2772`. Choose "
                         "e = 5, which is coprime to 2772. Extended Euclid gives "
                         "`5·1109 − 2·2772 = 1`, so `d = 1109`. The message M = 1000 encrypts to "
                         "`1000⁵ mod 2881 = 962`, and `962¹¹⁰⁹ mod 2881 = 1000`. Anyone who could "
                         "factor 2881 could repeat this arithmetic, which is why real keys use "
                         "primes hundreds of digits long.")),
            ("p", "Section 31.8 asks how such primes are found. By the prime number theorem the "
                  "number of primes up to n is about `n/ln n`, so a random number near n is prime "
                  "with probability about `1/ln n`, and about ln n random tries find one, about "
                  "710 for 1024-bit numbers, half that if only odd numbers are tried. What is "
                  "needed is a fast test. Trial division takes about √n steps, exponential in "
                  "the number of bits."),
            ("p", "Fermat's theorem gives a fast test that almost works: if n is prime then "
                  "`aⁿ⁻¹ ≡ 1 (mod n)` for every a from 1 to n − 1. PSEUDOPRIME checks this for "
                  "a = 2 and is wrong only on base-2 pseudoprimes, composites that pass, of "
                  "which there are 22 below 10,000. Trying more bases does not repair it, "
                  "because Carmichael numbers pass for every base coprime to them. The Miller-Rabin "
                  "test adds a second check. Write `n − 1 = 2ᵗ·u` with u odd, compute `a^u mod n`, "
                  "and square it t times to reach `aⁿ⁻¹`. If some square is 1 while the value "
                  "before it was neither 1 nor n − 1, that value is a nontrivial square root of "
                  "1 and n is composite (Corollary 31.35); if the last value is not 1, Fermat's "
                  "test fails. Either way WITNESS returns true."),
            ("thm", ("Theorems 31.38 and 31.39, in short",
                     "If n is an odd composite, at least `(n − 1)/2` of the bases 1 to n − 1 are "
                     "witnesses. MILLER-RABIN tries s bases chosen independently at random, so "
                     "if n is composite it answers prime with probability at most `2^(−s)`, and "
                     "if n is prime it always answers prime.")),
            ("p", "The authors add two remarks. The bound is about the test's coin flips, not "
                  "about how likely a given n is to be prime, and Bayes's theorem shows that for "
                  "a random 1024-bit number about nine trials are needed just to outweigh the "
                  "prior odds against primality; they suggest s = 50 for almost any use. And "
                  "the true count is better than the theorem: an improved argument shows that "
                  "at most `(n − 1)/4` bases are non-witnesses, some n have exactly that many, "
                  "and for a random odd composite far fewer are expected."),
            ("p", "Now the lab, the one the Algorithms Subject's lesson Witnesses, Liars, and "
                  "One-Sided Error uses. Its slider n runs over odd numbers up to 2,047, and for "
                  "each it tests every base from 2 to n − 2, so the counts are exact. It traces "
                  "the chain for one chosen base, counts witnesses and non-witnesses, counts "
                  "Fermat's witnesses beside them, and gives the exact chance that a chosen "
                  "number of random bases all fail to testify. It differs from the book in three "
                  "ways. Its letters are swapped: it writes `n − 1 = d·2ˢ` with d odd, where the "
                  "book writes `2ᵗ·u`, and it calls the number of bases t, where the book calls "
                  "it s. Its bound is `(1/4)` to the number of bases, from the improved "
                  "argument, not Theorem 31.39's `2^(−s)`, and a tile checks that at least three "
                  "quarters of the bases are witnesses, not Theorem 31.38's half. And it leaves out the bases 1 "
                  "and n − 1, which never testify, where the book draws from 1 to n − 1."),
            ("p", "The lesson's number is preset psp2047, `2047 = 23 · 89`. Here "
                  "`n − 1 = 2·1023`, so `t = 1`, and `2¹¹ = 2048 ≡ 1`, so `2¹⁰²³ = (2¹¹)⁹³ ≡ 1`: "
                  "base 2 yields no testimony, and a test that tried only base 2 would call 2047 "
                  "prime. The lab counts 1,804 witnesses among the 2,044 bases, `451/511`, "
                  "`0.8826`, and 240 non-witnesses, the smallest of them 2. Base 3 is a witness: "
                  "`3¹⁰²³ ≡ 1565` and `1565² ≡ 1013`, not 1. In the book's count over 1 to 2,046 "
                  "there are 242 non-witnesses, far under the `(n − 1)/2 = 1023` that Theorem "
                  "31.38 allows."),
            ("h3", "Exercise"),
            ("p", "Set the lab's n to 1,387 and trace base 2. First predict by hand: "
                  "`1386 = 2·693`, so compute `2⁶⁹³ mod 1387` by repeated squaring and square the "
                  "result once. Decide whether Fermat's test is fooled at base 2, whether the "
                  "strong test is, and what the gcd of 1387 with one less than the value before "
                  "the final 1 tells you. Then read the witness count and check it against `(n − 1)/2`."),
            ("p", "That completes Part VII's first five chapters. The next course, Strings, "
                  "Geometry and Hardness, reads the rest of Part VII, beginning with string "
                  "matching in Chapter 32, where Rabin and Karp's matcher uses the modular "
                  "arithmetic of this chapter."),
        ],
        "lab": ("random", {"mode": "witness", "preset": "psp2047"}),
        "steps_title": "One base of the Miller-Rabin test",
        "steps_intro": "Factor out the twos from n − 1 before anything else.",
        "steps": [
            ("Write n − 1 as 2ᵗ·u",
             "Divide n − 1 by 2 until it is odd. The odd part is u and the number of halvings "
             "is t."),
            ("Raise a to the power u",
             "Use repeated squaring. If the result is 1 or n − 1, the base gives no testimony; "
             "stop."),
            ("Square up to t − 1 times",
             "Square modulo n. Reaching n − 1 ends the chain with no testimony. Reaching 1 "
             "from a value other than ±1 is a nontrivial square root of 1: a is a witness."),
            ("Read the verdict",
             "If the chain never reached n − 1, a is a witness and n is composite. Otherwise "
             "this base proves nothing, and the test tries another."),
            ("Do it on a number of your own",
             "Pick an odd composite of your own below 2,047 with two prime factors, predict "
             "whether base 2 is a witness by hand, then set the lab's n to it and compare its "
             "witness count with `(n − 1)/2`."),
        ],
        "worked": {
            "title": "Decrypting with the Chinese remainder theorem",
            "intro": [
                "Check the example's decryption of C = 962 without computing `962¹¹⁰⁹` modulo "
                "2881 directly, by working modulo 43 and 67 as Theorem 31.36's proof does.",
            ],
            "lines": [
                "M = 1000 ≡ 11 (mod 43) and ≡ 62 (mod 67)",
                "d = 1109 ≡ 17 (mod 42) and ≡ 53 (mod 66)",
                "962 ≡ 16 (mod 43); 16¹⁷ ≡ 11 (mod 43)",
                "962 ≡ 24 (mod 67); 24⁵³ ≡ 62 (mod 67)",
                "the CRT joins 11 (mod 43) and 62 (mod 67) into 1000 (mod 2881)",
            ],
            "after": [
                "Fermat's theorem lets each exponent drop modulo p − 1 or q − 1, and the two "
                "small powers recover M's remainders. Real implementations decrypt this way "
                "because the two half-size powers are cheaper than one full-size power; the "
                "secret primes are needed to do it.",
            ],
        },
        "quiz_title": "Keys, witnesses and error",
        "quiz": [
            {"q": "With p = 11, q = 17 and e = 7, what is the RSA secret exponent d?",
             "a": ["23", "7", "107", "13"],
             "c": 0,
             "why": "`φ(n) = 10·16 = 160` and `7·23 = 161 = 160 + 1`, so `d = 23`. 7 would make "
                    "the secret key equal the public one, and `7·7 = 49` is not 1 modulo 160. "
                    "107 is the inverse of 7 modulo n = 187, since `7·107 = 749 = 4·187 + 1`, "
                    "but modulo 160 it gives `749 ≡ 109`, so it does not decrypt. 13 has no "
                    "derivation: `7·13 = 91`."},
            {"q": "For n = 2047, `2¹⁰²³ ≡ 1 (mod 2047)`. What does base 2 tell the Miller-Rabin "
                  "test?",
             "a": ["Nothing: it is not a witness, and 2047 is in fact composite",
                   "That 2047 is prime",
                   "That 2047 is composite, since 1023 is odd",
                   "That 2047 is a Carmichael number"],
             "c": 0,
             "why": "The chain starts at 1, so it can never show a nontrivial square root, and "
                    "the last value is 1, so Fermat's test passes: no testimony. A base that is "
                    "not a witness proves nothing, and 2047 = 23·89. 1023 being odd is just how u "
                    "is defined. A Carmichael number fools Fermat's test at every coprime base, "
                    "but base 3 already fails it here."},
            {"q": "MILLER-RABIN tries s = 10 independent random bases on a composite n. What "
                  "does Theorem 31.39 guarantee about the chance it answers prime?",
             "a": ["At most `2⁻¹⁰`, about 1 in 1,000",
                   "Exactly `2⁻¹⁰`",
                   "At most `10/n`",
                   "Zero, once s is at least 10"],
             "c": 0,
             "why": "Each base is a witness with probability at least 1/2, so all ten miss with "
                    "probability at most `2⁻¹⁰ = 1/1024`. The true chance is usually far smaller, "
                    "so exactly is wrong; for 2047 the lab's exact figure for one base is "
                    "`60/511`. The bound does not depend on n. No finite s makes the error zero; "
                    "it only shrinks."},
            {"q": "Why does a nontrivial square root of 1 modulo n prove n composite?",
             "a": ["Modulo an odd prime, x² ≡ 1 has only the solutions 1 and −1",
                   "Every composite has one, and no prime does, by Fermat's theorem",
                   "It shows that aⁿ⁻¹ is not 1 modulo n",
                   "Its square root is a factor of n"],
             "c": 0,
             "why": "If p is an odd prime and p divides `(x − 1)·(x + 1)`, it divides one factor, "
                    "so x ≡ ±1; an x other than ±1 with `x² ≡ 1` rules primality out (Corollary "
                    "31.35, from Theorem 31.34). Powers of an odd prime have no nontrivial "
                    "square root of 1 at all, so not every composite has one, and the fact comes "
                    "from that divisibility argument, not from Fermat's theorem. Such a root can occur while `aⁿ⁻¹ ≡ 1`. What yields a factor is the "
                    "gcd of n with x − 1, not the root itself."},
        ],
        "mistakes": [
            ("Reading a passed test as proof of primality",
             "The answer composite is a proof; the answer prime is only the absence of one. On "
             "2047, base 2 gives no testimony, and a test that stopped there would accept a "
             "composite. The lab shows 240 such bases out of 2,044; the guarantee is about "
             "the chance of drawing only those, which s random bases drive below `2^(−s)`."),
            ("Trusting Fermat's test with more bases",
             "Adding bases helps against most pseudoprimes but not against Carmichael numbers, "
             "which satisfy `aⁿ⁻¹ ≡ 1` for every base coprime to them, so only bases sharing a "
             "factor with n expose them. The square-root check is what makes the Miller-Rabin "
             "test immune: for every odd composite at least half the bases are witnesses."),
            ("Computing d modulo n instead of modulo φ(n)",
             "The decryption exponent is the inverse of e modulo `φ(n) = (p − 1)·(q − 1)`, "
             "because exponents work modulo p − 1 and q − 1 by Fermat's theorem. An inverse "
             "taken modulo n, or n − 1, has no such property and does not decrypt in general; "
             "computing φ(n) needs p and q, which is where the secrecy lies."),
        ],
        "standard": (
            "Finish when you can build an RSA key and run one Miller-Rabin base by hand.",
            "Generate an RSA key from two small primes, encrypt and decrypt a message, say why "
            "decryption works, trace the Miller-Rabin chain for one base, and state what the "
            "answers prime and composite each guarantee."
        ),
        "note": (
            "The lab counts witnesses exactly for odd n up to 2,047 over the bases 2 to n − 2 "
            "and prints the improved bound, a quarter to the number of bases, beside the exact error; it does not run RSA, "
            "which the example and the worked check carry by hand. Theorem 31.38's bound holds "
            "for every odd composite; the counts are facts about the number on the slider."
        ),
    },
]
