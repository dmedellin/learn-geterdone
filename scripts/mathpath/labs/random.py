"""Randomised Algorithms -- five modes, and not one figure that is a single run.

THE HAZARD THIS COURSE IS FOR. A randomised algorithm's cost is a DISTRIBUTION,
and a page that prints one run of it has printed a sample and called it a
property. Every mode here therefore prints three different kinds of number
side by side, and never one without the others:

    over every execution     the exact distribution, enumerated or computed by
                             recursion over the algorithm's own state, with
                             every probability an exact fraction
    over the seeds shown     the mean of a stated number of seeded runs, which
                             is a MEASUREMENT and is labelled as one
    the proved bound         the inequality the course states, printed beside
                             the exact quantity it bounds, so the reader can
                             see how much slack it has

The gap between the second and the first is the lesson. `costs` opens on a
sorted input at n = 8: with a fixed pivot it costs 28 comparisons every single
time, with a random pivot the exact expectation is 2369/140 and the mean over
120 seeds is a different number again. None of those three is the other two.

ALWAYS, OR WITH HIGH PROBABILITY. Every bound on this page says which, in those
words, and where it is the second kind the page SHOWS a run that misses it:

  always          quicksort's comparison count never exceeds n(n − 1)/2, and
                  the exact distribution's support is checked to sit inside it
  with high       Karger's contraction returns a given minimum cut with
  probability     probability at least 2/(n(n − 1)), and `karger` lists the
                  seeds among the ones it ran where it returned something else
  with high       at least three quarters of the bases are Miller-Rabin
  probability     witnesses for a composite, and `witness` prints the STRONG
                  LIARS -- the bases that are not -- and the smallest of them,
                  because "a is not a witness" is exactly the run where a
                  single-base test is wrong
  in expectation  a uniformly random assignment satisfies 7m/8 clauses, and
                  `max3sat` prints the assignments that do worse, the number of
                  them, and the best assignment there is

THE GENERATOR IS THE ONE simulate.py ARGUED FOR, AND IT IS NOT REBUILT HERE.
`algo_core.SEEDED_JS` is MINSTD -- a = 16807, c = 0, m = 2^31 − 1, PRIME -- over
`sysdesign_core.lcgStream`, with the splitmix64 finaliser on the seed. Every
draw in this kit is consumed as `x % k` (a pivot index, a contraction, a coin),
which is exactly the consumption a power-of-two modulus destroys: under the
glibc parameters the rest of this library uses, x % 4 runs 0, 1, 2, 3 forever
and a mode whose whole claim is "one run is not the expectation" would have
been demonstrating the opposite. The seed is mixed because an LCG's k-th value
is affine in its seed, and four of these five modes hand the reader a seed
slider. Nothing here writes a second generator.

WHAT IS COMPUTED AND WHAT IT IS CHECKED AGAINST. `algo_core.RANDOM_JS` holds
the arithmetic -- `shuffleFrequencies`, `kargerExact`, `minCutBrute`,
`strongTest`, `witnessCount`, `max3satEnumerate`, and the Markov and Chebyshev
bounds over a pmf -- and nothing here reimplements one. What this kit adds is
the second opinion:

  the closed form against    `rqsPmf` builds the comparison distribution of
  the enumeration            randomised quicksort by recursion over subproblem
                             SIZES, and `rqsClosed` evaluates 2(n + 1)H_n − 4n
                             with `sysdesign_core.harmonic` exact. The two are
                             computed from different definitions and the page
                             prints them in the same row.
  the measurement against    every mode runs the shipped algorithm over the
  the enumeration            seeds a slider names and prints the sample mean as
                             a fraction beside the exact one. Neither is
                             allowed to stand in for the other.
  the output against the     `rqsRun` returns `ordered` and `permutation`, both
  question that was asked    checked on the array it produced, and the panel
                             prints them. A sorting arm whose only assertion is
                             a comparison COUNT is the defect that kept an
                             unsorted array in this repository for months: an
                             unsorted array has a comparison count too.
  every minimum cut, not     `karger` enumerates every bipartition, collects
  the one that was asked     ALL the minimum cuts, and prints the exact
  about                      probability of each. `kargerExact` answers about
                             one cut; the algorithm succeeds if it returns any
                             of them, and those are different numbers.

THE MODES:

  shuffle    both shuffles over EVERY tape, the exact probability of each
             permutation, the total variation distance from uniform, and n!
             against n^n -- the divisibility argument that proves the naive
             swap cannot be uniform whatever a sample shows. The slider offers
             n = 3 to 5, because 120 bars is as many as the figure can carry;
             `rkShuffleCap` refuses above six for the naive swap and above
             seven for Fisher-Yates, which are different numbers because the
             tape counts are n^n and n!
  costs      randomised quicksort: the fixed-pivot count on the input the
             reader chose, the exact distribution over every execution, the
             closed form, the mean over the seeds shown, and Markov and
             Chebyshev against the exact tail
  karger     the exact success probability by recursion over contraction
             states, every minimum cut enumerated, the 2/(n(n − 1)) bound, the
             seeds that missed, and what repetition does to all of it
  witness    the strong test's chain, the exact fraction of bases that are
             witnesses, the strong liars themselves, the Fermat test beside it
             on a Carmichael number, and the error after t random bases
  max3sat    every assignment enumerated, the exact mean, 7m/8, the clause that
             repeats a variable and breaks the equality, the best assignment,
             and the mean over the seeds shown

BLOCKS PER MODE. RATIONAL_JS, STREAM_JS, COUNT_JS, RFIXED_JS, SEEDED_JS,
ORACLE_JS, RANDOM_JS and this kit's own block are on every page here.
ORACLE_JS is on all five and not only on the modes that enumerate, because
`oracleCap` is what every cap in this kit refuses through -- including
`rkShuffleCap` -- and a page missing it would throw a ReferenceError that the
mode's own catch would then report to the reader as "the instance is too big".
That is why each catch here re-throws anything that is not a cap refusal.
HARMONIC_JS is added only by `costs`, the one mode with a closed form to check
its enumeration against, and DIGRAPH_JS only by `karger`, the one mode with a
graph.

Measured, gzipped, on a real shipped lesson page with this lab swapped in --
Algorithms course 1 lesson 1, whose body is heavier than the median, so these
run about 2 KB above the tables in graphkit.py and flowkit.py. Against the
repository's 62 KB ceiling:

    shuffle 45.3   max3sat 45.5   witness 45.9   costs 46.6   karger 50.9

Re-derive them rather than trusting them. `karger` is the heaviest because it
is the only mode carrying the directed-graph representation and its renderer;
the four others differ by less than a kilobyte, because RANDOM_JS is one block
and a mode cannot take half of it.

WHAT RANDOM_JS SHIPS THAT NO MODE HERE CALLS, named rather than left to be
discovered: `reservoir` and its k/n retention claim. It is on every page in
this kit because RANDOM_JS is indivisible, and there is no lesson behind it
yet. Nothing in this repository executed it either until this kit's mathcheck
section did -- the claim is now enumerated over every tape at six items or
fewer -- and a sixth mode is where it belongs, costing nothing on the wire.

NOTHING HERE ROUNDS EXCEPT A PRINTED DECIMAL, AND NOTHING IS IRRATIONAL. Every
probability, expectation, variance, mean, tail and bound in this kit is a ratio
of two integers, held as BigInt over BigInt. `Rfixed` prints a decimal beside
the fraction where the fraction is long, and that is a rounding of the
PRINTING: the fraction is printed too. simulate.py has three genuinely
irrational printed quantities and labels each; this kit has none, because a
standard error is never taken -- the exact variance is available, so Chebyshev
is applied to it directly.

EVERY PRESET PINS WHAT IT PRINTS, AND NO PRESET CARRIES A NOTE. Each of the 24
presets here used to carry a `label` and a `note`, both prose about an outcome
and neither readable by any check in this repository -- a sweep of fifteen kits
found 57 of those strings false about the lab they described. The notes are
deleted (they were embedded in every page as `SHP`/`CSP`/`KGP`/`WTP`/`MSP` data
and never printed) and each preset now carries `expect`: {kpi element id: the
exact text the page prints}, one to three tiles, read off the running kit with
`node scripts/labcheck.js --observe <page>`. scripts/labcheck.js selects the
option on the BUILT page, dispatches the menu's change handler and compares
the tile. Of the three kinds of number above, the presets pin the EXACT ones
and the BOUNDS; a measured mean is reproducible under the seeded generator but
pinning it would check the seed slider's default rather than the lab's claim.
See `_expect` below and scripts/mathpath/AGENTS.md for the rule.
"""

from .algo_core import (COUNT_JS, DIGRAPH_JS, ORACLE_JS, RANDOM_JS, RFIXED_JS,
                        SEEDED_JS)
from .algebra_core import RATIONAL_JS
from .common import Lab
from .sysdesign_core import HARMONIC_JS, STREAM_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

RKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     Two grammars, both 1-based because that is what the prose uses.

       an edge      `u-v`, repeated to make a parallel pair, which Karger's
                    algorithm needs: the multiplicity between two supernodes is
                    the whole reason contraction favours a small cut, and a
                    representation that folded a repeated edge into one entry
                    would quietly change the probability it is there to compute.
       a clause     `1 2 -3`, a signed variable per literal, clauses separated
                    by a semicolon or a newline. `-3` is NOT x3. */
  var RK_MAXN = 12;
  var RK_MAXEDGES = 24;
  var RK_MAXVARS = 12;
  var RK_MAXCLAUSES = 14;

  function rkPieces(text, re) {
    var parts = String(text).split(re), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }
  function rkParseGraph(text, maxN) {
    maxN = maxN === undefined ? 8 : maxN;
    var cl = rkPieces(text, /[,;\n]+/), raw = [], n = 0, i;
    if (!cl.length) return { bad: 'write at least one edge' };
    if (cl.length > RK_MAXEDGES) return { bad: 'that is more than ' + RK_MAXEDGES + ' edges' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*(?:-|to)\s*(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as an edge' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'a loop at ' + u + ' is never contracted, so it cannot be an edge' };
      raw.push([u, v]);
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (n < 3) return { bad: 'a cut needs at least three vertices to be interesting' };
    var G = dgNew(n, false);
    for (i = 0; i < raw.length; i += 1) dgAdd(G, raw[i][0] - 1, raw[i][1] - 1, 1, 0);
    return { G: G, n: n };
  }
  function rkParseCnf(text, maxVars, maxClauses) {
    maxVars = maxVars === undefined ? RK_MAXVARS : maxVars;
    maxClauses = maxClauses === undefined ? RK_MAXCLAUSES : maxClauses;
    var cl = rkPieces(text, /[;\n]+/), clauses = [], n = 0, i, k;
    if (!cl.length) return { bad: 'write at least one clause' };
    if (cl.length > maxClauses) return { bad: 'that is more than ' + maxClauses + ' clauses' };
    for (i = 0; i < cl.length; i += 1) {
      var lits = rkPieces(cl[i], /[\s,]+/), out = [];
      for (k = 0; k < lits.length; k += 1) {
        if (!/^-?\d+$/.test(lits[k])) return { bad: 'cannot read "' + lits[k] + '" as a literal' };
        var lit = parseInt(lits[k], 10);
        if (lit === 0) return { bad: 'there is no variable 0; the literals are 1, -1, 2, -2 and so on' };
        if (Math.abs(lit) > maxVars) return { bad: 'variable ' + Math.abs(lit) + ' is past ' + maxVars };
        out.push(lit);
        if (Math.abs(lit) > n) n = Math.abs(lit);
      }
      if (!out.length) return { bad: 'clause ' + (i + 1) + ' is empty' };
      clauses.push(out);
    }
    return { formula: { n: n, clauses: clauses } };
  }
  function rkClauseText(cl) {
    return cl.map(function (l) { return (l < 0 ? '¬x' : 'x') + Math.abs(l); }).join(' ∨ ');
  }
  function rkAssignText(a) {
    return (a || []).map(function (v, i) { return 'x' + (i + 1) + '=' + (v ? 'T' : 'F'); }).join('  ');
  }
  function rkPlural(k, one, many) { return k === 1 ? one : many; }
  function rkClamp(v, lo, hi) {
    if (!isFinite(v)) return lo;
    return Math.max(lo, Math.min(hi, Math.round(v)));
  }
  /* Every permutation of 0..n-1, as a callback rather than a list, because the
     caller runs an algorithm on each and never needs them all at once. */
  function rkForEachPermutation(n, fn) {
    var a = new Array(n).fill(0), used = new Array(n).fill(false);
    (function go(k) {
      if (k === n) { fn(a); return; }
      for (var v = 0; v < n; v += 1) {
        if (used[v]) continue;
        used[v] = true; a[k] = v;
        go(k + 1);
        used[v] = false;
      }
    })(0);
  }
  /* A rational as "p/q" and, where the fraction is long, a decimal beside it.
     The decimal is a rounding of the PRINTING and the fraction is always
     there: no verdict on any of these pages is read off the decimal. */
  function rkBoth(a, places) {
    var t = Rtext(a);
    if (t.length <= 7 && a.d === 1n) return t;
    /* Below 1e-4 a decimal is a row of zeros and says nothing, so it is
       quoted as "1 in N" -- which is how a failure probability is read in
       practice, and it is still exact. */
    if (!Rzero(a) && Rcmp(Rabs(a), R(1n, 10000n)) < 0) return t + ' = ' + RoneIn(a);
    return t + ' = ' + Rfixed(a, places === undefined ? 4 : places);
  }

  /* --------------------------------------------------------------- drawing

     Grouped bars: one group per row, one bar per series, the exact
     distribution and the measured one in the same group so the gap between
     them is the picture. The function that builds the markup returns a string
     and touches nothing, which is what lets mathcheck assert on it. */
  var RK_BOX = { left: 36, right: 498, base: 196, top: 30 };
  function rkBarsSvg(rows, series, opts) {
    opts = opts || {};
    var box = opts.box || RK_BOX, n = rows.length;
    var maxV = opts.maxY || 0;
    if (!opts.maxY) rows.forEach(function (r) {
      r.values.forEach(function (v) { if (v > maxV) maxV = v; });
    });
    if (!(maxV > 0)) maxV = 1;
    var span = box.base - box.top, W = (box.right - box.left) / Math.max(1, n);
    var pad = Math.min(6, W * 0.18), bw = (W - 2 * pad) / Math.max(1, series.length);
    var every = Math.ceil(n / 24);
    var s = '<line x1="' + box.left + '" y1="' + box.base + '" x2="' + (box.right + 4)
          + '" y2="' + box.base + '" stroke="var(--line-strong)" />'
          + '<line x1="' + box.left + '" y1="' + box.top + '" x2="' + box.left + '" y2="'
          + box.base + '" stroke="var(--line-strong)" />';
    rows.forEach(function (r, i) {
      var x0 = box.left + i * W + pad;
      r.values.forEach(function (v, k) {
        var h = Math.max(0, Math.min(1, v / maxV)) * span;
        s += '<rect x="' + (x0 + k * bw).toFixed(1) + '" y="' + (box.base - h).toFixed(1)
          + '" width="' + Math.max(1, bw - 1).toFixed(1) + '" height="' + h.toFixed(1)
          + '" fill="' + series[k].colour + '" opacity="' + (series[k].faint ? 0.5 : 0.9) + '" />';
      });
      if (i % every === 0) {
        s += '<text x="' + (x0 + (W - 2 * pad) / 2).toFixed(1) + '" y="' + (box.base + 14)
          + '" text-anchor="middle" font-size="10" fill="var(--muted)">' + r.label + '</text>';
      }
    });
    /* A horizontal reference: the uniform level a shuffle is compared with,
       or an expectation. It is a REFERENCE and no verdict is read off it. */
    (opts.rules || []).forEach(function (r) {
      var y = box.base - Math.max(0, Math.min(1, r.value / maxV)) * span;
      s += '<line x1="' + box.left + '" y1="' + y.toFixed(1) + '" x2="' + box.right
        + '" y2="' + y.toFixed(1) + '" stroke="' + r.colour
        + '" stroke-width="2" stroke-dasharray="6 4" />'
        + '<text x="' + (box.right - 2) + '" y="' + Math.max(box.top + 10, y - 4).toFixed(1)
        + '" text-anchor="end" font-size="11" font-weight="700" fill="' + r.colour + '">'
        + r.label + '</text>';
    });
    (opts.marks || []).forEach(function (m) {
      var x = box.left + (m.at + 0.5) * W;
      s += '<line x1="' + x.toFixed(1) + '" y1="' + box.top + '" x2="' + x.toFixed(1) + '" y2="'
        + box.base + '" stroke="' + m.colour + '" stroke-width="2" stroke-dasharray="5 4" />'
        + '<text x="' + Math.min(box.right - 40, x + 4).toFixed(1) + '" y="' + (box.top + 12)
        + '" font-size="11" font-weight="700" fill="' + m.colour + '">' + m.label + '</text>';
    });
    series.forEach(function (ser, k) {
      s += '<rect x="' + (box.left + 6 + k * 168) + '" y="5" width="10" height="10" fill="'
        + ser.colour + '" opacity="' + (ser.faint ? 0.5 : 0.9) + '" />'
        + '<text x="' + (box.left + 21 + k * 168) + '" y="14" font-size="11" fill="var(--muted)">'
        + ser.label + '</text>';
    });
    return s;
  }
  function rkDrawBars(el, rows, series, opts) {
    var s = rkBarsSvg(rows, series, opts);
    if (el) el.innerHTML = s;
    return s;
  }

  /* ---------------------------------------------------------- shuffle

     `shuffleFrequencies` enumerates every tape. The tape counts are n! for
     Fisher-Yates and n^n for the naive swap, so the cap is not the same for
     the two and it is stated per kind rather than once. */
  function rkShuffleCap(n, kind) {
    return oracleCap('rkShuffle', n, kind === 'naive' ? 6 : 7);
  }
  function rkShuffleExact(n, kind) {
    rkShuffleCap(n, kind);
    return shuffleFrequencies(n, kind);
  }
  /* n! and n^n as BigInt, and whether the first divides the second. This is
     the PROOF, and it is why the mode does not rest on the frequencies: if n!
     does not divide n^n then n^n tapes cannot split evenly over n!
     permutations, whatever any sample suggests. It fails for every n >= 3. */
  function rkNaiveDivides(n) {
    var fact = 1n, i;
    for (i = 2n; i <= BigInt(n); i += 1n) fact *= i;
    var pow = BigInt(n) ** BigInt(n);
    return { factorial: fact, tapes: pow, divides: pow % fact === 0n,
             remainder: pow % fact };
  }
  /* Total variation distance from uniform: half the sum of |p - 1/N| over the
     N permutations, exact. Zero exactly when the shuffle is uniform, which is
     a single number the panel can print instead of a table the reader has to
     scan. */
  function rkTotalVariation(rows, total) {
    var u = R(1n, BigInt(total)), d = R(0n, 1n), seen = 0;
    rows.forEach(function (r) { d = Radd(d, Rabs(Rsub(r.probability, u))); seen += 1; });
    /* a permutation no tape produces still differs from uniform by 1/N */
    d = Radd(d, Rmul(R(BigInt(total - seen), 1n), u));
    return Rdiv(d, R(2n, 1n));
  }
  /* The same shuffle run over a range of SEEDS, through the kit's one
     generator. A measurement, and labelled as one everywhere it is printed. */
  function rkShuffleSeeds(n, seeds) {
    var freq = {}, s;
    for (s = 1; s <= seeds; s += 1) {
      var key = algoPermutation(n, s).join('');
      freq[key] = (freq[key] || 0) + 1;
    }
    return { freq: freq, seeds: seeds, distinct: Object.keys(freq).length };
  }

  /* -------------------------------------------- randomised quicksort

     THE COST IS A DISTRIBUTION AND THIS IS BOTH HALVES OF SAYING SO.

     `rqsRun` executes the algorithm: a pivot index taken from the seeded
     stream, a partition of a subarray of length L costing L - 1 comparisons,
     and -- the part that is not optional -- the array it produced, checked to
     be sorted AND to be a permutation of what went in. A sorting routine
     whose only assertion is a comparison count can return anything: an
     unsorted array has a comparison count too, and that is how a broken arm
     stayed in this repository for months.

     `rqsPmf` computes the distribution over EVERY execution. Not by
     enumerating pivot tapes -- that is n! of them and it is the wrong object,
     because the cost depends only on the SIZES the pivot splits the subarray
     into. So it is a bottom-up recursion on size: D(0) = D(1) = the point mass
     at 0, and

         D(k) = (k - 1) + (1/k) * sum over i of ( D(i) convolved D(k-1-i) )

     with every weight an exact rational. The expectation of D(n) must equal
     2(n + 1)H_n - 4n, which `rqsClosed` computes from `harmonic` -- a
     different definition, and the two are printed in one row. */
  function rqsSortedArray(a) {
    for (var i = 1; i < a.length; i += 1) if (a[i - 1] > a[i]) return false;
    return true;
  }
  function rqsSameMultiset(a, b) {
    if (a.length !== b.length) return false;
    var x = a.slice().sort(function (p, q) { return p - q; });
    var y = b.slice().sort(function (p, q) { return p - q; });
    for (var i = 0; i < x.length; i += 1) if (x[i] !== y[i]) return false;
    return true;
  }
  function rqsPartition(a, lo, hi, p, c) {
    var t = a[p]; a[p] = a[hi]; a[hi] = t;
    var pivot = a[hi], i = lo, j;
    for (j = lo; j < hi; j += 1) {
      c.compares += 1;
      if (a[j] < pivot) {
        if (i !== j) { var s = a[i]; a[i] = a[j]; a[j] = s; c.swaps += 1; }
        i += 1;
      }
    }
    if (i !== hi) { var u = a[i]; a[i] = a[hi]; a[hi] = u; c.swaps += 1; }
    return i;
  }
  /* draws === null is the FIXED rule: always the last element. That is the
     arm whose cost on a sorted input is n(n-1)/2 every time, which is the
     whole reason the other arm exists. */
  function rqsRun(input, draws) {
    var a = input.slice(), c = counter(), trace = [], at = 0, over = 0;
    (function go(lo, hi, depth) {
      if (lo >= hi) return;
      var len = hi - lo + 1, p;
      if (draws === null || draws === undefined) p = hi;
      else {
        if (at >= draws.length) { over += 1; }
        p = lo + (draws[at % draws.length] % len);
        at += 1;
      }
      trace.push({ at: trace.length, lo: lo, hi: hi, length: len, depth: depth, pivot: a[p] });
      var m = rqsPartition(a, lo, hi, p, c);
      go(lo, m - 1, depth + 1);
      go(m + 1, hi, depth + 1);
    })(0, a.length - 1, 0);
    return runOf({ sorted: a, ordered: rqsSortedArray(a),
                   permutation: rqsSameMultiset(a, input),
                   partitions: trace.length, drawsUsed: at, drawsShort: over },
                 usedCounts(c), trace);
  }
  function rqsConvolve(L, Rt, weight, into, shift) {
    Object.keys(L).forEach(function (lk) {
      Object.keys(Rt).forEach(function (rk) {
        var k = shift + Number(lk) + Number(rk);
        var p = Rmul(weight, Rmul(L[lk], Rt[rk]));
        into[k] = into[k] === undefined ? p : Radd(into[k], p);
      });
    });
  }
  function rqsPmf(n, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('rqsPmf', n, cap);
    var one = {}; one[0] = R(1n, 1n);
    var table = [one, one], k, i;
    for (k = 2; k <= n; k += 1) {
      var acc = {}, w = R(1n, BigInt(k));
      for (i = 0; i < k; i += 1) rqsConvolve(table[i], table[k - 1 - i], w, acc, k - 1);
      table.push(acc);
    }
    return table[n];
  }
  function rqsPairs(map) {
    return Object.keys(map).map(Number).sort(function (a, b) { return a - b; })
      .map(function (k) { return [k, map[k]]; });
  }
  function rqsTotal(pairs) {
    var t = R(0n, 1n);
    pairs.forEach(function (p) { t = Radd(t, p[1]); });
    return t;
  }
  function rqsClosed(n) {
    if (n <= 1) return R(0n, 1n);
    return Rsub(Rmul(R(BigInt(2 * (n + 1)), 1n), harmonic(n, 1)), R(BigInt(4 * n), 1n));
  }
  /* THE INDEPENDENT ORACLE for rqsPmf, and a theorem in its own right.

     rqsPmf reasons about subproblem SIZES and never sorts anything. This runs
     the shipped algorithm with the FIXED last-element pivot over every one of
     the n! input orders and tallies what it counted. The two distributions
     must be identical, because randomising the pivot on a fixed input and
     fixing the pivot on a uniformly random input are the same experiment --
     which is a claim this course makes and which is therefore computed here
     rather than asserted.

     It also checks the thing a comparison count cannot check: every one of the
     n! runs is required to have produced a sorted permutation of its input.
     An arm whose only assertion is a count will happily return an unsorted
     array, and has. */
  function rqsOverOrders(n, cap) {
    cap = cap === undefined ? 7 : cap;
    oracleCap('rqsOverOrders', n, cap);
    var acc = {}, total = 0n, bad = 0;
    rkForEachPermutation(n, function (a) {
      var run = rqsRun(a, null);
      if (!run.result.ordered || !run.result.permutation) bad += 1;
      var c = run.counts.compares || 0;
      acc[c] = (acc[c] || 0n) + 1n;
      total += 1n;
    });
    var pmf = {};
    Object.keys(acc).forEach(function (k) { pmf[k] = R(acc[k], total); });
    return { pmf: pmf, orders: total, allSorted: bad === 0, unsorted: bad };
  }
  /* Two pmfs, value by value, exactly. undefined on one side is probability
     zero, which is what makes this a comparison of DISTRIBUTIONS and not of
     the keys that happen to be present. */
  function rqsSamePmf(a, b) {
    var keys = {}, same = true;
    Object.keys(a).forEach(function (k) { keys[k] = true; });
    Object.keys(b).forEach(function (k) { keys[k] = true; });
    Object.keys(keys).forEach(function (k) {
      var x = a[k] === undefined ? R(0n, 1n) : a[k];
      var y = b[k] === undefined ? R(0n, 1n) : b[k];
      if (!Requ(x, y)) same = false;
    });
    return same;
  }

  /* The measurement: the same algorithm over seeds 1..S, and the sample mean
     as an exact fraction. `allSorted` is the guard -- every one of the S runs
     is checked to have produced a sorted permutation of its input, so the
     counts below are counts of a run that did the job. */
  function rqsSeeds(input, seeds) {
    var rows = [], total = 0n, lo = null, hi = null, hist = {}, ok = true, s;
    for (s = 1; s <= seeds; s += 1) {
      var run = rqsRun(input, algoStream(s, Math.max(1, input.length)));
      var c = run.counts.compares || 0;
      if (!run.result.ordered || !run.result.permutation || run.result.drawsShort) ok = false;
      rows.push({ seed: s, compares: c, partitions: run.result.partitions });
      total += BigInt(c);
      hist[c] = (hist[c] || 0) + 1;
      if (lo === null || c < lo) lo = c;
      if (hi === null || c > hi) hi = c;
    }
    return { rows: rows, seeds: seeds, mean: R(total, BigInt(seeds)),
             min: lo, max: hi, hist: hist, allSorted: ok };
  }
  /* How many of those seeds landed at or above a threshold, as a fraction --
     the measured tail, to put beside the exact one and beside Markov's and
     Chebyshev's bounds on it. */
  function rqsSeedTail(sample, t) {
    var hits = sample.rows.filter(function (r) { return r.compares >= t; });
    return { hits: hits.length, seeds: hits.map(function (r) { return r.seed; }),
             fraction: R(BigInt(hits.length), BigInt(sample.seeds)) };
  }

  /* -------------------------------------------------------------- Karger

     `kargerExact` answers about ONE cut. The algorithm succeeds if it returns
     ANY minimum cut, and on a graph with several of them those are different
     numbers -- so the page enumerates the minimum cuts and adds their exact
     probabilities up. Reporting the first number as the success probability
     would understate it, silently, on exactly the graphs a reader tries. */
  function rkMinCuts(G, cap) {
    cap = cap === undefined ? RK_KARGER_CAP : cap;
    oracleCap('rkMinCuts', G.n, cap);
    var best = null, cuts = [], mask, v;
    for (mask = 1; mask < (1 << (G.n - 1)); mask += 1) {
      var side = [];
      for (v = 0; v < G.n; v += 1) side.push((mask >> v) & 1);
      var size = 0;
      G.arcs.forEach(function (a) { if (side[a.u] !== side[a.v]) size += 1; });
      if (best === null || size < best) { best = size; cuts = [side]; }
      else if (size === best) cuts.push(side);
    }
    return { size: best, cuts: cuts, count: cuts.length };
  }
  function rkSideKey(side) {
    var flip = side[0] === 1;
    return side.map(function (b) { return flip ? 1 - b : b; }).join('');
  }
  function rkSideText(side) {
    var a = [], b = [];
    side.forEach(function (x, v) { (x ? b : a).push(v + 1); });
    return '{' + a.join(', ') + '} | {' + b.join(', ') + '}';
  }
  /* The exact probability of returning SOME minimum cut, and the per-cut
     breakdown the panel prints under it. */
  var RK_KARGER_CAP = 8;
  function rkKargerTotal(G, cap) {
    var mc = rkMinCuts(G, cap), total = R(0n, 1n);
    var rows = mc.cuts.map(function (side) {
      var ex = kargerExact(G, side, cap === undefined ? RK_KARGER_CAP : cap);
      total = Radd(total, ex.probability);
      return { side: side, key: rkSideKey(side), text: rkSideText(side),
               probability: ex.probability, states: ex.states };
    });
    var N = BigInt(G.n);
    var bound = R(2n, N * (N - 1n));
    return { size: mc.size, rows: rows, count: mc.count, any: total, bound: bound,
             beatsBound: Rcmp(total, bound) >= 0 };
  }
  /* The measurement, and the seeds that MISSED. A with-high-probability bound
     is not an always bound, and the honest way to say so is to name the runs
     where the algorithm returned a bigger cut. */
  function rkKargerSeeds(G, seeds, minSize) {
    var rows = [], hits = 0, s;
    for (s = 1; s <= seeds; s += 1) {
      var run = kargerRun(G, s);
      var two = run.result.groups === 2;
      var got = run.result.cutSize, ok = two && got === minSize;
      if (ok) hits += 1;
      rows.push({ seed: s, cutSize: got, ok: ok, groups: run.result.groups,
                  key: two ? rkSideKey(rkGroupSide(run.result.group)) : null,
                  rounds: run.counts.rounds || 0 });
    }
    return { rows: rows, seeds: seeds, hits: hits,
             rate: R(BigInt(hits), BigInt(seeds)),
             missed: rows.filter(function (r) { return !r.ok; }).map(function (r) { return r.seed; }) };
  }
  /* kargerRun leaves a group label per vertex; two labels survive on a
     connected graph, and which side is which does not matter, so it is
     normalised the way rkSideKey is. A run that stopped with more than two
     groups -- which only a disconnected graph produces -- is reported as such
     rather than collapsed into a bipartition it is not. */
  function rkGroupSide(group) {
    var first = group[0];
    return group.map(function (g) { return g === first ? 0 : 1; });
  }
  /* Amplification, exactly: t independent runs miss only if all t miss. */
  function rkAmplify(p, t) {
    var miss = Rsub(R(1n, 1n), p), acc = R(1n, 1n), i;
    for (i = 0; i < t; i += 1) acc = Rmul(acc, miss);
    return { success: Rsub(R(1n, 1n), acc), failure: acc };
  }
  /* The least t whose success probability reaches the target, by multiplying
     rather than by a logarithm -- exact, and it refuses rather than looping. */
  function rkTrialsFor(p, target, cap) {
    cap = cap === undefined ? 4000 : cap;
    if (Rcmp(p, R(0n, 1n)) <= 0) return null;
    var miss = Rsub(R(1n, 1n), p), acc = R(1n, 1n), want = Rsub(R(1n, 1n), target), t = 0;
    while (Rcmp(acc, want) > 0) {
      acc = Rmul(acc, miss);
      t += 1;
      if (t > cap) return null;
    }
    return t;
  }

  /* ------------------------------------------------------ Miller-Rabin

     `witnessCount` gives the exact fraction of bases that are witnesses. What
     this adds is the other side of it: the STRONG LIARS, the bases for which
     the test says nothing, because "at least three quarters are witnesses" is
     a statement whose content is that the remaining quarter exists. */
  function rkLiars(n, cap) {
    cap = cap === undefined ? 2047 : cap;
    oracleCap('rkLiars', n, cap);
    var liars = [], a;
    for (a = 2; a <= n - 2; a += 1) {
      var r = strongTest(n, a);
      if (r.valid && !r.witness) liars.push(a);
    }
    return { liars: liars, count: liars.length, smallest: liars.length ? liars[0] : null };
  }
  /* The Fermat test on the same bases, so a Carmichael number can be shown
     defeating one and not the other. a^(n-1) mod n, by the same squaring
     chain the strong test uses.

     THE COPRIME BASES ARE COUNTED SEPARATELY AND THAT IS NOT A DETAIL. "The
     Fermat test fails on a Carmichael number" is a statement about the bases
     COPRIME TO n: for those, a^(n-1) is 1 and the test learns nothing. A base
     sharing a factor with n is caught by the Fermat test too, and at n = 561
     there are 240 of those out of 558, so a lab that printed one fraction
     would have shown the Fermat test catching 561 about two times in five and
     called the Carmichael property refuted. Both fractions are printed, and
     the Carmichael verdict is read off the coprime one. */
  function rkFermatCount(n, cap) {
    cap = cap === undefined ? 2047 : cap;
    oracleCap('rkFermatCount', n, cap);
    var witnesses = 0, total = 0, coprime = 0, coprimeWitnesses = 0, liars = [], a;
    for (a = 2; a <= n - 2; a += 1) {
      total += 1;
      var v = powModTrace(a, n - 1, n).value, shares = rkGcd(BigInt(a), BigInt(n)) !== 1n;
      if (!shares) coprime += 1;
      if (v === 1n) liars.push(a);
      else { witnesses += 1; if (!shares) coprimeWitnesses += 1; }
    }
    return { witnesses: witnesses, total: total, coprime: coprime, liars: liars,
             coprimeWitnesses: coprimeWitnesses,
             fraction: total ? R(BigInt(witnesses), BigInt(total)) : R(0n, 1n),
             coprimeFraction: coprime ? R(BigInt(coprimeWitnesses), BigInt(coprime)) : R(0n, 1n),
             carmichael: coprimeWitnesses === 0 && coprime > 0 && total > coprime };
  }
  function rkGcd(a, b) { while (b) { var t = a % b; a = b; b = t; } return a < 0n ? -a : a; }
  /* The error after t independently chosen bases, exactly: it is the fraction
     of LIARS raised to t, not the 1/4^t the bound allows for. Both are
     printed, which is the point -- the bound is loose and the page says by
     how much on this n. */
  function rkErrorAfter(liarFraction, t) {
    var acc = R(1n, 1n), i;
    for (i = 0; i < t; i += 1) acc = Rmul(acc, liarFraction);
    return acc;
  }
  function rkQuarterAfter(t) {
    var acc = R(1n, 1n), i;
    for (i = 0; i < t; i += 1) acc = Rmul(acc, R(1n, 4n));
    return acc;
  }

  /* --------------------------------------------------------- MAX-3-SAT

     `max3satEnumerate` gives the exact mean over every assignment and the
     7m/8 claim beside it. What this adds is the shape of the distribution --
     how many assignments satisfy each number of clauses -- the OPTIMUM, and
     the measurement over seeds, because "the expectation is 7m/8" does not say
     that any particular random assignment reaches it, and the histogram shows
     the ones that do not. */
  function rkSatHistogram(formula, cap) {
    var ex = max3satEnumerate(formula, cap);
    var rows = Object.keys(ex.histogram).map(Number)
      .sort(function (a, b) { return a - b; })
      .map(function (k) {
        return { satisfied: k, count: ex.histogram[k],
                 probability: R(BigInt(ex.histogram[k]), ex.assignments) };
      });
    var below = R(0n, 1n), belowCount = 0;
    rows.forEach(function (r) {
      if (Rcmp(R(BigInt(8 * r.satisfied), 1n), R(BigInt(7 * formula.clauses.length), 1n)) < 0) {
        below = Radd(below, r.probability);
        belowCount += r.count;
      }
    });
    return { rows: rows, exact: ex, belowMean: below, belowCount: belowCount };
  }
  /* A uniformly random assignment per seed, from the coin tape. The mean over
     those seeds is a measurement; 7m/8 is the expectation. */
  function rkSatSeeds(formula, seeds) {
    var rows = [], total = 0n, lo = null, hi = null, s;
    for (s = 1; s <= seeds; s += 1) {
      var coins = algoCoins(s, formula.n);
      var assign = coins.map(function (b) { return b === 1; });
      var sat = satEval(formula, assign);
      rows.push({ seed: s, satisfied: sat, assignment: assign });
      total += BigInt(sat);
      if (lo === null || sat < lo) lo = sat;
      if (hi === null || sat > hi) hi = sat;
    }
    return { rows: rows, seeds: seeds, mean: R(total, BigInt(seeds)), min: lo, max: hi };
  }
  /* Which clauses have three distinct variables, per clause rather than as one
     verdict: the equality with 7m/8 fails exactly on the ones that do not, and
     a reader editing the formula should see WHICH clause broke it. */
  function rkClauseWidths(formula) {
    return formula.clauses.map(function (cl, i) {
      var vs = cl.map(function (l) { return Math.abs(l); }), seen = {}, dup = false, k;
      for (k = 0; k < vs.length; k += 1) { if (seen[vs[k]]) dup = true; seen[vs[k]] = true; }
      var models = 0, total = Math.pow(2, Object.keys(seen).length);
      /* the clause's own satisfying assignments, over its own variables */
      var vars = Object.keys(seen).map(Number);
      for (var mask = 0; mask < total; mask += 1) {
        var val = {};
        vars.forEach(function (v, j) { val[v] = !!(mask & (1 << j)); });
        var ok = cl.some(function (l) { return (l > 0) === val[Math.abs(l)]; });
        if (ok) models += 1;
      }
      return { index: i, clause: cl, text: rkClauseText(cl), width: cl.length,
               distinct: vars.length, repeats: dup, models: models, local: total,
               share: R(BigInt(models), BigInt(total)) };
    });
  }
"""


# ---------------------------------------------------------------------------
# One core per mode. A page ships only the blocks its mode calls: `shuffle`
# and `witness` need no graph and no oracle, `costs` needs the harmonic
# number it checks its enumeration against, and only `karger` carries the
# graph representation and its renderer.
# ---------------------------------------------------------------------------

_BASE_JS = (RATIONAL_JS + STREAM_JS + COUNT_JS + RFIXED_JS + SEEDED_JS
            + ORACLE_JS + RANDOM_JS + RKIT_JS)
_COSTS_JS = _BASE_JS + HARMONIC_JS
_GRAPH_JS = _BASE_JS + DIGRAPH_JS

# ORACLE_JS is on every page here and not only on the modes that enumerate:
# `oracleCap` is what every cap in this kit refuses through, including
# `rkShuffleCap`, and a page missing it would not refuse -- it would throw a
# ReferenceError that the mode's own catch would then print as if it were the
# refusal. Which is exactly why the catches below re-throw anything that is
# not a cap refusal: a catch that swallows a programming error turns a broken
# lab into a blank panel with a plausible sentence under it.
_REFUSAL_JS = r'''
  /* A cap refusal, and nothing else. oracleCap throws with this wording; any
     other error is a defect in the lab and must reach the console rather than
     be reported to the reader as an instance being too big. */
  function rkIsRefusal(e) { return /exceeds the exhaustive cap/.test(String(e && e.message)); }
'''


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the other Algorithms kits use.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, step, value)
    )


def _select(cid, label, options, chosen):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value, placeholder=None):
    """A text box. Nothing this kit's grammars use needs escaping in an
    attribute -- an edge is `1-2` and a clause is `1 2 -3` -- so the value
    ships in the markup rather than being assigned by the script. flowkit
    fills its box from the script because a flow arc carries a `>`, which a
    value attribute cannot hold without an entity that scripts/labcheck.js
    does not decode; there is no `>` here.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(value), _attr(placeholder or value))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)
        for tone, text in legend
    )
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
        '        <div class="inline-legend">%s</div>\n'
        "      </div>\n" % (name, subtitle, swatches)
    )


