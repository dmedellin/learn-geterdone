"""Course 10: Measuring Systems -- one kit, ten modes, one arithmetic.

Every earlier course produced a number. This one asks how you would know it
from a live system, and the answer is that you would not know it exactly: the
measurement has an error bar, a bucket width, a sampling rate, a scrape
interval and a threshold, and each of those is a way the number can be wrong
while looking right. Each mode makes one of those into arithmetic the reader
can move.

Six decisions run through all ten.

  PERCENTILES COME FROM sysdesign_core, NOT FROM HERE. `percentile` and
  `percentileRank` are nearest rank, they are what course 2's `latency` kit
  prints, and `aggregate`, `histogram` and `omission` all call them rather than
  defining a second rule. That is the point of those three lessons: the fleet
  p99, the bucketed p99 and the corrected p99 are three answers produced by ONE
  definition applied to three different samples, and a kit that quietly used a
  second definition would be teaching that the disagreement is a matter of
  convention. It is not. It is a fact about the sample.

  ONE FORMULA, NAMED WHERE IT REPEATS. `atLeastOne(p, k) = 1 - (1-p)^k` is the
  sampling lesson's capture probability, the load-test lesson's "did the run
  ever see the tail", and the alerting lesson's "did a rare false alarm happen
  at least once this month". They are the same arithmetic and the three modes
  call the same function, so the pages can say so without the reader having to
  take it on trust.

  THE BUDGET IS 30 DAYS HERE, AND IT SAYS SO. 99.9% of a 30-day window is
  exactly 43.2 minutes, which is the figure burn-rate alerting is quoted
  against. Course 5's `avail` kit uses a 2 628 000-second month -- a twelfth of
  a 365-day year -- under which the same objective is 43.8 minutes, and counts
  the budget in failed requests rather than in minutes. Both are right; they
  are different conventions, and `burn` prints which one it is using and what
  the other would give, because a reader who cannot reconcile two pages of the
  same library assumes one of them is broken.

  EXACT EXCEPT FOR ONE ROOT AND ONE IDEALISATION, BOTH LABELLED. Capture
  probabilities, binomial tails, bucket widths, cardinalities and budget
  fractions are exact fractions. `sli` prints a square root, so it calls
  `standardErrorApprox` and says on its face that the figure rounds -- while
  the variance under the root, and the sample size the lesson solves for, stay
  exact. `sample` additionally prints the 1 - e^(-sk) idealisation beside the
  exact 1 - (1-s)^k, computed by `expNegApprox`, which rounds; that mode says
  so and also says the thing worth knowing, which is that the rounding is
  around 1e-13 while the gap to the exact answer is 4.5e-4 on that mode's own
  preset -- nine orders of magnitude larger, because an approximation and a
  rounded approximation are different kinds of wrong.

  NOTHING IS AVERAGED THAT CANNOT BE AVERAGED. The kit computes the mean of a
  set of per-host p99s in exactly one place, `aggregate`, where the whole
  lesson is that the number is not a percentile of anything.

  ONE SEEDED STREAM, AND NOT THE PATH'S DEFAULT ONE. `scrape` draws spike times
  and then takes them modulo a horizon and compares them modulo a scrape
  interval, so it uses MINSTD -- multiplier 16807, modulus 2^31 - 1, prime --
  rather than the glibc constants the rest of the path uses, whose power-of-two
  modulus makes the low bits a cycle instead of a sample. Under those constants
  a run at a 4, 8 or 16 second interval catches exactly d/I of its spikes every
  time, which is precisely the claim this lesson exists to deny. The seed is put
  through the splitmix64 finaliser first for the reason shard.py sets out: an
  LCG's value is affine in its seed, and this mode asks the reader to reseed.

The modes, and the lesson each belongs to:

  sli         L1  sqrt(p(1-p)/n), the +/- against the objective, and the n it needs
  aggregate   L2  the fleet p99 from the merged sample, against the mean of the p99s
  histogram   L3  the containing bucket, its width, and the factor-r error
  omission    L4  the naive p99, and the p99 after the skipped requests are imputed
  scrape      L5  min(1, d/I), the longest invisible spike, a run's misses, and
                  the rate a counter reset breaks -- see the note below
  sample      L6  1 - (1-s)^k, the rate that catches a rare event, and reweighting
  cardinality L7  the product of the label cardinalities, and the bytes it costs
  loadtest    L8  1 - (1-t)^n, and the n a stated confidence needs, by exact search
  burn        L9  b*w/period, period/b, and the multi-window pairs
  threshold   L10 the exact binomial tail of a threshold, and pages per week

One thing this kit shows that section 4.10 of the design gives no mode for: a
counter that RESETS. A rate is a difference between two reads, a restart sets
the counter to zero, and the naive difference across that is a large negative
-- or, once the counter has climbed again, a small positive that reads as a
quiet spell. It belongs with L5 because it is the second thing a scrape
interval cannot see: the reset itself is invisible and the only evidence for it
is that the number went down. So `scrape` carries it as a second panel with its
own two controls, rather than inventing an eleventh mode for a lesson that does
not exist.
"""

import json

from .algebra_core import RATIONAL_JS
from .common import Lab
from .counting import BIGINT_JS
from .sysdesign_core import APPROX_JS, AVAIL_JS, PERCENTILE_JS, RCEIL_JS, STREAM_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

