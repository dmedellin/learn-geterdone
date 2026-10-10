"""dekit -- the differential-equations kit (PLAN section D.3).

docs/differential-equations/PLAN.md section D.3 specifies fifteen modes; the
conventions of D.0 bind every one, and the shared blocks come from de_core
(D.1). This file builds the eight first-order modes and dispatches the other
seven to dekit_b.MODES, so two engineers can build the kit without sharing a
file:

  verify      (vf)  substitute a candidate, read the residual; fit C and D
  field       (sf)  a slope field, the exact slope at a point, the nullcline,
                    the horizontal solutions
  euler       (eu)  exact Euler steps, the exact error against a known solution
  order       (od)  errors at three step sizes, their ratios, the observed order
  separable   (sp)  G(y) = H(t) + C, the constant, the explicit branch, its domain
  growth      (gr)  y′ = k·(y − A) by Euler, exactly, beside the closed form
  autonomous  (au)  equilibria, stability by the sign of f, f′(y*), limits
  bifurcate   (bf)  equilibria against a parameter, and where two of them meet

PRESETS ARE LESSON DATA. Every mode takes cfg['presets'] (each an id, a label
naming the instance, the instance fields of D.3 and `expect`) and
cfg['preset']. A preset's change handler rewrites the instance inputs; a
redraw-only select (sfGrid, odMethod, spView, auView) keeps the value the
lesson ships (cfg['grid'], cfg['method'], cfg['view']) and no preset sets it.

Every module-level JavaScript name this file adds is prefixed DK_ (shared by
these eight modes) or by its mode's two letters (vf, sf, eu, od, sp, gr, au,
bf). DK_JS and MODE_JS are exported for the tests and for mathcheck.js; DK_JS
is three parts (DK_BASE_JS, DK_ROOTS_JS, DK_CLOSED_JS) and a page carries only
the parts its mode calls.

DEVIATIONS FROM D.3, each the closest correct thing:

  * Inputs whose D.3 id is also a tile's id take the suffix In: vfICIn,
    euExactIn, spGIn, spHIn. A page cannot carry one id twice; the tiles keep
    D.3's names.
  * euler: euExact reads `undefined at t = 5/4` when the known solution has a
    pole between t0 and tₙ, not only when RFeval hits a pole AT tₙ.
    1/(1 − t) at 5/4 is −4, a number, but the solution through (0, 1) ends at
    t = 1, and printing −4 would be the confidently wrong figure lesson 3.10
    exists to warn about. The table's y(tₙ) column uses the same rule, and so
    does order's y(T).
  * field: sfEquil lists y = c when f(t, c) = 0 for EVERY t (the roots of the
    gcd of f's coefficients in t), not `none` whenever f contains t: y′ = t·y
    has the horizontal solution y = 0. When f has no t it is D.3's rule.
  * A fraction longer than 48 characters prints in a tile or a table cell as
    `≈ 6.72e23 (exact: 1849 digits over 1849)`: lessons 3.10 and 4.6 make
    fractions of hundreds and thousands of digits. It is the exact value that
    is rounded, and the digit counts say how large the fraction is.
  * separable: spCheck differentiates the implicit relation (G′ = g and
    H′ = h, exactly) and, when there is an explicit solution, the composite
    G(y(t)); so the implicit-only `poly` preset of lesson 4.2 still gets a
    check. spImplicit scales a polynomial G to leading coefficient 1
    (y² = t² + 4), and a polynomial whose leading coefficient is negative is
    printed from its constant term (1 − t², 2/(2 − t²)).
  * autonomous: auSteps and auLimit describe the FIRST start (D.3 says so for
    auLimit); the table lists every start. auEquil prints the rational
    equilibria and then a surd pair (0, (1 ± √5)/2), as D.3's example does;
    auTypes and auSlope list every equilibrium in increasing order, and f′ at
    a surd equilibrium is exact too (f′((1 − √5)/2) = −√5). auInflect reads
    `none` when f′ has no real root and `none rational` when its real roots
    are irrational or not placed.
  * bifurcate: the critical values are the rational roots in [amin, amax] of
    the discriminant, computed for degree 2 and 3 alike as the Sylvester
    resultant Res_y(f, f_y) divided exactly by the leading coefficient; for
    degree 1 they are the roots of the leading coefficient.
"""

from fractions import Fraction

from . import de_core as dc
from . import dekit_b

KIT = "dekit"


# ---------------------------------------------------------------------------
# Python-side validation helpers
# ---------------------------------------------------------------------------


def _pf(p, mode, field, letters, allow_none=False):
    return dc.formula(p.get(field), set(letters), KIT, mode, p, field, allow_none=allow_none)


def _pr(p, mode, field, allow_none=False):
    return dc.rational(p.get(field), KIT, mode, p, field, allow_none=allow_none)


def _int(p, mode, field, lo, hi, default=None):
    value = p.get(field, default)
    dc.check(KIT, mode, p, isinstance(value, int) and not isinstance(value, bool) and lo <= value <= hi,
             "%s must be a whole number from %d to %d, not %r" % (field, lo, hi, value))
    return value


def _txt(p, mode, field, allowed=None, allow_none=False):
    value = p.get(field)
    if value is None or (isinstance(value, str) and not value.strip()):
        if allow_none:
            return None
        dc.check(KIT, mode, p, False, "%s is missing" % field)
    dc.check(KIT, mode, p, isinstance(value, str), "%s must be text, not %r" % (field, value))
    dc.check(KIT, mode, p, not (set(value) & set('<>&"')), "%s may not contain < > & or a double quote" % field)
    if allowed is not None:
        bad = sorted(set(value) - set(allowed))
        dc.check(KIT, mode, p, not bad, "%s %r may not contain %s" % (field, value, " ".join(bad)))
    return value


def _vec(p, mode, field, sizes, allow_none=False):
    """A list of rationals of one of the given lengths, as canonical texts."""
    value = p.get(field)
    if value is None:
        if allow_none:
            return None
        dc.check(KIT, mode, p, False, "%s is missing" % field)
    dc.check(KIT, mode, p, isinstance(value, (list, tuple)) and len(value) in sizes,
             "%s must be a list of %s rationals, not %r" % (field, " or ".join(str(s) for s in sizes), value))
    return [dc.rational(v, KIT, mode, p, field) for v in value]


def _F(text_):
    return Fraction(text_)


def _join(items):
    return " ".join(items)


# ---------------------------------------------------------------------------
# DK_JS -- helpers shared by the eight modes. Arithmetic a tile prints happens
# in de_core's blocks or in the exact helpers here, never in floating point.
# ---------------------------------------------------------------------------

DK_BASE_JS = r"""
  /* ---- dekit: page helpers ---------------------------------------------- */
  function DK_window(fns, xmin, xmax) {
    var ys = [], i, j;
    for (j = 0; j < fns.length; j += 1) {
      for (i = 0; i <= 240; i += 1) {
        var y = fns[j](xmin + (xmax - xmin) * i / 240);
        if (typeof y === 'number' && isFinite(y)) ys.push(y);
      }
    }
    if (!ys.length) return { xmin: xmin, xmax: xmax, ymin: -1, ymax: 1 };
    ys.sort(function (a, b) { return a - b; });
    var lo = ys[0], hi = ys[ys.length - 1];
    var qlo = ys[Math.floor(ys.length * 0.06)], qhi = ys[Math.ceil(ys.length * 0.94) - 1];
    if (hi - lo > 6 * Math.max(qhi - qlo, 1e-9)) { lo = qlo; hi = qhi; }
    if (hi - lo < 1e-9) { lo -= 1; hi += 1; }
    var pad = 0.1 * (hi - lo);
    return { xmin: xmin, xmax: xmax, ymin: lo - pad, ymax: hi + pad };
  }
  function DK_plot(id, win, alt) {
    var plot = Plot(DE_el(id), win).frame();
    plot.describe(alt);
    return plot;
  }
  function DK_table(caption, head, rows, focus) {
    var h = '<table class=tt><caption>' + DE_esc(caption) + '</caption><thead><tr>', i, j;
    for (i = 0; i < head.length; i += 1) h += '<th>' + DE_esc(head[i]) + '</th>';
    h += '</tr></thead><tbody>';
    for (i = 0; i < rows.length; i += 1) {
      h += i === focus ? '<tr class=focus>' : '<tr>';
      for (j = 0; j < rows[i].length; j += 1) h += '<td>' + DE_esc(rows[i][j]) + '</td>';
      h += '</tr>';
    }
    return h + '</tbody></table>';
  }
  function DK_need(text, what) {
    var r = DE_rat(text);
    if (r === null) throw new Error(what + ' must be a rational number such as 2, -1/2 or 0.25');
    return r;
  }
  /* Rationals separated by spaces (commas and brackets are ignored): the
     start, the window, a point, an initial value. */
  function DK_list(text, count, what) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-');
    s = s.replace(/[(),;]/g, ' ').replace(/^\s+|\s+$/g, '');
    var parts = s.length ? s.split(/\s+/) : [], out = [], i;
    if (count !== null && parts.length !== count) {
      throw new Error(what + ' takes ' + count + ' rational numbers separated by spaces');
    }
    for (i = 0; i < parts.length; i += 1) {
      var r = DE_rat(parts[i]);
      if (r === null) throw new Error(what + ': ' + parts[i] + ' is not a rational number');
      out.push(r);
    }
    return out;
  }
  function DK_range(id) {
    var el = DE_el(id), v = parseInt(el.value, 10);
    if (!isFinite(v)) v = parseInt(el.getAttribute('min') || '1', 10);
    DE_set(id + 'Out', v);
    return v;
  }
  /* D.0's step caps: h a positive rational with denominator at most 10⁶, and
     the last t within |t| ≤ 10⁶. */
  function DK_h(h, t0, n) {
    if (Rsign(h) <= 0) throw new Error('h must be positive');
    if (h.d > 1000000n) throw new Error('the denominator of h is over 1000000; this lab steps with a denominator of at most 1000000');
    var tN = Radd(t0, Rmul(h, R(BigInt(n))));
    if (Rcmp(Rabs(tN), R(1000000n)) > 0) throw new Error('the steps reach t = ' + DE_q(tN) + '; this lab keeps |t| at most 1000000');
    return h;
  }
  /* An exact value for a tile. A fraction too long to read prints rounded,
     with the size of the exact one beside it. */
  function DK_big(r) {
    var s = DE_q(r);
    if (s.length <= 48) return s;
    var nd = (r.n < 0n ? -r.n : r.n).toString().length, dd = r.d.toString().length;
    return DE_dec(DE_float(r)) + ' (exact: ' + nd + ' digits over ' + dd + ')';
  }
  /* A polynomial whose leading coefficient is negative is written from its
     constant term when that reads better: 1 − t², 2 − t², t − t². */
  function DK_ptext(p, v) {
    p = Pnorm(p);
    var pos = false, i;
    for (i = 0; i < p.length - 1; i += 1) if (p[i] && Rsign(p[i]) > 0) pos = true;
    if (!(p.length && Rsign(Plead(p)) < 0 && pos)) return DE_ptext(p, v);
    var pieces = [];
    for (i = 0; i < p.length; i += 1) {
      if (!p[i] || Rzero(p[i])) continue;
      pieces.push({ c: p[i], body: i === 0 ? '' : (i === 1 ? v : v + DE_sup(i)), dot: false });
    }
    return DE_sum(pieces);
  }
  /* a POLY_JS list at a double, for drawing */
  function DK_pf(p, x) {
    var acc = 0, i;
    for (i = p.length - 1; i >= 0; i -= 1) acc = acc * x + Rnum(p[i] || R0);
    return acc;
  }
  /* Every rational root, ascending. POLY_JS's Prationalroots tries only the
     divisors of the leading coefficient when the constant term is 0, so it
     misses 4 in y − y²/4; the powers of the variable come off first here. */
  function DK_ratroots(p) {
    p = Pnorm(p);
    var k = 0, out = [], i;
    while (k < p.length && Rzero(p[k])) k += 1;
    if (k === p.length) return [];
    var rest = Prationalroots(p.slice(k));
    if (k > 0) out.push(R0);
    for (i = 0; i < rest.length; i += 1) if (!Rzero(rest[i])) out.push(rest[i]);
    out.sort(Rcmp);
    return out;
  }
  function DK_sub(k) {
    var s = String(k), out = '', i, subs = '₀₁₂₃₄₅₆₇₈₉';
    for (i = 0; i < s.length; i += 1) out += subs.charAt(s.charCodeAt(i) - 48);
    return out;
  }
"""

