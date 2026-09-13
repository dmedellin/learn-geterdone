"""Course 1 of System Design: capacity estimation.

Eight modes, one per shape of back-of-envelope arithmetic the course teaches,
and ten lessons drawing on them. Every figure below is a ratio of integers
whenever its inputs are, so the lab prints ``125/108`` where the reader can
check it and never ``1.1574074074074074``.

Three places genuinely round, and each says so on the page:

  * the geometric-mean centre of an asymmetric interval, which is a square root
    (``sqrtApprox``, Newton, with ``Rsqrt`` used instead wherever the root is
    exact -- the symmetric case, which is the one lesson 1 works);
  * the width of an interval quoted in decimal powers of ten (``log10Approx``).
    The integer bracket beside it is an exact search over powers of ten and is
    what the page asserts; the decimal is the gloss;
  * the log ruler's PIXEL POSITIONS in the scale mode. The ratio the lesson is
    about is exact; only where a rung is drawn is rounded.

Nothing else here uses a float. In particular the machine count is a genuine
ceiling of an exact rational (``Rceil``), the storage series is an exact sum of
exact powers (``Rpow``), and the peak-to-mean ratio is ``24 * peak / total``
with both ends integers.

Three lessons share the ``rate`` mode, so a lesson names its own worked example
with a ``preset`` key alongside ``mode``. The preset is what makes the panel
open on the numbers the prose just used, and an unknown one raises rather than
opening on somebody else's:

    L1  orders-of-magnitude            magnitude   ten-million-users
    L2  rates-and-the-day-in-seconds   rate        day-in-seconds
    L3  read-write-ratio               rate        read-write
    L4  storage-from-ingest...         accumulate  event-log
    L5  bandwidth-bits-and-overhead    rate        bandwidth
    L6  latency-numbers-on-a-log-scale scale       ram-vs-disk
    L7  peak-to-average                peak        consumer-evening
    L8  from-request-cost-to-machine-count  machines   checkout-api
    L9  memory-and-the-working-set     workingset  social-timeline
    L10 triangulating-an-estimate      triangulate photo-bytes

The three ``rate`` lessons differ ONLY in that key -- same mode, three chains,
three different opening panels -- which is why leaving it off would silently
give lessons 3 and 5 lesson 2's widget.
"""

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal
from .counting import BIGINT_JS
from .sysdesign_core import APPROX_JS, RCEIL_JS

ESTIMATE_JS = r"""
  /* ======================= printing an exact rational =======================

     algebra_core's Rdec goes through Number(a.n)/Number(a.d). A capacity figure
     is routinely 10^15 over 10^72 once a monthly growth factor has been raised
     to the 36th power, both ends overflow a double, and the reader is handed
     NaN. Rround does the same job entirely in BigInt: exact up to the one
     rounding it names, at any size. */
  function Rround(a, places) {
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (n * scale * 10n / d + 5n) / 10n;
    var s = q.toString();
    while (s.length <= places) s = '0' + s;
    var out = places > 0 ? s.slice(0, s.length - places) + '.' + s.slice(s.length - places) : s;
    return (neg ? '-' : '') + out;
  }
  /* Trailing zeros dropped, and the point with them if nothing is left. */
  function Rtrim(text) {
    if (text.indexOf('.') < 0) return text;
    return text.replace(/0+$/, '').replace(/\.$/, '');
  }
  /* Digit grouping that stops at the decimal point, which counting.py's group()
     does not: it would turn 1234567.89 into 1 234 567.89 only by luck. */
  function groupDec(text) {
    var dot = text.indexOf('.');
    var whole = dot < 0 ? text : text.slice(0, dot), rest = dot < 0 ? '' : text.slice(dot);
    var sign = '';
    if (whole.charAt(0) === '-') { sign = '-'; whole = whole.slice(1); }
    return sign + whole.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + rest;
  }
  /* An exact rational shown the way a capacity answer is read: grouped, to a
     stated number of places, with the fraction itself beside it when short. */
  function showR(a, places) {
    return groupDec(Rtrim(Rround(a, places === undefined ? 2 : places)));
  }
  /* Rtext with the digits grouped. 100000 and 100 000 are the same number and
     only one of them can be read at a glance, which matters most for exactly
     the ratios this course is about. */
  function Rtextg(a) {
    var w = groupDec(a.n.toString());
    return a.d === 1n ? w : w + '/' + groupDec(a.d.toString());
  }

  /* ========================= widths in powers of ten ======================= */

  /* The largest integer e with 10^e <= a. An exact search over powers of ten:
     no logarithm is anywhere near the number the page asserts. */
  function decadeBracket(a) {
    if (a.n <= 0n) return null;
    var e = 0, v = a, one = R(1n, 1n), ten = R(10n, 1n);
    while (Rcmp(v, ten) >= 0) { v = Rdiv(v, ten); e += 1; }
    while (Rcmp(v, one) < 0) { v = Rmul(v, ten); e -= 1; }
    return e;
  }
  /* The same width as a decimal, which is what "an answer good to half an order
     of magnitude" means out loud. It ROUNDS, twice: the BigInt ends are trimmed
     to fifteen digits before the division, then Math.log10 runs. Accurate to
     about 1e-15 relative, and the page labels it as the gloss on the bracket. */
  function log10Approx(a) {
    if (a.n <= 0n) return NaN;
    var n = a.n, d = a.d, shift = 0, cap = 1000000000000000n;
    while (n > cap) { n /= 10n; shift += 1; }
    while (d > cap) { d /= 10n; shift -= 1; }
    return shift + Math.log10(Number(n) / Number(d));
  }

  /* ===================== L1: an estimate is an interval ====================

     A factor known to "a factor of k" is the interval [c/k, c*k]; the product
     of intervals of positive numbers is [prod lo, prod hi], and the half-width
     of the product is the PRODUCT of the half-widths -- which is the whole
     lesson: three factors at 2 give a product at 8, not at 6 and not at 2. */
  function productInterval(centres, downs, ups) {
    var lo = R(1n, 1n), hi = R(1n, 1n), c = R(1n, 1n), d = R(1n, 1n), u = R(1n, 1n);
    for (var i = 0; i < centres.length; i += 1) {
      lo = Rmul(lo, Rdiv(centres[i], downs[i]));
      hi = Rmul(hi, Rmul(centres[i], ups[i]));
      c = Rmul(c, centres[i]);
      d = Rmul(d, downs[i]);
      u = Rmul(u, ups[i]);
    }
    return { lo: lo, hi: hi, centre: c, down: d, up: u, ratio: Rdiv(hi, lo) };
  }
  /* The misconception, computed rather than described: the arithmetic midpoint
     of [c/8, 8c] is 65c/16, four times the estimate it is supposed to centre. */
  function arithMid(lo, hi) { return Rdiv(Radd(lo, hi), R(2n, 1n)); }
  /* The honest centre of a multiplicative range. Exact when lo*hi is a perfect
     square -- which every symmetric interval is, so lesson 1's own example is
     exact -- and null when it is not, at which point the caller must say it is
     rounding and use geoMeanApprox. */
  function geoMeanExact(lo, hi) { return Rsqrt(Rmul(lo, hi)); }
  function geoMeanApprox(lo, hi) { return sqrtApprox(Rmul(lo, hi), 1e-15); }

  /* ============================ L2: rates =================================

     86400 seconds in a day, 10^5 in the shortcut. The shortcut's day is
     100000/86400 = 125/108 long, so a rate divided by it comes out 108/125 of
     the truth. Both fractions are exact and the page prints both, because the
     reader who remembers only "15.7%" will apply it in the wrong direction. */
  function dailyVolume(users, actions) { return Rmul(users, actions); }
  function rpsExact(users, actions) { return Rdiv(dailyVolume(users, actions), R(86400n, 1n)); }
  function rpsRounded(users, actions) { return Rdiv(dailyVolume(users, actions), R(100000n, 1n)); }
  /* How much longer the shortcut's day is: 125/108. */
  function dayLengthRatio() { return Rdiv(R(100000n, 1n), R(86400n, 1n)); }
  /* How much lower the shortcut's rate is: 108/125, the reciprocal. */
  function rateShortfallRatio() { return Rinv(dayLengthRatio()); }

  /* ============================ L3: one rate, two ==========================

     r reads per write. The write share is 1/(r+1) and the reader's instinct is
     1/r; at r = 100 that is 1/101 against 1/100, which is the lesson. */
  function splitRates(total, r) {
    var one = R(1n, 1n), denom = Radd(r, one);
    var writeShare = Rdiv(one, denom), readShare = Rdiv(r, denom);
    return {
      reads: Rmul(total, readShare), writes: Rmul(total, writeShare),
      readShare: readShare, writeShare: writeShare,
      naiveWriteShare: Rdiv(one, r),
      naiveOver: Rdiv(Rdiv(one, r), writeShare)
    };
  }

  /* ============================ L5: bandwidth ==============================

     A link is bits a second, a payload is bytes, and the header is charged once
     per request whatever the payload. Mbit/s here is 10^6 bits a second, which
     is what a link is sold in; the page says so rather than leaving the reader
     to wonder whether it meant 2^20. */
  function requestBytes(payload, header) { return Radd(payload, header); }
  function bandwidthBits(rate, payload, header) {
    return Rmul(R(8n, 1n), Rmul(rate, requestBytes(payload, header)));
  }
  function bandwidthMbit(rate, payload, header) {
    return Rdiv(bandwidthBits(rate, payload, header), R(1000000n, 1n));
  }
  /* The slip the lesson names: the BYTES divided by a million, called Mbit/s.
     Exactly an eighth of the truth, whatever the inputs. */
  function bandwidthNoEight(rate, payload, header) {
    return Rdiv(Rmul(rate, requestBytes(payload, header)), R(1000000n, 1n));
  }
  function headerShare(payload, header) { return Rdiv(header, requestBytes(payload, header)); }
  /* Headers are at least half the bytes exactly when the payload is no bigger
     than the header, so the crossover payload IS the header size -- a one-line
     result, and the reason the lesson can state it without a table. */
  function headerCrossover(header) { return header; }

  /* ============================ L4: accumulation ===========================

     Storage is the sum of a rate over a retention window. At constant ingest
     that is an arithmetic series with zero common difference -- rate * days --
     and under growth it is a geometric one. Growth compounds once a month, so
     the window is a run of 30-day blocks each at its own constant rate; the
     model is stepwise and the page says so, because a continuously compounded
     day would be an irrational factor and this course has no need of one. */
  var DAYS_PER_MONTH = 30;
  function growthTerms(ingestPerDay, days, growth) {
    var factor = Radd(R(1n, 1n), growth);
    var rows = [], running = R(0n, 1n), left = days, m = 0;
    while (left > 0) {
      var span = left < DAYS_PER_MONTH ? left : DAYS_PER_MONTH;
      var rate = Rmul(ingestPerDay, Rpow(factor, m));
      var bytes = Rmul(rate, R(BigInt(span), 1n));
      running = Radd(running, bytes);
      rows.push({ month: m, days: span, rate: rate, bytes: bytes, running: running });
      left -= span; m += 1;
    }
    return rows;
  }
  function storageGrowth(ingestPerDay, days, growth, copies) {
    var rows = growthTerms(ingestPerDay, days, growth);
    var total = rows.length ? rows[rows.length - 1].running : R(0n, 1n);
    return Rmul(total, R(BigInt(copies), 1n));
  }
  function storageFlat(ingestPerDay, days, copies) {
    return Rmul(Rmul(ingestPerDay, R(BigInt(days), 1n)), R(BigInt(copies), 1n));
  }

  /* ============================ L6: the log ruler ==========================

     The rungs are measured reference latencies and are lesson data, printed on
     the page in full. The only thing computed from them is the ratio, and it is
     computed exactly: "how many RAM reads fit in one disk seek" is an integer,
     and a reader who gets 99999.99999 cannot tell it from a wrong answer. */
  function rungRatio(slowNs, fastNs) { return Rdiv(R(BigInt(slowNs), 1n), R(BigInt(fastNs), 1n)); }

  /* ============================ L7: peak to average =======================

     Integer weights for 24 hours, so the daily total is an exact multiple of
     the base rate and no bucket is a rounded share of a total. peakStats then
     reads the profile: mean rps is the day's total over 86400 -- the number the
     lesson warns against sizing to -- and peak rps is the busiest bucket over
     3600. Their ratio is 24 * peak / total, exactly. */
  function profileWeights(shape, peakHour, amp) {
    var w = [], h, dist, far;
    for (h = 0; h < 24; h += 1) {
      dist = Math.abs(h - peakHour);
      if (dist > 12) dist = 24 - dist;
      far = Math.abs(h - ((peakHour + 12) % 24));
      if (far > 12) far = 24 - far;
      if (shape === 'flat') w.push(10);
      else if (shape === 'office') w.push(10 + amp * Math.max(0, 6 - dist));
      else if (shape === 'twopeak') w.push(10 + amp * Math.max(0, 6 - dist) + amp * Math.max(0, 4 - far));
      else if (shape === 'spike') w.push(dist === 0 ? 10 + amp * 12 : 10);
      else throw new Error('unknown profile shape: ' + shape);
    }
    return w;
  }
  function peakStats(buckets) {
    var total = R(0n, 1n), peak = buckets[0], at = 0;
    for (var h = 0; h < buckets.length; h += 1) {
      total = Radd(total, buckets[h]);
      if (Rcmp(buckets[h], peak) > 0) { peak = buckets[h]; at = h; }
    }
    var meanRps = Rdiv(total, R(86400n, 1n)), peakRps = Rdiv(peak, R(3600n, 1n));
    return {
      total: total, peak: peak, peakHour: at, meanRps: meanRps, peakRps: peakRps,
      ratio: Rzero(meanRps) ? null : Rdiv(peakRps, meanRps)
    };
  }

  /* ============================ L8: machines ===============================

     Capacity per machine is one over the resource a request costs: a request
     that takes cost milliseconds of one core leaves a machine with cores cores
     able to serve cores * 1000 / cost a second. N is the CEILING of the peak
     over the usable capacity, because 3.2 machines is four, and the headroom is
     named rather than assumed: nFull is what sizing at 100% would have said. */
  function machineCount(peakRps, costMs, cores, rho) {
    var capacity = Rdiv(Rmul(R(BigInt(cores), 1n), R(1000n, 1n)), costMs);
    var usable = Rmul(capacity, rho);
    var exact = Rdiv(peakRps, usable);
    var n = Rceil(exact);
    var fleet = Rmul(R(n, 1n), capacity);
    return {
      capacity: capacity, usable: usable, exact: exact, n: n, fleet: fleet,
      utilisation: Rzero(fleet) ? null : Rdiv(peakRps, fleet),
      spare: Rzero(fleet) ? null : Rsub(fleet, peakRps),
      nFull: Rceil(Rdiv(peakRps, capacity))
    };
  }

  /* ============================ L9: the working set ========================

     The lesson's model: a stated hot fraction of the data takes a stated share
     of the traffic, and within each region the keys are equally popular. The
     hit rate is then piecewise linear in the cached fraction, with a knee where
     the hot region runs out, and workingSetFraction is its inverse. Course 4
     lesson 4 replaces the stated share with the Zipf curve; this is the version
     that can be done on an envelope. */
  function hitRateAt(hot, share, frac) {
    var one = R(1n, 1n);
    if (Rcmp(frac, hot) <= 0) return Rzero(hot) ? share : Rmul(share, Rdiv(frac, hot));
    var coldData = Rsub(one, hot);
    if (Rzero(coldData)) return one;
    return Radd(share, Rmul(Rsub(one, share), Rdiv(Rsub(frac, hot), coldData)));
  }
  function workingSetFraction(hot, share, target) {
    var one = R(1n, 1n);
    if (Rcmp(target, share) <= 0) return Rzero(share) ? one : Rmul(hot, Rdiv(target, share));
    var coldShare = Rsub(one, share);
    if (Rzero(coldShare)) return hot;
    return Radd(hot, Rmul(Rsub(one, hot), Rdiv(Rsub(target, share), coldShare)));
  }
  function workingSetBytes(datasetBytes, hot, share, target) {
    return Rmul(datasetBytes, workingSetFraction(hot, share, target));
  }

  /* ============================ L10: triangulation =========================

     Two chains, each a product of factors, and the ratio of their answers. The
     check passes when the ratio lies inside [1/k, k] for the half-width k that
     lesson 1 computed -- agreement is a claim about a range, never about two
     numbers being close.

     sharedFactors is the part that makes a fake check visible. A factor that
     appears in both chains with the same value cancels out of the ratio, so it
     cannot disagree, and a "check" resting on it has tested nothing. */
  function routeProduct(values) {
    var p = R(1n, 1n);
    for (var i = 0; i < values.length; i += 1) p = Rmul(p, values[i]);
    return p;
  }
  function routeRatio(a, b) { return Rzero(b) ? null : Rdiv(a, b); }
  function withinBand(ratio, k) {
    if (ratio === null || Rzero(k)) return false;
    return Rcmp(ratio, Rinv(k)) >= 0 && Rcmp(ratio, k) <= 0;
  }
  function sharedFactors(namesA, valuesA, namesB, valuesB) {
    var out = [];
    for (var i = 0; i < namesA.length; i += 1) {
      for (var j = 0; j < namesB.length; j += 1) {
        if (namesA[i] === namesB[j] && Requ(valuesA[i], valuesB[j])) { out.push(namesA[i]); break; }
      }
    }
    return out;
  }

  /* ============================ units ======================================

     Decimal units throughout -- kB is 1000 bytes, not 1024 -- because a link is
     sold in decimal and a disk is sold in decimal, and a course that mixes the
     two produces a 7% error it cannot see. The page states the convention. */
  var BYTE_UNITS = [['PB', 1000000000000000n], ['TB', 1000000000000n], ['GB', 1000000000n],
                    ['MB', 1000000n], ['kB', 1000n], ['B', 1n]];
  function fmtBytes(a, places) {
    for (var i = 0; i < BYTE_UNITS.length; i += 1) {
      if (i === BYTE_UNITS.length - 1 || Rcmp(a, R(BYTE_UNITS[i][1], 1n)) >= 0) {
        return showR(Rdiv(a, R(BYTE_UNITS[i][1], 1n)), places === undefined ? 2 : places)
          + ' ' + BYTE_UNITS[i][0];
      }
    }
  }
  /* The ladder every "how big is it" slider runs on: a 1, 1.5, 2, 3, 5, 7 rung
     in each decade, so an index is an exact rational and every worked example
     on the course lands on a rung. */
  var LADDER_MANT = [[1n, 1n], [3n, 2n], [2n, 1n], [3n, 1n], [5n, 1n], [7n, 1n]];
  function ladderValue(i) {
    if (i < 0) i = 0;
    var m = LADDER_MANT[i % 6], e = Math.floor(i / 6);
    return Rmul(R(m[0], m[1]), Rpow(R(10n, 1n), e));
  }
  function ladderIndex(mantIdx, decade) { return decade * 6 + mantIdx; }

  /* Superscript digits, so a decade reads 10⁷ on an SVG ruler where a
     <sup> tag cannot go. Presentation, but shared by four of the eight modes
     and therefore worth one definition rather than four. */
  var SUPERSCRIPT = ['\u2070', '\u00b9', '\u00b2', '\u00b3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079'];
  function supNum(v) {
    var s = Math.abs(v).toString(), out = '';
    for (var i = 0; i < s.length; i += 1) out += SUPERSCRIPT[+s.charAt(i)];
    return (v < 0 ? '\u207b' : '') + out;
  }
  function powTen(e) { return '10' + supNum(e); }

  /* a/b as a Number, safely at any size: exact division first, then the rounded
     logarithm, then back out of it. This is for PIXELS. Rnum would hand back
     NaN the moment either end left the exact-integer range of a double, which a
     cumulative byte count under a compounded growth factor does at once. */
  function ratioApprox(a, b) {
    if (Rzero(b)) return NaN;
    if (Rzero(a)) return 0;
    var q = Rdiv(a, b), sign = 1;
    if (q.n < 0n) { q = R(-q.n, q.d); sign = -1; }
    return sign * Math.pow(10, log10Approx(q));
  }
"""


