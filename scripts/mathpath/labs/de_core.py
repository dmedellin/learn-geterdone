"""Shared exact-arithmetic, printing and drawing blocks for calckit and dekit.

Specified in docs/differential-equations/PLAN.md sections D.0 and D.1. This
module is not a lab: it holds JavaScript blocks, a Python assembler that puts
the blocks a mode needs on its page in dependency order, and the markup and
preset helpers both kits share. algebra_core is frontier-tier shared code and
is not edited; these blocks sit BESIDE it.

THE PYTHON API (what calckit.py and dekit.py import)

  script(*names, extra='')   the page script: algebra_core's RATIONAL_JS,
                             POLY_JS, EXPR_JS and PLOT_JS always, SURD_JS when
                             'SURD' is named, then SHOW_JS and every de_core
                             block named (with the blocks they depend on), in
                             dependency order, each exactly once, then `extra`
                             (the mode's own block). Names: 'SURD', 'MPOLY',
                             'RF', 'EP', 'STEP', 'DRAW' ('SHOW' is implied).
  BLOCKS, DEPENDS            name -> JavaScript, and name -> the names it needs
  literal(name, value)       `var name = <value>;` as a JS literal written with
                             single quotes only. Never a double quote: the
                             copy-contract lexers pair quotes across a page.
  js(value)                  the literal alone
  attr(text)                 HTML attribute escape
  select(cid, label, options, chosen, wrap_id=None)
  text(cid, label, value, wrap_id=None, label_id=None, disabled=False)
                             a text box; its shipped value may contain none of
                             < > & " (labcheck reads values undecoded). wrap_id
                             names the .field div, so a mode can hide it with
                             style.display (never [hidden]: .field sets display)
  range_(cid, label, lo, hi, value)   a range, with <span id=cid+'Out'>
  kpis(items)                [(label, tile id)] -> the kpi-grid
  hint(text), toolbar(name, subtitle, legend), stage(inner), svg(cid, alt),
  wrap(cid), banner(cid)     page furniture
  presets(cfg, kit, mode)    validates cfg['presets'] (non-empty; ids unique
                             and markup-safe; every preset has a label)
  chosen(presets, cfg, kit, mode)   the preset cfg['preset'] names (default the
                             first)
  check(kit, mode, preset, ok, why) raise ValueError naming the preset
  choice(cfg, key, allowed, kit, mode)   a redraw-only control's shipped value
  rational(value, kit, mode, preset, field, allow_none=False)
                             int, Fraction or 'p/q' text -> canonical 'p/q'
  formula(value, letters, kit, mode, preset, field, allow_none=False)
                             a typed formula: ASCII digits, operators,
                             brackets and the given letters only
  options(presets), expect(presets)
  lab(cfg, title=, subtitle=, markup=, controls=, script=, panel_title=,
      panel_intro=, select=, presets=)   -> Lab with expect={select: {...}}

THE JAVASCRIPT API (module-level and named; each block is a NAME = r'''...'''
raw string so scripts/mathcheck.js can extract it)

  SHOW_JS  (always shipped)
    DE_q(r)               an exact rational in the library's notation: 3/4, −2,
                          0. It is Rtext with the minus sign U+2212, because
                          algebra_core's Rtext prints a hyphen and is not edited.
    DE_dec(x)             a double: '≈ ' + six significant figures, trailing
                          zeros dropped; scientific (≈ 2.06115e-9) below 1e-4
                          and from 1e21; '—' for NaN or an infinity
    DE_root(p, s, imag)   p ± s, with p a rational and s quadroots' {q, k}
                          (q·√k): (−1 ± √5)/2, −1 ± 2i, ±2i, ±√5/2. A rational
                          pair (k = 1, real) prints both values ascending:
                          '−2, −1'. With p === null it prints the one value:
                          √5, 2√6, √10/2
    DE_float(r)           a rational as the nearest double; safe for numerators
                          of thousands of digits, where Rnum gives NaN
    DE_rat(text)          a typed rational ('3', '-7/4', '0.5', '−2') or null
    DE_sup(k)             superscript digits
    DE_lin(r, v)          r times v: t, −t, 3t, t/3, −2t/3
    DE_sum(pieces)        [{c: R, body: str, dot: bool}] -> a signed sum. A
                          coefficient 1 is not written; an integer is glued
                          (3t²), or joined by '·' with dot (2·e^(−t)); 1/d
                          without dot divides (t³/3); any other fraction is
                          (2/3)·body. Zero terms are skipped; empty is '0'.
    DE_ptext(p, v)        a POLY_JS coefficient list in that notation:
                          3t² − 12t + 9 (POLY_JS's Ptext prints 3t^2 - 12t + 9)
    DE_el(id), DE_set(id, text), DE_html(id, html), DE_esc(s), DE_msg(e),
    DE_refuse(statusId, tiles, stages, why), DE_ok(statusId, html)
                          page furniture. DE_set skips an id the page does not
                          carry (a tile a lesson omits). Markup built in a
                          script quotes no attribute: class=tt.

  MPOLY_JS  polynomials over Q in named variables
    {vars: ['t', 'y'], terms: [{e: [i, j], c: R}]}: terms merged, zero-free,
    sorted descending lexicographically in the order of vars.
    MPmake(vars, terms), MPconst(vars, r), MPvar(vars, name), MPzero(p),
    MPlift(p, vars), MPunify(a, b) (both over the union of their vars),
    MPadd, MPsub, MPmul, MPscale(p, r), MPpow(p, k),
    MPeval(p, point) (point {t: R, y: R}; exact; a missing variable throws),
    MPevalFloat(p, point), MPpartial(p, v), MPdegree(p[, v]) (-1 for zero),
    MPhas(p, v), MPtext(p[, {by: v}]) (by: ascending powers of v, the way a
    difference quotient is read: 3t² + 3th + h²; descending otherwise),
    MPfromExpr(node, vars) (null when not a polynomial in vars),
    MPparse(text, vars[, limits]) (throws Error with D.0's sentence, 'this
    lab steps polynomial right-hand sides exactly; sin(t) is not one', or
    names an unknown letter, a degree or a term count past limits, default
    {degree: 6, terms: 24}), MPtoPoly(p, v) (null if another variable
    appears), MPfromPoly(list, vars, v), MPsubst(p, v, q), MPdivVar(p, v)
    (exact division by v; null when a term lacks v), Pintegral(list) (the
    antiderivative of a POLY_JS list, constant 0), Etext(node) (an EXPR_JS
    tree as ASCII). (MPbalanced(s, i), the index of the bracket closing
    s[i], lives in SHOW_JS so RF_JS and EP_JS need no MPOLY_JS.)

  RF_JS  rational functions of one variable over Q
    {num: POLY, den: POLY}, lowest terms, den monic.
    RFmake(num, den), RFconst(r), RFvar(), RFpoly(list), RFadd, RFsub, RFmul,
    RFdiv, RFscale(F, r), RFpow(F, k) (k may be negative), RFderiv (quotient
    rule), RFeval(F, x) (exact; null at a pole), RFevalFloat(F, x), RFzero,
    RFequal, RFispoly, RFtext(F, v[, factored]) (factored prints the
    denominator as (s + 1)(s + 2), s(s + 1)², ((s + 1)² + 4)),
    RFfromExpr(node, v) (null when not rational in v), RFparse(text, v)
    (throws), RFsolve(M, rhs) (exact Gauss-Jordan; null when singular),
    RFpartial(F) -> {poly, terms: [{root, power, coef}], quad: null |
    {alpha, beta2, A, B, poly}} (linear factors of any multiplicity and at
    most one irreducible quadratic) or {refused: '...'}, RFpartialText(P, v).

  EP_JS  exponential polynomials Σ c·tᵏ·e^(at)·T(bt), T ∈ {1, cos, sin}
    a list of {c: R, k: int, a: R, b: R (≥ 0), trig: '1' | 'cos' | 'sin'},
    merged and zero-free; b = 0 forces trig '1' and drops sin(0·t) terms;
    sorted a descending, then b ascending, then trig, then k descending.
    EPmake(terms), EPconst(r), EPadd, EPsub, EPscale(e, r), EPmulpoly(e, p)
    (p a POLY_JS list in t), EPderiv, EPzero, EPequal, EPispoly,
    EPtext(e) (2·e^(−t) − e^(−2t); 2·e^(−t)·cos(2t) + e^(−t)·sin(2t);
    (2/3)·t − 2/9), EPevalExact(e, t0) (exact when every term has a = b = 0,
    or t0 = 0; else null), EPevalFloat(e, t), EPparse(text, env) (env gives
    C and D rational values; throws), EPfamily(text) -> {base, C, D, hasC,
    hasD} (parses at (C, D) = (0, 0), (1, 0), (0, 1) and checks linearity at
    (1, 1) and (2, 0), (0, 2); throws), EPlaplace(e) -> an RF in s,
    EPfromPartial(P) -> {ep} or {refused}.

  STEP_JS  exact steppers
    DE_DIGITS = 2000. DE_euler(f, t0, y0, h, n), DE_heun, DE_rk4: f an MPOLY
    in t and y (either may be absent); each returns {rows: [{t, y}], steps,
    stopped, digits}: steps completed; stopped true when the digit budget
    ended the run (the step that broke it is NOT kept, so y′ = y², y(0) = 1,
    h = 1/4 stops after step 11); digits the widest denominator kept, in
    decimal digits. DE_eulerSys(f, g, t0, x0, y0, h, n[, names]) -> rows
    [{t, x, y}] (names: the unknowns as f and g spell them, default
    ['x', 'y']). DE_digits(list of R): the most digits in any numerator or
    denominator.

  DRAW_JS  drawing (floats; pixels only)
    DE_arrows(plot, f, grid) (f(t, y) a slope, or [dx, dy] for a vector
    field; grid arrows per side, default 15), DE_polyline(plot, pts, cls)
    (pts [[x, y]]; default class 'plot-curve good'), DE_rk4float(f, start,
    h, n) (start [t0, y0] with f(t, y) a number, or [t0, x0, y0] with
    f(t, x, y) -> [dx, dy]; n defaults to 400; returns [t, y] or [x, y]
    points, stopping at a non-finite value or one past 1e6). Classes: an
    exact polygon 'plot-curve good', a float curve 'plot-curve alt', arrows
    'plot-tickmark'; the legend names both curves.
"""

