"""Course 2: Latency and the Tail -- one kit, eleven modes, one arithmetic.

A request is slow for one of four reasons: it went far, it went back and forth,
it waited for the slowest of many, or it was the unlucky one in a hundred. Each
mode of this kit is one of those reasons made into a number the reader can move.

Three decisions run through all eleven.

  MILLISECONDS, ALWAYS. Every time on this page is a rational number of
  milliseconds and every size is a count of bytes. The course's own `how_to`
  says that mixing microseconds into a budget is the arithmetic error it
  reliably produces, so there is one unit and the conversions happen once, in
  `transferMs` and `lightFloorMs`, where `mathcheck.js` can call them.

  PERCENTILES ARE RANKS. `percentile` in sysdesign_core.py is nearest rank, so
  every percentile printed here is a value some request actually took, and the
  rank that selected it is printed beside it. That is what makes the `percentile`
  and `convolve` modes able to contradict each other's naive arithmetic on the
  reader's own numbers: p99(A + B) is computed from the convolution of the two
  stage distributions, and the sum of the two stage p99s is computed beside it,
  and on the lesson's preset they are 78 ms and 110 ms. Nothing decides which is
  bigger except the arithmetic.

  ONE ROUNDED FIGURE, NAMED. `mathis` is the only mode that rounds: the bound is
  (MSS/RTT)(1/sqrt p) and `Rsqrt` returns null for a non-square, so it calls
  `sqrtApprox` from the core and the page says on its face that it did. Every
  other figure in the kit is an exact fraction, printed by `Rfixed` -- long
  division in BigInt, because 0.999^693 has a numerator of two thousand digits
  and `Number()` of that is Infinity.

The modes, and the lesson each belongs to:

  bdp         L1  bandwidth x RTT, the time, and which term dominates
  lightspeed  L2  2d/(2c/3), and how much of a measured RTT it does not explain
  roundtrips  L3  k*RTT + bytes/bandwidth, and the payload where they cross
  dag         L4  the longest path through a stage DAG, and every stage's slack
  percentile  L5  p50, p95, p99 by rank, against a mean that is none of them
  fanout      L6  1 - p^n, and the n at which a per-call p99 becomes the median
  hedge       L7  the tail a backup request buys, and what it costs in load
  convolve    L8  the sum's pmf by convolution, against the sum of the p99s
  budget      L9  what the SLO leaves the code after the floors are taken out
  timeout     L10 (r+1)T against the budget, and the good calls T kills
  mathis      L11 the loss-limited throughput of one flow, and the stream count
"""

import json

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal
from .sysdesign_core import APPROX_JS, PERCENTILE_JS, PMF_JS, RCEIL_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds, as top-level functions so scripts/mathcheck.js
# can call every one of them without a DOM. Nothing here touches the document;
# everything that does lives in the per-mode scripts below.
# ---------------------------------------------------------------------------

LATENCY_JS = r"""
  /* ---------------------------------------------------------------- output

     Rdec goes through Number, and this course produces rationals Number
     cannot hold: 0.999^693 has a 2078-digit numerator, Number() of it is
     Infinity, and Infinity/Infinity is NaN. So decimals here are long
     division in BigInt, rounded half up at the last digit printed. */
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
  /* A percentage of an exact probability, still exact until the last digit. */
  function Rpct(a, places) { return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%'; }
  /* Digit grouping, for byte counts that run to seven figures. */
  function commas(value) {
    var s = String(value), out = '', i, c = 0;
    for (i = s.length - 1; i >= 0; i -= 1) {
      out = s.charAt(i) + out;
      c += 1;
      if (c % 3 === 0 && i > 0 && s.charAt(i - 1) !== '-') out = ' ' + out;
    }
    return out;
  }
  /* Decimal byte units, which is what a link rate is quoted in: 1 kB = 1000 B.
     Stated rather than assumed, because the KiB/kB slip is a 2.4% error at MB
     and this course compares transfer time against a round trip. */
  function bytesText(bytes) {
    var b = Number(bytes);
    if (b >= 1000000) return Rfixed(R(BigInt(bytes), 1000000n), 3) + ' MB';
    if (b >= 1000) return Rfixed(R(BigInt(bytes), 1000n), 2) + ' kB';
    return commas(bytes) + ' B';
  }

  /* ------------------------------------------------- L1, L3: bytes and time

     One round trip is RTT milliseconds whatever the link is. The bytes cost
     size/bandwidth. Both terms below are exact: a bandwidth in Mbit/s is
     mbps*10^6 bits a second, and a millisecond is a thousandth, so the
     conversion is a fraction with no decimal in it anywhere. */
  function transferMs(bytes, mbps) {
    /* bytes*8 bits / (mbps*10^6 bit/s), in ms  =  bytes*8 / (mbps*1000) */
    return R(BigInt(bytes) * 8n, BigInt(mbps) * 1000n);
  }
  function bdpBytes(mbps, rttMs) {
    /* bandwidth * RTT in bytes: mbps*10^6 * rtt/1000 / 8 = 125*mbps*rtt */
    return R(125n * BigInt(mbps) * BigInt(rttMs), 1n);
  }
  function linkTimeMs(k, rttMs, bytes, mbps) {
    return Radd(R(BigInt(k) * BigInt(rttMs), 1n), transferMs(bytes, mbps));
  }
  /* The payload at which the bytes cost as much as the k round trips. At k = 1
     this IS the bandwidth-delay product, which is why L1 and L3 are one fact. */
  function crossoverBytes(k, rttMs, mbps) {
    return R(125n * BigInt(k) * BigInt(rttMs) * BigInt(mbps), 1n);
  }

  /* ------------------------------------------------------- L2: the floor

     Light in fibre goes at about two thirds of c, so the round trip over a
     great-circle distance d is 2d/(2c/3) = 3d/c seconds, and no engineering
     removes it. c is exact by definition -- the metre is defined from it --
     so the floor is an exact fraction of a millisecond. */
  function lightFloorMs(km) {
    return R(3n * BigInt(km) * 1000000n, 299792458n);
  }
  /* What a measured round trip does NOT explain: the part that is queueing,
     serialisation, middleboxes and software, i.e. everything you can fix. */
  function unexplainedMs(measuredMs, km) {
    return Rsub(R(BigInt(measuredMs), 1n), lightFloorMs(km));
  }

  /* -------------------------------------------- L4: the longest path in a DAG

     Stages in series add; stages in parallel take the maximum; so the
     end-to-end time is the longest path through the stage graph, and a stage
     off that path can be sped up to zero without moving the answer.

     `times` is indexed by stage and `edges` are [from, to] pairs that must run
     forward in that index order -- the kit only ever builds forward edges, and
     an order that is already topological is what makes one pass correct.
     Earliest start ES, latest start LS, and slack = LS - ES, which is exactly
     the project-network vocabulary: a stage with slack 0 is critical. */
  function dagSchedule(times, edges) {
    var n = times.length, i, e, ES = [], LF = [], slack = [], EF = [], LS = [];
    for (i = 0; i < n; i += 1) ES.push(0);
    for (i = 0; i < n; i += 1) {
      for (e = 0; e < edges.length; e += 1) {
        if (edges[e][1] !== i) continue;
        var u = edges[e][0];
        if (u >= i) continue;                     /* not forward: not an edge here */
        var cand = ES[u] + times[u];
        if (cand > ES[i]) ES[i] = cand;
      }
    }
    var length = 0;
    for (i = 0; i < n; i += 1) { EF.push(ES[i] + times[i]); if (EF[i] > length) length = EF[i]; }
    for (i = 0; i < n; i += 1) LF.push(length);
    for (i = n - 1; i >= 0; i -= 1) {
      for (e = 0; e < edges.length; e += 1) {
        if (edges[e][0] !== i) continue;
        var w = edges[e][1];
        if (w <= i) continue;
        var bound = LF[w] - times[w];
        if (bound < LF[i]) LF[i] = bound;
      }
    }
    for (i = 0; i < n; i += 1) { LS.push(LF[i] - times[i]); slack.push(LS[i] - ES[i]); }
    return { ES: ES, EF: EF, LS: LS, LF: LF, slack: slack, length: length,
             path: dagCriticalPath(times, edges, ES, slack) };
  }
  /* One critical path, as a list of stage indices. There can be more than one;
     this returns the first in index order, and the slack column is what tells
     the reader whether another stage ties. */
  function dagCriticalPath(times, edges, ES, slack) {
    var n = times.length, i, e, start = -1, path = [];
    for (i = 0; i < n; i += 1) if (slack[i] === 0 && ES[i] === 0) { start = i; break; }
    if (start < 0) return path;
    var cur = start;
    path.push(cur);
    for (;;) {
      var next = -1;
      for (e = 0; e < edges.length; e += 1) {
        var u = edges[e][0], w = edges[e][1];
        if (u !== cur || w <= u) continue;
        if (slack[w] === 0 && ES[w] === ES[cur] + times[cur]) { next = w; break; }
      }
      if (next < 0) return path;
      path.push(next);
      cur = next;
    }
  }

  /* --------------------------------------------- L5, L10: samples by rank

     A sample is a sorted list of integer milliseconds. `percentile` in the core
     selects by nearest rank; these two only get the list into shape and say
     what the mean is, which is the number the lesson is arguing with. */
  function parseSample(text) {
    var raw = String(text).split(/[^0-9]+/), out = [], i;
    for (i = 0; i < raw.length; i += 1) {
      if (!raw[i]) continue;
      out.push(Number(raw[i]));
    }
    if (!out.length) return null;
    return out.sort(function (a, b) { return a - b; });
  }
  function sampleMean(sorted) {
    var s = 0n;
    for (var i = 0; i < sorted.length; i += 1) s += BigInt(sorted[i]);
    return R(s, BigInt(sorted.length));
  }
  /* How many of the sample are strictly below a rational -- the count that
     answers "how many users are faster than the average user?". */
  function countBelow(sorted, x) {
    var c = 0;
    for (var i = 0; i < sorted.length; i += 1) if (Rcmp(R(BigInt(sorted[i]), 1n), x) < 0) c += 1;
    return c;
  }

  /* ------------------------------------------ L7, L8, L10: distributions

     A stage's latency is a pmf given as value:weight pairs the reader types.
     The weights are integers and the probabilities are their exact fractions,
     which is what lets a 49-atom convolution still print as a fraction. */
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
  /* The sample a run-length spec stands for, so the rank definition of a
     percentile can be applied to the same distribution the pmf functions use. */
  function expandSpec(spec) {
    var sorted = spec.slice().sort(function (a, b) { return a[0] - b[0]; }), out = [], i, j;
    for (i = 0; i < sorted.length; i += 1) for (j = 0; j < sorted[i][1]; j += 1) out.push(sorted[i][0]);
    return out;
  }
  /* P(X <= t) for a pmf, and the percentile by the same rule the core uses on
     a sample: the smallest value whose cumulative probability reaches q. */
  function pmfCdfAt(pairs, t) {
    var s = R(0n, 1n);
    for (var i = 0; i < pairs.length; i += 1) if (pairs[i][0] <= t) s = Radd(s, pairs[i][1]);
    return s;
  }
  function pmfPercentile(pairs, q) {
    var sorted = pairs.slice().sort(function (a, b) { return a[0] - b[0]; });
    var cum = R(0n, 1n);
    for (var i = 0; i < sorted.length; i += 1) {
      cum = Radd(cum, sorted[i][1]);
      if (Rcmp(cum, q) >= 0) return sorted[i][0];
    }
    return sorted.length ? sorted[sorted.length - 1][0] : null;
  }

  /* ------------------------------------------------- L6: fan-out amplification

     P(all n independent calls land inside their own p-th percentile) = p^n.
     The break-even n is where that falls to a half -- the point at which a
     per-call p99 has become the whole request's median.

     By binary search rather than a scan: p^n decreases in n, so the search is
     exact, and at p = 999/1000 the answer is 693, where a scan would multiply
     out a two-thousand-digit fraction 693 times. */
  function fanoutBreakEven(p, limit) {
    var half = R(1n, 2n);
    if (Rcmp(p, R(1n, 1n)) >= 0) return 0;
    if (Rcmp(p, half) <= 0) return 1;
    var lo = 1, hi = 2;
    while (hi <= limit && Rcmp(Rpow(p, hi), half) > 0) { lo = hi; hi *= 2; }
    if (hi > limit) return 0;
    while (lo + 1 < hi) {
      var mid = (lo + hi) >> 1;
      if (Rcmp(Rpow(p, mid), half) > 0) lo = mid; else hi = mid;
    }
    return hi;
  }

  /* ------------------------------------------------------- L7: hedging

     Send a backup copy after d milliseconds. The request finishes at
     min(X, d + Y) with Y an independent copy, so under independence
     P(hedged > t) = P(X > t) * P(X > t - d) -- and at t just past d that is
     the tail squared, which is the whole argument for the technique.

     The times where that function can change are the sample's own values and
     those values shifted by d, so the hedged percentile is a search over that
     grid rather than over a continuum. */
  function hedgedTail(pairs, d, t) {
    return Rmul(pmfTail(pairs, t), pmfTail(pairs, t - d));
  }
  function hedgeGrid(pairs, d) {
    var seen = {}, out = [], i, k;
    for (i = 0; i < pairs.length; i += 1) { seen[pairs[i][0]] = true; seen[pairs[i][0] + d] = true; }
    for (k in seen) if (Object.prototype.hasOwnProperty.call(seen, k)) out.push(Number(k));
    return out.sort(function (a, b) { return a - b; });
  }
  function hedgedQuantile(pairs, d, q) {
    var want = Rsub(R(1n, 1n), q), grid = hedgeGrid(pairs, d), i;
    for (i = 0; i < grid.length; i += 1) {
      if (Rcmp(hedgedTail(pairs, d, grid[i]), want) <= 0) return grid[i];
    }
    return null;
  }
  /* The extra load a hedge at d costs: the fraction of requests that live long
     enough to trigger the backup copy. Hedging at the p50 doubles the load. */
  function hedgeLoad(pairs, d) { return pmfTail(pairs, d); }

  /* ------------------------------------------------------- L9: the budget

     Allocate backwards. The SLO minus the floors that no code can remove is
     what the code may spend; split evenly, a stage whose own floor is above
     its even share cannot fit, and the surplus the others release is what is
     available to cover it.

     `residual` is computed two ways -- as available minus the floors, and as
     the surplus minus the shortfall -- and the page prints both, because an
     allocation that does not balance is an allocation with a bug in it. */
  function budgetPlan(sloMs, fixedMs, floors) {
    var n = floors.length, i, zero = R(0n, 1n);
    var avail = Rsub(R(BigInt(sloMs), 1n), R(BigInt(fixedMs), 1n));
    var share = n ? Rdiv(avail, R(BigInt(n), 1n)) : zero;
    var rows = [], floorTotal = zero, spare = zero, need = zero;
    for (i = 0; i < n; i += 1) {
      var f = R(BigInt(floors[i]), 1n), residual = Rsub(share, f);
      floorTotal = Radd(floorTotal, f);
      if (Rcmp(residual, zero) < 0) need = Rsub(need, residual); else spare = Radd(spare, residual);
      rows.push({ floor: f, share: share, residual: residual, fits: Rcmp(residual, zero) >= 0 });
    }
    return { avail: avail, share: share, rows: rows, floorTotal: floorTotal,
             residual: Rsub(avail, floorTotal), spare: spare, need: need,
             balanced: Requ(Rsub(avail, floorTotal), Rsub(spare, need)) };
  }

  /* --------------------------------------------------- L10: timeouts and retries

     The worst case is (r + 1) timeouts back to back and it must fit the budget;
     the timeout itself kills every call that would have finished after it. */
  function worstCaseMs(timeoutMs, retries) {
    return R(BigInt(timeoutMs) * BigInt(retries + 1), 1n);
  }
  function killFraction(sorted, timeoutMs) {
    return Rsub(R(1n, 1n), empiricalCdf(sorted, timeoutMs));
  }
  function allAttemptsLost(p, retries) { return Rpow(p, retries + 1); }

  /* ------------------------------------------- L11: the loss-limited bound

     Mathis: one TCP flow is bounded by (MSS/RTT)(1/sqrt p), and the square root
     is why this is the one figure on this course that rounds. sqrtApprox is the
     core's Newton iteration; the bound below is a Number, not a rational, and
     every caller says so on the page. */
  function mathisBytesPerSecApprox(mssBytes, rttMs, loss) {
    var root = sqrtApprox(loss, 1e-15);
    if (!(root > 0)) return NaN;
    return (mssBytes * 1000 / rttMs) / root;
  }
  function mathisMbitsApprox(mssBytes, rttMs, loss) {
    return mathisBytesPerSecApprox(mssBytes, rttMs, loss) * 8 / 1000000;
  }
  function streamsToFillApprox(linkMbits, flowMbits) {
    if (!(flowMbits > 0)) return 0;
    return Math.ceil(linkMbits / flowMbits);
  }
"""

