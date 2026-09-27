"""Duality and sensitivity analysis: one kit, ten modes, one per lesson.

WHAT THIS KIT IS FOR.  Every linear programme carries a second one whose
variables are prices, and the simplex method has been solving both the whole
time.  The ten modes walk that fact from "how do you write it down" to "a
zero-sum game has a value", and every number on every one of them is computed
in the browser from the model the lesson just stated.

THE MODES, and the one that is not here:

    construct    the dual built pairing by pairing, and the dual of the dual
    certificate  c'x <= y'Ax <= b'y with exact numbers at each link
    read         y = c_B' B^-1 read off the final tableau, checked column by column
    slackness    a claimed optimum certified or refuted, with no simplex run
    rhs          z*(b_i) as an exact piecewise-linear function of one right-hand side
    cost         the range of one objective coefficient, and the pivot at its end
    newcol       price a column that is not in the model, and test a row that is not
    dualsimplex  a cut added and feasibility restored, one dual ratio test at a time
    parametric   the efficient frontier of two objectives, with exact breakpoints
    game         a zero-sum game as a pair of dual programmes

`newrow` is NOT a mode.  A lesson names exactly one mode and the lesson that
would need it -- pricing a new activity and adding a constraint -- is one
lesson, so `newcol` carries both panels.  Adding an eleventh mode would leave
it unreachable and would make one more page for a reader to download.

WHAT IS RE-USED RATHER THAN RE-DERIVED.  or_core's mathcheck section already
proves, on 178 two-variable programmes that agree with corner enumeration, that
the reported point is feasible and attains z, that y'b = z*, that y'A - c >= 0
column by column, and that B^-1 A rebuilt from the ORIGINAL matrix is the
tableau entry for entry -- on <=, >=, = and flipped rows alike, and at every
rhsRange endpoint against a fresh solve plus a point a hundredth outside that
must break the prediction.  This kit's job is to make that visible.  So
dualModel, lpSolve, dualVector, basisInverse, rhsRange, rhsCurve, costRange,
paramFront, priceColumn, addRow, dualPivot, dualRatio and dualSimplexRun are
CALLED here, never re-implemented, and DUALITY_KIT_JS below holds only the
three things course three asks for that the engine does not already do.

PAGE WEIGHT, and what was left out because of it.  This is the heaviest kit on
its path after `schedule` and `integer`, so the block list is a decision rather
than a formality.  Three blocks the design table named are not taken:

  * `algebra_systems.LINEAR_JS` is a linear-expression PARSER over an
    expression AST it does not ship -- Lof and Lequation read nodes that only
    `algebra_core.EXPR_JS` produces -- so taking it means taking EXPR_JS too,
    or shipping a parser whose entry points throw.  The three printers this kit
    actually wanted out of it (relhtml, a row as text, a row evaluated at a
    point) are twenty lines, and they are in DUALITY_KIT_JS where mathcheck can
    call them.
  * `counting.BIGINT_JS` is not referenced by any block this kit loads, and
    nothing here counts arrangements.  Shipping fact/perm/comb unreferenced on
    ten pages is 0.4 KB gzipped of code no reader can reach.
  * `algebra_core.PLOT_JS` is 3.6 KB gzipped for two figures -- the piecewise
    z*(b) curve and the (f1, f2) front -- that are a polyline and a scatter of
    at most a dozen points each.  Section four's cut order names this cut
    explicitly; `pxOf` and `spanOf` below are what replaced it, and both are
    exact until the last step, where a PIXEL is allowed to round and the number
    it stands for is printed beside it in full.

MEASURED, on a rendered lesson page and not on the lab alone, because the lab
alone is not what a reader downloads.  The ceiling is 62 KB gzipped (root
AGENTS.md, "A note on page weight"); the ten pages of this kit come in between
51.7 and 52.6 KB, the heaviest being `newcol`, which carries two panels.  About
30 KB of that is chrome and prose and 22 KB is the engine, so each mode's own
driver is 1 to 2 KB gzipped.

That fits because EVERY MODE SHIPS ONLY ITS OWN DRIVER.  One Python function
per mode means render.py builds one script for the lesson it is rendering,
rather than one script carrying all ten -- which is what the page-weight note
in AGENTS.md describes for the older single-function labs, and is why ten modes
here cost what five cost there.  Re-derive the numbers rather than trusting
them; they go stale every time a mode grows.
"""

import json

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import DUAL_JS, ORFMT_JS, PHASE_JS, RANGE_JS, TABLEAU_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions only, so scripts/mathcheck.js
# executes the shipped source rather than a transcription of it, and so nothing
# here can close over a DOM element.
# ---------------------------------------------------------------------------

DUALITY_KIT_JS = r"""
  /* The three things course three asks for that or_core does not already do:
     a point checked against a model row by row (the certificate chain needs it
     on BOTH programmes), the complementary-slackness system solved for a
     candidate price vector, and a zero-sum game written as a pair of dual
     linear programmes.  Plus the small printers and the two pixel helpers that
     took the place of a plotting library.

     Needs, above it: RATIONAL_JS, FORMAT_JS (Rread, esc), MATRIX_JS (Mrref),
     and or_core's ORFMT_JS, TABLEAU_JS, PHASE_JS, DUAL_JS, RANGE_JS. */

  /* ---- reading a preset, and reading what a reader typed ---------------- */

  /* A preset is JSON -- numbers as strings, so 3/2 survives the trip -- and
     this is the only place it becomes a model.  Nothing downstream ever sees
     a string where it expects a rational. */
  function specModel(spec) {
    var cons = [], i;
    for (i = 0; i < spec.cons.length; i += 1) {
      cons.push({ a: spec.cons[i].a.map(Rparse), rel: spec.cons[i].rel || 'le',
                  b: Rparse(spec.cons[i].b), name: spec.cons[i].name });
    }
    return { max: spec.max !== false, names: spec.names.slice(),
             obj: spec.obj.map(Rparse), cons: cons,
             free: (spec.free || []).slice(), nonpos: (spec.nonpos || []).slice() };
  }
  /* n numbers from a text box, or a sentence saying what went wrong.  A reader
     types "0 3/2 1" and a bad fraction becomes a status line, never a throw. */
  function readVec(text, n, what) {
    var cells = String(text).trim().split(/[\s,]+/).filter(function (t) { return t.length > 0; });
    if (cells.length !== n) {
      return { bad: what + ' needs ' + n + ' number' + (n === 1 ? '' : 's')
        + ' separated by spaces, and I read ' + cells.length };
    }
    var out = [], i;
    for (i = 0; i < cells.length; i += 1) {
      var r = Rread(cells[i]);
      if (r === null) {
        return { bad: what + ': "' + esc(cells[i]) + '" is not a whole number or a fraction' };
      }
      out.push(r);
    }
    return { v: out };
  }

  /* ---- writing a model out, in the reader's own letters ------------------ */

  function relHtml(rel) { return rel === 'ge' ? '&gt;=' : (rel === 'eq' ? '=' : '&lt;='); }

  /* "3x1 + 5x2".  A zero term is dropped and a coefficient of 1 is not
     printed, because "1x1" is how a reader stops reading the letters. */
  function rowText(a, names) {
    var out = '', j, first = true;
    for (j = 0; j < a.length; j += 1) {
      if (Rzero(a[j])) continue;
      var neg = Rsign(a[j]) < 0, v = neg ? Rneg(a[j]) : a[j];
      out += first ? (neg ? '-' : '') : (neg ? ' - ' : ' + ');
      out += (Requ(v, R1) ? '' : Rtext(v)) + (names[j] || ('x' + (j + 1)));
      first = false;
    }
    return first ? '0' : out;
  }
  /* The whole programme as lines a page can print without knowing its shape. */
  function modelLines(model) {
    var names = model.names || [], out = [], i;
    out.push({ kind: 'obj', name: 'objective',
               text: (model.max === false ? 'min ' : 'max ') + rowText(model.obj, names) });
    for (i = 0; i < model.cons.length; i += 1) {
      out.push({ kind: 'con', index: i, name: model.cons[i].name || ('row ' + (i + 1)),
                 text: rowText(model.cons[i].a, names) + ' ' + relHtml(model.cons[i].rel || 'le')
                   + ' ' + Rtext(model.cons[i].b) });
    }
    var free = model.free || [], nonpos = model.nonpos || [], signs = [];
    for (i = 0; i < model.obj.length; i += 1) {
      var nm = names[i] || ('x' + (i + 1));
      signs.push(free.indexOf(i) >= 0 ? nm + ' free'
                 : (nonpos.indexOf(i) >= 0 ? nm + ' &lt;= 0' : nm + ' &gt;= 0'));
    }
    out.push({ kind: 'sign', name: 'signs', text: signs.join(', ') });
    return out;
  }
  /* Do two models say the same thing?  This is the whole of the dual-of-the-
     dual claim, and it is checked row by row and sign by sign rather than
     asserted, because "the dual is the primal transposed" produces a model
     that looks right at a glance and bounds nothing. */
  function modelsAgree(a, b) {
    var i, j, notes = [];
    if ((a.max !== false) !== (b.max !== false)) notes.push('the direction differs');
    if (a.obj.length !== b.obj.length) notes.push('a different number of variables');
    else for (j = 0; j < a.obj.length; j += 1) {
      if (!Requ(a.obj[j], b.obj[j])) notes.push('objective coefficient ' + (j + 1) + ' differs');
    }
    if (a.cons.length !== b.cons.length) notes.push('a different number of rows');
    else for (i = 0; i < a.cons.length; i += 1) {
      var p = a.cons[i], q = b.cons[i];
      if ((p.rel || 'le') !== (q.rel || 'le')) notes.push('row ' + (i + 1) + ' has a different relation');
      if (!Requ(p.b, q.b)) notes.push('row ' + (i + 1) + ' has a different right-hand side');
      for (j = 0; j < p.a.length; j += 1) {
        if (!Requ(p.a[j], q.a[j])) notes.push('row ' + (i + 1) + ' has a different coefficient');
      }
    }
    return { same: notes.length === 0, notes: notes };
  }

  /* ---- a point, checked against a model row by row ---------------------- */

  /* Used on the PRIMAL and on dualModel's output by the same code, which is
     the point: "is this y dual feasible" is "is this x primal feasible" asked
     of the other programme, and a kit that wrote two checkers would let them
     disagree eventually. */
  function pointCheck(model, x) {
    var names = model.names || [], rows = [], signs = [], i, j, ok = true;
    for (i = 0; i < model.cons.length; i += 1) {
      var k = model.cons[i], rel = k.rel || 'le', s = R0, parts = [];
      for (j = 0; j < x.length; j += 1) {
        s = Radd(s, Rmul(k.a[j], x[j]));
        if (!Rzero(k.a[j])) parts.push('(' + Rtext(k.a[j]) + ')(' + Rtext(x[j]) + ')');
      }
      var slack = Rsub(k.b, s), holds;
      if (rel === 'le') holds = Rsign(slack) >= 0;
      else if (rel === 'ge') holds = Rsign(slack) <= 0;
      else holds = Rzero(slack);
      if (!holds) ok = false;
      rows.push({ i: i, name: k.name || ('row ' + (i + 1)), rel: rel, value: s, b: k.b,
                  slack: slack, tight: Rzero(slack), ok: holds,
                  text: (parts.length ? parts.join(' + ') : '0') + ' = ' + Rtext(s)
                    + ' ' + relHtml(rel) + ' ' + Rtext(k.b) });
    }
    var free = model.free || [], nonpos = model.nonpos || [];
    for (j = 0; j < x.length; j += 1) {
      var want = free.indexOf(j) >= 0 ? 'free' : (nonpos.indexOf(j) >= 0 ? 'le0' : 'ge0');
      var good = want === 'free' || (want === 'ge0' ? Rsign(x[j]) >= 0 : Rsign(x[j]) <= 0);
      if (!good) ok = false;
      signs.push({ j: j, name: names[j] || ('x' + (j + 1)), value: x[j], want: want, ok: good });
    }
    var obj = R0;
    for (j = 0; j < x.length; j += 1) obj = Radd(obj, Rmul(model.obj[j], x[j]));
    var bad = [];
    for (i = 0; i < rows.length; i += 1) if (!rows[i].ok) bad.push(rows[i].name);
    for (j = 0; j < signs.length; j += 1) {
      if (!signs[j].ok) bad.push(signs[j].name + ', whose sign is wrong');
    }
    return { rows: rows, signs: signs, ok: ok, obj: obj, x: x.slice(), bad: bad };
  }

  /* ---- weak duality, as three numbers and the two links between them ---- */

  /* c'x <= y'Ax <= b'y.  The first inequality is x >= 0 applied to y'A - c;
     the second is the row sign restrictions applied to b - Ax.  A feasible x
     can never pass a feasible y, so when a reader's numbers say otherwise
     exactly one of the two points is infeasible, and `forbids` names which --
     which is what somebody who has just tried to beat the bound needs to read,
     rather than "the chain holds". */
  function weakChain(model, x, y) {
    var dual = dualModel(model);
    var px = pointCheck(model, x), dy = pointCheck(dual, y);
    var m = model.cons.length, n = model.obj.length, i, j;
    var mid = R0, terms = [];
    for (i = 0; i < m; i += 1) {
      var ax = R0;
      for (j = 0; j < n; j += 1) ax = Radd(ax, Rmul(model.cons[i].a[j], x[j]));
      mid = Radd(mid, Rmul(y[i], ax));
      terms.push({ i: i, name: model.cons[i].name || ('row ' + (i + 1)), y: y[i], ax: ax,
                   b: model.cons[i].b, product: Rmul(y[i], ax),
                   headroom: Rmul(y[i], Rsub(model.cons[i].b, ax)) });
    }
    var maxP = model.max !== false;
    var link1 = maxP ? Rcmp(px.obj, mid) <= 0 : Rcmp(px.obj, mid) >= 0;
    var link2 = maxP ? Rcmp(mid, dy.obj) <= 0 : Rcmp(mid, dy.obj) >= 0;
    var gap = maxP ? Rsub(dy.obj, px.obj) : Rsub(px.obj, dy.obj);
    var forbids = null;
    if (Rsign(gap) < 0) forbids = !px.ok ? 'primal' : (!dy.ok ? 'dual' : 'none');
    return { primal: px, dual: dy, dualOf: dual, cx: px.obj, mid: mid, by: dy.obj,
             terms: terms, link1: link1, link2: link2, gap: gap,
             gapLow: maxP ? Rsub(mid, px.obj) : Rsub(px.obj, mid),
             gapHigh: maxP ? Rsub(dy.obj, mid) : Rsub(mid, dy.obj),
             beatsBound: Rsign(gap) < 0, forbids: forbids,
             bothFeasible: px.ok && dy.ok, proves: px.ok && dy.ok && Rzero(gap) };
  }

  /* ---- complementary slackness, solved rather than checked --------------- */

  /* A CLAIMED optimum determines a candidate y: a row with slack left over
     prices at zero, and a variable the claim uses positively forces its dual
     constraint tight.  That is a small linear system, solved here by the same
     Mrref the elimination lessons use, and the candidate is then tested for
     dual feasibility.  Certified, or refuted with the constraint that fails --
     and no simplex run either way.

     When the system does not pin y down, which is what a DEGENERATE optimum
     does, the unforced prices are REPORTED as unforced and set to zero for the
     test rather than silently chosen. */
  function slacknessCandidate(model, x) {
    var px = pointCheck(model, x), m = model.cons.length, n = model.obj.length, i, j;
    var eqs = [], fromRows = [], fromCols = [];
    for (i = 0; i < m; i += 1) {
      if (px.rows[i].tight) continue;
      var e = [];
      for (j = 0; j < m; j += 1) e.push(j === i ? R1 : R0);
      e.push(R0);
      eqs.push(e);
      fromRows.push({ kind: 'row', index: i, name: px.rows[i].name, slack: px.rows[i].slack,
                      text: 'y for ' + px.rows[i].name + ' = 0',
                      why: px.rows[i].name + ' has ' + Rtext(px.rows[i].slack)
                        + ' of it left over, so it cannot be worth anything' });
    }
    for (j = 0; j < n; j += 1) {
      if (Rzero(x[j])) continue;
      var nm = (model.names || [])[j] || ('x' + (j + 1)), e2 = [], parts = [];
      for (i = 0; i < m; i += 1) {
        e2.push(model.cons[i].a[j]);
        if (!Rzero(model.cons[i].a[j])) parts.push(Rterm(model.cons[i].a[j]) + 'y' + (i + 1));
      }
      e2.push(model.obj[j]);
      eqs.push(e2);
      fromCols.push({ kind: 'col', index: j, name: nm, value: x[j],
                      text: (parts.length ? parts.join(' + ') : '0') + ' = ' + Rtext(model.obj[j]),
                      why: nm + ' = ' + Rtext(x[j]) + ' is positive, so its dual constraint '
                        + 'must hold with equality' });
    }
    var y = [], unforced = [], consistent = true;
    for (i = 0; i < m; i += 1) y.push(R0);
    if (eqs.length) {
      var red = Mrref(eqs, { cols: m });
      for (i = 0; i < red.M.length; i += 1) {
        var allZero = true;
        for (j = 0; j < m; j += 1) if (!Rzero(red.M[i][j])) allZero = false;
        if (allZero && !Rzero(red.M[i][m])) consistent = false;
      }
      if (consistent) {
        for (i = 0; i < red.pivots.length; i += 1) y[red.pivots[i]] = red.M[i][m];
        for (j = 0; j < m; j += 1) if (red.pivots.indexOf(j) < 0) unforced.push(j);
      }
    } else {
      for (j = 0; j < m; j += 1) unforced.push(j);
    }
    var dual = dualModel(model);
    var dy = consistent ? pointCheck(dual, y) : null;
    var violated = [];
    if (dy) {
      for (i = 0; i < dy.rows.length; i += 1) if (!dy.rows[i].ok) violated.push(dy.rows[i]);
      for (j = 0; j < dy.signs.length; j += 1) {
        if (dy.signs[j].ok) continue;
        violated.push({ i: -1, name: dy.signs[j].name, rel: dy.signs[j].want, ok: false,
                        value: dy.signs[j].value,
                        text: dy.signs[j].name + ' = ' + Rtext(dy.signs[j].value)
                          + ', and this row may not be priced that way' });
      }
    }
    var certified = px.ok && consistent && dy !== null && dy.ok;
    return { primal: px, y: y, equations: fromRows.concat(fromCols), consistent: consistent,
             unforced: unforced, dualOf: dual, dualCheck: dy, violated: violated,
             certified: certified, dualValue: dy ? dy.obj : null,
             gap: dy ? Rsub(dy.obj, px.obj) : null,
             loose: unforced.length > 0 && consistent,
             verdict: !px.ok ? 'infeasible'
               : (!consistent ? 'no-price' : (certified ? 'certified' : 'refuted')) };
  }

  /* ---- a zero-sum game, as a pair of dual linear programmes -------------- */

  /* The row player's problem.  The variables are the mix p and then the
     guaranteed payoff v, which is FREE -- a game whose value is negative is one
     a v >= 0 column cannot express, and pinning v at >= 0 is the mistake that
     makes a lab work on rock-paper-scissors and fail on everything else.

       max v  s.t.  v - sum_i p_i A_ij <= 0  for every column j
                    sum_i p_i = 1,  p >= 0,  v free

     dualModel of exactly this is the column player's problem, one variable per
     column, and strong duality between them IS the minimax theorem. */
  function gameRowModel(P, rowNames, colNames) {
    var m = P.length, n = P[0].length, names = [], obj = [], cons = [], i, j;
    for (i = 0; i < m; i += 1) {
      names.push((rowNames && rowNames[i]) || ('p' + (i + 1)));
      obj.push(R0);
    }
    names.push('v');
    obj.push(R1);
    for (j = 0; j < n; j += 1) {
      var a = [];
      for (i = 0; i < m; i += 1) a.push(Rneg(P[i][j]));
      a.push(R1);
      cons.push({ a: a, rel: 'le', b: R0,
                  name: 'against ' + ((colNames && colNames[j]) || ('column ' + (j + 1))) });
    }
    var sum = [];
    for (i = 0; i < m; i += 1) sum.push(R1);
    sum.push(R0);
    cons.push({ a: sum, rel: 'eq', b: R1, name: 'the mix adds to 1' });
    return { max: true, names: names, obj: obj, cons: cons, free: [m] };
  }

  /* Both programmes solved, the value, both mixes, and every pure strategy
     scored against the opponent's optimum.  `rowPure[i]` is what row i earns
     against the column player's mix and is <= v; `colPure[j]` is what column j
     concedes against the row player's mix and is >= v.  Those two lists ARE the
     minimax theorem on this instance, and they are what a reader hunting for a
     single best row runs into. */
  function gameSolve(P, rowNames, colNames, opts) {
    opts = opts || { rule: 'bland', maxPivots: 400 };
    var m = P.length, n = P[0].length, i, j;
    var rowLP = gameRowModel(P, rowNames, colNames), colLP = dualModel(rowLP);
    var rs = lpSolve(rowLP, opts), cs = lpSolve(colLP, opts);
    if (rs.status !== 'optimal' || cs.status !== 'optimal') {
      return { status: rs.status === 'optimal' ? cs.status : rs.status,
               rowLP: rowLP, colLP: colLP, p: null, q: null, value: null };
    }
    var p = rs.x.slice(0, m), v = rs.x[m], q = cs.x.slice(0, n), u = cs.x[n];
    var rowPure = [], colPure = [], expected = R0;
    for (i = 0; i < m; i += 1) {
      var s = R0;
      for (j = 0; j < n; j += 1) s = Radd(s, Rmul(P[i][j], q[j]));
      rowPure.push({ i: i, name: (rowNames && rowNames[i]) || ('row ' + (i + 1)), payoff: s,
                     weight: p[i], used: !Rzero(p[i]), atValue: Requ(s, v), ok: Rcmp(s, v) <= 0 });
    }
    for (j = 0; j < n; j += 1) {
      var t = R0;
      for (i = 0; i < m; i += 1) t = Radd(t, Rmul(P[i][j], p[i]));
      colPure.push({ j: j, name: (colNames && colNames[j]) || ('column ' + (j + 1)), payoff: t,
                     weight: q[j], used: !Rzero(q[j]), atValue: Requ(t, v), ok: Rcmp(t, v) >= 0 });
    }
    for (i = 0; i < m; i += 1) {
      for (j = 0; j < n; j += 1) expected = Radd(expected, Rmul(Rmul(p[i], q[j]), P[i][j]));
    }
    var rowsAt = 0, colsAt = 0;
    for (i = 0; i < m; i += 1) if (rowPure[i].atValue) rowsAt += 1;
    for (j = 0; j < n; j += 1) if (colPure[j].atValue) colsAt += 1;
    return { status: 'optimal', rowLP: rowLP, colLP: colLP, rowSolve: rs, colSolve: cs,
             p: p, q: q, value: v, dualValue: u, expected: expected,
             rowPure: rowPure, colPure: colPure,
             minimax: Requ(v, u) && Requ(expected, v),
             pure: rowsAt === 1 && colsAt === 1 };
  }
  /* One pure strategy against a mix: the reader's own choice, scored. */
  function pureAgainst(P, i, q) {
    var s = R0, j;
    for (j = 0; j < q.length; j += 1) s = Radd(s, Rmul(P[i][j], q[j]));
    return s;
  }
  /* A column of the payoff matrix against the row player's mix. */
  function pureColAgainst(P, j, p) {
    var s = R0, i;
    for (i = 0; i < p.length; i += 1) s = Radd(s, Rmul(P[i][j], p[i]));
    return s;
  }

  /* ---- the pivot at the end of a cost range ------------------------------ */

  /* Inside its range a changed objective coefficient moves z and nothing else.
     AT the end of the range some nonbasic reduced cost has reached exactly
     zero: two corners are now equally good, and one pivot moves to the other.
     tabEnter will not find that column -- it hunts strictly negative reduced
     costs, which is right for solving and wrong for showing a tie -- so the
     tied column is found here and pivoted on deliberately.

     Assembly over tabCost, tabRatio and tabPivot; no new arithmetic, and in
     particular no second opinion about what a pivot is. */
  function costPivot(tab, j, cnew) {
    var c = tab.c.slice(), k;
    c[j] = tab.maximised ? cnew : Rneg(cnew);
    var t2 = tabCost(tabCopy(tab), c);
    var tie = [];
    for (k = 0; k < t2.n; k += 1) {
      if (t2.basis.indexOf(k) >= 0 || t2.forbid[k]) continue;
      if (Rzero(t2.z[k])) tie.push({ j: k, name: t2.names[k] });
    }
    var after = null, ratio = null, improving = -1;
    for (k = 0; k < t2.n; k += 1) {
      if (t2.basis.indexOf(k) >= 0 || t2.forbid[k]) continue;
      if (Rsign(t2.z[k]) < 0) { improving = k; break; }
    }
    if (tie.length) {
      var rt = tabRatio(t2, tie[0].j, 'dantzig');
      if (!rt.unbounded) { after = tabPivot(t2, rt.leave, tie[0].j); ratio = rt; }
    }
    var here = tabRead(t2);
    return { tab: t2, tie: tie, ratio: ratio, after: after, optimal: improving < 0,
             read: here, afterRead: after ? tabRead(after) : null,
             z: t2.z[t2.n], zOrig: t2.maximised ? t2.z[t2.n] : Rneg(t2.z[t2.n]) };
  }

  /* ---- reading a slider ------------------------------------------------- */

  /* A range input hands back a STRING, and it can hand back one that is not a
     number: an empty value attribute, or a bound a previous redraw moved out
     from under it.  BigInt(NaN) throws rather than drawing anything, and a
     blank panel with no error anywhere is the hardest kind of defect to find,
     so every slider in this kit is read through here. */
  function clampInt(value, lo, hi, fallback) {
    /* Number('') is 0, not NaN, so an EMPTY slider would silently read as the
       bottom of its range rather than as missing.  That is the quirk this
       trim() is here for. */
    var t = String(value).trim();
    var v = t === '' ? NaN : Math.round(Number(t));
    if (!isFinite(v)) v = Math.round(Number(fallback));
    if (!isFinite(v)) v = lo;
    if (v < lo) v = lo;
    if (v > hi) v = hi;
    return v;
  }

  /* ---- two pixels of a plot, without a plotting library ------------------ */

  /* Rnum goes through Number and this path produces rationals Number cannot
     hold, so a position is taken from Rfixed -- BigInt long division -- and
     only then becomes a float.  A PIXEL is allowed to round; the number it
     stands for is not, and every figure here prints the exact value beside it. */
  function pxOf(v, lo, hi, a, b) {
    var d = Rsub(hi, lo);
    if (Rzero(d)) return a;
    return a + (b - a) * parseFloat(Rfixed(Rdiv(Rsub(v, lo), d), 6));
  }
  /* The smallest interval holding every value, padded, and widened when they
     all coincide so that a one-point plot still has an axis. */
  function spanOf(values) {
    var lo = null, hi = null, i;
    for (i = 0; i < values.length; i += 1) {
      if (lo === null || Rcmp(values[i], lo) < 0) lo = values[i];
      if (hi === null || Rcmp(values[i], hi) > 0) hi = values[i];
    }
    if (lo === null) return { lo: R0, hi: R1 };
    if (Requ(lo, hi)) return { lo: Rsub(lo, R1), hi: Radd(hi, R1) };
    var pad = Rdiv(Rsub(hi, lo), R(20n, 1n));
    return { lo: Rsub(lo, pad), hi: Radd(hi, pad) };
  }
"""


