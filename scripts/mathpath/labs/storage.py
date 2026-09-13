"""Course 8: Storage Engines and Indexes -- one kit, eleven modes.

Every storage engine is a bargain between reads, writes and space, and the
bargain is countable. So the modes here are the eleven places the count is
made: what an access PATTERN costs against what a SIZE costs, how many levels
a tree has, what a range query does to a hash index, what an index costs a
writer, what an LSM rewrites, what a filter buys back, where the three
amplifications trade against each other, what an fsync caps, what a columnar
layout reads, what the page cache holds, and what a backup schedule means in
bytes and in hours.

Five decisions run through all eleven.

  A HEIGHT IS AN INTEGER SEARCH, NOT A LOGARITHM. `btreeHeight` multiplies B
  into an accumulator until it reaches N and counts the multiplications. That
  is the definition -- the smallest h with B^h >= N -- and it is exact at the
  boundary, where `Math.ceil(Math.log(N)/Math.log(B))` is not. At B = 3, N = 9
  that quotient is 2.0000000000000004 and its ceiling is 3: a two-level tree
  reported as three, a whole extra I/O on a page whose subject is counting
  I/Os. It is not a rare corner -- B = 5 at N = 125, B = 8 at N = 2 097 152 and
  B = 19 at N = 2 476 099 all do the same thing, and the lab prints both
  answers side by side wherever they differ. `levelsForSize` runs the same
  search for an LSM's level count.

  BYTES ARE DECIMAL. 1 kB = 1000 B and 1 GB = 10^9 B, everywhere, and the
  pages say so. It is not a detail: the lesson's headline figure, a gigabyte
  as 4 kB random reads costing about 250 times the sequential read, is 250.75
  in decimal units and 262.9 in binary ones. A reader checking the arithmetic
  has to know which units the 250 came from.

  THE BLOOM FILTER'S SIZING ROUNDS, AND SAYS SO ON ITS FACE. `bitsPerKeyApprox`
  is a logarithm and `bloomApprox` is an exponential; both are Numbers, and the
  `bloom` mode labels every figure derived from them. It also prints the
  textbook 1.44 * log2(1/p) beside the real 1/ln2 = 1.4427 form, because the
  familiar "9.57 bits per key at 1%" is the two-digit constant's answer and
  the constant's own answer is 9.585. And it evaluates the EXACT form
  (1 - (1 - 1/m)^(kn))^k as a rational where that is possible -- at m = 64,
  n = 8, k = 5 -- so a reader can see what the approximation costs. The
  derivation, the optimal k and the no-deletion rule are Algorithms
  `randomised-algorithms/bloom-filters`; this lesson only sizes.

  THE PAGE CACHE IS COURSE 4'S CACHE. `workingset` calls `zipfHit` in
  sysdesign_core.py -- the same function the `cache` kit's `zipf` mode calls,
  not a second copy -- and `mathcheck.js` pins the two against each other on a
  shared input so they cannot drift. Past the size where the exact harmonic is
  readable it switches to `harmonicApprox` and returns `rounded: true`, which
  the page reports; at s = 0 it stays exact at any size, because H(n,0) = n.

  AN UNKNOWN MODE RAISES. A kit that fell back to a default would render a
  finished-looking page carrying another lesson's widget, and every markup
  assertion would pass.

The modes, and the lesson each belongs to:

  io          L1  seeks*t_seek + bytes/bw, both ways, and the crossover chunk
  btree       L2  the smallest h with B^h >= N, and the I/Os a lookup costs
  rangeq      L3  a workload mix in I/Os, hash against tree
  indexcost   L4  k + 1 random writes, and the throughput that leaves
  lsm         L5  WA = L*F/2, RA = L, and the compaction bandwidth
  bloom       L6  bits per key, the filter's memory, and RA with and without
  rum         L7  the read/update/memory triple for three engine shapes
  fsync       L8  1/t, B/t, and the batch wait that pays for the difference
  columnar    L9  bytes scanned each way, and the whole-row lookup that flips it
  workingset  L10 the Zipf hit rate of the page cache, and (1 - h)*reads
  recovery    L11 bytes at risk against hours to restore
"""

import json

from .algebra_core import RATIONAL_JS
from .common import Lab
from .sysdesign_core import APPROX_JS, HARMONIC_JS, QUEUE_JS, RCEIL_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

STORAGE_JS = r"""
  /* ---------------------------------------------------------------- output

     Rdec goes through Number(a.n)/Number(a.d), and this course produces
     rationals a double cannot hold: a filter's exact false-positive rate at
     m = 64, n = 8, k = 5 is a fraction with a 362-digit denominator. So the
     decimals here are long division in BigInt, rounded half up at the last
     digit printed, exact at every size up to that one rounding. */
  function Rfix(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);          /* round half up */
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }
  /* A percentage of an exact ratio, exact until the last digit printed. */
  function Rpct(a, places) {
    return Rfix(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }
  /* A float for PLOTTING only. Never for a figure: it goes through Rfix, so it
     cannot be the NaN that Number(huge)/Number(huge) produces. */
  function Rflt(a) { return parseFloat(Rfix(a, 9)); }
  /* Digit grouping. 62500000 and 62 500 000 are the same number and only one
     of them can be read at a glance. */
  function grp(value) {
    var s = String(value), sign = '';
    if (s.charAt(0) === '-') { sign = '-'; s = s.slice(1); }
    return sign + s.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  }
  /* DECIMAL byte units: 1 kB = 1000 B, 1 GB = 10^9 B. Stated rather than
     assumed, because this course's headline ratio depends on which. */
  function byteText(a) {
    var b = Rabs(a), i;
    var units = [[1000000000000000n, ' PB'], [1000000000000n, ' TB'],
                 [1000000000n, ' GB'], [1000000n, ' MB'], [1000n, ' kB']];
    for (i = 0; i < units.length; i += 1) {
      if (Rcmp(b, R(units[i][0], 1n)) >= 0) return Rfix(Rdiv(a, R(units[i][0], 1n)), 2) + units[i][1];
    }
    return grp(Rfix(a, 0)) + ' B';
  }
  /* A duration, in whatever unit keeps it readable. An entity, so this belongs
     in innerHTML rather than textContent. */
  function secText(a) {
    var b = Rabs(a);
    if (Rzero(b)) return '0 s';
    if (Rcmp(b, R(1n, 1000000n)) < 0) return Rfix(Rmul(a, R(1000000000n, 1n)), 1) + ' ns';
    if (Rcmp(b, R(1n, 1000n)) < 0) return Rfix(Rmul(a, R(1000000n, 1n)), 1) + ' &micro;s';
    if (Rcmp(b, R(1n, 1n)) < 0) return Rfix(Rmul(a, R(1000n, 1n)), 2) + ' ms';
    if (Rcmp(b, R(600n, 1n)) < 0) return Rfix(a, 2) + ' s';
    if (Rcmp(b, R(7200n, 1n)) < 0) return Rfix(Rdiv(a, R(60n, 1n)), 1) + ' min';
    if (Rcmp(b, R(172800n, 1n)) < 0) return Rfix(Rdiv(a, R(3600n, 1n)), 2) + ' h';
    return Rfix(Rdiv(a, R(86400n, 1n)), 2) + ' days';
  }

  /* ============ L1: the pattern, not the size ==============================

     time = seeks * t_seek + bytes / bandwidth.

     Both terms are always there. The mistake the lesson names is dropping the
     first one, which is the same as assuming one seek -- true for a sequential
     read and false by five orders of magnitude for a random one. */
  function seekCount(totalBytes, chunkBytes) { return Rceil(Rdiv(totalBytes, chunkBytes)); }
  function ioTime(seeks, seekSec, totalBytes, bwBps) {
    return Radd(Rmul(R(seeks, 1n), seekSec), Rdiv(totalBytes, bwBps));
  }
  function randomTime(totalBytes, chunkBytes, seekSec, bwBps) {
    return ioTime(seekCount(totalBytes, chunkBytes), seekSec, totalBytes, bwBps);
  }
  /* One seek and then the whole file: the SAME formula at one seek, not a
     second model. The bytes term is identical in both, which is the point --
     everything that differs between them is the seek count. */
  function seqTime(totalBytes, seekSec, bwBps) { return ioTime(1n, seekSec, totalBytes, bwBps); }
  function ioRatio(totalBytes, chunkBytes, seekSec, bwBps) {
    return Rdiv(randomTime(totalBytes, chunkBytes, seekSec, bwBps),
                seqTime(totalBytes, seekSec, bwBps));
  }
  /* The chunk at which the transfer costs exactly what the seek costs:
     chunk / bw = t_seek, so chunk = t_seek * bw. Below it the arm dominates
     and the size of the read hardly matters; above it the bandwidth does and
     the seek hardly matters. One multiplication, exact. */
  function crossoverChunk(seekSec, bwBps) { return Rmul(seekSec, bwBps); }

  /* ============ L2: a height is an integer search ==========================

     The smallest h with B^h >= N, found by multiplying B into an accumulator
     and counting. No logarithm, so nothing rounds, and the boundary case
     N = B^h comes out h rather than h + 1. */
  function btreeHeight(n, b) {
    var N = BigInt(n), B = BigInt(b);
    if (N <= 1n) return 1;
    if (B < 2n) return null;                  /* a fanout of one never covers N */
    var cap = 1n, h = 0;
    while (cap < N) { cap *= B; h += 1; if (h > 512) return null; }
    return h;
  }
  /* What the same height looks like through a logarithm, for the page that
     shows why this kit does not use one. */
  function btreeHeightByLog(n, b) { return Math.ceil(Math.log(n) / Math.log(b)); }
  function btreeCapacity(b, h) { return BigInt(b) ** BigInt(h); }
  function btreeNodes(b, level) { return BigInt(b) ** BigInt(level - 1); }
  /* I/Os a lookup costs: one per level the page cache does not already hold.
     Caching more levels than there are is not negative work. */
  function lookupIos(n, b, cached) {
    var h = btreeHeight(n, b);
    if (h === null) return null;
    var c = cached < 0 ? 0 : (cached > h ? h : cached);
    return h - c;
  }

  /* ============ L3: hash against tree, counted in I/Os =====================

     "Hash is faster" is a claim about point lookups presented as a claim about
     everything. A hash index destroys the order a range needs, so a range on
     one is a full scan; a tree pays its height on every lookup and then walks
     leaves in order. The expected probe length Theta(1 + alpha) that makes a
     hash lookup one I/O is Algorithms `data-structures/hashing-with-chaining`;
     it is cited, not re-derived. */
  function pagesFor(rows, perPage) {
    return Rceil(Rdiv(R(BigInt(rows), 1n), R(BigInt(perPage), 1n)));
  }
  function hashPointIos() { return 1n; }
  function hashRangeIos(rows, perPage) { return pagesFor(rows, perPage); }
  function treePointIos(rows, b) { return BigInt(btreeHeight(rows, b)); }
  /* The descent is paid once and the matching leaves are read in order, so a
     range of `width` rows is h - 1 interior pages plus the leaf pages it
     spans. */
  function treeRangeIos(rows, b, width, perPage) {
    return BigInt(btreeHeight(rows, b)) - 1n + pagesFor(width, perPage);
  }
  function mixIos(points, ranges, perPoint, perRange) {
    return Radd(Rmul(R(BigInt(points), 1n), R(perPoint, 1n)),
                Rmul(R(BigInt(ranges), 1n), R(perRange, 1n)));
  }
  /* The range rate at which the two engines cost the same, given the point
     rate: r*(hashRange - treeRange) = p*(treePoint - hashPoint). Exact, and
     null when nothing ties them. */
  function rangeCrossover(points, hashPoint, hashRange, treePoint, treeRange) {
    var dr = hashRange - treeRange;
    if (dr === 0n) return null;
    return Rdiv(Rmul(R(BigInt(points), 1n), R(treePoint - hashPoint, 1n)), R(dr, 1n));
  }

  /* ============ L4: an index is not free for writes ========================

     One insert writes the table and then every index on it, each in a
     different place: k indexes make k + 1 random writes, and a device that
     does D of those a second does D/(k+1) inserts. */
  function writesPerInsert(k) { return R(BigInt(k) + 1n, 1n); }
  function insertRate(deviceWrites, k) {
    return Rdiv(R(BigInt(deviceWrites), 1n), writesPerInsert(k));
  }
  /* The share of the bare rate that k indexes leave: 1/(k+1). */
  function throughputShare(k) { return Rinv(writesPerInsert(k)); }
  /* The smallest k whose share falls to or below a target -- "the k that
     halves throughput" is this at 1/2, computed rather than asserted. */
  function indexesForShare(share) {
    if (Rzero(share)) return null;
    var k = Rceil(Rinv(share)) - 1n;
    return k < 0n ? 0n : k;
  }
  /* The largest k that still meets an insert target: D/(k+1) >= t means
     k <= D/t - 1, and the floor of an exact rational is the answer. */
  function maxIndexesFor(deviceWrites, target) {
    if (target <= 0) return null;
    var k = Rfloor(Rdiv(R(BigInt(deviceWrites), 1n), R(BigInt(target), 1n))) - 1n;
    return k < 0n ? null : k;
  }

  /* ============ L5: append-only is not the same as cheap ===================

     A levelled LSM merges each level into the next. A byte arriving at a level
     is rewritten once for each merge it takes part in, and a level is on
     average half full of the data it will eventually hold, so the level costs
     about F/2 rewrites -- and L levels cost L*F/2. Read amplification before
     filters is L: a lookup that misses has to ask every level. */
  function lsmWriteAmp(levels, fanout) {
    return Rdiv(R(BigInt(levels) * BigInt(fanout), 1n), R(2n, 1n));
  }
  function lsmReadAmp(levels) { return R(BigInt(levels), 1n); }
  /* What that costs the disk: every byte ingested is written WA times, so the
     bandwidth compaction needs is ingest * WA. Sizing the disk to the ingest
     rate alone is the misconception of L7, and it starts here. */
  function compactionBw(ingestBps, wa) { return Rmul(ingestBps, wa); }
  function levelCapacity(memtableBytes, fanout, level) {
    return Rmul(memtableBytes, R(BigInt(fanout) ** BigInt(level), 1n));
  }
  /* How many levels the data actually forces, by the same exact integer search
     the B-tree height uses: the smallest L with memtable * F^L >= size. */
  function levelsForSize(datasetBytes, memtableBytes, fanout) {
    var F = BigInt(fanout);
    if (F < 2n) return null;
    if (Rcmp(memtableBytes, datasetBytes) >= 0) return 0;
    var cap = memtableBytes, L = 0;
    while (Rcmp(cap, datasetBytes) < 0) {
      cap = Rmul(cap, R(F, 1n)); L += 1; if (L > 512) return null;
    }
    return L;
  }

  /* ============ L6: bits per key, and which constant it came from ==========

     At the optimal number of hashes k = (m/n) ln 2 the bargain is
     m/n = log2(1/p) / ln 2 bits per key, INDEPENDENT OF n.

     This rounds -- it is a logarithm -- and so does everything below it. It is
     also not the number a textbook quotes: 1.44 is a two-digit rounding of
     1/ln 2 = 1.4427, and at p = 1/100 the two answers are 9.567 and 9.585.
     Both are returned, and the page says which is which.

     The derivation, the optimal k, the exact form under the independent-hash
     idealisation and the rule that a filter supports no deletion belong to
     Algorithms `randomised-algorithms/bloom-filters`. */
  function bitsPerKeyTextbook(p) { return 1.44 * Math.log2(1 / p); }
  function bloomBits(n, p) { return Math.ceil(n * bitsPerKeyApprox(p)); }
  function bloomMemoryBytes(n, p) { return R(BigInt(bloomBits(n, p)), 8n); }
  /* k = (m/n) ln 2 = log2(1/p) at the optimum, rounded to a whole number,
     because you cannot run 6.64 hash functions. */
  function bloomHashes(p) {
    var k = Math.round(Math.log2(1 / p));
    return k < 1 ? 1 : k;
  }
  /* The EXACT false-positive rate under the independent-hash idealisation,
     (1 - (1 - 1/m)^(kn))^k, as a rational. Evaluable only while m and kn are
     small: a production filter has m near 10^10 and there is no fraction to
     print. Returns null past the limit rather than a rounded number wearing an
     exact label. */
  function bloomExactRate(m, n, k) {
    if (m > 4096 || k * n > 512) return null;
    var one = R(1n, 1n);
    var empty = Rpow(Rsub(one, R(1n, BigInt(m))), k * n);
    return Rpow(Rsub(one, empty), k);
  }
  /* Read amplification with a filter on every level: the level that holds the
     key costs one, and each of the other L - 1 costs p -- the probability its
     filter says yes when the key is not there. Exact, because p is a target
     the reader chose and not a measurement. */
  function readAmpWithFilter(levels, p) {
    return Radd(R(1n, 1n), Rmul(R(BigInt(levels) - 1n, 1n), p));
  }

  /* ============ L7: three corners of one triangle ==========================

     Read, update and memory amplification cannot all be minimised. Each engine
     below minimises one and pays in the other two, and the numbers come from
     the reader's F, L and page geometry rather than from a quotation. */
  function rumLevelled(levels, fanout) {
    return { read: lsmReadAmp(levels),
             write: lsmWriteAmp(levels, fanout),
             space: Radd(R(1n, 1n), R(1n, BigInt(fanout))) };
  }
  /* Tiered keeps up to F runs per level instead of merging into one, so a
     lookup probes every run (L*F), a byte is written once per level (L), and a
     level can hold F copies of the same key (F). */
  function rumTiered(levels, fanout) {
    return { read: R(BigInt(levels) * BigInt(fanout), 1n),
             write: R(BigInt(levels), 1n),
             space: R(BigInt(fanout), 1n) };
  }
  /* A B-tree reads one page per level and writes a WHOLE PAGE to change one
     row, and its pages are not full: at fill factor f it occupies 1/f of what
     it holds. */
  function rumBtree(height, pageBytes, rowBytes, fill) {
    return { read: R(BigInt(height), 1n),
             write: Rdiv(R(BigInt(pageBytes), 1n), R(BigInt(rowBytes), 1n)),
             space: Rinv(fill) };
  }
  /* Where an engine sits in the triangle: the share each of its three costs
     takes of their total, so it lands nearest the corner it pays most in.
     Shares, not raw amplifications, because the three are in different units
     and only their proportions can be plotted together. */
  function rumShares(triple) {
    var total = Radd(Radd(triple.read, triple.write), triple.space);
    if (Rzero(total)) return null;
    return { read: Rdiv(triple.read, total),
             write: Rdiv(triple.write, total),
             space: Rdiv(triple.space, total) };
  }

  /* ============ L8: fsync caps durability =================================

     write() returning means the bytes reached the page cache. Durability is
     the fsync, and one fsync per commit caps DURABLE writes at 1/t whatever
     the CPU and the network can do. Grouping B commits into one fsync
     amortises it to t/B each -- paid for with the wait to fill the batch. */
  function durableCap(tfSec) { return Rinv(tfSec); }
  function groupedCap(tfSec, batch) { return Rdiv(R(BigInt(batch), 1n), tfSec); }
  function perWriteCost(tfSec, batch) { return Rdiv(tfSec, R(BigInt(batch), 1n)); }
  /* A write arrives uniformly among the B places in its batch, so it waits for
     (B - 1)/2 further arrivals at 1/lambda each. */
  function fillWait(batch, lam) {
    return Rdiv(R(BigInt(batch) - 1n, 1n), Rmul(R(2n, 1n), lam));
  }
  /* The whole commit latency: the fill wait, then the batch queues for the one
     thread that fsyncs. mm1 is course 3's result REUSED, not a second model --
     batches arrive at lambda/B and are served at 1/t. At B = 1 the queue is
     unstable whenever lambda exceeds 1/t, which is the lesson's cap arriving
     as a queueing fact rather than as an assertion. */
  function commitLatency(tfSec, batch, lam) {
    var lamB = Rdiv(lam, R(BigInt(batch), 1n));
    var q = mm1(lamB, durableCap(tfSec));
    var fill = fillWait(batch, lam);
    if (!q.stable) return { stable: false, rho: q.rho, fill: fill };
    return { stable: true, rho: q.rho, fill: fill, service: q.W, total: Radd(fill, q.W) };
  }
  /* The batch size that minimises that latency, found by evaluating the curve
     at every B in range. A closed form for this shape of trade-off exists --
     it is the EOQ of Operations Research `inventory-models/the-eoq-formula-
     without-calculus` -- and this lesson deliberately scans instead, so the
     curve is on the page. */
  function bestBatch(tfSec, lam, maxB) {
    var best = null, B, c;
    for (B = 1; B <= maxB; B += 1) {
      c = commitLatency(tfSec, B, lam);
      if (!c.stable) continue;
      if (best === null || Rcmp(c.total, best.total) < 0) best = { batch: B, total: c.total };
    }
    return best;
  }

  /* ============ L9: bytes scanned is a layout question =====================

     A row store reads whole rows even when the query names one column; a
     column store reads only the columns named. Then both are divided by
     whatever their layout compresses to -- and a column of like values
     compresses better than a row of unlike ones, which is half of why the
     comparison goes the way it does. */
  function columnBytes(rowBytes, cols) {
    return Rdiv(R(BigInt(rowBytes), 1n), R(BigInt(cols), 1n));
  }
  function rowScanBytes(rows, rowBytes, ratio) {
    return Rdiv(R(BigInt(rows) * BigInt(rowBytes), 1n), ratio);
  }
  function colScanBytes(rows, rowBytes, cols, selected, ratio) {
    return Rdiv(Rmul(R(BigInt(rows), 1n), Rmul(columnBytes(rowBytes, cols),
                R(BigInt(selected), 1n))), ratio);
  }
  function scanSeconds(bytes, bwBps) { return Rdiv(bytes, bwBps); }
  /* The number of selected columns at which the two scans cost the same:
     sel/cols / colRatio = 1 / rowRatio, so sel = cols * colRatio / rowRatio.
     When that exceeds the column count, no selection flips a scan -- and the
     page says so instead of printing a column that does not exist. */
  function colCrossover(cols, rowRatio, colRatio) {
    return Rdiv(Rmul(R(BigInt(cols), 1n), colRatio), rowRatio);
  }
  /* The misconception, counted. Fetching one WHOLE row is one page in a row
     store and one page per column in a column store: columnar is not always
     faster, and this is the query where it loses. An unknown layout throws,
     because a silent default here would show a reader a row-store count under
     a column-store heading. */
  function wholeRowIos(cols, layout) {
    if (layout === 'row') return 1n;
    if (layout === 'column') return BigInt(cols);
    throw new Error('wholeRowIos: unknown layout ' + layout);
  }

  /* ============ L10: the page cache is course 4's cache ====================

     Memory over dataset is the cached fraction, the Zipf exponent is the skew,
     and the hit rate is the same ratio of harmonics. `zipfHit` is
     sysdesign_core.py's -- the SAME function the cache kit calls -- so the two
     courses cannot drift apart. */
  function pageCount(bytes, pageBytes) { return Rfloor(Rdiv(bytes, pageBytes)); }
  function wsHit(c, n, s, limit) {
    if (c <= 0) return { rounded: false, exact: R(0n, 1n), value: 0 };
    if (c >= n) return { rounded: false, exact: R(1n, 1n), value: 1 };
    /* s = 0 is uniform popularity, where H(n,0) = n exactly at any n. No
       approximation is needed and none is used -- and this is also the control
       the lesson compares the skewed case against. */
    if (s === 0) {
      var u = R(BigInt(c), BigInt(n));
      return { rounded: false, exact: u, value: Rflt(u) };
    }
    if (n <= limit) {
      var r = zipfHit(c, n, s);
      return { rounded: false, exact: r, value: Rflt(r) };
    }
    /* Past the limit the exact harmonic is neither computable in a redraw nor
       readable on a page, so this rounds and SAYS it rounds. */
    return { rounded: true, exact: null, value: harmonicApprox(c, s) / harmonicApprox(n, s) };
  }
  /* What is left for the disk: (1 - h) * reads. */
  function diskIopsExact(reads, h) {
    return Rmul(R(BigInt(reads), 1n), Rsub(R(1n, 1n), h));
  }
  function diskIopsApprox(reads, hValue) { return reads * (1 - hValue); }

  /* ============ L11: two different numbers ================================

     RPO is a number of BYTES -- everything written since the last backup, all
     of which a restore loses. RTO is a number of HOURS -- copy the dataset
     back, then replay the log that covers the gap. "We have backups" answers
     neither question. */
  function rpoBytes(intervalSec, writeBps) { return Rmul(intervalSec, writeBps); }
  /* The worst case is a failure the instant before the next backup; the
     expected case is half an interval, because the failure lands uniformly
     inside it. */
  function rpoExpectedBytes(intervalSec, writeBps) {
    return Rdiv(rpoBytes(intervalSec, writeBps), R(2n, 1n));
  }
  function restoreSeconds(sizeBytes, restoreBps) { return Rdiv(sizeBytes, restoreBps); }
  function replaySeconds(logBytes, replayBps) { return Rdiv(logBytes, replayBps); }
  function rtoSeconds(sizeBytes, restoreBps, logBytes, replayBps) {
    return Radd(restoreSeconds(sizeBytes, restoreBps), replaySeconds(logBytes, replayBps));
  }
  /* The longest backup interval that still fits an RTO target. Null when the
     copy alone blows it -- at which point the schedule is not the problem and
     the page says which number is. */
  function intervalForRto(sizeBytes, restoreBps, writeBps, replayBps, targetSec) {
    var left = Rsub(targetSec, restoreSeconds(sizeBytes, restoreBps));
    if (Rcmp(left, R(0n, 1n)) <= 0) return null;
    return Rdiv(Rmul(left, replayBps), writeBps);
  }
"""

