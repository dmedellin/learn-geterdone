"""Course 9, the queueing half: five modes over one cut equation.

This is the second of course 9's two kits. `markov` solves linear systems on a
transition matrix; this one draws a queue. They are separated for the reason
course 4's two kits are: the controls a reader needs to type a 5 by 5 matrix and
the controls they need to move an arrival rate are not the same controls, and a
single kit would have answered one question under the other's title.

THE ONE EQUATION. Cut the chain between n and n + 1. What crosses upward in the
long run must cross back down, so

    pi_n lambda_n  =  pi_{n+1} mu_{n+1}

and every queue on this course is that sentence with different rates.  M/M/1 is
lambda_n = lambda and mu_n = mu.  M/M/s is mu_n = min(n, s) mu, and Erlang C is
a READING of the resulting pi rather than a second formula.  M/M/1/K is the same
chain stopped at K, and balking is lambda_n falling with n.  `or_core.birthDeath`
is that one function and all five modes call it.

TWO ROUTES ON EVERY PAGE, AND THEY HAVE TO AGREE.

  * The cut equations give pi as a product of ratios, normalised.
  * `globalBalance` below builds the FULL balance system -- pi_n(lambda_n + mu_n)
    = pi_{n-1} lambda_{n-1} + pi_{n+1} mu_{n+1} for every state, with sum pi = 1
    replacing one dependent row -- and solves it by exact Gauss-Jordan over
    rationals. Nothing about it knows what a cut is.

  Both are exact, so `Requ` decides whether they agree: not a tolerance, an
  equality of fractions. The page prints the verdict. A cut argument that is
  merely a shortcut would show up here as a disagreement, and the reason to
  compute both is that "cutting the chain is legitimate" is precisely the step a
  reader is being asked to believe.

AND A THIRD, BORROWED. Where the System Design path already owns a closed form
for the same model, this kit calls THAT function rather than writing a second
one: `mm1`, `mm1k` and `erlangC` come from `sysdesign_core.QUEUE_JS`, which
`content/system_design/c3_queues` is built on. So the two Subjects cannot
disagree about M/M/1, and the pages say which function produced which column.

WHAT ROUNDS. One of this path's four irrational quantities is here: `e^(-lambda)`
in the Poisson limit, in mode `poisson`. It is `expNegApprox` from
`sysdesign_core.APPROX_JS` -- borrowed, not re-implemented, for the same reason
the closed forms are. That function is the reciprocal of a POSITIVE-term series
for e^x, so nothing cancels and the result is correct to a rounding of the
double; the page states the method, prints the exact binomial beside it, and
prints the difference between them. Everything else in this kit is exact
rational arithmetic, and a truncated chain's pi has denominators that outgrow a
double quickly: at lambda = 19/20, mu = 1 and sixty states the normaliser is
already hundreds of digits.

WHAT THIS KIT DOES NOT SAY. `birthDeath` truncates: the reader chooses how many
states, and the chain is finite. For a genuinely infinite queue that is an
approximation, and mode `mm1` prints the truncation error rather than hiding it
-- the exact tail mass above the last state, as a fraction, beside the closed
form for the untruncated chain. For M/M/1/K the truncation is not an
approximation at all; it is the model, which is mode `finite`'s point.

The five modes, one lesson each.

  cut       arbitrary rates, the cut equations one at a time, and the same pi
            recovered from the full balance system by elimination
  mm1       the constant-rate chain: pi_n, L, Lq, W, Wq, P(N > k), the
            truncation error, and the closed form beside it
  mms       s servers: Erlang C read out of the same pi, and what adding a
            server does at fixed offered load
  finite    a chain stopped at K, and a chain whose arrivals balk: blocking,
            the admitted rate, and the two different W values
  poisson   the arrival process itself: n Bernoulli opportunities exactly, and
            the Poisson limit, which is where this kit stops being exact
"""

import json

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .counting import BIGINT_JS
from .or_core import CHAIN_JS, ORFMT_JS
from .sysdesign_core import APPROX_JS, QUEUE_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no DOM: scripts/mathcheck.js
# extracts this block and calls every one of them, the renderer included.
# ---------------------------------------------------------------------------