DK_ROOTS_JS = r"""
  /* ---- dekit: exact real roots and the phase line ------------------------ */
  /* p + q·√k as text: (1 − √5)/2, −√2, 1 + √3. */
  function DK_rootOne(p, q, k) {
    if (k === 1n || Rzero(q)) return DE_q(k === 1n ? Radd(p, q) : p);
    var D = p.d * q.d / bgcd(p.d, q.d);
    var P = p.n * (D / p.d), Q = q.n * (D / q.d), neg = Q < 0n;
    if (neg) Q = -Q;
    var part = DE_rootpart(Q, k, false);
    if (P === 0n) return (neg ? '−' : '') + part + (D === 1n ? '' : '/' + D);
    var body = DE_q(R(P)) + (neg ? ' − ' : ' + ') + part;
    return D === 1n ? body : '(' + body + ')/' + D;
  }
  /* A polynomial at p + q·√k, exactly: {a, b} meaning a + b·√k. */
  function DK_surdEval(poly, x) {
    var a = R0, b = R0, i, P = x.p, Q = x.q, K = R(x.k);
    for (i = poly.length - 1; i >= 0; i -= 1) {
      var na = Radd(Rmul(a, P), Rmul(Rmul(b, Q), K)), nb = Radd(Rmul(a, Q), Rmul(b, P));
      a = Radd(na, poly[i] || R0); b = nb;
    }
    return { a: a, b: b };
  }
  function DK_surdText(v, k) { return Rzero(v.b) ? DE_q(v.a) : DK_rootOne(v.a, v.b, k); }
  /* The real roots of a POLY_JS list, exactly: every rational root, and the
     two surd roots when what is left after the rational ones is a quadratic.
     open is true when a factor of degree 3 or more is left, whose real roots
     this kit cannot place exactly. */
  function DK_roots(p) {
    p = Pnorm(p);
    var out = [], pair = null, open = false, i;
    if (Pdeg(p) < 1) return { list: out, pair: null, open: false, rest: [] };
    var rat = DK_ratroots(p);
    for (i = 0; i < rat.length; i += 1) out.push({ r: rat[i], p: rat[i], q: R0, k: 1n, x: DE_float(rat[i]), text: DE_q(rat[i]) });
    var rest = Pfactor(p).rest;
    if (rest.length && Pdeg(rest) === 2) {
      var qr = quadroots(rest[2], rest[1], rest[0]);
      if (qr.kind === 'irrational') {
        var w = DE_float(qr.s.q) * Math.sqrt(Number(qr.s.k)), c = DE_float(qr.p);
        out.push({ r: null, p: qr.p, q: Rneg(qr.s.q), k: qr.s.k, x: c - w, text: DK_rootOne(qr.p, Rneg(qr.s.q), qr.s.k) });
        out.push({ r: null, p: qr.p, q: qr.s.q, k: qr.s.k, x: c + w, text: DK_rootOne(qr.p, qr.s.q, qr.s.k) });
        pair = DE_root(qr.p, qr.s, false);
      }
    } else if (rest.length && Pdeg(rest) > 2) open = true;
    out.sort(function (u, v) { return u.r && v.r ? Rcmp(u.r, v.r) : u.x - v.x; });
    return { list: out, pair: pair, open: open, rest: rest };
  }
  /* The roots as D.3 prints them: the rational ones ascending, then a surd
     pair as one entry; with a prefix (y = ) every root separately. */
  function DK_eqText(rr, prefix) {
    var parts = [], i;
    prefix = prefix || '';
    for (i = 0; i < rr.list.length; i += 1) if (rr.list[i].r) parts.push(prefix + rr.list[i].text);
    if (rr.pair) {
      if (prefix) { for (i = 0; i < rr.list.length; i += 1) if (!rr.list[i].r) parts.push(prefix + rr.list[i].text); }
      else parts.push(rr.pair);
    }
    return parts.length ? parts.join(', ') : 'none';
  }
  /* A rational strictly between two roots: the midpoint when both are
     rational, else a dyadic rational well inside the gap. */
  function DK_between(A, B) {
    if (A.r && B.r) return Rdiv(Radd(A.r, B.r), R(2n));
    var mid = (A.x + B.x) / 2, gap = (B.x - A.x) / 8, den = 16, k;
    for (k = 0; k < 40; k += 1) {
      var num = Math.round(mid * den);
      if (num / den > A.x + gap && num / den < B.x - gap) return R(BigInt(num), BigInt(den));
      den *= 2;
    }
    throw new Error('two equilibria are too close together to separate');
  }
  /* The phase line of y′ = f(y): equilibria, the sign of f on every interval
     (each found by evaluating f exactly at a rational test point), each
     equilibrium classified by the signs on its two sides, and f′ there. */
  function DK_phase(f) {
    f = Pnorm(f);
    if (!f.length) throw new Error('f is 0, so every value of y is an equilibrium');
    var rr = DK_roots(f);
    if (rr.open) {
      throw new Error('f has the factor ' + DE_ptext(rr.rest, 'y') + ', of degree ' + Pdeg(rr.rest)
        + ' with no rational root; this lab places equilibria only when they are rational or the roots of a quadratic');
    }
    var L = rr.list, tests = [], signs = [], types = [], slopes = [], i;
    if (!L.length) tests.push(R0);
    else {
      tests.push(R(BigInt(Math.floor(L[0].x)) - 1n));
      for (i = 0; i + 1 < L.length; i += 1) tests.push(DK_between(L[i], L[i + 1]));
      tests.push(R(BigInt(Math.ceil(L[L.length - 1].x)) + 1n));
    }
    for (i = 0; i < tests.length; i += 1) signs.push(Rsign(Peval(f, tests[i])));
    var fp = Pderiv(f);
    for (i = 0; i < L.length; i += 1) {
      var sl = signs[i], sr = signs[i + 1];
      types.push(sl > 0 && sr < 0 ? 'stable' : (sl < 0 && sr > 0 ? 'unstable' : 'semistable'));
      slopes.push(DK_surdText(DK_surdEval(fp, L[i]), L[i].k));
    }
    return { f: f, fp: fp, rr: rr, list: L, tests: tests, signs: signs, types: types, slopes: slopes };
  }
  function DK_typesText(ph) {
    var out = [], i;
    for (i = 0; i < ph.list.length; i += 1) out.push(ph.list[i].text + ' ' + ph.types[i]);
    return out.length ? out.join('; ') : 'none';
  }
  /* Where a start goes, read off the phase line: to the next equilibrium in
     the direction f points, or without bound. */
  function DK_limit(ph, y0) {
    var s = Rsign(Peval(ph.f, y0)), i, L = ph.list;
    if (s === 0) return 'at equilibrium';
    var x0 = DE_float(y0);
    if (s > 0) {
      for (i = 0; i < L.length; i += 1) if (L[i].r ? Rcmp(L[i].r, y0) > 0 : L[i].x > x0) return '→ ' + L[i].text;
      return '→ +∞';
    }
    for (i = L.length - 1; i >= 0; i -= 1) if (L[i].r ? Rcmp(L[i].r, y0) < 0 : L[i].x < x0) return '→ ' + L[i].text;
    return '→ −∞';
  }
"""

DK_CLOSED_JS = r"""
  /* ---- dekit: a known solution --------------------------------------------- */
  /* A typed closed form: a rational function of t, or an exponential
     polynomial with no C or D. */
  function DK_closed(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    if (!/\S/.test(s)) return null;
    if (/[CD]/.test(s)) throw new Error('a known solution has no C or D in it; fix the constants first');
    var F = null;
    try { F = RFfromExpr(Eparse(s), 't'); } catch (e) { F = null; }
    if (F !== null) return { kind: 'rf', F: F, text: RFtext(F, 't') };
    var ep = EPparse(s, {});
    return { kind: 'ep', e: ep, text: EPtext(ep) };
  }
  /* A pole of den between a and b, ends included: true or false. Exact for
     the rational roots; the roots of what is left (no rational root) are
     irrational, so comparing them with the rational ends in floating point
     cannot tie: a quadratic by its formula, anything larger by a scan for a
     change of sign. */
  function DK_poleBetween(den, a, b) {
    den = Pnorm(den);
    if (Pdeg(den) < 1) return false;
    var lo = Rcmp(a, b) <= 0 ? a : b, hi = Rcmp(a, b) <= 0 ? b : a, rat = DK_ratroots(den), i;
    for (i = 0; i < rat.length; i += 1) if (Rcmp(rat[i], lo) >= 0 && Rcmp(rat[i], hi) <= 0) return true;
    var rest = Pfactor(den).rest, xl = DE_float(lo), xh = DE_float(hi);
    if (!rest.length) return false;
    if (Pdeg(rest) === 2) {
      var A = DE_float(rest[2]), B = DE_float(rest[1]), disc = B * B - 4 * A * DE_float(rest[0]);
      if (disc < 0) return false;
      var r1 = (-B - Math.sqrt(disc)) / (2 * A), r2 = (-B + Math.sqrt(disc)) / (2 * A);
      return (r1 >= xl && r1 <= xh) || (r2 >= xl && r2 <= xh);
    }
    var prev = null, k;
    for (k = 0; k <= 2048; k += 1) {
      var v = DK_pf(rest, xl + (xh - xl) * k / 2048);
      if (v === 0 || (prev !== null && (v > 0) !== (prev > 0))) return true;
      prev = v;
    }
    return false;
  }
  /* A closed form at t, on the interval that holds t0: {r} exact, {x}
     rounded, or {undef} past a pole. */
  function DK_at(ex, t0, t) {
    if (ex.kind === 'rf') {
      if (DK_poleBetween(ex.F.den, t0, t)) return { undef: true };
      return { r: RFeval(ex.F, t) };
    }
    var r = EPevalExact(ex.e, t);
    return r !== null ? { r: r } : { x: EPevalFloat(ex.e, DE_float(t)) };
  }
  function DK_atText(v) { return v.undef ? 'undefined' : (v.r ? DK_big(v.r) : DE_dec(v.x)); }
  function DK_atFloat(ex, x) { return ex.kind === 'rf' ? RFevalFloat(ex.F, x) : EPevalFloat(ex.e, x); }
"""

DK_JS = DK_BASE_JS + DK_ROOTS_JS + DK_CLOSED_JS


def _dk(roots=False, closed=False):
    return DK_BASE_JS + (DK_ROOTS_JS if roots else "") + (DK_CLOSED_JS if closed else "")


# ---------------------------------------------------------------------------
# verify (vf)
# ---------------------------------------------------------------------------

