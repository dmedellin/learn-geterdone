"""dekit, second half: linear1, stiff, char, oscillator, phase, jacobian, laplace.

docs/differential-equations/PLAN.md section D.3; the conventions of D.0 bind
every mode, and the shared blocks come from de_core (D.1). dekit.py dispatches
these modes here, so two engineers can build the fifteen modes without sharing
a file. MODES maps a mode name to a function cfg -> Lab.

  linear1     (lf)  y′ + p(t)·y = q(t): μ, y_h, y_p, the constant, steady state
  stiff       (sk)  Euler's factor 1 − a·h on y′ = −a·y, the bound, backward Euler
  char        (ce)  a·y″ + b·y′ + c·y = 0: roots, general solution, C₁, C₂, W(0)
  oscillator  (os)  m·x″ + c·x′ + k·x = F₀·cos(ωt): every exact quantity
  phase       (pp)  x′ = A·x: trace, determinant, eigen-data, type, exact Euler
  jacobian    (jb)  a polynomial system: equilibria, Jacobians, types, a search
  laplace     (lp)  transforms, the derivative rule, IVPs, partial fractions, steps

PRESETS ARE LESSON DATA. Every mode takes cfg['presets'] (each an id, a label
naming the instance, the instance fields of D.3 and `expect`) and
cfg['preset']. The instances go into a JS table written by de_core.literal and
the Lab carries expect={'XXPreset': {id: expect}}. A preset's change handler
rewrites the instance inputs; a redraw-only select keeps the value the lesson
ships, except lpKind, which D.3 says the preset sets, and jbAt, which lists
the preset's own points and is reset to the first of them.

Module-level JavaScript names here are prefixed DB_ (shared by these modes) or
with the mode's two letters. Every tile is written by textContent; every
figure is exact unless it is printed behind ≈.

DEVIATIONS FROM D.3, each the closest correct thing:

  * Ids a page cannot carry twice: char's coefficient inputs are ceAIn, ceBIn,
    ceCIn (D.3 names the c input ceC, which is also the constants tile), and
    laplace's signal input is lpFIn (lpF is also the transform tile).
  * char numbers the roots r₁ > r₂ (the larger first). Section C's worked lines
    and the ceC and ceW examples fix that order (y = 2·e^(−t) − e^(−2t) has
    C₁ = 2, C₂ = −1 and W(0) = r₂ − r₁ = −1); D.3's ceGeneral example writes
    the other order. Under that one order the surd preset's W(0) is −√5, not
    the √5 that D.3 and section C print.
  * stiff's verdict for the factor −1 exactly is `oscillates without decaying`
    (D.3's table would call it `oscillates and grows`, which is false).
  * linear1 adds a tile lfLast (Euler's last value, steps view) and oscillator
    adds osCross (where a critically damped motion crosses zero), because the
    lessons' worked lines read those figures and D.3 gives them no tile.
  * linear1 with a constant p ≠ 0 and an initial value at t0 ≠ 0 fits no
    constant (it would be (y0 − y_p(t0))·e^(a·t0), not rational): lfC prints —
    and the banner says why; the other tiles still print.
  * laplace inverts with its own partial fractions (LP_partial): RFpartial
    takes one irreducible quadratic and section C's cosine-force needs two,
    (s² + 1)(s² + 4). The time-domain answer is found by solving for the
    coefficients of the exponential-polynomial basis the factors name, and is
    checked by transforming it back.
  * laplace's derivative kind prints ℒ[f] in lpF and ℒ[f′], computed directly,
    in lpY; lpEqual compares lpY with s·F − f(0).
"""

from fractions import Fraction

from . import de_core as dc

KIT = "dekit"


# ---------------------------------------------------------------------------
# Python-side validation helpers.
# ---------------------------------------------------------------------------


def _r(p, mode, field, allow_none=False):
    return dc.rational(p.get(field), KIT, mode, p, field, allow_none=allow_none)


def _f(text_):
    return Fraction(text_)


def _int(p, mode, field, lo, hi, default=None):
    value = p.get(field, default)
    dc.check(KIT, mode, p, isinstance(value, int) and not isinstance(value, bool) and lo <= value <= hi,
             "%s must be a whole number from %d to %d, not %r" % (field, lo, hi, value))
    return value


def _rlist(p, mode, field, lengths, allow_none=False):
    """A list of rationals, as space-separated canonical text."""
    value = p.get(field)
    if value is None:
        dc.check(KIT, mode, p, allow_none, "%s is missing" % field)
        return ""
    dc.check(KIT, mode, p, isinstance(value, (list, tuple)) and len(value) in lengths,
             "%s must be a list of %s rationals" % (field, " or ".join(str(n) for n in lengths)))
    return " ".join(dc.rational(v, KIT, mode, p, field) for v in value)


_EQ_CHARS = set("0123456789+-*/^(). '=")


def _eq(p, mode, field, allow_none=False):
    """A typed equation: ASCII digits, operators, brackets, primes, one = and letters."""
    value = p.get(field)
    if value is None or (isinstance(value, str) and not value.strip()):
        dc.check(KIT, mode, p, allow_none, "%s is missing" % field)
        return None
    s = str(value)
    dc.check(KIT, mode, p, all(c in _EQ_CHARS or ("a" <= c.lower() <= "z") for c in s),
             "%s %r may use only digits, letters, + - * / ^ ( ) . ' and =" % (field, s))
    dc.check(KIT, mode, p, s.count("=") == 1, "%s %r must have exactly one =" % (field, s))
    dc.check(KIT, mode, p, "'" in s, "%s %r has no derivative: write y' for the unknown's rate" % (field, s))
    depth = 0
    for c in s:
        depth += {"(": 1, ")": -1}.get(c, 0)
        dc.check(KIT, mode, p, depth >= 0, "%s %r closes a bracket it never opened" % (field, s))
    dc.check(KIT, mode, p, depth == 0, "%s %r leaves a bracket open" % (field, s))
    return s


def _formula(p, mode, field, letters, allow_none=False):
    return dc.formula(p.get(field), letters, KIT, mode, p, field, allow_none=allow_none)


_EP_LETTERS = set("tecosinpxCD")


# ---------------------------------------------------------------------------
# DB_JS: the helpers these seven modes share.
# ---------------------------------------------------------------------------

DB_JS = r"""
  /* ---- dekit (second half): shared helpers ------------------------------- */
  function DB_need(text, what) {
    var r = DE_rat(text);
    if (r === null) throw new Error(what + ' must be a rational number such as 2, -1/2 or 0.25');
    return r;
  }
  /* numbers separated by spaces or commas; counts lists the lengths allowed */
  function DB_list(text, what, counts) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-').replace(/,/g, ' ');
    s = s.replace(/^\s+|\s+$/g, '');
    var parts = s.length ? s.split(/\s+/) : [], out = [], i;
    if (counts.indexOf(parts.length) < 0) {
      if (counts.length === 1 && counts[0] === 1) throw new Error(what + ': type one number');
      throw new Error(what + ': type ' + counts.join(' or ') + ' numbers, separated by spaces');
    }
    for (i = 0; i < parts.length; i += 1) out.push(DB_need(parts[i], what));
    return out;
  }
  function DB_blank(text) { return !/\S/.test(String(text === undefined || text === null ? '' : text)); }
  function DB_bdig(n) { if (n < 0n) n = -n; return n.toString().length; }
  /* a step h: a positive rational, denominator at most 10⁶, and the last t
     within 10⁶ of 0 (D.0's caps) */
  function DB_step(text, n, t0) {
    var h = DB_need(text, 'h');
    if (Rsign(h) <= 0) throw new Error('h must be positive');
    if (h.d > 1000000n) throw new Error('h must have a denominator of at most 1000000');
    var last = Radd(t0 || R0, Rmul(h, R(BigInt(n))));
    if (Rcmp(Rabs(last), R(1000000n)) > 0) throw new Error('n·h takes t past 1000000');
    return h;
  }
  function DB_range(id) {
    var el = DE_el(id), v = parseInt(el.value, 10);
    var lo = parseInt(el.getAttribute('min') || '1', 10), hi = parseInt(el.getAttribute('max') || '64', 10);
    if (!isFinite(lo)) lo = 1;
    if (!isFinite(hi)) hi = 64;
    if (!isFinite(v)) v = lo;
    if (v < lo) v = lo;
    if (v > hi) v = hi;
    DE_set(id + 'Out', v);
    return v;
  }
  /* e^(rt) as the library writes it: e^t, e^(−2t), e^(t/20); '' when r = 0 */
  function DB_exp(r, v) {
    v = v || 't';
    if (Rzero(r)) return '';
    if (Requ(r, R1)) return 'e^' + v;
    return 'e^(' + DE_lin(r, v) + ')';
  }
  /* name times e^(rt): C₁·e^(−t), or the name alone when r = 0 */
  function DB_times(name, r) { return Rzero(r) ? name : name + '·' + DB_exp(r); }
  /* signed pieces joined: the first as it is, the rest with + or − */
  function DB_join(list) {
    var out = '', i;
    for (i = 0; i < list.length; i += 1) {
      var s = list[i];
      if (s === '' || s === '0') continue;
      if (out === '') out = s;
      else if (s.charAt(0) === '−') out += ' − ' + s.slice(1);
      else out += ' + ' + s;
    }
    return out === '' ? '0' : out;
  }
  function DB_window(fns, xmin, xmax) {
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
    var qlo = ys[Math.floor(ys.length * 0.04)], qhi = ys[Math.ceil(ys.length * 0.96) - 1];
    if (hi - lo > 8 * Math.max(qhi - qlo, 1e-9)) { lo = qlo; hi = qhi; }
    if (lo > 0) lo = Math.min(0, lo - 0.1 * (hi - lo));
    if (hi < 0) hi = Math.max(0, hi + 0.1 * (hi - lo));
    if (hi - lo < 1e-9) { lo -= 1; hi += 1; }
    var pad = 0.1 * (hi - lo);
    return { xmin: xmin, xmax: xmax, ymin: lo - pad, ymax: hi + pad };
  }
  function DB_plot(id, win, alt) {
    var plot = Plot(DE_el(id), win).frame();
    plot.describe(alt);
    return plot;
  }
"""

# Shared pieces only some modes ship, to keep each page's script to what it uses.
DB_TAB_JS = r"""
  function DB_table(caption, head, rows) {
    var h = '<table class=tt><caption>' + DE_esc(caption) + '</caption><thead><tr>', i, j;
    for (i = 0; i < head.length; i += 1) h += '<th>' + DE_esc(head[i]) + '</th>';
    h += '</tr></thead><tbody>';
    for (i = 0; i < rows.length; i += 1) {
      h += '<tr>';
      for (j = 0; j < rows[i].length; j += 1) h += '<td>' + DE_esc(rows[i][j]) + '</td>';
      h += '</tr>';
    }
    return h + '</tbody></table>';
  }
"""

DB_ROOT_JS = r"""
  function DB_vec(x, y) { return '(' + DE_q(x) + ', ' + DE_q(y) + ')'; }
  /* a nonzero rational vector as whole numbers in lowest terms, the first
     nonzero entry positive: (2, −2) is (1, −1) */
  function DB_intvec(x, y) {
    var den = x.d * y.d / bgcd(x.d, y.d);
    var a = x.n * (den / x.d), b = y.n * (den / y.d);
    var g = bgcd(a < 0n ? -a : a, b < 0n ? -b : b);
    if (g === 0n) return [R0, R0];
    a /= g; b /= g;
    if (a < 0n || (a === 0n && b < 0n)) { a = -a; b = -b; }
    return [R(a), R(b)];
  }
  /* the roots of a quadratic in the tile vocabulary: −2, −1 | −2 (repeated) |
     −1 ± 2i | ±2i | (1 ± √5)/2 */
  function DB_roottext(qr) {
    if (qr.kind === 'double') return DE_q(qr.p) + ' (repeated)';
    /* an irrational imaginary part is written i√2, never √2i, which reads
       as the root of 2i */
    return DE_root(qr.p, qr.s, qr.kind === 'complex').replace(/([0-9]*)√([0-9]+)i/, '$1i√$2');
  }
  /* √r: exact when rational, else the surd and its rounded value */
  function DB_sqrt(r) {
    var s = Rsurd(r);
    if (s.k === 1n) return DE_q(s.q);
    return DE_root(null, s) + ' ' + DE_dec(Math.sqrt(DE_float(r)));
  }
  /* the type of the origin for x′ = A·x from the trace, the determinant and
     the discriminant; scalar is true when A is a multiple of I */
  function DB_type(tau, det, disc, scalar) {
    if (Rsign(det) < 0) return 'saddle';
    if (Rzero(det)) return 'non-isolated equilibria';
    if (Rsign(disc) > 0) return Rsign(tau) < 0 ? 'stable node' : 'unstable node';
    if (Rzero(disc)) return scalar ? 'star node' : 'degenerate node';
    if (Rzero(tau)) return 'centre';
    return Rsign(tau) < 0 ? 'stable spiral' : 'unstable spiral';
  }
"""

# ---------------------------------------------------------------------------
# DB_EQ_JS: reading a linear equation typed as lhs = rhs (linear1, laplace).
# ---------------------------------------------------------------------------

DB_EQ_JS = r"""
  /* ---- dekit: reading a linear equation ---------------------------------
     The equation is split into terms at the + and − signs outside brackets.
     A term holding the unknown (y, y′ or y″; any letter but t and e) is a
     coefficient times it, read as a rational function of t; every other term
     is forcing, moved to the right-hand side. A term with the unknown twice,
     inside a bracket, under a power or in a denominator is refused: the
     equation is then not linear, or must be multiplied out first. */
  function DB_terms(side) {
    var out = [], depth = 0, cur = '', neg = false, prev = '', i;
    for (i = 0; i < side.length; i += 1) {
      var ch = side.charAt(i);
      if (ch === '(') depth += 1;
      if (ch === ')') { depth -= 1; if (depth < 0) throw new Error('a bracket is closed that was never opened'); }
      if (depth === 0 && (ch === '+' || ch === '-') && '^*/('.indexOf(prev) < 0) {
        if (/\S/.test(cur)) { out.push({ neg: neg, text: cur.replace(/^\s+|\s+$/g, '') }); cur = ''; neg = ch === '-'; }
        else if (ch === '-') neg = !neg;
        prev = ch;
        continue;
      }
      cur += ch;
      if (/\S/.test(ch)) prev = ch;
    }
    if (depth > 0) throw new Error('a bracket is not closed');
    if (/\S/.test(cur)) out.push({ neg: neg, text: cur.replace(/^\s+|\s+$/g, '') });
    else if (prev === '+' || prev === '-') throw new Error('a sign with no term after it');
    return out;
  }
  /* where the unknown u stands in a term, skipping the names cos, sin, exp */
  function DB_find(s, u) {
    var hits = [], depth = 0, i;
    for (i = 0; i < s.length; i += 1) {
      var ch = s.charAt(i);
      if (/^(cos|sin|exp)\s*\(/.test(s.slice(i))) { i += 2; continue; }
      if (ch === '(') depth += 1;
      else if (ch === ')') depth -= 1;
      else if (ch === u) {
        var j = i + 1, primes = 0;
        while (s.charAt(j) === '\'') { primes += 1; j += 1; }
        hits.push({ at: i, end: j, depth: depth, primes: primes });
      }
    }
    return hits;
  }
  function DB_term(term, u) {
    var hits = DB_find(term.text, u), s = term.text;
    if (!hits.length) return null;
    var hit = hits[0], name = u + new Array(hit.primes + 1).join('′');
    if (hits.length > 1) throw new Error('the term ' + s + ' holds ' + u + ' twice, so the equation is not linear');
    if (hit.depth > 0) {
      if (/(sin|cos|tan|exp|ln|log|sqrt|abs)\s*\(/.test(s)) throw new Error(name + ' is inside a function in ' + s + ', so the equation is not linear');
      throw new Error('multiply out the bracket around ' + name + ' in ' + s);
    }
    if (hit.primes > 2) throw new Error('this lab reads up to ' + u + '′′; ' + s + ' has a higher derivative');
    var after = s.slice(hit.end).replace(/^\s+/, '');
    if (after.charAt(0) === '^') throw new Error(name + ' is raised to a power in ' + s + ', so the equation is not linear');
    var coef = (s.slice(0, hit.at) + ' ' + s.slice(hit.end)).replace(/^\s+|\s+$/g, '');
    coef = coef.replace(/\*\s*\//g, '/').replace(/^[*]\s*/, '').replace(/\s*[*]$/, '').replace(/^\s+|\s+$/g, '');
    if (coef.charAt(coef.length - 1) === '/') throw new Error(name + ' is in a denominator in ' + s + ', so the equation is not linear');
    if (coef.charAt(0) === '/') coef = '1' + coef;
    var F;
    if (coef === '') F = RFconst(R1);
    else {
      try { F = RFparse(coef, 't'); } catch (e) {
        throw new Error('the coefficient ' + coef + ' of ' + name + ' cannot be read: ' + DE_msg(e));
      }
    }
    return { order: hit.primes, coef: term.neg ? RFscale(F, R(-1n)) : F };
  }
  /* lhs = rhs as the coefficients of y, y′, y″ (rational functions of t) in
     lhs − rhs, and the forcing terms, each signed as it stands on the right */
  function DB_eqparse(text, reserved) {
    var s = String(text === undefined || text === null ? '' : text);
    s = s.replace(/−/g, '-').replace(/·/g, '*').replace(/[′’]/g, '\'').replace(/″/g, '\'\'');
    if (!/\S/.test(s)) throw new Error('there is no equation here');
    var sides = s.split('=');
    if (sides.length !== 2) throw new Error('write one equation, lhs = rhs, with exactly one =');
    var m = /([A-Za-z])\s*'/.exec(s);
    if (!m) throw new Error('there is no derivative here: write the unknown with a prime, as y\'');
    var u = m[1], all = s.match(/[A-Za-z]\s*'/g), i, j;
    for (i = 0; i < all.length; i += 1) {
      if (all[i].charAt(0) !== u) throw new Error('two letters carry primes, ' + u + ' and ' + all[i].charAt(0) + '; this lab solves for one unknown');
    }
    if (u === 't' || u === 'e' || (reserved && reserved.indexOf(u) >= 0)) {
      throw new Error('the letter ' + u + ' is reserved here; call the unknown y');
    }
    s = s.replace(new RegExp(u + '\\s+\'', 'g'), u + '\'');
    sides = s.split('=');
    var coef = [RFconst(R0), RFconst(R0), RFconst(R0)], forcing = [], order = 0;
    for (j = 0; j < 2; j += 1) {
      var terms = DB_terms(sides[j]);
      if (!terms.length) throw new Error('one side of the equation is empty');
      for (i = 0; i < terms.length; i += 1) {
        var t = terms[i];
        if (j === 1) t = { neg: !t.neg, text: t.text };
        var got = DB_term(t, u);
        if (got) coef[got.order] = RFadd(coef[got.order], got.coef);
        else forcing.push({ neg: !t.neg, text: t.text });
      }
    }
    for (i = 0; i < 3; i += 1) if (!RFzero(coef[i])) order = i;
    if (order === 0) throw new Error('the derivatives of ' + u + ' cancel; there is no differential equation left');
    return { u: u, coef: coef, forcing: forcing, order: order };
  }
  /* forcing terms as one exponential polynomial in t */
  function DB_forcing(list) {
    var out = [], i;
    for (i = 0; i < list.length; i += 1) {
      var e;
      try { e = EPparse(list[i].text, {}); } catch (err) {
        throw new Error('the forcing term ' + list[i].text + ' is outside this lab: ' + DE_msg(err));
      }
      out = EPadd(out, list[i].neg ? EPscale(e, R(-1n)) : e);
    }
    return out;
  }
  function DB_isconst(F) { return RFispoly(F) && Pdeg(F.num) <= 0; }
  function DB_cval(F) { return F.num.length ? F.num[0] : R0; }
"""