import json
import re
from fractions import Fraction

from .algebra_core import EXPR_JS, PLOT_JS, POLY_JS, RATIONAL_JS, SURD_JS
from .common import Lab

# ---------------------------------------------------------------------------
# SHOW_JS -- printing and page furniture. Shipped on every page of both kits.
# ---------------------------------------------------------------------------

SHOW_JS = r"""
  /* ---- de_core: printing ------------------------------------------------
     Three printers for a number and no fourth: DE_q for an exact rational,
     DE_dec for a double (always behind the approximately sign), DE_root for a
     surd or a complex pair. A tile that may hold either prints whichever
     applies, and never a bare decimal. */
  var DE_SUPS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'];
  function DE_q(r) {
    var s = Rtext(r);
    return s.charAt(0) === '-' ? '−' + s.slice(1) : s;
  }
  function DE_float(r) {
    var n = r.n, d = r.d, neg = n < 0n;
    if (neg) n = -n;
    if (n === 0n) return 0;
    var ln = n.toString().length, ld = d.toString().length;
    var sn = ln > 18 ? ln - 18 : 0, sd = ld > 18 ? ld - 18 : 0;
    var nn = Number(sn ? n / (10n ** BigInt(sn)) : n);
    var dd = Number(sd ? d / (10n ** BigInt(sd)) : d);
    var v = (nn / dd) * Math.pow(10, sn - sd);
    return neg ? -v : v;
  }
  function DE_trim(s) {
    return s.indexOf('.') >= 0 ? s.replace(/0+$/, '').replace(/\.$/, '') : s;
  }
  function DE_expform(s) {
    var m = /^([0-9.]+)e([+-][0-9]+)$/.exec(s);
    return DE_trim(m[1]) + 'e' + (m[2].charAt(0) === '+' ? m[2].slice(1) : m[2]);
  }
  function DE_dec(x) {
    if (typeof x !== 'number' || !isFinite(x)) return '—';
    if (x === 0) return '≈ 0';
    var ax = Math.abs(x), s;
    if (ax < 1e-4 || ax >= 1e21) s = DE_expform(ax.toExponential(5));
    else {
      s = ax.toPrecision(6);
      s = s.indexOf('e') >= 0 ? DE_expform(s) : DE_trim(s);
    }
    return '≈ ' + (x < 0 ? '−' : '') + s;
  }
  function DE_rat(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-');
    s = s.replace(/^\s+|\s+$/g, '');
    if (!s.length) return null;
    return Rparse(s);
  }
  function DE_sup(k) {
    var s = String(k), out = '', i;
    for (i = 0; i < s.length; i += 1) out += DE_SUPS[s.charCodeAt(i) - 48];
    return out;
  }
  /* r times a variable: t, −t, 3t, t/3, −2t/3. */
  function DE_lin(r, v) {
    v = v || 't';
    var neg = r.n < 0n, n = neg ? -r.n : r.n, s = (n === 1n ? '' : String(n)) + v;
    if (r.d !== 1n) s += '/' + r.d;
    return (neg ? '−' : '') + s;
  }
  function DE_sum(pieces) {
    var out = '', i;
    for (i = 0; i < pieces.length; i += 1) {
      var c = pieces[i].c, body = pieces[i].body || '', dot = pieces[i].dot;
      if (Rzero(c)) continue;
      var neg = c.n < 0n, mag = Rabs(c), txt;
      if (body === '') txt = Rtext(mag);
      else if (Requ(mag, R1)) txt = body;
      else if (mag.d === 1n) txt = String(mag.n) + (dot ? '·' : '') + body;
      else if (!dot && mag.n === 1n) txt = body + '/' + mag.d;
      else txt = '(' + Rtext(mag) + ')·' + body;
      if (out === '') out = (neg ? '−' : '') + txt;
      else out += (neg ? ' − ' : ' + ') + txt;
    }
    return out === '' ? '0' : out;
  }
  function DE_ptext(p, v) {
    v = v || 't';
    var pieces = [], i;
    for (i = p.length - 1; i >= 0; i -= 1) {
      if (!p[i] || Rzero(p[i])) continue;
      pieces.push({ c: p[i], body: i === 0 ? '' : (i === 1 ? v : v + DE_sup(i)), dot: false });
    }
    return DE_sum(pieces);
  }
  /* Q·√k (times i) with Q a positive integer: the part after the ±. */
  function DE_rootpart(Q, k, imag) {
    var s = (Q === 1n && (k !== 1n || imag)) ? '' : String(Q);
    if (k !== 1n) s += '√' + k;
    if (imag) s += 'i';
    return s;
  }
  function DE_root(p, s, imag) {
    var k = s.k, q = s.q;
    if (p === null || p === undefined) {
      if (Rzero(q)) return '0';
      var one = DE_rootpart(q.n < 0n ? -q.n : q.n, k, imag);
      return (q.n < 0n ? '−' : '') + one + (q.d === 1n ? '' : '/' + q.d);
    }
    if (Rzero(q)) return DE_q(p);
    if (k === 1n && !imag) return DE_q(Rsub(p, Rabs(q))) + ', ' + DE_q(Radd(p, Rabs(q)));
    var D = p.d * q.d / bgcd(p.d, q.d);
    var P = p.n * (D / p.d), Qn = q.n * (D / q.d);
    if (Qn < 0n) Qn = -Qn;
    var term = DE_rootpart(Qn, k, imag);
    if (P === 0n) return '±' + term + (D === 1n ? '' : '/' + D);
    var body = DE_q(R(P)) + ' ± ' + term;
    return D === 1n ? body : '(' + body + ')/' + D;
  }

  /* ---- de_core: page furniture -------------------------------------------
     Tiles are written by textContent and never with an entity; a tile id the
     page does not carry (one a lesson omits) is skipped, not an error.
     Markup built here quotes no attribute: class=tt. */
  function DE_el(id) { return document.getElementById(id); }
  function DE_set(id, text) { var el = DE_el(id); if (el) el.textContent = String(text); }
  function DE_html(id, html) { var el = DE_el(id); if (el) el.innerHTML = html; }
  function DE_esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function DE_msg(e) { return e && e.message ? e.message : String(e); }
  function DE_refuse(statusId, tiles, stages, why) {
    var i;
    for (i = 0; i < tiles.length; i += 1) DE_set(tiles[i], '—');
    for (i = 0; i < stages.length; i += 1) {
      var el = DE_el(stages[i]);
      if (el) { el.textContent = ''; el.innerHTML = ''; }
    }
    DE_html(statusId, '<span class=tone-red><strong>Refused.</strong> ' + DE_esc(why) + '</span>');
  }
  function DE_ok(statusId, html) { DE_html(statusId, html); }
  /* The index of the bracket that closes the one at s[at] (the last index
     when it is never closed); the parsers in MPOLY_JS, RF_JS and EP_JS use it. */
  function MPbalanced(s, at) {
    var depth = 0, i;
    for (i = at; i < s.length; i += 1) {
      if (s.charAt(i) === '(') depth += 1;
      else if (s.charAt(i) === ')') { depth -= 1; if (depth === 0) return i; }
    }
    return s.length - 1;
  }
"""

# ---------------------------------------------------------------------------
# MPOLY_JS -- polynomials over Q in named variables.
# ---------------------------------------------------------------------------