MEASURE_JS = r"""
  /* ================================================================= output

     Rdec goes through Number(a.n)/Number(a.d), and this course produces
     rationals a double cannot hold: (999/1000)^2996 -- the load-test answer at
     95% confidence -- has a numerator of nine thousand digits, Number() of it
     is Infinity, and Infinity/Infinity is NaN. So decimals here are long
     division in BigInt, rounded half up at the last digit printed. */
  function Rfixed(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);          /* round half up */
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }
  /* Scaling by a hundred THROUGH THE NUMERATOR, not through Rmul.

     Rmul goes via R(), which runs a gcd, and the fractions printed here have
     numerators of thousands of digits -- one such gcd costs more than every
     other computation on the page put together. Rfixed only long-divides, so
     the fraction it is handed does not have to be in lowest terms, and the
     value printed is identical. */
  function Rpct(a, places) {
    return Rfixed({ n: a.n * 100n, d: a.d }, places === undefined ? 2 : places) + '%';
  }
  /* A probability that is nearly 1 or nearly 0 needs its own width, because a
     fixed two places prints 0.9999994 as 100.00% -- which is the claim these
     alerting lessons deny. Widen until a non-nine appears, to a limit. */
  function RpctAuto(a) {
    var scaled = { n: a.n * 100n, d: a.d }, places = 2, i;
    for (i = 2; i <= 10; i += 1) {
      var s = Rfixed(scaled, i);
      places = i;
      /* Anchored at BOTH ends: the test is "did this round away to 100 or to
         zero", not "does it happen to end in a nought". Unanchored, 50.00%
         looks degenerate because of the nought in 50. */
      if (!/^(100|0)\.0*$/.test(s)) break;
    }
    return Rfixed(scaled, places) + '%';
  }
  /* A double for a PIXEL COORDINATE, and never for a figure.

     Rnum is Number(a.n)/Number(a.d), and the probabilities on this course have
     denominators of hundreds or thousands of digits: Number() of one of those
     is Infinity, Infinity/Infinity is NaN, and a chart of NaNs paints nothing
     while throwing nothing -- the failure looks like a styling problem. So a
     coordinate is long-divided to nine places first. Every printed figure
     comes from Rfixed or Rpct on the exact fraction, never from here. */
  function Rplot(a) { return parseFloat(Rfixed(a, 9)); }

  /* Milliseconds, seconds, minutes and hours from an exact rational count of
     minutes -- the budget lesson's one unit, converted once, here. */
  function minutesText(a) {
    if (Rcmp(a, R(1n, 1n)) < 0) return Rfixed(Rmul(a, R(60n, 1n)), 1) + ' s';
    if (Rcmp(a, R(120n, 1n)) < 0) return Rfixed(a, 2) + ' min';
    if (Rcmp(a, R(2880n, 1n)) < 0) return Rfixed(Rdiv(a, R(60n, 1n)), 2) + ' h';
    return Rfixed(Rdiv(a, R(1440n, 1n)), 2) + ' days';
  }

  /* ============================================ THE FORMULA THAT REPEATS

     P(at least one of k independent trials happens) = 1 - (1-p)^k.

     It is the sampling lesson's capture probability at rate p over k slow
     requests, the load-test lesson's "did n requests ever include one from the
     top 0.1%", and the alerting lesson's "did a 0.1%-per-window false alarm
     fire at least once in a month of windows". Three lessons, three stories,
     one function -- so that a page can say they are the same formula and the
     reader can check that the same code produced all three.

     WHY THIS IS NOT Rsub(1, Rpow(1 - p, k)), WHICH IS WHAT IT MEANS. R()
     normalises with a gcd on every operation, and the powers this course asks
     for are enormous: at p = 1/1000 and k = 8640 the numerator has 26 000
     digits, one gcd on which costs about a second, and a lab that recomputes
     while a slider is dragged cannot pay that.

     Two facts make the gcd unnecessary. Writing p = a/b in lowest terms --
     which R() guarantees -- the value is (b^k - (b-a)^k)/b^k; and
     gcd(b, b - a) = gcd(b, a) = 1, so a prime dividing b^k divides the
     numerator only if it divides (b-a)^k, which it cannot. The fraction is
     therefore ALREADY in lowest terms and needs no reduction. It is exact, not
     an approximation, and scripts/mathcheck.js asserts that it agrees with the
     rational-arithmetic form term for term. */
  function atLeastOne(p, k) {
    var a = p.n, b = p.d;
    if (k <= 0 || a === 0n) return R(0n, 1n);
    var bk = b ** BigInt(k);
    return { n: bk - (b - a) ** BigInt(k), d: bk };
  }
  /* The same value at n = 0, step, 2*step, ... for the curve a page draws.

     Carrying the power forward one factor at a time rather than recomputing it
     at each point: the load-test lesson plots sixty points out to three
     thousand requests, and sixty independent (999/1000)^n each with a
     nine-thousand-digit numerator is a second and a half of arithmetic for a
     picture. Every entry is the same exact fraction atLeastOne returns, by the
     same argument about lowest terms. */
  function atLeastOneCurve(p, step, points) {
    var a = p.n, b = p.d, f = (b - a) ** BigInt(step), g = b ** BigInt(step);
    var num = 1n, den = 1n, out = [], i;
    for (i = 0; i <= points; i += 1) {
      out.push({ n: den - num, d: den });
      num *= f;
      den *= g;
    }
    return out;
  }
  /* The smallest k for which that reaches a target, by exact integer search:
     doubling to bracket, then bisection. No logarithm -- a logarithm would
     round, and this answer is a count. */
  function trialsForTarget(p, target, limit) {
    if (Rcmp(p, R(0n, 1n)) <= 0) return 0;
    if (Rcmp(target, R(1n, 1n)) >= 0) return 0;          /* certainty needs infinity */
    if (Rcmp(atLeastOne(p, 1), target) >= 0) return 1;
    var lo = 1, hi = 2;
    while (hi <= limit && Rcmp(atLeastOne(p, hi), target) < 0) { lo = hi; hi *= 2; }
    if (hi > limit) return 0;
    while (lo + 1 < hi) {
      var mid = (lo + hi) >> 1;
      if (Rcmp(atLeastOne(p, mid), target) >= 0) hi = mid; else lo = mid;
    }
    return hi;
  }
  /* The smallest rate, in units of 1/steps, that catches at least one of k with
     the stated confidence. A scan rather than a solve, for the same reason. */
  function rateForTarget(k, target, steps) {
    for (var j = 1; j <= steps; j += 1) {
      if (Rcmp(atLeastOne(R(BigInt(j), BigInt(steps)), k), target) >= 0) return R(BigInt(j), BigInt(steps));
    }
    return R(1n, 1n);
  }
  /* The same answer by bisection instead of by scanning, for the callers whose
     k is in the thousands: atLeastOne rises with j, so the search is exact, and
     a scan of ten thousand rates each raising a sixty-thousand-digit power does
     not finish while a slider moves. mathcheck.js asserts the two agree.

     The SLI lesson reads this backwards and gets the rule of three: with no
     failures in n requests, the largest failure rate that would still have let
     the window come back clean with probability 1 - c is this same rate at
     k = n. At n = 1000 and c = 95% it is exactly 3/1000. */
  function rateForTargetSearch(k, target, steps) {
    var lo = 0, hi = steps;
    if (Rcmp(atLeastOne(R(1n, BigInt(steps)), k), target) >= 0) return R(1n, BigInt(steps));
    while (lo + 1 < hi) {
      var mid = (lo + hi) >> 1;
      if (Rcmp(atLeastOne(R(BigInt(mid), BigInt(steps)), k), target) >= 0) hi = mid; else lo = mid;
    }
    return R(BigInt(hi), BigInt(steps));
  }
  /* The rule of thumb the same lesson prints beside the exact answer:
     1 - e^(-sk). It ROUNDS -- expNegApprox sums a positive-term series and
     divides, to about 1e-13 -- and it is also a different number, because the
     idealisation is not the exact binomial. Both facts are on the page. */
  function captureApprox(s, k) { return 1 - expNegApprox(Rnum(s) * k, 1e-15); }

  /* ============================================ L1: an SLI and its error bar

     An SLI is good/total over a window. The estimator's variance is p(1-p)/n
     EXACTLY -- that part is a fraction and stays one -- and the standard error
     is its square root, which is the one irrational figure on this course. */
  function sliRatio(good, total) { return R(BigInt(good), BigInt(total)); }
  function sliVariance(p, n) {
    return Rdiv(Rmul(p, Rsub(R(1n, 1n), p)), R(BigInt(n), 1n));
  }
  /* Rounds, and every caller says so. */
  function sliSeApprox(p, n) { return standardErrorApprox(Rnum(p), n); }
  /* The n at which the standard error is at most w, by exact comparison:
     p(1-p)/n <= w^2 needs no root at all, which is why this answer is exact
     while the error bar it sizes is not. Doubling, then bisection. */
  function sampleSizeForWidth(p, w) {
    var v = Rmul(p, Rsub(R(1n, 1n), p)), w2 = Rmul(w, w);
    if (Rzero(w2)) return 0;
    if (Rzero(v)) return 1;
    var fits = function (n) { return Rcmp(Rdiv(v, R(BigInt(n), 1n)), w2) <= 0; };
    if (fits(1)) return 1;
    var lo = 1, hi = 2;
    while (!fits(hi) && hi < 1000000000) { lo = hi; hi *= 2; }
    while (lo + 1 < hi) { var mid = Math.floor((lo + hi) / 2); if (fits(mid)) hi = mid; else lo = mid; }
    return hi;
  }
  /* The same answer in closed form, ceil(p(1-p)/w^2). The page prints both and
     they must agree: a search and a formula that disagree mean one is wrong,
     and the reader is entitled to see which. */
  function sampleSizeClosed(p, w) {
    var w2 = Rmul(w, w);
    if (Rzero(w2)) return 0n;
    var n = Rceil(Rdiv(Rmul(p, Rsub(R(1n, 1n), p)), w2));
    return n < 1n ? 1n : n;
  }
  /* How many standard errors separate an observation from an objective. The
     misconception this lesson refutes is reading a gap of 0.7 SE as evidence. */
  function sigmasApprox(p, objective, n) {
    var se = sliSeApprox(p, n);
    if (!(se > 0)) return Infinity;
    return Math.abs(Rnum(Rsub(p, objective))) / se;
  }

  /* ================================================ L2: aggregating samples

     A sample is a sorted list of integer milliseconds. It is typed either as
     values or as value:count runs, because the lesson's preset needs one host
     with ninety requests on it and nobody types ninety numbers.

     percentile() and percentileRank() are NOT defined here. They come from
     sysdesign_core, they are nearest rank, and they are the same two functions
     course 2 prints its p99 with. */
  function parseRuns(text) {
    var parts = String(text).split(/[,;\s]+/), out = [], i, j;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var m = /^([0-9]+)(?::([0-9]+))?$/.exec(s);
      if (!m) return null;
      var v = Number(m[1]), c = m[2] === undefined ? 1 : Number(m[2]);
      if (c < 1 || c > 4000) return null;
      for (j = 0; j < c; j += 1) out.push(v);
    }
    if (!out.length) return null;
    return out.sort(function (a, b) { return a - b; });
  }
  function mergeSamples(lists) {
    var out = [], i;
    for (i = 0; i < lists.length; i += 1) out = out.concat(lists[i]);
    return out.sort(function (a, b) { return a - b; });
  }
  function sampleMean(sorted) {
    var s = 0n;
    for (var i = 0; i < sorted.length; i += 1) s += BigInt(sorted[i]);
    return R(s, BigInt(sorted.length));
  }
  /* The mean of a list of per-host percentiles. This is the ONLY place in the
     kit that averages percentiles, and it exists to be contradicted. */
  function meanOfPercentiles(values) {
    var s = 0n;
    for (var i = 0; i < values.length; i += 1) s += BigInt(values[i]);
    return R(s, BigInt(values.length));
  }
  function hostPercentiles(lists, q) {
    var out = [];
    for (var i = 0; i < lists.length; i += 1) out.push(percentile(lists[i], q));
    return out;
  }
  /* The fleet percentile: the percentile OF THE MERGED SAMPLE. One definition,
     applied to every request the fleet served. */
  function fleetPercentile(lists, q) { return percentile(mergeSamples(lists), q); }
  /* The bound that does hold: the pooled percentile can never exceed the
     largest per-host one, because ceil(qn_1) + ... + ceil(qn_h) >= ceil(qN).
     The mean of the per-host percentiles has no such relation to anything,
     which is the lesson. */
  function maxOf(values) {
    var m = values[0];
    for (var i = 1; i < values.length; i += 1) if (values[i] > m) m = values[i];
    return m;
  }
  function minOf(values) {
    var m = values[0];
    for (var i = 1; i < values.length; i += 1) if (values[i] < m) m = values[i];
    return m;
  }

  /* ============================================== L3: histograms and buckets

     A histogram does not store the requests. It stores how many fell in each
     bucket, so a percentile read off it is known only to the width of the
     bucket that contains it. With exponential buckets at ratio r, every bucket
     is r times as wide as its lower edge, so the answer is known to a FACTOR
     of r -- a p99 reported as 100 ms with r = 2 is somewhere in [100, 200).

     Edges are exact rationals, so r = 3/2 is a ratio of three halves and not
     1.4999999999999998. */
  function bucketEdges(base, ratio, count) {
    var out = [], b = R(BigInt(base), 1n), i;
    for (i = 0; i <= count; i += 1) out.push(Rmul(b, Rpow(ratio, i)));
    return out;
  }
  /* The bucket containing a value: -1 below the first edge, edges.length - 1
     for the open-ended overflow bucket above the last. */
  function bucketIndex(edges, value) {
    var v = R(BigInt(value), 1n), i;
    if (Rcmp(v, edges[0]) < 0) return -1;
    for (i = 0; i + 1 < edges.length; i += 1) {
      if (Rcmp(v, edges[i + 1]) < 0) return i;
    }
    return edges.length - 1;
  }
  /* Counts per bucket, with the two open ends kept separate rather than folded
     in: a sample that overflows the last edge is a histogram that cannot
     report its own tail at all, and the page has to be able to say so. */
  function bucketCounts(sorted, edges) {
    var under = 0, over = 0, inside = [], i;
    for (i = 0; i + 1 < edges.length; i += 1) inside.push(0);
    for (i = 0; i < sorted.length; i += 1) {
      var b = bucketIndex(edges, sorted[i]);
      if (b < 0) under += 1;
      else if (b >= inside.length) over += 1;
      else inside[b] += 1;
    }
    return { under: under, inside: inside, over: over };
  }
  /* What the HISTOGRAM can report: the first bucket whose cumulative count
     reaches the rank the percentile needs. The rank is percentileRank from the
     core -- the same rank the exact percentile uses -- so the only difference
     between the two answers is the bucketing, which is the lesson. */
  function histogramBucket(sorted, edges, q) {
    var rank = percentileRank(sorted.length, q);
    var counts = bucketCounts(sorted, edges), cum = counts.under, i;
    if (cum >= rank) return -1;
    for (i = 0; i < counts.inside.length; i += 1) {
      cum += counts.inside[i];
      if (cum >= rank) return i;
    }
    return counts.inside.length;
  }
  function bucketWidth(edges, i) {
    if (i < 0 || i + 1 >= edges.length) return null;
    return Rsub(edges[i + 1], edges[i]);
  }
  /* The relative width of any bucket is r - 1, at every scale. That is the
     whole argument for exponential bucketing: the error is a constant
     PERCENTAGE rather than a constant number of milliseconds. */
  function bucketRelative(ratio) { return Rsub(ratio, R(1n, 1n)); }

  /* ================================================== L4: coordinated omission

     A closed-loop generator sends the next request when the last one comes
     back. During a stall it therefore sends nothing, so a stall that should
     have hit every request scheduled inside it is measured exactly once.

     The correction is to impute the requests the schedule called for: at an
     interval I, a stall of S beginning with a request at time T means requests
     were due at T + I, T + 2I, ... up to T + S, and each of those would have
     waited until the stall cleared -- latencies S - I, S - 2I, ... down to the
     last one still inside the stall. Nothing random, nothing precomputed:
     integer arithmetic on the numbers the reader set. */
  function naiveSample(n, serviceMs, stallMs) {
    var out = [], i;
    for (i = 0; i < n - 1; i += 1) out.push(serviceMs);
    out.push(stallMs);
    return out.sort(function (a, b) { return a - b; });
  }
  function imputedLatencies(intervalMs, stallMs) {
    var out = [], j;
    if (intervalMs <= 0) return out;
    for (j = 1; j * intervalMs < stallMs; j += 1) out.push(stallMs - j * intervalMs);
    return out;
  }
  function correctedSample(n, intervalMs, serviceMs, stallMs) {
    return naiveSample(n, serviceMs, stallMs)
      .concat(imputedLatencies(intervalMs, stallMs))
      .sort(function (a, b) { return a - b; });
  }
  /* How much of the stall the generator never charged anyone for. */
  function omittedCount(intervalMs, stallMs) { return imputedLatencies(intervalMs, stallMs).length; }

  /* ================================================= L5: scrape intervals

     A gauge is read every I seconds. A spike of duration d is seen only if a
     read instant falls inside it, so the probability over a uniformly random
     phase is min(1, d/I) -- exact, and the min is a comparison, not a rounding.

     The longest spike that can be entirely invisible is therefore one instant
     short of the interval: at a one-second granularity, I - 1 seconds. */
  function catchProbability(d, I) {
    if (I <= 0) return R(1n, 1n);
    var p = R(BigInt(d), BigInt(I));
    return Rcmp(p, R(1n, 1n)) >= 0 ? R(1n, 1n) : p;
  }
  function longestInvisible(I) { return I <= 1 ? 0 : I - 1; }
  /* One RUN, from the seeded stream in sysdesign_core: spike start times drawn
     over a horizon, then the scrape instants laid over them and the hits
     counted. The probability above is what happens on average; this is what
     happened on the run drawn, and the two differ, which is the point of
     showing both. */
  /* MINSTD -- a = 16807, c = 0, m = 2^31 - 1, which is PRIME -- rather than the
     glibc constants the rest of the path uses, because these draws are consumed
     MODULO a horizon and then compared modulo a scrape interval. Under a
     power-of-two modulus the low bits are a cycle and not a sample: x % 4 runs
     0, 1, 2, 3 forever, so at an interval of 4, 8 or 16 seconds the drawn run
     would catch exactly d/I of its spikes every single time, and this page --
     whose whole point is that one run is NOT the probability -- would be
     demonstrating the arithmetic with the arithmetic. A prime modulus shares no
     factor with any reducer.

     The seed is mixed before it becomes a state, by the splitmix64 finaliser,
     for the reason shard.py sets out: an LCG's k-th value is affine in its
     seed, so the small seeds a slider offers walk a straight line instead of
     sampling, and this mode asks the reader to reseed and compare. */
  function measureSeedState(seed) {
    var mask = 0xFFFFFFFFFFFFFFFFn;
    var x = (BigInt(seed) + 1n) * 0x9E3779B97F4A7C15n & mask;
    x = ((x ^ (x >> 30n)) * 0xBF58476D1CE4E5B9n) & mask;
    x = ((x ^ (x >> 27n)) * 0x94D049BB133111EBn) & mask;
    x = x ^ (x >> 31n);
    return Number(x % 2147483646n) + 1;                /* never the fixed point 0 */
  }
  function measureStream(seed, count) {
    return lcgStream(16807, 0, 2147483647, measureSeedState(seed), count);
  }
  function spikeStarts(count, horizon, seed) {
    var raw = measureStream(seed, count), out = [], i;
    for (i = 0; i < raw.length; i += 1) out.push(raw[i] % horizon);
    return out.sort(function (a, b) { return a - b; });
  }
  function scrapeInstants(I, offset, horizon) {
    var out = [], t;
    for (t = offset; t < horizon; t += I) out.push(t);
    return out;
  }
  /* A spike covering [s, s + d) is caught if any instant lands in it. */
  function spikeCaught(start, d, I, offset) {
    if (I <= 0) return true;
    var first = Math.ceil((start - offset) / I) * I + offset;
    return first < start + d;
  }
  function caughtCount(starts, d, I, offset) {
    var c = 0;
    for (var i = 0; i < starts.length; i += 1) if (spikeCaught(starts[i], d, I, offset)) c += 1;
    return c;
  }

  /* ----------------------------------------- L5 also: a counter that resets

     A rate is the difference between two reads divided by the time between
     them. A process restart sets the counter back to zero, so the two reads
     either side of it differ by a NEGATIVE number, and the naive rate is a
     large negative -- or worse, where the counter has climbed again before the
     next read, a small positive that reads as a quiet period.

     The correction is the one every time-series database makes: a decrease
     between consecutive reads is a reset, and the increase across that gap is
     the second read itself, because the counter started again from zero. It is
     right in sign and still low in value, because the increments between the
     last read and the restart went with the process; the page prints how many
     were lost, since a correction that hides its own residue is worse than the
     error it fixes. Integers throughout. */
  function counterSamples(perSecond, I, horizon, resetAt) {
    var out = [], t;
    for (t = 0; t <= horizon; t += I) {
      var since = (resetAt > 0 && t >= resetAt) ? t - resetAt : t;
      out.push([t, since * perSecond]);
    }
    return out;
  }
  function naiveRates(samples) {
    var out = [], i;
    for (i = 1; i < samples.length; i += 1) {
      out.push(R(BigInt(samples[i][1] - samples[i - 1][1]), BigInt(samples[i][0] - samples[i - 1][0])));
    }
    return out;
  }
  function correctedRates(samples) {
    var out = [], i;
    for (i = 1; i < samples.length; i += 1) {
      var d = samples[i][1] - samples[i - 1][1];
      if (d < 0) d = samples[i][1];          /* a decrease is a restart from zero */
      out.push(R(BigInt(d), BigInt(samples[i][0] - samples[i - 1][0])));
    }
    return out;
  }
  /* The interval in which the counter went backwards, or -1. */
  function resetInterval(samples) {
    for (var i = 1; i < samples.length; i += 1) if (samples[i][1] < samples[i - 1][1]) return i;
    return -1;
  }
  /* The increments the correction cannot recover: those between the last read
     before the restart and the restart itself. */
  function lostIncrements(perSecond, I, resetAt) {
    if (resetAt <= 0) return 0;
    return perSecond * (resetAt - Math.floor(resetAt / I) * I);
  }

  /* ================================================ L6: sampling rare events

     The capture probability is atLeastOne(s, k) above -- the same function the
     load test and the alert use. What is local to this lesson is what sampling
     does to a MEAN once the rate stops being uniform.

     A population is value:count runs. Sampling keeps a fraction sHead of the
     requests at or below a threshold and sTail of those above it. The expected
     sampled multiset therefore holds rate_i * count_i of each value, and:

       the naive mean divides the sampled total by the sampled count;
       the reweighted mean divides each sampled item by its own inclusion
       probability first -- Horvitz-Thompson -- and recovers the true mean.

     Both are computed here from the same runs, exactly, so the page shows the
     distortion and the correction rather than asserting either. */
  function runsFromText(text) {
    var parts = String(text).split(/[,;\s]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var m = /^([0-9]+):([0-9]+)$/.exec(s);
      if (!m) return null;
      if (Number(m[2]) <= 0) return null;
      out.push([Number(m[1]), Number(m[2])]);
    }
    return out.length ? out.sort(function (a, b) { return a[0] - b[0]; }) : null;
  }
  function runRate(value, threshold, sHead, sTail) {
    return value > threshold ? sTail : sHead;
  }
  function trueMean(runs) {
    var num = R(0n, 1n), den = R(0n, 1n), i;
    for (i = 0; i < runs.length; i += 1) {
      num = Radd(num, R(BigInt(runs[i][0]) * BigInt(runs[i][1]), 1n));
      den = Radd(den, R(BigInt(runs[i][1]), 1n));
    }
    return Rzero(den) ? R(0n, 1n) : Rdiv(num, den);
  }
  function sampledMean(runs, threshold, sHead, sTail) {
    var num = R(0n, 1n), den = R(0n, 1n), i;
    for (i = 0; i < runs.length; i += 1) {
      var rate = runRate(runs[i][0], threshold, sHead, sTail);
      var kept = Rmul(rate, R(BigInt(runs[i][1]), 1n));
      num = Radd(num, Rmul(kept, R(BigInt(runs[i][0]), 1n)));
      den = Radd(den, kept);
    }
    return Rzero(den) ? R(0n, 1n) : Rdiv(num, den);
  }
  function reweightedMean(runs, threshold, sHead, sTail) {
    var num = R(0n, 1n), den = R(0n, 1n), i;
    for (i = 0; i < runs.length; i += 1) {
      var rate = runRate(runs[i][0], threshold, sHead, sTail);
      if (Rzero(rate)) continue;                 /* never sampled, never estimable */
      var kept = Rmul(rate, R(BigInt(runs[i][1]), 1n));
      var weight = Rdiv(kept, rate);             /* each item counted 1/rate times */
      num = Radd(num, Rmul(weight, R(BigInt(runs[i][0]), 1n)));
      den = Radd(den, weight);
    }
    return Rzero(den) ? R(0n, 1n) : Rdiv(num, den);
  }
  function slowCount(runs, threshold) {
    var c = 0;
    for (var i = 0; i < runs.length; i += 1) if (runs[i][0] > threshold) c += runs[i][1];
    return c;
  }

  /* ==================================================== L7: metric cardinality

     A label is not a field, it is a multiplier: the series count is the
     product of the label cardinalities, and the storage is series x samples x
     bytes. Everything here is integer, so the only interesting question is how
     fast the product grows, which is the lesson. */
  function seriesCount(cards) {
    var p = 1n;
    for (var i = 0; i < cards.length; i += 1) p *= BigInt(cards[i]);
    return p;
  }
  function samplesPerDay(scrapeSeconds) {
    return R(86400n, BigInt(scrapeSeconds));
  }
  function bytesPerDay(series, scrapeSeconds, bytesPerSample) {
    return Rmul(Rmul(R(series, 1n), samplesPerDay(scrapeSeconds)), R(BigInt(bytesPerSample), 1n));
  }
  /* Decimal gigabytes, stated: 1 GB = 10^9 B, the unit a bill is quoted in. */
  function gigabytes(bytes) { return Rdiv(bytes, R(1000000000n, 1n)); }

  /* ================================================= L9: the error budget

     99.9% of a 30-day window is exactly 43.2 minutes. A burn rate b is a
     multiple of the rate that would consume exactly the whole budget over
     exactly the period, so a window of w minutes at burn b spends b*w/period
     of it, and the budget runs out after period/b.

     Minutes throughout, exactly. 43.2 is 216/5. */
  function periodMinutes(days) { return R(BigInt(days) * 1440n, 1n); }
  function budgetMinutes(objective, days) {
    return Rmul(Rsub(R(1n, 1n), objective), periodMinutes(days));
  }
  function burnFraction(b, windowMinutes, days) {
    return Rdiv(Rmul(b, windowMinutes), periodMinutes(days));
  }
  function budgetSpentMinutes(b, windowMinutes, days, objective) {
    return Rmul(burnFraction(b, windowMinutes, days), budgetMinutes(objective, days));
  }
  function exhaustMinutes(b, days) {
    if (Rzero(b)) return null;                      /* a burn of zero never exhausts */
    return Rdiv(periodMinutes(days), b);
  }
  /* The error RATE a burn rate corresponds to: b times the budget's own rate. */
  function burnErrorRate(b, objective) {
    return Rmul(b, Rsub(R(1n, 1n), objective));
  }

  /* ============================================ L10: thresholds and false alarms

     A threshold on a noisy ratio fires when the window's error count reaches k,
     and the probability of that when NOTHING HAS CHANGED is the exact binomial
     upper tail. availKofN(p, k, n) from sysdesign_core is that tail -- it was
     written for "at least k of n replicas up" and the arithmetic is identical,
     which is worth saying rather than writing a second copy of it.

     Pages per week is that probability times the number of windows, and the
     probability of at least one page is atLeastOne -- the sampling formula
     again, on windows instead of requests. */
  function thresholdCount(rate, n) {
    /* The smallest integer error count STRICTLY above the threshold rate. */
    var exact = Rmul(rate, R(BigInt(n), 1n));
    var k = Rceil(exact);
    if (Requ(R(k, 1n), exact)) k += 1n;
    return k < 1n ? 1n : k;
  }
  function falseAlarmProbability(p, k, n) { return availKofN(p, Number(k), n); }
  function windowsPer(minutesInSpan, windowMinutes) {
    return R(BigInt(minutesInSpan), BigInt(windowMinutes));
  }
  function expectedPages(q, windows) { return Rmul(q, windows); }
  function binomialTerm(p, j, n) {
    return Rmul(R(comb(n, j), 1n), Rmul(Rpow(p, j), Rpow(Rsub(R(1n, 1n), p), n - j)));
  }
  /* The whole distribution, by the ratio between neighbouring terms:
     P(j+1)/P(j) = (n-j)/(j+1) * p/(1-p). Exact, and one pass instead of one
     binomial coefficient per term -- which matters because the page draws the
     distribution AND tabulates every threshold's tail, and availKofN would be
     recomputed from scratch for each. The suffix sums of this array are those
     tails, and scripts/mathcheck.js asserts they equal availKofN term for
     term, so the cheap path and the shared one cannot drift apart. */
  function binomialPmf(p, n) {
    var one = R(1n, 1n), q = Rsub(one, p);
    if (Rzero(q)) return null;                      /* p = 1: every trial fires */
    var ratio = Rdiv(p, q), term = Rpow(q, n), out = [term], j;
    for (j = 0; j < n; j += 1) {
      term = Rmul(term, Rmul(R(BigInt(n - j), BigInt(j + 1)), ratio));
      out.push(term);
    }
    return out;
  }
  /* P(X >= k) for every k at once, as suffix sums. Index k is the tail at k. */
  function pmfUpperTails(pmf) {
    var out = new Array(pmf.length), s = R(0n, 1n), j;
    for (j = pmf.length - 1; j >= 0; j -= 1) { s = Radd(s, pmf[j]); out[j] = s; }
    return out;
  }
"""

