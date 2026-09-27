"""Course 8: Inventory Models -- one kit, seven modes, and no derivative.

THE ECONOMIC ORDER QUANTITY IS FOUND BY A DISCRIMINANT HERE, and that is not a
presentation choice. `content/operations_research/__init__.py` promises the
reader, in the prerequisites a course page prints, that this path uses no
calculus: "the economic order quantity is found by the discriminant of a
quadratic". So the route below is the route the page advertises.

    Is there an order quantity costing at most T?

        KD/Q + hQ/2 <= T   <=>   hQ^2/2 - TQ + KD <= 0

    a quadratic in Q with a positive leading coefficient. It dips below zero
    exactly when its discriminant T^2 - 2hKD is positive, its two roots are the
    ends of the interval of quantities that are cheap enough, and THE ROOTS
    MERGE exactly when the discriminant is zero -- at T = sqrt(2hKD), which is
    therefore the least achievable cost and the merged root Q = T/h = sqrt(2KD/h)
    is the only quantity that achieves it.

Nothing is differentiated, nothing is asserted, and the minimum arrives as a
consequence of two roots colliding. `or_core.eoqDiscriminant` is that argument
and mode `discriminant` is the reader driving it.

THE FLATNESS CLAIM IS THE SAME ARGUMENT AGAIN, and this kit computes it rather
than repeating it. The path's key line says "Q* = sqrt(2KD/h) and the cost curve
is flat either side of it". Ordering t times the EOQ costs (t + 1/t)/2 times the
minimum -- `or_core.eoqRatio`, exact at every rational t and free of K, D and h
-- so "within a fraction e of the minimum" is

        (t + 1/t)/2 <= 1 + e    <=>    t^2 - 2(1 + e)t + 1 <= 0

another quadratic, whose discriminant is 4e(2 + e) and whose roots are
(1 + e) +- sqrt(e(2 + e)).  `eoqBand` below returns that pair as an exact surd.
At e = 1/100 the band is [0.8682, 1.1518]: ordering 13% too little or 15% too
much costs one per cent. That is the flatness claim with numbers on it, and it
is a discriminant, not a second derivative.

WHAT ROUNDS, AND WHERE IT SAYS SO. Two of this path's four irrational quantities
are here -- the economic order quantity and its cost -- and they are carried as
exact surds {q, k} meaning q*sqrt(k) all the way to the point of printing.
`surdDec` in or_core.ORFMT_JS is the only function that rounds them, it takes
three guard digits and rounds once, and EVERY panel below that prints one calls
`roundedNote` beside it, which is the sentence naming the rounding and its
method. A page that printed 109.5445 without that sentence would have replaced a
fact the reader can check with a decimal they cannot.

Costs are compared with `surdValueCmp`, which does not round: same radicand by
one squaring, different radicands by rational brackets refined until they
separate. So "the deepest discount is cheapest" is a proof on the instance and
not a comparison of two decimals that happen to differ.

WHAT THIS KIT DOES NOT READ. `or_core.epqCost` returns a `bStar` field and mode
`epq` ignores it, deliberately: that field multiplies `Qstar.q`, the RATIONAL
FACTOR of the surd, so it is short by a factor of sqrt(k) whenever the optimal
run size is irrational, and its pi = 0 branch tests `backlog === R1` by object
identity and then adds h to h. `epqBestB` below computes the optimal backorder
level at a FIXED rational Q, where the answer is rational and the formula is
b = f Q h / (h + pi), and mode `epq` prints that. The defect is reported, not
patched here: or_core.py is shared by twelve kits.

The seven modes, one lesson each.

  eoq           the sawtooth, the two cost curves crossing, Q* as a surd, and
                the flatness band computed by the second discriminant
  discriminant  "is there a Q costing at most T" as a quadratic, its roots
                drawn, and the merge at T = C*
  discount      all-units price breaks: the DISCONTINUOUS total-cost curve, one
                candidate per band, and the winner chosen without rounding
  epq           a finite production rate and planned backorders as ONE formula,
                with the sawtooth redrawn as each is switched on
  newsvendor    the critical ratio against the whole tabulated cost curve
  reorder       lead-time demand by convolution, the expected shortage, and
                cycle service against FILL RATE, which is not the same number
  review        periodic review over R + L periods, and why it is R + L
"""

import json

from .algebra_core import RATIONAL_JS, SURD_JS
from .algebra_systems import FORMAT_JS
from .common import Lab
from .or_core import INV_JS, ORFMT_JS
from .sysdesign_core import PMF_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no DOM: scripts/mathcheck.js
# extracts this block and calls every one of them, including the three that draw
# -- they return strings of SVG rather than touching an element, so what the
# reader sees is assertable and not merely describable.
# ---------------------------------------------------------------------------