MPOLY_JS = r"""
  /* ---- de_core: polynomials in several variables -------------------------
     A right-hand side f(t, y) is a polynomial in two letters, a difference
     quotient one in t and h. One representation serves both: a list of vars
     and a list of {e: exponents in that order, c: rational} terms, merged,
     zero-free and sorted, so two equal polynomials are equal lists. */
  function MPcmp(a, b) {
    var i;
    for (i = 0; i < a.e.length; i += 1) if (a.e[i] !== b.e[i]) return b.e[i] - a.e[i];
    return 0;
  }
  function MPmake(vars, terms) {
    var map = {}, keys = [], i, out = [];
    for (i = 0; i < terms.length; i += 1) {
      var key = terms[i].e.join(',');
      if (!map.hasOwnProperty(key)) { map[key] = { e: terms[i].e.slice(), c: R0 }; keys.push(key); }
      map[key].c = Radd(map[key].c, terms[i].c);
    }
    for (i = 0; i < keys.length; i += 1) if (!Rzero(map[keys[i]].c)) out.push(map[keys[i]]);
    out.sort(MPcmp);
    return { vars: vars.slice(), terms: out };
  }
  function MPzeros(n) { var e = [], i; for (i = 0; i < n; i += 1) e.push(0); return e; }
  function MPconst(vars, r) { return MPmake(vars, [{ e: MPzeros(vars.length), c: r }]); }
  function MPvar(vars, name) {
    var e = MPzeros(vars.length), at = vars.indexOf(name);
    if (at < 0) throw new Error('no variable ' + name);
    e[at] = 1;
    return MPmake(vars, [{ e: e, c: R1 }]);
  }
  function MPzero(p) { return p.terms.length === 0; }
  /* The same polynomial over another list of variables. */
  function MPlift(p, vars) {
    var terms = [], i, j;
    for (i = 0; i < p.terms.length; i += 1) {
      var e = MPzeros(vars.length);
      for (j = 0; j < p.vars.length; j += 1) {
        if (!p.terms[i].e[j]) continue;
        var at = vars.indexOf(p.vars[j]);
        if (at < 0) throw new Error('the variable ' + p.vars[j] + ' has no place here');
        e[at] = p.terms[i].e[j];
      }
      terms.push({ e: e, c: p.terms[i].c });
    }
    return MPmake(vars, terms);
  }
  function MPunify(a, b) {
    var vars = a.vars.slice(), i;
    for (i = 0; i < b.vars.length; i += 1) if (vars.indexOf(b.vars[i]) < 0) vars.push(b.vars[i]);
    return [MPlift(a, vars), MPlift(b, vars)];
  }
  function MPadd(a, b) { var u = MPunify(a, b); return MPmake(u[0].vars, u[0].terms.concat(u[1].terms)); }
  function MPscale(p, r) {
    return MPmake(p.vars, p.terms.map(function (t) { return { e: t.e, c: Rmul(t.c, r) }; }));
  }
  function MPsub(a, b) { return MPadd(a, MPscale(b, R(-1n))); }
  function MPmul(a, b) {
    var u = MPunify(a, b), x = u[0], y = u[1], terms = [], i, j, k;
    for (i = 0; i < x.terms.length; i += 1) {
      for (j = 0; j < y.terms.length; j += 1) {
        var e = [];
        for (k = 0; k < x.vars.length; k += 1) e.push(x.terms[i].e[k] + y.terms[j].e[k]);
        terms.push({ e: e, c: Rmul(x.terms[i].c, y.terms[j].c) });
      }
    }
    return MPmake(x.vars, terms);
  }
  function MPpow(p, k) {
    var out = MPconst(p.vars, R1), i;
    for (i = 0; i < k; i += 1) out = MPmul(out, p);
    return out;
  }
  /* Exact at a rational point {t: R, y: R}. A variable the polynomial uses
     and the point does not name is an error, never a silent zero. */
  function MPeval(p, point) {
    var acc = R0, i, j;
    for (i = 0; i < p.terms.length; i += 1) {
      var term = p.terms[i].c;
      for (j = 0; j < p.vars.length; j += 1) {
        var e = p.terms[i].e[j];
        if (!e) continue;
        if (!point || !point.hasOwnProperty(p.vars[j])) throw new Error('no value for ' + p.vars[j]);
        term = Rmul(term, Rpow(point[p.vars[j]], e));
      }
      acc = Radd(acc, term);
    }
    return acc;
  }
  function MPevalFloat(p, point) {
    var acc = 0, i, j;
    for (i = 0; i < p.terms.length; i += 1) {
      var term = Rnum(p.terms[i].c);
      for (j = 0; j < p.vars.length; j += 1) {
        var e = p.terms[i].e[j];
        if (e) term *= Math.pow(point[p.vars[j]], e);
      }
      acc += term;
    }
    return acc;
  }
  function MPpartial(p, v) {
    var at = p.vars.indexOf(v), terms = [], i;
    if (at < 0) return MPconst(p.vars, R0);
    for (i = 0; i < p.terms.length; i += 1) {
      var e = p.terms[i].e.slice();
      if (!e[at]) continue;
      var c = Rmul(p.terms[i].c, R(BigInt(e[at])));
      e[at] -= 1;
      terms.push({ e: e, c: c });
    }
    return MPmake(p.vars, terms);
  }
  function MPdegree(p, v) {
    var at = v === undefined ? -1 : p.vars.indexOf(v), best = -1, i, j;
    if (v !== undefined && at < 0) return p.terms.length ? 0 : -1;
    for (i = 0; i < p.terms.length; i += 1) {
      var d = 0;
      if (at >= 0) d = p.terms[i].e[at];
      else for (j = 0; j < p.vars.length; j += 1) d += p.terms[i].e[j];
      if (d > best) best = d;
    }
    return best;
  }
  function MPhas(p, v) { return MPdegree(p, v) > 0; }
  function MPbody(vars, e) {
    var s = '', j;
    for (j = 0; j < vars.length; j += 1) {
      if (!e[j]) continue;
      s += vars[j] + (e[j] === 1 ? '' : DE_sup(e[j]));
    }
    return s;
  }
  /* The library's notation: t² − y, y − y²/4, 3t² + 3th + h². With {by: v}
     the terms run in ascending powers of v; otherwise descending. */
  function MPtext(p, opts) {
    var terms = p.terms.slice(), at = opts && opts.by ? p.vars.indexOf(opts.by) : -1;
    if (at >= 0) {
      terms.sort(function (a, b) { return a.e[at] !== b.e[at] ? a.e[at] - b.e[at] : MPcmp(a, b); });
    }
    return DE_sum(terms.map(function (t) { return { c: t.c, body: MPbody(p.vars, t.e), dot: false }; }));
  }
  /* An EXPR_JS tree as a polynomial in vars, or null. Division by a nonzero
     constant only; a power must be a whole number from 0 to 64; no calls. */
  function MPfromExpr(node, vars) {
    var a, b;
    switch (node.k) {
      case 'num': { var r = Rparse(node.v); return r === null ? null : MPconst(vars, r); }
      case 'var': return vars.indexOf(node.v) >= 0 ? MPvar(vars, node.v) : null;
      case 'neg': a = MPfromExpr(node.a, vars); return a === null ? null : MPscale(a, R(-1n));
      case 'add': case 'sub': case 'mul':
        a = MPfromExpr(node.a, vars); b = MPfromExpr(node.b, vars);
        if (a === null || b === null) return null;
        return node.k === 'add' ? MPadd(a, b) : (node.k === 'sub' ? MPsub(a, b) : MPmul(a, b));
      case 'div':
        a = MPfromExpr(node.a, vars); b = MPfromExpr(node.b, vars);
        if (a === null || b === null || MPdegree(b) > 0 || MPzero(b)) return null;
        return MPscale(a, Rinv(b.terms[0].c));
      case 'pow':
        a = MPfromExpr(node.a, vars); b = MPfromExpr(node.b, vars);
        if (a === null || b === null || MPdegree(b) > 0) return null;
        var e = b.terms.length ? b.terms[0].c : R0;
        if (!Rint(e) || e.n < 0n || e.n > 64n) return null;
        return MPpow(a, Number(e.n));
    }
    return null;
  }
  function Etext(node) {
    function wrap(n) {
      var s = Etext(n);
      return (n.k === 'add' || n.k === 'sub' || n.k === 'neg') ? '(' + s + ')' : s;
    }
    switch (node.k) {
      case 'num': case 'var': return node.v;
      case 'neg': return '-' + wrap(node.a);
      case 'add': return Etext(node.a) + ' + ' + Etext(node.b);
      case 'sub': return Etext(node.a) + ' - ' + wrap(node.b);
      case 'mul': return wrap(node.a) + '*' + wrap(node.b);
      case 'div': return wrap(node.a) + '/' + wrap(node.b);
      case 'pow': return wrap(node.a) + '^' + wrap(node.b);
      case 'fn': return node.v + '(' + Etext(node.a) + ')';
    }
    return '?';
  }
  /* The smallest piece of a tree that is not a polynomial in vars. */
  function MPoffender(node, vars) {
    if (node.k === 'num' || node.k === 'var') return null;
    if (node.k === 'fn') return node;
    var kids = node.k === 'neg' ? [node.a] : [node.a, node.b], i;
    for (i = 0; i < kids.length; i += 1) {
      var inner = MPoffender(kids[i], vars);
      if (inner) return inner;
    }
    return MPfromExpr(node, vars) === null ? node : null;
  }
  /* What a reader types, as a polynomial in vars -- or a refusal naming the
     piece that is not one, in the sentence D.0 prescribes. */
  function MPparse(text, vars, limits) {
    limits = limits || { degree: 6, terms: 24 };
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    var head = 'this lab steps polynomial right-hand sides exactly; ';
    if (!/\S/.test(s)) throw new Error('there is nothing typed here');
    var fm = /(sin|cos|tan|exp|ln|log|sqrt|abs)\s*\(/.exec(s);
    if (fm) {
      var close = MPbalanced(s, fm.index + fm[0].length - 1);
      throw new Error(head + s.slice(fm.index, close + 1).replace(/\s+/g, '') + ' is not one');
    }
    var em = /(^|[^A-Za-z])e\s*\^\s*(\([^)]*\)|-?[A-Za-z0-9]+)/.exec(s);
    if (em && vars.indexOf('e') < 0) {
      throw new Error(head + em[0].slice(em[1].length).replace(/\s+/g, '') + ' is not one');
    }
    var letters = s.match(/[A-Za-z]/g) || [], i;
    for (i = 0; i < letters.length; i += 1) {
      if (vars.indexOf(letters[i]) < 0) {
        throw new Error('the letter ' + letters[i] + ' is not a variable here; this lab reads '
          + vars.join(' and '));
      }
    }
    var tree = Eparse(s);
    var p = MPfromExpr(tree, vars);
    if (p === null) {
      var bad = MPoffender(tree, vars);
      throw new Error(head + (bad ? Etext(bad) : s.replace(/\s+/g, '')) + ' is not one');
    }
    if (MPdegree(p) > limits.degree) {
      throw new Error('the degree is ' + MPdegree(p) + '; this lab takes degree ' + limits.degree + ' at most');
    }
    if (p.terms.length > limits.terms) {
      throw new Error('there are ' + p.terms.length + ' terms; this lab takes ' + limits.terms + ' at most');
    }
    return p;
  }
  /* One variable's dense coefficient list for POLY_JS, or null when another
     variable appears. */
  function MPtoPoly(p, v) {
    var at = p.vars.indexOf(v), out = [], i, j;
    for (i = 0; i < p.terms.length; i += 1) {
      for (j = 0; j < p.vars.length; j += 1) if (j !== at && p.terms[i].e[j]) return null;
      var k = at < 0 ? 0 : p.terms[i].e[at];
      while (out.length <= k) out.push(R0);
      out[k] = Radd(out[k], p.terms[i].c);
    }
    return Pnorm(out);
  }
  function MPfromPoly(list, vars, v) {
    var at = vars.indexOf(v), terms = [], i;
    for (i = 0; i < list.length; i += 1) {
      if (!list[i] || Rzero(list[i])) continue;
      var e = MPzeros(vars.length);
      if (i > 0) { if (at < 0) throw new Error('no variable ' + v); e[at] = i; }
      terms.push({ e: e, c: list[i] });
    }
    return MPmake(vars, terms);
  }
  /* Substitute the polynomial q for the variable v. */
  function MPsubst(p, v, q) {
    var u = MPunify(p, q), P = u[0], Q = u[1], at = P.vars.indexOf(v), out = MPconst(P.vars, R0), i;
    if (at < 0) return P;
    var powers = [MPconst(P.vars, R1)];
    for (i = 0; i < P.terms.length; i += 1) {
      var e = P.terms[i].e.slice(), k = e[at];
      while (powers.length <= k) powers.push(MPmul(powers[powers.length - 1], Q));
      e[at] = 0;
      out = MPadd(out, MPmul(MPmake(P.vars, [{ e: e, c: P.terms[i].c }]), powers[k]));
    }
    return out;
  }
  function MPdivVar(p, v) {
    var at = p.vars.indexOf(v), terms = [], i;
    if (at < 0) return MPzero(p) ? p : null;
    for (i = 0; i < p.terms.length; i += 1) {
      if (!p.terms[i].e[at]) return null;
      var e = p.terms[i].e.slice();
      e[at] -= 1;
      terms.push({ e: e, c: p.terms[i].c });
    }
    return MPmake(p.vars, terms);
  }
  /* The reverse power rule on a POLY_JS list: the antiderivative with
     constant 0. */
  function Pintegral(p) {
    var out = [R0], i;
    for (i = 0; i < p.length; i += 1) out.push(Rdiv(p[i] || R0, R(BigInt(i + 1))));
    return Pnorm(out);
  }
"""