# ---------------------------------------------------------------------------
# linear1 (lf)
# ---------------------------------------------------------------------------

LINEAR1_JS = r"""
  /* ---- dekit/linear1: y′ + p(t)·y = q(t) -----------------------------------
     Normalised by the coefficient of y′. A constant p = a gives μ = e^(at) and
     y_h = C·e^(−at); y_p is found by undetermined coefficients, an exact
     linear system for each exponential-trigonometric family in q (times t
     when the family is e^(−at) itself). p = a/t gives μ = tᵃ and
     y = (∫tᵃ·q dt + C)/tᵃ, a sum of powers of t, every coefficient a fraction. */
  function DB_coefof(e, k, a, b, trig) {
    var i;
    for (i = 0; i < e.length; i += 1) {
      var t = e[i];
      if (t.k === k && Requ(t.a, a) && Requ(t.b, b) && t.trig === trig) return t.c;
    }
    return R0;
  }
  /* y_p for y′ + a·y = q, q an exponential polynomial */
  function lfUndet(q, a) {
    var groups = [], seen = {}, out = [], i, j, k;
    for (i = 0; i < q.length; i += 1) {
      var key = Rtext(q[i].a) + '|' + Rtext(q[i].b);
      if (!seen.hasOwnProperty(key)) { seen[key] = groups.length; groups.push({ al: q[i].a, b: q[i].b, K: 0 }); }
      var g0 = groups[seen[key]];
      if (q[i].k > g0.K) g0.K = q[i].k;
    }
    for (j = 0; j < groups.length; j += 1) {
      var g = groups[j], res = Rzero(g.b) && Requ(g.al, Rneg(a));
      var trigs = Rzero(g.b) ? ['1'] : ['cos', 'sin'], basis = [], targets = [], tr;
      for (k = 0; k <= g.K; k += 1) {
        for (tr = 0; tr < trigs.length; tr += 1) {
          basis.push({ k: res ? k + 1 : k, trig: trigs[tr] });
          targets.push({ k: k, trig: trigs[tr] });
        }
      }
      var images = basis.map(function (bb) {
        var e = EPmake([{ c: R1, k: bb.k, a: g.al, b: g.b, trig: bb.trig }]);
        return EPadd(EPderiv(e), EPscale(e, a));
      });
      var M = [], rhs = [];
      for (i = 0; i < targets.length; i += 1) {
        var row = [];
        for (k = 0; k < images.length; k += 1) row.push(DB_coefof(images[k], targets[i].k, g.al, g.b, targets[i].trig));
        M.push(row);
        rhs.push(DB_coefof(q, targets[i].k, g.al, g.b, targets[i].trig));
      }
      var x = RFsolve(M, rhs);
      if (x === null) throw new Error('the coefficient system for the particular solution is singular');
      for (i = 0; i < basis.length; i += 1) out.push({ c: x[i], k: basis[i].k, a: g.al, b: g.b, trig: basis[i].trig });
    }
    return EPmake(out);
  }
  /* sums of c·tᵖ with whole p of either sign: [{p, c}], descending p */
  function lfLaurent(list) {
    var map = {}, keys = [], out = [], i;
    for (i = 0; i < list.length; i += 1) {
      var key = String(list[i].p);
      if (!map.hasOwnProperty(key)) { map[key] = { p: list[i].p, c: R0 }; keys.push(key); }
      map[key].c = Radd(map[key].c, list[i].c);
    }
    for (i = 0; i < keys.length; i += 1) if (!Rzero(map[keys[i]].c)) out.push(map[keys[i]]);
    out.sort(function (x, y) { return y.p - x.p; });
    return out;
  }
  /* t³/5 + (4/5)/t², t/2 + (3/2)/t */
  function lfLtext(L) {
    var pieces = [], i;
    for (i = 0; i < L.length; i += 1) {
      var c = L[i].c, p = L[i].p;
      if (p >= 0) { pieces.push(DE_sum([{ c: c, body: p === 0 ? '' : (p === 1 ? 't' : 't' + DE_sup(p)), dot: false }])); continue; }
      var den = 't' + (p === -1 ? '' : DE_sup(-p)), mag = Rabs(c), num;
      if (Requ(mag, R1)) num = '1';
      else if (mag.d === 1n) num = String(mag.n);
      else num = '(' + Rtext(mag) + ')';
      pieces.push((c.n < 0n ? '−' : '') + num + '/' + den);
    }
    return DB_join(pieces);
  }
  function lfLeval(L, t) {
    var acc = R0, i;
    for (i = 0; i < L.length; i += 1) {
      var p = L[i].p, pw = p >= 0 ? Rpow(t, p) : Rinv(Rpow(t, -p));
      acc = Radd(acc, Rmul(L[i].c, pw));
    }
    return acc;
  }
  function lfLfloat(L, t) {
    var acc = 0, i;
    for (i = 0; i < L.length; i += 1) acc += Rnum(L[i].c) * Math.pow(t, L[i].p);
    return acc;
  }
  /* tᵖ alone, and C times tᵖ */
  function lfPow(p) {
    if (p === 0) return '1';
    if (p > 0) return p === 1 ? 't' : 't' + DE_sup(p);
    return '1/t' + (p === -1 ? '' : DE_sup(-p));
  }
  function lfCpow(p) {
    if (p === 0) return 'C';
    if (p > 0) return 'C·' + lfPow(p);
    return 'C/t' + (p === -1 ? '' : DE_sup(-p));
  }
  function lfSolve(eqText, icText) {
    var E = DB_eqparse(eqText, []), u = E.u, i;
    if (E.order !== 1) throw new Error('this lab solves first-order equations, and ' + u + '′′ makes this one second order');
    var A = E.coef[1], B = E.coef[0], qraw = DB_forcing(E.forcing), q, r = { u: u };
    if (DB_isconst(A)) q = EPscale(qraw, Rinv(DB_cval(A)));
    else {
      var nz = [];
      for (i = 0; i < A.num.length; i += 1) if (!Rzero(A.num[i])) nz.push(i);
      if (!RFispoly(A) || nz.length !== 1) {
        throw new Error('the coefficient of ' + u + '′ is ' + RFtext(A, 't') + '; this lab divides by a constant or a multiple of a power of t');
      }
      var m = nz[0], c = A.num[m], qt = [];
      if (!EPispoly(qraw)) throw new Error('q(t) would be ' + EPtext(qraw) + ' divided by ' + RFtext(A, 't') + ', outside the forms this lab solves');
      for (i = 0; i < qraw.length; i += 1) {
        if (qraw[i].k < m) throw new Error('dividing by ' + RFtext(A, 't') + ' leaves a negative power of t in q(t)');
        qt.push({ c: Rdiv(qraw[i].c, c), k: qraw[i].k - m, a: R0, b: R0, trig: '1' });
      }
      q = EPmake(qt);
    }
    var p = RFdiv(B, A);
    r.p = p; r.q = q;
    r.ic = DB_blank(icText) ? null : DB_list(icText, 'the initial value t0 y0', [2]);
    if (DB_isconst(p)) return lfConstant(r, DB_cval(p));
    var a = p.num.length === 1 ? p.num[0] : null;
    var overT = a !== null && p.den.length === 2 && Rzero(p.den[0]) && Requ(p.den[1], R1);
    if (!overT || !Rint(a) || a.n > 4n || a.n < -4n || a.n === 0n) {
      throw new Error('p(t) = ' + RFtext(p, 't') + '; this lab solves a constant p, or a/t with a a whole number from −4 to 4');
    }
    if (!EPispoly(q)) throw new Error('with p = ' + RFtext(p, 't') + ' this lab takes q(t) a polynomial, not ' + EPtext(q));
    return lfOverT(r, Number(a.n));
  }
  function lfConstant(r, a) {
    r.kind = 'const'; r.a = a;
    r.mu = Rzero(a) ? '1' : DB_exp(a);
    r.yh = DB_times('C', Rneg(a));
    r.yp = lfUndet(r.q, a);
    r.ypText = EPtext(r.yp);
    r.C = null; r.why = '';
    if (r.ic) {
      var t0 = r.ic[0], y0 = r.ic[1];
      if (Rzero(t0) || Rzero(a)) {
        var at = EPevalExact(r.yp, t0);
        if (at === null) r.why = 'y_p is not rational at t0 = ' + DE_q(t0) + ', so the constant is not fitted; this lab fits at t0 = 0';
        else r.C = Rsub(y0, at);
      } else {
        r.why = 'at t0 = ' + DE_q(t0) + ' the constant would be (y0 − y_p(t0))·e^(' + DE_lin(a, 't0') + '), which is not rational; this lab fits at t0 = 0';
      }
    }
    var qconst = EPispoly(r.q) && (r.q.length === 0 || (r.q.length === 1 && r.q[0].k === 0));
    if (!Rzero(a) && qconst) {
      var b = r.q.length ? r.q[0].c : R0;
      r.steady = DE_q(Rdiv(b, a)) + (Rsign(a) < 0 ? ' (repelling)' : '');
    } else r.steady = 'none';
    var hpart = r.C === null ? r.yh : (Rzero(r.C) ? '' : EPtext(EPmake([{ c: r.C, k: 0, a: Rneg(a), b: R0, trig: '1' }])));
    r.solution = r.u + ' = ' + DB_join([r.yp.length ? r.ypText : '', hpart]);
    var self = r;
    r.ypF = function (t) { return EPevalFloat(self.yp, t); };
    r.yhF = function (t, C) { return C * Math.exp(-Rnum(a) * t); };
    return r;
  }
  function lfOverT(r, a) {
    r.kind = 'overT'; r.a = R(BigInt(a));
    r.mu = lfPow(a);
    r.yh = lfCpow(-a);
    var integ = [], i;
    for (i = 0; i < r.q.length; i += 1) {
      var pw = r.q[i].k + a;
      if (pw === -1) throw new Error('the integral of tᵃ·q(t) has a ln t term, which this lab does not print');
      integ.push({ p: pw + 1 - a, c: Rdiv(r.q[i].c, R(BigInt(pw + 1))) });
    }
    r.ypL = lfLaurent(integ);
    r.ypText = lfLtext(r.ypL);
    r.C = null; r.why = '';
    if (r.ic) {
      var t0 = r.ic[0], y0 = r.ic[1];
      if (Rzero(t0)) throw new Error('with p = ' + RFtext(r.p, 't') + ' the equation is not defined at t0 = 0; give the initial value at a t0 other than 0');
      var t0a = a >= 0 ? Rpow(t0, a) : Rinv(Rpow(t0, -a));
      r.C = Rmul(Rsub(y0, lfLeval(r.ypL, t0)), t0a);
    }
    r.steady = 'none';
    if (r.C === null) r.solution = r.u + ' = ' + DB_join([r.ypL.length ? r.ypText : '', r.yh]);
    else r.solution = r.u + ' = ' + lfLtext(lfLaurent(r.ypL.concat([{ p: -a, c: r.C }])));
    var self = r;
    r.ypF = function (t) { return lfLfloat(self.ypL, t); };
    r.yhF = function (t, C) { return C * Math.pow(t, -a); };
    return r;
  }
  /* exact Euler from the initial value, for a constant p and a polynomial q */
  function lfSteps(r, h, n) {
    if (r.kind !== 'const') return { why: 'Euler steps are shown for a constant p only' };
    if (!r.ic) return { why: 'give an initial value t0 y0 to step from' };
    if (!EPispoly(r.q)) return { why: 'q(t) = ' + EPtext(r.q) + ' is not rational at the step points, so the steps would not be exact' };
    var rows = [{ t: r.ic[0], y: r.ic[1] }], k;
    for (k = 0; k < n; k += 1) {
      var last = rows[rows.length - 1], qv = EPevalExact(r.q, last.t);
      var next = { t: Radd(last.t, h), y: Radd(last.y, Rmul(h, Rsub(qv, Rmul(r.a, last.y)))) };
      if (Math.max(DB_bdig(next.y.n), DB_bdig(next.y.d)) > 2000) return { rows: rows, stopped: true };
      rows.push(next);
    }
    return { rows: rows, stopped: false, factor: Rsub(R1, Rmul(r.a, h)) };
  }
"""


