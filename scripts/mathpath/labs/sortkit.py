"""Course 2: Sorting and Selection -- one kit, ten modes, one arithmetic.

The spine of this course is a single exact statement:

    E[comparisons] = 2(n+1)H_n - 4n      for randomised quicksort

and the reason it is the spine is not that it is tight but that it holds ON
EVERY INPUT. The randomness is the algorithm's, not the data's. So the kit is
built so a reader can watch that distinction rather than be told it: `expected`
evaluates the closed form exactly over `sysdesign_core.harmonic(n, 1)`, solves
the recurrence T(n) = (n-1) + (1/n) sum (T(i) + T(n-1-i)) independently, and --
at small n -- averages over EVERY pivot sequence on the array actually on the
screen. The three agree as fractions, on a sorted input, on a reversed one and
on the input built to destroy median-of-three, which is the lesson.

THE CLAIM THIS KIT MUST NOT OVERREACH. Every other mode measures a count on one
array. A count on one array is not a bound: it is one row of a table with n!
rows, and the sorting page is where that confusion is most tempting because the
measured column looks like evidence for the proved one. So every mode puts the
measured figure and a proved one side by side -- in the panel where there is a
cell for it and in the status line otherwise -- and says which of the two is a
claim about all inputs. The proved figure of last resort is ceil(log2 n!),
which every comparison sort obeys on every array. Four modes can do better than
a disclaimer and do:

  expected    averages over every pivot sequence, exactly, at n <= 10 -- a
              claim about all runs on this input, not a sample of them
  adversary   runs the tournament on every permutation of 1..n at n <= 8 and
              reports the worst count found, against n + ceil(log2 n) - 2
  mom         prints the count the pivot is GUARANTEED to discard beside the
              count it discarded, round by round; the gap between them is the
              slack a proof about every array gives away
  quick       builds the input that kills the chosen pivot rule, so the bad
              case is exhibited rather than asserted

WHAT IS REUSED RATHER THAN REWRITTEN. `algo_core.SORT_JS` holds the counted
algorithms; nothing here reimplements one. From outside the Algorithms core:

  ALGO_JS.mergeSort    reused as it ships. It returns a comparison total and
                       nothing else, which is exactly what a baseline is for:
                       `select` and `quick` print the measured count beside a
                       total produced by a different algorithm, written for
                       another course, that has never heard of this one.
  ALGO_JS.ilog2        the integer log used for the comparison-bound column.
  sysdesign_core       `harmonic(n, 1)` IS H_n, exact, so the expectation is a
                       fraction; `lcgStream` under SEEDED_JS's MINSTD
                       parameters is the seed stream.
  ORACLE_JS.oracleCap  the one place an exhaustive refusal is spelled. Two
                       modes here enumerate and both refuse above a cap
                       through it rather than inventing a second message.

ALGO_JS.insertionSort is NOT reused: it returns a total and no sorted output,
so it cannot show a reader what insertion sort did to a record list. SORT_JS
carries its own, tagged. ALGO_JS.makeArray's 'shuffle' is NOT reused either:
it is one fixed permutation taking no seed, and `expected` needs a stream of
different ones.

WHAT THIS KIT ADDS, and why each piece could not be taken from the core:

  killerInput        the input that kills a pivot rule, produced by McIlroy's
                     adversary -- the algorithm's own comparisons are answered
                     so as to keep the worst case alive, which is the same
                     argument the adversary lesson makes about lower bounds.
                     Nothing is recalled from a paper: the array is built by
                     running the rule, and the lab then MEASURES the real run
                     on it.
  quickRecurrence    the recurrence solved exactly, as an independent check on
                     the closed form.
  quickExhaustive    the average over every pivot sequence on a given array.
  countingPlacement  counting sort with tags, so the placement direction can
                     be reversed and the stability lost in front of the
                     reader. `countingSortRun` returns keys and no tags, so it
                     cannot show this; it is still used for the counts, the
                     prefix sums and the n + k column.
  msdFlatRun         one pass per digit from the MOST significant, no
                     recursion -- the misconception of the radix lesson, run.
  minMaxPairs        min and max together in ceil(3n/2) - 2, and scanSecond,
                     the 2n - 3 the lesson's misconception assumes.
  tournamentEvery    the tournament on every permutation, to a cap.
  momFractions       1/g and 1 - (g+1)/(4g) as exact rationals, because
                     whether they sum to under one is the entire linearity
                     argument and 0.8999999999999999 is not an argument.
  bucketExpectedWork the inner work bucket sort expects IF the keys are
                     uniform, exactly -- the figure the measured column
                     leaves behind the moment the distribution stops being.
  momGuarantee       the per-round discard as a COUNT. momRun ships a
                     `guarantee` field, and it is floor(3n/10) whatever the
                     group size is -- right for five, wrong for three and
                     seven -- and it carries no slack, so it reports a
                     violation on rounds too small for the counting argument
                     to be in force. The form here is
                     ceil((g+1)/2)(ceil(ceil(n/g)/2) - 2), which is CLRS's
                     3n/10 - 6 at g = 5 and holds on every round mathcheck
                     sweeps.
  sortingLowerBound  ceil(log2 n!) as an integer over a BigInt factorial: the
                     one bound in this kit that holds for every comparison
                     sort and every input, printed beside the measurement in
                     every mode that makes comparisons at all.

The modes, and the lesson each belongs to:

  stability   L1   the tags after a sort, the violations, the two-key passes
  partition   L2   the three regions and the invariant, step by step
  quick       L3   comparisons and depth by pivot rule, on the killer input
  expected    L4   the exact expectation three ways, against a measured mean
  counting    L6   counts, prefix sums, and the placement direction
  radix       L7   the digit passes, and the two ways to break them
  bucket      L8   per-bucket work under three distributions
  select      L9   quickselect against sort-then-index
  mom         L10  the group size, the guarantee, and the level sums
  adversary   L11  the reader against the adversary, and the tournament
"""

import json

from .algebra_core import RATIONAL_JS
from .algo_core import (
    COUNT_JS,
    ORACLE_JS,
    RFIXED_JS,
    SEEDED_JS,
    SERIES_JS,
    SORT_JS,
)
from .algorithms import ALGO_JS
from .common import Lab
from .sysdesign_core import HARMONIC_JS, STREAM_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no DOM, so every one of
# them is callable from scripts/mathcheck.js exactly as it ships.
# ---------------------------------------------------------------------------