# ---------------------------------------------------------------- furniture

_CORE_JS = RATIONAL_JS + BIGINT_JS + RCEIL_JS + APPROX_JS + ESTIMATE_JS


def _options(items, chosen):
    return "".join(
        '<option value="%s"%s>%s</option>'
        % (key, " selected" if key == chosen else "", label)
        for key, label in items
    )


def _select(cid, label, items, chosen):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n'
        "        </div>\n" % (cid, cid, label, cid, _options(items, chosen))
    )


def _range(cid, label, lo, hi, value, step=1):
    """One control: the row that names it, the readout, and the slider.

    The readout starts empty. Every number on the panel is written by redraw()
    from the arithmetic, so a lab whose script failed shows dashes rather than
    a plausible figure nothing computed.
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


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own, so this is how three lessons share one mode
    without any of them showing another lesson's numbers. An unknown preset
    raises for the same reason an unknown mode does: a silent fallback ships a
    page that looks finished and is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("estimate mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "estimate mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "estimate mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


# The nine ways a factor can be known. The first six are symmetric, which is
# lesson 1's case and the one where the geometric centre comes out exact; the
# last three are not, and are what the rounded root exists for.
PM_STEPS = [
    {"label": "known exactly", "down": [1, 1], "up": [1, 1], "text": "×1"},
    {"label": "± 1.5×", "down": [3, 2], "up": [3, 2], "text": "±1.5×"},
    {"label": "± 2×", "down": [2, 1], "up": [2, 1], "text": "±2×"},
    {"label": "± 3×", "down": [3, 1], "up": [3, 1], "text": "±3×"},
    {"label": "± 5×", "down": [5, 1], "up": [5, 1], "text": "±5×"},
    {"label": "± 10×", "down": [10, 1], "up": [10, 1], "text": "±10×"},
    {"label": "÷2 … ×3", "down": [2, 1], "up": [3, 1], "text": "÷2…×3"},
    {"label": "÷2 … ×5", "down": [2, 1], "up": [5, 1], "text": "÷2…×5"},
    {"label": "÷3 … ×10", "down": [3, 1], "up": [10, 1], "text": "÷3…×10"},
]


def _ladder(mant_index, decade):
    """Index on the 1, 1.5, 2, 3, 5, 7 ladder, in the given decade."""
    return decade * 6 + mant_index


# ============================================================ mode: magnitude

MAGNITUDE_PRESETS = [
    {
        "key": "ten-million-users",
        "label": "10M users × 100 actions/day × 1 kB, each known to a factor of 2",
        "answer": "bytes written per day",
        "factors": [
            {"name": "daily users", "unit": "users", "ladder": _ladder(0, 7), "pm": 2},
            {"name": "actions per user per day", "unit": "actions", "ladder": _ladder(0, 2), "pm": 2},
            {"name": "bytes per action", "unit": "bytes", "ladder": _ladder(0, 3), "pm": 2},
        ],
    },
    {
        "key": "photo-uploads",
        "label": "500k uploaders × 20 photos/day × 2 MB, known unevenly",
        "answer": "bytes uploaded per day",
        "factors": [
            {"name": "daily uploaders", "unit": "people", "ladder": _ladder(4, 5), "pm": 2},
            {"name": "photos per person per day", "unit": "photos", "ladder": _ladder(2, 1), "pm": 3},
            {"name": "bytes per photo", "unit": "bytes", "ladder": _ladder(2, 6), "pm": 1},
        ],
    },
    {
        "key": "sensor-fleet",
        "label": "1M sensors × 1000 events/day × 200 B, one factor known exactly",
        "answer": "bytes ingested per day",
        "factors": [
            {"name": "sensors deployed", "unit": "sensors", "ladder": _ladder(0, 6), "pm": 1},
            {"name": "events per sensor per day", "unit": "events", "ladder": _ladder(0, 3), "pm": 2},
            {"name": "bytes per event", "unit": "bytes", "ladder": _ladder(2, 2), "pm": 0},
        ],
    },
    {
        "key": "skewed-high",
        "label": "the same 10M users, with one factor skewed high (÷2 … ×3)",
        "answer": "bytes written per day",
        "factors": [
            {"name": "daily users", "unit": "users", "ladder": _ladder(0, 7), "pm": 2},
            {"name": "actions per user per day", "unit": "actions", "ladder": _ladder(0, 2), "pm": 6},
            {"name": "bytes per action", "unit": "bytes", "ladder": _ladder(0, 3), "pm": 2},
        ],
    },
]

MAGNITUDE_SCRIPT = r"""
  var sel = document.getElementById('mgPreset');
  var bars = document.getElementById('mgBars');
  var table = document.getElementById('mgTable');
  var status = document.getElementById('mgStatus');
  var C = ['mgC1', 'mgC2', 'mgC3'], K = ['mgK1', 'mgK2', 'mgK3'];

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('magnitude: no preset named ' + sel.value);
  }

  function applyPreset() {
    var p = preset();
    for (var i = 0; i < 3; i += 1) {
      document.getElementById(C[i]).value = p.factors[i].ladder;
      document.getElementById(K[i]).value = p.factors[i].pm;
    }
  }

  /* Every slider is an INDEX. The value it stands for is looked up here and
     nowhere else, so the number in the table and the number in the bar are the
     same exact rational rather than two roundings of one intention. */
  function readState() {
    var p = preset(), st = { p: p, centres: [], downs: [], ups: [], steps: [] };
    for (var i = 0; i < 3; i += 1) {
      var ci = +document.getElementById(C[i]).value, ki = +document.getElementById(K[i]).value;
      var step = PM[ki];
      st.centres.push(ladderValue(ci));
      st.downs.push(R(BigInt(step.down[0]), BigInt(step.down[1])));
      st.ups.push(R(BigInt(step.up[0]), BigInt(step.up[1])));
      st.steps.push(step);
      document.getElementById(C[i] + 'Lab').textContent =
        p.factors[i].name + ' — central value (' + p.factors[i].unit + ')';
      document.getElementById(K[i] + 'Lab').textContent =
        'how well ' + p.factors[i].name + ' is known';
      document.getElementById(C[i] + 'Out').textContent = showR(st.centres[i], 2);
      document.getElementById(K[i] + 'Out').textContent = step.label;
    }
    return st;
  }

  function drawBars(st, prod) {
    var lo = prod.lo, hi = prod.hi, i, flo, fhi;
    for (i = 0; i < 3; i += 1) {
      flo = Rdiv(st.centres[i], st.downs[i]);
      fhi = Rmul(st.centres[i], st.ups[i]);
      if (Rcmp(flo, lo) < 0) lo = flo;
      if (Rcmp(fhi, hi) > 0) hi = fhi;
    }
    /* Positions only. The ruler is logarithmic because that is the only scale
       on which a factor of two is the same distance everywhere, and the
       logarithm behind the pixel is rounded; every number printed is not. */
    var a = log10Approx(lo), b = log10Approx(hi), mid;
    if (!(b - a > 0.5)) { mid = (a + b) / 2; a = mid - 0.5; b = mid + 0.5; }
    var padv = (b - a) * 0.08;
    a -= padv; b += padv;
    function x(v) { return 14 + (log10Approx(v) - a) / (b - a) * 492; }
    var s = '', d;
    for (d = Math.ceil(a); d <= Math.floor(b); d += 1) {
      var px = 14 + (d - a) / (b - a) * 492;
      s += '<line x1="' + px.toFixed(1) + '" y1="16" x2="' + px.toFixed(1) + '" y2="146" stroke="var(--line)" stroke-dasharray="3 4" />'
        + '<text x="' + px.toFixed(1) + '" y="162" text-anchor="middle" font-size="11" fill="var(--muted)">' + powTen(d) + '</text>';
    }
    var ys = [38, 64, 90];
    for (i = 0; i < 3; i += 1) {
      flo = Rdiv(st.centres[i], st.downs[i]);
      fhi = Rmul(st.centres[i], st.ups[i]);
      var x0 = x(flo), x1 = x(fhi), xc = x(st.centres[i]);
      if (x1 - x0 < 3) x1 = x0 + 3;
      s += '<rect x="' + x0.toFixed(1) + '" y="' + (ys[i] - 5) + '" width="' + (x1 - x0).toFixed(1)
        + '" height="10" rx="3" fill="var(--cyan)" opacity="0.38" />'
        + '<line x1="' + xc.toFixed(1) + '" y1="' + (ys[i] - 8) + '" x2="' + xc.toFixed(1) + '" y2="' + (ys[i] + 8)
        + '" stroke="var(--green)" stroke-width="2" />'
        + '<text x="14" y="' + (ys[i] - 10) + '" font-size="11" fill="var(--muted)">' + st.p.factors[i].name
        + ' &#183; ' + st.steps[i].text + '</text>';
    }
    var px0 = x(prod.lo), px1 = x(prod.hi), pxc = x(prod.centre);
    if (px1 - px0 < 3) px1 = px0 + 3;
    s += '<rect x="' + px0.toFixed(1) + '" y="120" width="' + (px1 - px0).toFixed(1)
      + '" height="16" rx="4" fill="var(--amber)" opacity="0.42" />'
      + '<line x1="' + pxc.toFixed(1) + '" y1="116" x2="' + pxc.toFixed(1) + '" y2="140" stroke="var(--green)" stroke-width="2" />'
      + '<text x="14" y="112" font-size="11" fill="var(--text)">the product &#183; ' + st.p.answer + '</text>';
    bars.innerHTML = s;
  }

  function redraw() {
    var st = readState();
    var prod = productInterval(st.centres, st.downs, st.ups);
    var h = '<thead><tr><th>factor</th><th>central value</th><th>known to</th><th>low end</th><th>high end</th><th>width</th></tr></thead><tbody>';
    for (var i = 0; i < 3; i += 1) {
      var flo = Rdiv(st.centres[i], st.downs[i]), fhi = Rmul(st.centres[i], st.ups[i]);
      h += '<tr><td>' + st.p.factors[i].name + '</td><td>' + showR(st.centres[i], 2) + '</td><td>'
        + st.steps[i].text + '</td><td class="tone-cyan">' + showR(flo, 2) + '</td><td class="tone-amber">'
        + showR(fhi, 2) + '</td><td>' + Rtext(Rdiv(fhi, flo)) + '×</td></tr>';
    }
    h += '<tr><td><strong>product</strong></td><td><strong>' + showR(prod.centre, 2)
      + '</strong></td><td>÷' + Rtext(prod.down) + ' … ×' + Rtext(prod.up)
      + '</td><td class="tone-cyan"><strong>' + showR(prod.lo, 2) + '</strong></td><td class="tone-amber"><strong>'
      + showR(prod.hi, 2) + '</strong></td><td><strong>' + Rtext(prod.ratio) + '×</strong></td></tr>';
    table.innerHTML = h + '</tbody>';

    var exact = geoMeanExact(prod.lo, prod.hi);
    var mid = arithMid(prod.lo, prod.hi);
    var bracket = decadeBracket(prod.ratio);
    var decades = log10Approx(prod.ratio);
    document.getElementById('mgLo').textContent = showR(prod.lo, 2);
    document.getElementById('mgHi').textContent = showR(prod.hi, 2);
    document.getElementById('mgHalf').textContent = '÷' + Rtext(prod.down) + ' … ×' + Rtext(prod.up);
    document.getElementById('mgSpan').textContent = Rtextg(prod.ratio) + '×';
    document.getElementById('mgGeo').textContent = exact === null
      ? showR2(geoMeanApprox(prod.lo, prod.hi)) + ' (rounded)'
      : showR(exact, 2);
    document.getElementById('mgMid').textContent = showR(mid, 2);
    drawBars(st, prod);

    var ratioToCentre = Rdiv(mid, prod.centre);
    status.innerHTML = 'The three factors are known to '
      + st.steps[0].text + ', ' + st.steps[1].text + ' and ' + st.steps[2].text
      + ', so the product is known to <strong>÷' + Rtext(prod.down) + ' … ×' + Rtext(prod.up)
      + '</strong> — the half-widths multiply. End to end the interval is <strong>'
      + Rtextg(prod.ratio) + '×</strong> wide, which is between ' + powTen(bracket) + ' and '
      + powTen(bracket + 1) + ' (' + decades.toFixed(2) + ' powers of ten, rounded). '
      + (exact === null
          ? 'The interval is not symmetric, so its geometric centre is irrational and is printed rounded by Newton’s method: <strong>'
            + showR2(geoMeanApprox(prod.lo, prod.hi)) + '</strong>.'
          : 'The interval is symmetric, so its geometric centre is exactly the product of the central values: <strong>'
            + showR(exact, 2) + '</strong>.')
      + ' <span class="tone-red">The arithmetic midpoint is ' + showR(mid, 2) + '</span>, which is '
      + Rtext(ratioToCentre) + '× the estimate — an average of a low end and a high end that differ by a '
      + 'factor is dragged to the high end, which is why the honest centre of a multiplicative range is the geometric mean.';
  }

  /* A rounded Number, grouped the way an exact one is, so the two read alike
     and the page can say which is which rather than relying on their shape. */
  function showR2(v) {
    if (!isFinite(v)) return '—';
    return groupDec(Rtrim(v.toFixed(2)));
  }

  for (var i = 0; i < 3; i += 1) {
    document.getElementById(C[i]).addEventListener('input', redraw);
    document.getElementById(K[i]).addEventListener('input', redraw);
  }
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _magnitude(cfg):
    """Lesson 1: three ranged factors, and the interval their product lives in."""
    idx = _preset_index(cfg, MAGNITUDE_PRESETS, "magnitude")
    p = MAGNITUDE_PRESETS[idx]
    markup = (
        _toolbar(
            "Ranges multiply",
            "three factors, each an interval, and the interval their product lives in",
            _swatch("tone-cyan", "low end")
            + _swatch("tone-green", "central value")
            + _swatch("tone-amber", "high end"),
        )
        + '      <div class="lab-stage" id="mgStage" tabindex="0" role="region" aria-label="Each factor as an interval on a logarithmic ruler, with the product beneath.">'
        '<svg id="mgBars" style="min-width:520px" viewBox="0 0 520 176" role="img" '
        'aria-label="Factor intervals and the product interval on a logarithmic ruler."></svg></div>\n'
        '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="mgTable"></table></div>\n'
        '      <div class="status-banner" id="mgStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("mgPreset", "Worked example", [(q["key"], q["label"]) for q in MAGNITUDE_PRESETS], p["key"])
        + _range("mgC1", p["factors"][0]["name"], 0, 59, p["factors"][0]["ladder"])
        + _range("mgK1", "how well it is known", 0, len(PM_STEPS) - 1, p["factors"][0]["pm"])
        + _range("mgC2", p["factors"][1]["name"], 0, 59, p["factors"][1]["ladder"])
        + _range("mgK2", "how well it is known", 0, len(PM_STEPS) - 1, p["factors"][1]["pm"])
        + _range("mgC3", p["factors"][2]["name"], 0, 59, p["factors"][2]["ladder"])
        + _range("mgK3", "how well it is known", 0, len(PM_STEPS) - 1, p["factors"][2]["pm"])
        + _kpi([
            ("mgLo", "Low end"),
            ("mgHi", "High end"),
            ("mgHalf", "Product known to"),
            ("mgSpan", "High ÷ low"),
            ("mgGeo", "Geometric centre"),
            ("mgMid", "Arithmetic midpoint"),
        ])
    )
    script = (
        _CORE_JS
        + cfg_literal("PRESETS", MAGNITUDE_PRESETS)
        + cfg_literal("PM", PM_STEPS)
        + MAGNITUDE_SCRIPT
    )
    return Lab(
        title="Orders of magnitude",
        subtitle="Three factors, three intervals, one product",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set each factor and say how well you know it"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every end of every interval is an exact fraction, and the product interval is "
            "the product of the ends. The geometric centre is exact whenever the interval is "
            "symmetric; where it is not, the page says it is rounding and how.",
        ),
        script=script,
    )


