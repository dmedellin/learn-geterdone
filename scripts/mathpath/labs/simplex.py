"""Course 2: The Simplex Method -- one kit, seven modes, nine lessons.

The algorithm is the subject here, so this kit's whole job is to make one
pivot at a time visible: which column enters and at what rate, which row
leaves and after which ratio, what the Gauss-Jordan step does to every other
row, and what the tableau says when it refuses to finish.

Three decisions run through all seven modes.

  THE ENGINE IS or_core, NOT A COPY OF IT. `stdForm`, `tabInit`, `tabEnter`,
  `tabRatio`, `tabPivot`, `simplexRun`, `phaseOne`, `farkasCertificate` and
  `basisInverse` ship in scripts/mathpath/labs/or_core.py and are concatenated
  here as source. Nothing in this file re-implements a pivot. `tabPivot`
  returns its row operations in the shape `algebra_systems.Mrref` returns, so
  the trace on the tableau page is printed by the same `Mtrace` that prints
  Gaussian elimination one course earlier -- a reader moving from elimination
  to a tableau reads the same page furniture, because it IS the same code.

  EXACTNESS IS LOAD BEARING, NOT TIDINESS, AND THE PAGE SAYS SO. Two of the
  nine lessons are about results a float destroys. Beale's example returns to
  its starting tableau after six pivots and the claim is that the tableau is
  IDENTICAL -- a statement about equality of numbers, which no double can make
  about 1/50 and -1/25. The Klee-Minty cube costs Dantzig's rule exactly
  2^n - 1 pivots only because every degenerate-looking comparison lands
  exactly; round one of them away and the count collapses and takes the lesson
  with it. Neither figure is reproducible in floating point at all, so the
  `degenerate` and `kleeminty` pages state that on their face.

  THE NUMBERS ARE MEASURED, AND scripts/mathcheck.js PINS THEM. Beale under
  Dantzig: cycled, 6 pivots, entering x1 x2 x3 x4 s1 s2, leaving rows
  1,2,1,2,1,2, z = 0 at all seven tableaux, sixth tableau equal to the first
  entry for entry. Under Bland: optimal in 6 at z* = 1/20. Klee-Minty under
  Dantzig: 3, 7, 15 pivots at n = 2, 3, 4 with z* = 100^(n-1); under Bland
  3, 5, 9; under best improvement 1 at every n. n = 5 is 31 against 15, which
  is why the control stops at 4.

The modes, and the lesson each belongs to:

  walk        L1  the region, the basis at every corner, and a refused jump
  pivot       L2  a reader-named (row, column), every row operation traced
  ratio       L3  every ratio with its reason, and the override that goes wrong
  auto        L4  preset `rules`       rate x step = dz, and four rules counted
              L6  preset `signatures`  the unbounded ray, and the whole edge
              L9  preset `kleeminty`   2^n - 1, and the objective that collapses it
  phase1      L5  artificials minimised, or infeasibility certified by Farkas
  degenerate  L7  Beale's cycle, Bland's escape, and a zero-length pivot
  matrix      L8  B, B^-1 and the three products, entry for entry
"""

import json

from .algebra_core import PLOT_JS, RATIONAL_JS
from .algebra_systems import FEAS_JS, FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import DUAL_JS, ORFMT_JS, PHASE_JS, TABLEAU_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds on top of or_core, as TOP-LEVEL functions so
# scripts/mathcheck.js can call every one of them without a DOM. The two that
# take an SVG element take it as an argument rather than closing over one, for
# the same reason: a helper closed over the document cannot be tested, and the
# untestable parts are the parts that turn out to be wrong.
# ---------------------------------------------------------------------------