VERIFY_JS = r"""
  /* ---- dekit/verify: substitute a candidate, read the residual ----------
     The equation lhs = rhs becomes the polynomial lhs − rhs in t, y, v = y′
     and w = y″. A rational-function candidate is substituted over RF_JS; an
     exponential-polynomial one, in a linear equation, over EP_JS; either way
     the residual is computed symbolically and compared with zero. */
  var VF_VARS = ['t', 'y', 'v', 'w'];
  function vfSide(text) {
    try {
      return MPparse(text, VF_VARS);
    } catch (e) {
      throw new Error(DE_msg(e).replace('this lab reads t and y and v and w', 'this lab reads t, y, y′ and y″')
        .replace('this lab steps polynomial right-hand sides exactly', 'this lab reads equations polynomial in t, y, y′ and y″'));
    }
  }
  function vfEquation(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    s = s.replace(/″/g, '\'\'').replace(/′/g, '\'');
    if (/y\s*'\s*'\s*'/.test(s)) throw new Error('y‴ makes the order 3; this lab checks equations of order 1 and 2');
    var stray = /[vw]/.exec(s);
    if (stray) throw new Error('the letter ' + stray[0] + ' is not a variable here; this lab reads t, y, y′ and y″');
    var parts = s.split('=');
    if (parts.length !== 2) throw new Error('write the equation with one = sign, as y\'\' + y = 0');
    var subst = function (x) { return x.replace(/y\s*'\s*'/g, 'w').replace(/y\s*'/g, 'v'); };
    var L = subst(parts[0]), Rr = subst(parts[1]);
    if (/'/.test(L + Rr)) throw new Error('a prime belongs straight after y, as y\' or y\'\'');
    var P = MPlift(MPsub(vfSide(L), vfSide(Rr)), VF_VARS);
    var order = MPhas(P, 'w') ? 2 : (MPhas(P, 'v') ? 1 : 0);
    if (!order) throw new Error('there is no y′ in this equation, so it is not a differential equation');
    var linear = true, i;
    for (i = 0; i < P.terms.length; i += 1) {
      var e = P.terms[i].e;
      if (e[1] + e[2] + e[3] > 1) linear = false;
    }
    return { P: P, order: order, linear: linear };
  }
  function vfCandidate(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    if (!/\S/.test(s)) throw new Error('there is no candidate here');
    if (!/[CD]/.test(s)) {
      var F = null;
      try { F = RFfromExpr(Eparse(s), 't'); } catch (e) { F = null; }
      if (F !== null) return { kind: 'rf', F: F };
    }
    return { kind: 'ep', fam: EPfamily(s) };
  }
  /* The residual of a rational function F, as a rational function. */
  function vfResidualRF(P, F) {
    var Ys = [F, RFderiv(F)], acc = RFconst(R0), i;
    Ys.push(RFderiv(Ys[1]));
    for (i = 0; i < P.terms.length; i += 1) {
      var e = P.terms[i].e, term = RFconst(P.terms[i].c);
      if (e[0]) term = RFmul(term, RFpow(RFvar(), e[0]));
      if (e[1]) term = RFmul(term, RFpow(Ys[0], e[1]));
      if (e[2]) term = RFmul(term, RFpow(Ys[1], e[2]));
      if (e[3]) term = RFmul(term, RFpow(Ys[2], e[3]));
      acc = RFadd(acc, term);
    }
    return acc;
  }
  /* A linear equation as a_y·y + a_v·y′ + a_w·y″ + q, the coefficients
     polynomials in t. */
  function vfLinearParts(P) {
    var zero = MPconst(VF_VARS, R0);
    var q = MPsubst(MPsubst(MPsubst(P, 'y', zero), 'v', zero), 'w', zero);
    return {
      a: [MPtoPoly(MPpartial(P, 'y'), 't'), MPtoPoly(MPpartial(P, 'v'), 't'), MPtoPoly(MPpartial(P, 'w'), 't')],
      q: MPtoPoly(q, 't')
    };
  }
  function vfApply(parts, Y, withForcing) {
    var d1 = EPderiv(Y), d2 = EPderiv(d1);
    var out = EPadd(EPadd(EPmulpoly(Y, parts.a[0]), EPmulpoly(d1, parts.a[1])), EPmulpoly(d2, parts.a[2]));
    if (withForcing) out = EPadd(out, EPmulpoly(EPconst(R1), parts.q));
    return out;
  }
  function vfFloatResidual(P, Y) {
    var d1 = EPderiv(Y), d2 = EPderiv(d1), pts = [0, 0.5, 1, 1.5, 2], worst = 0, i;
    for (i = 0; i < pts.length; i += 1) {
      var t = pts[i];
      var r = MPevalFloat(P, { t: t, y: EPevalFloat(Y, t), v: EPevalFloat(d1, t), w: EPevalFloat(d2, t) });
      if (!isFinite(r)) return NaN;
      worst = Math.max(worst, Math.abs(r));
    }
    return worst;
  }
  /* The residual of the family base + C·(dC) + D·(dD), term by term. */
  function vfFamText(rb, names, rdirs) {
    var out = EPzero(rb) ? '' : EPtext(rb), k;
    for (k = 0; k < names.length; k += 1) {
      if (EPzero(rdirs[k])) continue;
      out += (out ? ' + ' : '') + names[k] + '·(' + EPtext(rdirs[k]) + ')';
    }
    return out || '0';
  }
  /* y(t0) and y′(t0) of an exponential polynomial, exactly, or a refusal. */
  function vfAt(e, t0) {
    var a = EPevalExact(e, t0), b = EPevalExact(EPderiv(e), t0);
    if (a === null || b === null) {
      throw new Error('the candidate is exact only at t = 0, and the initial value is at t = ' + DE_q(t0) + '; no fit is printed');
    }
    return [a, b];
  }
  /* Fix the constants from the initial values, exactly. */
  function vfFit(out, fam, names, dirs, ic) {
    var base = vfAt(fam.base, ic[0]), dv = [], rows = [], k, j, Y = fam.base, sol = null;
    for (k = 0; k < dirs.length; k += 1) dv.push(vfAt(dirs[k], ic[0]));
    for (k = 1; k < ic.length; k += 1) {
      var row = [];
      for (j = 0; j < dirs.length; j += 1) row.push(dv[j][k - 1]);
      rows.push({ row: row, rhs: Rsub(ic[k], base[k - 1]), label: (k === 1 ? 'y(' : 'y′(') + DE_q(ic[0]) + ') = ' + DE_q(ic[k]) });
    }
    if (names.length === 1) {
      for (k = 0; k < rows.length; k += 1) {
        if (Rzero(rows[k].row[0])) continue;
        sol = [Rdiv(rows[k].rhs, rows[k].row[0])];
        out.family = names[0] + ' = ' + DE_q(sol[0]) + ' from ' + rows[k].label;
        break;
      }
      if (!sol) out.note += ' No value of ' + names[0] + ' fits these initial values.';
    } else if (names.length === 2) {
      if (rows.length < 2) out.note += ' Two constants need two values: y(t0) and y′(t0).';
      else {
        sol = RFsolve([rows[0].row, rows[1].row], [rows[0].rhs, rows[1].rhs]);
        if (sol) out.family = names[0] + ' = ' + DE_q(sol[0]) + ', ' + names[1] + ' = ' + DE_q(sol[1]);
        else out.note += ' No values of C and D fit these initial values.';
      }
    } else sol = [];
    if (!sol) return Y;
    for (k = 0; k < sol.length; k += 1) Y = EPadd(Y, EPscale(dirs[k], sol[k]));
    var fit = vfAt(Y, ic[0]);
    out.icText = 'satisfied';
    if (!Requ(fit[0], ic[1])) out.icText = 'fails: y(' + DE_q(ic[0]) + ') = ' + DE_q(fit[0]);
    else if (ic.length === 3 && !Requ(fit[1], ic[2])) out.icText = 'fails: y′(' + DE_q(ic[0]) + ') = ' + DE_q(fit[1]);
    out.text = EPtext(Y);
    return Y;
  }
  function vfCompute(eqText, candText, icText) {
    var eq = vfEquation(eqText), cand = vfCandidate(candText);
    var ic = DK_list(icText, null, 'the initial values');
    if (ic.length !== 0 && ic.length !== 2 && ic.length !== 3) {
      throw new Error('the initial values are t0 y0, or t0 y0 v0 for y(t0) and y′(t0)');
    }
    var out = { eq: eq, cand: cand, ic: ic, note: '', family: '—', icText: '—' };
    if (cand.kind === 'rf') {
      var res = vfResidualRF(eq.P, cand.F);
      out.zero = RFzero(res);
      out.residual = RFtext(res, 't');
      out.verdict = out.zero ? 'Solution' : 'Not a solution';
      out.draw = function (x) { return RFevalFloat(cand.F, x); };
      out.text = RFtext(cand.F, 't');
      if (ic.length) {
        var y0 = RFeval(cand.F, ic[0]), d = RFderiv(cand.F), v0 = RFeval(d, ic[0]);
        if (y0 === null) out.icText = 'fails: y(' + DE_q(ic[0]) + ') is undefined';
        else if (!Requ(y0, ic[1])) out.icText = 'fails: y(' + DE_q(ic[0]) + ') = ' + DE_q(y0);
        else if (ic.length === 3 && v0 !== null && !Requ(v0, ic[2])) out.icText = 'fails: y′(' + DE_q(ic[0]) + ') = ' + DE_q(v0);
        else out.icText = 'satisfied';
      }
      return out;
    }
    var fam = cand.fam, names = [], dirs = [], k;
    if (fam.hasC) { names.push('C'); dirs.push(fam.C); }
    if (fam.hasD) { names.push('D'); dirs.push(fam.D); }
    out.text = EPtext(fam.base);
    if (!eq.linear) {
      if (names.length) throw new Error('a candidate with C or D is fitted here only in a linear equation');
      var worst = vfFloatResidual(eq.P, fam.base);
      out.zero = null;
      out.residual = isFinite(worst) ? DE_dec(worst) + ' at most' : '—';
      out.verdict = 'Checked at 5 points only';
      out.note = ' The equation is nonlinear and the candidate is not a rational function, so this lab cannot decide it exactly: the residual was evaluated in floating point at t = 0, 1/2, 1, 3/2 and 2.';
    } else {
      var parts = vfLinearParts(eq.P), rb = vfApply(parts, fam.base, true), rdirs = [];
      out.zero = EPzero(rb);
      for (k = 0; k < dirs.length; k += 1) { rdirs.push(vfApply(parts, dirs[k], false)); out.zero = out.zero && EPzero(rdirs[k]); }
      out.residual = names.length ? vfFamText(rb, names, rdirs) : (EPzero(rb) ? '0' : EPtext(rb));
      out.verdict = out.zero ? 'Solution' : 'Not a solution';
    }
    var Y = fam.base;
    if (names.length && !ic.length) out.family = names.join(', ') + ' free';
    if (ic.length) {
      try {
        if (names.length) Y = vfFit(out, fam, names, dirs, ic);
        else {
          var at = vfAt(Y, ic[0]);
          out.icText = 'satisfied';
          if (!Requ(at[0], ic[1])) out.icText = 'fails: y(' + DE_q(ic[0]) + ') = ' + DE_q(at[0]);
          else if (ic.length === 3 && !Requ(at[1], ic[2])) out.icText = 'fails: y′(' + DE_q(ic[0]) + ') = ' + DE_q(at[1]);
        }
      } catch (err) {
        out.family = '—'; out.icText = '—';
        out.note += ' ' + DE_msg(err) + '.';
      }
    }
    out.draw = function (x) { return EPevalFloat(Y, x); };
    return out;
  }
"""


def _verify(cfg):
    mode = "verify"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        eq = _txt(p, mode, "equation", allowed="0123456789+-*/^(). ='ty")
        dc.check(KIT, mode, p, eq.count("=") == 1, "equation %r needs exactly one =" % eq)
        ic = _vec(p, mode, "ic", (2, 3), allow_none=True)
        table[str(p["id"])] = {
            "equation": eq,
            "candidate": _txt(p, mode, "candidate"),
            "ic": _join(ic) if ic else "",
        }
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Order", "vfOrder"), ("Linear?", "vfLinear"), ("Residual", "vfResidual"),
             ("Verdict", "vfVerdict"), ("Initial values", "vfIC"), ("Constants", "vfFamily")]
    markup = (
        dc.toolbar("Substitute and check", "the residual is simplified symbolically, never evaluated",
                   [("cyan", "the candidate, drawn"), ("muted", "slope field (first order)")])
        + dc.stage(dc.svg("vfPlot", "the candidate solution"))
        + dc.banner("vfStatus")
    )
    controls = (
        dc.select("vfPreset", "Equation and candidate", dc.options(found), pick["id"])
        + dc.text("vfEq", "Equation, with y' and y'' for the derivatives", first["equation"])
        + dc.text("vfCand", "Candidate y(t)", first["candidate"])
        + dc.text("vfICIn", "Initial values: t0 y0, or t0 y0 v0 (may be empty)", first["ic"])
        + dc.kpis(tiles)
        + dc.hint("Candidates: a ratio of polynomials in t, such as 1/(1 - t), or sums of terms such as "
                  "3t^2, 2e^(-t), t cos(2t) and C e^(3t), with the constants C and D.")
    )
    glue = dc.literal("VFP", table) + r"""
  var VF_TILES = ['vfOrder', 'vfLinear', 'vfResidual', 'vfVerdict', 'vfIC', 'vfFamily'];
  var vfPresetIn = DE_el('vfPreset'), vfEqIn = DE_el('vfEq'), vfCandIn = DE_el('vfCand'), vfICIn = DE_el('vfICIn');
  function vfRender(r) {
    DE_set('vfOrder', String(r.eq.order));
    DE_set('vfLinear', r.eq.linear ? 'Linear' : 'Nonlinear');
    DE_set('vfResidual', r.residual);
    DE_set('vfVerdict', r.verdict);
    DE_set('vfIC', r.icText);
    DE_set('vfFamily', r.family);
    var t0 = r.ic.length ? DE_float(r.ic[0]) : 0, lo = t0 - 2, hi = t0 + 2;
    var plot = DK_plot('vfPlot', DK_window([r.draw], lo, hi), 'the candidate y = ' + r.text + ' for t from ' + lo + ' to ' + hi);
    var P = r.eq.P;
    if (r.eq.order === 1 && MPdegree(P, 'v') === 1) {
      var a = MPpartial(P, 'v'), b = MPsubst(P, 'v', MPconst(VF_VARS, R0));
      DE_arrows(plot, function (t, y) {
        var pt = { t: t, y: y, v: 0, w: 0 };
        return -MPevalFloat(b, pt) / MPevalFloat(a, pt);
      }, 15);
    }
    plot.curve(r.draw);
    if (r.ic.length) plot.point(t0, DE_float(r.ic[1]), 'plot-point', 'start');
    var msg = r.zero === null ? '<strong>Rounded.</strong> ' : '<strong>Exact.</strong> ';
    msg += 'Substituting y = ' + DE_esc(r.text) + ', the left side minus the right side is ' + DE_esc(r.residual) + ': '
      + DE_esc(r.verdict.toLowerCase()) + '.';
    DE_ok('vfStatus', msg + DE_esc(r.note));
  }
  function redraw() {
    try {
      vfRender(vfCompute(vfEqIn.value, vfCandIn.value, vfICIn.value));
    } catch (e) {
      DE_refuse('vfStatus', VF_TILES, ['vfPlot'], DE_msg(e));
    }
  }
  vfPresetIn.addEventListener('change', function () {
    var p = VFP[vfPresetIn.value];
    if (p) { vfEqIn.value = p.equation; vfCandIn.value = p.candidate; vfICIn.value = p.ic; }
    redraw();
  });
  [vfEqIn, vfCandIn, vfICIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Checking a solution", subtitle="Substitute, simplify, compare with zero",
        markup=markup, controls=controls,
        script=dc.script("MPOLY", "EP", "DRAW", extra=_dk() + VERIFY_JS + glue),
        panel_title="Choose the equation and the candidate",
        panel_intro="A candidate solves the equation when the residual, the left side minus the right side "
                    "after substituting, is zero for every t. The lab simplifies it symbolically.",
        select="vfPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# field (sf)
# ---------------------------------------------------------------------------

FIELD_JS = r"""
  /* ---- dekit/field: a slope field, read exactly at one point ------------
     The segments are pixels; the slope at the chosen point, the nullcline
     and the horizontal solutions are exact. y = c is a horizontal solution
     when f(t, c) = 0 for every t: c is a root of every coefficient of f in t. */
  function sfCompute(fText, winText, startText, pointText) {
    var f = MPparse(fText, ['t', 'y']);
    var w = DK_list(winText, 4, 'the window');
    if (Rcmp(w[0], w[1]) >= 0 || Rcmp(w[2], w[3]) >= 0) throw new Error('the window is tmin tmax ymin ymax, with tmin < tmax and ymin < ymax');
    var st = DK_list(startText, null, 'the start');
    if (st.length && st.length !== 2) throw new Error('the start takes two rational numbers, t0 y0, or nothing');
    var pt = DK_list(pointText, 2, 'the point');
    var slope = MPeval(f, { t: pt[0], y: pt[1] });
    var dy = MPdegree(f, 'y'), hasT = MPhas(f, 't'), zero, equil, eqRoots = null;
    var cols = {}, keys = [], i;
    for (i = 0; i < f.terms.length; i += 1) {
      var e = f.terms[i].e, key = String(e[0]);
      if (!cols.hasOwnProperty(key)) { cols[key] = []; keys.push(key); }
      while (cols[key].length <= e[1]) cols[key].push(R0);
      cols[key][e[1]] = Radd(cols[key][e[1]], f.terms[i].c);
    }
    if (MPzero(f)) { zero = 'everywhere'; equil = 'every y = c'; }
    else {
      var g = Pnorm(cols[keys[0]]);
      for (i = 1; i < keys.length; i += 1) g = Pgcd(g, Pnorm(cols[keys[i]]));
      if (Pdeg(g) < 1) equil = 'none';
      else {
        eqRoots = DK_roots(g);
        equil = DK_eqText(eqRoots, 'y = ');
        if (eqRoots.open) equil = (equil === 'none' ? '' : equil + ', and ') + 'the roots of ' + DE_ptext(eqRoots.rest, 'y');
      }
      if (dy === 1) {
        var a = MPtoPoly(MPpartial(f, 'y'), 't'), b = MPtoPoly(MPsubst(f, 'y', MPconst(f.vars, R0)), 't');
        zero = 'y = ' + RFtext(RFmake(Pscale(b, R(-1n)), a), 't');
      } else if (dy < 1) zero = 'none in y';
      else if (!hasT) {
        var rr = DK_roots(MPtoPoly(f, 'y'));
        zero = rr.open ? '—' : DK_eqText(rr, 'y = ');
      } else zero = '—';
    }
    return { f: f, win: w, start: st.length ? st : null, pt: pt, slope: slope, zero: zero, equil: equil, eqRoots: eqRoots };
  }
