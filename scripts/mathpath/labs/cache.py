"""Course 4: Caching and Hit Rates -- one kit, eight modes, one arithmetic.

A cache is one number, the miss rate, and every decision about a cache is
arithmetic on that number. So the modes here are the six things the miss rate
is made of or does: what it costs the backend, what it costs the latency
distribution, what the skew of the workload lets it be, what a replacement
policy can reach on a trace, what a TTL trades away, and what happens in the
second after a hot key expires.

Four decisions run through all eight.

  THE HIT RATE IS A RATIO OF HARMONICS, AND IT IS EXACT. Under a Zipf
  popularity p_i proportional to 1/i^s, caching the top C of N keys hits
  H(C,s)/H(N,s) of the requests. `zipfHit` in sysdesign_core.py computes it
  over BigInt rationals, and the reader moves C, N and s and watches it. That
  ratio is the whole reason a small cache of a skewed workload is worth
  building, and it is also the reason a bigger one stops being worth it: at
  N = 50 and s = 2 the ninetieth per cent costs five keys and the ninety-ninth
  costs twenty-eight.

  PAST ABOUT FIFTY KEYS THE EXACT FORM STOPS BEING READABLE. H(50,2) is a
  fraction whose denominator runs to forty-three digits, and a page that
  prints it has stopped communicating. `harmonicApprox` is the core's rounding function for
  exactly this, and `zipfShare` below switches to it above a stated limit,
  returns `rounded: true`, and the three modes that call it say on their face
  that they have switched and that the figure is no longer exact.

  FARTHEST-IN-FUTURE IS A BOUND, NOT A POLICY. `replayPolicy(trace, k, 'opt')`
  lives in the core rather than here because it is the bound the replacement
  lesson rests on: no online policy beats it, and on the ten-reference trace
  A B C A B D A B C D with three slots it gets 1/2 where LRU gets 2/5 and FIFO
  gets 1/5. `replace` shows it beside the three runnable policies and says that
  it cannot be run -- it reads the future. WHY it is optimal is Algorithms'
  `greedy-algorithms-and-matroids/optimal-caching`; this course cites that
  proof and does not repeat it. What this course owns is the other direction:
  Belady's anomaly, FIFO getting WORSE with a bigger cache, which `replace`
  finds by scanning k on the reader's own trace rather than asserting.

  A REQUEST HIT RATE AND A BYTE HIT RATE ARE DIFFERENT NUMBERS. `byteHit` below
  weights each rank by its object size, and because object size grows with rank
  -- popular objects are small -- the two come apart. At size exponent b = 0
  they are equal, which is the control; at b = s the byte hit rate collapses to
  C/N, the uniform rate, exactly. Neither is asserted: both come out of the
  same sum.

The modes, and the lesson each belongs to:

  hitrate/load    L1  (1-h)lambda, the backend's rho, and the wait it leaves
  hitrate/latency L2  h*t_hit + (1-h)*t_miss, and the p99 that steps
  zipf            L3  the top-k share H(k,s)/H(N,s), against uniform k/N
  size            L4  the C that reaches a target h, and what the next nine costs
  replace         L5  FIFO, LRU, LFU and farthest-in-future, and the anomaly
  ttl             L6  the piecewise stale fraction, beside a timeline that runs
  stampede        L7  lambda*d through the miss window, and 1 with coalescing
  write           L8  distinct keys per flush, the ratio, the bytes at risk
  levels          L9  (1-h1)(1-h2|miss), and the conditional latency
  hitrate/bytes   L10 origin bytes and cost, from a byte hit rate that is derived
"""

import json

from .algebra_core import RATIONAL_JS
from .common import Lab
from .sysdesign_core import APPROX_JS, HARMONIC_JS, QUEUE_JS, RCEIL_JS, REPLAY_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

CACHE_JS = r"""
  /* ---------------------------------------------------------------- output

     algebra_core's Rdec goes through Number(a.n)/Number(a.d), and this course
     produces rationals a double cannot hold: H(50,2) has a forty-three-digit
     denominator and a byte weight at b - s = 2 over fifty ranks is worse. So
     the decimals here are long division in BigInt, rounded half up at the last
     digit printed, exact at every size up to that one rounding. */
  function Rshow(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);          /* round half up */
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }
  /* A percentage of an exact probability, exact until the last digit printed. */
  function Rpercent(a, places) {
    return Rshow(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }
  /* A float for PLOTTING only. Never for a figure: it goes through Rshow, so
     it cannot be the NaN that Number(huge)/Number(huge) produces. */
  function Rfloat(a) { return parseFloat(Rshow(a, 9)); }
  /* Digit grouping. 1000000 and 1 000 000 are the same number and only one of
     them can be read at a glance. */
  function groupNum(value) {
    var s = String(value), sign = '';
    if (s.charAt(0) === '-') { sign = '-'; s = s.slice(1); }
    return sign + s.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  }
  /* Decimal byte units, which is what egress is billed in: 1 GB = 10^9 B. */
  function bytesText(bytes) {
    var b = Number(bytes);
    if (b >= 1000000000) return Rshow(R(BigInt(bytes), 1000000000n), 2) + ' GB';
    if (b >= 1000000) return Rshow(R(BigInt(bytes), 1000000n), 2) + ' MB';
    if (b >= 1000) return Rshow(R(BigInt(bytes), 1000n), 2) + ' kB';
    return groupNum(bytes) + ' B';
  }
  /* Money. Held in cents so that a price of a tenth of a cent per gigabyte is
     an integer and a monthly bill is an exact fraction of a dollar. */
  function moneyText(cents) {
    return '$' + groupNum(Rshow(Rdiv(cents, R(100n, 1n)), 2));
  }

  /* ============ L1: the backend sees the MISS rate, not the hit rate ========

     Everything the backend experiences is (1 - h)*lambda. That is why 90% to
     99% is a tenfold cut in backend load rather than "nine per cent better":
     the quantity that moved is 1/10 to 1/100, and the ratio of those is 10. */
  function backendRate(lam, h) { return Rmul(Rsub(R(1n, 1n), h), lam); }
  function backendRho(lam, h, cap) { return Rdiv(backendRate(lam, h), cap); }
  /* How many times smaller the backend load is at hTo than at hFrom. The whole
     of L1 in one fraction: at 90% and 99% this is 10. */
  function missMultiple(hFrom, hTo) {
    var to = Rsub(R(1n, 1n), hTo);
    if (Rzero(to)) return null;                       /* a perfect cache has no ratio */
    return Rdiv(Rsub(R(1n, 1n), hFrom), to);
  }

  /* ============ L2: an expectation, and a percentile that is not one ========

     The mean is h*t_hit + (1-h)*t_miss, a weighted average that lands between
     the two and equals neither. The percentile is a RANK on a two-atom
     distribution: P(X <= t_hit) = h, so the q-quantile is t_hit exactly when
     h >= q and t_miss otherwise. It does not interpolate and it does not move
     smoothly -- it steps, once, at h = q. That step is the lesson: at a 99%
     hit rate the p99 is still the miss latency, and at 99.1% it is not. */
  function meanLatency(h, tHit, tMiss) {
    return Radd(Rmul(h, tHit), Rmul(Rsub(R(1n, 1n), h), tMiss));
  }
  function latencyQuantile(h, tHit, tMiss, q) {
    return Rcmp(h, q) >= 0 ? tHit : tMiss;
  }
  /* The hit rate at which that quantile stops being the miss latency. It IS q,
     and saying so is the point: to move the p99 you need h > 0.99. */
  function quantileFlip(q) { return q; }

  /* ================= L3, L4, L10: Zipf popularity, exactly =================

     p_i proportional to 1/i^s over N keys, so the top-C share is
     H(C,s)/H(N,s) -- which is zipfHit in sysdesign_core.py. The exponent is an
     integer here and the pages say why: at a fractional s every term 1/i^s is
     irrational and there is no exact fraction to print at all. s = 0 is the
     uniform control, where H(n,0) = n and the share collapses to C/N. */

  /* i^e as an exact rational, for e of either sign. The negative side is what
     a size profile needs when popular objects are the LARGE ones. */
  function rankTerm(i, e) {
    var p = 1n, kb = BigInt(i), m = e < 0 ? -e : e, j;
    for (j = 0; j < m; j += 1) p *= kb;
    return e < 0 ? R(1n, p) : R(p, 1n);
  }
  /* The probability of rank i itself: (1/i^s)/H(N,s). */
  function zipfProb(i, n, s) { return Rdiv(rankTerm(i, -s), harmonic(n, s)); }

  /* The top-C share, exact below the limit and ROUNDED above it.

     harmonic() is exact and costs O(n*s) BigInt operations against a growing
     denominator; it is comfortable to about fifty keys, which is also where
     the printed fraction stops being readable by a human. Past that the core's
     harmonicApprox rounds, and this returns rounded: true so that the caller
     can say so on the page. A lab that switched silently would be telling the
     reader that an approximation is an exact fraction. */
  function zipfShare(c, n, s, limit) {
    if (c <= 0) return { rounded: false, exact: R(0n, 1n), value: 0 };
    if (c >= n) return { rounded: false, exact: R(1n, 1n), value: 1 };
    if (n <= limit) {
      var r = zipfHit(c, n, s);
      return { rounded: false, exact: r, value: Rfloat(r) };
    }
    return { rounded: true, exact: null, value: harmonicApprox(c, s) / harmonicApprox(n, s) };
  }

  /* The smallest C whose share reaches the target. An exact scan with a
     running prefix, so H(N,s) is summed once rather than C times. Returns N
     when no prefix reaches it, which can only happen at target > 1. */
  function sizeForTarget(n, s, target) {
    var Hn = harmonic(n, s), acc = R(0n, 1n), i;
    for (i = 1; i <= n; i += 1) {
      acc = Radd(acc, rankTerm(i, -s));
      if (Rcmp(Rdiv(acc, Hn), target) >= 0) return i;
    }
    return n;
  }
  /* The same search once the catalogue is past the exact limit. It rounds,
     because harmonicApprox rounds, and sizeTarget below labels it. */
  function sizeForTargetApprox(n, s, target) {
    var hn = harmonicApprox(n, s), t = Rfloat(target), acc = 0, i;
    for (i = 1; i <= n; i += 1) {
      acc += 1 / Math.pow(i, s);
      if (acc / hn >= t) return i;
    }
    return n;
  }
  function sizeTarget(n, s, target, limit) {
    if (n <= limit) return { c: sizeForTarget(n, s, target), rounded: false };
    return { c: sizeForTargetApprox(n, s, target), rounded: true };
  }
  /* h(C) for every C from 1 to N, for drawing the curve the target is read off.
     Plot values only -- every figure the page states comes from zipfShare. */
  function hitCurve(n, s, limit) {
    var out = [], i;
    if (n <= limit) {
      var Hn = harmonic(n, s), acc = R(0n, 1n);
      for (i = 1; i <= n; i += 1) { acc = Radd(acc, rankTerm(i, -s)); out.push(Rfloat(Rdiv(acc, Hn))); }
      return out;
    }
    var hn = harmonicApprox(n, s), a = 0;
    for (i = 1; i <= n; i += 1) { a += 1 / Math.pow(i, s); out.push(a / hn); }
    return out;
  }

  /* ---- L10: the same sum, weighted by size, which is a different number ----

     A CDN is billed in bytes, so the hit rate that matters is a BYTE hit rate:
     sum over the cached ranks of p_i * size_i, over the same sum across all
     ranks. With size_i proportional to i^b the weights are i^(b-s), so this is
     the identical harmonic ratio at exponent s - b, and three cases fall out
     of one formula rather than out of three assertions:

       b = 0   every object the same size    byte hit rate  =  request hit rate
       b = s   size grows exactly as fast as popularity falls    =  C/N, uniform
       b > 0   popular objects are smaller   byte hit rate  <  request hit rate

     The last is the real shape of a CDN workload and the reason the two
     numbers must not be confused: the cheap hits are the small ones. */
  function byteWeight(n, s, b) {
    var total = R(0n, 1n), i;
    for (i = 1; i <= n; i += 1) total = Radd(total, rankTerm(i, b - s));
    return total;
  }
  function byteHit(c, n, s, b) {
    if (c <= 0) return R(0n, 1n);
    if (c >= n) return R(1n, 1n);
    return Rdiv(byteWeight(c, s, b), byteWeight(n, s, b));
  }
  /* The same two sums in floating point, for a catalogue past the exact limit.
     harmonicApprox cannot stand in for this: its exponent must be at least 0
     and b - s is routinely negative here, which is the ordinary case of large
     unpopular objects. Summed term by term, and every caller says it rounds. */
  function byteWeightApprox(n, s, b) {
    var t = 0, i;
    for (i = 1; i <= n && i <= 100000; i += 1) t += Math.pow(i, b - s);
    return t;
  }
  function byteHitApprox(c, n, s, b) {
    if (c <= 0) return 0;
    if (c >= n) return 1;
    return byteWeightApprox(c, s, b) / byteWeightApprox(n, s, b);
  }
  /* The object at rank i, in bytes, under that profile. */
  function objectBytes(i, b, baseBytes) {
    return Rmul(R(BigInt(baseBytes), 1n), rankTerm(i, b));
  }
  /* What the origin still has to serve, and what a month of it costs. Cents
     per gigabyte is an integer, so the bill is an exact fraction of a cent. */
  function originBytes(totalBytes, bHit) { return Rmul(totalBytes, Rsub(R(1n, 1n), bHit)); }
  function egressCost(bytesPerDay, centsPerGb, days) {
    return Rmul(Rdiv(bytesPerDay, R(1000000000n, 1n)), Rmul(centsPerGb, R(BigInt(days), 1n)));
  }

  /* ============= L5: replacement on a trace, stepped and counted ===========

     replayPolicy in sysdesign_core.py counts hits and is the tested one; it
     does not report the cache contents, and a lesson whose point is that you
     can WATCH a policy make its mistake needs them. So this steps the same
     rules and mathcheck.js pins it against the core on every policy the core
     implements. The one it does not implement is LFU, whose rule is stated
     here rather than inherited: evict the smallest use count, ties broken by
     insertion order, and a count dies with the entry it belongs to.

     An unknown policy throws. The core's replayPolicy quietly treats anything
     it does not recognise as FIFO, which would show a reader a FIFO run under
     an LFU heading and nothing downstream would notice. */
  function replayTrace(trace, k, policy) {
    if (policy !== 'fifo' && policy !== 'lru' && policy !== 'lfu' && policy !== 'opt') {
      throw new Error('replayTrace: unknown policy ' + policy);
    }
    var cache = [], count = {}, hits = 0, steps = [], i, j;
    for (i = 0; i < trace.length; i += 1) {
      var key = trace[i], at = cache.indexOf(key), evicted = null, hit = at >= 0;
      if (hit) {
        hits += 1;
        if (policy === 'lru') { cache.splice(at, 1); cache.push(key); }
        count[key] += 1;
      } else {
        if (cache.length >= k) {
          var victim = 0;
          if (policy === 'opt') {
            /* evict whichever resident key is next used farthest ahead, or
               never used again -- the bound, and the one rule that cannot be
               run online because it reads the rest of the trace. */
            var best = -1;
            for (j = 0; j < cache.length; j += 1) {
              var next = trace.indexOf(cache[j], i + 1);
              if (next === -1) { victim = j; best = Infinity; break; }
              if (next > best) { best = next; victim = j; }
            }
          } else if (policy === 'lfu') {
            var low = -1;
            for (j = 0; j < cache.length; j += 1) {
              var c = count[cache[j]];
              if (low < 0 || c < low) { low = c; victim = j; }
            }
          }
          evicted = cache[victim];
          cache.splice(victim, 1);
          delete count[evicted];
        }
        cache.push(key);
        count[key] = 1;
      }
      steps.push({ key: key, hit: hit, evicted: evicted, cache: cache.slice() });
    }
    return {
      steps: steps, hits: hits, misses: trace.length - hits,
      rate: trace.length ? R(BigInt(hits), BigInt(trace.length)) : R(0n, 1n)
    };
  }

  /* Misses at every cache size from 1 to kmax. */
  function missBySize(trace, policy, kmax) {
    var out = [], k;
    for (k = 1; k <= kmax; k += 1) out.push(replayTrace(trace, k, policy).misses);
    return out;
  }
  /* Belady's anomaly, FOUND rather than asserted: the first cache size whose
     next size up misses MORE. FIFO is not a stack algorithm, so its miss count
     is not monotone in k; LRU, LFU-by-this-rule on a stack trace and OPT come
     back null on the traces this lesson uses, and the page reports which.
     Returning the actual k and the two counts is what lets the page name the
     anomaly on the reader's own trace instead of promising it. */
  function firstAnomaly(trace, policy, kmax) {
    var m = missBySize(trace, policy, kmax), k;
    for (k = 0; k + 1 < m.length; k += 1) {
      if (m[k + 1] > m[k]) return { k: k + 1, up: k + 2, from: m[k], to: m[k + 1] };
    }
    return null;
  }
  /* The reader's own reference string. Keys are alphanumeric tokens; anything
     else is a separator, so "A B C" and "A,B,C" and "a-b-c" all parse. */
  function parseTrace(text) {
    var raw = String(text).toUpperCase().split(/[^A-Z0-9]+/), out = [], i;
    for (i = 0; i < raw.length; i += 1) if (raw[i]) out.push(raw[i]);
    return out;
  }
  /* The distinct keys of a trace, in first-use order: the compulsory misses no
     policy and no cache size can avoid. */
  function traceKeys(trace) {
    var seen = {}, out = [], i;
    for (i = 0; i < trace.length; i += 1) {
      if (!Object.prototype.hasOwnProperty.call(seen, trace[i])) { seen[trace[i]] = true; out.push(trace[i]); }
    }
    return out;
  }

  /* ==================== L6: a TTL is a staleness budget ====================

     Under updates every U and a TTL of T, with the phase between them uniform,
     the expected stale fraction is piecewise:

       T <= U    T/(2U)        an update lands inside the window with
                               probability T/U, half the window old on average
       T >= U    1 - U/(2T)    the window outlives the update, so it is stale
                               for all but the first U/2 of it on average

     Both halves come from E[max(0, T - G)]/T with G uniform on [0,U), and they
     agree at T = U, where both give 1/2. */
  function staleFraction(T, U) {
    var two = R(2n, 1n);
    if (Rcmp(T, U) <= 0) return Rdiv(T, Rmul(two, U));
    return Rsub(R(1n, 1n), Rdiv(U, Rmul(two, T)));
  }
  /* What a short TTL costs: a key read lambda times a second and expiring
     every T seconds misses once per TTL, so the miss rate is 1/(lambda*T),
     which is 1 once the TTL is shorter than the gap between reads. */
  function ttlMissRate(lamKey, T) {
    var d = Rmul(lamKey, T);
    if (Rcmp(d, R(1n, 1n)) <= 0) return R(1n, 1n);
    return Rinv(d);
  }
  /* The first update STRICTLY after t, under updates at phase + kU. Strictly,
     because a refresh at the same instant as an update picks up the new value:
     that boundary is the difference between a stale fraction and a wrong one. */
  function nextUpdateAfter(t, phase, U) {
    var k = Rfloor(Rdiv(Rsub(t, phase), U)) + 1n;
    return Radd(phase, Rmul(R(k, 1n), U));
  }
  /* One concrete run, so the model's assumptions are on the page rather than
     in a footnote: refreshes at 0, T, 2T, ..., updates at phase + kU, and the
     copy is stale from the first update inside a window until the window ends. */
  function staleRun(T, U, phase, windows) {
    var spans = [], stale = R(0n, 1n), j;
    for (j = 0; j < windows; j += 1) {
      var lo = Rmul(R(BigInt(j), 1n), T), hi = Radd(lo, T);
      var g = nextUpdateAfter(lo, phase, U);
      if (Rcmp(g, hi) < 0) { spans.push([g, hi]); stale = Radd(stale, Rsub(hi, g)); }
    }
    var total = Rmul(R(BigInt(windows), 1n), T);
    return { spans: spans, stale: stale, total: total, fraction: Rdiv(stale, total) };
  }
  /* The same run averaged over m phases, sampled at the MIDPOINT of each of m
     equal slices of [0,U). This is the "uniform refresh phase" of the formula
     made into something that runs.

     Midpoints rather than left endpoints, and the difference is not cosmetic:
     the quantity being averaged is max(0, T - G), which is linear in G, and a
     midpoint sample is exact on a linear piece while a left-endpoint sample is
     not. At U = 60, T = 10 the left-endpoint grid includes G = 0 exactly --
     the case where an update lands on a refresh and nothing is ever stale --
     and misses the other end, which drags 1/12 down to 1/16. The average would
     then disagree with the formula for a reason that is about the sampling
     rather than about the model, which is the opposite of what this page is
     for. With midpoints the two agree wherever T divides U, and the residual
     disagreement is the model's own. */
  function staleAverage(T, U, m, windows) {
    var tot = R(0n, 1n), j;
    for (j = 0; j < m; j += 1) {
      tot = Radd(tot, staleRun(T, U, Rmul(R(BigInt(2 * j + 1), BigInt(2 * m)), U), windows).fraction);
    }
    return Rdiv(tot, R(BigInt(m), 1n));
  }

  /* ======================= L7: the stampede at expiry ======================

     The moment a hot key expires, every request that arrives before the first
     miss has been filled goes through to the backend. By Little's Law the
     number in that window is lambda*d -- a rate times a time, nothing else --
     and coalescing (one in-flight fill per key, the rest waiting on it) makes
     it one. A cache does not protect a backend during the miss window; the
     coalescing does. */
  function stampedeSize(lamKey, missMs) {
    return Rmul(lamKey, Rdiv(missMs, R(1000n, 1n)));
  }
  /* Whole requests, because three-tenths of a request does not arrive: the
     ceiling is what the backend actually counts. */
  function stampedeCount(lamKey, missMs) { return Rceil(stampedeSize(lamKey, missMs)); }
  /* The same burst from k independent hot keys expiring together, which is
     what a fleet-wide TTL set at deploy time produces. */
  function stampedeTotal(lamKey, missMs, keys) {
    return Rmul(stampedeSize(lamKey, missMs), R(BigInt(keys), 1n));
  }

  /* ==================== L8: write-through and write-back ===================

     Write-through sends every write. Write-back sends the DISTINCT keys in
     each flush window, so the ratio it buys is writes over distinct keys --
     and the price is a loss window: everything dirty at the moment of a crash
     is gone. The distinct count and the peak dirty set both come off the
     reader's own trace. */
  function distinctPerWindow(trace, w) {
    var out = [], i, j;
    if (w < 1) w = 1;
    for (i = 0; i < trace.length; i += w) {
      var seen = {}, keys = [], n = 0;
      for (j = i; j < i + w && j < trace.length; j += 1) {
        n += 1;
        if (!Object.prototype.hasOwnProperty.call(seen, trace[j])) { seen[trace[j]] = true; keys.push(trace[j]); }
      }
      out.push({ start: i, writes: n, keys: keys, distinct: keys.length });
    }
    return out;
  }
  function coalescing(trace, w) {
    var wins = distinctPerWindow(trace, w), writes = 0, distinct = 0, peak = 0, i;
    for (i = 0; i < wins.length; i += 1) {
      writes += wins[i].writes;
      distinct += wins[i].distinct;
      if (wins[i].distinct > peak) peak = wins[i].distinct;
    }
    return {
      windows: wins, writes: writes, distinct: distinct, peak: peak,
      ratio: distinct ? R(BigInt(writes), BigInt(distinct)) : R(0n, 1n)
    };
  }
  /* Bytes at risk: the largest dirty set a flush interval ever holds, times
     the object size. Not an average -- an average loss window is not what a
     crash takes. */
  function bytesAtRisk(peakDistinct, objBytes) {
    return Rmul(R(BigInt(peakDistinct), 1n), R(BigInt(objBytes), 1n));
  }

  /* ================= L9: the second level is CONDITIONAL ===================

     h2 is measured on the requests that MISSED L1, so it is a conditional
     probability and the global miss rate is the product (1-h1)(1-h2|miss), not
     a sum and not h2. The latency is the same conditioning read forwards:
     every request pays t1, the (1-h1) that miss pay t2, and the (1-h1)(1-h2)
     that miss both pay t3. */
  function globalHit(h1, h2) { return Radd(h1, Rmul(Rsub(R(1n, 1n), h1), h2)); }
  function globalMiss(h1, h2) { return Rmul(Rsub(R(1n, 1n), h1), Rsub(R(1n, 1n), h2)); }
  function levelLatency(h1, h2, t1, t2, t3) {
    return Radd(t1, Rmul(Rsub(R(1n, 1n), h1), Radd(t2, Rmul(Rsub(R(1n, 1n), h2), t3))));
  }
  /* The two wrong answers this lesson exists to kill, computed so that the
     page can print them beside the right one rather than describe them. */
  function naiveSumHit(h1, h2) { return Radd(h1, h2); }
  function conditionalShare(h1, h2) { return Rmul(Rsub(R(1n, 1n), h1), h2); }
"""

