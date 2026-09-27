"""Networks, the tableau half: three modes over one transportation tableau.

Course 4 of the Operations Research path is the one course on this path that
takes TWO kits, and this is the second of them. `network` draws networks;
`transport` draws tableaux. They are different user interfaces over the same
linear programme, and forcing them into one kit would have produced a mode
that draws nothing -- so the exception is deliberate and recorded.

Three modes, one lesson each.

  setup      balancing, the dummy row or column, and the two starting rules
             applied a step at a time with the occupied-cell count against
             m + n - 1 at every step
  modi       u, v, the reduced costs, and THE STEPPING-STONE CYCLE FOUND AND
             DRAWN, with theta tabulated over the minus cells and one
             iteration at a time
  hungarian  the row and column reductions, THE MINIMUM COVER COMPUTED BY
             KOENIG FROM A MATCHING, the adjustment step, and a greedy attempt
             shown with its gap

Four decisions run through all three.

  THE CYCLE IS COMPUTED, DRAWN, AND CHECKED. `or_core.stoneCycle` finds the
  unique cycle the entering cell creates in the spanning forest of basic
  cells, by a walk on the forest rather than by searching for rectangles. This
  kit draws it on the tableau -- a closed path through the cell centres, a
  plus or a minus on every corner, theta on the minus cells and a ring on the
  cell that leaves. `checkCycle` below then verifies the drawn thing against
  the rule readers break: a cycle may CROSS an empty cell but may only TURN at
  an occupied one. And `rectangleGuess` runs the guess a reader makes first --
  along the entering row to the first occupied cell, down that column, back --
  and names the corner that breaks it when it is empty. On the default view the
  guess is REFUSED FIRST, at (2,1), and closes on the second iteration; the
  empty corner is highlighted rather than described. That order is the right way
  round for the lesson -- a reader meets the failure before the shortcut that
  usually works -- and the surplus preset's first three pivots are all plain
  rectangles, so the guess is not being set up to fail.

  THE COVER IS KOENIG'S, NEVER "DRAW LINES UNTIL YOU CANNOT". `or_core.hungarian`
  builds the bipartite graph of the zero cells, calls `bipartiteMatch`, and
  reads the minimum vertex cover off the alternating-reachable set; the cover
  it returns has exactly the size of the matching, which is Koenig's theorem
  and is the claim the lesson rests on. `coverCheck` below re-verifies on the
  page that every zero really is covered, so the reader sees the property
  checked and not asserted. The line-drawing recipe has no stopping proof and
  is not implemented here. The derivation is
  `algorithms/graph-algorithms/bipartite-matching-via-flow`; Discrete
  Mathematics does not contain Koenig's theorem and must not be cited for it.

  THE DUAL IS RECOVERED AND ADDED UP. The Hungarian method's row and column
  constants are a dual feasible solution, and the total subtracted equals the
  cost of the assignment found -- strong duality on the instance. `assignDual`
  recovers u and v from the final reduced matrix (the recovery is fixed up to
  a shift u_i - t, v_j + t, and the matrix is SQUARE, so the total is
  invariant), checks u_i + v_j <= c_ij everywhere, and prints the two numbers
  side by side. If they ever disagreed the page would say so.

  u_1 = 0 IS A NORMALISATION AND THE READER MOVES IT. `shiftPotentials` takes
  the potentials `uvPotentials` returns and renormalises them on any u or any
  v the reader picks. Every u and every v moves; not one reduced cost does,
  and the page recomputes the whole reduced-cost table under the new
  normalisation to show that rather than to claim it.
"""

import json

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS
from .common import Lab
from .or_core import NET_JS, ORFMT_JS, TRANS_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no DOM: scripts/mathcheck.js
# extracts this block and calls every one of them. A helper closed over the
# document cannot be tested, and the untestable parts are the wrong ones.
# ---------------------------------------------------------------------------