def _linear1(cfg):
    mode = "linear1"
    found = dc.presets(cfg, KIT, mode)
    view = dc.choice(cfg, "view", ["solve", "parts", "steps"], KIT, mode)
    table = {}
    for p in found:
        h = _r(p, mode, "h", allow_none=True) or "1/4"
        dc.check(KIT, mode, p, _f(h) > 0, "h must be positive")
        table[str(p["id"])] = {"eq": _eq(p, mode, "equation"), "ic": _rlist(p, mode, "ic", (2,), allow_none=True),
                               "h": h, "n": _int(p, mode, "n", 1, 64, default=4)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Integrating factor μ", "lfMu"), ("Homogeneous solution y_h", "lfYh"),
             ("Particular solution y_p", "lfYp"), ("Constant C", "lfC"), ("Steady state", "lfSteady"),
             ("Solution", "lfSolution"), ("Euler's last value (steps view)", "lfLast")]
    markup = (
        dc.toolbar("A first-order linear equation", "y′ + p(t)·y = q(t), solved symbolically",
                   [("cyan", "solution"), ("purple", "y_p"), ("muted", "y_h"), ("green", "Euler's steps (exact)")])
        + dc.stage(dc.svg("lfPlot", "the solution of the linear equation"))
        + dc.wrap("lfTable")
        + dc.banner("lfStatus")
    )
    controls = (
        dc.select("lfPreset", "Equation", dc.options(found), pick["id"])
        + dc.text("lfEq", "Equation", first["eq"])
        + dc.text("lfIC", "Initial value t0 y0 (may be empty)", first["ic"])
        + dc.text("lfH", "Step h (steps view)", first["h"])
        + dc.range_("lfN", "Steps n (steps view)", 1, 64, first["n"])
        + dc.select("lfView", "View", [("solve", "the solution"), ("parts", "y_h and y_p"),
                                       ("steps", "Euler's steps")], view)
        + dc.kpis(tiles)
        + dc.hint("Type the equation with a prime: 2y' + 6y = 4t, t y' - 2y = 0, y' + 2y = cos(t).")
    )
    glue = dc.literal("LFP", table) + r"""
  var LF_TILES = ['lfMu', 'lfYh', 'lfYp', 'lfC', 'lfSteady', 'lfSolution', 'lfLast'];
  var lfPresetIn = DE_el('lfPreset'), lfEqIn = DE_el('lfEq'), lfICIn = DE_el('lfIC'), lfHIn = DE_el('lfH');
  var lfNIn = DE_el('lfN'), lfViewIn = DE_el('lfView');
  function lfRender(r, view) {
    var steps = null, h = null, n = DB_range('lfN'), note = '';
    DE_set('lfMu', r.mu);
    DE_set('lfYh', r.yh);
    DE_set('lfYp', r.ypText);
    DE_set('lfC', r.C === null ? '—' : DE_q(r.C));
    DE_set('lfSteady', r.steady);
    DE_set('lfSolution', r.solution);
    DE_set('lfLast', '—');
    DE_html('lfTable', '');
    if (view === 'steps') {
      try { h = DB_step(lfHIn.value, n, r.ic ? r.ic[0] : R0); steps = lfSteps(r, h, n); }
      catch (e) { steps = { why: DE_msg(e) }; }
      if (steps.rows) {
        var last = steps.rows[steps.rows.length - 1], rows = [], i;
        DE_set('lfLast', DE_q(last.y));
        for (i = 0; i < steps.rows.length; i += 1) {
          var sr = steps.rows[i], tf = DE_float(sr.t);
          rows.push([String(i), DE_q(sr.t), DE_q(sr.y), r.C === null ? '—' : DE_dec(r.ypF(tf) + r.yhF(tf, DE_float(r.C)))]);
        }
        DE_html('lfTable', DB_table('Euler with h = ' + DE_q(h) + (steps.factor ? '; each step multiplies the gap to the steady state by 1 − p·h = ' + DE_q(steps.factor) : ''),
          ['n', 'tₙ', r.u + 'ₙ, exact', r.u + '(tₙ), rounded'], rows));
        note = ' Euler with h = ' + DE_q(h) + ' reaches ' + r.u + ' = ' + DE_q(last.y) + ' at t = ' + DE_q(last.t)
          + (steps.stopped ? ', where the digit budget stopped it' : '') + '.';
      } else note = ' No steps: ' + steps.why + '.';
    }
    var t0 = r.ic ? DE_float(r.ic[0]) : (r.kind === 'overT' ? 0.25 : 0);
    var span = r.kind === 'const' && !Rzero(r.a) ? Math.max(4, Math.min(40, 5 / Math.abs(Rnum(r.a)))) : 4;
    var lo = r.kind === 'overT' ? Math.max(0.05, Math.min(t0, 0.25)) : Math.min(0, t0), hi = t0 + span;
    var Cf = r.C === null ? 1 : DE_float(r.C), fns, drawC = r.C === null ? [-2, -1, 0, 1, 2] : [Cf];
    var full = function (C) { return function (t) { return r.ypF(t) + r.yhF(t, C); }; };
    var yhC = function (t) { return r.yhF(t, Cf); };
    fns = view === 'parts' ? [r.ypF, yhC, full(Cf)] : drawC.map(full);
    var plot = DB_plot('lfPlot', DB_window(fns, lo, hi), 'the solution ' + r.solution);
    if (view === 'parts') plot.curve(yhC, 'plot-curve parent').curve(r.ypF, 'plot-curve alt').curve(full(Cf));
    else {
      fns.forEach(function (fn) { plot.curve(fn); });
      if (steps && steps.rows) {
        for (var k = 1; k < steps.rows.length; k += 1) {
          var a0 = steps.rows[k - 1], a1 = steps.rows[k];
          plot.segment(DE_float(a0.t), DE_float(a0.y), DE_float(a1.t), DE_float(a1.y), 'plot-curve good');
        }
      }
    }
    DE_ok('lfStatus', '<strong>Exact.</strong> In standard form p(t) = ' + DE_esc(RFtext(r.p, 't')) + ' and q(t) = '
      + DE_esc(EPtext(r.q)) + '; μ = ' + DE_esc(r.mu) + ', y_h = ' + DE_esc(r.yh) + ', y_p = ' + DE_esc(r.ypText) + '. '
      + (r.C !== null ? 'The initial value ' + DE_esc(r.u) + '(' + DE_esc(DE_q(r.ic[0])) + ') = ' + DE_esc(DE_q(r.ic[1])) + ' gives C = ' + DE_esc(DE_q(r.C)) + '.'
        : (r.why ? DE_esc(r.why) + '.' : 'With no initial value C stays free; the drawing shows C from −2 to 2.'))
      + DE_esc(note) + (view === 'steps' ? ' The polygon is the exact steps; the curve is the closed form.' : ''));
  }
  function redraw() {
    var r;
    try {
      r = lfSolve(lfEqIn.value, lfICIn.value);
    } catch (e) {
      DE_refuse('lfStatus', LF_TILES, ['lfPlot', 'lfTable'], DE_msg(e)); return;
    }
    lfRender(r, lfViewIn.value);
  }
  lfPresetIn.addEventListener('change', function () {
    var p = LFP[lfPresetIn.value];
    if (p) { lfEqIn.value = p.eq; lfICIn.value = p.ic; lfHIn.value = p.h; lfNIn.value = String(p.n); }
    redraw();
  });
  [lfEqIn, lfICIn, lfHIn, lfNIn].forEach(function (el) { el.addEventListener('input', redraw); });
  lfViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="First-order linear equations", subtitle="μ, y_h, y_p and the constant, exactly",
        markup=markup, controls=controls,
        script=dc.script("EP", extra=DB_JS + DB_TAB_JS + DB_EQ_JS + LINEAR1_JS + glue),
        panel_title="Choose the equation",
        panel_intro="The lab divides by the coefficient of y′, reads p and q, and solves: the integrating factor, "
                    "the homogeneous solution, one particular solution and the constant from the initial value.",
        select="lfPreset", presets=found,
    )



# ---------------------------------------------------------------------------
# stiff (sk)
# ---------------------------------------------------------------------------

STIFF_JS = r"""
  /* ---- dekit/stiff: Euler's factor on y′ = −a·y -----------------------------
     One forward Euler step multiplies y by 1 − a·h, one backward step by
     1/(1 + a·h); the sequence is y0 times the factor to the n, exactly. */
  function skVerdict(rho) {
    var c1 = Rcmp(rho, R1), cm = Rcmp(rho, R(-1n));
    if (c1 > 0) return 'grows';
    if (c1 === 0) return 'constant';
    if (Rsign(rho) >= 0) return 'decays';
    if (cm > 0) return 'oscillates and decays';
    if (cm === 0) return 'oscillates without decaying';
    return 'oscillates and grows';
  }
  function skCompute(aText, y0Text, hText, n, scheme) {
    var a = DB_need(aText, 'a'), y0 = DB_need(y0Text, 'y0'), h = DB_step(hText, n, R0);
    if (Rsign(a) <= 0) throw new Error('a must be positive: y′ = −a·y is the decay this lab studies');
    var fwd = Rsub(R1, Rmul(a, h)), bwd = Rinv(Radd(R1, Rmul(a, h)));
    var rho = scheme === 'backward' ? bwd : fwd, rows = [y0], k;
    for (k = 0; k < n; k += 1) rows.push(Rmul(rows[k], rho));
    var T = Rmul(h, R(BigInt(n)));
    return { a: a, y0: y0, h: h, n: n, scheme: scheme, fwd: fwd, bwd: bwd, rho: rho, rows: rows,
             verdict: skVerdict(rho), bound: Rdiv(R(2n), a), T: T,
             tru: DE_float(y0) * Math.exp(-DE_float(Rmul(a, T))) };
  }
"""


def _stiff(cfg):
    mode = "stiff"
    found = dc.presets(cfg, KIT, mode)
    scheme = dc.choice(cfg, "scheme", ["forward", "backward"], KIT, mode)
    table = {}
    for p in found:
        a, h = _r(p, mode, "a"), _r(p, mode, "h")
        dc.check(KIT, mode, p, _f(a) > 0, "a must be positive")
        dc.check(KIT, mode, p, _f(h) > 0, "h must be positive")
        table[str(p["id"])] = {"a": a, "y0": _r(p, mode, "y0"), "h": h, "n": _int(p, mode, "n", 1, 64)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Factor per step", "skFactor"), ("What the steps do", "skVerdict"),
             ("Forward Euler decays when", "skLimit"), ("Last value yₙ", "skLast"),
             ("True y(n·h), rounded", "skTrue"), ("Backward factor 1/(1 + a·h)", "skBackward")]
    markup = (
        dc.toolbar("A step that is too big", "y′ = −a·y stepped by Euler, exactly",
                   [("green", "Euler's steps (exact)"), ("cyan", "y0·e^(−at)")])
        + dc.stage(dc.svg("skPlot", "Euler's steps on the decay equation"))
        + dc.wrap("skTable")
        + dc.banner("skStatus")
    )
    controls = (
        dc.select("skPreset", "Decay rate and step", dc.options(found), pick["id"])
        + dc.text("skA", "Decay rate a", first["a"])
        + dc.text("skY0", "y0", first["y0"])
        + dc.text("skH", "Step h", first["h"])
        + dc.range_("skN", "Steps n", 1, 64, first["n"])
        + dc.select("skScheme", "Scheme", [("forward", "forward Euler"), ("backward", "backward Euler")], scheme)
        + dc.kpis(tiles)
        + dc.hint("Forward Euler multiplies by 1 − a·h each step; backward Euler divides by 1 + a·h.")
    )
    glue = dc.literal("SKP", table) + r"""
  var SK_TILES = ['skFactor', 'skVerdict', 'skLimit', 'skLast', 'skTrue', 'skBackward'];
  var skPresetIn = DE_el('skPreset'), skAIn = DE_el('skA'), skY0In = DE_el('skY0'), skHIn = DE_el('skH');
  var skNIn = DE_el('skN'), skSchemeIn = DE_el('skScheme');
  function skRender(r) {
    var rows = [], i, hf = DE_float(r.h), af = DE_float(r.a), yf = DE_float(r.y0);
    DE_set('skFactor', DE_q(r.rho));
    DE_set('skVerdict', r.verdict);
    DE_set('skLimit', 'h < ' + DE_q(r.bound));
    DE_set('skLast', DE_q(r.rows[r.n]));
    DE_set('skTrue', DE_dec(r.tru));
    DE_set('skBackward', DE_q(r.bwd));
    for (i = 0; i < r.rows.length; i += 1) {
      rows.push([String(i), DE_q(Rmul(r.h, R(BigInt(i)))), DE_q(r.rows[i]), DE_dec(yf * Math.exp(-af * hf * i))]);
    }
    DE_html('skTable', DB_table((r.scheme === 'backward' ? 'Backward' : 'Forward') + ' Euler: each step multiplies y by ' + DE_q(r.rho),
      ['n', 'tₙ', 'yₙ, exact', 'y0·e^(−a·tₙ), rounded'], rows));
    var pts = r.rows.map(function (y, k) { return [hf * k, DE_float(y)]; });
    var T = hf * r.n, tru = function (t) { return yf * Math.exp(-af * t); };
    var ys = pts.map(function (q) { return q[1]; }).concat([yf, 0]);
    var lo = Math.min.apply(null, ys), hi = Math.max.apply(null, ys), pad = 0.1 * Math.max(hi - lo, 1e-9);
    var plot = DB_plot('skPlot', { xmin: 0, xmax: T, ymin: lo - pad, ymax: hi + pad }, 'Euler on y′ = −' + DE_q(r.a) + 'y with h = ' + DE_q(r.h));
    plot.curve(tru);
    DE_polyline(plot, pts, 'plot-curve good');
    DE_ok('skStatus', '<strong>Exact.</strong> ' + (r.scheme === 'backward' ? 'Backward' : 'Forward') + ' Euler on y′ = −' + DE_esc(DE_q(r.a))
      + '·y with h = ' + DE_esc(DE_q(r.h)) + ' multiplies y by ' + DE_esc(DE_q(r.rho)) + ' each step, so yₙ = ' + DE_esc(DE_q(r.y0))
      + '·(' + DE_esc(DE_q(r.rho)) + ')ⁿ: it ' + DE_esc(r.verdict) + '. Forward Euler decays only for h < 2/a = ' + DE_esc(DE_q(r.bound))
      + '; the backward factor ' + DE_esc(DE_q(r.bwd)) + ' lies between 0 and 1 for every h. The true y(' + DE_esc(DE_q(r.T)) + ') is '
      + DE_esc(DE_dec(r.tru)) + ', rounded.');
  }
  function redraw() {
    var r;
    try {
      r = skCompute(skAIn.value, skY0In.value, skHIn.value, DB_range('skN'), skSchemeIn.value);
    } catch (e) {
      DE_refuse('skStatus', SK_TILES, ['skPlot', 'skTable'], DE_msg(e)); return;
    }
    skRender(r);
  }
  skPresetIn.addEventListener('change', function () {
    var p = SKP[skPresetIn.value];
    if (p) { skAIn.value = p.a; skY0In.value = p.y0; skHIn.value = p.h; skNIn.value = String(p.n); }
    redraw();
  });
  [skAIn, skY0In, skHIn, skNIn].forEach(function (el) { el.addEventListener('input', redraw); });
  skSchemeIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Stiffness", subtitle="Euler's factor 1 − a·h, exactly",
        markup=markup, controls=controls,
        script=dc.script("DRAW", extra=DB_JS + DB_TAB_JS + STIFF_JS + glue),
        panel_title="Choose the decay rate and the step",
        panel_intro="Each Euler step multiplies y by the same factor. Whether the steps decay, wobble or blow up "
                    "is read off that one number.",
        select="skPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# char (ce)
# ---------------------------------------------------------------------------

CHAR_JS = r"""
  /* ---- dekit/char: a·y″ + b·y′ + c·y = 0 ----------------------------------
     y = e^(rt) turns the equation into a·r² + b·r + c = 0, solved exactly by
     quadroots. The roots are numbered r₁ > r₂. The constants are fitted at
     t = 0 when the roots are rational, repeated, or α ± βi with β rational;
     the fitted solution is an exponential polynomial and its residual is
     computed, not assumed. */
  function ceSolve(aText, bText, cText, icText) {
    var a = DB_need(aText, 'a'), b = DB_need(bText, 'b'), c = DB_need(cText, 'c');
    if (Rzero(a)) throw new Error('a is 0, so the equation is not second order');
    var qr = quadroots(a, b, c), r = { a: a, b: b, c: c, qr: qr, disc: qr.disc };
    r.ic = DB_blank(icText) ? null : DB_list(icText, 'the initial values y0 v0', [2]);
    r.kind = { rational: 'two real roots', irrational: 'two real roots (irrational)', double: 'one repeated root', complex: 'complex pair' }[qr.kind];
    r.roots = DB_roottext(qr);
    var big = Radd(qr.p, Rabs(qr.s.q)), small = Rsub(qr.p, Rabs(qr.s.q)), C = null, ep = null, why = '';
    if (qr.kind === 'rational') {
      r.general = DB_join([DB_times('C₁', big), DB_times('C₂', small)]);
      r.W = DE_q(Rsub(small, big));
      r.basis = [EPmake([{ c: R1, k: 0, a: big, b: R0, trig: '1' }]), EPmake([{ c: R1, k: 0, a: small, b: R0, trig: '1' }])];
      if (r.ic) {
        var c2 = Rdiv(Rsub(r.ic[1], Rmul(big, r.ic[0])), Rsub(small, big));
        C = [Rsub(r.ic[0], c2), c2];
      }
    } else if (qr.kind === 'irrational') {
      r.general = 'C₁·e^(r₁t) + C₂·e^(r₂t) with r = ' + r.roots;
      r.W = DE_root(null, { q: Rneg(Rmul(R(2n), Rabs(qr.s.q))), k: qr.s.k });
      r.basis = null;
      if (r.ic) why = 'the roots are irrational; the constants would be surds and this lab fits only rational ones';
    } else if (qr.kind === 'double') {
      var lam = qr.p;
      r.general = Rzero(lam) ? 'C₁ + C₂·t' : '(C₁ + C₂·t)·' + DB_exp(lam);
      r.W = '1';
      r.basis = [EPmake([{ c: R1, k: 0, a: lam, b: R0, trig: '1' }]), EPmake([{ c: R1, k: 1, a: lam, b: R0, trig: '1' }])];
      if (r.ic) C = [r.ic[0], Rsub(r.ic[1], Rmul(lam, r.ic[0]))];
    } else {
      var al = qr.p, beta = qr.s.k === 1n ? Rabs(qr.s.q) : null;
      var bt = beta !== null ? DE_lin(beta, 't') : (function () { var w = DE_root(null, { q: Rabs(qr.s.q), k: qr.s.k }); return (w.indexOf('/') >= 0 ? '(' + w + ')' : w) + '·t'; })();
      var inner = 'C₁·cos(' + bt + ') + C₂·sin(' + bt + ')';
      r.general = Rzero(al) ? inner : DB_exp(al) + '·(' + inner + ')';
      r.W = DE_root(null, { q: Rabs(qr.s.q), k: qr.s.k });
      r.basis = beta === null ? null : [EPmake([{ c: R1, k: 0, a: al, b: beta, trig: 'cos' }]), EPmake([{ c: R1, k: 0, a: al, b: beta, trig: 'sin' }])];
      if (r.ic) {
        if (beta === null) why = 'the frequency ' + r.W + ' is irrational; the constant C₂ would be a surd and this lab fits only rational ones';
        else C = [r.ic[0], Rdiv(Rsub(r.ic[1], Rmul(al, r.ic[0])), beta)];
      }
    }
    r.C = C; r.why = why;
    if (C) {
      ep = EPadd(EPscale(r.basis[0], C[0]), EPscale(r.basis[1], C[1]));
      var d1 = EPderiv(ep), d2 = EPderiv(d1);
      r.residual = EPadd(EPadd(EPscale(d2, a), EPscale(d1, b)), EPscale(ep, c));
      r.icOK = Requ(EPevalExact(ep, R0), r.ic[0]) && Requ(EPevalExact(d1, R0), r.ic[1]);
    }
    r.ep = ep;
    return r;
  }
"""


