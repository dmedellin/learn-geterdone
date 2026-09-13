"""Course 3: Queues and Utilisation -- one kit, thirteen modes, one arithmetic.

Everything on this course is a consequence of one sentence: work that arrives
irregularly has to wait for work that is already there. The modes below are the
thirteen places that sentence turns into a number.

Four decisions run through all of them.

  A SLOTTED SIMULATION IS NOT M/M/1. This is the correctness point the kit
  exists to get right. With Bernoulli arrivals p per slot and geometric service
  q per slot, the chain is Geo/Geo/1, and its exact mean number in system is

      L = rho(1 - p)/(1 - rho)          rho = p/q

  not rho/(1 - rho). At p = 2/5, q = 1/2 that is 12/5 against 4: the continuous
  formula overstates the slotted answer by 5/3. They agree only as the slot
  shrinks, because p = lambda*Delta goes to zero with it, and the gap

      rho/(1 - rho) - L = rho*p/(1 - rho)

  is linear in Delta. So `mm1` does not claim its formula is checked against a
  simulation -- it shows the convergence, with `geoGeo1` giving the exact
  finite-slot answer at each step -- and `slotted` names its model on the page.
  The derivation of the discrete chain is Operations Research's
  `markov-chains-decisions-and-queues/queues-in-discrete-time`; this kit calls
  the core's `geoGeo1` and says where the derivation lives.

  THE SIMULATION STARTS EMPTY. A mean taken from t = 0 is biased low, because
  the run spends its first slots in states the stationary chain visits rarely.
  `slotted` and `variability` therefore report the mean twice -- from t = 0 and
  after a discarded warm-up -- and print the gap between them. Neither is the
  exact answer; the exact answer is the closed form beside them.

  LITTLE'S LAW IS OWNED HERE, AND IT IS AN IDENTITY. `trace` proves L = lambda*W
  by counting, with no distribution anywhere in it, and it lets the reader cut
  the measurement window short so the identity visibly fails while work is still
  in flight. `finite` carries the other half of the misconception: in a lossy
  system the rate that crosses the boundary is lambda(1 - pK), not lambda, so
  both W values are printed side by side and labelled.

  EXACT UNLESS THE LESSON IS ABOUT AN APPROXIMATION. Three modes round and say
  so on their face: `memoryless` (e^-x by series), `poisson` (the same), and
  `variability`, whose arithmetic is exact and whose MODEL is the approximation
  -- which is why the page prints the exact Geo/Geo/1 answer beside Kingman's
  and lets them disagree.

  AND THE ROUNDED ONE HAS A RANGE. sysdesign_core's `expNegApprox` sums the
  ALTERNATING series for e^-x, whose largest term is about e^x/sqrt(2*pi*x)
  while the answer is e^-x, so it loses roughly 2x/ln(10) significant digits to
  cancellation. Measured: the relative error is 3e-9 at x = 10, 1.6e-7 at
  x = 12, 4e-3 at x = 17, 173% at x = 20, and past x = 21 the SIGN is wrong.
  That is a defect in the core -- 1/exp(x) by a positive-term series would be
  right everywhere -- and fixing it there is not this kit's to do while nine
  other kits are being built against the same file. So `memoryless` and
  `poisson` bound their controls to x <= 12, `expNegSafe` returns NaN outside
  that, and both pages say on their face where the limit is and why. The exact
  columns on both pages have no such limit, which is the argument for exactness
  stated in one number.

The modes, and the lesson each belongs to:

  rates        L1  rho = lambda/mu, and the backlog growth rate when rho >= 1
  trace        L2  the area under N(t) against the sum of sojourn times
  little       L3  any one of L, lambda, W from the other two, with units
  slotted      L4  bunching against determinism at equal rho, on a seeded run
  memoryless   L5  (1 - lambda*Delta)^(t/Delta) exact, e^(-lambda*t) rounded
  poisson      L6  the binomial exactly, its Poisson limit rounded, and the tail
  mm1          L7  pi_n, L, Lq, W, Wq, P(N > k), and the shrinking-slot panel
  knee         L8  W/S = 1/(1 - rho) as a hyperbola, and the rho for W = k*S
  variability  L9  Kingman against the exact chain and against the simulation
  mms          L10 a pooled M/M/s against s separate M/M/1s at the same load
  finite       L11 pi_K, the admitted rate, and BOTH W values
  bucket       L12 a token bucket on a trace, against a fixed window
  backlog      L13 the area a spike leaves behind, and how long it takes to go

Mode `knee` is section 4.3's "mode mm1, knee view" promoted to a mode key of its
own. A view selected by a config key that the dispatch does not validate is the
hazard the unknown-mode rule exists for: an unknown view would render L7's
widget under L8's title and nothing downstream would notice. Two mode keys, two
validated names, two different drawings.
"""

import json

from .algebra_core import RATIONAL_JS
from .common import Lab
from .counting import BIGINT_JS
from .sysdesign_core import (
    APPROX_JS,
    QUEUE_JS,
    RCEIL_JS,
    SLOTTED_JS,
    STREAM_JS,
    TRACE_JS,
)

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document.
# ---------------------------------------------------------------------------

QUEUE_KIT_JS = r"""
  /* ---------------------------------------------------------------- output

     Rdec goes through Number, and this course produces rationals Number cannot
     hold: (19/20)^400 has a 521-digit numerator and Number() of it is 0, while
     M/M/1/K at K = 20 has a denominator of 21 digits. So decimals here are long
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
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }
  /* The exact fraction when a reader can read it, and a decimal when the exact
     form has run to twenty digits. Both are the same number; only one of them
     is evidence. The cut is on digits, not on magnitude, so it is the same
     rule on every page of the course. */
  function Rshort(a, places, digits) {
    if (digits === undefined) digits = 9;
    var wide = String(a.n < 0n ? -a.n : a.n).length > digits || String(a.d).length > digits;
    return wide ? Rfixed(a, places === undefined ? 4 : places) : Rtext(a);
  }
  function commas(value) {
    var s = String(value), out = '', i, c = 0;
    for (i = s.length - 1; i >= 0; i -= 1) {
      out = s.charAt(i) + out;
      c += 1;
      if (c % 3 === 0 && i > 0 && s.charAt(i - 1) !== '-') out = ' ' + out;
    }
    return out;
  }

  /* ------------------------------------------------- L1: rates, not latencies

     mu is a RATE. A service time of S milliseconds is mu = 1000/S per second,
     and the whole misconception of lesson 1 is reading mu off as if it were S.
     Both directions are here so the page can print the conversion rather than
     assert it. */
  function muFromServiceMs(serviceMs) { return R(1000n, BigInt(serviceMs)); }
  function serviceMsFromMu(mu) { return Rdiv(R(1000n, 1n), mu); }
  /* Above rho = 1 the backlog grows at lambda - mu per second, for ever. This
     is a straight line, not a queue: no steady state exists to ask L about. */
  function growthPerSec(lam, mu) { return Rsub(lam, mu); }
  function backlogAfter(lam, mu, secs) {
    var g = growthPerSec(lam, mu);
    if (Rcmp(g, R(0n, 1n)) <= 0) return R(0n, 1n);
    return Rmul(g, R(BigInt(secs), 1n));
  }

  /* ------------------------------------- L2: Little's Law inside a window

     littleFromTrace in the core takes the horizon to be the last departure, so
     every customer has finished and the identity holds exactly. This is the
     same counting over a window the reader can cut SHORT, which is where the
     identity stops holding -- not because the law is false but because the
     three quantities are then being measured over different populations.

     area  : sum over t in [0, T) of N(t), the same area littleFromTrace uses
     done  : the customers who both arrived and departed inside the window
     The honest W is the mean sojourn of `done`; the seductive one divides the
     area by every arrival, including those still in flight. */
  function littleWindow(arrivals, departures, T) {
    var i, area = 0, arrived = 0, done = 0, doneTime = 0, inflight = 0;
    for (var t = 0; t < T; t += 1) {
      for (i = 0; i < arrivals.length; i += 1) {
        if (arrivals[i] <= t && departures[i] > t) area += 1;
      }
    }
    for (i = 0; i < arrivals.length; i += 1) {
      if (arrivals[i] >= T) continue;
      arrived += 1;
      if (departures[i] <= T) { done += 1; doneTime += departures[i] - arrivals[i]; }
      else inflight += 1;
    }
    var Tr = R(BigInt(T), 1n);
    var L = Rdiv(R(BigInt(area), 1n), Tr);
    var lam = Rdiv(R(BigInt(arrived), 1n), Tr);
    var W = done ? Rdiv(R(BigInt(doneTime), 1n), R(BigInt(done), 1n)) : R(0n, 1n);
    return {
      area: area, arrived: arrived, done: done, inflight: inflight,
      L: L, lambda: lam, W: W, lamW: Rmul(lam, W),
      holds: Requ(L, Rmul(lam, W))
    };
  }

  /* -------------------------------------------------- L3: sizing with L = lam*W

     One identity, three ways round. Units are carried as strings because the
     error this lesson is about is a unit error: a pool of N connections at W
     milliseconds each supports N/W per MILLISECOND, which is 1000N/W a second,
     and a reader who forgets the thousand sizes the pool 1000x wrong. */
  function littleSolve(which, a, b) {
    if (which === 'L') return Rmul(a, b);            /* lambda * W          */
    if (which === 'lambda') return Rdiv(a, b);       /* L / W               */
    if (which === 'W') return Rdiv(a, b);            /* L / lambda          */
    throw new Error('littleSolve: no unknown named ' + which);
  }
  /* The throughput a pool of N caps at, when each holder keeps it for W ms. */
  function poolCapPerSec(N, waitMs) {
    return Rdiv(Rmul(R(BigInt(N), 1n), R(1000n, 1n)), waitMs);
  }
  /* And the pool a target rate needs: lambda per second * W ms / 1000. */
  function poolForRate(ratePerSec, waitMs) {
    return Rdiv(Rmul(ratePerSec, waitMs), R(1000n, 1n));
  }

  /* --------------------------------------- L4, L7, L9: the slotted chain

     One Bernoulli arrival per slot with probability p; geometric service with
     parameter q; LATE ARRIVAL, meaning a departure is resolved before an
     arrival within the same slot, so a job that arrives in slot t cannot leave
     before slot t + 1. That convention is what makes the stationary chain the
     one geoGeo1 solves, and changing it changes the number -- which is why it
     is stated on the page and not only here.

     Exactly two draws are consumed per slot whether or not the departure draw
     is used. Consuming one when the queue is empty would make the arrival
     sequence depend on q, and then the deterministic-service arm below would
     not be seeing the same arrivals. */
  var LCG_A = 1103515245, LCG_C = 12345, LCG_M = 2147483648;

  /* u is a raw stream value in [0, m); the comparison is exact in BigInt
     because a Number comparison here would be right until it silently was not. */
  function drawBelow(u, m, prob) {
    return BigInt(u) * prob.d < prob.n * BigInt(m);
  }
  function slottedRun(p, q, seed, slots) {
    var u = lcgStream(LCG_A, LCG_C, LCG_M, seed, 2 * slots), n = 0, out = [];
    for (var t = 0; t < slots; t += 1) {
      if (n > 0 && drawBelow(u[2 * t], LCG_M, q)) n -= 1;   /* departure first */
      if (drawBelow(u[2 * t + 1], LCG_M, p)) n += 1;        /* then the arrival */
      out.push(n);
    }
    return out;
  }
  /* The same arrivals, served in exactly D slots every time: c_s^2 = 0. */
  function slottedDetRun(p, D, seed, slots) {
    var u = lcgStream(LCG_A, LCG_C, LCG_M, seed, 2 * slots), n = 0, rem = 0, out = [];
    for (var t = 0; t < slots; t += 1) {
      if (n > 0) { if (rem === 0) rem = D; rem -= 1; if (rem === 0) n -= 1; }
      if (drawBelow(u[2 * t + 1], LCG_M, p)) n += 1;
      out.push(n);
    }
    return out;
  }
  /* D/D/1: an arrival every A slots, service exactly S slots, S < A. Nothing
     random in it, and nothing ever waits -- which is lesson 4's whole point. */
  function ddRun(A, S, slots) {
    var n = 0, rem = 0, out = [];
    for (var t = 0; t < slots; t += 1) {
      if (n > 0) { if (rem === 0) rem = S; rem -= 1; if (rem === 0) n -= 1; }
      if (t % A === 0) n += 1;
      out.push(n);
    }
    return out;
  }
  /* The mean of a run from slot `from` onward, exact. `from` is the discarded
     warm-up, and the difference between from = 0 and from > 0 is the initial
     transient the lesson names. */
  function runMean(trace, from) {
    var s = 0n, i, n = 0;
    for (i = from; i < trace.length; i += 1) { s += BigInt(trace[i]); n += 1; }
    if (!n) return R(0n, 1n);
    return R(s, BigInt(n));
  }
  /* The running mean at `points` evenly spaced cut-offs, exact, in one pass.

     Calling runMean at each cut-off would be O(points * slots); a cumulative
     sum makes it O(slots), which is what lets the curve be drawn from the same
     exact arithmetic as the headline number rather than from a float shadow of
     it. Each entry is [slot, mean]. */
  function runningMeans(trace, from, points) {
    var out = [], cum = 0n, kept = 0, i, every = Math.max(1, Math.floor((trace.length - from) / points));
    for (i = from; i < trace.length; i += 1) {
      cum += BigInt(trace[i]);
      kept += 1;
      if (kept % every === 0 || i === trace.length - 1) out.push([i + 1, R(cum, BigInt(kept))]);
    }
    return out;
  }

  /* Those waiting rather than in service. L - Lq = rho is the misconception of
     lesson 7, and this is the same subtraction done slot by slot. */
  function queueOf(trace) {
    return trace.map(function (n) { return n > 0 ? n - 1 : 0; });
  }
  function runMax(trace) {
    var m = 0;
    for (var i = 0; i < trace.length; i += 1) if (trace[i] > m) m = trace[i];
    return m;
  }
  /* The exact number waiting in the discrete chain: L - rho, because exactly
     rho of the time there is one in service. */
  function geoGeo1Lq(p, q) {
    var g = geoGeo1(p, q);
    if (!g.stable) return null;
    return Rsub(g.L, g.rho);
  }
  /* The chain's own coefficients of variation, which are NOT free parameters:
     a Bernoulli arrival stream has geometric gaps, so c_a^2 = 1 - p, and a
     geometric service has c_s^2 = 1 - q. Kingman evaluated at these is a fair
     comparison; Kingman evaluated at 1 and 1 is the M/M/1 answer wearing a
     slotted simulation's clothes. */
  function slottedCa2(p) { return Rsub(R(1n, 1n), p); }
  function slottedCs2(q) { return Rsub(R(1n, 1n), q); }

  /* The initial transient, made visible rather than argued about.

     E[N_t] starts at 0 because the run starts empty and climbs toward L, so a
     mean taken from t = 0 is biased LOW in expectation. On one run that bias is
     smaller than the sampling noise and the sign can come out either way, which
     is exactly why a warm-up is discarded rather than debated: this averages
     the occupancy at each slot over `seeds` independent runs, and the curve it
     returns rises from zero with nothing to argue about. */
  function transientCurve(p, q, seed0, seeds, slots) {
    var acc = [], s, t;
    for (t = 0; t < slots; t += 1) acc.push(0);
    for (s = 0; s < seeds; s += 1) {
      var run = slottedRun(p, q, seed0 + s, slots);
      for (t = 0; t < slots; t += 1) acc[t] += run[t];
    }
    return acc.map(function (v) { return R(BigInt(v), BigInt(seeds)); });
  }

  /* The mean of part of an ensemble curve, exact. Early against late is the
     bias the empty start causes, stated as two numbers rather than as a claim. */
  function curveMean(curve, from, to) {
    var s = R(0n, 1n), i, n = 0;
    for (i = from; i < to && i < curve.length; i += 1) { s = Radd(s, curve[i]); n += 1; }
    return n ? Rdiv(s, R(BigInt(n), 1n)) : R(0n, 1n);
  }

  /* --------------------------------- L7: the shrinking slot, done exactly

     p = lambda*Delta and q = mu*Delta, so both must be probabilities: the
     largest legal slot is 1/max(lambda, mu), and the panel starts there. The
     exact mean at each step is geoGeo1's, and its distance from rho/(1 - rho)
     is rho*p/(1 - rho) -- linear in Delta, which is why ten times smaller is
     ten times closer and not merely closer. */
  function largestLegalSlot(lam, mu) {
    var bigger = Rcmp(lam, mu) >= 0 ? lam : mu;
    if (Rzero(bigger)) return null;
    return Rinv(bigger);
  }
  function slottedMean(lam, mu, delta) {
    var p = Rmul(lam, delta), q = Rmul(mu, delta), one = R(1n, 1n);
    if (Rcmp(p, one) > 0 || Rcmp(q, one) > 0) return null;
    var g = geoGeo1(p, q);
    return g.stable ? g.L : null;
  }
  /* The whole panel: `steps` slot sizes, each a tenth of the one before. */
  function convergenceRows(lam, mu, steps) {
    var base = largestLegalSlot(lam, mu), rows = [], i;
    if (!base) return rows;
    var cont = mm1(lam, mu);
    for (i = 0; i < steps; i += 1) {
      var delta = Rdiv(base, Rpow(R(10n, 1n), i));
      var L = slottedMean(lam, mu, delta);
      rows.push({
        delta: delta, p: Rmul(lam, delta), q: Rmul(mu, delta), L: L,
        gap: L && cont.stable ? Rsub(cont.L, L) : null
      });
    }
    return rows;
  }

  /* ------------------------------------------------------- L8: the knee

     W/S = 1/(1 - rho), a hyperbola with an asymptote at rho = 1. The inverse is
     the more useful direction: the utilisation at which the response time has
     reached k service times is exactly (k - 1)/k, so k = 10 is 90% and k = 100
     is 99%, and the last tenth of a machine costs what the first nine did. */
  function kneeFactor(rho) { return Rinv(Rsub(R(1n, 1n), rho)); }
  function rhoForFactor(k) { return R(BigInt(k - 1), BigInt(k)); }

  /* ------------------------------------------------ L9: Kingman's formula

     Wq ~ (rho/(1 - rho)) * ((ca^2 + cs^2)/2) * S. The arithmetic is exact for
     rational ca^2, cs^2 and S. The MODEL is the approximation, and the page
     proves that rather than asserting it: at ca^2 = cs^2 = 1 this returns the
     M/M/1 Wq exactly, and at the slotted chain's own coefficients it misses the
     chain's exact answer -- in the same direction every time, because it is a
     heavy-traffic limit being read at moderate load. */
  function kingmanWq(rho, ca2, cs2, S) {
    var one = R(1n, 1n);
    if (Rcmp(rho, one) >= 0) return null;
    return Rmul(Rdiv(rho, Rsub(one, rho)), Rmul(Rdiv(Radd(ca2, cs2), R(2n, 1n)), S));
  }

  /* ------------------------------- L5: geometric to exponential, both ways

     P(T > t) = (1 - lambda*Delta)^(t/Delta) exactly, against e^(-lambda*t)
     rounded. t is a whole number of seconds and Delta is 1/k of one, so the
     exponent is the integer t*k and no rounding enters the exact side at all. */
  function geoTail(lam, invDelta, t) {
    var delta = R(1n, BigInt(invDelta));
    var per = Rsub(R(1n, 1n), Rmul(lam, delta));
    if (Rcmp(per, R(0n, 1n)) < 0) return null;
    return Rpow(per, t * invDelta);
  }
  /* Memorylessness, exactly: P(T > s + t | T > s) = P(T > t), for EVERY s.
     Not approximately, not in the limit -- it is the defining property, and the
     geometric has it at any slot size, which is why the limit keeps it. */
  function geoCondTail(lam, invDelta, s, t) {
    var both = geoTail(lam, invDelta, s + t), past = geoTail(lam, invDelta, s);
    if (!both || !past || Rzero(past)) return null;
    return Rdiv(both, past);
  }
  /* e^-x, from the core, WITH ITS RANGE STATED.

     expNegApprox sums the alternating series 1 - x + x^2/2! - ..., whose largest
     term is about e^x/sqrt(2*pi*x) while the answer is e^-x, so it throws away
     roughly 2x/ln(10) significant digits to cancellation. In double precision
     that is all sixteen of them by about x = 19, and past x = 21 the result
     changes sign. Measured: the relative error is 3e-9 at x = 10, 1.6e-7 at
     x = 12, 4e-3 at x = 17 and 173% at x = 20.

     So this kit does not hand it an x it cannot answer. The two modes that call
     it bound their controls to EXP_SAFE_X and say so on the page, and the two
     functions below refuse rather than return a number that is confidently
     wrong -- which on a page promising checkable arithmetic is the worse
     failure of the two. Widening the bound is a change to the core's method,
     not to this kit. */
  var EXP_SAFE_X = 12;
  function expNegSafe(x) {
    if (!(x >= 0) || x > EXP_SAFE_X) return NaN;
    var v = expNegApprox(x, 1e-15);
    return (v > 0 && v <= 1) ? v : NaN;
  }
  function expTailApprox(lam, t) { return expNegSafe(Rnum(lam) * t); }

  /* ------------------------------- L6: the binomial exactly, Poisson rounded

     The count in a window of n opportunities each firing with probability m/n
     is binomial, and that is EXACT. Its limit as n grows is e^-m m^k/k!, which
     is not, because e^-m is not rational. Both are printed, the difference is
     printed, and the difference is what "Poisson" means. */
  function binomRow(n, m, upto) {
    /* P(k+1) = P(k) * ((n-k)/(k+1)) * (p/(1-p)), from P(0) = (1-p)^n.

       By recurrence rather than comb(n,k)p^k(1-p)^(n-k) per term, for a reason
       that is not tidiness: at n = 1000 and p = 1/100 each term has a
       two-thousand-digit denominator, and summing the upper tail one closed
       form at a time takes long enough that the page never paints. The
       recurrence is one multiplication per step and the answers are identical. */
    var p = R(BigInt(m), BigInt(n)), one = R(1n, 1n), notp = Rsub(one, p);
    if (Rzero(notp)) return [one];
    var ratio = Rdiv(p, notp), out = [], cur = Rpow(notp, n), k;
    out.push(cur);
    for (k = 0; k < upto && k < n; k += 1) {
      cur = Rmul(cur, Rmul(R(BigInt(n - k), BigInt(k + 1)), ratio));
      out.push(cur);
    }
    return out;
  }
  function binomPmf(n, m, k) {
    if (k < 0 || k > n) return R(0n, 1n);
    var row = binomRow(n, m, k);
    return row[k];
  }
  /* P(count > C) as 1 minus the head, which is C + 1 terms rather than n - C.
     Exact either way; only one of them finishes. */
  function tailFromRow(row, C) {
    var s = R(0n, 1n), k;
    for (k = 0; k <= C && k < row.length; k += 1) s = Radd(s, row[k]);
    return Rsub(R(1n, 1n), s);
  }
  function binomTail(n, m, C) {
    if (C >= n) return R(0n, 1n);
    return tailFromRow(binomRow(n, m, Math.max(0, C)), C);
  }
  /* Variance equals the mean is the Poisson signature, and the binomial says
     what it costs to get there: n*p(1-p) = m(1 - m/n), exactly. At n = 100 and
     m = 10 the variance is 9, not 10, and that 10% is the whole gap between a
     window of a hundred opportunities and a window of infinitely many. */
  function binomVar(n, m) {
    return Rmul(R(BigInt(m), 1n), Rsub(R(1n, 1n), R(BigInt(m), BigInt(n))));
  }

  function poissonPmfApprox(m, k) {
    var t = expNegSafe(m);
    for (var i = 1; i <= k; i += 1) t = t * m / i;
    return t;
  }
  /* The head is accumulated term by term, so the tail is one pass rather than
     one pass per C. The same rewrite the binomial needed, for the same reason. */
  function poissonTailApprox(m, C) {
    var t = expNegSafe(m), head = t, k;
    for (k = 1; k <= C; k += 1) { t = t * m / k; head += t; }
    return 1 - head;
  }
  /* The smallest headroom C that keeps P(count > C) at or under a target. The
     tail falls with C, so the first C that clears it is the answer. */
  function headroomForApprox(m, target, limit) {
    var t = expNegSafe(m), head = t, C;
    if (!(t > 0)) return -1;
    for (C = 0; C <= limit; C += 1) {
      if (1 - head <= target) return C;
      t = t * m / (C + 1);
      head += t;
    }
    return -1;
  }

  /* ----------------------------------- L11: the K a loss target needs

     mm1k gives the blocking at one K; this is the smallest K that gets it under
     a target. Monotone in K for rho < 1, and at rho >= 1 it may never get
     there, which the -1 says. */
  function smallestBuffer(lam, mu, target, limit) {
    for (var K = 1; K <= limit; K += 1) {
      if (Rcmp(mm1k(lam, mu, K).blocking, target) <= 0) return K;
    }
    return -1;
  }
  /* The latency cap a buffer of K buys: at most K jobs ahead of you, each
     taking S = 1/mu on average, so the wait cannot exceed about K*S however
     hard the offered load pushes. */
  function bufferLatencyCap(mu, K) { return Rdiv(R(BigInt(K), 1n), mu); }

  /* -------------------------------------------- L12: the token bucket

     Capacity b, refilling at r tokens a second. An arrival at time t tops the
     bucket up by r*(t - last) seconds' worth, capped at b, and is admitted if a
     whole token is there. Times are integer milliseconds and r is a rational,
     so the token level is exact at every step and no drift accumulates.

     The bound is the lesson: at most b + r*t admissions in any window of t,
     which is why a bucket is not "r per second". */
  function bucketRun(times, r, b) {
    var cap = R(BigInt(b), 1n), tokens = cap, last = times.length ? times[0] : 0;
    var out = [], admitted = 0;
    for (var i = 0; i < times.length; i += 1) {
      var gap = R(BigInt(times[i] - last), 1000n);          /* ms -> seconds */
      tokens = Radd(tokens, Rmul(r, gap));
      if (Rcmp(tokens, cap) > 0) tokens = cap;
      last = times[i];
      var pass_ = Rcmp(tokens, R(1n, 1n)) >= 0;
      if (pass_) { tokens = Rsub(tokens, R(1n, 1n)); admitted += 1; }
      out.push({ t: times[i], admit: pass_, tokens: tokens });
    }
    return { rows: out, admitted: admitted, rejected: times.length - admitted };
  }
  /* The fixed window a bucket replaces: reset a counter every `windowMs`. It
     admits `limit` in each window, so two full windows back to back put 2*limit
     through in one window's width -- the boundary burst. */
  function fixedWindowRun(times, limit, windowMs) {
    var out = [], admitted = 0, bucketIndex = -1, count = 0;
    for (var i = 0; i < times.length; i += 1) {
      var w = Math.floor(times[i] / windowMs);
      if (w !== bucketIndex) { bucketIndex = w; count = 0; }
      var pass_ = count < limit;
      if (pass_) { count += 1; admitted += 1; }
      out.push({ t: times[i], admit: pass_, window: w });
    }
    return { rows: out, admitted: admitted, rejected: times.length - admitted };
  }
  /* The largest number of ADMITTED arrivals in any window of `windowMs`, taken
     over every window that starts at an admission. That is the number the
     downstream service actually sees, and it is what the two limiters are
     being compared on. */
  function largestBurst(rows, windowMs) {
    var ts = [], i, j, best = 0;
    for (i = 0; i < rows.length; i += 1) if (rows[i].admit) ts.push(rows[i].t);
    for (i = 0; i < ts.length; i += 1) {
      var c = 0;
      for (j = i; j < ts.length; j += 1) if (ts[j] - ts[i] < windowMs) c += 1;
      if (c > best) best = c;
    }
    return best;
  }
  function parseTimes(text, limit) {
    var raw = String(text).split(/[^0-9]+/), out = [], i;
    for (i = 0; i < raw.length; i += 1) {
      if (!raw[i]) continue;
      out.push(Number(raw[i]));
      if (out.length >= limit) break;
    }
    if (!out.length) return null;
    return out.sort(function (a, b) { return a - b; });
  }

  /* --------------------------------- L13: the backlog a spike leaves behind

     While lambda > mu the backlog grows at (lambda - mu) a second; the peak is
     that rate times the spike, which is the AREA between the two curves. It
     then drains at (mu - lambda_after), and the drain takes

         peak / (mu - lambda_after)

     seconds -- which is longer than the spike whenever the recovery headroom is
     smaller than the excess was. The lag a consumer sees is backlog/mu, so the
     worst lag arrives at the END of the spike and decays from there. */
  function backlogPlan(mu, before, spike, spikeSecs, after) {
    var zero = R(0n, 1n);
    var excess = Rsub(spike, mu);
    var peak = Rcmp(excess, zero) > 0 ? Rmul(excess, R(BigInt(spikeSecs), 1n)) : zero;
    var headroom = Rsub(mu, after);
    var drains = Rcmp(headroom, zero) > 0;
    var drainSecs = drains && !Rzero(peak) ? Rdiv(peak, headroom) : null;
    return {
      excess: excess, peak: peak, headroom: headroom, drains: drains,
      drainSecs: drainSecs,
      maxLagSecs: Rdiv(peak, mu),
      beforeStable: Rcmp(before, mu) < 0,
      totalSecs: drainSecs ? Radd(R(BigInt(spikeSecs), 1n), drainSecs) : null
    };
  }
  /* The backlog at a chosen second of the episode, for the curve: it rises on
     [0, spike] and falls after, and never goes below zero. */
  function backlogAt(plan, spikeSecs, secs) {
    var zero = R(0n, 1n);
    if (secs <= 0) return zero;
    if (secs <= spikeSecs) {
      var up = Rmul(plan.excess, R(BigInt(secs), 1n));
      return Rcmp(up, zero) > 0 ? up : zero;
    }
    if (!plan.drains) {
      return Radd(plan.peak, Rmul(Rsub(zero, plan.headroom), R(BigInt(secs - spikeSecs), 1n)));
    }
    var down = Rsub(plan.peak, Rmul(plan.headroom, R(BigInt(secs - spikeSecs), 1n)));
    return Rcmp(down, zero) > 0 ? down : zero;
  }
"""

