"""Course 6: Replication and Consistency -- one kit, thirteen modes, one arithmetic.

Replication is bought in four currencies and the reader's intuition is wrong
about all four. This kit exists to make each one a number the reader moves.

Four decisions run through all thirteen modes.

  MILLISECONDS FOR TIME, MICROSECONDS FOR CLOCKS. Latency, lag and quorum
  distributions are integer milliseconds, the same unit course 2 uses, so a
  reader carrying a pmf across from `latency` finds it means the same thing.
  Clock skew is the one exception and it is microseconds, because a drift rate
  in parts per million IS microseconds per second and converting it to
  milliseconds puts a decimal point in the only place on this course where the
  arithmetic would then stop being integral. `skewMicros` does the conversion
  once, where scripts/mathcheck.js can call it.

  THE BINOMIAL TAIL IS `availKofN`, NOT A SECOND COPY. A quorum ack is "at
  least W of N replied by t" and a majority's availability is "at least
  floor(n/2) + 1 of n are up", and those are the same sum over the same
  coefficients that course 5 already ships. `quorumAckBy` and `majorityAvail`
  both call it. Rewriting the tail here would be a second implementation to
  keep right, and the whole argument for the shared core is that there is one.

  EXACT, WITH NOTHING ROUNDED ANYWHERE. Every figure in this kit is a rational
  or an integer count. There is no `Approx` function in it and no mode that
  prints a float: the order statistic is an enumerated pmf, the quorum tails are
  binomial sums over fractions, the overlap counts are combinations, the
  linearizations are counted rather than sampled, and the election probability
  is a finite sum of exact powers. That is unusual on this path -- most courses
  have one rounded figure -- and it is a property of the subject, not a boast.

  THE CAP IS THE LESSON. `linearize` refuses a history of more than six
  operations, and the page says why on its face: the enumeration is 6! = 720
  orders and 7! is 5040. A real checker does not enumerate. Hiding the cap
  behind a silent truncation would teach the opposite of the thing the lesson
  is for, so the refusal prints the factorial it declined to compute.

The modes, and the lesson each belongs to:

  fanout     L1  N read, 1 write, N work, N storage -- and the ceiling 1 + rho
  sync       L2  pmfMax(pairs, N - 1): the slowest follower, not the average
  lag        L3  P(lag > t), against the tail past the MEAN lag
  quorum     L4  R + W - N, with both set families enumerated
  quorumlat  L5  P(at least W of N by t), swept in N -- larger N is faster
  sloppy     L6  C(N-W, R)/C(N, R), exactly 2/3 at N = 3, R = W = 1
  majority   L7  2f + 1, and why the majority of four is worse than of three
  election   L8  sum_j n(1/T)((T-j)/T)^(n-1), and 1/P as an exact fraction
  lamport    L9  max(L_local, L_msg) + 1, with a false pair exhibited
  vector     L10 the vectors, and every incomparable pair listed
  drift      L11 ppm x interval, 2*epsilon, and the order it cannot decide
  linearize  L12 the legal total orders, counted, at most six operations
  merge      L13 what last-writer-wins discards and the counter CRDT does not
"""

from .algebra_core import RATIONAL_JS
from .common import Lab
from .counting import BIGINT_JS
from .sysdesign_core import AVAIL_JS, PERCENTILE_JS, PMF_JS, RCEIL_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

REPLICA_JS = r"""
  /* ================================================================= output

     Rdec goes through Number(a.n)/Number(a.d), and this course builds
     rationals a double cannot hold at either end: F(t)^(N-1) for a
     thousand-weight pmf has a denominator of thirty digits by N = 5, and the
     majority of nine nodes at five nines has one of forty-five. So decimals
     here are long division in BigInt, rounded half up at the last digit. */
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
  /* How many nines: the largest k with 1 - A <= 10^-k, by an exact search over
     powers of ten. No logarithm goes anywhere near a number this page asserts. */
  function ninesOf(a) {
    var down = Rsub(R(1n, 1n), a);
    if (down.n <= 0n) return 99;
    var k = 0, bound = R(1n, 10n);
    while (k < 15 && Rcmp(down, bound) <= 0) { k += 1; bound = Rdiv(bound, R(10n, 1n)); }
    return k;
  }
  /* A percentage with enough places to be worth printing. A majority of five
     at four nines each is 99.999999940%, and a fixed two places renders that
     as 100.00% -- which is the claim course 5 and this course both deny. */
  function RpctAuto(a) {
    if (Requ(a, R(1n, 1n))) return '100%';
    if (Rzero(a)) return '0%';
    return Rpct(a, Math.min(14, Math.max(3, ninesOf(a) + 3)));
  }
  /* Decimal byte units, which is what a replication stream is quoted in:
     1 kB = 1000 B. Stated rather than assumed. */
  function bytesText(bytes) {
    var b = Number(bytes);
    if (b >= 1000000000) return Rfixed(R(BigInt(bytes), 1000000000n), 2) + ' GB';
    if (b >= 1000000) return Rfixed(R(BigInt(bytes), 1000000n), 2) + ' MB';
    if (b >= 1000) return Rfixed(R(BigInt(bytes), 1000n), 2) + ' kB';
    return group(BigInt(bytes)) + ' B';
  }
  /* A rational rounded DOWN to a whole number of bytes, for a figure that is a
     count of bytes rather than a rate. Rfloor is the core's. */
  function bytesFloor(a) { return Rfloor(a); }

  /* ========================================= the distributions three modes share

     A replica's reply time, a follower's lag and a quorum's per-replica
     latency are all one shape: a pmf the reader types as value:weight pairs,
     with the probabilities the exact fractions of those weights. The weights
     are integers, so a 5-atom distribution raised to the 8th power is still a
     fraction and the tail of it is still exact. */
  function parsePmfSpec(text) {
    var parts = String(text).split(','), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var m = /^([0-9]+)\s*:\s*([0-9]+)$/.exec(s);
      if (!m) return null;
      if (Number(m[2]) <= 0) return null;
      out.push([Number(m[1]), Number(m[2])]);
    }
    return out.length ? out : null;
  }
  function pmfFromSpec(spec) {
    var total = 0n, i;
    for (i = 0; i < spec.length; i += 1) total += BigInt(spec[i][1]);
    if (total === 0n) return null;
    var out = [];
    for (i = 0; i < spec.length; i += 1) out.push([spec[i][0], R(BigInt(spec[i][1]), total)]);
    return out.sort(function (a, b) { return a[0] - b[0]; });
  }
  /* F(t) = P(X <= t), exact. */
  function pmfCdfAt(pairs, t) {
    var s = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) if (pairs[i][0] <= t) s = Radd(s, pairs[i][1]);
    return s;
  }
  /* The q-th percentile of a pmf, by the same rank rule sysdesign_core uses on
     a sample: the smallest attainable value whose cumulative probability
     reaches q. A percentile printed here is a value some reply actually took. */
  function pmfPercentile(pairs, q) {
    var sorted = pairs.slice().sort(function (a, b) { return a[0] - b[0]; });
    var cum = R(0n, 1n);
    for (var i = 0; i < sorted.length; i += 1) {
      cum = Radd(cum, sorted[i][1]);
      if (Rcmp(cum, q) >= 0) return sorted[i][0];
    }
    return sorted.length ? sorted[sorted.length - 1][0] : null;
  }
  /* The attainable values, ascending: the only instants at which any of these
     step functions can change, so every search below is over this grid rather
     than over a continuum. */
  function pmfSupport(pairs) {
    var out = [], i;
    for (i = 0; i < pairs.length; i += 1) out.push(pairs[i][0]);
    return out.sort(function (a, b) { return a - b; });
  }
  /* The mass strictly above a RATIONAL threshold. pmfTail takes a number; the
     mean of a pmf is a fraction, and L3's whole argument is about the mass
     past the mean. */
  function tailPastRational(pairs, x) {
    var s = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) {
      if (Rcmp(R(BigInt(pairs[i][0]), 1n), x) > 0) s = Radd(s, pairs[i][1]);
    }
    return s;
  }

  /* =========================================== L1: what a replication factor buys

     N replicas serve reads in parallel and every one of them must apply every
     write. So the four multipliers are N, 1, N and N, and the cluster's
     throughput is whatever that leaves. With rho reads per write, a replica
     carries ALL the writes plus 1/N of the reads:

         T/(1 + rho) + (T rho/(1 + rho))/N  <=  c
         T(N)  =  c N (1 + rho) / (N + rho)

     which rises with N and stops at c(1 + rho). That ceiling is the read/write
     ratio and nothing else -- it is the number course 1 computed, and it is
     what decides whether a replication factor pays. At rho = 0, T(N) = c for
     every N: a write-only workload gets nothing at all from replication. */
  function fanoutSpeedup(n, rho) {
    var N = R(BigInt(n), 1n), one = R(1n, 1n);
    return Rdiv(Rmul(N, Radd(one, rho)), Radd(N, rho));
  }
  function fanoutCeiling(rho) { return Radd(R(1n, 1n), rho); }
  function fanoutPlan(perReplica, n, rho) {
    var c = perReplica, one = R(1n, 1n), N = R(BigInt(n), 1n);
    var speedup = fanoutSpeedup(n, rho);
    var total = Rmul(c, speedup);
    var writes = Rdiv(total, Radd(one, rho));
    var reads = Rsub(total, writes);
    return {
      readCapacity: Rmul(c, N),        /* N x, if every op were a read */
      writeCapacity: c,                /* 1 x, whatever N is */
      workMultiplier: N,               /* N x the write work */
      storageMultiplier: N,            /* N x the bytes */
      total: total, reads: reads, writes: writes,
      speedup: speedup, ceiling: fanoutCeiling(rho),
      perReplicaLoad: Radd(writes, Rdiv(reads, N))
    };
  }

  /* ======================================== L2: a sync write waits for the slowest

     The write is acknowledged when the LAST of the N - 1 followers has acked,
     so its distribution is the maximum of N - 1 independent copies and
     P(max <= t) = F(t)^(N-1). pmfMax does that exactly.

     At N = 1 there is no follower to wait for, so the wait is zero rather than
     one copy of the distribution -- the degenerate case has to be right or the
     "N times one replica" comparison starts from the wrong place. */
  function syncAckPmf(pairs, n) {
    if (n <= 1) return [[0, R(1n, 1n)]];
    return pmfMax(pairs, n - 1);
  }
  /* The misconception, computed rather than asserted: N times one replica's
     own percentile, which is exactly what "synchronising to three replicas
     costs three times one replica's latency" predicts. The write waits for
     the MAXIMUM of N - 1 replicas, and a maximum is not a sum. */
  function naiveSyncCost(pairs, n, q) {
    return pmfPercentile(pairs, q) * n;
  }
  /* The asynchronous alternative charges no latency and risks bytes instead:
     the writes that have left the leader and reached nobody. */
  function asyncAtRiskBytes(writesPerSec, lagMs, bytesPerWrite) {
    return Rdiv(Rmul(Rmul(R(BigInt(writesPerSec), 1n), lagMs), R(BigInt(bytesPerWrite), 1n)),
                R(1000n, 1n));
  }

  /* ================================================ L3: a stale read is the TAIL

     A read issued t after the write is stale exactly when the follower's lag
     exceeds t, so P(stale) = P(lag > t). Read-your-writes and monotonic reads
     are the two guarantees that fail on precisely this mass. */
  function staleProb(pairs, t) { return pmfTail(pairs, t); }
  function staleReadsPerSec(pairs, t, ratePerSec) {
    return Rmul(pmfTail(pairs, t), R(BigInt(ratePerSec), 1n));
  }
  /* The delay at which staleness has fallen to 1 - q. */
  function freshDelay(pairs, q) { return pmfPercentile(pairs, q); }

  /* ============================================== L4: overlap, by the pigeonhole

     A read set of R and a write set of W have R + W members between them among
     N nodes. If R + W > N they cannot all be distinct, so at least R + W - N
     of them are the same node -- and that minimum is attained, which is why
     the number is the minimum and not merely a bound.

     The sets are enumerated rather than counted because L4's objective is to
     exhibit a disjoint pair when one exists. C(9,4) = 126, so the worst case
     the controls allow is 126 x 126 = 15 876 pairs. */
  function quorumOverlap(n, r, w) { return r + w - n; }
  function quorumOverlaps(n, r, w) { return r + w > n; }
  /* Every k-subset of {0..n-1}, in lexicographic order. */
  function subsets(n, k) {
    var out = [], idx = [], i;
    if (k < 0 || k > n) return out;
    for (i = 0; i < k; i += 1) idx.push(i);
    for (;;) {
      out.push(idx.slice());
      var j = k - 1;
      while (j >= 0 && idx[j] === n - k + j) j -= 1;
      if (j < 0) return out;
      idx[j] += 1;
      for (i = j + 1; i < k; i += 1) idx[i] = idx[i - 1] + 1;
    }
  }
  function overlapSize(a, b) {
    var c = 0;
    for (var i = 0; i < a.length; i += 1) if (b.indexOf(a[i]) >= 0) c += 1;
    return c;
  }
  /* The smallest overlap over every (write set, read set) pair, and the first
     pair that misses entirely -- the counterexample the lesson exhibits. */
  function quorumScan(n, r, w) {
    var W = subsets(n, w), Rs = subsets(n, r), i, j;
    if (!W.length || !Rs.length) {
      return { min: 0, disjoint: 0, witness: null, writeSets: W, readSets: Rs, pairs: 0 };
    }
    var min = n + 1, disjoint = 0, witness = null;
    for (i = 0; i < W.length; i += 1) {
      for (j = 0; j < Rs.length; j += 1) {
        var o = overlapSize(W[i], Rs[j]);
        if (o < min) min = o;
        if (o === 0) { disjoint += 1; if (!witness) witness = { write: W[i], read: Rs[j] }; }
      }
    }
    return { min: min, disjoint: disjoint, witness: witness,
             writeSets: W, readSets: Rs, pairs: W.length * Rs.length };
  }
  /* The same count without enumerating: C(n,w) write sets, each missed by the
     C(n-w,r) read sets drawn from the nodes the write did not touch. The page
     computes both and prints their agreement. */
  function disjointPairCount(n, r, w) { return comb(n, w) * comb(n - w, r); }

  /* =================================== L5: a quorum waits for the W-th fastest

     P(ack by t) = P(at least W of the N replies have arrived by t), which is
     the binomial tail at success probability F(t) -- availKofN, the same sum
     course 5 uses for a k-of-n availability. It is not rewritten here.

     With W fixed, raising N adds terms to that tail and can only raise it. So
     MORE REPLICAS MAKE THE WRITE FASTER, which is the one result on this
     course readers refuse until they have computed it. */
  function quorumAckBy(pairs, t, w, n) {
    if (w <= 0) return R(1n, 1n);
    if (w > n) return R(0n, 1n);
    return availKofN(pmfCdfAt(pairs, t), w, n);
  }
  function quorumPercentile(pairs, w, n, q) {
    var vals = pmfSupport(pairs), i;
    for (i = 0; i < vals.length; i += 1) {
      if (Rcmp(quorumAckBy(pairs, vals[i], w, n), q) >= 0) return vals[i];
    }
    return null;
  }
  function quorumSweep(pairs, w, maxN, q) {
    var rows = [], n;
    for (n = w; n <= maxN; n += 1) {
      rows.push({ n: n, p: quorumPercentile(pairs, w, n, q) });
    }
    return rows;
  }

  /* ============================================ L6: what a sloppy quorum misses

     With R + W <= N a read set can miss every node the write touched. The
     write landed on some W of the N; the read picks R of the N, and it misses
     the write entirely when all R come from the N - W the write did not touch:

         P(miss) = C(N - W, R) / C(N, R)

     At N = 3, R = W = 1 that is C(2,1)/C(3,1) = 2/3. Two reads in three miss a
     write that was acknowledged. comb returns 0 for R > N - W, which is the
     right answer and not a guard: past that point no read set can avoid the
     write. */
  function sloppyMiss(n, r, w) {
    var whole = comb(n, r);
    if (whole === 0n) return null;
    return R(comb(n - w, r), whole);
  }
  function sloppyHit(n, r, w) {
    var m = sloppyMiss(n, r, w);
    return m === null ? null : Rsub(R(1n, 1n), m);
  }

  /* =============================== L7: 2f + 1, and the node that buys nothing

     A majority of n is floor(n/2) + 1, so a cluster survives n - (floor(n/2) +
     1) = floor((n - 1)/2) failures. Four nodes tolerate one, exactly as three
     do. Worse: the majority of four is THREE, so its availability is the
     probability three of four are up -- lower than two of three. The fourth
     node costs money and buys negative reliability. */
  function majoritySize(n) { return Math.floor(n / 2) + 1; }
  function faultsTolerated(n) { return Math.floor((n - 1) / 2); }
  function majorityAvail(a, n) { return availKofN(a, majoritySize(n), n); }
  function evenIsWasted(n) { return n >= 2 && n % 2 === 0; }

  /* ================================================ L8: the split vote, exactly

     n candidates each pick one of T slots uniformly. The election is clean when
     exactly one candidate holds the strictly earliest slot: choose that
     candidate (n ways), choose its slot j (probability 1/T), and require the
     other n - 1 to land strictly later, which they do with probability
     ((T - j)/T)^(n-1).

         P(clean) = sum_{j=1..T} n (1/T) ((T - j)/T)^(n-1)

     At T = 1 every term carries a factor of zero, so a FIXED timeout is a
     guaranteed tie for n >= 2. That is the whole reason the timeout is
     randomised, and it falls straight out of the formula. */
  function electionTerm(n, T, j) {
    return Rmul(R(BigInt(n), BigInt(T)), Rpow(R(BigInt(T - j), BigInt(T)), n - 1));
  }
  function electionClean(n, T) {
    var s = R(0n, 1n), j;
    if (n <= 0 || T <= 0) return R(0n, 1n);
    for (j = 1; j <= T; j += 1) s = Radd(s, electionTerm(n, T, j));
    return s;
  }
  /* Rounds until one succeeds: a geometric mean, 1/P. Null when P is zero,
     because "expected rounds" is then not a number and printing a large one
     would be a lie about a process that never terminates. */
  function electionRounds(n, T) {
    var p = electionClean(n, T);
    return Rzero(p) ? null : Rinv(p);
  }
  /* The window a target clean-election rate needs. P(clean) rises with T --
     more slots, fewer ties -- so a binary search is exact, and it matters:
     scanning to 400 evaluates eighty thousand exact-power terms and a reader
     dragging the candidate slider feels every one of them. */
  function slotsForClean(n, target, limit) {
    if (Rcmp(electionClean(n, 1), target) >= 0) return 1;
    if (Rcmp(electionClean(n, limit), target) < 0) return null;
    var lo = 1, hi = limit;
    while (lo + 1 < hi) {
      var mid = (lo + hi) >> 1;
      if (Rcmp(electionClean(n, mid), target) >= 0) hi = mid; else lo = mid;
    }
    return hi;
  }

  /* ======================================= L9, L10: a message diagram, stamped

     The spec a reader edits is "A:4 B:4 C:3; A2 to B2; B3 to C2", meaning
     three processes with that many local events each, a message sent at A's
     second event and delivered at B's second, and another from B's third to
     C's second. "to", "->", ">" and "-" are all accepted as the arrow, and the
     presets use the word: a ">" inside an HTML attribute value truncates the
     tag for every regex-based reader of a page, labcheck's DOM shim included,
     so a default carrying one would arrive at the lab empty.

     Parsing returns null on anything that is not a diagram: a typo must not
     print confident stamps for a graph that does not exist. */
  function parseDiagram(text) {
    var chunks = String(text).split(';'), i;
    var head = (chunks[0] || '').trim();
    if (!head) return null;
    var procs = [], names = {}, parts = head.split(/\s+/);
    for (i = 0; i < parts.length; i += 1) {
      var m = /^([A-Z]):([1-9]|10)$/.exec(parts[i].trim());
      if (!m) return null;
      if (Object.prototype.hasOwnProperty.call(names, m[1])) return null;
      names[m[1]] = procs.length;
      procs.push({ name: m[1], count: Number(m[2]) });
    }
    if (!procs.length || procs.length > 4) return null;
    var msgs = [], taken = {}, sent = {};
    for (i = 1; i < chunks.length; i += 1) {
      var s = chunks[i].trim();
      if (!s) continue;
      var g = /^([A-Z])([0-9]+)\s*(?:to|->|>|-)\s*([A-Z])([0-9]+)$/.exec(s);
      if (!g) return null;
      if (!Object.prototype.hasOwnProperty.call(names, g[1])) return null;
      if (!Object.prototype.hasOwnProperty.call(names, g[3])) return null;
      var from = names[g[1]], fe = Number(g[2]) - 1;
      var to = names[g[3]], te = Number(g[4]) - 1;
      if (from === to) return null;
      if (fe >= procs[from].count || te >= procs[to].count) return null;
      var rk = to + ':' + te, sk = from + ':' + fe;
      if (taken[rk] || sent[rk] || taken[sk] || sent[sk]) return null;
      taken[rk] = true;
      sent[sk] = true;
      msgs.push({ from: from, fromEvent: fe, to: to, toEvent: te });
    }
    return { procs: procs, msgs: msgs };
  }
  /* The events in one flat list, process by process, with the two edges that
     define happens-before: the previous event on the same process, and the
     send a receive is waiting for. The flat order makes the previous event on
     a process exactly index - 1, which is what lets one pass be correct. */
  function diagramEvents(d) {
    var out = [], p, e, i;
    for (p = 0; p < d.procs.length; p += 1) {
      for (e = 0; e < d.procs[p].count; e += 1) {
        out.push({ proc: p, index: e, name: d.procs[p].name + (e + 1), recv: -1, send: -1 });
      }
    }
    var at = {};
    for (i = 0; i < out.length; i += 1) at[out[i].proc + ':' + out[i].index] = i;
    for (var m = 0; m < d.msgs.length; m += 1) {
      var s = at[d.msgs[m].from + ':' + d.msgs[m].fromEvent];
      var r = at[d.msgs[m].to + ':' + d.msgs[m].toEvent];
      out[r].recv = s;
      out[s].send = r;
    }
    return out;
  }
  /* A topological order of the events, or null if the messages make a cycle --
     a diagram in which a message is received before it was sent. Kahn, so the
     null is a proof rather than an iteration limit. */
  function diagramOrder(events) {
    var n = events.length, indeg = [], adj = [], i, k;
    for (i = 0; i < n; i += 1) { indeg.push(0); adj.push([]); }
    for (i = 0; i < n; i += 1) {
      if (events[i].index > 0) { adj[i - 1].push(i); indeg[i] += 1; }
      if (events[i].recv >= 0) { adj[events[i].recv].push(i); indeg[i] += 1; }
    }
    var queue = [], order = [];
    for (i = 0; i < n; i += 1) if (indeg[i] === 0) queue.push(i);
    while (queue.length) {
      var v = queue.shift();
      order.push(v);
      for (k = 0; k < adj[v].length; k += 1) {
        indeg[adj[v][k]] -= 1;
        if (indeg[adj[v][k]] === 0) queue.push(adj[v][k]);
      }
    }
    return order.length === n ? order : null;
  }
  /* L(e) = max(L of the previous event on this process, L of the send this
     event receives) + 1. */
  function lamportStamps(d) {
    var events = diagramEvents(d), order = diagramOrder(events), i;
    if (!order) return null;
    var L = [];
    for (i = 0; i < events.length; i += 1) L.push(0);
    for (i = 0; i < order.length; i += 1) {
      var v = order[i], best = 0;
      if (events[v].index > 0 && L[v - 1] > best) best = L[v - 1];
      if (events[v].recv >= 0 && L[events[v].recv] > best) best = L[events[v].recv];
      L[v] = best + 1;
    }
    return L;
  }
  /* The vector version: elementwise maximum of the same two predecessors, then
     increment this process's own component. */
  function vectorStamps(d) {
    var events = diagramEvents(d), order = diagramOrder(events), i, j;
    if (!order) return null;
    var k = d.procs.length, V = [];
    for (i = 0; i < events.length; i += 1) {
      var z = [];
      for (j = 0; j < k; j += 1) z.push(0);
      V.push(z);
    }
    for (i = 0; i < order.length; i += 1) {
      var v = order[i], cur = [];
      for (j = 0; j < k; j += 1) cur.push(0);
      if (events[v].index > 0) for (j = 0; j < k; j += 1) { if (V[v - 1][j] > cur[j]) cur[j] = V[v - 1][j]; }
      if (events[v].recv >= 0) {
        for (j = 0; j < k; j += 1) { if (V[events[v].recv][j] > cur[j]) cur[j] = V[events[v].recv][j]; }
      }
      cur[events[v].proc] += 1;
      V[v] = cur;
    }
    return V;
  }
  /* -1 if a happens before b, 1 if b before a, 0 if equal, NULL if neither --
     which is what concurrent means. Not "at the same time": incomparable. */
  function vecCompare(a, b) {
    var le = true, ge = true, i;
    for (i = 0; i < a.length; i += 1) {
      if (a[i] > b[i]) le = false;
      if (a[i] < b[i]) ge = false;
    }
    if (le && ge) return 0;
    if (le) return -1;
    if (ge) return 1;
    return null;
  }
  function concurrentPairs(V) {
    var out = [], i, j;
    for (i = 0; i < V.length; i += 1) {
      for (j = i + 1; j < V.length; j += 1) if (vecCompare(V[i], V[j]) === null) out.push([i, j]);
    }
    return out;
  }
  /* L9's counterexample: a pair with L(a) < L(b) where a does NOT happen
     before b. Lamport's converse fails exactly here, and the only way to know
     it failed is the vector clock of L10. */
  function lamportFalsePairs(L, V) {
    var out = [], i, j;
    for (i = 0; i < L.length; i += 1) {
      for (j = 0; j < L.length; j += 1) {
        if (i === j) continue;
        if (L[i] < L[j] && vecCompare(V[i], V[j]) === null) out.push([i, j]);
      }
    }
    return out;
  }
  /* The direction that DOES hold: a happens before b implies L(a) < L(b). The
     page checks it on the reader's own diagram rather than asserting it. */
  function lamportConsistent(L, V) {
    var i, j;
    for (i = 0; i < L.length; i += 1) {
      for (j = 0; j < L.length; j += 1) {
        if (i === j) continue;
        if (vecCompare(V[i], V[j]) === -1 && !(L[i] < L[j])) return false;
      }
    }
    return true;
  }

  /* ========================================== L11: drift, skew and commit-wait

     A clock drifting d parts per million gains or loses d MICROSECONDS every
     second -- that is what ppm means -- so between corrections s seconds apart
     it can be off by d*s microseconds. Two clocks can be off in opposite
     directions, so the uncertainty on comparing their timestamps is 2*epsilon,
     and waiting 2*epsilon before committing turns a bound into an order.

     NTP does not make clocks equal. It bounds how far apart they drift between
     corrections, and this is that bound. */
  function skewMicros(ppm, intervalSec) {
    return Rmul(R(BigInt(ppm), 1n), R(BigInt(intervalSec), 1n));
  }
  function commitWaitMicros(ppm, intervalSec) {
    return Rmul(R(2n, 1n), skewMicros(ppm, intervalSec));
  }
  /* Wall-clock order is trustworthy only when the true separation exceeds the
     window. Inside it, the two timestamps can disagree with reality and
     nothing on either machine can tell. */
  function orderTrustworthy(gapMicros, ppm, intervalSec) {
    return Rcmp(gapMicros, commitWaitMicros(ppm, intervalSec)) > 0;
  }
  /* How many times the true gap the uncertainty window is. Above one, the
     order is undecidable from the clocks alone. */
  function windowRatio(gapMicros, ppm, intervalSec) {
    if (Rzero(gapMicros)) return null;
    return Rdiv(commitWaitMicros(ppm, intervalSec), gapMicros);
  }

  /* ========================================= L12: linearizability by enumeration

     A history is linearizable exactly when SOME total order of its operations
     is both consistent with real time -- if a returned before b was invoked,
     a comes first -- and legal for a register: a read returns the value of the
     most recent write. So enumerate the orders and count the legal ones. The
     count is a proof either way, and zero is a violation.

     SIX OPERATIONS, AND THE CAP IS THE LESSON. 6! is 720 orders, 7! is 5040,
     10! is 3 628 800. The enumeration is factorial and no amount of care makes
     it otherwise, which is why a real checker searches with pruning instead
     and why the general problem is NP-hard. The refusal below prints the
     factorial it declined to compute rather than silently truncating. */
  function parseHistory(text) {
    /* Split on ";" and not "," -- the interval [2, 6] contains a comma, and a
       separator that appears inside an operation is a separator that silently
       cuts every operation in half. */
    var parts = String(text).split(';'), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var m = /^([A-Z])\s*(w|r)\s*([0-9]+)\s*\[\s*([0-9]+)\s*,\s*([0-9]+)\s*\]$/.exec(s);
      if (!m) return null;
      var st = Number(m[4]), en = Number(m[5]);
      if (en <= st) return null;
      out.push({ client: m[1], kind: m[2], value: Number(m[3]), start: st, end: en,
                 name: m[1] + ' ' + (m[2] === 'w' ? 'write ' : 'read ') + m[3],
                 shortName: m[1] + '.' + m[2] + m[3] });
    }
    if (!out.length || out.length > 12) return null;
    return out;
  }
  /* The real-time partial order: a precedes b when a RETURNED before b was
     INVOKED. Overlapping operations are concurrent and may go either way,
     which is the freedom the enumeration searches. */
  function realTimeBefore(a, b) { return a.end <= b.start; }
  function orderRespectsRealTime(ops, perm) {
    var i, j;
    for (i = 0; i < perm.length; i += 1) {
      for (j = i + 1; j < perm.length; j += 1) {
        if (realTimeBefore(ops[perm[j]], ops[perm[i]])) return false;
      }
    }
    return true;
  }
  /* Legal for a register starting at `initial`: every read returns whatever
     the last write put there. */
  function orderLegal(ops, perm, initial) {
    var value = initial, i;
    for (i = 0; i < perm.length; i += 1) {
      var op = ops[perm[i]];
      if (op.kind === 'w') { value = op.value; continue; }
      if (op.value !== value) return false;
    }
    return true;
  }
  /* Every permutation of 0..k-1. Built by insertion, so the count is exactly
     k! and mathcheck can check it against fact(k). */
  function permutations(k) {
    if (k <= 0) return [[]];
    var base = permutations(k - 1), out = [], i, j;
    for (i = 0; i < base.length; i += 1) {
      for (j = 0; j <= base[i].length; j += 1) {
        var p = base[i].slice();
        p.splice(j, 0, k - 1);
        out.push(p);
      }
    }
    return out;
  }
  function linearizations(ops, initial) {
    var perms = permutations(ops.length), valid = [], rt = 0, i;
    for (i = 0; i < perms.length; i += 1) {
      if (!orderRespectsRealTime(ops, perms[i])) continue;
      rt += 1;
      if (orderLegal(ops, perms[i], initial)) valid.push(perms[i]);
    }
    return { total: perms.length, realTime: rt, valid: valid };
  }
  /* The two counts a reader should be able to check by hand on three
     operations: the concurrent pairs, and the pairs real time has already
     decided. Together they are C(k,2). */
  function historyPairs(ops) {
    var forced = 0, concurrent = 0, i, j;
    for (i = 0; i < ops.length; i += 1) {
      for (j = i + 1; j < ops.length; j += 1) {
        if (realTimeBefore(ops[i], ops[j]) || realTimeBefore(ops[j], ops[i])) forced += 1;
        else concurrent += 1;
      }
    }
    return { forced: forced, concurrent: concurrent };
  }

  /* ================================== L13: what each merge throws away, counted

     The trace is a list of updates: "B:5:+3" is replica B adding three at time
     5. No replica has seen any other's update, which is what makes them
     concurrent.

     LAST-WRITER-WINS keeps one replica's register and discards the rest. The
     winner holds the largest timestamp -- ties broken by replica name, which is
     what a real LWW register does and is why "the clocks are accurate" does
     not save it -- and its value is the sum of ITS OWN deltas. Every update at
     any other replica is gone, and the page lists them by name.

     THE COUNTER CRDT keeps one count per replica. The merge is the elementwise
     maximum and the value is the sum, and because maximum is commutative,
     associative and idempotent the merged state does not depend on the order
     the replicas met in or on how many times they met. Nothing is discarded,
     and the total is the sum of every delta in the trace. */
  function parseTrace(text) {
    var parts = String(text).split(','), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var m = /^([A-Z])\s*:\s*([0-9]+)\s*:\s*\+?([0-9]+)$/.exec(s);
      if (!m) return null;
      var delta = Number(m[3]);
      if (delta <= 0) return null;          /* a grow-only counter grows */
      out.push({ replica: m[1], ts: Number(m[2]), delta: delta,
                 name: m[1] + ' +' + delta + ' at t=' + Number(m[2]) });
    }
    if (!out.length || out.length > 12) return null;
    return out;
  }
  function traceReplicas(trace) {
    var seen = [], i;
    for (i = 0; i < trace.length; i += 1) {
      if (seen.indexOf(trace[i].replica) < 0) seen.push(trace[i].replica);
    }
    return seen.sort();
  }
  function traceTotal(trace) {
    var t = 0;
    for (var i = 0; i < trace.length; i += 1) t += trace[i].delta;
    return t;
  }
  function lwwMerge(trace) {
    var i, best = 0, tied = false;
    for (i = 1; i < trace.length; i += 1) {
      if (trace[i].ts > trace[best].ts) { best = i; tied = false; continue; }
      if (trace[i].ts === trace[best].ts && trace[i].replica !== trace[best].replica) {
        tied = true;
        if (trace[i].replica > trace[best].replica) best = i;
      }
    }
    var winner = trace[best].replica, value = 0, kept = [], lost = [];
    for (i = 0; i < trace.length; i += 1) {
      if (trace[i].replica === winner) { value += trace[i].delta; kept.push(trace[i].name); }
      else lost.push(trace[i].name);
    }
    return { winner: winner, value: value, kept: kept, lost: lost,
             tieBroken: tied, discarded: traceTotal(trace) - value };
  }
  function crdtCounts(trace) {
    var reps = traceReplicas(trace), counts = {}, i;
    for (i = 0; i < reps.length; i += 1) counts[reps[i]] = 0;
    for (i = 0; i < trace.length; i += 1) counts[trace[i].replica] += trace[i].delta;
    return counts;
  }
  function crdtValue(counts) {
    var t = 0, k;
    for (k in counts) if (Object.prototype.hasOwnProperty.call(counts, k)) t += counts[k];
    return t;
  }
  /* The merge itself, so the three laws can be checked rather than claimed. */
  function crdtJoin(a, b) {
    var out = {}, k;
    for (k in a) if (Object.prototype.hasOwnProperty.call(a, k)) out[k] = a[k];
    for (k in b) {
      if (!Object.prototype.hasOwnProperty.call(b, k)) continue;
      out[k] = (out[k] === undefined || b[k] > out[k]) ? b[k] : out[k];
    }
    return out;
  }
  function countsEqual(a, b) {
    var k;
    for (k in a) if (Object.prototype.hasOwnProperty.call(a, k) && b[k] !== a[k]) return false;
    for (k in b) if (Object.prototype.hasOwnProperty.call(b, k) && a[k] !== b[k]) return false;
    return true;
  }
  /* The per-replica state after a replica has applied only its own updates --
     which is the state the merges above are merging. */
  function replicaStates(trace) {
    var reps = traceReplicas(trace), out = {}, i, j;
    for (i = 0; i < reps.length; i += 1) {
      var v = {};
      for (j = 0; j < reps.length; j += 1) v[reps[j]] = 0;
      for (j = 0; j < trace.length; j += 1) if (trace[j].replica === reps[i]) v[reps[i]] += trace[j].delta;
      out[reps[i]] = v;
    }
    return out;
  }
"""