# ---------------------------------------------------------------------------
# RF_JS -- rational functions in one variable.
# ---------------------------------------------------------------------------

RF_JS = r"""
  /* ---- de_core: rational functions ----------------------------------------
     num/den over Q, the denominator monic and the fraction in lowest terms,
     so equal functions are equal pairs and a pole is a zero of den. */
  function RFmake(num, den) {
    num = Pnorm(num); den = Pnorm(den);
    if (!den.length) throw new Error('division by zero');
    if (!num.length) return { num: [], den: [R1] };
    var g = Pgcd(num, den);
    if (Pdeg(g) > 0) { num = Pdivmod(num, g).q; den = Pdivmod(den, g).q; }
    var lead = Plead(den);
    return { num: Pscale(num, Rinv(lead)), den: Pscale(den, Rinv(lead)) };
  }
  function RFconst(r) { return RFmake([r], [R1]); }
  function RFvar() { return RFmake([R0, R1], [R1]); }
  function RFpoly(list) { return RFmake(list, [R1]); }
  function RFadd(F, G) { return RFmake(Padd(Pmul(F.num, G.den), Pmul(G.num, F.den)), Pmul(F.den, G.den)); }
  function RFsub(F, G) { return RFmake(Psub(Pmul(F.num, G.den), Pmul(G.num, F.den)), Pmul(F.den, G.den)); }
  function RFmul(F, G) { return RFmake(Pmul(F.num, G.num), Pmul(F.den, G.den)); }
  function RFdiv(F, G) {
    if (!Pnorm(G.num).length) throw new Error('division by the zero function');
    return RFmake(Pmul(F.num, G.den), Pmul(F.den, G.num));
  }
  function RFscale(F, r) { return RFmake(Pscale(F.num, r), F.den); }
  function RFpow(F, k) {
    var out = RFconst(R1), i, base = k < 0 ? RFdiv(RFconst(R1), F) : F;
    for (i = 0; i < (k < 0 ? -k : k); i += 1) out = RFmul(out, base);
    return out;
  }
  function RFderiv(F) {
    return RFmake(Psub(Pmul(Pderiv(F.num), F.den), Pmul(F.num, Pderiv(F.den))), Pmul(F.den, F.den));
  }
  function RFeval(F, x) {
    var d = Peval(F.den, x);
    if (Rzero(d)) return null;
    return Rdiv(Peval(F.num, x), d);
  }
  function RFevalFloat(F, x) {
    var n = 0, d = 0, i;
    for (i = F.num.length - 1; i >= 0; i -= 1) n = n * x + Rnum(F.num[i]);
    for (i = F.den.length - 1; i >= 0; i -= 1) d = d * x + Rnum(F.den[i]);
    return n / d;
  }
  function RFzero(F) { return Pnorm(F.num).length === 0; }
  function RFequal(F, G) { return RFzero(RFsub(F, G)); }
  function RFispoly(F) { return Pdeg(F.den) === 0; }
  function RFbracket(s) { return (s.indexOf(' + ') >= 0 || s.indexOf(' − ') >= 0) ? '(' + s + ')' : s; }
  /* A monic factor (v − r)^m, or a monic irreducible quadratic completed to
     (v − α)² + β² when β² > 0. */
  function RFfactortext(f, v) {
    if (f.quad) {
      var alpha = Rdiv(Rneg(f.quad[1] || R0), R(2n)), beta2 = Rsub(f.quad[0] || R0, Rmul(alpha, alpha));
      if (Rsign(beta2) > 0) {
        var inner = Rzero(alpha) ? v : '(' + DE_ptext([Rneg(alpha), R1], v) + ')';
        return '(' + inner + '² + ' + DE_q(beta2) + ')';
      }
      return '(' + DE_ptext(f.quad, v) + ')';
    }
    var base = Rzero(f.root) ? v : '(' + DE_ptext([Rneg(f.root), R1], v) + ')';
    return base + (f.mult > 1 ? DE_sup(f.mult) : '');
  }
  function RFdenfactors(den) {
    var fac = Pfactor(den), out = [], i;
    for (i = 0; i < fac.factors.length; i += 1) out.push({ root: fac.factors[i].root, mult: fac.factors[i].mult });
    /* s, then (s + 1), then (s + 2): roots descending, the way they are written */
    out.sort(function (x, y) { return Rcmp(y.root, x.root); });
    if (fac.rest.length) {
      var rest = Pmonic(fac.rest);
      out.push(Pdeg(rest) === 2 ? { quad: rest } : { other: rest });
    }
    return out;
  }
  function RFtext(F, v, factored) {
    v = v || 't';
    var num = DE_ptext(F.num, v);
    if (Pdeg(F.den) === 0) return num;
    var den;
    if (factored) {
      var fs = RFdenfactors(F.den), parts = [], i;
      for (i = 0; i < fs.length; i += 1) {
        parts.push(fs[i].other ? '(' + DE_ptext(fs[i].other, v) + ')' : RFfactortext(fs[i], v));
      }
      den = fs.length > 1 ? '(' + parts.join('') + ')' : parts[0];
    } else {
      den = DE_ptext(F.den, v);
      if (!(den === v || /^[a-z][⁰¹²³⁴⁵⁶⁷⁸⁹]+$/.test(den))) den = '(' + den + ')';
    }
    return RFbracket(num) + '/' + den;
  }
  /* An EXPR_JS tree as a rational function of v, or null: sums, products,
     quotients and whole-number powers (negative ones too), and no calls. */
  function RFfromExpr(node, v) {
    var a, b;
    switch (node.k) {
      case 'num': { var r = Rparse(node.v); return r === null ? null : RFconst(r); }
      case 'var': return node.v === v ? RFvar() : null;
      case 'neg': a = RFfromExpr(node.a, v); return a === null ? null : RFscale(a, R(-1n));
      case 'add': case 'sub': case 'mul': case 'div':
        a = RFfromExpr(node.a, v); b = RFfromExpr(node.b, v);
        if (a === null || b === null) return null;
        if (node.k === 'add') return RFadd(a, b);
        if (node.k === 'sub') return RFsub(a, b);
        if (node.k === 'mul') return RFmul(a, b);
        return RFzero(b) ? null : RFdiv(a, b);
      case 'pow':
        a = RFfromExpr(node.a, v); b = RFfromExpr(node.b, v);
        if (a === null || b === null || !RFispoly(b) || Pdeg(b.num) > 0) return null;
        var e = b.num.length ? b.num[0] : R0;
        if (!Rint(e) || e.n > 32n || e.n < -32n) return null;
        if (e.n < 0n && RFzero(a)) return null;
        return RFpow(a, Number(e.n));
    }
    return null;
  }
  function RFparse(text, v) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    var head = 'this lab reads polynomials and ratios of them exactly; ';
    if (!/\S/.test(s)) throw new Error('there is nothing typed here');
    var fm = /(sin|cos|tan|exp|ln|log|sqrt|abs)\s*\(/.exec(s);
    if (fm) {
      var close = MPbalanced(s, fm.index + fm[0].length - 1);
      throw new Error(head + s.slice(fm.index, close + 1).replace(/\s+/g, '') + ' is not one');
    }
    var letters = s.match(/[A-Za-z]/g) || [], i;
    for (i = 0; i < letters.length; i += 1) {
      if (letters[i] !== v) throw new Error('the letter ' + letters[i] + ' is not the variable here; this lab reads ' + v);
    }
    var F = RFfromExpr(Eparse(s), v);
    if (F === null) throw new Error(head + 'a power must be a whole number and no denominator may be 0');
    return F;
  }
  /* The square system M x = rhs over Q by Gauss-Jordan; null when singular. */
  function RFsolve(M, rhs) {
    var n = M.length, A = [], i, j, k;
    for (i = 0; i < n; i += 1) A.push(M[i].slice().concat([rhs[i]]));
    for (j = 0; j < n; j += 1) {
      var piv = -1;
      for (i = j; i < n; i += 1) if (!Rzero(A[i][j])) { piv = i; break; }
      if (piv < 0) return null;
      var tmp = A[j]; A[j] = A[piv]; A[piv] = tmp;
      var inv = Rinv(A[j][j]);
      for (k = j; k <= n; k += 1) A[j][k] = Rmul(A[j][k], inv);
      for (i = 0; i < n; i += 1) {
        if (i === j || Rzero(A[i][j])) continue;
        var f = A[i][j];
        for (k = j; k <= n; k += 1) A[i][k] = Rsub(A[i][k], Rmul(f, A[j][k]));
      }
    }
    var out = [];
    for (i = 0; i < n; i += 1) out.push(A[i][n]);
    return out;
  }
  /* Partial fractions: linear factors of any multiplicity and at most one
     irreducible quadratic, by solving the exact linear system for the
     coefficients. Anything else is refused, by name. */
  function RFpartial(F) {
    var dm = Pdivmod(F.num, F.den), poly = dm.q, rem = dm.r, den = F.den;
    var fs = RFdenfactors(den), i, j, basis = [], cols = [], quad = null;
    for (i = 0; i < fs.length; i += 1) {
      if (fs[i].other) return { refused: 'the denominator has an irreducible factor of degree 3 or more' };
      if (fs[i].quad) quad = fs[i].quad;
    }
    for (i = 0; i < fs.length; i += 1) {
      if (fs[i].quad) continue;
      var lin = [Rneg(fs[i].root), R1];
      for (j = 1; j <= fs[i].mult; j += 1) {
        basis.push(Pdivmod(den, Ppow(lin, j)).q);
        cols.push({ root: fs[i].root, power: j });
      }
    }
    if (quad) {
      var cof = Pdivmod(den, quad).q;
      basis.push(Pmul([R0, R1], cof));
      cols.push({ quadA: true });
      basis.push(cof);
      cols.push({ quadB: true });
    }
    var n = Pdeg(den), M = [], rhs = [];
    for (i = 0; i < n; i += 1) {
      var row = [];
      for (j = 0; j < basis.length; j += 1) row.push(basis[j][i] || R0);
      M.push(row);
      rhs.push(rem[i] || R0);
    }
    var x = n ? RFsolve(M, rhs) : [];
    if (x === null) return { refused: 'the coefficient system is singular' };
    var terms = [], qA = R0, qB = R0;
    for (j = 0; j < cols.length; j += 1) {
      if (cols[j].quadA) qA = x[j];
      else if (cols[j].quadB) qB = x[j];
      else if (!Rzero(x[j])) terms.push({ root: cols[j].root, power: cols[j].power, coef: x[j] });
    }
    terms.sort(function (u, w) { return Rcmp(w.root, u.root) || u.power - w.power; });
    var q = null;
    if (quad) {
      var alpha = Rdiv(Rneg(quad[1]), R(2n));
      q = { alpha: alpha, beta2: Rsub(quad[0], Rmul(alpha, alpha)), A: qA, B: qB, poly: quad };
    }
    return { poly: poly, terms: terms, quad: q };
  }
  function RFpartialText(P, v) {
    v = v || 's';
    if (P.refused) return '—';
    var out = [], i;
    var polytext = DE_ptext(P.poly, v);
    if (polytext !== '0') out.push({ neg: false, text: polytext });
    for (i = 0; i < P.terms.length; i += 1) {
      var t = P.terms[i], c = t.coef, neg = c.n < 0n, mag = Rabs(c);
      var den = RFfactortext({ root: t.root, mult: t.power }, v);
      var numtxt = mag.d === 1n ? String(mag.n) : '(' + Rtext(mag) + ')';
      out.push({ neg: neg, text: numtxt + '/' + den });
    }
    if (P.quad && !(Rzero(P.quad.A) && Rzero(P.quad.B))) {
      var num = DE_ptext([P.quad.B, P.quad.A], v);
      out.push({ neg: false, text: RFbracket(num) + '/' + RFfactortext({ quad: P.quad.poly }, v) });
    }
    if (!out.length) return '0';
    var s = (out[0].neg ? '−' : '') + out[0].text;
    for (i = 1; i < out.length; i += 1) s += (out[i].neg ? ' − ' : ' + ') + out[i].text;
    return s;
  }
"""

