"""Course 1 of Operations Research: linear programming models.

Six modes, ten lessons. The split is the one the course note fixes: `model`
carries the five modelling lessons behind a required ``preset`` key (``mix``,
``diet``, ``blend``, ``multiperiod``), and the two that share ``mix`` are then
separated by a second required key, ``view``. The remaining five lessons take
one mode each -- ``reform``, ``goal``, ``standard``, ``basic``, ``convex``.

WHAT IS BORROWED RATHER THAN REBUILT, because this kit sits on top of two
engines that already ship and a third implementation of a simplex is how two
pages come to disagree:

  * two variables are ``algebra_systems``' work and not this file's.
    ``Ccorners`` enumerates the corners, ``FMfeasible`` decides emptiness,
    ``Cunbounded``/``Cgrows``/``Crec`` decide whether an objective runs away
    along a recession direction, and ``Cholds`` tests one point against one
    half-plane.  FEAS_JS eliminates ``y`` by Fourier-Motzkin and is TWO
    VARIABLE ONLY, so the split is firm and mechanical: two variables by
    corners, three or more by the engine.
  * three or more variables are ``or_core``'s.  ``stdForm`` names every slack,
    surplus and artificial and says what it measures; ``lpSolve`` runs Phase I,
    hands its tableau to Phase II and reports ``optimal``/``unbounded``/
    ``infeasible``; ``tabRead`` reads the basic feasible solution back.
  * the row reduction in ``basic`` is ``Mrref`` with its narrated ``ops``, and
    the count of bases is ``comb`` from ``counting.BIGINT_JS``.
  * what a reader TYPES is parsed by ``Xparse`` and evaluated exactly by
    ``Xeval``, so ``9/2`` and ``3 + 1/2`` are the same candidate point and
    neither becomes 4.5.

WHAT IS NEW is LP_JS below: the dispatch between those two solvers, the
constraint-by-constraint candidate check, the slack table, the share
arithmetic, the lexicographic goal driver, the basis enumeration and the exact
segment interval the convexity lesson needs.  All of it is top-level functions
in a raw string, so scripts/mathcheck.js runs the shipped source.

NOTHING ROUNDS.  Every figure on all ten lessons is a ratio of integers over
BigInt; the only floats are pixel coordinates inside ``Plot``.
"""

from .algebra_core import EXPR_JS, PLOT_JS, RATIONAL_JS
from .algebra_systems import EXACT_JS, FEAS_JS, FORMAT_JS, LINEAR_JS, MATRIX_JS
from .common import Lab, cfg_literal
from .counting import BIGINT_JS
from .or_core import ORFMT_JS, PHASE_JS, TABLEAU_JS

LP_JS = r"""
  /* ================= the two solvers, and which one answers ================

     A lesson-sized linear programme in two variables has a picture, and the
     picture is the evidence: Ccorners enumerates every crossing of two
     boundary lines and keeps the ones that satisfy every constraint.  Above
     two variables there is no picture and FEAS_JS cannot be extended -- it
     eliminates y by Fourier-Motzkin and there is no second y -- so the engine
     takes over.  Both routes answer the SAME question and this file makes the
     choice once, here, rather than in six redraw functions. */

  /* The half-plane list FEAS_JS wants, sign restrictions included as
     constraints rather than assumed.  x >= 0 is a constraint: dropping it
     changes the answer, and the candidate check below lists it in the same
     shape as the rest for exactly that reason. */
  function lpHalfPlanes(model) {
    var cons = [], free = model.free || [], j;
    model.cons.forEach(function (k, i) {
      Cfromrow({ c: [k.a[0], k.a[1]], b: k.b, rel: k.rel || 'le',
                 src: k.name || ('row ' + (i + 1)) })
        .forEach(function (h) { cons.push(h); });
    });
    for (j = 0; j < 2; j += 1) {
      if (free.indexOf(j) >= 0) continue;
      cons.push(Cnew(j === 0 ? R(-1n, 1n) : R0, j === 1 ? R(-1n, 1n) : R0, R0, false,
                     model.names[j] + ' >= 0'));
    }
    return cons;
  }

  function lpObjAt(model, x) {
    var s = R0, j;
    for (j = 0; j < model.obj.length; j += 1) s = Radd(s, Rmul(model.obj[j], x[j]));
    return s;
  }

  /* Two variables: every corner, the objective at each, and the winner.  The
     unbounded verdict is Cgrows on the objective direction (negated for a
     minimisation), which DECIDES the question rather than sampling it. */
  function lpByCorners(model) {
    var cons = lpHalfPlanes(model);
    var feas = FMfeasible(cons);
    var minimise = model.max === false;
    var ox = minimise ? Rneg(model.obj[0]) : model.obj[0];
    var oy = minimise ? Rneg(model.obj[1]) : model.obj[1];
    if (!feas.feasible) {
      return { method: 'corners', status: 'infeasible', cons: cons, feas: feas,
               corners: [], x: null, z: null, best: -1, runs: false,
               unboundedRegion: false };
    }
    var runs = Cgrows(cons, ox, oy);
    var raw = Ccorners(cons), corners = [], i;
    for (i = 0; i < raw.length; i += 1) {
      var p = [raw[i].x, raw[i].y];
      corners.push({ x: raw[i].x, y: raw[i].y, inRegion: raw[i].inRegion,
                     from: raw[i].from, z: lpObjAt(model, p) });
    }
    var best = -1;
    for (i = 0; i < corners.length; i += 1) {
      if (!corners[i].inRegion) continue;
      if (best < 0) { best = i; continue; }
      var c = Rcmp(corners[i].z, corners[best].z);
      if (minimise ? c < 0 : c > 0) best = i;
    }
    var ties = [];
    for (i = 0; i < corners.length; i += 1) {
      if (corners[i].inRegion && best >= 0 && Requ(corners[i].z, corners[best].z)) ties.push(i);
    }
    /* When the objective runs away there is no best corner, and a corner that
       merely happens to be the best of the ones drawn is not one: reporting it
       would put a finite number under a page that has just said there is none.
       The corner list is still returned, because the picture still has corners. */
    var status = runs ? 'unbounded' : (best < 0 ? 'infeasible' : 'optimal');
    return { method: 'corners', status: status,
             cons: cons, feas: feas, corners: corners,
             best: status === 'optimal' ? best : -1, ties: ties,
             x: status === 'optimal' ? [corners[best].x, corners[best].y] : null,
             z: status === 'optimal' ? corners[best].z : null,
             runs: runs, unboundedRegion: Cunbounded(cons) };
  }

  /* Three or more: or_core's Phase I, Phase II and the read-back.  The status
     names are the same strings the corner route uses, so a caller never has to
     know which solver answered. */
  function lpByEngine(model) {
    var sol = lpSolve(model);
    var st = sol.status === 'infeasible' ? 'infeasible'
      : (sol.status === 'unbounded' ? 'unbounded'
         : (sol.status === 'optimal' ? 'optimal' : sol.status));
    /* An unbounded run's tableau still holds a number, and printing it would
       be printing the last point the search happened to stand on as though it
       were an optimum.  There is no optimal value, so there is none here. */
    return { method: 'simplex', status: st, sol: sol, std: sol.std,
             x: st === 'optimal' ? sol.x : null,
             z: st === 'optimal' ? sol.zOrig : null, corners: [], best: -1 };
  }

  /* The dispatch itself.  TWO VARIABLES BY CORNERS, THREE OR MORE BY THE
     ENGINE -- said once, in one place. */
  function lpSolveModel(model) {
    return model.obj.length === 2 ? lpByCorners(model) : lpByEngine(model);
  }

  /* ================= what the page prints about a model =================== */

  function lpSenseWord(model) { return model.max === false ? 'minimise' : 'maximise'; }
  function lpObjText(model) {
    return lpSenseWord(model) + '  ' + Ltext(model.obj, model.names);
  }
  function lpRowText(row, names) {
    return Ltext(row.a, names) + ' ' + relhtml(row.rel || 'le') + ' ' + Rtext(row.b);
  }
  function lpSignText(model) {
    var free = model.free || [], kept = [], j;
    for (j = 0; j < model.names.length; j += 1) if (free.indexOf(j) < 0) kept.push(model.names[j]);
    if (!kept.length) return 'every variable is free';
    return kept.join(', ') + ' &gt;= 0';
  }

  /* ================= a candidate point, constraint by constraint ==========

     The misconception this answers is that a model is checked by "does the
     solver like it".  Each row is reported separately, with its own left-hand
     value, its own right-hand value and the signed difference between them, so
     a failure names the constraint that failed rather than the model.  The
     sign restrictions are in the same list and the same shape. */
  function lpCandidate(model, point) {
    var rows = [], free = model.free || [], i, j;
    for (i = 0; i < model.cons.length; i += 1) {
      var k = model.cons[i], lhs = R0;
      for (j = 0; j < model.obj.length; j += 1) lhs = Radd(lhs, Rmul(k.a[j], point[j]));
      var rel = k.rel || 'le', diff = Rsub(lhs, k.b);
      var ok = rel === 'le' ? Rsign(diff) <= 0 : (rel === 'ge' ? Rsign(diff) >= 0 : Rzero(diff));
      rows.push({ kind: 'constraint', name: k.name || ('row ' + (i + 1)),
                  text: lpRowText(k, model.names), lhs: lhs, rhs: k.b, diff: diff,
                  rel: rel, ok: ok });
    }
    for (j = 0; j < model.names.length; j += 1) {
      if (free.indexOf(j) >= 0) continue;
      rows.push({ kind: 'sign', name: model.names[j] + ' not negative',
                  text: model.names[j] + ' &gt;= 0', lhs: point[j], rhs: R0,
                  diff: point[j], rel: 'ge', ok: Rsign(point[j]) >= 0 });
    }
    var bad = [];
    for (i = 0; i < rows.length; i += 1) if (!rows[i].ok) bad.push(i);
    return { rows: rows, ok: bad.length === 0, failed: bad, z: lpObjAt(model, point) };
  }

  /* ================= slack and surplus at a point =========================

     Named by or_core's stdForm, which is the function that knows a <= row gets
     a slack ADDED and a >= row gets a surplus SUBTRACTED, and which carries the
     sentence saying what each one measures in the situation. */
  function lpSlackRows(model, x) {
    var std = stdForm(model), out = [], i, j;
    for (i = 0; i < model.cons.length; i += 1) {
      var k = model.cons[i], lhs = R0;
      for (j = 0; j < model.obj.length; j += 1) lhs = Radd(lhs, Rmul(k.a[j], x[j]));
      var rel = k.rel || 'le';
      var value = rel === 'le' ? Rsub(k.b, lhs) : Rsub(lhs, k.b);
      var col = std.rowSlack[i];
      out.push({ row: i, name: k.name || ('row ' + (i + 1)), rel: rel,
                 lhs: lhs, rhs: k.b, value: value, tight: Rzero(value),
                 varName: col >= 0 ? std.names[col] : '&mdash;',
                 kind: col >= 0 ? std.kinds[col] : 'equality',
                 measures: col >= 0 ? std.sentences[col]
                   : 'an equality row carries no slack at all: it is tight wherever it holds' });
    }
    return { std: std, rows: out };
  }

  /* ================= the recession-cone certificate =======================

     "The region is unbounded, therefore the problem is unbounded" is the
     misconception, and the answer is that unboundedness is a property of the
     OBJECTIVE along the region's recession directions.  Crec drops every
     constant, which turns the constraints into a cone; Cholds then tests a
     named direction against that cone, and Cgrows decides the same question
     over ALL directions at once rather than over the named few. */
  function lpRecession(model, dirs) {
    var cons = lpHalfPlanes(model), rec = Crec(cons), rows = [], i, t;
    for (i = 0; i < dirs.length; i += 1) {
      var d = dirs[i], isRec = true;
      for (t = 0; t < rec.length; t += 1) {
        if (!Cholds(rec[t], d.d[0], d.d[1])) { isRec = false; break; }
      }
      var change = Radd(Rmul(model.obj[0], d.d[0]), Rmul(model.obj[1], d.d[1]));
      rows.push({ name: d.name, d: d.d, recession: isRec, change: change });
    }
    var minimise = model.max === false;
    var runs = Cgrows(cons, minimise ? Rneg(model.obj[0]) : model.obj[0],
                            minimise ? Rneg(model.obj[1]) : model.obj[1]);
    return { rows: rows, runs: runs, minimise: minimise,
             unboundedRegion: Cunbounded(cons), feasible: FMfeasible(cons).feasible };
  }

"""


BLEND_JS = r"""
  /* ================= blending: the share, cleared and achieved ============ */

  /* "at least t of the blend is component i" is  x_i >= t * (x_1 + ... + x_n),
     which is linear once the denominator is cleared -- and clearing is legal
     only because the total is a non-negative quantity.  The cleared row is
     (1 - t) x_i - t * (the rest) >= 0. */
  function lpShareRow(i, t, n, atLeast, name) {
    var a = [], j;
    for (j = 0; j < n; j += 1) a.push(j === i ? Rsub(R1, t) : Rneg(t));
    return { a: a, rel: atLeast ? 'ge' : 'le', b: R0, name: name };
  }
  function lpShares(x) {
    var total = R0, i, shares = [];
    for (i = 0; i < x.length; i += 1) total = Radd(total, x[i]);
    for (i = 0; i < x.length; i += 1) shares.push(Rzero(total) ? null : Rdiv(x[i], total));
    return { total: total, shares: shares };
  }
  /* The move this lesson DECLINES.  x_i / x_j >= t clears to
     x_i - t x_j >= 0 only if x_j is known positive; if the feasible set
     contains a point with x_j = 0 the two statements are different, and the
     test for that is a linear programme, not an opinion: add x_j <= 0 and ask
     whether anything is left. */
  function lpDenominatorCanVanish(model, j) {
    var probe = { max: model.max, names: model.names.slice(), obj: model.obj.slice(),
                  cons: model.cons.slice(), free: model.free };
    var a = [], q;
    for (q = 0; q < model.obj.length; q += 1) a.push(q === j ? R1 : R0);
    probe.cons = probe.cons.concat([{ a: a, rel: 'le', b: R0, name: model.names[j] + ' driven to zero' }]);
    var res = lpSolveModel(probe);
    return { canVanish: res.status !== 'infeasible', probe: probe, result: res };
  }

  /* ================= multiperiod planning ================================= */

  /* One balance equation per period, I_t = I_{t-1} + P_t - D_t, written as
     P_t + I_{t-1} - I_t = D_t.  The inventory variable is the thing that
     carries the link, so it is a variable and not a formula. */
  function lpBalanceModel(demand, cap, prod, hold, start) {
    var T = demand.length, names = [], obj = [], cons = [], t, q;
    for (t = 0; t < T; t += 1) names.push('P' + (t + 1));
    for (t = 0; t < T; t += 1) names.push('I' + (t + 1));
    for (t = 0; t < T; t += 1) obj.push(prod[t]);
    for (t = 0; t < T; t += 1) obj.push(hold);
    for (t = 0; t < T; t += 1) {
      var a = [];
      for (q = 0; q < 2 * T; q += 1) a.push(R0);
      a[t] = R1;                                   /* produced in period t */
      if (t > 0) a[T + t - 1] = R1;                /* carried in           */
      a[T + t] = R(-1n, 1n);                       /* carried out          */
      cons.push({ a: a, rel: 'eq', b: Rsub(demand[t], t === 0 ? start : R0),
                  name: 'balance in period ' + (t + 1) });
    }
    for (t = 0; t < T; t += 1) {
      var c = [];
      for (q = 0; q < 2 * T; q += 1) c.push(q === t ? R1 : R0);
      cons.push({ a: c, rel: 'le', b: cap, name: 'capacity in period ' + (t + 1) });
    }
    return { max: false, names: names, obj: obj, cons: cons };
  }

  /* The aggregate constraint the misconception offers instead: total
     production at least total demand, with no inventory variable at all. */
  function lpAggregateModel(demand, cap, prod, hold, start) {
    var T = demand.length, names = [], obj = [], cons = [], t, q, need = Rneg(start);
    for (t = 0; t < T; t += 1) { names.push('P' + (t + 1)); obj.push(prod[t]); need = Radd(need, demand[t]); }
    var a = [];
    for (q = 0; q < T; q += 1) a.push(R1);
    cons.push({ a: a, rel: 'ge', b: need, name: 'total production covers total demand' });
    for (t = 0; t < T; t += 1) {
      var c = [];
      for (q = 0; q < T; q += 1) c.push(q === t ? R1 : R0);
      cons.push({ a: c, rel: 'le', b: cap, name: 'capacity in period ' + (t + 1) });
    }
    return { max: false, names: names, obj: obj, cons: cons };
  }

  /* What the aggregate plan actually does to the reader, period by period:
     running stock, and the demand it fails to meet. */
  function lpRunStock(plan, demand, start) {
    var stock = start, rows = [], t, short_ = R0;
    for (t = 0; t < demand.length; t += 1) {
      var before = Radd(stock, plan[t]);
      var after = Rsub(before, demand[t]);
      var unmet = Rsign(after) < 0 ? Rneg(after) : R0;
      short_ = Radd(short_, unmet);
      rows.push({ period: t + 1, produced: plan[t], available: before, demand: demand[t],
                  closing: Rsign(after) < 0 ? R0 : after, unmet: unmet });
      stock = Rsign(after) < 0 ? R0 : after;
    }
    return { rows: rows, unmet: short_, met: Rzero(short_) };
  }

"""