SIMPLEX_JS = r"""
  /* ------------------------------------------------- a model from lesson data

     A worked example is written as pairs of integers, never as rationals, and
     becomes exact rationals here, in the browser. Nothing is precomputed:
     change a coefficient with a control and every figure on the page is
     recomputed from this model rather than looked up. */
  function Rpair(p) {
    if (typeof p === 'number') return R(BigInt(p), 1n);
    return R(BigInt(p[0]), BigInt(p.length > 1 ? p[1] : 1));
  }
  function spxModel(spec) {
    return { max: spec.max !== false, names: spec.names.slice(),
             obj: spec.obj.map(Rpair),
             cons: spec.cons.map(function (k) {
               return { a: k.a.map(Rpair), rel: k.rel || 'le', b: Rpair(k.b),
                        name: k.name };
             }),
             free: spec.free || [], nonpos: spec.nonpos || [] };
  }

  /* ---- the worked examples, in the block mathcheck executes ------------

     THE LESSON DATA LIVES HERE, not in the Python that builds the markup, and
     that is deliberate. scripts/mathcheck.js evaluates this block as source,
     so every figure a page prints -- three pivots under Dantzig and one under
     greatest improvement on `mix`, an empty region certified by (-1, 1) on
     `emptyregion` -- is a figure a test can pin against the SAME programme the
     reader sees. A copy of these coefficients in a test file would be a
     transcription, and a transcription proves nothing about the page.

     A key no page names raises, exactly as an unknown mode does. */
  function spxWorked(key) {
    var W = {
      /* the textbook two-product mix: five corners, z* = 36 at (2, 6) */
      plants: { max: true, names: ['x1', 'x2'], obj: [3, 5],
        cons: [{ a: [1, 0], rel: 'le', b: 4, name: 'plant A hours' },
               { a: [0, 2], rel: 'le', b: 12, name: 'plant B hours' },
               { a: [3, 2], rel: 'le', b: 18, name: 'plant C hours' }] },
      orchard: { max: true, names: ['x1', 'x2'], obj: [2, 3],
        cons: [{ a: [1, 1], rel: 'le', b: 7, name: 'land' },
               { a: [2, 1], rel: 'le', b: 10, name: 'water' },
               { a: [1, 3], rel: 'le', b: 15, name: 'labour' }] },
      square: { max: true, names: ['x1', 'x2'], obj: [1, 1],
        cons: [{ a: [1, 0], rel: 'le', b: 3, name: 'first cap' },
               { a: [0, 1], rel: 'le', b: 3, name: 'second cap' }] },
      /* one pivot turns this one into fractions everywhere */
      fractions: { max: true, names: ['x1', 'x2', 'x3'], obj: [4, 3, 6],
        cons: [{ a: [3, 1, 2], rel: 'le', b: 7, name: 'mill time' },
               { a: [1, 4, 2], rel: 'le', b: 9, name: 'kiln time' },
               { a: [2, 2, 5], rel: 'le', b: 11, name: 'packing' }] },
      /* a MINIMISATION: the solver negates it on the way in, so the internal
         value is +24 while the answer the lesson asked for is -24 */
      costmin: { max: false, names: ['x1', 'x2'], obj: [2, -3],
        cons: [{ a: [1, 1], rel: 'le', b: 8, name: 'capacity' },
               { a: [2, 1], rel: 'le', b: 10, name: 'handling' }] },
      /* three boundary lines through (0, 2): a tie, then a pivot of length zero */
      concurrent: { max: true, names: ['x1', 'x2'], obj: [3, 9],
        cons: [{ a: [1, 4], rel: 'le', b: 8, name: 'carving' },
               { a: [1, 2], rel: 'le', b: 4, name: 'finishing' }] },
      /* x2 has no positive entry anywhere, so no row limits it */
      nolimit: { max: true, names: ['x1', 'x2'], obj: [1, 1],
        cons: [{ a: [1, -1], rel: 'le', b: 4, name: 'first' },
               { a: [1, -2], rel: 'le', b: 6, name: 'second' }] },
      /* THE RATE-AGAINST-IMPROVEMENT EXAMPLE. x2 is the steepest column
         (rate 9) and moves z by 36; x3 has rate 3 and moves it by 60, which is
         the whole optimum. Dantzig takes 3 pivots here, greatest improvement 1. */
      mix: { max: true, names: ['x1', 'x2', 'x3'], obj: [5, 9, 3],
        cons: [{ a: [3, 2, 0], rel: 'le', b: 20, name: 'assembly' },
               { a: [1, 3, 0], rel: 'le', b: 12, name: 'finishing' },
               { a: [4, 4, 1], rel: 'le', b: 20, name: 'packing' }] },
      /* a net cost, minimised: one input that costs and two products that
         earn, so the stopping rule is the minimisation one and the optimum is
         negative. Dantzig takes 3 pivots here, greatest improvement 2. */
      netcost: { max: false, names: ['x1', 'x2', 'x3'], obj: [4, -8, -6],
        cons: [{ a: [3, 2, 1], rel: 'le', b: 13, name: 'blending' },
               { a: [4, 0, 2], rel: 'le', b: 17, name: 'roasting' },
               { a: [2, 4, 0], rel: 'le', b: 21, name: 'packing' }] },
      /* the objective escapes along a ray */
      nowhere: { max: true, names: ['x1', 'x2'], obj: [1, 1],
        cons: [{ a: [1, -1], rel: 'le', b: 1, name: 'first' },
               { a: [-1, 1], rel: 'le', b: 1, name: 'second' }] },
      /* the objective is parallel to a binding constraint: a whole optimal edge */
      wholeedge: { max: true, names: ['x1', 'x2'], obj: [3, 2],
        cons: [{ a: [3, 2], rel: 'le', b: 12, name: 'material' },
               { a: [1, 0], rel: 'le', b: 3, name: 'first cap' },
               { a: [0, 1], rel: 'le', b: 5, name: 'second cap' }] },
      /* an UNBOUNDED REGION whose objective is bounded, which is the pair of
         claims this course has to separate. The region runs on for ever along
         (0, 1) -- add as much x2 as you like -- and the objective falls in
         exactly that direction, so it has an optimum anyway. */
      openregion: { max: true, names: ['x1', 'x2'], obj: [2, -1],
        cons: [{ a: [1, -1], rel: 'le', b: 1, name: 'pairing rule' },
               { a: [1, 0], rel: 'le', b: 6, name: 'ceiling' }] },
      /* two requirements and a cap: two artificials, Phase I ends at zero and
         hands a real basic feasible solution to Phase II */
      demandcap: { max: false, names: ['x1', 'x2'], obj: [2, 3],
        cons: [{ a: [1, 1], rel: 'ge', b: 4, name: 'demand' },
               { a: [2, 1], rel: 'ge', b: 5, name: 'quality floor' },
               { a: [1, 0], rel: 'le', b: 3, name: 'capacity' }] },
      /* the empty region the two-variable course drew as a blank picture */
      emptyregion: { max: true, names: ['x1', 'x2'], obj: [1, 1],
        cons: [{ a: [1, 1], rel: 'le', b: 1, name: 'the first line' },
               { a: [1, 1], rel: 'ge', b: 4, name: 'the second line' }] },
      /* the second row IS the first, doubled: an artificial stays basic at zero */
      repeatedrow: { max: true, names: ['x1', 'x2'], obj: [1, 2],
        cons: [{ a: [1, 1], rel: 'eq', b: 4, name: 'balance' },
               { a: [2, 2], rel: 'eq', b: 8, name: 'the same balance, doubled' },
               { a: [0, 1], rel: 'le', b: 3, name: 'storage' }] },
      /* a >= row, so the identity columns are a slack AND an artificial */
      contract: { max: true, names: ['x1', 'x2'], obj: [3, 2],
        cons: [{ a: [1, 1], rel: 'le', b: 4, name: 'capacity' },
               { a: [1, 3], rel: 'ge', b: 6, name: 'contract' }] },
      blend: { max: true, names: ['x1', 'x2', 'x3'], obj: [4, 3, 5],
        cons: [{ a: [1, 1, 1], rel: 'eq', b: 10, name: 'blend' },
               { a: [2, 1, 0], rel: 'le', b: 14, name: 'mill' },
               { a: [0, 1, 3], rel: 'ge', b: 6, name: 'floor' }] }
    };
    if (!W[key]) throw new Error('spxWorked: no worked example named ' + key);
    return spxModel(W[key]);
  }
  function spxWorkedKeys() {
    return ['plants', 'orchard', 'square', 'fractions', 'costmin', 'concurrent', 'nolimit',
            'mix', 'netcost', 'nowhere', 'wholeedge', 'openregion', 'demandcap',
            'emptyregion', 'repeatedrow', 'contract', 'blend'];
  }

  /* ---- printing a programme the way the lesson wrote it ----------------- */

  /* Kit-local rather than algebra_systems' Ltext, which arrives with the whole
     of LINEAR_JS attached -- 2.7 KB gzipped for one printer this needs. */
  function spxTerms(coeffs, names) {
    var out = '', i;
    for (i = 0; i < coeffs.length; i += 1) {
      if (Rzero(coeffs[i])) continue;
      var neg = Rsign(coeffs[i]) < 0, mag = Rabs(coeffs[i]);
      var head = out === '' ? (neg ? '-' : '') : (neg ? ' - ' : ' + ');
      out += head + (Requ(mag, R1) ? '' : Rtext(mag)) + names[i];
    }
    return out === '' ? '0' : out;
  }
  function spxRelText(rel) {
    return rel === 'ge' ? '&gt;=' : (rel === 'eq' ? '=' : '&lt;=');
  }
  function spxConText(model, i) {
    var k = model.cons[i];
    return spxTerms(k.a, model.names) + ' ' + spxRelText(k.rel || 'le') + ' ' + Rtext(k.b);
  }
  function spxObjText(model) {
    return (model.max === false ? 'minimise ' : 'maximise ') + spxTerms(model.obj, model.names);
  }
  function spxPointText(vals) {
    return '(' + vals.map(Rtext).join(', ') + ')';
  }
  function spxBasisText(tab) {
    return '{' + tab.basis.map(function (j) { return tab.names[j]; }).join(', ') + '}';
  }

  /* ---- a tableau at a NAMED basis, not just the one the solver reached ---

     Gauss-Jordan each wanted column into a row that is not already carrying
     one of them. Returns null when the columns are dependent, which is what
     makes "that is not a basis" a computed answer rather than an assumption. */
  function spxTabAt(std, basis, costs) {
    var tab = tabInit(std, costs), i, r, k;
    for (i = 0; i < basis.length; i += 1) {
      k = basis[i];
      if (tab.basis.indexOf(k) >= 0) continue;
      var row = -1;
      for (r = 0; r < tab.m; r += 1) {
        if (basis.indexOf(tab.basis[r]) >= 0) continue;
        if (!Rzero(tab.T[r][k])) { row = r; break; }
      }
      if (row < 0) return null;
      tab = tabPivot(tab, row, k);
    }
    return tab;
  }

  /* ---- corners, and the basis standing at each one ----------------------

     THE TWO-VARIABLE CASE ONLY, and deliberately so: `Ccorners` eliminates y,
     and the whole point of the corner picture is that a reader can see the
     walk. With every row a <=, the columns are x1, x2 and one slack per row,
     so a point fixes every column value and the basis is the columns that are
     not zero there, filled from the zero ones when the corner is degenerate.
     Three lines through one corner is exactly that case. */
  function spxRegionCons(model) {
    var out = model.cons.map(function (k) {
      if ((k.rel || 'le') === 'ge') return Cnew(Rneg(k.a[0]), Rneg(k.a[1]), Rneg(k.b), false, k.name);
      return Cnew(k.a[0], k.a[1], k.b, false, k.name);
    });
    var eqs = [];
    model.cons.forEach(function (k) {
      if ((k.rel || 'le') === 'eq') eqs.push(Cnew(Rneg(k.a[0]), Rneg(k.a[1]), Rneg(k.b), false, k.name));
    });
    return out.concat(eqs).concat([Cnew(R(-1n, 1n), R0, R0, false, 'x1 >= 0'),
                                   Cnew(R0, R(-1n, 1n), R0, false, 'x2 >= 0')]);
  }
  function spxColumnValues(std, x, y) {
    var vals = [x, y], i;
    for (i = 0; i < std.m; i += 1) {
      vals.push(Rsub(std.b[i], Radd(Rmul(std.A[i][0], x), Rmul(std.A[i][1], y))));
    }
    return vals;
  }
  function spxBasisAtPoint(std, vals) {
    var nz = [], zs = [], j;
    for (j = 0; j < std.n; j += 1) (Rzero(vals[j]) ? zs : nz).push(j);
    var basis = nz.slice();
    for (j = 0; j < zs.length && basis.length < std.m; j += 1) {
      if (spxTabAt(std, basis.concat([zs[j]]))) basis = basis.concat([zs[j]]);
    }
    if (basis.length !== std.m) return null;
    basis.sort(function (a, b) { return a - b; });
    return { basis: basis, degenerate: nz.length < std.m, nonzero: nz, zeros: zs };
  }
  /* Every corner of the region, each with the tableau that stands at it. */
  function spxCorners(model) {
    var std = stdForm(model), cons = spxRegionCons(model), pts = Ccorners(cons), out = [];
    pts.forEach(function (p) {
      var vals = spxColumnValues(std, p.x, p.y);
      var b = spxBasisAtPoint(std, vals);
      if (!b) return;
      var tab = spxTabAt(std, b.basis);
      if (!tab) return;
      var read = tabRead(tab);
      out.push({ x: p.x, y: p.y, basis: b.basis, tab: tab, read: read,
                 degenerate: b.degenerate, z: read.zOrig, from: p.from });
    });
    return { std: std, cons: cons, corners: out };
  }

  /* ---- adjacency: one variable in, one variable out --------------------- */
  function spxBasisDiff(a, b) {
    var A = a.slice().sort(function (p, q) { return p - q; });
    var B = b.slice().sort(function (p, q) { return p - q; });
    var leaves = A.filter(function (j) { return B.indexOf(j) < 0; });
    var enters = B.filter(function (j) { return A.indexOf(j) < 0; });
    return { leaves: leaves, enters: enters, changes: leaves.length,
             same: leaves.length === 0, adjacent: leaves.length === 1 };
  }

  /* ---- the ray, evaluated -----------------------------------------------

     `tabRatio(...).ray` is a direction in column space. The point at t is the
     current basic solution plus t times that direction, and z moves by t times
     the rate. Evaluating it at t = 1, 10, 100 is what turns "unbounded" from a
     word into three points a reader can check against the constraints. */
  function spxRayPoint(tab, ray, t) {
    var read = tabRead(tab), tt = Rpair(t), j;
    var cols = [];
    for (j = 0; j < tab.n; j += 1) cols.push(Radd(read.x[j], Rmul(tt, ray[j])));
    var z = R0;
    for (j = 0; j < tab.n; j += 1) z = Radd(z, Rmul(tab.c[j], cols[j]));
    return { t: tt, cols: cols, point: stdPoint(tab.std, cols),
             z: tab.maximised ? z : Rneg(z) };
  }

  /* ---- the second optimal corner ----------------------------------------

     A zero reduced cost on a NONBASIC column at optimality is the signature.
     Pivoting that column in moves to a different basis at the same objective
     value, and every point on the segment between the two is optimal -- which
     the caller checks by sampling, exactly, rather than asserting. */
  function spxAlternate(tab) {
    var j, cands = [];
    for (j = 0; j < tab.n; j += 1) {
      if (tab.basis.indexOf(j) >= 0 || tab.forbid[j]) continue;
      if (Rzero(tab.z[j])) cands.push(j);
    }
    for (j = 0; j < cands.length; j += 1) {
      var rt = tabRatio(tab, cands[j], 'dantzig');
      if (rt.unbounded || rt.leave < 0) continue;
      if (Rzero(rt.rows[rt.leave].ratio)) continue;   /* degenerate, not a second corner */
      return { col: cands[j], name: tab.names[cands[j]], ratio: rt,
               tab: tabPivot(tab, rt.leave, cands[j]), candidates: cands };
    }
    return { col: -1, name: null, ratio: null, tab: null, candidates: cands };
  }
  /* The objective at x = (1-s)P + sQ, exactly. */
  function spxSegment(p, q, s) {
    var ss = Rpair(s), one = Rsub(R1, ss);
    var out = [], i;
    for (i = 0; i < p.length; i += 1) out.push(Radd(Rmul(one, p[i]), Rmul(ss, q[i])));
    return out;
  }
  function spxValue(model, pt) {
    var z = R0, i;
    for (i = 0; i < model.obj.length; i += 1) z = Radd(z, Rmul(model.obj[i], pt[i]));
    return z;
  }

  /* ---- running the thing under each rule -------------------------------- */

  /* THE FOUR RULES ARE LESSON CONTENT. Counting them side by side on one
     programme is what separates "finite" from "fast", and the count is the
     only honest way to say it: nothing here predicts a count, every one is
     run. */
  function spxRules() { return ['dantzig', 'bland', 'bestImprovement', 'lastIndex']; }
  function spxRuleLabel(rule) {
    if (rule === 'bland') return "Bland: smallest index";
    if (rule === 'bestImprovement') return 'greatest improvement: largest rate x step';
    if (rule === 'lastIndex') return 'largest index';
    return 'Dantzig: most negative reduced cost';
  }
  function spxRun(model, rule, maxPivots) {
    var sol = lpSolve(model, { rule: rule, maxPivots: maxPivots || 200 });
    return { rule: rule, sol: sol, status: sol.status,
             pivots: sol.run ? sol.run.pivots : 0,
             z: sol.zOrig, run: sol.run };
  }
  function spxRuleTable(model, maxPivots) {
    return spxRules().map(function (rule) { return spxRun(model, rule, maxPivots); });
  }

  /* ---- rate x step = dz, checked rather than claimed --------------------- */
  function spxDeltaCheck(step) {
    var e = step.rates[step.enter];
    var product = (e && e.step) ? Rmul(e.rate, e.step) : null;
    return { rate: e ? e.rate : null, step: e ? e.step : null, product: product,
             delta: step.delta, ok: product !== null && Requ(product, step.delta) };
  }

  /* ---- an illegal pivot, allowed and then shown ------------------------- */

  /* The ratio test is the rule that keeps every basic variable at or above
     zero. Overriding it is permitted here BECAUSE the wreckage is the lesson:
     this returns the basic variables the override drove below zero and the
     point outside the region that the tableau now stands for. */
  function spxOverride(tab, row, col) {
    if (Rzero(tab.T[row][col])) {
      return { legal: false, zero: true, tab: null, negatives: [],
               why: 'the entry in that row and column is 0, and dividing the row by it is not an operation' };
    }
    var after = tabPivot(tab, row, col);
    var read = tabRead(after), negatives = [], i;
    for (i = 0; i < after.m; i += 1) {
      if (Rsign(after.T[i][after.n]) < 0) {
        negatives.push({ row: i, col: after.basis[i], name: after.names[after.basis[i]],
                         value: after.T[i][after.n] });
      }
    }
    return { legal: negatives.length === 0, zero: false, tab: after, read: read,
             negatives: negatives,
             why: negatives.length === 0
               ? 'every basic variable stayed at or above zero, so the new tableau is a basic FEASIBLE solution'
               : negatives.map(function (n) { return n.name + ' = ' + Rtext(n.value); }).join(', ')
                 + ' -- below zero, so this tableau no longer stands for a point of the region' };
  }
  /* Which constraints a point breaks, and by how much. `Cholds` decides; this
     only reports. */
  function spxViolations(model, x, y) {
    var cons = spxRegionCons(model), out = [], i;
    for (i = 0; i < cons.length; i += 1) {
      if (Cholds(cons[i], x, y)) continue;
      var lhs = Radd(Rmul(cons[i].a, x), Rmul(cons[i].b, y));
      out.push({ index: i, name: cons[i].src, lhs: lhs, rhs: cons[i].c,
                 by: Rsub(lhs, cons[i].c) });
    }
    return out;
  }

  /* ---- two tableaux, compared entry for entry ---------------------------

     "It returns to where it started" is a claim about EQUALITY OF NUMBERS.
     This is the function that makes it one, and it compares the basis, the
     body and the objective row -- not a norm, not a tolerance. */
  function spxTabEqual(a, b) {
    var i, j, diffs = [];
    var key = function (t) { return t.basis.slice().sort(function (p, q) { return p - q; }).join(','); };
    if (key(a) !== key(b)) {
      diffs.push({ where: 'the basis itself', a: a.basis.join(','), b: b.basis.join(',') });
    }
    for (i = 0; i < a.m; i += 1) {
      for (j = 0; j <= a.n; j += 1) {
        if (!Requ(a.T[i][j], b.T[i][j])) {
          diffs.push({ where: 'R' + (i + 1) + ' column ' + (j + 1),
                       a: Rtext(a.T[i][j]), b: Rtext(b.T[i][j]) });
        }
      }
    }
    for (j = 0; j <= a.n; j += 1) {
      if (!Requ(a.z[j], b.z[j])) {
        diffs.push({ where: 'z column ' + (j + 1), a: Rtext(a.z[j]), b: Rtext(b.z[j]) });
      }
    }
    return { equal: diffs.length === 0, diffs: diffs };
  }

  /* ---- the two programmes this course is named for ---------------------- */

  /* BEALE (1955). max (3/4)x1 - 150x2 + (1/50)x3 - 6x4, three rows, x >= 0.
     From the slack basis, Dantzig's rule with the lowest-row-index ratio
     tie-break returns to that basis after exactly six pivots with the tableau
     identical entry for entry; Bland's rule terminates after six at z* = 1/20.
     Same count, different ending: that contrast is the lesson. */
  function bealeModel() {
    return spxModel({ max: true, names: ['x1', 'x2', 'x3', 'x4'],
      obj: [[3, 4], [-150, 1], [1, 50], [-6, 1]],
      cons: [
        { a: [[1, 4], [-60, 1], [-1, 25], [9, 1]], rel: 'le', b: [0, 1], name: 'first' },
        { a: [[1, 2], [-90, 1], [-1, 50], [3, 1]], rel: 'le', b: [0, 1], name: 'second' },
        { a: [[0, 1], [0, 1], [1, 1], [0, 1]], rel: 'le', b: [1, 1], name: 'third' }] });
  }

  /* KLEE-MINTY. max sum 10^(n-j) x_j subject to
     2 sum_{j<i} 10^(i-j) x_j + x_i <= 100^(i-1), a squashed n-cube whose 2^n
     vertices Dantzig's rule visits every one of.

     `reversed` keeps the SAME REGION and the same optimal vertex and only
     turns the objective coefficients round, 10^(j-1) instead of 10^(n-j).
     Dantzig's rule then walks straight there. The pivot count is a property of
     the rule and the objective together, never of the region alone. */
  function kleeMinty(n, reversed) {
    var obj = [], names = [], cons = [], i, j;
    for (j = 1; j <= n; j += 1) {
      obj.push(reversed ? R(10n ** BigInt(j - 1), 1n) : R(10n ** BigInt(n - j), 1n));
      names.push('x' + j);
    }
    for (i = 1; i <= n; i += 1) {
      var a = [];
      for (j = 1; j <= n; j += 1) {
        a.push(j < i ? R(2n * 10n ** BigInt(i - j), 1n) : (j === i ? R1 : R0));
      }
      cons.push({ a: a, rel: 'le', b: R(100n ** BigInt(i - 1), 1n), name: 'face ' + i });
    }
    return { max: true, names: names, obj: obj, cons: cons, free: [], nonpos: [] };
  }
  /* 2^n - 1, as a number to hold the measured count against. */
  function spxCubeBound(n) { return Math.pow(2, n) - 1; }

  /* ---- the tableau as a table ------------------------------------------

     `Mtable` from algebra_systems already prints a matrix with row labels and
     column heads, and `tabMatrix` already puts the body and the objective row
     into one matrix. So this is a caption and a set of labels, and the table
     a reader sees here is the same widget the elimination course drew. */
  function spxHeads(tab) {
    return tab.names.slice().concat(['rhs']);
  }
  function spxRowLabels(tab) {
    return tab.basis.map(function (j) { return tab.names[j]; }).concat(['z']);
  }
  function spxTableauHtml(caption, tab, opts) {
    opts = opts || {};
    return Mtable(caption, tabMatrix(tab), {
      heads: spxHeads(tab), rowlabels: spxRowLabels(tab),
      focus: opts.focus === undefined ? -1 : opts.focus, mark: opts.mark });
  }

  /* ---- the region, drawn ------------------------------------------------

     The svg is an ARGUMENT rather than something this closes over, so the
     drawing can be exercised without a page. Every verdict printed beside the
     picture is exact; only the pixels are floating point, and the shading is
     the one place a picture is sampled rather than decided. */
  function spxWindow(xs, ys) {
    var lo = Math.min(0, Math.min.apply(null, xs)), hi = Math.max.apply(null, xs);
    var lo2 = Math.min(0, Math.min.apply(null, ys)), hi2 = Math.max.apply(null, ys);
    var padx = Math.max(1, (hi - lo) * 0.18), pady = Math.max(1, (hi2 - lo2) * 0.18);
    return { xmin: lo - padx, xmax: hi + padx, ymin: lo2 - pady, ymax: hi2 + pady };
  }
  function spxDrawRegion(svg, model, marks, describe) {
    var cons = spxRegionCons(model), pts = Ccorners(cons);
    var xs = [], ys = [];
    pts.forEach(function (p) { xs.push(Rnum(p.x)); ys.push(Rnum(p.y)); });
    (marks || []).forEach(function (m) { xs.push(Rnum(m.x)); ys.push(Rnum(m.y)); });
    if (!xs.length) { xs = [0, 1]; ys = [0, 1]; }
    var win = spxWindow(xs, ys), plot = Plot(svg, win);
    plot.frame();
    var nums = cons.map(function (k) { return [Rnum(k.a), Rnum(k.b), Rnum(k.c)]; });
    plot.shade(function (x, y) {
      for (var i = 0; i < nums.length; i += 1) {
        if (nums[i][0] * x + nums[i][1] * y > nums[i][2] + 1e-9) return false;
      }
      return true;
    });
    cons.forEach(function (k) {
      var a = Rnum(k.a), b = Rnum(k.b), c = Rnum(k.c);
      if (b === 0) { if (a !== 0) plot.vline(c / a, 'plot-curve alt'); return; }
      plot.segment(win.xmin, (c - a * win.xmin) / b, win.xmax, (c - a * win.xmax) / b, 'plot-curve alt');
    });
    pts.forEach(function (p) { plot.point(Rnum(p.x), Rnum(p.y), 'plot-point'); });
    (marks || []).forEach(function (m) {
      if (m.to) plot.segment(Rnum(m.x), Rnum(m.y), Rnum(m.to.x), Rnum(m.to.y), m.lineClass || 'plot-aux');
    });
    (marks || []).forEach(function (m) {
      plot.point(Rnum(m.x), Rnum(m.y), m.cls || 'plot-point', m.label);
    });
    plot.describe(describe || ('The feasible region of ' + model.cons.length
      + ' constraints with ' + pts.length + ' corner points marked.'));
    return { plot: plot, win: win, corners: pts };
  }
"""