"""


def _field(cfg):
    mode = "field"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        win = _vec(p, mode, "window", (4,))
        dc.check(KIT, mode, p, _F(win[0]) < _F(win[1]) and _F(win[2]) < _F(win[3]),
                 "window is [tmin, tmax, ymin, ymax] with tmin < tmax and ymin < ymax")
        start = _vec(p, mode, "start", (2,), allow_none=True)
        table[str(p["id"])] = {
            "f": _pf(p, mode, "f", "ty"),
            "window": _join(win),
            "start": _join(start) if start else "",
            "point": _join(_vec(p, mode, "point", (2,))),
        }
    grid = dc.choice(cfg, "grid", ["15", "11", "21"], KIT, mode)
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Slope at the point", "sfSlope"), ("Direction there", "sfSign"),
             ("Slope 0 (nullcline)", "sfZero"), ("Horizontal solutions", "sfEquil")]
    markup = (
        dc.toolbar("A slope field", "the segment at (t, y) has slope f(t, y)",
                   [("muted", "slope segments"), ("purple", "a solution, drawn by stepping in floating point"),
                    ("green", "horizontal solutions")])
        + dc.stage(dc.svg("sfPlot", "a slope field"))
        + dc.banner("sfStatus")
    )
    controls = (
        dc.select("sfPreset", "Equation", dc.options(found), pick["id"])
        + dc.text("sfF", "f(t, y) in y' = f(t, y)", first["f"])
        + dc.text("sfWindow", "Window: tmin tmax ymin ymax", first["window"])
        + dc.text("sfStart", "Start of a drawn solution: t0 y0 (may be empty)", first["start"])
        + dc.text("sfPoint", "Point: t y", first["point"])
        + dc.select("sfGrid", "Segments per side", [("11", "11"), ("15", "15"), ("21", "21")], grid)
        + dc.kpis(tiles)
        + dc.hint("Type a polynomial in t and y: t - y, y(1 - y), y^2, 2t.")
    )
    glue = dc.literal("SFP", table) + r"""
  var SF_TILES = ['sfSlope', 'sfSign', 'sfZero', 'sfEquil'];
  var sfPresetIn = DE_el('sfPreset'), sfFIn = DE_el('sfF'), sfWinIn = DE_el('sfWindow'), sfStartIn = DE_el('sfStart');
  var sfPointIn = DE_el('sfPoint'), sfGridIn = DE_el('sfGrid');
  function sfRender(r) {
    var s = Rsign(r.slope), i;
    DE_set('sfSlope', DE_q(r.slope));
    DE_set('sfSign', s > 0 ? 'rising' : (s < 0 ? 'falling' : 'flat'));
    DE_set('sfZero', r.zero);
    DE_set('sfEquil', r.equil);
    var win = { xmin: DE_float(r.win[0]), xmax: DE_float(r.win[1]), ymin: DE_float(r.win[2]), ymax: DE_float(r.win[3]) };
    var fn = function (t, y) { return MPevalFloat(r.f, { t: t, y: y }); };
    var plot = DK_plot('sfPlot', win, 'slope field of y′ = ' + MPtext(r.f) + ' for ' + win.xmin + ' ≤ t ≤ ' + win.xmax);
    DE_arrows(plot, fn, parseInt(sfGridIn.value, 10) || 15);
    if (r.eqRoots) for (i = 0; i < r.eqRoots.list.length; i += 1) plot.hline(r.eqRoots.list[i].x, 'plot-curve good');
    if (r.start) {
      var t0 = DE_float(r.start[0]), y0 = DE_float(r.start[1]);
      DE_polyline(plot, DE_rk4float(fn, [t0, y0], (win.xmax - t0) / 400 || 0.01), 'plot-curve alt');
      DE_polyline(plot, DE_rk4float(fn, [t0, y0], (win.xmin - t0) / 400 || -0.01), 'plot-curve alt');
      plot.point(t0, y0, 'plot-point', 'start');
    }
    plot.point(DE_float(r.pt[0]), DE_float(r.pt[1]), 'plot-point', 'slope ' + DE_q(r.slope));
    DE_ok('sfStatus', '<strong>Exact.</strong> At (' + DE_esc(DE_q(r.pt[0])) + ', ' + DE_esc(DE_q(r.pt[1])) + ') the slope is f = '
      + DE_esc(DE_q(r.slope)) + '. The segments are drawn from f in floating point'
      + (r.start ? '; the purple curve is drawn by stepping in floating point, a picture rather than a computed figure.' : '.'));
  }
  function redraw() {
    try {
      sfRender(sfCompute(sfFIn.value, sfWinIn.value, sfStartIn.value, sfPointIn.value));
    } catch (e) {
      DE_refuse('sfStatus', SF_TILES, ['sfPlot'], DE_msg(e));
    }
  }
  sfPresetIn.addEventListener('change', function () {
    var p = SFP[sfPresetIn.value];
    if (p) { sfFIn.value = p.f; sfWinIn.value = p.window; sfStartIn.value = p.start; sfPointIn.value = p.point; }
    redraw();
  });
  [sfFIn, sfWinIn, sfStartIn, sfPointIn].forEach(function (el) { el.addEventListener('input', redraw); });
  sfGridIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Slope fields", subtitle="The slope at every point, before any solving",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", "RF", "DRAW", extra=_dk(roots=True) + FIELD_JS + glue),
        panel_title="Choose the right-hand side",
        panel_intro="Each segment has the slope a solution through that point must have. The slope at the "
                    "chosen point is computed exactly.",
        select="sfPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# euler (eu)
# ---------------------------------------------------------------------------

EULER_JS = r"""
  /* ---- dekit/euler: exact Euler steps -------------------------------------
     yₙ₊₁ = yₙ + h·f(tₙ, yₙ) in exact fractions, to n steps or the digit
     budget; the known solution is exact where it is rational at tₙ. */
  function euCompute(fText, startText, hText, n, exactText) {
    var f = MPparse(fText, ['t', 'y']);
    var st = DK_list(startText, 2, 'the start (t0 y0)');
    if (n < 1 || n > 64) throw new Error('n runs from 1 to 64');
    var h = DK_h(DK_need(hText, 'h'), st[0], n);
    var ex = DK_closed(exactText);
    var run = DE_euler(f, st[0], st[1], h, n), rows = [], i;
    for (i = 0; i < run.rows.length; i += 1) {
      var row = run.rows[i], at = ex ? DK_at(ex, st[0], row.t) : null, err = null;
      if (at && at.r) err = { r: Rabs(Rsub(row.y, at.r)) };
      else if (at && !at.undef) err = { x: Math.abs(DE_float(row.y) - at.x) };
      rows.push({ t: row.t, y: row.y, f: MPeval(f, { t: row.t, y: row.y }), at: at, err: err });
    }
    return { f: f, t0: st[0], y0: st[1], h: h, n: n, run: run, ex: ex, rows: rows, last: rows[rows.length - 1] };
  }
"""


def _euler(cfg):
    mode = "euler"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        h = _pr(p, mode, "h")
        dc.check(KIT, mode, p, _F(h) > 0, "h must be positive")
        table[str(p["id"])] = {
            "f": _pf(p, mode, "f", "ty"),
            "start": _join([_pr(p, mode, "t0"), _pr(p, mode, "y0")]),
            "h": h,
            "n": _int(p, mode, "n", 1, 64),
            "exact": _txt(p, mode, "exact", allow_none=True) or "",
        }
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Last yₙ", "euLast"), ("Last yₙ, rounded", "euLastDec"), ("Known solution at tₙ", "euExact"),
             ("Error |yₙ − y(tₙ)|", "euError"), ("Widest denominator (digits)", "euDigits"), ("Steps", "euStopped")]
    markup = (
        dc.toolbar("Euler's method, exactly", "every yₙ is a fraction",
                   [("green", "Euler polygon (exact)"), ("cyan", "known solution")])
        + dc.stage(dc.svg("euPlot", "the Euler polygon"))
        + dc.wrap("euTable")
        + dc.banner("euStatus")
    )
    controls = (
        dc.select("euPreset", "Equation and step", dc.options(found), pick["id"])
        + dc.text("euF", "f(t, y) in y' = f(t, y)", first["f"])
        + dc.text("euStart", "Start: t0 y0", first["start"])
        + dc.text("euH", "Step h", first["h"])
        + dc.range_("euN", "Steps n", 1, 64, first["n"])
        + dc.text("euExactIn", "Known solution y(t) (may be empty)", first["exact"])
        + dc.kpis(tiles)
        + dc.hint("f is a polynomial in t and y. The known solution is a ratio of polynomials in t, "
                  "or sums of terms such as 3e^(-t) and t^2.")
    )
    glue = dc.literal("EUP", table) + r"""
  var EU_TILES = ['euLast', 'euLastDec', 'euExact', 'euError', 'euDigits', 'euStopped'];
  var euPresetIn = DE_el('euPreset'), euFIn = DE_el('euF'), euStartIn = DE_el('euStart'), euHIn = DE_el('euH');
  var euNIn = DE_el('euN'), euExactIn = DE_el('euExactIn');
  function euErr(w) { return !w.err ? '—' : (w.err.r ? DK_big(w.err.r) : DE_dec(w.err.x)); }
  function euRender(r) {
    var last = r.last, run = r.run, i, rows = [];
    DE_set('euLast', DK_big(last.y));
    DE_set('euLastDec', DE_dec(DE_float(last.y)));
    DE_set('euExact', !r.ex ? '—' : (last.at.undef ? 'undefined at t = ' + DE_q(last.t) : DK_atText(last.at)));
    DE_set('euError', euErr(last));
    DE_set('euDigits', String(run.digits));
    DE_set('euStopped', run.stopped ? 'stopped after step ' + run.steps + ': digit budget'
      : (r.n === 1 ? 'the one step' : 'all ' + r.n + ' steps'));
    for (i = 0; i < r.rows.length; i += 1) {
      var w = r.rows[i], row = [String(i), DE_q(w.t), DK_big(w.y), DK_big(w.f)];
      if (r.ex) row.push(DK_atText(w.at), euErr(w));
      rows.push(row);
    }
    var head = ['n', 'tₙ', 'yₙ', 'f(tₙ, yₙ)'];
    if (r.ex) head.push('y(tₙ)', 'error');
    DE_html('euTable', DK_table('yₙ₊₁ = yₙ + h·f(tₙ, yₙ) with h = ' + DE_q(r.h), head, rows, rows.length - 1));
    var pts = [], lo = DE_float(r.t0), hi = DE_float(last.t);
    for (i = 0; i < r.rows.length; i += 1) pts.push([DE_float(r.rows[i].t), DE_float(r.rows[i].y)]);
    var fns = [function (x) {
      var best = null, j;
      for (j = 0; j < pts.length; j += 1) if (best === null || Math.abs(pts[j][0] - x) < Math.abs(best[0] - x)) best = pts[j];
      return best ? best[1] : NaN;
    }];
    var exf = r.ex ? function (x) { return DK_atFloat(r.ex, x); } : null;
    if (exf) fns.push(exf);
    if (hi - lo < 1e-9) hi = lo + 1;
    var plot = DK_plot('euPlot', DK_window(fns, lo, hi), 'Euler polygon for y′ = ' + MPtext(r.f) + ' with h = ' + DE_q(r.h));
    if (exf) plot.curve(exf);
    DE_polyline(plot, pts, 'plot-curve good');
    for (i = 0; i < pts.length; i += 1) plot.point(pts[i][0], pts[i][1], 'plot-point');
    var msg = '<strong>Exact.</strong> y′ = ' + DE_esc(MPtext(r.f)) + ' from y(' + DE_esc(DE_q(r.t0)) + ') = ' + DE_esc(DE_q(r.y0))
      + ' with h = ' + DE_esc(DE_q(r.h)) + ': y' + DK_sub(run.steps) + ' = ' + DE_esc(DK_big(last.y)) + '.';
    if (run.stopped) {
      msg += ' Step ' + (run.steps + 1) + ' would pass the budget of ' + DE_DIGITS + ' digits: a quadratic right-hand side doubles the digits each step. Nothing was rounded to continue.';
    }
    if (r.ex && last.at.undef) {
      msg += ' The known solution y = ' + DE_esc(r.ex.text) + ' has a pole between t = ' + DE_esc(DE_q(r.t0)) + ' and t = '
        + DE_esc(DE_q(last.t)) + ', so the solution through the start does not reach tₙ; Euler steps past it without noticing.';
    }
    DE_ok('euStatus', msg);
  }
  function redraw() {
    try {
      euRender(euCompute(euFIn.value, euStartIn.value, euHIn.value, DK_range('euN'), euExactIn.value));
    } catch (e) {
      DE_refuse('euStatus', EU_TILES, ['euTable', 'euPlot'], DE_msg(e));
    }
  }
  euPresetIn.addEventListener('change', function () {
    var p = EUP[euPresetIn.value];
    if (p) { euFIn.value = p.f; euStartIn.value = p.start; euHIn.value = p.h; euNIn.value = String(p.n); euExactIn.value = p.exact; }
    redraw();
  });
  [euFIn, euStartIn, euHIn, euNIn, euExactIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Euler's method", subtitle="Exact steps, and the exact error",
        markup=markup, controls=controls,
        script=dc.script("MPOLY", "RF", "EP", "STEP", "DRAW", extra=_dk(closed=True) + EULER_JS + glue),
        panel_title="Choose the equation and the step",
        panel_intro="Each step follows the slope at its left end for a time h. The fractions are exact; the "
                    "method is not.",
        select="euPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# order (od)
# ---------------------------------------------------------------------------

ORDER_JS = r"""
  /* ---- dekit/order: the error at three step sizes ------------------------
     E(h) = |y_N − y(T)| with N = (T − t0)/h, for three h; the ratios of
     successive errors, and log₂ of the last as the observed order. */
  var OD_STEPPERS = { euler: DE_euler, heun: DE_heun, rk4: DE_rk4 };
  var OD_NAMES = { euler: 'Euler', heun: 'improved Euler', rk4: 'Runge–Kutta' };
  function odPow2(r) {
    var n = r.n, d = r.d;
    if (n <= 0n) return null;
    if (d === 1n && (n & (n - 1n)) === 0n) return n.toString(2).length - 1;
    if (n === 1n && (d & (d - 1n)) === 0n) return -(d.toString(2).length - 1);
    return null;
  }
  function odCompute(fText, startText, TText, exactText, hsText, method) {
    var f = MPparse(fText, ['t', 'y']);
    var st = DK_list(startText, 2, 'the start (t0 y0)');
    var T = DK_need(TText, 'T');
    if (Rcmp(T, st[0]) <= 0) throw new Error('T must be after the start t0 = ' + DE_q(st[0]));
    var ex = DK_closed(exactText);
    if (!ex) throw new Error('the error needs the known solution y(t)');
    var hs = DK_list(hsText, 3, 'the step sizes');
    var cap = method === 'rk4' ? 32 : 64, step = OD_STEPPERS[method] || DE_euler;
    var Y = DK_at(ex, st[0], T);
    if (Y.undef) throw new Error('the known solution y = ' + ex.text + ' has a pole before T = ' + DE_q(T));
    var rows = [], i;
    for (i = 0; i < 3; i += 1) {
      var h = hs[i];
      if (Rsign(h) <= 0) throw new Error('every h must be positive');
      var N = Rdiv(Rsub(T, st[0]), h);
      if (!Rint(N)) throw new Error('(T − t0)/h = ' + DE_q(N) + ' for h = ' + DE_q(h) + ' is not a whole number of steps');
      if (N.n > BigInt(cap)) throw new Error('h = ' + DE_q(h) + ' needs ' + N.n + ' steps; this method takes at most ' + cap);
      DK_h(h, st[0], Number(N.n));
      var run = step(f, st[0], st[1], h, Number(N.n));
      if (run.stopped) throw new Error('with h = ' + DE_q(h) + ' the digit budget stopped the run after step ' + run.steps + ', before T');
      var yN = run.rows[run.rows.length - 1].y;
      var E = Y.r ? { r: Rabs(Rsub(yN, Y.r)) } : { x: Math.abs(DE_float(yN) - Y.x) };
      rows.push({ h: h, N: N.n, yN: yN, E: E, zero: E.r ? Rzero(E.r) : E.x === 0 });
    }
    var ratio = '—', order = '—', zeros = 0;
    for (i = 0; i < 3; i += 1) if (rows[i].zero) zeros += 1;
    if (zeros === 3) order = 'exact (error 0)';
    else if (!zeros) {
      if (Y.r) {
        var r1 = Rdiv(rows[0].E.r, rows[1].E.r), r2 = Rdiv(rows[1].E.r, rows[2].E.r), k = odPow2(r2);
        ratio = DK_big(r1) + ', ' + DK_big(r2);
        order = k !== null ? String(k) : DE_dec(Math.log(DE_float(r2)) / Math.LN2);
      } else {
        var x1 = rows[0].E.x / rows[1].E.x, x2 = rows[1].E.x / rows[2].E.x;
        ratio = DE_dec(x1) + ', ' + DE_dec(x2);
        order = DE_dec(Math.log(x2) / Math.LN2);
      }
    }
    return { f: f, t0: st[0], y0: st[1], T: T, ex: ex, Y: Y, rows: rows, ratio: ratio, order: order, method: method };
  }