# ---------------------------------------------------------------------------
# EP_JS -- exponential polynomials.
# ---------------------------------------------------------------------------

EP_JS = r"""
  /* ---- de_core: exponential polynomials -----------------------------------
     Σ c·tᵏ·e^(at)·T(bt), T one of 1, cos, sin, with c, a, b rational. The
     class is closed under differentiation, so whether a candidate solves a
     linear equation is decided by computing the residual and comparing it
     with zero -- not by evaluating anything. */
  var EP_TRIG = { '1': 0, 'cos': 1, 'sin': 2 };
  function EPcmp(x, y) {
    var c = Rcmp(y.a, x.a);
    if (c) return c;
    c = Rcmp(x.b, y.b);
    if (c) return c;
    if (x.trig !== y.trig) return EP_TRIG[x.trig] - EP_TRIG[y.trig];
    return y.k - x.k;
  }
  function EPmake(terms) {
    var map = {}, keys = [], out = [], i;
    for (i = 0; i < terms.length; i += 1) {
      var t = terms[i], c = t.c, b = t.b || R0, trig = t.trig || '1';
      if (Rzero(b)) { if (trig === 'sin') continue; trig = '1'; }
      if (trig === '1') b = R0;
      if (Rsign(b) < 0) { b = Rneg(b); if (trig === 'sin') c = Rneg(c); }
      var key = t.k + '|' + Rtext(t.a) + '|' + Rtext(b) + '|' + trig;
      if (!map.hasOwnProperty(key)) { map[key] = { c: R0, k: t.k, a: t.a, b: b, trig: trig }; keys.push(key); }
      map[key].c = Radd(map[key].c, c);
    }
    for (i = 0; i < keys.length; i += 1) if (!Rzero(map[keys[i]].c)) out.push(map[keys[i]]);
    out.sort(EPcmp);
    return out;
  }
  function EPconst(r) { return EPmake([{ c: r, k: 0, a: R0, b: R0, trig: '1' }]); }
  function EPadd(x, y) { return EPmake(x.concat(y)); }
  function EPscale(e, r) {
    return EPmake(e.map(function (t) { return { c: Rmul(t.c, r), k: t.k, a: t.a, b: t.b, trig: t.trig }; }));
  }
  function EPsub(x, y) { return EPadd(x, EPscale(y, R(-1n))); }
  function EPmulpoly(e, p) {
    var out = [], i, j;
    for (i = 0; i < e.length; i += 1) {
      for (j = 0; j < p.length; j += 1) {
        if (!p[j] || Rzero(p[j])) continue;
        out.push({ c: Rmul(e[i].c, p[j]), k: e[i].k + j, a: e[i].a, b: e[i].b, trig: e[i].trig });
      }
    }
    return EPmake(out);
  }
  /* (tᵏ e^(at) cos bt)′ = k tᵏ⁻¹ e^(at) cos bt + a tᵏ e^(at) cos bt − b tᵏ e^(at) sin bt,
     and the sine the same way with + b cos. */
  function EPderiv(e) {
    var out = [], i;
    for (i = 0; i < e.length; i += 1) {
      var t = e[i];
      if (t.k > 0) out.push({ c: Rmul(t.c, R(BigInt(t.k))), k: t.k - 1, a: t.a, b: t.b, trig: t.trig });
      out.push({ c: Rmul(t.c, t.a), k: t.k, a: t.a, b: t.b, trig: t.trig });
      if (t.trig === 'cos') out.push({ c: Rneg(Rmul(t.c, t.b)), k: t.k, a: t.a, b: t.b, trig: 'sin' });
      if (t.trig === 'sin') out.push({ c: Rmul(t.c, t.b), k: t.k, a: t.a, b: t.b, trig: 'cos' });
    }
    return EPmake(out);
  }
  function EPzero(e) { return e.length === 0; }
  function EPequal(x, y) { return EPzero(EPsub(x, y)); }
  function EPispoly(e) {
    var i;
    for (i = 0; i < e.length; i += 1) if (!Rzero(e[i].a) || e[i].trig !== '1') return false;
    return true;
  }
  function EPbody(t) {
    var parts = [];
    if (t.k === 1) parts.push('t');
    else if (t.k > 1) parts.push('t' + DE_sup(t.k));
    if (!Rzero(t.a)) parts.push(Requ(t.a, R1) ? 'e^t' : 'e^(' + DE_lin(t.a, 't') + ')');
    if (t.trig !== '1') parts.push(t.trig + '(' + DE_lin(t.b, 't') + ')');
    return parts.join('·');
  }
  function EPtext(e) {
    return DE_sum(e.map(function (t) {
      return { c: t.c, body: EPbody(t), dot: !Rzero(t.a) || t.trig !== '1' };
    }));
  }
  function EPevalExact(e, t0) {
    var acc = R0, i;
    for (i = 0; i < e.length; i += 1) {
      var t = e[i];
      if (Rzero(t0)) {
        if (t.k === 0 && t.trig !== 'sin') acc = Radd(acc, t.c);
        continue;
      }
      if (!Rzero(t.a) || t.trig !== '1') return null;
      acc = Radd(acc, Rmul(t.c, Rpow(t0, t.k)));
    }
    return acc;
  }
  function EPevalFloat(e, x) {
    var acc = 0, i;
    for (i = 0; i < e.length; i += 1) {
      var t = e[i], v = Rnum(t.c) * Math.pow(x, t.k) * Math.exp(Rnum(t.a) * x);
      if (t.trig === 'cos') v *= Math.cos(Rnum(t.b) * x);
      if (t.trig === 'sin') v *= Math.sin(Rnum(t.b) * x);
      acc += v;
    }
    return acc;
  }
  /* ---- the candidate grammar ----
     Terms joined by + and -. A term is a product of factors, side by side or
     joined by * or ·: a rational (2, 3/4, 0.5, (2/5)), C or D, t or t^k,
     e^(r t) / e^t / e^-t / exp(r t), cos(b t), sin(b t); a trailing /n
     divides. env gives C and D their values for this parse. */
  function EPlinear(src) {
    var s = src.replace(/\s+/g, '').replace(/\*/g, '');
    var bad = 'the rate ' + src + ' is not a rational multiple of t';
    var m = /^([+-]?)([0-9]*\.?[0-9]*)(?:\/([0-9]+))?(t)?(?:\/([0-9]+))?$/.exec(s);
    if (!m || (!m[2] && !m[4])) throw new Error(bad);
    if (/^0+$/.test(m[3] || '1') || /^0+$/.test(m[5] || '1')) throw new Error(bad);
    if (!m[4]) {
      var c = DE_rat(m[1] + m[2] + (m[3] ? '/' + m[3] : ''));
      if (c === null || !Rzero(c)) throw new Error(bad);
      return R0;
    }
    var r = m[2] ? DE_rat(m[2]) : R1;
    if (r === null) throw new Error(bad);
    if (m[3]) r = Rdiv(r, R(BigInt(m[3])));
    if (m[5]) r = Rdiv(r, R(BigInt(m[5])));
    return m[1] === '-' ? Rneg(r) : r;
  }
  function EPparse(text, env) {
    env = env || {};
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/·/g, '*');
    var i = 0, out = [];
    function ws() { while (i < s.length && /\s/.test(s.charAt(i))) i += 1; }
    function group() {
      var close = MPbalanced(s, i);
      if (s.charAt(close) !== ')') throw new Error('a bracket is not closed');
      var inner = s.slice(i + 1, close);
      i = close + 1;
      return inner;
    }
    ws();
    if (i >= s.length) throw new Error('there is no candidate here');
    while (i < s.length) {
      ws();
      var sign = R1, signs = 0;
      while (s.charAt(i) === '+' || s.charAt(i) === '-') {
        if (s.charAt(i) === '-') sign = Rneg(sign);
        i += 1; signs += 1; ws();
      }
      if (signs > 1) throw new Error('two signs in a row');
      if (!out.length || signs) { /* a new term */ } else throw new Error('terms are joined by + or -');
      var term = { c: sign, k: 0, a: R0, b: R0, trig: '1' }, factors = 0, trigs = 0;
      while (i < s.length) {
        ws();
        var ch = s.charAt(i), m;
        if (ch === '+' || ch === '-' || i >= s.length) break;
        if (ch === '*') { i += 1; continue; }
        if ((m = /^[0-9]*\.?[0-9]+(?:\/[0-9]+)?/.exec(s.slice(i))) && m[0].length) {
          var r = DE_rat(m[0]);
          if (r === null) throw new Error('the number ' + m[0] + ' cannot be read');
          term.c = Rmul(term.c, r); i += m[0].length;
        } else if (ch === '/') {
          i += 1; ws();
          m = /^[0-9]+/.exec(s.slice(i));
          if (!m || /^0+$/.test(m[0])) throw new Error('only a division by a whole number other than 0 is in this class');
          term.c = Rdiv(term.c, R(BigInt(m[0]))); i += m[0].length;
          continue;
        } else if (ch === '(') {
          var inner = group(), q = DE_rat(inner);
          if (q === null) throw new Error('(' + inner + ') is not a rational coefficient; write the terms out');
          term.c = Rmul(term.c, q);
        } else if (ch === 'C' || ch === 'D') {
          if (!env.hasOwnProperty(ch)) throw new Error('no value for ' + ch);
          term.c = Rmul(term.c, env[ch]); i += 1;
        } else if (/^(cos|sin)\s*\(/.test(s.slice(i))) {
          var name = s.slice(i, i + 3);
          i += 3; ws();
          if (trigs) throw new Error('a product of two of cos and sin is outside this class');
          trigs += 1;
          term.trig = name; term.b = EPlinear(group());
        } else if (/^exp\s*\(/.test(s.slice(i))) {
          i += 3; ws();
          term.a = Radd(term.a, EPlinear(group()));
        } else if (ch === 'e' && !/^[a-z]/.test(s.slice(i + 1))) {
          i += 1; ws();
          if (s.charAt(i) !== '^') throw new Error('e on its own is a number, not a term of this class; write e^(t)');
          i += 1; ws();
          if (s.charAt(i) === '(') term.a = Radd(term.a, EPlinear(group()));
          else {
            m = /^-?[0-9]*\.?[0-9]*t/.exec(s.slice(i));
            if (!m) throw new Error('write the exponent of e in brackets, as e^(2t)');
            term.a = Radd(term.a, EPlinear(m[0])); i += m[0].length;
          }
        } else if (ch === 't') {
          i += 1; ws();
          var k = 1;
          if (s.charAt(i) === '^') {
            i += 1; ws();
            m = /^\(?([0-9]+)\)?/.exec(s.slice(i));
            if (!m) throw new Error('a power of t must be a whole number');
            k = parseInt(m[1], 10); i += m[0].length;
          }
          term.k += k;
          if (term.k > 12) throw new Error('t^' + term.k + ' is past the power this lab handles, 12');
        } else {
          throw new Error('cannot read ' + s.slice(i, i + 8).replace(/\s+$/, '') + ' as part of a term');
        }
        factors += 1;
      }
      if (!factors) throw new Error('a sign with no term after it');
      out.push(term);
    }
    return EPmake(out);
  }
  /* A candidate with symbolic C and D: parsed at (0, 0), (1, 0), (0, 1), and
     at (1, 1), (2, 0), (0, 2) to check that it is linear in them. */
  function EPfamily(text) {
    var hasC = /C/.test(String(text)), hasD = /D/.test(String(text));
    var p00 = EPparse(text, { C: R0, D: R0 });
    var p10 = EPparse(text, { C: R1, D: R0 }), p01 = EPparse(text, { C: R0, D: R1 });
    var dC = EPsub(p10, p00), dD = EPsub(p01, p00);
    var p11 = EPparse(text, { C: R1, D: R1 });
    var p20 = EPparse(text, { C: R(2n), D: R0 }), p02 = EPparse(text, { C: R0, D: R(2n) });
    if (!EPequal(p11, EPadd(p00, EPadd(dC, dD)))
        || !EPequal(p20, EPadd(p00, EPscale(dC, R(2n))))
        || !EPequal(p02, EPadd(p00, EPscale(dD, R(2n))))) {
      throw new Error('the candidate is not linear in C and D');
    }
    return { base: p00, C: hasC ? dC : [], D: hasD ? dD : [], hasC: hasC, hasD: hasD };
  }
  /* ℒ[tᵏ·g] = (−1)ᵏ dᵏ/dsᵏ ℒ[g], with ℒ[e^(at)] = 1/(s − a),
     ℒ[e^(at) cos bt] = (s − a)/((s − a)² + b²), ℒ[e^(at) sin bt] = b/((s − a)² + b²). */
  function EPlaplace(e) {
    var out = RFconst(R0), i, j;
    for (i = 0; i < e.length; i += 1) {
      var t = e[i], sa = [Rneg(t.a), R1], F;
      if (t.trig === '1') F = RFmake([R1], sa);
      else {
        var q = Padd(Pmul(sa, sa), [Rmul(t.b, t.b)]);
        F = t.trig === 'cos' ? RFmake(sa, q) : RFmake([t.b], q);
      }
      for (j = 0; j < t.k; j += 1) F = RFscale(RFderiv(F), R(-1n));
      out = RFadd(out, RFscale(F, t.c));
    }
    return out;
  }
  /* The inverse: 1/(s − a)ᵏ ↔ tᵏ⁻¹e^(at)/(k − 1)!, and
     (A·s + B)/((s − α)² + β²) ↔ e^(αt)(A·cos βt + ((B + Aα)/β)·sin βt). */
  function EPfromPartial(P) {
    if (P.refused) return { refused: P.refused };
    if (!Pzero(P.poly)) return { refused: 'the transform has a polynomial part, which is not the transform of a function in this class' };
    var terms = [], i;
    for (i = 0; i < P.terms.length; i += 1) {
      var t = P.terms[i], fact = R1, j;
      for (j = 2; j < t.power; j += 1) fact = Rmul(fact, R(BigInt(j)));
      terms.push({ c: Rdiv(t.coef, fact), k: t.power - 1, a: t.root, b: R0, trig: '1' });
    }
    if (P.quad && !(Rzero(P.quad.A) && Rzero(P.quad.B))) {
      var beta = Rsign(P.quad.beta2) > 0 ? Rsqrt(P.quad.beta2) : null;
      if (beta === null) {
        return { refused: 'the factor ' + DE_ptext(P.quad.poly, 's') + ' gives the frequency √(' + DE_q(P.quad.beta2)
          + '), which is irrational; this lab does not print it' };
      }
      terms.push({ c: P.quad.A, k: 0, a: P.quad.alpha, b: beta, trig: 'cos' });
      terms.push({ c: Rdiv(Radd(P.quad.B, Rmul(P.quad.A, P.quad.alpha)), beta), k: 0, a: P.quad.alpha, b: beta, trig: 'sin' });
    }
    return { ep: EPmake(terms) };
  }
"""