# ---------------------------------------------------------------------------
# The engine, concatenated. or_core's own header says which block needs which
# above it: PHASE_JS needs TABLEAU_JS, DUAL_JS needs both plus MATRIX_JS, and
# everything needs RATIONAL_JS and ORFMT_JS. FEAS_JS and PLOT_JS are the
# two-variable picture; MATRIX_JS is Mtable and Mtrace, which print every
# tableau and every row-operation trace on this course.
#
# One core for all seven modes rather than a per-mode selection. Measured
# rather than estimated, on a rendered lesson page of ordinary prose length:
# the nine blocks are 21.8 KB gzipped, this kit's own SIMPLEX_JS is 7.8 KB, the
# heaviest mode's whole page is 52.1 KB gzipped against the repository's 62 KB
# ceiling, and the lightest is 51 KB. Dropping PLOT_JS and FEAS_JS from the
# four modes that draw nothing would buy about 6 KB and cost the guarantee that
# every mode has the same functions under it; at 52 KB that trade is not worth
# making. Re-derive the figures rather than trusting them -- they go stale
# every time or_core grows.
# ---------------------------------------------------------------------------

_CORE_JS = (RATIONAL_JS + PLOT_JS + FORMAT_JS + MATRIX_JS + FEAS_JS
            + ORFMT_JS + TABLEAU_JS + PHASE_JS + DUAL_JS + SIMPLEX_JS)


# ---------------------------------------------------------------------------
# Control furniture. Every lab on the path uses the same three shapes, so a
# reader moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


def _js_literal(value):
    """A JS literal for lesson data.

    json.dumps output is valid JS and the escape makes "</script>" structurally
    impossible -- the same argument common.cfg_literal makes for its payloads.
    """
    return json.dumps(value).replace("</", "<\\/")


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