"""


def _order(cfg):
    mode = "order"
    found = dc.presets(cfg, KIT, mode)
    method = dc.choice(cfg, "method", ["euler", "heun", "rk4"], KIT, mode)
    cap = 32 if method == "rk4" else 64
    table = {}
    for p in found:
        t0, T = _pr(p, mode, "t0"), _pr(p, mode, "T")
        hs = _vec(p, mode, "hs", (3,))
        for h in hs:
            dc.check(KIT, mode, p, _F(h) > 0, "every h must be positive")
            steps = (_F(T) - _F(t0)) / _F(h)
            dc.check(KIT, mode, p, steps.denominator == 1 and 1 <= steps <= cap,
                     "(T - t0)/h = %s for h = %s must be a whole number from 1 to %d" % (steps, h, cap))
        table[str(p["id"])] = {
            "f": _pf(p, mode, "f", "ty"),
            "start": _join([t0, _pr(p, mode, "y0")]),
            "T": T,
            "exact": _txt(p, mode, "exact"),
            "hs": _join(hs),
        }
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Error at h₁", "odE1"), ("Error at h₂", "odE2"), ("Error at h₃", "odE3"),
             ("Ratios E(h₁)/E(h₂), E(h₂)/E(h₃)", "odRatio"), ("Observed order", "odOrder")]
    markup = (
        dc.toolbar("The order of a method", "halve h and watch the error",
                   [("green", "log₂ error against log₂ h")])
        + dc.wrap("odTable")
        + dc.stage(dc.svg("odPlot", "error against step size"))
        + dc.banner("odStatus")
    )
    controls = (
        dc.select("odPreset", "Equation", dc.options(found), pick["id"])
        + dc.text("odF", "f(t, y) in y' = f(t, y)", first["f"])
        + dc.text("odStart", "Start: t0 y0", first["start"])
        + dc.text("odT", "End T", first["T"])
        + dc.text("odExact", "Known solution y(t)", first["exact"])
        + dc.text("odHs", "Three step sizes", first["hs"])
        + dc.select("odMethod", "Method", [("euler", "Euler"), ("heun", "improved Euler"),
                                            ("rk4", "Runge–Kutta (RK4)")], method)
        + dc.kpis(tiles)
        + dc.hint("Each h must divide T − t0 into a whole number of steps: at most 64, or 32 for RK4.")
    )
    glue = dc.literal("ODP", table) + r"""
  var OD_TILES = ['odE1', 'odE2', 'odE3', 'odRatio', 'odOrder'];
  var odPresetIn = DE_el('odPreset'), odFIn = DE_el('odF'), odStartIn = DE_el('odStart'), odTIn = DE_el('odT');
  var odExactIn = DE_el('odExact'), odHsIn = DE_el('odHs'), odMethodIn = DE_el('odMethod');
  function odErrText(E) { return E.r ? DK_big(E.r) : DE_dec(E.x); }
  function odRender(r) {
    var i, rows = [], pts = [];
    DE_set('odE1', odErrText(r.rows[0].E));
    DE_set('odE2', odErrText(r.rows[1].E));
    DE_set('odE3', odErrText(r.rows[2].E));
    DE_set('odRatio', r.ratio);
    DE_set('odOrder', r.order);
    for (i = 0; i < 3; i += 1) {
      var w = r.rows[i];
      rows.push([DE_q(w.h), String(w.N), DK_big(w.yN), DK_atText(r.Y), odErrText(w.E)]);
      var ex = w.E.r ? DE_float(w.E.r) : w.E.x;
      if (ex > 0) pts.push([Math.log(DE_float(w.h)) / Math.LN2, Math.log(ex) / Math.LN2]);
    }
    DE_html('odTable', DK_table(OD_NAMES[r.method] + ' on y′ = ' + MPtext(r.f) + ' to T = ' + DE_q(r.T),
      ['h', 'N', 'y_N', 'y(T)', 'error'], rows, 2));
    if (pts.length >= 2) {
      var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
      var win = { xmin: Math.min.apply(null, xs) - 0.5, xmax: Math.max.apply(null, xs) + 0.5,
        ymin: Math.min.apply(null, ys) - 1, ymax: Math.max.apply(null, ys) + 1 };
      var plot = DK_plot('odPlot', win, 'log₂ of the error against log₂ of h');
      DE_polyline(plot, pts, 'plot-curve good');
      for (i = 0; i < pts.length; i += 1) plot.point(pts[i][0], pts[i][1], 'plot-point');
    } else DE_el('odPlot').textContent = '';
    var msg = (r.Y.r ? '<strong>Exact.</strong> ' : '<strong>Rounded.</strong> ') + DE_esc(OD_NAMES[r.method]) + ' on y′ = '
      + DE_esc(MPtext(r.f)) + ' from y(' + DE_esc(DE_q(r.t0)) + ') = ' + DE_esc(DE_q(r.y0)) + ' to T = ' + DE_esc(DE_q(r.T))
      + ', against y(T) = ' + DE_esc(DK_atText(r.Y)) + '.';
    if (!r.Y.r) msg += ' y(T) is irrational, so every error is rounded by the stated rule.';
    msg += ' The slope of the plotted line, log₂ of the error against log₂ of h, is the order.';
    DE_ok('odStatus', msg);
  }
  function redraw() {
    try {
      odRender(odCompute(odFIn.value, odStartIn.value, odTIn.value, odExactIn.value, odHsIn.value, odMethodIn.value));
    } catch (e) {
      DE_refuse('odStatus', OD_TILES, ['odTable', 'odPlot'], DE_msg(e));
    }
  }
  odPresetIn.addEventListener('change', function () {
    var p = ODP[odPresetIn.value];
    if (p) { odFIn.value = p.f; odStartIn.value = p.start; odTIn.value = p.T; odExactIn.value = p.exact; odHsIn.value = p.hs; }
    redraw();
  });
  [odFIn, odStartIn, odTIn, odExactIn, odHsIn].forEach(function (el) { el.addEventListener('input', redraw); });
  odMethodIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Order of a method", subtitle="Errors at h, h/2 and h/4, and their ratios",
        markup=markup, controls=controls,
        script=dc.script("MPOLY", "RF", "EP", "STEP", "DRAW", extra=_dk(closed=True) + ORDER_JS + glue),
        panel_title="Choose the equation and the steps",
        panel_intro="A method of order p divides its error by about 2ᵖ when h is halved. The errors here are "
                    "exact wherever the known solution is rational at T.",
        select="odPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# separable (sp)
# ---------------------------------------------------------------------------