# ---------------------------------------------------------------------------
# STEP_JS -- exact steppers with a digit budget.
# ---------------------------------------------------------------------------

STEP_JS = r"""
  /* ---- de_core: exact steppers --------------------------------------------
     Euler, improved Euler (Heun) and Runge-Kutta step a polynomial
     right-hand side exactly. A quadratic right-hand side doubles the digits
     of the denominators at every step, so after each step the state is
     measured and, past DE_DIGITS digits, the run STOPS: the step that broke
     the budget is not kept, and nothing is rounded to continue. */
  var DE_DIGITS = 2000;
  function DE_bdigits(n) { if (n < 0n) n = -n; return n.toString().length; }
  function DE_digits(list) {
    var best = 0, i;
    for (i = 0; i < list.length; i += 1) {
      var w = Math.max(DE_bdigits(list[i].n), DE_bdigits(list[i].d));
      if (w > best) best = w;
    }
    return best;
  }
  function DE_den(list) {
    var best = 0, i;
    for (i = 0; i < list.length; i += 1) { var w = DE_bdigits(list[i].d); if (w > best) best = w; }
    return best;
  }
  function DE_f(f, t, y) { return MPeval(f, { t: t, y: y }); }
  function DE_run(t0, y0, h, n, step) {
    var rows = [{ t: t0, y: y0 }], stopped = false, k, digits = DE_den([t0, y0]);
    for (k = 0; k < n; k += 1) {
      var last = rows[rows.length - 1];
      var next = { t: Radd(last.t, h), y: step(last.t, last.y) };
      if (DE_digits([next.t, next.y]) > DE_DIGITS) { stopped = true; break; }
      rows.push(next);
      digits = Math.max(digits, DE_den([next.t, next.y]));
    }
    return { rows: rows, steps: rows.length - 1, stopped: stopped, digits: digits };
  }
  function DE_euler(f, t0, y0, h, n) {
    return DE_run(t0, y0, h, n, function (t, y) { return Radd(y, Rmul(h, DE_f(f, t, y))); });
  }
  function DE_heun(f, t0, y0, h, n) {
    return DE_run(t0, y0, h, n, function (t, y) {
      var k1 = DE_f(f, t, y), k2 = DE_f(f, Radd(t, h), Radd(y, Rmul(h, k1)));
      return Radd(y, Rmul(Rdiv(h, R(2n)), Radd(k1, k2)));
    });
  }
  function DE_rk4(f, t0, y0, h, n) {
    var half = Rdiv(h, R(2n)), sixth = Rdiv(h, R(6n));
    return DE_run(t0, y0, h, n, function (t, y) {
      var k1 = DE_f(f, t, y);
      var k2 = DE_f(f, Radd(t, half), Radd(y, Rmul(half, k1)));
      var k3 = DE_f(f, Radd(t, half), Radd(y, Rmul(half, k2)));
      var k4 = DE_f(f, Radd(t, h), Radd(y, Rmul(h, k3)));
      var sum = Radd(Radd(k1, Rmul(R(2n), k2)), Radd(Rmul(R(2n), k3), k4));
      return Radd(y, Rmul(sixth, sum));
    });
  }
  /* x′ = f, y′ = g, with names the two unknowns as f and g spell them. */
  function DE_eulerSys(f, g, t0, x0, y0, h, n, names) {
    names = names || ['x', 'y'];
    var rows = [{ t: t0, x: x0, y: y0 }], stopped = false, k, digits = DE_den([t0, x0, y0]);
    for (k = 0; k < n; k += 1) {
      var last = rows[rows.length - 1], pt = { t: last.t };
      pt[names[0]] = last.x; pt[names[1]] = last.y;
      var next = { t: Radd(last.t, h), x: Radd(last.x, Rmul(h, MPeval(f, pt))), y: Radd(last.y, Rmul(h, MPeval(g, pt))) };
      if (DE_digits([next.t, next.x, next.y]) > DE_DIGITS) { stopped = true; break; }
      rows.push(next);
      digits = Math.max(digits, DE_den([next.t, next.x, next.y]));
    }
    return { rows: rows, steps: rows.length - 1, stopped: stopped, digits: digits };
  }
"""

