"""calckit -- the calculus kit of the Differential Equations Subject. Seven modes.

Specified in docs/differential-equations/PLAN.md section D.2; the conventions
in D.0 bind every mode, and the shared blocks come from de_core (D.1). Each
mode computes from the function the lesson states, in the browser, exactly:
a difference quotient is a fraction, a derivative is the number the column of
fractions is printed beside, an integral is a sum of fractions. The one mode
that cannot be exact, `transcendental`, rounds by the stated rule and labels
every figure it rounds.

  quotient        (qt)  (f(a + h) − f(a))/h for a halving column of h; f′(a)
  hpoly           (hp)  the quotient as a polynomial in h; product and chain
                        rules checked against it
  tangent         (tg)  the tangent line and the exact error of the linear
                        approximation
  derivative      (dv)  p′, p″, their rational zeros, where p rises and falls
  transcendental  (tq)  rounded quotients of bᵗ, sin and cos, and the limit
  riemann         (rs)  left, right, trapezoid and midpoint sums; exact errors
  antiderivative  (ad)  F, its constant, F(b) − F(a), linearity, additivity

PRESETS ARE LESSON DATA. Every mode takes cfg['presets'] (each an id, a label
naming the instance, the instance fields of D.2 and `expect`) and
cfg['preset']. The kit writes the instances into a JS table with
de_core.literal and returns Lab(expect={'XXPreset': {id: expect}}). A preset's
change handler rewrites the instance inputs; a redraw-only select (dvOrder,
rsRule) keeps the value the lesson ships. The one select a preset does set is
tqKind, which D.2 names "set by the preset": lesson 7.1 mixes sin and cos.

DEVIATIONS FROM D.2, each the closest correct thing:

  * quotient with show_limit false omits qtGap, the gap column and the tangent
    as well as qtLimit: the gap is |quotient − f′(a)|, and printing it would
    print the derivative on a page that has not defined one.
  * derivative takes `order` from the lesson's cfg, not from a preset: dvOrder
    is a redraw-only select and D.0 forbids a preset touching one. A preset's
    `order` field, if present, must agree with it.
  * antiderivative's f and split inputs are adFIn and adSplitAt: D.2 gives the
    controls the same ids as the tiles adF and adSplit, and a page cannot
    carry one id twice. The tiles keep their names.
  * hpoly prints the quotient grouped by ascending powers of h
    (4t³ − 4t + 6t²h − 2h + 4th² + h³), the reading the lesson asks for.
"""

from . import de_core as dc

KIT = "calckit"
_T = set("t")


def _pf(p, mode, field, letters=_T, allow_none=False):
    return dc.formula(p.get(field), letters, KIT, mode, p, field, allow_none=allow_none)


def _pr(p, mode, field, allow_none=False):
    return dc.rational(p.get(field), KIT, mode, p, field, allow_none=allow_none)


def _int(p, mode, field, lo, hi, default=None):
    value = p.get(field, default)
    dc.check(KIT, mode, p, isinstance(value, int) and not isinstance(value, bool) and lo <= value <= hi,
             "%s must be a whole number from %d to %d, not %r" % (field, lo, hi, value))
    return value


def _hide(cfg_key):
    return "" if cfg_key else ' style="display:none;"'


# ---------------------------------------------------------------------------
# Shared calckit JavaScript: windows and tables. No arithmetic that a tile
# prints happens here.
# ---------------------------------------------------------------------------

CK_JS = r"""
  /* ---- calckit: drawing windows and tables ------------------------------- */
  function CK_window(fns, xmin, xmax) {
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
    if (lo > 0) lo = Math.min(0, lo - 0.1 * (hi - lo));
    if (hi < 0) hi = Math.max(0, hi + 0.1 * (hi - lo));
    if (hi - lo < 1e-9) { lo -= 1; hi += 1; }
    var pad = 0.1 * (hi - lo);
    return { xmin: xmin, xmax: xmax, ymin: lo - pad, ymax: hi + pad };
  }
  function CK_plot(id, win, alt) {
    var svg = DE_el(id);
    var plot = Plot(svg, win).frame();
    plot.describe(alt);
    return plot;
  }
  function CK_line(plot, x0, y0, slope, cls) {
    var w = plot.win;
    plot.segment(w.xmin, y0 + slope * (w.xmin - x0), w.xmax, y0 + slope * (w.xmax - x0), cls);
  }
  function CK_table(caption, head, rows, focus) {
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
  function CK_need(text, what) {
    var r = DE_rat(text);
    if (r === null) throw new Error(what + ' must be a rational number such as 2, -1/2 or 0.25');
    return r;
  }
  function CK_range(id) {
    var el = DE_el(id), v = parseInt(el.value, 10);
    if (!isFinite(v)) v = parseInt(el.getAttribute('min') || '0', 10);
    DE_set(id + 'Out', v);
    return v;
  }
  /* a POLY_JS list at a double, for drawing */
  function CK_pfloat(p, x) {
    var acc = 0, i;
    for (i = p.length - 1; i >= 0; i -= 1) acc = acc * x + Rnum(p[i]);
    return acc;
  }
  function CK_poly(text, what, degree) {
    var p = MPtoPoly(MPparse(text, ['t'], { degree: degree || 12, terms: 24 }), 't');
    if (p === null) throw new Error(what + ' must be a polynomial in t');
    return p;
  }
"""

# ---------------------------------------------------------------------------
# quotient (qt)
# ---------------------------------------------------------------------------

QUOTIENT_JS = r"""
  /* ---- calckit/quotient: the exact difference quotient -------------------
     Q = (f(a + h) − f(a))/h for h, h/2, h/4, ... as fractions, and the number
     f′(a) = (the derivative of f) at a, which the column is printed beside. */
  function qtCompute(fText, aText, hText, halvings) {
    var F = RFparse(fText, 't');
    var a = CK_need(aText, 'a'), h = CK_need(hText, 'h');
    if (Rsign(h) <= 0) throw new Error('h must be positive: the interval is from a to a + h');
    var fa = RFeval(F, a);
    if (fa === null) throw new Error('f is undefined at t = ' + DE_q(a));
    var rows = [], hk = h, k;
    for (k = 0; k <= halvings; k += 1) {
      var fah = RFeval(F, Radd(a, hk));
      if (fah === null) throw new Error('f is undefined at t = ' + DE_q(Radd(a, hk)) + ', the far end of an interval');
      rows.push({ h: hk, fah: fah, q: Rdiv(Rsub(fah, fa), hk) });
      hk = Rdiv(hk, R(2n));
    }
    var limit = RFeval(RFderiv(F), a);
    var i;
    for (i = 0; i < rows.length; i += 1) rows[i].gap = Rabs(Rsub(rows[i].q, limit));
    return { F: F, a: a, h: h, fa: fa, rows: rows, limit: limit };
  }
"""