INVKIT_JS = r"""
  /* ------------------------------------------------------------- reading in

     Every number a reader types goes through FORMAT_JS's Rread, so "7/2" is
     exact and "banana" is null rather than NaN. `invPositive` is the guard the
     models need: K, D, h and P are rates and quantities, and a zero or negative
     one is not a small model, it is no model. */
  function invRead(text) { return Rread(text); }
  function invPositive(text) {
    var v = Rread(text);
    return (v === null || Rsign(v) <= 0) ? null : v;
  }
  function invNonNegative(text) {
    var v = Rread(text);
    return (v === null || Rsign(v) < 0) ? null : v;
  }
  /* A rational as a plain number, for coordinates only. Rnum goes through
     Number and this path produces rationals Number cannot hold, so the decimal
     comes from Rfixed's BigInt long division and is parsed back. Nothing
     downstream of a coordinate is arithmetic. */
  function pxOf(r) { return parseFloat(Rfixed(r, 6)); }

  /* -------------------------------------------------- the EOQ, split in two

     The two halves of the cost are the lesson: ordering falls like KD/Q and
     holding rises like hQ/2, so the total has a minimum where neither term is
     small. Split rather than summed, because the crossing IS the optimum and a
     reader should see the two lines meet. */
  function eoqSplit(Q, K, D, h) {
    if (Rzero(Q)) return null;
    var order = Rdiv(Rmul(K, D), Q), hold = Rdiv(Rmul(h, Q), R(2n, 1n));
    return { Q: Q, order: order, hold: hold, total: Radd(order, hold),
             crossing: Requ(order, hold) };
  }
  /* The curve on a rational grid. `n` samples across [lo, hi], every one an
     exact rational, so the drawn shape and the printed table are the same
     numbers. */
  function eoqCurve(K, D, h, lo, hi, n) {
    var out = [], i, span = Rsub(hi, lo);
    for (i = 0; i <= n; i += 1) {
      var Q = Radd(lo, Rmul(span, R(BigInt(i), BigInt(n))));
      var pt = eoqSplit(Q, K, D, h);
      if (pt !== null) out.push(pt);
    }
    return out;
  }

  /* THE FLATNESS BAND, BY THE SECOND DISCRIMINANT.

     C(t Q*) / C* = (t + 1/t)/2 exactly, for every rational t and whatever K, D
     and h were -- that is `eoqRatio` in or_core. So "costs at most (1 + e)
     times the minimum" is

         (t + 1/t)/2 <= 1 + e   <=>   t^2 - 2(1 + e) t + 1 <= 0

     and the ends of the band are the roots of a quadratic with RATIONAL
     coefficients: (1 + e) +- sqrt(e(2 + e)). No calculus, no sampling, and the
     answer is a surd rather than a pair of decimals. */
  function eoqBand(e) {
    if (Rsign(e) < 0) return null;
    var one = R(1n, 1n), two = R(2n, 1n);
    var qr = quadroots(one, Rneg(Rmul(two, Radd(one, e))), one);
    /* THE ENDS ARE SURDS, not rationals, and they are carried as such. Writing
       p +- s.q here and calling it the answer would drop the sqrt(s.k) -- which
       is exactly the defect this kit reports in or_core's `bStar`, and it is
       easier to commit than to notice: at e = 1/100 the wrong form gives a band
       of [1.00, 1.02] and the right one [0.8682, 1.1518]. */
    return { disc: qr.disc, p: qr.p, s: qr.s, kind: qr.kind, tolerance: e,
             lo: surdValue(qr.p, { q: Rneg(qr.s.q), k: qr.s.k }),
             hi: surdValue(qr.p, { q: qr.s.q, k: qr.s.k }),
             exact: qr.s.k === 1n,
             why: 'the band is the interval where t^2 - 2(1 + ' + Rtext(e) + ')t + 1 <= 0, whose '
               + 'discriminant is ' + Rtext(qr.disc) + ' -- so the ends are ' + Rtext(qr.p)
               + ' +- sqrt(' + Rtext(Rmul(e, Radd(two, e))) + '), and not one of K, D or h appears in it' };
  }

  /* ---- rational brackets, for the products that are not one surd ---------

     t_+ times Q* is (a + b sqrt(m)) times (c sqrt(k)), which has TWO radicands
     and is therefore not a surd this module can carry. Rather than pretend, the
     page brackets each factor by rationals from `surdBounds` at a stated
     precision and multiplies the brackets. The printed decimal is the midpoint
     of a bracket whose width is under 10^-14 of the value, so every digit shown
     is a digit of the true number -- which is a proof about the printing, not a
     hope about it. */
  function bndOf(v, p) { return surdBounds(v, p === undefined ? 16 : p); }
  function bndMul(a, b) {
    /* both intervals strictly positive, which every caller here checks */
    return [Rmul(a[0], b[0]), Rmul(a[1], b[1])];
  }
  function bndScale(a, r) {
    return Rsign(r) >= 0 ? [Rmul(a[0], r), Rmul(a[1], r)] : [Rmul(a[1], r), Rmul(a[0], r)];
  }
  function bndFrom(r, a) { return [Rsub(r, a[1]), Rsub(r, a[0])]; }
  function bndDec(a, places) {
    return Rfixed(Rdiv(Radd(a[0], a[1]), R(2n, 1n)), places === undefined ? 4 : places);
  }
  function bndWidth(a) { return Rsub(a[1], a[0]); }

  /* The same band expressed in order quantities: t times the EOQ. */
  function eoqBandQ(K, D, h, e) {
    var band = eoqBand(e);
    if (band === null) return null;
    var star = eoq(K, D, h), q = star.Qsurd;
    if (Rzero(q.q)) return null;
    var qb = bndOf(surdValue(R0, q));
    var loB = bndOf(band.lo), hiB = bndOf(band.hi);
    var one = R(1n, 1n), hundred = R(100n, 1n);
    return { band: band, Qsurd: q, loT: loB, hiT: hiB,
             loBand: bndMul(loB, qb), hiBand: bndMul(hiB, qb),
             loValue: bndDec(bndMul(loB, qb), 4), hiValue: bndDec(bndMul(hiB, qb), 4),
             belowPct: bndDec(bndScale(bndFrom(one, loB), hundred), 1),
             abovePct: bndDec(bndScale([Rsub(hiB[0], one), Rsub(hiB[1], one)], hundred), 1),
             star: surdDec(q, 4), exactEnds: band.exact,
             why: band.exact
               ? 'the ends of the band are rational multiples of the EOQ'
               : 'the ends of the band are ' + Rtext(band.s.q) + ' sqrt(' + band.s.k + ') either side of '
                 + Rtext(band.p) + ' times the EOQ, so both are printed from a rational bracket' };
  }
  /* Comparing a rational cost at a rational Q with the IRRATIONAL minimum,
     exactly. surdValueCmp does not round: this is the function that lets the
     page say "this Q costs strictly more than the minimum" as a fact. */
  function eoqAbove(Q, K, D, h) {
    var here = eoqCostAt(Q, K, D, h);
    if (here === null) return null;
    var star = eoq(K, D, h);
    var cmp = surdValueCmp(surdValue(here, { q: R0, k: 1n }), surdValue(R0, star.costSurd));
    return { at: here, cmp: cmp, star: star.costSurd,
             why: cmp > 0 ? 'costs strictly more than the minimum, proved by comparing squares rather than decimals'
                 : (cmp === 0 ? 'costs exactly the minimum, so this Q is the EOQ and the EOQ is rational here'
                    : 'costs LESS than the minimum, which cannot happen and means the arithmetic is wrong') };
  }
  /* The cheapest WHOLE order quantity in [lo, hi], by looking at every one of
     them. The formula gives a real number and a warehouse orders an integer, so
     the page shows the scan beside the surd and the reader sees that rounding
     the surd to the nearer whole number is the answer -- which is a claim, and
     this is the check of it. */
  function eoqWholeScan(K, D, h, lo, hi) {
    var best = null, bestQ = 0, q;
    for (q = lo; q <= hi; q += 1) {
      var c = eoqCostAt(R(BigInt(q), 1n), K, D, h);
      if (c === null) continue;
      if (best === null || Rcmp(c, best) < 0) { best = c; bestQ = q; }
    }
    if (best === null) return null;
    return { Q: bestQ, cost: best, scanned: hi - lo + 1,
             why: 'every whole quantity from ' + lo + ' to ' + hi + ' was priced; the cheapest is '
               + bestQ + ' at ' + Rtext(best) };
  }

  /* --------------------------------------------- the sawtooth, as a polyline

     Stock arrives in a batch of Q and drains at D. The average on hand is Q/2
     BECAUSE the sawtooth is straight, which is the model's one real assumption
     and the drawing is where a reader can see it. Returns points in cycle
     units: x in [0, cycles], y in stock. */
  function sawPoints(Q, D, cycles) {
    var pts = [], c;
    if (Rzero(Q) || Rzero(D)) return pts;
    for (c = 0; c < cycles; c += 1) {
      pts.push([c, pxOf(Q)]);
      pts.push([c + 1, 0]);
    }
    return pts;
  }
  /* The production sawtooth: stock builds at P - D for the first fraction D/P
     of the cycle, then drains at D; with planned backorders the whole shape
     drops by b. One polyline, four corners a cycle, and with P infinite and
     b = 0 it IS the plain sawtooth -- the two named models are readings of one
     picture, which is the lesson. */
  function epqPoints(Q, b, D, P, cycles) {
    var pts = [], c;
    if (Rzero(Q) || Rzero(D)) return pts;
    var f = P === null ? R1 : Rsub(R1, Rdiv(D, P));
    if (Rsign(f) <= 0) return pts;
    var peak = pxOf(Rsub(Rmul(f, Q), b)), low = -pxOf(b);
    /* the fraction of a cycle spent producing is D/P, or zero when P is
       infinite; the peak is reached at the end of it */
    var up = P === null ? 0 : pxOf(Rdiv(D, P));
    var riseFrom = low, riseTo = peak;
    for (c = 0; c < cycles; c += 1) {
      pts.push([c, riseFrom]);
      pts.push([c + up, riseTo]);
      pts.push([c + 1, low]);
    }
    return pts;
  }

  /* -------------------------------------------------- all-units price breaks

     The total cost is DISCONTINUOUS at every break, because the whole order is
     repriced and not just the units above the break. `bandOf` is the step
     function that makes it so, and drawing the curve band by band rather than
     as one polyline is the only honest way to draw it: a line joining the two
     sides of a break asserts costs that no quantity has. */
  function bandOf(breaks, Q) {
    var at = -1, i;
    for (i = 0; i < breaks.length; i += 1) if (Rcmp(Q, breaks[i].from) >= 0) at = i;
    return at;
  }
  function allUnitsCostAt(breaks, K, D, h, Q) {
    var at = bandOf(breaks, Q);
    if (at < 0 || Rzero(Q)) return null;
    var band = breaks[at], hb = band.h || h;
    var cycle = eoqCostAt(Q, K, D, hb);
    if (cycle === null) return null;
    return { band: at, price: band.price, buy: Rmul(D, band.price),
             cycle: cycle, total: Radd(Rmul(D, band.price), cycle) };
  }
  /* One polyline per band, so the jumps stay jumps. */
  function discountCurve(breaks, K, D, h, lo, hi, n) {
    var series = [], i, j;
    for (i = 0; i < breaks.length; i += 1) {
      var from = Rcmp(breaks[i].from, lo) > 0 ? breaks[i].from : lo;
      var to = i + 1 < breaks.length ? breaks[i + 1].from : hi;
      if (Rcmp(to, hi) > 0) to = hi;
      if (Rcmp(from, to) >= 0) continue;
      var pts = [], span = Rsub(to, from);
      for (j = 0; j <= n; j += 1) {
        var Q = Radd(from, Rmul(span, R(BigInt(j), BigInt(n))));
        var c = allUnitsCostAt(breaks, K, D, h, Q);
        /* the top end of a band belongs to the NEXT band, so it is priced here
           at this band's price to draw the open end of the segment */
        if (c === null) continue;
        var hb = breaks[i].h || h, cyc = eoqCostAt(Q, K, D, hb);
        pts.push([pxOf(Q), pxOf(Radd(Rmul(D, breaks[i].price), cyc))]);
      }
      series.push({ band: i, pts: pts, price: breaks[i].price });
    }
    return series;
  }
  /* Every whole quantity in range, priced under the all-units rule. This is the
     page's own check on `discountCandidates`: one candidate per band is a CLAIM
     that the cheapest quantity is either a band's EOQ or a band's floor, and a
     scan of the range is what makes it a checked claim rather than a rule. */
  function discountScan(breaks, K, D, h, lo, hi) {
    var best = null, bestQ = 0, q;
    for (q = lo; q <= hi; q += 1) {
      var c = allUnitsCostAt(breaks, K, D, h, R(BigInt(q), 1n));
      if (c === null) continue;
      if (best === null || Rcmp(c.total, best) < 0) { best = c.total; bestQ = q; }
    }
    return best === null ? null : { Q: bestQ, cost: best, scanned: hi - lo + 1 };
  }

  /* ----------------------------------------------- production and backorders

     At a FIXED rational Q the best backorder level is rational and it is
     b = f Q h / (h + pi) -- a quadratic in b with rational coefficients, whose
     vertex is that ratio. So this kit prints a number it can carry exactly,
     rather than reading or_core's `bStar`, which multiplies the RATIONAL FACTOR
     of an irrational Q* and is short by sqrt(k) whenever the run size is
     irrational. */
  function epqBestB(Q, K, D, h, P, pi) {
    var f = P === null ? R1 : Rsub(R1, Rdiv(D, P));
    if (Rsign(f) <= 0 || Rzero(Q)) return null;
    if (pi === null || Rzero(pi)) {
      return { b: R0, f: f, feasible: false,
               why: 'with no backorder penalty the model has no finite optimum -- every unit backordered '
                 + 'is free, so b = 0 is shown and the panel says the model has run out' };
    }
    var b = Rdiv(Rmul(Rmul(f, Q), h), Radd(h, pi));
    return { b: b, f: f, feasible: true,
             cost: epqCostAt(Q, b, K, D, h, P, pi),
             why: 'at Q = ' + Rtext(Q) + ' the cost is a quadratic in b whose vertex is f Q h / (h + pi) = '
               + Rtext(b) };
  }
  /* The cost profile against Q, with b already at its best for each Q. The
     minimum of THIS curve is the surd or_core's epqCost returns, and the page
     draws them together so the reader sees the surd sitting at the bottom of a
     curve computed without it. */
  function epqProfile(K, D, h, P, pi, lo, hi, n) {
    var out = [], i, span = Rsub(hi, lo);
    for (i = 0; i <= n; i += 1) {
      var Q = Radd(lo, Rmul(span, R(BigInt(i), BigInt(n))));
      var best = epqBestB(Q, K, D, h, P, pi);
      if (best === null) continue;
      var b = best.feasible ? best.b : R0;
      var c = epqCostAt(Q, b, K, D, h, P, pi);
      if (c === null) continue;
      out.push({ Q: Q, b: b, cost: c });
    }
    return out;
  }

  /* --------------------------------------------------------- the newsvendor

     or_core's `newsvendor` tabulates the cost at every Q IN THE SUPPORT of the
     demand distribution, which is where the answer is. It is not where a reader
     looks first: they try 0, they try one more than the largest demand, and
     they want to know those are worse. `nvWiden` prices every whole Q in a
     window, support or not, so "the crossing is the minimum" is a statement
     about the whole line and not about five of its points. */
  function nvCostAt(pmf, cu, co, Q) {
    var over = R0, under = R0, j;
    for (j = 0; j < pmf.length; j += 1) {
      var d = pmf[j][0];
      if (d < Q) over = Radd(over, Rmul(pmf[j][1], R(BigInt(Q - d), 1n)));
      else under = Radd(under, Rmul(pmf[j][1], R(BigInt(d - Q), 1n)));
    }
    return { Q: Q, over: over, under: under, cost: Radd(Rmul(co, over), Rmul(cu, under)) };
  }
  function nvWiden(pmf, cu, co, lo, hi) {
    var rows = [], q, best = null;
    for (q = lo; q <= hi; q += 1) {
      var row = nvCostAt(pmf, cu, co, q);
      rows.push(row);
      if (best === null || Rcmp(row.cost, rows[best].cost) < 0) best = rows.length - 1;
    }
    return { rows: rows, best: best, Q: rows.length ? rows[best].Q : null };
  }

  /* ------------------------------------------- service, and the other service

     CYCLE SERVICE is the probability a cycle ends without a stockout. FILL RATE
     is the fraction of DEMAND met from stock. They are different numbers and
     readers quote whichever they met first: at a reorder point that runs 3/8 of
     a unit short per cycle on an order of 100, cycle service might be 7/8 while
     the fill rate is 1 - (3/8)/100 = 0.99625. Both are printed, side by side,
     with their definitions, because a service level without its definition is
     not a number. */
  function serviceRows(pmf, L, lo, hi) {
    var out = [], r;
    for (r = lo; r <= hi; r += 1) out.push(reorderPoint(pmf, L, r));
    return out;
  }
  function fillRate(pmf, L, r, Q) {
    if (Rzero(Q)) return null;
    var rp = reorderPoint(pmf, L, r);
    return { fill: Rsub(R1, Rdiv(rp.shortage, Q)), cycle: rp.cycleService,
             shortage: rp.shortage, safety: rp.safety,
             why: 'cycle service is P(no stockout in a cycle) = ' + Rtext(rp.cycleService)
               + '; the fill rate is the fraction of demand met from stock, 1 - (' + Rtext(rp.shortage)
               + ')/' + Rtext(Q) + ' = ' + Rtext(Rsub(R1, Rdiv(rp.shortage, Q)))
               + ' -- the same policy, two different service levels' };
  }
  /* The smallest reorder point that reaches a cycle-service target. Monotone in
     r, so the first that clears it is the answer; -1 when none in range does. */
  function smallestReorder(pmf, L, alpha, limit) {
    var r;
    for (r = 0; r <= limit; r += 1) {
      if (Rcmp(reorderPoint(pmf, L, r).cycleService, alpha) >= 0) return r;
    }
    return -1;
  }

  /* ------------------------------------------------------- drawing, as text

     Three functions, each returning a string of SVG. Nothing here touches an
     element, so scripts/mathcheck.js asserts on the drawing itself rather than
     on a description of it -- the reason the rest of this path writes its
     renderers this way. */
  function plotFrame(series, box) {
    var x0 = null, x1 = null, y0 = 0, y1 = null, s, p;
    for (s = 0; s < series.length; s += 1) {
      for (p = 0; p < series[s].pts.length; p += 1) {
        var pt = series[s].pts[p];
        if (x0 === null || pt[0] < x0) x0 = pt[0];
        if (x1 === null || pt[0] > x1) x1 = pt[0];
        if (pt[1] < y0) y0 = pt[1];
        if (y1 === null || pt[1] > y1) y1 = pt[1];
      }
    }
    if (x0 === null) return null;
    if (x1 === x0) x1 = x0 + 1;
    if (y1 === null || y1 === y0) y1 = y0 + 1;
    var L = box.left === undefined ? 52 : box.left, Rr = box.right === undefined ? 14 : box.right;
    var T = box.top === undefined ? 12 : box.top, B = box.bottom === undefined ? 26 : box.bottom;
    var w = box.w - L - Rr, hgt = box.h - T - B;
    return { x0: x0, x1: x1, y0: y0, y1: y1, L: L, T: T, w: w, h: hgt,
             sx: function (v) { return L + w * (v - x0) / (x1 - x0); },
             sy: function (v) { return T + hgt - hgt * (v - y0) / (y1 - y0); } };
  }
  function plotSvg(series, box, opts) {
    opts = opts || {};
    var f = plotFrame(series, box);
    if (f === null) return '<text x="14" y="24" font-size="11" fill="var(--muted)">nothing to draw</text>';
    var out = '<line x1="' + f.L + '" y1="' + (f.T + f.h) + '" x2="' + (f.L + f.w) + '" y2="' + (f.T + f.h)
      + '" stroke="var(--line-strong)" />'
      + '<line x1="' + f.L + '" y1="' + f.T + '" x2="' + f.L + '" y2="' + (f.T + f.h)
      + '" stroke="var(--line-strong)" />';
    if (f.y0 < 0) {
      out += '<line x1="' + f.L + '" y1="' + f.sy(0) + '" x2="' + (f.L + f.w) + '" y2="' + f.sy(0)
        + '" stroke="var(--line)" stroke-dasharray="3 3" />';
    }
    var s, p;
    for (s = 0; s < series.length; s += 1) {
      var sr = series[s], d = '';
      for (p = 0; p < sr.pts.length; p += 1) {
        d += (p ? ' L ' : 'M ') + f.sx(sr.pts[p][0]).toFixed(2) + ' ' + f.sy(sr.pts[p][1]).toFixed(2);
      }
      if (!d) continue;
      out += '<path d="' + d + '" fill="none" stroke="var(--' + (sr.tone || 'cyan') + ')" stroke-width="'
        + (sr.width || 2) + '"' + (sr.dash ? ' stroke-dasharray="' + sr.dash + '"' : '') + ' />';
    }
    var marks = opts.marks || [];
    for (s = 0; s < marks.length; s += 1) {
      var m = marks[s];
      if (m.kind === 'v') {
        out += '<line x1="' + f.sx(m.at).toFixed(2) + '" y1="' + f.T + '" x2="' + f.sx(m.at).toFixed(2)
          + '" y2="' + (f.T + f.h) + '" stroke="var(--' + (m.tone || 'amber')
          + ')" stroke-width="1.5" stroke-dasharray="4 3" />';
      } else {
        out += '<circle cx="' + f.sx(m.at).toFixed(2) + '" cy="' + f.sy(m.y).toFixed(2)
          + '" r="4" fill="var(--' + (m.tone || 'amber') + ')" />';
      }
      if (m.label) {
        out += '<text x="' + Math.min(f.L + f.w - 4, f.sx(m.at) + 5).toFixed(2) + '" y="'
          + (m.kind === 'v' ? f.T + 12 : f.sy(m.y) - 8).toFixed(2)
          + '" font-size="10" fill="var(--' + (m.tone || 'amber') + ')">' + m.label + '</text>';
      }
    }
    if (opts.bandFrom !== undefined && opts.bandTo !== undefined) {
      var bx = f.sx(opts.bandFrom), bw = f.sx(opts.bandTo) - bx;
      out = '<rect x="' + bx.toFixed(2) + '" y="' + f.T + '" width="' + bw.toFixed(2) + '" height="' + f.h
        + '" fill="var(--green)" opacity="0.12" />' + out;
    }
    out += '<text x="' + f.L + '" y="' + (box.h - 8) + '" font-size="10" fill="var(--muted)">'
      + (opts.xlo === undefined ? f.x0 : opts.xlo) + '</text>'
      + '<text x="' + (f.L + f.w) + '" y="' + (box.h - 8) + '" font-size="10" fill="var(--muted)" '
      + 'text-anchor="end">' + (opts.xhi === undefined ? f.x1 : opts.xhi) + '</text>'
      + '<text x="4" y="' + (f.T + 9) + '" font-size="10" fill="var(--muted)">'
      + (opts.yhi === undefined ? '' : opts.yhi) + '</text>'
      + '<text x="4" y="' + (f.T + f.h) + '" font-size="10" fill="var(--muted)">'
      + (opts.ylo === undefined ? '' : opts.ylo) + '</text>';
    if (opts.xlabel) {
      out += '<text x="' + (f.L + f.w / 2) + '" y="' + (box.h - 8) + '" font-size="10" fill="var(--muted)" '
        + 'text-anchor="middle">' + opts.xlabel + '</text>';
    }
    return out;
  }
  /* A pmf as bars, with a marker at one value. Used by three modes, which is
     why it is one function and not three. */
  function barsSvg(pairs, box, opts) {
    opts = opts || {};
    if (!pairs.length) return '<text x="14" y="24" font-size="11" fill="var(--muted)">no distribution</text>';
    var L = 40, T = 12, B = 26, w = box.w - L - 14, hgt = box.h - T - B;
    var top = R0, i;
    for (i = 0; i < pairs.length; i += 1) if (Rcmp(pairs[i][1], top) > 0) top = pairs[i][1];
    var peak = pxOf(top) || 1;
    var slot = w / pairs.length, out = '';
    out += '<line x1="' + L + '" y1="' + (T + hgt) + '" x2="' + (L + w) + '" y2="' + (T + hgt)
      + '" stroke="var(--line-strong)" />';
    for (i = 0; i < pairs.length; i += 1) {
      var bh = hgt * pxOf(pairs[i][1]) / peak;
      var tone = 'cyan';
      if (opts.markAt !== undefined && pairs[i][0] === opts.markAt) tone = 'amber';
      else if (opts.shortAbove !== undefined && pairs[i][0] > opts.shortAbove) tone = 'red';
      out += '<rect x="' + (L + i * slot + 1.5).toFixed(2) + '" y="' + (T + hgt - bh).toFixed(2)
        + '" width="' + Math.max(1, slot - 3).toFixed(2) + '" height="' + bh.toFixed(2)
        + '" rx="2" fill="var(--' + tone + ')" opacity="0.85" />';
      if (pairs.length <= 24) {
        out += '<text x="' + (L + i * slot + slot / 2).toFixed(2) + '" y="' + (T + hgt + 13)
          + '" font-size="9" fill="var(--muted)" text-anchor="middle">' + pairs[i][0] + '</text>';
      }
    }
    if (opts.markAt !== undefined) {
      var at = -1;
      for (i = 0; i < pairs.length; i += 1) if (pairs[i][0] === opts.markAt) at = i;
      if (at >= 0) {
        out += '<line x1="' + (L + at * slot + slot / 2).toFixed(2) + '" y1="' + T + '" x2="'
          + (L + at * slot + slot / 2).toFixed(2) + '" y2="' + (T + hgt)
          + '" stroke="var(--amber)" stroke-width="1.5" stroke-dasharray="4 3" />'
          + '<text x="' + (L + at * slot + slot / 2 + 5).toFixed(2) + '" y="' + (T + 11)
          + '" font-size="10" fill="var(--amber)">' + (opts.markLabel || '') + '</text>';
      }
    }
    out += '<text x="4" y="' + (T + 9) + '" font-size="10" fill="var(--muted)">' + Rshort(top) + '</text>'
      + '<text x="4" y="' + (T + hgt) + '" font-size="10" fill="var(--muted)">0</text>';
    return out;
  }
  /* The sentence that has to sit beside every rounded figure on this kit's
     pages. One function, so it cannot be worded two ways or forgotten in one
     place -- and mathcheck asserts that each mode that prints a surd calls it. */
  function roundedNote(places) {
    return 'rounded to ' + places + ' decimal places from the exact surd, by integer square root with '
      + 'three guard digits &mdash; the surd itself is exact and is printed beside it';
  }
"""