SEPARABLE_JS = r"""
  /* ---- dekit/separable: g(y)·y′ = h(t), integrated on both sides -------
     G = ∫g and H = ∫h exactly (g a polynomial, or 1/y, or 1/y²), the
     constant from the initial value, the explicit branch the initial value
     selects, the interval it lives on, and the chain-rule check. */
  function spParseG(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/\s+/g, '');
    if (s === '1/y') return { kind: 'ln' };
    if (s === '1/y^2' || s === '1/(y^2)' || s === 'y^(-2)' || s === '1/y²') return { kind: 'inv2' };
    var p;
    try {
      p = MPtoPoly(MPparse(text, ['y']), 'y');
    } catch (e) {
      throw new Error('g must be a polynomial in y, or exactly 1/y or 1/y^2: ' + DE_msg(e));
    }
    if (!Pnorm(p).length) throw new Error('g is 0, so the equation says 0 = h(t)');
    return { kind: 'poly', g: Pnorm(p) };
  }
  /* The interval holding t0 on which the polynomial P is not 0. */
  function spInterval(P, t0) {
    var rr = DK_roots(P), lo = null, hi = null, x0 = DE_float(t0), i;
    if (rr.open) return '—';
    for (i = 0; i < rr.list.length; i += 1) {
      var x = rr.list[i], below = x.r ? Rcmp(x.r, t0) < 0 : x.x < x0;
      if (below) lo = x; else if (!hi) hi = x;
    }
    if (!lo && !hi) return 'all t';
    if (!lo) return 't < ' + hi.text;
    if (!hi) return 't > ' + lo.text;
    return lo.text + ' < t < ' + hi.text;
  }
  /* −1/K written as L/(−L·K), L clearing K's denominators, with the signs
     turned so that the denominator does not start with a minus. */
  function spRecip(K) {
    var L = 1n, i;
    for (i = 0; i < K.length; i += 1) L = L * K[i].d / bgcd(L, K[i].d);
    var D = Pscale(K, R(-L)), num = R(L);
    if (Pdeg(D) === 0) return DE_q(Rdiv(num, D[0]));
    var allNeg = true;
    for (i = 0; i < D.length; i += 1) if (D[i] && Rsign(D[i]) > 0) allNeg = false;
    if (allNeg) { D = Pscale(D, R(-1n)); num = Rneg(num); }
    var dt = DK_ptext(D, 't');
    if (!(dt === 't' || /^t[⁰¹²³⁴⁵⁶⁷⁸⁹]+$/.test(dt))) dt = '(' + dt + ')';
    return DE_q(num) + '/' + dt;
  }
  function spPoly(out, g, H, h, ic) {
    var G = Pintegral(g.g), deg = Pdeg(G), ok = true;
    out.Gtext = DE_ptext(G, 'y');
    ok = Pzero(Psub(Pderiv(G), g.g));
    out.checks.push('G′(y) = ' + DE_ptext(Pderiv(G), 'y') + ' = g(y)');
    if (!ic) {
      out.C = '—';
      out.implicit = out.Gtext + ' = ' + DE_ptext(H, 't') + ' + C';
      out.explicit = deg === 1 ? 'y = ' + DE_ptext(Pscale(H, Rinv(G[1])), 't') + ' + C' : 'implicit only';
      out.domain = deg === 1 ? 'all t' : '—';
      return ok;
    }
    var t0 = ic[0], y0 = ic[1];
    var C = Rsub(Peval(G, y0), Peval(H, t0)), K = Padd(H, [C]), s = Rinv(Plead(G));
    out.C = DE_q(C);
    out.implicit = DE_ptext(Pscale(G, s), 'y') + ' = ' + DK_ptext(Pscale(K, s), 't');
    if (deg === 1) {
      var Yp = Pscale(K, Rinv(G[1])), comp = [], j;
      out.explicit = 'y = ' + DK_ptext(Yp, 't');
      out.domain = 'all t';
      out.draw = function (x) { return DK_pf(Yp, x); };
      for (j = G.length - 1; j >= 0; j -= 1) comp = Padd(Pmul(comp, Yp), [G[j] || R0]);
      out.checks.push('d/dt G(y(t)) = ' + DE_ptext(Pderiv(comp), 't'));
      return ok && Pzero(Psub(Pderiv(comp), h));
    }
    if (deg !== 2) {
      out.explicit = 'implicit only';
      out.domain = '—';
      out.checks.push('differentiating ' + out.implicit + ' gives g(y)·y′ = h(t), the equation');
      return ok;
    }
    /* a·y² + b·y = K(t): y = p ± √Q with p = −b/(2a), Q = K/a + p² */
    var a = G[2], b = G[1] || R0, p = Rdiv(Rneg(b), Rmul(R(2n), a));
    var Q = Padd(Pscale(K, Rinv(a)), [Rmul(p, p)]), side = Rcmp(y0, p), Qt = DK_ptext(Q, 't');
    if (side === 0) {
      out.explicit = 'implicit only';
      out.domain = '—';
      out.note = ' y0 = ' + DE_q(y0) + ' is where the two branches meet, and neither is differentiable there.';
      return ok;
    }
    var sg = side > 0 ? 1 : -1, rs = Pdeg(Q) === 0 ? Rsqrt(Q[0] || R0) : null, root;
    if (rs !== null) root = DE_q(Radd(p, sg > 0 ? rs : Rneg(rs)));
    else {
      root = '√(' + Qt + ')';
      root = Rzero(p) ? (sg > 0 ? '' : '−') + root : DE_q(p) + (sg > 0 ? ' + ' : ' − ') + root;
    }
    out.explicit = 'y = ' + root;
    out.domain = Pdeg(Q) === 0 ? 'all t' : spInterval(Q, t0);
    out.draw = function (x) { var q = DK_pf(Q, x); return q > 0 ? DE_float(p) + sg * Math.sqrt(q) : NaN; };
    /* g(y) = 2a·y + b = (2a·p + b) ± 2a·√Q and y′ = ±Q′/(2√Q); with
       2a·p + b = 0 the product is a·Q′, whatever the branch */
    var A = Radd(Rmul(Rmul(R(2n), a), p), b), aQ = Pscale(Pderiv(Q), a);
    out.checks.push('y = ' + DE_q(p) + ' ± √Q(t), Q(t) = ' + Qt + ': g(y)·y′ = ' + DE_q(a) + '·Q′(t) = ' + DE_ptext(aQ, 't'));
    return ok && Rzero(A) && Pzero(Psub(aQ, h));
  }
  function spCompute(gText, hText, icText) {
    var g = spParseG(gText);
    var h;
    try { h = Pnorm(MPtoPoly(MPparse(hText, ['t']), 't')); } catch (e) { throw new Error('h must be a polynomial in t: ' + DE_msg(e)); }
    var ic = DK_list(icText, null, 'the initial value');
    if (ic.length && ic.length !== 2) throw new Error('the initial value is t0 y0, or nothing');
    var H = Pintegral(h), out = { g: g, h: h, H: H, ic: ic.length ? ic : null, checks: [], note: '' };
    out.Htext = DE_ptext(H, 't');
    var ok = Pzero(Psub(Pderiv(H), h));
    out.checks.push('H′(t) = ' + DE_ptext(Pderiv(H), 't') + ' = h(t)');
    if (g.kind === 'poly') ok = spPoly(out, g, H, h, out.ic) && ok;
    else if (g.kind === 'inv2') {
      out.Gtext = '−1/y';
      out.checks.push('d/dy(−1/y) = 1/y² = g(y)');
      if (!ic.length) {
        out.C = '—';
        out.implicit = '−1/y = ' + DE_ptext(H, 't') + ' + C';
        out.explicit = 'y = −1/(' + DE_ptext(H, 't') + ' + C)';
        out.domain = '—';
      } else {
        if (Rzero(ic[1])) throw new Error('g = 1/y² is undefined at y0 = 0');
        var C2 = Rsub(Rneg(Rinv(ic[1])), Peval(H, ic[0])), K2 = Padd(H, [C2]);
        out.C = DE_q(C2);
        out.implicit = '−1/y = ' + DK_ptext(K2, 't');
        out.explicit = 'y = ' + spRecip(K2);
        out.domain = Pdeg(K2) === 0 ? 'all t' : spInterval(K2, ic[0]);
        out.draw = function (x) { return -1 / DK_pf(K2, x); };
        var back = RFdiv(RFconst(R(-1n)), RFmake([R(-1n)], K2));
        ok = ok && RFequal(RFderiv(back), RFpoly(h));
        out.checks.push('−1/y(t) = ' + DK_ptext(K2, 't') + ', whose derivative is ' + RFtext(RFderiv(back), 't'));
      }
    } else {
      out.Gtext = 'ln|y|';
      out.checks.push('d/dy ln|y| = 1/y = g(y)');
      if (!ic.length) {
        out.C = '—';
        out.implicit = 'ln|y| = ' + DE_ptext(H, 't') + ' + C';
        out.explicit = 'y = C·e^(' + DE_ptext(H, 't') + ')';
        out.domain = 'all t';
      } else {
        var y0 = ic[1];
        if (Rzero(y0)) throw new Error('g = 1/y is undefined at y0 = 0');
        var Ht0 = Peval(H, ic[0]), E = Psub(H, [Ht0]), ay = Rabs(y0);
        var lnPart = Requ(ay, R1) ? '' : 'ln ' + DE_q(ay);
        out.C = Rzero(Ht0) ? (lnPart || '0') : (lnPart ? lnPart + (Rsign(Ht0) > 0 ? ' − ' : ' + ') + DE_q(Rabs(Ht0)) : DE_q(Rneg(Ht0)));
        var Et = DK_ptext(E, 't'), rhs = Et === '0' ? '' : Et;
        out.implicit = 'ln|y| = ' + (rhs && lnPart ? rhs + ' + ' + lnPart : (rhs || lnPart || '0'));
        var expo = Et === '0' ? '' : (Et === 't' ? 'e^t' : 'e^(' + Et + ')');
        out.explicit = 'y = ' + (expo ? DE_sum([{ c: y0, body: expo, dot: true }]) : DE_q(y0));
        out.domain = 'all t';
        out.draw = function (x) { return DE_float(y0) * Math.exp(DK_pf(E, x)); };
        ok = ok && Pzero(Psub(Pderiv(E), h));
        out.checks.push('ln|y(t)| = ' + (rhs || '0') + (lnPart ? ' + ' + lnPart : '') + ', whose derivative is ' + DE_ptext(Pderiv(E), 't'));
      }
    }
    out.check = ok ? 'equal' : 'differ';
    return out;
  }
"""


def _separable(cfg):
    mode = "separable"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        g = _txt(p, mode, "g", allowed="0123456789+-*/^(). y")
        ic = _vec(p, mode, "ic", (2,), allow_none=True)
        table[str(p["id"])] = {"g": g, "h": _pf(p, mode, "h", "t"), "ic": _join(ic) if ic else ""}
    view = dc.choice(cfg, "view", ["solve", "check"], KIT, mode)
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("G(y) = ∫g dy", "spG"), ("H(t) = ∫h dt", "spH"), ("Constant C", "spC"),
             ("Implicit solution", "spImplicit"), ("Explicit solution", "spExplicit"),
             ("Where it exists", "spDomain"), ("Chain-rule check", "spCheck")]
    markup = (
        dc.toolbar("Separable equations", "∫g(y) dy = ∫h(t) dt, exactly",
                   [("cyan", "the solution, drawn"), ("amber", "the initial value")])
        + dc.stage(dc.svg("spPlot", "the solution curve"))
        + dc.wrap("spTable")
        + dc.banner("spStatus")
    )
    controls = (
        dc.select("spPreset", "Equation g(y)·y' = h(t)", dc.options(found), pick["id"])
        + dc.text("spGIn", "g(y)", first["g"])
        + dc.text("spHIn", "h(t)", first["h"])
        + dc.text("spIC", "Initial value: t0 y0 (may be empty)", first["ic"])
        + dc.select("spView", "Show", [("solve", "the solution"), ("check", "the chain-rule check")], view)
        + dc.kpis(tiles)
        + dc.hint("g is a polynomial in y, or exactly 1/y or 1/y^2; h is a polynomial in t.")
    )
    glue = dc.literal("SPP", table) + r"""
  var SP_TILES = ['spG', 'spH', 'spC', 'spImplicit', 'spExplicit', 'spDomain', 'spCheck'];
  var spPresetIn = DE_el('spPreset'), spGIn = DE_el('spGIn'), spHIn = DE_el('spHIn'), spICIn = DE_el('spIC');
  var spViewIn = DE_el('spView');
  function spRender(r) {
    DE_set('spG', r.Gtext);
    DE_set('spH', r.Htext);
    DE_set('spC', r.C);
    DE_set('spImplicit', r.implicit);
    DE_set('spExplicit', r.explicit);
    DE_set('spDomain', r.domain);
    DE_set('spCheck', r.check);
    var i, rows = [];
    if (spViewIn.value === 'check') {
      for (i = 0; i < r.checks.length; i += 1) rows.push([r.checks[i]]);
      DE_html('spTable', DK_table('Differentiating gives back the equation: ' + r.check, ['step'], rows, -1));
    } else {
      rows.push(['∫g(y) dy', r.Gtext], ['∫h(t) dt', r.Htext], ['C', r.C], ['implicit', r.implicit], ['explicit', r.explicit], ['where', r.domain]);
      DE_html('spTable', DK_table('G(y) = H(t) + C', ['', ''], rows, -1));
    }
    var t0 = r.ic ? DE_float(r.ic[0]) : 0, lo = t0 - 3, hi = t0 + 3, fn = r.draw || null;
    if (!fn && r.ic) {
      var gk = r.g, hp = r.h;
      var pts = DE_rk4float(function (t, y) {
        var gy = gk.kind === 'poly' ? DK_pf(gk.g, y) : (gk.kind === 'ln' ? 1 / y : 1 / (y * y));
        return DK_pf(hp, t) / gy;
      }, [t0, DE_float(r.ic[1])], 3 / 400, 400);
      fn = function (x) {
        var j;
        for (j = 1; j < pts.length; j += 1) if (pts[j][0] >= x && pts[j - 1][0] <= x) return pts[j][1];
        return NaN;
      };
    }
    var plot = DK_plot('spPlot', DK_window(fn ? [fn] : [], lo, hi), 'the solution of the separable equation');
    if (fn) plot.curve(fn);
    if (r.ic) plot.point(t0, DE_float(r.ic[1]), 'plot-point', 'start');
    var msg = '<strong>Exact.</strong> ∫g(y) dy = ' + DE_esc(r.Gtext) + ' and ∫h(t) dt = ' + DE_esc(r.Htext) + ', so '
      + DE_esc(r.implicit) + '.';
    if (r.explicit !== 'implicit only') msg += ' Solved for y: ' + DE_esc(r.explicit) + (r.domain !== '—' ? ', for ' + DE_esc(r.domain) : '') + '.';
    else if (r.ic) msg += ' This relation is not solved for y here; the curve is drawn by stepping in floating point.';
    DE_ok('spStatus', msg + DE_esc(r.note));
  }
  function redraw() {
    try {
      spRender(spCompute(spGIn.value, spHIn.value, spICIn.value));
    } catch (e) {
      DE_refuse('spStatus', SP_TILES, ['spTable', 'spPlot'], DE_msg(e));
    }
  }
  spPresetIn.addEventListener('change', function () {
    var p = SPP[spPresetIn.value];
    if (p) { spGIn.value = p.g; spHIn.value = p.h; spICIn.value = p.ic; }
    redraw();
  });
  [spGIn, spHIn, spICIn].forEach(function (el) { el.addEventListener('input', redraw); });
  spViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Separable equations", subtitle="Both sides integrated exactly",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", "RF", "DRAW", extra=_dk(roots=True) + SEPARABLE_JS + glue),
        panel_title="Choose g and h",
        panel_intro="An equation g(y)·y′ = h(t) separates: the chain rule makes ∫g(y)·y′ dt the same as "
                    "∫g(y) dy. One initial value fixes the constant and the branch.",
        select="spPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# growth (gr)
# ---------------------------------------------------------------------------

GROWTH_JS = r"""
  /* ---- dekit/growth: y′ = k·(y − A) -----------------------------------------
     Euler's factor 1 + kh, the exact sequence yₙ = A + (y0 − A)(1 + kh)ⁿ
     checked against the recursion, the closed form rounded, the doubling
     time ln 2/|k| rounded, and the first step past a target. */
  function grCompute(kText, y0Text, AText, hText, n, targetText) {
    var k = DK_need(kText, 'k'), y0 = DK_need(y0Text, 'y0');
    var A = /\S/.test(String(AText || '')) ? DK_need(AText, 'A') : R0;
    if (Rzero(k)) throw new Error('k = 0 is not a growth equation: y′ = 0 keeps y constant');
    if (n < 1 || n > 64) throw new Error('n runs from 1 to 64');
    var h = DK_h(DK_need(hText, 'h'), R0, n);
    var target = /\S/.test(String(targetText || '')) ? DK_need(targetText, 'the target') : null;
    var factor = Radd(R1, Rmul(k, h)), seq = [y0], m;
    for (m = 1; m <= n; m += 1) {
      var prev = seq[m - 1], next = Radd(prev, Rmul(h, Rmul(k, Rsub(prev, A))));
      if (!Requ(next, Radd(A, Rmul(Rsub(y0, A), Rpow(factor, m))))) throw new Error('the recursion and the formula disagree at step ' + m);
      seq.push(next);
    }
    var tN = DE_float(Rmul(h, R(BigInt(n))));
    var truth = DE_float(A) + DE_float(Rsub(y0, A)) * Math.exp(DE_float(k) * tN);
    var hit = '—';
    if (target !== null) {
      var c = Rcmp(target, y0);
      hit = 'never within ' + n + ' steps';
      for (m = 0; m <= n; m += 1) {
        var d = Rcmp(seq[m], target);
        if (c === 0 || (c > 0 && d >= 0) || (c < 0 && d <= 0)) {
          hit = 'step ' + m + ' (t = ' + DE_q(Rmul(h, R(BigInt(m)))) + ')';
          break;
        }
      }
    }
    return {
      k: k, y0: y0, A: A, h: h, n: n, factor: factor, seq: seq, last: seq[n], truth: truth,
      error: Math.abs(truth - DE_float(seq[n])), T: Math.LN2 / Math.abs(DE_float(k)), hit: hit
    };
  }
