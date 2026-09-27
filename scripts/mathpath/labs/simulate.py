"""Simulation and variance reduction -- one kit, nine modes, one arithmetic.

Every earlier course on this path ended in a formula.  This one runs the model
instead, and then refuses to pretend the number it produced is the answer: a
simulation's output is a random variable, and the only honest report is an
estimate with an interval around it.  Each mode is one step of that, and the
last four are one idea in four costumes -- every one of them moves a covariance.

  sample       the generator, U = x/m, and the cumulative table AS the sampler
  montecarlo   the running mean, the exact sample variance, SE as a surd
  bound        +-k SE, the guarantee 1 - 1/k^2, and the coverage actually seen
  des          the event calendar, one event at a time, against the exact mean
  warmup       the transient, the bias it puts in a time-average, batch means
  crn          the same stream fed to both systems, and what it does to Var(A-B)
  antithetic   U against 1 - U, in the best case and in the worst one
  control      the variance as a quadratic in b, its vertex, and 1 - rho^2
  importance   p, q, the weights p/q, and the two variances that follow

Six decisions run through all nine.

  THE STREAM IS MINSTD, AND THE SEED IS MIXED BEFORE IT IS USED.  a = 16807,
  c = 0, m = 2^31 - 1, which is PRIME, with the splitmix64 finaliser on the
  seed.  Not the glibc constants, and the reason is specific to this kit rather
  than stylistic: a power-of-two modulus has low bits that are a CYCLE and not a
  sample -- x % 4 runs 0, 1, 2, 3 forever -- and this kit reduces.  `des` takes
  draws modulo a slot horizon, and a mode whose whole claim is that one run is
  not the expectation would have been demonstrating the claim's opposite.  The
  same defect, on another kit, made 1200 keys land in 4, 8 and 16 bins perfectly
  level and would have had a hash-imbalance lesson refute itself.  The seed is
  mixed because an LCG's k-th value is an AFFINE function of its seed -- under a
  purely multiplicative one it is literally seed x (a^k mod m) -- so the small
  seeds a slider offers walk a straight line instead of sampling, and six of
  these nine modes ask the reader to reseed and compare.  shard.py's
  `shardSeedState` and measure.py's `measureSeedState` are the same finaliser,
  for the same reason.

  ONE MODE USES A DIFFERENT GENERATOR ON PURPOSE, AND SAYS SO.  `sample` is the
  lesson ABOUT generators: the reader sets a, c, m and the seed, and the page
  reports the Hull-Dobell conditions for whatever they chose.  Its opening
  parameters are a = 25173, c = 13849, m = 65536, whose modulus is a power of
  two -- which is safe in that mode and only in that mode, because a sampled
  value there comes from comparing U against a cumulative table, which reads the
  HIGH bits of x, never x modulo a small number.  The page carries MINSTD as one
  of its choices so the two can be compared, and says in one line why every
  other page of this course uses the prime modulus.

  EVERY SAMPLE STATISTIC IS AN EXACT FRACTION, because the stream is integers
  and the sampled values are rational.  A sample mean over 200 draws prints as
  413/200; a sample variance, a covariance and a coverage count are ratios of
  integers.  Three quantities here are genuinely irrational and each is printed
  in exact form and then rounded WITH THE ROUNDING LABELLED: the standard error
  sqrt(s^2/n), the half-width k SE built on it, and rho.  Of rho, the quantity
  that matters -- rho^2 = Cov^2/(Var X . Var C) -- is itself an exact rational,
  so the reduction factor 1 - rho^2 is exact even where rho is not.  `Rsurd`
  carries the root exactly and `surdDec` is the only function that rounds.

  THERE IS NO NORMAL DISTRIBUTION ANYWHERE, AND THE COST IS PRINTED.  The only
  interval this path can justify is Chebyshev's, which holds for every
  distribution with a finite variance.  At k = 5 the guarantee is 1 - 1/25 =
  24/25 = 96%; the folklore +-2 SE guarantees 1 - 1/4 = 3/4 and nothing more,
  because the 95% figure comes from an approximation this path has not built.
  Five standard errors against two is a width ratio of exactly 5/2 = 2.5, and
  buying that width back with runs instead costs (5/2)^2 = 25/4 = 6.25 times as
  many.  `bound` prints 5/2 and 25/4 as fractions.  The phrase "five times
  wider" is wrong as a width and appears nowhere.

  THE CALENDAR IS NEVER QUERIED.  `des` is one of the hardest labs on this path
  because its table changes shape at every event: different columns in service,
  different queue contents, a pending list of varying length.  Two rules make
  that safe.  `desRun` returns the COMPLETE snapshot per event, so rendering
  event i is a pure function of i and the second window.redrawLab() reproduces
  the first exactly.  And the calendar is written as innerHTML into ONE element
  the markup declares, and nothing is ever read back out of it -- the failure
  mode the contract is guarding against is a script that builds markup and then
  reaches into it, because querySelector returns null in the test DOM and
  reading an id the markup does not declare throws.  Writing into a declared id
  and reading nothing cannot fail that way.

  NEXT-EVENT SIMULATION IS NOT A DIFFERENT MODEL FROM FIXED-TICK, and this kit
  does not pretend otherwise.  The queue simulated here is the slotted chain the
  previous course solved exactly, for which fixed-tick simulation IS the model;
  next-event simulation is the efficient form of the same computation, skipping
  the slots where nothing happens, and the two agree slot for slot.  They
  diverge only for continuous-time systems, which this path does not sample.
  `des` states that positively rather than listing it as an error.

WHAT SECTION 4.12's BLOCK LIST ASKS FOR AND THIS KIT DOES NOT TAKE, each with
its reason, because a block shipped for one function is bytes on every page:

  * `algebra_core.PLOT_JS` -- 3.6 KB gzipped, and the two figures that wanted it
    (the quadratic in b, and a running mean) are a polyline and a dozen marks.
    `simPlot` below is what replaced it; duality.py made the same cut for the
    same reason.  PLOT_JS also fixes its own 660x420 viewBox, which is taller
    than any figure here needs.
  * `sysdesign_core.APPROX_JS` -- its `standardErrorApprox` is a double's
    Math.sqrt.  This kit prints the standard error as an EXACT surd and rounds
    it once with `surdDec`, which is strictly better evidence, so taking the
    block would ship a float square root that no page calls.
  * `probability.FRACTION_JS` -- Number-based fractions with a Number gcd.  Every
    fraction in this kit is BigInt over BigInt; a second, lossy fraction type on
    the same page is a defect waiting to be reached for.

And one the list omits but names a function from: `geoGeo1` ships in
`sysdesign_core.SLOTTED_JS`, not in QUEUE_JS, so `des`, `warmup`, `crn` and
`control` take SLOTTED_JS.  That is the point of the shared function -- the
exact mean this course measures against is the same code the System Design
course prints, so the two subjects cannot disagree about 12/5.

MEASURED, on rendered lesson pages rather than on the lab alone, because the
lab alone is not what a reader downloads.  The ceiling is 62 KB gzipped (root
AGENTS.md, "A note on page weight").  The nine modes come in between 37.0 and
42.7 KB gzipped, measured by rendering each of them into the longest lesson on a
generated path, so the prose and chrome around the lab are a real page's; the
heaviest are `warmup` and `control`, which ship the exact transient and the
surds on top of the run.  That leaves 19 KB of headroom at the worst mode.

Where the weight is.  or_core's own share -- RATIONAL_JS, ORFMT_JS and SIM_JS
together -- is 6.2 KB gzipped, against the 4.8 KB section 4.12 estimated for
SIM_JS alone; this kit's own six blocks are 11.9 KB gzipped if all six shipped
together, and no mode takes all six.  Of the borrowed blocks, `number.NT_JS` is
the dear one at 2.7 KB and only `sample` carries it, which is the whole argument
for selecting per mode: it is there for one function, `hullDobell`, on the one
page that certifies a period.  Re-derive all of these rather than trusting them;
they go stale every time a block grows.
"""

import json

from .algebra_core import RATIONAL_JS, SURD_JS
from .common import Lab
from .number import NT_JS
from .or_core import ORFMT_JS, SIM_JS
from .sysdesign_core import PMF_JS, SLOTTED_JS, STREAM_JS, TRACE_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

SIMBASE_JS = r"""
  /* ============================================================== printing

     Reader text reaches innerHTML and this course's readers type < and > all
     day, so it is escaped once, at the boundary.  Written here rather than
     borrowed from algebra_systems.FORMAT_JS because taking that block for six
     one-line helpers would put 1.3 KB gzipped on all nine pages of this course
     to save forty lines on one of them. */
  function simEsc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function simTd(t, cls) { return '<td' + (cls ? ' class="' + cls + '"' : '') + '>' + t + '</td>'; }
  function simTdl(t, cls) { return '<td style="text-align:left;"' + (cls ? ' class="' + cls + '"' : '') + '>' + t + '</td>'; }
  function simTh(t) { return '<th>' + t + '</th>'; }
  function simTr(cells, cls) { return '<tr' + (cls ? ' class="' + cls + '"' : '') + '>' + cells.join('') + '</tr>'; }
  function simHead(cells) { return '<thead>' + simTr(cells.map(simTh)) + '</thead>'; }
  function simChip(t, kind) { return '<span class="chip' + (kind ? ' ' + kind : '') + '">' + t + '</span>'; }
  function simTick(ok) { return simChip(ok ? 'holds' : 'fails', ok ? 'ok' : 'no'); }

  /* A rational as a fraction when a reader can read it and a labelled decimal
     when the exact form has run to twenty digits.  Rshort makes that cut on
     DIGITS; this only adds the word, because an unlabelled decimal on a page
     that promises exactness is the one thing worse than a fraction nobody can
     read. */
  function simNum(a, places) {
    if (a === null || a === undefined) return '&mdash;';
    var exact = Rtext(a);
    if (exact.length <= 19) return exact;
    /* "shown to N places" rather than "rounded": these numbers ARE exact -- a
       ratio of two whole numbers -- and only their printed form is cut short.
       "(rounded)" is reserved for the three quantities on this course that are
       genuinely irrational, and saying it of a rational is the kind of small
       untruth that makes a reader distrust the ones that are true. */
    var pl = places === undefined ? 5 : places;
    return Rfixed(a, pl) + ' (exact, shown to ' + pl + ' places)';
  }
  /* Reader input that might be nonsense.  A bad value becomes a sentence in the
     status banner rather than an exception. */
  function simReadInt(text, lo, hi) {
    var s = String(text).trim();
    if (!/^[0-9]+$/.test(s)) return null;
    var v = BigInt(s);
    if (v < BigInt(lo) || v > BigInt(hi)) return null;
    return v;
  }

  /* ========================================================= pixels, and only

     Nothing downstream reads these back: an exact rational becomes an x or a y
     here, and every number that is REPORTED stays on the exact side. */
  function simPx(r) { return Number(r.n) / Number(r.d); }
  function simAt(v, lo, hi, a, b) { return a + (v - lo) * (b - a) / (hi - lo || 1); }
  function simEl(tag, attrs, inner) {
    var s = '<' + tag, k;
    for (k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k) && attrs[k] !== null && attrs[k] !== undefined) {
        s += ' ' + k + '="' + attrs[k] + '"';
      }
    }
    return inner === undefined ? s + ' />' : s + '>' + inner + '</' + tag + '>';
  }
  function simLabel(x, y, text, tone, anchor, size) {
    return simEl('text', { x: x, y: y, 'font-size': size || 10, 'text-anchor': anchor || 'start',
                           fill: 'var(--' + (tone || 'muted') + ')' }, text);
  }

  /* ==================================================== THE STREAM, ONCE

     MINSTD: a = 16807, c = 0, m = 2^31 - 1, prime.  The module docstring says
     why this kit does not use a power-of-two modulus; the short version is that
     this kit REDUCES, and the low bits of a power-of-two modulus are a cycle
     rather than a sample.

     The seed never becomes the state.  An LCG's k-th value is affine in its
     seed, so seeds 1, 2, 3 produce three points on a straight line rather than
     three samples of anything, and six of these nine modes ask the reader to
     reseed.  The finaliser is splitmix64 -- multiply, xor-shift, multiply,
     xor-shift -- which is nonlinear over the integers and breaks the affinity. */
  function simMultiplier() { return 16807; }
  function simModulus() { return 2147483647; }
  function simSeedState(seed) {
    var mask = 0xFFFFFFFFFFFFFFFFn;
    var x = (BigInt(seed) + 1n) * 0x9E3779B97F4A7C15n & mask;
    x = ((x ^ (x >> 30n)) * 0xBF58476D1CE4E5B9n) & mask;
    x = ((x ^ (x >> 27n)) * 0x94D049BB133111EBn) & mask;
    x = x ^ (x >> 31n);
    return Number(x % BigInt(simModulus() - 1)) + 1;      /* never the fixed point 0 */
  }
  function simStream(seed, count) {
    return lcgStream(simMultiplier(), 0, simModulus(), simSeedState(seed), count);
  }
  /* Uniform rationals in (0, 1), exact fractions over the modulus.  The modulus
     is odd, so U is never exactly 1/2 and no comparison in this kit has to
     decide a tie it cannot decide. */
  function simUniform(seed, count) {
    var m = BigInt(simModulus());
    return simStream(seed, count).map(function (x) { return R(BigInt(x), m); });
  }
  /* Inverse-transform sampling over a whole seeded run.

     This is the SAME rule sampleFromPmf applies -- the first value whose
     cumulative probability reaches U -- carried out on the integers the stream
     produces rather than on the fraction x/m.  U < F(k) is x d < n m when
     F(k) = n/d, and that comparison is exact in whole numbers and allocates
     nothing, where the rational form builds a fraction and runs a gcd per draw
     per candidate.  Measured: a mode that draws forty thousand values went from
     nine hundred milliseconds to a hundred and forty, which is the difference
     between a slider and a stall.

     THE TWO PATHS ARE HELD TOGETHER RATHER THAN TRUSTED.  Every row this kit
     PRINTS is sampleFromPmf's own answer, and scripts/mathcheck.js requires the
     two to agree draw for draw over a full run on every table the kit ships --
     because a fast path that disagreed with the definition would quietly be a
     different lesson.  Doubles are used only where both sides of the comparison
     are integers inside their exact range; past that the same comparison runs in
     BigInt, and `safe` is where that is decided rather than assumed. */
  function simDraws(pairs, seed, count) {
    var M = simModulus(), Mb = BigInt(M), raw = simStream(seed, count);
    var cum = simCumulative(pairs), i, j, k;
    var LIMIT = 9007199254740991;
    var safe = true, bigN = [], bigD = [], numN = [], numD = [];
    for (i = 0; i < cum.length; i += 1) {
      bigN.push(cum[i].hi.n); bigD.push(cum[i].hi.d);
      numN.push(Number(cum[i].hi.n)); numD.push(Number(cum[i].hi.d));
      if (Number(cum[i].hi.d) * M > LIMIT) safe = false;
    }
    var last = cum.length - 1, out = [];
    for (j = 0; j < count; j += 1) {
      var v = cum[last].value;
      if (safe) {
        for (k = 0; k < cum.length; k += 1) {
          if (raw[j] * numD[k] < numN[k] * M) { v = cum[k].value; break; }
        }
      } else {
        var xb = BigInt(raw[j]);
        for (k = 0; k < cum.length; k += 1) {
          if (xb * bigD[k] < bigN[k] * Mb) { v = cum[k].value; break; }
        }
      }
      out.push(v);
    }
    return out;
  }
  /* The empirical frequency of every value of a pmf, as an exact fraction of
     the number of draws, beside the theoretical probability. */
  function simFrequencies(pairs, draws) {
    var counts = {}, i, out = [], n = draws.length;
    for (i = 0; i < draws.length; i += 1) {
      var key = Rtext(draws[i]);
      counts[key] = (counts[key] || 0) + 1;
    }
    for (i = 0; i < pairs.length; i += 1) {
      var c = counts[Rtext(pairs[i][0])] || 0;
      out.push({ value: pairs[i][0], count: c, p: pairs[i][1],
                 empirical: n ? R(BigInt(c), BigInt(n)) : R0,
                 expected: Rmul(pairs[i][1], R(BigInt(n), 1n)) });
    }
    return out;
  }
  /* The exact mean and variance OF A PMF -- the numbers every estimate on this
     course is measured against, and the reason it is a measurement rather than
     a demonstration. */
  function simPmfMean(pairs) {
    var m = R0, i;
    for (i = 0; i < pairs.length; i += 1) m = Radd(m, Rmul(pairs[i][0], pairs[i][1]));
    return m;
  }
  function simPmfVar(pairs) {
    var m = simPmfMean(pairs), v = R0, i;
    for (i = 0; i < pairs.length; i += 1) {
      var d = Rsub(pairs[i][0], m);
      v = Radd(v, Rmul(pairs[i][1], Rmul(d, d)));
    }
    return v;
  }
  /* The cumulative table.  It is not a helper: it IS the sampler, and the first
     lesson's whole claim is that there is nothing else in the box. */
  function simCumulative(pairs) {
    var cum = R0, out = [], i;
    for (i = 0; i < pairs.length; i += 1) {
      var lo = cum;
      cum = Radd(cum, pairs[i][1]);
      out.push({ value: pairs[i][0], p: pairs[i][1], lo: lo, hi: cum });
    }
    return out;
  }
  /* The running mean after each draw, which is what a reader watches settle --
     and, the lesson's misconception, what a slow process ALSO looks like. */
  function simRunningMean(xs) {
    var s = R0, out = [], i;
    for (i = 0; i < xs.length; i += 1) {
      s = Radd(s, xs[i]);
      out.push(Rdiv(s, R(BigInt(i + 1), 1n)));
    }
    return out;
  }
"""


