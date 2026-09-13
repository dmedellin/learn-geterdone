"""Course 9 of System Design: scaling laws, capacity and what it costs.

Thirteen modes, eleven lessons, and one claim underneath all of them: the next
machine buys less than a machine, the next month costs more than this one, and
both shortfalls are ratios of integers you can check rather than rules of thumb
you have to trust.

FOUR DECISIONS RUN THROUGH THE KIT.

  THE UNIVERSAL SCALABILITY LAW TURNS OVER, AND THE TURN IS EXACT. A reader who
  has only met Amdahl expects a plateau. C(N) = N/(1 + a(N-1) + bN(N-1)) does
  not plateau: past a peak it FALLS, and the next machine is actively harmful.
  The peak is found here by an exact integer predicate rather than by a root --

      C(N+1) <= C(N)   <=>   b*N*(N+1) >= 1 - a

  which is the same algebra as N* = sqrt((1-a)/b) with the square root taken
  out of it. So `uslPeakExact` is a search over integers with no rounding
  anywhere, `uslPeakRootApprox` is the familiar root printed rounded BESIDE it,
  and a mathcheck case asserts the curve really descends at the N they agree on.
  A coherency term quietly dropped would make the curve monotone, every figure
  on the page would still look plausible, and that assertion is what fails.

  RHO IS rho = lambda/mu, AND IT IS THE SAME rho COURSE 3 USES. `autoscale` and
  `headroom` are utilisation lessons wearing a cost hat, and both compute
  utilisation exactly as `queue`'s lesson 1 does -- demand over the capacity
  that is actually in service -- rather than inventing a second definition that
  would disagree with it by the width of a boot window. Both pages therefore
  also print course 3's two consequences: above rho = 1 there is no steady
  state and the backlog grows at lambda - mu per second, and below it the
  response time multiplier is 1/(1 - rho). Losing one of N machines is not a
  small change to rho; it multiplies it by N/(N-1), and at rho = 0.9 with ten
  machines that lands exactly on 1.

  EXACT UNLESS THE LESSON IS ABOUT AN APPROXIMATION, and then labelled. Three
  places round, each on its own face:

    * `usl` prints sqrt((1-a)/b) rounded by Newton (`sqrtApprox`) as a GLOSS on
      the exact integer peak beside it, never in place of it;
    * `growth` prints log(limit/current)/log(1+r) rounded (`logApprox`) as a
      gloss on the exact month, which is an integer search over Rpow;
    * `batch` states that B/lambda is the rule of thumb and computes the two
      exact waits -- (B-1)/lambda for the first item, (B-1)/(2*lambda) on
      average -- beside it, so the reader can see the rule overstate by 1/lambda.

  Everything else, including every break-even on the second half of the course,
  is a crossing of exact fractions. That is what makes a break-even a place
  rather than a decimal.

  A BREAK-EVEN IS AN EQUALITY BEFORE IT IS AN OPINION. Each of the six on this
  course is solved as an equation and then located by an exact comparison:

    reserved vs on-demand   u* = reserved/on-demand, and the optimal reserved
                            level is the smallest level whose hours-above share
                            has fallen to u* -- a marginal argument, exact
    spot vs on-demand       q* = (on-demand - spot)/on-demand
    cold vs hot storage     a* = (hot - cold)/retrieval accesses per GB-month
    compress vs send        bw* = rate*(k-1)/k, i.e. rate > bw*k/(k-1) -- and
                            with the far end's decompression counted, the same
                            equality with 1/(k*drate) added to the per-byte cost
    data vs compute         (code + result) against the dataset, with the
                            bandwidth cancelling out of the comparison entirely
    fixed vs egress         V* = fixed / egress-per-request

The modes, and the lesson each belongs to:

  amdahl     L1   S(n), its ceiling 1/(1-p), and the n reaching 90% of it
  usl        L2   the exact integer peak, the turnover, and the rounded root
  batch      L3   F/B + v falling against the fill wait rising
  vertical   L4   N small machines with coordination against one big price rung
  waste      L5   1 - mean*rho/peak over a 24-bucket day
  reserve    L6   u*, the optimal reserved level, and spot's interruption model
  autoscale  L7   r*tau*(D - tau/2) as a trapezoid, and the reserve that voids it
  unit       L8   compute + storage + egress per request, and which one wins
  tier       L9   (hot - cold)/retrieval, and the age it is reached at
  compress   L10  both transfer times and the break-even bandwidth
  placement  L11  D/bw against (code + result)/bw, and the result ratio
  headroom   --   rho after losing f of N, which is rho*N/(N-f)
  growth     --   the month a compounding load reaches a limit, by integer search

`headroom` and `growth` are not in the eleven-lesson table; they are the two
figures the course's outcomes name that no other mode computes -- N-1 capacity
after a failure, and the month a plan runs out -- and they are modes rather
than views of `waste` and `unit` because a view selected by an unvalidated key
is the defect the unknown-mode rule exists to prevent.
"""

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal
from .sysdesign_core import APPROX_JS, RCEIL_JS

SCALE_JS = r"""
  /* ======================== printing an exact rational ======================

     algebra_core's Rdec goes through Number(a.n)/Number(a.d). This course
     produces rationals a double cannot hold at either end: a monthly growth
     factor raised to the 60th month is a 60-digit numerator over a 60-digit
     denominator, and Number() of that pair is Infinity/Infinity. Every decimal
     printed here is therefore long division in BigInt, rounded half up at the
     last digit shown, and exact up to that one rounding at any size. */
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
  /* Digit grouping that stops at the decimal point. counting.py's group() does
     not: it would turn 1234567.89 into 1 234 567.89 only by accident. */
  function groupDec(text) {
    var dot = text.indexOf('.');
    var whole = dot < 0 ? text : text.slice(0, dot), rest = dot < 0 ? '' : text.slice(dot);
    var sign = '';
    if (whole.charAt(0) === '-') { sign = '-'; whole = whole.slice(1); }
    return sign + whole.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + rest;
  }
  function Rtrim(text) {
    if (text.indexOf('.') < 0) return text;
    return text.replace(/0+$/, '').replace(/\.$/, '');
  }
  function Rnice(a, places) { return groupDec(Rtrim(Rfixed(a, places === undefined ? 2 : places))); }
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 1 : places) + '%';
  }
  /* The exact fraction while a reader can read it, a decimal once it has run
     to twenty digits. Both are the same number; only one is evidence. */
  function Rshort(a, places, digits) {
    if (digits === undefined) digits = 9;
    var wide = String(a.n < 0n ? -a.n : a.n).length > digits || String(a.d).length > digits;
    return wide ? Rfixed(a, places === undefined ? 4 : places) : Rtext(a);
  }
  function Rtextg(a) {
    var w = groupDec(a.n.toString());
    return a.d === 1n ? w : w + '/' + groupDec(a.d.toString());
  }
  /* Money, at the number of places the size of the figure calls for. A unit
     cost of nine millionths of a dollar printed to two places is $0.00, which
     is how a cost lesson loses the term it is about. */
  function money(a) {
    var m = Rabs(a), places;
    if (Rcmp(m, R(1000n, 1n)) >= 0) places = 0;
    else if (Rcmp(m, R(1n, 1n)) >= 0) places = 2;
    else if (Rcmp(m, R(1n, 1000n)) >= 0) places = 5;
    else places = 8;
    return '$' + groupDec(Rfixed(a, places));
  }
  function moneyAt(a, places) { return '$' + groupDec(Rfixed(a, places)); }

  /* ---- pixels only ------------------------------------------------------

     log10Approx and ratioApprox exist so a bar can be POSITIONED at a size
     Number cannot divide. Nothing they return is ever printed as a figure. */
  function log10Approx(a) {
    if (a.n <= 0n) return NaN;
    var n = a.n, d = a.d, shift = 0, cap = 1000000000000000n;
    while (n > cap) { n /= 10n; shift += 1; }
    while (d > cap) { d /= 10n; shift -= 1; }
    return shift + Math.log10(Number(n) / Number(d));
  }
  function ratioApprox(a, b) {
    if (Rzero(b)) return NaN;
    if (Rzero(a)) return 0;
    var q = Rdiv(a, b), sign = 1;
    if (q.n < 0n) { q = R(-q.n, q.d); sign = -1; }
    return sign * Math.pow(10, log10Approx(q));
  }
  var SUPERSCRIPT = ['⁰', '¹', '²', '³', '⁴', '⁵',
                     '⁶', '⁷', '⁸', '⁹'];
  function supNum(v) {
    var s = Math.abs(v).toString(), out = '';
    for (var i = 0; i < s.length; i += 1) out += SUPERSCRIPT[+s.charAt(i)];
    return (v < 0 ? '⁻' : '') + out;
  }
  function powTen(e) { return '10' + supNum(e); }

  /* Decimal units throughout: a GB is 10^9 bytes, because a link and a disk
     are both sold in decimal and mixing the two is a silent 7% error. */
  var GB = 1000000000n;
  var BYTE_UNITS = [['PB', 1000000000000000n], ['TB', 1000000000000n], ['GB', 1000000000n],
                    ['MB', 1000000n], ['kB', 1000n], ['B', 1n]];
  function fmtBytes(a, places) {
    for (var i = 0; i < BYTE_UNITS.length; i += 1) {
      if (i === BYTE_UNITS.length - 1 || Rcmp(Rabs(a), R(BYTE_UNITS[i][1], 1n)) >= 0) {
        return Rnice(Rdiv(a, R(BYTE_UNITS[i][1], 1n)), places === undefined ? 2 : places)
          + ' ' + BYTE_UNITS[i][0];
      }
    }
  }
  /* The ladder every "how big is it" slider runs on: a 1, 1.5, 2, 3, 5, 7 rung
     in each decade, so a slider INDEX is an exact rational and every worked
     example on the course lands on a rung rather than near one. */
  var LADDER_MANT = [[1n, 1n], [3n, 2n], [2n, 1n], [3n, 1n], [5n, 1n], [7n, 1n]];
  function ladderValue(i) {
    if (i < 0) i = 0;
    var m = LADDER_MANT[i % 6], e = Math.floor(i / 6);
    return Rmul(R(m[0], m[1]), Rpow(R(10n, 1n), e));
  }
  function ladderIndex(mantIdx, decade) { return decade * 6 + mantIdx; }

  function fmtSecs(a) {
    if (Rcmp(Rabs(a), R(1n, 1n)) < 0) return Rnice(Rmul(a, R(1000n, 1n)), 1) + ' ms';
    if (Rcmp(Rabs(a), R(3600n, 1n)) >= 0) return Rnice(Rdiv(a, R(3600n, 1n)), 2) + ' h';
    if (Rcmp(Rabs(a), R(120n, 1n)) >= 0) return Rnice(Rdiv(a, R(60n, 1n)), 2) + ' min';
    return Rnice(a, 2) + ' s';
  }

  /* ======================= L1: Amdahl's Law ================================

     S(n) = 1/((1-p) + p/n). The serial share (1-p) never shrinks, so S(n)
     climbs to 1/(1-p) and stops: five per cent serial caps the speedup at
     twenty, and the twenty-first machine is not the problem -- the two hundred
     and first buys the same nothing. */
  function amdahlSpeedup(p, n) {
    var one = R(1n, 1n);
    return Rinv(Radd(Rsub(one, p), Rdiv(p, R(BigInt(n), 1n))));
  }
  /* The ceiling, which is the asymptote the curve never reaches. p = 1 has no
     ceiling; the page says so rather than dividing by zero. */
  function amdahlCeiling(p) {
    var free = Rsub(R(1n, 1n), p);
    return Rzero(free) ? null : Rinv(free);
  }
  /* The smallest n reaching a fraction f of the ceiling, by exact scan. This
     is the number the lesson asserts. */
  function amdahlReach(p, f, limit) {
    var ceiling = amdahlCeiling(p);
    if (ceiling === null) return null;
    var want = Rmul(f, ceiling);
    for (var n = 1; n <= limit; n += 1) {
      if (Rcmp(amdahlSpeedup(p, n), want) >= 0) return n;
    }
    return null;
  }
  /* The same n in closed form, exactly: S(n) >= f/(1-p) rearranges to
     n >= (f/(1-f)) * (p/(1-p)), and the ceiling of THAT is an integer with no
     rounding in it. Printed beside the scan as the check the lesson asks for.
     At f = 9/10 it is the familiar 9p/(1-p). */
  function amdahlReachClosed(p, f) {
    var one = R(1n, 1n);
    if (Rzero(Rsub(one, f)) || Rzero(Rsub(one, p))) return null;
    return Number(Rceil(Rmul(Rdiv(f, Rsub(one, f)), Rdiv(p, Rsub(one, p)))));
  }
  /* Efficiency: what fraction of the machines you bought is doing work. The
     misconception is that it stays at 1, and it is S(n)/n. */
  function amdahlEfficiency(p, n) { return Rdiv(amdahlSpeedup(p, n), R(BigInt(n), 1n)); }
  /* What the reader expected: n machines, n times faster. */
  function linearSpeedup(n) { return R(BigInt(n), 1n); }

  /* ======================= L2: the Universal Scalability Law ===============

     C(N) = N/(1 + a(N-1) + bN(N-1)) in units of one machine's throughput. The
     contention term a is Amdahl wearing different clothes -- with b = 0 the
     curve rises to 1/a and PLATEAUS. The coherency term b is what makes it
     turn over: every pair of machines must agree, there are N(N-1) ordered
     pairs, and past a point that cost grows faster than the work does. */
  function uslThroughput(N, alpha, beta) {
    var one = R(1n, 1n), Nn = R(BigInt(N), 1n), Nm = R(BigInt(N - 1), 1n);
    var den = Radd(one, Radd(Rmul(alpha, Nm), Rmul(beta, Rmul(Nn, Nm))));
    return Rzero(den) ? null : Rdiv(Nn, den);
  }
  /* THE EXACT PEAK, with no square root in it.

     C(N+1) <= C(N) reduces to (1-a) <= b*N*(N+1) -- expand both denominators
     and everything but that cancels. So the peak is the smallest N at which
     the coherency cost of one more pair has caught the parallel work up, and
     it is an integer search over exact fractions. b = 0 has no peak, which is
     exactly the Amdahl case, and the function returns null rather than a
     largest-so-far that a longer scan would have moved. */
  function uslBeyondPeak(N, alpha, beta) {
    return Rcmp(Rmul(beta, R(BigInt(N) * BigInt(N + 1), 1n)), Rsub(R(1n, 1n), alpha)) >= 0;
  }
  function uslPeakExact(alpha, beta, limit) {
    if (Rzero(beta)) return null;
    for (var N = 1; N <= limit; N += 1) if (uslBeyondPeak(N, alpha, beta)) return N;
    return null;
  }
  /* The same peak the slow way, as the argmax of the scan. The two must agree,
     and mathcheck asserts they do at every (a, b) it tries. */
  function uslPeakScan(alpha, beta, limit) {
    var best = null, bestN = 0;
    for (var N = 1; N <= limit; N += 1) {
      var c = uslThroughput(N, alpha, beta);
      if (c !== null && (best === null || Rcmp(c, best) > 0)) { best = c; bestN = N; }
    }
    return { N: bestN, value: best, interior: bestN < limit };
  }
  /* The familiar closed form, which is a square root and therefore ROUNDS --
     hence the name. It is printed beside the exact peak as a check on it and
     never in its place: the integer search is what the page asserts, and
     sqrt((1-a)/b) is the explanation of why that integer is where it is. */
  function uslPeakRootApprox(alpha, beta) {
    if (Rzero(beta)) return Infinity;
    return sqrtApprox(Rdiv(Rsub(R(1n, 1n), alpha), beta), 1e-15);
  }
  /* Amdahl's ceiling of the same curve: with b = 0, C(N) -> 1/a. Printed so a
     reader can see which term is doing which job. */
  function uslContentionCeiling(alpha) { return Rzero(alpha) ? null : Rinv(alpha); }
  function uslCurve(alpha, beta, maxN) {
    var out = [];
    for (var N = 1; N <= maxN; N += 1) out.push(uslThroughput(N, alpha, beta));
    return out;
  }
  /* How much of the peak is left at N, so the page can say "at twice the peak
     you have thrown away a third of it" with a fraction rather than a shrug. */
  function uslRetained(N, alpha, beta, peakN) {
    var here = uslThroughput(N, alpha, beta), top = uslThroughput(peakN, alpha, beta);
    return (here === null || top === null || Rzero(top)) ? null : Rdiv(here, top);
  }

  /* ======================= L3: batching ====================================

     Per-item cost F/B + v falls with the batch and the fill wait rises with
     it, so there is no B that is best at both. The cost curve is a hyperbola
     and flattens: the whole saving between B and infinity is F/B, so once the
     fixed share has fallen below a stated fraction of v there is nothing left
     to buy with latency. */
  function perItemCost(F, v, B) { return Radd(Rdiv(F, R(BigInt(B), 1n)), v); }
  function fixedShare(F, v, B) {
    var total = perItemCost(F, v, B);
    return Rzero(total) ? null : Rdiv(Rdiv(F, R(BigInt(B), 1n)), total);
  }
  /* The smallest B whose fixed share has fallen to k times the variable cost.
     F/B <= k*v rearranges to B >= F/(k*v), and its ceiling is exact. */
  function batchForFixedShare(F, v, k) {
    if (Rzero(v) || Rzero(k)) return null;
    return Number(Rceil(Rdiv(F, Rmul(k, v))));
  }
  /* The waits, all three exact.

     The first item of a batch waits for B-1 more arrivals; the average item
     waits half that. B/lambda is the rule of thumb the lesson states, and it
     overstates the first item's wait by exactly 1/lambda -- one inter-arrival
     time, whatever B is, which is why it is a usable rule and still not the
     number. */
  function batchWaitFirst(B, lam) { return Rdiv(R(BigInt(B - 1), 1n), lam); }
  function batchWaitMean(B, lam) { return Rdiv(R(BigInt(B - 1), 1n), Rmul(R(2n, 1n), lam)); }
  function batchWaitRule(B, lam) { return Rdiv(R(BigInt(B), 1n), lam); }
  /* A timer caps the wait and therefore caps the batch: in T seconds only
     lambda*T items can arrive, so a B beyond that is never reached and the
     flush is partial. floor, because a partial arrival is not an item. */
  function batchUnderTimer(B, lam, T) {
    var reach = Number(Rfloor(Rmul(lam, T)));
    if (reach < 1) reach = 1;
    return { effective: reach < B ? reach : B, capped: reach < B, reach: reach };
  }

  /* ======================= L4: vertical against horizontal =================

     Horizontal capacity is NOT N times a machine. N machines coordinate, and
     the coordination is the same contention term the Universal Scalability Law
     names -- so this mode calls uslThroughput with b = 0 rather than inventing
     a second overhead model that would disagree with lesson 2 by construction.
     Vertical capacity is a ladder of rungs, each twice the last, at a price
     that is more than twice the last: the premium per doubling is what makes
     the curve superlinear and is the thing the reader edits. */
  function horizontalNodes(targetUnits, alpha, limit) {
    var want = R(BigInt(targetUnits), 1n);
    for (var N = 1; N <= limit; N += 1) {
      var c = uslThroughput(N, alpha, R(0n, 1n));
      if (c !== null && Rcmp(c, want) >= 0) return N;
    }
    return null;                      /* 1/a is a ceiling on the fleet too */
  }
  function horizontalCost(N, unitPrice) { return Rmul(R(BigInt(N), 1n), unitPrice); }
  /* The rung that holds the target: 2^k >= target, found by doubling, not by
     a logarithm. You cannot buy a fraction of a machine size. */
  function verticalRung(targetUnits) {
    var k = 0, cap = 1;
    while (cap < targetUnits) { cap *= 2; k += 1; }
    return { rung: k, units: cap };
  }
  /* Price of rung k: base * (2*premium)^k. premium = 1 is linear in capacity,
     and every real price ladder is above it. */
  function verticalCost(targetUnits, basePrice, premium) {
    var r = verticalRung(targetUnits);
    return Rmul(basePrice, Rpow(Rmul(R(2n, 1n), premium), r.rung));
  }
  /* Which plan is cheaper at a target, as an exact comparison of two exact
     prices. STRICTLY cheaper: at one unit of capacity the two plans ARE the
     same machine at the same price, and a break-even reported at a tie is a
     crossing the curves have not made. A target horizontal cannot reach at all
     -- 1/a is a ceiling on a fleet exactly as it is on a program -- counts as
     a vertical win, because it is one. */
  function horizontalWinsAt(t, basePrice, unitPrice, premium, alpha, nodeLimit) {
    var N = horizontalNodes(t, alpha, nodeLimit);
    if (N === null) return false;
    return Rcmp(horizontalCost(N, unitPrice), verticalCost(t, basePrice, premium)) < 0;
  }
  /* THE BREAK-EVEN IS NOT THE FIRST CROSSING, because the vertical ladder is a
     staircase. A rung you have just bought is cheap until it is full, so
     horizontal can win at one target and lose at the next. Two figures, and
     the page prints both: the first target horizontal wins at, and the target
     past which it never loses again. The gap between them IS "you buy the next
     size up", priced. */
  function shapeFirstCrossing(basePrice, unitPrice, premium, alpha, maxUnits, nodeLimit) {
    for (var t = 1; t <= maxUnits; t += 1) {
      if (horizontalWinsAt(t, basePrice, unitPrice, premium, alpha, nodeLimit)) return t;
    }
    return null;
  }
  function shapeBreakEven(basePrice, unitPrice, premium, alpha, maxUnits, nodeLimit) {
    var lastVerticalWin = 0;
    for (var t = 1; t <= maxUnits; t += 1) {
      if (!horizontalWinsAt(t, basePrice, unitPrice, premium, alpha, nodeLimit)) lastVerticalWin = t;
    }
    return lastVerticalWin >= maxUnits ? null : lastVerticalWin + 1;
  }

  /* ======================= L5: utilisation and waste =======================

     You pay for peak/rho_target and you use the mean, so the waste is
     1 - mean*rho/peak. The misconception is arithmetic rather than conceptual:
     "thirty per cent used, so cut seventy per cent" cuts the capacity the peak
     hour needs, and the page computes how many hours would then be over. */
  function paidCapacity(peak, rhoTarget) {
    return Rzero(rhoTarget) ? null : Rdiv(peak, rhoTarget);
  }
  function wasteFraction(mean, peak, rhoTarget) {
    if (Rzero(peak)) return null;
    return Rsub(R(1n, 1n), Rdiv(Rmul(mean, rhoTarget), peak));
  }
  function profileStats(buckets) {
    var total = R(0n, 1n), peak = buckets[0], at = 0, trough = buckets[0];
    for (var h = 0; h < buckets.length; h += 1) {
      total = Radd(total, buckets[h]);
      if (Rcmp(buckets[h], peak) > 0) { peak = buckets[h]; at = h; }
      if (Rcmp(buckets[h], trough) < 0) trough = buckets[h];
    }
    var mean = Rdiv(total, R(BigInt(buckets.length), 1n));
    return {
      total: total, peak: peak, peakAt: at, trough: trough, mean: mean,
      peakToMean: Rzero(mean) ? null : Rdiv(peak, mean)
    };
  }
  /* How many hours a given capacity fails to cover, and by how much at worst.
     This is what "cut seventy per cent" actually buys. */
  function hoursOver(buckets, capacity) {
    var count = 0, worst = R(0n, 1n);
    for (var h = 0; h < buckets.length; h += 1) {
      if (Rcmp(buckets[h], capacity) > 0) {
        count += 1;
        var gap = Rsub(buckets[h], capacity);
        if (Rcmp(gap, worst) > 0) worst = gap;
      }
    }
    return { hours: count, worst: worst };
  }
  /* The shape of a day, as INTEGER weights, so the total is an exact multiple
     of the base and no bucket is a rounded share of a total. */
  function dayShape(shape, peakHour, amp) {
    var w = [], h, dist, far;
    for (h = 0; h < 24; h += 1) {
      dist = Math.abs(h - peakHour); if (dist > 12) dist = 24 - dist;
      far = Math.abs(h - ((peakHour + 12) % 24)); if (far > 12) far = 24 - far;
      if (shape === 'flat') w.push(12);
      else if (shape === 'evening') w.push(12 + amp * Math.max(0, 6 - dist));
      else if (shape === 'office') w.push(12 + amp * Math.max(0, 5 - dist) + amp * Math.max(0, 3 - far));
      else if (shape === 'batchwindow') w.push(dist <= 1 ? 12 + amp * 10 : 12);
      else if (shape === 'weekendish') w.push(12 + amp * Math.max(0, 8 - dist) / 2);
      else throw new Error('unknown day shape: ' + shape);
    }
    return w;
  }

  /* ======================= L6: reserved, on-demand, spot ===================

     The break-even utilisation is the reserved price over the on-demand price:
     a reserved unit is paid for every hour whether or not it runs, so it pays
     exactly when it runs more than r/d of the time.

     The optimal reserved LEVEL follows from the same marginal argument and is
     exact. Raising the level by one unit costs 24r a day and saves d for each
     hour the profile is above it, so the level is worth raising while

         (hours above)/24 > r/d = u*

     which makes the optimum a quantile of the profile, not its mean and not
     its peak. cost() is evaluated at every integer level as well, and the two
     agree -- a marginal rule and a total both computed, because the rule is
     the lesson and the total is the check. */
  function breakEvenUtilisation(reservedPrice, onDemandPrice) {
    return Rzero(onDemandPrice) ? null : Rdiv(reservedPrice, onDemandPrice);
  }
  function mixCost(buckets, level, reservedPrice, onDemandPrice) {
    var lv = R(BigInt(level), 1n);
    var reserved = Rmul(Rmul(lv, R(BigInt(buckets.length), 1n)), reservedPrice);
    var burst = R(0n, 1n);
    for (var h = 0; h < buckets.length; h += 1) {
      if (Rcmp(buckets[h], lv) > 0) burst = Radd(burst, Rsub(buckets[h], lv));
    }
    return { total: Radd(reserved, Rmul(burst, onDemandPrice)),
             reservedCost: reserved, burstUnits: burst,
             burstCost: Rmul(burst, onDemandPrice) };
  }
  function hoursAbove(buckets, level) {
    var lv = R(BigInt(level), 1n), c = 0;
    for (var h = 0; h < buckets.length; h += 1) if (Rcmp(buckets[h], lv) > 0) c += 1;
    return c;
  }
  /* The level by the marginal rule: raise while the share of hours above the
     level still exceeds u*. Exact, and it never evaluates a total. */
  function reserveLevelMarginal(buckets, reservedPrice, onDemandPrice) {
    var u = breakEvenUtilisation(reservedPrice, onDemandPrice);
    if (u === null) return 0;
    var n = buckets.length, level = 0;
    while (Rcmp(R(BigInt(hoursAbove(buckets, level)), BigInt(n)), u) > 0) level += 1;
    return level;
  }
  /* The level by exhaustive search over every integer level up to the peak.
     Same answer, different route. */
  function reserveLevelSearch(buckets, reservedPrice, onDemandPrice, maxLevel) {
    var best = null, bestLevel = 0;
    for (var lv = 0; lv <= maxLevel; lv += 1) {
      var c = mixCost(buckets, lv, reservedPrice, onDemandPrice).total;
      if (best === null || Rcmp(c, best) < 0) { best = c; bestLevel = lv; }
    }
    return { level: bestLevel, cost: best };
  }
  /* SPOT NEEDS AN INTERRUPTION MODEL, or it is just a cheaper price.

     A spot unit is paid for whatever happens; with probability q the hour is
     reclaimed and the work it owed must be bought on demand instead. So the
     expected price of a DELIVERED unit-hour is s + q*d, spot beats on-demand
     exactly while q < (d - s)/d, and a discount of ninety per cent is worth
     nothing at an interruption rate above ninety per cent. */
  function spotExpectedPrice(spotPrice, onDemandPrice, q) {
    return Radd(spotPrice, Rmul(q, onDemandPrice));
  }
  function spotBreakEvenRate(spotPrice, onDemandPrice) {
    if (Rzero(onDemandPrice)) return null;
    return Rdiv(Rsub(onDemandPrice, spotPrice), onDemandPrice);
  }
  function spotWorthIt(spotPrice, onDemandPrice, q) {
    return Rcmp(spotExpectedPrice(spotPrice, onDemandPrice, q), onDemandPrice) < 0;
  }

  /* ======================= L7: autoscaling lag =============================

     Instances take tau seconds to boot, so a fleet tracking a ramp of r units
     a second is always r*tau units behind. The shortfall is the area between
     demand and capacity, and with no reserve held it is the trapezoid

         r*tau*(D - tau/2)

     -- a triangle of r*tau^2/2 while the ramp and the lag overlap, then a
     rectangle of r*tau for the rest of the ramp. A reserve of h units eats
     into it from below and removes it entirely at h = r*tau, which is the
     lesson: autoscaling does not handle a spike, a reserve does, and the
     reserve you need is the ramp rate times the boot time.

     RHO IS COURSE 3'S RHO. Capacity in service during the boot window is the
     old fleet, demand is the new load, and their ratio is lambda/mu exactly as
     `queue` lesson 1 defines it -- so the same two consequences hold and the
     page prints them: above 1 there is no steady state and the backlog grows
     at lambda - mu per second, and the shortfall area IS that backlog. */
  function autoscaleShortfall(rampRate, tau, duration, reserve) {
    var zero = R(0n, 1n);
    var m = Rcmp(tau, duration) <= 0 ? tau : duration;         /* min(tau, D) */
    var atM = Rsub(Rmul(rampRate, m), reserve);
    var triangle = zero;
    if (Rcmp(atM, zero) > 0 && !Rzero(rampRate)) {
      triangle = Rdiv(Rmul(atM, atM), Rmul(R(2n, 1n), rampRate));
    }
    var lagDeficit = Rsub(Rmul(rampRate, tau), reserve);
    if (Rcmp(lagDeficit, zero) < 0) lagDeficit = zero;
    var flat = zero;
    if (Rcmp(duration, tau) > 0) flat = Rmul(Rsub(duration, tau), lagDeficit);
    return { area: Radd(triangle, flat), triangle: triangle, rectangle: flat,
             peakDeficit: lagDeficit };
  }
  /* The closed form the lesson states, which holds when no reserve is held and
     the ramp outlasts the boot. Printed beside the general area as its check. */
  function autoscaleTrapezoid(rampRate, tau, duration) {
    return Rmul(Rmul(rampRate, tau), Rsub(duration, Rdiv(tau, R(2n, 1n))));
  }
  function autoscaleReserveNeeded(rampRate, tau) { return Rmul(rampRate, tau); }
  /* Demand and capacity at t, in units. Capacity is the base fleet plus the
     reserve, and it only starts growing once the boot window has passed. */
  function autoscaleDemand(base, rampRate, duration, t) {
    var elapsed = Rcmp(t, duration) < 0 ? t : duration;
    return Radd(base, Rmul(rampRate, elapsed));
  }
  function autoscaleCapacity(base, reserve, rampRate, tau, duration, t) {
    var zero = R(0n, 1n);
    var behind = Rsub(t, tau);
    if (Rcmp(behind, zero) < 0) behind = zero;
    if (Rcmp(behind, duration) > 0) behind = duration;
    return Radd(Radd(base, reserve), Rmul(rampRate, behind));
  }
  /* rho = lambda/mu. The same ratio of two rates queue lesson 1 computes, and
     the reason this page can quote 1/(1 - rho) and the backlog growth rate
     without deriving either one again. */
  function rhoAt(demand, capacity) { return Rzero(capacity) ? null : Rdiv(demand, capacity); }
  function backlogGrowth(demand, capacity) {
    var gap = Rsub(demand, capacity);
    return Rcmp(gap, R(0n, 1n)) > 0 ? gap : R(0n, 1n);
  }
  /* W/S = 1/(1 - rho): course 3 lesson 8's hyperbola, quoted here because the
     cost of a boot window is not only the work that missed, it is what the
     work that did not miss waited. Null at or above rho = 1, where there is no
     steady state to ask about. */
  function responseFactor(rho) {
    var free = Rsub(R(1n, 1n), rho);
    return Rcmp(free, R(0n, 1n)) <= 0 ? null : Rinv(free);
  }

  /* ======================= L8: cost per request ============================

     Three terms, and they do not behave alike. The fixed term falls with
     volume; the compute, storage and egress terms are flat per request and do
     not care how many requests there are. So "cost scales with users" is
     wrong twice over: the TOTAL rises linearly and the UNIT cost falls, and
     the term that ends up dominating is nearly always the one nobody sized --
     bytes leaving the building.

     Storage accrues with retention rather than with traffic: a request stored
     for R months occupies its bytes for R months, so its share of the storage
     bill is bytes * R * price, with the volume cancelling out. */
  function computePerRequest(fixedMonthly, variablePerRequest, volume) {
    if (Rzero(volume)) return null;
    return Radd(Rdiv(fixedMonthly, volume), variablePerRequest);
  }
  function storagePerRequest(bytesPerRequest, retentionMonths, pricePerGbMonth) {
    return Rdiv(Rmul(Rmul(bytesPerRequest, retentionMonths), pricePerGbMonth), R(GB, 1n));
  }
  function egressPerRequest(bytesOut, pricePerGb) {
    return Rdiv(Rmul(bytesOut, pricePerGb), R(GB, 1n));
  }
  function unitCost(cfg, volume) {
    var fixedShareOf = Rzero(volume) ? null : Rdiv(cfg.fixedMonthly, volume);
    var compute = cfg.variablePerRequest;
    var storage = storagePerRequest(cfg.bytesPerRequest, cfg.retentionMonths, cfg.storagePrice);
    var egress = egressPerRequest(cfg.bytesOut, cfg.egressPrice);
    if (fixedShareOf === null) return null;
    var total = Radd(Radd(fixedShareOf, compute), Radd(storage, egress));
    return { fixed: fixedShareOf, compute: compute, storage: storage, egress: egress,
             total: total, monthly: Rmul(total, volume) };
  }
  /* The volume at which the fixed term stops being the biggest one: the
     crossing with whichever flat term is largest. An equality, solved. */
  function fixedCrossing(fixedMonthly, perRequestTerm) {
    return Rzero(perRequestTerm) ? null : Rdiv(fixedMonthly, perRequestTerm);
  }
  function dominantTerm(parts) {
    var names = ['fixed', 'compute', 'storage', 'egress'], best = names[0];
    for (var i = 1; i < names.length; i += 1) {
      if (Rcmp(parts[names[i]], parts[best]) > 0) best = names[i];
    }
    return best;
  }

  /* ======================= L9: storage tiers ===============================

     A GB costs hot - cold less in the cold tier every month and costs
     retrieval per access to read. So the break-even access rate is

         a* = (hot - cold) / retrieval    accesses per GB per month

     and "everything old should go cold" is only true where the access rate has
     fallen below it. The age profile is geometric: accesses at age k are the
     age-zero rate times decay^k, exact through Rpow, so the break-even AGE is
     an exact integer search and not a curve read off by eye. */
  function tierBreakEvenAccesses(hotPrice, coldPrice, retrievalPrice) {
    if (Rzero(retrievalPrice)) return null;
    return Rdiv(Rsub(hotPrice, coldPrice), retrievalPrice);
  }
  function accessesAtAge(baseAccesses, decay, age) {
    return Rmul(baseAccesses, Rpow(decay, age));
  }
  function tierBreakEvenAge(baseAccesses, decay, hotPrice, coldPrice, retrievalPrice, maxAge) {
    var target = tierBreakEvenAccesses(hotPrice, coldPrice, retrievalPrice);
    if (target === null) return null;
    for (var age = 0; age <= maxAge; age += 1) {
      if (Rcmp(accessesAtAge(baseAccesses, decay, age), target) <= 0) return age;
    }
    return null;
  }
  /* The monthly bill for one age bucket on each tier. Cold is cheaper to keep
     and charges for every read; hot charges for neither. */
  function tierCost(gb, accesses, hotPrice, coldPrice, retrievalPrice, cold) {
    var keep = Rmul(gb, cold ? coldPrice : hotPrice);
    var read = cold ? Rmul(Rmul(gb, accesses), retrievalPrice) : R(0n, 1n);
    return { keep: keep, read: read, total: Radd(keep, read) };
  }
  function tierPlan(buckets, hotPrice, coldPrice, retrievalPrice, moveAge) {
    var allHot = R(0n, 1n), tiered = R(0n, 1n), moved = R(0n, 1n), rows = [];
    for (var i = 0; i < buckets.length; i += 1) {
      var b = buckets[i], isCold = moveAge !== null && i >= moveAge;
      var hot = tierCost(b.gb, b.accesses, hotPrice, coldPrice, retrievalPrice, false);
      var chosen = tierCost(b.gb, b.accesses, hotPrice, coldPrice, retrievalPrice, isCold);
      allHot = Radd(allHot, hot.total);
      tiered = Radd(tiered, chosen.total);
      if (isCold) moved = Radd(moved, b.gb);
      rows.push({ age: i, gb: b.gb, accesses: b.accesses, cold: isCold,
                  hot: hot.total, chosen: chosen.total });
    }
    return { allHot: allHot, tiered: tiered, saving: Rsub(allHot, tiered),
             movedGb: moved, rows: rows };
  }

  /* ======================= L10: compress or not ============================

     Sending S bytes raw takes S/bw. Compressing first takes S/rate to squeeze,
     then S/(k*bw) to send, and optionally S/(k*drate) to expand at the far
     end. Setting the two equal and cancelling S gives the break-even

         1/bw = 1/rate + 1/(k*bw)   =>   bw* = rate*(k-1)/k

     -- which is the lesson's "compression wins when the rate exceeds
     bw*k/(k-1)", the same equality read the other way round. On a fast enough
     link no compressor is fast enough, and that is the point. */
  function rawTime(bytes, bandwidth) { return Rzero(bandwidth) ? null : Rdiv(bytes, bandwidth); }
  function compressedTime(bytes, bandwidth, ratio, rate, decompressRate) {
    if (Rzero(bandwidth) || Rzero(rate) || Rzero(ratio)) return null;
    var squeeze = Rdiv(bytes, rate);
    var send = Rdiv(bytes, Rmul(ratio, bandwidth));
    var expand = decompressRate === null ? R(0n, 1n) : Rdiv(bytes, Rmul(ratio, decompressRate));
    return { squeeze: squeeze, send: send, expand: expand,
             total: Radd(squeeze, Radd(send, expand)) };
  }
  /* The break-even bandwidth, exactly, including the decompression term when
     it is on the critical path: 1/bw = 1/rate + 1/(k*drate) + 1/(k*bw). */
  function compressBreakEvenBandwidth(ratio, rate, decompressRate) {
    var one = R(1n, 1n);
    if (Rzero(ratio) || Rzero(rate)) return null;
    var perByte = Rinv(rate);
    if (decompressRate !== null && !Rzero(decompressRate)) {
      perByte = Radd(perByte, Rinv(Rmul(ratio, decompressRate)));
    }
    if (Rzero(perByte)) return null;
    return Rdiv(Rsub(one, Rinv(ratio)), perByte);
  }
  /* And the same crossing read as a compressor speed, which is how the lesson
     states it: rate > bw * k/(k-1). */
  function compressBreakEvenRate(ratio, bandwidth) {
    var one = R(1n, 1n);
    if (Rcmp(ratio, one) <= 0) return null;
    return Rmul(bandwidth, Rdiv(ratio, Rsub(ratio, one)));
  }

  /* ======================= L11: move the data or the compute ===============

     D/bw against (code + result)/bw. The bandwidth cancels out of the
     comparison entirely -- the decision is code + result against D and nothing
     else -- and the result-to-input ratio is usually a thousandth, which is
     why shipping the query is not a clever optimisation but the default. */
  function moveDataTime(datasetBytes, bandwidth) { return rawTime(datasetBytes, bandwidth); }
  function moveComputeTime(codeBytes, resultBytes, bandwidth) {
    return rawTime(Radd(codeBytes, resultBytes), bandwidth);
  }
  function resultRatio(resultBytes, datasetBytes) {
    return Rzero(datasetBytes) ? null : Rdiv(resultBytes, datasetBytes);
  }
  /* The crossover: move the compute while code + result < D, so the result
     size at which the two plans tie is D - code. Bandwidth free. */
  function placementCrossover(datasetBytes, codeBytes) {
    var gap = Rsub(datasetBytes, codeBytes);
    return Rcmp(gap, R(0n, 1n)) > 0 ? gap : R(0n, 1n);
  }
  function placementSpeedup(datasetBytes, codeBytes, resultBytes) {
    var moved = Radd(codeBytes, resultBytes);
    return Rzero(moved) ? null : Rdiv(datasetBytes, moved);
  }

  /* ======================= headroom: N-1 capacity ==========================

     rho = lambda/(N*capacity) -- lambda over mu, the same definition course 3
     gives, with mu the capacity actually in service. Lose f of N and mu falls
     by the factor (N-f)/N, so rho is MULTIPLIED by N/(N-f). At rho = 0.9 on
     ten machines, losing one lands exactly on rho = 1: there is no steady
     state, the backlog grows at lambda - mu per second, and the response-time
     multiplier 1/(1 - rho) that was ten is gone.

     So the utilisation you may plan for is not the one you can survive, it is
     rho_max * (N - f)/N, and the machine count that supports a target follows
     from an equality rather than a habit. */
  function fleetCapacity(N, perMachine) { return Rmul(R(BigInt(N), 1n), perMachine); }
  function fleetRho(lambda, N, perMachine) {
    var mu = fleetCapacity(N, perMachine);
    return Rzero(mu) ? null : Rdiv(lambda, mu);
  }
  function survivingFraction(N, lost) { return R(BigInt(N - lost), BigInt(N)); }
  function rhoAfterLoss(rho, N, lost) {
    if (N - lost <= 0) return null;
    return Rmul(rho, R(BigInt(N), BigInt(N - lost)));
  }
  /* The smallest N whose surviving capacity still holds rho at or under the
     target, by exact scan. lambda/((N-f)*cap) <= rhoMax rearranges to
     N >= lambda/(cap*rhoMax) + f, whose ceiling is the same integer with no
     search -- both are computed and the page prints them together. */
  function machinesForHeadroom(lambda, perMachine, rhoMax, lost, limit) {
    for (var N = lost + 1; N <= limit; N += 1) {
      var rho = fleetRho(lambda, N - lost, perMachine);
      if (rho !== null && Rcmp(rho, rhoMax) <= 0) return N;
    }
    return null;
  }
  function machinesForHeadroomClosed(lambda, perMachine, rhoMax, lost) {
    if (Rzero(perMachine) || Rzero(rhoMax)) return null;
    return Number(Rceil(Radd(Rdiv(lambda, Rmul(perMachine, rhoMax)), R(BigInt(lost), 1n))));
  }
  /* The nameplate you may actually use: the target utilisation discounted by
     the fraction of the fleet a failure takes away. */
  function usableUtilisation(rhoMax, N, lost) { return Rmul(rhoMax, survivingFraction(N, lost)); }

  /* ======================= growth: the month the plan runs out =============

     A load compounding at r a month is current*(1+r)^m, exact through Rpow at
     any m, and the month it reaches a limit is the smallest m for which that
     exact fraction is at or above the limit -- an integer search, with nothing
     rounded in it.

     log(limit/current)/log(1+r) is the same number and IS rounded; it is
     printed beside the exact month as the gloss, which is the only honest way
     round: the search is the assertion and the logarithm is the explanation. */
  function loadAtMonth(current, rate, m) {
    return Rmul(current, Rpow(Radd(R(1n, 1n), rate), m));
  }
  function monthsToLimit(current, rate, limit, maxMonths) {
    if (Rcmp(current, limit) >= 0) return 0;
    if (Rcmp(rate, R(0n, 1n)) <= 0) return null;
    for (var m = 1; m <= maxMonths; m += 1) {
      if (Rcmp(loadAtMonth(current, rate, m), limit) >= 0) return m;
    }
    return null;
  }
  /* The rounded closed form, labelled everywhere it appears. */
  function monthsToLimitApprox(current, rate, limit) {
    if (Rcmp(rate, R(0n, 1n)) <= 0 || Rzero(current)) return Infinity;
    return logApprox(Rnum(Rdiv(limit, current))) / logApprox(Rnum(Radd(R(1n, 1n), rate)));
  }
  function doublingMonths(rate, maxMonths) {
    return monthsToLimit(R(1n, 1n), rate, R(2n, 1n), maxMonths);
  }
  /* The capacity plan itself: machines needed each month is the ceiling of the
     month's load over what one machine may carry, which is capacity times the
     target utilisation. The ceiling is the lesson -- 3.2 machines is four. */
  function machinesAtMonth(current, rate, m, perMachine, rhoTarget) {
    var usable = Rmul(perMachine, rhoTarget);
    if (Rzero(usable)) return null;
    return Number(Rceil(Rdiv(loadAtMonth(current, rate, m), usable)));
  }
  /* The month you must ORDER in, given a lead time: the plan runs out at month
     M, so the order goes in at M - lead, and a lead time longer than the
     runway means it should already have gone in. */
  function orderMonth(limitMonth, leadMonths) {
    if (limitMonth === null) return null;
    return limitMonth - leadMonths;
  }
"""


