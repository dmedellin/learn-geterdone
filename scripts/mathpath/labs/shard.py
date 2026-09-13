"""Course 7: Partitioning and Load Balancing -- one kit, twelve modes.

Splitting data or traffic across N nodes is balls into bins, and almost every
intuition a reader brings to it is wrong in a way that costs money. The kit
exists to let the arithmetic contradict the intuition on numbers the reader
chose, in the six places the course says it will.

Five decisions run through all twelve modes.

  THE STREAM IS MINSTD, NOT THE GLIBC LCG THE REST OF THE PATH USES. Every
  other seeded lab on this path draws from a = 1 103 515 245, c = 12 345,
  m = 2^31. This kit takes its draws MODULO N, and the low bits of a
  power-of-two-modulus LCG are periodic: under that generator x % 4 is
  0, 1, 2, 3, 0, 1, 2, 3 forever, and 1 200 keys into 8 or 16 bins come out
  PERFECTLY level -- max/mean exactly 1.0000. A hash-imbalance lesson drawing
  from it would demonstrate the opposite of its own claim. So shardStream uses
  a = 16 807, c = 0, m = 2^31 - 1, which is prime, so every bit of the state is
  as good as every other and x % N is not a cycle. The constants are printed on
  every page that draws. The seed does NOT become the state: an LCG's k-th
  value is an affine function of its seed, so consecutive seeds hand out
  correlated placements, and every mode here asks the reader to reseed and
  compare. shardSeedState runs the seed through the splitmix64 finaliser first,
  which is nonlinear and breaks that. The defect it fixes was measured, not
  imagined -- see the comment on that function.

  MEASURED AND STATED ARE DIFFERENT COLUMNS. Two results on this course are
  stated and not proved anywhere in the library -- the one-choice maximum load
  Theta(log n / log log n) and the two-choice ln ln n -- because their proofs
  need Chernoff bounds, which no Subject here teaches. Every mode that prints
  one says so in those words, prints it through logApprox as a rounded number,
  and puts the number the page actually MEASURED beside it. The same rule
  covers the 1/sqrt(V) rate in vnodes.

  EXACT WHERE COUNTING IS POSSIBLE, AND COUNTING IS POSSIBLE MORE OFTEN THAN
  IT LOOKS. The rehash fractions are the clearest case: over a complete cycle
  of N(N+1) consecutive hashes, exactly N of them keep their home under mod N
  -> mod N+1, so the moved fraction is N/(N+1) EXACTLY, by enumeration, and the
  ring's 1/(N+1) is the rest of the same one. modCycleMoved counts it and
  rehashShareSum adds the two fractions and gets 1. That identity is the whole
  argument for consistent hashing and it is checked, not asserted.

  A HOT KEY IS NOT A BALANCE PROBLEM. hottestLoad(lam, f, N) is f*lam plus the
  uniform remainder, and the first term has no N in it. The hotkey mode draws
  the curve against N precisely so the reader watches it flatten onto f*lam
  instead of falling, which no amount of resharding changes.

  RATE AND WORK ARE DIFFERENT QUANTITIES. scatter exists because "we sharded,
  so each node does less" is true per shard and false in total: an unrouted
  query is N shard requests, so the fleet's request rate went UP by a factor of
  N while each shard's share of any one query went down.

The modes, and the lesson each belongs to:

  count       L1  ceil(lam/(c*rho)) against ceil(D*RF/per-node), and the larger
  bins        L2  a seeded placement's occupancy, its max, and max/mean
  rehash      L3  keys moved under mod N and under a ring, counted both ways
  vnodes      L4  arc shares on the ring, and the spread at V = 1, 10, 100
  range       L5  the hottest range's share of CURRENT writes, per pattern
  hotkey      L6  f*lam + (1-f)lam/N against N, and f/s after salting
  straggler   L7  the exact distribution of the maximum of N partition times
  twochoice   L8  one choice against d, from one stream, with both asymptotics
  scatter     L9  N x rate, and the tail, exact and from a seeded run
  index       L10 r*N + w against r + 2w, and the crossover r/w = 1/(N-1)
  crossshard  L11 N^(1-k), and the two-phase cost the rest of them pay
  rebalance   L12 m*D/B, the capacity the copy steals, and the wait at that rho
"""

from .algebra_core import RATIONAL_JS
from .common import Lab
from .counting import BIGINT_JS
from .sysdesign_core import APPROX_JS, PMF_JS, PERCENTILE_JS, QUEUE_JS, RCEIL_JS, STREAM_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Every function here is top-level and touches
# nothing but its arguments, so scripts/mathcheck.js can call each one without
# a DOM -- which is the only way the parts that turn out to be wrong get found.
# ---------------------------------------------------------------------------