TRANSPORT_JS = r"""
  /* ------------------------------------------------------------- reading in

     A tableau typed by a reader: rows separated by ';', entries by spaces or
     commas. Every entry goes through FORMAT_JS's Rread, so "7/2" is exact and
     "banana" is null rather than NaN. */
  function parseRow(text) {
    var parts = String(text).trim().split(/[\s,]+/), out = [], k;
    for (k = 0; k < parts.length; k += 1) {
      if (!parts[k]) continue;
      var v = Rread(parts[k]);
      if (v === null) return null;
      out.push(v);
    }
    return out.length ? out : null;
  }
  function parseGrid(text) {
    var rows = String(text).split(';'), out = [], k;
    for (k = 0; k < rows.length; k += 1) {
      if (!rows[k].trim()) continue;
      var r = parseRow(rows[k]);
      if (r === null) return null;
      out.push(r);
    }
    if (!out.length) return null;
    for (k = 1; k < out.length; k += 1) if (out[k].length !== out[0].length) return null;
    return out;
  }
  /* c dot x over the whole tableau, and over the REAL cells only -- the second
     is what the dummy costs, or rather what it does not. */
  function tableauCost(cost, x, rows, cols) {
    var total = R0, i, j;
    for (i = 0; i < x.length; i += 1) {
      if (rows !== undefined && rows !== null && i >= rows) continue;
      for (j = 0; j < x[i].length; j += 1) {
        if (cols !== undefined && cols !== null && j >= cols) continue;
        total = Radd(total, Rmul(cost[i][j], x[i][j]));
      }
    }
    return total;
  }

  /* ------------------------------------------------- the basis as a forest

     m + n - 1 basic cells on m + n row/column nodes is a SPANNING TREE, and
     everything the transportation simplex does is that sentence used twice.
     `basisForest` is the test: a cycle among the basic cells means the
     potentials are over-determined, and fewer than m + n - 1 edges means some
     entering cell has no cycle at all. */
  function basisForest(basis, m, n) {
    var parent = [], k, i;
    for (i = 0; i < m + n; i += 1) parent.push(i);
    var find = function (a) { while (parent[a] !== a) { parent[a] = parent[parent[a]]; a = parent[a]; } return a; };
    var cycle = null, edges = 0;
    for (k = 0; k < basis.length; k += 1) {
      var ra = find(basis[k].i), rb = find(m + basis[k].j);
      if (ra === rb) { if (cycle === null) cycle = { i: basis[k].i, j: basis[k].j }; continue; }
      parent[ra] = rb; edges += 1;
    }
    var roots = {};
    for (i = 0; i < m + n; i += 1) roots[find(i)] = true;
    var components = Object.keys(roots).length;
    return { acyclic: cycle === null, cycle: cycle, edges: edges, components: components,
             spanning: components === 1 && cycle === null && basis.length === m + n - 1,
             why: cycle !== null
               ? 'the basic cells contain a cycle through (' + (cycle.i + 1) + ',' + (cycle.j + 1)
                 + '), so they are not a tree and the potentials are over-determined'
               : (components === 1
                   ? 'the ' + basis.length + ' basic cells form a spanning tree of the ' + m
                     + ' supply nodes and ' + n + ' demand nodes'
                   : 'the basic cells fall into ' + components
                     + ' pieces, so some empty cell has no stepping-stone cycle at all') };
  }

  /* A degenerate start has FEWER than m + n - 1 basic cells, and then some
     entering cell has no cycle. The repair is a zero allocation -- the epsilon
     cell -- placed where it JOINS TWO PIECES of the forest rather than
     anywhere convenient, because a cell inside one piece would close a cycle.
     The cheapest such cell is chosen so the choice is stated rather than
     arbitrary, and every cell added is named. */
  function padBasis(basis, m, n, cost) {
    var out = basis.map(function (c) { return { i: c.i, j: c.j, x: c.x }; });
    var added = [], guard = 0;
    while (out.length < m + n - 1 && guard < m * n + 1) {
      guard += 1;
      var parent = [], i, j, k;
      for (i = 0; i < m + n; i += 1) parent.push(i);
      var find = function (a) { while (parent[a] !== a) { parent[a] = parent[parent[a]]; a = parent[a]; } return a; };
      for (k = 0; k < out.length; k += 1) parent[find(out[k].i)] = find(m + out[k].j);
      var bi = -1, bj = -1;
      for (i = 0; i < m; i += 1) for (j = 0; j < n; j += 1) {
        if (find(i) === find(m + j)) continue;
        if (bi < 0 || Rcmp(cost[i][j], cost[bi][bj]) < 0) { bi = i; bj = j; }
      }
      if (bi < 0) break;
      out.push({ i: bi, j: bj, x: R0, epsilon: true });
      added.push({ i: bi, j: bj, cost: cost[bi][bj] });
    }
    var names = added.map(function (c) { return '(' + (c.i + 1) + ',' + (c.j + 1) + ')'; });
    return { basis: out, added: added, count: out.length, want: m + n - 1,
             why: added.length === 0
               ? 'the start already occupies m + n - 1 = ' + (m + n - 1) + ' cells, so nothing was added'
               : 'the start was degenerate, so a zero allocation was placed in '
                 + names.join(' and ') + ' -- the cheapest cell that joins two pieces of the '
                 + 'forest without closing a cycle; a zero anywhere inside one piece would close one' };
  }

  /* ------------------------------------------------------ entering and cycle

     Two entering rules, because the reader should see that the OPTIMUM does
     not depend on the rule and the path to it does. Dantzig takes the most
     negative reduced cost; Bland takes the first negative one in row order and
     cannot cycle. */
  function pickEntering(reduced, basis, m, n, rule) {
    var isBasic = {}, k, i, j;
    for (k = 0; k < basis.length; k += 1) isBasic[basis[k].i + ',' + basis[k].j] = true;
    var best = null;
    for (i = 0; i < m; i += 1) {
      for (j = 0; j < n; j += 1) {
        var r = reduced[i][j];
        if (r === null || isBasic[i + ',' + j] || Rsign(r) >= 0) continue;
        if (best === null) { best = { i: i, j: j, value: r }; if (rule === 'bland') return best; continue; }
        if (rule === 'bland') return best;
        if (Rcmp(r, best.value) < 0) best = { i: i, j: j, value: r };
      }
    }
    return best;
  }

  /* The rule readers break, checked on the cycle actually drawn: signs
     alternate from the entering cell, every corner after the first carries an
     allocation, and each row and each column of the tableau is used exactly
     twice or not at all. A cycle may CROSS an empty cell; it may not TURN at
     one, and turning is what having a corner there means. */
  function checkCycle(cells, basis) {
    if (!cells || cells.length < 4) {
      return { ok: false, bad: null, why: 'a stepping-stone cycle needs at least four corners' };
    }
    if (cells.length % 2 !== 0) {
      return { ok: false, bad: null, why: 'a cycle alternating + and - must have an even number of corners' };
    }
    var occupied = {}, k;
    for (k = 0; k < basis.length; k += 1) occupied[basis[k].i + ',' + basis[k].j] = true;
    var rows = {}, cols = {};
    for (k = 0; k < cells.length; k += 1) {
      var c = cells[k], want = (k % 2 === 0) ? 1 : -1;
      if (c.sign !== want) {
        return { ok: false, bad: c, why: 'corner (' + (c.i + 1) + ',' + (c.j + 1)
          + ') carries the wrong sign; the signs alternate from the entering cell outwards' };
      }
      if (k > 0 && !occupied[c.i + ',' + c.j]) {
        return { ok: false, bad: c, why: 'the path turns at (' + (c.i + 1) + ',' + (c.j + 1)
          + '), which carries no allocation -- a stepping-stone cycle may cross an empty cell '
          + 'but may only turn at an occupied one' };
      }
      rows[c.i] = (rows[c.i] || 0) + 1;
      cols[c.j] = (cols[c.j] || 0) + 1;
    }
    var key;
    for (key in rows) if (rows[key] !== 2) {
      return { ok: false, bad: { i: Number(key), j: -1 },
               why: 'row ' + (Number(key) + 1) + ' has ' + rows[key]
                 + ' corners on the path; a cycle enters and leaves every row it touches exactly once' };
    }
    for (key in cols) if (cols[key] !== 2) {
      return { ok: false, bad: { i: -1, j: Number(key) },
               why: 'column ' + (Number(key) + 1) + ' has ' + cols[key]
                 + ' corners on the path; a cycle enters and leaves every column it touches exactly once' };
    }
    return { ok: true, bad: null,
             why: 'the path has ' + cells.length + ' corners, alternating + and -, every one after the '
               + 'entering cell occupied, and every row and column it touches used exactly twice' };
  }

  /* The guess a reader makes before the walk: along the entering row to the
     first occupied cell, down that column to the first occupied cell, and back
     along that row. It closes only when the fourth corner is occupied too, and
     the corner that is empty is the one to highlight. */
  function rectangleGuess(basis, enter, m, n) {
    var occupied = {}, k, i, j;
    for (k = 0; k < basis.length; k += 1) occupied[basis[k].i + ',' + basis[k].j] = true;
    var j2 = -1, i2 = -1;
    for (j = 0; j < n; j += 1) if (j !== enter.j && occupied[enter.i + ',' + j]) { j2 = j; break; }
    if (j2 < 0) {
      return { ok: false, cells: null, corner: null,
               why: 'row ' + (enter.i + 1) + ' has no other occupied cell, so no rectangle starts here at all' };
    }
    for (i = 0; i < m; i += 1) if (i !== enter.i && occupied[i + ',' + j2]) { i2 = i; break; }
    if (i2 < 0) {
      return { ok: false, cells: null, corner: null,
               why: 'column ' + (j2 + 1) + ' has no other occupied cell, so the rectangle cannot turn downwards' };
    }
    var cells = [{ i: enter.i, j: enter.j }, { i: enter.i, j: j2 }, { i: i2, j: j2 }, { i: i2, j: enter.j }];
    var closes = occupied[i2 + ',' + enter.j] === true;
    return { ok: closes, cells: cells, corner: closes ? null : { i: i2, j: enter.j },
             why: closes
               ? 'the plain rectangle (' + (enter.i + 1) + ',' + (enter.j + 1) + ') - ('
                 + (enter.i + 1) + ',' + (j2 + 1) + ') - (' + (i2 + 1) + ',' + (j2 + 1) + ') - ('
                 + (i2 + 1) + ',' + (enter.j + 1) + ') closes on four occupied corners, so here the guess '
                 + 'and the computed cycle agree'
               : 'the fourth corner (' + (i2 + 1) + ',' + (enter.j + 1) + ') is EMPTY, so the rectangle would '
                 + 'turn where nothing is allocated; the guess is refused and the computed cycle goes further' };
  }

  /* ------------------------------------------------------- the normalisation

     u_1 = 0 is not an assumption about the answer. The m + n potentials are
     determined only up to adding t to every u and subtracting it from every v,
     so the reader fixes whichever one they like and watches every u and every
     v move while not one reduced cost does. */
  function shiftPotentials(uv, cost, kind, at) {
    var m = uv.u.length, n = uv.v.length, i, j;
    if (!uv.connected) return null;
    if (kind === 'v') { if (at < 0 || at >= n) return null; }
    else if (at < 0 || at >= m) return null;
    var t = kind === 'v' ? Rneg(uv.v[at]) : uv.u[at];
    var u = [], v = [];
    for (i = 0; i < m; i += 1) u.push(Rsub(uv.u[i], t));
    for (j = 0; j < n; j += 1) v.push(Radd(uv.v[j], t));
    var reduced = [], same = true;
    for (i = 0; i < m; i += 1) {
      var row = [];
      for (j = 0; j < n; j += 1) {
        var r = Rsub(cost[i][j], Radd(u[i], v[j]));
        row.push(r);
        if (uv.reduced[i][j] === null || !Requ(r, uv.reduced[i][j])) same = false;
      }
      reduced.push(row);
    }
    return { u: u, v: v, reduced: reduced, shift: t, kind: kind, at: at, same: same,
             why: 'fixing ' + kind + (at + 1) + ' = 0 moves every potential by '
               + Rtext(t) + (Rzero(t) ? ' (which is none, here)' : '')
               + ' and leaves every reduced cost exactly where it was' };
  }

  /* ------------------------------------------------------- the MODI iteration

     One call, every iteration kept. The lab shows them one at a time rather
     than animating, because the thing to look at is the cycle and a cycle that
     flashes past is a decoration. */
  function modiRun(cost, start, m, n, opts) {
    opts = opts || {};
    var rule = opts.rule === 'bland' ? 'bland' : 'dantzig';
    var pad = padBasis(start.basis, m, n, cost);
    var basis = pad.basis.map(function (c) { return { i: c.i, j: c.j, x: c.x }; });
    var x = start.x.map(function (r) { return r.slice(); });
    var iterations = [], guard = 0, capped = false, k;
    while (true) {
      guard += 1;
      if (guard > 4 * (m + n) + 8) { capped = true; break; }
      var uv = uvPotentials(cost, basis, m, n);
      var enter = uv.connected ? pickEntering(uv.reduced, basis, m, n, rule) : null;
      var it = { basis: basis.map(function (c) { return { i: c.i, j: c.j, x: c.x }; }),
                 x: x.map(function (r) { return r.slice(); }), uv: uv, entering: enter,
                 cost: tableauCost(cost, x), forest: basisForest(basis, m, n),
                 cycle: null, check: null, rect: null, optimal: enter === null && uv.connected };
      if (enter === null) { iterations.push(it); break; }
      var cyc = stoneCycle(basis, enter, m, n);
      it.cycle = cyc;
      it.check = cyc.found ? checkCycle(cyc.cells, basis) : { ok: false, bad: null, why: cyc.why };
      it.rect = rectangleGuess(basis, enter, m, n);
      iterations.push(it);
      if (!cyc.found || !it.check.ok) break;
      for (k = 0; k < cyc.cells.length; k += 1) {
        var c = cyc.cells[k];
        x[c.i][c.j] = c.sign > 0 ? Radd(x[c.i][c.j], cyc.theta) : Rsub(x[c.i][c.j], cyc.theta);
      }
      var left = false;
      basis = basis.filter(function (b) {
        if (!left && b.i === cyc.leaving.i && b.j === cyc.leaving.j) { left = true; return false; }
        return true;
      }).concat([{ i: enter.i, j: enter.j }]).map(function (b) {
        return { i: b.i, j: b.j, x: x[b.i][b.j] };
      });
    }
    var last = iterations[iterations.length - 1];
    return { iterations: iterations, pad: pad, capped: capped,
             optimal: !capped && last !== undefined && last.optimal === true,
             cost: last === undefined ? R0 : last.cost, x: x };
  }

  /* --------------------------------------------------------- the assignment

     The dual of the assignment problem, recovered from what the Hungarian
     method left behind. M_ij = c_ij - u_i - v_j holds by construction at every
     step, so u and v are recoverable from the final reduced matrix up to a
     shift u_i - t, v_j + t -- and because the matrix is SQUARE that shift adds
     n*t and subtracts n*t, so sum(u) + sum(v) is the same number whichever
     recovery you pick. That number is the dual objective, and it equals the
     assignment's cost: strong duality, on this instance, computed twice. */
  function assignDual(cost, reduced) {
    var n = cost.length, u = [], v = [], i, j;
    /* v_1 := 0 is the recovery's own normalisation, and the sum is immune to it. */
    for (i = 0; i < n; i += 1) u.push(Rsub(cost[i][0], reduced[i][0]));
    for (j = 0; j < n; j += 1) v.push(Rsub(Rsub(cost[0][j], reduced[0][j]), u[0]));
    var consistent = true, feasible = true, total = R0;
    for (i = 0; i < n; i += 1) {
      for (j = 0; j < n; j += 1) {
        if (!Requ(Radd(Radd(u[i], v[j]), reduced[i][j]), cost[i][j])) consistent = false;
        if (Rsign(reduced[i][j]) < 0) feasible = false;
      }
    }
    for (i = 0; i < n; i += 1) total = Radd(total, u[i]);
    for (j = 0; j < n; j += 1) total = Radd(total, v[j]);
    return { u: u, v: v, total: total, consistent: consistent, feasible: feasible,
             why: 'the row and column constants add to ' + Rtext(total)
               + ', and u_i + v_j <= c_ij holds ' + (feasible ? 'in every cell' : 'nowhere near everywhere') };
  }

  /* Does the cover the matching produced actually cover every zero? Koenig
     says a cover of that size exists; this checks that THIS one is a cover,
     on the page, in front of the reader. */
  function coverCheck(M, cover) {
    var n = M.length, rows = {}, cols = {}, missed = [], i, j;
    for (i = 0; i < cover.left.length; i += 1) rows[Number(String(cover.left[i]).slice(1))] = true;
    for (j = 0; j < cover.right.length; j += 1) cols[Number(String(cover.right[j]).slice(1))] = true;
    for (i = 0; i < n; i += 1) {
      for (j = 0; j < n; j += 1) {
        if (Rzero(M[i][j]) && !rows[i] && !cols[j]) missed.push({ i: i, j: j });
      }
    }
    return { ok: missed.length === 0, missed: missed, rows: rows, cols: cols, size: cover.size,
             why: missed.length === 0
               ? 'every zero lies in one of the ' + cover.size + ' covered lines'
               : missed.length + ' zero cell(s) lie outside the cover, which would make it not a cover' };
  }

  /* Cheapest cell first, and never revisited. It is what a reader does by hand
     and it is not the Hungarian method; the gap is the point, and on a matrix
     where it happens to be right the page says that a lucky answer is not a
     proof. */
  function greedyAssign(cost) {
    var n = cost.length, usedR = {}, usedC = {}, assignment = [], order = [], i, j, k;
    for (i = 0; i < n; i += 1) assignment.push(-1);
    for (k = 0; k < n; k += 1) {
      var bi = -1, bj = -1;
      for (i = 0; i < n; i += 1) {
        if (usedR[i]) continue;
        for (j = 0; j < n; j += 1) {
          if (usedC[j]) continue;
          if (bi < 0 || Rcmp(cost[i][j], cost[bi][bj]) < 0) { bi = i; bj = j; }
        }
      }
      if (bi < 0) break;
      usedR[bi] = true; usedC[bj] = true; assignment[bi] = bj;
      order.push({ i: bi, j: bj, cost: cost[bi][bj] });
    }
    var value = R0;
    for (i = 0; i < n; i += 1) if (assignment[i] >= 0) value = Radd(value, cost[i][assignment[i]]);
    return { assignment: assignment, order: order, value: value, complete: order.length === n };
  }
"""

