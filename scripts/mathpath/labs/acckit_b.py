"""acckit_b -- family B of the Accelerate kit: constructs, statistics, groups and samples.

Specified in docs/accelerate/PLAN.md section D (family B); the seam with
family A (acckit.py: the entry point and modes delivery, flow, branches,
release, change, work) is docs/accelerate/kit-contract.md; the report an
author configures a lesson from is the "Family B" section of
docs/accelerate/kit-report.md. Six modes:

  likert      (alk)  score, westrum, alpha             Chapters 3, 11, 13, Appendix C
  stats       (ast)  describe, pearson, spurious, confound   Chapter 12
  validity    (avd)  matrix, ave                        Chapter 13, Appendix C
  groups      (agr)  likely, enps, bias                 Chapters 2, 10, 14, 15
  sample      (asn)  snowball                           Chapter 15
  capability  (acp)  profile                            Chapter 1, Appendix A

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"acckit (Accelerate), family B"), and one block per view. A page ships the
base block and its own view's block only.

THE SAMPLES ARE THE LESSON'S. No item, answer, team or capability is a
constant here: every one arrives in a preset. Nothing typed is evaluated as
script. Nothing here grades a team: every tile is a figure computed from the
sample stated, and every status line says so (aktStatus).

EXACTNESS. Every figure is an exact BigInt rational, a count or a list. A
square root (r, a standard deviation, the root of an AVE) is printed from
the exact rational under it by aktSqrtFixed (an integer square root, half
up), and a threshold on a root is tested on the squares (sqrt(AVE) > |r| as
AVE > r^2). No p-value is ever computed.

IDS. Every JS function and variable and every element id begins with its
mode's prefix (alk, ast, avd, agr, asn, acp); no name here begins akt/AKT_.
"""

import re
from fractions import Fraction

from . import eakit_core as ea
from .acckit import mode_lab, arec, alist

_N = ea.NAME
_MINUS = "−"

# ---------------------------------------------------------------------------
# likert (alk): construct scores, Westrum culture, Cronbach's alpha
# ---------------------------------------------------------------------------

ALK_JS = r"""
  var ALK_VIEW = {};
  function alkCompute(view, inst, opts) { return eaRun(ALK_VIEW[view], inst, opts); }
  /* An exact decimal with as few places as it needs (at most 6), else the
     fraction and 3 places. */
  function alkShow(r) {
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    if (eaBig(r)) return eaSci(r);
    return eaFrac(r) + ' ≈ ' + eaFixed(r, 3);
  }
  function alkSigned(r) { return (r.n > 0n ? '+' : '') + alkShow(r); }
  function alkMean(v) { return Rdiv(eaSum(v), R(BigInt(v.length))); }
  /* Each answer record gives one whole answer per item, 1 to points. */
  function alkAnswers(list, k, points, what, itemNames) {
    var seen = {};
    list.forEach(function (a, i) {
      if (a.rest.length !== k) eaRefuse(what + ', record ' + (i + 1) + ' (' + a.respondent + ') gives ' + eaPlural(a.rest.length, 'answer', 'answers')
        + '; there ' + (k === 1 ? 'is 1 item' : 'are ' + k + ' items') + ' (' + itemNames.join(', ') + '), so each record needs ' + k);
      a.rest.forEach(function (x, j) {
        if (Rcmp(x, R1) < 0 || Rcmp(x, R(BigInt(points))) > 0) eaRefuse(what + ', record ' + (i + 1) + ' (' + a.respondent + '): answer ' + (j + 1) + ' is '
          + eaInt(x.n) + '; on a ' + points + '-point scale an answer is 1 to ' + points);
      });
      if (seen[a.respondent]) eaRefuse(what + ' names ' + a.respondent + ' twice');
      seen[a.respondent] = true;
    });
  }
  /* The scored answer: points + 1 − answer for a reverse-coded item. */
  function alkScore(x, item, points, reverse) { return reverse && item.reverse === 'yes' ? Rsub(R(BigInt(points + 1)), x) : x; }
  /* Constructs in the order of their first item. */
  function alkConstructs(items) {
    var list = [], of = {};
    items.forEach(function (it, j) { if (!of[it.construct]) { of[it.construct] = []; list.push(it.construct); } of[it.construct].push(j); });
    return { list: list, of: of };
  }
  /* Each respondent's mean on a construct (its items' scored answers). */
  function alkMeans(answers, items, cons, points, reverse) {
    return answers.map(function (a) {
      var m = {};
      cons.list.forEach(function (c) { m[c] = alkMean(cons.of[c].map(function (j) { return alkScore(a.rest[j], items[j], points, reverse); })); });
      return m;
    });
  }
  function alkPoints(inst) { return Number(inst.points); }
  function alkLineOk(r, points, what) {
    if (Rcmp(r, R1) < 0 || Rcmp(r, R(BigInt(points))) > 0) eaRefuse(what + ' is ' + alkShow(r) + '; on a ' + points + '-point scale it lies from 1 to ' + points);
  }
"""

ALK_VIEW_JS = {}

ALK_VIEW_JS["score"] = r"""
  ALK_VIEW.score = function (inst) {
    var points = alkPoints(inst), items = inst.items, A = inst.answers, cons = alkConstructs(items), line = inst.line;
    alkAnswers(A, items.length, points, 'Answers', items.map(function (it) { return it.item; }));
    alkLineOk(line, points, 'The line');
    var means = alkMeans(A, items, cons, points, true), raw = alkMeans(A, items, cons, points, false);
    var cmean = {}, craw = {}, side = [];
    cons.list.forEach(function (c) {
      cmean[c] = alkMean(means.map(function (m) { return m[c]; }));
      craw[c] = alkMean(raw.map(function (m) { return m[c]; }));
      var above = 0, at = 0, below = 0;
      means.forEach(function (m) { var k = Rcmp(m[c], line); if (k > 0) above += 1; else if (k < 0) below += 1; else at += 1; });
      side.push(c + ': ' + above + ' above, ' + at + ' at, ' + below + ' below');
    });
    var itemMeans = items.map(function (it, j) { return alkMean(A.map(function (a) { return alkScore(a.rest[j], it, points, true); })); });
    var rev = items.filter(function (it) { return it.reverse === 'yes'; }).map(function (it) { return it.item; });
    var moved = cons.list.filter(function (c) { return !Requ(cmean[c], craw[c]); });
    var rows = A.map(function (a, i) { return [a.respondent].concat(cons.list.map(function (c) { return alkShow(means[i][c]); })); });
    return {
      tiles: { alkN: eaInt(A.length), alkConstructs: cons.list.map(function (c) { return c + ' ' + alkShow(cmean[c]); }).join('; '),
        alkItems: items.map(function (it, j) { return it.item + ' ' + alkShow(itemMeans[j]); }).join('; '),
        alkLine: side.join('; '), alkReversed: eaCount(rev),
        alkUnreversed: cons.list.map(function (c) { return c + ' ' + alkShow(craw[c]); }).join('; ') },
      status: aktStatus(eaPlural(A.length, 'respondent', 'respondents') + ' on ' + eaPlural(items.length, 'item', 'items') + ' in '
        + eaPlural(cons.list.length, 'construct', 'constructs') + '; ' + eaPlural(rev.length, 'item is', 'items are') + ' reverse-coded (scored ' + (points + 1) + ' − the answer). '
        + (moved.length ? 'Left unreversed, ' + eaPlural(moved.length, 'construct mean', 'construct means') + ' would be wrong: ' + moved.join(', ') + '.' : 'Reversing changes no construct mean here.')),
      table: { caption: 'Each respondent\'s mean on each construct, reverse-coded items reversed',
        head: ['respondent'].concat(cons.list), rows: rows }
    };
  };
"""

ALK_VIEW_JS["westrum"] = r"""
  /* Band by the lesson's cuts: below the first, pathological; from the first
     up to the second, bureaucratic; from the second up, generative. */
  function alkBand(m, cuts) { return Rcmp(m, cuts[0]) < 0 ? 'pathological' : Rcmp(m, cuts[1]) < 0 ? 'bureaucratic' : 'generative'; }
  var ALK_BANDS = ['pathological', 'bureaucratic', 'generative'];
  ALK_VIEW.westrum = function (inst) {
    var points = alkPoints(inst), items = inst.items, cons = alkConstructs(items), cuts = inst.cuts, A = inst.answers, B = inst.answers2;
    if (cons.list.length !== 1) eaRefuse('Items: the westrum view scores one construct, and the items name ' + cons.list.length + ': ' + cons.list.join(', '));
    if (cuts.length !== 2) eaRefuse('The cuts are two values on the scale, low then high; there ' + (cuts.length === 1 ? 'is 1' : 'are ' + cuts.length));
    alkLineOk(cuts[0], points, 'The first cut'); alkLineOk(cuts[1], points, 'The second cut');
    if (Rcmp(cuts[0], cuts[1]) >= 0) eaRefuse('The cuts go low then high, and ' + alkShow(cuts[0]) + ' is not below ' + alkShow(cuts[1]));
    var names = items.map(function (it) { return it.item; }), c = cons.list[0];
    alkAnswers(A, items.length, points, 'Answers', names);
    alkAnswers(B, items.length, points, 'Second answers', names);
    function survey(L) {
      var m = alkMeans(L, items, cons, points, true).map(function (x) { return x[c]; }), count = { pathological: 0, bureaucratic: 0, generative: 0 }, of = {};
      m.forEach(function (x, i) { count[alkBand(x, cuts)] += 1; of[L[i].respondent] = x; });
      var team = L.length ? alkMean(m) : null;
      return { m: m, of: of, team: team, count: count,
        bands: ALK_BANDS.map(function (b) { return b + ' ' + count[b]; }).join(', '),
        teamText: L.length ? alkShow(team) + ', ' + alkBand(team, cuts) : 'no second survey given' };
    }
    var one = survey(A), two = survey(B), both = [], only = [];
    A.forEach(function (a) { if (two.of[a.respondent] !== undefined) both.push(a.respondent); else only.push(a.respondent); });
    var rows = A.map(function (a, i) {
      var x = one.m[i], y = two.of[a.respondent];
      return [a.respondent, alkShow(x), alkBand(x, cuts), y === undefined ? '' : alkShow(y), y === undefined ? '' : alkBand(y, cuts), y === undefined ? '' : alkSigned(Rsub(y, x))];
    });
    B.forEach(function (b) { if (one.of[b.respondent] === undefined) { var y = two.of[b.respondent]; rows.push([b.respondent, '', '', alkShow(y), alkBand(y, cuts), '']); } });
    var change = B.length ? alkSigned(Rsub(two.team, one.team)) + ' (' + alkBand(one.team, cuts) + ' to ' + alkBand(two.team, cuts) + ')' : 'no second survey given';
    var per = !B.length ? 'no second survey given' : both.length ? eaInt(both.length) + ': ' + both.map(function (r) { return r + ' ' + alkSigned(Rsub(two.of[r], one.of[r])); }).join(', ') : '0: no respondent answered both';
    return {
      tiles: { alkN: eaInt(A.length), alkTeam: one.teamText, alkBands: one.bands, alkTeam2: two.teamText,
        alkBands2: B.length ? two.bands : 'no second survey given', alkChange: change, alkEach: per },
      status: aktStatus('Bands by the cuts the lesson states, ' + alkShow(cuts[0]) + ' and ' + alkShow(cuts[1]) + ' (the book gives none): the team mean is '
        + one.teamText + (B.length ? ', and ' + two.teamText + ' in the second survey' : '') + '. A band names a mean; it does not grade the team.'),
      table: { caption: 'Each respondent: mean and band, and in the second survey',
        head: ['respondent', 'mean', 'band', 'second mean', 'second band', 'change'], rows: rows }
    };
  };
"""