BDKIT_JS = r"""
  /* ---------------------------------------------------- building the rates

     A birth-death chain on states 0..N is two lists: lam[n] for n = 0..N-1 is
     the arrival rate OUT OF state n, and mu[n] for n = 0..N-1 is the service
     rate out of state n+1. Every mode below produces those two lists and hands
     them to or_core's birthDeath, so there is one chain and five readings of
     it rather than five models. */
  function ratesConstant(lam, mu, N) {
    var a = [], b = [], n;
    for (n = 0; n < N; n += 1) { a.push(lam); b.push(mu); }
    return { lam: a, mu: b, kind: 'M/M/1', servers: 1 };
  }
  function ratesServers(lam, mu, s, N) {
    var a = [], b = [], n;
    for (n = 0; n < N; n += 1) {
      a.push(lam);
      b.push(Rmul(R(BigInt(Math.min(n + 1, s)), 1n), mu));
    }
    return { lam: a, mu: b, kind: 'M/M/' + s, servers: s };
  }
  /* Balking: an arrival joins a queue of length n with probability 1/(n + 1),
     so lam_n = lam/(n + 1). A state-dependent arrival rate is the one thing the
     closed forms cannot absorb, and it costs this kit nothing because the cut
     equation never assumed the rates were constant. */
  function ratesBalking(lam, mu, N) {
    var a = [], b = [], n;
    for (n = 0; n < N; n += 1) {
      a.push(Rdiv(lam, R(BigInt(n + 1), 1n)));
      b.push(mu);
    }
    return { lam: a, mu: b, kind: 'balking', servers: 1 };
  }
  /* Rates typed by a reader, one per state, for the mode that shows the cut
     equations on an arbitrary chain. */
  function readRates(text) {
    var parts = String(text).trim().split(/[\s,;]+/).filter(function (t) { return t.length; });
    var out = [], k;
    for (k = 0; k < parts.length; k += 1) {
      var v = Rread(parts[k]);
      if (v === null || Rsign(v) < 0) return null;
      out.push(v);
    }
    return out.length ? out : null;
  }

  /* ------------------------------------------- the second route to the same pi

     THE FULL BALANCE SYSTEM, which knows nothing about cuts. For every state n

         pi_n (lam_n + mu_n)  =  pi_{n-1} lam_{n-1} + pi_{n+1} mu_{n+1}

     with lam_N = 0 and mu_0 = 0. Those N + 1 equations are dependent, so one is
     dropped by name and sum pi = 1 takes its place -- exactly as steadyState
     does for a discrete chain, and for the same reason. Solved by Mrref over
     rationals, so the comparison with the cut answer is an equality of
     fractions and not a tolerance. */
  function globalBalance(lam, mu, dropIndex) {
    var N = lam.length, n, j;
    var states = N + 1;
    var drop = dropIndex === undefined ? states - 1 : dropIndex;
    var rows = [];
    for (n = 0; n < states; n += 1) {
      if (n === drop) continue;
      var row = [];
      for (j = 0; j < states; j += 1) row.push(R0);
      var out = R0;
      if (n < N) out = Radd(out, lam[n]);                 /* upward, if there is one */
      if (n > 0) out = Radd(out, mu[n - 1]);              /* downward, if there is one */
      row[n] = Rneg(out);
      if (n > 0) row[n - 1] = Radd(row[n - 1], lam[n - 1]);
      if (n < N) row[n + 1] = Radd(row[n + 1], mu[n]);
      row.push(R0);
      rows.push(row);
    }
    var last = [];
    for (j = 0; j < states; j += 1) last.push(R1);
    last.push(R1);
    rows.push(last);
    var red = Mrref(rows, { cols: states });
    var pi = [];
    for (n = 0; n < states; n += 1) pi.push(red.rank === states ? red.M[n][states] : null);
    return { system: rows, dropped: drop, pi: pi, rank: red.rank, ops: red.ops,
             unique: red.rank === states,
             why: 'balance equation ' + (drop + 1) + ' is dropped because the ' + states
               + ' equations are dependent, and sum pi = 1 takes its place -- the same replacement the '
               + 'discrete chain needs, for the same reason' };
  }
  /* Do the two routes agree, entry for entry, exactly? */
  function routesAgree(cutPi, systemPi) {
    if (!systemPi || systemPi.indexOf(null) >= 0) {
      return { ok: false, at: -1, why: 'the balance system has no unique solution, so there is nothing '
        + 'to compare the cut equations with' };
    }
    if (cutPi.length !== systemPi.length) {
      return { ok: false, at: -1, why: 'the two routes produced distributions of different lengths, '
        + cutPi.length + ' against ' + systemPi.length };
    }
    for (var i = 0; i < cutPi.length; i += 1) {
      if (!Requ(cutPi[i], systemPi[i])) {
        return { ok: false, at: i, why: 'the two routes disagree at state ' + i + ': the cut equations '
          + 'give ' + Rtext(cutPi[i]) + ' and the balance system ' + Rtext(systemPi[i]) };
      }
    }
    return { ok: true, at: -1, why: 'every entry of pi from the cut equations is EXACTLY the entry the '
      + 'full balance system produces -- an equality of fractions, not two decimals that look alike' };
  }

  /* ---------------------------------------------- what truncation costs

     birthDeath works on a finite chain, and an M/M/1 queue is not finite. The
     honest figure is the mass the truncation threw away: for the untruncated
     chain pi_n = (1 - rho) rho^n, so everything above state N carries rho^(N+1).
     Exact, and printed rather than assumed negligible. */
  function truncationTail(rho, N) {
    if (Rcmp(rho, R1) >= 0) {
      return { tail: null, why: 'rho is at least 1, so the untruncated chain has no distribution at all '
        + 'and the truncation is not an approximation of anything' };
    }
    var tail = Rpow(rho, N + 1);
    return { tail: tail,
             why: 'the untruncated chain puts rho^' + (N + 1) + ' = ' + Rshort(tail, 6, 8)
               + ' of its probability above state ' + N + ', and that is exactly what this truncation '
               + 'redistributes over the states it keeps' };
  }
  /* P(N > k) on the truncated chain, exact. */
  function queueTail(pi, k) {
    var s = R0, n;
    for (n = k + 1; n < pi.length; n += 1) s = Radd(s, pi[n]);
    return s;
  }
  /* The probability an arrival has to wait, read off the SAME pi: with s
     servers that is P(N >= s). Erlang C is this number, and this kit computes
     it as a reading rather than as a formula. */
  function waitProbability(pi, s) {
    var t = R0, n;
    for (n = s; n < pi.length; n += 1) t = Radd(t, pi[n]);
    return t;
  }
  /* The busy-server count, which is what utilisation means with s servers. */
  function serversBusy(pi, s) {
    var b = R0, n;
    for (n = 0; n < pi.length; n += 1) b = Radd(b, Rmul(R(BigInt(Math.min(n, s)), 1n), pi[n]));
    return b;
  }

  /* --------------------------------------------- the arrival process itself

     n opportunities in one unit of time, each an arrival with probability
     lambda/n, independent. The count is BINOMIAL and that is exact. Its limit
     as n grows is e^(-lambda) lambda^k / k!, and that is not, because
     e^(-lambda) is irrational for every rational lambda except 0.

     The recurrence is the one queue.py uses for the same job -- P(k+1) = P(k) *
     ((n-k)/(k+1)) * p/(1-p) from P(0) = (1-p)^n -- because at n = 1000 the
     closed form per term has a two-thousand-digit denominator and the page
     never paints. scripts/mathcheck.js holds this function against that one on
     the same inputs, so the two Subjects cannot drift apart about a binomial. */
  function binomRowR(n, p, upto) {
    var one = R1, notp = Rsub(one, p);
    if (Rsign(p) < 0 || Rcmp(p, one) > 0) return null;
    if (Rzero(notp)) {
      var all = [];
      for (var i = 0; i <= upto && i < n; i += 1) all.push(R0);
      all.push(one);
      return all;
    }
    var ratio = Rdiv(p, notp), out = [], cur = Rpow(notp, n), k;
    out.push(cur);
    for (k = 0; k < upto && k < n; k += 1) {
      cur = Rmul(cur, Rmul(R(BigInt(n - k), BigInt(k + 1)), ratio));
      out.push(cur);
    }
    return out;
  }
  /* THE ONE APPROXIMATION IN THIS KIT, and the only place it is allowed.
     expNegApprox is sysdesign_core's, shared with the System Design path, and
     it is the reciprocal of a positive-term series for e^x: every term has the
     same sign, so nothing cancels and the answer is right to a rounding of the
     double. It returns a Number and this returns Numbers, which is how the
     boundary is marked -- a rational never leaves this function. */
  function poissonRowApprox(lam, upto) {
    var m = parseFloat(Rfixed(lam, 17));
    var t = expNegApprox(m, 1e-15), out = [t], k;
    for (k = 1; k <= upto; k += 1) { t = t * m / k; out.push(t); }
    return out;
  }
  /* The binomial exactly, the Poisson rounded, and the gap between them --
     which is what "Poisson limit" means, stated as a measurement. */
  function poissonGap(n, lam, upto) {
    var p = Rdiv(lam, R(BigInt(n), 1n));
    var exact = binomRowR(n, p, upto);
    if (exact === null) {
      return { bad: 'lambda/n is not a probability: lambda = ' + Rtext(lam) + ' over n = ' + n
        + ' is ' + Rtext(p) };
    }
    var approx = poissonRowApprox(lam, upto), rows = [], worst = 0, at = -1, k;
    for (k = 0; k < exact.length; k += 1) {
      var ex = parseFloat(Rfixed(exact[k], 17));
      var d = Math.abs(ex - approx[k]);
      if (d > worst) { worst = d; at = k; }
      rows.push({ k: k, exact: exact[k], decimal: ex, poisson: approx[k], diff: ex - approx[k] });
    }
    return { p: p, rows: rows, worst: worst, at: at,
             note: 'the binomial column is exact rational arithmetic; the Poisson column is not, '
               + 'because e^(-lambda) is irrational and every entry carries a factor of it' };
  }
  /* The sentence that has to sit beside the Poisson column, in one place so it
     cannot be worded two ways. */
  function poissonNote() {
    return 'The Poisson column is <strong>not exact and cannot be</strong>: every entry carries a factor '
      + 'of e<sup>&minus;&lambda;</sup>, which is irrational for every rational &lambda; other than 0. '
      + 'It is computed by <code>expNegApprox</code>, shared with the System Design path, as the '
      + 'reciprocal of the positive-term series for e<sup>&lambda;</sup> &mdash; every term the same '
      + 'sign, so nothing cancels &mdash; and it is correct to the rounding of a double, about sixteen '
      + 'significant figures. The binomial column beside it is exact rational arithmetic with no such '
      + 'caveat, and the difference between the two columns is printed rather than described.';
  }

  /* ------------------------------------------------------- drawing the chain

     States in a row, arrivals bowed over the top and services under the
     bottom, so the two directions of the cut are visibly two directions. A
     string of SVG, with no element involved. */
  function bdSvg(lam, mu, pi, opts) {
    opts = opts || {};
    var N = lam.length, states = N + 1, w = opts.w || 660, hgt = opts.h || 220;
    var show = Math.min(states, opts.max || 9);
    var L = 26, gap = (w - 2 * L) / Math.max(1, show - 1), cy = hgt / 2;
    var defs = '<defs><marker id="bdUp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
      + 'markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
      + 'fill="var(--cyan)" /></marker>'
      + '<marker id="bdDown" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
      + 'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--purple)" /></marker></defs>';
    var out = '', n;
    if (opts.cutAt !== undefined && opts.cutAt >= 0 && opts.cutAt < show - 1) {
      var cx = L + gap * (opts.cutAt + 0.5);
      out += '<line x1="' + cx.toFixed(1) + '" y1="14" x2="' + cx.toFixed(1) + '" y2="' + (hgt - 14)
        + '" stroke="var(--amber)" stroke-width="2" stroke-dasharray="5 4" />'
        + '<text x="' + (cx + 5).toFixed(1) + '" y="22" font-size="10" fill="var(--amber)">the cut</text>';
    }
    for (n = 0; n < show - 1; n += 1) {
      var x1 = L + gap * n, x2 = L + gap * (n + 1);
      out += '<path d="M ' + (x1 + 15) + ' ' + (cy - 8) + ' Q ' + ((x1 + x2) / 2) + ' ' + (cy - 42)
        + ' ' + (x2 - 17) + ' ' + (cy - 8) + '" fill="none" stroke="var(--cyan)" stroke-width="1.6" '
        + 'marker-end="url(#bdUp)" />'
        + '<text x="' + ((x1 + x2) / 2) + '" y="' + (cy - 30) + '" font-size="10" fill="var(--cyan)" '
        + 'text-anchor="middle">' + Rshort(lam[n], 3, 5) + '</text>'
        + '<path d="M ' + (x2 - 15) + ' ' + (cy + 8) + ' Q ' + ((x1 + x2) / 2) + ' ' + (cy + 42)
        + ' ' + (x1 + 17) + ' ' + (cy + 8) + '" fill="none" stroke="var(--purple)" stroke-width="1.6" '
        + 'marker-end="url(#bdDown)" />'
        + '<text x="' + ((x1 + x2) / 2) + '" y="' + (cy + 38) + '" font-size="10" fill="var(--purple)" '
        + 'text-anchor="middle">' + Rshort(mu[n], 3, 5) + '</text>';
    }
    for (n = 0; n < show; n += 1) {
      var cxn = L + gap * n;
      var p = pi && pi[n] ? parseFloat(Rfixed(pi[n], 6)) : 0;
      var rad = 13 + 9 * Math.min(1, p * 2.2);
      out += '<circle cx="' + cxn.toFixed(1) + '" cy="' + cy + '" r="' + rad.toFixed(1)
        + '" fill="var(--cyan)" opacity="0.16" />'
        + '<circle cx="' + cxn.toFixed(1) + '" cy="' + cy + '" r="13" fill="var(--panel-solid)" '
        + 'stroke="var(--cyan)" stroke-width="1.8" />'
        + '<text x="' + cxn.toFixed(1) + '" y="' + (cy + 4) + '" font-size="11" font-weight="700" '
        + 'fill="var(--cyan)" text-anchor="middle">' + n + '</text>';
      if (pi && pi[n]) {
        out += '<text x="' + cxn.toFixed(1) + '" y="' + (hgt - 6) + '" font-size="9" fill="var(--muted)" '
          + 'text-anchor="middle">' + Rfixed(pi[n], 3) + '</text>';
      }
    }
    if (states > show) {
      out += '<text x="' + (w - 10) + '" y="' + (cy + 4) + '" font-size="11" fill="var(--muted)" '
        + 'text-anchor="end">&hellip; ' + (states - show) + ' more</text>';
    }
    return defs + out;
  }
  /* pi as bars, for the modes where the shape of the distribution is the point. */
  function piSvg(pi, opts) {
    opts = opts || {};
    var w = opts.w || 660, hgt = opts.h || 170, L = 36, T = 12, B = 24;
    if (!pi.length) return '<text x="14" y="24" font-size="11" fill="var(--muted)">nothing to draw</text>';
    var show = Math.min(pi.length, opts.max || 40);
    var top = R0, i;
    for (i = 0; i < show; i += 1) if (Rcmp(pi[i], top) > 0) top = pi[i];
    var peak = parseFloat(Rfixed(top, 9)) || 1;
    var base = hgt - B, slot = (w - L - 14) / show, out = '';
    out += '<line x1="' + L + '" y1="' + base + '" x2="' + (w - 14) + '" y2="' + base
      + '" stroke="var(--line-strong)" />';
    for (i = 0; i < show; i += 1) {
      var bh = (base - T) * parseFloat(Rfixed(pi[i], 9)) / peak;
      var tone = (opts.markFrom !== undefined && i >= opts.markFrom) ? 'amber' : 'cyan';
      out += '<rect x="' + (L + i * slot + 1).toFixed(2) + '" y="' + (base - bh).toFixed(2)
        + '" width="' + Math.max(1, slot - 2).toFixed(2) + '" height="' + bh.toFixed(2)
        + '" rx="1.5" fill="var(--' + tone + ')" opacity="0.85" />';
      if (show <= 24) {
        out += '<text x="' + (L + i * slot + slot / 2).toFixed(2) + '" y="' + (base + 12)
          + '" font-size="9" fill="var(--muted)" text-anchor="middle">' + i + '</text>';
      }
    }
    out += '<text x="4" y="' + (T + 8) + '" font-size="10" fill="var(--muted)">' + Rfixed(top, 3) + '</text>'
      + '<text x="4" y="' + base + '" font-size="10" fill="var(--muted)">0</text>';
    return out;
  }
"""