GOAL_JS = r"""
  /* ================= goal programming ===================================

     A target is a constraint carrying two deviation variables, of which only
     the one you mind is penalised.  Priorities are then solved
     LEXICOGRAPHICALLY: a preemptive goal programme is a SEQUENCE of linear
     programmes, each freezing the previous level's achieved deviation as a
     constraint, and the loop below is that sequence.  The solve inside it is
     or_core's; the loop is the lesson. */
  function goalNames(base, goals) {
    var names = base.names.slice(), j;
    for (j = 0; j < goals.length; j += 1) {
      names.push('u' + (j + 1));                   /* under-achievement, d-  */
      names.push('o' + (j + 1));                   /* over-achievement,  d+  */
    }
    return names;
  }
  function goalPenalty(base, goals, j) {
    var n = base.names.length;
    return goals[j].mind === 'over' ? n + 2 * j + 1 : n + 2 * j;
  }
  function goalBuild(base, goals, obj, frozen) {
    var n = base.names.length, G = goals.length, N = n + 2 * G, cons = [], j, q;
    base.cons.forEach(function (k) {
      var a = k.a.slice();
      while (a.length < N) a.push(R0);
      cons.push({ a: a, rel: k.rel || 'le', b: k.b, name: k.name });
    });
    for (j = 0; j < G; j += 1) {
      var a2 = [];
      for (q = 0; q < N; q += 1) a2.push(R0);
      for (q = 0; q < n; q += 1) a2[q] = goals[j].a[q];
      a2[n + 2 * j] = R1;
      a2[n + 2 * j + 1] = R(-1n, 1n);
      cons.push({ a: a2, rel: 'eq', b: goals[j].target, name: goals[j].name });
    }
    (frozen || []).forEach(function (f) { cons.push(f); });
    return { max: false, names: goalNames(base, goals), obj: obj, cons: cons };
  }
  function goalZero(base, goals) {
    var out = [], q, N = base.names.length + 2 * goals.length;
    for (q = 0; q < N; q += 1) out.push(R0);
    return out;
  }
  function goalLexicographic(base, goals, order) {
    var levels = [], frozen = [], k;
    for (k = 0; k < order.length; k += 1) {
      var g = order[k];
      var obj = goalZero(base, goals);
      obj[goalPenalty(base, goals, g)] = R1;
      var model = goalBuild(base, goals, obj, frozen);
      var res = lpSolveModel(model);
      var achieved = res.x === null ? null : res.x[goalPenalty(base, goals, g)];
      levels.push({ level: k + 1, goal: g, model: model, result: res,
                    achieved: achieved, frozen: frozen.slice(),
                    met: achieved !== null && Rzero(achieved) });
      if (achieved === null) break;
      var fa = goalZero(base, goals);
      fa[goalPenalty(base, goals, g)] = R1;
      frozen = frozen.concat([{ a: fa, rel: 'eq', b: achieved,
                                name: goals[g].name + ' held at ' + Rtext(achieved) }]);
    }
    return { levels: levels, order: order.slice(),
             final: levels.length ? levels[levels.length - 1].result : null };
  }
  /* The other way this goes wrong, and it is silent: three goals in three
     different units added into one weighted objective. */
  function goalWeighted(base, goals, weights) {
    var obj = goalZero(base, goals), j;
    for (j = 0; j < goals.length; j += 1) obj[goalPenalty(base, goals, j)] = weights[j];
    var model = goalBuild(base, goals, obj, []);
    return { model: model, result: lpSolveModel(model) };
  }
  function goalDeviations(base, goals, x) {
    var out = [], j;
    for (j = 0; j < goals.length; j += 1) {
      var n = base.names.length;
      out.push({ goal: j, under: x === null ? null : x[n + 2 * j],
                 over: x === null ? null : x[n + 2 * j + 1],
                 penalised: goals[j].mind === 'over' ? 'o' + (j + 1) : 'u' + (j + 1) });
    }
    return out;
  }

"""


BASIS_JS = r"""
  /* ================= basic solutions ======================================

     With m equations in n + m variables, choosing which n variables are zero
     and solving the rest is a basic solution.  Every one of them is solved by
     Mrref on the basis columns augmented with b -- the same row reduction the
     reader already met -- and classified from the answer rather than from the
     picture. */
  function lpChoose(N, m) {
    var out = [];
    (function rec(start, chosen) {
      if (chosen.length === m) { out.push(chosen.slice()); return; }
      for (var j = start; j < N; j += 1) { chosen.push(j); rec(j + 1, chosen); chosen.pop(); }
    })(0, []);
    return out;
  }
  /* The line a column standing at zero puts the point on: a decision column
     gives an axis, a slack column gives its row's boundary.  Two nonbasic
     columns are therefore two lines, and a singular basis is exactly two
     PARALLEL lines -- which is the sentence the lesson wants instead of
     "the matrix was singular". */
  function lpColumnLine(std, model, j) {
    if (j < std.nd) {
      var a = [], q;
      for (q = 0; q < 2; q += 1) a.push(q === j ? R1 : R0);
      return { a: a, b: R0, text: model.names[j] + ' = 0', name: model.names[j] + ' = 0' };
    }
    var row = -1, i;
    for (i = 0; i < std.m; i += 1) if (std.rowSlack[i] === j) row = i;
    if (row < 0) return { a: [R0, R0], b: R0, text: 'no line', name: 'no line' };
    return { a: model.cons[row].a.slice(), b: model.cons[row].b,
             text: Ltext(model.cons[row].a, model.names) + ' = ' + Rtext(model.cons[row].b),
             name: model.cons[row].name || ('row ' + (row + 1)) };
  }
  function lpBasisSolve(std, cols) {
    var aug = [], i, k;
    for (i = 0; i < std.m; i += 1) {
      var row = [];
      for (k = 0; k < cols.length; k += 1) row.push(std.A[i][cols[k]]);
      row.push(std.b[i]);
      aug.push(row);
    }
    var red = Mrref(aug, { cols: std.m });
    var singular = red.rank < std.m;
    var x = [], values = [];
    for (k = 0; k < std.n; k += 1) x.push(R0);
    if (!singular) {
      for (i = 0; i < std.m; i += 1) {
        x[cols[red.pivots[i]]] = red.M[i][std.m];
        values.push({ col: cols[red.pivots[i]], value: red.M[i][std.m] });
      }
    }
    var negative = [], zero = [];
    if (!singular) {
      for (k = 0; k < values.length; k += 1) {
        if (Rsign(values[k].value) < 0) negative.push(values[k].col);
        if (Rzero(values[k].value)) zero.push(values[k].col);
      }
    }
    return { cols: cols.slice(), aug: aug, red: red, singular: singular, x: x,
             values: values, negative: negative, degenerate: zero.length > 0,
             feasible: !singular && negative.length === 0,
             kind: singular ? 'singular'
               : (negative.length ? 'infeasible' : (zero.length ? 'degenerate' : 'feasible')) };
  }
  function lpBasisTable(model) {
    var std = stdForm(model);
    var bases = lpChoose(std.n, std.m), out = [], i, j;
    var cons = lpHalfPlanes(model), corners = Ccorners(cons);
    for (i = 0; i < bases.length; i += 1) {
      var sol = lpBasisSolve(std, bases[i]);
      var nonbasic = [];
      for (j = 0; j < std.n; j += 1) if (bases[i].indexOf(j) < 0) nonbasic.push(j);
      var lines = nonbasic.map(function (q) { return lpColumnLine(std, model, q); });
      var det = lines.length === 2
        ? Rsub(Rmul(lines[0].a[0], lines[1].a[1]), Rmul(lines[0].a[1], lines[1].a[0])) : R1;
      var at = -1;
      if (!sol.singular) {
        for (j = 0; j < corners.length; j += 1) {
          if (Requ(corners[j].x, sol.x[0]) && Requ(corners[j].y, sol.x[1])) { at = j; break; }
        }
      }
      out.push({ basis: bases[i], nonbasic: nonbasic, lines: lines, parallel: Rzero(det),
                 solve: sol, corner: at, z: sol.singular ? null : lpObjAt(model, [sol.x[0], sol.x[1]]) });
    }
    return { std: std, rows: out, corners: corners, cons: cons,
             count: comb(std.n, std.m) };
  }

"""


SEG_JS = r"""
  /* ================= convexity ============================================

     The segment between two points, the objective along it, and the exact
     interval of t on which the segment lies inside a set of half-planes.  The
     interval is a DECISION, not a sample: a . (p + t(q - p)) <= c is one
     linear inequality in t, so the whole family collapses to one lo and one
     hi, and a union of two such intervals either covers [0, 1] or does not. */
  function segPoint(p, q, t) {
    var out = [], i;
    for (i = 0; i < p.length; i += 1) out.push(Radd(p[i], Rmul(t, Rsub(q[i], p[i]))));
    return out;
  }
  function segSamples(p, q, obj, k) {
    var rows = [], i, prev = null;
    for (i = 0; i <= k; i += 1) {
      var t = R(BigInt(i), BigInt(k));
      var z = segPoint(p, q, t);
      var v = R0, j;
      for (j = 0; j < obj.length; j += 1) v = Radd(v, Rmul(obj[j], z[j]));
      rows.push({ t: t, point: z, value: v, diff: prev === null ? null : Rsub(v, prev) });
      prev = v;
    }
    var constant = true;
    for (i = 2; i < rows.length; i += 1) if (!Requ(rows[i].diff, rows[1].diff)) constant = false;
    return { rows: rows, constant: constant, step: rows.length > 1 ? rows[1].diff : null };
  }
  function segInterval(cons, p, q) {
    var lo = R0, hi = R1, i, blocked = null;
    for (i = 0; i < cons.length; i += 1) {
      var k = cons[i];
      var atP = Radd(Rmul(k.a, p[0]), Rmul(k.b, p[1]));
      var atQ = Radd(Rmul(k.a, q[0]), Rmul(k.b, q[1]));
      var m = Rsub(atQ, atP), rhs = Rsub(k.c, atP);
      if (Rzero(m)) {
        if (Rsign(rhs) < 0) { blocked = i; lo = R1; hi = R0; break; }
        continue;
      }
      var bound = Rdiv(rhs, m);
      if (Rsign(m) > 0) { if (Rcmp(bound, hi) < 0) hi = bound; }
      else { if (Rcmp(bound, lo) > 0) lo = bound; }
    }
    return { lo: lo, hi: hi, empty: Rcmp(lo, hi) > 0, blocked: blocked };
  }
  /* Does a union of intervals cover the whole segment?  Sorted by left end,
     then swept: the reach advances only where the next interval starts at or
     before it. */
  function segCovered(intervals) {
    var live = intervals.filter(function (I) { return !I.empty; });
    live.sort(function (a, b) { return Rcmp(a.lo, b.lo); });
    var reach = R0, i, gapAt = null;
    for (i = 0; i < live.length; i += 1) {
      if (Rcmp(live[i].lo, reach) > 0) { gapAt = live[i].lo; break; }
      if (Rcmp(live[i].hi, reach) > 0) reach = live[i].hi;
    }
    return { covered: gapAt === null && Rcmp(reach, R1) >= 0,
             reach: reach, gapAt: gapAt };
  }
  function setHolds(cons, x, y) {
    var i;
    for (i = 0; i < cons.length; i += 1) if (!Cholds(cons[i], x, y)) return false;
    return true;
  }
  /* The best corner of one convex block, which is what makes a local optimum
     on a UNION of blocks a thing a reader can see: each block has its own, and
     only one of them is global. */
  function setBest(cons, obj, maximise) {
    var raw = Ccorners(cons), best = -1, i, out = [];
    for (i = 0; i < raw.length; i += 1) {
      var v = Radd(Rmul(obj[0], raw[i].x), Rmul(obj[1], raw[i].y));
      out.push({ x: raw[i].x, y: raw[i].y, z: v, inRegion: raw[i].inRegion });
      if (!raw[i].inRegion) continue;
      if (best < 0) { best = i; continue; }
      var c = Rcmp(v, out[best].z);
      if (maximise ? c > 0 : c < 0) best = i;
    }
    return { corners: out, best: best,
             x: best < 0 ? null : [out[best].x, out[best].y],
             z: best < 0 ? null : out[best].z };
  }

"""


REFORM_JS = r"""
  /* ================= reformulations ======================================

     ALL FOUR rewrites on this lesson are one object: an objective that is the
     max (or the min) of a list of linear pieces.

       a free variable        one piece
       |x| + (linear)         max of  x + ...  and  -x + ...
       max(p1, p2)            max of the two pieces, by definition
       a two-segment cost     max of the two segment lines when the second
                              price is the higher -- and MIN of them when it is
                              not, which is the convexity condition stated
                              rather than assumed

     The original is then optimised by CORNER ENUMERATION, and the corners are
     Ccorners' on each sub-region where one piece is the selected one: on that
     sub-region the objective is linear, so its optimum over it is at one of
     its corners, and the optimum over the whole region is the best of them.
     That is a proof, not a sampling. */
  function pieceValue(pieces, x, y, combine) {
    var best = null, i;
    for (i = 0; i < pieces.length; i += 1) {
      var v = Radd(Radd(Rmul(pieces[i].a[0], x), Rmul(pieces[i].a[1], y)), pieces[i].k);
      if (best === null) best = v;
      else if (combine === 'min' ? Rcmp(v, best) < 0 : Rcmp(v, best) > 0) best = v;
    }
    return best;
  }
  function pieceRegion(cons, pieces, i, combine) {
    var out = cons.slice(), j;
    for (j = 0; j < pieces.length; j += 1) {
      if (j === i) continue;
      /* piece i is the selected one here: for a max, piece j <= piece i. */
      var lo = combine === 'min' ? pieces[j] : pieces[i];
      var hi = combine === 'min' ? pieces[i] : pieces[j];
      out.push(Cnew(Rsub(hi.a[0], lo.a[0]), Rsub(hi.a[1], lo.a[1]),
                    Rsub(lo.k, hi.k), false, 'piece ' + (i + 1) + ' is the one that counts'));
    }
    return out;
  }
  function pieceOptimum(cons, pieces, combine, maximise) {
    var best = null, bestAt = null, regions = [], i, j;
    for (i = 0; i < pieces.length; i += 1) {
      var sub = pieceRegion(cons, pieces, i, combine);
      var feas = FMfeasible(sub);
      var raw = feas.feasible ? Ccorners(sub) : [];
      var runs = feas.feasible && Cgrows(sub, maximise ? pieces[i].a[0] : Rneg(pieces[i].a[0]),
                                              maximise ? pieces[i].a[1] : Rneg(pieces[i].a[1]));
      var pts = [];
      for (j = 0; j < raw.length; j += 1) {
        if (!raw[j].inRegion) continue;
        var v = pieceValue(pieces, raw[j].x, raw[j].y, combine);
        pts.push({ x: raw[j].x, y: raw[j].y, value: v });
        if (best === null || (maximise ? Rcmp(v, best) > 0 : Rcmp(v, best) < 0)) {
          best = v; bestAt = [raw[j].x, raw[j].y];
        }
      }
      regions.push({ piece: i, feasible: feas.feasible, runs: runs, points: pts });
    }
    var unbounded = regions.some(function (r) { return r.runs; });
    return { regions: regions, value: unbounded ? null : best, at: unbounded ? null : bestAt,
             unbounded: unbounded, status: unbounded ? 'unbounded' : (best === null ? 'infeasible' : 'optimal') };
  }
  /* The epigraph rewrite: one auxiliary variable t, one row per piece saying
     t >= that piece, and t minimised.  It is legal exactly when the direction
     of optimisation forces t down onto the largest piece -- so MINIMISING a
     max is the legal case and maximising it is not, and the lab shows the
     difference as two numbers rather than as a warning. */
  function epigraphModel(cons2, pieces, names, maximise) {
    var n = names.length, cons = [], i, q;
    cons2.forEach(function (k) {
      var a = k.a.slice();
      while (a.length < n + 1) a.push(R0);
      cons.push({ a: a, rel: k.rel || 'le', b: k.b, name: k.name });
    });
    for (i = 0; i < pieces.length; i += 1) {
      var a2 = [];
      for (q = 0; q < n; q += 1) a2.push(Rneg(pieces[i].a[q]));
      a2.push(R1);
      cons.push({ a: a2, rel: 'ge', b: pieces[i].k, name: 't is at least piece ' + (i + 1) });
    }
    var obj = [];
    for (q = 0; q < n; q += 1) obj.push(R0);
    obj.push(R1);
    return { max: maximise, names: names.concat(['t']), obj: obj, cons: cons, free: [n] };
  }
  /* The segment rewrite: a cost quoted in two price bands is modelled by
     splitting the quantity into one variable per band, u <= the break and
     v >= 0, and pricing them separately.  The optimiser fills the CHEAPER band
     first, which is the band the lesson intends only when the later band costs
     more -- so convexity is the condition, and where it fails this model
     reports a cost no actual quantity achieves. */
  function segmentModel(cons2, names, idx, brk, p1, p2, rest, maximise) {
    var n = names.length, cons = [], q, i;
    var expand = function (a) {
      var out = [];
      for (q = 0; q < n; q += 1) out.push(a[q]);
      out.push(a[idx]);                  /* the second band, same coefficient */
      return out;
    };
    cons2.forEach(function (k) { cons.push({ a: expand(k.a), rel: k.rel || 'le', b: k.b, name: k.name }); });
    var cap = [];
    for (q = 0; q <= n; q += 1) cap.push(q === idx ? R1 : R0);
    cons.push({ a: cap, rel: 'le', b: brk, name: 'the first price band runs out at ' + Rtext(brk) });
    var obj = [];
    for (q = 0; q < n; q += 1) obj.push(rest[q]);
    obj[idx] = p1;
    obj.push(p2);
    var outNames = names.slice();
    outNames[idx] = names[idx] + '(1)';
    outNames.push(names[idx] + '(2)');
    return { max: maximise, names: outNames, obj: obj, cons: cons };
  }

  /* The split rewrite: a free variable carried as the difference of two
     non-negative ones, and its absolute value as their SUM.  The sum is only
     |x| when the direction of optimisation pushes at least one of them to
     zero -- true when it is minimised, false when it is not. */
  function splitModel(cons2, names, idx, absolute, obj0, maximise) {
    var n = names.length, cons = [], i, q, N = n + 1;
    var expand = function (a) {
      var out = [];
      for (q = 0; q < n; q += 1) out.push(a[q]);
      out.push(Rneg(a[idx]));            /* the negative part               */
      return out;
    };
    cons2.forEach(function (k) { cons.push({ a: expand(k.a), rel: k.rel || 'le', b: k.b, name: k.name }); });
    var obj = expand(obj0);
    if (absolute) {
      obj[idx] = obj0[idx];
      obj[n] = obj0[idx];                /* x+ + x- rather than x+ - x-     */
    }
    var outNames = names.slice();
    outNames[idx] = names[idx] + '+';
    outNames.push(names[idx] + '-');
    return { max: maximise, names: outNames, obj: obj, cons: cons };
  }
"""