ALK_VIEW_JS["alpha"] = r"""
  /* Population variance: the mean squared deviation from the mean. */
  function alkVar(v) { var m = alkMean(v), s = R0; v.forEach(function (x) { var d = Rsub(x, m); s = Radd(s, Rmul(d, d)); }); return Rdiv(s, R(BigInt(v.length))); }
  /* alpha = k/(k − 1)·(1 − Σ item variances / total variance), or null when
     the total varies by nothing. */
  function alkAlpha(A, cols) {
    var k = cols.length, vars = cols.map(function (j) { return alkVar(A.map(function (a) { return a.rest[j]; })); });
    var tot = alkVar(A.map(function (a) { return eaSum(cols.map(function (j) { return a.rest[j]; })); }));
    if (Rzero(tot)) return { vars: vars, tot: tot, alpha: null };
    var kk = R(BigInt(k), BigInt(k - 1));
    return { vars: vars, tot: tot, alpha: Rmul(kk, Rsub(R1, Rdiv(eaSum(vars), tot))) };
  }
  function alkThree(r) {
    if (Rint(r)) return eaInt(r.n);
    if (eaBig(r)) return eaSci(r);
    return eaFrac(r) + (eaExactAt(r, 3) ? ' = ' : ' ≈ ') + eaFixed(r, 3);
  }
  ALK_VIEW.alpha = function (inst, opts) {
    var points = alkPoints(inst), names = inst.items, A = inst.answers, k = names.length;
    alkAnswers(A, k, points, 'Answers', names);
    var cols = names.map(function (_n, j) { return j; }), all = alkAlpha(A, cols), min = Rparse(opts.alpha_min || '0.7');
    if (all.alpha === null) eaRefuse('Answers: every respondent\'s total is the same, so the total varies by nothing and alpha is not defined');
    var del = names.map(function (nm, j) {
      if (k < 3) return nm + ' not computed (one item would be left)';
      var rest = alkAlpha(A, cols.filter(function (c) { return c !== j; }));
      return nm + ' ' + (rest.alpha === null ? 'not defined (the rest total the same)' : eaFixed(rest.alpha, 3));
    });
    var meets = Rcmp(all.alpha, min) >= 0;
    return {
      tiles: { alkK: eaInt(k), alkN: eaInt(A.length),
        alkVars: names.map(function (nm, j) { return nm + ' ' + alkShow(all.vars[j]); }).join('; '),
        alkTotal: alkShow(all.tot), alkAlpha: alkThree(all.alpha), alkDeleted: del.join('; '),
        alkMeets: (meets ? 'yes: ' : 'no: ') + eaFixed(all.alpha, 3) + (meets ? ' ≥ ' : ' < ') + alkShow(min) },
      status: aktStatus('Alpha over ' + eaPlural(k, 'item', 'items') + ' and ' + eaPlural(A.length, 'respondent', 'respondents') + ' is ' + eaFixed(all.alpha, 3)
        + (meets ? ', at or above ' : ', below ') + alkShow(min) + '. It says how far the items move together in this sample; it does not say they measure what their names say.'),
      table: { caption: 'Each respondent\'s answers and total', head: ['respondent'].concat(names).concat(['total']),
        rows: A.map(function (a) { return [a.respondent].concat(a.rest.map(function (x) { return eaInt(x.n); })).concat([eaInt(eaSum(a.rest).n)]); }) }
    };
  };
"""

# ---------------------------------------------------------------------------
# stats (ast): describe, Pearson's r, spurious trends, a confounder
# ---------------------------------------------------------------------------

AST_JS = r"""
  var AST_VIEW = {};
  function astCompute(view, inst, opts) { return eaRun(AST_VIEW[view], inst, opts); }
  /* An exact decimal with as few places as it needs (at most 6), else the
     fraction and 3 places. */
  function astShow(r) {
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    if (eaBig(r)) return eaSci(r);
    return eaFrac(r) + ' ≈ ' + eaFixed(r, 3);
  }
  function astSigned(r) { return (r.n > 0n ? '+' : '') + astShow(r); }
  /* The signed root of q (sign -1, 0 or 1): exact when sqrt(q) is a decimal
     of at most 3 places, else "≈" and 3 places by the exact method. */
  function astRootText(q, sign) {
    var e = aktSqrtExact(q);
    if (e !== null && eaExactAt(e, 3)) return astShow(sign < 0 ? Rneg(e) : e);
    return '≈ ' + aktRootSigned(sign, q, 3);
  }
  function astMean(v) { return aktMean(v); }
  /* Sums of squares and of cross-products about the means. */
  function astSums(xs, ys) {
    var mx = astMean(xs), my = astMean(ys), sxx = R0, syy = R0, sxy = R0;
    xs.forEach(function (x, i) {
      var dx = Rsub(x, mx), dy = Rsub(ys[i], my);
      sxx = Radd(sxx, Rmul(dx, dx)); syy = Radd(syy, Rmul(dy, dy)); sxy = Radd(sxy, Rmul(dx, dy));
    });
    return { n: xs.length, mx: mx, my: my, sxx: sxx, syy: syy, sxy: sxy };
  }
  /* r from sums: {ok, r2, sign, text} or {ok: false, why}. */
  function astR(s) {
    if (Rzero(s.sxx)) return { ok: false, why: 'not defined: every x is the same' };
    if (Rzero(s.syy)) return { ok: false, why: 'not defined: every y is the same' };
    var r2 = Rdiv(Rmul(s.sxy, s.sxy), Rmul(s.sxx, s.syy)), sign = Rsign(s.sxy);
    return { ok: true, r2: r2, sign: sign, text: astRootText(r2, sign) };
  }
  function astRt(c) { return c.ok ? c.text : c.why; }
  function astSay(c) { return astRt(c).replace(/^≈ /, 'about '); }
  /* How a second r compares with a first, on the squares, exactly. */
  function astVersus(a, b) {
    if (!a.ok || !b.ok) return 'cannot be compared: one r is not defined';
    var c = Rcmp(b.r2, a.r2), size = c < 0 ? 'smaller in size' : c > 0 ? 'larger in size' : 'the same size';
    var sign = a.sign === b.sign ? 'the same sign' : (a.sign === 0 || b.sign === 0) ? 'no sign to compare, since one r is 0' : 'the opposite sign';
    return size + ', ' + sign;
  }
"""

AST_VIEW_JS = {}

AST_VIEW_JS["describe"] = r"""
  AST_VIEW.describe = function (inst) {
    var v = inst.values.map(function (x) { return x.value === undefined ? x : x.value; }), n = v.length;
    var sorted = v.slice().sort(Rcmp), mean = astMean(v), median = aktMedian(v);
    var freq = {}, order = [];
    sorted.forEach(function (x) { var k = Rtext(x); if (!freq[k]) { freq[k] = { x: x, n: 0 }; order.push(k); } freq[k].n += 1; });
    var top = 0;
    order.forEach(function (k) { if (freq[k].n > top) top = freq[k].n; });
    var modes = order.filter(function (k) { return freq[k].n === top; });
    var modeText = modes.length === order.length
      ? (order.length === 1 ? astShow(freq[modes[0]].x) + ' (every value, ' + eaPlural(top, 'time', 'times') + ')'
        : 'none: every value occurs ' + (top === 1 ? 'once' : eaPlural(top, 'time', 'times')))
      : modes.map(function (k) { return astShow(freq[k].x); }).join(', ') + ' (' + eaPlural(top, 'time', 'times') + (modes.length > 1 ? ' each)' : ')');
    var ss = R0;
    v.forEach(function (x) { var d = Rsub(x, mean); ss = Radd(ss, Rmul(d, d)); });
    var pv = Rdiv(ss, R(BigInt(n))), sv = Rdiv(ss, R(BigInt(n - 1)));
    var lo = sorted[0], hi = sorted[n - 1];
    return {
      tiles: { astN: eaInt(n), astMean: astShow(mean), astMedian: astShow(median), astMode: modeText,
        astMin: astShow(lo), astMax: astShow(hi), astRange: astShow(Rsub(hi, lo)),
        astPopSd: astRootText(pv, 1) + ' (variance ' + astShow(pv) + ')',
        astSampleSd: astRootText(sv, 1) + ' (variance ' + astShow(sv) + ')' },
      status: aktStatus(eaPlural(n, 'value', 'values') + ': mean ' + astShow(mean) + ', median ' + astShow(median)
        + '; the sample standard deviation divides by n − 1 = ' + eaInt(n - 1) + ', the population one by n = ' + eaInt(n) + '.'),
      table: { caption: 'The values in order, with their distance from the mean',
        head: ['rank', 'value', 'value − mean', 'squared'],
        rows: sorted.map(function (x, i) { var d = Rsub(x, mean); return [eaInt(i + 1), astShow(x), astShow(d), astShow(Rmul(d, d))]; }) }
    };
  };
"""

AST_VIEW_JS["pearson"] = r"""
  AST_VIEW.pearson = function (inst, opts) {
    var P = inst.pairs, xs = P.map(function (p) { return p.x; }), ys = P.map(function (p) { return p.y; });
    var s = astSums(xs, ys), c = astR(s);
    if (!c.ok) eaRefuse('Pairs: r is ' + c.why + ', so there is no correlation to compute');
    var b = Rdiv(s.sxy, s.sxx), a = Rsub(s.my, Rmul(b, s.mx));
    var cuts = (opts.strength || ['0.3', '0.7']).map(Rparse), r2 = c.r2;
    var strength = Rcmp(r2, Rmul(cuts[0], cuts[0])) < 0 ? 'weak' : Rcmp(r2, Rmul(cuts[1], cuts[1])) < 0 ? 'moderate' : 'strong';
    var words = c.sign === 0 ? 'none: r = 0' : (c.sign > 0 ? 'positive' : 'negative') + ', ' + strength;
    var bt = astShow(Rabs(b));
    var line = 'y = ' + astShow(a) + (b.n < 0n ? ' − ' : ' + ') + bt + '·x';
    return {
      tiles: { astN: eaInt(s.n), astMeans: 'x̄ = ' + astShow(s.mx) + ', ȳ = ' + astShow(s.my), astR: c.text,
        astR2: eaPct(r2), astLine: line, astWords: words },
      status: aktStatus('Over ' + eaPlural(s.n, 'pair', 'pairs') + ', r is ' + astSay(c)
        + ' and r² says ' + eaPct(r2).replace(/^.*[=≈] /, '') + ' of the variation in y goes with x along the line; it does not say x moves y.'),
      table: { caption: 'Each pair, its deviations from the means and their product',
        head: ['name', 'x', 'y', 'x − x̄', 'y − ȳ', 'product'],
        rows: P.map(function (p) { var dx = Rsub(p.x, s.mx), dy = Rsub(p.y, s.my); return [p.name, astShow(p.x), astShow(p.y), astShow(dx), astShow(dy), astShow(Rmul(dx, dy))]; }) }
    };
  };
"""