# ---------------------------------------------------------------------------
# DRAW_JS -- the drawings. Floating point, for pixels only.
# ---------------------------------------------------------------------------

DRAW_JS = r"""
  /* ---- de_core: drawing ----------------------------------------------------
     Pixels only. A curve with no closed form is drawn by stepping in floating
     point and the legend says so; every number a tile prints comes from the
     exact side. Everything goes through the Plot api, so it is clipped. */
  function DE_arrows(plot, f, grid) {
    var w = plot.win, n = grid || 15, i, j;
    var cw = (w.xmax - w.xmin) / n, ch = (w.ymax - w.ymin) / n;
    var kx = (w.xmax - w.xmin) / (plot.sx(w.xmax) - plot.sx(w.xmin));
    var ky = (w.ymax - w.ymin) / (plot.sy(w.ymax) - plot.sy(w.ymin));
    var len = 0.34 * Math.min(Math.abs(cw / kx), Math.abs(ch / ky));
    for (i = 0; i < n; i += 1) {
      for (j = 0; j < n; j += 1) {
        var x = w.xmin + (i + 0.5) * cw, y = w.ymin + (j + 0.5) * ch, v = f(x, y), dx, dy;
        if (typeof v === 'number') { dx = 1; dy = v; } else if (v && v.length === 2) { dx = v[0]; dy = v[1]; } else continue;
        if (!isFinite(dx) || !isFinite(dy)) continue;
        var px = dx / kx, py = dy / ky, norm = Math.sqrt(px * px + py * py);
        if (!(norm > 0)) continue;
        var hx = px / norm * len * kx, hy = py / norm * len * ky;
        plot.segment(x - hx, y - hy, x + hx, y + hy, 'plot-tickmark');
      }
    }
    return plot;
  }
  function DE_polyline(plot, pts, cls) {
    var i;
    for (i = 1; i < pts.length; i += 1) {
      var a = pts[i - 1], b = pts[i];
      if (!isFinite(a[0]) || !isFinite(a[1]) || !isFinite(b[0]) || !isFinite(b[1])) continue;
      plot.segment(a[0], a[1], b[0], b[1], cls || 'plot-curve good');
    }
    return plot;
  }
  function DE_rk4float(f, start, h, n) {
    n = n || 400;
    var out = [], k;
    if (start.length === 2) {
      var t = start[0], y = start[1];
      out.push([t, y]);
      for (k = 0; k < n; k += 1) {
        var k1 = f(t, y), k2 = f(t + h / 2, y + h / 2 * k1), k3 = f(t + h / 2, y + h / 2 * k2), k4 = f(t + h, y + h * k3);
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t = t + h;
        if (!isFinite(y) || Math.abs(y) > 1e6) break;
        out.push([t, y]);
      }
      return out;
    }
    var s = start[0], x = start[1], z = start[2];
    out.push([x, z]);
    for (k = 0; k < n; k += 1) {
      var a1 = f(s, x, z), a2 = f(s + h / 2, x + h / 2 * a1[0], z + h / 2 * a1[1]);
      var a3 = f(s + h / 2, x + h / 2 * a2[0], z + h / 2 * a2[1]), a4 = f(s + h, x + h * a3[0], z + h * a3[1]);
      x = x + h / 6 * (a1[0] + 2 * a2[0] + 2 * a3[0] + a4[0]);
      z = z + h / 6 * (a1[1] + 2 * a2[1] + 2 * a3[1] + a4[1]);
      s = s + h;
      if (!isFinite(x) || !isFinite(z) || Math.abs(x) > 1e6 || Math.abs(z) > 1e6) break;
      out.push([x, z]);
    }
    return out;
  }
"""