# ---------------------------------------------------------------- furniture

# counting.BIGINT_JS is deliberately NOT here. Every page ships its whole kit,
# and nothing on this course is a factorial or a binomial coefficient: the kits
# that must carry it are the ones calling erlangC or availKofN, which are
# queue, avail, replica, shard and measure. Adding it "for safety" is a few
# kilobytes on each of eleven lesson pages in exchange for nothing.
_CORE_JS = RATIONAL_JS + RCEIL_JS + APPROX_JS + SCALE_JS


def _options(items, chosen):
    return "".join(
        '<option value="%s"%s>%s</option>'
        % (key, " selected" if key == chosen else "", label)
        for key, label in items
    )


def _select(cid, label, items, chosen):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n'
        "        </div>\n" % (cid, cid, label, cid, _options(items, chosen))
    )


def _range(cid, label, lo, hi, value, step=1):
    """One control: the row that names it, the readout, and the slider.

    The readout opens empty. Every number on the panel is written by redraw()
    from the arithmetic, so a lab whose script threw shows dashes rather than a
    plausible figure that nothing computed.
    """
    return (
        '        <div id="%sRow">\n'
        '          <div class="range-row"><label class="small-copy" for="%s" id="%sLab">%s</label>'
        '<span class="range-value" id="%sOut">&mdash;</span></div>\n'
        '          <input id="%s" type="range" min="%d" max="%d" step="%d" value="%d" />\n'
        "        </div>\n" % (cid, cid, cid, label, cid, cid, lo, hi, step, value)
    )