_CORE_JS = RATIONAL_JS + RCEIL_JS + HARMONIC_JS + QUEUE_JS + APPROX_JS + STORAGE_JS

# The page count at which the exact harmonic stops being computable in a
# redraw and readable on a page. Stated once, used by `workingset`, and printed
# on that page beside every figure it makes rounded.
EXACT_LIMIT = 40


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the path uses, so a reader
# moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _preset(values):
    """Embed a mode's worked example as a JS literal.

    json.dumps output is valid JS, and the escape makes "</script>"
    structurally impossible -- the argument common.cfg_literal makes.
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


def _table(cid):
    return (
        '      <div class="table-wrap" style="margin-top:12px;">'
        '<table class="tt" id="%s"></table></div>\n' % cid
    )


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
# L1 - io: sequential against random
# ---------------------------------------------------------------------------

# Chunk sizes in DECIMAL bytes, so 4 kB is 4000 B and the lesson's 250x is the
# number that comes out. Held as an index because a slider over four orders of
# magnitude is unusable linearly.
_CHUNKS = [500, 1000, 4000, 16000, 64000, 250000, 1000000, 4000000, 16000000]

# Three devices, as (seek microseconds, bandwidth MB/s). The disk is L1's
# worked example; the other two are the same arithmetic on hardware that moved
# the seek by two orders of magnitude and the bandwidth by one.
_DEVICES = [
    ("disk", "Spinning disk &mdash; 10 ms seek, 100 MB/s", 10000, 100),
    ("ssd", "SATA SSD &mdash; 100 &micro;s, 500 MB/s", 100, 500),
    ("nvme", "NVMe &mdash; 20 &micro;s, 3000 MB/s", 20, 3000),
]


def _io(cfg):
    chunk_ix = int(cfg.get("chunk_ix", 2))
    seek_us = int(cfg.get("seek_us", 10000))
    bw_mb = int(cfg.get("bw_mb", 100))
    size_gb = int(cfg.get("size_gb", 1))
    device = cfg.get("device", "disk")

    markup = (
        _toolbar(
            "The pattern, not the size",
            "time = seeks &times; t<sub>seek</sub> + bytes / bandwidth, both ways",
            [
                ("cyan", "sequential"),
                ("red", "random"),
                ("amber", "crossover chunk"),
                ("muted", "log scale"),
            ],
        )
        + _stage(
            _svg(
                "ioPlot",
                "0 0 660 220",
                "Sequential and random read times as logarithmic bars, with the ratio "
                "plotted against chunk size and the crossover chunk marked.",
            )
        )
        + _table("ioTable")
        + _banner("ioStatus")
    )
    controls = (
        _select("ioDev", "Device", [(k, t) for k, t, _s, _b in _DEVICES] + [("custom", "Custom &mdash; the sliders below")], device)
        + _range("ioChunk", "Chunk size per read", 0, len(_CHUNKS) - 1, chunk_ix, 1)
        + _range("ioSeek", "Seek time t<sub>seek</sub> (&micro;s)", 10, 20000, seek_us, 10)
        + _range("ioBw", "Sequential bandwidth (MB/s)", 50, 5000, bw_mb, 50)
        + _range("ioSize", "Total to read (GB)", 1, 20, size_gb, 1)
        + _kpis(
            [
                ("Sequential time", "ioSeq"),
                ("Random time", "ioRand"),
                ("Random &divide; sequential", "ioRatio"),
                ("Crossover chunk t<sub>seek</sub> &times; bw", "ioCross"),
            ]
        )
        + _hint(
            "ioHint",
            "Bytes here are decimal: 1 kB = 1000 B and 1 GB = 10<sup>9</sup> B. It is not a "
            "detail. The same gigabyte in 4 kB random reads is 250.75 times the sequential "
            "time in these units and 262.9 times it in binary ones, and a reader checking "
            "the arithmetic has to know which 250 is being quoted.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "chunk": chunk_ix,
                "seek": seek_us,
                "bw": bw_mb,
                "size": size_gb,
                "device": device,
                "chunks": _CHUNKS,
                "devices": [[k, s, b] for k, _t, s, b in _DEVICES],
            }
        )
        + r"""
  var devS = document.getElementById('ioDev');
  var chunkS = document.getElementById('ioChunk');
  var seekS = document.getElementById('ioSeek');
  var bwS = document.getElementById('ioBw');
  var sizeS = document.getElementById('ioSize');
  var plot = document.getElementById('ioPlot');
  var table = document.getElementById('ioTable');
  var status = document.getElementById('ioStatus');

  function chunkLabel(bytes) { return byteText(R(BigInt(bytes), 1n)); }

  function redraw() {
    var ci = Math.min(+chunkS.value, PRESET.chunks.length - 1);
    var chunkB = PRESET.chunks[ci];
    var us = +seekS.value, mb = +bwS.value, gb = +sizeS.value;

    var seekSec = R(BigInt(us), 1000000n);
    var bwBps = R(BigInt(mb) * 1000000n, 1n);
    var total = R(BigInt(gb) * 1000000000n, 1n);
    var chunk = R(BigInt(chunkB), 1n);

    document.getElementById('ioChunkOut').innerHTML = chunkLabel(chunkB);
    document.getElementById('ioSeekOut').innerHTML = secText(seekSec);
    document.getElementById('ioBwOut').textContent = grp(mb) + ' MB/s';
    document.getElementById('ioSizeOut').textContent = gb + ' GB';

    var seeks = seekCount(total, chunk);
    var rand = randomTime(total, chunk, seekSec, bwBps);
    var seq = seqTime(total, seekSec, bwBps);
    var ratio = ioRatio(total, chunk, seekSec, bwBps);
    var cross = crossoverChunk(seekSec, bwBps);

    document.getElementById('ioSeq').innerHTML = secText(seq);
    document.getElementById('ioRand').innerHTML = secText(rand);
    document.getElementById('ioRatio').innerHTML = Rfix(ratio, 2) + '&times;';
    document.getElementById('ioCross').innerHTML = byteText(cross);

    /* Every row recomputes the SAME formula at a different chunk. Nothing is
       stored: the 250 the lesson quotes is row three of this table. */
    var rows = '', i;
    for (i = 0; i < PRESET.chunks.length; i += 1) {
      var cb = R(BigInt(PRESET.chunks[i]), 1n);
      var rt = randomTime(total, cb, seekSec, bwBps);
      var rr = Rdiv(rt, seq);
      var here = i === ci;
      var win = Rcmp(cb, cross) >= 0;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + chunkLabel(PRESET.chunks[i])
        + (here ? ' &larr;' : '') + '</td><td>' + grp(seekCount(total, cb)) + '</td><td>'
        + secText(rt) + '</td><td>' + Rfix(rr, 2) + '&times;</td><td class="'
        + (win ? 'tone-green">bandwidth-bound' : 'tone-red">seek-bound') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>chunk</th><th>seeks</th><th>random time</th>'
      + '<th>&divide; sequential</th><th>which term dominates</th></tr></thead><tbody>'
      + rows + '</tbody>';

    /* ---- the drawing: two logarithmic bars, then the ratio curve ---- */
    var x0 = 40, wid = 580;
    var lo = Math.log10(Math.max(Rflt(seq), 1e-9));
    var hi = Math.log10(Math.max(Rflt(rand), 1e-9));
    var span = Math.max(hi - lo, 0.5);
    function barW(t) { return Math.max(6, wid * (Math.log10(Math.max(t, 1e-9)) - lo + span * 0.15) / (span * 1.15)); }

    var s = '<text x="' + x0 + '" y="16" font-size="11" fill="var(--muted)">'
      + gb + ' GB, one seek then the bytes</text>'
      + '<rect x="' + x0 + '" y="22" width="' + barW(Rflt(seq)) + '" height="22" rx="3" '
      + 'fill="var(--cyan)" opacity="0.9" />'
      + '<text x="' + (x0 + barW(Rflt(seq)) + 8) + '" y="38" font-size="11" fill="var(--cyan)" '
      + 'font-weight="700">' + secText(seq) + '</text>'
      + '<text x="' + x0 + '" y="66" font-size="11" fill="var(--muted)">the same '
      + gb + ' GB in ' + grp(seeks) + ' reads of ' + chunkLabel(chunkB) + '</text>'
      + '<rect x="' + x0 + '" y="72" width="' + barW(Rflt(rand)) + '" height="22" rx="3" '
      + 'fill="var(--red)" opacity="0.9" />'
      + '<text x="' + (x0 + barW(Rflt(rand)) + 8) + '" y="88" font-size="11" fill="var(--red)" '
      + 'font-weight="700">' + secText(rand) + '</text>'
      + '<text x="' + x0 + '" y="108" font-size="10" fill="var(--muted)">bar widths are '
      + 'logarithmic; the ratio printed beside them is exact</text>';

    /* the ratio against chunk size, on the same log-spaced axis as the table */
    var ay = 190, atop = 124, n = PRESET.chunks.length;
    var maxLog = 0, pts = [], j;
    for (j = 0; j < n; j += 1) {
      var rj = Math.log10(Math.max(Rflt(Rdiv(randomTime(total, R(BigInt(PRESET.chunks[j]), 1n), seekSec, bwBps), seq)), 1));
      pts.push(rj);
      if (rj > maxLog) maxLog = rj;
    }
    var path = '';
    for (j = 0; j < n; j += 1) {
      var px = x0 + (wid * j) / (n - 1), py = ay - (ay - atop) * (pts[j] / (maxLog || 1));
      path += (j ? ' L ' : 'M ') + px + ' ' + py;
    }
    s += '<line x1="' + x0 + '" y1="' + ay + '" x2="' + (x0 + wid) + '" y2="' + ay
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<path d="' + path + '" fill="none" stroke="var(--purple)" stroke-width="2" />'
      + '<text x="' + x0 + '" y="' + (atop - 4) + '" font-size="11" fill="var(--purple)">'
      + 'random &divide; sequential, against chunk size (log)</text>';
    /* where the crossover chunk falls on that axis */
    var ck = Rflt(cross), placed = -1;
    for (j = 0; j + 1 < n; j += 1) {
      if (ck >= PRESET.chunks[j] && ck <= PRESET.chunks[j + 1]) {
        placed = j + (ck - PRESET.chunks[j]) / (PRESET.chunks[j + 1] - PRESET.chunks[j]);
      }
    }
    if (placed >= 0) {
      var cx = x0 + (wid * placed) / (n - 1);
      s += '<line x1="' + cx + '" y1="' + atop + '" x2="' + cx + '" y2="' + (ay + 6)
        + '" stroke="var(--amber)" stroke-width="2" stroke-dasharray="4 3" />'
        + '<text x="' + (cx + 4) + '" y="' + (atop + 12) + '" font-size="10" fill="var(--amber)">'
        + 'crossover ' + byteText(cross) + '</text>';
    }
    var cxNow = x0 + (wid * ci) / (n - 1);
    s += '<circle cx="' + cxNow + '" cy="' + (ay - (ay - atop) * (pts[ci] / (maxLog || 1)))
      + '" r="4" fill="var(--red)" />'
      + '<text x="' + x0 + '" y="' + (ay + 16) + '" font-size="10" fill="var(--muted)">'
      + chunkLabel(PRESET.chunks[0]) + '</text>'
      + '<text x="' + (x0 + wid) + '" y="' + (ay + 16) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">' + chunkLabel(PRESET.chunks[n - 1]) + '</text>';
    plot.innerHTML = s;

    var seekTerm = Rmul(R(seeks, 1n), seekSec), byteTerm = Rdiv(total, bwBps);
    status.innerHTML = 'Reading ' + gb + ' GB sequentially is one seek and then the bytes: '
      + secText(seekSec) + ' + ' + secText(byteTerm) + ' = <strong>' + secText(seq)
      + '</strong>. Reading the same ' + gb + ' GB in ' + grp(seeks) + ' chunks of '
      + chunkLabel(chunkB) + ' is <em>the same second term</em> and ' + grp(seeks)
      + ' seeks: ' + secText(seekTerm) + ' + ' + secText(byteTerm) + ' = <strong>'
      + secText(rand) + '</strong>, which is ' + Rfix(ratio, 2)
      + ' times as long. Every byte of the difference is the first term &mdash; which is '
      + 'why "size &divide; bandwidth" is the wrong model for a random read and the right '
      + 'one for a sequential one. The two terms are equal at a chunk of <strong>'
      + byteText(cross) + '</strong>: below it the arm decides the time and the size of the '
      + 'read barely matters, above it the bandwidth decides and the seek barely matters.';
  }

  function applyDevice() {
    var key = devS.value, i;
    for (i = 0; i < PRESET.devices.length; i += 1) {
      if (PRESET.devices[i][0] === key) {
        seekS.value = PRESET.devices[i][1];
        bwS.value = PRESET.devices[i][2];
      }
    }
    redraw();
  }
  devS.addEventListener('change', applyDevice);
  [chunkS, sizeS].forEach(function (el) { el.addEventListener('input', redraw); });
  [seekS, bwS].forEach(function (el) {
    el.addEventListener('input', function () { devS.value = 'custom'; redraw(); });
  });

  chunkS.value = PRESET.chunk; seekS.value = PRESET.seek;
  bwS.value = PRESET.bw; sizeS.value = PRESET.size; devS.value = PRESET.device;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Sequential against random, in seeks and bytes",
        subtitle="One gigabyte is ten seconds or forty-two minutes, and the difference is the seek count",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the chunk, the device and the size",
        panel_intro="Both times come out of one formula, seeks &times; t<sub>seek</sub> + bytes / "
        "bandwidth, evaluated at one seek and at one seek per chunk. The crossover is where "
        "its two terms are equal.",
    )