_CORE_JS = (
    RATIONAL_JS + BIGINT_JS + RCEIL_JS + QUEUE_JS + SLOTTED_JS + TRACE_JS
    + STREAM_JS + APPROX_JS + QUEUE_KIT_JS
)


# ---------------------------------------------------------------------------
# Control furniture. The same three shapes every lab on the path uses, so a
# reader moving between courses moves between the same widgets. Every label
# carries an id, because three modes retitle a control when the reader changes
# what it stands for and getElementById is the only way in.
# ---------------------------------------------------------------------------


def _js_string(text):
    """A JS string literal for a preset the reader can then edit."""
    return json.dumps(text).replace("</", "<\\/")


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" id="%sLab" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, cid, label, cid, value, cid, lo, hi, step, value)
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


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own. An unknown preset raises for the same reason
    an unknown mode does: a silent fallback ships a page that looks finished and
    is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("queue mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "queue mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "queue mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


def _presets_js(presets):
    return "  var PRESETS = %s;\n" % json.dumps(presets).replace("</", "<\\/")


# ---------------------------------------------------------------------------
# L1 - rates
# ---------------------------------------------------------------------------

RATE_PRESETS = [
    {"key": "eighty-percent", "label": "800 rps into a 1 ms service — the lesson's example",
     "lam": 800, "svc": 1},
    {"key": "overloaded", "label": "1200 rps into the same service — rho above 1", "lam": 1200, "svc": 1},
    {"key": "slow-service", "label": "800 rps into a 2 ms service — the same load, half the rate",
     "lam": 800, "svc": 2},
]


def _rates(cfg):
    idx = _preset_index(cfg, RATE_PRESETS, "rates")
    pre = RATE_PRESETS[idx]

    markup = (
        _toolbar(
            "Arrival rate, service rate, utilisation",
            "&rho; = &lambda;/&mu;, and what happens to the backlog when it reaches 1",
            [("cyan", "arrivals &lambda;"), ("green", "service &mu;"), ("red", "the gap when &rho; &ge; 1")],
        )
        + _stage(_svg("raPlot", "0 0 520 160", "Arrival rate and service rate drawn as two bars, with the gap between them."))
        + _table("raTable")
        + _banner("raStatus")
    )
    controls = (
        _select("raPreset", "Worked example", [(p["key"], p["label"]) for p in RATE_PRESETS], pre["key"])
        + _range("raLam", "Arrival rate &lambda; (requests per second)", 50, 2000, pre["lam"], 10)
        + _range("raSvc", "Mean service time S (ms)", 1, 20, pre["svc"])
        + _kpis(
            [
                ("Service rate &mu; = 1000/S", "raMu"),
                ("Utilisation &rho; = &lambda;/&mu;", "raRho"),
                ("Backlog growth &lambda; &minus; &mu;", "raGrow"),
                ("Backlog after one minute", "raAfter"),
            ]
        )
        + _hint(
            "raHint",
            "&mu; is a <em>rate</em>, not a latency. A service that takes S = 2 ms has "
            "&mu; = 500 per second, and &rho; = &lambda;/&mu; is a ratio of two rates "
            "&mdash; a pure number with no seconds left in it.",
        )
    )

    script = _CORE_JS + _presets_js(RATE_PRESETS) + r"""
  var sel = document.getElementById('raPreset');
  var lamS = document.getElementById('raLam'), svcS = document.getElementById('raSvc');
  var plot = document.getElementById('raPlot'), table = document.getElementById('raTable');
  var status = document.getElementById('raStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('rates: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    lamS.value = p.lam;
    svcS.value = p.svc;
  }

  function redraw() {
    var lamV = +lamS.value, svcV = +svcS.value;
    var lam = R(BigInt(lamV), 1n), mu = muFromServiceMs(svcV);
    var rho = Rdiv(lam, mu), grow = growthPerSec(lam, mu);
    var after = backlogAfter(lam, mu, 60);
    var stable = Rcmp(rho, R(1n, 1n)) < 0;

    document.getElementById('raLamOut').textContent = commas(lamV) + ' / s';
    document.getElementById('raSvcOut').textContent = svcV + ' ms';
    document.getElementById('raMu').textContent = Rshort(mu, 2) + ' / s';
    document.getElementById('raRho').textContent = Rtext(rho) + ' = ' + Rfixed(rho, 4);
    document.getElementById('raGrow').textContent = Rshort(grow, 2) + ' / s';
    document.getElementById('raAfter').textContent = stable ? 'none — it drains'
      : commas(Rfixed(after, 0)) + ' waiting';

    table.innerHTML = '<thead><tr><th>quantity</th><th>how it is built</th><th>exactly</th></tr></thead><tbody>'
      + '<tr><td class="tone-cyan">&lambda;</td><td>the arrival rate you set</td><td>' + commas(lamV) + ' / s</td></tr>'
      + '<tr><td>S</td><td>mean service time, a duration</td><td>' + svcV + ' ms</td></tr>'
      + '<tr><td class="tone-green">&mu; = 1/S</td><td>1000 &divide; ' + svcV + ' ms</td><td>'
      + Rshort(mu, 2) + ' / s</td></tr>'
      + '<tr><td>&rho; = &lambda;/&mu;</td><td>' + commas(lamV) + ' &divide; ' + Rshort(mu, 2)
      + ' &mdash; the seconds cancel</td><td>' + Rtext(rho) + '</td></tr>'
      + '<tr><td class="' + (stable ? 'tone-muted' : 'tone-red') + '">&lambda; &minus; &mu;</td>'
      + '<td>how fast the backlog changes</td><td>' + Rshort(grow, 2) + ' / s</td></tr>'
      + '</tbody>';

    var top = Rcmp(lam, mu) > 0 ? lam : mu;
    var unit = 440 / Math.max(1, parseFloat(Rfixed(top, 4)));
    var lpx = Math.max(2, parseFloat(Rfixed(lam, 4)) * unit);
    var mpx = Math.max(2, parseFloat(Rfixed(mu, 4)) * unit);
    var s = '<text x="0" y="14" font-size="11" fill="var(--muted)">arrivals per second</text>'
      + '<rect x="0" y="22" width="' + lpx + '" height="26" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (lpx + 8) + '" y="40" font-size="11" fill="var(--cyan)" font-weight="700">'
      + commas(lamV) + '</text>'
      + '<text x="0" y="72" font-size="11" fill="var(--muted)">departures per second the server can manage</text>'
      + '<rect x="0" y="80" width="' + mpx + '" height="26" rx="3" fill="var(--green)" opacity="0.85" />'
      + '<text x="' + (mpx + 8) + '" y="98" font-size="11" fill="var(--green)" font-weight="700">'
      + Rshort(mu, 2) + '</text>';
    if (!stable) {
      s += '<rect x="' + mpx + '" y="22" width="' + Math.max(1, lpx - mpx) + '" height="26" rx="3" '
        + 'fill="var(--red)" opacity="0.7" />'
        + '<text x="' + mpx + '" y="130" font-size="10" fill="var(--red)">this gap, '
        + Rshort(grow, 2) + ' a second, never goes away &mdash; it accumulates</text>';
    } else {
      s += '<rect x="' + lpx + '" y="80" width="' + Math.max(1, mpx - lpx) + '" height="26" rx="3" '
        + 'fill="var(--muted)" opacity="0.35" />'
        + '<text x="0" y="130" font-size="10" fill="var(--muted)">the grey headroom is what absorbs a burst; '
        + 'at &rho; = ' + Rtext(rho) + ' there is ' + Rpct(Rsub(R(1n, 1n), rho), 1) + ' of it</text>';
    }
    s += '<line x1="0" y1="146" x2="520" y2="146" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="158" font-size="10" fill="var(--muted)">both bars are rates; &rho; is their ratio, '
      + 'and it has no units</text>';
    plot.innerHTML = s;

    status.innerHTML = stable
      ? 'A service taking <strong>' + svcV + ' ms</strong> is <strong>&mu; = ' + Rshort(mu, 2)
        + ' per second</strong> &mdash; not "' + svcV + '". At &lambda; = ' + commas(lamV)
        + ' that is <strong>&rho; = ' + Rtext(rho) + '</strong>, so the server is busy '
        + Rpct(rho, 1) + ' of the time and idle the rest. The backlog shrinks at '
        + Rshort(Rsub(R(0n, 1n), grow), 2) + ' a second whenever there is one, so it does not build.'
      : '<span class="tone-red">&rho; = ' + Rtext(rho) + ' &ge; 1.</span> There is no queue length to '
        + 'compute here, because nothing settles: work arrives ' + Rshort(grow, 2)
        + ' a second faster than it leaves, so after one minute <strong>'
        + commas(Rfixed(after, 0)) + '</strong> requests are waiting and after an hour sixty times that. '
        + 'This is a straight line, not a queue &mdash; every formula later in this course assumes '
        + '&rho; &lt; 1 and none of them applies above it.';
  }

  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  [lamS, svcS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Rates, not latencies",
        subtitle="ρ = λ/μ is a ratio of two rates, and ρ ≥ 1 is a straight line",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the load and the service"),
        panel_intro=cfg.get(
            "panel_intro",
            "&mu; is computed from the service time you set, &rho; from the two rates, and the "
            "growth rate from their difference. All three are exact fractions.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - trace
# ---------------------------------------------------------------------------

TRACE_PRESETS = [
    {"key": "five-customers", "label": "five customers over ten slots — the lesson's trace",
     "arr": "0 1 2 5 6", "dep": "3 4 6 8 10", "T": 10},
    {"key": "all-at-once", "label": "the same five, arriving together — L moves, W does not",
     "arr": "0 0 0 0 0", "dep": "3 4 6 8 10", "T": 10},
    {"key": "one-at-a-time", "label": "one at a time, never overlapping — L is the busy fraction",
     "arr": "0 2 4 6 8", "dep": "2 4 6 8 10", "T": 10},
]


def _trace(cfg):
    idx = _preset_index(cfg, TRACE_PRESETS, "trace")
    pre = TRACE_PRESETS[idx]

    markup = (
        _toolbar(
            "Little's Law on a trace",
            "the area under N(t), and the sum of the times &mdash; the same number, counted twice",
            [("cyan", "N(t)"), ("amber", "each customer's stay"), ("red", "still in flight")],
        )
        + _stage(
            _svg("trPlot", "0 0 520 190", "The number-in-system staircase with its area shaded, above a bar per customer.")
        )
        + _table("trTable")
        + _banner("trStatus")
    )
    controls = (
        _select("trPreset", "Worked example", [(p["key"], p["label"]) for p in TRACE_PRESETS], pre["key"])
        + _text("trArr", "Arrival times (slots)", pre["arr"])
        + _text("trDep", "Departure times (slots, same order)", pre["dep"])
        + _range("trT", "Measurement window T (slots)", 1, 24, pre["T"])
        + _kpis(
            [
                ("L &mdash; area &divide; T", "trL"),
                ("&lambda; &mdash; arrivals &divide; T", "trLam"),
                ("W &mdash; mean time in system", "trW"),
                ("&lambda;W, which should be L", "trLamW"),
            ]
        )
        + _hint(
            "trHint",
            "Nothing here assumes a distribution. The area under the staircase and the sum of the "
            "customers' stays are two ways of adding up the same rectangles, so L = &lambda;W is an "
            "identity. Shorten T below the last departure and watch it stop holding &mdash; not "
            "because the law failed, but because the three averages are then over different people.",
        )
    )

    script = _CORE_JS + _presets_js(TRACE_PRESETS) + r"""
  var sel = document.getElementById('trPreset');
  var arrIn = document.getElementById('trArr'), depIn = document.getElementById('trDep');
  var tS = document.getElementById('trT');
  var plot = document.getElementById('trPlot'), table = document.getElementById('trTable');
  var status = document.getElementById('trStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('trace: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    arrIn.value = p.arr;
    depIn.value = p.dep;
    tS.value = p.T;
  }
  function nums(text) {
    var raw = String(text).split(/[^0-9]+/), out = [], i;
    for (i = 0; i < raw.length; i += 1) if (raw[i]) out.push(Number(raw[i]));
    return out;
  }

  function redraw() {
    var arr = nums(arrIn.value), dep = nums(depIn.value), T = +tS.value;
    document.getElementById('trTOut').textContent = T + ' slots';
    var n = Math.min(arr.length, dep.length), i, ok = n > 0;
    arr = arr.slice(0, n); dep = dep.slice(0, n);
    for (i = 0; i < n; i += 1) if (dep[i] <= arr[i]) ok = false;

    if (!ok) {
      plot.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">'
        + 'Every customer needs an arrival and a strictly later departure.</text>';
      table.innerHTML = '';
      document.getElementById('trL').textContent = '—';
      document.getElementById('trLam').textContent = '—';
      document.getElementById('trW').textContent = '—';
      document.getElementById('trLamW').textContent = '—';
      status.innerHTML = '<span class="tone-red">Give the same number of arrivals and departures, '
        + 'each departure after its arrival.</span> The identity is about customers who were both '
        + 'counted in and counted out; a customer with no arrival is not a customer.';
      return;
    }

    var w = littleWindow(arr, dep, T);
    var full = littleFromTrace(arr, dep);
    document.getElementById('trL').textContent = Rtext(w.L);
    document.getElementById('trLam').textContent = Rtext(w.lambda) + ' / slot';
    document.getElementById('trW').textContent = Rtext(w.W) + ' slots';
    document.getElementById('trLamW').textContent = Rtext(w.lamW);

    var rows = '<thead><tr><th>customer</th><th>in</th><th>out</th><th>stay</th><th>counted?</th></tr></thead><tbody>';
    for (i = 0; i < n; i += 1) {
      var inWindow = arr[i] < T, done = inWindow && dep[i] <= T;
      rows += '<tr><td>#' + (i + 1) + '</td><td>' + arr[i] + '</td><td>' + dep[i] + '</td><td>'
        + (dep[i] - arr[i]) + '</td><td class="' + (done ? 'tone-green' : 'tone-red') + '">'
        + (done ? 'yes' : (inWindow ? 'still in flight at T' : 'arrives after T')) + '</td></tr>';
    }
    rows += '<tr><td colspan="3">area under N(t) on [0, ' + T + ')</td><td>' + w.area
      + '</td><td class="tone-cyan">= &Sigma; stays when all are done</td></tr>';
    rows += '</tbody>';
    table.innerHTML = rows;

    /* the staircase */
    var occ = occupancyTrace(arr, dep, T), peak = 1, t;
    for (t = 0; t < occ.length; t += 1) if (occ[t] > peak) peak = occ[t];
    var W0 = 500 / Math.max(1, T), H = 92, base = 104;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">N(t), the number in the system &mdash; '
      + 'the shaded area is ' + w.area + '</text>';
    for (t = 0; t < occ.length; t += 1) {
      if (!occ[t]) continue;
      var h = (occ[t] / peak) * H;
      s += '<rect x="' + (10 + t * W0) + '" y="' + (base - h) + '" width="' + Math.max(1, W0 - 1)
        + '" height="' + h + '" fill="var(--cyan)" opacity="0.5" />';
      s += '<text x="' + (10 + t * W0 + W0 / 2) + '" y="' + (base - h - 3) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--cyan)">' + occ[t] + '</text>';
    }
    s += '<line x1="10" y1="' + base + '" x2="' + (10 + T * W0) + '" y2="' + base
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 13) + '" font-size="9" fill="var(--muted)">t = 0</text>'
      + '<text x="' + (10 + T * W0) + '" y="' + (base + 13) + '" text-anchor="end" font-size="9" '
      + 'fill="var(--muted)">T = ' + T + '</text>';
    for (i = 0; i < n && i < 10; i += 1) {
      var y = 126 + i * 6, x0 = 10 + arr[i] * W0, x1 = 10 + Math.min(dep[i], T) * W0;
      var cut = dep[i] > T;
      s += '<rect x="' + x0 + '" y="' + y + '" width="' + Math.max(2, x1 - x0) + '" height="4" rx="2" fill="var('
        + (cut ? '--red' : '--amber') + ')" opacity="0.85" />';
    }
    s += '<text x="10" y="186" font-size="10" fill="var(--muted)">each bar is one customer\'s stay; '
      + 'stack them and you have the shaded area above</text>';
    plot.innerHTML = s;

    if (w.holds) {
      status.innerHTML = 'Over ' + T + ' slots the area under N(t) is <strong>' + w.area
        + '</strong> and the ' + w.done + ' completed stays add to the same <strong>' + w.area
        + '</strong> &mdash; they are the same rectangles counted along two different axes. So L = '
        + Rtext(w.L) + ', &lambda; = ' + Rtext(w.lambda) + ' per slot, W = ' + Rtext(w.W)
        + ' slots, and <strong>&lambda;W = ' + Rtext(w.lamW) + ' = L</strong>, exactly. '
        + 'No arrival distribution was assumed anywhere in that, and none is needed: '
        + 'it is a statement about an area.';
    } else {
      status.innerHTML = '<span class="tone-red">&lambda;W = ' + Rtext(w.lamW) + ', but L = '
        + Rtext(w.L) + '.</span> The law has not failed &mdash; the window has. '
        + w.inflight + ' of the ' + w.arrived + ' customers who arrived before T = ' + T
        + ' are still in the system at T, so their time is in the area but not in W, which '
        + 'averages only the ' + w.done + ' that finished. Take the window out to '
        + full.horizon + ' slots, where everyone has left, and the two sides agree at '
        + Rtext(full.L) + ' again.';
    }
  }

  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  [arrIn, depIn].forEach(function (el) { el.addEventListener('input', redraw); });
  tS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Little's Law, proved by counting",
        subtitle="L = λW with no distribution in it anywhere",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the trace"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both sides are recomputed from the times you type: the area under the staircase on the "
            "left, the sum of the stays on the right. Shorten T to see what a window with work still "
            "in flight does to them.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - little