SIMSURD_JS = r"""
  /* THE ONE ROOT ON THIS COURSE, and the two functions that take it.

     These are a block of their own rather than part of SIMBASE_JS because they
     call `Rsurd` and `surdtext` from algebra_core.SURD_JS, and only three of the
     nine modes print a standard error.  Left in the base block they were
     declarations referring to functions six pages do not carry: harmless while
     nobody called them, and a throw on the first redraw the moment somebody did.
     A block whose dependencies are not the base block's dependencies is a
     separate block -- that is the whole rule, and a static scan of which mode
     calls what is what found this one. */

  /* sqrt(s^2 / n) as an exact surd.  The variance under the root stays a
     fraction; the root is where this course's exactness ends, and it ends here
     and in one other place (the Chebyshev half-width built on it). */
  function simStandardError(variance, n) {
    if (variance === null || !n) return null;
    return Rsurd(Rdiv(variance, R(BigInt(n), 1n)));
  }
  /* A surd and its decimal, with the rounding NAMED.  Every standard error this
     course prints is printed in this shape: the exact form first, because that is
     the evidence, and the decimal after it, because a reader reads a decimal --
     with the word "rounded" attached, because an unlabelled decimal on a page
     that promises exactness is the one thing worse than an unreadable fraction. */
  function simSurd(s, places) {
    if (s === null) return '&mdash;';
    if (s.k === 1n) return Rtext(s.q);
    return surdtext(s) + ' = ' + surdDec(s, places === undefined ? 4 : places) + ' (rounded)';
  }
"""

SIMDRAW_JS = r"""
  /* THE SHARED FIGURE: several series, a band, a shaded span, rules and marks,
     with exact values turned into pixels at the last moment.  Six modes draw on
     it -- a running mean with a narrowing ribbon, replication means inside a
     Chebyshev band, an occupancy trace with its transient shaded, a variance
     parabola with its vertex, a weight trace -- so the shapes are declared here
     once and nothing closes over a document element. */
  function simPlot(spec) {
    var w = spec.width || 660, h = spec.height || 230;
    var L = spec.left || 48, Rm = 14, T = 14, B = 28, i, k;
    var xs = [], ys = [];
    for (i = 0; i < (spec.series || []).length; i += 1) {
      for (k = 0; k < spec.series[i].pts.length; k += 1) {
        xs.push(spec.series[i].pts[k][0]); ys.push(spec.series[i].pts[k][1]);
      }
    }
    for (i = 0; i < (spec.bands || []).length; i += 1) {
      for (k = 0; k < spec.bands[i].pts.length; k += 1) {
        xs.push(spec.bands[i].pts[k][0]);
        ys.push(spec.bands[i].pts[k][1]); ys.push(spec.bands[i].pts[k][2]);
      }
    }
    for (i = 0; i < (spec.rules || []).length; i += 1) ys.push(spec.rules[i].y);
    for (i = 0; i < (spec.marks || []).length; i += 1) { xs.push(spec.marks[i].x); ys.push(spec.marks[i].y); }
    if (!xs.length) return { svg: simLabel(L, h / 2, 'nothing to draw yet', 'muted'), height: h };
    var x0 = spec.x0 !== undefined ? spec.x0 : Math.min.apply(null, xs);
    var x1 = spec.x1 !== undefined ? spec.x1 : Math.max.apply(null, xs);
    var y0 = spec.y0 !== undefined ? spec.y0 : Math.min.apply(null, ys);
    var y1 = spec.y1 !== undefined ? spec.y1 : Math.max.apply(null, ys);
    if (!(x1 > x0)) x1 = x0 + 1;
    if (!(y1 > y0)) y1 = y0 + 1;
    var pad = (y1 - y0) * 0.06;
    y0 -= pad; y1 += pad;
    var px = function (v) { return simAt(v, x0, x1, L, w - Rm); };
    var py = function (v) { return simAt(v, y0, y1, h - B, T); };
    var s = '';
    /* The shaded span goes down first: it is a region of the x axis (a warm-up
       discarded, a batch), and everything else has to read on top of it. */
    for (i = 0; i < (spec.spans || []).length; i += 1) {
      var sp = spec.spans[i];
      s += simEl('rect', { x: px(sp.x0), y: T, width: Math.max(0.5, px(sp.x1) - px(sp.x0)), height: h - B - T,
                           fill: 'var(--' + (sp.tone || 'amber') + ')', 'fill-opacity': sp.opacity || '0.13' });
      if (sp.label) s += simLabel(px(sp.x0) + 4, T + 11, sp.label, sp.tone || 'amber', 'start', 9);
    }
    for (i = 0; i < 4; i += 1) {
      var gy = y0 + ((y1 - y0) * i) / 3;
      s += simEl('line', { x1: L, y1: py(gy), x2: w - Rm, y2: py(gy), stroke: 'var(--line)', 'stroke-width': 0.6 });
      s += simLabel(L - 5, py(gy) + 3, (spec.fmtY ? spec.fmtY(gy) : gy.toFixed(2)), 'muted', 'end', 9);
    }
    s += simEl('line', { x1: L, y1: h - B, x2: w - Rm, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 })
       + simEl('line', { x1: L, y1: T, x2: L, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 });
    /* The band: a ribbon between two y values at each x, as one polygon, so a
       +-SE ribbon narrowing with n reads as a shape and not as two lines. */
    for (i = 0; i < (spec.bands || []).length; i += 1) {
      var bd = spec.bands[i], up = [], down = [];
      for (k = 0; k < bd.pts.length; k += 1) {
        up.push(px(bd.pts[k][0]) + ',' + py(bd.pts[k][2]));
        down.push(px(bd.pts[k][0]) + ',' + py(bd.pts[k][1]));
      }
      down.reverse();
      s += simEl('polygon', { points: up.concat(down).join(' '), fill: 'var(--' + (bd.tone || 'cyan') + ')',
                              'fill-opacity': bd.opacity || '0.15' });
    }
    for (i = 0; i < (spec.rules || []).length; i += 1) {
      var ru = spec.rules[i];
      s += simEl('line', { x1: L, y1: py(ru.y), x2: w - Rm, y2: py(ru.y), stroke: 'var(--' + (ru.tone || 'green') + ')',
                           'stroke-width': 1.3, 'stroke-dasharray': ru.solid ? null : '6 4' });
      if (ru.label) s += simLabel(w - Rm - 2, py(ru.y) - 4, ru.label, ru.tone || 'green', 'end', 9.5);
    }
    for (i = 0; i < (spec.series || []).length; i += 1) {
      var ser = spec.series[i], pts = ser.pts, d = '';
      for (k = 0; k < pts.length; k += 1) {
        if (k === 0) d += 'M' + px(pts[k][0]) + ' ' + py(pts[k][1]);
        else if (ser.step) d += 'L' + px(pts[k][0]) + ' ' + py(pts[k - 1][1]) + 'L' + px(pts[k][0]) + ' ' + py(pts[k][1]);
        else d += 'L' + px(pts[k][0]) + ' ' + py(pts[k][1]);
      }
      s += simEl('path', { d: d, fill: 'none', stroke: 'var(--' + ser.tone + ')',
                           'stroke-width': ser.thin ? 1 : 1.8, 'stroke-dasharray': ser.dashed ? '5 3' : null });
      if (ser.dots) {
        for (k = 0; k < pts.length; k += 1) {
          s += simEl('circle', { cx: px(pts[k][0]), cy: py(pts[k][1]), r: ser.r || 2.6,
                                 fill: 'var(--' + ser.tone + ')' });
        }
      }
      if (ser.label && pts.length) {
        s += simLabel(px(pts[pts.length - 1][0]) - 2, py(pts[pts.length - 1][1]) - 6, ser.label, ser.tone, 'end', 9.5);
      }
    }
    for (i = 0; i < (spec.marks || []).length; i += 1) {
      var mk = spec.marks[i];
      s += simEl('circle', { cx: px(mk.x), cy: py(mk.y), r: mk.r || 4, fill: 'var(--' + (mk.tone || 'purple') + ')',
                             'fill-opacity': mk.hollow ? '0.25' : '1',
                             stroke: 'var(--' + (mk.tone || 'purple') + ')', 'stroke-width': 1.2 });
      if (mk.label) s += simLabel(px(mk.x) + 7, py(mk.y) - 6, mk.label, mk.tone || 'purple', 'start', 9.5);
    }
    for (i = 0; i < (spec.drops || []).length; i += 1) {
      var dr = spec.drops[i];
      s += simEl('line', { x1: px(dr.x), y1: T, x2: px(dr.x), y2: h - B, stroke: 'var(--' + (dr.tone || 'amber') + ')',
                           'stroke-width': 1, 'stroke-dasharray': '3 3' });
      if (dr.label) s += simLabel(px(dr.x) + 3, T + 10, dr.label, dr.tone || 'amber', 'start', 9);
    }
    s += simLabel(L, h - 8, (spec.fmtX ? spec.fmtX(x0) : String(x0)), 'muted', 'start', 9);
    s += simLabel(w - Rm, h - 8, spec.xLabel || '', 'text', 'end', 10);
    return { svg: s, height: h, x0: x0, x1: x1, y0: y0, y1: y1 };
  }

  /* THE SHARED BARS: two or three variances whose ORDER is the lesson, drawn so
     that "this one is a quarter of that one" is visible rather than read out of
     a table. */
  function simBars(items, spec) {
    var w = (spec || {}).width || 660, rowH = 30, L = (spec || {}).left || 168, Rm = 108, i;
    var top = null;
    for (i = 0; i < items.length; i += 1) {
      var v = Math.abs(simPx(items[i].value));
      if (top === null || v > top) top = v;
    }
    if (!top) top = 1;
    var s = '';
    for (i = 0; i < items.length; i += 1) {
      var y = 8 + i * rowH, len = (Math.abs(simPx(items[i].value)) / top) * (w - L - Rm);
      s += simLabel(L - 8, y + 14, items[i].label, items[i].tone, 'end', 10);
      s += simEl('rect', { x: L, y: y + 4, width: Math.max(1, len), height: 14, rx: 2,
                           fill: 'var(--' + items[i].tone + ')', 'fill-opacity': '0.75' });
      s += simLabel(L + len + 6, y + 15, items[i].text || simNum(items[i].value, 4), items[i].tone, 'start', 10);
    }
    return { svg: s, height: 14 + items.length * rowH };
  }
"""


SIMSTAIR_JS = r"""
  /* The cumulative staircase, with each draw shown LANDING in its step.

     This is the only figure on the course that has to make a sampler visible
     rather than a statistic, so the drawing is the argument: F(k) as a step
     function on the vertical axis, the intervals it cuts [0, 1) into as bands,
     and each U as a tick inside the band it fell in.  A reader who has seen
     U = 19511/32768 land in the third band does not then reach for floor(kU)+1. */
  function simStaircase(cum, us, spec) {
    var w = (spec || {}).width || 660, h = (spec || {}).height || 240;
    var L = 56, Rm = 118, T = 14, B = 26, i, k;
    var py = function (v) { return simAt(v, 0, 1, h - B, T); };
    var s = simEl('line', { x1: L, y1: h - B, x2: w - Rm, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 })
          + simEl('line', { x1: L, y1: T, x2: L, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 });
    var tones = ['cyan', 'green', 'amber', 'purple', 'blue', 'red'];
    for (i = 0; i < cum.length; i += 1) {
      var lo = simPx(cum[i].lo), hi = simPx(cum[i].hi), tone = tones[i % tones.length];
      s += simEl('rect', { x: L, y: py(hi), width: w - Rm - L, height: Math.max(0.8, py(lo) - py(hi)), rx: 1,
                           fill: 'var(--' + tone + ')', 'fill-opacity': '0.13' });
      s += simEl('line', { x1: L, y1: py(hi), x2: w - Rm, y2: py(hi), stroke: 'var(--' + tone + ')',
                           'stroke-width': 1.4 });
      s += simLabel(L - 6, py((lo + hi) / 2) + 3, Rtext(cum[i].hi), tone, 'end', 9);
      s += simLabel(w - Rm + 8, py((lo + hi) / 2) + 3,
                    'value ' + Rtext(cum[i].value) + ', p = ' + Rtext(cum[i].p), tone, 'start', 9.5);
    }
    /* Every draw shown is a draw the table below also lists: the picture and the
       table come out of the same array, so they cannot disagree. */
    for (k = 0; k < us.length; k += 1) {
      var x = simAt(k + 0.5, 0, us.length, L + 4, w - Rm - 4), u = simPx(us[k]);
      s += simEl('line', { x1: x, y1: py(u) - 5, x2: x, y2: py(u) + 5, stroke: 'var(--text)', 'stroke-width': 1.6 });
      s += simEl('circle', { cx: x, cy: py(u), r: 2.4, fill: 'var(--text)' });
    }
    s += simLabel(L, h - 8, 'draw 1', 'muted', 'start', 9);
    s += simLabel(w - Rm, h - 8, 'draw ' + us.length, 'muted', 'end', 9);
    s += simLabel(L - 6, T + 4, 'F', 'muted', 'end', 9);
    return { svg: s, height: h };
  }
"""


SIMQ_JS = r"""
  /* THE SLOTTED QUEUE, SIMULATED.

     The model is the one the previous course solved exactly: Bernoulli arrivals
     with probability p per slot, geometric service with parameter q, single
     server, first in first out.  Both distributions are sampled by inverse
     transform from the seeded stream, so the run is reproducible from its seed
     and every quantity it produces is a fraction.

     ONE STREAM, TWO PURPOSES, AT FIXED OFFSETS.  Slot t's arrival test reads
     draw t, and the i-th arrival's service reads draw T + i.  The offsets are
     fixed rather than consumed in order because common random numbers is a whole
     lesson of this course: two configurations differing only in q must see the
     SAME arrivals, and they only do if the arrival draws sit at indices that do
     not depend on how many service draws have been taken.  Consuming one stream
     in event order would silently decorrelate the two runs, and the mode built
     to measure that correlation would report a smaller one than it should.

     The service duration is a geometric variate on {1, 2, ...}: the smallest s
     with 1 - (1-q)^s > U.  The tail is carried as a running product, so the
     inverse transform costs one multiplication per slot of service rather than a
     power per candidate.

     ARITHMETIC IN WHOLE NUMBERS, FOR THE SAME REASON simDraws USES IT.  The
     arrival test is U < p, which is x pd < pn m, and both sides are integers far
     inside a double's exact range for any arrival probability a lesson states;
     the service test is (1 - q)^s < 1 - U, which is (qd - qn)^s m < (m - x) qd^s,
     and that one needs BigInt because qd^s outgrows a double at about the
     twentieth slot of service.  Neither is an approximation of the rational
     comparison -- they are the rational comparison, cross-multiplied.  Measured:
     the comparison mode's widest setting went from nine hundred milliseconds to
     a hundred and forty. */
  function simService(x, M, qn, qd) {
    var fail = qd - qn, num = fail, den = qd, rest = M - x, s = 1;
    while (num * M >= rest * den && s < 4000) { num *= fail; den *= qd; s += 1; }
    return s;
  }
  function simSlotRun(p, q, T, seed) {
    var raw = simStream(seed, 2 * T), M = simModulus(), Mb = BigInt(M);
    var pn = Number(p.n), pd = Number(p.d);
    var arrivals = [], services = [], t;
    for (t = 0; t < T; t += 1) {
      if (raw[t] * pd < pn * M) {
        arrivals.push(t);
        services.push(simService(BigInt(raw[T + services.length]), Mb, q.n, q.d));
      }
    }
    /* First in, first out on a single server: service starts when the server is
       free and the customer has arrived, whichever is later. */
    var free = 0, starts = [], departs = [], i, area = 0;
    for (i = 0; i < arrivals.length; i += 1) {
      var st = arrivals[i] > free ? arrivals[i] : free;
      starts.push(st); free = st + services[i]; departs.push(free);
      area += departs[i] - arrivals[i];
    }
    /* THE AREA IS THE ESTIMATE.  Customer i is in the system over the slots
       [arrival, departure), so the sum of those lengths is both the integral of
       N(t) and the sum of the customers' times -- which is Little's Law as an
       identity about averages rather than as a model, and is exactly what
       littleFromTrace computes from the same two arrays. */
    return { arrivals: arrivals, services: services, starts: starts, departs: departs,
             T: T, area: area, count: arrivals.length,
             L: R(BigInt(area), BigInt(T)),
             lambda: R(BigInt(arrivals.length), BigInt(T)),
             busy: services.reduce(function (a, b) { return a + b; }, 0) };
  }
  /* The occupancy over a window of slots, and the time-average over it.  The
     window is what the warm-up lesson moves: an average from slot 0 is an
     average of a system that was never in steady state. */
  function simWindowAverage(run, w, T) {
    var occ = occupancyTrace(run.arrivals, run.departs, T), s = 0, t;
    for (t = w; t < T; t += 1) s += occ[t];
    return { occupancy: occ, from: w, to: T,
             average: T > w ? R(BigInt(s), BigInt(T - w)) : null,
             naive: T > 0 ? R(BigInt(occ.reduce(function (a, b) { return a + b; }, 0)), BigInt(T)) : null };
  }
  /* The first k customers of a run, as a run.

     THIS IS NOT AN OPTIMISATION, IT IS A BOUND ON A QUADRATIC.  desRun returns
     the complete pending calendar with every snapshot, which is what makes
     rendering event i a pure function of i -- and also what makes the whole
     structure quadratic in the number of events.  A four-thousand-slot run has
     three thousand events and would build four and a half million calendar
     entries to show a reader twenty.  The head of a first-in-first-out run on a
     single server is exact: customer j's start and departure depend only on
     customers before j, so the first k rows of the truncated run are the first k
     rows of the whole one, and the long-run average is computed from the full
     arrays without going near desRun. */
  function simRunHead(run, k) {
    var n = Math.min(k, run.arrivals.length);
    return { arrivals: run.arrivals.slice(0, n), services: run.services.slice(0, n),
             starts: run.starts.slice(0, n), departs: run.departs.slice(0, n),
             T: run.T, count: n };
  }
  /* The calendar, as desRun's per-event snapshots, plus the queue contents each
     snapshot implies: who holds the server and who is queued behind them.

     THE ACTIVE SET IS WALKED, NOT RECOMPUTED FROM THE CLOCK.  The obvious
     implementation asks, at clock t, which customers satisfy arrival <= t <
     departure -- and it disagrees with desRun's own count whenever two events
     share an instant.  A departure at t is taken before an arrival at t, so
     immediately after the departure event desRun has the arriving customer NOT
     yet in the system while the clock test already includes them: the table then
     says three in system and lists two.  That defect was in this block until
     mathcheck compared the two.  Walking the same event list desRun returns, one
     event at a time, makes the count and the contents the same object by
     construction rather than by agreement.

     The head of the active set is the one in service, because the server is
     first in first out and never idle while anyone is present: the earliest
     still-present customer either started when it arrived to an empty server or
     started the instant its predecessor left. */
  function simCalendar(run, limit) {
    var des = desRun(run.arrivals.map(function (t) { return R(BigInt(t), 1n); }),
                     run.services.map(function (s) { return R(BigInt(s), 1n); }));
    var events = des.events.slice(0, limit === undefined ? des.events.length : limit);
    var active = [], out = [], i, at;
    for (i = 0; i < events.length; i += 1) {
      var ev = events[i];
      if (ev.kind === 'arrival') {
        active.push(ev.who);
      } else {
        at = active.indexOf(ev.who);
        if (at >= 0) active.splice(at, 1);
      }
      out.push({ index: i, t: ev.t, kind: ev.kind, who: ev.who, inSystem: ev.inSystem,
                 serving: active.length ? active[0] : null,
                 waiting: active.slice(1),
                 pending: ev.calendarAfter.slice(0, 4),
                 pendingMore: Math.max(0, ev.calendarAfter.length - 4) });
    }
    return { events: out, total: des.events.length, des: des };
  }
"""