_CORE_JS = (RATIONAL_JS + RCEIL_JS + HARMONIC_JS + QUEUE_JS + REPLAY_JS
            + APPROX_JS + CACHE_JS)

# The catalogue size at which the exact harmonic stops being readable and the
# kit switches to the core's rounding function. Stated once, used by the three
# modes that print a share, and printed on each of their pages.
EXACT_LIMIT = 50


# ---------------------------------------------------------------------------
# Control furniture. The same three shapes every lab on the path uses, so a
# reader moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _preset(values):
    """Embed a mode's worked example as a JS literal.

    json.dumps output is valid JS, and the escape makes "</script>" structurally
    impossible -- the argument common.cfg_literal makes for its payloads.
    """
    return "  var PRESET = %s;\n" % json.dumps(values).replace("</", "<\\/")


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


def _lab(cfg, *, title, subtitle, markup, controls, script, panel_title, panel_intro):
    return Lab(
        title=title,
        subtitle=subtitle,
        markup=markup,
        controls=controls,
        script=script,
        panel_title=cfg.get("panel_title", panel_title),
        panel_intro=cfg.get("panel_intro", panel_intro),
    )


# ---------------------------------------------------------------------------
# L1 - hitrate, the load view
# ---------------------------------------------------------------------------


def _hitrate_load(cfg):
    lam = int(cfg.get("lam", 10000))
    hit_tenths = int(cfg.get("hit_tenths", 900))
    capacity = int(cfg.get("capacity", 2000))

    markup = (
        _toolbar(
            "Backend load is the miss rate",
            "(1 &minus; h)&lambda;, and the &rho; it leaves the backend at",
            [("cyan", "hits, absorbed"), ("red", "misses, forwarded"), ("amber", "backend capacity")],
        )
        + _stage(_svg("hlPlot", "0 0 520 180", "Arriving requests split into hits absorbed by the cache and misses forwarded to the backend."))
        + _table("hlTable")
        + _banner("hlStatus")
    )
    controls = (
        _range("hlLam", "&lambda; &mdash; arriving requests per second", 100, 50000, lam, 100)
        + _range("hlHit", "Hit rate h (tenths of a per cent)", 0, 999, hit_tenths, 1)
        + _range("hlCap", "Backend capacity &mu; (requests per second)", 50, 20000, capacity, 50)
        + _kpis(
            [
                ("Miss rate 1 &minus; h", "hlMiss"),
                ("Backend load (1 &minus; h)&lambda;", "hlLoad"),
                ("Backend &rho;", "hlRho"),
                ("Backend wait W (C3 L8)", "hlWait"),
            ]
        )
        + _hint(
            "hlHint",
            "State the miss rate, not the hit rate, whenever you are talking about the backend. "
            "Ninety and ninety-nine per cent sound adjacent; ten per cent and one per cent do not, "
            "and the backend sees the second pair.",
        )
    )

    script = _CORE_JS + _preset({"lam": lam, "hit": hit_tenths, "cap": capacity}) + r"""
  var lamS = document.getElementById('hlLam');
  var hitS = document.getElementById('hlHit');
  var capS = document.getElementById('hlCap');
  var plot = document.getElementById('hlPlot');
  var table = document.getElementById('hlTable');
  var status = document.getElementById('hlStatus');

  function redraw() {
    var lamV = +lamS.value, tenths = +hitS.value, cap = +capS.value;
    var lam = R(BigInt(lamV), 1n), h = R(BigInt(tenths), 1000n), mu = R(BigInt(cap), 1n);
    document.getElementById('hlLamOut').textContent = groupNum(lamV) + ' rps';
    document.getElementById('hlHitOut').textContent = Rpercent(h, 1);
    document.getElementById('hlCapOut').textContent = groupNum(cap) + ' rps';

    var miss = Rsub(R(1n, 1n), h);
    var load = backendRate(lam, h);
    var rho = backendRho(lam, h, mu);
    var q = mm1(load, mu);

    document.getElementById('hlMiss').textContent = Rtext(miss) + ' = ' + Rpercent(miss, 1);
    document.getElementById('hlLoad').textContent = Rshow(load, 1) + ' rps';
    document.getElementById('hlRho').textContent = Rtext(rho) + ' = ' + Rshow(rho, 4);
    document.getElementById('hlWait').textContent = q.stable
      ? Rshow(Rmul(q.W, R(1000n, 1n)), 2) + ' ms'
      : 'unbounded';

    /* Every row is recomputed from (1-h)lambda; nothing here is a stored
       table, and the ratio column is what makes the tenfold cut visible. */
    var rows = '', marks = [500, 900, 950, 990, 999], i;
    for (i = 0; i < marks.length; i += 1) {
      var hm = R(BigInt(marks[i]), 1000n), lm = backendRate(lam, hm), rm = Rdiv(lm, mu);
      var here = marks[i] === tenths;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + Rpercent(hm, 1) + (here ? ' &larr;' : '')
        + '</td><td>' + Rtext(Rsub(R(1n, 1n), hm)) + '</td><td>' + Rshow(lm, 1) + '</td><td>'
        + Rshow(rm, 4) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>hit rate h</th><th>miss rate 1 &minus; h</th>'
      + '<th>backend (1 &minus; h)&lambda;</th><th>backend &rho;</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var width = 480, hitPx = Math.max(0, width * Rfloat(h)), missPx = Math.max(0, width - hitPx);
    var capPx = Math.min(width, width * (cap / Math.max(lamV, 1)));
    var s = '<text x="20" y="18" font-size="11" fill="var(--muted)">' + groupNum(lamV)
      + ' requests a second arrive</text>'
      + '<rect x="20" y="26" width="' + hitPx + '" height="26" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<rect x="' + (20 + hitPx) + '" y="26" width="' + missPx + '" height="26" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<text x="24" y="44" font-size="11" fill="var(--on-accent)" font-weight="700">'
      + (hitPx > 90 ? Rpercent(h, 1) + ' hit' : '') + '</text>'
      + '<text x="20" y="82" font-size="11" fill="var(--muted)">of those, the misses reach the backend</text>'
      + '<rect x="20" y="90" width="' + Math.max(2, missPx) + '" height="26" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<text x="' + (26 + Math.max(2, missPx)) + '" y="108" font-size="11" fill="var(--red)" font-weight="700">'
      + Rshow(load, 1) + ' rps</text>'
      + '<line x1="' + (20 + capPx) + '" y1="70" x2="' + (20 + capPx) + '" y2="130" stroke="var(--amber)" '
      + 'stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + (24 + capPx) + '" y="128" font-size="10" fill="var(--amber)">capacity '
      + groupNum(cap) + '</text>'
      + '<line x1="20" y1="146" x2="500" y2="146" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="20" y="164" font-size="10" fill="var(--muted)">the bar above the dashed line is the part '
      + 'of the backend that is busy: &rho; = ' + Rshow(rho, 4) + '</text>';
    plot.innerHTML = s;

    var ten = missMultiple(R(9n, 10n), R(99n, 100n));
    status.innerHTML = 'At h = ' + Rpercent(h, 1) + ' the cache absorbs ' + Rshow(Rmul(h, lam), 1)
      + ' rps and the backend still sees <strong>' + Rshow(load, 1) + ' rps</strong>, which is '
      + Rtext(rho) + ' of its ' + groupNum(cap) + ' rps capacity'
      + (q.stable
          ? ' &mdash; a mean wait of <strong>' + Rshow(Rmul(q.W, R(1000n, 1n)), 2)
            + ' ms</strong> by the M/M/1 result of course 3.'
          : ' &mdash; past 1, so the backlog grows without bound and there is no mean wait to quote.')
      + ' Moving h from 90% to 99% does not make the backend 9% happier: it divides its load by '
      + '<strong>' + Rtext(ten) + '</strong>, because the quantity that moved is the miss rate, '
      + Rtext(R(1n, 10n)) + ' to ' + Rtext(R(1n, 100n)) + '.';
  }

  [lamS, hitS, capS].forEach(function (el) { el.addEventListener('input', redraw); });
  lamS.value = PRESET.lam; hitS.value = PRESET.hit; capS.value = PRESET.cap;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A hit rate is a statement about the backend",
        subtitle="(1 − h)λ is what arrives there, and ρ is what it does",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the traffic and the cache",
        panel_intro="The backend load is recomputed from (1 &minus; h)&lambda; every time you move a "
        "control, and the table beside it is the same formula at five hit rates.",
    )


# ---------------------------------------------------------------------------
# L2 - hitrate, the latency view
# ---------------------------------------------------------------------------


def _hitrate_latency(cfg):
    hit_tenths = int(cfg.get("hit_tenths", 950))
    t_hit = int(cfg.get("t_hit", 1))
    t_miss = int(cfg.get("t_miss", 40))

    markup = (
        _toolbar(
            "The mean and the percentile disagree",
            "h&middot;t<sub>hit</sub> + (1 &minus; h)&middot;t<sub>miss</sub>, against a rank",
            [("cyan", "hit latency"), ("red", "miss latency"), ("purple", "the mean"), ("amber", "the quantile")],
        )
        + _stage(_svg("hqPlot", "0 0 520 190", "The two-outcome latency distribution as a staircase, with the mean and three percentiles marked."))
        + _table("hqTable")
        + _banner("hqStatus")
    )
    controls = (
        _range("hqHit", "Hit rate h (tenths of a per cent)", 500, 999, hit_tenths, 1)
        + _range("hqHitMs", "Hit latency t<sub>hit</sub> (ms)", 1, 20, t_hit, 1)
        + _range("hqMissMs", "Miss latency t<sub>miss</sub> (ms)", 5, 400, t_miss, 1)
        + _kpis(
            [
                ("Mean latency", "hqMean"),
                ("p50", "hqP50"),
                ("p95", "hqP95"),
                ("p99", "hqP99"),
            ]
        )
        + _hint(
            "hqHint",
            "The mean is an average of two numbers and is equal to neither of them. The percentile "
            "is a rank on the same two outcomes, so it is always one of them, and it steps.",
        )
    )

    script = _CORE_JS + _preset({"hit": hit_tenths, "thit": t_hit, "tmiss": t_miss}) + r"""
  var hitS = document.getElementById('hqHit');
  var hitMsS = document.getElementById('hqHitMs');
  var missMsS = document.getElementById('hqMissMs');
  var plot = document.getElementById('hqPlot');
  var table = document.getElementById('hqTable');
  var status = document.getElementById('hqStatus');

  var QUANTS = [[R(1n, 2n), 'p50'], [R(19n, 20n), 'p95'], [R(99n, 100n), 'p99'], [R(999n, 1000n), 'p99.9']];

  function redraw() {
    var tenths = +hitS.value, th = +hitMsS.value, tm = +missMsS.value;
    var h = R(BigInt(tenths), 1000n), tHit = R(BigInt(th), 1n), tMiss = R(BigInt(tm), 1n);
    document.getElementById('hqHitOut').textContent = Rpercent(h, 1);
    document.getElementById('hqHitMsOut').textContent = th + ' ms';
    document.getElementById('hqMissMsOut').textContent = tm + ' ms';

    var mean = meanLatency(h, tHit, tMiss);
    document.getElementById('hqMean').textContent = Rtext(mean) + ' ms';
    var i, rows = '';
    for (i = 0; i < QUANTS.length; i += 1) {
      var q = QUANTS[i][0], v = latencyQuantile(h, tHit, tMiss, q);
      var isHit = Rcmp(h, q) >= 0;
      rows += '<tr><td>' + QUANTS[i][1] + '</td><td>' + Rtext(q) + '</td><td class="tone-'
        + (isHit ? 'cyan">' : 'red">') + Rtext(v) + ' ms</td><td>' + (isHit ? 'a hit' : 'a miss')
        + '</td><td>h ' + (isHit ? '&ge;' : '&lt;') + ' ' + Rpercent(q, 1) + '</td></tr>';
    }
    document.getElementById('hqP50').textContent = Rtext(latencyQuantile(h, tHit, tMiss, R(1n, 2n))) + ' ms';
    document.getElementById('hqP95').textContent = Rtext(latencyQuantile(h, tHit, tMiss, R(19n, 20n))) + ' ms';
    document.getElementById('hqP99').textContent = Rtext(latencyQuantile(h, tHit, tMiss, R(99n, 100n))) + ' ms';
    table.innerHTML = '<thead><tr><th>percentile</th><th>q</th><th>value</th><th>outcome</th>'
      + '<th>why</th></tr></thead><tbody>' + rows + '</tbody>';

    /* The staircase: P(X <= t) is h up to t_miss and 1 after it, which is why
       a percentile can only ever be one of the two values. */
    var x0 = 40, x1 = 470, span = Math.max(tm, 1);
    var xh = x0 + (x1 - x0) * (th / span), xm = x1;
    var yTop = 30, yBot = 140;
    var hFrac = Rfloat(h);
    var yH = yBot - (yBot - yTop) * hFrac;
    var s = '<line x1="' + x0 + '" y1="' + yBot + '" x2="' + x1 + '" y2="' + yBot
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + yTop + '" x2="' + x0 + '" y2="' + yBot
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="' + (x0 - 6) + '" y="' + (yTop + 4) + '" text-anchor="end" font-size="10" fill="var(--muted)">1</text>'
      + '<text x="' + (x0 - 6) + '" y="' + (yBot + 4) + '" text-anchor="end" font-size="10" fill="var(--muted)">0</text>'
      + '<line x1="' + x0 + '" y1="' + yBot + '" x2="' + xh + '" y2="' + yBot + '" stroke="var(--muted)" stroke-width="2" />'
      + '<line x1="' + xh + '" y1="' + yBot + '" x2="' + xh + '" y2="' + yH + '" stroke="var(--cyan)" stroke-width="3" />'
      + '<line x1="' + xh + '" y1="' + yH + '" x2="' + xm + '" y2="' + yH + '" stroke="var(--cyan)" stroke-width="3" />'
      + '<line x1="' + xm + '" y1="' + yH + '" x2="' + xm + '" y2="' + yTop + '" stroke="var(--red)" stroke-width="3" />'
      + '<text x="' + xh + '" y="' + (yBot + 16) + '" text-anchor="middle" font-size="10" fill="var(--cyan)">t_hit = '
      + th + '</text>'
      + '<text x="' + xm + '" y="' + (yBot + 16) + '" text-anchor="end" font-size="10" fill="var(--red)">t_miss = '
      + tm + '</text>';
    for (i = 0; i < QUANTS.length; i += 1) {
      var qq = Rfloat(QUANTS[i][0]), yq = yBot - (yBot - yTop) * qq;
      var landsHit = Rcmp(h, QUANTS[i][0]) >= 0;
      s += '<line x1="' + x0 + '" y1="' + yq + '" x2="' + (landsHit ? xh : xm) + '" y2="' + yq
        + '" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3" />'
        + '<text x="' + (x1 + 4) + '" y="' + (yq + 3) + '" font-size="9" fill="var(--amber)">'
        + QUANTS[i][1] + '</text>';
    }
    var xmean = x0 + (x1 - x0) * (Rfloat(mean) / span);
    s += '<line x1="' + xmean + '" y1="' + (yTop - 8) + '" x2="' + xmean + '" y2="' + (yBot + 4)
      + '" stroke="var(--purple)" stroke-width="2" />'
      + '<text x="' + (xmean + 4) + '" y="' + (yTop - 10) + '" font-size="10" fill="var(--purple)">mean '
      + Rshow(mean, 2) + ' ms</text>'
      + '<text x="' + x0 + '" y="176" font-size="10" fill="var(--muted)">the vertical axis is P(latency &le; t): '
      + 'it is flat at h between the two values, so no percentile can land between them</text>';
    plot.innerHTML = s;

    var p99IsMiss = Rcmp(h, R(99n, 100n)) < 0;
    status.innerHTML = 'At h = ' + Rpercent(h, 1) + ', ' + th + ' ms and ' + tm
      + ' ms the mean is <strong>' + Rtext(mean) + ' ms</strong> &mdash; a number no request ever takes. '
      + 'The p99 is <strong>' + Rtext(latencyQuantile(h, tHit, tMiss, R(99n, 100n))) + ' ms</strong>'
      + (p99IsMiss
          ? ', the MISS latency, because 1 &minus; h = ' + Rtext(Rsub(R(1n, 1n), h))
            + ' is at least a hundredth: more than one request in a hundred misses, so the '
            + 'hundredth-slowest is one of them. "99% hit rate, so the p99 is the hit latency" is '
            + 'the sentence this page exists to refute.'
          : ', the HIT latency, and it only just became one: it flips the moment h passes '
            + Rpercent(quantileFlip(R(99n, 100n)), 0) + ', not gradually. Drop h by a tenth of a '
            + 'per cent and the p99 jumps back to ' + tm + ' ms.')
      + ' The mean moved smoothly while you dragged; the percentile did not move at all and then '
      + 'moved by ' + Rtext(Rsub(tMiss, tHit)) + ' ms at once.';
  }

  [hitS, hitMsS, missMsS].forEach(function (el) { el.addEventListener('input', redraw); });
  hitS.value = PRESET.hit; hitMsS.value = PRESET.thit; missMsS.value = PRESET.tmiss;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Average latency under a cache",
        subtitle="An expectation over two outcomes, and the percentile that ignores it",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the two latencies and the hit rate",
        panel_intro="The mean is the weighted average of the two times. The percentiles are ranks "
        "on the same two outcomes, so each is one of them and each steps at its own q.",
    )