# ---------------------------------------------------------------------------


def _little(cfg):
    solve = cfg.get("solve", "L")
    if solve not in ("L", "lambda", "W"):
        raise ValueError("queue mode 'little': solve must be L, lambda or W, not %r" % (solve,))
    rate = int(cfg.get("rate", 500))
    wait = int(cfg.get("wait", 40))
    pool = int(cfg.get("pool", 20))

    markup = (
        _toolbar(
            "Sizing with L = &lambda;W",
            "concurrency = throughput &times; latency, solved for whichever one you do not know",
            [("cyan", "L, in flight"), ("amber", "&lambda;, per second"), ("green", "W, milliseconds")],
        )
        + _stage(_svg("liPlot", "0 0 520 170", "A rectangle whose width is the arrival rate and whose height is the wait, with its area the concurrency."))
        + _table("liTable")
        + _banner("liStatus")
    )
    controls = (
        _select(
            "liSolve",
            "Which one is unknown",
            [
                ("L", "L &mdash; how many are in flight (size the pool)"),
                ("lambda", "&lambda; &mdash; the throughput a pool can support"),
                ("W", "W &mdash; the latency the other two imply"),
            ],
            solve,
        )
        + _range("liRate", "&lambda; &mdash; throughput (requests per second)", 10, 4000, rate, 10)
        + _range("liWait", "W &mdash; time in system (ms)", 1, 500, wait)
        + _range("liPool", "L &mdash; pool size (connections in flight)", 1, 400, pool)
        + _kpis(
            [
                ("The unknown", "liAnswer"),
                ("L", "liL"),
                ("&lambda;", "liLam"),
                ("W", "liW"),
            ]
        )
        + _hint(
            "liHint",
            "The unit trap is the whole lesson: &lambda; is per <em>second</em> and W is in "
            "<em>milliseconds</em>, so L = &lambda;W &divide; 1000. A thread that spends its time "
            "waiting on I/O is in flight and occupies a slot whether or not a core is running it, "
            "so core count does not size this.",
        )
    )

    script = _CORE_JS + r"""
  var solveSel = document.getElementById('liSolve');
  var rateS = document.getElementById('liRate'), waitS = document.getElementById('liWait');
  var poolS = document.getElementById('liPool');
  var plot = document.getElementById('liPlot'), table = document.getElementById('liTable');
  var status = document.getElementById('liStatus');

  function redraw() {
    var which = solveSel.value;
    if (which !== 'L' && which !== 'lambda' && which !== 'W') {
      throw new Error('little: no unknown named ' + which);
    }
    var rate = R(BigInt(+rateS.value), 1n);
    var wait = R(BigInt(+waitS.value), 1n);
    var pool = R(BigInt(+poolS.value), 1n);
    var thousand = R(1000n, 1n);
    var L, lam, W, derivedLabel;

    if (which === 'L') {
      lam = rate; W = wait;
      L = poolForRate(lam, W);                    /* lambda * W / 1000 */
      derivedLabel = 'L = &lambda;W = ' + Rtext(lam) + ' &times; ' + Rtext(W) + ' ms';
    } else if (which === 'lambda') {
      L = pool; W = wait;
      lam = poolCapPerSec(+poolS.value, W);       /* 1000 L / W */
      derivedLabel = '&lambda; = L/W = ' + Rtext(L) + ' &divide; ' + Rtext(W) + ' ms';
    } else {
      L = pool; lam = rate;
      W = Rdiv(Rmul(L, thousand), lam);           /* 1000 L / lambda */
      derivedLabel = 'W = L/&lambda; = ' + Rtext(L) + ' &divide; ' + Rtext(lam) + ' / s';
    }

    document.getElementById('liRateOut').textContent = commas(+rateS.value) + ' / s'
      + (which === 'lambda' ? ' (derived, not read)' : '');
    document.getElementById('liWaitOut').textContent = (+waitS.value) + ' ms'
      + (which === 'W' ? ' (derived, not read)' : '');
    document.getElementById('liPoolOut').textContent = commas(+poolS.value)
      + (which === 'L' ? ' (derived, not read)' : '');

    document.getElementById('liL').textContent = Rshort(L, 3) + ' in flight';
    document.getElementById('liLam').textContent = Rshort(lam, 2) + ' / s';
    document.getElementById('liW').textContent = Rshort(W, 3) + ' ms';
    document.getElementById('liAnswer').textContent =
      which === 'L' ? Rshort(L, 3) + ' in flight'
      : (which === 'lambda' ? Rshort(lam, 2) + ' / s' : Rshort(W, 3) + ' ms');

    var check = Rdiv(Rmul(lam, W), thousand);
    table.innerHTML = '<thead><tr><th>symbol</th><th>reads</th><th>units</th><th>value</th></tr></thead><tbody>'
      + '<tr><td class="tone-cyan">L</td><td>number in the system at once</td><td>requests (no time in it)</td><td>'
      + Rshort(L, 3) + '</td></tr>'
      + '<tr><td class="tone-amber">&lambda;</td><td>arrivals that complete per second</td><td>1/s</td><td>'
      + Rshort(lam, 2) + '</td></tr>'
      + '<tr><td class="tone-green">W</td><td>time each one is in the system</td><td>ms</td><td>'
      + Rshort(W, 3) + '</td></tr>'
      + '<tr><td>&lambda;W &divide; 1000</td><td>' + derivedLabel + '</td><td>requests</td><td>'
      + Rshort(check, 3) + '</td></tr>'
      + '<tr><td>a pool of ' + commas(Rfixed(L, 0)) + '</td><td>caps throughput at L/W</td><td>1/s</td><td>'
      + Rshort(poolCapPerSec(Number(Rfixed(L, 0)), W), 2) + '</td></tr>'
      + '</tbody>';

    var wpx = Math.min(430, 6 + parseFloat(Rfixed(lam, 3)) / 10);
    var hpx = Math.min(96, 6 + parseFloat(Rfixed(W, 3)) / 5);
    var s = '<rect x="16" y="' + (112 - hpx) + '" width="' + wpx + '" height="' + hpx
      + '" fill="var(--cyan)" opacity="0.28" stroke="var(--cyan)" stroke-width="1" />'
      + '<text x="' + (16 + wpx / 2) + '" y="' + (112 - hpx / 2)
      + '" text-anchor="middle" font-size="12" fill="var(--cyan)" font-weight="700">L = '
      + Rshort(L, 2) + '</text>'
      + '<line x1="16" y1="122" x2="' + (16 + wpx) + '" y2="122" stroke="var(--amber)" stroke-width="2" />'
      + '<text x="' + (16 + wpx / 2) + '" y="136" text-anchor="middle" font-size="10" fill="var(--amber)">'
      + '&lambda; = ' + Rshort(lam, 2) + ' / s</text>'
      + '<line x1="8" y1="' + (112 - hpx) + '" x2="8" y2="112" stroke="var(--green)" stroke-width="2" />'
      + '<text x="14" y="' + (108 - hpx) + '" font-size="10" fill="var(--green)">W = '
      + Rshort(W, 2) + ' ms</text>'
      + '<line x1="0" y1="150" x2="520" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="164" font-size="10" fill="var(--muted)">the area is the concurrency; '
      + 'widen the rate or raise the latency and the same rectangle grows</text>';
    plot.innerHTML = s;

    var cores = 8;
    status.innerHTML = 'Solving for <strong>' + (which === 'lambda' ? '&lambda;' : which)
      + '</strong>: ' + derivedLabel + ' = <strong>'
      + (which === 'L' ? Rshort(L, 3) + ' in flight'
         : (which === 'lambda' ? Rshort(lam, 2) + ' per second' : Rshort(W, 3) + ' ms'))
      + '</strong>. A pool of <strong>' + commas(Rfixed(L, 0)) + '</strong> at this latency cannot '
      + 'exceed <strong>' + Rshort(poolCapPerSec(Number(Rfixed(L, 0)), W), 2)
      + ' per second</strong> however fast the machine is, because each slot is occupied for '
      + Rshort(W, 2) + ' ms whatever it is doing. That is why ' + cores + ' cores is not the answer: '
      + 'a thread blocked on I/O still holds its slot, so the number you need is '
      + Rshort(L, 2) + ', not ' + cores + '.';
  }

  solveSel.addEventListener('change', redraw);
  [rateS, waitS, poolS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Sizing with Little's Law",
        subtitle="Concurrency, throughput and latency: fix any two",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fix two, read the third"),
        panel_intro=cfg.get(
            "panel_intro",
            "The identity is solved in the browser for whichever quantity you mark unknown, with "
            "the unit conversion done once and printed.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - slotted
# ---------------------------------------------------------------------------

_SLOT_SIZES = [("1", "&Delta; = 1 (one slot per time unit)"),
               ("2", "&Delta; = 1/2"),
               ("5", "&Delta; = 1/5"),
               ("10", "&Delta; = 1/10")]


def _slotted(cfg):
    p_num = int(cfg.get("p20", 8))
    q_num = int(cfg.get("q20", 10))
    sub = int(cfg.get("sub", 1))
    seed = int(cfg.get("seed", 7))
    warm = int(cfg.get("warm", 10))

    markup = (
        _toolbar(
            "Bunching, not overload",
            "Bernoulli arrivals against a clockwork schedule, at exactly the same &rho;",
            [("cyan", "Bernoulli arrivals"), ("green", "D/D/1, same &rho;"),
             ("amber", "running mean"), ("purple", "exact Geo/Geo/1")],
        )
        + _stage(
            _svg("slPlot", "0 0 520 210",
                 "The random queue-length trace above a deterministic one, with both running means below.")
            + _svg("slTrans", "0 0 520 128",
                   "The mean occupancy at each slot averaged over many runs, rising from zero.")
        )
        + _table("slTable")
        + _banner("slStatus")
    )
    controls = (
        _range("slP", "p &mdash; arrival probability per slot (twentieths)", 1, 19, p_num)
        + _range("slQ", "q &mdash; service completion probability per slot (twentieths)", 2, 20, q_num)
        + _select("slSub", "Slot size", _SLOT_SIZES, str(sub))
        + _range("slSeed", "Seed", 1, 40, seed)
        + _range("slWarm", "Warm-up discarded (% of the run)", 0, 40, warm)
        + _kpis(
            [
                ("Mean N from t = 0", "slMean0"),
                ("Mean N after warm-up", "slMeanW"),
                ("D/D/1 mean at the same &rho;", "slMeanD"),
                ("Random &divide; clockwork", "slRatio"),
            ]
        )
        + _hint(
            "slHint",
            "The model is named, because a slotted simulation is a model and not a measurement: "
            "one Bernoulli arrival per slot with probability p, geometric service with parameter q, "
            "under the <em>late-arrival</em> convention &mdash; a departure is resolved before an "
            "arrival inside the same slot. That is the Geo/Geo/1 chain, and its exact answer is "
            "solved in Operations Research, <span class=\"tt\">queues-in-discrete-time</span>. "
            "It is not M/M/1, and at &Delta; = 1 it is not close to it.",
        )
    )

    script = _CORE_JS + r"""
  var pS = document.getElementById('slP'), qS = document.getElementById('slQ');
  var subSel = document.getElementById('slSub'), seedS = document.getElementById('slSeed');
  var warmS = document.getElementById('slWarm');
  var plot = document.getElementById('slPlot'), trans = document.getElementById('slTrans');
  var table = document.getElementById('slTable'), status = document.getElementById('slStatus');
  var BASE = 2000;

  function polyline(pts, colour, width, dash) {
    if (!pts.length) return '';
    return '<polyline fill="none" stroke="var(' + colour + ')" stroke-width="' + width + '"'
      + (dash ? ' stroke-dasharray="' + dash + '"' : '')
      + ' points="' + pts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />';
  }

  function redraw() {
    var pn = +pS.value, qn = +qS.value, k = +subSel.value, seed = +seedS.value, warmPct = +warmS.value;
    if (pn >= qn) { qn = Math.min(20, pn + 1); qS.value = qn; }
    var kb = BigInt(k);
    var p = R(BigInt(pn), 20n * kb), q = R(BigInt(qn), 20n * kb);
    var rho = Rdiv(p, q);
    var slots = BASE * k, warmSlots = Math.floor(slots * warmPct / 100);

    document.getElementById('slPOut').textContent = Rtext(p);
    document.getElementById('slQOut').textContent = Rtext(q);
    document.getElementById('slSeedOut').textContent = String(seed);
    document.getElementById('slWarmOut').textContent = warmPct + '% (' + commas(warmSlots) + ' slots)';

    var run = slottedRun(p, q, seed, slots);
    var A = Number(rho.d) * k, S = Number(rho.n) * k;
    var det = ddRun(A, S, slots);
    var exact = geoGeo1(p, q);
    var mean0 = runMean(run, 0), meanW = runMean(run, warmSlots), meanD = runMean(det, 0);

    document.getElementById('slMean0').textContent = Rfixed(mean0, 4);
    document.getElementById('slMeanW').textContent = Rfixed(meanW, 4);
    document.getElementById('slMeanD').textContent = Rtext(meanD);
    document.getElementById('slRatio').innerHTML = Rzero(meanD) ? '&mdash;'
      : Rfixed(Rdiv(meanW, meanD), 3) + '&times;';

    var peak = Math.max(1, runMax(run.slice(0, 240)));
    var show = Math.min(240, slots), W0 = 500 / show, base = 92, i;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">the first ' + show
      + ' slots &mdash; <tspan fill="var(--cyan)">Bernoulli arrivals</tspan> against '
      + '<tspan fill="var(--green)">an arrival every ' + A + ' slots, served in exactly ' + S + '</tspan></text>';
    for (i = 0; i < show; i += 1) {
      if (!run[i]) continue;
      var h = (run[i] / peak) * 68;
      s += '<rect x="' + (10 + i * W0) + '" y="' + (base - h) + '" width="' + Math.max(0.8, W0 - 0.3)
        + '" height="' + h + '" fill="var(--cyan)" opacity="0.55" />';
    }
    var dpts = [];
    for (i = 0; i < show; i += 1) dpts.push([10 + i * W0, base - (det[i] / peak) * 68]);
    s += polyline(dpts, '--green', 1.2, '');
    s += '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 12) + '" font-size="9" fill="var(--muted)">peak of ' + peak
      + ' waiting on the random run; the clockwork run never exceeds 1</text>';

    var rmA = runningMeans(run, 0, 180), rmD = runningMeans(det, 0, 180);
    var top = Math.max(parseFloat(Rfixed(exact.stable ? exact.L : mean0, 3)), parseFloat(Rfixed(mean0, 3))) * 1.5 + 0.5;
    function yOf(v) { return 196 - (v / top) * 62; }
    s += '<text x="0" y="122" font-size="11" fill="var(--muted)">the running means, over all '
      + commas(slots) + ' slots</text>';
    s += polyline(rmA.map(function (r) { return [10 + (r[0] / slots) * 500, yOf(parseFloat(Rfixed(r[1], 4)))]; }), '--amber', 1.6, '');
    s += polyline(rmD.map(function (r) { return [10 + (r[0] / slots) * 500, yOf(parseFloat(Rfixed(r[1], 4)))]; }), '--green', 1.4, '');
    if (exact.stable) {
      var ye = yOf(parseFloat(Rfixed(exact.L, 4)));
      s += '<line x1="10" y1="' + ye + '" x2="510" y2="' + ye
        + '" stroke="var(--purple)" stroke-width="1.2" stroke-dasharray="4 3" />'
        + '<text x="510" y="' + (ye - 4) + '" text-anchor="end" font-size="9" fill="var(--purple)">'
        + 'exact Geo/Geo/1 L = ' + Rtext(exact.L) + '</text>';
    }
    if (warmSlots > 0) {
      var xw = 10 + (warmSlots / slots) * 500;
      s += '<line x1="' + xw + '" y1="130" x2="' + xw + '" y2="196" stroke="var(--red)" stroke-width="1" stroke-dasharray="2 3" />'
        + '<text x="' + (xw + 3) + '" y="138" font-size="9" fill="var(--red)">warm-up ends</text>';
    }
    s += '<line x1="10" y1="196" x2="510" y2="196" stroke="var(--line-strong)" stroke-width="1" />';
    plot.innerHTML = s;

    /* The initial transient, as an ensemble rather than as an argument. */
    var seeds = 24, span = 160;
    var curve = transientCurve(p, q, seed, seeds, span);
    var earlyMean = curveMean(curve, 0, Math.floor(span / 8));
    var lateMean = curveMean(curve, Math.floor(span / 2), span);
    var ctop = parseFloat(Rfixed(exact.stable ? exact.L : R(1n, 1n), 3)) * 1.4 + 0.3;
    var t2 = '<text x="0" y="12" font-size="11" fill="var(--muted)">E[N at slot t], averaged over '
      + seeds + ' runs that all start empty &mdash; this is the initial transient</text>';
    t2 += polyline(curve.map(function (v, ix) {
      return [10 + (ix / span) * 500, 100 - (parseFloat(Rfixed(v, 4)) / ctop) * 70];
    }), '--cyan', 1.4, '');
    if (exact.stable) {
      var yl = 100 - (parseFloat(Rfixed(exact.L, 4)) / ctop) * 70;
      t2 += '<line x1="10" y1="' + yl + '" x2="510" y2="' + yl
        + '" stroke="var(--purple)" stroke-width="1.2" stroke-dasharray="4 3" />';
    }
    t2 += '<line x1="10" y1="100" x2="510" y2="100" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="114" font-size="9" fill="var(--muted)">t = 0, empty</text>'
      + '<text x="510" y="114" text-anchor="end" font-size="9" fill="var(--muted)">t = ' + span + '</text>'
      + '<text x="10" y="126" font-size="10" fill="var(--muted)">E[N] over the first '
      + Math.floor(span / 8) + ' slots is ' + Rfixed(earlyMean, 3) + ' against ' + Rfixed(lateMean, 3)
      + ' over the last half &mdash; that is the bias, and it is downward</text>';
    trans.innerHTML = t2;

    var ca2 = slottedCa2(p), cs2 = slottedCs2(q);
    table.innerHTML = '<thead><tr><th>row</th><th>what it is</th><th>value</th></tr></thead><tbody>'
      + '<tr><td>p, q</td><td>arrival and service probabilities per slot</td><td>' + Rtext(p) + ', ' + Rtext(q) + '</td></tr>'
      + '<tr><td>&rho; = p/q</td><td>the same for both runs, by construction</td><td>' + Rtext(rho) + '</td></tr>'
      + '<tr><td>c<sub>a</sub><sup>2</sup>, c<sub>s</sub><sup>2</sup></td>'
      + '<td>1 &minus; p and 1 &minus; q for this chain; 0 and 0 for the clockwork one</td><td>'
      + Rtext(ca2) + ', ' + Rtext(cs2) + '</td></tr>'
      + '<tr><td class="tone-cyan">random, from t = 0</td><td>one run, transient included</td><td>'
      + Rfixed(mean0, 4) + '</td></tr>'
      + '<tr><td class="tone-amber">random, after warm-up</td><td>the same run, first ' + commas(warmSlots)
      + ' slots discarded</td><td>' + Rfixed(meanW, 4) + '</td></tr>'
      + '<tr><td class="tone-cyan">ensemble, slots 0 to ' + Math.floor(span / 8) + '</td>'
      + '<td>E[N] over ' + seeds + ' runs, while the transient is still running</td><td>'
      + Rfixed(earlyMean, 4) + '</td></tr>'
      + '<tr><td class="tone-amber">ensemble, slots ' + Math.floor(span / 2) + ' to ' + span + '</td>'
      + '<td>the same ' + seeds + ' runs, once the transient has decayed</td><td>'
      + Rfixed(lateMean, 4) + '</td></tr>'
      + '<tr><td class="tone-green">clockwork D/D/1</td><td>same &rho;, nothing random</td><td>'
      + Rtext(meanD) + '</td></tr>'
      + '<tr><td class="tone-purple">exact Geo/Geo/1</td><td>&rho;(1 &minus; p)/(1 &minus; &rho;), '
      + 'solved in Operations Research</td><td>'
      + (exact.stable ? Rtext(exact.L) : 'unstable') + '</td></tr>'
      + '<tr><td class="tone-red">&rho;/(1 &minus; &rho;)</td><td>the continuous M/M/1 formula, '
      + 'which is a different model</td><td>' + Rtext(Rdiv(rho, Rsub(R(1n, 1n), rho))) + '</td></tr>'
      + '</tbody>';

    status.innerHTML = 'Both runs are at <strong>&rho; = ' + Rtext(rho) + '</strong>. The clockwork one '
      + '&mdash; an arrival every ' + A + ' slots, served in exactly ' + S + ' &mdash; holds <strong>'
      + Rtext(meanD) + '</strong>, which is &rho; itself: the server is busy that fraction of the time and '
      + '<em>nothing ever waits</em>. The Bernoulli run, at the same utilisation, holds <strong>'
      + Rfixed(meanW, 4) + '</strong>, about <strong>' + (Rzero(meanD) ? '—' : Rfixed(Rdiv(meanW, meanD), 2))
      + '&times;</strong> as much, and peaks at ' + peak + '. Nothing is overloaded in either run. '
      + 'What waits is the bunching. '
      + (exact.stable
          ? 'The exact answer for this chain is <span class="tone-purple">' + Rtext(exact.L)
            + '</span> &mdash; the Geo/Geo/1 mean, derived in Operations Research. Note what it is '
            + '<em>not</em>: &rho;/(1 &minus; &rho;) = ' + Rtext(Rdiv(rho, Rsub(R(1n, 1n), rho)))
            + ', the M/M/1 answer, which belongs to a different model and only meets this one as the '
            + 'slot shrinks. '
          : '')
      + 'One last thing, and it is what the second drawing is for: <strong>the simulation starts '
      + 'empty</strong>. Over ' + seeds + ' runs, E[N] across the first ' + Math.floor(span / 8)
      + ' slots is <strong>' + Rfixed(earlyMean, 3) + '</strong> and across the last half it is '
      + '<strong>' + Rfixed(lateMean, 3) + '</strong>, so a mean taken from t = 0 is biased low. '
      + 'That is the initial transient. On <em>one</em> run the bias is smaller than the sampling '
      + 'noise and can land either way &mdash; here ' + Rfixed(mean0, 4) + ' from t = 0 against '
      + Rfixed(meanW, 4) + ' after the warm-up &mdash; which is exactly why a warm-up is discarded '
      + 'as a matter of routine rather than argued about run by run. Operations Research, '
      + '<span class="tt">warm-up-and-the-initial-transient</span>, is where that argument lives.';
  }

  [pS, qS, seedS, warmS].forEach(function (el) { el.addEventListener('input', redraw); });
  subSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Why queues form below full utilisation",
        subtitle="A seeded slotted run against a clockwork one, at exactly the same ρ",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the slotted model"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both runs are simulated in the browser from the seed you set, and the exact answer for "
            "the random one is computed from the chain beside them. The simulation shows the "
            "phenomenon; the exact number is a formula, not a measurement.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - memoryless