# ================================================================= mode: rate


def _kpi_dyn(rows):
    """A kpi grid whose labels are written by redraw().

    The rate mode runs three different unit chains, and a chain that renamed its
    answer but not the label above it would be the exact defect the contract's
    "two modes must differ" rule exists to catch, one level down.
    """
    return (
        '        <div class="kpi-grid">\n'
        + "".join(
            '          <div class="kpi"><span id="%sLab">%s</span><strong id="%s">&mdash;</strong></div>\n'
            % (cid, label, cid)
            for cid, label in rows
        )
        + "        </div>\n"
    )


RATE_PRESETS = [
    {
        "key": "day-in-seconds",
        "label": "10M users × 100 actions a day — per day to per second",
        "a": _ladder(0, 7), "b": _ladder(0, 2), "c": _ladder(0, 3), "useC": False,
        "aLab": "daily users", "bLab": "actions per user per day", "cLab": "unused",
    },
    {
        "key": "read-write",
        "label": "10 000 requests a second, 100 reads to every write",
        "a": _ladder(0, 4), "b": _ladder(0, 2), "c": _ladder(0, 3), "useC": False,
        "aLab": "total requests per second", "bLab": "reads per write (the r in r:1)", "cLab": "unused",
    },
    {
        "key": "bandwidth",
        "label": "2 000 requests a second × 1 kB payload + 200 B of headers",
        "a": _ladder(2, 3), "b": _ladder(0, 3), "c": _ladder(2, 2), "useC": True,
        "aLab": "requests per second", "bLab": "payload bytes per request", "cLab": "header bytes per request",
    },
]