def _stage(inner):
    return '      <div class="lab-stage">%s</div>\n' % inner


def _svg(cid, box, alt):
    return '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)


def _table(cid, top=12):
    return ('      <div class="table-wrap" style="margin-top:%dpx;">'
            '<table class="tt" id="%s"></table></div>\n' % (top, cid))


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _js(text):
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
    """The preset table as data the script reads, not as branches.

    Every preset goes through the same parser the reader's own typing does, so
    a preset cannot show a number the typed version would not.
    """
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _expect(presets):
    """{preset id: {kpi element id: the exact text the page prints}}.

    A preset used to carry a `label` and a `note`, both prose about an outcome
    and neither readable by any check here -- a sweep of fifteen kits found 57
    of those strings false. The note is gone; what replaces it is this, and
    scripts/labcheck.js selects the option on the BUILT page, dispatches the
    menu's own change handler and compares getElementById(kpi).textContent
    against it. Every figure below was read off the running kit with
    `node scripts/labcheck.js --observe <page>`, never copied out of the code
    that computes it.

    THREE KINDS OF NUMBER, AND WHICH OF THEM IS PINNED. This kit prints exact
    quantities, measurements over the seeds the slider names, and proved
    bounds. All three are reproducible -- the generator is seeded -- but only
    the first and the third are statements about the algorithm, so those are
    what the presets pin. A measured mean is pinned nowhere here: it would
    pass, and it would be pinning the seed slider's default rather than the
    lab's claim.

    A tile is read with every OTHER control at the value the markup ships --
    120 seeds, 10 repetitions, 5 bases, the target 99/100 -- so a claim that
    only appears once the reader moves one of those cannot be pinned. Those
    are named in a comment beside the preset that makes them.
    """
    return {p["id"]: dict(p.get("expect") or {}) for p in presets}


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "random: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries. Spelled once so no mode can quietly drop
# it: three kinds of number appear on each of these pages and confusing them
# is the only mistake this course is really about.
_THREE_NUMBERS = (
    "  /* Three kinds of number appear on this page and they are never the same\n"
    "     thing. An EXACT quantity is computed over every execution the algorithm\n"
    "     has, as a fraction of two integers. A MEASUREMENT is the mean, rate or\n"
    "     count over the seeds the slider names, and it moves when the slider\n"
    "     moves. A BOUND is the inequality the course proves, printed beside the\n"
    "     exact quantity it bounds so its slack is visible. Every label below\n"
    "     says which of the three it is, and no panel here prints a measurement\n"
    "     without the exact quantity it is estimating. */\n"
)