def _quotient(cfg):
    mode = "quotient"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        table[str(p["id"])] = {
            "f": _pf(p, mode, "f"),
            "a": _pr(p, mode, "a"),
            "h": _pr(p, mode, "h"),
            "halvings": _int(p, mode, "halvings", 0, 12),
        }
        dc.check(KIT, mode, p, table[str(p["id"])]["h"][0] != "-" and table[str(p["id"])]["h"] != "0",
                 "h must be positive")
    show = dc.choice(cfg, "show_limit", ["true", "false"], KIT, mode) == "true"
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("First quotient", "qtFirst"), ("Last quotient", "qtLast")]
    if show:
        tiles += [("Gap to f′(a)", "qtGap"), ("f′(a)", "qtLimit")]
    legend = [("cyan", "f"), ("red", "secant at the smallest h")]
    if show:
        legend.append(("green", "tangent, slope f′(a)"))
    markup = (
        dc.toolbar("Difference quotients, exactly", "the slope of a secant over [a, a + h]", legend)
        + dc.stage(dc.svg("qtPlot", "f with a secant"))
        + dc.wrap("qtTable")
        + dc.banner("qtStatus")
    )
    controls = (
        dc.select("qtPreset", "Function and point", dc.options(found), pick["id"])
        + dc.text("qtF", "f(t)", first["f"])
        + dc.text("qtA", "a", first["a"])
        + dc.text("qtH", "first h", first["h"])
        + dc.range_("qtHalvings", "Halvings of h", 0, 12, first["halvings"])
        + dc.kpis(tiles)
        + dc.hint("Type a polynomial or a ratio of polynomials in t: t^2, t^3 - t, 1/t, (t+1)/(t-2).")
    )
    glue = dc.literal("QTP", table) + dc.literal("QT_SHOW", show) + r"""
  var QT_TILES = ['qtFirst', 'qtLast', 'qtGap', 'qtLimit'];
  var qtPresetIn = DE_el('qtPreset'), qtFIn = DE_el('qtF'), qtAIn = DE_el('qtA'), qtHIn = DE_el('qtH');
  var qtHalvIn = DE_el('qtHalvings');
  function qtRender(r) {
    var last = r.rows[r.rows.length - 1], i, rows = [];
    DE_set('qtFirst', DE_q(r.rows[0].q));
    DE_set('qtLast', DE_q(last.q));
    if (QT_SHOW) { DE_set('qtGap', DE_q(last.gap)); DE_set('qtLimit', DE_q(r.limit)); }
    for (i = 0; i < r.rows.length; i += 1) {
      var row = [DE_q(r.rows[i].h), DE_q(r.rows[i].fah), DE_q(r.rows[i].q)];
      if (QT_SHOW) row.push(DE_q(r.rows[i].gap));
      rows.push(row);
    }
    var head = ['h', 'f(a + h)', 'quotient'];
    if (QT_SHOW) head.push('gap to f′(a)');
    DE_html('qtTable', CK_table('f(a) = ' + DE_q(r.fa) + '; each quotient is (f(a + h) − f(a))/h', head, rows, rows.length - 1));
    var ftext = RFtext(r.F, 't'), a = Rnum(r.a), h0 = Rnum(r.h), span = Math.max(h0, 1) * 0.75;
    var fn = function (x) { return RFevalFloat(r.F, x); };
    var plot = CK_plot('qtPlot', CK_window([fn], a - span, a + h0 + span), 'f(t) = ' + ftext + ' with the secant from a to a + h');
    plot.curve(fn);
    var x1 = Rnum(Radd(r.a, last.h));
    CK_line(plot, a, Rnum(r.fa), Rnum(last.q), 'plot-curve warn');
    if (QT_SHOW) CK_line(plot, a, Rnum(r.fa), Rnum(r.limit), 'plot-curve good');
    plot.point(a, Rnum(r.fa), 'plot-point', 'a').point(x1, Rnum(last.fah), 'plot-point');
    var msg = '<strong>Exact.</strong> f(t) = ' + DE_esc(ftext) + ' at a = ' + DE_esc(DE_q(r.a))
      + ', from h = ' + DE_esc(DE_q(r.h)) + ' halved ' + (r.rows.length - 1) + ' times: the quotient runs from '
      + DE_esc(DE_q(r.rows[0].q)) + ' to ' + DE_esc(DE_q(last.q)) + '.';
    if (QT_SHOW) {
      msg += Rzero(last.gap) && Rzero(r.rows[0].gap)
        ? ' Every row equals f′(a) = ' + DE_esc(DE_q(r.limit)) + ': this quotient does not depend on h.'
        : ' The derivative of f at a is ' + DE_esc(DE_q(r.limit)) + '; the table shows ' + r.rows.length
          + ' quotients, and the claim that they approach it is about every h, not about the last row.';
    }
    DE_ok('qtStatus', msg);
  }
  function redraw() {
    var r;
    try {
      r = qtCompute(qtFIn.value, qtAIn.value, qtHIn.value, CK_range('qtHalvings'));
    } catch (e) {
      DE_refuse('qtStatus', QT_TILES, ['qtTable', 'qtPlot'], DE_msg(e)); return;
    }
    qtRender(r);
  }
  qtPresetIn.addEventListener('change', function () {
    var p = QTP[qtPresetIn.value];
    if (p) { qtFIn.value = p.f; qtAIn.value = p.a; qtHIn.value = p.h; qtHalvIn.value = String(p.halvings); }
    redraw();
  });
  [qtFIn, qtAIn, qtHIn, qtHalvIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Difference quotients", subtitle="Average rates as exact fractions",
        markup=markup, controls=controls, script=dc.script("RF", extra=CK_JS + QUOTIENT_JS + glue),
        panel_title="Choose the function and the point",
        panel_intro="Each row is the average rate of change over [a, a + h], computed as a fraction. "
                    "Halving h adds a row; nothing is rounded.",
        select="qtPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# hpoly (hp)
# ---------------------------------------------------------------------------

HPOLY_JS = r"""
  /* ---- calckit/hpoly: the quotient as a polynomial in h ------------------
     For a polynomial p, p(t + h) − p(t) has h in every term, so dividing by h
     is exact algebra and the part free of h is read off. Nothing approaches
     anything: setting h = 0 happens after the division, never before. */
  var HP_V = ['t', 'h'];
  function hpQuotient(P) {
    var shifted = MPsubst(P, 't', MPadd(MPvar(HP_V, 't'), MPvar(HP_V, 'h')));
    var diff = MPsub(shifted, P), Q = MPdivVar(diff, 'h');
    var C = MPtoPoly(MPsubst(Q, 'h', MPconst(HP_V, R0)), 't');
    return { shifted: shifted, diff: diff, Q: Q, C: C };
  }
  function hpCompute(kind, fText, gText, aText) {
    var f = CK_poly(fText, 'f', 12), g = null, P, rule = null, naive = null;
    if (kind !== 'single') g = CK_poly(gText, 'g', 12);
    if (kind === 'single') P = f;
    else if (kind === 'product') {
      P = Pmul(f, g);
      rule = Padd(Pmul(Pderiv(f), g), Pmul(f, Pderiv(g)));
      naive = Pmul(Pderiv(f), Pderiv(g));
    } else {
      if (Pdeg(f) * Math.max(Pdeg(g), 0) > 12) {
        throw new Error('the composition has degree ' + Pdeg(f) * Pdeg(g) + '; this lab takes 12 at most');
      }
      var gm = MPfromPoly(g, HP_V, 't');
      P = MPtoPoly(MPsubst(MPfromPoly(f, HP_V, 't'), 't', gm), 't');
      rule = Pmul(MPtoPoly(MPsubst(MPfromPoly(Pderiv(f), HP_V, 't'), 't', gm), 't'), Pderiv(g));
    }
    if (Pdeg(P) > 12) throw new Error('the product has degree ' + Pdeg(P) + '; this lab takes 12 at most');
    var q = hpQuotient(MPfromPoly(P, HP_V, 't'));
    var at = null, aT = String(aText === undefined || aText === null ? '' : aText);
    if (/\S/.test(aT)) {
      var a = CK_need(aT, 'a');
      at = MPeval(q.Q, { t: a, h: R(1n, 8n) });
      q.a = a;
    }
    return { kind: kind, f: f, g: g, P: P, q: q, rule: rule, naive: naive, at: at,
             equal: rule === null ? null : Pzero(Psub(q.C, rule)) };
  }