def _kpi(rows):
    return (
        '        <div class="kpi-grid">\n'
        + "".join(
            '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
            % (label, cid)
            for cid, label in rows
        )
        + "        </div>\n"
    )


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _stage(sid, svg_id, width, height, label, aria):
    """A drawing, at one of the three viewBox widths theme.py gives a scroll
    minimum. Any other width shrinks the labels to illegibility on a phone
    instead of letting the stage scroll, which is the whole point of the rule.
    """
    if width not in (460, 520, 660):
        raise ValueError(
            "scale: viewBox width %d has no horizontal-scroll minimum in "
            "theme.py; use 460, 520 or 660" % width
        )
    return (
        '      <div class="lab-stage" id="%s" tabindex="0" role="region" aria-label="%s">'
        '<svg id="%s" style="min-width:%dpx" viewBox="0 0 %d %d" role="img" '
        'aria-label="%s"></svg></div>\n' % (sid, label, svg_id, width, width, height, aria)
    )


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own, which is how two lessons can share a mode
    without either showing the other's numbers. An unknown preset raises for
    the same reason an unknown mode does: a silent fallback ships a page that
    looks finished and is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("scale mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "scale mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "scale mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


# =============================================================== mode: amdahl

AMDAHL_PRESETS = [
    {
        "key": "five-per-cent-serial",
        "label": "95% parallel — the lesson's own case, capped at 20×",
        "p": 950, "n": 32, "f": 90,
        "what": "a request path whose last twentieth cannot be split",
    },
    {
        "key": "well-parallelised",
        "label": "99% parallel — a hundredfold ceiling, and 891 machines to reach 90% of it",
        "p": 990, "n": 128, "f": 90,
        "what": "a map-reduce whose reduce is one per cent of the work",
    },
    {
        "key": "mostly-serial",
        "label": "70% parallel — the ceiling is 3.33× and the fourth machine is already wasted",
        "p": 700, "n": 16, "f": 90,
        "what": "a report job that spends a third of its time in one query",
    },
    {
        "key": "near-perfect",
        "label": "99.9% parallel — a thousandfold ceiling that still exists",
        "p": 999, "n": 256, "f": 95,
        "what": "an embarrassingly parallel render with one serial upload",
    },
]

AMDAHL_SCRIPT = r"""
  var sel = document.getElementById('amPreset');
  var plot = document.getElementById('amPlot');
  var status = document.getElementById('amStatus');
  var table = document.getElementById('amTable');
  var LIMIT = 200000;             /* the scan's bound: 99% of a 1000x ceiling
                                     needs 98 901 machines, so the bound has to
                                     clear the sliders' worst case honestly. */

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('amdahl: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('amP').value = p.p;
    document.getElementById('amN').value = p.n;
    document.getElementById('amF').value = p.f;
  }

  function state() {
    var pv = +document.getElementById('amP').value;
    var n = +document.getElementById('amN').value;
    var fv = +document.getElementById('amF').value;
    return { p: R(BigInt(pv), 1000n), n: n, f: R(BigInt(fv), 100n), pv: pv, fv: fv };
  }

  function draw(st, ceiling, reach) {
    var maxN = st.n < 8 ? 8 : st.n;
    var top = ratioApprox(ceiling, R(1n, 1n)) * 1.12;
    if (!(top > 0)) top = 2;
    var x = function (n) { return 40 + (n - 1) / (maxN - 1) * 452; };
    var y = function (v) { return 168 - Math.min(v, top) / top * 146; };
    var s = '';
    /* the ceiling, which is the whole lesson */
    var yc = y(ratioApprox(ceiling, R(1n, 1n)));
    s += '<line x1="40" y1="' + yc.toFixed(1) + '" x2="492" y2="' + yc.toFixed(1)
      + '" stroke="var(--red)" stroke-width="1.6" stroke-dasharray="6 4" />'
      + '<text x="492" y="' + (yc - 6).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--red)">'
      + 'ceiling 1/(1&minus;p) = ' + Rnice(ceiling, 2) + '&times;</text>';
    /* what the reader expected: n machines, n times faster */
    var lin = '';
    for (var n = 1; n <= maxN; n += 1) {
      lin += (n === 1 ? 'M' : 'L') + x(n).toFixed(1) + ' ' + y(n).toFixed(1) + ' ';
    }
    s += '<path d="' + lin + '" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="3 3" />';
    /* Amdahl itself */
    var path = '';
    for (n = 1; n <= maxN; n += 1) {
      var v = ratioApprox(amdahlSpeedup(st.p, n), R(1n, 1n));
      path += (n === 1 ? 'M' : 'L') + x(n).toFixed(1) + ' ' + y(v).toFixed(1) + ' ';
    }
    s += '<path d="' + path + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />';
    if (reach !== null && reach <= maxN) {
      s += '<line x1="' + x(reach).toFixed(1) + '" y1="22" x2="' + x(reach).toFixed(1)
        + '" y2="168" stroke="var(--green)" stroke-width="1.4" stroke-dasharray="4 3" />'
        + '<text x="' + (x(reach) + 4).toFixed(1) + '" y="34" font-size="10" fill="var(--green)">n = '
        + reach + '</text>';
    }
    var here = ratioApprox(amdahlSpeedup(st.p, st.n), R(1n, 1n));
    s += '<circle cx="' + x(st.n).toFixed(1) + '" cy="' + y(here).toFixed(1)
      + '" r="4" fill="var(--amber)" />'
      + '<line x1="40" y1="168" x2="492" y2="168" stroke="var(--line-strong)" />'
      + '<line x1="40" y1="22" x2="40" y2="168" stroke="var(--line-strong)" />'
      + '<text x="40" y="184" font-size="10" fill="var(--muted)">1 machine</text>'
      + '<text x="492" y="184" text-anchor="end" font-size="10" fill="var(--muted)">' + maxN + ' machines</text>'
      + '<text x="8" y="30" font-size="10" fill="var(--muted)">speedup</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state(), p = preset();
    var one = R(1n, 1n);
    var ceiling = amdahlCeiling(st.p);
    var serial = Rsub(one, st.p);
    document.getElementById('amPOut').textContent = Rpct(st.p, 1) + ' parallel, ' + Rpct(serial, 1) + ' serial';
    document.getElementById('amNOut').textContent = st.n + ' machines';
    document.getElementById('amFOut').textContent = Rpct(st.f, 0) + ' of the ceiling';

    var here = amdahlSpeedup(st.p, st.n);
    var reach = ceiling === null ? null : amdahlReach(st.p, st.f, LIMIT);
    var closed = ceiling === null ? null : amdahlReachClosed(st.p, st.f);
    draw(st, ceiling === null ? R(BigInt(st.n), 1n) : ceiling, reach);

    document.getElementById('amSpeed').textContent = Rshort(here, 3) + '×';
    document.getElementById('amCeil').textContent = ceiling === null ? 'none — p = 1' : Rshort(ceiling, 3) + '×';
    document.getElementById('amLeft').textContent = ceiling === null ? '—'
      : Rpct(Rdiv(here, ceiling), 2) + ' of it';
    document.getElementById('amReach').textContent = reach === null ? '—' : reach + ' machines';
    document.getElementById('amClosed').textContent = closed === null ? '—' : closed + ' machines';
    document.getElementById('amEff').textContent = Rpct(amdahlEfficiency(st.p, st.n), 2);

    var rows = '<thead><tr><th>machines n</th><th>S(n) exact</th><th>S(n)</th>'
      + '<th>n machines, n&times; faster</th><th>efficiency S(n)/n</th></tr></thead><tbody>';
    var picks = [1, 2, 4, 8, st.n, reach].filter(function (v, i, a) {
      return v !== null && v >= 1 && a.indexOf(v) === i;
    }).sort(function (a, b) { return a - b; });
    for (var i = 0; i < picks.length; i += 1) {
      var n = picks[i], sv = amdahlSpeedup(st.p, n);
      rows += '<tr><td>' + n + (n === st.n ? ' <span class="tone-amber">(shown)</span>' : '')
        + (n === reach ? ' <span class="tone-green">(reaches ' + Rpct(st.f, 0) + ')</span>' : '')
        + '</td><td>' + Rshort(sv, 4) + '</td><td>' + Rnice(sv, 3) + '×</td>'
        + '<td class="tone-muted">' + n + '×</td><td>' + Rpct(amdahlEfficiency(st.p, n), 1)
        + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'With ' + Rpct(st.p, 1) + ' of ' + p.what + ' parallel, the other <strong>'
      + Rpct(serial, 1) + '</strong> never shrinks — so S(n) = 1/((1&minus;p) + p/n) climbs to '
      + (ceiling === null ? 'no ceiling at all, because p = 1' :
        '<strong>' + Rshort(ceiling, 3) + '×</strong> and stops')
      + '. At ' + st.n + ' machines you have <strong>' + Rnice(here, 3) + '×</strong>'
      + (ceiling === null ? '' : ', which is ' + Rpct(Rdiv(here, ceiling), 2) + ' of the ceiling')
      + ', while <span class="tone-red">' + st.n + ' machines, ' + st.n + '× faster</span> would have said '
      + st.n + '× — the grey line, and it is wrong by a factor of '
      + Rnice(Rdiv(R(BigInt(st.n), 1n), here), 2) + '. '
      + (reach === null ? ''
        : 'Reaching ' + Rpct(st.f, 0) + ' of the ceiling takes <strong>' + reach
          + '</strong> machines. That is a scan over integers, and rearranging '
          + 'S(n) &ge; f/(1&minus;p) gives n &ge; (f/(1&minus;f))&thinsp;&middot;&thinsp;(p/(1&minus;p)), '
          + 'whose ceiling is <strong>' + closed + '</strong> — the same integer by algebra, with no root '
          + 'and no logarithm in either route. ')
      + 'Efficiency at ' + st.n + ' machines is ' + Rpct(amdahlEfficiency(st.p, st.n), 2)
      + ': the rest of what you bought is waiting on the serial part.';
  }

  ['amP', 'amN', 'amF'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _amdahl(cfg):
    """Lesson 1: the speedup, the ceiling it never reaches, and the n that gets close."""
    idx = _preset_index(cfg, AMDAHL_PRESETS, "amdahl")
    p = AMDAHL_PRESETS[idx]
    markup = (
        _toolbar(
            "Amdahl's ceiling",
            "the serial part does not shrink, so the speedup stops",
            _swatch("tone-cyan", "S(n)")
            + _swatch("tone-red", "the ceiling 1/(1&minus;p)")
            + _swatch("tone-muted", "n machines, n&times; faster")
            + _swatch("tone-green", "the n that reaches the target"),
        )
        + _stage(
            "amStage", "amPlot", 520, 192,
            "Amdahl speedup against machine count, with its asymptote and the linear expectation.",
            "The speedup curve flattening below a dashed ceiling, with the straight line a reader expects running off the top.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="amTable"></table></div>\n'
        '      <div class="status-banner" id="amStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("amPreset", "Worked example", [(q["key"], q["label"]) for q in AMDAHL_PRESETS], p["key"])
        + _range("amP", "parallel fraction p", 0, 999, p["p"])
        + _range("amN", "machines n", 1, 512, p["n"])
        + _range("amF", "target: this much of the ceiling", 50, 99, p["f"])
        + _kpi([
            ("amSpeed", "Speedup S(n)"),
            ("amCeil", "Ceiling 1/(1&minus;p)"),
            ("amLeft", "Fraction of the ceiling"),
            ("amReach", "n for the target, by scan"),
            ("amClosed", "… and in closed form"),
            ("amEff", "Efficiency S(n)/n"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", AMDAHL_PRESETS) + AMDAHL_SCRIPT
    return Lab(
        title="Amdahl's Law",
        subtitle="What the next machine buys, and where it stops buying anything",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the parallel fraction and add machines"),
        panel_intro=cfg.get(
            "panel_intro",
            "S(n), the ceiling and the machine count that reaches a stated fraction of it are "
            "exact fractions of the parallel fraction you set. The machine count is found twice "
            "— by a scan over integers and by rearranging the inequality — and the two integers "
            "must agree.",
        ),
        script=script,
    )


# ================================================================== mode: usl

USL_PRESETS = [
    {
        "key": "coherency-at-ninety-nine",
        "label": "α = 0.02, β = 0.0001 — the lesson's own curve, peaking at 99 machines",
        "alpha": 200, "beta": 10, "span": 260,
        "what": "a service whose replicas must agree on every write",
    },
    {
        "key": "contention-only",
        "label": "β = 0 — no coherency term at all, so it plateaus like Amdahl and never falls",
        "alpha": 200, "beta": 0, "span": 260,
        "what": "the same service with the agreement cost pretended away",
    },
    {
        "key": "chatty-cluster",
        "label": "α = 0.05, β = 0.001 — a chatty cluster that peaks at 31 and is worse at 64",
        "alpha": 500, "beta": 100, "span": 96,
        "what": "a cluster gossiping state on every request",
    },
    {
        "key": "nearly-shared-nothing",
        "label": "α = 0.005, β = 0.00001 — shared-nothing, peaking past 300",
        "alpha": 50, "beta": 1, "span": 400,
        "what": "a shared-nothing tier with one sequence generator left in it",
    },
]

USL_SCRIPT = r"""
  var sel = document.getElementById('usPreset');
  var plot = document.getElementById('usPlot');
  var status = document.getElementById('usStatus');
  var table = document.getElementById('usTable');
  var SCAN = 20000;              /* the peak at beta = 1/100000 is near 313; the
                                    bound clears every slider position with room. */

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('usl: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('usA').value = p.alpha;
    document.getElementById('usB').value = p.beta;
    document.getElementById('usN').value = p.span;
  }
  function state() {
    return {
      alpha: R(BigInt(+document.getElementById('usA').value), 10000n),
      beta: R(BigInt(+document.getElementById('usB').value), 100000n),
      span: +document.getElementById('usN').value
    };
  }

  function draw(st, curve, peakN, peakV) {
    var top = 0, i;
    for (i = 0; i < curve.length; i += 1) {
      var v = ratioApprox(curve[i], R(1n, 1n));
      if (v > top) top = v;
    }
    if (peakV !== null) {
      var pv = ratioApprox(peakV, R(1n, 1n));
      if (pv > top) top = pv;
    }
    top *= 1.14;
    if (!(top > 0)) top = 1;
    var x = function (n) { return 46 + (n - 1) / (st.span - 1) * 596; };
    var y = function (v) { return 176 - v / top * 150; };
    var s = '';
    /* the contention-only curve: what the same alpha does with NO coherency
       term. It plateaus. The gap between the two lines IS beta. */
    var flat = '';
    for (i = 1; i <= st.span; i += 1) {
      var fv = ratioApprox(uslThroughput(i, st.alpha, R(0n, 1n)), R(1n, 1n));
      flat += (i === 1 ? 'M' : 'L') + x(i).toFixed(1) + ' ' + y(fv).toFixed(1) + ' ';
    }
    s += '<path d="' + flat + '" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3" />';
    /* the descending half, shaded: past the peak the next machine is harmful */
    if (peakN !== null && peakN < st.span) {
      s += '<rect x="' + x(peakN).toFixed(1) + '" y="26" width="' + (x(st.span) - x(peakN)).toFixed(1)
        + '" height="150" fill="var(--red)" opacity="0.10" />'
        + '<text x="' + (x(peakN) + 8).toFixed(1) + '" y="40" font-size="10" fill="var(--red)">'
        + 'past the peak: every machine here makes it worse</text>';
    }
    var path = '';
    for (i = 1; i <= st.span; i += 1) {
      var cv = ratioApprox(curve[i - 1], R(1n, 1n));
      path += (i === 1 ? 'M' : 'L') + x(i).toFixed(1) + ' ' + y(cv).toFixed(1) + ' ';
    }
    s += '<path d="' + path + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />';
    if (peakN !== null && peakN <= st.span) {
      var py = y(ratioApprox(peakV, R(1n, 1n)));
      s += '<line x1="' + x(peakN).toFixed(1) + '" y1="' + py.toFixed(1) + '" x2="' + x(peakN).toFixed(1)
        + '" y2="176" stroke="var(--green)" stroke-width="1.5" stroke-dasharray="4 3" />'
        + '<circle cx="' + x(peakN).toFixed(1) + '" cy="' + py.toFixed(1) + '" r="4.5" fill="var(--green)" />'
        + '<text x="' + x(peakN).toFixed(1) + '" y="' + (py - 9).toFixed(1)
        + '" text-anchor="middle" font-size="10" fill="var(--green)">N* = ' + peakN + '</text>';
    }
    s += '<line x1="46" y1="176" x2="642" y2="176" stroke="var(--line-strong)" />'
      + '<line x1="46" y1="26" x2="46" y2="176" stroke="var(--line-strong)" />'
      + '<text x="46" y="192" font-size="10" fill="var(--muted)">1</text>'
      + '<text x="642" y="192" text-anchor="end" font-size="10" fill="var(--muted)">' + st.span + ' machines</text>'
      + '<text x="8" y="34" font-size="10" fill="var(--muted)">throughput</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state(), p = preset();
    document.getElementById('usAOut').textContent = 'α = ' + Rtext(st.alpha) + ' = ' + Rfixed(st.alpha, 5);
    document.getElementById('usBOut').textContent = 'β = ' + Rtext(st.beta) + ' = ' + Rfixed(st.beta, 6);
    document.getElementById('usNOut').textContent = 'showing 1 … ' + st.span + ' machines';

    var peakN = uslPeakExact(st.alpha, st.beta, SCAN);
    var scanned = uslPeakScan(st.alpha, st.beta, peakN === null ? st.span : peakN * 2 + 4);
    var peakV = peakN === null ? null : uslThroughput(peakN, st.alpha, st.beta);
    var curve = uslCurve(st.alpha, st.beta, st.span);
    draw(st, curve, peakN, peakV);

    var closed = uslPeakRootApprox(st.alpha, st.beta);
    var ceil = uslContentionCeiling(st.alpha);
    var atSpan = uslThroughput(st.span, st.alpha, st.beta);
    document.getElementById('usPeakN').textContent = peakN === null ? 'none — β = 0' : peakN + ' machines';
    document.getElementById('usPeakC').textContent = peakV === null ? '—' : Rnice(peakV, 3) + '× one machine';
    document.getElementById('usClosed').textContent = peakN === null ? '∞ (no root to take)'
      : closed.toFixed(4) + ' (rounded)';
    document.getElementById('usScan').textContent = scanned.N + ' machines';
    document.getElementById('usEnd').textContent = atSpan === null ? '—' : Rnice(atSpan, 3) + '×';
    document.getElementById('usCeil').textContent = ceil === null ? 'none — α = 0' : Rnice(ceil, 3) + '×';

    var picks = [1, 2, 4];
    if (peakN !== null) {
      [peakN - 1, peakN, peakN + 1, peakN * 2].forEach(function (v) { if (v >= 1) picks.push(v); });
    }
    picks.push(st.span);
    picks = picks.filter(function (v, i, a) { return a.indexOf(v) === i; })
                 .sort(function (a, b) { return a - b; });
    var rows = '<thead><tr><th>machines N</th><th>C(N) exact</th><th>C(N)</th>'
      + '<th>vs the machine before</th><th>share of the peak</th></tr></thead><tbody>';
    for (var i = 0; i < picks.length; i += 1) {
      var N = picks[i], c = uslThroughput(N, st.alpha, st.beta);
      if (c === null) continue;
      var prev = N > 1 ? uslThroughput(N - 1, st.alpha, st.beta) : null;
      var delta = prev === null ? null : Rsub(c, prev);
      var kept = peakN === null ? null : uslRetained(N, st.alpha, st.beta, peakN);
      rows += '<tr><td>' + N + (N === peakN ? ' <span class="tone-green">(the peak)</span>' : '')
        + '</td><td>' + Rshort(c, 4) + '</td><td>' + Rnice(c, 4) + '</td><td'
        + (delta !== null && Rcmp(delta, R(0n, 1n)) < 0 ? ' class="tone-red"' : '')
        + '>' + (delta === null ? '—' : (Rcmp(delta, R(0n, 1n)) >= 0 ? '+' : '') + Rnice(delta, 4))
        + '</td><td>' + (kept === null ? '—' : Rpct(kept, 2)) + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    if (peakN === null) {
      status.innerHTML = '<span class="tone-amber">β = 0, so there is no coherency cost and the curve '
        + 'does not turn over.</span> This is Amdahl again: C(N) climbs towards 1/α = '
        + (ceil === null ? 'no ceiling' : '<strong>' + Rnice(ceil, 3) + '×</strong>')
        + ' and plateaus there for ever. At ' + st.span + ' machines it is '
        + Rnice(atSpan, 3) + '× and still rising. Put β back and the same curve acquires a '
        + 'peak and a descent — which is the difference between "extra machines stop helping" and '
        + '"extra machines start hurting", and the whole reason the Universal Scalability Law '
        + 'is not just Amdahl with more letters.';
    } else {
      var twice = peakN * 2, atTwice = uslThroughput(twice, st.alpha, st.beta);
      status.innerHTML = 'For ' + p.what + ', contention α = ' + Rtext(st.alpha)
        + ' and coherency β = ' + Rtext(st.beta) + '. The peak is at <strong>N* = ' + peakN
        + '</strong> machines, carrying <strong>' + Rnice(peakV, 3) + '×</strong> one machine. '
        + 'That integer is not read off the curve: C(N+1) &le; C(N) reduces exactly to '
        + 'β&thinsp;N(N+1) &ge; 1&minus;α, so N* is the smallest N satisfying it — no root, '
        + 'no rounding. The familiar &radic;((1&minus;α)/β) = <strong>' + closed.toFixed(4)
        + '</strong> is printed rounded beside it and agrees, and the scan’s argmax is ' + scanned.N + '. '
        + '<span class="tone-red">Past N* the curve falls.</span> At ' + twice + ' machines — twice the peak, '
        + 'twice the bill — it carries ' + Rnice(atTwice, 3) + '×, which is '
        + Rpct(uslRetained(twice, st.alpha, st.beta, peakN), 1) + ' of the peak. '
        + 'The dashed line is the same α with β set to zero: it plateaus at '
        + (ceil === null ? 'no ceiling' : Rnice(ceil, 2) + '×') + ' and never comes down. '
        + 'A reader who has only met Amdahl expects the dashed line.';
    }
  }

  ['usA', 'usB', 'usN'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _usl(cfg):
    """Lesson 2: the peak, the descent past it, and the root printed as a check."""
    idx = _preset_index(cfg, USL_PRESETS, "usl")
    p = USL_PRESETS[idx]
    markup = (
        _toolbar(
            "The Universal Scalability Law",
            "contention flattens the curve; coherency turns it over",
            _swatch("tone-cyan", "C(N) with both terms")
            + _swatch("tone-muted", "the same &alpha; with &beta; = 0")
            + _swatch("tone-green", "the exact peak N*")
            + _swatch("tone-red", "where another machine is worse"),
        )
        + _stage(
            "usStage", "usPlot", 660, 200,
            "Throughput against machine count, rising to a peak and then falling.",
            "The Universal Scalability Law curve peaking and descending, with the contention-only curve plateauing above it.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="usTable"></table></div>\n'
        '      <div class="status-banner" id="usStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("usPreset", "Worked example", [(q["key"], q["label"]) for q in USL_PRESETS], p["key"])
        + _range("usA", "contention &alpha;, in ten-thousandths", 0, 2000, p["alpha"])
        + _range("usB", "coherency &beta;, in hundred-thousandths", 0, 500, p["beta"])
        + _range("usN", "machines shown", 8, 400, p["span"])
        + _kpi([
            ("usPeakN", "Peak N*, exactly"),
            ("usPeakC", "Throughput at the peak"),
            ("usClosed", "&radic;((1&minus;&alpha;)/&beta;)"),
            ("usScan", "Peak by scanning the curve"),
            ("usEnd", "Throughput at the far end"),
            ("usCeil", "Amdahl's 1/&alpha; for this &alpha;"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", USL_PRESETS) + USL_SCRIPT
    return Lab(
        title="The Universal Scalability Law",
        subtitle="A peak, and a descent on the other side of it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set contention and coherency"),
        panel_intro=cfg.get(
            "panel_intro",
            "C(N) is evaluated as an exact fraction at every integer N. The peak is the smallest "
            "N with βN(N+1) ≥ 1−α, which is the closed form with the square root "
            "taken out of it; the root itself is printed rounded beside it as a check. Set β "
            "to zero and the curve stops turning over — that is what the coherency term is.",
        ),
        script=script,
    )


# ================================================================ mode: batch

BATCH_PRESETS = [
    {
        "key": "write-batching",
        "label": "a write path: 2000 µ$ per batch call, 100 µ$ an item, 500 items/s",
        "F": 2000, "v": 100, "lam": 500, "B": 100, "share": 20, "timer": 200,
        "what": "a batched write to an object store",
    },
    {
        "key": "cheap-fixed",
        "label": "a cheap call: 300 µ$ fixed — batching buys much less",
        "F": 300, "v": 100, "lam": 500, "B": 20, "share": 20, "timer": 60,
        "what": "an in-datacentre RPC with a small envelope",
    },
    {
        "key": "expensive-fixed",
        "label": "an expensive call: 20 000 µ$ fixed, and a batch of a thousand",
        "F": 20000, "v": 100, "lam": 500, "B": 400, "share": 20, "timer": 900,
        "what": "a third-party API billed per request",
    },
    {
        "key": "slow-arrivals",
        "label": "the same write path at 20 items/s — the same batch costs 25× the wait",
        "F": 2000, "v": 100, "lam": 20, "B": 100, "share": 20, "timer": 2000,
        "what": "the same batched write on a quiet shard",
    },
]

BATCH_SCRIPT = r"""
  var sel = document.getElementById('baPreset');
  var plot = document.getElementById('baPlot');
  var status = document.getElementById('baStatus');
  var table = document.getElementById('baTable');
  var MAXB = 800;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('batch: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('baB').value = p.B;
    document.getElementById('baF').value = p.F;
    document.getElementById('baLam').value = p.lam;
    document.getElementById('baShare').value = p.share;
    document.getElementById('baTimer').value = p.timer;
  }
  function state() {
    var p = preset();
    return {
      p: p,
      F: R(BigInt(+document.getElementById('baF').value), 1n),
      v: R(BigInt(p.v), 1n),
      lam: R(BigInt(+document.getElementById('baLam').value), 1n),
      B: +document.getElementById('baB').value,
      share: R(BigInt(+document.getElementById('baShare').value), 100n),
      timer: R(BigInt(+document.getElementById('baTimer').value), 1000n)
    };
  }

  function draw(st, chosen, advised) {
    var span = 200, i;
    var costTop = ratioApprox(perItemCost(st.F, st.v, 1), R(1n, 1n)) * 1.05;
    var waitTop = ratioApprox(batchWaitMean(span, st.lam), R(1n, 1n)) * 1.15;
    if (!(costTop > 0)) costTop = 1;
    if (!(waitTop > 0)) waitTop = 1;
    var x = function (B) { return 48 + (B - 1) / (span - 1) * 428; };
    var yc = function (v) { return 162 - Math.min(v, costTop) / costTop * 132; };
    var yw = function (v) { return 162 - Math.min(v, waitTop) / waitTop * 132; };
    var s = '', cost = '', wait = '';
    for (i = 1; i <= span; i += 1) {
      cost += (i === 1 ? 'M' : 'L') + x(i).toFixed(1) + ' '
        + yc(ratioApprox(perItemCost(st.F, st.v, i), R(1n, 1n))).toFixed(1) + ' ';
      wait += (i === 1 ? 'M' : 'L') + x(i).toFixed(1) + ' '
        + yw(ratioApprox(batchWaitMean(i, st.lam), R(1n, 1n))).toFixed(1) + ' ';
    }
    /* the floor the cost curve is falling towards: v, the part batching cannot
       touch. Without it the hyperbola looks as if it goes to zero. */
    var floorY = yc(ratioApprox(st.v, R(1n, 1n)));
    s += '<line x1="48" y1="' + floorY.toFixed(1) + '" x2="476" y2="' + floorY.toFixed(1)
      + '" stroke="var(--red)" stroke-width="1.4" stroke-dasharray="5 4" />'
      + '<text x="476" y="' + (floorY - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--red)">'
      + 'the floor: v = ' + Rnice(st.v, 0) + ' µ$ an item, whatever B is</text>'
      + '<path d="' + cost + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />'
      + '<path d="' + wait + '" fill="none" stroke="var(--amber)" stroke-width="2" />';
    if (advised !== null && advised <= span) {
      s += '<line x1="' + x(advised).toFixed(1) + '" y1="20" x2="' + x(advised).toFixed(1)
        + '" y2="162" stroke="var(--green)" stroke-width="1.4" stroke-dasharray="4 3" />'
        + '<text x="' + (x(advised) + 4).toFixed(1) + '" y="32" font-size="10" fill="var(--green)">B = '
        + advised + ', where the fixed share has fallen to ' + Rpct(st.share, 0) + '</text>';
    }
    if (chosen <= span) {
      s += '<circle cx="' + x(chosen).toFixed(1) + '" cy="'
        + yc(ratioApprox(perItemCost(st.F, st.v, chosen), R(1n, 1n))).toFixed(1)
        + '" r="4" fill="var(--cyan)" />'
        + '<circle cx="' + x(chosen).toFixed(1) + '" cy="'
        + yw(ratioApprox(batchWaitMean(chosen, st.lam), R(1n, 1n))).toFixed(1)
        + '" r="4" fill="var(--amber)" />';
    }
    s += '<line x1="48" y1="162" x2="476" y2="162" stroke="var(--line-strong)" />'
      + '<text x="48" y="178" font-size="10" fill="var(--muted)">B = 1</text>'
      + '<text x="476" y="178" text-anchor="end" font-size="10" fill="var(--muted)">B = ' + span + '</text>'
      + '<text x="6" y="28" font-size="10" fill="var(--cyan)">µ$ / item</text>'
      + '<text x="514" y="28" text-anchor="end" font-size="10" fill="var(--amber)">mean wait</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    var B = st.B;
    var timer = batchUnderTimer(B, st.lam, st.timer);
    var effective = timer.effective;
    var advised = batchForFixedShare(st.F, st.v, st.share);
    document.getElementById('baBOut').textContent = 'B = ' + B
      + (timer.capped ? ' — but the timer flushes at ' + effective : '');
    document.getElementById('baFOut').textContent = Rnice(st.F, 0) + ' µ$ per batch call';
    document.getElementById('baLamOut').textContent = Rnice(st.lam, 0) + ' items/s arriving';
    document.getElementById('baShareOut').textContent = 'fixed share down to ' + Rpct(st.share, 0) + ' of v';
    document.getElementById('baTimerOut').textContent = fmtSecs(st.timer) + ' flush timer';
    draw(st, effective, advised);

    var unit = perItemCost(st.F, st.v, effective);
    var alone = perItemCost(st.F, st.v, 1);
    document.getElementById('baUnit').textContent = Rnice(unit, 2) + ' µ$';
    document.getElementById('baSaving').textContent = Rnice(Rdiv(alone, unit), 2) + '× cheaper than B = 1';
    document.getElementById('baWaitMean').textContent = fmtSecs(batchWaitMean(effective, st.lam));
    document.getElementById('baWaitFirst').textContent = fmtSecs(batchWaitFirst(effective, st.lam));
    document.getElementById('baRule').textContent = fmtSecs(batchWaitRule(effective, st.lam));
    document.getElementById('baAdvised').textContent = advised === null ? '—' : 'B = ' + advised;

    var picks = [1, 2, 5, 10, effective, advised, MAXB].filter(function (v, i, a) {
      return v !== null && v >= 1 && v <= MAXB && a.indexOf(v) === i;
    }).sort(function (a, b) { return a - b; });
    var rows = '<thead><tr><th>batch B</th><th>F/B + v exact</th><th>µ$ / item</th>'
      + '<th>fixed share</th><th>mean wait</th><th>first item waits</th></tr></thead><tbody>';
    for (var i = 0; i < picks.length; i += 1) {
      var b = picks[i], u = perItemCost(st.F, st.v, b);
      rows += '<tr><td>' + b + (b === effective ? ' <span class="tone-amber">(shown)</span>' : '')
        + (b === advised ? ' <span class="tone-green">(the flat part)</span>' : '')
        + '</td><td>' + Rshort(u, 3) + '</td><td>' + Rnice(u, 2) + '</td><td>'
        + Rpct(fixedShare(st.F, st.v, b), 1) + '</td><td>' + fmtSecs(batchWaitMean(b, st.lam))
        + '</td><td>' + fmtSecs(batchWaitFirst(b, st.lam)) + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    var ruleOver = Rsub(batchWaitRule(effective, st.lam), batchWaitFirst(effective, st.lam));
    status.innerHTML = 'For ' + st.p.what + ', one item alone costs <strong>' + Rnice(alone, 0)
      + ' µ$</strong> — nearly all of it the ' + Rnice(st.F, 0)
      + ' µ$ call. At B = ' + effective + ' the same item costs <strong>' + Rnice(unit, 2)
      + ' µ$</strong>, which is ' + Rnice(Rdiv(alone, unit), 2) + '× cheaper, and the fixed '
      + 'share has fallen to ' + Rpct(fixedShare(st.F, st.v, effective), 1) + '. '
      + '<span class="tone-red">Bigger is not better past that</span>: the whole remaining saving is F/B = '
      + Rnice(Rdiv(st.F, R(BigInt(effective), 1n)), 2) + ' µ$, and the curve is flat because it is '
      + 'a hyperbola sitting on a floor of v = ' + Rnice(st.v, 0) + ' µ$ that batching cannot touch. '
      + 'The wait paid for it is <strong>' + fmtSecs(batchWaitMean(effective, st.lam))
      + '</strong> on average and <strong>' + fmtSecs(batchWaitFirst(effective, st.lam))
      + '</strong> for the first item in the batch — (B&minus;1)/λ and half of it, both exact. '
      + 'The rule of thumb B/λ says ' + fmtSecs(batchWaitRule(effective, st.lam))
      + ', which overstates the first item’s wait by exactly ' + fmtSecs(ruleOver)
      + ' — one inter-arrival time, at every B. '
      + (timer.capped ? '<span class="tone-amber">The ' + fmtSecs(st.timer) + ' timer binds here:</span> only '
          + timer.reach + ' items arrive in that window, so the batch flushes partial and B = ' + B
          + ' is never reached. ' : '')
      + '“Where the curve flattens” is a judgement, and the same fixed-against-holding bargain has '
      + 'an exact optimum in Operations Research — inventory-models/the-eoq-formula-without-calculus, '
      + 'with latency in the holding cost’s role.';
  }

  ['baB', 'baF', 'baLam', 'baShare', 'baTimer'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _batch(cfg):
    """Lesson 3: one curve down, one curve up, and the B where the first flattens."""
    idx = _preset_index(cfg, BATCH_PRESETS, "batch")
    p = BATCH_PRESETS[idx]
    markup = (
        _toolbar(
            "Batching",
            "per-item cost falls, the fill wait rises, and neither is free",
            _swatch("tone-cyan", "&micro;$ per item")
            + _swatch("tone-amber", "mean wait")
            + _swatch("tone-red", "the floor v")
            + _swatch("tone-green", "where the fixed share has gone"),
        )
        + _stage(
            "baStage", "baPlot", 520, 186,
            "Per-item cost falling with batch size against the fill wait rising with it.",
            "A falling cost hyperbola resting on a dashed floor, crossed by a rising wait line.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="baTable"></table></div>\n'
        '      <div class="status-banner" id="baStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("baPreset", "Worked example", [(q["key"], q["label"]) for q in BATCH_PRESETS], p["key"])
        + _range("baB", "batch size B", 1, 800, p["B"])
        + _range("baF", "fixed cost per batch call, &micro;$", 50, 40000, p["F"], 50)
        + _range("baLam", "arrival rate &lambda;, items a second", 5, 5000, p["lam"], 5)
        + _range("baShare", "call it flat when the fixed share is this much of v", 2, 100, p["share"])
        + _range("baTimer", "flush timer, ms", 5, 3000, p["timer"], 5)
        + _kpi([
            ("baUnit", "Cost per item"),
            ("baSaving", "Against B = 1"),
            ("baWaitMean", "Mean added wait"),
            ("baWaitFirst", "First item waits"),
            ("baRule", "The rule of thumb B/&lambda;"),
            ("baAdvised", "Where the curve is flat"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", BATCH_PRESETS) + BATCH_SCRIPT
    return Lab(
        title="Batching: cost and latency",
        subtitle="One curve down, one curve up, and no B that is best at both",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the costs, the arrival rate and the batch"),
        panel_intro=cfg.get(
            "panel_intro",
            "F/B + v and the two exact waits — (B−1)/λ for the first item, half that on "
            "average — are fractions of the numbers you set. B/λ is the rule of thumb and is "
            "printed beside them, overstating the first item's wait by exactly one inter-arrival time.",
        ),
        script=script,
    )


# ============================================================= mode: vertical

VERTICAL_PRESETS = [
    {
        "key": "web-tier",
        "label": "a web tier: 500 rps a node at $100, a ladder at 10% premium a doubling",
        "target": 5, "premium": 110, "alpha": 50, "node": 100, "box": 100, "unit": 500,
        "what": "a stateless web tier",
    },
    {
        "key": "steep-ladder",
        "label": "a steep ladder: 40% a doubling — horizontal wins almost at once",
        "target": 5, "premium": 140, "alpha": 50, "node": 100, "box": 100, "unit": 500,
        "what": "a licensed appliance priced by socket",
    },
    {
        "key": "chatty-fleet",
        "label": "coordination α = 0.02: the fleet has its own ceiling at 50 nodes' worth",
        "target": 16, "premium": 110, "alpha": 200, "node": 100, "box": 100, "unit": 500,
        "what": "a fleet sharing one lock service",
    },
    {
        "key": "cheap-big-box",
        "label": "a big box discounted to $70 at the smallest rung",
        "target": 8, "premium": 115, "alpha": 50, "node": 100, "box": 70, "unit": 500,
        "what": "a managed database with a committed-use discount",
    },
]

VERTICAL_SCRIPT = r"""
  var sel = document.getElementById('vtPreset');
  var plot = document.getElementById('vtPlot');
  var status = document.getElementById('vtStatus');
  var table = document.getElementById('vtTable');
  var MAXT = 64, NODELIMIT = 6000;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('vertical: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('vtT').value = p.target;
    document.getElementById('vtM').value = p.premium;
    document.getElementById('vtA').value = p.alpha;
    document.getElementById('vtN').value = p.node;
    document.getElementById('vtB').value = p.box;
  }
  function state() {
    var p = preset();
    return {
      p: p,
      t: +document.getElementById('vtT').value,
      premium: R(BigInt(+document.getElementById('vtM').value), 100n),
      alpha: R(BigInt(+document.getElementById('vtA').value), 10000n),
      node: R(BigInt(+document.getElementById('vtN').value), 1n),
      box: R(BigInt(+document.getElementById('vtB').value), 1n),
      unit: R(BigInt(p.unit), 1n)
    };
  }

  function draw(st, first, breakeven) {
    var top = 0, t, hv, vv, hs = [], vs = [];
    for (t = 1; t <= MAXT; t += 1) {
      var N = horizontalNodes(t, st.alpha, NODELIMIT);
      hv = N === null ? null : ratioApprox(horizontalCost(N, st.node), R(1n, 1n));
      vv = ratioApprox(verticalCost(t, st.box, st.premium), R(1n, 1n));
      hs.push(hv); vs.push(vv);
      if (hv !== null && hv > top) top = hv;
      if (vv > top) top = vv;
    }
    top *= 1.1;
    if (!(top > 0)) top = 1;
    var x = function (v) { return 50 + (v - 1) / (MAXT - 1) * 594; };
    var y = function (v) { return 172 - v / top * 146; };
    var s = '';
    if (breakeven !== null) {
      s += '<rect x="' + x(breakeven).toFixed(1) + '" y="24" width="' + (x(MAXT) - x(breakeven)).toFixed(1)
        + '" height="148" fill="var(--cyan)" opacity="0.08" />';
    }
    var hp = '', vp = '', started = false;
    for (t = 1; t <= MAXT; t += 1) {
      vp += (t === 1 ? 'M' : 'L') + x(t).toFixed(1) + ' ' + y(vs[t - 1]).toFixed(1) + ' ';
      if (hs[t - 1] !== null) {
        hp += (started ? 'L' : 'M') + x(t).toFixed(1) + ' ' + y(hs[t - 1]).toFixed(1) + ' ';
        started = true;
      }
    }
    s += '<path d="' + vp + '" fill="none" stroke="var(--amber)" stroke-width="2.2" />'
      + '<path d="' + hp + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />';
    if (first !== null) {
      s += '<line x1="' + x(first).toFixed(1) + '" y1="24" x2="' + x(first).toFixed(1)
        + '" y2="172" stroke="var(--purple)" stroke-width="1.3" stroke-dasharray="3 3" />'
        + '<text x="' + (x(first) + 4).toFixed(1) + '" y="36" font-size="10" fill="var(--purple)">first crossing '
        + first + '×</text>';
    }
    if (breakeven !== null) {
      s += '<line x1="' + x(breakeven).toFixed(1) + '" y1="24" x2="' + x(breakeven).toFixed(1)
        + '" y2="172" stroke="var(--green)" stroke-width="1.6" stroke-dasharray="5 3" />'
        + '<text x="' + (x(breakeven) + 4).toFixed(1) + '" y="50" font-size="10" fill="var(--green)">'
        + 'horizontal wins from ' + breakeven + '× on</text>';
    }
    s += '<line x1="' + x(st.t).toFixed(1) + '" y1="24" x2="' + x(st.t).toFixed(1)
      + '" y2="172" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="50" y1="172" x2="644" y2="172" stroke="var(--line-strong)" />'
      + '<text x="50" y="188" font-size="10" fill="var(--muted)">1× a node</text>'
      + '<text x="644" y="188" text-anchor="end" font-size="10" fill="var(--muted)">' + MAXT + '×</text>'
      + '<text x="6" y="32" font-size="10" fill="var(--muted)">$ / month</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    document.getElementById('vtTOut').textContent = st.t + '× a node = '
      + Rnice(Rmul(st.unit, R(BigInt(st.t), 1n)), 0) + ' rps wanted';
    document.getElementById('vtMOut').textContent = Rnice(st.premium, 2) + '× the price for 2× the size';
    document.getElementById('vtAOut').textContent = 'α = ' + Rtext(st.alpha) + ' (fleet ceiling '
      + (Rzero(st.alpha) ? 'none' : Rnice(Rinv(st.alpha), 1) + '×') + ')';
    document.getElementById('vtNOut').textContent = money(st.node) + ' a small node, a month';
    document.getElementById('vtBOut').textContent = money(st.box) + ' for the smallest single box';

    var N = horizontalNodes(st.t, st.alpha, NODELIMIT);
    var hCost = N === null ? null : horizontalCost(N, st.node);
    var rung = verticalRung(st.t);
    var vCost = verticalCost(st.t, st.box, st.premium);
    var first = shapeFirstCrossing(st.box, st.node, st.premium, st.alpha, MAXT, NODELIMIT);
    var breakeven = shapeBreakEven(st.box, st.node, st.premium, st.alpha, MAXT, NODELIMIT);
    draw(st, first, breakeven);

    document.getElementById('vtNodes').textContent = N === null
      ? 'unreachable — 1/α is ' + Rnice(Rinv(st.alpha), 1) + '×' : N + ' nodes';
    document.getElementById('vtIdeal').textContent = st.t + ' nodes, if they never coordinated';
    document.getElementById('vtHcost').textContent = hCost === null ? '—' : money(hCost);
    document.getElementById('vtVcost').textContent = money(vCost) + ' (rung ' + rung.rung + ', '
      + rung.units + '×)';
    document.getElementById('vtFirst').textContent = first === null ? 'never below ' + MAXT + '×' : first + '×';
    document.getElementById('vtBreak').textContent = breakeven === null
      ? 'not below ' + MAXT + '×' : breakeven + '×';

    var rows = '<thead><tr><th>capacity wanted</th><th>nodes, coordination included</th>'
      + '<th>horizontal $</th><th>rung</th><th>vertical $</th><th>cheaper</th></tr></thead><tbody>';
    var picks = [1, 2, 4, st.t, first, breakeven, 16, MAXT].filter(function (v, i, a) {
      return v !== null && v >= 1 && v <= MAXT && a.indexOf(v) === i;
    }).sort(function (a, b) { return a - b; });
    for (var i = 0; i < picks.length; i += 1) {
      var t = picks[i], n = horizontalNodes(t, st.alpha, NODELIMIT);
      var hc = n === null ? null : horizontalCost(n, st.node);
      var r = verticalRung(t), vc = verticalCost(t, st.box, st.premium);
      var wins = hc !== null && Rcmp(hc, vc) < 0;
      rows += '<tr><td>' + t + '×' + (t === st.t ? ' <span class="tone-amber">(shown)</span>' : '')
        + '</td><td>' + (n === null ? '— unreachable' : n + ' (ideal ' + t + ')')
        + '</td><td>' + (hc === null ? '—' : money(hc)) + '</td><td>2' + supNum(r.rung)
        + ' = ' + r.units + '×</td><td>' + money(vc) + '</td><td class="'
        + (wins ? 'tone-cyan' : 'tone-amber') + '">' + (wins ? 'horizontal' : 'vertical') + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'To serve ' + Rnice(Rmul(st.unit, R(BigInt(st.t), 1n)), 0) + ' rps for ' + st.p.what
      + ' — ' + st.t + '× a node — horizontal needs <strong>'
      + (N === null ? 'more nodes than exist' : N + ' nodes, not ' + st.t)
      + '</strong>, because N machines deliver N/(1 + α(N&minus;1)) machines’ worth, not N. '
      + 'That is the Universal Scalability Law’s contention term with β = 0, the same one lesson 2 '
      + 'draws, and it puts a ceiling of ' + (Rzero(st.alpha) ? 'none' : Rnice(Rinv(st.alpha), 1) + '×')
      + ' on the fleet itself. '
      + (hCost === null ? '' : 'That costs <strong>' + money(hCost) + '</strong> a month. ')
      + 'Vertically you buy rung ' + rung.rung + ' — ' + rung.units + '× a node, because you cannot buy '
      + 'half a machine size — at <strong>' + money(vCost) + '</strong>, a ladder priced at '
      + Rnice(st.premium, 2) + '× for each doubling. '
      + '<span class="tone-red">“Horizontal is always cheaper” is false here twice over:</span> '
      + (first === null
          ? 'across every capacity up to ' + MAXT + '× the single box wins.'
          : 'horizontal first wins at <strong>' + first + '×</strong>, then loses again — '
            + 'the ladder is a staircase and a rung you have just bought is cheap until it is full — '
            + 'and only from <strong>'
            + (breakeven === null ? 'beyond ' + MAXT + '×' : breakeven + '×')
            + '</strong> does it never lose again. The gap between those two numbers is the price of '
            + '“buy the next size up”.')
      + ' And the single box has no parallel path at all: one machine is one failure domain, '
      + 'which course 5 lesson 4 has already priced and this page does not repeat.';
  }

  ['vtT', 'vtM', 'vtA', 'vtN', 'vtB'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _vertical(cfg):
    """Lesson 4: N small machines with coordination against a superlinear ladder."""
    idx = _preset_index(cfg, VERTICAL_PRESETS, "vertical")
    p = VERTICAL_PRESETS[idx]
    markup = (
        _toolbar(
            "Vertical against horizontal",
            "a ladder that prices doublings against a fleet that coordinates",
            _swatch("tone-cyan", "N small machines")
            + _swatch("tone-amber", "one big machine")
            + _swatch("tone-purple", "first crossing")
            + _swatch("tone-green", "and past here horizontal never loses"),
        )
        + _stage(
            "vtStage", "vtPlot", 660, 196,
            "Monthly cost of a fleet against the cost of a single box, at each target capacity.",
            "A staircase of vertical prices crossed by the rising cost of a coordinating fleet.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="vtTable"></table></div>\n'
        '      <div class="status-banner" id="vtStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("vtPreset", "Worked example", [(q["key"], q["label"]) for q in VERTICAL_PRESETS], p["key"])
        + _range("vtT", "capacity wanted, in nodes' worth", 1, 64, p["target"])
        + _range("vtM", "price premium per doubling, %", 100, 250, p["premium"])
        + _range("vtA", "coordination &alpha;, in ten-thousandths", 0, 400, p["alpha"])
        + _range("vtN", "one small node, $ a month", 25, 400, p["node"], 5)
        + _range("vtB", "the smallest single box, $ a month", 25, 400, p["box"], 5)
        + _kpi([
            ("vtNodes", "Nodes actually needed"),
            ("vtIdeal", "Nodes if they never talked"),
            ("vtHcost", "Horizontal, a month"),
            ("vtVcost", "Vertical, a month"),
            ("vtFirst", "First crossing"),
            ("vtBreak", "Horizontal wins from"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", VERTICAL_PRESETS) + VERTICAL_SCRIPT
    return Lab(
        title="Vertical vs horizontal",
        subtitle="Coordination on one side, a price premium on the other",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Price a target capacity both ways"),
        panel_intro=cfg.get(
            "panel_intro",
            "The node count comes from the same contention term lesson 2 draws, so the two pages "
            "cannot disagree about what a fleet delivers. Both prices are exact, and the crossing "
            "is reported twice — the first target horizontal wins at, and the target past which "
            "it never loses again.",
        ),
        script=script,
    )


# ================================================================ mode: waste

WASTE_PRESETS = [
    {
        "key": "consumer-evening",
        "label": "course 1's consumer profile: one evening peak at 21:00, 250 rps a point",
        "shape": "evening", "hour": 21, "amp": 6, "base": 250, "rho": 70,
        "what": "a consumer app",
    },
    {
        "key": "office-hours",
        "label": "a business app: two humps either side of lunch",
        "shape": "office", "hour": 10, "amp": 5, "base": 180, "rho": 70,
        "what": "a business app",
    },
    {
        "key": "flat-internal",
        "label": "an internal service with no daily shape — the only profile that is not wasteful",
        "shape": "flat", "hour": 12, "amp": 0, "base": 300, "rho": 70,
        "what": "an internal service",
    },
    {
        "key": "nightly-batch",
        "label": "a nightly batch window: two hours carry the day",
        "shape": "batchwindow", "hour": 3, "amp": 9, "base": 120, "rho": 85,
        "what": "a nightly batch",
    },
]

WASTE_SCRIPT = r"""
  var sel = document.getElementById('waPreset');
  var barsEl = document.getElementById('waBars');
  var status = document.getElementById('waStatus');
  var hourS = document.getElementById('waHour'), liftS = document.getElementById('waLift');
  /* One hand edit per hour. redraw() only READS it, so a second redraw with no
     interaction between the two is the same drawing. */
  var LIFT = [];
  for (var z = 0; z < 24; z += 1) LIFT.push(100);

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('waste: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('waPeak').value = p.hour;
    document.getElementById('waAmp').value = p.amp;
    document.getElementById('waRho').value = p.rho;
    for (var i = 0; i < 24; i += 1) LIFT[i] = 100;
    liftS.value = 100;
  }
  function buckets() {
    var p = preset();
    var base = R(BigInt(p.base), 1n);
    var w = dayShape(p.shape, +document.getElementById('waPeak').value,
                     +document.getElementById('waAmp').value);
    var out = [];
    for (var h = 0; h < 24; h += 1) {
      out.push(Rmul(base, Rmul(R(BigInt(w[h]), 1n), R(BigInt(LIFT[h]), 100n))));
    }
    return out;
  }

  function draw(bs, st, paid, chosen) {
    var top = ratioApprox(paid, R(1n, 1n)) * 1.08;
    if (!(top > 0)) top = 1;
    var y = function (v) { return 168 - v / top * 142; };
    var s = '', h;
    /* what you pay for, and the band above the load that is the waste */
    var yp = y(ratioApprox(paid, R(1n, 1n)));
    s += '<rect x="22" y="' + yp.toFixed(1) + '" width="482" height="' + (168 - yp).toFixed(1)
      + '" fill="var(--red)" opacity="0.08" />';
    for (h = 0; h < 24; h += 1) {
      var x = 22 + h * 20;
      var hv = ratioApprox(bs[h], R(1n, 1n));
      var ytop = y(hv);
      /* the paid-for column, and the used part of it */
      s += '<rect x="' + x + '" y="' + yp.toFixed(1) + '" width="15" height="' + (168 - yp).toFixed(1)
        + '" rx="2" fill="var(--red)" opacity="0.13" />'
        + '<rect x="' + x + '" y="' + ytop.toFixed(1) + '" width="15" height="'
        + Math.max(1, 168 - ytop).toFixed(1) + '" rx="2" fill="'
        + (h === st.peakAt ? 'var(--amber)' : (h === chosen ? 'var(--purple)' : 'var(--cyan)'))
        + '" opacity="' + (h === st.peakAt || h === chosen ? '0.95' : '0.6') + '" />';
      if (h % 3 === 0) {
        s += '<text x="' + (x + 7) + '" y="184" text-anchor="middle" font-size="10" fill="var(--muted)">'
          + h + '</text>';
      }
    }
    var ym = y(ratioApprox(st.mean, R(1n, 1n)));
    s += '<line x1="18" y1="' + yp.toFixed(1) + '" x2="508" y2="' + yp.toFixed(1)
      + '" stroke="var(--red)" stroke-width="1.7" />'
      + '<text x="508" y="' + (yp - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--red)">'
      + 'paid for: peak/ρ = ' + Rnice(paid, 0) + ' rps</text>'
      + '<line x1="18" y1="' + ym.toFixed(1) + '" x2="508" y2="' + ym.toFixed(1)
      + '" stroke="var(--green)" stroke-width="1.5" stroke-dasharray="5 4" />'
      + '<text x="508" y="' + (ym + 12).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--green)">'
      + 'used: the mean, ' + Rnice(st.mean, 0) + ' rps</text>'
      + '<line x1="18" y1="168" x2="508" y2="168" stroke="var(--line-strong)" />';
    barsEl.innerHTML = s;
  }

  function redraw() {
    var p = preset(), chosen = +hourS.value;
    var rho = R(BigInt(+document.getElementById('waRho').value), 100n);
    var bs = buckets(), st = profileStats(bs);
    var paid = paidCapacity(st.peak, rho);
    var waste = wasteFraction(st.mean, st.peak, rho);
    document.getElementById('waPeakOut').textContent =
      document.getElementById('waPeak').value + ':00 is the busy centre';
    document.getElementById('waAmpOut').textContent = 'shape ' + document.getElementById('waAmp').value;
    document.getElementById('waRhoOut').textContent = 'ρ target ' + Rpct(rho, 0);
    document.getElementById('waHourOut').textContent = chosen + ':00, now at ' + LIFT[chosen] + '% of its shape';
    document.getElementById('waLiftOut').textContent = LIFT[chosen] + '%';
    draw(bs, st, paid, chosen);

    document.getElementById('waPaid').textContent = Rnice(paid, 0) + ' rps';
    document.getElementById('waUsed').textContent = Rnice(st.mean, 0) + ' rps';
    document.getElementById('waPeakV').textContent = Rnice(st.peak, 0) + ' rps at ' + st.peakAt + ':00';
    document.getElementById('waWaste').textContent = Rpct(waste, 1);
    document.getElementById('waExact').textContent = Rshort(waste, 4);
    document.getElementById('waRatio').textContent = st.peakToMean === null ? '—'
      : Rshort(st.peakToMean, 3) + '×';

    /* The misconception, priced: cut to what you USE and see what breaks. */
    var cut = hoursOver(bs, st.mean);
    var worstRho = rhoAt(st.peak, st.mean);
    status.innerHTML = 'The ' + p.what + ' peaks at <strong>' + Rnice(st.peak, 0) + ' rps</strong> and averages '
      + '<strong>' + Rnice(st.mean, 0) + ' rps</strong>, a ratio of '
      + (st.peakToMean === null ? '—' : '<strong>' + Rshort(st.peakToMean, 3) + '</strong>') + '. '
      + 'Running the peak hour at ρ = ' + Rpct(rho, 0) + ' means buying <strong>'
      + Rnice(paid, 0) + ' rps</strong> of capacity — peak over ρ — and using the mean of it, so '
      + 'the waste is 1 &minus; mean&middot;ρ/peak = <strong>' + Rshort(waste, 4) + ' = '
      + Rpct(waste, 1) + '</strong>. Note what that fraction does NOT contain: the size of the day '
      + 'cancels out, so doubling every bucket changes nothing. Only the SHAPE and ρ matter. '
      + '<span class="tone-red">“' + Rpct(Rsub(R(1n, 1n), Rdiv(st.mean, paid)), 0)
      + ' idle, so cut it” is the misconception</span>: cutting to the ' + Rnice(st.mean, 0)
      + ' rps you actually use leaves <strong>' + cut.hours + ' of the 24 hours</strong> over capacity, '
      + 'the worst by ' + Rnice(cut.worst, 0) + ' rps — and at the peak hour ρ would be '
      + (worstRho === null ? '—' : Rshort(worstRho, 3))
      + ', which course 3 says is not a busy queue but no steady state at all. '
      + 'The only profile with no waste is a flat one, and the way to flatten a profile is to put '
      + 'work on it that does not care when it runs.';
  }

  ['waPeak', 'waAmp', 'waRho'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  hourS.addEventListener('input', function () { liftS.value = LIFT[+hourS.value]; redraw(); });
  liftS.addEventListener('input', function () { LIFT[+hourS.value] = +liftS.value; redraw(); });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _waste(cfg):
    """Lesson 5: you pay for peak/rho and you use the mean."""
    idx = _preset_index(cfg, WASTE_PRESETS, "waste")
    p = WASTE_PRESETS[idx]
    markup = (
        _toolbar(
            "Utilisation and waste",
            "you pay for peak/&rho; and you use the mean",
            _swatch("tone-cyan", "load in the hour")
            + _swatch("tone-amber", "the peak hour")
            + _swatch("tone-purple", "the hour you are editing")
            + _swatch("tone-red", "capacity paid for and not used")
            + _swatch("tone-green", "the mean"),
        )
        + _stage(
            "waStage", "waBars", 520, 192,
            "Hourly load against the capacity bought for the peak, with the unused band shaded.",
            "Twenty-four hourly bars inside a taller block of paid-for capacity, with the mean marked.",
        )
        + '      <div class="status-banner" id="waStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("waPreset", "Worked example", [(q["key"], q["label"]) for q in WASTE_PRESETS], p["key"])
        + _range("waPeak", "when the busy period is centred", 0, 23, p["hour"])
        + _range("waAmp", "how pronounced the shape is", 0, 12, p["amp"])
        + _range("waRho", "target utilisation &rho; at the peak, %", 30, 95, p["rho"])
        + _range("waHour", "reshape one hour by hand: which hour", 0, 23, 12)
        + _range("waLift", "… and its height, as a % of the shape", 0, 300, 100, 5)
        + _kpi([
            ("waPaid", "Capacity paid for"),
            ("waUsed", "Capacity used"),
            ("waPeakV", "The peak hour"),
            ("waWaste", "Waste"),
            ("waExact", "Waste, exactly"),
            ("waRatio", "Peak / mean"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", WASTE_PRESETS) + WASTE_SCRIPT
    return Lab(
        title="Utilisation and waste",
        subtitle="The gap between what you buy and what you use",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Reshape the day and set the target utilisation"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each bucket is an exact multiple of the profile's base, so the mean, the peak and "
            "1 − mean·ρ/peak are exact fractions. The size of the day cancels out of "
            "the waste entirely: only the shape and ρ move it.",
        ),
        script=script,
    )


# ============================================================== mode: reserve

RESERVE_PRESETS = [
    {
        "key": "evening-fleet",
        "label": "an evening fleet: 7¢/h reserved against 12¢/h on demand, so u* = 7/12",
        "shape": "evening", "hour": 21, "amp": 4,
        "res": 7, "dem": 12, "spot": 4, "q": 15,
        "what": "an evening-peaking web fleet",
    },
    {
        "key": "deep-commitment",
        "label": "a three-year commitment at 3¢/h: u* = 1/4, and the reserve climbs into the shoulder",
        "shape": "evening", "hour": 21, "amp": 4,
        "res": 3, "dem": 12, "spot": 4, "q": 15,
        "what": "the same fleet on a three-year commitment",
    },
    {
        "key": "barely-worth-it",
        "label": "a commitment at 11¢/h against 12¢/h: u* = 11/12, and almost nothing is worth reserving",
        "shape": "evening", "hour": 21, "amp": 6,
        "res": 11, "dem": 12, "spot": 4, "q": 15,
        "what": "a fleet on a one-month commitment",
    },
    {
        "key": "spiky-batch",
        "label": "a nightly batch: two hours of spike, and spot at 4¢/h with a 40% interruption rate",
        "shape": "batchwindow", "hour": 3, "amp": 6,
        "res": 7, "dem": 12, "spot": 4, "q": 40,
        "what": "a nightly batch fleet",
    },
]

RESERVE_SCRIPT = r"""
  var sel = document.getElementById('rsPreset');
  var barsEl = document.getElementById('rsBars');
  var status = document.getElementById('rsStatus');
  var table = document.getElementById('rsTable');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('reserve: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('rsPeak').value = p.hour;
    document.getElementById('rsAmp').value = p.amp;
    document.getElementById('rsR').value = p.res;
    document.getElementById('rsD').value = p.dem;
    document.getElementById('rsQ').value = p.q;
  }
  function state() {
    var p = preset();
    var w = dayShape(p.shape, +document.getElementById('rsPeak').value,
                     +document.getElementById('rsAmp').value);
    var bs = [];
    for (var h = 0; h < 24; h += 1) bs.push(R(BigInt(w[h]), 1n));
    return {
      p: p, buckets: bs, weights: w,
      res: R(BigInt(+document.getElementById('rsR').value), 100n),
      dem: R(BigInt(+document.getElementById('rsD').value), 100n),
      spot: R(BigInt(p.spot), 100n),
      q: R(BigInt(+document.getElementById('rsQ').value), 100n)
    };
  }

  function draw(st, level) {
    var top = 0, h;
    for (h = 0; h < 24; h += 1) if (st.weights[h] > top) top = st.weights[h];
    top *= 1.12;
    if (!(top > 0)) top = 1;
    var y = function (v) { return 166 - v / top * 140; };
    var s = '', yl = y(level);
    s += '<rect x="22" y="' + yl.toFixed(1) + '" width="482" height="' + (166 - yl).toFixed(1)
      + '" fill="var(--green)" opacity="0.10" />';
    for (h = 0; h < 24; h += 1) {
      var x = 22 + h * 20, v = st.weights[h];
      var base = Math.min(v, level), over = Math.max(0, v - level);
      s += '<rect x="' + x + '" y="' + y(base).toFixed(1) + '" width="15" height="'
        + Math.max(1, 166 - y(base)).toFixed(1) + '" rx="2" fill="var(--green)" opacity="0.75" />';
      if (over > 0) {
        s += '<rect x="' + x + '" y="' + y(v).toFixed(1) + '" width="15" height="'
          + (y(base) - y(v)).toFixed(1) + '" rx="2" fill="var(--amber)" opacity="0.9" />';
      }
      if (h % 3 === 0) {
        s += '<text x="' + (x + 7) + '" y="182" text-anchor="middle" font-size="10" fill="var(--muted)">'
          + h + '</text>';
      }
    }
    s += '<line x1="18" y1="' + yl.toFixed(1) + '" x2="508" y2="' + yl.toFixed(1)
      + '" stroke="var(--green)" stroke-width="1.8" />'
      + '<text x="508" y="' + (yl - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--green)">'
      + 'reserve ' + level + ' instances</text>'
      + '<text x="26" y="' + (y(top / 1.12) - 6).toFixed(1) + '" font-size="10" fill="var(--amber)">'
      + 'everything above the line is bought on demand</text>'
      + '<line x1="18" y1="166" x2="508" y2="166" stroke="var(--line-strong)" />';
    barsEl.innerHTML = s;
  }

  function redraw() {
    var st = state();
    var u = breakEvenUtilisation(st.res, st.dem);
    var level = reserveLevelMarginal(st.buckets, st.res, st.dem);
    var stats = profileStats(st.buckets);
    var peak = Number(stats.peak.n);
    var searched = reserveLevelSearch(st.buckets, st.res, st.dem, peak);
    document.getElementById('rsPeakOut').textContent =
      document.getElementById('rsPeak').value + ':00 is the busy centre';
    document.getElementById('rsAmpOut').textContent = 'shape ' + document.getElementById('rsAmp').value;
    document.getElementById('rsROut').textContent = document.getElementById('rsR').value + '¢/h reserved';
    document.getElementById('rsDOut').textContent = document.getElementById('rsD').value + '¢/h on demand';
    document.getElementById('rsQOut').textContent = Rpct(st.q, 0) + ' of spot hours reclaimed';
    draw(st, level);

    var best = mixCost(st.buckets, level, st.res, st.dem);
    var allDemand = mixCost(st.buckets, 0, st.res, st.dem);
    var allReserved = mixCost(st.buckets, peak, st.res, st.dem);
    var saving = Rsub(allDemand.total, best.total);

    document.getElementById('rsU').textContent = u === null ? '—' : Rtext(u) + ' = ' + Rpct(u, 1);
    document.getElementById('rsLevel').textContent = level + ' instances';
    document.getElementById('rsSearch').textContent = searched.level + ' instances';
    document.getElementById('rsCost').textContent = money(best.total) + ' a day';
    document.getElementById('rsSaved').textContent = money(saving) + ' a day ('
      + Rpct(Rdiv(saving, allDemand.total), 1) + ')';
    var q = spotBreakEvenRate(st.spot, st.dem);
    document.getElementById('rsSpot').textContent = q === null ? '—' : Rtext(q) + ' = ' + Rpct(q, 1);

    var rows = '<thead><tr><th>plan</th><th>reserved instance-hours</th><th>on-demand instance-hours</th>'
      + '<th>cost a day</th><th>against all on demand</th></tr></thead><tbody>';
    var plans = [
      ['all on demand, reserve nothing', 0],
      ['reserve the optimum', level],
      ['reserve the peak (the misconception)', peak]
    ];
    for (var i = 0; i < plans.length; i += 1) {
      var lv = plans[i][1], c = mixCost(st.buckets, lv, st.res, st.dem);
      var delta = Rsub(allDemand.total, c.total);
      rows += '<tr><td>' + plans[i][0] + '</td><td>' + (lv * 24) + '</td><td>'
        + Rnice(c.burstUnits, 0) + '</td><td>' + money(c.total) + '</td><td class="'
        + (Rcmp(delta, R(0n, 1n)) > 0 ? 'tone-green' : (Rzero(delta) ? 'tone-muted' : 'tone-red')) + '">'
        + (Rcmp(delta, R(0n, 1n)) > 0 ? 'saves ' + money(delta)
            : (Rzero(delta) ? 'the baseline' : 'costs ' + money(Rsub(R(0n, 1n), delta)) + ' more'))
        + '</td></tr>';
    }
    /* Spot as a fourth arm, priced with its interruption model rather than
       with its sticker. */
    var eff = spotExpectedPrice(st.spot, st.dem, st.q);
    var spotPlan = Radd(Rmul(Rmul(R(BigInt(level), 1n), R(24n, 1n)), st.res), Rmul(best.burstUnits, eff));
    var spotDelta = Rsub(allDemand.total, spotPlan);
    rows += '<tr><td>reserve the optimum, burst onto <strong>spot</strong> at ' + money(st.spot)
      + '/h with ' + Rpct(st.q, 0) + ' reclaimed</td><td>' + (level * 24) + '</td><td>'
      + Rnice(best.burstUnits, 0) + ' at ' + money(eff) + ' expected</td><td>' + money(spotPlan)
      + '</td><td class="' + (Rcmp(spotDelta, R(0n, 1n)) > 0 ? 'tone-green' : 'tone-red') + '">'
      + (Rcmp(spotDelta, R(0n, 1n)) > 0 ? 'saves ' + money(spotDelta)
          : 'costs ' + money(Rsub(R(0n, 1n), spotDelta)) + ' more') + '</td></tr>';
    table.innerHTML = rows + '</tbody>';

    var hours = hoursAbove(st.buckets, level);
    status.innerHTML = 'For ' + st.p.what + ', a reserved instance-hour costs '
      + money(st.res) + ' and an on-demand one ' + money(st.dem) + ', so the break-even utilisation is '
      + 'u* = reserved/on-demand = <strong>' + Rtext(u) + ' = ' + Rpct(u, 1)
      + '</strong>: a reserved instance pays for itself exactly when it runs more than that share of the time. '
      + 'Raising the reserved level by one costs 24&thinsp;&times;&thinsp;' + money(st.res)
      + ' a day and saves ' + money(st.dem) + ' for each hour the profile is above it, so it is worth '
      + 'raising while the hours-above share still exceeds u*. That stops at <strong>' + level
      + ' instances</strong>, where ' + hours + ' of 24 hours (' + Rpct(R(BigInt(hours), 24n), 1)
      + ') are still above — and searching every level from 0 to ' + peak + ' agrees: '
      + searched.level + '. The bill falls from ' + money(allDemand.total) + ' to <strong>'
      + money(best.total) + '</strong> a day. '
      + '<span class="tone-red">Reserving the peak instead</span> costs ' + money(allReserved.total)
      + ', because the peak hour’s instances would sit paid-for and idle for the other 23. '
      + 'Spot is not simply cheaper: an interrupted hour must be re-bought on demand, so a delivered '
      + 'spot hour costs s + q&middot;d = <strong>' + money(eff) + '</strong> expected, and spot only '
      + 'beats on demand while q &lt; (d&minus;s)/d = <strong>' + Rtext(q) + ' = ' + Rpct(q, 1)
      + '</strong>. At ' + Rpct(st.q, 0) + ' reclaimed it '
      + (spotWorthIt(st.spot, st.dem, st.q) ? 'does' : '<span class="tone-red">does not</span>') + '. '
      + 'When the profile is a forecast rather than a known shape this is a newsvendor problem and the '
      + 'optimum is a quantile — Operations Research inventory-models/the-newsvendor-problem.';
  }

  ['rsPeak', 'rsAmp', 'rsR', 'rsD', 'rsQ'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _reserve(cfg):
    """Lesson 6: u*, the level the marginal argument picks, and spot with a model."""
    idx = _preset_index(cfg, RESERVE_PRESETS, "reserve")
    p = RESERVE_PRESETS[idx]
    markup = (
        _toolbar(
            "Reserved, on-demand and spot",
            "the break-even is a price ratio; the level is a quantile",
            _swatch("tone-green", "reserved")
            + _swatch("tone-amber", "bought on demand"),
        )
        + _stage(
            "rsStage", "rsBars", 520, 190,
            "Hourly instance demand split by a reserved level, with the burst above it on demand.",
            "Twenty-four hourly bars cut by a reserved level, green below and amber above.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="rsTable"></table></div>\n'
        '      <div class="status-banner" id="rsStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("rsPreset", "Worked example", [(q["key"], q["label"]) for q in RESERVE_PRESETS], p["key"])
        + _range("rsPeak", "when the busy period is centred", 0, 23, p["hour"])
        + _range("rsAmp", "how pronounced the shape is", 0, 10, p["amp"])
        + _range("rsR", "reserved price, ¢ an instance-hour", 1, 24, p["res"])
        + _range("rsD", "on-demand price, ¢ an instance-hour", 2, 40, p["dem"])
        + _range("rsQ", "spot hours reclaimed, %", 0, 90, p["q"])
        + _kpi([
            ("rsU", "Break-even utilisation u*"),
            ("rsLevel", "Reserve, by the marginal rule"),
            ("rsSearch", "… and by searching every level"),
            ("rsCost", "Cost of the optimal mix"),
            ("rsSaved", "Saved against all on demand"),
            ("rsSpot", "Spot break-even interruption rate"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", RESERVE_PRESETS) + RESERVE_SCRIPT
    return Lab(
        title="Reserved vs on-demand",
        subtitle="Reserve the floor, buy the spikes, and price spot's interruptions",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set both prices and reshape the profile"),
        panel_intro=cfg.get(
            "panel_intro",
            "u* is the price ratio exactly. The optimal reserved level is found twice — by the "
            "marginal rule, which never evaluates a total, and by costing every level from zero to "
            "the peak — and the two must agree. Spot is priced with an interruption model, "
            "because without one it is only a smaller number.",
        ),
        script=script,
    )


# ============================================================ mode: autoscale

AUTOSCALE_PRESETS = [
    {
        "key": "instance-boot",
        "label": "a 90 s instance boot against a 50 rps/s ramp for five minutes, no reserve",
        "base": 5000, "rate": 50, "tau": 90, "dur": 300, "reserve": 0,
        "what": "a fleet of instances that take 90 seconds to boot",
    },
    {
        "key": "warm-pool",
        "label": "the same ramp with a 4500 rps warm pool — exactly r·τ, and the shortfall vanishes",
        "base": 5000, "rate": 50, "tau": 90, "dur": 300, "reserve": 4500,
        "what": "the same fleet with a warm pool held",
    },
    {
        "key": "container-start",
        "label": "a 10 s container start: the same ramp, a ninth of the boot, a much smaller triangle",
        "base": 5000, "rate": 50, "tau": 10, "dur": 300, "reserve": 0,
        "what": "a fleet of containers that start in ten seconds",
    },
    {
        "key": "flash-spike",
        "label": "a 30 s flash spike at 300 rps/s — the ramp is over before the fleet moves",
        "base": 5000, "rate": 300, "tau": 90, "dur": 30, "reserve": 0,
        "what": "a broadcast spike shorter than the boot window",
    },
]

AUTOSCALE_SCRIPT = r"""
  var sel = document.getElementById('asPreset');
  var plot = document.getElementById('asPlot');
  var status = document.getElementById('asStatus');
  var table = document.getElementById('asTable');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('autoscale: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('asRate').value = p.rate;
    document.getElementById('asTau').value = p.tau;
    document.getElementById('asDur').value = p.dur;
    document.getElementById('asRes').value = p.reserve;
  }
  function state() {
    var p = preset();
    return {
      p: p,
      base: R(BigInt(p.base), 1n),
      rate: R(BigInt(+document.getElementById('asRate').value), 1n),
      tau: R(BigInt(+document.getElementById('asTau').value), 1n),
      dur: R(BigInt(+document.getElementById('asDur').value), 1n),
      reserve: R(BigInt(+document.getElementById('asRes').value), 1n),
      tauN: +document.getElementById('asTau').value,
      durN: +document.getElementById('asDur').value
    };
  }

  function draw(st) {
    var span = st.durN + st.tauN + 60, i, t;
    if (span < 60) span = 60;
    var top = ratioApprox(Radd(Radd(st.base, st.reserve), Rmul(st.rate, st.dur)), R(1n, 1n)) * 1.12;
    if (!(top > 0)) top = 1;
    var x = function (s2) { return 50 + s2 / span * 590; };
    var y = function (v) { return 174 - v / top * 148; };
    var s = '', dem = '', cap = '', fill = '';
    for (i = 0; i <= span; i += 1) {
      t = R(BigInt(i), 1n);
      var d = ratioApprox(autoscaleDemand(st.base, st.rate, st.dur, t), R(1n, 1n));
      var c = ratioApprox(autoscaleCapacity(st.base, st.reserve, st.rate, st.tau, st.dur, t), R(1n, 1n));
      dem += (i === 0 ? 'M' : 'L') + x(i).toFixed(1) + ' ' + y(d).toFixed(1) + ' ';
      cap += (i === 0 ? 'M' : 'L') + x(i).toFixed(1) + ' ' + y(c).toFixed(1) + ' ';
    }
    /* the shortfall, as an area: demand on top, capacity beneath, back again */
    for (i = 0; i <= span; i += 1) {
      t = R(BigInt(i), 1n);
      var dv = autoscaleDemand(st.base, st.rate, st.dur, t);
      var cv = autoscaleCapacity(st.base, st.reserve, st.rate, st.tau, st.dur, t);
      var hi = Rcmp(dv, cv) > 0 ? dv : cv;
      fill += (i === 0 ? 'M' : 'L') + x(i).toFixed(1) + ' '
        + y(ratioApprox(hi, R(1n, 1n))).toFixed(1) + ' ';
    }
    for (i = span; i >= 0; i -= 1) {
      t = R(BigInt(i), 1n);
      var cv2 = autoscaleCapacity(st.base, st.reserve, st.rate, st.tau, st.dur, t);
      fill += 'L' + x(i).toFixed(1) + ' ' + y(ratioApprox(cv2, R(1n, 1n))).toFixed(1) + ' ';
    }
    s += '<path d="' + fill + 'Z" fill="var(--red)" opacity="0.22" />'
      + '<path d="' + cap + '" fill="none" stroke="var(--green)" stroke-width="2.2" />'
      + '<path d="' + dem + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />'
      + '<line x1="' + x(st.tauN).toFixed(1) + '" y1="26" x2="' + x(st.tauN).toFixed(1)
      + '" y2="174" stroke="var(--amber)" stroke-width="1.3" stroke-dasharray="4 3" />'
      + '<text x="' + (x(st.tauN) + 4).toFixed(1) + '" y="38" font-size="10" fill="var(--amber)">'
      + 'τ = ' + st.tauN + ' s: the first new instance is ready</text>'
      + '<line x1="' + x(st.durN).toFixed(1) + '" y1="26" x2="' + x(st.durN).toFixed(1)
      + '" y2="174" stroke="var(--muted)" stroke-width="1" stroke-dasharray="2 4" />'
      + '<text x="' + (x(st.durN) + 4).toFixed(1) + '" y="52" font-size="10" fill="var(--muted)">'
      + 'D = ' + st.durN + ' s: the ramp stops</text>'
      + '<line x1="50" y1="174" x2="640" y2="174" stroke="var(--line-strong)" />'
      + '<text x="50" y="190" font-size="10" fill="var(--muted)">t = 0</text>'
      + '<text x="640" y="190" text-anchor="end" font-size="10" fill="var(--muted)">' + span + ' s</text>'
      + '<text x="6" y="34" font-size="10" fill="var(--muted)">rps</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    document.getElementById('asRateOut').textContent = Rnice(st.rate, 0) + ' rps a second of ramp';
    document.getElementById('asTauOut').textContent = 'τ = ' + Rnice(st.tau, 0) + ' s to boot';
    document.getElementById('asDurOut').textContent = 'D = ' + Rnice(st.dur, 0) + ' s of ramp';
    document.getElementById('asResOut').textContent = Rnice(st.reserve, 0) + ' rps held warm';
    draw(st);

    var sh = autoscaleShortfall(st.rate, st.tau, st.dur, st.reserve);
    var closed = autoscaleTrapezoid(st.rate, st.tau, st.dur);
    var need = autoscaleReserveNeeded(st.rate, st.tau);
    var worstT = Rcmp(st.tau, st.dur) <= 0 ? st.tau : st.dur;
    var dem = autoscaleDemand(st.base, st.rate, st.dur, worstT);
    var cap = autoscaleCapacity(st.base, st.reserve, st.rate, st.tau, st.dur, worstT);
    var rho = rhoAt(dem, cap);
    var growth = backlogGrowth(dem, cap);
    var factor = rho === null ? null : responseFactor(rho);
    var drain = Rzero(st.reserve) || Rzero(sh.area) ? null : Rdiv(sh.area, st.reserve);

    document.getElementById('asShort').textContent = Rnice(sh.area, 0) + ' requests';
    document.getElementById('asClosed').textContent = Rnice(closed, 0) + ' requests';
    document.getElementById('asNeed').textContent = Rnice(need, 0) + ' rps';
    document.getElementById('asRho').textContent = rho === null ? '—' : Rshort(rho, 4);
    document.getElementById('asGrowth').textContent = Rnice(growth, 0) + ' req/s';
    document.getElementById('asDrain').textContent = Rzero(sh.area) ? 'nothing to drain'
      : (drain === null ? 'never — no spare capacity' : fmtSecs(drain));

    var rows = '<thead><tr><th>moment</th><th>demand λ</th><th>capacity μ in service</th>'
      + '<th>ρ = λ/μ</th><th>backlog growth λ−μ</th>'
      + '<th>W/S = 1/(1−ρ)</th></tr></thead><tbody>';
    var marks = [[0, 'the ramp starts'], [Math.floor(st.tauN / 2), 'half way through the boot'],
                 [st.tauN, 'τ: the first instance is ready'],
                 [st.durN, 'D: the ramp stops'],
                 [st.durN + st.tauN, 'the fleet has caught up']];
    for (var i = 0; i < marks.length; i += 1) {
      var t = R(BigInt(marks[i][0]), 1n);
      var d = autoscaleDemand(st.base, st.rate, st.dur, t);
      var c = autoscaleCapacity(st.base, st.reserve, st.rate, st.tau, st.dur, t);
      var r = rhoAt(d, c), g = backlogGrowth(d, c), f = r === null ? null : responseFactor(r);
      rows += '<tr><td>t = ' + marks[i][0] + ' s, ' + marks[i][1] + '</td><td>' + Rnice(d, 0)
        + '</td><td>' + Rnice(c, 0) + '</td><td class="'
        + (r !== null && Rcmp(r, R(1n, 1n)) >= 0 ? 'tone-red' : 'tone-green') + '">'
        + (r === null ? '—' : Rshort(r, 4)) + '</td><td>' + Rnice(g, 0) + '</td><td>'
        + (f === null ? 'no steady state' : Rnice(f, 2) + '×') + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'For ' + st.p.what + ', demand climbs at ' + Rnice(st.rate, 0)
      + ' rps a second while capacity does not move for ' + Rnice(st.tau, 0)
      + ' seconds — so the fleet is permanently <strong>r·τ = ' + Rnice(need, 0)
      + ' rps</strong> behind. The shortfall is the area between the two lines: a triangle of '
      + Rnice(sh.triangle, 0) + ' while the ramp and the boot overlap, then a rectangle of '
      + Rnice(sh.rectangle, 0) + ', <strong>' + Rnice(sh.area, 0) + ' requests</strong> in total'
      + (Rzero(st.reserve) && Rcmp(st.dur, st.tau) >= 0
          ? ' — and r·τ·(D − τ/2) = ' + Rnice(closed, 0)
            + ', the closed form, agrees exactly.'
          : '. (The lesson’s r·τ·(D − τ/2) = ' + Rnice(closed, 0)
            + ' assumes no reserve and a ramp longer than the boot; the area above is the general case.)')
      + ' At the worst instant λ = ' + Rnice(dem, 0) + ' rps against μ = ' + Rnice(cap, 0)
      + ' rps in service, so <strong>ρ = ' + (rho === null ? '—' : Rshort(rho, 4))
      + '</strong> — the same λ/μ course 3 defines, and '
      + (rho !== null && Rcmp(rho, R(1n, 1n)) >= 0
          ? '<span class="tone-red">above 1 there is no steady state at all</span>: the backlog grows at '
            + 'λ−μ = ' + Rnice(growth, 0) + ' requests a second, which is what the shaded '
            + 'area is measuring.'
          : 'below 1, so the queue is finite and the response time multiplier 1/(1−ρ) is '
            + (factor === null ? '—' : Rnice(factor, 2) + '×') + '.')
      + ' <span class="tone-amber">Autoscaling does not handle a spike; a reserve does.</span> '
      + 'Hold ' + Rnice(need, 0) + ' rps warm and the shortfall is exactly zero, because the reserve '
      + 'covers precisely the capacity the boot window costs. '
      + (Rzero(st.reserve)
          ? 'With no reserve there is also nothing spare once the ramp ends, so the backlog that built '
            + 'up never drains: capacity and demand end level.'
          : 'The ' + Rnice(st.reserve, 0) + ' rps you are holding is also the only spare capacity after '
            + 'the ramp, so the backlog drains at that rate — '
            + (drain === null ? 'and there is none left to drain.' : fmtSecs(drain) + ' of it.'));
  }

  ['asRate', 'asTau', 'asDur', 'asRes'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _autoscale(cfg):
    """Lesson 7: the trapezoid the boot window leaves behind, and the reserve that voids it."""
    idx = _preset_index(cfg, AUTOSCALE_PRESETS, "autoscale")
    p = AUTOSCALE_PRESETS[idx]
    markup = (
        _toolbar(
            "Autoscaling lag",
            "the fleet is always r&middot;&tau; behind, and the gap has an area",
            _swatch("tone-cyan", "demand")
            + _swatch("tone-green", "capacity in service")
            + _swatch("tone-red", "the shortfall")
            + _swatch("tone-amber", "&tau;, the boot window"),
        )
        + _stage(
            "asStage", "asPlot", 660, 198,
            "Demand ramping away from capacity during the boot window, with the shortfall shaded.",
            "A rising demand line with a lagging capacity line beneath it and the area between them filled.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="asTable"></table></div>\n'
        '      <div class="status-banner" id="asStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("asPreset", "Worked example", [(q["key"], q["label"]) for q in AUTOSCALE_PRESETS], p["key"])
        + _range("asRate", "ramp rate r, rps a second", 5, 500, p["rate"], 5)
        + _range("asTau", "boot time &tau;, seconds", 0, 300, p["tau"], 5)
        + _range("asDur", "ramp length D, seconds", 10, 900, p["dur"], 10)
        + _range("asRes", "reserve held warm, rps", 0, 20000, p["reserve"], 100)
        + _kpi([
            ("asShort", "Shortfall"),
            ("asClosed", "r&middot;&tau;&middot;(D &minus; &tau;/2)"),
            ("asNeed", "Reserve that removes it"),
            ("asRho", "&rho; at the worst instant"),
            ("asGrowth", "Backlog growth &lambda;&minus;&mu;"),
            ("asDrain", "Time to drain it afterwards"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", AUTOSCALE_PRESETS) + AUTOSCALE_SCRIPT
    return Lab(
        title="Autoscaling lag",
        subtitle="A boot window is a shortfall with an area, and a reserve is what removes it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the ramp, the boot time and the reserve"),
        panel_intro=cfg.get(
            "panel_intro",
            "The shortfall is the exact area between demand and the capacity actually in service, "
            "and r·τ·(D − τ/2) is printed beside it as the check. ρ is "
            "λ/μ — course 3's definition, not a second one — so the same two "
            "consequences apply: above 1 the backlog grows at λ−μ, and below it the "
            "response time multiplier is 1/(1−ρ).",
        ),
        script=script,
    )


# ================================================================= mode: unit

UNIT_PRESETS = [
    {
        "key": "api-with-egress",
        "label": "an API at 500M requests a month, 120 kB out of each one",
        "vol": 52, "fixed": 4000, "vcost": 1, "ret": 12,
        "bytes": 2000, "out": 120000, "storagePrice": 23, "egressPrice": 9000,
        "what": "a public API serving 120 kB responses",
    },
    {
        "key": "thin-responses",
        "label": "the same service answering 2 kB — egress stops mattering",
        "vol": 52, "fixed": 4000, "vcost": 1, "ret": 12,
        "bytes": 2000, "out": 2000, "storagePrice": 23, "egressPrice": 9000,
        "what": "the same service answering 2 kB",
    },
    {
        "key": "early-days",
        "label": "the same service at 2M requests a month — the fixed cost is the whole bill",
        "vol": 38, "fixed": 4000, "vcost": 1, "ret": 12,
        "bytes": 2000, "out": 120000, "storagePrice": 23, "egressPrice": 9000,
        "what": "the same service in its first month",
    },
    {
        "key": "seven-year-retention",
        "label": "a logging service keeping 84 months of 20 kB events",
        "vol": 50, "fixed": 4000, "vcost": 1, "ret": 36,
        "bytes": 20000, "out": 1000, "storagePrice": 23, "egressPrice": 9000,
        "what": "a logging service with a long retention",
    },
]

UNIT_SCRIPT = r"""
  var sel = document.getElementById('unPreset');
  var plot = document.getElementById('unPlot');
  var status = document.getElementById('unStatus');
  var table = document.getElementById('unTable');
  var TONES = { fixed: 'var(--purple)', compute: 'var(--cyan)',
                storage: 'var(--green)', egress: 'var(--amber)' };
  var NAMES = { fixed: 'fixed, shared out', compute: 'compute',
                storage: 'storage', egress: 'egress' };

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('unit: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('unVol').value = p.vol;
    document.getElementById('unFix').value = p.fixed;
    document.getElementById('unVar').value = p.vcost;
    document.getElementById('unRet').value = p.ret;
  }
  function state() {
    var p = preset();
    return {
      p: p,
      volIdx: +document.getElementById('unVol').value,
      volume: ladderValue(+document.getElementById('unVol').value),
      cfg: {
        fixedMonthly: R(BigInt(+document.getElementById('unFix').value), 1n),
        variablePerRequest: R(BigInt(+document.getElementById('unVar').value), 1000000n),
        bytesPerRequest: R(BigInt(p.bytes), 1n),
        retentionMonths: R(BigInt(+document.getElementById('unRet').value), 1n),
        storagePrice: R(BigInt(p.storagePrice), 1000n),
        bytesOut: R(BigInt(p.out), 1n),
        egressPrice: R(BigInt(p.egressPrice), 100000n)
      }
    };
  }

  function draw(st, parts) {
    var lo = 30, hi = 66, i;                       /* ladder rungs: 10^5 .. 10^11 */
    var top = ratioApprox(unitCost(st.cfg, ladderValue(lo)).total, R(1n, 1n)) * 1.05;
    if (!(top > 0)) top = 1;
    var x = function (idx) { return 54 + (idx - lo) / (hi - lo) * 588; };
    var y = function (v) { return 168 - Math.min(v, top) / top * 140; };
    var s = '', keys = ['fixed', 'compute', 'storage', 'egress'], k;
    /* stacked, so the reader sees which band is thick where */
    var prev = [];
    for (i = lo; i <= hi; i += 1) prev.push(0);
    for (k = 0; k < keys.length; k += 1) {
      var up = '', down = '';
      for (i = lo; i <= hi; i += 1) {
        var pc = unitCost(st.cfg, ladderValue(i));
        var below = prev[i - lo];
        var above = below + ratioApprox(pc[keys[k]], R(1n, 1n));
        up += (i === lo ? 'M' : 'L') + x(i).toFixed(1) + ' ' + y(above).toFixed(1) + ' ';
        prev[i - lo] = above;
      }
      for (i = hi; i >= lo; i -= 1) {
        var pc2 = unitCost(st.cfg, ladderValue(i));
        down += 'L' + x(i).toFixed(1) + ' '
          + y(prev[i - lo] - ratioApprox(pc2[keys[k]], R(1n, 1n))).toFixed(1) + ' ';
      }
      s += '<path d="' + up + down + 'Z" fill="' + TONES[keys[k]] + '" opacity="0.5" />';
    }
    for (i = lo; i <= hi; i += 6) {
      s += '<text x="' + x(i).toFixed(1) + '" y="184" text-anchor="middle" font-size="10" fill="var(--muted)">'
        + powTen(Math.floor(i / 6)) + '</text>';
    }
    s += '<line x1="' + x(st.volIdx).toFixed(1) + '" y1="24" x2="' + x(st.volIdx).toFixed(1)
      + '" y2="168" stroke="var(--text)" stroke-width="1.4" />'
      + '<text x="' + (x(st.volIdx) + 4).toFixed(1) + '" y="36" font-size="10" fill="var(--text)">'
      + Rnice(st.volume, 0) + ' req/month</text>'
      + '<line x1="54" y1="168" x2="642" y2="168" stroke="var(--line-strong)" />'
      + '<text x="6" y="32" font-size="10" fill="var(--muted)">$ / request</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    var parts = unitCost(st.cfg, st.volume);
    document.getElementById('unVolOut').textContent = Rnice(st.volume, 0) + ' requests a month';
    document.getElementById('unFixOut').textContent = money(st.cfg.fixedMonthly) + ' a month, fixed';
    document.getElementById('unVarOut').textContent = document.getElementById('unVar').value
      + ' µ$ of compute a request';
    document.getElementById('unRetOut').textContent = Rnice(st.cfg.retentionMonths, 0) + ' months retained';
    draw(st, parts);

    var winner = dominantTerm(parts);
    var cross = fixedCrossing(st.cfg.fixedMonthly, parts.egress);
    document.getElementById('unTotal').textContent = money(parts.total);
    document.getElementById('unMonthly').textContent = money(parts.monthly) + ' a month';
    document.getElementById('unEgress').textContent = money(parts.egress);
    document.getElementById('unStorage').textContent = money(parts.storage);
    document.getElementById('unWinner').textContent = NAMES[winner];
    document.getElementById('unCross').textContent = cross === null ? '—'
      : Rnice(cross, 0) + ' req/month';

    var rows = '<thead><tr><th>term</th><th>where it comes from</th><th>$ per request</th>'
      + '<th>share</th><th>$ a month</th><th>does it fall with volume?</th></tr></thead><tbody>';
    var keys = ['fixed', 'compute', 'storage', 'egress'];
    var whys = {
      fixed: 'fixed ÷ volume',
      compute: 'the variable cost you set',
      storage: 'bytes × retention × price/GB-month',
      egress: 'bytes out × price/GB'
    };
    for (var i = 0; i < keys.length; i += 1) {
      var k = keys[i];
      rows += '<tr><td><span class="' + (k === 'fixed' ? 'tone-purple'
        : (k === 'compute' ? 'tone-cyan' : (k === 'storage' ? 'tone-green' : 'tone-amber')))
        + '"><i class="legend-swatch"></i>' + NAMES[k] + '</span>'
        + (k === winner ? ' <strong>(the biggest)</strong>' : '')
        + '</td><td>' + whys[k] + '</td><td>' + money(parts[k]) + '</td><td>'
        + (Rzero(parts.total) ? '—' : Rpct(Rdiv(parts[k], parts.total), 1)) + '</td><td>'
        + money(Rmul(parts[k], st.volume)) + '</td><td>'
        + (k === 'fixed' ? '<span class="tone-green">yes, as 1/volume</span>'
            : '<span class="tone-red">no — flat per request</span>') + '</td></tr>';
    }
    rows += '<tr><td><strong>total</strong></td><td>the four added</td><td><strong>'
      + money(parts.total) + '</strong></td><td>100%</td><td><strong>' + money(parts.monthly)
      + '</strong></td><td>only through the fixed term</td></tr>';
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'At ' + Rnice(st.volume, 0) + ' requests a month, ' + st.p.what
      + ' costs <strong>' + money(parts.total) + ' a request</strong> and <strong>'
      + money(parts.monthly) + ' a month</strong>. Only one of the four terms falls with volume: '
      + 'the fixed ' + money(st.cfg.fixedMonthly) + ' shared out, which is ' + money(parts.fixed)
      + ' here. The other three are flat per request whatever the volume, so '
      + '<span class="tone-red">“cost scales with users” is wrong in both directions</span> '
      + '— the monthly total rises linearly and the unit cost falls. '
      + 'Storage is the term that does not follow traffic: ' + Rnice(st.cfg.bytesPerRequest, 0)
      + ' bytes held for ' + Rnice(st.cfg.retentionMonths, 0) + ' months is '
      + money(parts.storage) + ' a request, and doubling the retention doubles it while the request '
      + 'rate is untouched. <span class="tone-amber">Egress is the term that surprises:</span> '
      + Rnice(st.cfg.bytesOut, 0) + ' bytes at ' + moneyAt(st.cfg.egressPrice, 3) + ' a GB is '
      + money(parts.egress) + ' a request, which is ' + (Rzero(parts.compute) ? '—'
          : Rnice(Rdiv(parts.egress, parts.compute), 1) + '× the compute') + '. '
      + 'The biggest term here is <strong>' + NAMES[winner] + '</strong>. '
      + (cross === null ? ''
          : 'The fixed term stops being larger than egress at <strong>' + Rnice(cross, 0)
            + ' requests a month</strong> — fixed ÷ egress-per-request, an equality, not a curve read by eye.');
  }

  ['unVol', 'unFix', 'unVar', 'unRet'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _unit(cfg):
    """Lesson 8: four terms, one of which falls with volume and three of which do not."""
    idx = _preset_index(cfg, UNIT_PRESETS, "unit")
    p = UNIT_PRESETS[idx]
    markup = (
        _toolbar(
            "Cost per request",
            "compute, storage and egress, and the one term that falls with volume",
            _swatch("tone-purple", "fixed, shared out")
            + _swatch("tone-cyan", "compute")
            + _swatch("tone-green", "storage")
            + _swatch("tone-amber", "egress"),
        )
        + _stage(
            "unStage", "unPlot", 660, 190,
            "The four cost terms per request, stacked, against monthly volume.",
            "A stacked band chart in which only the lowest band narrows as volume rises.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="unTable"></table></div>\n'
        '      <div class="status-banner" id="unStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("unPreset", "Worked example", [(q["key"], q["label"]) for q in UNIT_PRESETS], p["key"])
        + _range("unVol", "requests a month", 30, 66, p["vol"])
        + _range("unFix", "fixed cost, $ a month", 0, 40000, p["fixed"], 100)
        + _range("unVar", "compute, &micro;$ a request", 0, 50, p["vcost"])
        + _range("unRet", "retention, months", 0, 60, p["ret"])
        + _kpi([
            ("unTotal", "Cost per request"),
            ("unMonthly", "Monthly total"),
            ("unEgress", "Egress per request"),
            ("unStorage", "Storage per request"),
            ("unWinner", "Biggest term"),
            ("unCross", "Fixed falls below egress at"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", UNIT_PRESETS) + UNIT_SCRIPT
    return Lab(
        title="Cost per request",
        subtitle="Decomposed, because the term that dominates is rarely the one you sized",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the volume, the costs and the retention"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each of the four terms is an exact fraction of the inputs, and only the fixed one "
            "depends on volume. The crossing where it stops being the largest is fixed ÷ "
            "egress-per-request — an equality solved, not a curve read off by eye.",
        ),
        script=script,
    )


# ================================================================= mode: tier

TIER_PRESETS = [
    {
        "key": "log-archive",
        "label": "logs: 2.3¢ hot, 0.4¢ cold, 1¢ a GB to read — a* = 1.9 reads a GB-month",
        "hot": 23, "cold": 4, "retrieval": 10, "base": 8, "decay": 50, "gb": 1000,
        "what": "a log archive",
    },
    {
        "key": "expensive-retrieval",
        "label": "deep archive: 0.1¢ cold, but 5¢ a GB to read — a* falls to 0.44",
        "hot": 23, "cold": 1, "retrieval": 50, "base": 8, "decay": 50, "gb": 1000,
        "what": "a deep archive with an expensive read",
    },
    {
        "key": "slow-decay",
        "label": "a media library whose reads only fall 10% a month — nothing is ever cold enough",
        "hot": 23, "cold": 4, "retrieval": 10, "base": 8, "decay": 90, "gb": 1000,
        "what": "a media library",
    },
    {
        "key": "cold-on-arrival",
        "label": "a compliance dump read twice a year — cold from month zero",
        "hot": 23, "cold": 4, "retrieval": 10, "base": 1, "decay": 50, "gb": 1000,
        "what": "a compliance dump",
    },
]

TIER_SCRIPT = r"""
  var sel = document.getElementById('tiPreset');
  var barsEl = document.getElementById('tiBars');
  var status = document.getElementById('tiStatus');
  var table = document.getElementById('tiTable');
  var AGES = 24;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('tier: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('tiHot').value = p.hot;
    document.getElementById('tiCold').value = p.cold;
    document.getElementById('tiRet').value = p.retrieval;
    document.getElementById('tiBase').value = p.base;
    document.getElementById('tiDecay').value = p.decay;
  }
  function state() {
    var p = preset();
    var hot = R(BigInt(+document.getElementById('tiHot').value), 1000n);
    var cold = R(BigInt(+document.getElementById('tiCold').value), 1000n);
    var retrieval = R(BigInt(+document.getElementById('tiRet').value), 1000n);
    var base = R(BigInt(+document.getElementById('tiBase').value), 1n);
    var decay = R(BigInt(+document.getElementById('tiDecay').value), 100n);
    var buckets = [];
    for (var age = 0; age < AGES; age += 1) {
      buckets.push({ gb: R(BigInt(p.gb), 1n), accesses: accessesAtAge(base, decay, age) });
    }
    return { p: p, hot: hot, cold: cold, retrieval: retrieval, base: base,
             decay: decay, buckets: buckets };
  }

  function draw(st, target, moveAge) {
    var top = ratioApprox(st.base, R(1n, 1n)) * 1.2;
    if (target !== null) {
      var tv = ratioApprox(target, R(1n, 1n)) * 1.2;
      if (tv > top) top = tv;
    }
    if (!(top > 0)) top = 1;
    var y = function (v) { return 158 - v / top * 128; };
    var s = '', age;
    if (moveAge !== null && moveAge < AGES) {
      s += '<rect x="' + (24 + moveAge * 20) + '" y="20" width="' + ((AGES - moveAge) * 20 - 4)
        + '" height="138" fill="var(--cyan)" opacity="0.09" />';
    }
    for (age = 0; age < AGES; age += 1) {
      var x = 24 + age * 20;
      var v = ratioApprox(st.buckets[age].accesses, R(1n, 1n));
      var cold = moveAge !== null && age >= moveAge;
      s += '<rect x="' + x + '" y="' + y(v).toFixed(1) + '" width="15" height="'
        + Math.max(1, 158 - y(v)).toFixed(1) + '" rx="2" fill="'
        + (cold ? 'var(--cyan)' : 'var(--amber)') + '" opacity="0.85" />';
      if (age % 3 === 0) {
        s += '<text x="' + (x + 7) + '" y="174" text-anchor="middle" font-size="10" fill="var(--muted)">'
          + age + '</text>';
      }
    }
    if (target !== null) {
      var yt = y(ratioApprox(target, R(1n, 1n)));
      s += '<line x1="20" y1="' + yt.toFixed(1) + '" x2="504" y2="' + yt.toFixed(1)
        + '" stroke="var(--green)" stroke-width="1.8" stroke-dasharray="6 4" />'
        + '<text x="504" y="' + (yt - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--green)">'
        + 'a* = ' + Rnice(target, 3) + ' reads a GB-month</text>';
    }
    if (moveAge !== null && moveAge < AGES) {
      s += '<text x="' + (28 + moveAge * 20) + '" y="32" font-size="10" fill="var(--cyan)">'
        + 'cold from month ' + moveAge + '</text>';
    } else {
      s += '<text x="28" y="32" font-size="10" fill="var(--amber)">'
        + 'nothing is read seldom enough to go cold</text>';
    }
    s += '<line x1="20" y1="158" x2="504" y2="158" stroke="var(--line-strong)" />'
      + '<text x="262" y="188" text-anchor="middle" font-size="10" fill="var(--muted)">age of the data, in months</text>';
    barsEl.innerHTML = s;
  }

  function redraw() {
    var st = state();
    var target = tierBreakEvenAccesses(st.hot, st.cold, st.retrieval);
    var moveAge = tierBreakEvenAge(st.base, st.decay, st.hot, st.cold, st.retrieval, AGES - 1);
    document.getElementById('tiHotOut').textContent = moneyAt(st.hot, 3) + ' a GB-month, hot';
    document.getElementById('tiColdOut').textContent = moneyAt(st.cold, 3) + ' a GB-month, cold';
    document.getElementById('tiRetOut').textContent = moneyAt(st.retrieval, 3) + ' a GB to read back';
    document.getElementById('tiBaseOut').textContent = Rnice(st.base, 0) + ' reads a GB in month 0';
    document.getElementById('tiDecayOut').textContent = Rpct(st.decay, 0) + ' of last month’s reads';
    draw(st, target, moveAge);

    var plan = tierPlan(st.buckets, st.hot, st.cold, st.retrieval, moveAge);
    document.getElementById('tiStar').textContent = target === null ? '—'
      : Rtext(target) + ' = ' + Rnice(target, 3) + ' reads/GB-month';
    document.getElementById('tiAge').textContent = moveAge === null
      ? 'never, inside ' + AGES + ' months' : 'month ' + moveAge;
    document.getElementById('tiSaving').textContent = money(plan.saving) + ' a month';
    document.getElementById('tiHotBill').textContent = money(plan.allHot) + ' a month';
    document.getElementById('tiTiered').textContent = money(plan.tiered) + ' a month';
    document.getElementById('tiMoved').textContent = Rnice(plan.movedGb, 0) + ' GB';

    var rows = '<thead><tr><th>age</th><th>reads a GB-month</th><th>all hot</th>'
      + '<th>cold: keep + read back</th><th>cheaper</th><th>tier chosen</th></tr></thead><tbody>';
    var picks = [0, 1, 2];
    if (moveAge !== null) { picks.push(moveAge - 1); picks.push(moveAge); picks.push(moveAge + 1); }
    picks.push(AGES - 1);
    picks = picks.filter(function (v, i, aa) { return v >= 0 && v < AGES && aa.indexOf(v) === i; })
                 .sort(function (x, y) { return x - y; });
    for (var i = 0; i < picks.length; i += 1) {
      var age = picks[i], b = st.buckets[age];
      var h = tierCost(b.gb, b.accesses, st.hot, st.cold, st.retrieval, false);
      var c = tierCost(b.gb, b.accesses, st.hot, st.cold, st.retrieval, true);
      var coldWins = Rcmp(c.total, h.total) < 0;
      rows += '<tr><td>month ' + age + (age === moveAge ? ' <span class="tone-green">(a* reached)</span>' : '')
        + '</td><td>' + Rshort(b.accesses, 4) + '</td><td>' + money(h.total) + '</td><td>'
        + money(c.keep) + ' + ' + money(c.read) + ' = ' + money(c.total) + '</td><td class="'
        + (coldWins ? 'tone-cyan' : 'tone-amber') + '">' + (coldWins ? 'cold' : 'hot')
        + '</td><td>' + (moveAge !== null && age >= moveAge ? 'cold' : 'hot') + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'For ' + st.p.what + ', a GB costs ' + moneyAt(st.hot, 3) + ' a month hot and '
      + moneyAt(st.cold, 3) + ' cold, so moving it saves ' + moneyAt(Rsub(st.hot, st.cold), 3)
      + ' a month and costs ' + moneyAt(st.retrieval, 3) + ' every time it is read back. Setting those '
      + 'equal gives the break-even access rate <strong>a* = (hot &minus; cold)/retrieval = '
      + (target === null ? '—' : Rtext(target) + ' = ' + Rnice(target, 3))
      + ' reads a GB-month</strong>. Reads fall to ' + Rpct(st.decay, 0)
      + ' of the month before, so a*&nbsp;is crossed at <strong>'
      + (moveAge === null ? 'no age inside ' + AGES + ' months' : 'month ' + moveAge)
      + '</strong> — found by evaluating ' + Rnice(st.base, 0) + '&thinsp;&times;&thinsp;'
      + Rtext(st.decay) + '&#8319; exactly at each integer age, not by reading the curve. '
      + '<span class="tone-red">“Everything old should go cold” is the misconception</span>: '
      + (moveAge === null
          ? 'here nothing is read seldom enough, and tiering the whole archive would ADD to the bill.'
          : 'data younger than month ' + moveAge + ' is still read often enough that the retrieval '
            + 'charges exceed the storage saving, and moving it costs money rather than saving it.')
      + ' Tiering at the break-even age moves ' + Rnice(plan.movedGb, 0) + ' GB and takes the bill from '
      + money(plan.allHot) + ' to <strong>' + money(plan.tiered) + '</strong> a month, a saving of '
      + money(plan.saving) + '. Here <em>c</em> is the cold-tier price throughout and is never a server count.';
  }

  ['tiHot', 'tiCold', 'tiRet', 'tiBase', 'tiDecay'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _tier(cfg):
    """Lesson 9: (hot - cold)/retrieval, and the age at which the profile reaches it."""
    idx = _preset_index(cfg, TIER_PRESETS, "tier")
    p = TIER_PRESETS[idx]
    markup = (
        _toolbar(
            "Storage tiers",
            "the break-even is a price difference over a retrieval charge",
            _swatch("tone-amber", "read often enough to stay hot")
            + _swatch("tone-cyan", "cold enough to move")
            + _swatch("tone-green", "a*, the break-even access rate"),
        )
        + _stage(
            "tiStage", "tiBars", 520, 196,
            "Reads per GB-month falling with age, against the break-even access rate.",
            "A decaying bar chart of access rates crossed by a dashed break-even line.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="tiTable"></table></div>\n'
        '      <div class="status-banner" id="tiStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("tiPreset", "Worked example", [(q["key"], q["label"]) for q in TIER_PRESETS], p["key"])
        + _range("tiHot", "hot tier, tenths of a cent a GB-month", 5, 60, p["hot"])
        + _range("tiCold", "cold tier, tenths of a cent a GB-month", 1, 40, p["cold"])
        + _range("tiRet", "retrieval, tenths of a cent a GB read", 1, 200, p["retrieval"])
        + _range("tiBase", "reads a GB in the first month", 1, 64, p["base"])
        + _range("tiDecay", "reads kept each month, %", 10, 98, p["decay"])
        + _kpi([
            ("tiStar", "Break-even a*"),
            ("tiAge", "Break-even age"),
            ("tiSaving", "Saving from tiering there"),
            ("tiHotBill", "Everything hot"),
            ("tiTiered", "Tiered at a*"),
            ("tiMoved", "Data moved"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", TIER_PRESETS) + TIER_SCRIPT
    return Lab(
        title="Storage tiers and the access break-even",
        subtitle="Cold is cheaper to keep and dearer to read, and a* is where those meet",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set both prices, the retrieval charge and the decay"),
        panel_intro=cfg.get(
            "panel_intro",
            "a* = (hot − cold)/retrieval is exact, and the age at which the profile reaches it "
            "is an integer search over exact powers of the decay factor — not a curve read off "
            "by eye. Here c is the cold-tier price and is never a server count.",
        ),
        script=script,
    )


# ============================================================= mode: compress

COMPRESS_PATHS = [
    ("send", "compress, then send"),
    ("roundtrip", "compress, send, then decompress at the far end"),
]

COMPRESS_PRESETS = [
    {
        "key": "gigabit-link",
        "label": "10 GB over a 1 Gbit/s link, 4× at 250 MB/s — compression wins",
        "size": 60, "ratio": 40, "rate": 250, "bw": 1000, "dec": 800, "path": "send",
        "what": "a 10 GB dataset over a gigabit link",
    },
    {
        "key": "fast-link",
        "label": "the same file over 25 Gbit/s — no compressor here is fast enough",
        "size": 60, "ratio": 40, "rate": 250, "bw": 10000, "dec": 800, "path": "send",
        "what": "the same file over a 25 Gbit/s fabric",
    },
    {
        "key": "slow-wan",
        "label": "a 100 Mbit/s WAN — even a slow compressor pays",
        "size": 60, "ratio": 40, "rate": 60, "bw": 100, "dec": 300, "path": "send",
        "what": "the same file over a 100 Mbit/s WAN",
    },
    {
        "key": "counting-the-far-end",
        "label": "the same gigabit link with decompression on the critical path",
        "size": 60, "ratio": 40, "rate": 250, "bw": 1000, "dec": 300, "path": "roundtrip",
        "what": "a transfer whose reader must expand before it can start",
    },
]

COMPRESS_SCRIPT = r"""
  var sel = document.getElementById('cpPreset');
  var pathSel = document.getElementById('cpPath');
  var barsEl = document.getElementById('cpBars');
  var status = document.getElementById('cpStatus');
  var table = document.getElementById('cpTable');
  var MB = 1000000n;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('compress: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('cpSize').value = p.size;
    document.getElementById('cpRatio').value = p.ratio;
    document.getElementById('cpRate').value = p.rate;
    document.getElementById('cpBw').value = p.bw;
    document.getElementById('cpDec').value = p.dec;
    pathSel.value = p.path;
  }
  function state() {
    var roundtrip = pathSel.value === 'roundtrip';
    if (pathSel.value !== 'send' && !roundtrip) {
      throw new Error('compress: unknown transfer path ' + pathSel.value);
    }
    return {
      p: preset(),
      bytes: ladderValue(+document.getElementById('cpSize').value),
      ratio: R(BigInt(+document.getElementById('cpRatio').value), 10n),
      /* MB/s here is 10^6 bytes a second and Mbit/s is 10^6 BITS a second:
         the link is divided by 8 and the page says so, because mixing the two
         is a factor of eight and looks like a plausible answer. */
      rate: Rmul(R(BigInt(+document.getElementById('cpRate').value), 1n), R(MB, 1n)),
      bandwidth: Rdiv(Rmul(R(BigInt(+document.getElementById('cpBw').value), 1n), R(MB, 1n)), R(8n, 1n)),
      decRate: roundtrip
        ? Rmul(R(BigInt(+document.getElementById('cpDec').value), 1n), R(MB, 1n)) : null,
      roundtrip: roundtrip
    };
  }

  function draw(st, raw, comp) {
    var top = ratioApprox(raw, R(1n, 1n));
    var ct = ratioApprox(comp.total, R(1n, 1n));
    if (ct > top) top = ct;
    top *= 1.08;
    if (!(top > 0)) top = 1;
    var w = function (v) { return v / top * 400; };
    var s = '';
    s += '<text x="14" y="34" font-size="11" fill="var(--muted)">send it raw</text>'
      + '<rect x="96" y="22" width="' + w(ratioApprox(raw, R(1n, 1n))).toFixed(1)
      + '" height="22" rx="3" fill="var(--red)" opacity="0.75" />'
      + '<text x="' + (100 + w(ratioApprox(raw, R(1n, 1n)))).toFixed(1)
      + '" y="38" font-size="11" fill="var(--text)">' + fmtSecs(raw) + '</text>';
    var x0 = 96, parts = [['squeeze', comp.squeeze, 'var(--purple)'],
                          ['send', comp.send, 'var(--cyan)'],
                          ['expand', comp.expand, 'var(--green)']];
    s += '<text x="14" y="80" font-size="11" fill="var(--muted)">compress first</text>';
    for (var i = 0; i < parts.length; i += 1) {
      var wv = w(ratioApprox(parts[i][1], R(1n, 1n)));
      if (wv <= 0) continue;
      s += '<rect x="' + x0.toFixed(1) + '" y="68" width="' + Math.max(1, wv).toFixed(1)
        + '" height="22" rx="3" fill="' + parts[i][2] + '" opacity="0.8" />';
      if (wv > 34) {
        s += '<text x="' + (x0 + wv / 2).toFixed(1) + '" y="84" text-anchor="middle" font-size="10" '
          + 'fill="var(--text)">' + parts[i][0] + '</text>';
      }
      x0 += wv;
    }
    s += '<text x="' + (x0 + 4).toFixed(1) + '" y="84" font-size="11" fill="var(--text)">'
      + fmtSecs(comp.total) + '</text>';
    /* the crossing, drawn as the bandwidth axis rather than as a time */
    s += '<line x1="96" y1="108" x2="496" y2="108" stroke="var(--line-strong)" />'
      + '<text x="14" y="126" font-size="11" fill="var(--muted)">bandwidth</text>';
    var bwv = log10Approx(st.bandwidth), bev = null;
    var be = compressBreakEvenBandwidth(st.ratio, st.rate, st.decRate);
    if (be !== null && be.n > 0n) bev = log10Approx(be);
    var axLo = 5, axHi = 10.5;
    var xa = function (l) { return 96 + (l - axLo) / (axHi - axLo) * 400; };
    for (var d = Math.ceil(axLo); d <= Math.floor(axHi); d += 1) {
      s += '<line x1="' + xa(d).toFixed(1) + '" y1="122" x2="' + xa(d).toFixed(1)
        + '" y2="132" stroke="var(--line)" />'
        + '<text x="' + xa(d).toFixed(1) + '" y="146" text-anchor="middle" font-size="9" fill="var(--muted)">'
        + powTen(d) + ' B/s</text>';
    }
    if (bev !== null && bev >= axLo && bev <= axHi) {
      s += '<rect x="96" y="122" width="' + Math.max(0, xa(bev) - 96).toFixed(1)
        + '" height="10" fill="var(--green)" opacity="0.28" />'
        + '<rect x="' + xa(bev).toFixed(1) + '" y="122" width="' + Math.max(0, 496 - xa(bev)).toFixed(1)
        + '" height="10" fill="var(--red)" opacity="0.22" />'
        + '<line x1="' + xa(bev).toFixed(1) + '" y1="116" x2="' + xa(bev).toFixed(1)
        + '" y2="138" stroke="var(--green)" stroke-width="2" />'
        + '<text x="' + xa(bev).toFixed(1) + '" y="114" text-anchor="middle" font-size="10" fill="var(--green)">'
        + 'break-even ' + fmtBytes(be, 1) + '/s</text>';
    }
    if (bwv >= axLo && bwv <= axHi) {
      s += '<circle cx="' + xa(bwv).toFixed(1) + '" cy="127" r="5" fill="var(--amber)" />'
        + '<text x="' + xa(bwv).toFixed(1) + '" y="160" text-anchor="middle" font-size="10" fill="var(--amber)">'
        + 'this link</text>';
    }
    barsEl.innerHTML = s;
  }

  function redraw() {
    var st = state();
    document.getElementById('cpSizeOut').textContent = fmtBytes(st.bytes, 2) + ' to move';
    document.getElementById('cpRatioOut').textContent = Rnice(st.ratio, 1) + '× smaller once compressed';
    document.getElementById('cpRateOut').textContent = fmtBytes(st.rate, 0) + '/s compressing';
    document.getElementById('cpBwOut').textContent = document.getElementById('cpBw').value
      + ' Mbit/s = ' + fmtBytes(st.bandwidth, 1) + '/s';
    document.getElementById('cpDecOut').textContent = st.decRate === null
      ? 'not on the critical path' : fmtBytes(st.decRate, 0) + '/s decompressing';

    var raw = rawTime(st.bytes, st.bandwidth);
    var comp = compressedTime(st.bytes, st.bandwidth, st.ratio, st.rate, st.decRate);
    var be = compressBreakEvenBandwidth(st.ratio, st.rate, st.decRate);
    var rateStar = compressBreakEvenRate(st.ratio, st.bandwidth);
    draw(st, raw, comp);

    document.getElementById('cpRaw').textContent = fmtSecs(raw);
    document.getElementById('cpComp').textContent = fmtSecs(comp.total);
    document.getElementById('cpWin').textContent = Rcmp(comp.total, raw) < 0
      ? 'compress: ' + Rnice(Rdiv(raw, comp.total), 2) + '× faster'
      : 'send it raw: compressing is ' + Rnice(Rdiv(comp.total, raw), 2) + '× slower';
    document.getElementById('cpBe').textContent = be === null ? '—' : fmtBytes(be, 2) + '/s ('
      + Rnice(Rdiv(Rmul(be, R(8n, 1n)), R(1000000n, 1n)), 0) + ' Mbit/s)';
    document.getElementById('cpRateStar').textContent = rateStar === null ? '— ratio must exceed 1'
      : fmtBytes(rateStar, 2) + '/s';
    document.getElementById('cpBytes').textContent = fmtBytes(Rdiv(st.bytes, st.ratio), 2) + ' on the wire';

    var rows = '<thead><tr><th>step</th><th>how long it takes</th><th>seconds</th>'
      + '<th>share of the compressed plan</th></tr></thead><tbody>';
    var rowsData = [
      ['squeeze', 'size ÷ compressor rate', comp.squeeze],
      ['send', 'size ÷ (ratio × bandwidth)', comp.send]
    ];
    if (st.roundtrip) rowsData.push(['expand', 'size ÷ (ratio × decompressor rate)', comp.expand]);
    for (var i = 0; i < rowsData.length; i += 1) {
      rows += '<tr><td>' + rowsData[i][0] + '</td><td>' + rowsData[i][1] + '</td><td>'
        + fmtSecs(rowsData[i][2]) + '</td><td>'
        + (Rzero(comp.total) ? '—' : Rpct(Rdiv(rowsData[i][2], comp.total), 1)) + '</td></tr>';
    }
    rows += '<tr><td><strong>compressed, total</strong></td><td>the steps above, added</td><td><strong>'
      + fmtSecs(comp.total) + '</strong></td><td>100%</td></tr>'
      + '<tr><td class="tone-red"><strong>raw</strong></td><td>size ÷ bandwidth</td><td><strong>'
      + fmtSecs(raw) + '</strong></td><td>'
      + (Rzero(comp.total) ? '—' : Rnice(Rdiv(raw, comp.total), 2) + '× the compressed plan')
      + '</td></tr>';
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'Sending ' + fmtBytes(st.bytes, 2) + ' for ' + st.p.what + ' raw takes <strong>'
      + fmtSecs(raw) + '</strong>. Compressing ' + Rnice(st.ratio, 1) + '× first puts only '
      + fmtBytes(Rdiv(st.bytes, st.ratio), 2) + ' on the wire, but costs ' + fmtSecs(comp.squeeze)
      + ' to squeeze' + (st.roundtrip ? ' and ' + fmtSecs(comp.expand) + ' to expand at the far end' : '')
      + ', for <strong>' + fmtSecs(comp.total) + '</strong> in all. '
      + (Rcmp(comp.total, raw) < 0
          ? '<span class="tone-green">Compression wins here</span>, by '
            + Rnice(Rdiv(raw, comp.total), 2) + '×. '
          : '<span class="tone-red">Compression LOSES here</span>: the link is fast enough that the '
            + 'compressor is the bottleneck, and the squeeze costs more than the bytes it saves. ')
      + 'Setting the two times equal cancels the size entirely and leaves 1/bw = 1/rate'
      + (st.roundtrip ? ' + 1/(k&middot;drate)' : '') + ' + 1/(k&middot;bw), so the break-even bandwidth is '
      + '<strong>' + (be === null ? '—' : fmtBytes(be, 2) + '/s') + '</strong>'
      + (st.roundtrip ? '' : ' = rate&middot;(k&minus;1)/k')
      + ' — and read the other way round, on this link you would need a compressor faster than '
      + '<strong>' + (rateStar === null ? '—' : fmtBytes(rateStar, 2) + '/s')
      + '</strong> = bw&middot;k/(k&minus;1). <span class="tone-amber">“Always compress” is a '
      + 'habit from slow links.</span> Note also that the size never appears in the break-even: it '
      + 'decides how long both plans take and nothing about which one wins. '
      + 'Mbit/s here is 10⁶ bits a second and MB/s is 10⁶ bytes a second; the page divides by '
      + 'eight rather than leaving you to wonder.';
  }

  ['cpSize', 'cpRatio', 'cpRate', 'cpBw', 'cpDec'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  pathSel.addEventListener('change', redraw);
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _compress(cfg):
    """Lesson 10: two transfer times, and the bandwidth at which compressing stops paying."""
    idx = _preset_index(cfg, COMPRESS_PRESETS, "compress")
    p = COMPRESS_PRESETS[idx]
    markup = (
        _toolbar(
            "Compress or not",
            "the size cancels out; the link speed decides",
            _swatch("tone-red", "sent raw")
            + _swatch("tone-purple", "squeeze")
            + _swatch("tone-cyan", "send")
            + _swatch("tone-green", "expand, and the break-even"),
        )
        + _stage(
            "cpStage", "cpBars", 520, 168,
            "Raw transfer time against the compressed plan's three steps, and where this link sits against the break-even.",
            "Two horizontal time bars and a bandwidth axis split at the break-even.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="cpTable"></table></div>\n'
        '      <div class="status-banner" id="cpStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("cpPreset", "Worked example", [(q["key"], q["label"]) for q in COMPRESS_PRESETS], p["key"])
        + _select("cpPath", "What is on the critical path", COMPRESS_PATHS, p["path"])
        + _range("cpSize", "how much to move", 42, 72, p["size"])
        + _range("cpRatio", "compression ratio, tenths", 11, 200, p["ratio"])
        + _range("cpRate", "compressor, MB/s", 5, 2000, p["rate"], 5)
        + _range("cpBw", "link, Mbit/s", 10, 25000, p["bw"], 10)
        + _range("cpDec", "decompressor, MB/s", 5, 4000, p["dec"], 5)
        + _kpi([
            ("cpRaw", "Raw transfer"),
            ("cpComp", "Compressed plan"),
            ("cpWin", "Which wins"),
            ("cpBe", "Break-even bandwidth"),
            ("cpRateStar", "Compressor needed on this link"),
            ("cpBytes", "Bytes actually sent"),
        ])
    )
    script = (
        _CORE_JS
        + cfg_literal("PRESETS", COMPRESS_PRESETS)
        + COMPRESS_SCRIPT
    )
    return Lab(
        title="Compress or not",
        subtitle="A fast enough link outruns every compressor",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the file, the ratio, the compressor and the link"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both times are exact fractions. The break-even bandwidth is the equality solved rather "
            "than a curve read off: the size cancels out of it completely, so how much you are "
            "moving decides how long both plans take and nothing at all about which one wins.",
        ),
        script=script,
    )


# ============================================================ mode: placement

PLACEMENT_PRESETS = [
    {
        "key": "aggregate-a-table",
        "label": "2 TB scanned to produce a 5 MB aggregate, 200 kB of code",
        "data": 74, "result": 40, "code": 32, "bw": 1000,
        "what": "an aggregation over a 2 TB table",
    },
    {
        "key": "fat-result",
        "label": "the same table, but the job returns half of it",
        "data": 74, "result": 72, "code": 32, "bw": 1000,
        "what": "a job that returns 1 TB of rows",
    },
    {
        "key": "tiny-dataset",
        "label": "a 30 MB lookup table — small enough that moving it is fine",
        "data": 51, "result": 32, "code": 32, "bw": 1000,
        "what": "a 30 MB lookup table",
    },
    {
        "key": "fat-binary",
        "label": "a 700 MB container image against a 20 GB dataset",
        "data": 62, "result": 36, "code": 58, "bw": 1000,
        "what": "a job shipped as a 700 MB image",
    },
]

PLACEMENT_SCRIPT = r"""
  var sel = document.getElementById('plPreset');
  var barsEl = document.getElementById('plBars');
  var status = document.getElementById('plStatus');
  var table = document.getElementById('plTable');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('placement: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('plData').value = p.data;
    document.getElementById('plResult').value = p.result;
    document.getElementById('plCode').value = p.code;
    document.getElementById('plBw').value = p.bw;
  }
  function state() {
    return {
      p: preset(),
      data: ladderValue(+document.getElementById('plData').value),
      result: ladderValue(+document.getElementById('plResult').value),
      code: ladderValue(+document.getElementById('plCode').value),
      bandwidth: Rdiv(Rmul(R(BigInt(+document.getElementById('plBw').value), 1n), R(1000000n, 1n)), R(8n, 1n))
    };
  }

  function draw(st, tData, tCompute) {
    var top = ratioApprox(tData, R(1n, 1n));
    var tc = ratioApprox(tCompute, R(1n, 1n));
    if (tc > top) top = tc;
    if (!(top > 0)) top = 1;
    var w = function (v) { return Math.max(1.5, v / top * 360); };
    var s = '';
    s += '<text x="14" y="36" font-size="11" fill="var(--muted)">move the data</text>'
      + '<rect x="132" y="22" width="' + w(ratioApprox(tData, R(1n, 1n))).toFixed(1)
      + '" height="24" rx="3" fill="var(--red)" opacity="0.75" />'
      + '<text x="' + (136 + w(ratioApprox(tData, R(1n, 1n)))).toFixed(1)
      + '" y="39" font-size="11" fill="var(--text)">' + fmtSecs(tData) + '</text>'
      + '<text x="14" y="82" font-size="11" fill="var(--muted)">move the compute</text>';
    var x0 = 132;
    var wc = w(ratioApprox(st.code, R(1n, 1n)) / ratioApprox(st.bandwidth, R(1n, 1n)));
    var wr = w(ratioApprox(st.result, R(1n, 1n)) / ratioApprox(st.bandwidth, R(1n, 1n)));
    s += '<rect x="' + x0 + '" y="68" width="' + wc.toFixed(1)
      + '" height="24" rx="3" fill="var(--purple)" opacity="0.85" />'
      + '<rect x="' + (x0 + wc).toFixed(1) + '" y="68" width="' + wr.toFixed(1)
      + '" height="24" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (x0 + wc + wr + 4).toFixed(1) + '" y="85" font-size="11" fill="var(--text)">'
      + fmtSecs(tCompute) + '</text>'
      + '<text x="132" y="110" font-size="10" fill="var(--purple)">code</text>'
      + '<text x="172" y="110" font-size="10" fill="var(--cyan)">result</text>';
    /* the bytes themselves, on a log ruler, because the ratio is the lesson */
    var axLo = 3, axHi = 15;
    var xa = function (l) { return 132 + (l - axLo) / (axHi - axLo) * 360; };
    s += '<line x1="132" y1="140" x2="492" y2="140" stroke="var(--line-strong)" />';
    for (var d = Math.ceil(axLo); d <= Math.floor(axHi); d += 3) {
      s += '<text x="' + xa(d).toFixed(1) + '" y="156" text-anchor="middle" font-size="9" fill="var(--muted)">'
        + powTen(d) + ' B</text>';
    }
    var marks = [[st.data, 'var(--red)', 'dataset'], [st.result, 'var(--cyan)', 'result'],
                 [st.code, 'var(--purple)', 'code']];
    for (var i = 0; i < marks.length; i += 1) {
      var lv = log10Approx(marks[i][0]);
      if (!(lv >= axLo && lv <= axHi)) continue;
      s += '<circle cx="' + xa(lv).toFixed(1) + '" cy="140" r="5" fill="' + marks[i][1] + '" />'
        + '<text x="' + xa(lv).toFixed(1) + '" y="' + (128 - i * 12)
        + '" text-anchor="middle" font-size="9" fill="' + marks[i][1] + '">' + marks[i][2] + '</text>';
    }
    s += '<text x="14" y="144" font-size="11" fill="var(--muted)">the bytes</text>';
    barsEl.innerHTML = s;
  }

  function redraw() {
    var st = state();
    document.getElementById('plDataOut').textContent = fmtBytes(st.data, 2) + ' of data';
    document.getElementById('plResultOut').textContent = fmtBytes(st.result, 2) + ' of result';
    document.getElementById('plCodeOut').textContent = fmtBytes(st.code, 2) + ' of code';
    document.getElementById('plBwOut').textContent = document.getElementById('plBw').value
      + ' Mbit/s = ' + fmtBytes(st.bandwidth, 1) + '/s';

    var tData = moveDataTime(st.data, st.bandwidth);
    var tCompute = moveComputeTime(st.code, st.result, st.bandwidth);
    var ratio = resultRatio(st.result, st.data);
    var cross = placementCrossover(st.data, st.code);
    var speed = placementSpeedup(st.data, st.code, st.result);
    draw(st, tData, tCompute);

    document.getElementById('plData2').textContent = fmtSecs(tData);
    document.getElementById('plCompute').textContent = fmtSecs(tCompute);
    document.getElementById('plRatio').textContent = ratio === null ? '—'
      : Rshort(ratio, 6) + ' = ' + Rpct(ratio, 4);
    document.getElementById('plWin').textContent = Rcmp(tCompute, tData) < 0
      ? 'move the compute' : 'move the data';
    document.getElementById('plSpeed').textContent = speed === null ? '—'
      : Rnice(speed, 1) + '×';
    document.getElementById('plCross').textContent = fmtBytes(cross, 2) + ' of result';

    var rows = '<thead><tr><th>plan</th><th>what crosses the link</th><th>bytes</th>'
      + '<th>time at ' + fmtBytes(st.bandwidth, 1) + '/s</th></tr></thead><tbody>'
      + '<tr><td class="tone-red">move the data to the compute</td><td>the whole dataset</td><td>'
      + fmtBytes(st.data, 2) + '</td><td>' + fmtSecs(tData) + '</td></tr>'
      + '<tr><td class="tone-cyan">move the compute to the data</td><td>the code, then the result</td><td>'
      + fmtBytes(st.code, 2) + ' + ' + fmtBytes(st.result, 2) + ' = ' + fmtBytes(Radd(st.code, st.result), 2)
      + '</td><td>' + fmtSecs(tCompute) + '</td></tr>'
      + '<tr><td><strong>the crossing</strong></td><td>code + result = dataset</td><td><strong>'
      + fmtBytes(cross, 2) + '</strong> of result</td><td>both plans tie</td></tr></tbody>';
    table.innerHTML = rows;

    status.innerHTML = 'For ' + st.p.what + ', pulling the data to the compute means moving '
      + fmtBytes(st.data, 2) + ' and takes <strong>' + fmtSecs(tData) + '</strong>. Shipping the job '
      + 'instead means moving ' + fmtBytes(st.code, 2) + ' of code and bringing '
      + fmtBytes(st.result, 2) + ' of result back: <strong>' + fmtSecs(tCompute) + '</strong>'
      + (speed === null ? '' : ', ' + Rnice(speed, 1) + '× '
          + (Rcmp(speed, R(1n, 1n)) > 0 ? 'faster' : 'slower')) + '. '
      + 'The bandwidth divides both sides and cancels: the comparison is code + result against the '
      + 'dataset and nothing else, so the two plans tie at exactly <strong>' + fmtBytes(cross, 2)
      + '</strong> of result and a faster link moves neither the crossing nor the verdict. '
      + 'The result-to-input ratio here is <strong>' + (ratio === null ? '—' : Rshort(ratio, 6))
      + ' = ' + (ratio === null ? '—' : Rpct(ratio, 4)) + '</strong>, and that it is usually tiny '
      + 'is the whole reason a query language exists. '
      + '<span class="tone-red">Pulling everything to the client</span> is the misconception, and it '
      + 'is a misconception about this ratio rather than about bandwidth: it is wrong exactly when '
      + 'the result is smaller than the input, which is nearly always.';
  }

  ['plData', 'plResult', 'plCode', 'plBw'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _placement(cfg):
    """Lesson 11: D/bw against (code + result)/bw, where the bandwidth cancels."""
    idx = _preset_index(cfg, PLACEMENT_PRESETS, "placement")
    p = PLACEMENT_PRESETS[idx]
    markup = (
        _toolbar(
            "Move the data or the compute",
            "the link cancels; the result-to-input ratio decides",
            _swatch("tone-red", "the dataset")
            + _swatch("tone-purple", "the code")
            + _swatch("tone-cyan", "the result"),
        )
        + _stage(
            "plStage", "plBars", 520, 164,
            "The two transfer plans timed side by side, with the three sizes on a logarithmic ruler.",
            "Two horizontal time bars above a logarithmic ruler marking the dataset, result and code sizes.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="plTable"></table></div>\n'
        '      <div class="status-banner" id="plStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("plPreset", "Worked example", [(q["key"], q["label"]) for q in PLACEMENT_PRESETS], p["key"])
        + _range("plData", "the dataset", 36, 80, p["data"])
        + _range("plResult", "the result it produces", 18, 80, p["result"])
        + _range("plCode", "the code that produces it", 18, 62, p["code"])
        + _range("plBw", "link, Mbit/s", 10, 25000, p["bw"], 10)
        + _kpi([
            ("plData2", "Move the data"),
            ("plCompute", "Move the compute"),
            ("plRatio", "Result / input"),
            ("plWin", "Cheaper plan"),
            ("plSpeed", "How much cheaper"),
            ("plCross", "The two tie at"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", PLACEMENT_PRESETS) + PLACEMENT_SCRIPT
    return Lab(
        title="Move the data or the compute",
        subtitle="A comparison the link speed drops out of entirely",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the dataset, the result, the code and the link"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both times are exact. The crossing is code + result against the dataset — the "
            "bandwidth divides both sides and cancels — so a faster link changes how long both "
            "plans take and nothing about which of them wins.",
        ),
        script=script,
    )


# ============================================================= mode: headroom

HEADROOM_PRESETS = [
    {
        "key": "ninety-per-cent-of-ten",
        "label": "ten machines at ρ = 0.9 — lose one and ρ is exactly 1",
        "n": 10, "cap": 1000, "lam": 9000, "lost": 1, "rhomax": 90,
        "what": "a ten-machine tier run at ninety per cent",
    },
    {
        "key": "three-machines",
        "label": "three machines: losing one takes a THIRD of the fleet, not a tenth",
        "n": 3, "cap": 1000, "lam": 1800, "lost": 1, "rhomax": 90,
        "what": "a three-machine tier",
    },
    {
        "key": "two-zones",
        "label": "twelve machines across three zones — a zone is four of them at once",
        "n": 12, "cap": 1000, "lam": 7200, "lost": 4, "rhomax": 90,
        "what": "a twelve-machine tier spread over three zones",
    },
    {
        "key": "big-fleet",
        "label": "sixty machines at ρ = 0.9 — one loss barely moves it",
        "n": 60, "cap": 1000, "lam": 54000, "lost": 1, "rhomax": 90,
        "what": "a sixty-machine tier",
    },
]

HEADROOM_SCRIPT = r"""
  var sel = document.getElementById('hdPreset');
  var plot = document.getElementById('hdPlot');
  var status = document.getElementById('hdStatus');
  var table = document.getElementById('hdTable');
  var LIMIT = 4000;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('headroom: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('hdN').value = p.n;
    document.getElementById('hdCap').value = p.cap;
    document.getElementById('hdLam').value = p.lam;
    document.getElementById('hdLost').value = p.lost;
    document.getElementById('hdMax').value = p.rhomax;
  }
  function state() {
    var n = +document.getElementById('hdN').value;
    var lost = +document.getElementById('hdLost').value;
    if (lost >= n) lost = n - 1;
    return {
      p: preset(), n: n, lost: lost,
      cap: R(BigInt(+document.getElementById('hdCap').value), 1n),
      lam: R(BigInt(+document.getElementById('hdLam').value), 1n),
      rhomax: R(BigInt(+document.getElementById('hdMax').value), 100n)
    };
  }

  function draw(st, rho, after) {
    var cols = st.n > 30 ? 30 : st.n;
    var cell = Math.floor(470 / cols);
    if (cell < 6) cell = 6;
    var s = '', i;
    for (i = 0; i < st.n && i < 60; i += 1) {
      var row = Math.floor(i / cols), col = i % cols;
      var x = 26 + col * cell, y = 26 + row * 26;
      var dead = i >= st.n - st.lost;
      s += '<rect x="' + x + '" y="' + y + '" width="' + Math.max(4, cell - 4) + '" height="20" rx="3" fill="'
        + (dead ? 'var(--red)' : 'var(--green)') + '" opacity="' + (dead ? '0.55' : '0.8') + '" />';
      if (dead && cell >= 12) {
        s += '<line x1="' + x + '" y1="' + y + '" x2="' + (x + cell - 4) + '" y2="' + (y + 20)
          + '" stroke="var(--red)" stroke-width="1.4" />';
      }
    }
    var rows = Math.ceil(Math.min(st.n, 60) / cols);
    var baseY = 26 + rows * 26 + 14;
    /* two utilisation bars, before and after, with the rho = 1 wall drawn */
    var barW = 400;
    function bar(label, value, y, tone) {
      var frac = ratioApprox(value, R(1n, 1n));
      var full = Math.min(frac, 1.25);
      return '<text x="26" y="' + (y + 13) + '" font-size="10" fill="var(--muted)">' + label + '</text>'
        + '<rect x="120" y="' + y + '" width="' + barW + '" height="18" rx="3" fill="var(--line)" opacity="0.5" />'
        + '<rect x="120" y="' + y + '" width="' + (full / 1.25 * barW).toFixed(1)
        + '" height="18" rx="3" fill="' + tone + '" opacity="0.85" />'
        + '<line x1="' + (120 + barW / 1.25).toFixed(1) + '" y1="' + (y - 4) + '" x2="'
        + (120 + barW / 1.25).toFixed(1) + '" y2="' + (y + 22) + '" stroke="var(--red)" stroke-width="1.6" />'
        + '<text x="' + (124 + barW).toFixed(1) + '" y="' + (y + 13)
        + '" text-anchor="end" font-size="10" fill="var(--text)">ρ = ' + Rfixed(value, 3) + '</text>';
    }
    s += bar('every machine up', rho, baseY, 'var(--cyan)')
      + bar('after losing ' + st.lost, after === null ? R(0n, 1n) : after, baseY + 30, 'var(--amber)')
      + '<text x="' + (120 + barW / 1.25).toFixed(1) + '" y="' + (baseY - 8)
      + '" text-anchor="middle" font-size="10" fill="var(--red)">ρ = 1</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    var rho = fleetRho(st.lam, st.n, st.cap);
    var after = rhoAfterLoss(rho, st.n, st.lost);
    var frac = survivingFraction(st.n, st.lost);
    document.getElementById('hdNOut').textContent = st.n + ' machines';
    document.getElementById('hdCapOut').textContent = Rnice(st.cap, 0) + ' rps each';
    document.getElementById('hdLamOut').textContent = Rnice(st.lam, 0) + ' rps of demand';
    document.getElementById('hdLostOut').textContent = 'losing ' + st.lost + ' of ' + st.n;
    document.getElementById('hdMaxOut').textContent = 'ρ after the loss must stay under '
      + Rpct(st.rhomax, 0);
    draw(st, rho, after);

    var need = machinesForHeadroom(st.lam, st.cap, st.rhomax, st.lost, LIMIT);
    var needClosed = machinesForHeadroomClosed(st.lam, st.cap, st.rhomax, st.lost);
    var usable = usableUtilisation(st.rhomax, st.n, st.lost);
    var before = rho === null ? null : responseFactor(rho);
    var factorAfter = after === null ? null : responseFactor(after);

    document.getElementById('hdRho').textContent = rho === null ? '—' : Rshort(rho, 4);
    document.getElementById('hdAfter').textContent = after === null ? '—' : Rshort(after, 4);
    document.getElementById('hdFrac').textContent = Rtext(frac) + ' = ' + Rpct(frac, 2) + ' of nameplate';
    document.getElementById('hdNeed').textContent = need === null ? 'more than ' + LIMIT : need + ' machines';
    document.getElementById('hdClosed').textContent = needClosed === null ? '—' : needClosed + ' machines';
    document.getElementById('hdUsable').textContent = Rpct(usable, 2);

    var rows = '<thead><tr><th>state</th><th>machines carrying it</th><th>capacity μ</th>'
      + '<th>ρ = λ/μ</th><th>W/S = 1/(1−ρ)</th></tr></thead><tbody>';
    var states = [['every machine up', st.n], ['losing one', st.n - 1], ['losing ' + st.lost, st.n - st.lost]];
    for (var i = 0; i < states.length; i += 1) {
      var m = states[i][1];
      if (m < 1) continue;
      var mu = fleetCapacity(m, st.cap), r = fleetRho(st.lam, m, st.cap);
      var f = r === null ? null : responseFactor(r);
      rows += '<tr><td>' + states[i][0] + '</td><td>' + m + '</td><td>' + Rnice(mu, 0)
        + ' rps</td><td class="' + (r !== null && Rcmp(r, R(1n, 1n)) >= 0 ? 'tone-red' : 'tone-green')
        + '">' + (r === null ? '—' : Rshort(r, 4)) + '</td><td>'
        + (f === null ? '<span class="tone-red">no steady state</span>' : Rnice(f, 2) + '×')
        + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = 'With ' + st.n + ' machines at ' + Rnice(st.cap, 0) + ' rps each, ' + st.p.what
      + ' carries ' + Rnice(st.lam, 0) + ' rps at <strong>ρ = '
      + (rho === null ? '—' : Rshort(rho, 4)) + '</strong> — λ over μ, the same '
      + 'definition course 3 gives, with μ the capacity actually in service. '
      + 'Lose ' + st.lost + ' of the ' + st.n + ' and μ falls to <strong>' + Rtext(frac)
      + '</strong> of nameplate, so ρ is <em>multiplied</em> by N/(N−f) = '
      + Rtext(Rinv(frac)) + ' and becomes <strong>'
      + (after === null ? '—' : Rshort(after, 4)) + '</strong>. '
      + (after !== null && Rcmp(after, R(1n, 1n)) >= 0
          ? '<span class="tone-red">That is at or above 1: there is no steady state left.</span> '
            + 'The queue does not get slower, it grows without bound at λ−μ = '
            + Rnice(backlogGrowth(st.lam, fleetCapacity(st.n - st.lost, st.cap)), 0)
            + ' requests a second, and 1/(1−ρ) is not a number any more. '
          : 'Response time goes from ' + (before === null ? '—' : Rnice(before, 2) + '×')
            + ' the service time to ' + (factorAfter === null ? '—' : Rnice(factorAfter, 2) + '×')
            + ' — course 3 lesson 8’s 1/(1−ρ), the same hyperbola. ')
      + '<span class="tone-amber">Running at ρ = 0.9 leaves nothing for a failure</span>, and '
      + 'the number that actually matters is N−1 capacity: <strong>(N−1)/N = '
      + Rtext(survivingFraction(st.n, 1)) + '</strong> of nameplate, which on three machines is two '
      + 'thirds and on sixty is fifty-nine sixtieths. That is why a small fleet needs far more '
      + 'headroom than a large one for the same failure. '
      + 'To hold ρ at or under ' + Rpct(st.rhomax, 0) + ' after losing ' + st.lost + ', you need '
      + '<strong>' + (need === null ? 'more machines than the scan tries' : need) + '</strong> '
      + 'machines — by scanning, and by rearranging λ/((N−f)&middot;cap) ≤ ρ'
      + '<sub>max</sub> to N ≥ λ/(cap&middot;ρ<sub>max</sub>) + f, whose ceiling is '
      + (needClosed === null ? '—' : needClosed) + '. Equivalently, the utilisation you may plan '
      + 'for at ' + st.n + ' machines is ρ<sub>max</sub>&middot;(N−f)/N = <strong>'
      + Rpct(usable, 2) + '</strong>, not ' + Rpct(st.rhomax, 0) + '.';
  }

  ['hdN', 'hdCap', 'hdLam', 'hdLost', 'hdMax'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _headroom(cfg):
    """Headroom: what losing one of N does to rho, and the N that survives it."""
    idx = _preset_index(cfg, HEADROOM_PRESETS, "headroom")
    p = HEADROOM_PRESETS[idx]
    markup = (
        _toolbar(
            "Headroom and N&minus;1",
            "losing one of N multiplies &rho; by N/(N&minus;1)",
            _swatch("tone-green", "machines up")
            + _swatch("tone-red", "machines lost, and the &rho; = 1 wall")
            + _swatch("tone-cyan", "&rho; with the fleet whole")
            + _swatch("tone-amber", "&rho; after the loss"),
        )
        + _stage(
            "hdStage", "hdPlot", 520, 196,
            "The fleet with the lost machines struck out, and utilisation before and after the loss.",
            "A grid of machine blocks above two utilisation bars measured against a rho equals one wall.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="hdTable"></table></div>\n'
        '      <div class="status-banner" id="hdStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("hdPreset", "Worked example", [(q["key"], q["label"]) for q in HEADROOM_PRESETS], p["key"])
        + _range("hdN", "machines N", 2, 60, p["n"])
        + _range("hdCap", "capacity of one machine, rps", 100, 5000, p["cap"], 100)
        + _range("hdLam", "demand &lambda;, rps", 100, 60000, p["lam"], 100)
        + _range("hdLost", "machines lost at once", 1, 8, p["lost"])
        + _range("hdMax", "&rho; you will accept after the loss, %", 50, 99, p["rhomax"])
        + _kpi([
            ("hdRho", "&rho; with the fleet whole"),
            ("hdAfter", "&rho; after the loss"),
            ("hdFrac", "Capacity that survives"),
            ("hdNeed", "Machines needed, by scan"),
            ("hdClosed", "… and in closed form"),
            ("hdUsable", "&rho; you may plan for"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", HEADROOM_PRESETS) + HEADROOM_SCRIPT
    return Lab(
        title="Headroom and N−1 capacity",
        subtitle="The utilisation you can survive, not the one you can run",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Size the fleet against the failure you expect"),
        panel_intro=cfg.get(
            "panel_intro",
            "ρ is λ/μ — course 3's definition — with μ the capacity "
            "actually in service, so losing f of N multiplies it by N/(N−f) exactly. The machine "
            "count that holds a target is found by a scan and by rearranging the inequality, and the "
            "two integers must agree.",
        ),
        script=script,
    )


# =============================================================== mode: growth

GROWTH_PRESETS = [
    {
        "key": "ten-per-cent-a-month",
        "label": "5000 rps growing 10% a month against a 50 000 rps limit",
        "cur": 5000, "rate": 10, "limit": 50000, "cap": 1000, "rho": 70, "lead": 3,
        "what": "a service growing ten per cent a month",
    },
    {
        "key": "doubling-quarterly",
        "label": "26% a month — a doubling every quarter, and the limit inside a year",
        "cur": 5000, "rate": 26, "limit": 50000, "cap": 1000, "rho": 70, "lead": 3,
        "what": "a service doubling every quarter",
    },
    {
        "key": "long-lead-time",
        "label": "the same 10% a month, but hardware takes nine months to arrive",
        "cur": 5000, "rate": 10, "limit": 50000, "cap": 1000, "rho": 70, "lead": 9,
        "what": "a service on nine-month hardware lead times",
    },
    {
        "key": "modest-growth",
        "label": "3% a month — slow, and still doubling inside two years",
        "cur": 5000, "rate": 3, "limit": 50000, "cap": 1000, "rho": 70, "lead": 3,
        "what": "a service growing three per cent a month",
    },
]

GROWTH_SCRIPT = r"""
  var sel = document.getElementById('grPreset');
  var plot = document.getElementById('grPlot');
  var status = document.getElementById('grStatus');
  var table = document.getElementById('grTable');
  var HORIZON = 48, MAXSCAN = 2000;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('growth: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('grCur').value = p.cur;
    document.getElementById('grRate').value = p.rate;
    document.getElementById('grLimit').value = p.limit;
    document.getElementById('grRho').value = p.rho;
    document.getElementById('grLead').value = p.lead;
  }
  function state() {
    var p = preset();
    return {
      p: p,
      current: R(BigInt(+document.getElementById('grCur').value), 1n),
      rate: R(BigInt(+document.getElementById('grRate').value), 100n),
      limit: R(BigInt(+document.getElementById('grLimit').value), 1n),
      cap: R(BigInt(p.cap), 1n),
      rho: R(BigInt(+document.getElementById('grRho').value), 100n),
      lead: +document.getElementById('grLead').value
    };
  }

  function draw(st, hit) {
    var top = ratioApprox(st.limit, R(1n, 1n)) * 1.25;
    if (!(top > 0)) top = 1;
    var x = function (m) { return 52 + m / HORIZON * 590; };
    var y = function (v) { return 150 - Math.min(v, top) / top * 124; };
    var s = '', m, path = '';
    var yl = y(ratioApprox(st.limit, R(1n, 1n)));
    s += '<rect x="52" y="26" width="590" height="' + Math.max(0, yl - 26).toFixed(1)
      + '" fill="var(--red)" opacity="0.08" />'
      + '<line x1="52" y1="' + yl.toFixed(1) + '" x2="642" y2="' + yl.toFixed(1)
      + '" stroke="var(--red)" stroke-width="1.7" />'
      + '<text x="642" y="' + (yl - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--red)">'
      + 'the limit: ' + Rnice(st.limit, 0) + ' rps</text>';
    for (m = 0; m <= HORIZON; m += 1) {
      path += (m === 0 ? 'M' : 'L') + x(m).toFixed(1) + ' '
        + y(ratioApprox(loadAtMonth(st.current, st.rate, m), R(1n, 1n))).toFixed(1) + ' ';
    }
    s += '<path d="' + path + '" fill="none" stroke="var(--cyan)" stroke-width="2.3" />';
    if (hit !== null && hit <= HORIZON) {
      s += '<line x1="' + x(hit).toFixed(1) + '" y1="26" x2="' + x(hit).toFixed(1)
        + '" y2="150" stroke="var(--amber)" stroke-width="1.6" stroke-dasharray="5 3" />'
        + '<text x="' + (x(hit) + 4).toFixed(1) + '" y="40" font-size="10" fill="var(--amber)">'
        + 'month ' + hit + '</text>';
      var order = orderMonth(hit, st.lead);
      if (order !== null && order >= 0 && order <= HORIZON) {
        s += '<line x1="' + x(order).toFixed(1) + '" y1="26" x2="' + x(order).toFixed(1)
          + '" y2="150" stroke="var(--green)" stroke-width="1.5" stroke-dasharray="3 3" />'
          + '<text x="' + (x(order) + 4).toFixed(1) + '" y="56" font-size="10" fill="var(--green)">'
          + 'order by month ' + order + '</text>';
      } else if (order !== null) {
        s += '<text x="56" y="56" font-size="10" fill="var(--red)">'
          + 'the order should already have gone in (month ' + order + ')</text>';
      }
    }
    /* the machine count, as the staircase it actually is */
    for (m = 0; m <= HORIZON; m += 2) {
      var n = machinesAtMonth(st.current, st.rate, m, st.cap, st.rho);
      if (n === null) continue;
      var h = Math.min(28, n);
      s += '<rect x="' + (x(m) - 4).toFixed(1) + '" y="' + (186 - h).toFixed(1)
        + '" width="8" height="' + Math.max(1, h) + '" rx="1" fill="var(--purple)" opacity="0.65" />';
    }
    s += '<line x1="52" y1="150" x2="642" y2="150" stroke="var(--line-strong)" />'
      + '<line x1="52" y1="186" x2="642" y2="186" stroke="var(--line-strong)" />'
      + '<text x="6" y="34" font-size="10" fill="var(--muted)">rps</text>'
      + '<text x="6" y="184" font-size="10" fill="var(--purple)">machines</text>'
      + '<text x="52" y="200" font-size="10" fill="var(--muted)">now</text>'
      + '<text x="642" y="200" text-anchor="end" font-size="10" fill="var(--muted)">'
      + HORIZON + ' months</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var st = state();
    document.getElementById('grCurOut').textContent = Rnice(st.current, 0) + ' rps today';
    document.getElementById('grRateOut').textContent = Rpct(st.rate, 0) + ' a month, compounding';
    document.getElementById('grLimitOut').textContent = Rnice(st.limit, 0) + ' rps is the limit';
    document.getElementById('grRhoOut').textContent = 'sizing each machine to ρ = ' + Rpct(st.rho, 0);
    document.getElementById('grLeadOut').textContent = st.lead + ' months to get hardware';

    var hit = monthsToLimit(st.current, st.rate, st.limit, MAXSCAN);
    var approx = monthsToLimitApprox(st.current, st.rate, st.limit);
    var dbl = doublingMonths(st.rate, MAXSCAN);
    draw(st, hit);

    var order = orderMonth(hit, st.lead);
    document.getElementById('grMonth').textContent = hit === null
      ? 'never, at this rate' : 'month ' + hit;
    document.getElementById('grApprox').textContent = isFinite(approx)
      ? approx.toFixed(3) + ' (rounded)' : '∞';
    document.getElementById('grDouble').textContent = dbl === null ? 'never' : 'every ' + dbl + ' months';
    document.getElementById('grNow').textContent = machinesAtMonth(st.current, st.rate, 0, st.cap, st.rho)
      + ' machines';
    document.getElementById('grThen').textContent = hit === null ? '—'
      : machinesAtMonth(st.current, st.rate, hit, st.cap, st.rho) + ' machines';
    document.getElementById('grOrder').textContent = order === null ? '—'
      : (order < 0 ? 'already late by ' + (-order) + ' months' : 'month ' + order);

    var rows = '<thead><tr><th>month</th><th>load, exactly</th><th>load</th>'
      + '<th>&times; today</th><th>machines at ρ = ' + Rpct(st.rho, 0)
      + '</th><th>past the limit?</th></tr></thead><tbody>';
    var picks = [0, 6, 12];
    if (hit !== null) { picks.push(hit - 1); picks.push(hit); }
    if (order !== null && order >= 0) picks.push(order);
    picks.push(24); picks.push(HORIZON);
    picks = picks.filter(function (v, i, a) { return v >= 0 && a.indexOf(v) === i; })
                 .sort(function (a, b) { return a - b; });
    for (var i = 0; i < picks.length; i += 1) {
      var m = picks[i], load = loadAtMonth(st.current, st.rate, m);
      var over = Rcmp(load, st.limit) >= 0;
      rows += '<tr><td>' + m + (m === hit ? ' <span class="tone-amber">(the limit)</span>' : '')
        + (m === order ? ' <span class="tone-green">(order now)</span>' : '')
        + '</td><td>' + Rshort(load, 2, 12) + '</td><td>' + Rnice(load, 0) + ' rps</td><td>'
        + Rnice(Rdiv(load, st.current), 2) + '×</td><td>'
        + machinesAtMonth(st.current, st.rate, m, st.cap, st.rho) + '</td><td class="'
        + (over ? 'tone-red' : 'tone-green') + '">' + (over ? 'yes' : 'no') + '</td></tr>';
    }
    table.innerHTML = rows + '</tbody>';

    status.innerHTML = st.p.what + ' is at ' + Rnice(st.current, 0) + ' rps today and compounds at '
      + Rpct(st.rate, 0) + ' a month, so month m carries current&thinsp;&times;&thinsp;(1+r)&#7504; '
      + '— an exact fraction at every m, however large the power. '
      + (hit === null
          ? 'At this rate it never reaches ' + Rnice(st.limit, 0) + ' rps.'
          : 'It reaches the ' + Rnice(st.limit, 0) + ' rps limit in <strong>month ' + hit
            + '</strong>, found by testing each month’s exact value against the limit. '
            + 'log(limit/current)/log(1+r) = <strong>' + (isFinite(approx) ? approx.toFixed(3) : '∞')
            + '</strong> is the same answer rounded, and it is printed as the gloss rather than as '
            + 'the assertion: the integer search is what the page claims, and a logarithm cannot be '
            + 'checked by hand the way a comparison can.')
      + ' The load doubles ' + (dbl === null ? 'never' : 'every <strong>' + dbl + ' months</strong>')
      + ', which is the part people underestimate — ' + Rpct(st.rate, 0)
      + ' a month sounds small and is ' + Rnice(Rdiv(loadAtMonth(st.current, st.rate, 12), st.current), 2)
      + '× in a year. The fleet goes from '
      + machinesAtMonth(st.current, st.rate, 0, st.cap, st.rho) + ' machines to '
      + (hit === null ? '—' : machinesAtMonth(st.current, st.rate, hit, st.cap, st.rho))
      + ' by then, each a ceiling of load over capacity×ρ, because 3.2 machines is four. '
      + (order === null ? ''
          : (order < 0
              ? '<span class="tone-red">With a ' + st.lead + '-month lead time the order should '
                + 'already have gone in ' + (-order) + ' months ago.</span>'
              : 'With a ' + st.lead + '-month lead time the order has to go in by <strong>month '
                + order + '</strong>, which is the date the plan is actually about.'));
  }

  ['grCur', 'grRate', 'grLimit', 'grRho', 'grLead'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _growth(cfg):
    """Growth: the month a compounding load reaches a limit, by exact integer search."""
    idx = _preset_index(cfg, GROWTH_PRESETS, "growth")
    p = GROWTH_PRESETS[idx]
    markup = (
        _toolbar(
            "A capacity plan under growth",
            "compounding reaches a limit on a date, and hardware has a lead time",
            _swatch("tone-cyan", "load")
            + _swatch("tone-red", "the limit")
            + _swatch("tone-amber", "the month it is reached")
            + _swatch("tone-green", "the month to order in")
            + _swatch("tone-purple", "machines"),
        )
        + _stage(
            "grStage", "grPlot", 660, 208,
            "A compounding load curve against a capacity limit, with the machine count beneath it.",
            "An exponential load curve crossing a limit line, with order and limit months marked and a staircase of machine counts below.",
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="grTable"></table></div>\n'
        '      <div class="status-banner" id="grStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("grPreset", "Worked example", [(q["key"], q["label"]) for q in GROWTH_PRESETS], p["key"])
        + _range("grCur", "load today, rps", 100, 50000, p["cur"], 100)
        + _range("grRate", "growth a month, %", 0, 40, p["rate"])
        + _range("grLimit", "the limit you run into, rps", 1000, 500000, p["limit"], 1000)
        + _range("grRho", "target utilisation &rho;, %", 40, 95, p["rho"])
        + _range("grLead", "lead time for capacity, months", 0, 18, p["lead"])
        + _kpi([
            ("grMonth", "Limit reached in"),
            ("grApprox", "log(limit/current)/log(1+r)"),
            ("grDouble", "Doubling time"),
            ("grNow", "Machines today"),
            ("grThen", "Machines at the limit"),
            ("grOrder", "Order capacity by"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", GROWTH_PRESETS) + GROWTH_SCRIPT
    return Lab(
        title="A capacity plan under growth",
        subtitle="The month the plan runs out, found by counting rather than by a logarithm",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the growth rate, the limit and the lead time"),
        panel_intro=cfg.get(
            "panel_intro",
            "current·(1+r)ᵐ is an exact fraction at every month, so the month the limit is "
            "reached is an integer search with nothing rounded in it. "
            "log(limit/current)/log(1+r) is printed beside it as the rounded gloss, never in its place.",
        ),
        script=script,
    )


# ------------------------------------------------------------------ dispatch

_BUILDERS = {
    "amdahl": _amdahl,
    "usl": _usl,
    "batch": _batch,
    "vertical": _vertical,
    "waste": _waste,
    "reserve": _reserve,
    "autoscale": _autoscale,
    "unit": _unit,
    "tier": _tier,
    "compress": _compress,
    "placement": _placement,
    "headroom": _headroom,
    "growth": _growth,
}

MODES = tuple(_BUILDERS)


def scale_lab(cfg):
    """The scaling-and-cost kit: thirteen modes, eleven lessons.

    An unknown mode RAISES. The alternative -- a silent default -- is how a
    lesson on the Universal Scalability Law's peak ends up showing the reader
    Amdahl's plateau: the page builds, renders, redraws and passes every markup
    assertion in the suite while teaching the opposite of its own hard idea.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "scale: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["SCALE_JS", "MODES", "scale_lab"]