def _char(cfg):
    mode = "char"
    found = dc.presets(cfg, KIT, mode)
    view = dc.choice(cfg, "view", ["roots", "solution", "wronskian"], KIT, mode)
    table = {}
    for p in found:
        a = _r(p, mode, "a")
        dc.check(KIT, mode, p, _f(a) != 0, "a must not be 0")
        table[str(p["id"])] = {"a": a, "b": _r(p, mode, "b"), "c": _r(p, mode, "c"),
                               "ic": _rlist(p, mode, "ic", (2,), allow_none=True)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Discriminant b² − 4ac", "ceDisc"), ("Kind of roots", "ceKind"), ("Roots", "ceRoots"),
             ("General solution", "ceGeneral"), ("Constants", "ceC"), ("Solution", "ceSolution"),
             ("Wronskian W(0)", "ceW")]
    markup = (
        dc.toolbar("The characteristic equation", "y = e^(rt) turns a·y″ + b·y′ + c·y = 0 into a·r² + b·r + c = 0",
                   [("cyan", "the curve shown"), ("purple", "second solution"), ("green", "roots")])
        + dc.stage(dc.svg("cePlot", "the characteristic equation and its solutions"))
        + dc.banner("ceStatus")
    )
    controls = (
        dc.select("cePreset", "Equation", dc.options(found), pick["id"])
        + dc.text("ceAIn", "a (coefficient of y″)", first["a"])
        + dc.text("ceBIn", "b (coefficient of y′)", first["b"])
        + dc.text("ceCIn", "c (coefficient of y)", first["c"])
        + dc.text("ceIC", "Initial values y(0) y′(0) (may be empty)", first["ic"])
        + dc.select("ceView", "View", [("roots", "the roots"), ("solution", "the solution"),
                                       ("wronskian", "the two solutions")], view)
        + dc.kpis(tiles)
        + dc.hint("Three rational coefficients; the initial values are two numbers, y(0) then y′(0).")
    )
    glue = dc.literal("CEP", table) + r"""
  var CE_TILES = ['ceDisc', 'ceKind', 'ceRoots', 'ceGeneral', 'ceC', 'ceSolution', 'ceW'];
  var cePresetIn = DE_el('cePreset'), ceAIn = DE_el('ceAIn'), ceBIn = DE_el('ceBIn'), ceCIn = DE_el('ceCIn');
  var ceICIn = DE_el('ceIC'), ceViewIn = DE_el('ceView');
  function ceFloatBasis(r) {
    var qr = r.qr, p = Rnum(qr.p), m = Rnum(Rabs(qr.s.q)) * Math.sqrt(Number(qr.s.k));
    if (qr.kind === 'double') return [function (t) { return Math.exp(p * t); }, function (t) { return t * Math.exp(p * t); }];
    if (qr.kind === 'complex') return [function (t) { return Math.exp(p * t) * Math.cos(m * t); }, function (t) { return Math.exp(p * t) * Math.sin(m * t); }];
    return [function (t) { return Math.exp((p + m) * t); }, function (t) { return Math.exp((p - m) * t); }];
  }
  function ceRender(r, view) {
    DE_set('ceDisc', DE_q(r.disc));
    DE_set('ceKind', r.kind);
    DE_set('ceRoots', r.roots);
    DE_set('ceGeneral', r.general);
    DE_set('ceC', r.C ? 'C₁ = ' + DE_q(r.C[0]) + ', C₂ = ' + DE_q(r.C[1]) : '—');
    DE_set('ceSolution', r.ep ? EPtext(r.ep) : '—');
    DE_set('ceW', r.W);
    var plot, fb = ceFloatBasis(r);
    if (view === 'roots') {
      var a = Rnum(r.a), b = Rnum(r.b), c = Rnum(r.c), cen = Rnum(r.qr.p);
      var half = Math.max(2, Rnum(Rabs(r.qr.s.q)) * Math.sqrt(Number(r.qr.s.k)) * 1.6);
      var pr = function (x) { return a * x * x + b * x + c; };
      plot = DB_plot('cePlot', DB_window([pr], cen - half, cen + half), 'the characteristic polynomial');
      plot.curve(pr);
      if (r.qr.kind !== 'complex') {
        var m = Rnum(Rabs(r.qr.s.q)) * Math.sqrt(Number(r.qr.s.k));
        plot.point(cen - m, 0, 'plot-point root').point(cen + m, 0, 'plot-point root');
      }
    } else if (view === 'solution' && r.ep) {
      var yf = function (t) { return EPevalFloat(r.ep, t); };
      plot = DB_plot('cePlot', DB_window([yf], 0, 6), 'the fitted solution');
      plot.curve(yf);
    } else {
      plot = DB_plot('cePlot', DB_window(fb, 0, 4), 'the two basic solutions');
      plot.curve(fb[0]).curve(fb[1], 'plot-curve alt');
    }
    var check = '';
    if (r.ep) {
      check = EPzero(r.residual) && r.icOK ? ' Substituted back, the residual a·y″ + b·y′ + c·y is 0 and both initial values hold.'
        : ' Substituted back, the residual is ' + EPtext(r.residual) + '.';
    }
    var more = r.why ? ' ' + r.why.charAt(0).toUpperCase() + r.why.slice(1) + '.' : (r.ic ? check : ' Give y(0) and y′(0) to fit the constants.');
    DE_ok('ceStatus', '<strong>Exact.</strong> ' + DE_esc(DE_ptext([r.c, r.b, r.a], 'r')) + ' = 0 has discriminant '
      + DE_esc(DE_q(r.disc)) + ': ' + DE_esc(r.kind) + ', ' + DE_esc(r.roots) + '.' + DE_esc(more));
  }
  function redraw() {
    var r;
    try {
      r = ceSolve(ceAIn.value, ceBIn.value, ceCIn.value, ceICIn.value);
    } catch (e) {
      DE_refuse('ceStatus', CE_TILES, ['cePlot'], DE_msg(e)); return;
    }
    ceRender(r, ceViewIn.value);
  }
  cePresetIn.addEventListener('change', function () {
    var p = CEP[cePresetIn.value];
    if (p) { ceAIn.value = p.a; ceBIn.value = p.b; ceCIn.value = p.c; ceICIn.value = p.ic; }
    redraw();
  });
  [ceAIn, ceBIn, ceCIn, ceICIn].forEach(function (el) { el.addEventListener('input', redraw); });
  ceViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The characteristic equation", subtitle="Roots, the general solution and the constants, exactly",
        markup=markup, controls=controls,
        script=dc.script("SURD", "EP", extra=DB_JS + DB_ROOT_JS + CHAR_JS + glue),
        panel_title="Choose the coefficients",
        panel_intro="Substituting y = e^(rt) leaves a·r² + b·r + c = 0. Its roots decide the form of every "
                    "solution; two initial values fix the two constants.",
        select="cePreset", presets=found,
    )


# ---------------------------------------------------------------------------
# oscillator (os)
# ---------------------------------------------------------------------------

OSCILLATOR_JS = r"""
  /* RK4 in doubles on (x, v)′ = f(t, x, v), for drawing only: [[t, x, v]] */
  function DB_rk4sys(f, t, x, v, h, n) {
    var out = [[t, x, v]], k;
    for (k = 0; k < n; k += 1) {
      var a1 = f(t, x, v), a2 = f(t + h / 2, x + h / 2 * a1[0], v + h / 2 * a1[1]);
      var a3 = f(t + h / 2, x + h / 2 * a2[0], v + h / 2 * a2[1]), a4 = f(t + h, x + h * a3[0], v + h * a3[1]);
      x += h / 6 * (a1[0] + 2 * a2[0] + 2 * a3[0] + a4[0]);
      v += h / 6 * (a1[1] + 2 * a2[1] + 2 * a3[1] + a4[1]);
      t += h;
      if (!isFinite(x) || !isFinite(v) || Math.abs(x) > 1e6 || Math.abs(v) > 1e6) break;
      out.push([t, x, v]);
    }
    return out;
  }
  /* ---- dekit/oscillator: m·x″ + c·x′ + k·x = F0·cos(ωt) ------------------
     Every quantity with a rational value is printed as a fraction; a square
     root is a surd with its rounded value beside it; π, e^(−π) and the phase
     angle are rounded and say so. */
  function osPi(r) { return DE_lin(r, 'π'); }
  /* 2π/ω₀ with ω₀ = q·√k */
  function osPeriodText(s) {
    var r = Rdiv(R(2n), s.q), val = 2 * Math.PI / (Rnum(s.q) * Math.sqrt(Number(s.k)));
    if (s.k === 1n) return osPi(r) + ' ' + DE_dec(val);
    var num = (r.n === 1n ? '' : String(r.n)) + 'π';
    return num + '/' + (r.d === 1n ? '√' + s.k : '(' + r.d + '√' + s.k + ')') + ' ' + DE_dec(val);
  }
  function osCompute(mText, cText, kText, icText, F0Text, wText) {
    var m = DB_need(mText, 'm'), c = DB_need(cText, 'c'), k = DB_need(kText, 'k');
    if (Rsign(m) <= 0) throw new Error('m must be positive');
    if (Rsign(k) <= 0) throw new Error('k must be positive');
    if (Rsign(c) < 0) throw new Error('c must not be negative');
    var ic = DB_list(icText, 'the initial values x0 v0', [2]), x0 = ic[0], v0 = ic[1];
    var F0 = DB_blank(F0Text) ? R0 : DB_need(F0Text, 'F0');
    var w = DB_blank(wText) ? null : DB_need(wText, 'ω');
    if (!Rzero(F0) && (w === null || Rsign(w) <= 0)) throw new Error('ω must be positive when F0 is not 0');
    if (w === null) w = R0;
    var r = { m: m, c: c, k: k, x0: x0, v0: v0, F0: F0, w: w, two: R(2n) };
    var w0sq = Rdiv(k, m), w0 = Rsurd(w0sq), half = Rdiv(c, Rmul(R(2n), m));
    r.w0sq = w0sq; r.w0 = w0;
    r.disc = Rsub(Rmul(c, c), Rmul(R(4n), Rmul(m, k)));
    r.type = Rzero(c) ? 'undamped' : (Rsign(r.disc) < 0 ? 'underdamped' : (Rzero(r.disc) ? 'critically damped' : 'overdamped'));
    r.omega0 = DB_sqrt(w0sq);
    var forced = !Rzero(F0), w2 = Rmul(w, w);
    r.beat = forced && Rzero(c) && w0.k === 1n && !Requ(w, w0.q);
    if (r.beat) {
      var d = Rabs(Rsub(w0.q, w));
      r.period = osPi(Rdiv(R(2n), d)) + ' ' + DE_dec(2 * Math.PI / Rnum(d));
    } else r.period = osPeriodText(w0);
    var free = Rzero(c) && !forced;
    r.ampSq = free ? DE_q(Radd(Rmul(x0, x0), Rdiv(Rmul(v0, v0), w0sq))) : '—';
    r.amp = free ? DB_sqrt(Radd(Rmul(x0, x0), Rdiv(Rmul(v0, v0), w0sq))) : '—';
    if (!free || (Rzero(x0) && Rzero(v0))) r.phase = '—';
    else if (Rzero(v0)) r.phase = Rsign(x0) > 0 ? '0' : 'π ' + DE_dec(Math.PI);
    else if (Rzero(x0)) r.phase = Rsign(v0) > 0 ? 'π/2 ' + DE_dec(Math.PI / 2) : '−π/2 ' + DE_dec(-Math.PI / 2);
    else r.phase = DE_dec(Math.atan2(DE_float(v0) / Math.sqrt(DE_float(w0sq)), DE_float(x0)));
    r.ccrit = DB_sqrt(Rmul(R(4n), Rmul(m, k)));
    r.omegaD = '—'; r.envelope = '—'; r.cross = '—';
    if (r.type === 'underdamped') {
      var wd2 = Rsub(w0sq, Rmul(half, half));
      r.wd2 = wd2;
      r.omegaD = 'ω_d² = ' + DE_q(wd2);
      r.envelope = 'c/(2m) = ' + DE_q(half) + '; peaks shrink by ' + DE_dec(Math.exp(-Rnum(half) * 2 * Math.PI / Math.sqrt(DE_float(wd2))));
    }
    if (r.type === 'critically damped' && !forced) {
      var root = Rneg(half), C2 = Rsub(v0, Rmul(root, x0));
      r.C1 = x0; r.C2 = C2;
      var at = Rzero(C2) ? null : Rdiv(Rneg(x0), C2);
      r.cross = at !== null && Rsign(at) > 0 ? 't = ' + DE_q(at) : 'none for t > 0';
    }
    r.forced = '—'; r.resonant = '—';
    if (forced && Rzero(c)) {
      if (Requ(w2, w0sq)) {
        r.forced = 'resonance: ' + DE_sum([{ c: Rdiv(F0, Rmul(R(2n), Rmul(m, w))), body: 't·sin(' + DE_lin(w, 't') + ')', dot: true }]);
      } else r.forced = 'A = ' + DE_q(Rdiv(F0, Rmul(m, Rsub(w0sq, w2))));
    } else if (forced) {
      var e1 = Rsub(k, Rmul(m, w2)), e2 = Rmul(c, w);
      r.forced = 'A² = ' + DE_q(Rdiv(Rmul(F0, F0), Radd(Rmul(e1, e1), Rmul(e2, e2))));
      var wr2 = Rsub(w0sq, Rdiv(Rmul(c, c), Rmul(R(2n), Rmul(m, m))));
      if (Rsign(wr2) <= 0) r.resonant = 'none';
      else {
        var dd = Rmul(Rmul(c, c), Rsub(w0sq, Rmul(half, half)));
        r.resonant = 'ω_r² = ' + DE_q(wr2) + '; A_max = ' + DB_sqrt(Rdiv(Rmul(F0, F0), dd));
        r.wr = Math.sqrt(DE_float(wr2));
      }
    }
    r.energy = DE_q(Radd(Rdiv(Rmul(m, Rmul(v0, v0)), R(2n)), Rdiv(Rmul(k, Rmul(x0, x0)), R(2n))));
    return r;
  }