# ---------------------------------------------------------------------------
# L10 - hitrate, the bytes view
# ---------------------------------------------------------------------------


def _hitrate_bytes(cfg):
    n = int(cfg.get("n", 20))
    s = int(cfg.get("s", 1))
    c = int(cfg.get("c", 4))
    b = int(cfg.get("b", 1))
    gb_day = int(cfg.get("gb_day", 50000))
    cents_gb = int(cfg.get("cents_gb", 2))

    markup = (
        _toolbar(
            "Request hits and byte hits are two numbers",
            "a CDN is billed in bytes, and the popular objects are the small ones",
            [("cyan", "request hit rate"), ("purple", "byte hit rate"), ("red", "origin bytes"), ("muted", "object size by rank")],
        )
        + _stage(_svg("hbPlot", "0 0 520 210", "Requests by rank and bytes by rank drawn as two profiles, with the cached prefix shaded in each."))
        + _table("hbTable")
        + _banner("hbStatus")
    )
    controls = (
        _range("hbN", "Catalogue size N (objects)", 4, 120, n, 1)
        + _range("hbS", "Popularity exponent s", 0, 3, s, 1)
        + _range("hbC", "Objects cached at the edge, C", 1, 120, c, 1)
        + _range("hbB", "Size exponent b &mdash; size &prop; rank<sup>b</sup>", -1, 3, b, 1)
        + _range("hbEgress", "Total edge egress (GB/day)", 100, 200000, gb_day, 100)
        + _range("hbPrice", "Origin egress price (cents/GB)", 1, 20, cents_gb, 1)
        + _kpis(
            [
                ("Request hit rate", "hbReq"),
                ("Byte hit rate", "hbByte"),
                ("Origin GB/day", "hbOrigin"),
                ("Origin egress, 30 days", "hbCost"),
            ]
        )
        + _hint(
            "hbHint",
            "Both hit rates are the same harmonic ratio: the request one weights each rank by its "
            "popularity, the byte one by popularity times size. At b = 0 they are equal, which is "
            "the control; at b = s the byte hit rate is exactly C/N.",
        )
    )

    script = _CORE_JS + _preset(
        {"n": n, "s": s, "c": c, "b": b, "gb": gb_day, "price": cents_gb, "limit": EXACT_LIMIT}
    ) + r"""
  var nS = document.getElementById('hbN');
  var sS = document.getElementById('hbS');
  var cS = document.getElementById('hbC');
  var bS = document.getElementById('hbB');
  var gbS = document.getElementById('hbEgress');
  var priceS = document.getElementById('hbPrice');
  var plot = document.getElementById('hbPlot');
  var table = document.getElementById('hbTable');
  var status = document.getElementById('hbStatus');

  function redraw() {
    var n = +nS.value, s = +sS.value, b = +bS.value, gb = +gbS.value, price = +priceS.value;
    var c = Math.min(+cS.value, n);
    document.getElementById('hbNOut').textContent = n + ' objects';
    document.getElementById('hbSOut').textContent = 's = ' + s;
    document.getElementById('hbCOut').textContent = 'top ' + c + ' (' + Rpercent(R(BigInt(c), BigInt(n)), 1) + ' of the catalogue)';
    document.getElementById('hbBOut').textContent = 'b = ' + b;
    document.getElementById('hbEgressOut').textContent = groupNum(gb) + ' GB/day';
    document.getElementById('hbPriceOut').textContent = price + '&cent;/GB';

    var rounded = n > PRESET.limit;
    var req = zipfShare(c, n, s, PRESET.limit);
    var byteR = rounded ? null : byteHit(c, n, s, b);
    var byteValue = rounded ? byteHitApprox(c, n, s, b) : Rfloat(byteR);

    document.getElementById('hbReq').textContent = req.rounded
      ? '~' + (100 * req.value).toFixed(2) + '%'
      : Rpercent(req.exact, 2);
    document.getElementById('hbByte').textContent = rounded
      ? '~' + (100 * byteValue).toFixed(2) + '%'
      : Rpercent(byteR, 2);

    /* Origin bytes and the bill, from the BYTE hit rate -- the whole point of
       the page is that using the request one here is the error. */
    var totalBytes = Rmul(R(BigInt(gb), 1n), R(1000000000n, 1n));
    var bh = rounded ? R(BigInt(Math.round(1000000 * byteValue)), 1000000n) : byteR;
    var origin = originBytes(totalBytes, bh);
    var originGb = Rdiv(origin, R(1000000000n, 1n));
    var cost = egressCost(origin, R(BigInt(price), 1n), 30);
    var wrongOrigin = originBytes(totalBytes, rounded
      ? R(BigInt(Math.round(1000000 * req.value)), 1000000n) : req.exact);
    var wrongCost = egressCost(wrongOrigin, R(BigInt(price), 1n), 30);

    document.getElementById('hbOrigin').textContent = groupNum(Rshow(originGb, 0)) + ' GB';
    document.getElementById('hbCost').textContent = moneyText(cost);

    var rows = '', shown = Math.min(n, 8), i;
    for (i = 1; i <= shown; i += 1) {
      var p = rounded ? null : zipfProb(i, n, s);
      var size = objectBytes(i, b, 100000);
      rows += '<tr><td>' + i + '</td><td>' + (rounded ? '&mdash;' : Rtext(p)) + '</td><td>'
        + bytesText(size.n / size.d) + '</td><td>'
        + (rounded ? '&mdash;' : Rtext(Rmul(p, rankTerm(i, b)))) + '</td><td>'
        + (i <= c ? '<span class="tone-cyan">cached</span>' : '<span class="tone-red">origin</span>')
        + '</td></tr>';
    }
    if (n > shown) rows += '<tr><td colspan="5" class="tone-muted">&hellip; ' + (n - shown)
      + ' further ranks, all computed</td></tr>';
    table.innerHTML = '<thead><tr><th>rank i</th><th>p<sub>i</sub></th><th>size at 100 kB base</th>'
      + '<th>p<sub>i</sub> &times; rank<sup>b</sup></th><th>where it is served</th></tr></thead><tbody>'
      + rows + '</tbody>';

    /* Two profiles: the share of REQUESTS each rank takes, and the share of
       BYTES. The cached prefix is shaded in both, and the gap between the two
       shaded areas is the whole lesson. */
    var x0 = 30, wid = 460, barW = Math.max(1.5, wid / n - 1);
    var pv = [], bv = [], pmax = 0, bmax = 0;
    var Hs = rounded ? null : harmonic(n, s), Wb = rounded ? null : byteWeight(n, s, b);
    for (i = 1; i <= n; i += 1) {
      var pi = rounded ? (1 / Math.pow(i, s)) / harmonicApprox(n, s) : Rfloat(Rdiv(rankTerm(i, -s), Hs));
      var bi = rounded ? Math.pow(i, b - s) / byteWeightApprox(n, s, b)
                       : Rfloat(Rdiv(rankTerm(i, b - s), Wb));
      pv.push(pi); bv.push(bi);
      if (pi > pmax) pmax = pi;
      if (bi > bmax) bmax = bi;
    }
    var sSvg = '<text x="' + x0 + '" y="14" font-size="11" fill="var(--cyan)">share of REQUESTS by rank</text>';
    for (i = 0; i < n; i += 1) {
      var hgt = Math.max(1, 58 * (pv[i] / (pmax || 1)));
      sSvg += '<rect x="' + (x0 + i * (wid / n)) + '" y="' + (78 - hgt) + '" width="' + barW
        + '" height="' + hgt + '" fill="var(--cyan)" opacity="' + (i < c ? '0.95' : '0.28') + '" />';
    }
    sSvg += '<text x="' + x0 + '" y="100" font-size="11" fill="var(--purple)">share of BYTES by rank</text>';
    for (i = 0; i < n; i += 1) {
      var hgt2 = Math.max(1, 58 * (bv[i] / (bmax || 1)));
      sSvg += '<rect x="' + (x0 + i * (wid / n)) + '" y="' + (164 - hgt2) + '" width="' + barW
        + '" height="' + hgt2 + '" fill="var(--purple)" opacity="' + (i < c ? '0.95' : '0.28') + '" />';
    }
    var edge = x0 + c * (wid / n);
    sSvg += '<line x1="' + edge + '" y1="18" x2="' + edge + '" y2="170" stroke="var(--amber)" '
      + 'stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + (edge + 4) + '" y="182" font-size="10" fill="var(--amber)">cache edge at C = ' + c + '</text>'
      + '<text x="' + x0 + '" y="200" font-size="10" fill="var(--muted)">solid bars are cached: '
      + 'the left one covers ' + (100 * req.value).toFixed(1) + '% of the requests and '
      + (100 * byteValue).toFixed(1) + '% of the bytes</text>';
    plot.innerHTML = sSvg;

    var gap = req.value - byteValue;
    status.innerHTML = 'The edge holds the top ' + c + ' of ' + n + ' objects. That is <strong>'
      + (100 * req.value).toFixed(2) + '%</strong> of the requests but <strong>'
      + (100 * byteValue).toFixed(2) + '%</strong> of the bytes'
      + (b === 0
          ? ' &mdash; and they are equal, because at b = 0 every object is the same size and a '
            + 'byte hit rate is a request hit rate under another name. That is the control: move b '
            + 'off zero and watch them separate.'
          : (b === s
              ? ' &mdash; and the byte hit rate is exactly C/N = ' + Rtext(R(BigInt(c), BigInt(n)))
                + ', the UNIFORM rate, because at b = s size grows exactly as fast as popularity '
                + 'falls and every rank carries the same bytes.'
              : (gap > 0
                  ? ' &mdash; a gap of ' + (100 * gap).toFixed(2) + ' points, because the popular '
                    + 'objects are the small ones and caching them buys requests more cheaply than bytes.'
                  : ' &mdash; the byte rate is the HIGHER one here, because at b = ' + b
                    + ' the popular objects are the large ones. That is a thumbnail cache, not a CDN.')))
      + ' The bill follows the byte rate: <strong>' + groupNum(Rshow(originGb, 0))
      + ' GB/day</strong> to the origin, <strong>' + moneyText(cost) + '</strong> over thirty days. '
      + 'Billing from the request hit rate instead would have predicted ' + moneyText(wrongCost) + '.'
      + (rounded
          ? ' <span class="tone-red">Both rates above are rounded.</span> At N = ' + n
            + ' &mdash; past ' + PRESET.limit + ' &mdash; the exact harmonic is a fraction whose '
            + 'denominator runs to dozens of digits, so this page calls harmonicApprox and the '
            + 'figures carry a ~. Drop N to ' + PRESET.limit + ' or below for exact fractions.'
          : ' Every figure here is an exact fraction.');
  }

  [nS, sS, cS, bS, gbS, priceS].forEach(function (el) { el.addEventListener('input', redraw); });
  nS.value = PRESET.n; sS.value = PRESET.s; cS.value = PRESET.c; bS.value = PRESET.b;
  gbS.value = PRESET.gb; priceS.value = PRESET.price;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="CDN egress and origin load",
        subtitle="The byte hit rate is a different number, and it is the one on the invoice",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the catalogue, the skew and the size profile",
        panel_intro="The byte hit rate is not a second slider: it is computed from the same ranks, "
        "weighted by object size. Set b = 0 and the two rates coincide.",
    )


# ---------------------------------------------------------------------------
# L3 - zipf
# ---------------------------------------------------------------------------


def _zipf(cfg):
    n = int(cfg.get("n", 20))
    s = int(cfg.get("s", 1))
    k = int(cfg.get("k", 4))

    markup = (
        _toolbar(
            "Popularity is skewed",
            "p<sub>i</sub> &prop; 1/i<sup>s</sup>, so the top k carry H(k,s)/H(N,s)",
            [("cyan", "the top k"), ("muted", "the tail"), ("amber", "uniform k/N"), ("red", "rounded")],
        )
        + _stage(_svg("zfPlot", "0 0 520 200", "The Zipf rank curve with the top k shaded, and the cumulative share drawn over it."))
        + _table("zfTable")
        + _banner("zfStatus")
    )
    controls = (
        _range("zfN", "Catalogue size N (keys)", 4, 200, n, 1)
        + _range("zfS", "Zipf exponent s", 0, 3, s, 1)
        + _range("zfK", "Top k keys", 1, 200, k, 1)
        + _kpis(
            [
                ("H(k, s)", "zfHk"),
                ("H(N, s)", "zfHn"),
                ("Top-k share", "zfShare"),
                ("Uniform would give k/N", "zfUniform"),
            ]
        )
        + _hint(
            "zfHint",
            "s is the Zipf exponent, and nothing else on this course is called s. At s = 0 every "
            "key is equally popular and the share collapses to k/N; that is the misconception, "
            "computed rather than described.",
        )
    )

    script = _CORE_JS + _preset({"n": n, "s": s, "k": k, "limit": EXACT_LIMIT}) + r"""
  var nS = document.getElementById('zfN');
  var sS = document.getElementById('zfS');
  var kS = document.getElementById('zfK');
  var plot = document.getElementById('zfPlot');
  var table = document.getElementById('zfTable');
  var status = document.getElementById('zfStatus');

  function redraw() {
    var n = +nS.value, s = +sS.value, k = Math.min(+kS.value, n);
    document.getElementById('zfNOut').textContent = n + ' keys';
    document.getElementById('zfSOut').textContent = 's = ' + s + (s === 0 ? ' (uniform)' : (s === 1 ? ' (classic Zipf)' : ''));
    document.getElementById('zfKOut').textContent = 'top ' + k;

    var exact = n <= PRESET.limit;
    var share = zipfShare(k, n, s, PRESET.limit);
    var uniform = R(BigInt(k), BigInt(n));

    document.getElementById('zfHk').textContent = exact ? Rtext(harmonic(k, s)) : '~' + harmonicApprox(k, s).toFixed(6);
    document.getElementById('zfHn').textContent = exact ? Rtext(harmonic(n, s)) : '~' + harmonicApprox(n, s).toFixed(6);
    document.getElementById('zfShare').textContent = share.rounded
      ? '~' + (100 * share.value).toFixed(3) + '%'
      : Rtext(share.exact) + ' = ' + Rpercent(share.exact, 2);
    document.getElementById('zfUniform').textContent = Rtext(uniform) + ' = ' + Rpercent(uniform, 2);

    var rows = '', shown = Math.min(n, 8), i;
    for (i = 1; i <= shown; i += 1) {
      var p = exact ? zipfProb(i, n, s) : null;
      var cum = zipfShare(i, n, s, PRESET.limit);
      rows += '<tr><td>' + i + '</td><td>1/' + i + '<sup>' + s + '</sup></td><td>'
        + (exact ? Rtext(p) : '~' + ((1 / Math.pow(i, s)) / harmonicApprox(n, s)).toFixed(6)) + '</td><td>'
        + (cum.rounded ? '~' + (100 * cum.value).toFixed(3) + '%' : Rpercent(cum.exact, 2)) + '</td><td'
        + (i <= k ? ' class="tone-cyan">in the top k' : ' class="tone-muted">in the tail') + '</td></tr>';
    }
    if (n > shown) rows += '<tr><td colspan="5" class="tone-muted">&hellip; ranks ' + (shown + 1)
      + ' to ' + n + ', all computed the same way</td></tr>';
    table.innerHTML = '<thead><tr><th>rank i</th><th>weight</th><th>p<sub>i</sub></th>'
      + '<th>cumulative share</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var x0 = 34, wid = 450, top = 26, bot = 132;
    var vals = [], cums = [], pmax = 0;
    var Hs = exact ? harmonic(n, s) : null;
    for (i = 1; i <= n; i += 1) {
      var pi = exact ? Rfloat(Rdiv(rankTerm(i, -s), Hs)) : (1 / Math.pow(i, s)) / harmonicApprox(n, s);
      vals.push(pi);
      if (pi > pmax) pmax = pi;
      cums.push(zipfShare(i, n, s, PRESET.limit).value);
    }
    var barW = Math.max(1.2, wid / n - 1);
    var sSvg = '<line x1="' + x0 + '" y1="' + bot + '" x2="' + (x0 + wid) + '" y2="' + bot
      + '" stroke="var(--line-strong)" stroke-width="1" />';
    for (i = 0; i < n; i += 1) {
      var hgt = Math.max(1, (bot - top) * (vals[i] / (pmax || 1)));
      sSvg += '<rect x="' + (x0 + i * (wid / n)) + '" y="' + (bot - hgt) + '" width="' + barW
        + '" height="' + hgt + '" fill="var(--cyan)" opacity="' + (i < k ? '0.95' : '0.25') + '" />';
    }
    var path = '';
    for (i = 0; i < n; i += 1) {
      path += (i ? ' L ' : 'M ') + (x0 + (i + 0.5) * (wid / n)) + ' ' + (bot - (bot - top) * cums[i]);
    }
    sSvg += '<path d="' + path + '" fill="none" stroke="var(--purple)" stroke-width="2" />'
      + '<line x1="' + x0 + '" y1="' + (bot - (bot - top) * (k / n)) + '" x2="' + (x0 + wid) + '" y2="'
      + (bot - (bot - top) * (k / n)) + '" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="' + (x0 + wid) + '" y="' + (bot - (bot - top) * (k / n) - 4) + '" text-anchor="end" '
      + 'font-size="10" fill="var(--amber)">uniform: k/N = ' + Rpercent(uniform, 1) + '</text>'
      + '<line x1="' + (x0 + k * (wid / n)) + '" y1="' + top + '" x2="' + (x0 + k * (wid / n)) + '" y2="'
      + bot + '" stroke="var(--amber)" stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + x0 + '" y="18" font-size="11" fill="var(--cyan)">p_i by rank (bars)</text>'
      + '<text x="' + (x0 + 160) + '" y="18" font-size="11" fill="var(--purple)">cumulative share (line)</text>'
      + '<text x="' + x0 + '" y="' + (bot + 16) + '" font-size="10" fill="var(--muted)">rank 1</text>'
      + '<text x="' + (x0 + wid) + '" y="' + (bot + 16) + '" text-anchor="end" font-size="10" fill="var(--muted)">rank '
      + n + '</text>'
      + '<text x="' + x0 + '" y="' + (bot + 40) + '" font-size="10" fill="var(--muted)">'
      + 'the purple line reaches ' + (100 * (share.value)).toFixed(1) + '% at k = ' + k
      + '; the dashed amber line is where uniform popularity would have put it</text>';
    plot.innerHTML = sSvg;

    var ratio = share.value / Math.max(k / n, 1e-12);
    status.innerHTML = 'The top ' + k + ' of ' + n + ' keys is ' + Rpercent(uniform, 1)
      + ' of the catalogue and '
      + (share.rounded ? '<strong>~' + (100 * share.value).toFixed(3) + '%</strong>'
                       : '<strong>' + Rtext(share.exact) + ' = ' + Rpercent(share.exact, 2) + '</strong>')
      + ' of the requests &mdash; '
      + (s === 0
          ? 'exactly the same number, because s = 0 IS uniform popularity. This is the '
            + 'misconception the lesson names: cache 10% of the keys, get 10% of the requests. '
            + 'Raise s and watch it stop being true.'
          : ratio.toFixed(2) + ' times its share of the catalogue. That multiple is the whole '
            + 'reason a cache is worth building, and it is H(k,s)/H(N,s) divided by k/N, nothing more.')
      + (share.rounded
          ? ' <span class="tone-red">This figure is rounded.</span> Past N = ' + PRESET.limit
            + ' the exact harmonic stops being readable &mdash; H(50,2) alone has a forty-three-digit '
            + 'denominator &mdash; so the page switches to harmonicApprox, which sums in floating '
            + 'point. Below N = ' + PRESET.limit + ' every figure on this page is an exact fraction.'
          : ' Both harmonics above are exact fractions, summed term by term over BigInt.')
      + ' The exponent is an integer here because at a fractional s every term 1/i<sup>s</sup> is '
      + 'irrational and there is no exact fraction to print at all.';
  }

  [nS, sS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  nS.value = PRESET.n; sS.value = PRESET.s; kS.value = PRESET.k;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Popularity is skewed: Zipf",
        subtitle="The top-k share as a ratio of harmonic numbers, exact while it is readable",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the catalogue, the skew and k",
        panel_intro="H(k,s) and H(N,s) are summed term by term in the browser, and the share is "
        "their exact ratio. The amber line is what uniform popularity would have given.",
    )