"""


def _hpoly(cfg):
    mode = "hpoly"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        kind = str(p.get("kind", "single"))
        dc.check(KIT, mode, p, kind in ("single", "product", "compose"),
                 "kind must be single, product or compose, not %r" % kind)
        g = _pf(p, mode, "g", allow_none=True)
        dc.check(KIT, mode, p, (g is None) == (kind == "single"),
                 "g is required for product and compose and must be null for single")
        table[str(p["id"])] = {"kind": kind, "f": _pf(p, mode, "f"), "g": g or "",
                               "a": _pr(p, mode, "a", allow_none=True) or ""}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    glabel = {"single": "g(t)", "product": "Second factor g(t)", "compose": "Inner function g(t)"}[first["kind"]]
    tiles = [("Quotient", "hpQ"), ("Part free of h", "hpConst"), ("The rule gives", "hpRule"),
             ("Rule and quotient", "hpEqual"), ("Quotient at t = a, h = 1/8", "hpAt")]
    markup = (
        dc.toolbar("The quotient as a polynomial in h", "expand, cancel the h, then read off the rest", [])
        + dc.stage('<div class="table-wrap" id="hpTable"></div>')
        + dc.banner("hpStatus")
    )
    controls = (
        dc.select("hpPreset", "Polynomial", dc.options(found), pick["id"])
        + dc.text("hpF", "Outer function f(t)" if first["kind"] == "compose" else "f(t)", first["f"],
                  label_id="hpFLabel")
        + dc.text("hpG", glabel, first["g"], wrap_id="hpGWrap", label_id="hpGLabel").replace(
            'id="hpGWrap"', 'id="hpGWrap"' + _hide(first["kind"] != "single"))
        + dc.text("hpA", "a (may be empty)", first["a"])
        + dc.kpis(tiles)
        + dc.hint("Polynomials in t only: t^3 - t, 3t + 1, (t^2 + 1)^2.")
    )
    glue = dc.literal("HPP", table) + dc.literal("HP_KIND", first["kind"]) + r"""
  var HP_TILES = ['hpQ', 'hpConst', 'hpRule', 'hpEqual', 'hpAt'];
  var hpKind = HP_KIND;
  var hpPresetIn = DE_el('hpPreset'), hpFIn = DE_el('hpF'), hpGIn = DE_el('hpG'), hpAIn = DE_el('hpA');
  function hpLabels() {
    DE_set('hpFLabel', hpKind === 'compose' ? 'Outer function f(t)' : 'f(t)');
    DE_set('hpGLabel', hpKind === 'product' ? 'Second factor g(t)' : 'Inner function g(t)');
    var wrap = DE_el('hpGWrap');
    if (wrap) wrap.style.display = hpKind === 'single' ? 'none' : '';
  }
  function hpRender(r) {
    var q = r.q;
    DE_set('hpQ', MPtext(q.Q, { by: 'h' }));
    DE_set('hpConst', DE_ptext(q.C));
    if (r.kind === 'single') DE_set('hpRule', '—');
    else if (r.kind === 'product') DE_set('hpRule', 'f′g + fg′ = ' + DE_ptext(r.rule) + '; f′g′ = ' + DE_ptext(r.naive));
    else DE_set('hpRule', DE_ptext(r.rule));
    DE_set('hpEqual', r.equal === null ? '—' : (r.equal ? 'equal' : 'differ'));
    DE_set('hpAt', r.at === null ? '—' : DE_q(r.at));
    var name = r.kind === 'single' ? 'p(t)' : (r.kind === 'product' ? 'f(t)·g(t)' : 'f(g(t))');
    var rows = [[name, DE_ptext(r.P)], [name.replace(/t\)/g, 't + h)'), MPtext(q.shifted, { by: 'h' })],
                ['the difference', MPtext(q.diff, { by: 'h' })], ['divided by h', MPtext(q.Q, { by: 'h' })],
                ['the part free of h', DE_ptext(q.C)]];
    if (r.rule) rows.push([r.kind === 'product' ? 'f′g + fg′' : 'f′(g(t))·g′(t)', DE_ptext(r.rule)]);
    DE_html('hpTable', CK_table('every line is exact algebra; h is set to 0 only after the division', ['', 'polynomial'], rows, 4));
    var msg = '<strong>Exact.</strong> The difference of ' + DE_esc(name) + ' over [t, t + h] has h in every term, so it divides by h with nothing left over; '
      + 'the part free of h is ' + DE_esc(DE_ptext(q.C)) + '.';
    if (r.equal !== null) msg += r.equal ? ' The rule gives the same polynomial.' : ' The rule gives a different polynomial.';
    DE_ok('hpStatus', msg);
  }
  function redraw() {
    var r;
    try {
      r = hpCompute(hpKind, hpFIn.value, hpGIn.value, hpAIn.value);
    } catch (e) {
      DE_refuse('hpStatus', HP_TILES, ['hpTable'], DE_msg(e)); return;
    }
    hpRender(r);
  }
  hpPresetIn.addEventListener('change', function () {
    var p = HPP[hpPresetIn.value];
    if (p) { hpKind = p.kind; hpFIn.value = p.f; hpGIn.value = p.g; hpAIn.value = p.a; hpLabels(); }
    redraw();
  });
  [hpFIn, hpGIn, hpAIn].forEach(function (el) { el.addEventListener('input', redraw); });
  hpLabels();
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The quotient in h", subtitle="Difference quotients of polynomials, by algebra",
        markup=markup, controls=controls, script=dc.script("MPOLY", extra=CK_JS + HPOLY_JS + glue),
        panel_title="Choose the polynomial",
        panel_intro="For a polynomial, the difference quotient is a polynomial in h. Its part free of h "
                    "is found by algebra, with no limit taken.",
        select="hpPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# tangent (tg)
# ---------------------------------------------------------------------------

TANGENT_JS = r"""
  /* ---- calckit/tangent: the tangent line and its exact error ------------- */
  function tgCompute(fText, aText, hText) {
    var F = RFparse(fText, 't'), a = CK_need(aText, 'a'), h = CK_need(hText, 'h');
    var fa = RFeval(F, a);
    if (fa === null) throw new Error('f is undefined at t = ' + DE_q(a));
    var slope = RFeval(RFderiv(F), a);
    var approx = Radd(fa, Rmul(slope, h)), tru = RFeval(F, Radd(a, h));
    if (tru === null) throw new Error('f is undefined at t = ' + DE_q(Radd(a, h)));
    return { F: F, a: a, h: h, fa: fa, slope: slope, line: [Rsub(fa, Rmul(slope, a)), slope],
             approx: approx, tru: tru, error: Rsub(tru, approx) };
  }
"""


def _tangent(cfg):
    mode = "tangent"
    found = dc.presets(cfg, KIT, mode)
    table = {str(p["id"]): {"f": _pf(p, mode, "f"), "a": _pr(p, mode, "a"), "h": _pr(p, mode, "h")}
             for p in found}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("f(a)", "tgValue"), ("f′(a)", "tgSlope"), ("Tangent line", "tgLine"),
             ("Line at a + h", "tgApprox"), ("f(a + h)", "tgTrue"), ("Error, f minus line", "tgError")]
    markup = (
        dc.toolbar("The tangent line", "f(a) + f′(a)·(t − a), and how far f is from it at a + h",
                   [("cyan", "f"), ("green", "tangent line")])
        + dc.stage(dc.svg("tgPlot", "f with its tangent line"))
        + dc.banner("tgStatus")
    )
    controls = (
        dc.select("tgPreset", "Function and point", dc.options(found), pick["id"])
        + dc.text("tgF", "f(t)", first["f"])
        + dc.text("tgA", "a", first["a"])
        + dc.text("tgH", "h", first["h"])
        + dc.kpis(tiles)
        + dc.hint("A polynomial or a ratio of polynomials in t: t^2, t^3, 1/t.")
    )
    glue = dc.literal("TGP", table) + r"""
  var TG_TILES = ['tgValue', 'tgSlope', 'tgLine', 'tgApprox', 'tgTrue', 'tgError'];
  var tgPresetIn = DE_el('tgPreset'), tgFIn = DE_el('tgF'), tgAIn = DE_el('tgA'), tgHIn = DE_el('tgH');
  function tgRender(r) {
    DE_set('tgValue', DE_q(r.fa));
    DE_set('tgSlope', DE_q(r.slope));
    DE_set('tgLine', 'y = ' + DE_ptext(r.line));
    DE_set('tgApprox', DE_q(r.approx));
    DE_set('tgTrue', DE_q(r.tru));
    DE_set('tgError', DE_q(r.error));
    var a = Rnum(r.a), h = Rnum(r.h), span = Math.max(Math.abs(h), 1);
    var fn = function (x) { return RFevalFloat(r.F, x); };
    var lo = Math.min(a, a + h) - span, hi = Math.max(a, a + h) + span;
    var plot = CK_plot('tgPlot', CK_window([fn], lo, hi), 'f(t) = ' + RFtext(r.F, 't') + ' and its tangent at t = ' + DE_q(r.a));
    plot.curve(fn);
    CK_line(plot, a, Rnum(r.fa), Rnum(r.slope), 'plot-curve good');
    plot.point(a, Rnum(r.fa), 'plot-point', 'a').point(a + h, Rnum(r.tru), 'plot-point vertex')
      .point(a + h, Rnum(r.approx), 'plot-point root');
    DE_ok('tgStatus', '<strong>Exact.</strong> At a = ' + DE_esc(DE_q(r.a)) + ', f(a) = ' + DE_esc(DE_q(r.fa)) + ' and f′(a) = '
      + DE_esc(DE_q(r.slope)) + '. At a + h = ' + DE_esc(DE_q(Radd(r.a, r.h))) + ' the line gives ' + DE_esc(DE_q(r.approx))
      + ' and f gives ' + DE_esc(DE_q(r.tru)) + ': the error is ' + DE_esc(DE_q(r.error)) + '.');
  }
  function redraw() {
    var r;
    try {
      r = tgCompute(tgFIn.value, tgAIn.value, tgHIn.value);
    } catch (e) {
      DE_refuse('tgStatus', TG_TILES, ['tgPlot'], DE_msg(e)); return;
    }
    tgRender(r);
  }
  tgPresetIn.addEventListener('change', function () {
    var p = TGP[tgPresetIn.value];
    if (p) { tgFIn.value = p.f; tgAIn.value = p.a; tgHIn.value = p.h; }
    redraw();
  });
  [tgFIn, tgAIn, tgHIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The tangent line", subtitle="The linear approximation and its exact error",
        markup=markup, controls=controls, script=dc.script("RF", extra=CK_JS + TANGENT_JS + glue),
        panel_title="Choose the function and the point",
        panel_intro="The tangent line at a has slope f′(a). The error at a + h is f(a + h) minus the line, "
                    "computed as a fraction.",
        select="tgPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# derivative (dv)
# ---------------------------------------------------------------------------

DERIVATIVE_JS = r"""
  /* ---- calckit/derivative: p′, p″ and where they change sign -------------
     The sign of p′ between its zeros is tested at a rational point inside
     each interval, exactly. A zero of even multiplicity does not change the
     sign, and the tile says so rather than calling it a turn. */
  function dvZeros(d) {
    /* real zeros, ascending: {x: float, r: R | null, surd: text | null, mult} */
    var fac = Pfactor(d), out = [], i;
    for (i = 0; i < fac.factors.length; i += 1) {
      out.push({ x: Rnum(fac.factors[i].root), r: fac.factors[i].root, mult: fac.factors[i].mult });
    }
    var rest = fac.rest, exact = true;
    if (rest.length && Pdeg(rest) === 2) {
      var qr = quadroots(rest[2], rest[1], rest[0]);
      if (qr.kind === 'irrational') {
        var m = Rnum(qr.s.q) * Math.sqrt(Number(qr.s.k)), p = Rnum(qr.p);
        out.push({ x: p - m, r: null, mult: 1, text: dvSurd(qr.p, qr.s, -1) });
        out.push({ x: p + m, r: null, mult: 1, text: dvSurd(qr.p, qr.s, 1) });
      }
    } else if (rest.length && Pdeg(rest) > 2) {
      var k, prev = null, n = 4000, lo = -1000, hi = 1000;
      for (k = 0; k <= n; k += 1) {
        var x = lo + (hi - lo) * k / n, s = Math.sign(CK_pfloat(rest, x));
        if (prev !== null && s !== prev && s !== 0) exact = false;
        prev = s;
      }
    }
    out.sort(function (u, w) { return u.x - w.x; });
    return { list: out, exact: exact };
  }
  /* one of p ± q√k, as a single value: (1 + √5)/2 */
  function dvSurd(p, s, sign) {
    var D = p.d * s.q.d / bgcd(p.d, s.q.d), P = p.n * (D / p.d), Q = s.q.n * (D / s.q.d);
    var term = (Q === 1n ? '' : String(Q)) + '√' + s.k;
    var body = P === 0n ? (sign < 0 ? '−' : '') + term : DE_q(R(P)) + (sign < 0 ? ' − ' : ' + ') + term;
    return D === 1n ? body : (P === 0n ? body + '/' + D : '(' + body + ')/' + D);
  }
  function dvText(z) { return z.r !== null ? DE_q(z.r) : z.text; }
  /* a rational strictly between two real numbers (floats; −Infinity or
     Infinity for an open end), exact when both ends are rational */
  function dvBetween(lo, hi) {
    if (lo.r !== null && hi.r !== null) return Rdiv(Radd(lo.r, hi.r), R(2n));
    var a = lo.x, b = hi.x, d = 1;
    if (!isFinite(a) && !isFinite(b)) return R0;
    if (!isFinite(a)) return R(BigInt(Math.floor(b) - 1));
    if (!isFinite(b)) return R(BigInt(Math.ceil(a) + 1));
    while (d < 1e9) {
      var c = Math.floor(a * d) + 1;
      if (c / d < b) return R(BigInt(c), BigInt(d));
      d *= 2;
    }
    return R(BigInt(Math.round((a + b) / 2 * 1e6)), 1000000n);
  }
  function dvIntervals(d, zs) {
    if (Pzero(d)) return 'constant';
    var ends = [{ x: -Infinity, r: null }].concat(zs).concat([{ x: Infinity, r: null }]), parts = [], i;
    for (i = 0; i + 1 < ends.length; i += 1) {
      var sign = Rsign(Peval(d, dvBetween(ends[i], ends[i + 1])));
      var word = sign > 0 ? 'rising' : 'falling', where;
      if (zs.length === 0) where = 'for every t';
      else if (i === 0) where = 't < ' + dvText(ends[1]);
      else if (i === ends.length - 2) where = 't > ' + dvText(ends[i]);
      else where = dvText(ends[i]) + ' < t < ' + dvText(ends[i + 1]);
      parts.push(word + ' ' + where);
    }
    return parts.join('; ');
  }
  function dvCompute(fText) {
    var p = CK_poly(fText, 'p', 10), d1 = Pderiv(p), d2 = Pderiv(d1);
    var z1 = Pzero(d1) ? { list: [], exact: true } : dvZeros(d1);
    var z2 = Pzero(d2) ? { list: [], exact: true } : dvZeros(d2);
    var rational = [], i;
    for (i = 0; i < z1.list.length; i += 1) {
      if (z1.list[i].r !== null) rational.push(DE_q(z1.list[i].r) + (z1.list[i].mult % 2 === 0 ? ' (no sign change)' : ''));
    }
    var zeros = Pzero(d1) ? 'every t (p′ = 0)' : (rational.length ? rational.join(', ') : 'none rational');
    var inflect = [], other = false;
    for (i = 0; i < z2.list.length; i += 1) {
      if (z2.list[i].mult % 2 === 0) continue;
      if (z2.list[i].r !== null) inflect.push(DE_q(z2.list[i].r)); else other = true;
    }
    if (!z2.exact) other = true;
    return {
      p: p, d1: d1, d2: d2, z1: z1.list, z2: z2.list, zeros: zeros,
      intervals: z1.exact ? dvIntervals(d1, z1.list) : 'p′ has zeros this lab cannot place exactly',
      inflect: inflect.length ? 't = ' + inflect.join(', ') : (other ? 'none rational' : 'none')
    };
  }