def _holder(cid, top=12):
    """A container a mode writes a whole table into.

    The tables come back from `Mtable` and `Mtrace` complete -- `table-wrap`,
    `tt`, caption and all -- so this must NOT restate those classes or the page
    ships a table-wrap inside a table-wrap.
    """
    return '      <div id="%s" style="margin-top:%dpx;"></div>\n' % (cid, top)


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own, so this is how three lessons share mode
    `auto` without any of them showing another lesson's numbers. An unknown
    preset raises for the same reason an unknown mode does: a silent fallback
    ships a page that looks finished and is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("simplex mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "simplex mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "simplex mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


def _options(presets):
    return [(i, p["label"]) for i, p in enumerate(presets)]


# ---------------------------------------------------------------------------
# L1 - walk: the region, the basis at every corner, and a refused jump
# ---------------------------------------------------------------------------
#
# The misconception this mode exists to break is that the method searches the
# interior, or else tries every corner and keeps the best. It does neither, and
# the way to show that is to let a reader try to jump: two corners are ADJACENT
# when their bases differ in exactly one column, and a jump to any other corner
# is refused with the two columns that would have had to change at once.

WALK_PRESETS = [
    {"key": "plants", "label": "two products across three plants", "worked": "plants"},
    {"key": "orchard", "label": "three resources, five corners", "worked": "orchard"},
    {"key": "square", "label": "a square, where the diagonal is the refusal", "worked": "square"},
]


def _walk(cfg):
    idx = _preset_index(cfg, WALK_PRESETS, "walk")
    p = WALK_PRESETS[idx]

    markup = (
        _toolbar(
            "Corner to adjacent corner",
            "the basis at every corner, and the single column an edge exchanges",
            [("cyan", "the region"), ("green", "where the basis stands"),
             ("amber", "the corner you asked for"), ("red", "refused: two changes at once")],
        )
        + _stage(_svg("wkPlot", "0 0 660 420",
                      "The feasible region with every corner marked, the current basis highlighted, "
                      "and the requested move drawn as an edge."))
        + _holder("wkTable")
        + _holder("wkPath")
        + _banner("wkStatus")
    )
    controls = (
        _select("wkPreset", "Worked example", _options(WALK_PRESETS), idx)
        + _range("wkFrom", "The basis stands at corner", 0, 7, 0)
        + _range("wkTo", "Try to move to corner", 0, 7, 1)
        + _range("wkC1", "objective coefficient on x1", -4, 9, 0)
        + _range("wkC2", "objective coefficient on x2", -4, 9, 0)
        + _kpis([("Basis here", "wkBasis"), ("Objective here", "wkZ"),
                 ("Columns exchanged", "wkExchange"), ("Verdict", "wkVerdict")])
        + _hint(
            "wkHint",
            "A basis is a set of columns, so two corners are adjacent exactly when their sets "
            "differ in one member. Everything else on the picture is a corner the method never "
            "considers from here, however close it looks.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal([q["worked"] for q in WALK_PRESETS]) + ";\n" + r"""
  var preset = document.getElementById('wkPreset');
  var fromS = document.getElementById('wkFrom'), toS = document.getElementById('wkTo');
  var c1S = document.getElementById('wkC1'), c2S = document.getElementById('wkC2');
  var plot = document.getElementById('wkPlot'), cornerOut = document.getElementById('wkTable');
  var pathOut = document.getElementById('wkPath'), status = document.getElementById('wkStatus');
  /* null, not the control's value, so the FIRST redraw also syncs the two
     objective sliders to the worked example rather than to the markup. */
  var lastPreset = null;

  function redraw() {
    var model = spxWorked(PRESETS[+preset.value]);
    if (preset.value !== lastPreset) {
      lastPreset = preset.value;
      c1S.value = Rtext(model.obj[0]);
      c2S.value = Rtext(model.obj[1]);
    }
    model.obj = [R(BigInt(+c1S.value), 1n), R(BigInt(+c2S.value), 1n)];
    document.getElementById('wkC1Out').textContent = c1S.value;
    document.getElementById('wkC2Out').textContent = c2S.value;
    var found = spxCorners(model), cs = found.corners;
    var lo = 0, hi = cs.length - 1;
    var i = Math.max(lo, Math.min(hi, +fromS.value));
    var j = Math.max(lo, Math.min(hi, +toS.value));
    document.getElementById('wkFromOut').textContent = spxPointText([cs[i].x, cs[i].y]);
    document.getElementById('wkToOut').textContent = spxPointText([cs[j].x, cs[j].y]);

    var here = cs[i], there = cs[j];
    var diff = spxBasisDiff(here.basis, there.basis);
    document.getElementById('wkBasis').textContent = spxBasisText(here.tab);
    document.getElementById('wkZ').textContent = Rtext(here.z);
    document.getElementById('wkExchange').textContent = diff.same
      ? 'none, it is the same basis'
      : (there.tab.names[diff.enters[0]] + ' in, ' + here.tab.names[diff.leaves[0]] + ' out'
         + (diff.changes > 1 ? ' and ' + (diff.changes - 1) + ' more' : ''));
    document.getElementById('wkVerdict').textContent = diff.same ? 'already there'
      : (diff.adjacent ? 'one edge away' : diff.changes + ' columns at once');

    /* The path the method actually walks from the slack basis, so the reader
       can see that it visits a PATH and not every corner. */
    var run = lpSolve(model, { rule: 'dantzig', maxPivots: 60 });
    var visited = [], seen = {};
    if (run.run) {
      run.run.path.forEach(function (t) {
        var pt = stdPoint(t.std, tabRead(t).x);
        seen[Rtext(pt[0]) + '|' + Rtext(pt[1])] = true;
        visited.push(pt);
      });
    }

    var marks = [];
    for (var k = 1; k < visited.length; k += 1) {
      marks.push({ x: visited[k - 1][0], y: visited[k - 1][1],
                   to: { x: visited[k][0], y: visited[k][1] }, lineClass: 'plot-aux',
                   cls: 'plot-hole' });
    }
    marks.push({ x: here.x, y: here.y, cls: 'plot-point', label: 'basis here',
                 to: { x: there.x, y: there.y },
                 lineClass: diff.adjacent || diff.same ? 'plot-curve' : 'plot-asym' });
    marks.push({ x: there.x, y: there.y, cls: 'plot-point', label: diff.same ? '' : 'asked for' });
    spxDrawRegion(plot, model, marks,
      'The feasible region, the walk the method takes from the origin, and the move from '
      + spxPointText([here.x, here.y]) + ' to ' + spxPointText([there.x, there.y])
      + (diff.adjacent ? ', which is one edge' : ', which is not an edge') + '.');

    cornerOut.innerHTML = spxCornerTable(model, cs, i, seen);
    pathOut.innerHTML = table('The walk from the slack basis, one edge at a time',
      ['pivot', 'entering', 'leaving', 'corner reached', 'objective'],
      (run.run ? run.run.steps : []).map(function (s, k) {
        var pt = visited[k + 1];
        return tr([rowhead(String(k + 1)), td(s.enterName), td(s.leaveName),
                   tdl(spxPointText(pt)), td(Rtext(run.std.maximised ? s.zAfter : Rneg(s.zAfter)))]);
      }));

    var reason;
    if (diff.same) {
      reason = 'That is the corner the basis already stands at, so there is nothing to exchange.';
    } else if (diff.adjacent) {
      reason = 'Those two bases differ in exactly one column: <strong>'
        + there.tab.names[diff.enters[0]] + '</strong> comes in and <strong>'
        + here.tab.names[diff.leaves[0]] + '</strong> goes out. That is one edge of the region, and '
        + 'one pivot of the method. The objective goes from <strong>' + Rtext(here.z)
        + '</strong> to <strong>' + Rtext(there.z) + '</strong>.';
    } else {
      reason = '<span class="tone-red">Refused.</span> Getting from ' + spxBasisText(here.tab)
        + ' to ' + spxBasisText(there.tab) + ' means changing <strong>' + diff.changes
        + '</strong> columns at once &mdash; ' + diff.leaves.map(function (c) { return here.tab.names[c]; }).join(' and ')
        + ' out, ' + diff.enters.map(function (c) { return there.tab.names[c]; }).join(' and ')
        + ' in. One pivot exchanges one column, so no single pivot goes there: those two corners '
        + 'are not joined by an edge, and the method walks the boundary rather than jumping across it.';
    }
    status.innerHTML = reason + ' The region has <strong>' + cs.length + '</strong> corners and the '
      + 'method visited <strong>' + visited.length + '</strong> of them, in <strong>'
      + (run.run ? run.run.pivots : 0) + '</strong> ' + plural(run.run ? run.run.pivots : 0, 'pivot', 'pivots')
      + ' &mdash; which is why the number of corners is not the amount of work.';
  }

  function spxCornerTable(model, cs, current, seen) {
    return table('Every corner of the region, and the basis standing at it',
      ['corner', 'basis', 'objective', 'one edge from here?', 'on the walk?'],
      cs.map(function (c, k) {
        var d = spxBasisDiff(cs[current].basis, c.basis);
        var mark = d.same ? chip('standing here', 'ok')
          : (d.adjacent ? chip('yes', 'ok') : chip(d.changes + ' columns differ', 'no'));
        return tr([tdl(spxPointText([c.x, c.y]) + (c.degenerate ? ' ' + chip('degenerate', 'warn') : '')),
                   tdl(spxBasisText(c.tab)), td(Rtext(c.z)), td(mark),
                   td(seen[Rtext(c.x) + '|' + Rtext(c.y)] ? chip('visited', 'ok') : '')],
                  d.same ? 'focus' : '');
      }));
  }

  preset.addEventListener('change', redraw);
  [fromS, toS, c1S, c2S].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Adjacent corners, and the column an edge exchanges",
        subtitle="Two bases are adjacent when they differ in exactly one column; anything else is not an edge",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose two corners"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every corner's basis is read off a tableau built at that corner, and the verdict "
            "on a move is the size of the difference between two sets of columns.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 - pivot: a reader-named (row, column), every row operation traced
# ---------------------------------------------------------------------------
#
# The misconception is that the z-row is a running total kept outside the row
# operations. It is one more equation, `tabPivot` carries it through every
# step, and the trace prints it as row `z` beside R1, R2 and R3 so that
# leaving it out is visibly the same error as dropping the constant column
# from an elimination.
#
# An ILLEGAL pivot is permitted here and shown, not prevented: the negative
# right-hand side it produces is the evidence that the ratio test is a rule
# about staying in the region rather than a formality.

PIVOT_PRESETS = [
    {"key": "plants", "label": "two products across three plants",
     "worked": "plants", "row": 2, "col": 2},
    {"key": "fractions", "label": "a pivot that turns the tableau into fractions",
     "worked": "fractions", "row": 1, "col": 1},
    {"key": "minimise", "label": "a minimisation, where the sign convention bites",
     "worked": "costmin", "row": 1, "col": 2},
]


def _pivot(cfg):
    idx = _preset_index(cfg, PIVOT_PRESETS, "pivot")
    p = PIVOT_PRESETS[idx]

    markup = (
        _toolbar(
            "One pivot, every row operation",
            "a Gauss-Jordan step on the chosen column, applied to the objective row too",
            [("cyan", "the starting tableau"), ("green", "the pivot entry"),
             ("amber", "the row operations"), ("red", "a right-hand side below zero")],
        )
        + _stage('<div id="pvStart"></div>')
        + _holder("pvTrace")
        + _holder("pvAfter")
        + _banner("pvStatus")
    )
    controls = (
        _select("pvPreset", "Worked example", _options(PIVOT_PRESETS), idx)
        + _range("pvRow", "Pivot on row", 1, 4, p["row"])
        + _range("pvCol", "Pivot on column", 1, 9, p["col"])
        + _kpis([("Pivot entry", "pvEntry"), ("Basic solution after", "pvPoint"),
                 ("Objective after", "pvZ"), ("Legal?", "pvLegal")])
        + _hint(
            "pvHint",
            "The rules would choose this pivot for you. You do not have to let them: name any "
            "row and any column and the step is carried out exactly as written, including the "
            "one that leaves a basic variable negative.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal(PIVOT_PRESETS) + ";\n" + r"""
  var preset = document.getElementById('pvPreset');
  var rowS = document.getElementById('pvRow'), colS = document.getElementById('pvCol');
  var startOut = document.getElementById('pvStart'), traceOut = document.getElementById('pvTrace');
  var afterOut = document.getElementById('pvAfter'), status = document.getElementById('pvStatus');
  var lastPreset = preset.value;

  function redraw() {
    var p = PRESETS[+preset.value];
    if (preset.value !== lastPreset) {
      lastPreset = preset.value;
      rowS.value = p.row; colS.value = p.col;
    }
    var model = spxWorked(p.worked), std = stdForm(model), tab = tabInit(std);
    var r = Math.max(0, Math.min(std.m - 1, (+rowS.value) - 1));
    var k = Math.max(0, Math.min(std.n - 1, (+colS.value) - 1));
    document.getElementById('pvRowOut').textContent = 'R' + (r + 1) + '  (' + tab.names[tab.basis[r]] + ' is basic there)';
    document.getElementById('pvColOut').textContent = tab.names[k];

    var labels = [];
    for (var i = 0; i < std.m; i += 1) labels.push('R' + (i + 1));
    labels.push('z');
    startOut.innerHTML = spxTableauHtml(spxObjText(model) + ',  as a tableau', tab,
      { focus: r, mark: function (i2, j2) { return i2 === r && j2 === k; } });

    var entry = tab.T[r][k];
    document.getElementById('pvEntry').textContent = tab.names[k] + ' in R' + (r + 1) + ' = ' + Rtext(entry);

    var move = spxOverride(tab, r, k);
    if (move.zero) {
      traceOut.innerHTML = steps('No operation to trace',
        [['R' + (r + 1) + ' / 0', 'the pivot entry is 0, and a Gauss-Jordan step divides the row by it']]);
      afterOut.innerHTML = '';
      document.getElementById('pvPoint').textContent = 'unchanged';
      document.getElementById('pvZ').textContent = 'unchanged';
      document.getElementById('pvLegal').textContent = 'no such pivot';
      status.innerHTML = '<span class="tone-red">There is no pivot here.</span> The entry of '
        + tab.names[k] + ' in R' + (r + 1) + ' is <strong>0</strong>. A pivot divides the row by that '
        + 'entry to make it 1, and no multiple of a row of zeros will ever clear '
        + tab.names[k] + ' out of the others. Choose a row where ' + tab.names[k] + ' is not 0.';
      return;
    }

    var after = move.tab, read = move.read, pt = stdPoint(std, read.x);
    traceOut.innerHTML = Mtrace('The pivot, one row operation at a time', tabMatrix(tab), after.ops,
      { heads: spxHeads(tab), rowlabels: labels });
    afterOut.innerHTML = spxTableauHtml('After the pivot: ' + tab.names[k] + ' is basic in R' + (r + 1)
      + ', ' + tab.names[tab.basis[r]] + ' is not', after,
      { focus: r, mark: function (i2, j2) {
        return i2 < after.m && j2 === after.n && Rsign(after.T[i2][after.n]) < 0;
      } });

    document.getElementById('pvPoint').textContent = model.names.join(', ') + ' = ' + spxPointText(pt);
    document.getElementById('pvZ').textContent = Rtext(read.zOrig)
      + (std.maximised ? '' : '  (internally ' + Rtext(read.z) + ', because the solver maximises)');
    document.getElementById('pvLegal').textContent = move.legal ? 'yes, still feasible' : 'permitted, not feasible';

    var enter = tabEnter(tab, 'dantzig');
    var wouldRow = -1;
    if (enter.enter >= 0) {
      var rt = tabRatio(tab, enter.enter, 'dantzig');
      wouldRow = rt.unbounded ? -1 : rt.leave;
    }
    var advice = enter.enter < 0
      ? 'No column has a negative reduced cost here, so the rules would have stopped rather than pivoted.'
      : ('The rules would have chosen <strong>' + tab.names[enter.enter] + '</strong> in <strong>R'
         + (wouldRow + 1) + '</strong>: ' + enter.why + '.');

    if (move.legal) {
      status.innerHTML = 'Every right-hand side stayed at or above zero, so this tableau still stands for '
        + 'a corner of the region: ' + model.names.join(', ') + ' = <strong>' + spxPointText(pt)
        + '</strong> with objective <strong>' + Rtext(read.zOrig) + '</strong>. '
        + after.ops.length + ' row ' + plural(after.ops.length, 'operation', 'operations')
        + ' did it, and the objective row was one of them &mdash; look at the z line of the trace, which '
        + 'moved with the others. ' + advice;
    } else {
      status.innerHTML = '<span class="tone-red">This pivot was carried out and it left the region.</span> '
        + move.why + '. The tableau is still algebraically correct &mdash; the equations all hold &mdash; '
        + 'but a basic variable below zero means the point it describes, ' + spxPointText(pt)
        + ', is not in the region at all. That is the whole job of the ratio test: it is the rule that '
        + 'keeps this from happening. ' + advice;
    }
  }

  preset.addEventListener('change', redraw);
  [rowS, colS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The tableau, and one pivot carried out on it",
        subtitle="A Gauss-Jordan step on a chosen column, with the objective row carried through like any other",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Name a row and a column"),
        panel_intro=cfg.get(
            "panel_intro",
            "The trace below the tableau is the same trace the elimination lab prints, because it is "
            "the same code: a pivot here is a Gauss-Jordan step with one extra row.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L3 - ratio: every ratio with its reason, and the override that goes wrong
# ---------------------------------------------------------------------------
#
# The misconception is that the ratio test is a rule about ALL the rows.
# `tabRatio` returns a reason for every row, including the two reasons a row
# is excluded -- a zero entry, which never binds, and a negative one, where
# the basic variable GROWS as the entering variable does. Taking the minimum
# over the excluded rows as well is exactly the override this mode offers, and
# the point it lands on is drawn outside the region with the constraint it
# breaks named.

RATIO_PRESETS = [
    {"key": "plants", "label": "two products across three plants",
     "worked": "plants", "col": 2, "row": 3},
    {"key": "tie", "label": "a tie in the ratio test", "worked": "concurrent", "col": 2, "row": 2},
    {"key": "nolimit", "label": "a column no row limits at all",
     "worked": "nolimit", "col": 2, "row": 1},
]


def _ratio(cfg):
    idx = _preset_index(cfg, RATIO_PRESETS, "ratio")
    p = RATIO_PRESETS[idx]

    markup = (
        _toolbar(
            "The ratio test, row by row",
            "the longest step along the edge that leaves every basic variable at or above zero",
            [("cyan", "the region"), ("green", "where the ratio test lands"),
             ("amber", "a row the test excludes"), ("red", "where your override lands")],
        )
        + _stage(_svg("rtPlot", "0 0 660 420",
                      "The feasible region, the point the ratio test moves to, and the point an "
                      "overridden leaving row moves to."))
        + _holder("rtTable")
        + _holder("rtAfter")
        + _banner("rtStatus")
    )
    controls = (
        _select("rtPreset", "Worked example", _options(RATIO_PRESETS), idx)
        + _range("rtCol", "Entering column", 1, 8, p["col"])
        + _range("rtRow", "Leave from row (yours)", 1, 4, p["row"])
        + _kpis([("Smallest ratio", "rtMin"), ("Row the test chooses", "rtPick"),
                 ("Your row lands at", "rtPoint"), ("Still in the region?", "rtOk")])
        + _hint(
            "rtHint",
            "A row with a zero entry never binds and a row with a negative one never binds either "
            "&mdash; its basic variable grows as the entering one does. Only the strictly positive "
            "entries produce a limit, and the smallest of those limits is the step.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal(RATIO_PRESETS) + ";\n" + r"""
  var preset = document.getElementById('rtPreset');
  var colS = document.getElementById('rtCol'), rowS = document.getElementById('rtRow');
  var plot = document.getElementById('rtPlot'), table_ = document.getElementById('rtTable');
  var afterOut = document.getElementById('rtAfter'), status = document.getElementById('rtStatus');
  var lastPreset = preset.value;

  function redraw() {
    var p = PRESETS[+preset.value];
    if (preset.value !== lastPreset) {
      lastPreset = preset.value; colS.value = p.col; rowS.value = p.row;
    }
    var model = spxWorked(p.worked), std = stdForm(model), tab = tabInit(std);
    var k = Math.max(0, Math.min(std.n - 1, (+colS.value) - 1));
    var mine = Math.max(0, Math.min(std.m - 1, (+rowS.value) - 1));
    document.getElementById('rtColOut').textContent = tab.names[k];
    document.getElementById('rtRowOut').textContent = 'R' + (mine + 1) + ' (' + tab.names[tab.basis[mine]] + ' leaves)';

    var rt = tabRatio(tab, k, 'dantzig');
    var rate = Rneg(tab.z[k]);
    document.getElementById('rtMin').textContent = rt.unbounded ? 'there is none' : Rtext(rt.min);
    document.getElementById('rtPick').textContent = rt.unbounded ? 'no row limits this column'
      : 'R' + (rt.leave + 1) + ' (' + tab.names[tab.basis[rt.leave]] + ' leaves)'
        + (rt.tie.length > 1 ? ', after a ' + rt.tie.length + '-way tie' : '');

    table_.innerHTML = table('Every row tested against column ' + tab.names[k],
      ['row', 'basic there', 'right-hand side', 'entry in ' + tab.names[k], 'ratio', 'why'],
      rt.rows.map(function (row, i) {
        var cls = '';
        if (!rt.unbounded && i === rt.leave) cls = 'focus';
        return tr([rowhead('R' + (i + 1)), td(tab.names[row.leaving]), td(Rtext(row.b)),
                   td(Rtext(row.a)), td(row.eligible ? Rtext(row.ratio) : chip('excluded', 'no')),
                   tdl(row.why)], cls);
      }));

    var marks = [], here = stdPoint(std, tabRead(tab).x);
    marks.push({ x: here[0], y: here[1], cls: 'plot-point', label: 'now' });
    var correct = null, mineMove = spxOverride(tab, mine, k);
    if (!rt.unbounded) {
      var ct = tabPivot(tab, rt.leave, k);
      correct = stdPoint(std, tabRead(ct).x);
      marks.push({ x: correct[0], y: correct[1], cls: 'plot-point',
                   label: 'ratio test: ' + spxPointText(correct),
                   to: { x: here[0], y: here[1] }, lineClass: 'plot-curve' });
    }
    var minePt = null;
    if (!mineMove.zero) {
      minePt = stdPoint(std, mineMove.read.x);
      marks.push({ x: minePt[0], y: minePt[1], cls: 'plot-hole',
                   label: mineMove.legal ? '' : 'yours: ' + spxPointText(minePt),
                   to: { x: here[0], y: here[1] }, lineClass: mineMove.legal ? 'plot-curve' : 'plot-asym' });
    }
    spxDrawRegion(plot, model, marks,
      'The feasible region with the point the ratio test reaches and the point the chosen row reaches.');

    document.getElementById('rtPoint').textContent = mineMove.zero ? 'nowhere: the entry is 0'
      : spxPointText(minePt);
    document.getElementById('rtOk').textContent = mineMove.zero ? 'no pivot'
      : (mineMove.legal ? 'yes' : 'no');

    afterOut.innerHTML = mineMove.zero ? '' : spxTableauHtml(
      'The tableau after leaving from R' + (mine + 1), mineMove.tab,
      { mark: function (i2, j2) {
        return i2 < mineMove.tab.m && j2 === mineMove.tab.n && Rsign(mineMove.tab.T[i2][j2]) < 0;
      } });

    if (rt.unbounded) {
      status.innerHTML = '<span class="tone-amber">No row limits this column.</span> Every entry of '
        + tab.names[k] + ' is zero or negative, so no basic variable is driven down as ' + tab.names[k]
        + ' grows: ' + tab.names[k] + ' can be raised for ever and the objective rises by <strong>'
        + Rtext(rate) + '</strong> per unit without end. There is no leaving row to choose, and the '
        + 'right answer is not a pivot at all &mdash; it is the word <em>unbounded</em>.';
      return;
    }
    var breaks = mineMove.zero ? [] : spxViolations(model, minePt[0], minePt[1]);
    if (mine === rt.leave) {
      status.innerHTML = 'That is the row the test chooses. ' + rt.rows[rt.leave].why
        + ', and every other eligible row allows a larger step than the region does. The point moves from '
        + spxPointText(here) + ' to <strong>' + spxPointText(correct) + '</strong>, with the objective '
        + 'rising by rate ' + Rtext(rate) + ' times step ' + Rtext(rt.min) + ' = <strong>'
        + Rtext(Rmul(rate, rt.min)) + '</strong>.'
        + (rt.tie.length > 1
            ? ' <span class="tone-amber">Two rows tie at ' + Rtext(rt.min) + '.</span> Whichever leaves, '
              + 'the other stays basic AT ZERO, and the next basis is degenerate.'
            : '');
    } else if (!mineMove.zero && mineMove.legal) {
      status.innerHTML = '<span class="tone-amber">That row is legal but short.</span> Leaving from R'
        + (mine + 1) + ' lands at ' + spxPointText(minePt) + ' rather than ' + spxPointText(correct)
        + ', so the step stops before the edge runs out and the objective reaches only '
        + Rtext(tabRead(mineMove.tab).zOrig) + ' instead of ' + Rtext(tabRead(tabPivot(tab, rt.leave, k)).zOrig)
        + '. Nothing is broken; the method just did less work than it could have.';
    } else if (mineMove.zero) {
      status.innerHTML = '<span class="tone-red">There is no pivot in that row.</span> The entry of '
        + tab.names[k] + ' in R' + (mine + 1) + ' is 0, so that row says nothing about how far '
        + tab.names[k] + ' can grow, and it cannot be divided by it either.';
    } else {
      status.innerHTML = '<span class="tone-red">That row is not eligible, and here is what it costs.</span> '
        + rt.rows[mine].why + '. Leaving from R' + (mine + 1) + ' anyway drives '
        + mineMove.negatives.map(function (n) { return '<strong>' + n.name + ' to ' + Rtext(n.value) + '</strong>'; }).join(' and ')
        + ', which puts the point at ' + spxPointText(minePt) + ' &mdash; outside the region, drawn hollow '
        + 'on the picture. It breaks '
        + (breaks.length
            ? breaks.map(function (v) { return '<strong>' + v.name + '</strong> by ' + Rtext(v.by); }).join(' and ')
            : 'a non-negativity requirement')
        + '. The ratio test is not bookkeeping: it is the only thing keeping the walk inside the region.';
    }
  }

  preset.addEventListener('change', redraw);
  [colS, rowS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The ratio test, and what overriding it costs",
        subtitle="Only the strictly positive entries limit the step, and the smallest of those limits is it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose a column, then a row"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every row gets a ratio or a reason it has none. Override the choice and the basic "
            "variable that goes negative is named, and the point it lands on is drawn outside the region.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L4, L6, L9 - auto: one solver, three panels
# ---------------------------------------------------------------------------
#
# The three lessons that share this mode are separated by the `preset` key,
# and each preset changes what the PANEL TABULATES as well as the data:
#
#   rules       rate, step, rate x step and dz at every pivot, and the four
#               entering rules counted against each other on one programme
#   signatures  the improving column with no positive entry, and the zero
#               reduced cost on a nonbasic column -- the ray evaluated at
#               t = 1, 10, 100, or the objective sampled along the whole edge
#   kleeminty   the measured pivot count against 2^n - 1, under each rule,
#               with the objective reversed on the same region
#
# One solver, three drawings. A fourth preset name raises, exactly as an
# unknown mode does.

AUTO_PRESETS = [
    {"key": "rules", "label": "rate times step, and four entering rules"},
    {"key": "signatures", "label": "the ray, and the whole edge"},
    {"key": "kleeminty", "label": "the cube that costs two to the n"},
]

RULES_CASES = [
    {"key": "mix", "label": "three products: the steepest column is the wrong one", "worked": "mix"},
    {"key": "plants", "label": "two products across three plants", "worked": "plants"},
    {"key": "netcost", "label": "a net cost, minimised: the stopping rule flips", "worked": "netcost"},
]


SIGNATURE_CASES = [
    {"key": "nowhere", "label": "nowhere to stop: an improving column with no positive entry",
     "worked": "nowhere"},
    {"key": "wholeedge", "label": "the whole edge: a zero reduced cost off the basis",
     "worked": "wholeedge"},
    {"key": "bounded", "label": "an unbounded region whose objective is not",
     "worked": "openregion"},
]


def _auto(cfg):
    idx = _preset_index(cfg, AUTO_PRESETS, "auto")
    return (_auto_rules, _auto_signatures, _auto_kleeminty)[idx](cfg)


def _auto_rules(cfg):
    markup = (
        _toolbar(
            "Rate times step is the improvement",
            "the reduced cost is a rate, the ratio test is the step, and only their product moves z",
            [("cyan", "every candidate column"), ("green", "the column the rule takes"),
             ("amber", "the largest actual improvement on offer"), ("muted", "not eligible")],
        )
        + _stage('<div id="arSteps"></div>')
        + _holder("arCands")
        + _holder("arRules")
        + _banner("arStatus")
    )
    controls = (
        _select("arCase", "Worked example", _options(RULES_CASES), 0)
        + _select("arRule", "Entering rule",
                  [("dantzig", "Dantzig: most negative reduced cost"),
                   ("bland", "Bland: smallest index"),
                   ("bestImprovement", "greatest improvement: largest rate times step"),
                   ("lastIndex", "largest index")], "dantzig")
        + _range("arStep", "Inspect the candidates at pivot", 1, 12, 1)
        + _kpis([("Pivots under this rule", "arPivots"), ("Optimum reached", "arZ"),
                 ("Steepest column here", "arSteep"), ("Most improving column here", "arBest")])
        + _hint(
            "arHint",
            "The steepest column is the one with the most negative reduced cost. The most improving "
            "column is the one with the largest rate times step. They are routinely not the same "
            "column, and only the second one is about the objective.",
        )
    )

    script = _CORE_JS + "  var CASES = " + _js_literal([q["worked"] for q in RULES_CASES]) + ";\n" + r"""
  var caseS = document.getElementById('arCase'), ruleS = document.getElementById('arRule');
  var stepS = document.getElementById('arStep');
  var stepsOut = document.getElementById('arSteps'), candsOut = document.getElementById('arCands');
  var rulesOut = document.getElementById('arRules'), status = document.getElementById('arStatus');

  function redraw() {
    var model = spxWorked(CASES[+caseS.value]), rule = ruleS.value;
    var sol = lpSolve(model, { rule: rule, maxPivots: 60 });
    var steps_ = sol.run ? sol.run.steps : [];
    var at = Math.max(0, Math.min(steps_.length - 1, (+stepS.value) - 1));
    document.getElementById('arStepOut').textContent = steps_.length
      ? (at + 1) + ' of ' + steps_.length : 'none to inspect';

    document.getElementById('arPivots').textContent = sol.run ? sol.run.pivots : 0;
    document.getElementById('arZ').textContent = sol.status === 'optimal'
      ? Rtext(sol.zOrig) : sol.status;

    /* Every pivot, with rate x step = dz CHECKED rather than asserted. */
    var allOk = true;
    stepsOut.innerHTML = table(spxObjText(model) + ' &mdash; ' + spxRuleLabel(rule),
      ['pivot', 'in', 'out', 'rate', 'step', 'rate x step', 'change in z', 'z after'],
      steps_.map(function (s, i) {
        var d = spxDeltaCheck(s);
        if (!d.ok) allOk = false;
        var zAfter = sol.std.maximised ? s.zAfter : Rneg(s.zAfter);
        return tr([rowhead(String(i + 1)), td(s.enterName), td(s.leaveName),
                   td(Rtext(d.rate)), td(Rtext(d.step)), td(Rtext(d.product)),
                   td(Rtext(s.delta) + ' ' + (d.ok ? chip('equal', 'ok') : chip('differs', 'no'))),
                   td(Rtext(zAfter))], i === at ? 'focus' : '');
      }));

    if (!steps_.length) {
      candsOut.innerHTML = '';
    } else {
      var s = steps_[at], best = null, steep = null;
      s.rates.forEach(function (r) {
        if (!r.eligible) return;
        if (steep === null || Rcmp(r.reduced, steep.reduced) < 0) steep = r;
        if (r.unbounded) { best = r; return; }
        if (best === null || (best.delta && Rcmp(r.delta, best.delta) > 0)) best = r;
      });
      document.getElementById('arSteep').textContent = steep ? steep.name + ' (rate ' + Rtext(steep.rate) + ')' : 'none';
      document.getElementById('arBest').textContent = best
        ? best.name + (best.delta ? ' (moves z by ' + Rtext(best.delta) + ')' : ' (without limit)') : 'none';
      candsOut.innerHTML = table('Pivot ' + (at + 1) + ': every column, before the rule chooses',
        ['column', 'reduced cost', 'rate', 'step', 'rate x step', 'status'],
        s.rates.map(function (r) {
          var cls = r.j === s.enter ? 'focus' : '';
          var note = r.basic ? chip('basic', 'muted')
            : (!r.eligible ? chip('no improvement', 'muted')
               : (r.unbounded ? chip('no limit', 'warn')
                  : (best && r.j === best.j ? chip('largest change', 'ok') : '')));
          return tr([rowhead(r.name), td(Rtext(r.reduced)),
                     td(r.eligible ? Rtext(r.rate) : ''),
                     td(r.eligible && r.step ? Rtext(r.step) : ''),
                     td(r.eligible && r.delta ? Rtext(r.delta) : ''),
                     td(note)], cls);
        }));
    }

    var runs = spxRuleTable(model, 60);
    var fewest = runs[0];
    runs.forEach(function (r) { if (r.pivots < fewest.pivots) fewest = r; });
    rulesOut.innerHTML = table('The same programme under all four entering rules',
      ['rule', 'pivots', 'ends', 'optimum'],
      runs.map(function (r) {
        return tr([tdl(spxRuleLabel(r.rule)), td(String(r.pivots)), td(r.status),
                   td(r.status === 'optimal' ? Rtext(r.z) : '')],
                  r.rule === rule ? 'focus' : '');
      }));

    var same = runs.every(function (r) {
      return r.status !== 'optimal' || Requ(r.z, runs[0].z);
    });
    status.innerHTML = 'Under ' + spxRuleLabel(rule) + ' this takes <strong>'
      + (sol.run ? sol.run.pivots : 0) + '</strong> '
      + plural(sol.run ? sol.run.pivots : 0, 'pivot', 'pivots') + ' and stops at <strong>'
      + (sol.status === 'optimal' ? Rtext(sol.zOrig) : sol.status) + '</strong>. The fewest any rule '
      + 'takes here is <strong>' + fewest.pivots + '</strong>, under ' + spxRuleLabel(fewest.rule)
      + '. ' + (same ? 'Every rule that finished reached the same optimum, by a different route: the '
                     + 'rule chooses the path, never the answer. '
                     : '')
      + (allOk
          ? 'At every pivot above, rate times step is <strong>exactly</strong> the change in z &mdash; '
            + 'compared as fractions, not as decimals that happen to agree to six places.'
          : '<span class="tone-red">A pivot above has rate times step different from the change in z, '
            + 'which should be impossible.</span>')
      + ' That product is why the steepest column is not the best one: the reduced cost is a rate per '
      + 'unit, and a column with a large rate and a step of nothing moves the objective by nothing.';
  }

  [caseS, ruleS].forEach(function (el) { el.addEventListener('change', redraw); });
  stepS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Reduced costs, and the rule that reads them",
        subtitle="A reduced cost is a rate per unit; the improvement is that rate times the step the ratio test allows",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Switch the entering rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every candidate column carries its own rate, step and product, so the column a rule "
            "picks can be compared with the column that would have moved the objective most.",
        ),
        script=script,
    )


def _auto_signatures(cfg):
    markup = (
        _toolbar(
            "The three tableaux that refuse to finish",
            "an improving column with no positive entry, and a zero reduced cost off the basis",
            [("cyan", "the region"), ("green", "the optimal corner"),
             ("amber", "the second optimal corner, one pivot away"),
             ("red", "the ray, which never stops")],
        )
        + _stage(_svg("asPlot", "0 0 660 420",
                      "The feasible region, with either the ray the objective escapes along or the "
                      "two optimal corners and the edge between them."))
        + _holder("asSig")
        + _holder("asEval")
        + _banner("asStatus")
    )
    controls = (
        _select("asCase", "Worked example", _options(SIGNATURE_CASES), 0)
        + _range("asT", "One more point along the ray or the edge", 0, 100, 25)
        + _kpis([("What the tableau says", "asVerdict"), ("The signature column", "asCol"),
                 ("Objective at the corner", "asZ"), ("Region unbounded?", "asRegion")])
        + _hint(
            "asHint",
            "An unbounded region and an unbounded objective are two different claims. The first is "
            "about the shape of the set; the second is about one column of one tableau, and the "
            "third worked example has the first without the second.",
        )
    )

    script = _CORE_JS + "  var CASES = " + _js_literal([q["worked"] for q in SIGNATURE_CASES]) + ";\n" + r"""
  var caseS = document.getElementById('asCase'), tS = document.getElementById('asT');
  var plot = document.getElementById('asPlot'), sigOut = document.getElementById('asSig');
  var evalOut = document.getElementById('asEval'), status = document.getElementById('asStatus');

  function redraw() {
    var model = spxWorked(CASES[+caseS.value]);
    var sol = lpSolve(model, { rule: 'dantzig', maxPivots: 60 });
    var cons = spxRegionCons(model);
    var openRegion = Cunbounded(cons);
    document.getElementById('asRegion').textContent = openRegion ? 'yes, it runs on for ever' : 'no, it is closed';

    var tab = sol.run ? sol.run.tab : sol.tab;
    var here = stdPoint(sol.std, tabRead(tab).x);
    var marks = [{ x: here[0], y: here[1], cls: 'plot-point', label: spxPointText(here) }];
    var raw = +tS.value;

    if (sol.status === 'unbounded') {
      var ray = sol.ray, col = -1, j;
      for (j = 0; j < ray.length; j += 1) if (Requ(ray[j], R1) && tab.basis.indexOf(j) < 0) { col = j; break; }
      document.getElementById('asVerdict').textContent = 'unbounded: no row limits the column';
      document.getElementById('asCol').textContent = tab.names[col];
      document.getElementById('asZ').textContent = 'there is no optimum';
      document.getElementById('asTOut').textContent = 't = ' + raw;

      sigOut.innerHTML = table('Column ' + tab.names[col] + ', row by row: nothing stops it',
        ['row', 'basic there', 'entry', 'what it limits'],
        tabRatio(tab, col, 'dantzig').rows.map(function (row, i) {
          return tr([rowhead('R' + (i + 1)), td(tab.names[row.leaving]), td(Rtext(row.a)), tdl(row.why)]);
        }));

      var ts = [1, 10, 100, raw];
      evalOut.innerHTML = table('The ray x(t), evaluated exactly',
        ['t'].concat(model.names).concat(['objective', 'still feasible?']),
        ts.map(function (t, i) {
          var pt = spxRayPoint(tab, ray, t);
          var ok = spxViolations(model, pt.point[0], pt.point[1]).length === 0;
          return tr([rowhead('t = ' + t)]
            .concat(pt.point.map(function (v) { return td(Rtext(v)); }))
            .concat([td(Rtext(pt.z)), td(ok ? chip('yes', 'ok') : chip('no', 'no'))]),
            i === 3 ? 'focus' : '');
        }));
      var far = spxRayPoint(tab, ray, 100);
      marks.push({ x: far.point[0], y: far.point[1], cls: 'plot-hole', label: 'x(t), t large',
                   to: { x: here[0], y: here[1] }, lineClass: 'plot-asym' });
      spxDrawRegion(plot, model, marks, 'The region, and the ray along which the objective grows without end.');
      status.innerHTML = '<span class="tone-red">Nowhere to stop.</span> Column <strong>'
        + tab.names[col] + '</strong> improves the objective and no row has a positive entry in it, so '
        + 'the ratio test has nothing to return. The ray is read <em>straight off that column</em>: '
        + 'raise ' + tab.names[col] + ' by t and every basic variable changes by minus its entry times t. '
        + 'At t = 100 the point is ' + spxPointText(far.point) + ' with objective <strong>'
        + Rtext(far.z) + '</strong>, and it is still feasible, which is the proof. This is a statement '
        + 'about one column of one tableau, not about the shape of the region.';
      return;
    }

    var alt = spxAlternate(tab);
    document.getElementById('asZ').textContent = Rtext(sol.zOrig);
    if (alt.col >= 0) {
      var other = stdPoint(sol.std, tabRead(alt.tab).x);
      document.getElementById('asVerdict').textContent = 'optimal, and not uniquely so';
      document.getElementById('asCol').textContent = alt.name + ', reduced cost 0 and not basic';
      var s = [raw, 100];
      document.getElementById('asTOut').textContent = 's = ' + raw + '%';
      sigOut.innerHTML = table('Reduced costs at the optimal tableau',
        ['column', 'basic?', 'reduced cost', 'what it means'],
        tab.names.map(function (nm, j) {
          var basic = tab.basis.indexOf(j) >= 0;
          var why = basic ? 'basic, so its reduced cost is 0 by construction'
            : (Rzero(tab.z[j]) ? 'ZERO on a nonbasic column: bringing it in changes nothing'
               : 'positive, so bringing it in would lower the objective');
          return tr([rowhead(nm), td(basic ? chip('yes', 'ok') : ''), td(Rtext(tab.z[j])), tdl(why)],
                    (!basic && Rzero(tab.z[j])) ? 'focus' : '');
        }));
      evalOut.innerHTML = table('The objective along the segment between the two optimal corners',
        ['s'].concat(model.names).concat(['objective']),
        [[0, 1], [raw, 100], [1, 2], [1, 1]].map(function (frac, i) {
          var pt = spxSegment(here, other, frac);
          return tr([rowhead(Rtext(Rpair(frac)))]
            .concat(pt.map(function (v) { return td(Rtext(v)); }))
            .concat([td(Rtext(spxValue(model, pt)))]), i === 1 ? 'focus' : '');
        }));
      marks.push({ x: other[0], y: other[1], cls: 'plot-point', label: spxPointText(other),
                   to: { x: here[0], y: here[1] }, lineClass: 'plot-curve' });
      var mid = spxSegment(here, other, [raw, 100]);
      marks.push({ x: mid[0], y: mid[1], cls: 'plot-hole', label: '' });
      spxDrawRegion(plot, model, marks, 'The region with both optimal corners and the optimal edge between them.');
      status.innerHTML = '<span class="tone-amber">Optimal, and not only here.</span> Column <strong>'
        + alt.name + '</strong> is not in the basis and its reduced cost is <strong>0</strong>: bringing it '
        + 'in changes the basis without changing the objective. One pivot moves from '
        + spxPointText(here) + ' to <strong>' + spxPointText(other) + '</strong>, both at <strong>'
        + Rtext(sol.zOrig) + '</strong>, and every point of the segment between them is optimal too '
        + '&mdash; the table samples it and the value never moves. Note what this is NOT: a zero on a '
        + 'NONBASIC column is a second optimum; a zero on a BASIC one is degeneracy, and a different story.';
      return;
    }

    document.getElementById('asVerdict').textContent = 'optimal, and uniquely so';
    document.getElementById('asCol').textContent = 'there is none';
    document.getElementById('asTOut').textContent = 'no second corner to walk to';
    sigOut.innerHTML = table('Reduced costs at the optimal tableau',
      ['column', 'basic?', 'reduced cost', 'what it means'],
      tab.names.map(function (nm, j) {
        var basic = tab.basis.indexOf(j) >= 0;
        return tr([rowhead(nm), td(basic ? chip('yes', 'ok') : ''), td(Rtext(tab.z[j])),
                   tdl(basic ? 'basic, so its reduced cost is 0 by construction'
                        : 'strictly positive, so raising it would lower the objective')]);
      }));
    /* `Cgrows(cons, c, d)` asks whether cx + dy grows without bound on the
       region, so asking it about (1, 0) and (0, 1) asks which way the region
       itself runs on for ever, and asking it about the objective asks the
       other question. Two questions, one routine, and the answers differ. */
    var dirs = [['more ' + model.names[0], R1, R0],
                ['more ' + model.names[1], R0, R1],
                ['along the objective, ' + spxTerms(model.obj, model.names), model.obj[0], model.obj[1]]];
    evalOut.innerHTML = table('Which way the region runs on for ever, and what the objective does there',
      ['direction', 'does the region run on for ever this way?', 'and the objective'],
      dirs.map(function (d, i) {
        var open = Cgrows(cons, d[1], d[2]);
        return tr([tdl(d[0]),
                   td(open ? chip('yes, without end', 'warn') : chip('no, it is capped', 'ok')),
                   tdl(i < 2
                       ? 'changes by ' + Rtext(model.obj[i]) + ' per unit in this direction'
                       : (open ? 'so it has no maximum'
                          : 'no direction the region runs on for ever in raises it, so it has one'))],
                  i === 2 ? 'focus' : '');
      }));
    spxDrawRegion(plot, model, marks, 'An unbounded region on which the objective is nevertheless bounded.');
    status.innerHTML = 'This region <strong>' + (openRegion ? 'does' : 'does not')
      + '</strong> run on for ever, and the objective is bounded anyway: the optimum is <strong>'
      + Rtext(sol.zOrig) + '</strong> at ' + spxPointText(here) + '. Every nonbasic reduced cost is '
      + 'strictly positive, so there is no improving column at all &mdash; not one without a positive '
      + 'entry, and not one with a zero reduced cost. Unboundedness of the objective is a property of a '
      + 'COLUMN; unboundedness of the region is a property of the SET; and this programme has the second '
      + 'without the first.';
  }

  caseS.addEventListener('change', redraw);
  tS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Unbounded, and optimal more than once",
        subtitle="The ray read off a column with no positive entry, and the edge every point of which is optimal",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick the awkward tableau"),
        panel_intro=cfg.get(
            "panel_intro",
            "The ray is produced from the tableau, not from the picture, and then checked against "
            "the constraints at t = 1, 10 and 100.",
        ),
        script=script,
    )


def _auto_kleeminty(cfg):
    markup = (
        _toolbar(
            "The cube that costs two to the n",
            "a squashed n-cube whose every vertex Dantzig's rule visits, counted here rather than quoted",
            [("cyan", "the measured pivot count"), ("green", "the bound two to the n minus one"),
             ("amber", "another rule, fewer pivots"), ("red", "the count that does not survive rounding")],
        )
        + _stage('<div id="akCounts"></div>')
        + _holder("akPath")
        + _holder("akCorners")
        + _banner("akStatus")
    )
    controls = (
        _select("akObj", "The objective", [("0", "the cube: coefficients 10^(n-j)"),
                                           ("1", "the same region, coefficients reversed")], "0")
        + _range("akN", "Dimensions n", 2, 4, 3)
        + _select("akRule", "Entering rule",
                  [("dantzig", "Dantzig: most negative reduced cost"),
                   ("bland", "Bland: smallest index"),
                   ("bestImprovement", "greatest improvement: largest rate times step"),
                   ("lastIndex", "largest index")], "dantzig")
        + _kpis([("Pivots taken", "akPivots"), ("Two to the n minus one", "akBound"),
                 ("Vertices of the cube", "akVerts"), ("Optimum", "akZ")])
        + _hint(
            "akHint",
            "The control stops at four dimensions on purpose: n = 5 is 31 pivots against 15, and the "
            "point of the example is the doubling, which is already plain at 15.",
        )
    )

    script = _CORE_JS + r"""
  var objS = document.getElementById('akObj'), nS = document.getElementById('akN');
  var ruleS = document.getElementById('akRule');
  var countsOut = document.getElementById('akCounts'), pathOut = document.getElementById('akPath');
  var cornersOut = document.getElementById('akCorners'), status = document.getElementById('akStatus');

  function redraw() {
    var n = Math.max(2, Math.min(4, +nS.value)), rule = ruleS.value, reversed = objS.value === '1';
    document.getElementById('akNOut').textContent = n + ' dimensions, ' + Math.pow(2, n) + ' vertices';
    var model = kleeMinty(n, reversed);
    var sol = lpSolve(model, { rule: rule, maxPivots: 400 });

    document.getElementById('akPivots').textContent = sol.run.pivots;
    document.getElementById('akBound').textContent = spxCubeBound(n);
    document.getElementById('akVerts').textContent = Math.pow(2, n);
    document.getElementById('akZ').textContent = Rtext(sol.zOrig);

    var ns = [2, 3, 4];
    countsOut.innerHTML = table(
      reversed ? 'The same region, the objective reversed: pivots actually taken'
               : 'Pivots actually taken, against the bound 2^n - 1',
      ['n', 'vertices 2^n', 'bound 2^n - 1'].concat(spxRules().map(spxRuleLabel)),
      ns.map(function (m) {
        var runs = spxRuleTable(kleeMinty(m, reversed), 400);
        return tr([rowhead('n = ' + m), td(String(Math.pow(2, m))), td(String(spxCubeBound(m)))]
          .concat(runs.map(function (r) {
            var hit = !reversed && r.rule === 'dantzig' && r.pivots === spxCubeBound(m);
            return td(String(r.pivots) + (hit ? ' ' + chip('exactly the bound', 'ok') : ''),
                      (r.rule === rule && m === n) ? 'on' : '');
          })), m === n ? 'focus' : '');
      }));

    pathOut.innerHTML = table('Every pivot at n = ' + n + ' under ' + spxRuleLabel(rule),
      ['pivot', 'in', 'out', 'objective after'],
      sol.run.steps.map(function (s, i) {
        return tr([rowhead(String(i + 1)), td(s.enterName), td(s.leaveName),
                   td(Rshort(sol.std.maximised ? s.zAfter : Rneg(s.zAfter), 4))]);
      }));

    var visited = {}, count = 0;
    sol.run.path.forEach(function (t) {
      var key = stdPoint(t.std, tabRead(t).x).map(Rtext).join(',');
      if (!visited[key]) { visited[key] = true; count += 1; }
    });
    cornersOut.innerHTML = table('The corner the method stands at, pivot by pivot',
      ['after pivot'].concat(model.names).concat(['objective']),
      sol.run.path.map(function (t, i) {
        var pt = stdPoint(t.std, tabRead(t).x), rd = tabRead(t);
        return tr([rowhead(i === 0 ? 'start' : String(i))]
          .concat(pt.map(function (v) { return td(Rshort(v, 3)); }))
          .concat([td(Rshort(rd.zOrig, 3))]), i === sol.run.path.length - 1 ? 'focus' : '');
      }));

    var dantzig = spxRun(model, 'dantzig', 400), bland = spxRun(model, 'bland', 400);
    var best = spxRun(model, 'bestImprovement', 400);
    status.innerHTML = (reversed
        ? 'Same region, same optimal vertex, objective coefficients turned round. Dantzig now takes <strong>'
          + dantzig.pivots + '</strong> ' + plural(dantzig.pivots, 'pivot', 'pivots')
          + ' where the cube ordering cost it ' + spxRun(kleeMinty(n, false), 'dantzig', 400).pivots
          + '. Bland still takes <strong>' + bland.pivots + '</strong>, because Bland never looks at a '
          + 'coefficient. The pivot count is a property of the rule and the objective together &mdash; '
          + 'never of the region on its own. '
        : 'At n = ' + n + ' this visited <strong>' + count + '</strong> of the <strong>'
          + Math.pow(2, n) + '</strong> vertices in <strong>' + dantzig.pivots + '</strong> pivots under '
          + 'Dantzig, and 2^n - 1 is <strong>' + spxCubeBound(n) + '</strong>. Bland takes <strong>'
          + bland.pivots + '</strong> and greatest improvement takes <strong>' + best.pivots
          + '</strong>: run another rule and count fewer. ')
      + 'Three statements, all true, none implying another: the method is <em>finite</em> because '
      + "Bland's rule cannot repeat a basis; it is <em>exponential in the worst case</em> because this "
      + 'cube exists; and it is <em>fast in practice</em> because problems like this one are constructed '
      + 'rather than met. <span class="tone-red">None of these counts survives rounding.</span> The '
      + 'coefficients here run from 1 to 10^' + (n - 1) + ' and the comparisons that pick the entering '
      + 'column have to land exactly; in floating point one of them lands the other way and the count '
      + 'collapses, taking the example with it.';
  }

  [objS, ruleS].forEach(function (el) { el.addEventListener('change', redraw); });
  nS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Termination, and the cube that makes it expensive",
        subtitle="Finite is not fast: the pivot count measured against two to the n minus one, under four rules",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Raise the dimension"),
        panel_intro=cfg.get(
            "panel_intro",
            "Nothing here is a quoted figure. Each count is a run of the method on the cube built "
            "in your browser, under the rule you chose.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 - phase1: artificials minimised, or infeasibility certified
# ---------------------------------------------------------------------------
#
# The misconception is that an artificial variable is a slack with a different
# name. A slack MEASURES something -- `stdForm` writes the sentence for each
# one -- and may be positive at the optimum. An artificial measures nothing,
# exists only to fill a column, and a positive one at the end of Phase I is
# not a solution but a PROOF that there is none. `farkasCertificate` turns
# that proof into arithmetic a reader can check row by row.

PHASE_PRESETS = [
    {"key": "mixed", "label": "two requirements and a cap: Phase I hands over a basis",
     "worked": "demandcap"},
    {"key": "empty", "label": "an empty region, proved empty by a number", "worked": "emptyregion"},
    {"key": "redundant", "label": "a repeated row, and an artificial left at zero",
     "worked": "repeatedrow"},
]


def _phase1(cfg):
    idx = _preset_index(cfg, PHASE_PRESETS, "phase1")

    markup = (
        _toolbar(
            "Phase I: manufacture a start, or prove there is none",
            "minimise the sum of the artificials; zero hands over a basis, positive is a certificate",
            [("cyan", "the artificial columns"), ("green", "an artificial driven to zero"),
             ("amber", "an artificial left basic at zero"), ("red", "an artificial that cannot reach zero")],
        )
        + _stage('<div id="p1Tab"></div>')
        + _holder("p1Steps")
        + _holder("p1After")
        + _banner("p1Status")
    )
    controls = (
        _select("p1Preset", "Worked example", _options(PHASE_PRESETS), idx)
        + _range("p1Step", "Show the Phase I tableau after pivot", 0, 8, 0)
        + _kpis([("Phase I optimum", "p1Value"), ("Is there a feasible point?", "p1Feasible"),
                 ("Artificials still basic", "p1Arts"), ("Phase II optimum", "p1Z")])
        + _hint(
            "p1Hint",
            "The Phase I objective is the sum of the artificials and it is minimised, so its optimum "
            "is never negative. Zero means the original constraints have a common solution. Anything "
            "above zero means they do not, and the number itself is the proof.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal([q["worked"] for q in PHASE_PRESETS]) + ";\n" + r"""
  var preset = document.getElementById('p1Preset'), stepS = document.getElementById('p1Step');
  var tabOut = document.getElementById('p1Tab'), stepsOut = document.getElementById('p1Steps');
  var afterOut = document.getElementById('p1After'), status = document.getElementById('p1Status');

  function redraw() {
    var model = spxWorked(PRESETS[+preset.value]), std = stdForm(model);
    var ph = phaseOne(std, {});
    var path = ph.run ? ph.run.path : [tabInit(std)];
    var at = Math.max(0, Math.min(path.length - 1, +stepS.value));
    document.getElementById('p1StepOut').textContent = at === 0 ? 'the starting tableau'
      : at + ' of ' + (path.length - 1);

    var cur = path[at];
    tabOut.innerHTML = spxTableauHtml(
      at === 0 ? 'The Phase I tableau: cost 1 on every artificial, 0 on everything else'
               : 'Phase I after ' + at + ' ' + plural(at, 'pivot', 'pivots'),
      cur, { mark: function (i2, j2) { return j2 < std.n && std.kinds[j2] === 'artificial'; } });

    document.getElementById('p1Value').textContent = Rtext(ph.value);
    document.getElementById('p1Feasible').textContent = ph.feasible ? 'yes' : 'no, and this proves it';
    document.getElementById('p1Arts').textContent = ph.artificialsAtZero.length
      ? ph.artificialsAtZero.map(function (a) { return a.name; }).join(', ') + ' (at zero)'
      : 'none';

    stepsOut.innerHTML = table('What each column is, and what it measures',
      ['column', 'kind', 'what it measures'],
      std.names.map(function (nm, j) {
        return tr([rowhead(nm), td(chip(std.kinds[j], std.kinds[j] === 'artificial' ? 'no' : 'ok')),
                   tdl(std.sentences[j])], std.kinds[j] === 'artificial' ? 'focus' : '');
      }))
      + table('The sum of the artificials after every Phase I pivot',
        ['pivot', 'in', 'out', 'sum of the artificials'].concat(ph.artificials
          ? ph.artificials.map(function (j) { return std.names[j]; }) : []),
        path.map(function (t, i) {
          var st = i === 0 ? null : ph.run.steps[i - 1];
          var rd = tabRead(t);
          return tr([rowhead(i === 0 ? 'start' : String(i)),
                     td(st ? st.enterName : ''), td(st ? st.leaveName : ''),
                     td(Rtext(Rneg(t.z[t.n])))]
            .concat((ph.artificials || []).map(function (j) { return td(Rtext(rd.x[j])); })),
            i === at ? 'focus' : '');
        }));

    if (!ph.feasible) {
      var cert = farkasCertificate(ph.T);
      document.getElementById('p1Z').textContent = 'there is no feasible point to optimise over';
      afterOut.innerHTML = table('The certificate y, checked one line at a time',
        ['what is checked', 'the arithmetic', 'holds?'],
        cert.checks.columns.map(function (c) {
          return tr([rowhead('column ' + c.name), tdl(c.text), td(c.ok ? chip('yes', 'ok') : chip('no', 'no'))]);
        }).concat([tr([rowhead('y . b &gt; 0'), tdl(cert.checks.b.text),
                       td(cert.checks.b.ok ? chip('yes', 'ok') : chip('no', 'no'))], 'focus')]));
      status.innerHTML = '<span class="tone-red">There is no point that satisfies every constraint at once.</span> '
        + 'Phase I minimised the sum of the artificials and could not get below <strong>'
        + Rtext(ph.value) + '</strong>. That number is not evidence of a failed search; it is a proof, '
        + 'and the proof is written out above: with y = (' + cert.y.map(Rtext).join(', ')
        + '), every column of A has y . a &lt;= 0 while y . b = <strong>'
        + Rtext(cert.checks.b.value) + ' &gt; 0</strong>. Any x satisfying the constraints would make '
        + 'y . (Ax) both at most 0 and at least y . b, so no such x exists. Compare this with the blank '
        + 'picture the two-variable course drew for the same region: the picture showed nothing, and '
        + 'showing nothing is not the same sentence as there being nothing.';
      return;
    }

    var sol = lpSolve(model, {});
    document.getElementById('p1Z').textContent = sol.status === 'optimal' ? Rtext(sol.zOrig) : sol.status;
    var two = phaseTwo(std, ph);
    afterOut.innerHTML = spxTableauHtml(
      'The tableau handed to Phase II: the real objective restored, the artificial columns locked out',
      two, { mark: function (i2, j2) { return j2 < std.n && std.kinds[j2] === 'artificial'; } })
      + table('Phase II, from that basis',
        ['pivot', 'in', 'out', 'objective after'],
        (sol.run ? sol.run.steps : []).map(function (s, i) {
          return tr([rowhead(String(i + 1)), td(s.enterName), td(s.leaveName),
                     td(Rtext(std.maximised ? s.zAfter : Rneg(s.zAfter)))]);
        }));

    var stayed = ph.artificialsAtZero.length, red = ph.redundant.length;
    status.innerHTML = 'Phase I drove the artificials to <strong>' + Rtext(ph.value)
      + '</strong> in ' + (ph.run ? ph.run.pivots : 0) + ' '
      + plural(ph.run ? ph.run.pivots : 0, 'pivot', 'pivots')
      + ', so the original constraints do have a common solution and the basis it ended on is a genuine '
      + 'basic feasible solution of the real problem. Phase II then reached <strong>'
      + (sol.status === 'optimal' ? Rtext(sol.zOrig) : sol.status) + '</strong> at '
      + spxPointText(sol.x || []) + '. '
      + (stayed
          ? '<span class="tone-amber">An artificial stayed basic at zero</span> ('
            + ph.artificialsAtZero.map(function (a) { return a.name; }).join(', ')
            + '), which is not an error: it is a degenerate basic feasible solution, and the column is '
            + 'swapped out for a real one where a real one exists. '
            + (red ? 'For row ' + ph.redundant.map(function (r) { return r + 1; }).join(', ')
                     + ' none does, and that is the honest finding: the row is a combination of the '
                     + 'others and carries no information the others do not already carry. '
                   : '')
          : 'Every artificial left the basis, so nothing had to be swapped out. ')
      + 'Note what an artificial is not. A slack measures something real and may be positive at the end; '
      + 'an artificial measures nothing at all, and a positive one here would have been a proof rather '
      + 'than a solution.';
  }

  preset.addEventListener('change', redraw);
  stepS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Artificial variables, and the number that proves there is no solution",
        subtitle="Minimise the sum of the artificials: zero hands a basis to the real problem, positive is a certificate",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Run Phase I"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every column says what it measures, so the difference between a slack and an artificial "
            "is on the page rather than in the vocabulary.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 - degenerate: Beale's cycle, Bland's escape, and a zero-length pivot
# ---------------------------------------------------------------------------
#
# EXACTNESS IS THE LESSON HERE, NOT THE STYLE. "The sixth tableau equals the
# first" is a claim about equality of numbers: `spxTabEqual` compares 4 x 8
# rationals and an objective row, entry for entry, with no tolerance anywhere.
# In floating point the entries would come back nearly equal and the claim
# would be a story about what nearly means. The measured figures, which
# scripts/mathcheck.js pins: Dantzig cycles in 6 pivots with z = 0 at all
# seven tableaux; Bland terminates in 6 at z* = 1/20.
#
# The second preset is the other half of the lesson and the one that is easy
# to see: three lines through one corner in two variables, a tie in the ratio
# test, and then a pivot of length zero that changes the basis without moving
# the point at all.

DEGENERATE_PRESETS = [
    {"key": "beale", "label": "Beale's example, which returns to where it started",
     "worked": None, "rule": "dantzig"},
    {"key": "concurrent", "label": "three lines through one corner, and a pivot of length zero",
     "worked": "concurrent", "rule": "dantzig"},
]


def _degenerate(cfg):
    idx = _preset_index(cfg, DEGENERATE_PRESETS, "degenerate")

    markup = (
        _toolbar(
            "Degeneracy, cycling, and the rule that ends it",
            "a tie in the ratio test leaves a basic variable at zero, and the next pivot can move nothing",
            [("cyan", "a pivot that moves the point"), ("amber", "a pivot of length zero"),
             ("red", "a basis seen before"), ("green", "the basis the rule stops on")],
        )
        + _stage('<div id="dgTab"></div>')
        + '      <div class="lab-stage" id="dgPlotWrap" style="margin-top:12px;">'
        + _svg("dgPlot", "0 0 660 420",
               "The two-variable region, with the three boundary lines that pass through one corner.")
        + "</div>\n"
        + _holder("dgSteps")
        + _holder("dgCompare")
        + _banner("dgStatus")
    )
    controls = (
        _select("dgPreset", "Worked example", _options(DEGENERATE_PRESETS), idx)
        + _select("dgRule", "Entering rule",
                  [("dantzig", "Dantzig: most negative reduced cost"),
                   ("bland", "Bland: smallest index"),
                   ("bestImprovement", "greatest improvement: largest rate times step"),
                   ("lastIndex", "largest index")], DEGENERATE_PRESETS[idx]["rule"])
        + _range("dgStep", "Show the tableau after pivot", 0, 8, 0)
        + _kpis([("How it ends", "dgEnds"), ("Pivots", "dgPivots"),
                 ("Pivots that moved nothing", "dgStuck"), ("Objective at the end", "dgZ")])
        + _hint(
            "dgHint",
            "Degeneracy is geometry, not arithmetic error: it is more constraint boundaries through a "
            "corner than the corner has dimensions. Every number on this page is an exact fraction, and "
            "the cycle is still there.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal(DEGENERATE_PRESETS) + ";\n" + r"""
  var preset = document.getElementById('dgPreset'), ruleS = document.getElementById('dgRule');
  var stepS = document.getElementById('dgStep');
  var tabOut = document.getElementById('dgTab'), plotWrap = document.getElementById('dgPlotWrap');
  var plot = document.getElementById('dgPlot'), stepsOut = document.getElementById('dgSteps');
  var cmpOut = document.getElementById('dgCompare'), status = document.getElementById('dgStatus');
  var lastPreset = preset.value;

  function redraw() {
    var p = PRESETS[+preset.value];
    if (preset.value !== lastPreset) { lastPreset = preset.value; ruleS.value = p.rule; }
    var model = p.worked ? spxWorked(p.worked) : bealeModel();
    var rule = ruleS.value;
    var sol = lpSolve(model, { rule: rule, maxPivots: 60 });
    var path = sol.run.path, steps_ = sol.run.steps;
    var at = Math.max(0, Math.min(path.length - 1, +stepS.value));
    document.getElementById('dgStepOut').textContent = at === 0 ? 'the starting tableau'
      : at + ' of ' + steps_.length;

    var cur = path[at];
    tabOut.innerHTML = spxTableauHtml(
      (at === 0 ? 'The starting tableau' : 'After pivot ' + at) + ':  ' + spxBasisText(cur)
        + ',  z = ' + Rtext(tabRead(cur).zOrig),
      cur, { mark: function (i2, j2) { return i2 < cur.m && j2 === cur.n && Rzero(cur.T[i2][j2]); } });

    var stuck = steps_.filter(function (s) { return Rzero(s.delta); }).length;
    document.getElementById('dgEnds').textContent = sol.status;
    document.getElementById('dgPivots').textContent = steps_.length;
    document.getElementById('dgStuck').textContent = stuck;
    document.getElementById('dgZ').textContent = sol.status === 'cycled'
      ? Rtext(tabRead(sol.run.tab).zOrig) + ' (and never moved)' : Rtext(sol.zOrig);

    var seen = {};
    stepsOut.innerHTML = table('Every pivot, with the basis it produced',
      ['pivot', 'in', 'out', 'from row', 'step length', 'change in z', 'basis after', 'seen before?'],
      steps_.map(function (s, i) {
        var key = basisKey(sol.run.bases[i + 1]);
        var before = seen[key] !== undefined;
        if (!before) seen[key] = i + 1;
        var len = s.rates[s.enter].step;
        return tr([rowhead(String(i + 1)), td(s.enterName), td(s.leaveName),
                   td('R' + (s.row + 1)),
                   td(Rtext(len) + (Rzero(len) ? ' ' + chip('moves nothing', 'warn') : '')),
                   td(Rtext(s.delta)),
                   tdl('{' + sol.run.bases[i + 1].map(function (j) { return sol.tab.names[j]; }).join(', ') + '}'),
                   td(before ? chip('yes, at pivot ' + seen[key], 'no') : '')],
                  Rzero(s.delta) ? 'focus' : '');
      }));

    if (p.worked) {
      plotWrap.hidden = false;
      var marks = [];
      path.forEach(function (t, i) {
        var pt = stdPoint(t.std, tabRead(t).x);
        marks.push({ x: pt[0], y: pt[1], cls: i === path.length - 1 ? 'plot-point' : 'plot-hole',
                     label: i === 0 ? 'start' : (i === path.length - 1 ? spxPointText(pt) : '') });
      });
      spxDrawRegion(plot, model, marks,
        'The region, with the corner where three boundary lines meet and the points the method stands at.');
    } else {
      plotWrap.hidden = true;
    }

    var first = path[0], last = path[path.length - 1];
    var same = spxTabEqual(first, last);
    if (sol.status === 'cycled') {
      cmpOut.innerHTML = table('The first tableau against the last, entry for entry',
        ['what was compared', 'entries', 'all equal?'],
        [tr([rowhead('the basis'), tdl(spxBasisText(first) + ' against ' + spxBasisText(last)),
             td(chip('same set', 'ok'))]),
         tr([rowhead('the body'), tdl(first.m + ' rows of ' + (first.n + 1) + ' fractions'),
             td(same.equal ? chip('identical', 'ok') : chip(same.diffs.length + ' differ', 'no'))]),
         tr([rowhead('the objective row'), tdl((first.n + 1) + ' fractions'),
             td(same.equal ? chip('identical', 'ok') : chip('differ', 'no'))])], 'focus');
    } else {
      cmpOut.innerHTML = table('Where the rule stopped',
        ['column', 'basic?', 'reduced cost', 'value'],
        sol.tab.names.map(function (nm, j) {
          var basic = sol.tab.basis.indexOf(j) >= 0;
          var rd = tabRead(sol.tab);
          return tr([rowhead(nm), td(basic ? chip('yes', 'ok') : ''), td(Rtext(sol.tab.z[j])),
                     td(Rtext(rd.x[j]))],
                    basic && Rzero(rd.x[j]) ? 'focus' : '');
        }));
    }

    var other = spxRun(model, rule === 'bland' ? 'dantzig' : 'bland', 60);
    if (sol.status === 'cycled') {
      status.innerHTML = '<span class="tone-red">It came back to where it started.</span> After <strong>'
        + steps_.length + '</strong> pivots the basis is the one it began with, the objective sat at '
        + '<strong>' + Rtext(tabRead(last).zOrig) + '</strong> the whole way, and the tableau is '
        + (same.equal ? '<strong>identical entry for entry</strong>' : 'NOT identical, which should be impossible')
        + ' &mdash; every one of the ' + (first.m * (first.n + 1) + first.n + 1)
        + ' fractions compared as a fraction, not as a decimal that happens to agree. '
        + 'This is why the arithmetic here is exact: in floating point the entries would come back '
        + 'nearly equal, and "nearly" is a different claim from the one the example makes. '
        + 'Switch the rule to Bland and it stops in ' + other.pivots + ' at z* = ' + Rtext(other.z)
        + ' &mdash; the same count, a different ending, and that contrast is the whole lesson.';
    } else {
      status.innerHTML = 'Under ' + spxRuleLabel(rule) + ' this stops after <strong>' + steps_.length
        + '</strong> ' + plural(steps_.length, 'pivot', 'pivots') + ' at <strong>' + Rtext(sol.zOrig)
        + '</strong>. ' + (stuck
            ? '<span class="tone-amber">' + stuck + ' of them moved the point nowhere at all.</span> A tie '
              + 'in the ratio test leaves a basic variable at zero, and the next pivot then exchanges a '
              + 'column while the point stays exactly where it was: the basis changed, the objective did '
              + 'not. An objective that stops changing is not the same thing as being finished. '
            : 'No pivot here had length zero. ')
        + 'Bland’s rule is what makes the method provably terminate: there are finitely many bases, '
        + 'and under the smallest-index rule none can repeat. The other rule on offer takes '
        + other.pivots + ' ' + plural(other.pivots, 'pivot', 'pivots') + ' and ends '
        + other.status + '.';
    }
  }

  [preset, ruleS].forEach(function (el) { el.addEventListener('change', redraw); });
  stepS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Degeneracy, cycling, and Bland's rule",
        subtitle="A tie in the ratio test, a pivot that moves nothing, and a tableau that comes back identical",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Change the rule and watch the ending change"),
        panel_intro=cfg.get(
            "panel_intro",
            "The comparison of the first tableau with the last is done entry for entry on exact "
            "fractions, because that is the only way the claim can be made at all.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 - matrix: B, B inverse, and the three products
# ---------------------------------------------------------------------------
#
# The misconception is that the slack columns always hold B^-1. They hold it
# when the starting basis was an identity IN THOSE COLUMNS, which is true
# after a <=-only setup and false the moment a >= or an = row appears: a
# surplus column is -1, not +1, and the identity column beside it is the
# ARTIFICIAL. So the default preset here has a >= row, and the page names the
# columns it actually read B^-1 out of and what kind each one is. A lab that
# only ever showed the <=-only case could not correct this.

MATRIX_PRESETS = [
    {"key": "gerow", "label": "a requirement row: the identity is not in the slacks",
     "worked": "contract"},
    {"key": "equality", "label": "a blend that must balance exactly", "worked": "blend"},
    {"key": "slacks", "label": "only caps, where the slogan happens to be true",
     "worked": "plants"},
]


def _matrix(cfg):
    idx = _preset_index(cfg, MATRIX_PRESETS, "matrix")

    markup = (
        _toolbar(
            "Every tableau is B inverse times the original data",
            "extract B from the basis, invert it, and rebuild the tableau by multiplication",
            [("cyan", "the tableau on screen"), ("green", "rebuilt from the original A and b"),
             ("amber", "the columns that started as the identity"),
             ("red", "the slack columns, which are not always those")],
        )
        + _stage('<div id="mxTab"></div>')
        + _holder("mxWhere")
        + _holder("mxTrace")
        + _holder("mxProd")
        + _banner("mxStatus")
    )
    controls = (
        _select("mxPreset", "Worked example", _options(MATRIX_PRESETS), idx)
        + _range("mxPivot", "Rebuild the tableau after pivot", 0, 8, 0)
        + _select("mxShow", "Show",
                  [("0", "B inverse times A, against the tableau body"),
                   ("1", "B inverse times b, against the right-hand column"),
                   ("2", "the objective row from c_B, B inverse and A")], "0")
        + _kpis([("Basis", "mxBasis"), ("Columns holding B inverse", "mxCols"),
                 ("Rebuilt entries checked", "mxChecked"), ("Any disagreement?", "mxAgree")])
        + _hint(
            "mxHint",
            "The rule is the columns that started as the identity, never the slack columns. On a "
            "requirement row the slack is a surplus and its column is minus one; the identity column "
            "beside it is the artificial, and that is where B inverse is.",
        )
    )

    script = _CORE_JS + "  var PRESETS = " + _js_literal([q["worked"] for q in MATRIX_PRESETS]) + ";\n" + r"""
  var preset = document.getElementById('mxPreset'), pivotS = document.getElementById('mxPivot');
  var showS = document.getElementById('mxShow');
  var tabOut = document.getElementById('mxTab'), whereOut = document.getElementById('mxWhere');
  var traceOut = document.getElementById('mxTrace'), prodOut = document.getElementById('mxProd');
  var status = document.getElementById('mxStatus');

  function redraw() {
    var model = spxWorked(PRESETS[+preset.value]), std = stdForm(model);
    var sol = lpSolve(model, { rule: 'dantzig', maxPivots: 60 });
    var path = sol.run ? sol.run.path : [sol.tab];
    var at = Math.max(0, Math.min(path.length - 1, +pivotS.value));
    var tab = path[at];
    document.getElementById('mxPivotOut').textContent = at === 0
      ? 'the first Phase II tableau' : at + ' of ' + (path.length - 1);

    var bi = basisInverse(tab);
    document.getElementById('mxBasis').textContent = spxBasisText(tab);

    var cols = std.identity.map(function (c, i) {
      return { row: i, col: c, name: std.names[c], kind: std.kinds[c] };
    });
    document.getElementById('mxCols').textContent = cols.map(function (c) { return c.name; }).join(', ');
    var allSlack = cols.every(function (c) { return c.kind === 'slack'; });

    var when = at === 0 ? 'the first tableau of the real objective'
      : 'after ' + at + ' ' + plural(at, 'pivot', 'pivots');
    tabOut.innerHTML = spxTableauHtml('The tableau on screen, ' + when, tab, {});

    whereOut.innerHTML = table('Which columns started as the identity, and what kind each one is',
      ['row', 'identity column', 'kind', 'is it the slack of that row?'],
      cols.map(function (c) {
        var slackCol = std.rowSlack[c.row];
        var isSlack = slackCol === c.col;
        return tr([rowhead('R' + (c.row + 1)), td(c.name), td(chip(c.kind, isSlack ? 'ok' : 'no')),
                   tdl(isSlack ? 'yes, this row is a cap and its slack column is +1'
                        : (slackCol < 0
                            ? 'this row has no slack at all: it is an equality, and the identity column is its artificial ' + c.name
                            : 'NO. The slack of this row is ' + std.names[slackCol] + ', whose column is '
                              + Rtext(std.A[c.row][slackCol]) + '. The identity column is ' + c.name))],
                  isSlack ? '' : 'focus');
      }));

    if (bi.singular) {
      traceOut.innerHTML = '';
      prodOut.innerHTML = '';
      document.getElementById('mxChecked').textContent = '0';
      document.getElementById('mxAgree').textContent = 'B is singular';
      status.innerHTML = '<span class="tone-red">Those columns are not a basis.</span> B has no inverse, '
        + 'so there is nothing to rebuild.';
      return;
    }

    var mheads = [];
    for (var q = 0; q < std.m; q += 1) mheads.push('B col ' + (q + 1));
    for (q = 0; q < std.m; q += 1) mheads.push('I col ' + (q + 1));
    traceOut.innerHTML = Mtable('B: the columns of the ORIGINAL A belonging to '
        + spxBasisText(tab), bi.B, { heads: bi.columns.map(function (c) { return c.name; }) })
      + Mtrace('Reducing [ B | I ] to [ I | B inverse ]', Maug(bi.B, Mid(std.m)), bi.ops,
               { heads: mheads, split: std.m });

    var mode = +showS.value, checked = 0, wrong = 0, body;
    if (mode === 1) {
      body = table('B inverse times b, against the right-hand column of the tableau',
        ['row', 'rebuilt from the original b', 'on the tableau', 'same?'],
        bi.Binvb.map(function (row, i) {
          var got = row[0], want = tab.T[i][tab.n];
          checked += 1; if (!Requ(got, want)) wrong += 1;
          return tr([rowhead(tab.names[tab.basis[i]]), td(Rtext(got)), td(Rtext(want)),
                     td(Requ(got, want) ? chip('yes', 'ok') : chip('no', 'no'))]);
        }));
    } else if (mode === 2) {
      body = table('c_B times B inverse times A, minus c, against the objective row',
        ['column', 'rebuilt', 'on the tableau', 'same?'],
        bi.zrow.map(function (got, j) {
          var want = tab.z[j];
          checked += 1; if (!Requ(got, want)) wrong += 1;
          return tr([rowhead(tab.names[j]), td(Rtext(got)), td(Rtext(want)),
                     td(Requ(got, want) ? chip('yes', 'ok') : chip('no', 'no'))]);
        }));
    } else {
      var rows = [];
      for (var i = 0; i < std.m; i += 1) {
        var cells = [rowhead(tab.names[tab.basis[i]])];
        for (var j = 0; j < std.n; j += 1) {
          var got = bi.BinvA[i][j], want = tab.T[i][j];
          checked += 1;
          var ok = Requ(got, want);
          if (!ok) wrong += 1;
          cells.push(td(Rtext(got), ok ? '' : 'no'));
        }
        rows.push(tr(cells));
      }
      body = table('B inverse times A, entry for entry &mdash; compare it with the tableau body above',
        [''].concat(std.names), rows);
    }
    prodOut.innerHTML = Mtable('B inverse', bi.Binv, {}) + body;

    document.getElementById('mxChecked').textContent = checked;
    document.getElementById('mxAgree').textContent = wrong ? wrong + ' entries differ' : 'none';

    status.innerHTML = 'This is the tableau ' + when
      + ', and every entry of it was just rebuilt from the ORIGINAL A and b by one '
      + 'matrix multiplication: <strong>' + checked + '</strong> entries compared, <strong>'
      + (wrong ? wrong + ' disagree' : 'none disagree') + '</strong>. A tableau twenty pivots in is a '
      + 'view of the data you typed, not a degraded copy of it &mdash; which is also why the fractions '
      + 'never run away: by Cramer’s rule each entry is a ratio of determinants of submatrices of '
      + 'the original data, so the denominators are bounded by that data however many pivots it takes. '
      + (allSlack
          ? 'Here B inverse does sit in the slack columns, because every row is a cap and the slack '
            + 'columns really were the identity at the start. That is the case the slogan was learned on.'
          : '<span class="tone-red">Here it does not sit in the slack columns.</span> The columns that '
            + 'started as the identity are <strong>' + cols.map(function (c) { return c.name; }).join(', ')
            + '</strong>, and ' + cols.filter(function (c) { return c.kind !== 'slack'; })
                .map(function (c) { return c.name; }).join(', ')
            + ' ' + plural(cols.filter(function (c) { return c.kind !== 'slack'; }).length, 'is an', 'are')
            + ' artificial. Read B inverse out of the slack columns here and you read the wrong block.');
  }

  [preset, showS].forEach(function (el) { el.addEventListener('change', redraw); });
  pivotS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The tableau as a matrix product",
        subtitle="B from the basis, B inverse by reduction, and the tableau rebuilt from the original data",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Rebuild a tableau"),
        panel_intro=cfg.get(
            "panel_intro",
            "The inverse is computed by reducing B beside the identity, with the trace shown, and "
            "then the products are compared with the tableau entry for entry.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "walk": _walk,
    "pivot": _pivot,
    "ratio": _ratio,
    "auto": _auto,
    "phase1": _phase1,
    "degenerate": _degenerate,
    "matrix": _matrix,
}

MODES = tuple(sorted(_MODES))

# What `preset` means in each mode, so a caller (and the build script that
# asserts no two of them render alike) can enumerate them without importing
# seven private lists.
PRESETS_BY_MODE = {
    "walk": WALK_PRESETS,
    "pivot": PIVOT_PRESETS,
    "ratio": RATIO_PRESETS,
    "auto": AUTO_PRESETS,
    "phase1": PHASE_PRESETS,
    "degenerate": DEGENERATE_PRESETS,
    "matrix": MATRIX_PRESETS,
}


def simplex_lab(cfg):
    """Course 2's kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is deliberate and it is the contract, not defensiveness. A kit
    that quietly fell back to a default mode would render a finished-looking
    page carrying another lesson's widget, and nothing downstream would notice:
    the markup tests pass, labcheck passes, and the reader is shown the wrong
    lesson's arithmetic under the right lesson's title. An unknown PRESET
    raises the same way and for the same reason -- three of these nine lessons
    are separated by the preset key alone, so a silent fallback there is
    exactly as wrong as a silent fallback on the mode.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _MODES:
        raise ValueError(
            "simplex_lab: unknown mode %r; the seven modes of this course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg)


__all__ = ["simplex_lab", "SIMPLEX_JS", "MODES", "PRESETS_BY_MODE"]