"""


def _growth(cfg):
    mode = "growth"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        k, h = _pr(p, mode, "k"), _pr(p, mode, "h")
        dc.check(KIT, mode, p, _F(k) != 0, "k = 0 is not a growth equation")
        dc.check(KIT, mode, p, _F(h) > 0, "h must be positive")
        a = _pr(p, mode, "A", allow_none=True)
        table[str(p["id"])] = {
            "k": k, "y0": _pr(p, mode, "y0"), "A": a if a is not None else "0", "h": h,
            "n": _int(p, mode, "n", 1, 64),
            "target": _pr(p, mode, "target", allow_none=True) or "",
        }
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Euler factor 1 + kh", "grFactor"), ("Last yₙ (exact)", "grLast"), ("Closed form at tₙ", "grTrue"),
             ("Error", "grError"), ("Doubling time or half-life", "grT"), ("First step past the target", "grHit"),
             ("Steady state A", "grSteady")]
    markup = (
        dc.toolbar("Growth and decay", "y′ = k·(y − A)",
                   [("green", "Euler steps (exact)"), ("cyan", "closed form, rounded")])
        + dc.stage(dc.svg("grPlot", "Euler steps beside the closed form"))
        + dc.wrap("grTable")
        + dc.banner("grStatus")
    )
    controls = (
        dc.select("grPreset", "Situation", dc.options(found), pick["id"])
        + dc.text("grK", "Rate k", first["k"])
        + dc.text("grY0", "Start y0", first["y0"])
        + dc.text("grA", "Shift A (0 for pure growth or decay)", first["A"])
        + dc.text("grH", "Step h", first["h"])
        + dc.range_("grN", "Steps n", 1, 64, first["n"])
        + dc.text("grTarget", "Target (may be empty)", first["target"])
        + dc.kpis(tiles)
    )
    glue = dc.literal("GRP", table) + r"""
  var GR_TILES = ['grFactor', 'grLast', 'grTrue', 'grError', 'grT', 'grHit', 'grSteady'];
  var grPresetIn = DE_el('grPreset'), grKIn = DE_el('grK'), grY0In = DE_el('grY0'), grAIn = DE_el('grA');
  var grHIn = DE_el('grH'), grNIn = DE_el('grN'), grTargetIn = DE_el('grTarget');
  function grRender(r) {
    var i, rows = [], pts = [], up = Rsign(r.k) > 0;
    DE_set('grFactor', DE_q(r.factor));
    DE_set('grLast', DK_big(r.last));
    DE_set('grTrue', DE_dec(r.truth));
    DE_set('grError', DE_dec(r.error));
    DE_set('grT', DE_dec(r.T));
    DE_set('grHit', r.hit);
    DE_set('grSteady', DE_q(r.A) + (up ? ' (repelling)' : ''));
    var hf = DE_float(r.h), A = DE_float(r.A), c = DE_float(Rsub(r.y0, r.A)), kf = DE_float(r.k);
    for (i = 0; i < r.seq.length; i += 1) {
      rows.push([String(i), DE_q(Rmul(r.h, R(BigInt(i)))), DK_big(r.seq[i]), DE_dec(A + c * Math.exp(kf * hf * i))]);
      pts.push([hf * i, DE_float(r.seq[i])]);
    }
    DE_html('grTable', DK_table('yₙ = ' + DE_q(r.A) + ' + (' + DE_q(Rsub(r.y0, r.A)) + ')·(' + DE_q(r.factor) + ')ⁿ beside the closed form',
      ['n', 'tₙ', 'yₙ (exact)', 'closed form (rounded)'], rows, rows.length - 1));
    var fn = function (x) { return A + c * Math.exp(kf * x); };
    var plot = DK_plot('grPlot', DK_window([fn], 0, hf * r.n), 'Euler steps for y′ = k(y − A) beside the closed form');
    plot.curve(fn);
    DE_polyline(plot, pts, 'plot-curve good');
    if (A >= plot.win.ymin && A <= plot.win.ymax) plot.hline(A, 'plot-aux', 'A');
    var kt = DE_q(Rabs(r.k)), kd = Rint(Rabs(r.k)) ? kt : '(' + kt + ')';
    DE_ok('grStatus', '<strong>Exact.</strong> The factor is 1 + kh = ' + DE_esc(DE_q(r.factor)) + ', so yₙ = '
      + DE_esc(DE_q(r.A)) + ' + (' + DE_esc(DE_q(Rsub(r.y0, r.A))) + ')·(' + DE_esc(DE_q(r.factor)) + ')ⁿ, checked against the step-by-step recursion. '
      + (up ? 'Doubling' : 'Halving') + ' time ln 2/' + DE_esc(kd) + ' ' + DE_esc(DE_dec(r.T))
      + '; the closed form and the error are rounded by the stated rule.');
  }
  function redraw() {
    try {
      grRender(grCompute(grKIn.value, grY0In.value, grAIn.value, grHIn.value, DK_range('grN'), grTargetIn.value));
    } catch (e) {
      DE_refuse('grStatus', GR_TILES, ['grTable', 'grPlot'], DE_msg(e));
    }
  }
  grPresetIn.addEventListener('change', function () {
    var p = GRP[grPresetIn.value];
    if (p) {
      grKIn.value = p.k; grY0In.value = p.y0; grAIn.value = p.A; grHIn.value = p.h; grNIn.value = String(p.n);
      grTargetIn.value = p.target;
    }
    redraw();
  });
  [grKIn, grY0In, grAIn, grHIn, grNIn, grTargetIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Growth and decay", subtitle="A geometric sequence beside an exponential",
        markup=markup, controls=controls,
        script=dc.script("DRAW", extra=_dk() + GROWTH_JS + glue),
        panel_title="Choose the rate and the start",
        panel_intro="Euler's method on y′ = k·(y − A) multiplies the gap y − A by 1 + kh at every step. "
                    "The sequence is exact; the closed form needs e and is rounded.",
        select="grPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# autonomous (au)
# ---------------------------------------------------------------------------

AUTONOMOUS_JS = r"""
  /* ---- dekit/autonomous: the phase line of y′ = f(y) --------------------
     Equilibria exactly (rational, or a surd pair), the sign of f between
     them at exact test points, the type of each, f′ there, where each start
     goes, exact Euler steps to the budget, and the inflection levels: the
     rational roots of f′ where f′ changes sign and f is not 0. */
  function auInflect(f, fp) {
    var roots = DK_ratroots(fp), out = [], i;
    for (i = 0; i < roots.length; i += 1) {
      var r = roots[i], mult = 0, q = fp;
      while (Pdeg(q) > 0 && Rzero(Peval(q, r))) { q = Pdivmod(q, [Rneg(r), R1]).q; mult += 1; }
      if (mult % 2 === 1 && !Rzero(Peval(f, r))) out.push('y = ' + DE_q(r));
    }
    if (out.length) return out.join(', ');
    if (Pdeg(fp) < 1) return 'none';
    var all = DK_roots(fp);
    return (all.open || all.list.length > roots.length) ? 'none rational' : 'none';
  }
  function auCompute(fText, startsText, hText, n) {
    var fm = MPparse(fText, ['y'], { degree: 4, terms: 24 });
    var f = Pnorm(MPtoPoly(fm, 'y'));
    var starts = DK_list(startsText, null, 'the starts');
    if (!starts.length || starts.length > 6) throw new Error('type from 1 to 6 starting values');
    if (n < 1 || n > 64) throw new Error('n runs from 1 to 64');
    var h = DK_h(DK_need(hText, 'h'), R0, n);
    var ph = DK_phase(f), runs = [], i;
    for (i = 0; i < starts.length; i += 1) runs.push(DE_euler(fm, R0, starts[i], h, n));
    return { fm: fm, f: f, ph: ph, starts: starts, h: h, n: n, runs: runs, inflect: auInflect(f, ph.fp) };
  }
  function auStepsText(run) {
    var k = run.steps;
    return k + (k === 1 ? ' exact step' : ' exact steps') + (run.stopped ? ', then digit budget' : '');
  }
"""


def _autonomous(cfg):
    mode = "autonomous"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        h = _pr(p, mode, "h")
        dc.check(KIT, mode, p, _F(h) > 0, "h must be positive")
        starts = p.get("starts")
        dc.check(KIT, mode, p, isinstance(starts, (list, tuple)) and 1 <= len(starts) <= 6,
                 "starts must be a list of 1 to 6 rationals")
        win = _vec(p, mode, "window", (3,))
        dc.check(KIT, mode, p, _F(win[0]) > 0 and _F(win[1]) < _F(win[2]),
                 "window is [tmax, ymin, ymax] with tmax > 0 and ymin < ymax")
        table[str(p["id"])] = {
            "f": _pf(p, mode, "f", "y"),
            "starts": _join([dc.rational(s, KIT, mode, p, "starts") for s in starts]),
            "h": h,
            "n": _int(p, mode, "n", 1, 64),
            "window": [float(_F(w)) for w in win],
        }
    view = dc.choice(cfg, "view", ["line", "steps", "curves"], KIT, mode)
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Equilibria", "auEquil"), ("Types", "auTypes"), ("f′ at each", "auSlope"),
             ("The first start goes", "auLimit"), ("Exact Euler steps, first start", "auSteps"),
             ("Inflection levels", "auInflect")]
    markup = (
        dc.toolbar("Autonomous equations", "y′ = f(y): the sign of f decides the direction",
                   [("green", "exact Euler steps"), ("purple", "curves drawn by stepping in floating point"),
                    ("cyan", "phase line")])
        + dc.stage(dc.svg("auPlot", "the phase line"))
        + dc.wrap("auTable")
        + dc.banner("auStatus")
    )
    controls = (
        dc.select("auPreset", "Equation", dc.options(found), pick["id"])
        + dc.text("auF", "f(y) in y' = f(y)", first["f"])
        + dc.text("auStarts", "Starting values y(0)", first["starts"])
        + dc.text("auH", "Step h", first["h"])
        + dc.range_("auN", "Steps n", 1, 64, first["n"])
        + dc.select("auView", "Show", [("line", "the phase line"), ("steps", "exact Euler steps"),
                                        ("curves", "solution curves")], view)
        + dc.kpis(tiles)
        + dc.hint("f is a polynomial in y of degree 4 at most: y^2 - 1, y(1 - y/4), y^3 - 4y^2 + 3y.")
    )
    glue = dc.literal("AUP", table) + r"""
  var AU_TILES = ['auEquil', 'auTypes', 'auSlope', 'auLimit', 'auSteps', 'auInflect'];
  var auPresetIn = DE_el('auPreset'), auFIn = DE_el('auF'), auStartsIn = DE_el('auStarts'), auHIn = DE_el('auH');
  var auNIn = DE_el('auN'), auViewIn = DE_el('auView');
  var auWin = (AUP[auPresetIn.value] || { window: [6, -2, 6] }).window;
  function auArrow(svg, x, y, dir) {
    svg.appendChild(svgel('polygon', { class: 'plot-end closed',
      points: (x + 7 * dir) + ',' + y + ' ' + (x - 5 * dir) + ',' + (y - 6) + ' ' + (x - 5 * dir) + ',' + (y + 6) }));
  }
  function auLine(r) {
    var ph = r.ph, L = ph.list, lo = auWin[1], hi = auWin[2], i;
    for (i = 0; i < L.length; i += 1) { lo = Math.min(lo, L[i].x - 1); hi = Math.max(hi, L[i].x + 1); }
    var svg = DE_el('auPlot'), nl = NumberLine(svg, lo, hi), cuts = [lo];
    for (i = 0; i < L.length; i += 1) cuts.push(L[i].x);
    cuts.push(hi);
    for (i = 0; i + 1 < cuts.length; i += 1) {
      if (ph.signs[i]) auArrow(svg, nl.sx((cuts[i] + cuts[i + 1]) / 2), 44, ph.signs[i] > 0 ? 1 : -1);
    }
    for (i = 0; i < L.length; i += 1) nl.point(L[i].x, ph.types[i] === 'stable');
    nl.describe('phase line of y′ = ' + DE_ptext(r.f, 'y') + ': ' + DK_typesText(ph));
  }
  function auPlane(r, curves) {
    var L = r.ph.list, i, j;
    var plot = DK_plot('auPlot', { xmin: 0, xmax: auWin[0], ymin: auWin[1], ymax: auWin[2] }, 'solutions of y′ = ' + DE_ptext(r.f, 'y'));
    for (i = 0; i < L.length; i += 1) plot.hline(L[i].x, 'plot-aux', L[i].text);
    for (i = 0; i < r.runs.length; i += 1) {
      var pts = [];
      for (j = 0; j < r.runs[i].rows.length; j += 1) pts.push([DE_float(r.runs[i].rows[j].t), DE_float(r.runs[i].rows[j].y)]);
      if (curves) {
        DE_polyline(plot, DE_rk4float(function (t, y) { return DK_pf(r.f, y); }, [0, DE_float(r.starts[i])], auWin[0] / 400, 400), 'plot-curve alt');
        pts = pts.slice(0, 4);
      }
      DE_polyline(plot, pts, 'plot-curve good');
      plot.point(0, DE_float(r.starts[i]), 'plot-point');
    }
  }
  function auRender(r) {
    var ph = r.ph, i, L = ph.list, sl = [], rows = [];
    DE_set('auEquil', DK_eqText(ph.rr));
    DE_set('auTypes', DK_typesText(ph));
    for (i = 0; i < L.length; i += 1) sl.push('f′(' + L[i].text + ') = ' + ph.slopes[i]);
    DE_set('auSlope', sl.length ? sl.join('; ') : '—');
    DE_set('auLimit', DK_limit(ph, r.starts[0]));
    DE_set('auSteps', auStepsText(r.runs[0]));
    DE_set('auInflect', r.inflect);
    for (i = 0; i < r.starts.length; i += 1) {
      var run = r.runs[i];
      rows.push([DE_q(r.starts[i]), DK_limit(ph, r.starts[i]), run.rows.length > 1 ? DK_big(run.rows[1].y) : '—',
        DK_big(run.rows[run.rows.length - 1].y), auStepsText(run)]);
    }
    DE_html('auTable', DK_table('y′ = ' + DE_ptext(r.f, 'y') + ', exact Euler steps with h = ' + DE_q(r.h),
      ['y(0)', 'goes', 'y₁', 'last yₙ', 'steps'], rows, -1));
    if (auViewIn.value === 'line') auLine(r); else auPlane(r, auViewIn.value === 'curves');
    var msg = '<strong>Exact.</strong> y′ = ' + DE_esc(DE_ptext(r.f, 'y')) + ': equilibria ' + DE_esc(DK_eqText(ph.rr))
      + '. The sign of f, tested exactly at ' + ph.tests.map(function (t) { return DE_esc(DE_q(t)); }).join(', ')
      + ', is ' + ph.signs.map(function (s) { return s > 0 ? '+' : (s < 0 ? '−' : '0'); }).join(', ') + '.';
    var surd = L.filter(function (x) { return !x.r; });
    if (surd.length) msg += ' Rounded: ' + surd.map(function (x) { return DE_esc(x.text) + ' ' + DE_esc(DE_dec(x.x)); }).join('; ') + '.';
    if (r.runs[0].stopped) msg += ' The Euler steps stop at the budget of ' + DE_DIGITS + ' digits: a quadratic right-hand side doubles the digits each step.';
    if (auViewIn.value === 'curves') msg += ' The purple curves are drawn by stepping in floating point.';
    DE_ok('auStatus', msg);
  }
  function redraw() {
    try {
      auRender(auCompute(auFIn.value, auStartsIn.value, auHIn.value, DK_range('auN')));
    } catch (e) {
      DE_refuse('auStatus', AU_TILES, ['auTable', 'auPlot'], DE_msg(e));
    }
  }
  auPresetIn.addEventListener('change', function () {
    var p = AUP[auPresetIn.value];
    if (p) { auFIn.value = p.f; auStartsIn.value = p.starts; auHIn.value = p.h; auNIn.value = String(p.n); auWin = p.window; }
    redraw();
  });
  [auFIn, auStartsIn, auHIn, auNIn].forEach(function (el) { el.addEventListener('input', redraw); });
  auViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Autonomous equations", subtitle="Equilibria, the phase line, and where solutions go",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", "STEP", "DRAW", extra=_dk(roots=True) + AUTONOMOUS_JS + glue),
        panel_title="Choose f",
        panel_intro="When the right-hand side has no t, the sign of f(y) alone says which way every solution "
                    "moves. Equilibria are the exact roots of f.",
        select="auPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# bifurcate (bf)
# ---------------------------------------------------------------------------

BIFURCATE_JS = r"""
  /* ---- dekit/bifurcate: equilibria of y′ = f(y, a) against a ------------
     At the chosen a, the phase line exactly. The critical values, where two
     equilibria meet, are the rational roots of the discriminant of f in y:
     the Sylvester resultant Res_y(f, ∂f/∂y) divided exactly by the leading
     coefficient. */
  function bfCoeffs(fm) {
    var cs = [], i, yi = fm.vars.indexOf('y'), ai = fm.vars.indexOf('a');
    for (i = 0; i < fm.terms.length; i += 1) {
      var e = fm.terms[i].e, j = yi < 0 ? 0 : e[yi], k = ai < 0 ? 0 : e[ai], mono = [];
      while (cs.length <= j) cs.push([]);
      while (mono.length < k) mono.push(R0);
      mono.push(fm.terms[i].c);
      cs[j] = Padd(cs[j], mono);
    }
    return cs.map(Pnorm);
  }
  function bfDet(M) {
    var n = M.length, out = [], j;
    if (n === 1) return Pnorm(M[0][0]);
    for (j = 0; j < n; j += 1) {
      if (!Pnorm(M[0][j]).length) continue;
      var minor = [], i;
      for (i = 1; i < n; i += 1) minor.push(M[i].slice(0, j).concat(M[i].slice(j + 1)));
      var term = Pmul(M[0][j], bfDet(minor));
      out = j % 2 ? Psub(out, term) : Padd(out, term);
    }
    return Pnorm(out);
  }
  /* The discriminant of Σ cs[j]·yʲ (coefficients polynomials in a), up to
     its sign, which does not move its roots. */
  function bfDisc(cs) {
    var n = cs.length - 1, m = n - 1, size = 2 * n - 1, ds = [], M = [], i, j;
    for (j = 1; j <= n; j += 1) ds.push(Pscale(cs[j], R(BigInt(j))));
    for (i = 0; i < m; i += 1) {
      var row = [];
      for (j = 0; j < size; j += 1) row.push(j - i >= 0 && j - i <= n ? cs[n - (j - i)] : []);
      M.push(row);
    }
    for (i = 0; i < n; i += 1) {
      var row2 = [];
      for (j = 0; j < size; j += 1) row2.push(j - i >= 0 && j - i <= m ? ds[m - (j - i)] : []);
      M.push(row2);
    }
    var dm = Pdivmod(bfDet(M), cs[n]);
    if (!Pzero(dm.r)) throw new Error('the resultant is not divisible by the leading coefficient');
    return Pnorm(dm.q);
  }
  function bfCompute(fText, aText, rangeText) {
    var fm = MPparse(fText, ['y', 'a']);
    var a = DK_need(aText, 'a');
    var rg = DK_list(rangeText, 2, 'the range');
    if (Rcmp(rg[0], rg[1]) >= 0) throw new Error('the range is amin amax with amin < amax');
    var cs = bfCoeffs(fm), n = cs.length - 1, i, crit = [];
    if (n < 1) throw new Error('f has no y in it, so it has no equilibria to follow');
    if (n > 3) throw new Error('f has degree ' + n + ' in y; this lab takes degree 3 at most');
    var D = n === 1 ? Pnorm(cs[1]) : bfDisc(cs), every = !D.length;
    if (!every && Pdeg(D) >= 1) {
      var rts = DK_ratroots(D);
      for (i = 0; i < rts.length; i += 1) if (Rcmp(rts[i], rg[0]) >= 0 && Rcmp(rts[i], rg[1]) <= 0) crit.push('a = ' + DE_q(rts[i]));
    }
    var fy = [];
    for (i = 0; i <= n; i += 1) fy.push(Peval(cs[i], a));
    fy = Pnorm(fy);
    if (!fy.length) throw new Error('at a = ' + DE_q(a) + ', f is 0 for every y');
    var critText = every ? 'every a' : (crit.length ? crit.join(', ') : 'none rational in [' + DE_q(rg[0]) + ', ' + DE_q(rg[1]) + ']');
    return { fm: fm, cs: cs, n: n, a: a, rg: rg, ph: DK_phase(fy), crit: critText, D: D };
  }
  /* Float roots at a, for the drawing only: sign changes on a fine grid. */
  function bfFloatRoots(cs, a, ylo, yhi) {
    var c = [], i, out = [];
    for (i = 0; i < cs.length; i += 1) c.push(DK_pf(cs[i], a));
    var f = function (y) { var v = 0, k; for (k = c.length - 1; k >= 0; k -= 1) v = v * y + c[k]; return v; };
    var fy = function (y) { var v = 0, k; for (k = c.length - 1; k >= 1; k -= 1) v = v * y + k * c[k]; return v; };
    var steps = 600, prev = f(ylo);
    for (i = 1; i <= steps; i += 1) {
      var y = ylo + (yhi - ylo) * i / steps, cur = f(y);
      if (prev === 0 || (prev < 0) !== (cur < 0)) {
        var lo = y - (yhi - ylo) / steps, hi = y, it, m;
        for (it = 0; it < 50; it += 1) { m = (lo + hi) / 2; if ((f(lo) < 0) !== (f(m) < 0)) hi = m; else lo = m; }
        out.push({ y: (lo + hi) / 2, stable: fy((lo + hi) / 2) < 0 });
      }
      prev = cur;
    }
    return out;
  }