"""


def _derivative(cfg):
    mode = "derivative"
    found = dc.presets(cfg, KIT, mode)
    order = dc.choice(cfg, "order", ["1", "2"], KIT, mode)
    table = {}
    for p in found:
        if "order" in p:
            dc.check(KIT, mode, p, str(p["order"]) == order,
                     "order %r disagrees with the lesson's order %s (dvOrder is redraw-only)" % (p["order"], order))
        win = p.get("window")
        if win is not None:
            dc.check(KIT, mode, p, isinstance(win, (list, tuple)) and len(win) == 2,
                     "window must be [tmin, tmax]")
            lo, hi = (dc.rational(w, KIT, mode, p, "window") for w in win)
            dc.check(KIT, mode, p, float(_frac(lo)) < float(_frac(hi)), "window must have tmin < tmax")
            win = [float(_frac(lo)), float(_frac(hi))]
        table[str(p["id"])] = {"f": _pf(p, mode, "f"), "window": win}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("p′(t)", "dvDeriv"), ("p″(t)", "dvSecond"), ("Zeros of p′", "dvZeros"),
             ("Where p rises and falls", "dvIntervals"), ("Inflection points", "dvInflect")]
    markup = (
        dc.toolbar("The derivative as a function", "the power rule, term by term, and the sign of p′",
                   [("cyan", "p"), ("purple", "p′"), ("muted", "p″ (second order)"), ("green", "zeros of p′")])
        + dc.stage(dc.svg("dvPlot", "p and its derivative"))
        + dc.banner("dvStatus")
    )
    controls = (
        dc.select("dvPreset", "Polynomial", dc.options(found), pick["id"])
        + dc.text("dvF", "p(t)", first["f"])
        + dc.select("dvOrder", "Derivatives shown", [("1", "p′"), ("2", "p′ and p″")], order)
        + dc.kpis(tiles)
        + dc.hint("A polynomial in t of degree 10 at most: t^3 - 6t^2 + 9t.")
    )
    glue = dc.literal("DVP", table) + r"""
  var DV_TILES = ['dvDeriv', 'dvSecond', 'dvZeros', 'dvIntervals', 'dvInflect'];
  var dvPresetIn = DE_el('dvPreset'), dvFIn = DE_el('dvF'), dvOrderIn = DE_el('dvOrder');
  var dvWindow = DVP[dvPresetIn.value] ? DVP[dvPresetIn.value].window : null;
  function dvRender(r) {
    var two = dvOrderIn.value === '2', i;
    DE_set('dvDeriv', DE_ptext(r.d1));
    DE_set('dvSecond', two ? DE_ptext(r.d2) : '—');
    DE_set('dvZeros', r.zeros);
    DE_set('dvIntervals', r.intervals);
    DE_set('dvInflect', two ? r.inflect : '—');
    var xs = [];
    for (i = 0; i < r.z1.length; i += 1) xs.push(r.z1[i].x);
    for (i = 0; i < r.z2.length; i += 1) xs.push(r.z2[i].x);
    var lo = -3, hi = 3;
    if (dvWindow) { lo = dvWindow[0]; hi = dvWindow[1]; }
    else if (xs.length) { lo = Math.min.apply(null, xs) - 2; hi = Math.max.apply(null, xs) + 2; }
    var fp = function (x) { return CK_pfloat(r.p, x); };
    var f1 = function (x) { return CK_pfloat(r.d1, x); };
    var f2 = function (x) { return CK_pfloat(r.d2, x); };
    var plot = CK_plot('dvPlot', CK_window([fp], lo, hi), 'p(t) = ' + DE_ptext(r.p) + ' and p′(t) = ' + DE_ptext(r.d1));
    plot.curve(fp).curve(f1, 'plot-curve alt');
    if (two) plot.curve(f2, 'plot-curve parent');
    for (i = 0; i < r.z1.length; i += 1) plot.point(r.z1[i].x, fp(r.z1[i].x), 'plot-point root');
    DE_ok('dvStatus', '<strong>Exact.</strong> p′(t) = ' + DE_esc(DE_ptext(r.d1)) + (two ? ' and p″(t) = ' + DE_esc(DE_ptext(r.d2)) : '')
      + ', by the power rule. The sign of p′ is tested at a rational point between consecutive zeros: '
      + DE_esc(r.intervals) + '.');
  }
  function redraw() {
    var r;
    try {
      r = dvCompute(dvFIn.value);
    } catch (e) {
      DE_refuse('dvStatus', DV_TILES, ['dvPlot'], DE_msg(e)); return;
    }
    dvRender(r);
  }
  dvPresetIn.addEventListener('change', function () {
    var p = DVP[dvPresetIn.value];
    if (p) { dvFIn.value = p.f; dvWindow = p.window; }
    redraw();
  });
  dvFIn.addEventListener('input', function () { dvWindow = null; redraw(); });
  dvOrderIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="The derivative", subtitle="p′ and p″ term by term, and their signs",
        markup=markup, controls=controls,
        script=dc.script("SURD", "MPOLY", extra=CK_JS + DERIVATIVE_JS + glue),
        panel_title="Choose the polynomial",
        panel_intro="The derivative of tⁿ is n·tⁿ⁻¹, applied term by term. Where p′ is positive the graph "
                    "of p rises; the lab tests the sign between every pair of zeros.",
        select="dvPreset", presets=found,
    )