_CORE_JS = RATIONAL_JS + RCEIL_JS + PERCENTILE_JS + PMF_JS + APPROX_JS + LATENCY_JS


# ---------------------------------------------------------------------------
# Control furniture. Every lab on the path uses the same three shapes, so a
# reader moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _js_string(text):
    """A JS string literal for a preset the reader can then edit.

    json.dumps output is valid JS and the escape makes "</script>" structurally
    impossible, the same argument common.cfg_literal makes for its payloads.
    """
    return json.dumps(text).replace("</", "<\\/")


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
    return (
        '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)
    )


def _table(cid):
    return '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%s"></table></div>\n' % cid


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


# ---------------------------------------------------------------------------
# L1 - bdp
# ---------------------------------------------------------------------------


def _bdp(cfg):
    mbps = int(cfg.get("bandwidth", 100))
    rtt = int(cfg.get("rtt", 80))
    size = int(cfg.get("size_kb", 64))

    markup = (
        _toolbar(
            "Bandwidth-delay product",
            "one round trip against the bytes, at the size you choose",
            [("amber", "round trip"), ("cyan", "bytes on the wire"), ("purple", "crossover")],
        )
        + _stage(_svg("bdPlot", "0 0 520 150", "The round-trip term and the transfer term drawn as two bars."))
        + _table("bdTable")
        + _banner("bdStatus")
    )
    controls = (
        _range("bdBw", "Bandwidth (Mbit/s)", 1, 1000, mbps)
        + _range("bdRtt", "Round-trip time (ms)", 1, 400, rtt)
        + _range("bdSize", "Transfer size (kB, 1 kB = 1000 B)", 1, 4000, size)
        + _kpis(
            [
                ("Bandwidth-delay product", "bdBdp"),
                ("Time = RTT + size/bandwidth", "bdTime"),
                ("Share spent waiting", "bdShare"),
                ("Crossover size", "bdCross"),
            ]
        )
        + _hint(
            "bdHint",
            "The bandwidth-delay product is how many bytes fit on the wire at once. A transfer "
            "smaller than it finishes before the pipe is even full, so buying more bandwidth "
            "changes nothing and shortening the round trip changes everything.",
        )
    )

    script = _CORE_JS + r"""
  var bwS = document.getElementById('bdBw'), rttS = document.getElementById('bdRtt'), szS = document.getElementById('bdSize');
  var plot = document.getElementById('bdPlot'), table = document.getElementById('bdTable');
  var status = document.getElementById('bdStatus');

  function redraw() {
    var mbps = +bwS.value, rtt = +rttS.value, kb = +szS.value, bytes = kb * 1000;
    document.getElementById('bdBwOut').textContent = mbps + ' Mbit/s';
    document.getElementById('bdRttOut').textContent = rtt + ' ms';
    document.getElementById('bdSizeOut').textContent = bytesText(bytes);

    var bdp = bdpBytes(mbps, rtt);
    var wait = R(BigInt(rtt), 1n);
    var send = transferMs(bytes, mbps);
    var total = Radd(wait, send);
    var share = Rdiv(wait, total);
    var cross = crossoverBytes(1, rtt, mbps);

    document.getElementById('bdBdp').textContent = bytesText(bdp.n / bdp.d);
    document.getElementById('bdTime').textContent = Rfixed(total, 3) + ' ms';
    document.getElementById('bdShare').textContent = Rpct(share, 1);
    document.getElementById('bdCross').textContent = bytesText(cross.n / cross.d);

    table.innerHTML = '<thead><tr><th>term</th><th>what it is</th><th>exact value</th><th>ms</th></tr></thead><tbody>'
      + '<tr><td class="tone-amber">RTT</td><td>one round trip, whatever the link</td><td>'
      + rtt + '</td><td>' + Rfixed(wait, 3) + '</td></tr>'
      + '<tr><td class="tone-cyan">size / bandwidth</td><td>' + commas(bytes) + ' B &times; 8 &divide; ('
      + mbps + ' &times; 10<sup>6</sup>)</td><td>' + Rtext(send) + '</td><td>' + Rfixed(send, 3) + '</td></tr>'
      + '<tr><td>total</td><td>RTT + size/bandwidth</td><td>' + Rtext(total) + '</td><td>'
      + Rfixed(total, 3) + '</td></tr></tbody>';

    var span = Rcmp(wait, send) >= 0 ? wait : send;
    var unit = Rcmp(span, R(0n, 1n)) === 0 ? 1 : 430 / parseFloat(Rfixed(span, 6));
    var wpx = Math.max(2, parseFloat(Rfixed(wait, 6)) * unit);
    var spx = Math.max(2, parseFloat(Rfixed(send, 6)) * unit);
    var s = '<text x="0" y="16" font-size="11" fill="var(--muted)">one round trip</text>'
      + '<rect x="0" y="24" width="' + wpx + '" height="26" rx="3" fill="var(--amber)" opacity="0.85" />'
      + '<text x="' + (wpx + 8) + '" y="42" font-size="11" fill="var(--amber)" font-weight="700">'
      + Rfixed(wait, 2) + ' ms</text>'
      + '<text x="0" y="82" font-size="11" fill="var(--muted)">the bytes</text>'
      + '<rect x="0" y="90" width="' + spx + '" height="26" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (spx + 8) + '" y="108" font-size="11" fill="var(--cyan)" font-weight="700">'
      + Rfixed(send, 2) + ' ms</text>'
      + '<line x1="0" y1="132" x2="520" y2="132" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="146" font-size="10" fill="var(--purple)">the two bars are equal at '
      + bytesText(cross.n / cross.d) + ', which is the bandwidth-delay product</text>';
    plot.innerHTML = s;

    var latencyBound = Rcmp(send, wait) < 0;
    status.innerHTML = 'At ' + mbps + ' Mbit/s and ' + rtt + ' ms, the wire holds <strong>'
      + bytesText(bdp.n / bdp.d) + '</strong> at once. This ' + bytesText(bytes) + ' transfer takes <strong>'
      + Rfixed(total, 3) + ' ms</strong>, of which ' + Rpct(share, 1) + ' is the round trip'
      + (latencyBound
          ? ' &mdash; it is <span class="tone-amber">latency-bound</span>. Doubling the bandwidth to '
            + (2 * mbps) + ' Mbit/s would save ' + Rfixed(Rsub(send, transferMs(bytes, 2 * mbps)), 3)
            + ' ms; halving the round trip would save ' + Rfixed(Rdiv(wait, R(2n, 1n)), 3) + ' ms.'
          : ' &mdash; it is <span class="tone-cyan">bandwidth-bound</span>, because '
            + bytesText(bytes) + ' is past the ' + bytesText(cross.n / cross.d)
            + ' crossover. Here more bandwidth is the thing that helps.');
  }

  [bwS, rttS, szS].forEach(function (el) { el.addEventListener('input', redraw); });
  bwS.value = """ + str(mbps) + r"""; rttS.value = """ + str(rtt) + r"""; szS.value = """ + str(size) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Latency and throughput are two numbers",
        subtitle="The bandwidth-delay product, and which term your transfer is paying",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the link and the transfer"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both terms are computed exactly from the sizes you set: one round trip, "
            "and the bytes divided by the bandwidth.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - lightspeed
# ---------------------------------------------------------------------------

_ROUTES = [
    ("5585", "New York &rarr; London (5585 km)"),
    ("4139", "New York &rarr; San Francisco (4139 km)"),
    ("8280", "San Francisco &rarr; Tokyo (8280 km)"),
    ("7200", "Mumbai &rarr; London (7200 km)"),
    ("10263", "Frankfurt &rarr; Singapore (10263 km)"),
    ("16993", "London &rarr; Sydney (16993 km)"),
]