# ---------------------------------------------------------------------------
# L2 - btree: the height, by integer search
# ---------------------------------------------------------------------------


def _btree(cfg):
    mant = int(cfg.get("mant", 1))
    exp = int(cfg.get("exp", 9))
    fanout = int(cfg.get("fanout", 500))
    cached = int(cfg.get("cached", 2))

    markup = (
        _toolbar(
            "Height is the smallest h with B<sup>h</sup> &ge; N",
            "Found by multiplying, not by a logarithm &mdash; and then minus the cached levels",
            [
                ("cyan", "cached level"),
                ("purple", "level read from disk"),
                ("amber", "the level that reaches N"),
                ("red", "what a logarithm would say"),
            ],
        )
        + _stage(
            _svg(
                "btTree",
                "0 0 520 240",
                "The levels of a B-tree drawn as rows of nodes, cached levels tinted, with "
                "the running capacity beside each.",
            )
        )
        + _table("btTable")
        + _banner("btStatus")
    )
    controls = (
        _range("btMant", "Keys N &mdash; leading digit", 1, 9, mant, 1)
        + _range("btExp", "Keys N &mdash; power of ten", 3, 12, exp, 1)
        + _range("btB", "Fanout B (entries per page)", 2, 1000, fanout, 1)
        + _range("btCached", "Levels held in the page cache", 0, 6, cached, 1)
        + _kpis(
            [
                ("Height &lceil;log<sub>B</sub> N&rceil;", "btHeight"),
                ("Capacity B<sup>h</sup>", "btCap"),
                ("I/Os per lookup", "btIos"),
                ("A logarithm would say", "btLog"),
            ]
        )
        + _hint(
            "btHint",
            "&quot;log N is slow for big N&quot; is the misconception. Multiply the fanout out "
            "and look: the height only moves when N crosses a whole power of B, so a thousandfold "
            "more data costs one more level, and the page cache is holding the first two of them "
            "anyway.",
        )
    )

    script = (
        _CORE_JS
        + _preset({"mant": mant, "exp": exp, "b": fanout, "cached": cached})
        + r"""
  var mantS = document.getElementById('btMant');
  var expS = document.getElementById('btExp');
  var bS = document.getElementById('btB');
  var cachedS = document.getElementById('btCached');
  var plot = document.getElementById('btTree');
  var table = document.getElementById('btTable');
  var status = document.getElementById('btStatus');

  /* N as a BigInt, so 9 x 10^12 is a number and not a float. */
  function keysOf(m, e) { return BigInt(m) * 10n ** BigInt(e); }

  function redraw() {
    var m = +mantS.value, e = +expS.value, b = +bS.value, cache = +cachedS.value;
    var N = keysOf(m, e);

    document.getElementById('btMantOut').textContent = m;
    document.getElementById('btExpOut').innerHTML = '10<sup>' + e + '</sup> &mdash; N = ' + grp(N);
    document.getElementById('btBOut').textContent = b + ' per page';
    document.getElementById('btCachedOut').textContent = cache + (cache === 1 ? ' level' : ' levels');

    var h = btreeHeight(N, b);
    var ios = lookupIos(N, b, cache);
    var byLog = btreeHeightByLog(Number(N), b);
    var cap = btreeCapacity(b, h);

    document.getElementById('btHeight').textContent = h + (h === 1 ? ' level' : ' levels');
    document.getElementById('btCap').innerHTML = grp(cap) + ' keys';
    document.getElementById('btIos').textContent = ios + (ios === 1 ? ' page read' : ' page reads');
    document.getElementById('btLog').innerHTML = byLog === h
      ? byLog + ' &mdash; agrees here'
      : '<span class="tone-red">' + byLog + ' &mdash; wrong</span>';

    /* The search itself, one row per multiplication. This IS the computation
       the height came from, not a description of it. */
    var rows = '', level, acc = 1n;
    for (level = 1; level <= h; level += 1) {
      acc *= BigInt(b);
      var nodes = btreeNodes(b, level);
      var reached = acc >= N;
      var isCached = level <= cache;
      rows += '<tr><td>' + level + '</td><td>' + grp(nodes) + '</td><td>' + grp(acc)
        + '</td><td>' + byteText(Rmul(R(nodes, 1n), R(4000n, 1n))) + '</td><td class="'
        + (isCached ? 'tone-cyan">cached, free' : 'tone-purple">one disk read')
        + '</td><td>' + (reached ? '<span class="tone-amber">B<sup>' + level
            + '</sup> &ge; N &mdash; stop</span>' : 'still short of N') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>level</th><th>nodes B<sup>L-1</sup></th>'
      + '<th>keys covered B<sup>L</sup></th><th>level size at 4 kB a page</th>'
      + '<th>cost of a lookup</th><th>search</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: one row of node boxes per level ---- */
    var x0 = 30, wid = 460, top = 30, rowH = Math.min(34, 180 / Math.max(h, 1));
    var s = '<text x="' + x0 + '" y="18" font-size="11" fill="var(--muted)">'
      + grp(N) + ' keys at B = ' + b + ': ' + h + (h === 1 ? ' level' : ' levels') + ', of which '
      + Math.min(cache, h) + ' cached</text>';
    var level2, acc2 = 1n;
    for (level2 = 1; level2 <= h; level2 += 1) {
      acc2 *= BigInt(b);
      var y = top + (level2 - 1) * rowH;
      var boxes = Math.min(Number(btreeNodes(b, level2) > 24n ? 24n : btreeNodes(b, level2)), 24);
      var bw = Math.min(16, (wid - 130) / Math.max(boxes, 1) - 2);
      var isC = level2 <= cache;
      var fill = isC ? 'var(--cyan)' : 'var(--purple)';
      var j;
      for (j = 0; j < boxes; j += 1) {
        s += '<rect x="' + (x0 + j * (bw + 2)) + '" y="' + y + '" width="' + bw
          + '" height="' + (rowH - 10) + '" rx="2" fill="' + fill + '" opacity="'
          + (isC ? '0.9' : '0.55') + '" />';
      }
      if (btreeNodes(b, level2) > 24n) {
        s += '<text x="' + (x0 + boxes * (bw + 2) + 4) + '" y="' + (y + rowH - 16)
          + '" font-size="10" fill="var(--muted)">&hellip; ' + grp(btreeNodes(b, level2))
          + ' nodes</text>';
      }
      s += '<text x="' + (x0 + wid - 130) + '" y="' + (y + rowH - 16) + '" font-size="10" fill="'
        + (isC ? 'var(--cyan)' : 'var(--purple)') + '">L' + level2 + ': covers ' + grp(acc2)
        + '</text>';
    }
    var baseY = top + h * rowH + 8;
    s += '<line x1="' + x0 + '" y1="' + baseY + '" x2="' + (x0 + wid) + '" y2="' + baseY
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="' + x0 + '" y="' + (baseY + 18) + '" font-size="11" fill="var(--amber)">'
      + 'B<sup>' + h + '</sup> = ' + grp(cap) + ' &ge; ' + grp(N) + ', and B<sup>' + (h - 1)
      + '</sup> = ' + grp(btreeCapacity(b, h - 1)) + ' is not</text>'
      + '<text x="' + x0 + '" y="' + (baseY + 36) + '" font-size="11" fill="var(--purple)" '
      + 'font-weight="700">a lookup reads ' + ios + ' of the ' + h + ' levels from disk</text>';
    plot.innerHTML = s;

    status.innerHTML = 'N = ' + grp(N) + ' keys at a fanout of ' + b + ' is <strong>' + h
      + (h === 1 ? ' level' : ' levels') + '</strong>, found by multiplying ' + b
      + ' into an accumulator ' + h + ' times and stopping at the first value that reaches N: '
      + grp(btreeCapacity(b, 1)) + (h > 1 ? ', ' + grp(btreeCapacity(b, 2)) : '')
      + (h > 2 ? ', ' + grp(btreeCapacity(b, 3)) : '')
      + (h > 3 ? ', &hellip;, ' + grp(cap) : '') + '. With ' + Math.min(cache, h)
      + ' of those levels resident in the page cache a lookup costs <strong>' + ios
      + (ios === 1 ? ' page read' : ' page reads') + '</strong>, not ' + h + '. '
      + (byLog === h
          ? 'A logarithm agrees at this N &mdash; but it is not always safe: at B = 3, N = 9, '
            + 'Math.log(9)/Math.log(3) is 2.0000000000000004 and its ceiling is 3, a two-level '
            + 'tree reported as three. Try it on the sliders.'
          : '<span class="tone-red">A logarithm says ' + byLog + ' here, and it is wrong.</span> '
            + 'Math.log(N)/Math.log(B) lands a hair on the wrong side of a whole power and the '
            + 'ceiling promotes it, which is exactly why this lab multiplies instead.')
      + ' The misconception the lesson names is that &quot;log N is slow for big N&quot;: move '
      + 'the power-of-ten slider and watch the height sit still for three decades at a time.';
  }

  [mantS, expS, bS, cachedS].forEach(function (el) { el.addEventListener('input', redraw); });
  mantS.value = PRESET.mant; expS.value = PRESET.exp;
  bS.value = PRESET.b; cachedS.value = PRESET.cached;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="The height of a B-tree, counted rather than logged",
        subtitle="A billion keys at B = 500 is four levels, and the cache holds two of them",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set N, the fanout and what the cache holds",
        panel_intro="The height is the smallest h with B<sup>h</sup> &ge; N, found by "
        "multiplication in BigInt. The table is the search itself: one row per multiplication.",
    )


# ---------------------------------------------------------------------------
# L3 - rangeq: a hash index against a tree, on a workload mix
# ---------------------------------------------------------------------------

# Fixed geometry, stated on the page rather than hidden: a 4 kB page holds 500
# index entries and 200 rows.
_RQ_FANOUT = 500
_RQ_PER_PAGE = 200

_RQ_ROWS = [
    (100000, "100 000 rows"),
    (1000000, "1 000 000 rows"),
    (10000000, "10 000 000 rows"),
    (100000000, "100 000 000 rows"),
]


def _rangeq(cfg):
    rows = int(cfg.get("rows", 1000000))
    points = int(cfg.get("points", 900))
    ranges = int(cfg.get("ranges", 100))
    width = int(cfg.get("width", 100))

    markup = (
        _toolbar(
            "One I/O, or the whole table",
            "A hash destroys the order a range needs; a tree pays its height and then walks",
            [
                ("cyan", "point lookups"),
                ("red", "range scans"),
                ("purple", "tree total"),
                ("amber", "crossover"),
            ],
        )
        + _stage(
            _svg(
                "rqPlot",
                "0 0 520 200",
                "Stacked logarithmic bars of the I/O a second each engine does, split into "
                "the point part and the range part.",
            )
        )
        + _table("rqTable")
        + _banner("rqStatus")
    )
    controls = (
        _select("rqRows", "Rows in the table", [(str(v), t) for v, t in _RQ_ROWS], rows)
        + _range("rqPoint", "Point lookups a second", 0, 5000, points, 10)
        + _range("rqRange", "Range scans a second", 0, 500, ranges, 1)
        + _range("rqWidth", "Rows a range returns", 1, 5000, width, 1)
        + _kpis(
            [
                ("Hash index, I/O a second", "rqHash"),
                ("B-tree, I/O a second", "rqTree"),
                ("Tree height", "rqHeight"),
                ("Ranges a second that tie them", "rqCross"),
            ]
        )
        + _hint(
            "rqHint",
            "A page is 4 kB and holds 500 index entries or 200 rows, so the fanout is 500 and a "
            "scan reads rows/200 pages. The one-I/O hash lookup is the expected probe length "
            "&Theta;(1 + &alpha;) under simple uniform hashing, which Algorithms "
            "<span class=\"tt\">data-structures/hashing-with-chaining</span> proves; it is cited "
            "here, not re-derived.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "rows": rows,
                "points": points,
                "ranges": ranges,
                "width": width,
                "b": _RQ_FANOUT,
                "perPage": _RQ_PER_PAGE,
            }
        )
        + r"""
  var rowsS = document.getElementById('rqRows');
  var pointS = document.getElementById('rqPoint');
  var rangeS = document.getElementById('rqRange');
  var widthS = document.getElementById('rqWidth');
  var plot = document.getElementById('rqPlot');
  var table = document.getElementById('rqTable');
  var status = document.getElementById('rqStatus');

  function redraw() {
    var rows = +rowsS.value, p = +pointS.value, r = +rangeS.value, w = +widthS.value;
    var b = PRESET.b, per = PRESET.perPage;

    document.getElementById('rqPointOut').textContent = grp(p) + '/s';
    document.getElementById('rqRangeOut').textContent = grp(r) + '/s';
    document.getElementById('rqWidthOut').textContent = grp(w) + ' rows';

    var hp = hashPointIos(), hr = hashRangeIos(rows, per);
    var tp = treePointIos(rows, b), tr = treeRangeIos(rows, b, w, per);
    var hashTotal = mixIos(p, r, hp, hr);
    var treeTotal = mixIos(p, r, tp, tr);
    var cross = rangeCrossover(p, hp, hr, tp, tr);

    document.getElementById('rqHash').innerHTML = grp(Rfix(hashTotal, 0)) + ' I/O';
    document.getElementById('rqTree').innerHTML = grp(Rfix(treeTotal, 0)) + ' I/O';
    document.getElementById('rqHeight').textContent = btreeHeight(rows, b) + ' levels';
    document.getElementById('rqCross').innerHTML = cross === null
      ? 'nothing ties them'
      : Rtext(cross) + ' = ' + Rfix(cross, 3) + '/s';

    var winner = Rcmp(hashTotal, treeTotal);
    var trows = ''
      + '<tr><td>point lookup</td><td>' + grp(hp) + ' I/O</td><td>' + grp(tp)
      + ' I/O</td><td class="tone-cyan">hash, by ' + grp(tp - hp) + '</td></tr>'
      + '<tr><td>range of ' + grp(w) + ' rows</td><td>' + grp(hr) + ' I/O (full scan)</td><td>'
      + grp(tr) + ' I/O</td><td class="tone-purple">tree, by ' + grp(hr - tr) + '</td></tr>'
      + '<tr><td>' + grp(p) + ' point lookups a second</td><td>'
      + grp(Rfix(Rmul(R(BigInt(p), 1n), R(hp, 1n)), 0)) + '</td><td>'
      + grp(Rfix(Rmul(R(BigInt(p), 1n), R(tp, 1n)), 0)) + '</td><td></td></tr>'
      + '<tr><td>' + grp(r) + ' range scans a second</td><td>'
      + grp(Rfix(Rmul(R(BigInt(r), 1n), R(hr, 1n)), 0)) + '</td><td>'
      + grp(Rfix(Rmul(R(BigInt(r), 1n), R(tr, 1n)), 0)) + '</td><td></td></tr>'
      + '<tr><td><strong>the mix</strong></td><td><strong>' + grp(Rfix(hashTotal, 0))
      + '</strong></td><td><strong>' + grp(Rfix(treeTotal, 0)) + '</strong></td><td class="'
      + (winner <= 0 ? 'tone-cyan">hash wins' : 'tone-purple">tree wins') + '</td></tr>';
    table.innerHTML = '<thead><tr><th>operation</th><th>hash index</th><th>B-tree</th>'
      + '<th>cheaper</th></tr></thead><tbody>' + trows + '</tbody>';

    /* ---- the drawing: two stacked bars, logarithmic ---- */
    var x0 = 120, wid = 370;
    var hi = Math.max(Rflt(hashTotal), Rflt(treeTotal), 1);
    function span(v) { return Math.max(2, wid * Math.log10(Math.max(v, 1) + 1) / Math.log10(hi + 1)); }
    var hPoint = Rflt(Rmul(R(BigInt(p), 1n), R(hp, 1n)));
    var hRange = Rflt(Rmul(R(BigInt(r), 1n), R(hr, 1n)));
    var tPoint = Rflt(Rmul(R(BigInt(p), 1n), R(tp, 1n)));
    var tRange = Rflt(Rmul(R(BigInt(r), 1n), R(tr, 1n)));

    var s = '<text x="10" y="18" font-size="11" fill="var(--muted)">I/O a second, '
      + 'logarithmic; the totals beside the bars are exact</text>'
      + '<text x="10" y="52" font-size="11" fill="var(--text)">hash index</text>'
      + '<rect x="' + x0 + '" y="36" width="' + span(hPoint) + '" height="22" rx="3" '
      + 'fill="var(--cyan)" opacity="0.9" />'
      + '<rect x="' + (x0 + span(hPoint)) + '" y="36" width="'
      + (span(hPoint + hRange) - span(hPoint)) + '" height="22" rx="3" fill="var(--red)" '
      + 'opacity="0.9" />'
      + '<text x="' + (x0 + span(hPoint + hRange) + 8) + '" y="52" font-size="11" '
      + 'fill="var(--red)" font-weight="700">' + grp(Rfix(hashTotal, 0)) + '</text>'
      + '<text x="10" y="100" font-size="11" fill="var(--text)">B-tree</text>'
      + '<rect x="' + x0 + '" y="84" width="' + span(tPoint) + '" height="22" rx="3" '
      + 'fill="var(--cyan)" opacity="0.9" />'
      + '<rect x="' + (x0 + span(tPoint)) + '" y="84" width="'
      + (span(tPoint + tRange) - span(tPoint)) + '" height="22" rx="3" fill="var(--purple)" '
      + 'opacity="0.9" />'
      + '<text x="' + (x0 + span(tPoint + tRange) + 8) + '" y="100" font-size="11" '
      + 'fill="var(--purple)" font-weight="700">' + grp(Rfix(treeTotal, 0)) + '</text>'
      + '<line x1="10" y1="124" x2="510" y2="124" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="144" font-size="11" fill="var(--cyan)">the cyan part is the point '
      + 'lookups, where the hash is ' + grp(tp - hp) + ' I/O cheaper on every one</text>'
      + '<text x="10" y="162" font-size="11" fill="var(--red)">the red part is '
      + grp(r) + ' full scans of ' + grp(hr) + ' pages each &mdash; the order a hash threw '
      + 'away, paid for once a query</text>'
      + '<text x="10" y="182" font-size="11" fill="var(--amber)">'
      + (cross === null
          ? 'no range rate ties the two engines at this width'
          : 'they tie at ' + Rfix(cross, 3) + ' range scans a second')
      + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'On this mix the hash index does <strong>' + grp(Rfix(hashTotal, 0))
      + ' I/O a second</strong> and the B-tree <strong>' + grp(Rfix(treeTotal, 0))
      + '</strong>. The hash is genuinely cheaper per point lookup &mdash; ' + grp(hp)
      + ' against ' + grp(tp) + ' &mdash; and that is the whole of the true claim behind '
      + '&quot;hash is faster&quot;. A range of ' + grp(w) + ' rows costs it ' + grp(hr)
      + ' I/O, because a hash has no order to walk and the only way to find the matching rows '
      + 'is to read them all; the tree pays its ' + btreeHeight(rows, b)
      + '-level descent once and then reads ' + grp(pagesFor(w, per))
      + ' leaf pages in order. '
      + (cross === null
          ? 'At this range width nothing ties them.'
          : 'The two engines tie at <strong>' + Rfix(cross, 3)
            + ' range scans a second</strong> against ' + grp(p) + ' point lookups: '
            + (Rcmp(R(BigInt(r), 1n), cross) > 0
                ? 'you are above it, so the tree wins this workload.'
                : 'you are below it, so the hash wins this workload.'))
      + ' The claim to make about an index is therefore never &quot;faster&quot; but '
      + '&quot;faster at which operation, at what mix&quot;.';
  }

  rowsS.addEventListener('change', redraw);
  [pointS, rangeS, widthS].forEach(function (el) { el.addEventListener('input', redraw); });
  rowsS.value = PRESET.rows; pointS.value = PRESET.points;
  rangeS.value = PRESET.ranges; widthS.value = PRESET.width;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Hash against tree, counted in I/Os",
        subtitle="One I/O for a point lookup, the whole table for a range",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the mix and the range width",
        panel_intro="Both totals are the same two products summed: point rate &times; I/O a point, "
        "plus range rate &times; I/O a range. The crossover is the range rate at which they are equal.",
    )