"""


def _oscillator(cfg):
    mode = "oscillator"
    found = dc.presets(cfg, KIT, mode)
    view = dc.choice(cfg, "view", ["motion", "phase", "amplitude"], KIT, mode)
    table = {}
    for p in found:
        m, c, k = _r(p, mode, "m"), _r(p, mode, "c"), _r(p, mode, "k")
        dc.check(KIT, mode, p, _f(m) > 0 and _f(k) > 0 and _f(c) >= 0, "m and k must be positive and c not negative")
        F0 = _r(p, mode, "F0", allow_none=True) or "0"
        w = _r(p, mode, "w", allow_none=True) or ""
        dc.check(KIT, mode, p, _f(F0) == 0 or (w and _f(w) > 0), "w must be positive when F0 is not 0")
        table[str(p["id"])] = {"m": m, "c": c, "k": k, "ic": _rlist(p, mode, "ic", (2,)), "F0": F0, "w": w}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Motion", "osType"), ("c² − 4mk", "osDisc"), ("ω₀² = k/m", "osOmega0Sq"), ("ω₀", "osOmega0"),
             ("Undamped period 2π/ω₀, or beat period when forced", "osPeriod"), ("Amplitude squared A²", "osAmpSq"),
             ("Amplitude A", "osAmp"), ("Phase φ", "osPhase"), ("Critical damping c_crit = 2√(mk)", "osCcrit"),
             ("Pseudo-frequency squared", "osOmegaD"), ("Envelope", "osEnvelope"),
             ("Forced response", "osForced"), ("Resonant frequency", "osResonant"),
             ("Energy E₀", "osEnergy"), ("Zero crossing (critical damping)", "osCross")]
    markup = (
        dc.toolbar("The mass on a spring", "m·x″ + c·x′ + k·x = F₀·cos(ωt)",
                   [("cyan", "drawn by stepping in floating point"), ("muted", "envelope or marks")])
        + dc.stage(dc.svg("osPlot", "the motion of the oscillator"))
        + dc.banner("osStatus")
    )
    controls = (
        dc.select("osPreset", "Oscillator", dc.options(found), pick["id"])
        + dc.text("osM", "Mass m", first["m"])
        + dc.text("osC", "Damping c", first["c"])
        + dc.text("osK", "Spring constant k", first["k"])
        + dc.text("osIC", "Start x(0) x′(0)", first["ic"])
        + dc.text("osF0", "Forcing F₀ (0 for none)", first["F0"])
        + dc.text("osW", "Forcing frequency ω", first["w"])
        + dc.select("osView", "View", [("motion", "x against t"), ("phase", "x against x′"),
                                       ("amplitude", "amplitude against ω")], view)
        + dc.kpis(tiles)
        + dc.hint("Rational m, c, k; the start is two numbers, x(0) then x′(0).")
    )
    glue = dc.literal("OSP", table) + r"""
  var OS_TILES = ['osType', 'osDisc', 'osOmega0Sq', 'osOmega0', 'osPeriod', 'osAmpSq', 'osAmp', 'osPhase', 'osCcrit',
                  'osOmegaD', 'osEnvelope', 'osForced', 'osResonant', 'osEnergy', 'osCross'];
  var osPresetIn = DE_el('osPreset'), osMIn = DE_el('osM'), osCIn = DE_el('osC'), osKIn = DE_el('osK');
  var osICIn = DE_el('osIC'), osF0In = DE_el('osF0'), osWIn = DE_el('osW'), osViewIn = DE_el('osView');
  function osRender(r, view) {
    DE_set('osType', r.type);
    DE_set('osDisc', DE_q(r.disc));
    DE_set('osOmega0Sq', DE_q(r.w0sq));
    DE_set('osOmega0', r.omega0);
    DE_set('osPeriod', r.period);
    DE_set('osAmpSq', r.ampSq);
    DE_set('osAmp', r.amp);
    DE_set('osPhase', r.phase);
    DE_set('osCcrit', r.ccrit);
    DE_set('osOmegaD', r.omegaD);
    DE_set('osEnvelope', r.envelope);
    DE_set('osForced', r.forced);
    DE_set('osResonant', r.resonant);
    DE_set('osEnergy', r.energy);
    DE_set('osCross', r.cross);
    var m = DE_float(r.m), c = DE_float(r.c), k = DE_float(r.k), F0 = DE_float(r.F0), w = DE_float(r.w);
    var w0 = Math.sqrt(k / m), P = 2 * Math.PI / w0;
    var T = Math.min(40, Math.max(6, 3 * P));
    if (r.beat) T = Math.min(60, Math.max(T, 1.5 * 2 * Math.PI / Math.abs(w0 - w)));
    var f = function (t, x, v) { return [v, (F0 * Math.cos(w * t) - c * v - k * x) / m]; };
    var path = DB_rk4sys(f, 0, DE_float(r.x0), DE_float(r.v0), T / 800, 800), plot;
    if (view === 'amplitude' && F0 !== 0) {
      var amp = function (om) { var e1 = k - m * om * om, e2 = c * om; return Math.abs(F0) / Math.sqrt(e1 * e1 + e2 * e2); };
      var top = 3 * Math.max(w0, w);
      plot = DB_plot('osPlot', DB_window([amp], 0, top), 'the steady amplitude against the forcing frequency');
      plot.curve(amp);
      plot.vline(w, 'plot-aux', 'ω');
      if (r.wr) plot.vline(r.wr, 'plot-asym', 'ω_r');
    } else if (view === 'phase') {
      var xs = path.map(function (q) { return q[1]; }), vs = path.map(function (q) { return q[2]; });
      var xm = Math.max(1e-9, Math.max.apply(null, xs.map(Math.abs))) * 1.15, vm = Math.max(1e-9, Math.max.apply(null, vs.map(Math.abs))) * 1.15;
      plot = DB_plot('osPlot', { xmin: -xm, xmax: xm, ymin: -vm, ymax: vm }, 'the path in the x, x′ plane');
      DE_polyline(plot, path.map(function (q) { return [q[1], q[2]]; }), 'plot-curve');
    } else {
      var lo = 0, hi = 0;
      path.forEach(function (q) { if (q[1] < lo) lo = q[1]; if (q[1] > hi) hi = q[1]; });
      var pad = 0.1 * Math.max(hi - lo, 1e-9);
      plot = DB_plot('osPlot', { xmin: 0, xmax: T, ymin: lo - pad, ymax: hi + pad }, 'x against t');
      DE_polyline(plot, path.map(function (q) { return [q[0], q[1]]; }), 'plot-curve');
      if (r.type === 'underdamped' && F0 === 0) {
        var rate = c / (2 * m), wd = Math.sqrt(DE_float(r.wd2)), x0 = DE_float(r.x0), v0 = DE_float(r.v0);
        var A = Math.sqrt(x0 * x0 + Math.pow((v0 + rate * x0) / wd, 2));
        plot.curve(function (t) { return A * Math.exp(-rate * t); }, 'plot-curve parent');
        plot.curve(function (t) { return -A * Math.exp(-rate * t); }, 'plot-curve parent');
      }
    }
    DE_ok('osStatus', '<strong>Exact where it says so.</strong> ω₀² = k/m = ' + DE_esc(DE_q(r.w0sq)) + ' and c² − 4mk = '
      + DE_esc(DE_q(r.disc)) + ': ' + DE_esc(r.type) + '. The energy at the start is ' + DE_esc(r.energy)
      + (r.C2 !== undefined ? '; critically damped, x = (C₁ + C₂·t)·e^(rt) with C₁ = ' + DE_esc(DE_q(r.C1)) + ', C₂ = ' + DE_esc(DE_q(r.C2)) + ', zero crossing ' + DE_esc(r.cross) : '')
      + '. Figures behind ≈ are rounded; the curve is drawn by stepping in floating point.');
  }
  function redraw() {
    var r;
    try {
      r = osCompute(osMIn.value, osCIn.value, osKIn.value, osICIn.value, osF0In.value, osWIn.value);
    } catch (e) {
      DE_refuse('osStatus', OS_TILES, ['osPlot'], DE_msg(e)); return;
    }
    osRender(r, osViewIn.value);
  }
  osPresetIn.addEventListener('change', function () {
    var p = OSP[osPresetIn.value];
    if (p) { osMIn.value = p.m; osCIn.value = p.c; osKIn.value = p.k; osICIn.value = p.ic; osF0In.value = p.F0; osWIn.value = p.w; }
    redraw();
  });
  [osMIn, osCIn, osKIn, osICIn, osF0In, osWIn].forEach(function (el) { el.addEventListener('input', redraw); });
  osViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The oscillator", subtitle="Free, damped and forced motion, with every exact quantity",
        markup=markup, controls=controls,
        script=dc.script("SURD", "DRAW", extra=DB_JS + DB_ROOT_JS + OSCILLATOR_JS + glue),
        panel_title="Choose the oscillator",
        panel_intro="Mass, damping and spring decide ω₀² = k/m and the sign of c² − 4mk; a forcing term adds a "
                    "response of its own. Fractions are exact; anything with π or e is rounded and marked ≈.",
        select="osPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# phase (pp) -- and the matrix analysis jacobian reuses (DB_MAT_JS).
# ---------------------------------------------------------------------------

DB_MAT_JS = r"""
  /* ---- dekit: a 2×2 matrix as a linear system ------------------------------
     Trace, determinant, discriminant, eigenvalues by quadroots, integer
     eigenvectors for rational eigenvalues, the type, and the real general
     solution with its constants fitted to a start when the arithmetic stays
     rational. A = [[a, b], [c, d]] as rationals. */
  function DB_eigvec(A, lam) {
    var a = Rsub(A[0][0], lam), b = A[0][1], c = A[1][0], d = Rsub(A[1][1], lam);
    if (!Rzero(b) || !Rzero(a)) return DB_intvec(b, Rneg(a));
    if (!Rzero(c) || !Rzero(d)) return DB_intvec(d, Rneg(c));
    return null;
  }
  function DB_mat(A) {
    var a = A[0][0], b = A[0][1], c = A[1][0], d = A[1][1];
    var tau = Radd(a, d), det = Rsub(Rmul(a, d), Rmul(b, c)), disc = Rsub(Rmul(tau, tau), Rmul(R(4n), det));
    var qr = quadroots(R1, Rneg(tau), det), M = { A: A, tau: tau, det: det, disc: disc, qr: qr };
    M.scalar = Rzero(b) && Rzero(c) && Requ(a, d);
    M.type = DB_type(tau, det, disc, M.scalar);
    M.eig = DB_roottext(qr);
    M.vectors = '—'; M.general = '—'; M.basis = null;
    if (qr.kind === 'rational') {
      var l1 = qr.roots[0], l2 = qr.roots[1], v1 = DB_eigvec(A, l1), v2 = DB_eigvec(A, l2);
      M.vectors = DB_vec(v1[0], v1[1]) + ', ' + DB_vec(v2[0], v2[1]);
      M.general = DB_times('C₁', l1) + '·' + DB_vec(v1[0], v1[1]) + ' + ' + DB_times('C₂', l2) + '·' + DB_vec(v2[0], v2[1]);
      M.basis = { kind: 'real', l: [l1, l2], v: [v1, v2] };
    } else if (qr.kind === 'double') {
      var lam = qr.p, e = DB_exp(lam), pre = e ? e + '·' : '';
      if (M.scalar) {
        M.vectors = 'every direction';
        M.general = pre + '(C₁·(1, 0) + C₂·(0, 1))';
        M.basis = { kind: 'star', l: lam };
      } else {
        var v = DB_eigvec(A, lam), w;
        /* (A − λI)w = v: a generalised vector, solved exactly */
        var am = Rsub(a, lam), dm = Rsub(d, lam);
        if (!Rzero(b)) w = [R0, Rdiv(v[0], b)];
        else if (!Rzero(am)) w = [Rdiv(v[0], am), R0];
        else if (!Rzero(c)) w = [Rdiv(v[1], c), R0];
        else w = [R0, Rdiv(v[1], dm)];
        M.vectors = DB_vec(v[0], v[1]);
        M.general = pre + '(C₁·' + DB_vec(v[0], v[1]) + ' + C₂·(t·' + DB_vec(v[0], v[1]) + ' + ' + DB_vec(w[0], w[1]) + '))';
        M.basis = { kind: 'double', l: lam, v: v, w: w };
      }
    } else if (qr.kind === 'complex' && qr.s.k === 1n) {
      var al = qr.p, be = Rabs(qr.s.q);
      /* v = (b, α − a + βi) = u + i·w for λ = α + βi; b ≠ 0 since bc < 0 */
      var u = [b, Rsub(al, a)], ww = [R0, be], sc = DB_intvec(b, R0);
      var k = Rdiv(sc[0], b);
      u = [Rmul(u[0], k), Rmul(u[1], k)]; ww = [Rmul(ww[0], k), Rmul(ww[1], k)];
      var bt = DE_lin(be, 't'), ex = DB_exp(al);
      var body = 'C₁·(u·cos(' + bt + ') − w·sin(' + bt + ')) + C₂·(u·sin(' + bt + ') + w·cos(' + bt + '))';
      M.general = (ex ? ex + '·(' + body + ')' : body) + ', u = ' + DB_vec(u[0], u[1]) + ', w = ' + DB_vec(ww[0], ww[1]);
      M.basis = { kind: 'complex', al: al, be: be, u: u, w: ww };
    }
    return M;
  }
  /* C₁, C₂ from a start (x0, y0), or null */
  function DB_fit(M, x0, y0) {
    var B = M.basis, cols;
    if (!B) return null;
    if (B.kind === 'real') cols = [B.v[0], B.v[1]];
    else if (B.kind === 'star') cols = [[R1, R0], [R0, R1]];
    else if (B.kind === 'double') cols = [B.v, B.w];
    else cols = [B.u, B.w];
    /* C₁·col₀ + C₂·col₁ = (x0, y0) by Cramer's rule */
    var det = Rsub(Rmul(cols[0][0], cols[1][1]), Rmul(cols[1][0], cols[0][1]));
    if (Rzero(det)) return null;
    return [Rdiv(Rsub(Rmul(x0, cols[1][1]), Rmul(cols[1][0], y0)), det),
            Rdiv(Rsub(Rmul(cols[0][0], y0), Rmul(x0, cols[0][1])), det)];
  }
  function DB_matparse(text) {
    var s = String(text === undefined || text === null ? '' : text).replace(/−/g, '-');
    var rows = s.split(';');
    if (rows.length !== 2) throw new Error('type the matrix as two rows separated by a semicolon: a b; c d');
    return [DB_list(rows[0], 'the first row', [2]), DB_list(rows[1], 'the second row', [2])];
  }
  function DB_mattext(A) { return DE_q(A[0][0]) + ' ' + DE_q(A[0][1]) + '; ' + DE_q(A[1][0]) + ' ' + DE_q(A[1][1]); }
"""

PHASE_JS = r"""
  /* ---- dekit/phase: x′ = A·x -----------------------------------------------
     Euler's step is (xₙ₊₁, yₙ₊₁) = (I + h·A)(xₙ, yₙ), exactly; the ratio of
     squared radii over the last step is printed as a fraction (for a rotation
     it is 1 + h² every step). */
  function ppCompute(aText, startText, hText, n) {
    var A = DB_matparse(aText), M = DB_mat(A);
    var st = DB_list(startText, 'the start x0 y0', [2]), h = DB_step(hText, n, R0);
    M.start = st; M.h = h; M.n = n;
    var C = DB_fit(M, st[0], st[1]);
    M.C = C;
    var rows = [[st[0], st[1]]], k, stopped = false;
    for (k = 0; k < n; k += 1) {
      var p = rows[k];
      var nx = Radd(p[0], Rmul(h, Radd(Rmul(A[0][0], p[0]), Rmul(A[0][1], p[1]))));
      var ny = Radd(p[1], Rmul(h, Radd(Rmul(A[1][0], p[0]), Rmul(A[1][1], p[1]))));
      if (Math.max(DB_bdig(nx.n), DB_bdig(nx.d), DB_bdig(ny.n), DB_bdig(ny.d)) > 2000) { stopped = true; break; }
      rows.push([nx, ny]);
    }
    M.rows = rows; M.stopped = stopped;
    var last = rows[rows.length - 1], prev = rows.length > 1 ? rows[rows.length - 2] : null;
    var r2 = function (q) { return Radd(Rmul(q[0], q[0]), Rmul(q[1], q[1])); };
    M.last = DB_vec(last[0], last[1]);
    M.ratio = prev && !Rzero(r2(prev)) ? DE_q(Rdiv(r2(last), r2(prev))) : '—';
    return M;
  }
"""


def _matrix(p, mode, field):
    value = p.get(field)
    ok = (isinstance(value, (list, tuple)) and len(value) == 2
          and all(isinstance(row, (list, tuple)) and len(row) == 2 for row in value))
    dc.check(KIT, mode, p, ok, "%s must be [[a, b], [c, d]]" % field)
    return "; ".join(" ".join(dc.rational(v, KIT, mode, p, field) for v in row) for row in value)