# ---------------------------------------------------------------------------
# shuffle -- every tape, and the divisibility argument behind the frequencies
# ---------------------------------------------------------------------------

_SH_PRESETS = [
    {
        "id": "naive4",
        "label": "the naive swap at n = 4 — 256 tapes, 24 permutations",
        "n": "4", "kind": "naive",
        "expect": {
            "shTapes": "256",
            "shDiv": "256 / 24 — remainder 16",
            "shUniform": "no",
        },
    },
    {
        "id": "fy4",
        "label": "Fisher–Yates at n = 4 — 24 tapes, 24 permutations",
        "n": "4", "kind": "fisheryates",
        "expect": {
            "shTapes": "24",
            "shUniform": "yes",
            "shTV": "0, exactly",
        },
    },
    {
        "id": "naive3",
        "label": "the naive swap at n = 3 — 27 tapes, 6 permutations",
        "n": "3", "kind": "naive",
        "expect": {
            "shDiv": "27 / 6 — remainder 3",
            "shTop": "021 at 5/27",
            "shBot": "210 at 4/27",
        },
    },
    {
        "id": "naive5",
        "label": "the naive swap at n = 5 — 3125 tapes",
        "n": "5", "kind": "naive",
        # "the spread widens with n" is a claim about two presets at once, and a tile
        # holds one preset's figure. What is pinned is the pair: shTV here against
        # shTV on naive4, 3157/37500 = 0.0842 against 25/384 = 0.0651.
        "expect": {
            "shTapes": "3125",
            "shTV": "3157/37500 = 0.0842",
        },
    },
]


