"""The exact engine the System Design labs share.

Every figure on a System Design page is a capacity, a latency, a probability or
a cost, and all four are ratios of integers whenever the inputs are. So the
arithmetic here is `RATIONAL_JS` from algebra_core -- BigInt numerator over
BigInt denominator -- and a page prints `2/3`, not `0.6666666666666666`.

That is not fussiness. The subject's whole claim is that a reader can check the
number, and a reader checking `1 - (1 - 1/m)^(k*n)` against a printed
`0.010000000000000002` cannot tell a right answer from a wrong one.

Four quantities here genuinely are irrational and the lessons that use them say
so: a standard error, `e^-x`, a square root, and the Zipf normaliser past the
point where its exact form is unreadable. Each has a function whose name ends
`Approx`, each states its method, and no other function in this module rounds.

The blocks are raw strings so `scripts/mathcheck.js` can execute the SHIPPED
source rather than a transcription of it -- see that file's header. Anything
mathcheck needs to call is a top-level function, for the reason logic.py gives:
a helper closed over a lab's DOM cannot be tested in isolation, and the parts
that go untested are the parts that turn out to be wrong.
"""

HARMONIC_JS = r"""
  /* Generalised harmonic H(n,s) = sum_{k=1..n} 1/k^s, exact for integer s.

     The Zipf popularity model needs it twice: as the normaliser of the whole
     key space and as the partial sum over the cached prefix, and a cache hit
     rate is their ratio. Kept exact because the ratio of two large harmonics
     loses its leading digits in floating point exactly when the tail matters,
     which is the case a caching lesson is about. */
  function harmonic(n, s) {
    var total = R(0n, 1n);
    for (var k = 1; k <= n; k += 1) {
      var kb = BigInt(k), den = 1n;
      for (var j = 0; j < s; j += 1) den *= kb;
      total = Radd(total, R(1n, den));
    }
    return total;
  }

  /* The Zipf hit rate: the c most popular of n keys, exponent s.
     H(c,s)/H(n,s) -- exact, and the reason a small cache of a skewed
     workload holds most of the traffic. */
  function zipfHit(c, n, s) {
    if (c <= 0) return R(0n, 1n);
    if (c >= n) return R(1n, 1n);
    return Rdiv(harmonic(c, s), harmonic(n, s));
  }
"""

PERCENTILE_JS = r"""
  /* Nearest-rank percentile: the smallest value at or above q of the sample.

     Nearest rank rather than an interpolating definition because it returns a
     value that was actually observed. A p99 of 412ms that no request took is a
     worse answer for this subject than one that a request did. */
  function percentileRank(n, q) {
    /* q is a rational in [0,1]; the rank is ceil(q*n), at least 1. */
    var prod = Rmul(q, R(BigInt(n), 1n));
    /* A rational is {n, d}; Rnum() is its DECIMAL value, not its numerator. */
    var r = prod.n, d = prod.d;
    var rank = r / d + (r % d === 0n ? 0n : 1n);
    if (rank < 1n) rank = 1n;
    if (rank > BigInt(n)) rank = BigInt(n);
    return Number(rank);
  }
  function percentile(sorted, q) {
    if (!sorted.length) return null;
    return sorted[percentileRank(sorted.length, q) - 1];
  }

  /* P(X <= t) for a sample: a rational, count over total. */
  function empiricalCdf(sorted, t) {
    var c = 0;
    for (var i = 0; i < sorted.length; i += 1) if (sorted[i] <= t) c += 1;
    return R(BigInt(c), BigInt(sorted.length));
  }
"""