SHARDKIT_JS = r"""
  /* ================================================================ output */

  /* Rdec goes through Number(a.n)/Number(a.d). This kit produces rationals a
     double cannot hold -- N^(1-k) at k = 12 and N = 64 has a 65-bit
     denominator -- so decimals here are long division in BigInt, rounded half
     up at the last digit printed. */
  function Rfixed(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }
  /* A rational count of bytes read the way a capacity plan reads it, decimal
     throughout: 1 TB is 10^12 bytes, which is what a disk is sold as and what
     a throttle is quoted in. Stated once here rather than assumed twice. */
  function byteText(a) {
    var units = [[1000000000000000n, 'PB'], [1000000000000n, 'TB'],
                 [1000000000n, 'GB'], [1000000n, 'MB'], [1000n, 'kB']];
    for (var i = 0; i < units.length; i += 1) {
      if (Rcmp(Rabs(a), R(units[i][0], 1n)) >= 0) {
        return Rfixed(Rdiv(a, R(units[i][0], 1n)), 2) + ' ' + units[i][1];
      }
    }
    return Rfixed(a, 0) + ' B';
  }
  /* Seconds as an operator reads them. Exact: the seconds keep their fraction. */
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

  /* ================================================= the seeded placement

     MINSTD: a = 16807, c = 0, m = 2^31 - 1, prime. See the module docstring
     for why this kit does not use the generator the rest of the path uses --
     the short version is that this kit takes its values MODULO N, and the low
     bits of a power-of-two modulus are a cycle rather than a sample.

     The seed itself never becomes the state -- see shardSeedState. */
  function shardMultiplier() { return 16807; }
  function shardModulus() { return 2147483647; }
  /* The seed is MIXED before it becomes a state, and this is not decoration.
     An LCG's k-th value is an AFFINE function of its seed -- under a purely
     multiplicative one it is literally seed x (a^k mod m) -- so for the small
     seeds a slider offers, nothing wraps and the whole placement scales with
     the seed. Measured, before this was here: the arc a joining node took on
     seeds 1 through 12 came out 0.0206, 0.0309, 0.0411, 0.0514, 0.0617, ...
     a straight line, not twelve samples of anything. Every mode on this course
     asks the reader to reseed and compare, so correlated seeds would make the
     comparison meaningless while looking perfectly random on any one of them.
     The finaliser below is the splitmix64 mixer: multiply, xor-shift, multiply,
     xor-shift, which is nonlinear over the integers and breaks the affinity. */
  function shardSeedState(seed) {
    var mask = 0xFFFFFFFFFFFFFFFFn;
    var x = (BigInt(seed) + 1n) * 0x9E3779B97F4A7C15n & mask;
    x = ((x ^ (x >> 30n)) * 0xBF58476D1CE4E5B9n) & mask;
    x = ((x ^ (x >> 27n)) * 0x94D049BB133111EBn) & mask;
    x = x ^ (x >> 31n);
    return Number(x % BigInt(shardModulus() - 1)) + 1;   /* never the fixed point 0 */
  }
  function shardStream(seed, count) {
    return lcgStream(shardMultiplier(), 0, shardModulus(), shardSeedState(seed), count);
  }
  /* Uniform rationals in (0, 1) from that stream, for inverse-transform
     sampling. Exact fractions over the modulus, not doubles. */
  function shardUniform(seed, count) {
    var m = BigInt(shardModulus());
    return shardStream(seed, count).map(function (x) { return R(BigInt(x), m); });
  }

  /* ======================================================= L1: how many

     Two constraints, and the answer is the larger. Both are ceilings of exact
     rationals, because 23.08 shards is 24 shards and the whole point of a
     sizing lesson is that the fraction rounds the expensive way. */
  function shardsForLoad(lamPeak, perNode, rhoTarget) {
    if (Rzero(perNode) || Rzero(rhoTarget)) return null;
    return Rceil(Rdiv(lamPeak, Rmul(perNode, rhoTarget)));
  }
  function shardsForStorage(dataBytes, rf, perNodeBytes) {
    if (Rzero(perNodeBytes)) return null;
    return Rceil(Rdiv(Rmul(dataBytes, rf), perNodeBytes));
  }
  function bindingShards(byLoad, byStorage) {
    if (byLoad === null || byStorage === null) return null;
    if (byLoad > byStorage) return { n: byLoad, binding: 'load', slack: byLoad - byStorage };
    if (byStorage > byLoad) return { n: byStorage, binding: 'storage', slack: byStorage - byLoad };
    return { n: byLoad, binding: 'both', slack: 0n };
  }
  /* What the chosen count actually leaves: the utilisation each node runs at
     and the bytes each one holds. A count chosen on one constraint is checked
     against the other here, which is the lesson's misconception. */
  function utilisationAt(lamPeak, perNode, n) {
    return Rdiv(lamPeak, Rmul(perNode, R(BigInt(n), 1n)));
  }
  function bytesPerNodeAt(dataBytes, rf, n) {
    return Rdiv(Rmul(dataBytes, rf), R(BigInt(n), 1n));
  }

  /* ==================================================== L2: balls in bins

     m keys into N bins by h % N. The occupancy is counted, never modelled:
     the mean is m/N exactly and the maximum is whatever the stream produced. */
  function binOccupancy(seed, m, n) {
    var counts = new Array(n).fill(0), draws = shardStream(seed, m), i;
    for (i = 0; i < m; i += 1) counts[draws[i] % n] += 1;
    return counts;
  }
  function occMax(counts) {
    var best = 0;
    for (var i = 0; i < counts.length; i += 1) if (counts[i] > best) best = counts[i];
    return best;
  }
  function occMin(counts) {
    var best = counts.length ? counts[0] : 0;
    for (var i = 0; i < counts.length; i += 1) if (counts[i] < best) best = counts[i];
    return best;
  }
  function occEmpty(counts) {
    var c = 0;
    for (var i = 0; i < counts.length; i += 1) if (counts[i] === 0) c += 1;
    return c;
  }
  function occTotal(counts) {
    var t = 0;
    for (var i = 0; i < counts.length; i += 1) t += counts[i];
    return t;
  }
  /* max/mean as an exact fraction: max * N / m. The figure the lesson is
     about, and it is a ratio of integers, so it prints as one. */
  function maxOverMean(counts) {
    var m = occTotal(counts);
    if (!m) return null;
    return R(BigInt(occMax(counts)) * BigInt(counts.length), BigInt(m));
  }
  function minOverMean(counts) {
    var m = occTotal(counts);
    if (!m) return null;
    return R(BigInt(occMin(counts)) * BigInt(counts.length), BigInt(m));
  }
  /* The excess over the mean measured in root-means: (max - mean)/sqrt(mean).
     The lesson's claim is that the gap grows like a square root of the mean
     rather than staying a fixed percentage of it, and this is the number that
     stays roughly constant while max/mean shrinks. It ROUNDS -- sqrtApprox is
     Newton from a rational -- and the page says so. */
  function excessInRootMeansApprox(counts) {
    var m = occTotal(counts), n = counts.length;
    if (!m || !n) return NaN;
    var mean = R(BigInt(m), BigInt(n));
    var excess = Rsub(R(BigInt(occMax(counts)), 1n), mean);
    var root = sqrtApprox(mean, 1e-15);
    return root === 0 ? NaN : Rnum(excess) / root;
  }
  /* The one-choice maximum load, STATED and not proved: for n balls in n bins
     it is Theta(log n / log log n). Printed rounded, through logApprox, and
     every page that prints it says the proof is not in this library. */
  function oneChoiceStatedApprox(n) {
    if (n < 16) return NaN;
    return logApprox(n) / logApprox(logApprox(n));
  }
  function twoChoiceStatedApprox(n) {
    if (n < 16) return NaN;
    return logApprox(logApprox(n));
  }

  /* ====================================================== L3: rehashing

     The two fractions, stated. They sum to one, which is the entire argument
     for consistent hashing and is checked below rather than asserted. */
  function modMoveShare(n) { return R(BigInt(n), BigInt(n) + 1n); }
  function ringMoveShare(n) { return R(1n, BigInt(n) + 1n); }
  function rehashShareSum(n) { return Radd(modMoveShare(n), ringMoveShare(n)); }

  /* The exact count, by enumeration. Over the complete cycle of N(N+1)
     consecutive hash values, h % N equals h % (N+1) exactly when both are the
     same v < N -- and by the Chinese Remainder Theorem each of the N(N+1)
     pairs of residues occurs exactly once. So exactly N keys stay and the
     moved fraction is N/(N+1) on the nose, with no sampling in it at all. */
  function modCycleMoved(n) {
    var total = n * (n + 1), moved = 0, h;
    for (h = 0; h < total; h += 1) if (h % n !== h % (n + 1)) moved += 1;
    return { moved: moved, total: total, share: R(BigInt(moved), BigInt(total)) };
  }
  /* The same count over a seeded sample of m hashes, which is what a reader
     with a real key set would measure. It lands near N/(N+1), not on it. */
  function modSampleMoved(seed, m, n) {
    var draws = shardStream(seed, m), moved = 0, i;
    for (i = 0; i < m; i += 1) if (draws[i] % n !== draws[i] % (n + 1)) moved += 1;
    return { moved: moved, total: m, share: R(BigInt(moved), BigInt(m)) };
  }

  /* The ring. Token j belongs to node floor(j/v), so the tokens of an N-node
     ring are a PREFIX of the tokens of an (N+1)-node ring: adding a node adds
     tokens and moves nothing else, which is the property the whole scheme is
     for. A key at position p belongs to the first token at or after p going
     clockwise, wrapping -- successor ownership, stated once and used
     everywhere in this kit. */
  function ringTokens(seed, n, v) {
    var draws = shardStream(seed, n * v), out = [], j;
    for (j = 0; j < n * v; j += 1) out.push({ pos: draws[j], node: Math.floor(j / v) });
    out.sort(function (a, b) { return a.pos - b.pos; });
    return out;
  }
  function ringOwner(tokens, pos) {
    for (var i = 0; i < tokens.length; i += 1) if (tokens[i].pos >= pos) return tokens[i].node;
    return tokens.length ? tokens[0].node : -1;   /* wrapped past the last token */
  }
  /* Each node's share of the ring, as an exact rational over the modulus.
     The arc (previous token, this token] belongs to this token. */
  function ringShares(seed, n, v) {
    var tokens = ringTokens(seed, n, v), m = shardModulus();
    var arcs = new Array(n).fill(0), i;
    for (i = 0; i < tokens.length; i += 1) {
      var prev = i === 0 ? tokens[tokens.length - 1].pos - m : tokens[i - 1].pos;
      arcs[tokens[i].node] += tokens[i].pos - prev;
    }
    return arcs.map(function (a) { return R(BigInt(a), BigInt(m)); });
  }
  /* The arc the (N+1)-th node takes when it joins, exactly: its token's own
     arc under the new ring. Its EXPECTATION is 1/(N+1); what a given seed
     hands you is this. */
  function ringNewNodeArc(seed, n, v) {
    var shares = ringShares(seed, n + 1, v);
    return shares[n];
  }
  /* And the count of keys that actually move, which is the enumeration the
     lesson asks for rather than the expectation. */
  function ringSampleMoved(seed, keySeed, m, n, v) {
    var before = ringTokens(seed, n, v), after = ringTokens(seed, n + 1, v);
    var keys = shardStream(keySeed, m), moved = 0, i;
    for (i = 0; i < m; i += 1) {
      if (ringOwner(before, keys[i]) !== ringOwner(after, keys[i])) moved += 1;
    }
    return { moved: moved, total: m, share: R(BigInt(moved), BigInt(m)) };
  }

  /* The mean arc a joining node takes over several seeds. One ring is one
     draw of an exponential-looking quantity with a very long tail, so a single
     arc says nothing about 1/(N+1); the average over seeds is what converges
     to it, and the page shows both rather than pretending the first is the
     second. */
  function ringArcMeanApprox(seed, n, v, seeds) {
    var acc = R(0n, 1n), i;
    for (i = 0; i < seeds; i += 1) acc = Radd(acc, ringNewNodeArc(seed + i, n, v));
    return Rdiv(acc, R(BigInt(seeds), 1n));
  }

  /* ================================================== L4: virtual nodes

     Sum of shares is 1 by construction; the figures are how far from level
     the shares are. maxOverMeanShares is the objective the lesson states. */
  function shareMaxOverMean(shares) {
    var n = shares.length, best = shares[0], i;
    for (i = 1; i < n; i += 1) if (Rcmp(shares[i], best) > 0) best = shares[i];
    return Rmul(best, R(BigInt(n), 1n));
  }
  function shareMinOverMean(shares) {
    var n = shares.length, worst = shares[0], i;
    for (i = 1; i < n; i += 1) if (Rcmp(shares[i], worst) < 0) worst = shares[i];
    return Rmul(worst, R(BigInt(n), 1n));
  }
  function shareTotal(shares) {
    var t = R(0n, 1n);
    for (var i = 0; i < shares.length; i += 1) t = Radd(t, shares[i]);
    return t;
  }
  /* The relative spread: root mean square of (share*N - 1) over the nodes.
     THIS is the quantity that falls like 1/sqrt(V) -- the maximum of N draws
     is far too noisy at one seed to show a rate, and a lesson that asked the
     reader to read 1/sqrt(V) off a single maximum would be asking them to see
     something that is not there. It rounds: the square root is sqrtApprox. */
  function spreadRmsApprox(shares) {
    var n = shares.length, acc = R(0n, 1n), i;
    for (i = 0; i < n; i += 1) {
      var d = Rsub(Rmul(shares[i], R(BigInt(n), 1n)), R(1n, 1n));
      acc = Radd(acc, Rmul(d, d));
    }
    return sqrtApprox(Rdiv(acc, R(BigInt(n), 1n)), 1e-15);
  }
  /* The STATED rate: relative spread falls like 1/sqrt(V). Rounded, labelled,
     and printed beside the measured value rather than instead of it. */
  function spreadRateStatedApprox(v) { return 1 / sqrtApprox(R(BigInt(v), 1n), 1e-15); }
  /* Averaging the measured spread over several seeds, because one ring is one
     sample and the rate is a claim about the distribution. */
  function spreadRmsOverSeedsApprox(seed, n, v, seeds) {
    var acc = 0, i;
    for (i = 0; i < seeds; i += 1) acc += spreadRmsApprox(ringShares(seed + i, n, v));
    return acc / seeds;
  }
  function maxOverMeanOverSeedsApprox(seed, n, v, seeds) {
    var acc = 0, i;
    for (i = 0; i < seeds; i += 1) acc += Rnum(shareMaxOverMean(ringShares(seed + i, n, v)));
    return acc / seeds;
  }

  /* =============================================== L5: range partitioning

     Ranges keep locality and lose balance. The three patterns are the three
     things a key can be, and the figure is the hottest range's share of the
     writes happening NOW -- not of the writes ever, which is the trap: a
     monotonic key is perfectly balanced over all time and completely
     unbalanced at every instant of it. */
  function rangeWindows(pattern, m, n, windows, seed, buckets) {
    var grid = [], w, i, draws = shardStream(seed, m), per = Math.floor(m / windows);
    var b = Math.max(1, Math.min(n, buckets || 1)), wide = Math.floor(n / b);
    for (w = 0; w < windows; w += 1) {
      var row = new Array(n).fill(0);
      for (i = 0; i < per; i += 1) {
        var t = w * per + i, bin;
        if (pattern === 'monotonic') {
          /* key = the counter itself; the ranges split the key space evenly,
             so at time t every write lands in the one range holding t. */
          bin = Math.min(n - 1, Math.floor(t * n / m));
        } else if (pattern === 'hashed') {
          /* key = h(id); the range a write lands in has nothing to do with
             when it happened, and a time-range scan has to visit all N. */
          bin = draws[t] % n;
        } else if (pattern === 'prefixed') {
          /* the remedy: a hashed bucket in FRONT of the timestamp. The key
             space is ordered by bucket first, so each bucket owns n/b
             contiguous ranges and marches through them monotonically. Writes
             at any instant are spread over b ranges -- one per bucket -- and a
             time-range scan visits b ranges rather than 1 or N. */
          bin = (draws[t] % b) * wide + Math.min(wide - 1, Math.floor(t * wide / m));
          if (bin > n - 1) bin = n - 1;
        } else {
          return null;
        }
        row[bin] += 1;
      }
      grid.push(row);
    }
    return grid;
  }
  /* The hottest range's share of one window, exactly. */
  function hottestShare(row) {
    var total = occTotal(row);
    if (!total) return R(0n, 1n);
    return R(BigInt(occMax(row)), BigInt(total));
  }
  /* The worst window, which is the number that sizes the shard. */
  function worstWindowShare(grid) {
    var worst = R(0n, 1n);
    for (var w = 0; w < grid.length; w += 1) {
      var s = hottestShare(grid[w]);
      if (Rcmp(s, worst) > 0) worst = s;
    }
    return worst;
  }
  /* And the share over the WHOLE run, which is the figure that makes a
     monotonic key look fine. */
  function lifetimeShare(grid) {
    var n = grid.length ? grid[0].length : 0, totals = new Array(n).fill(0), w, i;
    for (w = 0; w < grid.length; w += 1) for (i = 0; i < n; i += 1) totals[i] += grid[w][i];
    return hottestShare(totals);
  }
  /* How many ranges a scan of one window of time has to touch under each
     pattern, which is what the locality is FOR and what a hash throws away. */
  function scanRanges(pattern, n, buckets) {
    if (pattern === 'monotonic') return 1;
    if (pattern === 'prefixed') return Math.max(1, Math.min(n, buckets || 1));
    if (pattern === 'hashed') return n;
    return null;
  }

  /* ========================================================= L6: hot keys

     The first term has no N in it, and that is the lesson. */
  function hottestLoad(lam, f, n) {
    var uniform = Rdiv(Rmul(Rsub(R(1n, 1n), f), lam), R(BigInt(n), 1n));
    return Radd(Rmul(f, lam), uniform);
  }
  function hottestLoadSalted(lam, f, n, s) {
    var uniform = Rdiv(Rmul(Rsub(R(1n, 1n), f), lam), R(BigInt(n), 1n));
    return Radd(Rdiv(Rmul(f, lam), R(BigInt(s), 1n)), uniform);
  }
  /* What no N ever gets below: the hot key's own traffic. */
  function hotAsymptote(lam, f) { return Rmul(f, lam); }
  function meanLoad(lam, n) { return Rdiv(lam, R(BigInt(n), 1n)); }
  /* Imbalance as the hottest shard over the average one. */
  function hotImbalance(lam, f, n) { return Rdiv(hottestLoad(lam, f, n), meanLoad(lam, n)); }
  /* Salting costs s reads for every read of the hot key: the fan-out a reader
     of that key now pays, which is the price of the fix. */
  function saltReadAmplification(f, s) {
    return Radd(Rmul(f, R(BigInt(s), 1n)), Rsub(R(1n, 1n), f));
  }
  /* The salt that brings the hot shard down to a target multiple of the mean,
     by exact integer search rather than by a logarithm. Returns null when no
     salt can: even s -> infinity leaves the uniform term. */
  function saltForTarget(lam, f, n, targetMultiple) {
    var goal = Rmul(targetMultiple, meanLoad(lam, n));
    for (var s = 1; s <= 4096; s += 1) {
      if (Rcmp(hottestLoadSalted(lam, f, n, s), goal) <= 0) return s;
    }
    return null;
  }

  /* ======================================================= L7: stragglers

     A scatter job ends when its slowest partition ends, so the job's time is
     the maximum of N draws. pmfMax gives that distribution exactly -- P(max <=
     t) = F(t)^N, differenced -- and the mean and the percentile are read off
     it rather than simulated. */

  /* A pmf the reader typed: "20:70, 40:20, 120:8, 400:2" is value:weight, and
     the weights are normalised to exact rational probabilities. Returns null
     on anything that is not a distribution, which is what stops a typo
     printing a confident wrong tail. */
  function parsePmf(text) {
    var parts = String(text).split(','), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (!s) continue;
      var bits = s.split(':');
      if (bits.length !== 2) return null;
      var v = Number(bits[0].trim()), w = Rparse(bits[1].trim());
      if (!isFinite(v) || Math.floor(v) !== v || w === null) return null;
      if (Rcmp(w, R(0n, 1n)) < 0) return null;
      out.push([v, w]);
    }
    if (!out.length) return null;
    var total = R(0n, 1n);
    for (i = 0; i < out.length; i += 1) total = Radd(total, out[i][1]);
    if (Rzero(total)) return null;
    return pmfNormalise(out);
  }
  /* The nearest-rank percentile of a DISTRIBUTION: the smallest value whose
     cumulative probability is at least q. Same convention as percentile() in
     the core -- a value that the distribution actually puts mass on, never an
     interpolated one -- lifted from a sample to a pmf, and the two agree
     exactly on an equiprobable pmf, which is how mathcheck.js checks it. */
  function pmfQuantile(pairs, q) {
    var sorted = pairs.slice().sort(function (x, y) { return x[0] - y[0]; });
    var cum = R(0n, 1n), i;
    for (i = 0; i < sorted.length; i += 1) {
      cum = Radd(cum, sorted[i][1]);
      if (Rcmp(cum, q) >= 0) return sorted[i][0];
    }
    return sorted.length ? sorted[sorted.length - 1][0] : null;
  }
  /* The straggler tax: what the maximum costs over one partition. */
  function stragglerTax(pairs, n) {
    var one = pmfMean(pairs), all = pmfMean(pmfMax(pairs, n));
    return { one: one, all: all, ratio: Rzero(one) ? null : Rdiv(all, one) };
  }
  /* P(at least one partition lands beyond t), which is the shape of the whole
     lesson: a rare slow partition is not rare once there are N of them. */
  function anySlowerThan(pairs, n, t) {
    return Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), pmfTail(pairs, t)), n));
  }

  /* The smallest partition count at which a tail value becomes the job's
     q-quantile. An exact integer search over N, not a logarithm: a 0.5%
     partition is not the p99 of one partition and IS the p99 of three. */
  function smallestNForQuantile(pairs, q, value, cap) {
    for (var n = 1; n <= cap; n += 1) {
      if (pmfQuantile(pmfMax(pairs, n), q) >= value) return n;
    }
    return null;
  }
  /* The slowest value the pmf puts any mass on, which is what a job of enough
     partitions eventually waits for. */
  function pmfWorst(pairs) {
    var worst = null;
    for (var i = 0; i < pairs.length; i += 1) {
      if (Rzero(pairs[i][1])) continue;
      if (worst === null || pairs[i][0] > worst) worst = pairs[i][0];
    }
    return worst;
  }

  /* ================================================ L8: two choices

     Both placements are driven by ONE stream, so the comparison is between
     two policies on identical randomness rather than between two runs. Ball i
     reads draws[i*d] .. draws[i*d + d - 1]; the one-choice arm uses the first
     of each group and ignores the rest, so the arms cannot be accused of
     having been handed different luck. */
  function placeChoices(seed, balls, bins, d) {
    var draws = shardStream(seed, balls * d), counts = new Array(bins).fill(0), i, j;
    for (i = 0; i < balls; i += 1) {
      var best = draws[i * d] % bins;
      for (j = 1; j < d; j += 1) {
        var cand = draws[i * d + j] % bins;
        if (counts[cand] < counts[best]) best = cand;
      }
      counts[best] += 1;
    }
    return counts;
  }
  function placeOneChoiceFrom(seed, balls, bins, d) {
    /* the SAME draws, with the extra choices discarded rather than redrawn */
    var draws = shardStream(seed, balls * d), counts = new Array(bins).fill(0), i;
    for (i = 0; i < balls; i += 1) counts[draws[i * d] % bins] += 1;
    return counts;
  }
  /* The maxima either way across a run of seeds, because one seed is one
     sample of a maximum and the result is about the distribution. */
  function maxLoadAcrossSeeds(seed, balls, bins, d, seeds) {
    var one = [], many = [], i;
    for (i = 0; i < seeds; i += 1) {
      one.push(occMax(placeOneChoiceFrom(seed + i, balls, bins, d)));
      many.push(occMax(placeChoices(seed + i, balls, bins, d)));
    }
    return { one: one, many: many };
  }
  function meanOf(list) {
    var t = 0;
    for (var i = 0; i < list.length; i += 1) t += list[i];
    return list.length ? R(BigInt(t), BigInt(list.length)) : null;
  }

  /* =================================================== L9: scatter-gather

     Two different quantities, and the misconception is that they are one.
     Sharding divides the WORK of a query; it multiplies the number of
     REQUESTS, because an unrouted query asks every shard. */
  function shardRequestRate(queryRate, n) { return Rmul(queryRate, R(BigInt(n), 1n)); }
  function requestAmplification(n) { return R(BigInt(n), 1n); }
  /* A routed query asks one shard; the ratio is the value of the routing key. */
  function routedRequestRate(queryRate) { return queryRate; }
  /* A seeded run of Q queries, each the maximum of N shard latencies drawn by
     inverse transform from the pmf. The sample is returned sorted so the
     nearest-rank percentile in the core can be read straight off it, and the
     page prints it beside the EXACT tail from pmfMax -- two routes to one
     number, which is the only way to notice when one of them is wrong. */
  function scatterSample(pairs, n, queries, seed) {
    var us = shardUniform(seed, n * queries), out = [], q, i;
    for (q = 0; q < queries; q += 1) {
      var worst = null;
      for (i = 0; i < n; i += 1) {
        var v = sampleFromPmf(pairs, us[q * n + i]);
        if (worst === null || v > worst) worst = v;
      }
      out.push(worst);
    }
    return out.sort(function (a, b) { return a - b; });
  }

  /* ======================================== L10: local and global indexes

     Local: read every shard, write one. Global: read one shard, write two --
     the base row and the index entry, which live on different shards. */
  function localIndexCost(r, w, n) { return Radd(Rmul(r, R(BigInt(n), 1n)), w); }
  function globalIndexCost(r, w) { return Radd(r, Rmul(R(2n, 1n), w)); }
  /* The crossover: r*N + w = r + 2w gives r(N - 1) = w, so the ratio r/w at
     which the two cost the same is 1/(N - 1). Below it the local index wins;
     above it the global one does. Exact, and undefined at N = 1 because at one
     shard there is no difference to have. */
  function indexCrossover(n) {
    if (n <= 1) return null;
    return R(1n, BigInt(n) - 1n);
  }
  function cheaperIndex(r, w, n) {
    var c = Rcmp(localIndexCost(r, w, n), globalIndexCost(r, w));
    return c < 0 ? 'local' : (c > 0 ? 'global' : 'equal');
  }

  /* ================================================ L11: cross-shard work

     k independently hashed keys all land on one shard with probability
     N^(1-k): the first key picks a shard and the other k-1 have to match it.
     Rpow takes the negative exponent, so this is one call and stays exact. */
  function sameShardProb(k, n) {
    if (k < 1 || n < 1) return null;
    return Rpow(R(BigInt(n), 1n), 1 - k);
  }
  function crossShardProb(k, n) { return Rsub(R(1n, 1n), sameShardProb(k, n)); }
  /* The expected number of distinct shards a k-key transaction touches:
     N(1 - (1 - 1/N)^k), which is how many two-phase participants there are. */
  function expectedShardsTouched(k, n) {
    var nb = R(BigInt(n), 1n);
    return Rmul(nb, Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), Rinv(nb)), k)));
  }
  /* Two-phase commit, itemised: a prepare round trip, a commit round trip,
     and an fsync at each end of each phase. One shard pays none of it. */
  function twoPhaseCost(rtt, fsync) {
    return { rtt: Rmul(R(2n, 1n), rtt), fsync: Rmul(R(2n, 1n), fsync),
             total: Radd(Rmul(R(2n, 1n), rtt), Rmul(R(2n, 1n), fsync)) };
  }
  function meanAddedLatency(k, n, rtt, fsync) {
    return Rmul(crossShardProb(k, n), twoPhaseCost(rtt, fsync).total);
  }

  /* ===================================================== L12: rebalancing

     Moving m of D bytes at a throttled B bytes a second takes m*D/B seconds,
     and the copy is not free while it runs: it takes a share of the node's
     transfer budget, which is capacity the node is no longer serving with. */
  function rebalanceSeconds(fraction, dataBytes, throttleBps) {
    if (Rzero(throttleBps)) return null;
    return Rdiv(Rmul(fraction, dataBytes), throttleBps);
  }
  function movedBytes(fraction, dataBytes) { return Rmul(fraction, dataBytes); }
  /* The share of the node's budget the copy holds, and the service rate left. */
  function stolenShare(throttleBps, budgetBps) {
    if (Rzero(budgetBps)) return null;
    return Rdiv(throttleBps, budgetBps);
  }
  function serviceDuringMove(mu, throttleBps, budgetBps) {
    var stolen = stolenShare(throttleBps, budgetBps);
    if (stolen === null) return null;
    return Rmul(mu, Rsub(R(1n, 1n), stolen));
  }
  /* The utilisation before and during, and the wait C3 L8 reads off each --
     mm1 is the course-3 result, reused rather than restated. */
  function rebalanceLoad(lamNode, mu, throttleBps, budgetBps) {
    var muMove = serviceDuringMove(mu, throttleBps, budgetBps);
    var before = mm1(lamNode, mu);
    var during = muMove === null || Rzero(muMove) ? { stable: false } : mm1(lamNode, muMove);
    return { before: before, during: during, muMove: muMove };
  }
"""

# Every mode ships the same engine: the rationals, the BigInt factorials that
# comb needs, the ceiling, the nearest-rank percentile, the pmf algebra, M/M/1
# for the wait during a rebalance, the seeded stream, the four rounding
# functions, and this kit's own arithmetic on top.
_CORE_JS = (RATIONAL_JS + BIGINT_JS + RCEIL_JS + PERCENTILE_JS + PMF_JS + QUEUE_JS
            + STREAM_JS + APPROX_JS + SHARDKIT_JS)


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the path uses, so a reader
# moving between courses moves between the same widgets.
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


# The sentence every mode that prints an asymptotic has to carry, in the words
# reconciliation #17 requires. Written once so that no page can drift from it.
_STATED_NOTE = (
    "The maximum-load results on this course &mdash; &Theta;(log n / log log n) for one choice "
    "and about ln ln n for two &mdash; are <strong>stated, not proved</strong>: their proofs need "
    "Chernoff bounds, which no subject in this library teaches. What this lab does is "
    "<strong>measure</strong> them. Algorithms <span class=\"tt\">randomised-algorithms / "
    "balls-in-bins</span> states the one-choice result and computes the exact expected number of "
    "colliding pairs and of empty bins, which this page does not."
)

_STREAM_NOTE = (
    "The placement is drawn from an LCG with multiplier 16&nbsp;807, increment 0 and modulus "
    "2&#179;&#185;&nbsp;&minus;&nbsp;1, which is prime &mdash; the generator the rest of this path "
    "uses has modulus 2&#179;&#185;, and the low bits of a power-of-two modulus are a cycle, so "
    "keys taken modulo 8 or 16 from it come out perfectly level. The seed is mixed before it "
    "becomes a state, so seed 4 is not seed 3 rescaled. The same seed draws the same placement "
    "every time this page is opened."
)


# ---------------------------------------------------------------------------
# L1 - count
# ---------------------------------------------------------------------------