def _lightspeed(cfg):
    km = int(cfg.get("km", 5585))
    measured = int(cfg.get("measured", 76))

    markup = (
        _toolbar(
            "The speed-of-light floor",
            "2d &divide; (&#8532;c), and the part of a measured round trip it does not explain",
            [("green", "the floor"), ("red", "everything else"), ("muted", "c is exact")],
        )
        + _stage(_svg("lsPlot", "0 0 520 130", "A measured round trip split into the light-speed floor and the remainder."))
        + _table("lsTable")
        + _banner("lsStatus")
    )
    controls = (
        _select("lsRoute", "Route", _ROUTES + [("custom", "&mdash; or set the distance below &mdash;")], str(km))
        + _range("lsKm", "Great-circle distance (km)", 100, 20000, km, 1)
        + _range("lsRtt", "Measured round-trip time (ms)", 1, 500, measured)
        + _kpis(
            [
                ("Floor: 2d &divide; (&#8532;c)", "lsFloor"),
                ("Measured", "lsMeasured"),
                ("Measured &divide; floor", "lsRatio"),
                ("Unexplained remainder", "lsRest"),
            ]
        )
        + _hint(
            "lsHint",
            "Light in fibre travels at about two thirds of c, so the round trip is 3d/c seconds. "
            "c is exact by definition, so the floor is an exact fraction. A CDN shortens d. "
            "Nothing shortens 3/c.",
        )
    )

    script = _CORE_JS + r"""
  var routeSel = document.getElementById('lsRoute'), kmS = document.getElementById('lsKm'), rttS = document.getElementById('lsRtt');
  var plot = document.getElementById('lsPlot'), table = document.getElementById('lsTable');
  var status = document.getElementById('lsStatus');

  function redraw() {
    var km = +kmS.value, measured = +rttS.value;
    document.getElementById('lsKmOut').textContent = commas(km) + ' km';
    document.getElementById('lsRttOut').textContent = measured + ' ms';

    var floor = lightFloorMs(km);
    var rest = unexplainedMs(measured, km);
    var meas = R(BigInt(measured), 1n);
    var ratio = Rdiv(meas, floor);

    document.getElementById('lsFloor').textContent = Rfixed(floor, 3) + ' ms';
    document.getElementById('lsMeasured').textContent = measured + ' ms';
    document.getElementById('lsRatio').textContent = Rfixed(ratio, 3) + '&times;';
    document.getElementById('lsRest').textContent = Rfixed(rest, 3) + ' ms';

    table.innerHTML = '<thead><tr><th>step</th><th>exactly</th><th>ms</th></tr></thead><tbody>'
      + '<tr><td>distance there and back</td><td>2 &times; ' + commas(km) + ' km</td><td>&mdash;</td></tr>'
      + '<tr><td>speed in fibre</td><td>&#8532; &times; 299 792 458 m/s</td><td>&mdash;</td></tr>'
      + '<tr><td class="tone-green">floor = 3d / c</td><td>' + Rtext(floor) + '</td><td>' + Rfixed(floor, 4) + '</td></tr>'
      + '<tr><td>measured</td><td>' + measured + '</td><td>' + measured + '.0000</td></tr>'
      + '<tr><td class="tone-red">remainder</td><td>' + Rtext(rest) + '</td><td>' + Rfixed(rest, 4) + '</td></tr>'
      + '</tbody>';

    var top = Rcmp(meas, floor) > 0 ? meas : floor;
    var unit = 500 / Math.max(0.001, parseFloat(Rfixed(top, 6)));
    var fpx = Math.max(1, parseFloat(Rfixed(floor, 6)) * unit);
    var rpx = Math.max(0, parseFloat(Rfixed(rest, 6)) * unit);
    var s = '<text x="0" y="16" font-size="11" fill="var(--muted)">the measured round trip, split</text>'
      + '<rect x="0" y="28" width="' + fpx + '" height="30" rx="3" fill="var(--green)" opacity="0.85" />';
    if (rpx > 0) {
      s += '<rect x="' + fpx + '" y="28" width="' + rpx + '" height="30" rx="3" fill="var(--red)" opacity="0.7" />';
    }
    s += '<text x="2" y="76" font-size="10" fill="var(--green)">floor ' + Rfixed(floor, 2) + ' ms</text>'
      + (rpx > 24 ? '<text x="' + (fpx + 4) + '" y="76" font-size="10" fill="var(--red)">remainder '
          + Rfixed(rest, 2) + ' ms</text>' : '')
      + '<line x1="0" y1="92" x2="520" y2="92" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="110" font-size="10" fill="var(--muted)">the green bar is what physics charges; '
      + 'only the red bar is engineering, and only the red bar can be removed</text>';
    plot.innerHTML = s;

    var below = Rcmp(meas, floor) < 0;
    status.innerHTML = below
      ? '<span class="tone-red">' + measured + ' ms is below the ' + Rfixed(floor, 3)
        + ' ms floor for ' + commas(km) + ' km.</span> That is not a fast network; it is a measurement '
        + 'of something nearer than you think, or of a cache that never left the continent.'
      : 'Over ' + commas(km) + ' km the round trip cannot be under <strong>' + Rfixed(floor, 3)
        + ' ms</strong>. A measured ' + measured + ' ms is <strong>' + Rfixed(ratio, 3)
        + '&times;</strong> the floor, leaving <strong>' + Rfixed(rest, 3) + ' ms</strong> ('
        + Rpct(Rdiv(rest, meas), 1) + ' of the trip) that queueing, serialisation and software are '
        + 'spending. Moving the content closer changes the green bar; everything else you can do '
        + 'changes only the red one.';
  }

  routeSel.addEventListener('change', function () {
    if (routeSel.value !== 'custom') kmS.value = routeSel.value;
    redraw();
  });
  [kmS, rttS].forEach(function (el) { el.addEventListener('input', redraw); });
  routeSel.value = '""" + str(km) + r"""';
  kmS.value = """ + str(km) + r"""; rttS.value = """ + str(measured) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The floor under a route",
        subtitle="What the distance costs, and what is left over to blame on the system",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a route, or set a distance"),
        panel_intro=cfg.get(
            "panel_intro",
            "The floor is 3d/c and c is exact, so the green bar is a fact about the route. "
            "Everything above it is the part you can work on.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - roundtrips
# ---------------------------------------------------------------------------


def _roundtrips(cfg):
    dns = int(cfg.get("dns", 1))
    tcp = int(cfg.get("tcp", 1))
    tls = int(cfg.get("tls", 2))
    req = int(cfg.get("req", 1))
    rtt = int(cfg.get("rtt", 80))
    mbps = int(cfg.get("bandwidth", 10))
    kb = int(cfg.get("payload_kb", 14))

    markup = (
        _toolbar(
            "Round trips, not bytes",
            "k &times; RTT laid end to end, against the bytes",
            [("amber", "a round trip"), ("cyan", "the payload"), ("purple", "crossover payload")],
        )
        + _stage(_svg("rtPlot", "0 0 520 150", "Each round trip drawn as a block on a timeline, then the transfer."))
        + _table("rtTable")
        + _banner("rtStatus")
    )
    controls = (
        _select("rtDns", "DNS lookup", [("1", "1 round trip"), ("0", "cached (0)")], str(dns))
        + _select("rtTcp", "TCP handshake", [("1", "1 round trip"), ("0", "connection reused (0)")], str(tcp))
        + _select(
            "rtTls",
            "TLS handshake",
            [("2", "TLS 1.2 (2 round trips)"), ("1", "TLS 1.3 (1)"), ("0", "resumed / plaintext (0)")],
            str(tls),
        )
        + _select("rtReq", "The request itself", [("1", "1 round trip"), ("0", "pushed (0)")], str(req))
        + _range("rtRtt", "Round-trip time (ms)", 1, 300, rtt)
        + _range("rtBw", "Bandwidth (Mbit/s)", 1, 1000, mbps)
        + _range("rtSize", "Payload (kB)", 1, 2000, kb)
        + _kpis(
            [
                ("Round trips k", "rtK"),
                ("Time to first byte", "rtTtfb"),
                ("Total time", "rtTotal"),
                ("Crossover payload", "rtCross"),
            ]
        )
        + _hint(
            "rtHint",
            "Every handshake is sequential: none of them can start until the one before it has "
            "finished. That is why the count matters more than the bytes, and why the fix for a "
            "slow first load is usually removing a round trip rather than removing a kilobyte.",
        )
    )

    script = _CORE_JS + r"""
  var dnsSel = document.getElementById('rtDns'), tcpSel = document.getElementById('rtTcp');
  var tlsSel = document.getElementById('rtTls'), reqSel = document.getElementById('rtReq');
  var rttS = document.getElementById('rtRtt'), bwS = document.getElementById('rtBw'), szS = document.getElementById('rtSize');
  var plot = document.getElementById('rtPlot'), table = document.getElementById('rtTable');
  var status = document.getElementById('rtStatus');
  var LEGS = [['DNS lookup', dnsSel], ['TCP handshake', tcpSel], ['TLS handshake', tlsSel], ['request', reqSel]];

  function redraw() {
    var rtt = +rttS.value, mbps = +bwS.value, kb = +szS.value, bytes = kb * 1000;
    document.getElementById('rtRttOut').textContent = rtt + ' ms';
    document.getElementById('rtBwOut').textContent = mbps + ' Mbit/s';
    document.getElementById('rtSizeOut').textContent = bytesText(bytes);

    var k = 0, i, rows = '';
    for (i = 0; i < LEGS.length; i += 1) k += +LEGS[i][1].value;
    var trips = R(BigInt(k * rtt), 1n);
    var send = transferMs(bytes, mbps);
    var total = Radd(trips, send);
    var cross = crossoverBytes(k, rtt, mbps);

    document.getElementById('rtK').textContent = k + (k === 1 ? ' round trip' : ' round trips');
    document.getElementById('rtTtfb').textContent = Rfixed(trips, 3) + ' ms';
    document.getElementById('rtTotal').textContent = Rfixed(total, 3) + ' ms';
    document.getElementById('rtCross').textContent = k ? bytesText(cross.n / cross.d) : 'no round trips left';

    var at = 0;
    for (i = 0; i < LEGS.length; i += 1) {
      var n = +LEGS[i][1].value;
      rows += '<tr><td>' + LEGS[i][0] + '</td><td>' + n + '</td><td>' + (n * rtt) + '</td><td>'
        + (n ? at + ' &rarr; ' + (at + n * rtt) : '&mdash;') + '</td></tr>';
      at += n * rtt;
    }
    rows += '<tr><td class="tone-cyan">payload ' + bytesText(bytes) + '</td><td>&mdash;</td><td>'
      + Rfixed(send, 3) + '</td><td>' + at + ' &rarr; ' + Rfixed(total, 3) + '</td></tr>';
    table.innerHTML = '<thead><tr><th>leg</th><th>round trips</th><th>ms</th><th>window</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var totalMs = parseFloat(Rfixed(total, 6)) || 1;
    var unit = 508 / totalMs, x = 0, s = '';
    for (i = 0; i < LEGS.length; i += 1) {
      var count = +LEGS[i][1].value, j;
      for (j = 0; j < count; j += 1) {
        var w = rtt * unit;
        s += '<rect x="' + x + '" y="30" width="' + Math.max(1, w - 2) + '" height="30" rx="3" '
          + 'fill="var(--amber)" opacity="' + (0.55 + 0.1 * i) + '" />';
        if (w > 34) s += '<text x="' + (x + w / 2 - 1) + '" y="50" text-anchor="middle" font-size="9" '
          + 'fill="var(--bg)">' + rtt + '</text>';
        x += w;
      }
    }
    var sw = parseFloat(Rfixed(send, 6)) * unit;
    s += '<rect x="' + x + '" y="30" width="' + Math.max(1, sw) + '" height="30" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="0" y="20" font-size="11" fill="var(--muted)">' + k + ' &times; ' + rtt
      + ' ms of handshakes, then ' + Rfixed(send, 2) + ' ms of bytes</text>'
      + '<line x1="0" y1="72" x2="520" y2="72" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="0" y="92" font-size="10" fill="var(--purple)">the cyan block only catches the amber ones at '
      + (k ? bytesText(cross.n / cross.d) : '&mdash;') + '</text>'
      + '<text x="0" y="112" font-size="10" fill="var(--muted)">time to first byte: ' + Rfixed(trips, 2)
      + ' ms &mdash; total: ' + Rfixed(total, 2) + ' ms</text>';
    plot.innerHTML = s;

    var tripsWin = Rcmp(trips, send) > 0;
    status.innerHTML = k === 0
      ? 'With every handshake removed the whole time is the <span class="tone-cyan">'
        + Rfixed(send, 3) + ' ms</span> of bytes. That is the only regime in which shaving kilobytes is the fix.'
      : '<strong>' + k + ' round trips at ' + rtt + ' ms is ' + Rfixed(trips, 1) + ' ms</strong> before a byte of '
        + 'the answer arrives; the ' + bytesText(bytes) + ' payload then costs ' + Rfixed(send, 3) + ' ms, '
        + 'for ' + Rfixed(total, 3) + ' ms in all. '
        + (tripsWin
            ? 'The round trips are <span class="tone-amber">' + Rfixed(Rdiv(trips, send), 1)
              + '&times;</span> the bytes: you would have to grow the payload to '
              + bytesText(cross.n / cross.d) + ' before the bytes cost as much. Removing one handshake saves '
              + rtt + ' ms &mdash; the same as deleting ' + bytesText(crossoverBytes(1, rtt, mbps).n / crossoverBytes(1, rtt, mbps).d) + '.'
            : 'The bytes now cost more than the handshakes, because ' + bytesText(bytes) + ' is past the '
              + bytesText(cross.n / cross.d) + ' crossover.');
  }

  [dnsSel, tcpSel, tlsSel, reqSel].forEach(function (el) { el.addEventListener('change', redraw); });
  [rttS, bwS, szS].forEach(function (el) { el.addEventListener('input', redraw); });
  dnsSel.value = '""" + str(dns) + r"""'; tcpSel.value = '""" + str(tcp) + r"""';
  tlsSel.value = '""" + str(tls) + r"""'; reqSel.value = '""" + str(req) + r"""';
  rttS.value = """ + str(rtt) + r"""; bwS.value = """ + str(mbps) + r"""; szS.value = """ + str(kb) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Counting round trips",
        subtitle="k × RTT + bytes ÷ bandwidth, with k the part you can change",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Turn handshakes on and off"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each handshake waits for the one before it, so the count multiplies the round-trip "
            "time. The crossover is the payload at which the bytes finally cost as much.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4 - dag
# ---------------------------------------------------------------------------

_DAG_STAGES = [
    ("gateway", "dgT0", 4, 1, 60),
    ("authz", "dgT1", 18, 1, 120),
    ("cache", "dgT2", 6, 1, 120),
    ("enrich", "dgT3", 22, 1, 120),
    ("db", "dgT4", 55, 1, 200),
    ("render", "dgT5", 12, 1, 120),
    ("respond", "dgT6", 3, 1, 60),
]

# Edges as index pairs. Index order is already topological, which is what makes
# the one-pass evaluation in dagSchedule correct.
_DAG_BASE_EDGES = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]]