BLOCKS = {
    "SURD": SURD_JS,
    "SHOW": SHOW_JS,
    "MPOLY": MPOLY_JS,
    "RF": RF_JS,
    "EP": EP_JS,
    "STEP": STEP_JS,
    "DRAW": DRAW_JS,
}

# What each block calls in another. SHOW is shipped on every page.
DEPENDS = {
    "SURD": (),
    "SHOW": (),
    "MPOLY": ("SHOW",),
    "RF": ("SHOW",),
    "EP": ("SHOW", "RF"),
    "STEP": ("SHOW", "MPOLY"),
    "DRAW": (),
}

_ORDER = ("SURD", "SHOW", "MPOLY", "RF", "EP", "STEP", "DRAW")


def script(*names, extra=""):
    """The page script for a mode: algebra_core's four always-shipped blocks,
    then the named de_core blocks with their dependencies, each once, in
    dependency order, then `extra`."""
    want = {"SHOW"}
    stack = list(names)
    while stack:
        name = stack.pop()
        if name not in BLOCKS:
            raise ValueError("de_core has no block %r; the blocks are %s" % (name, ", ".join(_ORDER)))
        if name not in want:
            want.add(name)
            stack.extend(DEPENDS[name])
    out = RATIONAL_JS + POLY_JS + EXPR_JS + PLOT_JS
    for name in _ORDER:
        if name in want:
            out += BLOCKS[name]
    return out + extra


# The algebra_core blocks a page carries unedited. They predate the
# no-double-quote rule (their messages quote a token), so a test of that rule
# strips these first and holds everything de_core and the kits add to it.
ALGEBRA_BLOCKS = (RATIONAL_JS, POLY_JS, EXPR_JS, PLOT_JS, SURD_JS)


# ---------------------------------------------------------------------------
# Data as a JS literal with single quotes only.
# ---------------------------------------------------------------------------

_IDENT = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")


def js(value):
    """A Python value as a JS literal written without a double quote."""
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return json.dumps(value)
    if isinstance(value, Fraction):
        return js(str(value))
    if isinstance(value, str):
        out = value.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
        out = out.replace('"', "\\u0022").replace("</", "<\\/")
        return "'%s'" % out
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(js(v) for v in value) + "]"
    if isinstance(value, dict):
        parts = []
        for k, v in value.items():
            key = str(k)
            parts.append("%s: %s" % (key if _IDENT.match(key) else js(key), js(v)))
        return "{" + ", ".join(parts) + "}"
    raise TypeError("de_core.js cannot write %r" % (value,))


def literal(name, value):
    return "  var %s = %s;\n" % (name, js(value))


# ---------------------------------------------------------------------------
# Markup.
# ---------------------------------------------------------------------------


def attr(text_):
    return (str(text_).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def select(cid, label, options_, chosen_, wrap_id=None):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (attr(v), " selected" if str(v) == str(chosen_) else "", attr(t))
        for v, t in options_
    )
    wid = ' id="%s"' % wrap_id if wrap_id else ""
    return (
        '        <div class="field"%s>\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (wid, cid, label, cid, opts)
    )


def text(cid, label, value, wrap_id=None, label_id=None, disabled=False):
    """A text box. Its shipped value may contain none of > < & " (labcheck
    reads a control's starting value without decoding entities)."""
    value = "" if value is None else str(value)
    for bad in '><&"':
        if bad in value:
            raise ValueError("a control value may not contain %r: %r" % (bad, value))
    wid = ' id="%s"' % wrap_id if wrap_id else ""
    lid = ' id="%s"' % label_id if label_id else ""
    return (
        '        <div class="field"%s>\n          <label for="%s"%s>%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" spellcheck="false"%s>\n'
        "        </div>\n" % (wid, cid, lid, label, cid, value, " disabled" if disabled else "")
    )


def range_(cid, label, lo, hi, value):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="1" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, value)
    )


def kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def hint(text_):
    return '        <p class="small-copy" style="margin:0;">%s</p>\n' % text_


def toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, label)
        for tone, label in legend
    )
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
        '        <div class="inline-legend">%s</div>\n'
        "      </div>\n" % (name, subtitle, swatches)
    )


def stage(inner):
    return '      <div class="lab-stage">%s</div>\n' % inner


def svg(cid, alt):
    return '<svg id="%s" viewBox="0 0 660 420" role="img" aria-label="%s"></svg>' % (cid, attr(alt))


def wrap(cid, top=12):
    return '      <div class="table-wrap" style="margin-top:%dpx;" id="%s"></div>\n' % (top, cid)


def banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


# ---------------------------------------------------------------------------
# Presets: lesson data, validated at build time. A malformed instance raises
# ValueError naming the preset; a missing `expect` does not (labcheck owns it).
# ---------------------------------------------------------------------------


def presets(cfg, kit, mode):
    found = cfg.get("presets")
    if not isinstance(found, list) or not found:
        raise ValueError("%s/%s: cfg['presets'] must be a non-empty list" % (kit, mode))
    seen = set()
    for p in found:
        if not isinstance(p, dict) or not p.get("id") or not p.get("label"):
            raise ValueError("%s/%s: every preset needs an id and a label: %r" % (kit, mode, p))
        pid = str(p["id"])
        if pid in seen:
            raise ValueError("%s/%s: preset id %r is used twice" % (kit, mode, pid))
        if any(c in pid for c in "<>&\"' "):
            raise ValueError("%s/%s: preset id %r may not contain < > & quotes or spaces" % (kit, mode, pid))
        seen.add(pid)
    return found


def check(kit, mode, preset, ok, why):
    if not ok:
        raise ValueError("%s/%s: preset %r: %s" % (kit, mode, preset.get("id"), why))


def chosen(found, cfg, kit, mode):
    want = str(cfg.get("preset", found[0]["id"]))
    for p in found:
        if str(p["id"]) == want:
            return p
    raise ValueError("%s/%s: no preset %r; this lesson has %s"
                     % (kit, mode, want, ", ".join(str(p["id"]) for p in found)))


def choice(cfg, key, allowed, kit, mode):
    value = cfg.get(key, allowed[0])
    value = str(value).lower() if isinstance(value, bool) else str(value)
    if value not in [str(a) for a in allowed]:
        raise ValueError("%s/%s: cfg[%r] must be one of %s, not %r"
                         % (kit, mode, key, ", ".join(str(a) for a in allowed), value))
    return value


_RAT = re.compile(r"^\s*[+-]?\d+(\s*/\s*\d+)?\s*$|^\s*[+-]?\d*\.\d+\s*$")


def rational(value, kit, mode, preset, field, allow_none=False):
    """A preset's rational field as canonical text ('3', '-7/4')."""
    if value is None or (isinstance(value, str) and not value.strip()):
        if allow_none:
            return None
        check(kit, mode, preset, False, "%s is missing" % field)
    if isinstance(value, bool):
        check(kit, mode, preset, False, "%s must be a rational, not %r" % (field, value))
    if isinstance(value, float):
        value = repr(value)
    if isinstance(value, (int, Fraction)):
        return str(Fraction(value))
    s = str(value).replace("−", "-")
    check(kit, mode, preset, bool(_RAT.match(s)),
          "%s must be a rational such as 3, -7/4 or 0.5, not %r" % (field, value))
    try:
        frac = Fraction(s.replace(" ", ""))
    except ZeroDivisionError:
        check(kit, mode, preset, False, "%s has a zero denominator: %r" % (field, value))
    return str(frac)


def formula(value, letters, kit, mode, preset, field, allow_none=False):
    """A typed formula: ASCII digits, operators, brackets and the named
    letters only (a function name passes when each of its letters is named)."""
    if value is None or (isinstance(value, str) and not value.strip()):
        if allow_none:
            return None
        check(kit, mode, preset, False, "%s is missing" % field)
    s = str(value)
    check(kit, mode, preset, all(c in "0123456789+-*/^(). " or c in letters for c in s),
          "%s %r may use only digits, + - * / ^ ( ) . and the letters %s"
          % (field, s, ", ".join(sorted(letters))))
    depth = 0
    for c in s:
        depth += {"(": 1, ")": -1}.get(c, 0)
        check(kit, mode, preset, depth >= 0, "%s %r closes a bracket it never opened" % (field, s))
    check(kit, mode, preset, depth == 0, "%s %r leaves a bracket open" % (field, s))
    return s


def options(found):
    return [(str(p["id"]), p["label"]) for p in found]


def expect(found):
    return {str(p["id"]): dict(p.get("expect") or {}) for p in found}


def lab(cfg, *, title, subtitle, markup, controls, script, panel_title, panel_intro, select, presets):
    return Lab(
        title=title,
        subtitle=subtitle,
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", panel_title),
        panel_intro=cfg.get("panel_intro", panel_intro),
        script=script,
        expect={select: expect(presets)},
    )


__all__ = [
    "SHOW_JS", "MPOLY_JS", "RF_JS", "EP_JS", "STEP_JS", "DRAW_JS", "BLOCKS", "DEPENDS",
    "ALGEBRA_BLOCKS", "script", "js", "literal", "attr", "select", "text", "range_", "kpis",
    "hint", "toolbar", "stage", "svg", "wrap", "banner", "presets", "check", "chosen", "choice",
    "rational", "formula", "options", "expect", "lab",
]