_CORE_JS = (RATIONAL_JS + BIGINT_JS + RCEIL_JS + PERCENTILE_JS + PMF_JS
            + AVAIL_JS + REPLICA_JS)


# ---------------------------------------------------------------------------
# Control furniture. The same three shapes every lab on the path uses, so a
# reader moving between courses moves between the same widgets. Drawings use
# only the viewBox widths theme.py gives a horizontal-scroll minimum -- 520 for
# a chart, 660 for a space-time diagram -- because any other width shrinks the
# labels to illegibility on a phone instead of scrolling.
# ---------------------------------------------------------------------------


def _attr(text):
    """A value safe to put inside a double-quoted HTML attribute."""
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


def _text(cid, label, value):
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, label, cid, _attr(value))
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


# The per-replica reply-time distribution L2 and L5 share. Five atoms, a
# thousand weights, and a tail that is thin enough for the percentile to move
# when N does -- which is the whole point of both lessons.
_REPLY_PMF = "2:600, 4:300, 8:70, 16:22, 24:6, 40:2"

# The follower-lag distribution of L3. Its mean is 33.7 ms and a fifth of the
# mass is above that, which is the lesson.
_LAG_PMF = "10:500, 25:300, 50:120, 120:60, 250:15, 400:5"

# The message diagram L9 and L10 share, so that the two lessons stamp the same
# picture and the reader can compare what each kind of clock could see.
_DIAGRAM = "A:4 B:4 C:3; A2 to B2; B3 to C2; C1 to A4"


# ---------------------------------------------------------------------------
# L1 - fanout
# ---------------------------------------------------------------------------