def _frac(text_):
    from fractions import Fraction
    return Fraction(text_)


# ---------------------------------------------------------------------------
# transcendental (tq)
# ---------------------------------------------------------------------------

TRANSCENDENTAL_JS = r"""
  /* ---- calckit/transcendental: quotients that cannot be fractions --------
     2^h, sin h and cos h are irrational for rational h ≠ 0 (apart from the
     cases below), so these quotients are doubles, every one printed behind
     the approximately sign. The exact entries are printed exactly. */
  function tqLimitText(kind, b, a) {
    if (kind === 'sin') return Rzero(a) ? 'cos(0) = 1' : 'cos(' + DE_q(a) + ') ' + DE_dec(Math.cos(Rnum(a)));
    if (kind === 'cos') return Rzero(a) ? '−sin(0) = 0' : '−sin(' + DE_q(a) + ') ' + DE_dec(-Math.sin(Rnum(a)));
    if (b.e) {
      if (Rzero(a)) return 'ln e = 1';
      var ea = Requ(a, R1) ? 'e' : (Rint(a) && Rsign(a) > 0 ? 'e^' + a.n : 'e^(' + DE_q(a) + ')');
      return ea + ' ' + DE_dec(Math.exp(Rnum(a)));
    }
    if (Requ(b.r, R1)) return 'ln 1 = 0';
    var lnb = b.r.d === 1n ? 'ln ' + DE_q(b.r) : 'ln(' + DE_q(b.r) + ')', coef = '';
    if (!Rzero(a)) coef = Rint(a) ? DE_q(Rpow(b.r, Number(a.n))) + '·' : DE_q(b.r) + '^(' + DE_q(a) + ')·';
    return coef + lnb + ' ' + DE_dec(Math.pow(Rnum(b.r), Rnum(a)) * Math.log(Rnum(b.r)));
  }
  function tqCompute(kind, bText, aText, hText, halvings) {
    var a = CK_need(aText, 'a'), h = CK_need(hText, 'h'), b = null;
    if (Rsign(h) <= 0) throw new Error('h must be positive');
    if (kind === 'exp') {
      var bs = String(bText === undefined || bText === null ? '' : bText).replace(/^\s+|\s+$/g, '');
      if (bs === 'e') b = { e: true, v: Math.E };
      else {
        var br = DE_rat(bs);
        if (br === null) throw new Error('b must be e or a rational number such as 2 or 3/2');
        if (Rsign(br) <= 0) throw new Error('b must be positive: b^t is not defined for every t when b ≤ 0');
        b = { e: false, r: br, v: Rnum(br) };
      }
    }
    var f = kind === 'exp' ? function (x) { return Math.pow(b.v, x); } : (kind === 'sin' ? Math.sin : Math.cos);
    var A = Rnum(a), fa = f(A), rows = [], hk = h, k;
    var faExact = kind === 'exp' && !b.e && Rint(a) ? Rpow(b.r, Number(a.n)) : (kind === 'sin' && Rzero(a) ? R0 : (kind === 'cos' && Rzero(a) ? R1 : null));
    for (k = 0; k <= halvings; k += 1) {
      var H = Rnum(hk), exact = null;
      if (kind === 'exp' && !b.e && Requ(b.r, R1)) exact = R0;
      else if (kind === 'exp' && !b.e && Rint(a) && Requ(hk, R1)) exact = Rmul(Rsub(b.r, R1), Rpow(b.r, Number(a.n)));
      rows.push({ h: hk, value: (f(A + H) - fa) / H, exact: exact, fah: f(A + H) });
      hk = Rdiv(hk, R(2n));
    }
    var limit = kind === 'exp' ? fa * Math.log(b.v) : (kind === 'sin' ? Math.cos(A) : -Math.sin(A));
    var last = rows[rows.length - 1], ratio;
    if (faExact !== null && Rzero(faExact)) ratio = '—';
    else if (last.exact !== null && faExact !== null) ratio = DE_q(Rdiv(last.exact, faExact));
    else ratio = DE_dec(last.value / fa);
    return { kind: kind, b: b, a: a, h: h, rows: rows, fa: fa, faExact: faExact, limit: limit,
             limitText: tqLimitText(kind, b, a), ratio: ratio, f: f };
  }
  function tqShow(row) { return row.exact !== null ? DE_q(row.exact) : DE_dec(row.value); }
"""