# The drawing, kept OUT of LP_JS so that the arithmetic block stays free of
# anything that needs a document. Every routine here takes the svg element as
# an argument rather than closing over one, which is what makes `Plot` reusable
# and what makes these testable beside it.
REGION_JS = r"""
  /* A window that holds every point of interest with a quarter-width margin,
     and never collapses to zero width on a region that is a single point. */
  function lpWindow(pts) {
    var xs = [0], ys = [0], i;
    for (i = 0; i < pts.length; i += 1) { xs.push(Rnum(pts[i][0])); ys.push(Rnum(pts[i][1])); }
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    var px = Math.max(1, (xmax - xmin) * 0.25), py = Math.max(1, (ymax - ymin) * 0.25);
    return { xmin: xmin - px, xmax: xmax + px, ymin: ymin - py, ymax: ymax + py };
  }
  function lpLine(plot, a, b, c, win, cls) {
    var an = Rnum(a), bn = Rnum(b), cn = Rnum(c);
    if (an === 0 && bn === 0) return;
    if (bn === 0) { plot.vline(cn / an, cls); return; }
    plot.segment(win.xmin, (cn - an * win.xmin) / bn, win.xmax, (cn - an * win.xmax) / bn, cls);
  }
  /* The shading is the one place a picture samples rather than decides: the
     grid is in pixels and so are its sample points. Every verdict printed
     beneath it -- empty, unbounded, this corner wins -- came from exact
     arithmetic and not from the picture. */
  function lpShade(plot, cons, cls) {
    var nums = cons.map(function (k) { return [Rnum(k.a), Rnum(k.b), Rnum(k.c)]; });
    plot.shade(function (x, y) {
      for (var i = 0; i < nums.length; i += 1) {
        if (nums[i][0] * x + nums[i][1] * y > nums[i][2] + 1e-9) return false;
      }
      return true;
    }, cls);
  }
  function lpDrawRegion(svg, cons, pts, opts) {
    opts = opts || {};
    var win = lpWindow(pts.concat(opts.extra || []));
    var plot = Plot(svg, win);
    plot.frame();
    lpShade(plot, cons, 'plot-shade');
    cons.forEach(function (k) { lpLine(plot, k.a, k.b, k.c, win, 'plot-curve'); });
    return { plot: plot, win: win };
  }
"""


# ---------------------------------------------------------------- furniture

# WHAT EACH MODE ACTUALLY CONCATENATES, and why it is not one list.
#
# Page weight on this repository is capped at 62 KB gzipped and the shared
# blocks alone are 34 KB of it, so a mode that ships a block it never calls is
# spending a reader's bandwidth on dead code. The splits that matter:
#
#   MATRIX_JS   only `basic` row-reduces anything (3.2 KB gzipped)
#   BIGINT_JS   only `basic` counts bases with `comb`
#   EXPR/EXACT  only the view that lets a reader TYPE a point parses one
#   PLOT/REGION only the four modes that draw
#   TABLEAU/PHASE  every mode that solves above two variables -- which is all
#               of them but `convex`, whose sets are two-dimensional by
#               construction and are answered by Ccorners alone (8.6 KB)
_BASE_JS = RATIONAL_JS + FORMAT_JS + LINEAR_JS + FEAS_JS + ORFMT_JS
_ENGINE_JS = TABLEAU_JS + PHASE_JS
_DRAW_JS = PLOT_JS + REGION_JS


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


def _text(cid, label, value, hint=""):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, cid, label, cid, value)
        + ('        <p class="small-copy" id="%sHint" style="margin:0 0 6px;">%s</p>\n' % (cid, hint)
           if hint else "")
    )


def _range(cid, label, lo, hi, value, step=1):
    """One slider, its name, and a readout that starts empty.

    Every number on the panel is written by redraw() out of the arithmetic, so
    a lab whose script died shows a dash rather than a plausible figure nothing
    computed.
    """
    return (
        '        <div id="%sRow">\n'
        '          <div class="range-row"><label class="small-copy" for="%s" id="%sLab">%s</label>'
        '<span class="range-value" id="%sOut">&mdash;</span></div>\n'
        '          <input id="%s" type="range" min="%d" max="%d" step="%d" value="%d" />\n'
        "        </div>\n" % (cid, cid, cid, label, cid, cid, lo, hi, step, value)
    )


def _kpi(rows):
    """A kpi grid whose labels are written by redraw().

    Six modes of this kit rename what they are reporting as the data change --
    a slack becomes a surplus when a relation flips, a deviation is named for
    whichever goal sits at this priority level -- and a cell that renamed its
    number but not the label above it is the defect the duplicate-render guard
    exists to catch, one level down.
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


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _stage(sid, svgid, describe):
    return ('      <div class="lab-stage" id="%s" tabindex="0" role="region" aria-label="%s">'
            '<svg id="%s" viewBox="0 0 660 420" role="img" aria-label="%s"></svg></div>\n'
            % (sid, describe, svgid, describe))


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Five lessons share the ``model`` mode, so this is how each of them opens on
    its own numbers instead of on somebody else's. An unknown preset RAISES for
    exactly the reason an unknown mode does: a silent fallback ships a page
    that looks finished and is about a different situation.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("lp mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "lp mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "lp mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


def _choice(cfg, key, allowed, mode, default):
    """A rendering key that is NOT the preset, validated the way the preset is.

    Two of the five modelling lessons open on the same preset and are separated
    by ``view`` alone. That makes ``view`` a rendering key with exactly the
    duplicate-render hazard ``preset`` has, so an unknown value raises here
    rather than quietly picking the other lesson's widget.
    """
    want = cfg.get(key)
    if want is None:
        return default
    if want not in allowed:
        raise ValueError(
            "lp mode %r has no %s %r; known values: %s" % (mode, key, want, ", ".join(allowed))
        )
    return want


# =========================================================== mode: model
#
# Five lessons, four presets, two views. `mix` opens two of those lessons and
# the preset alone therefore does not separate them, so `view` does: one checks
# a reader-typed candidate point constraint by constraint, the other tabulates
# the slacks at the optimum and marks which rows stay tight as an availability
# moves. Both keys are validated; neither has a silent fallback.

MODEL_VIEWS = ("candidate", "slacks")

_MIX_JS = r"""
  var PRESET = 'mix', PLOTTED = true;
  var MIXNAMES = ['C', 'T', 'B'];
  var MIXLONG = ['chairs', 'tables', 'benches'];
  var MIXRATE = [[1, 0, 1], [0, 2, 1], [3, 2, 2]];
  var MIXPROFIT = [3, 5, 4];
  var MIXROW = ['the carpentry shop', 'the finishing shop', 'the assembly line'];
  var MIXUNIT = ['bench hours', 'finishing hours', 'assembly hours'];

  function readData() {
    return { n: slider('mdProducts'),
             avail: [slider('mdA1'), slider('mdA2'), slider('mdA3')] };
  }
  function buildModel(d) {
    var names = MIXNAMES.slice(0, d.n), obj = [], cons = [], i, j;
    for (j = 0; j < d.n; j += 1) obj.push(ri(MIXPROFIT[j]));
    for (i = 0; i < 3; i += 1) {
      var a = [];
      for (j = 0; j < d.n; j += 1) a.push(ri(MIXRATE[i][j]));
      cons.push({ a: a, rel: 'le', b: ri(d.avail[i]), name: MIXROW[i] });
    }
    return { max: true, names: names, obj: obj, cons: cons };
  }
  function unitsLine() {
    var out = [], j;
    for (j = 0; j < slider('mdProducts'); j += 1) {
      out.push(MIXNAMES[j] + ' = ' + MIXLONG[j] + ' made this week, in units');
    }
    return out.join(';&nbsp; ');
  }
  function dataTable(d, model) {
    var heads = [''], body = [], i, j;
    for (j = 0; j < d.n; j += 1) heads.push(MIXLONG[j] + ' (' + MIXNAMES[j] + ')');
    heads.push('available');
    for (i = 0; i < 3; i += 1) {
      var cells = [rowhead(MIXROW[i])];
      for (j = 0; j < d.n; j += 1) cells.push(td(Rtext(model.cons[i].a[j])));
      cells.push(td(Rtext(model.cons[i].b) + ' ' + MIXUNIT[i]));
      body.push(tr(cells));
    }
    var pr = [rowhead('profit a unit')];
    for (j = 0; j < d.n; j += 1) pr.push(td(Rtext(model.obj[j])));
    pr.push(td('&mdash;'));
    body.push(tr(pr));
    return table('The data table the model is written from', heads, body);
  }
  /* The unit chain, checked rather than asserted: a rate is hours per unit, a
     decision is units, and the product had better be hours -- which is the
     same hours the availability is quoted in. A model whose two sides carry
     different units is wrong before it is solved. */
  function extraPanel(d, model, res) {
    var body = [], i;
    for (i = 0; i < 3; i += 1) {
      var leftUnit = MIXUNIT[i], rightUnit = MIXUNIT[i];
      body.push(tr([rowhead(MIXROW[i]),
                    tdl(leftUnit + ' per unit  &times;  units made  =  ' + leftUnit),
                    tdl(rightUnit + ' on hand'),
                    td(leftUnit === rightUnit ? tone('they agree', 'green')
                       : tone('they do not agree', 'red'))]));
    }
    return table('Both sides of every row, in the units they are measured in',
                 ['', 'what the left-hand side measures', 'what the right-hand side measures', ''],
                 body);
  }
  function drawExtra(plot, win, model, res) { return plot; }
  function verdictExtra(d, model, res) {
    return 'Tight means used up. It does not mean that one more hour would buy anything: two '
      + 'resources can both be exhausted with only one of them worth paying for, and the '
      + 'difference between them is a price. This course deliberately cannot compute one yet.';
  }
"""

_DIET_JS = r"""
  var PRESET = 'diet', PLOTTED = true;
  var DIETNAMES = ['G', 'P'];
  var DIETLONG = ['grain', 'pellets'];
  var DIETROW = ['the protein requirement', 'the fibre requirement'];
  var DIETUNIT = ['grams of protein', 'grams of fibre'];
  var DIETRATE = [[1, 3], [2, 1]];

  function readData() {
    return { req: [slider('mdR1'), slider('mdR2')], cost2: slider('mdC2') };
  }
  function buildModel(d) {
    var cons = [], i, j;
    for (i = 0; i < 2; i += 1) {
      var a = [];
      for (j = 0; j < 2; j += 1) a.push(ri(DIETRATE[i][j]));
      cons.push({ a: a, rel: 'ge', b: ri(d.req[i]), name: DIETROW[i] });
    }
    return { max: false, names: DIETNAMES, obj: [ri(2), ri(d.cost2)], cons: cons };
  }
  function unitsLine() {
    return 'G = kilograms of grain in the ration;&nbsp; P = kilograms of pellets in the ration';
  }
  function dataTable(d, model) {
    var heads = ['', DIETLONG[0] + ' (G)', DIETLONG[1] + ' (P)', 'at least'], body = [], i, j;
    for (i = 0; i < 2; i += 1) {
      var cells = [rowhead(DIETROW[i])];
      for (j = 0; j < 2; j += 1) cells.push(td(Rtext(model.cons[i].a[j])));
      cells.push(td(Rtext(model.cons[i].b) + ' ' + DIETUNIT[i]));
      body.push(tr(cells));
    }
    body.push(tr([rowhead('cost a kilogram')].concat(
      model.obj.map(function (c) { return td(Rtext(c)); })).concat([td('&mdash;')])));
    return table('The nutrient table the model is written from', heads, body);
  }
  /* The certificate the lesson is about. The region here runs off to the
     north-east forever, and that is harmless: unboundedness is a property of
     the OBJECTIVE along the region's recession directions, not of the region.
     Crec drops every constant, which turns the constraints into a cone; the
     named directions are then tested against that cone, and Cgrows decides the
     same question over every direction at once. */
  function extraPanel(d, model, res) {
    var dirs = [{ name: 'more grain, same pellets', d: [ri(1), ri(0)] },
                { name: 'same grain, more pellets', d: [ri(0), ri(1)] },
                { name: 'more of both, equally', d: [ri(1), ri(1)] }];
    var rec = lpRecession(model, dirs);
    var body = rec.rows.map(function (q) {
      return tr([rowhead(q.name), td('(' + Rtext(q.d[0]) + ', ' + Rtext(q.d[1]) + ')'),
                 td(q.recession ? tone('yes, forever', 'amber') : tone('no, a wall stops it', 'muted')),
                 td(Rtext(q.change)),
                 tdl(!q.recession ? 'the question does not arise: the region does not go this way'
                     : (Rsign(q.change) > 0
                        ? 'cost only rises along it, so walking out this way never helps'
                        : (Rzero(q.change) ? 'cost is flat along it, so walking out this way changes nothing'
                           : tone('cost FALLS along it, so the minimum runs away', 'red'))))]);
    });
    var verdict = rec.runs
      ? tone('the cost falls without limit along a direction the region contains, so there is no minimum', 'red')
      : tone('no recession direction lowers the cost, so a minimum exists and sits at a corner', 'green');
    return table('The recession-cone test, direction by direction', 
                 ['direction', 'as a vector', 'does the region go on forever this way?',
                  'change in cost per step', 'what that settles'], body)
      + '<p class="small-copy" id="mdRecSay" style="margin:8px 0 0;">Over every direction at once, '
      + 'not only the three named above: ' + verdict + '.</p>';
  }
  /* The directions the panel tested, drawn as rays from the cheapest corner.
     A reader who is told the region runs on forever should be able to see
     which way, and the ray stops where the drawing window does rather than
     where a shading grid ran out of samples. */
  function drawExtra(plot, win, model, res) {
    if (!res.x) return plot;
    var dirs = [[1, 0], [0, 1], [1, 1]], i;
    var x0 = Rnum(res.x[0]), y0 = Rnum(res.x[1]);
    var span = Math.max(win.xmax - win.xmin, win.ymax - win.ymin) * 2;
    var rec = Crec(lpHalfPlanes(model));
    for (i = 0; i < dirs.length; i += 1) {
      var d0 = R(BigInt(dirs[i][0]), 1n), d1 = R(BigInt(dirs[i][1]), 1n), ok = true, t;
      for (t = 0; t < rec.length; t += 1) if (!Cholds(rec[t], d0, d1)) { ok = false; break; }
      if (!ok) continue;
      plot.segment(x0, y0, x0 + dirs[i][0] * span, y0 + dirs[i][1] * span, 'plot-aux');
    }
    return plot;
  }
  function verdictExtra(d, model, res) {
    return 'An unbounded region is not an unbounded problem. The set here extends forever to the '
      + 'north-east and the cost only climbs as you walk that way, so the smallest cost still '
      + 'exists and still sits at a corner.';
  }