# ---------------------------------------------------------------------------
# L4 - indexcost: k indexes make an insert k + 1 random writes
# ---------------------------------------------------------------------------


def _indexcost(cfg):
    k = int(cfg.get("k", 3))
    device = int(cfg.get("device", 10000))
    target = int(cfg.get("target", 2500))

    markup = (
        _toolbar(
            "An index is free for readers only",
            "k indexes make one insert k + 1 random writes, so throughput divides by k + 1",
            [
                ("cyan", "the table's own write"),
                ("purple", "one write per index"),
                ("amber", "throughput left"),
                ("red", "below the target"),
            ],
        )
        + _stage(
            _svg(
                "ixPlot",
                "0 0 520 200",
                "One insert drawn as k plus one random writes, with the insert throughput "
                "that leaves shown as a shrinking bar.",
            )
        )
        + _table("ixTable")
        + _banner("ixStatus")
    )
    controls = (
        _range("ixK", "Indexes on the table (k)", 0, 8, k, 1)
        + _range("ixDev", "Random writes the device does a second", 500, 50000, device, 500)
        + _range("ixTarget", "Inserts a second the workload needs", 100, 20000, target, 100)
        + _kpis(
            [
                ("Random writes per insert", "ixWrites"),
                ("Inserts a second", "ixRate"),
                ("Share of the bare rate", "ixShare"),
                ("Most indexes that still meet the target", "ixMaxK"),
            ]
        )
        + _hint(
            "ixHint",
            "The writes are random because the indexes are ordered on different keys: an insert "
            "that is sequential in the table lands in a different place in every index. That is "
            "why the cost is k + 1 <em>random</em> writes and not k + 1 bytes.",
        )
    )

    script = (
        _CORE_JS
        + _preset({"k": k, "device": device, "target": target})
        + r"""
  var kS = document.getElementById('ixK');
  var devS = document.getElementById('ixDev');
  var targetS = document.getElementById('ixTarget');
  var plot = document.getElementById('ixPlot');
  var table = document.getElementById('ixTable');
  var status = document.getElementById('ixStatus');

  function redraw() {
    var k = +kS.value, device = +devS.value, target = +targetS.value;

    document.getElementById('ixKOut').textContent = k + (k === 1 ? ' index' : ' indexes');
    document.getElementById('ixDevOut').textContent = grp(device) + ' writes/s';
    document.getElementById('ixTargetOut').textContent = grp(target) + ' inserts/s';

    var per = writesPerInsert(k);
    var rate = insertRate(device, k);
    var share = throughputShare(k);
    var maxK = maxIndexesFor(device, target);
    var halving = indexesForShare(R(1n, 2n));

    document.getElementById('ixWrites').innerHTML = Rtext(per) + ' &mdash; the table and '
      + k + (k === 1 ? ' index' : ' indexes');
    document.getElementById('ixRate').innerHTML = grp(Rfix(rate, 0)) + ' a second';
    document.getElementById('ixShare').innerHTML = Rtext(share) + ' = ' + Rpct(share, 2);
    document.getElementById('ixMaxK').innerHTML = maxK === null
      ? '<span class="tone-red">none &mdash; the bare table misses it</span>'
      : grp(maxK) + (maxK === 1n ? ' index' : ' indexes');

    /* Every row recomputes device/(k+1). The "k that halves throughput" is not
       asserted anywhere: it is the first row whose share reaches 1/2. */
    var rows = '', i;
    for (i = 0; i <= 8; i += 1) {
      var ri = insertRate(device, i), si = throughputShare(i);
      var meets = Rcmp(ri, R(BigInt(target), 1n)) >= 0;
      var here = i === k;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + i + (here ? ' &larr;' : '')
        + '</td><td>' + Rtext(writesPerInsert(i)) + '</td><td>' + grp(Rfix(ri, 0))
        + '</td><td>' + Rtext(si) + ' = ' + Rpct(si, 1) + '</td><td class="'
        + (meets ? 'tone-green">meets ' : 'tone-red">misses ') + grp(target) + '/s</td>'
        + '<td>' + (BigInt(i) === halving ? '<span class="tone-amber">throughput halved</span>' : '')
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>indexes k</th><th>writes per insert</th>'
      + '<th>inserts a second</th><th>share of bare rate</th><th>against the target</th>'
      + '<th></th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: the writes one insert costs, then what is left ---- */
    var x0 = 24, boxW = 46, gap = 8;
    var s = '<text x="' + x0 + '" y="18" font-size="11" fill="var(--muted)">'
      + 'one insert, in random writes</text>'
      + '<rect x="' + x0 + '" y="26" width="' + boxW + '" height="30" rx="3" '
      + 'fill="var(--cyan)" opacity="0.9" />'
      + '<text x="' + (x0 + boxW / 2) + '" y="46" text-anchor="middle" font-size="10" '
      + 'fill="var(--on-accent)" font-weight="700">table</text>';
    var i2;
    for (i2 = 1; i2 <= k; i2 += 1) {
      var bx = x0 + i2 * (boxW + gap);
      s += '<rect x="' + bx + '" y="26" width="' + boxW + '" height="30" rx="3" '
        + 'fill="var(--purple)" opacity="0.75" />'
        + '<text x="' + (bx + boxW / 2) + '" y="46" text-anchor="middle" font-size="10" '
        + 'fill="var(--on-accent)" font-weight="700">idx ' + i2 + '</text>';
    }
    s += '<text x="' + (x0 + (k + 1) * (boxW + gap) + 6) + '" y="46" font-size="11" '
      + 'fill="var(--text)" font-weight="700">= ' + Rtext(per) + '</text>';

    var barX = 24, barW = 460, bareW = barW, leftW = barW * Rflt(share);
    var targetX = barX + barW * Math.min(1, target / Math.max(device, 1));
    s += '<text x="' + barX + '" y="88" font-size="11" fill="var(--muted)">'
      + 'the device does ' + grp(device) + ' random writes a second, whatever they are for</text>'
      + '<rect x="' + barX + '" y="96" width="' + bareW + '" height="24" rx="3" '
      + 'fill="var(--line-strong)" opacity="0.35" />'
      + '<rect x="' + barX + '" y="96" width="' + Math.max(2, leftW) + '" height="24" rx="3" '
      + 'fill="var(--amber)" opacity="0.9" />'
      + '<text x="' + (barX + 6) + '" y="113" font-size="11" fill="var(--on-accent)" '
      + 'font-weight="700">' + (leftW > 120 ? grp(Rfix(rate, 0)) + ' inserts/s' : '') + '</text>'
      + '<line x1="' + targetX + '" y1="90" x2="' + targetX + '" y2="130" '
      + 'stroke="var(--red)" stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + (targetX + 4) + '" y="142" font-size="10" fill="var(--red)">'
      + 'target ' + grp(target) + '/s</text>'
      + '<text x="' + barX + '" y="170" font-size="11" fill="var(--muted)">'
      + 'the amber bar is ' + Rtext(share) + ' of the grey one, because every insert now costs '
      + Rtext(per) + ' writes instead of one</text>'
      + '<text x="' + barX + '" y="188" font-size="11" fill="'
      + (Rcmp(rate, R(BigInt(target), 1n)) >= 0 ? 'var(--green)' : 'var(--red)') + '">'
      + (Rcmp(rate, R(BigInt(target), 1n)) >= 0
          ? 'still above the target'
          : 'below the target: the indexes, not the device, are the ceiling') + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'With ' + k + (k === 1 ? ' index' : ' indexes')
      + ' an insert is <strong>' + Rtext(per) + ' random writes</strong> &mdash; the row, and '
      + 'one more in every index, each in a different place because every index is ordered on '
      + 'a different key. A device that does ' + grp(device)
      + ' random writes a second therefore does <strong>' + grp(Rfix(rate, 0))
      + ' inserts a second</strong>, which is ' + Rtext(share) + ' of its bare rate. '
      + 'The k that halves throughput is <strong>' + grp(halving) + '</strong>: one index, '
      + 'because 1/(k+1) reaches 1/2 at k = 1 and the page computes that from the share column '
      + 'rather than asserting it. '
      + (maxK === null
          ? 'At this target no number of indexes works &mdash; the bare table already misses it, '
            + 'so the device is the thing to change.'
          : 'At ' + grp(target) + ' inserts a second the most indexes you can carry is <strong>'
            + grp(maxK) + '</strong>, from &lfloor;' + grp(device) + '/' + grp(target)
            + '&rfloor; &minus; 1.')
      + ' Indexes are free for readers and never for writers, and this is the exchange rate.';
  }

  [kS, devS, targetS].forEach(function (el) { el.addEventListener('input', redraw); });
  kS.value = PRESET.k; devS.value = PRESET.device; targetS.value = PRESET.target;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="The write cost of an index",
        subtitle="k + 1 random writes an insert, and the throughput that leaves",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Add indexes and watch the writer pay",
        panel_intro="Insert throughput is the device's random-write rate divided by k + 1, "
        "recomputed as you move k. The table is the same division at every k from none to eight.",
    )


# ---------------------------------------------------------------------------
# L5 - lsm: write amplification
# ---------------------------------------------------------------------------

# A memtable of 64 MB, decimal. Stated on the page, and the only number in this
# mode the reader does not set.
_LSM_MEMTABLE = 64000000


def _lsm(cfg):
    fanout = int(cfg.get("fanout", 10))
    levels = int(cfg.get("levels", 5))
    ingest_mb = int(cfg.get("ingest_mb", 50))
    data_gb = int(cfg.get("data_gb", 1000))

    markup = (
        _toolbar(
            "Append-only is not the same as cheap",
            "Each byte is rewritten about F/2 times per level, so WA &asymp; L&middot;F/2",
            [
                ("cyan", "bytes ingested"),
                ("red", "bytes compaction rewrites"),
                ("purple", "a level"),
                ("amber", "levels the data forces"),
            ],
        )
        + _stage(
            _svg(
                "lsPyramid",
                "0 0 660 240",
                "The levels of an LSM tree as a pyramid, each labelled with its capacity and "
                "the bytes compaction rewrites there.",
            )
        )
        + _table("lsTable")
        + _banner("lsStatus")
    )
    controls = (
        _range("lsF", "Fanout F between levels", 2, 20, fanout, 1)
        + _range("lsL", "Levels L", 1, 8, levels, 1)
        + _range("lsIngest", "Ingest (MB/s)", 1, 500, ingest_mb, 1)
        + _range("lsData", "Data resident in the tree (GB)", 1, 5000, data_gb, 1)
        + _kpis(
            [
                ("Write amplification L&middot;F/2", "lsWa"),
                ("Read amplification, no filters", "lsRa"),
                ("Compaction bandwidth", "lsBw"),
                ("Levels the data forces", "lsLevels"),
            ]
        )
        + _hint(
            "lsHint",
            "F/2 and not F: a level is on average half full of the data it will eventually hold "
            "when the merge into it happens, so a byte passing through is rewritten about F/2 "
            "times there. The read amplification of L is what the next lesson's Bloom filters "
            "cancel &mdash; which is why that lesson exists.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "f": fanout,
                "l": levels,
                "ingest": ingest_mb,
                "data": data_gb,
                "memtable": _LSM_MEMTABLE,
            }
        )
        + r"""
  var fS = document.getElementById('lsF');
  var lS = document.getElementById('lsL');
  var ingestS = document.getElementById('lsIngest');
  var dataS = document.getElementById('lsData');
  var plot = document.getElementById('lsPyramid');
  var table = document.getElementById('lsTable');
  var status = document.getElementById('lsStatus');

  function redraw() {
    var f = +fS.value, l = +lS.value, mb = +ingestS.value, gb = +dataS.value;
    var ingest = R(BigInt(mb) * 1000000n, 1n);
    var data = R(BigInt(gb) * 1000000000n, 1n);
    var memtable = R(BigInt(PRESET.memtable), 1n);

    document.getElementById('lsFOut').textContent = 'F = ' + f;
    document.getElementById('lsLOut').textContent = l + (l === 1 ? ' level' : ' levels');
    document.getElementById('lsIngestOut').textContent = grp(mb) + ' MB/s';
    document.getElementById('lsDataOut').innerHTML = byteText(data);

    var wa = lsmWriteAmp(l, f);
    var ra = lsmReadAmp(l);
    var bw = compactionBw(ingest, wa);
    var forced = levelsForSize(data, memtable, f);

    document.getElementById('lsWa').innerHTML = Rtext(wa) + ' &times; &mdash; '
      + Rfix(wa, 1) + ' bytes written per byte ingested';
    document.getElementById('lsRa').innerHTML = Rtext(ra) + ' levels probed on a miss';
    document.getElementById('lsBw').innerHTML = byteText(bw) + '/s';
    document.getElementById('lsLevels').innerHTML = forced === null
      ? 'a fanout of one never fills'
      : forced + (forced === l
          ? ' &mdash; <span class="tone-green">matches L</span>'
          : ' &mdash; <span class="tone-amber">L is set to ' + l + '</span>');

    /* One row per level: the capacity, the bytes that pass through it, and the
       F/2 rewrites each of those bytes costs. */
    var rows = '', i, cumulative = R(0n, 1n);
    var half = R(BigInt(f), 2n);
    for (i = 1; i <= l; i += 1) {
      var cap = levelCapacity(memtable, f, i);
      var rewritten = Rmul(ingest, half);
      cumulative = Radd(cumulative, half);
      var covered = Rcmp(cap, data) >= 0;
      rows += '<tr><td>L' + i + '</td><td>' + byteText(cap) + '</td><td>' + Rtext(half)
        + ' &times;</td><td>' + byteText(rewritten) + '/s</td><td>' + Rtext(cumulative)
        + ' &times;</td><td class="' + (covered ? 'tone-amber">holds all of it'
            : 'tone-muted">not yet all of it') + '</td></tr>';
    }
    rows += '<tr><td><strong>total</strong></td><td>&mdash;</td><td><strong>' + Rtext(wa)
      + ' &times;</strong></td><td><strong>' + byteText(bw) + '/s</strong></td><td>'
      + Rtext(wa) + ' &times;</td><td></td></tr>';
    table.innerHTML = '<thead><tr><th>level</th><th>capacity memtable&middot;F<sup>L</sup></th>'
      + '<th>rewrites per byte</th><th>bandwidth at this ingest</th><th>cumulative WA</th>'
      + '<th>against the data</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: a pyramid, one bar per level, width by log capacity -- */
    var x0 = 30, wid = 600, top = 40, rowH = Math.min(26, 150 / Math.max(l, 1));
    var maxLog = Math.log10(Math.max(Rflt(levelCapacity(memtable, f, l)), 10));
    var minLog = Math.log10(Math.max(Rflt(memtable), 10));
    var s = '<text x="' + x0 + '" y="18" font-size="11" fill="var(--cyan)">'
      + grp(mb) + ' MB/s in at the memtable</text>'
      + '<text x="' + x0 + '" y="32" font-size="11" fill="var(--red)">'
      + byteText(bw) + '/s out at the disk &mdash; ' + Rtext(wa) + ' times as much</text>';
    var j;
    for (j = 1; j <= l; j += 1) {
      var capj = levelCapacity(memtable, f, j);
      var frac = (Math.log10(Math.max(Rflt(capj), 10)) - minLog) / Math.max(maxLog - minLog, 0.5);
      var w = Math.max(40, wid * (0.18 + 0.82 * frac));
      var y = top + (j - 1) * rowH;
      s += '<rect x="' + x0 + '" y="' + y + '" width="' + w + '" height="' + (rowH - 6)
        + '" rx="3" fill="var(--purple)" opacity="' + (0.35 + 0.06 * j) + '" />'
        + '<text x="' + (x0 + 6) + '" y="' + (y + rowH - 14) + '" font-size="10" '
        + 'fill="var(--text)">L' + j + ' &mdash; ' + byteText(capj) + '</text>'
        + '<text x="' + (x0 + w + 6) + '" y="' + (y + rowH - 14) + '" font-size="10" '
        + 'fill="var(--red)">+' + Rtext(half) + ' &times; rewrite</text>';
    }
    var ly = top + l * rowH + 14;
    s += '<line x1="' + x0 + '" y1="' + ly + '" x2="' + (x0 + wid) + '" y2="' + ly
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="' + x0 + '" y="' + (ly + 20) + '" font-size="11" fill="var(--red)" '
      + 'font-weight="700">' + l + ' &times; ' + Rtext(half) + ' = ' + Rtext(wa)
      + ' bytes written for every byte ingested</text>'
      + '<text x="' + x0 + '" y="' + (ly + 38) + '" font-size="11" fill="var(--purple)">'
      + 'and a lookup that misses asks all ' + l + ' levels: read amplification '
      + Rtext(ra) + ', which the next lesson cancels with a filter</text>'
      + '<text x="' + x0 + '" y="' + (ly + 56) + '" font-size="10" fill="var(--amber)">'
      + (forced === null ? ''
          : byteText(data) + ' over a ' + byteText(memtable) + ' memtable at F = ' + f
            + ' forces ' + forced + (forced === 1 ? ' level' : ' levels')
            + ', by the same integer search the B-tree height uses')
      + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A levelled LSM with fanout ' + f + ' and ' + l
      + (l === 1 ? ' level' : ' levels') + ' writes <strong>' + Rtext(wa)
      + ' bytes for every byte you hand it</strong>: ' + l + ' levels, each rewriting a byte '
      + 'about ' + Rtext(half) + ' times as it merges. At ' + grp(mb)
      + ' MB/s of ingest that is <strong>' + byteText(bw) + '/s of disk write bandwidth</strong> '
      + '&mdash; the number to size the device against, and it is ' + Rtext(wa)
      + ' times the one most people size against. '
      + (forced === null ? ''
          : byteText(data) + ' of data over a ' + byteText(memtable) + ' memtable actually forces '
            + forced + (forced === 1 ? ' level' : ' levels') + ', found the same way a B-tree '
            + 'height is: multiply F in until the capacity reaches the data. ')
      + 'Read amplification is <strong>' + Rtext(ra)
      + '</strong> before filters, because a key that is not there has to be looked for on every '
      + 'level. That number is what &ldquo;Bloom Filters: Bits per Key&rdquo; cancels, and it is the reason that lesson is a '
      + 'lesson rather than a paragraph: "append-only, therefore cheap" is wrong on both axes at '
      + 'once, and only one of them can be bought back.';
  }

  [fS, lS, ingestS, dataS].forEach(function (el) { el.addEventListener('input', redraw); });
  fS.value = PRESET.f; lS.value = PRESET.l;
  ingestS.value = PRESET.ingest; dataS.value = PRESET.data;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Write amplification in an LSM tree",
        subtitle="L levels at F/2 rewrites each, and the compaction bandwidth that implies",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the fanout, the levels and the ingest",
        panel_intro="Write amplification is L &times; F/2, summed one level at a time in the "
        "table, and the compaction bandwidth is the ingest rate multiplied by it.",
    )