def _transcendental(cfg):
    mode = "transcendental"
    found = dc.presets(cfg, KIT, mode)
    table = {}
    for p in found:
        kind = str(p.get("kind", "exp"))
        dc.check(KIT, mode, p, kind in ("exp", "sin", "cos"), "kind must be exp, sin or cos, not %r" % kind)
        b = p.get("b")
        if kind == "exp":
            b = "e" if str(b) == "e" else _pr(p, mode, "b")
            dc.check(KIT, mode, p, b == "e" or not b.startswith("-") and b != "0", "b must be positive or e")
        else:
            b = "" if b is None else ("e" if str(b) == "e" else _pr(p, mode, "b"))
        h = _pr(p, mode, "h")
        dc.check(KIT, mode, p, not h.startswith("-") and h != "0", "h must be positive")
        table[str(p["id"])] = {"kind": kind, "b": b, "a": _pr(p, mode, "a"), "h": h,
                               "halvings": _int(p, mode, "halvings", 0, 12)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("First quotient", "tqFirst"), ("Last quotient", "tqLast"),
             ("What they approach", "tqLimit"), ("Last quotient ÷ f(a)", "tqRatio")]
    markup = (
        dc.toolbar("Quotients that are not fractions", "rounded to six significant figures and labelled",
                   [("cyan", "f"), ("red", "secant at the smallest h"), ("green", "tangent")])
        + dc.stage(dc.svg("tqPlot", "f with a secant and the tangent"))
        + dc.wrap("tqTable")
        + dc.banner("tqStatus")
    )
    controls = (
        dc.select("tqPreset", "Function and point", dc.options(found), pick["id"])
        + dc.select("tqKind", "Function", [("exp", "b^t"), ("sin", "sin t"), ("cos", "cos t")], first["kind"])
        + dc.text("tqB", "b (for b^t; e is accepted)", first["b"])
        + dc.text("tqA", "a", first["a"])
        + dc.text("tqH", "first h", first["h"])
        + dc.range_("tqHalvings", "Halvings of h", 0, 12, first["halvings"])
        + dc.kpis(tiles)
    )
    glue = dc.literal("TQP", table) + r"""
  var TQ_TILES = ['tqFirst', 'tqLast', 'tqLimit', 'tqRatio'];
  var tqPresetIn = DE_el('tqPreset'), tqKindIn = DE_el('tqKind'), tqBIn = DE_el('tqB'), tqAIn = DE_el('tqA');
  var tqHIn = DE_el('tqH'), tqHalvIn = DE_el('tqHalvings');
  function tqName(r) {
    if (r.kind !== 'exp') return r.kind + ' t';
    return (r.b.e ? 'e' : DE_q(r.b.r)) + '^t';
  }
  function tqRender(r) {
    var last = r.rows[r.rows.length - 1], rows = [], i;
    DE_set('tqFirst', tqShow(r.rows[0]));
    DE_set('tqLast', tqShow(last));
    DE_set('tqLimit', r.limitText);
    DE_set('tqRatio', r.ratio);
    for (i = 0; i < r.rows.length; i += 1) rows.push([DE_q(r.rows[i].h), DE_dec(r.rows[i].fah), tqShow(r.rows[i])]);
    DE_html('tqTable', CK_table('f(t) = ' + tqName(r) + ' at a = ' + DE_q(r.a) + '; a value behind ≈ is rounded', ['h', 'f(a + h)', 'quotient'], rows, rows.length - 1));
    var a = Rnum(r.a), h0 = Rnum(r.h), span = Math.max(h0, 1);
    var plot = CK_plot('tqPlot', CK_window([r.f], a - span, a + h0 + span * 0.5), 'f(t) = ' + tqName(r) + ' near t = ' + DE_q(r.a));
    plot.curve(r.f);
    CK_line(plot, a, r.fa, last.value, 'plot-curve warn');
    CK_line(plot, a, r.fa, r.limit, 'plot-curve good');
    plot.point(a, r.fa, 'plot-point', 'a');
    DE_ok('tqStatus', '<strong>Rounded and labelled.</strong> The quotients of ' + DE_esc(tqName(r)) + ' at a = ' + DE_esc(DE_q(r.a))
      + ' are computed in floating point and printed to six significant figures; an entry with no ≈ is exact. They head for '
      + DE_esc(r.limitText) + '.');
  }
  function redraw() {
    var r;
    try {
      r = tqCompute(tqKindIn.value, tqBIn.value, tqAIn.value, tqHIn.value, CK_range('tqHalvings'));
    } catch (e) {
      DE_refuse('tqStatus', TQ_TILES, ['tqTable', 'tqPlot'], DE_msg(e)); return;
    }
    tqRender(r);
  }
  tqPresetIn.addEventListener('change', function () {
    var p = TQP[tqPresetIn.value];
    if (p) {
      tqKindIn.value = p.kind; tqBIn.value = p.b; tqAIn.value = p.a; tqHIn.value = p.h;
      tqHalvIn.value = String(p.halvings);
    }
    redraw();
  });
  [tqBIn, tqAIn, tqHIn, tqHalvIn].forEach(function (el) { el.addEventListener('input', redraw); });
  tqKindIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Rates of bᵗ, sin and cos", subtitle="Rounded quotients, labelled, and what they approach",
        markup=markup, controls=controls, script=dc.script(extra=CK_JS + TRANSCENDENTAL_JS + glue),
        panel_title="Choose the function and the point",
        panel_intro="These quotients have no fraction form, so each is rounded to six significant figures "
                    "and printed behind the approximately sign. The limit is stated, not computed.",
        select="tqPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# riemann (rs)
# ---------------------------------------------------------------------------

RIEMANN_JS = r"""
  /* ---- calckit/riemann: sums of rate times width, exactly -----------------
     Left, right, trapezoid and midpoint sums are sums of fractions. The
     exact total is F(b) − F(a) for a polynomial; for 1/t it is a logarithm,
     which no fraction equals, so it is rounded and says which log it is. */
  function rsPole(F, a, b) {
    var fac = Pfactor(F.den), i;
    for (i = 0; i < fac.factors.length; i += 1) {
      var r = fac.factors[i].root;
      if (Rcmp(r, a) >= 0 && Rcmp(r, b) <= 0) return DE_q(r);
    }
    if (fac.rest.length) {
      var lo = Rnum(a), hi = Rnum(b), k, prev = null;
      for (k = 0; k <= 2000; k += 1) {
        var v = RFevalFloat({ num: fac.rest, den: [R1] }, lo + (hi - lo) * k / 2000), s = v > 0 ? 1 : (v < 0 ? -1 : 0);
        if (s === 0 || (prev !== null && s !== prev)) return 'a point inside it';
        prev = s;
      }
    }
    return null;
  }
  function rsSum(F, a, b, n, rule) {
    var h = Rdiv(Rsub(b, a), R(BigInt(n))), L = R0, Rr = R0, M = R0, i;
    for (i = 0; i < n; i += 1) {
      var left = Radd(a, Rmul(h, R(BigInt(i))));
      L = Radd(L, RFeval(F, left));
      Rr = Radd(Rr, RFeval(F, Radd(left, h)));
      if (rule === 'mid') M = Radd(M, RFeval(F, Radd(left, Rdiv(h, R(2n)))));
    }
    L = Rmul(L, h); Rr = Rmul(Rr, h); M = Rmul(M, h);
    var S = rule === 'left' ? L : (rule === 'right' ? Rr : (rule === 'trap' ? Rdiv(Radd(L, Rr), R(2n)) : M));
    return { h: h, left: L, right: Rr, sum: S };
  }
  /* The exact integral: {exact: R} for a polynomial or a rational function
     whose partial fractions have no 1/(t − r) term; {approx: float, suffix}
     when a logarithm appears; null when the lab cannot say. */
  function rsExact(F, a, b) {
    if (RFispoly(F)) {
      var P = Pintegral(Pscale(F.num, Rinv(F.den[0])));
      return { exact: Rsub(Peval(P, b), Peval(P, a)) };
    }
    var parts = RFpartial(F);
    if (parts.refused || parts.quad) return null;
    var P2 = Pintegral(parts.poly), ex = Rsub(Peval(P2, b), Peval(P2, a)), logs = 0, hasLog = false, i;
    for (i = 0; i < parts.terms.length; i += 1) {
      var t = parts.terms[i], ua = Rsub(a, t.root), ub = Rsub(b, t.root);
      if (t.power === 1) {
        hasLog = true;
        logs += Rnum(t.coef) * (Math.log(Math.abs(Rnum(ub))) - Math.log(Math.abs(Rnum(ua))));
      } else {
        var k = t.power - 1, c = Rdiv(t.coef, R(BigInt(-k)));
        ex = Radd(ex, Rmul(c, Rsub(Rpow(ub, -k), Rpow(ua, -k))));
      }
    }
    if (!hasLog) return { exact: ex };
    var one = Pdeg(F.den) === 1 && Rzero(F.den[0]) && Pdeg(F.num) === 0 && Requ(F.num[0], R1);
    var named = one && Requ(a, R1) && Rint(b);
    return { approx: DE_float(ex) + logs, suffix: named ? ' (ln ' + b.n + ', rounded)' : ' (rounded)' };
  }
  function rsCompute(fText, aText, bText, n, rule) {
    var F = RFparse(fText, 't'), a = CK_need(aText, 'a'), b = CK_need(bText, 'b');
    if (Rcmp(b, a) <= 0) throw new Error('b must be greater than a');
    if (n < 1 || n > 64) throw new Error('n runs from 1 to 64');
    var pole = rsPole(F, a, b);
    if (pole !== null) throw new Error('f has a pole at ' + (pole.charAt(0) === 'a' ? pole : 't = ' + pole) + ', inside [a, b]; there is no total to sum');
    var s1 = rsSum(F, a, b, n, rule), s2 = rsSum(F, a, b, 2 * n, rule), ex = rsExact(F, a, b);
    var out = { F: F, a: a, b: b, n: n, rule: rule, s1: s1, s2: s2, ex: ex, gap: Rsub(s1.right, s1.left) };
    if (ex === null) { out.exText = '—'; out.errText = '—'; out.ratio = '—'; return out; }
    if (ex.exact) {
      var e1 = Rsub(s1.sum, ex.exact), e2 = Rsub(s2.sum, ex.exact);
      out.exText = DE_q(ex.exact); out.errText = DE_q(e1);
      out.ratio = (Rzero(e1) || Rzero(e2)) ? '—' : DE_q(Rdiv(e1, e2));
      out.err = e1;
    } else {
      var f1 = DE_float(s1.sum) - ex.approx, f2 = DE_float(s2.sum) - ex.approx;
      out.exText = DE_dec(ex.approx) + ex.suffix; out.errText = DE_dec(f1);
      out.ratio = (f1 === 0 || f2 === 0) ? '—' : DE_dec(f1 / f2);
    }
    return out;
  }