# ---------------------------------------------------------------------------
# L4 - size
# ---------------------------------------------------------------------------


def _size(cfg):
    n = int(cfg.get("n", 50))
    s = int(cfg.get("s", 2))
    target_tenths = int(cfg.get("target_tenths", 900))

    markup = (
        _toolbar(
            "Cache size against hit rate",
            "h(C) = H(C,s)/H(N,s), and the C a target costs",
            [("cyan", "h(C)"), ("amber", "the target"), ("purple", "the C that reaches it"), ("red", "the next nine")],
        )
        + _stage(_svg("szPlot", "0 0 520 200", "The hit-rate curve against cache size, with the target line and the required C marked."))
        + _table("szTable")
        + _banner("szStatus")
    )
    controls = (
        _range("szN", "Catalogue size N (keys)", 10, 200, n, 1)
        + _range("szS", "Zipf exponent s", 0, 3, s, 1)
        + _range("szTarget", "Target hit rate (tenths of a per cent)", 500, 999, target_tenths, 1)
        + _kpis(
            [
                ("C for the target", "szC"),
                ("as a share of N", "szShare"),
                ("C for 90%", "szC90"),
                ("C for 99%", "szC99"),
            ]
        )
        + _hint(
            "szHint",
            "This replaces the stated hot fraction of course 1 lesson 9. There the working set was "
            "given as a percentage; here it comes out of the skew, and the curve shows why the "
            "number was never proportional to the cache size.",
        )
    )

    script = _CORE_JS + _preset({"n": n, "s": s, "target": target_tenths, "limit": EXACT_LIMIT}) + r"""
  var nS = document.getElementById('szN');
  var sS = document.getElementById('szS');
  var tS = document.getElementById('szTarget');
  var plot = document.getElementById('szPlot');
  var table = document.getElementById('szTable');
  var status = document.getElementById('szStatus');

  function redraw() {
    var n = +nS.value, s = +sS.value, tenths = +tS.value;
    var target = R(BigInt(tenths), 1000n);
    document.getElementById('szNOut').textContent = n + ' keys';
    document.getElementById('szSOut').textContent = 's = ' + s + (s === 0 ? ' (uniform)' : '');
    document.getElementById('szTargetOut').textContent = Rpercent(target, 1);

    var got = sizeTarget(n, s, target, PRESET.limit);
    var c90 = sizeTarget(n, s, R(9n, 10n), PRESET.limit);
    var c99 = sizeTarget(n, s, R(99n, 100n), PRESET.limit);
    var here = zipfShare(got.c, n, s, PRESET.limit);

    document.getElementById('szC').textContent = got.c + ' of ' + n + (got.rounded ? ' (rounded)' : '');
    document.getElementById('szShare').textContent = Rtext(R(BigInt(got.c), BigInt(n))) + ' = '
      + Rpercent(R(BigInt(got.c), BigInt(n)), 1);
    document.getElementById('szC90').textContent = c90.c + ' keys';
    document.getElementById('szC99').textContent = c99.c + ' keys';

    /* Diminishing returns, as the marginal contribution of each further key.
       Every row is recomputed; the "gain" column is the difference of two
       exact shares, not a slope read off a picture. */
    var rows = '', marks = [], i;
    var step = Math.max(1, Math.floor(n / 8));
    for (i = 1; i <= n; i += step) marks.push(i);
    if (marks[marks.length - 1] !== n) marks.push(n);
    var prev = null;
    for (i = 0; i < marks.length; i += 1) {
      var cShare = zipfShare(marks[i], n, s, PRESET.limit);
      var txt = cShare.rounded ? '~' + (100 * cShare.value).toFixed(3) + '%' : Rpercent(cShare.exact, 3);
      var gain = prev === null ? '&mdash;' : ((100 * (cShare.value - prev)) / Math.max(1, step)).toFixed(3) + ' pts/key';
      prev = cShare.value;
      rows += '<tr><td>' + marks[i] + '</td><td>' + txt + '</td><td>' + gain + '</td><td'
        + (marks[i] >= got.c ? ' class="tone-purple">reaches the target' : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>cache size C</th><th>h(C)</th><th>marginal gain</th>'
      + '<th></th></tr></thead><tbody>' + rows + '</tbody>';

    var curve = hitCurve(n, s, PRESET.limit);
    var x0 = 36, wid = 450, top = 24, bot = 150;
    var path = '', j;
    for (j = 0; j < curve.length; j += 1) {
      path += (j ? ' L ' : 'M ') + (x0 + (j + 1) * (wid / n)) + ' ' + (bot - (bot - top) * curve[j]);
    }
    var ty = bot - (bot - top) * Rfloat(target);
    var cx = x0 + got.c * (wid / n);
    var sSvg = '<line x1="' + x0 + '" y1="' + bot + '" x2="' + (x0 + wid) + '" y2="' + bot
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + top + '" x2="' + x0 + '" y2="' + bot
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<path d="' + path + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<line x1="' + x0 + '" y1="' + ty + '" x2="' + (x0 + wid) + '" y2="' + ty
      + '" stroke="var(--amber)" stroke-width="1.5" stroke-dasharray="4 3" />'
      + '<text x="' + (x0 + wid) + '" y="' + (ty - 5) + '" text-anchor="end" font-size="10" fill="var(--amber)">target '
      + Rpercent(target, 1) + '</text>'
      + '<line x1="' + cx + '" y1="' + top + '" x2="' + cx + '" y2="' + bot
      + '" stroke="var(--purple)" stroke-width="2" />'
      + '<circle cx="' + cx + '" cy="' + (bot - (bot - top) * curve[got.c - 1]) + '" r="4" fill="var(--purple)" />'
      + '<text x="' + (cx + 5) + '" y="' + (top + 12) + '" font-size="10" fill="var(--purple)">C = ' + got.c + '</text>'
      + '<text x="' + (x0 - 6) + '" y="' + (top + 4) + '" text-anchor="end" font-size="10" fill="var(--muted)">1</text>'
      + '<text x="' + (x0 - 6) + '" y="' + (bot + 4) + '" text-anchor="end" font-size="10" fill="var(--muted)">0</text>'
      + '<text x="' + x0 + '" y="' + (bot + 16) + '" font-size="10" fill="var(--muted)">C = 1</text>'
      + '<text x="' + (x0 + wid) + '" y="' + (bot + 16) + '" text-anchor="end" font-size="10" fill="var(--muted)">C = '
      + n + '</text>';
    var x90 = x0 + c90.c * (wid / n), x99 = x0 + c99.c * (wid / n);
    sSvg += '<line x1="' + x90 + '" y1="' + (bot + 22) + '" x2="' + x99 + '" y2="' + (bot + 22)
      + '" stroke="var(--red)" stroke-width="3" />'
      + '<text x="' + x0 + '" y="' + (bot + 42) + '" font-size="10" fill="var(--red)">the red bar is what the '
      + 'next nine costs: ' + c90.c + ' keys reach 90%, ' + c99.c + ' reach 99%</text>';
    plot.innerHTML = sSvg;

    var extra = c99.c - c90.c;
    status.innerHTML = 'At N = ' + n + ' and s = ' + s + ', reaching <strong>' + Rpercent(target, 1)
      + '</strong> takes <strong>' + got.c + '</strong> of the ' + n + ' keys &mdash; '
      + Rpercent(R(BigInt(got.c), BigInt(n)), 1) + ' of the catalogue, delivering '
      + (here.rounded ? '~' + (100 * here.value).toFixed(3) + '%' : Rpercent(here.exact, 3)) + '. '
      + 'Hit rate is not proportional to cache size: going from 90% to 99% costs '
      + (extra > 0
          ? '<strong>' + extra + ' more keys</strong>, ' + (c90.c > 0 ? (c99.c / c90.c).toFixed(1) : '&infin;')
            + ' times the cache for one more nine'
          : 'nothing here, because the catalogue is small enough that both land on the same C')
      + '. That is what the flattening curve is.'
      + (got.rounded
          ? ' <span class="tone-red">C is found by a rounded search.</span> At N = ' + n + ' &mdash; past '
            + PRESET.limit + ' &mdash; the prefix sums come from harmonicApprox rather than from exact '
            + 'harmonics, so a C on the boundary could be out by one. Below N = ' + PRESET.limit
            + ' the scan compares exact fractions and cannot be.'
          : ' The scan compares exact fractions, so the C above is the smallest one that reaches the target.');
  }

  [nS, sS, tS].forEach(function (el) { el.addEventListener('input', redraw); });
  nS.value = PRESET.n; sS.value = PRESET.s; tS.value = PRESET.target;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Cache size and hit rate",
        subtitle="Read the C off the curve, and see what the next nine costs",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the catalogue, the skew and the target",
        panel_intro="The required C is found by scanning exact prefix sums until the ratio reaches "
        "the target &mdash; nothing is read off the drawing.",
    )


# ---------------------------------------------------------------------------
# L5 - replace
# ---------------------------------------------------------------------------

_TRACES = [
    ("A B C A B D A B C D", "the course trace &mdash; A B C A B D A B C D"),
    ("1 2 3 4 1 2 5 1 2 3 4 5", "Belady's trace &mdash; 1 2 3 4 1 2 5 1 2 3 4 5"),
    ("A B C D E A B C D E A B", "a round robin &mdash; A B C D E A B C D E A B"),
    ("A A A B A A C A A A B A", "one hot key &mdash; A A A B A A C A A A B A"),
]

_POLICIES = [("fifo", "FIFO"), ("lru", "LRU"), ("lfu", "LFU"), ("opt", "OPT (farthest-in-future)")]


def _replace(cfg):
    trace = str(cfg.get("trace", "A B C A B D A B C D"))
    k1 = int(cfg.get("k1", 3))
    k2 = int(cfg.get("k2", 4))
    step = int(cfg.get("step", 10))

    markup = (
        _toolbar(
            "Four policies on one reference string",
            "three you can run, and one that reads the future",
            [("green", "hit"), ("red", "miss"), ("purple", "OPT, the bound"), ("amber", "Belady's anomaly")],
        )
        + _stage(_svg("rpPlot", "0 0 520 230", "A hit-and-miss grid for four replacement policies, and the miss count of each against cache size."))
        + _table("rpTable")
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="rpSteps"></table></div>\n'
        + _banner("rpStatus")
    )
    controls = (
        _select("rpPreset", "Reference string", _TRACES + [("custom", "&mdash; or type your own below &mdash;")], trace)
        + _text("rpTrace", "Trace (any separators)", trace)
        + _range("rpK1", "Cache size, first run", 1, 8, k1, 1)
        + _range("rpK2", "Cache size, second run", 1, 8, k2, 1)
        + _range("rpStep", "Step through the first run", 1, 40, step, 1)
        + _kpis(
            [
                ("OPT hits at the first size", "rpOpt"),
                ("LRU hits", "rpLru"),
                ("FIFO hits", "rpFifo"),
                ("Belady's anomaly", "rpAnomaly"),
            ]
        )
        + _hint(
            "rpHint",
            "Farthest-in-future is the bound, not a policy: it evicts the key used furthest ahead, "
            "which needs the rest of the trace. WHY no online policy beats it is proved in "
            "Algorithms, greedy-algorithms-and-matroids/optimal-caching; this page only measures it.",
        )
    )

    script = _CORE_JS + _preset({"trace": trace, "k1": k1, "k2": k2, "step": step}) + r"""
  var presetS = document.getElementById('rpPreset');
  var traceS = document.getElementById('rpTrace');
  var k1S = document.getElementById('rpK1');
  var k2S = document.getElementById('rpK2');
  var stepS = document.getElementById('rpStep');
  var plot = document.getElementById('rpPlot');
  var table = document.getElementById('rpTable');
  var steps = document.getElementById('rpSteps');
  var status = document.getElementById('rpStatus');

  var POLICIES = [['fifo', 'FIFO'], ['lru', 'LRU'], ['lfu', 'LFU'], ['opt', 'OPT']];

  function redraw() {
    var text = traceS.value || PRESET.trace;
    var trace = parseTrace(text);
    if (!trace.length) trace = parseTrace(PRESET.trace);
    var k1 = +k1S.value, k2 = +k2S.value;
    var at = Math.min(+stepS.value, trace.length);
    document.getElementById('rpK1Out').textContent = k1 + ' slot' + (k1 === 1 ? '' : 's');
    document.getElementById('rpK2Out').textContent = k2 + ' slot' + (k2 === 1 ? '' : 's');
    document.getElementById('rpStepOut').textContent = 'reference ' + at + ' of ' + trace.length;

    var keys = traceKeys(trace), kmax = Math.max(6, Math.min(10, keys.length + 1));
    var runs1 = {}, runs2 = {}, i, j;
    for (i = 0; i < POLICIES.length; i += 1) {
      runs1[POLICIES[i][0]] = replayTrace(trace, k1, POLICIES[i][0]);
      runs2[POLICIES[i][0]] = replayTrace(trace, k2, POLICIES[i][0]);
    }

    document.getElementById('rpOpt').textContent = runs1.opt.hits + ' / ' + trace.length
      + ' = ' + Rtext(runs1.opt.rate);
    document.getElementById('rpLru').textContent = runs1.lru.hits + ' / ' + trace.length
      + ' = ' + Rtext(runs1.lru.rate);
    document.getElementById('rpFifo').textContent = runs1.fifo.hits + ' / ' + trace.length
      + ' = ' + Rtext(runs1.fifo.rate);

    /* Scanned for every policy rather than claimed for one. "LRU never gets
       worse with more room" is a real theorem about stack algorithms, and a
       page that asserts it while measuring only FIFO is asking to be believed
       rather than checked. */
    var anomalies = {}, anomalyNames = [];
    for (i = 0; i < POLICIES.length; i += 1) {
      anomalies[POLICIES[i][0]] = firstAnomaly(trace, POLICIES[i][0], kmax);
      if (anomalies[POLICIES[i][0]]) anomalyNames.push(POLICIES[i][1]);
    }
    var anomaly = anomalies.fifo;
    var anomalyText = [];
    for (i = 0; i < POLICIES.length; i += 1) {
      var an = anomalies[POLICIES[i][0]];
      if (an) {
        anomalyText.push(POLICIES[i][1] + ' ' + an.from + ' &rarr; ' + an.to + ' misses, k = '
          + an.k + ' &rarr; ' + an.up);
      }
    }
    document.getElementById('rpAnomaly').textContent = anomalyText.length
      ? anomalyText.join('; ')
      : 'none, for any policy at any k up to ' + kmax;

    var rows = '';
    for (i = 0; i < POLICIES.length; i += 1) {
      var p = POLICIES[i][0], a = runs1[p], b = runs2[p];
      var worse = b.misses > a.misses;
      rows += '<tr><td' + (p === 'opt' ? ' class="tone-purple">' : '>') + POLICIES[i][1]
        + (p === 'opt' ? ' &mdash; offline' : '') + '</td><td>' + a.hits + '</td><td>' + Rtext(a.rate)
        + '</td><td>' + b.hits + '</td><td>' + Rtext(b.rate) + '</td><td'
        + (worse ? ' class="tone-amber">worse with more slots' : (b.hits > a.hits ? '>better' : '>unchanged'))
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>policy</th><th>hits at k = ' + k1 + '</th><th>rate</th>'
      + '<th>hits at k = ' + k2 + '</th><th>rate</th><th>k = ' + k1 + ' &rarr; ' + k2
      + '</th></tr></thead><tbody>' + rows + '</tbody>';

    /* The cache contents of all four policies at the chosen reference, so the
       reader can watch a policy make the eviction it is about to regret. */
    var srows = '';
    for (i = 0; i < POLICIES.length; i += 1) {
      var st = runs1[POLICIES[i][0]].steps[at - 1];
      srows += '<tr><td>' + POLICIES[i][1] + '</td><td class="tone-' + (st.hit ? 'green">hit' : 'red">miss')
        + '</td><td class="tt">' + (st.cache.length ? st.cache.join(' ') : '&mdash;') + '</td><td>'
        + (st.evicted === null ? '&mdash;' : st.evicted) + '</td></tr>';
    }
    steps.innerHTML = '<thead><tr><th>policy</th><th>reference ' + at + ' (&ldquo;'
      + trace[at - 1] + '&rdquo;) at k = ' + k1 + '</th><th>cache after</th><th>evicted</th>'
      + '</tr></thead><tbody>' + srows + '</tbody>';

    var x0 = 60, cell = Math.min(30, 440 / Math.max(trace.length, 1)), y0 = 30;
    var sSvg = '';
    for (j = 0; j < trace.length; j += 1) {
      sSvg += '<text x="' + (x0 + j * cell + cell / 2) + '" y="' + (y0 - 6) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">' + trace[j] + '</text>';
    }
    for (i = 0; i < POLICIES.length; i += 1) {
      var run = runs1[POLICIES[i][0]];
      sSvg += '<text x="' + (x0 - 8) + '" y="' + (y0 + i * 24 + 14) + '" text-anchor="end" font-size="10" fill="var(--'
        + (POLICIES[i][0] === 'opt' ? 'purple' : 'muted') + ')">' + POLICIES[i][1] + '</text>';
      for (j = 0; j < trace.length; j += 1) {
        var hit = run.steps[j].hit;
        sSvg += '<rect x="' + (x0 + j * cell) + '" y="' + (y0 + i * 24) + '" width="' + (cell - 2)
          + '" height="18" rx="2" fill="var(--' + (hit ? 'green' : 'red') + ')" opacity="'
          + (hit ? '0.85' : '0.55') + '" />';
      }
      sSvg += '<text x="' + (x0 + trace.length * cell + 6) + '" y="' + (y0 + i * 24 + 14)
        + '" font-size="10" fill="var(--text)">' + run.hits + '</text>';
    }
    sSvg += '<line x1="' + (x0 + (at - 1) * cell - 1) + '" y1="' + (y0 - 4) + '" x2="'
      + (x0 + (at - 1) * cell - 1) + '" y2="' + (y0 + 4 * 24) + '" stroke="var(--amber)" stroke-width="2" />';

    /* Misses against cache size for each policy: the picture in which FIFO's
       line goes back UP and the others never do. */
    var by = {}, maxMiss = 0;
    for (i = 0; i < POLICIES.length; i += 1) {
      by[POLICIES[i][0]] = missBySize(trace, POLICIES[i][0], kmax);
      for (j = 0; j < kmax; j += 1) if (by[POLICIES[i][0]][j] > maxMiss) maxMiss = by[POLICIES[i][0]][j];
    }
    var gx = 60, gw = 400, gt = 140, gb = 200, colours = ['cyan', 'green', 'amber', 'purple'];
    sSvg += '<line x1="' + gx + '" y1="' + gb + '" x2="' + (gx + gw) + '" y2="' + gb
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="' + (gx - 8) + '" y="' + (gt + 4) + '" text-anchor="end" font-size="9" fill="var(--muted)">'
      + maxMiss + '</text>'
      + '<text x="' + (gx - 8) + '" y="' + (gb + 4) + '" text-anchor="end" font-size="9" fill="var(--muted)">0</text>';
    for (i = 0; i < POLICIES.length; i += 1) {
      var path = '', vals = by[POLICIES[i][0]];
      for (j = 0; j < kmax; j += 1) {
        path += (j ? ' L ' : 'M ') + (gx + j * (gw / Math.max(kmax - 1, 1))) + ' '
          + (gb - (gb - gt) * (vals[j] / Math.max(maxMiss, 1)));
      }
      sSvg += '<path d="' + path + '" fill="none" stroke="var(--' + colours[i] + ')" stroke-width="2" opacity="0.9" />';
    }
    sSvg += '<text x="' + gx + '" y="' + (gb + 16) + '" font-size="10" fill="var(--muted)">misses against cache size, '
      + 'k = 1 to ' + kmax + (anomaly ? ' &mdash; FIFO rises at k = ' + anomaly.k : ' &mdash; every line falls here') + '</text>';
    plot.innerHTML = sSvg;

    var gap = Rsub(runs1.opt.rate, runs1.lru.rate);
    status.innerHTML = 'On ' + trace.length + ' references over ' + keys.length + ' distinct keys with '
      + k1 + ' slots, OPT gets <strong>' + Rtext(runs1.opt.rate) + '</strong>, LRU <strong>'
      + Rtext(runs1.lru.rate) + '</strong>, LFU <strong>' + Rtext(runs1.lfu.rate) + '</strong> and FIFO <strong>'
      + Rtext(runs1.fifo.rate) + '</strong>. OPT is ahead of LRU by ' + Rtext(gap)
      + ' and it is not a policy anyone can run: it evicts by looking at the rest of the trace. '
      + 'It is the BOUND &mdash; no online policy beats it, which Algorithms proves in '
      + '<span class="tt">greedy-algorithms-and-matroids/optimal-caching</span> by an exchange '
      + 'argument this course does not repeat. '
      + (anomaly
          ? 'What this course owns is the other direction, and it is measured here rather than '
            + 'promised: <strong>Belady\'s anomaly</strong>. FIFO misses ' + anomaly.from
            + ' times with ' + anomaly.k + ' slots and <strong>' + anomaly.to + '</strong> times with '
            + anomaly.up + ' &mdash; a bigger cache, MORE misses. FIFO is not a stack algorithm, so '
            + 'its miss count need not fall when you give it more room, and here it does not.'
          : '<strong>Belady\'s anomaly</strong> does not appear on this trace: no policy\'s miss '
            + 'count rises at any size from 1 to ' + kmax + '. That is not a guarantee for FIFO '
            + '&mdash; it is not a stack algorithm and has no such guarantee. Load Belady\'s trace '
            + 'from the selector and watch FIFO get worse when the cache grows.')
      + ' The scan above covers all four policies at every k from 1 to ' + kmax + ': '
      + (anomalyNames.length
          ? 'it finds a rise for ' + anomalyNames.join(' and ') + ' and for no other.'
          : 'it finds no rise for any of them on this trace.')
      + ' LRU and OPT are stack algorithms, so no trace can make their lines rise; FIFO and LFU '
      + 'have no such guarantee, and the selector has a trace that breaks FIFO.';
  }

  presetS.addEventListener('change', function () {
    if (presetS.value !== 'custom') { traceS.value = presetS.value; }
    redraw();
  });
  [traceS, k1S, k2S, stepS].forEach(function (el) { el.addEventListener('input', redraw); });
  traceS.value = PRESET.trace; k1S.value = PRESET.k1; k2S.value = PRESET.k2; stepS.value = PRESET.step;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Replacement policies on a trace",
        subtitle="FIFO, LRU, LFU and the offline bound, at two cache sizes",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Edit the reference string and the two cache sizes",
        panel_intro="Every hit is counted by replaying your trace through each policy in the "
        "browser. Run it at two sizes before you read the anomaly: seeing FIFO lose hits "
        "is more convincing than the sentence that says it does.",
    )