"""


def _bifurcate(cfg):
    mode = "bifurcate"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        rg = _vec(p, mode, "range", (2,))
        dc.check(KIT, mode, p, _F(rg[0]) < _F(rg[1]), "range is [amin, amax] with amin < amax")
        table[str(p["id"])] = {"f": _pf(p, mode, "f", "ay"), "a": _pr(p, mode, "a"), "range": _join(rg)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Equilibria at this a", "bfEquil"), ("Types", "bfTypes"), ("How many", "bfCount"),
             ("Critical values of a", "bfCritical")]
    markup = (
        dc.toolbar("Bifurcations", "equilibria of y′ = f(y, a) as a moves",
                   [("green", "stable (solid)"), ("muted", "unstable (dashed)"), ("amber", "the chosen a")])
        + dc.stage(dc.svg("bfPlot", "the bifurcation diagram"))
        + dc.banner("bfStatus")
    )
    controls = (
        dc.select("bfPreset", "Family", dc.options(found), pick["id"])
        + dc.text("bfF", "f(y, a) in y' = f(y, a)", first["f"])
        + dc.text("bfA", "Parameter a", first["a"])
        + dc.text("bfRange", "Range of a: amin amax", first["range"])
        + dc.kpis(tiles)
        + dc.hint("f is a polynomial in y and a, of degree 3 at most in y: a + y^2, a y - y^3, a y - y^2.")
    )
    glue = dc.literal("BFP", table) + r"""
  var BF_TILES = ['bfEquil', 'bfTypes', 'bfCount', 'bfCritical'];
  var bfPresetIn = DE_el('bfPreset'), bfFIn = DE_el('bfF'), bfAIn = DE_el('bfA'), bfRangeIn = DE_el('bfRange');
  function bfDraw(r) {
    var ph = r.ph, amin = DE_float(r.rg[0]), amax = DE_float(r.rg[1]), cols = [], ybound = 1, i, j, k;
    for (i = 0; i <= 60; i += 1) {
      var av = amin + (amax - amin) * i / 60, c = [], big = 0;
      for (j = 0; j < r.cs.length; j += 1) c.push(DK_pf(r.cs[j], av));
      var lead = Math.abs(c[c.length - 1]);
      if (lead > 1e-12) for (j = 0; j < c.length - 1; j += 1) big = Math.max(big, Math.abs(c[j]) / lead);
      ybound = Math.max(ybound, Math.min(1 + big, 50));
    }
    for (i = 0; i < ph.list.length; i += 1) ybound = Math.max(ybound, Math.abs(ph.list[i].x) + 1);
    for (i = 0; i <= 60; i += 1) {
      var aa = amin + (amax - amin) * i / 60;
      cols.push({ a: aa, roots: bfFloatRoots(r.cs, aa, -ybound, ybound) });
    }
    var plot = DK_plot('bfPlot', { xmin: amin, xmax: amax, ymin: -ybound * 1.1, ymax: ybound * 1.1 }, 'equilibria of y′ = f(y, a) against a');
    var gap = 0.2 * ybound;
    for (i = 0; i + 1 < cols.length; i += 1) {
      for (k = 0; k < cols[i].roots.length; k += 1) {
        var p = cols[i].roots[k], best = null;
        for (j = 0; j < cols[i + 1].roots.length; j += 1) {
          var cand = cols[i + 1].roots[j], d = Math.abs(cand.y - p.y);
          if (cand.stable === p.stable && d < gap && (!best || d < Math.abs(best.y - p.y))) best = cand;
        }
        if (best) plot.segment(cols[i].a, p.y, cols[i + 1].a, best.y, p.stable ? 'plot-curve good' : 'plot-curve parent');
      }
    }
    var af = DE_float(r.a);
    plot.vline(af, 'plot-aux', 'a = ' + DE_q(r.a));
    for (i = 0; i < ph.list.length; i += 1) plot.point(af, ph.list[i].x, 'plot-point');
  }
  function bfRender(r) {
    var ph = r.ph, count = ph.list.length;
    DE_set('bfEquil', DK_eqText(ph.rr));
    DE_set('bfTypes', DK_typesText(ph));
    DE_set('bfCount', count === 0 ? 'no equilibria' : (count === 1 ? '1 equilibrium' : count + ' equilibria'));
    DE_set('bfCritical', r.crit);
    bfDraw(r);
    var msg = '<strong>Exact.</strong> At a = ' + DE_esc(DE_q(r.a)) + ', y′ = ' + DE_esc(DE_ptext(ph.f, 'y')) + ': equilibria '
      + DE_esc(DK_eqText(ph.rr)) + '. Two equilibria meet where f and ∂f/∂y vanish together; '
      + (r.n === 1 ? 'for an f of degree 1 in y that is where the coefficient of y, ' + DE_esc(DE_ptext(r.D, 'a')) + ', is 0'
        : 'the discriminant in y is a multiple of ' + DE_esc(DE_ptext(r.D, 'a')))
      + '. The diagram is drawn from floating-point roots.';
    var surd = ph.list.filter(function (x) { return !x.r; });
    if (surd.length) msg += ' Rounded: ' + surd.map(function (x) { return DE_esc(x.text) + ' ' + DE_esc(DE_dec(x.x)); }).join('; ') + '.';
    DE_ok('bfStatus', msg);
  }
  function redraw() {
    try {
      bfRender(bfCompute(bfFIn.value, bfAIn.value, bfRangeIn.value));
    } catch (e) {
      DE_refuse('bfStatus', BF_TILES, ['bfPlot'], DE_msg(e));
    }
  }
  bfPresetIn.addEventListener('change', function () {
    var p = BFP[bfPresetIn.value];
    if (p) { bfFIn.value = p.f; bfAIn.value = p.a; bfRangeIn.value = p.range; }
    redraw();
  });
  [bfFIn, bfAIn, bfRangeIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Bifurcations", subtitle="Where equilibria are born and meet",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", "DRAW", extra=_dk(roots=True) + BIFURCATE_JS + glue),
        panel_title="Choose the family and the parameter",
        panel_intro="Equilibria are the roots of f(·, a). As a moves they move, and where two meet the number "
                    "of equilibria changes.",
        select="bfPreset", presets=found,
    )


# ---------------------------------------------------------------------------

MODES = {
    "verify": _verify,
    "field": _field,
    "euler": _euler,
    "order": _order,
    "separable": _separable,
    "growth": _growth,
    "autonomous": _autonomous,
    "bifurcate": _bifurcate,
}

# Each mode's own pure-function block, for scripts/mathcheck.js and the tests.
MODE_JS = {
    "verify": VERIFY_JS,
    "field": FIELD_JS,
    "euler": EULER_JS,
    "order": ORDER_JS,
    "separable": SEPARABLE_JS,
    "growth": GROWTH_JS,
    "autonomous": AUTONOMOUS_JS,
    "bifurcate": BIFURCATE_JS,
}


def dekit_lab(cfg):
    """The differential-equations kit. `cfg["mode"]` chooses the mode; an
    unknown one raises."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    build = MODES.get(mode) or dekit_b.MODES.get(mode)
    if build is None:
        raise ValueError("dekit has no mode %r yet: docs/differential-equations/PLAN.md section D.3" % (mode,))
    return build(cfg)


__all__ = ["dekit_lab", "MODES", "MODE_JS", "DK_JS", "DK_BASE_JS", "DK_ROOTS_JS", "DK_CLOSED_JS"]