_CORE_JS = (RATIONAL_JS + FORMAT_JS + MATRIX_JS + BIGINT_JS + ORFMT_JS
            + QUEUE_JS + APPROX_JS + CHAIN_JS + BDKIT_JS)


# ---------------------------------------------------------------------------
# The worked examples.
# ---------------------------------------------------------------------------

CUT_PRESETS = {
    "machines": {
        "label": "Three machines and one repairer: the arrival rate falls as the queue grows",
        "lam": "3 2 1", "mu": "2 2 2",
    },
    "steady": {
        "label": "Constant rates: the cut equations become a geometric series",
        "lam": "3 3 3 3 3 3", "mu": "5 5 5 5 5 5",
    },
    "twoservers": {
        "label": "Two servers: the service rate doubles once, then stops",
        "lam": "4 4 4 4 4", "mu": "3 6 6 6 6",
    },
    "unstable": {
        "label": "Arrivals faster than service, on a chain that is cut short anyway",
        "lam": "5 5 5 5", "mu": "3 3 3 3",
    },
}

MM1_PRESETS = {
    "eighty": {"label": "Eighty per cent loaded", "lam": "4", "mu": "5", "N": 40},
    "half": {"label": "Half loaded", "lam": "1", "mu": "2", "N": 30},
    "ninetyfive": {"label": "Ninety-five per cent loaded, where the tail matters", "lam": "19", "mu": "20", "N": 60},
}

MMS_PRESETS = {
    "desk": {"label": "A three-server desk at an offered load of 2", "lam": "2", "mu": "1", "s": 3, "N": 40},
    "pair": {"label": "Two servers, offered load 3/2", "lam": "3", "mu": "2", "s": 2, "N": 40},
    "bank": {"label": "Five servers, offered load 4", "lam": "4", "mu": "1", "s": 5, "N": 45},
}

FINITE_PRESETS = {
    "buffer": {"label": "A buffer of five, overloaded", "lam": "6", "mu": "5", "K": 5},
    "tiny": {"label": "Room for two, and a queue that would never settle", "lam": "3", "mu": "2", "K": 2},
    "roomy": {"label": "A buffer of twelve at a load of four fifths", "lam": "4", "mu": "5", "K": 12},
}

POISSON_PRESETS = {
    "three": {"label": "Three arrivals a second on average", "lam": "3", "n": 40},
    "half": {"label": "A rate below one, where the Poisson head is nearly everything", "lam": "1/2", "n": 20},
    "eight": {"label": "Eight a second, where a small n is visibly not Poisson", "lam": "8", "n": 20},
}


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on the path uses.
# ---------------------------------------------------------------------------


def _payload(name, values):
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


def _panel(cid):
    return '      <div id="%s" style="margin-top:12px;"></div>\n' % cid


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
            "birthdeath_lab: mode %r has no preset %r; the presets are %s"
            % (mode, chosen, ", ".join(sorted(presets)))
        )
    return chosen, presets[chosen]


_HELP_JS = r"""
  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function readPos(text) {
    var v = Rread(text);
    return (v === null || Rsign(v) <= 0) ? null : v;
  }
"""


# ---------------------------------------------------------------------------
# Mode `cut` -- the one equation, and the system that confirms it
# ---------------------------------------------------------------------------


