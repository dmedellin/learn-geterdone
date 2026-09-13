"""Course 5: Availability and Failure -- one kit, thirteen modes, one arithmetic.

Availability is a fraction, and every lesson on this course is something that
happens to that fraction under composition. The kit exists because the reader's
intuition about composition is reliably wrong in six specific places, and the
only thing that fixes it is watching the arithmetic contradict the intuition on
numbers the reader chose.

Four decisions run through all thirteen modes.

  A FRACTION, NEVER A PERCENTAGE, INSIDE THE ARITHMETIC. The course's own
  how_to says it: the interesting differences here are in the fourth decimal
  place and a percentage hides them. So every availability is an exact rational
  and the percentage is produced once, at the last moment, by Rpct.

  ONE PERIOD TABLE, STATED. A month is a twelfth of a 365-day year -- 2 628 000
  seconds exactly -- because that is the convention under which 99.9% is the
  43.8 minutes a month the lesson quotes. A 30-day month would make it 43.2 and
  the reader would be unable to reconcile the page with the prose. Every period
  on every mode comes from periodSeconds, where mathcheck.js can call it.

  THE THREE COMPOSITIONS MUST AGREE WHERE THEY MEET. k-of-n at k = n is the
  series product and at k = 1 is the parallel form; those are identities, not
  approximations, and the kofn mode computes all three and prints the agreement
  rather than asserting it. If availKofN ever stops agreeing, the page says so
  on its face and scripts/mathcheck.js fails.

  ONE ROUNDED FIGURE, NAMED, AND IT IS THE MODEL THAT ROUNDS. `durability` is
  the only mode here that prints a float, and the thing being approximated is
  not the division -- it is the first-order rare-event truncation, which drops
  every term where two failures overlap. So that mode prints the float from
  durabilityLossApprox AND the exact fraction of the same first-order formula
  beside it, so the reader can see that the two agree and that the gap to the
  truth is somewhere else entirely. Every other figure in the kit is exact.

The modes, and the lesson each belongs to:

  nines       L1  (1 - A) x period, both directions, on a ladder of nines
  mtbf        L2  MTBF/(MTBF + MTTR), and the two levers that are worth the same
  series      L3  the product, and how far under the weakest link it lands
  parallel    L4  1 - prod(1 - Ai), with the failover time charged against it
  kofn        L5  the binomial tail, term by term, against series and parallel
  correlated  L6  c + (1 - c)p^2, and the c at which redundancy stops paying
  budget      L7  (1 - SLO) x requests, and what an incident spends of it
  retry       L8  (1 - p^(r+1))/(1 - p), worst exactly when p is worst
  storm       L9  the iteration table, its fixed point, and where it sits
  backoff     L10 two seeded histograms: waves with jitter and without
  shed        L11 goodput under shedding against goodput under collapse
  durability  L12 N! f^N (R/8760)^(N-1), the one approximation, labelled
  shuffle     L13 C(n-k,k)/C(n,k) and 1/C(n,k), with a sample assignment drawn
"""

from .algebra_core import RATIONAL_JS
from .common import Lab
from .counting import BIGINT_JS
from .sysdesign_core import APPROX_JS, AVAIL_JS, STREAM_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

AVAILKIT_JS = r"""
  /* ================================================================ output

     Rdec goes through Number(a.n)/Number(a.d). This course produces rationals
     that a double cannot hold at either end -- the storm iteration's seventh
     iterate has a three-thousand-digit denominator, and Number() of it is
     Infinity -- so decimals here are long division in BigInt, rounded half up
     at the last digit printed. */
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
  /* An availability as a percentage, still exact until the last digit. Five
     places by default, because four nines is 99.99000% and three is 99.90000%
     and at two places those are the same string. */
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 5 : places) + '%';
  }
  /* A percentage with enough places to be worth printing. Three nines needs
     five places and ten nines needs twelve, and a fixed width either wastes
     the column or prints 100.000000% for a number that is emphatically not
     one -- which on this course is the whole point being made. */
  function RpctAuto(a) {
    if (Requ(a, R(1n, 1n))) return '100%';
    return Rpct(a, Math.min(14, Math.max(4, ninesOf(a) + 2)));
  }
  /* Scientific notation for the one mode that prints a float. */
  function sciText(x, places) {
    if (!isFinite(x)) return 'n/a';
    if (x === 0) return '0';
    var e = Math.floor(Math.log10(Math.abs(x)));
    var m = x / Math.pow(10, e);
    return m.toFixed(places === undefined ? 3 : places)
      + ' &times; 10<sup>' + (e < 0 ? '&minus;' + (-e) : e) + '</sup>';
  }

  /* ========================================================= the periods

     One table, used by every mode. A month is a TWELFTH OF A 365-DAY YEAR,
     which is the convention under which 99.9% is 43.8 minutes a month; a
     30-day month gives 43.2 and no reader could reconcile that with the
     lesson. Stated here once rather than assumed thirteen times. */
  function periodSeconds(name) {
    if (name === 'hour') return R(3600n, 1n);
    if (name === 'day') return R(86400n, 1n);
    if (name === 'week') return R(604800n, 1n);
    if (name === 'month') return R(2628000n, 1n);
    if (name === 'quarter') return R(7884000n, 1n);
    if (name === 'year') return R(31536000n, 1n);
    return null;
  }
  /* Downtime in seconds over a period, and the availability that a downtime
     budget implies. The two directions of L1, and each is the other's inverse. */
  function downtimeSeconds(a, periodSec) {
    return Rmul(Rsub(R(1n, 1n), a), periodSec);
  }
  function availFromDowntime(downSec, periodSec) {
    return Rsub(R(1n, 1n), Rdiv(downSec, periodSec));
  }
  /* How many nines an availability has: the largest k with 1 - A <= 10^-k.
     An exact search over powers of ten, so no logarithm is anywhere near the
     number the page asserts. 99.95% has three nines, not three and a half. */
  function ninesOf(a) {
    var down = Rsub(R(1n, 1n), a);
    if (down.n <= 0n) return 99;
    var k = 0, bound = R(1n, 10n);
    while (k < 15 && Rcmp(down, bound) <= 0) { k += 1; bound = Rdiv(bound, R(10n, 1n)); }
    return k;
  }
  /* A duration read the way an incident review reads it. Exact: the seconds
     part keeps its fraction when it has one. */
  function durText(secs) {
    var neg = secs.n < 0n, a = neg ? R(-secs.n, secs.d) : secs;
    var whole = a.n / a.d, rem = Rsub(a, R(whole, 1n));
    var d = whole / 86400n, h = (whole % 86400n) / 3600n;
    var m = (whole % 3600n) / 60n, s = whole % 60n;
    var out = [];
    if (d > 0n) out.push(d + ' d');
    if (h > 0n) out.push(h + ' h');
    if (m > 0n) out.push(m + ' min');
    var tail = Radd(R(s, 1n), rem);
    if (tail.n > 0n || !out.length) out.push(Rfixed(tail, tail.d === 1n ? 0 : 2) + ' s');
    return (neg ? '-' : '') + out.join(' ');
  }
  /* A percentage the reader typed, as an exact fraction of one. "99.9" is
     999/1000 and stays 999/1000; it never becomes 0.9990000000000001. */
  function pctToFraction(text) {
    var r = Rparse(String(text).trim());
    if (r === null) return null;
    return Rdiv(r, R(100n, 1n));
  }
  /* A comma-separated chain of percentages, exactly. Returns null on anything
     that is not a list of availabilities, which is what stops a typo printing
     a confident wrong product. */
  function parseChain(text) {
    var parts = String(text).split(','), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var v = pctToFraction(s);
      if (v === null) return null;
      if (Rcmp(v, R(0n, 1n)) < 0 || Rcmp(v, R(1n, 1n)) > 0) return null;
      out.push(v);
    }
    return out.length ? out : null;
  }

  /* ================================================== L2: MTBF and MTTR

     A = MTBF/(MTBF + MTTR). Both arguments are rational seconds, so the
     availability of a 1000-hour/1-hour machine is 1000/1001 and not a
     decimal that has already lost the digit the lesson is about. */
  function availFromMtbf(mtbf, mttr) {
    return Rdiv(mtbf, Radd(mtbf, mttr));
  }
  /* The repair time a target availability allows, and the time between
     failures it would otherwise demand. R = M(1 - A)/A;  M = RA/(1 - A). */
  function mttrForTarget(mtbf, target) {
    return Rdiv(Rmul(mtbf, Rsub(R(1n, 1n), target)), target);
  }
  function mtbfForTarget(mttr, target) {
    return Rdiv(Rmul(mttr, target), Rsub(R(1n, 1n), target));
  }
  function failuresPerPeriod(mtbf, periodSec) { return Rdiv(periodSec, mtbf); }

  /* ============================================= L4: charging the failover

     1 - prod(1 - Ai) assumes the switch is instant. It is not: every failover
     is downtime of its own, and the events that trigger it happen at a rate
     the reader sets. The adjusted availability subtracts that time from the
     ideal, which is the whole of the lesson's misconception. */
  function failoverCharge(failoverSec, eventsPerPeriod, periodSec) {
    return Rdiv(Rmul(failoverSec, eventsPerPeriod), periodSec);
  }
  function parallelWithFailover(list, failoverSec, eventsPerPeriod, periodSec) {
    var ideal = availParallel(list);
    var charge = failoverCharge(failoverSec, eventsPerPeriod, periodSec);
    var adj = Rsub(ideal, charge);
    return { ideal: ideal, charge: charge, adjusted: Rcmp(adj, R(0n, 1n)) < 0 ? R(0n, 1n) : adj };
  }

  /* ============================================ L5: the binomial, term by term

     availKofN in the core sums the tail. This lists the terms it summed, so
     the reader can see that j = n is the series product and that the whole
     sum from j = 1 is the parallel form -- the two identities the lesson
     needs and the kofn mode checks on screen. */
  function kofnTerms(a, n) {
    var q = Rsub(R(1n, 1n), a), out = [], j;
    for (j = 0; j <= n; j += 1) {
      out.push({
        j: j,
        c: comb(n, j),
        term: Rmul(R(comb(n, j), 1n), Rmul(Rpow(a, j), Rpow(q, n - j)))
      });
    }
    return out;
  }
  /* The terms must sum to one. A binomial that does not is a binomial with a
     wrong coefficient in it, and this is the cheapest possible check. */
  function kofnTotal(a, n) {
    var terms = kofnTerms(a, n), s = R(0n, 1n), i;
    for (i = 0; i < terms.length; i += 1) s = Radd(s, terms[i].term);
    return s;
  }

  /* ============================================== L6: the common cause

     P(both down) = c + (1 - c)p^2. At c = 0 this is independence and the pair
     is p^2; it rises from there the moment c does, because c is added whole
     and only the p^2 term is discounted.
     The break-even is where the pair is no better than one machine:
        c + (1 - c)p^2 = p  =>  c(1 - p^2) = p(1 - p)  =>  c = p/(1 + p).
     Exact, and it is the number the lesson asks the reader to find. */
  function pairBothDown(c, p) {
    return Radd(c, Rmul(Rsub(R(1n, 1n), c), Rmul(p, p)));
  }
  function correlatedBreakEven(p) { return Rdiv(p, Radd(R(1n, 1n), p)); }
  /* How many times better than a single machine the pair actually is. Under
     independence this is 1/p; it collapses to 1 at the break-even. */
  function redundancyGain(c, p) { return Rdiv(p, pairBothDown(c, p)); }

  /* ================================================ L7: the error budget

     The budget is a count of FAILED REQUESTS, not of minutes, which is the
     lesson's misconception in one line: an incident that fails a tenth of
     requests for an hour costs a tenth of what a full outage costs. */
  function budgetRequests(slo, requests) {
    return Rmul(Rsub(R(1n, 1n), slo), requests);
  }
  function incidentBurn(ratePerSec, durationSec, severity) {
    return Rmul(Rmul(ratePerSec, durationSec), severity);
  }
  /* The full outage the budget pays for, in seconds -- the figure that makes
     an SLO concrete, and the one an on-call engineer actually remembers. */
  function budgetSeconds(slo, periodSec) {
    return Rmul(Rsub(R(1n, 1n), slo), periodSec);
  }

  /* ================================================ L8: retries as load

     retryAttempts and retrySuccess are in the core. What the lesson needs on
     top is the load: lambda attempts for every lambda requests, which is the
     amplification, and the share of that load which is duplicate work. */
  function amplifiedLoad(lambda, p, r) { return Rmul(lambda, retryAttempts(p, r)); }
  function duplicateShare(p, r) {
    var a = retryAttempts(p, r);
    return Rdiv(Rsub(a, R(1n, 1n)), a);
  }
  /* P(the attempt number i is ever made) = p^(i-1): every earlier attempt
     must have failed. This is the column the attempt ladder draws. */
  function attemptReach(p, i) { return Rpow(p, i); }

  /* =============================================== L9: the retry storm

     The map the lesson iterates. Load feeds failure feeds retries feeds load:

       p(L)  = base + (1 - base) * max(0, (L - C)/L)     failure rises with load
       L'    = lambda * retryAttempts(p(L), r)            retries raise the load

     Both halves are exact, and stormNext is one application of the composed
     map. It is a top-level function precisely so that mathcheck.js can iterate
     it without a page: a fixed point nobody has computed twice is a claim. */
  function stormFailure(load, cap, base) {
    var over = Rcmp(load, cap) > 0 ? Rdiv(Rsub(load, cap), load) : R(0n, 1n);
    return Radd(base, Rmul(Rsub(R(1n, 1n), base), over));
  }
  function stormNext(lambda, cap, base, r, load) {
    var p = stormFailure(load, cap, base);
    var amp = retryAttempts(p, r);
    return { p: p, amp: amp, load: Rmul(lambda, amp) };
  }
  /* The iteration, as the table the lesson shows. It stops early when the
     exact fractions outgrow the digit budget, and says so rather than
     hanging: the amplification 1 + p + ... + p^r carries the rth power of p's
     denominator, so at r = 3 each step cubes it and the seventh iterate
     already carries three thousand digits. That growth is a fact about the
     map, and the table prints the digit count as its own column. */
  function stormRun(lambda, cap, base, r, steps, digitCap) {
    var rows = [], load = lambda, i;
    for (i = 0; i < steps; i += 1) {
      if (String(load.d).length > digitCap) return { rows: rows, stopped: true };
      var s = stormNext(lambda, cap, base, r, load);
      rows.push({ step: i + 1, into: load, p: s.p, amp: s.amp, out: s.load });
      load = s.load;
    }
    return { rows: rows, stopped: false };
  }
  /* The fixed point, BRACKETED rather than iterated to. The map is increasing
     in L and bounded above by lambda*(r + 1), so g(L) = stormNext(L) - L is
     non-negative at lambda and non-positive at lambda*(r+1) and a root is
     caught between them. Bisection evaluates the map afresh at each probe, so
     nothing compounds and the denominators stay small -- which is why this
     reaches an answer the iteration cannot afford to reach.

     The result is an exact ENCLOSURE, not a rounded number: the fixed point
     is >= lo and <= hi, and both ends are fractions. */
  function stormFixedPoint(lambda, cap, base, r, halvings) {
    var lo = lambda, hi = Rmul(lambda, R(BigInt(r + 1), 1n)), i;
    for (i = 0; i < halvings; i += 1) {
      var mid = Rdiv(Radd(lo, hi), R(2n, 1n));
      var g = Rsub(stormNext(lambda, cap, base, r, mid).load, mid);
      if (Rcmp(g, R(0n, 1n)) >= 0) lo = mid; else hi = mid;
    }
    return { lo: lo, hi: hi };
  }

  /* ============================================== L10: backoff and jitter

     Every client fails at the same instant -- that is what an outage IS -- and
     schedules retry i at base * 2^(i-1) after that failure. Without jitter
     every client's retry i lands at the same millisecond, so the waves arrive
     at 1, 2, 4 and 8 seconds. With jitter of width w the delay is spread
     uniformly over [d(1 - w/2), d(1 + w/2)).

     The spread comes from lcgStream, so the histogram is the same every time
     the page is opened and a reader can check what they were told. */
  function backoffDelayMs(baseMs, attempt) {
    return baseMs * Math.pow(2, attempt - 1);
  }
  function backoffHistogram(clients, outageSec, baseMs, jitterPct, maxAttempts, horizonSec, seed, slotMs) {
    /* THE SLOT WIDTH IS THE WHOLE MEASUREMENT. Without jitter every client
       retries in the SAME millisecond, so the spike is instantaneous and any
       bucket wider than that understates it; a one-second bucket smears 600
       simultaneous retries into a comfortable-looking 600 a second. So the
       histogram is built at slotMs resolution, the page says what that is, and
       the un-jittered peak it reports is a floor rather than a measurement. */
    var A = 1103515245, C = 12345, M = 2147483648;
    var draws = lcgStream(A, C, M, seed, clients * maxAttempts);
    var slots = Math.ceil((horizonSec * 1000) / slotMs);
    var plain = [], jitter = [], i, t;
    for (t = 0; t < slots; t += 1) { plain.push(0); jitter.push(0); }
    var outageMs = outageSec * 1000, horizonMs = horizonSec * 1000;
    for (i = 0; i < clients; i += 1) {
      var a;
      for (a = 1; a <= maxAttempts; a += 1) {
        var d = backoffDelayMs(baseMs, a);
        /* no jitter: every client at the same millisecond */
        if (d < horizonMs) plain[Math.floor(d / slotMs)] += 1;
        if (d >= outageMs) break;            /* this attempt succeeds; the client stops */
      }
      for (a = 1; a <= maxAttempts; a += 1) {
        var dj = backoffDelayMs(baseMs, a);
        var u = draws[i * maxAttempts + (a - 1)] / M;
        var spread = dj * (1 - jitterPct / 200) + dj * (jitterPct / 100) * u;
        if (spread < horizonMs) jitter[Math.floor(spread / slotMs)] += 1;
        if (spread >= outageMs) break;
      }
    }
    return { plain: plain, jitter: jitter, slots: slots, slotMs: slotMs };
  }
  /* Slot counts folded back to whole seconds, for a table a reader can read. */
  function perSecond(counts, slotMs) {
    var per = Math.round(1000 / slotMs), out = [], i;
    for (i = 0; i < counts.length; i += 1) {
      var s = Math.floor(i / per);
      while (out.length <= s) out.push(0);
      out[s] += counts[i];
    }
    return out;
  }
  function peakOf(counts) {
    var m = 0;
    for (var i = 0; i < counts.length; i += 1) if (counts[i] > m) m = counts[i];
    return m;
  }
  function totalOf(counts) {
    var s = 0;
    for (var i = 0; i < counts.length; i += 1) s += counts[i];
    return s;
  }

  /* ================================= L11: shedding against collapse

     ONE SERVICE MODEL, TWO ADMISSION POLICIES. Under capacity every admitted
     request completes. Over it the server's capacity is spread across more
     requests than it can finish inside a client's patience, so the share that
     completes is C/L and the goodput is C*(C/L) -- work spent on a request
     that is then abandoned is work not spent on the rest. That collapse model
     is the lesson's own, it is stated on the page, and it is evaluated here
     rather than drawn.

     The shedder is not a second model: it admits min(offered, threshold) and
     puts THAT through the same function. Which is why a threshold above
     capacity collapses too, and the page can say so. */
  function goodputUnshed(offered, cap) {
    if (Rcmp(offered, cap) <= 0) return offered;
    return Rdiv(Rmul(cap, cap), offered);
  }
  /* What the shedder lets through, before the service model touches it. The
     rejected count and the utilisation are both about THIS number and not
     about the goodput, which is why it is a function of its own. */
  function admittedLoad(offered, threshold) {
    return Rcmp(offered, threshold) < 0 ? offered : threshold;
  }
  function goodputShed(offered, cap, threshold) {
    return goodputUnshed(admittedLoad(offered, threshold), cap);
  }
  function rejectedFraction(offered, threshold) {
    if (Rcmp(offered, threshold) <= 0) return R(0n, 1n);
    return Rdiv(Rsub(offered, threshold), offered);
  }

  /* ================================= L12: durability, and the one rounding

     Losing an item needs all N copies gone inside one repair window. To first
     order the first copy fails at rate N*f a year, and each further copy must
     follow inside the window R:

       P  ~=  N! * f^N * (R/8760)^(N-1)

     WHAT IS APPROXIMATE HERE IS THE MODEL, NOT THE DIVISION. The formula
     truncates every term in which failures overlap or a repair completes
     mid-window; the arithmetic on rational f and R is exact and
     durabilityLossExact returns it. The two functions are kept side by side
     for that reason: the page prints both, and their agreement is what shows
     the reader that the gap to the truth is in the modelling. */
  function durabilityLossExact(n, f, windowHours) {
    var share = Rdiv(windowHours, R(8760n, 1n));
    return Rmul(R(fact(n), 1n), Rmul(Rpow(f, n), Rpow(share, n - 1)));
  }
  function durabilityLossApprox(n, f, windowHours) {
    var share = Rnum(windowHours) / 8760;
    return Number(fact(n)) * Math.pow(Rnum(f), n) * Math.pow(share, n - 1);
  }
  /* The size of the truncation, shown rather than asserted: the first-order
     term x against the 1 - e^-x it stands in for. expNegApprox is the core's
     series, and this is the only place the kit calls it. */
  function truncationGap(x) {
    return { first: x, exact: 1 - expNegApprox(x, 1e-15) };
  }

  /* ================================== L13: shuffle sharding, exactly

     A tenant holds k of n nodes. A second tenant, drawn independently and
     uniformly, overlaps it in j nodes with the hypergeometric probability
        C(k,j) * C(n-k, k-j) / C(n,k)
     and the two ends of that distribution are the lesson: j = 0 is
     C(n-k,k)/C(n,k), no shared node at all, and j = k is 1/C(n,k), the
     identical set -- which is the only one of the k+1 outcomes that is an
     outage for both. */
  function shuffleOverlap(n, k, j) {
    var total = comb(n, k);
    if (total === 0n) return R(0n, 1n);
    return R(comb(k, j) * comb(n - k, k - j), total);
  }
  function shuffleDisjoint(n, k) { return shuffleOverlap(n, k, 0); }
  function shuffleIdentical(n, k) { return shuffleOverlap(n, k, k); }
  /* The share of tenants one bad node takes with it: a tenant uses k of the n
     nodes, so k/n of them touch any given node -- degraded, not down. */
  function blastFraction(n, k) { return R(BigInt(k), BigInt(n)); }
  /* A sample assignment, seeded, so the drawing and the probabilities above
     come from the same run and the reader can count the overlaps by eye. A
     partial Fisher-Yates over the node list, driven by lcgStream. */
  /* MINSTD (16807, 0, 2^31 - 1), NOT the glibc LCG the jitter panel uses, and
     the seed scrambled before it is used.

     The difference matters only because this function takes its draws MOD a
     small number. glibc's modulus is 2^31, so the low bits of its stream have
     tiny period -- mod 4 it is 0,1,2,3,0,1,2,3 forever -- and a partial
     Fisher-Yates driven by it explores measurably fewer sets than shuffle
     sharding actually reaches: averaged over forty seeds at n = 8, k = 2 and
     fifty tenants, 19.9 distinct sets against MINSTD's 23.4. This lesson
     prints the exact combinatorics beside a drawn sample, so a sample that is
     15% short makes the exact figure look wrong.

     2^31 - 1 is prime, so no modulus shares a factor with it. The seed goes
     through a splitmix64 finaliser first because an LCG's k-th value is affine
     in its seed: without it, reseeding 1, 2, 3 walks a straight line instead of
     sampling, and every mode here asks the reader to reseed and compare.

     The jitter panel above keeps glibc deliberately: it consumes draws as
     x / M, which uses the high bits, where glibc is fine. */
  function shuffleSeedState(seed) {
    var mask = (1n << 64n) - 1n;
    var x = (BigInt(seed >>> 0) + 0x9E3779B97F4A7C15n) & mask;
    x = ((x ^ (x >> 30n)) * 0xBF58476D1CE4E5B9n) & mask;
    x = ((x ^ (x >> 27n)) * 0x94D049BB133111EBn) & mask;
    x = x ^ (x >> 31n);
    return Number(x % 2147483646n) + 1;          /* never the fixed point 0 */
  }
  function shuffleAssign(n, k, tenants, seed) {
    var A = 16807, C = 0, M = 2147483647;
    var draws = lcgStream(A, C, M, shuffleSeedState(seed), tenants * k), out = [], t, i;
    for (t = 0; t < tenants; t += 1) {
      var pool = [], pick = [];
      for (i = 0; i < n; i += 1) pool.push(i);
      for (i = 0; i < k; i += 1) {
        var j = i + (draws[t * k + i] % (n - i));
        var tmp = pool[i]; pool[i] = pool[j]; pool[j] = tmp;
        pick.push(pool[i]);
      }
      out.push(pick.sort(function (x, y) { return x - y; }));
    }
    return out;
  }
  /* How many of a drawn set of tenants share every node with the first one --
     the count the sample assignment can be checked against. */
  function identicalCount(sets) {
    if (!sets.length) return 0;
    var first = sets[0].join(','), c = 0, i;
    for (i = 1; i < sets.length; i += 1) if (sets[i].join(',') === first) c += 1;
    return c;
  }
  function disjointCount(sets) {
    if (!sets.length) return 0;
    var first = sets[0], c = 0, i, j;
    for (i = 1; i < sets.length; i += 1) {
      var shared = false;
      for (j = 0; j < sets[i].length; j += 1) if (first.indexOf(sets[i][j]) >= 0) shared = true;
      if (!shared) c += 1;
    }
    return c;
  }
"""