def _dag(cfg):
    times = [int(cfg.get(cid, default)) for _, cid, default, _lo, _hi in _DAG_STAGES]
    serialise = str(cfg.get("serialise", "0"))
    enrich_first = str(cfg.get("enrich_first", "0"))

    markup = (
        _toolbar(
            "Serial sums, parallel maxes",
            "the longest path through the stage graph, and what every other stage has spare",
            [("red", "critical path"), ("cyan", "has slack"), ("muted", "dependency")],
        )
        + _stage(_svg("dgPlot", "0 0 660 200", "The stage graph, with the critical path drawn through it."))
        + _table("dgTable")
        + _banner("dgStatus")
    )
    controls = (
        _select(
            "dgSerial",
            "Edge: authz &rarr; cache",
            [("0", "absent (cache runs beside authz)"), ("1", "present (cache waits for authz)")],
            serialise,
        )
        + _select(
            "dgEnrich",
            "Edge: enrich &rarr; db",
            [("0", "absent (db needs only the key)"), ("1", "present (db needs the enriched key)")],
            enrich_first,
        )
        + "".join(
            _range(cid, "%s (ms)" % name, lo, hi, value)
            for (name, cid, _d, lo, hi), value in zip(_DAG_STAGES, times)
        )
        + _kpis(
            [
                ("End to end", "dgLength"),
                ("Critical path", "dgPath"),
                ("Stages with slack", "dgSlackCount"),
                ("Largest slack", "dgMaxSlack"),
            ]
        )
        + _hint(
            "dgHint",
            "Slack is how much a stage could grow before the answer changes. A stage with slack "
            "can be made instant and the end-to-end time will not move, which is why the slack "
            "column is the list of optimisations that do nothing.",
        )
    )

    script = (
        _CORE_JS
        + cfg_literal("STAGE_NAMES", [name for name, _c, _d, _lo, _hi in _DAG_STAGES])
        + cfg_literal("BASE_EDGES", _DAG_BASE_EDGES)
        + r"""
  var serialSel = document.getElementById('dgSerial'), enrichSel = document.getElementById('dgEnrich');
  var SLIDERS = ['dgT0', 'dgT1', 'dgT2', 'dgT3', 'dgT4', 'dgT5', 'dgT6'].map(function (id) {
    return document.getElementById(id);
  });
  var plot = document.getElementById('dgPlot'), table = document.getElementById('dgTable');
  var status = document.getElementById('dgStatus');

  function edgeList() {
    var edges = BASE_EDGES.map(function (e) { return [e[0], e[1]]; });
    if (serialSel.value === '1') edges.push([1, 2]);   /* authz -> cache */
    if (enrichSel.value === '1') edges.push([3, 4]);   /* enrich -> db   */
    return edges;
  }

  function columns(n, edges) {
    /* depth = the longest chain of edges reaching a stage; it is also where
       the stage belongs on the drawing, because a stage cannot start before
       everything upstream of it has. */
    var depth = [], i, e;
    for (i = 0; i < n; i += 1) depth.push(0);
    for (i = 0; i < n; i += 1) {
      for (e = 0; e < edges.length; e += 1) {
        if (edges[e][1] === i && edges[e][0] < i && depth[edges[e][0]] + 1 > depth[i]) {
          depth[i] = depth[edges[e][0]] + 1;
        }
      }
    }
    return depth;
  }

  function redraw() {
    var times = SLIDERS.map(function (el) { return +el.value; }), i;
    for (i = 0; i < SLIDERS.length; i += 1) {
      document.getElementById(SLIDERS[i].id + 'Out').textContent = times[i] + ' ms';
    }
    var edges = edgeList();
    var sched = dagSchedule(times, edges);
    var onPath = {};
    for (i = 0; i < sched.path.length; i += 1) onPath[sched.path[i]] = true;

    var slackCount = 0, maxSlack = 0, maxSlackAt = -1;
    for (i = 0; i < times.length; i += 1) {
      if (sched.slack[i] > 0) slackCount += 1;
      if (sched.slack[i] > maxSlack) { maxSlack = sched.slack[i]; maxSlackAt = i; }
    }

    document.getElementById('dgLength').textContent = sched.length + ' ms';
    document.getElementById('dgPath').textContent = sched.path.map(function (ix) { return STAGE_NAMES[ix]; }).join(' → ');
    document.getElementById('dgSlackCount').textContent = slackCount + ' of ' + times.length;
    document.getElementById('dgMaxSlack').textContent = maxSlackAt < 0
      ? 'none' : maxSlack + ' ms (' + STAGE_NAMES[maxSlackAt] + ')';

    var rows = '';
    for (i = 0; i < times.length; i += 1) {
      var crit = sched.slack[i] === 0;
      rows += '<tr><td class="' + (crit ? 'tone-red' : 'tone-cyan') + '">' + STAGE_NAMES[i] + '</td><td>'
        + times[i] + '</td><td>' + sched.ES[i] + '</td><td>' + sched.EF[i] + '</td><td>' + sched.LS[i]
        + '</td><td>' + sched.LF[i] + '</td><td>' + sched.slack[i] + '</td><td>'
        + (crit ? 'critical' : 'free') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>stage</th><th>ms</th><th>earliest start</th><th>earliest finish</th>'
      + '<th>latest start</th><th>latest finish</th><th>slack</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var depth = columns(times.length, edges), maxDepth = 0, seen = {}, row = [], x = [], y = [];
    for (i = 0; i < depth.length; i += 1) if (depth[i] > maxDepth) maxDepth = depth[i];
    for (i = 0; i < depth.length; i += 1) {
      var d = depth[i];
      row.push(seen[d] || 0);
      seen[d] = (seen[d] || 0) + 1;
    }
    var colW = maxDepth > 0 ? Math.min(150, 544 / maxDepth) : 150;
    for (i = 0; i < depth.length; i += 1) { x.push(12 + depth[i] * colW); y.push(24 + row[i] * 62); }

    var s = '', e;
    for (e = 0; e < edges.length; e += 1) {
      var u = edges[e][0], w = edges[e][1];
      if (u >= w) continue;
      var hot = onPath[u] && onPath[w] && sched.ES[u] + times[u] === sched.ES[w];
      s += '<line x1="' + (x[u] + 92) + '" y1="' + (y[u] + 17) + '" x2="' + x[w] + '" y2="' + (y[w] + 17)
        + '" stroke="' + (hot ? 'var(--red)' : 'var(--line-strong)') + '" stroke-width="' + (hot ? 2.5 : 1.2)
        + '" opacity="' + (hot ? 0.9 : 0.5) + '" />';
    }
    for (i = 0; i < times.length; i += 1) {
      var critical = sched.slack[i] === 0;
      s += '<rect x="' + x[i] + '" y="' + y[i] + '" width="92" height="34" rx="5" fill="'
        + (critical ? 'var(--red)' : 'var(--cyan)') + '" opacity="' + (critical ? 0.9 : 0.45) + '" />'
        + '<text x="' + (x[i] + 46) + '" y="' + (y[i] + 15) + '" text-anchor="middle" font-size="10.5" '
        + 'fill="var(--bg)" font-weight="700">' + STAGE_NAMES[i] + '</text>'
        + '<text x="' + (x[i] + 46) + '" y="' + (y[i] + 28) + '" text-anchor="middle" font-size="9.5" '
        + 'fill="var(--bg)">' + times[i] + ' ms' + (critical ? '' : ' · slack ' + sched.slack[i]) + '</text>';
    }
    s += '<text x="12" y="192" font-size="10" fill="var(--muted)">end to end = the longest path = '
      + sched.length + ' ms</text>';
    plot.innerHTML = s;

    var naive = 0;
    for (i = 0; i < times.length; i += 1) naive += times[i];
    var freeText = maxSlackAt < 0
      ? 'Every stage is on the path.'
      : 'Making <strong>' + STAGE_NAMES[maxSlackAt] + '</strong> instant would save <strong>0 ms</strong>: it has '
        + maxSlack + ' ms of slack, so it could take ' + (times[maxSlackAt] + maxSlack)
        + ' ms before the answer moved at all.';
    status.innerHTML = 'The end-to-end time is <strong>' + sched.length + ' ms</strong> &mdash; the longest path, '
      + '<span class="tone-red">' + sched.path.map(function (ix) { return STAGE_NAMES[ix]; }).join(' → ')
      + '</span>, not the ' + naive + ' ms the stages add up to and not the '
      + Math.max.apply(null, times) + ' ms of the slowest stage. ' + freeText
      + ' Shave a millisecond off any critical stage and the whole request gets a millisecond faster; '
      + 'shave one off any other and nothing happens.';
  }

  [serialSel, enrichSel].forEach(function (el) { el.addEventListener('change', redraw); });
  SLIDERS.forEach(function (el) { el.addEventListener('input', redraw); });
  serialSel.value = '""" + serialise + r"""'; enrichSel.value = '""" + enrich_first + r"""';
""" + "".join(
            "  document.getElementById('%s').value = %d;\n" % (cid, value)
            for (_n, cid, _d, _lo, _hi), value in zip(_DAG_STAGES, times)
        ) + r"""  redraw();
  window.redrawLab = redraw;
"""
    )
    return Lab(
        title="The critical path through a stage graph",
        subtitle="Serial stages add, parallel stages take the max, and slack names the rest",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the stages and the dependencies"),
        panel_intro=cfg.get(
            "panel_intro",
            "Earliest and latest times are computed in one pass over the graph; their difference "
            "is slack, and a stage with slack is a stage whose speed does not matter.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - percentile
# ---------------------------------------------------------------------------

_PERCENTILE_SAMPLE = "12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420"


def _percentile(cfg):
    sample = str(cfg.get("sample", _PERCENTILE_SAMPLE))
    q = int(cfg.get("q", 99))

    markup = (
        _toolbar(
            "Percentiles from a sample",
            "a rank in a sorted list, not an average of anything",
            [("cyan", "the sample"), ("amber", "the selected rank"), ("red", "the mean")],
        )
        + _stage(_svg("pcPlot", "0 0 520 150", "The sorted sample as ticks on a time axis, with the percentiles marked."))
        + _table("pcTable")
        + _banner("pcStatus")
    )
    controls = (
        _text("pcSample", "The sample (milliseconds, any separator)", sample)
        + _range("pcQ", "Percentile to select", 1, 100, q)
        + _kpis(
            [
                ("p50 (median)", "pcP50"),
                ("p95", "pcP95"),
                ("p99", "pcP99"),
                ("Mean", "pcMean"),
            ]
        )
        + _hint(
            "pcHint",
            "The rank is &lceil;q &times; n&rceil;, so the answer is always a value some request "
            "actually took. The mean is not: it is an arithmetic average that can land in a gap "
            "no request ever occupied.",
        )
    )

    script = _CORE_JS + r"""
  var sampleIn = document.getElementById('pcSample'), qS = document.getElementById('pcQ');
  var plot = document.getElementById('pcPlot'), table = document.getElementById('pcTable');
  var status = document.getElementById('pcStatus');

  function redraw() {
    var q = +qS.value;
    document.getElementById('pcQOut').textContent = 'p' + q;
    var sorted = parseSample(sampleIn.value);
    if (!sorted) {
      plot.innerHTML = '';
      table.innerHTML = '';
      ['pcP50', 'pcP95', 'pcP99', 'pcMean'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      status.innerHTML = '<span class="tone-red">No numbers in that sample.</span> Type request times in '
        + 'milliseconds, separated by commas or spaces.';
      return;
    }

    var n = sorted.length;
    var qr = R(BigInt(q), 100n);
    var rank = percentileRank(n, qr);
    var picked = percentile(sorted, qr);
    var p50 = percentile(sorted, R(1n, 2n)), p95 = percentile(sorted, R(95n, 100n)), p99 = percentile(sorted, R(99n, 100n));
    var mean = sampleMean(sorted);
    var faster = countBelow(sorted, mean);

    document.getElementById('pcP50').textContent = p50 + ' ms (rank ' + percentileRank(n, R(1n, 2n)) + ')';
    document.getElementById('pcP95').textContent = p95 + ' ms (rank ' + percentileRank(n, R(95n, 100n)) + ')';
    document.getElementById('pcP99').textContent = p99 + ' ms (rank ' + percentileRank(n, R(99n, 100n)) + ')';
    document.getElementById('pcMean').textContent = Rtext(mean) + ' = ' + Rfixed(mean, 2) + ' ms';

    var rows = '', i;
    for (i = 0; i < n; i += 1) {
      var atRank = (i + 1) === rank;
      rows += '<tr><td>' + (i + 1) + '</td><td class="' + (atRank ? 'tone-amber' : '') + '">' + sorted[i]
        + '</td><td>' + Rfixed(R(BigInt(i + 1), BigInt(n)), 4) + '</td><td>'
        + (atRank ? 'selected by p' + q : '') + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>rank</th><th>ms</th><th>rank / n</th><th></th></tr></thead><tbody>'
      + rows + '</tbody>';

    var lo = sorted[0], hi = sorted[n - 1], span = (hi - lo) || 1;
    function px(v) { return 10 + ((v - lo) / span) * 500; }
    var s = '';
    for (i = 0; i < n; i += 1) {
      s += '<line x1="' + px(sorted[i]) + '" y1="46" x2="' + px(sorted[i]) + '" y2="78" stroke="var(--cyan)" '
        + 'stroke-width="2" opacity="0.7" />';
    }
    var mx = px(parseFloat(Rfixed(mean, 6)));
    s += '<line x1="' + px(picked) + '" y1="34" x2="' + px(picked) + '" y2="90" stroke="var(--amber)" stroke-width="2.5" />'
      + '<text x="' + Math.min(px(picked) + 5, 400) + '" y="30" font-size="10" fill="var(--amber)" font-weight="700">p'
      + q + ' = ' + picked + ' ms</text>'
      + '<line x1="' + mx + '" y1="34" x2="' + mx + '" y2="90" stroke="var(--red)" stroke-width="2" stroke-dasharray="4 3" />'
      + '<text x="' + Math.min(mx + 5, 400) + '" y="110" font-size="10" fill="var(--red)">mean = '
      + Rfixed(mean, 2) + ' ms</text>'
      + '<line x1="10" y1="90" x2="510" y2="90" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="132" font-size="10" fill="var(--muted)">' + lo + ' ms</text>'
      + '<text x="510" y="132" text-anchor="end" font-size="10" fill="var(--muted)">' + hi + ' ms</text>'
      + '<text x="10" y="16" font-size="11" fill="var(--muted)">' + n + ' requests, sorted; each tick is one</text>';
    plot.innerHTML = s;

    var maxedOut = rank === n && q < 100;
    status.innerHTML = 'p' + q + ' of ' + n + ' samples is rank &lceil;' + q + '/100 &times; ' + n + '&rceil; = <strong>'
      + rank + '</strong>, and the ' + rank + 'th sorted value is <strong>' + picked + ' ms</strong> &mdash; '
      + 'a time a request actually took. The mean is <strong>' + Rtext(mean) + ' = ' + Rfixed(mean, 2)
      + ' ms</strong>, and <strong>' + faster + ' of ' + n + '</strong> requests ('
      + Rpct(R(BigInt(faster), BigInt(n)), 0) + ') were faster than it, so the mean is not what a typical '
      + 'user sees; it is the median ' + p50 + ' ms that is. '
      + (maxedOut
          ? '<span class="tone-amber">Note that rank ' + rank + ' is the largest value in the sample.</span> '
            + 'With ' + n + ' measurements every percentile above ' + Rfixed(R(BigInt(n - 1), BigInt(n)), 4)
            + ' selects the maximum &mdash; you cannot measure a p99 from ' + n + ' requests, you can only '
            + 'measure the worst of ' + n + '.'
          : (p50 > 0
              ? 'The tail is ' + Rfixed(R(BigInt(p99), BigInt(p50)), 1) + '&times; the median here.'
              : 'The median is 0 ms, so the tail has no ratio to it.'));
  }

  sampleIn.addEventListener('input', redraw);
  qS.addEventListener('input', redraw);
  sampleIn.value = """ + _js_string(sample) + r""";
  qS.value = """ + str(q) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="p50, p95, p99 and the mean",
        subtitle="Four numbers about one sample, three of which a request actually took",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the sample"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every value is selected by rank from the sorted list you typed, and the rank is "
            "printed beside it so the selection can be checked by eye.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 - fanout
# ---------------------------------------------------------------------------


def _fanout(cfg):
    width = int(cfg.get("width", 69))
    pct = str(cfg.get("percentile", "99/100"))

    markup = (
        _toolbar(
            "Tail amplification under fan-out",
            "P(all n calls land inside their own percentile) = p&#8319;",
            [("cyan", "P(at least one slow)"), ("amber", "your fan-out"), ("purple", "break-even n")],
        )
        + _stage(_svg("foPlot", "0 0 520 190", "The probability that a request is slow, plotted against the fan-out width."))
        + _table("foTable")
        + _banner("foStatus")
    )
    controls = (
        _select(
            "foP",
            "Per-call percentile the calls sit inside",
            [
                ("9/10", "p90 (nine in ten are fast)"),
                ("19/20", "p95"),
                ("99/100", "p99"),
                ("999/1000", "p99.9"),
            ],
            pct,
        )
        + _range("foN", "Fan-out width n", 1, 400, width)
        + _kpis(
            [
                ("P(all n fast) = p&#8319;", "foAll"),
                ("P(at least one slow)", "foSlow"),
                ("Break-even n (p&#8319; = &frac12;)", "foBreak"),
                ("Checked against pmfMax", "foCheck"),
            ]
        )
        + _hint(
            "foHint",
            "Each call is fast with probability p and they are independent, so all n are fast with "
            "probability p&#8319;. There is no n at which this stops mattering; there is only the n "
            "at which the per-call tail has become the request's ordinary experience.",
        )
    )

    script = _CORE_JS + r"""
  var pSel = document.getElementById('foP'), nS = document.getElementById('foN');
  var plot = document.getElementById('foPlot'), table = document.getElementById('foTable');
  var status = document.getElementById('foStatus');
  var SAMPLES = 61;

  function readP() {
    var parts = pSel.value.split('/');
    return R(BigInt(parts[0]), BigInt(parts[1]));
  }

  function redraw() {
    var n = +nS.value, p = readP();
    document.getElementById('foNOut').textContent = n + (n === 1 ? ' call' : ' calls');

    var all = Rpow(p, n);
    var slow = Rsub(R(1n, 1n), all);
    var breakEven = fanoutBreakEven(p, 20000);

    /* The same number a second way: a call is a two-outcome distribution --
       0 for "inside its percentile", 1 for "outside" -- and the maximum of n
       independent copies is 0 exactly when every one of them is. */
    var per = [[0, p], [1, Rsub(R(1n, 1n), p)]];
    var mx = pmfMax(per, n);
    var agrees = Requ(mx[0][1], all);

    document.getElementById('foAll').textContent = Rfixed(all, 6);
    document.getElementById('foSlow').textContent = Rpct(slow, 4);
    document.getElementById('foBreak').textContent = breakEven ? 'n = ' + breakEven : 'beyond 20 000';
    document.getElementById('foCheck').textContent = agrees ? 'agrees exactly' : 'DISAGREES';

    var marks = [1, 2, 5, 10, 20, 50, 69, 100, 200, 400], rows = '', i;
    if (marks.indexOf(n) < 0) { marks.push(n); marks.sort(function (a, b) { return a - b; }); }
    if (breakEven && marks.indexOf(breakEven) < 0) { marks.push(breakEven); marks.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < marks.length; i += 1) {
      var m = marks[i], pa = Rpow(p, m);
      var tag = m === n ? 'tone-amber' : (m === breakEven ? 'tone-purple' : '');
      rows += '<tr><td class="' + tag + '">' + m + '</td><td>' + Rfixed(pa, 6) + '</td><td>'
        + Rpct(Rsub(R(1n, 1n), pa), 3) + '</td><td>'
        + (m === breakEven ? 'the per-call tail is now the median' : (m === n ? 'your fan-out' : '')) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>fan-out n</th><th>P(all fast) = p<sup>n</sup></th>'
      + '<th>P(at least one slow)</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var span = Math.max(n, breakEven ? Math.round(breakEven * 1.6) : n, 10);
    var pts = [], j;
    for (j = 0; j < SAMPLES; j += 1) {
      var xn = Math.round(j * span / (SAMPLES - 1));
      var val = parseFloat(Rfixed(Rsub(R(1n, 1n), Rpow(p, xn)), 9));
      pts.push((10 + (xn / span) * 500) + ',' + (150 - val * 130));
    }
    var bx = breakEven ? 10 + (breakEven / span) * 500 : -100;
    var nx = 10 + (n / span) * 500;
    var s = '<line x1="10" y1="20" x2="510" y2="20" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="14" y="17" font-size="9" fill="var(--muted)">1</text>'
      + '<line x1="10" y1="85" x2="510" y2="85" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="14" y="82" font-size="9" fill="var(--muted)">&frac12;</text>'
      + '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />';
    if (breakEven && breakEven <= span) {
      s += '<line x1="' + bx + '" y1="20" x2="' + bx + '" y2="150" stroke="var(--purple)" stroke-width="2" '
        + 'stroke-dasharray="5 4" /><text x="' + Math.min(bx + 5, 250) + '" y="36" font-size="10" '
        + 'fill="var(--purple)" font-weight="700">n = ' + breakEven + ': half of all requests are slow</text>';
    }
    s += '<line x1="' + nx + '" y1="20" x2="' + nx + '" y2="150" stroke="var(--amber)" stroke-width="2" />'
      + '<text x="' + Math.min(nx + 5, 400) + '" y="' + Math.max(52, 150 - parseFloat(Rfixed(slow, 6)) * 130 - 8)
      + '" font-size="10" fill="var(--amber)" font-weight="700">n = ' + n + ': ' + Rpct(slow, 2) + '</text>'
      + '<line x1="10" y1="150" x2="510" y2="150" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="10" y="168" font-size="10" fill="var(--muted)">fan-out width, 0 to ' + span + '</text>'
      + '<text x="510" y="168" text-anchor="end" font-size="10" fill="var(--muted)">'
      + 'vertical axis: P(at least one call is slow)</text>';
    plot.innerHTML = s;

    var pText = Rtext(p);
    status.innerHTML = 'Every one of the ' + n + ' calls is fast with probability ' + pText
      + ', and they are independent, so all ' + n + ' are fast with probability ' + pText + '<sup>' + n
      + '</sup> = <strong>' + Rfixed(all, 6) + '</strong>. The request is therefore slow <strong>'
      + Rpct(slow, 3) + '</strong> of the time. '
      + (breakEven
          ? 'At <span class="tone-purple">n = ' + breakEven + '</span> that reaches one half: a fan-out that '
            + 'wide has turned each service\'s ' + Rpct(Rsub(R(1n, 1n), p), 1) + ' tail into the median '
            + 'experience of the request. '
          : '')
      + 'The two computations agree exactly (p<sup>n</sup> by repeated squaring, and P(max = fast) from '
      + 'pmfMax over the two-outcome distribution), which is the same fact stated twice.';
  }

  pSel.addEventListener('change', redraw);
  nS.addEventListener('input', redraw);
  pSel.value = '""" + pct + r"""'; nS.value = """ + str(width) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="What a fan-out does to a tail",
        subtitle="pⁿ, and the width at which a per-call p99 becomes the request's median",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the fan-out"),
        panel_intro=cfg.get(
            "panel_intro",
            "p&#8319; is computed as an exact fraction and checked against the maximum of n "
            "independent copies, which is the same statement in the language of distributions.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - hedge
# ---------------------------------------------------------------------------

_HEDGE_SPEC = "10:40, 12:25, 15:15, 20:10, 30:5, 50:3, 120:1, 300:1"


def _hedge(cfg):
    spec = str(cfg.get("spec", _HEDGE_SPEC))
    delay = int(cfg.get("delay", 30))

    markup = (
        _toolbar(
            "Hedged requests",
            "send a backup after d; the request finishes at min(X, d + Y)",
            [("cyan", "one copy"), ("green", "hedged"), ("amber", "the hedge delay")],
        )
        + _stage(_svg("hgPlot", "0 0 520 180", "The survival curve of one copy against the hedged survival curve."))
        + _table("hgTable")
        + _banner("hgStatus")
    )
    controls = (
        _text("hgSpec", "The service's latency, as ms:count pairs", spec)
        + _range("hgDelay", "Hedge delay d (ms)", 1, 300, delay)
        + _kpis(
            [
                ("p99 of one copy", "hgBase"),
                ("p99 hedged", "hgHedged"),
                ("P(both slow) = p&sup2;", "hgSquare"),
                ("Extra load", "hgLoad"),
            ]
        )
        + _hint(
            "hgHint",
            "The backup only goes out if the first copy is still running at d, so the extra load "
            "is exactly the tail past d. Hedging at the median doubles the traffic; hedging at the "
            "p95 adds a twentieth of it.",
        )
    )

    script = _CORE_JS + r"""
  var specIn = document.getElementById('hgSpec'), dS = document.getElementById('hgDelay');
  var plot = document.getElementById('hgPlot'), table = document.getElementById('hgTable');
  var status = document.getElementById('hgStatus');
  var KPIS = ['hgBase', 'hgHedged', 'hgSquare', 'hgLoad'];

  function redraw() {
    var d = +dS.value;
    document.getElementById('hgDelayOut').textContent = d + ' ms';
    var spec = parsePmfSpec(specIn.value);
    var pmf = spec ? pmfFromSpec(spec) : null;
    if (!pmf) {
      plot.innerHTML = '';
      table.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That distribution did not parse.</span> Write it as '
        + 'milliseconds and counts: <span class="tone-muted">10:40, 12:25, 30:5</span>.';
      return;
    }

    var q99 = R(99n, 100n), q50 = R(1n, 2n);
    var base99 = pmfPercentile(pmf, q99);
    var base50 = pmfPercentile(pmf, q50);
    var tailAtD = hedgeLoad(pmf, d);
    var squared = Rpow(tailAtD, 2);
    var hedged99 = hedgedQuantile(pmf, d, q99);
    var hedged50 = hedgedQuantile(pmf, d, q50);

    document.getElementById('hgBase').textContent = base99 + ' ms';
    document.getElementById('hgHedged').textContent = hedged99 === null ? 'no time qualifies' : hedged99 + ' ms';
    document.getElementById('hgSquare').textContent = Rtext(squared) + ' = ' + Rpct(squared, 4);
    document.getElementById('hgLoad').textContent = '+' + Rpct(tailAtD, 2);

    var grid = hedgeGrid(pmf, d), rows = '', i;
    for (i = 0; i < grid.length; i += 1) {
      var t = grid[i], one = pmfTail(pmf, t), both = hedgedTail(pmf, d, t);
      var tag = (hedged99 !== null && t === hedged99) ? 'tone-green' : (t === d ? 'tone-amber' : '');
      rows += '<tr><td class="' + tag + '">' + t + '</td><td>' + Rtext(one) + '</td><td>' + Rtext(both)
        + '</td><td>' + Rfixed(both, 6) + '</td><td>'
        + (t === d ? 'the hedge goes out here' : (hedged99 !== null && t === hedged99 ? 'hedged p99' : ''))
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>t (ms)</th><th>P(X &gt; t)</th><th>P(hedged &gt; t)</th>'
      + '<th>decimal</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var hi = grid[grid.length - 1] || 1;
    function px(t) { return 12 + (t / hi) * 496; }
    function py(prob) { return 142 - parseFloat(Rfixed(prob, 9)) * 118; }
    var onePts = [], bothPts = [];
    for (i = 0; i < grid.length; i += 1) {
      onePts.push(px(grid[i]) + ',' + py(pmfTail(pmf, grid[i])));
      bothPts.push(px(grid[i]) + ',' + py(hedgedTail(pmf, d, grid[i])));
    }
    var s = '<polyline points="' + onePts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<polyline points="' + bothPts.join(' ') + '" fill="none" stroke="var(--green)" stroke-width="2.5" />'
      + '<line x1="' + px(d) + '" y1="18" x2="' + px(d) + '" y2="142" stroke="var(--amber)" stroke-width="2" '
      + 'stroke-dasharray="5 4" />'
      + '<text x="' + Math.min(px(d) + 5, 380) + '" y="32" font-size="10" fill="var(--amber)" font-weight="700">'
      + 'hedge at ' + d + ' ms</text>'
      + '<line x1="12" y1="' + py(R(1n, 100n)) + '" x2="508" y2="' + py(R(1n, 100n)) + '" stroke="var(--purple)" '
      + 'stroke-width="1" stroke-dasharray="3 3" />'
      + '<text x="12" y="' + (py(R(1n, 100n)) - 4) + '" font-size="9" fill="var(--purple)">1% &mdash; where the p99 is read off</text>'
      + '<line x1="12" y1="142" x2="508" y2="142" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="12" y="160" font-size="10" fill="var(--muted)">0 ms</text>'
      + '<text x="508" y="160" text-anchor="end" font-size="10" fill="var(--muted)">' + hi + ' ms</text>'
      + '<text x="12" y="176" font-size="10" fill="var(--muted)">vertical axis: the probability a request is '
      + 'still running at t</text>';
    plot.innerHTML = s;

    var saved = hedged99 === null ? null : base99 - hedged99;
    status.innerHTML = 'A backup sent at <strong>' + d + ' ms</strong> goes out for the <strong>'
      + Rpct(tailAtD, 2) + '</strong> of requests still running then &mdash; that is the extra load, exactly. '
      + 'Past the delay the request needs BOTH copies to be slow, so the tail there is '
      + Rtext(tailAtD) + '&sup2; = <strong>' + Rtext(squared) + '</strong> ('
      + Rpct(squared, 4) + '). '
      + (hedged99 === null
          ? ''
          : 'The p99 falls from <strong>' + base99 + ' ms</strong> to <strong>' + hedged99 + ' ms</strong>'
            + (saved > 0 ? ', a saving of ' + saved + ' ms for ' + Rpct(tailAtD, 1) + ' more traffic. ' : '. '))
      + 'The median is unmoved at ' + base50 + ' ms' + (hedged50 === base50 ? '' : ' (hedged: ' + hedged50 + ' ms)')
      + ' &mdash; hedging buys nothing for the ordinary request and everything for the unlucky one. '
      + '<span class="tone-muted">Independence is the assumption doing the work here: if the first copy is slow '
      + 'because the server is slow, the backup goes to the same slow server and p&sup2; is a fiction.</span>';
  }

  specIn.addEventListener('input', redraw);
  dS.addEventListener('input', redraw);
  specIn.value = """ + _js_string(spec) + r""";
  dS.value = """ + str(delay) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A backup request, and what it costs",
        subtitle="The tail squared past the hedge delay, bought with the tail in extra load",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the hedge delay"),
        panel_intro=cfg.get(
            "panel_intro",
            "The hedged survival curve is P(X &gt; t) &times; P(X &gt; t &minus; d), computed "
            "exactly at every time the curve can change.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - convolve
# ---------------------------------------------------------------------------

_CONV_A = "4:520, 6:250, 9:120, 14:60, 22:30, 38:16, 70:4"
_CONV_B = "12:420, 17:300, 24:150, 34:80, 48:36, 72:12, 130:2"


def _convolve(cfg):
    spec_a = str(cfg.get("stage_a", _CONV_A))
    spec_b = str(cfg.get("stage_b", _CONV_B))

    markup = (
        _toolbar(
            "Percentiles do not add",
            "the sum's distribution is the convolution, and its p99 is not the sum of the p99s",
            [("cyan", "the sum's pmf"), ("green", "true p99 of A + B"), ("red", "p99(A) + p99(B)")],
        )
        + _stage(_svg("cvPlot", "0 0 520 180", "The convolved distribution drawn as bars, with both p99s marked."))
        + _table("cvTable")
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="cvAtoms"></table></div>\n'
        + _banner("cvStatus")
    )
    controls = (
        _text("cvA", "Stage A, as ms:weight pairs", spec_a)
        + _text("cvB", "Stage B, as ms:weight pairs", spec_b)
        + _kpis(
            [
                ("p99(A) + p99(B)", "cvNaive"),
                ("p99(A + B), exactly", "cvTrue"),
                ("The naive sum overstates by", "cvGap"),
                ("Means, which do add", "cvMeans"),
            ]
        )
        + _hint(
            "cvHint",
            "The convolution enumerates every pair of outcomes and multiplies their probabilities, "
            "so the sum's distribution is exact. Adding the two p99s assumes both stages are having "
            "their bad day at the same time, and independent stages almost never are.",
        )
    )

    script = _CORE_JS + r"""
  var aIn = document.getElementById('cvA'), bIn = document.getElementById('cvB');
  var plot = document.getElementById('cvPlot'), table = document.getElementById('cvTable');
  var atoms = document.getElementById('cvAtoms'), status = document.getElementById('cvStatus');
  var KPIS = ['cvNaive', 'cvTrue', 'cvGap', 'cvMeans'];

  function redraw() {
    var sa = parsePmfSpec(aIn.value), sb = parsePmfSpec(bIn.value);
    var A = sa ? pmfFromSpec(sa) : null, B = sb ? pmfFromSpec(sb) : null;
    if (!A || !B) {
      plot.innerHTML = '';
      table.innerHTML = '';
      atoms.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">One of the two stages did not parse.</span> Each is a list of '
        + 'ms:weight pairs, like <span class="tone-muted">4:520, 6:250, 9:120</span>.';
      return;
    }

    var S = pmfNormalise(pmfConvolve(A, B));
    var q50 = R(1n, 2n), q95 = R(95n, 100n), q99 = R(99n, 100n);
    var a99 = pmfPercentile(A, q99), b99 = pmfPercentile(B, q99), s99 = pmfPercentile(S, q99);
    var a95 = pmfPercentile(A, q95), b95 = pmfPercentile(B, q95), s95 = pmfPercentile(S, q95);
    var a50 = pmfPercentile(A, q50), b50 = pmfPercentile(B, q50), s50 = pmfPercentile(S, q50);
    var naive = a99 + b99;
    var mA = pmfMean(A), mB = pmfMean(B), mS = pmfMean(S);

    document.getElementById('cvNaive').textContent = a99 + ' + ' + b99 + ' = ' + naive + ' ms';
    document.getElementById('cvTrue').textContent = s99 + ' ms';
    document.getElementById('cvGap').textContent = (naive - s99) + ' ms ('
      + Rpct(Rdiv(R(BigInt(naive - s99), 1n), R(BigInt(s99 || 1), 1n)), 1) + ')';
    document.getElementById('cvMeans').textContent = Rtext(mA) + ' + ' + Rtext(mB) + ' = ' + Rtext(mS);

    table.innerHTML = '<thead><tr><th></th><th>p50</th><th>p95</th><th>p99</th><th>mean</th></tr></thead><tbody>'
      + '<tr><td>stage A</td><td>' + a50 + '</td><td>' + a95 + '</td><td>' + a99 + '</td><td>' + Rtext(mA) + '</td></tr>'
      + '<tr><td>stage B</td><td>' + b50 + '</td><td>' + b95 + '</td><td>' + b99 + '</td><td>' + Rtext(mB) + '</td></tr>'
      + '<tr><td class="tone-red">A + B, added naively</td><td>' + (a50 + b50) + '</td><td>' + (a95 + b95)
      + '</td><td>' + naive + '</td><td>' + Rtext(Radd(mA, mB)) + '</td></tr>'
      + '<tr><td class="tone-green">A + B, by convolution</td><td>' + s50 + '</td><td>' + s95 + '</td><td>'
      + s99 + '</td><td>' + Rtext(mS) + '</td></tr></tbody>';

    /* The rows around the crossing: where the cumulative probability of the
       sum first reaches 99/100, and what the naive answer would have claimed. */
    var cum = R(0n, 1n), rows = '', i, hitAt = -1;
    var cums = [];
    for (i = 0; i < S.length; i += 1) { cum = Radd(cum, S[i][1]); cums.push(cum); if (hitAt < 0 && Rcmp(cum, q99) >= 0) hitAt = i; }
    var from = Math.max(0, hitAt - 4), to = Math.min(S.length - 1, hitAt + 3);
    for (i = from; i <= to; i += 1) {
      var tag = i === hitAt ? 'tone-green' : '';
      rows += '<tr><td class="' + tag + '">' + S[i][0] + '</td><td>' + Rtext(S[i][1]) + '</td><td>'
        + Rtext(cums[i]) + '</td><td>' + Rfixed(cums[i], 6) + '</td><td>'
        + (i === hitAt ? 'first to reach 99/100' : '') + '</td></tr>';
    }
    atoms.innerHTML = '<thead><tr><th>A + B (ms)</th><th>probability</th><th>cumulative</th>'
      + '<th>decimal</th><th></th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">' + S.length + ' distinct sums from '
      + A.length + ' &times; ' + B.length + ' pairs, every probability an exact fraction.</td></tr></tfoot>';

    var hi = Math.max(S[S.length - 1][0], naive) || 1;
    var maxP = 0;
    for (i = 0; i < S.length; i += 1) { var v = parseFloat(Rfixed(S[i][1], 9)); if (v > maxP) maxP = v; }
    if (!maxP) maxP = 1;
    function px(t) { return 12 + (t / hi) * 496; }
    var s = '';
    for (i = 0; i < S.length; i += 1) {
      var h = (parseFloat(Rfixed(S[i][1], 9)) / maxP) * 110;
      s += '<rect x="' + (px(S[i][0]) - 1.5) + '" y="' + (140 - h) + '" width="3" height="' + Math.max(1, h)
        + '" rx="1" fill="var(--cyan)" opacity="0.85" />';
    }
    s += '<line x1="' + px(s99) + '" y1="18" x2="' + px(s99) + '" y2="140" stroke="var(--green)" stroke-width="2.5" />'
      + '<text x="' + Math.max(12, Math.min(px(s99) - 4, 300)) + '" y="32" font-size="10" fill="var(--green)" '
      + 'font-weight="700">p99(A + B) = ' + s99 + ' ms</text>'
      + '<line x1="' + px(naive) + '" y1="18" x2="' + px(naive) + '" y2="140" stroke="var(--red)" stroke-width="2.5" '
      + 'stroke-dasharray="5 4" />'
      + '<text x="' + Math.min(px(naive) + 5, 330) + '" y="52" font-size="10" fill="var(--red)" font-weight="700">'
      + 'p99(A) + p99(B) = ' + naive + ' ms</text>'
      + '<line x1="12" y1="140" x2="508" y2="140" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="12" y="158" font-size="10" fill="var(--muted)">0 ms</text>'
      + '<text x="508" y="158" text-anchor="end" font-size="10" fill="var(--muted)">' + hi + ' ms</text>'
      + '<text x="12" y="174" font-size="10" fill="var(--muted)">each bar is one attainable total, at its exact '
      + 'probability</text>';
    plot.innerHTML = s;

    var both = Rmul(pmfTail(A, a99 - 1), pmfTail(B, b99 - 1));
    var verdict;
    if (s99 < naive) {
      verdict = 'The true p99 of the two stages together is <strong>' + s99 + ' ms</strong>, while adding the '
        + 'stage p99s gives <span class="tone-red">' + naive + ' ms</span> &mdash; an overstatement of '
        + (naive - s99) + ' ms. Adding them assumes both stages are at their p99 in the same request, which '
        + 'happens with probability ' + Rtext(both) + ' = ' + Rpct(both, 4) + '.';
    } else if (s99 > naive) {
      verdict = '<span class="tone-amber">On these two distributions the sum\'s p99 (' + s99 + ' ms) is ABOVE the '
        + 'sum of the p99s (' + naive + ' ms).</span> That happens when the mass past each stage\'s p99 sits far '
        + 'out: a single rare spike carries the pair over the line on its own. The lesson is not that the naive '
        + 'sum is always too big &mdash; it is that it is not the p99 of anything.';
    } else {
      verdict = 'Here the two happen to coincide at ' + s99 + ' ms. They are still different quantities: one is '
        + 'a percentile of the sum, the other a sum of percentiles.';
    }
    status.innerHTML = verdict + ' The means, by contrast, add exactly: ' + Rtext(mA) + ' + ' + Rtext(mB)
      + ' = <strong>' + Rtext(mS) + '</strong>' + (Requ(Radd(mA, mB), mS) ? '' : ' (they disagree, which would be a bug)')
      + ' &mdash; expectation is linear and percentiles are not, and that is the whole difference.';
  }

  [aIn, bIn].forEach(function (el) { el.addEventListener('input', redraw); });
  aIn.value = """ + _js_string(spec_a) + r""";
  bIn.value = """ + _js_string(spec_b) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two stages in series",
        subtitle="The sum by convolution, beside the sum of the p99s that is not it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the two stages"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every pair of outcomes is enumerated and its probability multiplied out, so the "
            "distribution of the total is exact and so is its p99.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 - budget
# ---------------------------------------------------------------------------

_BUDGET_STAGES = [("gateway", "bgS0", 8), ("auth", "bgS1", 20), ("search", "bgS2", 150), ("render", "bgS3", 40)]


def _budget(cfg):
    slo = int(cfg.get("slo", 400))
    light = int(cfg.get("light_floor", 56))
    handshake = int(cfg.get("handshake", 152))
    floors = [int(cfg.get(cid, default)) for _n, cid, default in _BUDGET_STAGES]

    markup = (
        _toolbar(
            "A latency budget, allocated backwards",
            "the SLO, minus what physics takes, split across the stages that are left",
            [("muted", "fixed floors"), ("cyan", "fits its share"), ("red", "does not fit")],
        )
        + _stage(_svg("bgPlot", "0 0 520 170", "The budget drawn as a bar, with the fixed floors and each stage's share."))
        + _table("bgTable")
        + _banner("bgStatus")
    )
    controls = (
        _range("bgSlo", "SLO, as a p99 (ms)", 50, 1500, slo)
        + _range("bgLight", "Light-speed floor from L2 (ms)", 0, 400, light)
        + _range("bgHand", "Handshake round trips from L3 (ms)", 0, 600, handshake)
        + "".join(
            _range(cid, "%s floor (ms)" % name, 1, 400, value)
            for (name, cid, _d), value in zip(_BUDGET_STAGES, floors)
        )
        + _kpis(
            [
                ("Left for the code", "bgAvail"),
                ("Even share per stage", "bgShare"),
                ("Residual overall", "bgResidual"),
                ("Stages that do not fit", "bgFail"),
            ]
        )
        + _hint(
            "bgHint",
            "Subtract the floors first: they are not negotiable and no amount of profiling removes "
            "them. What is left is the only part the code is allowed to spend, and an even split of "
            "it is the first thing to try &mdash; not because it is right, but because it shows you "
            "immediately which stage the budget cannot hold.",
        )
    )

    script = (
        _CORE_JS
        + cfg_literal("BUDGET_NAMES", [name for name, _c, _d in _BUDGET_STAGES])
        + r"""
  var sloS = document.getElementById('bgSlo'), lightS = document.getElementById('bgLight'), handS = document.getElementById('bgHand');
  var STAGE_S = ['bgS0', 'bgS1', 'bgS2', 'bgS3'].map(function (id) { return document.getElementById(id); });
  var plot = document.getElementById('bgPlot'), table = document.getElementById('bgTable');
  var status = document.getElementById('bgStatus');

  function redraw() {
    var slo = +sloS.value, light = +lightS.value, hand = +handS.value, i;
    var floors = STAGE_S.map(function (el) { return +el.value; });
    document.getElementById('bgSloOut').textContent = slo + ' ms';
    document.getElementById('bgLightOut').textContent = light + ' ms';
    document.getElementById('bgHandOut').textContent = hand + ' ms';
    for (i = 0; i < STAGE_S.length; i += 1) {
      document.getElementById(STAGE_S[i].id + 'Out').textContent = floors[i] + ' ms';
    }

    var fixed = light + hand;
    var plan = budgetPlan(slo, fixed, floors);
    var zero = R(0n, 1n);
    var failing = [];
    for (i = 0; i < plan.rows.length; i += 1) if (!plan.rows[i].fits) failing.push(BUDGET_NAMES[i]);

    document.getElementById('bgAvail').textContent = Rfixed(plan.avail, 1) + ' ms of ' + slo;
    document.getElementById('bgShare').textContent = Rtext(plan.share) + ' = ' + Rfixed(plan.share, 2) + ' ms';
    document.getElementById('bgResidual').textContent = Rfixed(plan.residual, 2) + ' ms';
    document.getElementById('bgFail').textContent = failing.length ? failing.join(', ') : 'none';

    var rows = '<tr><td class="tone-muted">light-speed floor (L2)</td><td>' + light
      + '</td><td>fixed</td><td>&mdash;</td><td>cannot be spent</td></tr>'
      + '<tr><td class="tone-muted">handshake round trips (L3)</td><td>' + hand
      + '</td><td>fixed</td><td>&mdash;</td><td>cannot be spent</td></tr>';
    for (i = 0; i < plan.rows.length; i += 1) {
      var r = plan.rows[i];
      rows += '<tr><td class="' + (r.fits ? 'tone-cyan' : 'tone-red') + '">' + BUDGET_NAMES[i] + '</td><td>'
        + floors[i] + '</td><td>' + Rfixed(r.share, 2) + '</td><td>' + Rfixed(r.residual, 2) + '</td><td>'
        + (r.fits ? 'fits, with ' + Rfixed(r.residual, 1) + ' ms spare' : 'short by ' + Rfixed(Rsub(zero, r.residual), 1) + ' ms')
        + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>item</th><th>floor (ms)</th><th>even share</th><th>residual</th>'
      + '<th></th></tr></thead><tbody>' + rows + '</tbody>';

    var total = Math.max(slo, fixed + floors.reduce(function (a, b) { return a + b; }, 0)) || 1;
    var unit = 496 / total, x = 12, s = '';
    s += '<rect x="' + x + '" y="34" width="' + (light * unit) + '" height="30" fill="var(--muted)" opacity="0.55" />';
    x += light * unit;
    s += '<rect x="' + x + '" y="34" width="' + (hand * unit) + '" height="30" fill="var(--muted)" opacity="0.35" />';
    x += hand * unit;
    for (i = 0; i < floors.length; i += 1) {
      var w = floors[i] * unit;
      s += '<rect x="' + x + '" y="34" width="' + Math.max(1, w - 1) + '" height="30" rx="2" fill="'
        + (plan.rows[i].fits ? 'var(--cyan)' : 'var(--red)') + '" opacity="0.85" />';
      if (w > 40) s += '<text x="' + (x + w / 2) + '" y="54" text-anchor="middle" font-size="9" fill="var(--bg)">'
        + BUDGET_NAMES[i] + '</text>';
      x += w;
    }
    var sx = 12 + slo * unit;
    s += '<line x1="' + sx + '" y1="20" x2="' + sx + '" y2="86" stroke="var(--amber)" stroke-width="2.5" />'
      + '<text x="' + Math.max(12, Math.min(sx - 60, 390)) + '" y="16" font-size="10" fill="var(--amber)" '
      + 'font-weight="700">SLO = ' + slo + ' ms</text>'
      + '<text x="12" y="104" font-size="10" fill="var(--muted)">grey: the floors from lessons 2 and 3. '
      + 'The bar past the amber line is the part that does not fit.</text>'
      + '<text x="12" y="126" font-size="10" fill="var(--muted)">even share of what is left: '
      + Rfixed(plan.share, 2) + ' ms per stage</text>'
      + '<text x="12" y="148" font-size="10" fill="var(--muted)">residual: ' + Rfixed(plan.residual, 2)
      + ' ms &mdash; surplus ' + Rfixed(plan.spare, 2) + ' ms minus shortfall ' + Rfixed(plan.need, 2) + ' ms'
      + (plan.balanced ? ', and the two agree' : ', WHICH DO NOT AGREE') + '</text>';
    plot.innerHTML = s;

    var over = Rcmp(plan.residual, zero) < 0;
    status.innerHTML = 'The SLO is ' + slo + ' ms and ' + fixed + ' ms of it is gone before any code runs, '
      + 'leaving <strong>' + Rfixed(plan.avail, 1) + ' ms</strong> for ' + plan.rows.length + ' stages &mdash; '
      + '<strong>' + Rfixed(plan.share, 2) + ' ms</strong> each on an even split. '
      + (failing.length
          ? '<span class="tone-red">' + failing.join(' and ') + ' cannot fit</span>: the floor'
            + (failing.length > 1 ? 's are' : ' is') + ' above that share by ' + Rfixed(plan.need, 1) + ' ms in total, '
            + 'while the other stages release only ' + Rfixed(plan.spare, 1) + ' ms. '
          : 'Every stage fits its share, with ' + Rfixed(plan.spare, 1) + ' ms of surplus across them. ')
      + (over
          ? 'The budget is <span class="tone-red">' + Rfixed(Rsub(zero, plan.residual), 1) + ' ms short</span> '
            + 'whatever you do with the allocation: either the SLO moves, a floor comes down, or a stage leaves '
            + 'the critical path. '
          : 'The whole plan fits with ' + Rfixed(plan.residual, 1) + ' ms of headroom left over. ')
      + '<span class="tone-muted">And note the unit: this is a budget of p99s, so the stage figures have to be '
      + 'p99s too. Budgeting in means and reporting in percentiles is how a plan that adds up delivers an SLO '
      + 'that does not.</span>';
  }

  [sloS, lightS, handS].forEach(function (el) { el.addEventListener('input', redraw); });
  STAGE_S.forEach(function (el) { el.addEventListener('input', redraw); });
  sloS.value = """ + str(slo) + r"""; lightS.value = """ + str(light) + r"""; handS.value = """ + str(handshake) + r""";
""" + "".join(
            "  document.getElementById('%s').value = %d;\n" % (cid, value)
            for (_n, cid, _d), value in zip(_BUDGET_STAGES, floors)
        ) + r"""  redraw();
  window.redrawLab = redraw;
"""
    )
    return Lab(
        title="What the SLO leaves the code",
        subtitle="Floors first, then the residual, then the stage that does not fit in it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the SLO and the floors"),
        panel_intro=cfg.get(
            "panel_intro",
            "The residual is computed twice &mdash; as the budget minus the floors, and as the "
            "surplus minus the shortfall &mdash; and the page says whether they agree.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 - timeout
# ---------------------------------------------------------------------------

_TIMEOUT_SPEC = "8:45, 11:25, 16:15, 24:8, 45:4, 90:2, 400:1"


def _timeout(cfg):
    spec = str(cfg.get("spec", _TIMEOUT_SPEC))
    timeout = int(cfg.get("timeout", 90))
    retries = int(cfg.get("retries", 1))
    budget = int(cfg.get("budget", 250))

    markup = (
        _toolbar(
            "Timeouts and retries inside the budget",
            "(r + 1) &times; T against the budget, and the good calls T throws away",
            [("cyan", "completes in time"), ("red", "killed by the timeout"), ("amber", "the budget")],
        )
        + _stage(_svg("toPlot", "0 0 520 180", "The measured distribution with the timeout cut, and the worst case against the budget."))
        + _table("toTable")
        + _banner("toStatus")
    )
    controls = (
        _text("toSpec", "Measured call latency, as ms:count pairs", spec)
        + _range("toT", "Timeout T (ms)", 1, 420, timeout)
        + _range("toR", "Retries r", 0, 5, retries)
        + _range("toBudget", "Budget for this call (ms)", 20, 1200, budget)
        + _kpis(
            [
                ("Worst case (r + 1) &times; T", "toWorst"),
                ("Good calls killed, 1 &minus; F(T)", "toKill"),
                ("P(every attempt times out)", "toLost"),
                ("Fits the budget?", "toFits"),
            ]
        )
        + _hint(
            "toHint",
            "A timeout is a decision to give up on a call that would have succeeded. Set at the "
            "mean it discards the whole upper half of the distribution; set past the p99 it "
            "discards almost nothing but leaves a worst case the budget may not be able to hold.",
        )
    )

    script = _CORE_JS + r"""
  var specIn = document.getElementById('toSpec'), tS = document.getElementById('toT');
  var rS = document.getElementById('toR'), budgetS = document.getElementById('toBudget');
  var plot = document.getElementById('toPlot'), table = document.getElementById('toTable');
  var status = document.getElementById('toStatus');
  var KPIS = ['toWorst', 'toKill', 'toLost', 'toFits'];

  function redraw() {
    var T = +tS.value, r = +rS.value, budget = +budgetS.value;
    document.getElementById('toTOut').textContent = T + ' ms';
    document.getElementById('toROut').textContent = r + (r === 1 ? ' retry' : ' retries');
    document.getElementById('toBudgetOut').textContent = budget + ' ms';

    var spec = parsePmfSpec(specIn.value);
    if (!spec) {
      plot.innerHTML = '';
      table.innerHTML = '';
      KPIS.forEach(function (id) { document.getElementById(id).textContent = '—'; });
      status.innerHTML = '<span class="tone-red">That distribution did not parse.</span> Write it as '
        + 'ms:count pairs, like <span class="tone-muted">8:45, 11:25, 400:1</span>.';
      return;
    }
    var sorted = expandSpec(spec), n = sorted.length;
    var worst = worstCaseMs(T, r);
    var killed = killFraction(sorted, T);
    var lost = allAttemptsLost(killed, r);
    var fits = Rcmp(worst, R(BigInt(budget), 1n)) <= 0;
    var mean = sampleMean(sorted);
    var p50 = percentile(sorted, R(1n, 2n));
    var p99 = percentile(sorted, R(99n, 100n));

    document.getElementById('toWorst').textContent = (r + 1) + ' × ' + T + ' = ' + Rfixed(worst, 0) + ' ms';
    document.getElementById('toKill').textContent = Rtext(killed) + ' = ' + Rpct(killed, 2);
    document.getElementById('toLost').textContent = Rtext(lost) + ' = ' + Rpct(lost, 4);
    document.getElementById('toFits').textContent = fits ? 'yes, by ' + Rfixed(Rsub(R(BigInt(budget), 1n), worst), 0) + ' ms'
      : 'no, over by ' + Rfixed(Rsub(worst, R(BigInt(budget), 1n)), 0) + ' ms';

    var marks = [], i;
    var meanMs = Math.round(parseFloat(Rfixed(mean, 0)));
    [['the mean', meanMs], ['the median (p50)', p50], ['the p99', p99], ['your timeout', T]].forEach(function (m) {
      marks.push(m);
    });
    var rows = '';
    for (i = 0; i < marks.length; i += 1) {
      var at = marks[i][1], k = killFraction(sorted, at);
      rows += '<tr><td class="' + (marks[i][0] === 'your timeout' ? 'tone-amber' : '') + '">' + marks[i][0]
        + '</td><td>' + at + '</td><td>' + Rtext(k) + '</td><td>' + Rpct(k, 2) + '</td><td>'
        + Rfixed(worstCaseMs(at, r), 0) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>timeout set at</th><th>ms</th><th>good calls killed</th>'
      + '<th>as a percentage</th><th>worst case at r = ' + r + '</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">' + n + ' measured calls; every fraction is a count '
      + 'over ' + n + '.</td></tr></tfoot>';

    var hi = Math.max(sorted[n - 1], budget, parseFloat(Rfixed(worst, 0))) || 1;
    function px(t) { return 12 + (t / hi) * 496; }
    var s = '';
    for (i = 0; i < n; i += 1) {
      s += '<line x1="' + px(sorted[i]) + '" y1="34" x2="' + px(sorted[i]) + '" y2="62" stroke="'
        + (sorted[i] > T ? 'var(--red)' : 'var(--cyan)') + '" stroke-width="1.6" opacity="0.6" />';
    }
    s += '<text x="12" y="24" font-size="11" fill="var(--muted)">' + n + ' calls; red ones the timeout would kill</text>'
      + '<line x1="' + px(T) + '" y1="28" x2="' + px(T) + '" y2="70" stroke="var(--amber)" stroke-width="2.5" />'
      + '<text x="' + Math.min(px(T) + 5, 410) + '" y="80" font-size="10" fill="var(--amber)" font-weight="700">'
      + 'T = ' + T + ' ms</text>'
      + '<text x="12" y="112" font-size="11" fill="var(--muted)">worst case: ' + (r + 1) + ' attempts back to back</text>';
    var x = 12;
    for (i = 0; i <= r; i += 1) {
      var w = (T / hi) * 496;
      s += '<rect x="' + x + '" y="120" width="' + Math.max(1, w - 2) + '" height="24" rx="3" fill="var(--red)" '
        + 'opacity="' + (0.45 + 0.12 * i) + '" />';
      x += w;
    }
    var bx = px(budget);
    s += '<line x1="' + bx + '" y1="112" x2="' + bx + '" y2="152" stroke="var(--amber)" stroke-width="2.5" '
      + 'stroke-dasharray="5 4" />'
      + '<text x="' + Math.max(12, Math.min(bx + 5, 380)) + '" y="166" font-size="10" fill="var(--amber)">budget '
      + budget + ' ms</text>'
      + '<text x="12" y="166" font-size="10" fill="' + (fits ? 'var(--cyan)' : 'var(--red)') + '">'
      + Rfixed(worst, 0) + ' ms of attempts</text>';
    plot.innerHTML = s;

    status.innerHTML = 'A timeout of <strong>' + T + ' ms</strong> with ' + r + ' '
      + (r === 1 ? 'retry' : 'retries') + ' has a worst case of <strong>' + Rfixed(worst, 0)
      + ' ms</strong>, which ' + (fits ? 'fits the ' + budget + ' ms budget' : '<span class="tone-red">does not fit '
        + 'the ' + budget + ' ms budget</span>') + '. It kills <strong>' + Rtext(killed) + '</strong> of calls ('
      + Rpct(killed, 2) + ') that would otherwise have finished, and all ' + (r + 1) + ' attempts fail together '
      + 'with probability ' + Rtext(killed) + '<sup>' + (r + 1) + '</sup> = ' + Rpct(lost, 4) + '. '
      + '<span class="tone-muted">Set at the mean instead &mdash; ' + Rfixed(mean, 2) + ' ms, so ' + meanMs
      + ' ms &mdash; it would kill '
      + Rpct(killFraction(sorted, meanMs), 1) + ' of good calls</span> &mdash; the mean sits above most of this '
      + 'distribution and below all of its tail, which is exactly the wrong place for a cut-off.';
  }

  specIn.addEventListener('input', redraw);
  [tS, rS, budgetS].forEach(function (el) { el.addEventListener('input', redraw); });
  specIn.value = """ + _js_string(spec) + r""";
  tS.value = """ + str(timeout) + r"""; rS.value = """ + str(retries) + r"""; budgetS.value = """ + str(budget) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Choosing a timeout that fits",
        subtitle="The worst case against the budget, and the good calls the cut-off discards",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the timeout and the retries"),
        panel_intro=cfg.get(
            "panel_intro",
            "The killed fraction is 1 &minus; F(T) counted off the measured calls, and the worst "
            "case is every attempt taking the full timeout.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L11 - mathis
# ---------------------------------------------------------------------------


def _mathis(cfg):
    mss = int(cfg.get("mss", 1460))
    rtt = int(cfg.get("rtt", 100))
    loss_tenths = int(cfg.get("loss_tenths", 10))
    link = int(cfg.get("link_mbits", 10000))

    markup = (
        _toolbar(
            "The loss-limited bound on one flow",
            "(MSS &divide; RTT) &times; 1 &divide; &radic;p &mdash; the one rounded figure on this course",
            [("cyan", "one flow"), ("amber", "the link"), ("red", "rounded, not exact")],
        )
        + _stage(_svg("mtPlot", "0 0 520 180", "The bound plotted against the loss rate, with the link capacity for comparison."))
        + _table("mtTable")
        + _banner("mtStatus")
    )
    controls = (
        _range("mtMss", "MSS (bytes)", 200, 9000, mss)
        + _range("mtRtt", "Round-trip time (ms)", 1, 400, rtt)
        + _range("mtLoss", "Loss rate (tenths of a percent)", 1, 200, loss_tenths)
        + _range("mtLink", "Link capacity (Mbit/s)", 10, 40000, link, 10)
        + _kpis(
            [
                ("Bound on one flow", "mtFlow"),
                ("Link capacity", "mtLink2"),
                ("Streams to fill the link", "mtStreams"),
                ("1 &divide; &radic;p", "mtRoot"),
            ]
        )
        + _hint(
            "mtHint",
            "Loss enters as an inverse square root, so the bound is the one figure in this course "
            "computed in floating point: Rsqrt returns null for a rate that is not a perfect "
            "square, and sqrtApprox rounds by Newton's method instead. Every figure on this panel "
            "inherits that rounding, and no other page on the course does.",
        )
    )

    script = _CORE_JS + r"""
  var mssS = document.getElementById('mtMss'), rttS = document.getElementById('mtRtt');
  var lossS = document.getElementById('mtLoss'), linkS = document.getElementById('mtLink');
  var plot = document.getElementById('mtPlot'), table = document.getElementById('mtTable');
  var status = document.getElementById('mtStatus');

  function lossRational(tenths) { return R(BigInt(tenths), 1000n); }

  function redraw() {
    var mss = +mssS.value, rtt = +rttS.value, tenths = +lossS.value, link = +linkS.value;
    var loss = lossRational(tenths);
    document.getElementById('mtMssOut').textContent = mss + ' B';
    document.getElementById('mtRttOut').textContent = rtt + ' ms';
    document.getElementById('mtLossOut').textContent = Rfixed(Rmul(loss, R(100n, 1n)), 1) + '%';
    document.getElementById('mtLinkOut').textContent = link >= 1000 ? (link / 1000) + ' Gbit/s' : link + ' Mbit/s';

    var flow = mathisMbitsApprox(mss, rtt, loss);
    var streams = streamsToFillApprox(link, flow);
    var root = sqrtApprox(loss, 1e-15);
    var exact = Rsqrt(loss);

    document.getElementById('mtFlow').textContent = flow.toFixed(3) + ' Mbit/s';
    document.getElementById('mtLink2').textContent = (link >= 1000 ? (link / 1000) + ' Gbit/s' : link + ' Mbit/s');
    document.getElementById('mtStreams').textContent = streams ? commas(streams) : '—';
    document.getElementById('mtRoot').textContent = (1 / root).toFixed(6);

    var rows = '', sweep = [1, 2, 5, 10, 20, 50, 100], i;
    if (sweep.indexOf(tenths) < 0) { sweep.push(tenths); sweep.sort(function (a, b) { return a - b; }); }
    for (i = 0; i < sweep.length; i += 1) {
      var p = lossRational(sweep[i]), f = mathisMbitsApprox(mss, rtt, p);
      rows += '<tr><td class="' + (sweep[i] === tenths ? 'tone-amber' : '') + '">'
        + Rfixed(Rmul(p, R(100n, 1n)), 1) + '%</td><td>' + Rtext(p) + '</td><td>'
        + (1 / sqrtApprox(p, 1e-15)).toFixed(3) + '</td><td>' + f.toFixed(3) + '</td><td>'
        + commas(streamsToFillApprox(link, f)) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>loss p</th><th>exactly</th><th>1/&radic;p (rounded)</th>'
      + '<th>Mbit/s per flow</th><th>streams to fill the link</th></tr></thead><tbody>' + rows + '</tbody>'
      + '<tfoot><tr><td colspan="5" class="small-copy">Column three is rounded by sqrtApprox, Newton\'s method '
      + 'to a tolerance of 10<sup>&minus;15</sup>; columns four and five inherit that rounding. Column two is '
      + 'exact, and is all that survives of exactness on this page.</td></tr></tfoot>';

    var pts = [], j, maxF = mathisMbitsApprox(mss, rtt, lossRational(1));
    for (j = 0; j < 60; j += 1) {
      var t = 1 + j * (200 - 1) / 59;
      var f2 = mathisMbitsApprox(mss, rtt, R(BigInt(Math.round(t * 100)), 100000n));
      pts.push((12 + (t / 200) * 496) + ',' + (142 - Math.min(1, f2 / (maxF || 1)) * 118));
    }
    var lx = 12 + (tenths / 200) * 496;
    var linkY = 142 - Math.min(1, link / (maxF || 1)) * 118;
    var s = '<polyline points="' + pts.join(' ') + '" fill="none" stroke="var(--cyan)" stroke-width="2.5" />'
      + '<line x1="' + lx + '" y1="18" x2="' + lx + '" y2="142" stroke="var(--red)" stroke-width="2" />'
      + '<text x="' + Math.min(lx + 5, 280) + '" y="32" font-size="10" fill="var(--red)" font-weight="700">'
      + Rfixed(Rmul(loss, R(100n, 1n)), 1) + '% loss &rarr; ' + flow.toFixed(2) + ' Mbit/s</text>';
    if (link <= maxF) {
      s += '<line x1="12" y1="' + linkY + '" x2="508" y2="' + linkY + '" stroke="var(--amber)" stroke-width="1.5" '
        + 'stroke-dasharray="4 3" /><text x="12" y="' + (linkY - 4) + '" font-size="9" fill="var(--amber)">the link</text>';
    } else {
      s += '<text x="12" y="16" font-size="9" fill="var(--amber)">the link is off the top of this chart: '
        + (link / Math.max(flow, 0.0001)).toFixed(0) + '&times; one flow</text>';
    }
    s += '<line x1="12" y1="142" x2="508" y2="142" stroke="var(--line-strong)" stroke-width="1" />'
      + '<text x="12" y="160" font-size="10" fill="var(--muted)">0.1% loss</text>'
      + '<text x="508" y="160" text-anchor="end" font-size="10" fill="var(--muted)">20% loss</text>'
      + '<text x="12" y="176" font-size="10" fill="var(--muted)">vertical axis: the bound on a single flow, '
      + 'against its value at 0.1%</text>';
    plot.innerHTML = s;

    status.innerHTML = 'At ' + mss + '-byte segments, a ' + rtt + ' ms round trip and '
      + Rfixed(Rmul(loss, R(100n, 1n)), 1) + '% loss, one TCP flow is bounded by <strong>'
      + flow.toFixed(3) + ' Mbit/s</strong> &mdash; on a '
      + (link >= 1000 ? (link / 1000) + ' Gbit/s' : link + ' Mbit/s') + ' link, so filling it would take <strong>'
      + commas(streams) + '</strong> parallel streams. The link rate is not the flow rate and '
      + 'buying a faster link does not change this number; only the round trip and the loss do. '
      + '<span class="tone-red">This figure is rounded.</span> The bound divides by &radic;p, and '
      + (exact
          ? 'although p = ' + Rtext(loss) + ' happens to be an exact square here ('
            + Rtext(exact) + '), the value above is still computed by sqrtApprox, which rounds, so that every '
            + 'point on the curve is produced the same way.'
          : 'p = ' + Rtext(loss) + ' has no rational root &mdash; Rsqrt returns null for it &mdash; so sqrtApprox '
            + 'computes it by Newton\'s method to a tolerance of 10<sup>&minus;15</sup>.')
      + ' It is the only figure on this course that is not an exact fraction.';
  }

  [mssS, rttS, lossS, linkS].forEach(function (el) { el.addEventListener('input', redraw); });
  mssS.value = """ + str(mss) + r"""; rttS.value = """ + str(rtt) + r""";
  lossS.value = """ + str(loss_tenths) + r"""; linkS.value = """ + str(link) + r""";
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Packet loss and throughput",
        subtitle="One flow's ceiling, which the link rate has nothing to do with",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the path"),
        panel_intro=cfg.get(
            "panel_intro",
            "The bound is (MSS/RTT)(1/&radic;p). The square root is why this page rounds and says "
            "so; every other page in the course prints exact fractions.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "bdp": _bdp,
    "lightspeed": _lightspeed,
    "roundtrips": _roundtrips,
    "dag": _dag,
    "percentile": _percentile,
    "fanout": _fanout,
    "hedge": _hedge,
    "convolve": _convolve,
    "budget": _budget,
    "timeout": _timeout,
    "mathis": _mathis,
}

MODES = tuple(sorted(_MODES))


def latency_lab(cfg):
    """Course 2's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is deliberate and it is the contract, not defensiveness. A kit
    that quietly fell back to a default mode would render a finished-looking
    page carrying another lesson's widget, and nothing downstream would notice:
    the markup tests pass, labcheck passes, and the reader is shown the wrong
    lesson's arithmetic under the right lesson's title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "latency_lab: unknown mode %r; the eleven modes of course 2 are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["latency_lab", "LATENCY_JS", "MODES"]