"""

_BLEND_JS = r"""
  var PRESET = 'blend', PLOTTED = false;
  var BLENDNAMES = ['N', 'R', 'B'];
  var BLENDLONG = ['naphtha', 'reformate', 'butane'];
  var BLENDCOST = [5, 0, 2];

  function readData() {
    return { minA: slider('mdMinA'), maxC: slider('mdMaxC'),
             batch: slider('mdBatch'), priceB: slider('mdPriceB') };
  }
  function buildModel(d) {
    var tA = R(BigInt(d.minA), 100n), tC = R(BigInt(d.maxC), 100n);
    var cons = [{ a: [R1, R1, R1], rel: 'eq', b: ri(d.batch), name: 'the batch is filled exactly' },
      lpShareRow(0, tA, 3, true, 'the naphtha share'),
      lpShareRow(2, tC, 3, false, 'the butane ceiling')];
    return { max: false, names: BLENDNAMES, obj: [ri(BLENDCOST[0]), ri(d.priceB), ri(BLENDCOST[2])],
             cons: cons, tA: tA, tC: tC };
  }
  function unitsLine() {
    return BLENDNAMES.map(function (nm, i) {
      return nm + ' = litres of ' + BLENDLONG[i] + ' in the batch';
    }).join(';&nbsp; ');
  }
  function dataTable(d, model) {
    return table('The blend, as the specification states it',
      ['', 'cost a litre', 'the share required of it'],
      [tr([rowhead(BLENDLONG[0] + ' (N)'), td(Rtext(model.obj[0])),
           tdl('at least ' + Rpct(model.tA, 1) + ' of the batch')]),
       tr([rowhead(BLENDLONG[1] + ' (R)'), td(Rtext(model.obj[1])), tdl('whatever is left')]),
       tr([rowhead(BLENDLONG[2] + ' (B)'), td(Rtext(model.obj[2])),
           tdl('at most ' + Rpct(model.tC, 1) + ' of the batch')]),
       tr([rowhead('the batch'), td('&mdash;'), tdl('exactly ' + Rtext(model.cons[0].b) + ' litres')])]);
  }
  /* Three panels in a row: the requirement as stated, the same requirement
     with the denominator cleared, and the share actually achieved. The middle
     one is the lesson: the clearing is legal here only because the total is a
     non-negative quantity, and the fourth row is the requirement where that
     condition FAILS and the move is declined. */
  function extraPanel(d, model, res) {
    var shares = res.x ? lpShares(res.x) : null;
    var body = [
      tr([rowhead(BLENDLONG[0]),
          tdl('N &gt;= ' + Rtext(model.tA) + ' &times; (N + R + B)'),
          tdl(Ltext(model.cons[1].a, model.names) + ' &gt;= 0'),
          td(shares && shares.shares[0] ? Rpct(shares.shares[0], 2) : '&mdash;')]),
      tr([rowhead(BLENDLONG[1]), tdl('no share is stated for it'),
          tdl('&mdash;'),
          td(shares && shares.shares[1] ? Rpct(shares.shares[1], 2) : '&mdash;')]),
      tr([rowhead(BLENDLONG[2]),
          tdl('B &lt;= ' + Rtext(model.tC) + ' &times; (N + R + B)'),
          tdl(Ltext(model.cons[2].a, model.names) + ' &lt;= 0'),
          td(shares && shares.shares[2] ? Rpct(shares.shares[2], 2) : '&mdash;')])];
    var vanish = lpDenominatorCanVanish(model, 2);
    body.push(tr([rowhead('the requirement this lab declines'),
      tdl('N / B &gt;= 2, a ratio whose denominator is itself a decision'),
      tdl(vanish.canVanish
          ? tone('declined: the constraints allow B = 0, and at that point the ratio is not a '
                 + 'number at all. Clearing it to N - 2B &gt;= 0 is a DIFFERENT '
                 + 'requirement, not the same one rearranged.', 'red')
          : tone('safe here: no feasible blend has B = 0, so the denominator cannot vanish '
                 + 'and the clearing is a rearrangement rather than a new statement.', 'green')),
      td('&mdash;')]));
    return table('The ratio as stated, the ratio cleared, and the share achieved',
      ['', 'as the specification says it', 'once the denominator is cleared',
       'achieved at the optimum'], body);
  }
  function drawExtra(plot, win, model, res) { return plot; }
  function verdictExtra(d, model, res) {
    return 'Writing the naphtha requirement as "N &gt;= ' + Rtext(model.tA) + '" instead would '
      + 'be a quantity where a proportion is meant: the variable is measured in litres and the '
      + 'requirement is measured in nothing. The model that results is feasible, solvable, and '
      + 'about a different problem.';
  }
"""

_MULTI_JS = r"""
  var PRESET = 'multiperiod', PLOTTED = false;

  function readData() {
    var T = slider('mdT'), demand = [], t;
    for (t = 1; t <= 4; t += 1) demand.push(slider('mdD' + t));
    return { T: T, demand: demand.slice(0, T), cap: slider('mdCap'),
             hold: slider('mdHold'), start: slider('mdStart'),
             aggregate: document.getElementById('mdAgg').value === 'aggregate' };
  }
  /* Production is cheaper later, which is what makes the misconception bite:
     an aggregate constraint lets the plan wait, and waiting is exactly what a
     balance equation forbids. */
  function costs(T) {
    var out = [], t;
    for (t = 0; t < T; t += 1) out.push(ri(9 - t));
    return out;
  }
  function buildModel(d) {
    var demand = d.demand.map(ri);
    var m = d.aggregate
      ? lpAggregateModel(demand, ri(d.cap), costs(d.T), ri(d.hold), ri(d.start))
      : lpBalanceModel(demand, ri(d.cap), costs(d.T), ri(d.hold), ri(d.start));
    m.demandR = demand;
    return m;
  }
  function unitsLine() {
    return 'P1 to P' + slider('mdT') + ' = units made in each period;&nbsp; I1 to I'
      + slider('mdT') + ' = units still in the store at the end of each period';
  }
  function dataTable(d, model) {
    var heads = [''], body = [], t;
    for (t = 0; t < d.T; t += 1) heads.push('period ' + (t + 1));
    var dm = [rowhead('demand')], ct = [rowhead('cost to make one')];
    var cs = costs(d.T);
    for (t = 0; t < d.T; t += 1) { dm.push(td(Rtext(model.demandR[t]))); ct.push(td(Rtext(cs[t]))); }
    body.push(tr(dm)); body.push(tr(ct));
    return table('The plan, period by period', heads, body)
      + '<p class="small-copy" id="mdPlanSay" style="margin:8px 0 0;">Opening stock '
      + d.start + ', capacity ' + d.cap + ' a period, and ' + d.hold
      + ' to carry one unit from one period into the next.</p>';
  }
  /* The two plans side by side, and the demand the aggregate one leaves
     unmet. One aggregate constraint does NOT say what T balance equations say:
     it is satisfied by producing everything at the end, after every earlier
     demand has already gone unserved. */
  function extraPanel(d, model, res) {
    var demand = d.demand.map(ri);
    var other = d.aggregate
      ? lpBalanceModel(demand, ri(d.cap), costs(d.T), ri(d.hold), ri(d.start))
      : lpAggregateModel(demand, ri(d.cap), costs(d.T), ri(d.hold), ri(d.start));
    var otherRes = lpSolveModel(other);
    var mine = res.x ? lpRunStock(res.x.slice(0, d.T), demand, ri(d.start)) : null;
    var theirs = otherRes.x ? lpRunStock(otherRes.x.slice(0, d.T), demand, ri(d.start)) : null;
    var body = [], t;
    for (t = 0; t < d.T; t += 1) {
      body.push(tr([rowhead('period ' + (t + 1)),
        td(mine ? Rtext(mine.rows[t].produced) : '&mdash;'),
        td(mine ? Rtext(mine.rows[t].closing) : '&mdash;'),
        td(mine && !Rzero(mine.rows[t].unmet) ? tone(Rtext(mine.rows[t].unmet), 'red') : '0'),
        td(theirs ? Rtext(theirs.rows[t].produced) : '&mdash;'),
        td(theirs && !Rzero(theirs.rows[t].unmet) ? tone(Rtext(theirs.rows[t].unmet), 'red') : '0')]));
    }
    var here = d.aggregate ? 'one aggregate row' : 'a balance row per period';
    var there = d.aggregate ? 'a balance row per period' : 'one aggregate row';
    return table('What each way of writing the link actually produces',
      ['', 'made, with ' + here, 'carried out', 'demand missed',
       'made, with ' + there, 'demand missed'], body)
      + '<p class="small-copy" id="mdAggSay" style="margin:8px 0 0;">'
      + (mine && theirs
         ? ('With ' + here + ' the plan costs ' + Rtext(res.z) + ' and misses ' + Rtext(mine.unmet)
            + ' units of demand; with ' + there + ' it costs ' + Rtext(otherRes.z) + ' and misses '
            + Rtext(theirs.unmet) + '. The cheaper plan is not the better one whenever the missed '
            + 'column is not zero, and that column is what the aggregate row cannot see.')
         : 'one of the two ways of writing the link has no feasible plan at these numbers.')
      + '</p>';
  }
  function drawExtra(plot, win, model, res) { return plot; }
  function verdictExtra(d, model, res) {
    return 'The inventory variable is what carries the link between one period and the next. '
      + 'Total production at least total demand is a weaker statement, and the difference is '
      + 'visible in the missed-demand column rather than in the cost.';
  }
"""


MODEL_BODY = r"""
  var VIEW = '__VIEW__';
  var CONTROLS = __CONTROLS__;

  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function out(id, text) { document.getElementById(id + 'Out').textContent = text; }
  function el(id) { return document.getElementById(id); }
  function kpi(id, label, value) {
    el(id + 'Lab').textContent = label;
    el(id).innerHTML = value;
  }
  function pointtext(p) { return '(' + p.map(function (v) { return Rshort(v, 4, 9); }).join(', ') + ')'; }

  /* The linear programme itself, rewritten every time a datum moves. Nothing
     here is stored: the objective and every row are printed out of the same
     model object the solver is about to be handed. */
  function lpBlock(model) {
    var lines = ['<div>' + lpObjText(model) + '</div>', '<div>subject to</div>'];
    model.cons.forEach(function (k, i) {
      lines.push('<div>&nbsp;&nbsp;' + lpRowText(k, model.names)
        + '&nbsp;&nbsp;<span class="tone-muted">' + esc(k.name || ('row ' + (i + 1))) + '</span></div>');
    });
    lines.push('<div>&nbsp;&nbsp;' + lpSignText(model) + '&nbsp;&nbsp;'
      + '<span class="tone-muted">a constraint, not a convention</span></div>');
    /* What the letters stand for and what they are measured in. A decision
       variable without a unit is the commonest way a model comes out wrong,
       and the unit belongs beside the programme rather than in the prose. */
    lines.push('<div class="tone-muted">' + unitsLine() + '</div>');
    return lines.join('');
  }

  function candidateTable(model, res) {
    var typed = String(el('mdCand').value || ''), parts = typed.split(','), point = [], bad = null, j;
    for (j = 0; j < model.names.length; j += 1) {
      var piece = parts[j] === undefined ? '' : parts[j];
      var parsed = Xparse(piece);
      if (parsed.bad) { bad = 'the entry for ' + model.names[j] + ': ' + parsed.bad; break; }
      var got = Xeval(parsed.node, {});
      if (got.bad) { bad = 'the entry for ' + model.names[j] + ': ' + got.bad; break; }
      point.push(got.v);
    }
    if (bad) {
      return { html: '<div class="status-banner" id="mdCandBad">' + tone(esc(bad), 'red')
        + ' Type one value for each decision, separated by commas &mdash; whole numbers, fractions '
        + 'like 9/2, or arithmetic like 3 + 1/2, all read exactly.</div>', point: null, check: null };
    }
    var check = lpCandidate(model, point);
    var body = check.rows.map(function (q) {
      return tr([rowhead(esc(q.name)), tdl(q.text), td(Rshort(q.lhs, 4, 9)), td(Rshort(q.rhs, 4, 9)),
                 td(Rshort(q.diff, 4, 9)),
                 td(q.ok ? tone('holds', 'green') : tone('broken', 'red'))]);
    });
    return { point: point, check: check,
      html: table('Your point ' + pointtext(point) + ', checked one constraint at a time',
        ['', 'the constraint', 'left-hand value', 'right-hand value', 'left minus right', ''], body) };
  }

  function slackTable(model, res) {
    if (!res.x) return '';
    var sr = lpSlackRows(model, res.x);
    var body = sr.rows.map(function (q) {
      return tr([rowhead(esc(q.name)), td(Rshort(q.lhs, 4, 9)), td(Rshort(q.rhs, 4, 9)),
                 td('<span class="tt">' + q.varName + '</span>'),
                 td(Rshort(q.value, 4, 9)),
                 td(q.tight ? tone('tight', 'amber') : tone('slack', 'green')),
                 tdl(q.measures)]);
    });
    return table('Every row at the optimum: tight exactly where the new variable is zero',
      ['', 'used', 'available', 'the new variable', 'its value', '', 'what it measures'], body);
  }

  function draw(model, res, candidate) {
    var stage = el('mdStage');
    if (!stage) return;
    var svg = el('mdPlot');
    if (model.obj.length !== 2) {
      svg.textContent = '';
      stage.hidden = true;
      return;
    }
    stage.hidden = false;
    var pts = [], i;
    for (i = 0; i < res.corners.length; i += 1) pts.push([res.corners[i].x, res.corners[i].y]);
    if (candidate) pts.push(candidate);
    if (!pts.length) pts.push([R0, R0]);
    var drawn = lpDrawRegion(svg, res.cons, pts);
    for (i = 0; i < res.corners.length; i += 1) {
      var c = res.corners[i];
      drawn.plot.point(Rnum(c.x), Rnum(c.y), i === res.best ? 'plot-end' : 'plot-point',
                       i === res.best ? pointtext([c.x, c.y]) : '');
    }
    if (candidate) drawn.plot.point(Rnum(candidate[0]), Rnum(candidate[1]), 'plot-hole', 'your point');
    drawExtra(drawn.plot, drawn.win, model, res);
    drawn.plot.describe('The feasible region of ' + res.cons.length + ' half-planes with '
      + res.corners.length + ' corners marked, the winning corner picked out'
      + (candidate ? ', and the point you typed drawn as an open circle' : '') + '.');
  }

  function redraw() {
    var d = readData();
    var i;
    for (i = 0; i < CONTROLS.length; i += 1) out(CONTROLS[i][0], String(slider(CONTROLS[i][0])));
    var model = buildModel(d);
    var res = lpSolveModel(model);
    el('mdLp').innerHTML = lpBlock(model);
    var candidate = null, check = null, main = '';
    if (VIEW === 'candidate') {
      var ct = candidateTable(model, res);
      main = ct.html;
      candidate = ct.point;
      check = ct.check;
    } else {
      main = slackTable(model, res);
    }
    el('mdTable').innerHTML = dataTable(d, model) + main;
    el('mdExtra').innerHTML = extraPanel(d, model, res);
    draw(model, res, candidate);

    var solved = res.method === 'corners'
      ? ('corners: ' + res.corners.length + ' of them')
      : 'the exact simplex';
    var zText = res.z === null ? 'none' : Rshort(res.z, 4, 9);
    if (VIEW === 'candidate') {
      kpi('mdK1', 'Your point scores', check ? Rshort(check.z, 4, 9) : '&mdash;');
      kpi('mdK2', 'The best any plan scores', zText);
      kpi('mdK3', 'Rows your point breaks',
          check ? String(check.failed.length) + ' of ' + String(check.rows.length) : '&mdash;');
      kpi('mdK4', 'Decisions in the model', String(model.names.length));
    } else {
      var sr = res.x ? lpSlackRows(model, res.x) : null;
      var tight = 0;
      if (sr) for (i = 0; i < sr.rows.length; i += 1) if (sr.rows[i].tight) tight += 1;
      kpi('mdK1', 'The best any plan scores', zText);
      kpi('mdK2', 'Rows used right up', sr ? String(tight) : '&mdash;');
      kpi('mdK3', 'Rows with something left', sr ? String(sr.rows.length - tight) : '&mdash;');
      kpi('mdK4', 'Solved by', solved);
    }

    var head;
    if (res.status === 'infeasible') {
      head = '<strong>No plan satisfies every row at once.</strong> ';
    } else if (res.status === 'unbounded') {
      head = '<strong>There is no best plan: the objective runs away.</strong> ';
    } else {
      head = '<strong>' + (model.max === false ? 'Least' : 'Best') + ' achievable: ' + zText
        + (res.x ? ' at ' + pointtext(res.x) : '') + '.</strong> ';
    }
    var how = res.method === 'corners'
      ? ('Two decisions, so this one is answered by enumerating every crossing of two boundary '
         + 'lines and keeping the ones that satisfy the rest &mdash; ' + res.corners.length
         + ' of them here. ')
      : ('More than two decisions, so there is no picture and the exact simplex answers it '
         + 'instead: every constraint becomes an equality, Phase I finds a first feasible basis '
         + 'and Phase II improves it. ');
    var typed = (VIEW === 'candidate' && check)
      ? (check.ok
         ? 'The point you typed satisfies every row, so it is a plan someone could actually run. '
         : 'The point you typed breaks ' + check.failed.length + ' of the ' + check.rows.length
           + ' rows, and the table names which. ')
      : '';
    el('mdStatus').innerHTML = head + typed + how + verdictExtra(d, model, res);
  }

  CONTROLS.forEach(function (c) {
    var node = document.getElementById(c[0]);
    if (node) node.addEventListener('input', redraw);
  });
  __EXTRAWIRE__
  redraw();
  window.redrawLab = redraw;