AST_VIEW_JS["spurious"] = r"""
  AST_VIEW.spurious = function (inst) {
    var S = inst.series;
    S.forEach(function (p, i) {
      if (i && Rcmp(p.t, S[i - 1].t) <= 0) eaRefuse('Series, record ' + (i + 1) + ': t is ' + astShow(p.t) + ', not after ' + astShow(S[i - 1].t) + '; give the series in order of t, each t once');
    });
    var xs = S.map(function (p) { return p.x; }), ys = S.map(function (p) { return p.y; });
    var dx = [], dy = [];
    for (var i = 1; i < S.length; i += 1) { dx.push(Rsub(xs[i], xs[i - 1])); dy.push(Rsub(ys[i], ys[i - 1])); }
    var lv = astR(astSums(xs, ys)), df = astR(astSums(dx, dy));
    return {
      tiles: { astN: eaInt(S.length), astRLevels: astRt(lv), astRDiffs: astRt(df), astCompare: astVersus(lv, df) },
      status: aktStatus('Two series that both trend can correlate in their levels whatever links them; the first differences (each value less the one before, '
        + eaPlural(dx.length, 'difference', 'differences') + ') take the trend out. Against the r of the levels, ' + astSay(lv) + ', the r of the differences, ' + astSay(df) + ', is ' + astVersus(lv, df) + '.'),
      table: { caption: 'Each step: the levels and the change from the step before',
        head: ['t', 'x', 'y', 'change in x', 'change in y'],
        rows: S.map(function (p, i) { return [astShow(p.t), astShow(p.x), astShow(p.y), i ? astShow(dx[i - 1]) : '', i ? astShow(dy[i - 1]) : '']; }) }
    };
  };
"""

AST_VIEW_JS["confound"] = r"""
  AST_VIEW.confound = function (inst) {
    var rows = inst.rows, groups = [], by = {};
    rows.forEach(function (r) { if (!by[r.z]) { by[r.z] = { z: r.z, xs: [], ys: [] }; groups.push(by[r.z]); } by[r.z].xs.push(r.x); by[r.z].ys.push(r.y); });
    var all = astR(astSums(rows.map(function (r) { return r.x; }), rows.map(function (r) { return r.y; })));
    var sxx = R0, syy = R0, sxy = R0, parts = [], trows = [];
    groups.forEach(function (g) {
      var s = astSums(g.xs, g.ys), c;
      sxx = Radd(sxx, s.sxx); syy = Radd(syy, s.syy); sxy = Radd(sxy, s.sxy);
      if (s.n < 3) c = { ok: false, why: 'not computed: fewer than 3 rows' };
      else c = astR(s);
      parts.push(g.z + ' ' + astRt(c) + ' (n = ' + s.n + ')');
      trows.push([g.z, eaInt(s.n), astShow(s.mx), astShow(s.my), astShow(s.sxx), astShow(s.syy), astShow(s.sxy), astRt(c)]);
    });
    var pooled = astR({ sxx: sxx, syy: syy, sxy: sxy });
    return {
      tiles: { astN: eaInt(rows.length), astGroups: eaInt(groups.length) + ': ' + groups.map(function (g) { return g.z; }).join(', '),
        astR: astRt(all), astWithin: parts.join('; '), astPooled: astRt(pooled), astCompare: astVersus(all, pooled) },
      status: aktStatus('Over all ' + eaPlural(rows.length, 'row', 'rows') + ' r is ' + astSay(all) + '; inside the ' + eaPlural(groups.length, 'group', 'groups')
        + ' of z, pooled, it is ' + astSay(pooled) + ' (' + astVersus(all, pooled) + '). What z does to the pair is the difference; the rows alone do not say which way anything acts.'),
      table: { caption: 'Each group of z: its means, sums of squares and cross-products, and r',
        head: ['z', 'n', 'mean x', 'mean y', 'Sxx', 'Syy', 'Sxy', 'r'], rows: trows }
    };
  };
"""

# ---------------------------------------------------------------------------
# validity (avd): the item correlation matrix, AVE and composite reliability
# ---------------------------------------------------------------------------

AVD_JS = r"""
  var AVD_VIEW = {};
  function avdCompute(view, inst, opts) { return eaRun(AVD_VIEW[view], inst, opts); }
  /* An exact decimal with as few places as it needs (at most 6), else the
     fraction and 3 places. */
  function avdShow(r) {
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    if (eaBig(r)) return eaSci(r);
    return eaFrac(r) + ' ≈ ' + eaFixed(r, 3);
  }
  /* Three places: exact when the value is a decimal of at most 3 places. */
  function avdThree(r) { return (eaExactAt(r, 3) ? '' : '≈ ') + eaFixed(r, 3); }
  /* sqrt(q): exact when it is a decimal of at most 3 places, else "≈" and 3
     places by the exact method. */
  function avdRoot(q) { var e = aktSqrtExact(q); return e !== null && eaExactAt(e, 3) ? avdShow(e) : '≈ ' + aktSqrtFixed(q, 3); }
  /* Groups of names in the order first given. */
  function avdGroups(list, key, member) {
    var order = [], of = {};
    list.forEach(function (x) { var c = x[key]; if (!of[c]) { of[c] = []; order.push(c); } of[c].push(x[member]); });
    return { order: order, of: of };
  }
"""

AVD_VIEW_JS = {}

AVD_VIEW_JS["matrix"] = r"""
  function avdKey(a, b) { return a < b ? a + ' ' + b : b + ' ' + a; }
  AVD_VIEW.matrix = function (inst) {
    var items = inst.items, con = {}, g = avdGroups(items, 'construct', 'item'), r = {};
    items.forEach(function (it) { con[it.item] = it.construct; });
    if (g.order.length < 2) eaRefuse('Items: the matrix view compares constructs, and the items name only 1, ' + g.order[0]);
    inst.corr.forEach(function (p, i) {
      [p.a, p.b].forEach(function (x) { if (con[x] === undefined) eaRefuse('Correlations, record ' + (i + 1) + ': ' + x + ' is not one of the items'); });
      if (p.a === p.b) eaRefuse('Correlations, record ' + (i + 1) + ': ' + p.a + ' is paired with itself');
      var k = avdKey(p.a, p.b);
      if (r[k] !== undefined) eaRefuse('Correlations, record ' + (i + 1) + ': the pair ' + p.a + ', ' + p.b + ' is given twice');
      r[k] = p.r;
    });
    var n = items.length;
    for (var i = 0; i < n; i += 1) for (var j = i + 1; j < n; j += 1) {
      if (r[avdKey(items[i].item, items[j].item)] === undefined) eaRefuse('Correlations: the pair ' + items[i].item + ', ' + items[j].item
        + ' is missing; give every pair of different items once, ' + eaInt(n * (n - 1) / 2) + ' pairs for ' + n + ' items');
    }
    function mean(a, list) {
      var v = list.filter(function (b) { return b !== a; }).map(function (b) { return r[avdKey(a, b)]; });
      return v.length ? aktMean(v) : null;
    }
    var within = g.order.map(function (c) {
      var m = g.of[c], v = [];
      m.forEach(function (a, x) { m.slice(x + 1).forEach(function (b) { v.push(r[avdKey(a, b)]); }); });
      return c + ' ' + (v.length ? avdShow(aktMean(v)) : 'one item, no pairs');
    });
    var cross = [];
    items.forEach(function (a, x) { items.slice(x + 1).forEach(function (b) { if (a.construct !== b.construct) cross.push(r[avdKey(a.item, b.item)]); }); });
    var flagged = [], untested = [], rows = items.map(function (it) {
      var own = mean(it.item, g.of[it.construct]), worse = [];
      var cells = g.order.map(function (c) {
        if (c === it.construct) return '';
        var m = mean(it.item, g.of[c]);
        if (own !== null && Rcmp(m, own) > 0) worse.push(c + ' ' + avdShow(m));
        return avdShow(m);
      });
      if (own === null) untested.push(it.item);
      else if (worse.length) flagged.push(it.item + ' (own ' + avdShow(own) + '; with ' + worse.join(', with ') + ')');
      return [it.item, it.construct, own === null ? 'none (alone)' : avdShow(own)].concat(cells);
    });
    return {
      tiles: { avdItems: eaPlural(n, 'item', 'items') + ' in ' + eaPlural(g.order.length, 'construct', 'constructs'),
        avdWithin: within.join('; '), avdCross: avdShow(aktMean(cross)), avdFlagged: aktListed(flagged.length, flagged, '; ') },
      status: aktStatus('Each item\'s mean correlation with the other items of its own construct is set against its mean with each other construct\'s items; '
        + eaPlural(flagged.length, 'item correlates', 'items correlate') + ' more with another construct than with its own'
        + (untested.length ? ', and ' + eaPlural(untested.length, 'item is', 'items are') + ' alone in its construct, so not tested (' + untested.join(', ') + ')' : '') + '.'),
      table: { caption: 'Each item: its mean correlation with its own construct and with each other one',
        head: ['item', 'construct', 'own'].concat(g.order.map(function (c) { return 'with ' + c; })), rows: rows }
    };
  };
"""