SORTKIT_JS = r"""
  /* ------------------------------------------------ the reference drawings

     n log2 n and n^2/2 are DRAWINGS. They are sampled at double precision and
     no verdict is read off either: the verdicts below compare integers. */
  function nLogN(n) { return n <= 1 ? 0 : n * Math.log2(n); }
  function nSquaredHalf(n) { return (n * (n - 1)) / 2; }
  /* The comparison lower bound as an integer: ceil(log2 n!) comparisons are
     necessary for any comparison sort, and this counts it by summing ilog2
     rather than by calling a factorial that overflows past 170. */
  function sortingLowerBound(n) {
    var fact = 1n, k, bits = 0;
    for (k = 2; k <= n; k += 1) fact *= BigInt(k);
    while ((1n << BigInt(bits)) < fact) bits += 1;
    return bits;
  }

  /* -------------------------------------- L3: an input that kills a rule

     McIlroy's adversary, applied to the pivot rule the reader chose. The
     items are the ORIGINAL POSITIONS 0..n-1 and their values are decided
     while the sort runs: a comparison between two items that both still have
     an undecided value freezes one of them at the next-smallest value, so the
     pivot keeps turning out to be near the smallest thing left. Every answer
     the adversary gives is consistent with the values it finally hands back,
     which is what makes the array a REAL input rather than a trick: the lab
     then runs the shipped quickRun on it and measures what happens.

     The mirror below has the same shape as quickRun's -- the same pivot rule,
     the same Lomuto partition, the same order of comparisons, short-circuits
     included -- because the adversary's answers depend on the order it is
     asked. That is the one place this file duplicates the core on purpose,
     and the duplication is checked: mathcheck asserts the measured count on
     the array this returns is quadratic. */
  function killerInput(n, rule) {
    var val = new Array(n).fill(null), gas = n - 1, nsolid = 0, candidate = 0, asked = 0;
    function freeze(x) { val[x] = nsolid; nsolid += 1; }
    function valueOf(x) { return val[x] === null ? gas : val[x]; }
    function le(x, y) {
      asked += 1;
      if (val[x] === null && val[y] === null) {
        if (x === candidate) freeze(x); else freeze(y);
      }
      if (val[x] === null) candidate = x;
      else if (val[y] === null) candidate = y;
      return valueOf(x) <= valueOf(y);
    }
    var arr = [], i;
    for (i = 0; i < n; i += 1) arr.push(i);
    function pivotIndex(lo, hi) {
      if (rule === 'first') return lo;
      if (rule === 'middle') return (lo + hi) >> 1;
      if (rule === 'median3') {
        var m = (lo + hi) >> 1, x = arr[lo], y = arr[m], z = arr[hi];
        if ((le(x, y) && le(y, z)) || (le(z, y) && le(y, x))) return m;
        if ((le(y, x) && le(x, z)) || (le(z, x) && le(x, y))) return lo;
        return hi;
      }
      return hi;                       /* 'last', and the fallback for 'random' */
    }
    (function sort(lo, hi) {
      if (lo >= hi) return;
      var pi = pivotIndex(lo, hi);
      if (pi !== hi) { var s = arr[pi]; arr[pi] = arr[hi]; arr[hi] = s; }
      var pivot = arr[hi], k = lo - 1;
      for (var j = lo; j < hi; j += 1) {
        if (le(arr[j], pivot)) { k += 1; if (k !== j) { var t = arr[k]; arr[k] = arr[j]; arr[j] = t; } }
      }
      var t2 = arr[k + 1]; arr[k + 1] = arr[hi]; arr[hi] = t2;
      sort(lo, k); sort(k + 2, hi);
    })(0, n - 1);
    return { array: val.map(function (v) { return (v === null ? gas : v) + 1; }), asked: asked };
  }

  /* The input orders the two quicksort modes offer. 'killer' is built against
     the rule in hand, so choosing a different rule changes the array. */
  function sortInput(kind, n, seed, rule) {
    var a = [], i;
    if (kind === 'sorted') { for (i = 1; i <= n; i += 1) a.push(i); return a; }
    if (kind === 'reversed') { for (i = n; i >= 1; i -= 1) a.push(i); return a; }
    if (kind === 'organ') {
      for (i = 1; i <= Math.ceil(n / 2); i += 1) a.push(i);
      for (i = Math.floor(n / 2); i >= 1; i -= 1) a.push(i + Math.ceil(n / 2));
      return a.slice(0, n);
    }
    if (kind === 'killer') return killerInput(n, rule === 'random' ? 'median3' : rule).array;
    if (kind === 'equal') { for (i = 0; i < n; i += 1) a.push(1); return a; }
    var order = algoPermutation(n, seed === undefined ? 1 : seed);
    return order.map(function (v) { return v + 1; });
  }

  /* ------------------------------- L4: the expectation, three ways

     One. The closed form, over an exact H_n. Two. The recurrence solved from
     the bottom, which uses no harmonic number at all and is therefore an
     independent derivation rather than a rearrangement. Three. Every pivot
     sequence on the array actually shown, averaged exactly. */
  function quickRecurrence(n) {
    var E = [R(0n, 1n), R(0n, 1n)], m, i;
    for (m = 2; m <= n; m += 1) {
      var s = R(0n, 1n);
      for (i = 0; i < m; i += 1) s = Radd(s, Radd(E[i], E[m - 1 - i]));
      E.push(Radd(R(BigInt(m - 1), 1n), Rdiv(s, R(BigInt(m), 1n))));
    }
    return E[Math.max(0, n)];
  }
  /* The average over EVERY pivot sequence, exactly. The enumeration is
     Catalan(n) executions -- 1430 at n = 8, 16796 at n = 10 -- so the cap is
     10 and the refusal is oracleCap's, not a second message. This is the
     only figure in the kit that is a claim about all runs on the array rather
     than about the runs that were sampled. */
  function quickExhaustive(a, cap) {
    oracleCap('every pivot sequence', a.length, cap === undefined ? 10 : cap);
    function rec(arr) {
      var n = arr.length;
      if (n <= 1) return { mean: R(0n, 1n), executions: 1 };
      var total = R(0n, 1n), runs = 0, p, i;
      for (p = 0; p < n; p += 1) {
        var pivot = arr[p], lo = [], hi = [];
        for (i = 0; i < n; i += 1) {
          if (i === p) continue;
          if (arr[i] <= pivot) lo.push(arr[i]); else hi.push(arr[i]);
        }
        var L = rec(lo), H = rec(hi);
        runs += L.executions * H.executions;
        total = Radd(total, Radd(R(BigInt(n - 1), 1n), Radd(L.mean, H.mean)));
      }
      return { mean: Rdiv(total, R(BigInt(n), 1n)), executions: runs };
    }
    return rec(a.slice());
  }
  /* The running mean over a prefix of the seeds, as exact rationals, so the
     plot is a sequence of fractions converging on a fraction. */
  function quickRunningMeans(a, seeds) {
    var total = 0n, out = [];
    seeds.forEach(function (s, i) {
      total += BigInt(quickRun(a, 'random', s).counts.compares || 0);
      out.push(R(total, BigInt(i + 1)));
    });
    return out;
  }
  function seedList(first, count) {
    var out = [], i;
    for (i = 0; i < count; i += 1) out.push(first + i);
    return out;
  }

  /* --------------------------- L6: the placement direction IS the stability

     countingSortRun returns sorted KEYS, which is the right answer and the
     wrong object for this lesson: with no tag on a record there is nothing to
     see when two equal keys swap. This runs the identical algorithm -- same
     tally, same prefix sums, same decrement-then-place rule -- over tagged
     records, with the loop direction as a parameter. Backwards is stable;
     forwards is the same algorithm reversing every run of equal keys, which
     is what the lesson asks the reader to watch. */
  function countingPlacement(records, k, backward) {
    var c = counter(), count = new Array(k).fill(0), i;
    records.forEach(function (r) { count[r.key] += 1; c.reads += 1; });
    var tally = count.slice();
    for (i = 1; i < k; i += 1) count[i] += count[i - 1];
    var prefix = count.slice(), out = new Array(records.length).fill(null), steps = [];
    var order = [];
    for (i = 0; i < records.length; i += 1) order.push(backward ? records.length - 1 - i : i);
    order.forEach(function (idx) {
      var key = records[idx].key;
      count[key] -= 1;
      out[count[key]] = records[idx];
      c.writes += 1;
      steps.push({ at: steps.length, from: idx, to: count[key], key: key, tag: records[idx].tag });
    });
    return runOf({ sorted: out, tally: tally, prefix: prefix,
                   violations: stabilityViolations(records, out),
                   backward: !!backward }, usedCounts(c), steps);
  }

  /* ------------------------------------------- L7: the MSD misconception

     One distribution pass per digit, most significant first, with no
     recursion into the buckets -- which is what a reader who has just seen
     LSD radix work naturally writes down, and it scrambles. Run rather than
     asserted: the verdict below is a comparison against the sorted array. */
  function msdFlatRun(keys, base) {
    var c = counter(), cur = keys.slice(), passes = [], maxKey = Math.max.apply(null, keys.concat([0]));
    var digits = 0, v = maxKey, d, i;
    while (v > 0) { digits += 1; v = Math.floor(v / base); }
    digits = Math.max(1, digits);
    for (d = digits - 1; d >= 0; d -= 1) {
      var buckets = [];
      for (i = 0; i < base; i += 1) buckets.push([]);
      cur.forEach(function (key) {
        buckets[Math.floor(key / Math.pow(base, d)) % base].push(key);
        c.moves += 1;
      });
      cur = [].concat.apply([], buckets);
      passes.push({ digit: d, buckets: buckets.map(function (b) { return b.slice(); }), after: cur.slice() });
    }
    var want = keys.slice().sort(function (x, y) { return x - y; });
    return runOf({ sorted: cur, digits: digits, passes: passes,
                   correct: cur.join(',') === want.join(',') }, usedCounts(c), passes);
  }

  /* ------------------------------------- L8: the distribution is the claim

     Bucket sort's linear expectation is a statement about the INPUT
     DISTRIBUTION, so the mode's arms are distributions and nothing else
     changes. Every key comes off the seeded stream, so a reader who moves the
     seed sees a different sample of the same distribution rather than a
     different distribution. */
  function bucketKeys(kind, n, top, seed) {
    var draws = algoStream(seed === undefined ? 1 : seed, n + 4), out = [], i;
    var narrow = Math.max(1, Math.floor(top / 20)), tiny = Math.max(1, Math.floor(top / 64));
    for (i = 0; i < n; i += 1) {
      if (kind === 'clustered') out.push(Math.floor(top / 10) + (draws[i] % narrow));
      else if (kind === 'onebucket') out.push(draws[i] % tiny);
      else out.push(draws[i] % top);
    }
    return out;
  }
  /* The expected per-bucket work when the keys ARE uniform: n keys over b
     buckets put n/b in each, and insertion sort on a bucket of size m does at
     most m(m-1)/2 comparisons, so the expectation is b * (n/b)(n/b - 1)/2.
     Exact, and the point of printing it is that the measured column leaves it
     behind the moment the distribution stops being uniform. */
  function bucketExpectedWork(n, buckets) {
    var per = R(BigInt(n), BigInt(buckets));
    var inner = Rmul(per, Rsub(per, R(1n, 1n)));
    return Rdiv(Rmul(R(BigInt(buckets), 1n), inner), R(2n, 1n));
  }

  /* ---------------------------------- L10: what the group size guarantees

     With groups of g (odd), n/g groups have medians, half of them lie on each
     side of the median of medians, and (g+1)/2 elements of each such group
     lie on that side of its own median. So at least n(g+1)/(4g) elements are
     discarded and the recurrence is T(n/g) + T(n - n(g+1)/(4g)) + cn. The two
     fractions are returned EXACTLY, because whether they sum to under one is
     the whole argument and 0.8999999999999999 is not an argument. */
  /* And the guarantee for ONE round, as an integer rather than a fraction of
     n. The fraction above is the asymptotic form and the recurrence wants it;
     a round wants the count, and the count carries slack the fraction hides:
     of the ceil(n/g) groups at least half have medians on the pivot's side,
     and each of those contributes ceil((g+1)/2) elements -- but the group
     holding the pivot and the partial last group cannot be counted on, which
     is where the -2 comes from. At g = 5 this is CLRS's 3n/10 - 6 exactly.

     This is written here rather than read off momRun's `guarantee` field
     because that field is floor(3n/10) whatever the group size is -- right for
     five, wrong for three and seven, and it has no slack, so it reports a
     violation on small rounds where the counting argument was never in force.
     mathcheck sweeps both: this bound holds on every round of every run tried,
     and the shipped field does not. */
  function momGuarantee(n, group) {
    var perGroup = Math.ceil((group + 1) / 2);
    var groups = Math.ceil(n / group);
    return Math.max(0, perGroup * (Math.ceil(groups / 2) - 2));
  }
  function momFractions(group) {
    var g = BigInt(group);
    var f1 = R(1n, g);
    var discard = R(g + 1n, 4n * g);
    var f2 = Rsub(R(1n, 1n), discard);
    return { f1: f1, f2: f2, discard: discard, sum: Radd(f1, f2),
             converges: Rcmp(Radd(f1, f2), R(1n, 1n)) < 0 };
  }

  /* ------------------------------------- L11: min and max, and the sweep

     Pair first, then push the smaller at the running minimum and the larger
     at the running maximum: 1 + 3(n-2)/2 comparisons for even n, which is
     ceil(3n/2) - 2, against the 2n - 2 of two independent scans. */
  function minMaxPairs(a) {
    var c = counter(), n = a.length, mn = null, mx = null, i = 0, trace = [];
    if (n === 0) return runOf({ min: null, max: null, bound: 0, naive: 0 }, usedCounts(c), trace);
    if (n % 2) { mn = a[0]; mx = a[0]; i = 1; }
    else {
      c.compares += 1;
      if (a[0] <= a[1]) { mn = a[0]; mx = a[1]; } else { mn = a[1]; mx = a[0]; }
      i = 2;
    }
    for (; i + 1 < n; i += 2) {
      var lo, hi;
      c.compares += 1;
      if (a[i] <= a[i + 1]) { lo = a[i]; hi = a[i + 1]; } else { lo = a[i + 1]; hi = a[i]; }
      c.compares += 1; if (lo < mn) mn = lo;
      c.compares += 1; if (hi > mx) mx = hi;
      trace.push({ at: trace.length, pair: [a[i], a[i + 1]], min: mn, max: mx });
    }
    var bound = Math.ceil((3 * n) / 2) - 2;
    return runOf({ min: mn, max: mx, bound: bound, naive: Math.max(0, 2 * n - 2) },
                 usedCounts(c), trace);
  }
  /* The second largest by two independent scans, which is the 2n - 3 the
     lesson's misconception assumes is unavoidable. */
  function scanSecond(a) {
    var c = counter(), mx = a[0], sd = null, i;
    for (i = 1; i < a.length; i += 1) {
      c.compares += 1;
      if (a[i] > mx) { sd = mx; mx = a[i]; }
      else { c.compares += 1; if (sd === null || a[i] > sd) sd = a[i]; }
    }
    return runOf({ max: mx, second: sd }, usedCounts(c), []);
  }
  /* EVERY permutation of 1..n through the tournament. This is the one figure
     on the page that is a statement about all inputs and not about the input
     on screen: it reports the worst count over n! arrangements and whether the
     right answer came back from each. n! is 40 320 at the cap of 8 and
     362 880 at 9, so the cap is 8 and oracleCap refuses above it. */
  function tournamentEvery(n, cap) {
    oracleCap('every arrangement', n, cap === undefined ? 8 : cap);
    var worst = 0, wrong = 0, over = 0, count = 0, bound = 0, worstCase = null;
    var base = [], i;
    for (i = 1; i <= n; i += 1) base.push(i);
    (function go(cur, rest) {
      if (!rest.length) {
        var t = tournament(cur);
        var used = t.counts.compares || 0;
        count += 1;
        bound = t.result.bound;
        if (t.result.max !== n || t.result.second !== n - 1) wrong += 1;
        if (used > t.result.bound) over += 1;
        if (used > worst) { worst = used; worstCase = cur.slice(); }
        return;
      }
      for (var j = 0; j < rest.length; j += 1) {
        go(cur.concat([rest[j]]), rest.slice(0, j).concat(rest.slice(j + 1)));
      }
    })([], base);
    return { arrangements: count, worst: worst, bound: bound, wrong: wrong,
             over: over, worstCase: worstCase };
  }

  /* --------------------------------------------------------- reading input

     A reader's own list. Out-of-range and non-numeric entries are dropped
     rather than clamped: a lab that silently turns 900 into 9 shows a figure
     for an array the reader did not type. */
  function parseKeys(text, lo, hi, cap) {
    var out = [];
    String(text).split(/[^0-9-]+/).forEach(function (piece) {
      if (!piece.length) return;
      var v = parseInt(piece, 10);
      if (!isFinite(v) || v < lo || v > hi) return;
      if (out.length < cap) out.push(v);
    });
    return out;
  }
  /* Ordinal suffixes, spelled once. 23rd, not 23th: the naive rule gets the
     teens and the twenties wrong and a rank is the one thing this course
     writes out in words. */
  function ordinalSuffix(k) {
    var tens = k % 100;
    if (tens >= 11 && tens <= 13) return 'th';
    var unit = k % 10;
    return unit === 1 ? 'st' : unit === 2 ? 'nd' : unit === 3 ? 'rd' : 'th';
  }
  function ordinal(k) { return k + ordinalSuffix(k); }
  function tagRecords(keys) {
    return keys.map(function (k, i) { return { key: k, tag: i + 1 }; });
  }
  /* Digit grouping, for the counts that run past a thousand. */
  function groupDigits(value) {
    var s = String(value), out = '', i, c = 0;
    for (i = s.length - 1; i >= 0; i -= 1) {
      out = s.charAt(i) + out;
      c += 1;
      if (c % 3 === 0 && i > 0 && s.charAt(i - 1) !== '-') out = ' ' + out;
    }
    return out;
  }
"""

_CORE_JS = (RATIONAL_JS + HARMONIC_JS + STREAM_JS + ALGO_JS + COUNT_JS + RFIXED_JS
            + SERIES_JS + SEEDED_JS + ORACLE_JS + SORT_JS + SORTKIT_JS)


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every kit on the path uses, so a reader
# moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _js_string(text):
    """A preset as a JS string literal the reader can then edit."""
    return json.dumps(text).replace("</", "<\\/")


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
        '<option value="%s"%s>%s</option>' % (v, " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, label, cid, value)
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n' % (label, cid)
        for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _buttons(items, wrap=""):
    return (
        '        <div class="btn-row"%s>%s</div>\n'
        % ((' id="%s"' % wrap) if wrap else "",
           "".join('<button class="btn small" id="%s" type="button">%s</button>' % (cid, text)
                   for cid, text in items))
    )


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text) for tone, text in legend
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


def _table(cid):
    return '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%s"></table></div>\n' % cid


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


# The sentence every mode carries in some form: what was measured is one row
# of a table with n! rows, and the proved figure is the whole table. Spelled
# once here so no mode can quietly drop it, and given the mode's own nouns so
# no two modes say the same words.
_OVERREACH = (
    "  /* The counts on this page came from running the algorithm on the array\n"
    "     on screen. That is one input. A bound is a statement about every\n"
    "     input, and this kit never reads one off a measurement -- where a\n"
    "     proved figure is printed it is computed from the proof, and where the\n"
    "     two diverge the status line says which is which. */\n"
)


# ---------------------------------------------------------------------------
# L1 - stability
# ---------------------------------------------------------------------------

_STABILITY_KEYS = "7, 3, 7, 1, 9, 3, 5, 1"
_STABILITY_PAIRS = "3:70, 1:40, 3:20, 2:90, 1:10, 3:50, 2:30, 1:60"


