"""Hash tables: chaining, probing, resizing, universality, and three probabilities.

Seven modes, seven lessons, two courses. Four belong to `data-structures`, where
a hash table is a structure whose cost has to be executed to be believed, and
three to `randomised-algorithms`, where the same table is the place exact
probability is easiest to check by hand:

    chaining    Hashing with Chaining
    probing     Open Addressing and Linear Probing
    resize      Resizing and the Load Factor
    universal   Universal Hashing
    balls       Balls in Bins and the Birthday Bound
    bloom       Bloom Filters
    countmin    The Count-Min Sketch

THE ARITHMETIC IS `algo_core.HASH_JS`, concatenated as it ships. Load factors,
expected chain lengths, collision rates, the all-distinct product, the Bloom
false-positive rate and the Count-Min guarantee are exact rationals over BigInt;
probe counts, cluster lengths, keys moved and measured means are counts produced
by running the table. This module adds only what a PANEL needs: key sets, the
naive delete that the tombstone lesson exists to refute, an operation pattern,
one seeded instance per probabilistic mode, and six drawings.

TWO DECISIONS THAT ARE NOT OBVIOUS FROM THE DESIGN.

  DECIMALS COME FROM `RFIXED_JS`, NOT FROM `Rdec`. Three of the quantities here
  do not survive a double. `bloomExact(1000, 100, 7)` is a fraction whose
  denominator is 1000^700 -- 2101 digits -- so `Rnum` makes both halves Infinity
  and `Rdec` prints `NaN`. `ballsExact(n, m).allDistinct` and the resize mode's
  amortised cost have the same shape at their own extremes. Every decimal on
  these pages is `Rfixed`, which is BigInt long division and works at any size,
  and the exact fraction is printed beside it wherever it is short enough to
  read -- `Rfraction` decides that by counting digits rather than by guessing.

  THE SEEDED STREAM IS `SEEDED_JS`, AND ON THIS KIT IT IS LOAD-BEARING. Every
  draw here is consumed as `x % m` -- a bin, a slot, a bit. Under the glibc
  parameters the rest of the library uses, the modulus is 2^31 and the low bits
  are a short cycle: 1200 draws mod 4 come out 300, 300, 300, 300, and a
  collision lesson dealt from that stream would demonstrate the opposite of its
  claim. `SEEDED_JS` is MINSTD -- modulus 2^31 - 1, which is prime -- with a
  splitmix64 finaliser on the seed so consecutive seeds are not a straight line.

WHAT ROUNDS HERE, AND WHERE IT SAYS SO. Two of the path's four approximations
live on this kit and both are the MODEL rather than the arithmetic.

  `knuthProbeApprox(alpha)` on `probing`. The clustering curves assume a uniform
  hash and the idealised cluster distribution the analysis derives, and this
  library proves neither; the page measures probes and prints the curve beside
  them under the word "approximation". Above alpha = 0.98 the function returns
  nothing and the panel prints the refusal instead of a figure, because the
  curve is vertical there -- 1250.5 probes at 0.98, 5000.5 at 0.99 -- and a number
  read off it is not about any table.

  `sysdesign_core.bloomApprox` on `bloom`. It is printed BESIDE `bloomExact`,
  which is a rational: at m = 1000, n = 100, k = 7 the exact rate is 0.008214
  and the independent-hash idealisation gives 0.008194. The gap between them is
  the independence assumption, and showing both is the lesson.

And one thing that is neither exact nor an approximation of something this
library could compute: the maximum-load asymptotics `log n / log log n` and
`ln ln n` printed on `balls` come from `sysdesign_core.logApprox` and are
labelled STATED, NOT PROVED, in those words. Their proofs need Chernoff bounds,
which no Subject in this library teaches, so the panel puts the load it MEASURED
in the next column and never lets the asymptotic pass as a derivation.

WHERE THE DESIGN AND THE ENGINE DISAGREED, AND WHAT WAS DONE. Two places.

  The `bloom` sliders are small. `bloomKStar` scans k exactly, and an exact scan
  over k = 1..10 at m = 1000, n = 100 takes 55 seconds in node: `Rpow` reduces by
  gcd at every squaring and the numbers reach a hundred thousand digits. Measured,
  not feared. So the sliders are n <= 20 keys and <= 12 bits per key -- m <= 240 --
  where the whole scan is under half a second, which is also exactly the "small
  m, n, k" the lesson asks the reader to compute by hand. The 1000/100/7 instance
  is asserted in scripts/mathcheck.js instead, where one evaluation is cheap.

  `probing` offers only power-of-two table sizes. `probeSlot`'s double-hashing
  rule makes its second hash odd, which is coprime with m only when m is a power
  of two; at m = 13 the step could share a factor and the probe sequence would
  not reach every slot. Offering a table size that silently breaks one of the
  three rules is the kind of defect a lesson cannot survive.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, HASH_JS, RFIXED_JS, SEEDED_JS, SERIES_JS
from .common import Lab, cfg_literal
from .sysdesign_core import APPROX_JS, STREAM_JS

HASHKIT_JS = r"""
  /* ===================== key sets, including the ones that degenerate =======

     A hash lesson is only honest if the reader can hand it the input that
     defeats it, so three of the four key sets here are chosen to do exactly
     that and the fourth is the reader's own.

       seeded    distinct draws from the MINSTD stream, which is what "simple
                 uniform hashing" looks like when you actually run it
       stride    m, 2m, 3m, ... -- every key congruent to 0 mod m, so the
                 division rule puts all n of them in ONE chain and the
                 multiplicative rule does not. This is the lesson's own
                 counterexample, not a pathological curiosity
       runs      1000, 1001, 1002, ... -- consecutive keys, which the division
                 rule spreads perfectly and which cluster badly under linear
                 probing once they are in the table
       own       whatever the reader typed */
  function hashParseKeys(text, cap) {
    var out = [], seen = {}, ignored = [], truncated = false;
    (String(text === undefined || text === null ? '' : text).match(/-?\d+/g) || [])
      .forEach(function (token) {
        var v = parseInt(token, 10);
        if (!isFinite(v) || v < 0) { ignored.push(token); return; }
        if (seen[v]) return;
        seen[v] = true;
        if (out.length < cap) out.push(v); else truncated = true;
      });
    return { keys: out, ignored: ignored, truncated: truncated };
  }
  function hashKeySet(kind, n, m, seed) {
    var out = [], seen = {}, i;
    if (kind === 'stride') { for (i = 1; i <= n; i += 1) out.push(i * m); return out; }
    if (kind === 'runs') { for (i = 0; i < n; i += 1) out.push(1000 + i); return out; }
    var draws = algoStream(seed, 4 * n + 8);
    for (i = 0; i < draws.length && out.length < n; i += 1) {
      var k = draws[i] % 9973;
      if (!seen[k]) { seen[k] = true; out.push(k); }
    }
    var next = 1;
    while (out.length < n) { if (!seen[next]) { seen[next] = true; out.push(next); } next += 1; }
    return out;
  }
  /* A rational printed as a fraction only when a reader could read it. The
     Bloom rate's denominator runs to hundreds of digits; saying so is more
     honest than printing it, and Rfixed gives the decimal either way. */
  function Rfraction(a, maxDigits) {
    var cap = maxDigits === undefined ? 18 : maxDigits;
    var d = String(a.d), n = String(a.n < 0n ? -a.n : a.n);
    if (d.length > cap || n.length > cap) {
      return 'a fraction with a ' + d.length + '-digit denominator';
    }
    return Rtext(a);
  }

  /* ===================== the one approximation this kit prints as a curve ===

     knuthProbeApprox returns null above alpha = 0.98 rather than a number read
     off a vertical curve. The panel has to honour that, so the refusal text
     lives here -- next to the numbers it refuses -- rather than being invented
     again in each place the figure is shown. */
  function knuthRow(alpha) {
    var k = knuthProbeApprox(alpha);
    if (!k) {
      return {
        quoted: false,
        unsuccessful: 'not quoted above &alpha; = 0.98',
        successful: 'not quoted above &alpha; = 0.98',
        note: 'Above &alpha; = 0.98 the curve is effectively vertical &mdash; 1250.5 probes at '
            + '0.98, 5000.5 at 0.99 &mdash; so a figure read off it says nothing about a real '
            + 'table, and the function returns nothing rather than a number.'
      };
    }
    return {
      quoted: true,
      unsuccessful: k.unsuccessful.toFixed(2),
      successful: k.successful.toFixed(2),
      note: 'Knuth&rsquo;s clustering curves, under uniform hashing: an APPROXIMATION, and the '
          + 'model is what approximates &mdash; the probes beside them were counted.'
    };
  }

  /* ===================== the delete that empties the slot ===================

     probeRun tombstones, which is correct. This is the same routine with the
     one line the misconception changes: a delete empties its slot instead of
     marking it. Everything else is identical on purpose, so the only thing the
     two runs can disagree about is the tombstone.

     It is a separate top-level function rather than a flag on the shipped one
     because the shipped one must not be able to produce a broken table. */
  function probeNaiveRun(ops, m, rule) {
    var slots = new Array(m).fill(null), c = counter(), trace = [], n = 0;
    ops.forEach(function (o, step) {
      var i, at = -1, probes = 0, found = false;
      for (i = 0; i < m; i += 1) {
        at = probeSlot(o.key, m, rule, i);
        probes += 1; c.probes += 1;
        if (o.op === 'insert') {
          if (slots[at] === null) { slots[at] = o.key; n += 1; found = true; break; }
          if (slots[at] === o.key) { found = true; break; }
        } else {
          if (slots[at] === o.key) {
            found = true;
            if (o.op === 'delete') { slots[at] = null; n -= 1; }
            break;
          }
          if (slots[at] === null) break;         /* an emptied slot ends the search */
        }
      }
      trace.push({ at: step, op: o.op, key: o.key, slot: found ? at : null,
                   probes: probes, found: found });
    });
    return runOf({ slots: slots, dead: new Array(m).fill(false), size: n },
                 usedCounts(c), trace);
  }
  /* Fill a table, delete a third of its keys, then search for every key that is
     STILL THERE, under both delete policies. With tombstones nothing is lost;
     emptying loses whichever keys sat past a hole in their own probe chain, and
     naming them is the lesson. */
  function deleteDemo(m, rule, seed) {
    var n = Math.max(4, Math.floor(0.7 * m));
    var keys = hashKeySet('seeded', n, m, seed);
    var ops = keys.map(function (k) { return { op: 'insert', key: k }; });
    var removed = keys.filter(function (_k, i) { return i % 3 === 0; });
    removed.forEach(function (k) { ops.push({ op: 'delete', key: k }); });
    var live = keys.filter(function (k) { return removed.indexOf(k) < 0; });
    live.forEach(function (k) { ops.push({ op: 'search', key: k }); });
    function lost(run) {
      return run.trace.filter(function (r) { return r.op === 'search' && !r.found; })
                      .map(function (r) { return r.key; });
    }
    return { keys: keys, removed: removed, live: live,
             lostWithTombstones: lost(probeRun(ops, m, rule)),
             lostWhenEmptied: lost(probeNaiveRun(ops, m, rule)) };
  }

  /* ===================== probes, measured ==================================

     alpha is the control and n follows from it, because alpha is what both
     Knuth curves are functions of. The unsuccessful mean is measured by
     searching for keys the table does not hold; the successful mean by
     searching for every key it does. Both are exact rationals -- a mean of
     integers is a fraction -- and they are what the approximation is compared
     against, never the other way round. */
  function probeMeasure(m, rule, seed, alphaPct) {
    var n = Math.max(1, Math.min(m - 1, Math.floor(alphaPct * m / 100)));
    var keys = hashKeySet('seeded', n, m, seed);
    var ops = keys.map(function (k) { return { op: 'insert', key: k }; });
    var absent = [], probe = 700001;
    while (absent.length < 12) {
      if (keys.indexOf(probe) < 0) absent.push(probe);
      probe += 7;
    }
    absent.forEach(function (k) { ops.push({ op: 'search', key: k }); });
    keys.forEach(function (k) { ops.push({ op: 'search', key: k }); });
    var run = probeRun(ops, m, rule);
    var un = 0, unN = 0, su = 0, suN = 0;
    run.trace.forEach(function (r) {
      if (r.op !== 'search') return;
      if (r.found) { su += r.probes; suN += 1; } else { un += r.probes; unN += 1; }
    });
    return {
      run: run, n: run.result.size, keys: keys, alpha: run.result.alpha,
      unsuccessful: R(BigInt(un), BigInt(Math.max(1, unN))),
      successful: R(BigInt(su), BigInt(Math.max(1, suN)))
    };
  }
  function probeSweep(m, rule, seed, pcts) {
    return pcts.map(function (p) {
      var got = probeMeasure(m, rule, seed, p);
      var k = knuthProbeApprox(p / 100);
      return { pct: p, measured: Rnum(got.unsuccessful), predicted: k ? k.unsuccessful : Infinity };
    });
  }

  /* ===================== an operation pattern for the resize mode ===========

     Three patterns, and the middle one is the one the lesson is about: fill to
     just under the threshold, then alternate insert and delete across it. With
     hysteresis that costs nothing; with the two thresholds set to the same
     number it rehashes on nearly every operation. */
  function resizeOps(pattern, count, seed) {
    var ops = [], i;
    if (pattern === 'grow') {
      for (i = 0; i < count; i += 1) ops.push({ op: 'insert', key: i });
      return ops;
    }
    if (pattern === 'boundary') {
      var fill = Math.max(2, Math.floor(count / 3));
      for (i = 0; i < fill; i += 1) ops.push({ op: 'insert', key: i });
      for (i = fill; i < count; i += 1) ops.push({ op: (i - fill) % 2 ? 'delete' : 'insert', key: i });
      return ops;
    }
    var draws = algoStream(seed, count);
    for (i = 0; i < count; i += 1) ops.push({ op: draws[i] % 5 < 3 ? 'insert' : 'delete', key: i });
    return ops;
  }

  /* ===================== universality, and what it is not ===================

     universalCount enumerates every (a, b). This is the other half of the
     lesson: for ONE FIXED function h(k) = k mod m an adversary needs no search
     at all -- any two keys congruent mod m collide, with probability 1, and no
     choice of m removes them. The randomness that makes the guarantee is in the
     choice of function, and this is what it looks like when there is none. */
  function adversaryPair(m) {
    return { x: 1, y: 1 + m, rate: R(1n, 1n),
             why: 'any two keys congruent mod m, chosen after the function is fixed' };
  }

  /* ===================== one seeded throw, for the exact expectations =======

     ballsExact is exact and says nothing about any particular throw. This is a
     particular throw, from the reader's seed, so the exact expectation has a
     measurement beside it rather than only a claim. */
  function throwBalls(n, m, seed) {
    var bins = new Array(m).fill(0), draws = algoStream(seed, n), i;
    for (i = 0; i < n; i += 1) bins[draws[i] % m] += 1;
    var empty = 0, maxLoad = 0, pairs = 0;
    bins.forEach(function (b) {
      if (!b) empty += 1;
      if (b > maxLoad) maxLoad = b;
      pairs += b * (b - 1) / 2;
    });
    return { bins: bins, empty: empty, maxLoad: maxLoad, pairs: pairs };
  }
  /* THE TWO NUMBERS THIS LIBRARY STATES AND DOES NOT PROVE. log n / log log n
     is the maximum load of n balls in n bins with one choice; ln ln n is what
     two choices bring it down to. Both need Chernoff bounds, which this path's
     not_covered list excludes, so they are reference numbers and the panel says
     so in those words with a MEASURED load in the next column. Null below n = 4,
     where ln ln n is not positive and the ratio means nothing. */
  function statedMaxLoad(n) {
    if (!(n >= 4)) return null;
    var ln = logApprox(n), lnln = logApprox(ln);
    if (!(lnln > 0)) return null;
    return { oneChoice: ln / lnln, twoChoice: lnln,
             stated: 'stated, not proved anywhere in this library' };
  }

  /* ===================== one Bloom filter, actually built ===================

     k bits per key, set from k integer hashes of the key. Then 200 keys that
     were never inserted are looked up: every one whose k bits all happen to be
     set is a false positive, and every one with a clear bit is a certain
     negative. The measured count sits beside the exact rate. */
  function bloomInstance(m, n, k, seed) {
    var bits = new Array(m).fill(0), keys = hashKeySet('seeded', n, 9973, seed), j;
    function bitOf(key, i) { return hashOf(key * (2 * i + 1) + i, m, 'multiply'); }
    keys.forEach(function (key) { for (j = 0; j < k; j += 1) bits[bitOf(key, j)] = 1; });
    var set = 0;
    bits.forEach(function (b) { set += b; });
    var trials = 0, falsePositives = 0, probe = 400001, i;
    for (i = 0; i < 200; i += 1, probe += 13) {
      if (keys.indexOf(probe) >= 0) continue;
      trials += 1;
      var all = true;
      for (j = 0; j < k; j += 1) if (!bits[bitOf(probe, j)]) { all = false; break; }
      if (all) falsePositives += 1;
    }
    return { bits: bits, set: set, keys: keys, trials: trials,
             falsePositives: falsePositives,
             measured: R(BigInt(falsePositives), BigInt(Math.max(1, trials))) };
  }

  /* ===================== a stream for the sketch ============================ */
  function streamPreset(kind, seed) {
    var out = [], i;
    if (kind === 'heavy') {
      for (i = 0; i < 40; i += 1) out.push(1);
      for (i = 0; i < 24; i += 1) out.push(2 + (i % 11));
      return out;
    }
    if (kind === 'uniform') { for (i = 0; i < 60; i += 1) out.push(1 + (i % 10)); return out; }
    var draws = algoStream(seed, 64);
    for (i = 0; i < 64; i += 1) out.push(1 + (draws[i] % 12));
    return out;
  }
  function hashParseStream(text, cap) {
    var out = [], ignored = [], truncated = false;
    (String(text === undefined || text === null ? '' : text).match(/-?\d+/g) || [])
      .forEach(function (token) {
        var v = parseInt(token, 10);
        if (!isFinite(v) || v < 1) { ignored.push(token); return; }
        if (out.length < cap) out.push(v); else truncated = true;
      });
    return { stream: out, ignored: ignored, truncated: truncated };
  }

  /* ===================== the drawings ======================================

     Each is two functions: one that BUILDS the markup from the thing it draws
     and returns a string, touching nothing, and one that INSTALLS it with the
     element as its first argument. That is what lets scripts/mathcheck.js
     assert on a drawing without a document. */
  function chainSvg(chains, longest) {
    var m = chains.length, rowH = Math.max(7, Math.min(20, Math.floor(272 / Math.max(1, m))));
    var s = '', i, j;
    for (i = 0; i < m; i += 1) {
      var y = 12 + i * rowH, ch = chains[i], h = Math.max(5, rowH - 3);
      s += '<text x="0" y="' + (y + h - 2) + '" font-size="10" fill="var(--muted)">' + i + '</text>';
      s += '<rect x="22" y="' + y + '" width="26" height="' + h + '" rx="2" fill="var(--panel-3)" '
        + 'stroke="var(--line-strong)" stroke-width="1" />';
      if (!ch.length) {
        s += '<text x="54" y="' + (y + h - 2) + '" font-size="9" fill="var(--muted)">empty</text>';
        continue;
      }
      var tone = (ch.length === longest && longest > 1) ? '--amber' : '--cyan';
      for (j = 0; j < ch.length && j < 15; j += 1) {
        var x = 54 + j * 40;
        s += '<line x1="' + (x - 6) + '" y1="' + (y + h / 2) + '" x2="' + x + '" y2="' + (y + h / 2)
          + '" stroke="var(--line-strong)" stroke-width="1" />';
        s += '<rect x="' + x + '" y="' + y + '" width="34" height="' + h + '" rx="2" fill="var('
          + tone + ')" opacity="0.85" />';
        if (h >= 12) s += '<text x="' + (x + 17) + '" y="' + (y + h - 3)
          + '" text-anchor="middle" font-size="9" font-weight="800" fill="var(--on-accent)">'
          + ch[j] + '</text>';
      }
      if (ch.length > 15) s += '<text x="656" y="' + (y + h - 2) + '" text-anchor="end" '
        + 'font-size="9" fill="var(--muted)">and ' + (ch.length - 15) + ' further</text>';
    }
    return s;
  }
  function drawChains(el, chains, longest) {
    var s = chainSvg(chains, longest);
    if (el) el.innerHTML = s;
    return s;
  }
  function slotStripSvg(slots, dead, opts) {
    opts = opts || {};
    var m = slots.length, cols = Math.min(m, 32);
    var rows = Math.ceil(m / cols), cw = Math.floor(636 / cols), ch = rows > 2 ? 34 : 44;
    var s = '', i;
    for (i = 0; i < m; i += 1) {
      var r = Math.floor(i / cols), c = i % cols;
      var x = 12 + c * cw, y = 16 + r * (ch + 14);
      var fill = 'var(--panel-3)';
      if (dead[i]) fill = 'var(--red)';
      else if (slots[i] !== null) fill = 'var(--cyan)';
      s += '<rect x="' + x + '" y="' + y + '" width="' + (cw - 3) + '" height="' + ch
        + '" rx="3" fill="' + fill + '" opacity="' + (slots[i] === null && !dead[i] ? '0.5' : '0.9')
        + '" stroke="var(--line-strong)" stroke-width="1" />';
      if (cw >= 18) {
        s += '<text x="' + (x + (cw - 3) / 2) + '" y="' + (y + ch / 2 + 3) + '" text-anchor="middle" '
          + 'font-size="9" font-weight="700" fill="var('
          + (slots[i] === null && !dead[i] ? '--muted' : '--on-accent') + '">'
          + (dead[i] ? 'x' : (slots[i] === null ? '' : slots[i])) + '</text>';
      }
      s += '<text x="' + (x + (cw - 3) / 2) + '" y="' + (y + ch + 11) + '" text-anchor="middle" '
        + 'font-size="8" fill="var(--muted)">' + i + '</text>';
    }
    return s;
  }
  function drawSlots(el, slots, dead, opts) {
    var s = slotStripSvg(slots, dead, opts);
    if (el) el.innerHTML = s;
    return s;
  }
  /* Every (a, b) of the universal family as one cell, so "at most 1/m of them"
     is something the reader counts rather than something the page asserts. */
  function pairGridSvg(p, m, x, y) {
    var cw = Math.floor(600 / p), chh = Math.floor(196 / Math.max(1, p - 1));
    var s = '', a, b;
    for (a = 1; a < p; a += 1) {
      for (b = 0; b < p; b += 1) {
        var hit = (((a * x + b) % p) % m) === (((a * y + b) % p) % m);
        var px = 44 + b * cw, py = 18 + (a - 1) * chh;
        s += '<rect x="' + px + '" y="' + py + '" width="' + Math.max(2, cw - 2) + '" height="'
          + Math.max(2, chh - 2) + '" rx="2" fill="var(' + (hit ? '--red' : '--panel-3')
          + ')" opacity="' + (hit ? '0.9' : '0.55') + '" stroke="var(--line)" stroke-width="0.5" />';
      }
      if (chh >= 12) s += '<text x="38" y="' + (18 + (a - 1) * chh + chh - 3)
        + '" text-anchor="end" font-size="9" fill="var(--muted)">a=' + a + '</text>';
    }
    s += '<text x="44" y="14" font-size="10" fill="var(--muted)">b = 0</text>'
      + '<text x="' + (44 + (p - 1) * cw + cw - 2) + '" y="14" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">b = ' + (p - 1) + '</text>'
      + '<text x="44" y="230" font-size="10" fill="var(--muted)">each cell is one (a, b); '
      + 'a red cell is a pair that collides</text>';
    return s;
  }
  function drawPairGrid(el, p, m, x, y) {
    var s = pairGridSvg(p, m, x, y);
    if (el) el.innerHTML = s;
    return s;
  }
  function loadBarsSvg(bins, maxLoad) {
    var m = bins.length, bw = Math.max(1, Math.floor(630 / m)), top = Math.max(1, maxLoad);
    var s = '<line x1="14" y1="206" x2="654" y2="206" stroke="var(--line-strong)" />', i;
    for (i = 0; i < m; i += 1) {
      var h = Math.round((bins[i] / top) * 180);
      var tone = bins[i] === 0 ? '--line-strong' : (bins[i] === maxLoad ? '--amber' : '--cyan');
      s += '<rect x="' + (14 + i * bw) + '" y="' + (206 - h) + '" width="' + Math.max(1, bw - 1)
        + '" height="' + Math.max(1, h) + '" fill="var(' + tone + ')" opacity="0.85" />';
    }
    s += '<text x="14" y="222" font-size="10" fill="var(--muted)">slot 0</text>'
      + '<text x="654" y="222" text-anchor="end" font-size="10" fill="var(--muted)">slot '
      + (m - 1) + '</text>'
      + '<text x="14" y="14" font-size="10" fill="var(--muted)">tallest bin: ' + maxLoad + '</text>';
    return s;
  }
  function drawLoadBars(el, bins, maxLoad) {
    var s = loadBarsSvg(bins, maxLoad);
    if (el) el.innerHTML = s;
    return s;
  }
  function bitStripSvg(bits) {
    var m = bits.length, cols = Math.min(m, 60);
    var cw = Math.floor(636 / cols), rows = Math.ceil(m / cols);
    var rh = Math.max(6, Math.min(18, Math.floor(96 / Math.max(1, rows))));
    var s = '', i;
    for (i = 0; i < m; i += 1) {
      var r = Math.floor(i / cols), c = i % cols;
      s += '<rect x="' + (12 + c * cw) + '" y="' + (12 + r * (rh + 3)) + '" width="'
        + Math.max(2, cw - 2) + '" height="' + rh + '" rx="1.5" fill="var('
        + (bits[i] ? '--cyan' : '--panel-3') + ')" opacity="' + (bits[i] ? '0.9' : '0.55')
        + '" stroke="var(--line)" stroke-width="0.5" />';
    }
    return s;
  }
  function drawBits(el, bits) {
    var s = bitStripSvg(bits);
    if (el) el.innerHTML = s;
    return s;
  }
  function sketchGridSvg(sketch, hot) {
    var d = sketch.length, w = d ? sketch[0].length : 0;
    var cw = Math.floor(600 / Math.max(1, w)), rh = Math.min(30, Math.floor(170 / Math.max(1, d)));
    var top = 1, i, j;
    sketch.forEach(function (row) { row.forEach(function (v) { if (v > top) top = v; }); });
    var s = '', mark = hot || {};
    for (i = 0; i < d; i += 1) {
      for (j = 0; j < w; j += 1) {
        var v = sketch[i][j], x = 48 + j * cw, y = 16 + i * (rh + 6);
        var on = mark[i] === j;
        s += '<rect x="' + x + '" y="' + y + '" width="' + Math.max(3, cw - 3) + '" height="' + rh
          + '" rx="2" fill="var(' + (on ? '--amber' : '--cyan') + ')" opacity="'
          + (0.18 + 0.72 * (v / top)) + '" stroke="var(--line-strong)" stroke-width="'
          + (on ? 1.8 : 0.6) + '" />';
        if (cw >= 20 && rh >= 14) s += '<text x="' + (x + (cw - 3) / 2) + '" y="' + (y + rh / 2 + 3)
          + '" text-anchor="middle" font-size="9" font-weight="700" fill="var(--text)">' + v
          + '</text>';
      }
      s += '<text x="42" y="' + (16 + i * (rh + 6) + rh / 2 + 3) + '" text-anchor="end" '
        + 'font-size="9" fill="var(--muted)">row ' + (i + 1) + '</text>';
    }
    return s;
  }
  function drawSketch(el, sketch, hot) {
    var s = sketchGridSvg(sketch, hot);
    if (el) el.innerHTML = s;
    return s;
  }