SIMCHAIN_JS = r"""
  /* pi_0 P^t, EXACTLY, for the slotted chain -- which is what turns the warm-up
     lesson from "the start looks low" into a statement with numbers behind it.

     THE CHAIN.  N_t is the number in system at the end of slot t.  Within a slot
     a departure happens first, with probability q when someone is in service,
     and then an arrival, with probability p.  So from state n the chain steps to
     n - 1, n or n + 1, and from 0 only to 0 or 1.  At p = 2/5 and q = 1/2 that
     gives E[N_0] = 0, E[N_1] = 2/5, E[N_2] = 3/5, E[N_3] = 37/50 and
     E[N_4] = 17/20, climbing toward the stationary 12/5 -- and those five
     fractions are the check that the convention here is the convention geoGeo1
     solved, rather than a neighbouring one that differs by a slot.

     WHY THE VECTOR IS INTEGERS OVER A COMMON DENOMINATOR.  The obvious
     implementation carries pi_t as rationals and calls R() once per entry per
     step, and R() runs a gcd.  After four hundred steps the denominators are
     eight hundred digits wide and those gcds cost more than everything else on
     the page put together.  Held as BigInt numerators over a single power of the
     step denominator, a step is multiply-and-add with no gcd at all, and the two
     window averages the lesson prints are accumulated in the same integers with
     exactly one gcd between them.

     AND WHY THE FLOAT FOR THE DRAWING IS A LONG DIVISION.  Number(n)/Number(d)
     on an eight-hundred-digit fraction is Infinity/Infinity, which is NaN -- and
     a NaN y coordinate draws a curve with holes in it and reports nothing wrong.
     That defect was in this block until it was measured: E[N_399] came back NaN
     while every printed figure beside it was right.  `values` is the exact
     numerator long-divided by the exact denominator in BigInt and then scaled
     down, so it is a correctly rounded six-place decimal of the exact value at
     every t, and it is used for pixels and for nothing else.

     THE CAP IS NAMED, NOT HIDDEN.  The chain can reach state t after t steps, so
     an untruncated vector grows without bound.  The state space is capped and the
     weight that would leave the top stays at the top, which makes this the exact
     transient of the CAPPED chain; `capNum` over `dens` is the probability
     sitting on the cap, and every page that draws this curve prints it, because a
     truncation a reader cannot see is a truncation they cannot discount. */
  var SIM_TRANSIENT_SCALE = 1000000n;

  function simTransient(p, q, T, cap) {
    var d = p.d * q.d / bgcd(p.d, q.d);
    var a = p.n * (d / p.d), b = q.n * (d / q.d), D = d * d;
    var nu = [1n], den = 1n, nums = [], dens = [], values = [], capNum = [], t, i;
    for (t = 0; t <= T; t += 1) {
      var sum = 0n;
      for (i = 0; i < nu.length; i += 1) sum += BigInt(i) * nu[i];
      nums.push(sum); dens.push(den);
      values.push(Number((sum * SIM_TRANSIENT_SCALE) / den) / Number(SIM_TRANSIENT_SCALE));
      capNum.push(nu.length > cap ? nu[cap] : 0n);
      if (t === T) break;
      var len = Math.min(nu.length + 1, cap + 1), next = new Array(len).fill(0n);
      for (i = 0; i < nu.length; i += 1) {
        var wt = nu[i];
        if (wt === 0n) continue;
        if (i === 0) {
          next[0] += wt * (d - a) * d;
          if (1 < len) next[1] += wt * a * d; else next[0] += wt * a * d;
        } else {
          next[i - 1] += wt * b * (d - a);
          next[i] += wt * (b * a + (d - b) * (d - a));
          if (i + 1 < len) next[i + 1] += wt * (d - b) * a; else next[i] += wt * (d - b) * a;
        }
      }
      nu = next; den *= D;
    }
    return { nums: nums, dens: dens, values: values, capNum: capNum, cap: cap, D: D, T: T };
  }
  /* E[N_t] as a fraction.  Reduced -- which costs a gcd -- because this is the
     form a reader reads, and it is only ever asked for at the small t where the
     fraction is short enough to read.  Past that, `simTransientRaw` hands back the
     same number unreduced, which Rfixed long-divides without caring. */
  function simTransientExact(tr, t) { return R(tr.nums[t], tr.dens[t]); }
  function simTransientRaw(tr, t) { return { n: tr.nums[t], d: tr.dens[t] }; }
  function simTransientCapMass(tr, t) { return { n: tr.capNum[t], d: tr.dens[t] }; }

  /* The EXPECTED time-average over a window of slots: the average of the exact
     E[N_t] over the window, which is the number a run of that window is an
     estimate of.  The bias a warm-up removes is the gap between this over
     [0, T) and the stationary mean, and it is theory rather than noise.

     Summed in the integers.  The terms have denominators D^from up to D^(to-1),
     so scaling each by the power of D that is missing puts them all over the
     largest one, and the whole sum is then a single fraction -- one gcd for a
     four-hundred-term exact average, against four hundred of them. */
  function simExpectedAverage(tr, from, to) {
    if (to <= from || to > tr.nums.length) return null;
    var acc = 0n, f = 1n, Db = BigInt(tr.D), t;
    for (t = to - 1; t >= from; t -= 1) { acc += tr.nums[t] * f; f *= Db; }
    return R(acc, tr.dens[to - 1] * BigInt(to - from));
  }
"""


SIMBINOM_JS = r"""
  /* The rare event, as an exact table.

     Ten fair coins all landing heads is a probability of 1/1024: near enough to
     one in a thousand to be the case importance sampling exists for, and known
     exactly, which is what makes the variance comparison a measurement.  The
     distribution of the number of heads under a coin with P(head) = theta is a
     binomial table, exact for rational theta, and the likelihood ratio p/q is a
     ratio of two of its entries.

     The binomial coefficient is computed by the multiply-then-divide recurrence
     in BigInt: C(n, k) = C(n, k-1) (n - k + 1)/k is an integer at every step, so
     nothing rounds and nothing overflows. */
  function simBinomCoeff(n, k) {
    var r = 1n, i;
    for (i = 0; i < k; i += 1) r = r * BigInt(n - i) / BigInt(i + 1);
    return r;
  }
  function simBinomPmf(n, theta) {
    var out = [], k, one = Rsub(R1, theta);
    for (k = 0; k <= n; k += 1) {
      out.push([R(BigInt(k), 1n),
                Rmul(R(simBinomCoeff(n, k), 1n), Rmul(Rpow(theta, k), Rpow(one, n - k)))]);
    }
    return out;
  }
  /* A q with a HOLE, for the refusal.  The mass at the target is deleted and the
     rest renormalised, so q is a perfectly good distribution that simply never
     produces the outcome p cares about -- which is the one case importanceRun
     will not answer, because an estimator that skips the outcome is biased in a
     way no variance figure reveals. */
  function simHoledPmf(pairs, at) {
    var kept = [], i;
    for (i = 0; i < pairs.length; i += 1) {
      kept.push([pairs[i][0], Rcmp(pairs[i][0], at) === 0 ? R0 : pairs[i][1]]);
    }
    return pmfNormalise(kept);
  }
  /* One RUN under q: each draw's weight, the running weighted estimate, and the
     count of draws that hit the event.  The estimate is exact -- a sum of
     rational weights over an integer count -- and the point of running it is
     that a bad q's estimate wanders near the right answer for a long time while
     all the damage sits in the spread. */
  function simImportanceRun(p, q, at, seed, count) {
    var draws = simDraws(q, seed, count), rows = [], sum = R0, hits = 0, i;
    var pw = {}, qw = {};
    for (i = 0; i < p.length; i += 1) pw[Rtext(p[i][0])] = p[i][1];
    for (i = 0; i < q.length; i += 1) qw[Rtext(q[i][0])] = q[i][1];
    for (i = 0; i < draws.length; i += 1) {
      var key = Rtext(draws[i]), qi = qw[key], pi = pw[key];
      var w = (qi === undefined || Rzero(qi)) ? R0 : Rdiv(pi, qi);
      var hit = Rcmp(draws[i], at) === 0;
      if (hit) { hits += 1; sum = Radd(sum, w); }
      rows.push({ draw: draws[i], w: w, hit: hit });
      if (i < draws.length) rows[i].running = Rdiv(sum, R(BigInt(i + 1), 1n));
    }
    return { rows: rows, hits: hits, estimate: Rdiv(sum, R(BigInt(count), 1n)), draws: draws };
  }
"""


# ---------------------------------------------------------------------------
# WHICH BLOCKS EACH MODE SHIPS, and why that is a table rather than a constant.
#
# or_core.py's header says a kit "concatenates only the blocks it needs, and
# that is the single biggest lever on page weight". Nine lessons are nine
# SEPARATE PAGES and they do not need the same blocks: only `sample` certifies a
# generator's period, so only `sample` carries number theory; only the four
# queue modes need the trace and the exact slotted chain; only `importance`
# needs a pmf convolution's module; and only the three modes that print a
# standard error or a correlation need surds.
#
# THE RULE FOR EDITING THIS TABLE: a block belongs in a mode's list when that
# mode CALLS something in it. Every block is top-level function declarations
# only, so a function present but never called costs bytes and nothing else --
# and a function called but absent throws on the first redraw, which
# scripts/labcheck.js catches on every published page.
# ---------------------------------------------------------------------------

_BASE = RATIONAL_JS + ORFMT_JS + SIMBASE_JS + SIM_JS   # everything prints, escapes and draws
_QUEUE = TRACE_JS + SLOTTED_JS + SIMQ_JS               # the slotted run and its exact mean

_MODE_JS = {
    # the generator itself, its period certificate, and the staircase
    "sample": RATIONAL_JS + ORFMT_JS + SIMBASE_JS + SIM_JS + STREAM_JS + NT_JS + SIMSTAIR_JS,
    # the running mean, the exact variance, and the root that rounds
    "montecarlo": _BASE + STREAM_JS + SURD_JS + SIMSURD_JS + SIMDRAW_JS,
    # k, the guarantee, and the coverage counted by comparing squares
    "bound": _BASE + STREAM_JS + SURD_JS + SIMSURD_JS + SIMDRAW_JS,
    # the calendar, one event at a time, against the exact mean
    "des": _BASE + STREAM_JS + _QUEUE + SIMDRAW_JS,
    # the transient as theory, the bias it causes, and batch means
    "warmup": _BASE + STREAM_JS + _QUEUE + SIMCHAIN_JS + SIMDRAW_JS,
    # two configurations, one stream or two, and Var(A - B)
    "crn": _BASE + STREAM_JS + _QUEUE + SIMDRAW_JS,
    # U against 1 - U, in the best case and the worst one
    "antithetic": _BASE + STREAM_JS + SIMDRAW_JS,
    # the quadratic in b, its vertex, and 1 - rho^2
    "control": _BASE + STREAM_JS + _QUEUE + SURD_JS + SIMSURD_JS + SIMDRAW_JS,
    # p, q, the weights, and the two variances
    "importance": _BASE + STREAM_JS + PMF_JS + SIMBINOM_JS + SIMDRAW_JS,
}


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the library uses, so a reader
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
        '          <input id="%s" type="text" value="%s" inputmode="numeric" autocomplete="off">\n'
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


def _preset(cfg, mode, table, default):
    """The preset this lesson opens on, or a refusal.

    A preset that fell back to a default would render the WRONG worked example
    under the right lesson's prose -- the panel's numbers would not be the
    prose's numbers -- and nothing in the suite would notice, because the lab
    builds and draws. So an unknown one raises, the same way an unknown mode
    does. Every lesson opens on its own worked example by naming it here.
    """
    name = cfg.get("preset", default)
    if name not in table:
        raise ValueError(
            "simulate_lab: mode %r has no preset %r; its presets are %s"
            % (mode, name, ", ".join(sorted(table)))
        )
    return name, table[name]


def _js(name, value):
    """A preset table as a JS literal, so the page carries the data the panel
    describes rather than a transcription of it."""
    return "  var %s = %s;\n" % (name, json.dumps(value).replace("</", "<\\/"))


# The distribution five of the nine modes sample: outcomes 0 to 4 with
# probabilities 1, 4, 6, 4, 1 over 16. Its mean is exactly 2 and its variance is
# exactly 1, which is why the theoretical standard errors at 100, 400 and 1600
# draws are exactly 1/10, 1/20 and 1/40 and the halving is a fact rather than an
# approximation. Written as [value, [numerator, denominator]] so the rational
# survives the trip through JSON as integers.
_PMFS = {
    "binomial16": ("outcomes 0 to 4 with probabilities 1, 4, 6, 4, 1 over 16 — mean exactly 2, "
                   "variance exactly 1",
                   [[0, [1, 16]], [1, [4, 16]], [2, [6, 16]], [3, [4, 16]], [4, [1, 16]]]),
    "skewed": ("a skewed table — 0 with probability 1/2 and the rest falling away, so the mean "
               "sits well below the middle outcome",
               [[0, [1, 2]], [1, [1, 4]], [2, [1, 8]], [3, [1, 16]], [4, [1, 16]]]),
    "uniform5": ("five equally likely outcomes — the one table for which the shortcut a reader "
                 "reaches for is not wrong",
                 [[0, [1, 5]], [1, [1, 5]], [2, [1, 5]], [3, [1, 5]], [4, [1, 5]]]),
}

_PMF_JS_LITERAL = _js("PMFS", {k: v[1] for k, v in _PMFS.items()})

# Turning that literal into rationals, once, in the one place it happens.
_PMF_READ_JS = r"""
  /* A preset is integers -- numerator and denominator -- so a probability of
     6/16 survives JSON as two integers rather than as 0.375, and nothing
     downstream ever sees a float where it expects a fraction. */
  function pmfOf(name) {
    return PMFS[name].map(function (row) { return [R(BigInt(row[0]), 1n), R(BigInt(row[1][0]), BigInt(row[1][1]))]; });
  }
"""


# ---------------------------------------------------------------------------
# sample -- the generator, and the cumulative table as the sampler
# ---------------------------------------------------------------------------

# Four parameter sets, and the fourth is the one that fails. A reader who has
# only ever seen a generator that works cannot tell the certificate from
# decoration, so one choice here has a period of four out of a modulus of
# sixteen and the page says which condition it broke.
_GENERATORS = {
    "turbo": ("25173", "13849", "65536",
              "full period 65536: c is odd and a − 1 = 25172 is divisible by 4"),
    "minstd": ("16807", "0", "2147483647",
               "the multiplicative generator every other page of this course draws from"),
    "tiny": ("5", "3", "16",
             "small enough to walk the whole period by hand, which is where this generator was first met"),
    "broken": ("2", "4", "16",
               "a generator that fails the conditions: its stream collapses onto a handful of values"),
}