"""


MODEL_PRESETS = [
    {
        "key": "mix",
        "js": _MIX_JS,
        "plotted": True,
        "title": "Product mix, written from a table",
        "subtitle": "Per-unit rates down the columns, availabilities down the right",
        "legend": (_swatch("tone-cyan", "the feasible region")
                   + _swatch("tone-amber", "its corners")
                   + _swatch("tone-green", "the winning corner")),
        "panel_title": "Change the workshop and watch the programme rewrite itself",
        "panel_intro": (
            "Every coefficient below is read off the data table, so a change to an availability "
            "rewrites the linear programme and re-solves it rather than adjusting an answer. Two "
            "products are enumerated corner by corner; move to three and the picture is gone and "
            "the simplex engine answers instead."),
        "controls": (
            _range("mdProducts", "how many products the workshop makes", 2, 3, 2)
            + _range("mdA1", "bench hours available in the carpentry shop", 1, 12, 4)
            + _range("mdA2", "hours available in the finishing shop", 2, 24, 12)
            + _range("mdA3", "hours available on the assembly line", 6, 30, 18)),
        "sliders": ["mdProducts", "mdA1", "mdA2", "mdA3"],
    },
    {
        "key": "diet",
        "js": _DIET_JS,
        "plotted": True,
        "legend": (_swatch("tone-cyan", "the feasible region")
                   + _swatch("tone-amber", "its corners")
                   + _swatch("tone-muted", "a direction it runs on forever")
                   + _swatch("tone-green", "the cheapest corner")),
        "title": "A covering model, and whether the cost runs away",
        "subtitle": "Requirements are ≥ rows, their surplus is over-fulfilment",
        "panel_title": "Set the requirements, then try to make the cost run away",
        "panel_intro": (
            "The region here has no ceiling: you can always feed more. That is harmless while "
            "every direction it runs in costs money, and the recession-cone panel tests exactly "
            "that, direction by direction, and then over every direction at once. Push the price "
            "of pellets below zero and watch the verdict change."),
        "controls": (
            _range("mdR1", "grams of protein the ration must supply", 3, 18, 9)
            + _range("mdR2", "grams of fibre the ration must supply", 3, 18, 8)
            + _range("mdC2", "what a kilogram of pellets costs, a disposal credit allowed", -3, 6, 3)),
        "sliders": ["mdR1", "mdR2", "mdC2"],
    },
    {
        "key": "blend",
        "js": _BLEND_JS,
        "plotted": False,
        "legend": (_swatch("tone-cyan", "as the specification states it")
                   + _swatch("tone-purple", "once the denominator is cleared")
                   + _swatch("tone-green", "achieved at the optimum")),
        "title": "Blending, and the share that is secretly linear",
        "subtitle": "A percentage of a total the decisions themselves add up to",
        "panel_title": "Set the shares the specification demands",
        "panel_intro": (
            "A share is a percentage of a total that the decisions themselves make up, so the "
            "requirement has a decision in its denominator until it is cleared. Clearing is legal "
            "here because the total is a quantity that cannot be negative; the last row of the "
            "panel is a requirement where that condition fails, and the lab declines it."),
        "controls": (
            _range("mdMinA", "per cent of the blend that must be naphtha", 0, 60, 30)
            + _range("mdMaxC", "per cent of the blend that may be butane", 5, 60, 25)
            + _range("mdBatch", "litres in the batch", 50, 200, 100, 10)
            + _range("mdPriceB", "what a litre of reformate costs", 1, 9, 3)),
        "sliders": ["mdMinA", "mdMaxC", "mdBatch", "mdPriceB"],
    },
    {
        "key": "multiperiod",
        "js": _MULTI_JS,
        "plotted": False,
        "legend": (_swatch("tone-cyan", "made in the period")
                   + _swatch("tone-purple", "carried into the next")
                   + _swatch("tone-red", "demand that went unmet")),
        "title": "Planning over periods, linked by one balance equation",
        "subtitle": "Inventory is the variable that carries one period into the next",
        "panel_title": "Set the demands, then replace the balance rows with one aggregate row",
        "panel_intro": (
            "One balance equation per period says stock carried out is stock carried in plus what "
            "was made minus what was sold. The selector swaps all of them for the single row "
            "“total made is at least total demand”, which sounds like the same thing and "
            "is not: the table shows the plan it then prefers and the demand that plan misses."),
        "controls": (
            _select("mdAgg", "How the periods are linked",
                    [("balance", "a balance equation in every period"),
                     ("aggregate", "one aggregate row for the whole horizon")], "balance")
            + _range("mdT", "how many periods the plan covers", 2, 4, 4)
            + _range("mdD1", "demand in the first period", 0, 40, 20)
            + _range("mdD2", "demand in the second period", 0, 40, 35)
            + _range("mdD3", "demand in the third period", 0, 40, 30)
            + _range("mdD4", "demand in the fourth period", 0, 40, 25)
            + _range("mdCap", "most that can be made in one period", 20, 80, 60)
            + _range("mdHold", "cost of carrying one unit into the next period", 0, 5, 1)
            + _range("mdStart", "stock on hand before the first period", 0, 20, 5)),
        "sliders": ["mdT", "mdD1", "mdD2", "mdD3", "mdD4", "mdCap", "mdHold", "mdStart"],
    },
]

MODEL_KEYS = tuple(p["key"] for p in MODEL_PRESETS)


def _model(cfg):
    """Five lessons behind one mode: the preset picks the situation, the view
    picks what the main table answers about it."""
    idx = _preset_index(cfg, MODEL_PRESETS, "model")
    p = MODEL_PRESETS[idx]
    view = _choice(cfg, "view", MODEL_VIEWS, "model",
                   "candidate" if p["key"] == "mix" else "slacks")
    stage = _stage("mdStage", "mdPlot",
                   "The feasible region, its corners, and the corner the objective picks.") \
        if p["plotted"] else ""
    markup = (
        _toolbar(p["title"], p["subtitle"], p["legend"])
        + stage
        + '      <div class="mathblock" id="mdLp" style="margin-top:12px;"></div>\n'
        '      <div id="mdTable" style="margin-top:12px;"></div>\n'
        '      <div id="mdExtra" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="mdStatus" style="margin-top:12px;"></div>'
    )
    candidate_field = _text(
        "mdCand", "A candidate point to check", "2, 6",
        "One value per decision, separated by commas. Fractions like <code>9/2</code> and "
        "arithmetic like <code>3 + 1/2</code> are read exactly, never as 4.5.",
    ) if view == "candidate" else ""
    controls = (
        candidate_field
        + p["controls"]
        + _kpi([("mdK1", "&mdash;"), ("mdK2", "&mdash;"), ("mdK3", "&mdash;"), ("mdK4", "&mdash;")])
    )
    wire = ""
    if p["key"] == "multiperiod":
        wire = "document.getElementById('mdAgg').addEventListener('change', redraw);"
    if view == "candidate":
        wire += "\n  document.getElementById('mdCand').addEventListener('input', redraw);"
    script = (
        _BASE_JS + (EXPR_JS + EXACT_JS if view == "candidate" else "")
        + _ENGINE_JS + LP_JS + BLEND_JS
        + (_DRAW_JS if p["plotted"] else "")
        + p["js"]
        + MODEL_BODY
        .replace("__VIEW__", view)
        .replace("__CONTROLS__", "[" + ", ".join("['%s']" % s for s in p["sliders"]) + "]")
        .replace("__EXTRAWIRE__", wire)
    )
    return Lab(
        title=p["title"],
        subtitle=p["subtitle"],
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", p["panel_title"]),
        panel_intro=cfg.get("panel_intro", p["panel_intro"]),
        script=script,
    )


# ========================================================== mode: reform
#
# One argument made four times. All four rewrites here are the same object --
# an objective that is the max (or the min) of a list of linear pieces -- and
# the original is optimised by CORNER ENUMERATION over the sub-regions on which
# one piece is the selected one, because on each of those the objective is
# linear and its optimum over it is therefore at one of its corners.

REFORM_SCRIPT = r"""
  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function el(id) { return document.getElementById(id); }
  function out(id, text) { el(id + 'Out').textContent = text; }
  function lab(id, text) { el(id + 'Lab').textContent = text; }
  function kpi(id, label, value) { el(id + 'Lab').textContent = label; el(id).innerHTML = value; }
  function pointtext(p) { return '(' + p.map(function (v) { return Rshort(v, 4, 9); }).join(', ') + ')'; }
  var BREAK = 3;

  function baseRows(cap, freeX) {
    var rows = [{ a: [ri(1), ri(1)], rel: 'le', b: ri(8), name: 'the shared line' },
                { a: [ri(1), ri(0)], rel: 'le', b: ri(5), name: 'the eastern limit' },
                { a: [ri(0), ri(1)], rel: 'le', b: ri(6), name: 'the northern limit' },
                { a: [ri(2), ri(3)], rel: 'ge', b: ri(cap), name: 'the order that must be met' }];
    if (freeX) rows.push({ a: [ri(-1), ri(0)], rel: 'le', b: ri(4), name: 'the western limit' });
    return rows;
  }

  /* Each rewrite, as data: the pieces the original objective is built from,
     the model the rewrite produces, and the sentence that says why the
     direction of optimisation is what makes it legal. */
  function spec(rule, p1, p2, cap, maximise) {
    var freeX = rule !== 'band';
    var rows = baseRows(cap, freeX);
    var free = freeX ? [0] : [];
    var s = { rows: rows, free: free, rule: rule, maximise: maximise };
    if (rule === 'free') {
      s.pieces = [{ a: [ri(p1), ri(p2)], k: R0 }];
      s.combine = 'max';
      s.original = (maximise ? 'maximise ' : 'minimise ') + p1 + 'x + ' + p2 + 'y, with x free to go negative';
      s.reform = splitModel(rows, ['x', 'y'], 0, false, [ri(p1), ri(p2)], maximise);
      s.aux = 'x+ and x-';
      s.why = 'a free variable is carried as x+ minus x-, both held at or above zero. Nothing '
        + 'pushes either of them anywhere in particular, and nothing needs to: any pair with the '
        + 'right difference gives the same objective, so this rewrite is the one of the four that '
        + 'is legal in BOTH directions.';
      s.p1Lab = 'what one unit of x is worth'; s.p2Lab = 'what one unit of y is worth';
    } else if (rule === 'abs') {
      s.pieces = [{ a: [ri(p1), ri(p2)], k: R0 }, { a: [ri(-p1), ri(p2)], k: R0 }];
      s.combine = 'max';
      s.original = (maximise ? 'maximise ' : 'minimise ') + p1 + '|x| + ' + p2 + 'y, with x free';
      s.reform = splitModel(rows, ['x', 'y'], 0, true, [ri(p1), ri(p2)], maximise);
      s.aux = 'x+ and x-';
      s.why = 'the absolute value is carried as x+ PLUS x-, and that sum is |x| only when at '
        + 'least one of the two is pushed to zero. Minimising does push it there. Maximising '
        + 'pushes both of them up together instead, and the rewrite stops being about |x| at all.';
      s.p1Lab = 'the penalty on the size of x'; s.p2Lab = 'what one unit of y contributes';
    } else if (rule === 'minmax') {
      s.pieces = [{ a: [ri(p1), ri(1)], k: R0 }, { a: [ri(-1), ri(p2)], k: R0 }];
      s.combine = 'max';
      s.original = (maximise ? 'maximise ' : 'minimise ') + 'max(' + p1 + 'x + y,  -x + ' + p2 + 'y)';
      s.reform = epigraphModel(rows, s.pieces, ['x', 'y'], maximise);
      s.reform.free = [0, 2];
      s.aux = 't';
      s.why = 't is held at or above every piece, so t is at least the largest of them. '
        + 'Minimising t squeezes it down ONTO that largest piece, which is what makes the '
        + 'rewrite an equality in disguise. Maximising t lets it float upward with nothing '
        + 'above it, and the rewrite has no finite answer at all.';
      s.p1Lab = 'the weight on x in the first piece'; s.p2Lab = 'the weight on y in the second piece';
    } else {
      var gap = ri((p1 - p2) * BREAK);
      s.pieces = [{ a: [ri(p1), ri(4)], k: R0 }, { a: [ri(p2), ri(4)], k: gap }];
      s.combine = p2 >= p1 ? 'max' : 'min';
      s.original = (maximise ? 'maximise ' : 'minimise ') + 'a cost of ' + p1 + ' for each of the first '
        + BREAK + ' units of x and ' + p2 + ' for every unit after that, plus 4 for each y';
      s.reform = segmentModel(rows, ['x', 'y'], 0, ri(BREAK), ri(p1), ri(p2), [R0, ri(4)], maximise);
      s.aux = 'x(1) and x(2)';
      s.why = 'the quantity is split into one variable per price band and the bands are priced '
        + 'separately. A minimiser fills the CHEAPER band first, which is the earlier band only '
        + 'when the later one costs more. That condition is convexity, and it is stated here '
        + 'rather than assumed: at these two prices the cost function is '
        + (p2 >= p1 ? 'convex and the rewrite is exact' : 'CONCAVE and the rewrite is not')
        + '.';
      s.p1Lab = 'price of each of the first ' + BREAK + ' units of x';
      s.p2Lab = 'price of every unit of x after that';
    }
    return s;
  }

  function piecesText(s) {
    return s.pieces.map(function (p, i) {
      return '<div>&nbsp;&nbsp;piece ' + (i + 1) + ':&nbsp;' + Ltext(p.a, ['x', 'y'])
        + (Rzero(p.k) ? '' : plusnum(p.k)) + '</div>';
    }).join('');
  }
  function modelText(model) {
    var lines = ['<div>' + lpObjText(model) + '</div>', '<div>subject to</div>'];
    model.cons.forEach(function (k, i) {
      lines.push('<div>&nbsp;&nbsp;' + lpRowText(k, model.names) + '</div>');
    });
    lines.push('<div>&nbsp;&nbsp;' + lpSignText(model) + '</div>');
    return lines.join('');
  }

  function redraw() {
    var rule = el('rfRule').value, maximise = el('rfDir').value === 'max';
    var p1 = slider('rfP1'), p2 = slider('rfP2'), cap = slider('rfCap');
    out('rfP1', String(p1)); out('rfP2', String(p2)); out('rfCap', String(cap));
    var s = spec(rule, p1, p2, cap, maximise);
    lab('rfP1', s.p1Lab); lab('rfP2', s.p2Lab);
    var model = { max: maximise, names: ['x', 'y'], obj: [R0, R0], cons: s.rows, free: s.free };
    var cons = lpHalfPlanes(model);
    var orig = pieceOptimum(cons, s.pieces, s.combine, maximise);
    var ref = lpSolveModel(s.reform);

    el('rfLp').innerHTML = '<div>' + esc(s.original) + '</div>'
      + '<div>which is the ' + (s.combine === 'min' ? 'smaller' : 'larger')
      + ' of these linear pieces</div>'
      + piecesText(s)
      + '<div>subject to</div>'
      + s.rows.map(function (k) { return '<div>&nbsp;&nbsp;' + lpRowText(k, ['x', 'y']) + '</div>'; }).join('')
      + '<div>&nbsp;&nbsp;' + lpSignText(model) + '</div>';

    var body = [];
    orig.regions.forEach(function (rg) {
      if (!rg.feasible) {
        body.push(tr([rowhead('where piece ' + (rg.piece + 1) + ' is the one that counts'),
                      tdl('no point of the region is in this part of it'), td('&mdash;'), td('&mdash;')]));
        return;
      }
      if (rg.runs) {
        body.push(tr([rowhead('where piece ' + (rg.piece + 1) + ' is the one that counts'),
                      tdl(tone('the objective runs away in this part of the region', 'red')),
                      td('&mdash;'), td('&mdash;')]));
        return;
      }
      rg.points.forEach(function (pt, i) {
        var win = orig.at !== null && Requ(pt.x, orig.at[0]) && Requ(pt.y, orig.at[1]);
        body.push(tr([rowhead(i === 0 ? 'where piece ' + (rg.piece + 1) + ' counts' : ''),
                      tdl('corner ' + pointtext([pt.x, pt.y])),
                      td(Rshort(pt.value, 4, 9)),
                      td(win ? tone('the best of them', 'green') : '')]));
      });
    });
    el('rfCorners').innerHTML = table('The original, by enumerating the corners of each part',
      ['', 'corner', 'the original objective there', ''], body);

    /* Every variable of the rewrite with the value it took, because the
       auxiliary ones are the whole argument and hiding them would hide it. */
    var auxText = '&mdash;';
    if (ref.x) {
      auxText = s.reform.names.map(function (nm, i) {
        return nm + ' = ' + Rshort(ref.x[i], 4, 9);
      }).join(',&nbsp; ') + '&nbsp; (the auxiliary ones are ' + esc(s.aux) + ')';
    }
    el('rfReform').innerHTML = '<div class="mathblock" id="rfReformLp">' + modelText(s.reform) + '</div>'
      + table('The reformulation, by the simplex engine',
        ['', ''],
        [tr([rowhead('what it reports'), tdl(ref.status === 'optimal'
            ? Rshort(ref.z, 4, 9) + ' at ' + pointtext(ref.x)
            : tone('no finite answer: the rewrite is ' + esc(ref.status), 'red'))]),
         tr([rowhead('the auxiliary variables there'), tdl(auxText)]),
         tr([rowhead('why the direction matters'), tdl(s.why)])]);

    var stage = el('rfStage'), svg = el('rfPlot');
    var pts = [];
    orig.regions.forEach(function (rg) { rg.points.forEach(function (p) { pts.push([p.x, p.y]); }); });
    if (!pts.length) pts.push([R0, R0]);
    var drawn = lpDrawRegion(svg, cons, pts);
    var i, j;
    for (i = 0; i < s.pieces.length; i += 1) {
      for (j = i + 1; j < s.pieces.length; j += 1) {
        lpLine(drawn.plot, Rsub(s.pieces[i].a[0], s.pieces[j].a[0]),
               Rsub(s.pieces[i].a[1], s.pieces[j].a[1]),
               Rsub(s.pieces[j].k, s.pieces[i].k), drawn.win, 'plot-asym');
      }
    }
    orig.regions.forEach(function (rg) {
      rg.points.forEach(function (p) { drawn.plot.point(Rnum(p.x), Rnum(p.y), 'plot-point', ''); });
    });
    if (orig.at) drawn.plot.point(Rnum(orig.at[0]), Rnum(orig.at[1]), 'plot-end', pointtext(orig.at));
    drawn.plot.describe('The region, the dashed lines where one piece of the objective overtakes '
      + 'another, every corner of every part, and the corner the original objective picks.');

    var agree = orig.status === 'optimal' && ref.status === 'optimal' && Requ(orig.value, ref.z);
    kpi('rfK1', 'The original, corner by corner',
        orig.status === 'optimal' ? Rshort(orig.value, 4, 9) : esc(orig.status));
    kpi('rfK2', 'The reformulation, by simplex',
        ref.status === 'optimal' ? Rshort(ref.z, 4, 9) : esc(ref.status));
    kpi('rfK3', 'The two, subtracted',
        (orig.status === 'optimal' && ref.status === 'optimal')
          ? Rshort(Rsub(ref.z, orig.value), 4, 9) : 'no comparison to make');
    kpi('rfK4', 'Is the rewrite the same problem?',
        agree ? tone('yes', 'green') : tone('no', 'red'));

    el('rfStatus').innerHTML = (agree
      ? '<strong>The two agree exactly.</strong> They were computed by different methods on '
        + 'different models &mdash; corners of the original, a tableau of the rewrite &mdash; and '
        + 'the difference between them is exactly zero, which is the only evidence worth having '
        + 'that the rewrite is the same problem. '
      : '<strong>The two disagree, and that is the point.</strong> The rewrite is not the same '
        + 'problem here: it is a different one, with an answer the original cannot reach. '
        + 'A reader who only ran the rewrite would have no way to notice. ')
      + s.why;
  }

  ['rfRule', 'rfDir'].forEach(function (id) {
    document.getElementById(id).addEventListener('change', redraw);
  });
  ['rfP1', 'rfP2', 'rfCap'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""


def _reform(cfg):
    markup = (
        _toolbar("The same problem, written twice",
                 "Corners of the original against a tableau of the rewrite",
                 _swatch("tone-cyan", "the feasible region")
                 + _swatch("tone-purple", "a boundary")
                 + _swatch("tone-muted", "where one piece overtakes another")
                 + _swatch("tone-green", "the original's best corner"))
        + _stage("rfStage", "rfPlot",
                 "The region, the lines where one piece of the objective overtakes another, and "
                 "the corner the original objective picks.")
        + '      <div class="mathblock" id="rfLp" style="margin-top:12px;"></div>\n'
        '      <div id="rfCorners" style="margin-top:12px;"></div>\n'
        '      <div id="rfReform" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="rfStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("rfRule", "Which rewrite",
                [("minmax", "the largest of two expressions, made into one variable"),
                 ("abs", "a size, written without the absolute-value bars"),
                 ("free", "a variable allowed to go negative"),
                 ("band", "a cost quoted in two price bands")], "minmax")
        + _select("rfDir", "Which direction the objective is pushed",
                  [("min", "minimise"), ("max", "maximise")], "min")
        + _range("rfP1", "the first coefficient", 1, 9, 2)
        + _range("rfP2", "the second coefficient", 1, 9, 5)
        + _range("rfCap", "the order that must be met", 0, 24, 12)
        + _kpi([("rfK1", "&mdash;"), ("rfK2", "&mdash;"), ("rfK3", "&mdash;"), ("rfK4", "&mdash;")])
    )
    script = _BASE_JS + _ENGINE_JS + LP_JS + REFORM_JS + _DRAW_JS + REFORM_SCRIPT
    return Lab(
        title="The same problem, written twice",
        subtitle="An auxiliary variable is legal exactly when the direction forces its value",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a rewrite, then flip the direction and watch it break"),
        panel_intro=cfg.get(
            "panel_intro",
            "The original is answered by enumerating the corners of each part of the region on "
            "which one piece of the objective is the one that counts; the rewrite is answered by "
            "the simplex engine. Neither looks at the other. Subtracting them is therefore "
            "evidence, and on three of the four rewrites the difference stops being zero the "
            "moment the direction is flipped."),
        script=script,
    )