_CORE_JS = (RATIONAL_JS + BIGINT_JS + RCEIL_JS + PERCENTILE_JS + AVAIL_JS
            + STREAM_JS + APPROX_JS + MEASURE_JS)


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the path uses, so a reader
# moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _js_string(text):
    """A JS string literal for a preset the reader can then edit.

    json.dumps output is valid JS and the escape makes "</script>" structurally
    impossible, the same argument common.cfg_literal makes for its payloads.
    """
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


# The objectives a selector offers, as exact fractions. A percentage never
# enters the arithmetic; the option VALUE is the fraction itself, so the page
# computes from 999/1000 and prints 99.9% rather than the other way round.
_OBJECTIVES = [
    ("99/100", "99% &mdash; two nines"),
    ("995/1000", "99.5%"),
    ("999/1000", "99.9% &mdash; three nines"),
    ("9995/10000", "99.95%"),
    ("9999/10000", "99.99% &mdash; four nines"),
]


# ---------------------------------------------------------------------------
# L1 - sli
# ---------------------------------------------------------------------------


def _sli(cfg):
    window = int(cfg.get("window", 1000))
    observed = int(cfg.get("observed_tenthousandths", 9995))
    objective = str(cfg.get("objective", "999/1000"))

    markup = (
        _toolbar(
            "An SLI and its error bar",
            "good &divide; total over a window, plus or minus what the window can resolve",
            [("cyan", "the measurement"), ("amber", "&plusmn; one standard error"), ("green", "the objective")],
        )
        + _stage(_svg("slBar", "0 0 660 170", "The measured ratio drawn with its error bar against the objective line."))
        + _table("slTable")
        + _banner("slStatus")
    )
    controls = (
        _range("slN", "Requests in the window", 100, 20000, window, 100)
        + _range("slObs", "Measured success ratio (ten-thousandths)", 9900, 10000, observed, 1)
        + _select("slObj", "The objective", _OBJECTIVES, objective)
        + _kpis(
            [
                ("Measured SLI", "slP"),
                ("Variance p(1&minus;p)/n, exact", "slVar"),
                ("Standard error (rounded)", "slSe"),
                ("Gap to the objective", "slGap"),
                ("Gap, in standard errors", "slSigma"),
                ("Window needed to resolve it", "slNeed"),
            ]
        )
        + _hint(
            "slHint",
            "The variance is an exact fraction and so is the window size this page solves for: "
            "p(1&minus;p)/n &le; w&sup2; needs no square root at all. Only the error bar itself is "
            "rounded, because it is a root, and it is the one rounded figure on this course.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('slN'), obsS = document.getElementById('slObs');
  var objSel = document.getElementById('slObj');
  var bar = document.getElementById('slBar'), table = document.getElementById('slTable');
  var status = document.getElementById('slStatus');

  /* An SLI is good divided by total, so the only ratios a window of n can
     produce are the n + 1 fractions with denominator n. A ratio between two of
     them was never an observation, and saying which two it sits between is the
     same resolution limit the error bar measures, arrived at by counting. */
  function reachable(p, n) {
    var good = Rmul(p, R(BigInt(n), 1n));
    if (Rint(good)) return '';
    var lo = sliRatio(Rfloor(good), n), hi = sliRatio(Rceil(good), n);
    return ' <span class="tone-muted">And strictly, ' + Rpct(p, 3) + ' of ' + group(BigInt(n))
      + ' requests is ' + Rfixed(good, 1) + ' successful requests, which no window can return. The '
      + 'nearest ratios this window can actually produce are ' + Rfloor(good) + '/' + n + ' = '
      + Rpct(lo, 3) + ' and ' + Rceil(good) + '/' + n + ' = ' + Rpct(hi, 3)
      + ' &mdash; the same resolution limit, counted '
      + 'rather than estimated.</span>';
  }

  function redraw() {
    var n = +nS.value, obs = +obsS.value;
    var p = R(BigInt(obs), 10000n), objective = Rparse(objSel.value);
    document.getElementById('slNOut').textContent = group(BigInt(n)) + ' requests';
    document.getElementById('slObsOut').textContent = Rpct(p, 2);

    var variance = sliVariance(p, n);
    var se = sliSeApprox(p, n);
    var gap = Rsub(p, objective);
    var sigmas = sigmasApprox(p, objective, n);
    var half = Rdiv(Rabs(gap), R(2n, 1n));
    var need = Rzero(gap) ? 0 : sampleSizeForWidth(p, half);
    var closed = Rzero(gap) ? 0n : sampleSizeClosed(p, half);

    document.getElementById('slP').textContent = Rpct(p, 3) + ' = ' + Rtext(p);
    document.getElementById('slVar').textContent = Rtext(variance);
    document.getElementById('slSe').textContent = (se * 100).toFixed(4) + '% (rounded)';
    document.getElementById('slGap').textContent = (Rcmp(gap, R(0n, 1n)) >= 0 ? '+' : '') + Rpct(gap, 4);
    var clean = Requ(p, R(1n, 1n));
    document.getElementById('slSigma').innerHTML = clean ? 'none &mdash; the error bar is zero at 100%'
      : (Rzero(gap) ? 'none &mdash; it is the objective' : sigmas.toFixed(2) + ' SE');
    document.getElementById('slNeed').innerHTML = clean ? '&mdash;'
      : (need ? group(BigInt(need)) + ' requests' : '&mdash;');

    var rows = '', ladder = [100, 300, 1000, 3000, 10000, 30000, 100000], i;
    if (ladder.indexOf(n) < 0) { ladder.push(n); ladder.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < ladder.length; i += 1) {
      var m = ladder[i], v = sliVariance(p, m), s = sliSeApprox(p, m);
      rows += '<tr><td class="' + (m === n ? 'tone-amber' : '') + '">' + group(BigInt(m)) + '</td><td>'
        + Rtext(v) + '</td><td>' + (s * 100).toFixed(4) + '%</td><td>'
        + (Rpct(Rsub(p, R(BigInt(Math.round(s * 1000000)), 1000000n)), 3)) + ' &ndash; '
        + (Rpct(Radd(p, R(BigInt(Math.round(s * 1000000)), 1000000n)), 3)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>window n</th><th>p(1&minus;p)/n, exact</th>'
      + '<th>standard error</th><th>p &plusmn; one standard error</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4" class="small-copy">Column two is exact. Columns three and four are '
      + 'its square root and so are rounded &mdash; standardErrorApprox, the only rounding on this page.'
      + '</td></tr></tfoot>';

    /* The drawing: the measured ratio, its error bar, and the objective, on an
       axis that spans the interesting range rather than 0 to 1. */
    var lo = Rplot(objective) - 6 * se - 0.0008, hi = Rplot(p) + 6 * se + 0.0008;
    if (Rplot(p) < lo) lo = Rplot(p) - 6 * se - 0.0008;
    if (Rplot(objective) > hi) hi = Rplot(objective) + 6 * se + 0.0008;
    var span = (hi - lo) || 1;
    function px(v) { return 24 + ((v - lo) / span) * 612; }
    var px1 = px(Rplot(p) - se), px2 = px(Rplot(p) + se), pxm = px(Rplot(p)), pxo = px(Rplot(objective));
    var s2 = '<line x1="24" y1="104" x2="636" y2="104" stroke="var(--line-strong)" stroke-width="1" />'
      + '<rect x="' + Math.min(px1, px2) + '" y="60" width="' + Math.max(2, Math.abs(px2 - px1))
      + '" height="28" rx="3" fill="var(--amber)" opacity="0.35" />'
      + '<line x1="' + px1 + '" y1="54" x2="' + px1 + '" y2="94" stroke="var(--amber)" stroke-width="2" />'
      + '<line x1="' + px2 + '" y1="54" x2="' + px2 + '" y2="94" stroke="var(--amber)" stroke-width="2" />'
      + '<line x1="' + pxm + '" y1="44" x2="' + pxm + '" y2="104" stroke="var(--cyan)" stroke-width="3" />'
      + '<text x="' + Math.min(pxm + 6, 470) + '" y="40" font-size="11" fill="var(--cyan)" font-weight="700">measured '
      + Rpct(p, 3) + '</text>'
      + '<line x1="' + pxo + '" y1="44" x2="' + pxo + '" y2="126" stroke="var(--green)" stroke-width="2" stroke-dasharray="5 4" />'
      + '<text x="' + Math.min(pxo + 6, 470) + '" y="122" font-size="11" fill="var(--green)">objective '
      + Rpct(objective, 3) + '</text>'
      + '<text x="24" y="152" font-size="10" fill="var(--muted)">' + (lo * 100).toFixed(3) + '%</text>'
      + '<text x="636" y="152" text-anchor="end" font-size="10" fill="var(--muted)">' + (hi * 100).toFixed(3) + '%</text>'
      + '<text x="24" y="20" font-size="11" fill="var(--muted)">the amber band is one standard error either side of '
      + 'the measurement, on ' + group(BigInt(n)) + ' requests</text>';
    bar.innerHTML = s2;

    var covers = sigmas <= 1;
    var above = Rcmp(p, objective) >= 0;
    if (clean) {
      var bound = rateForTargetSearch(n, R(95n, 100n), 10000);
      status.innerHTML = '<strong>' + group(BigInt(n)) + ' requests and not one failure</strong> puts the '
        + 'estimate on the boundary, where p(1&minus;p)/n is <strong>exactly zero</strong> and the error '
        + 'bar vanishes. That is the formula reporting that it does not apply here, not a measurement of '
        + 'certainty. What a clean window does support is an upper bound, and it comes from the sampling '
        + 'lesson\'s own formula read backwards: the largest failure rate that would still have let '
        + group(BigInt(n)) + ' requests come back clean 5% of the time is <strong>' + Rtext(bound) + ' = '
        + Rpct(bound, 4) + '</strong>. That is the exact form of the rule of three &mdash; the familiar '
        + '3/n is ' + (3 / n).toFixed(6) + ' &mdash; and it is the honest sentence to write in the review: '
        + 'not "we met ' + Rpct(objective, 3) + '", but "nothing failed, and the rate is under '
        + Rpct(bound, 3) + ' with 95% confidence".';
      return;
    }
    status.innerHTML = '<strong>' + Rpct(p, 3) + ' on ' + group(BigInt(n)) + ' requests</strong> carries a standard '
      + 'error of <strong>' + (se * 100).toFixed(4) + '%</strong>. The objective is ' + Rpct(objective, 3)
      + ', which is ' + (Rzero(gap) ? 'exactly the measurement' : sigmas.toFixed(2) + ' standard errors '
        + (above ? 'below' : 'above') + ' it') + '. '
      + (covers
          ? '<span class="tone-red">That is inside the noise.</span> A window this short cannot tell these two '
            + 'ratios apart, so ' + Rpct(p, 3) + ' here is not evidence of ' + (above ? 'meeting' : 'missing')
            + ' ' + Rpct(objective, 3) + '. To separate them by two standard errors you need <strong>'
            + group(BigInt(need)) + ' requests</strong> &mdash; the exact solution of p(1&minus;p)/n &le; ('
            + Rtext(half) + ')&sup2;, which the search and the closed form ceil(p(1&minus;p)/w&sup2;) = '
            + group(closed) + ' both give.'
          : 'That gap is <span class="tone-green">larger than the noise</span>: at ' + group(BigInt(n))
            + ' requests the measurement resolves it. The window at which the gap is exactly two standard '
            + 'errors is ' + group(BigInt(need)) + ' requests.')
      + ' The variance ' + Rtext(variance) + ' is exact; its square root is not, and '
      + '<span class="tone-amber">every figure derived from the error bar on this page is rounded</span>.'
      + reachable(p, n);
  }

  [nS, obsS].forEach(function (el) { el.addEventListener('input', redraw); });
  objSel.addEventListener('change', redraw);
  nS.value = """ + str(window) + r"""; obsS.value = """ + str(observed) + r""";
  objSel.value = '""" + objective + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="An SLI is a ratio with an error bar",
        subtitle="What a window of n requests can and cannot tell you about a ratio",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the window and what it measured"),
        panel_intro=cfg.get(
            "panel_intro",
            "The variance is exact and so is the window size solved for. The error bar is a "
            "square root, so it rounds, and the page says so wherever it appears.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - aggregate
# ---------------------------------------------------------------------------

# The preset is the one the course's how_to asks for: a fleet where the mean of
# the per-host p99s lands BELOW the fleet median. Two small hosts serving five
# fast requests each and one large host serving ninety slow ones does it, and
# it is not a contrivance -- it is a canary pair and a production pool.
_HOST_A = "8, 9, 10, 11, 12"
_HOST_B = "10, 11, 12, 13, 14"
_HOST_C = "150:20, 180:20, 220:20, 260:15, 320:10, 400:5"


def _aggregate(cfg):
    host_a = str(cfg.get("host_a", _HOST_A))
    host_b = str(cfg.get("host_b", _HOST_B))
    host_c = str(cfg.get("host_c", _HOST_C))
    q = int(cfg.get("q", 99))

    markup = (
        _toolbar(
            "Percentiles do not average",
            "the p99 of the merged sample, against the mean of the per-host p99s",
            [("cyan", "the merged fleet"), ("amber", "fleet p99"), ("red", "mean of the p99s")],
        )
        + _stage(_svg("agPlot", "0 0 660 210", "Each host's sample as ticks with its own p99, then the merged sample with the fleet p99 and the mean of the p99s marked."))
        + _table("agTable")
        + _banner("agStatus")
    )
    controls = (
        _text("agA", "web-1 (ms; v:count repeats a value)", host_a)
        + _text("agB", "web-2", host_b)
        + _text("agC", "web-3", host_c)
        + _range("agQ", "Percentile", 50, 100, q)
        + _kpis(
            [
                ("Fleet p99, merged sample", "agFleet"),
                ("Mean of the per-host p99s", "agMean"),
                ("The two differ by", "agDiff"),
                ("Fleet median", "agMedian"),
                ("Largest per-host p99", "agMax"),
                ("Requests in the fleet", "agN"),
            ]
        )
        + _hint(
            "agHint",
            "Both numbers come from the same nearest-rank definition and the same requests. The "
            "fleet figure applies it once to every request the fleet served; the other applies it "
            "per host and then averages the answers, which is an average of ranks and is not a "
            "percentile of anything.",
        )
    )

    script = _CORE_JS + r"""
  var inA = document.getElementById('agA'), inB = document.getElementById('agB'), inC = document.getElementById('agC');
  var qS = document.getElementById('agQ');
  var plot = document.getElementById('agPlot'), table = document.getElementById('agTable');
  var status = document.getElementById('agStatus');
  var NAMES = ['web-1', 'web-2', 'web-3'];

  function redraw() {
    var q = +qS.value;
    document.getElementById('agQOut').textContent = 'p' + q;
    var lists = [parseRuns(inA.value), parseRuns(inB.value), parseRuns(inC.value)];
    var live = [], names = [], i;
    for (i = 0; i < lists.length; i += 1) if (lists[i]) { live.push(lists[i]); names.push(NAMES[i]); }
    if (!live.length) {
      plot.innerHTML = '';
      table.innerHTML = '';
      ['agFleet', 'agMean', 'agDiff', 'agMedian', 'agMax', 'agN'].forEach(function (id) {
        document.getElementById(id).innerHTML = '&mdash;';
      });
      status.innerHTML = '<span class="tone-red">No samples.</span> Type request times in milliseconds, '
        + 'separated by commas; <span class="tt">150:20</span> means twenty requests of 150 ms.';
      return;
    }

    var qr = R(BigInt(q), 100n);
    var merged = mergeSamples(live);
    var perHost = hostPercentiles(live, qr);
    var mean = meanOfPercentiles(perHost);
    var fleet = fleetPercentile(live, qr);
    var median = fleetPercentile(live, R(1n, 2n));
    var biggest = maxOf(perHost), smallest = minOf(perHost);
    var busiest = 0;
    for (i = 0; i < live.length; i += 1) if (live[i].length > busiest) busiest = live[i].length;
    var fleetR = R(BigInt(fleet), 1n);
    var diff = Rsub(fleetR, mean);

    document.getElementById('agFleet').textContent = fleet + ' ms';
    document.getElementById('agMean').innerHTML = Rtext(mean) + ' = ' + Rfixed(mean, 2) + ' ms';
    document.getElementById('agDiff').innerHTML = Rfixed(diff, 2) + ' ms'
      + (Rzero(mean) ? '' : ' (&times;' + Rfixed(Rdiv(fleetR, mean), 2) + ')');
    document.getElementById('agMedian').textContent = median + ' ms';
    document.getElementById('agMax').textContent = biggest + ' ms';
    document.getElementById('agN').textContent = group(BigInt(merged.length)) + ' requests';

    var rows = '';
    for (i = 0; i < live.length; i += 1) {
      var n = live[i].length, rank = percentileRank(n, qr);
      rows += '<tr><td>' + names[i] + '</td><td>' + n + '</td><td>&lceil;' + q + '/100 &times; ' + n
        + '&rceil; = ' + rank + '</td><td class="tone-cyan">' + perHost[i] + ' ms</td><td>'
        + Rfixed(R(BigInt(n), BigInt(merged.length)), 3) + '</td></tr>';
    }
    rows += '<tr><td class="tone-red">mean of those ' + live.length + '</td><td>&mdash;</td><td>'
      + 'an average of ' + live.length + ' ranks</td><td class="tone-red">' + Rfixed(mean, 2)
      + ' ms</td><td>&mdash;</td></tr>';
    rows += '<tr><td class="tone-amber">fleet, merged</td><td>' + merged.length + '</td><td>&lceil;' + q
      + '/100 &times; ' + merged.length + '&rceil; = ' + percentileRank(merged.length, qr)
      + '</td><td class="tone-amber">' + fleet + ' ms</td><td>1.000</td></tr>';
    table.innerHTML = '<thead><tr><th>sample</th><th>requests</th><th>rank selected</th><th>p' + q
      + '</th><th>share of the fleet</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">Every row in the p' + q + ' column is nearest '
      + 'rank &mdash; the same percentile() the latency course prints. Only the row in red is an '
      + 'average, and it is the only row that is not a request time anyone waited.</td></tr></tfoot>';

    var lo = merged[0], hi = merged[merged.length - 1], span = (hi - lo) || 1;
    function px(v) { return 26 + ((v - lo) / span) * 604; }
    var s = '', y = 34;
    for (i = 0; i < live.length; i += 1) {
      var j;
      s += '<text x="0" y="' + (y + 4) + '" font-size="10" fill="var(--muted)">' + names[i] + '</text>';
      for (j = 0; j < live[i].length; j += 1) {
        s += '<line x1="' + px(live[i][j]) + '" y1="' + (y - 8) + '" x2="' + px(live[i][j]) + '" y2="'
          + (y + 8) + '" stroke="var(--cyan)" stroke-width="1.5" opacity="0.55" />';
      }
      s += '<circle cx="' + px(perHost[i]) + '" cy="' + y + '" r="4" fill="var(--cyan)" />'
        + '<text x="' + Math.min(px(perHost[i]) + 7, 600) + '" y="' + (y - 9) + '" font-size="9" '
        + 'fill="var(--cyan)">p' + q + ' ' + perHost[i] + '</text>';
      y += 34;
    }
    y += 8;
    for (i = 0; i < merged.length; i += 1) {
      s += '<line x1="' + px(merged[i]) + '" y1="' + (y - 10) + '" x2="' + px(merged[i]) + '" y2="'
        + (y + 10) + '" stroke="var(--muted)" stroke-width="1.5" opacity="0.5" />';
    }
    s += '<text x="0" y="' + (y + 4) + '" font-size="10" fill="var(--muted)">fleet</text>'
      + '<line x1="' + px(fleet) + '" y1="' + (y - 16) + '" x2="' + px(fleet) + '" y2="' + (y + 16)
      + '" stroke="var(--amber)" stroke-width="3" />'
      + '<text x="' + Math.max(0, Math.min(px(fleet) - 60, 560)) + '" y="' + (y + 32) + '" font-size="10" '
      + 'fill="var(--amber)" font-weight="700">fleet p' + q + ' = ' + fleet + ' ms</text>'
      + '<line x1="' + px(Rplot(mean)) + '" y1="' + (y - 16) + '" x2="' + px(Rplot(mean)) + '" y2="' + (y + 16)
      + '" stroke="var(--red)" stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + Math.max(0, Math.min(px(Rplot(mean)) + 6, 460)) + '" y="' + (y - 20) + '" font-size="10" '
      + 'fill="var(--red)">mean of the p' + q + 's = ' + Rfixed(mean, 1) + ' ms</text>'
      + '<line x1="' + px(median) + '" y1="' + (y - 16) + '" x2="' + px(median) + '" y2="' + (y + 16)
      + '" stroke="var(--green)" stroke-width="2" />'
      + '<text x="' + Math.max(0, Math.min(px(median) - 30, 520)) + '" y="' + (y + 46) + '" font-size="10" '
      + 'fill="var(--green)">fleet median ' + median + ' ms</text>'
      + '<text x="0" y="14" font-size="11" fill="var(--muted)">each tick is one request; the bottom row is '
      + 'every request the fleet served</text>';
    plot.innerHTML = s;

    var belowMedian = Rcmp(mean, R(BigInt(median), 1n)) < 0;
    status.innerHTML = 'The fleet p' + q + ' is <strong>' + fleet + ' ms</strong> &mdash; rank '
      + percentileRank(merged.length, qr) + ' of the ' + group(BigInt(merged.length))
      + ' requests the fleet actually served. Averaging the ' + live.length + ' per-host p' + q
      + 's gives <strong>' + Rfixed(mean, 2) + ' ms</strong>, which is '
      + (Rzero(diff) ? 'the same number here, on this data and by coincidence'
          : Rfixed(Rabs(diff), 2) + ' ms ' + (Rcmp(diff, R(0n, 1n)) > 0 ? 'BELOW' : 'above') + ' it')
      + '. '
      + (belowMedian
          ? '<span class="tone-red">It is also below the fleet median of ' + median + ' ms</span> &mdash; '
            + 'a number reported as a 99th percentile that more than half the fleet\'s requests were '
            + 'slower than. That is what averaging ranks does: the two small hosts contribute an equal '
            + 'vote and ' + Math.round(100 * busiest / merged.length) + '% of the '
            + 'requests are on one host.'
          : 'The pooled figure can never exceed the largest per-host p' + q + ' (' + biggest
            + ' ms) or fall below the smallest (' + smallest + ' ms), because the ranks add. The mean '
            + 'has no such relation to anything; move a small host and watch it move.')
      + ' Give one host more requests and the fleet figure follows the requests; the mean does not.';
  }

  [inA, inB, inC].forEach(function (el) { el.addEventListener('input', redraw); });
  qS.addEventListener('input', redraw);
  inA.value = """ + _js_string(host_a) + r"""; inB.value = """ + _js_string(host_b) + r""";
  inC.value = """ + _js_string(host_c) + r"""; qS.value = """ + str(q) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The fleet p99, and the number that is not one",
        subtitle="Two answers from one definition and one set of requests",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the per-host samples"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both figures are recomputed from the requests you type. The fleet percentile merges "
            "them first; the mean averages the per-host answers afterwards.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - histogram
# ---------------------------------------------------------------------------

# 25 ms doubling gives an edge at exactly 100 ms, so the lesson's sentence --
# "a p99 reported as 100 ms with r = 2 is somewhere in [100, 200)" -- is the
# bucket this preset lands in rather than a number chosen to sound round.
_HIST_SAMPLE = "30:40, 45:25, 60:15, 85:10, 120:6, 137:3, 400:1"

_RATIOS = [
    ("2/1", "2 &mdash; each bucket twice the last"),
    ("3/2", "3/2"),
    ("5/4", "5/4"),
    ("10/1", "10 &mdash; a decade a bucket"),
]


def _histogram(cfg):
    base = int(cfg.get("base", 25))
    ratio = str(cfg.get("ratio", "2/1"))
    buckets = int(cfg.get("buckets", 6))
    sample = str(cfg.get("sample", _HIST_SAMPLE))
    q = int(cfg.get("q", 99))

    markup = (
        _toolbar(
            "A histogram knows its buckets, not its requests",
            "the containing bucket, its width, and the factor the answer is known to",
            [("cyan", "bucket counts"), ("amber", "the reported bucket"), ("purple", "the exact percentile")],
        )
        + _stage(_svg("hgPlot", "0 0 660 200", "The bucket counts as bars, with the bucket the percentile falls in highlighted and the exact value marked inside it."))
        + _table("hgTable")
        + _banner("hgStatus")
    )
    controls = (
        _text("hgSample", "The requests (ms; v:count repeats a value)", sample)
        + _range("hgBase", "First bucket edge (ms)", 5, 100, base, 5)
        + _select("hgRatio", "Bucket ratio r", _RATIOS, ratio)
        + _range("hgCount", "Buckets", 3, 10, buckets)
        + _range("hgQ", "Percentile", 50, 100, q)
        + _kpis(
            [
                ("Exact percentile, from the sample", "hgExact"),
                ("What the histogram can report", "hgBucket"),
                ("Bucket width", "hgWidth"),
                ("Relative error, r &minus; 1", "hgRel"),
                ("Requests in that bucket", "hgIn"),
                ("Requests past the last edge", "hgOver"),
            ]
        )
        + _hint(
            "hgHint",
            "Both answers use the same rank. The exact one reads the request at that rank; the "
            "histogram only knows which bucket the rank fell in, so its answer is an interval. "
            "At ratio r every bucket is r times its own lower edge wide, which is why the error is "
            "a constant percentage rather than a constant number of milliseconds.",
        )
    )

    script = _CORE_JS + r"""
  var sampleIn = document.getElementById('hgSample'), baseS = document.getElementById('hgBase');
  var ratioSel = document.getElementById('hgRatio'), countS = document.getElementById('hgCount');
  var qS = document.getElementById('hgQ');
  var plot = document.getElementById('hgPlot'), table = document.getElementById('hgTable');
  var status = document.getElementById('hgStatus');

  function redraw() {
    var base = +baseS.value, count = +countS.value, q = +qS.value;
    var ratio = Rparse(ratioSel.value);
    document.getElementById('hgBaseOut').textContent = base + ' ms';
    document.getElementById('hgCountOut').textContent = count + ' buckets';
    document.getElementById('hgQOut').textContent = 'p' + q;

    var sorted = parseRuns(sampleIn.value);
    if (!sorted) {
      plot.innerHTML = '';
      table.innerHTML = '';
      ['hgExact', 'hgBucket', 'hgWidth', 'hgRel', 'hgIn', 'hgOver'].forEach(function (id) {
        document.getElementById(id).innerHTML = '&mdash;';
      });
      status.innerHTML = '<span class="tone-red">No requests in that sample.</span> Type times in '
        + 'milliseconds; <span class="tt">120:6</span> means six requests of 120 ms.';
      return;
    }

    var qr = R(BigInt(q), 100n);
    var edges = bucketEdges(base, ratio, count);
    var counts = bucketCounts(sorted, edges);
    var exact = percentile(sorted, qr);
    var rank = percentileRank(sorted.length, qr);
    var reported = histogramBucket(sorted, edges, qr);
    var inside = reported >= 0 && reported < counts.inside.length;
    var lo = inside ? edges[reported] : null, hi = inside ? edges[reported + 1] : null;
    var width = inside ? bucketWidth(edges, reported) : null;
    var rel = bucketRelative(ratio);

    document.getElementById('hgExact').textContent = exact + ' ms (rank ' + rank + ' of ' + sorted.length + ')';
    document.getElementById('hgBucket').innerHTML = inside
      ? '[' + Rfixed(lo, 0) + ', ' + Rfixed(hi, 0) + ') ms'
      : (reported < 0 ? 'under ' + Rfixed(edges[0], 0) + ' ms' : '&ge; ' + Rfixed(edges[edges.length - 1], 0) + ' ms, open-ended');
    document.getElementById('hgWidth').innerHTML = inside ? Rfixed(width, 1) + ' ms' : 'unbounded';
    document.getElementById('hgRel').innerHTML = Rpct(rel, 1) + ' of the lower edge';
    document.getElementById('hgIn').innerHTML = inside ? counts.inside[reported] + ' of ' + sorted.length : '&mdash;';
    document.getElementById('hgOver').textContent = counts.over + ' of ' + sorted.length;

    var rows = '', cum = counts.under, i;
    if (counts.under) {
      rows += '<tr><td>under ' + Rfixed(edges[0], 0) + '</td><td>' + counts.under + '</td><td>'
        + cum + '</td><td>' + Rfixed(R(BigInt(cum), BigInt(sorted.length)), 3) + '</td><td></td></tr>';
    }
    for (i = 0; i < counts.inside.length; i += 1) {
      cum += counts.inside[i];
      var mark = i === reported ? 'tone-amber' : '';
      rows += '<tr><td class="' + mark + '">[' + Rfixed(edges[i], 0) + ', ' + Rfixed(edges[i + 1], 0)
        + ')</td><td>' + counts.inside[i] + '</td><td>' + cum + '</td><td>'
        + Rfixed(R(BigInt(cum), BigInt(sorted.length)), 3) + '</td><td>'
        + (i === reported ? 'rank ' + rank + ' lands here' : '') + '</td></tr>';
    }
    if (counts.over) {
      cum += counts.over;
      rows += '<tr><td class="tone-red">&ge; ' + Rfixed(edges[edges.length - 1], 0) + ', open</td><td>'
        + counts.over + '</td><td>' + cum + '</td><td>'
        + Rfixed(R(BigInt(cum), BigInt(sorted.length)), 3) + '</td><td>no upper bound at all</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>bucket (ms)</th><th>count</th><th>cumulative</th>'
      + '<th>cumulative share</th><th></th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">Edges are ' + base + ' &times; ('
      + Rtext(ratio) + ')<sup>i</sup>, exact rationals: this bucketing\'s fourth edge is '
      + Rtext(Rmul(R(BigInt(base), 1n), Rpow(ratio, 3))) + ', and at r = 3/2 it would be '
      + Rtext(Rmul(R(BigInt(base), 1n), Rpow(R(3n, 2n), 3))) + ' &mdash; a fraction, not a rounded '
      + 'decimal.</td></tr></tfoot>';

    var wide = 632 / Math.max(1, counts.inside.length + (counts.under ? 1 : 0) + (counts.over ? 1 : 0));
    var top = 1, s = '';
    for (i = 0; i < counts.inside.length; i += 1) if (counts.inside[i] > top) top = counts.inside[i];
    if (counts.over > top) top = counts.over;
    if (counts.under > top) top = counts.under;
    var x = 14, slot = 0;
    function bar(label, n, tone, isReported) {
      var h = Math.max(1, (n / top) * 110);
      var out = '<rect x="' + x + '" y="' + (150 - h) + '" width="' + Math.max(4, wide - 6) + '" height="' + h
        + '" rx="2" fill="var(--' + tone + ')" opacity="' + (isReported ? '0.95' : '0.55') + '" />'
        + '<text x="' + (x + wide / 2 - 3) + '" y="164" text-anchor="middle" font-size="9" fill="var(--muted)">'
        + label + '</text>'
        + '<text x="' + (x + wide / 2 - 3) + '" y="' + (144 - h) + '" text-anchor="middle" font-size="9" '
        + 'fill="var(--' + tone + ')">' + n + '</text>';
      x += wide;
      slot += 1;
      return out;
    }
    if (counts.under) s += bar('&lt;' + Rfixed(edges[0], 0), counts.under, 'muted', false);
    for (i = 0; i < counts.inside.length; i += 1) {
      s += bar(Rfixed(edges[i], 0), counts.inside[i], i === reported ? 'amber' : 'cyan', i === reported);
    }
    if (counts.over) s += bar('&ge;' + Rfixed(edges[edges.length - 1], 0), counts.over, 'red', reported >= counts.inside.length);
    if (inside) {
      var start = 14 + wide * ((counts.under ? 1 : 0) + reported);
      var frac = Rplot(Rdiv(Rsub(R(BigInt(exact), 1n), lo), width));
      var mx = start + Math.max(0, Math.min(1, frac)) * Math.max(4, wide - 6);
      s += '<line x1="' + mx + '" y1="24" x2="' + mx + '" y2="150" stroke="var(--purple)" stroke-width="2" />'
        + '<text x="' + Math.max(0, Math.min(mx - 40, 520)) + '" y="20" font-size="10" fill="var(--purple)" '
        + 'font-weight="700">the exact p' + q + ' is ' + exact + ' ms, in here somewhere</text>';
    }
    s += '<line x1="14" y1="150" x2="646" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="14" y="184" font-size="10" fill="var(--muted)">bucket lower edges; every request inside one '
      + 'bucket is the same request as far as the histogram is concerned</text>';
    plot.innerHTML = s;

    status.innerHTML = inside
      ? 'Rank ' + rank + ' falls in <strong>[' + Rfixed(lo, 0) + ', ' + Rfixed(hi, 0) + ') ms</strong>, so a '
        + 'histogram with these buckets can only report that the p' + q + ' is somewhere in a '
        + '<strong>' + Rfixed(width, 1) + ' ms</strong> window &mdash; a factor of ' + Rtext(ratio)
        + ', which is <strong>' + Rpct(rel, 1) + '</strong> of the lower edge, at every scale. The sample '
        + 'itself says <span class="tone-purple">' + exact + ' ms</span>, and the '
        + counts.inside[reported] + ' request' + (counts.inside[reported] === 1 ? '' : 's') + ' in that bucket '
        + 'are indistinguishable to the histogram. '
        + (counts.over
            ? '<span class="tone-red">' + counts.over + ' request' + (counts.over === 1 ? '' : 's') + ' also '
              + 'landed past the last edge</span>, in the open-ended bucket &mdash; and a percentile that '
              + 'lands there has no upper bound at all, which is the failure mode worth remembering.'
            : 'Nothing overflowed the last edge here, so every percentile this histogram reports is at '
              + 'least bounded.')
      : (reported < 0
          ? 'Rank ' + rank + ' falls below the first edge, so the histogram can say only that the p' + q
            + ' is under ' + Rfixed(edges[0], 0) + ' ms. The sample says ' + exact + ' ms.'
          : '<span class="tone-red">Rank ' + rank + ' falls in the open-ended bucket past '
            + Rfixed(edges[edges.length - 1], 0) + ' ms.</span> The histogram has no upper bound to report '
            + 'and the usual convention prints the last edge, which is not an estimate of anything: the '
            + 'sample says ' + exact + ' ms. Raise the bucket count or the ratio until the tail is covered.');
  }

  [baseS, countS, qS].forEach(function (el) { el.addEventListener('input', redraw); });
  sampleIn.addEventListener('input', redraw);
  ratioSel.addEventListener('change', redraw);
  sampleIn.value = """ + _js_string(sample) + r"""; baseS.value = """ + str(base) + r""";
  countS.value = """ + str(buckets) + r"""; qS.value = """ + str(q) + r""";
  ratioSel.value = '""" + ratio + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A percentile is only as sharp as its bucket",
        subtitle="The interval a histogram can actually report, and the factor it is known to",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the buckets and the sample"),
        panel_intro=cfg.get(
            "panel_intro",
            "The exact percentile and the reported bucket are computed from the same requests and "
            "the same rank. The difference between them is the bucketing, and nothing else.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - omission
# ---------------------------------------------------------------------------


def _omission(cfg):
    requests = int(cfg.get("requests", 100))
    interval = int(cfg.get("interval_ms", 10))
    service = int(cfg.get("service_ms", 2))
    stall = int(cfg.get("stall_ms", 1000))
    q = int(cfg.get("q", 99))

    markup = (
        _toolbar(
            "Coordinated omission",
            "the requests a stalled generator never sent, put back at the times they were due",
            [("cyan", "requests that were sent"), ("red", "the stall"), ("amber", "imputed requests")],
        )
        + _stage(_svg("coPlot", "0 0 660 190", "A timeline of scheduled requests, the stall, and the imputed requests drawn at the times the schedule called for."))
        + _table("coTable")
        + _banner("coStatus")
    )
    controls = (
        _range("coN", "Requests the generator sent", 20, 400, requests, 10)
        + _range("coGap", "Scheduled interval between requests (ms)", 1, 50, interval)
        + _range("coSvc", "Service time when healthy (ms)", 1, 50, service)
        + _range("coStall", "The stall (ms)", 50, 3000, stall, 10)
        + _range("coQ", "Percentile", 50, 100, q)
        + _kpis(
            [
                ("Naive p99, as measured", "coNaive"),
                ("Corrected p99", "coFixed"),
                ("Requests never sent", "coMissing"),
                ("Naive median", "coNaiveMed"),
                ("Corrected median", "coFixedMed"),
                ("Ratio, corrected &divide; naive", "coRatio"),
            ]
        )
        + _hint(
            "coHint",
            "A closed-loop generator sends the next request when the last one returns, so while the "
            "system is stalled it sends nothing and the stall is measured once. The correction puts "
            "back the requests the schedule called for during the stall, each waiting from the "
            "moment it was due until the stall cleared.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('coN'), gapS = document.getElementById('coGap');
  var svcS = document.getElementById('coSvc'), stallS = document.getElementById('coStall');
  var qS = document.getElementById('coQ');
  var plot = document.getElementById('coPlot'), table = document.getElementById('coTable');
  var status = document.getElementById('coStatus');

  function redraw() {
    var n = +nS.value, gap = +gapS.value, svc = +svcS.value, stall = +stallS.value, q = +qS.value;
    document.getElementById('coNOut').textContent = n + ' requests';
    document.getElementById('coGapOut').textContent = 'every ' + gap + ' ms';
    document.getElementById('coSvcOut').textContent = svc + ' ms';
    document.getElementById('coStallOut').textContent = group(BigInt(stall)) + ' ms';
    document.getElementById('coQOut').textContent = 'p' + q;

    var qr = R(BigInt(q), 100n), half = R(1n, 2n);
    var naive = naiveSample(n, svc, stall);
    var imputed = imputedLatencies(gap, stall);
    var fixed = correctedSample(n, gap, svc, stall);
    var naiveP = percentile(naive, qr), fixedP = percentile(fixed, qr);
    var naiveMed = percentile(naive, half), fixedMed = percentile(fixed, half);
    var ratio = naiveP > 0 ? R(BigInt(fixedP), BigInt(naiveP)) : null;

    document.getElementById('coNaive').textContent = naiveP + ' ms (rank ' + percentileRank(naive.length, qr)
      + ' of ' + naive.length + ')';
    document.getElementById('coFixed').textContent = fixedP + ' ms (rank ' + percentileRank(fixed.length, qr)
      + ' of ' + fixed.length + ')';
    document.getElementById('coMissing').textContent = group(BigInt(imputed.length)) + ' requests';
    document.getElementById('coNaiveMed').textContent = naiveMed + ' ms';
    document.getElementById('coFixedMed').textContent = fixedMed + ' ms';
    document.getElementById('coRatio').innerHTML = ratio ? '&times;' + Rfixed(ratio, 1) : '&mdash;';

    var rows = '', probes = [50, 90, 95, 99, 100], i;
    if (probes.indexOf(q) < 0) { probes.push(q); probes.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < probes.length; i += 1) {
      var pr = R(BigInt(probes[i]), 100n);
      var a = percentile(naive, pr), b = percentile(fixed, pr);
      rows += '<tr><td class="' + (probes[i] === q ? 'tone-amber' : '') + '">p' + probes[i] + '</td><td>'
        + a + ' ms</td><td>' + b + ' ms</td><td>' + (a > 0 ? '&times;' + Rfixed(R(BigInt(b), BigInt(a)), 1) : '&mdash;')
        + '</td></tr>';
    }
    rows += '<tr><td>mean</td><td>' + Rfixed(sampleMean(naive), 2) + ' ms</td><td>'
      + Rfixed(sampleMean(fixed), 2) + ' ms</td><td>&times;'
      + Rfixed(Rdiv(sampleMean(fixed), sampleMean(naive)), 1) + '</td></tr>';
    rows += '<tr><td>requests counted</td><td>' + naive.length + '</td><td>' + fixed.length + '</td><td>+'
      + imputed.length + '</td></tr>';
    table.innerHTML = '<thead><tr><th></th><th>as measured</th><th>corrected</th><th>ratio</th></tr></thead>'
      + '<tbody>' + rows + '</tbody><tfoot><tr><td colspan="4" class="small-copy">Both columns are '
      + 'nearest rank on their own sample. The correction does not change a single measured number; '
      + 'it adds the ' + imputed.length + ' requests the schedule called for and the generator did not '
      + 'send, at latencies ' + (imputed.length ? (stall - gap) + ' ms down to ' + imputed[imputed.length - 1]
        + ' ms' : 'none, because the stall is shorter than one interval') + '.</td></tr></tfoot>';

    /* The timeline: scheduled slots across the width, the stall as a block, and
       the imputed requests as the sloping line of waits it hides. */
    var window0 = Math.min(n, 40), span = window0 * gap + stall;
    function px(t) { return 16 + (t / span) * 628; }
    var s = '', i2, before = Math.floor(window0 / 2);
    for (i2 = 0; i2 < before; i2 += 1) {
      s += '<line x1="' + px(i2 * gap) + '" y1="58" x2="' + px(i2 * gap) + '" y2="' + (58 - Math.max(2, svc / 4))
        + '" stroke="var(--cyan)" stroke-width="2" />';
    }
    var t0 = before * gap;
    s += '<rect x="' + px(t0) + '" y="30" width="' + Math.max(2, px(t0 + stall) - px(t0)) + '" height="28" rx="3" '
      + 'fill="var(--red)" opacity="0.55" />'
      + '<text x="' + px(t0) + '" y="24" font-size="10" fill="var(--red)">one request measured ' + group(BigInt(stall))
      + ' ms &mdash; the only thing the generator recorded</text>';
    for (i2 = 0; i2 < imputed.length; i2 += 1) {
      var due = t0 + (i2 + 1) * gap;
      s += '<line x1="' + px(due) + '" y1="' + (100 + 60 * (i2 / Math.max(1, imputed.length))) + '" x2="'
        + px(t0 + stall) + '" y2="' + (100 + 60 * (i2 / Math.max(1, imputed.length)))
        + '" stroke="var(--amber)" stroke-width="1" opacity="0.6" />';
    }
    for (i2 = 0; i2 < before; i2 += 1) {
      s += '<line x1="' + px(t0 + stall + i2 * gap) + '" y1="58" x2="' + px(t0 + stall + i2 * gap) + '" y2="'
        + (58 - Math.max(2, svc / 4)) + '" stroke="var(--cyan)" stroke-width="2" />';
    }
    s += '<line x1="16" y1="58" x2="644" y2="58" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="16" y="14" font-size="11" fill="var(--muted)">one tick per request actually sent, at ' + gap
      + ' ms apart</text>'
      + '<text x="16" y="' + (176) + '" font-size="10" fill="var(--amber)">each amber line is a request the '
      + 'schedule called for and the generator never sent: ' + imputed.length + ' of them, waiting from when '
      + 'they were due until the stall cleared</text>';
    plot.innerHTML = s;

    var hidden = fixedP > naiveP;
    status.innerHTML = 'The generator sent ' + n + ' requests and measured a p' + q + ' of <strong>'
      + naiveP + ' ms</strong>' + (naiveP <= svc ? ' &mdash; the healthy service time, because the one slow '
        + 'request is a single sample and rank ' + percentileRank(naive.length, qr) + ' of ' + naive.length
        + ' does not reach it' : '') + '. During the ' + group(BigInt(stall)) + ' ms stall the schedule called '
      + 'for <strong>' + imputed.length + '</strong> more requests at ' + gap + ' ms apart, and a closed loop '
      + 'sent none of them. Putting them back at the times they were due gives a p' + q + ' of <strong>'
      + fixedP + ' ms</strong>'
      + (hidden
          ? ' &mdash; <span class="tone-red">' + (naiveP > 0 ? Rfixed(ratio, 0) + ' times' : 'far') + ' the '
            + 'measured figure</span>. Every one of those requests was a user waiting; the generator was the '
            + 'only party that did not notice.'
          : ', which here is no worse, because the stall is shorter than one interval and the schedule '
            + 'called for nothing during it.')
      + ' The correction adds no measurement and invents no distribution: it charges the stall once per '
      + 'request that was due inside it, which is what an open-loop generator would have charged.';
  }

  [nS, gapS, svcS, stallS, qS].forEach(function (el) { el.addEventListener('input', redraw); });
  nS.value = """ + str(requests) + r"""; gapS.value = """ + str(interval) + r""";
  svcS.value = """ + str(service) + r"""; stallS.value = """ + str(stall) + r"""; qS.value = """ + str(q) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The requests the load generator never sent",
        subtitle="A stall measured once, and the same stall charged to everyone it delayed",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the schedule and the stall"),
        panel_intro=cfg.get(
            "panel_intro",
            "The naive sample is what the generator recorded. The corrected sample is that same "
            "recording plus the requests the schedule called for while it was blocked.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - scrape
# ---------------------------------------------------------------------------


def _scrape(cfg):
    interval = int(cfg.get("interval_s", 15))
    width = int(cfg.get("spike_s", 3))
    spikes = int(cfg.get("spikes", 12))
    offset = int(cfg.get("offset_s", 0))
    seed = int(cfg.get("seed", 7))
    reset_at = int(cfg.get("reset_s", 152))
    per_second = int(cfg.get("counter_rate", 40))

    markup = (
        _toolbar(
            "What a scrape interval cannot see",
            "min(1, d/I), the longest spike that can hide between two reads, and a counter that restarted",
            [("cyan", "the true signal"), ("amber", "scrape instants"), ("red", "spikes nobody saw")],
        )
        + _stage(_svg("scPlot", "0 0 660 180", "Spikes drawn along a five-minute horizon with the scrape instants over them, the missed ones marked."))
        + _table("scTable")
        + _table("scCounter")
        + _banner("scStatus")
    )
    controls = (
        _range("scI", "Scrape interval I (seconds)", 1, 60, interval)
        + _range("scD", "Spike duration d (seconds)", 1, 60, width)
        + _range("scCount", "Spikes in the five minutes", 1, 30, spikes)
        + _range("scOffset", "Phase of the first scrape (seconds)", 0, 59, offset)
        + _range("scSeed", "Seed for the spike times", 1, 40, seed)
        + _range("scRate", "A counter climbing at (per second)", 1, 200, per_second)
        + _range("scReset", "The process restarts at (seconds, 0 = never)", 0, 299, reset_at)
        + _kpis(
            [
                ("P(catch a spike) = min(1, d/I)", "scProb"),
                ("Longest invisible spike", "scBlind"),
                ("Scrapes in five minutes", "scReads"),
                ("Spikes this run", "scTotal"),
                ("Caught on this run", "scSeen"),
                ("Missed on this run", "scMissed"),
                ("Naive rate across the restart", "scNaive"),
                ("Corrected rate, and what it loses", "scFixed"),
            ]
        )
        + _hint(
            "scHint",
            "The probability is exact and it is a comparison, not a rounding: d/I capped at one. The "
            "run below is one particular set of spike times from a seeded stream, so the fraction it "
            "catches is near the probability and not equal to it &mdash; which is what a single "
            "afternoon of monitoring is.",
        )
    )

    script = _CORE_JS + r"""
  var iS = document.getElementById('scI'), dS = document.getElementById('scD');
  var cS = document.getElementById('scCount'), offS = document.getElementById('scOffset');
  var seedS = document.getElementById('scSeed'), rateS = document.getElementById('scRate');
  var resetS = document.getElementById('scReset');
  var plot = document.getElementById('scPlot'), table = document.getElementById('scTable');
  var counterTable = document.getElementById('scCounter');
  var status = document.getElementById('scStatus');
  var HORIZON = 300;

  function redraw() {
    var I = +iS.value, d = +dS.value, count = +cS.value, off = +offS.value % Math.max(1, I), seed = +seedS.value;
    document.getElementById('scIOut').textContent = 'every ' + I + ' s';
    document.getElementById('scDOut').textContent = d + ' s long';
    document.getElementById('scCountOut').textContent = count + ' spikes';
    document.getElementById('scOffsetOut').textContent = '+' + off + ' s';
    document.getElementById('scSeedOut').textContent = 'seed ' + seed;
    var perSecond = +rateS.value, resetAt = +resetS.value;
    document.getElementById('scRateOut').textContent = '+' + perSecond + '/s';
    document.getElementById('scResetOut').innerHTML = resetAt > 0 ? 'at ' + resetAt + ' s' : 'no restart';

    var prob = catchProbability(d, I);
    var blind = longestInvisible(I);
    var starts = spikeStarts(count, HORIZON, seed);
    var reads = scrapeInstants(I, off, HORIZON);
    var caught = caughtCount(starts, d, I, off);
    var missed = starts.length - caught;

    document.getElementById('scProb').innerHTML = Rtext(prob) + ' = ' + Rpct(prob, 1);
    document.getElementById('scBlind').textContent = blind + ' s';
    document.getElementById('scReads').textContent = reads.length + ' reads';
    document.getElementById('scTotal').textContent = starts.length + ' spikes';
    document.getElementById('scSeen').textContent = caught + ' spikes';
    document.getElementById('scMissed').textContent = missed + ' spikes';

    var rows = '', ladder = [1, 5, 10, 15, 30, 60], i;
    if (ladder.indexOf(I) < 0) { ladder.push(I); ladder.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < ladder.length; i += 1) {
      var p2 = catchProbability(d, ladder[i]);
      rows += '<tr><td class="' + (ladder[i] === I ? 'tone-amber' : '') + '">' + ladder[i] + ' s</td><td>'
        + Rtext(p2) + '</td><td>' + Rpct(p2, 1) + '</td><td>' + longestInvisible(ladder[i]) + ' s</td><td>'
        + Math.floor(HORIZON / ladder[i]) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>interval I</th><th>d/I exactly</th><th>P(caught)</th>'
      + '<th>longest invisible spike</th><th>reads in 5 min</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">A shorter interval costs storage in proportion '
      + '&mdash; course 10\'s cardinality lesson prices it &mdash; and buys exactly this column of '
      + 'probabilities, which is the trade the two lessons make together.</td></tr></tfoot>';

    /* The counter panel: the same reads, on a metric that only goes up until
       the process restarts. */
    var samples = counterSamples(perSecond, I, HORIZON, resetAt);
    var naive = naiveRates(samples), fixedR = correctedRates(samples);
    var at = resetInterval(samples), lost = lostIncrements(perSecond, I, resetAt);
    var truth = R(BigInt(perSecond), 1n);
    document.getElementById('scNaive').innerHTML = at < 0 ? 'no restart &mdash; both agree'
      : Rfixed(naive[at - 1], 2) + '/s';
    document.getElementById('scFixed').innerHTML = at < 0 ? Rfixed(truth, 2) + '/s, correctly'
      : Rfixed(fixedR[at - 1], 2) + '/s, losing ' + group(BigInt(lost));
    var crows = '', lo2 = at < 0 ? 1 : Math.max(1, at - 2), hi3 = at < 0 ? Math.min(5, naive.length) : Math.min(naive.length, at + 2);
    for (i = lo2; i <= hi3; i += 1) {
      var mark = i === at ? 'tone-red' : '';
      crows += '<tr><td class="' + mark + '">' + samples[i - 1][0] + ' &rarr; ' + samples[i][0] + ' s</td><td>'
        + group(BigInt(samples[i - 1][1])) + ' &rarr; ' + group(BigInt(samples[i][1])) + '</td><td class="' + mark + '">'
        + Rfixed(naive[i - 1], 2) + '/s</td><td>' + Rfixed(fixedR[i - 1], 2) + '/s</td><td>'
        + (i === at ? 'the counter went backwards' : '') + '</td></tr>';
    }
    counterTable.innerHTML = '<thead><tr><th>window</th><th>counter read</th><th>naive rate</th>'
      + '<th>corrected rate</th><th></th></tr></thead><tbody>' + crows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">'
      + (at < 0
          ? 'With no restart the two columns are the same number, which is the point: the correction '
            + 'costs nothing when nothing resets. Move the restart slider off zero.'
          : 'A rate is (read &minus; previous read) &divide; time. Across a restart that difference is '
            + 'negative, so the naive column reports <strong>' + Rfixed(naive[at - 1], 2) + '/s</strong> for a '
            + 'counter that never stopped climbing at ' + perSecond + '/s. Treating a decrease as a restart '
            + 'and taking the second read as the whole increase gives ' + Rfixed(fixedR[at - 1], 2)
            + '/s &mdash; right in sign, and still short by the ' + group(BigInt(lost)) + ' increments that '
            + 'happened between the last read and the restart. Those are gone: no read ever saw them.')
      + '</td></tr></tfoot>';

    function px(t) { return 16 + (t / HORIZON) * 628; }
    var s = '<line x1="16" y1="110" x2="644" y2="110" stroke="var(--line-strong)" stroke-width="1" />';
    for (i = 0; i < starts.length; i += 1) {
      var hit = spikeCaught(starts[i], d, I, off);
      s += '<rect x="' + px(starts[i]) + '" y="52" width="' + Math.max(1.5, px(starts[i] + d) - px(starts[i]))
        + '" height="58" fill="var(--' + (hit ? 'cyan' : 'red') + ')" opacity="' + (hit ? '0.75' : '0.9') + '" />';
    }
    for (i = 0; i < reads.length; i += 1) {
      s += '<line x1="' + px(reads[i]) + '" y1="110" x2="' + px(reads[i]) + '" y2="126" stroke="var(--amber)" '
        + 'stroke-width="1.5" />';
    }
    s += '<text x="16" y="20" font-size="11" fill="var(--muted)">five minutes of a signal that spiked '
      + starts.length + ' times</text>'
      + '<text x="16" y="38" font-size="10" fill="var(--red)">' + missed + ' of them fell entirely between two '
      + 'reads and are not in any graph anyone will look at</text>'
      + '<text x="16" y="146" font-size="10" fill="var(--amber)">' + reads.length + ' scrape instants, ' + I
      + ' s apart, phase +' + off + ' s</text>'
      + '<text x="644" y="146" text-anchor="end" font-size="10" fill="var(--muted)">300 s</text>';
    plot.innerHTML = s;

    var always = Rcmp(prob, R(1n, 1n)) === 0;
    status.innerHTML = always
      ? 'At d = ' + d + ' s and I = ' + I + ' s every spike outlasts the gap between reads, so d/I caps at '
        + '<strong>1</strong> and nothing can hide. This run caught ' + caught + ' of ' + starts.length + '.'
      : 'A ' + d + ' s spike read every ' + I + ' s is caught with probability <strong>' + Rtext(prob)
        + ' = ' + Rpct(prob, 1) + '</strong>, so about ' + Rfixed(Rmul(prob, R(BigInt(starts.length), 1n)), 1)
        + ' of these ' + starts.length + ' spikes would be expected to show up; <strong>' + caught
        + '</strong> did on this seed. <span class="tone-red">' + missed + ' spike'
        + (missed === 1 ? '' : 's') + ' left no trace at all.</span> Any spike shorter than <strong>'
        + blind + ' s</strong> can fall entirely between two reads, so a flat graph at this interval is '
        + 'evidence about the reads and not about the system. The fix is a shorter interval, an aggregate '
        + 'the exporter computes between reads (a max or a counter, which cannot miss what it accumulates), '
        + 'or an alert on the counter rather than on the gauge. '
        + (at < 0
            ? 'A counter has its own failure, and the restart slider shows it: set it anywhere but zero.'
            : '<span class="tone-red">And a counter has its own failure.</span> The process restarted at '
              + resetAt + ' s, between the reads at ' + samples[at - 1][0] + ' s and ' + samples[at][0]
              + ' s, so that window\'s naive rate is <strong>' + Rfixed(naive[at - 1], 2) + '/s</strong> for a '
              + 'counter climbing steadily at ' + perSecond + '/s. The reset is invisible &mdash; no read saw '
              + 'it &mdash; and the only evidence is that the number went down, which is exactly what the '
              + 'correction keys on.');
  }

  [iS, dS, cS, offS, seedS, rateS, resetS].forEach(function (el) { el.addEventListener('input', redraw); });
  iS.value = """ + str(interval) + r"""; dS.value = """ + str(width) + r"""; cS.value = """ + str(spikes) + r""";
  offS.value = """ + str(offset) + r"""; seedS.value = """ + str(seed) + r""";
  rateS.value = """ + str(per_second) + r"""; resetS.value = """ + str(reset_at) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Spikes and the interval that reads them",
        subtitle="min(1, d/I), what a flat graph is evidence of, and a counter that went backwards",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the interval and the spike"),
        panel_intro=cfg.get(
            "panel_intro",
            "The probability is an exact fraction. The run drawn beneath it is one seeded set of "
            "spike times, so its hit rate is near that probability rather than equal to it. The "
            "second table is the other thing these reads cannot see: a process restart, which sends "
            "the counter to zero and the naive rate negative.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - sample
# ---------------------------------------------------------------------------

_POPULATION = "5:900, 8:60, 12:30, 400:10"

_CONFIDENCES = [
    ("1/2", "50% &mdash; a coin toss"),
    ("9/10", "90%"),
    ("95/100", "95%"),
    ("99/100", "99%"),
]


def _sample(cfg):
    per_mille = int(cfg.get("rate_per_mille", 10))
    events = int(cfg.get("events", 10))
    confidence = str(cfg.get("confidence", "95/100"))
    population = str(cfg.get("population", _POPULATION))
    threshold = int(cfg.get("threshold_ms", 100))

    markup = (
        _toolbar(
            "Sampling and rare events",
            "1 &minus; (1&minus;s)&#7503;, the rate a rare event needs, and what tail bias does to a mean",
            [("cyan", "capture probability"), ("amber", "your rate"), ("purple", "the rate needed")],
        )
        + _stage(_svg("saPlot", "0 0 660 180", "Capture probability against sampling rate, with the chosen rate and the rate the target needs both marked."))
        + _table("saTable")
        + _banner("saStatus")
    )
    controls = (
        _range("saRate", "Sampling rate s (per mille)", 1, 1000, per_mille)
        + _range("saK", "Requests in the problem you are hunting", 1, 60, events)
        + _select("saConf", "Confidence you want in catching one", _CONFIDENCES, confidence)
        + _text("saPop", "The traffic (ms:count)", population)
        + _range("saThr", "Sample every request slower than (ms)", 10, 500, threshold, 10)
        + _kpis(
            [
                ("P(catch at least one)", "saP"),
                ("P(miss all of them)", "saMiss"),
                ("Rate needed for the target", "saNeed"),
                ("Mean of the tail-biased sample", "saBiased"),
                ("Reweighted estimate", "saFixed"),
                ("True mean of the traffic", "saTrue"),
            ]
        )
        + _hint(
            "saHint",
            "One per cent sampling does not see one per cent of every problem &mdash; it sees a "
            "problem of k requests with probability 1 &minus; (1&minus;s)&#7503;, which for small k is "
            "almost nothing. Keeping every slow request instead fixes that and breaks the mean, "
            "unless each sampled request is counted 1/s times when the mean is taken.",
        )
    )

    script = _CORE_JS + r"""
  var rateS = document.getElementById('saRate'), kS = document.getElementById('saK');
  var confSel = document.getElementById('saConf'), popIn = document.getElementById('saPop');
  var thrS = document.getElementById('saThr');
  var plot = document.getElementById('saPlot'), table = document.getElementById('saTable');
  var status = document.getElementById('saStatus');

  function redraw() {
    var perMille = +rateS.value, k = +kS.value, thr = +thrS.value;
    var s = R(BigInt(perMille), 1000n), target = Rparse(confSel.value);
    document.getElementById('saRateOut').textContent = Rpct(s, 1);
    document.getElementById('saKOut').textContent = k + ' requests';
    document.getElementById('saThrOut').textContent = thr + ' ms';

    var caught = atLeastOne(s, k);
    var missed = Rsub(R(1n, 1n), caught);
    var need = rateForTarget(k, target, 1000);
    var runs = runsFromText(popIn.value);

    document.getElementById('saP').innerHTML = Rpct(caught, 2) + ' <span class="small">= ' + Rtext(caught) + '</span>';
    document.getElementById('saMiss').textContent = Rpct(missed, 2);
    document.getElementById('saNeed').innerHTML = Rpct(need, 1) + ' <span class="small">= ' + Rtext(need) + '</span>';

    if (runs) {
      var biased = sampledMean(runs, thr, s, R(1n, 1n));
      var fixedM = reweightedMean(runs, thr, s, R(1n, 1n));
      var truth = trueMean(runs);
      document.getElementById('saBiased').textContent = Rfixed(biased, 2) + ' ms';
      document.getElementById('saFixed').textContent = Rfixed(fixedM, 2) + ' ms';
      document.getElementById('saTrue').innerHTML = Rtext(truth) + ' = ' + Rfixed(truth, 2) + ' ms';
    } else {
      ['saBiased', 'saFixed', 'saTrue'].forEach(function (id) {
        document.getElementById(id).innerHTML = '&mdash;';
      });
    }

    var rows = '', ladder = [1, 5, 10, 50, 100, 250, 500], i;
    if (ladder.indexOf(perMille) < 0) { ladder.push(perMille); ladder.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < ladder.length; i += 1) {
      var si = R(BigInt(ladder[i]), 1000n), pi = atLeastOne(si, k);
      rows += '<tr><td class="' + (ladder[i] === perMille ? 'tone-amber' : '') + '">' + Rpct(si, 1)
        + '</td><td>' + Rpct(pi, 3) + '</td><td>' + (100 * captureApprox(si, k)).toFixed(3) + '%</td><td>'
        + Rfixed(Rmul(si, R(BigInt(k), 1n)), 3) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>rate s</th><th>1 &minus; (1&minus;s)<sup>' + k
      + '</sup>, exact</th><th>1 &minus; e<sup>&minus;s&middot;' + k + '</sup>, rounded</th>'
      + '<th>expected captures s&middot;k</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4" class="small-copy">Column three is the rule of thumb, computed by '
      + 'expNegApprox, which <strong>rounds</strong> &mdash; it sums a positive-term series to about '
      + '10<sup>&minus;13</sup>. That rounding is not why it differs from column two: the two columns '
      + 'are different quantities, and at s = ' + Rpct(s, 1) + ' they differ by '
      + Math.abs(100 * (captureApprox(s, k) - Rplot(caught))).toFixed(3) + ' percentage points &mdash; '
      + 'orders of magnitude more than 10<sup>&minus;13</sup>. An approximation and a rounded '
      + 'approximation are different kinds of wrong, and this course keeps them apart.</td></tr></tfoot>';

    var pts = [], j;
    for (j = 0; j <= 100; j += 1) {
      var sj = R(BigInt(j * 10), 1000n);
      var v = j === 0 ? 0 : Rplot(atLeastOne(sj, k));
      pts.push((22 + (j / 100) * 616) + ',' + (146 - v * 116));
    }
    var sx = 22 + (Math.min(1000, perMille) / 1000) * 616;
    var nx = 22 + (Rplot(need)) * 616;
    var ty = 146 - Rplot(target) * 116;
    var g = '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<line x1="22" y1="' + ty + '" x2="638" y2="' + ty + '" stroke="var(--green)" stroke-width="1.5" '
      + 'stroke-dasharray="4 3" /><text x="22" y="' + (ty - 5) + '" font-size="10" fill="var(--green)">target '
      + Rpct(target, 0) + '</text>'
      + '<line x1="' + sx + '" y1="26" x2="' + sx + '" y2="146" stroke="var(--amber)" stroke-width="2" />'
      + '<text x="' + Math.min(sx + 5, 420) + '" y="' + Math.max(22, 140 - Rplot(caught) * 116) + '" font-size="10" '
      + 'fill="var(--amber)" font-weight="700">s = ' + Rpct(s, 1) + ' catches ' + Rpct(caught, 1) + '</text>'
      + '<line x1="' + nx + '" y1="26" x2="' + nx + '" y2="146" stroke="var(--purple)" stroke-width="2" '
      + 'stroke-dasharray="5 4" />'
      + '<text x="' + Math.min(nx + 5, 420) + '" y="40" font-size="10" fill="var(--purple)">needs '
      + Rpct(need, 1) + '</text>'
      + '<line x1="22" y1="146" x2="638" y2="146" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="22" y="164" font-size="10" fill="var(--muted)">0%</text>'
      + '<text x="638" y="164" text-anchor="end" font-size="10" fill="var(--muted)">100% sampled</text>'
      + '<text x="22" y="18" font-size="11" fill="var(--muted)">P(at least one of ' + k
      + ' requests sampled), against the rate</text>';
    plot.innerHTML = g;

    var slow = runs ? slowCount(runs, thr) : 0;
    status.innerHTML = 'At <strong>' + Rpct(s, 1) + '</strong> sampling, a problem made of <strong>' + k
      + '</strong> requests is caught with probability <strong>' + Rpct(caught, 2) + '</strong> &mdash; so it '
      + 'is missed ' + Rpct(missed, 1) + ' of the time. Reaching ' + Rpct(target, 0) + ' confidence needs '
      + '<strong>' + Rpct(need, 1) + '</strong>, found by scanning the thousandths rather than by taking a '
      + 'logarithm. <span class="tone-muted">This is the same 1 &minus; (1&minus;p)&#7503; that the load-test '
      + 'lesson uses for n requests and the alerting lesson uses for a month of windows; all three call one '
      + 'function.</span> '
      + (runs
          ? 'Keeping every request over ' + thr + ' ms fixes the capture problem &mdash; there are ' + slow
            + ' of them and none is dropped &mdash; and it breaks the mean: the sampled requests average '
            + '<strong>' + Rfixed(sampledMean(runs, thr, s, R(1n, 1n)), 2) + ' ms</strong> against a true '
            + Rfixed(trueMean(runs), 2) + ' ms. Counting each sampled request 1/s times restores it exactly: '
            + '<span class="tone-green">' + Rfixed(reweightedMean(runs, thr, s, R(1n, 1n)), 2)
            + ' ms</span>. A tail-biased sample is a good sample and a dishonest average.'
          : '<span class="tone-red">The traffic field needs ms:count pairs</span>, such as 5:900, 400:10.');
  }

  [rateS, kS, thrS].forEach(function (el) { el.addEventListener('input', redraw); });
  popIn.addEventListener('input', redraw);
  confSel.addEventListener('change', redraw);
  rateS.value = """ + str(per_mille) + r"""; kS.value = """ + str(events) + r""";
  thrS.value = """ + str(threshold) + r"""; popIn.value = """ + _js_string(population) + r""";
  confSel.value = '""" + confidence + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="One per cent sampling does not see one per cent of a problem",
        subtitle="The capture probability, the rate it takes, and the mean it ruins",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the rate and the problem"),
        panel_intro=cfg.get(
            "panel_intro",
            "The capture probability is exact. Beside it the page prints the e-to-the-minus rule of "
            "thumb, which rounds and says so, and differs by far more than its rounding.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - cardinality
# ---------------------------------------------------------------------------

_LABELS = [
    ("service", "cdL0", 40, 1, 200),
    ("endpoint", "cdL1", 120, 1, 400),
    ("status", "cdL2", 6, 1, 60),
    ("instance", "cdL3", 30, 1, 300),
    ("method", "cdL4", 4, 1, 20),
]

_EXTRA = [
    ("1", "no sixth label"),
    ("50", "region &times; zone (50)"),
    ("500", "customer (500)"),
    ("10000", "user_id (10 000)"),
    ("1000000", "request_id (1 000 000) &mdash; the mistake"),
]


def _cardinality(cfg):
    cards = [int(cfg.get(cid, default)) for _n, cid, default, _lo, _hi in _LABELS]
    extra = str(cfg.get("extra", "1"))
    scrape = int(cfg.get("scrape_s", 15))
    per_sample = int(cfg.get("bytes_per_sample", 2))

    markup = (
        _toolbar(
            "A label is a multiplier",
            "the product of the cardinalities, and the bytes a day of it costs",
            [("cyan", "series after each label"), ("amber", "the sixth label"), ("red", "storage per day")],
        )
        + _stage(_svg("cdPlot", "0 0 660 190", "The running product after each label is added, drawn on a log axis with the exact counts printed."))
        + _table("cdTable")
        + _banner("cdStatus")
    )
    controls = (
        "".join(
            _range(cid, "%s &mdash; distinct values" % name, lo, hi, value)
            for (name, cid, _d, lo, hi), value in zip(_LABELS, cards)
        )
        + _select("cdExtra", "Add one more label", _EXTRA, extra)
        + _range("cdScrape", "Scrape interval (seconds)", 1, 120, scrape)
        + _range("cdBytes", "Bytes per stored sample", 1, 16, per_sample)
        + _kpis(
            [
                ("Series", "cdSeries"),
                ("Samples per series per day", "cdSamples"),
                ("Samples per day", "cdTotal"),
                ("Storage per day", "cdDay"),
                ("Storage per 30 days", "cdMonth"),
                ("The sixth label multiplies by", "cdMult"),
            ]
        )
        + _hint(
            "cdHint",
            "Every figure here is an integer count, so the arithmetic is exact and the only "
            "interesting question is how fast a product grows. A label with one value per request "
            "makes the series count equal the request count, which is a log with extra steps.",
        )
    )

    script = _CORE_JS + r"""
  var SLIDERS = ['cdL0', 'cdL1', 'cdL2', 'cdL3', 'cdL4'].map(function (id) { return document.getElementById(id); });
  var NAMES = ['service', 'endpoint', 'status', 'instance', 'method'];
  var extraSel = document.getElementById('cdExtra'), scrapeS = document.getElementById('cdScrape');
  var bytesS = document.getElementById('cdBytes');
  var plot = document.getElementById('cdPlot'), table = document.getElementById('cdTable');
  var status = document.getElementById('cdStatus');
  var EXTRA_NAMES = { '50': 'region x zone', '500': 'customer', '10000': 'user_id', '1000000': 'request_id' };

  function redraw() {
    var cards = [], i;
    for (i = 0; i < SLIDERS.length; i += 1) {
      cards.push(+SLIDERS[i].value);
      document.getElementById(SLIDERS[i].id + 'Out').textContent = group(BigInt(+SLIDERS[i].value)) + ' values';
    }
    var extra = +extraSel.value, scrape = +scrapeS.value, per = +bytesS.value;
    document.getElementById('cdScrapeOut').textContent = 'every ' + scrape + ' s';
    document.getElementById('cdBytesOut').textContent = per + ' B';

    var names = NAMES.slice(), all = cards.slice();
    if (extra > 1) { names.push(EXTRA_NAMES[extraSel.value] || 'extra label'); all.push(extra); }
    var series = seriesCount(all);
    var perDay = samplesPerDay(scrape);
    var samples = Rmul(R(series, 1n), perDay);
    var bytes = bytesPerDay(series, scrape, per);
    var gb = gigabytes(bytes);

    document.getElementById('cdSeries').textContent = group(series);
    document.getElementById('cdSamples').textContent = Rfixed(perDay, 0) + ' samples';
    document.getElementById('cdTotal').textContent = group(Rfixed(samples, 0)) + ' samples';
    document.getElementById('cdDay').textContent = Rfixed(gb, 2) + ' GB';
    document.getElementById('cdMonth').textContent = Rfixed(Rmul(gb, R(30n, 1n)), 1) + ' GB';
    document.getElementById('cdMult').innerHTML = extra > 1 ? '&times;' + group(BigInt(extra)) : 'nothing added';

    var rows = '', running = 1n;
    for (i = 0; i < all.length; i += 1) {
      var before = running;
      running *= BigInt(all[i]);
      rows += '<tr><td class="' + (i >= NAMES.length ? 'tone-amber' : '') + '">' + names[i] + '</td><td>'
        + group(BigInt(all[i])) + '</td><td>' + group(before) + ' &times; ' + group(BigInt(all[i]))
        + '</td><td>' + group(running) + '</td><td>'
        + Rfixed(gigabytes(bytesPerDay(running, scrape, per)), 3) + ' GB</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>label added</th><th>cardinality</th><th>product so far</th>'
      + '<th>series</th><th>storage per day</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">1 GB = 10<sup>9</sup> bytes, the unit a bill is '
      + 'quoted in. ' + per + ' bytes per sample is the compressed figure a time-series database reaches '
      + 'on smooth data; a counter that jumps costs more, and this page computes the bytes for whatever '
      + 'number you set.</td></tr></tfoot>';

    /* A log axis, because the whole point is that the product spans decades.
       The bar LENGTHS are logarithms and so are rounded; every count printed
       beside them is exact. */
    var maxLog = Math.max(1, Number(String(running).length));
    var s = '', y = 34, running2 = 1n;
    for (i = 0; i < all.length; i += 1) {
      running2 *= BigInt(all[i]);
      var digits = String(running2).length;
      var w = Math.max(3, (digits / maxLog) * 520);
      s += '<rect x="96" y="' + (y - 11) + '" width="' + w + '" height="18" rx="3" fill="var(--'
        + (i >= NAMES.length ? 'amber' : 'cyan') + ')" opacity="0.8" />'
        + '<text x="0" y="' + (y + 3) + '" font-size="10" fill="var(--muted)">' + names[i] + '</text>'
        + '<text x="' + (96 + w + 6) + '" y="' + (y + 3) + '" font-size="10" fill="var(--'
        + (i >= NAMES.length ? 'amber' : 'cyan') + ')">' + group(running2) + ' series</text>';
      y += 26;
    }
    s += '<text x="0" y="16" font-size="11" fill="var(--muted)">series after each label, on a log axis: '
      + 'one bar step is a digit</text>'
      + '<text x="0" y="' + (y + 10) + '" font-size="10" fill="var(--red)">' + Rfixed(gb, 2)
      + ' GB a day, ' + Rfixed(Rmul(gb, R(30n, 1n)), 1) + ' GB a month at ' + per + ' B per sample and a '
      + scrape + ' s scrape</text>';
    plot.innerHTML = s;

    var withoutExtra = seriesCount(cards);
    status.innerHTML = '<strong>' + group(series) + ' series</strong> is the product '
      + all.map(function (c) { return group(BigInt(c)); }).join(' &times; ') + ', and at a ' + scrape
      + ' second scrape each one stores ' + Rfixed(perDay, 0) + ' samples a day: <strong>'
      + Rfixed(gb, 2) + ' GB a day</strong>, ' + Rfixed(Rmul(gb, R(30n, 1n)), 1) + ' GB a month. '
      + (extra > 1
          ? '<span class="tone-amber">The sixth label multiplied the whole thing by ' + group(BigInt(extra))
            + '</span>, from ' + group(withoutExtra) + ' series to ' + group(series) + ' &mdash; it did not '
            + 'add ' + group(BigInt(extra)) + ' series, it multiplied every series that already existed. '
            + (extra >= 1000000
                ? 'At one value per request this is not a metric at all: it is a log line with a numeric '
                  + 'field, stored in a database designed for the opposite shape.'
                : 'That is the whole hazard: a label reads like a column and behaves like a Cartesian product.')
          : 'Add the sixth label and watch the product rather than the sum: the cost of a label is '
            + 'multiplicative, which is why one carelessly chosen one can cost more than the other five '
            + 'together.')
      + ' Halving the scrape interval doubles this bill and buys exactly the catch probabilities the '
      + 'scrape-interval lesson computes.';
  }

  SLIDERS.concat([scrapeS, bytesS]).forEach(function (el) { el.addEventListener('input', redraw); });
  extraSel.addEventListener('change', redraw);
""" + "".join(
        "  document.getElementById('%s').value = %d;\n" % (cid, value)
        for (_n, cid, _d, _lo, _hi), value in zip(_LABELS, cards)
    ) + r"""  extraSel.value = '""" + extra + r"""';
  scrapeS.value = """ + str(scrape) + r"""; bytesS.value = """ + str(per_sample) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="What a label costs",
        subtitle="The product of the cardinalities, and the gigabytes a day it turns into",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the labels"),
        panel_intro=cfg.get(
            "panel_intro",
            "The series count is recomputed as each label is added, so the multiplication is "
            "visible one row at a time rather than as a single finished number.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - loadtest
# ---------------------------------------------------------------------------

_TAILS = [
    ("1/100", "p99 &mdash; the top 1%"),
    ("1/1000", "p99.9 &mdash; the top 0.1%"),
    ("1/10000", "p99.99 &mdash; the top 0.01%"),
]


def _loadtest(cfg):
    tail = str(cfg.get("tail", "1/1000"))
    confidence = str(cfg.get("confidence", "95/100"))
    runs = int(cfg.get("runs", 600))

    markup = (
        _toolbar(
            "How long to run a load test",
            "1 &minus; (1&minus;t)&#8319;, and the n a stated confidence needs",
            [("cyan", "P(the run saw the tail)"), ("amber", "your run length"), ("green", "the confidence")],
        )
        + _stage(_svg("ltPlot", "0 0 660 180", "The probability that a run of n requests contains at least one from the target tail, with the run length and the confidence marked."))
        + _table("ltTable")
        + _banner("ltStatus")
    )
    controls = (
        _select("ltTail", "The percentile you want to measure", _TAILS, tail)
        + _select("ltConf", "Confidence that the run saw it", _CONFIDENCES, confidence)
        + _range("ltN", "Requests in the run", 100, 6000, runs, 100)
        + _kpis(
            [
                ("P(this run sees the tail)", "ltP"),
                ("Requests needed", "ltNeed"),
                ("P(at that many)", "ltAt"),
                ("Expected tail requests in the run", "ltExp"),
                ("Requests for an even chance", "ltHalf"),
                ("At 500 requests a second", "ltTime"),
            ]
        )
        + _hint(
            "ltHint",
            "The answer is a count, so it is found by an exact integer search &mdash; bracket by "
            "doubling, then bisect &mdash; and never by a logarithm. Every probability printed here "
            "is an exact fraction with a numerator of thousands of digits, divided out at the last "
            "moment.",
        )
    )

    script = _CORE_JS + r"""
  var tailSel = document.getElementById('ltTail'), confSel = document.getElementById('ltConf');
  var nS = document.getElementById('ltN');
  var plot = document.getElementById('ltPlot'), table = document.getElementById('ltTable');
  var status = document.getElementById('ltStatus');

  function redraw() {
    var n = +nS.value;
    var t = Rparse(tailSel.value), target = Rparse(confSel.value);
    document.getElementById('ltNOut').textContent = group(BigInt(n)) + ' requests';

    var seen = atLeastOne(t, n);
    var need = trialsForTarget(t, target, 1 << 22);
    var atNeed = need ? atLeastOne(t, need) : null;
    var half = trialsForTarget(t, R(1n, 2n), 1 << 22);
    var expected = Rmul(t, R(BigInt(n), 1n));
    var seconds = need ? R(BigInt(need), 500n) : null;

    document.getElementById('ltP').textContent = Rpct(seen, 2);
    document.getElementById('ltNeed').innerHTML = need ? group(BigInt(need)) + ' requests' : '&mdash;';
    document.getElementById('ltAt').innerHTML = atNeed ? Rpct(atNeed, 3) : '&mdash;';
    document.getElementById('ltExp').textContent = Rfixed(expected, 2) + ' requests';
    document.getElementById('ltHalf').textContent = group(BigInt(half)) + ' requests';
    document.getElementById('ltTime').innerHTML = seconds ? Rfixed(seconds, 1) + ' s of load' : '&mdash;';

    var rows = '', ladder = [100, 300, 600, 1000, 3000, 6000], i;
    if (ladder.indexOf(n) < 0) { ladder.push(n); ladder.sort(function (a, b) { return a - b; }); }
    if (ladder.indexOf(need) < 0 && need && need <= 60000) { ladder.push(need); ladder.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < ladder.length; i += 1) {
      var pi = atLeastOne(t, ladder[i]);
      rows += '<tr><td class="' + (ladder[i] === n ? 'tone-amber' : (ladder[i] === need ? 'tone-green' : ''))
        + '">' + group(BigInt(ladder[i])) + '</td><td>' + Rpct(pi, 3) + '</td><td>'
        + Rfixed(Rmul(t, R(BigInt(ladder[i]), 1n)), 2) + '</td><td>'
        + (ladder[i] === need ? 'the answer for ' + Rpct(target, 0) : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>run length n</th><th>P(sees the tail)</th>'
      + '<th>expected tail requests</th><th></th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4" class="small-copy">Seeing ONE request from the tail is the weakest '
      + 'possible claim to have measured it &mdash; a percentile estimated from a single observation is '
      + 'the observation. Expect ten before believing the number, which multiplies every n here by about '
      + 'ten.</td></tr></tfoot>';

    var want = Math.max(n, need ? Math.min(need, 60000) : n, 1);
    var steps = 60, step = Math.max(1, Math.round(want / steps)), top = step * steps;
    var curve = atLeastOneCurve(t, step, steps), pts = [], j;
    for (j = 0; j <= steps; j += 1) {
      pts.push((22 + (j / steps) * 616) + ',' + (146 - Rplot(curve[j]) * 116));
    }
    var nx = 22 + (n / top) * 616, gx = need ? 22 + (Math.min(need, top) / top) * 616 : 0;
    var ty = 146 - Rplot(target) * 116;
    var s = '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<line x1="22" y1="' + ty + '" x2="638" y2="' + ty + '" stroke="var(--green)" stroke-width="1.5" '
      + 'stroke-dasharray="4 3" /><text x="22" y="' + (ty - 5) + '" font-size="10" fill="var(--green)">'
      + Rpct(target, 0) + ' confidence</text>'
      + '<line x1="' + nx + '" y1="26" x2="' + nx + '" y2="146" stroke="var(--amber)" stroke-width="2" />'
      + '<text x="' + Math.min(nx + 5, 400) + '" y="' + Math.max(22, 140 - Rplot(seen) * 116) + '" font-size="10" '
      + 'fill="var(--amber)" font-weight="700">' + group(BigInt(n)) + ' requests &rarr; ' + Rpct(seen, 1) + '</text>';
    if (need && need <= top) {
      s += '<line x1="' + gx + '" y1="26" x2="' + gx + '" y2="146" stroke="var(--purple)" stroke-width="2" '
        + 'stroke-dasharray="5 4" /><text x="' + Math.min(gx + 5, 420) + '" y="40" font-size="10" '
        + 'fill="var(--purple)">' + group(BigInt(need)) + ' needed</text>';
    }
    s += '<line x1="22" y1="146" x2="638" y2="146" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="22" y="164" font-size="10" fill="var(--muted)">0</text>'
      + '<text x="638" y="164" text-anchor="end" font-size="10" fill="var(--muted)">' + group(BigInt(top))
      + ' requests</text>'
      + '<text x="22" y="18" font-size="11" fill="var(--muted)">P(a run of n requests contains at least one '
      + 'from the top ' + Rpct(t, 2) + ')</text>';
    plot.innerHTML = s;

    var short = Rcmp(seen, target) < 0;
    status.innerHTML = 'A run of <strong>' + group(BigInt(n)) + ' requests</strong> contains at least one '
      + 'request from the top ' + Rpct(t, 2) + ' with probability <strong>' + Rpct(seen, 2) + '</strong>, and '
      + 'expects <strong>' + Rfixed(expected, 2) + '</strong> of them. '
      + (short
          ? '<span class="tone-red">That is short of ' + Rpct(target, 0) + '.</span> Reaching it takes <strong>'
            + group(BigInt(need)) + ' requests</strong> &mdash; ' + Rfixed(seconds, 1) + ' seconds at 500 '
            + 'requests a second &mdash; found by bracketing and bisecting on the exact fraction, with no '
            + 'logarithm anywhere. An even chance takes ' + group(BigInt(half)) + '.'
          : 'That clears ' + Rpct(target, 0) + '; the shortest run that does is <strong>' + group(BigInt(need))
            + ' requests</strong>, and an even chance takes ' + group(BigInt(half)) + '.')
      + ' A one-minute run that reports a p99.9 is reporting the largest number it happened to see, which '
      + 'is a different quantity with the same name.';
  }

  nS.addEventListener('input', redraw);
  [tailSel, confSel].forEach(function (el) { el.addEventListener('change', redraw); });
  nS.value = """ + str(runs) + r"""; tailSel.value = '""" + tail + r"""'; confSel.value = '""" + confidence + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A run long enough to have seen the tail",
        subtitle="The probability a load test ever met the request it is reporting on",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the percentile and the confidence"),
        panel_intro=cfg.get(
            "panel_intro",
            "The run length is a count, so it is found by an exact integer search on the same "
            "1 &minus; (1&minus;p)&#7503; the sampling lesson uses.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - burn
# ---------------------------------------------------------------------------

# The four windows burn-rate alerting is usually quoted with. The values are
# minutes, so every figure on the page is an exact rational number of minutes.
_WINDOWS = [
    ("5", "5 minutes"),
    ("60", "1 hour"),
    ("360", "6 hours"),
    ("1440", "1 day"),
    ("4320", "3 days"),
]

# The standard multi-window pairs, as (burn rate x10, window minutes, label).
# Declared here and emitted into the script below, so that the table the page
# draws and the pairs this module documents cannot drift apart.
_PAIRS = ((144, 60, "1 hour"), (60, 360, "6 hours"), (30, 1440, "1 day"), (10, 4320, "3 days"))


def _burn(cfg):
    objective = str(cfg.get("objective", "999/1000"))
    days = int(cfg.get("days", 30))
    burn_tenths = int(cfg.get("burn_tenths", 144))
    window = str(cfg.get("window", "60"))

    markup = (
        _toolbar(
            "Burn rate against the budget",
            "b &times; w &divide; period of the budget, and period &divide; b until it is gone",
            [("green", "budget left"), ("red", "spent in this window"), ("amber", "time to exhaustion")],
        )
        + _stage(_svg("brPlot", "0 0 660 200", "The error budget as a bar with the window's spend taken out, and the period with the exhaustion point marked."))
        + _table("brTable")
        + _banner("brStatus")
    )
    controls = (
        _select("brObj", "The objective", _OBJECTIVES, objective)
        + _range("brDays", "The period (days)", 1, 90, days)
        + _range("brBurn", "Burn rate b (tenths)", 1, 400, burn_tenths)
        + _select("brWindow", "Alert window w", _WINDOWS, window)
        + _kpis(
            [
                ("Error budget for the period", "brBudget"),
                ("Error rate at this burn", "brRate"),
                ("Budget this window spends", "brSpend"),
                ("As a share of the budget", "brShare"),
                ("Time to exhaustion", "brExhaust"),
                ("Budget left when it pages", "brLeft"),
            ]
        )
        + _hint(
            "brHint",
            "A burn rate of 1 spends the whole budget exactly at the end of the period. A burn of 14.4 "
            "spends 2% of it in an hour, which is why that pair pages fast; a burn of 1 over three days "
            "spends 10% of it, which is why that pair pages slowly and catches the quiet leak the fast "
            "one cannot see.",
        )
    )

    script = _CORE_JS + r"""
  var objSel = document.getElementById('brObj'), daysS = document.getElementById('brDays');
  var burnS = document.getElementById('brBurn'), winSel = document.getElementById('brWindow');
  var plot = document.getElementById('brPlot'), table = document.getElementById('brTable');
  var status = document.getElementById('brStatus');
  var PAIRS = """ + json.dumps([list(pair) for pair in _PAIRS]) + r""";

  function redraw() {
    var days = +daysS.value, tenths = +burnS.value, w = +winSel.value;
    var objective = Rparse(objSel.value), b = R(BigInt(tenths), 10n), wm = R(BigInt(w), 1n);
    document.getElementById('brDaysOut').textContent = days + (days === 1 ? ' day' : ' days');
    document.getElementById('brBurnOut').innerHTML = Rfixed(b, 1) + '&times;';

    var budget = budgetMinutes(objective, days);
    var rate = burnErrorRate(b, objective);
    var share = burnFraction(b, wm, days);
    var spend = budgetSpentMinutes(b, wm, days, objective);
    var exhaust = exhaustMinutes(b, days);
    var left = Rsub(budget, spend);

    document.getElementById('brBudget').innerHTML = Rtext(budget) + ' min = <strong>' + Rfixed(budget, 2)
      + ' minutes</strong>';
    document.getElementById('brRate').innerHTML = Rpct(rate, 3) + ' of requests failing';
    document.getElementById('brSpend').textContent = minutesText(spend);
    document.getElementById('brShare').innerHTML = Rtext(share) + ' = ' + Rpct(share, 2);
    document.getElementById('brExhaust').textContent = exhaust ? minutesText(exhaust) : 'never';
    document.getElementById('brLeft').textContent = minutesText(left) + ' of ' + Rfixed(budget, 1);

    var rows = '', i;
    for (i = 0; i < PAIRS.length; i += 1) {
      var pb = R(BigInt(PAIRS[i][0]), 10n), pw = R(BigInt(PAIRS[i][1]), 1n);
      var pf = burnFraction(pb, pw, days), pe = exhaustMinutes(pb, days);
      rows += '<tr><td>' + Rfixed(pb, 1) + '&times;</td><td>' + PAIRS[i][2] + '</td><td>' + Rtext(pf)
        + '</td><td>' + Rpct(pf, 2) + '</td><td>' + minutesText(budgetSpentMinutes(pb, pw, days, objective))
        + '</td><td>' + minutesText(pe) + '</td></tr>';
    }
    rows += '<tr><td class="tone-amber">' + Rfixed(b, 1) + '&times;</td><td class="tone-amber">'
      + minutesText(wm) + '</td><td>' + Rtext(share) + '</td><td>' + Rpct(share, 2) + '</td><td>'
      + minutesText(spend) + '</td><td>' + (exhaust ? minutesText(exhaust) : 'never') + '</td></tr>';
    table.innerHTML = '<thead><tr><th>burn b</th><th>window w</th><th>b&middot;w/period</th>'
      + '<th>share of the budget</th><th>minutes of it</th><th>exhausts in</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="6" class="small-copy">The first four rows are the pairs '
      + 'multi-window alerting is usually built from: a fast pair that pages within the hour on a severe '
      + 'burn, and a slow pair that catches a burn too gentle for the fast one to notice before the budget '
      + 'is gone. Every figure is exact on a ' + days + '-day period.</td></tr></tfoot>';

    var full = 560, spent = Math.max(1, Math.min(full, Rplot(share) * full));
    var s = '<text x="0" y="16" font-size="11" fill="var(--muted)">the error budget, ' + Rfixed(budget, 2)
      + ' minutes over ' + days + ' days</text>'
      + '<rect x="0" y="30" width="' + full + '" height="26" rx="3" fill="var(--green)" opacity="0.35" />'
      + '<rect x="0" y="30" width="' + spent + '" height="26" rx="3" fill="var(--red)" opacity="0.8" />'
      + '<text x="' + Math.min(spent + 8, 430) + '" y="48" font-size="10" fill="var(--red)">'
      + minutesText(spend) + ' spent in ' + minutesText(wm) + ' at ' + Rfixed(b, 1) + '&times;</text>'
      + '<text x="0" y="74" font-size="10" fill="var(--green)">' + minutesText(left) + ' left</text>';
    var px = function (m) { return 8 + Math.min(1, m / (days * 1440)) * 620; };
    s += '<line x1="8" y1="130" x2="628" y2="130" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="8" y="104" font-size="11" fill="var(--muted)">the period, and where this burn runs out</text>'
      + '<text x="8" y="150" font-size="10" fill="var(--muted)">day 0</text>'
      + '<text x="628" y="150" text-anchor="end" font-size="10" fill="var(--muted)">day ' + days + '</text>';
    if (exhaust && Rcmp(exhaust, R(BigInt(days) * 1440n, 1n)) <= 0) {
      var ex = px(Rplot(exhaust));
      s += '<line x1="' + ex + '" y1="112" x2="' + ex + '" y2="146" stroke="var(--amber)" stroke-width="3" />'
        + '<text x="' + Math.max(0, Math.min(ex - 40, 470)) + '" y="172" font-size="10" fill="var(--amber)" '
        + 'font-weight="700">budget gone after ' + minutesText(exhaust) + '</text>';
    } else {
      s += '<text x="8" y="172" font-size="10" fill="var(--green)">at this burn the budget outlasts the '
        + 'period</text>';
    }
    plot.innerHTML = s;

    var fast = Rcmp(share, R(1n, 50n)) <= 0;
    status.innerHTML = 'At ' + Rpct(objective, 3) + ' over ' + days + ' days the budget is <strong>'
      + Rtext(budget) + ' minutes = ' + Rfixed(budget, 2) + '</strong> &mdash; on the standard 30-day window '
      + 'three nines is exactly 43.2 minutes, and that is this number with the slider at 30. '
      + '<span class="tone-muted">Course 5 counts the same budget in failed requests over a 2 628 000-second '
      + 'month, where the same objective is 43.8 minutes; the convention is stated on both pages because '
      + 'the two figures are the same fact about different months.</span> Burning at <strong>'
      + Rfixed(b, 1) + '&times;</strong> means ' + Rpct(rate, 3) + ' of requests failing, which exhausts the '
      + 'budget in <strong>' + (exhaust ? minutesText(exhaust) : 'never') + '</strong>. A ' + minutesText(wm)
      + ' window at that rate spends <strong>' + Rtext(share) + ' = ' + Rpct(share, 2) + '</strong> of it'
      + (fast ? ', so an alert on this pair fires while most of the budget is still there.'
              : ', so by the time this pair fires a large part of the budget is already gone &mdash; which is '
                + 'what the faster pair is for.')
      + ' <strong>An SLO is not an SLA.</strong> The arithmetic above is identical for both; what differs is '
      + 'the consequence of the last row. An objective missed spends a budget your own team owns, and the '
      + 'response is to stop shipping features until it recovers. An agreement missed spends money, because '
      + 'a contract attached a refund to it &mdash; which is why an SLA is normally set looser than the SLO '
      + 'it is measured against, so that the internal alarm fires long before the external one does.';
  }

  [daysS, burnS].forEach(function (el) { el.addEventListener('input', redraw); });
  [objSel, winSel].forEach(function (el) { el.addEventListener('change', redraw); });
  daysS.value = """ + str(days) + r"""; burnS.value = """ + str(burn_tenths) + r""";
  objSel.value = '""" + objective + r"""'; winSel.value = '""" + window + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Spending an error budget",
        subtitle="What a burn rate costs per window, and when it runs out",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the objective and the burn"),
        panel_intro=cfg.get(
            "panel_intro",
            "The budget, the share a window spends and the time to exhaustion are exact fractions "
            "of a minute, computed from the objective and the period you set.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - threshold
# ---------------------------------------------------------------------------

_ALERT_WINDOWS = [
    ("1", "1 minute"),
    ("5", "5 minutes"),
    ("15", "15 minutes"),
    ("60", "1 hour"),
]


def _threshold(cfg):
    per_mille = int(cfg.get("rate_per_mille", 10))
    window_n = int(cfg.get("window_requests", 200))
    threshold_pct = int(cfg.get("threshold_pct", 2))
    window_minutes = str(cfg.get("window_minutes", "5"))

    markup = (
        _toolbar(
            "What a threshold fires at when nothing is wrong",
            "the exact binomial tail of a window, and the pages a week it comes to",
            [("cyan", "errors per window"), ("red", "the threshold and above"), ("amber", "the true rate")],
        )
        + _stage(_svg("thPlot", "0 0 660 200", "The distribution of errors in one window, with every outcome at or above the threshold shaded."))
        + _table("thTable")
        + _banner("thStatus")
    )
    controls = (
        _range("thRate", "True error rate (per mille)", 1, 50, per_mille)
        + _range("thN", "Requests in one window", 20, 200, window_n, 10)
        + _range("thPct", "Alert when the window's error rate exceeds (%)", 1, 20, threshold_pct)
        + _select("thWin", "Window length", _ALERT_WINDOWS, window_minutes)
        + _kpis(
            [
                ("Errors needed to fire", "thK"),
                ("P(fires with nothing wrong)", "thQ"),
                ("Windows in a week", "thWindows"),
                ("False pages a week", "thPages"),
                ("P(at least one in the next hour)", "thHour"),
                ("False pages in 30 days", "thMonth"),
            ]
        )
        + _hint(
            "thHint",
            "The tail is exact: availKofN from the availability course, which is the same binomial "
            "upper tail as &ldquo;at least k of n replicas up&rdquo; and is reused rather than "
            "rewritten. No square root and no normal approximation appear on this page.",
        )
    )

    script = _CORE_JS + r"""
  var rateS = document.getElementById('thRate'), nS = document.getElementById('thN');
  var pctS = document.getElementById('thPct'), winSel = document.getElementById('thWin');
  var plot = document.getElementById('thPlot'), table = document.getElementById('thTable');
  var status = document.getElementById('thStatus');

  function redraw() {
    var perMille = +rateS.value, n = +nS.value, pct = +pctS.value, wm = +winSel.value;
    var p = R(BigInt(perMille), 1000n), rate = R(BigInt(pct), 100n);
    document.getElementById('thRateOut').textContent = Rpct(p, 1);
    document.getElementById('thNOut').textContent = n + ' requests';
    document.getElementById('thPctOut').textContent = pct + '%';

    var k = thresholdCount(rate, n);
    var kn = Number(k);
    var q = kn > n ? R(0n, 1n) : falseAlarmProbability(p, k, n);
    var pmf = binomialPmf(p, n), tails = pmf ? pmfUpperTails(pmf) : null;
    var weekWindows = windowsPer(7 * 24 * 60, wm);
    var monthWindows = windowsPer(30 * 24 * 60, wm);
    var pages = expectedPages(q, weekWindows);
    var monthPages = expectedPages(q, monthWindows);
    var perHour = Math.round(60 / wm);
    var hour = atLeastOne(q, perHour);
    var mean = Rmul(p, R(BigInt(n), 1n));

    document.getElementById('thK').innerHTML = kn > n ? 'more than ' + n + ' &mdash; it cannot fire'
      : group(k) + ' errors (&gt; ' + pct + '% of ' + n + ')';
    document.getElementById('thQ').innerHTML = RpctAuto(q);
    document.getElementById('thWindows').textContent = Rfixed(weekWindows, 0) + ' windows';
    document.getElementById('thPages').textContent = Rfixed(pages, 2) + ' pages';
    document.getElementById('thHour').innerHTML = RpctAuto(hour);
    document.getElementById('thMonth').textContent = Rfixed(monthPages, 1) + ' pages';

    var rows = '', j;
    var hi = Math.min(n, Math.max(kn + 4, 10));
    for (j = Math.max(1, kn - 4); j <= hi; j += 1) {
      var tj = tails ? tails[j] : falseAlarmProbability(p, BigInt(j), n);
      rows += '<tr><td class="' + (j === kn ? 'tone-red' : '') + '">' + j + '</td><td>'
        + Rfixed(R(BigInt(j), BigInt(n)), 4) + '</td><td>' + RpctAuto(tj) + '</td><td>'
        + Rfixed(expectedPages(tj, weekWindows), 2) + '</td><td>'
        + (j === kn ? 'the threshold you set' : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>fires at k errors</th><th>k/n</th><th>P(fires by chance)</th>'
      + '<th>false pages a week</th><th></th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">Column three is availKofN(p, k, n), the exact '
      + 'binomial upper tail. The whole distribution is also computed from its neighbour ratio and its '
      + 'suffix sums agree with it'
      + (tails ? ' &mdash; here to the last digit: ' + (Requ(tails[kn], q) ? 'they match exactly'
          : 'they DISAGREE, which is a bug') : '')
      + '.</td></tr></tfoot>';

    var top = R(0n, 1n), lo = Math.max(0, kn - 8), hi2 = Math.min(n, kn + 8), i;
    if (pmf) {
      for (i = lo; i <= hi2; i += 1) if (Rcmp(pmf[i], top) > 0) top = pmf[i];
    }
    var wide = 620 / Math.max(1, hi2 - lo + 1);
    var s = '';
    if (pmf && !Rzero(top)) {
      for (i = lo; i <= hi2; i += 1) {
        var h = Math.max(1, Rplot(Rdiv(pmf[i], top)) * 112);
        var x = 16 + (i - lo) * wide;
        s += '<rect x="' + x + '" y="' + (146 - h) + '" width="' + Math.max(3, wide - 5) + '" height="' + h
          + '" rx="2" fill="var(--' + (i >= kn ? 'red' : 'cyan') + ')" opacity="' + (i >= kn ? '0.9' : '0.6') + '" />'
          + '<text x="' + (x + wide / 2 - 2) + '" y="160" text-anchor="middle" font-size="9" fill="var(--muted)">'
          + i + '</text>';
      }
      var kx = 16 + (Math.max(lo, Math.min(hi2 + 1, kn)) - lo) * wide - 2;
      s += '<line x1="' + kx + '" y1="26" x2="' + kx + '" y2="150" stroke="var(--red)" stroke-width="2" '
        + 'stroke-dasharray="4 3" />'
        + '<text x="' + Math.max(0, Math.min(kx + 5, 420)) + '" y="24" font-size="10" fill="var(--red)" '
        + 'font-weight="700">fires at ' + group(k) + ' or more: ' + RpctAuto(q) + ' of windows</text>';
      var mx = 16 + (Math.max(lo, Math.min(hi2, Rplot(mean))) - lo) * wide + wide / 2;
      s += '<line x1="' + mx + '" y1="118" x2="' + mx + '" y2="150" stroke="var(--amber)" stroke-width="2" />'
        + '<text x="' + Math.max(0, Math.min(mx - 30, 500)) + '" y="180" font-size="10" fill="var(--amber)">'
        + 'the true rate puts ' + Rfixed(mean, 2) + ' errors in a window</text>';
    }
    s += '<line x1="16" y1="150" x2="636" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="16" y="16" font-size="11" fill="var(--muted)">errors in one window of ' + n
      + ' requests, with nothing whatever wrong</text>';
    plot.innerHTML = s;

    status.innerHTML = kn > n
      ? 'A threshold of ' + pct + '% needs more than ' + n + ' errors in a window of ' + n
        + ' requests, so it can never fire &mdash; which is its own kind of broken alert.'
      : 'The service is behaving exactly to specification at <strong>' + Rpct(p, 1) + '</strong>, so a window '
        + 'of ' + n + ' requests holds <strong>' + Rfixed(mean, 2) + '</strong> errors on average. The '
        + 'threshold fires at <strong>' + group(k) + '</strong>, which happens by chance in <strong>'
        + RpctAuto(q) + '</strong> of windows. At ' + wm + '-minute windows that is <strong>'
        + Rfixed(pages, 1) + ' pages a week</strong> and ' + Rfixed(monthPages, 0) + ' in a 30-day month, '
        + 'with nothing to find in any of them. The chance of at least one in the next hour alone is '
        + RpctAuto(hour) + ' &mdash; <span class="tone-muted">1 &minus; (1&minus;q)&#7503; again, the same '
        + 'function the sampling and load-test lessons call.</span> A threshold is a statement about the '
        + 'sample, not about the system: raise k, lengthen the window so n grows, or alert on the budget '
        + 'burn rate, which asks how much of a month this is costing rather than what one window did.';
  }

  [rateS, nS, pctS].forEach(function (el) { el.addEventListener('input', redraw); });
  winSel.addEventListener('change', redraw);
  rateS.value = """ + str(per_mille) + r"""; nS.value = """ + str(window_n) + r""";
  pctS.value = """ + str(threshold_pct) + r"""; winSel.value = '""" + window_minutes + r"""';
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A threshold fires on the sample, not on the system",
        subtitle="The exact chance a healthy service trips a fixed threshold, and the pages it costs",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the rate, the window and the threshold"),
        panel_intro=cfg.get(
            "panel_intro",
            "Nothing is wrong in this model: the error rate is exactly what you set. Every page the "
            "threshold produces here is a false one, and the binomial tail counts them exactly.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "sli": _sli,
    "aggregate": _aggregate,
    "histogram": _histogram,
    "omission": _omission,
    "scrape": _scrape,
    "sample": _sample,
    "cardinality": _cardinality,
    "loadtest": _loadtest,
    "burn": _burn,
    "threshold": _threshold,
}

MODES = tuple(sorted(_MODES))


def measure_lab(cfg):
    """Course 10's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, not defensiveness. A kit that quietly fell back
    to a default would render a finished-looking page carrying another lesson's
    widget: the markup assertions pass, labcheck passes, and the reader is
    shown the wrong lesson's arithmetic under the right lesson's title. On a
    course about how measurements mislead, that failure would be particularly
    hard to argue with.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "measure_lab: unknown mode %r; the ten modes of course 10 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["measure_lab", "MEASURE_JS", "MODES"]