def _cut(cfg):
    chosen, here = _preset(cfg, CUT_PRESETS, "cut", "machines")

    markup = (
        _toolbar(
            "What crosses the cut upward must cross back down",
            "one equation per cut, and the whole distribution is their product",
            [
                ("cyan", "arrivals, crossing upward"),
                ("purple", "services, crossing downward"),
                ("amber", "the cut you are looking at"),
                ("green", "the balance system agreeing"),
            ],
        )
        + _stage(_svg("bcChain", "0 0 660 220",
                      "The birth-death chain as a row of states, with arrival rates bowed above and "
                      "service rates below, and one cut marked."))
        + _table("bcCuts")
        + _panel("bcSystem")
        + _table("bcPi")
        + _banner("bcStatus")
    )
    controls = (
        _select("bcPreset", "Worked example",
                [(k, CUT_PRESETS[k]["label"]) for k in
                 ("machines", "steady", "twoservers", "unstable")], chosen)
        + _text("bcLam", "Arrival rate out of each state, from state 0", here["lam"])
        + _text("bcMu", "Service rate out of each state, from state 1", here["mu"])
        + _range("bcCut", "Which cut to look at", 0, 8, 0, 1)
        + _kpis(
            [
                ("States", "bcStatesK"),
                ("&pi; from the cuts", "bcPiK"),
                ("&pi; from the system", "bcSysK"),
                ("Do they agree", "bcAgreeK"),
                ("L", "bcLK"),
                ("W", "bcWK"),
            ]
        )
        + _hint(
            "bcHint",
            "Nothing here assumes the rates are constant. That is the reason to meet the cut "
            "equation before any named queue: M/M/1 is the case where every arrival rate is the same "
            "number, and the moment a rate depends on the state &mdash; a second server, a finite "
            "room, a customer who balks &mdash; the closed forms stop applying and this equation does "
            "not.",
        )
    )

    script = _CORE_JS + _HELP_JS + _payload("PRESETS", CUT_PRESETS) + r"""
  var presetS = document.getElementById('bcPreset');
  var lamIn = document.getElementById('bcLam');
  var muIn = document.getElementById('bcMu');
  var cutS = document.getElementById('bcCut');
  var chainEl = document.getElementById('bcChain');
  var cutsEl = document.getElementById('bcCuts');
  var sysEl = document.getElementById('bcSystem');
  var piEl = document.getElementById('bcPi');
  var statusEl = document.getElementById('bcStatus');

  function blank(message) {
    chainEl.innerHTML = ''; cutsEl.innerHTML = ''; sysEl.innerHTML = ''; piEl.innerHTML = '';
    ['bcStatesK', 'bcPiK', 'bcSysK', 'bcAgreeK', 'bcLK', 'bcWK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var lam = readRates(lamIn.value), mu = readRates(muIn.value);
    if (lam === null || mu === null || lam.length !== mu.length) {
      blank('Give one arrival rate per state starting at state 0, and one service rate per state '
        + 'starting at state 1, as the same number of non-negative numbers or fractions in each box. '
        + 'A chain with N arrival rates has states 0 to N.');
      return;
    }
    if (lam.length > 8) {
      blank('This mode prints every cut equation and the whole balance system, so it stops at eight '
        + 'cuts. Modes <em>mm1</em> and <em>finite</em> take chains as long as you like.');
      return;
    }
    var zeroMu = mu.filter(function (v) { return Rzero(v); });
    if (zeroMu.length) {
      blank('A service rate of zero closes the chain off: nothing can come back down from that state, '
        + 'so the cut equation above it has no solution with positive probability on both sides. Every '
        + 'service rate here has to be strictly positive.');
      return;
    }
    var bd = birthDeath(lam, mu);
    var gb = globalBalance(lam, mu);
    var agree = routesAgree(bd.pi, gb.pi);
    var states = bd.pi.length;
    var cut = Math.max(0, Math.min(bd.cuts.length - 1, +cutS.value || 0));
    cutS.max = String(Math.max(0, bd.cuts.length - 1));
    document.getElementById('bcCutOut').textContent = 'between ' + cut + ' and ' + (cut + 1);

    chainEl.innerHTML = bdSvg(lam, mu, bd.pi, { w: 660, h: 220, cutAt: cut, max: 9 });

    var rows = [], i;
    for (i = 0; i < bd.cuts.length; i += 1) {
      var c = bd.cuts[i];
      rows.push(tr([rowhead('cut ' + i + ' | ' + (i + 1)),
        td(Rtext(c.lam)), td(Rtext(c.mu)), td('<strong>' + Rtext(c.ratio) + '</strong>'),
        td(Rtext(bd.ratios[i + 1])),
        tdl(c.why)], i === cut ? 'focus' : ''));
    }
    cutsEl.innerHTML = '<caption>One equation per cut, and the running product they make</caption>'
      + '<thead>' + tr([th('cut'), th('&lambda;&#8345;'), th('&mu;&#8345;&#8330;&#8321;'),
        th('ratio'), th('&pi;&#8345; / &pi;&#8320;'), th('the equation')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    sysEl.innerHTML = Mtable('The FULL balance system, which knows nothing about cuts &mdash; row n says '
      + '&pi;&#8345;(&lambda;&#8345; + &mu;&#8345;) = &pi;&#8345;&#8330;&#8321;&lambda;&#8345;&#8330;&#8321; '
      + '+ &pi;&#8345;&#8331;&#8321;&mu;&#8345;&#8331;&#8321;, with equation ' + (gb.dropped + 1)
      + ' dropped and &sum;&pi; = 1 in its place', gb.system, { split: states });

    var pRows = [];
    for (i = 0; i < states; i += 1) {
      pRows.push(tr([rowhead('state ' + i), td(Rtext(bd.ratios[i])),
        td('<strong>' + Rshort(bd.pi[i], 6, 8) + '</strong>'),
        td(gb.pi[i] === null ? '&mdash;' : Rshort(gb.pi[i], 6, 8)),
        td(gb.pi[i] !== null && Requ(bd.pi[i], gb.pi[i])
           ? '<span class="tone-green">identical</span>'
           : '<span class="tone-red">DIFFERENT</span>')]));
    }
    piEl.innerHTML = '<caption>The distribution, twice, by two routes that share no arithmetic</caption>'
      + '<thead>' + tr([th('state'), th('&pi;&#8345;/&pi;&#8320;'), th('from the cuts'),
        th('from the balance system'), th('')])
      + '</thead><tbody>' + pRows.join('') + '</tbody>';

    setKpi('bcStatesK', '0 to ' + (states - 1));
    setKpi('bcPiK', bd.pi.map(function (v) { return Rfixed(v, 4); }).join(', '));
    setKpi('bcSysK', gb.unique ? gb.pi.map(function (v) { return Rfixed(v, 4); }).join(', ')
      : '<span class="tone-red">rank ' + gb.rank + '</span>');
    setKpi('bcAgreeK', agree.ok ? '<span class="tone-green">exactly</span>'
      : '<span class="tone-red">NO</span>');
    setKpi('bcLK', Rshort(bd.L, 5, 7));
    setKpi('bcWK', bd.W === null ? '&mdash;' : Rshort(bd.W, 5, 7));

    var focus = bd.cuts[cut];
    statusEl.innerHTML = '<strong>Cut ' + cut + ' says ' + focus.why + '.</strong> '
      + 'In the long run the chain crosses the line between ' + cut + ' and ' + (cut + 1)
      + ' upward exactly as often as it crosses back down &mdash; it cannot do otherwise, because to '
      + 'cross up twice in a row it would have to be on both sides at once. Rate up is '
      + '&pi;<sub>' + cut + '</sub>&lambda;<sub>' + cut + '</sub> and rate down is '
      + '&pi;<sub>' + (cut + 1) + '</sub>&mu;<sub>' + (cut + 1) + '</sub>, so '
      + '&pi;<sub>' + (cut + 1) + '</sub> = &pi;<sub>' + cut + '</sub> &times; '
      + Rtext(focus.ratio) + '. Chaining those from state 0 and dividing by the total gives the whole '
      + 'distribution, with no matrix anywhere in it. '
      + '<strong>' + agree.why.charAt(0).toUpperCase() + agree.why.slice(1) + '.</strong> '
      + (agree.ok
          ? 'That is the check worth having: cutting a chain is the step a reader is asked to believe, '
            + 'and the balance system above was solved by Gauss-Jordan over rationals without any notion '
            + 'of a cut in it. Two routes, no shared arithmetic, the same fractions.'
          : '<span class="tone-red">The two routes disagree, which means one of them is wrong; the page '
            + 'reports it rather than printing whichever it prefers.</span>')
      + ' ' + bd.why + '. '
      + (bd.stable
          ? 'At the top of the chain the arrival rate is below the service rate, so this would still be '
            + 'a distribution if the last pair of rates went on for ever.'
          : '<span class="tone-amber">At the top of the chain arrivals are at least as fast as '
            + 'service</span>, so the untruncated chain would have no distribution at all &mdash; what '
            + 'you are looking at is a finite chain, and its answers are answers about that finite '
            + 'chain and not about an unbounded queue.');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    lamIn.value = p.lam; muIn.value = p.mu;
    redraw();
  });
  [lamIn, muIn, cutS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="One equation, and every queue on this course is a reading of it",
        subtitle="cut the chain, balance the crossings, and check it against the full linear system",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Type any rates you like &mdash; they do not have to be constant",
        panel_intro="The cut equations build &pi; as a product of ratios. Beside them the full balance "
        "system is solved by exact elimination, and the page compares the two distributions fraction by "
        "fraction rather than to a tolerance.",
    )


# ---------------------------------------------------------------------------
# Mode `mm1` -- constant rates, and what the truncation costs
# ---------------------------------------------------------------------------


def _mm1(cfg):
    chosen, here = _preset(cfg, MM1_PRESETS, "mm1", "eighty")

    markup = (
        _toolbar(
            "Constant rates turn the product into a geometric series",
            "&pi;&#8345; = (1 &minus; &rho;)&rho;&#8319;, and every other figure is a sum of those",
            [
                ("cyan", "&pi;&#8345; on the truncated chain"),
                ("amber", "the states the truncation drops"),
                ("green", "the closed form, from the System Design core"),
                ("red", "what the truncation redistributes"),
            ],
        )
        + _stage(_svg("bmPi", "0 0 660 170",
                      "The stationary distribution as bars, falling geometrically."))
        + _table("bmStats")
        + _table("bmTail")
        + _banner("bmStatus")
    )
    controls = (
        _select("bmPreset", "Worked example",
                [(k, MM1_PRESETS[k]["label"]) for k in ("eighty", "half", "ninetyfive")], chosen)
        + _text("bmLam", "Arrival rate &lambda;", here["lam"])
        + _text("bmMu", "Service rate &mu;", here["mu"])
        + _range("bmN", "States kept in the chain", 5, 90, here["N"], 1)
        + _range("bmK", "Report P(N &gt; k) for k =", 0, 20, 3, 1)
        + _kpis(
            [
                ("&rho; = &lambda;/&mu;", "bmRhoK"),
                ("L from the chain", "bmLK"),
                ("L from the closed form", "bmLcK"),
                ("W", "bmWK"),
                ("P(N &gt; k)", "bmTailK"),
                ("Truncation drops", "bmTruncK"),
            ]
        )
        + _hint(
            "bmHint",
            "Drag the number of states down and watch the two L columns separate: the chain is "
            "finite and the closed form is not, so they agree only while the discarded tail is "
            "small. At &rho; = 19/20 the tail above forty states is still over a tenth, and the page "
            "prints that fraction rather than calling the truncation harmless.",
        )
    )

    script = _CORE_JS + _HELP_JS + _payload("PRESETS", MM1_PRESETS) + r"""
  var presetS = document.getElementById('bmPreset');
  var lamIn = document.getElementById('bmLam');
  var muIn = document.getElementById('bmMu');
  var nS = document.getElementById('bmN');
  var kS = document.getElementById('bmK');
  var piEl = document.getElementById('bmPi');
  var statsEl = document.getElementById('bmStats');
  var tailEl = document.getElementById('bmTail');
  var statusEl = document.getElementById('bmStatus');

  function blank(message) {
    piEl.innerHTML = ''; statsEl.innerHTML = ''; tailEl.innerHTML = '';
    ['bmRhoK', 'bmLK', 'bmLcK', 'bmWK', 'bmTailK', 'bmTruncK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var lam = readPos(lamIn.value), mu = readPos(muIn.value);
    if (lam === null || mu === null) {
      blank('The arrival rate and the service rate both have to be positive numbers or fractions. '
        + '&mu; is a RATE, not a duration: a service taking 1/5 of a unit of time has &mu; = 5.');
      return;
    }
    var N = Math.max(5, Math.min(90, +nS.value || 5));
    document.getElementById('bmNOut').textContent = '0 to ' + N;
    var k = Math.max(0, Math.min(20, +kS.value || 0));
    document.getElementById('bmKOut').textContent = String(k);
    var rho = Rdiv(lam, mu);
    var rates = ratesConstant(lam, mu, N);
    var bd = birthDeath(rates.lam, rates.mu);
    var closed = mm1(lam, mu);
    var trunc = truncationTail(rho, N);

    piEl.innerHTML = piSvg(bd.pi, { w: 660, h: 170, max: 24 });

    var rows = [];
    function statRow(name, chain, form, note) {
      rows.push(tr([rowhead(name), td(chain), td(form, 'tone-green'), tdl(note)]));
    }
    statRow('&rho;', Rtext(rho), Rtext(closed.rho), 'the same number by definition; nothing to compare');
    statRow('&pi;&#8320;', Rshort(bd.pi[0], 6, 8),
      closed.stable ? Rshort(closed.p0, 6, 8) : 'no distribution',
      'the chain normalises over the states it kept; the closed form normalises over all of them');
    statRow('L', Rshort(bd.L, 6, 8), closed.stable ? Rshort(closed.L, 6, 8) : 'unbounded',
      'the mean number in the system');
    statRow('L&#8340;', Rshort(bd.Lq, 6, 8), closed.stable ? Rshort(closed.Lq, 6, 8) : 'unbounded',
      'the mean number WAITING, which excludes the one being served');
    statRow('W', bd.W === null ? '&mdash;' : Rshort(bd.W, 6, 8),
      closed.stable ? Rshort(closed.W, 6, 8) : 'unbounded',
      'L divided by the rate that actually gets in, which on a truncated chain is not &lambda;');
    statsEl.innerHTML = '<caption>The chain, and the closed form the System Design path already '
      + 'owns</caption><thead>' + tr([th('quantity'), th('from the cut equations'),
        th('from sysdesign_core.mm1'), th('what it is')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var tRows = [], j;
    for (j = 0; j <= Math.min(k + 4, bd.pi.length - 1); j += 1) {
      var tail = queueTail(bd.pi, j);
      var geo = Rcmp(rho, R1) < 0 ? Rpow(rho, j + 1) : null;
      tRows.push(tr([rowhead('k = ' + j), td(Rshort(bd.pi[j], 6, 8)),
        td(Rshort(tail, 6, 8), j === k ? 'tone-amber' : ''),
        td(geo === null ? '&mdash;' : Rshort(geo, 6, 8), 'tone-green'),
        td(geo === null ? '&mdash;' : Rshort(Rsub(geo, tail), 6, 8))]));
    }
    tailEl.innerHTML = '<caption>P(N &gt; k) on the truncated chain, against &rho;<sup>k+1</sup> on the '
      + 'untruncated one</caption><thead>'
      + tr([th('k'), th('&pi;&#8342;'), th('P(N &gt; k), truncated'), th('&rho;<sup>k+1</sup>'), th('difference')])
      + '</thead><tbody>' + tRows.join('') + '</tbody>';

    setKpi('bmRhoK', Rtext(rho) + (Rcmp(rho, R1) >= 0 ? ' <span class="tone-red">&ge; 1</span>' : ''));
    setKpi('bmLK', Rshort(bd.L, 5, 7));
    setKpi('bmLcK', closed.stable ? Rshort(closed.L, 5, 7) : '<span class="tone-red">unbounded</span>');
    setKpi('bmWK', bd.W === null ? '&mdash;' : Rshort(bd.W, 5, 7));
    setKpi('bmTailK', Rshort(queueTail(bd.pi, k), 6, 8));
    setKpi('bmTruncK', trunc.tail === null ? '<span class="tone-red">everything above ' + N + '</span>'
      : Rshort(trunc.tail, 6, 8));

    var gap = closed.stable ? Rsub(closed.L, bd.L) : null;
    statusEl.innerHTML = '<strong>With every &lambda;&#8345; equal to ' + Rtext(lam)
      + ' and every &mu;&#8345; equal to ' + Rtext(mu) + ', each cut gives the same ratio &rho; = '
      + Rtext(rho) + ', so the product telescopes and &pi;&#8345; = &pi;&#8320;&rho;&#8319;.</strong> '
      + 'That is the geometric distribution, and it is a consequence of the cut equations rather than '
      + 'a separate result: nothing was assumed about the shape of &pi;. '
      + (Rcmp(rho, R1) < 0
          ? 'The untruncated chain normalises to &pi;&#8320; = 1 &minus; &rho; = ' + Rtext(closed.p0)
            + ' and gives L = &rho;/(1 &minus; &rho;) = ' + Rtext(closed.L) + '. '
            + '<strong>This chain is truncated at state ' + N + '</strong>, and ' + trunc.why + '. '
            + 'That is why its L is ' + Rshort(bd.L, 6, 8) + ' rather than ' + Rshort(closed.L, 6, 8)
            + ' &mdash; a gap of ' + Rshort(gap, 6, 8) + ', which shrinks as you add states and never '
            + 'reaches zero. The page prints the gap instead of choosing a number of states at which to '
            + 'stop mentioning it.'
          : '<span class="tone-red">&rho; = ' + Rtext(rho) + ' is at least 1</span>, so there is no '
            + 'untruncated M/M/1 queue here at all: the backlog grows without bound at rate '
            + Rtext(Rsub(lam, mu)) + ' per unit time. The finite chain above still has a distribution '
            + '&mdash; it cannot grow past state ' + N + ' &mdash; but it is the distribution of a '
            + 'DIFFERENT model, one with a buffer, and mode <em>finite</em> is where that model belongs.')
      + ' Everything in the left-hand column is exact: &pi;&#8320; on a ninety-state chain at &rho; = '
      + '19/20 has a denominator of hundreds of digits, and it is carried as a fraction rather than '
      + 'rounded into a double.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    lamIn.value = p.lam; muIn.value = p.mu; nS.value = String(p.N);
    redraw();
  });
  [lamIn, muIn, nS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="The same cut, with the rates held still",
        subtitle="a geometric distribution derived rather than quoted, and the price of a finite chain",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the two rates and choose how much of the chain to keep",
        panel_intro="Every figure on the left comes from the cut equations on a finite chain. The column "
        "beside it is the closed form the System Design path already owns, called rather than "
        "re-derived, so the two Subjects cannot disagree about M/M/1.",
    )


# ---------------------------------------------------------------------------
# Mode `mms` -- s servers, and Erlang C as a reading of the same pi
# ---------------------------------------------------------------------------


def _mms(cfg):
    chosen, here = _preset(cfg, MMS_PRESETS, "mms", "desk")

    markup = (
        _toolbar(
            "The service rate rises until every server is busy, then stops",
            "&mu;&#8345; = min(n, s)&mu; &mdash; one change to one list, and Erlang C falls out",
            [
                ("cyan", "states with an idle server"),
                ("amber", "states where an arrival has to wait"),
                ("green", "Erlang C, from the System Design core"),
                ("purple", "service rate per state"),
            ],
        )
        + _stage(_svg("bsChain", "0 0 660 220",
                      "The chain with the service rate rising for the first s states and constant "
                      "afterwards."))
        + _stage(_svg("bsPi", "0 0 660 170",
                      "The stationary distribution, with the states in which an arrival waits shaded."))
        + _table("bsStats")
        + _banner("bsStatus")
    )
    controls = (
        _select("bsPreset", "Worked example",
                [(k, MMS_PRESETS[k]["label"]) for k in ("desk", "pair", "bank")], chosen)
        + _text("bsLam", "Arrival rate &lambda;", here["lam"])
        + _text("bsMu", "Service rate &mu; of ONE server", here["mu"])
        + _range("bsS", "Servers s", 1, 8, here["s"], 1)
        + _range("bsN", "States kept in the chain", 12, 80, here["N"], 1)
        + _kpis(
            [
                ("Offered load a = &lambda;/&mu;", "bsAK"),
                ("Utilisation &rho; = a/s", "bsRhoK"),
                ("P(wait), from &pi;", "bsWaitK"),
                ("Erlang C", "bsErlK"),
                ("L&#8340;", "bsLqK"),
                ("Servers busy on average", "bsBusyK"),
            ]
        )
        + _hint(
            "bsHint",
            "Add a server and the offered load does not change &mdash; it is &lambda;/&mu; and neither "
            "moves &mdash; but the probability of waiting collapses. That is the whole argument for "
            "pooling, and it is one number here rather than a slogan. Notice also that Erlang C is "
            "not computed: it is P(N &ge; s), added up from the same &pi; the cut equations gave.",
        )
    )

    script = _CORE_JS + _HELP_JS + _payload("PRESETS", MMS_PRESETS) + r"""
  var presetS = document.getElementById('bsPreset');
  var lamIn = document.getElementById('bsLam');
  var muIn = document.getElementById('bsMu');
  var sS = document.getElementById('bsS');
  var nS = document.getElementById('bsN');
  var chainEl = document.getElementById('bsChain');
  var piEl = document.getElementById('bsPi');
  var statsEl = document.getElementById('bsStats');
  var statusEl = document.getElementById('bsStatus');

  function blank(message) {
    chainEl.innerHTML = ''; piEl.innerHTML = ''; statsEl.innerHTML = '';
    ['bsAK', 'bsRhoK', 'bsWaitK', 'bsErlK', 'bsLqK', 'bsBusyK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var lam = readPos(lamIn.value), mu = readPos(muIn.value);
    if (lam === null || mu === null) {
      blank('The arrival rate and one server&rsquo;s service rate both have to be positive.');
      return;
    }
    var s = Math.max(1, Math.min(8, +sS.value || 1));
    var N = Math.max(12, Math.min(80, +nS.value || 12));
    document.getElementById('bsSOut').textContent = String(s);
    document.getElementById('bsNOut').textContent = '0 to ' + N;
    var a = Rdiv(lam, mu), rho = Rdiv(a, R(BigInt(s), 1n));
    var rates = ratesServers(lam, mu, s, N);
    var bd = birthDeath(rates.lam, rates.mu, { servers: s });
    var wait = waitProbability(bd.pi, s);
    var busy = serversBusy(bd.pi, s);
    var erl = erlangC(lam, mu, s);

    chainEl.innerHTML = bdSvg(rates.lam, rates.mu, bd.pi, { w: 660, h: 220, max: 9 });
    piEl.innerHTML = piSvg(bd.pi, { w: 660, h: 170, max: 24, markFrom: s });

    var rows = [], j;
    for (j = 1; j <= Math.min(8, Math.max(s + 2, 4)); j += 1) {
      var rj = ratesServers(lam, mu, j, N);
      var bj = birthDeath(rj.lam, rj.mu, { servers: j });
      var rhoj = Rdiv(a, R(BigInt(j), 1n));
      var stable = Rcmp(rhoj, R1) < 0;
      rows.push(tr([rowhead(j + (j === 1 ? ' server' : ' servers')),
        td(Rtext(rhoj) + (stable ? '' : ' <span class="tone-red">&ge; 1</span>')),
        td(Rpct(waitProbability(bj.pi, j), 3), j === s ? 'tone-amber' : ''),
        td(Rshort(bj.Lq, 5, 7)),
        td(bj.Wq === null ? '&mdash;' : Rshort(bj.Wq, 5, 7)),
        td(Rpct(Rdiv(serversBusy(bj.pi, j), R(BigInt(j), 1n)), 2))]));
    }
    statsEl.innerHTML = '<caption>The same offered load a = ' + Rtext(a) + ', spread over more '
      + 'servers</caption><thead>' + tr([th('servers'), th('&rho; = a/s'), th('P(wait)'), th('L&#8340;'),
        th('W&#8340;'), th('each server busy')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var agrees = erl.stable
      && Rcmp(Rabs(Rsub(wait, erl.pWait)), R(1n, 1000000n)) < 0;
    setKpi('bsAK', Rtext(a));
    setKpi('bsRhoK', Rtext(rho) + (Rcmp(rho, R1) >= 0 ? ' <span class="tone-red">&ge; 1</span>' : ''));
    setKpi('bsWaitK', Rpct(wait, 3));
    setKpi('bsErlK', erl.stable ? Rpct(erl.pWait, 3) + (agrees ? ' <span class="tone-green">&check;</span>'
      : ' <span class="tone-red">&ne;</span>') : '<span class="tone-red">unstable</span>');
    setKpi('bsLqK', Rshort(bd.Lq, 5, 7));
    setKpi('bsBusyK', Rshort(busy, 4, 6) + ' of ' + s);

    statusEl.innerHTML = '<strong>One line changes: &mu;&#8345; = min(n, s)&mu; instead of &mu;.</strong> '
      + 'Below state ' + s + ' an arriving customer finds a free server, so adding one more customer '
      + 'adds one more busy server and the service rate rises with n; at and above state ' + s
      + ' every server is busy and the rate stops rising. The cut equations do not care: they were '
      + 'never told the rates were constant. '
      + '<strong>Erlang C is not a second formula on this page.</strong> The probability an arrival '
      + 'waits is the probability the system is already in state ' + s + ' or above, so it is '
      + '&pi;<sub>' + s + '</sub> + &pi;<sub>' + (s + 1) + '</sub> + &hellip; = ' + Rpct(wait, 3)
      + ' &mdash; added up from the same &pi;. '
      + (erl.stable
          ? 'sysdesign_core&rsquo;s <code>erlangC</code>, which the System Design path uses, gives '
            + Rpct(erl.pWait, 3) + ' from the closed form, and the two '
            + (agrees ? '<span class="tone-green">agree to within the truncation</span>'
               : '<span class="tone-red">disagree, which means one of them is wrong</span>') + '. '
          : 'The closed form refuses this load with ' + s + ' server' + (s === 1 ? '' : 's')
            + ', because &rho; = ' + Rtext(rho) + ' is at least 1 and the untruncated queue has no '
            + 'distribution. ')
      + 'On average ' + Rshort(busy, 4, 6) + ' of the ' + s + ' servers '
      + (Rcmp(busy, R1) <= 0 ? 'is' : 'are') + ' busy, which is a&rsquo;s worth of work whatever s is: '
      + 'adding a server does not reduce the work, it reduces the waiting.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    lamIn.value = p.lam; muIn.value = p.mu; sS.value = String(p.s); nS.value = String(p.N);
    redraw();
  });
  [lamIn, muIn, sS, nS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="More servers, the same work, far less waiting",
        subtitle="one change to the rate list, and Erlang C read off the distribution it produces",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the load and slide the number of servers",
        panel_intro="The service rate out of state n is min(n, s)&mu;, and that single change is the "
        "whole of M/M/s. The probability of waiting is summed from the resulting &pi; and checked "
        "against the closed form the System Design path uses.",
    )


# ---------------------------------------------------------------------------
# Mode `finite` -- a chain that really is finite, and one whose arrivals balk
# ---------------------------------------------------------------------------


def _finite(cfg):
    chosen, here = _preset(cfg, FINITE_PRESETS, "finite", "buffer")

    markup = (
        _toolbar(
            "A queue with a wall does not need to be stable",
            "blocking at the top, an admitted rate below &lambda;, and two numbers both called W",
            [
                ("cyan", "&pi; on the finite chain"),
                ("red", "the blocked state"),
                ("green", "the closed form for M/M/1/K"),
                ("purple", "the same chain with arrivals that balk"),
            ],
        )
        + _stage(_svg("bfChain", "0 0 660 220",
                      "The chain stopped at K, with no arc out of the top state."))
        + _stage(_svg("bfPi", "0 0 660 170",
                      "The stationary distribution on the finite chain."))
        + _table("bfStats")
        + _banner("bfStatus")
    )
    controls = (
        _select("bfPreset", "Worked example",
                [(k, FINITE_PRESETS[k]["label"]) for k in ("buffer", "tiny", "roomy")], chosen)
        + _text("bfLam", "Arrival rate &lambda;", here["lam"])
        + _text("bfMu", "Service rate &mu;", here["mu"])
        + _range("bfK", "Capacity K", 1, 20, here["K"], 1)
        + _select("bfKind", "Which chain",
                  [("block", "a hard wall at K: arrivals above it are lost"),
                   ("balk", "arrivals that balk: &lambda;&#8345; = &lambda;/(n+1)")], "block")
        + _kpis(
            [
                ("&rho; = &lambda;/&mu;", "bfRhoK"),
                ("Blocking &pi;&#8342;", "bfBlockK"),
                ("Admitted rate", "bfAdmK"),
                ("L", "bfLK"),
                ("W with &lambda;", "bfW1K"),
                ("W with the admitted rate", "bfW2K"),
            ]
        )
        + _hint(
            "bfHint",
            "Little&rsquo;s Law needs the rate that actually gets in, and on a lossy system that is "
            "&lambda;(1 &minus; &pi;&#8342;) rather than &lambda;. Both divisions are printed here, "
            "labelled, because the wrong one is the single most common error in a finite-queue "
            "calculation and it is always too small.",
        )
    )

    script = _CORE_JS + _HELP_JS + _payload("PRESETS", FINITE_PRESETS) + r"""
  var presetS = document.getElementById('bfPreset');
  var lamIn = document.getElementById('bfLam');
  var muIn = document.getElementById('bfMu');
  var kS = document.getElementById('bfK');
  var kindS = document.getElementById('bfKind');
  var chainEl = document.getElementById('bfChain');
  var piEl = document.getElementById('bfPi');
  var statsEl = document.getElementById('bfStats');
  var statusEl = document.getElementById('bfStatus');

  function blank(message) {
    chainEl.innerHTML = ''; piEl.innerHTML = ''; statsEl.innerHTML = '';
    ['bfRhoK', 'bfBlockK', 'bfAdmK', 'bfLK', 'bfW1K', 'bfW2K'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var lam = readPos(lamIn.value), mu = readPos(muIn.value);
    if (lam === null || mu === null) {
      blank('Both rates have to be positive numbers or fractions.');
      return;
    }
    var K = Math.max(1, Math.min(20, +kS.value || 1));
    document.getElementById('bfKOut').textContent = String(K);
    var balking = kindS.value === 'balk';
    var rho = Rdiv(lam, mu);
    var rates = balking ? ratesBalking(lam, mu, K) : ratesConstant(lam, mu, K);
    var bd = birthDeath(rates.lam, rates.mu);
    var closed = mm1k(lam, mu, K);
    var block = bd.pi[bd.pi.length - 1];
    var admitted = bd.lambdaEffective;
    var naiveW = Rdiv(bd.L, lam);

    chainEl.innerHTML = bdSvg(rates.lam, rates.mu, bd.pi, { w: 660, h: 220, max: 9 });
    piEl.innerHTML = piSvg(bd.pi, { w: 660, h: 170, max: 21, markFrom: bd.pi.length - 1 });

    var rows = [], j;
    for (j = 1; j <= Math.min(K + 3, 12); j += 1) {
      var rj = balking ? ratesBalking(lam, mu, j) : ratesConstant(lam, mu, j);
      var bj = birthDeath(rj.lam, rj.mu);
      var bl = bj.pi[bj.pi.length - 1];
      rows.push(tr([rowhead('K = ' + j), td(Rpct(bl, 3), j === K ? 'tone-amber' : ''),
        td(Rshort(bj.lambdaEffective, 5, 7)), td(Rshort(bj.L, 5, 7)),
        td(bj.W === null ? '&mdash;' : Rshort(bj.W, 5, 7)),
        td(Rshort(Rdiv(bj.L, lam), 5, 7), 'tone-red')]));
    }
    statsEl.innerHTML = '<caption>Capacity against blocking, and the two divisions Little&rsquo;s Law '
      + 'invites</caption><thead>' + tr([th('capacity'), th('blocking'), th('admitted rate'), th('L'),
        th('W = L / admitted &check;'), th('L / &lambda; &#10007;')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var closedAgrees = !balking
      && Rcmp(Rabs(Rsub(block, closed.blocking)), R(1n, 1000000000n)) < 0
      && Requ(bd.L, closed.L);
    setKpi('bfRhoK', Rtext(rho) + (Rcmp(rho, R1) >= 0
      ? ' <span class="tone-amber">&ge; 1, and it does not matter</span>' : ''));
    setKpi('bfBlockK', Rpct(block, 4));
    setKpi('bfAdmK', Rshort(admitted, 5, 7) + ' of ' + Rtext(lam));
    setKpi('bfLK', Rshort(bd.L, 5, 7));
    setKpi('bfW1K', '<span class="tone-red">' + Rshort(naiveW, 5, 7) + '</span>');
    setKpi('bfW2K', bd.W === null ? '&mdash;'
      : '<span class="tone-green">' + Rshort(bd.W, 5, 7) + '</span>');

    statusEl.innerHTML = '<strong>' + (balking
        ? 'Arrivals balk: a customer who finds n already there joins with probability 1/(n+1), so '
          + '&lambda;&#8345; = &lambda;/(n+1).'
        : 'The chain stops at K = ' + K + ': there is no arc out of the top state, so an arrival that '
          + 'finds the system full is lost.') + '</strong> '
      + 'Either way &rho; = ' + Rtext(rho) + ' is not a stability condition any more. '
      + (Rcmp(rho, R1) >= 0
          ? 'It is <span class="tone-amber">at least 1</span> here, and the chain still has a perfectly '
            + 'good distribution, because a queue that cannot grow cannot run away. '
          : 'It is below 1 here, but that is now a fact about the shape of &pi; rather than a condition '
            + 'for &pi; to exist. ')
      + 'The system is full ' + Rpct(block, 4) + ' of the time, so the rate that actually gets in is '
      + '&lambda;(1 &minus; &pi;&#8342;) = ' + Rshort(admitted, 6, 8) + ' rather than ' + Rtext(lam) + '. '
      + '<strong>That is the rate Little&rsquo;s Law needs.</strong> Dividing L by it gives W = '
      + (bd.W === null ? '&mdash;' : Rshort(bd.W, 6, 8))
      + '; dividing by &lambda; instead gives ' + Rshort(naiveW, 6, 8)
      + ', which is <span class="tone-red">too small by a factor of 1 &minus; &pi;&#8342;</span> and is '
      + 'the standard error in a finite-queue calculation. It is too small because it credits the system '
      + 'with serving customers it never admitted. '
      + (balking
          ? 'The closed form <code>mm1k</code> does not apply to a balking chain at all &mdash; it '
            + 'assumes a constant arrival rate &mdash; which is exactly why this course builds queues '
            + 'from the cut equation and not from a table of formulas.'
          : 'sysdesign_core&rsquo;s <code>mm1k</code> gives blocking ' + Rpct(closed.blocking, 4)
            + ' and L = ' + Rshort(closed.L, 6, 8) + ', and the two routes '
            + (closedAgrees ? '<span class="tone-green">agree exactly</span>'
               : '<span class="tone-red">disagree, which means one of them is wrong</span>')
            + ' &mdash; one Subject&rsquo;s closed form and this one&rsquo;s cut equations, on the same '
            + 'model.');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    lamIn.value = p.lam; muIn.value = p.mu; kS.value = String(p.K);
    redraw();
  });
  kindS.addEventListener('change', redraw);
  [lamIn, muIn, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A queue with a wall, and the rate that actually gets in",
        subtitle="blocking, the admitted rate, and the division Little&rsquo;s Law really asks for",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Set the capacity, or let arrivals balk instead",
        panel_intro="Truncation here is not an approximation: it is the model. Both W values are printed "
        "side by side, and the balking chain is the case no closed form covers and the cut equation "
        "handles without changing.",
    )


# ---------------------------------------------------------------------------
# Mode `poisson` -- the arrival process, and where exactness stops
# ---------------------------------------------------------------------------


def _poisson(cfg):
    chosen, here = _preset(cfg, POISSON_PRESETS, "poisson", "three")

    markup = (
        _toolbar(
            "n chances at &lambda;/n each, and what happens as n grows",
            "the binomial is exact; its limit carries e<sup>&minus;&lambda;</sup> and cannot be",
            [
                ("cyan", "the exact binomial"),
                ("amber", "the Poisson limit, rounded"),
                ("red", "the difference between them"),
                ("green", "the exact column&rsquo;s denominator"),
            ],
        )
        + _stage(_svg("bpBars", "0 0 660 190",
                      "The exact binomial distribution of the number of arrivals in one unit of time."))
        + _table("bpGrid")
        + _table("bpConv")
        + _banner("bpStatus")
    )
    controls = (
        _select("bpPreset", "Worked example",
                [(k, POISSON_PRESETS[k]["label"]) for k in ("three", "half", "eight")], chosen)
        + _text("bpLam", "Mean arrivals per unit time &lambda;", here["lam"])
        + _range("bpN", "Opportunities n in that unit of time", 8, 400, here["n"], 1)
        + _range("bpK", "Counts to tabulate", 4, 14, 8, 1)
        + _kpis(
            [
                ("p = &lambda;/n", "bpPK"),
                ("P(0), exactly", "bpZeroK"),
                ("P(0), Poisson", "bpZeroPK"),
                ("Largest difference", "bpGapK"),
                ("Exact variance", "bpVarK"),
                ("Poisson variance", "bpVarPK"),
            ]
        )
        + _hint(
            "bpHint",
            "The Poisson signature is that the variance equals the mean. The binomial says what that "
            "costs: its variance is &lambda;(1 &minus; &lambda;/n), which is short by exactly "
            "&lambda;&sup2;/n. Push n up and the two columns close; the gap is the whole content of "
            "the word &ldquo;limit&rdquo;, and it is a number rather than a gesture.",
        )
    )

    script = _CORE_JS + _HELP_JS + _payload("PRESETS", POISSON_PRESETS) + r"""
  var presetS = document.getElementById('bpPreset');
  var lamIn = document.getElementById('bpLam');
  var nS = document.getElementById('bpN');
  var kS = document.getElementById('bpK');
  var barsEl = document.getElementById('bpBars');
  var gridEl = document.getElementById('bpGrid');
  var convEl = document.getElementById('bpConv');
  var statusEl = document.getElementById('bpStatus');

  function blank(message) {
    barsEl.innerHTML = ''; gridEl.innerHTML = ''; convEl.innerHTML = '';
    ['bpPK', 'bpZeroK', 'bpZeroPK', 'bpGapK', 'bpVarK', 'bpVarPK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var lam = readPos(lamIn.value);
    if (lam === null) {
      blank('The mean arrival rate has to be a positive number or fraction, such as 3 or 1/2.');
      return;
    }
    var n = Math.max(8, Math.min(400, +nS.value || 8));
    var upto = Math.max(4, Math.min(14, +kS.value || 4));
    document.getElementById('bpNOut').textContent = String(n);
    document.getElementById('bpKOut').textContent = '0 to ' + upto;
    if (Rcmp(lam, R(BigInt(n), 1n)) > 0) {
      blank('With &lambda; = ' + Rtext(lam) + ' and only ' + n + ' opportunities, each one would have to '
        + 'fire with probability greater than 1. Raise n above &lambda;, or lower &lambda;.');
      return;
    }
    var g = poissonGap(n, lam, upto);
    if (g.bad) { blank('<strong>' + g.bad + '.</strong>'); return; }

    var pmf = g.rows.map(function (r) { return [r.k, r.exact]; });
    barsEl.innerHTML = piSvg(g.rows.map(function (r) { return r.exact; }), { w: 660, h: 190, max: 15 });

    var rows = [], i;
    for (i = 0; i < g.rows.length; i += 1) {
      var r = g.rows[i];
      rows.push(tr([rowhead('k = ' + r.k),
        td(Rshort(r.exact, 9, 8), 'tone-cyan'),
        td(Rfixed(r.exact, 9)),
        td(r.poisson.toFixed(9), 'tone-amber'),
        td(Math.abs(r.diff) === 0 ? '0' : r.diff.toExponential(2),
           Math.abs(r.diff) > 1e-4 ? 'tone-red' : 'tone-muted'),
        td(String(r.exact.d).length + ' digits', 'tone-green')]));
    }
    gridEl.innerHTML = '<caption>The number of arrivals in one unit of time: exact, and in the '
      + 'limit</caption><thead>' + tr([th('count'), th('binomial, exactly'), th('as a decimal'),
        th('Poisson, rounded'), th('difference'), th('denominator')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var cRows = [];
    [8, 20, 50, 120, 400].forEach(function (m) {
      if (Rcmp(lam, R(BigInt(m), 1n)) > 0) return;
      var gm = poissonGap(m, lam, upto);
      if (gm.bad) return;
      var vm = Rmul(lam, Rsub(R1, Rdiv(lam, R(BigInt(m), 1n))));
      cRows.push(tr([rowhead('n = ' + m), td(Rtext(gm.p)),
        td(Rfixed(gm.rows[0].exact, 9)), td(gm.worst.toExponential(3), m === n ? 'tone-amber' : ''),
        td(Rshort(vm, 6, 8)), td(Rshort(Rsub(lam, vm), 6, 8), 'tone-red')]));
    });
    convEl.innerHTML = '<caption>More opportunities, each less likely: the exact distribution walking '
      + 'towards its limit</caption><thead>'
      + tr([th('n'), th('p = &lambda;/n'), th('P(0) exactly'), th('largest gap to Poisson'),
        th('variance, exactly'), th('short of the mean by')])
      + '</thead><tbody>' + cRows.join('') + '</tbody>';

    var variance = Rmul(lam, Rsub(R1, Rdiv(lam, R(BigInt(n), 1n))));
    setKpi('bpPK', Rtext(g.p));
    setKpi('bpZeroK', Rshort(g.rows[0].exact, 9, 8));
    setKpi('bpZeroPK', g.rows[0].poisson.toFixed(9) + ' <span class="tone-amber">rounded</span>');
    setKpi('bpGapK', g.worst.toExponential(3) + ' at k = ' + g.at);
    setKpi('bpVarK', Rtext(variance));
    setKpi('bpVarPK', Rtext(lam) + ' <span class="tone-amber">= the mean</span>');

    statusEl.innerHTML = '<strong>One unit of time, ' + n + ' independent opportunities, each an arrival '
      + 'with probability &lambda;/n = ' + Rtext(g.p) + '.</strong> '
      + 'The count is binomial and the whole of that column is exact rational arithmetic: P(0) = '
      + '(1 &minus; ' + Rtext(g.p) + ')<sup>' + n + '</sup> has a denominator of '
      + String(g.rows[0].exact.d).length + ' digits, and it is carried as a fraction rather than as the '
      + 'nearest double. '
      + poissonNote()
      + ' On these numbers the two columns differ by at most ' + g.worst.toExponential(3)
      + ', at k = ' + g.at + '. '
      + '<strong>The variance is where the gap has a name.</strong> The binomial variance is '
      + '&lambda;(1 &minus; &lambda;/n) = ' + Rtext(variance) + ', short of the mean ' + Rtext(lam)
      + ' by exactly &lambda;&sup2;/n = ' + Rtext(Rsub(lam, variance))
      + '. &ldquo;Variance equals the mean&rdquo; is the Poisson signature, and this is what it costs to '
      + 'get there: a window of finitely many opportunities is not a window of infinitely many, and the '
      + 'difference is that fraction. Every arrival process in the other four modes of this kit is '
      + 'Poisson, which is why this page is the one that says where the exactness stops.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    lamIn.value = p.lam; nS.value = String(p.n);
    redraw();
  });
  [lamIn, nS, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Where the arrivals come from, and where the exactness stops",
        subtitle="a binomial in fractions, and a limit that carries an irrational number",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Slide the number of opportunities and watch the limit arrive",
        panel_intro="The exact column is a binomial in rational arithmetic with denominators of hundreds "
        "of digits. The column beside it is the Poisson limit, which cannot be exact because "
        "e<sup>&minus;&lambda;</sup> is irrational, and the page prints the difference.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "cut": _cut,
    "mm1": _mm1,
    "mms": _mms,
    "finite": _finite,
    "poisson": _poisson,
}

MODES = tuple(sorted(_MODES))


def birthdeath_lab(cfg):
    """The queues kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract. A kit that fell back to a default would render a
    finished-looking page carrying another lesson's widget: every markup
    assertion passes, labcheck passes, and the reader is shown the wrong
    arithmetic under the right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "birthdeath_lab: unknown mode %r; the five modes of the queues kit are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})