PMF_JS = r"""
  /* Discrete distributions as [value, probability] pairs with rational
     probabilities. Convolution is the sum of two independent draws, which is
     how a latency budget adds a serial chain and how periodic review covers
     R+L periods of demand. Exact, so a 12-step convolution is still a fraction. */
  function pmfNormalise(pairs) {
    var total = R(0n, 1n), i;
    for (i = 0; i < pairs.length; i += 1) total = Radd(total, pairs[i][1]);
    if (Rzero(total)) return pairs.slice();
    var out = [];
    for (i = 0; i < pairs.length; i += 1) out.push([pairs[i][0], Rdiv(pairs[i][1], total)]);
    return out;
  }
  function pmfConvolve(a, b) {
    var acc = {}, i, j;
    for (i = 0; i < a.length; i += 1) {
      for (j = 0; j < b.length; j += 1) {
        var v = a[i][0] + b[j][0], p = Rmul(a[i][1], b[j][1]);
        acc[v] = acc[v] ? Radd(acc[v], p) : p;
      }
    }
    var keys = Object.keys(acc).map(Number).sort(function (x, y) { return x - y; });
    return keys.map(function (v) { return [v, acc[v]]; });
  }
  function pmfMean(pairs) {
    var m = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) {
      m = Radd(m, Rmul(R(BigInt(pairs[i][0]), 1n), pairs[i][1]));
    }
    return m;
  }
  /* P(X > t): the tail a stale-read or a timeout lesson asks for. */
  function pmfTail(pairs, t) {
    var s = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) if (pairs[i][0] > t) s = Radd(s, pairs[i][1]);
    return s;
  }
  /* The pmf of the maximum of k independent copies -- the fan-out lesson's
     whole point: P(max <= t) = F(t)^k, so the tail is what k does to it. */
  function pmfMax(pairs, k) {
    var sorted = pairs.slice().sort(function (x, y) { return x[0] - y[0]; });
    var out = [], cum = R(0n, 1n), prev = R(0n, 1n);
    for (var i = 0; i < sorted.length; i += 1) {
      cum = Radd(cum, sorted[i][1]);
      var here = Rpow(cum, k);
      out.push([sorted[i][0], Rsub(here, prev)]);
      prev = here;
    }
    return out;
  }
"""

QUEUE_JS = r"""
  /* Birth-death queues, exact for rational arrival and service rates.

     M/M/1 is derived in the lessons from the cut balance equations, so these
     are the closed forms that result, not a separate model: rho = lam/mu,
     pi_n = (1-rho)rho^n, L = rho/(1-rho), W = L/lam. */
  function mm1(lam, mu) {
    var rho = Rdiv(lam, mu);
    if (Rcmp(rho, R(1n, 1n)) >= 0) return { rho: rho, stable: false };
    var one = R(1n, 1n), free = Rsub(one, rho);
    var L = Rdiv(rho, free);
    var Lq = Rdiv(Rmul(rho, rho), free);
    return {
      rho: rho, stable: true, p0: free, L: L, Lq: Lq,
      W: Rdiv(L, lam), Wq: Rdiv(Lq, lam)
    };
  }

  /* Erlang C: the probability an arrival waits with s servers.
     Rational throughout -- the factorials are BigInt, so a 20-server desk is
     still an exact fraction. */
  function erlangC(lam, mu, s) {
    var a = Rdiv(lam, mu), rho = Rdiv(a, R(BigInt(s), 1n));
    if (Rcmp(rho, R(1n, 1n)) >= 0) return { rho: rho, stable: false };
    var sum = R(0n, 1n), n;
    for (n = 0; n < s; n += 1) sum = Radd(sum, Rdiv(Rpow(a, n), R(fact(n), 1n)));
    var last = Rdiv(Rpow(a, s), Rmul(R(fact(s), 1n), Rsub(R(1n, 1n), rho)));
    var p0 = Rinv(Radd(sum, last));
    var pw = Rmul(last, p0);
    var Lq = Rdiv(Rmul(pw, rho), Rsub(R(1n, 1n), rho));
    return {
      rho: rho, stable: true, p0: p0, pWait: pw, Lq: Lq,
      Wq: Rdiv(Lq, lam), L: Radd(Lq, a), W: Rdiv(Radd(Lq, a), lam)
    };
  }

  /* M/M/1/K: finite capacity. Stable at any rho because the queue cannot grow,
     which is the lesson -- and the arrival rate Little's law may use is the
     EFFECTIVE one, lam(1 - pK). */
  function mm1k(lam, mu, K) {
    var rho = Rdiv(lam, mu), n, un = [], total = R(0n, 1n);
    for (n = 0; n <= K; n += 1) { var t = Rpow(rho, n); un.push(t); total = Radd(total, t); }
    var pi = un.map(function (t) { return Rdiv(t, total); });
    var L = R(0n, 1n);
    for (n = 0; n <= K; n += 1) L = Radd(L, Rmul(R(BigInt(n), 1n), pi[n]));
    var pK = pi[K], lamEff = Rmul(lam, Rsub(R(1n, 1n), pK));
    return { rho: rho, pi: pi, blocking: pK, lamEff: lamEff, L: L, W: Rdiv(L, lamEff) };
  }
"""