_CORE_JS = RATIONAL_JS + BIGINT_JS + AVAIL_JS + STREAM_JS + APPROX_JS + AVAILKIT_JS


# ---------------------------------------------------------------------------
# Control furniture. The same three shapes every lab on the path uses, so a
# reader moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


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


# The availabilities a target selector offers, as exact fractions. Percentages
# never enter the arithmetic; the option VALUE is the fraction itself.
_TARGETS = [
    ("9/10", "90% &mdash; one nine"),
    ("99/100", "99% &mdash; two nines"),
    ("995/1000", "99.5%"),
    ("999/1000", "99.9% &mdash; three nines"),
    ("9995/10000", "99.95%"),
    ("9999/10000", "99.99% &mdash; four nines"),
    ("99999/100000", "99.999% &mdash; five nines"),
    ("999999/1000000", "99.9999% &mdash; six nines"),
]

_PERIODS = [
    ("day", "a day (86 400 s)"),
    ("week", "a week (604 800 s)"),
    ("month", "a month (2 628 000 s, a twelfth of a 365-day year)"),
    ("quarter", "a quarter (7 884 000 s)"),
    ("year", "a year (31 536 000 s)"),
]


# ---------------------------------------------------------------------------
# L1 - nines
# ---------------------------------------------------------------------------