RATE_SCRIPT = r"""
  var sel = document.getElementById('rtPreset');
  var chainTable = document.getElementById('rtChain');
  var colsTable = document.getElementById('rtCols');
  var status = document.getElementById('rtStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('rate: no preset named ' + sel.value);
  }

  /* A proportion as a percentage: the exact fraction, with the decimal beside
     it, because "425/27%" is right and unreadable and "15.74%" is readable and
     rounded, and the reader is owed both. */
  function pct(frac) {
    var hundred = Rmul(frac, R(100n, 1n));
    var exact = Rtext(hundred), dec = Rtrim(Rround(hundred, 2));
    return exact === dec ? exact + '%' : dec + '% (' + exact + '%)';
  }

  function applyPreset() {
    var p = preset();
    document.getElementById('rtA').value = p.a;
    document.getElementById('rtB').value = p.b;
    document.getElementById('rtC').value = p.c;
  }

  /* Three chains, each assembled from the tested top-level functions rather
     than recomputed here: the chain is the bookkeeping, and the bookkeeping is
     what the lesson is about -- every row carries the unit its value leaves
     behind, so a missing "/s" is visible rather than merely wrong. */
  function chainFor(key, a, b, c) {
    var one = R(1n, 1n);
    if (key === 'day-in-seconds') {
      var daily = dailyVolume(a, b), exact = rpsExact(a, b), rounded = rpsRounded(a, b);
      return {
        steps: [
          { op: '', name: 'daily users', value: a, unit: 'users', run: a, runUnit: 'users' },
          { op: '×', name: 'actions per user per day', value: b, unit: 'actions / user / day', run: daily, runUnit: 'actions / day' },
          { op: '÷', name: 'seconds in a day', value: R(86400n, 1n), unit: 's / day', run: exact, runUnit: 'actions / s' }
        ],
        colA: 'dividing by 86 400', colB: 'dividing by 10⁵',
        rows: [
          { name: 'requests per second', a: exact, b: rounded, unit: 'req / s' },
          { name: 'requests per day', a: daily, b: daily, unit: 'req / day' }
        ],
        ratio: Rdiv(exact, rounded),
        kpi: [
          { label: 'Requests / s (exact)', value: showR(exact, 3) },
          { label: 'Requests / s (10⁵ day)', value: showR(rounded, 3) },
          { label: 'Shortcut day is longer by', value: pct(Rsub(dayLengthRatio(), one)) },
          { label: 'So the rate comes out low by', value: pct(Rsub(one, rateShortfallRatio())) }
        ],
        verdict: 'The shortcut day is <strong>' + Rtext(dayLengthRatio()) + '</strong> of a real day — '
          + pct(Rsub(dayLengthRatio(), one)) + ' too long, which is the 15.7% the lesson quotes. '
          + 'Dividing by it therefore makes the RATE <strong>' + Rtext(rateShortfallRatio()) + '</strong> of the truth, '
          + pct(Rsub(one, rateShortfallRatio())) + ' low, and those are two different percentages of '
          + 'the same approximation. Both are exact fractions: 10⁵/86 400 = ' + Rtext(dayLengthRatio())
          + ' and its reciprocal ' + Rtext(rateShortfallRatio()) + '. '
          + '<span class="tone-amber">Reading the chain upward</span> turns the rate back into a daily volume: '
          + showR(exact, 3) + ' req/s × 86 400 s/day = ' + showR(daily, 0) + ' req/day, which is where it started.'
      };
    }
    if (key === 'read-write') {
      var sp = splitRates(a, b);
      return {
        steps: [
          { op: '', name: 'total requests per second', value: a, unit: 'req / s', run: a, runUnit: 'req / s' },
          { op: '×', name: 'read share = r/(r+1)', value: sp.readShare, unit: 'reads / req', run: sp.reads, runUnit: 'reads / s' },
          { op: '×', name: 'write share = 1/(r+1)', value: sp.writeShare, unit: 'writes / req', run: sp.writes, runUnit: 'writes / s' }
        ],
        colA: 'the write share 1/(r+1)', colB: 'the instinct, 1/r',
        rows: [
          { name: 'write share', a: sp.writeShare, b: sp.naiveWriteShare, unit: 'of all requests' },
          { name: 'writes per second', a: sp.writes, b: Rmul(a, sp.naiveWriteShare), unit: 'writes / s' },
          { name: 'reads per second', a: sp.reads, b: Rmul(a, Rsub(one, sp.naiveWriteShare)), unit: 'reads / s' }
        ],
        ratio: sp.naiveOver,
        kpi: [
          { label: 'Reads / s', value: showR(sp.reads, 2) },
          { label: 'Writes / s', value: showR(sp.writes, 2) },
          { label: 'Read share (exact)', value: Rtext(sp.readShare) },
          { label: 'Write share (exact)', value: Rtext(sp.writeShare) }
        ],
        verdict: 'A ratio of <strong>' + Rtext(b) + ':1</strong> splits the rate into '
          + Rtext(sp.readShare) + ' reads and <strong>' + Rtext(sp.writeShare) + '</strong> writes — '
          + 'one part in ' + Rtext(Radd(b, one)) + ', not one part in ' + Rtext(b) + ', because the ratio counts '
          + 'reads AGAINST writes and the total is both. '
          + '<span class="tone-red">The instinct 1/r = ' + Rtext(sp.naiveWriteShare)
          + '</span> overstates the write rate by a factor of <strong>' + Rtext(sp.naiveOver) + '</strong>, which is '
          + pct(Rsub(sp.naiveOver, one)) + ' — small here, and it is the write path that '
          + 'sizes the storage and the replication. The two shares add to ' + Rtext(Radd(sp.readShare, sp.writeShare))
          + ', which the instinct’s pair does not.'
      };
    }
    if (key === 'bandwidth') {
      var per = requestBytes(b, c), bits = bandwidthBits(a, b, c);
      var mbit = bandwidthMbit(a, b, c), wrong = bandwidthNoEight(a, b, c);
      var share = headerShare(b, c), cross = headerCrossover(c);
      return {
        steps: [
          { op: '', name: 'requests per second', value: a, unit: 'req / s', run: a, runUnit: 'req / s' },
          { op: '×', name: 'bytes per request (payload + header)', value: per, unit: 'B / req', run: Rmul(a, per), runUnit: 'B / s' },
          { op: '×', name: 'bits per byte', value: R(8n, 1n), unit: 'bit / B', run: bits, runUnit: 'bit / s' },
          { op: '÷', name: 'bits per megabit', value: R(1000000n, 1n), unit: 'bit / Mbit', run: mbit, runUnit: 'Mbit / s' }
        ],
        colA: 'in bits, as a link is sold', colB: 'bytes ÷ 10⁶, the ×8 forgotten',
        rows: [
          { name: 'link rate', a: mbit, b: wrong, unit: 'Mbit / s' },
          { name: 'bytes per second', a: Rmul(a, per), b: Rmul(a, per), unit: 'B / s' }
        ],
        ratio: Rdiv(mbit, wrong),
        kpi: [
          { label: 'Link rate', value: showR(mbit, 3) + ' Mbit/s' },
          { label: 'Bytes per request', value: showR(per, 0) + ' B' },
          { label: 'Header share (exact)', value: Rtext(share) },
          { label: 'Headers are half below', value: showR(cross, 0) + ' B of payload' }
        ],
        verdict: 'The link carries <strong>' + showR(mbit, 3) + ' Mbit/s</strong>. '
          + 'Headers are <strong>' + Rtext(share) + '</strong> of the bytes on the wire ('
          + Rtrim(Rround(Rmul(share, R(100n, 1n)), 1)) + '%), and they are charged once per request whatever the '
          + 'payload: at a payload of <strong>' + showR(cross, 0) + ' B</strong>, the header size itself, they are '
          + 'exactly half the traffic, and below it they are the majority. '
          + '<span class="tone-red">Dividing the bytes by 10⁶ and calling the answer Mbit/s</span> gives '
          + showR(wrong, 3) + ', which is the truth divided by <strong>' + Rtext(Rdiv(mbit, wrong))
          + '</strong> — the factor of 8 is not a rounding, it is the whole difference between a byte and a bit. '
          + 'Mbit here is 10⁶ bits a second, which is what a link is sold in.'
      };
    }
    throw new Error('rate: no chain named ' + key);
  }

  function redraw() {
    var p = preset();
    var a = ladderValue(+document.getElementById('rtA').value);
    var b = ladderValue(+document.getElementById('rtB').value);
    var c = ladderValue(+document.getElementById('rtC').value);
    document.getElementById('rtALab').textContent = p.aLab;
    document.getElementById('rtBLab').textContent = p.bLab;
    document.getElementById('rtCLab').textContent = p.cLab;
    document.getElementById('rtAOut').textContent = showR(a, 2);
    document.getElementById('rtBOut').textContent = showR(b, 2);
    document.getElementById('rtCOut').textContent = showR(c, 2);
    document.getElementById('rtCRow').hidden = !p.useC;

    var ch = chainFor(p.key, a, b, c);
    var h = '<thead><tr><th></th><th>quantity</th><th>value</th><th>unit</th><th>running total</th><th>unit so far</th></tr></thead><tbody>';
    ch.steps.forEach(function (s) {
      h += '<tr><td class="tone-muted">' + (s.op || '&nbsp;') + '</td><td>' + s.name + '</td><td>'
        + showR(s.value, 3) + '</td><td class="tone-muted">' + s.unit + '</td><td>' + showR(s.run, 3)
        + '</td><td class="tone-cyan">' + s.runUnit + '</td></tr>';
    });
    chainTable.innerHTML = h + '</tbody>';

    var g = '<thead><tr><th>figure</th><th>' + ch.colA + '</th><th>' + ch.colB + '</th><th>unit</th></tr></thead><tbody>';
    ch.rows.forEach(function (r) {
      var same = Requ(r.a, r.b);
      g += '<tr><td>' + r.name + '</td><td class="tone-green">' + showR(r.a, 4) + '</td><td class="'
        + (same ? 'tone-muted' : 'tone-red') + '">' + showR(r.b, 4) + '</td><td class="tone-muted">'
        + r.unit + '</td></tr>';
    });
    g += '<tr><td><strong>ratio between the columns</strong></td><td colspan="3"><strong>'
      + Rtext(ch.ratio) + '</strong> &#183; exactly, as a fraction</td></tr>';
    colsTable.innerHTML = g + '</tbody>';

    for (var i = 0; i < 4; i += 1) {
      document.getElementById('rtK' + (i + 1) + 'Lab').textContent = ch.kpi[i].label;
      document.getElementById('rtK' + (i + 1)).textContent = ch.kpi[i].value;
    }
    status.innerHTML = ch.verdict;
  }

  ['rtA', 'rtB', 'rtC'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _rate(cfg):
    """Lessons 2, 3 and 5: one unit chain, three things it sizes."""
    idx = _preset_index(cfg, RATE_PRESETS, "rate")
    p = RATE_PRESETS[idx]
    markup = (
        _toolbar(
            "The unit chain",
            "write the units down first, because nearly every wrong estimate is a unit error",
            _swatch("tone-cyan", "unit carried forward")
            + _swatch("tone-green", "the figure that is right")
            + _swatch("tone-red", "the figure the shortcut gives"),
        )
        + '      <div class="lab-stage" id="rtStage" tabindex="0" role="region" aria-label="The unit chain, one row per step.">\n'
        '        <div class="table-wrap"><table class="tt" id="rtChain"></table></div>\n'
        "      </div>\n"
        '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="rtCols"></table></div>\n'
        '      <div class="status-banner" id="rtStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("rtPreset", "Worked example", [(q["key"], q["label"]) for q in RATE_PRESETS], p["key"])
        + _range("rtA", p["aLab"], 0, 59, p["a"])
        + _range("rtB", p["bLab"], 0, 59, p["b"])
        + _range("rtC", p["cLab"], 0, 59, p["c"])
        + _kpi_dyn([("rtK1", "&mdash;"), ("rtK2", "&mdash;"), ("rtK3", "&mdash;"), ("rtK4", "&mdash;")])
    )
    script = _CORE_JS + cfg_literal("PRESETS", RATE_PRESETS) + RATE_SCRIPT
    return Lab(
        title="Rates and unit chains",
        subtitle="Per day to per second, one rate into two, and bytes into bits",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose a chain, then move its factors"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each row carries the unit its value leaves behind, so the chain either arrives "
            "at the unit you wanted or visibly does not. Both result columns are exact "
            "fractions and so is the ratio between them.",
        ),
        script=script,
    )


# =========================================================== mode: accumulate

ACCUMULATE_PRESETS = [
    {
        "key": "event-log",
        "label": "500 GB a day, kept 90 days, growing 5% a month, 3 copies",
        "ingest": _ladder(4, 11), "days": 90, "growth": 5, "copies": 3,
        "what": "event log",
    },
    {
        "key": "flat-archive",
        "label": "2 TB a day, kept a year, no growth, 2 copies",
        "ingest": _ladder(2, 12), "days": 365, "growth": 0, "copies": 2,
        "what": "archive",
    },
    {
        "key": "fast-growth",
        "label": "100 GB a day, kept two years, growing 15% a month, 3 copies",
        "ingest": _ladder(0, 11), "days": 730, "growth": 15, "copies": 3,
        "what": "telemetry store",
    },
]

ACCUMULATE_SCRIPT = r"""
  var sel = document.getElementById('acPreset');
  var curve = document.getElementById('acCurve');
  var table = document.getElementById('acTable');
  var status = document.getElementById('acStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('accumulate: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('acIngest').value = p.ingest;
    document.getElementById('acDays').value = p.days;
    document.getElementById('acGrowth').value = p.growth;
    document.getElementById('acCopies').value = p.copies;
  }

  function drawCurve(rows, ingest, days) {
    /* Two cumulative curves against the same axis: the arithmetic series at
       constant ingest and the geometric one under growth. The pixels go
       through ratioApprox; every figure on the page and in the table does not. */
    var last = rows[rows.length - 1].running;
    var flatEnd = Rmul(ingest, R(BigInt(days), 1n));
    var top = Rcmp(last, flatEnd) > 0 ? last : flatEnd;
    if (Rzero(top)) top = R(1n, 1n);
    var n = rows.length;
    function px(i) { return 34 + (n < 2 ? 0.5 : i / (n - 1)) * 470; }
    function py(v) { return 168 - ratioApprox(v, top) * 148; }
    var s = '<line x1="34" y1="168" x2="508" y2="168" stroke="var(--line-strong)" />'
      + '<line x1="34" y1="14" x2="34" y2="168" stroke="var(--line-strong)" />';
    var flat = '', grow = '', running = R(0n, 1n), i;
    for (i = 0; i < n; i += 1) {
      running = Radd(running, Rmul(ingest, R(BigInt(rows[i].days), 1n)));
      flat += (i ? 'L' : 'M') + px(i).toFixed(1) + ' ' + py(running).toFixed(1) + ' ';
      grow += (i ? 'L' : 'M') + px(i).toFixed(1) + ' ' + py(rows[i].running).toFixed(1) + ' ';
    }
    s += '<path d="' + flat + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />'
      + '<path d="' + grow + '" fill="none" stroke="var(--amber)" stroke-width="2.6" />'
      + '<text x="40" y="26" font-size="11" fill="var(--amber)">with growth</text>'
      + '<text x="40" y="42" font-size="11" fill="var(--cyan)">constant ingest</text>'
      + '<text x="34" y="184" font-size="11" fill="var(--muted)">month 1</text>'
      + '<text x="508" y="184" text-anchor="end" font-size="11" fill="var(--muted)">month ' + n + '</text>'
      + '<text x="40" y="164" font-size="11" fill="var(--muted)">0</text>';
    curve.innerHTML = s;
  }

  function redraw() {
    var p = preset();
    var ingest = ladderValue(+document.getElementById('acIngest').value);
    var days = +document.getElementById('acDays').value;
    var pct = +document.getElementById('acGrowth').value;
    var copies = +document.getElementById('acCopies').value;
    var growth = R(BigInt(pct), 100n);
    document.getElementById('acIngestOut').textContent = fmtBytes(ingest, 2) + ' / day';
    document.getElementById('acDaysOut').textContent = days + ' days';
    document.getElementById('acGrowthOut').textContent = pct + '% a month';
    document.getElementById('acCopiesOut').textContent = copies + (copies === 1 ? ' copy' : ' copies');

    var rows = growthTerms(ingest, days, growth);
    var oneCopy = rows[rows.length - 1].running;
    var total = storageGrowth(ingest, days, growth, copies);
    var flat = storageFlat(ingest, days, copies);

    var h = '<thead><tr><th>month</th><th>days in it</th><th>ingest that month, per day</th>'
      + '<th>bytes added</th><th>held, one copy</th></tr></thead><tbody>';
    rows.forEach(function (r) {
      h += '<tr><td>' + (r.month + 1) + '</td><td>' + r.days + '</td><td>' + fmtBytes(r.rate, 2)
        + '</td><td class="tone-cyan">' + fmtBytes(r.bytes, 2) + '</td><td class="tone-amber">'
        + fmtBytes(r.running, 2) + '</td></tr>';
    });
    table.innerHTML = h + '</tbody>';
    drawCurve(rows, ingest, days);

    var growthOver = Rzero(flat) ? null : Rdiv(total, flat);
    document.getElementById('acTotal').textContent = fmtBytes(total, 2);
    document.getElementById('acFlat').textContent = fmtBytes(flat, 2);
    document.getElementById('acOne').textContent = fmtBytes(oneCopy, 2);
    document.getElementById('acRatio').textContent = growthOver === null ? '—' : showR(growthOver, 4) + '×';
    document.getElementById('acLast').textContent = fmtBytes(rows[rows.length - 1].rate, 2) + ' / day';
    document.getElementById('acMonths').textContent = rows.length;

    status.innerHTML = 'Over ' + days + ' days the ' + p.what + ' accumulates <strong>'
      + fmtBytes(oneCopy, 2) + '</strong> of unique data, and at ' + copies
      + (copies === 1 ? ' copy' : ' copies') + ' it occupies <strong>' + fmtBytes(total, 2) + '</strong>. '
      + 'Rate × time alone would have said ' + fmtBytes(Rmul(ingest, R(BigInt(days), 1n)), 2)
      + ' — <span class="tone-red">short by the growth and short again by the replication</span>, a factor of '
      + (growthOver === null ? '—' : showR(Rmul(growthOver, R(BigInt(copies), 1n)), 3))
      + ' once both are put back. ' + (pct === 0
          ? 'At 0% growth the series is arithmetic: ' + rows.length + ' equal terms, and the sum is just rate × days.'
          : 'The series is geometric with ratio ' + Rtext(Radd(R(1n, 1n), growth)) + ': ingest compounds once a month, '
            + 'so the window is ' + rows.length + ' blocks each at its own constant rate, and by the last block the daily '
            + 'ingest has reached ' + fmtBytes(rows[rows.length - 1].rate, 2) + ', '
            + showR(Rdiv(rows[rows.length - 1].rate, ingest), 3) + '× where it started. Every term is exact: '
            + 'the month-m rate is ingest × (' + Rtext(Radd(R(1n, 1n), growth)) + ')^m with both ends integers.')
      + ' Units are decimal — 1 kB is 1000 B — which is what a disk is sold in.';
  }

  ['acIngest', 'acDays', 'acGrowth', 'acCopies'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _accumulate(cfg):
    """Lesson 4: storage is a sum of a rate over a window, then copies."""
    idx = _preset_index(cfg, ACCUMULATE_PRESETS, "accumulate")
    p = ACCUMULATE_PRESETS[idx]
    markup = (
        _toolbar(
            "Storage over a retention window",
            "a sum of a rate, term by term, then multiplied by the copies",
            _swatch("tone-cyan", "constant ingest") + _swatch("tone-amber", "with growth"),
        )
        + '      <div class="lab-stage" id="acStage" tabindex="0" role="region" aria-label="Cumulative bytes held, constant ingest against compounded growth.">'
        '<svg id="acCurve" style="min-width:520px" viewBox="0 0 520 192" role="img" '
        'aria-label="Two cumulative storage curves over the retention window."></svg></div>\n'
        '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="acTable"></table></div>\n'
        '      <div class="status-banner" id="acStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("acPreset", "Worked example", [(q["key"], q["label"]) for q in ACCUMULATE_PRESETS], p["key"])
        + _range("acIngest", "bytes ingested per day", 0, 89, p["ingest"])
        + _range("acDays", "retention window, in days", 1, 1095, p["days"])
        + _range("acGrowth", "growth, % a month", 0, 30, p["growth"])
        + _range("acCopies", "copies kept (replication factor)", 1, 6, p["copies"])
        + _kpi([
            ("acTotal", "Storage, all copies"),
            ("acFlat", "If ingest never grew"),
            ("acOne", "Unique data, one copy"),
            ("acRatio", "Growth costs"),
            ("acLast", "Ingest in the last month"),
            ("acMonths", "Monthly blocks"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", ACCUMULATE_PRESETS) + ACCUMULATE_SCRIPT
    return Lab(
        title="Storage from ingest and retention",
        subtitle="An arithmetic series at constant ingest, a geometric one under growth",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the ingest, the window, the growth and the copies"),
        panel_intro=cfg.get(
            "panel_intro",
            "Growth compounds once a month, so the window is a run of 30-day blocks each at "
            "its own constant rate and every term is an exact power. The table is the series; "
            "the total is its sum, times the copies.",
        ),
        script=script,
    )


# ================================================================ mode: scale

# Reference latencies in nanoseconds. These are lesson DATA -- measured figures
# the course quotes and prints in full -- and the only thing computed from them
# is the ratio between two, which is computed exactly.
RUNGS = [
    {"key": "l1", "label": "L1 cache reference", "ns": 1},
    {"key": "mispredict", "label": "branch mispredict", "ns": 3},
    {"key": "l2", "label": "L2 cache reference", "ns": 4},
    {"key": "mutex", "label": "mutex lock and unlock", "ns": 17},
    {"key": "ram", "label": "main memory reference", "ns": 100},
    {"key": "compress", "label": "compress 1 kB", "ns": 2000},
    {"key": "net1kb", "label": "send 1 kB over a 1 Gbit/s link", "ns": 10000},
    {"key": "ssdread", "label": "SSD random read", "ns": 150000},
    {"key": "ram1mb", "label": "read 1 MB sequentially from memory", "ns": 250000},
    {"key": "dcrt", "label": "round trip inside one datacentre", "ns": 500000},
    {"key": "ssd1mb", "label": "read 1 MB sequentially from SSD", "ns": 1000000},
    {"key": "seek", "label": "disk seek", "ns": 10000000},
    {"key": "disk1mb", "label": "read 1 MB sequentially from disk", "ns": 20000000},
    {"key": "continent", "label": "packet California to the Netherlands and back", "ns": 150000000},
]

SCALE_PRESETS = [
    {"key": "ram-vs-disk", "label": "main memory against a disk seek", "slow": "seek", "fast": "ram"},
    {"key": "l1-vs-ssd", "label": "L1 cache against an SSD random read", "slow": "ssdread", "fast": "l1"},
    {"key": "dc-vs-continent", "label": "a datacentre round trip against a cross-continent one", "slow": "continent", "fast": "dcrt"},
    {"key": "ssd-vs-disk", "label": "1 MB from SSD against 1 MB from disk", "slow": "disk1mb", "fast": "ssd1mb"},
]

SCALE_SCRIPT = r"""
  var slowSel = document.getElementById('scSlow'), fastSel = document.getElementById('scFast');
  var ruler = document.getElementById('scRuler');
  var status = document.getElementById('scStatus');

  function rung(key) {
    for (var i = 0; i < RUNGS.length; i += 1) if (RUNGS[i].key === key) return RUNGS[i];
    throw new Error('scale: no rung named ' + key);
  }
  function indexOfRung(key) {
    for (var i = 0; i < RUNGS.length; i += 1) if (RUNGS[i].key === key) return i;
    throw new Error('scale: no rung named ' + key);
  }

  function draw(slow, fast) {
    /* One row per rung, its bar drawn on a logarithmic axis. The logarithm is
       rounded and is used for PIXELS only: the ratio the lesson is about is a
       quotient of two integers and is printed exactly beneath. */
    var maxLog = Math.log10(RUNGS[RUNGS.length - 1].ns);
    var left = 246, right = 508, span = right - left;
    function x(ns) { return left + (Math.log10(ns) / maxLog) * span; }
    var s = '', d;
    for (d = 0; d <= Math.floor(maxLog); d += 1) {
      var gx = left + (d / maxLog) * span;
      s += '<line x1="' + gx.toFixed(1) + '" y1="10" x2="' + gx.toFixed(1) + '" y2="' + (14 + RUNGS.length * 20)
        + '" stroke="var(--line)" stroke-dasharray="3 4" />'
        + '<text x="' + gx.toFixed(1) + '" y="' + (30 + RUNGS.length * 20) + '" text-anchor="middle" font-size="10" fill="var(--muted)">'
        + powTen(d) + ' ns</text>';
    }
    RUNGS.forEach(function (r, i) {
      var y = 22 + i * 20, picked = r.key === slow.key || r.key === fast.key;
      var colour = r.key === slow.key ? 'var(--amber)' : (r.key === fast.key ? 'var(--cyan)' : 'var(--line-strong)');
      s += '<text x="6" y="' + (y + 4) + '" font-size="11" fill="' + (picked ? 'var(--text)' : 'var(--muted)') + '">'
        + r.label + '</text>'
        + '<rect x="' + left + '" y="' + (y - 4) + '" width="' + Math.max(2, x(r.ns) - left).toFixed(1)
        + '" height="8" rx="3" fill="' + colour + '" opacity="' + (picked ? '0.95' : '0.3') + '" />';
    });
    var ySlow = 22 + indexOfRung(slow.key) * 20, yFast = 22 + indexOfRung(fast.key) * 20;
    s += '<line x1="' + x(slow.ns).toFixed(1) + '" y1="' + ySlow + '" x2="' + x(slow.ns).toFixed(1) + '" y2="' + yFast
      + '" stroke="var(--green)" stroke-width="1.5" stroke-dasharray="4 3" />'
      + '<line x1="' + x(fast.ns).toFixed(1) + '" y1="' + yFast + '" x2="' + x(slow.ns).toFixed(1) + '" y2="' + yFast
      + '" stroke="var(--green)" stroke-width="2" />';
    ruler.innerHTML = s;
  }

  function redraw() {
    var slow = rung(slowSel.value), fast = rung(fastSel.value);
    var ratio = rungRatio(slow.ns, fast.ns);
    var bracket = decadeBracket(ratio);
    var span = rungRatio(RUNGS[RUNGS.length - 1].ns, RUNGS[0].ns);
    draw(slow, fast);

    document.getElementById('scSlowNs').textContent = group(BigInt(slow.ns)) + ' ns';
    document.getElementById('scFastNs').textContent = group(BigInt(fast.ns)) + ' ns';
    document.getElementById('scRatio').textContent = Rtextg(ratio);
    document.getElementById('scBracket').textContent = bracket === null
      ? '—' : powTen(bracket) + ' ≤ ratio < ' + powTen(bracket + 1);
    document.getElementById('scSpan').textContent = Rtextg(span) + '×';
    document.getElementById('scHuman').textContent = showR(ratio, 2);

    var same = slow.key === fast.key;
    status.innerHTML = same
      ? 'Both ends of the comparison are <strong>' + slow.label + '</strong>, so the ratio is '
        + Rtextg(ratio) + '. Pick two different rungs.'
      : '<strong>' + group(BigInt(slow.ns)) + ' ns ÷ ' + group(BigInt(fast.ns)) + ' ns = '
        + Rtextg(ratio) + '</strong> — that many <em>' + fast.label + '</em>s fit inside one <em>'
        + slow.label + '</em>. The ratio sits between ' + powTen(bracket) + ' and ' + powTen(bracket + 1)
        + ', which is the only form worth remembering: the ruler is logarithmic because a factor of ten is '
        + 'the same distance everywhere on it, and <span class="tone-red">a linear intuition puts every rung '
        + 'below ' + powTen(Math.floor(Math.log10(RUNGS[RUNGS.length - 1].ns)))
        + ' ns on top of each other</span>. End to end the ruler spans ' + Rtextg(span)
        + '×, from ' + RUNGS[0].label + ' to ' + RUNGS[RUNGS.length - 1].label
        + '. Both ends are integers, so the quotient is exact — only where a bar is DRAWN goes through a '
        + 'rounded logarithm.';
  }

  slowSel.addEventListener('change', redraw);
  fastSel.addEventListener('change', redraw);
  redraw(); window.redrawLab = redraw;
"""


def _scale(cfg):
    """Lesson 6: the latency ladder, and the ratio between two of its rungs."""
    idx = _preset_index(cfg, SCALE_PRESETS, "scale")
    p = SCALE_PRESETS[idx]
    opts = [(r["key"], r["label"]) for r in RUNGS]
    height = 40 + len(RUNGS) * 20
    markup = (
        _toolbar(
            "The latency ladder",
            "ten thousand million to one, on the only ruler that holds it",
            _swatch("tone-amber", "the slower operation") + _swatch("tone-cyan", "the faster one"),
        )
        + '      <div class="lab-stage" id="scStage" tabindex="0" role="region" aria-label="Reference latencies on a logarithmic ruler.">'
        '<svg id="scRuler" style="min-width:520px" viewBox="0 0 520 %d" role="img" '
        'aria-label="Each reference latency drawn as a bar on a logarithmic scale."></svg></div>\n'
        '      <div class="status-banner" id="scStatus" style="margin-top:12px;"></div>' % height
    )
    controls = (
        _select("scSlow", "The slower operation", opts, p["slow"])
        + _select("scFast", "The faster operation", opts, p["fast"])
        + _kpi([
            ("scSlowNs", "The slower one"),
            ("scFastNs", "The faster one"),
            ("scRatio", "Exact ratio"),
            ("scHuman", "As a decimal"),
            ("scBracket", "Which decade"),
            ("scSpan", "The whole ruler spans"),
        ])
    )
    script = _CORE_JS + cfg_literal("RUNGS", RUNGS) + SCALE_SCRIPT
    return Lab(
        title="Latency numbers on a log scale",
        subtitle="Pick two rungs; the ratio is the knowledge",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick two operations to compare"),
        panel_intro=cfg.get(
            "panel_intro",
            "The rungs are measured reference figures and are printed in full. The ratio "
            "between any two is a quotient of integers and is exact; the rounded logarithm "
            "is used only to decide where a bar is drawn.",
        ),
        script=script,
    )


# ================================================================= mode: peak

PEAK_PRESETS = [
    {
        "key": "consumer-evening",
        "label": "a consumer app: one evening peak at 21:00",
        "shape": "office", "hour": 21, "amp": 6, "base": _ladder(0, 6),
        "what": "consumer app",
    },
    {
        "key": "office-hours",
        "label": "a business app: two humps either side of lunch",
        "shape": "twopeak", "hour": 10, "amp": 5, "base": _ladder(4, 5),
        "what": "business app",
    },
    {
        "key": "flat-internal",
        "label": "an internal service with no daily shape at all",
        "shape": "flat", "hour": 12, "amp": 0, "base": _ladder(2, 5),
        "what": "internal service",
    },
    {
        "key": "broadcast-spike",
        "label": "a broadcast: one hour carries the day",
        "shape": "spike", "hour": 19, "amp": 10, "base": _ladder(0, 5),
        "what": "broadcast",
    },
]

PEAK_SCRIPT = r"""
  var sel = document.getElementById('pkPreset');
  var barsEl = document.getElementById('pkBars');
  var status = document.getElementById('pkStatus');
  var hourS = document.getElementById('pkHour'), liftS = document.getElementById('pkLift');
  /* One hand-edit per hour, kept here so the reader can shape several bars in
     turn. redraw() only READS it, which is why a second redraw is harmless. */
  var LIFT = [];
  for (var z = 0; z < 24; z += 1) LIFT.push(100);

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('peak: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('pkPeakHour').value = p.hour;
    document.getElementById('pkAmp').value = p.amp;
    document.getElementById('pkBase').value = p.base;
    for (var i = 0; i < 24; i += 1) LIFT[i] = 100;
    liftS.value = 100;
  }

  function buckets() {
    var p = preset();
    var base = ladderValue(+document.getElementById('pkBase').value);
    var w = profileWeights(p.shape, +document.getElementById('pkPeakHour').value,
                           +document.getElementById('pkAmp').value);
    var out = [];
    for (var h = 0; h < 24; h += 1) {
      out.push(Rmul(base, Rmul(R(BigInt(w[h]), 1n), R(BigInt(LIFT[h]), 100n))));
    }
    return out;
  }

  function draw(bs, st, chosen) {
    var top = st.peak;
    if (Rzero(top)) top = R(1n, 1n);
    var s = '', h, x, bh;
    var meanPerHour = Rdiv(st.total, R(24n, 1n));
    for (h = 0; h < 24; h += 1) {
      x = 22 + h * 20;
      bh = ratioApprox(bs[h], top) * 140;
      s += '<rect x="' + x + '" y="' + (162 - bh).toFixed(1) + '" width="15" height="' + Math.max(1, bh).toFixed(1)
        + '" rx="2" fill="' + (h === st.peakHour ? 'var(--amber)' : (h === chosen ? 'var(--purple)' : 'var(--cyan)'))
        + '" opacity="' + (h === st.peakHour || h === chosen ? '0.95' : '0.55') + '" />';
      if (h % 3 === 0) {
        s += '<text x="' + (x + 7) + '" y="178" text-anchor="middle" font-size="10" fill="var(--muted)">' + h + '</text>';
      }
    }
    var my = 162 - ratioApprox(meanPerHour, top) * 140;
    s += '<line x1="18" y1="' + my.toFixed(1) + '" x2="504" y2="' + my.toFixed(1)
      + '" stroke="var(--green)" stroke-width="1.6" stroke-dasharray="5 4" />'
      + '<text x="504" y="' + (my - 5).toFixed(1) + '" text-anchor="end" font-size="10" fill="var(--green)">mean hour</text>'
      + '<line x1="18" y1="162" x2="504" y2="162" stroke="var(--line-strong)" />';
    barsEl.innerHTML = s;
  }

  function redraw() {
    var p = preset();
    var chosen = +hourS.value;
    var bs = buckets(), st = peakStats(bs);
    document.getElementById('pkPeakHourOut').textContent = document.getElementById('pkPeakHour').value + ':00';
    document.getElementById('pkAmpOut').textContent = document.getElementById('pkAmp').value;
    var quietest = bs[0];
    for (var q = 1; q < 24; q += 1) if (Rcmp(bs[q], quietest) < 0) quietest = bs[q];
    document.getElementById('pkBaseOut').textContent = showR(quietest, 0) + ' req in the quietest hour';
    document.getElementById('pkHourOut').textContent = chosen + ':00 (now at ' + LIFT[chosen] + '% of its shaped height)';
    document.getElementById('pkLiftOut').textContent = LIFT[chosen] + '%';
    draw(bs, st, chosen);

    document.getElementById('pkPeakRps').textContent = showR(st.peakRps, 2) + ' req/s';
    document.getElementById('pkMeanRps').textContent = showR(st.meanRps, 2) + ' req/s';
    document.getElementById('pkRatio').textContent = st.ratio === null ? '—' : Rtext(st.ratio);
    document.getElementById('pkRatioDec').textContent = st.ratio === null ? '—' : showR(st.ratio, 3) + '×';
    document.getElementById('pkTotal').textContent = showR(st.total, 0) + ' req/day';
    document.getElementById('pkWhen').textContent = st.peakHour + ':00';

    var shortfall = st.ratio === null ? null : Rsub(st.peakRps, st.meanRps);
    status.innerHTML = 'The ' + p.what + ' takes <strong>' + showR(st.total, 0) + '</strong> requests a day. '
      + 'Dividing that by 86 400 gives <strong>' + showR(st.meanRps, 2) + ' req/s</strong> — '
      + '<span class="tone-red">the number you must not size to</span>. The busiest hour is '
      + st.peakHour + ':00, carrying ' + showR(st.peak, 0) + ' requests, which is <strong>'
      + showR(st.peakRps, 2) + ' req/s</strong>. '
      + (st.ratio === null ? '' : 'Peak over mean is <strong>' + Rtext(st.ratio)
          + '</strong> exactly — 24 × the busiest bucket over the day’s total, both integers — or '
          + showR(st.ratio, 3) + '×. Provisioning for the mean would leave you '
          + showR(shortfall, 2) + ' req/s short at the peak, every day, at the hour it matters. ')
      + 'You pay for the mean and you build for the peak, and the multiplier between them came from this profile, '
      + 'not from a rule of thumb: flatten the shape and it falls to 1.';
  }

  ['pkPeakHour', 'pkAmp', 'pkBase'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  hourS.addEventListener('input', function () { liftS.value = LIFT[+hourS.value]; redraw(); });
  liftS.addEventListener('input', function () { LIFT[+hourS.value] = +liftS.value; redraw(); });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _peak(cfg):
    """Lesson 7: a daily profile, its peak, its mean, and the ratio."""
    idx = _preset_index(cfg, PEAK_PRESETS, "peak")
    p = PEAK_PRESETS[idx]
    markup = (
        _toolbar(
            "The daily profile",
            "twenty-four buckets; you pay for the mean and build for the peak",
            _swatch("tone-amber", "the busiest hour")
            + _swatch("tone-purple", "the hour you are editing")
            + _swatch("tone-green", "the mean hour"),
        )
        + '      <div class="lab-stage" id="pkStage" tabindex="0" role="region" aria-label="Requests in each hour of the day, with the mean marked.">'
        '<svg id="pkBars" style="min-width:520px" viewBox="0 0 520 188" role="img" '
        'aria-label="Twenty-four hourly buckets with the peak and the mean marked."></svg></div>\n'
        '      <div class="status-banner" id="pkStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("pkPreset", "Worked example", [(q["key"], q["label"]) for q in PEAK_PRESETS], p["key"])
        + _range("pkPeakHour", "when the busy period is centred", 0, 23, p["hour"])
        + _range("pkAmp", "how pronounced the shape is", 0, 12, p["amp"])
        + _range("pkBase", "how big the day is (scales every bucket)", 0, 71, p["base"])
        + _range("pkHour", "shape one hour by hand: which hour", 0, 23, 12)
        + _range("pkLift", "… and its height, as a % of the shape", 0, 400, 100, 5)
        + _kpi([
            ("pkPeakRps", "Peak"),
            ("pkMeanRps", "Mean"),
            ("pkRatio", "Peak / mean, exact"),
            ("pkRatioDec", "Peak / mean"),
            ("pkTotal", "Requests a day"),
            ("pkWhen", "Busiest hour"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", PEAK_PRESETS) + PEAK_SCRIPT
    return Lab(
        title="Peak to average",
        subtitle="The provisioning multiplier comes from the profile",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Shape the day"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each bucket is an exact multiple of the quietest hour, so the daily total is "
            "exact and peak over mean is 24 × the busiest bucket over that total — "
            "a ratio of two integers, not a rule of thumb.",
        ),
        script=script,
    )


# ============================================================= mode: machines

MACHINES_PRESETS = [
    {
        "key": "checkout-api",
        "label": "a checkout API: 20 000 req/s peak, 40 ms of one core each, 8 cores, 60% target",
        "peak": _ladder(2, 4), "cost": 400, "cores": 8, "rho": 60, "what": "checkout API",
    },
    {
        "key": "thumbnailer",
        "label": "an image thumbnailer: 2 000 req/s, 250 ms each, 16 cores, 70% target",
        "peak": _ladder(2, 3), "cost": 2500, "cores": 16, "rho": 70, "what": "thumbnailer",
    },
    {
        "key": "static-edge",
        "label": "a static edge: 500 000 req/s, 2 ms each, 4 cores, 80% target",
        "peak": _ladder(4, 5), "cost": 20, "cores": 4, "rho": 80, "what": "edge cache",
    },
]

MACHINES_SCRIPT = r"""
  var sel = document.getElementById('mcPreset');
  var stair = document.getElementById('mcStair');
  var status = document.getElementById('mcStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('machines: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('mcPeak').value = p.peak;
    document.getElementById('mcCost').value = p.cost;
    document.getElementById('mcCores').value = p.cores;
    document.getElementById('mcRho').value = p.rho;
  }

  function drawStair(peak, usable, res) {
    /* N against the peak rate, in a window six machines wide either side, so
       that the step structure is the thing you see: N is a CEILING, and the
       point sitting partway up a tread is what "3.2 machines is four" means. */
    var six = Rmul(usable, R(6n, 1n));
    var lo = Rsub(peak, six), hi = Radd(peak, six);
    if (lo.n < 0n) lo = R(0n, 1n);
    if (Rcmp(hi, lo) <= 0) hi = Radd(lo, R(1n, 1n));
    var nLo = Rceil(Rdiv(lo, usable)), nHi = Rceil(Rdiv(hi, usable));
    var yLo = Number(nLo) - 1, yHi = Number(nHi) + 1;
    if (yLo < 0) yLo = 0;
    if (yHi <= yLo) yHi = yLo + 1;
    function px(v) { return 40 + ratioApprox(Rsub(v, lo), Rsub(hi, lo)) * 466; }
    function py(n) { return 156 - ((n - yLo) / (yHi - yLo)) * 138; }
    var s = '<line x1="40" y1="156" x2="506" y2="156" stroke="var(--line-strong)" />'
      + '<line x1="40" y1="12" x2="40" y2="156" stroke="var(--line-strong)" />';
    var d = '', prev = null, i;
    for (i = 0; i <= 240; i += 1) {
      var x = Radd(lo, Rmul(Rsub(hi, lo), R(BigInt(i), 240n)));
      var n = Number(Rceil(Rdiv(x, usable)));
      if (prev !== null && n !== prev) d += 'L' + px(x).toFixed(1) + ' ' + py(n).toFixed(1) + ' ';
      d += (i === 0 ? 'M' : 'L') + px(x).toFixed(1) + ' ' + py(n).toFixed(1) + ' ';
      prev = n;
    }
    s += '<path d="' + d + '" fill="none" stroke="var(--cyan)" stroke-width="2.2" />';
    var xp = px(peak), yp = py(Number(res.n));
    s += '<line x1="' + xp.toFixed(1) + '" y1="12" x2="' + xp.toFixed(1) + '" y2="156" stroke="var(--amber)" stroke-dasharray="4 3" />'
      + '<circle cx="' + xp.toFixed(1) + '" cy="' + yp.toFixed(1) + '" r="4.5" fill="var(--amber)" />'
      + '<text x="' + Math.min(xp + 8, 430).toFixed(1) + '" y="' + Math.max(yp - 9, 22).toFixed(1)
      + '" font-size="11" fill="var(--amber)">N = ' + res.n + ' at the peak</text>'
      + '<text x="6" y="' + py(yHi - 1).toFixed(1) + '" font-size="10" fill="var(--muted)">' + (yHi - 1) + '</text>'
      + '<text x="6" y="' + py(yLo).toFixed(1) + '" font-size="10" fill="var(--muted)">' + yLo + '</text>'
      + '<text x="40" y="172" font-size="10" fill="var(--muted)">' + showR(lo, 0) + ' req/s</text>'
      + '<text x="506" y="172" text-anchor="end" font-size="10" fill="var(--muted)">' + showR(hi, 0) + ' req/s</text>';
    stair.innerHTML = s;
  }

  function redraw() {
    var p = preset();
    var peak = ladderValue(+document.getElementById('mcPeak').value);
    var tenths = +document.getElementById('mcCost').value;
    var cost = R(BigInt(tenths), 10n);
    var cores = +document.getElementById('mcCores').value;
    var rhoPct = +document.getElementById('mcRho').value;
    var rho = R(BigInt(rhoPct), 100n);
    document.getElementById('mcPeakOut').textContent = showR(peak, 0) + ' req/s at the peak';
    document.getElementById('mcCostOut').textContent = Rtrim(Rround(cost, 1)) + ' ms of one core';
    document.getElementById('mcCoresOut').textContent = cores + (cores === 1 ? ' core' : ' cores');
    document.getElementById('mcRhoOut').textContent = rhoPct + '% target utilisation';

    var res = machineCount(peak, cost, cores, rho);
    drawStair(peak, res.usable, res);
    document.getElementById('mcCap').textContent = showR(res.capacity, 2) + ' req/s';
    document.getElementById('mcUsable').textContent = showR(res.usable, 2) + ' req/s';
    document.getElementById('mcExact').textContent = Rtext(res.exact);
    document.getElementById('mcN').textContent = String(res.n);
    document.getElementById('mcUtil').textContent = res.utilisation === null
      ? '—' : Rtrim(Rround(Rmul(res.utilisation, R(100n, 1n)), 2)) + '%';
    document.getElementById('mcFull').textContent = String(res.nFull);

    status.innerHTML = 'One machine serves <strong>' + showR(res.capacity, 2) + ' req/s</strong> — '
      + cores + ' cores × 1000 ms/s ÷ ' + Rtrim(Rround(cost, 1))
      + ' ms per request, which is one over the resource a request costs. At a target of ' + rhoPct
      + '% that machine is allowed <strong>' + showR(res.usable, 2) + ' req/s</strong>, so the fleet needs '
      + '<strong>' + Rtext(res.exact) + '</strong> machines — and machines are integers, so '
      + '<strong>N = ' + res.n + '</strong>. At N the peak sits at ' + (res.utilisation === null ? '—'
        : Rtrim(Rround(Rmul(res.utilisation, R(100n, 1n)), 2)) + '%')
      + ' of the fleet, leaving ' + showR(res.spare, 2) + ' req/s of headroom. '
      + '<span class="tone-red">Sizing at 100% would have said ' + res.nFull + '</span>, which is '
      + (res.nFull === res.n ? 'the same answer here and is still the wrong reasoning'
         : (res.n - res.nFull) + ' fewer machines and no room for a failure, a deploy or a bad afternoon')
      + '. The ' + rhoPct + '% is taken as given on this course; “Queues and Utilisation” is where it is earned, and the knee '
      + 'in the queueing curve is the reason it is not 95%.';
  }

  ['mcPeak', 'mcCost', 'mcCores', 'mcRho'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _machines(cfg):
    """Lesson 8: a request's cost, a headroom, and the integer that falls out."""
    idx = _preset_index(cfg, MACHINES_PRESETS, "machines")
    p = MACHINES_PRESETS[idx]
    markup = (
        _toolbar(
            "From a request's cost to a machine count",
            "N = ⌈peak / (capacity × ρ)⌉, and the ceiling is the lesson",
            _swatch("tone-cyan", "machines needed") + _swatch("tone-amber", "your peak"),
        )
        + '      <div class="lab-stage" id="mcStage" tabindex="0" role="region" aria-label="Machine count as a staircase against the peak request rate.">'
        '<svg id="mcStair" style="min-width:520px" viewBox="0 0 520 180" role="img" '
        'aria-label="The machine count rising in integer steps as the peak rate grows."></svg></div>\n'
        '      <div class="status-banner" id="mcStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("mcPreset", "Worked example", [(q["key"], q["label"]) for q in MACHINES_PRESETS], p["key"])
        + _range("mcPeak", "peak requests per second", 0, 59, p["peak"])
        + _range("mcCost", "cost of one request, in tenths of a millisecond of one core", 1, 5000, p["cost"])
        + _range("mcCores", "cores per machine", 1, 64, p["cores"])
        + _range("mcRho", "target utilisation, %", 5, 100, p["rho"])
        + _kpi([
            ("mcCap", "Capacity per machine"),
            ("mcUsable", "… at the target"),
            ("mcExact", "Machines needed, exactly"),
            ("mcN", "N"),
            ("mcUtil", "Peak sits at"),
            ("mcFull", "N if sized at 100%"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", MACHINES_PRESETS) + MACHINES_SCRIPT
    return Lab(
        title="From a request's cost to a machine count",
        subtitle="An integer, with a headroom you have to name",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the peak, the cost and the headroom"),
        panel_intro=cfg.get(
            "panel_intro",
            "The machines-needed figure is an exact fraction and N is its ceiling. The "
            "staircase shows why that matters: the peak sits partway up a tread, and the "
            "rest of the tread is the headroom you did not ask for.",
        ),
        script=script,
    )


# =========================================================== mode: workingset

WORKINGSET_PRESETS = [
    {
        "key": "social-timeline",
        "label": "5 TB of timelines, a tenth of it taking 90% of the reads, 80% wanted",
        "data": _ladder(4, 12), "hot": 10, "share": 90, "target": 80, "what": "timeline store",
    },
    {
        "key": "catalog",
        "label": "200 GB catalogue, 5% hot at 75% of reads, 95% wanted",
        "data": _ladder(2, 11), "hot": 5, "share": 75, "target": 95, "what": "catalogue",
    },
    {
        "key": "no-skew",
        "label": "1 TB with no skew at all: half the data, half the reads",
        "data": _ladder(0, 12), "hot": 50, "share": 50, "target": 90, "what": "uniform store",
    },
]

WORKINGSET_SCRIPT = r"""
  var sel = document.getElementById('wsPreset');
  var plot = document.getElementById('wsPlot');
  var status = document.getElementById('wsStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('workingset: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('wsData').value = p.data;
    document.getElementById('wsHot').value = p.hot;
    document.getElementById('wsShare').value = p.share;
    document.getElementById('wsTarget').value = p.target;
  }

  function draw(hot, share, target, frac) {
    function px(f) { return 46 + ratioApprox(f, R(1n, 1n)) * 454; }
    function py(f) { return 150 - ratioApprox(f, R(1n, 1n)) * 136; }
    var s = '<line x1="46" y1="150" x2="500" y2="150" stroke="var(--line-strong)" />'
      + '<line x1="46" y1="10" x2="46" y2="150" stroke="var(--line-strong)" />'
      + '<text x="6" y="18" font-size="10" fill="var(--muted)">100%</text>'
      + '<text x="6" y="153" font-size="10" fill="var(--muted)">0%</text>'
      + '<text x="46" y="166" font-size="10" fill="var(--muted)">cache nothing</text>'
      + '<text x="500" y="166" text-anchor="end" font-size="10" fill="var(--muted)">cache everything</text>';
    /* Two segments and a knee: within the hot region every key is equally
       popular, and so is every key outside it. That is the lesson's model, and
       the knee is exactly where the hot region runs out. */
    s += '<path d="M' + px(R(0n, 1n)).toFixed(1) + ' ' + py(R(0n, 1n)).toFixed(1)
      + ' L' + px(hot).toFixed(1) + ' ' + py(share).toFixed(1)
      + ' L' + px(R(1n, 1n)).toFixed(1) + ' ' + py(R(1n, 1n)).toFixed(1)
      + '" fill="none" stroke="var(--cyan)" stroke-width="2.4" />'
      + '<circle cx="' + px(hot).toFixed(1) + '" cy="' + py(share).toFixed(1) + '" r="4" fill="var(--cyan)" />'
      + '<line x1="46" y1="' + py(target).toFixed(1) + '" x2="500" y2="' + py(target).toFixed(1)
      + '" stroke="var(--green)" stroke-dasharray="5 4" />'
      + '<line x1="' + px(frac).toFixed(1) + '" y1="10" x2="' + px(frac).toFixed(1) + '" y2="150" '
      + 'stroke="var(--amber)" stroke-dasharray="4 3" />'
      + '<circle cx="' + px(frac).toFixed(1) + '" cy="' + py(target).toFixed(1) + '" r="4.5" fill="var(--amber)" />';
    /* The same answer as a bar: the hot bytes, the cold bytes, and the prefix
       that has to sit in memory to reach the target. */
    s += '<rect x="46" y="180" width="454" height="16" rx="3" fill="var(--line-strong)" opacity="0.3" />'
      + '<rect x="46" y="180" width="' + Math.max(1, px(hot) - 46).toFixed(1)
      + '" height="16" rx="3" fill="var(--cyan)" opacity="0.35" />'
      + '<rect x="46" y="184" width="' + Math.max(1, px(frac) - 46).toFixed(1)
      + '" height="8" rx="2" fill="var(--amber)" opacity="0.95" />'
      + '<text x="6" y="192" font-size="10" fill="var(--muted)">data</text>';
    plot.innerHTML = s;
  }

  function redraw() {
    var p = preset();
    var data = ladderValue(+document.getElementById('wsData').value);
    var hotPct = +document.getElementById('wsHot').value;
    var sharePct = +document.getElementById('wsShare').value;
    var targetPct = +document.getElementById('wsTarget').value;
    var hot = R(BigInt(hotPct), 100n), share = R(BigInt(sharePct), 100n), target = R(BigInt(targetPct), 100n);
    document.getElementById('wsDataOut').textContent = fmtBytes(data, 2);
    document.getElementById('wsHotOut').textContent = hotPct + '% of the data is hot';
    document.getElementById('wsShareOut').textContent = sharePct + '% of the reads go to it';
    document.getElementById('wsTargetOut').textContent = targetPct + '% hit rate wanted';

    var frac = workingSetFraction(hot, share, target);
    var bytes = workingSetBytes(data, hot, share, target);
    var hotOnly = hitRateAt(hot, share, hot);
    draw(hot, share, target, frac);

    document.getElementById('wsBytes').textContent = fmtBytes(bytes, 2);
    document.getElementById('wsFrac').textContent = Rtext(frac) + ' of the data';
    document.getElementById('wsPct').textContent = Rtrim(Rround(Rmul(frac, R(100n, 1n)), 2)) + '%';
    document.getElementById('wsHotBytes').textContent = fmtBytes(Rmul(data, hot), 2);
    document.getElementById('wsHotHit').textContent = Rtext(hotOnly);
    document.getElementById('wsAll').textContent = fmtBytes(data, 2);

    var beyondKnee = Rcmp(target, share) > 0;
    status.innerHTML = 'A hit rate of ' + targetPct + '% needs <strong>' + Rtext(frac)
      + '</strong> of the data resident — <strong>' + fmtBytes(bytes, 2) + '</strong> of RAM against '
      + fmtBytes(data, 2) + ' on disk. '
      + (beyondKnee
          ? '<span class="tone-amber">That target is past the knee.</span> The hot ' + hotPct
            + '% buys the first ' + Rtext(hotOnly) + ' of the hits for ' + fmtBytes(Rmul(data, hot), 2)
            + '; every hit after that is bought out of the cold region at the cold region’s price, which is why '
            + 'the points of hit rate after ' + Rtrim(Rround(Rmul(hotOnly, R(100n, 1n)), 1))
            + '% cost more memory than every point before it put together.'
          : 'That target is inside the hot region, so it is bought at the hot region’s price: the memory '
            + 'needed is the target as a fraction of the hot share, times the hot data.')
      + ' <span class="tone-red">Caching is not all-or-nothing</span>: the curve between "cache nothing" and '
      + '"cache everything" is where every real system lives, and the knee at ('
      + Rtext(hot) + ', ' + Rtext(share) + ') is the whole reason a small cache is worth having. '
      + 'The hot fraction here is STATED; “Cache Size and Hit Rate” replaces it with the Zipf curve, which derives '
      + 'the same shape from a popularity exponent instead of asserting it.';
  }

  ['wsData', 'wsHot', 'wsShare', 'wsTarget'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _workingset(cfg):
    """Lesson 9: RAM is sized to the hot fraction, not to the dataset."""
    idx = _preset_index(cfg, WORKINGSET_PRESETS, "workingset")
    p = WORKINGSET_PRESETS[idx]
    markup = (
        _toolbar(
            "The working set",
            "hit rate against the fraction of the data you keep resident",
            _swatch("tone-cyan", "the hit-rate curve")
            + _swatch("tone-green", "the target")
            + _swatch("tone-amber", "what it costs"),
        )
        + '      <div class="lab-stage" id="wsStage" tabindex="0" role="region" aria-label="Hit rate against cached fraction, with the target and its cost.">'
        '<svg id="wsPlot" style="min-width:520px" viewBox="0 0 520 204" role="img" '
        'aria-label="A two-segment hit-rate curve with a knee where the hot region ends."></svg></div>\n'
        '      <div class="status-banner" id="wsStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("wsPreset", "Worked example", [(q["key"], q["label"]) for q in WORKINGSET_PRESETS], p["key"])
        + _range("wsData", "dataset size", 0, 89, p["data"])
        + _range("wsHot", "hot fraction of the data, %", 1, 90, p["hot"])
        + _range("wsShare", "share of the reads it takes, %", 10, 99, p["share"])
        + _range("wsTarget", "hit rate wanted, %", 1, 99, p["target"])
        + _kpi([
            ("wsBytes", "Memory needed"),
            ("wsPct", "Of the dataset"),
            ("wsFrac", "… exactly"),
            ("wsHotBytes", "The hot data alone"),
            ("wsHotHit", "Hit rate if you cache just that"),
            ("wsAll", "Caching everything"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", WORKINGSET_PRESETS) + WORKINGSET_SCRIPT
    return Lab(
        title="Memory and the working set",
        subtitle="Size the cache to the hot fraction, not to the dataset",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the dataset, the skew and the hit rate you want"),
        panel_intro=cfg.get(
            "panel_intro",
            "Within the hot region every key is equally popular, and so is every key outside "
            "it, so the hit rate is piecewise linear with a knee where the hot region ends. "
            "Both the fraction and the bytes are exact.",
        ),
        script=script,
    )


# ========================================================== mode: triangulate

TRIANGULATE_PRESETS = [
    {
        "key": "photo-bytes",
        "label": "bytes uploaded a day: from the people, and from the object store",
        "quantity": "bytes uploaded per day",
        "aTitle": "Route A · from the people",
        "aLead": {"name": "daily uploaders", "ladder": _ladder(4, 5)},
        "aMid": {"name": "photos per person per day", "value": [20, 1]},
        "bTitle": "Route B · from the object store",
        "bLead": {"name": "objects written per day", "ladder": _ladder(0, 7)},
        "bOwn": {"name": "mean object size measured on disk", "value": [1800000, 1]},
        "shared": {"name": "bytes per photo", "ladder": _ladder(2, 6)},
    },
    {
        "key": "requests-a-day",
        "label": "requests a day: from the users, and from the access log",
        "quantity": "requests per day",
        "aTitle": "Route A · from the users",
        "aLead": {"name": "daily active users", "ladder": _ladder(0, 7)},
        "aMid": {"name": "sessions per user per day", "value": [3, 1]},
        "bTitle": "Route B · from the access log",
        "bLead": {"name": "sessions in the log per day", "ladder": _ladder(3, 7)},
        "bOwn": {"name": "requests per session counted in the log", "value": [12, 1]},
        "shared": {"name": "requests per session", "ladder": _ladder(0, 1)},
    },
    {
        "key": "lake-bytes",
        "label": "bytes into the lake: from the fleet, and from the landing zone",
        "quantity": "bytes ingested per day",
        "aTitle": "Route A · from the device fleet",
        "aLead": {"name": "devices reporting", "ladder": _ladder(0, 6)},
        "aMid": {"name": "events per device per day", "value": [2000, 1]},
        "bTitle": "Route B · from the landing zone",
        "bLead": {"name": "events landing per day", "ladder": _ladder(2, 9)},
        "bOwn": {"name": "bytes per event on a sampled file", "value": [180, 1]},
        "shared": {"name": "bytes per event", "ladder": _ladder(2, 2)},
    },
]

TRIANGULATE_SCRIPT = r"""
  var sel = document.getElementById('tgPreset');
  var shareSel = document.getElementById('tgShare');
  var tableA = document.getElementById('tgTableA'), tableB = document.getElementById('tgTableB');
  /* The DRAWING. The slider below is 'tgBand'; this must not share its id:
     a browser's getElementById returns the FIRST match in document order,
     which is this svg, so a shared id made the slider read undefined and the
     band compute NaN. labcheck cannot catch it -- its shim stores ids in a
     Map, so the LAST registration wins and the slider resolved correctly
     there. The duplicate-id check in ci.yml is what catches it. */
  var bandEl = document.getElementById('tgBandPlot');
  var status = document.getElementById('tgStatus');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('triangulate: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('tgA').value = p.aLead.ladder;
    document.getElementById('tgB').value = p.bLead.ladder;
    document.getElementById('tgS').value = p.shared.ladder;
  }
  function fixed(pair) { return R(BigInt(pair[0]), BigInt(pair[1])); }

  function chains() {
    var p = preset(), shared = shareSel.value === 'shared';
    var lead = ladderValue(+document.getElementById('tgA').value);
    var bLead = ladderValue(+document.getElementById('tgB').value);
    var assumption = ladderValue(+document.getElementById('tgS').value);
    var a = {
      title: p.aTitle,
      names: [p.aLead.name, p.aMid.name, p.shared.name],
      values: [lead, fixed(p.aMid.value), assumption]
    };
    var b = shared
      ? { title: p.bTitle, names: [p.bLead.name, p.shared.name], values: [bLead, assumption] }
      : { title: p.bTitle, names: [p.bLead.name, p.bOwn.name], values: [bLead, fixed(p.bOwn.value)] };
    return { p: p, a: a, b: b, shared: shared };
  }

  function renderChain(el, chain, total, shareNames) {
    var h = '<thead><tr><th colspan="2">' + chain.title + '</th></tr></thead><tbody>';
    for (var i = 0; i < chain.names.length; i += 1) {
      var isShared = shareNames.indexOf(chain.names[i]) >= 0;
      h += '<tr><td class="' + (isShared ? 'tone-red' : 'tone-muted') + '">' + chain.names[i]
        + (isShared ? ' &#183; shared' : '') + '</td><td>' + showR(chain.values[i], 2) + '</td></tr>';
    }
    h += '<tr><td><strong>product</strong></td><td><strong>' + showR(total, 2) + '</strong></td></tr>';
    el.innerHTML = h + '</tbody>';
  }

  function drawBand(ratio, k) {
    /* The ratio on a logarithmic ruler with the accepted band drawn around 1,
       because "agree" is a claim about a range and the range is the one the
       first lesson computed. */
    var lr = ratio === null ? 0 : log10Approx(ratio), lk = log10Approx(k);
    var reach = Math.max(lk, Math.abs(lr)) * 1.35 + 0.05;
    function x(l) { return 260 + (l / reach) * 238; }
    var s = '<line x1="22" y1="52" x2="498" y2="52" stroke="var(--line-strong)" />'
      + '<rect x="' + x(-lk).toFixed(1) + '" y="30" width="' + (x(lk) - x(-lk)).toFixed(1)
      + '" height="26" rx="4" fill="var(--green)" opacity="0.22" />'
      + '<line x1="260" y1="24" x2="260" y2="62" stroke="var(--green)" stroke-width="2" />'
      + '<text x="260" y="18" text-anchor="middle" font-size="10" fill="var(--green)">1</text>'
      + '<text x="' + x(-lk).toFixed(1) + '" y="74" text-anchor="middle" font-size="10" fill="var(--muted)">÷'
      + Rtext(k) + '</text>'
      + '<text x="' + x(lk).toFixed(1) + '" y="74" text-anchor="middle" font-size="10" fill="var(--muted)">×'
      + Rtext(k) + '</text>';
    if (ratio !== null) {
      var inside = withinBand(ratio, k);
      var px = Math.max(22, Math.min(498, x(lr)));
      s += '<circle cx="' + px.toFixed(1) + '" cy="52" r="6" fill="' + (inside ? 'var(--cyan)' : 'var(--red)') + '" />'
        + '<text x="' + px.toFixed(1) + '" y="18" text-anchor="middle" font-size="11" fill="'
        + (inside ? 'var(--cyan)' : 'var(--red)') + '">A ÷ B = ' + Rtext(ratio) + '</text>';
    }
    bandEl.innerHTML = s;
  }

  function redraw() {
    var st = chains();
    var k = R(BigInt(+document.getElementById('tgBand').value), 1n);
    var totalA = routeProduct(st.a.values), totalB = routeProduct(st.b.values);
    var ratio = routeRatio(totalA, totalB);
    var shareNames = sharedFactors(st.a.names, st.a.values, st.b.names, st.b.values);

    document.getElementById('tgALab').textContent = st.p.aLead.name;
    document.getElementById('tgBLab').textContent = st.p.bLead.name;
    document.getElementById('tgSLab').textContent = st.p.shared.name + ' — the assumption under test';
    document.getElementById('tgBandLab').textContent = 'agreement band from lesson 1: ÷k … ×k';
    document.getElementById('tgAOut').textContent = showR(ladderValue(+document.getElementById('tgA').value), 2);
    document.getElementById('tgBOut').textContent = showR(ladderValue(+document.getElementById('tgB').value), 2);
    document.getElementById('tgSOut').textContent = showR(ladderValue(+document.getElementById('tgS').value), 2);
    document.getElementById('tgBandOut').textContent = '÷' + Rtext(k) + ' … ×' + Rtext(k);

    renderChain(tableA, st.a, totalA, shareNames);
    renderChain(tableB, st.b, totalB, shareNames);
    drawBand(ratio, k);

    var inside = withinBand(ratio, k);
    document.getElementById('tgTotalA').textContent = showR(totalA, 2);
    document.getElementById('tgTotalB').textContent = showR(totalB, 2);
    document.getElementById('tgRatio').textContent = ratio === null ? '—' : Rtext(ratio);
    document.getElementById('tgRatioDec').textContent = ratio === null ? '—' : showR(ratio, 4);
    document.getElementById('tgVerdict').textContent = shareNames.length
      ? 'no check made' : (inside ? 'they agree' : 'they do not agree');
    document.getElementById('tgShared').textContent = shareNames.length
      ? shareNames.join(', ') : 'none — the routes are independent';

    status.innerHTML = 'Route A says <strong>' + showR(totalA, 2) + '</strong> ' + st.p.quantity
      + ', route B says <strong>' + showR(totalB, 2) + '</strong>, and the ratio is <strong>'
      + (ratio === null ? '—' : Rtext(ratio)) + '</strong> — exact, a quotient of two products of '
      + 'exact fractions. The factors in “Orders of Magnitude” gave an interval ÷' + Rtext(k) + ' … ×'
      + Rtext(k) + ' wide, and the ratio '
      + (inside ? '<span class="tone-green">lies inside it</span>' : '<span class="tone-red">lies outside it</span>')
      + '. ' + (shareNames.length
          ? '<span class="tone-red">But the two routes share ' + shareNames.join(' and ')
            + ', so this is not a check.</span> Drag that slider: both answers move together and the ratio does not '
            + 'move at all. A factor common to both chains cancels out of the quotient, which means it cannot be '
            + 'contradicted — an agreement that no possible value of it could break has tested nothing.'
          : 'The routes share no factor, so the agreement is evidence: drag the assumption and route A moves while '
            + 'route B stays where the measurement put it. '
            + (inside
                ? 'Within the width the inputs deserve, the two routes are telling the same story.'
                : 'They disagree by more than the inputs allow, which means an assumption is wrong — that is '
                  + 'the useful outcome, not the failure.'));
  }

  ['tgA', 'tgB', 'tgS', 'tgBand'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  shareSel.addEventListener('change', redraw);
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _triangulate(cfg):
    """Lesson 10: a second route, and what makes it a check rather than a ritual."""
    idx = _preset_index(cfg, TRIANGULATE_PRESETS, "triangulate")
    p = TRIANGULATE_PRESETS[idx]
    markup = (
        _toolbar(
            "Two routes to one number",
            "and whether their agreement means anything",
            _swatch("tone-cyan", "inside the band")
            + _swatch("tone-red", "a factor both routes share")
            + _swatch("tone-green", "the band “Orders of Magnitude” gave"),
        )
        + '      <div class="lab-stage" id="tgStage" tabindex="0" role="region" aria-label="Two factor chains and the ratio between their answers.">\n'
        '        <div class="grid-2">\n'
        '          <div class="table-wrap"><table class="tt" id="tgTableA"></table></div>\n'
        '          <div class="table-wrap"><table class="tt" id="tgTableB"></table></div>\n'
        "        </div>\n"
        '        <svg id="tgBandPlot" style="min-width:520px" viewBox="0 0 520 84" role="img" '
        'aria-label="The ratio between the two routes against the agreement band."></svg>\n'
        "      </div>\n"
        '      <div class="status-banner" id="tgStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("tgPreset", "Worked example", [(q["key"], q["label"]) for q in TRIANGULATE_PRESETS], p["key"])
        + _select(
            "tgShare",
            "Where route B gets the contested figure",
            [
                ("own", "route B measured it for itself"),
                ("shared", "route B took route A’s assumption"),
            ],
            "own",
        )
        + _range("tgA", p["aLead"]["name"], 0, 59, p["aLead"]["ladder"])
        + _range("tgB", p["bLead"]["name"], 0, 59, p["bLead"]["ladder"])
        + _range("tgS", p["shared"]["name"], 0, 59, p["shared"]["ladder"])
        + _range("tgBand", "agreement band, ÷k … ×k", 1, 12, 8)
        + _kpi([
            ("tgTotalA", "Route A"),
            ("tgTotalB", "Route B"),
            ("tgRatio", "A ÷ B, exact"),
            ("tgRatioDec", "A ÷ B"),
            ("tgVerdict", "Verdict"),
            ("tgShared", "Shared factors"),
        ])
    )
    script = _CORE_JS + cfg_literal("PRESETS", TRIANGULATE_PRESETS) + TRIANGULATE_SCRIPT
    return Lab(
        title="Triangulating an estimate",
        subtitle="Two routes, one ratio, and the factor that would make it meaningless",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Build the second route, then decide whether it is one"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both products and the ratio between them are exact. The second selector is the "
            "point of the lesson: take route A's assumption into route B and the ratio stops "
            "responding to it, which is what a fake check looks like from the inside.",
        ),
        script=script,
    )


# ---------------------------------------------------------------- the kit

_BUILDERS = {
    "magnitude": _magnitude,
    "rate": _rate,
    "accumulate": _accumulate,
    "scale": _scale,
    "peak": _peak,
    "machines": _machines,
    "workingset": _workingset,
    "triangulate": _triangulate,
}

MODES = tuple(_BUILDERS)


def estimate_lab(cfg):
    """The capacity-estimation kit: eight modes, ten lessons.

    An unknown mode RAISES. The alternative -- falling back to a default -- is
    how a lesson on the working set ends up showing the reader a log ruler, with
    a page that builds, renders, redraws and passes every markup assertion in
    the suite while teaching the wrong thing.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "estimate: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["ESTIMATE_JS", "MODES", "estimate_lab"]
