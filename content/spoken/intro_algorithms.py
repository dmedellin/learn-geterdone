"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title, as
SPOKEN.update({...}) under a "# <Course title>" comment.
"""

SPOKEN = {}

# Sorting and Order Statistics
SPOKEN.update({
    "A[1..n]": "A from 1 to n",
    "A[1..heap-size]": "A from 1 to heap-size",
    "A[1..13]": "A from 1 to 13",
    "A[p..r]": "A from p to r",
    "A[p..q − 1]": "A from p to q minus 1",
    "A[q + 1..r]": "A from q plus 1 to r",
    "C[0..k]": "C from 0 to k",
    "C[0..4]": "C from 0 to 4",
    "log₁₀/₉ n = Θ(lg n)": "log base 10 over 9 of n equals theta of log base 2 of n",
    "Pr{zᵢ meets zⱼ} = 2/(j − i + 1)": "the probability that z sub i meets z sub j equals 2 over the quantity j minus i plus 1",
    "Pr{zᵢ is compared to zⱼ} = 2/(j − i + 1)": "the probability that z sub i is compared to z sub j equals 2 over the quantity j minus i plus 1",
    "Θ((b/r)·(n + 2ʳ))": "theta of b over r, times the quantity n plus 2 to the power r",
    "Θ(d·(n + k))": "theta of d times the quantity n plus k",
    "d passes of n + k: Θ(d·(n + k))": "d passes of n plus k, theta of d times the quantity n plus k",
})

# Strings, Geometry and Hardness
SPOKEN.update({
    "a valid shift s: T[s+1..s+m] = P": "a valid shift s, T from s plus 1 to s plus m equals P",
    "Θ((n − m + 1)·m)": "theta of the quantity n minus m plus 1, times m",
    "δ(q, a) = σ(P_q·a)": "delta of q and a equals sigma of P sub q followed by a",
    "π[q]: longest proper border of P_q": "pi of q, the longest proper border of P sub q",
    "on a mismatch, fall back from q to π[q]": "on a mismatch, fall back from q to pi of q",
    "q = 4   a vs b, no: k = π[1] = 0": "q equals 4, a against b, no, k becomes pi of 1, which is 0",
    "q = 7   b vs a, no: k = π[3] = 1": "q equals 7, b against a, no, k becomes pi of 3, which is 1",
    "O(m³·|Σ|)": "big O of m cubed times the size of the alphabet",
    "O(m·|Σ|)": "big O of m times the size of the alphabet",
    "L1 ≤P L2: x ∈ L1 iff f(x) ∈ L2": "L 1 reduces to L 2 in polynomial time, x is in L 1 if and only if f of x is in L 2",
    "ratio ρ(n): max(C/C*, C*/C) ≤ ρ(n)": "ratio rho of n, the larger of C over C star and C star over C is at most rho of n",
    "ratio H(max |S|) ≤ ln |X| + 1": "the ratio, H of the largest set's size, is at most the natural log of the size of X, plus 1",
    "1-2, 2-3, 3-4, 4-5, 2-6, 3-6, 6-7": "edges 1 2, 2 3, 3 4, 4 5, 2 6, 3 6 and 6 7",
    "take 1-2: cover {1, 2}; remove 2-3, 2-6": "take edge 1 2, the cover is 1 and 2, remove edges 2 3 and 2 6",
    "take 3-4: cover adds 3, 4; remove 3-6, 4-5": "take edge 3 4, the cover adds 3 and 4, remove edges 3 6 and 4 5",
    "take 6-7: cover adds 6, 7; no edges left": "take edge 6 7, the cover adds 6 and 7, no edges are left",
    "matching A = {1-2, 3-4, 6-7}, |A| = 3": "the matching A is the edges 1 2, 3 4 and 6 7, the size of A is 3",
})

# Graph Algorithms
SPOKEN.update({
    "v.d never falls below δ(s, v)": "v dot d never falls below delta s v, the true distance from s to v",
    "settled means final: d = δ(s, u)": "settled means final, d equals delta s u, the true distance from s to u",
    "a spanning tree has |V| − 1 edges": "a spanning tree has one edge fewer than there are vertices",
    "|V| − 1 rounds fix every simple path": "the number of vertices minus 1 rounds fix every simple path",
    "time runs from 1 to 2|V|": "time runs from 1 to twice the number of vertices",
    "integer capacities: O(E·|f*|)": "integer capacities, big O of E times the value of a maximum flow",
})

# Data Structures
SPOKEN.update({
    "s/2ʷ": "s over 2 to the power w",
    "s ≈ 0.618·2ʷ": "s approximately equal to 0.618 times 2 to the power w",
})

# Advanced Data Structures
SPOKEN.update({
    "height h ≤ log_t((n + 1)/2)": "height h is at most log base t of n plus 1 over 2",
    "h ≤ log_t((n + 1)/2)": "h is at most log base t of n plus 1 over 2",
    "log_t((n + 1)/2)": "log base t of n plus 1 over 2",
    "Φ(H) = t(H) + 2m(H)": "Phi of H equals t of H plus 2 times m of H",
    "t(H)": "t of H",
    "m(H)": "m of H",
    "t(H) + 2m(H)": "t of H plus 2 times m of H",
    "O(D(n) + t(H))": "big O of D of n plus t of H",
    "D(n) + t(H) − 1": "D of n plus t of H minus 1",
    "D(n) + 1 + 2m(H)": "D of n plus 1 plus 2 times m of H",
    "O(t(H))": "big O of t of H",
    "t(H) + c": "t of H plus c",
    "m(H) − c + 2": "m of H minus c plus 2",
    "s(k)": "s of k",
    "2 + s(0) + s(1) + … + s(k − 2)": "2 plus s of 0 plus s of 1, and so on, up to s of k minus 2",
    "o(lg n)": "little o of log base 2 of n",
    "o(n lg n)": "little o of n log base 2 of n",
    "both: O(m α(n)), and α(n) ≤ 4 in use": "both, big O of m times alpha of n, and alpha of n is at most 4 in use",
    "A_k(j)": "A sub k of j",
    "A_k(1) ≥ n": "A sub k of 1 is at least n",
    "α(10⁶) = 4": "alpha of 10 to the 6th equals 4",
})

# Foundations
SPOKEN.update({
    "f(n) = o(g(n))": "f of n is little o of g of n",
    "2n = o(n²)": "2 n is little o of n squared",
    "o(n²)": "little o of n squared",
    "o(g(n))": "little o of g of n",
    "n! = o(nⁿ)": "n factorial is little o of n to the n",
    "n! = ω(2ⁿ)": "n factorial is little omega of 2 to the n",
    "pass j inserts A[j] into A[1..j − 1]": "pass j inserts A at j into A from 1 to j minus 1",
    "A[1..j − 1]: the first j − 1 keys, sorted": "A from 1 to j minus 1, the first j minus 1 keys, sorted",
    "key = A[j]": "key equals A at j",
    "A[i] > key": "A at i is greater than key",
    "A[i] ≥ key": "A at i is at least key",
    "A[1..j − 1]": "A from 1 to j minus 1",
    "A[j..n]": "A from j to n",
    "A[j + 1..n]": "A from j plus 1 to n",
    "A[1..j]": "A from 1 to j",
    "A[1..7]": "A from 1 to 7",
    "A[p..q]": "A from p to q",
    "A[p..k − 1]": "A from p to k minus 1",
    "A[i..j]": "A from i to j",
    "A[i..n]": "A from i to n",
    "A[low..high]": "A from low to high",
    "A[low..mid]": "A from low to mid",
    "A[mid + 1..high]": "A from mid plus 1 to high",
    "A[1..5]": "A from 1 to 5",
    "A[2..2]": "A from 2 to 2",
    "A[2..4]": "A from 2 to 4",
    "A[2..8]": "A from 2 to 8",
    "A[3..3]": "A from 3 to 3",
    "A[3..6]": "A from 3 to 6",
    "A[3..12]": "A from 3 to 12",
    "A[6..8]": "A from 6 to 8",
    "best ending at 6: A[3..6], sum 11": "best ending at 6, A from 3 to 6, sum 11",
    "best starting at 7: A[7..10], sum −1": "best starting at 7, A from 7 to 10, sum negative 1",
    "crossing: A[3..10], sum 11 − 1 = 10": "crossing, A from 3 to 10, sum 11 minus 1 equals 10",
    "left half's best: A[3..6], sum 11": "left half's best, A from 3 to 6, sum 11",
    "right half's best: A[8..10], sum 8": "right half's best, A from 8 to 10, sum 8",
    "best of three: A[3..6], sum 11": "best of three, A from 3 to 6, sum 11",
    "Σ (t_j − 1)": "the sum of the quantity t sub j minus 1",
    "2·Σ (t_j − 1) = 30": "2 times the sum of the quantity t sub j minus 1, equals 30",
    "n + 3·(n − 1) + Σ t_j + 2·Σ (t_j − 1)": "n plus 3 times the quantity n minus 1, plus the sum of t sub j, plus 2 times the sum of the quantity t sub j minus 1",
    "lines executed = n + 3·(n − 1) + Σt_j + 2·Σ(t_j − 1)": "lines executed equals n plus 3 times the quantity n minus 1, plus the sum of t sub j, plus 2 times the sum of the quantity t sub j minus 1",
    "mid = ⌊(low + high)/2⌋": "mid equals the floor of the quantity low plus high, over 2",
    "c·n^k·lg^p n": "c times n to the power k times log base 2 of n to the power p",
    "the lab's recurrences, f(n) = c·n^k·lg^p n": "the lab's recurrences, f of n equals c times n to the power k times log base 2 of n to the power p",
    "n²·lg² n": "n squared times the square of log base 2 of n",
})

# Advanced Design and Analysis Techniques
SPOKEN.update({
    "r(n): best first piece plus best rest": "r of n, the best first piece plus the best rest",
    "s(j) records the first piece to cut": "s of j records the first piece to cut",
    "r(j)": "r of j",
    "s(j)": "s of j",
    "r(n)": "r of n",
    "s(n)": "s of n",
    "pᵢ + r(j − i)": "p sub i plus r of j minus i",
    "r(j − i)": "r of j minus i",
    "n − s(n)": "n minus s of n",
    "s(n − s(n))": "s of the quantity n minus s of n",
    "a subtree pushed down costs w(i, j) more": "a subtree pushed down costs w of i and j more",
    "e[i, r − 1] + e[r + 1, j] + w(i, j)": "e of i and r minus 1, plus e of r plus 1 and j, plus w of i and j",
    "w(r + 1, j)": "w of r plus 1 and j",
    "w(i, j)": "w of i and j",
    "c.freq · d(c)": "c dot freq times d of c",
    "d(c)": "d of c",
    "(a.freq − x.freq)·(d(a) − d(x))": "a dot freq minus x dot freq, times the quantity d of a minus d of x",
    "−(a.freq − x.freq)·(d(a) − d(x))": "minus the quantity a dot freq minus x dot freq, times the quantity d of a minus d of x",
    "w₀ − w(e)": "w nought minus w of e",
    "T     0    0↑    0↑    0↑    0↑    1↖": "row T, 0, then 0 up, 0 up, 0 up, 0 up, and 1 diagonal",
    "A     0    0↑    0↑    0↑    1↖    1↑": "row A, 0, then 0 up, 0 up, 0 up, 1 diagonal, and 1 up",
    "B     0   [1↖]   1←    1←    1↑    1↑": "row B, 0, then 1 diagonal on the path, 1 left, 1 left, 1 up, and 1 up",
    "L     0    1↑   [2↖]   2←    2←    2←": "row L, 0, then 1 up, 2 diagonal on the path, 2 left, 2 left, and 2 left",
    "E     0    1↑    2↑   [3↖]  [3←]  [3←]": "row E, 0, then 1 up, 2 up, 3 diagonal on the path, 3 left on the path, and 3 left on the path",
})

# Parallel, Matrix, Linear and Number Algorithms
SPOKEN.update({
    "T∞(n) = max(T∞(n − 1), T∞(n − 2)) + Θ(1) = Θ(n)": "T infinity of n equals the max of T infinity of n minus 1 and T infinity of n minus 2, plus theta of 1, which is theta of n",
    "M∞(n) = M∞(n/2) + Θ(lg n) = Θ(lg² n)": "M infinity of n equals M infinity of n over 2, plus theta of log n, which is theta of log squared n",
    "span:  T∞(n) = T∞(n/2) + Θ(n) = Θ(n)": "span, T infinity of n equals T infinity of n over 2, plus theta of n, which is theta of n",
    "T∞(n) = T∞(n/2) + Θ(n) = Θ(n)": "T infinity of n equals T infinity of n over 2, plus theta of n, which is theta of n",
    "P-MERGE span: PM∞(n) = PM∞(3n/4) + Θ(lg n) = Θ(lg² n)": "P-MERGE span, P M infinity of n equals P M infinity of 3 n over 4, plus theta of log n, which is theta of log squared n",
    "sort span:  T∞(n) = T∞(n/2) + Θ(lg² n) = Θ(lg³ n)": "sort span, T infinity of n equals T infinity of n over 2, plus theta of log squared n, which is theta of log cubed n",
    "π[i]": "pi of i",
    "yᵢ = b[π[i]] − (lᵢ₁·y₁ + … + lᵢ,ᵢ₋₁·yᵢ₋₁)": "y sub i equals b at pi of i, minus the sum of l sub i j times y sub j for j from 1 to i minus 1",
    "xᵢ = (yᵢ − (uᵢ,ᵢ₊₁·xᵢ₊₁ + … + uᵢₙ·xₙ))/uᵢᵢ": "x sub i equals y sub i minus the sum of u sub i j times x sub j for j from i plus 1 to n, all over u sub i i",
    "u₂₂ = 3 − (1/2)·8 = −1": "u sub 2 2 equals 3 minus one half times 8, which is negative 1",
    "[[3, 1], [0, 2]]": "the matrix with rows 3, 1 and 0, 2",
    "U = [[3, 1], [0, 2]]": "U equals the matrix with rows 3, 1 and 0, 2",
    "A = [[0, 2], [3, 1]]": "A equals the matrix with rows 0, 2 and 3, 1",
    "[[0, 2], [3, 1]]": "the matrix with rows 0, 2 and 3, 1",
    "[[1, 3, 2], [2, 2, 5], [4, 1, 3]]": "the matrix with rows 1, 3, 2, then 2, 2, 5, then 4, 1, 3",
    "[[1, 2], [2, 4]]": "the matrix with rows 1, 2 and 2, 4",
    "[[1, 2, 2], [4, 4, 2], [2, 6, 4]]": "the matrix with rows 1, 2, 2, then 4, 4, 2, then 2, 6, 4",
    "A = [[1, 3], [2, 8]]": "A equals the matrix with rows 1, 3 and 2, 8",
    "[[2, 8], [1, 3]]": "the matrix with rows 2, 8 and 1, 3",
    "(ω₈ᵏ)² = ω₄ᵏ": "the square of omega sub 8 to the power k equals omega sub 4 to the power k",
    "Lamé: O(lg b) recursive calls": "Lamé, big O of log b recursive calls",
    "cᵢ = mᵢ·(mᵢ⁻¹ mod nᵢ)": "c sub i equals m sub i times the inverse of m sub i modulo n sub i",
    "2¹⁰²³ = (2¹¹)⁹³ ≡ 1": "2 to the power 1023 equals 2 to the power 11, raised to the power 93, which is congruent to 1",
    "A(x) = A_e(x²) + x·A_o(x²)": "A of x equals A even of x squared, plus x times A odd of x squared",
    "A_e(x) = a₀ + a₂x + a₄x² + …": "A even of x equals a sub 0 plus a sub 2 x plus a sub 4 x squared, and so on",
    "A_o(x) = a₁ + a₃x + a₅x² + …": "A odd of x equals a sub 1 plus a sub 3 x plus a sub 5 x squared, and so on",
    "n = pq, φ(n) = (p − 1)·(q − 1)": "n equals p times q, and phi of n equals the quantity p minus 1, times the quantity q minus 1",
    "e coprime to φ(n), d = e⁻¹ mod φ(n)": "e coprime to phi of n, and d equals the inverse of e modulo phi of n",
    "φ(n) = (p − 1)·(q − 1)": "phi of n equals the quantity p minus 1, times the quantity q minus 1",
    "φ(n) = 42·66 = 2772": "phi of n equals 42 times 66, which is 2772",
    "φ(n) = 10·16 = 160": "phi of n equals 10 times 16, which is 160",
    "O(m α(n))": "big O of m times alpha of n",
    "α(n)": "alpha of n",
    "φ(n)": "phi of n",
    "M = (S, ℐ)": "M equals the pair S and script I",
})