def _phase(cfg):
    mode = "phase"
    found = dc.presets(cfg, KIT, mode)
    view = dc.choice(cfg, "view", ["field", "exact", "solution"], KIT, mode)
    table = {}
    for p in found:
        h = _r(p, mode, "h", allow_none=True) or "1/4"
        dc.check(KIT, mode, p, _f(h) > 0, "h must be positive")
        table[str(p["id"])] = {"A": _matrix(p, mode, "A"),
                               "start": _rlist(p, mode, "start", (2,), allow_none=True) or "1 0",
                               "h": h, "n": _int(p, mode, "n", 1, 64, default=8)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Trace τ", "ppTrace"), ("Determinant Δ", "ppDet"), ("τ² − 4Δ", "ppDisc"), ("Eigenvalues", "ppEig"),
             ("The origin is a", "ppType"), ("Eigenvectors", "ppVectors"), ("General solution", "ppGeneral"),
             ("Constants from the start", "ppC"), ("Euler: last radius² over the one before", "ppRatio"),
             ("Euler: last point", "ppLast")]
    markup = (
        dc.toolbar("A linear system in the plane", "x′ = A·x: the matrix decides the picture",
                   [("muted", "the field"), ("green", "Euler's steps (exact)"), ("cyan", "drawn by stepping in floating point")])
        + dc.stage(dc.svg("ppPlot", "the phase plane of the linear system"))
        + dc.banner("ppStatus")
    )
    controls = (
        dc.select("ppPreset", "Matrix", dc.options(found), pick["id"])
        + dc.text("ppA", "Matrix A (a b; c d)", first["A"])
        + dc.text("ppStart", "Start x0 y0", first["start"])
        + dc.text("ppH", "Euler step h", first["h"])
        + dc.range_("ppN", "Euler steps n", 1, 64, first["n"])
        + dc.select("ppView", "View", [("field", "the field"), ("exact", "Euler's steps"),
                                       ("solution", "solution curves")], view)
        + dc.kpis(tiles)
        + dc.hint("Type the matrix by rows: 0 1; -2 -3 means x′ = y, y′ = −2x − 3y.")
    )
    glue = dc.literal("PPP", table) + r"""
  var PP_TILES = ['ppTrace', 'ppDet', 'ppDisc', 'ppEig', 'ppType', 'ppVectors', 'ppGeneral', 'ppC', 'ppRatio', 'ppLast'];
  var ppPresetIn = DE_el('ppPreset'), ppAIn = DE_el('ppA'), ppStartIn = DE_el('ppStart'), ppHIn = DE_el('ppH');
  var ppNIn = DE_el('ppN'), ppViewIn = DE_el('ppView');
  function ppRender(M, view) {
    DE_set('ppTrace', DE_q(M.tau));
    DE_set('ppDet', DE_q(M.det));
    DE_set('ppDisc', DE_q(M.disc));
    DE_set('ppEig', M.eig);
    DE_set('ppType', M.type);
    DE_set('ppVectors', M.vectors);
    DE_set('ppGeneral', M.general);
    DE_set('ppC', M.C ? 'C₁ = ' + DE_q(M.C[0]) + ', C₂ = ' + DE_q(M.C[1]) : '—');
    DE_set('ppRatio', M.ratio);
    DE_set('ppLast', M.last);
    var A = M.A.map(function (row) { return row.map(DE_float); });
    var fv = function (t, x, y) { return [A[0][0] * x + A[0][1] * y, A[1][0] * x + A[1][1] * y]; };
    var pts = M.rows.map(function (q) { return [DE_float(q[0]), DE_float(q[1])]; });
    var R0f = Math.max(1, Math.abs(pts[0][0]), Math.abs(pts[0][1])) * 1.6;
    if (view === 'exact') pts.forEach(function (q) { R0f = Math.max(R0f, Math.abs(q[0]) * 1.1, Math.abs(q[1]) * 1.1); });
    R0f = Math.min(R0f, 1e5);
    var plot = DB_plot('ppPlot', { xmin: -R0f, xmax: R0f, ymin: -R0f, ymax: R0f }, 'the phase plane of x′ = A·x with A = ' + DB_mattext(M.A));
    if (view === 'field') {
      DE_arrows(plot, function (x, y) { return fv(0, x, y); }, 15);
      if (M.basis && M.basis.kind === 'real') {
        M.basis.v.forEach(function (v) {
          var vx = DE_float(v[0]), vy = DE_float(v[1]), L = 3 * R0f / Math.sqrt(vx * vx + vy * vy);
          plot.segment(-vx * L, -vy * L, vx * L, vy * L, 'plot-curve alt');
        });
      }
    } else if (view === 'exact') {
      DE_polyline(plot, DE_rk4float(fv, [0, pts[0][0], pts[0][1]], DE_float(M.h) * M.n / 400, 400), 'plot-curve alt');
      DE_polyline(plot, pts, 'plot-curve good');
    } else {
      var k;
      for (k = 0; k < 8; k += 1) {
        var ang = Math.PI * k / 4, s0 = [0, 0.7 * R0f * Math.cos(ang), 0.7 * R0f * Math.sin(ang)];
        DE_polyline(plot, DE_rk4float(fv, s0, 0.02, 300), 'plot-curve alt');
        DE_polyline(plot, DE_rk4float(function (t, x, y) { var v = fv(t, x, y); return [-v[0], -v[1]]; }, s0, 0.02, 300), 'plot-curve alt');
      }
      DE_polyline(plot, DE_rk4float(fv, [0, pts[0][0], pts[0][1]], 0.02, 400), 'plot-curve');
    }
    plot.point(pts[0][0], pts[0][1], 'plot-point', 'start');
    DE_ok('ppStatus', '<strong>Exact.</strong> τ = ' + DE_esc(DE_q(M.tau)) + ', Δ = ' + DE_esc(DE_q(M.det)) + ', τ² − 4Δ = '
      + DE_esc(DE_q(M.disc)) + ': ' + DE_esc(DE_ptext([M.det, Rneg(M.tau), R1], 'λ')) + ' = 0 gives ' + DE_esc(M.eig)
      + ', a ' + DE_esc(M.type) + '. ' + M.n + ' Euler steps with h = ' + DE_esc(DE_q(M.h)) + ' from ' + DE_esc(DB_vec(M.start[0], M.start[1]))
      + ' end at ' + DE_esc(M.last) + (M.stopped ? ' (stopped by the digit budget)' : '') + '. The curves are drawn by stepping in floating point.');
  }
  function redraw() {
    var M;
    try {
      M = ppCompute(ppAIn.value, ppStartIn.value, ppHIn.value, DB_range('ppN'));
    } catch (e) {
      DE_refuse('ppStatus', PP_TILES, ['ppPlot'], DE_msg(e)); return;
    }
    ppRender(M, ppViewIn.value);
  }
  ppPresetIn.addEventListener('change', function () {
    var p = PPP[ppPresetIn.value];
    if (p) { ppAIn.value = p.A; ppStartIn.value = p.start; ppHIn.value = p.h; ppNIn.value = String(p.n); }
    redraw();
  });
  [ppAIn, ppStartIn, ppHIn, ppNIn].forEach(function (el) { el.addEventListener('input', redraw); });
  ppViewIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The phase plane", subtitle="Trace, determinant, eigenvalues and exact Euler steps",
        markup=markup, controls=controls,
        script=dc.script("SURD", "DRAW", extra=DB_JS + DB_ROOT_JS + DB_MAT_JS + PHASE_JS + glue),
        panel_title="Choose the matrix",
        panel_intro="The trace and the determinant decide the picture. Euler's steps are exact fractions; the "
                    "curves behind them are drawn by stepping in floating point.",
        select="ppPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# jacobian (jb)
# ---------------------------------------------------------------------------

JACOBIAN_JS = r"""
  /* ---- dekit/jacobian: x′ = f(x, y), y′ = g(x, y) ---------------------------
     f and g are polynomials; each listed point is tested exactly, the
     Jacobian of partial derivatives is evaluated exactly at the selected one
     and classified as a linear system. A centre of the linearisation says
     nothing certain about the nonlinear system, and the tile says so. */
  function jbPointList(text, vars) {
    var s = String(text === undefined || text === null ? '' : text);
    if (!/\S/.test(s)) throw new Error('list at least one point, as 0 0; 1 1');
    var parts = s.split(';'), out = [], i;
    if (parts.length > 6) throw new Error('this lab checks at most six points at a time');
    for (i = 0; i < parts.length; i += 1) out.push(DB_list(parts[i], 'a point ' + vars[0] + ' ' + vars[1], [2]));
    return out;
  }
  function jbAt(vars, p) { var o = {}; o[vars[0]] = p[0]; o[vars[1]] = p[1]; return o; }
  function jbPtext(p) { return DB_vec(p[0], p[1]); }
  function jbCheckText(f, g, vars, p) {
    var fv = MPeval(f, jbAt(vars, p)), gv = MPeval(g, jbAt(vars, p));
    if (Rzero(fv) && Rzero(gv)) return { eq: true, text: 'is an equilibrium' };
    return { eq: false, text: 'f = ' + DE_q(fv) + ', g = ' + DE_q(gv) + ': not an equilibrium' };
  }
  /* every (p/q, r/q) with |p|, |r| ≤ 12 and q from 1 to 4, tested exactly */
  function jbSearch(f, g, vars) {
    var seen = {}, hits = [], q, p, r;
    for (q = 1; q <= 4; q += 1) {
      for (p = -12; p <= 12; p += 1) {
        for (r = -12; r <= 12; r += 1) {
          var pt = [R(BigInt(p), BigInt(q)), R(BigInt(r), BigInt(q))], key = Rtext(pt[0]) + ',' + Rtext(pt[1]);
          if (seen[key]) continue;
          seen[key] = 1;
          var at = jbAt(vars, pt);
          if (Rzero(MPeval(f, at)) && Rzero(MPeval(g, at))) hits.push(pt);
        }
      }
    }
    hits.sort(function (u, w) { return Rcmp(u[0], w[0]) || Rcmp(u[1], w[1]); });
    if (!hits.length) return { hits: hits, text: 'found none' };
    var shown = hits.slice(0, 6).map(jbPtext).join(', ');
    return { hits: hits, text: 'found ' + hits.length + ': ' + shown + (hits.length > 6 ? ', …' : '') };
  }
  /* f = −β·S·I and g = β·S·I − γ·I, read off the coefficients */
  function jbSIR(f, g, start) {
    if (!start) return { why: 'give a start S0 I0 to compute R₀' };
    var SI = function (t) { return t.e[0] === 1 && t.e[1] === 1; }, I1 = function (t) { return t.e[0] === 0 && t.e[1] === 1; };
    if (f.terms.length !== 1 || !SI(f.terms[0]) || Rsign(f.terms[0].c) >= 0) return { why: 'f is not of the form −β·S·I' };
    var beta = Rneg(f.terms[0].c), gamma = null, i;
    if (g.terms.length !== 2) return { why: 'g is not of the form β·S·I − γ·I' };
    for (i = 0; i < 2; i += 1) {
      if (SI(g.terms[i])) { if (!Requ(g.terms[i].c, beta)) return { why: 'the S·I coefficients of f and g do not cancel' }; }
      else if (I1(g.terms[i]) && Rsign(g.terms[i].c) < 0) gamma = Rneg(g.terms[i].c);
      else return { why: 'g is not of the form β·S·I − γ·I' };
    }
    if (gamma === null) return { why: 'g is not of the form β·S·I − γ·I' };
    var R0v = Rdiv(Rmul(beta, start[0]), gamma), peak = Rdiv(gamma, beta);
    var tail = Rcmp(start[0], peak) > 0 ? 'I peaks at S = ' + DE_q(peak) : 'I falls from the start';
    return { beta: beta, gamma: gamma, text: 'R₀ = ' + DE_q(R0v) + '; ' + tail };
  }
  function jbCompute(fText, gText, vars, ptsText, atIndex, search, extra, startText) {
    var lim = { degree: 3, terms: 24 };
    var f = MPparse(fText, vars, lim), g = MPparse(gText, vars, lim);
    var pts = jbPointList(ptsText, vars), at = atIndex >= 0 && atIndex < pts.length ? atIndex : 0;
    var start = DB_blank(startText) ? null : DB_list(startText, 'the start', [2]);
    var r = { f: f, g: g, vars: vars, pts: pts, at: at, start: start };
    r.checks = pts.map(function (p) { return jbCheckText(f, g, vars, p); });
    var P = jbAt(vars, pts[at]);
    var J = [[MPeval(MPpartial(f, vars[0]), P), MPeval(MPpartial(f, vars[1]), P)],
             [MPeval(MPpartial(g, vars[0]), P), MPeval(MPpartial(g, vars[1]), P)]];
    var M = DB_mat(J);
    r.J = J; r.M = M;
    r.type = !r.checks[at].eq ? '—' : (M.type === 'centre' ? 'centre (linearisation inconclusive)' : M.type);
    r.found = search === 'grid' ? jbSearch(f, g, vars) : null;
    r.sir = extra === 'sir' ? jbSIR(f, g, start) : null;
    return r;
  }