_CORE_JS = RATIONAL_JS + FORMAT_JS + ORFMT_JS + NET_JS + TRANS_JS + TRANSPORT_JS


# ---------------------------------------------------------------------------
# The worked examples. Every preset is a cost table and its margins, typed the
# way a reader types them, so the lab parses its own presets through the same
# path a reader's edit takes -- there is no second, privileged way in.
#
# `balanced` is the instance scripts/mathcheck.js pins: its transportation LP
# is solved independently by the exact simplex through Phase I with equality
# rows, and the optimum is 435. The kit's default preset is therefore the one
# instance whose answer is proved somewhere other than here.
# ---------------------------------------------------------------------------

TRANS_PRESETS = {
    "balanced": {
        "label": "Three plants, four depots (supply and demand already balance)",
        "cost": "10 2 20 11; 12 7 9 20; 4 14 16 18",
        "supply": "15 25 10",
        "demand": "5 15 15 15",
        "rows": "Plant A, Plant B, Plant C",
        "cols": "Depot 1, Depot 2, Depot 3, Depot 4",
    },
    "surplus": {
        "label": "Three mills, three yards (supply exceeds demand)",
        "cost": "8 6 10; 9 12 13; 14 9 16",
        "supply": "20 30 25",
        "demand": "20 25 20",
        "rows": "Mill A, Mill B, Mill C",
        "cols": "Yard 1, Yard 2, Yard 3",
    },
    "degenerate": {
        "label": "Three depots, three shops (the north-west rule ties)",
        "cost": "5 3 8; 4 7 6; 9 2 5",
        "supply": "10 20 10",
        "demand": "10 20 10",
        "rows": "Depot A, Depot B, Depot C",
        "cols": "Shop 1, Shop 2, Shop 3",
    },
}

ASSIGN_PRESETS = {
    "jobs": {
        "label": "Four fitters, four jobs",
        "cost": "10 19 8 15; 10 18 7 17; 13 16 9 14; 12 19 8 18",
        "rows": "Fitter A, Fitter B, Fitter C, Fitter D",
        "cols": "Job 1, Job 2, Job 3, Job 4",
    },
    "sites": {
        "label": "Four crews, four sites (greedy loses badly here)",
        "cost": "90 75 75 80; 35 85 55 65; 125 95 90 105; 45 110 95 115",
        "rows": "Crew A, Crew B, Crew C, Crew D",
        "cols": "Site 1, Site 2, Site 3, Site 4",
    },
    "crews": {
        "label": "Five drivers, five routes (greedy happens to be right)",
        "cost": "9 11 14 11 7; 6 15 13 13 10; 12 13 6 8 8; 11 9 10 12 9; 7 12 14 10 14",
        "rows": "Driver A, Driver B, Driver C, Driver D, Driver E",
        "cols": "Route 1, Route 2, Route 3, Route 4, Route 5",
    },
}


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on the path uses.
# ---------------------------------------------------------------------------


def _payload(name, values):
    """Embed a JS literal. The escape makes "</script>" structurally impossible."""
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


# ---------------------------------------------------------------------------
# Mode `setup` -- balancing, the dummy, and the two starting rules
# ---------------------------------------------------------------------------