_CORE_JS = (
    RATIONAL_JS + FORMAT_JS + MATRIX_JS + ORFMT_JS + TABLEAU_JS + PHASE_JS
    + DUAL_JS + RANGE_JS + DUALITY_KIT_JS
)


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the path uses, so a reader
# moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _js_string(text):
    return json.dumps(text).replace("</", "<\\/")


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" id="%sLab" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, cid, label, cid, value, cid, lo, hi, step, value)
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
    return '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)


def _table(cid, top=12):
    return ('      <div class="table-wrap" style="margin-top:%dpx;">'
            '<table class="tt" id="%s"></table></div>\n' % (top, cid))


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own. An unknown preset raises for the same reason
    an unknown mode does: a silent fallback ships a page that looks finished and
    is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("duality mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "duality mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "duality mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


def _presets_js(presets):
    return "  var PRESETS = %s;\n" % json.dumps(presets).replace("</", "<\\/")


def _preset_fn(cid, mode):
    """`preset()`, identical in every mode and wrong in a different way in each
    if it were written ten times."""
    return (
        "  function preset() {\n"
        "    for (var i = 0; i < PRESETS.length; i += 1) {\n"
        "      if (PRESETS[i].key === document.getElementById('%s').value) return PRESETS[i];\n"
        "    }\n"
        "    throw new Error('%s: no preset named ' + document.getElementById('%s').value);\n"
        "  }\n" % (cid, mode, cid)
    )


# ---------------------------------------------------------------------------
# The models. Written once, named by story rather than by letter, and shared
# between the modes that want the same worked example -- a reader who meets the
# workshop when the dual is constructed should meet the same workshop when its
# prices are read off the tableau.
#
# Every one of these is solved in the browser. Nothing below records an answer:
# the comments say what the answer IS so that a later edit that breaks one is
# visible in the diff, and scripts/mathcheck.js is where the claim is tested.
# ---------------------------------------------------------------------------

# max 3x1 + 5x2 -- z* = 36 at (2, 6), y = (0, 3/2, 1)
WORKSHOP = {
    "max": True, "names": ["x1", "x2"], "obj": ["3", "5"],
    "cons": [{"a": ["1", "0"], "rel": "le", "b": "4", "name": "cutting"},
             {"a": ["0", "2"], "rel": "le", "b": "12", "name": "glazing"},
             {"a": ["3", "2"], "rel": "le", "b": "18", "name": "assembly"}],
}

# A >= row, so the column holding B^-1 for it is an ARTIFICIAL and not the
# surplus beside it -- z* = 21 at (3, 3/2), y = (3/4, 1/2, 0)
BAKERY = {
    "max": True, "names": ["x", "y"], "obj": ["5", "4"],
    "cons": [{"a": ["6", "4"], "rel": "le", "b": "24", "name": "flour"},
             {"a": ["1", "2"], "rel": "le", "b": "6", "name": "sugar"},
             {"a": ["1", "1"], "rel": "ge", "b": "2", "name": "contract"}],
}

# An = row -- z* = 15 at (3, 0), y = (0, 0, 5)
EQROW = {
    "max": True, "names": ["x", "y"], "obj": ["5", "4"],
    "cons": [{"a": ["6", "4"], "rel": "le", "b": "24", "name": "flour"},
             {"a": ["1", "2"], "rel": "le", "b": "6", "name": "sugar"},
             {"a": ["1", "1"], "rel": "eq", "b": "3", "name": "contract"}],
}

# A minimisation -- z* = 9 at (3, 1), y = (2, 0, 1)
BLEND = {
    "max": False, "names": ["x", "y"], "obj": ["2", "3"],
    "cons": [{"a": ["1", "1"], "rel": "ge", "b": "4", "name": "protein"},
             {"a": ["1", "0"], "rel": "le", "b": "3", "name": "supply"},
             {"a": ["0", "1"], "rel": "ge", "b": "1", "name": "oats"}],
}

# DEGENERATE at (2, 2): three rows tight, and the third one priced at zero.
DEGEN = {
    "max": True, "names": ["x", "y"], "obj": ["1", "1"],
    "cons": [{"a": ["1", "0"], "rel": "le", "b": "2", "name": "kiln"},
             {"a": ["0", "1"], "rel": "le", "b": "2", "name": "wheel"},
             {"a": ["1", "1"], "rel": "le", "b": "4", "name": "firing"}],
}

# Three variables, two basic and one not -- z* = 46 at (2, 6, 0), y = (3, 2, 0).
# Every cost range and every right-hand-side range on this one is a whole
# number, which is what makes it the preset a slider can land exactly on.
THREE = {
    "max": True, "names": ["x1", "x2", "x3"], "obj": ["8", "5", "3"],
    "cons": [{"a": ["2", "1", "1"], "rel": "le", "b": "10", "name": "machine"},
             {"a": ["1", "1", "2"], "rel": "le", "b": "8", "name": "labour"},
             {"a": ["1", "0", "0"], "rel": "le", "b": "4", "name": "contract"}],
}

# A free variable and an equality, for the construction rules that are not the
# textbook case -- the dual of an = row is a price with no sign restriction.
MIXED = {
    "max": True, "names": ["u", "v"], "obj": ["4", "3"], "free": [1],
    "cons": [{"a": ["2", "1"], "rel": "le", "b": "10", "name": "capacity"},
             {"a": ["1", "-1"], "rel": "ge", "b": "1", "name": "balance"},
             {"a": ["1", "1"], "rel": "eq", "b": "4", "name": "quota"}],
}

# Two objectives on one region. Four supported efficient corners at
# (7, 0), (6, 3), (4, 6), (0, 10), breaking at lambda = 1/12, 1/3 and 1/2.
FRONT = {
    "max": True, "names": ["x1", "x2"], "obj": ["1", "1"],
    "cons": [{"a": ["1", "0"], "rel": "le", "b": "8", "name": "kiln"},
             {"a": ["1", "1"], "rel": "le", "b": "10", "name": "clay"},
             {"a": ["2", "1"], "rel": "le", "b": "16", "name": "glaze"},
             {"a": ["3", "2"], "rel": "le", "b": "24", "name": "firing"},
             {"a": ["3", "1"], "rel": "le", "b": "21", "name": "packing"}],
}

# Three corners, breaking at lambda = 1/6 and 1/2.
FRONT3 = {
    "max": True, "names": ["x1", "x2"], "obj": ["1", "1"],
    "cons": [{"a": ["1", "0"], "rel": "le", "b": "8", "name": "kiln"},
             {"a": ["0", "1"], "rel": "le", "b": "6", "name": "wheel"},
             {"a": ["1", "1"], "rel": "le", "b": "10", "name": "clay"},
             {"a": ["2", "1"], "rel": "le", "b": "16", "name": "glaze"}],
}


# ---------------------------------------------------------------------------
# construct -- the dual built pairing by pairing, and the dual of the dual
# ---------------------------------------------------------------------------

CONSTRUCT_PRESETS = [
    {"key": "workshop", "model": WORKSHOP,
     "label": "a workshop with three shared resources — every row a cap"},
    {"key": "bakery", "model": BAKERY,
     "label": "the same shape with a floor in it — one row is a >="},
    {"key": "mixed", "model": MIXED,
     "label": "a cap, a floor, a quota and a variable free to go negative"},
    {"key": "blend", "model": BLEND,
     "label": "a minimisation, where every direction turns over"},
]

_CONSTRUCT_VIEWS = [
    ("primal", "the programme as written"),
    ("dual", "its dual"),
    ("dualdual", "the dual of that dual"),
]


def _construct(cfg):
    idx = _preset_index(cfg, CONSTRUCT_PRESETS, "construct")
    pre = CONSTRUCT_PRESETS[idx]
    markup = (
        _toolbar(
            "Writing the dual",
            "one price per row, one constraint per variable, and the rule that fixed each direction",
            [("cyan", "a row, and the price it creates"),
             ("purple", "a variable, and the constraint it creates"),
             ("amber", "a sign with no restriction on it")],
        )
        + _stage(_svg("cnPlot", "0 0 660 270",
                      "Each row of the programme joined to the dual variable it creates, and "
                      "each variable joined to the dual constraint it creates."))
        + _table("cnTable")
        + _banner("cnStatus")
    )
    controls = (
        _select("cnPreset", "Worked example",
                [(p["key"], p["label"]) for p in CONSTRUCT_PRESETS], pre["key"])
        + _select("cnView", "Take the dual of", _CONSTRUCT_VIEWS, "primal")
        + _kpis([("Rows, so prices", "cnRows"),
                 ("Variables, so constraints", "cnCols"),
                 ("Prices with no sign restriction", "cnFree"),
                 ("Same programme it started from", "cnBack")])
        + _hint(
            "cnHint",
            "Put units on every price as you write it: the objective's units divided by "
            "that row's units. A price whose units you cannot say is a price paired with "
            "the wrong row, and the check costs ten seconds.",
        )
    )
    script = _CORE_JS + _presets_js(CONSTRUCT_PRESETS) + _preset_fn("cnPreset", "construct") + r"""
  var view = document.getElementById('cnView');
  var plot = document.getElementById('cnPlot'), table = document.getElementById('cnTable');
  var status = document.getElementById('cnStatus');

  function box(x, y, w, tone, head, body) {
    return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="30" rx="4" '
      + 'fill="var(--panel-2)" stroke="var(--' + tone + ')" stroke-width="1" />'
      + '<text x="' + (x + 8) + '" y="' + (y + 13) + '" font-size="10" fill="var(--' + tone + ')" '
      + 'font-weight="700">' + head + '</text>'
      + '<text x="' + (x + 8) + '" y="' + (y + 25) + '" font-size="10" fill="var(--muted)">'
      + body + '</text>';
  }

  function redraw() {
    var p = preset(), primal = specModel(p.model);
    var dual = dualModel(primal), dd = dualModel(dual);
    var shown = view.value === 'dual' ? dual : (view.value === 'dualdual' ? dd : primal);
    var made = dualModel(shown);
    var back = modelsAgree(primal, dd);
    var lines = modelLines(shown), mlines = modelLines(made);
    var m = shown.cons.length, n = shown.obj.length, i, j;

    /* Every row on the left is joined to the thing it creates on the right.
       The rows come first and the variables after, in both columns, so the
       pairing is a straight line and never a crossing. */
    var s = '<text x="6" y="14" font-size="11" fill="var(--text)" font-weight="700">'
      + lines[0].text + '</text>'
      + '<text x="404" y="14" font-size="11" fill="var(--text)" font-weight="700">'
      + mlines[0].text + '</text>';
    var top = 26, step = 38;
    for (i = 0; i < m; i += 1) {
      var yy = top + i * step;
      s += box(6, yy, 250, 'cyan', shown.cons[i].name, lines[i + 1].text);
      s += box(404, yy, 250, 'cyan', made.names[i],
               made.pairs[i].sign === 'free' ? 'no sign restriction'
               : (made.pairs[i].sign === 'le0' ? made.names[i] + ' &lt;= 0'
                  : made.names[i] + ' &gt;= 0'));
      s += '<line x1="256" y1="' + (yy + 15) + '" x2="404" y2="' + (yy + 15)
        + '" stroke="var(--cyan)" stroke-width="1.2" opacity="0.75" />'
        + '<text x="268" y="' + (yy + 11) + '" font-size="9" fill="var(--muted)">'
        + 'one price for this row</text>';
    }
    for (j = 0; j < n; j += 1) {
      var y2 = top + (m + j) * step;
      s += box(6, y2, 250, 'purple', shown.names[j],
               lines[lines.length - 1].text.split(', ')[j] || '');
      s += box(404, y2, 250, 'purple', made.cons[j].name, mlines[j + 1].text);
      s += '<line x1="256" y1="' + (y2 + 15) + '" x2="404" y2="' + (y2 + 15)
        + '" stroke="var(--purple)" stroke-width="1.2" opacity="0.75" />'
        + '<text x="268" y="' + (y2 + 11) + '" font-size="9" fill="var(--muted)">'
        + 'one constraint for this one</text>';
    }
    plot.innerHTML = s;

    var body = '';
    for (i = 0; i < made.pairs.length; i += 1) {
      var q = made.pairs[i];
      /* dualModel writes its rules with RAW "<=" and ">=" in them -- they are
         sentences, not markup -- so a browser would read "<= row in a
         maximisation ... so y >" as a tag and swallow the whole clause. esc()
         is the difference between a rule a reader can read and a gap. */
      var tone = q.kind === 'row' ? 'tone-cyan' : 'tone-purple';
      body += tr([rowhead(q.kind === 'row' ? 'a row' : 'a variable'),
                  td(q.primal, tone), td(q.dual, tone),
                  td(q.kind === 'row'
                     ? (q.sign === 'free' ? 'free' : (q.sign === 'le0' ? '&lt;= 0' : '&gt;= 0'))
                     : relHtml(q.rel), q.sign === 'free' || q.rel === 'eq' ? 'tone-amber' : ''),
                  tdl(esc(q.rule))]);
    }
    table.innerHTML = '<thead>' + tr([th('what it is'), th('in this programme'),
      th('what it makes'), th('and in which direction'), th('the rule that fixed it')])
      + '</thead><tbody>' + body + '</tbody>';

    var freeCount = 0, negCount = 0;
    for (i = 0; i < m; i += 1) {
      if (made.pairs[i].sign === 'free') freeCount += 1;
      if (made.pairs[i].sign === 'le0') negCount += 1;
    }
    document.getElementById('cnRows').textContent = m + ' rows, ' + m + ' prices';
    document.getElementById('cnCols').textContent = n + ' variables, ' + n + ' constraints';
    document.getElementById('cnFree').textContent = freeCount === 0 ? 'none' : String(freeCount);
    document.getElementById('cnBack').textContent = back.same ? 'yes, row for row' : back.notes[0];

    var awkward = freeCount || negCount
      ? ' This one has ' + (freeCount ? freeCount + ' row that binds in both directions, whose price '
          + 'therefore has no sign restriction at all' : '')
        + (freeCount && negCount ? ', and ' : '')
        + (negCount ? negCount + ' row that is a floor rather than a cap, whose price comes out on '
          + 'the other side of zero' : '')
        + ' &mdash; ' + (freeCount && negCount ? 'the two cases' : 'a case')
        + ' a transposed matrix has nowhere to put.'
      : ' Every row here is a cap and every variable is held at or above zero, which is the one '
        + 'case where a transpose alone would look as though it had worked.';
    status.innerHTML = back.same
      ? 'Taking the dual twice returns <strong>the programme it started from</strong>, row for row and '
        + 'sign for sign &mdash; which it could not do if the rules were "transpose and copy the rest '
        + 'across". The direction of every constraint and the sign of every variable are forced by '
        + 'the one requirement that the prices must combine the rows into a valid bound, and the '
        + 'column on the right is what that forcing produced.' + awkward
      : '<span class="tone-red">The dual of the dual is not the programme it started from: '
        + back.notes[0] + '.</span> That is the misconception this panel exists to show: a transpose '
        + 'with everything else copied across is a problem that bounds nothing.';
  }

  document.getElementById('cnPreset').addEventListener('change', redraw);
  view.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="One price per row, one constraint per variable",
        subtitle="the dual built pairing by pairing, and the dual of the dual returning the primal",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose a programme, and which one to take the dual of"),
        panel_intro=cfg.get(
            "panel_intro",
            "Nothing here is a table to memorise. Each direction and each sign is forced by "
            "the requirement that the prices, multiplied through the rows, must bound the "
            "objective &mdash; and the last control takes the dual twice, which returns what "
            "it started from.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# certificate -- c'x <= y'Ax <= b'y, with exact numbers at each link
# ---------------------------------------------------------------------------

CERTIFICATE_PRESETS = [
    {"key": "workshop", "model": WORKSHOP, "x": "1 1", "y": "0 2 1",
     "label": "a workshop plan, and a set of prices someone guessed"},
    {"key": "bakery", "model": BAKERY, "x": "1 1", "y": "1 0 0",
     "label": "a plan with a floor in it, and the crudest prices that work"},
    {"key": "blend", "model": BLEND, "x": "3 2", "y": "1 0 0",
     "label": "a minimisation, where the certificate bounds from below"},
]


def _certificate(cfg):
    idx = _preset_index(cfg, CERTIFICATE_PRESETS, "certificate")
    pre = CERTIFICATE_PRESETS[idx]
    markup = (
        _toolbar(
            "Weak duality as a certificate",
            "any feasible pair brackets the optimum, and neither point had to be solved for",
            [("cyan", "what the plan earns"), ("amber", "the middle quantity"),
             ("green", "what the prices allow"), ("purple", "where the two meet")],
        )
        + _stage(_svg("cePlot", "0 0 660 150",
                      "The three quantities of the weak duality chain marked on one axis, "
                      "with the optimum between them."))
        + _table("ceTable")
        + _banner("ceStatus")
    )
    controls = (
        _select("cePreset", "Worked example",
                [(p["key"], p["label"]) for p in CERTIFICATE_PRESETS], pre["key"])
        + _text("ceX", "A plan &mdash; one number per variable", pre["x"])
        + _text("ceY", "A set of prices &mdash; one per row", pre["y"])
        + _kpis([("What the plan earns", "ceCx"),
                 ("The middle quantity", "ceMid"),
                 ("What the prices allow", "ceBy"),
                 ("The gap the pair leaves", "ceGap")])
        + _hint(
            "ceHint",
            "Try to find a plan that beats the price bound. Every attempt is refused, and the "
            "panel names the row it broke to get there &mdash; that refusal is the whole of "
            "weak duality, and it is why a guessed set of prices is already a proof.",
        )
    )
    script = _CORE_JS + _presets_js(CERTIFICATE_PRESETS) + _preset_fn("cePreset", "certificate") + r"""
  var inX = document.getElementById('ceX'), inY = document.getElementById('ceY');
  var plot = document.getElementById('cePlot'), table = document.getElementById('ceTable');
  var status = document.getElementById('ceStatus');

  function applyPreset() { var p = preset(); inX.value = p.x; inY.value = p.y; }

  function mark(px, top, tone, label, value) {
    return '<line x1="' + px + '" y1="' + top + '" x2="' + px + '" y2="' + (top + 26)
      + '" stroke="var(--' + tone + ')" stroke-width="2.5" />'
      + '<text x="' + px + '" y="' + (top - 4) + '" font-size="10" text-anchor="middle" '
      + 'fill="var(--' + tone + ')" font-weight="700">' + value + '</text>'
      + '<text x="' + px + '" y="' + (top + 38) + '" font-size="9" text-anchor="middle" '
      + 'fill="var(--muted)">' + label + '</text>';
  }

  function redraw() {
    var p = preset(), model = specModel(p.model), maxP = model.max !== false;
    var rx = readVec(inX.value, model.obj.length, 'the plan');
    var ry = readVec(inY.value, model.cons.length, 'the prices');
    if (rx.bad || ry.bad) {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + (rx.bad || ry.bad) + '.</span> '
        + 'Both boxes take whole numbers or fractions, separated by spaces.';
      return;
    }
    var w = weakChain(model, rx.v, ry.v);
    /* BOTH programmes are solved, not one: the mark on the axis is where the
       two meet, and a reader is entitled to see that the second one arrives at
       the same number rather than be told it does. */
    var best = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    var bestDual = lpSolve(w.dualOf, { rule: 'bland', maxPivots: 300 });
    var meet = best.status === 'optimal' && bestDual.status === 'optimal'
      && Requ(best.zOrig, bestDual.zOrig);
    var lo = spanOf([w.cx, w.mid, w.by]);
    var px1 = pxOf(w.cx, lo.lo, lo.hi, 40, 620);
    var px2 = pxOf(w.mid, lo.lo, lo.hi, 40, 620);
    var px3 = pxOf(w.by, lo.lo, lo.hi, 40, 620);
    var s = '<line x1="20" y1="72" x2="640" y2="72" stroke="var(--line-strong)" stroke-width="1" />'
      + mark(px1, 46, 'cyan', 'what the plan earns', Rshort(w.cx, 3))
      + mark(px2, 46, 'amber', 'the prices, applied to the plan', Rshort(w.mid, 3))
      + mark(px3, 46, 'green', 'what the prices allow', Rshort(w.by, 3));
    if (best.status === 'optimal' && w.bothFeasible) {
      var pz = pxOf(best.zOrig, lo.lo, lo.hi, 40, 620);
      s += '<circle cx="' + pz + '" cy="72" r="4.5" fill="var(--purple)" />'
        + '<text x="' + pz + '" y="' + 126 + '" font-size="10" text-anchor="middle" '
        + 'fill="var(--purple)" font-weight="700">'
        + (meet ? 'both programmes solve to ' + Rshort(best.zOrig, 3)
           : 'the optimum is ' + Rshort(best.zOrig, 3))
        + ', and this pair already bracketed it</text>';
    }
    if (w.bothFeasible) {
      var a = Math.min(px1, px3), bq = Math.max(px1, px3);
      s += '<rect x="' + a + '" y="66" width="' + Math.max(1, bq - a) + '" height="12" '
        + 'fill="var(--purple)" opacity="0.18" />';
    }
    plot.innerHTML = s;

    var body = '', i, j;
    for (i = 0; i < w.terms.length; i += 1) {
      var t = w.terms[i], r = w.primal.rows[i];
      body += tr([rowhead(t.name), td(Rshort(t.y, 3)), td(Rshort(t.ax, 3)), td(Rshort(t.b, 3)),
                  td(Rshort(t.headroom, 3), Rsign(t.headroom) < 0 ? 'tone-red' : 'tone-green'),
                  tdl(r.ok ? 'the plan respects this row' : 'the plan BREAKS this row')]);
    }
    for (j = 0; j < model.obj.length; j += 1) {
      var col = w.dual.rows[j], gap = Rsub(col.value, col.b);
      body += tr([rowhead(model.names[j]), td(Rshort(rx.v[j], 3)), td(Rshort(col.value, 3)),
                  td(Rshort(col.b, 3)), td(Rshort(Rmul(rx.v[j], gap), 3),
                     Rsign(Rmul(rx.v[j], gap)) < 0 ? 'tone-red' : 'tone-green'),
                  tdl(col.ok ? 'the prices cover what this one uses'
                      : 'the prices do NOT cover what this one uses')]);
    }
    table.innerHTML = '<thead>' + tr([th('row or variable'), th('price, or amount made'),
      th('what it uses'), th('what is there, or what it earns'), th('what this term adds'),
      th('and so')]) + '</thead><tbody>' + body + '</tbody>';

    document.getElementById('ceCx').textContent = Rshort(w.cx, 3);
    document.getElementById('ceMid').textContent = Rshort(w.mid, 3);
    document.getElementById('ceBy').textContent = Rshort(w.by, 3);
    document.getElementById('ceGap').textContent = w.bothFeasible ? Rshort(w.gap, 3)
      : 'no bound yet';

    var chain = Rshort(w.cx, 3) + ' ' + (maxP ? '&lt;=' : '&gt;=') + ' ' + Rshort(w.mid, 3)
      + ' ' + (maxP ? '&lt;=' : '&gt;=') + ' ' + Rshort(w.by, 3);
    /* A MINIMISATION runs the other way: the prices bound from BELOW and the
       plan from above, so a sentence written for a maximisation is not merely
       clumsy on one, it is the wrong claim. */
    var far = maxP ? 'earn more than ' : 'cost less than ';
    var near = maxP ? 'is achievable' : 'is achievable, so the answer is no worse than that';
    if (!w.primal.ok && !w.dual.ok) {
      status.innerHTML = '<span class="tone-red">Neither point is feasible</span>, so neither number '
        + 'is evidence about anything: the plan breaks ' + w.primal.bad.join(' and ')
        + ', and the prices fail to cover ' + w.dual.bad.join(' and ') + '.';
    } else if (!w.primal.ok) {
      status.innerHTML = '<span class="tone-red">That plan is not feasible</span> &mdash; it breaks '
        + w.primal.bad.join(' and ') + ' &mdash; so the ' + Rshort(w.cx, 3) + ' it appears to reach is '
        + 'not a number about this problem. The prices are feasible, so <strong>no feasible plan can '
        + far + Rshort(w.by, 3) + '</strong>: that is the link that forbids the attempt, and it is an '
        + 'inequality about every plan at once rather than a check on this one.';
    } else if (!w.dual.ok) {
      status.innerHTML = '<span class="tone-red">Those prices are not feasible</span> &mdash; they do '
        + 'not cover ' + w.dual.bad.join(' and ') + ' &mdash; so ' + Rshort(w.by, 3)
        + ' certifies nothing. A set of prices is only a proof when every variable\'s dual constraint '
        + 'holds; that is the sign restriction the second link is made of.';
    } else if (w.proves) {
      status.innerHTML = 'Both points are feasible and the chain closes: ' + chain
        + '. <strong>The two ends are equal, so both points are proved optimal</strong> with no '
        + 'further argument at all &mdash; and neither of them had to be solved for.';
    } else {
      status.innerHTML = 'Both points are feasible, so ' + chain + ' holds and the optimum is '
        + 'somewhere in between. The pair proves <strong>no plan can ' + far + Rshort(w.by, 3)
        + '</strong> and that <strong>' + Rshort(w.cx, 3) + ' ' + near + '</strong>; the gap of '
        + Rshort(w.gap, 3) + ' is what is still unknown, and it is not a measure of how wrong '
        + 'either point is.';
    }
  }

  document.getElementById('cePreset').addEventListener('change', function () { applyPreset(); redraw(); });
  [inX, inY].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Any feasible pair is already a proof",
        subtitle="c·x ≤ y·Ax ≤ b·y, with exact numbers at each link and the refusal named",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a plan and a set of prices"),
        panel_intro=cfg.get(
            "panel_intro",
            "Neither box has to be optimal and neither has to be solved for. As long as both "
            "are feasible the chain holds, and the two ends bracket the answer &mdash; which "
            "is what makes a guessed set of prices worth having.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# read -- y = c_B' B^-1, off the columns that STARTED as the identity
# ---------------------------------------------------------------------------

READ_PRESETS = [
    {"key": "workshop", "model": WORKSHOP,
     "label": "three caps, so the identity columns are the three slacks"},
    {"key": "bakery", "model": BAKERY,
     "label": "one row is a >=, so its identity column is NOT the slack beside it"},
    {"key": "eqrow", "model": EQROW,
     "label": "one row is an =, which has no slack column at all"},
]

_READ_VIEWS = [
    ("tableau", "the final tableau, with those columns marked"),
    ("inverse", "the basis, its inverse, and the tableau rebuilt from the original data"),
    ("feasible", "every dual constraint, checked one column at a time"),
]


def _read(cfg):
    idx = _preset_index(cfg, READ_PRESETS, "read")
    pre = READ_PRESETS[idx]
    markup = (
        _toolbar(
            "Reading the prices off the tableau",
            "they are in the objective row, under the columns that started as the identity",
            [("cyan", "a column that started as the identity"),
             ("green", "the objective row the prices come from"),
             ("red", "a column that only looks like one")],
        )
        + _stage(_table("rdTab", top=0))
        + _table("rdPanel")
        + _banner("rdStatus")
    )
    controls = (
        _select("rdPreset", "Worked example",
                [(p["key"], p["label"]) for p in READ_PRESETS], pre["key"])
        + _select("rdView", "Show", _READ_VIEWS, "tableau")
        + _kpis([("The prices", "rdY"),
                 ("What they value the resources at", "rdBy"),
                 ("What the plan actually earns", "rdZ"),
                 ("Dual constraints that hold", "rdOk")])
        + _hint(
            "rdHint",
            "The prices are not in the right-hand column &mdash; that is where the plan is. "
            "They are in the objective row, under the columns that were the identity at the "
            "start, and on a row that began as a &gt;= or an = those are not the slack columns.",
        )
    )
    script = _CORE_JS + _presets_js(READ_PRESETS) + _preset_fn("rdPreset", "read") + r"""
  var view = document.getElementById('rdView');
  var tabEl = document.getElementById('rdTab'), viewEl = document.getElementById('rdPanel');
  var status = document.getElementById('rdStatus');

  function redraw() {
    var p = preset(), model = specModel(p.model);
    var sol = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    if (sol.status !== 'optimal') {
      tabEl.innerHTML = '';
      viewEl.innerHTML = '';
      status.innerHTML = 'This programme comes back ' + sol.status + ', so there is no final '
        + 'tableau to read prices out of.';
      return;
    }
    var tab = sol.tab, dv = dualVector(tab), std = tab.std, i, j;
    var isId = [], idOf = [];
    for (j = 0; j < std.n; j += 1) { isId.push(false); idOf.push(-1); }
    for (i = 0; i < std.m; i += 1) { isId[std.identity[i]] = true; idOf[std.identity[i]] = i; }

    /* The tableau. A column that STARTED as the identity is marked; a surplus
       column sitting next to one is marked as the impostor it is. */
    var heads = [th('basic')], body = '';
    for (j = 0; j < std.n; j += 1) heads.push(th(std.names[j]));
    heads.push(th('value'));
    for (i = 0; i < tab.m; i += 1) {
      var cells = [rowhead(std.names[tab.basis[i]])];
      for (j = 0; j < std.n; j += 1) cells.push(td(Rshort(tab.T[i][j], 3), isId[j] ? 'on' : ''));
      cells.push(td(Rshort(tab.T[i][tab.n], 3)));
      body += tr(cells);
    }
    var zcells = [rowhead('objective')];
    for (j = 0; j < std.n; j += 1) {
      zcells.push(td(Rshort(tab.z[j], 3),
        isId[j] ? 'on' : (std.kinds[j] === 'surplus' ? 'tone-red' : '')));
    }
    zcells.push(td(Rshort(tab.z[tab.n], 3), 'tone-green'));
    body += tr(zcells, 'focus');
    tabEl.innerHTML = '<thead>' + tr(heads) + '</thead><tbody>' + body + '</tbody>';

    var out = '';
    if (view.value === 'tableau') {
      var rows = '';
      for (i = 0; i < std.m; i += 1) {
        var c = dv.columns[i];
        rows += tr([rowhead(model.cons[i].name), td(c.name, 'on'), td(c.kind),
                    td(Rshort(dv.y[i], 3), 'tone-cyan'),
                    tdl(c.isSlack
                        ? 'this row started with a slack, and the slack IS its identity column'
                        : 'this row started with an artificial, so the identity column is '
                          + c.name + ' and not the surplus beside it')]);
      }
      out = '<thead>' + tr([th('row'), th('its identity column'), th('what that column is'),
        th('its price'), th('and why that column')]) + '</thead><tbody>' + rows + '</tbody>';
    } else if (view.value === 'inverse') {
      var inv = basisInverse(tab), rows2 = '', ok = true;
      for (i = 0; i < tab.m; i += 1) {
        for (j = 0; j < std.n; j += 1) if (!Requ(inv.BinvA[i][j], tab.T[i][j])) ok = false;
      }
      for (i = 0; i < tab.m; i += 1) {
        rows2 += tr([rowhead('row ' + (i + 1)),
                     td(inv.B[i].map(Rtext).join('  ')),
                     td(inv.Binv[i].map(function (v) { return Rshort(v, 3); }).join('  '), 'on'),
                     td(inv.BinvA[i].map(function (v) { return Rshort(v, 3); }).join('  ')),
                     td(tab.T[i].slice(0, std.n).map(function (v) { return Rshort(v, 3); }).join('  '))]);
      }
      out = '<thead>' + tr([th('&nbsp;'), th('B, out of the ORIGINAL matrix'), th('B inverse'),
        th('B inverse times A'), th('what the tableau holds')]) + '</thead><tbody>' + rows2
        + tr([rowhead('agree?'), tdl(inv.columns.map(function (c) { return c.name; }).join(', ')
             + ' are the basic columns'), tdl('found in ' + inv.ops.length + ' row operations'),
             tdl(ok ? 'entry for entry' : 'NO'), tdl(ok
             ? 'so the tableau was never anything but B inverse times the data it started with'
             : 'a mismatch here would mean the tableau had drifted from the original data')])
        + '</tbody>';
    } else {
      var rows3 = '';
      for (j = 0; j < dv.check.length; j += 1) {
        var k = dv.check[j];
        rows3 += tr([rowhead(k.name), tdl(k.text), td(Rshort(k.gap, 3),
                     Rzero(k.gap) ? 'tone-amber' : ''),
                     tdl(Rzero(k.gap) ? 'tight, so this one is worth exactly what it uses'
                         : (k.ok ? 'slack, so it is not worth making'
                            : 'VIOLATED, which would mean these are not the optimal prices'))]);
      }
      out = '<thead>' + tr([th('column'), th('the prices applied to it'), th('what is left over'),
        th('and so')]) + '</thead><tbody>' + rows3 + '</tbody>';
    }
    viewEl.innerHTML = out;

    var okCount = 0;
    for (j = 0; j < dv.check.length; j += 1) if (dv.check[j].ok) okCount += 1;
    document.getElementById('rdY').textContent = dv.y.map(function (v) { return Rshort(v, 3); }).join(', ');
    document.getElementById('rdBy').textContent = Rshort(dv.value, 3);
    document.getElementById('rdZ').textContent = Rshort(sol.zOrig, 3);
    document.getElementById('rdOk').textContent = okCount + ' of ' + dv.check.length;

    var slackCount = 0;
    for (i = 0; i < dv.columns.length; i += 1) if (dv.columns[i].isSlack) slackCount += 1;
    status.innerHTML = 'The prices are <strong>' + dv.y.map(function (v) { return Rshort(v, 3); }).join(', ')
      + '</strong>, and what they value the resources at is <strong>' + Rshort(dv.value, 3)
      + '</strong> &mdash; exactly what the plan earns. '
      + (slackCount === dv.columns.length
         ? 'Here every row began as a cap, so every identity column is a slack and the shortcut '
           + '"read the slack columns" happens to work.'
         : 'Only ' + slackCount + ' of these ' + dv.columns.length + ' rows take their price from '
           + 'a slack column. On the rest the slack column is a surplus, which is minus the '
           + 'identity and holds nothing of the sort: reading prices off it gives the wrong '
           + 'numbers, and they look like numbers.')
      + ' Every dual constraint holds, so these prices are feasible for the second programme and '
      + 'the equality above is strong duality on this instance rather than evidence for it.';
  }

  document.getElementById('rdPreset').addEventListener('change', redraw);
  view.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The prices were in the tableau all along",
        subtitle="y = c_B·B⁻¹, read off the columns that started as the identity",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose a programme, and what to read off it"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tableau above is the one the simplex method finished with. The marked columns "
            "are the ones that were the identity when it started &mdash; which is not the same "
            "list as the slack columns the moment a row is a floor or a quota.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# slackness -- a claimed optimum certified or refuted, with no simplex run
# ---------------------------------------------------------------------------

SLACKNESS_PRESETS = [
    {"key": "workshop", "model": WORKSHOP, "x": "2 6",
     "label": "a claim about the workshop that happens to be right"},
    {"key": "plausible", "model": WORKSHOP, "x": "4 3",
     "label": "a feasible claim about the same workshop that is not optimal"},
    {"key": "degenerate", "model": DEGEN, "x": "2 2",
     "label": "a corner where three rows are tight and only two of them matter"},
    {"key": "three", "model": THREE, "x": "2 6 0",
     "label": "three activities, one of them not worth doing"},
]


def _slackness(cfg):
    idx = _preset_index(cfg, SLACKNESS_PRESETS, "slackness")
    pre = SLACKNESS_PRESETS[idx]
    markup = (
        _toolbar(
            "Certifying a claim without solving",
            "slack forces a price to zero, and a positive amount forces a constraint tight",
            [("green", "a condition that holds"), ("red", "a condition that fails"),
             ("amber", "a price the conditions never pinned down")],
        )
        + _stage(_svg("slPlot", "0 0 660 200",
                      "Each row and each variable drawn as a slackness condition, with the two "
                      "factors that must not both be non-zero."))
        + _table("slTable")
        + _banner("slStatus")
    )
    controls = (
        _select("slPreset", "Worked example",
                [(p["key"], p["label"]) for p in SLACKNESS_PRESETS], pre["key"])
        + _text("slX", "The claimed plan &mdash; one number per variable", pre["x"])
        + _kpis([("The prices the conditions force", "slY"),
                 ("What the plan earns", "slZ"),
                 ("What those prices value it at", "slBy"),
                 ("Verdict", "slVerdict")])
        + _hint(
            "slHint",
            "The converse does not hold, and one of the worked examples is there to show it: "
            "a row can be tight and still be worth nothing. Tightness is what a positive "
            "price forces, not what forces one.",
        )
    )
    script = _CORE_JS + _presets_js(SLACKNESS_PRESETS) + _preset_fn("slPreset", "slackness") + r"""
  var inX = document.getElementById('slX');
  var plot = document.getElementById('slPlot'), table = document.getElementById('slTable');
  var status = document.getElementById('slStatus');

  function applyPreset() { inX.value = preset().x; }

  function cell(x, y, w, tone, head, left, right, verdict) {
    return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="44" rx="4" '
      + 'fill="var(--panel-2)" stroke="var(--' + tone + ')" stroke-width="1" />'
      + '<text x="' + (x + 8) + '" y="' + (y + 14) + '" font-size="10" font-weight="700" '
      + 'fill="var(--' + tone + ')">' + head + '</text>'
      + '<text x="' + (x + 8) + '" y="' + (y + 27) + '" font-size="10" fill="var(--text)">'
      + left + '  &times;  ' + right + '</text>'
      + '<text x="' + (x + 8) + '" y="' + (y + 39) + '" font-size="9" fill="var(--muted)">'
      + verdict + '</text>';
  }

  function redraw() {
    var p = preset(), model = specModel(p.model);
    var rx = readVec(inX.value, model.obj.length, 'the claimed plan');
    if (rx.bad) {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + rx.bad + '.</span> One whole number or '
        + 'fraction per variable, separated by spaces.';
      return;
    }
    var sc = slacknessCandidate(model, rx.v), m = model.cons.length, n = model.obj.length, i, j;
    var s = '', wide = 316;
    for (i = 0; i < m; i += 1) {
      var r = sc.primal.rows[i], price = sc.y[i];
      var forced = r.tight;
      s += cell(6, 10 + i * 50, wide, r.ok ? (forced ? 'green' : 'muted') : 'red',
                r.name, 'price ' + Rshort(price, 3), 'slack ' + Rshort(r.slack, 3),
                !r.ok ? 'the plan breaks this row'
                : (forced ? 'tight, so a price here is allowed'
                   : 'slack left over, so its price is forced to zero'));
    }
    for (j = 0; j < n; j += 1) {
      var used = sc.dualCheck ? sc.dualCheck.rows[j] : null;
      var gap = used ? Rsub(used.value, used.b) : R0;
      s += cell(338, 10 + j * 50, wide,
                !sc.dualCheck ? 'muted' : (used.ok ? (Rzero(gap) ? 'green' : 'muted') : 'red'),
                model.names[j], 'amount ' + Rshort(rx.v[j], 3), 'left over ' + Rshort(gap, 3),
                !sc.dualCheck ? 'no prices to test against'
                : (!used.ok ? 'these prices do NOT cover what it uses'
                   : (Rzero(rx.v[j]) ? 'not made, so its constraint may be slack'
                      : 'made, so its constraint had to come out tight')));
    }
    plot.innerHTML = s;

    var body = '';
    for (i = 0; i < sc.equations.length; i += 1) {
      var e = sc.equations[i];
      body += tr([rowhead(e.kind === 'row' ? 'slack in ' + e.name : e.name + ' is positive'),
                  td(e.text), tdl(e.why)]);
    }
    if (!sc.equations.length) {
      body += tr([rowhead('nothing forced'), td('&mdash;'),
                  tdl('every row has slack and nothing is made, so the conditions say nothing')]);
    }
    body += tr([rowhead('the prices that solves for'),
                td(sc.consistent ? sc.y.map(function (v) { return Rshort(v, 3); }).join(', ')
                   : 'no solution', sc.consistent ? 'tone-cyan' : 'tone-red'),
                tdl(sc.consistent
                    ? (sc.unforced.length
                       ? 'the conditions leave ' + sc.unforced.length + ' price unforced; it is '
                         + 'shown at zero, and any value that keeps the prices feasible would do'
                       : 'one solution, and the conditions pinned every price')
                    : 'the conditions contradict each other, so no prices can go with this claim')],
               'focus');
    if (sc.dualCheck) {
      for (j = 0; j < sc.dualCheck.rows.length; j += 1) {
        var k = sc.dualCheck.rows[j];
        body += tr([rowhead('does ' + k.name + ' hold?'), td(k.text, k.ok ? 'tone-green' : 'tone-red'),
                    tdl(k.ok ? 'yes' : 'NO, and this is what refutes the claim')]);
      }
      for (j = 0; j < sc.dualCheck.signs.length; j += 1) {
        var g = sc.dualCheck.signs[j];
        if (g.ok) continue;
        body += tr([rowhead('is ' + g.name + ' allowed?'),
                    td(g.name + ' = ' + Rshort(g.value, 3), 'tone-red'),
                    tdl('no: a row of this kind cannot be priced that way, and that alone '
                        + 'refutes the claim')]);
      }
    }
    table.innerHTML = '<thead>' + tr([th('what the conditions say'), th('as an equation'),
      th('and why')]) + '</thead><tbody>' + body + '</tbody>';

    document.getElementById('slY').textContent = sc.consistent
      ? sc.y.map(function (v) { return Rshort(v, 3); }).join(', ') : 'none exist';
    document.getElementById('slZ').textContent = Rshort(sc.primal.obj, 3);
    document.getElementById('slBy').textContent = sc.dualValue === null ? '—'
      : Rshort(sc.dualValue, 3);
    document.getElementById('slVerdict').textContent =
      sc.verdict === 'certified' ? 'certified' : (sc.verdict === 'infeasible' ? 'not even feasible'
      : (sc.verdict === 'no-price' ? 'refuted' : 'refuted'));

    if (sc.verdict === 'infeasible') {
      status.innerHTML = '<span class="tone-red">That plan is not feasible</span> &mdash; it breaks '
        + sc.primal.bad.join(' and ') + ' &mdash; so there is nothing to certify. The conditions '
        + 'are about a feasible claim, and feasibility is the first thing to check.';
    } else if (sc.verdict === 'no-price') {
      status.innerHTML = '<span class="tone-red">Refuted.</span> The conditions that this claim '
        + 'forces contradict one another, so no set of prices can accompany it &mdash; and a '
        + 'plan with no prices to go with it is not optimal, which is settled without running '
        + 'the algorithm once.';
    } else if (sc.certified) {
      status.innerHTML = '<strong>Certified.</strong> The conditions force the prices <strong>'
        + sc.y.map(function (v) { return Rshort(v, 3); }).join(', ') + '</strong>; they are '
        + 'feasible for the second programme, and they value the resources at <strong>'
        + Rshort(sc.dualValue, 3) + '</strong>, which is what the plan earns. Two feasible points '
        + 'with equal values prove each other optimal, and nothing here was solved for.'
        + (sc.unforced.length
           ? ' <span class="tone-amber">Notice that the conditions did not pin every price down.</span> '
             + 'More rows are tight here than the corner needs, so a row can be tight and still be '
             + 'worth nothing &mdash; which is why the converse of these conditions is false.'
           : '');
    } else {
      var first = sc.violated.length ? sc.violated[0] : null;
      status.innerHTML = '<span class="tone-red">Refuted.</span> The conditions force the prices '
        + '<strong>' + sc.y.map(function (v) { return Rshort(v, 3); }).join(', ') + '</strong>, and '
        + 'those prices are not feasible for the second programme: ' + (first ? first.text : '')
        + '. So this plan cannot be optimal, and that is settled without a single pivot &mdash; '
        + 'the claim was refused by arithmetic on the claim itself.';
    }
  }

  document.getElementById('slPreset').addEventListener('change', function () { applyPreset(); redraw(); });
  inX.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Certified, or refuted with a reason",
        subtitle="the slackness conditions solved for a price vector, and that vector tested",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Claim a plan is optimal, and watch it be tested"),
        panel_intro=cfg.get(
            "panel_intro",
            "A claimed plan determines the prices that would have to go with it. Solving that "
            "small system and testing the result is a complete answer &mdash; certified or "
            "refuted &mdash; and it never runs the algorithm.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# rhs -- z* as an exact piecewise-linear function of one right-hand side
# ---------------------------------------------------------------------------

RHS_PRESETS = [
    {"key": "workshop", "model": WORKSHOP, "row": 2,
     "label": "the workshop, on the resource every plan is short of"},
    {"key": "three", "model": THREE, "row": 0,
     "label": "three activities, where two rows are worth something and one is not"},
    {"key": "degenerate", "model": DEGEN, "row": 2,
     "label": "a corner with a row that is tight and worth exactly nothing"},
]


def _rhs(cfg):
    idx = _preset_index(cfg, RHS_PRESETS, "rhs")
    pre = RHS_PRESETS[idx]
    markup = (
        _toolbar(
            "A price is a slope, over a stated range",
            "z as an exact piecewise-linear function of one right-hand side",
            [("cyan", "this basis, and the slope it gives"),
             ("purple", "a breakpoint, where the slope changes"),
             ("amber", "where the slider is")],
        )
        + _stage(_svg("rhPlot", "0 0 660 240",
                      "The optimal value drawn against one right-hand side: straight segments "
                      "joined at breakpoints, with the basis named on each."))
        + _table("rhTable")
        + _banner("rhStatus")
    )
    controls = (
        _select("rhPreset", "Worked example",
                [(p["key"], p["label"]) for p in RHS_PRESETS], pre["key"])
        + _select("rhRow", "Which right-hand side to move", [("0", "the first row")], "0")
        + _range("rhB", "How much of it there is", 0, 36, 18)
        + _kpis([("Its price", "rhY"),
                 ("The range that price holds over", "rhRange"),
                 ("What the price predicts", "rhPredict"),
                 ("What solving again gives", "rhActual")])
        + _hint(
            "rhHint",
            "At a breakpoint the curve has a corner: the slope coming from the left and the "
            "slope going to the right are both correct and they are different. That is why "
            "this is a rate over an interval and never a derivative.",
        )
    )
    script = _CORE_JS + _presets_js(RHS_PRESETS) + _preset_fn("rhPreset", "rhs") + r"""
  var rowSel = document.getElementById('rhRow'), slider = document.getElementById('rhB');
  var plot = document.getElementById('rhPlot'), table = document.getElementById('rhTable');
  var status = document.getElementById('rhStatus');
  var rowIdx = PRESETS[0].row, lastKey = null;

  function fnum(r) { return parseFloat(Rfixed(r, 6)); }

  function syncControls(model) {
    var opts = '', i;
    for (i = 0; i < model.cons.length; i += 1) {
      opts += '<option value="' + i + '">' + model.cons[i].name + '</option>';
    }
    rowSel.innerHTML = opts;
    if (rowIdx >= model.cons.length) rowIdx = 0;
    rowSel.value = String(rowIdx);
    var b0 = fnum(model.cons[rowIdx].b);
    var hi = Math.max(4, Math.round(b0 * 2));
    slider.min = 0;
    slider.max = hi;
    slider.value = String(clampInt(slider.value, 0, hi, b0));
    return { lo: R0, hi: R(BigInt(hi), 1n) };
  }

  function redraw() {
    var p = preset(), model = specModel(p.model);
    if (lastKey !== p.key) { lastKey = p.key; rowIdx = p.row; slider.value = String(Math.round(fnum(model.cons[p.row].b))); }
    var span = syncControls(model);
    var bNow = R(BigInt(clampInt(slider.value, 0, fnum(span.hi), fnum(model.cons[rowIdx].b))), 1n);
    var base = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    if (base.status !== 'optimal') {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = 'This programme is ' + base.status + ' as written, so there is no price to range.';
      return;
    }
    var rg = rhsRange(base.tab, rowIdx);
    var curve = rhsCurve(model, rowIdx, span.lo, span.hi, { rule: 'bland', maxPivots: 300 });
    var moved = { max: model.max, names: model.names, obj: model.obj, free: model.free,
                  nonpos: model.nonpos,
                  cons: model.cons.map(function (k, q) {
                    return q === rowIdx ? { a: k.a, rel: k.rel, b: bNow, name: k.name } : k;
                  }) };
    var again = lpSolve(moved, { rule: 'bland', maxPivots: 300 });
    var predict = Radd(base.zOrig, Rmul(rg.y_i, Rsub(bNow, rg.b)));
    var inside = (rg.lo === null || Rcmp(bNow, rg.lo) >= 0) && (rg.hi === null || Rcmp(bNow, rg.hi) <= 0);

    var pts = [], i, q;
    for (i = 0; i < curve.pieces.length; i += 1) {
      pts.push(curve.pieces[i].z);
      pts.push(curve.pieces[i].zEnd);
    }
    var s = '';
    if (!curve.pieces.length) {
      s = '<text x="10" y="30" font-size="11" fill="var(--muted)">' + curve.why + '</text>';
    } else {
      var zs = spanOf(pts), L = 46, Rr = 640, T = 20, B = 190;
      var X = function (v) { return pxOf(v, span.lo, span.hi, L, Rr); };
      var Y = function (v) { return B - (B - T) * (pxOf(v, zs.lo, zs.hi, 0, 1000) / 1000); };
      s += '<line x1="' + L + '" y1="' + B + '" x2="' + Rr + '" y2="' + B
        + '" stroke="var(--line-strong)" stroke-width="1" />'
        + '<line x1="' + L + '" y1="' + T + '" x2="' + L + '" y2="' + B
        + '" stroke="var(--line-strong)" stroke-width="1" />';
      for (i = 0; i < curve.pieces.length; i += 1) {
        q = curve.pieces[i];
        s += '<line x1="' + X(q.from) + '" y1="' + Y(q.z) + '" x2="' + X(q.to) + '" y2="' + Y(q.zEnd)
          + '" stroke="var(--cyan)" stroke-width="2.5" />'
          + '<text x="' + ((X(q.from) + X(q.to)) / 2) + '" y="' + (Y(q.z) + Y(q.zEnd)) / 2 + '" '
          + 'font-size="9" text-anchor="middle" fill="var(--muted)">slope ' + Rshort(q.slope, 3)
          + '</text>'
          + '<text x="' + ((X(q.from) + X(q.to)) / 2) + '" y="' + (B + 24) + '" font-size="9" '
          + 'text-anchor="middle" fill="var(--muted)">' + q.names.join(' ') + '</text>';
      }
      for (i = 0; i < curve.breakpoints.length; i += 1) {
        var bp = curve.breakpoints[i], zi = curve.pieces[i].zEnd;
        s += '<circle cx="' + X(bp) + '" cy="' + Y(zi) + '" r="4" fill="var(--purple)" />'
          + '<text x="' + X(bp) + '" y="' + (B + 12) + '" font-size="9" text-anchor="middle" '
          + 'fill="var(--purple)">' + Rshort(bp, 3) + '</text>';
      }
      s += '<line x1="' + X(bNow) + '" y1="' + T + '" x2="' + X(bNow) + '" y2="' + B
        + '" stroke="var(--amber)" stroke-width="1.5" stroke-dasharray="4 3" />'
        + '<text x="' + X(bNow) + '" y="' + (T - 6) + '" font-size="10" text-anchor="middle" '
        + 'fill="var(--amber)" font-weight="700">' + Rtext(bNow) + '</text>'
        + '<text x="6" y="' + (T + 4) + '" font-size="9" fill="var(--muted)">'
        + Rshort(zs.hi, 2) + '</text>'
        + '<text x="6" y="' + B + '" font-size="9" fill="var(--muted)">' + Rshort(zs.lo, 2) + '</text>'
        + '<text x="' + Rr + '" y="' + (B + 36) + '" font-size="9" text-anchor="end" '
        + 'fill="var(--muted)">how much of ' + model.cons[rowIdx].name + ' there is</text>';
    }
    plot.innerHTML = s;

    var body = '';
    for (i = 0; i < curve.pieces.length; i += 1) {
      q = curve.pieces[i];
      body += tr([rowhead(Rshort(q.from, 3) + ' to ' + Rshort(q.to, 3)),
                  td(Rshort(q.slope, 3), 'tone-cyan'), td(q.names.join(', ')),
                  td(Rshort(q.z, 3) + ' to ' + Rshort(q.zEnd, 3)),
                  tdl((Rcmp(bNow, q.from) >= 0 && Rcmp(bNow, q.to) <= 0)
                      ? 'the slider is on this piece' : '')]);
    }
    table.innerHTML = '<thead>' + tr([th('over this much of it'), th('each extra unit is worth'),
      th('and the plan is built from'), th('while the total runs'), th('&nbsp;')])
      + '</thead><tbody>' + body + '</tbody>';

    document.getElementById('rhBOut').textContent = Rtext(bNow);
    document.getElementById('rhBLab').innerHTML = 'How much ' + model.cons[rowIdx].name + ' there is';
    document.getElementById('rhY').textContent = Rshort(rg.y_i, 3) + ' each';
    document.getElementById('rhRange').textContent =
      (rg.lo === null ? 'no lower limit' : Rshort(rg.lo, 3)) + ' to '
      + (rg.hi === null ? 'no upper limit' : Rshort(rg.hi, 3));
    document.getElementById('rhPredict').textContent = Rshort(predict, 3);
    document.getElementById('rhActual').textContent = again.status === 'optimal'
      ? Rshort(again.zOrig, 3) : again.status;

    var agree = again.status === 'optimal' && Requ(again.zOrig, predict);
    status.innerHTML = (Rzero(rg.y_i)
      ? 'This row is priced at <strong>zero</strong>' + (rg.rows && false ? '' : '')
        + (base.read.tightRows.indexOf(rowIdx) >= 0
           ? ' even though it is tight: more rows are binding here than the corner needs, and a '
             + 'tight row that nothing would pay for is exactly what a degenerate corner produces.'
           : ', because there is some of it left over. Nothing would be paid for more of a thing '
             + 'that is already not running out.')
      : 'One more unit of ' + model.cons[rowIdx].name + ' is worth <strong>' + Rshort(rg.y_i, 3)
        + '</strong> &mdash; but only from <strong>'
        + (rg.lo === null ? 'no lower limit' : Rshort(rg.lo, 3)) + '</strong> to <strong>'
        + (rg.hi === null ? 'no upper limit' : Rshort(rg.hi, 3))
        + '</strong>. Outside that a different plan takes over and the price changes with it, '
        + 'so quoting the number without the interval quotes a different number.')
      + ' At ' + Rtext(bNow) + ' the price predicts <strong>' + Rshort(predict, 3)
      + '</strong> and solving again gives <strong>'
      + (again.status === 'optimal' ? Rshort(again.zOrig, 3) : again.status) + '</strong>'
      + (agree ? (inside ? ', which is the same number: inside the range the prediction is exact.'
                  : ', which agrees here by accident of where the pieces meet.')
         : ', and they differ &mdash; because ' + Rtext(bNow) + ' is outside the range, where '
           + 'this price no longer describes anything.');
  }

  document.getElementById('rhPreset').addEventListener('change', redraw);
  rowSel.addEventListener('change', function () { rowIdx = +rowSel.value; redraw(); });
  slider.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A price with its range, never without",
        subtitle="z drawn as an exact piecewise-linear function, and the price as one segment's slope",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Move one right-hand side and watch the price hold, then stop holding"),
        panel_intro=cfg.get(
            "panel_intro",
            "The curve is computed exactly rather than sampled: at the end of a basis's range "
            "some quantity is exactly zero, and a ratio test names the plan that takes over. "
            "No step size is chosen anywhere, so the breakpoints are the breakpoints.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# cost -- the range of one objective coefficient, and the pivot at its end
# ---------------------------------------------------------------------------

COST_PRESETS = [
    {"key": "three", "model": THREE, "var": 0,
     "label": "three activities: two are made, one is not, and the two cases differ"},
    {"key": "workshop", "model": WORKSHOP, "var": 0,
     "label": "the workshop, where both activities are made"},
]


def _cost(cfg):
    idx = _preset_index(cfg, COST_PRESETS, "cost")
    pre = COST_PRESETS[idx]
    markup = (
        _toolbar(
            "How far one coefficient can move",
            "two different computations, and which applies depends only on whether it is made",
            [("green", "the range where the plan does not move"),
             ("purple", "the breakpoint, where two plans tie"),
             ("amber", "where the slider is")],
        )
        + _stage(_svg("coPlot", "0 0 520 190",
                      "The coefficient's axis with the interval over which the plan is "
                      "unchanged, the breakpoints at its ends, and the current value."))
        + _table("coTable")
        + _banner("coStatus")
    )
    controls = (
        _select("coPreset", "Worked example",
                [(p["key"], p["label"]) for p in COST_PRESETS], pre["key"])
        + _select("coVar", "Whose coefficient to move", [("0", "the first")], "0")
        + _range("coC", "What it earns", 0, 16, 8)
        + _kpis([("Made at the moment", "coBasic"),
                 ("The range the plan survives", "coRange"),
                 ("What the plan earns now", "coZ"),
                 ("Has the plan itself changed?", "coMoved")])
        + _hint(
            "coHint",
            "Most changes to what something earns move only the total. The plan is a corner, "
            "and a corner does not move until some reduced cost changes sign &mdash; which "
            "happens at one value, not gradually.",
        )
    )
    script = _CORE_JS + _presets_js(COST_PRESETS) + _preset_fn("coPreset", "cost") + r"""
  var varSel = document.getElementById('coVar'), slider = document.getElementById('coC');
  var plot = document.getElementById('coPlot'), table = document.getElementById('coTable');
  var status = document.getElementById('coStatus');
  var varIdx = PRESETS[0]['var'], lastKey = null;

  function fnum(r) { return parseFloat(Rfixed(r, 6)); }

  function redraw() {
    var p = preset(), model = specModel(p.model);
    if (lastKey !== p.key) { lastKey = p.key; varIdx = p['var']; slider.value = String(Math.round(fnum(model.obj[p['var']]))); }
    var opts = '', i, j;
    for (j = 0; j < model.obj.length; j += 1) {
      opts += '<option value="' + j + '">' + model.names[j] + '</option>';
    }
    varSel.innerHTML = opts;
    if (varIdx >= model.obj.length) varIdx = 0;
    varSel.value = String(varIdx);

    var base = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    var cr = costRange(base.tab, varIdx);
    var c0 = fnum(model.obj[varIdx]);
    var loPx = cr.lo === null ? Math.max(0, c0 - 8) : fnum(cr.lo);
    var hiPx = cr.hi === null ? c0 + 8 : fnum(cr.hi);
    var axLo = Math.max(0, Math.floor(Math.min(loPx, c0) - 3));
    var axHi = Math.ceil(Math.max(hiPx, c0) + 3);
    slider.min = axLo;
    slider.max = axHi;
    slider.value = String(clampInt(slider.value, axLo, axHi, c0));
    var cNow = R(BigInt(clampInt(slider.value, axLo, axHi, c0)), 1n);
    var cp = costPivot(base.tab, varIdx, cNow);
    var inside = (cr.lo === null || Rcmp(cNow, cr.lo) >= 0) && (cr.hi === null || Rcmp(cNow, cr.hi) <= 0);
    var atEnd = (cr.lo !== null && Requ(cNow, cr.lo)) || (cr.hi !== null && Requ(cNow, cr.hi));
    var obj2 = model.obj.slice();
    obj2[varIdx] = cNow;
    var again = lpSolve({ max: model.max, names: model.names, obj: obj2, cons: model.cons,
                          free: model.free, nonpos: model.nonpos },
                        { rule: 'bland', maxPivots: 300 });
    var moved = again.status === 'optimal'
      && again.x.map(Rtext).join(',') !== base.x.map(Rtext).join(',');

    var L = 40, Rr = 480, AX = 96;
    var X = function (v) { return L + (Rr - L) * ((v - axLo) / Math.max(1, axHi - axLo)); };
    var s = '<line x1="' + L + '" y1="' + AX + '" x2="' + Rr + '" y2="' + AX
      + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<rect x="' + X(Math.max(axLo, loPx)) + '" y="' + (AX - 12) + '" width="'
      + Math.max(2, X(Math.min(axHi, hiPx)) - X(Math.max(axLo, loPx))) + '" height="24" '
      + 'fill="var(--green)" opacity="0.22" />'
      + '<text x="' + ((X(Math.max(axLo, loPx)) + X(Math.min(axHi, hiPx))) / 2) + '" y="'
      + (AX + 30) + '" font-size="10" text-anchor="middle" fill="var(--green)">'
      + 'the plan does not move anywhere in here</text>';
    if (cr.lo !== null) {
      s += '<line x1="' + X(fnum(cr.lo)) + '" y1="' + (AX - 18) + '" x2="' + X(fnum(cr.lo))
        + '" y2="' + (AX + 18) + '" stroke="var(--purple)" stroke-width="2" />'
        + '<text x="' + X(fnum(cr.lo)) + '" y="' + (AX - 24) + '" font-size="10" '
        + 'text-anchor="middle" fill="var(--purple)">' + Rshort(cr.lo, 3) + '</text>';
    }
    if (cr.hi !== null) {
      s += '<line x1="' + X(fnum(cr.hi)) + '" y1="' + (AX - 18) + '" x2="' + X(fnum(cr.hi))
        + '" y2="' + (AX + 18) + '" stroke="var(--purple)" stroke-width="2" />'
        + '<text x="' + X(fnum(cr.hi)) + '" y="' + (AX - 24) + '" font-size="10" '
        + 'text-anchor="middle" fill="var(--purple)">' + Rshort(cr.hi, 3) + '</text>';
    }
    s += '<polygon points="' + X(fnum(cNow)) + ',' + (AX - 6) + ' ' + (X(fnum(cNow)) - 6)
      + ',' + (AX - 20) + ' ' + (X(fnum(cNow)) + 6) + ',' + (AX - 20) + '" fill="var(--amber)" />'
      + '<text x="' + L + '" y="20" font-size="11" fill="var(--text)" font-weight="700">'
      + 'what ' + model.names[varIdx] + ' earns, and what that does to the plan</text>'
      + '<text x="' + L + '" y="36" font-size="10" fill="var(--muted)">'
      + (cr.basic ? 'it is made at the moment, so moving this moves every other reduced cost too'
         : 'it is not made at the moment, so moving this moves only its own reduced cost') + '</text>'
      + '<text x="' + L + '" y="' + (AX + 54) + '" font-size="10" fill="var(--text)">'
      + 'now: ' + model.names.map(function (nm, k) {
          return nm + ' = ' + Rshort(again.status === 'optimal' ? again.x[k] : base.x[k], 3);
        }).join(',  ') + '</text>'
      + '<text x="' + L + '" y="' + (AX + 70) + '" font-size="10" fill="var(--muted)">'
      + 'as written: ' + model.names.map(function (nm, k) {
          return nm + ' = ' + Rshort(base.x[k], 3); }).join(',  ') + '</text>'
      + '<text x="' + L + '" y="' + (AX + 86) + '" font-size="9" fill="var(--muted)">' + axLo
      + ' to ' + axHi + ' along this axis</text>';
    plot.innerHTML = s;

    var body = '';
    for (i = 0; i < cr.terms.length; i += 1) {
      var t = cr.terms[i];
      body += tr([rowhead(t.name), td(Rshort(t.reduced, 3)), td(Rshort(t.coef, 3)),
                  td(Rshort(t.bound, 3), 'tone-purple'), tdl(t.why)]);
    }
    if (atEnd && cp.tie.length) {
      body += tr([rowhead('the tie'), td(cp.tie.map(function (t) { return t.name; }).join(', '),
                  'tone-amber'), td('0'), td(Rtext(cNow)),
                  tdl('at exactly this value that reduced cost is zero, so two corners earn the '
                      + 'same and one pivot moves between them')], 'focus');
      if (cp.afterRead) {
        body += tr([rowhead('the other corner'),
                    td(model.names.map(function (nm, k) {
                      return nm + ' = ' + Rshort(stdPoint(base.std, cp.afterRead.x)[k], 3);
                    }).join(', '), 'tone-green'), td('&mdash;'), td('&mdash;'),
                    tdl('one pivot away, earning the same total &mdash; which is what a tie means')]);
      }
    }
    table.innerHTML = '<thead>' + tr([th('the column it moves'), th('what is left over there now'),
      th('how fast this change eats it'), th('so the limit is'), th('and why')])
      + '</thead><tbody>' + body + '</tbody>';

    document.getElementById('coCOut').textContent = Rtext(cNow);
    document.getElementById('coCLab').innerHTML = 'What ' + model.names[varIdx] + ' earns';
    document.getElementById('coBasic').textContent = cr.basic ? 'yes' : 'no, none of it is made';
    document.getElementById('coRange').textContent =
      (cr.lo === null ? 'no lower limit' : Rshort(cr.lo, 3)) + ' to '
      + (cr.hi === null ? 'no upper limit' : Rshort(cr.hi, 3));
    document.getElementById('coZ').textContent = again.status === 'optimal'
      ? Rshort(again.zOrig, 3) : again.status;
    document.getElementById('coMoved').textContent = moved ? 'yes, a different corner' : 'no';

    status.innerHTML = (cr.basic
      ? 'This one is made, so moving what it earns moves <strong>every</strong> other column\'s '
        + 'reduced cost, by this change times that column\'s entry in its own row &mdash; a ratio '
        + 'test over all of them, and an interval with two ends.'
      : 'None of this one is made, so moving what it earns moves <strong>only its own</strong> '
        + 'reduced cost. Nothing happens at all until it has improved by exactly that amount, '
        + 'which is one computation rather than a ratio test.')
      + ' The range is <strong>' + (cr.lo === null ? 'no lower limit' : Rshort(cr.lo, 3)) + ' to '
      + (cr.hi === null ? 'no upper limit' : Rshort(cr.hi, 3)) + '</strong>. '
      + (inside && !atEnd
         ? 'At ' + Rtext(cNow) + ' the plan is unchanged and only the total moved, to '
           + (again.status === 'optimal' ? Rshort(again.zOrig, 3) : '') + '.'
         : (atEnd
            ? 'At ' + Rtext(cNow) + ' a reduced cost is exactly zero: <strong>two corners earn the '
              + 'same</strong>, and the table shows the single pivot between them.'
            : 'At ' + Rtext(cNow) + ' the range has been left behind and the answer has changed '
              + 'once &mdash; not gradually, and not by as much as the coefficient moved.'));
  }

  document.getElementById('coPreset').addEventListener('change', redraw);
  varSel.addEventListener('change', function () { varIdx = +varSel.value; redraw(); });
  slider.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two different computations, and which one depends on the plan",
        subtitle="the range of one objective coefficient, and the single pivot at its end",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Move what one activity earns"),
        panel_intro=cfg.get(
            "panel_intro",
            "Pick something the plan makes and something it does not, and watch the two "
            "computations differ. The answer changes exactly once, at a value the panel "
            "prints, and not before.",
        ),
        script=script,
    )

# ---------------------------------------------------------------------------
# newcol -- TWO PANELS: price a column that is not in the model, and test a
# row that is not. This is the mode `newrow` would have been, and it is one
# mode because the lesson that needs both is one lesson.
# ---------------------------------------------------------------------------

NEWCOL_PRESETS = [
    {"key": "worth-making", "model": WORKSHOP, "col": "1 1 1", "cost": "4",
     "row": "1 1", "rel": "le", "rhs": "5",
     "label": "a product that pays for what it uses, and a rule that bites"},
    {"key": "not-worth-making", "model": WORKSHOP, "col": "1 2 3", "cost": "4",
     "row": "1 1", "rel": "le", "rhs": "10",
     "label": "a profitable product that would make the plan worse, and a rule that does not"},
    {"key": "three", "model": THREE, "col": "1 1 1", "cost": "6",
     "row": "1 1 1", "rel": "le", "rhs": "7",
     "label": "three activities already, and a fourth proposed"},
]

_RELS = [("le", "at most"), ("ge", "at least")]


def _newcol(cfg):
    idx = _preset_index(cfg, NEWCOL_PRESETS, "newcol")
    pre = NEWCOL_PRESETS[idx]
    markup = (
        _toolbar(
            "Two questions the final tableau answers",
            "what a product you have never made would be worth, and whether a new rule matters",
            [("cyan", "what it earns"), ("amber", "what it uses, at these prices"),
             ("green", "worth doing"), ("red", "not worth doing, or broken")],
        )
        + _stage(_svg("ncPlot", "0 0 660 150",
                      "What a proposed activity earns drawn against what it would consume "
                      "valued at the prices already in hand."))
        + _table("ncPrice")
        + _table("ncRow")
        + _banner("ncStatus")
    )
    controls = (
        _select("ncPreset", "Worked example",
                [(p["key"], p["label"]) for p in NEWCOL_PRESETS], pre["key"])
        + _text("ncCol", "What one unit of it would use &mdash; one number per row", pre["col"])
        + _text("ncCost", "What one unit of it would earn", pre["cost"])
        + _text("ncRowA", "A proposed new rule &mdash; one number per activity", pre["row"])
        + _select("ncRel", "The rule says", _RELS, pre["rel"])
        + _text("ncRhs", "and that limit is", pre["rhs"])
        + _kpis([("What it earns beyond what it uses", "ncReduced"),
                 ("Worth making?", "ncEnters"),
                 ("What the new rule has left over", "ncSlack"),
                 ("What re-optimising would cost", "ncCost2")])
        + _hint(
            "ncHint",
            "A profitable product is not automatically worth making. It is worth making only "
            "if what it earns exceeds what its ingredients are already worth in the plan you "
            "have &mdash; and the prices for that are sitting in the tableau already.",
        )
    )
    script = _CORE_JS + _presets_js(NEWCOL_PRESETS) + _preset_fn("ncPreset", "newcol") + r"""
  var inCol = document.getElementById('ncCol'), inCost = document.getElementById('ncCost');
  var inRow = document.getElementById('ncRowA'), inRel = document.getElementById('ncRel');
  var inRhs = document.getElementById('ncRhs');
  var plot = document.getElementById('ncPlot');
  var priceT = document.getElementById('ncPrice'), rowT = document.getElementById('ncRow');
  var status = document.getElementById('ncStatus');

  function applyPreset() {
    var p = preset();
    inCol.value = p.col; inCost.value = p.cost;
    inRow.value = p.row; inRel.value = p.rel; inRhs.value = p.rhs;
  }
  function fnum(r) { return parseFloat(Rfixed(r, 6)); }

  function redraw() {
    var p = preset(), model = specModel(p.model);
    var m = model.cons.length, n = model.obj.length, i, j;
    var rc = readVec(inCol.value, m, 'what it uses');
    var rk = readVec(inCost.value, 1, 'what it earns');
    var ra = readVec(inRow.value, n, 'the new rule');
    var rb = readVec(inRhs.value, 1, 'the limit');
    if (rc.bad || rk.bad || ra.bad || rb.bad) {
      plot.innerHTML = '';
      priceT.innerHTML = '';
      rowT.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + (rc.bad || rk.bad || ra.bad || rb.bad)
        + '.</span> Whole numbers or fractions, separated by spaces.';
      return;
    }
    var base = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    var priced = priceColumn(base.tab, rc.v, rk.v[0]);
    var newRow = { a: ra.v, rel: inRel.value, b: rb.v[0], name: 'the new rule' };
    var at = R0;
    for (j = 0; j < n; j += 1) at = Radd(at, Rmul(ra.v[j], base.x[j]));
    var slack = Rsub(rb.v[0], at);
    var violated = inRel.value === 'le' ? Rsign(slack) < 0 : Rsign(slack) > 0;
    var added = violated ? addRow(base.tab, newRow, { maxPivots: 300 }) : null;

    /* What it earns against what it uses, at the prices already in hand. */
    var earn = fnum(rk.v[0]), uses = fnum(priced.used);
    var scale = 560 / Math.max(1, Math.abs(earn), Math.abs(uses));
    var s = '<text x="6" y="16" font-size="11" fill="var(--muted)">what one unit earns</text>'
      + '<rect x="6" y="24" width="' + Math.max(2, Math.abs(earn) * scale) + '" height="26" rx="3" '
      + 'fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (12 + Math.abs(earn) * scale) + '" y="42" font-size="11" fill="var(--cyan)" '
      + 'font-weight="700">' + Rshort(rk.v[0], 3) + '</text>'
      + '<text x="6" y="76" font-size="11" fill="var(--muted)">what one unit uses, valued at the '
      + 'prices already in the plan</text>'
      + '<rect x="6" y="84" width="' + Math.max(2, Math.abs(uses) * scale) + '" height="26" rx="3" '
      + 'fill="var(--amber)" opacity="0.85" />'
      + '<text x="' + (12 + Math.abs(uses) * scale) + '" y="102" font-size="11" fill="var(--amber)" '
      + 'font-weight="700">' + Rshort(priced.used, 3) + '</text>';
    var gapPx = (Math.abs(earn) - Math.abs(uses)) * scale;
    s += '<text x="6" y="134" font-size="10" fill="var(--' + (priced.enters ? 'green' : 'red')
      + ')" font-weight="700">'
      + (priced.enters
         ? 'it earns ' + Rshort(priced.reduced, 3) + ' more than it consumes, so it belongs in the plan'
         : 'it consumes ' + Rshort(Rneg(priced.reduced), 3)
           + ' more than it earns, so making it would make the plan worse') + '</text>';
    if (gapPx > 2 && priced.enters) {
      s += '<rect x="' + (6 + Math.abs(uses) * scale) + '" y="24" width="' + gapPx + '" height="26" '
        + 'rx="3" fill="var(--green)" opacity="0.5" />';
    }
    plot.innerHTML = s;

    var body = '', parts = '';
    for (i = 0; i < m; i += 1) {
      body += tr([rowhead(model.cons[i].name), td(Rshort(priced.y[i], 3)), td(Rshort(rc.v[i], 3)),
                  td(Rshort(Rmul(priced.y[i], rc.v[i]), 3)),
                  tdl('what one unit of it takes out of ' + model.cons[i].name
                      + ', at the price that row already carries')]);
    }
    body += tr([rowhead('altogether'), td('&mdash;'), td('&mdash;'), td(Rshort(priced.used, 3), 'tone-amber'),
                tdl('the value of the ingredients one unit would consume')], 'focus');
    body += tr([rowhead('what it earns'), td('&mdash;'), td('&mdash;'), td(Rshort(rk.v[0], 3), 'tone-cyan'),
                tdl('as proposed')]);
    body += tr([rowhead('the difference'), td('&mdash;'), td('&mdash;'),
                td(Rshort(priced.reduced, 3), priced.enters ? 'tone-green' : 'tone-red'),
                tdl(priced.enters
                    ? 'positive, so it enters; the single pivot below is the whole re-optimisation'
                    : 'not positive, so the plan you have is still optimal with this column in it')]);
    if (priced.enters && priced.after) {
      var z2 = priced.after.maximised ? priced.after.z[priced.after.n]
        : Rneg(priced.after.z[priced.after.n]);
      body += tr([rowhead('the one pivot'), td('&mdash;'), td('&mdash;'),
                  td(priced.after.names[priced.after.left] + ' leaves', 'tone-amber'),
                  tdl(priced.ratio
                      ? 'the ratio test picks row ' + (priced.ratio.leave + 1) + ': '
                        + priced.ratio.rows[priced.ratio.leave].why
                      : 'nothing limits how much of it to make, so the plan is unbounded with it in')]);
      body += tr([rowhead('and then'), td('&mdash;'), td('&mdash;'), td(Rshort(z2, 3), 'tone-green'),
                  tdl('up from ' + Rshort(base.zOrig, 3) + ', and the new activity is now made')]);
    }
    priceT.innerHTML = '<thead>' + tr([th('row'), th('its price'), th('what one unit uses'),
      th('so it consumes'), th('&nbsp;')]) + '</thead><tbody>' + body + '</tbody>';

    var rbody = '';
    for (j = 0; j < n; j += 1) {
      rbody += tr([rowhead(model.names[j]), td(Rshort(ra.v[j], 3)), td(Rshort(base.x[j], 3)),
                   td(Rshort(Rmul(ra.v[j], base.x[j]), 3)),
                   tdl('what the plan you already have puts into the new rule')]);
    }
    rbody += tr([rowhead('the rule reads'), td('&mdash;'), td('&mdash;'),
                 td(Rshort(at, 3) + ' ' + relHtml(inRel.value) + ' ' + Rshort(rb.v[0], 3),
                    violated ? 'tone-red' : 'tone-green'),
                 tdl(violated ? 'the plan you have BREAKS it' : 'the plan you have already obeys it')],
                'focus');
    rbody += tr([rowhead('left over'), td('&mdash;'), td('&mdash;'),
                 td(Rshort(slack, 3), violated ? 'tone-red' : ''),
                 tdl(violated ? 'a shortfall, so the plan has to change'
                     : 'so adding this rule changes nothing at all &mdash; no re-solve, no pivot')]);
    if (added) {
      rbody += tr([rowhead('restoring it'), td('&mdash;'), td('&mdash;'),
                   td(added.run.steps.length + (added.run.steps.length === 1 ? ' pivot' : ' pivots'),
                      'tone-amber'),
                   tdl('starting from the tableau already in hand rather than from nothing')]);
      rbody += tr([rowhead('and then'), td('&mdash;'), td('&mdash;'),
                   td(added.status === 'optimal' ? Rshort(added.run.zOrig, 3) : added.status),
                   tdl(added.status === 'optimal'
                       ? 'down from ' + Rshort(base.zOrig, 3)
                         + ' &mdash; a rule can only ever cost, never pay'
                       : 'the rule cannot be satisfied at all')]);
    }
    rowT.innerHTML = '<thead>' + tr([th('activity'), th('its coefficient in the new rule'),
      th('how much of it the plan makes'), th('so it contributes'), th('&nbsp;')])
      + '</thead><tbody>' + rbody + '</tbody>';

    document.getElementById('ncReduced').textContent = Rshort(priced.reduced, 3);
    document.getElementById('ncEnters').textContent = priced.enters ? 'yes' : 'no';
    document.getElementById('ncSlack').textContent = Rshort(slack, 3);
    document.getElementById('ncCost2').textContent = !violated ? 'nothing to do'
      : (added.status === 'optimal'
         ? added.run.steps.length + ' pivot' + (added.run.steps.length === 1 ? '' : 's')
         : added.status);

    status.innerHTML = (priced.enters
      ? 'The proposed activity earns <strong>' + Rshort(rk.v[0], 3) + '</strong> and consumes '
        + '<strong>' + Rshort(priced.used, 3) + '</strong> worth of what the plan is already short '
        + 'of, so it is worth <strong>' + Rshort(priced.reduced, 3)
        + '</strong> a unit and one pivot brings it in.'
      : 'The proposed activity earns <strong>' + Rshort(rk.v[0], 3) + '</strong>, which sounds like '
        + 'a reason to make it, and consumes <strong>' + Rshort(priced.used, 3) + '</strong> worth '
        + 'of resources the plan is already using. <span class="tone-red">Making it would cost '
        + Rshort(Rneg(priced.reduced), 3) + ' a unit.</span> Profit is not the test; profit '
        + 'beyond what the ingredients are already worth is.')
      + ' The proposed rule reads ' + Rshort(at, 3) + ' ' + relHtml(inRel.value) + ' '
      + Rshort(rb.v[0], 3) + ' at the plan in hand, so '
      + (violated
         ? 'it does bite, and restoring feasibility from the tableau already computed takes '
           + added.run.steps.length + ' pivot'
           + (added.run.steps.length === 1 ? '' : 's') + ' rather than a fresh start.'
         : 'it changes nothing: a rule the current plan already obeys is a rule you can add and '
           + 'walk away from, and neither question needed the algorithm run again.');
  }

  document.getElementById('ncPreset').addEventListener('change', function () { applyPreset(); redraw(); });
  [inCol, inCost, inRow, inRhs].forEach(function (el) { el.addEventListener('input', redraw); });
  inRel.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Price a column, test a row, re-solve neither",
        subtitle="what a product you have never made is worth, and whether a new rule matters",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Propose an activity, and propose a rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both questions are answered from the tableau already in hand. Only a favourable "
            "price or a broken rule costs anything further, and the panel says which of the "
            "two you are looking at.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# dualsimplex -- optimality kept, feasibility hunted, one ratio test at a time
# ---------------------------------------------------------------------------

DUALSIMPLEX_PRESETS = [
    {"key": "workshop", "model": WORKSHOP, "row": "1 1", "rel": "le", "rhs": "5",
     "label": "a rule that cuts the workshop's plan off, and two pivots back"},
    {"key": "three", "model": THREE, "row": "1 1 1", "rel": "le", "rhs": "6",
     "label": "three activities capped in total"},
    {"key": "harmless", "model": WORKSHOP, "row": "1 1", "rel": "le", "rhs": "9",
     "label": "a rule the plan already obeys, so there is nothing to restore"},
]


def _dualsimplex(cfg):
    idx = _preset_index(cfg, DUALSIMPLEX_PRESETS, "dualsimplex")
    pre = DUALSIMPLEX_PRESETS[idx]
    markup = (
        _toolbar(
            "Restoring feasibility without losing optimality",
            "the leaving row is a negative right-hand side; the entering column comes from a ratio test along it",
            [("red", "the row that is negative"), ("cyan", "the column the ratio test picks"),
             ("amber", "where the objective has got to")],
        )
        + _stage(_table("dsTab", top=0))
        + _table("dsRatio")
        + _banner("dsStatus")
    )
    controls = (
        _select("dsPreset", "Worked example",
                [(p["key"], p["label"]) for p in DUALSIMPLEX_PRESETS], pre["key"])
        + _text("dsRowA", "The cutting rule &mdash; one number per activity", pre["row"])
        + _select("dsRel", "The rule says", _RELS, pre["rel"])
        + _text("dsRhs", "and that limit is", pre["rhs"])
        + _range("dsStep", "Pivots performed", 0, 4, 0)
        + _kpis([("Rows still negative", "dsNeg"),
                 ("Leaving next", "dsLeave"),
                 ("Entering next", "dsEnter"),
                 ("The objective here", "dsZ")])
        + _hint(
            "dsHint",
            "Try to say which plan it will land on before moving the slider. You will usually "
            "be wrong, and being wrong on purpose is how the ratio test along the objective "
            "row stops being a rule and starts being a reason.",
        )
    )
    script = _CORE_JS + _presets_js(DUALSIMPLEX_PRESETS) + _preset_fn("dsPreset", "dualsimplex") + r"""
  var inRow = document.getElementById('dsRowA'), inRel = document.getElementById('dsRel');
  var inRhs = document.getElementById('dsRhs'), step = document.getElementById('dsStep');
  var tabEl = document.getElementById('dsTab'), ratioEl = document.getElementById('dsRatio');
  var status = document.getElementById('dsStatus');

  function applyPreset() {
    var p = preset();
    inRow.value = p.row; inRel.value = p.rel; inRhs.value = p.rhs; step.value = '0';
  }

  function redraw() {
    var p = preset(), model = specModel(p.model), n = model.obj.length, i, j;
    var ra = readVec(inRow.value, n, 'the cutting rule');
    var rb = readVec(inRhs.value, 1, 'the limit');
    if (ra.bad || rb.bad) {
      tabEl.innerHTML = '';
      ratioEl.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + (ra.bad || rb.bad) + '.</span> '
        + 'Whole numbers or fractions, separated by spaces.';
      return;
    }
    var base = lpSolve(model, { rule: 'bland', maxPivots: 300 });
    var added = addRow(base.tab, { a: ra.v, rel: inRel.value, b: rb.v[0], name: 'the new rule' },
                       { maxPivots: 300 });
    var run = added.run, total = run.steps.length;
    step.min = 0;
    step.max = Math.max(1, total);
    var k = clampInt(step.value, 0, total, 0);
    var cur = run.path[k], std = cur.std;
    var dp = dualPivot(cur);

    var heads = [th('basic')], body = '';
    for (j = 0; j < cur.n; j += 1) heads.push(th(cur.names[j]));
    heads.push(th('value'));
    for (i = 0; i < cur.m; i += 1) {
      var neg = Rsign(cur.T[i][cur.n]) < 0;
      var cells = [rowhead(cur.names[cur.basis[i]])];
      for (j = 0; j < cur.n; j += 1) {
        cells.push(td(Rshort(cur.T[i][j], 3), (dp.leave === i && dp.enter === j) ? 'on' : ''));
      }
      cells.push(td(Rshort(cur.T[i][cur.n], 3), neg ? 'tone-red' : ''));
      body += tr(cells, dp.leave === i ? 'focus' : '');
    }
    var zc = [rowhead('objective')];
    for (j = 0; j < cur.n; j += 1) {
      zc.push(td(Rshort(cur.z[j], 3), dp.enter === j ? 'tone-cyan' : ''));
    }
    zc.push(td(Rshort(cur.maximised ? cur.z[cur.n] : Rneg(cur.z[cur.n]), 3), 'tone-amber'));
    body += tr(zc);
    tabEl.innerHTML = '<thead>' + tr(heads) + '</thead><tbody>' + body + '</tbody>';

    var rbody = '';
    if (dp.leave < 0) {
      rbody = tr([rowhead('nothing to do'), td('&mdash;'), td('&mdash;'), td('&mdash;'),
                  tdl('every quantity in the right-hand column is non-negative again, so this '
                      + 'basis is feasible and the objective row was never touched')]);
    } else {
      for (j = 0; j < dp.ratios.length; j += 1) {
        var t = dp.ratios[j];
        rbody += tr([rowhead(t.name), td(Rshort(t.a, 3)),
                     td(Rshort(cur.z[t.j], 3)),
                     td(t.ratio === null ? '&mdash;' : Rshort(t.ratio, 3),
                        t.j === dp.enter ? 'tone-cyan' : ''),
                     tdl(t.why)]);
      }
      rbody += tr([rowhead('so'), td('&mdash;'), td('&mdash;'),
                   td(dp.enter < 0 ? 'none' : cur.names[dp.enter], 'tone-cyan'),
                   tdl(dp.enter < 0
                       ? 'no entry in that row is negative, so the row asserts that a '
                         + 'non-negative combination is negative and the problem has no answer'
                       : 'the smallest of those ratios is the cheapest way to lift the negative '
                         + 'quantity out, which is why it is the one that enters')], 'focus');
    }
    ratioEl.innerHTML = '<thead>' + tr([th('column'), th('its entry in the leaving row'),
      th('what is left over there'), th('the ratio'), th('and why')]) + '</thead><tbody>'
      + rbody + '</tbody>';

    var negCount = 0;
    for (i = 0; i < cur.m; i += 1) if (Rsign(cur.T[i][cur.n]) < 0) negCount += 1;
    document.getElementById('dsStepOut').textContent = k + ' of ' + total;
    document.getElementById('dsNeg').textContent = negCount === 0 ? 'none' : String(negCount);
    document.getElementById('dsLeave').textContent = dp.leave < 0 ? 'nothing'
      : cur.names[cur.basis[dp.leave]];
    document.getElementById('dsEnter').textContent = dp.enter < 0 ? 'nothing' : cur.names[dp.enter];
    document.getElementById('dsZ').textContent =
      Rshort(cur.maximised ? cur.z[cur.n] : Rneg(cur.z[cur.n]), 3);

    var z0 = run.path[0].maximised ? run.path[0].z[run.path[0].n] : Rneg(run.path[0].z[run.path[0].n]);
    status.innerHTML = (total === 0
      ? 'The rule as typed does not cut the plan off, so the tableau is already both optimal and '
        + 'feasible and there is nothing to restore. That is the first thing to check, and it is '
        + 'free.'
      : 'The rule cuts the plan off, so the tableau arrives <strong>optimal in its objective row '
        + 'and infeasible in its right-hand column</strong> &mdash; and that is the shape this '
        + 'method exists for. It is ' + total + ' pivot' + (total === 1 ? '' : 's')
        + ' back to an answer, and the objective moves from ' + Rshort(z0, 3) + ' to '
        + (run.status === 'optimal'
           ? Rshort(run.zOrig, 3) + ', downwards the whole way &mdash; the opposite direction from '
             + 'the ordinary method, because this one starts outside the feasible region and '
             + 'walks in'
           : 'nowhere: ' + run.status)
        + '. The old tableau described the old basis, and a basis of the old problem is still a '
        + 'basis of the new one &mdash; just not a feasible one, and restoring it is cheaper than '
        + 'rebuilding.');
  }

  document.getElementById('dsPreset').addEventListener('change', function () { applyPreset(); redraw(); });
  [inRow, inRhs].forEach(function (el) { el.addEventListener('input', redraw); });
  inRel.addEventListener('change', redraw);
  step.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Optimal in one column, infeasible in the other",
        subtitle="the dual ratio test tabulated at every pivot, and the objective moving the other way",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Add a rule that cuts the plan off, then walk back"),
        panel_intro=cfg.get(
            "panel_intro",
            "The slider performs the pivots one at a time. At each one the leaving row is the "
            "most negative quantity and the entering column is whichever costs least to bring "
            "in, measured along that row against the objective row.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# parametric -- the efficient frontier of two objectives, exactly
# ---------------------------------------------------------------------------

PARAMETRIC_PRESETS = [
    {"key": "four-corners", "model": FRONT, "f1": "4 1", "f2": "1 4",
     "label": "two objectives that disagree, and four corners between them"},
    {"key": "three-corners", "model": FRONT3, "f1": "3 1", "f2": "1 3",
     "label": "a smaller region, and three"},
]


def _parametric(cfg):
    idx = _preset_index(cfg, PARAMETRIC_PRESETS, "parametric")
    pre = PARAMETRIC_PRESETS[idx]
    markup = (
        _toolbar(
            "Weighing two objectives against each other",
            "the corners a weighted sum can reach, and the finitely many weights where the answer changes",
            [("cyan", "a corner no other corner beats on both"),
             ("purple", "a weight where the answer changes"),
             ("amber", "the weight the slider is on")],
        )
        + _stage(_svg("paPlot", "0 0 660 250",
                      "Each reachable corner plotted by what it scores on the two objectives, "
                      "with the weight scale beneath it."))
        + _table("paTable")
        + _banner("paStatus")
    )
    controls = (
        _select("paPreset", "Worked example",
                [(p["key"], p["label"]) for p in PARAMETRIC_PRESETS], pre["key"])
        + _text("paF1", "The first objective &mdash; one number per activity", pre["f1"])
        + _text("paF2", "The second objective", pre["f2"])
        + _range("paLam", "Weight on the second objective, in hundredths", 0, 100, 50)
        + _kpis([("The weight, exactly", "paLamOutX"),
                 ("The corner it chooses", "paCorner"),
                 ("What that scores", "paScores"),
                 ("Weights where the answer changes", "paBreaks")])
        + _hint(
            "paHint",
            "The slider moves in hundredths and the breakpoints do not: they are exact "
            "fractions, computed rather than found by sampling. Between two of them nothing "
            "changes at all, however finely the slider is moved.",
        )
    )
    script = _CORE_JS + _presets_js(PARAMETRIC_PRESETS) + _preset_fn("paPreset", "parametric") + r"""
  var inF1 = document.getElementById('paF1'), inF2 = document.getElementById('paF2');
  var lam = document.getElementById('paLam');
  var plot = document.getElementById('paPlot'), table = document.getElementById('paTable');
  var status = document.getElementById('paStatus');

  function applyPreset() { var p = preset(); inF1.value = p.f1; inF2.value = p.f2; }

  function redraw() {
    var p = preset(), model = specModel(p.model), n = model.obj.length, i;
    var r1 = readVec(inF1.value, n, 'the first objective');
    var r2 = readVec(inF2.value, n, 'the second objective');
    if (r1.bad || r2.bad) {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + (r1.bad || r2.bad) + '.</span> '
        + 'One whole number or fraction per activity.';
      return;
    }
    var front = paramFront(model, r1.v, r2.v, { maxPieces: 24 });
    lam.min = 0;
    lam.max = 100;
    var L = R(BigInt(clampInt(lam.value, 0, 100, 50)), 100n);
    var here = -1;
    for (i = 0; i < front.corners.length; i += 1) {
      if (Rcmp(L, front.corners[i].from) >= 0 && Rcmp(L, front.corners[i].to) <= 0) { here = i; break; }
    }
    if (here < 0 && front.corners.length) here = front.corners.length - 1;

    var s = '';
    if (!front.corners.length) {
      s = '<text x="10" y="30" font-size="11" fill="var(--muted)">this region is '
        + front.status + ', so there is no frontier to trace</text>';
    } else {
      var xs = front.corners.map(function (c) { return c.f1; });
      var ys = front.corners.map(function (c) { return c.f2; });
      var sx = spanOf(xs), sy = spanOf(ys);
      var Lx = 52, Rx = 630, Ty = 24, By = 178;
      s += '<line x1="' + Lx + '" y1="' + By + '" x2="' + Rx + '" y2="' + By
        + '" stroke="var(--line-strong)" stroke-width="1" />'
        + '<line x1="' + Lx + '" y1="' + Ty + '" x2="' + Lx + '" y2="' + By
        + '" stroke="var(--line-strong)" stroke-width="1" />'
        + '<text x="' + Rx + '" y="' + (By + 16) + '" font-size="10" text-anchor="end" '
        + 'fill="var(--muted)">what the first objective scores</text>'
        + '<text x="6" y="' + (Ty - 8) + '" font-size="10" fill="var(--muted)">'
        + 'the second</text>';
      var pts = [];
      for (i = 0; i < front.corners.length; i += 1) {
        var c = front.corners[i];
        pts.push([pxOf(c.f1, sx.lo, sx.hi, Lx + 12, Rx - 12),
                  By - (By - Ty - 12) * (pxOf(c.f2, sy.lo, sy.hi, 0, 1000) / 1000)]);
      }
      s += '<polyline points="' + pts.map(function (q) { return q[0] + ',' + q[1]; }).join(' ')
        + '" fill="none" stroke="var(--cyan)" stroke-width="1.5" opacity="0.55" />';
      for (i = 0; i < front.corners.length; i += 1) {
        var eff = front.efficient.indexOf(i) >= 0;
        s += '<circle cx="' + pts[i][0] + '" cy="' + pts[i][1] + '" r="' + (i === here ? 7 : 5)
          + '" fill="var(--' + (i === here ? 'amber' : (eff ? 'cyan' : 'muted')) + ')" />'
          + '<text x="' + pts[i][0] + '" y="' + (pts[i][1] - 11) + '" font-size="9" '
          + 'text-anchor="middle" fill="var(--' + (i === here ? 'amber' : 'muted') + ')">('
          + Rshort(front.corners[i].f1, 2) + ', ' + Rshort(front.corners[i].f2, 2) + ')</text>';
      }
      /* The weight scale, with every breakpoint on it. */
      var by = 218;
      s += '<line x1="' + Lx + '" y1="' + by + '" x2="' + Rx + '" y2="' + by
        + '" stroke="var(--line-strong)" stroke-width="1" />'
        + '<text x="' + (Lx - 6) + '" y="' + (by + 4) + '" font-size="9" text-anchor="end" '
        + 'fill="var(--muted)">0</text>'
        + '<text x="' + (Rx + 6) + '" y="' + (by + 4) + '" font-size="9" fill="var(--muted)">1</text>'
        + '<text x="' + Lx + '" y="' + (by + 20) + '" font-size="9" fill="var(--muted)">'
        + 'all the weight on the first objective</text>'
        + '<text x="' + Rx + '" y="' + (by + 20) + '" font-size="9" text-anchor="end" '
        + 'fill="var(--muted)">all of it on the second</text>';
      for (i = 0; i < front.breakpoints.length; i += 1) {
        var bx = pxOf(front.breakpoints[i], R0, R1, Lx, Rx);
        s += '<line x1="' + bx + '" y1="' + (by - 8) + '" x2="' + bx + '" y2="' + (by + 8)
          + '" stroke="var(--purple)" stroke-width="2" />'
          + '<text x="' + bx + '" y="' + (by - 12) + '" font-size="9" text-anchor="middle" '
          + 'fill="var(--purple)">' + Rtext(front.breakpoints[i]) + '</text>';
      }
      var lx = pxOf(L, R0, R1, Lx, Rx);
      s += '<polygon points="' + lx + ',' + (by - 2) + ' ' + (lx - 6) + ',' + (by - 14) + ' '
        + (lx + 6) + ',' + (by - 14) + '" fill="var(--amber)" />';
    }
    plot.innerHTML = s;

    var body = '';
    for (i = 0; i < front.corners.length; i += 1) {
      var q = front.corners[i], eff = front.efficient.indexOf(i) >= 0;
      body += tr([rowhead(model.names.map(function (nm, k) {
                    return nm + ' = ' + Rshort(q.x[k], 3); }).join(', ')),
                  td(Rshort(q.f1, 3)), td(Rshort(q.f2, 3)),
                  td(Rtext(q.from) + ' to ' + Rtext(q.to), 'tone-purple'),
                  tdl(eff ? (i === here ? 'what this weight chooses'
                             : 'no other corner beats it on both')
                      : 'another corner beats it on both, so no weight would choose it')],
                 i === here ? 'focus' : '');
    }
    table.innerHTML = '<thead>' + tr([th('the plan'), th('the first objective'),
      th('the second'), th('chosen for weights'), th('&nbsp;')]) + '</thead><tbody>'
      + body + '</tbody>';

    document.getElementById('paLamOut').textContent = Rtext(L);
    document.getElementById('paLamOutX').textContent = Rtext(L);
    document.getElementById('paCorner').textContent = here < 0 ? 'none'
      : model.names.map(function (nm, k) {
          return nm + ' = ' + Rshort(front.corners[here].x[k], 3); }).join(', ');
    document.getElementById('paScores').textContent = here < 0 ? '—'
      : Rshort(front.corners[here].f1, 3) + ' and ' + Rshort(front.corners[here].f2, 3);
    document.getElementById('paBreaks').textContent = front.breakpoints.length
      ? front.breakpoints.map(Rtext).join(', ') : 'none';

    status.innerHTML = front.corners.length
      ? 'Sweeping the weight from one end to the other visits <strong>'
        + front.corners.length + '</strong> corner' + (front.corners.length === 1 ? '' : 's')
        + ', and the answer changes at exactly '
        + (front.breakpoints.length
           ? front.breakpoints.length + ' weight' + (front.breakpoints.length === 1 ? '' : 's')
             + ': ' + front.breakpoints.map(Rtext).join(', ')
           : 'no weight at all')
        + '. Those are the corners no feasible plan beats on both objectives at once, and that '
        + 'set is what the mathematics delivers &mdash; <strong>the weight itself is a decision, '
        + 'made outside the model</strong>, and there is no single answer to hand over without '
        + 'one. Between two breakpoints the slider changes nothing, however finely it is moved.'
      : 'This region is ' + front.status + ' under the first objective, so there is no frontier.';
  }

  document.getElementById('paPreset').addEventListener('change', function () { applyPreset(); redraw(); });
  [inF1, inF2].forEach(function (el) { el.addEventListener('input', redraw); });
  lam.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A front, not an answer",
        subtitle="every corner a weighted sum can reach, and the exact weights where it changes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Weigh two objectives against each other"),
        panel_intro=cfg.get(
            "panel_intro",
            "The corners and the weights at which they change are computed exactly, from the "
            "same ranging that decided how far one coefficient could move. Chaining that is "
            "all a parametric sweep is.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# game -- a zero-sum game as a pair of dual programmes
# ---------------------------------------------------------------------------

GAME_PRESETS = [
    {"key": "cycle", "matrix": "0 -1 1; 1 0 -1; -1 1 0",
     "label": "a game that goes round in a circle, and is worth nothing to either side"},
    {"key": "mixed", "matrix": "3 -1; -2 1",
     "label": "two choices each, no best single one, and a value that is not a whole number"},
    {"key": "saddle", "matrix": "4 2; 3 1",
     "label": "a game where one row really is best, and mixing buys nothing"},
    {"key": "four", "matrix": "2 -1 0 1; -1 3 1 -2; 0 1 -1 2; 1 -2 2 0",
     "label": "four choices each"},
]


def _game(cfg):
    idx = _preset_index(cfg, GAME_PRESETS, "game")
    pre = GAME_PRESETS[idx]
    markup = (
        _toolbar(
            "A game is a pair of dual programmes",
            "the row player maximises the worst case, the column player minimises the best, and they meet",
            [("cyan", "the row player's mixture"), ("purple", "the column player's mixture"),
             ("green", "the value of the game"), ("red", "a pure choice doing worse")],
        )
        + _stage(_svg("gmPlot", "0 0 520 210",
                      "Every pure choice scored against the opponent's optimal mixture, with "
                      "the value of the game marked."))
        + _table("gmTable")
        + _banner("gmStatus")
    )
    controls = (
        _select("gmPreset", "Worked example",
                [(p["key"], p["label"]) for p in GAME_PRESETS], pre["key"])
        + _text("gmMatrix", "The payoffs to the row player &mdash; rows separated by ;", pre["matrix"])
        + _select("gmSide", "Test a pure choice for", [("row", "the row player"),
                                                       ("col", "the column player")], "row")
        + _select("gmPure", "Which one", [("0", "the first")], "0")
        + _kpis([("The value of the game", "gmValue"),
                 ("The row player's mixture", "gmP"),
                 ("The column player's mixture", "gmQ"),
                 ("What that pure choice gets", "gmPure2")])
        + _hint(
            "gmHint",
            "Against an opponent who can see your choice, a single row is something to be "
            "exploited and a mixture is not. Try every pure choice against the optimal "
            "mixture: not one of them does better than the value, and most do worse.",
        )
    )
    script = _CORE_JS + _presets_js(GAME_PRESETS) + _preset_fn("gmPreset", "game") + r"""
  var inM = document.getElementById('gmMatrix'), side = document.getElementById('gmSide');
  var pureSel = document.getElementById('gmPure');
  var plot = document.getElementById('gmPlot'), table = document.getElementById('gmTable');
  var status = document.getElementById('gmStatus');
  var pureIdx = 0;

  function applyPreset() { inM.value = preset().matrix; pureIdx = 0; }
  function fnum(r) { return parseFloat(Rfixed(r, 6)); }

  function redraw() {
    var parsed = Mparse(inM.value, 'the payoff table'), i, j;
    if (parsed.bad) {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = '<span class="tone-red">' + parsed.bad + '.</span> Rows are separated '
        + 'by a semicolon and entries by spaces.';
      return;
    }
    var P = parsed.M, m = P.length, n = P[0].length;
    if (m > 4 || n > 4) {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = '<span class="tone-red">This panel solves games up to four choices '
        + 'each way, and that one is ' + m + ' by ' + n + '.</span> Both programmes are solved '
        + 'exactly, and the tables stay readable only that far.';
      return;
    }
    var g = gameSolve(P);
    if (g.status !== 'optimal') {
      plot.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = 'Both programmes came back ' + g.status + ', which a finite game '
        + 'cannot do &mdash; check the payoffs.';
      return;
    }
    var list = side.value === 'row' ? g.rowPure : g.colPure;
    var opts = '';
    for (i = 0; i < list.length; i += 1) {
      opts += '<option value="' + i + '">' + (side.value === 'row' ? 'row ' : 'column ')
        + (i + 1) + '</option>';
    }
    pureSel.innerHTML = opts;
    if (pureIdx >= list.length) pureIdx = 0;
    pureSel.value = String(pureIdx);
    var chosen = list[pureIdx];

    /* Every pure choice, scored against the opponent's optimal mixture. */
    var vals = list.map(function (t) { return t.payoff; }).concat([g.value]);
    var sp = spanOf(vals), zero = pxOf(g.value, sp.lo, sp.hi, 40, 470);
    var s = '<text x="6" y="16" font-size="11" fill="var(--text)" font-weight="700">'
      + (side.value === 'row'
         ? 'each row, played on its own against the column player\'s mixture'
         : 'each column, played on its own against the row player\'s mixture') + '</text>';
    for (i = 0; i < list.length; i += 1) {
      var yy = 34 + i * 34, px = pxOf(list[i].payoff, sp.lo, sp.hi, 40, 470);
      var good = list[i].atValue;
      s += '<text x="6" y="' + (yy + 14) + '" font-size="10" fill="var(--muted)">'
        + (side.value === 'row' ? 'row ' : 'col ') + (i + 1) + '</text>'
        + '<line x1="' + zero + '" y1="' + yy + '" x2="' + px + '" y2="' + yy
        + '" stroke="var(--' + (good ? 'green' : 'red') + ')" stroke-width="0" />'
        + '<rect x="' + Math.min(zero, px) + '" y="' + yy + '" width="'
        + Math.max(2, Math.abs(px - zero)) + '" height="16" rx="3" fill="var(--'
        + (good ? 'green' : 'red') + ')" opacity="' + (i === pureIdx ? '0.9' : '0.4') + '" />'
        + '<text x="' + (px + (px >= zero ? 8 : -8)) + '" y="' + (yy + 12) + '" font-size="10" '
        + 'text-anchor="' + (px >= zero ? 'start' : 'end') + '" fill="var(--'
        + (good ? 'green' : 'red') + ')">' + Rshort(list[i].payoff, 3) + '</text>';
    }
    var base = 34 + list.length * 34 + 6;
    s += '<line x1="' + zero + '" y1="24" x2="' + zero + '" y2="' + base
      + '" stroke="var(--green)" stroke-width="2" />'
      + '<text x="' + zero + '" y="' + (base + 14) + '" font-size="10" text-anchor="middle" '
      + 'fill="var(--green)" font-weight="700">the value, ' + Rshort(g.value, 3) + '</text>'
      + '<text x="6" y="' + (base + 32) + '" font-size="9" fill="var(--muted)">'
      + (side.value === 'row'
         ? 'nothing to the right of that line: no single row beats the guarantee'
         : 'nothing to the left of it: no single column holds the row player below the value')
      + '</text>';
    plot.innerHTML = s;

    var body = '', heads = [th('&nbsp;')];
    for (j = 0; j < n; j += 1) heads.push(th('col ' + (j + 1)));
    heads.push(th('weight'));
    heads.push(th('on its own'));
    for (i = 0; i < m; i += 1) {
      var cells = [rowhead('row ' + (i + 1))];
      for (j = 0; j < n; j += 1) {
        cells.push(td(Rtext(P[i][j]),
          (!Rzero(g.p[i]) && !Rzero(g.q[j])) ? 'on' : ''));
      }
      cells.push(td(Rshort(g.p[i], 3), 'tone-cyan'));
      cells.push(td(Rshort(g.rowPure[i].payoff, 3), g.rowPure[i].atValue ? 'tone-green' : 'tone-red'));
      body += tr(cells, side.value === 'row' && i === pureIdx ? 'focus' : '');
    }
    var wc = [rowhead('weight')];
    for (j = 0; j < n; j += 1) wc.push(td(Rshort(g.q[j], 3), 'tone-purple'));
    wc.push(td('&mdash;'));
    wc.push(td('&mdash;'));
    body += tr(wc);
    var pc = [rowhead('on its own')];
    for (j = 0; j < n; j += 1) {
      pc.push(td(Rshort(g.colPure[j].payoff, 3), g.colPure[j].atValue ? 'tone-green' : 'tone-red'));
    }
    pc.push(td('&mdash;'));
    pc.push(td(Rshort(g.value, 3), 'tone-green'));
    body += tr(pc, side.value === 'col' ? 'focus' : '');
    table.innerHTML = '<thead>' + tr(heads) + '</thead><tbody>' + body + '</tbody>';

    document.getElementById('gmValue').textContent = Rshort(g.value, 3);
    document.getElementById('gmP').textContent = g.p.map(function (v) { return Rshort(v, 3); }).join(', ');
    document.getElementById('gmQ').textContent = g.q.map(function (v) { return Rshort(v, 3); }).join(', ');
    document.getElementById('gmPure2').textContent = Rshort(chosen.payoff, 3)
      + (chosen.atValue ? ', the value itself' : (side.value === 'row' ? ', which is worse'
                                                  : ', which is worse for that player'));

    status.innerHTML = 'Both programmes were written from the table and solved exactly, and they '
      + 'agree: the row player can guarantee <strong>' + Rshort(g.value, 3) + '</strong> and the '
      + 'column player can hold them to it. That equality is <strong>strong duality between two '
      + 'programmes that are each other\'s dual</strong>, wearing different words. '
      + (g.pure
         ? 'This one has a best single row and a best single column, so mixing buys nothing here '
           + '&mdash; which is the special case, not the rule.'
         : 'There is <strong>no best single choice</strong>: '
           + (side.value === 'row' ? 'row ' : 'column ') + (pureIdx + 1) + ' played on its own gets '
           + Rshort(chosen.payoff, 3)
           + (chosen.atValue
              ? ', which ties the value only because the mixture already puts weight on it'
              : ', which is worse than the guarantee')
           + '. Against an opponent who can see the choice, a single row is exploitable and a '
           + 'mixture is not, and the value is what the mixture guarantees whatever the other '
           + 'side does.');
  }

  document.getElementById('gmPreset').addEventListener('change', function () { applyPreset(); redraw(); });
  inM.addEventListener('input', redraw);
  side.addEventListener('change', function () { pureIdx = 0; redraw(); });
  pureSel.addEventListener('change', function () { pureIdx = +pureSel.value; redraw(); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The minimax theorem is strong duality",
        subtitle="both programmes solved exactly, and every single choice tested against the mixture",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the payoffs, and try a single choice against the mixture"),
        panel_intro=cfg.get(
            "panel_intro",
            "The row player's programme and the column player's are each other's dual, and "
            "the panel writes and solves both. Their common value is the value of the game, "
            "and the last control plays one choice on its own against it.",
        ),
        script=script,
    )

# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

# Ten, and the lesson order rather than the alphabet, because the order IS the
# argument: construct, then the two theorems, then the four things a final
# tableau tells you, then the two ways to use them on a problem that changed,
# then the two places duality is the content rather than the method.
_MODES = {
    "construct": _construct,
    "certificate": _certificate,
    "read": _read,
    "slackness": _slackness,
    "rhs": _rhs,
    "cost": _cost,
    "newcol": _newcol,
    "dualsimplex": _dualsimplex,
    "parametric": _parametric,
    "game": _game,
}

MODES = tuple(sorted(_MODES))


def duality_lab(cfg):
    """This course's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract rather than defensiveness. A kit that quietly fell
    back to a default would render a finished-looking page carrying another
    lesson's widget, and nothing downstream would notice: the markup assertions
    pass, labcheck passes, and the reader is shown the wrong arithmetic under
    the right title. On this course the failure has a specific shape -- `rhs`
    and `cost` are two DIFFERENT ranging computations that look alike on the
    page, and `newcol` and `dualsimplex` both end in a dual simplex run -- so a
    silent fallback between any of them is exactly the confusion the ranging
    lessons exist to remove.

    `newrow` is deliberately absent: `newcol` carries both of its panels. Asking
    for it raises, and the message lists what does exist.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "duality_lab: unknown mode %r; the ten modes of this course are %s"
            % (mode, ", ".join(MODES)))
    return _MODES[mode](cfg or {})


__all__ = ["duality_lab", "DUALITY_KIT_JS", "MODES"]