"""


def _jacobian(cfg):
    mode = "jacobian"
    found = dc.presets(cfg, KIT, mode)
    view = dc.choice(cfg, "view", ["field", "linearised", "trajectory"], KIT, mode)
    search = dc.choice(cfg, "search", ["off", "grid"], KIT, mode)
    table = {}
    for p in found:
        vars_ = list(p.get("vars") or ["x", "y"])
        dc.check(KIT, mode, p, vars_ in (["x", "y"], ["S", "I"]), "vars must be ['x', 'y'] or ['S', 'I']")
        pts = p.get("points")
        dc.check(KIT, mode, p, isinstance(pts, (list, tuple)) and 1 <= len(pts) <= 6
                 and all(isinstance(q, (list, tuple)) and len(q) == 2 for q in pts),
                 "points must be a list of one to six [x, y] pairs")
        win = p.get("window")
        if win is not None:
            dc.check(KIT, mode, p, isinstance(win, (list, tuple)) and len(win) == 4,
                     "window must be [xmin, xmax, ymin, ymax]")
            win = [float(_f(dc.rational(w, KIT, mode, p, "window"))) for w in win]
            dc.check(KIT, mode, p, win[0] < win[1] and win[2] < win[3], "window must have xmin < xmax and ymin < ymax")
        extra = p.get("extra")
        dc.check(KIT, mode, p, extra in (None, "sir"), "extra must be 'sir' or None")
        table[str(p["id"])] = {
            "f": _formula(p, mode, "f", set(vars_)), "g": _formula(p, mode, "g", set(vars_)), "vars": vars_,
            "points": "; ".join(" ".join(dc.rational(v, KIT, mode, p, "points") for v in q) for q in pts),
            "labels": ["(%s)" % ", ".join(str(_f(dc.rational(v, KIT, mode, p, "points"))).replace("-", "−") for v in q)
                       for q in pts],
            "start": _rlist(p, mode, "start", (2,), allow_none=True), "window": win, "extra": extra}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    v0, v1 = first["vars"]
    tiles = [("At the selected point", "jbCheck"), ("Jacobian J", "jbJ"), ("Trace of J", "jbTrace"),
             ("Determinant of J", "jbDet"), ("Eigenvalues of J", "jbEig"), ("Linearised type", "jbType"),
             ("Grid search", "jbFound"), ("Epidemic threshold", "jbExtra")]
    markup = (
        dc.toolbar("A nonlinear system", "equilibria checked exactly, linearised by the Jacobian",
                   [("muted", "the field"), ("green", "listed points"), ("cyan", "drawn by stepping in floating point")])
        + dc.stage(dc.svg("jbPlot", "the phase plane of the nonlinear system"))
        + dc.wrap("jbTable")
        + dc.banner("jbStatus")
    )
    controls = (
        dc.select("jbPreset", "System", dc.options(found), pick["id"])
        + dc.text("jbF", "%s′ = f(%s, %s)" % (v0, v0, v1), first["f"], label_id="jbFLabel")
        + dc.text("jbG", "%s′ = g(%s, %s)" % (v1, v0, v1), first["g"], label_id="jbGLabel")
        + dc.text("jbPoints", "Points to check (x y; x y)", first["points"])
        + dc.select("jbAt", "Linearise at", [(str(i), lab) for i, lab in enumerate(first["labels"])], "0")
        + dc.text("jbStart", "Start for the trajectory (may be empty)", first["start"])
        + dc.select("jbSearch", "Search a grid of fractions", [("off", "off"), ("grid", "on")], search)
        + dc.select("jbView", "View", [("field", "the field"), ("linearised", "the linearisation"),
                                       ("trajectory", "a trajectory")], view)
        + dc.kpis(tiles)
        + dc.hint("Polynomials of degree 3 at most: y - x^2, x(3 - x - 2y).")
    )
    glue = dc.literal("JBP", table) + r"""
  var JB_TILES = ['jbCheck', 'jbJ', 'jbTrace', 'jbDet', 'jbEig', 'jbType', 'jbFound', 'jbExtra'];
  var jbPresetIn = DE_el('jbPreset'), jbFIn = DE_el('jbF'), jbGIn = DE_el('jbG'), jbPointsIn = DE_el('jbPoints');
  var jbAtIn = DE_el('jbAt'), jbStartIn = DE_el('jbStart'), jbSearchIn = DE_el('jbSearch'), jbViewIn = DE_el('jbView');
  var jbCur = JBP[jbPresetIn.value] || JBP[Object.keys(JBP)[0]];
  function jbOptions(pts, keep) {
    var html = '', i;
    for (i = 0; i < pts.length; i += 1) html += '<option value=' + i + '>' + DE_esc(jbPtext(pts[i])) + '</option>';
    DE_html('jbAt', html);
    jbAtIn.value = String(keep >= 0 && keep < pts.length ? keep : 0);
  }
  function jbRender(r, view) {
    var J = r.J, M = r.M, vars = r.vars;
    DE_set('jbCheck', r.checks[r.at].text);
    DE_set('jbJ', DB_mattext(J));
    DE_set('jbTrace', DE_q(M.tau));
    DE_set('jbDet', DE_q(M.det));
    DE_set('jbEig', M.eig);
    DE_set('jbType', r.type);
    DE_set('jbFound', r.found ? r.found.text : '—');
    DE_set('jbExtra', r.sir && r.sir.text ? r.sir.text : '—');
    var rows = r.pts.map(function (p, i) { return [jbPtext(p), r.checks[i].text]; });
    DE_html('jbTable', DB_table('Each listed point, tested exactly', ['(' + vars[0] + ', ' + vars[1] + ')', 'f and g there'], rows));
    var fx = function (x, y) { var o = {}; o[vars[0]] = x; o[vars[1]] = y; return [MPevalFloat(r.f, o), MPevalFloat(r.g, o)]; };
    var win = jbCur && jbCur.window ? { xmin: jbCur.window[0], xmax: jbCur.window[1], ymin: jbCur.window[2], ymax: jbCur.window[3] } : null;
    if (!win) {
      var xs = r.pts.map(function (p) { return DE_float(p[0]); }), ys = r.pts.map(function (p) { return DE_float(p[1]); });
      if (r.start) { xs.push(DE_float(r.start[0])); ys.push(DE_float(r.start[1])); }
      win = { xmin: Math.min.apply(null, xs) - 1.5, xmax: Math.max.apply(null, xs) + 1.5, ymin: Math.min.apply(null, ys) - 1.5, ymax: Math.max.apply(null, ys) + 1.5 };
    }
    var plot = DB_plot('jbPlot', win, 'the system ' + vars[0] + '′ = ' + MPtext(r.f) + ', ' + vars[1] + '′ = ' + MPtext(r.g)), note = '';
    if (view === 'linearised') {
      var Jf = J.map(function (row) { return row.map(DE_float); }), cx = DE_float(r.pts[r.at][0]), cy = DE_float(r.pts[r.at][1]);
      var rad = 0.3 * Math.min(win.xmax - win.xmin, win.ymax - win.ymin), k;
      var lin = function (t, u, v) { return [Jf[0][0] * u + Jf[0][1] * v, Jf[1][0] * u + Jf[1][1] * v]; };
      var back = function (t, u, v) { var d = lin(t, u, v); return [-d[0], -d[1]]; };
      for (k = 0; k < 8; k += 1) {
        var s0 = [0, rad * Math.cos(Math.PI * k / 4), rad * Math.sin(Math.PI * k / 4)];
        [lin, back].forEach(function (fn) {
          DE_polyline(plot, DE_rk4float(fn, s0, 0.02, 300).map(function (q) { return [q[0] + cx, q[1] + cy]; }), 'plot-curve alt');
        });
      }
    } else if (view === 'trajectory' && r.start) {
      DE_polyline(plot, DE_rk4float(function (t, x, y) { return fx(x, y); }, [0, DE_float(r.start[0]), DE_float(r.start[1])], 0.02, 1500), 'plot-curve alt');
      var ex = DE_eulerSys(r.f, r.g, R0, r.start[0], r.start[1], R(1n, 8n), 8, vars);
      DE_polyline(plot, ex.rows.map(function (q) { return [DE_float(q.x), DE_float(q.y)]; }), 'plot-curve good');
      note = ' ' + ex.steps + ' exact Euler steps with h = 1/8 from the start' + (ex.stopped ? ', then the digit budget stopped them (a quadratic right-hand side doubles the digits each step)' : '') + '.';
    } else DE_arrows(plot, fx, 15);
    r.pts.forEach(function (p, i) { plot.point(DE_float(p[0]), DE_float(p[1]), r.checks[i].eq ? 'plot-point root' : 'plot-point', jbPtext(p)); });
    DE_ok('jbStatus', '<strong>Exact.</strong> At ' + DE_esc(jbPtext(r.pts[r.at])) + ' the system ' + DE_esc(r.checks[r.at].text)
      + '; J = ' + DE_esc(DB_mattext(J)) + ', trace ' + DE_esc(DE_q(M.tau)) + ', determinant ' + DE_esc(DE_q(M.det)) + '.'
      + (r.found ? ' The search tried every (p/q, r/q) with |p|, |r| ≤ 12 and q from 1 to 4, and ' + DE_esc(r.found.text) + '; it cannot see an equilibrium off that grid.' : '')
      + (r.sir && r.sir.why ? ' No epidemic threshold: ' + DE_esc(r.sir.why) + '.' : '') + DE_esc(note));
  }
  function redraw() {
    var r;
    try {
      r = jbCompute(jbFIn.value, jbGIn.value, jbCur.vars, jbPointsIn.value, parseInt(jbAtIn.value, 10), jbSearchIn.value,
                    jbCur.extra, jbStartIn.value);
    } catch (e) {
      DE_refuse('jbStatus', JB_TILES, ['jbPlot', 'jbTable'], DE_msg(e)); return;
    }
    jbRender(r, jbViewIn.value);
  }
  jbPresetIn.addEventListener('change', function () {
    var p = JBP[jbPresetIn.value];
    if (p) {
      jbCur = p;
      jbFIn.value = p.f; jbGIn.value = p.g; jbPointsIn.value = p.points; jbStartIn.value = p.start;
      DE_set('jbFLabel', p.vars[0] + '′ = f(' + p.vars[0] + ', ' + p.vars[1] + ')');
      DE_set('jbGLabel', p.vars[1] + '′ = g(' + p.vars[0] + ', ' + p.vars[1] + ')');
      try { jbOptions(jbPointList(p.points, p.vars), 0); } catch (e) { jbAtIn.value = '0'; }
    }
    redraw();
  });
  jbPointsIn.addEventListener('input', function () {
    try { jbOptions(jbPointList(jbPointsIn.value, jbCur.vars), parseInt(jbAtIn.value, 10)); } catch (e) { /* the redraw refuses */ }
    redraw();
  });
  [jbFIn, jbGIn, jbStartIn].forEach(function (el) { el.addEventListener('input', redraw); });
  [jbAtIn, jbSearchIn, jbViewIn].forEach(function (el) { el.addEventListener('change', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Equilibria and the Jacobian", subtitle="Checked exactly, linearised, and classified",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", "STEP", "DRAW", extra=DB_JS + DB_TAB_JS + DB_ROOT_JS + DB_MAT_JS + JACOBIAN_JS + glue),
        panel_title="Choose the system",
        panel_intro="A point is an equilibrium when f and g are both exactly 0 there. The Jacobian of partial "
                    "derivatives at an equilibrium is a linear system, classified by its trace and determinant.",
        select="jbPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# laplace (lp)
# ---------------------------------------------------------------------------

LAPLACE_JS = r"""
  /* ---- dekit/laplace: transforms as exact rational functions of s ---------
     ℒ of an exponential polynomial is EPlaplace. Inverting factors the
     denominator into linear factors (Pfactor) and irreducible quadratics
     (the characteristic polynomial and the forcing's (s − a)² + b² are
     tried first), then solves one exact linear system for the coefficients
     of the time functions those factors name, and transforms the answer back
     to check it. A quadratic with irrational roots or an irrational
     frequency is refused by name. */
  function LP_quadkey(q) { return q.map(Rtext).join(','); }
  /* the monic quadratics (s − a)² + b² an exponential polynomial carries */
  function LP_cands(e, list) {
    var out = list || [], seen = {}, i;
    for (i = 0; i < out.length; i += 1) seen[LP_quadkey(out[i])] = 1;
    for (i = 0; i < e.length; i += 1) {
      if (e[i].trig === '1') continue;
      var a = e[i].a, b = e[i].b, q = [Radd(Rmul(a, a), Rmul(b, b)), Rmul(R(-2n), a), R1];
      if (!seen[LP_quadkey(q)]) { seen[LP_quadkey(q)] = 1; out.push(q); }
    }
    return out;
  }
  function LP_factor(den, cands) {
    var fac = Pfactor(den), lin = [], quads = [], i;
    for (i = 0; i < fac.factors.length; i += 1) lin.push({ root: fac.factors[i].root, mult: fac.factors[i].mult });
    lin.sort(function (x, y) { return Rcmp(y.root, x.root); });
    var rest = fac.rest.length ? Pmonic(fac.rest) : [];
    if (Pdeg(rest) > 0) {
      for (i = 0; i < (cands || []).length; i += 1) {
        var m = 0;
        while (Pdeg(rest) >= 2) {
          var dm = Pdivmod(rest, cands[i]);
          if (!Pzero(dm.r)) break;
          rest = Pmonic(dm.q); m += 1;
        }
        if (m) quads.push({ poly: cands[i], mult: m });
      }
      if (Pdeg(rest) === 2) quads.push({ poly: rest, mult: 1 });
      else if (Pdeg(rest) > 2) throw new Error('the denominator has the factor ' + DE_ptext(rest, 's') + ', irreducible of degree 3 or more; this lab does not split it');
    }
    for (i = 0; i < quads.length; i += 1) {
      var q = quads[i], al = Rdiv(Rneg(q.poly[1]), R(2n)), b2 = Rsub(q.poly[0], Rmul(al, al));
      if (Rsign(b2) <= 0) {
        throw new Error('the factor ' + DE_ptext(q.poly, 's') + ' has irrational roots; the solution would have'
          + ' irrational exponents, which this lab does not print');
      }
      var be = Rsqrt(b2);
      if (be === null) {
        throw new Error('the factor ' + DE_ptext(q.poly, 's') + ' gives the frequency √(' + DE_q(b2)
          + '), which is irrational: the solution has an irrational frequency this lab does not print');
      }
      q.alpha = al; q.beta = be;
    }
    quads.sort(function (x, y) { return Rcmp(y.alpha, x.alpha) || Rcmp(x.beta, y.beta); });
    return { lin: lin, quads: quads };
  }
  function LP_den(fz) {
    var parts = [], i;
    for (i = 0; i < fz.lin.length; i += 1) parts.push(RFfactortext({ root: fz.lin[i].root, mult: fz.lin[i].mult }, 's'));
    for (i = 0; i < fz.quads.length; i += 1) {
      parts.push(RFfactortext({ quad: fz.quads[i].poly }, 's') + (fz.quads[i].mult > 1 ? DE_sup(fz.quads[i].mult) : ''));
    }
    if (!parts.length) return '';
    return parts.length > 1 ? '(' + parts.join('') + ')' : parts[0];
  }
  function LP_rftext(F, fz) {
    var num = DE_ptext(F.num, 's'), den = LP_den(fz);
    if (den === '') return num;
    return RFbracket(num) + '/' + den;
  }
  function LP_poles(fz) {
    var out = [], lin = fz.lin.slice(), i;
    lin.sort(function (x, y) { return Rcmp(x.root, y.root); });
    for (i = 0; i < lin.length; i += 1) out.push(DE_q(lin[i].root) + (lin[i].mult > 1 ? ' (repeated)' : ''));
    for (i = 0; i < fz.quads.length; i += 1) {
      out.push(DE_root(fz.quads[i].alpha, { q: fz.quads[i].beta, k: 1n }, true) + (fz.quads[i].mult > 1 ? ' (repeated)' : ''));
    }
    return out.length ? out.join(', ') : 'none';
  }
  /* solve Σ xᵢ·Nᵢ = F.num for the basis numerators Nᵢ over the denominator D */
  function LP_system(F, nums) {
    var n = Pdeg(F.den), M = [], rhs = [], r, i;
    if (nums.length !== n) throw new Error('the factors do not account for the denominator');
    for (r = 0; r < n; r += 1) {
      var row = [];
      for (i = 0; i < n; i += 1) row.push(nums[i][r] || R0);
      M.push(row);
      rhs.push(F.num[r] || R0);
    }
    var x = RFsolve(M, rhs);
    if (x === null) throw new Error('the coefficient system is singular');
    return x;
  }
  function LP_proper(F) {
    if (!RFzero(F) && Pdeg(F.num) >= Pdeg(F.den)) {
      throw new Error('the transform ' + RFtext(F, 's') + ' has a polynomial part, which is not the transform of a function this lab prints');
    }
  }
  /* the inverse transform: the time functions the factors name, fitted */
  function LP_invert(F, fz) {
    if (RFzero(F)) return [];
    LP_proper(F);
    var basis = [], i, j;
    for (i = 0; i < fz.lin.length; i += 1) {
      for (j = 0; j < fz.lin[i].mult; j += 1) basis.push(EPmake([{ c: R1, k: j, a: fz.lin[i].root, b: R0, trig: '1' }]));
    }
    for (i = 0; i < fz.quads.length; i += 1) {
      var q = fz.quads[i];
      for (j = 0; j < q.mult; j += 1) {
        basis.push(EPmake([{ c: R1, k: j, a: q.alpha, b: q.beta, trig: 'cos' }]));
        basis.push(EPmake([{ c: R1, k: j, a: q.alpha, b: q.beta, trig: 'sin' }]));
      }
    }
    var nums = basis.map(function (e) {
      var L = EPlaplace(e), dm = Pdivmod(F.den, L.den);
      if (!Pzero(dm.r)) throw new Error('the factors do not account for the denominator');
      return Pmul(L.num, dm.q);
    });
    var x = LP_system(F, nums), out = [];
    for (i = 0; i < basis.length; i += 1) out = EPadd(out, EPscale(basis[i], x[i]));
    if (!RFequal(EPlaplace(out), F)) throw new Error('the inverse did not transform back to F');
    return out;
  }
  /* partial fractions over the same factors */
  function LP_partial(F, fz) {
    if (RFzero(F)) return [];
    LP_proper(F);
    var D = F.den, cols = [], nums = [], i, j;
    for (i = 0; i < fz.lin.length; i += 1) {
      var lin = [Rneg(fz.lin[i].root), R1];
      for (j = 1; j <= fz.lin[i].mult; j += 1) {
        nums.push(Pdivmod(D, Ppow(lin, j)).q);
        cols.push({ root: fz.lin[i].root, power: j });
      }
    }
    for (i = 0; i < fz.quads.length; i += 1) {
      for (j = 1; j <= fz.quads[i].mult; j += 1) {
        var co = Pdivmod(D, Ppow(fz.quads[i].poly, j)).q;
        nums.push(Pmul([R0, R1], co)); cols.push({ quad: fz.quads[i], power: j, part: 'A' });
        nums.push(co); cols.push({ quad: fz.quads[i], power: j, part: 'B' });
      }
    }
    var x = LP_system(F, nums), out = [];
    for (i = 0; i < cols.length; i += 1) {
      if (cols[i].quad) {
        if (cols[i].part === 'A') out.push({ quad: cols[i].quad, power: cols[i].power, A: x[i], B: x[i + 1] });
      } else if (!Rzero(x[i])) out.push({ root: cols[i].root, power: cols[i].power, coef: x[i] });
    }
    return out;
  }
  function LP_ptext(P) {
    var pieces = [], i;
    for (i = 0; i < P.length; i += 1) {
      var t = P[i];
      if (t.quad) {
        if (Rzero(t.A) && Rzero(t.B)) continue;
        var neg = Rsign(t.A) < 0 || (Rzero(t.A) && Rsign(t.B) < 0);
        var A = neg ? Rneg(t.A) : t.A, B = neg ? Rneg(t.B) : t.B;
        var den = RFfactortext({ quad: t.quad.poly }, 's') + (t.power > 1 ? DE_sup(t.power) : '');
        var nt = DE_ptext([B, A], 's');
        pieces.push((neg ? '−' : '') + (/[ \/]/.test(nt) ? '(' + nt + ')' : nt) + '/' + den);
      } else {
        var c = t.coef, mag = Rabs(c), num = mag.d === 1n ? String(mag.n) : '(' + Rtext(mag) + ')';
        pieces.push((c.n < 0n ? '−' : '') + num + '/' + RFfactortext({ root: t.root, mult: t.power }, 's'));
      }
    }
    return DB_join(pieces);
  }
  function LP_e(c) { return 'e^(' + DE_lin(Rneg(c), 's') + ')'; }
  /* a piece e^(−cs)·F(s) of Y, as text */
  function LP_piece(c, F, fz) {
    if (Rzero(c)) return LP_rftext(F, fz);
    var den = LP_den(fz), tail = den === '' ? '' : '/' + den;
    if (Pdeg(F.num) <= 0) {
      var k = F.num.length ? F.num[0] : R0, mag = Rabs(k), lead;
      if (Requ(mag, R1)) lead = '';
      else if (mag.d === 1n) lead = String(mag.n);
      else lead = '(' + Rtext(mag) + ')·';
      return (k.n < 0n ? '−' : '') + lead + LP_e(c) + tail;
    }
    return LP_e(c) + '·' + LP_rftext(F, fz);
  }
  /* r times a shifted variable v = (t − c): t − c, −(t − c), 2(t − c), (t − c)/2 */
  function LP_lin(r, v) {
    var inner = v.slice(1, -1), neg = r.n < 0n, n = neg ? -r.n : r.n, s;
    if (n === 1n && r.d === 1n) return neg ? '−' + v : inner;
    s = (n === 1n ? '' : String(n)) + v + (r.d === 1n ? '' : '/' + r.d);
    return (neg ? '−' : '') + s;
  }
  function LP_shiftbody(t, v) {
    var parts = [];
    if (t.k >= 1) parts.push(v + (t.k > 1 ? DE_sup(t.k) : ''));
    if (!Rzero(t.a)) parts.push('e^(' + LP_lin(t.a, v) + ')');
    if (t.trig !== '1') parts.push(t.trig + '(' + LP_lin(t.b, v) + ')');
    return parts.join('·');
  }
  function LP_isconst(t) { return t.k === 0 && Rzero(t.a) && t.trig === '1'; }
  /* the value of y on one interval: constants merged, then the unshifted
     terms, then each switched piece written in t − c */
  function LP_value(active) {
    var cst = R0, entries = [], i, j;
    for (i = 0; i < active.length; i += 1) {
      for (j = 0; j < active[i].ep.length; j += 1) if (LP_isconst(active[i].ep[j])) cst = Radd(cst, active[i].ep[j].c);
    }
    entries.push({ c: cst, body: '', dot: false });
    for (i = 0; i < active.length; i += 1) {
      var v = '(t − ' + DE_q(active[i].c) + ')';
      for (j = 0; j < active[i].ep.length; j += 1) {
        var t = active[i].ep[j];
        if (LP_isconst(t)) continue;
        if (Rzero(active[i].c)) entries.push({ c: t.c, body: EPbody(t), dot: !Rzero(t.a) || t.trig !== '1' });
        else entries.push({ c: t.c, body: LP_shiftbody(t, v), dot: true });
      }
    }
    return DE_sum(entries);
  }
  /* forcing terms: k·u(t − c) switched terms, and an exponential polynomial */
  function LP_forcing(list) {
    var ep = [], steps = {}, keys = [], i;
    for (i = 0; i < list.length; i += 1) {
      var text = list[i].text, sign = list[i].neg ? R(-1n) : R1;
      if (/u\s*\(/.test(text)) {
        var m = /^(.*?)[\s*]*u\s*\(\s*t\s*-\s*([0-9]+(?:\/[0-9]+)?|[0-9]*\.[0-9]+)\s*\)\s*$/.exec(text);
        if (!m) {
          if (/u\s*\(\s*t\s*(\+[^)]*)?\)/.test(text)) throw new Error('the step in ' + text + ' switches on at t ≤ 0; this lab takes u(t - c) with c > 0');
          throw new Error('write a switched term as k·u(t - c) with k a number; ' + text + ' is not one');
        }
        var ks = m[1].replace(/^\s+|\s+$/g, '').replace(/^\((.*)\)$/, '$1'), k = ks === '' ? R1 : DE_rat(ks);
        if (k === null) throw new Error('write a switched term as k·u(t - c) with k a number; ' + text + ' is not one');
        var c = DE_rat(m[2]);
        if (c === null || Rsign(c) <= 0) throw new Error('the step in ' + text + ' switches on at t ≤ 0; this lab takes u(t - c) with c > 0');
        var key = Rtext(c);
        if (!steps.hasOwnProperty(key)) { steps[key] = { c: c, k: R0 }; keys.push(key); }
        steps[key].k = Radd(steps[key].k, Rmul(sign, k));
      } else {
        var e;
        try { e = EPparse(text, {}); } catch (err) {
          throw new Error('the forcing term ' + text + ' is outside this lab: ' + DE_msg(err));
        }
        ep = EPadd(ep, EPscale(e, sign));
      }
    }
    var out = [];
    for (i = 0; i < keys.length; i += 1) if (!Rzero(steps[keys[i]].k)) out.push(steps[keys[i]]);
    out.sort(function (x, y) { return Rcmp(x.c, y.c); });
    return { ep: ep, steps: out };
  }
  function LP_float(pieces, t) {
    var acc = 0, i;
    for (i = 0; i < pieces.length; i += 1) {
      var c = DE_float(pieces[i].c);
      if (t >= c) acc += EPevalFloat(pieces[i].ep, t - c);
    }
    return acc;
  }
  function LP_solve(eqText, icText) {
    var E = DB_eqparse(eqText, ['u', 's']), i;
    for (i = 0; i <= E.order; i += 1) {
      if (!DB_isconst(E.coef[i])) {
        throw new Error('this lab transforms equations with constant coefficients; the coefficient ' + RFtext(E.coef[i], 't') + ' is not constant');
      }
    }
    var a = [DB_cval(E.coef[0]), DB_cval(E.coef[1]), DB_cval(E.coef[2])], P = Pnorm(a.slice(0, E.order + 1));
    var ic = DB_list(icText, E.order === 2 ? 'the initial values y(0) y′(0)' : 'the initial value y(0)', [E.order]);
    var fr = LP_forcing(E.forcing);
    var r = { E: E, a: a, P: P, ic: ic, fr: fr, order: E.order };
    var cands = LP_cands(fr.ep, Pdeg(P) === 2 ? [Pmonic(P)] : []);
    /* the unswitched piece: initial values and the exponential forcing */
    var icpoly = E.order === 2 ? [Radd(Rmul(a[2], ic[1]), Rmul(a[1], ic[0])), Rmul(a[2], ic[0])] : [Rmul(a[1], ic[0])];
    var Fe = EPlaplace(fr.ep);
    var Y0 = RFadd(RFmake(icpoly, P), RFdiv(Fe, RFpoly(P)));
    var pieces = [], fpieces = [];
    if (!EPzero(fr.ep)) fpieces.push({ c: R0, F: Fe, fz: LP_factor(Fe.den, LP_cands(fr.ep, [])) });
    if (!RFzero(Y0)) pieces.push({ c: R0, F: Y0, k: null });
    for (i = 0; i < fr.steps.length; i += 1) {
      var st = fr.steps[i];
      pieces.push({ c: st.c, F: RFdiv(RFconst(st.k), RFpoly(Pmul([R0, R1], P))), k: st.k });
      fpieces.push({ c: st.c, F: RFmake([st.k], [R0, R1]), fz: { lin: [{ root: R0, mult: 1 }], quads: [] } });
    }
    for (i = 0; i < pieces.length; i += 1) {
      var pc = pieces[i];
      pc.fz = LP_factor(pc.F.den, cands);
      pc.partial = LP_partial(pc.F, pc.fz);
      pc.ep = LP_invert(pc.F, pc.fz);
    }
    r.pieces = pieces;
    r.poles = E.order === 2 ? LP_poles(LP_factor(Pmonic(P), [])) : DE_q(Rdiv(Rneg(a[0]), a[1]));
    r.lpF = fpieces.length ? DB_join(fpieces.map(function (fp) { return LP_piece(fp.c, fp.F, fp.fz); })) : '0';
    r.lpY = pieces.length ? DB_join(pieces.map(function (pc) { return LP_piece(pc.c, pc.F, pc.fz); })) : '0';
    r.lpPartial = pieces.length ? DB_join(pieces.map(function (pc) {
      var t = LP_ptext(pc.partial);
      return Rzero(pc.c) ? t : LP_e(pc.c) + '·(' + t + ')';
    })) : '0';
    /* the solution: one exponential polynomial, or one per interval */
    var cs = [], j;
    for (i = 0; i < pieces.length; i += 1) if (!Rzero(pieces[i].c)) cs.push(pieces[i].c);
    var base = pieces.length && Rzero(pieces[0].c) ? [pieces[0]] : [];
    if (!cs.length) r.solution = base.length ? EPtext(base[0].ep) : '0';
    else {
      var parts = [LP_value(base) + ' for t < ' + DE_q(cs[0])];
      for (j = 0; j < cs.length; j += 1) {
        var active = pieces.filter(function (pc) { return Rcmp(pc.c, cs[j]) <= 0; });
        parts.push(LP_value(active) + ' for ' + (j + 1 < cs.length ? DE_q(cs[j]) + ' ≤ t < ' + DE_q(cs[j + 1]) : 't ≥ ' + DE_q(cs[j])));
      }
      r.solution = parts.join('; ');
    }
    /* the check: each piece substituted back */
    var ok = true;
    for (i = 0; i < pieces.length; i += 1) {
      var e0 = pieces[i].ep, d1 = EPderiv(e0), d2 = EPderiv(d1);
      var lhs = EPadd(EPadd(EPscale(d2, a[2]), EPscale(d1, a[1])), EPscale(e0, a[0]));
      var want = Rzero(pieces[i].c) ? fr.ep : EPconst(pieces[i].k);
      var y0w = Rzero(pieces[i].c) ? ic[0] : R0, v0w = Rzero(pieces[i].c) ? (E.order === 2 ? ic[1] : null) : R0;
      if (!EPzero(EPsub(lhs, want)) || !Requ(EPevalExact(e0, R0), y0w)) ok = false;
      if (E.order === 2 && v0w !== null && !Requ(EPevalExact(d1, R0), v0w)) ok = false;
    }
    if (!pieces.length) ok = EPzero(fr.ep);
    r.check = ok ? 'residual 0' : 'the check failed';
    return r;
  }
  /* table, derivative, partial */
  function LP_table(fText) {
    var f = EPparse(fText, {}), F = EPlaplace(f), fz = LP_factor(F.den, LP_cands(f, []));
    return { f: f, F: F, fz: fz };
  }
"""


def _laplace(cfg):
    mode = "laplace"
    found = dc.presets(cfg, KIT, mode)
    kinds = ["table", "derivative", "solve", "partial", "step"]
    table = {}
    for p in found:
        kind = p.get("kind")
        dc.check(KIT, mode, p, kind in kinds, "kind must be one of %s" % ", ".join(kinds))
        if kind in ("table", "derivative"):
            sig = _formula(p, mode, "f", set("tecosinxp"))
            eq, ic = "", ""
        elif kind == "partial":
            sig = _formula(p, mode, "F", set("s"))
            eq, ic = "", ""
        else:
            sig = ""
            eq = _eq(p, mode, "equation")
            ic = _rlist(p, mode, "ic", (1, 2))
        table[str(p["id"])] = {"kind": kind, "f": sig, "eq": eq, "ic": ic}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    signal = first["kind"] in ("table", "derivative", "partial")
    tiles = [("Transform ℒ[f], or ℒ of the forcing", "lpF"), ("Poles", "lpPoles"),
             ("Y(s), or ℒ[f′] for the derivative rule", "lpY"), ("Partial fractions", "lpPartial"),
             ("Solution, or the inverse", "lpSolution"), ("Substituted back", "lpCheck"),
             ("ℒ[f′] against s·F − f(0)", "lpEqual")]
    markup = (
        dc.toolbar("The Laplace transform", "functions of t as exact rational functions of s",
                   [("cyan", "the function of t, drawn from its closed form")])
        + dc.stage(dc.svg("lpPlot", "the function of t"))
        + dc.banner("lpStatus")
    )
    controls = (
        dc.select("lpPreset", "Example", dc.options(found), pick["id"])
        + dc.select("lpKind", "What to compute", [("table", "a transform"), ("derivative", "the derivative rule"),
                                                  ("solve", "solve an equation"), ("partial", "partial fractions"),
                                                  ("step", "switched forcing")], first["kind"])
        + dc.text("lpFIn", "F(s)" if first["kind"] == "partial" else "Signal f(t)", first["f"],
                  label_id="lpFLabel", disabled=not signal)
        + dc.text("lpEq", "Equation", first["eq"], disabled=signal)
        + dc.text("lpIC", "Initial values y(0), then y′(0)", first["ic"], disabled=signal)
        + dc.kpis(tiles)
        + dc.hint("A signal such as 3t^2 - 2e^(-t) or cos(2t); an equation such as y'' + 3y' + 2y = u(t - 1).")
    )
    glue = dc.literal("LPP", table) + r"""
  var LP_TILES = ['lpF', 'lpPoles', 'lpY', 'lpPartial', 'lpSolution', 'lpCheck', 'lpEqual'];
  var lpPresetIn = DE_el('lpPreset'), lpKindIn = DE_el('lpKind'), lpFIn = DE_el('lpFIn'), lpEqIn = DE_el('lpEq');
  var lpICIn = DE_el('lpIC');
  function lpInputs(kind) {
    var signal = kind === 'table' || kind === 'derivative' || kind === 'partial';
    lpFIn.disabled = !signal; lpEqIn.disabled = signal; lpICIn.disabled = signal;
    DE_set('lpFLabel', kind === 'partial' ? 'F(s)' : 'Signal f(t)');
  }
  /* ∫₀ᵀ e^(−s·t)·f(t) dt by Simpson's rule, in doubles, for the banner */
  function lpTrunc(f, s, T) {
    var n = 2000, h = T / n, acc = 0, i;
    for (i = 0; i <= n; i += 1) {
      var t = i * h, w = (i === 0 || i === n) ? 1 : (i % 2 ? 4 : 2);
      acc += w * Math.exp(-s * t) * EPevalFloat(f, t);
    }
    return acc * h / 3;
  }
  function lpCompute(kind) {
    var r = { kind: kind };
    if (kind === 'table' || kind === 'derivative') {
      var T = LP_table(lpFIn.value);
      r.T = T;
      r.lpF = LP_rftext(T.F, T.fz);
      r.lpPoles = RFzero(T.F) ? 'none' : LP_poles(T.fz);
      if (kind === 'table') r.lpPartial = LP_ptext(LP_partial(T.F, T.fz));
      else {
        var D = EPlaplace(EPderiv(T.f)), f0 = EPevalExact(T.f, R0);
        var rule = RFsub(RFmul(RFvar(), T.F), RFconst(f0));
        r.lpY = LP_rftext(D, LP_factor(D.den, LP_cands(T.f, [])));
        r.rule = rule; r.f0 = f0;
        r.lpEqual = RFequal(D, rule) ? 'equal' : 'differ';
      }
      r.draw = function (t) { return EPevalFloat(T.f, t); };
      return r;
    }
    if (kind === 'partial') {
      var F = RFparse(lpFIn.value, 's'), fz = LP_factor(F.den, []);
      LP_proper(F);
      r.F = F;
      r.lpF = LP_rftext(F, fz);
      r.lpPoles = RFzero(F) ? 'none' : LP_poles(fz);
      r.lpPartial = LP_ptext(LP_partial(F, fz));
      var inv = LP_invert(F, fz);
      r.lpSolution = EPtext(inv);
      r.draw = function (t) { return EPevalFloat(inv, t); };
      return r;
    }
    var S = LP_solve(lpEqIn.value, lpICIn.value);
    r.S = S;
    r.lpF = S.lpF; r.lpPoles = S.poles; r.lpY = S.lpY; r.lpPartial = S.lpPartial; r.lpSolution = S.solution; r.lpCheck = S.check;
    r.draw = function (t) { return LP_float(S.pieces, t); };
    return r;
  }
  function lpRender(r) {
    LP_TILES.forEach(function (id) { DE_set(id, '—'); });
    ['lpF', 'lpPoles', 'lpY', 'lpPartial', 'lpSolution', 'lpCheck', 'lpEqual'].forEach(function (id) {
      if (r[id] !== undefined) DE_set(id, r[id]);
    });
    var top = 6, i;
    if (r.S) for (i = 0; i < r.S.pieces.length; i += 1) top = Math.max(top, DE_float(r.S.pieces[i].c) + 5);
    var plot = DB_plot('lpPlot', DB_window([r.draw], 0, top), 'the function of t');
    plot.curve(r.draw);
    var msg = '<strong>Exact.</strong> ';
    if (r.kind === 'table') {
      var s0 = 1, k;
      r.T.fz.lin.forEach(function (l) { s0 = Math.max(s0, Math.floor(DE_float(l.root)) + 1); });
      r.T.fz.quads.forEach(function (q) { s0 = Math.max(s0, Math.floor(DE_float(q.alpha)) + 1); });
      var Fs = RFeval(r.T.F, R(BigInt(s0))), vals = [];
      for (k = 0; k < 3; k += 1) vals.push(DE_dec(lpTrunc(r.T.f, s0, [1, 2, 5][k])));
      msg += 'ℒ[' + DE_esc(EPtext(r.T.f)) + '] = ' + DE_esc(r.lpF) + ', term by term from the table. At s = ' + s0
        + ' the integrals of e^(−st)·f(t) from 0 to T = 1, 2, 5 are ' + DE_esc(vals.join(', '))
        + ' (rounded), closing in on F(' + s0 + ') = ' + DE_esc(Fs === null ? '—' : DE_q(Fs)) + '.';
    } else if (r.kind === 'derivative') {
      msg += 'ℒ[f′] computed from f′ = ' + DE_esc(EPtext(EPderiv(r.T.f))) + ' is ' + DE_esc(r.lpY) + '; s·F − f(0) with f(0) = '
        + DE_esc(DE_q(r.f0)) + ' simplifies to ' + DE_esc(RFtext(r.rule, 's', true)) + ': ' + r.lpEqual + '.';
    } else if (r.kind === 'partial') {
      msg += DE_esc(r.lpF) + ' = ' + DE_esc(r.lpPartial) + '; each piece inverts by the table, and the inverse transforms back to F exactly.';
    } else {
      msg += 'Transforming both sides gives Y(s) = ' + DE_esc(r.lpY) + '; partial fractions ' + DE_esc(r.lpPartial)
        + '; inverted, y = ' + DE_esc(r.lpSolution) + '. Substituted back into the equation with its initial values: '
        + DE_esc(r.lpCheck) + '.';
    }
    DE_ok('lpStatus', msg);
  }
  function redraw() {
    var r;
    try {
      r = lpCompute(lpKindIn.value);
    } catch (e) {
      DE_refuse('lpStatus', LP_TILES, ['lpPlot'], DE_msg(e)); return;
    }
    lpRender(r);
  }
  lpPresetIn.addEventListener('change', function () {
    var p = LPP[lpPresetIn.value];
    if (p) { lpKindIn.value = p.kind; lpFIn.value = p.f; lpEqIn.value = p.eq; lpICIn.value = p.ic; lpInputs(p.kind); }
    redraw();
  });
  lpKindIn.addEventListener('change', function () { lpInputs(lpKindIn.value); redraw(); });
  [lpFIn, lpEqIn, lpICIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The Laplace transform", subtitle="Transforms, partial fractions and solutions, exactly",
        markup=markup, controls=controls,
        script=dc.script("EP", extra=DB_JS + DB_EQ_JS + LAPLACE_JS + glue),
        panel_title="Choose the example",
        panel_intro="Every transform here is an exact rational function of s. Solving an equation is algebra on "
                    "Y(s), then partial fractions, then the table read backwards.",
        select="lpPreset", presets=found,
    )

MODES = {
    "linear1": _linear1,
    "stiff": _stiff,
    "char": _char,
    "oscillator": _oscillator,
    "phase": _phase,
    "jacobian": _jacobian,
    "laplace": _laplace,
}