# ---------------------------------------------------------------------------
# L6 - ttl
# ---------------------------------------------------------------------------


def _ttl(cfg):
    update = int(cfg.get("update", 60))
    ttl = int(cfg.get("ttl", 10))
    lam_key = int(cfg.get("lam_key", 5))
    phase_pct = int(cfg.get("phase_pct", 25))

    markup = (
        _toolbar(
            "A TTL is a staleness budget",
            "T/(2U) below U, 1 &minus; U/(2T) above it &mdash; and a timeline that runs",
            [("cyan", "fresh"), ("red", "stale"), ("amber", "an update"), ("purple", "a refresh")],
        )
        + _stage(_svg("ttPlot", "0 0 520 200", "A timeline of refreshes and updates with the stale intervals shaded, above the stale fraction against TTL."))
        + _table("ttTable")
        + _banner("ttStatus")
    )
    controls = (
        _range("ttU", "Update interval U (seconds)", 1, 300, update, 1)
        + _range("ttT", "TTL T (seconds)", 1, 300, ttl, 1)
        + _range("ttLam", "Reads of this key per second", 1, 200, lam_key, 1)
        + _range("ttPhase", "Phase between the two clocks (% of U)", 0, 99, phase_pct, 1)
        + _kpis(
            [
                ("Stale fraction (formula)", "ttStale"),
                ("Stale fraction (this run)", "ttRun"),
                ("Averaged over phases", "ttAvg"),
                ("Miss rate 1/(&lambda;T)", "ttMiss"),
            ]
        )
        + _hint(
            "ttHint",
            "Treat the formula as a sensitivity, not a prediction. It assumes periodic updates and "
            "a uniform refresh phase; the timeline beside it is one concrete phase, and moving the "
            "phase control shows how far a single run can sit from the average.",
        )
    )

    script = _CORE_JS + _preset({"u": update, "t": ttl, "lam": lam_key, "phase": phase_pct}) + r"""
  var uS = document.getElementById('ttU');
  var tS = document.getElementById('ttT');
  var lamS = document.getElementById('ttLam');
  var phaseS = document.getElementById('ttPhase');
  var plot = document.getElementById('ttPlot');
  var table = document.getElementById('ttTable');
  var status = document.getElementById('ttStatus');

  function redraw() {
    var uV = +uS.value, tV = +tS.value, lamV = +lamS.value, ph = +phaseS.value;
    var U = R(BigInt(uV), 1n), T = R(BigInt(tV), 1n), lam = R(BigInt(lamV), 1n);
    var phase = Rmul(R(BigInt(ph), 100n), U);
    document.getElementById('ttUOut').textContent = uV + ' s';
    document.getElementById('ttTOut').textContent = tV + ' s';
    document.getElementById('ttLamOut').textContent = lamV + ' reads/s';
    document.getElementById('ttPhaseOut').textContent = ph + '% of U = ' + Rshow(phase, 2) + ' s';

    var formula = staleFraction(T, U);
    var horizon = 4 * uV;
    var windows = Math.max(1, Math.min(240, Math.ceil(horizon / tV)));
    var run = staleRun(T, U, phase, windows);
    var avg = staleAverage(T, U, 24, windows);
    var miss = ttlMissRate(lam, T);

    document.getElementById('ttStale').textContent = Rtext(formula) + ' = ' + Rpercent(formula, 2);
    document.getElementById('ttRun').textContent = Rtext(run.fraction) + ' = ' + Rpercent(run.fraction, 2);
    document.getElementById('ttAvg').textContent = Rpercent(avg, 2) + ' over 24 phases';
    document.getElementById('ttMiss').textContent = Rtext(miss) + ' = ' + Rpercent(miss, 2);

    var rows = '', marks = [1, Math.max(1, Math.round(uV / 4)), Math.max(1, Math.round(uV / 2)), uV,
                            2 * uV, 4 * uV], i;
    for (i = 0; i < marks.length; i += 1) {
      var Tm = R(BigInt(marks[i]), 1n), sf = staleFraction(Tm, U), mr = ttlMissRate(lam, Tm);
      var here = marks[i] === tV;
      rows += '<tr><td' + (here ? ' class="tone-purple">' : '>') + marks[i] + ' s' + (here ? ' &larr;' : '')
        + '</td><td>' + (Rcmp(Tm, U) <= 0 ? 'T/(2U)' : '1 &minus; U/(2T)') + '</td><td>' + Rtext(sf)
        + '</td><td>' + Rpercent(sf, 2) + '</td><td>' + Rpercent(mr, 2) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>TTL T</th><th>branch</th><th>stale fraction</th><th></th>'
      + '<th>miss rate 1/(&lambda;T)</th></tr></thead><tbody>' + rows + '</tbody>';

    /* The timeline. Refresh ticks below, update ticks above, and the stale
       stretches shaded between them -- the assumption made visible. */
    var x0 = 24, wid = 470, span = Rfloat(run.total), y = 62;
    function px(r) { return x0 + wid * (Rfloat(r) / (span || 1)); }
    var sSvg = '<line x1="' + x0 + '" y1="' + y + '" x2="' + (x0 + wid) + '" y2="' + y
      + '" stroke="var(--line-strong)" stroke-width="2" />'
      + '<text x="' + x0 + '" y="20" font-size="11" fill="var(--muted)">one run: updates every ' + uV
      + ' s, refreshes every ' + tV + ' s, over ' + Rshow(run.total, 0) + ' s</text>';
    for (i = 0; i < run.spans.length; i += 1) {
      var a = px(run.spans[i][0]), b = px(run.spans[i][1]);
      sSvg += '<rect x="' + a + '" y="' + (y - 10) + '" width="' + Math.max(1, b - a)
        + '" height="20" fill="var(--red)" opacity="0.55" />';
    }
    var jmax = Math.min(windows, 120), j;
    for (j = 0; j <= jmax; j += 1) {
      var xr = px(Rmul(R(BigInt(j), 1n), T));
      sSvg += '<line x1="' + xr + '" y1="' + (y + 10) + '" x2="' + xr + '" y2="' + (y + 22)
        + '" stroke="var(--purple)" stroke-width="1.5" />';
    }
    var upd = Radd(phase, R(0n, 1n)), guard = 0;
    while (Rcmp(upd, run.total) <= 0 && guard < 200) {
      var xu = px(upd);
      sSvg += '<line x1="' + xu + '" y1="' + (y - 22) + '" x2="' + xu + '" y2="' + (y - 10)
        + '" stroke="var(--amber)" stroke-width="2" />';
      upd = Radd(upd, U);
      guard += 1;
    }
    sSvg += '<text x="' + x0 + '" y="' + (y + 38) + '" font-size="10" fill="var(--purple)">refreshes</text>'
      + '<text x="' + (x0 + 80) + '" y="' + (y + 38) + '" font-size="10" fill="var(--amber)">updates</text>'
      + '<text x="' + (x0 + 150) + '" y="' + (y + 38) + '" font-size="10" fill="var(--red)">stale: '
      + Rshow(run.stale, 1) + ' s of ' + Rshow(run.total, 0) + ' s</text>';

    var gx = 40, gw = 440, gt = 116, gb = 176, kmax2 = Math.max(2 * uV, 4);
    var path = '';
    for (j = 1; j <= 60; j += 1) {
      var Tj = Rmul(R(BigInt(j), 60n), R(BigInt(kmax2), 1n));
      var v = Rfloat(staleFraction(Tj, U));
      path += (j > 1 ? ' L ' : 'M ') + (gx + gw * (j / 60)) + ' ' + (gb - (gb - gt) * v);
    }
    sSvg += '<path d="' + path + '" fill="none" stroke="var(--cyan)" stroke-width="2" />'
      + '<line x1="' + (gx + gw * (uV / kmax2)) + '" y1="' + gt + '" x2="' + (gx + gw * (uV / kmax2))
      + '" y2="' + gb + '" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="' + (gx + gw * (uV / kmax2) + 4) + '" y="' + (gt + 10) + '" font-size="9" fill="var(--amber)">T = U: '
      + 'both branches give 1/2</text>'
      + '<circle cx="' + (gx + gw * Math.min(1, tV / kmax2)) + '" cy="'
      + (gb - (gb - gt) * Rfloat(formula)) + '" r="4" fill="var(--purple)" />'
      + '<text x="' + gx + '" y="' + (gb + 16) + '" font-size="10" fill="var(--muted)">stale fraction against T, '
      + 'from 0 to ' + kmax2 + ' s &mdash; the kink at T = U is where the two branches meet</text>';
    plot.innerHTML = sSvg;

    var below = Rcmp(T, U) <= 0;
    status.innerHTML = 'With updates every ' + uV + ' s and a TTL of ' + tV + ' s the formula gives '
      + '<strong>' + Rtext(formula) + ' = ' + Rpercent(formula, 2) + '</strong> stale, by the '
      + (below ? 'T/(2U) branch (T &le; U)' : '1 &minus; U/(2T) branch (T &ge; U)')
      + '. The run drawn above, at a phase of ' + ph + '% of U, actually measured <strong>'
      + Rpercent(run.fraction, 2) + '</strong>, and averaging 24 phases gives <strong>'
      + Rpercent(avg, 2) + '</strong>. '
      + (Requ(run.fraction, formula)
          ? 'This phase happens to sit exactly on the average. '
          : 'A single run is one draw and the formula is the expectation over the phase, so they '
            + 'need not agree &mdash; move the phase control and watch how far one run can sit from '
            + 'the average. ')
      + (Requ(avg, formula)
          ? 'The 24-phase average lands exactly on the formula here, which is the model being '
            + 'confirmed rather than assumed: the phases are sampled at the midpoint of each slice '
            + 'and max(0, T &minus; G) is linear, so the sum is exact on every piece.'
          : 'The 24-phase average is ' + Rpercent(avg, 2) + ' against the formula\'s '
            + Rpercent(formula, 2) + ': with T not dividing U the horizon cuts an update period in '
            + 'half and the sampled phases do not tile it evenly. That residue is the model\'s '
            + 'assumption showing, which is what the timeline is here for.')
      + ' '
      + 'Shortening the TTL is not free: at ' + lamV + ' reads a second a ' + tV
      + ' s TTL misses <strong>' + Rpercent(miss, 2) + '</strong> of them, because the key expires '
      + 'once every ' + tV + ' s whether or not it changed. Halving T halves the staleness and '
      + 'doubles the misses.';
  }

  [uS, tS, lamS, phaseS].forEach(function (el) { el.addEventListener('input', redraw); });
  uS.value = PRESET.u; tS.value = PRESET.t; lamS.value = PRESET.lam; phaseS.value = PRESET.phase;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="TTL and staleness",
        subtitle="What a TTL costs in stale reads, and what a shorter one costs in misses",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the update interval, the TTL and the read rate",
        panel_intro="The formula and a concrete run are computed side by side. When they disagree, "
        "the run is right about that phase and the formula is right about the average.",
    )


# ---------------------------------------------------------------------------
# L7 - stampede
# ---------------------------------------------------------------------------


def _stampede(cfg):
    lam_key = int(cfg.get("lam_key", 500))
    miss_ms = int(cfg.get("miss_ms", 40))
    capacity = int(cfg.get("capacity", 200))
    keys = int(cfg.get("keys", 1))

    markup = (
        _toolbar(
            "The stampede at expiry",
            "&lambda;&middot;d requests through the miss window, or one with coalescing",
            [("red", "the burst"), ("green", "with coalescing"), ("amber", "backend capacity"), ("cyan", "steady state")],
        )
        + _stage(_svg("stPlot", "0 0 520 200", "The backend request rate over time, with the expiry burst drawn against the backend's capacity."))
        + _table("stTable")
        + _banner("stStatus")
    )
    controls = (
        _range("stLam", "Reads of the hot key per second", 10, 20000, lam_key, 10)
        + _range("stMiss", "Miss window d &mdash; time to fill (ms)", 1, 2000, miss_ms, 1)
        + _range("stCap", "Backend capacity (concurrent fills)", 1, 2000, capacity, 1)
        + _range("stKeys", "Hot keys expiring together", 1, 200, keys, 1)
        + _kpis(
            [
                ("Stampede size &lambda;&middot;d", "stSize"),
                ("Requests that reach the backend", "stCount"),
                ("With coalescing", "stCoal"),
                ("Against capacity", "stRatio"),
            ]
        )
        + _hint(
            "stHint",
            "The burst is a rate times a time, which is Little's Law and nothing more. A cache does "
            "not protect a backend during the miss window; single-flight coalescing does, by making "
            "the number in that window one per key instead of &lambda;&middot;d.",
        )
    )

    script = _CORE_JS + _preset({"lam": lam_key, "miss": miss_ms, "cap": capacity, "keys": keys}) + r"""
  var lamS = document.getElementById('stLam');
  var missS = document.getElementById('stMiss');
  var capS = document.getElementById('stCap');
  var keysS = document.getElementById('stKeys');
  var plot = document.getElementById('stPlot');
  var table = document.getElementById('stTable');
  var status = document.getElementById('stStatus');

  function redraw() {
    var lamV = +lamS.value, dV = +missS.value, capV = +capS.value, kV = +keysS.value;
    var lam = R(BigInt(lamV), 1n), d = R(BigInt(dV), 1n), cap = R(BigInt(capV), 1n);
    document.getElementById('stLamOut').textContent = groupNum(lamV) + ' reads/s';
    document.getElementById('stMissOut').textContent = dV + ' ms';
    document.getElementById('stCapOut').textContent = groupNum(capV) + ' concurrent';
    document.getElementById('stKeysOut').textContent = kV + ' key' + (kV === 1 ? '' : 's');

    var size = stampedeSize(lam, d);
    var count = stampedeCount(lam, d);
    var total = stampedeTotal(lam, d, kV);
    var coalesced = R(BigInt(kV), 1n);
    var ratio = Rdiv(total, cap);

    document.getElementById('stSize').textContent = Rtext(size) + ' per key';
    document.getElementById('stCount').textContent = groupNum(Rshow(total, 1)) + ' in flight';
    document.getElementById('stCoal').textContent = Rtext(coalesced) + ' &mdash; one per key';
    document.getElementById('stRatio').textContent = Rtext(ratio) + ' = ' + Rshow(ratio, 2) + '&times;';

    var rows = '', marks = [1, 10, 50, 100, 500, 2000], i;
    for (i = 0; i < marks.length; i += 1) {
      var dm = R(BigInt(marks[i]), 1n), sm = stampedeSize(lam, dm);
      var here = marks[i] === dV;
      rows += '<tr><td' + (here ? ' class="tone-red">' : '>') + marks[i] + ' ms' + (here ? ' &larr;' : '')
        + '</td><td>' + Rtext(sm) + '</td><td>' + Rceil(sm) + '</td><td>'
        + Rtext(Rmul(sm, R(BigInt(kV), 1n))) + '</td><td>' + kV + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>miss window d</th><th>&lambda;&middot;d</th><th>requests, rounded up</th>'
      + '<th>&times; ' + kV + ' hot keys</th><th>with coalescing</th></tr></thead><tbody>' + rows + '</tbody>';

    /* Backend rate over time: flat at zero while the key is cached, then a
       rectangle of height lambda*keys for d milliseconds. The capacity line
       is the same one course 3 drew. */
    var x0 = 40, wid = 450, base = 150, top = 34;
    var peak = Rfloat(Rmul(lam, R(BigInt(kV), 1n)));
    var scale = Math.max(peak, Rfloat(cap)) || 1;
    var burstW = Math.max(3, wid * Math.min(0.4, dV / 2000));
    var bx = x0 + wid * 0.4;
    var ph = (base - top) * (peak / scale);
    var ch = (base - top) * (Rfloat(cap) / scale);
    var sSvg = '<line x1="' + x0 + '" y1="' + base + '" x2="' + (x0 + wid) + '" y2="' + base
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + base + '" x2="' + bx + '" y2="' + base
      + '" stroke="var(--cyan)" stroke-width="3" />'
      + '<rect x="' + bx + '" y="' + (base - ph) + '" width="' + burstW + '" height="' + ph
      + '" fill="var(--red)" opacity="0.75" />'
      + '<line x1="' + (bx + burstW) + '" y1="' + base + '" x2="' + (x0 + wid) + '" y2="' + base
      + '" stroke="var(--cyan)" stroke-width="3" />'
      + '<line x1="' + x0 + '" y1="' + (base - ch) + '" x2="' + (x0 + wid) + '" y2="' + (base - ch)
      + '" stroke="var(--amber)" stroke-width="1.5" stroke-dasharray="4 3" />'
      + '<text x="' + (x0 + wid) + '" y="' + (base - ch - 5) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--amber)">capacity ' + groupNum(capV) + '</text>'
      + '<rect x="' + bx + '" y="' + (base - Math.max(3, (base - top) * (kV / scale))) + '" width="'
      + burstW + '" height="' + Math.max(3, (base - top) * (kV / scale))
      + '" fill="var(--green)" opacity="0.95" />'
      + '<text x="' + (bx + burstW + 6) + '" y="' + (base - ph + 12) + '" font-size="10" fill="var(--red)">'
      + groupNum(Rshow(total, 0)) + ' through</text>'
      + '<text x="' + (bx + burstW + 6) + '" y="' + (base - 4) + '" font-size="10" fill="var(--green)">'
      + kV + ' with coalescing</text>'
      + '<text x="' + x0 + '" y="24" font-size="11" fill="var(--muted)">backend request rate, with the key '
      + 'expiring at the red bar (' + dV + ' ms wide)</text>'
      + '<text x="' + x0 + '" y="' + (base + 18) + '" font-size="10" fill="var(--cyan)">cached: the backend sees nothing</text>'
      + '<text x="' + x0 + '" y="' + (base + 38) + '" font-size="10" fill="var(--muted)">the burst is '
      + '&lambda; &times; d = ' + groupNum(lamV) + ' &times; ' + dV + '/1000 = ' + Rtext(size)
      + ' per key, by Little\'s Law</text>';
    plot.innerHTML = sSvg;

    var over = Rcmp(total, cap) > 0;
    status.innerHTML = 'A key read ' + groupNum(lamV) + ' times a second, with a ' + dV
      + ' ms fill, lets <strong>' + Rtext(size) + '</strong> requests into the miss window &mdash; '
      + count + ' whole requests' + (kV > 1 ? ', and <strong>' + Rshow(total, 1) + '</strong> across the '
      + kV + ' keys expiring together' : '') + '. The backend can take ' + groupNum(capV)
      + ' at once, so the burst is <strong>' + Rshow(ratio, 2) + '&times;</strong> its capacity'
      + (over
          ? ' &mdash; it does not absorb this. The cache did not protect it: for d milliseconds there '
            + 'was no cache at all, which is the misconception this lesson names.'
          : ' &mdash; it absorbs this one, but the burst scales with &lambda; and with d, and neither '
            + 'is under your control at the moment a popular key expires.')
      + ' With single-flight coalescing exactly <strong>' + kV + '</strong> request'
      + (kV === 1 ? '' : 's') + ' reaches the backend and the rest wait on it: '
      + Rtext(size) + ' becomes 1 per key, a factor of ' + Rtext(size) + '.';
  }

  [lamS, missS, capS, keysS].forEach(function (el) { el.addEventListener('input', redraw); });
  lamS.value = PRESET.lam; missS.value = PRESET.miss; capS.value = PRESET.cap; keysS.value = PRESET.keys;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Cache stampedes",
        subtitle="What arrives at the backend in the window after a hot key expires",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the key's rate and the miss window",
        panel_intro="The burst is &lambda;&middot;d, computed from the rate and the window you set, "
        "and drawn against the backend capacity course 3 sized.",
    )