def _setup(cfg):
    chosen = cfg.get("preset", "balanced")
    if chosen not in TRANS_PRESETS:
        raise ValueError(
            "transport_lab: mode 'setup' has no preset %r; the presets are %s"
            % (chosen, ", ".join(sorted(TRANS_PRESETS)))
        )
    here = TRANS_PRESETS[chosen]

    markup = (
        _toolbar(
            "Balance first, then start",
            "a dummy at zero cost, and the occupied cells counted against m + n &minus; 1",
            [
                ("cyan", "allocated at this step"),
                ("green", "allocated earlier"),
                ("amber", "the dummy row or column"),
                ("muted", "still empty"),
            ],
        )
        + _stage(_svg("tsBars", "0 0 660 136",
                      "Total supply and total demand as two bars, with the dummy quantity that balances them."))
        + _table("tsGrid")
        + _table("tsTrace")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Worked example",
                [(k, TRANS_PRESETS[k]["label"]) for k in ("balanced", "surplus", "degenerate")], chosen)
        + _text("tsCost", "Cost table &mdash; rows separated by &ldquo;;&rdquo;", here["cost"])
        + _text("tsSupply", "Supplies", here["supply"])
        + _text("tsDemand", "Demands", here["demand"])
        + _select("tsRule", "Starting rule",
                  [("northwest", "North-west corner"), ("least", "Least cost")], "northwest")
        + _range("tsStep", "Allocations made so far", 0, 6, 6, 1)
        + _kpis(
            [
                ("Supply and demand", "tsTotals"),
                ("Dummy", "tsDummyK"),
                ("Occupied cells", "tsCellsK"),
                ("North-west corner cost", "tsNwK"),
                ("Least-cost cost", "tsLcK"),
                ("Real bill if the dummy were priced high", "tsPenaltyK"),
            ]
        )
        + _hint(
            "tsHint",
            "The dummy costs zero because what it carries is the quantity that never moves. "
            "Price it high instead and the tableau still finds the same real shipments &mdash; every "
            "plan sends the same quantity there &mdash; but reports a total inflated by a charge "
            "for goods that never move. The banner computes both.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", TRANS_PRESETS) + r"""
  var presetS = document.getElementById('tsPreset');
  var costIn = document.getElementById('tsCost');
  var supIn = document.getElementById('tsSupply');
  var demIn = document.getElementById('tsDemand');
  var ruleS = document.getElementById('tsRule');
  var stepS = document.getElementById('tsStep');
  var bars = document.getElementById('tsBars');
  var gridEl = document.getElementById('tsGrid');
  var traceEl = document.getElementById('tsTrace');
  var statusEl = document.getElementById('tsStatus');
  var snapToEnd = false;

  function names(text, count, prefix) {
    var parts = String(text || '').split(',').map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length; });
    if (parts.length !== count) { parts = []; for (var k = 0; k < count; k += 1) parts.push(prefix + (k + 1)); }
    return parts;
  }
  function px(r) { return parseFloat(Rfixed(r, 6)); }
  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    bars.innerHTML = '';
    gridEl.innerHTML = '';
    traceEl.innerHTML = '';
    ['tsTotals', 'tsDummyK', 'tsCellsK', 'tsNwK', 'tsLcK', 'tsPenaltyK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var cost = parseGrid(costIn.value), sup = parseRow(supIn.value), dem = parseRow(demIn.value);
    if (cost === null || sup === null || dem === null) {
      blank('Every entry has to be a number or a fraction such as 7/2. Rows of the cost table are '
        + 'separated by a semicolon, entries by spaces or commas.');
      return;
    }
    if (cost.length !== sup.length || cost[0].length !== dem.length) {
      blank('The cost table is ' + cost.length + ' by ' + cost[0].length + ', so it needs '
        + cost.length + ' supplies and ' + cost[0].length + ' demands; it was given '
        + sup.length + ' and ' + dem.length + '.');
      return;
    }
    var rowNames = names(PRESETS[presetS.value] ? PRESETS[presetS.value].rows : '', cost.length, 'Source ');
    var colNames = names(PRESETS[presetS.value] ? PRESETS[presetS.value].cols : '', cost[0].length, 'Sink ');

    /* Nothing below is stored: balance() decides the dummy from the two totals
       and both rules are run on the balanced data, every redraw. */
    var bal = balance(sup, dem, cost);
    var C = bal.cost, S = bal.supply, D = bal.demand, m = S.length, n = D.length;
    var realRows = bal.dummy === 'row' ? m - 1 : m, realCols = bal.dummy === 'col' ? n - 1 : n;
    if (bal.dummy === 'row') rowNames = rowNames.concat(['Dummy source']);
    if (bal.dummy === 'col') colNames = colNames.concat(['Dummy sink']);

    var nw = northwest(C, S, D), lc = leastCost(C, S, D);
    var run = ruleS.value === 'least' ? lc : nw;
    var maxStep = run.steps.length;
    stepS.max = String(maxStep);
    if (snapToEnd) { stepS.value = String(maxStep); snapToEnd = false; }
    var step = Math.max(0, Math.min(maxStep, +stepS.value || 0));
    document.getElementById('tsStepOut').textContent = step + ' of ' + maxStep;

    /* The allocations visible at this step, and nothing else. */
    var placed = {}, i, j, k;
    for (k = 0; k < step; k += 1) placed[run.steps[k].i + ',' + run.steps[k].j] = k;
    var last = step > 0 ? run.steps[step - 1] : null;

    var heads = [th('')], rows = [];
    for (j = 0; j < n; j += 1) heads.push(th(colNames[j]));
    heads.push(th('supply'));
    for (i = 0; i < m; i += 1) {
      var cells = [rowhead(rowNames[i])];
      for (j = 0; j < n; j += 1) {
        var at = placed[i + ',' + j];
        var dummyCell = (bal.dummy === 'row' && i === m - 1) || (bal.dummy === 'col' && j === n - 1);
        var body = '<span class="small">' + Rshort(C[i][j]) + '</span>';
        if (at !== undefined) {
          body += '<br><strong>' + Rshort(run.steps[at].amount) + '</strong>';
        }
        var cls = at === undefined ? (dummyCell ? 'tone-amber' : 'tone-muted')
          : (at === step - 1 ? 'tone-cyan' : (dummyCell ? 'tone-amber' : 'tone-green'));
        cells.push(td(body, cls));
      }
      cells.push(td(Rshort(S[i]), (bal.dummy === 'row' && i === m - 1) ? 'tone-amber' : ''));
      rows.push(tr(cells));
    }
    var foot = [rowhead('demand')];
    for (j = 0; j < n; j += 1) {
      foot.push(td(Rshort(D[j]), (bal.dummy === 'col' && j === n - 1) ? 'tone-amber' : ''));
    }
    foot.push(td(Rshort(bal.totalSupply)));
    rows.push(tr(foot));
    gridEl.innerHTML = '<caption>The balanced tableau: unit cost above, allocation below</caption>'
      + '<thead>' + tr(heads) + '</thead><tbody>' + rows.join('') + '</tbody>';

    /* The trace, one row per allocation actually made so far. */
    var traceRows = [];
    for (k = 0; k < step; k += 1) {
      var s = run.steps[k];
      traceRows.push(tr([rowhead('allocation ' + (k + 1)), tdl(s.why),
        td('<strong>' + (k + 1) + '</strong> of ' + run.want, k + 1 === run.want ? 'tone-green' : 'tone-muted')]));
    }
    if (!traceRows.length) {
      traceRows.push(tr([rowhead('nothing yet'),
        tdl('Move the slider to apply the ' + run.rule + ' rule one allocation at a time.'), td('0 of ' + run.want)]));
    }
    traceEl.innerHTML = '<caption>What the ' + run.rule + ' rule did, and the occupied-cell count after it</caption>'
      + '<thead>' + tr([th('step'), th('why this cell'), th('occupied of m + n &minus; 1')]) + '</thead>'
      + '<tbody>' + traceRows.join('') + '</tbody>';

    /* Two bars, one per side of the balance, with the dummy piece shown as the
       gap it fills rather than as a number in a caption. */
    var span = Rcmp(bal.totalSupply, bal.totalDemand) > 0 ? bal.totalSupply : bal.totalDemand;
    var scale = px(span) || 1, wide = 560;
    var supW = wide * px(bal.totalSupply) / scale, demW = wide * px(bal.totalDemand) / scale;
    var gap = Math.abs(supW - demW);
    var svg = '<text x="14" y="20" font-size="11" fill="var(--muted)">total supply</text>'
      + '<rect x="14" y="28" width="' + supW + '" height="24" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (20 + supW) + '" y="45" font-size="12" fill="var(--text)" font-weight="700">'
      + Rshort(bal.totalSupply) + '</text>'
      + '<text x="14" y="80" font-size="11" fill="var(--muted)">total demand</text>'
      + '<rect x="14" y="88" width="' + demW + '" height="24" rx="3" fill="var(--cyan)" opacity="0.85" />'
      + '<text x="' + (20 + demW) + '" y="105" font-size="12" fill="var(--text)" font-weight="700">'
      + Rshort(bal.totalDemand) + '</text>';
    if (bal.dummy !== null) {
      var gx = 14 + Math.min(supW, demW), gy = bal.dummy === 'col' ? 88 : 28;
      svg += '<rect x="' + gx + '" y="' + gy + '" width="' + gap + '" height="24" rx="3" '
        + 'fill="var(--amber)" opacity="0.75" />'
        + '<text x="' + (gx + 4) + '" y="' + (gy + 17) + '" font-size="11" fill="var(--on-accent)" '
        + 'font-weight="700">' + (gap > 96 ? 'dummy ' + Rshort(bal.amount) : '') + '</text>'
        + '<text x="14" y="130" font-size="10" fill="var(--amber)">the amber block is the dummy '
        + (bal.dummy === 'col' ? 'destination' : 'source') + ', carrying ' + Rshort(bal.amount)
        + ' at zero cost</text>';
    } else {
      svg += '<text x="14" y="130" font-size="10" fill="var(--muted)">the two sides already agree, '
        + 'so there is no dummy and no gap to fill</text>';
    }
    bars.innerHTML = svg;

    /* The misconception, priced. The dummy is re-priced high, the SAME rule is
       run on it, and MODI is taken to optimality on both -- because the answer
       is not what a reader expects. Every feasible solution ships the same
       quantity to the dummy, so a uniform price adds a CONSTANT to every total:
       the optimum does not move, the start does, and the number the tableau
       reports is inflated by exactly that constant. All three are computed. */
    var penalty = '<span class="tone-muted">no dummy on this instance</span>', priceLine = '';
    if (bal.dummy !== null) {
      var big = C[0][0];
      for (i = 0; i < realRows; i += 1) for (j = 0; j < realCols; j += 1) if (Rcmp(C[i][j], big) > 0) big = C[i][j];
      var pen = Rmul(big, R(10n, 1n));
      var Cp = C.map(function (r) { return r.slice(); });
      if (bal.dummy === 'col') { for (i = 0; i < m; i += 1) Cp[i][n - 1] = pen; }
      else { for (j = 0; j < n; j += 1) Cp[m - 1][j] = pen; }
      var alt = ruleS.value === 'least' ? leastCost(Cp, S, D) : northwest(Cp, S, D);
      var realZero = tableauCost(C, run.x, realRows, realCols);
      var realPen = tableauCost(C, alt.x, realRows, realCols);
      var bestZero = tableauCost(C, modiRun(C, run, m, n, {}).x, realRows, realCols);
      var bestPen = tableauCost(C, modiRun(Cp, alt, m, n, {}).x, realRows, realCols);
      penalty = 'start ' + Rshort(realZero) + ' &rarr; ' + Rshort(realPen)
        + (Requ(realZero, realPen) ? '' : ' <span class="tone-red">moved</span>')
        + ', optimum ' + Rshort(bestZero) + ' &rarr; ' + Rshort(bestPen)
        + (Requ(bestZero, bestPen) ? ' <span class="tone-green">unmoved</span>'
            : ' <span class="tone-red">moved</span>');
      priceLine = ' Price the dummy at ' + Rshort(pen) + ' and the real shipping bill of this start '
        + (Requ(realZero, realPen)
            ? (ruleS.value === 'least'
                ? 'happens not to move on this tableau'
                : 'does not move at all &mdash; the north-west corner rule never reads a cost')
            : 'moves from ' + Rshort(realZero) + ' to ' + Rshort(realPen))
        + (Requ(bestZero, bestPen)
            ? ', while the optimum stays at ' + Rshort(bestZero)
            : ', and the optimum goes from ' + Rshort(bestZero) + ' to ' + Rshort(bestPen))
        + ': every feasible solution ships the same '
        + Rshort(bal.amount) + ' to the dummy, so a uniform price adds the same '
        + Rshort(Rmul(pen, bal.amount)) + ' to every total. That constant is the whole objection. '
        + 'The tableau would report ' + Rshort(Radd(bestZero, Rmul(pen, bal.amount)))
        + ' for a plan that costs ' + Rshort(bestZero) + ', the difference being a charge for goods '
        + 'that never move.';
    }

    setKpi('tsTotals', Rshort(bal.totalSupply) + ' and ' + Rshort(bal.totalDemand));
    setKpi('tsDummyK', bal.dummy === null ? 'none needed'
      : (bal.dummy === 'col' ? 'a destination' : 'a source') + ' carrying ' + Rshort(bal.amount) + ' at cost 0');
    setKpi('tsCellsK', step + ' occupied, ' + run.want + ' wanted'
      + (step === run.want ? ' <span class="tone-green">&check;</span>' : ''));
    setKpi('tsNwK', Rshort(nw.cost) + (nw.degenerate ? ' <span class="tone-amber">degenerate</span>' : ''));
    setKpi('tsLcK', Rshort(lc.cost) + (lc.degenerate ? ' <span class="tone-amber">degenerate</span>' : ''));
    setKpi('tsPenaltyK', penalty);

    var cheaper = Rcmp(nw.cost, lc.cost);
    var eps = run.epsilon.map(function (c) { return '(' + (c.i + 1) + ',' + (c.j + 1) + ')'; });
    statusEl.innerHTML = '<strong>' + bal.why.charAt(0).toUpperCase() + bal.why.slice(1) + '.</strong> '
      + 'On the balanced tableau m + n &minus; 1 = ' + m + ' + ' + n + ' &minus; 1 = ' + run.want
      + ', and the ' + run.rule + ' rule has placed <strong>' + step + '</strong> of them so far. '
      + (cheaper === 0
          ? 'Both rules start at ' + Rshort(nw.cost) + ' here.'
          : 'The least-cost start costs ' + Rshort(lc.cost) + ' against the north-west corner&rsquo;s '
            + Rshort(nw.cost) + ', which is ' + Rshort(Rsub(nw.cost, lc.cost)) + ' better before any '
            + 'improvement step has run.')
      + (eps.length
          ? ' This start is <span class="tone-amber">degenerate</span>: ' + eps.join(' and ')
            + ' carr' + (eps.length === 1 ? 'ies' : 'y') + ' a zero, which is a named epsilon cell and not '
            + 'a missing one &mdash; it keeps the occupied count at ' + run.want + ' so the potentials stay determined.'
          : ' Neither rule tied here, so no zero allocation was needed.')
      + priceLine;
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    costIn.value = p.cost; supIn.value = p.supply; demIn.value = p.demand;
    snapToEnd = true;
    redraw();
  });
  ruleS.addEventListener('change', function () { snapToEnd = true; redraw(); });
  [costIn, supIn, demIn, stepS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A tableau that does not balance cannot be solved",
        subtitle="the dummy carries what never moves, at a cost of nothing",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Type a tableau, pick a rule, step through it",
        panel_intro="The totals are compared and the dummy row or column is added here, not stored; "
        "both starting rules are then run on the balanced table and the occupied-cell count is "
        "shown against m + n &minus; 1 after every allocation.",
    )


# ---------------------------------------------------------------------------
# Mode `modi` -- u, v, the reduced costs, and the stepping-stone cycle drawn
# ---------------------------------------------------------------------------


def _modi(cfg):
    chosen = cfg.get("preset", "balanced")
    if chosen not in TRANS_PRESETS:
        raise ValueError(
            "transport_lab: mode 'modi' has no preset %r; the presets are %s"
            % (chosen, ", ".join(sorted(TRANS_PRESETS)))
        )

    markup = (
        _toolbar(
            "One iteration, and the cycle it turns on",
            "u + v on the occupied cells, c &minus; u &minus; v on the rest, and a closed path of &plusmn;&theta;",
            [
                ("purple", "the stepping-stone cycle"),
                ("cyan", "entering cell"),
                ("red", "leaving cell"),
                ("amber", "a negative reduced cost"),
            ],
        )
        + _stage(_svg("tmGrid", "0 0 660 280",
                      "The transportation tableau with the stepping-stone cycle drawn as a closed path "
                      "through the cells it moves, plus and minus alternating around it."))
        + _table("tmTheta")
        + _table("tmNormT")
        + _banner("tmStatus")
    )
    controls = (
        _select("tmPreset", "Worked example",
                [(k, TRANS_PRESETS[k]["label"]) for k in ("balanced", "surplus", "degenerate")], chosen)
        + _select("tmStart", "Starting solution",
                  [("northwest", "North-west corner"), ("least", "Least cost")], "northwest")
        + _select("tmRule", "Entering cell",
                  [("dantzig", "Most negative reduced cost"), ("bland", "First negative, in row order")],
                  "dantzig")
        + _range("tmIter", "Iteration", 0, 3, 0, 1)
        + _range("tmNorm", "Which potential is fixed at zero", 0, 6, 0, 1)
        + _kpis(
            [
                ("Entering cell", "tmEnterK"),
                ("&theta;", "tmThetaK"),
                ("Leaving cell", "tmLeaveK"),
                ("Cost after this iteration", "tmCostK"),
                ("The cycle, checked", "tmCheckK"),
                ("The rectangle a reader guesses", "tmRectK"),
            ]
        )
        + _hint(
            "tmHint",
            "A stepping-stone cycle may cross an empty cell and may only turn at an occupied one. "
            "That is the rule the rectangle guess breaks, and when it breaks it the offending corner "
            "is ringed on the tableau rather than described.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", TRANS_PRESETS) + r"""
  var presetS = document.getElementById('tmPreset');
  var startS = document.getElementById('tmStart');
  var ruleS = document.getElementById('tmRule');
  var iterS = document.getElementById('tmIter');
  var normS = document.getElementById('tmNorm');
  var gridEl = document.getElementById('tmGrid');
  var thetaEl = document.getElementById('tmTheta');
  var normEl = document.getElementById('tmNormT');
  var statusEl = document.getElementById('tmStatus');

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function cellName(c) { return '(' + (c.i + 1) + ',' + (c.j + 1) + ')'; }
  function geom(m, n) {
    var left = 8, lab = 64, supw = 52, uw = 52;
    var cw = Math.floor((660 - left - lab - supw - uw - 8) / n), ch = 56, top = 30;
    return { left: left, lab: lab, x0: left + lab, cw: cw, ch: ch, top: top,
             supx: left + lab + n * cw, ux: left + lab + n * cw + supw, supw: supw, uw: uw,
             demy: top + m * ch, vy: top + m * ch + 26, height: top + m * ch + 70 };
  }
  function box(g, i, j) {
    return { x: g.x0 + j * g.cw, y: g.top + i * g.ch, cx: g.x0 + j * g.cw + g.cw / 2,
             cy: g.top + i * g.ch + g.ch / 2 };
  }
  function ring(g, i, j, colour, dashed) {
    var b = box(g, i, j);
    return '<rect x="' + (b.x + 2) + '" y="' + (b.y + 2) + '" width="' + (g.cw - 4) + '" height="'
      + (g.ch - 4) + '" rx="4" fill="none" stroke="var(--' + colour + ')" stroke-width="2"'
      + (dashed ? ' stroke-dasharray="5 3"' : '') + ' />';
  }

  function redraw() {
    var p = PRESETS[presetS.value];
    var cost = parseGrid(p.cost), sup = parseRow(p.supply), dem = parseRow(p.demand);
    var bal = balance(sup, dem, cost);
    var C = bal.cost, S = bal.supply, D = bal.demand, m = S.length, n = D.length, i, j, k;
    var start = startS.value === 'least' ? leastCost(C, S, D) : northwest(C, S, D);
    var run = modiRun(C, start, m, n, { rule: ruleS.value });
    var total = run.iterations.length;

    iterS.max = String(total - 1);
    var at = Math.max(0, Math.min(total - 1, +iterS.value || 0));
    document.getElementById('tmIterOut').textContent = (at + 1) + ' of ' + total;
    var it = run.iterations[at];

    normS.max = String(m + n - 1);
    var normAt = Math.max(0, Math.min(m + n - 1, +normS.value || 0));
    var normKind = normAt < m ? 'u' : 'v', normIx = normAt < m ? normAt : normAt - m;
    document.getElementById('tmNormOut').textContent = normKind + (normIx + 1) + ' = 0';
    var shift = shiftPotentials(it.uv, C, normKind, normIx);
    var u = shift === null ? it.uv.u : shift.u, v = shift === null ? it.uv.v : shift.v;
    var reduced = shift === null ? it.uv.reduced : shift.reduced;

    var basicAt = {};
    for (k = 0; k < it.basis.length; k += 1) basicAt[it.basis[k].i + ',' + it.basis[k].j] = it.basis[k];
    var onCycle = {};
    if (it.cycle && it.cycle.cells) {
      for (k = 0; k < it.cycle.cells.length; k += 1) {
        onCycle[it.cycle.cells[k].i + ',' + it.cycle.cells[k].j] = it.cycle.cells[k];
      }
    }

    /* ---- the tableau, drawn ------------------------------------------- */
    var g = geom(m, n), svg = '';
    gridEl.setAttribute('viewBox', '0 0 660 ' + g.height);
    for (j = 0; j < n; j += 1) {
      svg += '<text x="' + (g.x0 + j * g.cw + g.cw / 2) + '" y="20" font-size="11" fill="var(--muted)" '
        + 'text-anchor="middle">' + ((bal.dummy === 'col' && j === n - 1) ? 'dummy' : 'to ' + (j + 1)) + '</text>';
    }
    svg += '<text x="' + (g.supx + g.supw / 2) + '" y="20" font-size="11" fill="var(--muted)" '
      + 'text-anchor="middle">supply</text>'
      + '<text x="' + (g.ux + g.uw / 2) + '" y="20" font-size="11" fill="var(--cyan)" '
      + 'text-anchor="middle">u</text>';
    for (i = 0; i < m; i += 1) {
      var b0 = box(g, i, 0);
      svg += '<text x="' + (g.left + 4) + '" y="' + (b0.cy + 4) + '" font-size="11" fill="var(--muted)">'
        + ((bal.dummy === 'row' && i === m - 1) ? 'dummy' : 'from ' + (i + 1)) + '</text>';
      for (j = 0; j < n; j += 1) {
        var b = box(g, i, j), basic = basicAt[i + ',' + j], cyc = onCycle[i + ',' + j];
        var fill = basic ? 'var(--panel-3)' : 'var(--panel-2)';
        svg += '<rect x="' + b.x + '" y="' + b.y + '" width="' + g.cw + '" height="' + g.ch
          + '" fill="' + fill + '" stroke="var(--line)" stroke-width="1" />'
          + '<text x="' + (b.x + 5) + '" y="' + (b.y + 14) + '" font-size="10" fill="var(--muted)">'
          + Rshort(C[i][j]) + '</text>';
        if (basic) {
          svg += '<text x="' + b.cx + '" y="' + (b.cy + 8) + '" font-size="15" font-weight="700" '
            + 'fill="var(--text)" text-anchor="middle">' + Rshort(it.x[i][j]) + '</text>';
          if (Rzero(it.x[i][j])) {
            svg += '<text x="' + b.cx + '" y="' + (b.y + g.ch - 6) + '" font-size="9" fill="var(--amber)" '
              + 'text-anchor="middle">epsilon</text>';
          }
        } else if (reduced[i][j] !== null) {
          var neg = Rsign(reduced[i][j]) < 0;
          svg += '<text x="' + b.cx + '" y="' + (b.cy + 6) + '" font-size="12" fill="var(--'
            + (neg ? 'amber' : 'muted') + ')" text-anchor="middle">' + Rshort(reduced[i][j]) + '</text>';
        }
        if (cyc) {
          svg += '<text x="' + (b.x + g.cw - 6) + '" y="' + (b.y + 15) + '" font-size="12" '
            + 'font-weight="700" fill="var(--purple)" text-anchor="end">'
            + (cyc.sign > 0 ? '+' : '-') + '</text>';
        }
      }
      svg += '<rect x="' + g.supx + '" y="' + b0.y + '" width="' + g.supw + '" height="' + g.ch
        + '" fill="var(--panel-2)" stroke="var(--line)" />'
        + '<text x="' + (g.supx + g.supw / 2) + '" y="' + (b0.cy + 5) + '" font-size="12" '
        + 'fill="var(--text)" text-anchor="middle">' + Rshort(S[i]) + '</text>'
        + '<text x="' + (g.ux + g.uw / 2) + '" y="' + (b0.cy + 5) + '" font-size="12" '
        + 'fill="var(--cyan)" text-anchor="middle">' + (u[i] === null ? '?' : Rshort(u[i])) + '</text>';
    }
    svg += '<text x="' + (g.left + 4) + '" y="' + (g.demy + 17) + '" font-size="11" fill="var(--muted)">demand</text>'
      + '<text x="' + (g.left + 4) + '" y="' + (g.vy + 17) + '" font-size="11" fill="var(--cyan)">v</text>';
    for (j = 0; j < n; j += 1) {
      var cxj = g.x0 + j * g.cw + g.cw / 2;
      svg += '<text x="' + cxj + '" y="' + (g.demy + 17) + '" font-size="12" fill="var(--text)" '
        + 'text-anchor="middle">' + Rshort(D[j]) + '</text>'
        + '<text x="' + cxj + '" y="' + (g.vy + 17) + '" font-size="12" fill="var(--cyan)" '
        + 'text-anchor="middle">' + (v[j] === null ? '?' : Rshort(v[j])) + '</text>';
    }

    /* The refused rectangle first, so the computed cycle draws over it. */
    if (it.rect && it.rect.cells && !it.rect.ok) {
      var rpts = it.rect.cells.map(function (c) { var q = box(g, c.i, c.j); return q.cx + ',' + q.cy; });
      svg += '<polygon points="' + rpts.join(' ') + '" fill="none" stroke="var(--muted)" '
        + 'stroke-width="1.5" stroke-dasharray="3 4" opacity="0.8" />';
      if (it.rect.corner) svg += ring(g, it.rect.corner.i, it.rect.corner.j, 'red', true);
    }
    if (it.cycle && it.cycle.cells) {
      var pts = it.cycle.cells.map(function (c) { var q = box(g, c.i, c.j); return q.cx + ',' + q.cy; });
      svg += '<polygon points="' + pts.join(' ') + '" fill="none" stroke="var(--purple)" stroke-width="2.5" />';
      for (k = 0; k < it.cycle.cells.length; k += 1) {
        var qc = box(g, it.cycle.cells[k].i, it.cycle.cells[k].j);
        svg += '<circle cx="' + qc.cx + '" cy="' + qc.cy + '" r="4" fill="var(--purple)" />';
      }
    }
    if (it.entering) svg += ring(g, it.entering.i, it.entering.j, 'cyan', false);
    if (it.cycle && it.cycle.leaving) svg += ring(g, it.cycle.leaving.i, it.cycle.leaving.j, 'red', false);
    svg += '<text x="' + g.left + '" y="' + (g.height - 6) + '" font-size="10" fill="var(--muted)">'
      + (it.optimal
          ? 'every empty cell prices at zero or above, so no cycle improves this tableau'
          : 'the path turns only at occupied cells; ' + Rshort(it.cycle && it.cycle.theta !== null
              ? it.cycle.theta : R0) + ' moves round it, added at + and taken at -')
      + '</text>';
    gridEl.innerHTML = svg;

    /* ---- theta over the minus cells ----------------------------------- */
    var trows = [];
    if (it.cycle && it.cycle.found && it.cycle.minus) {
      for (k = 0; k < it.cycle.minus.length; k += 1) {
        var mc = it.cycle.minus[k];
        var isLeaving = it.cycle.leaving && mc.i === it.cycle.leaving.i && mc.j === it.cycle.leaving.j;
        var leftOver = Rsub(mc.x, it.cycle.theta);
        var note = isLeaving ? 'the smallest, so this cell leaves'
          : (Rzero(leftOver)
              ? 'ties with the smallest, so it stays in the basis carrying zero -- a named epsilon cell'
              : 'larger, so it survives with ' + Rshort(leftOver) + ' left');
        trows.push(tr([rowhead(cellName(mc)), td(Rshort(mc.x)),
          td(note, isLeaving ? 'tone-red' : (Rzero(leftOver) ? 'tone-amber' : 'tone-muted'))]));
      }
    } else {
      trows.push(tr([rowhead('none'),
        td('&mdash;'), td(it.optimal ? 'this tableau is optimal, so there is no cycle to move round'
          : 'no cycle was found for the entering cell')]));
    }
    thetaEl.innerHTML = '<caption>&theta; is the smallest allocation on a minus corner &mdash; the ratio test, '
      + 'in tableau clothing</caption><thead>'
      + tr([th('minus cell'), th('allocation'), th('what &theta; does to it')]) + '</thead><tbody>'
      + trows.join('') + '</tbody>';

    /* ---- the normalisation, demonstrated ------------------------------ */
    var nrows = [], base = it.uv;
    var uCells = [rowhead('u, with u1 = 0')], u2Cells = [rowhead('u, with ' + normKind + (normIx + 1) + ' = 0')];
    for (i = 0; i < m; i += 1) {
      uCells.push(td(base.u[i] === null ? '?' : Rshort(base.u[i])));
      u2Cells.push(td(u[i] === null ? '?' : Rshort(u[i]), 'tone-cyan'));
    }
    var vCells = [rowhead('v, with u1 = 0')], v2Cells = [rowhead('v, with ' + normKind + (normIx + 1) + ' = 0')];
    for (j = 0; j < n; j += 1) {
      vCells.push(td(base.v[j] === null ? '?' : Rshort(base.v[j])));
      v2Cells.push(td(v[j] === null ? '?' : Rshort(v[j]), 'tone-cyan'));
    }
    while (uCells.length < Math.max(m, n) + 1) uCells.push(td(''));
    while (u2Cells.length < Math.max(m, n) + 1) u2Cells.push(td(''));
    while (vCells.length < Math.max(m, n) + 1) vCells.push(td(''));
    while (v2Cells.length < Math.max(m, n) + 1) v2Cells.push(td(''));
    nrows.push(tr(uCells), tr(u2Cells), tr(vCells), tr(v2Cells));
    var heads = [th('')];
    for (k = 0; k < Math.max(m, n); k += 1) heads.push(th(String(k + 1)));
    normEl.innerHTML = '<caption>Move the normalisation and every potential moves; the reduced costs do not'
      + (shift !== null && Rzero(shift.shift)
          ? ' &mdash; the slider is sitting on the normalisation the potentials were solved with, so the two '
            + 'pairs agree here; move it and they will not'
          : (Rsign(shift.shift) < 0
              ? ' &mdash; every u has gained ' + Rshort(Rneg(shift.shift)) + ' and every v has lost it'
              : ' &mdash; every u has lost ' + Rshort(shift.shift) + ' and every v has gained it'))
      + '</caption><thead>' + tr(heads) + '</thead><tbody>' + nrows.join('') + '</tbody>';

    /* ---- the readouts -------------------------------------------------- */
    setKpi('tmEnterK', it.entering
      ? cellName(it.entering) + ' at ' + Rshort(it.entering.value)
      : '<span class="tone-green">none &mdash; optimal</span>');
    setKpi('tmThetaK', it.cycle && it.cycle.theta !== null
      ? Rshort(it.cycle.theta) + (Rzero(it.cycle.theta)
          ? ' <span class="tone-amber">a degenerate pivot</span>' : '')
      : '&mdash;');
    setKpi('tmLeaveK', it.cycle && it.cycle.leaving ? cellName(it.cycle.leaving) : '&mdash;');
    setKpi('tmCostK', Rshort(it.cost)
      + (at + 1 < total ? ' &rarr; ' + Rshort(run.iterations[at + 1].cost) : ''));
    setKpi('tmCheckK', it.check
      ? (it.check.ok ? '<span class="tone-green">a legal cycle</span>'
          : '<span class="tone-red">refused</span>')
      : '&mdash;');
    setKpi('tmRectK', it.rect
      ? (it.rect.ok ? '<span class="tone-green">closes, and agrees</span>'
          : '<span class="tone-red">refused at ' + (it.rect.corner ? cellName(it.rect.corner) : 'the start') + '</span>')
      : '&mdash;');

    var lines = [];
    if (run.pad.added.length) lines.push(run.pad.why.charAt(0).toUpperCase() + run.pad.why.slice(1) + '.');
    lines.push('<strong>' + it.forest.why.charAt(0).toUpperCase() + it.forest.why.slice(1) + '</strong>, '
      + 'so u + v = c has exactly one solution once one potential is fixed.');
    if (it.optimal) {
      lines.push('No empty cell prices below zero, so this tableau is <strong>optimal at '
        + Rshort(it.cost) + '</strong>, reached in ' + (total - 1) + ' improvement '
        + (total === 2 ? 'step' : 'steps') + ' from the ' + start.rule + ' start.');
    } else if (it.cycle && it.cycle.found && it.check.ok) {
      lines.push('Cell ' + cellName(it.entering) + ' prices at ' + Rshort(it.entering.value)
        + ', so one unit sent there saves that much. ' + it.check.why.charAt(0).toUpperCase()
        + it.check.why.slice(1) + '. ' + it.cycle.why.charAt(0).toUpperCase() + it.cycle.why.slice(1) + '.');
      lines.push(it.rect.why.charAt(0).toUpperCase() + it.rect.why.slice(1) + '.');
    } else {
      lines.push('<span class="tone-red">' + (it.check ? it.check.why : 'no cycle was found') + '</span>');
    }
    statusEl.innerHTML = lines.join(' ');
  }

  [presetS, startS, ruleS].forEach(function (el) {
    el.addEventListener('change', function () { iterS.value = '0'; redraw(); });
  });
  [iterS, normS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="The simplex, rewritten for a tableau",
        subtitle="u and v price the empty cells, and a closed path of ±θ does the pivot",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Step one iteration at a time",
        panel_intro="The potentials solve u + v = c on the occupied cells, the reduced costs are "
        "c &minus; u &minus; v on the rest, and the cycle is found by a walk on the tree of occupied "
        "cells &mdash; not by looking for a rectangle, which the second iteration here does not have.",
    )