# ============================================================ mode: goal
#
# A preemptive goal programme is a SEQUENCE of linear programmes, not one
# linear programme with weights. The reader reorders the priorities; each level
# freezes the deviation the level before it achieved and hands the rest on.

GOAL_ORDERS = [
    ("012", "profit, then overtime, then the deluxe run"),
    ("021", "profit, then the deluxe run, then overtime"),
    ("102", "overtime, then profit, then the deluxe run"),
    ("120", "overtime, then the deluxe run, then profit"),
    ("201", "the deluxe run, then profit, then overtime"),
    ("210", "the deluxe run, then overtime, then profit"),
]

GOAL_SCRIPT = r"""
  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function el(id) { return document.getElementById(id); }
  function out(id, text) { el(id + 'Out').textContent = text; }
  function kpi(id, label, value) { el(id + 'Lab').textContent = label; el(id).innerHTML = value; }
  var GOALNAMES = ['the profit target', 'the overtime limit', 'the deluxe run'];
  var DECIDE = ['S', 'D'];
  var GOALUNIT = ['pounds of profit', 'hours of overtime', 'deluxe units'];

  function readAll() {
    var order = el('glOrder').value.split('').map(function (c) { return parseInt(c, 10); });
    return { order: order, machine: slider('glMach'),
             targets: [slider('glT1'), slider('glT2'), slider('glT3')],
             weight: slider('glW') };
  }
  function buildGoals(d) {
    return [{ a: [ri(3), ri(4)], target: ri(d.targets[0]), mind: 'under', name: GOALNAMES[0] },
            { a: [ri(3), ri(6)], target: ri(d.targets[1]), mind: 'over', name: GOALNAMES[1] },
            { a: [R0, R1], target: ri(d.targets[2]), mind: 'under', name: GOALNAMES[2] }];
  }
  function buildBase(d) {
    return { names: DECIDE,
             cons: [{ a: [ri(2), ri(3)], rel: 'le', b: ri(d.machine), name: 'machine hours' }] };
  }
  function goalLine(g, i) {
    return Ltext(g.a, DECIDE) + ' + u' + (i + 1) + ' - o' + (i + 1)
      + ' = ' + Rtext(g.target);
  }

  function redraw() {
    var d = readAll();
    out('glMach', String(d.machine));
    out('glT1', String(d.targets[0])); out('glT2', String(d.targets[1])); out('glT3', String(d.targets[2]));
    var wr = R(BigInt(d.weight), 4n);
    out('glW', Rtext(wr));
    var base = buildBase(d), goals = buildGoals(d);
    var lex = goalLexicographic(base, goals, d.order);
    var wtd = goalWeighted(base, goals, [wr, R1, R1]);

    el('glLp').innerHTML = '<div>2S + 3D &lt;= ' + d.machine + '&nbsp;&nbsp;'
      + '<span class="tone-muted">machine hours, a hard constraint</span></div>'
      + goals.map(function (g, i) {
          return '<div>' + goalLine(g, i) + '&nbsp;&nbsp;<span class="tone-muted">'
            + esc(g.name) + ', measured in ' + GOALUNIT[i] + '; the one minded is '
            + (g.mind === 'over' ? 'o' : 'u') + (i + 1) + '</span></div>';
        }).join('')
      + '<div>S, D, and every u and o &gt;= 0</div>'
      + '<div class="tone-muted">S = standard cabinets built this week, in units;&nbsp; '
      + 'D = deluxe cabinets built this week, in units;&nbsp; u and o are how far under and how '
      + 'far over its target each goal lands, each in that goal&#39;s own unit</div>';

    var body = [], k;
    for (k = 0; k < lex.levels.length; k += 1) {
      var L = lex.levels[k], g = goals[L.goal];
      var devs = L.result.x ? goalDeviations(base, goals, L.result.x) : null;
      body.push(tr([rowhead('priority ' + (k + 1)),
        tdl(esc(g.name) + ', by driving ' + (g.mind === 'over' ? 'o' : 'u') + (L.goal + 1) + ' down'),
        tdl(L.frozen.length
            ? L.frozen.map(function (f) { return esc(f.name); }).join('; ')
            : tone('nothing frozen yet', 'muted')),
        td(L.achieved === null ? tone('no plan at all', 'red') : Rshort(L.achieved, 4, 9)),
        tdl(L.achieved === null ? '&mdash;'
            : (Rzero(L.achieved)
               ? tone('met exactly', 'green')
               : tone('missed by ' + Rshort(L.achieved, 4, 9) + ' ' + GOALUNIT[L.goal], 'amber'))),
        tdl(devs ? 'S = ' + Rshort(L.result.x[0], 4, 9) + ', D = '
              + Rshort(L.result.x[1], 4, 9) : '&mdash;')]));
    }
    el('glLevels').innerHTML = table('One linear programme per priority level, in the order you chose',
      ['', 'what this level minimises', 'what it carries in, frozen', 'achieved',
       '', 'the plan at this level'], body);

    var wbody = goals.map(function (g, i) {
      var lexAt = -1, q;
      for (q = 0; q < lex.levels.length; q += 1) if (lex.levels[q].goal === i) lexAt = q;
      var lexVal = lexAt >= 0 ? lex.levels[lexAt].achieved : null;
      var wdev = wtd.result.x ? goalDeviations(base, goals, wtd.result.x)[i] : null;
      var wVal = wdev ? (g.mind === 'over' ? wdev.over : wdev.under) : null;
      return tr([rowhead(esc(g.name)), td(GOALUNIT[i]),
                 td(lexVal === null ? '&mdash;' : Rshort(lexVal, 4, 9)),
                 td(wVal === null ? '&mdash;' : Rshort(wVal, 4, 9)),
                 tdl(lexVal !== null && wVal !== null && Requ(lexVal, wVal)
                     ? 'the same either way'
                     : tone('the two methods disagree about this goal', 'amber'))]);
    });
    el('glWeighted').innerHTML = table('Beside it: the same three goals added into ONE objective, '
      + 'with weights and no scaling',
      ['', 'measured in', 'missed, solving level by level', 'missed, with one weighted objective', ''],
      wbody)
      + '<p class="small-copy" id="glWeightSay" style="margin:8px 0 0;">The weighted objective adds '
      + Rtext(wr) + ' times a shortfall in pounds to 1 times an excess in hours to 1 times a '
      + 'shortfall in units, and minimises the total &mdash; ' + Rshort(wtd.result.z, 4, 9)
      + ' here. Nothing in the arithmetic objects to adding pounds to hours, which is exactly why '
      + 'this way of writing it fails quietly rather than loudly.</p>';

    var sacrificed = -1, worst = null, i2;
    for (i2 = 0; i2 < lex.levels.length; i2 += 1) {
      var a = lex.levels[i2].achieved;
      if (a === null || Rzero(a)) continue;
      if (worst === null || Rcmp(a, worst) > 0) { worst = a; sacrificed = lex.levels[i2].goal; }
    }
    for (i2 = 0; i2 < 3; i2 += 1) {
      var lv = null, q2;
      for (q2 = 0; q2 < lex.levels.length; q2 += 1) if (lex.levels[q2].goal === d.order[i2]) lv = lex.levels[q2];
      kpi('glK' + (i2 + 1), 'Priority ' + (i2 + 1) + ': ' + GOALNAMES[d.order[i2]] + ', missed by',
          lv && lv.achieved !== null ? Rshort(lv.achieved, 4, 9) + ' ' + GOALUNIT[d.order[i2]] : '&mdash;');
    }
    kpi('glK4', 'The goal that pays for the others',
        sacrificed < 0 ? tone('none: all three are met', 'green') : esc(GOALNAMES[sacrificed]));

    el('glStatus').innerHTML = (sacrificed < 0
      ? '<strong>Every goal is met at this ordering.</strong> '
      : '<strong>' + esc(GOALNAMES[sacrificed]) + ' is what pays for the rest at this ordering.</strong> ')
      + 'A target is not a constraint. Making one hard would produce "infeasible", and "infeasible" '
      + 'is a worse answer than "missed by ' + (worst === null ? '0' : Rshort(worst, 4, 9))
      + '" when the target was an aspiration in the first place. Reorder the priorities and the '
      + 'sequence of programmes changes, because each level hands the next one a frozen constraint '
      + 'rather than a suggestion.';
  }

  ['glOrder'].forEach(function (id) { document.getElementById(id).addEventListener('change', redraw); });
  ['glMach', 'glT1', 'glT2', 'glT3', 'glW'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""


def _goal(cfg):
    markup = (
        _toolbar("Targets, deviations, and one programme per priority",
                 "Each level freezes what the level above it achieved",
                 _swatch("tone-green", "met exactly")
                 + _swatch("tone-amber", "missed, and by how much")
                 + _swatch("tone-muted", "nothing frozen yet"))
        + '      <div class="mathblock" id="glLp"></div>\n'
        '      <div id="glLevels" style="margin-top:12px;"></div>\n'
        '      <div id="glWeighted" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="glStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("glOrder", "Which goal comes first", GOAL_ORDERS, "012")
        + _range("glMach", "machine hours the shop has", 20, 90, 60)
        + _range("glT1", "profit the plan aims at", 20, 120, 60)
        + _range("glT2", "overtime hours the plan aims to stay under", 6, 60, 30)
        + _range("glT3", "deluxe units the plan aims to build", 0, 20, 12)
        + _range("glW", "weight on a pound of profit, in quarters", 0, 16, 4)
        + _kpi([("glK1", "&mdash;"), ("glK2", "&mdash;"), ("glK3", "&mdash;"), ("glK4", "&mdash;")])
    )
    script = _BASE_JS + _ENGINE_JS + LP_JS + GOAL_JS + GOAL_SCRIPT
    return Lab(
        title="Targets, deviations, and one programme per priority",
        subtitle="A preemptive goal programme is a sequence of linear programmes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Reorder the priorities and watch which goal pays"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each target carries two deviation variables and only the one you mind is penalised. "
            "The levels are solved in the order you choose, and each one freezes the deviation it "
            "achieved as a constraint before the next begins. Beside it is the same three goals "
            "added into a single weighted objective, in three different units, with the answer "
            "that produces."),
        script=script,
    )


# ======================================================== mode: standard
#
# Standard form is a MODELLING act rather than a clerical one, which is why it
# belongs on this course: every added variable measures something in the
# situation, and or_core's stdForm is the function that knows what.

STANDARD_SCRIPT = r"""
  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function el(id) { return document.getElementById(id); }
  function out(id, text) { el(id + 'Out').textContent = text; }
  function kpi(id, label, value) { el(id + 'Lab').textContent = label; el(id).innerHTML = value; }
  function pointtext(p) { return '(' + p.map(function (v) { return Rshort(v, 4, 9); }).join(', ') + ')'; }

  function buildModel(d) {
    return { max: false, names: ['F', 'G'], obj: [ri(3), ri(d.cost)],
      cons: [{ a: [R1, R1], rel: 'ge', b: ri(d.b1), name: 'the delivery contract' },
             { a: [ri(2), R1], rel: d.rel, b: ri(d.b2), name: 'the kiln' },
             { a: [R1, R0], rel: 'le', b: ri(d.b3), name: 'the licence' }] };
  }

  function redraw() {
    var d = { b1: slider('stB1'), b2: slider('stB2'), b3: slider('stB3'),
              cost: slider('stCost'), rel: el('stRel').value };
    out('stB1', String(d.b1)); out('stB2', String(d.b2));
    out('stB3', String(d.b3)); out('stCost', String(d.cost));
    var model = buildModel(d);
    var res = lpSolveModel(model);
    var std = stdForm(model);

    el('stLp').innerHTML = '<div>' + lpObjText(model) + '&nbsp;&nbsp;<span class="tone-muted">'
      + 'which the engine runs as maximise ' + Ltext(model.obj.map(Rneg), model.names)
      + ' and negates back</span></div><div>subject to</div>'
      + model.cons.map(function (k) {
          return '<div>&nbsp;&nbsp;' + lpRowText(k, model.names) + '&nbsp;&nbsp;'
            + '<span class="tone-muted">' + esc(k.name) + '</span></div>';
        }).join('')
      + '<div>&nbsp;&nbsp;' + lpSignText(model) + '</div>'
      + '<div class="tone-muted">F = pieces fired and left plain;&nbsp; G = pieces fired and '
      + 'glazed &mdash; both counted in pieces a day</div>';

    /* Every column of the equality standard form, with the sentence stdForm
       carries for it. A surplus is SUBTRACTED, and that sign is not a
       convention: add it instead and the variable is forced negative at every
       feasible point, which breaks the x >= 0 the whole form is built on. */
    var cols = [], j;
    var DECIDES = ['pieces fired and left plain, counted in pieces a day',
                   'pieces fired and glazed, counted in pieces a day'];
    for (j = 0; j < std.n; j += 1) {
      cols.push(tr([rowhead('<span class="tt">' + std.names[j] + '</span>'),
                    td(std.kinds[j]),
                    td(j < std.nd ? '&mdash;'
                       : (std.kinds[j] === 'slack' ? 'added to its row'
                          : (std.kinds[j] === 'surplus' ? tone('subtracted from its row', 'amber')
                             : 'added to its row'))),
                    tdl(j < std.nd ? DECIDES[j] : std.sentences[j])]));
    }
    el('stCols').innerHTML = table('Every column of  minimise c.x subject to Ax = b, x at or above zero',
      ['', 'what kind of column', 'how it enters its row', 'what it measures in the situation'], cols);

    /* The artificial columns are deliberately NOT in this table. They exist to
       give Phase I a basis to start from and they are zero at every feasible
       point, so a column of zeros beside the slacks would say something about
       the search rather than about the situation. */
    var added = [], i;
    for (j = std.nd; j < std.n; j += 1) if (std.kinds[j] !== 'artificial') added.push(j);
    var nArt = std.n - std.nd - added.length;
    var heads = ['corner'].concat(added.map(function (q) {
      return '<span class="tt">' + std.names[q] + '</span>';
    })).concat(['the objective there', '']);
    var body = [];
    for (i = 0; i < res.corners.length; i += 1) {
      var c = res.corners[i];
      if (!c.inRegion) continue;
      var sr = lpSlackRows(model, [c.x, c.y]);
      var cells = [rowhead(pointtext([c.x, c.y]))];
      for (j = 0; j < added.length; j += 1) {
        var row = -1, q;
        for (q = 0; q < std.m; q += 1) if (std.rowSlack[q] === added[j]) row = q;
        var v = row >= 0 ? sr.rows[row].value : null;
        cells.push(td(v === null ? '&mdash;'
          : (Rzero(v) ? tone('0', 'amber') : Rshort(v, 4, 9))));
      }
      cells.push(td(Rshort(c.z, 4, 9)));
      cells.push(td(i === res.best ? tone('the cheapest', 'green') : ''));
      body.push(tr(cells));
    }
    el('stTable').innerHTML = table('Every slack and surplus at every corner: the zeros are the tight rows',
      heads, body)
      + '<p class="small-copy" id="stArtSay" style="margin:8px 0 0;">'
      + (nArt === 0
         ? 'Every row here is a <= with a right-hand side at or above zero, so the slack basis is '
           + 'already feasible and no artificial column was needed at all.'
         : (nArt + ' artificial ' + plural(nArt, 'column is', 'columns are') + ' left out of this '
            + 'table: they exist only to give the search a basis to start from, each is zero at '
            + 'every feasible point, and so they measure nothing about the pottery.'))
      + '</p>';

    var stage = el('stStage'), svg = el('stPlot');
    var pts = [];
    for (i = 0; i < res.corners.length; i += 1) pts.push([res.corners[i].x, res.corners[i].y]);
    if (!pts.length) pts.push([R0, R0]);
    var drawn = lpDrawRegion(svg, res.cons, pts);
    for (i = 0; i < res.corners.length; i += 1) {
      if (!res.corners[i].inRegion) continue;
      drawn.plot.point(Rnum(res.corners[i].x), Rnum(res.corners[i].y),
        i === res.best ? 'plot-end' : 'plot-point',
        i === res.best ? pointtext([res.corners[i].x, res.corners[i].y]) : '');
    }
    drawn.plot.describe('The feasible region with every corner marked and the cheapest one picked out.');

    var tightCols = 0;
    if (res.x) {
      var sr2 = lpSlackRows(model, res.x);
      for (i = 0; i < sr2.rows.length; i += 1) if (sr2.rows[i].tight) tightCols += 1;
    }
    kpi('stK1', 'The smallest cost', res.z === null ? 'none' : Rshort(res.z, 4, 9));
    kpi('stK2', 'The same thing the engine maximised',
        res.z === null ? 'none' : Rshort(Rneg(res.z), 4, 9));
    kpi('stK3', 'Columns after the two decisions', String(std.n - std.nd));
    kpi('stK4', 'Rows tight at the winning corner',
        res.x ? String(tightCols) + ' of ' + String(model.cons.length) : '&mdash;');

    el('stStatus').innerHTML = (res.status === 'optimal'
      ? '<strong>The cheapest plan costs ' + Rshort(res.z, 4, 9) + ' at ' + pointtext(res.x)
        + '.</strong> The engine reported ' + Rshort(Rneg(res.z), 4, 9) + ' and this page negated '
        + 'it back, which is the step that is usually forgotten: both numbers are on the panel so '
        + 'that neither can be mistaken for the other. '
      : '<strong>' + (res.status === 'infeasible'
          ? 'No plan satisfies every row at once.' : 'The cost runs away: there is no smallest.')
        + '</strong> ')
      + 'Read the table as a column of zeros rather than as a claim: a row is tight exactly where '
      + 'its own added variable is zero, and that is what "tight" means. The kiln row is currently '
      + (el('stRel').value === 'le'
         ? 'an upper limit, so it carries a slack that is ADDED.'
         : 'a requirement, so it carries a surplus that is SUBTRACTED. Adding it instead would '
           + 'force that variable negative at every feasible point, and the whole form rests on '
           + 'its being at or above zero.');
  }

  document.getElementById('stRel').addEventListener('change', redraw);
  ['stB1', 'stB2', 'stB3', 'stCost'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""


def _standard(cfg):
    markup = (
        _toolbar("Slack, surplus, and what each of them measures",
                 "Tight if and only if the added variable is zero",
                 _swatch("tone-cyan", "the feasible region")
                 + _swatch("tone-amber", "a zero, which is a tight row")
                 + _swatch("tone-green", "the cheapest corner"))
        + _stage("stStage", "stPlot",
                 "The feasible region with every corner marked and the cheapest picked out.")
        + '      <div class="mathblock" id="stLp" style="margin-top:12px;"></div>\n'
        '      <div id="stCols" style="margin-top:12px;"></div>\n'
        '      <div id="stTable" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="stStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("stRel", "The kiln row is",
                [("le", "an upper limit, so it takes a slack"),
                 ("ge", "a requirement, so it takes a surplus")], "le")
        + _range("stB1", "pieces the delivery contract demands", 1, 12, 4)
        + _range("stB2", "the kiln figure", 4, 20, 10)
        + _range("stB3", "pieces the licence allows to be fired", 1, 10, 4)
        + _range("stCost", "what one glazed piece costs to make", 1, 9, 5)
        + _kpi([("stK1", "&mdash;"), ("stK2", "&mdash;"), ("stK3", "&mdash;"), ("stK4", "&mdash;")])
    )
    script = _BASE_JS + _ENGINE_JS + LP_JS + _DRAW_JS + STANDARD_SCRIPT
    return Lab(
        title="Slack, surplus, and what each of them measures",
        subtitle="Adding a surplus instead of subtracting it forces the variable negative",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Flip the kiln row and watch its new column change kind"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every added column is named and given a meaning in the situation rather than a "
            "letter. The table underneath evaluates all of them at every corner, so that "
            "“tight if and only if the slack is zero” is a column of zeros you can read "
            "rather than a sentence you are asked to accept."),
        script=script,
    )