def _count(cfg):
    lam = int(cfg.get("peak_rps", 120000))
    per_node = int(cfg.get("node_rps", 8000))
    rho = int(cfg.get("target_rho_pct", 65))
    data_tb = int(cfg.get("data_tb", 48))
    rf = int(cfg.get("replication_factor", 3))
    node_tb = int(cfg.get("node_tb", 4))

    markup = (
        _toolbar(
            "Two constraints, one count",
            "load gives one number, storage gives another, and the answer is the larger",
            [("cyan", "from load"), ("purple", "from storage"), ("amber", "the binding one")],
        )
        + _stage(_svg("scBars", "0 0 520 200", "Two bars, the shard count from load and the shard count from storage, with the binding one marked."))
        + _table("scTable")
        + _banner("scStatus")
    )
    controls = (
        _range("scLam", "Peak load (requests a second)", 10000, 400000, lam, 5000)
        + _range("scNode", "Per-node capacity (requests a second)", 1000, 20000, per_node, 500)
        + _range("scRho", "Target utilisation (per cent)", 20, 95, rho)
        + _range("scData", "Dataset (TB, decimal)", 1, 400, data_tb)
        + _range("scRf", "Replication factor", 1, 5, rf)
        + _range("scNodeTb", "Per-node storage (TB)", 1, 32, node_tb)
        + _kpis(
            [
                ("Shards from load", "scByLoad"),
                ("Shards from storage", "scByStore"),
                ("The count to build", "scPick"),
                ("Which one binds", "scBind"),
                ("Utilisation at that count", "scUtil"),
                ("Bytes a node then holds", "scBytes"),
            ]
        )
        + _hint(
            "scHint",
            "Both counts are ceilings of exact fractions &mdash; &lceil;&lambda;/(c&middot;&rho;)&rceil; "
            "and &lceil;D&middot;RF/per-node&rceil; &mdash; because 23.08 shards is 24 shards. "
            "<em>c</em> here is one node's capacity in requests a second, never a count of servers. "
            "A terabyte is 10&#185;&#178; bytes, which is how a disk is sold.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('scLam'), nodeS = document.getElementById('scNode');
  var rhoS = document.getElementById('scRho'), dataS = document.getElementById('scData');
  var rfS = document.getElementById('scRf'), ntbS = document.getElementById('scNodeTb');
  var bars = document.getElementById('scBars'), table = document.getElementById('scTable');
  var status = document.getElementById('scStatus');
  var TB = 1000000000000n;

  function redraw() {
    var lam = R(BigInt(+lamS.value), 1n), per = R(BigInt(+nodeS.value), 1n);
    var rho = R(BigInt(+rhoS.value), 100n), rf = R(BigInt(+rfS.value), 1n);
    var data = R(BigInt(+dataS.value) * TB, 1n), nodeCap = R(BigInt(+ntbS.value) * TB, 1n);
    document.getElementById('scLamOut').textContent = group(BigInt(+lamS.value)) + ' /s';
    document.getElementById('scNodeOut').textContent = group(BigInt(+nodeS.value)) + ' /s';
    document.getElementById('scRhoOut').textContent = (+rhoS.value) + '%';
    document.getElementById('scDataOut').textContent = (+dataS.value) + ' TB';
    document.getElementById('scRfOut').textContent = '&times;' + (+rfS.value);
    document.getElementById('scNodeTbOut').textContent = (+ntbS.value) + ' TB';

    var byLoad = shardsForLoad(lam, per, rho), byStore = shardsForStorage(data, rf, nodeCap);
    var pick = bindingShards(byLoad, byStore);
    var n = pick.n;

    document.getElementById('scByLoad').textContent = group(byLoad);
    document.getElementById('scByStore').textContent = group(byStore);
    document.getElementById('scPick').textContent = group(n);
    document.getElementById('scBind').textContent = pick.binding === 'both'
      ? 'both, exactly' : (pick.binding === 'load' ? 'load, by ' + group(pick.slack) : 'storage, by ' + group(pick.slack));
    document.getElementById('scUtil').textContent = Rpct(utilisationAt(lam, per, n), 2);
    document.getElementById('scBytes').textContent = byteText(bytesPerNodeAt(data, rf, n));

    var loadRaw = Rdiv(lam, Rmul(per, rho)), storeRaw = Rdiv(Rmul(data, rf), nodeCap);
    table.innerHTML = '<thead><tr><th>constraint</th><th>the fraction</th><th>exactly</th>'
      + '<th>ceiling</th><th>what it leaves at N = ' + group(n) + '</th></tr></thead><tbody>'
      + '<tr><td class="tone-cyan">load</td><td class="tt">&lambda; / (c &middot; &rho;)</td>'
      + '<td class="tt">' + Rtext(loadRaw) + ' = ' + Rfixed(loadRaw, 2) + '</td>'
      + '<td><strong>' + group(byLoad) + '</strong></td>'
      + '<td>each node at ' + Rpct(utilisationAt(lam, per, n), 2) + ' of capacity</td></tr>'
      + '<tr><td class="tone-purple">storage</td><td class="tt">D &middot; RF / per-node</td>'
      + '<td class="tt">' + Rfixed(storeRaw, 2) + '</td>'
      + '<td><strong>' + group(byStore) + '</strong></td>'
      + '<td>each node holding ' + byteText(bytesPerNodeAt(data, rf, n)) + ' of ' + (+ntbS.value) + ' TB</td></tr>'
      + '</tbody>';

    var top = Number(byLoad > byStore ? byLoad : byStore), i;
    var scale = 430 / Math.max(1, top);
    var rows = [['load', byLoad, 'cyan', 40], ['storage', byStore, 'purple', 100]];
    var s = '';
    for (i = 0; i < rows.length; i += 1) {
      var w = Math.max(2, Number(rows[i][1]) * scale), y = rows[i][3];
      var live = (rows[i][1] === n);
      s += '<text x="0" y="' + (y - 6) + '" font-size="11" fill="var(--' + rows[i][2] + ')">'
        + rows[i][0] + ': ' + group(rows[i][1]) + ' shards</text>'
        + '<rect x="0" y="' + y + '" width="' + w + '" height="26" rx="3" fill="var(--' + rows[i][2]
        + ')" opacity="' + (live ? '0.92' : '0.4') + '" />'
        + (live ? '<text x="' + (w + 8) + '" y="' + (y + 18) + '" font-size="11" fill="var(--amber)" '
          + 'font-weight="700">binds</text>' : '');
    }
    s += '<line x1="0" y1="150" x2="520" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="166" font-size="10" fill="var(--muted)">one constraint is satisfied at the '
      + 'count the other demands; the count you build is the larger, and the slack on the other '
      + 'constraint is what you are paying for</text>'
      + '<text x="0" y="182" font-size="10" fill="var(--muted)">bars share one scale, 0 to '
      + group(BigInt(top)) + ' shards</text>';
    bars.innerHTML = s;

    status.innerHTML = 'Load asks for <strong class="tone-cyan">' + group(byLoad) + '</strong> shards and '
      + 'storage asks for <strong class="tone-purple">' + group(byStore) + '</strong>, so you build <strong>'
      + group(n) + '</strong>'
      + (pick.binding === 'both' ? ' &mdash; the one case where neither constraint is slack. '
        : ' and ' + pick.binding + ' is what binds, by ' + group(pick.slack) + ' shards. ')
      + 'At that count each node runs at <strong>' + Rpct(utilisationAt(lam, per, n), 2) + '</strong> of its '
      + group(BigInt(+nodeS.value)) + ' /s and holds <strong>' + byteText(bytesPerNodeAt(data, rf, n))
      + '</strong> of its ' + (+ntbS.value) + ' TB. '
      + (pick.binding === 'storage'
        ? 'Sizing on load alone would have built ' + group(byLoad) + ' and run out of disk.'
        : (pick.binding === 'load'
          ? 'Sizing on storage alone would have built ' + group(byStore) + ' and run out of throughput.'
          : 'Neither constraint has room; a rise in either one adds shards immediately.'));
  }

  [lamS, nodeS, rhoS, dataS, rfS, ntbS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="How many shards",
        subtitle="Load gives one count, storage gives another, and you build the larger",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Size it on both constraints"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both counts are ceilings of exact fractions, recomputed as you move either set of "
            "sliders. Watch which one binds change hands.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - bins
# ---------------------------------------------------------------------------


def _bins(cfg):
    keys = int(cfg.get("keys", 1200))
    shards = int(cfg.get("shards", 12))
    seed = int(cfg.get("seed", 7))

    markup = (
        _toolbar(
            "Hashing does not give equal shards",
            "the same m keys, the same N bins, and a maximum that is not the mean",
            [("cyan", "a shard"), ("red", "the fullest"), ("muted", "the mean")],
        )
        + _stage(_svg("sbHist", "0 0 520 230", "An occupancy histogram of m hashed keys across N shards, with the mean drawn across it and the fullest shard marked."))
        + _table("sbTable")
        + _banner("sbStatus")
    )
    controls = (
        _range("sbKeys", "Keys to place", 60, 6000, keys, 20)
        + _range("sbShards", "Shards", 2, 48, shards)
        + _range("sbSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Mean keys a shard", "sbMean"),
                ("The fullest shard", "sbMax"),
                ("The emptiest", "sbMin"),
                ("max / mean", "sbRatio"),
                ("Excess, in root-means", "sbRoot"),
                ("Shards with nothing", "sbEmpty"),
            ]
        )
        + _hint("sbHint", _STREAM_NOTE + " " + _STATED_NOTE)
    )

    script = _CORE_JS + r"""
  var kS = document.getElementById('sbKeys'), nS = document.getElementById('sbShards');
  var sS = document.getElementById('sbSeed');
  var hist = document.getElementById('sbHist'), table = document.getElementById('sbTable');
  var status = document.getElementById('sbStatus');
  var SEEDS = 8;

  function redraw() {
    var m = +kS.value, n = +nS.value, seed = +sS.value;
    document.getElementById('sbKeysOut').textContent = group(BigInt(m));
    document.getElementById('sbShardsOut').textContent = n;
    document.getElementById('sbSeedOut').textContent = seed;

    var counts = binOccupancy(seed, m, n);
    var mean = R(BigInt(m), BigInt(n)), ratio = maxOverMean(counts);
    document.getElementById('sbMean').textContent = Rfixed(mean, 2);
    document.getElementById('sbMax').textContent = group(BigInt(occMax(counts)));
    document.getElementById('sbMin').textContent = group(BigInt(occMin(counts)));
    document.getElementById('sbRatio').textContent = Rfixed(ratio, 3) + ' (' + Rtext(ratio) + ')';
    document.getElementById('sbRoot').textContent = excessInRootMeansApprox(counts).toFixed(2)
      + ' &radic;mean';
    document.getElementById('sbEmpty').textContent = occEmpty(counts);

    /* One seed is one sample of a maximum. The lesson is about the DISTRIBUTION
       of that maximum, so the table reseeds. */
    var rows = '', i, worst = 0, best = null, sum = R(0n, 1n);
    for (i = 0; i < SEEDS; i += 1) {
      var c = binOccupancy(seed + i, m, n), r = maxOverMean(c);
      sum = Radd(sum, r);
      if (occMax(c) > worst) worst = occMax(c);
      if (best === null || occMax(c) < best) best = occMax(c);
      rows += '<tr' + (i === 0 ? ' class="tone-cyan"' : '') + '><td>' + (seed + i)
        + (i === 0 ? ' &mdash; drawn above' : '') + '</td>'
        + '<td>' + group(BigInt(occMax(c))) + '</td><td>' + group(BigInt(occMin(c))) + '</td>'
        + '<td class="tt">' + Rtext(r) + '</td><td>' + Rfixed(r, 3) + '</td>'
        + '<td>' + occEmpty(c) + '</td></tr>';
    }
    var meanRatio = Rdiv(sum, R(BigInt(SEEDS), 1n));
    table.innerHTML = '<thead><tr><th>seed</th><th>fullest</th><th>emptiest</th>'
      + '<th>max/mean, exactly</th><th>as a decimal</th><th>empty shards</th></tr></thead><tbody>'
      + rows + '</tbody><tfoot><tr><th>mean over ' + SEEDS + ' seeds</th><th>&mdash;</th>'
      + '<th>&mdash;</th><th class="tt">' + Rtext(meanRatio) + '</th><th>'
      + Rfixed(meanRatio, 3) + '</th><th>&mdash;</th></tr></tfoot>';

    var top = Math.max(1, occMax(counts)), bw = 504 / n, s = '', meanY = 186 - (Rnum(mean) / top) * 150;
    for (i = 0; i < n; i += 1) {
      var h = (counts[i] / top) * 150, hot = (counts[i] === occMax(counts));
      s += '<rect x="' + (8 + i * bw + 1) + '" y="' + (186 - h) + '" width="' + Math.max(1, bw - 2)
        + '" height="' + h + '" fill="var(--' + (hot ? 'red' : 'cyan') + ')" opacity="'
        + (hot ? '0.95' : '0.72') + '" />';
      if (n <= 24) {
        s += '<text x="' + (8 + i * bw + bw / 2) + '" y="198" font-size="8" text-anchor="middle" '
          + 'fill="var(--muted)">' + i + '</text>';
      }
    }
    s += '<line x1="8" y1="186" x2="512" y2="186" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="8" y1="' + meanY + '" x2="512" y2="' + meanY + '" stroke="var(--muted)" '
      + 'stroke-width="1" stroke-dasharray="4 4" />'
      + '<text x="8" y="' + (meanY - 4) + '" font-size="10" fill="var(--muted)">mean '
      + Rfixed(mean, 2) + ' keys a shard</text>'
      + '<text x="8" y="14" font-size="11" fill="var(--red)">fullest ' + group(BigInt(occMax(counts)))
      + ', which is ' + Rfixed(ratio, 3) + ' times the mean</text>'
      + '<text x="8" y="214" font-size="10" fill="var(--muted)">' + group(BigInt(m)) + ' keys, '
      + n + ' shards, seed ' + seed + '; every bar is counted, none is modelled</text>'
      + '<text x="8" y="226" font-size="10" fill="var(--muted)">the gap above the mean grows like a '
      + 'square root of the mean, so it shrinks as a PERCENTAGE and grows in keys</text>';
    hist.innerHTML = s;

    var stated = oneChoiceStatedApprox(n);
    status.innerHTML = group(BigInt(m)) + ' keys into ' + n + ' shards leaves a mean of <strong>'
      + Rfixed(mean, 2) + '</strong> and a fullest shard of <strong>' + group(BigInt(occMax(counts)))
      + '</strong> &mdash; max/mean = <strong>' + Rtext(ratio) + '</strong> = ' + Rfixed(ratio, 3)
      + ', and the emptiest holds ' + group(BigInt(occMin(counts))) + '. Over seeds ' + seed
      + '&ndash;' + (seed + SEEDS - 1) + ' the fullest ranges from ' + group(BigInt(best)) + ' to '
      + group(BigInt(worst)) + ', so one run is one sample: the average max/mean is '
      + Rfixed(meanRatio, 3) + '. The excess over the mean is '
      + excessInRootMeansApprox(counts).toFixed(2) + ' root-means, which is the term that does not '
      + 'go away &mdash; sizing every shard at the mean under-provisions the fullest one by '
      + Rpct(Rsub(ratio, R(1n, 1n)), 1) + '.'
      + (isFinite(stated)
        ? ' For n keys into n bins the maximum is &Theta;(log n / log log n), which at n = ' + n
          + ' is about ' + stated.toFixed(2) + ' &mdash; stated, not proved, and rounded.'
        : '');
  }

  [kS, nS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Hash partitioning and imbalance",
        subtitle="Measure max over mean on a seeded placement, then reseed and measure again",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Place the keys and count them"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every bar is a count of keys the seeded stream actually put in that shard. Move the "
            "seed: the histogram changes and the maximum with it, which is the point.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - rehash
# ---------------------------------------------------------------------------


def _rehash(cfg):
    shards = int(cfg.get("shards", 7))
    keys = int(cfg.get("keys", 600))
    seed = int(cfg.get("seed", 11))
    # Ring seed 3 is the preset because at N = 7, V = 1 its joining node takes
    # 12.89% of the ring against an expectation of 12.50% -- a representative
    # draw rather than a flattering one. One token a node is a high-variance
    # ring (seed 5 takes 6.2%, seed 12 takes 30.9%), which is L4's whole subject,
    # so the lab prints this seed's arc, the mean over twelve seeds, and the
    # expectation side by side and the reader can move the slider.
    ring_seed = int(cfg.get("ring_seed", 3))

    markup = (
        _toolbar(
            "What moves when N changes",
            "mod N moves N/(N+1) of the keys and a ring moves 1/(N+1) &mdash; and those are one whole",
            [("red", "moves"), ("green", "stays"), ("muted", "the other scheme")],
        )
        + _stage(_svg("srBars", "0 0 660 210", "Two bars showing the fraction of keys that move under mod-N rehashing and under a consistent-hash ring, adding to one whole."))
        + _table("srTable")
        + _banner("srStatus")
    )
    controls = (
        _range("srShards", "Shards now (N)", 2, 24, shards)
        + _range("srKeys", "Keys in the sample", 60, 3000, keys, 20)
        + _range("srSeed", "Key seed", 1, 60, seed)
        + _range("srRing", "Ring seed", 1, 60, ring_seed)
        + _kpis(
            [
                ("mod N moves, exactly", "srModExact"),
                ("mod N moves, counted", "srModCount"),
                ("A ring moves, in expectation", "srRingExact"),
                ("A ring moves, counted", "srRingCount"),
                ("The two fractions add to", "srSum"),
                ("Keys spared by the ring", "srSpared"),
            ]
        )
        + _hint(
            "srHint",
            "The exact mod-N figure is an <strong>enumeration</strong>, not a sample: over a complete "
            "cycle of N(N+1) consecutive hashes, h mod N equals h mod (N+1) only when both are the "
            "same value below N, and by the Chinese Remainder Theorem each pair of residues occurs "
            "exactly once &mdash; so exactly N of every N(N+1) keys stay. The ring is drawn with one "
            "token a node under successor ownership: a key belongs to the first token at or after it, "
            "going clockwise.",
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('srShards'), kS = document.getElementById('srKeys');
  var sS = document.getElementById('srSeed'), rS = document.getElementById('srRing');
  var bars = document.getElementById('srBars'), table = document.getElementById('srTable');
  var status = document.getElementById('srStatus');
  var ARCSEEDS = 12;

  function redraw() {
    var n = +nS.value, m = +kS.value, seed = +sS.value, ringSeed = +rS.value;
    document.getElementById('srShardsOut').textContent = n + ' → ' + (n + 1);
    document.getElementById('srKeysOut').textContent = group(BigInt(m));
    document.getElementById('srSeedOut').textContent = seed;
    document.getElementById('srRingOut').textContent = ringSeed;

    var cycle = modCycleMoved(n), sample = modSampleMoved(seed, m, n);
    var ringShare = ringMoveShare(n), arc = ringNewNodeArc(ringSeed, n, 1);
    var ringCount = ringSampleMoved(ringSeed, seed, m, n, 1);
    var sum = rehashShareSum(n);

    document.getElementById('srModExact').textContent = Rtext(cycle.share) + ' = '
      + Rpct(cycle.share, 2);
    document.getElementById('srModCount').textContent = group(BigInt(sample.moved)) + ' of '
      + group(BigInt(m)) + ' = ' + Rpct(sample.share, 2);
    document.getElementById('srRingExact').textContent = Rtext(ringShare) + ' = '
      + Rpct(ringShare, 2);
    document.getElementById('srRingCount').textContent = group(BigInt(ringCount.moved)) + ' of '
      + group(BigInt(m)) + ' = ' + Rpct(ringCount.share, 2);
    document.getElementById('srSum').textContent = Rtext(sum);
    document.getElementById('srSpared').textContent = group(BigInt(sample.moved - ringCount.moved))
      + ' of ' + group(BigInt(m));

    /* The first keys, one row each, so the claim is a list and not a summary. */
    var draws = shardStream(seed, m), before = ringTokens(ringSeed, n, 1);
    var after = ringTokens(ringSeed, n + 1, 1), rows = '', i, shown = Math.min(12, m);
    for (i = 0; i < shown; i += 1) {
      var h = draws[i], oldMod = h % n, newMod = h % (n + 1);
      var oldRing = ringOwner(before, h), newRing = ringOwner(after, h);
      rows += '<tr><td class="tt">' + group(BigInt(h)) + '</td>'
        + '<td>' + oldMod + ' &rarr; ' + newMod + '</td>'
        + '<td class="tone-' + (oldMod === newMod ? 'green">stays' : 'red">moves') + '</td>'
        + '<td>' + oldRing + ' &rarr; ' + newRing + '</td>'
        + '<td class="tone-' + (oldRing === newRing ? 'green">stays' : 'red">moves') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>hash</th><th>mod ' + n + ' &rarr; mod ' + (n + 1) + '</th>'
      + '<th></th><th>ring node, before &rarr; after</th><th></th></tr></thead><tbody>' + rows
      + '</tbody><tfoot><tr><th>all ' + group(BigInt(m)) + ' keys</th>'
      + '<th colspan="2">' + group(BigInt(sample.moved)) + ' move (' + Rpct(sample.share, 2) + ')</th>'
      + '<th colspan="2">' + group(BigInt(ringCount.moved)) + ' move (' + Rpct(ringCount.share, 2)
      + ')</th></tr></tfoot>';

    var W = 600, x0 = 46;
    var modW = W * Rnum(cycle.share), ringW = W * Rnum(ringShare);
    var s = '';
    s += '<text x="0" y="22" font-size="11" fill="var(--text)">mod ' + n + '</text>'
      + '<rect x="' + x0 + '" y="10" width="' + modW + '" height="30" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<rect x="' + (x0 + modW) + '" y="10" width="' + (W - modW) + '" height="30" rx="3" fill="var(--green)" opacity="0.75" />'
      + '<text x="' + (x0 + modW / 2) + '" y="30" font-size="12" text-anchor="middle" fill="var(--bg)" '
      + 'font-weight="700">' + Rtext(cycle.share) + ' move</text>'
      + '<text x="' + (x0 + modW + (W - modW) / 2) + '" y="30" font-size="11" text-anchor="middle" '
      + 'fill="var(--bg)">' + Rtext(Rsub(R(1n, 1n), cycle.share)) + '</text>'
      + '<text x="0" y="82" font-size="11" fill="var(--text)">ring</text>'
      + '<rect x="' + x0 + '" y="70" width="' + ringW + '" height="30" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<rect x="' + (x0 + ringW) + '" y="70" width="' + (W - ringW) + '" height="30" rx="3" fill="var(--green)" opacity="0.75" />'
      + '<text x="' + (x0 + ringW + 8) + '" y="90" font-size="12" fill="var(--text)" font-weight="700">'
      + Rtext(ringShare) + ' move &mdash; the rest stay where they are</text>'
      + '<line x1="' + (x0 + modW) + '" y1="4" x2="' + (x0 + modW) + '" y2="116" stroke="var(--muted)" '
      + 'stroke-width="1" stroke-dasharray="3 3" />'
      + '<line x1="' + (x0 + ringW) + '" y1="4" x2="' + (x0 + ringW) + '" y2="116" stroke="var(--muted)" '
      + 'stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="' + x0 + '" y="130" font-size="11" fill="var(--muted)">the red of the top bar and the '
      + 'red of the bottom one are ' + Rtext(cycle.share) + ' and ' + Rtext(ringShare)
      + ', and they add to ' + Rtext(sum) + ' &mdash; one whole, exactly</text>';
    /* The ring itself, small, beside the claim. */
    var cx = 566, cy = 172, rad = 32, j;
    s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + rad + '" fill="none" stroke="var(--line-strong)" stroke-width="2" />';
    for (j = 0; j < after.length; j += 1) {
      var ang = 2 * Math.PI * (after[j].pos / shardModulus()) - Math.PI / 2;
      var joined = after[j].node === n;
      s += '<circle cx="' + (cx + rad * Math.cos(ang)) + '" cy="' + (cy + rad * Math.sin(ang))
        + '" r="' + (joined ? 5 : 3) + '" fill="var(--' + (joined ? 'red' : 'cyan') + ')" />';
    }
    s += '<text x="' + (cx - 96) + '" y="' + (cy - 18) + '" font-size="10" fill="var(--muted)">the ring, '
      + (n + 1) + ' tokens;</text>'
      + '<text x="' + (cx - 96) + '" y="' + (cy - 6) + '" font-size="10" fill="var(--red)">the joining one took '
      + Rpct(arc, 2) + '</text>'
      + '<text x="' + (cx - 96) + '" y="' + (cy + 6) + '" font-size="10" fill="var(--muted)">of the ring on this seed;</text>'
      + '<text x="' + (cx - 96) + '" y="' + (cy + 18) + '" font-size="10" fill="var(--muted)">over '
      + ARCSEEDS + ' seeds it averages ' + Rpct(ringArcMeanApprox(ringSeed, n, 1, ARCSEEDS), 2) + '</text>'
      + '<text x="0" y="' + (cy + 34) + '" font-size="10" fill="var(--muted)">one token a node is a '
      + 'high-variance ring: the arc a joining node takes has expectation 1/(N+1) and a very long '
      + 'tail. Virtual nodes are the next lesson.</text>';
    bars.innerHTML = s;

    status.innerHTML = 'Going from <strong>' + n + '</strong> shards to <strong>' + (n + 1)
      + '</strong>, mod-N rehashing moves <strong>' + Rtext(cycle.share) + '</strong> of the keys '
      + '&mdash; that is an enumeration over the ' + group(BigInt(cycle.total)) + ' hashes of a '
      + 'complete cycle, not an estimate &mdash; and the ' + group(BigInt(m)) + '-key sample above '
      + 'moved ' + group(BigInt(sample.moved)) + ', or ' + Rpct(sample.share, 2) + '. A ring moves '
      + '<strong>' + Rtext(ringShare) + '</strong> in expectation and moved ' + group(BigInt(ringCount.moved))
      + ' of the same keys here, because the joining node took ' + Rpct(arc, 2) + ' of the ring on '
      + 'this seed. <strong>' + Rtext(cycle.share) + ' + ' + Rtext(ringShare) + ' = ' + Rtext(sum)
      + '</strong>: the keys mod-N moves and the keys a ring moves are the whole key set between '
      + 'them, which is the entire argument for consistent hashing in one line. The intuition that '
      + 'adding a node moves 1/N of the keys is wrong by a factor of about N.';
  }

  [nS, kS, sS, rS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Rehashing when N changes",
        subtitle="Count the keys that move, both ways, and watch the two fractions add to one",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Add one shard"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every key's old home and new home is computed under both schemes and the moved ones "
            "are counted. The mod-N fraction is exact by enumeration; the ring's is exact for the "
            "ring this seed drew.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - vnodes
# ---------------------------------------------------------------------------


def _vnodes(cfg):
    nodes = int(cfg.get("nodes", 8))
    vnodes = int(cfg.get("vnodes", 1))
    seed = int(cfg.get("seed", 5))

    markup = (
        _toolbar(
            "A node owns an arc, not a share",
            "one token a node is a ring that does not balance; V tokens shrink the spread like 1/&radic;V",
            [("cyan", "a node's arcs"), ("red", "the largest share"), ("muted", "an equal share")],
        )
        + _stage(_svg("svRing", "0 0 660 250", "A consistent-hash ring with each node's tokens and arcs drawn, beside the share each node ends up owning."))
        + _table("svTable")
        + _banner("svStatus")
    )
    controls = (
        _range("svNodes", "Nodes", 3, 16, nodes)
        + _range("svV", "Virtual nodes a node (V)", 1, 200, vnodes)
        + _range("svSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Largest share", "svMax"),
                ("Smallest share", "svMin"),
                ("max / mean", "svRatio"),
                ("Relative spread, measured", "svSpread"),
                ("1 / &radic;V, the stated rate", "svRate"),
                ("Shares add to", "svTotal"),
            ]
        )
        + _hint(
            "svHint",
            "Each node's share is the total of the arcs its tokens own &mdash; an exact fraction of "
            "the ring, and the shares add to 1 by construction. The relative spread is the root mean "
            "square of (share &times; N &minus; 1) across the nodes, which is the quantity that falls "
            "like 1/&radic;V; the maximum of N draws is far too noisy at one seed to show a rate, so "
            "the table averages over seeds. The rate itself is <strong>stated</strong>, and the "
            "square root is <strong>rounded</strong> &mdash; Newton from a rational start. " + _STREAM_NOTE,
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('svNodes'), vS = document.getElementById('svV');
  var sS = document.getElementById('svSeed');
  var ring = document.getElementById('svRing'), table = document.getElementById('svTable');
  var status = document.getElementById('svStatus');
  var LADDER = [1, 10, 100], SEEDS = 8;
  var TONE = ['cyan', 'purple', 'green', 'amber', 'blue', 'red', 'muted', 'cyan',
              'purple', 'green', 'amber', 'blue', 'red', 'muted', 'cyan', 'purple'];

  function redraw() {
    var n = +nS.value, v = +vS.value, seed = +sS.value;
    document.getElementById('svNodesOut').textContent = n;
    document.getElementById('svVOut').textContent = v + (v === 1 ? ' token a node' : ' tokens a node');
    document.getElementById('svSeedOut').textContent = seed;

    var shares = ringShares(seed, n, v);
    var mx = shareMaxOverMean(shares), mn = shareMinOverMean(shares);
    var spread = spreadRmsApprox(shares);
    var topShare = Rdiv(mx, R(BigInt(n), 1n));       /* max/mean back to a share of the ring */
    document.getElementById('svMax').textContent = Rpct(topShare, 2)
      + ' (' + Rfixed(mx, 3) + ' &times; mean)';
    document.getElementById('svMin').textContent = Rpct(Rdiv(mn, R(BigInt(n), 1n)), 2)
      + ' (' + Rfixed(mn, 3) + ' &times; mean)';
    document.getElementById('svRatio').textContent = Rfixed(mx, 4);
    document.getElementById('svSpread').textContent = spread.toFixed(4);
    document.getElementById('svRate').textContent = spreadRateStatedApprox(v).toFixed(4);
    document.getElementById('svTotal').textContent = Rtext(shareTotal(shares));

    var rows = '', i, base = null;
    for (i = 0; i < LADDER.length; i += 1) {
      var vv = LADDER[i];
      var rms = spreadRmsOverSeedsApprox(seed, n, vv, SEEDS);
      var mm = maxOverMeanOverSeedsApprox(seed, n, vv, SEEDS);
      if (base === null) base = rms;
      rows += '<tr' + (vv === v ? ' class="tone-cyan"' : '') + '><td>V = ' + vv + '</td>'
        + '<td>' + (n * vv) + '</td>'
        + '<td>' + mm.toFixed(3) + '</td>'
        + '<td>' + rms.toFixed(4) + '</td>'
        + '<td>' + spreadRateStatedApprox(vv).toFixed(4) + '</td>'
        + '<td>' + (base > 0 ? (rms / base).toFixed(3) : '&mdash;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>virtual nodes</th><th>tokens on the ring</th>'
      + '<th>max/mean, mean of ' + SEEDS + ' seeds</th><th>relative spread, measured</th>'
      + '<th>1/&radic;V, stated</th><th>spread against V = 1</th></tr></thead><tbody>' + rows
      + '</tbody>';

    /* The ring on the left, the shares as a bar column on the right. */
    var cx = 150, cy = 124, rad = 96, tokens = ringTokens(seed, n, v), s = '', j;
    var M = shardModulus();
    for (j = 0; j < tokens.length; j += 1) {
      var prev = j === 0 ? tokens[tokens.length - 1].pos - M : tokens[j - 1].pos;
      var a0 = 2 * Math.PI * (prev / M) - Math.PI / 2;
      var a1 = 2 * Math.PI * (tokens[j].pos / M) - Math.PI / 2;
      var large = (a1 - a0) > Math.PI ? 1 : 0;
      s += '<path d="M ' + (cx + rad * Math.cos(a0)) + ' ' + (cy + rad * Math.sin(a0))
        + ' A ' + rad + ' ' + rad + ' 0 ' + large + ' 1 ' + (cx + rad * Math.cos(a1)) + ' '
        + (cy + rad * Math.sin(a1)) + '" fill="none" stroke="var(--' + TONE[tokens[j].node % TONE.length]
        + ')" stroke-width="9" opacity="0.85" />';
      if (tokens.length <= 40) {
        s += '<circle cx="' + (cx + rad * Math.cos(a1)) + '" cy="' + (cy + rad * Math.sin(a1))
          + '" r="2.5" fill="var(--text)" />';
      }
    }
    s += '<text x="' + cx + '" y="' + (cy - 4) + '" font-size="11" text-anchor="middle" fill="var(--muted)">'
      + (n * v) + ' tokens</text>'
      + '<text x="' + cx + '" y="' + (cy + 12) + '" font-size="11" text-anchor="middle" fill="var(--muted)">'
      + n + ' nodes, V = ' + v + '</text>'
      + '<text x="8" y="14" font-size="11" fill="var(--muted)">a key belongs to the first token at or '
      + 'after it, clockwise</text>';

    var bx = 300, bw = 336, i2;
    var top = Rnum(shareMaxOverMean(shares)) / n;
    for (i2 = 0; i2 < n; i2 += 1) {
      var frac = Rnum(shares[i2]), y = 28 + i2 * Math.min(20, 190 / n);
      var w = (frac / top) * bw, hot = Rcmp(Rmul(shares[i2], R(BigInt(n), 1n)), mx) === 0;
      s += '<rect x="' + bx + '" y="' + y + '" width="' + Math.max(1, w) + '" height="'
        + Math.max(4, Math.min(14, 150 / n)) + '" rx="2" fill="var(--' + (hot ? 'red' : 'cyan')
        + ')" opacity="' + (hot ? '0.95' : '0.7') + '" />'
        + (n <= 12 ? '<text x="' + (bx + w + 6) + '" y="' + (y + 10) + '" font-size="9" '
          + 'fill="var(--muted)">' + Rpct(shares[i2], 2) + '</text>' : '');
    }
    var evenX = bx + ((1 / n) / top) * bw;
    s += '<line x1="' + evenX + '" y1="20" x2="' + evenX + '" y2="' + (28 + n * Math.min(20, 190 / n))
      + '" stroke="var(--muted)" stroke-width="1" stroke-dasharray="4 4" />'
      + '<text x="' + (evenX + 4) + '" y="18" font-size="10" fill="var(--muted)">an equal share, '
      + Rpct(R(1n, BigInt(n)), 2) + '</text>'
      + '<text x="' + bx + '" y="238" font-size="10" fill="var(--muted)">max/mean = '
      + Rfixed(mx, 3) + ', relative spread ' + spread.toFixed(4) + ' against a stated 1/&radic;V = '
      + spreadRateStatedApprox(v).toFixed(4) + '</text>';
    ring.innerHTML = s;

    status.innerHTML = 'With <strong>' + n + '</strong> nodes and <strong>V = ' + v + '</strong> the '
      + 'largest node owns <strong>' + Rpct(topShare, 2)
      + '</strong> of the ring against an equal share of ' + Rpct(R(1n, BigInt(n)), 2)
      + ' &mdash; max/mean = <strong>' + Rfixed(mx, 3) + '</strong>, and the smallest owns '
      + Rfixed(mn, 3) + ' of the mean. The shares add to ' + Rtext(shareTotal(shares))
      + ', so nothing is missing; they are simply not equal. Across ' + SEEDS + ' seeds the measured '
      + 'relative spread is ' + spreadRmsOverSeedsApprox(seed, n, 1, SEEDS).toFixed(4) + ' at V = 1, '
      + spreadRmsOverSeedsApprox(seed, n, 10, SEEDS).toFixed(4) + ' at V = 10 and '
      + spreadRmsOverSeedsApprox(seed, n, 100, SEEDS).toFixed(4) + ' at V = 100, against the stated '
      + '1/&radic;V of 1.0000, 0.3162 and 0.1000. A ring does not balance by itself; V tokens are '
      + 'what makes it balance, and they buy the spread down by a square root, not by a factor of V.';
  }

  [nS, vS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Consistent hashing and virtual nodes",
        subtitle="A node's share is the arc it owns, and V tokens shrink the spread like 1/√V",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Give each node more tokens"),
        panel_intro=cfg.get(
            "panel_intro",
            "The ring is drawn from a seeded stream and each node's share is the exact fraction of "
            "the ring its arcs cover. Take V from 1 to 100 and watch the spread fall &mdash; slowly.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - range
# ---------------------------------------------------------------------------


def _range_mode(cfg):
    pattern = cfg.get("pattern", "monotonic")
    ranges = int(cfg.get("ranges", 8))
    writes = int(cfg.get("writes", 2400))
    buckets = int(cfg.get("buckets", 4))
    seed = int(cfg.get("seed", 5))
    if pattern not in ("monotonic", "hashed", "prefixed"):
        raise ValueError("shard range mode: unknown key pattern %r" % (pattern,))

    markup = (
        _toolbar(
            "Ranges keep locality and lose balance",
            "a monotonic key is perfectly balanced over all time and completely unbalanced at every instant of it",
            [("red", "the hottest range now"), ("cyan", "the others"), ("muted", "an equal share")],
        )
        + _stage(_svg("sgGrid", "0 0 660 240", "The write distribution across ranges in each of several time windows, for the chosen key pattern."))
        + _table("sgTable")
        + _banner("sgStatus")
    )
    controls = (
        _select(
            "sgPattern",
            "Key pattern",
            [
                ("monotonic", "a timestamp or an auto-increment id"),
                ("hashed", "the hash of the id"),
                ("prefixed", "a hashed bucket, then the timestamp"),
            ],
            pattern,
        )
        + _range("sgRanges", "Ranges (shards)", 2, 16, ranges)
        + _range("sgWrites", "Writes in the run", 400, 8000, writes, 200)
        + _range("sgBuckets", "Buckets in the prefix", 1, 16, buckets)
        + _range("sgSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Hottest range, right now", "sgNow"),
                ("Hottest range, over the run", "sgLife"),
                ("An equal share would be", "sgEven"),
                ("The hottest is over it by", "sgOver"),
                ("Ranges a one-window scan reads", "sgScan"),
                ("Ranges taking writes now", "sgLive"),
            ]
        )
        + _hint(
            "sgHint",
            "Every cell is a count of writes that pattern actually put in that range in that window. "
            "The trap is the second figure: over the whole run a monotonic key is spread perfectly "
            "evenly across the ranges, and at no instant during it was more than one range taking "
            "anything. The bucket prefix is the remedy and it costs the scan: one window of time is "
            "one range under a timestamp, all N under a hash, and as many as there are buckets under "
            "the prefix. " + _STREAM_NOTE,
        )
    )

    script = _CORE_JS + r"""
  var pSel = document.getElementById('sgPattern'), nS = document.getElementById('sgRanges');
  var wS = document.getElementById('sgWrites'), bS = document.getElementById('sgBuckets');
  var sS = document.getElementById('sgSeed');
  var gridEl = document.getElementById('sgGrid'), table = document.getElementById('sgTable');
  var status = document.getElementById('sgStatus');
  var WINDOWS = 8;

  function redraw() {
    var pattern = pSel.value, n = +nS.value, m = +wS.value, b = +bS.value, seed = +sS.value;
    document.getElementById('sgRangesOut').textContent = n;
    document.getElementById('sgWritesOut').textContent = group(BigInt(m));
    document.getElementById('sgBucketsOut').textContent = pattern === 'prefixed'
      ? b + (b === 1 ? ' bucket' : ' buckets') : 'unused by this pattern';
    document.getElementById('sgSeedOut').textContent = seed;

    var grid = rangeWindows(pattern, m, n, WINDOWS, seed, b);
    var worst = worstWindowShare(grid), life = lifetimeShare(grid);
    var even = R(1n, BigInt(n)), scan = scanRanges(pattern, n, b);
    var lastRow = grid[grid.length - 1], live = 0, i, w;
    for (i = 0; i < n; i += 1) if (lastRow[i] > 0) live += 1;

    document.getElementById('sgNow').textContent = Rpct(worst, 2) + ' of that window';
    document.getElementById('sgLife').textContent = Rpct(life, 2) + ' of all writes';
    document.getElementById('sgEven').textContent = Rpct(even, 2);
    document.getElementById('sgOver').textContent = Rfixed(Rdiv(worst, even), 2) + '&times;';
    document.getElementById('sgScan').textContent = scan + ' of ' + n;
    document.getElementById('sgLive').textContent = live + ' of ' + n;

    var rows = '';
    for (w = 0; w < grid.length; w += 1) {
      var cells = '';
      for (i = 0; i < n; i += 1) {
        var hot = grid[w][i] === occMax(grid[w]) && grid[w][i] > 0;
        cells += '<td class="' + (grid[w][i] === 0 ? 'tone-muted' : (hot ? 'tone-red' : 'tone-cyan'))
          + '">' + (grid[w][i] === 0 ? '&middot;' : group(BigInt(grid[w][i]))) + '</td>';
      }
      rows += '<tr><td>window ' + (w + 1) + '</td>' + cells + '<td>'
        + Rpct(hottestShare(grid[w]), 1) + '</td></tr>';
    }
    var head = '';
    for (i = 0; i < n; i += 1) head += '<th>r' + i + '</th>';
    table.innerHTML = '<thead><tr><th>time</th>' + head + '<th>hottest</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var top = 1, s = '';
    for (w = 0; w < grid.length; w += 1) if (occMax(grid[w]) > top) top = occMax(grid[w]);
    var cw = Math.min(72, 600 / n), ch = 22;
    for (w = 0; w < grid.length; w += 1) {
      for (i = 0; i < n; i += 1) {
        var v = grid[w][i], hot2 = (v === occMax(grid[w]) && v > 0);
        s += '<rect x="' + (46 + i * cw) + '" y="' + (18 + w * ch) + '" width="' + (cw - 2)
          + '" height="' + (ch - 3) + '" rx="2" fill="var(--' + (hot2 ? 'red' : 'cyan')
          + ')" opacity="' + (v === 0 ? '0.08' : (0.18 + 0.8 * (v / top))) + '" />';
      }
      s += '<text x="0" y="' + (33 + w * ch) + '" font-size="9" fill="var(--muted)">t' + (w + 1) + '</text>';
    }
    for (i = 0; i < n && n <= 16; i += 1) {
      s += '<text x="' + (46 + i * cw + (cw - 2) / 2) + '" y="14" font-size="9" text-anchor="middle" '
        + 'fill="var(--muted)">r' + i + '</text>';
    }
    s += '<text x="0" y="' + (18 + WINDOWS * ch + 18) + '" font-size="11" fill="var(--text)">'
      + (pattern === 'monotonic'
        ? 'a monotonic key: every write in a window lands in ONE range, and the range marches right'
        : (pattern === 'hashed'
          ? 'a hashed key: every window fills every range, and a time-range scan has to read all ' + n
          : 'a bucket prefix: ' + Math.max(1, Math.min(n, b)) + ' ranges take writes at a time, and a '
            + 'scan reads those ' + Math.max(1, Math.min(n, b)) + ' rather than 1 or ' + n))
      + '</text>'
      + '<text x="0" y="' + (18 + WINDOWS * ch + 34) + '" font-size="10" fill="var(--muted)">'
      + 'hottest range in the worst window: ' + Rpct(worst, 1) + ' of that window&rsquo;s writes; '
      + 'over the whole run the hottest range holds ' + Rpct(life, 1) + ', against an equal share of '
      + Rpct(even, 1) + '</text>'
      + '<text x="0" y="' + (18 + WINDOWS * ch + 48) + '" font-size="10" fill="var(--muted)">'
      + 'shade is writes in that cell, 0 to ' + group(BigInt(top)) + '; ' + group(BigInt(m))
      + ' writes over ' + WINDOWS + ' windows</text>';
    gridEl.innerHTML = s;

    status.innerHTML = (pattern === 'monotonic'
        ? 'A timestamp key sends <strong>' + Rpct(worst, 2) + '</strong> of the writes happening now '
          + 'to one range, whatever N is &mdash; and over the whole run that same range holds only '
          + Rpct(life, 2) + ', which is why a lifetime histogram makes this look healthy. The range '
          + 'that is hot moves, but there is always exactly one.'
        : (pattern === 'hashed'
          ? 'Hashing the key brings the hottest range down to <strong>' + Rpct(worst, 2)
            + '</strong> of the current writes against an equal share of ' + Rpct(even, 2)
            + ' &mdash; balanced, and it has thrown the ordering away: a scan of one window of time '
            + 'now reads all ' + n + ' ranges instead of one.'
          : 'A hashed bucket in front of the timestamp spreads the current writes over '
            + Math.max(1, Math.min(n, b)) + ' ranges, so the hottest takes <strong>' + Rpct(worst, 2)
            + '</strong> instead of everything, and a scan of one window reads those '
            + Math.max(1, Math.min(n, b)) + ' ranges rather than all ' + n + '. That is the trade '
            + 'stated in one number: balance costs fan-out, and the bucket count is the dial.'))
      + ' The hottest range is <strong>' + Rfixed(Rdiv(worst, even), 2) + ' times</strong> an equal '
      + 'share right now, and ' + live + ' of ' + n + ' ranges are taking any writes at all.';
  }

  pSel.addEventListener('change', redraw);
  [nS, wS, bS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Range partitioning and hot ranges",
        subtitle="The hottest range's share of the writes happening now, not of the writes ever",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose what the key is"),
        panel_intro=cfg.get(
            "panel_intro",
            "The grid is one row per window of time and one column per range, and every cell is "
            "counted. Switch the pattern and watch the lifetime figure stay put while the instant "
            "one collapses.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - hotkey
# ---------------------------------------------------------------------------


def _hotkey(cfg):
    lam = int(cfg.get("rps", 100000))
    hot_pct = int(cfg.get("hot_pct", 12))
    shards = int(cfg.get("shards", 16))
    salt = int(cfg.get("salt", 8))

    markup = (
        _toolbar(
            "A hot key does not care about N",
            "f&middot;&lambda; has no N in it, so the curve flattens instead of falling",
            [("red", "the hottest shard"), ("muted", "the mean shard"), ("amber", "after salting")],
        )
        + _stage(_svg("shCurve", "0 0 660 250", "The hottest shard's load drawn against the shard count, flattening onto the hot key's own traffic, with the salted curve beneath it."))
        + _table("shTable")
        + _banner("shStatus")
    )
    controls = (
        _range("shLam", "Total load (requests a second)", 1000, 500000, lam, 1000)
        + _range("shF", "The hot key's share (per cent)", 0, 60, hot_pct)
        + _range("shN", "Shards", 1, 64, shards)
        + _range("shS", "Salt the hot key into", 1, 64, salt)
        + _kpis(
            [
                ("Hottest shard now", "shHot"),
                ("An average shard", "shMean"),
                ("Imbalance", "shImb"),
                ("What no N gets below", "shFloor"),
                ("Hottest after salting", "shSalted"),
                ("Reads the salt costs", "shCost"),
            ]
        )
        + _hint(
            "shHint",
            "The hottest shard carries f&middot;&lambda; + (1&minus;f)&lambda;/N: its first term has "
            "no N in it at all, so doubling the shard count halves only the second. Salting the key "
            "into s pieces divides the first term by s and multiplies every read of that key by s "
            "&mdash; a fan-out, paid on the read path, which is the only thing that moves the floor.",
        )
    )

    script = _CORE_JS + r"""
  var lamS = document.getElementById('shLam'), fS = document.getElementById('shF');
  var nS = document.getElementById('shN'), sS = document.getElementById('shS');
  var curve = document.getElementById('shCurve'), table = document.getElementById('shTable');
  var status = document.getElementById('shStatus');
  var LADDER = [1, 2, 4, 8, 16, 32, 64, 128, 256, 1024];

  function redraw() {
    var lam = R(BigInt(+lamS.value), 1n), f = R(BigInt(+fS.value), 100n);
    var n = +nS.value, s = +sS.value;
    document.getElementById('shLamOut').textContent = group(BigInt(+lamS.value)) + ' /s';
    document.getElementById('shFOut').textContent = (+fS.value) + '%';
    document.getElementById('shNOut').textContent = n;
    document.getElementById('shSOut').textContent = s + (s === 1 ? ' piece (no salt)' : ' pieces');

    var hot = hottestLoad(lam, f, n), mean = meanLoad(lam, n);
    var salted = hottestLoadSalted(lam, f, n, s), floor = hotAsymptote(lam, f);
    document.getElementById('shHot').textContent = Rfixed(hot, 0) + ' /s';
    document.getElementById('shMean').textContent = Rfixed(mean, 0) + ' /s';
    document.getElementById('shImb').textContent = Rfixed(hotImbalance(lam, f, n), 2) + '&times; the mean';
    document.getElementById('shFloor').textContent = Rfixed(floor, 0) + ' /s';
    document.getElementById('shSalted').textContent = Rfixed(salted, 0) + ' /s';
    document.getElementById('shCost').textContent = Rfixed(saltReadAmplification(f, s), 2)
      + '&times; reads overall';

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var nn = LADDER[i];
      var h = hottestLoad(lam, f, nn), sl = hottestLoadSalted(lam, f, nn, s);
      rows += '<tr' + (nn === n ? ' class="tone-cyan"' : '') + '><td>' + group(BigInt(nn)) + '</td>'
        + '<td>' + Rfixed(meanLoad(lam, nn), 0) + '</td>'
        + '<td class="tone-red">' + Rfixed(h, 0) + '</td>'
        + '<td>' + Rfixed(hotImbalance(lam, f, nn), 2) + '&times;</td>'
        + '<td class="tone-amber">' + Rfixed(sl, 0) + '</td>'
        + '<td>' + Rfixed(Rsub(h, floor), 0) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>shards</th><th>mean shard</th><th>hottest shard</th>'
      + '<th>imbalance</th><th>hottest, salted ' + s + '</th><th>above the floor by</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    /* The curve against N, drawn from the formula at every N on the axis. */
    var MAXN = 64, x0 = 44, x1 = 640, y0 = 200, y1 = 24, i2;
    var top = Rnum(hottestLoad(lam, f, 1));
    if (top <= 0) top = 1;
    function px(nn) { return x0 + (x1 - x0) * (nn - 1) / (MAXN - 1); }
    function py(val) { return y0 - (y0 - y1) * Math.min(1, val / top); }
    var hotPath = '', meanPath = '', saltPath = '';
    for (i2 = 1; i2 <= MAXN; i2 += 1) {
      hotPath += (i2 === 1 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(hottestLoad(lam, f, i2)));
      meanPath += (i2 === 1 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(meanLoad(lam, i2)));
      saltPath += (i2 === 1 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(hottestLoadSalted(lam, f, i2, s)));
    }
    var floorY = py(Rnum(floor));
    var g = '<line x1="' + x0 + '" y1="' + y0 + '" x2="' + x1 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + y1 + '" x2="' + x0 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + floorY + '" x2="' + x1 + '" y2="' + floorY
      + '" stroke="var(--red)" stroke-width="1" stroke-dasharray="5 4" opacity="0.7" />'
      + '<text x="' + (x0 + 6) + '" y="' + (floorY - 5) + '" font-size="10" fill="var(--red)">'
      + 'f&middot;&lambda; = ' + Rfixed(floor, 0) + ' /s &mdash; the hot key&rsquo;s own traffic, which no N touches</text>'
      + '<path d="' + meanPath + '" fill="none" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="4 3" />'
      + '<path d="' + saltPath + '" fill="none" stroke="var(--amber)" stroke-width="2" />'
      + '<path d="' + hotPath + '" fill="none" stroke="var(--red)" stroke-width="2.4" />'
      + '<circle cx="' + px(Math.min(MAXN, n)) + '" cy="' + py(Rnum(hot)) + '" r="4" fill="var(--red)" />'
      + '<circle cx="' + px(Math.min(MAXN, n)) + '" cy="' + py(Rnum(salted)) + '" r="4" fill="var(--amber)" />'
      + '<text x="' + x0 + '" y="' + (y1 - 8) + '" font-size="11" fill="var(--muted)">'
      + 'requests a second on the busiest shard, 0 to ' + Rfixed(R(BigInt(Math.round(top)), 1n), 0) + '</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 14) + '" font-size="10" fill="var(--muted)">1 shard</text>'
      + '<text x="' + x1 + '" y="' + (y0 + 14) + '" font-size="10" text-anchor="end" fill="var(--muted)">'
      + MAXN + ' shards</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 30) + '" font-size="10" fill="var(--muted)">'
      + 'the dashed grey line is the mean shard, which does fall like 1/N; the red one is the '
      + 'hottest, which does not</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 44) + '" font-size="10" fill="var(--amber)">'
      + 'the amber line is the same system with the hot key split into ' + s + ' &mdash; the floor '
      + 'moved to ' + Rfixed(Rdiv(floor, R(BigInt(s), 1n)), 0) + ' /s, at ' + s + ' reads a read</text>';
    curve.innerHTML = g;

    var target = saltForTarget(lam, f, n, R(3n, 2n));
    status.innerHTML = 'At <strong>' + n + '</strong> shards the hottest one carries <strong>'
      + Rfixed(hot, 0) + ' /s</strong> against an average shard&rsquo;s ' + Rfixed(mean, 0)
      + ' &mdash; <strong>' + Rfixed(hotImbalance(lam, f, n), 2) + ' times</strong> the mean. '
      + 'Doubling to ' + (2 * n) + ' shards makes it ' + Rfixed(hottestLoad(lam, f, 2 * n), 0)
      + ' /s and a thousand shards makes it ' + Rfixed(hottestLoad(lam, f, 1024), 0) + ' /s, because '
      + 'f&middot;&lambda; = <strong>' + Rfixed(floor, 0) + ' /s</strong> is a floor no shard count '
      + 'reaches under. Salting the key into ' + s + ' brings the hottest shard to <strong>'
      + Rfixed(salted, 0) + ' /s</strong> &mdash; the hot term becomes f/s &mdash; and every read of '
      + 'that key now fans out to ' + s + ' shards, which is '
      + Rfixed(saltReadAmplification(f, s), 2) + ' times the reads overall. '
      + (target === null
        ? 'No salt below 4 096 brings this shard within 1.5 times the mean: the uniform term alone is already past it.'
        : 'A salt of ' + target + ' would bring it within 1.5 times the mean.');
  }

  [lamS, fS, nS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Hot keys and salting",
        subtitle="f·λ + (1−f)λ/N, and the first term is not a function of N",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Make one key hot"),
        panel_intro=cfg.get(
            "panel_intro",
            "The curve is evaluated from the formula at every shard count on the axis, so raising the "
            "hot key's share bends it flat in front of you. Then salt it and watch the floor drop.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - straggler
# ---------------------------------------------------------------------------


def _straggler(cfg):
    pmf = cfg.get("pmf", "20:900, 40:70, 120:25, 400:5")
    partitions = int(cfg.get("partitions", 24))

    markup = (
        _toolbar(
            "A job ends with its slowest partition",
            "the maximum of N draws, enumerated exactly &mdash; not simulated",
            [("cyan", "one partition"), ("red", "the maximum of N"), ("muted", "the mean")],
        )
        + _stage(_svg("ssDist", "0 0 660 240", "The distribution of one partition's time and the distribution of the maximum of N of them, drawn as two bar rows."))
        + _table("ssTable")
        + _banner("ssStatus")
    )
    controls = (
        _text("ssPmf", "Partition times (ms:weight)", pmf)
        + _range("ssN", "Partitions", 1, 128, partitions)
        + _kpis(
            [
                ("One partition, mean", "ssOneMean"),
                ("One partition, p99", "ssOneP99"),
                ("The job, mean", "ssJobMean"),
                ("The job, p99", "ssJobP99"),
                ("The straggler tax", "ssTax"),
                ("P(one of them is slow)", "ssAny"),
            ]
        )
        + _hint(
            "ssHint",
            "P(max &le; t) = F(t)<sup>N</sup>, differenced back into a distribution: the whole thing "
            "is enumerated exactly from the weights you typed, with rational probabilities, so nothing "
            "here is sampled. The percentile is nearest-rank &mdash; the smallest time the "
            "distribution puts at least that much mass at or below, which is a time a partition "
            "actually takes rather than an interpolation between two.",
        )
    )

    script = _CORE_JS + r"""
  var pIn = document.getElementById('ssPmf'), nS = document.getElementById('ssN');
  var dist = document.getElementById('ssDist'), table = document.getElementById('ssTable');
  var status = document.getElementById('ssStatus');
  var LADDER = [1, 2, 4, 8, 16, 32, 64, 128];
  var Q99 = R(99n, 100n), Q50 = R(1n, 2n), Q90 = R(9n, 10n);

  function redraw() {
    var n = +nS.value;
    document.getElementById('ssNOut').textContent = n;
    var pmf = parsePmf(pIn.value);
    if (pmf === null) {
      dist.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">Each entry is '
        + 'time:weight, separated by commas &mdash; for example 20:900, 40:70, 120:25, 400:5.</text>';
      table.innerHTML = '';
      status.innerHTML = 'That is not a distribution yet. Times are whole milliseconds and weights '
        + 'are non-negative; the weights are normalised for you, so they need not add to anything.';
      ['ssOneMean', 'ssOneP99', 'ssJobMean', 'ssJobP99', 'ssTax', 'ssAny'].forEach(function (id) {
        document.getElementById(id).innerHTML = '&mdash;';
      });
      return;
    }
    var job = pmfMax(pmf, n), worst = pmfWorst(pmf);
    var tax = stragglerTax(pmf, n);
    document.getElementById('ssOneMean').textContent = Rfixed(pmfMean(pmf), 2) + ' ms';
    document.getElementById('ssOneP99').textContent = pmfQuantile(pmf, Q99) + ' ms';
    document.getElementById('ssJobMean').textContent = Rfixed(pmfMean(job), 2) + ' ms';
    document.getElementById('ssJobP99').textContent = pmfQuantile(job, Q99) + ' ms';
    document.getElementById('ssTax').textContent = tax.ratio === null ? '&mdash;'
      : Rfixed(tax.ratio, 2) + '&times; one partition';
    var slow = pmfQuantile(pmf, Q99);          /* "slow" means a single partition's own p99 */
    document.getElementById('ssAny').textContent = Rpct(anySlowerThan(pmf, n, slow), 2)
      + ' past ' + slow + ' ms';

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var nn = LADDER[i], j = pmfMax(pmf, nn);
      rows += '<tr' + (nn === n ? ' class="tone-cyan"' : '') + '><td>' + nn + '</td>'
        + '<td>' + Rfixed(pmfMean(j), 2) + '</td>'
        + '<td>' + pmfQuantile(j, Q50) + '</td>'
        + '<td>' + pmfQuantile(j, Q90) + '</td>'
        + '<td class="tone-red">' + pmfQuantile(j, Q99) + '</td>'
        + '<td>' + Rpct(pmfTail(j, slow), 2) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>partitions</th><th>job mean (ms)</th><th>p50</th><th>p90</th>'
      + '<th>p99</th><th>P(job past ' + slow + ' ms)</th></tr></thead><tbody>'
      + rows + '</tbody>';

    /* Two rows of bars over the SAME support, one scale, so the mass visibly
       walks to the right as N grows. */
    var support = pmf.map(function (p) { return p[0]; }).sort(function (a, b) { return a - b; });
    var bw = Math.min(80, 600 / support.length), s = '', k;
    for (k = 0; k < support.length; k += 1) {
      var pOne = R(0n, 1n), pJob = R(0n, 1n), t;
      for (t = 0; t < pmf.length; t += 1) if (pmf[t][0] === support[k]) pOne = pmf[t][1];
      for (t = 0; t < job.length; t += 1) if (job[t][0] === support[k]) pJob = job[t][1];
      var h1 = Rnum(pOne) * 84, h2 = Rnum(pJob) * 84;
      s += '<rect x="' + (46 + k * bw) + '" y="' + (98 - h1) + '" width="' + (bw - 6) + '" height="'
        + h1 + '" fill="var(--cyan)" opacity="0.8" />'
        + '<rect x="' + (46 + k * bw) + '" y="' + (204 - h2) + '" width="' + (bw - 6) + '" height="'
        + h2 + '" fill="var(--red)" opacity="0.85" />'
        + '<text x="' + (46 + k * bw + (bw - 6) / 2) + '" y="216" font-size="9" text-anchor="middle" '
        + 'fill="var(--muted)">' + support[k] + ' ms</text>'
        + '<text x="' + (46 + k * bw + (bw - 6) / 2) + '" y="' + (94 - h1)
        + '" font-size="9" text-anchor="middle" fill="var(--muted)">' + Rpct(pOne, 1) + '</text>'
        + '<text x="' + (46 + k * bw + (bw - 6) / 2) + '" y="' + (200 - h2)
        + '" font-size="9" text-anchor="middle" fill="var(--muted)">' + Rpct(pJob, 1) + '</text>';
    }
    s += '<line x1="40" y1="98" x2="650" y2="98" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="40" y1="204" x2="650" y2="204" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="16" font-size="11" fill="var(--cyan)">one partition</text>'
      + '<text x="0" y="122" font-size="11" fill="var(--red)">the job: the maximum of ' + n + '</text>'
      + '<text x="0" y="232" font-size="10" fill="var(--muted)">both rows share one vertical scale, '
      + '0 to 100% of the probability; the mass moves right as N grows, which is the whole lesson</text>';
    dist.innerHTML = s;

    var flip = smallestNForQuantile(pmf, Q99, worst, 4096);
    status.innerHTML = 'One partition averages <strong>' + Rfixed(pmfMean(pmf), 2) + ' ms</strong> '
      + 'with a p99 of ' + pmfQuantile(pmf, Q99) + ' ms. A job over <strong>' + n + '</strong> of them '
      + 'averages <strong>' + Rfixed(pmfMean(job), 2) + ' ms</strong> and has a p99 of <strong>'
      + pmfQuantile(job, Q99) + ' ms</strong>, because it ends when the slowest one ends &mdash; a '
      + 'straggler tax of ' + (tax.ratio === null ? 'n/a' : Rfixed(tax.ratio, 2) + '&times;') + '. '
      + 'The rarest partition time you typed is ' + worst + ' ms at '
      + Rpct(pmfTail(pmf, worst - 1), 2) + ' of partitions'
      + (flip === null
        ? '.'
        : ', and from <strong>' + flip + '</strong> partitions on it IS the job&rsquo;s p99 &mdash; '
          + 'found by exact search over N, not by a logarithm.')
      + ' More partitions do not make the job linearly faster; past a point they only buy you more '
      + 'chances to draw the slow one.';
  }

  pIn.addEventListener('input', redraw);
  nS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Stragglers",
        subtitle="The job's time is the maximum of N partition times, enumerated exactly",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the partition-time distribution"),
        panel_intro=cfg.get(
            "panel_intro",
            "Type any distribution as time:weight pairs. The maximum of N is computed from it "
            "exactly, so both the mean and the p99 of the job are answers and not estimates.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - twochoice
# ---------------------------------------------------------------------------


def _twochoice(cfg):
    balls = int(cfg.get("balls", 1024))
    choices = int(cfg.get("choices", 2))
    seed = int(cfg.get("seed", 3))

    markup = (
        _toolbar(
            "The power of two choices",
            "one stream, two policies: take the lesser-loaded of d bins and the maximum collapses",
            [("red", "one choice"), ("green", "d choices"), ("muted", "the mean, which is 1")],
        )
        + _stage(_svg("stCols", "0 0 660 240", "Two occupancy profiles from the same seeded stream: one choice per ball above, the lesser of d choices below."))
        + _table("stTable")
        + _banner("stStatus")
    )
    controls = (
        _range("stBalls", "Keys, into as many bins", 64, 4096, balls, 64)
        + _range("stD", "Bins sampled per key (d)", 1, 4, choices)
        + _range("stSeed", "Seed", 1, 60, seed)
        + _kpis(
            [
                ("Maximum load, one choice", "stOne"),
                ("Maximum load, d choices", "stMany"),
                ("The mean is", "stMean"),
                ("ln n / ln ln n, stated", "stStatedOne"),
                ("ln ln n, stated", "stStatedTwo"),
                ("Bins left empty, each way", "stEmpty"),
            ]
        )
        + _hint(
            "stHint",
            "Both placements are driven by the <strong>same</strong> draws: key <em>i</em> reads d "
            "values, the one-choice arm takes the first and discards the rest, so neither arm can be "
            "accused of better luck. " + _STATED_NOTE + " " + _STREAM_NOTE,
        )
    )

    script = _CORE_JS + r"""
  var bS = document.getElementById('stBalls'), dS = document.getElementById('stD');
  var sS = document.getElementById('stSeed');
  var cols = document.getElementById('stCols'), table = document.getElementById('stTable');
  var status = document.getElementById('stStatus');
  var SEEDS = 8;

  function redraw() {
    var n = +bS.value, d = +dS.value, seed = +sS.value;
    document.getElementById('stBallsOut').textContent = group(BigInt(n)) + ' into ' + group(BigInt(n));
    document.getElementById('stDOut').textContent = d === 1 ? '1 (no choice at all)' : d;
    document.getElementById('stSeedOut').textContent = seed;

    var one = placeOneChoiceFrom(seed, n, n, d), many = placeChoices(seed, n, n, d);
    document.getElementById('stOne').textContent = occMax(one) + ' keys';
    document.getElementById('stMany').textContent = occMax(many) + ' keys';
    document.getElementById('stMean').textContent = '1 key a bin, exactly';
    var s1 = oneChoiceStatedApprox(n), s2 = twoChoiceStatedApprox(n);
    document.getElementById('stStatedOne').textContent = isFinite(s1) ? s1.toFixed(2) : '&mdash;';
    document.getElementById('stStatedTwo').textContent = isFinite(s2) ? s2.toFixed(2) : '&mdash;';
    document.getElementById('stEmpty').textContent = group(BigInt(occEmpty(one))) + ' / '
      + group(BigInt(occEmpty(many)));

    var acc = maxLoadAcrossSeeds(seed, n, n, d, SEEDS), rows = '', i;
    for (i = 0; i < SEEDS; i += 1) {
      rows += '<tr' + (i === 0 ? ' class="tone-cyan"' : '') + '><td>' + (seed + i)
        + (i === 0 ? ' &mdash; drawn above' : '') + '</td>'
        + '<td class="tone-red">' + acc.one[i] + '</td>'
        + '<td class="tone-green">' + acc.many[i] + '</td>'
        + '<td>' + (acc.many[i] > 0 ? Rfixed(R(BigInt(acc.one[i]), BigInt(acc.many[i])), 2) + '&times;' : '&mdash;')
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>seed</th><th>max, one choice</th><th>max, ' + d
      + ' choices</th><th>ratio</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><th>mean over ' + SEEDS + ' seeds</th>'
      + '<th>' + Rfixed(meanOf(acc.one), 2) + '</th><th>' + Rfixed(meanOf(acc.many), 2) + '</th>'
      + '<th>' + (isFinite(s1) && isFinite(s2) ? 'stated: ' + s1.toFixed(2) + ' vs ' + s2.toFixed(2)
        : 'stated: n too small') + '</th></tr></tfoot>';

    /* Not a bin-by-bin histogram -- at 1024 bins that is a grey smear. The
       profile is a count of BINS at each load, which is what the maximum lives
       in the tail of. */
    var top = Math.max(occMax(one), occMax(many)), prof1 = [], prof2 = [], i2;
    for (i2 = 0; i2 <= top; i2 += 1) { prof1.push(0); prof2.push(0); }
    for (i2 = 0; i2 < n; i2 += 1) { prof1[one[i2]] += 1; prof2[many[i2]] += 1; }
    var bw = Math.min(70, 600 / (top + 1)), s = '';
    for (i2 = 0; i2 <= top; i2 += 1) {
      var h1 = (prof1[i2] / n) * 74, h2 = (prof2[i2] / n) * 74;
      s += '<rect x="' + (46 + i2 * bw) + '" y="' + (96 - h1) + '" width="' + (bw - 6) + '" height="'
        + h1 + '" fill="var(--red)" opacity="0.85" />'
        + '<rect x="' + (46 + i2 * bw) + '" y="' + (202 - h2) + '" width="' + (bw - 6) + '" height="'
        + h2 + '" fill="var(--green)" opacity="0.85" />'
        + '<text x="' + (46 + i2 * bw + (bw - 6) / 2) + '" y="214" font-size="9" text-anchor="middle" '
        + 'fill="var(--muted)">' + i2 + '</text>'
        + (prof1[i2] ? '<text x="' + (46 + i2 * bw + (bw - 6) / 2) + '" y="' + (92 - h1)
          + '" font-size="8" text-anchor="middle" fill="var(--muted)">' + group(BigInt(prof1[i2]))
          + '</text>' : '')
        + (prof2[i2] ? '<text x="' + (46 + i2 * bw + (bw - 6) / 2) + '" y="' + (198 - h2)
          + '" font-size="8" text-anchor="middle" fill="var(--muted)">' + group(BigInt(prof2[i2]))
          + '</text>' : '');
    }
    s += '<line x1="40" y1="96" x2="650" y2="96" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="40" y1="202" x2="650" y2="202" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="16" font-size="11" fill="var(--red)">one choice: fullest bin holds '
      + occMax(one) + '</text>'
      + '<text x="0" y="120" font-size="11" fill="var(--green)">' + d + ' choices: fullest bin holds '
      + occMax(many) + '</text>'
      + '<text x="0" y="232" font-size="10" fill="var(--muted)">bars are how many BINS hold that many '
      + 'keys (the axis is load, not bin number); both rows share one scale, and the maximum is the '
      + 'rightmost bar that exists</text>';
    cols.innerHTML = s;

    status.innerHTML = group(BigInt(n)) + ' keys into ' + group(BigInt(n)) + ' bins leaves a mean of '
      + 'exactly one key a bin. Taking the first bin the stream names, the fullest holds <strong>'
      + occMax(one) + '</strong>; taking the lesser-loaded of <strong>' + d + '</strong> bins from the '
      + 'same draws, the fullest holds <strong>' + occMax(many) + '</strong>. Over seeds ' + seed
      + '&ndash;' + (seed + SEEDS - 1) + ' those average ' + Rfixed(meanOf(acc.one), 2) + ' and '
      + Rfixed(meanOf(acc.many), 2) + '. '
      + (isFinite(s1)
        ? 'The stated asymptotics at n = ' + group(BigInt(n)) + ' are ln n / ln ln n = ' + s1.toFixed(2)
          + ' for one choice and ln ln n = ' + s2.toFixed(2) + ' for two. '
        : '')
      + '<strong>Both of those results are stated here and not proved</strong> &mdash; their proofs '
      + 'need Chernoff bounds, which no subject in this library teaches &mdash; so what this lab does '
      + 'is measure them. Note also what is NOT needed: d = 2 already collapses the maximum, so a full '
      + 'least-loaded search over all ' + group(BigInt(n)) + ' bins buys almost nothing over sampling two.';
  }

  [bS, dS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The power of two choices",
        subtitle="Sampling two bins and taking the lesser, measured against sampling one",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Give each key a second look"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both arms run from one seeded stream, so the only difference between them is the policy. "
            "Move d from 1 to 2 and watch the tail of the load profile disappear.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - scatter
# ---------------------------------------------------------------------------


def _scatter(cfg):
    shards = int(cfg.get("shards", 24))
    rate = int(cfg.get("query_rate", 400))
    pmf = cfg.get("pmf", "10:80, 25:15, 90:4, 250:1")
    seed = int(cfg.get("seed", 9))

    markup = (
        _toolbar(
            "Scatter-gather costs N requests and waits for the worst",
            "sharding divides the work of a query and multiplies the number of requests",
            [("amber", "shard requests"), ("red", "the query's tail"), ("cyan", "one shard")],
        )
        + _stage(_svg("sxPlot", "0 0 660 240", "The exact distribution of an unrouted query's latency, the maximum of N shard latencies, beside a seeded run of the same queries."))
        + _table("sxTable")
        + _banner("sxStatus")
    )
    controls = (
        _range("sxShards", "Shards a query must ask", 1, 64, shards)
        + _range("sxRate", "Queries a second", 10, 5000, rate, 10)
        + _text("sxPmf", "Per-shard latency (ms:weight)", pmf)
        + _range("sxSeed", "Seed for the sampled run", 1, 60, seed)
        + _kpis(
            [
                ("Shard requests a second", "sxReq"),
                ("Request amplification", "sxAmp"),
                ("If the query were routed", "sxRouted"),
                ("Query p99, exact", "sxP99"),
                ("Query p99, from the run", "sxP99s"),
                ("One shard's own p99", "sxOne"),
            ]
        )
        + _hint(
            "sxHint",
            "Two routes to one number. The exact column differences F(t)<sup>N</sup> into a "
            "distribution and reads a nearest-rank percentile off it; the sampled column runs 400 "
            "queries from the seeded stream, takes the maximum of N draws each time, sorts them and "
            "reads the same percentile off the sample with the core's own percentile function. They "
            "should agree, and when one of them is wrong that is how you find out. " + _STREAM_NOTE,
        )
    )

    script = _CORE_JS + r"""
  var nS = document.getElementById('sxShards'), rS = document.getElementById('sxRate');
  var pIn = document.getElementById('sxPmf'), sS = document.getElementById('sxSeed');
  var plot = document.getElementById('sxPlot'), table = document.getElementById('sxTable');
  var status = document.getElementById('sxStatus');
  var QUERIES = 400, LADDER = [1, 2, 4, 8, 16, 32, 64];
  var Q50 = R(1n, 2n), Q90 = R(9n, 10n), Q99 = R(99n, 100n);

  function redraw() {
    var n = +nS.value, rate = +rS.value, seed = +sS.value;
    document.getElementById('sxShardsOut').textContent = n;
    document.getElementById('sxRateOut').textContent = group(BigInt(rate)) + ' /s';
    document.getElementById('sxSeedOut').textContent = seed;
    var pmf = parsePmf(pIn.value);
    if (pmf === null) {
      plot.innerHTML = '<text x="0" y="20" font-size="12" fill="var(--red)">Each entry is '
        + 'time:weight, separated by commas &mdash; for example 10:80, 25:15, 90:4, 250:1.</text>';
      table.innerHTML = '';
      status.innerHTML = 'That is not a distribution yet. Times are whole milliseconds and the '
        + 'weights are normalised for you.';
      ['sxReq', 'sxAmp', 'sxRouted', 'sxP99', 'sxP99s', 'sxOne'].forEach(function (id) {
        document.getElementById(id).innerHTML = '&mdash;';
      });
      return;
    }

    var q = R(BigInt(rate), 1n), req = shardRequestRate(q, n), exact = pmfMax(pmf, n);
    var sample = scatterSample(pmf, n, QUERIES, seed);
    document.getElementById('sxReq').textContent = Rfixed(req, 0) + ' /s';
    document.getElementById('sxAmp').textContent = Rtext(requestAmplification(n)) + '&times;';
    document.getElementById('sxRouted').textContent = Rfixed(routedRequestRate(q), 0) + ' /s';
    document.getElementById('sxP99').textContent = pmfQuantile(exact, Q99) + ' ms';
    document.getElementById('sxP99s').textContent = percentile(sample, Q99) + ' ms';
    document.getElementById('sxOne').textContent = pmfQuantile(pmf, Q99) + ' ms';

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var nn = LADDER[i], ex = pmfMax(pmf, nn);
      rows += '<tr' + (nn === n ? ' class="tone-cyan"' : '') + '><td>' + nn + '</td>'
        + '<td class="tone-amber">' + Rfixed(shardRequestRate(q, nn), 0) + '</td>'
        + '<td>' + Rfixed(pmfMean(ex), 2) + '</td>'
        + '<td>' + pmfQuantile(ex, Q50) + '</td>'
        + '<td>' + pmfQuantile(ex, Q90) + '</td>'
        + '<td class="tone-red">' + pmfQuantile(ex, Q99) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>shards asked</th><th>shard requests a second</th>'
      + '<th>query mean (ms)</th><th>p50</th><th>p90</th><th>p99</th></tr></thead><tbody>'
      + rows + '</tbody>';

    /* The exact cdf of the query, with the sampled cdf stepped over it. */
    var support = pmf.map(function (p) { return p[0]; }).sort(function (a, b) { return a - b; });
    var lo = support[0], hi = support[support.length - 1], span = Math.max(1, hi - lo);
    var x0 = 46, x1 = 640, y0 = 190, y1 = 26, s = '', k;
    function px(t) { return x0 + (x1 - x0) * (t - lo) / span; }
    function py(p) { return y0 - (y0 - y1) * p; }
    var cumE = 0, cumS = 0, pathE = 'M ' + x0 + ' ' + py(0), pathS = 'M ' + x0 + ' ' + py(0);
    for (k = 0; k < support.length; k += 1) {
      var t = support[k], pe = R(0n, 1n), j;
      for (j = 0; j < exact.length; j += 1) if (exact[j][0] === t) pe = exact[j][1];
      cumE += Rnum(pe);
      var below = 0;
      for (j = 0; j < sample.length; j += 1) if (sample[j] <= t) below += 1;
      cumS = below / sample.length;
      pathE += ' L ' + px(t) + ' ' + py(cumE - Rnum(pe)) + ' L ' + px(t) + ' ' + py(cumE);
      pathS += ' L ' + px(t) + ' ' + py(cumS);
      s += '<text x="' + px(t) + '" y="' + (y0 + 14) + '" font-size="9" text-anchor="middle" '
        + 'fill="var(--muted)">' + t + '</text>'
        + '<line x1="' + px(t) + '" y1="' + y1 + '" x2="' + px(t) + '" y2="' + y0
        + '" stroke="var(--line)" stroke-width="1" opacity="0.5" />';
    }
    var p99y = py(0.99);
    s = '<line x1="' + x0 + '" y1="' + y0 + '" x2="' + x1 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + y1 + '" x2="' + x0 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />' + s
      + '<line x1="' + x0 + '" y1="' + p99y + '" x2="' + x1 + '" y2="' + p99y
      + '" stroke="var(--red)" stroke-width="1" stroke-dasharray="5 4" opacity="0.8" />'
      + '<text x="' + (x0 + 4) + '" y="' + (p99y - 4) + '" font-size="10" fill="var(--red)">99%</text>'
      + '<path d="' + pathE + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />'
      + '<path d="' + pathS + '" fill="none" stroke="var(--amber)" stroke-width="1.6" stroke-dasharray="4 3" />'
      + '<text x="' + x0 + '" y="18" font-size="11" fill="var(--cyan)">exact: P(query &le; t) = '
      + 'F(t) to the power ' + n + '</text>'
      + '<text x="' + (x0 + 250) + '" y="18" font-size="11" fill="var(--amber)">sampled: ' + QUERIES
      + ' queries from seed ' + seed + '</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 30) + '" font-size="10" fill="var(--muted)">'
      + 'the exact p99 is ' + pmfQuantile(exact, Q99) + ' ms and the sampled p99 is '
      + percentile(sample, Q99) + ' ms; a single shard&rsquo;s p99 is ' + pmfQuantile(pmf, Q99)
      + ' ms, which is the number a per-shard dashboard shows you</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 44) + '" font-size="10" fill="var(--muted)">'
      + 'milliseconds along the axis, cumulative probability up it</text>';
    plot.innerHTML = s;

    status.innerHTML = 'At <strong>' + n + '</strong> shards, <strong>' + group(BigInt(rate))
      + ' queries a second</strong> become <strong>' + Rfixed(req, 0) + ' shard requests a second'
      + '</strong> &mdash; an amplification of ' + Rtext(requestAmplification(n)) + ', and the figure '
      + 'a routed query would leave at ' + Rfixed(q, 0) + '. Sharding divided the work of each query '
      + 'and multiplied the number of requests; both are true, and only the second one shows up in '
      + 'the fleet&rsquo;s request rate. The query waits for the slowest of the ' + n + ': its p99 is '
      + '<strong>' + pmfQuantile(exact, Q99) + ' ms</strong> exactly, and ' + percentile(sample, Q99)
      + ' ms in the seeded run of ' + QUERIES + ' &mdash; while a single shard&rsquo;s own p99 is only '
      + pmfQuantile(pmf, Q99) + ' ms. The partition count also caps how many consumers can read in '
      + 'parallel at ' + n + ', so it is the same dial as the fan-out.';
  }

  [nS, rS, sS].forEach(function (el) { el.addEventListener('input', redraw); });
  pIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Scatter-gather cost",
        subtitle="N requests per query, and a tail that is the maximum of N",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Ask every shard"),
        panel_intro=cfg.get(
            "panel_intro",
            "The exact curve and the seeded run are computed side by side from the same "
            "distribution, so you can see the request amplification and the tail move together.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - index
# ---------------------------------------------------------------------------


def _index(cfg):
    reads = int(cfg.get("reads", 5000))
    writes = int(cfg.get("writes", 2000))
    shards = int(cfg.get("shards", 16))

    markup = (
        _toolbar(
            "Local index or global index",
            "r&middot;N + w against r + 2w &mdash; neither is always better, and the ratio decides",
            [("cyan", "local"), ("purple", "global"), ("amber", "the crossover")],
        )
        + _stage(_svg("siPlot", "0 0 660 240", "The cost of a local secondary index and a global one drawn against the read-to-write ratio, with the crossover marked."))
        + _table("siTable")
        + _banner("siStatus")
    )
    controls = (
        _range("siR", "Indexed reads a second", 0, 20000, reads, 100)
        + _range("siW", "Writes a second", 0, 20000, writes, 100)
        + _range("siN", "Shards", 2, 64, shards)
        + _kpis(
            [
                ("Local index costs", "siLocal"),
                ("Global index costs", "siGlobal"),
                ("Cheaper here", "siPick"),
                ("By", "siBy"),
                ("Crossover r/w", "siCross"),
                ("Your r/w", "siRatio"),
            ]
        )
        + _hint(
            "siHint",
            "A local index lives beside the rows it indexes, so a write touches one shard and a "
            "lookup has to ask every shard: r&middot;N + w. A global index is itself partitioned by "
            "the indexed value, so a lookup asks one shard and a write touches two &mdash; the row "
            "and the index entry, on different shards: r + 2w. Setting them equal gives "
            "r(N &minus; 1) = w, so they cost the same at r/w = 1/(N &minus; 1), exactly.",
        )
    )

    script = _CORE_JS + r"""
  var rS = document.getElementById('siR'), wS = document.getElementById('siW');
  var nS = document.getElementById('siN');
  var plot = document.getElementById('siPlot'), table = document.getElementById('siTable');
  var status = document.getElementById('siStatus');
  var LADDER = [2, 4, 8, 16, 32, 64];

  function redraw() {
    var rv = +rS.value, wv = +wS.value, n = +nS.value;
    document.getElementById('siROut').textContent = group(BigInt(rv)) + ' /s';
    document.getElementById('siWOut').textContent = group(BigInt(wv)) + ' /s';
    document.getElementById('siNOut').textContent = n;

    var r = R(BigInt(rv), 1n), w = R(BigInt(wv), 1n);
    var local = localIndexCost(r, w, n), global_ = globalIndexCost(r, w);
    var cross = indexCrossover(n), pick = cheaperIndex(r, w, n);
    var ratio = wv === 0 ? null : R(BigInt(rv), BigInt(wv));

    document.getElementById('siLocal').textContent = Rfixed(local, 0) + ' shard ops /s';
    document.getElementById('siGlobal').textContent = Rfixed(global_, 0) + ' shard ops /s';
    document.getElementById('siPick').textContent = pick === 'equal' ? 'exactly equal'
      : (pick === 'local' ? 'the local index' : 'the global index');
    document.getElementById('siBy').textContent = pick === 'equal' ? '&mdash;'
      : Rfixed(Rdiv(pick === 'local' ? global_ : local, pick === 'local' ? local : global_), 2) + '&times;';
    document.getElementById('siCross').textContent = cross === null ? '&mdash;'
      : Rtext(cross) + ' = ' + Rfixed(cross, 4);
    document.getElementById('siRatio').textContent = ratio === null
      ? 'writes are zero' : Rtext(ratio) + ' = ' + Rfixed(ratio, 3);

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var nn = LADDER[i], c = indexCrossover(nn);
      rows += '<tr' + (nn === n ? ' class="tone-cyan"' : '') + '><td>' + nn + '</td>'
        + '<td>' + Rfixed(localIndexCost(r, w, nn), 0) + '</td>'
        + '<td>' + Rfixed(globalIndexCost(r, w), 0) + '</td>'
        + '<td class="tt">' + (c === null ? '&mdash;' : Rtext(c)) + '</td>'
        + '<td>' + (c === null ? '&mdash;' : Rfixed(c, 4)) + '</td>'
        + '<td class="tone-' + (cheaperIndex(r, w, nn) === 'local' ? 'cyan">local'
          : (cheaperIndex(r, w, nn) === 'global' ? 'purple">global' : 'muted">equal')) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>shards</th><th>local (ops/s)</th><th>global (ops/s)</th>'
      + '<th>crossover r/w</th><th>as a decimal</th><th>cheaper</th></tr></thead><tbody>'
      + rows + '</tbody>';

    /* Cost against the ratio r/w, holding the total r + w fixed so the two
       curves are comparable at every point on the axis. */
    var total = rv + wv, x0 = 52, x1 = 640, y0 = 190, y1 = 26, STEPS = 60, i2;
    var maxCost = Rnum(localIndexCost(R(BigInt(total), 1n), R(0n, 1n), n));
    if (maxCost <= 0) maxCost = 1;
    function px(k) { return x0 + (x1 - x0) * k / STEPS; }
    function py(v) { return y0 - (y0 - y1) * Math.min(1, v / maxCost); }
    var lp = '', gp = '';
    for (i2 = 0; i2 <= STEPS; i2 += 1) {
      var rr = R(BigInt(total) * BigInt(i2), BigInt(STEPS));
      var ww = Rsub(R(BigInt(total), 1n), rr);
      lp += (i2 === 0 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(localIndexCost(rr, ww, n)));
      gp += (i2 === 0 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(globalIndexCost(rr, ww)));
    }
    /* The crossover in these coordinates: r/(r+w) = 1/N, since r/w = 1/(N-1). */
    var crossK = STEPS / n;
    var s = '<line x1="' + x0 + '" y1="' + y0 + '" x2="' + x1 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + y1 + '" x2="' + x0 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + px(crossK) + '" y1="' + y1 + '" x2="' + px(crossK) + '" y2="' + y0
      + '" stroke="var(--amber)" stroke-width="1.4" stroke-dasharray="5 4" />'
      + '<text x="' + (px(crossK) + 6) + '" y="' + (y1 + 12) + '" font-size="10" fill="var(--amber)">'
      + 'they cost the same at r/w = ' + (cross === null ? '&mdash;' : Rtext(cross)) + '</text>'
      + '<path d="' + lp + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />'
      + '<path d="' + gp + '" fill="none" stroke="var(--purple)" stroke-width="2.2" />';
    if (total > 0) {
      var here = STEPS * rv / total;
      s += '<circle cx="' + px(here) + '" cy="' + py(Rnum(local)) + '" r="4" fill="var(--cyan)" />'
        + '<circle cx="' + px(here) + '" cy="' + py(Rnum(global_)) + '" r="4" fill="var(--purple)" />';
    }
    s += '<text x="' + x0 + '" y="18" font-size="11" fill="var(--cyan)">local: r&middot;N + w</text>'
      + '<text x="' + (x0 + 160) + '" y="18" font-size="11" fill="var(--purple)">global: r + 2w</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 14) + '" font-size="10" fill="var(--muted)">all writes</text>'
      + '<text x="' + x1 + '" y="' + (y0 + 14) + '" font-size="10" text-anchor="end" fill="var(--muted)">'
      + 'all reads</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 30) + '" font-size="10" fill="var(--muted)">'
      + 'the axis holds r + w fixed at ' + group(BigInt(total)) + ' operations a second and slides the '
      + 'mix from all writes to all reads; shard operations a second up the side, 0 to '
      + group(BigInt(Math.round(maxCost))) + '</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 44) + '" font-size="10" fill="var(--muted)">'
      + 'left of the amber line the local index is cheaper, right of it the global one is &mdash; and '
      + 'the line moves left as N grows</text>';
    plot.innerHTML = s;

    status.innerHTML = 'With <strong>' + group(BigInt(rv)) + '</strong> indexed reads and <strong>'
      + group(BigInt(wv)) + '</strong> writes a second across <strong>' + n + '</strong> shards, a '
      + 'local index costs <strong>' + Rfixed(local, 0) + '</strong> shard operations a second and a '
      + 'global one costs <strong>' + Rfixed(global_, 0) + '</strong>, so '
      + (pick === 'equal' ? 'they cost exactly the same here'
        : 'the ' + pick + ' index wins by ' + Rfixed(Rdiv(pick === 'local' ? global_ : local,
            pick === 'local' ? local : global_), 2) + ' times')
      + '. They break even at r/w = <strong>' + (cross === null ? '&mdash;' : Rtext(cross))
      + '</strong>, which is 1/(N &minus; 1) exactly; your ratio is '
      + (ratio === null ? 'undefined, because there are no writes' : Rtext(ratio))
      + '. Neither index is better in general: a write-mostly workload with a rare lookup wants the '
      + 'local one, and a read-mostly workload wants the global one, and the more shards you have the '
      + 'earlier the global one takes over.';
  }

  [rS, wS, nS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Local vs global secondary indexes",
        subtitle="r·N + w against r + 2w, and the crossover at r/w = 1/(N − 1)",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the workload mix"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both costs are exact, and the crossover is computed from N rather than read off the "
            "chart. Slide the reads past the writes and watch which index wins change hands.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - crossshard
# ---------------------------------------------------------------------------


def _crossshard(cfg):
    keys = int(cfg.get("keys_per_txn", 2))
    shards = int(cfg.get("shards", 16))
    rtt_us = int(cfg.get("rtt_us", 2000))
    fsync_us = int(cfg.get("fsync_us", 500))

    markup = (
        _toolbar(
            "Most transactions do not stay local",
            "k random keys land on one shard with probability N&#8319;&#8315;&#7580;&#8315;&#185;&#8318;",
            [("green", "stays on one shard"), ("red", "crosses"), ("muted", "the grid of key pairs")],
        )
        + _stage(_svg("skGrid", "0 0 660 240", "A grid of where two keys land, with the diagonal marking the transactions that stay on one shard, beside the probability against the shard count."))
        + _table("skTable")
        + _banner("skStatus")
    )
    controls = (
        _range("skK", "Keys in the transaction (k)", 2, 12, keys)
        + _range("skN", "Shards", 2, 64, shards)
        + _range("skRtt", "Round trip between shards (&micro;s)", 100, 20000, rtt_us, 100)
        + _range("skFsync", "An fsync (&micro;s)", 50, 5000, fsync_us, 50)
        + _kpis(
            [
                ("Stays on one shard", "skSame"),
                ("Crosses", "skCross"),
                ("Shards it expects to touch", "skTouch"),
                ("Two-phase commit adds", "skCost"),
                ("Mean added latency", "skMean"),
                ("At N = 2, k = 2 it is", "skTwo"),
            ]
        )
        + _hint(
            "skHint",
            "The first key picks a shard and each of the other k&nbsp;&minus;&nbsp;1 has to match it, "
            "so the probability is N<sup>1&minus;k</sup> &mdash; one call to Rpow with a negative "
            "exponent, exact however large N and k get. The two-phase cost is itemised: a prepare "
            "round trip, a commit round trip, and an fsync in each phase. A single-shard transaction "
            "pays none of it.",
        )
    )

    script = _CORE_JS + r"""
  var kS = document.getElementById('skK'), nS = document.getElementById('skN');
  var rS = document.getElementById('skRtt'), fS = document.getElementById('skFsync');
  var gridEl = document.getElementById('skGrid'), table = document.getElementById('skTable');
  var status = document.getElementById('skStatus');
  var LADDER = [2, 4, 8, 16, 32, 64];

  function redraw() {
    var k = +kS.value, n = +nS.value;
    var rtt = R(BigInt(+rS.value), 1000n), fsync = R(BigInt(+fS.value), 1000n);   /* to ms */
    document.getElementById('skKOut').textContent = k + (k === 2 ? ' keys' : ' keys');
    document.getElementById('skNOut').textContent = n;
    document.getElementById('skRttOut').textContent = Rfixed(rtt, 2) + ' ms';
    document.getElementById('skFsyncOut').textContent = Rfixed(fsync, 2) + ' ms';

    var same = sameShardProb(k, n), cross = crossShardProb(k, n);
    var cost = twoPhaseCost(rtt, fsync), added = meanAddedLatency(k, n, rtt, fsync);
    document.getElementById('skSame').textContent = Rtext(same) + ' = ' + Rpct(same, 4);
    document.getElementById('skCross').textContent = Rpct(cross, 4);
    document.getElementById('skTouch').textContent = Rfixed(expectedShardsTouched(k, n), 3)
      + ' of ' + n;
    document.getElementById('skCost').textContent = Rfixed(cost.total, 2) + ' ms';
    document.getElementById('skMean').textContent = Rfixed(added, 3) + ' ms a transaction';
    document.getElementById('skTwo').textContent = Rtext(sameShardProb(2, 2)) + ' local, '
      + Rtext(crossShardProb(2, 2)) + ' crossing';

    var rows = '', i;
    for (i = 0; i < LADDER.length; i += 1) {
      var nn = LADDER[i], sm = sameShardProb(k, nn);
      rows += '<tr' + (nn === n ? ' class="tone-cyan"' : '') + '><td>' + nn + '</td>'
        + '<td class="tt">' + Rtext(sm) + '</td>'
        + '<td class="tone-green">' + Rpct(sm, 4) + '</td>'
        + '<td class="tone-red">' + Rpct(crossShardProb(k, nn), 4) + '</td>'
        + '<td>' + Rfixed(expectedShardsTouched(k, nn), 3) + '</td>'
        + '<td>' + Rfixed(meanAddedLatency(k, nn, rtt, fsync), 3) + ' ms</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>shards</th><th>P(all ' + k + ' on one), exactly</th>'
      + '<th>stays local</th><th>crosses</th><th>shards touched</th><th>mean added latency</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    /* The grid is the k = 2 picture: where the first key went across, where the
       second went down, and the diagonal is the transactions that stayed. */
    var g = Math.min(n, 16), cell = Math.min(13, 190 / g), s = '', i2, j;
    for (i2 = 0; i2 < g; i2 += 1) {
      for (j = 0; j < g; j += 1) {
        s += '<rect x="' + (40 + j * cell) + '" y="' + (26 + i2 * cell) + '" width="' + (cell - 1.5)
          + '" height="' + (cell - 1.5) + '" fill="var(--' + (i2 === j ? 'green' : 'red')
          + ')" opacity="' + (i2 === j ? '0.9' : '0.3') + '" />';
      }
    }
    s += '<text x="40" y="18" font-size="11" fill="var(--muted)">where the first key lands &rarr;</text>'
      + '<text x="40" y="' + (34 + g * cell) + '" font-size="10" fill="var(--green)">the '
      + g + ' green cells are the transactions that stay on one shard</text>'
      + '<text x="40" y="' + (48 + g * cell) + '" font-size="10" fill="var(--red)">the other '
      + (g * g - g) + ' cross' + (n > 16 ? ' &mdash; drawn at 16 of ' + n + ' shards' : '') + '</text>';
    /* The probability against N, on the right. */
    var x0 = 330, x1 = 648, y0 = 200, y1 = 30, MAXN = 64;
    function px(nn) { return x0 + (x1 - x0) * (nn - 2) / (MAXN - 2); }
    function py(p) { return y0 - (y0 - y1) * p; }
    var path = '';
    for (i2 = 2; i2 <= MAXN; i2 += 1) {
      path += (i2 === 2 ? 'M ' : ' L ') + px(i2) + ' ' + py(Rnum(sameShardProb(k, i2)));
    }
    s += '<line x1="' + x0 + '" y1="' + y0 + '" x2="' + x1 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + y1 + '" x2="' + x0 + '" y2="' + y0
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + x0 + '" y1="' + py(0.5) + '" x2="' + x1 + '" y2="' + py(0.5)
      + '" stroke="var(--muted)" stroke-width="1" stroke-dasharray="4 4" />'
      + '<text x="' + (x0 + 4) + '" y="' + (py(0.5) - 4) + '" font-size="10" fill="var(--muted)">half</text>'
      + '<path d="' + path + '" fill="none" stroke="var(--green)" stroke-width="2.2" />'
      + '<circle cx="' + px(Math.min(MAXN, n)) + '" cy="' + py(Rnum(same)) + '" r="4" fill="var(--green)" />'
      + '<text x="' + x0 + '" y="' + (y1 - 12) + '" font-size="11" fill="var(--green)">'
      + 'P(all ' + k + ' keys on one shard) against N</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 14) + '" font-size="10" fill="var(--muted)">2 shards</text>'
      + '<text x="' + x1 + '" y="' + (y0 + 14) + '" font-size="10" text-anchor="end" fill="var(--muted)">'
      + MAXN + ' shards</text>'
      + '<text x="' + x0 + '" y="' + (y0 + 30) + '" font-size="10" fill="var(--muted)">'
      + 'at k = 2 the curve starts at one half, so even two shards already send half of every '
      + 'two-key transaction across a boundary</text>';
    gridEl.innerHTML = s;

    status.innerHTML = 'A transaction over <strong>' + k + '</strong> randomly hashed keys stays on '
      + 'one of <strong>' + n + '</strong> shards with probability <strong>' + Rtext(same)
      + '</strong> = ' + Rpct(same, 4) + ', so <strong>' + Rpct(cross, 4) + '</strong> of them cross '
      + 'and touch ' + Rfixed(expectedShardsTouched(k, n), 3) + ' shards on average. Each of those '
      + 'pays two-phase commit: ' + Rfixed(cost.rtt, 2) + ' ms of round trips and '
      + Rfixed(cost.fsync, 2) + ' ms of fsyncs, ' + Rfixed(cost.total, 2) + ' ms in all, which '
      + 'averages <strong>' + Rfixed(added, 3) + ' ms</strong> over every transaction. The number '
      + 'that ends the argument is the smallest case there is: at N = 2 and k = 2 the probability of '
      + 'staying local is ' + Rtext(sameShardProb(2, 2)) + ' &mdash; half of all two-key transactions '
      + 'already cross, at the very first shard you add.';
  }

  [kS, nS, rS, fS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Cross-shard transactions",
        subtitle="N to the power 1 − k, and the two-phase cost the rest of them pay",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Spread a transaction over k keys"),
        panel_intro=cfg.get(
            "panel_intro",
            "The probability is exact at every k and N, so push k up and watch how quickly a "
            "transaction stops being local &mdash; and how little the shard count has to do with it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L12 - rebalance
# ---------------------------------------------------------------------------


def _rebalance(cfg):
    moved_pct = int(cfg.get("moved_pct", 25))
    data_tb = int(cfg.get("data_tb", 48))
    throttle_mbs = int(cfg.get("throttle_mbs", 200))
    budget_mbs = int(cfg.get("budget_mbs", 800))
    node_rps = int(cfg.get("node_rps", 5000))
    service_rps = int(cfg.get("service_rps", 8000))

    markup = (
        _toolbar(
            "Rebalancing is neither instant nor free",
            "m&middot;D/B of wall clock, at a utilisation the copy raised while it ran",
            [("cyan", "serving"), ("amber", "the copy"), ("red", "the wait it causes")],
        )
        + _stage(_svg("szBar", "0 0 660 230", "The node's capacity split between serving and the throttled copy, with the queueing wait before and during the move."))
        + _table("szTable")
        + _banner("szStatus")
    )
    controls = (
        _range("szMoved", "Fraction of the data that moves", 1, 100, moved_pct)
        + _range("szData", "Dataset (TB, decimal)", 1, 400, data_tb)
        + _range("szThrottle", "Copy throttle (MB/s)", 10, 800, throttle_mbs, 10)
        + _range("szBudget", "A node's transfer budget (MB/s)", 100, 2000, budget_mbs, 50)
        + _range("szLam", "Requests a second at the node", 100, 20000, node_rps, 100)
        + _range("szMu", "The node serves (requests a second)", 200, 30000, service_rps, 100)
        + _kpis(
            [
                ("Bytes to move", "szBytes"),
                ("How long it takes", "szTime"),
                ("Capacity the copy takes", "szSteal"),
                ("Utilisation before", "szRhoA"),
                ("Utilisation during", "szRhoB"),
                ("Wait, before &rarr; during", "szWait"),
            ]
        )
        + _hint(
            "szHint",
            "A terabyte is 10&#185;&#178; bytes and a MB/s is 10&#8310; bytes a second, so the "
            "duration is m&middot;D/B with nothing hidden in the units. The copy is not free while "
            "it runs: it holds a share of the node's transfer budget, which is capacity the node is "
            "no longer serving with, so its effective service rate falls to &mu;(1 &minus; B/budget) "
            "&mdash; and the wait that produces is the M/M/1 result of &ldquo;The M/M/1 Queue&rdquo;, reused rather than "
            "restated.",
        )
    )

    script = _CORE_JS + r"""
  var mS = document.getElementById('szMoved'), dS = document.getElementById('szData');
  var tS = document.getElementById('szThrottle'), bS = document.getElementById('szBudget');
  var lS = document.getElementById('szLam'), uS = document.getElementById('szMu');
  var barEl = document.getElementById('szBar'), table = document.getElementById('szTable');
  var status = document.getElementById('szStatus');
  var TB = 1000000000000n, MBS = 1000000n;

  function redraw() {
    var frac = R(BigInt(+mS.value), 100n), data = R(BigInt(+dS.value) * TB, 1n);
    var thr = R(BigInt(+tS.value) * MBS, 1n), budget = R(BigInt(+bS.value) * MBS, 1n);
    var lam = R(BigInt(+lS.value), 1n), mu = R(BigInt(+uS.value), 1n);
    document.getElementById('szMovedOut').textContent = (+mS.value) + '%';
    document.getElementById('szDataOut').textContent = (+dS.value) + ' TB';
    document.getElementById('szThrottleOut').textContent = (+tS.value) + ' MB/s';
    document.getElementById('szBudgetOut').textContent = (+bS.value) + ' MB/s';
    document.getElementById('szLamOut').textContent = group(BigInt(+lS.value)) + ' /s';
    document.getElementById('szMuOut').textContent = group(BigInt(+uS.value)) + ' /s';

    var bytes = movedBytes(frac, data), secs = rebalanceSeconds(frac, data, thr);
    var stolen = stolenShare(thr, budget), load = rebalanceLoad(lam, mu, thr, budget);
    document.getElementById('szBytes').textContent = byteText(bytes);
    document.getElementById('szTime').textContent = secs === null ? '&mdash;' : durText(secs);
    document.getElementById('szSteal').textContent = stolen === null ? '&mdash;'
      : Rtext(stolen) + ' = ' + Rpct(stolen, 2);
    document.getElementById('szRhoA').textContent = Rpct(load.before.rho, 2);
    document.getElementById('szRhoB').textContent = Rcmp(stolen, R(1n, 1n)) >= 0
      ? 'the copy took it all' : Rpct(load.during.rho, 2);
    document.getElementById('szWait').textContent = (load.before.stable ? Rfixed(Rmul(load.before.W, R(1000n, 1n)), 3) + ' ms' : 'unstable')
      + ' &rarr; ' + (load.during.stable ? Rfixed(Rmul(load.during.W, R(1000n, 1n)), 3) + ' ms' : 'unstable');

    var rows = '', i, THROTTLES = [50, 100, 200, 400, 800];
    for (i = 0; i < THROTTLES.length; i += 1) {
      var t = R(BigInt(THROTTLES[i]) * MBS, 1n);
      var sec = rebalanceSeconds(frac, data, t), st = stolenShare(t, budget);
      var ld = rebalanceLoad(lam, mu, t, budget);
      rows += '<tr' + (THROTTLES[i] === +tS.value ? ' class="tone-cyan"' : '') + '><td>'
        + THROTTLES[i] + ' MB/s</td>'
        + '<td>' + (sec === null ? '&mdash;' : durText(sec)) + '</td>'
        + '<td>' + (st === null ? '&mdash;' : Rpct(st, 1)) + '</td>'
        + '<td>' + (ld.during.stable ? Rpct(ld.during.rho, 2) : 'past capacity') + '</td>'
        + '<td class="tone-red">' + (ld.during.stable
          ? Rfixed(Rmul(ld.during.W, R(1000n, 1n)), 3) + ' ms' : 'unbounded') + '</td>'
        + '<td>' + (ld.during.stable && load.before.stable
          ? Rfixed(Rdiv(ld.during.W, load.before.W), 2) + '&times;' : '&mdash;') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>throttle</th><th>the move takes</th><th>capacity it takes</th>'
      + '<th>utilisation during</th><th>wait during</th><th>against the wait before</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    /* Capacity as one bar, and the two waits as two more. */
    var W = 560, x0 = 76, s = '';
    var stealW = W * Math.min(1, Rnum(stolen));
    s += '<text x="0" y="30" font-size="11" fill="var(--text)">capacity</text>'
      + '<rect x="' + x0 + '" y="16" width="' + (W - stealW) + '" height="26" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<rect x="' + (x0 + W - stealW) + '" y="16" width="' + stealW + '" height="26" rx="3" fill="var(--amber)" opacity="0.9" />'
      + '<text x="' + (x0 + 8) + '" y="34" font-size="11" fill="var(--bg)">serving &mdash; '
      + (load.during.stable ? Rfixed(load.muMove, 0) : '0') + ' /s while the copy runs</text>'
      + '<text x="' + (x0 + W - stealW + 6) + '" y="54" font-size="10" fill="var(--amber)">the copy: '
      + Rpct(stolen, 1) + ' of the budget, for ' + (secs === null ? '&mdash;' : durText(secs)) + '</text>';
    var waitTop = 1;
    if (load.before.stable) waitTop = Math.max(waitTop, Rnum(load.before.W) * 1000);
    if (load.during.stable) waitTop = Math.max(waitTop, Rnum(load.during.W) * 1000);
    var rowsW = [['before the move', load.before, 'cyan', 88], ['during it', load.during, 'red', 138]];
    for (i = 0; i < rowsW.length; i += 1) {
      var st2 = rowsW[i][1];
      var w = st2.stable ? Math.max(2, (Rnum(st2.W) * 1000 / waitTop) * W) : W;
      s += '<text x="0" y="' + (rowsW[i][3] - 4) + '" font-size="10" fill="var(--muted)">'
        + rowsW[i][0] + '</text>'
        + '<rect x="' + x0 + '" y="' + rowsW[i][3] + '" width="' + w + '" height="22" rx="3" fill="var(--'
        + rowsW[i][2] + ')" opacity="' + (st2.stable ? '0.85' : '0.35') + '" />'
        + '<text x="' + (x0 + w + 8) + '" y="' + (rowsW[i][3] + 16) + '" font-size="11" fill="var(--'
        + rowsW[i][2] + ')">' + (st2.stable
          ? Rfixed(Rmul(st2.W, R(1000n, 1n)), 3) + ' ms at &rho; = ' + Rpct(st2.rho, 1)
          : 'unstable: &rho; is at or past 1') + '</text>';
    }
    s += '<text x="0" y="184" font-size="10" fill="var(--muted)">both wait bars share one scale, 0 to '
      + waitTop.toFixed(3) + ' ms; the wait is M/M/1&rsquo;s W = 1/(&mu; &minus; &lambda;), the course-3 '
      + 'result read at the utilisation the copy produced</text>'
      + '<text x="0" y="200" font-size="10" fill="var(--muted)">moving ' + byteText(bytes) + ' at '
      + (+tS.value) + ' MB/s takes ' + (secs === null ? '&mdash;' : durText(secs))
      + ', and the elevated utilisation lasts exactly that long</text>'
      + '<text x="0" y="216" font-size="10" fill="var(--muted)">a gentler throttle is a longer window '
      + 'at a lower &rho;, and a harder one is a shorter window at a worse one &mdash; that trade is '
      + 'the whole operational decision</text>';
    barEl.innerHTML = s;

    status.innerHTML = 'Moving <strong>' + (+mS.value) + '%</strong> of ' + (+dS.value) + ' TB is '
      + '<strong>' + byteText(bytes) + '</strong>, and at ' + (+tS.value) + ' MB/s it takes <strong>'
      + (secs === null ? '&mdash;' : durText(secs)) + '</strong>. While it runs the copy holds '
      + Rtext(stolen) + ' of the node&rsquo;s transfer budget, so the node serves '
      + (load.during.stable ? Rfixed(load.muMove, 0) : '0') + ' requests a second instead of '
      + group(BigInt(+uS.value)) + ' and its utilisation goes from <strong>'
      + Rpct(load.before.rho, 2) + '</strong> to <strong>'
      + (load.during.stable ? Rpct(load.during.rho, 2) : 'at or past 100%') + '</strong>. '
      + (load.before.stable && load.during.stable
        ? 'The M/M/1 wait at those two utilisations is '
          + Rfixed(Rmul(load.before.W, R(1000n, 1n)), 3) + ' ms and '
          + Rfixed(Rmul(load.during.W, R(1000n, 1n)), 3) + ' ms &mdash; a factor of '
          + Rfixed(Rdiv(load.during.W, load.before.W), 2) + ', held for the whole window. '
        : 'At that utilisation the queue has no steady state at all: the copy pushed the node past '
          + 'its own service rate, and the wait is unbounded for as long as the move lasts. ')
      + 'Rebalancing is not instantaneous and it is not free; it is a window of elevated latency '
      + 'whose length you choose with the throttle.';
  }

  [mS, dS, tS, bS, lS, uS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Rebalancing cost",
        subtitle="m·D/B of wall clock, and the utilisation the copy holds it at",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Move a fraction of the data"),
        panel_intro=cfg.get(
            "panel_intro",
            "The duration and the elevated utilisation are the same decision seen twice: a gentler "
            "throttle is a longer window at a lower rho. Both, and the wait each produces, are exact.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "count": _count,
    "bins": _bins,
    "rehash": _rehash,
    "vnodes": _vnodes,
    "range": _range_mode,
    "hotkey": _hotkey,
    "straggler": _straggler,
    "twochoice": _twochoice,
    "scatter": _scatter,
    "index": _index,
    "crossshard": _crossshard,
    "rebalance": _rebalance,
}

MODES = tuple(sorted(_MODES))


def shard_lab(cfg):
    """Course 7's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

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
            "shard_lab: unknown mode %r; the twelve modes of course 7 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["shard_lab", "SHARDKIT_JS", "MODES"]