# ---------------------------------------------------------------------------
# L8 - write
# ---------------------------------------------------------------------------

_WRITE_TRACES = [
    ("A B A C A B A D A B", "a hot key &mdash; A B A C A B A D A B"),
    ("A B C D E F G H I J", "all distinct &mdash; A B C D E F G H I J"),
    ("A A A A A A A A A A", "one key &mdash; A A A A A A A A A A"),
    ("A B A B C A B A B C", "two hot, one cold &mdash; A B A B C A B A B C"),
]


def _write(cfg):
    trace = str(cfg.get("trace", "A B A C A B A D A B"))
    window = int(cfg.get("window", 5))
    rate = int(cfg.get("rate", 1000))
    obj_kb = int(cfg.get("obj_kb", 4))

    markup = (
        _toolbar(
            "Write-through against write-back",
            "every write, or the distinct keys per flush &mdash; and what that risks",
            [("cyan", "a write"), ("purple", "a repeat, coalesced away"), ("amber", "a flush"), ("red", "bytes at risk")],
        )
        + _stage(_svg("wrPlot", "0 0 520 200", "The write trace drawn as a row of writes with flush boundaries, repeats marked as coalesced."))
        + _table("wrTable")
        + _banner("wrStatus")
    )
    controls = (
        _select("wrPreset", "Write trace", _WRITE_TRACES + [("custom", "&mdash; or type your own below &mdash;")], trace)
        + _text("wrTrace", "Trace (any separators)", trace)
        + _range("wrWindow", "Flush interval (writes per flush)", 1, 20, window, 1)
        + _range("wrRate", "Write rate (writes per second)", 10, 20000, rate, 10)
        + _range("wrObj", "Object size (kB)", 1, 256, obj_kb, 1)
        + _kpis(
            [
                ("Write-through backend writes", "wrThrough"),
                ("Write-back backend writes", "wrBack"),
                ("Coalescing ratio", "wrRatio"),
                ("Bytes at risk", "wrRisk"),
            ]
        )
        + _hint(
            "wrHint",
            "Write-back is not free. What it buys is the coalescing ratio; what it costs is a loss "
            "window &mdash; the flush interval times the write rate, in whichever keys are dirty when "
            "the process dies.",
        )
    )

    script = _CORE_JS + _preset({"trace": trace, "window": window, "rate": rate, "obj": obj_kb}) + r"""
  var presetS = document.getElementById('wrPreset');
  var traceS = document.getElementById('wrTrace');
  var winS = document.getElementById('wrWindow');
  var rateS = document.getElementById('wrRate');
  var objS = document.getElementById('wrObj');
  var plot = document.getElementById('wrPlot');
  var table = document.getElementById('wrTable');
  var status = document.getElementById('wrStatus');

  function redraw() {
    var trace = parseTrace(traceS.value || PRESET.trace);
    if (!trace.length) trace = parseTrace(PRESET.trace);
    var w = +winS.value, rate = +rateS.value, objKb = +objS.value;
    document.getElementById('wrWindowOut').textContent = w + ' write' + (w === 1 ? '' : 's') + ' per flush';
    document.getElementById('wrRateOut').textContent = groupNum(rate) + ' writes/s';
    document.getElementById('wrObjOut').textContent = objKb + ' kB';

    var co = coalescing(trace, w);
    var lam = R(BigInt(rate), 1n);
    var flushSecs = Rdiv(R(BigInt(w), 1n), lam);
    var backRate = co.writes ? Rmul(lam, R(BigInt(co.distinct), BigInt(co.writes))) : R(0n, 1n);
    var risk = bytesAtRisk(co.peak, objKb * 1000);

    document.getElementById('wrThrough').textContent = co.writes + ' on this trace, '
      + groupNum(rate) + ' rps';
    document.getElementById('wrBack').textContent = co.distinct + ' on this trace, '
      + Rshow(backRate, 1) + ' rps';
    document.getElementById('wrRatio').textContent = Rtext(co.ratio) + ' = ' + Rshow(co.ratio, 3) + '&times;';
    document.getElementById('wrRisk').textContent = bytesText(risk.n / risk.d) + ' over '
      + Rshow(Rmul(flushSecs, R(1000n, 1n)), 1) + ' ms';

    var rows = '', i;
    for (i = 0; i < co.windows.length; i += 1) {
      var win = co.windows[i];
      rows += '<tr><td>' + (i + 1) + '</td><td class="tt">'
        + trace.slice(win.start, win.start + win.writes).join(' ') + '</td><td>' + win.writes
        + '</td><td class="tone-purple">' + win.distinct + '</td><td>' + (win.writes - win.distinct)
        + '</td><td>' + bytesText(win.distinct * objKb * 1000) + '</td></tr>';
    }
    rows += '<tr><td><strong>all</strong></td><td class="tt">' + trace.length + ' writes</td><td>'
      + co.writes + '</td><td class="tone-purple">' + co.distinct + '</td><td>'
      + (co.writes - co.distinct) + '</td><td>peak ' + bytesText(risk.n / risk.d) + '</td></tr>';
    table.innerHTML = '<thead><tr><th>flush</th><th>writes in the window</th><th>writes</th>'
      + '<th>distinct keys</th><th>coalesced away</th><th>dirty bytes</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var x0 = 24, cell = Math.min(34, 470 / Math.max(trace.length, 1)), y = 50, i2, seen;
    var sSvg = '<text x="' + x0 + '" y="24" font-size="11" fill="var(--muted)">the trace, with a flush every '
      + w + ' write' + (w === 1 ? '' : 's') + '</text>';
    for (i = 0; i < trace.length; i += 1) {
      var windowStart = Math.floor(i / w) * w;
      seen = false;
      for (i2 = windowStart; i2 < i; i2 += 1) if (trace[i2] === trace[i]) seen = true;
      sSvg += '<rect x="' + (x0 + i * cell) + '" y="' + y + '" width="' + (cell - 3) + '" height="26" rx="3" '
        + 'fill="var(--' + (seen ? 'purple' : 'cyan') + ')" opacity="' + (seen ? '0.45' : '0.9') + '" />'
        + '<text x="' + (x0 + i * cell + (cell - 3) / 2) + '" y="' + (y + 18)
        + '" text-anchor="middle" font-size="10" fill="var(--on-accent)">' + trace[i] + '</text>';
      if ((i + 1) % w === 0 && i + 1 < trace.length) {
        sSvg += '<line x1="' + (x0 + (i + 1) * cell - 2) + '" y1="' + (y - 8) + '" x2="'
          + (x0 + (i + 1) * cell - 2) + '" y2="' + (y + 42) + '" stroke="var(--amber)" stroke-width="2" />';
      }
    }
    sSvg += '<text x="' + x0 + '" y="' + (y + 58) + '" font-size="10" fill="var(--cyan)">solid: a key this '
      + 'window has not seen &mdash; it must go to the backend</text>'
      + '<text x="' + x0 + '" y="' + (y + 74) + '" font-size="10" fill="var(--purple)">faded: a repeat inside '
      + 'the same window &mdash; write-back never sends it</text>';
    var bx = x0, bw = 460, by = 158;
    var frac = co.writes ? co.distinct / co.writes : 0;
    sSvg += '<rect x="' + bx + '" y="' + by + '" width="' + bw + '" height="18" rx="3" fill="var(--cyan)" opacity="0.35" />'
      + '<rect x="' + bx + '" y="' + by + '" width="' + (bw * frac) + '" height="18" rx="3" fill="var(--purple)" opacity="0.9" />'
      + '<text x="' + (bx + 6) + '" y="' + (by + 13) + '" font-size="10" fill="var(--on-accent)">write-back sends '
      + co.distinct + ' of ' + co.writes + '</text>'
      + '<text x="' + bx + '" y="' + (by + 34) + '" font-size="10" fill="var(--red)">bytes at risk: the largest dirty set, '
      + co.peak + ' key' + (co.peak === 1 ? '' : 's') + ' &times; ' + objKb + ' kB = ' + bytesText(risk.n / risk.d) + '</text>';
    plot.innerHTML = sSvg;

    status.innerHTML = 'Over ' + co.writes + ' writes flushed every ' + w
      + ', write-through sends all <strong>' + co.writes + '</strong> to the backend and write-back sends '
      + 'the <strong>' + co.distinct + '</strong> distinct keys &mdash; a coalescing ratio of <strong>'
      + Rtext(co.ratio) + '</strong>, so at ' + groupNum(rate) + ' writes a second the backend sees '
      + Rshow(backRate, 1) + ' rps instead of ' + groupNum(rate) + '. '
      + 'That ratio is bought, not given: the flush interval is ' + Rshow(Rmul(flushSecs, R(1000n, 1n)), 1)
      + ' ms of writes held in memory, and the largest dirty set on this trace is ' + co.peak
      + ' key' + (co.peak === 1 ? '' : 's') + ', so <strong>' + bytesText(risk.n / risk.d)
      + '</strong> is lost if the process dies at the wrong moment. '
      + (co.distinct === co.writes
          ? 'On this trace nothing coalesces &mdash; every write is to a different key inside its '
            + 'window &mdash; so write-back buys nothing at all and still carries the loss window.'
          : 'Widen the flush interval and the ratio improves while the bytes at risk grow; that is '
            + 'the whole trade, and both ends of it are on this page.');
  }

  presetS.addEventListener('change', function () {
    if (presetS.value !== 'custom') { traceS.value = presetS.value; }
    redraw();
  });
  [traceS, winS, rateS, objS].forEach(function (el) { el.addEventListener('input', redraw); });
  traceS.value = PRESET.trace; winS.value = PRESET.window; rateS.value = PRESET.rate; objS.value = PRESET.obj;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Write policies",
        subtitle="The coalescing ratio, and the loss window it is bought with",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Edit the write trace and the flush interval",
        panel_intro="Distinct keys per flush are counted off your own trace, and the bytes at risk "
        "are the largest dirty set it ever holds &mdash; not an average.",
    )


# ---------------------------------------------------------------------------
# L9 - levels
# ---------------------------------------------------------------------------


def _levels(cfg):
    h1_tenths = int(cfg.get("h1_tenths", 800))
    h2_tenths = int(cfg.get("h2_tenths", 500))
    t1 = int(cfg.get("t1", 1))
    t2 = int(cfg.get("t2", 5))
    t3 = int(cfg.get("t3", 50))

    markup = (
        _toolbar(
            "Two levels, and a conditional rate",
            "h&#8322; is measured on the requests that MISSED, so the misses multiply",
            [("cyan", "L1 hits"), ("purple", "L2 hits, given an L1 miss"), ("red", "to the origin"), ("amber", "the wrong answer")],
        )
        + _stage(_svg("lvPlot", "0 0 520 220", "The request flow through two cache levels to the origin, with the conditional rate on each branch."))
        + _table("lvTable")
        + _banner("lvStatus")
    )
    controls = (
        _range("lvH1", "L1 hit rate h&#8322;&#8321; (tenths of a per cent)", 0, 999, h1_tenths, 1)
        + _range("lvH2", "L2 hit rate given an L1 miss (tenths of a per cent)", 0, 999, h2_tenths, 1)
        + _range("lvT1", "t&#8321; &mdash; L1 lookup (ms)", 1, 20, t1, 1)
        + _range("lvT2", "t&#8322; &mdash; L2 lookup (ms)", 1, 60, t2, 1)
        + _range("lvT3", "t&#8323; &mdash; the origin (ms)", 5, 500, t3, 1)
        + _kpis(
            [
                ("Global hit rate", "lvHit"),
                ("Global miss (1&minus;h&#8321;)(1&minus;h&#8322;)", "lvMiss"),
                ("Mean latency", "lvMean"),
                ("Requests that reach the origin", "lvOrigin"),
            ]
        )
        + _hint(
            "lvHint",
            "E[X | B] is the expectation computed over the outcomes in which B happened, with their "
            "probabilities renormalised. Everything on this page is a finite enumeration of four "
            "outcomes, so nothing beyond that one line is needed.",
        )
    )

    script = _CORE_JS + _preset({"h1": h1_tenths, "h2": h2_tenths, "t1": t1, "t2": t2, "t3": t3}) + r"""
  var h1S = document.getElementById('lvH1');
  var h2S = document.getElementById('lvH2');
  var t1S = document.getElementById('lvT1');
  var t2S = document.getElementById('lvT2');
  var t3S = document.getElementById('lvT3');
  var plot = document.getElementById('lvPlot');
  var table = document.getElementById('lvTable');
  var status = document.getElementById('lvStatus');

  function redraw() {
    var a = +h1S.value, b = +h2S.value, t1v = +t1S.value, t2v = +t2S.value, t3v = +t3S.value;
    var h1 = R(BigInt(a), 1000n), h2 = R(BigInt(b), 1000n);
    var t1 = R(BigInt(t1v), 1n), t2 = R(BigInt(t2v), 1n), t3 = R(BigInt(t3v), 1n);
    document.getElementById('lvH1Out').textContent = Rpercent(h1, 1);
    document.getElementById('lvH2Out').textContent = Rpercent(h2, 1) + ' of the L1 misses';
    document.getElementById('lvT1Out').textContent = t1v + ' ms';
    document.getElementById('lvT2Out').textContent = t2v + ' ms';
    document.getElementById('lvT3Out').textContent = t3v + ' ms';

    var gHit = globalHit(h1, h2), gMiss = globalMiss(h1, h2);
    var mean = levelLatency(h1, h2, t1, t2, t3);
    var l2Share = conditionalShare(h1, h2);
    var naive = naiveSumHit(h1, h2);

    document.getElementById('lvHit').textContent = Rtext(gHit) + ' = ' + Rpercent(gHit, 2);
    document.getElementById('lvMiss').textContent = Rtext(gMiss) + ' = ' + Rpercent(gMiss, 2);
    document.getElementById('lvMean').textContent = Rtext(mean) + ' ms';
    document.getElementById('lvOrigin').textContent = Rpercent(gMiss, 2) + ' of all requests';

    /* The four outcomes, enumerated. A conditional expectation over a finite
       enumeration needs no machinery beyond the renormalised weights. */
    var rows = ''
      + '<tr><td class="tone-cyan">L1 hit</td><td>h&#8321;</td><td>' + Rtext(h1) + '</td><td>'
      + Rtext(t1) + ' ms</td><td>' + Rtext(Rmul(h1, t1)) + '</td></tr>'
      + '<tr><td class="tone-purple">L1 miss, L2 hit</td><td>(1&minus;h&#8321;)h&#8322;</td><td>'
      + Rtext(l2Share) + '</td><td>' + Rtext(Radd(t1, t2)) + ' ms</td><td>'
      + Rtext(Rmul(l2Share, Radd(t1, t2))) + '</td></tr>'
      + '<tr><td class="tone-red">both miss</td><td>(1&minus;h&#8321;)(1&minus;h&#8322;)</td><td>'
      + Rtext(gMiss) + '</td><td>' + Rtext(Radd(Radd(t1, t2), t3)) + ' ms</td><td>'
      + Rtext(Rmul(gMiss, Radd(Radd(t1, t2), t3))) + '</td></tr>'
      + '<tr><td><strong>all</strong></td><td>1</td><td>'
      + Rtext(Radd(Radd(h1, l2Share), gMiss)) + '</td><td>&mdash;</td><td><strong>'
      + Rtext(mean) + ' ms</strong></td></tr>';
    table.innerHTML = '<thead><tr><th>outcome</th><th>probability</th><th>value</th>'
      + '<th>latency</th><th>contribution</th></tr></thead><tbody>' + rows + '</tbody>';

    var y = 40, x0 = 30;
    var w1 = 440 * Rfloat(h1), w2 = 440 * Rfloat(l2Share), w3 = 440 * Rfloat(gMiss);
    var sSvg = '<text x="' + x0 + '" y="22" font-size="11" fill="var(--muted)">every request enters at the left; '
      + 'each branch is the share of ALL requests that takes it</text>'
      + '<rect x="' + x0 + '" y="' + y + '" width="440" height="22" rx="3" fill="var(--line)" opacity="0.6" />'
      + '<text x="' + (x0 + 4) + '" y="' + (y + 16) + '" font-size="10" fill="var(--text)">100% arrive, each paying t&#8321; = '
      + t1v + ' ms</text>'
      + '<rect x="' + x0 + '" y="' + (y + 40) + '" width="' + Math.max(2, w1) + '" height="24" rx="3" '
      + 'fill="var(--cyan)" opacity="0.9" />'
      + '<text x="' + (x0 + 4) + '" y="' + (y + 57) + '" font-size="10" fill="var(--on-accent)">L1 hit '
      + Rpercent(h1, 1) + '</text>'
      + '<rect x="' + (x0 + Math.max(2, w1)) + '" y="' + (y + 40) + '" width="' + Math.max(2, w2 + w3)
      + '" height="24" rx="3" fill="var(--line)" opacity="0.7" />'
      + '<text x="' + (x0 + Math.max(2, w1) + 4) + '" y="' + (y + 57) + '" font-size="10" fill="var(--text)">'
      + 'L1 miss ' + Rpercent(Rsub(R(1n, 1n), h1), 1) + ' &rarr; L2, paying t&#8322;</text>'
      + '<rect x="' + (x0 + Math.max(2, w1)) + '" y="' + (y + 80) + '" width="' + Math.max(2, w2)
      + '" height="24" rx="3" fill="var(--purple)" opacity="0.9" />'
      + '<text x="' + (x0 + Math.max(2, w1) + 4) + '" y="' + (y + 97) + '" font-size="10" fill="var(--on-accent)">'
      + 'L2 hit: ' + Rpercent(h2, 1) + ' OF THOSE = ' + Rpercent(l2Share, 2) + ' of all</text>'
      + '<rect x="' + (x0 + Math.max(2, w1) + Math.max(2, w2)) + '" y="' + (y + 80) + '" width="'
      + Math.max(2, w3) + '" height="24" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<text x="' + x0 + '" y="' + (y + 138) + '" font-size="10" fill="var(--red)">to the origin: '
      + '(1 &minus; h&#8321;)(1 &minus; h&#8322;) = ' + Rtext(gMiss) + ' = ' + Rpercent(gMiss, 2)
      + ' of all requests, paying t&#8323; = ' + t3v + ' ms on top</text>'
      + '<text x="' + x0 + '" y="' + (y + 158) + '" font-size="10" fill="var(--amber)">adding the rates would say '
      + Rpercent(naive, 1) + (Rcmp(naive, R(1n, 1n)) > 0 ? ' &mdash; over 100%, which is how you know it is wrong' : '')
      + '; reading h&#8322; as a global rate would say ' + Rpercent(h2, 1) + '</text>';
    plot.innerHTML = sSvg;

    status.innerHTML = 'With h&#8321; = ' + Rpercent(h1, 1) + ' and h&#8322; = ' + Rpercent(h2, 1)
      + ' <em>of the L1 misses</em>, the global hit rate is <strong>' + Rtext(gHit) + ' = '
      + Rpercent(gHit, 2) + '</strong> and the global MISS rate is the product <strong>'
      + Rtext(gMiss) + '</strong>. The mean latency is t&#8321; + (1&minus;h&#8321;)(t&#8322; + '
      + '(1&minus;h&#8322;)t&#8323;) = <strong>' + Rtext(mean) + ' ms</strong>, and every request '
      + 'pays t&#8321; whether or not it hits. '
      + 'The two wrong answers are on the drawing: adding the hit rates gives ' + Rpercent(naive, 1)
      + ', and taking L2\'s measured rate as a global one gives ' + Rpercent(h2, 1)
      + ' &mdash; but h&#8322; is conditional, measured only on the ' + Rpercent(Rsub(R(1n, 1n), h1), 1)
      + ' that reached L2, and it accounts for ' + Rpercent(l2Share, 2) + ' of all requests.';
  }

  [h1S, h2S, t1S, t2S, t3S].forEach(function (el) { el.addEventListener('input', redraw); });
  h1S.value = PRESET.h1; h2S.value = PRESET.h2;
  t1S.value = PRESET.t1; t2S.value = PRESET.t2; t3S.value = PRESET.t3;
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Multi-level caches",
        subtitle="The second level's hit rate is conditional, so the misses multiply",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the two hit rates and the three latencies",
        panel_intro="h&#8322; is entered as what it is measured as: the fraction of the L1 MISSES "
        "that L2 serves. The four outcomes are enumerated beneath the drawing.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_VIEWS = {
    "load": _hitrate_load,
    "latency": _hitrate_latency,
    "bytes": _hitrate_bytes,
}