AVAIL_JS = r"""
  /* Availability composition. Series multiplies down, parallel multiplies up,
     k-of-n is a binomial tail -- all exact, which matters because the
     interesting answers are differences in the fourth decimal place. */
  function availSeries(list) {
    var a = R(1n, 1n);
    for (var i = 0; i < list.length; i += 1) a = Rmul(a, list[i]);
    return a;
  }
  function availParallel(list) {
    var down = R(1n, 1n);
    for (var i = 0; i < list.length; i += 1) down = Rmul(down, Rsub(R(1n, 1n), list[i]));
    return Rsub(R(1n, 1n), down);
  }
  /* P(at least k of n independent components up), each up with probability a. */
  function availKofN(a, k, n) {
    var total = R(0n, 1n), q = Rsub(R(1n, 1n), a);
    for (var j = k; j <= n; j += 1) {
      total = Radd(total, Rmul(R(comb(n, j), 1n), Rmul(Rpow(a, j), Rpow(q, n - j))));
    }
    return total;
  }
  /* Expected attempts and success under a retry policy of r retries at failure
     probability p: the geometric sum the retry-storm lesson iterates on. */
  function retryAttempts(p, r) {
    var num = Rsub(R(1n, 1n), Rpow(p, r + 1));
    return Rdiv(num, Rsub(R(1n, 1n), p));
  }
  function retrySuccess(p, r) { return Rsub(R(1n, 1n), Rpow(p, r + 1)); }
"""

SLOTTED_JS = r"""
  /* The discrete-time queue: Bernoulli arrivals (p per slot), geometric service
     (q per slot), late arrival with departure first.

     This exists because a slotted simulation is NOT M/M/1 at finite slot size,
     and a lesson that checks the continuous formula against the simulation is
     checking it against a different model. At p = 2/5, q = 1/2 the exact mean
     here is 12/5, while rho/(1 - rho) at rho = p/q = 4/5 is 4 -- the continuous
     formula overstates it by 5/3. The two agree only as the slot shrinks, and
     the convergence panel is the lesson.

     pi_1/pi_0 = p/(q(1-p)); pi_{n+1}/pi_n = p(1-q)/(q(1-p)) for n >= 1. */
  function geoGeo1(p, q) {
    var one = R(1n, 1n);
    var ratio = Rdiv(Rmul(p, Rsub(one, q)), Rmul(q, Rsub(one, p)));
    var first = Rdiv(p, Rmul(q, Rsub(one, p)));
    if (Rcmp(ratio, one) >= 0) return { ratio: ratio, stable: false };
    var tail = Rdiv(one, Rsub(one, ratio));
    var p0 = Rinv(Radd(one, Rmul(first, tail)));
    /* sum_{n>=1} n r^{n-1} = 1/(1-r)^2 */
    var L = Rmul(p0, Rmul(first, Rmul(tail, tail)));
    return { ratio: ratio, stable: true, p0: p0, L: L, rho: Rdiv(p, q) };
  }
"""