# ========================================================== mode: basic
#
# Choosing which variables are zero and solving the rest is what replaces the
# drawing as soon as there are more than two variables. Here the drawing is
# still available, so every basic solution can be put on it -- including the
# ones that land outside the region, which are exactly the crossings the
# picture rejects.

BASIC_SCRIPT = r"""
  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function el(id) { return document.getElementById(id); }
  function out(id, text) { el(id + 'Out').textContent = text; }
  function kpi(id, label, value) { el(id + 'Lab').textContent = label; el(id).innerHTML = value; }
  function pointtext(p) { return '(' + p.map(function (v) { return Rshort(v, 4, 9); }).join(', ') + ')'; }
  var KINDTONE = { feasible: 'green', degenerate: 'amber', infeasible: 'red', singular: 'muted' };

  function buildModel(d) {
    return { max: true, names: ['C', 'T'], obj: [ri(3), ri(5)],
      cons: [{ a: [R1, R0], rel: 'le', b: ri(d.a1), name: 'the carpentry shop' },
             { a: [R0, ri(2)], rel: 'le', b: ri(d.a2), name: 'the finishing shop' },
             { a: [ri(3), ri(2)], rel: 'le', b: ri(d.a3), name: 'the assembly line' }] };
  }

  function redraw() {
    var d = { a1: slider('bsA1'), a2: slider('bsA2'), a3: slider('bsA3') };
    out('bsA1', String(d.a1)); out('bsA2', String(d.a2)); out('bsA3', String(d.a3));
    var model = buildModel(d);
    var bt = lpBasisTable(model);
    var pick = Math.max(0, Math.min(bt.rows.length - 1, slider('bsPick')));
    out('bsPick', String(pick + 1) + ' of ' + String(bt.rows.length));

    var counts = { feasible: 0, degenerate: 0, infeasible: 0, singular: 0 };
    var body = bt.rows.map(function (b, i) {
      counts[b.solve.kind] += 1;
      return tr([rowhead('<span class="tt">{'
          + b.basis.map(function (j) { return bt.std.names[j]; }).join(', ') + '}</span>'),
        tdl(b.nonbasic.map(function (j) { return bt.std.names[j]; }).join(' and ') + ' set to zero'),
        tdl(b.lines.map(function (L) { return esc(L.text); }).join('&nbsp; with &nbsp;')),
        td(b.solve.singular ? '&mdash;' : pointtext([b.solve.x[0], b.solve.x[1]])),
        td(b.z === null ? '&mdash;' : Rshort(b.z, 4, 9)),
        td(tone(b.solve.kind, KINDTONE[b.solve.kind])),
        td(i === pick ? tone('traced below', 'cyan') : '')]);
    });
    el('bsLegend').innerHTML = 'C = chairs made this week and T = tables made this week, both in '
      + 'units; s1, s2 and s3 are the hours each shop has left over, in that shop&#39;s own hours. '
      + 'Choosing which two of the five are zero is choosing a basis.';
    el('bsTable').innerHTML = table('Every choice of which variables are zero, solved exactly',
      ['the basis', 'set to zero', 'which two lines that puts the point on', 'the point',
       'the objective there', '', ''], body);

    var b = bt.rows[pick];
    var heads = b.basis.map(function (j) { return bt.std.names[j]; }).concat(['=']);
    el('bsTrace').innerHTML = Mtable('The basis columns and the right-hand side, before reducing',
        b.solve.aug, { split: bt.std.m, heads: heads })
      + Mtrace('Row reduction on those columns, one operation at a time',
        b.solve.aug, b.solve.red.ops, { split: bt.std.m, heads: heads })
      + '<p class="small-copy" id="bsSay" style="margin:8px 0 0;">'
      + (b.solve.singular
         ? tone('The reduction stops at rank ' + b.solve.red.rank + ' out of ' + bt.std.m
                + ': these columns are dependent, which in the picture is the two lines '
                + b.lines.map(function (L) { return esc(L.text); }).join(' and ')
                + ' being parallel. There is no point to find, so this choice is not a basic '
                + 'solution at all.', 'muted')
         : (b.solve.feasible
            ? tone('Every basic variable came out at or above zero, so this basic solution IS a '
                   + 'corner of the region'
                   + (b.solve.degenerate
                      ? ' &mdash; and one of them came out exactly zero, so more than two '
                        + 'boundaries pass through that corner and several bases describe it.'
                      : '.'), 'green')
            : tone('Basic variable' + (b.solve.negative.length === 1 ? ' ' : 's ')
                   + b.solve.negative.map(function (j) { return bt.std.names[j]; }).join(', ')
                   + ' came out negative. The two lines do cross, and the crossing is outside the '
                   + 'region: this is a basic solution that is not a corner, and the negative entry '
                   + 'is what rejects it.', 'red')))
      + '</p>';

    var svg = el('bsPlot'), pts = [], i;
    for (i = 0; i < bt.rows.length; i += 1) {
      if (!bt.rows[i].solve.singular) pts.push([bt.rows[i].solve.x[0], bt.rows[i].solve.x[1]]);
    }
    if (!pts.length) pts.push([R0, R0]);
    var drawn = lpDrawRegion(svg, bt.cons, pts);
    for (i = 0; i < bt.rows.length; i += 1) {
      var q = bt.rows[i];
      if (q.solve.singular) continue;
      var x = Rnum(q.solve.x[0]), y = Rnum(q.solve.x[1]);
      if (q.solve.feasible) drawn.plot.point(x, y, i === pick ? 'plot-end' : 'plot-point',
        i === pick ? pointtext([q.solve.x[0], q.solve.x[1]]) : '');
      else drawn.plot.hole(x, y);
    }
    drawn.plot.describe('Every basic solution on the picture: the feasible ones filled, the '
      + 'infeasible ones drawn as open circles outside the region.');

    kpi('bsK1', 'Bases there are to try', String(bt.count));
    kpi('bsK2', 'Of them, basic FEASIBLE solutions',
        String(counts.feasible + counts.degenerate));
    kpi('bsK3', 'Crossings the region rejects', String(counts.infeasible));
    kpi('bsK4', 'Choices that are not a basis at all',
        String(counts.singular) + ' singular, ' + String(counts.degenerate) + ' degenerate');

    el('bsStatus').innerHTML = '<strong>' + String(bt.count) + ' bases, '
      + String(counts.feasible + counts.degenerate) + ' of them feasible, '
      + String(bt.corners.length) + ' corners on the picture.</strong> '
      + 'Not every basic solution is a corner: ' + String(counts.infeasible) + ' of these are '
      + 'crossings of two boundary lines that sit outside the region, and what rejects them is a '
      + 'negative entry rather than a look at the diagram. '
      + (counts.degenerate
         ? 'Three boundaries currently pass through one corner, so ' + String(counts.degenerate)
           + ' different bases all describe that same point &mdash; which is why the number of '
           + 'corners is smaller than the number of basic feasible solutions.'
         : 'The count above is what makes an algorithm necessary: it is the number of bases to '
           + 'try, and it grows far faster than the picture does.');
  }

  ['bsA1', 'bsA2', 'bsA3', 'bsPick'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""


def _basic(cfg):
    markup = (
        _toolbar("Every basis, solved and classified",
                 "Feasible, infeasible, singular or degenerate, and where each one lands",
                 _swatch("tone-green", "a basic feasible solution")
                 + _swatch("tone-red", "a crossing outside the region")
                 + _swatch("tone-muted", "two parallel lines, so no point at all"))
        + _stage("bsStage", "bsPlot",
                 "Every basic solution on the picture, the infeasible ones drawn outside the region.")
        + '      <p class="small-copy" id="bsLegend" style="margin-top:12px;"></p>\n'
        '      <div id="bsTable" style="margin-top:12px;"></div>\n'
        '      <div id="bsTrace" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="bsStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _range("bsA1", "bench hours available in the carpentry shop", 1, 12, 4)
        + _range("bsA2", "hours available in the finishing shop", 2, 24, 12)
        + _range("bsA3", "hours available on the assembly line", 6, 30, 18)
        + _range("bsPick", "which basis to reduce, step by step", 0, 9, 0)
        + _kpi([("bsK1", "&mdash;"), ("bsK2", "&mdash;"), ("bsK3", "&mdash;"), ("bsK4", "&mdash;")])
    )
    script = (_BASE_JS + BIGINT_JS + MATRIX_JS + _ENGINE_JS + LP_JS + BASIS_JS
              + _DRAW_JS + BASIC_SCRIPT)
    return Lab(
        title="Every basis, solved and classified",
        subtitle="A basic feasible solution is a corner; a basic solution need not be",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Walk the bases while the picture is still there to check them"),
        panel_intro=cfg.get(
            "panel_intro",
            "Choosing which variables are zero and solving the rest by row reduction gives a basic "
            "solution; one with no negative entry is a corner. Every basis here is reduced by the "
            "same Mrref the elimination lessons used, and the trace for whichever one you pick is "
            "printed underneath. Push the assembly line up until three boundaries meet at one "
            "point and watch several bases collapse onto one corner."),
        script=script,
    )


# ========================================================= mode: convex
#
# The segment between two feasible points is feasible, and a linear objective
# is affine along it; so a feasible point from which no feasible direction
# improves cannot be beaten anywhere. That is the licence the simplex method
# needs in order to stop, and the non-convex setting is where it is withdrawn.

CONVEX_SCRIPT = r"""
  function ri(v) { return R(BigInt(v), 1n); }
  function slider(id) { return parseInt(document.getElementById(id).value, 10) || 0; }
  function el(id) { return document.getElementById(id); }
  function out(id, text) { el(id + 'Out').textContent = text; }
  function kpi(id, label, value) { el(id + 'Lab').textContent = label; el(id).innerHTML = value; }
  function pointtext(p) { return '(' + p.map(function (v) { return Rshort(v, 4, 9); }).join(', ') + ')'; }
  var SAMPLES = 8;

  function boxCons(x0, x1, y0, y1, name) {
    return [Cnew(ri(-1), R0, ri(-x0), false, name), Cnew(R1, R0, ri(x1), false, name),
            Cnew(R0, ri(-1), ri(-y0), false, name), Cnew(R0, R1, ri(y1), false, name)];
  }
  /* The convex setting is one polyhedron; the non-convex one is the UNION of
     two blocks, which is a set no single list of half-planes can express --
     which is why this piece is the kit's own and not Cnew's. */
  function blocksOf(kind) {
    if (kind === 'convex') {
      var m = { max: true, names: ['x', 'y'], obj: [R0, R0],
        cons: [{ a: [R1, R1], rel: 'le', b: ri(8), name: 'the shared line' },
               { a: [R1, R0], rel: 'le', b: ri(5), name: 'the eastern limit' },
               { a: [R0, R1], rel: 'le', b: ri(6), name: 'the northern limit' }] };
      return [{ name: 'the feasible set', cons: lpHalfPlanes(m) }];
    }
    return [{ name: 'the western block', cons: boxCons(0, 3, 0, 6, 'the western block') },
            { name: 'the eastern block', cons: boxCons(5, 8, 0, 6, 'the eastern block') }];
  }

  function redraw() {
    var kind = el('cxSet').value;
    var c1 = slider('cxObj');
    var p = [ri(slider('cxPX')), ri(slider('cxPY'))];
    var q = [ri(slider('cxQX')), ri(slider('cxQY'))];
    out('cxObj', String(c1)); out('cxPX', String(slider('cxPX'))); out('cxPY', String(slider('cxPY')));
    out('cxQX', String(slider('cxQX'))); out('cxQY', String(slider('cxQY')));
    var obj = [ri(c1), ri(2)];
    var blocks = blocksOf(kind), i, b;

    var inP = [], inQ = [];
    for (i = 0; i < blocks.length; i += 1) {
      if (setHolds(blocks[i].cons, p[0], p[1])) inP.push(i);
      if (setHolds(blocks[i].cons, q[0], q[1])) inQ.push(i);
    }
    var intervals = blocks.map(function (bk) { return segInterval(bk.cons, p, q); });
    var cover = segCovered(intervals);
    var samples = segSamples(p, q, obj, SAMPLES);

    el('cxSamples').innerHTML = table('The objective along the segment, sampled at exact fractions of it',
      ['t', 'the point there', 'the objective', 'change since the row above', 'is it in the set?'],
      samples.rows.map(function (r) {
        var inside = false;
        for (var k = 0; k < blocks.length; k += 1) {
          if (setHolds(blocks[k].cons, r.point[0], r.point[1])) inside = true;
        }
        return tr([rowhead(Rtext(r.t)), td(pointtext(r.point)), td(Rshort(r.value, 4, 9)),
                   td(r.diff === null ? '&mdash;' : Rshort(r.diff, 4, 9)),
                   td(inside ? tone('yes', 'green') : tone('no', 'red'))]);
      }));

    var mbody = blocks.map(function (bk, k) {
      var I = intervals[k];
      return tr([rowhead(esc(bk.name)),
                 tdl(I.empty ? tone('no part of the segment lies in it', 'muted')
                     : 'from t = ' + Rtext(I.lo) + ' to t = ' + Rtext(I.hi)),
                 td(inP.indexOf(k) >= 0 ? tone('yes', 'green') : tone('no', 'muted')),
                 td(inQ.indexOf(k) >= 0 ? tone('yes', 'green') : tone('no', 'muted'))]);
    });
    var best = blocks.map(function (bk) { return setBest(bk.cons, obj, true); });
    var bestAll = -1;
    for (i = 0; i < best.length; i += 1) {
      if (best[i].z === null) continue;
      if (bestAll < 0 || Rcmp(best[i].z, best[bestAll].z) > 0) bestAll = i;
    }
    var lbody = blocks.map(function (bk, k) {
      return tr([rowhead(esc(bk.name)),
                 td(best[k].x ? pointtext(best[k].x) : '&mdash;'),
                 td(best[k].z === null ? '&mdash;' : Rshort(best[k].z, 4, 9)),
                 tdl(k === bestAll
                     ? tone('the best point of the whole set', 'green')
                     : tone('a LOCAL best: no step inside this block improves on it, and it is '
                            + 'beaten from outside', 'red'))]);
    });
    el('cxWhere').innerHTML = table('Which part of the segment lies where',
        ['', 'the part of the segment inside it', 'is your first point in it?',
         'is your second point in it?'], mbody)
      + table('The best corner of each piece, and whether it is the best anywhere',
        ['', 'at', 'the objective there', ''], lbody);

    var svg = el('cxPlot');
    var pts = [p, q];
    for (i = 0; i < best.length; i += 1) if (best[i].x) pts.push(best[i].x);
    for (i = 0; i < blocks.length; i += 1) {
      var cs = Ccorners(blocks[i].cons);
      for (var j = 0; j < cs.length; j += 1) pts.push([cs[j].x, cs[j].y]);
    }
    var win = lpWindow(pts);
    var plot = Plot(svg, win);
    plot.frame();
    for (i = 0; i < blocks.length; i += 1) {
      lpShade(plot, blocks[i].cons, 'plot-shade');
      blocks[i].cons.forEach(function (k) { lpLine(plot, k.a, k.b, k.c, win, 'plot-curve'); });
    }
    plot.segment(Rnum(p[0]), Rnum(p[1]), Rnum(q[0]), Rnum(q[1]), 'plot-aux');
    for (i = 0; i < samples.rows.length; i += 1) {
      var r = samples.rows[i], insideAny = false;
      for (var k2 = 0; k2 < blocks.length; k2 += 1) {
        if (setHolds(blocks[k2].cons, r.point[0], r.point[1])) insideAny = true;
      }
      if (insideAny) plot.point(Rnum(r.point[0]), Rnum(r.point[1]), 'plot-point', '');
      else plot.hole(Rnum(r.point[0]), Rnum(r.point[1]));
    }
    for (i = 0; i < best.length; i += 1) {
      if (!best[i].x) continue;
      plot.point(Rnum(best[i].x[0]), Rnum(best[i].x[1]),
        i === bestAll ? 'plot-end' : 'plot-hole',
        (i === bestAll ? 'best anywhere ' : 'best in this block ') + pointtext(best[i].x));
    }
    plot.describe('The set, the segment between the two points you chose, the sampled points along '
      + 'it filled where they are inside and open where they are not, and the best corner of each '
      + 'piece of the set.');

    var bothIn = inP.length > 0 && inQ.length > 0;
    kpi('cxK1', 'The objective at your first point', Rshort(samples.rows[0].value, 4, 9));
    kpi('cxK2', 'The objective at your second point',
        Rshort(samples.rows[samples.rows.length - 1].value, 4, 9));
    kpi('cxK3', 'Change per eighth of the way',
        samples.constant ? Rshort(samples.step, 4, 9) + ', the same every step'
          : tone('not the same every step', 'red'));
    kpi('cxK4', 'Does the whole segment stay in the set?',
        !bothIn ? tone('one of your points is outside it', 'amber')
          : (cover.covered ? tone('yes', 'green') : tone('no', 'red')));

    var head;
    if (!bothIn) {
      head = '<strong>Pick two points that are both in the set.</strong> Convexity is a claim about '
        + 'the segment between two points OF the set, so it says nothing until both ends are in it. ';
    } else if (cover.covered) {
      head = '<strong>The whole segment stays inside.</strong> ';
    } else {
      head = '<strong>The segment leaves the set at t = ' + Rtext(cover.gapAt === null ? cover.reach : cover.reach)
        + '.</strong> ';
    }
    var affine = samples.constant
      ? 'Along the segment the objective changes by exactly ' + Rshort(samples.step, 4, 9)
        + ' at every one of the eight steps. That constant first difference IS what affine means, '
        + 'and it is why a linear objective can never have a bump in the middle of a segment to '
        + 'hide a better point in. '
      : 'The first differences are not constant, which would be a bug in this lab rather than a '
        + 'lesson: a linear objective is affine along any segment. ';
    var stop = (kind === 'convex')
      ? 'Put the two together. Every segment between two feasible points is feasible, and the '
        + 'objective is affine along each of them; so a feasible point with no improving feasible '
        + 'direction cannot be beaten by any feasible point at all. That is a proof of GLOBAL '
        + 'optimality from a purely local check, and it is the licence an algorithm needs in order '
        + 'to stop. The corner point theorem is not that licence: it says an optimum can be found '
        + 'at a corner, and says nothing about the corner you happen to be standing on.'
      : 'Here the licence is withdrawn, and you can see the exact step where. The set is a union '
        + 'of two blocks, the segment between a point of one and a point of the other leaves it, '
        + 'and the best corner of the poorer block has no improving step available inside its own '
        + 'block while being beaten from outside. A local check therefore proves nothing, which is '
        + 'the situation convexity exists to rule out.';
    el('cxStatus').innerHTML = head + affine + stop;
  }

  document.getElementById('cxSet').addEventListener('change', redraw);
  ['cxObj', 'cxPX', 'cxPY', 'cxQX', 'cxQY'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""


def _convex(cfg):
    markup = (
        _toolbar("A segment, and the objective along it",
                 "Constant first differences are what affine means",
                 _swatch("tone-cyan", "the set")
                 + _swatch("tone-purple", "the segment you chose")
                 + _swatch("tone-green", "the best point anywhere")
                 + _swatch("tone-red", "a sample that has left the set"))
        + _stage("cxStage", "cxPlot",
                 "The set, the segment between the two chosen points, and the best corner of each "
                 "piece of the set.")
        + '      <div id="cxSamples" style="margin-top:12px;"></div>\n'
        '      <div id="cxWhere" style="margin-top:12px;"></div>\n'
        '      <div class="status-banner" id="cxStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("cxSet", "Which set to work in",
                [("convex", "one polyhedron, which is convex"),
                 ("union", "two blocks with a gap between them, which is not")], "convex")
        + _range("cxPX", "first point, across", 0, 8, 1)
        + _range("cxPY", "first point, up", 0, 6, 1)
        + _range("cxQX", "second point, across", 0, 8, 5)
        + _range("cxQY", "second point, up", 0, 6, 3)
        + _range("cxObj", "what one unit across is worth", -4, 8, 3)
        + _kpi([("cxK1", "&mdash;"), ("cxK2", "&mdash;"), ("cxK3", "&mdash;"), ("cxK4", "&mdash;")])
    )
    script = _BASE_JS + LP_JS + SEG_JS + _DRAW_JS + CONVEX_SCRIPT
    return Lab(
        title="A segment, and the objective along it",
        subtitle="No improving direction proves global optimality only when the set is convex",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose two points, then take the gap away from under them"),
        panel_intro=cfg.get(
            "panel_intro",
            "The objective is evaluated at nine exact fractions of the way along the segment and "
            "its first differences are printed beside it. Whether the segment stays inside is "
            "decided rather than sampled: the condition collapses to one interval of t per block, "
            "and a union of two intervals either covers the whole segment or leaves a gap the "
            "panel names."),
        script=script,
    )