"""


def _riemann(cfg):
    mode = "riemann"
    found = dc.presets(cfg, KIT, mode)
    rule = dc.choice(cfg, "rule", ["left", "right", "trap", "mid"], KIT, mode)
    table = {}
    for p in found:
        a, b = _pr(p, mode, "a"), _pr(p, mode, "b")
        dc.check(KIT, mode, p, _frac(a) < _frac(b), "a must be less than b")
        table[str(p["id"])] = {"f": _pf(p, mode, "f"), "a": a, "b": b, "n": _int(p, mode, "n", 1, 64)}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    tiles = [("Sum", "rsSum"), ("Sum as a decimal", "rsSumDec"), ("Exact total", "rsExact"),
             ("Error, sum minus total", "rsError"), ("Right sum minus left sum", "rsGap"),
             ("Error at n ÷ error at 2n", "rsRatio")]
    markup = (
        dc.toolbar("Adding up a rate", "n pieces of width h = (b − a)/n, each rate times width",
                   [("cyan", "the rate f"), ("muted", "the pieces")])
        + dc.stage(dc.svg("rsPlot", "the rate and the pieces of the sum"))
        + dc.wrap("rsTable")
        + dc.banner("rsStatus")
    )
    controls = (
        dc.select("rsPreset", "Rate and interval", dc.options(found), pick["id"])
        + dc.text("rsF", "Rate f(t)", first["f"])
        + dc.text("rsA", "a", first["a"])
        + dc.text("rsB", "b", first["b"])
        + dc.range_("rsN", "Pieces n", 1, 64, first["n"])
        + dc.select("rsRule", "Rule", [("left", "left ends"), ("right", "right ends"),
                                       ("trap", "trapezoid"), ("mid", "midpoints")], rule)
        + dc.kpis(tiles)
        + dc.hint("A polynomial in t, or a ratio such as 1/t.")
    )
    glue = dc.literal("RSP", table) + r"""
  var RS_TILES = ['rsSum', 'rsSumDec', 'rsExact', 'rsError', 'rsGap', 'rsRatio'];
  var rsPresetIn = DE_el('rsPreset'), rsFIn = DE_el('rsF'), rsAIn = DE_el('rsA'), rsBIn = DE_el('rsB');
  var rsNIn = DE_el('rsN'), rsRuleIn = DE_el('rsRule');
  var RS_NAMES = { left: 'left', right: 'right', trap: 'trapezoid', mid: 'midpoint' };
  function rsRender(r) {
    var rows = [], i, h = r.s1.h;
    DE_set('rsSum', DE_q(r.s1.sum));
    DE_set('rsSumDec', DE_dec(DE_float(r.s1.sum)));
    DE_set('rsExact', r.exText);
    DE_set('rsError', r.errText);
    DE_set('rsGap', DE_q(r.gap));
    DE_set('rsRatio', r.ratio);
    for (i = 0; i < r.n; i += 1) {
      var left = Radd(r.a, Rmul(h, R(BigInt(i)))), right = Radd(left, h), mid = Radd(left, Rdiv(h, R(2n)));
      var height = r.rule === 'left' ? RFeval(r.F, left) : (r.rule === 'right' ? RFeval(r.F, right)
        : (r.rule === 'mid' ? RFeval(r.F, mid) : Rdiv(Radd(RFeval(r.F, left), RFeval(r.F, right)), R(2n))));
      rows.push([DE_q(left) + ' to ' + DE_q(right), DE_q(height), DE_q(Rmul(height, h))]);
    }
    DE_html('rsTable', CK_table(RS_NAMES[r.rule] + ' sum, n = ' + r.n + ', h = ' + DE_q(h) + ': the pieces add to ' + DE_q(r.s1.sum),
      ['piece', r.rule === 'trap' ? 'average of the ends' : 'rate used', 'rate times h'], rows, -1));
    var a = Rnum(r.a), b = Rnum(r.b), pad = 0.15 * (b - a), hf = Rnum(h);
    var fn = function (x) { return RFevalFloat(r.F, x); };
    var plot = CK_plot('rsPlot', CK_window([fn], a - pad, b + pad), 'the rate ' + RFtext(r.F, 't') + ' on [' + DE_q(r.a) + ', ' + DE_q(r.b) + '] in ' + r.n + ' pieces');
    var top = function (x) {
      var k = Math.min(r.n - 1, Math.floor((x - a) / hf)), l = a + k * hf;
      if (r.rule === 'left') return fn(l);
      if (r.rule === 'right') return fn(l + hf);
      if (r.rule === 'mid') return fn(l + hf / 2);
      return fn(l) + (fn(l + hf) - fn(l)) * (x - l) / hf;
    };
    plot.shade(function (x, y) {
      if (x < a || x > b) return false;
      var t = top(x);
      return (y >= 0 && y <= t) || (y <= 0 && y >= t);
    });
    for (i = 0; i < r.n; i += 1) {
      var l0 = a + i * hf, l1 = l0 + hf;
      plot.segment(l0, 0, l0, top(l0 + hf * 0.001), 'plot-aux');
      plot.segment(l1, 0, l1, top(l1 - hf * 0.001), 'plot-aux');
      plot.segment(l0, top(l0 + hf * 0.001), l1, top(l1 - hf * 0.001), 'plot-aux');
    }
    plot.curve(fn);
    DE_ok('rsStatus', '<strong>Exact.</strong> The ' + RS_NAMES[r.rule] + ' sum of ' + DE_esc(RFtext(r.F, 't')) + ' over ['
      + DE_esc(DE_q(r.a)) + ', ' + DE_esc(DE_q(r.b)) + '] in ' + r.n + ' pieces is ' + DE_esc(DE_q(r.s1.sum))
      + '; with ' + (2 * r.n) + ' pieces it is ' + DE_esc(DE_q(r.s2.sum)) + '. The total it estimates is ' + DE_esc(r.exText) + '.');
  }
  function redraw() {
    var r;
    try {
      r = rsCompute(rsFIn.value, rsAIn.value, rsBIn.value, CK_range('rsN'), rsRuleIn.value);
    } catch (e) {
      DE_refuse('rsStatus', RS_TILES, ['rsTable', 'rsPlot'], DE_msg(e)); return;
    }
    rsRender(r);
  }
  rsPresetIn.addEventListener('change', function () {
    var p = RSP[rsPresetIn.value];
    if (p) { rsFIn.value = p.f; rsAIn.value = p.a; rsBIn.value = p.b; rsNIn.value = String(p.n); }
    redraw();
  });
  [rsFIn, rsAIn, rsBIn, rsNIn].forEach(function (el) { el.addEventListener('input', redraw); });
  rsRuleIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Sums of a rate", subtitle="Left, right, trapezoid and midpoint sums as fractions",
        markup=markup, controls=controls, script=dc.script("MPOLY", "RF", extra=CK_JS + RIEMANN_JS + glue),
        panel_title="Choose the rate and the interval",
        panel_intro="Each piece contributes rate times width, and the sum is a fraction. The error is the sum "
                    "minus the exact total; the ratio compares it with the error at twice as many pieces.",
        select="rsPreset", presets=found,
    )


# ---------------------------------------------------------------------------
# antiderivative (ad)
# ---------------------------------------------------------------------------

ANTIDERIVATIVE_JS = r"""
  /* ---- calckit/antiderivative: the reverse power rule ---------------------
     F is found term by term, its constant from one value, and F(b) − F(a)
     exactly. Linearity and additivity are checked by computing both sides. */
  function adPair(text, what) {
    var s = String(text === undefined || text === null ? '' : text).replace(/^\s+|\s+$/g, '');
    if (!s.length) return null;
    var parts = s.split(/[\s,;]+/);
    if (parts.length !== 2) throw new Error(what + ' is two numbers separated by a space');
    return [CK_need(parts[0], what), CK_need(parts[1], what)];
  }
  function adSigned(x) { return Rsign(x) < 0 ? ' − ' + DE_q(Rabs(x)) : ' + ' + DE_q(x); }
  function adCompute(fText, useG, gText, coeffText, icText, aText, bText, splitText) {
    var f = CK_poly(fText, 'f', 12), F = Pintegral(f), out = { f: f, F: F, C: null, definite: null, linear: '—', split: '—' };
    var ic = adPair(icText, 'the initial value t0 y0');
    if (ic) { out.ic = ic; out.C = Rsub(ic[1], Peval(F, ic[0])); }
    var aS = String(aText || '').replace(/\s+/g, ''), bS = String(bText || '').replace(/\s+/g, '');
    if (aS.length !== bS.length && (!aS.length || !bS.length)) throw new Error('give both limits a and b, or neither');
    if (aS.length) {
      var a = CK_need(aS, 'a'), b = CK_need(bS, 'b');
      out.a = a; out.b = b;
      out.definite = Rsub(Peval(F, b), Peval(F, a));
      if (useG) {
        var g = CK_poly(gText, 'g', 12), cd = adPair(coeffText, 'the coefficients c d');
        if (!cd) throw new Error('the coefficients c d are missing');
        var G = Pintegral(g), whole = Pintegral(Padd(Pscale(f, cd[0]), Pscale(g, cd[1])));
        var lhs = Rsub(Peval(whole, b), Peval(whole, a));
        var p1 = Rmul(cd[0], out.definite), p2 = Rmul(cd[1], Rsub(Peval(G, b), Peval(G, a)));
        out.linear = (Requ(lhs, Radd(p1, p2)) ? 'equal: ' : 'differ: ') + DE_q(lhs) + ' = ' + DE_q(p1) + adSigned(p2);
        out.g = g;
      }
      var sS = String(splitText || '').replace(/\s+/g, '');
      if (sS.length) {
        var m = CK_need(sS, 'the split point');
        var i1 = Rsub(Peval(F, m), Peval(F, a)), i2 = Rsub(Peval(F, b), Peval(F, m));
        out.split = (Requ(out.definite, Radd(i1, i2)) ? 'equal: ' : 'differ: ') + DE_q(out.definite) + ' = ' + DE_q(i1) + adSigned(i2);
      }
    }
    return out;
  }
"""