def _shuffle(cfg):
    chosen = _chosen(_SH_PRESETS, cfg)
    markup = (
        _toolbar(
            "Two shuffles, every tape enumerated",
            "the exact probability of each permutation, against the frequency over the seeds shown",
            [("cyan", "exact, over every tape"), ("amber", "measured, over the seeds shown"),
             ("green", "the uniform level 1/n!")],
        )
        + _stage(_svg("shPlot", "0 0 520 220",
                      "One bar pair per permutation: its exact probability and the share of the "
                      "seeded runs that produced it, against the uniform level."))
        + _table("shPerms")
        + _table("shProof")
        + _banner("shStatus")
    )
    controls = (
        _select("shPreset", "Worked example", _options(_SH_PRESETS), chosen["id"])
        + _range("shN", "How many items, n", 3, 5, chosen["n"])
        + _select("shKind", "Which shuffle",
                  [("naive", "the naive swap: j anywhere in 0 to n−1"),
                   ("fisheryates", "Fisher–Yates: j in 0 to i, going down")], chosen["kind"])
        + _range("shSeeds", "Seeds to measure over", 24, 240, 120, 24)
        + _kpis([("Tapes, exactly", "shTapes"),
                 ("Permutations reached", "shReach"),
                 ("Uniform over every tape", "shUniform"),
                 ("Most likely permutation", "shTop"),
                 ("Least likely permutation", "shBot"),
                 ("Total variation from uniform", "shTV"),
                 ("n to the n, against n factorial", "shDiv"),
                 ("Measured: distinct permutations", "shSeen")])
        + _hint(
            "shHint",
            "A <em>tape</em> is one sequence of random draws &mdash; one complete run. "
            "Fisher&ndash;Yates draws <span class=\"tt\">j</span> in <span class=\"tt\">0..i</span> "
            "going down, so it has <span class=\"tt\">n!</span> tapes; the naive swap draws "
            "<span class=\"tt\">j</span> in <span class=\"tt\">0..n&minus;1</span> every time, so "
            "it has <span class=\"tt\">n^n</span>. The table below enumerates all of them, which "
            "is why the probabilities are fractions and not estimates.",
        )
    )
    script = _BASE_JS + _REFUSAL_JS + _THREE_NUMBERS + _presets_js(
        "SHP", _SH_PRESETS, ["n", "kind"]) + r"""
  var presetIn = document.getElementById('shPreset');
  var nIn = document.getElementById('shN'), nOut = document.getElementById('shNOut');
  var kindIn = document.getElementById('shKind');
  var seedsIn = document.getElementById('shSeeds'), seedsOut = document.getElementById('shSeedsOut');
  var plot = document.getElementById('shPlot');
  var permT = document.getElementById('shPerms'), proofT = document.getElementById('shProof');
  var status = document.getElementById('shStatus');
  var KPIS = ['shTapes', 'shReach', 'shUniform', 'shTop', 'shBot', 'shTV', 'shDiv', 'shSeen'];
  var MAXROWS = 24;

  function blank(why) {
    plot.innerHTML = ''; permT.innerHTML = ''; proofT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function factorial(n) { var f = 1, i; for (i = 2; i <= n; i += 1) f *= i; return f; }

  function redraw() {
    var n = parseInt(nIn.value, 10), kind = kindIn.value;
    var seeds = parseInt(seedsIn.value, 10);
    nOut.textContent = String(n);
    seedsOut.textContent = String(seeds);
    var exact;
    try { exact = rkShuffleExact(n, kind); }
    catch (e) { if (!rkIsRefusal(e)) throw e; blank(e.message); return; }
    var total = factorial(n);
    var measured = rkShuffleSeeds(n, seeds);
    var tv = rkTotalVariation(exact.rows, total);
    var div = rkNaiveDivides(n);

    /* one row per permutation the exact enumeration knows about, in
       permutation order so two readers see the same picture */
    var rows = exact.rows.slice().sort(function (a, b) { return a.perm < b.perm ? -1 : 1; });
    var bars = rows.map(function (r) {
      var hits = measured.freq[r.perm] || 0;
      return { label: r.perm, values: [Rnum(r.probability), hits / seeds] };
    });
    var uniform = 1 / total;
    plot.innerHTML = rkBarsSvg(bars,
      [{ label: 'exact, every tape', colour: 'var(--cyan)' },
       { label: 'measured, ' + seeds + ' seeds', colour: 'var(--amber)', faint: true }],
      { rules: [{ value: uniform, label: '1/' + total, colour: 'var(--green)' }] });

    var byCount = rows.slice().sort(function (a, b) { return b.count - a.count || (a.perm < b.perm ? -1 : 1); });
    var top = byCount[0], bot = byCount[byCount.length - 1];
    document.getElementById('shTapes').textContent = String(exact.tapes);
    document.getElementById('shReach').textContent = exact.distinct + ' of ' + total;
    document.getElementById('shUniform').textContent = exact.uniform ? 'yes' : 'no';
    document.getElementById('shTop').textContent = top.perm + ' at ' + Rtext(top.probability);
    document.getElementById('shBot').textContent = bot.perm + ' at ' + Rtext(bot.probability);
    document.getElementById('shTV').textContent = Rzero(tv) ? '0, exactly' : rkBoth(tv, 4);
    document.getElementById('shDiv').textContent = div.tapes + ' / ' + div.factorial + ' — '
      + (div.divides ? 'divides' : 'remainder ' + div.remainder);
    document.getElementById('shSeen').textContent = measured.distinct + ' of ' + total;

    var head = '<thead><tr><th>permutation</th><th>tapes</th><th>exact probability</th>'
      + '<th>seeds landing here</th><th>measured share</th></tr></thead><tbody>';
    var body = '';
    byCount.slice(0, MAXROWS).forEach(function (r) {
      var hits = measured.freq[r.perm] || 0;
      var even = Requ(r.probability, R(1n, BigInt(total)));
      body += '<tr><td class="tt">' + r.perm + '</td><td>' + r.count + '</td>'
        + '<td class="' + (even ? 'tone-green' : 'tone-red') + '">' + Rtext(r.probability) + '</td>'
        + '<td>' + hits + '</td><td>' + Rtext(R(BigInt(hits), BigInt(seeds))) + '</td></tr>';
    });
    permT.innerHTML = head + body + '</tbody>';

    /* The proof, as arithmetic rather than as a sentence. */
    proofT.innerHTML = '<thead><tr><th>the counting argument</th><th>value</th></tr></thead><tbody>'
      + '<tr><td>tapes this shuffle has</td><td class="tt">'
      + (kind === 'naive' ? 'n^n = ' + div.tapes : 'n! = ' + div.factorial) + '</td></tr>'
      + '<tr><td>permutations to share them between</td><td class="tt">n! = ' + div.factorial + '</td></tr>'
      + '<tr><td>tapes per permutation, if it were uniform</td><td class="tt">'
      + (kind === 'naive'
          ? (div.divides ? String(div.tapes / div.factorial) : 'not a whole number')
          : '1')
      + '</td></tr>'
      + '<tr><td>remainder</td><td class="tt">' + (kind === 'naive' ? String(div.remainder) : '0')
      + '</td></tr></tbody>';

    var tail = byCount.length > MAXROWS
      ? ' The table shows the ' + MAXROWS + ' most likely of ' + byCount.length
        + '; the figure above shows them all.' : '';
    if (kind === 'naive') {
      status.innerHTML = '<strong>' + exact.tapes + ' tapes over ' + total
        + ' permutations.</strong> '
        + (div.divides
            ? 'Here n! happens to divide n^n, so the counting argument alone says nothing — and '
              + 'the enumeration still reports <span class="tone-red">'
              + (exact.uniform ? 'uniform' : 'not uniform') + '</span>. '
            : 'n! does <span class="tone-red">not</span> divide n^n: the remainder is '
              + div.remainder + '. Every tape is equally likely and each produces exactly one '
              + 'permutation, so if the shuffle were uniform each permutation would come from '
              + 'exactly n^n / n! tapes — a whole number, which this is not. That is a PROOF '
              + 'that the naive swap cannot be uniform, and it does not depend on any sample. ')
        + 'The enumeration agrees: the most likely permutation has probability '
        + Rtext(top.probability) + ' and the least likely ' + Rtext(bot.probability)
        + ', a total variation distance of ' + Rtext(tv) + ' from uniform. '
        + 'The measured column is a <em>measurement</em> over ' + seeds + ' seeds and it is '
        + 'noisy in both directions — read it against the exact column, not instead of it.' + tail;
    } else {
      status.innerHTML = '<strong>' + exact.tapes + ' tapes over ' + total
        + ' permutations, one each.</strong> Fisher–Yates draws j in 0..i going down, so a tape is '
        + 'a sequence of n! possibilities and the map from tapes to permutations is a bijection: '
        + 'every permutation has probability exactly <span class="tone-green">'
        + Rtext(top.probability) + '</span> and the total variation distance from uniform is '
        + '<span class="tone-green">0</span>. '
        + 'The measured column still wanders — ' + measured.distinct + ' of ' + total
        + ' permutations appeared in ' + seeds + ' seeds and the counts are uneven. That is what '
        + 'a sample looks like when the distribution IS uniform, and it is the reason the verdict '
        + 'is read off the enumeration and not off the sample.' + tail;
    }
  }

  function apply() {
    var p = SHP[presetIn.value];
    if (!p) return;
    nIn.value = p.n; kindIn.value = p.kind;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  nIn.addEventListener('input', redraw);
  kindIn.addEventListener('change', redraw);
  seedsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two shuffles, every tape enumerated",
        subtitle="Fisher–Yates gives each permutation exactly one tape; the naive swap has n^n of them and n! does not divide it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set n, choose the shuffle, and read the exact column against the measured one"),
        panel_intro=cfg.get(
            "panel_intro",
            "The exact column enumerates <em>every</em> tape, so the probabilities are fractions "
            "rather than estimates. The measured column runs the shuffle over the seeds the slider "
            "names. They disagree, and the disagreement is the point: a sample cannot establish "
            "uniformity, and the counting argument below can refute it.",
        ),
        script=script,
        expect={"shPreset": _expect(_SH_PRESETS)},
    )


# ---------------------------------------------------------------------------
# costs -- one input, a fixed rule that always pays the worst case, and a
# random rule whose cost is a distribution
# ---------------------------------------------------------------------------

_CS_PRESETS = [
    {
        "id": "sorted8",
        "label": "already sorted, n = 8 — the input the fixed rule is worst on",
        "n": "8", "order": "sorted",
        "expect": {
            "csFixed": "28 comparisons, every time",
            "csExact": "2369/140 = 16.921",
            "csClosed": "2369/140 — agrees",
        },
    },
    {
        "id": "reversed8",
        "label": "reversed, n = 8 — a different input, the same worst case",
        "n": "8", "order": "reversed",
        "expect": {
            "csFixed": "28 comparisons, every time",
            "csExact": "2369/140 = 16.921",
        },
    },
    {
        "id": "alternating8",
        "label": "high and low alternating, n = 8",
        "n": "8", "order": "alternating",
        "expect": {
            "csFixed": "16 comparisons, every time",
            "csExact": "2369/140 = 16.921",
        },
    },
    {
        "id": "small5",
        "label": "n = 5 — small enough to read every execution off the table",
        "n": "5", "order": "sorted",
        # The support -- five possible counts, 6 to 10 -- is the distribution table and
        # the plot, and no tile holds it. csRange is the MEASURED range over the seeds,
        # a different quantity that happens to coincide at this n, so pinning it here
        # would look like the support and check the seed slider instead.
        "expect": {
            "csFixed": "10 comparisons, every time",
            "csWorst": "10 = n(n − 1)/2",
            "csExact": "37/5 = 7.400",
        },
    },
    {
        "id": "sorted10",
        "label": "already sorted, n = 10",
        "n": "10", "order": "sorted",
        "expect": {
            "csFixed": "45 comparisons, every time",
            "csWorst": "45 = n(n − 1)/2",
            "csExact": "30791/1260 = 24.437",
        },
    },
]

_CS_ORDERS = [
    ("sorted", "already sorted, 1 up to n"),
    ("reversed", "reversed, n down to 1"),
    ("alternating", "alternating: 1, n, 2, n−1, …"),
]


def _costs(cfg):
    chosen = _chosen(_CS_PRESETS, cfg)
    markup = (
        _toolbar(
            "Randomised quicksort: one input, a distribution of costs",
            "the fixed rule pays the same price every time; the random rule has a distribution, and the mean over seeds is not it",
            [("cyan", "exact, over every execution"), ("amber", "measured, over the seeds shown"),
             ("green", "the expectation"), ("red", "the worst case, which is always")],
        )
        + _stage(_svg("csPlot", "0 0 520 220",
                      "One bar pair per comparison count: its exact probability over every "
                      "execution and the share of the seeded runs that produced it."))
        + _table("csBounds")
        + _table("csAgree")
        + _banner("csStatus")
    )
    controls = (
        _select("csPreset", "Worked example", _options(_CS_PRESETS), chosen["id"])
        + _range("csN", "How many items, n", 2, 10, chosen["n"])
        + _select("csOrder", "The input", _CS_ORDERS, chosen["order"])
        + _range("csSeeds", "Seeds to measure over", 24, 240, 120, 24)
        + _range("csAt", "Tail: at least this many comparisons", 1, 45, 24)
        + _range("csDev", "Deviation: at least this far from the mean", 1, 45, 6)
        + _kpis([("Fixed pivot on this input", "csFixed"),
                 ("Worst case, always", "csWorst"),
                 ("Exact expectation, every execution", "csExact"),
                 ("Closed form 2(n+1)H − 4n", "csClosed"),
                 ("Measured mean over the seeds", "csMean"),
                 ("Measured range over the seeds", "csRange"),
                 ("Exact tail at the threshold", "csTail"),
                 ("Every run sorted its input", "csOk")])
        + _hint(
            "csHint",
            "The fixed rule takes the last element as the pivot; the random rule takes a uniformly "
            "random position. A partition of a block of length <span class=\"tt\">L</span> costs "
            "<span class=\"tt\">L&minus;1</span> comparisons either way. The exact column is the "
            "distribution over <em>every</em> execution, computed by recursion on the block sizes; "
            "the measured column runs the algorithm on the seeds the slider names. Read the three "
            "numbers in the first row against each other: one input, one price, and neither of "
            "them is the expectation.",
        )
    )
    script = _COSTS_JS + _REFUSAL_JS + _THREE_NUMBERS + _presets_js(
        "CSP", _CS_PRESETS, ["n", "order"]) + r"""
  var presetIn = document.getElementById('csPreset');
  var nIn = document.getElementById('csN'), nOut = document.getElementById('csNOut');
  var orderIn = document.getElementById('csOrder');
  var seedsIn = document.getElementById('csSeeds'), seedsOut = document.getElementById('csSeedsOut');
  var atIn = document.getElementById('csAt'), atOut = document.getElementById('csAtOut');
  var devIn = document.getElementById('csDev'), devOut = document.getElementById('csDevOut');
  var plot = document.getElementById('csPlot');
  var boundsT = document.getElementById('csBounds'), agreeT = document.getElementById('csAgree');
  var status = document.getElementById('csStatus');
  var KPIS = ['csFixed', 'csWorst', 'csExact', 'csClosed', 'csMean', 'csRange', 'csTail', 'csOk'];
  var ORDER_CAP = 7;

  function blank(why) {
    plot.innerHTML = ''; boundsT.innerHTML = ''; agreeT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  /* The input, built from the choice rather than stored: three arrangements
     of the same n distinct keys, so the only thing that changes between them
     is the ORDER, which is the variable the mode is about. */
  function buildInput(n, kind) {
    var a = [], i;
    if (kind === 'reversed') { for (i = n; i >= 1; i -= 1) a.push(i); return a; }
    if (kind === 'alternating') {
      var lo = 1, hi = n;
      while (lo <= hi) { a.push(lo); lo += 1; if (lo <= hi) { a.push(hi); hi -= 1; } }
      return a;
    }
    for (i = 1; i <= n; i += 1) a.push(i);
    return a;
  }

  function redraw() {
    var n = parseInt(nIn.value, 10), seeds = parseInt(seedsIn.value, 10);
    nOut.textContent = String(n);
    seedsOut.textContent = String(seeds);
    var worst = (n * (n - 1)) / 2;
    atIn.max = Math.max(1, worst); devIn.max = Math.max(1, worst);
    var at = rkClamp(parseInt(atIn.value, 10), 1, Math.max(1, worst));
    var dev = rkClamp(parseInt(devIn.value, 10), 1, Math.max(1, worst));
    atOut.textContent = String(at); devOut.textContent = String(dev);

    var input = buildInput(n, orderIn.value);
    var fixed = rqsRun(input, null);
    var pmf, pairs;
    try { pmf = rqsPmf(n); }
    catch (e) { if (!rkIsRefusal(e)) throw e; blank(e.message); return; }
    pairs = rqsPairs(pmf);
    var exact = pmfExpect(pairs), closed = rqsClosed(n);
    var variance = pmfVariance(pairs), mass = rqsTotal(pairs);
    var sample = rqsSeeds(input, seeds);
    var support = { lo: pairs[0][0], hi: pairs[pairs.length - 1][0] };

    /* the bars: one group per attainable comparison count */
    var bars = pairs.map(function (p) {
      return { label: String(p[0]), values: [Rnum(p[1]), (sample.hist[p[0]] || 0) / seeds] };
    });
    var eIndex = 0;
    pairs.forEach(function (p, i) { if (Rcmp(R(BigInt(p[0]), 1n), exact) <= 0) eIndex = i; });
    var marks = [{ at: eIndex, label: 'E = ' + Rfixed(exact, 2), colour: 'var(--green)' }];
    var atIndex = pairs.findIndex(function (p) { return p[0] >= at; });
    if (atIndex >= 0) marks.push({ at: atIndex, label: 'a = ' + at, colour: 'var(--purple)' });
    plot.innerHTML = rkBarsSvg(bars,
      [{ label: 'exact, every execution', colour: 'var(--cyan)' },
       { label: 'measured, ' + seeds + ' seeds', colour: 'var(--amber)', faint: true }],
      { marks: marks });

    var tail = exactTail(pairs, at), mk = markovBound(pairs, at);
    var devExact = exactDeviation(pairs, dev), cb = chebyshevBound(pairs, dev);
    var seedTail = rqsSeedTail(sample, at);

    document.getElementById('csFixed').textContent = (fixed.counts.compares || 0)
      + ' comparisons, every time';
    document.getElementById('csWorst').textContent = worst + ' = n(n − 1)/2';
    document.getElementById('csExact').textContent = rkBoth(exact, 3);
    document.getElementById('csClosed').textContent = Requ(exact, closed)
      ? Rtext(closed) + ' — agrees' : Rtext(closed) + ' — DISAGREES';
    document.getElementById('csMean').textContent = rkBoth(sample.mean, 3);
    document.getElementById('csRange').textContent = sample.min + ' to ' + sample.max;
    document.getElementById('csTail').textContent = 'P(C ≥ ' + at + ') = ' + Rtext(tail);
    document.getElementById('csOk').textContent = sample.allSorted
      ? 'yes, all ' + seeds : 'NO — that is a defect';

    boundsT.innerHTML = '<thead><tr><th>the claim</th><th>event</th><th>exact</th>'
      + '<th>bound</th><th>measured over ' + seeds + ' seeds</th></tr></thead><tbody>'
      + '<tr><td>Markov, P(X ≥ a) ≤ E/a</td><td class="tt">C ≥ ' + at + '</td>'
      + '<td class="tone-cyan">' + Rtext(tail) + ' = ' + Rfixed(tail, 5) + '</td>'
      + '<td class="tone-purple">' + Rtext(mk.bound) + ' = ' + Rfixed(mk.bound, 5) + '</td>'
      + '<td class="tone-amber">' + Rtext(seedTail.fraction) + '</td></tr>'
      + '<tr><td>Chebyshev, P(|X − E| ≥ t) ≤ Var/t²</td><td class="tt">|C − E| ≥ ' + dev + '</td>'
      + '<td class="tone-cyan">' + Rtext(devExact) + ' = ' + Rfixed(devExact, 5) + '</td>'
      + '<td class="tone-purple">' + Rtext(cb.bound) + ' = ' + Rfixed(cb.bound, 5) + '</td>'
      + '<td class="tone-muted">—</td></tr>'
      + '<tr><td>the support, which is an ALWAYS claim</td>'
      + '<td class="tt">' + support.lo + ' ≤ C ≤ ' + support.hi + '</td>'
      + '<td class="' + (support.hi <= worst ? 'tone-green' : 'tone-red') + '">inside n(n − 1)/2 = '
      + worst + '</td><td class="tone-muted">—</td>'
      + '<td class="tone-amber">' + sample.min + ' to ' + sample.max + '</td></tr>'
      + '<tr><td>the exact variance</td><td class="tt">Var(C)</td>'
      + '<td class="tone-cyan">' + rkBoth(variance, 4) + '</td>'
      + '<td class="tone-muted">—</td><td class="tone-muted">—</td></tr>'
      + '<tr><td>the probabilities add to one</td><td class="tt">Σ p</td>'
      + '<td class="' + (Requ(mass, R(1n, 1n)) ? 'tone-green' : 'tone-red') + '">' + Rtext(mass)
      + '</td><td class="tone-muted">—</td><td class="tone-muted">—</td></tr></tbody>';

    /* The independent oracle, where it fits. */
    var orders = null;
    if (n <= ORDER_CAP) orders = rqsOverOrders(n, ORDER_CAP);
    agreeT.innerHTML = '<thead><tr><th>where the distribution came from</th><th>executions</th>'
      + '<th>expectation</th><th>agrees with the recursion</th></tr></thead><tbody>'
      + '<tr><td>recursion on the block sizes, random pivot</td><td>every one</td>'
      + '<td class="tt">' + Rtext(exact) + '</td><td class="tone-cyan">—</td></tr>'
      + '<tr><td>the closed form 2(n + 1)H<sub>n</sub> − 4n</td><td>—</td>'
      + '<td class="tt">' + Rtext(closed) + '</td><td class="'
      + (Requ(exact, closed) ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + (orders
          ? '<tr><td>the FIXED pivot over every input order</td><td>' + orders.orders
            + ' orders</td><td class="tt">' + Rtext(pmfExpect(rqsPairs(orders.pmf)))
            + '</td><td class="' + (rqsSamePmf(orders.pmf, pmf) ? 'tone-green">yes, value by value'
                : 'tone-red">NO') + '</td></tr>'
            + '<tr><td>…and every one of those runs sorted its input</td><td>' + orders.orders
            + '</td><td class="tt">—</td><td class="'
            + (orders.allSorted ? 'tone-green">yes' : 'tone-red">NO, ' + orders.unsorted + ' did not')
            + '</td></tr>'
          : '<tr><td>the FIXED pivot over every input order</td><td class="tone-muted" colspan="3">'
            + 'not computed above n = ' + ORDER_CAP + ': that is ' + (ORDER_CAP + 1)
            + '! orders and the tab would stop responding</td></tr>')
      + '<tr><td>the mean over the seeds shown</td><td>' + seeds + ' of them</td>'
      + '<td class="tt tone-amber">' + Rtext(sample.mean) + '</td>'
      + '<td class="' + (Requ(sample.mean, exact) ? 'tone-amber">by coincidence, here'
          : 'tone-amber">no, and it is not meant to') + '</td></tr></tbody>';

    var gap = Rsub(sample.mean, exact);
    status.innerHTML = '<strong>One input. ' + (fixed.counts.compares || 0)
      + ' comparisons with the fixed rule, ' + Rtext(exact) + ' in expectation with the random one, '
      + Rtext(sample.mean) + ' measured over ' + seeds + ' seeds.</strong> '
      + 'Those are three different kinds of number. The first is a COUNT on one input and it is the '
      + 'same on every run — with the last element as the pivot this arrangement costs it every '
      + 'time. The second is an EXACT EXPECTATION over every execution the random rule has, and it '
      + 'is a fraction, not a measurement. The third is a MEASUREMENT: it is '
      + (Rzero(gap) ? 'exactly the expectation here, which is luck and moves the moment the slider does'
          : (Rcmp(gap, R(0n, 1n)) > 0 ? Rtext(gap) + ' above' : Rtext(Rabs(gap)) + ' below')
            + ' the expectation')
      + ', and moving the seed slider moves it. '
      + 'The worst case is <span class="tone-red">' + worst + '</span> and it is an ALWAYS claim: '
      + 'the exact distribution puts probability ' + Rtext(exactTail(pairs, worst))
      + ' on it and zero above it. Markov and Chebyshev are BOUNDS, and the table shows how much '
      + 'slack each has on this n — Markov gives ' + Rfixed(mk.bound, 4) + ' where the truth is '
      + Rfixed(tail, 5) + '. '
      + 'Changing the arrangement changes the first number and leaves the second alone, because a '
      + 'uniformly random pivot POSITION picks a uniformly random RANK whatever order the keys '
      + 'arrived in.';
  }

  function apply() {
    var p = CSP[presetIn.value];
    if (!p) return;
    nIn.value = p.n; orderIn.value = p.order;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  nIn.addEventListener('input', redraw);
  orderIn.addEventListener('change', redraw);
  seedsIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  devIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Randomised quicksort: one input, a distribution of costs",
        subtitle="The fixed rule pays n(n − 1)/2 on this input every time; the random rule has an expectation of 2(n + 1)H − 4n and a spread around it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Change the input and watch the fixed count move while the distribution does not"),
        panel_intro=cfg.get(
            "panel_intro",
            "The exact distribution is computed by recursion on the block sizes, checked against the "
            "closed form and against running the fixed-pivot algorithm on <em>every</em> input order. "
            "The measured column is a sample. Markov and Chebyshev sit beside the exact tails they "
            "bound, so the slack in each is a number rather than a word.",
        ),
        script=script,
        expect={"csPreset": _expect(_CS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# karger -- the exact success probability, every minimum cut, and the seeds
# that missed
# ---------------------------------------------------------------------------

_KG_PRESETS = [
    {
        "id": "barbell",
        "label": "two triangles joined by two edges",
        "spec": "1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 1-4, 2-5",
        "expect": {
            "kgMin": "2 edges",
            "kgCount": "3",
            "kgAny": "19/35 = 0.5429",
        },
    },
    {
        "id": "cycle4",
        "label": "a four-cycle",
        "spec": "1-2, 2-3, 3-4, 4-1",
        # "the bound is exactly met" is about each of the six cuts having probability
        # exactly 1/6 = 2/(n(n − 1)), and the per-cut probabilities are rows of the cut
        # table, not a KPI. What the tiles can say is that there are six of them and
        # that the algorithm returns one of them every time.
        "expect": {
            "kgCount": "6",
            "kgAny": "1",
        },
    },
    {
        "id": "bridge",
        "label": "two triangles joined by one edge",
        "spec": "1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 3-4",
        "expect": {
            "kgMin": "1 edge",
            "kgCount": "1",
            "kgAny": "13/35 = 0.3714",
        },
    },
    {
        "id": "parallel",
        "label": "a parallel pair between 1 and 2, five vertices",
        "spec": "1-2, 1-2, 1-3, 2-3, 3-4, 4-5, 4-5, 3-5",
        # The multiplicity claim -- the doubled 1-2 edge is what keeps the small cut
        # alive -- is only visible after the reader deletes one of the two, which is a
        # different instance. The tiles pin the instance this preset ships.
        "expect": {
            "kgSize": "5 vertices, 8 edges",
            "kgCount": "2",
            "kgAny": "19/35 = 0.5429",
        },
    },
    {
        "id": "star",
        "label": "a hub with a heavy rim — seven vertices",
        "spec": "1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 2-3, 3-4, 4-5, 5-6, 6-7, 7-2",
        "expect": {
            "kgSize": "7 vertices, 12 edges",
            "kgCount": "6",
            "kgAny": "503/770 = 0.6532",
        },
    },
]

_KG_TARGETS = [
    ("9/10", "9 in 10"),
    ("99/100", "99 in 100"),
    ("999/1000", "999 in 1000"),
]


def _karger(cfg):
    chosen = _chosen(_KG_PRESETS, cfg)
    markup = (
        _toolbar(
            "Karger's contraction, and the probability it works",
            "the exact success probability by recursion over contraction states, never by sampling",
            [("cyan", "exact, over every contraction order"),
             ("amber", "measured, over the seeds shown"),
             ("purple", "one side of a minimum cut"), ("green", "the other side")],
        )
        + _stage(_svg("kgPlot", "0 0 460 300",
                      "The graph, with the two sides of the minimum cut coloured.")
                 + _svg("kgBars", "0 0 520 220",
                        "One bar pair per minimum cut: its exact probability and the share of "
                        "seeded runs that returned it."))
        + _table("kgCuts")
        + _table("kgAmp")
        + _banner("kgStatus")
    )
    controls = (
        _select("kgPreset", "Worked example", _options(_KG_PRESETS), chosen["id"])
        + _text("kgSpec", "Edges, as u-v, repeated for a parallel pair", chosen["spec"])
        + _range("kgSeeds", "Seeds to measure over", 24, 240, 120, 24)
        + _range("kgReps", "Repetitions of the whole algorithm", 1, 60, 10)
        + _select("kgTarget", "Success you want from the repetitions", _KG_TARGETS, "99/100")
        + _kpis([("Vertices and edges", "kgSize"),
                 ("Minimum cut, by exhaustive search", "kgMin"),
                 ("How many minimum cuts there are", "kgCount"),
                 ("Exact P(returns some minimum cut)", "kgAny"),
                 ("The bound 2/(n(n − 1))", "kgBound"),
                 ("Measured success over the seeds", "kgRate"),
                 ("Exact P after the repetitions", "kgAfter"),
                 ("Repetitions needed for the target", "kgNeed")])
        + _hint(
            "kgHint",
            "An edge is <span class=\"tt\">1-2</span>; write it twice for a parallel pair, which "
            "the algorithm treats as two chances to contract that pair. Contraction merges the "
            "endpoints of a uniformly random edge and drops the loops it creates. The exact column "
            "is a recursion over <em>contraction states</em> &mdash; not a sample and not an "
            "enumeration of edge orders, because different orders reach the same state and the "
            "algorithm&rsquo;s future depends only on the state.",
        )
    )
    script = _GRAPH_JS + _REFUSAL_JS + _THREE_NUMBERS + _presets_js(
        "KGP", _KG_PRESETS, ["spec"]) + r"""
  var presetIn = document.getElementById('kgPreset'), specIn = document.getElementById('kgSpec');
  var seedsIn = document.getElementById('kgSeeds'), seedsOut = document.getElementById('kgSeedsOut');
  var repsIn = document.getElementById('kgReps'), repsOut = document.getElementById('kgRepsOut');
  var targetIn = document.getElementById('kgTarget');
  var plot = document.getElementById('kgPlot'), bars = document.getElementById('kgBars');
  var cutsT = document.getElementById('kgCuts'), ampT = document.getElementById('kgAmp');
  var status = document.getElementById('kgStatus');
  var KPIS = ['kgSize', 'kgMin', 'kgCount', 'kgAny', 'kgBound', 'kgRate', 'kgAfter', 'kgNeed'];

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; cutsT.innerHTML = ''; ampT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>, and a parallel pair is that clause written twice.';
  }

  function redraw() {
    var parsed = rkParseGraph(specIn.value, 8);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var seeds = parseInt(seedsIn.value, 10), reps = parseInt(repsIn.value, 10);
    seedsOut.textContent = String(seeds);
    repsOut.textContent = String(reps);

    var total;
    try { total = rkKargerTotal(G); }
    catch (e) { if (!rkIsRefusal(e)) throw e; blank(e.message); return; }
    if (total.size === 0) { blank('this graph is already disconnected, so the minimum cut is empty'); return; }
    var sample = rkKargerSeeds(G, seeds, total.size);
    var byKey = {};
    sample.rows.forEach(function (r) { if (r.ok) byKey[r.key] = (byKey[r.key] || 0) + 1; });

    /* the first minimum cut, in the order the enumeration found them, is the
       one the drawing colours; the table lists them all */
    var shown = total.rows[0];
    var colours = shown.side.map(function (b) { return b ? 3 : 1; });
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 230, cy: 150, radius: 110 }),
                                colours: colours, label: 'none',
                                highlight: G.arcs.map(function (a, id) { return id; })
                                  .filter(function (id) {
                                    return shown.side[G.arcs[id].u] !== shown.side[G.arcs[id].v]; }) });
    bars.innerHTML = rkBarsSvg(total.rows.map(function (r) {
        return { label: r.key, values: [Rnum(r.probability), (byKey[r.key] || 0) / seeds] };
      }),
      [{ label: 'exact, every contraction order', colour: 'var(--cyan)' },
       { label: 'measured, ' + seeds + ' seeds', colour: 'var(--amber)', faint: true }],
      { rules: [{ value: Rnum(total.bound), label: '2/(n(n − 1))', colour: 'var(--green)' }] });

    var amp = rkAmplify(total.any, reps);
    var targetText = targetIn.value.split('/');
    var target = R(BigInt(targetText[0]), BigInt(targetText[1]));
    var need = rkTrialsFor(total.any, target);

    document.getElementById('kgSize').textContent = n + ' vertices, ' + G.arcs.length + ' edges';
    document.getElementById('kgMin').textContent = total.size + ' '
      + rkPlural(total.size, 'edge', 'edges');
    document.getElementById('kgCount').textContent = String(total.count);
    document.getElementById('kgAny').textContent = rkBoth(total.any, 4);
    document.getElementById('kgBound').textContent = Rtext(total.bound) + ' — '
      + (total.beatsBound ? 'cleared' : 'NOT cleared');
    document.getElementById('kgRate').textContent = Rtext(sample.rate) + ' = '
      + Rfixed(sample.rate, 4);
    document.getElementById('kgAfter').textContent = rkBoth(amp.success, 6);
    document.getElementById('kgNeed').textContent = need === null ? 'never' : String(need);

    var head = '<thead><tr><th>minimum cut</th><th>sides</th><th>exact probability</th>'
      + '<th>against the bound</th><th>seeds that returned it</th></tr></thead><tbody>';
    var body = '';
    total.rows.forEach(function (r) {
      var hits = byKey[r.key] || 0;
      body += '<tr><td class="tt">' + r.key + '</td><td>' + r.text + '</td>'
        + '<td class="tone-cyan">' + Rtext(r.probability) + ' = ' + Rfixed(r.probability, 4) + '</td>'
        + '<td class="' + (Rcmp(r.probability, total.bound) >= 0 ? 'tone-green">at or above'
            : 'tone-red">BELOW') + '</td>'
        + '<td class="tone-amber">' + hits + ' of ' + seeds + '</td></tr>';
    });
    body += '<tr><td colspan="2"><strong>any of them</strong></td>'
      + '<td class="tone-cyan"><strong>' + Rtext(total.any) + ' = ' + Rfixed(total.any, 4)
      + '</strong></td><td class="tone-muted">—</td>'
      + '<td class="tone-amber"><strong>' + sample.hits + ' of ' + seeds + ' = '
      + Rfixed(sample.rate, 4) + '</strong></td></tr>';
    cutsT.innerHTML = head + body + '</tbody>';

    var missed = sample.missed.slice(0, 14);
    ampT.innerHTML = '<thead><tr><th>repetitions</th><th>exact P(at least one succeeds)</th>'
      + '<th>exact P(all fail)</th></tr></thead><tbody>'
      + [1, 2, 5, reps, need === null ? reps : need].filter(function (t, i, arr) {
          return t >= 1 && arr.indexOf(t) === i;
        }).sort(function (a, b) { return a - b; }).map(function (t) {
          var a = rkAmplify(total.any, t);
          return '<tr><td>' + t + (t === reps ? ' (the slider)' : '')
            + (t === need ? ' (enough for the target)' : '') + '</td>'
            + '<td class="tone-cyan">' + Rfixed(a.success, 6) + '</td>'
            + '<td class="tone-purple">' + Rfixed(a.failure, 6) + '</td></tr>';
        }).join('')
      + '<tr><td colspan="3" class="small-copy">Seeds that did <em>not</em> return a minimum cut: '
      + (sample.missed.length
          ? '<span class="tone-red">' + missed.join(', ')
            + (sample.missed.length > missed.length ? ' and ' + (sample.missed.length - missed.length) + ' more' : '')
            + '</span> — ' + sample.missed.length + ' of ' + seeds
          : '<span class="tone-green">none of the ' + seeds + '</span>, which happens when the '
            + 'exact probability is 1 and not otherwise')
      + '.</td></tr></tbody>';

    status.innerHTML = '<strong>The minimum cut has ' + total.size + ' '
      + rkPlural(total.size, 'edge', 'edges') + ', there '
      + (total.count === 1 ? 'is one of them' : 'are ' + total.count + ' of them')
      + ', and one run returns one with probability ' + Rtext(total.any) + '.</strong> '
      + 'That number is exact: it is a recursion over contraction states, each state weighted by '
      + 'the multiplicity of the pair contracted, and it sums over every order the algorithm could '
      + 'take. The measurement over ' + seeds + ' seeds came out '
      + Rtext(sample.rate) + ', which is '
      + (Requ(sample.rate, total.any) ? 'the same here — and it will not be for the next slider position'
          : (Rcmp(sample.rate, total.any) > 0 ? 'higher' : 'lower') + ' than the truth')
      + '. '
      + 'The bound 2/(n(n − 1)) = ' + Rtext(total.bound) + ' is about ONE named cut and this graph '
      + (total.beatsBound ? 'clears it' : 'does not clear it, which would be a defect') + '. '
      + 'This is a WITH HIGH PROBABILITY guarantee and not an always one: '
      + (sample.missed.length
          ? 'seed ' + sample.missed[0] + ' returned a cut of ' + sample.rows[sample.missed[0] - 1].cutSize
            + ' edges rather than ' + total.size + ', and ' + sample.missed.length + ' of the '
            + seeds + ' seeds did the same. '
          : 'on this graph every one of the ' + seeds + ' seeds happened to succeed, because the '
            + 'exact probability is 1 — pick another example to see it fail. ')
      + 'Repetition is what turns it into a guarantee worth having: ' + reps + ' independent runs '
      + 'succeed with probability ' + Rfixed(amp.success, 6) + ', and '
      + (need === null ? 'no number of runs reaches the target, because one run never succeeds'
          : need + ' of them reach ' + targetIn.value) + '. Nothing in that sentence is estimated.';
  }

  function apply() {
    var p = KGP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  seedsIn.addEventListener('input', redraw);
  repsIn.addEventListener('input', redraw);
  targetIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Karger's contraction, and the probability it works",
        subtitle="The success probability is a recursion over contraction states, exact; the measured rate over seeds is not it, and repetition is what makes either of them useful",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the graph, then read the exact probability against the measured rate"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every minimum cut is found by exhaustive search over the bipartitions, and each one "
            "gets its exact probability. The algorithm succeeds if it returns <em>any</em> of them, "
            "which is a different number from the bound, and the bound is about one named cut. The "
            "seeds that failed are listed, because a with-high-probability guarantee that never "
            "shows a failure has not been demonstrated.",
        ),
        script=script,
        expect={"kgPreset": _expect(_KG_PRESETS)},
    )


# ---------------------------------------------------------------------------
# witness -- three quarters of the bases, and the quarter that lies
# ---------------------------------------------------------------------------

_WT_PRESETS = [
    {
        "id": "carmichael561",
        "label": "561 — a Carmichael number, traced at base 50",
        "n": "561", "base": "50",
        "expect": {
            "wtWit": "550 = 275/279 = 0.9857",
            "wtFermat": "0 of 318 — none, so Fermat is useless here",
            "wtLiars": "8, smallest is 50",
        },
    },
    {
        "id": "psp2047",
        "label": "2047 — a strong pseudoprime to base 2",
        "n": "2047", "base": "2",
        "expect": {
            "wtWit": "1804 = 451/511 = 0.8826",
            "wtThree": "yes",
            "wtLiars": "240, smallest is 2",
        },
    },
    {
        "id": "fermat341",
        "label": "341 — a Fermat pseudoprime to base 2",
        "n": "341", "base": "2",
        # "Fermat is fooled by base 2" is about ONE base; wtFermat counts witnesses over
        # all 298 coprime bases and the base-2 row is in the comparison table. What is
        # pinned instead is the strong test not being fooled: the smallest base that
        # fails to testify is 4, so base 2 testifies.
        "expect": {
            "wtWit": "290 = 145/169 = 0.8580",
            "wtLiars": "48, smallest is 4",
        },
    },
    {
        "id": "carmichael1105",
        "label": "1105 — a second Carmichael number",
        "n": "1105", "base": "47",
        "expect": {
            "wtWhat": "1105 — composite, and a Carmichael number",
            "wtFermat": "0 of 766 — none, so Fermat is useless here",
            "wtLiars": "28, smallest is 47",
        },
    },
    {
        "id": "prime97",
        "label": "97 — a prime",
        "n": "97", "base": "5",
        "expect": {
            "wtWit": "0 = 0",
            "wtThree": "not applicable: n is prime",
            "wtErr": "not applicable",
        },
    },
]

_WT_CAP = 2047


def _witness(cfg):
    chosen = _chosen(_WT_PRESETS, cfg)
    markup = (
        _toolbar(
            "Miller–Rabin: the bases that testify, and the bases that lie",
            "at least three quarters of the bases are witnesses for a composite, and the rest are what one run risks",
            [("cyan", "exact, over every base"), ("purple", "the proved bound"),
             ("red", "a base that does not testify")],
        )
        + _stage(_svg("wtPlot", "0 0 520 220",
                      "The exact probability that t independently chosen bases all fail to "
                      "testify, against the bound one quarter to the t."))
        + _table("wtChain")
        + _table("wtCompare")
        + _banner("wtStatus")
    )
    controls = (
        _select("wtPreset", "Worked example", _options(_WT_PRESETS), chosen["id"])
        + _range("wtN", "The number under test, n", 5, _WT_CAP, chosen["n"], 2)
        + _range("wtBase", "The base a to trace", 2, _WT_CAP - 2, chosen["base"])
        + _range("wtReps", "How many independent bases", 1, 12, 5)
        + _kpis([("n, and what it is", "wtWhat"),
                 ("Bases tested, 2 to n − 2", "wtBases"),
                 ("Witnesses, exactly", "wtWit"),
                 ("At least three quarters", "wtThree"),
                 ("Bases that do not testify", "wtLiars"),
                 ("Fermat, on the coprime bases", "wtFermat"),
                 ("Exact error after the bases chosen", "wtErr"),
                 ("The bound, one quarter to the t", "wtBound")])
        + _hint(
            "wtHint",
            "Write <span class=\"tt\">n − 1 = d · 2^s</span> with <span class=\"tt\">d</span> odd. "
            "The chain is <span class=\"tt\">a^d</span> then repeated squaring. If it never "
            "reaches <span class=\"tt\">1</span> or <span class=\"tt\">n−1</span> then "
            "<span class=\"tt\">a</span> is a <em>witness</em> and n is composite &mdash; proved, "
            "not suspected. A square of something other than <span class=\"tt\">1</span> or "
            "<span class=\"tt\">n−1</span> landing on <span class=\"tt\">1</span> is a nontrivial "
            "square root, and its gcd with n is a factor.",
        )
    )
    script = _BASE_JS + _REFUSAL_JS + _THREE_NUMBERS + _presets_js(
        "WTP", _WT_PRESETS, ["n", "base"]) + r"""
  var presetIn = document.getElementById('wtPreset');
  var nIn = document.getElementById('wtN'), nOut = document.getElementById('wtNOut');
  var baseIn = document.getElementById('wtBase'), baseOut = document.getElementById('wtBaseOut');
  var repsIn = document.getElementById('wtReps'), repsOut = document.getElementById('wtRepsOut');
  var plot = document.getElementById('wtPlot');
  var chainT = document.getElementById('wtChain'), cmpT = document.getElementById('wtCompare');
  var status = document.getElementById('wtStatus');
  var KPIS = ['wtWhat', 'wtBases', 'wtWit', 'wtThree', 'wtLiars', 'wtFermat', 'wtErr', 'wtBound'];
  var CAP = 2047;

  function blank(why) {
    plot.innerHTML = ''; chainT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var n = parseInt(nIn.value, 10);
    if (n % 2 === 0) n += 1;
    nOut.textContent = String(n);
    baseIn.max = Math.max(2, n - 2);
    var a = rkClamp(parseInt(baseIn.value, 10), 2, Math.max(2, n - 2));
    baseOut.textContent = String(a);
    var reps = parseInt(repsIn.value, 10);
    repsOut.textContent = String(reps);
    if (n < 5) { blank('the strong test needs an odd n of at least 5'); return; }

    var wit, liars, fermat;
    try {
      wit = witnessCount(n, CAP);
      liars = rkLiars(n, CAP);
      fermat = rkFermatCount(n, CAP);
    } catch (e) { if (!rkIsRefusal(e)) throw e; blank(e.message); return; }
    var chain = strongTest(n, a);
    if (!chain.valid) { blank('the strong test is defined for an odd n of at least 3'); return; }

    /* the consistency the panel can check for itself: the core's witness
       count and this kit's list of non-witnesses must partition the bases */
    var partition = wit.witnesses + liars.count === wit.total;
    var liarFraction = wit.total ? R(BigInt(liars.count), BigInt(wit.total)) : R(0n, 1n);
    var err = rkErrorAfter(liarFraction, reps), bound = rkQuarterAfter(reps);

    var rows = [], t;
    for (t = 1; t <= Math.max(reps, 8); t += 1) {
      rows.push({ label: String(t),
                  values: [Rnum(rkErrorAfter(liarFraction, t)), Rnum(rkQuarterAfter(t))] });
    }
    plot.innerHTML = rkBarsSvg(rows,
      [{ label: 'exact, this n', colour: 'var(--cyan)' },
       { label: 'the bound (1/4) to the t', colour: 'var(--purple)', faint: true }],
      { maxY: 1 });

    document.getElementById('wtWhat').textContent = n + ' — '
      + (wit.prime ? 'prime: no base is a witness'
          : (fermat.carmichael ? 'composite, and a Carmichael number' : 'composite'));
    document.getElementById('wtBases').textContent = String(wit.total);
    document.getElementById('wtWit').textContent = wit.witnesses + ' = ' + Rtext(wit.fraction)
      + (Rzero(wit.fraction) ? '' : ' = ' + Rfixed(wit.fraction, 4));
    document.getElementById('wtThree').textContent = wit.prime
      ? 'not applicable: n is prime'
      : (Rcmp(wit.fraction, R(3n, 4n)) >= 0 ? 'yes' : 'NO — that would refute the theorem');
    document.getElementById('wtLiars').textContent = liars.count
      + (liars.smallest === null ? '' : ', smallest is ' + liars.smallest)
      + (partition ? '' : ' — THE COUNTS DO NOT PARTITION, which is a defect');
    document.getElementById('wtFermat').textContent = fermat.coprimeWitnesses + ' of '
      + fermat.coprime + (fermat.carmichael ? ' — none, so Fermat is useless here' : '');
    document.getElementById('wtErr').textContent = wit.prime ? 'not applicable' : rkBoth(err, 8);
    document.getElementById('wtBound').textContent = rkBoth(bound, 8);

    var head = '<thead><tr><th>step</th><th>value modulo n</th><th>what it means</th></tr></thead><tbody>';
    var body = '<tr><td>n − 1</td><td class="tt">' + chain.d + ' × 2^' + chain.s
      + '</td><td>d is odd, which is what makes the chain well defined</td></tr>';
    chain.chain.forEach(function (v, i) {
      var name = i === 0 ? 'a^d' : 'squared ' + i + (i === 1 ? ' time' : ' times');
      var meaning = v === 1n ? 'reached 1'
        : (v === BigInt(n) - 1n ? 'reached n − 1, so a does not testify' : 'neither 1 nor n − 1');
      body += '<tr><td>' + name + '</td><td class="tt">' + v + '</td><td class="'
        + (v === 1n || v === BigInt(n) - 1n ? 'tone-green' : 'tone-muted') + '">' + meaning
        + '</td></tr>';
    });
    if (chain.nontrivialRoot !== null) {
      body += '<tr><td>nontrivial root of 1</td><td class="tt">' + chain.nontrivialRoot
        + '</td><td class="tone-red">it squares to 1 without being 1 or n − 1, so n is composite '
        + 'and gcd(' + chain.nontrivialRoot + ' − 1, n) is a factor</td></tr>';
    }
    body += '<tr><td>verdict for a = ' + a + '</td><td class="'
      + (chain.witness ? 'tone-red">witness' : 'tone-amber">no testimony')
      + '</td><td>' + chain.reason + '</td></tr>';
    chainT.innerHTML = head + body + '</tbody>';

    cmpT.innerHTML = '<thead><tr><th>test</th><th>bases it catches n on</th><th>as a fraction</th>'
      + '<th>what one random base risks</th></tr></thead><tbody>'
      + '<tr><td>the strong test, every base 2 to n − 2</td><td>' + wit.witnesses + ' of '
      + wit.total + '</td><td class="tone-cyan">' + Rtext(wit.fraction) + '</td>'
      + '<td class="tone-red">' + Rtext(liarFraction) + ' = ' + Rfixed(liarFraction, 5) + '</td></tr>'
      + '<tr><td>the Fermat test, every base 2 to n − 2</td><td>' + fermat.witnesses + ' of '
      + fermat.total + '</td><td class="tone-cyan">' + Rtext(fermat.fraction) + '</td>'
      + '<td class="tone-red">' + Rtext(Rsub(R(1n, 1n), fermat.fraction)) + '</td></tr>'
      + '<tr><td>the Fermat test, <em>coprime</em> bases only</td><td>' + fermat.coprimeWitnesses
      + ' of ' + fermat.coprime + '</td><td class="'
      + (fermat.carmichael ? 'tone-red">0' : 'tone-cyan">' + Rtext(fermat.coprimeFraction)) + '</td>'
      + '<td class="tone-muted">' + (fermat.carmichael
          ? 'everything: this is what a Carmichael number is' : '—') + '</td></tr>'
      + '<tr><td>the proved bound for the strong test</td><td class="tone-muted">—</td>'
      + '<td class="tone-purple">at least 3/4</td><td class="tone-purple">at most 1/4</td></tr>'
      + '<tr><td>after ' + reps + ' independent bases</td><td class="tone-muted">—</td>'
      + '<td class="tone-muted">—</td><td class="tone-cyan">' + Rfixed(err, 8)
      + ', against the bound ' + Rfixed(bound, 8) + '</td></tr></tbody>';

    if (wit.prime) {
      status.innerHTML = '<strong>' + n + ' is prime, and the test has no witness for it at all: '
        + wit.witnesses + ' of ' + wit.total + ' bases.</strong> '
        + 'That direction of the test is never wrong — a witness is a PROOF of compositeness, so a '
        + 'prime cannot have one, and the chain for every base reaches 1 or n − 1. The uncertainty '
        + 'is entirely in the other direction, which is what the composite examples are for. '
        + 'Base ' + a + ' here: ' + chain.reason + '.';
    } else {
      status.innerHTML = '<strong>' + wit.witnesses + ' of the ' + wit.total
        + ' bases are witnesses — ' + Rtext(wit.fraction) + ', or ' + Rpct(wit.fraction, 2)
        + ' — and ' + liars.count + ' of them '
        + rkPlural(liars.count, 'is not', 'are not') + '.</strong> '
        + 'The theorem says at least three quarters, and this n '
        + (Rcmp(wit.fraction, R(3n, 4n)) >= 0 ? 'clears it' : 'does not, which would be a defect')
        + ' — with a lot of slack, which is the usual case and is why the bound is a bound. '
        + 'The other quarter is not a rounding error: base '
        + (liars.smallest === null ? a : liars.smallest) + ' '
        + (liars.smallest === null ? 'is a witness'
            : 'runs the whole chain and produces no testimony — ' + strongTest(n, liars.smallest).reason
              + ' — so a single run with that base reports nothing, and a reader who stopped '
              + 'there would call ' + n + ' prime')
        + '. That is what WITH HIGH PROBABILITY means, spelled out on one number. '
        + (fermat.carmichael
            ? 'The Fermat test is worse than loose here: it is useless. Not one of the '
              + fermat.coprime + ' coprime bases catches ' + n + ', because ' + n
              + ' is a Carmichael number, and the strong test still catches it with '
              + Rtext(wit.fraction) + ' of the bases. '
            : 'The Fermat test catches ' + n + ' on ' + Rtext(fermat.fraction)
              + ' of the bases against the strong test&rsquo;s ' + Rtext(wit.fraction) + '. ')
        + 'Choosing ' + reps + ' bases independently leaves an exact error of ' + rkBoth(err, 8)
        + ' on this n, against the bound ' + rkBoth(bound, 8)
        + '. The bound is what holds for every composite; the exact number is what holds for this '
        + 'one, and only the first is a guarantee.';
    }
  }

  function apply() {
    var p = WTP[presetIn.value];
    if (!p) return;
    nIn.value = p.n; baseIn.value = p.base;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  nIn.addEventListener('input', redraw);
  baseIn.addEventListener('input', redraw);
  repsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Miller–Rabin: the bases that testify, and the bases that lie",
        subtitle="At least three quarters of the bases are witnesses for a composite — here is the exact fraction, and the smallest base that is not one",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Trace one base, then read the fraction over all of them"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every base from 2 to n − 2 is tested, so the witness fraction is exact rather than "
            "sampled. The Fermat test runs beside it on the same bases, split by whether the base "
            "shares a factor with n &mdash; which is the split that decides whether a Carmichael "
            "number defeats it.",
        ),
        script=script,
        expect={"wtPreset": _expect(_WT_PRESETS)},
    )


# ---------------------------------------------------------------------------
# max3sat -- the expectation is 7m/8 exactly, and no single assignment is it
# ---------------------------------------------------------------------------

_MS_PRESETS = [
    {
        "id": "four",
        "label": "four clauses on three variables, each with three distinct variables",
        "cnf": "1 2 -3; -1 2 3; 1 -2 3; -1 -2 -3",
        "expect": {
            "msMean": "7/2 = 3.5000",
            "msSeven": "7/2 — agrees",
            "msBest": "4 of 4 — satisfiable",
        },
    },
    {
        "id": "unsat",
        "label": "all eight clauses on three variables",
        "cnf": "1 2 3; 1 2 -3; 1 -2 3; 1 -2 -3; -1 2 3; -1 2 -3; -1 -2 3; -1 -2 -3",
        "expect": {
            "msMean": "7",
            "msSeven": "7 — agrees",
            "msBest": "7 of 8 — not satisfiable",
        },
    },
    {
        "id": "repeat",
        "label": "a clause that repeats a variable",
        "cnf": "1 2 -3; -1 2 3; 1 1 2; -2 -3 -1",
        "expect": {
            "msMean": "27/8 = 3.3750",
            "msSeven": "7/2 — DOES NOT agree",
            "msRatio": "27/32 = 0.8438 (7/8 = 0.8750)",
        },
    },
    {
        "id": "wide",
        "label": "eight clauses on five variables",
        "cnf": "1 2 -3; -1 3 4; 2 -4 5; -2 -3 -5; 1 -4 5; -1 2 -5; 3 4 -1; -3 -4 2",
        "expect": {
            "msCount": "32",
            "msMean": "7",
            "msBest": "8 of 8 — satisfiable",
        },
    },
    {
        "id": "trivial",
        "label": "one clause — the smallest case the argument applies to",
        "cnf": "1 2 3",
        # msSize prints "3 variables, 1 clauses" here -- the tile does not singularise --
        # so it is left unpinned rather than have an expectation ratify the wording.
        "expect": {
            "msCount": "8",
            "msMean": "7/8 = 0.8750",
            "msSeven": "7/8 — agrees",
        },
    },
]


def _max3sat(cfg):
    chosen = _chosen(_MS_PRESETS, cfg)
    markup = (
        _toolbar(
            "A random assignment satisfies 7m/8 clauses, exactly",
            "the mean over every assignment, the best one there is, and the assignments that do worse",
            [("cyan", "exact, over every assignment"),
             ("amber", "measured, over the seeds shown"),
             ("green", "the mean 7m/8"), ("red", "the optimum")],
        )
        + _stage(_svg("msPlot", "0 0 520 220",
                      "One bar pair per number of clauses satisfied: the share of all assignments "
                      "that reach it and the share of the seeded coin flips that did."))
        + _table("msClauses")
        + _table("msDist")
        + _banner("msStatus")
    )
    controls = (
        _select("msPreset", "Worked example", _options(_MS_PRESETS), chosen["id"])
        + _text("msCnf", "Clauses, literals separated by spaces and clauses by a semicolon",
                chosen["cnf"])
        + _range("msSeeds", "Seeds to measure over", 24, 240, 120, 24)
        + _kpis([("Variables and clauses", "msSize"),
                 ("Assignments enumerated", "msCount"),
                 ("Exact mean over all of them", "msMean"),
                 ("7m/8, and whether it agrees", "msSeven"),
                 ("The best assignment there is", "msBest"),
                 ("Mean divided by the optimum", "msRatio"),
                 ("Assignments below the mean", "msBelow"),
                 ("Measured mean over the seeds", "msSample")])
        + _hint(
            "msHint",
            "A literal is a signed variable: <span class=\"tt\">3</span> is "
            "<span class=\"tt\">x3</span> and <span class=\"tt\">-3</span> is its negation. A "
            "clause with three <em>distinct</em> variables is satisfied by 7 of the 8 assignments "
            "to them, so its chance is exactly <span class=\"tt\">7/8</span> and expectations add "
            "whether or not the clauses are independent. Repeat a variable inside one clause and "
            "that clause has 4 local assignments rather than 8, so the sum is no longer "
            "<span class=\"tt\">7m/8</span> &mdash; the table below says which clause did it.",
        )
    )
    script = _BASE_JS + _REFUSAL_JS + _THREE_NUMBERS + _presets_js(
        "MSP", _MS_PRESETS, ["cnf"]) + r"""
  var presetIn = document.getElementById('msPreset'), cnfIn = document.getElementById('msCnf');
  var seedsIn = document.getElementById('msSeeds'), seedsOut = document.getElementById('msSeedsOut');
  var plot = document.getElementById('msPlot');
  var clausesT = document.getElementById('msClauses'), distT = document.getElementById('msDist');
  var status = document.getElementById('msStatus');
  var KPIS = ['msSize', 'msCount', 'msMean', 'msSeven', 'msBest', 'msRatio', 'msBelow', 'msSample'];

  function blank(why) {
    plot.innerHTML = ''; clausesT.innerHTML = ''; distT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A clause is '
      + '<span class="tt">1 2 -3</span>, and clauses are separated by a semicolon.';
  }

  function redraw() {
    var parsed = rkParseCnf(cnfIn.value, 12, 14);
    if (parsed.bad) { blank(parsed.bad); return; }
    var F = parsed.formula, m = F.clauses.length;
    var seeds = parseInt(seedsIn.value, 10);
    seedsOut.textContent = String(seeds);

    var hist;
    try { hist = rkSatHistogram(F, 12); }
    catch (e) { if (!rkIsRefusal(e)) throw e; blank(e.message); return; }
    var ex = hist.exact, widths = rkClauseWidths(F);
    var sample = rkSatSeeds(F, seeds);
    var seedHist = {};
    sample.rows.forEach(function (r) { seedHist[r.satisfied] = (seedHist[r.satisfied] || 0) + 1; });

    var bars = hist.rows.map(function (r) {
      return { label: String(r.satisfied),
               values: [Rnum(r.probability), (seedHist[r.satisfied] || 0) / seeds] };
    });
    var meanIndex = 0, bestIndex = hist.rows.length - 1;
    hist.rows.forEach(function (r, i) {
      if (Rcmp(R(BigInt(r.satisfied), 1n), ex.mean) <= 0) meanIndex = i;
      if (r.satisfied === ex.best) bestIndex = i;
    });
    plot.innerHTML = rkBarsSvg(bars,
      [{ label: 'exact, every assignment', colour: 'var(--cyan)' },
       { label: 'measured, ' + seeds + ' seeds', colour: 'var(--amber)', faint: true }],
      { marks: [{ at: meanIndex, label: '7m/8 = ' + Rtext(ex.sevenEighths), colour: 'var(--green)' },
                { at: bestIndex, label: 'best = ' + ex.best, colour: 'var(--red)' }] });

    var ratio = ex.best ? Rdiv(ex.mean, R(BigInt(ex.best), 1n)) : R(0n, 1n);
    document.getElementById('msSize').textContent = F.n + ' variables, ' + m + ' clauses';
    document.getElementById('msCount').textContent = String(ex.assignments);
    document.getElementById('msMean').textContent = rkBoth(ex.mean, 4);
    document.getElementById('msSeven').textContent = Rtext(ex.sevenEighths) + ' — '
      + (ex.matchesSevenEighths ? 'agrees' : 'DOES NOT agree');
    document.getElementById('msBest').textContent = ex.best + ' of ' + m
      + (ex.best === m ? ' — satisfiable' : ' — not satisfiable');
    document.getElementById('msRatio').textContent = Rtext(ratio) + ' = ' + Rfixed(ratio, 4)
      + ' (7/8 = ' + Rfixed(R(7n, 8n), 4) + ')';
    document.getElementById('msBelow').textContent = hist.belowCount + ' of ' + ex.assignments
      + ' = ' + Rtext(hist.belowMean);
    document.getElementById('msSample').textContent = rkBoth(sample.mean, 4)
      + ', best ' + sample.max;

    var head = '<thead><tr><th>clause</th><th>variables in it</th><th>distinct</th>'
      + '<th>local assignments satisfying it</th><th>its share of the mean</th></tr></thead><tbody>';
    var body = '';
    widths.forEach(function (w) {
      body += '<tr><td class="tt">' + w.text + '</td><td>' + w.width + '</td><td class="'
        + (w.repeats ? 'tone-red' : 'tone-green') + '">' + w.distinct
        + (w.repeats ? ' — a variable repeats' : '') + '</td>'
        + '<td>' + w.models + ' of ' + w.local + '</td>'
        + '<td class="tt">' + Rtext(w.share) + '</td></tr>';
    });
    var shareSum = R(0n, 1n);
    widths.forEach(function (w) { shareSum = Radd(shareSum, w.share); });
    body += '<tr><td colspan="4"><strong>the shares add to the mean, by linearity</strong></td>'
      + '<td class="' + (Requ(shareSum, ex.mean) ? 'tone-green' : 'tone-red') + '"><strong>'
      + Rtext(shareSum) + '</strong></td></tr>';
    clausesT.innerHTML = head + body + '</tbody>';

    distT.innerHTML = '<thead><tr><th>clauses satisfied</th><th>assignments</th>'
      + '<th>exact probability</th><th>seeds landing here</th></tr></thead><tbody>'
      + hist.rows.map(function (r) {
          return '<tr><td>' + r.satisfied + (r.satisfied === ex.best ? ' — the best' : '') + '</td>'
            + '<td>' + r.count + '</td><td class="tone-cyan">' + Rtext(r.probability) + '</td>'
            + '<td class="tone-amber">' + (seedHist[r.satisfied] || 0) + '</td></tr>';
        }).join('')
      + '<tr><td><strong>mean</strong></td><td>' + ex.assignments + '</td>'
      + '<td class="tone-cyan"><strong>' + Rtext(ex.mean) + '</strong></td>'
      + '<td class="tone-amber"><strong>' + Rtext(sample.mean) + '</strong></td></tr></tbody>';

    var offenders = widths.filter(function (w) { return w.repeats || w.distinct !== 3; });
    status.innerHTML = '<strong>' + ex.assignments + ' assignments, mean ' + Rtext(ex.mean)
      + ', 7m/8 = ' + Rtext(ex.sevenEighths) + ', best ' + ex.best + ' of ' + m + '.</strong> '
      + (ex.matchesSevenEighths
          ? 'The two agree exactly, and the clause table shows why: each clause has three distinct '
            + 'variables, so 7 of its 8 local assignments satisfy it, and expectations add whether '
            + 'or not the clauses share variables. Linearity does not need independence, which is '
            + 'the step most readers assume they need and do not have. '
          : '<span class="tone-red">They do not agree</span>, and the clause table names the '
            + 'culprit: ' + (offenders.length ? offenders.map(function (w) { return w.text; }).join(', ')
                : 'a clause that is not on three distinct variables')
            + ' has ' + (offenders.length ? offenders[0].distinct : '?') + ' distinct '
            + 'variables rather than three, so its share is ' + (offenders.length ? Rtext(offenders[0].share) : '?')
            + ' and not 7/8. The formula 7m/8 assumed something the formula on screen does not do. ')
      + 'The mean is an EXPECTATION over all ' + ex.assignments + ' assignments and no single '
      + 'assignment has to equal it: ' + hist.belowCount + ' of them do worse, with probability '
      + Rtext(hist.belowMean) + '. '
      + 'The measurement over ' + seeds + ' seeded coin flips came out ' + Rtext(sample.mean)
      + ' and ranged from ' + sample.min + ' to ' + sample.max + '. '
      + 'And the ratio the algorithm earns is ' + Rtext(ratio) + ' — the mean divided by the '
      + 'OPTIMUM ' + ex.best + ', found by enumerating every assignment, not by the mean divided '
      + 'by m. Those differ whenever the formula is unsatisfiable, and a ratio printed without the '
      + 'optimum it is a ratio to is not a ratio.';
  }

  function apply() {
    var p = MSP[presetIn.value];
    if (!p) return;
    cnfIn.value = p.cnf;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  cnfIn.addEventListener('input', redraw);
  seedsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A random assignment satisfies 7m/8 clauses, exactly",
        subtitle="The mean over every assignment is a fraction, the best assignment is found by enumeration, and the ratio between them is what the algorithm earns",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the formula and watch the equality with 7m/8 break"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every assignment is enumerated, so the mean is exact and the optimum is the true one. "
            "The clause table computes each clause's own share of the mean from its own variables, "
            "and those shares add to the mean by linearity &mdash; which holds whether or not the "
            "clauses share variables, and is the step the 7m/8 argument actually needs.",
        ),
        script=script,
        expect={"msPreset": _expect(_MS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice.
# ---------------------------------------------------------------------------

_MODES = {
    "shuffle": _shuffle,
    "costs": _costs,
    "karger": _karger,
    "witness": _witness,
    "max3sat": _max3sat,
}

MODES = tuple(sorted(_MODES))


def random_lab(cfg):
    """The randomised-algorithms kit. `cfg["mode"]` chooses the lesson."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "random_lab: unknown mode %r; the five randomised modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["random_lab", "RKIT_JS", "MODES"]