AVD_VIEW_JS["ave"] = r"""
  AVD_VIEW.ave = function (inst, opts) {
    var L = inst.loadings, g = avdGroups(L, 'construct', 'item'), lam = {}, t = {};
    ['ave_min', 'cr_min', 'loading_min', 'r_max'].forEach(function (k, i) { t[k] = Rparse(opts[k] || ['0.5', '0.7', '0.6', '0.85'][i]); });
    L.forEach(function (x) { lam[x.item] = x.loading; });
    var seen = {};
    inst.between.forEach(function (p, i) {
      [p.c1, p.c2].forEach(function (c) { if (!g.of[c]) eaRefuse('Between, record ' + (i + 1) + ': ' + c + ' is not one of the constructs (' + g.order.join(', ') + ')'); });
      if (p.c1 === p.c2) eaRefuse('Between, record ' + (i + 1) + ': ' + p.c1 + ' is paired with itself');
      var k = p.c1 < p.c2 ? p.c1 + ' ' + p.c2 : p.c2 + ' ' + p.c1;
      if (seen[k]) eaRefuse('Between, record ' + (i + 1) + ': the pair ' + p.c1 + ', ' + p.c2 + ' is given twice');
      seen[k] = true;
    });
    var tests = 0, passed = 0, fails = [], ave = {}, rows = [];
    function test(ok, what) { tests += 1; if (ok) passed += 1; else fails.push(what); return ok ? 'yes' : 'no'; }
    var aveT = [], crT = [], rootT = [];
    g.order.forEach(function (c) {
      var ls = g.of[c].map(function (i) { return lam[i]; }), sum = eaSum(ls), sq = Rmul(sum, sum), err = R0, s2 = R0;
      ls.forEach(function (l) { var l2 = Rmul(l, l); s2 = Radd(s2, l2); err = Radd(err, Rsub(R1, l2)); });
      var a = Rdiv(s2, R(BigInt(ls.length))), cr = Rdiv(sq, Radd(sq, err));
      ave[c] = a;
      var okA = test(Rcmp(a, t.ave_min) > 0, c + ' AVE'), okC = test(Rcmp(cr, t.cr_min) >= 0, c + ' CR');
      aveT.push(c + ' ' + avdShow(a)); crT.push(c + ' ' + avdShow(cr)); rootT.push(c + ' ' + avdRoot(a));
      rows.push([c, eaInt(ls.length), avdShow(a), okA, avdShow(cr), okC, avdRoot(a)]);
    });
    var low = [];
    L.forEach(function (x) { if (test(Rcmp(x.loading, t.loading_min) > 0, x.item + ' loading') === 'no') low.push(x.item + ' ' + avdShow(x.loading)); });
    var pairs = inst.between.map(function (p) {
      var r2 = Rmul(p.r, p.r), ra = avdShow(Rabs(p.r));
      var o1 = test(Rcmp(ave[p.c1], r2) > 0, '√AVE of ' + p.c1 + ' against ' + p.c2), o2 = test(Rcmp(ave[p.c2], r2) > 0, '√AVE of ' + p.c2 + ' against ' + p.c1);
      var o3 = test(Rcmp(r2, Rmul(t.r_max, t.r_max)) < 0, p.c1 + ', ' + p.c2 + ' |r|');
      return p.c1 + ', ' + p.c2 + ' |r| ' + ra + ': √AVE ' + p.c1 + ' above it ' + o1 + ', √AVE ' + p.c2 + ' above it ' + o2 + ', below ' + avdShow(t.r_max) + ' ' + o3;
    });
    return {
      tiles: { avdAve: aveT.join('; '), avdCr: crT.join('; '), avdRoot: rootT.join('; '), avdLow: aktListed(low.length, low),
        avdPairs: pairs.length ? pairs.join('; ') : 'no pair given', avdTests: eaInt(passed) + ' of ' + eaInt(tests) + ' pass' + (fails.length ? '; not passed: ' + fails.join(', ') : '') },
      status: aktStatus(eaInt(passed) + ' of ' + eaPlural(tests, 'test passes', 'tests pass') + ' at the thresholds stated (AVE above ' + avdShow(t.ave_min) + ', CR at least '
        + avdShow(t.cr_min) + ', loadings above ' + avdShow(t.loading_min) + ', |r| below ' + avdShow(t.r_max) + '). Passing says the items behave as a measure should in this sample; it does not say what they measure.'),
      table: { caption: 'Each construct: AVE, composite reliability and the square root of the AVE',
        head: ['construct', 'items', 'AVE', 'AVE passes', 'CR', 'CR passes', '√AVE'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# groups (agr): times as likely, eNPS, early against late respondents
# ---------------------------------------------------------------------------

AGR_JS = r"""
  var AGR_VIEW = {};
  function agrCompute(view, inst, opts) { return eaRun(AGR_VIEW[view], inst, opts); }
  /* "9 of 12 = 75%", "1 of 3 ≈ 33.3%". */
  function agrShare(m, n) { var t = eaPct(R(BigInt(m), BigInt(n))); return eaInt(m) + ' of ' + eaInt(n) + t.slice(t.search(/ [=≈] /)); }
  /* Two places always (acckit's rule for ratios): "2.00", "1.50", "≈ 2.67". */
  function agrTwo(r) { return aktTwo(r); }
  function agrThree(r) {
    if (Rint(r)) return eaInt(r.n);
    if (eaBig(r)) return eaSci(r);
    return eaFrac(r) + (eaExactAt(r, 3) ? ' = ' : ' ≈ ') + eaFixed(r, 3);
  }
  function agrShow(r) {
    for (var p = 0; p <= 6; p += 1) if (eaExactAt(r, p)) return eaFixed(r, p);
    return eaFrac(r) + ' ≈ ' + eaFixed(r, 3);
  }
"""

AGR_VIEW_JS = {}

AGR_VIEW_JS["likely"] = r"""
  AGR_VIEW.likely = function (inst) {
    var rows = inst.rows, of = {};
    rows.forEach(function (r, i) {
      if (Rcmp(r.met, r.n) > 0) eaRefuse('Rows, record ' + (i + 1) + ': ' + r.group + ' has ' + eaInt(r.met.n) + ' meeting the outcome, more than its n of ' + eaInt(r.n.n));
      of[r.group] = r;
    });
    [['first', inst.first], ['second', inst.second]].forEach(function (x) {
      if (!of[x[1]]) eaRefuse('The ' + x[0] + ' group, ' + x[1] + ', is not one of the groups (' + rows.map(function (r) { return r.group; }).join(', ') + ')');
    });
    if (inst.first === inst.second) eaRefuse('The two groups compared are the same group, ' + inst.first);
    var a = of[inst.first], b = of[inst.second];
    var sa = Rdiv(a.met, a.n), sb = Rdiv(b.met, b.n);
    var ratio = Rzero(sb) ? 'not defined: no one in ' + b.group + ' met it' : aktTimes(Rdiv(sa, sb));
    var am = a.met.n, an = a.n.n - a.met.n, bm = b.met.n, bn = b.n.n - b.met.n, odds;
    if (an === 0n) odds = 'not defined: everyone in ' + a.group + ' met it';
    else if (bm === 0n) odds = 'not defined: no one in ' + b.group + ' met it';
    else odds = agrTwo(R(am * bn, an * bm));
    return {
      tiles: { agrShares: rows.map(function (r) { return r.group + ' ' + agrShare(r.met.n, r.n.n); }).join('; '),
        agrRatio: ratio, agrDiff: aktPp(Rsub(sa, sb)), agrOdds: odds },
      status: aktStatus(a.group + ' meet the outcome ' + (Rzero(sb) ? 'where no one in ' + b.group + ' does' : ratio + ' as often as ' + b.group)
        + ' (' + aktPp(Rsub(sa, sb)) + '); the odds ratio, ' + odds + ', is a different figure and is not "times as likely".'),
      table: { caption: 'Each group: n, those meeting the outcome, the share and the odds',
        head: ['group', 'n', 'met', 'share', 'odds (met : not)'],
        rows: rows.map(function (r) { var no = r.n.n - r.met.n; return [r.group, eaInt(r.n.n), eaInt(r.met.n), eaPct(R(r.met.n, r.n.n)), no === 0n ? 'no one missed it' : agrShow(R(r.met.n, no))]; }) }
    };
  };
"""

AGR_VIEW_JS["enps"] = r"""
  AGR_VIEW.enps = function (inst) {
    var A = inst.answers.map(function (x) { return x.answer === undefined ? { name: '', answer: x } : x; }), n = A.length;
    var pro = 0, pas = 0, det = 0, six = 0, eight = 0;
    A.forEach(function (x) {
      var v = Number(x.answer.n);
      if (v >= 9) pro += 1; else if (v >= 7) pas += 1; else det += 1;
      if (v === 6) six += 1; if (v === 8) eight += 1;
    });
    var e = R(BigInt(pro - det), BigInt(n)), score = aktPp(e).replace(/ points$/, '');
    var step = aktPp(R(1n, BigInt(n)));
    return {
      tiles: { agrN: eaInt(n), agrPromoters: agrShare(pro, n), agrPassives: agrShare(pas, n), agrDetractors: agrShare(det, n),
        agrEnps: score,
        agrNear: six + eight === 0 ? '0: no answer is at 6 or 8' : eaInt(six + eight) + ': ' + eaInt(six) + ' at 6 (a detractor one point from passive), ' + eaInt(eight)
          + ' at 8 (a passive one point from promoter); each one moved raises eNPS by ' + step.replace('+', '') },
      status: aktStatus('eNPS is the percentage of promoters (9 or 10) less the percentage of detractors (0 to 6); passives (7 or 8) count in n only. Here it is '
        + score + ' over ' + eaPlural(n, 'answer', 'answers') + '.'),
      table: { caption: 'Each answer and its band', head: ['answer', 'how many', 'band'],
        rows: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0].map(function (v) {
          var k = A.filter(function (x) { return Number(x.answer.n) === v; }).length;
          return [String(v), eaInt(k), v >= 9 ? 'promoter' : v >= 7 ? 'passive' : 'detractor'];
        }).filter(function (r) { return r[1] !== '0'; }) }
    };
  };