_CORE_JS = RATIONAL_JS + SURD_JS + FORMAT_JS + PMF_JS + ORFMT_JS + INV_JS + INVKIT_JS


# ---------------------------------------------------------------------------
# The worked examples. Every preset is typed the way a reader types it, so the
# lab parses its own presets through the same path a reader's edit takes.
#
# `workshop` is the instance whose EOQ is RATIONAL -- 200 exactly, costing 1200
# -- which is the only kind of instance on which a reader can check every digit
# by hand. `bench` is the instance whose EOQ is IRRATIONAL, 20*sqrt(30), and it
# exists so that the rounding is met on a page rather than described on one.
# ---------------------------------------------------------------------------

EOQ_PRESETS = {
    "workshop": {
        "label": "A workshop: the EOQ comes out whole",
        "K": "100", "D": "1200", "h": "6", "unit": "brackets",
    },
    "bench": {
        "label": "A bench: the EOQ is irrational and stays a surd",
        "K": "50", "D": "600", "h": "5", "unit": "castings",
    },
    "bulk": {
        "label": "A bulk line: a large order and a small holding rate",
        "K": "400", "D": "9000", "h": "3", "unit": "drums",
    },
}

DISCOUNT_PRESETS = {
    "threeband": {
        "label": "Three price bands, holding charged as a fraction of price",
        "K": "40", "D": "1200",
        "breaks": "0 10 2; 500 9 9/5; 1000 8 8/5",
    },
    "twoband": {
        "label": "One break, and the discount is not worth taking",
        "K": "40", "D": "1200",
        "breaks": "0 10 2; 900 39/4 39/20",
    },
}

EPQ_PRESETS = {
    "machine": {
        "label": "A machine producing at twice demand, backorders penalised at h",
        "K": "100", "D": "1200", "h": "6", "P": "2400", "pi": "6",
    },
    "fast": {
        "label": "A fast line: production barely constrains the cycle",
        "K": "100", "D": "1200", "h": "6", "P": "12000", "pi": "3",
    },
    "tight": {
        "label": "Production only a fifth above demand",
        "K": "100", "D": "1200", "h": "6", "P": "1440", "pi": "12",
    },
}

NV_PRESETS = {
    "papers": {
        "label": "A stall: five demand outcomes, underage 7 and overage 3",
        "pmf": "0 1/10; 1 2/10; 2 3/10; 3 3/10; 4 1/10",
        "cu": "7", "co": "3",
    },
    "pastries": {
        "label": "A bakery: overage dominates, so the order shrinks",
        "pmf": "8 1/8; 9 1/4; 10 1/4; 11 1/4; 12 1/8",
        "cu": "2", "co": "5",
    },
    "spares": {
        "label": "A spare part: a stockout costs twenty times the leftover",
        "pmf": "0 1/2; 1 1/4; 2 1/8; 3 1/16; 4 1/16",
        "cu": "20", "co": "1",
    },
}

REORDER_PRESETS = {
    "steady": {
        "label": "Demand 0, 1 or 2 a period, lead time two periods",
        "pmf": "0 1/4; 1 1/2; 2 1/4", "L": 2, "r": 2, "Q": "100",
    },
    "lumpy": {
        "label": "Lumpy demand: mostly nothing, occasionally four",
        "pmf": "0 3/5; 1 1/5; 4 1/5", "L": 3, "r": 4, "Q": "60",
    },
}


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on the path uses.
# ---------------------------------------------------------------------------


def _payload(name, values):
    """Embed a JS literal. The escape makes "</script>" structurally impossible."""
    return "  var %s = %s;\n" % (name, json.dumps(values).replace("</", "<\\/"))


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
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>\n' % (cid, text)


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
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


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


def _preset(cfg, presets, mode, default):
    chosen = cfg.get("preset", default)
    if chosen not in presets:
        raise ValueError(
            "inventory_lab: mode %r has no preset %r; the presets are %s"
            % (mode, chosen, ", ".join(sorted(presets)))
        )
    return chosen, presets[chosen]


# ---------------------------------------------------------------------------
# Mode `eoq` -- the sawtooth, the two curves crossing, and the flat band
# ---------------------------------------------------------------------------