def _antiderivative(cfg):
    mode = "antiderivative"
    found = dc.presets(cfg, KIT, mode)
    table = {}

    def pair(p, field):
        v = p.get(field)
        if v is None:
            return ""
        dc.check(KIT, mode, p, isinstance(v, (list, tuple)) and len(v) == 2, "%s must be a pair" % field)
        return " ".join(_pr({"id": p["id"], field: x}, mode, field) for x in v)

    for p in found:
        g = _pf(p, mode, "g", allow_none=True)
        coeffs = pair(p, "coeffs")
        dc.check(KIT, mode, p, (g is None) == (coeffs == ""), "g and coeffs come together")
        a, b = _pr(p, mode, "a", allow_none=True), _pr(p, mode, "b", allow_none=True)
        dc.check(KIT, mode, p, (a is None) == (b is None), "give both a and b, or neither")
        split = _pr(p, mode, "split", allow_none=True)
        dc.check(KIT, mode, p, split is None or a is not None, "a split needs a and b")
        dc.check(KIT, mode, p, g is None or a is not None, "linearity is checked on [a, b]: give a and b")
        if a is not None:
            dc.check(KIT, mode, p, _frac(a) < _frac(b), "a must be less than b")
        table[str(p["id"])] = {"f": _pf(p, mode, "f"), "g": g or "", "showG": g is not None, "coeffs": coeffs,
                               "ic": pair(p, "ic"), "a": a or "", "b": b or "", "split": split or ""}
    pick = dc.chosen(found, cfg, KIT, mode)
    first = table[str(pick["id"])]
    hidden = "" if first["showG"] else ' style="display:none;"'
    tiles = [("Antiderivative", "adF"), ("Constant from the value", "adC"), ("F(b) − F(a)", "adDefinite"),
             ("Linearity", "adLinear"), ("Adjacent intervals", "adSplit")]
    markup = (
        dc.toolbar("Antiderivatives", "the reverse power rule, and the constant one value fixes",
                   [("cyan", "the rate f"), ("green", "the member through the value"), ("muted", "the family F + C")])
        + dc.stage(dc.svg("adPlot", "the antiderivative family"))
        + dc.banner("adStatus")
    )
    controls = (
        dc.select("adPreset", "Rate", dc.options(found), pick["id"])
        + dc.text("adFIn", "f(t)", first["f"])
        + dc.text("adG", "g(t)", first["g"], wrap_id="adGWrap").replace('id="adGWrap"', 'id="adGWrap"' + hidden)
        + dc.text("adCoeffs", "Coefficients c d, for c·f + d·g", first["coeffs"], wrap_id="adCWrap").replace(
            'id="adCWrap"', 'id="adCWrap"' + hidden)
        + dc.text("adIC", "Initial value t0 y0 (may be empty)", first["ic"])
        + dc.text("adA", "a (may be empty)", first["a"])
        + dc.text("adB", "b (may be empty)", first["b"])
        + dc.text("adSplitAt", "Split point (may be empty)", first["split"])
        + dc.kpis(tiles)
        + dc.hint("Polynomials in t: 3t^2 - 4t + 1. Two numbers are typed with a space between them.")
    )
    glue = dc.literal("ADP", table) + dc.literal("AD_SHOWG", first["showG"]) + r"""
  var AD_TILES = ['adF', 'adC', 'adDefinite', 'adLinear', 'adSplit'];
  var adShowG = AD_SHOWG;
  var adPresetIn = DE_el('adPreset'), adFIn = DE_el('adFIn'), adGIn = DE_el('adG'), adCIn = DE_el('adCoeffs');
  var adICIn = DE_el('adIC'), adAIn = DE_el('adA'), adBIn = DE_el('adB'), adSIn = DE_el('adSplitAt');
  function adWraps() {
    var show = adShowG ? '' : 'none';
    if (DE_el('adGWrap')) DE_el('adGWrap').style.display = show;
    if (DE_el('adCWrap')) DE_el('adCWrap').style.display = show;
  }
  function adRender(r) {
    var ftext = DE_ptext(r.F);
    DE_set('adF', ftext === '0' ? 'C' : ftext + ' + C');
    DE_set('adC', r.C === null ? '—' : DE_q(r.C));
    DE_set('adDefinite', r.definite === null ? '—' : DE_q(r.definite));
    DE_set('adLinear', r.linear);
    DE_set('adSplit', r.split);
    var fF = function (x) { return CK_pfloat(r.F, x); };
    var ff = function (x) { return CK_pfloat(r.f, x); };
    var lo = -2, hi = 3, j, plot;
    if (r.ic) {
      var t0 = Rnum(r.ic[0]), c = Rnum(r.C);
      lo = t0 - 2.5; hi = t0 + 2.5;
      var member = function (x) { return fF(x) + c; };
      plot = CK_plot('adPlot', CK_window([member], lo, hi), 'the family F + C, and the member through (' + DE_q(r.ic[0]) + ', ' + DE_q(r.ic[1]) + ')');
      for (j = -2; j <= 2; j += 1) {
        if (j === 0) continue;
        plot.curve((function (k) { return function (x) { return member(x) + k; }; })(j), 'plot-curve parent');
      }
      plot.curve(member, 'plot-curve good');
      plot.point(t0, Rnum(r.ic[1]), 'plot-point', '(t0, y0)');
    } else if (r.a) {
      var a = Rnum(r.a), b = Rnum(r.b), pad = 0.25 * (b - a);
      plot = CK_plot('adPlot', CK_window([ff], a - pad, b + pad), 'the rate f on [' + DE_q(r.a) + ', ' + DE_q(r.b) + ']');
      plot.shade(function (x, y) { if (x < a || x > b) return false; var v = ff(x); return (y >= 0 && y <= v) || (y <= 0 && y >= v); });
      plot.curve(ff);
    } else {
      plot = CK_plot('adPlot', CK_window([ff, fF], lo, hi), 'the rate f and the antiderivative F');
      plot.curve(ff).curve(fF, 'plot-curve good');
    }
    var msg = '<strong>Exact.</strong> F(t) = ' + DE_esc(ftext) + ' has F′ = f, term by term.';
    if (r.C !== null) msg += ' The value y(' + DE_esc(DE_q(r.ic[0])) + ') = ' + DE_esc(DE_q(r.ic[1])) + ' fixes C = ' + DE_esc(DE_q(r.C)) + '.';
    if (r.definite !== null) msg += ' F(b) − F(a) = ' + DE_esc(DE_q(r.definite)) + ', whatever C is.';
    DE_ok('adStatus', msg);
  }
  function redraw() {
    var r;
    try {
      r = adCompute(adFIn.value, adShowG, adGIn.value, adCIn.value, adICIn.value, adAIn.value, adBIn.value, adSIn.value);
    } catch (e) {
      DE_refuse('adStatus', AD_TILES, ['adPlot'], DE_msg(e)); return;
    }
    adRender(r);
  }
  adPresetIn.addEventListener('change', function () {
    var p = ADP[adPresetIn.value];
    if (p) {
      adFIn.value = p.f; adGIn.value = p.g; adCIn.value = p.coeffs; adICIn.value = p.ic;
      adAIn.value = p.a; adBIn.value = p.b; adSIn.value = p.split; adShowG = p.showG; adWraps();
    }
    redraw();
  });
  [adFIn, adGIn, adCIn, adICIn, adAIn, adBIn, adSIn].forEach(function (el) { el.addEventListener('input', redraw); });
  adWraps();
  redraw();
  window.redrawLab = redraw;
"""
    return dc.lab(
        cfg, title="Antiderivatives", subtitle="F, its constant, and F(b) − F(a)",
        markup=markup, controls=controls, script=dc.script("MPOLY", extra=CK_JS + ANTIDERIVATIVE_JS + glue),
        panel_title="Choose the rate",
        panel_intro="An antiderivative reverses the power rule term by term. One value fixes the constant; "
                    "a difference F(b) − F(a) does not depend on it.",
        select="adPreset", presets=found,
    )


# ---------------------------------------------------------------------------

_MODES = {
    "quotient": _quotient,
    "hpoly": _hpoly,
    "tangent": _tangent,
    "derivative": _derivative,
    "transcendental": _transcendental,
    "riemann": _riemann,
    "antiderivative": _antiderivative,
}

MODES = tuple(_MODES)

# Each mode's own pure-function block, for scripts/mathcheck.js and the tests.
MODE_JS = {
    "quotient": QUOTIENT_JS,
    "hpoly": HPOLY_JS,
    "tangent": TANGENT_JS,
    "derivative": DERIVATIVE_JS,
    "transcendental": TRANSCENDENTAL_JS,
    "riemann": RIEMANN_JS,
    "antiderivative": ANTIDERIVATIVE_JS,
}


def calckit_lab(cfg):
    """The calculus kit. `cfg["mode"]` chooses the mode; an unknown one raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError("calckit_lab: unknown mode %r; the seven modes are %s" % (mode, ", ".join(MODES)))
    return _MODES[mode](cfg or {})


__all__ = ["calckit_lab", "MODES", "MODE_JS", "CK_JS"]