# ---------------------------------------------------------------------------
# L6 - bloom: bits per key
# ---------------------------------------------------------------------------

# The small case where the EXACT form is evaluable, so the page can show what
# the approximation costs instead of only naming it.
_BLOOM_EXACT_M = 64
_BLOOM_EXACT_N = 8
_BLOOM_EXACT_K = 5


def _bloom(cfg):
    mant = int(cfg.get("mant", 1))
    exp = int(cfg.get("exp", 9))
    p_exp = int(cfg.get("p_exp", 2))
    levels = int(cfg.get("levels", 5))

    markup = (
        _toolbar(
            "Bits per key, and which constant it came from",
            "log<sub>2</sub>(1/p) / ln 2 bits a key, independent of n &mdash; and it rounds",
            [
                ("cyan", "a set bit"),
                ("purple", "a hash function"),
                ("red", "rounded figure"),
                ("green", "read amplification with filters"),
            ],
        )
        + _stage(
            _svg(
                "bfPlot",
                "0 0 660 220",
                "A small bit array with the hash functions of one key drawn onto it, beside "
                "bars for read amplification before and after filters.",
            )
        )
        + _table("bfTable")
        + _banner("bfStatus")
    )
    controls = (
        _range("bfMant", "Keys n &mdash; leading digit", 1, 9, mant, 1)
        + _range("bfExp", "Keys n &mdash; power of ten", 5, 11, exp, 1)
        + _range("bfP", "Target false-positive rate: one in 10^j", 1, 5, p_exp, 1)
        + _range("bfL", "LSM levels carried over from L5", 2, 8, levels, 1)
        + _kpis(
            [
                ("Bits per key, 1/ln2 = 1.4427", "bfBits"),
                ("Bits per key, textbook 1.44", "bfTextbook"),
                ("Filter size m, and its memory", "bfM"),
                ("Hash functions k", "bfK"),
                ("Read amplification before", "bfRaBefore"),
                ("Read amplification after", "bfRaAfter"),
            ]
        )
        + _hint(
            "bfHint",
            "The error is one-sided. A clear bit is a certain negative &mdash; if any of the k "
            "positions is zero the key was never inserted &mdash; and that is the design fact the "
            "whole use depends on: the filter can waste a read, never lose one. The derivation of "
            "the rate, the optimal k, and the rule that a filter supports no deletion are "
            "Algorithms <span class=\"tt\">randomised-algorithms/bloom-filters</span>.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "mant": mant,
                "exp": exp,
                "p": p_exp,
                "levels": levels,
                "exactM": _BLOOM_EXACT_M,
                "exactN": _BLOOM_EXACT_N,
                "exactK": _BLOOM_EXACT_K,
            }
        )
        + r"""
  var mantS = document.getElementById('bfMant');
  var expS = document.getElementById('bfExp');
  var pS = document.getElementById('bfP');
  var lS = document.getElementById('bfL');
  var plot = document.getElementById('bfPlot');
  var table = document.getElementById('bfTable');
  var status = document.getElementById('bfStatus');

  function redraw() {
    var m = +mantS.value, e = +expS.value, j = +pS.value, l = +lS.value;
    var n = m * Math.pow(10, e);
    var p = Math.pow(10, -j);
    var pExact = R(1n, 10n ** BigInt(j));

    document.getElementById('bfMantOut').textContent = m;
    document.getElementById('bfExpOut').innerHTML = '10<sup>' + e + '</sup> &mdash; n = ' + grp(n);
    document.getElementById('bfPOut').innerHTML = 'p = ' + Rtext(pExact) + ' = ' + Rpct(pExact, j > 2 ? j : 2);
    document.getElementById('bfLOut').textContent = l + ' levels';

    var bits = bitsPerKeyApprox(p);
    var textbook = bitsPerKeyTextbook(p);
    var mBits = bloomBits(n, p);
    var k = bloomHashes(p);
    var memory = bloomMemoryBytes(n, p);
    var raBefore = lsmReadAmp(l);
    var raAfter = readAmpWithFilter(l, pExact);
    var achieved = bloomApprox(mBits, n, k);

    document.getElementById('bfBits').innerHTML = '<span class="tone-red">~' + bits.toFixed(4)
      + '</span> bits';
    document.getElementById('bfTextbook').innerHTML = '<span class="tone-red">~'
      + textbook.toFixed(4) + '</span> bits &mdash; ' + (textbook < bits ? 'short by ' : 'over by ')
      + Math.abs(bits - textbook).toFixed(4);
    document.getElementById('bfM').innerHTML = grp(mBits) + ' bits = ' + byteText(memory);
    document.getElementById('bfK').textContent = k + (k === 1 ? ' hash' : ' hashes');
    document.getElementById('bfRaBefore').innerHTML = Rtext(raBefore) + ' levels probed';
    document.getElementById('bfRaAfter').innerHTML = '<span class="tone-green">'
      + Rtext(raAfter) + ' = ' + Rfix(raAfter, 4) + '</span>';

    /* The sizing at five target rates, so "independent of n" is visible: the
       bits-per-key column does not mention n anywhere. */
    var rows = '', i;
    for (i = 1; i <= 5; i += 1) {
      var pi = Math.pow(10, -i), pri = R(1n, 10n ** BigInt(i));
      var bi = bitsPerKeyApprox(pi), ti = bitsPerKeyTextbook(pi);
      var here = i === j;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + Rtext(pri) + ' = '
        + Rpct(pri, i > 2 ? i : 2) + (here ? ' &larr;' : '') + '</td><td>~' + bi.toFixed(4)
        + '</td><td>~' + ti.toFixed(4) + '</td><td>' + (bi - ti).toFixed(4) + '</td><td>'
        + byteText(bloomMemoryBytes(n, pi)) + '</td><td>' + bloomHashes(pi) + '</td><td>'
        + Rfix(readAmpWithFilter(l, pri), 4) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>target p</th><th>bits/key at 1/ln2</th>'
      + '<th>bits/key at 1.44</th><th>difference</th><th>memory for ' + grp(n) + ' keys</th>'
      + '<th>hashes k</th><th>read amp after</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: a small bit array, then the two RA bars ---- */
    var em = PRESET.exactM, en = PRESET.exactN, ek = PRESET.exactK;
    var exact = bloomExactRate(em, en, ek);
    var approx = bloomApprox(em, en, ek);
    var cellW = 8, x0 = 24, y0 = 34;
    var s = '<text x="' + x0 + '" y="20" font-size="11" fill="var(--muted)">'
      + 'the exact form where it is still evaluable: m = ' + em + ' bits, n = ' + en
      + ' keys, k = ' + ek + ' hashes</text>';
    /* A deterministic set of positions, so the picture and the claim come from
       one rule: position (7*key + 13*hash) mod m. Nothing random, nothing
       stored -- a reader can check every square. */
    var setBits = {}, key, hash;
    for (key = 0; key < en; key += 1) {
      for (hash = 0; hash < ek; hash += 1) setBits[(7 * key + 13 * hash) % em] = true;
    }
    var b2;
    for (b2 = 0; b2 < em; b2 += 1) {
      var cx = x0 + (b2 % 32) * cellW, cy = y0 + Math.floor(b2 / 32) * (cellW + 2);
      s += '<rect x="' + cx + '" y="' + cy + '" width="' + (cellW - 1) + '" height="'
        + (cellW - 1) + '" rx="1" fill="' + (setBits[b2] ? 'var(--cyan)' : 'var(--line-strong)')
        + '" opacity="' + (setBits[b2] ? '0.95' : '0.3') + '" />';
    }
    var arrowY = y0 + 2 * (cellW + 2) + 14;
    for (hash = 0; hash < ek; hash += 1) {
      var pos = (7 * 0 + 13 * hash) % em;
      var ax = x0 + (pos % 32) * cellW + cellW / 2;
      var ay = y0 + Math.floor(pos / 32) * (cellW + 2) + cellW;
      s += '<line x1="' + (x0 + 130) + '" y1="' + arrowY + '" x2="' + ax + '" y2="' + ay
        + '" stroke="var(--purple)" stroke-width="1" opacity="0.7" />';
    }
    s += '<circle cx="' + (x0 + 130) + '" cy="' + arrowY + '" r="4" fill="var(--purple)" />'
      + '<text x="' + (x0 + 140) + '" y="' + (arrowY + 4) + '" font-size="10" '
      + 'fill="var(--purple)">one key, ' + ek + ' hashes, ' + ek + ' bits set</text>'
      + '<text x="' + x0 + '" y="' + (arrowY + 24) + '" font-size="11" fill="var(--text)">'
      + 'exact (1 &minus; (1 &minus; 1/m)<tspan dy="-4" font-size="8">kn</tspan>'
      + '<tspan dy="4"></tspan>)<tspan dy="-4" font-size="8">k</tspan><tspan dy="4"></tspan> = '
      + (exact === null ? 'too large' : Rfix(exact, 6)) + '</text>'
      + '<text x="' + x0 + '" y="' + (arrowY + 42) + '" font-size="11" fill="var(--red)">'
      + 'approximation (1 &minus; e<tspan dy="-4" font-size="8">&minus;kn/m</tspan>'
      + '<tspan dy="4"></tspan>)<tspan dy="-4" font-size="8">k</tspan><tspan dy="4"></tspan> = ~'
      + approx.toFixed(6) + ', which is what every figure above uses</text>';

    var bx = 380, bw = 250, raMax = Math.max(Rflt(raBefore), 1);
    s += '<text x="' + bx + '" y="20" font-size="11" fill="var(--muted)">'
      + 'levels a lookup that misses has to read</text>'
      + '<rect x="' + bx + '" y="28" width="' + bw + '" height="22" rx="3" fill="var(--red)" '
      + 'opacity="0.85" />'
      + '<text x="' + (bx + 6) + '" y="44" font-size="11" fill="var(--on-accent)" '
      + 'font-weight="700">no filters: ' + Rtext(raBefore) + '</text>'
      + '<rect x="' + bx + '" y="58" width="' + Math.max(4, bw * Rflt(raAfter) / raMax)
      + '" height="22" rx="3" fill="var(--green)" opacity="0.9" />'
      + '<text x="' + (bx + 6) + '" y="74" font-size="11" fill="var(--on-accent)" '
      + 'font-weight="700">filters: ' + Rfix(raAfter, 3) + '</text>'
      + '<text x="' + bx + '" y="96" font-size="10" fill="var(--muted)">'
      + '1 + (L &minus; 1)p = 1 + ' + (l - 1) + ' &times; ' + Rtext(pExact) + ' = '
      + Rtext(raAfter) + ', exact &mdash; p is a target, not a measurement</text>'
      + '<text x="' + bx + '" y="118" font-size="10" fill="var(--muted)">'
      + 'the filters cost ' + byteText(memory) + ' of memory for ' + grp(n) + ' keys</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A target of ' + Rtext(pExact) + ' costs <strong>~' + bits.toFixed(3)
      + ' bits per key</strong> &mdash; ' + grp(mBits) + ' bits, ' + byteText(memory) + ', for '
      + grp(n) + ' keys at ' + k + ' hash functions &mdash; and that figure does not depend on n '
      + 'at all: doubling the keys doubles the filter and leaves the bits per key where they '
      + 'were. <span class="tone-red">It is rounded.</span> bitsPerKeyApprox is a logarithm and '
      + 'bloomApprox is an exponential built on expNegApprox, which sums the positive-term series '
      + 'for e<sup>x</sup> and divides once, accurate to about 1e-13 across the whole range; '
      + 'neither returns a fraction, and every figure above inherits that. '
      + 'The number a textbook quotes for 1% is 9.57 bits and the number here is <strong>'
      + bits.toFixed(3) + '</strong>: the textbook uses 1.44 where the constant is 1/ln 2 = '
      + '1.4427, and the table prints both columns so the gap is visible rather than argued. '
      + 'Against an LSM with ' + l + ' levels a filter on each turns a read amplification of '
      + Rtext(raBefore) + ' into <strong>1 + (L &minus; 1)p = ' + Rtext(raAfter)
      + '</strong>, which is exact because p is the target you chose. The derivation, the optimal '
      + 'k = (m/n) ln 2, and the fact that a filter admits no deletion are Algorithms '
      + '<span class="tt">randomised-algorithms/bloom-filters</span>; this lesson sizes and cites.';
  }

  [mantS, expS, pS, lS].forEach(function (el) { el.addEventListener('input', redraw); });
  mantS.value = PRESET.mant; expS.value = PRESET.exp;
  pS.value = PRESET.p; lS.value = PRESET.levels;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Bloom filters: bits per key",
        subtitle="9.585 bits at 1%, not the 9.57 a textbook quotes — and both are rounded",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the keys, the target rate and the levels",
        panel_intro="Bits per key is log<sub>2</sub>(1/p)/ln 2, computed in the browser at the "
        "target you choose. The exact false-positive form is evaluated beside it at a size "
        "where an exact fraction still exists.",
    )


# ---------------------------------------------------------------------------
# L7 - rum: the read/update/memory triangle
# ---------------------------------------------------------------------------

_RUM_PAGE = 4000
_RUM_KEYS = 1000000000
_RUM_FANOUT = 500


def _rum(cfg):
    fanout = int(cfg.get("fanout", 10))
    levels = int(cfg.get("levels", 5))
    ingest_mb = int(cfg.get("ingest_mb", 50))
    row_bytes = int(cfg.get("row_bytes", 128))

    markup = (
        _toolbar(
            "Three corners, and no engine at the centre",
            "Read, update and memory amplification cannot all be minimised at once",
            [
                ("cyan", "levelled LSM"),
                ("red", "tiered LSM"),
                ("purple", "B-tree"),
                ("amber", "the corner each pays in"),
            ],
        )
        + _stage(
            _svg(
                "rmTriangle",
                "0 0 520 280",
                "A triangle with read, update and memory at its corners and the three engines "
                "placed by the share each of their costs takes.",
            )
        )
        + _table("rmTable")
        + _banner("rmStatus")
    )
    controls = (
        _range("rmF", "Fanout F", 2, 20, fanout, 1)
        + _range("rmL", "Levels L", 1, 8, levels, 1)
        + _range("rmIngest", "Ingest (MB/s)", 1, 500, ingest_mb, 1)
        + _range("rmRow", "Row size (bytes)", 16, 1024, row_bytes, 16)
        + _kpis(
            [
                ("Levelled &mdash; read / update / memory", "rmLev"),
                ("Tiered &mdash; read / update / memory", "rmTier"),
                ("B-tree &mdash; read / update / memory", "rmBtree"),
                ("Disk bandwidth each needs at this ingest", "rmBw"),
            ]
        )
        + _hint(
            "rmHint",
            "The B-tree writes a whole 4 kB page to change one row and fills its pages to about "
            "two thirds, so its update and memory amplifications come out of the page geometry "
            "rather than out of a table. A billion keys at a fanout of 500 gives its read "
            "amplification, by the integer search of L2.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "f": fanout,
                "l": levels,
                "ingest": ingest_mb,
                "row": row_bytes,
                "page": _RUM_PAGE,
                "keys": _RUM_KEYS,
                "treeFanout": _RUM_FANOUT,
            }
        )
        + r"""
  var fS = document.getElementById('rmF');
  var lS = document.getElementById('rmL');
  var ingestS = document.getElementById('rmIngest');
  var rowS = document.getElementById('rmRow');
  var plot = document.getElementById('rmTriangle');
  var table = document.getElementById('rmTable');
  var status = document.getElementById('rmStatus');

  function tripleText(t) {
    return Rtext(t.read) + ' / ' + Rtext(t.write) + ' / ' + Rtext(t.space);
  }

  function redraw() {
    var f = +fS.value, l = +lS.value, mb = +ingestS.value, row = +rowS.value;
    var ingest = R(BigInt(mb) * 1000000n, 1n);
    var fill = R(2n, 3n);
    var h = btreeHeight(PRESET.keys, PRESET.treeFanout);

    document.getElementById('rmFOut').textContent = 'F = ' + f;
    document.getElementById('rmLOut').textContent = l + (l === 1 ? ' level' : ' levels');
    document.getElementById('rmIngestOut').textContent = grp(mb) + ' MB/s';
    document.getElementById('rmRowOut').textContent = grp(row) + ' B';

    var engines = [
      ['levelled LSM', 'cyan', rumLevelled(l, f)],
      ['tiered LSM', 'red', rumTiered(l, f)],
      ['B-tree', 'purple', rumBtree(h, PRESET.page, row, fill)]
    ];

    document.getElementById('rmLev').innerHTML = tripleText(engines[0][2]);
    document.getElementById('rmTier').innerHTML = tripleText(engines[1][2]);
    document.getElementById('rmBtree').innerHTML = tripleText(engines[2][2]);
    document.getElementById('rmBw').innerHTML = engines.map(function (e) {
      return byteText(compactionBw(ingest, e[2].write)) + '/s';
    }).join(' &middot; ');

    var rows = '', i;
    for (i = 0; i < engines.length; i += 1) {
      var t = engines[i][2], sh = rumShares(t);
      var worst = Rcmp(sh.read, sh.write) >= 0
        ? (Rcmp(sh.read, sh.space) >= 0 ? 'reads' : 'memory')
        : (Rcmp(sh.write, sh.space) >= 0 ? 'updates' : 'memory');
      rows += '<tr class="tone-' + engines[i][1] + '"><td>' + engines[i][0] + '</td><td>'
        + Rtext(t.read) + '</td><td>' + Rtext(t.write) + '</td><td>' + Rtext(t.space)
        + '</td><td>' + byteText(compactionBw(ingest, t.write)) + '/s</td><td>' + worst
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>engine</th><th>read amp</th><th>update amp</th>'
      + '<th>memory amp</th><th>disk write bandwidth at ' + grp(mb) + ' MB/s</th>'
      + '<th>pays most in</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: the triangle, and each engine at its centroid ---- */
    var ax = 260, ay = 40, bx = 60, by = 220, cx = 460, cy = 220;
    var s = '<polygon points="' + ax + ',' + ay + ' ' + bx + ',' + by + ' ' + cx + ',' + cy
      + '" fill="none" stroke="var(--line-strong)" stroke-width="1.5" />'
      + '<text x="' + ax + '" y="' + (ay - 10) + '" text-anchor="middle" font-size="11" '
      + 'fill="var(--amber)">READ &mdash; I/O a lookup</text>'
      + '<text x="' + (bx - 6) + '" y="' + (by + 18) + '" font-size="11" fill="var(--amber)">'
      + 'UPDATE &mdash; writes a write</text>'
      + '<text x="' + (cx + 6) + '" y="' + (cy + 18) + '" text-anchor="end" font-size="11" '
      + 'fill="var(--amber)">MEMORY &mdash; space a byte</text>';
    var j;
    for (j = 0; j < engines.length; j += 1) {
      var sh2 = rumShares(engines[j][2]);
      var wr = Rflt(sh2.read), ww = Rflt(sh2.write), ws = Rflt(sh2.space);
      var px = ax * wr + bx * ww + cx * ws;
      var py = ay * wr + by * ww + cy * ws;
      s += '<circle cx="' + px + '" cy="' + py + '" r="7" fill="var(--' + engines[j][1]
        + ')" opacity="0.9" />'
        + '<text x="' + (px + 11) + '" y="' + (py + 4) + '" font-size="10" fill="var(--'
        + engines[j][1] + ')" font-weight="700">' + engines[j][0] + '</text>';
    }
    s += '<text x="20" y="252" font-size="10" fill="var(--muted)">'
      + 'each engine sits at the weighted centre of its own three costs, so it lands nearest '
      + 'the corner it pays most in</text>'
      + '<text x="20" y="268" font-size="10" fill="var(--muted)">'
      + 'shares, not raw amplifications: the three are in different units and only their '
      + 'proportions can share an axis</text>';
    plot.innerHTML = s;

    var lev = engines[0][2], tier = engines[1][2], bt = engines[2][2];
    status.innerHTML = 'At F = ' + f + ' and L = ' + l + ' the three triples are <strong>'
      + tripleText(lev) + '</strong> levelled, <strong>' + tripleText(tier)
      + '</strong> tiered, and <strong>' + tripleText(bt)
      + '</strong> for a B-tree of ' + h + ' levels writing ' + grp(PRESET.page) + '-byte pages '
      + 'to change ' + grp(row) + '-byte rows at two-thirds fill. Every one of them is best at '
      + 'something: the tiered tree writes each byte only ' + Rtext(tier.write)
      + ' times and pays for it by probing ' + Rtext(tier.read)
      + ' runs on a lookup and keeping ' + Rtext(tier.space)
      + ' copies of a key; the levelled tree buys the reads back and pays '
      + Rtext(lev.write) + ' writes a byte; the B-tree reads in ' + Rtext(bt.read)
      + ' and writes ' + Rtext(bt.write)
      + ' bytes to change one row. Sizing a disk to the ingest rate is the misconception: at '
      + grp(mb) + ' MB/s in, the three engines need <strong>'
      + byteText(compactionBw(ingest, lev.write)) + '/s</strong>, <strong>'
      + byteText(compactionBw(ingest, tier.write)) + '/s</strong> and <strong>'
      + byteText(compactionBw(ingest, bt.write))
      + '/s</strong> of write bandwidth respectively, and none of those is ' + grp(mb) + ' MB/s.';
  }

  [fS, lS, ingestS, rowS].forEach(function (el) { el.addEventListener('input', redraw); });
  fS.value = PRESET.f; lS.value = PRESET.l;
  ingestS.value = PRESET.ingest; rowS.value = PRESET.row;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="The RUM trade-off, as three points on one triangle",
        subtitle="Read, update and memory amplification, computed for three engine shapes",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the fanout, the levels and the row size",
        panel_intro="Each engine's triple comes out of the same parameters, and the compaction "
        "bandwidth beside it is the ingest rate times its update amplification.",
    )