# ---------------------------------------------------------------------------
# Mode `hungarian` -- the reductions, and a cover computed by Koenig
# ---------------------------------------------------------------------------

MAX_ASSIGN = 6


def _hungarian(cfg):
    chosen = cfg.get("preset", "jobs")
    if chosen not in ASSIGN_PRESETS:
        raise ValueError(
            "transport_lab: mode 'hungarian' has no preset %r; the presets are %s"
            % (chosen, ", ".join(sorted(ASSIGN_PRESETS)))
        )
    here = ASSIGN_PRESETS[chosen]

    markup = (
        _toolbar(
            "Reduce, cover, adjust",
            "and the cover is a maximum matching, not a line count",
            [
                ("green", "a zero, and the matching that uses it"),
                ("amber", "covered by the minimum cover"),
                ("cyan", "the assignment finally made"),
                ("muted", "reduced entries above zero"),
            ],
        )
        + _stage(_svg("thGrid", "0 0 660 268",
                      "The reduced cost matrix with its zeros, the matching drawn on them, and the "
                      "covered rows and columns shaded."))
        + _table("thTrace")
        + _table("thDual")
        + _banner("thStatus")
    )
    controls = (
        _select("thPreset", "Worked example",
                [(k, ASSIGN_PRESETS[k]["label"]) for k in ("jobs", "sites", "crews")], chosen)
        + _text("thCost", "Cost matrix &mdash; rows separated by &ldquo;;&rdquo;", here["cost"])
        + _range("thStep", "Step of the method", 0, 6, 6, 1)
        + _kpis(
            [
                ("Maximum matching on the zeros", "thMatchK"),
                ("Minimum cover, by K&ouml;nig", "thCoverK"),
                ("Row and column constants add to", "thDualK"),
                ("The assignment costs", "thValueK"),
                ("Cheapest cell first gets", "thGreedyK"),
                ("Its gap", "thGapK"),
            ]
        )
        + _hint(
            "thHint",
            "The number of lines that covers every zero is a minimum vertex cover of the bipartite "
            "graph whose edges are the zero cells, and it equals the maximum matching on that graph. "
            "That is a theorem, proved from a minimum cut in "
            "<span class=\"chip\">algorithms/graph-algorithms/bipartite-matching-via-flow</span>, "
            "and it is why this lab never counts lines by eye.",
        )
    )

    script = _CORE_JS + _payload("PRESETS", ASSIGN_PRESETS) + _payload("MAXN", MAX_ASSIGN) + r"""
  var presetS = document.getElementById('thPreset');
  var costIn = document.getElementById('thCost');
  var stepS = document.getElementById('thStep');
  var gridEl = document.getElementById('thGrid');
  var traceEl = document.getElementById('thTrace');
  var dualEl = document.getElementById('thDual');
  var statusEl = document.getElementById('thStatus');
  var snapToEnd = false;

  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
  function blank(message) {
    gridEl.innerHTML = ''; traceEl.innerHTML = ''; dualEl.innerHTML = '';
    ['thMatchK', 'thCoverK', 'thDualK', 'thValueK', 'thGreedyK', 'thGapK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  function kindText(kind) {
    if (kind === 'rows') return 'row reduction';
    if (kind === 'cols') return 'column reduction';
    if (kind === 'adjust') return 'adjustment';
    return 'cover';
  }

  function redraw() {
    var cost = parseGrid(costIn.value), i, j, k;
    if (cost === null) {
      blank('Every entry has to be a number or a fraction such as 7/2, with rows separated by a semicolon.');
      return;
    }
    if (cost.length !== cost[0].length) {
      blank('An assignment problem needs as many rows as columns; this matrix is ' + cost.length
        + ' by ' + cost[0].length + '. Add a dummy row or column to square it up.');
      return;
    }
    if (cost.length > MAXN) {
      blank('This lab draws up to ' + MAXN + ' rows so the matching stays readable, and the matrix has '
        + cost.length + '.');
      return;
    }
    var n = cost.length;
    var h = hungarian(cost);
    var dual = assignDual(cost, h.reduced);
    var greedy = greedyAssign(cost);
    var total = h.steps.length;
    stepS.max = String(total - 1);
    if (snapToEnd) { stepS.value = String(total - 1); snapToEnd = false; }
    var at = Math.max(0, Math.min(total - 1, +stepS.value || 0));
    document.getElementById('thStepOut').textContent = (at + 1) + ' of ' + total + ', ' + kindText(h.steps[at].kind);
    var step = h.steps[at], M = step.M, finished = at === total - 1 && h.complete;

    /* The cover on this step, re-checked here rather than trusted. */
    var cover = step.kind === 'cover' ? coverCheck(M, step.cover) : null;
    /* The duals AT THIS STEP, recovered from this step's matrix: M_ij = c_ij - u_i - v_j
       holds after every reduction and every adjustment, so the same recovery works
       throughout and the reader watches the dual objective climb to the primal one. */
    var stepDual = assignDual(cost, M);
    var matched = {};
    if (step.kind === 'cover') for (k = 0; k < step.matching.length; k += 1) matched[step.matching[k][0]] = step.matching[k][1];

    /* ---- the matrix, drawn -------------------------------------------- */
    var left = 8, lab = 72, uw = 56;
    var cw = Math.floor((660 - left - lab - uw - 8) / n), ch = 46, top = 30;
    var x0 = left + lab, ux = x0 + n * cw, vy = top + n * ch, height = top + n * ch + 44;
    gridEl.setAttribute('viewBox', '0 0 660 ' + height);
    var svg = '';
    for (j = 0; j < n; j += 1) {
      svg += '<text x="' + (x0 + j * cw + cw / 2) + '" y="20" font-size="11" fill="var(--muted)" '
        + 'text-anchor="middle">task ' + (j + 1) + '</text>';
    }
    svg += '<text x="' + (ux + uw / 2) + '" y="20" font-size="11" fill="var(--cyan)" text-anchor="middle">u</text>';
    /* the covered bands first, so the numbers sit on top of them */
    if (cover) {
      for (i = 0; i < n; i += 1) if (cover.rows[i]) {
        svg += '<rect x="' + left + '" y="' + (top + i * ch) + '" width="' + (ux - left) + '" height="' + ch
          + '" fill="var(--amber)" opacity="0.16" />'
          + '<line x1="' + left + '" y1="' + (top + i * ch + ch / 2) + '" x2="' + ux + '" y2="'
          + (top + i * ch + ch / 2) + '" stroke="var(--amber)" stroke-width="2.5" />';
      }
      for (j = 0; j < n; j += 1) if (cover.cols[j]) {
        svg += '<rect x="' + (x0 + j * cw) + '" y="' + top + '" width="' + cw + '" height="' + (n * ch)
          + '" fill="var(--amber)" opacity="0.16" />'
          + '<line x1="' + (x0 + j * cw + cw / 2) + '" y1="' + top + '" x2="' + (x0 + j * cw + cw / 2)
          + '" y2="' + (top + n * ch) + '" stroke="var(--amber)" stroke-width="2.5" />';
      }
    }
    for (i = 0; i < n; i += 1) {
      svg += '<text x="' + (left + 4) + '" y="' + (top + i * ch + ch / 2 + 4) + '" font-size="11" '
        + 'fill="var(--muted)">worker ' + (i + 1) + '</text>';
      for (j = 0; j < n; j += 1) {
        var cellX = x0 + j * cw, cellY = top + i * ch, midX = cellX + cw / 2, midY = cellY + ch / 2;
        var zero = Rzero(M[i][j]);
        var assigned = finished && h.assignment[i] === j;
        svg += '<rect x="' + cellX + '" y="' + cellY + '" width="' + cw + '" height="' + ch
          + '" fill="none" stroke="var(--line)" stroke-width="1" />';
        if (assigned) {
          svg += '<rect x="' + (cellX + 2) + '" y="' + (cellY + 2) + '" width="' + (cw - 4) + '" height="'
            + (ch - 4) + '" rx="4" fill="var(--cyan)" opacity="0.18" stroke="var(--cyan)" stroke-width="2" />';
        }
        if (step.kind === 'cover' && matched[i] === j) {
          svg += '<circle cx="' + midX + '" cy="' + midY + '" r="13" fill="none" stroke="var(--green)" '
            + 'stroke-width="2" />';
        }
        svg += '<text x="' + midX + '" y="' + (midY + 4) + '" font-size="13" text-anchor="middle" fill="var(--'
          + (zero ? 'green' : 'muted') + ')" font-weight="' + (zero ? '700' : '400') + '">'
          + Rshort(M[i][j]) + '</text>';
        if (assigned) {
          svg += '<text x="' + (cellX + cw - 5) + '" y="' + (cellY + 13) + '" font-size="10" '
            + 'text-anchor="end" fill="var(--cyan)">costs ' + Rshort(cost[i][j]) + '</text>';
        }
      }
      svg += '<text x="' + (ux + uw / 2) + '" y="' + (top + i * ch + ch / 2 + 4) + '" font-size="12" '
        + 'fill="var(--cyan)" text-anchor="middle">' + Rshort(stepDual.u[i]) + '</text>';
    }
    svg += '<text x="' + (left + 4) + '" y="' + (vy + 17) + '" font-size="11" fill="var(--cyan)">v</text>';
    for (j = 0; j < n; j += 1) {
      svg += '<text x="' + (x0 + j * cw + cw / 2) + '" y="' + (vy + 17) + '" font-size="12" '
        + 'fill="var(--cyan)" text-anchor="middle">' + Rshort(stepDual.v[j]) + '</text>';
    }
    svg += '<text x="' + left + '" y="' + (height - 8) + '" font-size="10" fill="var(--muted)">'
      + (cover
          ? 'the amber lines are a minimum cover of size ' + cover.size + ', read off the matching of size '
            + step.matching.length + ' -- ' + (cover.ok ? 'and every zero lies on one'
              : 'BUT ' + cover.missed.length + ' zero(s) escape it, which would break the method')
          : 'u and v to the right and below are the constants taken off so far')
      + '</text>';
    gridEl.innerHTML = svg;

    /* ---- what each step did -------------------------------------------- */
    var rows = [];
    for (k = 0; k <= at; k += 1) {
      var s = h.steps[k];
      var detail = s.why;
      var size = s.kind === 'cover'
        ? '<strong>' + s.size + '</strong> lines = <strong>' + s.matching.length + '</strong> pairs'
        : (s.kind === 'adjust' ? 'smallest uncovered entry ' + Rshort(s.theta)
            : s.amounts.map(Rshort).join(', '));
      rows.push(tr([rowhead(kindText(s.kind)), tdl(detail), td(size, s.kind === 'cover' ? 'tone-green' : '')],
        k === at ? 'tone-cyan' : ''));
    }
    traceEl.innerHTML = '<caption>Every step so far, and the cover sizes it computed</caption><thead>'
      + tr([th('step'), th('what it did, and why it is allowed'), th('size')]) + '</thead><tbody>'
      + rows.join('') + '</tbody>';

    /* ---- the dual, added up, against the assignment --------------------- */
    var duRow = [rowhead('u (per worker)')], dvRow = [rowhead('v (per task)')], gRow = [rowhead('greedy picks')];
    for (i = 0; i < n; i += 1) duRow.push(td(Rshort(stepDual.u[i])));
    for (j = 0; j < n; j += 1) dvRow.push(td(Rshort(stepDual.v[j])));
    for (k = 0; k < greedy.order.length; k += 1) {
      gRow.push(td('(' + (greedy.order[k].i + 1) + ',' + (greedy.order[k].j + 1) + ') at '
        + Rshort(greedy.order[k].cost)));
    }
    while (duRow.length < n + 1) duRow.push(td(''));
    while (dvRow.length < n + 1) dvRow.push(td(''));
    while (gRow.length < n + 1) gRow.push(td(''));
    var dheads = [th('')];
    for (k = 0; k < n; k += 1) dheads.push(th(String(k + 1)));
    dualEl.innerHTML = '<caption>The constants taken off so far are a dual solution: they add to '
      + Rshort(stepDual.total) + ', and the assignment the method ends on costs ' + Rshort(h.value)
      + (Requ(stepDual.total, h.value) ? ' &mdash; the same number, which is where it stops'
          : ' &mdash; still below it, which is why there is another step')
      + '</caption><thead>' + tr(dheads) + '</thead><tbody>'
      + tr(duRow) + tr(dvRow) + tr(gRow) + '</tbody>';

    var gap = Rsub(greedy.value, h.value);
    setKpi('thMatchK', step.kind === 'cover' ? String(step.matching.length) + ' of ' + n
      : 'not computed at this step');
    setKpi('thCoverK', cover
      ? cover.size + (cover.size === n ? ' <span class="tone-green">enough</span>'
          : ' <span class="tone-amber">short of ' + n + '</span>')
      : '&mdash;');
    setKpi('thDualK', Rshort(stepDual.total)
      + (Requ(stepDual.total, dual.total) ? '' : ' so far')
      + (stepDual.feasible ? '' : ' <span class="tone-red">not dual feasible</span>'));
    setKpi('thValueK', Rshort(h.value)
      + (Requ(stepDual.total, h.value) ? ' <span class="tone-green">= the dual</span>' : ''));
    setKpi('thGreedyK', Rshort(greedy.value));
    setKpi('thGapK', Rzero(gap)
      ? '<span class="tone-amber">none, this time</span>'
      : '<span class="tone-red">' + Rshort(gap) + ' too much</span>');

    var parts = [];
    parts.push('<strong>' + kindText(step.kind).charAt(0).toUpperCase() + kindText(step.kind).slice(1)
      + ':</strong> ' + step.why + '.');
    if (cover) {
      parts.push('The lines are not counted by eye. The cover is read off the vertices an alternating '
        + 'search reaches from the unmatched rows, which is what makes it minimum and not merely small, and it '
        + 'is checked here: ' + cover.why + '.');
    }
    if (finished) {
      parts.push('The zeros now carry a complete assignment costing <strong>' + Rshort(h.value)
        + '</strong>, and the constants taken off the rows and columns add to ' + Rshort(dual.total)
        + ' &mdash; equal, which is strong duality on this instance and the check to run by hand.');
      parts.push(Rzero(gap)
        ? 'Taking the cheapest cell first happens to land on ' + Rshort(greedy.value)
          + ' here too. It is still not a method: it has no certificate, and on the crews-and-sites table '
          + 'it overspends.'
        : 'Taking the cheapest cell first commits to ' + (greedy.order.length
            ? '(' + (greedy.order[0].i + 1) + ',' + (greedy.order[0].j + 1) + ')' : 'its first pick')
          + ' and ends at ' + Rshort(greedy.value) + ', which is ' + Rshort(gap) + ' too much.');
    }
    statusEl.innerHTML = parts.join(' ');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    costIn.value = p.cost;
    snapToEnd = true;
    redraw();
  });
  costIn.addEventListener('input', function () { snapToEnd = true; redraw(); });
  stepS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Reduce the rows, reduce the columns, then count properly",
        subtitle="the minimum cover is a maximum matching, and the reductions are the dual",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Run the method one step at a time",
        panel_intro="Each step recomputes from the matrix in the box: the reductions, the maximum "
        "matching on the zero cells, the minimum cover K&ouml;nig&rsquo;s theorem reads off it, and the "
        "adjustment that creates a new zero without destroying the old ones.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "setup": _setup,
    "modi": _modi,
    "hungarian": _hungarian,
}

MODES = tuple(sorted(_MODES))


def transport_lab(cfg):
    """The tableau kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract. A kit that fell back to a default would render a
    finished-looking page carrying another lesson's widget: every markup
    assertion passes, labcheck passes, and the reader is shown the wrong
    arithmetic under the right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "transport_lab: unknown mode %r; the three modes of the tableau kit are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["transport_lab", "TRANSPORT_JS", "MODES", "TRANS_PRESETS", "ASSIGN_PRESETS", "MAX_ASSIGN"]