"""


# --------------------------------------------------------------- the furniture


def _options(items, chosen):
    return "".join(
        '<option value="%s"%s>%s</option>' % (key, " selected" if key == chosen else "", label)
        for key, label in items
    )


def _select(cid, label, items, chosen):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n'
        "        </div>\n" % (cid, cid, label, cid, _options(items, chosen))
    )


def _text(cid, label, value):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" />\n'
        "        </div>\n" % (cid, cid, label, cid, value)
    )


def _range(cid, label, lo, hi, value, step=1):
    """One slider, its name and its readout.

    The readout opens as a dash: every figure on the panel is written by
    redraw() from the arithmetic, so a lab whose script died shows dashes
    rather than a plausible number that nothing computed.
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


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>\n' % (cid, text)


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _stage(cid, svg_id, label, height, width=520):
    return (
        '      <div class="lab-stage" id="%s" tabindex="0" role="region" aria-label="%s">'
        '<svg id="%s" style="min-width:%dpx" viewBox="0 0 %d %d" role="img" aria-label="%s">'
        "</svg></div>\n" % (cid, label, svg_id, width, width, height, label)
    )


def _table(cid):
    return (
        '      <div class="table-wrap" style="margin-top:12px;">'
        '<table class="tt" id="%s"></table></div>\n' % cid
    )


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own, and an unknown preset raises for the same
    reason an unknown mode does: a silent fallback ships a page that looks
    finished and is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("hash mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "hash mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "hash mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


# Every mode needs the rationals, the counter convention, BigInt long division
# for the decimals, the seeded stream and the engine. SERIES_JS and APPROX_JS
# are added only by the modes that draw a curve or print a float, because the
# ceiling on a published page is 62 KB gzipped and a page that carried the whole
# core would spend a third of it on arithmetic it never calls.
_CORE_JS = (RATIONAL_JS + COUNT_JS + RFIXED_JS + STREAM_JS + SEEDED_JS + HASH_JS + HASHKIT_JS)
_PLOT_JS = _CORE_JS + SERIES_JS
_FLOAT_JS = _CORE_JS + APPROX_JS
_PLOT_FLOAT_JS = _CORE_JS + SERIES_JS + APPROX_JS


# ============================================================= mode: chaining

CHAINING_PRESETS = [
    {"key": "eight-slots", "label": "twenty keys into eight slots, drawn at random",
     "rule": "division", "keys": "seeded", "m": 8, "n": 20, "seed": 7},
    {"key": "degenerate", "label": "every key a multiple of m, which is the worst case",
     "rule": "division", "keys": "stride", "m": 8, "n": 20, "seed": 7},
    {"key": "half-full", "label": "a table at half load",
     "rule": "division", "keys": "seeded", "m": 16, "n": 8, "seed": 3},
]

CHAINING_SCRIPT = r"""
  var stage = document.getElementById('hcChains');
  var table = document.getElementById('hcTable');
  var status = document.getElementById('hcStatus');
  var preset = document.getElementById('hcPreset');
  var ruleSel = document.getElementById('hcRule');
  var kindSel = document.getElementById('hcKeys');
  var own = document.getElementById('hcOwn');
  var CAP = 60;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('chaining: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    ruleSel.value = p.rule;
    kindSel.value = p.keys;
    document.getElementById('hcM').value = p.m;
    document.getElementById('hcN').value = p.n;
    document.getElementById('hcSeed').value = p.seed;
  }

  function redraw() {
    var m = +document.getElementById('hcM').value;
    var n = +document.getElementById('hcN').value;
    var seed = +document.getElementById('hcSeed').value;
    var kind = kindSel.value, rule = ruleSel.value;
    document.getElementById('hcOwnField').hidden = kind !== 'own';
    document.getElementById('hcNRow').hidden = kind === 'own';
    document.getElementById('hcSeedRow').hidden = kind !== 'seeded';

    var typed = hashParseKeys(own.value, CAP);
    var keys = kind === 'own' ? typed.keys : hashKeySet(kind, n, m, seed);
    document.getElementById('hcMOut').textContent = m + ' slots';
    document.getElementById('hcNOut').textContent = n + ' keys';
    document.getElementById('hcSeedOut').textContent = 'seed ' + seed;

    if (!keys.length) {
      stage.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = 'Type some non-negative whole numbers to hash.';
      return;
    }
    var run = chainRun(keys, m, rule);
    var r = run.result;
    drawChains(stage, r.chains, r.longest);

    document.getElementById('hcAlpha').textContent = Rtext(r.alpha) + ' = ' + Rfixed(r.alpha, 3);
    document.getElementById('hcExpU').textContent = Rtext(r.expectedUnsuccessful)
      + ' = ' + Rfixed(r.expectedUnsuccessful, 3);
    document.getElementById('hcExpS').textContent = Rtext(r.expectedSuccessful)
      + ' = ' + Rfixed(r.expectedSuccessful, 3);
    document.getElementById('hcMean').textContent = Rtext(r.measuredMean)
      + ' = ' + Rfixed(r.measuredMean, 3);
    document.getElementById('hcLongest').textContent = r.longest;
    document.getElementById('hcEmpty').textContent = r.empty + ' of ' + m;

    var rows = '';
    rows += '<tr><td>load factor &alpha; = n/m</td><td class="tt">' + Rtext(r.alpha)
      + '</td><td>' + Rfixed(r.alpha, 4) + '</td><td>exact</td></tr>';
    rows += '<tr><td>expected, unsuccessful search</td><td class="tt">'
      + Rtext(r.expectedUnsuccessful) + '</td><td>' + Rfixed(r.expectedUnsuccessful, 4)
      + '</td><td>exact, and it is &alpha;</td></tr>';
    rows += '<tr><td>expected, successful search</td><td class="tt">'
      + Rtext(r.expectedSuccessful) + '</td><td>' + Rfixed(r.expectedSuccessful, 4)
      + '</td><td>exact: 1 + &alpha;/2 &minus; &alpha;/2m</td></tr>';
    rows += '<tr class="tone-cyan"><td>measured mean, all ' + keys.length + ' searches</td>'
      + '<td class="tt">' + Rtext(r.measuredMean) + '</td><td>' + Rfixed(r.measuredMean, 4)
      + '</td><td>counted, by running them</td></tr>';
    rows += '<tr><td>longest chain</td><td class="tt">' + r.longest + '</td><td>' + r.longest
      + '</td><td>counted &mdash; this is the worst case, and it is what &Theta;(n) means</td></tr>';
    table.innerHTML = '<thead><tr><th>quantity</th><th>exactly</th><th>as a decimal</th>'
      + '<th>where it comes from</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = '';
    if (kind === 'own' && typed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + typed.ignored.join(' ')
        + '</span> &mdash; keys are non-negative whole numbers. ';
    }
    if (kind === 'own' && typed.truncated) msg += 'Only the first ' + CAP + ' keys are hashed. ';
    msg += 'At &alpha; = <strong>' + Rtext(r.alpha) + '</strong> an unsuccessful search examines '
      + '<strong>' + Rfixed(r.expectedUnsuccessful, 3) + '</strong> elements on average and a '
      + 'successful one <strong>' + Rfixed(r.expectedSuccessful, 3) + '</strong>, under the '
      + 'simple-uniform-hashing assumption. Running all ' + keys.length + ' searches measured '
      + '<strong>' + Rfixed(r.measuredMean, 3) + '</strong>. ';
    if (kind === 'stride' && rule === 'division') {
      msg += '<span class="tone-red">Every key here is a multiple of m</span>, so k mod m is 0 for '
        + 'all of them and the whole table is one chain of ' + r.longest + '. The expectation is '
        + 'unchanged and it is now telling you nothing: &Theta;(1 + &alpha;) is an EXPECTATION '
        + 'under an assumption about the keys, and these keys break the assumption. Switch the '
        + 'rule to the multiplicative one and the same keys spread.';
    } else if (kind === 'stride') {
      msg += 'These keys are all multiples of m, which the division rule would put in a single '
        + 'chain; the multiplicative rule spreads them because it uses every bit of the key, not '
        + 'the low ones. No hash function removes the worst case &mdash; it moves which keys '
        + 'produce it.';
    } else {
      msg += 'The longest chain is <strong>' + r.longest + '</strong>, and ' + r.empty + ' of the '
        + m + ' slots ' + (r.empty === 1 ? 'is' : 'are') + ' empty. '
        + 'The expectation is an average over slots; the longest chain is what a '
        + 'single unlucky search pays, and no hash function makes the worst case go away.';
    }
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  [ruleSel, kindSel].forEach(function (el) { el.addEventListener('change', redraw); });
  own.addEventListener('input', redraw);
  ['hcM', 'hcN', 'hcSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _chaining(cfg):
    p = CHAINING_PRESETS[_preset_index(cfg, CHAINING_PRESETS, "chaining")]
    markup = (
        _toolbar(
            "Chains, drawn and walked",
            "the load factor is exact; the mean beside it was measured",
            _swatch("tone-cyan", "a chain")
            + _swatch("tone-amber", "the longest chain")
            + _swatch("tone-muted", "an empty slot"),
        )
        + _stage("hcStage", "hcChains", "One chain per slot, with the keys that hashed to it.",
                 290, 660)
        + _table("hcTable")
        + _banner("hcStatus")
    )
    controls = (
        _select("hcPreset", "Worked example",
                [(q["key"], q["label"]) for q in CHAINING_PRESETS], p["key"])
        + _select("hcRule", "Hash rule",
                  [("division", "division: h(k) = k mod m"),
                   ("multiply", "multiplicative: floor(m &middot; frac(k &middot; A))")], p["rule"])
        + _select("hcKeys", "Key set",
                  [("seeded", "drawn from a seeded stream"),
                   ("stride", "m, 2m, 3m, &hellip; &mdash; every key a multiple of m"),
                   ("runs", "1000, 1001, 1002, &hellip; &mdash; consecutive"),
                   ("own", "the keys you type")], p["keys"])
        + _range("hcM", "table slots m", 4, 20, p["m"])
        + _range("hcN", "keys n", 1, 60, p["n"])
        + _range("hcSeed", "stream seed", 1, 40, p["seed"])
        + _text("hcOwn", "Your keys", "12 20 28 36 44 7 15")
        + _kpi([
            ("hcAlpha", "Load factor &alpha;"),
            ("hcExpU", "Expected, unsuccessful"),
            ("hcExpS", "Expected, successful"),
            ("hcMean", "Measured mean probes"),
            ("hcLongest", "Longest chain"),
            ("hcEmpty", "Empty slots"),
        ])
        + _hint(
            "hcHint",
            "Both expectations are exact fractions of the n and m you chose, not lookups: "
            "&alpha; for an unsuccessful search and 1 + &alpha;/2 &minus; &alpha;/2m for a "
            "successful one. The mean beside them is counted by running every one of the n "
            "searches and adding up the links followed.",
        )
    )
    return Lab(
        title="Chaining and the load factor",
        subtitle="Expected cost is Θ(1 + α); the worst case is Θ(n), and you can build it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the table, choose the keys, walk the chains"),
        panel_intro=cfg.get(
            "panel_intro",
            "The load factor and both expected search costs are exact fractions computed from "
            "the n and m you set. The mean beside them is measured by running all n searches. "
            "Choose the key set that is every multiple of m and the two part company.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", CHAINING_PRESETS) + CHAINING_SCRIPT,
    )


# ============================================================== mode: probing

PROBING_PRESETS = [
    {"key": "linear-seventy", "label": "linear probing, a table at seven tenths",
     "rule": "linear", "m": 32, "alpha": 70, "seed": 5},
    {"key": "clustered", "label": "linear probing, nearly full",
     "rule": "linear", "m": 32, "alpha": 90, "seed": 5},
    {"key": "double", "label": "double hashing at the same load",
     "rule": "double", "m": 32, "alpha": 70, "seed": 5},
]

PROBING_SCRIPT = r"""
  var slotsEl = document.getElementById('hpSlots');
  var curve = document.getElementById('hpCurve');
  var table = document.getElementById('hpTable');
  var status = document.getElementById('hpStatus');
  var preset = document.getElementById('hpPreset');
  var ruleSel = document.getElementById('hpRule');
  var mSel = document.getElementById('hpM');
  var SWEEP = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95];

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('probing: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    ruleSel.value = p.rule;
    mSel.value = String(p.m);
    document.getElementById('hpAlpha').value = p.alpha;
    document.getElementById('hpSeed').value = p.seed;
  }

  function redraw() {
    var m = +mSel.value, rule = ruleSel.value;
    var pct = +document.getElementById('hpAlpha').value;
    var seed = +document.getElementById('hpSeed').value;
    document.getElementById('hpAlphaOut').textContent = 'aiming at load ' + (pct / 100).toFixed(2);
    document.getElementById('hpSeedOut').textContent = 'seed ' + seed;

    var got = probeMeasure(m, rule, seed, pct);
    var r = got.run.result;
    drawSlots(slotsEl, r.slots, r.dead, {});

    var alpha = Rnum(got.alpha), knuth = knuthRow(alpha);
    var sweep = probeSweep(m, rule, seed, SWEEP);
    drawSeries(curve, [
      { label: 'probes counted', colour: 'var(--cyan)', points: true,
        values: sweep.map(function (s) { return s.measured; }) },
      { label: "Knuth's curve", colour: 'var(--amber)', dashed: true,
        values: sweep.map(function (s) { return s.predicted; }) }
    ], SWEEP.map(function (p) { return (p / 100).toFixed(2); }), { xlabel: 'load' });

    document.getElementById('hpLoad').textContent = Rtext(got.alpha) + ' = ' + Rfixed(got.alpha, 3);
    document.getElementById('hpMean').textContent = Rtext(got.unsuccessful) + ' = '
      + Rfixed(got.unsuccessful, 3);
    document.getElementById('hpSucc').textContent = Rtext(got.successful) + ' = '
      + Rfixed(got.successful, 3);
    document.getElementById('hpKnuthU').textContent = knuth.unsuccessful;
    document.getElementById('hpKnuthS').textContent = knuth.successful;
    document.getElementById('hpCluster').textContent = r.longestCluster + ' slots';

    var demo = deleteDemo(m, rule, seed);
    document.getElementById('hpLost').textContent = demo.lostWhenEmptied.length
      ? (demo.lostWhenEmptied.length + ' key' + (demo.lostWhenEmptied.length === 1 ? '' : 's'))
      : 'none on this table';

    var rows = '';
    sweep.forEach(function (s) {
      var k = knuthProbeApprox(s.pct / 100);
      rows += '<tr' + (s.pct === pct ? ' class="tone-cyan"' : '') + '><td>'
        + (s.pct / 100).toFixed(2) + '</td><td>' + s.measured.toFixed(3) + '</td><td>'
        + (k ? k.unsuccessful.toFixed(3) : 'not quoted') + '</td><td>'
        + (k ? (s.measured - k.unsuccessful).toFixed(3) : '&mdash;') + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>load</th><th>probes counted</th>'
      + '<th>Knuth, approximate</th><th>counted &minus; approximate</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var msg = 'At &alpha; = <strong>' + Rtext(got.alpha) + '</strong> the table holds ' + got.n
      + ' of ' + m + ' slots and an unsuccessful search counted <strong>'
      + Rfixed(got.unsuccessful, 3) + '</strong> probes, with the longest run of non-empty slots '
      + '<strong>' + r.longestCluster + '</strong> long. ';
    if (knuth.quoted) {
      msg += 'Knuth&rsquo;s curve predicts <strong>' + knuth.unsuccessful + '</strong>. '
        + '<span class="tone-amber">That figure is an approximation</span> and the model is what '
        + 'approximates: it assumes a uniform hash and the idealised cluster distribution the '
        + 'analysis derives, neither of which is proved here. The number beside it was counted. ';
    } else {
      msg += '<span class="tone-amber">Knuth&rsquo;s curve is not quoted at this load.</span> '
        + knuth.note + ' ';
    }
    if (knuth.quoted && knuth.unsuccessful - Rnum(got.unsuccessful) > 2) {
      msg += '<span class="tone-amber">The two numbers have parted company, and that is the model '
        + 'rather than a mistake in either.</span> A table of ' + m + ' slots can never cost more '
        + 'than ' + m + ' probes, because there are only ' + m + ' of them; the curve describes a '
        + 'table big enough for the idealised cluster distribution to hold. Only one of them was '
        + 'counted. ';
    }
    msg += 'Deleting by emptying the slot instead of marking it loses <strong>'
      + demo.lostWhenEmptied.length + '</strong> of the ' + demo.live.length
      + ' keys that are still in the table'
      + (demo.lostWhenEmptied.length
          ? ' &mdash; ' + demo.lostWhenEmptied.slice(0, 6).join(', ')
            + (demo.lostWhenEmptied.length > 6 ? ' and more' : '')
            + ' become unreachable, because the hole ends a probe chain that used to run past it. '
          : '. ')
      + 'With tombstones it loses <strong>' + demo.lostWithTombstones.length + '</strong>. '
      + 'That is what the ' + r.tombstones + ' marked slots on the strip are for, and it is why '
      + '&alpha; must stay below 1: at &alpha; = 1 there is no empty slot to end any search.';
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  [ruleSel, mSel].forEach(function (el) { el.addEventListener('change', redraw); });
  ['hpAlpha', 'hpSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _probing(cfg):
    p = PROBING_PRESETS[_preset_index(cfg, PROBING_PRESETS, "probing")]
    markup = (
        _toolbar(
            "Slots, clusters and tombstones",
            "probes counted against a curve that is an approximation and says so",
            _swatch("tone-cyan", "occupied")
            + _swatch("tone-red", "tombstone")
            + _swatch("tone-amber", "the approximate curve"),
        )
        + _stage("hpStage", "hpSlots", "The probing table, slot by slot, with tombstones marked.",
                 150, 660)
        + _stage("hpPlot", "hpCurve",
                 "Probes counted at each load against Knuth's approximate curve.", 224)
        + _table("hpTable")
        + _banner("hpStatus")
    )
    controls = (
        _select("hpPreset", "Worked example",
                [(q["key"], q["label"]) for q in PROBING_PRESETS], p["key"])
        + _select("hpRule", "Probe sequence",
                  [("linear", "linear: h(k) + i"),
                   ("quadratic", "quadratic: h(k) + i + i&sup2;"),
                   ("double", "double hashing: h(k) + i &middot; h&#8322;(k)")], p["rule"])
        + _select("hpM", "Table slots m",
                  [("8", "8"), ("16", "16"), ("32", "32"), ("64", "64")], str(p["m"]))
        + _range("hpAlpha", "load factor &alpha;, as hundredths", 10, 99, p["alpha"], 1)
        + _range("hpSeed", "stream seed", 1, 40, p["seed"])
        + _kpi([
            ("hpLoad", "Load factor &alpha;"),
            ("hpMean", "Probes counted, unsuccessful"),
            ("hpSucc", "Probes counted, successful"),
            ("hpKnuthU", "Knuth, unsuccessful (approximate)"),
            ("hpKnuthS", "Knuth, successful (approximate)"),
            ("hpCluster", "Longest cluster"),
            ("hpLost", "Lost if a delete empties the slot"),
        ])
        + _hint(
            "hpHint",
            "Only powers of two are offered as table sizes: the double-hashing rule makes its "
            "second hash odd, which is coprime with m only when m is a power of two. Knuth's two "
            "curves are floating point and are labelled &mdash; above &alpha; = 0.98 they are not "
            "quoted at all, because the curve is vertical there.",
        )
    )
    return Lab(
        title="Open addressing, clustering and the tombstone",
        subtitle="Every probe is counted; the curve beside the count is an approximation",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fill the table, then try deleting the wrong way"),
        panel_intro=cfg.get(
            "panel_intro",
            "The probe counts are measured by running the searches. The dashed curve is "
            "Knuth's `½(1 + 1/(1−α)²)`, which is an approximation of the model rather than of the "
            "arithmetic, and above `α = 0.98` the panel refuses to quote it.",
        ),
        script=_PLOT_JS + cfg_literal("PRESETS", PROBING_PRESETS) + PROBING_SCRIPT,
    )


# =============================================================== mode: resize

RESIZE_PRESETS = [
    {"key": "hysteresis", "label": "double at 1, halve at a quarter",
     "grow": "1/1", "shrink": "1/4", "pattern": "boundary", "ops": 40, "seed": 9},
    {"key": "thrash", "label": "double at a half, halve at a half",
     "grow": "1/2", "shrink": "1/2", "pattern": "boundary", "ops": 40, "seed": 9},
    {"key": "growth-only", "label": "inserts only, to see the amortised line",
     "grow": "1/1", "shrink": "1/4", "pattern": "grow", "ops": 40, "seed": 9},
]

RESIZE_SCRIPT = r"""
  var plot = document.getElementById('hrCost');
  var table = document.getElementById('hrTable');
  var status = document.getElementById('hrStatus');
  var preset = document.getElementById('hrPreset');
  var growSel = document.getElementById('hrGrow');
  var shrinkSel = document.getElementById('hrShrink');
  var patSel = document.getElementById('hrPattern');

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('resize: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    growSel.value = p.grow;
    shrinkSel.value = p.shrink;
    patSel.value = p.pattern;
    document.getElementById('hrOps').value = p.ops;
    document.getElementById('hrSeed').value = p.seed;
  }

  function redraw() {
    var count = +document.getElementById('hrOps').value;
    var seed = +document.getElementById('hrSeed').value;
    document.getElementById('hrOpsOut').textContent = count + ' operations';
    document.getElementById('hrSeedOut').textContent = 'seed ' + seed;
    document.getElementById('hrSeedRow').hidden = patSel.value !== 'mixed';

    var growAt = Rparse(growSel.value), shrinkAt = Rparse(shrinkSel.value);
    var ops = resizeOps(patSel.value, count, seed);
    var run = resizeRun(ops, growAt, shrinkAt, 4);
    var r = run.result;

    var xs = run.trace.map(function (_t, i) { return i + 1; });
    drawSeries(plot, [
      { label: 'cost so far', colour: 'var(--cyan)', points: true,
        values: run.trace.map(function (t) { return t.total; }) },
      { label: '3m', colour: 'var(--amber)', dashed: true,
        values: run.trace.map(function (_t, i) { return 3 * (i + 1); }) },
      { label: 'table size', colour: 'var(--green)',
        values: run.trace.map(function (t) { return t.m; }) }
    ], xs.length ? xs : [0], { xlabel: 'operation' });

    var rehashes = run.trace.filter(function (t) { return t.event; }).length;
    document.getElementById('hrTotal').textContent = r.total;
    document.getElementById('hrBound').textContent = r.bound;
    document.getElementById('hrAmort').textContent = Rtext(r.amortised) + ' = '
      + Rfixed(r.amortised, 3);
    document.getElementById('hrMoved').textContent = r.moved;
    document.getElementById('hrRehash').textContent = rehashes + ' of ' + ops.length;
    document.getElementById('hrThrash').textContent = r.thrashAt === null
      ? 'none' : ('from operation ' + (r.thrashAt + 1));
    document.getElementById('hrFinal').textContent = r.table + ' slots, ' + r.size + ' keys';

    var rows = '', start = Math.max(0, (r.thrashAt === null ? run.trace.length - 12 : r.thrashAt - 2));
    run.trace.slice(start, start + 12).forEach(function (t, i) {
      var at = start + i;
      var thr = r.thrashAt !== null && at >= r.thrashAt && at <= r.thrashAt + 2;
      rows += '<tr' + (thr ? ' class="tone-red"' : (t.event ? ' class="tone-amber"' : '')) + '><td>'
        + (at + 1) + '</td><td>' + t.op + '</td><td>' + t.n + '</td><td>' + t.m + '</td>'
        + '<td class="tt">' + Rtext(t.alpha) + '</td><td>'
        + (t.event ? (t.event.from + ' &rarr; ' + t.event.to) : '&mdash;') + '</td><td>'
        + t.cost + '</td><td>' + t.total + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>step</th><th>operation</th><th>n</th><th>m</th>'
      + '<th>&alpha;</th><th>rehash</th><th>cost</th><th>cost so far</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var msg = ops.length + ' operations cost <strong>' + r.total + '</strong> in all, against the '
      + '<strong>' + r.bound + '</strong> the potential argument allows, which is '
      + (r.total <= r.bound ? 'inside it' : '<span class="tone-red">outside it</span>')
      + '. That is <strong>' + Rfixed(r.amortised, 3) + '</strong> per operation amortised, with '
      + r.moved + ' keys moved across ' + rehashes + ' rehash'
      + (rehashes === 1 ? '' : 'es') + '. ';
    if (r.thrashAt === null) {
      msg += 'Growing at <strong>' + Rtext(growAt) + '</strong> and shrinking at <strong>'
        + Rtext(shrinkAt) + '</strong> leaves a gap between the two thresholds, so an operation '
        + 'sequence that crosses one of them cannot immediately cross the other. '
        + '<span class="tone-cyan">The hysteresis is the whole mechanism.</span> Set both '
        + 'thresholds to a half and run the alternating pattern to watch it fail.';
    } else {
      msg += '<span class="tone-red">It thrashes from operation ' + (r.thrashAt + 1)
        + '</span>: three consecutive operations each rehash the whole table. Growing at '
        + Rtext(growAt) + ' and shrinking at ' + Rtext(shrinkAt)
        + ' leaves no room between the thresholds, so one insert takes the table over the grow '
        + 'line and the delete after it takes the doubled table under the shrink line. '
        + 'Shrinking at a quarter rather than at a half is what stops it, and it costs nothing '
        + 'but a little memory.';
    }
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  [growSel, shrinkSel, patSel].forEach(function (el) { el.addEventListener('change', redraw); });
  ['hrOps', 'hrSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _resize(cfg):
    p = RESIZE_PRESETS[_preset_index(cfg, RESIZE_PRESETS, "resize")]
    markup = (
        _toolbar(
            "Growing, shrinking and the gap between",
            "keys moved, counted; the amortised cost, exact",
            _swatch("tone-cyan", "cost so far")
            + _swatch("tone-amber", "the 3m line")
            + _swatch("tone-green", "table size")
            + _swatch("tone-red", "thrashing"),
        )
        + _stage("hrStage", "hrCost", "Cumulative rehash cost against the 3m line.", 224)
        + _table("hrTable")
        + _banner("hrStatus")
    )
    controls = (
        _select("hrPreset", "Worked example",
                [(q["key"], q["label"]) for q in RESIZE_PRESETS], p["key"])
        + _select("hrGrow", "Double when &alpha; reaches",
                  [("1/1", "1"), ("3/4", "3/4"), ("1/2", "1/2")], p["grow"])
        + _select("hrShrink", "Halve when &alpha; drops to",
                  [("1/4", "1/4"), ("3/8", "3/8"), ("1/2", "1/2")], p["shrink"])
        + _select("hrPattern", "Operation pattern",
                  [("grow", "inserts only"),
                   ("boundary", "fill, then alternate across the threshold"),
                   ("mixed", "a seeded mix, three inserts to two deletes")], p["pattern"])
        + _range("hrOps", "operations", 8, 80, p["ops"])
        + _range("hrSeed", "stream seed", 1, 40, p["seed"])
        + _kpi([
            ("hrTotal", "Total cost"),
            ("hrBound", "The 3m the argument allows"),
            ("hrAmort", "Amortised per operation"),
            ("hrMoved", "Keys moved"),
            ("hrRehash", "Rehashes"),
            ("hrThrash", "Thrashing point"),
            ("hrFinal", "Table at the end"),
        ])
        + _hint(
            "hrHint",
            "Thresholds are exact fractions, so 3/4 is 3/4 and not 0.75. The cost of an operation "
            "is 1 plus the keys it moved, and the amortised figure is that total over the number "
            "of operations &mdash; a fraction, printed exactly.",
        )
    )
    return Lab(
        title="Resizing, and why the two thresholds differ",
        subtitle="Double at one load, halve at a lower one, or every operation rehashes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set both thresholds, then try to make it thrash"),
        panel_intro=cfg.get(
            "panel_intro",
            "Cost is counted operation by operation: one for the write, plus one for every key a "
            "rehash moved. Set the grow and shrink thresholds to the same number, run the "
            "alternating pattern, and the amortised bound stops holding in front of you.",
        ),
        script=_PLOT_JS + cfg_literal("PRESETS", RESIZE_PRESETS) + RESIZE_SCRIPT,
    )


# ============================================================ mode: universal

UNIVERSAL_PRESETS = [
    {"key": "p11-m4", "label": "p = 11, m = 4, the pair 3 and 7",
     "p": 11, "m": 4, "x": 3, "y": 7},
    {"key": "p7-m3", "label": "p = 7, m = 3, the pair 1 and 4",
     "p": 7, "m": 3, "x": 1, "y": 4},
    {"key": "p13-m5", "label": "p = 13, m = 5, the pair 2 and 9",
     "p": 13, "m": 5, "x": 2, "y": 9},
]

UNIVERSAL_SCRIPT = r"""
  var grid = document.getElementById('huGrid');
  var table = document.getElementById('huTable');
  var status = document.getElementById('huStatus');
  var preset = document.getElementById('huPreset');
  var pSel = document.getElementById('huP');

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('universal: no preset named ' + preset.value);
  }
  function applyPreset() {
    var q = presetOf();
    pSel.value = String(q.p);
    document.getElementById('huM').value = q.m;
    document.getElementById('huX').value = q.x;
    document.getElementById('huY').value = q.y;
  }

  function redraw() {
    var p = +pSel.value;
    var m = +document.getElementById('huM').value;
    var x = Math.min(p - 1, +document.getElementById('huX').value);
    var y = Math.min(p - 1, +document.getElementById('huY').value);
    if (x === y) y = (y + 1) % p;
    document.getElementById('huMOut').textContent = m + ' slots';
    document.getElementById('huXOut').textContent = 'x = ' + x;
    document.getElementById('huYOut').textContent = 'y = ' + y;

    var got = universalCount(p, m, x, y);
    drawPairGrid(grid, p, m, x, y);

    document.getElementById('huTotal').textContent = got.total + ' pairs (a, b)';
    document.getElementById('huColl').textContent = got.collisions;
    document.getElementById('huRate').textContent = Rtext(got.rate) + ' = ' + Rfixed(got.rate, 4);
    document.getElementById('huBound').textContent = Rtext(got.bound) + ' = '
      + Rfixed(got.bound, 4);
    document.getElementById('huVerdict').textContent = got.withinBound
      ? 'at most 1/m, as claimed' : 'ABOVE 1/m';

    var adv = adversaryPair(m);
    document.getElementById('huFixed').textContent = Rtext(adv.rate) + ' — certain';

    var rows = '', shown = 0, a, b;
    for (a = 1; a < p && shown < 10; a += 1) {
      for (b = 0; b < p && shown < 10; b += 1) {
        var hx = ((a * x + b) % p) % m, hy = ((a * y + b) % p) % m;
        rows += '<tr' + (hx === hy ? ' class="tone-red"' : '') + '><td>' + a + '</td><td>' + b
          + '</td><td>' + (((a * x + b) % p)) + '</td><td>' + hx + '</td><td>'
          + (((a * y + b) % p)) + '</td><td>' + hy + '</td><td>'
          + (hx === hy ? 'collides' : 'separate') + '</td></tr>';
        shown += 1;
      }
    }
    table.innerHTML = '<thead><tr><th>a</th><th>b</th><th>ax+b mod p</th><th>h(x)</th>'
      + '<th>ay+b mod p</th><th>h(y)</th><th></th></tr></thead><tbody>' + rows
      + '</tbody><tfoot><tr><td colspan="7">the first ten of ' + got.total
      + ' pairs; the grid above is all of them</td></tr></tfoot>';

    status.innerHTML = 'Over every one of the <strong>' + got.total
      + '</strong> functions in the family &mdash; a from 1 to ' + (p - 1) + ', b from 0 to '
      + (p - 1) + ' &mdash; the fixed pair ' + x + ' and ' + y + ' collides <strong>'
      + got.collisions + '</strong> time' + (got.collisions === 1 ? '' : 's')
      + ', a rate of <strong>' + Rtext(got.rate)
      + '</strong> against the bound 1/m = <strong>' + Rtext(got.bound) + '</strong>. '
      + (got.withinBound ? 'Inside it, and it is inside it for every pair you can choose. '
                         : '<span class="tone-red">Outside it.</span> ')
      + '<span class="tone-cyan">The randomness is in the choice of function, not in the '
      + 'keys.</span> Fix one function instead &mdash; h(k) = k mod m, say &mdash; and an '
      + 'adversary who is allowed to see it picks ' + adv.x + ' and ' + adv.y
      + ', which collide with probability <strong>1</strong>: ' + adv.why
      + '. That is the difference the family buys, and it is a guarantee about every input '
      + 'rather than an assumption about the input you happened to get.';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  pSel.addEventListener('change', redraw);
  ['huM', 'huX', 'huY'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _universal(cfg):
    q = UNIVERSAL_PRESETS[_preset_index(cfg, UNIVERSAL_PRESETS, "universal")]
    markup = (
        _toolbar(
            "Every function in the family, counted",
            "the collision rate is a fraction over every (a, b), not a sample",
            _swatch("tone-red", "this (a, b) collides") + _swatch("tone-muted", "it separates"),
        )
        + _stage("huStage", "huGrid",
                 "One cell per (a, b) in the universal family, red where the chosen pair collides.",
                 240, 660)
        + _table("huTable")
        + _banner("huStatus")
    )
    controls = (
        _select("huPreset", "Worked example",
                [(r["key"], r["label"]) for r in UNIVERSAL_PRESETS], q["key"])
        + _select("huP", "Prime p", [("5", "5"), ("7", "7"), ("11", "11"), ("13", "13")], str(q["p"]))
        + _range("huM", "table slots m", 2, 6, q["m"])
        + _range("huX", "first key x", 0, 12, q["x"])
        + _range("huY", "second key y", 0, 12, q["y"])
        + _kpi([
            ("huTotal", "Functions in the family"),
            ("huColl", "Of them, colliding"),
            ("huRate", "Collision rate, exactly"),
            ("huBound", "The bound 1/m"),
            ("huVerdict", "Verdict"),
            ("huFixed", "One fixed function, adversarial keys"),
        ])
        + _hint(
            "huHint",
            "Nothing here is sampled. Every (a, b) with a in 1&hellip;p&minus;1 and b in "
            "0&hellip;p&minus;1 is enumerated and the colliding ones counted, so the rate is an "
            "exact fraction and the claim `Pr[h(x) = h(y)] &le; 1/m` is something you can check "
            "by counting cells.",
        )
    )
    return Lab(
        title="Universal hashing, counted over the whole family",
        subtitle="The randomness is in the function, and the keys may be chosen against you",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a pair of keys and count every function"),
        panel_intro=cfg.get(
            "panel_intro",
            "The family is `h(k) = ((ak + b) mod p) mod m`. Choose any two distinct keys and the "
            "grid enumerates every `(a, b)`, colouring the ones that collide. The fraction that "
            "results is exact, and it never exceeds `1/m` — which is what universality means.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", UNIVERSAL_PRESETS) + UNIVERSAL_SCRIPT,
    )


# ================================================================ mode: balls

BALLS_PRESETS = [
    {"key": "birthday", "label": "twenty-three keys into three hundred and sixty-five slots",
     "n": 23, "m": 365, "seed": 4},
    {"key": "quarter-full", "label": "a table a quarter full",
     "n": 32, "m": 128, "seed": 4},
    {"key": "equal", "label": "as many keys as slots",
     "n": 64, "m": 64, "seed": 4},
]

BALLS_SCRIPT = r"""
  var bars = document.getElementById('hbBars');
  var table = document.getElementById('hbTable');
  var status = document.getElementById('hbStatus');
  var preset = document.getElementById('hbPreset');

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('balls: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    document.getElementById('hbN').value = p.n;
    document.getElementById('hbM').value = p.m;
    document.getElementById('hbSeed').value = p.seed;
  }

  function redraw() {
    var n = +document.getElementById('hbN').value;
    var m = +document.getElementById('hbM').value;
    var seed = +document.getElementById('hbSeed').value;
    document.getElementById('hbNOut').textContent = n + ' keys';
    document.getElementById('hbMOut').textContent = m + ' slots';
    document.getElementById('hbSeedOut').textContent = 'seed ' + seed;

    var ex = ballsExact(n, m);
    var thrown = throwBalls(n, m, seed);
    drawLoadBars(bars, thrown.bins, thrown.maxLoad);

    var even = birthdayExact(m);
    document.getElementById('hbPairs').textContent = Rtext(ex.expectedPairs) + ' = '
      + Rfixed(ex.expectedPairs, 3);
    document.getElementById('hbPairsM').textContent = thrown.pairs;
    document.getElementById('hbEmpty').textContent = Rfixed(ex.expectedEmpty, 3);
    document.getElementById('hbEmptyM').textContent = thrown.empty + ' of ' + m;
    document.getElementById('hbBirthday').textContent = even.n === null
      ? 'past 4m' : (even.n + ' keys');
    document.getElementById('hbMaxLoad').textContent = thrown.maxLoad;

    var equal = throwBalls(m, m, seed);
    var stated = statedMaxLoad(m);
    document.getElementById('hbStated1').textContent = stated
      ? stated.oneChoice.toFixed(2) + ' — stated' : 'not quoted below four slots';
    document.getElementById('hbStated2').textContent = stated
      ? stated.twoChoice.toFixed(2) + ' — stated' : 'not quoted below four slots';
    document.getElementById('hbEqual').textContent = equal.maxLoad + ' — counted';

    var rows = '';
    rows += '<tr><td>expected colliding pairs, n(n&minus;1)/2m</td><td class="tt">'
      + Rtext(ex.expectedPairs) + '</td><td>' + Rfixed(ex.expectedPairs, 4)
      + '</td><td>exact, by linearity over pairs</td></tr>';
    rows += '<tr class="tone-cyan"><td>colliding pairs in this throw</td><td class="tt">'
      + thrown.pairs + '</td><td>' + thrown.pairs + '</td><td>counted</td></tr>';
    rows += '<tr><td>expected empty slots, m(1 &minus; 1/m)&#8319;</td><td class="tt">'
      + Rfraction(ex.expectedEmpty, 14) + '</td><td>' + Rfixed(ex.expectedEmpty, 4)
      + '</td><td>exact, by linearity over slots</td></tr>';
    rows += '<tr class="tone-cyan"><td>empty slots in this throw</td><td class="tt">'
      + thrown.empty + '</td><td>' + thrown.empty + '</td><td>counted</td></tr>';
    rows += '<tr><td>probability all ' + n + ' land apart</td><td class="tt">'
      + Rfraction(ex.allDistinct, 14) + '</td><td>' + Rfixed(ex.allDistinct, 6)
      + '</td><td>exact product, not the &radic;(2m ln 2) estimate</td></tr>';
    rows += '<tr class="tone-amber"><td>maximum load with one choice, at n = m</td>'
      + '<td class="tt">log n / log log n</td><td>'
      + (stated ? stated.oneChoice.toFixed(3) : '&mdash;')
      + '</td><td>STATED, NOT PROVED in this library</td></tr>';
    rows += '<tr class="tone-amber"><td>maximum load with two choices, at n = m</td>'
      + '<td class="tt">ln ln n</td><td>' + (stated ? stated.twoChoice.toFixed(3) : '&mdash;')
      + '</td><td>STATED, NOT PROVED in this library</td></tr>';
    rows += '<tr class="tone-cyan"><td>maximum load measured at n = m</td><td class="tt">'
      + equal.maxLoad + '</td><td>' + equal.maxLoad + '</td><td>counted, on this seed</td></tr>';
    table.innerHTML = '<thead><tr><th>quantity</th><th>exactly</th><th>as a decimal</th>'
      + '<th>where it comes from</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = 'With ' + n + ' keys in ' + m + ' slots the expected number of colliding PAIRS is '
      + '<strong>' + Rtext(ex.expectedPairs) + '</strong> = ' + Rfixed(ex.expectedPairs, 3)
      + ' and the expected number of empty slots is <strong>' + Rfixed(ex.expectedEmpty, 3)
      + '</strong>. Both are exact fractions and both come from linearity of expectation, over '
      + 'pairs and over slots. This seeded throw produced ' + thrown.pairs + ' colliding pair'
      + (thrown.pairs === 1 ? '' : 's') + ' and ' + thrown.empty + ' empty slot'
      + (thrown.empty === 1 ? '' : 's') + '. ';
    if (even.n !== null) {
      msg += 'A collision becomes more likely than not at <strong>' + even.n
        + '</strong> keys &mdash; found by multiplying the exact product out, not by the '
        + '&radic;(2m ln 2) rule of thumb. At that point n&sup2;/m is '
        + Rtext(R(BigInt(even.n * even.n), BigInt(m))) + ', which is where the square root of m '
        + 'puts it. <span class="tone-cyan">Collisions are not rare until '
        + 'the table is nearly full; they start at about the square root of it.</span> ';
    }
    if (stated) {
      msg += '<span class="tone-amber">The maximum load is a different question and this library '
        + 'does not answer it.</span> log n / log log n for one choice and ln ln n for two are '
        + 'STATED HERE, NOT PROVED: their proofs need Chernoff bounds, which nothing in this '
        + 'library teaches. At ' + m + ' keys in ' + m + ' slots they read '
        + stated.oneChoice.toFixed(2) + ' and ' + stated.twoChoice.toFixed(2)
        + ', and the tallest bin this seed actually produced was <strong>' + equal.maxLoad
        + '</strong>. The measured number is the one that was computed here.';
    }
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  ['hbN', 'hbM', 'hbSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _balls(cfg):
    p = BALLS_PRESETS[_preset_index(cfg, BALLS_PRESETS, "balls")]
    markup = (
        _toolbar(
            "Balls into bins, exactly",
            "two expectations as fractions, one seeded throw beside them",
            _swatch("tone-cyan", "a bin")
            + _swatch("tone-amber", "the tallest bin")
            + _swatch("tone-muted", "empty"),
        )
        + _stage("hbStage", "hbBars", "One bar per slot, showing how many keys landed in it.",
                 240, 660)
        + _table("hbTable")
        + _banner("hbStatus")
    )
    controls = (
        _select("hbPreset", "Worked example",
                [(q["key"], q["label"]) for q in BALLS_PRESETS], p["key"])
        + _range("hbN", "keys n", 2, 300, p["n"])
        + _range("hbM", "slots m", 2, 400, p["m"])
        + _range("hbSeed", "stream seed", 1, 40, p["seed"])
        + _kpi([
            ("hbPairs", "Expected colliding pairs"),
            ("hbPairsM", "Colliding pairs, counted"),
            ("hbEmpty", "Expected empty slots"),
            ("hbEmptyM", "Empty slots, counted"),
            ("hbBirthday", "Even odds of a collision at"),
            ("hbMaxLoad", "Tallest bin, counted"),
            ("hbStated1", "At n = m, one choice: log n / log log n"),
            ("hbStated2", "At n = m, two choices: ln ln n"),
            ("hbEqual", "Tallest bin at n = m, counted"),
        ])
        + _hint(
            "hbHint",
            "The two expectations and the all-apart probability are exact fractions over BigInt: "
            "the probability is the product (m/m)((m&minus;1)/m)&hellip; multiplied out, not the "
            "&radic;(2m ln 2) estimate. The two maximum-load figures are the exception and the "
            "panel says so on their own row &mdash; they are stated, not proved here.",
        )
    )
    return Lab(
        title="Balls in bins and the birthday bound",
        subtitle="Both expectations exact, the even-odds point found by multiplying it out",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Throw the keys, then check the expectations"),
        panel_intro=cfg.get(
            "panel_intro",
            "`n(n−1)/2m` expected colliding pairs and `m(1 − 1/m)ⁿ` expected empty slots, both "
            "exact fractions, with one seeded throw beside them. The two maximum-load "
            "asymptotics are labelled: this library states them and proves neither.",
        ),
        script=_FLOAT_JS + cfg_literal("PRESETS", BALLS_PRESETS) + BALLS_SCRIPT,
    )


# ================================================================ mode: bloom

BLOOM_PRESETS = [
    {"key": "ten-bits", "label": "sixteen keys at ten bits each, seven hashes",
     "n": 16, "bits": 10, "k": 7, "seed": 6},
    {"key": "eight-bits", "label": "sixteen keys at eight bits each",
     "n": 16, "bits": 8, "k": 6, "seed": 6},
    {"key": "too-many", "label": "twelve bits a key and every hash you can afford",
     "n": 12, "bits": 12, "k": 10, "seed": 6},
]

BLOOM_SCRIPT = r"""
  var bitsEl = document.getElementById('hfBits');
  var curve = document.getElementById('hfCurve');
  var table = document.getElementById('hfTable');
  var status = document.getElementById('hfStatus');
  var preset = document.getElementById('hfPreset');
  var KMAX = 10;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('bloom: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    document.getElementById('hfN').value = p.n;
    document.getElementById('hfPer').value = p.bits;
    document.getElementById('hfK').value = p.k;
    document.getElementById('hfSeed').value = p.seed;
  }

  function redraw() {
    var n = +document.getElementById('hfN').value;
    var per = +document.getElementById('hfPer').value;
    var k = +document.getElementById('hfK').value;
    var seed = +document.getElementById('hfSeed').value;
    var m = n * per;
    document.getElementById('hfNOut').textContent = n + ' keys';
    document.getElementById('hfPerOut').textContent = per + ' bits a key, so m = ' + m;
    document.getElementById('hfKOut').textContent = k + ' hash' + (k === 1 ? '' : 'es');
    document.getElementById('hfSeedOut').textContent = 'seed ' + seed;

    var exact = bloomExact(m, n, k);
    var approx = bloomApprox(m, n, k);
    var best = bloomKStar(m, n, KMAX);
    var inst = bloomInstance(m, n, k, seed);
    drawBits(bitsEl, inst.bits);

    var xs = best.rows.map(function (r) { return r.k; });
    drawSeries(curve, [
      { label: 'exact', colour: 'var(--cyan)', points: true,
        values: best.rows.map(function (r) { return Number(Rfixed(r.rate, 9)); }) },
      { label: 'idealised', colour: 'var(--amber)', dashed: true,
        values: best.rows.map(function (r) { return bloomApprox(m, n, r.k); }) }
    ], xs, { xlabel: 'k' });

    document.getElementById('hfExact').textContent = Rfixed(exact, 6);
    document.getElementById('hfApprox').textContent = approx.toFixed(6) + ' — approximate';
    document.getElementById('hfGap').textContent = (Number(Rfixed(exact, 9)) - approx).toExponential(2);
    document.getElementById('hfOneIn').textContent = RoneIn(exact);
    document.getElementById('hfKStar').textContent = best.k + ' hashes';
    document.getElementById('hfSet').textContent = inst.set + ' of ' + m + ' bits';
    document.getElementById('hfFalse').textContent = inst.falsePositives + ' of ' + inst.trials;

    var rows = '';
    best.rows.forEach(function (r) {
      var a = bloomApprox(m, n, r.k);
      rows += '<tr' + (r.k === k ? ' class="tone-cyan"' : (r.k === best.k ? ' class="tone-green"' : ''))
        + '><td>' + r.k + '</td><td>' + Rfixed(r.rate, 6) + '</td><td>' + a.toFixed(6)
        + '</td><td>' + (Number(Rfixed(r.rate, 9)) - a).toExponential(2) + '</td><td>'
        + RoneIn(r.rate) + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>k</th><th>exact rate</th>'
      + '<th>idealised, approximate</th><th>exact &minus; idealised</th><th>read as</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'At m = <strong>' + m + '</strong> bits, n = <strong>' + n
      + '</strong> keys and k = <strong>' + k + '</strong> hashes the false-positive rate is '
      + '(1 &minus; (1 &minus; 1/m)<sup>kn</sup>)<sup>k</sup> = <strong>' + Rfixed(exact, 6)
      + '</strong>, which is ' + RoneIn(exact) + '. That is a fraction over BigInt &mdash; '
      + Rfraction(exact, 12) + ' &mdash; and nothing about it is rounded except the printing. '
      + '<span class="tone-amber">Beside it, ' + approx.toFixed(6) + ' is the (1 &minus; '
      + 'e<sup>&minus;kn/m</sup>)<sup>k</sup> idealisation, and it is an approximation.</span> '
      + 'The gap between them is the independent-hash assumption: the exact form counts the bits '
      + 'a filter really sets, the idealisation pretends each of the kn bit-settings is '
      + 'independent. Scanning k exactly over 1 to ' + KMAX + ' puts the best at <strong>'
      + best.k + '</strong>, rate ' + Rfixed(best.rate, 6) + '. '
      + '<span class="tone-amber">Move the key slider and the idealised number does not '
      + 'change.</span> It depends only on kn/m, which is k divided by the bits per key, so it is '
      + 'the same figure for sixteen keys in 160 bits as for a hundred keys in a thousand. The '
      + 'exact rate is not: it is a different filter. That is the independence assumption, seen '
      + 'from the side. '
      + 'The filter built here set ' + inst.set + ' of its ' + m + ' bits and returned '
      + inst.falsePositives + ' false positive' + (inst.falsePositives === 1 ? '' : 's')
      + ' in ' + inst.trials + ' lookups of keys it never saw. <span class="tone-red">It can delete nothing.</span> Clearing a bit to remove one '
      + 'key clears it for every other key that set it, and those keys would then get a false '
      + 'NEGATIVE &mdash; which is the one answer a Bloom filter is built never to give.';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  ['hfN', 'hfPer', 'hfK', 'hfSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _bloom(cfg):
    p = BLOOM_PRESETS[_preset_index(cfg, BLOOM_PRESETS, "bloom")]
    markup = (
        _toolbar(
            "A filter, its exact rate and its idealisation",
            "the fraction is exact; the curve beside it assumes independence",
            _swatch("tone-cyan", "a set bit, and the exact rate")
            + _swatch("tone-amber", "the idealised rate")
            + _swatch("tone-green", "the best k"),
        )
        + _stage("hfStage", "hfBits", "The filter's bit array after every key has been inserted.",
                 120, 660)
        + _stage("hfPlot", "hfCurve", "The exact false-positive rate against k, with the "
                 "idealisation dashed beside it.", 224)
        + _table("hfTable")
        + _banner("hfStatus")
    )
    controls = (
        _select("hfPreset", "Worked example",
                [(q["key"], q["label"]) for q in BLOOM_PRESETS], p["key"])
        + _range("hfN", "keys n", 4, 20, p["n"])
        + _range("hfPer", "bits per key, so m = n &times; this", 4, 12, p["bits"])
        + _range("hfK", "hash functions k", 1, 10, p["k"])
        + _range("hfSeed", "stream seed", 1, 40, p["seed"])
        + _kpi([
            ("hfExact", "Exact rate"),
            ("hfApprox", "Idealised rate"),
            ("hfGap", "Exact minus idealised"),
            ("hfOneIn", "Read as"),
            ("hfKStar", "Best k, by exact scan"),
            ("hfSet", "Bits set in this filter"),
            ("hfFalse", "False positives measured"),
        ])
        + _hint(
            "hfHint",
            "The table stays small on purpose: the exact rate is a fraction whose denominator is "
            "m raised to kn, and scanning k exactly at a thousand bits takes the better part of a "
            "minute. These are the sizes the derivation is checked at by hand. The decimal comes "
            "from BigInt long division &mdash; a double turns this fraction into NaN.",
        )
    )
    return Lab(
        title="Bloom filters, exactly and idealised",
        subtitle="A clear bit is a certain no; the false-positive rate is a fraction",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Size the filter, then read both rates"),
        panel_intro=cfg.get(
            "panel_intro",
            "`(1 − (1 − 1/m)^{kn})^k` is computed exactly, as a fraction over BigInt, and the "
            "familiar `(1 − e^{−kn/m})^k` is printed beside it as the approximation it is. The "
            "gap between the two columns is the independent-hash assumption.",
        ),
        script=_PLOT_FLOAT_JS + cfg_literal("PRESETS", BLOOM_PRESETS) + BLOOM_SCRIPT,
    )


# ============================================================= mode: countmin

COUNTMIN_PRESETS = [
    {"key": "heavy-hitter", "label": "one key forty times, eleven others twice",
     "kind": "heavy", "w": 8, "d": 3, "seed": 2},
    {"key": "uniform", "label": "ten keys, six times each",
     "kind": "uniform", "w": 8, "d": 3, "seed": 2},
    {"key": "seeded", "label": "a seeded stream over twelve keys",
     "kind": "seeded", "w": 12, "d": 4, "seed": 2},
]

COUNTMIN_SCRIPT = r"""
  var grid = document.getElementById('hmGrid');
  var table = document.getElementById('hmTable');
  var status = document.getElementById('hmStatus');
  var preset = document.getElementById('hmPreset');
  var kindSel = document.getElementById('hmKind');
  var own = document.getElementById('hmStream');
  var CAP = 120;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('countmin: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    kindSel.value = p.kind;
    document.getElementById('hmW').value = p.w;
    document.getElementById('hmD').value = p.d;
    document.getElementById('hmSeed').value = p.seed;
  }

  function redraw() {
    var w = +document.getElementById('hmW').value;
    var d = +document.getElementById('hmD').value;
    var seed = +document.getElementById('hmSeed').value;
    document.getElementById('hmWOut').textContent = w + ' counters a row';
    document.getElementById('hmDOut').textContent = d + ' row' + (d === 1 ? '' : 's');
    document.getElementById('hmSeedOut').textContent = 'seed ' + seed;
    document.getElementById('hmStreamField').hidden = kindSel.value !== 'own';
    document.getElementById('hmSeedRow').hidden = kindSel.value !== 'seeded';

    var typed = hashParseStream(own.value, CAP);
    var stream = kindSel.value === 'own' ? typed.stream : streamPreset(kindSel.value, seed);
    if (!stream.length) {
      grid.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = 'Type a stream of positive whole numbers to sketch.';
      return;
    }
    var run = countMinRun(stream, w, d);
    var r = run.result;

    var heaviest = r.estimates.reduce(function (a, b) { return b.truth > a.truth ? b : a; });
    var hot = {};
    for (var i = 0; i < d; i += 1) {
      hot[i] = hashOf(heaviest.key * (2 * i + 1) + i, w, 'multiply');
    }
    drawSketch(grid, r.sketch, hot);

    document.getElementById('hmLen').textContent = r.total + ' updates';
    document.getElementById('hmKeys').textContent = r.estimates.length + ' distinct';
    document.getElementById('hmWorst').textContent = r.worstOver;
    document.getElementById('hmNever').textContent = r.neverUnder
      ? 'never below the truth' : 'UNDERESTIMATED';
    document.getElementById('hmEps').textContent = Rtext(r.eps) + ' = ' + Rfixed(r.eps, 4);
    document.getElementById('hmDelta').textContent = Rtext(r.delta) + ' = ' + Rfixed(r.delta, 5);
    document.getElementById('hmSlack').textContent = Rtext(Rmul(r.eps, R(BigInt(r.total), 1n)))
      + ' = ' + Rfixed(Rmul(r.eps, R(BigInt(r.total), 1n)), 2);

    var rows = '';
    r.estimates.forEach(function (e) {
      rows += '<tr' + (e.key === heaviest.key ? ' class="tone-amber"' : '') + '><td>' + e.key
        + '</td><td>' + e.truth + '</td><td>' + e.estimate + '</td><td'
        + (e.over ? ' class="tone-red"' : '') + '>' + e.over + '</td><td>'
        + (e.estimate >= e.truth ? 'never under' : 'UNDER') + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>key</th><th>true count</th><th>estimate</th>'
      + '<th>overcount</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = '';
    if (kindSel.value === 'own' && typed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + typed.ignored.join(' ')
        + '</span> &mdash; a stream is positive whole numbers. ';
    }
    if (kindSel.value === 'own' && typed.truncated) msg += 'Only the first ' + CAP + ' items are counted. ';
    msg += d + (d === 1 ? ' row' : ' rows') + ' of ' + w + ' counters take ' + r.total
      + ' updates over ' + r.estimates.length + ' distinct keys. Every estimate is the MINIMUM of the key&rsquo;s '
      + d + ' counters, so every one of them is <strong>'
      + (r.neverUnder ? 'at or above the truth' : 'not what the sketch promises') + '</strong>: '
      + 'a counter can only be raised by another key&rsquo;s updates, never lowered, so the error '
      + 'is one-sided by construction. The worst overcount here is <strong>' + r.worstOver
      + '</strong>. <span class="tone-cyan">With w = ' + w + ' the guarantee is Markov&rsquo;s, '
      + 'per row</span>: each row overcounts by ' + Rtext(r.eps) + ' of the ' + r.total
      + ' updates &mdash; that is ' + Rfixed(Rmul(r.eps, R(BigInt(r.total), 1n)), 2)
      + ' &mdash; with probability at most a half, so ' + d + ' rows leave at most '
      + Rtext(r.delta) + '. Both are exact fractions. The sharper e/w and e&#8315;&#7496; bounds '
      + 'need an inequality this library does not prove, so they are not quoted.';
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  kindSel.addEventListener('change', redraw);
  own.addEventListener('input', redraw);
  ['hmW', 'hmD', 'hmSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _countmin(cfg):
    p = COUNTMIN_PRESETS[_preset_index(cfg, COUNTMIN_PRESETS, "countmin")]
    markup = (
        _toolbar(
            "A sketch on a stream",
            "estimates against the truth, and the error only goes one way",
            _swatch("tone-cyan", "a counter")
            + _swatch("tone-amber", "the heaviest key's cells")
            + _swatch("tone-red", "an overcount"),
        )
        + _stage("hmStage", "hmGrid", "The sketch: d rows of w counters, shaded by their value.",
                 240, 660)
        + _table("hmTable")
        + _banner("hmStatus")
    )
    controls = (
        _select("hmPreset", "Worked example",
                [(q["key"], q["label"]) for q in COUNTMIN_PRESETS], p["key"])
        + _select("hmKind", "Stream",
                  [("heavy", "one heavy hitter among light keys"),
                   ("uniform", "every key equally often"),
                   ("seeded", "a seeded stream"),
                   ("own", "the stream you type")], p["kind"])
        + _range("hmW", "counters per row w", 4, 24, p["w"])
        + _range("hmD", "rows d", 1, 6, p["d"])
        + _range("hmSeed", "stream seed", 1, 40, p["seed"])
        + _text("hmStream", "Your stream", "1 1 1 1 2 2 3 4 4 4 5 1 1 2 6")
        + _kpi([
            ("hmLen", "Updates"),
            ("hmKeys", "Distinct keys"),
            ("hmWorst", "Worst overcount"),
            ("hmNever", "Direction of the error"),
            ("hmEps", "&epsilon; = 2/w"),
            ("hmDelta", "&delta; = 2&#8315;&#7496;"),
            ("hmSlack", "&epsilon; &times; updates"),
        ])
        + _hint(
            "hmHint",
            "The guarantee quoted is Markov's, applied per row, because that is the only tail "
            "inequality this library proves: each row overcounts by &epsilon; of the stream with "
            "probability at most a half, so d rows leave at most 2&#8315;&#7496;. The sharper e/w "
            "and e&#8315;&#7496; bounds need Chernoff, which is out of scope here.",
        )
    )
    return Lab(
        title="The Count-Min sketch",
        subtitle="Estimate by the minimum of d counters, and the error is one-sided",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Push a stream through and compare with the truth"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every key is hashed once per row and the estimate is the minimum of its `d` "
            "counters. Compare each estimate with the true count: the sketch is never below it, "
            "and the `(ε, δ)` the panel quotes are exact fractions of the `w` and `d` you chose.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", COUNTMIN_PRESETS) + COUNTMIN_SCRIPT,
    )


# --------------------------------------------------------------- the registry

_BUILDERS = {
    "chaining": _chaining,
    "probing": _probing,
    "resize": _resize,
    "universal": _universal,
    "balls": _balls,
    "bloom": _bloom,
    "countmin": _countmin,
}

MODES = tuple(_BUILDERS)


def hash_lab(cfg):
    """The hash-table kit: seven modes across two courses.

    An unknown mode RAISES. A silent fallback would render a finished-looking
    page carrying another lesson's widget -- the markup assertions pass, the
    lab runs, labcheck is happy, and the reader is shown the wrong arithmetic
    under the right title. Nothing else in the repository can see that.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "hash: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["HASHKIT_JS", "MODES", "hash_lab"]