def _eoq(cfg):
    chosen, here = _preset(cfg, EOQ_PRESETS, "eoq", "workshop")

    markup = (
        _toolbar(
            "Two costs pulling opposite ways",
            "ordering falls like K&middot;D/Q, holding rises like h&middot;Q/2",
            [
                ("cyan", "ordering cost"),
                ("purple", "holding cost"),
                ("green", "their total"),
                ("amber", "the EOQ, and the band within 1% of it"),
            ],
        )
        + _stage(_svg("ivCurve", "0 0 660 240",
                      "Ordering cost, holding cost and their total against the order quantity, with the "
                      "economic order quantity marked and the band that costs at most one per cent more shaded."))
        + _stage(_svg("ivSaw", "0 0 660 150",
                      "Stock on hand over four cycles: a batch arrives, the level falls in a straight line to "
                      "zero, and the next batch arrives."))
        + _table("ivGrid")
        + _banner("ivStatus")
    )
    controls = (
        _select("ivPreset", "Worked example",
                [(k, EOQ_PRESETS[k]["label"]) for k in ("workshop", "bench", "bulk")], chosen)
        + _text("ivK", "Ordering cost K, per order", here["K"])
        + _text("ivD", "Demand D, per unit time", here["D"])
        + _text("ivH", "Holding cost h, per unit per unit time", here["h"])
        + _range("ivQ", "Order quantity Q to price", 1, 800, 200, 1)
        + _range("ivTol", "Band: within this many per cent of the minimum", 1, 25, 1, 1)
        + _kpis(
            [
                ("Q* exactly", "ivQstarK"),
                ("Q* rounded", "ivQdecK"),
                ("C* exactly", "ivCstarK"),
                ("C* rounded", "ivCdecK"),
                ("Cost at your Q", "ivAtK"),
                ("Cheapest whole Q", "ivWholeK"),
            ]
        )
        + _hint(
            "ivHint",
            "The two costs cross where the total is least, and that is not a coincidence: "
            "K&middot;D/Q = h&middot;Q/2 rearranges to Q&sup2; = 2KD/h. Slide Q away from the "
            "optimum and watch the total barely move &mdash; the shaded band is every quantity "
            "costing at most one per cent more than the best one, computed from a discriminant "
            "rather than sampled.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", EOQ_PRESETS) + r"""
  var presetS = document.getElementById('ivPreset');
  var kIn = document.getElementById('ivK');
  var dIn = document.getElementById('ivD');
  var hIn = document.getElementById('ivH');
  var qS = document.getElementById('ivQ');
  var tolS = document.getElementById('ivTol');
  var curveEl = document.getElementById('ivCurve');
  var sawEl = document.getElementById('ivSaw');
  var gridEl = document.getElementById('ivGrid');
  var statusEl = document.getElementById('ivStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    curveEl.innerHTML = ''; sawEl.innerHTML = ''; gridEl.innerHTML = '';
    ['ivQstarK', 'ivQdecK', 'ivCstarK', 'ivCdecK', 'ivAtK', 'ivWholeK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var K = invPositive(kIn.value), D = invPositive(dIn.value), h = invPositive(hIn.value);
    if (K === null || D === null || h === null) {
      blank('K, D and h each have to be a positive number or fraction such as 7/2. A zero or negative '
        + 'one is not a small model, it is no model: the cost would have no minimum.');
      return;
    }
    var star = eoq(K, D, h), Qs = star.Qsurd;
    var rational = Qs.k === 1n;

    /* The whole curve is sampled EXACTLY, on rationals, and then turned into
       coordinates -- never the other way round. */
    var qMax = Math.max(8, Math.round(parseFloat(surdDec(Qs, 2)) * 2.6));
    qS.max = String(qMax);
    var Q = R(BigInt(Math.max(1, Math.min(qMax, +qS.value || 1))), 1n);
    document.getElementById('ivQOut').textContent = Rtext(Q);
    var lo = R(1n, 1n), hi = R(BigInt(qMax), 1n);
    var pts = eoqCurve(K, D, h, lo, hi, 90);
    var order = { tone: 'cyan', pts: [] }, hold = { tone: 'purple', pts: [] }, total = { tone: 'green', pts: [], width: 2.4 };
    for (var i = 0; i < pts.length; i += 1) {
      var x = pxOf(pts[i].Q);
      order.pts.push([x, pxOf(pts[i].order)]);
      hold.pts.push([x, pxOf(pts[i].hold)]);
      total.pts.push([x, pxOf(pts[i].total)]);
    }
    var e = R(BigInt(Math.max(1, +tolS.value || 1)), 100n);
    document.getElementById('ivTolOut').textContent = Rpct(e, 0);
    var bandQ = eoqBandQ(K, D, h, e);
    var starX = parseFloat(surdDec(Qs, 4)), starY = parseFloat(surdDec(star.costSurd, 4));
    curveEl.innerHTML = plotSvg([order, hold, total], { w: 660, h: 240 }, {
      marks: [{ kind: 'p', at: starX, y: starY, tone: 'amber', label: 'Q*' },
              { kind: 'p', at: pxOf(Q), y: pxOf(eoqCostAt(Q, K, D, h)), tone: 'red', label: 'your Q' }],
      bandFrom: parseFloat(bandQ.loValue), bandTo: parseFloat(bandQ.hiValue),
      xlo: '1', xhi: String(qMax), xlabel: 'order quantity Q', ylo: '0',
      yhi: 'cost per unit time'
    });

    /* The sawtooth at the reader's Q, not at Q*: the picture has to move when
       the control does, or it is decoration. */
    sawEl.innerHTML = plotSvg([{ tone: 'cyan', pts: sawPoints(Q, D, 4), width: 2 }], { w: 660, h: 150 }, {
      marks: [{ kind: 'v', at: 1, tone: 'muted', label: 'one cycle' }],
      xlo: '0', xhi: '4 cycles', ylo: '0', yhi: 'Q = ' + Rtext(Q),
      xlabel: 'time, in cycles of length Q/D = ' + Rshort(Rdiv(Q, D))
    });

    /* The table is the same numbers the curve was drawn from, at a handful of
       quantities around the optimum, so the drawing can be checked by reading. */
    var rows = [], around = [];
    var base = Math.max(1, Math.round(starX));
    [0.5, 0.75, 0.9, 1, 1.1, 1.25, 1.5].forEach(function (t) {
      var q = Math.max(1, Math.round(base * t));
      if (around.indexOf(q) < 0) around.push(q);
    });
    around.sort(function (a, b) { return a - b; });
    for (i = 0; i < around.length; i += 1) {
      var qq = R(BigInt(around[i]), 1n), sp = eoqSplit(qq, K, D, h);
      var above = eoqAbove(qq, K, D, h);
      rows.push(tr([rowhead(String(around[i])), td(Rshort(sp.order)), td(Rshort(sp.hold)),
        td('<strong>' + Rshort(sp.total) + '</strong>'),
        td(above.cmp > 0 ? 'more' : (above.cmp === 0 ? '<span class="tone-green">the minimum</span>'
          : '<span class="tone-red">below the minimum, which is impossible</span>'),
          above.cmp > 0 ? 'tone-muted' : 'tone-green')]));
    }
    gridEl.innerHTML = '<caption>The two costs and their total, at whole quantities around Q*</caption>'
      + '<thead>' + tr([th('Q'), th('ordering K&middot;D/Q'), th('holding h&middot;Q/2'), th('total'),
        th('against the exact minimum')]) + '</thead><tbody>' + rows.join('') + '</tbody>';

    var whole = eoqWholeScan(K, D, h, 1, qMax);
    setKpi('ivQstarK', rational ? Rtext(Qs.q) + ' <span class="tone-green">exact</span>'
      : surdtext(Qs) + ' <span class="tone-amber">irrational</span>');
    setKpi('ivQdecK', rational ? '&mdash;' : surdDec(Qs, 4));
    setKpi('ivCstarK', star.costSurd.k === 1n ? Rtext(star.costSurd.q) : surdtext(star.costSurd));
    setKpi('ivCdecK', star.costSurd.k === 1n ? '&mdash;' : surdDec(star.costSurd, 4));
    setKpi('ivAtK', Rshort(eoqCostAt(Q, K, D, h)));
    setKpi('ivWholeK', whole.Q + ' at ' + Rshort(whole.cost));

    var rounded = (!rational || star.costSurd.k !== 1n);
    statusEl.innerHTML = '<strong>Q* = sqrt(2KD/h) = '
      + (rational ? Rtext(Qs.q) : surdtext(Qs)) + '</strong> and the least cost is '
      + (star.costSurd.k === 1n ? Rtext(star.costSurd.q) : surdtext(star.costSurd)) + ' per unit time. '
      + (rounded
          ? '<span class="tone-amber">This one is irrational.</span> The decimal beside it is '
            + roundedNote(4) + '. '
          : 'Both come out rational on this instance, so every digit above is exact and you can check '
            + 'them by hand. ')
      + 'Within ' + Rpct(e, 0) + ' of the minimum the order quantity may be anything from '
      + bandQ.loValue + ' to ' + bandQ.hiValue + ' &mdash; that is '
      + bandQ.belowPct + '% below to ' + bandQ.abovePct + '% above, and '
      + '<strong>not one of K, D or h appears in those two percentages</strong>: '
      + bandQ.band.why + '. The cheapest WHOLE quantity is ' + whole.Q
      + ', which is ' + (Math.abs(whole.Q - starX) < 1 ? 'Q* rounded to the nearer integer'
        : 'not simply Q* rounded, because the curve is not symmetric about it') + '.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    kIn.value = p.K; dIn.value = p.D; hIn.value = p.h;
    redraw();
  });
  [kIn, dIn, hIn, qS, tolS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A batch too small is ordered too often; a batch too large sits in the store",
        subtitle="the quantity where those two costs balance, and how wide the flat bottom is",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set K, D and h, then move Q off the optimum",
        panel_intro="Nothing here is stored. The two cost curves are sampled on exact rationals, the "
        "economic order quantity is carried as a surd, and the shaded band comes from a second "
        "discriminant rather than from trying quantities until one is close enough.",
    )


# ---------------------------------------------------------------------------
# Mode `discriminant` -- the EOQ as two roots colliding
# ---------------------------------------------------------------------------


def _discriminant(cfg):
    chosen, here = _preset(cfg, EOQ_PRESETS, "discriminant", "workshop")

    markup = (
        _toolbar(
            "Ask for a budget, and read off the quantities that meet it",
            "hQ&sup2;/2 &minus; TQ + KD &le; 0 &mdash; a quadratic, and its discriminant decides",
            [
                ("cyan", "the parabola hQ&sup2;/2 &minus; TQ + KD"),
                ("green", "quantities that cost at most T"),
                ("amber", "the two roots"),
                ("red", "no quantity meets the budget"),
            ],
        )
        + _stage(_svg("idPara", "0 0 660 250",
                      "The quadratic in the order quantity, with the interval where it is at or below zero "
                      "shaded and its two roots marked."))
        + _table("idGrid")
        + _banner("idStatus")
    )
    controls = (
        _select("idPreset", "Worked example",
                [(k, EOQ_PRESETS[k]["label"]) for k in ("workshop", "bench", "bulk")], chosen)
        + _text("idK", "Ordering cost K", here["K"])
        + _text("idD", "Demand D", here["D"])
        + _text("idH", "Holding cost h", here["h"])
        + _range("idBudget", "Budget T, as a percentage of the least possible cost", 80, 200, 130, 1)
        + _kpis(
            [
                ("Budget T", "idTK"),
                ("Discriminant T&sup2; &minus; 2hKD", "idDiscK"),
                ("Roots", "idRootsK"),
                ("Least possible cost C*", "idCK"),
                ("Q at the merge", "idMergeK"),
                ("Width of the interval", "idWidthK"),
            ]
        )
        + _hint(
            "idHint",
            "Lower the budget and the two roots move together. They meet &mdash; the discriminant "
            "hits exactly zero &mdash; at T = &radic;(2hKD), and the single quantity left at that "
            "moment is the economic order quantity. Lower it any further and the discriminant goes "
            "negative: no order quantity is that cheap, and the parabola never reaches the axis.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", EOQ_PRESETS) + r"""
  var presetS = document.getElementById('idPreset');
  var kIn = document.getElementById('idK');
  var dIn = document.getElementById('idD');
  var hIn = document.getElementById('idH');
  var budS = document.getElementById('idBudget');
  var paraEl = document.getElementById('idPara');
  var gridEl = document.getElementById('idGrid');
  var statusEl = document.getElementById('idStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    paraEl.innerHTML = ''; gridEl.innerHTML = '';
    ['idTK', 'idDiscK', 'idRootsK', 'idCK', 'idMergeK', 'idWidthK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var K = invPositive(kIn.value), D = invPositive(dIn.value), h = invPositive(hIn.value);
    if (K === null || D === null || h === null) {
      blank('K, D and h each have to be a positive number or fraction. The quadratic below needs a '
        + 'positive leading coefficient h/2, or it opens downwards and the whole argument inverts.');
      return;
    }
    var star = eoq(K, D, h), Cstar = star.costSurd;
    /* The budget is set as a PERCENTAGE of C*, which is generally irrational,
       so the percentage is applied to a rational approximation of it and the
       page says so. The discriminant argument itself never touches that
       decimal: it is run on the rational T the slider produced. */
    var pct = Math.max(80, Math.min(200, +budS.value || 130));
    var Cdec = surdDec(Cstar, 4);
    var T = Rmul(Rparse(Cdec), R(BigInt(pct), 100n));
    /* At exactly 100% the interesting case is the MERGE, and it is only a merge
       when T is exactly C*. C* is rational often enough that the page should
       show the real thing when it can. */
    if (pct === 100 && Cstar.k === 1n) T = Cstar.q;
    document.getElementById('idBudgetOut').textContent = pct + '% of C*';

    var dsc = eoqDiscriminant(K, D, h, T);
    var a = Rdiv(h, R(2n, 1n));
    var qMax = Math.max(8, Math.round(parseFloat(surdDec(star.Qsurd, 2)) * 3));
    var pts = [], i;
    for (i = 0; i <= 120; i += 1) {
      var Q = Rmul(R(BigInt(qMax), 1n), R(BigInt(i), 120n));
      var y = Radd(Rsub(Rmul(a, Rmul(Q, Q)), Rmul(T, Q)), Rmul(K, D));
      pts.push([pxOf(Q), pxOf(y)]);
    }
    var marks = [], band = {};
    if (dsc.kind === 'double') {
      marks.push({ kind: 'p', at: pxOf(dsc.roots.roots[0]), y: 0, tone: 'amber', label: 'the merge' });
    } else if (dsc.feasible) {
      var r1 = Rsub(dsc.roots.p, dsc.roots.s.q), r2 = Radd(dsc.roots.p, dsc.roots.s.q);
      if (dsc.roots.s.k === 1n) {
        marks.push({ kind: 'p', at: pxOf(r1), y: 0, tone: 'amber', label: Rshort(r1) });
        marks.push({ kind: 'p', at: pxOf(r2), y: 0, tone: 'amber', label: Rshort(r2) });
        band = { bandFrom: pxOf(r1), bandTo: pxOf(r2) };
      } else {
        var d1 = parseFloat(Rfixed(dsc.roots.p, 4)) - parseFloat(surdDec(dsc.roots.s, 4));
        var d2 = parseFloat(Rfixed(dsc.roots.p, 4)) + parseFloat(surdDec(dsc.roots.s, 4));
        marks.push({ kind: 'p', at: d1, y: 0, tone: 'amber', label: d1.toFixed(2) });
        marks.push({ kind: 'p', at: d2, y: 0, tone: 'amber', label: d2.toFixed(2) });
        band = { bandFrom: d1, bandTo: d2 };
      }
    }
    var opts = { marks: marks, xlo: '0', xhi: String(qMax), ylo: '', yhi: '',
                 xlabel: 'order quantity Q' };
    if (band.bandFrom !== undefined) { opts.bandFrom = band.bandFrom; opts.bandTo = band.bandTo; }
    paraEl.innerHTML = plotSvg([{ tone: dsc.feasible ? 'cyan' : 'red', pts: pts, width: 2.2 }],
                               { w: 660, h: 250 }, opts);

    /* Walk the budget down to the merge in five steps, so the collision is
       something the reader watches rather than something the page announces. */
    var rows = [];
    [160, 140, 120, 110, 105, 100].forEach(function (p) {
      var Tp = Rmul(Rparse(Cdec), R(BigInt(p), 100n));
      if (p === 100 && Cstar.k === 1n) Tp = Cstar.q;
      var d = eoqDiscriminant(K, D, h, Tp);
      var width = '&mdash;';
      if (d.feasible && d.roots.kind !== 'double') {
        width = d.roots.s.k === 1n ? Rshort(Rmul(R(2n, 1n), d.roots.s.q))
          : surdDec({ q: Rmul(R(2n, 1n), d.roots.s.q), k: d.roots.s.k }, 3);
      } else if (d.roots.kind === 'double') {
        width = '<span class="tone-green">0 &mdash; the roots have met</span>';
      }
      rows.push(tr([rowhead(p + '% of C*'), td(Rshort(Tp)),
        td(Rshort(d.disc), Rsign(d.disc) < 0 ? 'tone-red' : (Rzero(d.disc) ? 'tone-green' : '')),
        td(d.roots.kind), td(width)]));
    });
    gridEl.innerHTML = '<caption>The budget walked down to the least possible cost, and what the '
      + 'discriminant does on the way</caption><thead>'
      + tr([th('budget'), th('T'), th('T&sup2; &minus; 2hKD'), th('roots'), th('width of the interval')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    setKpi('idTK', Rshort(T));
    setKpi('idDiscK', Rshort(dsc.disc)
      + (Rzero(dsc.disc) ? ' <span class="tone-green">exactly zero</span>'
         : (Rsign(dsc.disc) < 0 ? ' <span class="tone-red">negative</span>' : '')));
    setKpi('idRootsK', dsc.kind === 'double' ? 'one, doubled: ' + Rtext(dsc.roots.roots[0])
      : (dsc.feasible
          ? (dsc.roots.s.k === 1n
              ? Rshort(Rsub(dsc.roots.p, dsc.roots.s.q)) + ' to ' + Rshort(Radd(dsc.roots.p, dsc.roots.s.q))
              : pmtext(dsc.roots.p, dsc.roots.s, false))
          : 'none: the parabola never reaches the axis'));
    setKpi('idCK', Cstar.k === 1n ? Rtext(Cstar.q) : surdtext(Cstar) + ' &asymp; ' + surdDec(Cstar, 4));
    setKpi('idMergeK', star.Qsurd.k === 1n ? Rtext(star.Qsurd.q)
      : surdtext(star.Qsurd) + ' &asymp; ' + surdDec(star.Qsurd, 4));
    setKpi('idWidthK', dsc.feasible
      ? (dsc.roots.kind === 'double' ? '0'
         : (dsc.roots.s.k === 1n ? Rshort(Rmul(R(2n, 1n), dsc.roots.s.q))
            : surdDec({ q: Rmul(R(2n, 1n), dsc.roots.s.q), k: dsc.roots.s.k }, 3)))
      : '&mdash;');

    statusEl.innerHTML = '<strong>' + dsc.why.charAt(0).toUpperCase() + dsc.why.slice(1) + '.</strong> '
      + 'The question &ldquo;is there an order quantity costing at most T&rdquo; is '
      + 'K&middot;D/Q + h&middot;Q/2 &le; T, and multiplying by Q makes it '
      + 'h Q&sup2;/2 &minus; T Q + K D &le; 0 &mdash; a quadratic with a positive leading coefficient, '
      + 'so it is at or below zero exactly between its roots. The roots merge when the discriminant '
      + 'T&sup2; &minus; 2hKD is zero, at T = sqrt(2hKD) = '
      + (Cstar.k === 1n ? Rtext(Cstar.q) : surdtext(Cstar))
      + ', and the single quantity surviving there is T/h = '
      + (star.Qsurd.k === 1n ? Rtext(star.Qsurd.q) : surdtext(star.Qsurd))
      + '. <strong>That is the economic order quantity, derived here rather than quoted, and nothing '
      + 'was differentiated to get it.</strong>'
      + (Cstar.k === 1n ? ' Both figures are rational on this instance.'
         : ' <span class="tone-amber">Both are irrational on this instance</span>, so the decimals are '
           + roundedNote(4) + '; the budget slider is a percentage of that decimal, which is why the '
           + '100% row above is close to a merge rather than exactly one.');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    kIn.value = p.K; dIn.value = p.D; hIn.value = p.h;
    redraw();
  });
  [kIn, dIn, hIn, budS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="The order quantity is where two roots collide",
        subtitle="no derivative: a quadratic, its discriminant, and the budget at which the interval closes",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set a budget and watch the interval of affordable quantities close",
        panel_intro="Every figure here comes from the discriminant of h&middot;Q&sup2;/2 &minus; T&middot;Q "
        "+ K&middot;D. The economic order quantity is not assumed anywhere on this page; it is what is "
        "left when the two roots meet.",
    )


# ---------------------------------------------------------------------------
# Mode `discount` -- all-units price breaks, and a discontinuous curve
# ---------------------------------------------------------------------------


def _discount(cfg):
    chosen, here = _preset(cfg, DISCOUNT_PRESETS, "discount", "threeband")

    markup = (
        _toolbar(
            "The whole order is repriced, so the curve jumps",
            "one candidate per band: its own EOQ when that falls inside, the band&rsquo;s floor when it does not",
            [
                ("cyan", "the cheapest band"),
                ("purple", "the other bands"),
                ("amber", "each band&rsquo;s candidate quantity"),
                ("muted", "a price break"),
            ],
        )
        + _stage(_svg("iqCurve", "0 0 660 250",
                      "Total cost per unit time against order quantity, drawn as one segment per price "
                      "band so the jump at each break is visible."))
        + _table("iqGrid")
        + _banner("iqStatus")
    )
    controls = (
        _select("iqPreset", "Worked example",
                [(k, DISCOUNT_PRESETS[k]["label"]) for k in ("threeband", "twoband")], chosen)
        + _text("iqK", "Ordering cost K", here["K"])
        + _text("iqD", "Demand D", here["D"])
        + _text("iqBreaks", "Bands &mdash; &ldquo;from price holding&rdquo;, one per row", here["breaks"])
        + _kpis(
            [
                ("Bands", "iqBandsK"),
                ("Cheapest band", "iqBestK"),
                ("Its quantity", "iqQK"),
                ("Its cost", "iqCostK"),
                ("Cheapest whole Q, by scan", "iqScanK"),
                ("Do they agree", "iqAgreeK"),
            ]
        )
        + _hint(
            "iqHint",
            "The candidate with the smallest order quantity is not the cheapest plan, and the "
            "candidate in the cheapest band is not always reachable. Each band has one candidate: "
            "its own economic order quantity if that lands inside the band, and otherwise the "
            "quantity at the band&rsquo;s floor, because within a band the cost curve is still a "
            "single EOQ curve and the nearest point to its minimum is the floor.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", DISCOUNT_PRESETS) + r"""
  var presetS = document.getElementById('iqPreset');
  var kIn = document.getElementById('iqK');
  var dIn = document.getElementById('iqD');
  var bIn = document.getElementById('iqBreaks');
  var curveEl = document.getElementById('iqCurve');
  var gridEl = document.getElementById('iqGrid');
  var statusEl = document.getElementById('iqStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    curveEl.innerHTML = ''; gridEl.innerHTML = '';
    ['iqBandsK', 'iqBestK', 'iqQK', 'iqCostK', 'iqScanK', 'iqAgreeK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  /* "from price holding" a row, semicolons between rows. Parsed through Rread
     like every other reader input on this path, so 9/5 is exact. */
  function readBands(text) {
    var rows = String(text).split(';'), out = [], k;
    for (k = 0; k < rows.length; k += 1) {
      if (!rows[k].trim()) continue;
      var parts = rows[k].trim().split(/[\s,]+/);
      if (parts.length < 2) return null;
      var from = Rread(parts[0]), price = Rread(parts[1]);
      var hb = parts.length > 2 ? Rread(parts[2]) : null;
      if (from === null || price === null) return null;
      if (Rsign(from) < 0 || Rsign(price) <= 0) return null;
      if (parts.length > 2 && (hb === null || Rsign(hb) <= 0)) return null;
      out.push({ from: from, price: price, h: hb });
    }
    if (!out.length) return null;
    for (k = 1; k < out.length; k += 1) if (Rcmp(out[k].from, out[k - 1].from) <= 0) return null;
    if (!Rzero(out[0].from)) return null;
    return out;
  }

  function redraw() {
    var K = invPositive(kIn.value), D = invPositive(dIn.value);
    var breaks = readBands(bIn.value);
    if (K === null || D === null || breaks === null) {
      blank('Each band is &ldquo;from price holding&rdquo; &mdash; the quantity at which it starts, the '
        + 'unit price, and the holding cost at that price. Rows are separated by a semicolon, the first '
        + 'band must start at 0, and the starting quantities must increase.');
      return;
    }
    var hDefault = breaks[0].h || R(2n, 1n);
    var res = discountCandidates(breaks, K, D, hDefault);

    var top = breaks[breaks.length - 1].from;
    var hiQ = Math.max(40, Math.round(pxOf(top) * 1.8));
    var series = discountCurve(breaks, K, D, hDefault, R(1n, 1n), R(BigInt(hiQ), 1n), 40);
    var marks = [], i;
    for (i = 0; i < res.candidates.length; i += 1) {
      var c = res.candidates[i];
      var at = c.Q !== null ? pxOf(c.Q) : parseFloat(surdDec(c.Qsurd, 4));
      var y = c.cost.s.k === 1n ? pxOf(Radd(c.cost.r, c.cost.s.q))
        : parseFloat(Rfixed(c.cost.r, 4)) + parseFloat(surdDec(c.cost.s, 4));
      marks.push({ kind: 'p', at: at, y: y, tone: i === res.best ? 'green' : 'amber',
                   label: i === res.best ? 'cheapest' : 'band ' + (i + 1) });
    }
    for (i = 1; i < breaks.length; i += 1) {
      marks.push({ kind: 'v', at: pxOf(breaks[i].from), tone: 'muted', label: Rshort(breaks[i].from) });
    }
    curveEl.innerHTML = plotSvg(series.map(function (s) {
      return { tone: s.band === res.best ? 'cyan' : 'purple', pts: s.pts, width: s.band === res.best ? 2.4 : 1.6 };
    }), { w: 660, h: 250 }, { marks: marks, xlo: '1', xhi: String(hiQ), ylo: '', yhi: 'total cost per unit time',
                              xlabel: 'order quantity Q' });

    var rows = [];
    for (i = 0; i < res.candidates.length; i += 1) {
      var cd = res.candidates[i];
      var qText = cd.Q !== null ? Rtext(cd.Q)
        : (cd.Qsurd.k === 1n ? Rtext(cd.Qsurd.q) : surdtext(cd.Qsurd) + ' &asymp; ' + surdDec(cd.Qsurd, 4));
      var cText = cd.cost.s.k === 1n && Rzero(cd.cost.s.q)
        ? Rshort(cd.cost.r)
        : Rtext(cd.cost.r) + ' + ' + surdtext(cd.cost.s) + ' &asymp; '
          + Rfixed(Radd(cd.cost.r, Rparse(surdDec(cd.cost.s, 6))), 4);
      rows.push(tr([rowhead('band ' + (i + 1) + ', from ' + Rtext(cd.from)),
        td(Rtext(cd.price)), td(cd.at), td(qText), td('<strong>' + cText + '</strong>'),
        td(i === res.best ? '<span class="tone-green">&check; cheapest</span>' : '',
           i === res.best ? 'tone-green' : 'tone-muted')]));
    }
    gridEl.innerHTML = '<caption>One candidate per band, and the comparison between them &mdash; done on '
      + 'surds, not on decimals</caption><thead>'
      + tr([th('band'), th('price'), th('candidate is'), th('quantity'), th('total cost'), th('')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var scan = discountScan(breaks, K, D, hDefault, 1, hiQ);
    var bestC = res.candidates[res.best];
    var bestQ = bestC.Q !== null ? Math.round(pxOf(bestC.Q)) : Math.round(parseFloat(surdDec(bestC.Qsurd, 4)));
    var agree = scan !== null && Math.abs(scan.Q - bestQ) <= 1;
    setKpi('iqBandsK', String(breaks.length));
    setKpi('iqBestK', 'band ' + (res.best + 1) + ' at ' + Rtext(bestC.price));
    setKpi('iqQK', bestC.Q !== null ? Rtext(bestC.Q) : surdDec(bestC.Qsurd, 4));
    setKpi('iqCostK', bestC.cost.s.k === 1n && Rzero(bestC.cost.s.q) ? Rshort(bestC.cost.r)
      : Rfixed(Radd(bestC.cost.r, Rparse(surdDec(bestC.cost.s, 6))), 4));
    setKpi('iqScanK', scan === null ? '&mdash;' : scan.Q + ' at ' + Rfixed(scan.cost, 4));
    setKpi('iqAgreeK', agree ? '<span class="tone-green">yes, to the nearest unit</span>'
      : '<span class="tone-red">no &mdash; read the banner</span>');

    statusEl.innerHTML = '<strong>The total-cost curve is discontinuous at every break, and that is why '
      + 'the cheapest plan is not the one with the smallest order quantity.</strong> '
      + 'Buying into a cheaper band drops D&middot;price by '
      + Rshort(Rmul(D, Rsub(breaks[0].price, breaks[breaks.length - 1].price)))
      + ' per unit time across the whole range, which is a step, not a slope. '
      + res.candidates[res.best].why.charAt(0).toUpperCase() + res.candidates[res.best].why.slice(1) + '. '
      + 'The comparison between candidates is <strong>exact</strong>: each cost is a rational purchase '
      + 'bill plus a surd, and surdValueCmp settles same-radicand pairs by one squaring and '
      + 'different-radicand pairs by rational brackets refined until they separate &mdash; no decimal '
      + 'is compared with another decimal anywhere in it. '
      + (scan === null ? ''
         : 'As a check the page also prices every whole quantity from 1 to ' + hiQ + ': the cheapest is '
           + scan.Q + '. ' + (agree
              ? 'That agrees with the candidate rule, to the nearest unit &mdash; which is all a scan of '
                + 'whole numbers can say about a candidate that is a surd.'
              : '<span class="tone-red">That disagrees with the candidate rule, which means one of the '
                + 'two is wrong and the page is telling you rather than hiding it.</span>'));
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    kIn.value = p.K; dIn.value = p.D; bIn.value = p.breaks;
    redraw();
  });
  [kIn, dIn, bIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A price break moves the whole curve down, not part of it",
        subtitle="one candidate per band, and a comparison that never rounds",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the bands and see which candidate wins",
        panel_intro="All-units pricing reprices the entire order, so the total-cost curve drops by a "
        "constant at each break. Each band contributes one candidate and the winner is chosen by exact "
        "comparison of surd-valued costs.",
    )


# ---------------------------------------------------------------------------
# Mode `epq` -- a finite production rate and planned backorders, as one formula
# ---------------------------------------------------------------------------


def _epq(cfg):
    chosen, here = _preset(cfg, EPQ_PRESETS, "epq", "machine")

    markup = (
        _toolbar(
            "One sawtooth, two switches",
            "a finite production rate tilts the rise; a backorder penalty drops the whole shape below zero",
            [
                ("cyan", "stock on hand"),
                ("red", "backordered"),
                ("green", "the cost at the best backorder level"),
                ("amber", "the optimal run size"),
            ],
        )
        + _stage(_svg("ieSaw", "0 0 660 180",
                      "Stock over three production cycles: it builds while the machine runs, drains "
                      "afterwards, and dips below zero by the planned backorder level."))
        + _stage(_svg("ieProfile", "0 0 660 200",
                      "Cost per unit time against run size, with the backorder level already at its best "
                      "for each run size."))
        + _table("ieGrid")
        + _banner("ieStatus")
    )
    controls = (
        _select("iePreset", "Worked example",
                [(k, EPQ_PRESETS[k]["label"]) for k in ("machine", "fast", "tight")], chosen)
        + _text("ieK", "Setup cost K, per run", here["K"])
        + _text("ieD", "Demand D", here["D"])
        + _text("ieH", "Holding cost h", here["h"])
        + _text("ieP", "Production rate P (blank for instantaneous)", here["P"])
        + _text("iePi", "Backorder penalty &pi; (0 for none allowed)", here["pi"])
        + _range("ieQ", "Run size Q to price", 20, 1200, 400, 10)
        + _kpis(
            [
                ("Factor 1 &minus; D/P", "ieFK"),
                ("Backlog factor (h+&pi;)/&pi;", "ieBK"),
                ("Q* exactly", "ieQK"),
                ("Q* rounded", "ieQdecK"),
                ("Best b at your Q", "ieBestK"),
                ("Cost there", "ieCostK"),
            ]
        )
        + _hint(
            "ieHint",
            "Set P far above D and the tilt disappears: the run becomes instantaneous and the model "
            "is the plain EOQ. Set &pi; to zero and the shape lifts back above the axis. Both named "
            "models &mdash; the economic production quantity, and the EOQ with planned backorders "
            "&mdash; are readings of the one formula, not separate results to memorise.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", EPQ_PRESETS) + r"""
  var presetS = document.getElementById('iePreset');
  var kIn = document.getElementById('ieK');
  var dIn = document.getElementById('ieD');
  var hIn = document.getElementById('ieH');
  var pIn = document.getElementById('ieP');
  var piIn = document.getElementById('iePi');
  var qS = document.getElementById('ieQ');
  var sawEl = document.getElementById('ieSaw');
  var profEl = document.getElementById('ieProfile');
  var gridEl = document.getElementById('ieGrid');
  var statusEl = document.getElementById('ieStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    sawEl.innerHTML = ''; profEl.innerHTML = ''; gridEl.innerHTML = '';
    ['ieFK', 'ieBK', 'ieQK', 'ieQdecK', 'ieBestK', 'ieCostK'].forEach(function (id) { setKpi(id, '&mdash;'); });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var K = invPositive(kIn.value), D = invPositive(dIn.value), h = invPositive(hIn.value);
    var Ptext = String(pIn.value).trim();
    var P = Ptext === '' ? null : invPositive(Ptext);
    var pi = invNonNegative(piIn.value);
    if (K === null || D === null || h === null || pi === null || (Ptext !== '' && P === null)) {
      blank('K, D and h must be positive; the backorder penalty may be zero but not negative; and the '
        + 'production rate is either blank &mdash; meaning a run finishes instantly &mdash; or positive.');
      return;
    }
    var star = epqCost(K, D, h, P, null, pi);
    if (!star.feasible) {
      blank('<strong>' + star.why.charAt(0).toUpperCase() + star.why.slice(1) + '.</strong> '
        + 'The factor 1 &minus; D/P is ' + Rtext(star.factor) + ', which is not positive: at this '
        + 'production rate the machine cannot keep up with demand, so there is no cycle to optimise and '
        + 'no run size to choose. Raise P above D = ' + Rtext(D) + '.');
      return;
    }
    var Qs = star.Qsurd;
    var qTop = Math.max(40, Math.round(parseFloat(surdDec(Qs, 2)) * 2.4));
    qS.max = String(qTop);
    var Q = R(BigInt(Math.max(1, Math.min(qTop, +qS.value || 1))), 1n);
    document.getElementById('ieQOut').textContent = Rtext(Q);
    var best = epqBestB(Q, K, D, h, P, pi);
    var b = best.feasible ? best.b : R0;

    sawEl.innerHTML = plotSvg([{ tone: Rzero(b) ? 'cyan' : 'red', pts: epqPoints(Q, b, D, P, 3), width: 2.2 }],
      { w: 660, h: 180 }, {
        marks: [{ kind: 'v', at: 1, tone: 'muted', label: 'one cycle' }],
        xlo: '0', xhi: '3 cycles', ylo: Rzero(b) ? '0' : '-' + Rshort(b),
        yhi: Rshort(Rsub(Rmul(star.factor, Q), b)),
        xlabel: 'time, in cycles of length Q/D = ' + Rshort(Rdiv(Q, D))
      });

    var prof = epqProfile(K, D, h, P, pi, R(BigInt(Math.max(1, Math.round(qTop / 30))), 1n),
                          R(BigInt(qTop), 1n), 70);
    var pts = prof.map(function (row) { return [pxOf(row.Q), pxOf(row.cost)]; });
    var starX = parseFloat(surdDec(Qs, 4)), starY = parseFloat(surdDec(star.costSurd, 4));
    profEl.innerHTML = plotSvg([{ tone: 'green', pts: pts, width: 2.2 }], { w: 660, h: 200 }, {
      marks: [{ kind: 'p', at: starX, y: starY, tone: 'amber', label: 'Q*' },
              { kind: 'v', at: pxOf(Q), tone: 'red', label: 'your Q' }],
      xlo: '', xhi: String(qTop), ylo: '0', yhi: 'cost per unit time', xlabel: 'run size Q'
    });

    /* The two named models as ROWS of one table, both computed by the same
       function with different arguments. */
    var rows = [];
    var plain = epqCost(K, D, h, null, null, R0);
    var epqOnly = epqCost(K, D, h, P, null, R0);
    var backOnly = epqCost(K, D, h, null, null, pi);
    [['the plain EOQ (P infinite, no backorders)', plain],
     ['the production quantity (finite P, no backorders)', epqOnly],
     ['the EOQ with backorders (P infinite)', backOnly],
     ['both at once, which is this page', star]].forEach(function (pair) {
      var m = pair[1];
      rows.push(tr([rowhead(pair[0]),
        td(m.feasible ? Rtext(m.factor) : '&mdash;'),
        td(m.feasible ? Rtext(m.backlogFactor) : '&mdash;'),
        td(m.feasible ? (m.Qsurd.k === 1n ? Rtext(m.Qsurd.q) : surdtext(m.Qsurd) + ' &asymp; ' + surdDec(m.Qsurd, 3))
           : 'no cycle'),
        td(m.feasible ? (m.costSurd.k === 1n ? Rtext(m.costSurd.q)
            : surdtext(m.costSurd) + ' &asymp; ' + surdDec(m.costSurd, 3)) : '&mdash;')]));
    });
    gridEl.innerHTML = '<caption>Four models, one formula: each row is the same function with a '
      + 'different pair of switches</caption><thead>'
      + tr([th('model'), th('1 &minus; D/P'), th('(h+&pi;)/&pi;'), th('Q*'), th('C*')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    setKpi('ieFK', Rtext(star.factor));
    setKpi('ieBK', Rzero(pi) ? '&mdash; (no backorders)' : Rtext(star.backlogFactor));
    setKpi('ieQK', Qs.k === 1n ? Rtext(Qs.q) + ' <span class="tone-green">exact</span>' : surdtext(Qs));
    setKpi('ieQdecK', Qs.k === 1n ? '&mdash;' : surdDec(Qs, 4));
    setKpi('ieBestK', best.feasible ? Rtext(best.b) : '0 <span class="tone-amber">no penalty</span>');
    setKpi('ieCostK', Rshort(epqCostAt(Q, b, K, D, h, P, pi)));

    statusEl.innerHTML = '<strong>' + star.why.charAt(0).toUpperCase() + star.why.slice(1) + '.</strong> '
      + 'At the run size you picked, Q = ' + Rtext(Q) + ', the best number to leave backordered is '
      + (best.feasible ? 'f&middot;Q&middot;h/(h+&pi;) = ' + Rtext(best.b)
         : '0, because with no penalty the model has no finite answer')
      + ', and the cost there is ' + Rshort(epqCostAt(Q, b, K, D, h, P, pi)) + ' per unit time. '
      + 'The optimum over all run sizes is Q* = '
      + (Qs.k === 1n ? Rtext(Qs.q) : surdtext(Qs)) + ' costing '
      + (star.costSurd.k === 1n ? Rtext(star.costSurd.q) : surdtext(star.costSurd)) + '. '
      + (Qs.k === 1n && star.costSurd.k === 1n
          ? 'Both are rational on this instance.'
          : '<span class="tone-amber">At least one of those is irrational</span>, so the decimals beside '
            + 'them are ' + roundedNote(4) + '.')
      + ' <strong>This page prints the optimal backorder level at a fixed rational Q rather than at Q*</strong>, '
      + 'because at a rational Q the answer is rational and exact, while at an irrational Q* it is a '
      + 'surd &mdash; and a page that printed a rounded b beside an exact Q* would be mixing the two.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    kIn.value = p.K; dIn.value = p.D; hIn.value = p.h; pIn.value = p.P; piIn.value = p.pi;
    redraw();
  });
  [kIn, dIn, hIn, pIn, piIn, qS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A run that takes time, and a shortage you planned",
        subtitle="the production quantity and the backorder model are the same formula with two switches",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Turn each effect on and watch the sawtooth change shape",
        panel_intro="The holding rate is scaled by 1 &minus; D/P because stock builds only at the "
        "difference between the two rates, and divided again by (h+&pi;)/&pi; because a backordered "
        "unit is cheaper to carry than a stocked one. Both corrections are in one function.",
    )


# ---------------------------------------------------------------------------
# Mode `newsvendor` -- the critical ratio against the whole cost curve
# ---------------------------------------------------------------------------


def _newsvendor(cfg):
    chosen, here = _preset(cfg, NV_PRESETS, "newsvendor", "papers")

    markup = (
        _toolbar(
            "One order, one season, no second chance",
            "the critical ratio says where to stop; the cost curve says whether it was right",
            [
                ("cyan", "the demand distribution"),
                ("amber", "the order quantity the ratio picks"),
                ("green", "the cheapest quantity on the whole curve"),
                ("red", "quantities that run short"),
            ],
        )
        + _stage(_svg("inBars", "0 0 660 170",
                      "The demand distribution as bars, with the chosen order quantity marked."))
        + _stage(_svg("inCurve", "0 0 660 200",
                      "Expected cost against order quantity over a window wider than the demand support."))
        + _table("inGrid")
        + _banner("inStatus")
    )
    controls = (
        _select("inPreset", "Worked example",
                [(k, NV_PRESETS[k]["label"]) for k in ("papers", "pastries", "spares")], chosen)
        + _text("inPmf", "Demand &mdash; &ldquo;value probability&rdquo;, one per row", here["pmf"])
        + _text("inCu", "Underage cost c&#8348; (per unit short)", here["cu"])
        + _text("inCo", "Overage cost c&#8338; (per unit left)", here["co"])
        + _kpis(
            [
                ("Critical ratio", "inRatioK"),
                ("Q from the ratio", "inQK"),
                ("Cost there", "inCostK"),
                ("Cheapest on the curve", "inBestK"),
                ("Do they agree", "inAgreeK"),
                ("Mean demand", "inMeanK"),
            ]
        )
        + _hint(
            "inHint",
            "Raise the underage cost and the order climbs; raise the overage cost and it falls. "
            "The ratio c&#8348;/(c&#8348;+c&#8338;) is where the cumulative distribution has to reach, "
            "and the cost curve beside it is the check: the first quantity whose CDF reaches the "
            "ratio should be the cheapest one, and the panel says so only after comparing them.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", NV_PRESETS) + r"""
  var presetS = document.getElementById('inPreset');
  var pmfIn = document.getElementById('inPmf');
  var cuIn = document.getElementById('inCu');
  var coIn = document.getElementById('inCo');
  var barsEl = document.getElementById('inBars');
  var curveEl = document.getElementById('inCurve');
  var gridEl = document.getElementById('inGrid');
  var statusEl = document.getElementById('inStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    barsEl.innerHTML = ''; curveEl.innerHTML = ''; gridEl.innerHTML = '';
    ['inRatioK', 'inQK', 'inCostK', 'inBestK', 'inAgreeK', 'inMeanK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  /* "value probability" a row. The probabilities are NOT normalised silently:
     a distribution that does not sum to one is a typo, and normalising it would
     hide the typo and answer a question the reader did not ask. */
  function readPmf(text) {
    var rows = String(text).split(';'), out = [], k, total = R0;
    for (k = 0; k < rows.length; k += 1) {
      if (!rows[k].trim()) continue;
      var parts = rows[k].trim().split(/[\s,]+/);
      if (parts.length < 2) return null;
      var v = Rread(parts[0]), p = Rread(parts[1]);
      if (v === null || p === null || v.d !== 1n || v.n < 0n || Rsign(p) < 0) return null;
      out.push([Number(v.n), p]);
      total = Radd(total, p);
    }
    if (!out.length || !Requ(total, R1)) return null;
    out.sort(function (a, b) { return a[0] - b[0]; });
    return out;
  }

  function redraw() {
    var pmf = readPmf(pmfIn.value), cu = invPositive(cuIn.value), co = invPositive(coIn.value);
    if (pmf === null || cu === null || co === null) {
      blank('Each row is &ldquo;value probability&rdquo; with a whole non-negative value, rows separated '
        + 'by a semicolon, and <strong>the probabilities must sum to exactly 1</strong> &mdash; they are '
        + 'not rescaled for you, because a distribution that does not sum to one is a typo and rescaling '
        + 'it would answer a different question. Both costs must be positive.');
      return;
    }
    var nv = newsvendor(pmf, cu, co);
    var loQ = Math.max(0, pmf[0][0] - 2), hiQ = pmf[pmf.length - 1][0] + 2;
    var wide = nvWiden(pmf, cu, co, loQ, hiQ);

    barsEl.innerHTML = barsSvg(pmf, { w: 660, h: 170 },
      { markAt: nv.Q, markLabel: 'Q = ' + nv.Q, shortAbove: nv.Q });
    curveEl.innerHTML = plotSvg([{ tone: 'green',
      pts: wide.rows.map(function (r) { return [r.Q, pxOf(r.cost)]; }), width: 2.2 }],
      { w: 660, h: 200 }, {
        marks: [{ kind: 'v', at: nv.Q, tone: 'amber', label: 'the ratio says ' + nv.Q },
                { kind: 'p', at: wide.Q, y: pxOf(wide.rows[wide.best].cost), tone: 'green',
                  label: 'cheapest ' + wide.Q }],
        xlo: String(loQ), xhi: String(hiQ), ylo: '', yhi: 'expected cost',
        xlabel: 'order quantity Q, over a window wider than the demand'
      });

    var rows = [];
    for (var i = 0; i < wide.rows.length; i += 1) {
      var r = wide.rows[i];
      var inSupport = false, cdf = null, acc = R0;
      for (var j = 0; j < pmf.length; j += 1) {
        acc = Radd(acc, pmf[j][1]);
        if (pmf[j][0] === r.Q) { inSupport = true; cdf = acc; }
      }
      if (cdf === null) { acc = R0; for (j = 0; j < pmf.length; j += 1) if (pmf[j][0] <= r.Q) acc = Radd(acc, pmf[j][1]); cdf = acc; }
      var cls = r.Q === nv.Q ? 'tone-amber' : (i === wide.best ? 'tone-green' : '');
      rows.push(tr([rowhead(String(r.Q)), td(Rtext(cdf) + (Rcmp(cdf, nv.ratio) >= 0 ? ' &check;' : '')),
        td(Rshort(r.over)), td(Rshort(r.under)), td('<strong>' + Rshort(r.cost) + '</strong>', cls),
        td(inSupport ? '' : '<span class="tone-muted">outside the support</span>')]));
    }
    gridEl.innerHTML = '<caption>The cost at every whole order quantity in the window, not only at the '
      + 'values demand can take</caption><thead>'
      + tr([th('Q'), th('P(D &le; Q)'), th('expected left over'), th('expected short'), th('expected cost'), th('')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var agree = wide.Q === nv.Q;
    setKpi('inRatioK', Rtext(nv.ratio) + ' = ' + Rpct(nv.ratio, 1));
    setKpi('inQK', nv.Q === null ? 'never reached' : String(nv.Q));
    setKpi('inCostK', nv.cost === null ? '&mdash;' : Rshort(nv.cost));
    setKpi('inBestK', wide.Q + ' at ' + Rshort(wide.rows[wide.best].cost));
    setKpi('inAgreeK', agree ? '<span class="tone-green">yes</span>' : '<span class="tone-red">NO</span>');
    setKpi('inMeanK', Rshort(pmfMean(pmf)));

    statusEl.innerHTML = '<strong>' + nv.why.charAt(0).toUpperCase() + nv.why.slice(1) + '.</strong> '
      + 'The ratio is c&#8348;/(c&#8348;+c&#8338;) = ' + Rtext(cu) + '/(' + Rtext(cu) + ' + ' + Rtext(co)
      + ') = ' + Rtext(nv.ratio) + ', and it is a probability rather than a quantity: it says how often '
      + 'you are willing to be left holding stock. '
      + (agree
          ? 'The cheapest quantity on the whole tabulated curve is ' + wide.Q + ', which is the same '
            + 'quantity &mdash; <span class="tone-green">so on this instance the rule and the curve '
            + 'agree, and the page checked it rather than claiming it</span>.'
          : '<span class="tone-red">The cheapest quantity on the curve is ' + wide.Q + ', and the ratio '
            + 'picked ' + nv.Q + '. Those disagree, which means one of them is wrong; the page reports '
            + 'the disagreement rather than printing the one it prefers.</span>')
      + ' The window runs from ' + loQ + ' to ' + hiQ + ', which is wider than the demand can ever be: '
      + 'ordering more than the largest possible demand is priced here too, so &ldquo;the crossing is the '
      + 'minimum&rdquo; is a statement about the whole line and not about the few points where demand '
      + 'has mass. Every figure is exact &mdash; expectations over a finite distribution with rational '
      + 'probabilities are ratios of integers, and nothing on this page rounds.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pmfIn.value = p.pmf; cuIn.value = p.cu; coIn.value = p.co;
    redraw();
  });
  [pmfIn, cuIn, coIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Order once, for a season you cannot see",
        subtitle="the critical ratio, and the cost curve that has to agree with it",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the demand distribution and the two unit costs",
        panel_intro="The rule picks the smallest quantity whose cumulative probability reaches "
        "c&#8348;/(c&#8348;+c&#8338;). Beside it the expected cost is tabulated at every whole quantity "
        "in a window wider than the demand, so the rule is checked and not merely applied.",
    )


# ---------------------------------------------------------------------------
# Mode `reorder` -- lead-time demand, safety stock, and two service levels
# ---------------------------------------------------------------------------


def _reorder(cfg):
    chosen, here = _preset(cfg, REORDER_PRESETS, "reorder", "steady")

    markup = (
        _toolbar(
            "The risk lives in the lead time, not in the period",
            "L periods of demand convolved, and two different numbers both called &ldquo;service&rdquo;",
            [
                ("cyan", "lead-time demand"),
                ("amber", "the reorder point"),
                ("red", "demand that runs you short"),
                ("green", "the target met"),
            ],
        )
        + _stage(_svg("irBars", "0 0 660 180",
                      "The distribution of demand over the whole lead time, with the reorder point marked "
                      "and the outcomes above it shaded as shortages."))
        + _table("irGrid")
        + _banner("irStatus")
    )
    controls = (
        _select("irPreset", "Worked example",
                [(k, REORDER_PRESETS[k]["label"]) for k in ("steady", "lumpy")], chosen)
        + _text("irPmf", "Demand in ONE period &mdash; &ldquo;value probability&rdquo;", here["pmf"])
        + _range("irL", "Lead time L, in periods", 1, 5, here["L"], 1)
        + _range("irR", "Reorder point r", 0, 14, here["r"], 1)
        + _text("irQ", "Order quantity Q (for the fill rate)", here["Q"])
        + _kpis(
            [
                ("Mean lead-time demand", "irMeanK"),
                ("Safety stock r &minus; &mu;", "irSafeK"),
                ("Cycle service", "irCycleK"),
                ("Expected shortage", "irShortK"),
                ("Fill rate", "irFillK"),
                ("Smallest r for 95%", "irNeedK"),
            ]
        )
        + _hint(
            "irHint",
            "Raise the lead time by one period and watch the distribution spread, not merely shift: "
            "the mean grows by one period&rsquo;s demand but the tail grows faster, which is why a "
            "longer lead time needs more safety stock than the extra mean alone. The two service "
            "figures are different definitions of the same policy and they are printed side by side "
            "so that quoting one for the other is visible.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", REORDER_PRESETS) + r"""
  var presetS = document.getElementById('irPreset');
  var pmfIn = document.getElementById('irPmf');
  var lS = document.getElementById('irL');
  var rS = document.getElementById('irR');
  var qIn = document.getElementById('irQ');
  var barsEl = document.getElementById('irBars');
  var gridEl = document.getElementById('irGrid');
  var statusEl = document.getElementById('irStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    barsEl.innerHTML = ''; gridEl.innerHTML = '';
    ['irMeanK', 'irSafeK', 'irCycleK', 'irShortK', 'irFillK', 'irNeedK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  function readPmf(text) {
    var rows = String(text).split(';'), out = [], k, total = R0;
    for (k = 0; k < rows.length; k += 1) {
      if (!rows[k].trim()) continue;
      var parts = rows[k].trim().split(/[\s,]+/);
      if (parts.length < 2) return null;
      var v = Rread(parts[0]), p = Rread(parts[1]);
      if (v === null || p === null || v.d !== 1n || v.n < 0n || Rsign(p) < 0) return null;
      out.push([Number(v.n), p]);
      total = Radd(total, p);
    }
    if (!out.length || !Requ(total, R1)) return null;
    out.sort(function (a, b) { return a[0] - b[0]; });
    return out;
  }

  function redraw() {
    var pmf = readPmf(pmfIn.value), Q = invPositive(qIn.value);
    if (pmf === null || Q === null) {
      blank('Each row is &ldquo;value probability&rdquo;, rows separated by a semicolon, and the '
        + 'probabilities must sum to exactly 1. The order quantity must be positive &mdash; the fill '
        + 'rate divides by it.');
      return;
    }
    var L = Math.max(1, Math.min(5, +lS.value || 1));
    document.getElementById('irLOut').textContent = L + (L === 1 ? ' period' : ' periods');
    var lead = pmf, k;
    for (k = 1; k < L; k += 1) lead = pmfConvolve(lead, pmf);
    var top = lead[lead.length - 1][0];
    rS.max = String(Math.max(1, top));
    var r = Math.max(0, Math.min(top, +rS.value || 0));
    document.getElementById('irROut').textContent = String(r);

    var rp = reorderPoint(pmf, L, r);
    var fr = fillRate(pmf, L, r, Q);
    barsEl.innerHTML = barsSvg(lead, { w: 660, h: 180 },
      { markAt: r, markLabel: 'r = ' + r, shortAbove: r });

    var rows = [];
    var lo = Math.max(0, r - 3), hi = Math.min(top, r + 4);
    for (k = lo; k <= hi; k += 1) {
      var row = reorderPoint(pmf, L, k), f = fillRate(pmf, L, k, Q);
      rows.push(tr([rowhead(String(k)), td(Rshort(Rsub(R(BigInt(k), 1n), row.meanDemand))),
        td(Rshort(row.cycleService)), td(Rshort(row.shortage)), td(Rshort(f.fill)),
        td(k === r ? '<span class="tone-amber">&larr; yours</span>' : '', k === r ? 'tone-amber' : '')]));
    }
    gridEl.innerHTML = '<caption>Reorder points around yours: the same policy, measured two ways</caption>'
      + '<thead>' + tr([th('r'), th('safety stock'), th('cycle service'), th('expected shortage per cycle'),
        th('fill rate'), th('')]) + '</thead><tbody>' + rows.join('') + '</tbody>';

    var need = smallestReorder(pmf, L, R(19n, 20n), top);
    setKpi('irMeanK', Rshort(rp.meanDemand));
    setKpi('irSafeK', Rshort(rp.safety) + (Rsign(rp.safety) < 0 ? ' <span class="tone-red">negative</span>' : ''));
    setKpi('irCycleK', Rpct(rp.cycleService, 2));
    setKpi('irShortK', Rshort(rp.shortage));
    setKpi('irFillK', Rpct(fr.fill, 3));
    setKpi('irNeedK', need < 0 ? 'not reachable' : String(need));

    /* The spread argument, computed: one more period of lead time adds one
       period's mean and widens the support by the period's own range. */
    var one = reorderPoint(pmf, 1, r), meanOne = one.meanDemand;
    statusEl.innerHTML = '<strong>' + rp.why.charAt(0).toUpperCase() + rp.why.slice(1) + '.</strong> '
      + 'The lead-time distribution is the ' + L + '-fold convolution of one period&rsquo;s demand, so '
      + 'its mean is ' + L + ' &times; ' + Rshort(meanOne) + ' = ' + Rshort(rp.meanDemand)
      + ' and its support runs from ' + lead[0][0] + ' to ' + top + '. '
      + '<strong>Cycle service and fill rate are different numbers.</strong> Cycle service is '
      + 'P(no stockout in a cycle) = ' + Rpct(rp.cycleService, 2)
      + '; the fill rate is the fraction of demand met from stock, 1 &minus; ('
      + Rshort(rp.shortage) + ')/' + Rtext(Q) + ' = ' + Rpct(fr.fill, 3)
      + '. The gap between them is the order quantity: a big Q spreads the same expected shortage over '
      + 'more demand, so the fill rate rises while the cycle service does not move at all. '
      + (need < 0
          ? 'No reorder point in this range reaches 95% cycle service.'
          : 'For 95% cycle service the reorder point has to be ' + need + ', carrying '
            + Rshort(Rsub(R(BigInt(need), 1n), rp.meanDemand)) + ' of safety stock.')
      + ' Every figure is exact: the convolution is over rational probabilities, so nothing here rounds '
      + 'and the percentages are exact fractions printed to two places.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pmfIn.value = p.pmf; lS.value = String(p.L); rS.value = String(p.r); qIn.value = p.Q;
    redraw();
  });
  [pmfIn, lS, rS, qIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="When to reorder is a question about the lead time",
        subtitle="the convolution, the safety stock, and two service levels that are not the same number",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the per-period demand, the lead time and the reorder point",
        panel_intro="The lead-time distribution is built here by convolving the period distribution with "
        "itself, exactly. Cycle service and fill rate are computed from that same distribution and shown "
        "side by side, because they are routinely quoted for one another.",
    )


# ---------------------------------------------------------------------------
# Mode `review` -- periodic review, and why it is R + L periods
# ---------------------------------------------------------------------------


def _review(cfg):
    chosen, here = _preset(cfg, REORDER_PRESETS, "review", "steady")

    markup = (
        _toolbar(
            "An order placed now is the last one that can arrive before the next",
            "so the base-stock level covers R + L periods, not L and not R",
            [
                ("cyan", "demand over R + L periods"),
                ("amber", "the base-stock level S"),
                ("purple", "demand over L periods only, for comparison"),
                ("red", "the exposure a reader who used L would miss"),
            ],
        )
        + _stage(_svg("ipBars", "0 0 660 180",
                      "The distribution of demand over the review interval plus the lead time, with the "
                      "base-stock level marked."))
        + _table("ipGrid")
        + _banner("ipStatus")
    )
    controls = (
        _select("ipPreset", "Worked example",
                [(k, REORDER_PRESETS[k]["label"]) for k in ("steady", "lumpy")], chosen)
        + _text("ipPmf", "Demand in ONE period &mdash; &ldquo;value probability&rdquo;", here["pmf"])
        + _range("ipR", "Review interval R, in periods", 1, 4, 2, 1)
        + _range("ipL", "Lead time L, in periods", 0, 4, 1, 1)
        + _range("ipAlpha", "Service target, in per cent", 50, 99, 90, 1)
        + _kpis(
            [
                ("Periods covered", "ipSpanK"),
                ("Mean over them", "ipMeanK"),
                ("Base-stock level S", "ipSK"),
                ("Achieved service", "ipHitK"),
                ("S from L alone", "ipWrongK"),
                ("What that would cost", "ipGapK"),
            ]
        )
        + _hint(
            "ipHint",
            "Set the lead time to zero and the answer is still R periods of demand, not none: the "
            "order arrives instantly but the next one cannot be placed until the next review, so "
            "the stock has to last the interval. Set R to one and it becomes the continuous-review "
            "answer. The comparison row shows what covering only the lead time would leave exposed.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", REORDER_PRESETS) + r"""
  var presetS = document.getElementById('ipPreset');
  var pmfIn = document.getElementById('ipPmf');
  var rS = document.getElementById('ipR');
  var lS = document.getElementById('ipL');
  var aS = document.getElementById('ipAlpha');
  var barsEl = document.getElementById('ipBars');
  var gridEl = document.getElementById('ipGrid');
  var statusEl = document.getElementById('ipStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    barsEl.innerHTML = ''; gridEl.innerHTML = '';
    ['ipSpanK', 'ipMeanK', 'ipSK', 'ipHitK', 'ipWrongK', 'ipGapK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  function readPmf(text) {
    var rows = String(text).split(';'), out = [], k, total = R0;
    for (k = 0; k < rows.length; k += 1) {
      if (!rows[k].trim()) continue;
      var parts = rows[k].trim().split(/[\s,]+/);
      if (parts.length < 2) return null;
      var v = Rread(parts[0]), p = Rread(parts[1]);
      if (v === null || p === null || v.d !== 1n || v.n < 0n || Rsign(p) < 0) return null;
      out.push([Number(v.n), p]);
      total = Radd(total, p);
    }
    if (!out.length || !Requ(total, R1)) return null;
    out.sort(function (a, b) { return a[0] - b[0]; });
    return out;
  }
  function cdfAt(rows, x) {
    var acc = R0, i;
    for (i = 0; i < rows.length; i += 1) if (rows[i].x <= x) acc = Radd(acc, rows[i].p);
    return acc;
  }

  function redraw() {
    var pmf = readPmf(pmfIn.value);
    if (pmf === null) {
      blank('Each row is &ldquo;value probability&rdquo;, rows separated by a semicolon, and the '
        + 'probabilities must sum to exactly 1.');
      return;
    }
    var R_ = Math.max(1, Math.min(4, +rS.value || 1));
    var L = Math.max(0, Math.min(4, +lS.value || 0));
    var alpha = R(BigInt(Math.max(50, Math.min(99, +aS.value || 90))), 100n);
    document.getElementById('ipROut').textContent = R_ + (R_ === 1 ? ' period' : ' periods');
    document.getElementById('ipLOut').textContent = L + (L === 1 ? ' period' : ' periods');
    document.getElementById('ipAlphaOut').textContent = Rpct(alpha, 0);

    var bs = baseStock(pmf, R_, L, alpha);
    barsEl.innerHTML = barsSvg(bs.demand, { w: 660, h: 180 },
      { markAt: bs.S === null ? undefined : bs.S,
        markLabel: bs.S === null ? '' : 'S = ' + bs.S, shortAbove: bs.S === null ? undefined : bs.S });

    /* The misconception, priced: cover L periods only and see what the service
       level actually becomes over R + L. */
    var wrong = L === 0 ? null : baseStock(pmf, L, 0, alpha);
    var wrongS = wrong === null ? null : wrong.S;
    var achievedWrong = wrongS === null ? null : cdfAt(bs.rows, wrongS);

    var rows = [];
    for (var k = 0; k < bs.rows.length; k += 1) {
      var row = bs.rows[k];
      var cls = bs.S !== null && row.x === bs.S ? 'tone-amber'
        : (wrongS !== null && row.x === wrongS ? 'tone-red' : '');
      rows.push(tr([rowhead(String(row.x)), td(Rshort(row.p)), td(Rshort(row.cdf)),
        td(Rcmp(row.cdf, alpha) >= 0 ? '<span class="tone-green">&check; reaches the target</span>' : '', cls),
        td(bs.S !== null && row.x === bs.S ? 'S, covering R + L'
           : (wrongS !== null && row.x === wrongS ? 'what L alone would have given' : ''), cls)]));
    }
    gridEl.innerHTML = '<caption>Demand over ' + bs.periods + ' periods, and where the target is first '
      + 'reached</caption><thead>'
      + tr([th('total demand'), th('probability'), th('cumulative'), th(''), th('')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    setKpi('ipSpanK', 'R + L = ' + R_ + ' + ' + L + ' = ' + bs.periods);
    setKpi('ipMeanK', Rshort(bs.mean));
    setKpi('ipSK', bs.S === null ? 'not reachable' : String(bs.S));
    setKpi('ipHitK', bs.S === null ? '&mdash;' : Rpct(cdfAt(bs.rows, bs.S), 2));
    setKpi('ipWrongK', wrongS === null ? 'L = 0, so there is none' : String(wrongS));
    setKpi('ipGapK', achievedWrong === null ? '&mdash;'
      : Rpct(achievedWrong, 2) + ' <span class="tone-red">against ' + Rpct(alpha, 0) + '</span>');

    statusEl.innerHTML = '<strong>' + bs.why.charAt(0).toUpperCase() + bs.why.slice(1) + '.</strong> '
      + 'Think about when the next chance to act arrives. An order placed at this review lands after L = '
      + L + ' period' + (L === 1 ? '' : 's') + '; the order placed at the NEXT review lands R = ' + R_
      + ' period' + (R_ === 1 ? '' : 's') + ' later than that. So the stock on hand and on order right now '
      + 'has to carry the whole of R + L = ' + bs.periods + ' periods, and it is that convolution &mdash; '
      + 'mean ' + Rshort(bs.mean) + ', support ' + bs.demand[0][0] + ' to '
      + bs.demand[bs.demand.length - 1][0] + ' &mdash; that gets quantiled. '
      + (bs.S === null
          ? 'No level in the support reaches ' + Rpct(alpha, 0) + '.'
          : 'The smallest S reaching ' + Rpct(alpha, 0) + ' is <strong>' + bs.S + '</strong>, and it '
            + 'actually achieves ' + Rpct(cdfAt(bs.rows, bs.S), 2) + ' &mdash; a discrete distribution '
            + 'overshoots the target rather than meeting it exactly, which is a fact about the '
            + 'distribution and not a rounding.')
      + (wrongS === null
          ? ' With L = 0 there is no lead time to confuse with the interval, and the answer is still R '
            + 'periods of demand: the order arrives instantly, but the next one cannot be placed until '
            + 'the next review.'
          : ' <span class="tone-red">Covering the lead time alone would give S = ' + wrongS
            + '</span>, which over the real R + L periods delivers ' + Rpct(achievedWrong, 2)
            + ' service against a target of ' + Rpct(alpha, 0) + '. That gap is the whole reason the '
            + 'interval is in the formula.');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pmfIn.value = p.pmf;
    redraw();
  });
  [pmfIn, rS, lS, aS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Reviewing every R periods changes what the stock has to cover",
        subtitle="R + L, and the service level a reader who used L alone would actually get",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the review interval, the lead time and the target",
        panel_intro="The distribution quantiled here is the demand over the review interval PLUS the lead "
        "time, built by convolution on this page. The comparison row prices the usual mistake instead of "
        "warning about it.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "eoq": _eoq,
    "discriminant": _discriminant,
    "discount": _discount,
    "epq": _epq,
    "newsvendor": _newsvendor,
    "reorder": _reorder,
    "review": _review,
}

MODES = tuple(sorted(_MODES))


def inventory_lab(cfg):
    """The inventory kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract. A kit that fell back to a default would render a
    finished-looking page carrying another lesson's widget: every markup
    assertion passes, labcheck passes, and the reader is shown the wrong
    arithmetic under the right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "inventory_lab: unknown mode %r; the seven modes of the inventory kit are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})