def _fanout(cfg):
    n = int(cfg.get("n", 3))
    rho = int(cfg.get("reads_per_write", 9))
    per_replica = int(cfg.get("per_replica_ops", 1000))

    markup = (
        _toolbar(
            "What a replication factor buys",
            "N&times; reads, 1&times; writes, N&times; work, N&times; storage",
            [("cyan", "read capacity"), ("red", "write capacity"),
             ("amber", "write work and storage"), ("purple", "the ceiling")],
        )
        + _stage(_svg("fnPlot", "0 0 520 200",
                      "Cluster throughput against the number of replicas, with the read/write ceiling drawn."))
        + _table("fnTable")
        + _banner("fnStatus")
    )
    controls = (
        _range("fnN", "Replicas N", 1, 12, n)
        + _range("fnRho", "Reads per write", 0, 60, rho)
        + _range("fnCap", "One replica&rsquo;s capacity (ops/s)", 100, 5000, per_replica, step=100)
        + _kpis(
            [
                ("Read capacity", "fnRead"),
                ("Write capacity", "fnWrite"),
                ("Write work", "fnWork"),
                ("Storage", "fnStore"),
                ("Cluster throughput", "fnTotal"),
                ("Speed-up, and its ceiling", "fnSpeed"),
            ]
        )
        + _hint(
            "fnHint",
            "Every replica applies every write, so the write column never moves however many "
            "replicas you add. The read column is the only one that scales, which is why the "
            "read/write ratio &mdash; and not the replication factor &mdash; sets the ceiling.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('fnN'), rhoS = document.getElementById('fnRho');
  var capS = document.getElementById('fnCap');
  var plot = document.getElementById('fnPlot'), table = document.getElementById('fnTable');
  var status = document.getElementById('fnStatus');

  function redraw() {
    var n = +nS.value, rhoN = +rhoS.value, cap = +capS.value;
    document.getElementById('fnNOut').textContent = n + (n === 1 ? ' replica' : ' replicas');
    document.getElementById('fnRhoOut').textContent = rhoN + ' : 1';
    document.getElementById('fnCapOut').textContent = group(cap) + ' ops/s';

    var rho = R(BigInt(rhoN), 1n), c = R(BigInt(cap), 1n);
    var plan = fanoutPlan(c, n, rho);
    var one = fanoutPlan(c, 1, rho);

    document.getElementById('fnRead').textContent = n + '&times; = ' + Rtext(plan.readCapacity) + ' reads/s';
    document.getElementById('fnWrite').textContent = '1&times; = ' + Rtext(plan.writeCapacity) + ' writes/s';
    document.getElementById('fnWork').textContent = n + '&times; (' + n + ' applications of every write)';
    document.getElementById('fnStore').textContent = n + '&times; the bytes';
    document.getElementById('fnTotal').textContent = Rfixed(plan.total, 1) + ' ops/s';
    document.getElementById('fnSpeed').textContent = Rfixed(plan.speedup, 4) + '&times;, ceiling '
      + Rtext(plan.ceiling) + '&times;';

    var rows = '', i, prev = null;
    for (i = 1; i <= 12; i += 1) {
      var p = fanoutPlan(c, i, rho);
      var gain = prev === null ? null : Rsub(p.total, prev);
      rows += '<tr' + (i === n ? ' class="tone-cyan"' : '') + '><td>' + i + '</td>'
        + '<td>' + Rtext(Rmul(c, R(BigInt(i), 1n))) + '</td>'
        + '<td class="tone-red">' + Rtext(c) + '</td>'
        + '<td class="tone-amber">' + i + '&times;</td>'
        + '<td>' + Rfixed(p.total, 1) + '</td>'
        + '<td>' + Rfixed(p.speedup, 4) + '&times;</td>'
        + '<td>' + (gain === null ? '&mdash;' : '+' + Rfixed(gain, 1)) + '</td></tr>';
      prev = p.total;
    }
    table.innerHTML = '<thead><tr><th>N</th><th>read capacity</th><th>write capacity</th>'
      + '<th>write work<br>and storage</th><th>cluster ops/s</th><th>speed-up</th>'
      + '<th>what the<br>last replica added</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="7" class="small-copy">Column three is constant by construction: a '
      + 'write must be applied by every replica, so the cluster&rsquo;s write capacity is one '
      + 'replica&rsquo;s however many you buy. Column six rises to ' + Rtext(plan.ceiling)
      + '&times; and stops.</td></tr></tfoot>';

    var ceil = parseFloat(Rfixed(Rmul(c, plan.ceiling), 4));
    var top = Math.max(ceil, parseFloat(Rfixed(Rmul(c, R(12n, 1n)), 4)) / 4) || 1;
    function px(i) { return 30 + ((i - 1) / 11) * 470; }
    function py(v) { return 168 - Math.min(1, v / top) * 140; }
    var pts = [], s = '';
    for (i = 1; i <= 12; i += 1) {
      pts.push(px(i) + ',' + py(parseFloat(Rfixed(fanoutPlan(c, i, rho).total, 4))));
    }
    s += '<line x1="30" y1="' + py(ceil) + '" x2="500" y2="' + py(ceil)
      + '" stroke="var(--purple)" stroke-width="1.5" stroke-dasharray="5 4" />'
      + '<text x="30" y="' + (py(ceil) - 5) + '" font-size="10" fill="var(--purple)">ceiling = c(1 + '
      + rhoN + ') = ' + Rfixed(Rmul(c, plan.ceiling), 0) + ' ops/s, which no N reaches</text>';
    s += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />';
    for (i = 1; i <= 12; i += 1) {
      var v = parseFloat(Rfixed(fanoutPlan(c, i, rho).total, 4));
      s += '<circle cx="' + px(i) + '" cy="' + py(v) + '" r="' + (i === n ? 5 : 2.5) + '" fill="var('
        + (i === n ? '--amber' : '--cyan') + ')" />';
    }
    s += '<line x1="30" y1="' + py(parseFloat(Rfixed(c, 4))) + '" x2="500" y2="'
      + py(parseFloat(Rfixed(c, 4))) + '" stroke="var(--red)" stroke-width="1.5" />'
      + '<text x="500" y="' + (py(parseFloat(Rfixed(c, 4))) - 5)
      + '" text-anchor="end" font-size="10" fill="var(--red)">write-only workload: '
      + Rtext(c) + ' ops/s at every N</text>'
      + '<line x1="30" y1="168" x2="500" y2="168" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="30" y="184" font-size="10" fill="var(--muted)">N = 1</text>'
      + '<text x="500" y="184" text-anchor="end" font-size="10" fill="var(--muted)">N = 12</text>'
      + '<text x="30" y="196" font-size="10" fill="var(--muted)">vertical axis: ops/s the cluster '
      + 'serves at ' + rhoN + ' reads per write</text>';
    plot.innerHTML = s;

    var gainPct = Rdiv(Rsub(plan.total, one.total), one.total);
    var wasted = Rsub(plan.ceiling, plan.speedup);
    status.innerHTML = '<strong>' + n + (n === 1 ? ' replica' : ' replicas')
      + '</strong> at ' + rhoN + ' reads per write serve <strong>' + Rfixed(plan.total, 1)
      + ' ops/s</strong> &mdash; ' + Rfixed(plan.speedup, 4) + '&times; one replica, for '
      + n + '&times; the storage and ' + n + '&times; the write work. '
      + (rhoN === 0
          ? 'At zero reads per write the speed-up is exactly ' + Rtext(plan.speedup)
            + ': a write-only workload gets <span class="tone-red">nothing at all</span> from '
            + 'replication, and pays ' + n + '&times; for it.'
          : 'The ceiling is ' + Rtext(plan.ceiling) + '&times; and it is set by the read/write ratio, '
            + 'not by N: every replica still applies every write, so the writes are the serial part. '
            + 'You are ' + Rfixed(wasted, 4) + '&times; short of it, and the whole remaining fleet '
            + 'cannot close that gap.')
      + ' Reads went up ' + Rpct(gainPct, 1) + ' against one replica; write capacity did not move.';
  }

  [nS, rhoS, capS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Reads scale, writes do not",
        subtitle="Four multipliers, and the read/write ratio that caps the third",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the replication factor"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every figure is computed from N and the read/write ratio: the read capacity, "
            "the write capacity that does not move, and the ceiling the ratio sets.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - sync
# ---------------------------------------------------------------------------


def _sync(cfg):
    n = int(cfg.get("n", 3))
    spec = str(cfg.get("reply_pmf", _REPLY_PMF))
    write_rate = int(cfg.get("writes_per_sec", 2000))
    write_bytes = int(cfg.get("bytes_per_write", 400))

    markup = (
        _toolbar(
            "A synchronous write waits for the slowest",
            "P(max of N &minus; 1 &le; t) = F(t)<sup>N&minus;1</sup>",
            [("cyan", "one replica"), ("purple", "the maximum of N &minus; 1"),
             ("red", "what N&times; would predict")],
        )
        + _stage(_svg("syPlot", "0 0 520 200",
                      "The per-replica CDF and the CDF of the maximum, with both p99 marks."))
        + _table("syTable")
        + _table("sySweep")
        + _banner("syStatus")
    )
    controls = (
        _text("syPmf", "One replica&rsquo;s ack time, as ms:weight pairs", spec)
        + _range("syN", "Replicas N (one leader, N &minus; 1 followers)", 1, 9, n)
        + _range("syRate", "Write rate (writes/s), for the async alternative", 0, 20000, write_rate, step=100)
        + _range("syBytes", "Bytes per write", 50, 4000, write_bytes, step=50)
        + _kpis(
            [
                ("p99, one replica", "syOne"),
                ("p99, synchronous to N", "syMax"),
                ("N &times; one replica&rsquo;s p99, as claimed", "syNaive"),
                ("Mean wait, exactly", "syMean"),
                ("P(all followers acked by the single-replica p99)", "syAll"),
                ("Async instead: bytes at risk", "syRisk"),
            ]
        )
        + _hint(
            "syHint",
            "The maximum&rsquo;s distribution is F(t)<sup>N&minus;1</sup> evaluated at every "
            "attainable time, so the whole pmf is exact. Synchronising to three replicas does not "
            "cost three times one replica&rsquo;s latency &mdash; it costs whatever the slower of "
            "the two followers costs, and a maximum is not a sum.",
        )
    )

    script = _CORE_JS + r"""
  var pmfIn = document.getElementById('syPmf'), nS = document.getElementById('syN');
  var rateS = document.getElementById('syRate'), byteS = document.getElementById('syBytes');
  var plot = document.getElementById('syPlot'), table = document.getElementById('syTable');
  var sweep = document.getElementById('sySweep'), status = document.getElementById('syStatus');
  var KPIS = ['syOne', 'syMax', 'syNaive', 'syMean', 'syAll', 'syRisk'];

  function redraw() {
    var n = +nS.value, rate = +rateS.value, wb = +byteS.value;
    document.getElementById('syNOut').textContent = n + (n === 1 ? ' (no follower)' : '');
    document.getElementById('syRateOut').textContent = group(rate) + ' writes/s';
    document.getElementById('syBytesOut').textContent = group(wb) + ' B';

    var spec = parsePmfSpec(pmfIn.value), base = spec ? pmfFromSpec(spec) : null;
    if (!base) {
      plot.innerHTML = '';
      table.innerHTML = '';
      sweep.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not a distribution.</span> Type ms:weight '
        + 'pairs, like <span class="tone-muted">2:600, 4:250, 8:120, 16:25, 40:5</span>.';
      return;
    }

    var q99 = R(99n, 100n), q50 = R(1n, 2n);
    var maxPmf = syncAckPmf(base, n);
    var one99 = pmfPercentile(base, q99), max99 = pmfPercentile(maxPmf, q99);
    var naive = naiveSyncCost(base, n, q99);
    var meanWait = pmfMean(maxPmf), meanOne = pmfMean(base);
    var allBy = pmfCdfAt(maxPmf, one99);
    var risk = asyncAtRiskBytes(rate, meanOne, wb);

    document.getElementById('syOne').textContent = one99 + ' ms';
    document.getElementById('syMax').textContent = max99 + ' ms';
    document.getElementById('syNaive').textContent = naive + ' ms';
    document.getElementById('syMean').textContent = Rtext(meanWait) + ' ms = ' + Rfixed(meanWait, 3);
    document.getElementById('syAll').textContent = Rpct(allBy, 3);
    document.getElementById('syRisk').textContent = bytesText(bytesFloor(risk));

    var rows = '', i, cumOne = R(0n, 1n), cumMax = R(0n, 1n);
    var vals = pmfSupport(base);
    for (i = 0; i < vals.length; i += 1) {
      cumOne = pmfCdfAt(base, vals[i]);
      cumMax = pmfCdfAt(maxPmf, vals[i]);
      rows += '<tr><td>' + vals[i] + '</td>'
        + '<td>' + Rtext(base[i][1]) + '</td>'
        + '<td class="tone-cyan">' + Rtext(cumOne) + '</td>'
        + '<td class="tt">(' + Rtext(cumOne) + ')<sup>' + Math.max(0, n - 1) + '</sup></td>'
        + '<td class="tone-purple">' + Rfixed(cumMax, 8) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>t (ms)</th><th>P(one = t)</th><th>F(t)</th>'
      + '<th>F(t) raised to N &minus; 1</th><th>P(max &le; t)</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="5" class="small-copy">Column four is the whole '
      + 'lesson: raising a probability below one to a power drags it down, and the p99 moves to '
      + 'wherever column five first reaches 99/100.</td></tr></tfoot>';

    var srows = '', k;
    for (k = 1; k <= 9; k += 1) {
      var mp = syncAckPmf(base, k);
      srows += '<tr' + (k === n ? ' class="tone-purple"' : '') + '><td>' + k + '</td>'
        + '<td>' + Math.max(0, k - 1) + '</td>'
        + '<td>' + pmfPercentile(mp, q50) + '</td>'
        + '<td>' + pmfPercentile(mp, q99) + '</td>'
        + '<td>' + Rfixed(pmfMean(mp), 3) + '</td>'
        + '<td class="tone-red">' + naiveSyncCost(base, k, q99) + '</td></tr>';
    }
    sweep.innerHTML = '<thead><tr><th>N</th><th>followers waited for</th><th>p50 wait</th>'
      + '<th>p99 wait</th><th>mean wait</th><th>what N&times; would claim</th>'
      + '</tr></thead><tbody>' + srows + '</tbody>';

    var hi = vals[vals.length - 1] || 1;
    function px(t) { return 34 + (t / hi) * 466; }
    function py(p) { return 160 - p * 130; }
    var a = '', b = '', j;
    for (j = 0; j < vals.length; j += 1) {
      var f1 = parseFloat(Rfixed(pmfCdfAt(base, vals[j]), 9));
      var fm = parseFloat(Rfixed(pmfCdfAt(maxPmf, vals[j]), 9));
      a += (j ? ' ' : '') + px(vals[j]) + ',' + py(f1);
      b += (j ? ' ' : '') + px(vals[j]) + ',' + py(fm);
    }
    var s = '<polyline points="' + a + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<polyline points="' + b + '" fill="none" stroke="var(--purple)" stroke-width="2.5" />'
      + '<line x1="34" y1="' + py(0.99) + '" x2="500" y2="' + py(0.99)
      + '" stroke="var(--line-strong)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="34" y="' + (py(0.99) - 4) + '" font-size="10" fill="var(--muted)">99/100</text>'
      + '<line x1="' + px(max99) + '" y1="26" x2="' + px(max99) + '" y2="160" stroke="var(--purple)" '
      + 'stroke-width="2" /><text x="' + Math.min(px(max99) + 5, 330) + '" y="38" font-size="10" '
      + 'fill="var(--purple)" font-weight="700">sync p99 = ' + max99 + ' ms</text>'
      + '<line x1="' + px(one99) + '" y1="26" x2="' + px(one99) + '" y2="160" stroke="var(--cyan)" '
      + 'stroke-width="2" stroke-dasharray="4 3" /><text x="' + Math.min(px(one99) + 5, 330)
      + '" y="54" font-size="10" fill="var(--cyan)">one replica p99 = ' + one99 + ' ms</text>'
      + '<line x1="34" y1="160" x2="500" y2="160" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="34" y="176" font-size="10" fill="var(--muted)">0 ms</text>'
      + '<text x="500" y="176" text-anchor="end" font-size="10" fill="var(--muted)">' + hi + ' ms</text>'
      + '<text x="34" y="192" font-size="10" fill="var(--muted)">cyan: F(t) for one replica. '
      + 'purple: F(t) raised to the power ' + Math.max(0, n - 1) + ', the maximum of the followers.</text>';
    plot.innerHTML = s;

    var over = naive - max99;
    status.innerHTML = (n === 1
      ? 'At <strong>N = 1</strong> there is no follower to wait for, so the synchronous wait is zero '
        + 'and the comparison starts from here. Raise N and watch the purple curve peel away from the '
        + 'cyan one.'
      : 'Synchronising to <strong>' + n + ' replicas</strong> waits for the slowest of '
        + (n - 1) + ' follower' + (n === 2 ? '' : 's') + ': p99 = <strong>' + max99 + ' ms</strong>, '
        + 'against ' + one99 + ' ms for one replica. &ldquo;' + n + ' replicas cost ' + n
        + ' times one replica&rdquo; would predict <span class="tone-red">' + naive + ' ms</span>, '
        + (over > 0 ? 'which is ' + over + ' ms too high &mdash; '
            + Rfixed(R(BigInt(naive), BigInt(max99 || 1)), 2) + ' times the real figure'
          : (over < 0 ? 'which is ' + (-over) + ' ms too LOW' : 'which happens to land on it here'))
        + '. Latencies of independent replicas do not add: the write waits for their MAXIMUM, whose '
        + 'distribution is F(t) raised to the power ' + (n - 1) + ', and raising a number below one '
        + 'to a power is not multiplying it. All ' + (n - 1) + ' followers have acked by '
        + one99 + ' ms with probability ' + Rpct(allBy, 3) + '.')
      + ' The asynchronous alternative waits for nobody and risks the un-replicated tail instead: at '
      + group(rate) + ' writes/s, a mean lag of ' + Rfixed(meanOne, 3) + ' ms and ' + group(wb)
      + ' B a write, that is <strong>' + bytesText(bytesFloor(risk)) + '</strong> on the leader and '
      + 'nowhere else.';
  }

  [nS, rateS, byteS].forEach(function (el) { el.addEventListener('input', redraw); });
  pmfIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Synchronous writes wait for the slowest",
        subtitle="The maximum of N − 1 replicas, enumerated exactly",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the replicas and their reply times"),
        panel_intro=cfg.get(
            "panel_intro",
            "The acknowledged-by distribution is F(t)<sup>N&minus;1</sup> at every attainable "
            "time, computed from the pairs you type. Nothing here is sampled.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - lag
# ---------------------------------------------------------------------------


def _lag(cfg):
    spec = str(cfg.get("lag_pmf", _LAG_PMF))
    delay = int(cfg.get("read_delay_ms", 50))
    rate = int(cfg.get("reads_per_sec", 12000))

    markup = (
        _toolbar(
            "A stale read is the tail, not the mean",
            "P(stale at t) = P(lag &gt; t)",
            [("cyan", "lag within t"), ("red", "stale: lag past t"),
             ("amber", "the mean lag"), ("muted", "the mass the mean hides")],
        )
        + _stage(_svg("lgPlot", "0 0 520 190",
                      "The lag distribution as bars, with the mass past the read delay shaded."))
        + _table("lgTable")
        + _banner("lgStatus")
    )
    controls = (
        _text("lgPmf", "Replication lag, as ms:weight pairs", spec)
        + _range("lgDelay", "Read issued this long after the write (ms)", 0, 500, delay, step=5)
        + _range("lgRate", "Follower reads per second", 0, 50000, rate, step=500)
        + _kpis(
            [
                ("P(stale) at this delay", "lgP"),
                ("Stale reads per second", "lgCount"),
                ("Mean lag", "lgMean"),
                ("P(stale) at the MEAN lag", "lgAtMean"),
                ("Delay for 99% freshness", "lgFresh99"),
                ("Delay for 99.9% freshness", "lgFresh999"),
            ]
        )
        + _hint(
            "lgHint",
            "&ldquo;Average lag is 50 ms, so reads after 50 ms are fresh&rdquo; is the mistake this "
            "panel exists to price. The mean is one number about the middle; staleness is entirely a "
            "statement about the tail, and the two move independently.",
        )
    )

    script = _CORE_JS + r"""
  var pmfIn = document.getElementById('lgPmf'), dS = document.getElementById('lgDelay');
  var rS = document.getElementById('lgRate');
  var plot = document.getElementById('lgPlot'), table = document.getElementById('lgTable');
  var status = document.getElementById('lgStatus');
  var KPIS = ['lgP', 'lgCount', 'lgMean', 'lgAtMean', 'lgFresh99', 'lgFresh999'];

  function redraw() {
    var t = +dS.value, rate = +rS.value;
    document.getElementById('lgDelayOut').textContent = t + ' ms';
    document.getElementById('lgRateOut').textContent = group(rate) + ' reads/s';

    var spec = parsePmfSpec(pmfIn.value), lag = spec ? pmfFromSpec(spec) : null;
    if (!lag) {
      plot.innerHTML = '';
      table.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not a lag distribution.</span> Type '
        + 'ms:weight pairs, like <span class="tone-muted">10:500, 25:300, 50:120, 120:60, 400:20</span>.';
      return;
    }

    var stale = staleProb(lag, t);
    var perSec = staleReadsPerSec(lag, t, rate);
    var mean = pmfMean(lag);
    var atMean = tailPastRational(lag, mean);
    var f99 = freshDelay(lag, R(99n, 100n)), f999 = freshDelay(lag, R(999n, 1000n));

    document.getElementById('lgP').textContent = Rtext(stale) + ' = ' + Rpct(stale, 3);
    document.getElementById('lgCount').textContent = Rfixed(perSec, 1) + ' reads/s';
    document.getElementById('lgMean').textContent = Rtext(mean) + ' ms = ' + Rfixed(mean, 2);
    document.getElementById('lgAtMean').textContent = Rpct(atMean, 3);
    document.getElementById('lgFresh99').textContent = f99 + ' ms';
    document.getElementById('lgFresh999').textContent = f999 + ' ms';

    var rows = '', i, vals = pmfSupport(lag);
    for (i = 0; i < vals.length; i += 1) {
      var past = vals[i] > t;
      rows += '<tr class="' + (past ? 'tone-red' : 'tone-cyan') + '"><td>' + vals[i] + '</td>'
        + '<td>' + Rtext(lag[i][1]) + '</td>'
        + '<td>' + Rfixed(lag[i][1], 5) + '</td>'
        + '<td>' + Rtext(pmfCdfAt(lag, vals[i])) + '</td>'
        + '<td>' + Rtext(pmfTail(lag, vals[i])) + '</td>'
        + '<td>' + (past ? 'stale at a ' + t + ' ms read' : 'fresh') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>lag (ms)</th><th>probability</th><th>decimal</th>'
      + '<th>P(lag &le; this)</th><th>P(lag &gt; this)</th><th>at t = ' + t + ' ms</th>'
      + '</tr></thead><tbody>' + rows + '</tbody><tfoot><tr><td colspan="6" class="small-copy">'
      + 'P(stale) is the sum of the red rows&rsquo; probabilities and nothing else. The mean, '
      + Rtext(mean) + ' ms, appears nowhere in that sum.</td></tr></tfoot>';

    /* The axis has to cover the read delay as well as the distribution: the
       slider runs past the longest lag, and a marker drawn outside the viewBox
       is a marker the reader never sees. */
    var hi = Math.max(vals[vals.length - 1] || 1, t, 1), maxP = 0, j;
    for (j = 0; j < lag.length; j += 1) {
      var v = parseFloat(Rfixed(lag[j][1], 9));
      if (v > maxP) maxP = v;
    }
    if (!maxP) maxP = 1;
    function px(x) { return 30 + (x / hi) * 470; }
    var s = '';
    for (j = 0; j < lag.length; j += 1) {
      var h = (parseFloat(Rfixed(lag[j][1], 9)) / maxP) * 108;
      var stalebar = lag[j][0] > t;
      s += '<rect x="' + (px(lag[j][0]) - 5) + '" y="' + (146 - h) + '" width="10" height="'
        + Math.max(2, h) + '" rx="2" fill="var(' + (stalebar ? '--red' : '--cyan') + ')" opacity="0.9" />'
        + '<text x="' + px(lag[j][0]) + '" y="160" font-size="9" text-anchor="middle" fill="var(--muted)">'
        + lag[j][0] + '</text>';
    }
    var mx = px(parseFloat(Rfixed(mean, 6)));
    s += '<line x1="' + px(t) + '" y1="22" x2="' + px(t) + '" y2="146" stroke="var(--red)" '
      + 'stroke-width="2" /><text x="' + Math.min(px(t) + 5, 300) + '" y="34" font-size="10" '
      + 'fill="var(--red)" font-weight="700">read at ' + t + ' ms &rarr; ' + Rpct(stale, 2) + ' stale</text>'
      + '<line x1="' + mx + '" y1="22" x2="' + mx + '" y2="146" stroke="var(--amber)" '
      + 'stroke-width="1.5" stroke-dasharray="4 3" /><text x="' + Math.min(mx + 5, 300)
      + '" y="50" font-size="10" fill="var(--amber)">mean = ' + Rfixed(mean, 1) + ' ms &rarr; '
      + Rpct(atMean, 2) + ' still stale</text>'
      + '<line x1="30" y1="146" x2="500" y2="146" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="30" y="176" font-size="10" fill="var(--muted)">bar heights are exact '
      + 'probabilities; the red ones are the reads that see the old value</text>'
      + '<text x="30" y="188" font-size="10" fill="var(--muted)">horizontal axis: lag in '
      + 'milliseconds, to ' + hi + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A read issued <strong>' + t + ' ms</strong> after the write is stale with '
      + 'probability <strong>' + Rtext(stale) + '</strong> = ' + Rpct(stale, 3) + ', which at '
      + group(rate) + ' follower reads a second is <strong>' + Rfixed(perSec, 0)
      + ' stale reads every second</strong>. The mean lag is ' + Rtext(mean) + ' ms &mdash; and '
      + 'waiting for the mean leaves <span class="tone-amber">' + Rpct(atMean, 2)
      + '</span> of reads stale, because half the distribution is not the whole of it. '
      + 'Read-your-writes needs ' + f999 + ' ms to fail one read in a thousand here, and '
      + (Rcmp(stale, R(0n, 1n)) === 0
          ? 'at ' + t + ' ms every read is already fresh: the delay is past the longest lag in '
            + 'the distribution.'
          : 'monotonic reads fail on exactly this mass whenever a reader is moved between '
            + 'followers.');
  }

  [dS, rS].forEach(function (el) { el.addEventListener('input', redraw); });
  pmfIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Replication lag and stale reads",
        subtitle="P(stale) is the tail past the read delay, and the mean cannot see it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the lag and the read delay"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tail mass is summed exactly from the pairs you type, and the reads-per-second "
            "figure is that fraction of your read rate.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - quorum
# ---------------------------------------------------------------------------


def _quorum(cfg):
    n = int(cfg.get("n", 3))
    r = int(cfg.get("r", 2))
    w = int(cfg.get("w", 2))

    markup = (
        _toolbar(
            "Quorums overlap when R + W &gt; N",
            "and the minimum overlap is R + W &minus; N, by the pigeonhole principle",
            [("amber", "the write set"), ("cyan", "the read set"),
             ("green", "nodes in both"), ("red", "a disjoint pair")],
        )
        + _stage(_svg("qmGrid", "0 0 520 210",
                      "The N nodes with a write set and a read set marked, and their intersection."))
        + _table("qmTable")
        + _banner("qmStatus")
    )
    controls = (
        _range("qmN", "Replicas N", 1, 9, n)
        + _range("qmR", "Read quorum R", 1, 9, r)
        + _range("qmW", "Write quorum W", 1, 9, w)
        + _kpis(
            [
                ("R + W vs N", "qmSum"),
                ("Minimum overlap, claimed", "qmClaim"),
                ("Minimum overlap, over every pair", "qmMin"),
                ("Read sets &times; write sets", "qmPairs"),
                ("Pairs that miss entirely", "qmDisjoint"),
                ("C(N&minus;W, R) &times; C(N, W)", "qmFormula"),
            ]
        )
        + _hint(
            "qmHint",
            "Every C(N, R) read set is checked against every C(N, W) write set, so the minimum "
            "below is measured rather than argued. Overlap makes a read <em>able</em> to see the "
            "latest acknowledged write. It does not make the system linearizable &mdash; that "
            "needs an order on the operations, and it is lesson 12&rsquo;s business.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('qmN'), rS = document.getElementById('qmR');
  var wS = document.getElementById('qmW');
  var grid = document.getElementById('qmGrid'), table = document.getElementById('qmTable');
  var status = document.getElementById('qmStatus');

  function nodeName(i) { return String.fromCharCode(65 + i); }
  function setText(list) {
    var out = [], i;
    for (i = 0; i < list.length; i += 1) out.push(nodeName(list[i]));
    return '{' + out.join(', ') + '}';
  }

  function redraw() {
    var n = +nS.value, r = Math.min(+rS.value, n), w = Math.min(+wS.value, n);
    document.getElementById('qmNOut').textContent = n;
    document.getElementById('qmROut').textContent = r + (r === +rS.value ? '' : ' (capped at N)');
    document.getElementById('qmWOut').textContent = w + (w === +wS.value ? '' : ' (capped at N)');

    var scan = quorumScan(n, r, w);
    var claimed = quorumOverlap(n, r, w);
    var overlaps = quorumOverlaps(n, r, w);
    var formula = disjointPairCount(n, r, w);

    document.getElementById('qmSum').textContent = r + ' + ' + w + ' = ' + (r + w)
      + (overlaps ? ' > ' : (r + w === n ? ' = ' : ' < ')) + n;
    document.getElementById('qmClaim').textContent = (overlaps ? claimed : 0)
      + (overlaps ? ' node' + (claimed === 1 ? '' : 's') : ' — no guarantee');
    document.getElementById('qmMin').textContent = scan.min + ' node' + (scan.min === 1 ? '' : 's');
    document.getElementById('qmPairs').textContent = group(scan.readSets.length) + ' × '
      + group(scan.writeSets.length) + ' = ' + group(scan.pairs);
    document.getElementById('qmDisjoint').textContent = group(scan.disjoint);
    document.getElementById('qmFormula').textContent = group(comb(n - w, r)) + ' × '
      + group(comb(n, w)) + ' = ' + group(formula);

    /* The witness pair when one exists, otherwise the tightest pair -- which
       is the pair that attains the minimum the pigeonhole argument predicts. */
    var showW = scan.witness ? scan.witness.write : (scan.writeSets[0] || []);
    var showR = scan.witness ? scan.witness.read : null;
    if (!showR) {
      var bestGap = n + 1, i;
      for (i = 0; i < scan.readSets.length; i += 1) {
        var o = overlapSize(showW, scan.readSets[i]);
        if (o < bestGap) { bestGap = o; showR = scan.readSets[i]; }
      }
      if (!showR) showR = [];
    }

    var rows = '', k, shown = 0;
    for (k = 0; k < scan.writeSets.length && shown < 8; k += 1) {
      var wset = scan.writeSets[k], worst = null, worstO = n + 1, j;
      for (j = 0; j < scan.readSets.length; j += 1) {
        var oo = overlapSize(wset, scan.readSets[j]);
        if (oo < worstO) { worstO = oo; worst = scan.readSets[j]; }
      }
      rows += '<tr' + (worstO === 0 ? ' class="tone-red"' : '') + '><td class="tone-amber">'
        + setText(wset) + '</td><td class="tone-cyan">' + setText(worst || []) + '</td>'
        + '<td>' + worstO + '</td>'
        + '<td>' + (worstO === 0 ? 'the read sees none of this write'
                                 : 'they share ' + setText(intersect(wset, worst || []))) + '</td></tr>';
      shown += 1;
    }
    table.innerHTML = '<thead><tr><th>write set</th><th>its worst read set</th>'
      + '<th>overlap</th><th></th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="4" class="small-copy">'
      + (scan.writeSets.length > 8 ? 'The first 8 of ' + group(scan.writeSets.length)
           + ' write sets; ' : 'All ' + group(scan.writeSets.length) + ' write sets; ')
      + 'each row is paired with whichever of the ' + group(scan.readSets.length)
      + ' read sets shares the least with it.</td></tr></tfoot>';

    var cell = Math.min(52, Math.floor(460 / Math.max(n, 1)));
    var startX = 30, s = '';
    s += '<text x="30" y="18" font-size="11" fill="var(--muted)">the ' + n + ' replicas</text>';
    for (k = 0; k < n; k += 1) {
      var inW = showW.indexOf(k) >= 0, inR = showR.indexOf(k) >= 0;
      var fill = inW && inR ? '--green' : (inW ? '--amber' : (inR ? '--cyan' : '--line-strong'));
      var x = startX + k * (cell + 6);
      s += '<rect x="' + x + '" y="28" width="' + cell + '" height="' + cell + '" rx="6" fill="var('
        + fill + ')" opacity="' + (inW || inR ? '0.9' : '0.35') + '" />'
        + '<text x="' + (x + cell / 2) + '" y="' + (28 + cell / 2 + 5) + '" font-size="14" '
        + 'text-anchor="middle" fill="var(--on-accent)" font-weight="700">' + nodeName(k) + '</text>';
    }
    s += '<text x="30" y="' + (44 + cell) + '" font-size="11" fill="var(--amber)">write set W = '
      + setText(showW) + '</text>'
      + '<text x="30" y="' + (60 + cell) + '" font-size="11" fill="var(--cyan)">read set R = '
      + setText(showR) + '</text>'
      + '<text x="30" y="' + (76 + cell) + '" font-size="11" fill="var('
      + (overlapSize(showW, showR) ? '--green' : '--red') + ')" font-weight="700">'
      + (overlapSize(showW, showR)
          ? 'they share ' + setText(intersect(showW, showR)) + ' — the read can see the write'
          : 'they share NOTHING — this read cannot see that write')
      + '</text>'
      + '<text x="30" y="' + (98 + cell) + '" font-size="10" fill="var(--muted)">'
      + (overlaps
          ? 'R + W = ' + (r + w) + ' > N = ' + n + ', so every pair shares at least '
            + claimed + ' node. The picture above is the tightest pair there is.'
          : 'R + W = ' + (r + w) + ' ' + (r + w === n ? '=' : '<') + ' N = ' + n
            + ', so a disjoint pair exists and the picture above is one of ' + group(scan.disjoint) + '.')
      + '</text>'
      + '<text x="30" y="' + (116 + cell) + '" font-size="10" fill="var(--muted)">'
      + 'Overlap says a read CAN see the newest acknowledged write. Lesson 12 is about whether the '
      + 'operations have an order at all.</text>';
    grid.innerHTML = s;

    var agree = scan.disjoint === Number(formula);
    status.innerHTML = 'With <strong>N = ' + n + ', R = ' + r + ', W = ' + w + '</strong>, R + W '
      + (overlaps ? '&gt;' : (r + w === n ? '=' : '&lt;')) + ' N, so '
      + (overlaps
          ? 'every read set meets every write set in at least <strong>' + claimed
            + '</strong> node' + (claimed === 1 ? '' : 's') + '. The scan over all '
            + group(scan.pairs) + ' pairs finds a minimum of ' + scan.min + ', which is the same '
            + 'number: the pigeonhole bound is attained, not merely respected.'
          : '<span class="tone-red">' + group(scan.disjoint) + ' of the ' + group(scan.pairs)
            + ' pairs share nothing at all</span> and one of them is drawn above. A read at this '
            + 'configuration can be served entirely by replicas that never saw the write.')
      + ' The enumeration and the formula C(N&minus;W, R)&times;C(N, W) '
      + (agree ? 'agree exactly: ' + group(scan.disjoint) + ' disjoint pairs each way.'
               : '<span class="tone-red">disagree, which means this page is wrong.</span>')
      + ' <span class="tone-purple">Overlap is not linearizability.</span> It guarantees the read '
      + 'TOUCHES a replica that holds the newest acknowledged write; it does not order two '
      + 'concurrent writes, and it does not stop a read that started later from returning an older '
      + 'value than one that started earlier. That is lesson 12, and it is a different and harder '
      + 'question than this one.';
  }

  function intersect(a, b) {
    var out = [], i;
    for (i = 0; i < a.length; i += 1) if (b.indexOf(a[i]) >= 0) out.push(a[i]);
    return out;
  }

  [nS, rS, wS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Quorums overlap",
        subtitle="R + W > N, the minimum R + W − N, and the pair that misses when it does not",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the quorum configuration"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both set families are enumerated and every pair is compared, so the minimum overlap "
            "shown is measured against the bound rather than asserted from it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - quorumlat
# ---------------------------------------------------------------------------


def _quorumlat(cfg):
    n = int(cfg.get("n", 3))
    w = int(cfg.get("w", 2))
    spec = str(cfg.get("reply_pmf", _REPLY_PMF))

    markup = (
        _toolbar(
            "A quorum waits for the W-th fastest",
            "P(ack by t) = P(at least W of N replied by t) &mdash; a binomial tail",
            [("cyan", "P(ack by t) at this N"), ("muted", "the other N"),
             ("purple", "the p99"), ("green", "larger N, sooner")],
        )
        + _stage(_svg("qlCurve", "0 0 520 200",
                      "P(quorum acked by t) for several fleet sizes at a fixed W."))
        + _table("qlTable")
        + _table("qlSweep")
        + _banner("qlStatus")
    )
    controls = (
        _text("qlPmf", "One replica&rsquo;s reply time, as ms:weight pairs", spec)
        + _range("qlN", "Replicas asked, N", 1, 9, n)
        + _range("qlW", "Replies waited for, W", 1, 9, w)
        + _kpis(
            [
                ("Quorum p99 at this N", "qlP99"),
                ("p99 if you asked one more replica", "qlNext"),
                ("p99 waiting for ALL N", "qlAll"),
                ("P(quorum by the one-replica p50)", "qlByP50"),
                ("Extra replies bought", "qlSlack"),
                ("Binomial terms summed", "qlTerms"),
            ]
        )
        + _hint(
            "qlHint",
            "The tail is availKofN &mdash; the same sum course 5 uses for a k-of-n availability, at "
            "success probability F(t). Watch the p99 column as N rises with W held still: more "
            "replicas give the quorum more chances to be met early, so the write gets faster.",
        )
    )

    script = _CORE_JS + r"""
  var pmfIn = document.getElementById('qlPmf'), nS = document.getElementById('qlN');
  var wS = document.getElementById('qlW');
  var curve = document.getElementById('qlCurve'), table = document.getElementById('qlTable');
  var sweep = document.getElementById('qlSweep'), status = document.getElementById('qlStatus');
  var KPIS = ['qlP99', 'qlNext', 'qlAll', 'qlByP50', 'qlSlack', 'qlTerms'];

  function redraw() {
    var n = +nS.value, w = Math.min(+wS.value, n);
    document.getElementById('qlNOut').textContent = n;
    document.getElementById('qlWOut').textContent = w + (w === +wS.value ? '' : ' (capped at N)');

    var spec = parsePmfSpec(pmfIn.value), base = spec ? pmfFromSpec(spec) : null;
    if (!base) {
      curve.innerHTML = '';
      table.innerHTML = '';
      sweep.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not a distribution.</span> Type ms:weight '
        + 'pairs, like <span class="tone-muted">2:600, 4:250, 8:120, 16:25, 40:5</span>.';
      return;
    }

    var q99 = R(99n, 100n), q50 = R(1n, 2n);
    var here = quorumPercentile(base, w, n, q99);
    var next = quorumPercentile(base, w, n + 1, q99);
    var all = quorumPercentile(base, n, n, q99);
    var p50one = pmfPercentile(base, q50);
    var byP50 = quorumAckBy(base, p50one, w, n);

    document.getElementById('qlP99').textContent = (here === null ? 'never' : here + ' ms');
    document.getElementById('qlNext').textContent = (next === null ? 'never' : next + ' ms')
      + ' (N = ' + (n + 1) + ')';
    document.getElementById('qlAll').textContent = (all === null ? 'never' : all + ' ms');
    document.getElementById('qlByP50').textContent = Rpct(byP50, 3);
    document.getElementById('qlSlack').textContent = (n - w) + ' of ' + n + ' may be slow or dead';
    document.getElementById('qlTerms').textContent = (n - w + 1) + ' term'
      + (n - w + 1 === 1 ? '' : 's') + ', j = ' + w + ' to ' + n;

    var vals = pmfSupport(base), rows = '', i;
    for (i = 0; i < vals.length; i += 1) {
      var f = pmfCdfAt(base, vals[i]);
      var pq = quorumAckBy(base, vals[i], w, n);
      var first = Rcmp(pq, q99) >= 0 && (i === 0 || Rcmp(quorumAckBy(base, vals[i - 1], w, n), q99) < 0);
      rows += '<tr' + (first ? ' class="tone-purple"' : '') + '><td>' + vals[i] + '</td>'
        + '<td>' + Rtext(f) + '</td>'
        + '<td>' + Rfixed(pq, 8) + '</td>'
        + '<td>' + Rfixed(quorumAckBy(base, vals[i], n, n), 8) + '</td>'
        + '<td>' + (first ? 'first to reach 99/100' : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>t (ms)</th><th>F(t), one replica</th>'
      + '<th>P(&ge; ' + w + ' of ' + n + ' by t)</th><th>P(all ' + n + ' by t)</th><th></th>'
      + '</tr></thead><tbody>' + rows + '</tbody><tfoot><tr><td colspan="5" class="small-copy">'
      + 'Column three is availKofN(F(t), ' + w + ', ' + n + '): the binomial tail, summed exactly '
      + 'over BigInt coefficients. Column four is the same sum at k = n, which is what a write '
      + 'that waits for everybody pays.</td></tr></tfoot>';

    var srows = '', k, prevP = null;
    for (k = w; k <= 9; k += 1) {
      var p = quorumPercentile(base, w, k, q99);
      var move = prevP === null ? '&mdash;'
        : (p === null ? 'never' : (p < prevP ? '<span class="tone-green">' + (prevP - p)
            + ' ms faster</span>' : (p > prevP ? (p - prevP) + ' ms slower' : 'unchanged')));
      srows += '<tr' + (k === n ? ' class="tone-cyan"' : '') + '><td>' + k + '</td>'
        + '<td>' + w + '</td><td>' + (k - w) + '</td>'
        + '<td>' + (p === null ? 'never' : p + ' ms') + '</td>'
        + '<td>' + move + '</td></tr>';
      prevP = p;
    }
    sweep.innerHTML = '<thead><tr><th>N</th><th>W</th><th>replies you do not wait for</th>'
      + '<th>quorum p99</th><th>against the row above</th></tr></thead><tbody>' + srows
      + '</tbody><tfoot><tr><td colspan="5" class="small-copy">W is held at ' + w
      + ' down the whole column. Nothing about a replica changed; only how many there are to '
      + 'race.</td></tr></tfoot>';

    var hi = vals[vals.length - 1] || 1;
    function px(t) { return 34 + (t / hi) * 466; }
    function py(p) { return 162 - p * 132; }
    var s = '', kk;
    for (kk = w; kk <= 9; kk += 1) {
      var pts = [], j;
      for (j = 0; j < vals.length; j += 1) {
        pts.push(px(vals[j]) + ',' + py(parseFloat(Rfixed(quorumAckBy(base, vals[j], w, kk), 9))));
      }
      s += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var('
        + (kk === n ? '--cyan' : '--line-strong') + ')" stroke-width="' + (kk === n ? 2.8 : 1.2)
        + '" opacity="' + (kk === n ? 1 : 0.55) + '" />';
    }
    s += '<line x1="34" y1="' + py(0.99) + '" x2="500" y2="' + py(0.99) + '" stroke="var(--muted)" '
      + 'stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="34" y="' + (py(0.99) - 4) + '" font-size="10" fill="var(--muted)">99/100</text>';
    if (here !== null) {
      s += '<line x1="' + px(here) + '" y1="24" x2="' + px(here) + '" y2="162" stroke="var(--purple)" '
        + 'stroke-width="2" /><text x="' + Math.min(px(here) + 5, 320) + '" y="36" font-size="10" '
        + 'fill="var(--purple)" font-weight="700">p99 at N = ' + n + ' is ' + here + ' ms</text>';
    }
    if (next !== null && next !== here) {
      s += '<line x1="' + px(next) + '" y1="24" x2="' + px(next) + '" y2="162" stroke="var(--green)" '
        + 'stroke-width="2" stroke-dasharray="4 3" /><text x="' + Math.min(px(next) + 5, 320)
        + '" y="52" font-size="10" fill="var(--green)">p99 at N = ' + (n + 1) + ' is ' + next + ' ms</text>';
    }
    s += '<line x1="34" y1="162" x2="500" y2="162" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="34" y="178" font-size="10" fill="var(--muted)">0 ms</text>'
      + '<text x="500" y="178" text-anchor="end" font-size="10" fill="var(--muted)">' + hi + ' ms</text>'
      + '<text x="34" y="194" font-size="10" fill="var(--muted)">one curve per N from ' + w
      + ' to 9, W held at ' + w + '. Higher curves are larger fleets.</text>';
    curve.innerHTML = s;

    var faster = next !== null && here !== null && next < here;
    status.innerHTML = 'Waiting for <strong>' + w + ' of ' + n + '</strong> replies gives a p99 of '
      + '<strong>' + (here === null ? 'never — the quorum cannot be met' : here + ' ms') + '</strong>, '
      + 'against ' + (all === null ? 'never' : all + ' ms') + ' if the write waited for all ' + n + '. '
      + (faster
          ? '<span class="tone-green">Asking one more replica makes the write FASTER</span>: at N = '
            + (n + 1) + ' the same W = ' + w + ' quorum has a p99 of ' + next + ' ms, '
            + (here - next) + ' ms better. Nothing about any replica changed. The tail gained a term '
            + '&mdash; there are more ways for ' + w + ' of ' + (n + 1) + ' to be quick than for '
            + w + ' of ' + n + ' &mdash; and a sum of more non-negative terms is larger.'
          : (next !== null && here !== null && next === here
              ? 'At N = ' + (n + 1) + ' the p99 is the same ' + next + ' ms: the tail did rise, but '
                + 'not far enough to cross 99/100 at an earlier attainable time. It never falls.'
              : 'Raise N with W held still and watch the column: the tail can only rise.'))
      + ' The quorum is met by the one-replica median, ' + p50one + ' ms, with probability '
      + Rpct(byP50, 3) + ', and it tolerates ' + (n - w) + ' slow or dead replica'
      + (n - w === 1 ? '' : 's') + ' at no latency cost at all.';
  }

  [nS, wS].forEach(function (el) { el.addEventListener('input', redraw); });
  pmfIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Quorum latency: the W-th fastest",
        subtitle="A binomial tail, and why more replicas make a fixed-W write faster",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the quorum and the reply times"),
        panel_intro=cfg.get(
            "panel_intro",
            "P(ack by t) is availKofN at success probability F(t): the same binomial tail as a "
            "k-of-n availability, summed exactly. Sweep N before reading the verdict.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - sloppy
# ---------------------------------------------------------------------------


def _sloppy(cfg):
    n = int(cfg.get("n", 3))
    r = int(cfg.get("r", 1))
    w = int(cfg.get("w", 1))

    markup = (
        _toolbar(
            "A sloppy quorum misses",
            "P(miss) = C(N &minus; W, R) &divide; C(N, R)",
            [("red", "read sets that miss the write"), ("green", "read sets that hit it"),
             ("purple", "the overlapping configuration")],
        )
        + _stage(_svg("spBars", "0 0 520 200",
                      "Miss probability against the read quorum size, with the overlap threshold marked."))
        + _table("spTable")
        + _banner("spStatus")
    )
    controls = (
        _range("spN", "Replicas N", 1, 9, n)
        + _range("spR", "Read quorum R", 1, 9, r)
        + _range("spW", "Write quorum W", 1, 9, w)
        + _kpis(
            [
                ("Read sets that miss", "spMissSets"),
                ("Read sets in total", "spAllSets"),
                ("P(miss), exactly", "spMiss"),
                ("P(hit)", "spHit"),
                ("Smallest R that always hits", "spNeed"),
                ("P(miss) at R + W = N", "spEdge"),
            ]
        )
        + _hint(
            "spHint",
            "The write landed on some W of the N. A read draws R of the N, and it misses the write "
            "entirely when every one of those R comes from the N &minus; W the write never touched. "
            "Both counts are combinations, so the probability is an exact fraction.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('spN'), rS = document.getElementById('spR');
  var wS = document.getElementById('spW');
  var bars = document.getElementById('spBars'), table = document.getElementById('spTable');
  var status = document.getElementById('spStatus');

  function redraw() {
    var n = +nS.value, r = Math.min(+rS.value, n), w = Math.min(+wS.value, n);
    document.getElementById('spNOut').textContent = n;
    document.getElementById('spROut').textContent = r + (r === +rS.value ? '' : ' (capped at N)');
    document.getElementById('spWOut').textContent = w + (w === +wS.value ? '' : ' (capped at N)');

    var miss = sloppyMiss(n, r, w), hit = sloppyHit(n, r, w);
    var need = n - w + 1;
    var edgeR = Math.max(1, Math.min(n, n - w));
    var edge = sloppyMiss(n, edgeR, w);

    document.getElementById('spMissSets').textContent = 'C(' + (n - w) + ', ' + r + ') = '
      + group(comb(n - w, r));
    document.getElementById('spAllSets').textContent = 'C(' + n + ', ' + r + ') = '
      + group(comb(n, r));
    document.getElementById('spMiss').textContent = (miss === null ? '—'
      : Rtext(miss) + ' = ' + Rpct(miss, 3));
    document.getElementById('spHit').textContent = (hit === null ? '—' : Rpct(hit, 3));
    document.getElementById('spNeed').textContent = (need <= n ? 'R = ' + need + ' (R + W = ' + (need + w)
      + ' > ' + n + ')' : 'impossible at W = ' + w);
    document.getElementById('spEdge').textContent = (edge === null ? '—'
      : 'R = ' + edgeR + ': ' + Rtext(edge) + ' = ' + Rpct(edge, 2));

    var rows = '', k;
    for (k = 1; k <= n; k += 1) {
      var m = sloppyMiss(n, k, w), over = k + w > n;
      rows += '<tr class="' + (over ? 'tone-green' : 'tone-red') + '"'
        + (k === r ? ' style="font-weight:700;"' : '') + '><td>' + k + '</td>'
        + '<td>' + (k + w) + (over ? ' &gt; ' : (k + w === n ? ' = ' : ' &lt; ')) + n + '</td>'
        + '<td>' + group(comb(n - w, k)) + '</td>'
        + '<td>' + group(comb(n, k)) + '</td>'
        + '<td>' + (m === null ? '—' : Rtext(m)) + '</td>'
        + '<td>' + (m === null ? '—' : Rpct(m, 4)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>R</th><th>R + W vs N</th><th>C(N&minus;W, R)</th>'
      + '<th>C(N, R)</th><th>P(miss)</th><th>as a percentage</th></tr></thead><tbody>' + rows
      + '</tbody><tfoot><tr><td colspan="6" class="small-copy">The green rows are the configurations '
      + 'that overlap. Notice how far the last red row is from zero: R + W = N is not nearly as good '
      + 'as R + W &gt; N, it is a different guarantee &mdash; namely none.</td></tr></tfoot>';

    var bw = 460 / Math.max(n, 1), s = '', k2;
    for (k2 = 1; k2 <= n; k2 += 1) {
      var mm = sloppyMiss(n, k2, w);
      var v = mm === null ? 0 : parseFloat(Rfixed(mm, 9));
      var h = v * 120;
      var x = 34 + (k2 - 1) * bw;
      var over2 = k2 + w > n;
      s += '<rect x="' + (x + 3) + '" y="' + (152 - h) + '" width="' + (bw - 6) + '" height="'
        + Math.max(2, h) + '" rx="3" fill="var(' + (over2 ? '--green' : '--red') + ')" opacity="'
        + (k2 === r ? '1' : '0.55') + '" />'
        + '<text x="' + (x + bw / 2) + '" y="166" font-size="10" text-anchor="middle" fill="var(--muted)">R='
        + k2 + '</text>'
        + '<text x="' + (x + bw / 2) + '" y="' + (146 - h) + '" font-size="9" text-anchor="middle" '
        + 'fill="var(--muted)">' + (mm === null ? '' : Rtext(mm)) + '</text>';
    }
    var cutR = n - w + 1;
    if (cutR >= 1 && cutR <= n) {
      var cx = 34 + (cutR - 1) * bw;
      s += '<line x1="' + cx + '" y1="24" x2="' + cx + '" y2="152" stroke="var(--purple)" '
        + 'stroke-width="1.5" stroke-dasharray="4 3" />'
        + '<text x="' + (cx + 4) + '" y="36" font-size="10" fill="var(--purple)">R + W &gt; N from here</text>';
    }
    s += '<line x1="34" y1="152" x2="500" y2="152" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="34" y="184" font-size="10" fill="var(--muted)">bar height is P(miss) on a scale of '
      + '0 to 1, with the exact fraction printed above each bar</text>'
      + '<text x="34" y="196" font-size="10" fill="var(--muted)">W is held at ' + w
      + '; only the read quorum moves</text>';
    bars.innerHTML = s;

    var famous = (n === 3 && r === 1 && w === 1);
    status.innerHTML = 'At <strong>N = ' + n + ', R = ' + r + ', W = ' + w + '</strong> a read misses '
      + 'the write with probability <strong>' + (miss === null ? '—' : Rtext(miss)) + '</strong>'
      + (miss === null ? '' : ' = ' + Rpct(miss, 3))
      + (famous ? ' &mdash; two reads in three, which is the number the lesson quotes and it is exact, '
                + 'not a rule of thumb.' : '.')
      + ' ' + group(comb(n - w, r)) + ' of the ' + group(comb(n, r)) + ' possible read sets are drawn '
      + 'entirely from the ' + (n - w) + ' replica' + (n - w === 1 ? '' : 's') + ' the write never '
      + 'reached. ' + (r + w > n
          ? '<span class="tone-green">This configuration overlaps</span>, so that count is zero and '
            + 'the read is guaranteed to touch the write.'
          : (r + w === n
              ? '<span class="tone-red">R + W = N is not almost enough.</span> One more node in either '
                + 'quorum takes the miss probability to exactly zero; here it is ' + Rpct(miss, 3)
                + '. There is no gradual approach to safety &mdash; the guarantee is a threshold.'
              : 'Raising R to ' + need + ' or W to ' + (n - r + 1) + ' takes this to zero.'))
      + ' A sloppy quorum trades this probability for write availability during a partition: the '
      + 'write is accepted by whichever nodes are reachable, and the price is the fraction above.';
  }

  [nS, rS, wS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Sloppy quorums and the miss probability",
        subtitle="C(N − W, R) ÷ C(N, R), and why R + W = N buys nothing",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the sloppy configuration"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both combinations are computed in BigInt and their ratio is reduced to lowest terms, "
            "so the miss probability on this page is an exact fraction.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - majority
# ---------------------------------------------------------------------------

_NODE_AVAIL = [
    ("9/10", "90% &mdash; one nine"),
    ("99/100", "99% &mdash; two nines"),
    ("995/1000", "99.5%"),
    ("999/1000", "99.9% &mdash; three nines"),
    ("9999/10000", "99.99% &mdash; four nines"),
]


def _majority(cfg):
    n = int(cfg.get("n", 3))
    each = str(cfg.get("each", "99/100"))

    markup = (
        _toolbar(
            "2f + 1 tolerates f",
            "so a fourth node tolerates what three did, and is available less often",
            [("green", "odd sizes, which earn their node"), ("red", "even sizes, which do not"),
             ("cyan", "the majority's availability")],
        )
        + _stage(_svg("mjPlot", "0 0 520 200",
                      "Fault tolerance and majority availability against cluster size, with even sizes marked."))
        + _table("mjTable")
        + _banner("mjStatus")
    )
    controls = (
        _range("mjN", "Cluster size n", 1, 12, n)
        + _select("mjEach", "Each node&rsquo;s availability", _NODE_AVAIL, each)
        + _kpis(
            [
                ("Majority size", "mjQuorum"),
                ("Failures tolerated, f", "mjF"),
                ("Same f as", "mjSame"),
                ("Availability of the majority", "mjAvail"),
                ("Nines", "mjNines"),
                ("Against n &minus; 1", "mjDelta"),
            ]
        )
        + _hint(
            "mjHint",
            "The availability is the k-of-n binomial tail of course 5, at k = the majority. Read the "
            "table down the even rows: each of them tolerates exactly what the odd row above it "
            "tolerates, and is available <em>less</em> often, because the majority grew by one and "
            "the fleet grew by one too.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('mjN'), eachSel = document.getElementById('mjEach');
  var plot = document.getElementById('mjPlot'), table = document.getElementById('mjTable');
  var status = document.getElementById('mjStatus');

  function redraw() {
    var n = +nS.value;
    document.getElementById('mjNOut').textContent = n + (n === 1 ? ' node' : ' nodes');
    var a = Rparse(eachSel.value);

    var q = majoritySize(n), f = faultsTolerated(n), av = majorityAvail(a, n);
    var prev = n > 1 ? majorityAvail(a, n - 1) : null;

    document.getElementById('mjQuorum').textContent = q + ' of ' + n;
    document.getElementById('mjF').textContent = f + ' failure' + (f === 1 ? '' : 's');
    document.getElementById('mjSame').textContent = (evenIsWasted(n)
      ? 'n = ' + (n - 1) + ', which is one node cheaper'
      : (n < 12 ? 'n = ' + (n + 1) + ', which is one node dearer' : 'nothing smaller'));
    document.getElementById('mjAvail').textContent = RpctAuto(av);
    document.getElementById('mjNines').textContent = ninesOf(av) + ' nines';
    document.getElementById('mjDelta').textContent = (prev === null ? '—'
      : (Rcmp(av, prev) > 0 ? 'better' : (Rcmp(av, prev) < 0 ? 'WORSE' : 'identical'))
        + ' than ' + (n - 1) + ' nodes');

    var rows = '', k, before = null;
    for (k = 1; k <= 12; k += 1) {
      var kq = majoritySize(k), kf = faultsTolerated(k), ka = majorityAvail(a, k);
      var move = before === null ? '&mdash;'
        : (Rcmp(ka, before) > 0 ? '<span class="tone-green">better</span>'
            : (Rcmp(ka, before) < 0 ? '<span class="tone-red">worse</span>' : 'identical'));
      rows += '<tr class="' + (evenIsWasted(k) ? 'tone-red' : 'tone-green') + '"'
        + (k === n ? ' style="font-weight:700;"' : '') + '><td>' + k + '</td>'
        + '<td>' + kq + '</td><td>' + kf + '</td>'
        + '<td>' + RpctAuto(ka) + '</td>'
        + '<td>' + move + '</td>'
        + '<td>' + (evenIsWasted(k) ? 'wasted: f is ' + kf + ' at n = ' + (k - 1) + ' too' : '') + '</td></tr>';
      before = ka;
    }
    table.innerHTML = '<thead><tr><th>n</th><th>majority</th><th>f</th>'
      + '<th>availability of the majority</th><th>vs n &minus; 1</th><th></th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="6" class="small-copy">Every availability is the sum '
      + 'of the binomial terms from j = the majority to j = n, over exact fractions at A = '
      + Rtext(a) + '. Column three is floor((n &minus; 1)/2) and it is flat across every even step.'
      + '</td></tr></tfoot>';

    var bw = 460 / 12, s = '', maxF = 5;
    for (k = 1; k <= 12; k += 1) {
      var x = 34 + (k - 1) * bw;
      var kf2 = faultsTolerated(k);
      var h = (kf2 / maxF) * 92;
      s += '<rect x="' + (x + 3) + '" y="' + (126 - h) + '" width="' + (bw - 6) + '" height="'
        + Math.max(2, h) + '" rx="3" fill="var(' + (evenIsWasted(k) ? '--red' : '--green')
        + ')" opacity="' + (k === n ? '1' : '0.5') + '" />'
        + '<text x="' + (x + bw / 2) + '" y="140" font-size="10" text-anchor="middle" fill="var(--muted)">'
        + k + '</text>';
    }
    var pts = [], lo = 1, hi2 = 0;
    for (k = 1; k <= 12; k += 1) {
      var v = parseFloat(Rfixed(majorityAvail(a, k), 9));
      if (v < lo) lo = v;
      if (v > hi2) hi2 = v;
    }
    var span = (hi2 - lo) || 1;
    for (k = 1; k <= 12; k += 1) {
      var v2 = parseFloat(Rfixed(majorityAvail(a, k), 9));
      pts.push((34 + (k - 1) * bw + bw / 2) + ',' + (110 - ((v2 - lo) / span) * 86));
    }
    s += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2" />';
    for (k = 1; k <= 12; k += 1) {
      var v3 = parseFloat(Rfixed(majorityAvail(a, k), 9));
      s += '<circle cx="' + (34 + (k - 1) * bw + bw / 2) + '" cy="' + (110 - ((v3 - lo) / span) * 86)
        + '" r="' + (k === n ? 4.5 : 2.5) + '" fill="var(--cyan)" />';
    }
    s += '<text x="34" y="18" font-size="10" fill="var(--muted)">bars: failures tolerated. '
      + 'line: availability of the majority, stretched to fill the panel.</text>'
      + '<line x1="34" y1="126" x2="500" y2="126" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="34" y="158" font-size="10" fill="var(--red)">every even bar is the same height as '
      + 'the odd bar to its left &mdash; that node bought no tolerance</text>'
      + '<text x="34" y="172" font-size="10" fill="var(--cyan)">and the line DROPS at every even n, '
      + 'because the majority grew from ' + Math.floor(n / 2) + ' to ' + q + ' while each node is '
      + 'still only ' + Rpct(a, 2) + ' available</text>'
      + '<text x="34" y="190" font-size="10" fill="var(--muted)">cluster size n, 1 to 12</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A <strong>' + n + '-node</strong> cluster needs <strong>' + q
      + '</strong> for a majority, so it tolerates <strong>' + f + '</strong> failure'
      + (f === 1 ? '' : 's') + ' and its majority is available ' + RpctAuto(av) + ' of the time at '
      + Rpct(a, 2) + ' per node. '
      + (evenIsWasted(n)
          ? '<span class="tone-red">The ' + n + 'th node bought nothing.</span> ' + (n - 1)
            + ' nodes tolerate the same ' + f + ' failure' + (f === 1 ? '' : 's') + ', and their '
            + 'majority is available ' + RpctAuto(majorityAvail(a, n - 1)) + ' &mdash; '
            + (Rcmp(av, majorityAvail(a, n - 1)) < 0 ? 'BETTER than this one' : 'no worse')
            + '. An even cluster pays for a node and raises the bar it has to clear.'
          : 'Adding one more node would make it ' + (n + 1) + ', whose majority is ' + (q + 1)
            + ' &mdash; the same f = ' + f + ' for one more machine, and an availability of '
            + RpctAuto(majorityAvail(a, n + 1)) + '. Go to ' + (n + 2) + ' instead and f becomes '
            + faultsTolerated(n + 2) + '.')
      + ' Tolerance moves in steps of one for every TWO nodes, because a majority has to be more '
      + 'than half and half of n + 1 is more than half of n.';
  }

  nS.addEventListener('input', redraw);
  eachSel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Majorities and fault tolerance",
        subtitle="f = floor((n − 1)/2), and the availability of the quorum that follows",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Sweep the cluster size"),
        panel_intro=cfg.get(
            "panel_intro",
            "Tolerance is an integer computed from n; the availability beside it is the k-of-n "
            "binomial tail at k = the majority, summed over exact fractions.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - election
# ---------------------------------------------------------------------------


def _election(cfg):
    n = int(cfg.get("candidates", 5))
    slots = int(cfg.get("slots", 10))

    markup = (
        _toolbar(
            "Randomised election timeouts",
            "P(clean) = &Sigma;<sub>j</sub> n(1/T)((T &minus; j)/T)<sup>n&minus;1</sup>",
            [("cyan", "the term at each slot"), ("purple", "the sum"),
             ("red", "the split vote")],
        )
        + _stage(_svg("elBars", "0 0 520 200",
                      "One bar per slot for the probability that the earliest candidate is unique there."))
        + _table("elTable")
        + _banner("elStatus")
    )
    controls = (
        _range("elN", "Candidates n", 1, 12, n)
        + _range("elT", "Timeout slots T", 1, 40, slots)
        + _kpis(
            [
                ("P(clean election)", "elP"),
                ("P(split vote)", "elSplit"),
                ("Expected rounds", "elRounds"),
                ("Terms in the sum", "elTerms"),
                ("At a FIXED timeout (T = 1)", "elFixed"),
                ("Slots to reach 95% clean", "elNeed"),
            ]
        )
        + _hint(
            "elHint",
            "Pick the candidate that fires first (n ways), pick its slot (probability 1/T), and "
            "require the other n &minus; 1 to land strictly later. At T = 1 the last factor is zero "
            "for every term, which is the arithmetic saying that a fixed timeout is a guaranteed tie.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('elN'), tS = document.getElementById('elT');
  var bars = document.getElementById('elBars'), table = document.getElementById('elTable');
  var status = document.getElementById('elStatus');

  function redraw() {
    var n = +nS.value, T = +tS.value;
    document.getElementById('elNOut').textContent = n + (n === 1 ? ' candidate' : ' candidates');
    document.getElementById('elTOut').textContent = T + (T === 1 ? ' slot (fixed!)' : ' slots');

    var p = electionClean(n, T), rounds = electionRounds(n, T);
    var split = Rsub(R(1n, 1n), p);
    var fixed = electionClean(n, 1);
    var need = slotsForClean(n, R(95n, 100n), 400);

    document.getElementById('elP').textContent = Rfixed(p, 6) + ' = ' + Rpct(p, 3);
    document.getElementById('elSplit').textContent = Rpct(split, 3);
    document.getElementById('elRounds').textContent = (rounds === null
      ? 'never terminates' : Rfixed(rounds, 4) + ' rounds');
    document.getElementById('elTerms').textContent = T + ' term' + (T === 1 ? '' : 's')
      + ', j = 1 to ' + T;
    document.getElementById('elFixed').textContent = Rtext(fixed)
      + (Rzero(fixed) ? ' — always a tie' : ' — the single candidate wins');
    document.getElementById('elNeed').textContent = (need === null ? 'more than 400' : need + ' slots');

    var rows = '', j, run = R(0n, 1n), elided = false;
    for (j = 1; j <= T; j += 1) {
      var term = electionTerm(n, T, j);
      run = Radd(run, term);
      if (T <= 14 || j <= 8 || j > T - 3) {
        rows += '<tr' + (Rzero(term) ? ' class="tone-muted"' : '') + '><td>' + j + '</td>'
          + '<td class="tt">' + n + ' &times; (1/' + T + ') &times; (' + (T - j) + '/' + T + ')<sup>'
          + (n - 1) + '</sup></td>'
          + '<td>' + Rtext(term) + '</td>'
          + '<td>' + Rfixed(term, 6) + '</td>'
          + '<td>' + Rfixed(run, 6) + '</td></tr>';
      } else if (!elided) {
        elided = true;
        rows += '<tr class="tone-muted"><td colspan="5">&hellip; ' + (T - 11)
          + ' more terms, not listed here but summed in full &mdash; every one of them '
          + 'exactly</td></tr>';
      }
    }
    table.innerHTML = '<thead><tr><th>slot j</th><th>term</th><th>exact</th><th>decimal</th>'
      + '<th>running sum</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">The last term is always zero: a candidate '
      + 'firing in the final slot cannot have everyone else fire later. The sum is '
      + Rtext(p) + ', and its reciprocal is the expected number of rounds.</td></tr></tfoot>';

    var maxT = 0, vals = [];
    for (j = 1; j <= T; j += 1) {
      var v = parseFloat(Rfixed(electionTerm(n, T, j), 9));
      vals.push(v);
      if (v > maxT) maxT = v;
    }
    if (!maxT) maxT = 1;
    var bw = 466 / Math.max(T, 1), s = '';
    for (j = 0; j < T; j += 1) {
      var h = (vals[j] / maxT) * 106;
      var x = 34 + j * bw;
      s += '<rect x="' + (x + Math.min(2, bw / 6)) + '" y="' + (144 - h) + '" width="'
        + Math.max(1, bw - Math.min(4, bw / 3)) + '" height="' + Math.max(1, h)
        + '" rx="2" fill="var(--cyan)" opacity="0.85" />';
      if (T <= 20) {
        s += '<text x="' + (x + bw / 2) + '" y="158" font-size="9" text-anchor="middle" '
          + 'fill="var(--muted)">' + (j + 1) + '</text>';
      }
    }
    var frac = parseFloat(Rfixed(p, 9));
    s += '<rect x="34" y="176" width="466" height="10" rx="5" fill="var(--red)" opacity="0.35" />'
      + '<rect x="34" y="176" width="' + (466 * Math.min(1, frac)) + '" height="10" rx="5" '
      + 'fill="var(--purple)" />'
      + '<text x="34" y="171" font-size="10" fill="var(--muted)">'
      + 'each bar is the probability the earliest candidate is unique and fires in that slot</text>'
      + '<text x="34" y="196" font-size="10" fill="var(--purple)">purple: P(clean) = '
      + Rpct(p, 2) + '. red: the split vote, ' + Rpct(split, 2) + ', which costs another round.</text>'
      + '<text x="34" y="18" font-size="10" fill="var(--muted)">' + n + ' candidates over ' + T
      + ' slot' + (T === 1 ? '' : 's') + '</text>'
      + '<line x1="34" y1="144" x2="500" y2="144" stroke="var(--line-strong)" stroke-width="1" />';
    bars.innerHTML = s;

    status.innerHTML = (T === 1
      ? '<span class="tone-red">A fixed timeout is T = 1</span>, and every term in the sum carries '
        + 'a factor of ((T &minus; j)/T)<sup>n&minus;1</sup> = 0<sup>' + (n - 1) + '</sup>. So '
        + 'P(clean) = ' + Rtext(p) + ': with ' + n + ' candidate' + (n === 1 ? '' : 's')
        + ' they all fire together, split the vote, and do it again next round. '
        + (n === 1 ? 'The single-candidate case is the exception: with nobody to tie against, it wins.'
                   : 'This is why the timeout is randomised, and the arithmetic says so without '
                     + 'any appeal to intuition.')
      : '<strong>' + n + ' candidates</strong> over <strong>' + T + ' slots</strong> elect a leader '
        + 'in one round with probability <strong>' + Rtext(p) + '</strong> = ' + Rpct(p, 3)
        + ', so the expected number of rounds is 1/P = <strong>'
        + (rounds === null ? '&infin;' : Rfixed(rounds, 4)) + '</strong>. '
        + 'The split vote costs ' + Rpct(split, 3) + ' of elections a second round &mdash; and the '
        + 'rounds are independent, so the expectation is the geometric 1/P and not something '
        + 'larger.')
      + ' Widening the window to ' + (need === null ? 'more than 400' : need)
      + ' slots would make nineteen elections in twenty clean; it also makes every election that '
      + 'much slower to start, which is the trade the timeout range is choosing.';
  }

  [nS, tS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Randomised election timeouts",
        subtitle="The probability of a clean first round, and the rounds it takes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the candidates and the window"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every term is computed as an exact fraction and listed before it is summed, so the "
            "probability on this page can be checked slot by slot.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The space-time diagram L9 and L10 share.
#
# One drawing routine, two callers, because the lessons are meant to be the
# same picture stamped two ways -- and a reader who has to re-read the diagram
# on L10 is reading a different lesson than the one L9 set up. It is emitted
# into each mode's script as a string so that neither mode reaches into the
# other's ids: L9 draws lamport stamps and L10 draws vectors, and the caller
# passes the label for each event.
# ---------------------------------------------------------------------------

_DIAGRAM_JS = r"""
  /* Draw the diagram: one lane per process, a dot per event with `label(i)`
     printed above it, and an arrow per message. 660 wide, which is one of the
     three widths theme.py gives a horizontal-scroll minimum -- a space-time
     diagram with four lanes cannot be read at 520 on a phone, and a width the
     stylesheet does not know about shrinks to illegibility instead of
     scrolling. */
  function drawDiagram(d, events, label, markIds, markTone) {
    var lanes = d.procs.length, i;
    var laneH = 46, top = 30, left = 64, right = 640;
    var maxCount = 1;
    for (i = 0; i < lanes; i += 1) if (d.procs[i].count > maxCount) maxCount = d.procs[i].count;
    var step = (right - left) / (maxCount + 1);
    var s = '';
    for (i = 0; i < lanes; i += 1) {
      var y = top + i * laneH;
      s += '<line x1="' + left + '" y1="' + y + '" x2="' + right + '" y2="' + y
        + '" stroke="var(--line-strong)" stroke-width="1.5" />'
        + '<text x="' + (left - 12) + '" y="' + (y + 4) + '" text-anchor="end" font-size="13" '
        + 'fill="var(--text)" font-weight="700">' + d.procs[i].name + '</text>';
    }
    function ex(e) { return left + (events[e].index + 1) * step; }
    function ey(e) { return top + events[e].proc * laneH; }
    for (i = 0; i < d.msgs.length; i += 1) {
      var from = -1, to = -1, k;
      for (k = 0; k < events.length; k += 1) {
        if (events[k].proc === d.msgs[i].from && events[k].index === d.msgs[i].fromEvent) from = k;
        if (events[k].proc === d.msgs[i].to && events[k].index === d.msgs[i].toEvent) to = k;
      }
      if (from < 0 || to < 0) continue;
      s += '<line x1="' + ex(from) + '" y1="' + ey(from) + '" x2="' + ex(to) + '" y2="' + ey(to)
        + '" stroke="var(--amber)" stroke-width="1.6" opacity="0.9" />'
        + '<circle cx="' + ex(to) + '" cy="' + ey(to) + '" r="3.5" fill="var(--amber)" />';
    }
    for (i = 0; i < events.length; i += 1) {
      var marked = markIds && markIds.indexOf(i) >= 0;
      s += '<circle cx="' + ex(i) + '" cy="' + ey(i) + '" r="' + (marked ? 7 : 5) + '" fill="var('
        + (marked ? markTone : '--cyan') + ')" />'
        + '<text x="' + ex(i) + '" y="' + (ey(i) - 12) + '" text-anchor="middle" font-size="11" '
        + 'fill="var(' + (marked ? markTone : '--text') + ')" font-weight="700">' + label(i) + '</text>'
        + '<text x="' + ex(i) + '" y="' + (ey(i) + 18) + '" text-anchor="middle" font-size="9" '
        + 'fill="var(--muted)">' + events[i].name + '</text>';
    }
    return s;
  }
"""


# ---------------------------------------------------------------------------
# L9 - lamport
# ---------------------------------------------------------------------------


def _lamport(cfg):
    spec = str(cfg.get("diagram", _DIAGRAM))

    markup = (
        _toolbar(
            "Lamport clocks",
            "L(e) = max(L<sub>local</sub>, L<sub>msg</sub>) + 1",
            [("cyan", "an event, with its stamp"), ("amber", "a message"),
             ("red", "L(a) &lt; L(b) with a NOT before b")],
        )
        + _stage(_svg("lpDiag", "0 0 660 220",
                      "A space-time diagram with each event's Lamport stamp printed above it."))
        + _table("lpTable")
        + _banner("lpStatus")
    )
    controls = (
        _text("lpSpec", "The diagram: processes, then messages", spec)
        + _kpis(
            [
                ("Events", "lpEvents"),
                ("Messages", "lpMsgs"),
                ("Largest stamp", "lpMax"),
                ("Pairs where L decides correctly", "lpTrue"),
                ("Pairs where L decides WRONGLY", "lpFalse"),
                ("Does a&rarr;b imply L(a) &lt; L(b)?", "lpSound"),
            ]
        )
        + _hint(
            "lpHint",
            "Write <span class=\"tt\">A:4 B:4 C:3</span> for three processes with that many local "
            "events, then a message per clause as <span class=\"tt\">A2 to B2</span> &mdash; sent at "
            "A&rsquo;s second event, delivered at B&rsquo;s second. The stamps propagate along "
            "exactly those two kinds of edge and nothing else.",
        )
    )

    script = _CORE_JS + _DIAGRAM_JS + r"""
  var specIn = document.getElementById('lpSpec');
  var diag = document.getElementById('lpDiag'), table = document.getElementById('lpTable');
  var status = document.getElementById('lpStatus');
  var KPIS = ['lpEvents', 'lpMsgs', 'lpMax', 'lpTrue', 'lpFalse', 'lpSound'];

  function redraw() {
    var d = parseDiagram(specIn.value);
    var L = d ? lamportStamps(d) : null;
    var V = d ? vectorStamps(d) : null;
    if (!d || !L || !V) {
      diag.innerHTML = '';
      table.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not a diagram.</span> Processes first, as '
        + '<span class="tone-muted">A:4 B:4 C:3</span>, then one message per clause, as '
        + '<span class="tone-muted">A2 to B2</span>. Each event may send or receive at most once, '
        + 'and a message may not be received before it was sent.';
      return;
    }

    var events = diagramEvents(d), i, j;
    var wrong = lamportFalsePairs(L, V);
    var sound = lamportConsistent(L, V);
    var maxL = 0;
    for (i = 0; i < L.length; i += 1) if (L[i] > maxL) maxL = L[i];

    var decided = 0;
    for (i = 0; i < L.length; i += 1) {
      for (j = 0; j < L.length; j += 1) {
        if (i === j) continue;
        if (L[i] < L[j] && vecCompare(V[i], V[j]) === -1) decided += 1;
      }
    }

    document.getElementById('lpEvents').textContent = events.length;
    document.getElementById('lpMsgs').textContent = d.msgs.length;
    document.getElementById('lpMax').textContent = maxL;
    document.getElementById('lpTrue').textContent = decided + ' ordered pair'
      + (decided === 1 ? '' : 's');
    document.getElementById('lpFalse').textContent = wrong.length + ' ordered pair'
      + (wrong.length === 1 ? '' : 's');
    document.getElementById('lpSound').textContent = sound ? 'yes, on every pair here'
      : 'NO — this page is wrong';

    var marks = [];
    if (wrong.length) { marks = [wrong[0][0], wrong[0][1]]; }
    diag.innerHTML = drawDiagram(d, events, function (i2) { return L[i2]; }, marks, '--red')
      + '<text x="64" y="212" font-size="10" fill="var(--muted)">the number above each event is its '
      + 'Lamport stamp; the number below is the event&rsquo;s name</text>';

    var rows = '';
    for (i = 0; i < events.length; i += 1) {
      var prevL = events[i].index > 0 ? L[i - 1] : 0;
      var msgL = events[i].recv >= 0 ? L[events[i].recv] : null;
      rows += '<tr' + (marks.indexOf(i) >= 0 ? ' class="tone-red"' : '') + '><td>' + events[i].name
        + '</td><td>' + (events[i].index > 0 ? events[i - 1].name + ' = ' + prevL : 'nothing, 0')
        + '</td><td>' + (msgL === null ? '&mdash;'
            : events[events[i].recv].name + ' = ' + msgL)
        + '</td><td class="tt">max(' + prevL + ', ' + (msgL === null ? 0 : msgL) + ') + 1</td>'
        + '<td>' + L[i] + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>event</th><th>previous on this process</th>'
      + '<th>message received</th><th>rule</th><th>L</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">Every stamp is the maximum of those two '
      + 'inputs plus one. Nothing else can raise a clock, which is exactly why the stamps carry '
      + 'happens-before forward and cannot carry it back.</td></tr></tfoot>';

    var firstA = wrong.length ? events[wrong[0][0]].name : null;
    var firstB = wrong.length ? events[wrong[0][1]].name : null;
    status.innerHTML = 'The ' + events.length + ' events carry stamps 1 to ' + maxL + ', and on '
      + decided + ' ordered pair' + (decided === 1 ? '' : 's') + ' the stamps really do report the '
      + 'causal order: ' + (sound
          ? 'every pair where a happens before b has L(a) &lt; L(b), checked over all '
            + (L.length * (L.length - 1)) + ' ordered pairs.'
          : '<span class="tone-red">a pair violates it, which means this page is wrong.</span>')
      + ' <strong>The converse fails.</strong> '
      + (wrong.length
          ? 'There ' + (wrong.length === 1 ? 'is ' : 'are ') + wrong.length + ' ordered pair'
            + (wrong.length === 1 ? '' : 's') + ' with L(a) &lt; L(b) where a did NOT happen before b '
            + '&mdash; the first is <span class="tone-red">' + firstA + ' (L = '
            + L[wrong[0][0]] + ') and ' + firstB + ' (L = ' + L[wrong[0][1]] + ')</span>, marked in '
            + 'the diagram. They are concurrent: no chain of process edges and messages joins them '
            + 'in either direction. A smaller stamp means nothing on its own, and a system that '
            + 'resolved a conflict by comparing Lamport stamps would pick a winner between these '
            + 'two for no reason at all. Lesson 10 is the clock that can tell.'
          : 'On THIS diagram there happens to be no such pair &mdash; every pair of events is '
            + 'causally ordered, so the total order the stamps give is the causal order. Add a '
            + 'process, or remove a message, and the counterexample appears: the property is a '
            + 'fact about this diagram, not about Lamport clocks.');
  }

  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Lamport clocks",
        subtitle="A total order consistent with happens-before — and only one way round",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the message diagram"),
        panel_intro=cfg.get(
            "panel_intro",
            "The stamps are propagated along the diagram you type, in a topological order of the "
            "events, by the rule and nothing else.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - vector
# ---------------------------------------------------------------------------


def _vector(cfg):
    spec = str(cfg.get("diagram", _DIAGRAM))

    markup = (
        _toolbar(
            "Vector clocks and concurrency",
            "incomparable means concurrent, and the concurrent pairs are the conflicts",
            [("cyan", "an event, with its vector"), ("amber", "a message"),
             ("purple", "a concurrent pair")],
        )
        + _stage(_svg("vcDiag", "0 0 660 220",
                      "The same space-time diagram with each event's vector timestamp printed above it."))
        + _table("vcTable")
        + _table("vcPairs")
        + _banner("vcStatus")
    )
    controls = (
        _text("vcSpec", "The diagram: processes, then messages", spec)
        + _kpis(
            [
                ("Events", "vcEvents"),
                ("Pairs in total", "vcAll"),
                ("Ordered pairs", "vcOrdered"),
                ("Concurrent pairs", "vcConc"),
                ("Concurrent share", "vcShare"),
                ("Widest concurrent pair", "vcWidest"),
            ]
        )
        + _hint(
            "vcHint",
            "A vector is one counter per process. Comparing two of them elementwise gives three "
            "answers and a fourth: a &le; b, b &le; a, equal &mdash; or neither, which is what "
            "concurrent means. Concurrent is not simultaneous: two events a minute apart on the "
            "clock can be concurrent, and two at the same instant can be ordered.",
        )
    )

    script = _CORE_JS + _DIAGRAM_JS + r"""
  var specIn = document.getElementById('vcSpec');
  var diag = document.getElementById('vcDiag'), table = document.getElementById('vcTable');
  var pairsT = document.getElementById('vcPairs'), status = document.getElementById('vcStatus');
  var KPIS = ['vcEvents', 'vcAll', 'vcOrdered', 'vcConc', 'vcShare', 'vcWidest'];

  function vecText(v) { return '(' + v.join(', ') + ')'; }

  function redraw() {
    var d = parseDiagram(specIn.value);
    var V = d ? vectorStamps(d) : null;
    var L = d ? lamportStamps(d) : null;
    if (!d || !V || !L) {
      diag.innerHTML = '';
      table.innerHTML = '';
      pairsT.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not a diagram.</span> Processes first, as '
        + '<span class="tone-muted">A:4 B:4 C:3</span>, then one message per clause, as '
        + '<span class="tone-muted">A2 to B2</span>. Each event may send or receive at most once.';
      return;
    }

    var events = diagramEvents(d), i, j;
    var conc = concurrentPairs(V);
    var total = (events.length * (events.length - 1)) / 2;
    var share = total ? R(BigInt(conc.length), BigInt(total)) : R(0n, 1n);

    var widest = null, widestGap = -1;
    for (i = 0; i < conc.length; i += 1) {
      var gap = Math.abs(L[conc[i][0]] - L[conc[i][1]]);
      if (gap > widestGap) { widestGap = gap; widest = conc[i]; }
    }

    document.getElementById('vcEvents').textContent = events.length;
    document.getElementById('vcAll').textContent = total + ' unordered pair'
      + (total === 1 ? '' : 's');
    document.getElementById('vcOrdered').textContent = (total - conc.length);
    document.getElementById('vcConc').textContent = conc.length;
    document.getElementById('vcShare').textContent = Rtext(share) + ' = ' + Rpct(share, 1);
    document.getElementById('vcWidest').textContent = (widest === null ? 'none'
      : events[widest[0]].name + ' and ' + events[widest[1]].name + ', Lamport stamps '
        + widestGap + ' apart');

    var marks = widest === null ? [] : [widest[0], widest[1]];
    diag.innerHTML = drawDiagram(d, events, function (i2) { return vecText(V[i2]); }, marks, '--purple')
      + '<text x="64" y="212" font-size="10" fill="var(--muted)">the vector above each event counts '
      + 'events per process in the order ' + d.procs.map(function (p) { return p.name; }).join(', ')
      + '</text>';

    var rows = '';
    for (i = 0; i < events.length; i += 1) {
      var prevV = events[i].index > 0 ? vecText(V[i - 1]) : 'all zero';
      var msgV = events[i].recv >= 0 ? vecText(V[events[i].recv]) : '&mdash;';
      rows += '<tr' + (marks.indexOf(i) >= 0 ? ' class="tone-purple"' : '') + '><td>'
        + events[i].name + '</td><td>' + prevV + '</td><td>' + msgV + '</td>'
        + '<td>' + vecText(V[i]) + '</td><td>' + L[i] + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>event</th><th>previous on this process</th>'
      + '<th>message received</th><th>vector</th><th>Lamport, for comparison</th>'
      + '</tr></thead><tbody>' + rows + '</tbody><tfoot><tr><td colspan="5" class="small-copy">'
      + 'Elementwise maximum of the two inputs, then add one to this process&rsquo;s own component. '
      + 'The Lamport column is one number and cannot express what the vector expresses.'
      + '</td></tr></tfoot>';

    var prow = '';
    if (!conc.length) {
      prow = '<tr><td colspan="4">No concurrent pair: every pair of events on this diagram is '
        + 'causally ordered.</td></tr>';
    } else {
      for (i = 0; i < conc.length && i < 24; i += 1) {
        var a = conc[i][0], b = conc[i][1];
        prow += '<tr' + (widest && a === widest[0] && b === widest[1] ? ' class="tone-purple"' : '')
          + '><td>' + events[a].name + ' ' + vecText(V[a]) + '</td>'
          + '<td>' + events[b].name + ' ' + vecText(V[b]) + '</td>'
          + '<td>' + whyConcurrent(V[a], V[b], d) + '</td>'
          + '<td>' + L[a] + ' vs ' + L[b] + '</td></tr>';
      }
      if (conc.length > 24) {
        prow += '<tr class="tone-muted"><td colspan="4">&hellip; and ' + (conc.length - 24)
          + ' more</td></tr>';
      }
    }
    pairsT.innerHTML = '<thead><tr><th>event</th><th>event</th><th>why neither precedes the other</th>'
      + '<th>Lamport stamps</th></tr></thead><tbody>' + prow + '</tbody><tfoot><tr>'
      + '<td colspan="4" class="small-copy">Each of these is a write that could conflict with the '
      + 'other, and a merge has to decide between them. Lesson 13 counts what each way of deciding '
      + 'throws away.</td></tr></tfoot>';

    status.innerHTML = 'The diagram has ' + events.length + ' events and ' + total
      + ' pairs of them. <strong>' + conc.length + '</strong> '
      + (conc.length === 1 ? 'pair is' : 'pairs are') + ' concurrent &mdash; ' + Rtext(share)
      + ' of them &mdash; and every one is listed above with the component that beats each way. '
      + (conc.length
          ? 'Take ' + events[conc[0][0]].name + ' and ' + events[conc[0][1]].name + ': neither '
            + 'vector dominates the other, so no chain of process steps and messages joins them, so '
            + 'neither happened before the other. Their Lamport stamps are ' + L[conc[0][0]]
            + ' and ' + L[conc[0][1]] + ' &mdash; a single number cannot say "incomparable", which '
            + 'is why lesson 9&rsquo;s clock reported an order that is not there.'
          : 'On this diagram nothing is concurrent, so a Lamport stamp would have been enough. '
            + 'Delete a message and watch the count rise.')
      + ' <span class="tone-purple">Concurrent does not mean simultaneous.</span> It is a statement '
      + 'about reachability in this graph and says nothing about wall-clock time &mdash; which is '
      + 'lesson 11&rsquo;s subject, and a different kind of uncertainty entirely.';
  }

  /* The two components that make the pair incomparable: one where a leads and
     one where b does. Naming them is what turns "incomparable" from a verdict
     into something the reader can check on the row. */
  function whyConcurrent(a, b, d) {
    var ahead = -1, behind = -1, i;
    for (i = 0; i < a.length; i += 1) {
      if (a[i] > b[i] && ahead < 0) ahead = i;
      if (a[i] < b[i] && behind < 0) behind = i;
    }
    if (ahead < 0 || behind < 0) return 'incomparable';
    return d.procs[ahead].name + ' is ahead on the left, ' + d.procs[behind].name
      + ' is ahead on the right';
  }

  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Vector clocks and concurrency",
        subtitle="Happens-before as a partial order, with every incomparable pair listed",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the same message diagram"),
        panel_intro=cfg.get(
            "panel_intro",
            "The vectors propagate along the diagram you type, and every pair is compared "
            "elementwise. The concurrent pairs are the ones a merge will have to decide.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - drift
# ---------------------------------------------------------------------------


def _drift(cfg):
    ppm = int(cfg.get("ppm", 200))
    interval = int(cfg.get("sync_interval_s", 30))
    gap = int(cfg.get("true_gap_us", 5000))

    markup = (
        _toolbar(
            "Physical clocks and drift",
            "&epsilon; = drift &times; sync interval, and the commit-wait is 2&epsilon;",
            [("cyan", "event 1 and its uncertainty"), ("purple", "event 2 and its uncertainty"),
             ("red", "the overlap, where order is undecidable"), ("green", "the commit-wait")],
        )
        + _stage(_svg("drPlot", "0 0 520 200",
                      "Two events on a timeline, each drawn with its clock uncertainty window."))
        + _table("drTable")
        + _banner("drStatus")
    )
    controls = (
        _range("drPpm", "Clock drift (parts per million)", 1, 500, ppm)
        + _range("drSync", "Seconds between corrections", 1, 600, interval)
        + _range("drGap", "True separation of the two events (&micro;s)", 0, 40000, gap, step=250)
        + _kpis(
            [
                ("&epsilon;, one clock&rsquo;s error", "drEps"),
                ("2&epsilon;, the comparison window", "drWin"),
                ("Commit-wait needed", "drWait"),
                ("Window &divide; true separation", "drRatio"),
                ("Is the wall-clock order trustworthy?", "drSafe"),
                ("Throughput cost of the wait", "drCost"),
            ]
        )
        + _hint(
            "drHint",
            "One part per million is one microsecond per second, so the arithmetic is a "
            "multiplication and the units come out exactly. NTP does not make two clocks equal; it "
            "bounds how far apart they can drift before the next correction, and that bound is the "
            "whole of what a timestamp comparison can rely on.",
        )
    )

    script = _CORE_JS + r"""
  var ppmS = document.getElementById('drPpm'), syncS = document.getElementById('drSync');
  var gapS = document.getElementById('drGap');
  var plot = document.getElementById('drPlot'), table = document.getElementById('drTable');
  var status = document.getElementById('drStatus');

  function usText(a) {
    if (Rcmp(a, R(1000n, 1n)) >= 0) return Rfixed(Rdiv(a, R(1000n, 1n)), 3) + ' ms';
    return Rfixed(a, 1) + ' &micro;s';
  }

  function redraw() {
    var ppm = +ppmS.value, iv = +syncS.value, gapUs = +gapS.value;
    document.getElementById('drPpmOut').textContent = ppm + ' ppm';
    document.getElementById('drSyncOut').textContent = iv + ' s';
    document.getElementById('drGapOut').textContent = group(gapUs) + ' &micro;s';

    var eps = skewMicros(ppm, iv), win = commitWaitMicros(ppm, iv);
    var gap = R(BigInt(gapUs), 1n);
    var safe = orderTrustworthy(gap, ppm, iv);
    var ratio = windowRatio(gap, ppm, iv);
    var perSec = Rdiv(R(1000000n, 1n), win);

    document.getElementById('drEps').textContent = usText(eps);
    document.getElementById('drWin').textContent = usText(win);
    document.getElementById('drWait').textContent = usText(win) + ' before releasing a commit';
    document.getElementById('drRatio').textContent = (ratio === null ? 'the events coincide'
      : Rfixed(ratio, 3) + '&times;');
    document.getElementById('drSafe').textContent = safe ? 'yes, the gap clears the window'
      : 'NO — the window covers the gap';
    document.getElementById('drCost').textContent = Rfixed(perSec, 2)
      + ' serialised commits/s at most';

    var rows = '', options = [[10, 1], [10, 60], [50, 10], [50, 60], [100, 30], [200, 30],
                              [200, 60], [500, 300]];
    var i;
    for (i = 0; i < options.length; i += 1) {
      var e2 = skewMicros(options[i][0], options[i][1]);
      var w2 = commitWaitMicros(options[i][0], options[i][1]);
      rows += '<tr' + (options[i][0] === ppm && options[i][1] === iv ? ' class="tone-cyan"' : '')
        + '><td>' + options[i][0] + ' ppm</td><td>' + options[i][1] + ' s</td>'
        + '<td>' + usText(e2) + '</td><td>' + usText(w2) + '</td>'
        + '<td>' + Rfixed(Rdiv(R(1000000n, 1n), w2), 1) + '</td></tr>';
    }
    rows += '<tr class="tone-purple"><td>' + ppm + ' ppm</td><td>' + iv + ' s</td><td>'
      + usText(eps) + '</td><td>' + usText(win) + '</td><td>' + Rfixed(perSec, 1) + '</td></tr>';
    table.innerHTML = '<thead><tr><th>drift</th><th>sync interval</th><th>&epsilon;</th>'
      + '<th>2&epsilon;, the commit-wait</th><th>serialised commits/s</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="5" class="small-copy">Tighter clocks or more '
      + 'frequent corrections shrink the window, and the last column is what that buys: a commit '
      + 'that waits 2&epsilon; can be issued at most 10<sup>6</sup>/2&epsilon; times a second in a '
      + 'serial chain. Nothing here rounds &mdash; ppm is microseconds per second by definition.'
      + '</td></tr></tfoot>';

    /* Event 1 is at zero and its band reaches -epsilon, so the axis starts at
       -epsilon and not at zero -- otherwise the first band is drawn off the
       left-hand edge, where nothing throws and nobody sees it. The right end
       covers the second band and the commit-wait bar. */
    var half = parseFloat(Rfixed(eps, 3)), winPx = parseFloat(Rfixed(win, 3));
    var axLo = -half, axHi = Math.max(gapUs + half, winPx, half, 1);
    function px(us) { return 40 + ((us - axLo) / (axHi - axLo)) * 450; }
    var e1x = px(0), e2x = px(gapUs);
    var s = '';
    s += '<rect x="' + px(-half) + '" y="52" width="' + Math.max(2, px(half) - px(-half))
      + '" height="26" rx="4" fill="var(--cyan)" opacity="0.35" />'
      + '<rect x="' + px(gapUs - half) + '" y="92" width="' + Math.max(2, px(half) - px(-half))
      + '" height="26" rx="4" fill="var(--purple)" opacity="0.35" />'
      + '<line x1="' + e1x + '" y1="46" x2="' + e1x + '" y2="84" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<line x1="' + e2x + '" y1="86" x2="' + e2x + '" y2="124" stroke="var(--purple)" stroke-width="2.5" />'
      + '<text x="' + e1x + '" y="42" text-anchor="middle" font-size="11" fill="var(--cyan)" '
      + 'font-weight="700">event 1</text>'
      + '<text x="' + e2x + '" y="138" text-anchor="middle" font-size="11" fill="var(--purple)" '
      + 'font-weight="700">event 2, ' + group(gapUs) + ' &micro;s later</text>';
    if (!safe) {
      /* Distinct names, because `var` is function-scoped: a second `var lo` in
         here would rewrite the axis origin that px() closes over, and every
         later coordinate on the drawing would be measured from a pixel. */
      var bandLo = Math.max(px(gapUs - half), px(-half));
      var bandHi = Math.min(px(half), px(gapUs + half));
      s += '<rect x="' + bandLo + '" y="52" width="' + Math.max(2, bandHi - bandLo)
        + '" height="66" rx="4" fill="var(--red)" opacity="0.3" />'
        + '<text x="' + ((bandLo + bandHi) / 2) + '" y="152" text-anchor="middle" font-size="10" '
        + 'fill="var(--red)" font-weight="700">the windows overlap: either order is consistent with '
        + 'both clocks</text>';
    } else {
      s += '<text x="' + ((e1x + e2x) / 2) + '" y="152" text-anchor="middle" font-size="10" '
        + 'fill="var(--green)" font-weight="700">the windows are disjoint: the timestamps decide '
        + 'the order correctly</text>';
    }
    s += '<line x1="' + e1x + '" y1="166" x2="' + px(parseFloat(Rfixed(win, 3)))
      + '" y2="166" stroke="var(--green)" stroke-width="3" />'
      + '<text x="' + px(parseFloat(Rfixed(win, 3))) + '" y="180" font-size="10" '
      + 'fill="var(--green)">commit-wait 2&epsilon; = ' + usText(win) + '</text>'
      + '<text x="40" y="196" font-size="10" fill="var(--muted)">shaded bands are &plusmn;&epsilon; '
      + 'around each event: everywhere its timestamp could be, at ' + ppm + ' ppm between '
      + iv + '-second corrections</text>'
      + '<text x="40" y="24" font-size="10" fill="var(--muted)">one timeline, from &minus;&epsilon; to '
      + group(Math.round(axHi)) + ' &micro;s</text>';
    plot.innerHTML = s;

    status.innerHTML = 'At <strong>' + ppm + ' ppm</strong> between corrections <strong>' + iv
      + ' s</strong> apart, one clock can be off by &epsilon; = ' + usText(eps)
      + ', so comparing two of them carries an uncertainty of 2&epsilon; = <strong>' + usText(win)
      + '</strong>. '
      + (safe
          ? 'The two events are ' + group(gapUs) + ' &micro;s apart, which clears that window, so '
            + '<span class="tone-green">their timestamps really do give the right order</span> '
            + '&mdash; but only because the gap happens to be '
            + (ratio === null ? '' : Rfixed(Rinv(ratio), 2) + '&times; the window') + '.'
          : '<span class="tone-red">The two events are only ' + group(gapUs) + ' &micro;s apart, '
            + 'inside that window.</span> Event 2 really happened later, and yet a timestamp '
            + 'comparison can put it first: the windows overlap and nothing on either machine can '
            + 'tell which reading was the honest one. NTP did not fail here &mdash; it is working '
            + 'exactly to specification, and the specification is a bound, not an equality.')
      + ' A commit-wait of 2&epsilon; buys the order back by refusing to release a transaction until '
      + 'its timestamp is certainly in the past. It costs ' + usText(win) + ' of latency on every '
      + 'commit, which caps a serial chain at ' + Rfixed(perSec, 1) + ' commits a second. That is '
      + 'the trade: an uncertainty bound turned into an order, paid for in latency.';
  }

  [ppmS, syncS, gapS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Physical clocks and drift",
        subtitle="ε, the 2ε window, and the order a wall clock cannot decide",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the clock and the two events"),
        panel_intro=cfg.get(
            "panel_intro",
            "Parts per million are microseconds per second, so every figure here is an exact "
            "product. The commit-wait is twice the one-clock error and nothing more.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L12 - linearize
# ---------------------------------------------------------------------------

# Each preset is a history the lesson can point at. The default is the one the
# misconception names: every read returned a value that some replica really
# held, and there is still no order that explains them all.
_HISTORIES = [
    ("A w1[0,4]; B r1[2,6]; C r0[5,9]",
     "the violation: two honest reads, no legal order"),
    ("A w1[0,4]; B r1[2,6]; C r1[5,9]",
     "the same shape, made legal by one return value"),
    ("A w1[0,3]; B w2[1,5]; C r1[4,8]; D r2[6,10]",
     "two concurrent writes, and a read of each"),
    ("A w1[0,2]; B r1[1,4]; C w2[3,6]; D r2[5,8]; E r2[7,10]; F r2[9,12]",
     "six operations: the cap, and 720 orders"),
    ("A w1[0,2]; B r1[1,4]; C w2[3,6]; D r2[5,8]; E r2[7,10]; F r2[9,12]; G r2[11,14]",
     "seven operations: refused, with the reason"),
]


def _linearize(cfg):
    history = str(cfg.get("history", _HISTORIES[0][0]))
    initial = int(cfg.get("initial", 0))

    markup = (
        _toolbar(
            "Linearizability by enumeration",
            "count the total orders that real time allows and a register would accept",
            [("cyan", "an operation&rsquo;s interval"), ("green", "a legal order"),
             ("red", "no legal order exists"), ("purple", "the search space")],
        )
        + _stage(_svg("lzPlot", "0 0 660 250",
                      "Each operation drawn as an interval on a real-time axis, with one legal order marked."))
        + _table("lzTable")
        + _table("lzOrders")
        + _banner("lzStatus")
    )
    controls = (
        _select("lzPreset", "A history to start from",
                [(h, t) for h, t in _HISTORIES], history)
        + _text("lzSpec", "The history, one operation per clause: client, w or r, value, [invoked, returned]", history)
        + _range("lzInit", "The register&rsquo;s initial value", 0, 4, initial)
        + _kpis(
            [
                ("Operations", "lzOps"),
                ("Total orders, k!", "lzTotal"),
                ("Orders real time allows", "lzRt"),
                ("Of those, legal for a register", "lzValid"),
                ("Verdict", "lzVerdict"),
                ("Concurrent pairs", "lzConc"),
            ]
        )
        + _hint(
            "lzHint",
            "An operation is written <span class=\"tt\">B r1[2,6]</span>: client B read the value 1, "
            "invoked at 2 and returned at 6. Two operations whose intervals overlap may be ordered "
            "either way; one that returned before another was invoked may not. The count below is "
            "over every order, not a sample.",
        )
    )

    script = _CORE_JS + r"""
  var preset = document.getElementById('lzPreset'), specIn = document.getElementById('lzSpec');
  var initS = document.getElementById('lzInit');
  var plot = document.getElementById('lzPlot'), table = document.getElementById('lzTable');
  var orders = document.getElementById('lzOrders'), status = document.getElementById('lzStatus');
  var KPIS = ['lzOps', 'lzTotal', 'lzRt', 'lzValid', 'lzVerdict', 'lzConc'];

  function blank(message) {
    plot.innerHTML = '';
    table.innerHTML = '';
    orders.innerHTML = '';
    KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
    status.innerHTML = message;
  }

  function redraw() {
    var initial = +initS.value;
    document.getElementById('lzInitOut').textContent = initial;

    var ops = parseHistory(specIn.value);
    if (!ops) {
      blank('<span class="tone-red">That is not a history.</span> Each operation is '
        + '<span class="tone-muted">A w1[0,4]</span> or <span class="tone-muted">B r1[2,6]</span>: '
        + 'a client letter, w or r, the value, and the interval it was in flight, with the return '
        + 'strictly after the invocation. Separate the operations with semicolons &mdash; the '
        + 'comma is inside the interval.');
      return;
    }
    if (ops.length > 6) {
      document.getElementById('lzOps').textContent = ops.length;
      document.getElementById('lzTotal').textContent = group(fact(ops.length)) + ' orders';
      ['lzRt', 'lzValid', 'lzVerdict', 'lzConc'].forEach(function (id) {
        document.getElementById(id).textContent = 'not computed';
      });
      plot.innerHTML = '';
      table.innerHTML = '';
      orders.innerHTML = '';
      status.innerHTML = '<span class="tone-purple">Refused at ' + ops.length
        + ' operations, and the refusal is the lesson.</span> This checker enumerates every total '
        + 'order and there are ' + ops.length + '! = <strong>' + group(fact(ops.length))
        + '</strong> of them, against ' + group(fact(6)) + ' at six. The growth is factorial: '
        + group(fact(8)) + ' at eight, ' + group(fact(10)) + ' at ten, ' + group(fact(12))
        + ' at twelve. A real linearizability checker does not enumerate &mdash; it searches the '
        + 'order incrementally and prunes a branch the moment a read contradicts the register, and '
        + 'even then the general problem is NP-hard. The cap here is not a limitation of this page '
        + 'that a faster computer would lift. It is the shape of the problem, and a page that '
        + 'silently truncated your history to six would have hidden it.';
      return;
    }

    var res = linearizations(ops, initial);
    var pairs = historyPairs(ops);
    var ok = res.valid.length > 0;

    document.getElementById('lzOps').textContent = ops.length;
    document.getElementById('lzTotal').textContent = ops.length + '! = ' + group(fact(ops.length));
    document.getElementById('lzRt').textContent = res.realTime;
    document.getElementById('lzValid').textContent = res.valid.length;
    document.getElementById('lzVerdict').textContent = ok ? 'linearizable' : 'NOT linearizable';
    document.getElementById('lzConc').textContent = pairs.concurrent + ' of '
      + (pairs.concurrent + pairs.forced);

    var rows = '', i, j;
    for (i = 0; i < ops.length; i += 1) {
      var before = [], after = [], conc = [];
      for (j = 0; j < ops.length; j += 1) {
        if (i === j) continue;
        if (realTimeBefore(ops[j], ops[i])) before.push(ops[j].shortName);
        else if (realTimeBefore(ops[i], ops[j])) after.push(ops[j].shortName);
        else conc.push(ops[j].shortName);
      }
      rows += '<tr><td>' + ops[i].shortName + '</td><td>' + ops[i].name + '</td>'
        + '<td>[' + ops[i].start + ', ' + ops[i].end + ']</td>'
        + '<td>' + (before.length ? before.join(', ') : '&mdash;') + '</td>'
        + '<td>' + (after.length ? after.join(', ') : '&mdash;') + '</td>'
        + '<td class="tone-cyan">' + (conc.length ? conc.join(', ') : '&mdash;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th></th><th>operation</th><th>in flight</th>'
      + '<th>must follow</th><th>must precede</th><th>concurrent with</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="6" class="small-copy">Real time fixes '
      + pairs.forced + ' of the ' + (pairs.forced + pairs.concurrent) + ' pairs. The other '
      + pairs.concurrent + ' are free, and the enumeration is a search over exactly that freedom.'
      + '</td></tr></tfoot>';

    var orows = '', shown = Math.min(res.valid.length, 6);
    for (i = 0; i < shown; i += 1) {
      var names = [], value = initial, trace = [];
      for (j = 0; j < res.valid[i].length; j += 1) {
        var op = ops[res.valid[i][j]];
        names.push(op.shortName);
        if (op.kind === 'w') { value = op.value; trace.push('write ' + op.value + ' &rarr; ' + value); }
        else trace.push('read ' + op.value + ' = the register');
      }
      orows += '<tr class="tone-green"><td>' + (i + 1) + '</td><td>' + names.join(' &rarr; ')
        + '</td><td>' + trace.join('; ') + '</td></tr>';
    }
    if (!res.valid.length) {
      /* Not one legal order: show the real-time orders and what each read got
         wrong, because "there is no order" is a claim the page should support. */
      var perms = permutations(ops.length), listed = 0;
      for (i = 0; i < perms.length && listed < 6; i += 1) {
        if (!orderRespectsRealTime(ops, perms[i])) continue;
        var nm = [], v2 = initial, broke = null;
        for (j = 0; j < perms[i].length; j += 1) {
          var o2 = ops[perms[i][j]];
          nm.push(o2.shortName);
          if (o2.kind === 'w') { v2 = o2.value; continue; }
          if (broke === null && o2.value !== v2) {
            broke = o2.shortName + ' returned ' + o2.value + ' with ' + v2 + ' in the register';
          }
        }
        orows += '<tr class="tone-red"><td>' + (listed + 1) + '</td><td>' + nm.join(' &rarr; ')
          + '</td><td>' + (broke || 'legal') + '</td></tr>';
        listed += 1;
      }
    }
    orders.innerHTML = '<thead><tr><th></th><th>order</th><th>'
      + (res.valid.length ? 'what the register does' : 'where it breaks')
      + '</th></tr></thead><tbody>' + orows + '</tbody><tfoot><tr><td colspan="3" class="small-copy">'
      + (res.valid.length
          ? (res.valid.length > 6 ? 'The first 6 of ' + res.valid.length + ' legal orders.'
              : 'Every legal order, listed.')
          : 'Every order real time allows, and the first read in each that the register cannot have '
            + 'produced.')
      + '</td></tr></tfoot>';

    var lo = ops[0].start, hi = ops[0].end;
    for (i = 0; i < ops.length; i += 1) {
      if (ops[i].start < lo) lo = ops[i].start;
      if (ops[i].end > hi) hi = ops[i].end;
    }
    var span = (hi - lo) || 1;
    function px(t) { return 70 + ((t - lo) / span) * 560; }
    var rowH = Math.min(26, 150 / ops.length), s = '';
    for (i = 0; i < ops.length; i += 1) {
      var y = 30 + i * rowH;
      s += '<rect x="' + px(ops[i].start) + '" y="' + y + '" width="'
        + Math.max(6, px(ops[i].end) - px(ops[i].start)) + '" height="' + (rowH - 8) + '" rx="4" '
        + 'fill="var(--cyan)" opacity="0.55" />'
        + '<text x="' + (px(ops[i].start) + 6) + '" y="' + (y + rowH - 15) + '" font-size="10" '
        + 'fill="var(--text)" font-weight="700">' + ops[i].name + '</text>'
        + '<text x="62" y="' + (y + rowH - 15) + '" text-anchor="end" font-size="11" '
        + 'fill="var(--muted)">' + ops[i].shortName + '</text>';
    }
    var baseY = 30 + ops.length * rowH + 8;
    s += '<line x1="70" y1="' + baseY + '" x2="630" y2="' + baseY
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="70" y="' + (baseY + 14) + '" font-size="10" fill="var(--muted)">t = ' + lo + '</text>'
      + '<text x="630" y="' + (baseY + 14) + '" text-anchor="end" font-size="10" fill="var(--muted)">t = '
      + hi + '</text>';
    if (res.valid.length) {
      var picked = [];
      for (j = 0; j < res.valid[0].length; j += 1) picked.push(ops[res.valid[0][j]].shortName);
      s += '<text x="70" y="' + (baseY + 32) + '" font-size="11" fill="var(--green)" '
        + 'font-weight="700">one legal order: ' + picked.join(' &rarr; ') + '</text>'
        + '<text x="70" y="' + (baseY + 48) + '" font-size="10" fill="var(--muted)">'
        + res.valid.length + ' of the ' + res.realTime + ' orders real time allows are legal, out of '
        + group(fact(ops.length)) + ' orders in total</text>';
    } else {
      s += '<text x="70" y="' + (baseY + 32) + '" font-size="11" fill="var(--red)" '
        + 'font-weight="700">no legal order exists: this history is not linearizable</text>'
        + '<text x="70" y="' + (baseY + 48) + '" font-size="10" fill="var(--muted)">all '
        + res.realTime + ' orders real time allows were tried, out of ' + group(fact(ops.length))
        + ' in total</text>';
    }
    plot.innerHTML = s;

    status.innerHTML = 'This history has <strong>' + ops.length + ' operations</strong>, so there are '
      + ops.length + '! = ' + group(fact(ops.length)) + ' total orders. Real time rules out all but '
      + '<strong>' + res.realTime + '</strong> of them, and of those <strong>' + res.valid.length
      + '</strong> ' + (res.valid.length === 1 ? 'is' : 'are') + ' legal for a register starting at '
      + initial + '. '
      + (ok
          ? '<span class="tone-green">The history is linearizable</span>, and the order printed '
            + 'above is the witness &mdash; every read in it returns what the previous write put '
            + 'there, and no operation is moved outside its own interval.'
          : '<span class="tone-red">The history is NOT linearizable, and the count is the proof.</span> '
            + 'Every read in it returned a value that some replica really was holding, which is '
            + 'exactly the misconception: a value being real somewhere is not the same as the '
            + 'operations having an order. The table above shows, for each order real time permits, '
            + 'the first read that the register could not have produced.')
      + ' <span class="tone-purple">Six operations is the cap</span>, because 6! = ' + group(fact(6))
      + ' and 7! = ' + group(fact(7)) + '. Paste a seventh operation and the page will refuse and '
      + 'say why: enumeration is factorial, real checkers prune instead, and the general problem is '
      + 'NP-hard. That is a fact about linearizability, not about this widget.';
  }

  preset.addEventListener('change', function () { specIn.value = preset.value; redraw(); });
  specIn.addEventListener('input', redraw);
  initS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Linearizability by enumeration",
        subtitle="Count the legal total orders — and see why six is the cap",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the history"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every total order is generated, filtered by the real-time order, and replayed against "
            "a register. The count is exact and zero is a violation.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L13 - merge
# ---------------------------------------------------------------------------


def _merge(cfg):
    trace = str(cfg.get("trace", "A:3:+2, B:5:+3, C:4:+1, B:9:+4"))

    markup = (
        _toolbar(
            "Conflict resolution, counted",
            "last-writer-wins discards; the counter CRDT does not",
            [("red", "discarded by last-writer-wins"), ("green", "kept by both"),
             ("cyan", "the CRDT&rsquo;s per-replica counts"), ("purple", "the true total")],
        )
        + _stage(_svg("mgPlot", "0 0 520 270",
                      "Each update as a bar per replica, with the ones last-writer-wins throws away marked."))
        + _table("mgTable")
        + _table("mgLaws")
        + _banner("mgStatus")
    )
    controls = (
        _text("mgTrace", "Concurrent updates, as replica:timestamp:+delta", trace)
        + _kpis(
            [
                ("Updates in the trace", "mgCount"),
                ("True total, every update applied", "mgTrue"),
                ("Last-writer-wins value", "mgLww"),
                ("Updates LWW discards", "mgLost"),
                ("Counter CRDT value", "mgCrdt"),
                ("Updates the CRDT discards", "mgCrdtLost"),
            ]
        )
        + _hint(
            "mgHint",
            "Write <span class=\"tt\">B:5:+3</span> for replica B adding three at timestamp 5. No "
            "replica has seen any other&rsquo;s update, so all of these are concurrent &mdash; which "
            "is the case the two merges disagree about, and the only case that matters.",
        )
    )

    script = _CORE_JS + r"""
  var traceIn = document.getElementById('mgTrace');
  var plot = document.getElementById('mgPlot'), table = document.getElementById('mgTable');
  var laws = document.getElementById('mgLaws'), status = document.getElementById('mgStatus');
  var KPIS = ['mgCount', 'mgTrue', 'mgLww', 'mgLost', 'mgCrdt', 'mgCrdtLost'];

  function vecText(counts, reps) {
    var out = [], i;
    for (i = 0; i < reps.length; i += 1) out.push(reps[i] + '=' + counts[reps[i]]);
    return '{' + out.join(', ') + '}';
  }

  function redraw() {
    var trace = parseTrace(traceIn.value);
    if (!trace) {
      plot.innerHTML = '';
      table.innerHTML = '';
      laws.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That is not an update trace.</span> Each update is '
        + '<span class="tone-muted">B:5:+3</span> &mdash; a replica letter, a timestamp and a '
        + 'positive delta. A grow-only counter grows, so the delta must be positive, and at most '
        + 'twelve updates fit on the page.';
      return;
    }

    var reps = traceReplicas(trace);
    var total = traceTotal(trace);
    var lww = lwwMerge(trace);
    var counts = crdtCounts(trace);
    var crdt = crdtValue(counts);
    var states = replicaStates(trace);

    document.getElementById('mgCount').textContent = trace.length + ' at ' + reps.length
      + ' replica' + (reps.length === 1 ? '' : 's');
    document.getElementById('mgTrue').textContent = total;
    document.getElementById('mgLww').textContent = lww.value + ' (replica ' + lww.winner + ' wins)';
    document.getElementById('mgLost').textContent = lww.lost.length + ' update'
      + (lww.lost.length === 1 ? '' : 's') + ', worth ' + lww.discarded;
    document.getElementById('mgCrdt').textContent = crdt;
    document.getElementById('mgCrdtLost').textContent = (crdt === total ? '0 — nothing'
      : 'DISAGREES with the total');

    var rows = '', i;
    for (i = 0; i < trace.length; i += 1) {
      var dropped = trace[i].replica !== lww.winner;
      rows += '<tr class="' + (dropped ? 'tone-red' : 'tone-green') + '"><td>' + trace[i].replica
        + '</td><td>' + trace[i].ts + '</td><td>+' + trace[i].delta + '</td>'
        + '<td>' + (dropped ? 'discarded' : 'kept') + '</td>'
        + '<td>counted in ' + trace[i].replica + '&rsquo;s component</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>replica</th><th>timestamp</th><th>delta</th>'
      + '<th>under last-writer-wins</th><th>under the counter CRDT</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><td colspan="5" class="small-copy">Last-writer-wins keeps the '
      + 'register of the replica holding the largest timestamp &mdash; ' + lww.winner + ' at t = '
      + trace.reduce(function (m, u) { return u.replica === lww.winner && u.ts > m ? u.ts : m; }, 0)
      + ' &mdash; and that register contains only that replica&rsquo;s own updates. Every red row '
      + 'is an acknowledged write that no longer exists.</td></tr></tfoot>';

    /* The three laws, checked on this trace rather than asserted. If the merge
       were not commutative, associative and idempotent, the value would depend
       on which replicas happened to gossip first. */
    var lrows = '', a = states[reps[0]] || {}, b = states[reps[1]] || a, c = states[reps[2]] || b;
    var ab = crdtJoin(a, b), ba = crdtJoin(b, a);
    var abc = crdtJoin(crdtJoin(a, b), c), aBc = crdtJoin(a, crdtJoin(b, c));
    var twice = crdtJoin(ab, ab);
    lrows += '<tr class="' + (countsEqual(ab, ba) ? 'tone-green' : 'tone-red') + '">'
      + '<td>commutative</td><td class="tt">A &or; B = B &or; A</td><td>' + vecText(ab, reps)
      + '</td><td>' + vecText(ba, reps) + '</td><td>' + (countsEqual(ab, ba) ? 'equal' : 'DIFFER')
      + '</td></tr>'
      + '<tr class="' + (countsEqual(abc, aBc) ? 'tone-green' : 'tone-red') + '">'
      + '<td>associative</td><td class="tt">(A &or; B) &or; C = A &or; (B &or; C)</td><td>'
      + vecText(abc, reps) + '</td><td>' + vecText(aBc, reps) + '</td><td>'
      + (countsEqual(abc, aBc) ? 'equal' : 'DIFFER') + '</td></tr>'
      + '<tr class="' + (countsEqual(twice, ab) ? 'tone-green' : 'tone-red') + '">'
      + '<td>idempotent</td><td class="tt">(A &or; B) &or; (A &or; B) = A &or; B</td><td>'
      + vecText(twice, reps) + '</td><td>' + vecText(ab, reps) + '</td><td>'
      + (countsEqual(twice, ab) ? 'equal' : 'DIFFER') + '</td></tr>';
    laws.innerHTML = '<thead><tr><th>law</th><th>statement</th><th>left</th><th>right</th>'
      + '<th></th></tr></thead><tbody>' + lrows + '</tbody><tfoot><tr><td colspan="5" '
      + 'class="small-copy">The merge is elementwise maximum, so these three hold and the page '
      + 'checks them on your trace. Together they are why the replicas converge whatever order '
      + 'they meet in, how often they meet, and how many times a message is redelivered.'
      + '</td></tr></tfoot>';

    var lane = Math.min(40, 150 / Math.max(reps.length, 1)), s = '';
    var maxTs = 1, j;
    for (j = 0; j < trace.length; j += 1) if (trace[j].ts > maxTs) maxTs = trace[j].ts;
    function tx(t) { return 60 + (t / (maxTs + 1)) * 420; }
    for (i = 0; i < reps.length; i += 1) {
      var y = 34 + i * lane;
      s += '<line x1="60" y1="' + y + '" x2="490" y2="' + y + '" stroke="var(--line-strong)" '
        + 'stroke-width="1.2" />'
        + '<text x="52" y="' + (y + 4) + '" text-anchor="end" font-size="12" fill="var(--text)" '
        + 'font-weight="700">' + reps[i] + '</text>'
        + '<text x="496" y="' + (y + 4) + '" font-size="10" fill="var(--cyan)">'
        + counts[reps[i]] + '</text>';
    }
    for (j = 0; j < trace.length; j += 1) {
      var lanei = reps.indexOf(trace[j].replica), yy = 34 + lanei * lane;
      var kept = trace[j].replica === lww.winner;
      s += '<circle cx="' + tx(trace[j].ts) + '" cy="' + yy + '" r="7" fill="var('
        + (kept ? '--green' : '--red') + ')" />'
        + '<text x="' + tx(trace[j].ts) + '" y="' + (yy - 12) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(' + (kept ? '--green' : '--red') + ')" font-weight="700">+'
        + trace[j].delta + '</text>'
        + '<text x="' + tx(trace[j].ts) + '" y="' + (yy + 18) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">t=' + trace[j].ts + '</text>';
    }
    var by = 34 + reps.length * lane + 8;
    s += '<text x="60" y="' + (by + 10) + '" font-size="11" fill="var(--red)" font-weight="700">'
      + 'last-writer-wins: ' + lww.value + ' &mdash; ' + lww.lost.length + ' update'
      + (lww.lost.length === 1 ? '' : 's') + ' discarded, worth ' + lww.discarded + '</text>'
      + '<text x="60" y="' + (by + 28) + '" font-size="11" fill="var(--cyan)" font-weight="700">'
      + 'counter CRDT: ' + vecText(counts, reps) + ' &rarr; ' + crdt + '</text>'
      + '<text x="60" y="' + (by + 46) + '" font-size="11" fill="var(--purple)" font-weight="700">'
      + 'every update applied: ' + total + '</text>'
      + '<text x="60" y="' + (by + 64) + '" font-size="10" fill="var(--muted)">'
      + 'horizontal position is the timestamp; the number at the right of each lane is that '
      + 'replica&rsquo;s CRDT component</text>'
      + '<text x="60" y="24" font-size="10" fill="var(--muted)">' + trace.length
      + ' concurrent updates across ' + reps.length + ' replica'
      + (reps.length === 1 ? '' : 's') + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'The trace holds <strong>' + trace.length + ' concurrent updates</strong> '
      + 'worth <strong>' + total + '</strong> in total. <span class="tone-red">Last-writer-wins '
      + 'returns ' + lww.value + '</span>: replica ' + lww.winner + ' holds the largest timestamp, '
      + 'so its register wins and the other ' + lww.lost.length + ' update'
      + (lww.lost.length === 1 ? ' is' : 's are') + ' gone &mdash; '
      + (lww.lost.length ? lww.lost.join('; ') : 'none, because every update was at one replica')
      + '. <span class="tone-cyan">The counter CRDT returns ' + crdt + '</span> from '
      + vecText(counts, reps) + ', which is the true total, and it discards nothing. '
      + (lww.tieBroken
          ? '<span class="tone-amber">Two replicas share the largest timestamp here</span>, so the '
            + 'winner was chosen by replica name. That is what a real LWW register does, and it is '
            + 'the clearest form of the point: '
          : 'And note what accurate clocks would have bought: ')
      + 'the clocks are not the problem. Making every timestamp correct changes WHICH update '
      + 'survives and not HOW MANY do &mdash; last-writer-wins is an arbitrary choice among '
      + 'concurrent updates, and the count of discarded updates is ' + lww.lost.length
      + ' however good the clocks are. The CRDT keeps one count per replica and merges by '
      + 'elementwise maximum, and the three laws checked above are why every replica converges on '
      + crdt + ' whatever order the gossip arrives in.';
  }

  traceIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Conflict resolution, counted",
        subtitle="What last-writer-wins throws away, and what a counter CRDT keeps",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the concurrent update trace"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both merges run on the same trace and both counts are exact. The three merge laws are "
            "checked on your updates rather than claimed.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "fanout": _fanout,
    "sync": _sync,
    "lag": _lag,
    "quorum": _quorum,
    "quorumlat": _quorumlat,
    "sloppy": _sloppy,
    "majority": _majority,
    "election": _election,
    "lamport": _lamport,
    "vector": _vector,
    "drift": _drift,
    "linearize": _linearize,
    "merge": _merge,
}

MODES = tuple(sorted(_MODES))


def replica_lab(cfg):
    """Course 6's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract rather than defensiveness. A kit that fell back
    to a default mode would render a finished-looking page carrying another
    lesson's widget and nothing downstream would notice: the markup assertions
    pass, labcheck passes, and a reader is shown the sloppy-quorum arithmetic
    under the linearizability title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "replica_lab: unknown mode %r; the thirteen modes of course 6 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["replica_lab", "REPLICA_JS", "MODES"]