# ---------------------------------------------------------------------------

_DELTAS = [("1", "&Delta; = 1 second"), ("2", "&Delta; = 1/2 second"),
           ("10", "&Delta; = 1/10 second"), ("100", "&Delta; = 1/100 second")]


# The exponential column is computed by the core's alternating series, which is
# accurate to about seven significant figures at x = 12 and to none at all by
# x = 19. lambda*t IS that x, so the controls stop where the method does and the
# panel says why. A preset that asked for more would print a wrong number under
# a promise of a checkable one, so it raises instead.
_EXP_SAFE_X = 12


def _memoryless(cfg):
    lam10 = int(cfg.get("lam10", 5))
    t = int(cfg.get("t", 4))
    inv = int(cfg.get("inv_delta", 10))
    already = int(cfg.get("already", 3))
    if lam10 * t > 10 * _EXP_SAFE_X:
        raise ValueError(
            "queue mode 'memoryless': lambda*t = %s exceeds %d, where the core's "
            "alternating series for e^-x has lost every significant digit to "
            "cancellation" % (lam10 * t / 10.0, _EXP_SAFE_X)
        )

    markup = (
        _toolbar(
            "From geometric to exponential",
            "(1 &minus; &lambda;&Delta;)<sup>t/&Delta;</sup> exactly, against e<sup>&minus;&lambda;t</sup> rounded",
            [("cyan", "geometric, exact"), ("red", "exponential, rounded"), ("amber", "the gap")],
        )
        + _stage(
            _svg("mePlot", "0 0 520 178",
                 "The geometric survival curve drawn against the exponential it converges to.")
        )
        + _table("meTable")
        + _banner("meStatus")
    )
    controls = (
        _range("meLam", "&lambda; &mdash; arrivals per second (tenths)", 1, 15, lam10)
        + _range("meT", "t &mdash; how long we wait (seconds)", 1, 8, t)
        + _select("meDelta", "Slot size &Delta;", _DELTAS, str(inv))
        + _range("meAlready", "s &mdash; how long it has <em>already</em> been quiet (seconds)", 0, 10, already)
        + _kpis(
            [
                ("P(T &gt; t), geometric &mdash; exact", "meGeo"),
                ("P(T &gt; t) = e<sup>&minus;&lambda;t</sup> &mdash; rounded", "meExp"),
                ("Geometric &minus; exponential", "meGap"),
                ("P(T &gt; s+t | T &gt; s)", "meCond"),
            ]
        )
        + _hint(
            "meHint",
            "The geometric column is an exact fraction: (1 &minus; &lambda;&Delta;) is rational and "
            "the exponent t/&Delta; is a whole number of slots. The exponential column is "
            "<em>not</em> exact &mdash; e<sup>&minus;x</sup> is computed by its series and says so. "
            "Shrink &Delta; and the exact column walks toward the rounded one. The sliders stop at "
            "&lambda;t = 12 because that is where the series stops being able to answer: it "
            "alternates, so it loses about 2x/ln&nbsp;10 significant digits to cancellation, and by "
            "x = 19 a double has none left. The exact column has no such limit, which is the "
            "argument for exactness in one line.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('meLam'), tS = document.getElementById('meT');
  var dSel = document.getElementById('meDelta'), sS = document.getElementById('meAlready');
  var plot = document.getElementById('mePlot'), table = document.getElementById('meTable');
  var status = document.getElementById('meStatus');

  function redraw() {
    var lam = R(BigInt(+lamS.value), 10n), t = +tS.value, inv = +dSel.value, s = +sS.value;
    document.getElementById('meLamOut').textContent = Rtext(lam) + ' / s';
    document.getElementById('meTOut').textContent = t + ' s';
    document.getElementById('meAlreadyOut').textContent = s + ' s';

    var legal = Rcmp(Rmul(lam, R(1n, BigInt(inv))), R(1n, 1n)) <= 0;
    if (!legal) {
      plot.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">&lambda;&Delta; = '
        + Rtext(Rmul(lam, R(1n, BigInt(inv)))) + ' is not a probability. Choose a smaller slot.</text>';
      table.innerHTML = '';
      ['meGeo', 'meExp', 'meGap', 'meCond'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      status.innerHTML = '<span class="tone-red">&lambda;&Delta; must be at most 1.</span> At &lambda; = '
        + Rtext(lam) + ' per second a slot of ' + Rtext(R(1n, BigInt(inv)))
        + ' s would need more than one arrival in it, which a Bernoulli slot cannot hold. '
        + 'That is the first thing the shrinking slot buys: enough room for the model to be a model.';
      return;
    }

    var geo = geoTail(lam, inv, t);
    var ex = expTailApprox(lam, t);
    var gap = Rsub(geo, R(BigInt(Math.round(ex * 1000000000)), 1000000000n));
    var cond = geoCondTail(lam, inv, s, t);

    document.getElementById('meGeo').textContent = Rfixed(geo, 6);
    document.getElementById('meExp').textContent = ex.toFixed(6) + ' (rounded)';
    document.getElementById('meGap').textContent = Rfixed(gap, 6);
    document.getElementById('meCond').textContent = cond ? Rfixed(cond, 6) : '—';

    var rows = '<thead><tr><th>&Delta;</th><th>slots in ' + t + ' s</th>'
      + '<th>(1 &minus; &lambda;&Delta;)<sup>t/&Delta;</sup>, exact</th>'
      + '<th>e<sup>&minus;&lambda;t</sup>, rounded</th><th>gap</th></tr></thead><tbody>';
    var scale = [1, 2, 10, 100], i;
    for (i = 0; i < scale.length; i += 1) {
      var d = scale[i];
      if (Rcmp(Rmul(lam, R(1n, BigInt(d))), R(1n, 1n)) > 0) continue;
      var g = geoTail(lam, d, t);
      var gg = Rsub(g, R(BigInt(Math.round(ex * 1000000000)), 1000000000n));
      rows += '<tr><td class="' + (d === inv ? 'tone-cyan' : 'tone-muted') + '">'
        + Rtext(R(1n, BigInt(d))) + '</td><td>' + commas(t * d) + '</td><td>' + Rfixed(g, 8)
        + '</td><td>' + ex.toFixed(8) + '</td><td class="tone-amber">' + Rfixed(gg, 8) + '</td></tr>';
    }
    rows += '</tbody>';
    table.innerHTML = rows;

    var W0 = 500 / t, base = 128, pts = [], epts = [], k;
    for (k = 0; k <= t * 4; k += 1) {
      var tt = k / 4;
      var whole = Math.round(tt * inv);
      var gv = Rpow(Rsub(R(1n, 1n), Rmul(lam, R(1n, BigInt(inv)))), whole);
      pts.push([10 + tt * W0, base - parseFloat(Rfixed(gv, 6)) * 100]);
      epts.push([10 + tt * W0, base - expNegApprox(Rnum(lam) * tt, 1e-15) * 100]);
    }
    function poly(list, colour, width, dash) {
      return '<polyline fill="none" stroke="var(' + colour + ')" stroke-width="' + width + '"'
        + (dash ? ' stroke-dasharray="' + dash + '"' : '') + ' points="'
        + list.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />';
    }
    var sv = '<text x="0" y="12" font-size="11" fill="var(--muted)">P(nothing has arrived by time t)</text>'
      + poly(epts, '--red', 1.6, '5 3') + poly(pts, '--cyan', 1.8, '')
      + '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="10" y1="28" x2="10" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 12) + '" font-size="9" fill="var(--muted)">0</text>'
      + '<text x="510" y="' + (base + 12) + '" text-anchor="end" font-size="9" fill="var(--muted)">'
      + t + ' s</text>'
      + '<text x="14" y="34" font-size="9" fill="var(--muted)">1</text>';
    if (s > 0 && s + t <= 12) {
      var xs = 10 + Math.min(s, t) * W0;
      sv += '<line x1="' + xs + '" y1="28" x2="' + xs + '" y2="' + base
        + '" stroke="var(--amber)" stroke-width="1" stroke-dasharray="2 3" />'
        + '<text x="' + (xs + 3) + '" y="40" font-size="9" fill="var(--amber)">already quiet '
        + s + ' s &mdash; the curve from here has the same shape</text>';
    }
    sv += '<text x="10" y="' + (base + 28) + '" font-size="10" fill="var(--muted)">'
      + 'solid: the exact geometric at &Delta; = ' + Rtext(R(1n, BigInt(inv)))
      + '. dashed: e<sup>&minus;&lambda;t</sup>, which is what it becomes.</text>'
      + '<text x="10" y="' + (base + 42) + '" font-size="10" fill="var(--muted)">'
      + 'the two curves are not the same curve; the gap at t = ' + t + ' is ' + Rfixed(gap, 6) + '</text>';
    plot.innerHTML = sv;

    var same = cond && Requ(cond, geo);
    status.innerHTML = 'Waiting ' + t + ' seconds with nothing arriving has probability <strong>'
      + Rfixed(geo, 6) + '</strong> exactly, as the fraction (1 &minus; ' + Rtext(Rmul(lam, R(1n, BigInt(inv))))
      + ')<sup>' + commas(t * inv) + '</sup>. The exponential answer is <strong>' + ex.toFixed(6)
      + '</strong>, <span class="tone-red">rounded</span> &mdash; e<sup>&minus;x</sup> is computed by '
      + 'its alternating series here, because it is not a fraction. They differ by ' + Rfixed(gap, 6)
      + ' at &Delta; = ' + Rtext(R(1n, BigInt(inv))) + ', and the table shows that difference shrinking '
      + 'with the slot. '
      + (cond
          ? 'Now the part that does not shrink: having already been quiet for ' + s
            + ' s, the chance of another ' + t + ' quiet seconds is <strong>' + Rfixed(cond, 6)
            + '</strong> &mdash; ' + (same ? 'exactly the same number' : 'the same number')
            + ' as from a standing start. Nothing is "due". The wait has no memory at any slot size, '
            + 'which is why memorylessness survives the limit rather than appearing in it.'
          : '');
  }

  [lamS, tS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  dSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Memoryless waiting",
        subtitle="The geometric tail exactly, and the exponential it becomes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the rate and the slot"),
        panel_intro=cfg.get(
            "panel_intro",
            "The exact column is a fraction with an integer exponent. The rounded column is "
            "e<sup>&minus;&lambda;t</sup> by series, and the page says so wherever it prints it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - poisson
# ---------------------------------------------------------------------------

# How finely the window is chopped. The list stops at 20 for a reason worth
# stating rather than hiding: the binomial column here is EXACT, and (19/20)^480
# is a 625-digit fraction whose greatest common divisor costs real time to take.
# Chopping a hundred times finer is a two-second redraw, so the page offers the
# three steps that show the limit and says why there is not a fourth.
_OPPORTUNITIES = [("2", "n = 2m opportunities, each with probability 1/2"),
                  ("5", "n = 5m, each 1/5"),
                  ("20", "n = 20m, each 1/20")]

_TARGETS = [("100", "1 in 100"), ("1000", "1 in 1000"), ("10000", "1 in 10 000")]


def _poisson(cfg):
    mean = int(cfg.get("mean", 10))
    if mean > _EXP_SAFE_X:
        raise ValueError(
            "queue mode 'poisson': a mean of %d is past %d, where the core's series for "
            "e^-m has lost its significant digits; the binomial column stays exact but the "
            "Poisson column it is compared against would not be" % (mean, _EXP_SAFE_X)
        )
    thresh = int(cfg.get("threshold", 15))
    mult = int(cfg.get("multiplier", 20))
    target = int(cfg.get("target", 100))

    markup = (
        _toolbar(
            "Poisson arrivals and bursts",
            "the count in a window is the binomial's limit, and its variance is its mean",
            [("cyan", "binomial, exact"), ("red", "Poisson, rounded"), ("amber", "above the threshold")],
        )
        + _stage(
            _svg("poPlot", "0 0 520 190",
                 "The exact binomial distribution of the count in a window, with its Poisson limit over it.")
        )
        + _table("poTable")
        + _banner("poStatus")
    )
    controls = (
        _range("poM", "Mean count in the window, m", 1, 12, mean)
        + _range("poC", "Capacity C &mdash; how many the window can take", 0, 40, thresh)
        + _select("poN", "How the window is chopped up", _OPPORTUNITIES, str(mult))
        + _select("poTarget", "Burst target to size for", _TARGETS, str(target))
        + _kpis(
            [
                ("P(count &gt; C), binomial &mdash; exact", "poBin"),
                ("P(count &gt; C), Poisson &mdash; rounded", "poPoi"),
                ("Variance (binomial) vs mean", "poVar"),
                ("C that meets the target", "poNeed"),
            ]
        )
        + _hint(
            "poHint",
            "\"1000 per second\" does not mean 1000 arrive each second. With a Poisson count the "
            "standard deviation is &radic;m, so a mean of 1000 is 1000 &plusmn; 32 and a window "
            "sized at exactly the mean is over capacity about half the time. Two limits are worth "
            "knowing: the chopping stops at 20m because the bars are <em>exact</em> fractions and at "
            "100m the denominators run to two thousand digits; and the mean stops at 12 because the "
            "<em>rounded</em> column cannot go further &mdash; e<sup>&minus;m</sup> is summed by an "
            "alternating series that has lost every significant digit by m = 19. The exact column "
            "would have been happy to continue.",
        )
    )

    script = _CORE_JS + r"""
  var mS = document.getElementById('poM'), cS = document.getElementById('poC');
  var nSel = document.getElementById('poN'), tSel = document.getElementById('poTarget');
  var plot = document.getElementById('poPlot'), table = document.getElementById('poTable');
  var status = document.getElementById('poStatus');

  function redraw() {
    var m = +mS.value, C = +cS.value, mult = +nSel.value, tden = +tSel.value;
    var n = m * mult, target = 1 / tden;
    document.getElementById('poMOut').textContent = String(m);
    document.getElementById('poCOut').textContent = String(C);

    /* ONE binomial row per redraw, reused by the bars, both tails and the
       table. Built twice it doubles the redraw, and at n = 480 that is the
       difference between a slider that follows the mouse and one that does not.
       Declared here because everything below reads it. */
    var hi = Math.min(n, 3 * m + 8);
    var row = binomRow(n, m, Math.max(hi, Math.min(C, n), m));
    var binTail = tailFromRow(row, Math.min(C, n));
    var poiTail = poissonTailApprox(m, C);
    var variance = binomVar(n, m);
    var need = headroomForApprox(m, target, 400);

    document.getElementById('poBin').textContent = Rfixed(binTail, 6);
    document.getElementById('poPoi').textContent = poiTail.toFixed(6) + ' (rounded)';
    document.getElementById('poVar').textContent = Rtext(variance) + ' vs ' + m;
    document.getElementById('poNeed').textContent = need < 0 ? '—' : String(need);

    var k, bars = [], top = 0;
    for (k = 0; k <= hi; k += 1) {
      var pv = poissonPmfApprox(m, k);
      var bv = parseFloat(Rfixed(row[k], 8));
      bars.push([k, bv, pv]);
      if (bv > top) top = bv;
      if (pv > top) top = pv;
    }
    var W0 = 500 / (hi + 1), base = 136;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">the count in one window: '
      + '<tspan fill="var(--cyan)">' + commas(n) + ' chances at ' + Rtext(R(1n, BigInt(mult)))
      + ' each, exactly</tspan>, and <tspan fill="var(--red)">its Poisson limit, rounded</tspan></text>';
    for (k = 0; k < bars.length; k += 1) {
      var h = (bars[k][1] / top) * 104;
      s += '<rect x="' + (10 + k * W0) + '" y="' + (base - h) + '" width="' + Math.max(1, W0 - 1.4)
        + '" height="' + h + '" fill="var(' + (bars[k][0] > C ? '--amber' : '--cyan') + ')" opacity="0.72" />';
    }
    s += '<polyline fill="none" stroke="var(--red)" stroke-width="1.6" stroke-dasharray="4 3" points="'
      + bars.map(function (b, ix) {
          return (10 + ix * W0 + W0 / 2).toFixed(1) + ',' + (base - (b[2] / top) * 104).toFixed(1);
        }).join(' ') + '" />';
    var xc = 10 + (C + 1) * W0;
    if (C <= hi) {
      s += '<line x1="' + xc + '" y1="24" x2="' + xc + '" y2="' + base
        + '" stroke="var(--amber)" stroke-width="1.4" />'
        + '<text x="' + (xc + 4) + '" y="36" font-size="10" fill="var(--amber)">C = ' + C
        + ' &mdash; everything right of here is a burst you cannot serve</text>';
    }
    s += '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 13) + '" font-size="9" fill="var(--muted)">0</text>'
      + '<text x="' + (10 + m * W0) + '" y="' + (base + 13) + '" text-anchor="middle" font-size="9" '
      + 'fill="var(--muted)">m = ' + m + '</text>'
      + '<text x="510" y="' + (base + 13) + '" text-anchor="end" font-size="9" fill="var(--muted)">'
      + hi + '</text>'
      + '<text x="10" y="' + (base + 30) + '" font-size="10" fill="var(--muted)">the bars are exact '
      + 'fractions; the dashed line is e<sup>&minus;m</sup>m<sup>k</sup>/k!, which is not</text>'
      + '<text x="10" y="' + (base + 44) + '" font-size="10" fill="var(--muted)">chop the window '
      + 'finer and the bars walk onto the line &mdash; that limit is what "Poisson" means</text>';
    plot.innerHTML = s;

    var sigma = sqrtApprox(R(BigInt(m), 1n), 1e-15);
    table.innerHTML = '<thead><tr><th>quantity</th><th>binomial, exact</th><th>Poisson, rounded</th></tr></thead><tbody>'
      + '<tr><td>mean</td><td>' + m + '</td><td>' + m + '</td></tr>'
      + '<tr><td>variance</td><td>' + Rtext(variance) + ' = m(1 &minus; m/n)</td><td>' + m + '</td></tr>'
      + '<tr><td>P(count = m)</td><td>' + Rfixed(row[m], 6) + '</td><td>'
      + poissonPmfApprox(m, m).toFixed(6) + '</td></tr>'
      + '<tr><td class="tone-amber">P(count &gt; C)</td><td>' + Rfixed(binTail, 6) + '</td><td>'
      + poiTail.toFixed(6) + '</td></tr>'
      + '<tr><td>P(count &gt; m)</td><td>' + Rfixed(tailFromRow(row, m), 6) + '</td><td>'
      + poissonTailApprox(m, m).toFixed(6) + '</td></tr>'
      + '<tr><td>&radic;m, the spread</td><td colspan="2" class="tone-red">' + sigma.toFixed(4)
      + ' &mdash; a square root, so this one rounds too</td></tr>'
      + '<tr><td>method</td><td class="tone-cyan">exact fractions over BigInt</td>'
      + '<td class="tone-red">e<sup>&minus;m</sup> by an alternating series, good to about seven '
      + 'figures here and to none past m = 19 &mdash; which is why the mean stops at 12</td></tr>'
      + '</tbody>';

    status.innerHTML = 'A window whose mean is <strong>' + m + '</strong> has variance <strong>'
      + Rtext(variance) + '</strong> and spread about <strong>' + sigma.toFixed(2)
      + '</strong>, so "' + m + ' per window" means ' + m + ' &plusmn; ' + sigma.toFixed(0)
      + ', not ' + m + '. Sized at C = ' + C + ' the window overflows <strong>'
      + Rpct(binTail, 3) + '</strong> of the time by the exact binomial, and '
      + (poiTail * 100).toFixed(3) + '% by the Poisson limit &mdash; '
      + '<span class="tone-red">the second figure is rounded</span>, because e<sup>&minus;m</sup> is '
      + 'not a fraction and the page will not pretend it is. '
      + (need < 0 ? 'No capacity under 400 meets the chosen target.'
         : 'To keep the overflow under 1 in ' + commas(tden) + ' you need <strong>C = ' + need
           + '</strong> &mdash; ' + Rfixed(Rdiv(R(BigInt(need), 1n), R(BigInt(m), 1n)), 2)
           + '&times; the mean, which is the headroom the burstiness costs.');
  }

  [mS, cS].forEach(function (el) { el.addEventListener('input', redraw); });
  [nSel, tSel].forEach(function (el) { el.addEventListener('change', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Poisson arrivals and bursts",
        subtitle="The count in a window, and the headroom its spread costs",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the window"),
        panel_intro=cfg.get(
            "panel_intro",
            "The binomial bars are exact fractions computed from the number of opportunities you "
            "choose. The Poisson line is its limit and is rounded, which the page states wherever "
            "it prints one.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - mm1
# ---------------------------------------------------------------------------


def _mm1(cfg):
    lam20 = int(cfg.get("lam20", 16))
    mu20 = int(cfg.get("mu20", 20))
    n_show = int(cfg.get("n", 2))
    k_show = int(cfg.get("k", 3))

    markup = (
        _toolbar(
            "The M/M/1 queue",
            "&pi;<sub>n</sub> = (1 &minus; &rho;)&rho;<sup>n</sup>, and everything that follows from it",
            [("cyan", "&pi;<sub>n</sub>"), ("green", "in service"), ("amber", "waiting"),
             ("purple", "the slotted chain")],
        )
        + _stage(
            _svg("mmPlot", "0 0 520 180",
                 "The stationary distribution of the number in system, decaying geometrically.")
        )
        + _table("mmTable")
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="mmConv"></table></div>\n'
        + _banner("mmStatus")
    )
    controls = (
        _range("mmLam", "&lambda; &mdash; arrivals per unit time (twentieths)", 1, 19, lam20)
        + _range("mmMu", "&mu; &mdash; service rate (twentieths)", 2, 20, mu20)
        + _range("mmN", "n &mdash; which &pi;<sub>n</sub> to read off", 0, 12, n_show)
        + _range("mmK", "k &mdash; for the tail P(N &gt; k)", 0, 12, k_show)
        + _kpis(
            [
                ("&rho; = &lambda;/&mu;", "mmRho"),
                ("&pi;<sub>0</sub> = 1 &minus; &rho;", "mmP0"),
                ("L = &rho;/(1 &minus; &rho;)", "mmL"),
                ("L<sub>q</sub> = &rho;&sup2;/(1 &minus; &rho;)", "mmLq"),
                ("W = L/&lambda;", "mmW"),
                ("P(N &gt; k) = &rho;<sup>k+1</sup>", "mmTail"),
            ]
        )
        + _hint(
            "mmHint",
            "L counts everyone, including the one being served; L<sub>q</sub> counts only those "
            "waiting, and L &minus; L<sub>q</sub> = &rho; is the one in service. The second table "
            "is the shrinking-slot check: a discrete-time chain at &Delta;, &Delta;/10 and "
            "&Delta;/100, walking toward this formula rather than agreeing with it.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('mmLam'), muS = document.getElementById('mmMu');
  var nS = document.getElementById('mmN'), kS = document.getElementById('mmK');
  var plot = document.getElementById('mmPlot'), table = document.getElementById('mmTable');
  var conv = document.getElementById('mmConv'), status = document.getElementById('mmStatus');

  function redraw() {
    var lv = +lamS.value, mv = +muS.value;
    if (lv >= mv) { mv = Math.min(20, lv + 1); muS.value = mv; }
    var lam = R(BigInt(lv), 20n), mu = R(BigInt(mv), 20n);
    var n = +nS.value, k = +kS.value;
    document.getElementById('mmLamOut').textContent = Rtext(lam);
    document.getElementById('mmMuOut').textContent = Rtext(mu);
    document.getElementById('mmNOut').textContent = String(n);
    document.getElementById('mmKOut').textContent = String(k);

    var q = mm1(lam, mu), rho = q.rho, one = R(1n, 1n);
    var p0 = q.p0, pn = Rmul(p0, Rpow(rho, n)), tail = Rpow(rho, k + 1);
    var S = Rinv(mu);

    document.getElementById('mmRho').textContent = Rtext(rho);
    document.getElementById('mmP0').textContent = Rtext(p0);
    document.getElementById('mmL').textContent = Rshort(q.L, 4);
    document.getElementById('mmLq').textContent = Rshort(q.Lq, 4);
    document.getElementById('mmW').textContent = Rshort(q.W, 4) + ' (= ' + Rshort(Rdiv(q.W, S), 3) + ' S)';
    document.getElementById('mmTail').textContent = Rshort(tail, 6);

    var rows = '<thead><tr><th>quantity</th><th>from the balance equations</th><th>exactly</th></tr></thead><tbody>'
      + '<tr><td>&pi;<sub>0</sub></td><td>1 &minus; &rho;</td><td>' + Rtext(p0) + '</td></tr>'
      + '<tr><td class="tone-cyan">&pi;<sub>' + n + '</sub></td><td>(1 &minus; &rho;)&rho;<sup>' + n
      + '</sup></td><td>' + Rshort(pn, 6) + '</td></tr>'
      + '<tr><td>L</td><td>&rho;/(1 &minus; &rho;) &mdash; everyone, in service or waiting</td><td>'
      + Rshort(q.L, 4) + '</td></tr>'
      + '<tr><td class="tone-amber">L<sub>q</sub></td><td>&rho;&sup2;/(1 &minus; &rho;) &mdash; only those waiting</td><td>'
      + Rshort(q.Lq, 4) + '</td></tr>'
      + '<tr><td class="tone-green">L &minus; L<sub>q</sub></td><td>the one in service, which is &rho;</td><td>'
      + Rtext(Rsub(q.L, q.Lq)) + ' = &rho;</td></tr>'
      + '<tr><td>S = 1/&mu;</td><td>mean service time</td><td>' + Rtext(S) + '</td></tr>'
      + '<tr><td>W</td><td>L/&lambda; = S/(1 &minus; &rho;)</td><td>' + Rshort(q.W, 4) + '</td></tr>'
      + '<tr><td>W<sub>q</sub></td><td>L<sub>q</sub>/&lambda; = W &minus; S</td><td>'
      + Rshort(q.Wq, 4) + '</td></tr>'
      + '<tr><td>P(N &gt; ' + k + ')</td><td>&rho;<sup>' + (k + 1) + '</sup></td><td>'
      + Rshort(tail, 6) + '</td></tr></tbody>';
    table.innerHTML = rows;

    /* The shrinking-slot check. NOT a claim of agreement -- a sequence. */
    var crows = convergenceRows(lam, mu, 3), i;
    var head = '<thead><tr><th>slot &Delta;</th><th>p = &lambda;&Delta;</th><th>q = &mu;&Delta;</th>'
      + '<th>exact Geo/Geo/1 L</th><th>&rho;/(1 &minus; &rho;)</th><th>still short by</th></tr></thead><tbody>';
    for (i = 0; i < crows.length; i += 1) {
      var r = crows[i];
      head += '<tr><td class="tone-purple">' + Rtext(r.delta) + '</td><td>' + Rtext(r.p) + '</td><td>'
        + Rtext(r.q) + '</td><td>' + (r.L ? Rshort(r.L, 5) : '—') + '</td><td>' + Rshort(q.L, 5)
        + '</td><td class="tone-red">' + (r.gap ? Rshort(r.gap, 5) : '—') + '</td></tr>';
    }
    head += '<tr><td class="tone-muted">&Delta; &rarr; 0</td><td>0</td><td>0</td><td>'
      + Rshort(q.L, 5) + '</td><td>' + Rshort(q.L, 5) + '</td><td>0</td></tr></tbody>';
    conv.innerHTML = head;

    var top = parseFloat(Rfixed(p0, 6)), base = 132, W0 = 500 / 13, j;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">&pi;<sub>n</sub>, the chance of '
      + 'finding exactly n in the system &mdash; a geometric decay with ratio &rho; = ' + Rtext(rho) + '</text>';
    for (j = 0; j <= 12; j += 1) {
      var v = parseFloat(Rfixed(Rmul(p0, Rpow(rho, j)), 8));
      var h = top > 0 ? (v / top) * 96 : 0;
      s += '<rect x="' + (10 + j * W0) + '" y="' + (base - h) + '" width="' + (W0 - 6)
        + '" height="' + Math.max(0.6, h) + '" fill="var(' + (j === n ? '--amber' : '--cyan')
        + ')" opacity="' + (j === n ? '0.95' : '0.6') + '" />'
        + '<text x="' + (10 + j * W0 + (W0 - 6) / 2) + '" y="' + (base + 12) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">' + j + '</text>';
    }
    s += '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 28) + '" font-size="10" fill="var(--amber)">&pi;<sub>' + n + '</sub> = '
      + Rshort(pn, 6) + '</text>'
      + '<text x="10" y="' + (base + 42) + '" font-size="10" fill="var(--muted)">'
      + 'every bar is (1 &minus; &rho;)&rho;<sup>n</sup>, computed from the &lambda; and &mu; you set</text>';
    plot.innerHTML = s;

    var first = crows.length ? crows[0] : null;
    status.innerHTML = 'At &rho; = <strong>' + Rtext(rho) + '</strong> the system is empty '
      + Rpct(p0, 2) + ' of the time and holds <strong>' + Rshort(q.L, 4)
      + '</strong> on average &mdash; of which <strong>' + Rshort(q.Lq, 4) + '</strong> are waiting '
      + 'and exactly &rho; = ' + Rtext(rho) + ' is in service. Every figure above is an exact '
      + 'fraction from the cut balance &lambda;&pi;<sub>n</sub> = &mu;&pi;<sub>n+1</sub>. '
      + '<strong>This formula is not checked against a simulation.</strong> A slotted simulation is a '
      + '<span class="tone-purple">Geo/Geo/1</span> chain, a different model: at &Delta; = '
      + (first ? Rtext(first.delta) : '1') + ' its exact mean is '
      + (first && first.L ? Rshort(first.L, 4) : '—') + ', not ' + Rshort(q.L, 4)
      + '. The second table is the honest version of the check &mdash; the discrete chain solved '
      + 'exactly at three slot sizes, each a tenth of the last, with the shortfall falling by a '
      + 'factor of ten each time because it is &rho;p/(1 &minus; &rho;) and p = &lambda;&Delta;. '
      + 'They agree in the limit and nowhere else. The chain itself is derived in Operations '
      + 'Research, <span class="tt">queues-in-discrete-time</span>; the closed forms above are '
      + 'this course\'s.';
  }

  [lamS, muS, nS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The M/M/1 queue",
        subtitle="Flow balance across a cut, and the shrinking slot that reaches it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the two rates"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every figure is an exact fraction in &lambda; and &mu;. The second table solves the "
            "discrete-time chain exactly at three slot sizes, so the agreement with this formula is "
            "shown as a limit rather than claimed as a check.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - knee
# ---------------------------------------------------------------------------


def _knee(cfg):
    rho100 = int(cfg.get("rho100", 90))
    svc = int(cfg.get("service_ms", 10))
    factor = int(cfg.get("factor", 10))

    markup = (
        _toolbar(
            "The knee",
            "W/S = 1/(1 &minus; &rho;): a hyperbola, and the asymptote is the whole content",
            [("cyan", "W/S"), ("red", "the asymptote at &rho; = 1"), ("amber", "where you are")],
        )
        + _stage(
            _svg("knPlot", "0 0 520 200",
                 "Response time against utilisation, drawn as a hyperbola with a vertical asymptote at one.")
        )
        + _table("knTable")
        + _banner("knStatus")
    )
    controls = (
        _range("knRho", "&rho; &mdash; utilisation (hundredths)", 1, 99, rho100)
        + _range("knS", "S &mdash; mean service time (ms)", 1, 50, svc)
        + _range("knK", "k &mdash; how many service times you will tolerate", 2, 100, factor)
        + _kpis(
            [
                ("W/S = 1/(1 &minus; &rho;)", "knFactor"),
                ("W at this S", "knW"),
                ("&rho; at which W = kS", "knRhoK"),
                ("Headroom left there", "knHead"),
            ]
        )
        + _hint(
            "knHint",
            "Response time does not grow with load; it grows with the <em>reciprocal of the "
            "headroom</em>. Going from 50% to 90% multiplies the wait by five. Going from 90% to "
            "99% multiplies it by ten more. The last tenth of a machine costs more than the first "
            "nine, and no amount of tuning moves the asymptote.",
        )
    )

    script = _CORE_JS + r"""
  var rhoS = document.getElementById('knRho'), sS = document.getElementById('knS');
  var kS = document.getElementById('knK');
  var plot = document.getElementById('knPlot'), table = document.getElementById('knTable');
  var status = document.getElementById('knStatus');

  function redraw() {
    var rv = +rhoS.value, sv = +sS.value, kv = +kS.value;
    var rho = R(BigInt(rv), 100n), S = R(BigInt(sv), 1n);
    var f = kneeFactor(rho), W = Rmul(f, S);
    var rhoK = rhoForFactor(kv), head = Rsub(R(1n, 1n), rhoK);

    document.getElementById('knRhoOut').textContent = Rtext(rho) + ' (' + rv + '%)';
    document.getElementById('knSOut').textContent = sv + ' ms';
    document.getElementById('knKOut').innerHTML = kv + '&times; S';
    document.getElementById('knFactor').innerHTML = Rtext(f) + '&times;';
    document.getElementById('knW').textContent = Rshort(W, 3) + ' ms';
    document.getElementById('knRhoK').textContent = Rtext(rhoK) + ' = ' + Rpct(rhoK, 1);
    document.getElementById('knHead').textContent = Rtext(head) + ' = ' + Rpct(head, 1);

    var marks = [50, 80, 90, 95, 99], i;
    var rows = '<thead><tr><th>&rho;</th><th>headroom 1 &minus; &rho;</th><th>W/S</th>'
      + '<th>W at S = ' + sv + ' ms</th><th>vs the row above</th></tr></thead><tbody>';
    var prev = null;
    for (i = 0; i < marks.length; i += 1) {
      var r = R(BigInt(marks[i]), 100n), ff = kneeFactor(r);
      rows += '<tr><td class="' + (marks[i] === rv ? 'tone-amber' : 'tone-muted') + '">'
        + marks[i] + '%</td><td>' + Rtext(Rsub(R(1n, 1n), r)) + '</td><td>' + Rtext(ff)
        + '</td><td>' + Rshort(Rmul(ff, S), 2) + ' ms</td><td>'
        + (prev ? Rshort(Rdiv(ff, prev), 3) + '&times;' : '&mdash;') + '</td></tr>';
      prev = ff;
    }
    rows += '<tr><td class="tone-red">100%</td><td>0</td><td>&infin;</td><td>&infin;</td>'
      + '<td>the asymptote</td></tr></tbody>';
    table.innerHTML = rows;

    var cap = 20, base = 160, pts = [], j;
    for (j = 0; j <= 194; j += 1) {
      var x = j / 200;
      var yv = 1 / (1 - x);
      if (yv > cap) yv = cap;
      pts.push([10 + x * 470, base - (yv / cap) * 136]);
    }
    var xr = 10 + (rv / 100) * 470;
    var fv = Math.min(cap, parseFloat(Rfixed(f, 4)));
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">W/S against &rho;, capped at '
      + cap + '&times; so the shape is visible</text>'
      + '<polyline fill="none" stroke="var(--cyan)" stroke-width="1.8" points="'
      + pts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />'
      + '<line x1="480" y1="24" x2="480" y2="' + base + '" stroke="var(--red)" stroke-width="1.4" stroke-dasharray="4 3" />'
      + '<text x="476" y="36" text-anchor="end" font-size="10" fill="var(--red)">&rho; = 1</text>'
      + '<circle cx="' + xr + '" cy="' + (base - (fv / cap) * 136) + '" r="4" fill="var(--amber)" />'
      + '<text x="' + Math.min(430, xr + 8) + '" y="' + Math.max(30, base - (fv / cap) * 136 - 6)
      + '" font-size="10" fill="var(--amber)" font-weight="700">&rho; = ' + Rtext(rho)
      + ', W = ' + Rtext(f) + 'S</text>'
      + '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 13) + '" font-size="9" fill="var(--muted)">0</text>'
      + '<text x="' + (10 + 0.5 * 470) + '" y="' + (base + 13) + '" text-anchor="middle" font-size="9" '
      + 'fill="var(--muted)">50%</text>'
      + '<text x="' + (10 + 0.9 * 470) + '" y="' + (base + 13) + '" text-anchor="middle" font-size="9" '
      + 'fill="var(--muted)">90%</text>'
      + '<text x="10" y="' + (base + 30) + '" font-size="10" fill="var(--muted)">'
      + 'the curve is not steep because the load is high; it is steep because the headroom is small, '
      + 'and headroom is what the denominator is</text>';
    plot.innerHTML = s;

    var at50 = kneeFactor(R(1n, 2n)), at90 = kneeFactor(R(9n, 10n)), at99 = kneeFactor(R(99n, 100n));
    status.innerHTML = 'At &rho; = <strong>' + Rtext(rho) + '</strong> a request spends <strong>'
      + Rtext(f) + '&times;</strong> its own service time in the system &mdash; ' + Rshort(W, 3)
      + ' ms when S is ' + sv + ' ms &mdash; and ' + Rshort(Rsub(W, S), 3)
      + ' ms of that is spent waiting for other people. Read the row above as a shape, not a table: '
      + '50% &rarr; 90% multiplies the wait by ' + Rtext(Rdiv(at90, at50)) + ', and 90% &rarr; 99% by '
      + Rtext(Rdiv(at99, at90)) + ' more. To hold W under ' + kv + ' service times you must stay at or '
      + 'below <strong>&rho; = ' + Rtext(rhoK) + '</strong> &mdash; that is exactly (k &minus; 1)/k, '
      + 'so the headroom you must keep is 1/k = ' + Rtext(head) + '. Every claim here is the one '
      + 'hyperbola W = S/(1 &minus; &rho;); the asymptote at &rho; = 1 is not a large number, it is '
      + 'no number at all.';
  }

  [rhoS, sS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The knee",
        subtitle="Response time against utilisation, and the asymptote you cannot tune away",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Drag the utilisation"),
        panel_intro=cfg.get(
            "panel_intro",
            "W/S = 1/(1 &minus; &rho;) is evaluated exactly at the &rho; you choose, and inverted "
            "exactly for the utilisation that meets a target of k service times.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - variability
# ---------------------------------------------------------------------------


def _variability(cfg):
    p_num = int(cfg.get("p20", 8))
    q_num = int(cfg.get("q20", 10))
    ca_half = int(cfg.get("ca2_halves", 2))
    cs_half = int(cfg.get("cs2_halves", 0))
    seed = int(cfg.get("seed", 7))

    markup = (
        _toolbar(
            "Kingman's approximation",
            "exact arithmetic on an approximate model, held against the exact chain and a run",
            [("cyan", "Kingman"), ("purple", "exact Geo/Geo/1"), ("green", "simulated"),
             ("red", "the disagreement")],
        )
        + _stage(
            _svg("vaPlot", "0 0 520 180",
                 "Four estimates of the mean wait drawn as bars of different lengths.")
        )
        + _table("vaTable")
        + _banner("vaStatus")
    )
    controls = (
        _range("vaP", "p &mdash; arrival probability per slot (twentieths)", 1, 19, p_num)
        + _range("vaQ", "q &mdash; service completion probability per slot (twentieths)", 2, 20, q_num)
        + _range("vaCa", "c<sub>a</sub>&sup2; for the formula (halves)", 0, 4, ca_half)
        + _range("vaCs", "c<sub>s</sub>&sup2; for the formula (halves)", 0, 4, cs_half)
        + _range("vaSeed", "Seed", 1, 40, seed)
        + _kpis(
            [
                ("Kingman at your c&sup2;", "vaKing"),
                ("Kingman at the chain's own c&sup2;", "vaKingTrue"),
                ("Exact Geo/Geo/1 W<sub>q</sub>", "vaExact"),
                ("Simulated W<sub>q</sub>", "vaSim"),
            ]
        )
        + _hint(
            "vaHint",
            "W<sub>q</sub> &asymp; (&rho;/(1 &minus; &rho;)) &times; "
            "((c<sub>a</sub>&sup2; + c<sub>s</sub>&sup2;)/2) &times; S. The arithmetic is exact for "
            "rational c&sup2; and S. The <em>model</em> is the approximation, and the page shows "
            "that rather than saying it: the chain's own coefficients are 1 &minus; p and "
            "1 &minus; q, and even at those the formula misses the exact answer.",
        )
    )

    script = _CORE_JS + r"""
  var pS = document.getElementById('vaP'), qS = document.getElementById('vaQ');
  var caS = document.getElementById('vaCa'), csS = document.getElementById('vaCs');
  var seedS = document.getElementById('vaSeed');
  var plot = document.getElementById('vaPlot'), table = document.getElementById('vaTable');
  var status = document.getElementById('vaStatus');
  var SLOTS = 6000;

  function redraw() {
    var pn = +pS.value, qn = +qS.value;
    if (pn >= qn) { qn = Math.min(20, pn + 1); qS.value = qn; }
    var p = R(BigInt(pn), 20n), q = R(BigInt(qn), 20n), rho = Rdiv(p, q);
    var ca2 = R(BigInt(+caS.value), 2n), cs2 = R(BigInt(+csS.value), 2n);
    var seed = +seedS.value, S = Rinv(q);

    document.getElementById('vaPOut').textContent = Rtext(p);
    document.getElementById('vaQOut').textContent = Rtext(q) + ' (S = ' + Rtext(S) + ' slots)';
    document.getElementById('vaCaOut').textContent = Rtext(ca2);
    document.getElementById('vaCsOut').textContent = Rtext(cs2);
    document.getElementById('vaSeedOut').textContent = String(seed);

    var trueCa = slottedCa2(p), trueCs = slottedCs2(q);
    var kYours = kingmanWq(rho, ca2, cs2, S);
    var kTrue = kingmanWq(rho, trueCa, trueCs, S);
    var kMM1 = kingmanWq(rho, R(1n, 1n), R(1n, 1n), S);
    var kDet = kingmanWq(rho, trueCa, R(0n, 1n), S);
    var exactLq = geoGeo1Lq(p, q);
    var exactWq = exactLq ? Rdiv(exactLq, p) : null;

    var warm = Math.floor(SLOTS / 10);
    var run = slottedRun(p, q, seed, SLOTS);
    var simWq = Rdiv(runMean(queueOf(run), warm), p);
    var D = Number(Rceil(S));
    var det = slottedDetRun(p, D, seed, SLOTS);
    var simDetWq = Rdiv(runMean(queueOf(det), warm), R(BigInt(pn), 20n));

    document.getElementById('vaKing').textContent = kYours ? Rshort(kYours, 3) + ' slots' : '—';
    document.getElementById('vaKingTrue').textContent = kTrue ? Rshort(kTrue, 3) + ' slots' : '—';
    document.getElementById('vaExact').textContent = exactWq ? Rshort(exactWq, 3) + ' slots' : '—';
    document.getElementById('vaSim').textContent = Rfixed(simWq, 3) + ' slots';

    var rows = [
      ['tone-cyan', 'Kingman, c&sup2; = ' + Rtext(ca2) + ' and ' + Rtext(cs2),
       'the coefficients you set', kYours],
      ['tone-muted', 'Kingman, c&sup2; = 1 and 1',
       'the M/M/1 answer &mdash; every c&sup2; assumed exponential', kMM1],
      ['tone-cyan', 'Kingman, c&sup2; = ' + Rtext(trueCa) + ' and ' + Rtext(trueCs),
       'this chain\'s ACTUAL coefficients, 1 &minus; p and 1 &minus; q', kTrue],
      ['tone-amber', 'Kingman, c<sub>s</sub>&sup2; = 0',
       'the same arrivals, served in a fixed time', kDet],
      ['tone-purple', 'exact Geo/Geo/1', 'no approximation anywhere in it', exactWq]
    ];
    var body = '<thead><tr><th>row</th><th>what it assumes</th><th>W<sub>q</sub> (slots)</th>'
      + '<th>&divide; exact</th></tr></thead><tbody>', i;
    for (i = 0; i < rows.length; i += 1) {
      var v = rows[i][3];
      body += '<tr><td class="' + rows[i][0] + '">' + rows[i][1] + '</td><td>' + rows[i][2]
        + '</td><td>' + (v ? Rshort(v, 3) : '—') + '</td><td>'
        + (v && exactWq && !Rzero(exactWq) ? Rfixed(Rdiv(v, exactWq), 3) + '&times;' : '&mdash;')
        + '</td></tr>';
    }
    body += '<tr><td class="tone-green">simulated, geometric service</td><td>' + commas(SLOTS)
      + ' slots, seed ' + seed + ', first ' + commas(warm) + ' discarded</td><td>'
      + Rfixed(simWq, 3) + '</td><td>'
      + (exactWq && !Rzero(exactWq) ? Rfixed(Rdiv(simWq, exactWq), 3) + '&times;' : '&mdash;') + '</td></tr>'
      + '<tr><td class="tone-green">simulated, service fixed at ' + D + ' slots</td>'
      + '<td>the same arrivals, no service variance at all &mdash; service must be a whole '
      + 'number of slots, so this arm runs at &rho; = pD = ' + Rtext(Rmul(p, R(BigInt(D), 1n)))
      + '</td><td>' + Rfixed(simDetWq, 3) + '</td><td>&mdash;</td></tr></tbody>';
    table.innerHTML = body;

    var bars = [
      ['Kingman, c&sup2; = 1, 1', kMM1, '--muted'],
      ['Kingman, your c&sup2;', kYours, '--cyan'],
      ['Kingman, true c&sup2;', kTrue, '--cyan'],
      ['exact Geo/Geo/1', exactWq, '--purple'],
      ['simulated', simWq, '--green']
    ];
    var top = 0, j;
    for (j = 0; j < bars.length; j += 1) {
      if (!bars[j][1]) continue;
      var w = parseFloat(Rfixed(bars[j][1], 4));
      if (w > top) top = w;
    }
    var unit = top > 0 ? 300 / top : 1;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">mean wait before service, in slots '
      + '&mdash; five ways of answering the same question</text>';
    for (j = 0; j < bars.length; j += 1) {
      var y = 26 + j * 28, val = bars[j][1];
      s += '<text x="0" y="' + (y + 11) + '" font-size="10" fill="var(--muted)">' + bars[j][0] + '</text>';
      if (!val) continue;
      var px = Math.max(1, parseFloat(Rfixed(val, 4)) * unit);
      s += '<rect x="170" y="' + y + '" width="' + px + '" height="15" rx="2" fill="var(' + bars[j][2]
        + ')" opacity="0.8" />'
        + '<text x="' + (175 + px) + '" y="' + (y + 12) + '" font-size="10" fill="var(' + bars[j][2]
        + ')" font-weight="700">' + Rfixed(val, 3) + '</text>';
    }
    s += '<line x1="0" y1="168" x2="520" y2="168" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="' + (26 + bars.length * 28 + 8) + '" font-size="10" fill="var(--red)">'
      + 'the bars are not the same length, and that is the lesson: the formula is an approximation '
      + 'to a model, not a wrong arithmetic</text>';
    plot.innerHTML = s;

    var halves = Rcmp(cs2, R(0n, 1n)) === 0;
    status.innerHTML = 'At &rho; = <strong>' + Rtext(rho) + '</strong> and S = ' + Rtext(S)
      + ' slots, Kingman with c<sub>a</sub>&sup2; = ' + Rtext(ca2) + ' and c<sub>s</sub>&sup2; = '
      + Rtext(cs2) + ' gives <strong>' + (kYours ? Rshort(kYours, 3) : '—')
      + ' slots</strong>; with both coefficients at 1 it gives ' + (kMM1 ? Rshort(kMM1, 3) : '—')
      + ', which is the M/M/1 answer, and halving the service variance halves the '
      + '(c<sub>a</sub>&sup2; + c<sub>s</sub>&sup2;)/2 term with it &mdash; that factor is the '
      + 'whole content of the formula. ' + (halves
        ? 'With c<sub>s</sub>&sup2; = 0 you are looking at M/D/1, which waits half of what M/M/1 waits. '
        : '')
      + '<span class="tone-red">Now the disagreement.</span> This chain\'s own coefficients are '
      + Rtext(trueCa) + ' and ' + Rtext(trueCs) + ', and even there the formula says '
      + (kTrue ? Rshort(kTrue, 3) : '—') + ' while the exact answer is <strong>'
      + (exactWq ? Rshort(exactWq, 3) : '—') + '</strong> and a ' + commas(SLOTS)
      + '-slot run measures ' + Rfixed(simWq, 3) + '. The arithmetic above is exact; what is '
      + 'approximate is the claim that two numbers summarise a distribution. Kingman is a '
      + 'heavy-traffic limit read at moderate load, and it overstates here for that reason.';
  }

  [pS, qS, caS, csS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Variability, and what it costs",
        subtitle="Kingman's formula against the exact chain and against a run",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the variability"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every row is computed in the browser: the formula exactly, the chain exactly, and the "
            "simulation from the seed you choose. They do not agree, and the gap is the lesson.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - mms
# ---------------------------------------------------------------------------


def _mms(cfg):
    lam10 = int(cfg.get("lam10", 30))
    mu10 = int(cfg.get("mu10", 10))
    servers = int(cfg.get("servers", 4))

    markup = (
        _toolbar(
            "Pooling, and Erlang C",
            "one queue of s servers against s queues of one, at the same total load",
            [("cyan", "pooled M/M/s"), ("red", "s separate M/M/1"), ("amber", "the ratio")],
        )
        + _stage(
            _svg("msPlot", "0 0 520 190",
                 "The waiting time of a pooled queue against separate queues, across server counts.")
        )
        + _table("msTable")
        + _banner("msStatus")
    )
    controls = (
        _range("msLam", "&lambda; &mdash; total arrival rate (tenths)", 1, 80, lam10)
        + _range("msMu", "&mu; &mdash; service rate of one server (tenths)", 1, 40, mu10)
        + _range("msS", "servers (s)", 1, 12, servers)
        + _kpis(
            [
                ("&rho; = &lambda;/(s&mu;)", "msRho"),
                ("P(wait), pooled &mdash; Erlang C", "msPw"),
                ("W<sub>q</sub> pooled", "msWqP"),
                ("W<sub>q</sub> separate &divide; pooled", "msRatio"),
            ]
        )
        + _hint(
            "msHint",
            "Erlang C is <em>stated</em> here and used, not derived. It comes out of a birth&ndash;death "
            "chain whose death rate is min(n, s)&mu;, and that derivation is Operations Research, "
            "<span class=\"tt\">multiple-servers-and-erlang-c</span>. What this page is for is the "
            "design idea the formula prices: one queue in front of s servers beats s queues with "
            "one each, and the gap widens as &rho; rises.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('msLam'), muS = document.getElementById('msMu');
  var sS = document.getElementById('msS');
  var plot = document.getElementById('msPlot'), table = document.getElementById('msTable');
  var status = document.getElementById('msStatus');

  function redraw() {
    var lam = R(BigInt(+lamS.value), 10n), mu = R(BigInt(+muS.value), 10n), s = +sS.value;
    document.getElementById('msLamOut').textContent = Rtext(lam) + ' / s';
    document.getElementById('msMuOut').textContent = Rtext(mu) + ' / s each';
    document.getElementById('msSOut').textContent = s + (s === 1 ? ' server' : ' servers');

    var pooled = erlangC(lam, mu, s);
    var each = Rdiv(lam, R(BigInt(s), 1n));
    var sep = mm1(each, mu);
    var rho = Rdiv(lam, Rmul(R(BigInt(s), 1n), mu));

    document.getElementById('msRho').textContent = Rtext(rho);
    document.getElementById('msPw').textContent = pooled.stable ? Rshort(pooled.pWait, 5) : 'unstable';
    document.getElementById('msWqP').textContent = pooled.stable ? Rshort(pooled.Wq, 5) : '—';
    document.getElementById('msRatio').innerHTML =
      (pooled.stable && sep.stable && !Rzero(pooled.Wq))
        ? Rshort(Rdiv(sep.Wq, pooled.Wq), 3) + ' = ' + Rfixed(Rdiv(sep.Wq, pooled.Wq), 3) + '&times;'
        : '&mdash;';

    var body = '<thead><tr><th>arrangement</th><th>&rho;</th><th>P(wait)</th>'
      + '<th>L<sub>q</sub></th><th>W<sub>q</sub></th></tr></thead><tbody>';
    body += '<tr><td class="tone-cyan">one queue, ' + s + ' server' + (s === 1 ? '' : 's')
      + '</td><td>' + Rtext(rho) + '</td><td>'
      + (pooled.stable ? Rshort(pooled.pWait, 5) : 'unstable') + '</td><td>'
      + (pooled.stable ? Rshort(pooled.Lq, 5) : '—') + '</td><td>'
      + (pooled.stable ? Rshort(pooled.Wq, 5) : '—') + '</td></tr>';
    body += '<tr><td class="tone-red">' + s + ' queue' + (s === 1 ? '' : 's')
      + ', ' + Rtext(each) + ' / s each</td><td>' + (sep.stable ? Rtext(sep.rho) : Rtext(sep.rho))
      + '</td><td>' + (sep.stable ? Rshort(sep.rho, 5) : 'unstable') + '</td><td>'
      + (sep.stable ? Rshort(sep.Lq, 5) : '—') + '</td><td>'
      + (sep.stable ? Rshort(sep.Wq, 5) : '—') + '</td></tr>';
    if (pooled.stable && sep.stable && !Rzero(pooled.Wq)) {
      body += '<tr><td class="tone-amber">separate &divide; pooled</td><td colspan="3">'
        + 'the price of splitting the traffic</td><td>'
        + Rshort(Rdiv(sep.Wq, pooled.Wq), 3) + '&times;</td></tr>';
    }
    body += '<tr><td class="tone-muted">Erlang C</td><td colspan="4">'
      + 'P(wait) = (a<sup>s</sup>/s!)/(1 &minus; &rho;) &divide; '
      + '[&Sigma;<sub>n&lt;s</sub> a<sup>n</sup>/n! + (a<sup>s</sup>/s!)/(1 &minus; &rho;)], '
      + 'with a = &lambda;/&mu; = ' + Rtext(Rdiv(lam, mu)) + ' &mdash; stated here, derived in '
      + 'Operations Research</td></tr></tbody>';
    table.innerHTML = body;

    var maxS = 12, j, ppts = [], spts = [], top = 0, vals = [];
    for (j = 1; j <= maxS; j += 1) {
      var pj = erlangC(lam, mu, j), sj = mm1(Rdiv(lam, R(BigInt(j), 1n)), mu);
      var pv = pj.stable ? parseFloat(Rfixed(pj.Wq, 5)) : null;
      var sv = sj.stable ? parseFloat(Rfixed(sj.Wq, 5)) : null;
      vals.push([j, pv, sv]);
      if (pv !== null && pv > top) top = pv;
      if (sv !== null && sv > top) top = sv;
    }
    if (top <= 0) top = 1;
    var base = 146, W0 = 480 / maxS;
    var svg = '<text x="0" y="12" font-size="11" fill="var(--muted)">W<sub>q</sub> against the number '
      + 'of servers, at a fixed total &lambda; = ' + Rtext(lam) + '</text>';
    for (j = 0; j < vals.length; j += 1) {
      var x = 20 + j * W0;
      if (vals[j][2] !== null) {
        spts.push([x, base - Math.min(1, vals[j][2] / top) * 112]);
      }
      if (vals[j][1] !== null) {
        ppts.push([x, base - Math.min(1, vals[j][1] / top) * 112]);
      }
      svg += '<text x="' + x + '" y="' + (base + 13) + '" text-anchor="middle" font-size="9" fill="var('
        + (vals[j][0] === s ? '--amber' : '--muted') + ')">' + vals[j][0] + '</text>';
    }
    function line(pts, colour, dash) {
      if (!pts.length) return '';
      return '<polyline fill="none" stroke="var(' + colour + ')" stroke-width="1.8"'
        + (dash ? ' stroke-dasharray="4 3"' : '') + ' points="'
        + pts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />';
    }
    svg += line(spts, '--red', true) + line(ppts, '--cyan', false)
      + '<line x1="10" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="' + (base + 30) + '" font-size="10" fill="var(--cyan)">solid: one pooled queue</text>'
      + '<text x="170" y="' + (base + 30) + '" font-size="10" fill="var(--red)">dashed: '
      + 'the traffic split evenly into separate queues</text>'
      + '<text x="10" y="' + (base + 44) + '" font-size="10" fill="var(--muted)">both lines are at the '
      + 'same total load at every point; only the arrangement differs</text>';
    plot.innerHTML = svg;

    if (!pooled.stable) {
      status.innerHTML = '<span class="tone-red">&rho; = ' + Rtext(rho) + ' &ge; 1 with ' + s
        + ' server' + (s === 1 ? '' : 's') + '.</span> Pooling cannot rescue a system that is short '
        + 'of capacity; it rearranges waiting, it does not create service. Add servers until '
        + 's&mu; exceeds &lambda;, then come back and compare the arrangements.';
      return;
    }
    status.innerHTML = 'At &lambda; = ' + Rtext(lam) + ', &mu; = ' + Rtext(mu) + ' and s = ' + s
      + ', both arrangements run at <strong>&rho; = ' + Rtext(rho) + '</strong> &mdash; identical '
      + 'utilisation, identical hardware. Pooled, an arrival waits at all with probability <strong>'
      + Rshort(pooled.pWait, 5) + '</strong> and waits <strong>' + Rshort(pooled.Wq, 5)
      + '</strong> on average. Split into ' + s + ' independent queues of ' + Rtext(each)
      + ' per second, the same arrival waits <strong>' + Rshort(sep.Wq, 5) + '</strong> &mdash; '
      + (Rzero(pooled.Wq) ? '' : '<strong>' + Rshort(Rdiv(sep.Wq, pooled.Wq), 3)
          + '&times;</strong> as long, ')
      + 'because a queue with an idle server beside it is waiting for no reason. '
      + 'Raise &lambda; and watch that ratio grow: pooling is worth most exactly when you can '
      + 'least afford to wait.';
  }

  [lamS, muS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Many servers, and pooling",
        subtitle="One queue of s servers against s queues of one",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the load and the servers"),
        panel_intro=cfg.get(
            "panel_intro",
            "Erlang C prices the pooled arrangement and M/M/1 at &lambda;/s prices the separate "
            "one, both as exact fractions, so the ratio between them is exact too.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - finite
# ---------------------------------------------------------------------------

_LOSS_TARGETS = [("100", "1%"), ("1000", "0.1%"), ("10000", "0.01%")]


def _finite(cfg):
    lam20 = int(cfg.get("lam20", 16))
    mu20 = int(cfg.get("mu20", 20))
    K = int(cfg.get("K", 4))
    target = int(cfg.get("target", 100))

    markup = (
        _toolbar(
            "Bounded queues and loss",
            "a buffer of K turns waiting into dropping &mdash; and changes which &lambda; Little's Law takes",
            [("cyan", "&pi;<sub>n</sub>"), ("red", "blocked"), ("green", "admitted rate"),
             ("amber", "the wrong W")],
        )
        + _stage(
            _svg("fiPlot", "0 0 520 190",
                 "The truncated state distribution, with the blocked state marked, above the two candidate W values.")
        )
        + _table("fiTable")
        + _banner("fiStatus")
    )
    controls = (
        _range("fiLam", "&lambda; &mdash; offered arrival rate (twentieths)", 1, 30, lam20)
        + _range("fiMu", "&mu; &mdash; service rate (twentieths)", 2, 20, mu20)
        + _range("fiK", "K &mdash; buffer size (jobs the system can hold)", 1, 20, K)
        + _select("fiTarget", "Loss target", _LOSS_TARGETS, str(target))
        + _kpis(
            [
                ("&pi;<sub>K</sub> &mdash; blocking probability", "fiBlock"),
                ("Admitted rate &lambda;(1 &minus; &pi;<sub>K</sub>)", "fiAdm"),
                ("W = L / &lambda;(1 &minus; &pi;<sub>K</sub>)", "fiWright"),
                ("W = L / &lambda; &mdash; wrong", "fiWwrong"),
            ]
        )
        + _hint(
            "fiHint",
            "The rate that crosses into a lossy system is the <em>admitted</em> one. Lesson 2 "
            "proved L = &lambda;W on a trace of arrivals that actually entered; feed it the offered "
            "rate instead and you get a W that is too small by exactly the factor "
            "(1 &minus; &pi;<sub>K</sub>). Both are printed below so the size of that mistake is "
            "visible rather than described.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('fiLam'), muS = document.getElementById('fiMu');
  var kS = document.getElementById('fiK'), tSel = document.getElementById('fiTarget');
  var plot = document.getElementById('fiPlot'), table = document.getElementById('fiTable');
  var status = document.getElementById('fiStatus');

  function redraw() {
    var lam = R(BigInt(+lamS.value), 20n), mu = R(BigInt(+muS.value), 20n), K = +kS.value;
    var target = R(1n, BigInt(+tSel.value));
    document.getElementById('fiLamOut').textContent = Rtext(lam);
    document.getElementById('fiMuOut').textContent = Rtext(mu);
    document.getElementById('fiKOut').textContent = K + (K === 1 ? ' job' : ' jobs');

    var f = mm1k(lam, mu, K), rho = f.rho;
    var wrongW = Rdiv(f.L, lam);
    var cap = bufferLatencyCap(mu, K);
    var need = smallestBuffer(lam, mu, target, 60);

    document.getElementById('fiBlock').textContent = Rshort(f.blocking, 5) + ' = ' + Rpct(f.blocking, 3);
    document.getElementById('fiAdm').textContent = Rshort(f.lamEff, 5);
    document.getElementById('fiWright').textContent = Rshort(f.W, 4);
    document.getElementById('fiWwrong').textContent = Rshort(wrongW, 4);

    var body = '<thead><tr><th>n</th><th>&pi;<sub>n</sub></th><th>what it is</th></tr></thead><tbody>', n;
    for (n = 0; n <= K; n += 1) {
      body += '<tr><td class="' + (n === K ? 'tone-red' : 'tone-cyan') + '">' + n + '</td><td>'
        + Rshort(f.pi[n], 6) + '</td><td>'
        + (n === 0 ? 'empty' : (n === K ? 'full &mdash; an arrival here is dropped' : 'in service plus ' + (n - 1) + ' waiting'))
        + '</td></tr>';
    }
    body += '<tr><td colspan="3" class="tone-muted">&pi;<sub>K</sub> = (1 &minus; &rho;)&rho;<sup>K</sup>'
      + ' / (1 &minus; &rho;<sup>K+1</sup>)'
      + (Requ(rho, R(1n, 1n)) ? ' &mdash; at &rho; = 1 both halves vanish and every state is equally likely, which is the limit'
         : ', with &rho; = ' + Rtext(rho)) + '</td></tr>';
    body += '<tr><td>L</td><td>' + Rshort(f.L, 5) + '</td><td>&Sigma; n&pi;<sub>n</sub>, over a '
      + 'finite chain &mdash; so it exists at every &rho;, including &rho; &ge; 1</td></tr>'
      + '<tr><td class="tone-green">&lambda;(1 &minus; &pi;<sub>K</sub>)</td><td>' + Rshort(f.lamEff, 5)
      + '</td><td>the rate that actually crosses the boundary</td></tr>'
      + '<tr><td class="tone-green">W, correct</td><td>' + Rshort(f.W, 5)
      + '</td><td>L &divide; the admitted rate</td></tr>'
      + '<tr><td class="tone-amber">W, wrong</td><td>' + Rshort(wrongW, 5)
      + '</td><td>L &divide; the offered rate &mdash; too small by (1 &minus; &pi;<sub>K</sub>)</td></tr>'
      + '<tr><td>latency cap</td><td>' + Rshort(cap, 4) + '</td><td>at most K jobs ahead of you, '
      + 'about K/&mu; &mdash; a bounded buffer bounds the wait</td></tr></tbody>';
    table.innerHTML = body;

    var top = 0, j;
    for (j = 0; j <= K; j += 1) {
      var v = parseFloat(Rfixed(f.pi[j], 8));
      if (v > top) top = v;
    }
    if (top <= 0) top = 1;
    var W0 = 480 / (K + 1), base = 108;
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">&pi;<sub>n</sub> on a chain that '
      + 'stops at K = ' + K + ' &mdash; the last bar is the drop rate</text>';
    for (j = 0; j <= K; j += 1) {
      var h = (parseFloat(Rfixed(f.pi[j], 8)) / top) * 76;
      s += '<rect x="' + (20 + j * W0) + '" y="' + (base - h) + '" width="' + Math.max(2, W0 - 4)
        + '" height="' + Math.max(0.6, h) + '" fill="var(' + (j === K ? '--red' : '--cyan')
        + ')" opacity="0.78" />'
        + '<text x="' + (20 + j * W0 + (W0 - 4) / 2) + '" y="' + (base + 12) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">' + j + '</text>';
    }
    s += '<line x1="14" y1="' + base + '" x2="510" y2="' + base + '" stroke="var(--line-strong)" stroke-width="1" />';
    var wr = parseFloat(Rfixed(f.W, 5)), ww = parseFloat(Rfixed(wrongW, 5));
    var unit = Math.max(wr, ww) > 0 ? 300 / Math.max(wr, ww) : 1;
    s += '<text x="0" y="142" font-size="10" fill="var(--green)">W from the admitted rate</text>'
      + '<rect x="180" y="132" width="' + Math.max(1, wr * unit) + '" height="13" rx="2" fill="var(--green)" opacity="0.8" />'
      + '<text x="' + (185 + wr * unit) + '" y="143" font-size="10" fill="var(--green)" font-weight="700">'
      + Rfixed(f.W, 4) + '</text>'
      + '<text x="0" y="164" font-size="10" fill="var(--amber)">W from the offered rate</text>'
      + '<rect x="180" y="154" width="' + Math.max(1, ww * unit) + '" height="13" rx="2" fill="var(--amber)" opacity="0.8" />'
      + '<text x="' + (185 + ww * unit) + '" y="165" font-size="10" fill="var(--amber)" font-weight="700">'
      + Rfixed(wrongW, 4) + '</text>'
      + '<text x="0" y="182" font-size="10" fill="var(--muted)">the gap is the factor '
      + '1 &minus; &pi;<sub>K</sub> = ' + Rshort(Rsub(R(1n, 1n), f.blocking), 5) + '</text>';
    plot.innerHTML = s;

    var overOne = Rcmp(rho, R(1n, 1n)) >= 0;
    status.innerHTML = 'With K = ' + K + ' the system blocks <strong>' + Rpct(f.blocking, 3)
      + '</strong> of arrivals and admits <strong>' + Rshort(f.lamEff, 5)
      + '</strong> per unit time. It holds <strong>' + Rshort(f.L, 4) + '</strong> on average and '
      + 'the wait is capped near ' + Rshort(cap, 3) + ' &mdash; a bounded buffer converts waiting '
      + 'into dropping, which is a trade and not a fix. '
      + (overOne
          ? '<span class="tone-cyan">Note &rho; = ' + Rtext(rho) + ' &ge; 1 and the system is still '
            + 'perfectly well behaved:</span> a finite chain has a steady state at every load, because '
            + 'the excess leaves as loss instead of as backlog. '
          : '')
      + '<span class="tone-red">Now the error this lesson exists for.</span> W = L/&lambda; gives '
      + Rshort(wrongW, 4) + ', and it is wrong. Lesson 2 proved L = &lambda;W by counting customers '
      + 'that entered the system; here ' + Rpct(f.blocking, 3) + ' of them never did. The rate that '
      + 'crosses the boundary is &lambda;(1 &minus; &pi;<sub>K</sub>) = ' + Rshort(f.lamEff, 5)
      + ', so the true W is <strong>' + Rshort(f.W, 4) + '</strong> &mdash; larger by exactly '
      + '1/(1 &minus; &pi;<sub>K</sub>). '
      + (need < 0
          ? 'No buffer up to 60 gets the loss under the chosen target at this load.'
          : 'To hold loss under the target you need <strong>K = ' + need + '</strong>, which buys a '
            + 'latency cap of about ' + Rshort(bufferLatencyCap(mu, need), 3)
            + ' &mdash; the bufferbloat trade in one line: a bigger buffer drops less and waits longer.');
  }

  [lamS, muS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  tSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bounded queues and loss",
        subtitle="πₖ, the admitted rate, and the two W values it separates",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the buffer"),
        panel_intro=cfg.get(
            "panel_intro",
            "The truncated chain is solved exactly for the rates you set, and both candidate W "
            "values are printed side by side &mdash; the correct one from the admitted rate, the "
            "common mistake from the offered one.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L12 - bucket
# ---------------------------------------------------------------------------

BUCKET_PRESETS = [
    {"key": "boundary-burst",
     "label": "a burst straddling a window boundary — the lesson's trace",
     "times": "0 200 400 600 800 900 900 900 900 900 1000 1000 1000 1000 1000 1400 1600 1800 2000 2200",
     "rate": 5, "burst": 3},
    {"key": "steady", "label": "arrivals at exactly the rate — nothing is refused",
     "times": "0 200 400 600 800 1000 1200 1400 1600 1800 2000 2200 2400 2600 2800",
     "rate": 5, "burst": 3},
    {"key": "one-big-burst", "label": "everything at once — the burst size is the whole allowance",
     "times": "0 0 0 0 0 0 0 0 0 0 1000 2000 3000",
     "rate": 5, "burst": 8},
]


def _bucket(cfg):
    idx = _preset_index(cfg, BUCKET_PRESETS, "bucket")
    pre = BUCKET_PRESETS[idx]

    markup = (
        _toolbar(
            "Token buckets and rate limiting",
            "b + rt in any window of t &mdash; which is not the same as r per second",
            [("green", "admitted"), ("red", "rejected"), ("cyan", "tokens in the bucket"),
             ("amber", "the fixed window")],
        )
        + _stage(
            _svg("bkPlot", "0 0 520 200",
                 "The token level over time with each arrival marked admitted or rejected, above the same trace through a fixed window.")
        )
        + _table("bkTable")
        + _banner("bkStatus")
    )
    controls = (
        _select("bkPreset", "Worked example", [(p["key"], p["label"]) for p in BUCKET_PRESETS], pre["key"])
        + _text("bkTimes", "Arrival times (ms, any order)", pre["times"])
        + _range("bkRate", "r &mdash; refill rate (tokens per second)", 1, 20, pre["rate"])
        + _range("bkBurst", "b &mdash; bucket size (tokens)", 1, 20, pre["burst"])
        + _kpis(
            [
                ("Admitted by the bucket", "bkAdm"),
                ("Rejected by the bucket", "bkRej"),
                ("Largest second the bucket allows", "bkBurstOut"),
                ("Largest second the fixed window allows", "bkFixedBurst"),
            ]
        )
        + _hint(
            "bkHint",
            "A bucket of b tokens refilling at r admits at most b + rt in any window of length t, "
            "so it is not a cap of r per second &mdash; it is a cap on the <em>average</em> with b "
            "of slack. A fixed window claims to be a cap of r per second and is not even that: two "
            "full windows back to back put 2r through in one window's width.",
        )
    )

    script = _CORE_JS + _presets_js(BUCKET_PRESETS) + r"""
  var sel = document.getElementById('bkPreset'), timesIn = document.getElementById('bkTimes');
  var rateS = document.getElementById('bkRate'), burstS = document.getElementById('bkBurst');
  var plot = document.getElementById('bkPlot'), table = document.getElementById('bkTable');
  var status = document.getElementById('bkStatus');
  var WINDOW = 1000;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('bucket: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    timesIn.value = p.times;
    rateS.value = p.rate;
    burstS.value = p.burst;
  }

  function redraw() {
    var times = parseTimes(timesIn.value, 40);
    var rv = +rateS.value, bv = +burstS.value;
    document.getElementById('bkRateOut').textContent = rv + ' / s';
    document.getElementById('bkBurstOut2').textContent = bv + (bv === 1 ? ' token' : ' tokens');

    if (!times) {
      plot.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">'
        + 'Type some arrival times in milliseconds.</text>';
      table.innerHTML = '';
      ['bkAdm', 'bkRej', 'bkBurstOut', 'bkFixedBurst'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      status.innerHTML = '<span class="tone-red">No arrivals to rate-limit.</span> '
        + 'Type whole milliseconds separated by spaces.';
      return;
    }

    var r = R(BigInt(rv), 1n);
    var bucket = bucketRun(times, r, bv);
    var fixed = fixedWindowRun(times, rv, WINDOW);
    var bBurst = largestBurst(bucket.rows, WINDOW);
    var fBurst = largestBurst(fixed.rows, WINDOW);

    document.getElementById('bkAdm').textContent = bucket.admitted + ' of ' + times.length;
    document.getElementById('bkRej').textContent = String(bucket.rejected);
    document.getElementById('bkBurstOut').textContent = bBurst + ' (bound b + r = ' + (bv + rv) + ')';
    document.getElementById('bkFixedBurst').textContent = fBurst + ' (it claims ' + rv + ')';

    var span = Math.max(1, times[times.length - 1]);
    var X = function (t) { return 14 + (t / span) * 480; };
    var capTop = Math.max(1, bv);
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">tokens in the bucket, and what '
      + 'each arrival got &mdash; capacity ' + bv + ', refilling ' + rv + ' a second</text>';
    var tpts = [], i;
    for (i = 0; i < bucket.rows.length; i += 1) {
      var lvl = parseFloat(Rfixed(bucket.rows[i].tokens, 4));
      tpts.push([X(bucket.rows[i].t), 92 - (lvl / capTop) * 62]);
    }
    s += '<polyline fill="none" stroke="var(--cyan)" stroke-width="1.4" points="'
      + tpts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />';
    for (i = 0; i < bucket.rows.length; i += 1) {
      var row = bucket.rows[i];
      s += '<circle cx="' + X(row.t) + '" cy="' + (row.admit ? 100 : 108) + '" r="2.6" fill="var('
        + (row.admit ? '--green' : '--red') + ')" />';
    }
    s += '<line x1="14" y1="92" x2="500" y2="92" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="14" y="120" font-size="10" fill="var(--green)">upper dots: admitted ('
      + bucket.admitted + ')</text>'
      + '<text x="200" y="120" font-size="10" fill="var(--red)">lower dots: rejected ('
      + bucket.rejected + ')</text>';
    s += '<text x="0" y="142" font-size="11" fill="var(--muted)">the same trace through a fixed '
      + 'window of ' + WINDOW + ' ms with a limit of ' + rv + '</text>';
    var w;
    for (w = 0; w * WINDOW <= span; w += 1) {
      s += '<line x1="' + X(w * WINDOW) + '" y1="150" x2="' + X(w * WINDOW)
        + '" y2="176" stroke="var(--amber)" stroke-width="1" stroke-dasharray="2 3" />';
    }
    for (i = 0; i < fixed.rows.length; i += 1) {
      s += '<circle cx="' + X(fixed.rows[i].t) + '" cy="' + (fixed.rows[i].admit ? 158 : 166)
        + '" r="2.6" fill="var(' + (fixed.rows[i].admit ? '--green' : '--red') + ')" />';
    }
    s += '<line x1="14" y1="176" x2="500" y2="176" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="14" y="192" font-size="10" fill="var(--muted)">the dashed lines are window '
      + 'boundaries; the fixed window lets ' + fBurst + ' through in one second somewhere, '
      + 'against a stated limit of ' + rv + '</text>';
    plot.innerHTML = s;

    var body = '<thead><tr><th>t (ms)</th><th>tokens after</th><th>bucket</th><th>fixed window</th></tr></thead><tbody>';
    for (i = 0; i < bucket.rows.length && i < 24; i += 1) {
      body += '<tr><td>' + commas(bucket.rows[i].t) + '</td><td>'
        + Rfixed(bucket.rows[i].tokens, 3) + '</td><td class="'
        + (bucket.rows[i].admit ? 'tone-green' : 'tone-red') + '">'
        + (bucket.rows[i].admit ? 'admitted' : 'rejected') + '</td><td class="'
        + (fixed.rows[i].admit ? 'tone-green' : 'tone-red') + '">'
        + (fixed.rows[i].admit ? 'admitted' : 'rejected') + '</td></tr>';
    }
    if (bucket.rows.length > 24) {
      body += '<tr><td colspan="4" class="tone-muted">' + (bucket.rows.length - 24)
        + ' more arrivals, all counted in the totals above</td></tr>';
    }
    body += '<tr><td colspan="2">totals</td><td class="tone-green">' + bucket.admitted + ' in, '
      + bucket.rejected + ' out</td><td class="tone-amber">' + fixed.admitted + ' in, '
      + fixed.rejected + ' out</td></tr></tbody>';
    table.innerHTML = body;

    status.innerHTML = 'The bucket admitted <strong>' + bucket.admitted + ' of ' + times.length
      + '</strong> and the largest second it ever let through was <strong>' + bBurst
      + '</strong> &mdash; under the bound b + r&times;1 = ' + (bv + rv) + ', which is the guarantee: '
      + 'at most <strong>' + bv + ' + ' + rv + 't</strong> in any window of t seconds. So "'
      + rv + ' per second" is the long-run average, and ' + bv + ' is how much of it you may spend '
      + 'at once. The fixed window admitted ' + fixed.admitted + ' and let <strong>' + fBurst
      + '</strong> through in one second while claiming a limit of ' + rv
      + (fBurst > rv
          ? ' &mdash; <span class="tone-red">' + Rfixed(R(BigInt(fBurst), BigInt(rv)), 2)
            + '&times; its own limit</span>, because a counter that resets at a boundary lets a '
            + 'window\'s worth out on each side of it.'
          : ' on this trace. Move an arrival across a boundary and watch that change.');
  }

  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  timesIn.addEventListener('input', redraw);
  [rateS, burstS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    controls = controls.replace('id="bkBurstOut"', 'id="bkBurstOut2"', 1)
    return Lab(
        title="Token buckets and rate limiting",
        subtitle="b + rt in any window, and what a fixed window does instead",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the trace and the limiter"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each arrival is run through the bucket in order, with the token level kept as an exact "
            "fraction, and through a fixed window beside it so the two verdicts can differ.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L13 - backlog
# ---------------------------------------------------------------------------


def _backlog(cfg):
    mu = int(cfg.get("mu", 1000))
    before = int(cfg.get("before", 800))
    spike = int(cfg.get("spike", 1500))
    dur = int(cfg.get("duration", 60))
    after = int(cfg.get("after", 800))

    markup = (
        _toolbar(
            "Transient overload",
            "the area a spike leaves behind, and how long it takes to give it back",
            [("cyan", "&lambda;(t)"), ("green", "&mu;"), ("red", "backlog"), ("amber", "consumer lag")],
        )
        + _stage(
            _svg("blPlot", "0 0 520 210",
                 "The arrival rate against the service rate over an episode, with the accumulated backlog below it.")
        )
        + _table("blTable")
        + _banner("blStatus")
    )
    controls = (
        _range("blMu", "&mu; &mdash; what the consumer can drain (per second)", 100, 3000, mu, 50)
        + _range("blBefore", "&lambda; before the spike", 0, 3000, before, 50)
        + _range("blSpike", "&lambda; during the spike", 0, 4000, spike, 50)
        + _range("blDur", "how long the spike lasts (seconds)", 1, 300, dur)
        + _range("blAfter", "&lambda; after the spike", 0, 3000, after, 50)
        + _kpis(
            [
                ("Peak backlog", "blPeak"),
                ("Time to drain it", "blDrain"),
                ("Worst consumer lag", "blLag"),
                ("Total episode", "blTotal"),
            ]
        )
        + _hint(
            "blHint",
            "The backlog is an <em>area</em>: the excess rate multiplied by the time it lasts. It "
            "drains at the headroom you have left afterwards, so a one-minute spike can take ten "
            "minutes to clear &mdash; latency does not recover when the spike ends, it recovers "
            "when the area does.",
        )
    )

    script = _CORE_JS + r"""
  var muS = document.getElementById('blMu'), befS = document.getElementById('blBefore');
  var spkS = document.getElementById('blSpike'), durS = document.getElementById('blDur');
  var aftS = document.getElementById('blAfter');
  var plot = document.getElementById('blPlot'), table = document.getElementById('blTable');
  var status = document.getElementById('blStatus');

  function redraw() {
    var mu = R(BigInt(+muS.value), 1n), before = R(BigInt(+befS.value), 1n);
    var spike = R(BigInt(+spkS.value), 1n), after = R(BigInt(+aftS.value), 1n);
    var dur = +durS.value;
    document.getElementById('blMuOut').textContent = commas(+muS.value) + ' / s';
    document.getElementById('blBeforeOut').textContent = commas(+befS.value) + ' / s';
    document.getElementById('blSpikeOut').textContent = commas(+spkS.value) + ' / s';
    document.getElementById('blDurOut').textContent = dur + ' s';
    document.getElementById('blAfterOut').textContent = commas(+aftS.value) + ' / s';

    var plan = backlogPlan(mu, before, spike, dur, after);
    document.getElementById('blPeak').textContent = commas(Rfixed(plan.peak, 0)) + ' waiting';
    document.getElementById('blDrain').textContent = plan.drainSecs
      ? Rshort(plan.drainSecs, 1) + ' s' : (Rzero(plan.peak) ? 'nothing to drain' : 'never');
    document.getElementById('blLag').textContent = Rshort(plan.maxLagSecs, 2) + ' s';
    document.getElementById('blTotal').textContent = plan.totalSecs
      ? Rshort(plan.totalSecs, 1) + ' s' : (Rzero(plan.peak) ? '—' : 'unbounded');

    var horizon = plan.totalSecs
      ? Math.max(dur + 1, Math.ceil(parseFloat(Rfixed(plan.totalSecs, 3))) + Math.ceil(dur / 2))
      : dur * 4;
    horizon = Math.max(4, Math.min(2000, horizon));
    var X = function (t) { return 14 + (t / horizon) * 486; };
    var rateTop = Math.max(1, parseFloat(Rfixed(mu, 2)), parseFloat(Rfixed(spike, 2)),
                           parseFloat(Rfixed(before, 2)), parseFloat(Rfixed(after, 2))) * 1.15;
    var Y = function (v) { return 86 - (v / rateTop) * 62; };
    var lamPts = [[X(0), Y(parseFloat(Rfixed(before, 3)))], [X(0), Y(parseFloat(Rfixed(spike, 3)))],
                  [X(dur), Y(parseFloat(Rfixed(spike, 3)))], [X(dur), Y(parseFloat(Rfixed(after, 3)))],
                  [X(horizon), Y(parseFloat(Rfixed(after, 3)))]];
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">'
      + '<tspan fill="var(--cyan)">&lambda;(t)</tspan> against '
      + '<tspan fill="var(--green)">&mu;</tspan> &mdash; the shaded excess is what accumulates</text>';
    var ym = Y(parseFloat(Rfixed(mu, 3)));
    var ys = Y(parseFloat(Rfixed(spike, 3)));
    if (Rcmp(spike, mu) > 0) {
      s += '<rect x="' + X(0) + '" y="' + ys + '" width="' + (X(dur) - X(0)) + '" height="'
        + Math.max(1, ym - ys) + '" fill="var(--red)" opacity="0.22" />';
    }
    s += '<polyline fill="none" stroke="var(--cyan)" stroke-width="1.8" points="'
      + lamPts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />'
      + '<line x1="' + X(0) + '" y1="' + ym + '" x2="' + X(horizon) + '" y2="' + ym
      + '" stroke="var(--green)" stroke-width="1.6" stroke-dasharray="5 3" />'
      + '<text x="' + X(horizon) + '" y="' + (ym - 4) + '" text-anchor="end" font-size="9" '
      + 'fill="var(--green)">&mu; = ' + commas(+muS.value) + '</text>'
      + '<line x1="14" y1="86" x2="500" y2="86" stroke="var(--line-strong)" stroke-width="1" />';

    var bpts = [], t, peakPx = Math.max(1, parseFloat(Rfixed(plan.peak, 3)));
    for (t = 0; t <= horizon; t += Math.max(1, Math.round(horizon / 200))) {
      bpts.push([X(t), 176 - (parseFloat(Rfixed(backlogAt(plan, dur, t), 3)) / peakPx) * 70]);
    }
    s += '<text x="0" y="110" font-size="11" fill="var(--muted)">the backlog itself &mdash; it peaks '
      + 'when the spike ends, not when latency does</text>'
      + '<polyline fill="none" stroke="var(--red)" stroke-width="1.8" points="'
      + bpts.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '" />'
      + '<line x1="' + X(dur) + '" y1="106" x2="' + X(dur) + '" y2="176" '
      + 'stroke="var(--amber)" stroke-width="1" stroke-dasharray="2 3" />'
      + '<text x="' + (X(dur) + 4) + '" y="120" font-size="9" fill="var(--amber)">the spike ends here</text>'
      + '<line x1="14" y1="176" x2="500" y2="176" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="14" y="190" font-size="9" fill="var(--muted)">0 s</text>'
      + '<text x="500" y="190" text-anchor="end" font-size="9" fill="var(--muted)">' + horizon + ' s</text>'
      + '<text x="14" y="204" font-size="10" fill="var(--muted)">worst lag '
      + Rshort(plan.maxLagSecs, 2) + ' s = backlog &divide; &mu;, and it arrives at the moment the '
      + 'incident "ends"</text>';
    plot.innerHTML = s;

    var marks = [0, Math.round(dur / 2), dur], i;
    if (plan.drainSecs) {
      var d = parseFloat(Rfixed(plan.drainSecs, 3));
      marks.push(dur + Math.round(d / 2));
      marks.push(dur + Math.ceil(d));
    }
    var body = '<thead><tr><th>t (s)</th><th>&lambda;(t)</th><th>backlog</th><th>lag = backlog/&mu;</th></tr></thead><tbody>';
    for (i = 0; i < marks.length; i += 1) {
      var tt = marks[i], rate = tt < dur ? spike : after;
      if (tt === 0) rate = spike;
      var bl = backlogAt(plan, dur, tt);
      body += '<tr><td class="' + (tt === dur ? 'tone-red' : 'tone-muted') + '">' + tt + '</td><td>'
        + commas(Rfixed(rate, 0)) + '</td><td>' + commas(Rfixed(bl, 0)) + '</td><td>'
        + Rshort(Rdiv(bl, mu), 2) + ' s</td></tr>';
    }
    body += '<tr><td colspan="2" class="tone-red">excess rate &lambda; &minus; &mu;</td><td>'
      + commas(Rfixed(plan.excess, 0)) + ' / s</td><td>for ' + dur + ' s</td></tr>'
      + '<tr><td colspan="2">peak = excess &times; duration</td><td>'
      + commas(Rfixed(plan.peak, 0)) + '</td><td>the area</td></tr>'
      + '<tr><td colspan="2" class="tone-green">drain headroom &mu; &minus; &lambda;<sub>after</sub></td><td>'
      + commas(Rfixed(plan.headroom, 0)) + ' / s</td><td>'
      + (plan.drainSecs ? Rshort(plan.drainSecs, 1) + ' s to clear' : 'never clears') + '</td></tr></tbody>';
    table.innerHTML = body;

    if (Rzero(plan.peak)) {
      status.innerHTML = 'At &lambda; = ' + commas(+spkS.value) + ' the "spike" is still under &mu; = '
        + commas(+muS.value) + ', so nothing accumulates: the consumer keeps up and the backlog stays '
        + 'at zero throughout. Raise the spike above &mu; and an area starts to build.';
      return;
    }
    status.innerHTML = 'For ' + dur + ' seconds work arrives <strong>' + commas(Rfixed(plan.excess, 0))
      + '</strong> a second faster than it leaves, so the backlog reaches <strong>'
      + commas(Rfixed(plan.peak, 0)) + '</strong> &mdash; that is an area, '
      + commas(Rfixed(plan.excess, 0)) + ' &times; ' + dur + '. '
      + (plan.drains
          ? 'Afterwards &lambda; falls to ' + commas(+aftS.value) + ', leaving <strong>'
            + commas(Rfixed(plan.headroom, 0)) + '</strong> a second of headroom, so clearing it takes '
            + '<strong>' + Rshort(plan.drainSecs, 1) + ' seconds</strong> &mdash; '
            + Rshort(Rdiv(plan.drainSecs, R(BigInt(dur), 1n)), 2) + '&times; the length of the spike. '
            + 'The worst lag a consumer sees is <strong>' + Rshort(plan.maxLagSecs, 2)
            + ' seconds</strong> and it arrives at the <em>end</em> of the incident, which is why '
            + 'latency does not recover when the spike does: the graph of &lambda; goes back to '
            + 'normal at t = ' + dur + ' and the graph of lag does not reach zero until t = '
            + Rshort(plan.totalSecs, 1) + '.'
          : '<span class="tone-red">And it never drains:</span> &lambda; afterwards is '
            + commas(+aftS.value) + ', which is not below &mu; = ' + commas(+muS.value)
            + ', so there is no headroom to give the backlog back with. The lag grows without bound '
            + 'from here &mdash; the incident has no end until &lambda; falls.');
  }

  [muS, befS, spkS, durS, aftS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Transient overload and the backlog",
        subtitle="A spike is an area, and the drain is longer than the spike",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Shape the episode"),
        panel_intro=cfg.get(
            "panel_intro",
            "The peak, the drain time and the worst lag are computed from the rates you set as "
            "exact fractions: an area, a division, and a second division.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "rates": _rates,
    "trace": _trace,
    "little": _little,
    "slotted": _slotted,
    "memoryless": _memoryless,
    "poisson": _poisson,
    "mm1": _mm1,
    "knee": _knee,
    "variability": _variability,
    "mms": _mms,
    "finite": _finite,
    "bucket": _bucket,
    "backlog": _backlog,
}

MODES = tuple(sorted(_MODES))


def queue_lab(cfg):
    """Course 3's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, not defensiveness. A kit that quietly fell back
    to a default mode would render a finished-looking page carrying another
    lesson's widget, and nothing downstream would notice: the markup tests pass,
    labcheck passes, and the reader is shown the wrong lesson's arithmetic under
    the right lesson's title. On this course that failure has a specific shape --
    `mm1` and `slotted` compute two DIFFERENT models of the same queue, and a
    silent fallback between them is exactly the confusion section 4.1 of the
    reconciliation exists to stop.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "queue_lab: unknown mode %r; the thirteen modes of course 3 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["queue_lab", "QUEUE_KIT_JS", "MODES"]