def _nines(cfg):
    target = cfg.get("target", "999/1000")
    budget = int(cfg.get("budget_minutes", 44))
    period = cfg.get("period", "month")

    markup = (
        _toolbar(
            "Nines and downtime",
            "each further nine is ten times less of it, not a hundredth of a per cent more",
            [("cyan", "the nine you chose"), ("muted", "the ladder"), ("amber", "your budget")],
        )
        + _stage(_svg("nnLadder", "0 0 520 210", "A ladder of nines with the monthly downtime each one allows."))
        + _table("nnTable")
        + _banner("nnStatus")
    )
    controls = (
        _select(
            "nnDir",
            "Work from",
            [("target", "a target availability"), ("budget", "a downtime budget")],
            cfg.get("direction", "target"),
        )
        + _select("nnTarget", "Target availability", _TARGETS, target)
        + _range("nnBudget", "Downtime budget (minutes)", 1, 1200, budget)
        + _select("nnPeriod", "Budget period", _PERIODS, period)
        + _kpis(
            [
                ("Availability, exactly", "nnA"),
                ("As a percentage", "nnPct"),
                ("Nines", "nnNines"),
                ("Downtime per month", "nnMonth"),
                ("Downtime per year", "nnYear"),
                ("One more nine costs", "nnNext"),
            ]
        )
        + _hint(
            "nnHint",
            "A month here is a twelfth of a 365-day year &mdash; 2 628 000 seconds &mdash; which is "
            "the convention under which 99.9% is 43.8 minutes. Every figure is the exact fraction "
            "(1 &minus; A) &times; period; nothing is looked up.",
        )
    )

    script = _CORE_JS + r"""
  var dirSel = document.getElementById('nnDir'), tgtSel = document.getElementById('nnTarget');
  var budS = document.getElementById('nnBudget'), perSel = document.getElementById('nnPeriod');
  var ladder = document.getElementById('nnLadder'), table = document.getElementById('nnTable');
  var status = document.getElementById('nnStatus');
  var LADDER = ['day', 'week', 'month', 'quarter', 'year'];

  function currentAvail() {
    var minutes = +budS.value;
    document.getElementById('nnBudgetOut').textContent = minutes + ' min';
    if (dirSel.value === 'budget') {
      return availFromDowntime(R(BigInt(minutes) * 60n, 1n), periodSeconds(perSel.value));
    }
    return Rparse(tgtSel.value);
  }

  function redraw() {
    var a = currentAvail(), month = periodSeconds('month'), year = periodSeconds('year');
    var k = ninesOf(a), next = Rsub(R(1n, 1n), Rdiv(Rsub(R(1n, 1n), a), R(10n, 1n)));

    document.getElementById('nnA').textContent = Rtext(a);
    document.getElementById('nnPct').textContent = Rpct(a, 5);
    document.getElementById('nnNines').textContent = k >= 15 ? 'no downtime at all' : k + ' nine' + (k === 1 ? '' : 's');
    document.getElementById('nnMonth').textContent = durText(downtimeSeconds(a, month));
    document.getElementById('nnYear').textContent = durText(downtimeSeconds(a, year));
    document.getElementById('nnNext').textContent = durText(downtimeSeconds(next, month)) + ' a month';

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var per = periodSeconds(LADDER[i]);
      var here = downtimeSeconds(a, per), there = downtimeSeconds(next, per);
      rows += '<tr><td>' + LADDER[i] + '</td><td class="tt">' + Rtext(per) + ' s</td>'
        + '<td class="tone-cyan">' + durText(here) + '</td>'
        + '<td class="tone-muted">' + durText(there) + '</td>'
        + '<td>' + (Rzero(there) ? '&mdash;' : Rfixed(Rdiv(here, there), 0) + '&times;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>period</th><th>seconds in it</th><th>at ' + Rpct(a, 4)
      + '</th><th>at one more nine</th><th>ratio</th></tr></thead><tbody>' + rows + '</tbody>';

    var s = '', j;
    for (j = 1; j <= 6; j += 1) {
      var rung = Rsub(R(1n, 1n), Rpow(R(1n, 10n), j));
      var down = downtimeSeconds(rung, month);
      var w = 470 - (j - 1) * 74;                 /* a decade per rung, drawn linearly */
      var y = 14 + (j - 1) * 32;
      var live = (j === k);
      s += '<rect x="86" y="' + y + '" width="' + w + '" height="18" rx="3" fill="var('
        + (live ? '--cyan' : '--line-strong') + ')" opacity="' + (live ? '0.9' : '0.45') + '" />'
        + '<text x="0" y="' + (y + 13) + '" font-size="11" fill="var(' + (live ? '--cyan' : '--muted')
        + ')" font-weight="' + (live ? '700' : '400') + '">' + Rpct(rung, j > 3 ? j : 3) + '</text>'
        + '<text x="' + (92 + w) + '" y="' + (y + 13) + '" font-size="10" text-anchor="end" fill="var(--text)">'
        + durText(down) + ' a month</text>';
    }
    s += '<line x1="0" y1="200" x2="520" y2="200" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="208" font-size="10" fill="var(--muted)">each rung is one nine: the bar '
      + 'shortens by a factor of ten, not by a hundredth of a per cent</text>';
    ladder.innerHTML = s;

    var fromBudget = dirSel.value === 'budget';
    status.innerHTML = (fromBudget
        ? 'A budget of <strong>' + (+budS.value) + ' minutes per ' + perSel.value + '</strong> is an '
          + 'availability of <strong>' + Rtext(a) + '</strong> = ' + Rpct(a, 5) + ', so '
        : 'At <strong>' + Rpct(a, 5) + '</strong> ')
      + 'you may be down <strong>' + durText(downtimeSeconds(a, month)) + '</strong> a month and <strong>'
      + durText(downtimeSeconds(a, year)) + '</strong> a year. One more nine &mdash; ' + Rpct(next, 6)
      + ' &mdash; cuts that to ' + durText(downtimeSeconds(next, month)) + ' a month. '
      + 'The percentages differ by ' + Rpct(Rsub(next, a), 5) + ', which is why the difference sounds '
      + 'small; the minutes differ by a factor of <strong>ten</strong>, which is what it costs.';
  }

  [dirSel, tgtSel, perSel].forEach(function (el) { el.addEventListener('change', redraw); });
  budS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Nines are minutes",
        subtitle="Downtime is (1 − A) × period, and each nine is a factor of ten",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a target, or pick a budget"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both directions are the same equation rearranged, and both are exact fractions: "
            "an availability gives a downtime, and a downtime budget gives an availability.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - mtbf
# ---------------------------------------------------------------------------


def _mtbf(cfg):
    mtbf_h = int(cfg.get("mtbf_hours", 1000))
    mttr_m = int(cfg.get("mttr_minutes", 60))
    target = cfg.get("target", "9999/10000")

    markup = (
        _toolbar(
            "MTBF and MTTR",
            "A = MTBF &divide; (MTBF + MTTR), and the two levers are worth exactly the same",
            [("green", "running"), ("red", "being repaired"), ("purple", "either lever")],
        )
        + _stage(
            _svg("mtTrack", "0 0 520 96", "A year of operation drawn as alternating running and repairing segments.")
            + _svg("mtLevers", "0 0 520 118", "Downtime per year now, with the repair time halved, and with the time between failures doubled.")
        )
        + _table("mtTable")
        + _banner("mtStatus")
    )
    controls = (
        _range("mtMtbf", "Mean time between failures (hours)", 10, 8760, mtbf_h)
        + _range("mtMttr", "Mean time to repair (minutes)", 1, 1440, mttr_m)
        + _select("mtTarget", "Target availability", _TARGETS, target)
        + _kpis(
            [
                ("Availability, exactly", "mtA"),
                ("As a percentage", "mtPct"),
                ("Nines", "mtNines"),
                ("Failure cycles per year", "mtFail"),
                ("Downtime per year", "mtDown"),
                ("Repair time the target allows", "mtNeed"),
            ]
        )
        + _hint(
            "mtHint",
            "One cycle is MTBF + MTTR, so the availability is the running share of a cycle. "
            "Reliability is how often it breaks; availability is how much of the time it works, "
            "and the second is the one a user experiences.",
        )
    )

    script = _CORE_JS + r"""
  var mS = document.getElementById('mtMtbf'), rS = document.getElementById('mtMttr');
  var tgt = document.getElementById('mtTarget');
  var track = document.getElementById('mtTrack'), levers = document.getElementById('mtLevers');
  var table = document.getElementById('mtTable'), status = document.getElementById('mtStatus');

  function redraw() {
    var hours = +mS.value, mins = +rS.value;
    document.getElementById('mtMtbfOut').textContent = hours + ' h';
    document.getElementById('mtMttrOut').textContent = mins + ' min';

    var M = R(BigInt(hours) * 3600n, 1n), Rp = R(BigInt(mins) * 60n, 1n);
    var year = periodSeconds('year');
    var a = availFromMtbf(M, Rp);
    var halved = availFromMtbf(M, Rdiv(Rp, R(2n, 1n)));
    var doubled = availFromMtbf(Rmul(M, R(2n, 1n)), Rp);
    var want = Rparse(tgt.value);
    var needR = mttrForTarget(M, want);
    var needM = mtbfForTarget(Rp, want);
    var cycles = failuresPerPeriod(Radd(M, Rp), year);

    document.getElementById('mtA').textContent = Rtext(a);
    document.getElementById('mtPct').textContent = Rpct(a, 5);
    document.getElementById('mtNines').textContent = ninesOf(a) + ' nine' + (ninesOf(a) === 1 ? '' : 's');
    document.getElementById('mtFail').textContent = Rfixed(cycles, 2);
    document.getElementById('mtDown').textContent = durText(downtimeSeconds(a, year));
    document.getElementById('mtNeed').textContent = durText(needR);

    var same = Requ(halved, doubled);
    table.innerHTML = '<thead><tr><th>lever</th><th>MTBF</th><th>MTTR</th><th>A, exactly</th>'
      + '<th>downtime a year</th></tr></thead><tbody>'
      + '<tr><td>as it is</td><td>' + hours + ' h</td><td>' + mins + ' min</td><td class="tt">'
      + Rtext(a) + '</td><td>' + durText(downtimeSeconds(a, year)) + '</td></tr>'
      + '<tr><td class="tone-purple">halve the repair time</td><td>' + hours + ' h</td><td>'
      + Rfixed(R(BigInt(mins), 2n), 1) + ' min</td><td class="tt">' + Rtext(halved) + '</td><td>'
      + durText(downtimeSeconds(halved, year)) + '</td></tr>'
      + '<tr><td class="tone-purple">double the time between failures</td><td>' + (2 * hours)
      + ' h</td><td>' + mins + ' min</td><td class="tt">' + Rtext(doubled) + '</td><td>'
      + durText(downtimeSeconds(doubled, year)) + '</td></tr>'
      + '<tr><td class="tone-amber">to reach ' + Rpct(want, 4) + '</td><td>' + hours
      + ' h, or ' + Rfixed(Rdiv(needM, R(3600n, 1n)), 1) + ' h at the current repair time</td><td>'
      + durText(needR) + '</td><td class="tt">' + Rtext(want) + '</td><td>'
      + durText(downtimeSeconds(want, year)) + '</td></tr></tbody>';

    var cyclesShown = 8, cw = 512 / cyclesShown, i;
    var downShare = Rnum(Rdiv(Rp, Radd(M, Rp)));
    var s = '<text x="0" y="12" font-size="11" fill="var(--muted)">eight cycles, drawn to scale: '
      + 'each is MTBF then MTTR</text>';
    for (i = 0; i < cyclesShown; i += 1) {
      var x = 4 + i * cw, dw = Math.max(0.8, cw * downShare);
      s += '<rect x="' + x + '" y="24" width="' + (cw - dw) + '" height="30" rx="2" fill="var(--green)" opacity="0.75" />'
        + '<rect x="' + (x + cw - dw) + '" y="24" width="' + dw + '" height="30" fill="var(--red)" />';
    }
    s += '<text x="4" y="72" font-size="10" fill="var(--green)">running ' + Rpct(a, 4) + ' of every cycle</text>'
      + '<text x="516" y="72" font-size="10" text-anchor="end" fill="var(--red)">repairing '
      + Rpct(Rsub(R(1n, 1n), a), 4) + '</text>'
      + '<text x="4" y="90" font-size="10" fill="var(--muted)">the red slice is '
      + (downShare < 0.004 ? 'thinner than a pixel at this scale and is drawn at its minimum width'
                           : 'drawn at its true share of the cycle') + '</text>';
    track.innerHTML = s;

    var now = downtimeSeconds(a, year), h2 = downtimeSeconds(halved, year), d2 = downtimeSeconds(doubled, year);
    var unit = 430 / Math.max(1, parseFloat(Rfixed(now, 3)));
    function bar(label, value, y, tone) {
      var w = Math.max(2, parseFloat(Rfixed(value, 3)) * unit);
      return '<text x="0" y="' + (y + 12) + '" font-size="10" fill="var(--muted)">' + label + '</text>'
        + '<rect x="0" y="' + (y + 18) + '" width="' + w + '" height="16" rx="3" fill="var(' + tone + ')" opacity="0.85" />'
        + '<text x="' + (w + 6) + '" y="' + (y + 31) + '" font-size="10" fill="var(' + tone + ')">'
        + durText(value) + '</text>';
    }
    levers.innerHTML = bar('downtime a year, as it is', now, 0, '--red')
      + bar('with the repair time halved', h2, 36, '--purple')
      + bar('with the time between failures doubled', d2, 72, '--cyan')
      + '<text x="0" y="116" font-size="10" fill="var(--muted)">the lower two bars are the same length, '
      + 'and that is an identity, not a coincidence</text>';

    status.innerHTML = 'A machine that runs <strong>' + hours + ' h</strong> between failures and takes <strong>'
      + mins + ' min</strong> to repair is available <strong>' + Rtext(a) + '</strong> = ' + Rpct(a, 5)
      + ' of the time &mdash; ' + durText(downtimeSeconds(a, year)) + ' down a year over '
      + Rfixed(cycles, 2) + ' cycles. Halving the repair gives <strong>' + Rtext(halved)
      + '</strong>; doubling the time between failures gives <strong>' + Rtext(doubled) + '</strong>. '
      + (same
          ? 'Those are <span class="tone-purple">the same fraction</span>: A(2M, R) = 2M/(2M + R) = M/(M + R/2) = A(M, R/2), '
            + 'so the two levers are worth exactly the same and you should pull whichever is cheaper. Repairing faster '
            + 'usually is.'
          : '<span class="tone-red">Those should be the same fraction and are not, which is a defect in this page.</span>')
      + ' To reach ' + Rpct(want, 4) + ' you must repair within <strong>' + durText(needR)
      + '</strong>, or else run ' + Rfixed(Rdiv(needM, R(3600n, 1n)), 1) + ' h between failures.';
  }

  [mS, rS].forEach(function (el) { el.addEventListener('input', redraw); });
  tgt.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Availability is uptime over a cycle",
        subtitle="MTBF ÷ (MTBF + MTTR), and why repairing faster is the cheaper lever",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Move the two levers independently"),
        panel_intro=cfg.get(
            "panel_intro",
            "Reliability and availability are different numbers. A machine that fails rarely and "
            "takes a week to fix can be less available than one that fails weekly and is back in a minute.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - series
# ---------------------------------------------------------------------------

_DEFAULT_CHAIN = "99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9"


def _series(cfg):
    chain = cfg.get("chain", _DEFAULT_CHAIN)
    extra = int(cfg.get("extra", 0))
    extra_a = cfg.get("extra_avail", "9999/10000")

    markup = (
        _toolbar(
            "A chain multiplies down",
            "every dependency you add makes the whole thing worse than its weakest link",
            [("cyan", "running product"), ("amber", "the weakest link"), ("red", "what the chain costs")],
        )
        + _stage(_svg("seChainPlot", "0 0 520 190", "The running product of a chain of dependencies, falling with each one added."))
        + _table("seTable")
        + _banner("seStatus")
    )
    controls = (
        _text("seChain", "Dependency availabilities (percentages, comma separated)", chain)
        + _range("seExtra", "Extra dependencies bolted on", 0, 12, extra)
        + _select("seExtraA", "Each extra one at", _TARGETS, extra_a)
        + _kpis(
            [
                ("The chain, exactly", "seA"),
                ("As a percentage", "sePct"),
                ("Nines", "seNines"),
                ("The weakest link", "seWeak"),
                ("Downtime per month", "seDown"),
                ("Worse than the weakest by", "seFactor"),
            ]
        )
        + _hint(
            "seHint",
            "The product is exact: ten fractions of 999/1000 multiply to 999<sup>10</sup> over "
            "1000<sup>10</sup>, and no decimal is taken until the last digit is printed. Every "
            "dependency is a serial one &mdash; the request needs all of them.",
        )
    )

    script = _CORE_JS + r"""
  var chainIn = document.getElementById('seChain'), extraS = document.getElementById('seExtra');
  var extraSel = document.getElementById('seExtraA');
  var plot = document.getElementById('seChainPlot'), table = document.getElementById('seTable');
  var status = document.getElementById('seStatus');

  function redraw() {
    var extra = +extraS.value;
    document.getElementById('seExtraOut').textContent = extra === 0 ? 'none' : '+' + extra;
    var typed = parseChain(chainIn.value);
    if (typed === null) {
      table.innerHTML = '';
      plot.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">no chain to multiply</text>';
      status.innerHTML = '<span class="tone-red">That is not a list of availabilities.</span> Type '
        + 'percentages separated by commas, such as 99.9, 99.95, 99.99.';
      ['seA', 'sePct', 'seNines', 'seWeak', 'seDown', 'seFactor'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      return;
    }
    var bolt = Rparse(extraSel.value), list = typed.slice(), i;
    for (i = 0; i < extra; i += 1) list.push(bolt);

    var running = [], acc = R(1n, 1n), weak = list[0];
    for (i = 0; i < list.length; i += 1) {
      acc = Rmul(acc, list[i]);
      running.push(acc);
      if (Rcmp(list[i], weak) < 0) weak = list[i];
    }
    var total = availSeries(list), month = periodSeconds('month');
    var agrees = Requ(total, acc);
    /* A chain of perfect components has no downtime to compare, so the ratio
       is 0/0 rather than large; the page says so instead of dividing. */
    var weakDown = Rsub(R(1n, 1n), weak);
    var factor = Rzero(weakDown) ? null : Rdiv(Rsub(R(1n, 1n), total), weakDown);

    document.getElementById('seA').textContent = Rfixed(total, 7);
    document.getElementById('sePct').textContent = Rpct(total, 5);
    document.getElementById('seNines').textContent = ninesOf(total) + ' nine' + (ninesOf(total) === 1 ? '' : 's');
    document.getElementById('seWeak').textContent = Rpct(weak, 4);
    document.getElementById('seDown').textContent = durText(downtimeSeconds(total, month));
    document.getElementById('seFactor').textContent = factor === null
      ? 'nothing is down' : Rfixed(factor, 2) + '&times; the downtime';

    var rows = '';
    for (i = 0; i < list.length; i += 1) {
      rows += '<tr><td>' + (i + 1) + (i >= typed.length ? ' <span class="tone-muted">(bolted on)</span>' : '')
        + '</td><td class="tt">' + Rtext(list[i]) + '</td><td>' + Rpct(list[i], 4) + '</td>'
        + '<td class="tone-cyan">' + Rpct(running[i], 5) + '</td><td>'
        + durText(downtimeSeconds(running[i], month)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>dependency</th><th>its A, exactly</th><th>its A</th>'
      + '<th>running product</th><th>downtime a month</th></tr></thead><tbody>' + rows + '</tbody>';

    var n = list.length, lo = parseFloat(Rfixed(total, 8)), span = Math.max(1e-8, 1 - lo);
    var x0 = 18, w = 486, step = n > 1 ? w / (n - 1) : 0;
    function ypx(v) { return 22 + (1 - (parseFloat(Rfixed(v, 8)) - lo) / span) * 110; }
    var pts = '', s = '';
    for (i = 0; i < n; i += 1) {
      var px = x0 + i * step, py = ypx(running[i]);
      pts += (i ? ' ' : '') + px + ',' + py;
      s += '<rect x="' + (px - 5) + '" y="150" width="10" height="18" rx="2" fill="var('
        + (Requ(list[i], weak) ? '--amber' : '--line-strong') + ')" opacity="0.9" />';
    }
    s = '<polyline points="' + pts + '" fill="none" stroke="var(--cyan)" stroke-width="2" />' + s;
    for (i = 0; i < n; i += 1) {
      s += '<circle cx="' + (x0 + i * step) + '" cy="' + ypx(running[i]) + '" r="2.5" fill="var(--cyan)" />';
    }
    s += '<line x1="0" y1="' + ypx(weak) + '" x2="520" y2="' + ypx(weak)
      + '" stroke="var(--amber)" stroke-width="1" stroke-dasharray="4 3" />'
      + '<text x="518" y="' + (ypx(weak) - 4) + '" font-size="10" text-anchor="end" fill="var(--amber)">'
      + 'the weakest link alone, ' + Rpct(weak, 3) + '</text>'
      + '<text x="0" y="14" font-size="10" fill="var(--muted)">running product, top = 100%, bottom = '
      + Rpct(total, 4) + '</text>'
      + '<text x="0" y="184" font-size="10" fill="var(--red)">the line ends BELOW the dashed one: '
      + n + ' dependencies are worse than the worst of them</text>';
    plot.innerHTML = s;

    status.innerHTML = (agrees ? '' : '<span class="tone-red">The running product and availSeries disagree.</span> ')
      + '<strong>' + n + '</strong> serial dependencies, the weakest at ' + Rpct(weak, 4)
      + ', multiply to <strong>' + Rpct(total, 5) + '</strong> &mdash; '
      + durText(downtimeSeconds(total, month)) + ' a month against the weakest link&rsquo;s own '
      + durText(downtimeSeconds(weak, month)) + '. '
      + (factor === null
          ? 'Every component you gave is perfectly available, so there is no downtime to multiply; '
            + 'lower one of them below 100% and the product falls immediately.'
          : 'That is <strong>' + Rfixed(factor, 2) + '&times;</strong> the downtime of the single '
            + 'worst component, so &ldquo;as available as the weakest link&rdquo; is not merely '
            + 'optimistic, it is the wrong shape: each dependency multiplies what is left, and '
            + 'adding a 99.99% service to this chain still makes it worse.');
  }

  chainIn.addEventListener('input', redraw);
  extraS.addEventListener('input', redraw);
  extraSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Series: availability multiplies",
        subtitle="Ten dependencies at 99.9% are 99.0%, which is worse than any one of them",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Build the chain"),
        panel_intro=cfg.get(
            "panel_intro",
            "Type the dependencies a request needs, then bolt more on. The product is computed "
            "from the fractions you gave, one multiplication per dependency.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - parallel
# ---------------------------------------------------------------------------


def _parallel(cfg):
    paths = int(cfg.get("paths", 2))
    each = cfg.get("each", "99/100")
    failover = int(cfg.get("failover_seconds", 30))
    events = int(cfg.get("events_per_year", 12))

    markup = (
        _toolbar(
            "Redundancy multiplies up",
            "1 &minus; &prod;(1 &minus; A&#7522;), and then the failover bill",
            [("green", "a path is up"), ("red", "all paths down together"), ("amber", "failover time")],
        )
        + _stage(
            _svg("plTracks", "0 0 520 150", "One track per redundant path, and the combined track beneath them.")
        )
        + _table("plTable")
        + _banner("plStatus")
    )
    controls = (
        _range("plPaths", "Redundant paths", 1, 6, paths)
        + _select("plEach", "Each path&rsquo;s availability", _TARGETS, each)
        + _range("plFailover", "Failover time (seconds)", 0, 300, failover)
        + _range("plEvents", "Failover events per year", 0, 104, events)
        + _kpis(
            [
                ("Ideal A (instant failover)", "plIdeal"),
                ("Ideal nines", "plIdealN"),
                ("Charged for failover", "plCharge"),
                ("A after the charge", "plAdj"),
                ("Nines after the charge", "plAdjN"),
                ("Downtime per year", "plDown"),
            ]
        )
        + _hint(
            "plHint",
            "The parallel formula assumes the paths fail independently and that the switch between "
            "them is instant. The first assumption is the next lesson; the second is this slider, "
            "and it is usually the larger of the two errors.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('plPaths'), eachSel = document.getElementById('plEach');
  var foS = document.getElementById('plFailover'), evS = document.getElementById('plEvents');
  var tracks = document.getElementById('plTracks'), table = document.getElementById('plTable');
  var status = document.getElementById('plStatus');

  function redraw() {
    var n = +nS.value, fo = +foS.value, ev = +evS.value;
    document.getElementById('plPathsOut').textContent = n === 1 ? '1 (no redundancy)' : n;
    document.getElementById('plFailoverOut').textContent = fo + ' s';
    document.getElementById('plEventsOut').textContent = ev + ' a year';

    var a = Rparse(eachSel.value), year = periodSeconds('year'), list = [], i;
    for (i = 0; i < n; i += 1) list.push(a);
    var out = parallelWithFailover(list, R(BigInt(fo), 1n), R(BigInt(ev), 1n), year);

    document.getElementById('plIdeal').textContent = RpctAuto(out.ideal);
    document.getElementById('plIdealN').textContent = ninesOf(out.ideal) + ' nines';
    document.getElementById('plCharge').textContent = durText(R(BigInt(fo) * BigInt(ev), 1n)) + ' a year';
    document.getElementById('plAdj').textContent = RpctAuto(out.adjusted);
    document.getElementById('plAdjN').textContent = ninesOf(out.adjusted) + ' nines';
    document.getElementById('plDown').textContent = durText(downtimeSeconds(out.adjusted, year));

    var rows = '', k;
    for (k = 1; k <= 6; k += 1) {
      var sub = [];
      for (i = 0; i < k; i += 1) sub.push(a);
      var r2 = parallelWithFailover(sub, R(BigInt(fo), 1n), R(BigInt(ev), 1n), year);
      rows += '<tr' + (k === n ? ' class="tone-cyan"' : '') + '><td>' + k + '</td>'
        + '<td class="tt">' + Rtext(Rsub(R(1n, 1n), r2.ideal)) + '</td>'
        + '<td>' + RpctAuto(r2.ideal) + '</td>'
        + '<td>' + durText(downtimeSeconds(r2.ideal, year)) + '</td>'
        + '<td class="tone-amber">' + RpctAuto(r2.adjusted) + '</td>'
        + '<td>' + durText(downtimeSeconds(r2.adjusted, year)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>paths</th><th>P(all down), exactly</th><th>ideal A</th>'
      + '<th>ideal downtime a year</th><th>A with failover charged</th><th>real downtime a year</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var s = '', downShare = Rnum(Rsub(R(1n, 1n), a));
    for (i = 0; i < n; i += 1) {
      var y = 16 + i * 20;
      var dx = 40 + (i * 97) % 400, dw = Math.max(3, 480 * downShare);
      s += '<text x="0" y="' + (y + 11) + '" font-size="10" fill="var(--muted)">path ' + (i + 1) + '</text>'
        + '<rect x="44" y="' + y + '" width="472" height="13" rx="2" fill="var(--green)" opacity="0.55" />'
        + '<rect x="' + dx + '" y="' + y + '" width="' + dw + '" height="13" fill="var(--red)" opacity="0.9" />';
    }
    var cy = 24 + n * 20;
    s += '<text x="0" y="' + (cy + 11) + '" font-size="10" fill="var(--muted)">served</text>'
      + '<rect x="44" y="' + cy + '" width="472" height="15" rx="2" fill="var(--green)" opacity="0.85" />';
    if (n === 1) {
      s += '<rect x="40" y="' + cy + '" width="' + Math.max(3, 480 * downShare) + '" height="15" fill="var(--red)" />';
    }
    var fw = Math.max(1.5, 472 * Rnum(out.charge) * 400);
    s += '<rect x="44" y="' + cy + '" width="' + Math.min(472, fw) + '" height="15" fill="var(--amber)" opacity="0.9" />'
      + '<text x="0" y="' + (cy + 34) + '" font-size="10" fill="var(--amber)">the amber sliver is the '
      + durText(R(BigInt(fo) * BigInt(ev), 1n)) + ' a year spent switching, magnified 400&times; to be visible</text>'
      + '<text x="0" y="' + (cy + 48) + '" font-size="10" fill="var(--muted)">the red gaps are drawn at '
      + 'different offsets because independence is exactly the claim that they do not line up</text>';
    tracks.innerHTML = s;

    var dominates = Rcmp(out.charge, Rsub(R(1n, 1n), out.ideal)) > 0;
    status.innerHTML = '<strong>' + n + '</strong> path' + (n === 1 ? '' : 's') + ' at ' + Rpct(a, 4)
      + ' each are down together with probability <strong>' + Rtext(Rsub(R(1n, 1n), out.ideal))
      + '</strong>, so the ideal availability is <strong>' + RpctAuto(out.ideal) + '</strong> &mdash; '
      + durText(downtimeSeconds(out.ideal, year)) + ' a year. But ' + ev + ' failovers at ' + fo
      + ' s each is ' + durText(R(BigInt(fo) * BigInt(ev), 1n)) + ' of downtime that the formula does not '
      + 'contain, bringing the real figure to <strong>' + Rpct(out.adjusted, 6) + '</strong> ('
      + durText(downtimeSeconds(out.adjusted, year)) + ' a year). '
      + (dominates
          ? '<span class="tone-amber">The failover time is now the larger term:</span> adding a further path '
            + 'improves the part that is already small and leaves the part that is not untouched.'
          : 'The failover charge is still the smaller term here &mdash; raise the path count or the event '
            + 'rate and watch it overtake the thing redundancy was bought to fix.');
  }

  [nS, foS, evS].forEach(function (el) { el.addEventListener('input', redraw); });
  eachSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Parallel: redundancy, and its bill",
        subtitle="Two 99% paths give 99.99% — if they are independent and the switch is free",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Add paths, then charge for the switch"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both figures are computed from the same fractions: the ideal one from "
            "1 &minus; &prod;(1 &minus; A&#7522;), and the real one after subtracting the seconds "
            "spent failing over.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - kofn
# ---------------------------------------------------------------------------


def _kofn(cfg):
    n = int(cfg.get("n", 5))
    k = int(cfg.get("k", 3))
    each = cfg.get("each", "99/100")

    markup = (
        _toolbar(
            "k of n is a binomial tail",
            "and at k = n it is the series product, at k = 1 the parallel one",
            [("cyan", "terms that count (j &ge; k)"), ("muted", "terms that do not"), ("purple", "the identities")],
        )
        + _stage(_svg("knBars", "0 0 520 180", "The binomial terms for j nodes up, with the tail from k highlighted."))
        + _table("knTable")
        + _banner("knStatus")
    )
    controls = (
        _range("knN", "Replicas n", 1, 12, n)
        + _range("knK", "How many must be up, k", 1, 12, k)
        + _select("knEach", "Each replica&rsquo;s availability", _TARGETS, each)
        + _kpis(
            [
                ("A(k of n)", "knA"),
                ("Nines", "knNines"),
                ("Downtime per year", "knDown"),
                ("k = n against the series product", "knSeries"),
                ("k = 1 against the parallel form", "knParallel"),
                ("All n + 1 terms sum to", "knSum"),
            ]
        )
        + _hint(
            "knHint",
            "The coefficients are C(n, j) in BigInt, so the twelfth row of Pascal&rsquo;s triangle is "
            "exact and so is every term built on it. Raising n helps only while k stays put: a quorum "
            "that grows with the fleet is a chain wearing a redundancy costume.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('knN'), kS = document.getElementById('knK');
  var eachSel = document.getElementById('knEach');
  var bars = document.getElementById('knBars'), table = document.getElementById('knTable');
  var status = document.getElementById('knStatus');

  function redraw() {
    var n = +nS.value, k = Math.min(+kS.value, n);
    document.getElementById('knNOut').textContent = n;
    document.getElementById('knKOut').textContent = k + (k === +kS.value ? '' : ' (capped at n)');
    var a = Rparse(eachSel.value), year = periodSeconds('year'), i;

    var value = availKofN(a, k, n), terms = kofnTerms(a, n), total = kofnTotal(a, n);
    var copies = [];
    for (i = 0; i < n; i += 1) copies.push(a);
    var seriesSame = Requ(availKofN(a, n, n), availSeries(copies));
    var parallelSame = Requ(availKofN(a, 1, n), availParallel(copies));

    document.getElementById('knA').textContent = RpctAuto(value);
    document.getElementById('knNines').textContent = ninesOf(value) + ' nines';
    document.getElementById('knDown').textContent = durText(downtimeSeconds(value, year));
    document.getElementById('knSeries').textContent = seriesSame ? 'identical' : 'DISAGREE';
    document.getElementById('knParallel').textContent = parallelSame ? 'identical' : 'DISAGREE';
    document.getElementById('knSum').textContent = Rtext(total);

    var rows = '', tail = R(0n, 1n);
    for (i = n; i >= 0; i -= 1) {
      if (i >= k) tail = Radd(tail, terms[i].term);
      rows += '<tr' + (i >= k ? ' class="tone-cyan"' : ' class="tone-muted"') + '><td>' + i + '</td>'
        + '<td>' + group(terms[i].c) + '</td>'
        + '<td class="tt">A<sup>' + i + '</sup>(1&minus;A)<sup>' + (n - i) + '</sup></td>'
        + '<td>' + Rfixed(terms[i].term, 8) + '</td>'
        + '<td>' + (i >= k ? Rfixed(tail, 8) : '&mdash;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>j up</th><th>C(n, j)</th><th>term</th><th>probability</th>'
      + '<th>tail from j to n</th></tr></thead><tbody>' + rows + '</tbody>';

    var top = 0;
    for (i = 0; i <= n; i += 1) top = Math.max(top, parseFloat(Rfixed(terms[i].term, 8)));
    var bw = 500 / (n + 1), s = '';
    for (i = 0; i <= n; i += 1) {
      var h = top > 0 ? (parseFloat(Rfixed(terms[i].term, 8)) / top) * 112 : 0;
      var x = 10 + i * bw;
      s += '<rect x="' + (x + 2) + '" y="' + (134 - h) + '" width="' + (bw - 4) + '" height="' + Math.max(1, h)
        + '" rx="2" fill="var(' + (i >= k ? '--cyan' : '--line-strong') + ')" opacity="'
        + (i >= k ? '0.9' : '0.5') + '" />'
        + '<text x="' + (x + bw / 2) + '" y="148" font-size="10" text-anchor="middle" fill="var(--muted)">'
        + i + '</text>';
    }
    var cut = 10 + k * bw;
    s += '<line x1="' + cut + '" y1="14" x2="' + cut + '" y2="138" stroke="var(--purple)" stroke-width="1.5" stroke-dasharray="4 3" />'
      + '<text x="' + (cut + 4) + '" y="24" font-size="10" fill="var(--purple)">k = ' + k + '</text>'
      + '<text x="10" y="164" font-size="10" fill="var(--muted)">bars are P(exactly j replicas up); '
      + 'the quorum is the shaded tail, summed exactly</text>'
      + '<text x="10" y="176" font-size="10" fill="var(--purple)">k = n would be '
      + RpctAuto(availKofN(a, n, n)) + ', k = 1 would be ' + RpctAuto(availKofN(a, 1, n)) + '</text>';
    bars.innerHTML = s;

    var single = a, side = Rcmp(value, single);
    status.innerHTML = '<strong>' + k + ' of ' + n + '</strong> at ' + Rpct(a, 4) + ' each is <strong>'
      + RpctAuto(value) + '</strong>, from ' + (n - k + 1) + ' binomial term'
      + ((n - k + 1) === 1 ? '' : 's') + ' summed exactly. '
      + (side > 0
          ? 'That is better than one replica alone (' + Rpct(single, 4) + ').'
          : (side === 0
              ? 'That is exactly one replica alone (' + Rpct(single, 4) + '), which is what k = n = 1 '
                + 'means: there is no redundancy here to compose.'
              : '<span class="tone-red">That is WORSE than one replica alone</span> (' + Rpct(single, 4)
                + ') &mdash; needing all of them means every one of them is a dependency, and '
                + n + ' dependencies multiply down.'))
      + ' The two edges of this formula are the other two lessons: at k = n it returns '
      + RpctAuto(availKofN(a, n, n)) + ', which is what availSeries returns for the same n copies, and at '
      + 'k = 1 it returns ' + RpctAuto(availKofN(a, 1, n)) + ', which is what availParallel returns. '
      + (seriesSame && parallelSame
          ? 'Both agree here as exact fractions, which is the check that the binomial coefficients are right.'
          : '<span class="tone-red">One of those identities has failed, which means this page is wrong.</span>')
      + ' The ' + (n + 1) + ' terms sum to ' + Rtext(total) + '.';
  }

  [nS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  eachSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Quorums: k of n",
        subtitle="A binomial tail, and the two compositions it collapses to at its edges",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the quorum"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every term is C(n, j)A&#7469;(1 &minus; A)&#8319;&#8315;&#7469; as an exact fraction, "
            "and the answer is their sum from j = k upward.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - correlated
# ---------------------------------------------------------------------------


def _correlated(cfg):
    p_parts = int(cfg.get("p_per_10000", 100))
    c_parts = int(cfg.get("c_per_100000", 100))
    axis = int(cfg.get("axis_per_100000", 2000))

    markup = (
        _toolbar(
            "The common cause",
            "P(both down) = c + (1 &minus; c)p&sup2;, and c is a probability, never a count",
            [("cyan", "independence, p&sup2;"), ("red", "with the common cause"), ("purple", "where redundancy stops paying")],
        )
        + _stage(_svg("ccCurves", "0 0 520 200", "P(both down) against the common-cause probability, with the independent value as a flat line."))
        + _table("ccTable")
        + _banner("ccStatus")
    )
    controls = (
        _range("ccP", "Per-node failure probability p (parts per 10 000)", 1, 2000, p_parts)
        + _range("ccC", "Common-cause probability c (parts per 100 000)", 0, 5000, c_parts)
        + _range("ccAxis", "Draw c out to (parts per 100 000)", 200, 20000, axis, 100)
        + _kpis(
            [
                ("p, exactly", "ccPval"),
                ("Independence promises p&sup2;", "ccInd"),
                ("P(both down), really", "ccBoth"),
                ("Times worse than promised", "ccRatio"),
                ("Redundancy buys nothing at c =", "ccBreak"),
                ("Pair availability", "ccPair"),
            ]
        )
        + _hint(
            "ccHint",
            "Same rack, same deploy, same expired certificate, same configuration push. A common "
            "cause does not need to be likely to dominate: it only needs to be likelier than p&sup2;, "
            "and p&sup2; is very small indeed.",
        )
    )

    script = _CORE_JS + r"""
  var pS = document.getElementById('ccP'), cS = document.getElementById('ccC');
  var axS = document.getElementById('ccAxis');
  var curves = document.getElementById('ccCurves'), table = document.getElementById('ccTable');
  var status = document.getElementById('ccStatus');

  function redraw() {
    var pi = +pS.value, ci = +cS.value, ax = +axS.value;
    var p = R(BigInt(pi), 10000n), c = R(BigInt(ci), 100000n), axis = R(BigInt(ax), 100000n);
    document.getElementById('ccPOut').textContent = Rfixed(Rmul(p, R(100n, 1n)), 2) + '%';
    document.getElementById('ccCOut').textContent = Rfixed(Rmul(c, R(100n, 1n)), 3) + '%';
    document.getElementById('ccAxisOut').textContent = Rfixed(Rmul(axis, R(100n, 1n)), 2) + '%';

    var ind = Rmul(p, p), both = pairBothDown(c, p), brk = correlatedBreakEven(p);
    var ratio = Rzero(ind) ? null : Rdiv(both, ind);

    document.getElementById('ccPval').textContent = Rtext(p);
    document.getElementById('ccInd').textContent = Rtext(ind);
    document.getElementById('ccBoth').textContent = Rfixed(both, 8);
    document.getElementById('ccRatio').textContent = ratio === null ? '&mdash;' : Rfixed(ratio, 2) + '&times;';
    document.getElementById('ccBreak').textContent = Rtext(brk) + ' = ' + Rfixed(brk, 6);
    document.getElementById('ccPair').textContent = Rpct(Rsub(R(1n, 1n), both), 5);

    var marks = [R(0n, 1n), Rdiv(ind, R(10n, 1n)), ind, c, brk, axis], rows = '', i;
    var labels = ['independent (c = 0)', 'a tenth of p&sup2;', 'exactly p&sup2;',
                  'your c', 'the break-even c = p/(1 + p)', 'the right-hand edge'];
    for (i = 0; i < marks.length; i += 1) {
      var v = pairBothDown(marks[i], p);
      rows += '<tr' + (i === 3 ? ' class="tone-red"' : '') + '><td>' + labels[i] + '</td>'
        + '<td class="tt">' + Rfixed(marks[i], 8) + '</td>'
        + '<td>' + Rfixed(v, 8) + '</td>'
        + '<td>' + Rfixed(Rdiv(v, ind), 2) + '&times;</td>'
        + '<td>' + Rfixed(redundancyGain(marks[i], p), 2) + '&times;</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>common cause</th><th>c</th><th>P(both down)</th>'
      + '<th>against p&sup2;</th><th>better than one machine by</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var top = pairBothDown(axis, p), tv = parseFloat(Rfixed(top, 10)) || 1e-9;
    function xp(v) { return 30 + (parseFloat(Rfixed(v, 10)) / (parseFloat(Rfixed(axis, 10)) || 1e-9)) * 470; }
    function yp(v) { return 150 - (parseFloat(Rfixed(v, 10)) / tv) * 120; }
    var pts = '', steps = 60;
    for (i = 0; i <= steps; i += 1) {
      var cc = Rmul(axis, R(BigInt(i), BigInt(steps)));
      pts += (i ? ' ' : '') + xp(cc) + ',' + yp(pairBothDown(cc, p));
    }
    var s = '<line x1="30" y1="150" x2="510" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="30" y1="18" x2="30" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="30" y1="' + yp(ind) + '" x2="510" y2="' + yp(ind)
      + '" stroke="var(--cyan)" stroke-width="1.5" stroke-dasharray="5 3" />'
      + '<text x="34" y="' + (yp(ind) - 5) + '" font-size="10" fill="var(--cyan)">what independence promises: p&sup2; = '
      + Rtext(ind) + '</text>'
      + '<polyline points="' + pts + '" fill="none" stroke="var(--red)" stroke-width="2" />';
    if (Rcmp(brk, axis) <= 0) {
      s += '<line x1="' + xp(brk) + '" y1="18" x2="' + xp(brk) + '" y2="150" stroke="var(--purple)" '
        + 'stroke-width="1" stroke-dasharray="3 3" />'
        + '<text x="' + (xp(brk) + 4) + '" y="30" font-size="10" fill="var(--purple)">c = p/(1+p): the pair '
        + 'is now no better than one machine</text>';
    }
    if (Rcmp(c, axis) <= 0) {
      s += '<circle cx="' + xp(c) + '" cy="' + yp(both) + '" r="4" fill="var(--red)" />'
        + '<text x="' + Math.min(430, xp(c) + 8) + '" y="' + (yp(both) - 6) + '" font-size="10" fill="var(--red)">'
        + 'c = ' + Rfixed(c, 5) + ' &rarr; ' + Rfixed(both, 7) + '</text>';
    }
    s += '<text x="30" y="166" font-size="10" fill="var(--muted)">c = 0</text>'
      + '<text x="510" y="166" font-size="10" text-anchor="end" fill="var(--muted)">c = ' + Rfixed(axis, 5) + '</text>'
      + '<text x="30" y="186" font-size="10" fill="var(--muted)">vertical axis: P(both machines down at once), '
      + '0 at the line to ' + Rfixed(top, 7) + ' at the top</text>'
      + '<text x="30" y="196" font-size="10" fill="var(--muted)">the curve leaves the dashed line immediately, '
      + 'because c is added whole and only p&sup2; is discounted</text>';
    curves.innerHTML = s;

    var swamped = Rcmp(c, ind) > 0;
    status.innerHTML = 'Two machines that each fail with probability ' + Rtext(p)
      + ' are down together with probability <strong>' + Rfixed(both, 8) + '</strong>, not the '
      + Rtext(ind) + ' that independence promises &mdash; <strong>' + (ratio === null ? '&mdash;' : Rfixed(ratio, 1))
      + '&times;</strong> as often. '
      + (swamped
          ? '<span class="tone-red">The common cause has swamped the independent term:</span> c = '
            + Rfixed(c, 6) + ' is larger than p&sup2; = ' + Rtext(ind) + ', so almost every simultaneous '
            + 'outage is the shared cause and the second machine is barely involved.'
          : 'Here c is still below p&sup2; = ' + Rtext(ind) + ', so independence is nearly right &mdash; '
            + 'raise c past that point and the second machine stops mattering.')
      + ' Redundancy buys nothing at all once c reaches <strong>' + Rtext(brk) + '</strong> = '
      + Rfixed(brk, 6) + ', where the pair is exactly as available as one machine; the whole argument '
      + 'for a second machine lives below that number.';
  }

  [pS, cS, axS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Correlated failure",
        subtitle="A 0.1% common cause swamps a pair whose independent product is 10⁻⁴",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Move the common cause up from zero"),
        panel_intro=cfg.get(
            "panel_intro",
            "c is the probability that one event takes both machines at once. It is a probability "
            "between 0 and 1 &mdash; never a number of servers &mdash; and everything else on this "
            "page is computed from it exactly.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - budget
# ---------------------------------------------------------------------------


def _budget(cfg):
    slo = cfg.get("slo", "999/1000")
    rps = int(cfg.get("rps", 1000))
    minutes = int(cfg.get("incident_minutes", 30))
    severity = int(cfg.get("severity_pct", 100))
    count = int(cfg.get("incidents", 1))

    markup = (
        _toolbar(
            "The error budget",
            "(1 &minus; SLO) &times; requests, spent in failed requests and not in minutes",
            [("green", "budget left"), ("red", "burned"), ("amber", "over budget")],
        )
        + _stage(_svg("ebBar", "0 0 520 150", "The month's error budget as a bar, drained by each incident."))
        + _table("ebTable")
        + _banner("ebStatus")
    )
    controls = (
        _select("ebSlo", "The SLO (successful requests)", _TARGETS, slo)
        + _range("ebRps", "Requests per second", 10, 5000, rps)
        + _range("ebDur", "Incident duration (minutes)", 1, 600, minutes)
        + _range("ebSev", "Failed fraction during it (per cent)", 1, 100, severity)
        + _range("ebCount", "Incidents like it this month", 0, 12, count)
        + _kpis(
            [
                ("Requests this month", "ebReq"),
                ("Budget, in failed requests", "ebBudget"),
                ("One incident burns", "ebBurn"),
                ("Share of the budget", "ebShare"),
                ("Budget left", "ebLeft"),
                ("Full outage the budget pays for", "ebFull"),
            ]
        )
        + _hint(
            "ebHint",
            "An SLO is a ratio of requests, so an incident costs duration &times; failed fraction. "
            "Measuring it on uptime instead makes a half-broken hour look identical to a dead one, "
            "and they differ by a factor of two in what they actually spend.",
        )
    )

    script = _CORE_JS + r"""
  var sloSel = document.getElementById('ebSlo'), rpsS = document.getElementById('ebRps');
  var durS = document.getElementById('ebDur'), sevS = document.getElementById('ebSev');
  var cntS = document.getElementById('ebCount');
  var bar = document.getElementById('ebBar'), table = document.getElementById('ebTable');
  var status = document.getElementById('ebStatus');

  function redraw() {
    var rps = +rpsS.value, mins = +durS.value, sev = +sevS.value, count = +cntS.value;
    document.getElementById('ebRpsOut').textContent = group(BigInt(rps)) + ' rps';
    document.getElementById('ebDurOut').textContent = mins + ' min';
    document.getElementById('ebSevOut').textContent = sev + '%';
    document.getElementById('ebCountOut').textContent = count;

    var slo = Rparse(sloSel.value), month = periodSeconds('month');
    var rate = R(BigInt(rps), 1n), dur = R(BigInt(mins) * 60n, 1n), severity = R(BigInt(sev), 100n);
    var requests = Rmul(rate, month);
    var budget = budgetRequests(slo, requests);
    var burn = incidentBurn(rate, dur, severity);
    var spent = Rmul(burn, R(BigInt(count), 1n));
    var share = Rzero(budget) ? R(0n, 1n) : Rdiv(spent, budget);
    var left = Rsub(budget, spent);
    var full = budgetSeconds(slo, month);

    document.getElementById('ebReq').textContent = group(requests.n / requests.d);
    document.getElementById('ebBudget').textContent = group(budget.n / budget.d);
    document.getElementById('ebBurn').textContent = group(burn.n / burn.d);
    document.getElementById('ebShare').textContent = Rpct(share, 2);
    document.getElementById('ebLeft').textContent = Rcmp(left, R(0n, 1n)) < 0
      ? '&minus;' + group((Rsub(R(0n, 1n), left)).n / left.d) : group(left.n / left.d);
    document.getElementById('ebFull').textContent = durText(full);

    var sevs = [10, 25, 50, 100], rows = '', i;
    for (i = 0; i < sevs.length; i += 1) {
      var sv = R(BigInt(sevs[i]), 100n);
      var b = incidentBurn(rate, dur, sv);
      var sh = Rzero(budget) ? R(0n, 1n) : Rdiv(b, budget);
      /* the minutes at this severity that would spend the whole budget */
      var exhaust = Rdiv(budget, Rmul(Rmul(rate, sv), R(60n, 1n)));
      rows += '<tr' + (sevs[i] === sev ? ' class="tone-red"' : '') + '><td>' + sevs[i] + '% of requests failing</td>'
        + '<td>' + group(b.n / b.d) + '</td><td>' + Rpct(sh, 2) + '</td>'
        + '<td>' + Rfixed(exhaust, 1) + ' min</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>severity of a ' + mins + '-minute incident</th>'
      + '<th>failed requests</th><th>share of the month&rsquo;s budget</th>'
      + '<th>minutes at this severity that spend it all</th></tr></thead><tbody>' + rows + '</tbody>';

    var frac = Math.min(1, parseFloat(Rfixed(share, 6)));
    var over = Rcmp(spent, budget) > 0;
    var s = '<text x="0" y="14" font-size="11" fill="var(--muted)">the month&rsquo;s budget: '
      + group(budget.n / budget.d) + ' failed requests</text>'
      + '<rect x="0" y="24" width="512" height="30" rx="4" fill="var(--green)" opacity="0.35" />';
    var used = 512 * frac, seg = count > 0 ? used / count : 0;
    for (i = 0; i < count && i < 12; i += 1) {
      s += '<rect x="' + (i * seg) + '" y="24" width="' + Math.max(0.6, seg - 1) + '" height="30" fill="var('
        + (over ? '--amber' : '--red') + ')" opacity="0.85" />';
    }
    s += '<text x="4" y="70" font-size="10" fill="var(' + (over ? '--amber' : '--red') + ')">'
      + count + ' incident' + (count === 1 ? '' : 's') + ' &times; ' + group(burn.n / burn.d)
      + ' = ' + group(spent.n / spent.d) + ' requests, ' + Rpct(share, 2) + ' of it</text>'
      + '<line x1="0" y1="86" x2="512" y2="86" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="104" font-size="10" fill="var(--muted)">the same budget as time, if everything '
      + 'failed at once: ' + durText(full) + ' a month</text>'
      + '<rect x="0" y="112" width="512" height="12" rx="3" fill="var(--line-strong)" opacity="0.5" />'
      + '<rect x="0" y="112" width="'
      + Math.max(1, Math.min(512, 512 * (Rnum(Rmul(dur, R(BigInt(count), 1n))) / Math.max(1, Rnum(full)))))
      + '" height="12" rx="3" fill="var(--purple)" opacity="0.9" />'
      + '<text x="0" y="140" font-size="10" fill="var(--purple)">' + (count * mins) + ' minutes of incident '
      + 'against ' + durText(full) + ' of full outage &mdash; the two bars agree only at 100% severity</text>';
    bar.innerHTML = s;

    status.innerHTML = 'An SLO of <strong>' + Rpct(slo, 4) + '</strong> over ' + group(requests.n / requests.d)
      + ' requests is a budget of <strong>' + group(budget.n / budget.d) + '</strong> failed requests a month, '
      + 'which is <strong>' + durText(full) + '</strong> of complete outage. '
      + count + ' incident' + (count === 1 ? '' : 's') + ' of ' + mins + ' minutes at ' + sev
      + '% severity burn' + (count === 1 ? 's' : '') + ' <strong>' + group(spent.n / spent.d)
      + '</strong>, or <strong>' + Rpct(share, 2)
      + '</strong> of it. '
      + (over
          ? '<span class="tone-amber">That is over budget.</span> Everything after this point is a policy '
            + 'question, not an arithmetic one.'
          : 'That leaves ' + group(left.n / left.d) + ' for the rest of the month.')
      + ' Halve the severity and the same outage costs half as much &mdash; which is the difference '
      + 'between an SLO measured on requests and one measured on the clock.';
  }

  [rpsS, durS, sevS, cntS].forEach(function (el) { el.addEventListener('input', redraw); });
  sloSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Error budgets",
        subtitle="What an incident actually spends, in failed requests",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the SLO and the incident"),
        panel_intro=cfg.get(
            "panel_intro",
            "The budget is (1 &minus; SLO) &times; the requests in the period, and an incident spends "
            "its duration times the fraction of requests it failed. Both are exact counts.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - retry
# ---------------------------------------------------------------------------


def _retry(cfg):
    p_pct = int(cfg.get("p_pct", 10))
    retries = int(cfg.get("retries", 2))
    load = int(cfg.get("rps", 500))

    markup = (
        _toolbar(
            "Retries multiply load",
            "(1 &minus; p&#8319;&#8314;&sup1;) &divide; (1 &minus; p) attempts per request",
            [("cyan", "the first attempt"), ("amber", "retries"), ("red", "still failed")],
        )
        + _stage(_svg("rtLadder", "0 0 520 176", "One bar per attempt, its height the probability that the attempt is ever made."))
        + _table("rtTable")
        + _banner("rtStatus")
    )
    controls = (
        _range("rtP", "Failure probability p (per cent)", 0, 99, p_pct)
        + _range("rtR", "Retries after the first attempt", 0, 6, retries)
        + _range("rtLoad", "Requests offered per second", 10, 5000, load)
        + _kpis(
            [
                ("Expected attempts", "rtAtt"),
                ("Success probability", "rtSucc"),
                ("Still fails", "rtFail"),
                ("Amplification", "rtAmp"),
                ("Attempts per second", "rtAmpLoad"),
                ("Share of load that is retry", "rtDup"),
            ]
        )
        + _hint(
            "rtHint",
            "The amplification is a geometric sum, so it rises with p: the policy costs least when "
            "the service is healthy and most at the moment the service can least afford it. As "
            "p &rarr; 1 it tends to r + 1, which is the whole retry budget spent on every request.",
        )
    )

    script = _CORE_JS + r"""
  var pS = document.getElementById('rtP'), rS = document.getElementById('rtR');
  var loadS = document.getElementById('rtLoad');
  var ladder = document.getElementById('rtLadder'), table = document.getElementById('rtTable');
  var status = document.getElementById('rtStatus');

  function redraw() {
    var pc = +pS.value, r = +rS.value, lam = +loadS.value;
    document.getElementById('rtPOut').textContent = pc + '%';
    document.getElementById('rtROut').textContent = r === 0 ? 'none' : r;
    document.getElementById('rtLoadOut').textContent = group(BigInt(lam)) + ' rps';

    var p = R(BigInt(pc), 100n), lambda = R(BigInt(lam), 1n);
    var attempts = retryAttempts(p, r), success = retrySuccess(p, r);
    var lost = Rpow(p, r + 1), amplified = amplifiedLoad(lambda, p, r);

    document.getElementById('rtAtt').textContent = Rfixed(attempts, 4);
    document.getElementById('rtSucc').textContent = Rpct(success, 4);
    document.getElementById('rtFail').textContent = Rtext(lost) + ' = ' + Rfixed(lost, 8);
    document.getElementById('rtAmp').textContent = Rfixed(attempts, 3) + '&times;';
    document.getElementById('rtAmpLoad').textContent = Rfixed(amplified, 1) + ' /s';
    document.getElementById('rtDup').textContent = Rpct(duplicateShare(p, r), 2);

    var rows = '', i, running = R(0n, 1n);
    for (i = 0; i <= r; i += 1) {
      var reach = attemptReach(p, i);
      running = Radd(running, reach);
      rows += '<tr' + (i === 0 ? ' class="tone-cyan"' : ' class="tone-amber"') + '><td>'
        + (i === 0 ? 'the request itself' : 'retry ' + i) + '</td>'
        + '<td class="tt">p<sup>' + i + '</sup> = ' + Rtext(reach) + '</td>'
        + '<td>' + Rfixed(reach, 6) + '</td>'
        + '<td>' + Rfixed(Rmul(lambda, reach), 1) + ' /s</td>'
        + '<td>' + Rfixed(running, 4) + '</td></tr>';
    }
    rows += '<tr class="tone-red"><td>gives up, still failed</td><td class="tt">p<sup>' + (r + 1)
      + '</sup> = ' + Rtext(lost) + '</td><td>' + Rfixed(lost, 6) + '</td><td>'
      + Rfixed(Rmul(lambda, lost), 1) + ' /s</td><td>&mdash;</td></tr>';
    table.innerHTML = '<thead><tr><th>attempt</th><th>P(it is ever made)</th><th>as a decimal</th>'
      + '<th>at ' + group(BigInt(lam)) + ' rps</th><th>attempts so far</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var bw = 500 / (r + 2), s = '';
    for (i = 0; i <= r; i += 1) {
      var h = parseFloat(Rfixed(attemptReach(p, i), 8)) * 112;
      var x = 10 + i * bw;
      s += '<rect x="' + (x + 3) + '" y="' + (130 - h) + '" width="' + (bw - 6) + '" height="' + Math.max(1, h)
        + '" rx="2" fill="var(' + (i === 0 ? '--cyan' : '--amber') + ')" opacity="0.9" />'
        + '<text x="' + (x + bw / 2) + '" y="144" font-size="10" text-anchor="middle" fill="var(--muted)">'
        + (i === 0 ? 'try' : '+' + i) + '</text>';
    }
    var hx = 10 + (r + 1) * bw, hh = parseFloat(Rfixed(lost, 8)) * 112;
    s += '<rect x="' + (hx + 3) + '" y="' + (130 - hh) + '" width="' + (bw - 6) + '" height="' + Math.max(1, hh)
      + '" rx="2" fill="var(--red)" opacity="0.9" />'
      + '<text x="' + (hx + bw / 2) + '" y="144" font-size="10" text-anchor="middle" fill="var(--red)">lost</text>'
      + '<line x1="10" y1="130" x2="510" y2="130" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="160" font-size="10" fill="var(--muted)">bar height is P(the attempt happens) = '
      + 'p raised to the number of failures before it; the bars sum to the '
      + Rfixed(attempts, 4) + ' attempts every request costs</text>'
      + '<text x="10" y="172" font-size="10" fill="var(--amber)">at p = 0.9 the same policy would cost '
      + Rfixed(retryAttempts(R(9n, 10n), r), 3) + ' attempts, and at p = 0.99, '
      + Rfixed(retryAttempts(R(99n, 100n), r), 3) + '</text>';
    ladder.innerHTML = s;

    status.innerHTML = 'At p = ' + Rtext(p) + ' with ' + r + ' retr' + (r === 1 ? 'y' : 'ies')
      + ', every request costs <strong>' + Rfixed(attempts, 4) + ' attempts</strong> and succeeds '
      + Rpct(success, 4) + ' of the time; ' + Rtext(lost) + ' of requests are lost anyway. '
      + 'At ' + group(BigInt(lam)) + ' rps offered the service actually sees <strong>'
      + Rfixed(amplified, 1) + '</strong> attempts a second, of which ' + Rpct(duplicateShare(p, r), 2)
      + ' is retry traffic. The policy is cheap now &mdash; but the same '
      + r + ' retries cost <strong>' + Rfixed(retryAttempts(R(9n, 10n), r), 3)
      + ' attempts</strong> when the failure rate is 90%, and tend to ' + (r + 1)
      + ' as it approaches certainty. Retries are most expensive exactly when the service is worst, '
      + 'which is what the next lesson turns into a feedback loop.';
  }

  [pS, rS, loadS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Retries and request amplification",
        subtitle="Expected attempts, success, and the load the policy adds",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the failure rate and the policy"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both figures come from the same geometric series, evaluated as exact fractions: "
            "attempts are (1 &minus; p&#8319;&#8314;&sup1;)/(1 &minus; p) and success is "
            "1 &minus; p&#8319;&#8314;&sup1;.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - storm
# ---------------------------------------------------------------------------


def _storm(cfg):
    load_pct = int(cfg.get("load_pct", 95))
    base_pct = int(cfg.get("base_pct", 10))
    retries = int(cfg.get("retries", 3))
    steps = int(cfg.get("steps", 5))

    markup = (
        _toolbar(
            "The retry storm",
            "load feeds failure feeds retries feeds load &mdash; iterate it and see where it lands",
            [("cyan", "the iterates"), ("red", "capacity"), ("purple", "the fixed point")],
        )
        + _stage(_svg("stPath", "0 0 520 196", "Successive iterates of the load, against the capacity line."))
        + _table("stTable")
        + _banner("stStatus")
    )
    controls = (
        _range("stLoad", "Offered load before retries (per cent of capacity)", 50, 150, load_pct)
        + _range("stBase", "Failure probability with no overload (per cent)", 0, 30, base_pct)
        + _range("stR", "Retries", 0, 4, retries)
        + _range("stSteps", "Iterations to show", 3, 7, steps)
        + _kpis(
            [
                ("Where it starts", "stStart"),
                ("Fixed point, bracketed", "stFix"),
                ("Failure rate there", "stFixP"),
                ("Amplification there", "stAmp"),
                ("With retries switched off", "stNoRetry"),
                ("Verdict", "stVerdict"),
            ]
        )
        + _hint(
            "stHint",
            "Capacity is 1 by definition, so every load on this page is in units of capacity. "
            "The iterates are exact fractions and each step raises the failure probability to the "
            "(r + 1)th power, so the denominators grow very fast &mdash; the table stops when they "
            "outgrow the budget and says so.",
        )
    )

    script = _CORE_JS + r"""
  var loadS = document.getElementById('stLoad'), baseS = document.getElementById('stBase');
  var rS = document.getElementById('stR'), stepS = document.getElementById('stSteps');
  var plot = document.getElementById('stPath'), table = document.getElementById('stTable');
  var status = document.getElementById('stStatus');
  var DIGIT_CAP = 3000;

  function redraw() {
    var lp = +loadS.value, bp = +baseS.value, r = +rS.value, steps = +stepS.value;
    document.getElementById('stLoadOut').textContent = lp + '% of capacity';
    document.getElementById('stBaseOut').textContent = bp + '%';
    document.getElementById('stROut').textContent = r === 0 ? 'none' : r;
    document.getElementById('stStepsOut').textContent = steps;

    var cap = R(1n, 1n), lambda = R(BigInt(lp), 100n), base = R(BigInt(bp), 100n);
    var run = stormRun(lambda, cap, base, r, steps, DIGIT_CAP);
    var fix = stormFixedPoint(lambda, cap, base, r, 24);
    var mid = Rdiv(Radd(fix.lo, fix.hi), R(2n, 1n));
    var pAt = stormFailure(mid, cap, base), ampAt = retryAttempts(pAt, r);
    var above = Rcmp(fix.lo, cap) > 0, below = Rcmp(fix.hi, cap) <= 0;

    document.getElementById('stStart').textContent = Rfixed(lambda, 4) + ' of capacity';
    document.getElementById('stFix').textContent = Rfixed(fix.lo, 5) + ' &hellip; ' + Rfixed(fix.hi, 5);
    document.getElementById('stFixP').textContent = Rfixed(pAt, 5);
    document.getElementById('stAmp').textContent = Rfixed(ampAt, 4) + '&times;';
    document.getElementById('stNoRetry').textContent = Rfixed(lambda, 4) + ' of capacity';
    document.getElementById('stVerdict').textContent = above ? 'above capacity'
      : (below ? 'below capacity' : 'astride capacity');

    var rows = '', i;
    for (i = 0; i < run.rows.length; i += 1) {
      var row = run.rows[i];
      rows += '<tr><td>' + row.step + '</td>'
        + '<td>' + Rfixed(row.into, 5) + '</td>'
        + '<td>' + Rfixed(row.p, 5) + '</td>'
        + '<td>' + Rfixed(row.amp, 5) + '</td>'
        + '<td class="' + (Rcmp(row.out, cap) > 0 ? 'tone-red' : 'tone-cyan') + '">'
        + Rfixed(row.out, 5) + '</td>'
        + '<td class="tone-muted">' + group(BigInt(String(row.out.d).length)) + '</td></tr>';
    }
    if (run.stopped) {
      rows += '<tr class="tone-muted"><td colspan="6">the exact fractions passed '
        + group(BigInt(DIGIT_CAP)) + ' digits and the table stops here; the bracket below does not '
        + 'iterate, so it still answers</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>step</th><th>load in</th><th>failure p</th>'
      + '<th>attempts per request</th><th>load out</th><th>digits in the denominator</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var top = Math.max(1.15, parseFloat(Rfixed(fix.hi, 6)) * 1.1), n = run.rows.length;
    function yp(v) { return 150 - (parseFloat(Rfixed(v, 6)) / top) * 126; }
    var x0 = 30, dx = n > 0 ? 470 / Math.max(1, n) : 0, s = '', pts = '' + x0 + ',' + yp(lambda);
    for (i = 0; i < n; i += 1) pts += ' ' + (x0 + (i + 1) * dx) + ',' + yp(run.rows[i].out);
    s += '<line x1="30" y1="150" x2="510" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="30" y1="' + yp(cap) + '" x2="510" y2="' + yp(cap)
      + '" stroke="var(--red)" stroke-width="1.5" stroke-dasharray="5 3" />'
      + '<text x="34" y="' + (yp(cap) - 5) + '" font-size="10" fill="var(--red)">capacity</text>'
      + '<rect x="30" y="' + yp(fix.hi) + '" width="480" height="' + Math.max(1.5, yp(fix.lo) - yp(fix.hi))
      + '" fill="var(--purple)" opacity="0.35" />'
      + '<text x="508" y="' + (yp(fix.hi) - 5) + '" font-size="10" text-anchor="end" fill="var(--purple)">'
      + 'fixed point, bracketed at ' + Rfixed(fix.lo, 4) + '&hellip;' + Rfixed(fix.hi, 4) + '</text>'
      + '<polyline points="' + pts + '" fill="none" stroke="var(--cyan)" stroke-width="2" />'
      + '<circle cx="' + x0 + '" cy="' + yp(lambda) + '" r="3" fill="var(--cyan)" />';
    for (i = 0; i < n; i += 1) {
      s += '<circle cx="' + (x0 + (i + 1) * dx) + '" cy="' + yp(run.rows[i].out) + '" r="3" fill="var(--cyan)" />';
    }
    s += '<text x="30" y="166" font-size="10" fill="var(--muted)">step 0 (the load you offered)</text>'
      + '<text x="510" y="166" font-size="10" text-anchor="end" fill="var(--muted)">step ' + n + '</text>'
      + '<text x="30" y="182" font-size="10" fill="var(--muted)">vertical axis: load in units of capacity, '
      + '0 to ' + top.toFixed(2) + '</text>'
      + '<text x="30" y="194" font-size="10" fill="var(--purple)">the bracket is exact: the map is '
      + 'increasing, so a sign change between two fractions traps the fixed point between them</text>';
    plot.innerHTML = s;

    var startedFine = Rcmp(lambda, cap) <= 0;
    status.innerHTML = 'You offered <strong>' + Rfixed(lambda, 4) + '</strong> of capacity'
      + (startedFine ? ', which the service could serve' : ', which was already over capacity')
      + '. With ' + r + ' retr' + (r === 1 ? 'y' : 'ies') + ' the loop settles between <strong>'
      + Rfixed(fix.lo, 5) + '</strong> and <strong>' + Rfixed(fix.hi, 5) + '</strong> of capacity, at a '
      + 'failure rate of ' + Rfixed(pAt, 4) + ' and ' + Rfixed(ampAt, 4) + ' attempts a request. '
      + (above
          ? (startedFine
              ? '<span class="tone-red">The retries alone put the service over capacity.</span> Nothing '
                + 'else changed: the offered load was serviceable and the policy meant to protect it is '
                + 'what is now drowning it. Retries do not stop when the service recovers &mdash; they '
                + 'are what prevents it recovering, and switching them off returns the load to '
                + Rfixed(lambda, 4) + '.'
              : 'The service was already overloaded and the retries have made it worse, multiplying the '
                + 'excess rather than absorbing it.')
          : (r === 0
              ? 'With retries off the map is the identity and the fixed point is the offered load itself. '
                + 'Turn the retries up and watch the same offered load land somewhere else.'
              : 'The loop settles below capacity here, so the policy is affordable. Raise the offered '
                + 'load or the retry count and find the point where it is not: the transition is not '
                + 'gradual, because each extra attempt raises p, which raises the attempts again.'));
  }

  [loadS, baseS, rS, stepS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Retry storms",
        subtitle="A feedback loop, iterated to its fixed point — which can sit above capacity",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the load and the retry policy"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each row of the table is one application of the map: the load sets the failure rate, "
            "the failure rate sets the attempts, the attempts set the load. Work three of them by "
            "hand before you believe the last one.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - backoff
# ---------------------------------------------------------------------------


def _backoff(cfg):
    clients = int(cfg.get("clients", 600))
    outage = int(cfg.get("outage_seconds", 20))
    base_ms = int(cfg.get("base_ms", 1000))
    jitter = int(cfg.get("jitter_pct", 100))
    seed = int(cfg.get("seed", 7))

    markup = (
        _toolbar(
            "Backoff, with and without jitter",
            "the same clients, the same seed, the same policy &mdash; one of them synchronised",
            [("red", "no jitter"), ("green", "with jitter"), ("muted", "the outage")],
        )
        + _stage(_svg("boHist", "0 0 520 230", "Two histograms of retries per second: synchronised waves above, spread retries below."))
        + _table("boTable")
        + _banner("boStatus")
    )
    controls = (
        _range("boClients", "Clients that failed together", 50, 2000, clients)
        + _range("boOutage", "Outage length (seconds)", 1, 40, outage)
        + _range("boBase", "Backoff base (milliseconds)", 100, 4000, base_ms, 100)
        + _range("boJitter", "Jitter width (per cent of the delay)", 0, 100, jitter)
        + _range("boSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Peak retries a second, no jitter", "boPeak"),
                ("Peak retries a second, with jitter", "boPeakJ"),
                ("Peak cut by", "boFactor"),
                ("Retries in total, no jitter", "boTotal"),
                ("Retries in total, with jitter", "boTotalJ"),
                ("The waves land at", "boWave"),
            ]
        )
        + _hint(
            "boHint",
            "Every client fails at the same instant &mdash; that is what an outage is &mdash; and "
            "schedules retry i at base &times; 2&#8305;&#8315;&sup1; after it. Without jitter that is "
            "the same millisecond for all of them. The stream is an LCG with multiplier 1 103 515 245, "
            "increment 12 345 and modulus 2&#179;&#185;, so the same seed draws the same histogram. "
            "The bars are 200 ms wide: without jitter the whole wave lands inside one millisecond, so any wider bucket would flatter it.",
        )
    )

    script = _CORE_JS + r"""
  var cS = document.getElementById('boClients'), oS = document.getElementById('boOutage');
  var bS = document.getElementById('boBase'), jS = document.getElementById('boJitter');
  var sS = document.getElementById('boSeed');
  var hist = document.getElementById('boHist'), table = document.getElementById('boTable');
  var status = document.getElementById('boStatus');
  var ATTEMPTS = 8, SLOT_MS = 200, PER_SEC = 5;

  function redraw() {
    var clients = +cS.value, outage = +oS.value, base = +bS.value, jit = +jS.value, seed = +sS.value;
    document.getElementById('boClientsOut').textContent = group(BigInt(clients));
    document.getElementById('boOutageOut').textContent = outage + ' s';
    document.getElementById('boBaseOut').textContent = base + ' ms';
    document.getElementById('boJitterOut').textContent = jit === 0 ? 'none' : jit + '%';
    document.getElementById('boSeedOut').textContent = seed;

    var horizon = Math.min(40, outage + 20);
    var h = backoffHistogram(clients, outage, base, jit, ATTEMPTS, horizon, seed, SLOT_MS);
    var peakP = peakOf(h.plain) * PER_SEC, peakJ = peakOf(h.jitter) * PER_SEC;
    var totP = totalOf(h.plain), totJ = totalOf(h.jitter);
    var perP = perSecond(h.plain, SLOT_MS), perJ = perSecond(h.jitter, SLOT_MS);

    document.getElementById('boPeak').textContent = group(BigInt(peakP)) + ' /s';
    document.getElementById('boPeakJ').textContent = group(BigInt(peakJ)) + ' /s';
    document.getElementById('boFactor').textContent = peakJ > 0
      ? Rfixed(R(BigInt(peakP), BigInt(peakJ)), 2) + '&times;' : '&mdash;';
    document.getElementById('boTotal').textContent = group(BigInt(totP));
    document.getElementById('boTotalJ').textContent = group(BigInt(totJ));
    var waves = [], i;
    for (i = 1; i <= ATTEMPTS; i += 1) {
      var d = backoffDelayMs(base, i) / 1000;
      if (d <= horizon) waves.push(d < 1 ? d.toFixed(1) : String(d));
      if (d >= outage) break;
    }
    document.getElementById('boWave').textContent = waves.join(', ') + ' s';

    var rows = '';
    for (i = 0; i < perP.length; i += 1) {
      if (!perP[i] && !perJ[i]) continue;
      var busyP = 0, busyJ = 0, q;
      for (q = i * PER_SEC; q < (i + 1) * PER_SEC && q < h.slots; q += 1) {
        if (h.plain[q] > busyP) busyP = h.plain[q];
        if (h.jitter[q] > busyJ) busyJ = h.jitter[q];
      }
      rows += '<tr' + (i < outage ? '' : ' class="tone-muted"') + '><td>' + i + '&ndash;' + (i + 1) + ' s</td>'
        + '<td class="tone-red">' + group(BigInt(perP[i])) + '</td>'
        + '<td class="tone-red">' + group(BigInt(busyP)) + '</td>'
        + '<td class="tone-green">' + group(BigInt(perJ[i])) + '</td>'
        + '<td class="tone-green">' + group(BigInt(busyJ)) + '</td>'
        + '<td>' + (i < outage ? 'still down' : 'recovered') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>second after the failure</th><th>retries, no jitter</th>'
      + '<th>busiest ' + SLOT_MS + ' ms in it</th><th>retries, with jitter</th>'
      + '<th>busiest ' + SLOT_MS + ' ms in it</th><th>service</th></tr></thead><tbody>' + rows + '</tbody>';

    var top = Math.max(1, peakOf(h.plain), peakOf(h.jitter)), bw = 504 / h.slots, s = '';
    s += '<text x="0" y="12" font-size="11" fill="var(--red)">no jitter: every client retries in the '
      + 'same millisecond</text>';
    for (i = 0; i < h.slots; i += 1) {
      if (!h.plain[i]) continue;
      var hp = (h.plain[i] / top) * 76;
      s += '<rect x="' + (6 + i * bw) + '" y="' + (94 - hp) + '" width="' + Math.max(1, bw)
        + '" height="' + hp + '" fill="var(--red)" opacity="0.9" />';
    }
    s += '<line x1="6" y1="94" x2="510" y2="94" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="112" font-size="11" fill="var(--green)">jitter of ' + jit
      + '%: the same clients, the same seed, the same total</text>';
    for (i = 0; i < h.slots; i += 1) {
      if (!h.jitter[i]) continue;
      var hj = (h.jitter[i] / top) * 76;
      s += '<rect x="' + (6 + i * bw) + '" y="' + (194 - hj) + '" width="' + Math.max(1, bw)
        + '" height="' + hj + '" fill="var(--green)" opacity="0.9" />';
    }
    var ox = 6 + (outage * 1000 / SLOT_MS) * bw;
    s += '<line x1="6" y1="194" x2="510" y2="194" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + ox + '" y1="18" x2="' + ox + '" y2="194" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="' + Math.min(380, ox + 4) + '" y="206" font-size="10" fill="var(--muted)">the service comes '
      + 'back here (' + outage + ' s)</text>'
      + '<text x="6" y="220" font-size="10" fill="var(--muted)">both panels share one vertical scale, 0 to '
      + group(BigInt(top)) + ' retries per ' + SLOT_MS + ' ms slot, over ' + horizon + ' seconds</text>';
    hist.innerHTML = s;

    status.innerHTML = group(BigInt(clients)) + ' clients fail together and retry with a ' + base
      + ' ms base. Without jitter the retries arrive in waves at <strong>' + waves.join(', ')
      + ' s</strong>, and every client in a wave lands in the same millisecond &mdash; at a '
      + SLOT_MS + ' ms resolution that is <strong>' + group(BigInt(peakP)) + ' a second</strong>, and '
      + 'the true instantaneous spike is higher still, because doubling a constant keeps it constant. '
      + 'With ' + jit + '% jitter the same policy makes '
      + group(BigInt(totJ)) + ' retries peak at <strong>' + group(BigInt(peakJ)) + ' a second</strong>'
      + (peakJ > 0 && peakP > peakJ
          ? ', a factor of <strong>' + Rfixed(R(BigInt(peakP), BigInt(peakJ)), 2) + '</strong> off the spike'
          : '')
      + '. Backoff alone changed the total from ' + group(BigInt(totP)) + ' to ' + group(BigInt(totJ))
      + '; only jitter changed the peak, and it is the peak that decides whether the service gets far '
      + 'enough into its recovery to stay up.';
  }

  [cS, oS, bS, jS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Backoff and jitter",
        subtitle="Two seeded histograms of the same outage, one of them synchronised",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the outage and the policy"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both histograms are drawn from one seeded stream, so the run is reproducible: the "
            "same seed gives the same bars every time this page is opened.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - shed
# ---------------------------------------------------------------------------


def _shed(cfg):
    cap = int(cfg.get("capacity_rps", 1000))
    offered = int(cfg.get("offered_pct", 200))
    threshold = int(cfg.get("threshold_pct", 90))

    markup = (
        _toolbar(
            "Shedding against collapse",
            "rejecting deliberately, so that the requests you accept are the ones you finish",
            [("green", "goodput with shedding"), ("red", "goodput without"), ("amber", "rejected on purpose")],
        )
        + _stage(_svg("shCurve", "0 0 520 200", "Goodput against offered load, with shedding and without."))
        + _table("shTable")
        + _banner("shStatus")
    )
    controls = (
        _range("shCap", "Capacity (requests per second)", 100, 5000, cap, 50)
        + _range("shOffered", "Offered load (per cent of capacity)", 50, 400, offered)
        + _range("shThresh", "Shed everything above (per cent of capacity)", 40, 120, threshold)
        + _kpis(
            [
                ("Goodput with shedding", "shGood"),
                ("Goodput without", "shGoodU"),
                ("Rejected on purpose", "shRej"),
                ("Utilisation with shedding", "shRho"),
                ("Utilisation without", "shRhoU"),
                ("Shedding is better by", "shRatio"),
            ]
        )
        + _hint(
            "shHint",
            "The collapse model is the lesson&rsquo;s own and it is evaluated here, not drawn: above "
            "capacity the server still does C units of work a second, but only the share C/L of what "
            "it started finishes before the client gives up, so the goodput is C &times; (C/L). "
            "Shedding replaces that with a flat line at the threshold.",
        )
    )

    script = _CORE_JS + r"""
  var capS = document.getElementById('shCap'), offS = document.getElementById('shOffered');
  var thS = document.getElementById('shThresh');
  var curve = document.getElementById('shCurve'), table = document.getElementById('shTable');
  var status = document.getElementById('shStatus');

  function redraw() {
    var capacity = +capS.value, offPct = +offS.value, thPct = +thS.value;
    document.getElementById('shCapOut').textContent = group(BigInt(capacity)) + ' rps';
    document.getElementById('shOfferedOut').textContent = offPct + '% of capacity';
    document.getElementById('shThreshOut').textContent = thPct + '% of capacity';

    var cap = R(BigInt(capacity), 1n);
    var offered = Rmul(cap, R(BigInt(offPct), 100n));
    var threshold = Rmul(cap, R(BigInt(thPct), 100n));
    var admitted = admittedLoad(offered, threshold);
    var shed = goodputShed(offered, cap, threshold);
    var unshed = goodputUnshed(offered, cap);
    var rejected = Rsub(offered, admitted);
    var rhoShed = Rdiv(admitted, cap), rhoUn = Rdiv(offered, cap);
    var ratio = Rzero(unshed) ? null : Rdiv(shed, unshed);

    document.getElementById('shGood').textContent = Rfixed(shed, 1) + ' rps';
    document.getElementById('shGoodU').textContent = Rfixed(unshed, 1) + ' rps';
    document.getElementById('shRej').textContent = Rfixed(rejected, 1) + ' rps ('
      + Rpct(rejectedFraction(offered, threshold), 1) + ')';
    document.getElementById('shRho').textContent = Rfixed(rhoShed, 4);
    document.getElementById('shRhoU').textContent = Rfixed(rhoUn, 4);
    document.getElementById('shRatio').textContent = ratio === null ? '&mdash;' : Rfixed(ratio, 2) + '&times;';

    var loads = [50, 90, 100, 150, 200, 300, 400], rows = '', i;
    for (i = 0; i < loads.length; i += 1) {
      var L = Rmul(cap, R(BigInt(loads[i]), 100n));
      var g1 = goodputShed(L, cap, threshold), g2 = goodputUnshed(L, cap);
      rows += '<tr' + (loads[i] === offPct ? ' class="tone-cyan"' : '') + '><td>' + loads[i] + '%</td>'
        + '<td>' + Rfixed(L, 0) + '</td>'
        + '<td class="tone-green">' + Rfixed(g1, 1) + '</td>'
        + '<td class="tone-red">' + Rfixed(g2, 1) + '</td>'
        + '<td class="tone-amber">' + Rfixed(Rsub(L, admittedLoad(L, threshold)), 1) + '</td>'
        + '<td>' + (Rzero(g2) ? '&mdash;' : Rfixed(Rdiv(g1, g2), 2) + '&times;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>offered</th><th>requests a second</th><th>goodput, shedding</th>'
      + '<th>goodput, not shedding</th><th>rejected</th><th>ratio</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var xmax = 400, s = '', pts1 = '', pts2 = '';
    function xp(pct) { return 34 + (pct / xmax) * 472; }
    function yp(v) { return 154 - (parseFloat(Rfixed(Rdiv(v, cap), 6))) * 120; }
    for (i = 20; i <= xmax; i += 5) {
      var L2 = Rmul(cap, R(BigInt(i), 100n));
      pts1 += (pts1 ? ' ' : '') + xp(i) + ',' + yp(goodputShed(L2, cap, threshold));
      pts2 += (pts2 ? ' ' : '') + xp(i) + ',' + yp(goodputUnshed(L2, cap));
    }
    s = '<line x1="34" y1="154" x2="510" y2="154" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="34" y1="20" x2="34" y2="154" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + xp(100) + '" y1="20" x2="' + xp(100) + '" y2="154" stroke="var(--muted)" '
      + 'stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="' + (xp(100) + 4) + '" y="30" font-size="10" fill="var(--muted)">capacity</text>'
      + '<polyline points="' + pts2 + '" fill="none" stroke="var(--red)" stroke-width="2" />'
      + '<polyline points="' + pts1 + '" fill="none" stroke="var(--green)" stroke-width="2" />'
      + '<circle cx="' + xp(offPct) + '" cy="' + yp(shed) + '" r="4" fill="var(--green)" />'
      + '<circle cx="' + xp(offPct) + '" cy="' + yp(unshed) + '" r="4" fill="var(--red)" />'
      + '<text x="34" y="170" font-size="10" fill="var(--muted)">offered load, 20% to 400% of capacity</text>'
      + '<text x="510" y="170" font-size="10" text-anchor="end" fill="var(--muted)">400%</text>'
      + '<text x="34" y="186" font-size="10" fill="var(--green)">shedding: flat at the threshold, because '
      + 'every admitted request is one the server can finish</text>'
      + '<text x="34" y="198" font-size="10" fill="var(--red)">not shedding: rises to capacity, then falls, '
      + 'because work spent on abandoned requests is work not spent on the rest</text>';
    curve.innerHTML = s;

    var better = ratio !== null && Rcmp(shed, unshed) > 0;
    status.innerHTML = 'At <strong>' + Rfixed(offered, 0) + ' rps</strong> offered against '
      + group(BigInt(capacity)) + ' rps of capacity, shedding above ' + thPct + '% delivers <strong>'
      + Rfixed(shed, 1) + ' rps</strong> and rejects ' + Rfixed(rejected, 1) + ' of them outright. '
      + 'Not shedding accepts everything and delivers <strong>' + Rfixed(unshed, 1) + ' rps</strong>. '
      + (better
          ? 'Rejecting <span class="tone-amber">' + Rpct(rejectedFraction(offered, threshold), 1)
            + '</span> of the traffic served <strong>' + Rfixed(Rdiv(shed, unshed), 2) + '&times; more '
            + 'users</strong> than accepting all of it: the requests you refuse quickly cost nothing, '
            + 'and the requests you accept and then abandon cost the capacity that would have served '
            + 'someone else. Rejecting requests is how availability is defended, not how it is lost.'
          : (Rcmp(offered, threshold) <= 0
              ? 'Here the shedder is not shedding: its threshold is at or above the offered load, so '
                + 'the two arms are the same service. Push the offered load past the threshold and '
                + 'the curves separate.'
              : 'Here the load is inside capacity, so shedding costs users and buys nothing &mdash; '
                + 'push the offered load past 100% and the two curves separate.'))
      + ' Utilisation is ' + Rfixed(rhoShed, 4) + ' with the shedder and ' + Rfixed(rhoUn, 4) + ' without it.';
  }

  [capS, offS, thS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Load shedding and circuit breakers",
        subtitle="Goodput when you refuse work, against goodput when you accept all of it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the load and the shedding threshold"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both goodputs are computed from the load and the capacity you set. The collapse "
            "arm is the lesson&rsquo;s stated model, evaluated the same way the shedding arm is.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L12 - durability
# ---------------------------------------------------------------------------


def _durability(cfg):
    copies = int(cfg.get("copies", 3))
    rate = int(cfg.get("rate_per_1000", 20))
    window = int(cfg.get("window_hours", 24))
    groups = int(cfg.get("groups", 10000))

    markup = (
        _toolbar(
            "Durability, to first order",
            "N! &times; f&#8319; &times; (R/8760)&#8319;&#8315;&sup1; &mdash; the one figure on this course that rounds",
            [("cyan", "the loss probability"), ("purple", "halving the repair window"), ("red", "an approximation")],
        )
        + _stage(_svg("duCurve", "0 0 520 200", "Annual loss probability against the repair window, on a logarithmic scale."))
        + _table("duTable")
        + _banner("duStatus")
    )
    controls = (
        _range("duN", "Copies of each item, N", 2, 6, copies)
        + _range("duF", "Annual failure rate per copy (per 1000)", 1, 200, rate)
        + _range("duR", "Repair window R (hours)", 1, 168, window)
        + _range("duGroups", "Placement groups in the fleet", 100, 200000, groups, 100)
        + _kpis(
            [
                ("Loss per group per year", "duP"),
                ("With R halved", "duHalf"),
                ("Halving R divides by", "duFactor"),
                ("The same formula, exactly", "duExact"),
                ("Expected losses in the fleet", "duFleet"),
                ("Years between losses", "duYears"),
            ]
        )
        + _hint(
            "duHint",
            "What is approximate here is the model, not the division: the formula truncates every "
            "term in which failures overlap or a repair lands mid-window. The exact fraction of the "
            "same first-order formula is printed beside it, and the two agree &mdash; which is how "
            "you can tell that the gap to the truth is in the modelling.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('duN'), fS = document.getElementById('duF');
  var rS = document.getElementById('duR'), gS = document.getElementById('duGroups');
  var curve = document.getElementById('duCurve'), table = document.getElementById('duTable');
  var status = document.getElementById('duStatus');

  function redraw() {
    var n = +nS.value, fp = +fS.value, hours = +rS.value, groups = +gS.value;
    document.getElementById('duNOut').textContent = n + ' copies';
    document.getElementById('duFOut').textContent = (fp / 10).toFixed(1) + '% a year';
    document.getElementById('duROut').textContent = hours + ' h';
    document.getElementById('duGroupsOut').textContent = group(BigInt(groups));

    var f = R(BigInt(fp), 1000n), win = R(BigInt(hours), 1n);
    var p = durabilityLossApprox(n, f, win);
    var half = durabilityLossApprox(n, f, R(BigInt(hours), 2n));
    var exact = durabilityLossExact(n, f, win);
    var fleet = p * groups;
    var gap = truncationGap((n - 1) * Rnum(f) * hours / 8760);

    document.getElementById('duP').textContent = sciText(p, 3);
    document.getElementById('duHalf').textContent = sciText(half, 3);
    document.getElementById('duFactor').textContent = Math.pow(2, n - 1) + '&times;';
    document.getElementById('duExact').textContent = Rtext(exact);
    document.getElementById('duFleet').textContent = sciText(fleet, 3) + ' a year';
    document.getElementById('duYears').textContent = fleet > 0 ? sciText(1 / fleet, 3) + ' years' : '&mdash;';

    var rows = '', i;
    for (i = 2; i <= 6; i += 1) {
      var pi = durabilityLossApprox(i, f, win);
      rows += '<tr' + (i === n ? ' class="tone-cyan"' : '') + '><td>' + i + ' copies</td>'
        + '<td>' + group(fact(i)) + '</td>'
        + '<td>' + sciText(pi, 3) + '</td>'
        + '<td>' + sciText(durabilityLossApprox(i, f, R(BigInt(hours), 2n)), 3) + '</td>'
        + '<td>' + (pi > 0 ? sciText(1 / (pi * groups), 2) + ' y' : '&mdash;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>N</th><th>N!</th><th>loss a year, per group</th>'
      + '<th>with R halved</th><th>years between fleet losses</th></tr></thead><tbody>'
      + rows + '</tbody>'
      + '<tfoot><tr class="tone-red"><td colspan="5">the truncation itself: the first-order term '
      + gap.first.toExponential(6) + ' stands in for 1 &minus; e<sup>&minus;x</sup> = '
      + gap.exact.toExponential(6) + ', a relative gap of '
      + (gap.first > 0 ? ((gap.first - gap.exact) / gap.first * 100).toFixed(4) : '0') + '%</td></tr></tfoot>';

    var s = '', pts = '';
    var lo = Math.log10(Math.max(1e-30, durabilityLossApprox(n, f, R(1n, 1n))));
    var hi = Math.log10(Math.max(1e-30, durabilityLossApprox(n, f, R(168n, 1n))));
    var span = Math.max(1e-9, hi - lo);
    function xp(h) { return 34 + ((h - 1) / 167) * 472; }
    function yp(v) { return 150 - ((Math.log10(Math.max(1e-30, v)) - lo) / span) * 118; }
    for (i = 1; i <= 168; i += 1) {
      pts += (i > 1 ? ' ' : '') + xp(i) + ',' + yp(durabilityLossApprox(n, f, R(BigInt(i), 1n)));
    }
    s = '<line x1="34" y1="150" x2="510" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="34" y1="18" x2="34" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<polyline points="' + pts + '" fill="none" stroke="var(--cyan)" stroke-width="2" />'
      + '<circle cx="' + xp(hours) + '" cy="' + yp(p) + '" r="4" fill="var(--cyan)" />'
      + '<text x="' + Math.min(360, xp(hours) + 8) + '" y="' + (yp(p) - 6) + '" font-size="10" fill="var(--cyan)">'
      + 'R = ' + hours + ' h &rarr; ' + sciText(p, 2) + '</text>';
    if (hours >= 2) {
      s += '<circle cx="' + xp(hours / 2) + '" cy="' + yp(half) + '" r="4" fill="var(--purple)" />'
        + '<text x="' + Math.min(360, xp(hours / 2) + 8) + '" y="' + (yp(half) + 14)
        + '" font-size="10" fill="var(--purple)">R/2 &rarr; ' + sciText(half, 2) + ', a factor of '
        + Math.pow(2, n - 1) + '</text>';
    }
    s += '<text x="34" y="166" font-size="10" fill="var(--muted)">repair window, 1 h to 168 h</text>'
      + '<text x="510" y="166" font-size="10" text-anchor="end" fill="var(--muted)">168 h</text>'
      + '<text x="34" y="182" font-size="10" fill="var(--muted)">vertical axis is logarithmic: the curve '
      + 'is a straight line because the probability is R raised to the power N &minus; 1</text>'
      + '<text x="34" y="194" font-size="10" fill="var(--red)">every number on this page is rounded, and '
      + 'the rounding is the first-order model, not the arithmetic</text>';
    curve.innerHTML = s;

    status.innerHTML = '<strong>' + n + ' copies</strong> at a ' + (fp / 10).toFixed(1)
      + '% annual failure rate, replaced within <strong>' + hours + ' h</strong>, lose an item with '
      + 'probability <strong>' + sciText(p, 3) + '</strong> per group per year &mdash; and the same '
      + 'first-order formula as an exact fraction is ' + Rtext(exact) + ', which agrees. '
      + 'Across ' + group(BigInt(groups)) + ' groups that is ' + sciText(fleet, 3) + ' losses a year, '
      + 'one every ' + (fleet > 0 ? sciText(1 / fleet, 2) : '&mdash;') + ' years. '
      + 'Halving the repair window to ' + (hours / 2) + ' h divides that by <strong>'
      + Math.pow(2, n - 1) + '</strong>, not by two: R appears N &minus; 1 times. '
      + '<span class="tone-red">This figure is an approximation and the page says so.</span> '
      + 'It is a first-order rare-event estimate: it drops every term where two failures overlap or '
      + 'a repair finishes inside the window, which is why three copies is not three times the '
      + 'durability of one but f<sup>' + n + '</sup> times a factorial.';
  }

  [nS, fS, rS, gS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Replica loss and durability",
        subtitle="N failures inside one repair window, and what halving the window is worth",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the copies, the failure rate and the repair window"),
        panel_intro=cfg.get(
            "panel_intro",
            "This is the one lesson on the course whose figure is not exact. The formula is a "
            "first-order rare-event estimate and the page prints the exact fraction of that same "
            "formula beside it, so you can see which part is the approximation.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L13 - shuffle
# ---------------------------------------------------------------------------


def _shuffle(cfg):
    nodes = int(cfg.get("nodes", 16))
    per = int(cfg.get("per_tenant", 2))
    tenants = int(cfg.get("tenants", 12))
    seed = int(cfg.get("seed", 3))

    markup = (
        _toolbar(
            "Shuffle sharding",
            "C(n&minus;k, k)/C(n, k) share nothing; only 1/C(n, k) share everything",
            [("cyan", "the first tenant"), ("red", "an identical set"), ("amber", "some overlap")],
        )
        + _stage(_svg("sfGrid", "0 0 520 300", "A sample assignment of tenants to nodes, with overlaps against the first tenant marked."))
        + _table("sfTable")
        + _banner("sfStatus")
    )
    controls = (
        _range("sfN", "Nodes in the fleet, n", 4, 40, nodes)
        + _range("sfK", "Nodes each tenant uses, k", 1, 8, per)
        + _range("sfTenants", "Tenants drawn", 2, 24, tenants)
        + _range("sfSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Distinct shards, C(n, k)", "sfShards"),
                ("P(share no node)", "sfDisjoint"),
                ("P(identical set)", "sfIdentical"),
                ("One bad node degrades", "sfBlast"),
                ("Tenants sharing your whole set", "sfExpected"),
                ("The overlap terms sum to", "sfSum"),
            ]
        )
        + _hint(
            "sfHint",
            "Every probability here is a ratio of binomial coefficients in BigInt, so C(40, 8) is "
            "exact and so is the answer. Overlapping in one node is not an outage: it is a tenant "
            "that has lost one of its k and still has k &minus; 1.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('sfN'), kS = document.getElementById('sfK');
  var tS = document.getElementById('sfTenants'), sS = document.getElementById('sfSeed');
  var grid = document.getElementById('sfGrid'), table = document.getElementById('sfTable');
  var status = document.getElementById('sfStatus');

  function redraw() {
    var n = +nS.value, k = Math.min(+kS.value, +nS.value), tenants = +tS.value, seed = +sS.value;
    document.getElementById('sfNOut').textContent = n;
    document.getElementById('sfKOut').textContent = k + (k === +kS.value ? '' : ' (capped at n)');
    document.getElementById('sfTenantsOut').textContent = tenants;
    document.getElementById('sfSeedOut').textContent = seed;

    var shards = comb(n, k);
    var dis = shuffleDisjoint(n, k), ident = shuffleIdentical(n, k);
    var blast = blastFraction(n, k), i, j;
    var sum = R(0n, 1n);
    for (j = 0; j <= k; j += 1) sum = Radd(sum, shuffleOverlap(n, k, j));
    var sets = shuffleAssign(n, k, tenants, seed);
    var same = identicalCount(sets), none = disjointCount(sets);

    document.getElementById('sfShards').textContent = group(shards);
    document.getElementById('sfDisjoint').textContent = Rtext(dis) + ' = ' + Rpct(dis, 3);
    document.getElementById('sfIdentical').textContent = Rtext(ident) + ' = ' + Rpct(ident, 4);
    document.getElementById('sfBlast').textContent = Rtext(blast) + ' of tenants';
    document.getElementById('sfExpected').textContent = Rfixed(Rmul(ident, R(BigInt(tenants - 1), 1n)), 4)
      + ' of ' + (tenants - 1);
    document.getElementById('sfSum').textContent = Rtext(sum);

    var rows = '';
    for (j = 0; j <= k; j += 1) {
      var pj = shuffleOverlap(n, k, j);
      rows += '<tr class="' + (j === 0 ? 'tone-cyan' : (j === k ? 'tone-red' : 'tone-amber')) + '"><td>'
        + j + ' node' + (j === 1 ? '' : 's') + ' in common</td>'
        + '<td>C(' + k + ',' + j + ')&middot;C(' + (n - k) + ',' + (k - j) + ') = '
        + group(comb(k, j) * comb(n - k, k - j)) + '</td>'
        + '<td class="tt">' + Rtext(pj) + '</td><td>' + Rpct(pj, 4) + '</td>'
        + '<td>' + (j === 0 ? 'untouched' : (j === k ? 'down with you' : 'degraded, still has '
            + (k - j) + ' of ' + k)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>overlap with your shard</th><th>ways</th><th>probability</th>'
      + '<th>as a percentage</th><th>what it means for them</th></tr></thead><tbody>' + rows + '</tbody>';

    var cw = Math.min(12, 470 / n), rh = Math.min(11, 240 / tenants), s = '';
    s += '<text x="0" y="10" font-size="10" fill="var(--muted)">' + tenants + ' tenants (rows) over '
      + n + ' nodes (columns), drawn from seed ' + seed + '</text>';
    for (i = 0; i < tenants; i += 1) {
      var y = 18 + i * rh, overlap = 0;
      for (j = 0; j < sets[i].length; j += 1) if (sets[0].indexOf(sets[i][j]) >= 0) overlap += 1;
      var tone = i === 0 ? '--cyan' : (overlap === k ? '--red' : (overlap > 0 ? '--amber' : '--line-strong'));
      for (j = 0; j < n; j += 1) {
        var on = sets[i].indexOf(j) >= 0;
        s += '<rect x="' + (40 + j * cw) + '" y="' + y + '" width="' + Math.max(2, cw - 1.5)
          + '" height="' + Math.max(2, rh - 1.5) + '" rx="1.5" fill="var(' + (on ? tone : '--panel-2')
          + ')" opacity="' + (on ? '0.95' : '0.5') + '" />';
      }
      s += '<text x="0" y="' + (y + rh - 2) + '" font-size="9" fill="var(' + tone + ')">t'
        + (i + 1) + (i === 0 ? '' : ' ' + overlap) + '</text>';
    }
    var by = 26 + tenants * rh;
    s += '<text x="0" y="' + by + '" font-size="10" fill="var(--muted)">the number beside each tenant is '
      + 'how many of your ' + k + ' nodes it shares</text>'
      + '<text x="0" y="' + (by + 14) + '" font-size="10" fill="var(--red)">in this draw '
      + same + ' of ' + (tenants - 1) + ' tenants hold your exact set (expected '
      + Rfixed(Rmul(ident, R(BigInt(tenants - 1), 1n)), 3) + ') and ' + none + ' share no node at all '
      + '(expected ' + Rfixed(Rmul(dis, R(BigInt(tenants - 1), 1n)), 3) + ')</text>';
    grid.innerHTML = s;

    status.innerHTML = 'With <strong>n = ' + n + '</strong> and <strong>k = ' + k + '</strong> there are '
      + group(shards) + ' distinct shards. Two tenants share no node at all with probability <strong>'
      + Rtext(dis) + '</strong> = ' + Rpct(dis, 3) + ', and hold the identical set with probability <strong>'
      + Rtext(ident) + '</strong> = ' + Rpct(ident, 4) + '. Only the second is an outage: a tenant that '
      + 'overlaps you in ' + (k > 1 ? 'some but not all of your nodes still has the rest' : 'your single node has nothing else')
      + '. One bad node degrades ' + Rtext(blast) + ' of all tenants and takes down none of them'
      + (k === 1 ? ' &mdash; except at k = 1, where degraded and down are the same thing' : '')
      + '. That is the whole idea: overlap is common, and a full collision is '
      + (Rzero(ident) ? '&mdash;' : Rfixed(Rdiv(dis, ident), 0) + ' times rarer than missing entirely')
      + '.';
  }

  [nS, kS, tS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Blast radius and shuffle sharding",
        subtitle="Two tenants, k nodes each, and the probability that one of them takes the other down",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the fleet and the shard size"),
        panel_intro=cfg.get(
            "panel_intro",
            "The two probabilities are ratios of binomial coefficients, computed exactly; the "
            "assignment beneath them is drawn from a seed so the counts can be checked by eye.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "nines": _nines,
    "mtbf": _mtbf,
    "series": _series,
    "parallel": _parallel,
    "kofn": _kofn,
    "correlated": _correlated,
    "budget": _budget,
    "retry": _retry,
    "storm": _storm,
    "backoff": _backoff,
    "shed": _shed,
    "durability": _durability,
    "shuffle": _shuffle,
}

MODES = tuple(sorted(_MODES))


def avail_lab(cfg):
    """Course 5's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, not defensiveness. A kit that quietly fell back
    to a default would render a finished-looking page carrying another
    lesson's widget: the markup assertions pass, labcheck passes, and the
    reader is shown the wrong lesson's arithmetic under the right lesson's
    title. That failure is invisible to every other check in the repository,
    so it has to be impossible here.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "avail_lab: unknown mode %r; the thirteen modes of course 5 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["avail_lab", "AVAILKIT_JS", "MODES"]