# ---------------------------------------------------------------------------
# L8 - fsync: the durability cap, and what grouping buys
# ---------------------------------------------------------------------------

_FS_BATCHES = [1, 2, 4, 8, 16, 32, 64, 96, 128, 160, 192, 256]


def _fsync(cfg):
    t_us = int(cfg.get("t_us", 10000))
    batch = int(cfg.get("batch", 64))
    lam = int(cfg.get("lam", 5000))

    markup = (
        _toolbar(
            "write() returning is not durability",
            "1/t<sub>fsync</sub> durable writes a second, or B/t<sub>fsync</sub> grouped",
            [
                ("cyan", "writes filling a batch"),
                ("red", "the fsync"),
                ("amber", "the wait grouping costs"),
                ("green", "the batch that minimises latency"),
            ],
        )
        + _stage(
            _svg(
                "fsTimeline",
                "0 0 660 220",
                "A timeline of writes arriving, filling a batch, and one fsync committing them, "
                "with the latency curve against batch size beside it.",
            )
        )
        + _table("fsTable")
        + _banner("fsStatus")
    )
    controls = (
        _range("fsT", "fsync time t (&micro;s)", 100, 20000, t_us, 100)
        + _range("fsB", "Writes grouped per fsync (B)", 1, 256, batch, 1)
        + _range("fsLam", "Writes arriving a second (&lambda;)", 50, 20000, lam, 50)
        + _kpis(
            [
                ("Durable writes/s, one per fsync", "fsCap"),
                ("Durable writes/s, grouped", "fsGrouped"),
                ("fsync cost per write t/B", "fsPer"),
                ("Wait to fill the batch", "fsWait"),
                ("Commit latency, all in", "fsTotal"),
                ("B that minimises it", "fsBest"),
            ]
        )
        + _hint(
            "fsHint",
            "The queue here is the M/M/1 of Queues and Utilisation, reused rather than a second model: batches arrive at "
            "&lambda;/B and the one thread that fsyncs serves them at 1/t. At B = 1 that queue is "
            "unstable whenever &lambda; exceeds 1/t, which is the cap arriving as a queueing fact "
            "rather than as an assertion.",
        )
    )

    script = (
        _CORE_JS
        + _preset({"t": t_us, "b": batch, "lam": lam, "batches": _FS_BATCHES})
        + r"""
  var tS = document.getElementById('fsT');
  var bS = document.getElementById('fsB');
  var lamS = document.getElementById('fsLam');
  var plot = document.getElementById('fsTimeline');
  var table = document.getElementById('fsTable');
  var status = document.getElementById('fsStatus');

  function redraw() {
    var us = +tS.value, b = +bS.value, lamV = +lamS.value;
    var tf = R(BigInt(us), 1000000n), lam = R(BigInt(lamV), 1n);

    document.getElementById('fsTOut').innerHTML = secText(tf);
    document.getElementById('fsBOut').textContent = b + (b === 1 ? ' write' : ' writes');
    document.getElementById('fsLamOut').textContent = grp(lamV) + '/s';

    var cap = durableCap(tf);
    var grouped = groupedCap(tf, b);
    var per = perWriteCost(tf, b);
    var wait = fillWait(b, lam);
    var lat = commitLatency(tf, b, lam);
    var best = bestBatch(tf, lam, 256);
    /* The scanned minimum is rarely one of the round batch sizes, so it joins
       the list: a table whose "lowest" marker sits on no row would be claiming
       a minimum it does not show. */
    var sizes = PRESET.batches.slice();
    if (best !== null && sizes.indexOf(best.batch) < 0) {
      sizes.push(best.batch);
      sizes.sort(function (x, y) { return x - y; });
    }

    document.getElementById('fsCap').innerHTML = Rfix(cap, 1) + ' a second';
    document.getElementById('fsGrouped').innerHTML = Rfix(grouped, 1) + ' a second';
    document.getElementById('fsPer').innerHTML = secText(per);
    document.getElementById('fsWait').innerHTML = secText(wait);
    document.getElementById('fsTotal').innerHTML = lat.stable
      ? secText(lat.total)
      : '<span class="tone-red">unbounded &mdash; &rho; = ' + Rfix(lat.rho, 3) + '</span>';
    document.getElementById('fsBest').innerHTML = best === null
      ? '<span class="tone-red">no batch in range keeps up</span>'
      : '<span class="tone-green">B = ' + best.batch + '</span> at ' + secText(best.total);

    /* One row per batch size. The best B is not asserted: it is the smallest
       total in this column, found by evaluating the curve. */
    var rows = '', i;
    for (i = 0; i < sizes.length; i += 1) {
      var bi = sizes[i];
      var li = commitLatency(tf, bi, lam);
      var here = bi === b, isBest = best !== null && bi === best.batch;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + bi + (here ? ' &larr;' : '')
        + '</td><td>' + Rfix(groupedCap(tf, bi), 1) + '/s</td><td>'
        + (li.stable ? Rfix(li.rho, 3) : '<span class="tone-red">&ge; 1</span>') + '</td><td>'
        + secText(fillWait(bi, lam)) + '</td><td>'
        + (li.stable ? secText(li.service) : '&mdash;') + '</td><td>'
        + (li.stable ? '<strong>' + secText(li.total) + '</strong>' : '<span class="tone-red">'
            + 'the backlog grows without bound</span>') + '</td><td>'
        + (isBest ? '<span class="tone-green">lowest</span>' : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>batch B</th><th>durable writes/s</th><th>&rho;</th>'
      + '<th>wait to fill</th><th>queue + fsync</th><th>commit latency</th><th></th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: one batch filling, then one fsync ---- */
    var x0 = 24, wid = 380, y = 44;
    var shown = Math.min(b, 24);
    var s = '<text x="' + x0 + '" y="20" font-size="11" fill="var(--muted)">'
      + 'one fsync commits ' + b + (b === 1 ? ' write' : ' writes') + ', so each pays '
      + secText(per) + ' of it</text>';
    var j;
    for (j = 0; j < shown; j += 1) {
      var px = x0 + j * ((wid - 80) / Math.max(shown, 1));
      s += '<rect x="' + px + '" y="' + y + '" width="'
        + Math.max(3, (wid - 80) / Math.max(shown, 1) - 2) + '" height="20" rx="2" '
        + 'fill="var(--cyan)" opacity="0.85" />';
    }
    if (b > shown) {
      s += '<text x="' + (x0 + wid - 76) + '" y="' + (y + 15) + '" font-size="10" '
        + 'fill="var(--muted)">&hellip; ' + b + '</text>';
    }
    s += '<rect x="' + (x0 + wid - 40) + '" y="' + y + '" width="40" height="20" rx="2" '
      + 'fill="var(--red)" opacity="0.9" />'
      + '<text x="' + (x0 + wid - 20) + '" y="' + (y + 15) + '" text-anchor="middle" '
      + 'font-size="9" fill="var(--on-accent)" font-weight="700">fsync</text>'
      + '<line x1="' + x0 + '" y1="' + (y + 30) + '" x2="' + (x0 + wid - 42) + '" y2="'
      + (y + 30) + '" stroke="var(--amber)" stroke-width="2" />'
      + '<text x="' + x0 + '" y="' + (y + 46) + '" font-size="10" fill="var(--amber)">'
      + 'the first write in the batch waits ' + secText(wait) + ' on average for the rest</text>'
      + '<text x="' + x0 + '" y="' + (y + 66) + '" font-size="10" fill="var(--red)">'
      + 'and then ' + secText(tf) + ' for the fsync itself</text>'
      + '<text x="' + x0 + '" y="' + (y + 92) + '" font-size="11" fill="var(--text)">'
      + 'one per fsync: <tspan fill="var(--red)" font-weight="700">' + Rfix(cap, 1)
      + ' durable writes a second</tspan></text>'
      + '<text x="' + x0 + '" y="' + (y + 110) + '" font-size="11" fill="var(--text)">'
      + 'grouped ' + b + ': <tspan fill="var(--green)" font-weight="700">' + Rfix(grouped, 1)
      + ' a second</tspan> &mdash; the same disk</text>';

    /* the latency curve against batch size */
    var cx0 = 440, cw = 200, cbot = 170, ctop = 40;
    var vals = [], maxT = 0, k;
    for (k = 0; k < sizes.length; k += 1) {
      var lk = commitLatency(tf, sizes[k], lam);
      var v = lk.stable ? Rflt(lk.total) : null;
      vals.push(v);
      if (v !== null && v > maxT) maxT = v;
    }
    var path = '', started = false;
    for (k = 0; k < vals.length; k += 1) {
      if (vals[k] === null) continue;
      var px2 = cx0 + (cw * k) / (vals.length - 1);
      var py2 = cbot - (cbot - ctop) * (vals[k] / (maxT || 1));
      path += (started ? ' L ' : 'M ') + px2 + ' ' + py2;
      started = true;
    }
    s += '<line x1="' + cx0 + '" y1="' + cbot + '" x2="' + (cx0 + cw) + '" y2="' + cbot
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + (started ? '<path d="' + path + '" fill="none" stroke="var(--purple)" stroke-width="2" />' : '')
      + '<text x="' + cx0 + '" y="' + (ctop - 12) + '" font-size="10" fill="var(--purple)">'
      + 'commit latency against B</text>'
      + '<text x="' + cx0 + '" y="' + (cbot + 14) + '" font-size="10" fill="var(--muted)">B = 1</text>'
      + '<text x="' + (cx0 + cw) + '" y="' + (cbot + 14) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">B = 256</text>';
    if (best !== null) {
      var bi2 = sizes.indexOf(best.batch);
      var bxp = cx0 + (cw * bi2) / (vals.length - 1);
      s += '<line x1="' + bxp + '" y1="' + ctop + '" x2="' + bxp + '" y2="' + cbot
        + '" stroke="var(--green)" stroke-width="2" stroke-dasharray="4 3" />'
        + '<text x="' + (bxp + 4) + '" y="' + (ctop + 12) + '" font-size="10" '
        + 'fill="var(--green)">B = ' + best.batch + '</text>';
    }
    s += '<text x="' + cx0 + '" y="' + (cbot + 32) + '" font-size="10" fill="var(--muted)">'
      + 'scanned, not solved &mdash; the closed form for</text>'
      + '<text x="' + cx0 + '" y="' + (cbot + 46) + '" font-size="10" fill="var(--muted)">'
      + 'this shape is the EOQ of Operations Research</text>';
    plot.innerHTML = s;

    status.innerHTML = 'An fsync of ' + secText(tf) + ' caps durable writes at <strong>'
      + Rfix(cap, 1) + ' a second</strong> &mdash; one commit per fsync, whatever the CPU, the '
      + 'network and the page cache can do. Grouping ' + b
      + ' commits into one fsync makes that <strong>' + Rfix(grouped, 1)
      + ' a second</strong> on the same disk, because each write now carries only '
      + Rtext(R(1n, BigInt(b))) + ' of the fsync: ' + secText(per) + ' apiece. '
      + 'It is not free. A write waits <strong>' + secText(wait)
      + '</strong> for the rest of its batch to arrive at ' + grp(lamV) + ' a second, '
      + (lat.stable
          ? 'and then ' + secText(lat.service) + ' to queue and commit &mdash; <strong>'
            + secText(lat.total) + ' all in</strong>, at &rho; = ' + Rfix(lat.rho, 3) + '.'
          : '<span class="tone-red">and the commit queue is unstable at this batch size: '
            + '&rho; = ' + Rfix(lat.rho, 3) + ', so there is no mean latency to quote and the '
            + 'backlog grows without bound.</span>')
      + (best === null
          ? ' No batch size in range keeps up with this arrival rate.'
          : ' Scanning the curve, the batch that minimises commit latency here is <strong>B = '
            + best.batch + '</strong> at ' + secText(best.total)
            + '. That minimum is found by evaluating every B, not by a formula: the closed form '
            + 'for this shape of trade-off is the EOQ, and Operations Research '
            + '<span class="tt">inventory-models/the-eoq-formula-without-calculus</span> owns it.')
      + ' The misconception this lesson names is that write() returning means the data is safe. '
      + 'It means the bytes reached the page cache; only the fsync means the disk.';
  }

  [tS, bS, lamS].forEach(function (el) { el.addEventListener('input', redraw); });
  tS.value = PRESET.t; bS.value = PRESET.b; lamS.value = PRESET.lam;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="fsync and group commit",
        subtitle="The durability cap, what grouping buys, and the wait it costs",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the fsync time, the batch and the arrival rate",
        panel_intro="The cap is 1/t and the grouped cap is B/t; the latency beside them is the "
        "wait to fill the batch plus the M/M/1 sojourn of the batch at the fsync.",
    )


# ---------------------------------------------------------------------------
# L9 - columnar: bytes scanned, and the lookup that flips it
# ---------------------------------------------------------------------------

_CL_ROW_RATIO = 2
_CL_BW = 1000000000


def _columnar(cfg):
    rows_m = int(cfg.get("rows_m", 1000))
    width = int(cfg.get("width", 200))
    cols = int(cfg.get("cols", 20))
    selected = int(cfg.get("selected", 3))
    ratio = int(cfg.get("ratio", 5))

    markup = (
        _toolbar(
            "Bytes scanned is a question about the layout",
            "rows &times; selected widths, against rows &times; the whole row &mdash; then &divide; the ratio",
            [
                ("cyan", "columns the query reads"),
                ("muted", "columns it does not"),
                ("red", "row store, all of it"),
                ("amber", "the whole-row lookup"),
            ],
        )
        + _stage(
            _svg(
                "clGrid",
                "0 0 660 240",
                "A grid of columns with the selected ones highlighted, beside bars for the "
                "bytes each layout has to read.",
            )
        )
        + _table("clTable")
        + _banner("clStatus")
    )
    controls = (
        _range("clRows", "Rows in the table (millions)", 10, 2000, rows_m, 10)
        + _range("clWidth", "Row width (bytes)", 40, 800, width, 20)
        + _range("clCols", "Columns in the row", 4, 40, cols, 1)
        + _range("clSel", "Columns the query names", 1, 40, selected, 1)
        + _range("clRatio", "Compression ratio, columnar", 1, 12, ratio, 1)
        + _kpis(
            [
                ("Row store, bytes scanned", "clRow"),
                ("Column store, bytes scanned", "clCol"),
                ("Row store, time", "clRowT"),
                ("Column store, time", "clColT"),
                ("One whole-row lookup", "clLookup"),
                ("Columns at which they tie", "clCross"),
            ]
        )
        + _hint(
            "clHint",
            "The row store compresses 2&times; and is fixed; the columnar ratio is yours to move, "
            "because a column of like values is what compresses and that is half of why the "
            "comparison goes the way it does. The scan runs at 1 GB/s in both layouts.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "rows": rows_m,
                "width": width,
                "cols": cols,
                "sel": selected,
                "ratio": ratio,
                "rowRatio": _CL_ROW_RATIO,
                "bw": _CL_BW,
            }
        )
        + r"""
  var rowsS = document.getElementById('clRows');
  var widthS = document.getElementById('clWidth');
  var colsS = document.getElementById('clCols');
  var selS = document.getElementById('clSel');
  var ratioS = document.getElementById('clRatio');
  var plot = document.getElementById('clGrid');
  var table = document.getElementById('clTable');
  var status = document.getElementById('clStatus');

  function redraw() {
    var rowsM = +rowsS.value, width = +widthS.value, cols = +colsS.value;
    var sel = Math.min(+selS.value, cols), ratio = +ratioS.value;
    var rows = rowsM * 1000000;
    var rowRatio = R(BigInt(PRESET.rowRatio), 1n), colRatio = R(BigInt(ratio), 1n);
    var bw = R(BigInt(PRESET.bw), 1n);

    document.getElementById('clRowsOut').textContent = grp(rowsM) + ' M rows';
    document.getElementById('clWidthOut').textContent = grp(width) + ' B';
    document.getElementById('clColsOut').textContent = cols + ' columns';
    document.getElementById('clSelOut').textContent = sel + ' of ' + cols;
    document.getElementById('clRatioOut').textContent = ratio + '&times;';

    var rowBytes = rowScanBytes(rows, width, rowRatio);
    var colBytes = colScanBytes(rows, width, cols, sel, colRatio);
    var rowT = scanSeconds(rowBytes, bw), colT = scanSeconds(colBytes, bw);
    var cross = colCrossover(cols, rowRatio, colRatio);
    var lookupRow = wholeRowIos(cols, 'row'), lookupCol = wholeRowIos(cols, 'column');

    document.getElementById('clRow').innerHTML = byteText(rowBytes);
    document.getElementById('clCol').innerHTML = byteText(colBytes);
    document.getElementById('clRowT').innerHTML = secText(rowT);
    document.getElementById('clColT').innerHTML = secText(colT);
    document.getElementById('clLookup').innerHTML = grp(lookupRow) + ' I/O row store vs '
      + '<span class="tone-amber">' + grp(lookupCol) + ' I/O columnar</span>';
    document.getElementById('clCross').innerHTML = Rcmp(cross, R(BigInt(cols), 1n)) > 0
      ? Rfix(cross, 2) + ' &mdash; past all ' + cols
      : Rtext(cross) + ' = ' + Rfix(cross, 2) + ' columns';

    /* One row per possible selection. The crossover is the first row the row
       store wins, and it is read off the same two formulas. */
    var trows = '', i, step = Math.max(1, Math.ceil(cols / 8));
    for (i = 1; i <= cols; i += step) {
      var cb = colScanBytes(rows, width, cols, i, colRatio);
      var here = i === sel, wins = Rcmp(cb, rowBytes) < 0;
      trows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + i + ' of ' + cols
        + (here ? ' &larr;' : '') + '</td><td>' + byteText(cb) + '</td><td>'
        + secText(scanSeconds(cb, bw)) + '</td><td>' + byteText(rowBytes) + '</td><td>'
        + secText(rowT) + '</td><td class="' + (wins ? 'tone-cyan">columnar'
            : 'tone-red">row store') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>columns named</th><th>columnar bytes</th>'
      + '<th>columnar time</th><th>row-store bytes</th><th>row-store time</th>'
      + '<th>cheaper</th></tr></thead><tbody>' + trows + '</tbody>';

    /* ---- the drawing: the row, its columns, and two scan bars ---- */
    var x0 = 24, gw = 400, colW = Math.max(4, gw / cols), y0 = 34, rowsShown = 5;
    var s = '<text x="' + x0 + '" y="20" font-size="11" fill="var(--muted)">'
      + 'one row is ' + grp(width) + ' B across ' + cols + ' columns of '
      + byteText(columnBytes(width, cols)) + ' each</text>';
    var r, c;
    for (r = 0; r < rowsShown; r += 1) {
      for (c = 0; c < cols; c += 1) {
        s += '<rect x="' + (x0 + c * colW) + '" y="' + (y0 + r * 14) + '" width="'
          + Math.max(2, colW - 1.5) + '" height="12" fill="'
          + (c < sel ? 'var(--cyan)' : 'var(--line-strong)') + '" opacity="'
          + (c < sel ? '0.9' : '0.3') + '" />';
      }
    }
    s += '<text x="' + x0 + '" y="' + (y0 + rowsShown * 14 + 14) + '" font-size="10" '
      + 'fill="var(--cyan)">the columnar scan reads only the ' + sel + ' cyan columns</text>'
      + '<text x="' + x0 + '" y="' + (y0 + rowsShown * 14 + 30) + '" font-size="10" '
      + 'fill="var(--red)">the row store reads every square, because a row is contiguous</text>';

    var by = 160, bw2 = 600;
    var maxB = Math.max(Rflt(rowBytes), Rflt(colBytes), 1);
    s += '<rect x="' + x0 + '" y="' + by + '" width="'
      + Math.max(3, bw2 * Rflt(rowBytes) / maxB) + '" height="20" rx="3" fill="var(--red)" '
      + 'opacity="0.9" />'
      + '<text x="' + (x0 + 6) + '" y="' + (by + 15) + '" font-size="10" fill="var(--on-accent)" '
      + 'font-weight="700">row store ' + byteText(rowBytes) + ' &mdash; ' + secText(rowT) + '</text>'
      + '<rect x="' + x0 + '" y="' + (by + 26) + '" width="'
      + Math.max(3, bw2 * Rflt(colBytes) / maxB) + '" height="20" rx="3" fill="var(--cyan)" '
      + 'opacity="0.9" />'
      + '<text x="' + (x0 + 6) + '" y="' + (by + 41) + '" font-size="10" fill="var(--on-accent)" '
      + 'font-weight="700">columnar ' + byteText(colBytes) + ' &mdash; ' + secText(colT) + '</text>'
      + '<text x="' + x0 + '" y="' + (by + 66) + '" font-size="11" fill="var(--amber)">'
      + 'but one whole-row lookup is ' + grp(lookupRow) + ' I/O in the row store and '
      + grp(lookupCol) + ' in the columnar one &mdash; one page per column, and that is the '
      + 'query where columnar loses</text>';
    plot.innerHTML = s;

    var faster = Rcmp(colBytes, rowBytes) < 0;
    var mult = faster ? Rdiv(rowBytes, colBytes) : Rdiv(colBytes, rowBytes);
    status.innerHTML = 'A query naming ' + sel + ' of ' + cols + ' columns over ' + grp(rowsM)
      + ' million rows reads <strong>' + byteText(colBytes) + '</strong> in a column store and '
      + '<strong>' + byteText(rowBytes) + '</strong> in a row store &mdash; '
      + secText(colT) + ' against ' + secText(rowT) + ' at 1 GB/s, a factor of '
      + Rfix(mult, 2) + ' in favour of the ' + (faster ? 'column' : 'row') + ' store. '
      + 'The row store is not reading more <em>rows</em>; it is reading whole rows, because a row '
      + 'is contiguous on disk and a column is not. '
      + (Rcmp(cross, R(BigInt(cols), 1n)) > 0
          ? 'At these two compression ratios no selection flips the scan: the tie would need '
            + Rfix(cross, 2) + ' columns and there are only ' + cols
            + '. Lower the columnar ratio and the crossover moves inside the table.'
          : 'The two tie at <strong>' + Rfix(cross, 2) + ' columns</strong> &mdash; '
            + cols + ' &times; ' + Rtext(colRatio) + ' / ' + Rtext(rowRatio)
            + ' &mdash; and past that the row store wins the scan.')
      + ' And the scan is not the only query: fetching <em>one whole row</em> costs '
      + grp(lookupRow) + ' I/O in the row store and <strong>' + grp(lookupCol)
      + ' in the columnar one</strong>, one page per column. "Columnar is always faster" is a '
      + 'claim about analytical scans wearing the clothes of a claim about storage.';
  }

  [rowsS, widthS, colsS, selS, ratioS].forEach(function (el) {
    el.addEventListener('input', redraw);
  });
  rowsS.value = PRESET.rows; widthS.value = PRESET.width; colsS.value = PRESET.cols;
  selS.value = PRESET.sel; ratioS.value = PRESET.ratio;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Row against column, in bytes scanned",
        subtitle="And the whole-row lookup where the answer reverses",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the row, the columns and the compression",
        panel_intro="Bytes scanned is rows times the width the layout forces you to read, divided "
        "by what that layout compresses to. Both numbers, and the crossover, are recomputed as "
        "you move a control.",
    )


# ---------------------------------------------------------------------------
# L10 - workingset: course 4's cache, under another name
# ---------------------------------------------------------------------------

_WS_PAGE = 8000


def _workingset(cfg):
    mem_gb = int(cfg.get("mem_gb", 64))
    data_gb = int(cfg.get("data_gb", 500))
    skew = int(cfg.get("skew", 1))
    reads = int(cfg.get("reads", 20000))

    markup = (
        _toolbar(
            "The page cache is the cache of Caching and Hit Rates",
            "h = H(C,s)/H(N,s), and the disk still sees (1 &minus; h) &times; reads",
            [
                ("cyan", "pages memory holds"),
                ("muted", "pages it does not"),
                ("amber", "uniform would give C/N"),
                ("red", "rounded figure"),
            ],
        )
        + _stage(
            _svg(
                "wsPlot",
                "0 0 520 220",
                "The page popularity curve with the resident prefix shaded, and the residual "
                "disk IOPS drawn beside it.",
            )
        )
        + _table("wsTable")
        + _banner("wsStatus")
    )
    controls = (
        _range("wsMem", "Memory for the page cache (GB)", 1, 512, mem_gb, 1)
        + _range("wsData", "Dataset on disk (GB)", 10, 5000, data_gb, 10)
        + _range("wsSkew", "Zipf exponent s", 0, 3, skew, 1)
        + _range("wsReads", "Page reads a second", 1000, 200000, reads, 1000)
        + _kpis(
            [
                ("Pages N", "wsPages"),
                ("Pages memory holds, C", "wsCached"),
                ("C/N &mdash; share of the data", "wsShare"),
                ("Hit rate h", "wsHit"),
                ("Disk IOPS (1 &minus; h) &times; reads", "wsIops"),
                ("Uniform popularity would give", "wsUniform"),
            ]
        )
        + _hint(
            "wsHint",
            "This calls zipfHit in sysdesign_core.py &mdash; the same function the Caching and Hit Rates "
            "lab calls, not a second copy, so the two courses cannot drift apart. s is the Zipf "
            "exponent and nothing else on this path is called s.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "mem": mem_gb,
                "data": data_gb,
                "skew": skew,
                "reads": reads,
                "page": _WS_PAGE,
                "limit": EXACT_LIMIT,
            }
        )
        + r"""
  var memS = document.getElementById('wsMem');
  var dataS = document.getElementById('wsData');
  var skewS = document.getElementById('wsSkew');
  var readsS = document.getElementById('wsReads');
  var plot = document.getElementById('wsPlot');
  var table = document.getElementById('wsTable');
  var status = document.getElementById('wsStatus');

  function redraw() {
    var memGb = +memS.value, dataGb = +dataS.value, s = +skewS.value, reads = +readsS.value;
    var page = R(BigInt(PRESET.page), 1n);
    var mem = R(BigInt(memGb) * 1000000000n, 1n);
    var data = R(BigInt(dataGb) * 1000000000n, 1n);

    document.getElementById('wsMemOut').textContent = grp(memGb) + ' GB';
    document.getElementById('wsDataOut').textContent = grp(dataGb) + ' GB';
    document.getElementById('wsSkewOut').textContent = 's = ' + s
      + (s === 0 ? ' (uniform)' : (s === 1 ? ' (classic Zipf)' : ''));
    document.getElementById('wsReadsOut').textContent = grp(reads) + '/s';

    var N = Number(pageCount(data, page));
    var C = Math.min(Number(pageCount(mem, page)), N);
    var share = R(BigInt(C), BigInt(N));
    var hit = wsHit(C, N, s, PRESET.limit);
    var uniform = wsHit(C, N, 0, PRESET.limit);

    document.getElementById('wsPages').innerHTML = grp(N) + ' of ' + byteText(page);
    document.getElementById('wsCached').innerHTML = grp(C) + ' pages';
    document.getElementById('wsShare').innerHTML = Rpct(share, 2);
    document.getElementById('wsHit').innerHTML = hit.rounded
      ? '<span class="tone-red">~' + (100 * hit.value).toFixed(3) + '%</span>'
      : Rtext(hit.exact) + ' = ' + Rpct(hit.exact, 3);
    document.getElementById('wsIops').innerHTML = hit.rounded
      ? '<span class="tone-red">~' + grp(Math.round(diskIopsApprox(reads, hit.value)))
        + '/s</span>'
      : grp(Rfix(diskIopsExact(reads, hit.exact), 0)) + '/s';
    document.getElementById('wsUniform').innerHTML = Rpct(uniform.exact, 2)
      + ' &mdash; ' + grp(Math.round(diskIopsApprox(reads, uniform.value))) + ' IOPS';

    /* The same two harmonics at a sweep of memory sizes. Every row is
       recomputed; the last row is the SAME formula at a size small enough for
       the exact fraction to exist, so the machinery is visible on the page. */
    var rows = '', i, fracs = [64, 32, 16, 8, 4, 2, 1];
    for (i = 0; i < fracs.length; i += 1) {
      var ci = Math.max(1, Math.floor(N / fracs[i]));
      var hi = wsHit(ci, N, s, PRESET.limit);
      var here = Math.abs(ci - C) <= Math.max(1, C * 0.02);
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>1/' + fracs[i] + ' of the data'
        + (here ? ' &larr;' : '') + '</td><td>' + byteText(Rmul(R(BigInt(ci), 1n), page))
        + '</td><td>' + grp(ci) + '</td><td>'
        + (hi.rounded ? '<span class="tone-red">~' + (100 * hi.value).toFixed(3) + '%</span>'
                      : Rpct(hi.exact, 3))
        + '</td><td>' + grp(Math.round(diskIopsApprox(reads, hi.value))) + '/s</td></tr>';
    }
    var small = wsHit(4, PRESET.limit, s, PRESET.limit);
    rows += '<tr class="tone-muted"><td>the same formula at N = ' + PRESET.limit
      + ', C = 4</td><td>&mdash;</td><td>4</td><td>'
      + (small.rounded ? '~' + (100 * small.value).toFixed(3) + '%'
                       : '<span class="tone-green">' + Rtext(small.exact) + ' = '
                         + Rpct(small.exact, 3) + ', exact</span>')
      + '</td><td>&mdash;</td></tr>';
    table.innerHTML = '<thead><tr><th>memory</th><th>bytes</th><th>pages C</th>'
      + '<th>hit rate h</th><th>disk IOPS</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: the popularity curve, cached prefix shaded ---- */
    var x0 = 34, wid = 450, top = 28, bot = 130, cols = 120;
    var sMax = 0, vals = [], j;
    for (j = 0; j < cols; j += 1) {
      /* rank on a log scale, so a million pages fit across 450 pixels */
      var rank = Math.max(1, Math.round(Math.pow(N, (j + 1) / cols)));
      var w = 1 / Math.pow(rank, s);
      vals.push([rank, w]);
      if (w > sMax) sMax = w;
    }
    var sSvg = '<line x1="' + x0 + '" y1="' + bot + '" x2="' + (x0 + wid) + '" y2="' + bot
      + '" stroke="var(--line-strong)" stroke-width="1" />';
    for (j = 0; j < cols; j += 1) {
      var hgt = Math.max(1, (bot - top) * (vals[j][1] / (sMax || 1)));
      var resident = vals[j][0] <= C;
      sSvg += '<rect x="' + (x0 + j * (wid / cols)) + '" y="' + (bot - hgt) + '" width="'
        + Math.max(1.5, wid / cols - 1) + '" height="' + hgt + '" fill="'
        + (resident ? 'var(--cyan)' : 'var(--line-strong)') + '" opacity="'
        + (resident ? '0.95' : '0.35') + '" />';
    }
    var cutX = x0 + wid * (Math.log(Math.max(C, 1)) / Math.log(Math.max(N, 2)));
    sSvg += '<line x1="' + cutX + '" y1="' + top + '" x2="' + cutX + '" y2="' + bot
      + '" stroke="var(--amber)" stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + (cutX + 4) + '" y="' + (top + 12) + '" font-size="10" fill="var(--amber)">'
      + 'memory ends here</text>'
      + '<text x="' + x0 + '" y="18" font-size="11" fill="var(--cyan)">'
      + 'page popularity by rank, p<tspan dy="2" font-size="8">i</tspan><tspan dy="-2"></tspan>'
      + ' &prop; 1/i<tspan dy="-4" font-size="8">' + s + '</tspan><tspan dy="4"></tspan>'
      + ' (rank axis is logarithmic)</text>'
      + '<text x="' + x0 + '" y="' + (bot + 15) + '" font-size="10" fill="var(--muted)">'
      + 'rank 1</text>'
      + '<text x="' + (x0 + wid) + '" y="' + (bot + 15) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">rank ' + grp(N) + '</text>';

    var iops = hit.rounded ? diskIopsApprox(reads, hit.value) : Rflt(diskIopsExact(reads, hit.exact));
    var barW = 450, hitW = barW * Math.min(1, hit.value);
    sSvg += '<text x="' + x0 + '" y="' + (bot + 40) + '" font-size="11" fill="var(--muted)">'
      + 'of ' + grp(reads) + ' page reads a second</text>'
      + '<rect x="' + x0 + '" y="' + (bot + 48) + '" width="' + Math.max(2, hitW)
      + '" height="20" rx="3" fill="var(--cyan)" opacity="0.9" />'
      + '<rect x="' + (x0 + hitW) + '" y="' + (bot + 48) + '" width="'
      + Math.max(2, barW - hitW) + '" height="20" rx="3" fill="var(--red)" opacity="0.9" />'
      + '<text x="' + (x0 + 6) + '" y="' + (bot + 63) + '" font-size="10" '
      + 'fill="var(--on-accent)" font-weight="700">'
      + (hitW > 110 ? 'memory serves ' + (100 * hit.value).toFixed(1) + '%' : '') + '</text>'
      + '<text x="' + x0 + '" y="' + (bot + 84) + '" font-size="11" fill="var(--red)" '
      + 'font-weight="700">the disk still sees ' + grp(Math.round(iops)) + ' IOPS</text>';
    plot.innerHTML = sSvg;

    var multiple = hit.value / Math.max(uniform.value, 1e-12);
    status.innerHTML = grp(memGb) + ' GB of memory over ' + grp(dataGb) + ' GB of data is '
      + grp(C) + ' of ' + grp(N) + ' pages, <strong>' + Rpct(share, 2)
      + '</strong> of the dataset. At s = ' + s + ' those pages carry '
      + (hit.rounded ? '<strong>~' + (100 * hit.value).toFixed(2) + '%</strong>'
                     : '<strong>' + Rpct(hit.exact, 3) + '</strong>')
      + ' of the reads &mdash; '
      + (s === 0
          ? 'exactly their share of the data, because s = 0 IS uniform popularity, and this row '
            + 'is the control the skewed cases are measured against. It is also the one case '
            + 'that stays exact at any size: H(n,0) = n, so the ratio is just C/N.'
          : multiple.toFixed(1) + ' times their share of the data, which is the whole reason a '
            + 'page cache is worth having. Uniform popularity would have given only '
            + Rpct(uniform.exact, 2) + '.')
      + ' What is left is the number that matters for the disk: <strong>'
      + grp(Math.round(iops)) + ' IOPS</strong>, from (1 &minus; h) &times; ' + grp(reads)
      + '. "It is on disk, so every read is a disk read" is the misconception, and it is off by '
      + (hit.value < 1 ? (1 / Math.max(1 - hit.value, 1e-9)).toFixed(1) : 'an unbounded factor')
      + '&times; here. '
      + (hit.rounded
          ? '<span class="tone-red">This hit rate is rounded.</span> Past N = ' + PRESET.limit
            + ' pages the exact harmonic is neither computable in a redraw nor readable on a '
            + 'page, so h comes from harmonicApprox, which sums in floating point. The last row '
            + 'of the table is the same formula at a size where the exact fraction still exists, '
            + 'so you can see the machinery that produced it.'
          : 'Both harmonics here are exact fractions summed term by term over BigInt.');
  }

  [memS, dataS, skewS, readsS].forEach(function (el) { el.addEventListener('input', redraw); });
  memS.value = PRESET.mem; dataS.value = PRESET.data;
  skewS.value = PRESET.skew; readsS.value = PRESET.reads;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="Working set and the page cache",
        subtitle="Memory over dataset, the skew, and the IOPS that are left",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the memory, the dataset and the skew",
        panel_intro="The hit rate is H(C,s)/H(N,s) with C and N in pages &mdash; the Caching and Hit Rates "
        "formula, called through the same shared function &mdash; and the disk IOPS are "
        "(1 &minus; h) &times; the read rate.",
    )


# ---------------------------------------------------------------------------
# L11 - recovery: RPO against RTO
# ---------------------------------------------------------------------------


def _recovery(cfg):
    interval_h = int(cfg.get("interval_h", 24))
    write_mb = int(cfg.get("write_mb", 20))
    size_gb = int(cfg.get("size_gb", 2000))
    restore_mb = int(cfg.get("restore_mb", 200))
    replay_mb = int(cfg.get("replay_mb", 50))

    markup = (
        _toolbar(
            "Bytes at risk, and hours to be back",
            "RPO = interval &times; write rate; RTO = size / restore + the replay",
            [
                ("cyan", "since the last backup"),
                ("red", "lost on a restore"),
                ("purple", "copying the data back"),
                ("amber", "replaying the log"),
            ],
        )
        + _stage(
            _svg(
                "rcTimeline",
                "0 0 660 220",
                "A timeline of backups and a failure, with the bytes at risk marked and the "
                "restore and replay drawn as the recovery window.",
            )
        )
        + _table("rcTable")
        + _banner("rcStatus")
    )
    controls = (
        _range("rcInterval", "Backup interval (hours)", 1, 48, interval_h, 1)
        + _range("rcWrite", "Write rate (MB/s)", 1, 500, write_mb, 1)
        + _range("rcSize", "Dataset size (GB)", 100, 20000, size_gb, 100)
        + _range("rcRestore", "Restore bandwidth (MB/s)", 10, 2000, restore_mb, 10)
        + _range("rcReplay", "Log replay rate (MB/s)", 5, 500, replay_mb, 5)
        + _kpis(
            [
                ("RPO &mdash; worst case bytes", "rcRpo"),
                ("RPO &mdash; expected bytes", "rcRpoExp"),
                # NOT rcRestore/rcReplay: those are the sliders above, and
                # a browser resolves a duplicated id to the FIRST in
                # document order. Sharing them made the KPI writes land on
                # a range input, where innerHTML does nothing, so these two
                # rows would never have updated for a reader.
                ("Copying the data back", "rcRestoreVal"),
                ("Replaying the log", "rcReplayVal"),
                ("RTO &mdash; hours to be back", "rcRto"),
                ("Interval that fits a 4 h RTO", "rcMax"),
            ]
        )
        + _hint(
            "rcHint",
            "Two questions, two units. RPO is bytes and is fixed by the backup schedule; RTO is "
            "hours and is fixed by bandwidth. Shortening the interval shrinks both &mdash; less "
            "to lose and less to replay &mdash; but it cannot touch the copy, which is the floor.",
        )
    )

    script = (
        _CORE_JS
        + _preset(
            {
                "interval": interval_h,
                "write": write_mb,
                "size": size_gb,
                "restore": restore_mb,
                "replay": replay_mb,
            }
        )
        + r"""
  var intervalS = document.getElementById('rcInterval');
  var writeS = document.getElementById('rcWrite');
  var sizeS = document.getElementById('rcSize');
  var restoreS = document.getElementById('rcRestore');
  var replayS = document.getElementById('rcReplay');
  var plot = document.getElementById('rcTimeline');
  var table = document.getElementById('rcTable');
  var status = document.getElementById('rcStatus');

  var TARGET_RTO = R(14400n, 1n);        /* four hours, the target the panel names */

  function redraw() {
    var hours = +intervalS.value, wmb = +writeS.value, gb = +sizeS.value;
    var rmb = +restoreS.value, pmb = +replayS.value;
    var interval = R(BigInt(hours) * 3600n, 1n);
    var write = R(BigInt(wmb) * 1000000n, 1n);
    var size = R(BigInt(gb) * 1000000000n, 1n);
    var restore = R(BigInt(rmb) * 1000000n, 1n);
    var replay = R(BigInt(pmb) * 1000000n, 1n);

    document.getElementById('rcIntervalOut').textContent = hours + (hours === 1 ? ' hour' : ' hours');
    document.getElementById('rcWriteOut').textContent = grp(wmb) + ' MB/s';
    document.getElementById('rcSizeOut').innerHTML = byteText(size);
    document.getElementById('rcRestoreOut').textContent = grp(rmb) + ' MB/s';
    document.getElementById('rcReplayOut').textContent = grp(pmb) + ' MB/s';

    var rpo = rpoBytes(interval, write);
    var rpoExp = rpoExpectedBytes(interval, write);
    var copy = restoreSeconds(size, restore);
    var rep = replaySeconds(rpo, replay);
    var rto = rtoSeconds(size, restore, rpo, replay);
    var maxInterval = intervalForRto(size, restore, write, replay, TARGET_RTO);

    document.getElementById('rcRpo').innerHTML = byteText(rpo);
    document.getElementById('rcRpoExp').innerHTML = byteText(rpoExp);
    document.getElementById('rcRestoreVal').innerHTML = secText(copy);
    document.getElementById('rcReplayVal').innerHTML = secText(rep);
    document.getElementById('rcRto').innerHTML = secText(rto);
    document.getElementById('rcMax').innerHTML = maxInterval === null
      ? '<span class="tone-red">none &mdash; the copy alone is ' + secText(copy) + '</span>'
      : secText(maxInterval);

    /* One row per candidate interval. RPO and the replay both scale with it;
       the copy does not, which is what makes the copy the floor. */
    var rows = '', marks = [1, 2, 4, 6, 12, 24, 48], i;
    for (i = 0; i < marks.length; i += 1) {
      var ivl = R(BigInt(marks[i]) * 3600n, 1n);
      var rp = rpoBytes(ivl, write);
      var rt = rtoSeconds(size, restore, rp, replay);
      var here = marks[i] === hours;
      var fits = Rcmp(rt, TARGET_RTO) <= 0;
      rows += '<tr><td' + (here ? ' class="tone-cyan"' : '') + '>' + marks[i] + ' h'
        + (here ? ' &larr;' : '') + '</td><td>' + byteText(rp) + '</td><td>'
        + byteText(Rdiv(rp, R(2n, 1n))) + '</td><td>' + secText(copy) + '</td><td>'
        + secText(replaySeconds(rp, replay)) + '</td><td><strong>' + secText(rt)
        + '</strong></td><td class="' + (fits ? 'tone-green">inside 4 h'
            : 'tone-red">over 4 h') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>backup interval</th><th>RPO worst case</th>'
      + '<th>RPO expected</th><th>copy back</th><th>replay</th><th>RTO</th>'
      + '<th>against a 4 h target</th></tr></thead><tbody>' + rows + '</tbody>';

    /* ---- the drawing: the schedule, then the recovery window ---- */
    var x0 = 30, wid = 600, y = 54;
    var s = '<text x="' + x0 + '" y="20" font-size="11" fill="var(--muted)">'
      + 'backups every ' + hours + (hours === 1 ? ' hour' : ' hours') + ', writing '
      + grp(wmb) + ' MB/s between them</text>'
      + '<line x1="' + x0 + '" y1="' + y + '" x2="' + (x0 + wid) + '" y2="' + y
      + '" stroke="var(--line-strong)" stroke-width="1.5" />';
    var marks2 = 4, k;
    for (k = 0; k <= marks2; k += 1) {
      var mx = x0 + (wid - 120) * k / marks2;
      s += '<line x1="' + mx + '" y1="' + (y - 10) + '" x2="' + mx + '" y2="' + (y + 10)
        + '" stroke="var(--cyan)" stroke-width="2" />'
        + '<text x="' + mx + '" y="' + (y - 14) + '" text-anchor="middle" font-size="9" '
        + 'fill="var(--cyan)">backup</text>';
    }
    var failX = x0 + wid - 70;
    s += '<rect x="' + (x0 + (wid - 120)) + '" y="' + (y - 8) + '" width="' + (failX - x0 - wid + 120)
      + '" height="16" fill="var(--red)" opacity="0.35" />'
      + '<line x1="' + failX + '" y1="' + (y - 22) + '" x2="' + failX + '" y2="' + (y + 22)
      + '" stroke="var(--red)" stroke-width="2.5" />'
      + '<text x="' + failX + '" y="' + (y - 26) + '" text-anchor="middle" font-size="10" '
      + 'fill="var(--red)" font-weight="700">failure</text>'
      + '<text x="' + (x0 + wid - 118) + '" y="' + (y + 30) + '" font-size="10" fill="var(--red)">'
      + 'everything in this gap is gone: up to ' + byteText(rpo) + '</text>';

    var ry = 120, total = Math.max(Rflt(rto), 1e-9);
    var copyW = (wid - 60) * Rflt(copy) / total, repW = (wid - 60) * Rflt(rep) / total;
    s += '<text x="' + x0 + '" y="' + (ry - 10) + '" font-size="11" fill="var(--muted)">'
      + 'and then the clock the other question asks about</text>'
      + '<rect x="' + x0 + '" y="' + ry + '" width="' + Math.max(3, copyW) + '" height="26" '
      + 'rx="3" fill="var(--purple)" opacity="0.9" />'
      + '<rect x="' + (x0 + copyW) + '" y="' + ry + '" width="' + Math.max(3, repW)
      + '" height="26" rx="3" fill="var(--amber)" opacity="0.9" />'
      + '<text x="' + (x0 + 6) + '" y="' + (ry + 18) + '" font-size="10" '
      + 'fill="var(--on-accent)" font-weight="700">'
      + (copyW > 130 ? 'copy ' + byteText(size) + ' back: ' + secText(copy) : '') + '</text>'
      + '<text x="' + (x0 + copyW + 6) + '" y="' + (ry + 18) + '" font-size="10" '
      + 'fill="var(--on-accent)" font-weight="700">'
      + (repW > 110 ? 'replay: ' + secText(rep) : '') + '</text>'
      + '<text x="' + x0 + '" y="' + (ry + 46) + '" font-size="11" fill="var(--text)" '
      + 'font-weight="700">RTO = ' + secText(copy) + ' + ' + secText(rep) + ' = '
      + secText(rto) + '</text>'
      + '<text x="' + x0 + '" y="' + (ry + 66) + '" font-size="10" fill="var(--muted)">'
      + 'the purple block does not move when you change the backup schedule &mdash; it is '
      + byteText(size) + ' at ' + grp(rmb) + ' MB/s, and it is the floor under every RTO '
      + 'promise</text>'
      + '<text x="' + x0 + '" y="' + (ry + 84) + '" font-size="10" fill="var(--amber)">'
      + (maxInterval === null
          ? 'no schedule reaches a four-hour RTO: the copy alone is ' + secText(copy)
          : 'the longest interval that still fits a four-hour RTO is ' + secText(maxInterval))
      + '</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A backup every ' + hours + (hours === 1 ? ' hour' : ' hours')
      + ' at ' + grp(wmb) + ' MB/s puts <strong>' + byteText(rpo)
      + '</strong> at risk in the worst case and <strong>' + byteText(rpoExp)
      + '</strong> on average, because a failure lands uniformly inside the interval. That is '
      + 'the RPO, and it is measured in bytes. The RTO is a different number in a different '
      + 'unit: copying ' + byteText(size) + ' back at ' + grp(rmb) + ' MB/s takes <strong>'
      + secText(copy) + '</strong>, replaying ' + byteText(rpo) + ' of log at ' + grp(pmb)
      + ' MB/s takes <strong>' + secText(rep) + '</strong>, and the two together are <strong>'
      + secText(rto) + '</strong>. Halving the backup interval halves the bytes at risk and '
      + 'halves the replay &mdash; and leaves the copy exactly where it was, which is why the '
      + 'copy is the floor under any recovery-time promise. '
      + (maxInterval === null
          ? 'At this restore bandwidth a four-hour RTO is unreachable on any schedule: the copy '
            + 'alone is ' + secText(copy) + ', so the thing to buy is bandwidth, not more '
            + 'frequent backups.'
          : 'To stay inside four hours the interval has to be at most <strong>'
            + secText(maxInterval) + '</strong>.')
      + ' "We have backups" answers neither question: it is not a number of bytes and it is not '
      + 'a number of hours.';
  }

  [intervalS, writeS, sizeS, restoreS, replayS].forEach(function (el) {
    el.addEventListener('input', redraw);
  });
  intervalS.value = PRESET.interval; writeS.value = PRESET.write; sizeS.value = PRESET.size;
  restoreS.value = PRESET.restore; replayS.value = PRESET.replay;
  redraw();
  window.redrawLab = redraw;
"""
    )
    return _lab(
        cfg,
        title="RPO and RTO are two different numbers",
        subtitle="Bytes at risk from the schedule, hours to restore from the bandwidth",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the schedule and the bandwidths",
        panel_intro="RPO is the interval times the write rate; RTO is the dataset over the "
        "restore bandwidth plus the log over the replay rate. Both are recomputed as you move a "
        "control, and the table is the same pair at seven intervals.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "io": _io,
    "btree": _btree,
    "rangeq": _rangeq,
    "indexcost": _indexcost,
    "lsm": _lsm,
    "bloom": _bloom,
    "rum": _rum,
    "fsync": _fsync,
    "columnar": _columnar,
    "workingset": _workingset,
    "recovery": _recovery,
}

MODES = tuple(sorted(_MODES))


def storage_lab(cfg):
    """Course 8's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract, not defensiveness. A kit that quietly fell back
    to a default would render a finished-looking page carrying another lesson's
    widget: the markup assertions pass, labcheck passes, and the reader is shown
    the wrong lesson's arithmetic under the right lesson's title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "storage_lab: unknown mode %r; the eleven modes of course 8 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["storage_lab", "STORAGE_JS", "MODES", "EXACT_LIMIT"]