# ---------------------------------------------------------------- the kit

_BUILDERS = {
    "model": _model,
    "reform": _reform,
    "goal": _goal,
    "standard": _standard,
    "basic": _basic,
    "convex": _convex,
}

MODES = tuple(_BUILDERS)


def lp_lab(cfg):
    """Linear programming models: six modes, four presets, ten lessons.

    An unknown mode RAISES, and so does an unknown preset and an unknown view.
    The alternative -- falling back to the first of each -- ships a page that
    builds, renders, redraws and passes every markup assertion in the suite
    while showing a reader the widget for a different lesson.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "lp: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["LP_JS", "BLEND_JS", "GOAL_JS", "BASIS_JS", "SEG_JS", "REFORM_JS", "REGION_JS",
           "MODES", "MODEL_KEYS", "MODEL_VIEWS", "lp_lab"]


def _assert_the_rendering_keys_separate_the_lessons():
    """The one place the preset mechanism does not discharge the guard itself.

    Two of the five modelling lessons open on the same preset, ``mix``, and are
    told apart by ``view`` alone. The suite's duplicate-render guard compares
    (kit, mode) pairs of lessons that are in use, so it cannot see this until a
    course exists to name both -- and by then the page looks finished. Building
    every (preset, view) pair here costs a twentieth of a second at import and
    turns "a reviewer will remember" into an assertion.
    """
    seen = {}
    for key in MODEL_KEYS:
        for view in MODEL_VIEWS:
            lab = _model({"mode": "model", "preset": key, "view": view})
            seen.setdefault(lab.markup + lab.controls + lab.script, []).append((key, view))
    clashes = [v for v in seen.values() if len(v) > 1]
    if clashes:
        raise AssertionError(
            "lp mode 'model' renders identically for %s, so one of those lessons would "
            "show another lesson's widget" % clashes
        )


_assert_the_rendering_keys_separate_the_lessons()