"""

AGR_VIEW_JS["bias"] = r"""
  AGR_VIEW.bias = function (inst) {
    var T = inst.table, crit = inst.critical, early = 0n, late = 0n;
    T.forEach(function (r, i) {
      if (r.early.n + r.late.n === 0n) eaRefuse('Table, record ' + (i + 1) + ': ' + r.category + ' has no respondents, early or late');
      early += r.early.n; late += r.late.n;
    });
    if (early === 0n) eaRefuse('Table: no respondent is early, so there is nothing to compare');
    if (late === 0n) eaRefuse('Table: no respondent is late, so there is nothing to compare');
    var N = early + late, chi = R0, small = [], rows = [];
    T.forEach(function (r) {
      var row = r.early.n + r.late.n, part = R0, cells = [];
      [['early', r.early.n, early], ['late', r.late.n, late]].forEach(function (c) {
        var E = R(row * c[2], N), d = Rsub(R(c[1]), E), q = Rdiv(Rmul(d, d), E);
        part = Radd(part, q);
        if (Rcmp(E, R(5n)) < 0) small.push(r.category + ' ' + c[0] + ' (expected ' + agrShow(E) + ')');
        cells.push(eaInt(c[1]), agrShow(E));
      });
      chi = Radd(chi, part);
      rows.push([r.category].concat(cells).concat([agrShow(part)]));
    });
    var df = T.length - 1, over = Rcmp(chi, crit) > 0, c3 = eaFixed(chi, 3);
    return {
      tiles: { agrN: 'early ' + eaInt(early) + ', late ' + eaInt(late) + ', all ' + eaInt(N), agrChi: agrThree(chi), agrDf: eaInt(df),
        agrExceeds: (over ? 'yes: ' + c3 + ' is above ' : 'no: ' + c3 + ' is not above ') + agrShow(crit) + ', the critical value stated',
        agrSmall: aktListed(small.length, small) },
      status: aktStatus('χ² = ' + c3 + ' on ' + eaPlural(df, 'degree', 'degrees') + ' of freedom, ' + (over ? 'above' : 'not above') + ' the critical value the lesson states, '
        + agrShow(crit) + '; the lab gives no p-value.' + (small.length ? ' ' + eaPlural(small.length, 'cell has', 'cells have') + ' an expected count below 5, where the comparison is rough.' : '')
        + ' Late respondents standing in for non-respondents is an assumption, not a finding.'),
      table: { caption: 'Each category: observed and expected counts, early and late, and its share of χ²',
        head: ['category', 'early', 'expected', 'late', 'expected', '(O − E)²/E'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# sample (asn) and capability (acp)
# ---------------------------------------------------------------------------

ASN_JS = r"""
  var ASN_VIEW = {};
  function asnCompute(view, inst, opts) { return eaRun(ASN_VIEW[view], inst, opts); }
  /* "5 of 9 ≈ 55.6%". */
  function asnShare(m, n) { var t = eaPct(R(BigInt(m), BigInt(n))); return eaInt(m) + ' of ' + eaInt(n) + t.slice(t.search(/ [=≈] /)); }
"""

ASN_VIEW_JS = {}

ASN_VIEW_JS["snowball"] = r"""
  ASN_VIEW.snowball = function (inst) {
    var P = inst.people, by = {}, seeds = [];
    P.forEach(function (p) { by[p.person] = p; });
    P.forEach(function (p, i) {
      if (p.referred_by === '-') { seeds.push(p.person); return; }
      if (p.referred_by === p.person) eaRefuse('People, record ' + (i + 1) + ': ' + p.person + ' is referred by themselves');
      if (!by[p.referred_by]) eaRefuse('People, record ' + (i + 1) + ': ' + p.person + ' is referred by ' + p.referred_by + ', who is not one of the people');
    });
    /* Wave and seed by following referrals back; a loop never reaches a seed. */
    var wave = {}, seed = {};
    P.forEach(function (p) {
      var chain = [], x = p.person, seen = {};
      while (wave[x] === undefined && by[x].referred_by !== '-') {
        if (seen[x]) eaRefuse('People: ' + chain.slice(chain.indexOf(x)).join(', ') + ' refer one another in a loop that reaches no seed');
        seen[x] = true; chain.push(x); x = by[x].referred_by;
      }
      if (wave[x] === undefined) { wave[x] = 0; seed[x] = x; }
      for (var j = chain.length - 1; j >= 0; j -= 1) { var y = chain[j], up = by[y].referred_by; wave[y] = wave[up] + 1; seed[y] = seed[up]; }
    });
    var drop = inst.drop;
    if (drop !== '-' && seeds.indexOf(drop) < 0) eaRefuse('The seed to drop, ' + drop + ', is not one of the seeds (' + seeds.join(', ') + ')');
    var groups = [], top = 0;
    P.forEach(function (p) { if (groups.indexOf(p.group) < 0) groups.push(p.group); if (wave[p.person] > top) top = wave[p.person]; });
    var waves = [];
    for (var w = 0; w <= top; w += 1) waves.push('wave ' + w + ': ' + P.filter(function (p) { return wave[p.person] === w; }).length);
    function shares(list) {
      return groups.map(function (g) { return g + ' ' + asnShare(list.filter(function (p) { return p.group === g; }).length, list.length); }).join('; ');
    }
    var n = P.length, kept = P.filter(function (p) { return drop === '-' || seed[p.person] !== drop; });
    var lost = P.filter(function (p) { return drop !== '-' && seed[p.person] === drop; }).map(function (p) { return p.person; });
    return {
      tiles: { asnSeeds: aktListed(seeds.length, seeds), asnWaves: waves.join('; '), asnSize: eaInt(n),
        asnTrees: seeds.map(function (s) { return s + ' ' + asnShare(P.filter(function (p) { return seed[p.person] === s; }).length, n); }).join('; '),
        asnGroups: shares(P),
        asnLost: drop === '-' ? 'no seed dropped' : aktListed(lost.length, lost),
        asnAfter: drop === '-' ? 'no seed dropped' : kept.length ? shares(kept) : 'no one is left' },
      status: aktStatus('From ' + eaPlural(seeds.length, 'seed', 'seeds') + ' the referrals reach ' + eaPlural(n, 'person', 'people') + ' in '
        + eaPlural(top + 1, 'wave', 'waves') + '. Who is in the sample depends on whom the seeds know; the shares are of this sample, not of everyone it was drawn to reach.'),
      table: { caption: 'Each person: who referred them, their wave, the seed their chain starts from, and their group',
        head: ['person', 'referred by', 'wave', 'seed', 'group'],
        rows: P.map(function (p) { return [p.person, p.referred_by === '-' ? 'a seed' : p.referred_by, String(wave[p.person]), seed[p.person], p.group]; }) }
    };
  };
"""

ACP_JS = r"""
  var ACP_VIEW = {};
  function acpCompute(view, inst, opts) { return eaRun(ACP_VIEW[view], inst, opts); }
"""

ACP_VIEW_JS = {}

ACP_VIEW_JS["profile"] = r"""
  /* Each record's names: capabilities, each once. */
  function acpNames(list, known, what, key) {
    list.forEach(function (t, i) {
      var seen = {};
      t.rest.forEach(function (c) {
        if (!known[c]) eaRefuse(what + ', record ' + (i + 1) + ' (' + t[key] + '): ' + c + ' is not one of the capabilities');
        if (seen[c]) eaRefuse(what + ', record ' + (i + 1) + ' (' + t[key] + ') names ' + c + ' twice');
        seen[c] = true;
      });
    });
  }
  var ACP_SHOW = 3;
  ACP_VIEW.profile = function (inst) {
    var C = inst.capabilities, T = inst.teams, L = inst.levels, T2 = inst.teams2, known = {}, cats = [], inCat = {};
    C.forEach(function (c) { known[c.capability] = true; if (!inCat[c.category]) { inCat[c.category] = []; cats.push(c.category); } inCat[c.category].push(c.capability); });
    acpNames(T, known, 'Teams', 'team');
    acpNames(L, known, 'Levels', 'level');
    acpNames(T2, known, 'Teams at the second date', 'team');
    var levelOf = {}, has = {}, teamNames = T.map(function (t) { return t.team; });
    L.forEach(function (l, i) {
      l.rest.forEach(function (c) {
        if (levelOf[c] !== undefined) eaRefuse('Levels, record ' + (i + 1) + ' (' + l.level + '): ' + c + ' is already required by level ' + L[levelOf[c]].level);
        levelOf[c] = i;
      });
    });
    T2.forEach(function (t, i) { if (teamNames.indexOf(t.team) < 0) eaRefuse('Teams at the second date, record ' + (i + 1) + ': ' + t.team + ' is not one of the teams (' + teamNames.join(', ') + ')'); });
    T.forEach(function (t) { has[t.team] = {}; t.rest.forEach(function (c) { has[t.team][c] = true; }); });
    var total = C.length, overall = [], byCat = [], level = [], hidden = [], added = [];
    T.forEach(function (t) {
      var h = has[t.team];
      overall.push(t.team + ' ' + eaInt(t.rest.length) + ' of ' + eaInt(total));
      byCat.push(t.team + ': ' + cats.map(function (k) { return k + ' ' + inCat[k].filter(function (c) { return h[c]; }).length + ' of ' + inCat[k].length; }).join(', '));
      if (!L.length) return;
      var reached = -1;
      for (var i = 0; i < L.length; i += 1) { if (L[i].rest.every(function (c) { return h[c]; })) reached = i; else break; }
      level.push(t.team + ' ' + (reached < 0 ? 'none (level 1 of ' + L.length + ', ' + L[0].level + ', not met)' : L[reached].level + ' (level ' + (reached + 1) + ' of ' + L.length + ')'));
      var above = C.map(function (c) { return c.capability; }).filter(function (c) { return h[c] && levelOf[c] !== undefined && levelOf[c] > reached; });
      hidden.push(t.team + ' ' + aktListed(above.length, above));
    });
    T2.forEach(function (t) {
      var h = has[t.team], h2 = {};
      t.rest.forEach(function (c) { h2[c] = true; });
      var plus = C.map(function (c) { return c.capability; }).filter(function (c) { return h2[c] && !h[c]; });
      var minus = C.map(function (c) { return c.capability; }).filter(function (c) { return h[c] && !h2[c]; });
      added.push(t.team + ' +' + plus.length + (plus.length ? ' (' + plus.join(', ') + ')' : '') + (minus.length ? ', −' + minus.length + ' (' + minus.join(', ') + ')' : ''));
    });
    var count = C.map(function (c) { return T.filter(function (t) { return has[t.team][c.capability]; }).length; }), low = Math.min.apply(null, count);
    var fewest = C.filter(function (_c, i) { return count[i] === low; }).map(function (c) { return c.capability; });
    return {
      tiles: { acpTeams: aktListed(T.length, teamNames), acpOverall: overall.join('; '), acpCategories: byCat.join('; '),
        acpLevel: L.length ? level.join('; ') : 'no maturity model given', acpHidden: L.length ? hidden.join('; ') : 'no maturity model given',
        acpAdded: T2.length ? added.join('; ') : 'no second date given',
        acpFewest: eaInt(low) + ' of ' + eaPlural(T.length, 'team', 'teams') + ': ' + fewest.slice(0, ACP_SHOW).join(', ')
          + (fewest.length > ACP_SHOW ? ' and ' + eaInt(fewest.length - ACP_SHOW) + ' more (the table lists all)' : '') },
      status: aktStatus('A profile lists what each team has in place, capability by capability' + (L.length ? '; a maturity level is the highest level whose requirements, and every lower level\'s, are all met, and it says nothing of what a team has above it' : '')
        + (L.length ? '. Neither is a grade of the team.' : '. It is not a grade of the team.')),
      table: { caption: 'Each capability, its category, and the teams that have it in place',
        head: ['capability', 'category'].concat(L.length ? ['level'] : []).concat(teamNames),
        rows: C.map(function (c) { return [c.capability, c.category].concat(L.length ? [levelOf[c.capability] === undefined ? '' : L[levelOf[c.capability]].level] : []).concat(T.map(function (t) { return has[t.team][c.capability] ? 'yes' : ''; })); }) }
    };
  };
"""

# ---------------------------------------------------------------------------
# Python: printing for refusal sentences (the JS printers, mirrored)
# ---------------------------------------------------------------------------


def _fixed(fr, places):
    """eaFixed: exactly `places` decimals, half away from zero, grouped, U+2212."""
    fr = Fraction(fr)
    num, den = abs(fr.numerator), fr.denominator
    q = (num * 10 ** places * 2 // den + 1) // 2
    s = str(q).rjust(places + 1, "0")
    whole, frac = s[:len(s) - places], s[len(s) - places:]
    return (_MINUS if fr < 0 and q else "") + "{:,}".format(int(whole)) + ("." + frac if places else "")


def _show(fr):
    """astShow/alkShow/avdShow: an exact decimal in as few places as it needs (at most 6), else fraction ≈ 3 places."""
    fr = Fraction(fr)
    for p in range(7):
        if (fr * 10 ** p).denominator == 1:
            return _fixed(fr, p)
    return "%s/%s ≈ %s" % (ea.grp(fr.numerator), ea.grp(fr.denominator), _fixed(fr, 3))


def _plural(n, one, many):
    return "%s %s" % (ea.grp(n), one if n == 1 else many)


def _mean(v):
    return sum(v, Fraction(0)) / len(v)


def _sums(xs, ys):
    mx, my = _mean(xs), _mean(ys)
    return (sum(((x - mx) ** 2 for x in xs), Fraction(0)), sum(((y - my) ** 2 for y in ys), Fraction(0)))


def _cfg_dec(cfg, kit, key, default, lo, hi, strict_lo=False):
    """A lesson-level threshold: a decimal string (or an int) within [lo, hi]; returned as its text."""
    v = cfg.get(key, default)
    if isinstance(v, bool) or not isinstance(v, (str, int)):
        raise ValueError("%s: cfg[%r] is a decimal written as a string, such as \"0.7\", not %r" % (kit, key, v))
    s = str(v).strip()
    if not re.fullmatch(r"\d+(?:\.\d{1,6})?|\.\d{1,6}", s):
        raise ValueError("%s: cfg[%r] is a decimal written as a string, such as \"0.7\", not %r" % (kit, key, v))
    f = Fraction(s)
    if f > hi or f < lo or (strict_lo and f == lo):
        raise ValueError("%s: cfg[%r] lies %s %s to %s, and it is %s" % (kit, key, "above" if strict_lo else "from",
                                                                      _show(lo), _show(hi), s))
    return s


# ---------------------------------------------------------------------------
# Python: the checks (each mirrors a JS refusal beyond the field parser)
# ---------------------------------------------------------------------------


def _answers(lst, k, points, what, names):
    for i, a in enumerate(lst):
        if len(a["rest"]) != k:
            raise ValueError("%s, record %d (%s) gives %s; there %s (%s), so each record needs %d"
                             % (what, i + 1, a["respondent"], _plural(len(a["rest"]), "answer", "answers"),
                                "is 1 item" if k == 1 else "are %d items" % k, ", ".join(names), k))
        for j, x in enumerate(a["rest"]):
            if not 1 <= x <= points:
                raise ValueError("%s, record %d (%s): answer %d is %s; on a %d-point scale an answer is 1 to %d"
                                 % (what, i + 1, a["respondent"], j + 1, ea.grp(int(x)), points, points))


def _line_ok(r, points, what):
    if not 1 <= r <= points:
        raise ValueError("%s is %s; on a %d-point scale it lies from 1 to %d" % (what, _show(r), points, points))


def _check_score(inst, fixed):
    points = int(inst["points"])
    _answers(inst["answers"], len(inst["items"]), points, "Answers", [it["item"] for it in inst["items"]])
    _line_ok(inst["line"], points, "The line")


def _check_westrum(inst, fixed):
    points, items, cuts = int(inst["points"]), inst["items"], inst["cuts"]
    cons = []
    for it in items:
        if it["construct"] not in cons:
            cons.append(it["construct"])
    if len(cons) != 1:
        raise ValueError("Items: the westrum view scores one construct, and the items name %d: %s" % (len(cons), ", ".join(cons)))
    if len(cuts) != 2:
        raise ValueError("The cuts are two values on the scale, low then high; there %s"
                         % ("is 1" if len(cuts) == 1 else "are %d" % len(cuts)))
    _line_ok(cuts[0], points, "The first cut")
    _line_ok(cuts[1], points, "The second cut")
    if cuts[0] >= cuts[1]:
        raise ValueError("The cuts go low then high, and %s is not below %s" % (_show(cuts[0]), _show(cuts[1])))
    names = [it["item"] for it in items]
    _answers(inst["answers"], len(items), points, "Answers", names)
    _answers(inst["answers2"], len(items), points, "Second answers", names)


def _pvar(v):
    m = _mean(v)
    return sum(((x - m) ** 2 for x in v), Fraction(0)) / len(v)


def _check_alpha(inst, fixed):
    names, A = inst["items"], inst["answers"]
    _answers(A, len(names), int(inst["points"]), "Answers", names)
    if _pvar([sum(a["rest"], Fraction(0)) for a in A]) == 0:
        raise ValueError("Answers: every respondent's total is the same, so the total varies by nothing and alpha is "
                         "not defined")


def _check_pearson(inst, fixed):
    p = inst["pairs"]
    sxx, syy = _sums([x["x"] for x in p], [x["y"] for x in p])
    if sxx == 0:
        raise ValueError("Pairs: r is not defined: every x is the same, so there is no correlation to compute")
    if syy == 0:
        raise ValueError("Pairs: r is not defined: every y is the same, so there is no correlation to compute")


def _check_spurious(inst, fixed):
    s = inst["series"]
    for i in range(1, len(s)):
        if s[i]["t"] <= s[i - 1]["t"]:
            raise ValueError("Series, record %d: t is %s, not after %s; give the series in order of t, each t once"
                             % (i + 1, _show(s[i]["t"]), _show(s[i - 1]["t"])))


def _check_matrix(inst, fixed):
    items, con, cons = inst["items"], {}, []
    for it in items:
        con[it["item"]] = it["construct"]
        if it["construct"] not in cons:
            cons.append(it["construct"])
    if len(cons) < 2:
        raise ValueError("Items: the matrix view compares constructs, and the items name only 1, %s" % cons[0])
    seen = set()
    for i, p in enumerate(inst["corr"]):
        for x in (p["a"], p["b"]):
            if x not in con:
                raise ValueError("Correlations, record %d: %s is not one of the items" % (i + 1, x))
        if p["a"] == p["b"]:
            raise ValueError("Correlations, record %d: %s is paired with itself" % (i + 1, p["a"]))
        k = frozenset((p["a"], p["b"]))
        if k in seen:
            raise ValueError("Correlations, record %d: the pair %s, %s is given twice" % (i + 1, p["a"], p["b"]))
        seen.add(k)
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if frozenset((items[i]["item"], items[j]["item"])) not in seen:
                raise ValueError("Correlations: the pair %s, %s is missing; give every pair of different items once, "
                                 "%s pairs for %d items" % (items[i]["item"], items[j]["item"],
                                                             ea.grp(n * (n - 1) // 2), n))


def _check_ave(inst, fixed):
    cons = []
    for x in inst["loadings"]:
        if x["construct"] not in cons:
            cons.append(x["construct"])
    seen = set()
    for i, p in enumerate(inst["between"]):
        for c in (p["c1"], p["c2"]):
            if c not in cons:
                raise ValueError("Between, record %d: %s is not one of the constructs (%s)" % (i + 1, c, ", ".join(cons)))
        if p["c1"] == p["c2"]:
            raise ValueError("Between, record %d: %s is paired with itself" % (i + 1, p["c1"]))
        k = frozenset((p["c1"], p["c2"]))
        if k in seen:
            raise ValueError("Between, record %d: the pair %s, %s is given twice" % (i + 1, p["c1"], p["c2"]))
        seen.add(k)


def _check_likely(inst, fixed):
    rows = inst["rows"]
    for i, r in enumerate(rows):
        if r["met"] > r["n"]:
            raise ValueError("Rows, record %d: %s has %s meeting the outcome, more than its n of %s"
                             % (i + 1, r["group"], ea.grp(int(r["met"])), ea.grp(int(r["n"]))))
    names = [r["group"] for r in rows]
    for which, g in (("first", inst["first"]), ("second", inst["second"])):
        if g not in names:
            raise ValueError("The %s group, %s, is not one of the groups (%s)" % (which, g, ", ".join(names)))
    if inst["first"] == inst["second"]:
        raise ValueError("The two groups compared are the same group, %s" % inst["first"])


def _check_bias(inst, fixed):
    early = late = 0
    for i, r in enumerate(inst["table"]):
        if r["early"] + r["late"] == 0:
            raise ValueError("Table, record %d: %s has no respondents, early or late" % (i + 1, r["category"]))
        early += r["early"]
        late += r["late"]
    if early == 0:
        raise ValueError("Table: no respondent is early, so there is nothing to compare")
    if late == 0:
        raise ValueError("Table: no respondent is late, so there is nothing to compare")


def _check_snowball(inst, fixed):
    P = inst["people"]
    by = {p["person"]: p for p in P}
    seeds = []
    for i, p in enumerate(P):
        if p["referred_by"] == "-":
            seeds.append(p["person"])
            continue
        if p["referred_by"] == p["person"]:
            raise ValueError("People, record %d: %s is referred by themselves" % (i + 1, p["person"]))
        if p["referred_by"] not in by:
            raise ValueError("People, record %d: %s is referred by %s, who is not one of the people"
                             % (i + 1, p["person"], p["referred_by"]))
    wave = {}
    for p in P:
        chain, x, seen = [], p["person"], set()
        while x not in wave and by[x]["referred_by"] != "-":
            if x in seen:
                raise ValueError("People: %s refer one another in a loop that reaches no seed"
                                 % ", ".join(chain[chain.index(x):]))
            seen.add(x)
            chain.append(x)
            x = by[x]["referred_by"]
        if x not in wave:
            wave[x] = 0
        for y in reversed(chain):
            wave[y] = wave[by[y]["referred_by"]] + 1
    d = inst["drop"]
    if d != "-" and d not in seeds:
        raise ValueError("The seed to drop, %s, is not one of the seeds (%s)" % (d, ", ".join(seeds)))


def _names_ok(lst, known, what, key):
    for i, t in enumerate(lst):
        seen = set()
        for c in t["rest"]:
            if c not in known:
                raise ValueError("%s, record %d (%s): %s is not one of the capabilities" % (what, i + 1, t[key], c))
            if c in seen:
                raise ValueError("%s, record %d (%s) names %s twice" % (what, i + 1, t[key], c))
            seen.add(c)


def _check_profile(inst, fixed):
    known = {c["capability"] for c in inst["capabilities"]}
    _names_ok(inst["teams"], known, "Teams", "team")
    _names_ok(inst["levels"], known, "Levels", "level")
    _names_ok(inst["teams2"], known, "Teams at the second date", "team")
    level_of = {}
    for i, lv in enumerate(inst["levels"]):
        for c in lv["rest"]:
            if c in level_of:
                raise ValueError("Levels, record %d (%s): %s is already required by level %s"
                                 % (i + 1, lv["level"], c, inst["levels"][level_of[c]]["level"]))
            level_of[c] = i
    teams = [t["team"] for t in inst["teams"]]
    for i, t in enumerate(inst["teams2"]):
        if t["team"] not in teams:
            raise ValueError("Teams at the second date, record %d: %s is not one of the teams (%s)"
                             % (i + 1, t["team"], ", ".join(teams)))


# ---------------------------------------------------------------------------
# Python: the spec dicts (kit-contract.md section 2)
# ---------------------------------------------------------------------------

_POINTS = ("points", ea.choice("Points on the scale", "5", "7"), "7")
_ITEMS = ("items", arec("Items (item, construct, reverse-coded yes or no)",
                        [("item", _N), ("construct", _N), ("reverse", ea.YESNO)], unique=True, rows=3, hi=40), None)


def _answers_field(what, lo=1, lo_rest=1):
    return arec(what, [("respondent", _N)], ea.whole(1, 7), "answer", lo_rest, 40, unique=True, rows=4, lo=lo)


_ALPHA_RULE = ("Variances are population variances (divide by n). With sample variances (divide by n − 1) every "
               "variance grows by the same factor n/(n − 1), so the ratio, and alpha, are the same. ")


def _alpha_options(cfg, kit, tiles):
    return {"alpha_min": _cfg_dec(cfg, kit, "alpha_min", "0.7", Fraction(0), Fraction(1))}, ["alpha_min"], tiles


LIKERT = {
    "prefix": "alk", "fn": "alkCompute", "title": "Likert-type items", "js": ALK_JS,
    "views": {
        "score": {
            "fields": [_POINTS, _ITEMS,
                       ("answers", _answers_field("Answers (respondent, then one answer per item, in the items' order)"), None),
                       ("line", ea.field("The line (a value on the scale)", ea.num(lo=0)), "4")],
            "tiles": [("Respondents", "alkN"), ("Construct means, reverse-coded items reversed", "alkConstructs"),
                      ("Item means, as scored", "alkItems"), ("Respondents above, at and below the line", "alkLine"),
                      ("Reverse-coded items", "alkReversed"),
                      ("Construct means if nothing were reversed (the error)", "alkUnreversed")],
            "check": _check_score,
            "subtitle": "a construct's score from Likert-type items, reverse-coded where stated",
            "rules": "Each answer is a whole number from 1 to the scale's points, one per item in the items' order. A "
                     "reverse-coded item is scored points + 1 − the answer (on 7 points a 2 scores 6). A respondent's "
                     "score on a construct is the mean of their scored answers on its items; a construct's mean is "
                     "the mean of those scores over the respondents; an item's mean is over the respondents too, as "
                     "scored. A respondent is above the line when their score is greater than it, at it when equal. "
                     "The last tile scores every item as answered, the mistake of forgetting to reverse. Constructs "
                     "and items go in the order given; means are exact, shown to 3 places when they do not end.",
            "js": ALK_VIEW_JS["score"],
        },
        "westrum": {
            "fields": [_POINTS, _ITEMS,
                       ("answers", _answers_field("Answers (respondent, then one answer per item)"), None),
                       ("cuts", alist("Cuts on the scale (two values, low then high, the lesson's own)",
                                      ea.num(lo=0), lo=1, hi=4, things="values"), None),
                       ("answers2", _answers_field("Second survey's answers (the same shape; empty for none)", lo=0),
                        "")],
            "tiles": [("Respondents", "alkN"), ("Team mean and band", "alkTeam"), ("Respondents by band", "alkBands"),
                      ("Second survey: team mean and band", "alkTeam2"), ("Second survey: by band", "alkBands2"),
                      ("Change in the team mean", "alkChange"), ("Change per respondent in both surveys", "alkEach")],
            "check": _check_westrum,
            "subtitle": "a Westrum culture score and its band, by cut-points the lesson states",
            "rules": "Items are scored as in the score view (reverse-coded ones reversed) and must all belong to one "
                     "construct. A mean below the first cut is pathological, from the first cut up to (not including) "
                     "the second is bureaucratic, and from the second cut up is generative. The cuts are the "
                     "lesson's: the book gives none. The team mean is the mean of the respondents' means. With a "
                     "second survey, a respondent's change is their second mean less their first, for respondents "
                     "named in both; the change in the team mean uses everyone in each survey.",
            "js": ALK_VIEW_JS["westrum"],
        },
        "alpha": {
            "fields": [_POINTS,
                       ("items", alist("Items of the construct (2 to 20 names, in the answers' order)", _N, lo=2, hi=20,
                                       things="items"), None),
                       ("answers", _answers_field("Answers (respondent, then one answer per item)", lo=3, lo_rest=2),
                        None)],
            "tiles": [("Items k", "alkK"), ("Respondents n", "alkN"), ("Item variances", "alkVars"),
                      ("Variance of the total score", "alkTotal"), ("Cronbach's alpha", "alkAlpha"),
                      ("Alpha with each item removed", "alkDeleted"), ("At or above the threshold", "alkMeets")],
            "check": _check_alpha, "options": _alpha_options,
            "subtitle": "Cronbach's alpha for one construct's items",
            "rules": "Alpha = k/(k − 1) × (1 − the sum of the item variances ÷ the variance of the total score), "
                     "where the total is a respondent's answers added up, computed exactly and shown to 3 places. "
                     + _ALPHA_RULE + "Alpha with an item removed recomputes it over the other k − 1 items (not "
                     "computed when only one would be left). The threshold is the lesson's (default 0.70, the "
                     "book's), met when alpha is at or above it, compared exactly. Answers are used as given: "
                     "reverse any reverse-coded item before entering it.",
            "js": ALK_VIEW_JS["alpha"],
        },
    },
}


def _named_values(cfg, kind_what, key, each, list_what, rec_what, lo):
    if cfg.get("named", "no") == "yes":
        return (key, arec(rec_what, [("name", _N), (kind_what, each)], unique=True, rows=3, lo=lo), None)
    return (key, alist(list_what, each, lo=lo, things="values", control="area"), None)


def _named_options(cfg, kit, tiles):
    if cfg.get("named", "no") not in ("yes", "no"):
        raise ValueError("%s: cfg['named'] is \"yes\" or \"no\", not %r" % (kit, cfg.get("named")))
    return {}, ["named"], tiles


def _strength_options(cfg, kit, tiles):
    v = cfg.get("strength", ["0.3", "0.7"])
    if not isinstance(v, (list, tuple)) or len(v) != 2:
        raise ValueError("%s: cfg['strength'] is two decimals as strings, low then high, such as [\"0.3\", \"0.7\"], "
                         "not %r" % (kit, v))
    lo = _cfg_dec({"strength": v[0]}, kit, "strength", None, Fraction(0), Fraction(1), strict_lo=True)
    hi = _cfg_dec({"strength": v[1]}, kit, "strength", None, Fraction(0), Fraction(1), strict_lo=True)
    if Fraction(lo) >= Fraction(hi):
        raise ValueError("%s: cfg['strength'] goes low then high, and %s is not below %s" % (kit, lo, hi))
    return {"strength": [lo, hi]}, ["strength"], tiles


_XY = [("x", ea.num(lo=-ea.LIMIT)), ("y", ea.num(lo=-ea.LIMIT))]
_SD_RULE = ("A square root is printed to 3 places from the exact rational under it by an integer square root, "
            "rounded half up, so the digits depend on the inputs alone; it is shown without ≈ only when it is exact. ")
_R_RULE = ("r = Sxy ÷ √(Sxx × Syy), where Sxx and Syy are the sums of squared deviations from the means and Sxy the "
           "sum of their products; r² = Sxy² ÷ (Sxx × Syy) is exact. ")

STATS = {
    "prefix": "ast", "fn": "astCompute", "title": "Describing and relating measures", "js": AST_JS,
    "views": {
        "describe": {
            "fields": [("values", alist("Values", ea.num(lo=-ea.LIMIT), lo=2, things="values", control="area"), None)],
            "tiles": [("n", "astN"), ("Mean", "astMean"), ("Median", "astMedian"), ("Mode(s)", "astMode"),
                      ("Minimum", "astMin"), ("Maximum", "astMax"), ("Range", "astRange"),
                      ("Population standard deviation (÷ n)", "astPopSd"),
                      ("Sample standard deviation (÷ (n − 1))", "astSampleSd")],
            "check": None, "options": _named_options,
            "subtitle": "centre and spread of one measure",
            "rules": "The mean is the sum over n; the median is the middle value in order, or the mean of the two "
                     "middle ones; the modes are the values that occur most often, listed in increasing order, and "
                     "there is none when every value occurs equally often. The range is the maximum less the "
                     "minimum. The population variance divides the sum of squared deviations from the mean by n, "
                     "the sample variance by n − 1, and each standard deviation is its square root. " + _SD_RULE,
            "js": AST_VIEW_JS["describe"],
        },
        "pearson": {
            "fields": [("pairs", arec("Pairs (name, x, y)", [("name", _N)] + _XY, unique=True, rows=4, lo=3), None)],
            "tiles": [("n", "astN"), ("Means", "astMeans"), ("Pearson's r", "astR"), ("r² (shared variation)", "astR2"),
                      ("Least-squares line", "astLine"), ("Sign and strength", "astWords")],
            "check": _check_pearson, "options": _strength_options,
            "subtitle": "Pearson's r, r² and the least-squares line",
            "rules": _R_RULE + "The least-squares line has slope b = Sxy ÷ Sxx and intercept a = ȳ − b × x̄, exact. "
                     "Strength is by the lesson's cut-offs (default 0.3 and 0.7, a convention, not the book's): "
                     "|r| below the first is weak, below the second moderate, else strong, compared on the squares "
                     "exactly. " + _SD_RULE + "r is refused when every x or every y is the same.",
            "js": AST_VIEW_JS["pearson"],
        },
        "spurious": {
            "fields": [("series", arec("Series (t, x, y), in order of t", [("t", ea.whole(0, ea.LIMIT))] + _XY,
                                       rows=4, lo=4), None)],
            "tiles": [("Time points", "astN"), ("r of the levels", "astRLevels"),
                      ("r of the first differences", "astRDiffs"), ("The differences' r against the levels'", "astCompare")],
            "check": _check_spurious,
            "subtitle": "two trending series: r of the levels and of the changes",
            "rules": _R_RULE + "The first differences are each value less the one before (n − 1 of them, x and y "
                     "alike). The comparison is of size (|r|, on the squares, exactly) and of sign. An r is not "
                     "defined when every x (or y) is the same, as the differences of a straight-line trend are. "
                     + _SD_RULE,
            "js": AST_VIEW_JS["spurious"],
        },
        "confound": {
            "fields": [("rows", arec("Rows (name, x, y, z: z a group)", [("name", _N)] + _XY + [("z", _N)],
                                     unique=True, rows=4, lo=3), None)],
            "tiles": [("n", "astN"), ("Groups of z", "astGroups"), ("r over all rows", "astR"),
                      ("r within each group", "astWithin"), ("Pooled within-group r", "astPooled"),
                      ("Pooled against overall", "astCompare")],
            "check": None,
            "subtitle": "r over all rows, within each group of a third variable, and pooled",
            "rules": _R_RULE + "Within a group, deviations are from that group's own means; r is computed for a "
                     "group of 3 or more rows whose x and y vary. The pooled within-group r adds every group's Sxx, "
                     "Syy and Sxy (all groups, whatever their size) and takes Sxy ÷ √(Sxx × Syy) of the totals: the "
                     "relation left once each group's own level is taken out. Groups go in the order first given. "
                     + _SD_RULE,
            "js": AST_VIEW_JS["confound"],
        },
    },
}


def _ave_options(cfg, kit, tiles):
    fixed = {"ave_min": _cfg_dec(cfg, kit, "ave_min", "0.5", Fraction(0), Fraction(1)),
             "cr_min": _cfg_dec(cfg, kit, "cr_min", "0.7", Fraction(0), Fraction(1)),
             "loading_min": _cfg_dec(cfg, kit, "loading_min", "0.6", Fraction(0), Fraction(1)),
             "r_max": _cfg_dec(cfg, kit, "r_max", "0.85", Fraction(0), Fraction(1), strict_lo=True)}
    return fixed, list(fixed), tiles


_R1 = ea.num(lo=-1, hi=1)

VALIDITY = {
    "prefix": "avd", "fn": "avdCompute", "title": "Validity of constructs", "js": AVD_JS,
    "views": {
        "matrix": {
            "fields": [("items", arec("Items (item, construct)", [("item", _N), ("construct", _N)], unique=True,
                                      rows=3, lo=3, hi=11), None),
                       ("corr", arec("Correlations (item, item, r), every pair once", [("a", _N), ("b", _N), ("r", _R1)],
                                     rows=5), None)],
            "tiles": [("Items and constructs", "avdItems"), ("Mean correlation within each construct", "avdWithin"),
                      ("Mean correlation across constructs", "avdCross"),
                      ("Items closer to another construct than to their own", "avdFlagged")],
            "check": _check_matrix,
            "subtitle": "do items correlate more with their own construct than with others?",
            "rules": "Every pair of different items is given once, in either order. A construct's within mean is the "
                     "mean r over pairs of its own items; the across mean is over every pair from different "
                     "constructs. For each item, its own mean is its mean r with the other items of its construct, "
                     "and for each other construct its mean r with that construct's items; an item is listed when "
                     "one of those is greater than its own (signed r, compared exactly). An item alone in its "
                     "construct has no own mean and is not tested. Items and constructs go in the order given.",
            "js": AVD_VIEW_JS["matrix"],
        },
        "ave": {
            "fields": [("loadings", arec("Loadings (item, construct, loading)",
                                         [("item", _N), ("construct", _N), ("loading", ea.num(lo=0, hi=1))],
                                         unique=True, rows=4), None),
                       ("between", arec("Between constructs (construct, construct, r); empty for none",
                                        [("c1", _N), ("c2", _N), ("r", _R1)], rows=2, lo=0), "")],
            "tiles": [("AVE (mean squared loading)", "avdAve"), ("Composite reliability", "avdCr"),
                      ("√AVE", "avdRoot"), ("Items loading at or below the threshold", "avdLow"),
                      ("Each pair of constructs", "avdPairs"), ("Tests passed", "avdTests")],
            "check": _check_ave, "options": _ave_options,
            "subtitle": "average variance extracted, composite reliability, and √AVE against r",
            "rules": "For each construct, in the order given: AVE = the mean of its items' squared loadings; CR = "
                     "(Σλ)² ÷ ((Σλ)² + Σ(1 − λ²)), exact. The tests and their default thresholds, the book's: AVE "
                     "above 0.50, CR at least 0.70, each loading above 0.60, and for each pair of constructs, the "
                     "√AVE of each above |r| (tested exactly as AVE > r²) and |r| below 0.85 (as r² < 0.85²). "
                     "Lessons may state other thresholds. " + _SD_RULE,
            "js": AVD_VIEW_JS["ave"],
        },
    },
}

GROUPS = {
    "prefix": "agr", "fn": "agrCompute", "title": "Groups and shares", "js": AGR_JS,
    "views": {
        "likely": {
            "fields": [("rows", arec("Groups (group, n, how many meet the outcome)",
                                     [("group", _N), ("n", ea.whole(1, ea.LIMIT)), ("met", ea.whole(0, ea.LIMIT))],
                                     unique=True, rows=3, lo=2), None),
                       ("first", ea.field("The group compared", _N), None),
                       ("second", ea.field("Against the group", _N), None)],
            "tiles": [("Share meeting the outcome", "agrShares"), ("Times as likely (share ÷ share)", "agrRatio"),
                      ("Difference in percentage points", "agrDiff"), ("Odds ratio (a different figure)", "agrOdds")],
            "check": _check_likely,
            "subtitle": "\"twice as likely\": two shares, their ratio, their difference and the odds ratio",
            "rules": "A group's share is those meeting the outcome over its n, exact. \"Times as likely\" is the "
                     "first group's share over the second's, shown to 2 places; the difference is the first share "
                     "less the second in percentage points, to 1 place. The odds of a group are those meeting it "
                     "over those not; the odds ratio is the first group's odds over the second's, to 2 places. "
                     "The two ratios agree only when the outcome is rare, and neither is defined when it divides "
                     "by 0.",
            "js": AGR_VIEW_JS["likely"],
        },
        "enps": {
            "fields": [("answers", alist("Answers, 0 to 10", ea.whole(0, 10), things="answers", control="area"), None)],
            "tiles": [("Answers n", "agrN"), ("Promoters (9 or 10)", "agrPromoters"), ("Passives (7 or 8)", "agrPassives"),
                      ("Detractors (0 to 6)", "agrDetractors"), ("eNPS", "agrEnps"),
                      ("Answers one point below a higher band", "agrNear")],
            "check": None, "options": _named_options,
            "subtitle": "an employee Net Promoter Score",
            "rules": "Promoters answer 9 or 10, passives 7 or 8, detractors 0 to 6. eNPS = the percentage of "
                     "promoters less the percentage of detractors, from −100 to +100, exact, shown to 1 place when "
                     "it is not whole. An answer of 6 is one point from passive and an 8 one point from promoter; "
                     "moving either up a point raises eNPS by 100 ÷ n.",
            "js": AGR_VIEW_JS["enps"],
        },
        "bias": {
            "fields": [("table", arec("Table (category, early respondents, late respondents)",
                                      [("category", _N), ("early", ea.whole(0, ea.LIMIT)), ("late", ea.whole(0, ea.LIMIT))],
                                      unique=True, rows=3, lo=2), None),
                       ("critical", ea.field("Critical value (the lesson's, for its degrees of freedom and level)",
                                             ea.num(gt=0)), None)],
            "tiles": [("Respondents", "agrN"), ("χ²", "agrChi"), ("Degrees of freedom", "agrDf"),
                      ("χ² above the critical value", "agrExceeds"), ("Cells with an expected count below 5", "agrSmall")],
            "check": _check_bias,
            "subtitle": "a chi-square test of early against late respondents",
            "rules": "A cell's expected count is its row total × its column total ÷ all respondents. χ² = Σ (observed "
                     "− expected)² ÷ expected over every cell, exact, shown to 3 places; degrees of freedom = "
                     "(categories − 1) × (2 − 1). χ² is compared, exactly, with the critical value the lesson states "
                     "for those degrees of freedom and its level: the lab gives no p-value. Cells expected below 5 "
                     "are listed, in the order of the table, early before late.",
            "js": AGR_VIEW_JS["bias"],
        },
    },
}

SAMPLE = {
    "prefix": "asn", "fn": "asnCompute", "title": "A snowball sample", "js": ASN_JS,
    "views": {
        "snowball": {
            "fields": [("people", arec("People (person, referred by, - for a seed, group)",
                                       [("person", _N), ("referred_by", ea.PARENT), ("group", _N)], unique=True,
                                       rows=5), None),
                       ("drop", ea.field("A seed to drop (- for none)", ea.PARENT), "-")],
            "tiles": [("Seeds", "asnSeeds"), ("Waves", "asnWaves"), ("Sample size", "asnSize"),
                      ("Share from each seed's tree", "asnTrees"), ("Share per group", "asnGroups"),
                      ("Lost with the dropped seed", "asnLost"), ("Share per group without it", "asnAfter")],
            "check": _check_snowball,
            "subtitle": "who a snowball sample reaches from its seeds",
            "rules": "A seed is referred by no one (-) and is wave 0; a person referred by someone in wave n is in "
                     "wave n + 1, and belongs to the tree of the seed their chain of referrals starts from. Shares are "
                     "of the whole sample, exact; seeds and groups go in the order first given. Dropping a seed "
                     "removes its whole tree, and the shares after are of the people left. A referral loop that "
                     "reaches no seed is refused.",
            "js": ASN_VIEW_JS["snowball"],
        },
    },
}


def _names_rec(what, key, lo, lo_rest):
    return arec(what, [(key, _N)], _N, "capability", lo_rest, 60, unique=True, rows=3, lo=lo)


CAPABILITY = {
    "prefix": "acp", "fn": "acpCompute", "title": "A capability profile", "js": ACP_JS,
    "views": {
        "profile": {
            "fields": [("capabilities", arec("Capabilities (capability, category)",
                                             [("capability", _N), ("category", _N)], unique=True, rows=4), None),
                       ("teams", _names_rec("Teams (team, then each capability it has in place)", "team", 1, 0), None),
                       ("levels", _names_rec("Maturity model, lowest level first (level, then the capabilities it "
                                             "requires); empty for none", "level", 0, 1), ""),
                       ("teams2", _names_rec("The same teams at a second date (team, then its capabilities); empty "
                                             "for none", "team", 0, 0), "")],
            "tiles": [("Teams", "acpTeams"), ("In place, of all capabilities", "acpOverall"),
                      ("In place by category", "acpCategories"), ("Maturity level reached", "acpLevel"),
                      ("In place above that level (what the level hides)", "acpHidden"),
                      ("Added (and dropped) by the second date", "acpAdded"),
                      ("The capability fewest teams have", "acpFewest")],
            "check": _check_profile,
            "subtitle": "capabilities in place by category, and what a maturity level hides",
            "rules": "A team lists the capabilities it has in place; the rest are not. Categories and capabilities go "
                     "in the order given. With a maturity model, a team reaches the highest level whose required "
                     "capabilities, and every lower level's, are all in place (none when the first level's are not); "
                     "the capabilities it has that a higher level requires are listed as what the level hides. A "
                     "capability belongs to at most one level; the level tile names it and its place (level 2 of 3). With a second date, each team named there is compared "
                     "with itself: added, then dropped. The fewest is the capability in place in the fewest teams; "
                     "ties go in the order given, the first 3 named and the rest counted (the table lists all). "
                     "Names are one word each: write a multiword capability with hyphens (trunk-based-development).",
            "js": ACP_VIEW_JS["profile"],
        },
    },
}

SPECS = {"likert": LIKERT, "stats": STATS, "validity": VALIDITY, "groups": GROUPS, "sample": SAMPLE,
         "capability": CAPABILITY}


def _with_field(spec, view, key, field):
    views = dict(spec["views"])
    views[view] = dict(views[view], fields=[field if f[0] == key else f for f in views[view]["fields"]])
    return dict(spec, views=views)


def stats_lab(cfg):
    spec = STATS
    if cfg.get("view", "describe") == "describe":
        spec = _with_field(spec, "describe", "values", _named_values(
            cfg, "value", "values", ea.num(lo=-ea.LIMIT), "Values", "Values (name, value)", 2))
    return mode_lab(cfg, "stats", spec)


def groups_lab(cfg):
    spec = GROUPS
    if cfg.get("view", "likely") == "enps":
        spec = _with_field(spec, "enps", "answers", _named_values(
            cfg, "answer", "answers", ea.whole(0, 10), "Answers, 0 to 10", "Answers (name, answer 0 to 10)", 1))
    return mode_lab(cfg, "groups", spec)


MODES = {"likert": lambda cfg: mode_lab(cfg, "likert", LIKERT),
         "stats": stats_lab,
         "validity": lambda cfg: mode_lab(cfg, "validity", VALIDITY),
         "groups": groups_lab,
         "sample": lambda cfg: mode_lab(cfg, "sample", SAMPLE),
         "capability": lambda cfg: mode_lab(cfg, "capability", CAPABILITY)}

__all__ = ["MODES", "SPECS"]