def _sample(cfg):
    name, (label, spec) = _preset(cfg, "sample", _PMFS, "binomial16")
    gen = cfg.get("generator", "turbo")
    if gen not in _GENERATORS:
        raise ValueError(
            "simulate_lab: mode 'sample' has no generator %r; they are %s"
            % (gen, ", ".join(sorted(_GENERATORS)))
        )
    a, c, m, _why = _GENERATORS[gen]

    markup = (
        _toolbar(
            "The cumulative table is the sampler",
            "one integer per draw, turned into U = x/m, matched against F",
            [("cyan", "the first outcome's band"), ("green", "the second"),
             ("amber", "the third"), ("purple", "the fourth"),
             ("muted", "each draw, landing")],
        )
        + _stage(_svg("smStair", "0 0 660 240",
                      "The cumulative probability bands, with every shown draw's U marked in the band it fell in."))
        + _table("smDrawTable")
        + _table("smFreqTable")
        + _banner("smStatus")
    )
    controls = (
        _select("smPmf", "Distribution",
                [("binomial16", "1, 4, 6, 4, 1 over 16"),
                 ("skewed", "skewed, half the mass on the first outcome"),
                 ("uniform5", "five equally likely outcomes")], name)
        + _select("smGen", "Generator",
                  [("turbo", "a = 25173, c = 13849, m = 65536"),
                   ("minstd", "a = 16807, c = 0, m = 2147483647"),
                   ("tiny", "a = 5, c = 3, m = 16"),
                   ("broken", "a = 2, c = 4, m = 16")], gen)
        + _text("smA", "Multiplier a", a)
        + _text("smC", "Increment c", c)
        + _text("smM", "Modulus m", m)
        + _range("smSeed", "Seed", 0, 40, 1)
        + _range("smDraws", "Draws", 20, 400, 200, 20)
        + _kpis([
            ("The first U", "smFirstU"),
            ("Sample mean", "smMean"),
            ("True mean", "smTrue"),
            ("Period", "smPeriod"),
            ("Largest gap", "smGap"),
            ("Hull–Dobell", "smHD"),
        ])
        + _hint("smHint",
                "Every figure here is exact. U is the fraction x/m, the sampled value is the first "
                "one whose cumulative probability reaches U, and an empirical frequency is a count "
                "over the number of draws — so the run is reproducible from its seed and there is "
                "nothing in the sampler but the table.")
    )

    script = _MODE_JS["sample"] + _PMF_JS_LITERAL + _js("GENS", _GENERATORS) + _PMF_READ_JS + r"""
  var pmfSel = document.getElementById('smPmf'), genSel = document.getElementById('smGen');
  var aIn = document.getElementById('smA'), cIn = document.getElementById('smC'), mIn = document.getElementById('smM');
  var seedS = document.getElementById('smSeed'), drawsS = document.getElementById('smDraws');
  var stair = document.getElementById('smStair'), drawTable = document.getElementById('smDrawTable');
  var freqTable = document.getElementById('smFreqTable'), status = document.getElementById('smStatus');
  var lastGen = genSel.value;

  /* The walk is capped, and the cap is the honest reason: detecting a period by
     storing every value seen costs one entry per value, and a modulus of two
     thousand million has two thousand million of them. Below the cap the period
     is MEASURED; above it, the certificate is all there is, which is exactly why
     the theorem is worth having. */
  var WALK = 70000;

  function redraw() {
    if (genSel.value !== lastGen) {
      lastGen = genSel.value;
      aIn.value = GENS[lastGen][0]; cIn.value = GENS[lastGen][1]; mIn.value = GENS[lastGen][2];
    }
    var pmf = pmfOf(pmfSel.value), cum = simCumulative(pmf);
    var seed = +seedS.value, n = +drawsS.value;
    document.getElementById('smSeedOut').textContent = seed;
    document.getElementById('smDrawsOut').textContent = n;

    var A = simReadInt(aIn.value, 1, 2147483647);
    var C = simReadInt(cIn.value, 0, 2147483647);
    var M = simReadInt(mIn.value, 4, 2147483647);
    if (A === null || C === null || M === null) {
      stair.innerHTML = simLabel(20, 40, 'the generator needs three whole numbers', 'red');
      drawTable.innerHTML = ''; freqTable.innerHTML = '';
      status.innerHTML = 'a, c and m must be whole numbers with 4 &lt;= m &lt;= 2147483647, '
        + 'a at least 1 and c at least 0. Nothing is drawn from a generator that does not exist.';
      return;
    }

    var xs = lcgStream(Number(A), Number(C), Number(M), seed, n);
    var us = streamUniform(Number(A), Number(C), Number(M), seed, n);
    var draws = us.map(function (u) { return sampleFromPmf(pmf, u); });
    var freqs = simFrequencies(pmf, draws);
    var mean = sampleMean(draws), trueMean = simPmfMean(pmf);

    var shown = Math.min(n, 36);
    stair.innerHTML = simStaircase(cum, us.slice(0, shown), { width: 660, height: 240 }).svg;

    var rows = '', i, j;
    for (i = 0; i < Math.min(n, 10); i += 1) {
      var band = 0;
      for (j = 0; j < cum.length; j += 1) if (Rcmp(us[i], cum[j].hi) < 0) { band = j; break; }
      rows += simTr([simTd(String(i + 1)), simTd(String(xs[i])), simTd(Rtext(us[i])),
                     simTd(Rtext(cum[band].lo) + ' to ' + Rtext(cum[band].hi)),
                     simTd('<strong>' + Rtext(draws[i]) + '</strong>')]);
    }
    drawTable.innerHTML = '<caption>The first draws, one row each: the integer, the fraction it becomes, '
      + 'the band it lands in, the value that band carries.</caption>'
      + simHead(['draw', 'x', 'U = x/m', 'the band U fell in', 'sampled value'])
      + '<tbody>' + rows + '</tbody>';

    var frows = '', gap = null, gapAt = null;
    for (i = 0; i < freqs.length; i += 1) {
      var f = freqs[i], diff = Rsub(f.empirical, f.p), mag = Rabs(diff);
      if (gap === null || Rcmp(mag, gap) > 0) { gap = mag; gapAt = f.value; }
      frows += simTr([simTd(Rtext(f.value)), simTd(String(f.count)),
                      simTd('<strong>' + Rtext(f.empirical) + '</strong>'),
                      simTd(Rtext(f.p)), simTd(Rtext(f.expected)),
                      simTd((Rsign(diff) > 0 ? '+' : '') + Rtext(diff))]);
    }
    freqTable.innerHTML = '<caption>Empirical against theoretical, both as exact fractions.</caption>'
      + simHead(['value', 'count', 'count / draws', 'probability', 'expected count', 'difference'])
      + '<tbody>' + frows + '</tbody>';

    var hd = hullDobell(A, C, M);
    var primes = factorize(M).map(function (pe) { return pe[0]; });
    var walked = M <= BigInt(WALK)
      ? lcgRun(A, C, M, BigInt(seed), WALK + 1)
      : null;
    document.getElementById('smFirstU').textContent = Rtext(us[0]);
    document.getElementById('smMean').textContent = Rtext(mean);
    document.getElementById('smTrue').textContent = Rtext(trueMean);
    document.getElementById('smPeriod').textContent = walked
      ? (walked.period < 0 ? 'longer than ' + WALK : String(walked.period))
      : 'not walked at this m';
    document.getElementById('smGap').textContent = Rtext(gap) + ' at ' + Rtext(gapAt);
    document.getElementById('smHD').textContent = (hd[0] ? 1 : 0) + (hd[1] ? 1 : 0) + (hd[2] ? 1 : 0) + ' of 3';

    var conds = 'gcd(c, m) = gcd(' + C + ', ' + M + ') = ' + bgcd(C, M) + ' ' + simTick(hd[0])
      + ' &middot; a &minus; 1 = ' + (A - 1n) + ' divisible by every prime of m ('
      + primes.join(', ') + ') ' + simTick(hd[1])
      + ' &middot; ' + (M % 4n === 0n ? '4 divides m, so 4 must divide a &minus; 1' : '4 does not divide m, so the third condition is vacuous')
      + ' ' + simTick(hd[2]);

    var verdict;
    if (C === 0n) {
      verdict = 'With c = 0 the theorem does not apply and cannot: zero is a fixed point of '
        + 'x &rarr; ax mod m, so the period can never reach m and the best available is m &minus; 1 = '
        + (M - 1n) + ', which a primitive root attains. That is why this multiplier and this prime '
        + 'modulus are what every other page of this course draws from — and why the condition on '
        + 'gcd(c, m) reads as a failure here rather than as a defect.';
    } else if (hd[0] && hd[1] && hd[2]) {
      verdict = 'All three conditions hold, so the period is the full ' + M
        + (walked ? ' — and the walk above confirms it: ' + walked.period + ' values before the stream returns to its start.' : '.')
        + ' Full period is not the same as good: this generator visits every residue exactly once and '
        + 'is still unfit for anything but a lesson, which is the warning that came with it.';
    } else {
      verdict = 'The conditions do not all hold, so the period is short of ' + M
        + (walked ? ': the walk finds ' + walked.period + ' distinct values'
                    + (walked.start > 0 ? ' after a tail of ' + walked.start + ' the cycle never revisits' : '')
                    + '.' : '.')
        + ' A sampler fed a stream this short does not sample the table at all — it repeats a fixed '
        + 'cycle of outcomes, and the frequency column above is a count of that cycle.';
    }

    status.innerHTML = 'Hull&ndash;Dobell on a = ' + A + ', c = ' + C + ', m = ' + M + ': ' + conds
      + '<br />' + verdict
      + '<br />The sample mean over ' + n + ' draws is <strong>' + Rtext(mean) + '</strong> against a true mean of '
      + Rtext(trueMean) + ', and the largest gap between an empirical frequency and its probability is '
      + Rtext(gap) + ', at the value ' + Rtext(gapAt) + '. Neither is noise to be apologised for: they are '
      + 'what a finite sample of this table looks like, and how far they can be from the truth is the next '
      + 'thing this course computes.'
      + '<br />The shortcut to avoid: floor(k &middot; U) + 1 samples the UNIFORM distribution on k values, '
      + 'whatever table is on the page. It ignores the probability column entirely, so unequal '
      + 'probabilities come out flattened and the run still looks random.';
  }

  [pmfSel, genSel].forEach(function (el) { el.addEventListener('change', redraw); });
  [aIn, cIn, mIn].forEach(function (el) { el.addEventListener('input', redraw); });
  [seedS, drawsS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Inverse-transform sampling, exactly",
        subtitle="An integer becomes a fraction, and the cumulative table decides which value it is",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Step the stream, and watch each draw land in its band"),
        panel_intro=cfg.get(
            "panel_intro",
            "The generator produces integers; U = x/m turns one into a fraction in [0, 1); and the "
            "sampled value is the first one whose cumulative probability reaches U. Both sides are "
            "rational, so the whole run is exact and reproducible from its seed. On this table: "
            + label + ". The Hull–Dobell conditions are checked for whatever parameters you set, "
            "because a sampler is only as good as the period underneath it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# montecarlo -- the running mean, the exact variance, and the root that rounds
# ---------------------------------------------------------------------------

# The three sample sizes the lesson quadruples through. They are a constant
# rather than a slider position because the claim being checked is about the
# RATIO of two standard errors, and a ratio needs both ends named.
_MC_STEPS = (100, 400, 1600)


def _montecarlo(cfg):
    name, (label, spec) = _preset(cfg, "montecarlo", _PMFS, "binomial16")

    markup = (
        _toolbar(
            "Four times the runs for twice the precision",
            "the running mean against the exact expectation, inside a ribbon that narrows like one over root n",
            [("cyan", "the running mean"), ("green", "the exact expectation"),
             ("amber", "plus or minus one standard error"), ("purple", "the three sample sizes")],
        )
        + _stage(_svg("mcTrace", "0 0 660 250",
                      "The running sample mean against the exact expectation, with a standard-error ribbon narrowing as the number of draws grows."))
        + _table("mcTable")
        + _banner("mcStatus")
    )
    controls = (
        _select("mcPmf", "Distribution",
                [("binomial16", "1, 4, 6, 4, 1 over 16"),
                 ("skewed", "skewed, half the mass on the first outcome"),
                 ("uniform5", "five equally likely outcomes")], name)
        + _range("mcSeed", "Seed", 0, 40, 1)
        + _range("mcN", "Draws in the trace", 100, 1600, 400, 100)
        + _kpis([
            ("Sample mean", "mcMean"),
            ("Exact expectation", "mcTrue"),
            ("Sample variance", "mcVar"),
            ("Standard error", "mcSE"),
            ("Exact variance", "mcTrueVar"),
            ("Runs for half the width", "mcCost"),
        ])
        + _hint("mcHint",
                "The sample mean and the sample variance are exact fractions. The standard error is "
                "the one square root on this page: it is printed in exact surd form and then as a "
                "decimal, and the decimal is the only rounded number here.")
    )

    script = _MODE_JS["montecarlo"] + _PMF_JS_LITERAL + _PMF_READ_JS + _js("STEPS", list(_MC_STEPS)) + r"""
  var pmfSel = document.getElementById('mcPmf'), seedS = document.getElementById('mcSeed');
  var nS = document.getElementById('mcN');
  var svg = document.getElementById('mcTrace'), table = document.getElementById('mcTable');
  var status = document.getElementById('mcStatus');

  function redraw() {
    var pmf = pmfOf(pmfSel.value), seed = +seedS.value, n = +nS.value;
    document.getElementById('mcSeedOut').textContent = seed;
    document.getElementById('mcNOut').textContent = n;

    var biggest = Math.max(n, STEPS[STEPS.length - 1]);
    var draws = simDraws(pmf, seed, biggest);
    var trace = simRunningMean(draws.slice(0, n));
    var mu = simPmfMean(pmf), sigma2 = simPmfVar(pmf);
    var mean = sampleMean(draws.slice(0, n)), variance = sampleVar(draws.slice(0, n));
    var se = simStandardError(variance, n);

    /* PIXELS MAY ROUND; NOTHING REPORTED MAY. The ribbon's edge at draw i is
       mu +- sqrt(sigma^2 / i), and a y coordinate is a pixel, so the root is
       taken in floating point here and nowhere else on the page. */
    var muPx = simPx(mu), sdPx = Math.sqrt(simPx(sigma2));
    var pts = [], band = [], i, every = Math.max(1, Math.floor(n / 220));
    for (i = 0; i < trace.length; i += 1) {
      if (i % every !== 0 && i !== trace.length - 1) continue;
      pts.push([i + 1, simPx(trace[i])]);
      band.push([i + 1, muPx - sdPx / Math.sqrt(i + 1), muPx + sdPx / Math.sqrt(i + 1)]);
    }
    var marks = [];
    for (i = 0; i < STEPS.length; i += 1) {
      if (STEPS[i] <= trace.length) marks.push({ x: STEPS[i], y: simPx(trace[STEPS[i] - 1]), tone: 'purple',
                                                 label: String(STEPS[i]) });
    }
    svg.innerHTML = simPlot({
      width: 660, height: 250, series: [{ pts: pts, tone: 'cyan', thin: true }],
      bands: [{ pts: band, tone: 'amber', opacity: '0.18' }],
      rules: [{ y: muPx, tone: 'green', solid: true, label: 'exact ' + Rtext(mu) }],
      marks: marks, xLabel: 'draws', x0: 1, x1: trace.length
    }).svg;

    var rows = '', prevSe = null, prevN = null;
    for (i = 0; i < STEPS.length; i += 1) {
      var k = STEPS[i], sub = draws.slice(0, k);
      var mk = sampleMean(sub), vk = sampleVar(sub), sk = simStandardError(vk, k);
      var theory = simStandardError(sigma2, k);
      /* THE RATIO IS EXACT EVEN THOUGH NEITHER END IS. Squaring removes both
         roots: (sigma^2/n) / (sigma^2/4n) = 4, so the ratio is 2 whatever sigma
         is, and the halving is a fact rather than a measurement. */
      var ratio = prevSe === null ? null : Rsurd(Rdiv(Rdiv(sigma2, R(BigInt(prevN), 1n)), Rdiv(sigma2, R(BigInt(k), 1n))));
      rows += simTr([simTd(String(k)), simTd(Rtext(mk)), simTd(simNum(vk, 6)),
                     simTd(simSurd(sk, 5)), simTd(simSurd(theory, 5)),
                     simTd(ratio === null ? 'the first row' : Rtext(ratio.q) + (ratio.k === 1n ? '' : 'sqrt(' + ratio.k + ')'))],
                    k === n ? 'focus' : null);
      prevSe = sk; prevN = k;
    }
    table.innerHTML = '<caption>The same stream read at three lengths. The last column is the ratio of the '
      + 'theoretical standard error at the row above to this row: it squares to an integer, so it is exact.</caption>'
      + simHead(['draws', 'sample mean', 'sample variance', 'sample standard error', 'exact sigma / root n',
                 'previous SE / this SE'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('mcMean').textContent = Rtext(mean);
    document.getElementById('mcTrue').textContent = Rtext(mu);
    document.getElementById('mcVar').textContent = simNum(variance, 6);
    document.getElementById('mcSE').innerHTML = simSurd(se, 5);
    document.getElementById('mcTrueVar').textContent = Rtext(sigma2);
    document.getElementById('mcCost').textContent = 4 * n + ' draws';

    var err = Rabs(Rsub(mean, mu));
    status.innerHTML = 'Over ' + n + ' draws the sample mean is <strong>' + Rtext(mean)
      + '</strong> and the exact expectation is <strong>' + Rtext(mu) + '</strong>, so this run is '
      + Rtext(err) + ' out. The sample variance is ' + simNum(variance, 6)
      + ' exactly, and the standard error is ' + simSurd(se, 5)
      + ' — a square root, printed in exact form and then rounded, which is the one rounding on this page.'
      + '<br />The standard error falls like one over the square root of the number of draws, so halving it '
      + 'takes four times the runs: from ' + n + ' that is ' + (4 * n)
      + '. The table checks the claim rather than asserting it — the ratio column squares to an exact 4 at '
      + 'every step, and 4 is a whole number even where the two standard errors either side of it are not.'
      + '<br />Two things this does not say. More draws do not converge TO the exact answer; they shrink the '
      + 'spread of a random quantity, which is a different promise, and a single long run can still land '
      + 'further out than a short one. And a running mean that has stopped moving has not converged — a '
      + 'settled-looking trace is exactly what a small sample of a slow process produces, which is why the '
      + 'interval and not the picture is the evidence.'
      + '<br />The same one-over-root-n fact turns up when a quantity is measured rather than simulated: a '
      + 'thousand requests cannot tell a success ratio of 99.9% from 99.8%, for precisely the reason four '
      + 'times the runs buy twice the precision here.';
  }

  pmfSel.addEventListener('change', redraw);
  [seedS, nS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Monte Carlo and the standard error",
        subtitle="The sample mean has variance σ²/n, so its error falls like one over root n and not faster",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Estimate the expectation, then say how wrong the estimate could be"),
        panel_intro=cfg.get(
            "panel_intro",
            "The draws come from the same seeded stream and the same cumulative table as before, so "
            "the sample mean and the sample variance are exact fractions. On this table: " + label
            + ". The standard error is the square root of the sample variance over the number of "
            "draws: it is carried in exact surd form and rounded once, for printing, with the "
            "rounding named.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# bound -- what an interval GUARANTEES, as against what it is assumed to
# ---------------------------------------------------------------------------


def _bound(cfg):
    name, (label, spec) = _preset(cfg, "bound", _PMFS, "binomial16")

    markup = (
        _toolbar(
            "A guarantee, not an estimate of the error",
            "each replication's mean against a band of k standard errors, and the coverage counted",
            [("cyan", "a replication that covered the mean"), ("red", "one that did not"),
             ("green", "the exact mean"), ("amber", "the band, plus and minus k standard errors")],
        )
        + _stage(_svg("bdSpread", "0 0 660 250",
                      "Every replication's sample mean, with the band of k standard errors around the exact mean drawn across it."))
        + _table("bdTable")
        + _banner("bdStatus")
    )
    controls = (
        _select("bdPmf", "Distribution",
                [("binomial16", "1, 4, 6, 4, 1 over 16"),
                 ("skewed", "skewed, half the mass on the first outcome"),
                 ("uniform5", "five equally likely outcomes")], name)
        + _range("bdK", "k, in standard errors", 1, 6, 5)
        + _range("bdReps", "Replications", 10, 80, 40, 5)
        + _range("bdN", "Draws per replication", 25, 400, 100, 25)
        + _range("bdSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Guaranteed coverage", "bdBound"),
            ("Coverage seen", "bdSeen"),
            ("Half-width, k · SE", "bdHalf"),
            ("Outside the band", "bdOut"),
            ("Width against ±2 SE", "bdRatio"),
            ("Runs to match that width", "bdCost"),
        ])
        + _hint("bdHint",
                "The coverage count is exact because nothing is rooted: a replication is outside the "
                "band when the squared distance from the mean reaches k² times the variance, and both "
                "sides of that comparison are fractions.")
    )

    script = _MODE_JS["bound"] + _PMF_JS_LITERAL + _PMF_READ_JS + r"""
  var pmfSel = document.getElementById('bdPmf'), kS = document.getElementById('bdK');
  var repsS = document.getElementById('bdReps'), nS = document.getElementById('bdN');
  var seedS = document.getElementById('bdSeed');
  var svg = document.getElementById('bdSpread'), table = document.getElementById('bdTable');
  var status = document.getElementById('bdStatus');

  function redraw() {
    var pmf = pmfOf(pmfSel.value), k = +kS.value, reps = +repsS.value, n = +nS.value, seed = +seedS.value;
    document.getElementById('bdKOut').textContent = k;
    document.getElementById('bdRepsOut').textContent = reps;
    document.getElementById('bdNOut').textContent = n;
    document.getElementById('bdSeedOut').textContent = seed;

    var mu = simPmfMean(pmf), sigma2 = simPmfVar(pmf);
    /* The variance OF A REPLICATION MEAN is sigma^2/n, and sigma^2 here is the
       exact variance of the table rather than a sample estimate of it -- which is
       what makes this a coverage count against a known truth and not two
       estimates chasing each other. */
    var varMean = Rdiv(sigma2, R(BigInt(n), 1n));
    var means = [], j;
    for (j = 0; j < reps; j += 1) means.push(sampleMean(simDraws(pmf, seed + 1000 * (j + 1), n)));

    var K = R(BigInt(k), 1n);
    var cover = chebyshevCover(means, mu, K, varMean);
    var half = Rsurd(Rmul(Rmul(K, K), varMean));          /* k SE = sqrt(k^2 sigma^2 / n) */
    var folklore = Rsurd(Rmul(R(4n, 1n), varMean));
    var widthRatio = R(BigInt(k), 2n);
    var runCost = Rmul(widthRatio, widthRatio);

    var halfPx = Math.sqrt(simPx(Rmul(Rmul(K, K), varMean)));
    var marks = [];
    for (j = 0; j < means.length; j += 1) {
      marks.push({ x: j + 1, y: simPx(means[j]), tone: cover.rows[j].outside ? 'red' : 'cyan', r: 3.4 });
    }
    svg.innerHTML = simPlot({
      width: 660, height: 250, marks: marks,
      rules: [{ y: simPx(mu), tone: 'green', solid: true, label: 'exact ' + Rtext(mu) },
              { y: simPx(mu) + halfPx, tone: 'amber', label: 'plus k SE' },
              { y: simPx(mu) - halfPx, tone: 'amber', label: 'minus k SE' }],
      xLabel: 'replication', x0: 0, x1: means.length + 1
    }).svg;

    var rows = '', shown = Math.min(reps, 12);
    for (j = 0; j < shown; j += 1) {
      var row = cover.rows[j];
      rows += simTr([simTd(String(j + 1)), simTd(Rtext(row.value)),
                     simTd(simNum(row.squared, 6)), simTd(simNum(cover.threshold, 6)),
                     simTd(row.outside ? simChip('outside', 'no') : simChip('covered', 'ok'))],
                    row.outside ? 'focus' : null);
    }
    table.innerHTML = '<caption>The first replications. A replication is outside the band when the squared '
      + 'distance reaches k² times the variance of a mean — squares on both sides, so no root is taken and '
      + 'the count is exact.</caption>'
      + simHead(['replication', 'sample mean', '(mean − μ)²', 'k² · σ²/n', 'verdict'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('bdBound').textContent = Rtext(cover.bound) + ' = ' + Rpct(cover.bound, 0);
    /* A coverage of 40 out of 40 reduces to the fraction "1", which a reader
       reads as ONE replication. The count is what was counted; the fraction is
       what it means, and both are printed. */
    document.getElementById('bdSeen').textContent =
      (reps - cover.outside) + ' of ' + reps + ' = ' + Rpct(cover.coverage, 1);
    document.getElementById('bdHalf').innerHTML = simSurd(half, 5);
    document.getElementById('bdOut').textContent = cover.outside + ' of ' + reps;
    document.getElementById('bdRatio').textContent = Rtext(widthRatio) + ' times';
    document.getElementById('bdCost').textContent = Rtext(runCost) + ' times';

    status.innerHTML = 'At k = ' + k + ' Chebyshev guarantees coverage 1 − 1/' + (k * k) + ' = <strong>'
      + Rtext(cover.bound) + '</strong> = ' + Rpct(cover.bound, 0)
      + ', for every distribution with a finite variance and with no assumption to be wrong about. '
      + 'Over ' + reps + ' replications of ' + n + ' draws the band actually covered <strong>'
      + (reps - cover.outside) + ' of ' + reps + '</strong> — a fraction of ' + Rtext(cover.coverage)
      + ', with ' + cover.outside + ' outside. '
      + (cover.holds ? 'The guarantee held, as it must: '
                     : 'That is below the guarantee, which can happen to a finite count of replications and is '
                       + 'reported rather than hidden: ')
      + 'the bound is a worst case over all distributions, and the actual error is almost always far smaller. '
      + 'Read it as a promise about how bad things can get, never as an estimate of how bad they are.'
      + '<br />The width it costs. The folklore interval is plus or minus 2 standard errors, and under '
      + 'Chebyshev k = 2 guarantees 1 − 1/4 = <strong>3/4</strong> and nothing more; the 95% attached to it '
      + 'comes from a normal approximation this path has not built and does not assume. Against that '
      + 'folklore width, the band at k = ' + k + ' is <strong>' + Rtext(widthRatio)
      + ' times as wide</strong> — ' + k + ' standard errors rather than 2, half-width ' + simSurd(half, 5)
      + ' against ' + simSurd(folklore, 5) + '. Buying that width back with runs instead of with assumption '
      + 'costs <strong>' + Rtext(runCost) + ' times</strong> the draws, because the width falls like one over '
      + 'the square root of the count and the ratio therefore squares.'
      + '<br />Where the inequality comes from. The discrete-mathematics course states it as a theorem and '
      + 'stops; the two-line proof from Markov\'s inequality is in the algorithms course, in the lesson on '
      + 'turning an expectation into a probability. This page uses the statement and points at the proof '
      + 'rather than repeating either.';
  }

  pmfSel.addEventListener('change', redraw);
  [kS, repsS, nS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="How sure? Chebyshev's bound",
        subtitle="±k SE has guaranteed coverage 1 − 1/k², with nothing assumed and a width that says so",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Drag k, and watch the guarantee and the coverage move apart"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each replication draws its own sample and reports its own mean. The band is ±k standard "
            "errors around the exact mean of the table — on this one: " + label + " — and the "
            "coverage is a count of the replications that fell inside it, printed as an exact "
            "fraction beside the guarantee 1 − 1/k². The gap between the two is the result.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The slotted chain four modes share, as [label, p, q] with p and q as
# [numerator, denominator] so the rational survives JSON as integers. The exact
# mean of each is computed on the page by geoGeo1 -- the SAME function the
# System Design course prints -- so the two subjects cannot disagree about it.
# ---------------------------------------------------------------------------

_CHAINS = {
    "base": ("arrivals with probability 2/5 a slot, service completing with probability 1/2 — "
             "exact mean in system 12/5", [2, 5], [1, 2]),
    "faster": ("the same arrivals against a faster server, q = 3/5 — exact mean 6/5",
               [2, 5], [3, 5]),
    "busier": ("arrivals with probability 1/2 a slot against q = 3/5 — a heavier load and a "
               "slower-mixing queue", [1, 2], [3, 5]),
}

_CHAIN_JS_LITERAL = _js("CHAINS", {k: [v[1], v[2]] for k, v in _CHAINS.items()})

_CHAIN_READ_JS = r"""
  function chainOf(name) {
    var c = CHAINS[name];
    return { p: R(BigInt(c[0][0]), BigInt(c[0][1])), q: R(BigInt(c[1][0]), BigInt(c[1][1])) };
  }
"""


# ---------------------------------------------------------------------------
# des -- the event calendar, which IS the simulation
# ---------------------------------------------------------------------------


def _des(cfg):
    name, (label, pnum, qnum) = _preset(cfg, "des", _CHAINS, "base")

    markup = (
        _toolbar(
            "The clock jumps to the next event",
            "the calendar, the state and the area under the occupancy curve, one event at a time",
            [("cyan", "the number in system"), ("amber", "the clock, at the event shown"),
             ("green", "the exact long-run mean"), ("purple", "the run's time average")],
        )
        + _stage(_svg("dsTrace", "0 0 660 240",
                      "The number in system against the slot index, with the event currently shown marked."))
        + _table("dsLog")
        + _table("dsCal")
        + _banner("dsStatus")
    )
    controls = (
        _select("dsChain", "Configuration",
                [("base", "p = 2/5, q = 1/2"), ("faster", "p = 2/5, q = 3/5"),
                 ("busier", "p = 1/2, q = 3/5")], name)
        + _range("dsEvent", "Event", 1, 24, 6)
        + _range("dsSlots", "Slots in the long run", 200, 4000, 2000, 200)
        + _range("dsSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Clock", "dsClock"),
            ("In system", "dsIn"),
            ("Pending events", "dsPend"),
            ("Time average of the run", "dsL"),
            ("Exact long-run mean", "dsExact"),
            ("Server busy", "dsRho"),
        ])
        + _hint("dsHint",
                "Nothing here steps a slot at a time. The clock moves to the next scheduled event, "
                "the state changes, and new events are scheduled from there — so the calendar is the "
                "simulation, and every row of it is a fraction.")
    )

    script = _MODE_JS["des"] + _CHAIN_JS_LITERAL + _CHAIN_READ_JS + r"""
  var chainSel = document.getElementById('dsChain'), eventS = document.getElementById('dsEvent');
  var slotsS = document.getElementById('dsSlots'), seedS = document.getElementById('dsSeed');
  var svg = document.getElementById('dsTrace'), log = document.getElementById('dsLog');
  var cal = document.getElementById('dsCal'), status = document.getElementById('dsStatus');

  /* Twelve customers is twenty-four events, which is twice the ten the lesson
     asks a reader to keep by hand and still a calendar that fits on a screen. */
  var HEAD = 12;

  function redraw() {
    var ch = chainOf(chainSel.value), slots = +slotsS.value, seed = +seedS.value;
    document.getElementById('dsSlotsOut').textContent = slots;
    document.getElementById('dsSeedOut').textContent = seed;

    var run = simSlotRun(ch.p, ch.q, slots, seed);
    var head = simRunHead(run, HEAD);
    var calendar = simCalendar(head, 24);
    var at = Math.min(+eventS.value, calendar.events.length) - 1;
    document.getElementById('dsEventOut').textContent = (at + 1) + ' of ' + calendar.events.length;

    var here = calendar.events.length ? calendar.events[at] : null;
    var exact = geoGeo1(ch.p, ch.q);
    var little = littleFromTrace(run.arrivals, run.departs);

    /* The trace is drawn over the slots the calendar covers plus a margin, so the
       reader sees the events they are stepping through rather than a two-thousand
       slot smear -- and occupancyTrace costs one pass over the customers per slot
       it is asked for, so asking for thirty rather than four thousand is the
       difference between a page and a stall. The long-run average needs no
       occupancy at all: run.area IS the sum of the per-customer times. */
    var span = Math.max(24, head.departs.length ? head.departs[head.departs.length - 1] + 2 : 24);
    var occ = occupancyTrace(run.arrivals, run.departs, span + 1);
    var pts = [], t;
    for (t = 0; t <= span; t += 1) pts.push([t, occ[t] === undefined ? 0 : occ[t]]);
    svg.innerHTML = simPlot({
      width: 660, height: 240, series: [{ pts: pts, tone: 'cyan', step: true }],
      rules: [{ y: simPx(exact.L), tone: 'green', solid: true, label: 'exact ' + Rtext(exact.L) },
              { y: simPx(run.L), tone: 'purple', label: 'run ' + Rfixed(run.L, 3) }],
      drops: here ? [{ x: simPx(here.t), label: 'clock ' + Rtext(here.t) }] : [],
      xLabel: 'slot', y0: 0, x0: 0, x1: span
    }).svg;

    var rows = '', i, j;
    for (i = 0; i <= at; i += 1) {
      var ev = calendar.events[i];
      rows += simTr([simTd(String(i + 1)), simTd(Rtext(ev.t)),
                     simTd(ev.kind === 'arrival' ? simChip('arrival', 'hi') : simChip('departure', 'ok')),
                     simTd('customer ' + (ev.who + 1)),
                     simTd('<strong>' + ev.inSystem + '</strong>'),
                     simTd(ev.serving === null ? 'idle' : 'customer ' + (ev.serving + 1)),
                     simTdl(ev.waiting.length
                       ? ev.waiting.map(function (w) { return String(w + 1); }).join(', ')
                       : 'nobody')],
                    i === at ? 'focus' : null);
    }
    log.innerHTML = '<caption>The log, one row per event, kept the way a reader keeps it by hand: the clock, '
      + 'what happened, how many are in the system after it, who holds the server and who is queued.</caption>'
      + simHead(['event', 'clock', 'what', 'who', 'in system', 'in service', 'waiting'])
      + '<tbody>' + rows + '</tbody>';

    /* THE CALENDAR CHANGES SHAPE, and this is the table that shows it: one row
       per pending event, and there are as many as the state at this instant has
       scheduled. It is written into an element the markup declares and never
       read back out of, which is the only property the contract needs. */
    var crows = '';
    if (here) {
      for (j = 0; j < here.pending.length; j += 1) {
        crows += simTr([simTd(String(j + 1)), simTd(Rtext(here.pending[j].t)),
                        simTd(here.pending[j].kind === 'arrival' ? 'arrival' : 'departure'),
                        simTd('customer ' + (here.pending[j].who + 1)),
                        simTdl(Rcmp(here.pending[j].t, here.t) === 0
                          ? 'at this same instant, and departures are taken first'
                          : Rtext(Rsub(here.pending[j].t, here.t)) + ' slots ahead')]);
      }
      if (here.pendingMore > 0) {
        crows += simTr([simTdl('and ' + here.pendingMore + ' further event'
          + (here.pendingMore === 1 ? '' : 's') + ' beyond these, not shown — the calendar is kept legible '
          + 'rather than complete')]);
      }
    }
    cal.innerHTML = '<caption>' + (here
        ? 'The calendar immediately after event ' + (at + 1) + ', at clock ' + Rtext(here.t)
          + ': ' + here.pending.length + ' event' + (here.pending.length === 1 ? '' : 's') + ' pending'
        : 'nothing scheduled') + '. The next clock is the smallest of these, and the empty slots '
      + 'between here and there are never visited.</caption>'
      + simHead(['position', 'scheduled for', 'what', 'who', 'how far ahead'])
      + '<tbody>' + (crows || simTr([simTdl('the calendar is empty; the system has drained')])) + '</tbody>';

    document.getElementById('dsClock').textContent = here ? Rtext(here.t) : '—';
    document.getElementById('dsIn').textContent = here ? String(here.inSystem) : '—';
    document.getElementById('dsPend').textContent = here ? (here.pending.length + here.pendingMore) : '—';
    document.getElementById('dsL').textContent = Rshort(run.L, 4);
    document.getElementById('dsExact').textContent = Rtext(exact.L);
    document.getElementById('dsRho').textContent = Rpct(R(BigInt(Math.min(run.busy, slots)), BigInt(slots)), 1);

    var gap = Rsub(run.L, exact.L);
    status.innerHTML = 'Over ' + slots + ' slots this run produced ' + run.count + ' customers and a '
      + 'time-average number in system of <strong>' + Rshort(run.L, 4) + '</strong>, against the exact '
      + 'long-run <strong>' + Rtext(exact.L) + '</strong> the previous course solved for this chain — '
      + (Rsign(gap) === 0 ? 'the same number, which does happen and is worth checking rather than assuming.'
                          : Rfixed(Rabs(gap), 4) + ' ' + (Rsign(gap) > 0 ? 'above' : 'below') + ' it.')
      + ' The area under the curve above is both the integral of the number in system and the sum of the '
      + 'customers\' times in it, so Little\'s Law is an identity about these averages rather than a model: '
      + 'the run gives arrival rate ' + Rshort(little.lambda, 4) + ' and mean time in system '
      + Rshort(little.W, 4) + ', and their product is the time average.'
      + '<br />That gap is not a defect and it is not noise to be excused. The run\'s time average is an '
      + 'ESTIMATE of the steady-state value, with the standard error the previous lesson computed and the '
      + 'start-from-empty bias the next one removes. Reseed, and it lands somewhere else.'
      + '<br />One thing that is often called a mistake here and is not. This is a slotted model, so '
      + 'stepping one slot at a time IS the model, and next-event simulation is simply the efficient form '
      + 'of the same computation — it skips the slots where nothing happens and agrees slot for slot. The '
      + 'two methods part company only for systems in continuous time, which this path does not sample. '
      + 'The clock marker above jumps because there was nothing in between worth visiting.';
  }

  chainSel.addEventListener('change', redraw);
  [eventS, slotsS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Discrete-event simulation of a queue",
        subtitle="The clock does not tick — it jumps to the next scheduled event, and the calendar is the model",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Step the calendar, then run long and check the average"),
        panel_intro=cfg.get(
            "panel_intro",
            "Arrivals and service times are sampled by inverse transform from the seeded stream, so "
            "the run is reproducible and every figure in it is a fraction. On this configuration: "
            + label + ". Step through the events one at a time to keep the calendar by hand, then "
            "read the long run's time average against the exact value beside it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# warmup -- the transient, the bias it causes, and batch means
# ---------------------------------------------------------------------------

# The state space the exact transient is computed over. The chain can reach
# state t after t steps, so a cap is needed; 64 is far past anywhere these
# loads go, and the mass sitting on it is printed on the page rather than
# assumed away.
_WARMUP_CAP = 64


def _warmup(cfg):
    name, (label, pnum, qnum) = _preset(cfg, "warmup", _CHAINS, "base")

    markup = (
        _toolbar(
            "A run that starts empty is not sampling the steady state",
            "the transient shaded, the exact expectation drawn over the trace, and the two averages",
            [("cyan", "the number in system"), ("green", "the exact expectation at each slot"),
             ("amber", "the warm-up discarded"), ("purple", "the stationary mean")],
        )
        + _stage(_svg("wuTrace", "0 0 660 250",
                      "The number in system against the slot index, the discarded warm-up shaded, and the exact expected occupancy drawn over it."))
        + _table("wuTable")
        + _banner("wuStatus")
    )
    controls = (
        _select("wuChain", "Configuration",
                [("base", "p = 2/5, q = 1/2"), ("faster", "p = 2/5, q = 3/5"),
                 ("busier", "p = 1/2, q = 3/5")], name)
        + _range("wuW", "Warm-up discarded", 0, 200, 100, 10)
        + _range("wuB", "Batches", 2, 10, 4)
        + _range("wuSlots", "Slots in the run", 100, 400, 400, 50)
        + _range("wuSeed", "Seed", 0, 40, 0)
        + _kpis([
            ("Average from the start", "wuNaive"),
            ("Average after the warm-up", "wuKept"),
            ("What the discard changed", "wuBias"),
            ("Expected average from the start", "wuTheory0"),
            ("Expected average after it", "wuTheoryW"),
            ("Stationary mean", "wuStat"),
        ])
        + _hint("wuHint",
                "The green curve is not a fit to the trace. It is the exact expected occupancy at "
                "each slot, computed by carrying the whole distribution forward from an empty system "
                "one slot at a time, so the bias is visible as theory and not only as noise.")
    )

    script = _MODE_JS["warmup"] + _CHAIN_JS_LITERAL + _CHAIN_READ_JS + ("  var CAP = %d;\n" % _WARMUP_CAP) + r"""
  var chainSel = document.getElementById('wuChain'), wS = document.getElementById('wuW');
  var bS = document.getElementById('wuB'), slotsS = document.getElementById('wuSlots');
  var seedS = document.getElementById('wuSeed');
  var svg = document.getElementById('wuTrace'), table = document.getElementById('wuTable');
  var status = document.getElementById('wuStatus');

  /* The transient is a pure function of the chain, the horizon and the cap, and
     it is the one expensive thing on this page -- four hundred steps over
     forty-nine states, on numerators that reach eight hundred digits. Three of
     the five controls (the warm-up, the batch count, the seed) do not change it,
     and a reader drags the warm-up. So it is computed once per (chain, horizon)
     and kept, which is memoisation of a pure function rather than caching of a
     result that could go stale. */
  var cached = null, cachedKey = '';
  function transientFor(ch, slots) {
    var key = chainSel.value + '/' + slots;
    if (key !== cachedKey) { cached = simTransient(ch.p, ch.q, slots, CAP); cachedKey = key; }
    return cached;
  }

  function redraw() {
    var ch = chainOf(chainSel.value), slots = +slotsS.value, seed = +seedS.value, b = +bS.value;
    var w = Math.min(+wS.value, slots - b);
    if (w < 0) w = 0;
    document.getElementById('wuWOut').textContent = w + ' slots';
    document.getElementById('wuBOut').textContent = b;
    document.getElementById('wuSlotsOut').textContent = slots;
    document.getElementById('wuSeedOut').textContent = seed;

    var run = simSlotRun(ch.p, ch.q, slots, seed);
    var win = simWindowAverage(run, w, slots);
    var occ = win.occupancy.map(function (v) { return R(BigInt(v), 1n); });
    var bm = batchMeans(occ, w, b);
    var exact = geoGeo1(ch.p, ch.q);
    var tr = transientFor(ch, slots);
    var theory0 = simExpectedAverage(tr, 0, slots);
    var theoryW = simExpectedAverage(tr, w, slots);

    /* tr.values is the exact expectation long-divided to six places, and it is
       used HERE and nowhere else -- a y coordinate is a pixel. Everything the
       status line and the table report comes off the exact side. */
    var pts = [], curve = [], t, every = Math.max(1, Math.floor(slots / 260));
    for (t = 0; t < slots; t += 1) {
      if (t % every !== 0 && t !== slots - 1) continue;
      pts.push([t, win.occupancy[t]]);
      curve.push([t, tr.values[t]]);
    }
    svg.innerHTML = simPlot({
      width: 660, height: 250,
      series: [{ pts: pts, tone: 'cyan', step: true, thin: true },
               { pts: curve, tone: 'green' }],
      spans: w > 0 ? [{ x0: 0, x1: w, tone: 'amber', label: 'discarded: ' + w + ' slots' }] : [],
      rules: [{ y: simPx(exact.L), tone: 'purple', label: 'stationary ' + Rtext(exact.L) }],
      xLabel: 'slot', y0: 0, x0: 0, x1: slots - 1
    }).svg;

    var rows = '', i;
    for (i = 0; i < bm.means.length; i += 1) {
      rows += simTr([simTd(String(i + 1)),
                     simTd((w + i * bm.size) + ' to ' + (w + (i + 1) * bm.size - 1)),
                     simTd(String(bm.size)),
                     simTd('<strong>' + Rtext(bm.means[i]) + '</strong>')]);
    }
    rows += simTr([simTdl('the mean of the batch means'), simTd(''), simTd(''),
                   simTd(bm.grand === undefined || bm.grand === null ? '—' : Rtext(bm.grand))], 'focus');
    rows += simTr([simTdl('their sample variance, which is what an interval on this run would be built from'),
                   simTd(''), simTd(''),
                   simTd(bm.variance === undefined || bm.variance === null ? 'needs two batches' : simNum(bm.variance, 6))]);
    rows += simTr([simTdl('the average over every slot, warm-up included'), simTd(''), simTd(''),
                   simTd(Rtext(bm.naive))]);
    table.innerHTML = '<caption>Batch means out of one run: the warm-up is thrown away and what is left is '
      + 'split into equal batches. A batch mean is much closer to independent of its neighbours than one '
      + 'slot is of the next, which is what makes replications out of a single run possible at all.</caption>'
      + simHead(['batch', 'slots', 'size', 'batch mean'])
      + '<tbody>' + rows + '</tbody>';

    var bias = win.average === null ? null : Rsub(bm.naive, win.average);
    document.getElementById('wuNaive').textContent = Rshort(bm.naive, 4);
    document.getElementById('wuKept').textContent = win.average === null ? '—' : Rshort(win.average, 4);
    /* SIGNED, and signed the way the reader is looking at it: how far the
       discard MOVED the average, not how far the naive one sat from it. The
       same number with the opposite sign under a label reading "bias" is a
       figure nobody can act on. */
    document.getElementById('wuBias').textContent = bias === null
      ? '—' : (Rsign(bias) < 0 ? '+' : '') + Rfixed(Rneg(bias), 4);
    /* Exact fractions, shown short -- not rounded. The distinction is kept
       everywhere on this course because three quantities here genuinely ARE
       rounded, and a reader who has seen the word used loosely cannot tell
       which three. */
    document.getElementById('wuTheory0').textContent =
      theory0 === null ? '—' : Rfixed(theory0, 4) + ' (exact, to 4 places)';
    document.getElementById('wuTheoryW').textContent =
      theoryW === null ? '—' : Rfixed(theoryW, 4) + ' (exact, to 4 places)';
    document.getElementById('wuStat').textContent = Rtext(exact.L);

    var firstFive = [0, 1, 2, 3, 4].map(function (k) { return Rtext(simTransientExact(tr, k)); }).join(', ');
    status.innerHTML = 'Started empty, the chain has exact expected occupancy '
      + firstFive + ' over its first slots, climbing toward the stationary <strong>' + Rtext(exact.L)
      + '</strong>. Those are fractions, not measurements: the whole distribution is carried forward one '
      + 'slot at a time from an empty system. So the expected time-average over all ' + slots
      + ' slots is <strong>' + (theory0 === null ? '—' : Rfixed(theory0, 4))
      + '</strong> — an exact fraction, shown to four places — and over the ' + (slots - w)
      + ' slots after the warm-up it is <strong>' + (theoryW === null ? '—' : Rfixed(theoryW, 4))
      + '</strong> — the bias is downward, because the queue began with nothing in it, and the discard is '
      + 'what removes it.'
      + '<br />This run gave ' + Rshort(bm.naive, 4) + ' from slot zero against '
      + (win.average === null ? '—' : Rshort(win.average, 4)) + ' after the discard, a difference of '
      + (bias === null ? '—' : Rfixed(Rneg(bias), 4)) + '. '
      + (bias !== null && Rsign(bias) < 0
          ? 'So this run moved the way the theory says, and the discard recovered part of the gap to '
            + Rtext(exact.L) + '.'
          : 'So this run moved the OTHER way, which a single run of a queue this slow to mix does perfectly '
            + 'often — reseed and watch it change sign. The bias is a statement about the expectation, and '
            + 'the two exact figures above are where it is visible; one run is an estimate of them and '
            + 'carries the standard error to prove it.')
      + ' Averaging from the beginning is the default and it is wrong, and it is the one mistake here that '
      + 'no amount of care about the generator can fix.'
      + '<br />A longer run does not cure the bias, it dilutes it. The transient is a fixed quantity of '
      + 'wrongness at the front, so its share of the average falls like one over the run length — which is '
      + 'far slower than deleting it. Quadrupling a hundred slots to four hundred moves the expected average '
      + 'much less than throwing the first quarter away does.'
      + '<br />The exact curve is computed over ' + (CAP + 1) + ' states, because the chain can in principle '
      + 'reach any number in system and a vector cannot be unbounded. The probability sitting on the top '
      + 'state at the last slot is ' + Rfixed(simTransientCapMass(tr, slots - 1), 12)
      + ', so the truncation is stated rather than '
      + 'assumed away — and it is the reason this is the exact transient of a capped chain rather than of an '
      + 'unbounded one.';
  }

  chainSel.addEventListener('change', redraw);
  [wS, bS, slotsS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Warm-up and the initial transient",
        subtitle="Every average taken from an empty start is biased, and a longer run only dilutes it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Drag the warm-up, and watch the bias leave the average"),
        panel_intro=cfg.get(
            "panel_intro",
            "The same seeded run as before, on this configuration: " + label + ". Two averages are "
            "printed — one over every slot and one over the slots after the discarded warm-up — and "
            "beside them the exact expected value of each, so that the difference is theory rather "
            "than a story about noise. The batch means below turn one long run into replications.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# crn -- one stream fed to both systems, and what that does to Var(A - B)
# ---------------------------------------------------------------------------

# Which two configurations are being compared, and why the second pair is here:
# common random numbers works by making the two runs consume the stream the same
# way, and a pair that differs in the ARRIVAL probability consumes it
# differently from the first draw on. The reduction is smaller, and a reader who
# has seen both knows the technique has a mechanism rather than a magic.
_CRN_PAIRS = {
    "service": ("the same arrivals against two service rates, q = 1/2 and q = 3/5 — exact means "
                "12/5 and 6/5, so the true difference is 6/5", "base", "faster"),
    "arrival": ("two different arrival rates, 2/5 and 1/2, against q = 1/2 and q = 3/5 — the two "
                "runs stop consuming the stream in step, and the reduction shrinks", "base", "busier"),
}


def _crn(cfg):
    name, (label, left, right) = _preset(cfg, "crn", _CRN_PAIRS, "service")

    markup = (
        _toolbar(
            "Feed both systems the same stream",
            "the paired difference run by run, and the covariance that shrinks its variance",
            [("cyan", "the difference under a shared stream"), ("red", "under independent streams"),
             ("green", "the exact difference")],
        )
        + _stage(_svg("crDiff", "0 0 660 230",
                      "The estimated difference between the two configurations, replication by replication, under both schemes."))
        + _stage(_svg("crBars", "0 0 660 150",
                      "The variance of the paired difference under each scheme, drawn to scale against each other."))
        + _table("crTable")
        + _banner("crStatus")
    )
    controls = (
        _select("crPair", "What differs",
                [("service", "the service rate only"), ("arrival", "both rates")], name)
        + _select("crScheme", "Streams",
                  [("common", "one stream, fed to both"), ("independent", "a separate stream each")],
                  "common")
        + _range("crReps", "Replications", 8, 48, 24, 4)
        + _range("crSlots", "Slots per replication", 100, 800, 200, 50)
        + _range("crSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Exact difference", "crTrue"),
            ("Estimate, shared stream", "crEstC"),
            ("Estimate, separate streams", "crEstI"),
            ("Var of the difference, shared", "crVarC"),
            ("Var of the difference, separate", "crVarI"),
            ("Covariance doing the work", "crCov"),
        ])
        + _hint("crHint",
                "Both schemes are computed on every redraw, because the claim is a comparison. The "
                "marginal estimate of each system is untouched by the sharing — only the variance of "
                "the difference moves, and that is the only quantity anyone was estimating.")
    )

    script = _MODE_JS["crn"] + _CHAIN_JS_LITERAL + _CHAIN_READ_JS + _js("PAIRS", _CRN_PAIRS) + r"""
  var pairSel = document.getElementById('crPair'), schemeSel = document.getElementById('crScheme');
  var repsS = document.getElementById('crReps'), slotsS = document.getElementById('crSlots');
  var seedS = document.getElementById('crSeed');
  var diffSvg = document.getElementById('crDiff'), barsSvg = document.getElementById('crBars');
  var table = document.getElementById('crTable'), status = document.getElementById('crStatus');

  /* The separate-stream seeds are the shared ones plus a fixed shift, so the two
     schemes differ in exactly one thing: whether the second system reads the
     first system's draws. Anything else would confound the comparison the mode
     exists to make. */
  var SHIFT = 100000;

  function redraw() {
    var pair = PAIRS[pairSel.value], A = chainOf(pair[1]), B = chainOf(pair[2]);
    var reps = +repsS.value, slots = +slotsS.value, seed = +seedS.value;
    document.getElementById('crRepsOut').textContent = reps;
    document.getElementById('crSlotsOut').textContent = slots;
    document.getElementById('crSeedOut').textContent = seed;

    var xa = [], xbC = [], xbI = [], dC = [], dI = [], j;
    for (j = 0; j < reps; j += 1) {
      var s = seed + 1 + 977 * j;
      var ra = simSlotRun(A.p, A.q, slots, s);
      var rbC = simSlotRun(B.p, B.q, slots, s);
      var rbI = simSlotRun(B.p, B.q, slots, s + SHIFT);
      xa.push(ra.L); xbC.push(rbC.L); xbI.push(rbI.L);
      dC.push(Rsub(ra.L, rbC.L)); dI.push(Rsub(ra.L, rbI.L));
    }
    var trueDiff = Rsub(geoGeo1(A.p, A.q).L, geoGeo1(B.p, B.q).L);
    var varC = sampleVar(dC), varI = sampleVar(dI);
    var covC = sampleCov(xa, xbC), covI = sampleCov(xa, xbI);
    var rho2C = rhoSquared(xa, xbC);
    var ratio = (varC === null || varI === null || Rzero(varC)) ? null : Rdiv(varI, varC);
    var shared = schemeSel.value === 'common';

    diffSvg.innerHTML = simPlot({
      width: 660, height: 230,
      series: [{ pts: dC.map(function (d, i) { return [i + 1, simPx(d)]; }), tone: 'cyan', dots: true,
                 thin: !shared, dashed: !shared, label: 'shared' },
               { pts: dI.map(function (d, i) { return [i + 1, simPx(d)]; }), tone: 'red', dots: true,
                 thin: shared, dashed: shared, label: 'separate' }],
      rules: [{ y: simPx(trueDiff), tone: 'green', solid: true, label: 'exact ' + Rtext(trueDiff) }],
      xLabel: 'replication', x0: 0, x1: reps + 1
    }).svg;

    barsSvg.innerHTML = simBars([
      { label: 'Var of the difference, separate streams', value: varI === null ? R0 : varI, tone: 'red',
        text: varI === null ? '—' : Rfixed(varI, 5) },
      { label: 'Var of the difference, one shared stream', value: varC === null ? R0 : varC, tone: 'cyan',
        text: varC === null ? '—' : Rfixed(varC, 5) },
      { label: 'twice the covariance, the term removed', value: covC === null ? R0 : Rmul(R(2n, 1n), covC),
        tone: 'green', text: covC === null ? '—' : Rfixed(Rmul(R(2n, 1n), covC), 5) }
    ], { width: 660 }).svg;

    var rows = '', shown = Math.min(reps, 12);
    for (j = 0; j < shown; j += 1) {
      rows += simTr([simTd(String(j + 1)), simTd(Rshort(xa[j], 4)),
                     simTd(Rshort(xbC[j], 4)), simTd('<strong>' + Rshort(dC[j], 4) + '</strong>'),
                     simTd(Rshort(xbI[j], 4)), simTd('<strong>' + Rshort(dI[j], 4) + '</strong>')]);
    }
    table.innerHTML = '<caption>Replication by replication. The first system is the same run in both '
      + 'schemes; only the second system changes, between reading the same draws and reading its own. '
      + 'Look down the two difference columns, not across the estimates.</caption>'
      + simHead(['replication', 'first system', 'second, shared stream', 'difference',
                 'second, own stream', 'difference'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('crTrue').textContent = Rtext(trueDiff);
    document.getElementById('crEstC').textContent = Rfixed(sampleMean(dC), 4);
    document.getElementById('crEstI').textContent = Rfixed(sampleMean(dI), 4);
    document.getElementById('crVarC').textContent = varC === null ? '—' : Rfixed(varC, 5);
    document.getElementById('crVarI').textContent = varI === null ? '—' : Rfixed(varI, 5);
    document.getElementById('crCov').textContent = covC === null ? '—' : Rfixed(covC, 5);

    status.innerHTML = 'Var(A &minus; B) = Var A + Var B &minus; 2 Cov(A, B), and that is the whole lever. '
      + 'Feeding both configurations the same draws makes their outputs move together: the sample '
      + 'covariance here is <strong>' + (covC === null ? '—' : Rfixed(covC, 5))
      + '</strong> with a shared stream against ' + (covI === null ? '—' : Rfixed(covI, 5))
      + ' with separate ones, and twice that difference comes straight off the variance of the '
      + 'difference — ' + (varC === null ? '—' : Rfixed(varC, 5)) + ' shared against '
      + (varI === null ? '—' : Rfixed(varI, 5)) + ' separate'
      + (ratio === null ? '.' : ', a factor of <strong>' + Rfixed(ratio, 3) + '</strong>.')
      + ' The squared correlation between the two systems under sharing is '
      + (rho2C === null ? '—' : simNum(rho2C, 4)) + ', and it is a fraction, not a measurement of one.'
      + '<br />The estimates themselves barely move: ' + Rfixed(sampleMean(dC), 4) + ' shared against '
      + Rfixed(sampleMean(dI), 4) + ' separate, both aiming at the exact <strong>' + Rtext(trueDiff)
      + '</strong>. That is the point. Each system\'s own estimate is untouched by the sharing — its '
      + 'marginal distribution is identical — and only the difference improves. Crediting common random '
      + 'numbers with a smaller error bar on A alone is the misreading to avoid.'
      + '<br />Independent runs are not fairer. Fairness is not a property of seeds; it is a property of '
      + 'the estimator, and both of these are unbiased for the same number. Independent runs are simply '
      + 'noisier about the one quantity the comparison was for.'
      + (pairSel.value === 'arrival'
          ? '<br />On this pair the two systems differ in their arrival probability as well, so from the '
            + 'first draw on they are not consuming the stream in step — a slot that produces an arrival '
            + 'in one produces none in the other, and the service draws then line up against different '
            + 'customers. The covariance is still positive and the technique still pays, but less, and '
            + 'that is the mechanism rather than an exception to it.'
          : '<br />On this pair the two systems see exactly the same arrivals, because the arrival '
            + 'probability is the same and the test against it reads the same draw. Only the service '
            + 'times differ, which is the best case this technique has.');
  }

  [pairSel, schemeSel].forEach(function (el) { el.addEventListener('change', redraw); });
  [repsS, slotsS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Common random numbers",
        subtitle="Positive covariance shrinks the variance of the difference, which is the only thing being estimated",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "The same draws, or a fresh set, and the variance of the difference"),
        panel_intro=cfg.get(
            "panel_intro",
            "Two configurations of the slotted queue are estimated side by side: " + label + ". Each "
            "replication is run twice for the second configuration — once reading the first "
            "configuration's own draws, once reading its own — so the two schemes differ in exactly "
            "one thing and every variance below is an exact fraction.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# antithetic -- U against 1 - U, in the best case and in the worst one
# ---------------------------------------------------------------------------

# The two cases, and the second is not a footnote. Antithetic pairing is a fact
# about monotonicity, and a reader who has only seen it work cannot tell the
# condition from the conclusion.
_ANTITHETIC = {
    "monotone": ("g(U) = 1 when U is at least 1/2 and 0 otherwise — monotone in U, so the partner "
                 "draw is exactly 1 minus this one",
                 "monotone"),
    "nonmonotone": ("g(U) = the distance from U to 1/2 — symmetric about 1/2, so the partner draw "
                    "is identical and the pairing buys nothing at twice the cost",
                    "nonmonotone"),
}


def _antithetic(cfg):
    name, (label, kind) = _preset(cfg, "antithetic", _ANTITHETIC, "monotone")

    markup = (
        _toolbar(
            "Pair each draw with its opposite",
            "the pair table, the pair mean, and the variance that follows from the sign of the covariance",
            [("cyan", "the pair mean"), ("amber", "the draw from U"),
             ("red", "the draw from 1 minus U"), ("green", "the exact expectation")],
        )
        + _stage(_svg("anTrace", "0 0 660 230",
                      "Each pair's two draws and their mean, pair by pair, against the exact expectation."))
        + _stage(_svg("anBars", "0 0 660 150",
                      "The variance of the antithetic pair mean against the variance an independent pair would have."))
        + _table("anTable")
        + _banner("anStatus")
    )
    controls = (
        _select("anCase", "The quantity being averaged",
                [("monotone", "monotone in U — the best case"),
                 ("nonmonotone", "symmetric about 1/2 — the worst case")], name)
        + _range("anPairs", "Pairs", 8, 128, 64, 8)
        + _range("anSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Var of the pair mean", "anVarPair"),
            ("Var of one draw", "anVarOne"),
            ("Var of an independent pair mean", "anVarIndep"),
            ("Covariance within a pair", "anCov"),
            ("Squared correlation", "anRho"),
            ("What the pairing bought", "anGain"),
        ])
        + _hint("anHint",
                "A pair is one observation of the pair mean, not two independent draws. Counting it as "
                "two is how this technique gets credited with a reduction it did not achieve, so the "
                "comparison below is against an independent pair — the same two draws' worth of work.")
    )

    script = _MODE_JS["antithetic"] + _js("CASES", _ANTITHETIC) + r"""
  var caseSel = document.getElementById('anCase'), pairsS = document.getElementById('anPairs');
  var seedS = document.getElementById('anSeed');
  var traceSvg = document.getElementById('anTrace'), barsSvg = document.getElementById('anBars');
  var table = document.getElementById('anTable'), status = document.getElementById('anStatus');

  /* Both quantities are functions of U alone, which is what makes the pairing
     exact rather than approximate: the partner of U is 1 - U and nothing else in
     the run depends on the draw. The modulus is odd, so U is never 1/2 and the
     comparison in the monotone case never has to settle a tie. */
  function gOf(kind, u) {
    if (kind === 'monotone') return Rcmp(u, R(1n, 2n)) >= 0 ? R1 : R0;
    return Rabs(Rsub(u, R(1n, 2n)));
  }
  function exactMean(kind) {
    /* Both have an exact expectation, and both are worth having on the page: a
       reduction that moved the estimate would not be a reduction. */
    return kind === 'monotone' ? R(1n, 2n) : R(1n, 4n);
  }

  function redraw() {
    var kind = caseSel.value, pairs = +pairsS.value, seed = +seedS.value;
    document.getElementById('anPairsOut').textContent = pairs;
    document.getElementById('anSeedOut').textContent = seed;

    var us = simUniform(seed + 1, pairs), A = [], B = [], means = [], i;
    for (i = 0; i < pairs; i += 1) {
      var u = us[i], v = Rsub(R1, u);
      A.push(gOf(kind, u)); B.push(gOf(kind, v));
      means.push(Rdiv(Radd(A[i], B[i]), R(2n, 1n)));
    }
    var varPair = sampleVar(means), varOne = sampleVar(A);
    var varIndep = varOne === null ? null : Rdiv(varOne, R(2n, 1n));
    var cov = sampleCov(A, B), rho2 = rhoSquared(A, B);
    var mu = exactMean(kind);
    var gain = (varPair === null || varIndep === null || Rzero(varIndep)) ? null : Rdiv(varPair, varIndep);

    traceSvg.innerHTML = simPlot({
      width: 660, height: 230,
      series: [{ pts: A.map(function (x, k) { return [k + 1, simPx(x)]; }), tone: 'amber', dots: true, thin: true },
               { pts: B.map(function (x, k) { return [k + 1, simPx(x)]; }), tone: 'red', dots: true, thin: true },
               { pts: means.map(function (x, k) { return [k + 1, simPx(x)]; }), tone: 'cyan', dots: true }],
      rules: [{ y: simPx(mu), tone: 'green', solid: true, label: 'exact ' + Rtext(mu) }],
      xLabel: 'pair', x0: 0, x1: pairs + 1
    }).svg;

    barsSvg.innerHTML = simBars([
      { label: 'an independent pair mean', value: varIndep === null ? R0 : varIndep, tone: 'red',
        text: varIndep === null ? '—' : Rfixed(varIndep, 6) },
      { label: 'the antithetic pair mean', value: varPair === null ? R0 : varPair, tone: 'cyan',
        text: varPair === null ? '—' : Rfixed(varPair, 6) },
      { label: 'one draw on its own', value: varOne === null ? R0 : varOne, tone: 'amber',
        text: varOne === null ? '—' : Rfixed(varOne, 6) }
    ], { width: 660 }).svg;

    var rows = '', shown = Math.min(pairs, 10);
    for (i = 0; i < shown; i += 1) {
      rows += simTr([simTd(String(i + 1)), simTd(Rshort(us[i], 5)), simTd(Rshort(Rsub(R1, us[i]), 5)),
                     simTd(Rshort(A[i], 5)), simTd(Rshort(B[i], 5)),
                     simTd('<strong>' + Rshort(means[i], 5) + '</strong>')]);
    }
    table.innerHTML = '<caption>The pair table. Read the last column: in the monotone case every entry is '
      + 'the same number, and in the symmetric case every entry is the draw itself.</caption>'
      + simHead(['pair', 'U', '1 − U', 'g(U)', 'g(1 − U)', 'pair mean'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('anVarPair').textContent = varPair === null ? '—' : simNum(varPair, 6);
    document.getElementById('anVarOne').textContent = varOne === null ? '—' : simNum(varOne, 6);
    document.getElementById('anVarIndep').textContent = varIndep === null ? '—' : simNum(varIndep, 6);
    document.getElementById('anCov').textContent = cov === null ? '—' : simNum(cov, 6);
    document.getElementById('anRho').textContent = rho2 === null ? '—' : simNum(rho2, 6);
    document.getElementById('anGain').textContent = gain === null ? '—' : Rtext(gain) + ' times';

    var helped = gain !== null && Rcmp(gain, R1) < 0;
    status.innerHTML = 'Var of the pair mean = (Var A + Var B + 2 Cov(A, B)) / 4, so the sign of the '
      + 'covariance decides everything. Here the covariance within a pair is <strong>'
      + (cov === null ? '—' : simNum(cov, 6)) + '</strong> and the squared correlation is <strong>'
      + (rho2 === null ? '—' : simNum(rho2, 6)) + '</strong>.'
      + (kind === 'monotone'
          ? ' The quantity is monotone in U, so the partner draw is exactly 1 minus this one: every pair '
            + 'mean is exactly 1/2, the sample variance of the pair means is <strong>'
            + (varPair === null ? '—' : Rtext(varPair)) + '</strong>, and the correlation is exactly '
            + 'minus one. Against an independent pair, which would have variance '
            + (varIndep === null ? '—' : simNum(varIndep, 6)) + ', that is the whole variance gone. '
            + 'Inverse-transform sampling is monotone in U by construction, which is why this works on '
            + 'this path at all.'
          : ' The quantity is symmetric about 1/2, so g(1 − U) is g(U) identically: the pair is perfectly '
            + 'POSITIVELY correlated, the correlation is exactly plus one, and the pair mean has exactly '
            + 'the variance of a single draw — ' + (varPair === null ? '—' : simNum(varPair, 6))
            + ' against ' + (varOne === null ? '—' : simNum(varOne, 6))
            + '. It consumed two draws to produce one observation no better than one draw, which is '
            + 'exactly twice the work for the same width.')
      + '<br />The comparison that matters is against an independent PAIR, not against a single draw, '
      + 'because a pair costs two draws either way. On this case the antithetic pair mean has '
      + (gain === null ? '—' : Rtext(gain)) + ' times the variance of an independent pair mean — '
      + (helped ? 'a genuine reduction.' : 'no reduction at all, and on this quantity exactly double.')
      + ' A pair is ONE observation of the pair mean; counting it as two independent draws is how the '
      + 'technique gets credited with a reduction it did not make.'
      + '<br />And the estimate is untouched either way: both schemes are unbiased for the exact '
      + Rtext(mu) + '. Monotonicity is a real condition, not a technicality — when it fails the pairing '
      + 'can be exactly as bad as it was good, and both cases are on this page rather than one of them '
      + 'being mentioned.';
  }

  caseSel.addEventListener('change', redraw);
  [pairsS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Antithetic variates",
        subtitle="Pair U with 1 − U: a negative covariance halves the width, and a positive one wastes the draw",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "The pair table, and the variance column beside it"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each pair uses one draw and its opposite: " + label + ". Every figure below is an exact "
            "fraction, including the variance of the pair mean, so the two cases can be compared "
            "rather than described.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# control -- the variance as a quadratic in b, and the factor 1 - rho^2
# ---------------------------------------------------------------------------

# Two companions, both with a mean that is KNOWN rather than estimated, which is
# the condition the technique stands on. The second is there because the
# misconception that quietly ruins this method is that any correlated quantity
# will do: the honest failure is a control whose mean you know and whose
# correlation is nearly nothing, and it buys nearly nothing.
_CONTROL_VARIATES = {
    "arrivals": ("the number of arrivals in the run — its mean is exactly the number of slots times "
                 "the arrival probability, so it is known and not estimated, and it drives the queue",
                 "arrivals"),
    "foreign": ("a count of draws below 1/2 taken from a different stream — its mean is exactly half "
                "the slots, equally known, and it has almost nothing to do with the queue",
                "foreign"),
}


def _control(cfg):
    name, (label, which) = _preset(cfg, "control", _CONTROL_VARIATES, "arrivals")
    chain = cfg.get("chain", "base")
    if chain not in _CHAINS:
        raise ValueError(
            "simulate_lab: mode 'control' has no configuration %r; they are %s"
            % (chain, ", ".join(sorted(_CHAINS)))
        )

    markup = (
        _toolbar(
            "The variance is a quadratic in b",
            "its vertex is b* = Cov(X, C) / Var C, and at the vertex the variance has been multiplied by 1 − ρ²",
            [("cyan", "the variance at b"), ("purple", "the vertex, at b*"),
             ("amber", "the b you chose"), ("green", "the variance with no control at all")],
        )
        + _stage(_svg("ctCurve", "0 0 660 250",
                      "The variance of the controlled estimator as a function of b, with the vertex and the chosen b marked."))
        + _table("ctTable")
        + _banner("ctStatus")
    )
    controls = (
        _select("ctVariate", "The companion quantity",
                [("arrivals", "the arrivals, which drive the queue"),
                 ("foreign", "a count from another stream, nearly unrelated")], name)
        + _select("ctChain", "Configuration",
                  [("base", "p = 2/5, q = 1/2"), ("faster", "p = 2/5, q = 3/5"),
                   ("busier", "p = 1/2, q = 3/5")], chain)
        + _range("ctB", "b, as a percentage of b*", -100, 250, 100, 5)
        + _range("ctReps", "Replications", 8, 48, 24, 4)
        + _range("ctSlots", "Slots per replication", 100, 800, 200, 50)
        + _range("ctSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Cov(X, C)", "ctCov"),
            ("Var C", "ctVarC"),
            ("b*", "ctBStar"),
            ("ρ²", "ctRho"),
            ("The factor 1 − ρ²", "ctFactor"),
            ("Variance at your b", "ctVarAt"),
        ])
        + _hint("ctHint",
                "ρ = Cov(X, C) / (σ_X σ_C) — the covariance rescaled by both standard deviations, so "
                "that ρ lies between −1 and 1 and measures the strength of the linear relationship "
                "whatever the units of either quantity. σ_X and σ_C are square roots and ρ itself is "
                "generally irrational; ρ² is a ratio of exact rationals, so the reduction factor "
                "1 − ρ² is exact even where ρ is not.")
    )

    script = _MODE_JS["control"] + _CHAIN_JS_LITERAL + _CHAIN_READ_JS + _js("VARIATES", _CONTROL_VARIATES) + r"""
  var varSel = document.getElementById('ctVariate'), chainSel = document.getElementById('ctChain');
  var bS = document.getElementById('ctB'), repsS = document.getElementById('ctReps');
  var slotsS = document.getElementById('ctSlots'), seedS = document.getElementById('ctSeed');
  var svg = document.getElementById('ctCurve'), table = document.getElementById('ctTable');
  var status = document.getElementById('ctStatus');

  var FOREIGN = 400000;      /* a stream the queue never reads */

  function redraw() {
    var ch = chainOf(chainSel.value), which = varSel.value;
    var reps = +repsS.value, slots = +slotsS.value, seed = +seedS.value;
    document.getElementById('ctRepsOut').textContent = reps;
    document.getElementById('ctSlotsOut').textContent = slots;
    document.getElementById('ctSeedOut').textContent = seed;

    var X = [], C = [], j, i;
    for (j = 0; j < reps; j += 1) {
      var s = seed + 1 + 977 * j, run = simSlotRun(ch.p, ch.q, slots, s);
      X.push(run.L);
      if (which === 'arrivals') {
        C.push(R(BigInt(run.count), 1n));
      } else {
        /* x/m below 1/2 is 2x below m, in whole numbers and with no allocation.
           The modulus is odd, so there is no tie to settle. */
        var raw = simStream(s + FOREIGN, slots), c = 0, M = simModulus();
        for (i = 0; i < slots; i += 1) if (2 * raw[i] < M) c += 1;
        C.push(R(BigInt(c), 1n));
      }
    }
    /* THE CONTROL'S MEAN IS KNOWN, WHICH IS THE WHOLE CONDITION. The arrivals
       are a sum of `slots` independent indicators of probability p, so their mean
       is exactly slots x p; the foreign count is exactly half the slots. Neither
       is estimated from the run, and a control whose mean is only estimated
       reintroduces precisely the error it was brought in to remove. */
    var muC = which === 'arrivals' ? Rmul(R(BigInt(slots), 1n), ch.p) : R(BigInt(slots), 2n);
    var ctl = controlB(X, C);
    var exact = geoGeo1(ch.p, ch.q);

    if (ctl.bStar === null) {
      svg.innerHTML = simLabel(20, 40, 'the control has no variance, so there is no b to choose', 'red');
      table.innerHTML = '';
      status.innerHTML = 'Every replication produced the same value of the companion quantity, so Var C is '
        + 'zero and b* = Cov / Var C does not exist. Widen the run or the number of replications.';
      return;
    }

    var pct = +bS.value, b = Rmul(R(BigInt(pct), 100n), ctl.bStar);
    document.getElementById('ctBOut').textContent = pct + '% of b*';
    var varAt = controlVarAt(ctl.quadratic, b);
    var factor = Rsub(R1, ctl.rho2);

    /* The parabola is SAMPLED from the same quadratic the numbers come out of,
       so the picture and the figures cannot disagree. */
    var lo = simPx(ctl.bStar) - 1.6 * Math.abs(simPx(ctl.bStar) || 1);
    var hi = simPx(ctl.bStar) + 1.6 * Math.abs(simPx(ctl.bStar) || 1);
    var pts = [], k;
    for (k = 0; k <= 120; k += 1) {
      var bb = lo + (hi - lo) * k / 120;
      pts.push([bb, simPx(ctl.quadratic[0]) + simPx(ctl.quadratic[1]) * bb + simPx(ctl.quadratic[2]) * bb * bb]);
    }
    svg.innerHTML = simPlot({
      width: 660, height: 250, series: [{ pts: pts, tone: 'cyan' }],
      rules: [{ y: simPx(ctl.varRaw), tone: 'green', label: 'no control: ' + Rfixed(ctl.varRaw, 5) }],
      marks: [{ x: simPx(ctl.bStar), y: simPx(ctl.varAt), tone: 'purple', label: 'b*' },
              { x: simPx(b), y: simPx(varAt), tone: 'amber', hollow: true, label: 'your b' }],
      xLabel: 'b', fmtX: function (v) { return v.toFixed(3); }
    }).svg;

    var rows = '', shown = Math.min(reps, 12);
    for (j = 0; j < shown; j += 1) {
      var dev = Rsub(C[j], muC);
      rows += simTr([simTd(String(j + 1)), simTd(Rshort(X[j], 4)), simTd(Rtext(C[j])),
                     simTd((Rsign(dev) > 0 ? '+' : '') + Rtext(dev)),
                     simTd('<strong>' + Rfixed(Rsub(X[j], Rmul(b, dev)), 4) + '</strong>')]);
    }
    table.innerHTML = '<caption>Replication by replication: the output, the companion quantity, how far the '
      + 'companion fell from its KNOWN mean of ' + Rtext(muC) + ', and the corrected value. The correction '
      + 'has expectation zero, so the estimator stays unbiased at every b.</caption>'
      + simHead(['replication', 'X', 'C', 'C − E[C]', 'X − b(C − E[C])'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('ctCov').textContent = Rfixed(ctl.cov, 5);
    document.getElementById('ctVarC').textContent = Rfixed(ctl.varC, 4);
    document.getElementById('ctBStar').textContent = simNum(ctl.bStar, 6);
    document.getElementById('ctRho').textContent = simNum(ctl.rho2, 6);
    document.getElementById('ctFactor').textContent = simNum(factor, 6);
    document.getElementById('ctVarAt').textContent = Rfixed(varAt, 6);

    var rhoSurd = Rsurd(ctl.rho2);
    var rhoText = (Rsign(ctl.cov) < 0 ? '−' : '') + surdDec(rhoSurd, 4);
    status.innerHTML = 'X − b(C − E[C]) is unbiased for E[X] at every b, because the correction has '
      + 'expectation zero — and its variance is Var X − 2b Cov(X, C) + b² Var C, a quadratic in b. '
      + 'Completing the square puts the vertex at b* = Cov / Var C = <strong>' + simNum(ctl.bStar, 6)
      + '</strong>, and there the variance is Var X times 1 − ρ². Here ρ² is <strong>'
      + simNum(ctl.rho2, 6) + '</strong> and the factor 1 − ρ² is <strong>' + simNum(factor, 6)
      + '</strong> — both of them ratios of whole numbers, however they are shown: '
      + Rfixed(ctl.varRaw, 6) + ' becomes ' + Rfixed(ctl.varAt, 6) + '.'
      + '<br />ρ itself is about ' + rhoText + ' — a rounded decimal, because ρ is a covariance over a '
      + 'product of two square roots and is irrational at almost any data. ρ² is a ratio of two exact '
      + 'rationals, which is why the reduction factor above needs no rounding at all. That is the only '
      + 'quantity of the two worth printing.'
      + '<br />At your b the variance is ' + Rfixed(varAt, 6) + ', which is '
      + (Rcmp(varAt, ctl.varAt) <= 0 ? 'the minimum' : Rfixed(Rdiv(varAt, ctl.varAt), 4) + ' times the minimum')
      + ' — the curve rises on BOTH sides of b*, and a b of the wrong sign is worse than no control at all. '
      + 'The exact long-run value all of this is estimating is ' + Rtext(exact.L) + '.'
      + '<br />The condition the method stands on is not correlation, it is a KNOWN mean. '
      + (which === 'arrivals'
          ? 'The arrivals here have mean exactly ' + Rtext(muC) + ' — the number of slots times the arrival '
            + 'probability — and they drive the queue, so the correlation is real and the reduction is real.'
          : 'This companion has mean exactly ' + Rtext(muC) + ', just as firmly known, and almost nothing '
            + 'to do with the queue. The factor above is close to one: a correlated quantity is required, '
            + 'and a known mean on its own buys nothing.')
      + ' The control does NOT have to be the target in disguise. What it must not be is a quantity whose '
      + 'mean you estimated from the same run — that puts back exactly the error the control was for.';
  }

  [varSel, chainSel].forEach(function (el) { el.addEventListener('change', redraw); });
  [bS, repsS, slotsS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Control variates",
        subtitle="A companion with a known mean, and the variance multiplied by 1 − ρ²",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the companion, then drag b off its optimum"),
        panel_intro=cfg.get(
            "panel_intro",
            "The output is the time-average number in system over a run of the slotted queue; the "
            "companion is " + label + ". Cov(X, C), Var C, b* and ρ² are all exact fractions computed "
            "from the replications below, and the quadratic drawn above is the same quadratic those "
            "numbers come out of.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# importance -- p, q, the weights p/q, and the two variances that follow
# ---------------------------------------------------------------------------

# The event is ten fair coins all landing heads: probability 1/1024, near enough
# to one in a thousand to be the case this technique exists for, and known
# exactly, which is what makes the comparison a measurement. Each preset is the
# head probability of the coin q samples with, as [numerator, denominator].
_QCHOICES = {
    "good": ("a coin weighted toward heads, P(head) = 4/5 — the event becomes common and the "
             "weights stay small", [4, 5], False),
    "bad": ("a coin weighted away from heads, P(head) = 1/5 — the event becomes rarer still and the "
            "one weight that matters becomes enormous", [1, 5], False),
    "crude": ("the fair coin itself, P(head) = 1/2 — every weight is exactly 1, which is direct "
              "simulation written as importance sampling", [1, 2], False),
    "hole": ("the same coin weighted toward heads, but with all of its mass on ten heads removed — "
             "a perfectly good distribution that can never produce the event", [4, 5], True),
}


def _importance(cfg):
    name, (label, theta, holed) = _preset(cfg, "importance", _QCHOICES, "good")

    markup = (
        _toolbar(
            "Sample where the event is, then weight it back",
            "the likelihood ratio p/q per outcome, and what the reweighting does to the variance",
            [("cyan", "the running estimate"), ("green", "the exact probability"),
             ("amber", "the variance under a good q"), ("red", "under a bad one")],
        )
        + _stage(_svg("imRun", "0 0 660 240",
                      "The running importance-sampling estimate against the exact probability of the event."))
        + _stage(_svg("imBars", "0 0 660 150",
                      "The per-draw variance under direct sampling and under each choice of q, drawn to scale."))
        + _table("imTable")
        + _table("imDraws")
        + _banner("imStatus")
    )
    controls = (
        _select("imQ", "The distribution sampled from",
                [("good", "P(head) = 4/5 — a good q"), ("bad", "P(head) = 1/5 — a bad q"),
                 ("crude", "P(head) = 1/2 — direct simulation"),
                 ("hole", "P(head) = 4/5 with the event removed")], name)
        + _range("imDrawCount", "Draws", 200, 4000, 2000, 200)
        + _range("imSeed", "Seed", 0, 40, 1)
        + _kpis([
            ("Exact probability", "imTheta"),
            ("Per-draw variance, direct", "imVarP"),
            ("Per-draw variance, this q", "imVarQ"),
            ("The ratio between them", "imRatio"),
            ("Draws that hit the event", "imHits"),
            ("This run's estimate", "imEst"),
        ])
        + _hint("imHint",
                "Both estimators are unbiased for the same exact probability, so the estimate column "
                "is not where the difference lives. Read the variance column: the whole question is "
                "what the reweighting did to the spread, and it can collapse or explode.")
    )

    script = _MODE_JS["importance"] + _js("QCHOICES", _QCHOICES) + r"""
  var qSel = document.getElementById('imQ'), drawS = document.getElementById('imDrawCount');
  var seedS = document.getElementById('imSeed');
  var runSvg = document.getElementById('imRun'), barsSvg = document.getElementById('imBars');
  var table = document.getElementById('imTable'), drawTable = document.getElementById('imDraws');
  var status = document.getElementById('imStatus');

  var COINS = 10;

  function qOf(key) {
    var spec = QCHOICES[key], theta = R(BigInt(spec[1][0]), BigInt(spec[1][1]));
    var pmf = simBinomPmf(COINS, theta);
    return spec[2] ? simHoledPmf(pmf, R(BigInt(COINS), 1n)) : pmf;
  }

  function redraw() {
    var key = qSel.value, count = +drawS.value, seed = +seedS.value;
    document.getElementById('imDrawCountOut').textContent = count;
    document.getElementById('imSeedOut').textContent = seed;

    var p = simBinomPmf(COINS, R(1n, 2n)), q = qOf(key), at = R(BigInt(COINS), 1n);
    var indicator = function (x) { return Rcmp(x, at) === 0; };
    var res = importanceRun(p, q, indicator);
    var good = importanceRun(p, qOf('good'), indicator);
    var bad = importanceRun(p, qOf('bad'), indicator);

    var rows = '', i;
    for (i = 0; i < p.length; i += 1) {
      var qi = q[i][1], w = Rzero(qi) ? null : Rdiv(p[i][1], qi);
      rows += simTr([simTd(Rtext(p[i][0])), simTd(Rshort(p[i][1], 6)), simTd(Rshort(qi, 6)),
                     simTd(w === null ? 'undefined' : Rshort(w, 6)),
                     simTd(indicator(p[i][0]) ? simChip('the event', 'hi') : '')],
                    indicator(p[i][0]) ? 'focus' : null);
    }
    table.innerHTML = '<caption>The two tables side by side, with the likelihood ratio p/q per outcome. '
      + 'The row that matters is the last one; every other row contributes nothing to this estimate and '
      + 'is where direct simulation spends all of its draws.</caption>'
      + simHead(['heads', 'p', 'q', 'p / q', ''])
      + '<tbody>' + rows + '</tbody>';

    if (res.refused) {
      runSvg.innerHTML = simLabel(20, 40, 'there is no estimator here, and that is the answer', 'red');
      barsSvg.innerHTML = simBars([
        { label: 'direct sampling from p', value: good.varCrude, tone: 'green', text: Rshort(good.varCrude, 10) },
        { label: 'a good q, P(head) = 4/5', value: good.varIS, tone: 'amber', text: Rshort(good.varIS, 10) },
        { label: 'a bad q, P(head) = 1/5', value: bad.varIS, tone: 'red', text: Rshort(bad.varIS, 10) }
      ], { width: 660 }).svg;
      drawTable.innerHTML = '';
      document.getElementById('imTheta').textContent = Rtext(good.estimate);
      document.getElementById('imVarP').textContent = Rshort(good.varCrude, 10);
      document.getElementById('imVarQ').textContent = 'refused';
      document.getElementById('imRatio').textContent = 'refused';
      document.getElementById('imHits').textContent = '0, and it never will';
      document.getElementById('imEst').textContent = 'there is none';
      status.innerHTML = '<strong>Refused.</strong> ' + simEsc(res.why)
        + '<br />This q is a perfectly good distribution — its probabilities are positive and they sum to '
        + 'one — and it is still unusable, because the likelihood ratio p/q is undefined exactly where the '
        + 'event lives. An implementation that quietly skipped that outcome would return a number, and the '
        + 'number would be biased low with no variance figure anywhere showing it. Unbiasedness holds for '
        + 'EVERY q that is positive wherever p is, and for no other.'
        + '<br />That is the one condition on q. It is not a condition about being close to p, or about '
        + 'making the event common; those change the variance. This one decides whether there is an '
        + 'estimator at all.';
      return;
    }

    var run = simImportanceRun(p, q, at, seed + 1, count);
    var pts = [], every = Math.max(1, Math.floor(count / 240));
    for (i = 0; i < run.rows.length; i += 1) {
      if (i % every !== 0 && i !== run.rows.length - 1) continue;
      pts.push([i + 1, simPx(run.rows[i].running)]);
    }
    runSvg.innerHTML = simPlot({
      width: 660, height: 240, series: [{ pts: pts, tone: 'cyan', thin: true }],
      rules: [{ y: simPx(res.estimate), tone: 'green', solid: true, label: 'exact ' + Rtext(res.estimate) }],
      xLabel: 'draws', y0: 0
    }).svg;

    barsSvg.innerHTML = simBars([
      { label: 'direct sampling from p', value: res.varCrude, tone: 'green', text: Rshort(res.varCrude, 10) },
      { label: 'a good q, P(head) = 4/5', value: good.varIS, tone: 'amber', text: Rshort(good.varIS, 10) },
      { label: 'a bad q, P(head) = 1/5', value: bad.varIS, tone: 'red', text: Rshort(bad.varIS, 10) }
    ], { width: 660 }).svg;

    var drows = '', shownHits = 0;
    for (i = 0; i < run.rows.length && drows.split('<tr>').length <= 10; i += 1) {
      if (i >= 6 && !run.rows[i].hit) continue;
      if (run.rows[i].hit) shownHits += 1;
      drows += simTr([simTd(String(i + 1)), simTd(Rtext(run.rows[i].draw)),
                      simTd(Rshort(run.rows[i].w, 6)),
                      simTd(run.rows[i].hit ? simChip('hit', 'ok') : ''),
                      simTd(Rshort(run.rows[i].running, 8))],
                     run.rows[i].hit ? 'focus' : null);
    }
    drawTable.innerHTML = '<caption>The first draws, and then every draw that hit the event. A draw that '
      + 'misses contributes nothing whatever its weight; a draw that hits contributes its whole weight, '
      + 'which is why one enormous weight is the entire variance of a bad q.</caption>'
      + simHead(['draw', 'heads', 'weight p / q', '', 'running estimate'])
      + '<tbody>' + (drows || simTr([simTdl('no draw in this run hit the event')])) + '</tbody>';

    document.getElementById('imTheta').textContent = Rtext(res.estimate);
    /* These variances span four orders of magnitude, so six decimal places
       prints the small one as 0.000008 -- which is the number the whole lesson
       turns on, reduced to one significant figure. Ten places carries four
       significant figures at 1e-6 and still reads at 9.3. */
    document.getElementById('imVarP').textContent = Rshort(res.varCrude, 10);
    document.getElementById('imVarQ').textContent = Rshort(res.varIS, 10);
    document.getElementById('imRatio').textContent = res.ratio === null ? '—' : Rfixed(res.ratio, 4);
    document.getElementById('imHits').textContent = run.hits + ' of ' + count;
    document.getElementById('imEst').textContent = Rshort(run.estimate, 8);

    var helps = res.ratio !== null && Rcmp(res.ratio, R1) > 0;
    var qHit = q[COINS][1];
    status.innerHTML = 'The event is ten heads, so its probability under the fair coin is exactly <strong>'
      + Rtext(res.estimate) + '</strong> — known, which is what makes this a measurement. Direct sampling '
      + 'has per-draw variance p(1 − p) = <strong>' + Rshort(res.varCrude, 10) + '</strong>. Under this q '
      + 'the event occurs with probability ' + Rshort(qHit, 6) + ', the weight on it is '
      + Rshort(Rdiv(p[COINS][1], qHit), 6) + ', and the per-draw variance is <strong>'
      + Rshort(res.varIS, 10) + '</strong>'
      + (res.ratio === null ? '.' : ' — the variance is '
          + (helps ? 'DIVIDED by <strong>' + Rtext(res.ratio) + '</strong> ≈ ' + Rfixed(res.ratio, 4)
                   : 'MULTIPLIED by <strong>' + Rtext(Rinv(res.ratio)) + '</strong> ≈ ' + Rfixed(Rinv(res.ratio), 4))
          + '.')
      + ' Both are exact fractions, and both estimators are unbiased for the same number: the estimate is '
      + 'not where the difference is.'
      + '<br />This run of ' + count + ' draws hit the event ' + run.hits + ' time'
      + (run.hits === 1 ? '' : 's') + ' and came out at ' + Rshort(run.estimate, 8) + '. '
      + (run.hits === 0
          ? 'Not one hit, so the estimate is exactly zero — not near the answer, AT zero, with nothing on '
            + 'the page to suggest anything went wrong except the variance figure. That is the failure mode '
            + 'this lesson leads with: a bad q looks fine on a short run because all of the damage is in '
            + 'the spread and none of it is in the picture.'
          : run.hits < 4
            ? 'A handful of hits over thousands of draws is what a rare event looks like when you sample '
              + 'the wrong distribution: almost every run is wasted, and the estimate is decided by two or '
              + 'three of them.'
            : 'Enough hits for the estimate to have something to stand on, which is the entire purpose of '
              + 'moving the sampling distribution.')
      + '<br />The two failures to avoid. Oversampling the interesting region and forgetting to weight is '
      + 'not an estimator of anything — it is an estimate of a probability under q, reported as one under '
      + 'p. And importance sampling most certainly can hurt: the bad q on the bar chart above is four '
      + 'orders of magnitude worse than direct sampling, from the same estimator, with the same '
      + 'unbiasedness. Same method, same event, and the choice of q is the whole difference.';
  }

  qSel.addEventListener('change', redraw);
  [drawS, seedS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Importance sampling for rare events",
        subtitle="Sample where the event is, weight each draw by p/q, and watch what happens to the variance",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose q, and read the variance column rather than the estimate"),
        panel_intro=cfg.get(
            "panel_intro",
            "The event is ten fair coins all landing heads, a probability of exactly 1/1024. The "
            "distribution actually sampled from is " + label + ". Both tables, every likelihood ratio "
            "and both variances are exact fractions, so the comparison is arithmetic rather than a "
            "story about which q feels better.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "sample": _sample,
    "montecarlo": _montecarlo,
    "bound": _bound,
    "des": _des,
    "warmup": _warmup,
    "crn": _crn,
    "antithetic": _antithetic,
    "control": _control,
    "importance": _importance,
}

MODES = tuple(sorted(_MODES))


def simulate_lab(cfg):
    """The simulation kit. `cfg["mode"]` chooses the lesson.

    An unknown mode raises, and so does an unknown preset. The raise is the
    contract rather than defensiveness: a kit that fell back to a default would
    render a finished-looking page carrying another lesson's widget, or the right
    lesson's widget opened on someone else's worked example. Both pass every
    markup assertion in the suite and both pass labcheck, because the lab builds
    and draws; the reader is simply shown the wrong arithmetic under the right
    title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "simulate_lab: unknown mode %r; the nine modes of this course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["simulate_lab", "MODES", "SIMBASE_JS", "SIMSURD_JS", "SIMDRAW_JS", "SIMSTAIR_JS",
           "SIMQ_JS", "SIMCHAIN_JS", "SIMBINOM_JS"]