TRACE_JS = r"""
  /* Little's Law from a trace, which is how this library proves it: the area
     under the number-in-system curve is both the integral of N and the sum of
     the customers' times, so L = lambda*W is an identity about averages and
     needs no model at all.

     Arrivals and departures are integer slot indices, paired by index. */
  function littleFromTrace(arrivals, departures) {
    var n = arrivals.length, i, horizon = 0;
    for (i = 0; i < n; i += 1) if (departures[i] > horizon) horizon = departures[i];
    var area = 0, totalTime = 0;
    for (i = 0; i < n; i += 1) {
      var w = departures[i] - arrivals[i];
      totalTime += w;          /* sum of times in system */
      area += w;               /* which IS the area under N(t) */
    }
    var T = R(BigInt(horizon), 1n);
    return {
      horizon: horizon,
      L: Rdiv(R(BigInt(area), 1n), T),
      lambda: Rdiv(R(BigInt(n), 1n), T),
      W: Rdiv(R(BigInt(totalTime), 1n), R(BigInt(n), 1n)),
      area: area
    };
  }

  /* N(t) as a step function, for drawing the curve the area is under. */
  function occupancyTrace(arrivals, departures, horizon) {
    var out = [], t, i;
    for (t = 0; t < horizon; t += 1) {
      var c = 0;
      for (i = 0; i < arrivals.length; i += 1) {
        if (arrivals[i] <= t && departures[i] > t) c += 1;
      }
      out.push(c);
    }
    return out;
  }
"""

STREAM_JS = r"""
  /* A seeded stream. number.py's lcgRun detects the cycle of a generator, which
     is a different job; a lab that samples needs the values in order and needs
     the same values every time the page is opened, or a reader cannot check
     what they were told. */
  function lcgStream(a, c, m, seed, count) {
    /* BigInt, not Number. A typical multiplier times a typical state exceeds
       2^53 on the SECOND step, and a double silently rounds it -- the stream
       then looks reproducible, because it is reproducibly wrong. */
    var A = BigInt(a), C = BigInt(c), M = BigInt(m);
    var out = [], x = ((BigInt(seed) % M) + M) % M;
    for (var i = 0; i < count; i += 1) { x = (A * x + C) % M; out.push(Number(x)); }
    return out;
  }
  /* Uniform rationals in [0, 1) from that stream. */
  function streamUniform(a, c, m, seed, count) {
    return lcgStream(a, c, m, seed, count).map(function (x) {
      return R(BigInt(x), BigInt(m));
    });
  }
  /* Inverse-transform sampling from a pmf given as [value, rational] pairs. */
  function sampleFromPmf(pairs, u) {
    var cum = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) {
      cum = Radd(cum, pairs[i][1]);
      if (Rcmp(u, cum) < 0) return pairs[i][0];
    }
    return pairs[pairs.length - 1][0];
  }
"""

APPROX_JS = r"""
  /* The four places this subject cannot be exact. Each says how it rounds.

     Everything else in the module returns a rational. These return Numbers, and
     every lesson that calls one states that it is an approximation -- which is
     the library's rule, not a courtesy. */

  /* e^-x by its alternating series, summed until a term is below tol.
     Used for the Poisson limit and the Bloom filter rate. */
  function expNegApprox(x, tol) {
    var t = 1, s = 1, k = 1;
    tol = tol || 1e-15;
    while (Math.abs(t) > tol && k < 200) { t = -t * x / k; s += t; k += 1; }
    return s;
  }
  /* The Bloom false-positive rate. The exact form (1 - 1/m)^(kn) is available
     as a rational; this is the (1 - e^(-kn/m))^k idealisation lessons compare
     it against. */
  function bloomApprox(m, n, k) {
    return Math.pow(1 - expNegApprox(k * n / m, 1e-15), k);
  }
  /* Standard error of a proportion. A square root, so it rounds. */
  function standardErrorApprox(p, n) { return Math.sqrt(p * (1 - p) / n); }
  /* The Zipf normaliser past the point where its exact form is unreadable.
     harmonic() stays exact and is what the lessons use; this is for the
     lesson that asks what happens at a million keys. */
  function harmonicApprox(n, s) {
    if (s === 1) return Math.log(n) + 0.5772156649015329 + 1 / (2 * n);
    var t = 0;
    for (var k = 1; k <= n && k <= 100000; k += 1) t += 1 / Math.pow(k, s);
    return t;
  }
  /* Bits per key for a target false-positive rate: 1.44 * log2(1/p). */
  function bitsPerKeyApprox(target) { return Math.log2(1 / target) / Math.LN2 * Math.LN2 * 1.4426950408889634; }
"""

__all__ = ["HARMONIC_JS", "PERCENTILE_JS", "PMF_JS", "QUEUE_JS", "SLOTTED_JS",
           "TRACE_JS", "STREAM_JS", "AVAIL_JS", "APPROX_JS"]