def _stability(cfg):
    keys = cfg.get("keys", _STABILITY_KEYS)
    pairs = cfg.get("pairs", _STABILITY_PAIRS)
    algo = cfg.get("algo", "insertion")

    markup = (
        _toolbar(
            "Four promises, one of them visible",
            "equal keys carry their input position, so a reordering shows",
            [("cyan", "input order kept"), ("red", "equal keys reordered"),
             ("muted", "key value")],
        )
        + _stage(_svg("stPlot", "0 0 660 190",
                      "Records before and after the sort, each carrying the position it started in."))
        + _table("stTable")
        + _banner("stStatus")
    )
    controls = (
        _text("stKeys", "Keys (equal keys are the interesting ones)", keys)
        + _select("stAlgo", "Algorithm",
                  [("insertion", "insertion sort"), ("selection", "selection sort"),
                   ("merge", "merge sort"), ("quick", "quicksort, Lomuto split")], algo)
        + _text("stPairs", "Two-key records, written major:minor", pairs)
        + _kpis([("Comparisons made", "stCmp"), ("Elements moved", "stMoves"),
                 ("Pairs out of input order", "stViol"), ("Stable on this list", "stVerdict")])
        + _hint(
            "stHint",
            "A tag is the position a record started in. After a stable sort the tags inside "
            "each run of equal keys still ascend; after an unstable one they do not. The "
            "second list is sorted on two keys by two stable passes, in both orders.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var keysIn = document.getElementById('stKeys'), algoSel = document.getElementById('stAlgo');
  var pairsIn = document.getElementById('stPairs');
  var plot = document.getElementById('stPlot'), table = document.getElementById('stTable');
  var status = document.getElementById('stStatus');

  /* Records are (key, tag); the tag is the input position and nothing else,
     which is what makes a reordering of equal keys visible at all. */
  function readRecords() {
    var keys = parseKeys(keysIn.value, 0, 99, 12);
    if (!keys.length) keys = parseKeys(""" + _js_string(_STABILITY_KEYS) + r""", 0, 99, 12);
    return tagRecords(keys);
  }
  function readPairs() {
    var out = [];
    String(pairsIn.value).split(',').forEach(function (piece) {
      var bits = piece.split(':');
      if (bits.length !== 2) return;
      var a = parseInt(bits[0], 10), b = parseInt(bits[1], 10);
      if (!isFinite(a) || !isFinite(b)) return;
      if (out.length < 10) out.push({ major: a, minor: b, tag: out.length + 1 });
    });
    return out;
  }

  function cells(list, y, mark, label) {
    var n = list.length, w = Math.min(54, Math.floor(600 / Math.max(1, n))), s = '';
    s += '<text x="8" y="' + (y - 8) + '" font-size="11" fill="var(--muted)">' + label + '</text>';
    list.forEach(function (r, i) {
      var x = 8 + i * w, bad = mark && mark[r.tag];
      s += '<rect x="' + x + '" y="' + y + '" width="' + (w - 4) + '" height="40" rx="4" fill="'
        + (bad ? 'var(--red)' : 'var(--cyan)') + '" opacity="' + (bad ? '0.85' : '0.20') + '" />';
      s += '<text x="' + (x + (w - 4) / 2) + '" y="' + (y + 18) + '" text-anchor="middle" font-size="13"'
        + ' font-weight="700" fill="' + (bad ? 'var(--on-accent)' : 'var(--text)') + '">' + r.key + '</text>';
      s += '<text x="' + (x + (w - 4) / 2) + '" y="' + (y + 33) + '" text-anchor="middle" font-size="10"'
        + ' fill="' + (bad ? 'var(--on-accent)' : 'var(--muted)') + '">#' + r.tag + '</text>';
    });
    return s;
  }

  function redraw() {
    var records = readRecords(), algo = algoSel.value;
    var run = stableRun(records, algo);
    var out = run.result.output, viol = run.result.violations;
    var mark = {};
    viol.forEach(function (pairOut) { mark[pairOut[0].tag] = true; mark[pairOut[1].tag] = true; });

    document.getElementById('stCmp').textContent = groupDigits(run.counts.compares || 0);
    document.getElementById('stMoves').textContent =
      groupDigits((run.counts.moves || 0) + (run.counts.swaps || 0));
    document.getElementById('stViol').textContent = viol.length;
    document.getElementById('stVerdict').textContent = run.result.stable ? 'no reordering seen' : 'reordered';

    plot.innerHTML = cells(records, 30, null, 'as typed, tagged by position')
      + cells(out, 110, mark, 'after the sort you chose');

    var pairs = readPairs(), rows = '';
    if (pairs.length) {
      var both = twoKeyPasses(pairs, 'major', 'minor');
      function line(list) {
        return list.map(function (r) { return r.major + ':' + r.minor; }).join('  ');
      }
      rows = '<tr><td>minor key first, then major</td><td class="tone-cyan">' + line(both.correct)
        + '</td><td>the order the lesson asks for</td></tr>'
        + '<tr><td>major key first, then minor</td><td class="tone-red">' + line(both.wrong)
        + '</td><td>the second pass reorders what the first arranged</td></tr>'
        + '<tr><td>same sequence</td><td>' + (both.same ? 'yes' : 'no') + '</td>'
        + '<td>' + (both.same
            ? 'on this list the two orders happen to agree, which is a fact about this list'
            : 'the two pass orders do not agree, so the order is not a matter of taste') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>pass order</th><th>result</th><th>what happened</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    var known = algo === 'insertion' || algo === 'merge';
    var floorBound = sortingLowerBound(records.length);
    status.innerHTML = 'On this list ' + algo + ' made <strong>' + (run.counts.compares || 0)
      + '</strong> comparisons, against the <span class="tone-amber">' + floorBound
      + '</span> that ceil(log<sub>2</sub> ' + records.length
      + '!) says no comparison sort can go under on any list of this length &mdash; the first number is a measurement and the second is a proof. It left <strong>'
      + viol.length + '</strong> pair'
      + (viol.length === 1 ? '' : 's') + ' of equal keys out of input order. '
      + (viol.length
          ? 'One such pair is a counterexample, and a counterexample settles the question: this algorithm is <span class="tone-red">not stable</span>.'
          : 'Zero reorderings <span class="tone-amber">is not a proof of stability</span> &mdash; it is one list out of '
            + records.length + '! arrangements. '
            + (known
                ? 'Stability here is proved from the algorithm: this one never moves an element past an equal one.'
                : 'Try a list where an equal pair is separated by a smaller key.'));
  }

  [keysIn, algoSel, pairsIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Stability is a promise about equal keys",
        subtitle="Tag every record with where it started, then watch which sorts keep the order",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the list and the algorithm"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every record carries the position it was typed in. The sort runs in the browser "
            "and the tags are read off the output, so a reordering is seen rather than claimed.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - partition
# ---------------------------------------------------------------------------

_PARTITION_KEYS = "38, 27, 43, 3, 9, 82, 10, 55, 16, 7, 91, 24"


def _partition(cfg):
    keys = cfg.get("keys", _PARTITION_KEYS)
    scheme = cfg.get("scheme", "lomuto")
    pivot = int(cfg.get("pivot", 12))
    step = int(cfg.get("step", 6))

    markup = (
        _toolbar(
            "One pass, three regions",
            "the invariant is checked after every comparison, not at the end",
            [("cyan", "at most the pivot"), ("amber", "above the pivot"),
             ("muted", "not yet examined"), ("purple", "the pivot")],
        )
        + _stage(_svg("ptPlot", "0 0 660 200",
                      "The array at the chosen step, with the three regions painted and the two pointers marked."))
        + _table("ptTable")
        + _banner("ptStatus")
    )
    controls = (
        _text("ptKeys", "Array", keys)
        + _select("ptScheme", "Scheme",
                  [("lomuto", "Lomuto, one pointer"), ("hoare", "Hoare, two pointers")], scheme)
        + _range("ptPivot", "Pivot position", 1, 14, pivot)
        + _range("ptStep", "Step", 0, 14, step)
        + _kpis([("Comparisons", "ptCmp"), ("Swaps", "ptSwaps"),
                 ("Pivot ends at", "ptSplit"), ("Invariant held", "ptInv")])
        + _hint(
            "ptHint",
            "Lomuto keeps a[lo..i] at most the pivot and a[i+1..j-1] above it, and everything "
            "from j on is unexamined. Step through and the three regions grow and shrink; the "
            "invariant column is evaluated on the array itself at each step, never assumed.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var keysIn = document.getElementById('ptKeys'), schemeSel = document.getElementById('ptScheme');
  var pivotS = document.getElementById('ptPivot'), stepS = document.getElementById('ptStep');
  var plot = document.getElementById('ptPlot'), table = document.getElementById('ptTable');
  var status = document.getElementById('ptStatus');

  function readArray() {
    var a = parseKeys(keysIn.value, 0, 999, 14);
    if (a.length < 2) a = parseKeys(""" + _js_string(_PARTITION_KEYS) + r""", 0, 999, 14);
    return a;
  }
  function isSorted(list) {
    for (var i = 1; i < list.length; i += 1) if (list[i - 1] > list[i]) return false;
    return true;
  }

  function redraw() {
    var a = readArray(), n = a.length, scheme = schemeSel.value;
    var pi = Math.min(n, Math.max(1, +pivotS.value)) - 1;
    var run = partitionRun(a, pi, scheme);
    var steps = run.trace, last = Math.max(0, steps.length - 1);
    var at = Math.min(last, Math.max(0, +stepS.value));

    document.getElementById('ptPivotOut').textContent = 'element ' + (pi + 1) + ' (value ' + a[pi] + ')';
    document.getElementById('ptStepOut').textContent = steps.length
      ? (at + 1) + ' of ' + steps.length : 'no step to show';
    document.getElementById('ptCmp').textContent = run.counts.compares || 0;
    document.getElementById('ptSwaps').textContent = run.counts.swaps || 0;
    document.getElementById('ptSplit').textContent = scheme === 'hoare'
      ? 'boundary after ' + (run.result.split + 1) : 'position ' + (run.result.split + 1);
    document.getElementById('ptInv').textContent = run.result.invariant ? 'at every step' : 'broken';

    var frame = steps.length ? steps[at] : { array: run.result.array, i: run.result.split, j: n - 1,
                                             pivot: run.result.pivot };
    var arr = frame.array, w = Math.min(58, Math.floor(620 / Math.max(1, n))), s = '';
    s += '<text x="8" y="22" font-size="11" fill="var(--muted)">pivot value ' + frame.pivot
      + (steps.length ? ', after comparison ' + (at + 1) : ', partition complete') + '</text>';
    arr.forEach(function (v, i) {
      var tone = 'var(--line)';
      if (scheme === 'lomuto') {
        if (i <= frame.i) tone = 'var(--cyan)';
        else if (i <= frame.j) tone = 'var(--amber)';
        else if (i === n - 1) tone = 'var(--purple)';
      } else {
        if (i <= frame.j) tone = 'var(--cyan)';
        else if (i >= frame.i) tone = 'var(--amber)';
      }
      var x = 8 + i * w;
      s += '<rect x="' + x + '" y="36" width="' + (w - 4) + '" height="44" rx="4" fill="' + tone
        + '" opacity="0.30" />';
      s += '<text x="' + (x + (w - 4) / 2) + '" y="64" text-anchor="middle" font-size="13"'
        + ' font-weight="700" fill="var(--text)">' + v + '</text>';
    });
    function marker(idx, label, colour, y) {
      if (idx < 0 || idx >= n) return '';
      var x = 8 + idx * w + (w - 4) / 2;
      return '<line x1="' + x + '" y1="82" x2="' + x + '" y2="' + (y - 12) + '" stroke="' + colour
        + '" stroke-width="1.5" /><text x="' + x + '" y="' + y + '" text-anchor="middle" font-size="11"'
        + ' font-weight="700" fill="' + colour + '">' + label + '</text>';
    }
    if (scheme === 'lomuto') {
      s += marker(frame.i, 'i, end of the at-most region', 'var(--cyan)', 108);
      s += marker(frame.j, 'j, the element being compared', 'var(--amber)', 132);
    } else {
      s += marker(frame.j, 'j walks down', 'var(--cyan)', 108);
      s += marker(frame.i, 'i walks up', 'var(--amber)', 132);
    }
    s += '<text x="8" y="164" font-size="11" fill="var(--muted)">final arrangement</text>';
    run.result.array.forEach(function (v, i) {
      var x = 8 + i * w, tone = i === run.result.split ? 'var(--purple)' : 'var(--line-strong)';
      s += '<rect x="' + x + '" y="170" width="' + (w - 4) + '" height="22" rx="3" fill="' + tone
        + '" opacity="0.28" /><text x="' + (x + (w - 4) / 2) + '" y="186" text-anchor="middle"'
        + ' font-size="11" fill="var(--text)">' + v + '</text>';
    });
    plot.innerHTML = s;

    var rows = steps.map(function (st, idx) {
      var ok = st.invariant === undefined ? '&mdash;' : (st.invariant ? 'holds' : 'BROKEN');
      return '<tr><td>' + (idx + 1) + '</td><td>' + st.i + '</td><td>' + st.j + '</td><td class="tt">'
        + st.array.join(' ') + '</td><td class="' + (st.invariant === false ? 'tone-red' : 'tone-green')
        + '">' + ok + '</td></tr>';
    }).join('');
    table.innerHTML = '<thead><tr><th>step</th><th>i</th><th>j</th><th>array</th>'
      + '<th>invariant</th></tr></thead><tbody>' + rows + '</tbody>';

    var split = run.result.split;
    var left = run.result.array.slice(0, Math.max(0, split));
    var right = run.result.array.slice(split + 1);
    var leftSorted = isSorted(left), rightSorted = isSorted(right);
    status.innerHTML = 'One pass over ' + n + ' elements cost <strong>' + (run.counts.compares || 0)
      + '</strong> comparisons and <strong>' + (run.counts.swaps || 0) + '</strong> swaps. '
      + (scheme === 'lomuto'
          ? 'Lomuto compares every element once against the pivot, so the count is exactly n &minus; 1 = '
            + (n - 1) + ' on <em>every</em> array of this length &mdash; the only figure on this panel that does not depend on the data. '
          : 'Hoare stops when the pointers cross, so its comparison count depends on the data and is not n &minus; 1; here it was '
            + (run.counts.compares || 0) + '. ')
      + 'After the pass the left side is ' + (leftSorted ? 'sorted' : '<span class="tone-red">not sorted</span>')
      + ' and the right side is ' + (rightSorted ? 'sorted' : '<span class="tone-red">not sorted</span>')
      + '. Partition places one element and separates the rest; sorting the sides is the recursion, not the pass.';
  }

  [keysIn, schemeSel, pivotS, stepS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Partition is one pass and one invariant",
        subtitle="Three regions, a pointer each, and the invariant evaluated after every comparison",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the array, the pivot and the step"),
        panel_intro=cfg.get(
            "panel_intro",
            "The partition runs in the browser and records every step. The invariant column "
            "is computed from the array at that step, so a broken invariant would show as a "
            "broken invariant rather than as a missing one.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - quick
# ---------------------------------------------------------------------------

_RULES = [
    ("first", "first element"),
    ("middle", "middle element"),
    ("median3", "median of first, middle and last"),
    ("last", "last element"),
    ("random", "a seeded random element"),
]

_ORDERS = [
    ("sorted", "already sorted"),
    ("reversed", "reversed"),
    ("organ", "up then down"),
    ("shuffle", "a seeded shuffle"),
    ("killer", "the input built to kill this rule"),
    ("equal", "every key the same"),
]


def _quick(cfg):
    n = int(cfg.get("n", 32))
    rule = cfg.get("rule", "median3")
    order = cfg.get("order", "killer")
    seed = int(cfg.get("seed", 7))

    markup = (
        _toolbar(
            "The split decides everything",
            "comparisons measured on the array, against the two curves that bracket it",
            [("cyan", "measured comparisons"), ("green", "n log2 n, drawn"),
             ("red", "n(n-1)/2, drawn"), ("purple", "recursion depth")],
        )
        + _stage(_svg("qkPlot", "0 0 520 220",
                      "Measured comparisons against the two reference curves, over a range of sizes."))
        + _table("qkTable")
        + _banner("qkStatus")
    )
    controls = (
        _range("qkN", "Array length", 6, 64, n)
        + _select("qkRule", "Pivot rule", _RULES, rule)
        + _select("qkOrder", "Input order", _ORDERS, order)
        + _range("qkSeed", "Seed", 1, 40, seed)
        + _kpis([("Comparisons measured", "qkCmp"), ("Recursion depth", "qkDepth"),
                 ("n log2 n at this n", "qkNLog"), ("Worst a partition sort can do", "qkWorst")])
        + _hint(
            "qkHint",
            "The killer input is not quoted from anywhere: it is built by answering the "
            "rule's own comparisons so as to keep its worst case alive, and the array that "
            "comes out is then sorted by the ordinary quicksort and counted.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var nS = document.getElementById('qkN'), ruleSel = document.getElementById('qkRule');
  var orderSel = document.getElementById('qkOrder'), seedS = document.getElementById('qkSeed');
  var plot = document.getElementById('qkPlot'), table = document.getElementById('qkTable');
  var status = document.getElementById('qkStatus');

  function inputFor(kind, n, rule, seed) { return sortInput(kind, n, seed, rule); }
  /* A label table rather than select.options[...].text: the harness's DOM has
     no options collection, and reaching for one is how a lab dies in it. */
  var RULE_TEXT = { first: 'a first-element pivot', middle: 'a middle-element pivot',
    median3: 'median of three', last: 'a last-element pivot', random: 'a seeded random pivot' };

  function redraw() {
    var n = +nS.value, rule = ruleSel.value, order = orderSel.value, seed = +seedS.value;
    document.getElementById('qkNOut').textContent = n + ' elements';
    document.getElementById('qkSeedOut').textContent = (order === 'shuffle' || rule === 'random')
      ? 'seed ' + seed : 'seed ' + seed + ', unused by this pair';

    var a = inputFor(order, n, rule, seed);
    var run = quickRun(a, rule, seed);
    var merge = mergeSort(a.slice());

    document.getElementById('qkCmp').textContent = groupDigits(run.counts.compares || 0);
    document.getElementById('qkDepth').textContent = run.result.depth;
    document.getElementById('qkNLog').textContent = Math.round(nLogN(n));
    document.getElementById('qkWorst').textContent = groupDigits(nSquaredHalf(n));

    /* The sweep. Every point is a real run on a real array of that size, and
       the killer is rebuilt at each size because it is a function of the rule
       and the length, not a stored table. */
    var xs = [], measured = [], curve = [], quad = [], step = Math.max(1, Math.round(n / 12));
    for (var m = Math.max(4, step); m <= n; m += step) {
      xs.push(m);
      measured.push(quickRun(inputFor(order, m, rule, seed), rule, seed).counts.compares || 0);
      curve.push(nLogN(m));
      quad.push(nSquaredHalf(m));
    }
    if (xs[xs.length - 1] !== n) {
      xs.push(n); measured.push(run.counts.compares || 0);
      curve.push(nLogN(n)); quad.push(nSquaredHalf(n));
    }
    drawSeries(plot, [
      { label: 'measured', values: measured, colour: 'var(--cyan)', points: true },
      { label: 'n log2 n', values: curve, colour: 'var(--green)', dashed: true },
      { label: 'n(n-1)/2', values: quad, colour: 'var(--red)', dashed: true }
    ], xs, { xlabel: 'n' });

    var rows = run.trace.slice(0, 10).map(function (st) {
      return '<tr><td>' + (st.at + 1) + '</td><td>' + (st.lo + 1) + '&ndash;' + (st.hi + 1)
        + '</td><td>' + st.pivot + '</td><td>' + (st.split + 1) + '</td><td>' + st.left + ' | '
        + st.right + '</td><td>' + st.depth + '</td></tr>';
    }).join('');
    table.innerHTML = '<thead><tr><th>call</th><th>range</th><th>pivot</th><th>pivot lands at</th>'
      + '<th>sizes left | right</th><th>depth</th></tr></thead><tbody>' + rows
      + '</tbody><tfoot><tr><td colspan="6">' + run.trace.length
      + ' partitions in all; merge sort on the same array made ' + merge
      + ' comparisons, counted by an algorithm this kit did not write.</td></tr></tfoot>';

    /* The verdict is a MEASUREMENT at two sizes, not a reading off the drawn
       curve: a count that roughly quadruples when n doubles is behaving
       quadratically, and one that roughly doubles is not. Neither is a proof,
       and the sentence says so. */
    var measuredC = run.counts.compares || 0;
    var half = Math.max(4, Math.round(n / 2));
    var halfC = quickRun(inputFor(order, half, rule, seed), rule, seed).counts.compares || 0;
    var growth = measuredC / Math.max(1, halfC);
    var quadratic = growth >= 3.2;
    status.innerHTML = 'On this array of ' + n + ', ' + RULE_TEXT[rule]
      + ' made <strong>' + groupDigits(measuredC) + '</strong> comparisons and recursed '
      + run.result.depth + ' deep, where a balanced split would be about ' + (ilog2(n) + 1) + '. '
      + 'Halving the length to ' + half + ' costs ' + groupDigits(halfC) + ', so doubling n multiplies the work by '
      + growth.toFixed(2) + ' &mdash; '
      + (quadratic
          ? '<span class="tone-red">close to the 4 of a quadratic cost</span>'
            + (order === 'killer' ? ', which is this rule meeting the input built against it.'
               : order === 'equal' ? ', on an array with no structure in it at all beyond its ties.'
               : ', on this family of inputs.')
          : '<span class="tone-green">closer to the 2.2 of n log n</span> on this family of inputs.')
      + ' Two sizes are two measurements and not a bound. '
      + (order === 'equal'
          ? 'And this array is where the randomised rule stops helping: Lomuto sends every key equal to the pivot to the same side, so <em>every</em> pivot rule splits ' + n
            + ' into 0 and ' + (n - 1) + ' here, the seeded one included. 2(n+1)H<sub>n</sub> &minus; 4n is an expectation for <span class="tone-amber">distinct keys</span>, and this is the array that says so &mdash; move the seed and watch the count refuse to move with it.'
          : 'The only pivot rule whose bound survives the choice of input is the randomised one, because its randomness is not in the data.')
      + (order === 'killer'
          ? ' This array was not looked up: the adversary answered ' + killerInput(n, rule === 'random' ? 'median3' : rule).asked
            + ' of this rule\u2019s own comparisons while building it, each answer chosen so the worst case stayed reachable.'
          : '');
  }

  [nS, ruleSel, orderSel, seedS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Every deterministic pivot rule has a bad input",
        subtitle="Choose a rule, then meet the array built to defeat it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the rule and the input"),
        panel_intro=cfg.get(
            "panel_intro",
            "The killer array is constructed by answering the rule's own comparisons "
            "adversarially, then handed to the ordinary quicksort, which counts what it does.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - expected
# ---------------------------------------------------------------------------

# Every pivot sequence on n elements is Catalan(n) executions: 4 862 at nine,
# 16 796 at ten, 208 012 at twelve. Ten is what a redraw can afford; the two
# extra families are drawn at nine or fewer so that dragging the slider stays
# responsive, and the panel says so rather than going quiet.
_EXHAUSTIVE_CAP = 10
_COMPARE_CAP = 9


def _expected(cfg):
    n = int(cfg.get("n", 9))
    trials = int(cfg.get("trials", 120))
    which = cfg.get("input", "killer")
    seed = int(cfg.get("seed", 1))

    markup = (
        _toolbar(
            "The expectation, and what a measurement is not",
            "an exact fraction three ways, beside a mean over seeds",
            [("green", "exact expectation"), ("cyan", "mean over the seeds so far"),
             ("purple", "every pivot sequence")],
        )
        + _stage(_svg("exPlot", "0 0 520 220",
                      "The running mean over seeds against the exact expectation drawn as a level line."))
        + _table("exTable")
        + _banner("exStatus")
    )
    controls = (
        _range("exN", "Array length", 2, 24, n)
        + _range("exTrials", "Seeds drawn", 1, 300, trials)
        + _select("exInput", "The array the randomised sort is run on",
                  [("killer", "the median-of-three killer"), ("sorted", "already sorted"),
                   ("reversed", "reversed"), ("organ", "up then down"),
                   ("shuffle", "a seeded shuffle")], which)
        + _range("exSeed", "First seed", 1, 40, seed)
        + _kpis([("2(n+1)Hn - 4n", "exExact"), ("Mean over the seeds", "exMean"),
                 ("Mean minus expectation", "exGap"), ("Hn, exactly", "exHarm")])
        + _hint(
            "exHint",
            "The expectation is a property of the algorithm, so changing the array changes "
            "the measured mean and leaves the expectation where it was. The third row proves "
            "that rather than asserting it: it averages over every pivot sequence there is.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var nS = document.getElementById('exN'), trialsS = document.getElementById('exTrials');
  var inputSel = document.getElementById('exInput'), seedS = document.getElementById('exSeed');
  var plot = document.getElementById('exPlot'), table = document.getElementById('exTable');
  var status = document.getElementById('exStatus');
  var EXHAUSTIVE_CAP = """ + str(_EXHAUSTIVE_CAP) + r""", COMPARE_CAP = """ + str(_COMPARE_CAP) + r""";
  var INPUT_TEXT = { killer: 'the median-of-three killer', sorted: 'a sorted array',
    reversed: 'a reversed array', organ: 'an up-then-down array', shuffle: 'a seeded shuffle' };

  /* The exhaustive average, or the reason there is not one. oracleCap throws
     and this catches; the panel prints the refusal, which is the honest thing
     to show and also the lesson of the cap. */
  function everySequence(a, cap) {
    try {
      var r = quickExhaustive(a, cap);
      return { mean: r.mean, executions: r.executions, refused: null };
    } catch (err) {
      return { mean: null, executions: 0, refused: err.message };
    }
  }
  function fractionCell(r) {
    return r === null ? '&mdash;' : '<span class="tt">' + Rtext(r) + '</span>';
  }

  function redraw() {
    var n = +nS.value, trials = +trialsS.value, kind = inputSel.value, seed = +seedS.value;
    document.getElementById('exNOut').textContent = n + ' elements';
    document.getElementById('exTrialsOut').textContent = trials + (trials === 1 ? ' seed' : ' seeds');
    document.getElementById('exSeedOut').textContent = 'seeds ' + seed + ' to ' + (seed + trials - 1);

    var a = sortInput(kind, n, seed, 'median3');
    var exact = quickExpected(n), fromRecurrence = quickRecurrence(n), H = harmonic(n, 1);
    var seeds = seedList(seed, trials);
    var means = quickRunningMeans(a, seeds);
    var measured = means[means.length - 1];
    var gap = Rsub(measured, exact);

    document.getElementById('exExact').textContent = Rfixed(exact, 4);
    document.getElementById('exMean').textContent = Rfixed(measured, 4);
    document.getElementById('exGap').textContent = (Rcmp(gap, R(0n, 1n)) >= 0 ? '+' : '') + Rfixed(gap, 4);
    document.getElementById('exHarm').textContent = Rtext(H);

    /* The plot is the running mean wandering toward a level line. The line is
       the exact fraction; the wander is the sampling. */
    var pts = [], xs = [], stride = Math.max(1, Math.ceil(means.length / 40));
    for (var i = stride - 1; i < means.length; i += stride) {
      xs.push(i + 1);
      pts.push(parseFloat(Rfixed(means[i], 4)));
    }
    if (!xs.length) { xs.push(1); pts.push(parseFloat(Rfixed(means[0], 4))); }
    var level = xs.map(function () { return parseFloat(Rfixed(exact, 4)); });
    drawSeries(plot, [
      { label: 'mean so far', values: pts, colour: 'var(--cyan)', points: true },
      { label: 'expectation', values: level, colour: 'var(--green)', dashed: true }
    ], xs, { xlabel: 'seeds' });

    var shown = everySequence(a, EXHAUSTIVE_CAP);
    var rows = '<tr><td>2(n+1)H<sub>n</sub> &minus; 4n</td><td>' + fractionCell(exact) + '</td><td>'
      + Rfixed(exact, 4) + '</td><td>the closed form, over an exact H<sub>n</sub></td></tr>'
      + '<tr><td>T(n) = (n&minus;1) + (1/n)&sum;(T(i)+T(n&minus;1&minus;i))</td><td>'
      + fractionCell(fromRecurrence) + '</td><td>' + Rfixed(fromRecurrence, 4)
      + '</td><td>solved from the bottom, using no harmonic number &mdash; '
      + (Requ(fromRecurrence, exact) ? 'and it lands on the same fraction'
                                     : '<span class="tone-red">and it does not agree</span>') + '</td></tr>';
    rows += '<tr><td class="tone-purple">every pivot sequence on the array shown</td><td>'
      + (shown.refused ? '&mdash;' : fractionCell(shown.mean)) + '</td><td>'
      + (shown.refused ? '&mdash;' : Rfixed(shown.mean, 4)) + '</td><td>'
      + (shown.refused ? shown.refused
                       : groupDigits(shown.executions) + ' executions, each weighted by its probability &mdash; '
                         + (Requ(shown.mean, exact)
                             ? 'a claim about every run on this array, not a sample of them'
                             : '<span class="tone-red">and it does not match the closed form</span>'))
      + '</td></tr>';
    if (n <= COMPARE_CAP) {
      ['sorted', 'reversed', 'killer'].forEach(function (other) {
        if (other === kind) return;
        var r = everySequence(sortInput(other, n, seed, 'median3'), EXHAUSTIVE_CAP);
        rows += '<tr><td>the same, on ' + INPUT_TEXT[other] + '</td><td>' + fractionCell(r.mean)
          + '</td><td>' + (r.mean ? Rfixed(r.mean, 4) : '&mdash;') + '</td><td>'
          + (r.mean && Requ(r.mean, exact)
              ? 'a different array, the same fraction'
              : '<span class="tone-red">a different fraction on a different array</span>') + '</td></tr>';
      });
    } else {
      rows += '<tr><td>the same, on the other arrays</td><td>&mdash;</td><td>&mdash;</td>'
        + '<td>drawn at ' + COMPARE_CAP + ' elements or fewer, so that moving the slider stays quick</td></tr>';
    }
    rows += '<tr><td class="tone-cyan">mean over ' + trials + ' seed' + (trials === 1 ? '' : 's')
      + '</td><td>' + fractionCell(measured) + '</td><td>' + Rfixed(measured, 4)
      + '</td><td>a sample. Move the first seed and this row moves; nothing above it does.</td></tr>';
    table.innerHTML = '<thead><tr><th>where the number comes from</th><th>exactly</th>'
      + '<th>as a decimal</th><th>what it is a claim about</th></tr></thead><tbody>' + rows + '</tbody>';

    var agree = Requ(fromRecurrence, exact);
    status.innerHTML = 'At n = ' + n + ' the expectation is exactly <span class="tt">' + Rtext(exact)
      + '</span> = ' + Rfixed(exact, 4) + ' comparisons, and the recurrence solved independently '
      + (agree ? 'gives the same fraction' : '<span class="tone-red">disagrees</span>') + '. '
      + trials + ' seeds on ' + INPUT_TEXT[kind] + ' averaged <strong>' + Rfixed(measured, 4)
      + '</strong>, which is ' + Rfixed(gap, 4) + ' away. '
      + (shown.refused
          ? 'The gap is sampling and nothing else: the expectation is over the pivot, so it does not know which array it was handed.'
          : 'The row above the mean settles why: averaged over <em>every</em> pivot sequence this array costs <span class="tt">'
            + Rtext(shown.mean) + '</span> &mdash; the fraction the rows above give for the other arrays too. '
            + 'The measured mean differs from it because ' + trials + ' seeds are a sample of those '
            + groupDigits(shown.executions) + ' runs, not all of them.');
  }

  [nS, trialsS, inputSel, seedS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Expected on every input, not on the average input",
        subtitle="The exact fraction, the recurrence that produces it, and a mean that only approaches it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the size, the array and the seeds"),
        panel_intro=cfg.get(
            "panel_intro",
            "Hn is evaluated exactly, so the expectation is a fraction rather than a decimal "
            "that nearly agrees with one. The measured mean is a fraction too, and the two "
            "can therefore be subtracted.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - counting
# ---------------------------------------------------------------------------

_COUNTING_KEYS = "4, 1, 3, 4, 3, 0, 2, 4, 1, 3, 4, 2"

# The declared key range, as the lesson quotes it. Only the small ones are
# actually allocated and run; the large ones are arithmetic, because a count
# array of 2^32 slots is the misconception made concrete and not a thing to
# allocate in a reader's tab.
_RANGES = [
    ("0", "just wide enough for the keys"),
    ("256", "a byte, k = 256"),
    ("4096", "k = 4096"),
    ("65536", "a 16-bit key, k = 65 536"),
    ("16777216", "a 24-bit key, k = 16 777 216"),
    ("4294967296", "a 32-bit key, k = 4 294 967 296"),
]
_RUNNABLE_K = 4096


def _counting(cfg):
    keys = cfg.get("keys", _COUNTING_KEYS)
    declared = str(cfg.get("range", "0"))
    direction = cfg.get("direction", "backward")

    markup = (
        _toolbar(
            "Counting sort compares nothing",
            "a tally, a prefix sum, and a placement pass whose direction is the stability",
            [("cyan", "tally"), ("purple", "prefix sum"), ("red", "equal keys reordered"),
             ("muted", "output slot")],
        )
        + _stage(_svg("ctPlot", "0 0 660 210",
                      "The tally and the running prefix sums, then the output slots the records land in."))
        + _table("ctTable")
        + _banner("ctStatus")
    )
    controls = (
        _text("ctKeys", "Keys", keys)
        + _select("ctRange", "Declared key range k", _RANGES, declared)
        + _select("ctDir", "Placement pass",
                  [("backward", "from the back, as the algorithm says"),
                   ("forward", "from the front, same bookkeeping")], direction)
        + _kpis([("Work n + k", "ctWork"), ("Any comparison sort needs at least", "ctBound"),
                 ("Writes into the output", "ctWrites"), ("Equal keys reordered", "ctViol")])
        + _hint(
            "ctHint",
            "Nothing here is compared, so the comparison lower bound does not apply and there "
            "is no contradiction to explain. What does apply is n + k: the second term is the "
            "declared range, and a range wide enough to be interesting is wider than n log n.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var keysIn = document.getElementById('ctKeys'), rangeSel = document.getElementById('ctRange');
  var dirSel = document.getElementById('ctDir');
  var plot = document.getElementById('ctPlot'), table = document.getElementById('ctTable');
  var status = document.getElementById('ctStatus');
  var RUNNABLE = """ + str(_RUNNABLE_K) + r""";

  function readKeys() {
    var a = parseKeys(keysIn.value, 0, 99, 16);
    if (!a.length) a = parseKeys(""" + _js_string(_COUNTING_KEYS) + r""", 0, 99, 16);
    return a;
  }

  function redraw() {
    var keys = readKeys(), n = keys.length;
    var fit = Math.max.apply(null, keys) + 1;
    var declared = parseInt(rangeSel.value, 10) || 0;
    var kDeclared = Math.max(fit, declared);
    var kRun = Math.min(Math.max(fit, Math.min(kDeclared, RUNNABLE)), RUNNABLE);
    var backward = dirSel.value === 'backward';

    /* The shipped routine for the counts, the prefix sums and the n + k
       column; the tagged one beside it for the placement, because a sorted
       list of keys cannot show a reader that two equal keys changed places. */
    var plain = countingSortRun(keys, kRun);
    var run = countingPlacement(tagRecords(keys), kRun, backward);
    var viol = run.result.violations;

    var work = BigInt(n) + BigInt(kDeclared);
    document.getElementById('ctWork').textContent = groupDigits(work.toString());
    document.getElementById('ctBound').textContent = groupDigits(sortingLowerBound(n)) + ' comparisons';
    document.getElementById('ctWrites').textContent = run.counts.writes || 0;
    document.getElementById('ctViol').textContent = viol.length;

    /* The tally and the prefix sums, drawn over the key values that exist. */
    var shownKeys = Math.min(kRun, 16), cw = Math.floor(620 / Math.max(1, shownKeys));
    var maxTally = Math.max.apply(null, run.result.tally.slice(0, shownKeys).concat([1]));
    var s = '<text x="8" y="16" font-size="11" fill="var(--muted)">how many of each key, then the running total</text>';
    for (var v = 0; v < shownKeys; v += 1) {
      var x = 8 + v * cw, h = Math.round((run.result.tally[v] / maxTally) * 46);
      s += '<rect x="' + x + '" y="' + (72 - h) + '" width="' + (cw - 6) + '" height="' + Math.max(1, h)
        + '" rx="3" fill="var(--cyan)" opacity="0.55" />';
      s += '<text x="' + (x + (cw - 6) / 2) + '" y="86" text-anchor="middle" font-size="11"'
        + ' fill="var(--text)">' + v + '</text>';
      s += '<text x="' + (x + (cw - 6) / 2) + '" y="' + (66 - h) + '" text-anchor="middle" font-size="10"'
        + ' fill="var(--muted)">' + run.result.tally[v] + '</text>';
      s += '<text x="' + (x + (cw - 6) / 2) + '" y="102" text-anchor="middle" font-size="11"'
        + ' font-weight="700" fill="var(--purple)">' + run.result.prefix[v] + '</text>';
    }
    s += '<text x="8" y="130" font-size="11" fill="var(--muted)">output, each slot showing the key and the position it came from</text>';
    var ow = Math.min(52, Math.floor(620 / Math.max(1, n))), mark = {};
    viol.forEach(function (pairOut) { mark[pairOut[0].tag] = true; mark[pairOut[1].tag] = true; });
    run.result.sorted.forEach(function (r, i) {
      var x = 8 + i * ow, bad = mark[r.tag];
      s += '<rect x="' + x + '" y="140" width="' + (ow - 4) + '" height="40" rx="4" fill="'
        + (bad ? 'var(--red)' : 'var(--line-strong)') + '" opacity="' + (bad ? '0.85' : '0.24') + '" />'
        + '<text x="' + (x + (ow - 4) / 2) + '" y="158" text-anchor="middle" font-size="13"'
        + ' font-weight="700" fill="' + (bad ? 'var(--on-accent)' : 'var(--text)') + '">' + r.key + '</text>'
        + '<text x="' + (x + (ow - 4) / 2) + '" y="173" text-anchor="middle" font-size="10" fill="'
        + (bad ? 'var(--on-accent)' : 'var(--muted)') + '">#' + r.tag + '</text>';
    });
    s += '<text x="8" y="200" font-size="11" fill="var(--muted)">placement ran '
      + (backward ? 'from the back' : 'from the front') + ', ' + (run.counts.writes || 0) + ' writes</text>';
    plot.innerHTML = s;

    var rows = '';
    for (var key = 0; key < shownKeys; key += 1) {
      rows += '<tr><td>' + key + '</td><td>' + run.result.tally[key] + '</td><td>'
        + run.result.prefix[key] + '</td><td>' + (run.result.prefix[key] - run.result.tally[key])
        + '&ndash;' + (run.result.prefix[key] - 1) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>key</th><th>count</th><th>prefix sum</th>'
      + '<th>output slots it owns</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4">Sorted output: <span class="tt">'
      + plain.result.sorted.join(' ') + '</span> &mdash; produced by the shipped routine, which returns keys and no tags, '
      + 'and matching the tagged run above.</td></tr></tfoot>';

    var comparisonWork = n * Math.max(1, ilog2(n));
    var worthIt = work <= BigInt(comparisonWork);
    status.innerHTML = 'Counting ' + n + ' keys over a declared range of ' + groupDigits(kDeclared)
      + ' costs n + k = <strong>' + groupDigits(work.toString()) + '</strong> steps, against n log<sub>2</sub> n &asymp; '
      + groupDigits(comparisonWork) + ' for a comparison sort. '
      + (worthIt
          ? 'Here the range is small enough that <span class="tone-green">counting wins</span>.'
          : '<span class="tone-red">The range has swallowed the linearity</span>: &Theta;(n + k) is linear in n + k, and k is the part that grew.')
      + ' '
      + (kDeclared > RUNNABLE
          ? 'A tally array that wide is not allocated here; the pass above ran at k = ' + kRun + ', which is what a reader can see. '
          : '')
      + (viol.length
          ? 'Placing from the front reversed <strong>' + viol.length + '</strong> pair'
            + (viol.length === 1 ? '' : 's') + ' of equal keys: the bookkeeping is identical and the direction alone is what stability rests on.'
          : (backward
              ? 'Placing from the back kept every run of equal keys in input order, which is the property radix sort will need.'
              : 'Placing from the front reordered nothing on this list &mdash; which is a fact about this list, not about the algorithm. Add a second record with a repeated key.'));
  }

  [keysIn, rangeSel, dirSel].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Linear in n plus k, and k is not always small",
        subtitle="A tally, a prefix sum and a placement direction that is the whole stability argument",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the keys, the declared range and the pass"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tally and the prefix sums are computed from the keys you type. The declared "
            "range only changes the second term of n + k, which is the term that decides "
            "whether this algorithm is worth using.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - radix
# ---------------------------------------------------------------------------

_RADIX_KEYS = "329, 457, 657, 839, 436, 720, 355"


def _radix(cfg):
    keys = cfg.get("keys", _RADIX_KEYS)
    base = str(cfg.get("base", 10))
    variant = cfg.get("variant", "lsd")
    pass_at = int(cfg.get("pass", 1))

    markup = (
        _toolbar(
            "Every pass is a counting sort, and every pass must be stable",
            "the digit passes, and the two ways of getting them wrong",
            [("cyan", "this pass's buckets"), ("purple", "the digit being read"),
             ("red", "out of order"), ("green", "sorted")],
        )
        + _stage(_svg("rxPlot", "0 0 660 220",
                      "The buckets of the chosen pass and the array that comes out of it."))
        + _table("rxTable")
        + _banner("rxStatus")
    )
    controls = (
        _text("rxKeys", "Keys", keys)
        + _select("rxBase", "Base",
                  [("2", "base 2"), ("4", "base 4"), ("8", "base 8"),
                   ("10", "base 10"), ("16", "base 16")], base)
        + _select("rxVariant", "How the passes are run",
                  [("lsd", "least significant digit first, each pass stable"),
                   ("unstable", "least significant first, but each pass unstable"),
                   ("msd", "most significant digit first, no recursion")], variant)
        + _range("rxPass", "Pass", 1, 10, pass_at)
        + _kpis([("Digit passes", "rxPasses"), ("Work per pass, n + b", "rxPerPass"),
                 ("Elements moved", "rxMoves"), ("Sorted at the end", "rxOk")])
        + _hint(
            "rxHint",
            "The correctness argument for radix sort is not about digits, it is about "
            "stability: a pass on digit d must leave keys agreeing in digit d in the order "
            "the previous pass left them. Break that and the passes stop composing.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var keysIn = document.getElementById('rxKeys'), baseSel = document.getElementById('rxBase');
  var variantSel = document.getElementById('rxVariant'), passS = document.getElementById('rxPass');
  var plot = document.getElementById('rxPlot'), table = document.getElementById('rxTable');
  var status = document.getElementById('rxStatus');

  function readKeys() {
    var a = parseKeys(keysIn.value, 0, 4095, 12);
    if (a.length < 2) a = parseKeys(""" + _js_string(_RADIX_KEYS) + r""", 0, 4095, 12);
    return a;
  }

  function redraw() {
    var keys = readKeys(), base = parseInt(baseSel.value, 10), variant = variantSel.value;
    var run = variant === 'msd' ? msdFlatRun(keys, base) : radixRun(keys, base, variant === 'lsd');
    var passes = run.result.passes, at = Math.min(passes.length - 1, Math.max(0, +passS.value - 1));
    var frame = passes[at];

    document.getElementById('rxPassOut').textContent = 'pass ' + (at + 1) + ' of ' + passes.length
      + ', reading digit ' + frame.digit;
    document.getElementById('rxPasses').textContent = run.result.digits;
    document.getElementById('rxPerPass').textContent = keys.length + ' + ' + base + ' = ' + (keys.length + base);
    document.getElementById('rxMoves').textContent = run.counts.moves || 0;
    document.getElementById('rxOk').textContent = run.result.correct ? 'yes' : 'no';

    var bw = Math.floor(640 / Math.max(1, base)), s = '';
    s += '<text x="8" y="16" font-size="11" fill="var(--muted)">pass ' + (at + 1)
      + ' reads digit ' + frame.digit + ' (the ' + Math.pow(base, frame.digit) + 's)</text>';
    frame.buckets.forEach(function (bucket, d) {
      var x = 8 + d * bw;
      s += '<rect x="' + x + '" y="26" width="' + (bw - 5) + '" height="'
        + Math.max(18, 18 + bucket.length * 17) + '" rx="4" fill="var(--cyan)" opacity="0.14" />';
      s += '<text x="' + (x + (bw - 5) / 2) + '" y="40" text-anchor="middle" font-size="11"'
        + ' font-weight="700" fill="var(--purple)">' + d.toString(base) + '</text>';
      bucket.forEach(function (key, i) {
        s += '<text x="' + (x + (bw - 5) / 2) + '" y="' + (57 + i * 17) + '" text-anchor="middle"'
          + ' font-size="11" fill="var(--text)">' + key + '</text>';
      });
    });
    var sorted = keys.slice().sort(function (p, q) { return p - q; });
    s += '<text x="8" y="176" font-size="11" fill="var(--muted)">the array after this pass</text>';
    var cw = Math.min(64, Math.floor(640 / Math.max(1, keys.length)));
    frame.after.forEach(function (key, i) {
      var good = frame.after[i] === sorted[i];
      var x = 8 + i * cw;
      s += '<rect x="' + x + '" y="184" width="' + (cw - 5) + '" height="26" rx="3" fill="'
        + (good ? 'var(--green)' : 'var(--red)') + '" opacity="0.24" />'
        + '<text x="' + (x + (cw - 5) / 2) + '" y="202" text-anchor="middle" font-size="12"'
        + ' fill="var(--text)">' + key + '</text>';
    });
    plot.innerHTML = s;

    var rows = passes.map(function (p, i) {
      var done = p.after.join(',') === sorted.join(',');
      return '<tr><td>' + (i + 1) + '</td><td>digit ' + p.digit + '</td><td class="tt">'
        + p.after.join(' ') + '</td><td class="' + (done ? 'tone-green' : 'tone-muted') + '">'
        + (done ? 'sorted' : 'not yet') + '</td></tr>';
    }).join('');
    table.innerHTML = '<thead><tr><th>pass</th><th>reads</th><th>array afterwards</th>'
      + '<th>against the sorted array</th></tr></thead><tbody>' + rows + '</tbody>';

    var total = run.result.digits * (keys.length + base);
    status.innerHTML = run.result.digits + ' passes of n + b = ' + (keys.length + base)
      + ' is <strong>' + groupDigits(total) + '</strong> units of work, and not one comparison between two keys was made &mdash; '
      + 'so the ' + sortingLowerBound(keys.length) + ' comparisons that ceil(log<sub>2</sub> '
      + keys.length + '!) forces on every comparison sort are a bound this algorithm is simply outside, rather than one it beats. '
      + (variant === 'lsd'
          ? (run.result.correct
              ? 'Every pass was stable and the array <span class="tone-green">came out sorted</span>. The stability is doing the work: each pass only has to fix its own digit because the previous passes have already been left alone.'
              : '<span class="tone-red">It did not sort</span>, which on this input means something other than stability is wrong.')
          : variant === 'unstable'
            ? 'Each pass reverses its buckets, so a pass undoes what the passes before it settled. The result is <span class="tone-red">'
              + (run.result.correct ? 'still sorted on this input, which is luck rather than correctness' : 'not sorted') + '</span> &mdash; and a single such input is all a counterexample needs to be.'
            : 'Most significant first, with no recursion into the buckets, the LAST pass is the one on the least significant digit, and it overrides everything the passes before it arranged &mdash; so the array ends sorted on its final digit and nothing else: <span class="tone-red">'
              + (run.result.correct ? 'sorted here by accident' : 'not sorted') + '</span>. MSD is not wrong; MSD without recursing inside each bucket is.')
      + ' Correctness here is checked against the sorted array, not asserted.';
  }

  [keysIn, baseSel, variantSel, passS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Radix sorts by making every pass stable",
        subtitle="One counting sort per digit, and two ways to break the composition",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the keys, the base and the pass order"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each pass is run and its buckets are shown. The verdict under the array compares "
            "what came out against the sorted array, so a broken variant is seen failing.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - bucket
# ---------------------------------------------------------------------------


def _bucket(cfg):
    dist = cfg.get("dist", "uniform")
    n = int(cfg.get("n", 48))
    buckets = int(cfg.get("buckets", 12))
    seed = int(cfg.get("seed", 7))

    markup = (
        _toolbar(
            "An average-case bound is a claim about the input",
            "per-bucket insertion sort work, under a distribution you choose",
            [("cyan", "bucket occupancy"), ("amber", "comparisons inside a bucket"),
             ("green", "the work if the keys were uniform")],
        )
        + _stage(_svg("bkPlot", "0 0 660 210",
                      "Bucket occupancy, with the comparisons insertion sort made inside each bucket."))
        + _table("bkTable")
        + _banner("bkStatus")
    )
    controls = (
        _select("bkDist", "Key distribution",
                [("uniform", "uniform over the range"),
                 ("clustered", "clustered in a twentieth of the range"),
                 ("onebucket", "all inside the first bucket")], dist)
        + _range("bkN", "Keys", 8, 120, n)
        + _range("bkBuckets", "Buckets", 2, 32, buckets)
        + _range("bkSeed", "Seed", 1, 40, seed)
        + _kpis([("Comparisons measured", "bkCmp"), ("If the keys were uniform", "bkUniform"),
                 ("Fullest bucket", "bkMax"), ("Comparisons per key", "bkPer")])
        + _hint(
            "bkHint",
            "The linear expectation assumes the keys are uniform over the range the buckets "
            "divide. Nothing about the algorithm changes when you change the distribution; "
            "the assumption is what changes, and the work follows it.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var distSel = document.getElementById('bkDist'), nS = document.getElementById('bkN');
  var bS = document.getElementById('bkBuckets'), seedS = document.getElementById('bkSeed');
  var plot = document.getElementById('bkPlot'), table = document.getElementById('bkTable');
  var status = document.getElementById('bkStatus');
  var TOP = 1024;
  var DIST_TEXT = { uniform: 'uniform over the range', clustered: 'clustered in a twentieth of the range',
    onebucket: 'entirely inside the first bucket' };

  function redraw() {
    var dist = distSel.value, n = +nS.value, b = +bS.value, seed = +seedS.value;
    document.getElementById('bkNOut').textContent = n + ' keys';
    document.getElementById('bkBucketsOut').textContent = b + ' buckets';
    document.getElementById('bkSeedOut').textContent = 'seed ' + seed;

    var keys = bucketKeys(dist, n, TOP, seed);
    var run = bucketRun(keys, b, TOP);
    var work = run.result.work, measured = run.counts.compares || 0;
    var ifUniform = bucketExpectedWork(n, b);
    var fullest = work.reduce(function (m, w) { return Math.max(m, w.size); }, 0);

    document.getElementById('bkCmp').textContent = groupDigits(measured);
    document.getElementById('bkUniform').textContent = Rfixed(ifUniform, 2);
    document.getElementById('bkMax').textContent = fullest + ' of ' + n;
    document.getElementById('bkPer').textContent = (measured / Math.max(1, n)).toFixed(2);

    var bw = Math.floor(640 / Math.max(1, b)), tallest = Math.max(1, fullest), s = '';
    s += '<text x="8" y="16" font-size="11" fill="var(--muted)">each column is a bucket; the number under it is the comparisons insertion sort made inside</text>';
    work.forEach(function (w, i) {
      var x = 8 + i * bw, h = Math.round((w.size / tallest) * 120);
      s += '<rect x="' + x + '" y="' + (150 - h) + '" width="' + (bw - 5) + '" height="' + Math.max(1, h)
        + '" rx="3" fill="var(--cyan)" opacity="0.55" />';
      s += '<text x="' + (x + (bw - 5) / 2) + '" y="' + (144 - h) + '" text-anchor="middle"'
        + ' font-size="10" fill="var(--muted)">' + w.size + '</text>';
      s += '<text x="' + (x + (bw - 5) / 2) + '" y="166" text-anchor="middle" font-size="11"'
        + ' font-weight="700" fill="var(--amber)">' + w.compares + '</text>';
    });
    s += '<line x1="8" y1="150" x2="652" y2="150" stroke="var(--line-strong)" />';
    var level = Math.round((n / b / tallest) * 120);
    s += '<line x1="8" y1="' + (150 - level) + '" x2="652" y2="' + (150 - level)
      + '" stroke="var(--green)" stroke-dasharray="6 4" stroke-width="1.5" />';
    s += '<text x="652" y="' + (144 - level) + '" text-anchor="end" font-size="11" fill="var(--green)">n / b = '
      + (n / b).toFixed(2) + ' keys a bucket if uniform</text>';
    s += '<text x="8" y="192" font-size="11" fill="var(--muted)">' + n + ' keys, '
      + DIST_TEXT[dist] + ', measured ' + groupDigits(measured) + ' comparisons in total</text>';
    plot.innerHTML = s;

    var rows = work.map(function (w) {
      return '<tr><td>' + w.bucket + '</td><td>' + w.size + '</td><td>' + w.compares
        + '</td><td>' + (w.size * Math.max(0, w.size - 1) / 2) + '</td></tr>';
    }).join('');
    table.innerHTML = '<thead><tr><th>bucket</th><th>keys in it</th><th>comparisons made</th>'
      + '<th>most it could have cost</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4">Sorted: <span class="tt">'
      + (run.result.sorted.slice(0, 24).join(' ') + (n > 24 ? ' ...' : ''))
      + '</span></td></tr></tfoot>';

    var linearish = measured <= 2 * n;
    status.innerHTML = 'With the keys ' + DIST_TEXT[dist] + ', bucket sort made <strong>'
      + groupDigits(measured) + '</strong> comparisons on ' + n + ' keys &mdash; '
      + (measured / Math.max(1, n)).toFixed(2) + ' per key. Under the uniformity assumption the expected inner work is exactly '
      + '<span class="tt">' + Rtext(ifUniform) + '</span> = ' + Rfixed(ifUniform, 2) + '. '
      + (linearish
          ? '<span class="tone-green">The measurement is near it</span>, because the assumption happens to hold for these keys.'
          : '<span class="tone-red">The measurement has left it behind</span>: the algorithm is unchanged and the distribution is not, which is the whole content of an average-case claim.')
      + ' &Theta;(n) here was never a property of bucket sort; it was a property of the input it was promised.';
  }

  [distSel, nS, bS, seedS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bucket sort is linear when the keys agree to be uniform",
        subtitle="Change the distribution and nothing about the algorithm changes but its cost",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the distribution, the size and the buckets"),
        panel_intro=cfg.get(
            "panel_intro",
            "Keys come off the seeded stream under the distribution you pick, and every "
            "comparison is counted inside the bucket it happened in.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - select
# ---------------------------------------------------------------------------


def _select_mode(cfg):
    n = int(cfg.get("n", 24))
    k = int(cfg.get("k", 12))
    rule = cfg.get("rule", "random")
    order = cfg.get("order", "shuffle")
    seed = int(cfg.get("seed", 5))

    markup = (
        _toolbar(
            "Recurse into one side only",
            "the range that survives each partition, against sorting the whole array",
            [("cyan", "the range still in play"), ("purple", "the pivot and its rank"),
             ("muted", "discarded"), ("amber", "sort then index")],
        )
        + _stage(_svg("slPlot", "0 0 660 200",
                      "The surviving range after each partition, shrinking toward the wanted rank."))
        + _table("slTable")
        + _banner("slStatus")
    )
    controls = (
        _range("slN", "Array length", 6, 64, n)
        + _range("slK", "Which order statistic", 1, 64, k)
        + _select("slRule", "Pivot rule", _RULES, rule)
        + _select("slOrder", "Input order", _ORDERS, order)
        + _range("slSeed", "Seed", 1, 40, seed)
        + _kpis([("Comparisons to select", "slCmp"), ("Comparisons to sort first", "slSort"),
                 ("The value found", "slValue"), ("Partitions used", "slCalls")])
        + _hint(
            "slHint",
            "Quickselect throws away one side at every step, so the recurrence has one "
            "recursive term instead of two. That is the whole difference between expected "
            "linear and n log n, and the table shows the range being thrown away.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var nS = document.getElementById('slN'), kS = document.getElementById('slK');
  var ruleSel = document.getElementById('slRule'), orderSel = document.getElementById('slOrder');
  var seedS = document.getElementById('slSeed');
  var plot = document.getElementById('slPlot'), table = document.getElementById('slTable');
  var status = document.getElementById('slStatus');

  function redraw() {
    var n = +nS.value, rule = ruleSel.value, order = orderSel.value, seed = +seedS.value;
    var k = Math.min(n, Math.max(1, +kS.value));
    document.getElementById('slNOut').textContent = n + ' elements';
    document.getElementById('slKOut').textContent = 'the ' + ordinal(k)
      + ' smallest' + (k * 2 === n || k * 2 === n + 1 ? ', the median' : '');
    document.getElementById('slSeedOut').textContent = 'seed ' + seed;

    var a = sortInput(order, n, seed, rule);
    var run = quickselectRun(a, k, rule, seed);
    var sortFirst = run.result.sortThenIndex;
    var truth = a.slice().sort(function (p, q) { return p - q; })[k - 1];

    document.getElementById('slCmp').textContent = groupDigits(run.counts.compares || 0);
    document.getElementById('slSort').textContent = groupDigits(sortFirst);
    document.getElementById('slValue').textContent = run.result.value === null
      ? 'not reached' : String(run.result.value);
    document.getElementById('slCalls').textContent = run.counts.calls || 0;

    var s = '<text x="8" y="16" font-size="11" fill="var(--muted)">each bar is the range still in play after that partition</text>';
    var unit = 640 / Math.max(1, n);
    run.trace.forEach(function (st, i) {
      var y = 28 + i * 22;
      if (y > 168) return;
      s += '<rect x="8" y="' + y + '" width="640" height="16" rx="3" fill="var(--line)" opacity="0.5" />';
      s += '<rect x="' + (8 + st.lo * unit) + '" y="' + y + '" width="'
        + Math.max(2, (st.hi - st.lo + 1) * unit) + '" height="16" rx="3" fill="var(--cyan)" opacity="0.45" />';
      var px = 8 + (st.rank - 1) * unit;
      s += '<rect x="' + px + '" y="' + y + '" width="' + Math.max(2, unit)
        + '" height="16" rx="2" fill="var(--purple)" opacity="0.9" />';
      s += '<text x="654" y="' + (y + 12) + '" text-anchor="end" font-size="10" fill="var(--muted)">rank '
        + st.rank + '</text>';
    });
    var wx = 8 + (k - 1) * unit + Math.max(2, unit) / 2;
    s += '<line x1="' + wx + '" y1="24" x2="' + wx + '" y2="176" stroke="var(--amber)"'
      + ' stroke-dasharray="4 3" stroke-width="1.5" />';
    s += '<text x="8" y="192" font-size="11" fill="var(--amber)">the dashed line is rank ' + k
      + ', the one being looked for</text>';
    plot.innerHTML = s;

    var rows = run.trace.map(function (st, i) {
      return '<tr><td>' + (i + 1) + '</td><td>' + (st.lo + 1) + '&ndash;' + (st.hi + 1)
        + '</td><td>' + (st.hi - st.lo + 1) + '</td><td>' + st.pivot + '</td><td>' + st.rank
        + '</td><td>' + (st.rank === st.want ? 'found it'
            : st.want < st.rank ? 'keep the left side' : 'keep the right side') + '</td></tr>';
    }).join('');
    table.innerHTML = '<thead><tr><th>partition</th><th>range</th><th>size</th><th>pivot</th>'
      + '<th>pivot rank</th><th>what happens next</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="6">Sorting the whole array with merge sort &mdash; the shipped routine, '
      + 'written for another course and reused unchanged &mdash; costs ' + groupDigits(sortFirst)
      + ' comparisons and then one array index. Selection found the same value, '
      + (run.result.value === truth ? 'checked against the sorted array' : 'AND DISAGREES WITH THE SORTED ARRAY')
      + '.</td></tr></tfoot>';

    var measured = run.counts.compares || 0;
    status.innerHTML = 'Finding the ' + ordinal(k) + ' smallest of ' + n + ' cost <strong>'
      + groupDigits(measured) + '</strong> comparisons; sorting first and indexing costs '
      + groupDigits(sortFirst) + '. '
      + (measured < sortFirst
          ? 'Selection won here by ' + groupDigits(sortFirst - measured) + ' comparisons.'
          : '<span class="tone-red">Selection lost here</span>, which a deterministic pivot rule on the wrong input will do.')
      + ' The expected-linear claim is about the <em>random</em> pivot and it is an expectation: a good pivot, one in the middle half, '
      + 'has probability one half and leaves at most 3n/4, so the expected total is under 4n = ' + (4 * n)
      + '. This run is one draw, and one draw is not the expectation &mdash; change the seed and watch the count move while 4n does not.';
  }

  [nS, kS, ruleSel, orderSel, seedS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Finding one order statistic without sorting",
        subtitle="One recursive call instead of two, and the range that disappears each time",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the rank, the array and the pivot rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "The comparisons are counted as quickselect makes them, and the baseline beside "
            "them is merge sort's own total on the same array.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - mom
# ---------------------------------------------------------------------------


def _mom(cfg):
    n = int(cfg.get("n", 45))
    group = str(cfg.get("group", 5))
    k = int(cfg.get("k", 23))

    markup = (
        _toolbar(
            "A pivot with a guarantee, and the recurrence it buys",
            "the level sums of T(n) = T(f1 n) + T(f2 n) + n, as exact fractions",
            [("cyan", "work at this level"), ("green", "the sum converges"),
             ("red", "the sum does not"), ("purple", "the guaranteed discard")],
        )
        + _stage(_svg("mmPlot", "0 0 520 210",
                      "The work at each level of the recursion tree, shrinking or not shrinking by the ratio."))
        + _table("mmTable")
        + _table("mmRounds")
        + _banner("mmStatus")
    )
    controls = (
        _range("mmN", "Array length", 15, 125, n)
        + _select("mmGroup", "Group size",
                  [("3", "groups of 3"), ("5", "groups of 5"), ("7", "groups of 7")], group)
        + _range("mmK", "Which order statistic", 1, 125, k)
        + _kpis([("f1 + f2, exactly", "mmSum"), ("The tree sums to", "mmTotal"),
                 ("Comparisons, median of medians", "mmCmp"), ("Comparisons, quickselect", "mmQs")])
        + _hint(
            "mmHint",
            "With groups of g the pivot is guaranteed to beat at least n(g+1)/(4g) elements "
            "and lose to as many, so the surviving side is at most n minus that. Whether the "
            "two fractions sum to under one is the entire linearity argument, and it is "
            "evaluated here as a fraction rather than as a decimal that nearly is.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var nS = document.getElementById('mmN'), groupSel = document.getElementById('mmGroup');
  var kS = document.getElementById('mmK');
  var plot = document.getElementById('mmPlot'), table = document.getElementById('mmTable');
  var rounds = document.getElementById('mmRounds'), status = document.getElementById('mmStatus');

  function redraw() {
    var n = +nS.value, group = parseInt(groupSel.value, 10);
    var k = Math.min(n, Math.max(1, +kS.value));
    document.getElementById('mmNOut').textContent = n + ' elements';
    document.getElementById('mmKOut').textContent = 'the ' + ordinal(k) + ' smallest';

    var f = momFractions(group);
    var levels = levelSums(f.f1, f.f2, n, 9);
    var a = sortInput('shuffle', n, 11, 'median3');
    var run = momRun(a, k, group);
    var truth = a.slice().sort(function (p, q) { return p - q; })[k - 1];

    document.getElementById('mmSum').textContent = Rtext(f.sum);
    document.getElementById('mmTotal').textContent = levels.geometric
      ? Rtext(levels.geometric) + ' = ' + Rfixed(levels.geometric, 2)
      : 'it does not converge';
    document.getElementById('mmCmp').textContent = groupDigits(run.counts.compares || 0);
    document.getElementById('mmQs').textContent = groupDigits(run.result.quickselectCompares);

    var s = '<text x="8" y="16" font-size="11" fill="var(--muted)">work at each level of the recursion tree, at n = '
      + n + ' and groups of ' + group + '</text>';
    var top = parseFloat(Rfixed(levels.rows[0].sum, 4)) || 1;
    levels.rows.forEach(function (row, i) {
      var v = parseFloat(Rfixed(row.sum, 4));
      var w = Math.max(2, Math.round((v / top) * 430));
      var y = 30 + i * 19;
      s += '<rect x="60" y="' + y + '" width="' + w + '" height="14" rx="3" fill="'
        + (f.converges ? 'var(--cyan)' : 'var(--red)') + '" opacity="0.55" />';
      s += '<text x="52" y="' + (y + 11) + '" text-anchor="end" font-size="10" fill="var(--muted)">level '
        + i + '</text>';
      s += '<text x="' + (64 + w) + '" y="' + (y + 11) + '" font-size="10" fill="var(--muted)">'
        + Rfixed(row.sum, 2) + '</text>';
    });
    s += '<text x="8" y="204" font-size="11" fill="' + (f.converges ? 'var(--green)' : 'var(--red)')
      + '">ratio between levels is f1 + f2 = ' + Rtext(f.sum) + ', so the levels '
      + (f.converges ? 'shrink geometrically' : 'do not shrink at all') + '</text>';
    plot.innerHTML = s;

    var rows = '';
    [3, 5, 7].forEach(function (g) {
      var gf = momFractions(g);
      var mine = g === group;
      rows += '<tr><td>' + (mine ? '<strong>groups of ' + g + '</strong>' : 'groups of ' + g)
        + '</td><td class="tt">' + Rtext(gf.f1) + '</td><td class="tt">' + Rtext(gf.f2)
        + '</td><td class="tt">' + Rtext(gf.sum) + '</td><td class="'
        + (gf.converges ? 'tone-green' : 'tone-red') + '">'
        + (gf.converges ? 'under 1, so linear' : 'exactly 1, so n log n') + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>group size</th><th>f1, the medians</th>'
      + '<th>f2, the side that survives</th><th>f1 + f2</th><th>verdict</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="5">The guaranteed discard at groups of ' + group
      + ' is <span class="tt">' + Rtext(f.discard) + '</span> of the array, which is '
      + Math.floor(parseFloat(Rfixed(Rmul(f.discard, R(BigInt(n), 1n)), 4))) + ' of these ' + n
      + ' elements. The pivot is not the median and does not need to be.</td></tr></tfoot>';

    /* The rounds themselves, because the misconception the lesson names is
       that the pivot is the median. It is not: what is guaranteed is that at
       least n(g+1)/(4g) elements fall on each side of it, and the two columns
       below let a reader watch the actual split beat that guarantee by a lot
       and never fall short of it. */
    var roundRows = run.trace.map(function (st) {
      var worst = Math.min(st.less, st.greater), guard = momGuarantee(st.n, group);
      return '<tr><td>' + (st.at + 1) + '</td><td>' + st.n + '</td><td>' + st.groups
        + '</td><td>' + st.pivot + '</td><td>' + st.less + ' | ' + st.equal + ' | ' + st.greater
        + '</td><td class="' + (worst >= guard ? 'tone-green' : 'tone-red') + '">at least ' + guard
        + (worst >= guard ? ', and ' + worst + ' fell' : ', and only ' + worst + ' fell') + '</td></tr>';
    }).join('');
    rounds.innerHTML = '<thead><tr><th>round</th><th>elements</th><th>groups of ' + group
      + '</th><th>the pivot</th><th>below | equal | above</th>'
      + '<th>guaranteed discard</th></tr></thead><tbody>' + roundRows + '</tbody>'
      + '<tfoot><tr><td colspan="6">The pivot is never claimed to be the median. What is claimed is '
      + 'the last column &mdash; ceil((g+1)/2) elements from each of at least half the groups, less the '
      + 'group holding the pivot and the partial one at the end &mdash; and the column beside it is what '
      + 'actually happened here. The gap between them is the slack the proof gives away to be true of '
      + 'every array rather than of this one.</td></tr></tfoot>';

    var agrees = run.result.value === truth;
    status.innerHTML = 'At groups of ' + group + ' the recurrence is T(<span class="tt">' + Rtext(f.f1)
      + '</span>n) + T(<span class="tt">' + Rtext(f.f2) + '</span>n) + n, and the two fractions sum to <span class="tt">'
      + Rtext(f.sum) + '</span>. '
      + (f.converges
          ? '<span class="tone-green">Under one</span>, so the level sums are a geometric series and the tree totals <span class="tt">'
            + Rtext(levels.geometric) + '</span> = ' + Rfixed(levels.geometric, 2)
            + ' &mdash; linear in n, exactly, with no asymptotic hand-waving anywhere in that sentence.'
          : '<span class="tone-red">Exactly one</span>, so every level costs n and the tree has about log n of them: groups of three give n log n, not linear.')
      + ' On this particular array of ' + n + ' it spent ' + groupDigits(run.counts.compares || 0)
      + ' comparisons against quickselect’s ' + groupDigits(run.result.quickselectCompares)
      + ', and both found ' + (agrees ? 'the same value the sorted array holds at that rank'
                                      : '<span class="tone-red">different values</span>')
      + '. Those two counts are one input each; the fractions above are the claim about all of them.';
  }

  [nS, groupSel, kS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The pivot only has to be near the middle",
        subtitle="Groups of three, five and seven, and the sum that decides which of them is linear",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the size, the group and the rank"),
        panel_intro=cfg.get(
            "panel_intro",
            "The two fractions in the recurrence are computed from the group size as exact "
            "rationals, and the level sums of the recursion tree are evaluated as fractions "
            "too, so the comparison with one is a comparison of integers.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - adversary
# ---------------------------------------------------------------------------

# n! arrangements: 5 040 at seven, 40 320 at eight, 362 880 at nine. Eight is
# what the sweep can enumerate inside a redraw, and the result is cached per n
# so that dragging the slider does not re-enumerate what it already knows.
_SWEEP_CAP = 8


def _adversary(cfg):
    n = int(cfg.get("n", 8))
    game = cfg.get("game", "max")
    left = int(cfg.get("left", 1))
    right = int(cfg.get("right", 2))

    markup = (
        _toolbar(
            "Play the algorithm; the lab plays the adversary",
            "every answer is chosen to keep the most outcomes alive",
            [("cyan", "still unbeaten"), ("muted", "has lost"),
             ("purple", "the comparison you asked"), ("amber", "the bound")],
        )
        + _stage(_svg("adPlot", "0 0 660 210",
                      "The elements still in contention, the comparisons asked, and the bound."))
        + _table("adTable")
        + _banner("adStatus")
    )
    controls = (
        _select("adGame", "Which bound",
                [("max", "the maximum, n - 1, played against the adversary"),
                 ("minmax", "the minimum and maximum together, ceil(3n/2) - 2"),
                 ("second", "the second largest, n + ceil(log2 n) - 2")], game)
        + _range("adN", "How many elements", 4, 16, n)
        + _range("adLeft", "Compare this one", 1, 16, left)
        + _range("adRight", "against this one", 1, 16, right)
        + _buttons([("adAsk", "Ask that comparison"), ("adReset", "Start again")], wrap="adPlay")
        + _kpis([("Comparisons made", "adCmp"), ("The bound for this game", "adBound"),
                 ("What is still undecided", "adOpen"), ("Over every arrangement", "adSweep")])
        + _hint(
            "adHint",
            "The adversary never picks an array. It answers each comparison so that the "
            "largest number of arrangements remain consistent with everything it has said, "
            "which is why it can force n - 1 comparisons against any strategy at all.",
        )
    )

    script = _CORE_JS + _OVERREACH + r"""
  var gameSel = document.getElementById('adGame'), nS = document.getElementById('adN');
  var leftS = document.getElementById('adLeft'), rightS = document.getElementById('adRight');
  var askBtn = document.getElementById('adAsk'), resetBtn = document.getElementById('adReset');
  var play = document.getElementById('adPlay');
  var plot = document.getElementById('adPlot'), table = document.getElementById('adTable');
  var status = document.getElementById('adStatus');
  var SWEEP_CAP = """ + str(_SWEEP_CAP) + r""";

  /* The adversary is state, so it is built once per size and kept. Rebuilding
     it inside redraw would wipe the reader's game every time a slider moved. */
  var game = null, gameN = 0, sweepCache = {};

  function ensureGame(n) {
    if (!game || gameN !== n) { game = adversaryMax(n); gameN = n; }
  }
  function sweep(n) {
    if (sweepCache[n] !== undefined) return sweepCache[n];
    var r;
    try { r = tournamentEvery(n, SWEEP_CAP); }
    catch (err) { r = { refused: err.message }; }
    sweepCache[n] = r;
    return r;
  }

  function drawMax(n) {
    var st = game.state(), s = '', w = Math.min(60, Math.floor(640 / n));
    s += '<text x="8" y="16" font-size="11" fill="var(--muted)">every element except one must lose at least once, and the adversary never lets two lose at the same time</text>';
    for (var v = 0; v < n; v += 1) {
      var beaten = st.unbeaten.indexOf(v) < 0, x = 8 + v * w;
      s += '<rect x="' + x + '" y="30" width="' + (w - 5) + '" height="40" rx="5" fill="'
        + (beaten ? 'var(--line-strong)' : 'var(--cyan)') + '" opacity="' + (beaten ? '0.22' : '0.55') + '" />';
      s += '<text x="' + (x + (w - 5) / 2) + '" y="55" text-anchor="middle" font-size="13"'
        + ' font-weight="700" fill="var(--text)">' + (v + 1) + '</text>';
      s += '<text x="' + (x + (w - 5) / 2) + '" y="84" text-anchor="middle" font-size="10" fill="var(--muted)">'
        + (beaten ? 'lost' : 'unbeaten') + '</text>';
    }
    var bar = Math.round((st.compares / Math.max(1, st.lower)) * 600);
    s += '<text x="8" y="118" font-size="11" fill="var(--muted)">comparisons you have spent, against the n &minus; 1 the adversary can force</text>';
    s += '<rect x="8" y="126" width="600" height="18" rx="4" fill="var(--line)" opacity="0.5" />';
    s += '<rect x="8" y="126" width="' + Math.min(600, Math.max(0, bar)) + '" height="18" rx="4" fill="var(--purple)" opacity="0.7" />';
    s += '<text x="616" y="140" font-size="11" fill="var(--amber)">' + st.compares + ' / ' + st.lower + '</text>';
    var recent = st.trace.slice(-4);
    recent.forEach(function (row, i) {
      s += '<text x="8" y="' + (166 + i * 15) + '" font-size="11" fill="var(--muted)">asked '
        + (row.i + 1) + ' against ' + (row.j + 1) + ' &rarr; ' + (row.winner + 1) + ' survives'
        + (row.newInfo ? '' : ', and you already knew that') + '</text>';
    });
    return s;
  }

  function drawPairs(run, n) {
    var s = '<text x="8" y="16" font-size="11" fill="var(--muted)">each pair is settled with one comparison, then the loser meets the running minimum and the winner the running maximum</text>';
    run.trace.slice(0, 7).forEach(function (row, i) {
      var y = 34 + i * 24;
      s += '<text x="8" y="' + (y + 12) + '" font-size="11" fill="var(--text)">' + row.pair[0]
        + ' and ' + row.pair[1] + '</text>';
      s += '<rect x="120" y="' + y + '" width="180" height="16" rx="3" fill="var(--cyan)" opacity="0.35" />';
      s += '<text x="128" y="' + (y + 12) + '" font-size="11" fill="var(--text)">minimum so far ' + row.min + '</text>';
      s += '<rect x="320" y="' + y + '" width="180" height="16" rx="3" fill="var(--amber)" opacity="0.35" />';
      s += '<text x="328" y="' + (y + 12) + '" font-size="11" fill="var(--text)">maximum so far ' + row.max + '</text>';
    });
    s += '<text x="8" y="200" font-size="11" fill="var(--muted)">' + (run.counts.compares || 0)
      + ' comparisons for both ends, against ' + run.result.naive + ' for two separate scans</text>';
    return s;
  }

  function drawRounds(run) {
    var s = '<text x="8" y="16" font-size="11" fill="var(--muted)">the tournament, round by round; the winner of the last round met ceil(log2 n) opponents</text>';
    run.result.rounds.forEach(function (round, r) {
      var y = 36 + r * 30, w = Math.min(58, Math.floor(600 / Math.max(1, round.length)));
      s += '<text x="8" y="' + (y + 15) + '" font-size="10" fill="var(--muted)">round ' + (r + 1) + '</text>';
      round.forEach(function (v, i) {
        var x = 66 + i * w;
        s += '<rect x="' + x + '" y="' + y + '" width="' + (w - 5) + '" height="22" rx="3" fill="'
          + (r === run.result.rounds.length - 1 ? 'var(--purple)' : 'var(--cyan)') + '" opacity="0.4" />';
        s += '<text x="' + (x + (w - 5) / 2) + '" y="' + (y + 16) + '" text-anchor="middle"'
          + ' font-size="11" fill="var(--text)">' + v + '</text>';
      });
    });
    return s;
  }

  function redraw() {
    var which = gameSel.value, n = +nS.value;
    ensureGame(n);
    var i = Math.min(n, Math.max(1, +leftS.value)), j = Math.min(n, Math.max(1, +rightS.value));
    document.getElementById('adNOut').textContent = n + ' elements';
    document.getElementById('adLeftOut').textContent = which === 'max'
      ? 'element ' + i : 'element ' + i + ', used when you play the maximum';
    document.getElementById('adRightOut').textContent = which === 'max'
      ? 'element ' + j : 'element ' + j + ', likewise';
    play.hidden = which !== 'max';
    askBtn.hidden = which !== 'max';
    resetBtn.hidden = which !== 'max';

    var values = sortInput('shuffle', n, 3, 'median3');
    var rows = '', banner = '';

    if (which === 'max') {
      var st = game.state();
      plot.innerHTML = drawMax(n);
      document.getElementById('adCmp').textContent = st.compares;
      document.getElementById('adBound').textContent = st.lower + ' comparisons';
      document.getElementById('adOpen').textContent = st.unbeaten.length + ' still unbeaten';
      document.getElementById('adSweep').textContent = 'not enumerated for this game';
      rows = st.trace.map(function (row, idx) {
        return '<tr><td>' + (idx + 1) + '</td><td>' + (row.i + 1) + ' against ' + (row.j + 1)
          + '</td><td>' + (row.winner + 1) + '</td><td class="'
          + (row.newInfo ? 'tone-green' : 'tone-red') + '">'
          + (row.newInfo ? 'one more element has lost' : 'nothing new: that element had already lost')
          + '</td></tr>';
      }).join('');
      table.innerHTML = '<thead><tr><th>comparison</th><th>you asked</th><th>the adversary says</th>'
        + '<th>what it bought you</th></tr></thead><tbody>' + rows + '</tbody>';
      banner = 'You have spent <strong>' + st.compares + '</strong> comparisons and '
        + st.unbeaten.length + ' element' + (st.unbeaten.length === 1 ? ' is' : 's are')
        + ' still unbeaten. '
        + (st.settled
            ? (st.compares === st.lower
                ? '<span class="tone-green">Settled in exactly n &minus; 1</span>, which is the best any algorithm can do here &mdash; and the reason is the column beside each comparison: a comparison can only make one element lose for the first time.'
                : 'Settled, but in ' + st.compares + ' rather than ' + st.lower + ': the wasted comparisons are the ones marked as telling you nothing new.')
            : 'Until only one is unbeaten the maximum is not determined, so at least '
              + (st.unbeaten.length - 1) + ' more comparison'
              + (st.unbeaten.length - 1 === 1 ? ' is' : 's are') + ' still needed.')
        + ' The bound is not measured from your play: it is n &minus; 1 because every element but one must lose, and no single comparison can retire two of them.';
    } else if (which === 'minmax') {
      var mm = minMaxPairs(values);
      plot.innerHTML = drawPairs(mm, n);
      document.getElementById('adCmp').textContent = mm.counts.compares || 0;
      document.getElementById('adBound').textContent = mm.result.bound + ' comparisons';
      document.getElementById('adOpen').textContent = 'both ends found';
      document.getElementById('adSweep').textContent = 'the pairing is deterministic';
      rows = '<tr><td>pair first, then push each way</td><td>' + (mm.counts.compares || 0)
        + '</td><td>' + mm.result.bound + '</td><td>'
        + ((mm.counts.compares || 0) <= mm.result.bound ? 'meets the bound' : 'over the bound') + '</td></tr>'
        + '<tr><td>two separate scans</td><td>' + mm.result.naive + '</td><td>' + mm.result.bound
        + '</td><td>' + (mm.result.naive - mm.result.bound) + ' comparisons wasted</td></tr>';
      table.innerHTML = '<thead><tr><th>strategy</th><th>comparisons</th><th>the bound</th>'
        + '<th>verdict</th></tr></thead><tbody>' + rows + '</tbody>';
      banner = 'Finding both ends of ' + n + ' elements took <strong>' + (mm.counts.compares || 0)
        + '</strong> comparisons, and the adversary bound is ceil(3n/2) &minus; 2 = ' + mm.result.bound
        + '. Two independent scans would cost ' + mm.result.naive
        + '. The saving comes from the first comparison of each pair: it settles which of the two can still be the minimum and which can still be the maximum, so the pair costs three comparisons for two ends rather than four.';
    } else {
      var t = tournament(values), scan = scanSecond(values);
      plot.innerHTML = drawRounds(t);
      var sw = sweep(n);
      document.getElementById('adCmp').textContent = t.counts.compares || 0;
      document.getElementById('adBound').textContent = t.result.bound + ' comparisons';
      document.getElementById('adOpen').textContent = t.result.candidates + ' lost to the winner';
      document.getElementById('adSweep').textContent = sw.refused
        ? 'refused above ' + SWEEP_CAP : 'worst was ' + sw.worst + ' of ' + sw.bound;
      rows = '<tr><td>tournament, then the losers to the winner</td><td>' + (t.counts.compares || 0)
        + '</td><td>' + t.result.max + ' and ' + t.result.second + '</td><td>'
        + (n - 1) + ' to find the winner, then ' + Math.max(0, t.result.candidates - 1)
        + ' among the ' + t.result.candidates + ' it beat</td></tr>'
        + '<tr><td>one scan keeping the best two</td><td>' + (scan.counts.compares || 0)
        + '</td><td>' + scan.result.max + ' and ' + scan.result.second + '</td><td>'
        + 'up to 2n &minus; 3 = ' + (2 * n - 3) + ', because a loser is compared twice</td></tr>'
        + '<tr><td>every arrangement of 1 to ' + n + '</td><td>'
        + (sw.refused ? '&mdash;' : sw.worst + ' at worst') + '</td><td>'
        + (sw.refused ? '&mdash;' : groupDigits(sw.arrangements) + ' of them, ' + sw.wrong + ' wrong')
        + '</td><td>' + (sw.refused ? sw.refused
            : (sw.over === 0 ? 'not one of them went over the bound' : sw.over + ' went over the bound'))
        + '</td></tr>';
      table.innerHTML = '<thead><tr><th>strategy</th><th>comparisons</th><th>what it found</th>'
        + '<th>why</th></tr></thead><tbody>' + rows + '</tbody>';
      banner = 'On this arrangement the tournament used <strong>' + (t.counts.compares || 0)
        + '</strong> comparisons against the bound n + ceil(log<sub>2</sub> n) &minus; 2 = '
        + t.result.bound + ', while keeping the best two in one scan used ' + (scan.counts.compares || 0)
        + '. '
        + (sw.refused
            ? 'That is one arrangement out of ' + n + '!, and this panel does not enumerate them at this size: ' + sw.refused
            : 'And this is the one figure on the page that is <span class="tone-green">not about one input</span>: every one of the '
              + groupDigits(sw.arrangements) + ' arrangements of 1 to ' + n + ' was run, the worst cost '
              + sw.worst + ' comparisons, ' + (sw.over === 0 ? 'none exceeded the bound' : sw.over + ' exceeded the bound')
              + ' and ' + (sw.wrong === 0 ? 'every one returned the true second largest' : sw.wrong + ' returned the wrong answer') + '.')
        + ' The second largest is cheap because it can only be an element that lost to the winner, and the tournament leaves only ceil(log<sub>2</sub> n) of those.';
    }
    status.innerHTML = banner;
  }

  askBtn.addEventListener('click', function () {
    var n = +nS.value;
    ensureGame(n);
    var i = Math.min(n, Math.max(1, +leftS.value)) - 1, j = Math.min(n, Math.max(1, +rightS.value)) - 1;
    if (i !== j) game.ask(i, j);
    redraw();
  });
  resetBtn.addEventListener('click', function () { game = null; redraw(); });
  [gameSel, nS, leftS, rightS].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A lower bound is an argument, not a measurement",
        subtitle="Answer comparisons to keep the most outcomes alive, then meet each bound with an algorithm",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the bound and play"),
        panel_intro=cfg.get(
            "panel_intro",
            "The adversary holds no array. It answers each comparison so as to leave the "
            "most possibilities open, and the bound that falls out is a statement about "
            "every algorithm rather than about the one you played.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "stability": _stability,
    "partition": _partition,
    "quick": _quick,
    "expected": _expected,
    "counting": _counting,
    "radix": _radix,
    "bucket": _bucket,
    "select": _select_mode,
    "mom": _mom,
    "adversary": _adversary,
}

MODES = tuple(sorted(_MODES))


def sortkit_lab(cfg):
    """The sorting course's kit. `cfg["mode"]` chooses the lesson.

    An unknown mode raises, and the raise is the contract rather than
    defensiveness. A kit that fell back to a default would render a
    finished-looking page carrying another lesson's widget under this lesson's
    title, and nothing downstream would catch it: the markup assertions pass,
    labcheck passes, and the reader is taught the wrong thing confidently.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "sortkit_lab: unknown mode %r; the ten modes of the sorting course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["sortkit_lab", "SORTKIT_JS", "MODES"]