VIEWS = tuple(sorted(_VIEWS))


def _hitrate(cfg):
    """Mode `hitrate` carries three lessons, so it takes a second key.

    L1, L2 and L10 are all "what a hit rate is worth", in backend load, in
    latency and in bytes. They share a mode name because they share an idea,
    and they must not share a widget: an absent or unknown view raises for
    exactly the reason an unknown mode does.
    """
    view = cfg.get("view")
    if view not in _VIEWS:
        raise ValueError(
            "cache_lab: mode 'hitrate' needs a view; %r is not one of %s"
            % (view, ", ".join(VIEWS))
        )
    return _VIEWS[view](cfg)


_MODES = {
    "hitrate": _hitrate,
    "zipf": _zipf,
    "size": _size,
    "replace": _replace,
    "ttl": _ttl,
    "stampede": _stampede,
    "write": _write,
    "levels": _levels,
}

MODES = tuple(sorted(_MODES))


def cache_lab(cfg):
    """Course 4's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, not defensiveness. A kit that quietly fell back
    to a default would render a finished-looking page carrying another lesson's
    widget: the markup assertions pass, labcheck passes, and the reader is shown
    the wrong lesson's arithmetic under the right lesson's title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "cache_lab: unknown mode %r; the eight modes of course 4 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["cache_lab", "CACHE_JS", "MODES", "VIEWS", "EXACT_LIMIT"]
